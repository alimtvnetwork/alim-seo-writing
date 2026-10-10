# 04 — Usage Guidelines

How to combine the backgrounds (file `02`) and fonts (file `03`) without
breaking contrast or brand feel.

## Contrast minimums

| Background tone | Text on it | Minimum |
|-----------------|------------|---------|
| Dark (BG-D1…D4) | White `#ffffff` headlines | always passes — keep sub-copy at 70%+ white |
| Dark (BG-D1…D4) | Coloured accents | lavender `#c9b8e8`, sky `#9ecfff`, mint `#9fe8c9` |
| Light (BG-L1…L4, BG-H1…H4) | Headlines `#1a1a2e` | always passes |
| Light | Sub-copy `#4a4a5a` | passes on all light concepts |
| Light | Accent pills | white text on candy colours: red `#e5484d`, green `#2fae5f`, purple `#8b5cf6`, blue `#3b82f6` |

## The scrim rule

If a background's texture sits behind body text, add a scrim first:

- Dark bg: black gradient scrim, 40% → 0%, behind the text block.
- Light bg: solid white card at 85–92% opacity with 24px radius behind
  the text block (the magnet-board tile pattern).

Headlines may sit directly on texture; body copy may not.

## Asset workflow

1. Pick a background concept from file `02` and build it at 2x into
   `assets/backgrounds/` as `bg-<family>-<name>.png`.
2. Pick a font pairing from file `03` for the asset's tone.
3. Set the headline at 700 weight minimum, add an eyebrow label in mono
   or Nunito 800 uppercase where the source assets have one.
4. Check contrast with the table above; add a scrim if body text touches
   texture.
5. Keep the source backgrounds (`pixheads-purple-bg.png`,
   `blitz-dark-grid-bg.png`) untouched — they are references, not templates.

## Do / don't

- Do keep one hero shape per background.
- Do use pill badges for meta info (dates, categories, reading time).
- Do keep 120px quiet margins on dark backgrounds.
- Don't place thin text on the triangle watermark or the pinstripes.
- Don't mix the dark-technical grid with candy colours — pick a lane.
- Don't stretch or recolour the source backgrounds; rebuild the concept
  instead.
