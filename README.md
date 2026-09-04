# 🎨 Agent Design Taste

**Design library + decision system + AI-agent skill that teaches agents to produce UI with *taste* — instead of generic "modern premium AI SaaS" output.**

15 fully-documented design styles. Each style ships with: visual principles, when/when-not to use, font pairings, color/spacing/radius/shadow/border specs, layout & component patterns, good vs bad examples, Do/Don't lists, ready-to-paste prompts for **Codex / Claude / Lovable / v0**, design tokens (CSS variables), and a working example landing page (HTML file you can open instantly).

Plus **SKILL.md** — a procedural skill any AI agent can load to first analyze the *product and audience*, then *choose the right style*, then generate.

---

## Why this repo exists

AI-generated UI all looks the same: dark background, purple-to-blue gradient, glassy cards, Inter font, "Lorem ipsum" hero with a floating 3D shape. It's not that agents can't design — it's that nobody gave them a *taste system*.

This repo is that system:

1. **Analyze first.** Product, audience, emotion, industry, context.
2. **Decide.** Pick a style from a structured decision tree (not vibes).
3. **Generate.** With real constraints: tokens, type scale, Do/Don't, anti-slop rules.

---

## Structure

```
agent-design-taste/
├── README.md                  ← you are here
├── SKILL.md                   ← load this into any agent (Codex/Claude/etc.)
├── DECISION-MATRIX.md         ← product/audience → style decision system
├── ANTI-SLOP.md               ← universal rules that kill generic AI UI
├── styles/                    ← 15 styles, one folder each
│   ├── 01-minimalism/
│   │   ├── README.md          ← principles, when/not, do/don't, examples
│   │   ├── tokens.css         ← design tokens (CSS variables)
│   │   ├── prompts.md         ← ready prompts for Codex/Claude/Lovable/v0
│   │   └── example.html       ← working example landing page
│   ├── 02-glassmorphism/
│   ├── ...
│   └── 15-expressive-kinetic-typography/
└── assets/
    └── decision-tree.png      (optional visual)
```

Each style folder is **self-contained**: an agent can read just one folder and produce correct output in that style.

---

## The 15 styles

| # | Style | One-line identity | Best for |
|---|-------|-------------------|----------|
| 01 | [Minimalism](styles/01-minimalism/) | Less but better | B2B SaaS, premium products |
| 02 | [Glassmorphism](styles/02-glassmorphism/) | Translucent. Layered. Modern. | Dev tools, dashboards |
| 03 | [Liquid Glass](styles/03-liquid-glass/) | Fluid light and motion | Consumer apps, creative tools |
| 04 | [Bento Grid](styles/04-bento-grid/) | Modular organized blocks | Feature-rich products, landing pages |
| 05 | [Neo-Brutalism](styles/05-neo-brutalism/) | Bold raw unconventional | Youth brands, creative studios |
| 06 | [Brutalist / Anti-Grid](styles/06-brutalist-anti-grid/) | Break the grid on purpose | Portfolios, agencies, art |
| 07 | [Neumorphism](styles/07-neumorphism/) | Soft extruded surfaces | Simple utility apps (sparingly) |
| 08 | [Claymorphism](styles/08-claymorphism/) | Playful puffy 3D | Kids, education, friendly apps |
| 09 | [Skeuomorphism / Tactile](styles/09-skeuomorphism-tactile/) | Looks like the real thing | Audio, finance, retro tools |
| 10 | [Swiss / International](styles/10-swiss-international/) | Grid, type, order | Agencies, architecture, editorial |
| 11 | [Editorial / Magazine](styles/11-editorial-magazine/) | Reads like a magazine | Media, blogs, long-form |
| 12 | [Maximalism](styles/12-maximalism/) | More is more | Fashion, events, culture |
| 13 | [Y2K / Retrofuturism](styles/13-y2k-retrofuturism/) | Chrome, bubble, optimism | Music, streetwear, gaming |
| 14 | [3D / Spatial UI](styles/14-3d-spatial-ui/) | Depth you can move through | Web3, products, immersive tools |
| 15 | [Expressive / Kinetic Typography](styles/15-expressive-kinetic-typography/) | Type as the interface | Portfolios, campaigns, motion-first |

---

## Quick start (for an AI agent)

```
1. Read SKILL.md
2. Follow the workflow: analyze product → use DECISION-MATRIX.md → pick style
3. Load styles/<chosen>/README.md + tokens.css + prompts.md
4. Apply ANTI-SLOP.md rules during generation
5. Validate output against the style's Do/Don't checklist
```

## Quick start (for a human)

- Browse the [styles table](#the-15-styles) and open a folder.
- Copy `tokens.css` into your project.
- Steal from `example.html`.
- Or paste a `prompts.md` entry straight into Codex / Claude / Lovable / v0.

---

## For agent builders

**Claude / Hermes skills:** point the agent at `SKILL.md` (it's written as a procedural skill with a trigger, workflow, and quality gates).

**System prompt injection:** `DECISION-MATRIX.md` + `ANTI-SLOP.md` + the chosen style's `README.md` is ~2-3k tokens — cheap enough to inject per-task.

**MCP/RAG:** every file is markdown, deterministic, and self-contained — index `styles/` and retrieve per style name.

---

## Rules of the road

- Every style folder must answer: *when NOT to use this style*.
- Tokens are canonical: if `README.md` and `tokens.css` disagree, `tokens.css` wins.
- Example pages are single-file HTML, zero dependencies, open-in-browser.
- Prompts are tested patterns, not aspirations — concise, constraint-first.

## License

MIT © [AI Evolution Labs](https://github.com/aievolutionpl)
