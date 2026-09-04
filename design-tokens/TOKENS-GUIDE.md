# Design Tokens Guide

Three canonical formats per style — keep them in sync:

- `styles/<style>/tokens.css` — CSS variables (source of truth)
- `styles/<style>/tokens.json` — JSON (for design tools, JS, Figma plugins)
- `styles/<style>/tokens.tailwind.css` — Tailwind v4 `@theme` block

## Token categories (all styles must define)

| Category | Prefix | Example |
|---|---|---|
| Colors | `--color-` | `--color-primary: #0F172A;` |
| Fonts | `--font-` | `--font-display: 'Fraunces', serif;` |
| Font sizes | `--font-size-` | `--font-size-h1: 64px;` |
| Spacing | `--spacing-` | `--spacing-4: 16px;` |
| Radius | `--radius-` | `--radius-card: 12px;` |
| Shadows | `--shadow-` | `--shadow-card: 0 2px 8px rgb(0 0 0 / .08);` |
| Borders | `--border-` | `--border-default: 1px solid #E2E8F0;` |
| Container | `--container-width` | `1280px` |
| Motion | `--motion-` | `--motion-fast: 150ms;` |

## Rules

1. `tokens.css` is canonical — if docs and tokens disagree, tokens win.
2. Light mode in `:root`, dark mode in `[data-theme="dark"]` (or `@media (prefers-color-scheme: dark)` fallback documented in the file).
3. No ad-hoc values in components: if you type `13px` or `#7c3aed` in a
   component, it must exist as a token (or the tokens are wrong — fix tokens).
4. Contrast: every text/background token pair used together must pass 4.5:1
   (body) / 3:1 (large text).
5. Tailwind v4 usage:

```css
@import "tailwindcss";
@theme {
  --color-primary: #0F172A;
  --font-display: "Fraunces", serif;
  /* then use: bg-primary, font-display */
}
```

## Naming convention

Semantic over literal where hierarchy matters (`--color-text-secondary`,
not `--color-gray-500`); literal scales allowed for spacing only.
