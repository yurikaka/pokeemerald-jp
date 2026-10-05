"""Check restored Pokemon graphics damaged by the batch 219 false matches."""

from pathlib import Path

from build_berry_tag_gfx import lzdec


ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT.parent / "pokeemerald_wokann_dev"


def main():
    base = (ROOT / "baserom_jp.gba").read_bytes()
    patched = (ROOT / "pokeemerald_jp_chs.gba").read_bytes()
    animation_source = (REFERENCE / "data/data_b2d_gfx_front.s").read_text()
    static_source = (REFERENCE / "src/data/graphics/pokemon.h").read_text()
    for species in ("dusclops", "shedinja"):
        for filename in ("front.4bpp.lz", "anim_front.4bpp.lz", "back.4bpp.lz",
                         "normal.gbapal.lz", "shiny.gbapal.lz", "icon.4bpp",
                         "footprint.1bpp"):
            relative = f"graphics/pokemon/{species}/{filename}"
            declaration = animation_source if filename == "anim_front.4bpp.lz" else static_source
            if f'"{relative}"' not in declaration:
                raise ValueError(f"Missing Wokann graphics declaration: {relative}")
            original = (REFERENCE / relative).read_bytes()
            start = base.find(original)
            if start < 0 or base.find(original, start + 1) >= 0:
                raise ValueError(f"Resource is not uniquely located: {relative}")
            if patched[start:start + len(original)] != original:
                raise ValueError(f"Changed Pokemon graphics: {relative}")
            if filename.endswith(".lz"):
                address = start + 0x08000000
                if lzdec(base, address) != lzdec(patched, address):
                    raise ValueError(f"Changed decompressed resource: {relative}")
        print(f"{species}: all seven graphics resources match original Japanese ROM")


if __name__ == "__main__":
    main()
