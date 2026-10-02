#!/usr/bin/env python3
"""Port checklist strings with exact JP source and fixed literal evidence."""

import argparse
from collections import Counter
import json
from pathlib import Path
import struct
import subprocess
import warnings

from build_texts import convert_us_encoded_text, tokenize_line
from port_map_dialogue import encode_japanese, read_charmap
from review_text_checklists import ROOT, US, encode_source_controls, read_sources


JP_REGIONAL_TEXT = {
    "gText_WinsLosses": "胜：{CLEAR_TO 55}负：",
    "gText_FrontierFacilityClearStreak": "连续过关：{STR_VAR_1}",
    "gText_WinLoseDraw": "{CLEAR_TO 3}胜{CLEAR_TO 48}负{CLEAR_TO 96}平",
    "BattleFrontier_BattlePikeRoomNormal_Text_HowUnsportingOfYou": "这样啊……真遗憾……",
    "gText_ExitingChat": "因为没有参加者，\n聊天将结束！",
    "gTVWhatsNo1InHoennTodayText02": "{STR_VAR_1}今天在游戏厅\n玩了{STR_VAR_2}次轮盘游戏！\\p玩的时候双眼通红地大喊：\n“我看穿了小球的动向！”\\p据说当时的表情\n十分惊人。",
    "sText_Miss": "阿姨",
}

DYNAMIC_CALLERS = {
    "gText_AwesomeWonF701F700": "../pokeemerald_wokann_dev/src/pokemon_jump.c:2724: PrintPrizeMessage uses CopyItemName in slot 0 and ConvertIntToDecimalStringN in slot 1; itemName/itemQuantityStr are 64 bytes and prizeMsg is 256 bytes.",
    "gText_FirstPlacePrize": "../pokeemerald_wokann_dev/src/dodrio_berry_picking.c:4670: CopyItemName populates gStringVar1 and DynamicPlaceholderTextUtil_SetPlaceholderPtr slot 0 before message expansion; gStringVar4 is the output.",
    "gText_F700JoinedChat": "../pokeemerald_wokann_dev/src/union_room_chat.c:1406: ProcessReceivedChatMessage supplies the original received player name in slot 0, expands into receivedMessage[64] (caller at 1618); only the display template is redirected.",
    "gText_F700LeftChat": "../pokeemerald_wokann_dev/src/union_room_chat.c:1423: ProcessReceivedChatMessage supplies the original received player name in slot 0, expands into receivedMessage[64]; hostName is copied before template expansion and remains unmodified.",
    "gText_LeaderLeftEndingChat": "../pokeemerald_wokann_dev/src/union_room_chat.c:2174: GetChatHostName supplies slot 0; AddStdMessageWindow at 2371 expands into expandedPlaceholdersBuffer[0x106], without rewriting hostName or link player names.",
    "gText_RibbonsF700": "../pokeemerald_wokann_dev/src/pokenav_ribbons_summary.c:980: PrintCurrentMonRibbonCount converts the count into gStringVar1, assigns dynamic slot 0, expands into gStringVar4 and draws the count window; no ribbon/save field is written.",
    "gText_F700sQuiz": "../pokeemerald_wokann_dev/src/easy_chat.c:5060: sub_0811C5F4 reads the quiz author at SaveBlock1+0x3B70 or gText_Lady into slot 0. Caller at 2006 expands into the 32-byte screen title region +0x14..+0x33; it does not modify the saved quiz author.",
    "sText_TrainerCardInfoPage1": "../pokeemerald_wokann_dev/src/union_room.c:4541: ViewURoomPartnerTrainerCard provides slots 0 class, 1 original playerName, 2 card color, 3 dex count, 4 hours, 5 minutes; expands into trainerCardMsgStrBuffer[200] then copies to gStringVar4. Received trainerCard fields are only read.",
    "sText_TrainerCardInfoPage2": "../pokeemerald_wokann_dev/src/union_room.c:4570: ViewURoomPartnerTrainerCard replaces slots 0 wins, 2 losses, 3 trades and 4..7 easy-chat words in temporary buffers, expands into trainerCardMsgStrBuffer[200], and appends the display text to gStringVar4. It never rewrites the trainer card profile or statistics.",
    "sText_FinishedCheckingPlayersTrainerCard": "../pokeemerald_wokann_dev/src/union_room.c:4593: ViewURoomPartnerTrainerCard retains slot 1 as trainerCard->playerName, expands this final display sentence into trainerCardMsgStrBuffer[200], and appends it to gStringVar4; original received playerName is unmodified.",
}

