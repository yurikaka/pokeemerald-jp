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
PATCH_GENERATED_GFX := patch/gfx/berry_tag_tiles.4bpp
PATCH_GFX := $(filter-out $(PATCH_GENERATED_GFX),$(wildcard patch/gfx/*.4bpp)) $(PATCH_GENERATED_GFX)
PATCH_RAW_TILEMAPS := patch/gfx/summary_effect_battle.bin patch/gfx/summary_effect_contest.bin
PATCH_TILEMAPS := $(filter-out $(PATCH_RAW_TILEMAPS),$(wildcard patch/gfx/*.bin))
PATCH_GFX_LZ := $(patsubst patch/gfx/%.4bpp,$(PATCH_BUILD)/%.lz,$(PATCH_GFX))
PATCH_TILEMAP_LZ := $(patsubst patch/gfx/%.bin,$(PATCH_BUILD)/%.lz,$(PATCH_TILEMAPS))
PATCH_RESOURCES_LZ := $(PATCH_GFX_LZ) $(PATCH_TILEMAP_LZ)
PATCH_BATCHES := $(wildcard patch/batches/*.json)
PATCH_TEXTS := patch/texts.json $(wildcard patch/bag_return_locations*.json patch/item_names.json patch/item_descriptions.json patch/move_names.json patch/type_names.json patch/pocket_names.json patch/move_descriptions.json patch/ability_names.json patch/ability_descriptions.json patch/berry_info.json patch/decoration_info.json patch/pokedex_entries.json patch/trainer_names.json patch/trainer_class_names.json) $(PATCH_BATCHES)

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

$(PATCH_BUILD)/texts.inc: $(PATCH_TEXTS) patch/charmap_chs.txt patch/tools/build_texts.py | $(PATCH_BUILD)
	$(PYTHON) patch/tools/build_texts.py patch/charmap_chs.txt $@ $(PATCH_TEXTS)

$(PATCH_BUILD)/chinese_normal.latfont: patch/fonts/chinese_normal.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/chinese_small.latfont: patch/fonts/chinese_small.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/latin_normal.latfont: patch/fonts/latin_normal.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/latin_small.latfont: patch/fonts/latin_small.png | $(PATCH_BUILD)
	$(GBAGFX) $< $@

patch/gfx/berry_tag_tiles.4bpp: patch/tools/build_berry_tag_gfx.py baserom_jp.gba
	$(PYTHON) patch/tools/build_berry_tag_gfx.py

$(PATCH_GFX_LZ): $(PATCH_BUILD)/%.lz: patch/gfx/%.4bpp | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_TILEMAP_LZ): $(PATCH_BUILD)/%.lz: patch/gfx/%.bin | $(PATCH_BUILD)
	$(GBAGFX) $< $@

$(PATCH_BUILD)/payload.o: patch/chinese_engine.s $(PATCH_BUILD)/texts.inc \
		$(PATCH_BUILD)/chinese_normal.latfont $(PATCH_BUILD)/chinese_small.latfont \
		$(PATCH_BUILD)/latin_normal.latfont $(PATCH_BUILD)/latin_small.latfont \
		$(PATCH_RESOURCES_LZ) $(PATCH_RAW_TILEMAPS)
	$(PATCH_AS) -mcpu=arm7tdmi -mthumb -o $@ $<

$(PATCH_ELF): $(PATCH_BUILD)/payload.o patch/payload.ld
	$(PATCH_LD) -T patch/payload.ld -Map $(PATCH_BUILD)/payload.map -o $@ $<

$(PATCH_BIN): $(PATCH_ELF)
	$(PATCH_OBJCOPY) -O binary $< $@

$(CHS_ROM): $(ROM) $(PATCH_ELF) $(PATCH_BIN) patch/manifest.json $(PATCH_BATCHES) patch/tools/apply_patch.py
	$(PYTHON) patch/tools/apply_patch.py --rom $(ROM) --output $@ \
		--payload-elf $(PATCH_ELF) --payload-bin $(PATCH_BIN) \
		--manifest patch/manifest.json --nm $(PATCH_ARM_PREFIX)nm \
		$(foreach batch,$(PATCH_BATCHES),--batch $(batch))
