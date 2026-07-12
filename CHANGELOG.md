# Changelog

All notable changes to the Phantasy Star IV ROM Toolkit project.

## [1.0.0] - 2026-07-12

### Added - Phase 1: Font & Text Table Construction
- Located font tiles at 0x109400-0x10A400 (3 contiguous 2KB tables, 1bpp 8x8)
- Generated high-resolution font tile visualizations (4 PNG renders)
- **Cracked the custom text encoding**: 0x01-0x1A=A-Z, 0x1B-0x34=a-z, 0x35-0x3B=punctuation
- Created `psiv.tbl` character encoding table with full control code documentation

### Added - Phase 2: Dialogue & Script Extraction
- Extracted and decoded **5,052,256 characters** of dialogue text from expanded ROM region (0x200000+)
- Identified **4,849 scene markers** and **13,353 dialogue strings**
- Split dialogue into 3,999 individual scene files in `data/dialogue/by-scene/`
- Generated script statistics report with control code frequency analysis
- Created placeholder for full dialogue in repo (complete text in ZIP archive)

### Added - Phase 3: Graphics & Asset Extraction
- Extracted 9 graphics regions as raw .bin files (low-byte data tables, font tiles)
- Generated hex dump previews and byte frequency analysis for all graphics regions
- Extracted 10 Genesis 9-bit BGR palettes with RGB color values
- Created palette preview visualization (color swatches)

### Added - Phase 4: Data Structure Extraction
- Located 8/11 item names in ROM (Monomate, Dimate, Trimate, Antidote, Moon Dew, Telepipe, Escapipe, Eclipse Torch)
- Located 9/40 technique names (Wat, Tsu, Gra, Vol, Res, Anti, Rever, Ryuka, Hinas)
- Located 11/47 skill names (Crosscut, Flaeli, Hewn, Tandle, Efess, Phonon, Diem, Death, Shadow, Earth, Miracle)
- Located 9/11 character names (Alys, Hahn, Rune, Rika, Gryz, Demi, Wren, Raja, Kyra)
- Created CSV exports for all located data

### Added - Phase 5: ROM Rebuild Toolkit
- `extract_text.py` - Extract and decode dialogue from any ROM region
- `extract_tiles.py` - Extract 1bpp/4bpp tile data to PNG
- `extract_palettes.py` - Scan and export Genesis palette data
- `rom_map.py` - Generate visual ROM heat map
- Complete rebuild guide with checksum recalculation, pointer table format, VRAM budget

### Added - Documentation
- `docs/01-ROM-Analysis-Report.md` - Full ROM header, checksum, structure analysis
- `docs/02-Text-Encoding-Guide.md` - Complete character encoding documentation
- `docs/03-ROM-Rebuild-Guide.md` - Checksum recalculation, text insertion, VRAM budget
- `docs/04-Master-ROM-Index.md` - Every significant offset in the ROM
- `docs/05-Graphics-Modernization-Research.md` - 3-tier approach to modernizing Genesis graphics
- `docs/06-Script-Statistics.md` - Dialogue volume, control code distribution
- `docs/07-Graphics-Index.md` - Catalog of all extracted graphics regions

### Added - Graphics Modernization Research
- Researched algorithmic upscaling (xBRZ, Super xBR, hqx)
- Researched AI neural upscaling (Real-ESRGAN, waifu2x hybrid method)
- Researched HD-2D style (Octopath Traveler approach)
- Compiled free tool stack and effort estimates for each tier

## Project Stats

| Metric | Value |
|--------|-------|
| Total files in archive | 4,044 |
| Decoded dialogue characters | 5,052,256 |
| Scene files | 3,999 |
| Font tiles identified | 768 |
| Graphics regions extracted | 9 |
| Palettes extracted | 10 |
| Items located | 8/11 |
| Techniques located | 9/40 |
| Skills located | 11/47 |
| Python scripts | 4 |
| Documentation pages | 7 |
