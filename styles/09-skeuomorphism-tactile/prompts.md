# 09 Skeuomorphism Tactile — ready prompts

## Codex
```
Build a single-file HTML landing page for "TORSO FX-1" — a desktop hardware
compressor/audio interface by a synth company. Style: MODERN skeuomorphism
(Teenage Engineering industrial revival — NOT 2008 leather iOS). Fonts:
Space Grotesk 500 headings, IBM Plex Sans body 16px/1.6, JetBrains Mono for
readouts and engraved labels (10px uppercase +0.15em, text-shadow 0 1px 0
rgba(255,255,255,.4)). Palette: aluminum bg #E8E9EB, panels #F2F3F4, recessed
wells #D7D9DC, text #1F2328, ONE action hue hardware-orange #F25C05, amber
readouts #FFB000. Light logic: top-lit — raised surfaces get border-top 1px
rgba(255,255,255,.8) + border-bottom 1px rgba(0,0,0,.25) + soft drop shadow;
recessed zones get inset 0 2px 4px rgba(0,0,0,.25). Radii 4–12px max. Layout:
1160px container, split hero (copy left, control console right with dials,
fader, toggle switch, mono VU readout, LED dots), recessed feature wells,
spec-sheet section (mono tabular numbers, hairline rows), pricing as three
panels, CTA as a physical raised orange button with press state. Motion
200ms cubic-bezier(.2,.9,.3,1.2) — switches slide with a clunk, buttons
invert to inset on :active. No glassmorphism, no pastels, no leather/wood
textures, no rainbow neon glows, no emoji. Include prefers-color-scheme
dark variant ("rack unit": bg #14161A, panels #1E2126, wells #0E1013, same
light logic) and prefers-reduced-motion reset.
```

## Claude
```
Design a landing page for TORSO FX-1, a hardware audio compressor, in the
modern skeuomorphic style of Teenage Engineering and pro-audio gear. The
page itself should feel like a machined front panel: top-lit aluminum
surfaces, recessed wells, a hero console with believable dials (radial tick
marks, knurled edge), a toggle switch, and an amber backlit readout in
JetBrains Mono tabular numerals. Space Grotesk headings, IBM Plex Sans body,
engraved uppercase micro-labels. One action hue (hardware orange #F25C05)
plus amber readouts and small LED status dots — nothing else colored.
Every control needs a real press state (inset + 1px shift, 200ms clunk
easing). Deliver one self-contained HTML file, dark "rack unit" variant
via prefers-color-scheme, reduced-motion reset. No leather, no glass, no
neon cyberpunk glow — restrained industrial realism only.
```

## Lovable
```
Create a landing page for "TORSO FX-1" (desktop audio compressor) in modern
skeuomorphic hardware style. Rules: aluminum palette (#E8E9EB bg, #F2F3F4
panels, #D7D9DC recessed wells), top-lit edges (light top border, dark bottom
border on raised surfaces; inset shadows in wells), radii 4–12px, fonts
Space Grotesk + IBM Plex Sans + JetBrains Mono (readouts tabular). Hero =
split: copy left, control console right with 3 dials, 1 fader, toggle
switch, amber #FFB000 VU readout, LED dots. Features as recessed panel
wells. Spec table in mono. ONE orange #F25C05 action button with press
state. No glassmorphism, no pastels, no neon glows, no leather textures.
```

## v0
```
Landing page, style: industrial skeuomorphism (Teenage Engineering revival,
not 2008 iOS). Override shadcn defaults: radius 8px, replace border/card
shadows with light-logic pairs — raised: border-top 1px rgba(255,255,255,.8),
border-bottom 1px rgba(0,0,0,.25), shadow 0 2px 2px rgba(0,0,0,.12); wells:
inset 0 2px 4px rgba(0,0,0,.25). Palette: bg #E8E9EB, panel #F2F3F4, well
#D7D9DC, text #1F2328, primary #F25C05 (buttons only), readout amber
#FFB000, LED dots 8px. Fonts: Space Grotesk headings / IBM Plex Sans body /
JetBrains Mono labels+readouts (10px uppercase +0.15em engraved). Split
hero with control console (dials, fader, switch), recessed feature wells,
mono spec table, 3 pricing panels, physical CTA. Switch motion 200ms
cubic-bezier(.2,.9,.3,.1.2) clunk; buttons invert inset on press. No glass,
no pastels, no rainbow neon, no emoji icons. Dark "rack unit" variant via
prefers-color-scheme + prefers-reduced-motion reset.
```