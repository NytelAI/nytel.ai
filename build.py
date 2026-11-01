#!/usr/bin/env python3
"""Render the site's static pages from templates/*.j2 and _data/messaging.yaml.

_data/messaging.yaml is a copy of NytelAI/knowledge-base marketing/messaging.yaml,
the single source of truth for shared marketing phrases. Edit it there, copy it
here, then run:

    pip install jinja2 pyyaml
    python3 build.py            # writes index.html, overview.html, llms.txt, _footer.html
    quarto render whitepaper.qmd   # only if whitepaper.qmd or _footer.html changed

GitHub Pages serves the committed output as-is, so commit the rendered files too.
"""
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

ROOT = Path(__file__).resolve().parent
OUTPUTS = {
    "index.html.j2": "index.html",
    "overview.html.j2": "overview.html",
    "_footer.html.j2": "_footer.html",
    "llms.txt.j2": "llms.txt",
}


def main() -> None:
    m = yaml.safe_load((ROOT / "_data" / "messaging.yaml").read_text(encoding="utf-8"))
    caps = m["capabilities"]
    items, agents = caps["items"], caps["mvp_agents"]["items"]
    # Order: compliance work leads, MVP agents next, protocol work last (never lead with protocol work alone).
    built = [items[0], items[1], *agents, items[2], items[3]]
    cal_url = next(l["url"] for l in m["links"] if "cal.com" in l["url"])

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(enabled_extensions=("html", "html.j2")),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
    )
    for src, dst in OUTPUTS.items():
        out = env.get_template(src).render(m=m, built=built, cal_url=cal_url)
        (ROOT / dst).write_text(out, encoding="utf-8")
        print(f"wrote {dst}")


if __name__ == "__main__":
    main()
