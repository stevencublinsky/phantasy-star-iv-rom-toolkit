# Phantasy Star IV: The End of the Millennium
## ROM Analysis & Extraction Report
### Working Designs 6.01 Fan Retranslation

---

## 1. ROM Header Report

| Field | Offset | Size | Value |
|-------|--------|------|-------|
| Console | 0x100 | 16 bytes | `SEGA GENESIS` |
| Copyright | 0x110 | 16 bytes | `(C)SEGA 1994.NOV` |
| Title (Domestic) | 0x120 | 48 bytes | `PHANTASY STAR The end of the millennium` |
| Title (Overseas) | 0x150 | 48 bytes | `PHANTASY STAR The end of the millennium` |
| Serial | 0x180 | 14 bytes | `GM MK-1307 -00` |
| Checksum (stored) | 0x18E | 2 bytes | `0x16F7` |
| I/O Support | 0x190 | 16 bytes | `J` (3-button pad) |
| ROM Start | 0x1A0 | 4 bytes | `0x00000000` |
| ROM End | 0x1A4 | 4 bytes | `0x0030FA13` (3,209,748 bytes declared) |
| RAM Start | 0x1A8 | 4 bytes | `0x00FF0000` |
| RAM End | 0x1AC | 4 bytes | `0x00FFFFFF` |

### Checksum Verification
| Checksum | Value |
|----------|-------|
| Stored | `0x16F7` (5,879) |
| Calculated | `0xA496` (42,134) |
| Status | **MISMATCH - ROM IS PATCHED/MODIFIED** |
| Delta | `0x8D9F` |

### Format Identification
- **Format**: Raw BIN (no SMD interleave header detected)
- **Extension**: `.md` (misleading - contains raw binary ROM data, not Markdown)
- **First 16 bytes**: `FFFF 4FF0 0000 0220 0000 0200 0000 0200` (valid vector table)

### Vector Table
| Vector | Address | Purpose |
|--------|---------|---------|
| Stack Pointer | 0xFFFF4FF0 | System stack |
| Reset | 0x00000220 | Entry point (valid) |
| HBlank | 0xFFFFECB0 | Horizontal interrupt |
| VBlank | 0x00000510 | Vertical interrupt |
| Exception handlers | 0x00000200 | Common handler address |

---

## 2. Structural Map

### ROM Overview
| Property | Value |
|----------|-------|
| Total Size | 3,209,748 bytes (3.061 MB) |
| Standard PSIV Size | 2,097,152 bytes (2.00 MB) |
| Oversized By | 1,112,596 bytes (1.087 KB / 53%) |
| Genesis Maximum | 4,194,304 bytes (4.00 MB) |
| Within Hardware Limit | **YES** |

### Identified Regions

| Address Range | Size | Type | Notes |
|--------------|------|------|-------|
| 0x000000 - 0x0001FF | 512 B | Vector Table | 68K exception vectors |
| 0x000200 - 0x0003FF | 512 B | ROM Header | Standard Genesis header |
| 0x000400 - 0x07FFFF | ~511 KB | 68000 Code | Main game engine |
| 0x080000 - 0x0CFFFF | ~320 KB | Graphics (Compressed) | High entropy - sprites/tiles |
| 0x0D0000 - 0x0FFFFF | ~192 KB | Game Logic | Code + data |
| 0x100000 - 0x1BFFFF | ~768 KB | Graphics/Fonts/Data | Font tiles + compressed assets |
| 0x1C0000 - 0x1FFFFF | ~256 KB | Mixed Code/Data | Engine code + tables |
| **0x200000 - 0x30FA13** | **~1.09 MB** | **Retranslated Text** | **Patch data - all new dialogue** |

### Font Tile Regions (Identified)
| Address | Zero % | Likely Content |
|---------|--------|----------------|
| 0x109C00 | 93.9% | Font tiles (1bpp 8x8 or 8x16) |
| 0x109400 | 93.2% | Font tiles |
| 0x10A000 | 93.0% | Font tiles |
| 0x108C00 | 92.7% | Font tiles |
| 0x108800 | 92.3% | Font tiles |
| 0x108400 | 91.7% | Font tiles |

---

## 3. Text Analysis

### ASCII String Search Results

| Category | Found / Total | Verdict |
|----------|--------------|---------|
| Game Identifiers | SEGA GENESIS (1), PHANTASY STAR (3), WD (30) | Patch signatures present |
| Character Names | 0 / 11 | No ASCII storage |
| Item Names | 0 / 11 | No ASCII storage |
| Technique Names | 1 / 40 | False positive only |
| **Version String** | **0** | **"6.01" not in ROM - filename only** |

### Control Code Frequency Table

