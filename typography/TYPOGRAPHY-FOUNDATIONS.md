# Typography Foundations

Cross-style rules that every style's DNA builds on.

## Font role model

Every design needs an explicit role assignment:

| Role | Purpose | Typical families |
|---|---|---|
| **Display/Headline** | Personality, H1-H2 | Fraunces, Playfair, Space Grotesk, Archivo Black, Orbitron |
| **Text/Sans** | Body, UI | Inter, Söhne-like (Instrument Sans), Jakarta Sans, IBM Plex Sans |
| **Serif (editorial)** | Long-form reading, luxury | Fraunces, Newsreader, Source Serif, EB Garamond |
| **Grotesk (Swiss)** | Neutral structure | Inter, Archivo, Neue Haas-like |
| **Mono** | Code, labels, data | JetBrains Mono, IBM Plex Mono, Space Mono |
| **Display (expressive)** | Kinetic/Y2K statements | Unbounded, Clash-like (Archivo Expanded), Monoton |

## Rules

1. **Max 2-3 families** per project (display + text, optionally mono).
2. **Modular scale**: use ratios — 1.25 (major third) for dense UI, 1.333 (perfect fourth) for marketing pages. Example scale (1.333): 12, 16, 21, 28, 38, 50, 67px.
3. **Body**: 16-18px, line-height 1.5-1.7, measure 60-75 characters.
4. **Letter-spacing**: negative on large display (-0.02em to -0.04em), positive on small caps labels (+0.08em), never touch body text.
5. **Uppercase**: eyebrows/labels/buttons ≤ 12px only. Never headings > 24px in all caps, never body.
6. **Line-height**: tighter as size grows (H1: 1.05-1.15; body: 1.5-1.7).
7. **Weight range**: pick a family with ≥ 4 weights; use 3 (regular/semibold/bold). "Light on dark" display only above 32px.

## Common typographic failures (AI fingerprint)

- Inter at literally every size and weight — zero personality.
- `letter-spacing: normal` on a 64px display headline (too tight, collisions).
- All-caps H1 with +0.05em spacing on a serif — reads as shouting.
- Body at 14px because "it fits" — kills readability.
- Line-length > 90 characters — scanning dies.

## Per-style pointers

Full font specs live in each `styles/<style>/README.md` § Typography. This
file is the shared baseline; the style DNA overrides where it differs.