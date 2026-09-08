# Design Tokens Guide

Three formats per style. **`tokens.css` is the source of truth**; the other two
are generated from it and verified in CI.

| File | Role | Edit? |
|---|---|---|
| `styles/<style>/tokens.css` | CSS custom properties — **canonical** | yes |
| `styles/<style>/tokens.json` | JSON, for design tools and JS | **generated** |
| `styles/<style>/tokens.tailwind.css` | Tailwind v4 `@theme` block | **generated** |

```bash
python3 scripts/gen_tokens.py     # after any tokens.css change
```

---

## Required categories

Every style must define all of these. `scripts/validate.py` enforces it.

| Category | Prefix | Example |
|---|---|---|
| Colors | `--color-` | `--color-primary: #0F172A;` |
| Fonts | `--font-` | `--font-display: 'Fraunces', serif;` |
| Font sizes | `--font-size-` | `--font-size-h1: 64px;` |
| Spacing | `--spacing-` | `--spacing-4: 16px;` |
| Radius | `--radius-` | `--radius-card: 12px;` |
| Shadows | `--shadow-` | `--shadow-card: 0 2px 8px rgb(0 0 0 / .08);` |
| Borders | `--border-` | `--border-default: 1px solid var(--color-border);` |
| Container | `--container-` | `--container-width: 1280px;` |
| Motion | `--motion-` | `--motion-fast: 150ms;` |
| Easing | `--motion-ease*` | `--motion-ease: cubic-bezier(0.16, 1, 0.3, 1);` |

**`--shadow-focus` is mandatory** — a missing focus indicator is an
accessibility blocker, so the token that provides it is not optional.

Minimum color roles: `bg` · `surface` · `text` · `text-secondary` · `border` ·
`primary` · `primary-contrast` · `accent` · `accent-contrast` · `success` ·
`warning` · `error`.

---

## Rules

1. **Tokens are canonical.** If a style's `README.md` and its `tokens.css`
   disagree, the token wins and the README is a bug to fix.
2. **Light in `:root`, dark in `[data-theme="dark"]`.** The generator reads
   exactly these two blocks. A `prefers-color-scheme` fallback belongs in the
   consuming project, and should be documented where it is added.
3. **No ad-hoc values.** If you type `13px` or `#7c3aed` in a component, either
   it should be a token or the tokens are wrong. Fix the tokens.
4. **Contrast is part of the token contract, and it is enforced.**
   `python3 scripts/check_contrast.py` measures every text/background pair and
   every focus indicator in both themes, and CI fails on a miss. It resolves the
   dark palette as light-then-dark (dark blocks are partial overrides) and
   composites translucent colors before measuring — a ring at 35% opacity is
   measured as what it actually paints, not as the hue it was authored in.
   A style that genuinely cannot pass a pair adds a waiver **with a reason**
   rather than silencing the check. See `accessibility/ACCESSIBILITY.md`.

   Not checked at 3:1: `--color-border` against surfaces. WCAG 1.4.11 requires
   that of boundaries *needed to identify a component*, not of every hairline —
   dividers and subtle card edges are exempt, and failing all 15 styles on it
   would get the check switched off. `--shadow-focus` carries that requirement
   instead, and it is checked.
5. **Semantic over literal** where hierarchy matters: `--color-text-secondary`,
   not `--color-gray-500`. Literal scales are fine for spacing.

---

## Tailwind v4

The generator maps our categories onto Tailwind's theme namespaces, so the
variables actually produce utilities rather than sitting inert:

| Our category | Tailwind namespace | Generates |
|---|---|---|
| `--color-*` | `--color-*` | `bg-*`, `text-*`, `border-*` |
| `--font-*` | `--font-*` | `font-*` |
| `--font-size-*` | `--text-*` | `text-*` |
| `--spacing-*` | `--spacing-*` | `p-*`, `m-*`, `gap-*` |
| `--radius-*` | `--radius-*` | `rounded-*` |
| `--shadow-*` | `--shadow-*` | `shadow-*` |
| `--motion-ease*` | `--ease-*` | `ease-*` |
| `--container-*` | `--container-*` | `max-w-*` |

Motion durations and border shorthands have no Tailwind namespace, so the
generator emits them as plain custom properties in a `:root` block beneath the
`@theme` block — use them with `var()`.

```css
@import "tailwindcss";

@theme {
  --color-primary: #0F172A;
  --font-display: "Fraunces", serif;
  --text-h1: 56px;
  --radius-lg: 12px;
}
/* then: bg-primary · font-display · text-h1 · rounded-lg */
```

---

## Using tokens in a project that already has some

Do **not** paste a style's tokens over an existing system. Run
ANALYZE → MAP → ADAPT from `docs/PRECEDENCE.md`:

- Map our names onto theirs. **Theirs win** — you are adopting their vocabulary.
- Add only tokens that are genuinely missing.
- Never introduce a second spacing scale, a second radius scale, or a third
  font family into a project that already has them.
- A missing decision (no dark mode, no focus ring) is a **gap to flag**, not a
  blank to fill silently.
