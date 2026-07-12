# Phantasy Star IV - ROM Reverse Engineering Toolkit

Complete extraction, analysis, and rebuild toolkit for **Phantasy Star IV: The End of the Millennium** (Working Designs 6.01 retranslation patch).

---

## Download the Complete Archive

> **This repository contains all documentation, scripts, data CSVs, and analysis reports.**
>
> **For the complete archive including all binary assets, PNG visualizations, and 3,999 individual scene files:**
>
> **[Download phantasy-star-iv-rom-toolkit.zip](sandbox:///mnt/agents/output/phantasy-star-iv-rom-toolkit.zip)** (18 MB)
>
> The ZIP contains everything in this repo plus all binary files, high-res visualizations, and per-scene dialogue files.

---

## Latest Changes

See [CHANGELOG.md](CHANGELOG.md) for full version history.

### v1.0.0 (2026-07-12)
- **Text encoding cracked** - Custom single-byte encoding mapped (A-Z, a-z, punctuation)
- **Full dialogue extracted** - 5,052,256 characters decoded from expanded ROM region
- **Font tiles located** - 768 tiles at 0x109400+ (1bpp 8x8 format)
- **Graphics analysis** - 9 regions extracted with hex dumps and byte frequency reports
- **Palettes extracted** - 10 Genesis 9-bit BGR palettes with RGB values
- **Game data located** - 8 items, 9 techniques, 11 skills, 9 character names
- **4 Python scripts** - Text extraction, tile extraction, palette scanning, ROM mapping
- **7 documentation pages** - Complete analysis, encoding guide, rebuild guide, master index
- **Graphics modernization research** - 3-tier approach (algorithmic, AI, HD-2D)

---

## What's In This Repo

| Directory | Contents |
|-----------|----------|
| `docs/` | 7 analysis documents (ROM report, encoding guide, rebuild guide, master index, graphics research, script stats, graphics index) |
| `data/text-encoding/` | `psiv.tbl` - the cracked character encoding table |
| `data/game-data/` | Items, techniques, skills CSVs + pointer table analysis |
| `data/dialogue/full/` | Full decoded script (~5MB in ZIP) |
| `data/dialogue/by-scene/` | 3,999 individual scene files (in ZIP) |
| `data/graphics/raw/` | 9 extracted graphics binaries |
| `data/graphics/analysis/` | Hex dump previews and byte frequency reports |
| `data/palettes/` | Genesis palette data (raw + RGB values) |
| `scripts/` | 4 Python extraction tools |
| `visualizations/` | Font tile renders, ROM heat maps, palette previews |
| `CHANGELOG.md` | Full version history |

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

## Graphics Modernization

See `docs/05-Graphics-Modernization-Research.md` for a comprehensive survey of approaches:

1. **Algorithmic Upscale** (xBRZ/Super xBR) - 4-5 weeks, authentic pixel look
2. **AI Neural Upscale** (Real-ESRGAN + edge masks) - 9-10 weeks, enhanced detail
3. **HD-2D Style** (Octopath Traveler approach) - 6-12 months, modern-classic hybrid

---

## Complete Archive Contents

The ZIP download contains everything in this repo plus:

| Content | Size | Description |
|---------|------|-------------|
| `data/dialogue/full/dialogue-full-decoded.txt` | ~5 MB | Complete decoded dialogue |
| `data/dialogue/by-scene/` | 3,999 files | Per-scene dialogue files |
| `data/graphics/raw/*.bin` | ~52 KB | All 9 extracted graphics binaries |
| `data/palettes/palettes-raw.bin` | 428 B | Raw palette data |
| `visualizations/fonts/*.png` | ~750 KB | High-res font tile renders |
| `visualizations/rom-maps/*.png` | ~18 MB | Full ROM heat maps |
| `visualizations/palettes/*.png` | ~47 KB | Palette color swatches |

---

## License

This is a research/toolkit project for educational and preservation purposes.
Phantasy Star IV is property of Sega. The Working Designs 6.01 patch is a fan work.

---

*Generated from automated ROM reverse engineering analysis.*