BATTLE_CALLERS = {
    "gText_BattleRecordedOnPass": {
        "ids": {0x23},
        "source": "../pokeemerald_wokann_dev/src/battle_main.c:1992 calls TryGetStatusString then draws gDisplayedStringBattle. battle_message.c:3507 expands the battle template; placeholder 0x23 selects _0814F2BC, reading the local save playerName or link player name into the display string without a persistent write.",
    },
}

REVIEWED_BATTLE_NAME_SLOTS = {
    "sText_InGamePartnerSentOutZGoN": {5, 7, 50, 51},
    "sText_LinkPartnerSentOutPkmnGoPkmn": {9, 11, 31},
    "sText_LinkTrainer2WithdrewPkmn": {0, 34},
    "sText_PlayerBattledToDrawTrainer1": {28, 29},
    "sText_PlayerLostAgainstTrainer1": {28, 29},
    "sText_Trainer2SentOutPkmn": {0, 46, 47},
    "sText_TwoTrainersSentPkmn": {6, 8, 28, 29, 46, 47},
    "sText_TwoTrainersWantToBattle": {28, 29, 46, 47},
    "sText_TwoWildFled": {32, 33},
    "sText_WildFled": {32},
}

PERSISTENT_NAME_REFERENCES = {
    0x08070444: "../pokeemerald_wokann_dev/src/daycare.c:2230: CreateEgg passes gText_EggNickname to SetMonData(MON_DATA_NICKNAME).",
    0x080704C8: "../pokeemerald_wokann_dev/src/daycare.c:2313: SetInitialEggData passes gText_EggNickname to SetMonData(MON_DATA_NICKNAME).",
}

COMPUTED_NAME_REFERENCES = {
    0x0807F8F8,
    0x0807F908,
    0x0807F950,
    0x0807F9A8,
}

UNSAFE_SHARED_NAME_TABLES = {
    ".rodata.pokeblock_name_table_data": "Wokann src/pokeblock.c sub_08135F30 copies a name into a 24-byte list label, then starts the level suffix at dest+9. Chinese names exceed the nine-byte prefix. sub_08136CEC also copies table names into gBattleTextBuff1. Preserve the shared JP table until all bounded consumers are adapted.",
}


def write_patch(path, document):
    new = json.dumps(document, ensure_ascii=False, indent=2) + "\n"
    if path.exists():
        old = path.read_text()
        if old == new:
            return
        body = "*** Update File: " + str(path) + "\n@@\n"
        body += "".join("-" + line + "\n" for line in old.splitlines())
    else:
        body = "*** Add File: " + str(path) + "\n"
    body += "".join("+" + line + "\n" for line in new.splitlines())
    subprocess.run(["apply_patch"], input="*** Begin Patch\n" + body + "*** End Patch\n", text=True, check=True)


