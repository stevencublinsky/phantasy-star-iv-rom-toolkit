# Phantasy Star IV - Graphics Modernization Research Report
## From 16-Bit Genesis to Modern Standards (Non-AAA)

---

## Executive Summary

This report surveys practical, community-tested approaches for modernizing Sega Genesis-era graphics without AAA-level budgets or full 3D remakes. Three viable pipelines are covered:

1. **Algorithmic Upscaling** (xBRZ / Super xBR / hqx) - fast, free, preserves pixel aesthetic
2. **AI Neural Upscaling** (Real-ESRGAN + pixel-specific models) - detail-enhancing
3. **HD-2D Style** (Octopath Traveler approach) - 2D sprites in 3D environments

The recommended path is a **hybrid**: algorithmic upscale for UI/tiles, AI upscale for character portraits/battle sprites, HD-2D for field maps.

---

## 1. Genesis Graphics Constraints

| Specification | Value |
|-------------|-------|
| Max resolution | 320 x 224 (NTSC) |
| Color depth | 4bpp (16 colors from palette) |
| Colors on screen | 64 (4 palettes x 16 colors) |
| Sprite size max | 32 x 32 pixels |
| Tile format | 8x8 pixels, 4bpp planar |
| VRAM | 64 KB total |

---

## 2. Approach A: Algorithmic Upscaling

### Algorithm Comparison

| Algorithm | Scale | Best For |
|-----------|-------|----------|
| **xBRZ** | 2x-6x | Character sprites, battle graphics |
| **Super xBR** | 2x,4x,8x | Portraits, detailed sprites |
| **hqx** | 2x,3x,4x | Background tiles, environments |
| **OmniScale** | Any whole | Non-standard sizes |

### Recommended Pipeline
```
Raw 4bpp Tiles -> RetroGraphicsToolkit -> xBRZ 4x -> Aseprite cleanup -> Asset library
```

### Free Tools
- [Lospec Pixel Art Scaler](https://lospec.com/pixel-art-scaler/) (browser)
- [xBRZ Scaler](https://sourceforge.net/projects/xbrz/)
- [RetroGraphicsToolkit](https://forums.sonicretro.org/threads/retro-graphics-toolkit.34538/)
- [Aseprite](https://www.aseprite.org/) or GIMP

**Estimated effort**: 2-3 weeks for battle sprites, 1 week for UI/tiles.

---

## 3. Approach B: AI Neural Upscaling

### Leading Models

| Model | Best For |
|-------|----------|
| **Real-ESRGAN** | General purpose, sharp edges |
| **SwinIR** | Structure preservation |
| **ESRGAN (patrikspacek)** | Game sprites specifically |
| **waifu2x** | Anime-style pixel art |

### Hybrid Method (Community Best Practice)
```
Original -> xBRZ 4x (edge mask) + waifu2x 4x (detail) -> Combine -> Downscale 2x -> Final
```

**Estimated effort**: 4-6 weeks (manual cleanup per sprite).

---

## 4. Approach C: HD-2D Style

Following **Octopath Traveler**:
- 2D pixel-art sprites (upscaled xBRZ-style)
- 3D low-poly environments with modern lighting
- Bloom, depth-of-field, particle effects
- Unreal Engine 4/5 or Godot 4 rendering

**Estimated effort**: 6-12 months (most visually impressive).

---

## 5. Recommended Path for PSIV

### Tier 1: Algorithmic (4-5 weeks)
| Asset | Method | Scale |
|-------|--------|-------|
| Battle sprites | xBRZ 4x + cleanup | 2x-4x |
| Field character | xBRZ 4x | 2x |
| UI elements | hqx 4x | 4x |
| Font tiles | xBRZ 4x | 4x |

### Tier 2: AI-Enhanced (9-10 weeks)
Builds on Tier 1 with Real-ESRGAN for detail + xBRZ edge masks.

### Tier 3: HD-2D (6-12 months)
Adds 3D environments, dynamic lighting, post-processing.

---

## 6. Free Tool Stack

```
Extraction:    Python + numpy + PIL (completed)
Tile Extract:  RetroGraphicsToolkit / YY-CHR / Beehive
Decompress:    KENSS / SonicRetro tools
Upscale:       Lospec Scaler / xBRZ / Real-ESRGAN / waifu2x
Cleanup:       Aseprite or GIMP
Engine:        Unreal Engine 5 or Godot 4
```
