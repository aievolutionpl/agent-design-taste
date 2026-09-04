# 12 Maximalism — ready prompts

## Codex
```
Build a single-file HTML landing page for "Cacophony" (independent music
festival, Aug 14–16). Style: deliberate maximalism — layered richness,
pattern mixing, controlled chaos. Fonts: Fraunces 900 for oversized H1
(72px/0.95, may overlap imagery, one line uses outlined text via
-webkit-text-stroke), Archivo for body 17px/1.65, Space Mono for 12px
uppercase stamp labels (+0.12em). Palette: cream bg #FDF6EC, ink
#1A0B2E, vermilion primary #E8442E, accents marigold #FFB000 / violet
#7B2FA0 / teal #0FA3A3 (max 3 accents per screen). Structure: 12-col
grid underneath everything; full-bleed pattern hero (checker + dots
CSS patterns) with one rotated sticker; marquee ticker strip; dense
3-col lineup mosaic cards with 2px borders and hard offset shadows
(4px 4px 0 ink); poster-like pricing/tickets with featured plan on
pattern background. Radius: pill (999px) only — no 8px defaults. NO
soft shadows, no glassmorphism, no gradient blobs, no emoji confetti.
Hover: 200ms spring, scale 1.04 + shadow shift. Marquee pauses on
hover. Include prefers-reduced-motion reset (stop marquee/wiggles).
```

## Claude
```
Design a maximalist landing page for Cacophony, an indie music festival.
Maximalism = abundance with discipline: saturated color fields as
section backgrounds, mixed patterns (checkerboard, halftone dots,
zigzag borders — all in one shared palette), oversized Fraunces Black
type layered over imagery, rotated sticker badges, hard offset shadows
(never soft blur). Every section has ONE dominant idea; density is
ranked (hero loudest, support quieter); exactly one element may break
the grid per section. Body text stays plain 17px Archivo for
readability. Three font families max, contrasted by classification.
Palette: cream #FDF6EC, plum-black #1A0B2E, vermilion #E8442E +
max 3 accents. Deliver as one self-contained HTML file with dark mode,
pausing marquee, and a full prefers-reduced-motion reset. Do not use
glass, gradient meshes, emoji decorations, or corporate stock photos.
```

## Lovable
```
Create a maximalist landing page for "Cacophony" music festival. Rules:
cream bg #FDF6EC, ink #1A0B2E, 2px borders everywhere, hard offset
shadows (4px 4px 0 ink — NO soft shadows), pill radius only. Fonts:
Fraunces 900 (huge headlines), Archivo (body), Space Mono (uppercase
stamps). Patterns via CSS (checkerboard, polka dots) in shared palette;
rotated sticker badges (-4°). Sections: pattern hero + marquee ticker,
3-col lineup card mosaic, tickets pricing (featured plan has pattern
bg + 8px shadow), CTA band. Max 3 accent colors (#FFB000, #7B2FA0,
#0FA3A3). One grid-breaking element per section max. No glass, no
purple-blue gradients, no emoji walls. Add prefers-reduced-motion reset.
```

## v0
```
Landing page, style: editorial maximalism (festival poster energy).
Override shadcn defaults: radius = 999px pill (no 8px), borders 2px
solid #1A0B2E, shadows = hard offset (shadow-[4px_4px_0_#1A0B2E], never
blur). Fonts: Fraunces 900 headings (72px hero, tight leading), Archivo
body 17px, Space Mono 12px uppercase labels. Palette: bg #FDF6EC,
primary #E8442E, accents #FFB000/#7B2FA0/#0FA3A3 — no purple-blue mesh.
Sections: full-bleed CSS-pattern hero (checkerboard + dots), marquee
ticker (pause on hover), dense lineup mosaic, ticket pricing with
pattern-backed featured card, CTA band. One rotated/sticker element per
section. Use Lucide icons, single family. Include reduced-motion reset.
```