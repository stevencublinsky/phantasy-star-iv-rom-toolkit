# Phantasy Star IV - ROM Reverse Engineering Toolkit

Complete extraction, analysis, and rebuild toolkit for **Phantasy Star IV: The End of the Millennium** (Working Designs 6.01 retranslation patch).

---

## What's In This Repo

This project contains a full structural analysis of the PSIV Genesis/Mega Drive ROM, including decoded dialogue text, font extraction, graphics analysis, palette data, game data tables, and a complete rebuild guide.

| Directory | Contents |
|-----------|----------|
| `docs/` | All analysis reports, encoding guides, rebuild documentation |
| `data/text-encoding/` | Character table (.tbl) for the custom text encoding |
| `data/game-data/` | Items, techniques, skills, pointer tables |
| `data/dialogue/full/` | Complete decoded script (~5MB of dialogue) |
| `data/dialogue/by-scene/` | 3,999 individual scene files |
| `data/graphics/raw/` | Extracted graphics binaries from ROM |
| `data/graphics/analysis/` | Hex dump previews and byte frequency reports |
| `data/palettes/` | Genesis palette data (raw + RGB values) |
| `scripts/` | Python extraction tools (text, tiles, palettes, ROM map) |
| `visualizations/` | Font tile renders, ROM heat maps, palette previews |
| `research/` | Graphics modernization research report |

---

## ROM Details

| Property | Value |
|----------|-------|
| **Title** | Phantasy Star IV: The End of the Millennium |
| **Variant** | Phantasy Star Generation:4 - Working Designs 6.01 |
| **Platform** | Sega Genesis / Mega Drive |
| **Serial** | GM MK-1307 -00 |
| **Size** | 3,209,748 bytes (3.06 MB) - oversized from standard 2MB |
| **Format** | Raw BIN (no SMD interleave) |
| **Checksum** | 0x16F7 (stored) / 0xA496 (calculated) - patched ROM |
| **Header** | Valid SEGA GENESIS header at 0x100 |

This is a fan retranslation patch that adds ~1.1MB of new dialogue in the expanded ROM region (0x200000+).

---

## Key Discoveries

### Text Encoding (Cracked)
The retranslation uses a **custom single-byte encoding**:
- `0x00` = Space
- `0x01-0x1A` = A-Z (uppercase)
- `0x1B-0x34` = a-z (lowercase)
- `0x35-0x3B` = Punctuation (., '!?,-)
- `0x80-0xFF` = Control codes (scene markers, string ends, wait buttons)

See `docs/02-Text-Encoding-Guide.md` for the complete mapping.

### Font Tiles (Located)
- **Address**: 0x109400 - 0x10A400 (3 contiguous 2KB tables)
- **Format**: 1bpp 8x8 pixels (8 bytes per tile)
- **Total**: 768 tiles across 3 tables

### Dialogue (Fully Extracted)
- **4,849 scene markers** identified
- **13,353 dialogue strings** decoded
- **5,052,256 characters** of text

### Graphics Regions Identified
- 0x108400 - 0x10AC00: Font tile data (sparse 1bpp)
- 0x109400 - 0x10A400: Confirmed font tables
- 0x1155C4 - 0x1175D2: 8,206 byte low-byte data table
- 0x117603 - 0x119607: 8,196 byte low-byte data table

### Palettes Extracted
- 10 Genesis 9-bit BGR palettes extracted at offsets 0x0031F6 through 0x00729C

---

## Quick Start

### Decode Text from ROM
```bash
python scripts/extract_text.py \
  "Phantasy Star Gen4 - Working Designs 6.01.bin.md" \
  0x200000 0x30FA13 \
  data/text-encoding/psiv.tbl \
  output.txt
```

### Extract Tiles
```bash
python scripts/extract_tiles.py \
  "Phantasy Star Gen4 - Working Designs 6.01.bin.md" \
  0x109400 0x800 1bpp 8
```

### Generate ROM Map
```bash
python scripts/rom_map.py \
  "Phantasy Star Gen4 - Working Designs 6.01.bin.md" \
  rom_map.png
```

### Extract Palettes
```bash
python scripts/extract_palettes.py \
  "Phantasy Star Gen4 - Working Designs 6.01.bin.md"
```

---

## Technical Notes

### ROM Format
- Big-endian Motorola 68000 byte order
- 4bpp planar tile format (32 bytes per 8x8 tile)
- 9-bit BGR palette format (big-endian 16-bit words)
- Nemesis/Kosinski compression in graphics regions

### Control Codes (Expanded Region)
| Code | Function |
|------|----------|
| 0xF4 | Scene marker (followed by scene ID) |
| 0xFC | Wait for button |
| 0xFD | End of string |
| 0xFF | End of dialogue scene |

### Control Codes (Original ROM)
| Code | Function |
|------|----------|
| 0xBB-0xC0 | Insert character/monster/tech/item/value names |
| 0xC1 | Line break |
| 0xC2 | Clear window |
| 0xC3 | Wait for button |
| 0xC4-0xC5 | End of text |

---

## License

This is a research/toolkit project for educational and preservation purposes.
Phantasy Star IV is property of Sega. The Working Designs 6.01 patch is a fan work.

---

*Generated from automated ROM reverse engineering analysis.*
