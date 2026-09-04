# 02 Glassmorphism — ready prompts

## Codex
```
Build a single-file HTML landing page for "Pulse" (a music-streaming app).
Style: glassmorphism, but disciplined — MAX 2 glass surfaces per view
(navbar + one hero panel), everything else solid. Background: vivid
indigo→magenta gradient (#6366F1 → #EC4899) with two soft radial glows.
Glass recipe: rgb(255 255 255 / 0.12) bg, backdrop-filter blur(20px)
saturate(160%), 1px border rgb(255 255 255 / 0.25), radius 20px, shadow
0 8px 32px rgb(0 0 0 / .12). Fonts: Plus Jakarta Sans 700 for H1/H2
(-0.02em), Inter body 17px/1.6, JetBrains Mono 12px uppercase eyebrows
(+0.08em). Text near-white #F8FAFC, secondary #94A3B8. CTA = solid
accent fill (#A78BFA on dark), never glass buttons. Sections: split
hero (glass "now playing" card right, headline on solid left), 3 solid
feature cards, solid pricing, CTA band, footer. Dark theme. No nested
glass, no glass inputs/tables, no light font weights on glass. Hover:
brightness 1.05, 200ms. Guard with @supports (backdrop-filter) +
solid fallback; drop to 1 glass surface under 720px. Include
prefers-reduced-motion reset (freeze gradient drift).
```

## Claude
```
Design a glassmorphism landing page for Pulse, a music-streaming app.
Constraint first: readability beats decoration — count the glass surfaces,
cap at 2 (navbar + hero panel), all other surfaces solid with 1px borders.
Vivid indigo→magenta gradient backdrop; glass = blur(20px) saturate(160%),
white-alpha border, 20px radius. Type: Plus Jakarta Sans headings, Inter
body, JetBrains Mono labels; near-white text, one accent for solid CTAs.
Every text-on-glass pairing must pass AA contrast against the worst spot
of the gradient behind it. Deliver one self-contained HTML file, dark
theme, responsive (solid fallbacks on small screens), reduced-motion
reset. Do not use glass buttons, inputs, or card grids — that's slop.
```

## Lovable
```
Create a landing page for "Pulse" (music-streaming app) in restrained
glassmorphism. Hard rules: maximum 2 translucent/glass elements per
screen (navbar + one hero card); all other cards solid (#1E293B) with
1px rgba(255,255,255,0.10) borders. Background: linear-gradient
indigo #6366F1 → magenta #EC4899 with two blurred radial glows. Glass:
rgba(255,255,255,0.12) + backdrop-blur 20px + border rgba(255,255,255,0.25),
radius 20px. Fonts: Plus Jakarta Sans (headings), Inter (body 17px/1.6).
CTA solid #A78BFA, never translucent. Sections: split hero, 3 features,
pricing, CTA band. No purple-gradient-text, no neon orbs, no glass grids.
Mobile: replace glass with solid surfaces.
```

## v0
```
Landing page, style: dark glassmorphism (restrained). Override shadcn
defaults: background = indigo→magenta gradient (#6366F1→#EC4899) with
radial glows; card = solid #1E293B with border-white/10 by default; ONLY
the navbar and one hero panel get glass treatment (bg-white/10,
backdrop-blur-xl, border-white/25, rounded-3xl, shadow-xl). Font: Plus
Jakarta Sans headings / Inter body. Buttons: solid primary #A78BFA,
never translucent. Split hero with a "now playing" glass card, 3 solid
feature cards, pricing, CTA band. Max 2 glass surfaces per view — enforce
it. No gradient text, no glass inputs, no nested glass. Add reduced-motion
handling for any background animation.
```