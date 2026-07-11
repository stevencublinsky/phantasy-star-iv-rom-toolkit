#!/usr/bin/env python3
"""
Phantasy Star IV - Palette Extractor
Scans ROM for Genesis palette data.
"""

import sys
import struct

def scan_palettes(rom_path, start=0, end=None):
    """Scan for Genesis palette data (16 colors x 2 bytes)."""
    with open(rom_path, 'rb') as f:
        f.seek(start)
        data = f.read() if end is None else f.read(end - start)
    
    palettes = []
    for i in range(0, len(data) - 32, 2):
        valid_colors = 0
        for c in range(16):
            raw = (data[i + c*2] << 8) | data[i + c*2 + 1]
            if raw <= 0x0EEE:
                valid_colors += 1
        if valid_colors >= 14:
            palettes.append(start + i)
    
    return palettes

def export_palette(rom_path, offset, output_path):
    """Export palette as RGB values."""
    with open(rom_path, 'rb') as f:
        f.seek(offset)
        pal = f.read(32)
    
    with open(output_path, 'w') as f:
        f.write(f"# Palette at 0x{offset:06X}\n")
        f.write("| Index | R | G | B |\n")
        f.write("|-------|---|---|---|\n")
        for i in range(0, 32, 2):
            raw = (pal[i] << 8) | pal[i+1]
            r = ((raw >> 1) & 0x07) * 36
            g = ((raw >> 5) & 0x07) * 36
            b = ((raw >> 9) & 0x07) * 36
            f.write(f"| {i//2:2d} | {r:3d} | {g:3d} | {b:3d} |\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: extract_palettes.py <rom.bin> [offset_hex]")
        sys.exit(1)
    
    rom_path = sys.argv[1]
    if len(sys.argv) > 2:
        offset = int(sys.argv[2], 16)
        export_palette(rom_path, offset, f'palette_0x{offset:06X}.txt')
    else:
        palettes = scan_palettes(rom_path)
        print(f"Found {len(palettes)} potential palettes")
        for p in palettes[:20]:
            print(f"  0x{p:06X}")
