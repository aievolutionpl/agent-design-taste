# 13 Y2K Retrofuturism — ready prompts

## Codex
```
Build a single-file HTML landing page for "Bloop" (a fun consumer audio
app). Style: Y2K retrofuturism — the future as imagined from 1999. Fonts:
Orbitron 700 for headings (letter-spacing 0.03em; H1 56px chrome text via
background:linear-gradient(180deg,#EAF6FF,#9FB8CC 55%,#3A4A5C) +
background-clip:text), Space Grotesk body 16px/1.6, Space Mono for 12px
uppercase readout labels (+0.14em). Palette: ice-blue bg #E8F1F8, ink
#1B2A3A, electric blue primary #3B5BDB, pastel accents #C77DFF/#64E0D4/
#FFB8D1. Chrome and iridescence MUST be CSS gradients — no image files.
Structure: centered hero over soft iridescent sky gradient
(linear-gradient(135deg,#FFB8D1,#E3D0FF 35%,#A8E8FF 65%,#B8FFE3)), pill
floating navbar, bubble feature cards with bezel effect
(box-shadow: inset 0 2px 2px rgb(255 255 255/.8), inset 0 -3px 4px
rgb(0 0 0/.12)) and window-chrome headers (3 dots + mono title),
device-panel hero mock, capsule glowing CTA, status-bar footer with LED
dots + mono readout. Chrome reserved for H1 + primary CTA only. Hover:
200ms glow bloom + scale 1.03. Add prefers-reduced-motion reset (stop
shimmer/bobbing/blink). NO glassmorphism blur, NO purple-blue mesh, NO
matrix green, NO hard offset shadows.
```

## Claude
```
Design a Y2K retrofuturism landing page for Bloop, a consumer audio app.
Era logic: optimistic 1999 tech — everything plastic-glossy, pill-shaped,
bezelled. Build chrome and iridescence purely with CSS gradients (chrome
text = vertical metallic gradient with background-clip:text; iridescent
sky = soft 4-stop pastel gradient). Use Orbitron (headings) + Space
Grotesk (body) + Space Mono (uppercase system readouts, blinking-cursor
labels). Hierarchy rule: chrome on H1 and primary capsule CTA only;
all cards/panels stay matte white with inset bezel highlights and 24px+
radii. Layout: centered hero, bubble feature triads, device-panel mock
(nested surface with dot-matrix header), pricing with iridescent
gradient-border featured card, LED status-bar footer. Max 2 ambient
animations (6s bob, 4s shimmer), both disabled under
prefers-reduced-motion. Deliver one self-contained HTML file with dark
mode (deep navy sky, chrome value range preserved). No glass blur, no
neon hacker green, no gradient body text, no image-based textures.
```

## Lovable
```
Create a Y2K retrofuturism landing page for "Bloop" (consumer audio app).
Rules: ice-blue bg #E8F1F8, iridescent sky gradients via CSS only
(#FFB8D1→#E3D0FF→#A8E8FF→#B8FFE3), chrome text on H1 via metallic
gradient + background-clip:text. Fonts: Orbitron headings, Space Grotesk
body 16px, Space Mono uppercase readouts. Everything pill-shaped (999px
nav, buttons, badges); cards get bezel gloss (inset white highlight +
inset dark bottom shadow), 24px radius, optional window-chrome header
with 3 dots. Primary #3B5BDB glow on hover. Sections: centered hero with
device-panel mock, 3 bubble features, pricing (featured card with
iridescent gradient border), status-bar footer with LED dots. Chrome
only on H1 + main CTA. No glassmorphism, no purple mesh, no neon green.
Include prefers-reduced-motion reset.
```

## v0
```
Landing page, style: Y2K retrofuturism (1999 tech optimism). Override
shadcn defaults: radius 24px+ (pills 999px), shadows soft + inset bezel
(shadow-[inset_0_2px_2px_rgb(255_255_255/0.8),inset_0_-3px_4px_rgb(0_0_0/0.12)]),
NO hard offset shadows. Fonts: Orbitron headings, Space Grotesk body,
Space Mono 12px uppercase readouts. Palette: bg #E8F1F8, primary #3B5BDB,
pastel accents #C77DFF/#64E0D4/#FFB8D1. Chrome + iridescence as CSS
gradients only (H1: metallic gradient text; hero sky: pastel 4-stop
gradient). Chrome reserved for H1 + primary CTA. Pill navbar, bubble
feature cards with window-chrome headers, device-panel hero mock,
pricing with gradient-border featured plan, LED status-bar footer.
Hover: 200ms glow + scale 1.03. Add reduced-motion reset; no glass
blur, no purple-blue mesh, no matrix green, no emoji decorations.
```