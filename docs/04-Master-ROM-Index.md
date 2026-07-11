# Phantasy Star IV - Master ROM Index

## Working Designs 6.01 Retranslation

---

## System Regions

| Start | End | Size | Description |
|-------|-----|------|-------------|
| 0x000000 | 0x0000FF | 256 B | 68000 Vector Table |
| 0x000100 | 0x0001FF | 256 B | ROM Header (SEGA GENESIS) |

## Code Regions

| Start | End | Size | Description |
|-------|-----|------|-------------|
| 0x000200 | 0x07FFFF | ~512 KB | Main game engine code |
| 0x0D0000 | 0x0FFFFF | ~192 KB | Game logic and routines |
| 0x1C0000 | 0x1FFFFF | ~256 KB | Mixed code/data |

## Graphics Regions

| Start | End | Size | Description |
|-------|-----|------|-------------|
| 0x080000 | 0x0CFFFF | ~320 KB | Compressed sprites/tiles (high entropy) |
| 0x100000 | 0x1083FF | ~35 KB | Graphics bank 0 |
| 0x108400 | 0x10ABFF | ~10 KB | Sparse font tile data (candidate) |
| 0x109400 | 0x109BFF | 2 KB | **Font table 1** (1bpp 8x8, 256 tiles) |
| 0x109C00 | 0x10A3FF | 2 KB | **Font table 2** (1bpp 8x8, 256 tiles) |
| 0x10A400 | 0x10ABFF | 2 KB | **Font table 3** (1bpp 8x8, 256 tiles) |
| 0x10AC00 | 0x1BFFFF | ~700 KB | Graphics, fonts, compressed data |

## Data Tables

| Start | End | Size | Description |
|-------|-----|------|-------------|
| 0x1155C4 | 0x1175D2 | 8,206 B | Low-byte data table 1 |
| 0x117603 | 0x119607 | 8,196 B | Low-byte data table 2 |
| 0x1FA000 | 0x1FDFFF | ~16 KB | Item names and data |
| 0x1FE000 | 0x1FFFFF | ~8 KB | Technique/skill name references |

## Text Regions

| Start | End | Size | Description |
|-------|-----|------|-------------|
| 0x100000 | 0x1FFFFF | ~1 MB | Original game text (mixed encoding) |
| 0x200000 | 0x30FA13 | ~1.09 MB | **Retranslated dialogue text** |

### Notable Text Sub-regions

| Address | Description |
|---------|-------------|
| 0x211DF1 | First 0xC1 control code (expanded region) |
| 0x223003 | First 0xC3 control code |
| 0x223010 | First 0xC5 end marker |
| 0x22307D | First 0xC4 end marker |

## Palette Data

| Address | Colors | Description |
|---------|--------|-------------|
| 0x0031F6 | 16 | Title screen palette |
| 0x00589A | 16 | Early game palette |
| 0x006232 | 16 | Character/object palette |
| 0x007110 | 16 | UI palette |
| 0x007152 | 16 | Secondary palette |
| 0x007194 | 16 | Background palette |
| 0x0071D6 | 16 | Sprite palette |
| 0x007218 | 16 | Effect palette |
| 0x00725A | 16 | Additional palette |
| 0x00729C | 16 | Fade/transition palette |

## Found Data Structures

### Items

| Item Name | ROM Offset | Status |
|-----------|-----------|--------|
| Monomate | 0x20ADA0 | Found |
| Dimate | 0x1FA417 | Found |
| Trimate | 0x20D1B2 | Found |
| Antidote | 0x2C6CE4 | Found |
| Moon Dew | 0x2C6CF8 | Found |
| Telepipe | 0x2C6D0B | Found |
| Escapipe | 0x204E72 | Found |
| Eclipse Torch | 0x1FE7E0 | Found |

### Techniques

| Technique | ROM Offset | Status |
|-----------|-----------|--------|
| Wat | 0x1F2D90 | Found |
| Tsu | 0x222A25 | Found |
| Gra | 0x1E76BC | Found |
| Vol | 0x0C16C6 | Found |
| Res | 0x1F1069 | Found |
| Anti | 0x2C6CE4 | Found |
| Rever | 0x1FD6D6 | Found |
| Ryuka | 0x2C8AF0 | Found |
| Hinas | 0x2C8B1B | Found |

### Character Names

| Character | ROM Offset | Status |
|-----------|-----------|--------|
| Alys | 0x1DFA6C | Found |
| Hahn | 0x1DFC13 | Found |
| Rune | 0x1E73D2 | Found |
| Rika | 0x1E84F0 | Found |
| Gryz | 0x1E37E2 | Found |
| Demi | 0x1F2A39 | Found |
| Wren | 0x1F46E6 | Found |
| Raja | 0x1F3FB8 | Found |
| Kyra | 0x1FB4DF | Found |

## Control Code Distribution (Expanded Region)

| Code | Count | Description |
|------|-------|-------------|
| 0xBB | 3,248 | Insert Char 1 name |
| 0xBC | 2,706 | Insert Char 2 name |
| 0xBD | 2,524 | Insert Monster name |
| 0xBE | 2,217 | Insert Technique name |
| 0xBF | 4,012 | Insert Item name |
| 0xC0 | 2,570 | Insert numeric value |
| 0xC1 | 2,930 | Line break |
| 0xC2 | 2,804 | Clear window |
| 0xC3 | 2,895 | Wait for button |
| 0xC4 | 2,537 | End of text |
| 0xC5 | 3,977 | End of text (alt) |

## File Checksums

| Type | Value |
|------|-------|
| Stored Checksum | 0x16F7 |
| Calculated Checksum | 0xA496 |
| MD5 | 6968d7caa036a4111a69b9e57851b9df |
| SHA1 | f735c3f961707b30b5392dcf5016c61f46cad0a9 |

## ROM Specifications

| Parameter | Value |
|-----------|-------|
| Total Size | 3,209,748 bytes (3.061 MB) |
| Standard PSIV Size | 2,097,152 bytes (2.00 MB) |
| Oversized By | 1,112,596 bytes (1.087 KB) |
| Genesis Maximum | 4,194,304 bytes (4.00 MB) |
| Format | Raw BIN (no SMD interleave) |
| Console | SEGA GENESIS |
| Title | PHANTASY STAR The end of the millennium |
| Serial | GM MK-1307 -00 |
| Entry Point | 0x00000220 |
| Stack Pointer | 0xFFFF4FF0 |
