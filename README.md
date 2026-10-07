# Designing an siRNA against TTR — a worked case study

A live demo page for the [siRNA Toolkit](https://sirna-toolkit.streamlit.app),
walking the whole design process against transthyretin — the rare gene that
already has **two approved siRNA drugs**, patisiran (2018) and vutrisiran
(2022), developed a decade apart. They bind nine nucleotides apart and have
almost nothing in common chemically, which makes them an unusually good
answer key.

Both versions are published from this repo via GitHub Pages:

| | | |
|---|---|---|
| **[Interactive](https://kercheric.github.io/sirna-ttr-demo/)** | ~12 MB first load | Real Python in your browser. Move the controls and the figures and captions recompute. |
| **[Lightweight](https://kercheric.github.io/sirna-ttr-demo/fast/)** | ~300 KB | One file, instant on a slow connection. Figures fixed at their defaults. |

The lightweight build is the one to put behind a QR code at a poster — venue
wifi rarely rewards a 12 MB download. The interactive build is the one to
link from a homepage.

## What's live

The page is driven by one frozen data package, so every number comes from a
real pipeline run rather than being recomputed in the browser:

| section | behaviour |
|---|---|
| 1 — Walk the transcript | **live** GC window; map, points and caption recompute |
| 2 — Choose your candidates | **live** shortlist depth; reports when each drug is admitted |
| 3 — Pre-clinical tox package | **live** species requirement; survivors recounted and remapped |
| 4 — Chemistry | pre-rendered duplex drawing (SVG) |
| 5 — Clinical panel | precomputed values, **live** gene filter |

Sections 4 and 5 are precomputed on purpose. The duplex drawing needs a
headless browser to render, and the chemistry re-score needs a 4 MB random
forest — neither survives in a WebAssembly runtime. Both are still shown,
just not recomputed.

## How it works

`poster_demo.py` is a [marimo](https://marimo.io) notebook with **no
dependency on the toolkit codebase**. Its entire import surface is
`marimo`, `pandas` and `plotly`, and the whole dataset — 597 candidates,
eight species, both clinical panels and the duplex drawing — is embedded in
the file as 23 KB of gzipped base64.

That is what lets it run in a browser. The scientific pipeline behind it
needs ViennaRNA, scikit-learn, MAFFT, a headless Chromium and NCBI access,
none of which exist in WebAssembly, so all of it runs ahead of time and only
the results ship.

The notebook detects which build it is in (Pyodide reports
`sys.platform == "emscripten"`) and adjusts its own description of whether
the controls work, so the two pages can't make contradictory claims.

## Rebuilding

```bash
pip install marimo pandas plotly
python build.py
```

That writes the interactive build to the repo root and the lightweight one
to `fast/`. Commit and push; GitHub Pages serves from `main` at the root.

To refresh the **data** rather than the presentation, regenerate the package
from the toolkit repo:

```bash
python poster_figures/build_demo_data.py   # in the sirna-toolkit repo
```

It sources the TTR table from `demo/demo_ttr_df.parquet` — the toolkit's own
canonical demo capture — and writes the JSON *and* re-embeds it into
`poster_demo.py` in one pass, so the two can't drift. Copy the updated
notebook here and re-run `build.py`.

## Data

Transthyretin, `NM_000371.4`, 616 nt, 597 candidate guides. Scores, homology
calls and clinical percentiles come from the siRNA Toolkit pipeline. Drug
sequences and modification patterns are the published ones and are scored by
exactly the same machinery as every other candidate — nothing here is a
simulation.

Pipeline source and licence: the toolkit repository. This repo contains only
the generated demo page.
