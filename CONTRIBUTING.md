# Contributing

Thanks for wanting to make this better. This repository is knowledge, not code,
so the bar is different: **a change is good if it makes an agent's output
measurably better, and bad if it only makes the documentation longer.**

---

## Before you open a PR

```bash
python3 scripts/validate.py          # what CI runs
node    scripts/screenshot.mjs       # render all 15 examples, catch overflow
```

The first is what CI runs. It checks every style folder, every required file, every
internal link, every generated file's freshness, and the 24-section structure
of the style DNAs.

---

## Principles

1. **Observable rules only.** Encode guidance as checkable predicates, not
   adjectives.
   - ✅ "Body text ≥ 16px, contrast ≥ 4.5:1, one `<h1>` per page"
   - ❌ "Buttons should feel clear and modern"
2. **Negative constraints do more work than positive ones.** "Not like this"
   removes a region of the solution space; "like this" gestures at a point.
   Keep the Do lists short and let the Don't lists carry the weight.
3. **Never make an unsupported claim.** No invented citations. No integration
   mechanism that has not been checked against the tool's own documentation.
   No statistics without a source. If you are not sure, write what you *do*
   know and say what is unverified.
4. **Do not flatten individuality.** The 15 styles share a structure, not a
   voice. Neumorphism warns about itself; Maximalism does not apologise. That
   is correct.
5. **Every addition costs context.** Before adding a paragraph, ask which
   context profile pays for it. If the answer is "all of them", it belongs in
   `AGENT-BOOTSTRAP.md` and needs to be one line.

---

## Generated files — never edit by hand

| Generated | Source | Regenerate with |
|---|---|---|
| `styles/*/tokens.json` | `styles/*/tokens.css` | `python3 scripts/gen_tokens.py` |
| `styles/*/tokens.tailwind.css` | `styles/*/tokens.css` | `python3 scripts/gen_tokens.py` |
| `styles/index.json` | data in `scripts/gen_manifest.py` | `python3 scripts/gen_manifest.py` |
| `design-taste.manifest.json` | data in `scripts/gen_manifest.py` | `python3 scripts/gen_manifest.py` |

CI fails if a generated file is out of date with its source.

---

## Adding style #16

Every style folder must contain exactly these six files:

```
styles/16-your-style/
├── README.md              the 24-section Design DNA
├── tokens.css             canonical tokens (source of truth)
├── tokens.json            generated
├── tokens.tailwind.css    generated
├── prompts.md             ready prompts for Codex / Claude / Lovable / v0
└── example.html           single-file, zero-dependency working page
```

### Checklist

- [ ] Directory named `NN-kebab-case-slug`, with `NN` the next free number.
- [ ] `README.md` follows [`docs/STYLE-TEMPLATE.md`](docs/STYLE-TEMPLATE.md)
      exactly — all 24 sections, in order, with the same headings.
- [ ] **§ 15 "When NOT to use" is filled in properly.** A style with no honest
      failure mode has not been thought about. This is the section reviewers
      read first.
- [ ] **§ 13 Accessibility names this style's specific failure**, not generic
      WCAG advice. What does *this* style get wrong that others do not?
- [ ] **§ 20 Signature move is concrete.** "One accent color used only for
      actions" is a signature move. "Bold and modern" is not.
- [ ] `tokens.css` defines every required category: colors, fonts, font-sizes,
      spacing, radius, shadows, borders, container, motion, motion-ease —
      including `--shadow-focus`.
- [ ] Light theme in `:root`, dark theme in `[data-theme="dark"]`.
- [ ] Contrast verified: every text/background pair used together passes
      4.5:1 (body) or 3:1 (large text and UI boundaries).
- [ ] `example.html` opens in a browser with no build step and no network
      dependency beyond webfonts, and holds at **1440 / 768 / 390 / 360** —
      verify with `node scripts/screenshot.mjs <your-style-id>`.
- [ ] Routing data added to `STYLES` in `scripts/gen_manifest.py`: aliases,
      density fit, recommended product types, supporting styles, incompatible
      styles, veto conditions and scoring weights.
- [ ] `DECISION-MATRIX.md` gains a scoring card, and `STYLE-COMBINATIONS.md`
      gains its safe and dangerous pairings.
- [ ] `visual-language/VISUAL-LANGUAGE-FOUNDATIONS.md § 10` gains an image
      direction row.
- [ ] `accessibility/ACCESSIBILITY.md § 10` gains a characteristic-failure row.
- [ ] `README.md` and `README.pl.md` style tables gain a row.
- [ ] `python3 scripts/gen_tokens.py && python3 scripts/gen_manifest.py && python3 scripts/validate.py`
      all pass.

### What gets a style rejected

- It is a variant of an existing style rather than a distinct design language.
  (A darker Minimalism is not style #16.)
- "When NOT to use" is empty, hedged, or says "any project where it doesn't fit".
- The tokens cannot pass contrast without abandoning the style's own premise —
  unless, like Neumorphism, the entry says so explicitly and scopes itself to
  decorative use.
- The example page only works at 1440px.

---

## Changing an existing style

Style DNAs are referenced by installed agents. Treat them like an API:

- **Adding** to a section: fine.
- **Changing** a token value: note it in `CHANGELOG.md` — someone has copied it.
- **Renaming or removing** a section: it must happen in all 15, and it is a
  breaking change.

---

## Improving the core documents

`SKILL.md`, `DECISION-MATRIX.md`, `ANTI-SLOP.md` and
`evaluation/DESIGN-TASTE-SCORE.md` are the system's contract. Changes there
need a reason expressed as a failure: *"an agent did X, and the rules allowed
it."* Include the failing case in the PR.

---

## Versioning

Semantic versioning on the skill version in `SKILL.md` frontmatter and
`design-taste.manifest.json` — keep both in step.

| Change | Bump |
|---|---|
| New style, new document, new rule | minor |
| Renamed or moved file, changed workflow contract, removed rule | **major** |
| Wording, examples, typos, expanded guidance | patch |

---

## Commit and PR

- Conventional-ish commit subjects (`feat:`, `fix:`, `docs:`, `style:`) are
  appreciated but not enforced.
- Describe **what an agent will do differently** after your change. That is the
  only reliable measure here.
- If you changed a style DNA, say whether you re-rendered its `example.html`.
