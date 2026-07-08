# BSSDH 2026-book

Workshop materials for BSSDH 2026, published as a [Jupyter Book](https://jupyterbook.org/) on GitHub Pages.

**Live site:** https://lrskjr.github.io/BSSDH2026-book/

## Contents

- OpenRefine workshop guide
- Orange Data Mining workshop guide
- Downloadable data files and Orange workflows (.ows)
- Instructor sequence plans (English)

## Build locally

```bash
pip install -r requirements.txt
python scripts/convert_md.py   # re-convert from Obsidian vault if source changed
jupyter-book build . --all
```

Open `_build/html/index.html` in a browser.

## Publish

Push to `main` on GitHub. The workflow in `.github/workflows/deploy-book.yml` builds and deploys to GitHub Pages automatically.

## Source material

- English markdown: `vault_1/BSSDH/` (Obsidian)
- Data and Orange files: `BSSDH2026/data/Makslu kritika/bssdh openrefine and orange final/`

Danish versions are kept in the Obsidian vault only.