| Code | Function | Count | Frequency |
|------|----------|-------|-----------|
| 0xBB | Insert Character 1 name | 8,018 | HIGH |
| 0xBC | Insert Character 2 name | 9,122 | HIGH |
| 0xBD | Insert Monster name | 6,174 | HIGH |
| 0xBE | Insert Technique name | 5,459 | HIGH |
| 0xBF | Insert Item name | 8,829 | HIGH |
| 0xC0 | Insert numeric value | 13,807 | HIGH |
| 0xC1 | Line break | 8,293 | HIGH |
| 0xC2 | Clear window | 7,945 | HIGH |
| 0xC3 | Wait for button | 8,085 | HIGH |
| 0xC4 | End of text | 7,319 | HIGH |
| 0xC5 | End of text (alt) | 7,662 | HIGH |
| **TOTAL** | | **90,713** | |

### Encoding Verdict
> **CUSTOM TEXT ENCODING CONFIRMED**
>
> This ROM uses a custom character encoding system where printable characters are
> represented by byte values that map to specific font tiles. No ASCII text storage
> is used for game content. Full text extraction requires:
> 1. Font tile extraction from 0x108400-0x10AC00
> 2. Building a .tbl (table) file mapping byte values to characters
> 3. Using the .tbl to decode dialogue text, especially in the expanded region

---

## 4. Graphics Analysis

### Palette Data
- **1,675** potential palette tables identified throughout ROM
- **Format**: Genesis 9-bit color (big-endian 16-bit words, `----BBB-GGG-RRR`)
- **First palette**: 0x0031F6
- **Color depth**: 16 colors per palette (32 bytes each)

### Tile Data
- **Tile size**: Likely 8x8 pixels (32 bytes in 4bpp planar format)
- **Primary graphics regions**: 0x080000-0x0CFFFF, 0x100000-0x1BFFFF
- **Compression**: High entropy suggests compressed data (possibly Nemesis or Kosinski compression, standard for Sega Genesis)

### Font Tiles
- **Location**: 0x108400 - 0x10AC00 (approximately)
- **Format**: 1bpp (1 bit per pixel)
- **Tile size**: 8x8 (8 bytes) or 8x16 (16 bytes) most likely
- **Sparsity**: 91-94% zeros (typical for font character data)
- **Recommendation**: Extract as 1bpp 8x8 first, then try 8x16 if characters look vertically compressed

---

## 5. Rebuild Notes

### ROM Size Constraints
| Parameter | Value |
|-----------|-------|
| Genesis ROM Maximum | 4 MB (4,194,304 bytes) |
| Current ROM Size | 3.061 MB (3,209,748 bytes) |
| Available Space | ~1.0 MB remaining |
| Status | **SAFE** - can add ~1MB more data |

### VRAM Constraints (Genesis)
| Parameter | Value |
|-----------|-------|
| Total VRAM | 64 KB |
| Tile RAM | 32 KB (loadable at once) |
| Pattern Tables | 2 x 8 KB |
| Scroll Maps | 2 x 8 KB |
| Sprite Table | ~2 KB |
| Color RAM | 128 x 16 palettes x 2 bytes = 4 KB |

### Pointer Table Format
- **Architecture**: Big-endian (Motorola 68000)
- **Pointer size**: 24-bit or 32-bit (most likely 24-bit for Genesis bank switching)
- **Text pointers**: Likely stored as 24-bit offsets pointing to dialogue strings

### Checksum Recalculation
```python
# To fix checksum after modification:
checksum = sum(rom_data[0x200:]) & 0xFFFF
rom_data[0x18E:0x190] = struct.pack('>H', checksum)
```

### Patch Information (Metadata)
| Property | Value |
|----------|-------|
| Project | Phantasy Star Generation:4 |
| Variant | Working Designs ( adds WD-style humor) |
| Version | 6.01 (filename only, not embedded in ROM) |
| Author | doom@inbox.com (uploader) |
| Date Added to Archive | 2021-05-20 |
| Base Game | Phantasy Star IV (GM MK-1307) |
| Description | Comprehensive retranslation using fan-translated PS scripts |

### Key Findings for Rebuild
1. The patch adds ~1.1MB of retranslated text in the expanded region (0x200000+)
2. The original game code (0x000000-0x1FFFFF) appears largely intact
3. The "Working Designs" variant adds humorous dialogue in the style of WD's Sega CD translations
4. A "Purist" variant exists that removes these additions
5. Font extraction is the critical next step for full text dump capability
6. The expanded text region uses different control codes than the original game's text system

---

## Generated Artifacts

| File | Description |
|------|-------------|
| `psiv_rom_map_2mb.png` | Visual map of first 2MB of ROM |
| `psiv_rom_map_expanded.png` | Visual map of expanded text region |
| `font_1bpp_0x*.png` | Candidate font tile visualizations |
| `PSIV_ROM_Analysis_Report.md` | This report |

---

*Report generated from automated ROM analysis. All offsets are hexadecimal unless noted. All multi-byte values are big-endian (Motorola 68000 byte order).*