def main():
    warnings.filterwarnings("ignore", category=SyntaxWarning)
    parser = argparse.ArgumentParser()
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--batch", required=True)
    parser.add_argument("--objects", type=Path)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--common-placeholders", action="store_true")
    args = parser.parse_args()
    review = json.loads(args.review.read_text())
    plan = json.loads(args.plan.read_text())
    reviewed = {(record["kind"], record["document_line"]): record for record in review["records"]}
    object_references = {}
    if args.objects:
        for reference in json.loads(args.objects.read_text())["references"]:
            object_references.setdefault(reference["original"], []).append(reference)
    sources = read_sources(US)
    charmap = read_charmap(US / "charmap.txt")
    rom = (ROOT / "baserom_jp.gba").read_bytes()
    baseline = args.baseline.read_bytes()
    if len(baseline) < len(rom):
        raise ValueError("baseline ROM is shorter than the JP base ROM")
    used = {}
    for path in (ROOT / "patch/batches").glob("*.json"):
        for reference in json.loads(path.read_text()).get("reference_writes", []):
            used[int(reference["address"], 0)] = {"batch": str(path.relative_to(ROOT)), **reference}
    batch = {"texts": [], "reference_writes": []}
    mappings = []
    counts = Counter()
    for record in plan["records"]:
        if record["kind"] != "port":
            continue
        if record["decision"] in ("already_ported_pokedex", "already_ported_structured"):
            continue
        latest = reviewed[(record["kind"], record["document_line"])]
        record["verified_code_references"] = latest.get("verified_code_references", [])
        record["exact_jp_source_match"] = latest.get("exact_jp_source_match", [])
        object_candidates = object_references.get(record.get("jp_address"), [])
        unsafe_candidates = [reference for reference in object_candidates if reference.get("section") in UNSAFE_SHARED_NAME_TABLES]
        if unsafe_candidates:
            record["bounded_shared_name_table_gate"] = [
                {"address": reference["address"], "reason": UNSAFE_SHARED_NAME_TABLES[reference["section"]]}
                for reference in unsafe_candidates
            ]
        object_candidates = [reference for reference in object_candidates if reference.get("section") not in UNSAFE_SHARED_NAME_TABLES]
        object_candidates = [reference for reference in object_candidates if record["exact_jp_source_match"] or reference["referenced_symbol"] == record["symbol"]]
        record["verified_object_references"] = object_candidates
        if not record["exact_jp_source_match"] and not object_candidates:
            continue
        symbol = record["symbol"]
        candidates = sources.get(symbol, [])
        if len(candidates) != 1:
            continue
        text = JP_REGIONAL_TEXT.get(symbol, candidates[0]["text"].split("$")[0])
        record["final_text"] = text
        if not text.strip():
            record["remaining_verification"] = ["Empty strings can be sentinels; preserve the original EOS-only bytes, rather than inserting a language control prefix."]
            continue
        references = list({reference["address"]: reference for reference in [*record["verified_code_references"], *object_candidates]}.values())
        if not references:
            continue
        encoded = encode_source_controls(text + "$", charmap)
        if encoded is None:
            counts["encoding_gate"] += 1
            continue
        converted = convert_us_encoded_text(encoded, set(), False)
        tokens = tokenize_line(converted)
        placeholders = {token[1] for token, width in tokens if token[0] == 0xFD}
        dynamic = any(token[0] == 0xF7 for token, width in tokens)
        common = args.common_placeholders and candidates[0]["file"] != "src/battle_message.c" and placeholders.issubset({1, 2, 3, 4}) and not dynamic
        reviewed_dynamic = dynamic and symbol in DYNAMIC_CALLERS and not placeholders
        reviewed_battle = symbol in BATTLE_CALLERS and placeholders == BATTLE_CALLERS[symbol]["ids"] and not dynamic
        if symbol in REVIEWED_BATTLE_NAME_SLOTS and placeholders == REVIEWED_BATTLE_NAME_SLOTS[symbol] and not dynamic:
            expected_slots = REVIEWED_BATTLE_NAME_SLOTS[symbol]
            original_slots = set()
            for proof in record["exact_jp_source_match"]:
                original = bytes.fromhex(proof["encoded_hex"]) if "encoded_hex" in proof else encode_source_controls(proof["text"].split("$")[0] + "$", charmap)
                if original is not None:
                    original_slots.update(original[position + 1] for position in range(len(original) - 1) if original[position] == 0xFD)
            reviewed_battle = original_slots == expected_slots
        if (placeholders or dynamic) and not common and not reviewed_dynamic and not reviewed_battle:
            gate = "Dynamic text: verify producer and JP layout before a new literal override."
            if gate not in record.setdefault("remaining_verification", []):
                record["remaining_verification"].append(gate)
            counts["dynamic_gate"] += 1
            continue
        target = int(record["jp_address"], 0)
        accepted = []
        existing = []
        for reference in references:
            address = int(reference["address"], 0)
            capacity = reference.get("source", {}).get("display_buffer_size") if isinstance(reference.get("source"), dict) else None
            if capacity and (placeholders or dynamic or len(converted) > capacity):
                record.setdefault("bounded_display_buffer_gate", {})[reference["address"]] = {"capacity": capacity, "template_bytes": len(converted), "policy": "Do not redirect this bounded display buffer until worst-case expanded length is verified."}
                continue
            if address in COMPUTED_NAME_REFERENCES:
                record.setdefault("computed_reference_gate", {})[reference["address"]] = "Wokann berry_blender.c sub_0807F888 uses contiguous six-byte names and pointer subtraction; preserve the original block until display consumers are separately ported."
                continue
            if address in PERSISTENT_NAME_REFERENCES:
                exclusion = {"address": reference["address"], "reason": PERSISTENT_NAME_REFERENCES[address]}
                exclusions = record.setdefault("excluded_persistent_references", [])
                if exclusion not in exclusions:
                    exclusions.append(exclusion)
                continue
            if address in used:
                existing.append(used[address])
                continue
            prior = struct.unpack_from("<I", baseline, address - 0x08000000)[0]
            if prior != target:
                record.setdefault("existing_override_conflicts", []).append({"address": reference["address"], "original": record["jp_address"], "baseline_word": f"0x{prior:08X}"})
                continue
            if (address % 4 and reference.get("relocation") != "event_msgbox_word") or struct.unpack_from("<I", rom, address - 0x08000000)[0] != target:
                raise ValueError((symbol, reference))
            accepted.append(reference)
        if existing:
            record["existing_verified_references"] = existing
        if not accepted:
            continue
        name = "Chs_ChecklistLiteral_" + args.batch.split("_")[0] + "_" + symbol
        definition = {"name": name, "source_symbol": symbol, "us_encoded_hex": encoded.hex()}
        if reviewed_dynamic:
            definition["japanese_dynamic"] = True
            record["placeholder_contract"] = {"source": DYNAMIC_CALLERS[symbol], "policy": "Wrap expanded F7 slots in JPN and restore ENG. Original names and numeric slots retain their JP encoding; translated item-name strings carry their own ENG prefix. Only the display template is redirected; producer buffers and persistent fields are unmodified."}
        if placeholders:
            definition["japanese_placeholders"] = sorted(placeholders)
            record["placeholder_contract"] = {"source": "../pokeemerald_wokann_dev/src/string_util.c:327", "ids": sorted(placeholders), "policy": "StringExpandPlaceholders recursively copies playerName/gStringVar1..3 and preserves JPN/ENG controls. Japanese buffers require JPN; translated table/name buffers carry their own ENG/F5 prefix; outer ENG is restored after each placeholder. Battle and F7 dynamic substitution are excluded."}
            if reviewed_battle:
                source = BATTLE_CALLERS[symbol]["source"] if symbol in BATTLE_CALLERS else "../pokeemerald_wokann_dev/src/battle_message.c:3560: Native placeholder jump table at _0814E818; the US and exact JP template use identical slot IDs. Slots 5..11 read mon display names, 28/29 and 46/47 read trainer class/name, 31..34 read link player names, 50/51 read partner class/name; slot 0 expands the existing battle buffer. The template-selector path uses the independently verified literal/object reference listed below and passes it to TryGetStatusString at 3493."
                record["placeholder_contract"] = {"source": source, "ids": sorted(placeholders), "policy": "Each reviewed name/battle-buffer slot is wrapped in JPN and ENG is restored after expansion; already-translated names retain their own language prefix. Only the display template pointer changes; mon, save, link and battle-buffer producers remain unmodified."}
        if candidates[0]["file"].startswith("data/"):
            definition["auto_wrap"] = True
        batch["texts"].append(definition)
        for reference in accepted:
            entry = {"address": reference["address"], "original": record["jp_address"], "symbol": name, "source_symbol": symbol}
            batch["reference_writes"].append(entry)
            used[int(entry["address"], 0)] = entry
        record["execution"] = "ported_verified_literal"
        record["remaining_verification"] = [gate for gate in record.get("remaining_verification", []) if gate != "Dynamic text: verify producer and JP layout before a new literal override."]
        record["executed_batch"] = args.batch
        record["execution_references"] = accepted
        mappings.append({"symbol": symbol, "document_line": record["document_line"], "jp_source": record["exact_jp_source_match"], "references": accepted, "final_text": text, "placeholder_contract": record.get("placeholder_contract"), "language_options": {key: value for key, value in definition.items() if key in ("japanese_placeholders", "japanese_dynamic", "initial_japanese")}})
        counts["ported_verified_literal"] += 1
    if batch["texts"]:
        write_patch(ROOT / "patch/batches" / args.batch, batch)
        write_patch(ROOT / "patch/mapping_reports" / args.batch, {"policy": "Exact Wokann JP source bytes and literal/typed-object references; only explicitly reviewed placeholder producers are permitted; existing writes, persistent nickname constructors and computed Blender name blocks are excluded.", "mapping": mappings})
    plan["literal_execution_summary"] = dict(counts)
    write_patch(args.plan, plan)
    print(dict(counts))


if __name__ == "__main__":
    main()
