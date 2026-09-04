#!/usr/bin/env python3
"""Generate tokens.json + tokens.tailwind.css from each style's tokens.css."""
import re, json, sys, os

def parse_tokens(css_path):
    text = open(css_path, encoding="utf-8").read()
    blocks = re.findall(r'(:root|\[data-theme="dark"\])\s*\{([^}]+)\}', text)
    out = {}
    for name, body in blocks:
        theme = "light" if name == ":root" else "dark"
        toks = {}
        for k, v in re.findall(r'(--[\w-]+)\s*:\s*([^;]+);', body):
            toks[k] = v.strip()
        out[theme] = toks
    return out

def categorize(tokens):
    cats = {}
    for k, v in tokens.items():
        if k.startswith("--color-"): cats.setdefault("colors", {})[k[7:]] = v
        elif k.startswith("--font-size-"): cats.setdefault("fontSizes", {})[k[11:]] = v
        elif k.startswith("--font-"): cats.setdefault("fonts", {})[k[6:]] = v
        elif k.startswith("--spacing-"): cats.setdefault("spacing", {})[k[10:]] = v
        elif k.startswith("--radius-"): cats.setdefault("radius", {})[k[8:]] = v
        elif k.startswith("--shadow-"): cats.setdefault("shadows", {})[k[8:]] = v
        elif k.startswith("--border-"): cats.setdefault("borders", {})[k[8:]] = v
        elif k.startswith("--motion-"): cats.setdefault("motion", {})[k[8:]] = v
        elif k.startswith("--container-"): cats["containerWidth"] = v
    return cats

def tailwind(cats):
    lines = ["@import \"tailwindcss\";", "@theme {"]
    for cat in ("colors", "fonts", "fontSizes", "spacing", "radius", "shadows"):
        for k, v in cats.get(cat, {}).items():
            tk = k.replace("-", "-")  # keep kebab; tw v4 maps namespaced vars
            lines.append(f"  --{cat.rstrip('s')}-{tk}: {v};")
    lines.append("}")
    return "\n".join(lines)

root = "/home/aibot/repos/agent-design-taste"
import glob, os
for css in sorted(glob.glob(f"{root}/styles/*/tokens.css")):
    d = os.path.dirname(css)
    toks = parse_tokens(css)
    data = {"name": os.path.basename(d), "light": categorize(toks.get("light", {})), "dark": categorize(toks.get("dark", {}))}
    with open(f"{d}/tokens.json", "w") as f:
        json.dump(data, f, indent=2)
    with open(f"{d}/tokens.tailwind.css", "w") as f:
        f.write(tailwind(data["light"]) + "\n")
    print("ok", d)