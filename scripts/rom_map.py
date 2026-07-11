#!/usr/bin/env python3
"""
Phantasy Star IV - ROM Structure Mapper
Generates a visual/structural map of the ROM.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

def generate_map(rom_path, output_path='rom_map.png'):
    """Generate visual ROM map."""
    with open(rom_path, 'rb') as f:
        data = f.read()
    
    arr = np.frombuffer(data, dtype=np.uint8)
    size = min(len(arr), 0x200000)
    cols = 512
    rows = size // cols
    arr_2d = arr[:rows*cols].reshape(rows, cols)
    
    fig, ax = plt.subplots(figsize=(16, 8))
    im = ax.imshow(arr_2d, cmap='inferno', aspect='auto', vmin=0, vmax=255)
    ax.set_title(f'ROM Map: {rom_path}')
    ax.set_xlabel('Offset within 512-byte row')
    ax.set_ylabel('Row (x512 bytes)')
    plt.colorbar(im, ax=ax, label='Byte Value')
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    print(f"Saved: {output_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: rom_map.py <rom.bin> [output.png]")
        sys.exit(1)
    
    rom_path = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else 'rom_map.png'
    generate_map(rom_path, output)
