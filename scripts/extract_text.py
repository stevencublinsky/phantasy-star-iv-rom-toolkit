#!/usr/bin/env python3
"""
Phantasy Star IV - Text Extractor
Extracts dialogue text from ROM using the .tbl character table.
"""

import sys
import struct

def load_tbl(tbl_path):
    """Load character table from .tbl file."""
    tbl = {}
    with open(tbl_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, val = line.split('=', 1)
                try:
                    byte_val = int(key, 16)
                    tbl[byte_val] = val
                except ValueError:
                    pass
    return tbl

def decode_text(data, tbl):
    """Decode binary text data using character table."""
    result = []
    i = 0
    while i < len(data):
        b = data[i]
        if b in tbl:
            val = tbl[b]
            if val.startswith('<') and val.endswith('>'):
                result.append(f'\n{val}\n')
            else:
                result.append(val)
            i += 1
        elif b == 0xF4 and i + 1 < len(data):
            result.append(f'\n=== SCENE {data[i+1]:02X} ===\n')
            i += 2
        elif b >= 0x80:
            result.append(f'<CTRL_{b:02X}>')
            i += 1
        else:
            result.append(f'[{b:02X}]')
            i += 1
    return ''.join(result)

def extract_region(rom_path, start, end, tbl_path, output_path):
    """Extract and decode a text region from ROM."""
    with open(rom_path, 'rb') as f:
        f.seek(start)
        data = f.read(end - start)
    
    tbl = load_tbl(tbl_path)
    decoded = decode_text(data, tbl)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(decoded)
    
    print(f"Extracted 0x{start:06X}-0x{end:06X} to {output_path}")
    print(f"  Input: {len(data):,} bytes -> Output: {len(decoded):,} chars")

if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Usage: extract_text.py <rom.bin> <start_hex> <end_hex> <table.tbl> <output.txt>")
        sys.exit(1)
    
    rom_path = sys.argv[1]
    start = int(sys.argv[2], 16)
    end = int(sys.argv[3], 16)
    tbl_path = sys.argv[4]
    output_path = sys.argv[5]
    
    extract_region(rom_path, start, end, tbl_path, output_path)
