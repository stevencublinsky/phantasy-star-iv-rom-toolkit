#!/usr/bin/env python3
"""
Phantasy Star IV - Tile Extractor
Extracts 1bpp or 4bpp tile data from ROM.
"""

import sys
import numpy as np
from PIL import Image

def extract_1bpp_tiles(data, tile_size=8, cols=16):
    """Extract 1bpp tiles and return as PIL images."""
    tile_bytes = tile_size
    num_tiles = len(data) // tile_bytes
    rows = (num_tiles + cols - 1) // cols
    
    img = Image.new('1', (cols * 8, rows * tile_size), 0)
    pixels = img.load()
    
    for t in range(num_tiles):
        tx = (t % cols) * 8
        ty = (t // cols) * tile_size
        for y in range(tile_size):
            byte = data[t * tile_bytes + y]
            for x in range(8):
                if (byte >> (7 - x)) & 1:
                    pixels[tx + x, ty + y] = 1
    
    return img

def main():
    if len(sys.argv) < 4:
        print("Usage: extract_tiles.py <rom.bin> <offset_hex> <size_hex> [1bpp|4bpp] [8|16]")
        sys.exit(1)
    
    rom_path = sys.argv[1]
    offset = int(sys.argv[2], 16)
    size = int(sys.argv[3], 16)
    fmt = sys.argv[4] if len(sys.argv) > 4 else '1bpp'
    tile_size = int(sys.argv[5]) if len(sys.argv) > 5 else 8
    
    with open(rom_path, 'rb') as f:
        f.seek(offset)
        data = f.read(size)
    
    if fmt == '1bpp':
        img = extract_1bpp_tiles(data, tile_size)
        out_path = f'tiles_0x{offset:06X}_1bpp.png'
        img.save(out_path)
        print(f"Saved: {out_path}")

if __name__ == '__main__':
    main()
