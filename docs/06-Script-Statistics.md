# Phantasy Star IV - Script Statistics

## Working Designs 6.01 Retranslation

## Text Volume

| Metric | Value |
|--------|-------|
| Total decoded characters | 5,052,256 |
| Scene markers | 4,849 |
| String ends (<END>) | 13,353 |
| Scene ends (<END_SCENE>) | 15,227 |
| Total lines | 54,481 |
| Scene files generated | 4,849 |
| Unique scene IDs | 256 |

## Control Code Usage (Expanded Region)

| Code | Count | Description |
|------|-------|-------------|
| 0xBB | 3,248 | Insert Char 1 |
| 0xBC | 2,706 | Insert Char 2 |
| 0xBD | 2,524 | Insert Monster |
| 0xBE | 2,217 | Insert Tech |
| 0xBF | 4,012 | Insert Item |
| 0xC0 | 2,570 | Insert Value |
| 0xC1 | 2,930 | Line Break |
| 0xC2 | 2,804 | Clear Window |
| 0xC3 | 2,895 | Wait Button |
| 0xC4 | 2,537 | End Text |
| 0xC5 | 3,977 | End Text Alt |

## Data Structure Findings

| Category | Found | Total |
|----------|-------|-------|
| Items | 8 | 11 searched |
| Techniques | 9 | 40 searched |
| Skills | 11 | 47 searched |
| Character Names | 9 | 11 searched |

## Font Tables

| Address | Size | Tile Count |
|---------|------|------------|
| 0x109400 | 2,048 | 256 (8x8 1bpp) |
| 0x109C00 | 2,048 | 256 (8x8 1bpp) |
| 0x10A000 | 2,048 | 256 (8x8 1bpp) |

## Generated Files

| File | Description |
|------|-------------|
| psiv.tbl | Character encoding table |
| text_encoding_guide.md | Encoding documentation |
| dialogue_full.txt | Complete decoded script |
| dialogue_by_scene/ | Per-scene script files |
| pointer_tables.txt | Pointer table analysis |
| graphics_raw/ | Extracted graphics binaries |
| graphics_index.md | Graphics catalog |
| palettes_raw.bin | Raw palette data |
| palettes.txt | Palette RGB values |
| items.csv | Item data |
| techniques.csv | Technique data |
| skills.csv | Skill data |
| scripts/ | Python extraction toolkit |
| REBUILD_GUIDE.md | ROM rebuild documentation |
| MASTER_INDEX.md | Complete offset reference |
