AS := tools/binutils/bin/arm-none-eabi-as
LD := tools/binutils/bin/arm-none-eabi-ld
OBJCOPY := tools/binutils/bin/arm-none-eabi-objcopy
SHA1SUM := sha1sum -c
GBAFIX := tools/gbafix/gbafix

ASFLAGS := -mcpu=arm7tdmi

ASFILE := $(wildcard asm/*.s data/*.s)
OBJFILE := $(ASFILE:.s=.o)
NAME := pokeemerald_jp
ROM := $(NAME).gba
ELF := $(NAME).elf
CHS_ROM := $(NAME)_chs.gba
TITLE := POKEMON EMER
GAMECODE := BPEJ

PYTHON ?= python3
PATCH_ARM_PREFIX ?= arm-none-eabi-
PATCH_AS := $(PATCH_ARM_PREFIX)as
PATCH_LD := $(PATCH_ARM_PREFIX)ld
PATCH_OBJCOPY := $(PATCH_ARM_PREFIX)objcopy
GBAGFX ?= tools/gbagfx/gbagfx
PATCH_BUILD := build/patch
PATCH_ELF := $(PATCH_BUILD)/payload.elf
PATCH_BIN := $(PATCH_BUILD)/payload.bin
PATCH_MENU_INFO_US_GFX := $(PATCH_BUILD)/menu_info_us.4bpp
PATCH_BERRY_FIX_GFX := $(foreach scene,0 1 2 3 4 5,patch/gfx/berry_fix_$(scene)_tiles.4bpp patch/gfx/berry_fix_$(scene)_map.4bpp)
PATCH_BERRY_FIX_PALS := $(foreach scene,0 1 2 3 4 5,patch/gfx/berry_fix_$(scene).gbapal)
PATCH_GENERATED_GFX := patch/gfx/berry_tag_tiles.4bpp $(PATCH_BERRY_FIX_GFX) patch/gfx/contest_interface.4bpp patch/gfx/contest_applause.4bpp patch/gfx/contest_results.4bpp patch/gfx/contest_next_turn.4bpp
PATCH_RAW_GFX := patch/gfx/menu_info_tiles.4bpp patch/gfx/battle_status_tiles.4bpp patch/gfx/mon_markings_menu.4bpp patch/gfx/bag_hm_icon.4bpp
PATCH_GENERATED_GFX += patch/gfx/storage_menu.4bpp
PATCH_GFX := $(filter-out $(PATCH_GENERATED_GFX) $(PATCH_RAW_GFX),$(wildcard patch/gfx/*.4bpp)) $(PATCH_GENERATED_GFX)
PATCH_CONTEST_TITLES := $(addprefix patch/gfx/contest_title_,$(addsuffix .bin,normal super hyper master link cool beauty cute smart tough title))
PATCH_RAW_TILEMAPS := patch/gfx/summary_effect_battle.bin patch/gfx/summary_effect_contest.bin $(PATCH_CONTEST_TITLES)
PATCH_TILEMAPS := $(filter-out $(PATCH_RAW_TILEMAPS),$(wildcard patch/gfx/*.bin))
PATCH_GFX_LZ := $(patsubst patch/gfx/%.4bpp,$(PATCH_BUILD)/%.lz,$(PATCH_GFX))
PATCH_TILEMAP_LZ := $(patsubst patch/gfx/%.bin,$(PATCH_BUILD)/%.lz,$(PATCH_TILEMAPS))
PATCH_RESOURCES_LZ := $(PATCH_GFX_LZ) $(PATCH_TILEMAP_LZ)
PATCH_NAMING_GFX := $(addprefix $(PATCH_BUILD)/naming_screen_,$(addsuffix .4bpp,back_button ok_button))
PATCH_BATCHES := $(wildcard patch/batches/*.json)
PATCH_TEXTS := patch/texts.json $(wildcard patch/bag_return_locations*.json patch/item_names.json patch/item_descriptions.json patch/move_names.json patch/type_names.json patch/pocket_names.json patch/move_descriptions.json patch/ability_names.json patch/ability_descriptions.json patch/berry_info.json patch/battle_stat_names.json patch/level_up_stat_names.json patch/decoration_info.json patch/pokedex_entries.json patch/region_map_names.json patch/species_names.json patch/trainer_names.json patch/trainer_class_names.json) $(PATCH_BATCHES)

.PHONY: all chs patch-payload compare clean

all: $(ROM)

chs: $(CHS_ROM)

patch-payload: $(PATCH_BIN)

compare: $(ROM)
	$(SHA1SUM) rom_jp.sha1

clean:
	rm -f $(ROM) $(ELF) $(OBJFILE) $(CHS_ROM)
	rm -rf $(PATCH_BUILD)

$(ROM): $(ELF)
	$(OBJCOPY) -O binary $< $@

$(ELF): %.elf: $(OBJFILE) ld_script_jp.txt
	$(LD) -T ld_script_jp.txt -Map $*.map -o $@ $(OBJFILE)
	$(GBAFIX) -t"$(TITLE)" -c$(GAMECODE) -m01 --silent $@

$(OBJFILE): %.o: %.s
	$(AS) $(ASFLAGS) -o $@ $<

$(PATCH_BUILD):
	mkdir -p $@

$(PATCH_BUILD)/texts.inc $(PATCH_BUILD)/trainer_names_inline.bin &: $(PATCH_TEXTS) patch/charmap_chs.txt patch/tools/build_texts.py ../pokeemerald_us_chs/src/data/decoration/header.h ../pokeemerald_us_chs/src/data/decoration/description.h | $(PATCH_BUILD)
	$(PYTHON) patch/tools/build_texts.py patch/charmap_chs.txt $(PATCH_BUILD)/texts.inc $(PATCH_TEXTS)

$(PATCH_BUILD)/chinese_normal.latfont: patch/fonts/chinese_normal.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/chinese_small.latfont: patch/fonts/chinese_small.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/muzaipixel_chinese.latfont: patch/fonts/muzaipixel_chinese.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/muzaipixel_latin.latfont: patch/fonts/muzaipixel_latin.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/latin_normal.latfont: patch/fonts/latin_normal.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/latin_small.latfont: patch/fonts/latin_small.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

patch/gfx/berry_tag_tiles.4bpp: patch/tools/build_berry_tag_gfx.py baserom_jp.gba
	$(PYTHON) patch/tools/build_berry_tag_gfx.py

$(PATCH_MENU_INFO_US_GFX): ../pokeemerald_us_chs/graphics/interface/menu_info.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

patch/gfx/menu_info_tiles.4bpp: patch/tools/build_menu_info_gfx.py baserom_jp.gba $(PATCH_MENU_INFO_US_GFX)
	$(PYTHON) patch/tools/build_menu_info_gfx.py $(PATCH_MENU_INFO_US_GFX)

patch/gfx/battle_status_tiles.4bpp: patch/tools/build_battle_status_gfx.py baserom_jp.gba ../pokeemerald_us_chs/graphics/interface/status_icons.png
	$(PYTHON) patch/tools/build_battle_status_gfx.py

patch/gfx/mon_markings_menu.4bpp: patch/tools/build_markings_menu_gfx.py baserom_jp.gba patch/fonts/chinese_normal.png
	$(PYTHON) patch/tools/build_markings_menu_gfx.py

patch/gfx/bag_hm_icon.4bpp: patch/tools/build_bag_hm_icon.py patch/tools/build_berry_tag_gfx.py baserom_jp.gba ../pokeemerald_us_chs/graphics/bag/hm.png ../pokeemerald_wokann_dev/src/data/item_menu_data.c | $(PATCH_BUILD)
	$(PYTHON) patch/tools/build_bag_hm_icon.py

patch/gfx/wallclock.4bpp: patch/tools/build_wallclock_gfx.py baserom_jp.gba ../pokeemerald_wokann_dev/graphics/wallclock/clock.png.4bpp.lz ../pokeemerald_wokann_dev/graphics/wallclock/clock_start.bin ../pokeemerald_wokann_dev/graphics/wallclock/clock_view.bin
	$(PYTHON) patch/tools/build_wallclock_gfx.py

patch/gfx/contest_interface.4bpp patch/gfx/contest_applause.4bpp patch/gfx/contest_results.4bpp patch/gfx/contest_next_turn.4bpp $(PATCH_CONTEST_TITLES) &: patch/tools/build_contest_gfx.py patch/tools/build_berry_tag_gfx.py baserom_jp.gba ../pokeemerald_us_chs/graphics/contest/interface.png ../pokeemerald_us_chs/graphics/contest/applause.png ../pokeemerald_us_chs/graphics/contest/nextturn.png ../pokeemerald_us_chs/graphics/contest/results_screen/tiles.png $(wildcard ../pokeemerald_us_chs/graphics/contest/results_screen/title*.bin) $(wildcard ../pokeemerald_wokann_dev/graphics/contest/results_screen/*.lz) ../pokeemerald_wokann_dev/graphics/contest/interface.png.4bpp.lz ../pokeemerald_wokann_dev/graphics/contest/applause.4bpp.lz ../pokeemerald_wokann_dev/graphics/contest/nextturn.4bpp.lz
	$(PYTHON) patch/tools/build_contest_gfx.py

$(PATCH_BERRY_FIX_GFX) $(PATCH_BERRY_FIX_PALS) &: patch/tools/build_berry_fix_gfx.py patch/tools/build_berry_tag_gfx.py patch/tools/build_texts.py patch/fonts/chinese_small.png patch/fonts/latin_small.png patch/charmap_chs.txt baserom_jp.gba ../pokeemerald_us_chs/src/berry_fix_program.c ../pokeemerald_wokann_dev/src/berry_fix_graphics.c | $(PATCH_BUILD)
	$(PYTHON) patch/tools/build_berry_fix_gfx.py

$(PATCH_GFX_LZ): $(PATCH_BUILD)/%.lz: patch/gfx/%.4bpp | $(PATCH_BUILD)
	$(GBAGFX) $< $@

patch/gfx/easy_chat_mode.4bpp: patch/tools/build_easy_chat_mode_gfx.py patch/tools/build_berry_fix_gfx.py patch/tools/build_berry_tag_gfx.py patch/fonts/chinese_small.png patch/fonts/latin_small.png patch/charmap_chs.txt baserom_jp.gba ../pokeemerald_wokann_dev/graphics/easy_chat/mode.png.4bpp.lz
	$(PYTHON) patch/tools/build_easy_chat_mode_gfx.py

patch/gfx/storage_menu.4bpp: patch/tools/build_storage_menu_gfx.py patch/tools/build_berry_tag_gfx.py baserom_jp.gba ../pokeemerald_us_chs/graphics/pokemon_storage/menu.png ../pokeemerald_us_chs/graphics/pokemon_storage/display_menu.bin ../pokeemerald_wokann_dev/data/pokemon_storage/jp/0854BF9C.bin
	$(PYTHON) patch/tools/build_storage_menu_gfx.py

$(PATCH_BUILD)/storage_party.lz: ../pokeemerald_us_chs/graphics/pokemon_storage/party_menu.bin | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/payload.o: $(PATCH_BUILD)/storage_party.lz

$(PATCH_BUILD)/easy_chat_footer_tiles.4bpp $(PATCH_BUILD)/easy_chat_footer_map.bin &: patch/tools/build_easy_chat_footer_gfx.py patch/tools/build_berry_fix_gfx.py patch/fonts/chinese_small.png patch/fonts/latin_small.png patch/charmap_chs.txt baserom_jp.gba ../pokeemerald_us_chs/src/strings.c | $(PATCH_BUILD)
	$(PYTHON) patch/tools/build_easy_chat_footer_gfx.py

$(PATCH_BUILD)/easy_chat_footer_tiles.lz: $(PATCH_BUILD)/easy_chat_footer_tiles.4bpp
	$(GBAGFX) $< $@

$(PATCH_BUILD)/easy_chat_footer_map.lz: $(PATCH_BUILD)/easy_chat_footer_map.bin
	$(GBAGFX) $< $@

$(PATCH_TILEMAP_LZ): $(PATCH_BUILD)/%.lz: patch/gfx/%.bin | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/naming_screen_%.4bpp: ../pokeemerald_us_chs/graphics/naming_screen/%.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/trade_label_Cancel.4bpp $(PATCH_BUILD)/trade_label_ChooseAPkmn.4bpp $(PATCH_BUILD)/trade_label_CancelTrade.4bpp $(PATCH_BUILD)/trade_label_PressBToQuit.4bpp $(PATCH_BUILD)/trade_label_IsThisTradeOkay.4bpp &: patch/tools/build_trade_menu_text.py patch/tools/build_berry_fix_gfx.py patch/fonts/chinese_normal.png patch/fonts/latin_normal.png patch/charmap_chs.txt ../pokeemerald_us_chs/src/data/trade.h | $(PATCH_BUILD)
	$(PYTHON) patch/tools/build_trade_menu_text.py

$(PATCH_BUILD)/payload.o: patch/chinese_engine.s $(PATCH_BUILD)/texts.inc \
		$(PATCH_BUILD)/trade_label_Cancel.4bpp $(PATCH_BUILD)/trade_label_ChooseAPkmn.4bpp $(PATCH_BUILD)/trade_label_CancelTrade.4bpp $(PATCH_BUILD)/trade_label_PressBToQuit.4bpp $(PATCH_BUILD)/trade_label_IsThisTradeOkay.4bpp \
		$(PATCH_BUILD)/chinese_normal.latfont $(PATCH_BUILD)/chinese_small.latfont \
		$(PATCH_BUILD)/muzaipixel_chinese.latfont $(PATCH_BUILD)/muzaipixel_latin.latfont \
		patch/fonts/muzaipixel_latin_widths.bin \
		$(PATCH_BUILD)/latin_normal.latfont $(PATCH_BUILD)/latin_small.latfont \
		patch/gfx/title_logo.8bpp.lz patch/gfx/title_logo.bin.lz \
		patch/gfx/title_palette.gbapal patch/gfx/title_emerald.8bpp.lz \
		$(PATCH_RESOURCES_LZ) $(PATCH_RAW_TILEMAPS) $(PATCH_RAW_GFX) $(PATCH_NAMING_GFX) $(PATCH_BERRY_FIX_PALS) \
		$(PATCH_BUILD)/easy_chat_footer_tiles.lz $(PATCH_BUILD)/easy_chat_footer_map.lz
	$(PATCH_AS) -mcpu=arm7tdmi -mthumb -o $@ $<

$(PATCH_ELF): $(PATCH_BUILD)/payload.o patch/payload.ld
	$(PATCH_LD) -T patch/payload.ld -Map $(PATCH_BUILD)/payload.map -o $@ $<

$(PATCH_BIN): $(PATCH_ELF)
	$(PATCH_OBJCOPY) -O binary $< $@

$(CHS_ROM): $(ROM) $(PATCH_ELF) $(PATCH_BIN) patch/manifest.json $(PATCH_BATCHES) patch/tools/apply_patch.py $(PATCH_BUILD)/trainer_names_inline.bin
	$(PYTHON) patch/tools/apply_patch.py --rom $(ROM) --output $@ \
		--payload-elf $(PATCH_ELF) --payload-bin $(PATCH_BIN) \
		--manifest patch/manifest.json --nm $(PATCH_ARM_PREFIX)nm \
		$(foreach batch,$(PATCH_BATCHES),--batch $(batch))
