# Phantasy Star IV - ROM Rebuild Guide

## Working Designs 6.01 Retranslation

---

## 1. ROM Header Format

### Standard Genesis Header (0x100 - 0x1FF)

| Offset | Size | Field | Notes |
|--------|------|-------|-------|
| 0x100 | 16 bytes | Console | "SEGA GENESIS" or "SEGA MEGA DRIVE" |
| 0x110 | 16 bytes | Copyright | "(C)SEGA 1994.NOV" |
| 0x120 | 48 bytes | Title (Domestic) | "PHANTASY STAR The end of the millennium" |
| 0x150 | 48 bytes | Title (Overseas) | Same as domestic |
| 0x180 | 14 bytes | Serial | "GM MK-1307 -00" |
| 0x18E | 2 bytes | Checksum | See checksum section |
| 0x190 | 16 bytes | I/O | "J" (3-button pad) |
| 0x1A0 | 4 bytes | ROM Start | 0x00000000 |
| 0x1A4 | 4 bytes | ROM End | 0x0030FA13 (this ROM) |
| 0x1A8 | 4 bytes | RAM Start | 0x00FF0000 |
| 0x1AC | 4 bytes | RAM End | 0x00FFFFFF |

### Checksum Recalculation

```python
import struct

def recalculate_checksum(rom_data):
    """Recalculate Genesis ROM checksum."""
    # Sum all bytes from 0x200 to end
    checksum = sum(rom_data[0x200:]) & 0xFFFF
    # Store at 0x18E (big-endian)
    rom_data[0x18E:0x190] = struct.pack('>H', checksum)
    return checksum
```

---

## 2. Text Insertion Workflow

### Prerequisites
- Build the character table (`psiv.tbl`)
- Extract font tiles from 0x109400+
- Understand the control codes

### Steps

1. **Prepare Text**
   - Convert ASCII text to PSIV encoding
   - A-Z -> 0x01-0x1A
   - a-z -> 0x1B-0x34
   - Space -> 0x00
   - Punctuation -> see `text_encoding_guide.md`

2. **Preserve Control Codes**
   - Always keep control codes intact
   - Use 0xF4 for scene markers
   - Use 0xFC for line breaks within scenes
   - Use 0xFD for string ends
   - Use 0xFF for scene ends

3. **Calculate Sizes**
   - Original text block size must be known
   - New text must fit within original boundaries OR
   - Pointer tables must be updated to point to new location

4. **Update Pointers**
   - Find pointer table preceding text block
   - Update big-endian 24-bit or 32-bit pointers
   - Each pointer = target address of corresponding string

5. **Recalculate Checksum**
   - Always recalculate ROM checksum after modification
   - Use function above

---

## 3. Graphics Insertion

### Tile Format
- **1bpp tiles**: 8 bytes per 8x8 tile
- **4bpp tiles**: 32 bytes per 8x8 tile (Genesis planar format)
- **Font tiles**: 1bpp 8x8 at 0x109400+

### Palette Format
- 16 colors x 2 bytes = 32 bytes per palette
- Genesis 9-bit BGR: `----bbb-ggg-rrr` (big-endian)
- Maximum value per channel: 0x07 (3-bit)

### VRAM Budget
| Component | Size |
|-----------|------|
| Total VRAM | 64 KB |
| Tile RAM | 32 KB (loadable) |
| Pattern tables | 2 x 8 KB |
| Scroll maps | 2 x 8 KB |
| Sprite table | ~2 KB |
| Color RAM | 4 KB |

---

## 4. Pointer Table Repointing

### Finding Pointer Tables
1. Locate text block (search for control codes 0xC4/0xC5/0xFD/0xFF)
2. Search backward for incrementing address patterns
3. Pointers are big-endian (Motorola 68000 format)

### Pointer Formats
- **32-bit**: 4 bytes per pointer (most common)
- **24-bit**: 3 bytes per pointer (banked addressing)
- Deltas between pointers typically 10-200 bytes

### Repointing Steps
1. Identify pointer table start address
2. Count number of entries
3. Calculate new text block address
4. Write new pointers (big-endian)
5. Verify all pointers point to valid control code boundaries

---

## 5. Testing Checklist

### Emulator Compatibility
- [ ] Test on Genesis Plus GX (most accurate)
- [ ] Test on BlastEm (cycle-accurate)
- [ ] Test on real hardware if possible
- [ ] Verify save/load functionality
- [ ] Check all text displays correctly
- [ ] Verify no graphical glitches
- [ ] Check sound effects and music
- [ ] Test through multiple scenes/dialogue

### ROM Validation
- [ ] Header checksum matches calculated checksum
- [ ] ROM size within Genesis limits (<= 4MB)
- [ ] Vector table intact at 0x000-0x1FF
- [ ] No data corruption in unchanged regions

---

## 6. ROM Size Constraints

| Parameter | Value |
|-----------|-------|
| Maximum ROM size | 4 MB (4,194,304 bytes) |
| Current ROM size | ~3.06 MB (3,209,748 bytes) |
| Available space | ~1.0 MB |
| Status | SAFE for modifications |

---

## 7. Tools

| Tool | Purpose |
|------|---------|
| `scripts/extract_text.py` | Extract and decode dialogue text |
| `scripts/extract_tiles.py` | Extract graphics tiles |
| `scripts/extract_palettes.py` | Extract color palettes |
| `scripts/rom_map.py` | Generate ROM visual map |

---

## 8. Known Issues & Limitations

1. **Text encoding ambiguity**: Numbers 0-9 and some symbols are best-effort mappings
2. **Pointer tables**: Not fully documented; require manual analysis per text block
3. **Original vs expanded encoding**: Two different encoding schemes exist
4. **Compressed graphics**: Sprite/tile data may use compression (unverified)
5. **Control codes 0x80-0xFF**: Many undocumented; require runtime testing
