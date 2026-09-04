# 05 Neo-Brutalism — ready prompts

## Codex
```
Build a single-file HTML landing page for "Rampart" (a no-nonsense uptime
monitor for indie hackers). Style: neo-brutalism — flat colors, NO
gradients, NO shadows with blur. Every card/button: 2px solid #111 border
+ solid offset shadow "6px 6px 0 #111"; buttons press to translate(3px,3px)
with 3px shadow on hover, 120ms. Fonts: Archivo Black ALL-CAPS for H1
(64px) and H2, Space Grotesk 500 body 16px/1.6, Space Mono 12px uppercase
stamps (+0.1em). Palette: paper bg #FFFDF5, text #111, blocks yellow
#FFD02F (primary CTA), pink #FF90E8, blue #4D7CFE — max 3 block colors.
Layout: 1200px container, bordered navbar bar, giant caps hero on flat
color field with an overlapping status card, feature blocks with rotations
±1deg max, sticker-style 3-plan pricing, a mono marquee strip "99.9% UPTIME
— NO DASHBOARDS BLOAT — 2-MIN SETUP —", oversized footer. Radius 0.
Responsive: H1 36px on mobile, rotations to 0. Include
prefers-reduced-motion reset (stop marquee).
```

## Claude
```
Design a neo-brutalist landing page for Rampart, an uptime monitor for
indie hackers. The look: hard 2px black borders on everything, solid
offset shadows (Xpx Ypx 0 #111, never blurred), flat saturated color
blocks (yellow #FFD02F for actions, pink/blue accents — max 3), Archivo
Black uppercase headlines at 64px, Space Grotesk body, Space Mono stamps.
The signature interaction: buttons translate into their shadow on hover
(120ms). Structure it rigorously — the aggression sits on top of a strict
grid, blocks may rotate ±1deg only. Sections: color-band hero, 3 feature
blocks, pricing stickers, marquee strip, huge footer. One self-contained
HTML file, dark mode via prefers-color-scheme (invert border to paper
color), reduced-motion reset. No gradients, no glass, no soft shadows, no
more than 3 block colors.
```

## Lovable
```
Create a neo-brutalist landing page for "Rampart" (uptime monitoring for
indie hackers). Strict rules: radius 0, 2px #111 borders everywhere,
offset shadows solid with 0 blur (6px 6px 0 #111), hover press effect
translate(3px,3px). Fonts: Archivo Black (ALL-CAPS headings) + Space
Grotesk body + Space Mono uppercase labels. Bg #FFFDF5, blocks #FFD02F /
#FF90E8 / #4D7CFE only. Sections: hero with giant caps + overlapping
status card (rotated 1deg), 3 feature blocks, sticker pricing cards, mono
uppercase marquee, big footer. No gradients, no blur shadows, no
glassmorphism, no 4th color. Mobile: H1 36px, no rotation.
```

## v0
```
Landing page, style: neo-brutalism (Gumroad-like). Override shadcn
defaults: radius 0, border-width 2px, border-color #111, shadows must be
solid offsets "6px 6px 0 #111" (no blur, no opacity). Buttons: bg #FFD02F,
press to translate(3px,3px) on hover, 120ms. Fonts: Archivo Black
ALL-CAPS H1/H2, Space Grotesk body, Space Mono 12px uppercase stamps.
Page bg #FFFDF5, block colors limited to #FFD02F, #FF90E8, #4D7CFE.
Sections: flat hero band, 3 bordered feature blocks, sticker pricing,
marquee strip, oversized footer. Blocks rotate max ±1deg. No gradients,
no glass cards, no pastel softening.
```