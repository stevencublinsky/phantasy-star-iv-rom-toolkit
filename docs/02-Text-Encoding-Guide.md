# Phantasy Star IV - Text Encoding Guide

## Working Designs 6.01 Retranslation

---

## Encoding Summary

The retranslation patch uses a **custom single-byte character encoding** stored in the expanded ROM region (0x200000+). The original game (0x000000-0x1FFFFF) uses a different encoding system.

## Character Map

| Range | Content |
|-------|---------|
| 0x00 | Space |
| 0x01 - 0x1A | A - Z (uppercase) |
| 0x1B - 0x34 | a - z (lowercase) |
| 0x35 | . (period) |
| 0x36 | ' (apostrophe) |
| 0x37 | ! (exclamation) |
| 0x38 | - (hyphen) |
| 0x39 - 0x45 | 0 - 9 (digits, best-effort mapping) |
| 0x46 | " (double quote) |
| 0x47 | ( (open parenthesis) |
| 0x48 | ) (close parenthesis) |
| 0x49 | : (colon) |
| 0x4A | ; (semicolon) |
| 0x4B | & (ampersand) |
| 0x3A | , (comma) |
| 0x3B | ? (question mark) |

## Control Codes (Expanded Region)

| Code | Function |
|------|----------|
| 0xF4 | Scene marker (followed by scene ID byte) |
| 0xFC | Wait for button / continue |
| 0xFD | End of string |
| 0xFF | End of dialogue scene |

## Control Codes (Original ROM)

| Code | Function |
|------|----------|
| 0xBB | Insert Character 1 name |
| 0xBC | Insert Character 2 name |
| 0xBD | Insert Monster name |
| 0xBE | Insert Technique name |
| 0xBF | Insert Item name |
| 0xC0 | Insert numeric value |
| 0xC1 | Line break |
| 0xC2 | Clear window |
| 0xC3 | Wait for button |
| 0xC4 | End of text |
| 0xC5 | End of text (alt) |

## Font Tiles

- **Location**: 0x109400 - 0x10A400 (multiple 2KB tables)
- **Format**: 1bpp (1 bit per pixel)
- **Tile size**: 8x8 pixels (8 bytes per tile)
- **Total tiles**: 256 per table (2KB per table)
- **Tables found**: At least 3 contiguous tables

## Text Regions

| Region | Address Range | Content |
|--------|--------------|---------|
| Original Text | 0x100000 - 0x1FFFFF | Base game dialogue (different encoding) |
| Expanded Text | 0x200000 - 0x30FA13 | Retranslation dialogue (this encoding) |

## Notes

- The ellipsis "..." is represented as three period bytes: 0x35 0x35 0x35
- The encoding does not include all ASCII symbols; some special characters use control codes
- Uppercase and lowercase are in separate contiguous ranges (unlike ASCII)
- The font tables also contain Japanese characters in the 0x80+ tile range, but these are not used in the English text
