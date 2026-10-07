# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "pandas",
#     "plotly",
# ]
# ///
#
# PEP 723 inline metadata. marimo reads this to know what to install, and
# a WebAssembly build micropip-installs exactly this list -- without it
# plotly is simply absent in the browser and every figure cell dies with
# ModuleNotFoundError while the markdown still renders.
#
# Keep the list minimal and pure-Python: numpy and pandas ship inside
# Pyodide, plotly is a py3-none-any wheel. Anything needing a C
# extension built against CPython (ViennaRNA, scikit-learn's model
# loading, kaleido) cannot be added here -- which is why this notebook
# reads precomputed data instead.
import marimo

__generated_with = "0.25.1"
app = marimo.App(
    width="medium",
    app_title="Designing an siRNA against TTR",
)


@app.cell(hide_code=True)
def _():
    # Self-contained interactive build of the TTR case study.
    #
    # This notebook imports NOTHING from the toolkit. Every number it
    # shows was computed once by build_demo_data.py and frozen into
    # poster_demo_data.json; everything here is drawing and filtering.
    #
    # The point of that split is reach. With only pandas and plotly as
    # dependencies -- both pure-Python or already inside Pyodide -- the
    # notebook runs in a browser via WebAssembly, so the controls stay
    # live on a published page with no server behind it.
    #
    # Deliberately absent, because none of them survive in a browser:
    # ViennaRNA, scikit-learn, kaleido/chromium, MAFFT, NCBI. The duplex
    # drawing needs chromium to render, so it is pre-exported to SVG and
    # embedded; the chemistry re-score needs the 4 MB random forest, so
    # its results are precomputed. Both are still shown, just not
    # recomputed.
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _():
    # The whole data package, gzipped and base64'd -- 22.7 KB of text for
    # 597 candidates, eight species, both panels and the duplex drawing.
    #
    # Written here by build_demo_data.py; do not edit by hand. It exists
    # so the published notebook is ONE file with no network dependency:
    # a WebAssembly build runs in the visitor's browser, where there is
    # no filesystem to read poster_demo_data.json from and no safe way
    # to authenticate a fetch (any token shipped to a browser is public).
    #
    # Nothing in here is sensitive -- transcript positions, GC content,
    # published homology calls and approved-drug percentiles.
    # --- BEGIN EMBEDDED DATA (generated) ---
    DATA_B64 = "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"
    # --- END EMBEDDED DATA ---
    return (DATA_B64,)


@app.cell(hide_code=True)
def _():
    import sys

    # Pyodide reports sys.platform == "emscripten", which is how the
    # notebook knows whether its controls are actually live. The two
    # published builds come from this one file:
    #
    #   /        WebAssembly, real Python in the browser, controls work
    #   /fast/   static snapshot, ~300 KB, controls rendered but frozen
    #
    # Telling the reader which one they are on -- and linking to the
    # other -- has to happen here rather than by post-processing the
    # HTML: marimo mounts its app over the whole body, so a banner
    # injected before it is painted over.
    IS_LIVE = sys.platform == "emscripten"

    # Relative, so both work locally and under a GitHub Pages subpath.
    OTHER_HREF = "fast/" if IS_LIVE else "../"
    return IS_LIVE, OTHER_HREF


@app.cell(hide_code=True)
def _(IS_LIVE, OTHER_HREF, mo):
    mo.callout(
        mo.md(
            "**Interactive version.** The sliders and pickers below are "
            f"live. On a slow connection, the [lightweight version]"
            f"({OTHER_HREF}) loads in a fraction of the size."
            if IS_LIVE else
            "**Lightweight version.** Figures are fixed at their default "
            "settings so the page loads fast. For live controls, open the "
            f"[interactive version]({OTHER_HREF})."
        ),
        kind="info" if IS_LIVE else "neutral",
    )
    return


@app.cell(hide_code=True)
def _(DATA_B64):
    import base64
    import gzip
    import json
    from pathlib import Path

    import pandas as pd
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    def _load_package() -> dict:
        """The data package, from disk if available, else from the blob.

        Two sources on purpose. The JSON file is authoritative during
        development -- rebuild it and the notebook picks the change up
        on re-run. The embedded blob is what a published build uses,
        because a browser has no filesystem. build_demo_data.py writes
        both in the same pass, so they cannot drift.
        """
        here = Path.cwd()
        for cand in (here, here / "poster_figures", *here.parents):
            p = cand / "poster_demo_data.json"
            if p.exists():
                return json.loads(p.read_text(encoding="utf-8"))
        if DATA_B64:
            return json.loads(gzip.decompress(base64.b64decode(DATA_B64)))
        raise FileNotFoundError(
            "No data package. Run `python build_demo_data.py` from the "
            "poster_figures folder to generate poster_demo_data.json and "
            "embed it in this notebook.")

    DATA = _load_package()

    META = DATA["meta"]
    DRUGS = DATA["drugs"]
    SPECIES = DATA["species"]
    CAND = pd.DataFrame(DATA["candidates"]["rows"],
                        columns=DATA["candidates"]["columns"])
    CLINICAL = pd.DataFrame(DATA["clinical"])
    RESCORE = pd.DataFrame(DATA["rescore"])

    return (
        CAND, CLINICAL, DATA, DRUGS, META, RESCORE, SPECIES,
        go, make_subplots, pd,
    )


@app.cell(hide_code=True)
def _():
    # Palette, lifted from the poster build so the page and the printed
    # panels agree. Literals rather than an import: this notebook has no
    # toolkit dependency, and that is the whole point.
    GATE_IN = "#4ea76a"     # inside the GC window
    GATE_OUT = "#9aa3ad"    # outside it -- neutral grey, not a verdict
    EXON_DARK = "#2f6b3f"
    EXON_LIGHT = "#8cc49a"
    UTR_TINT = "#b9bfc7"
    INK = "#1a1a1a"
    MUTED = "#6b7280"
    GRID = "#e3e7ec"
    ACTIVE = "#1a7f37"
    SEED = "#b8860b"

    # Mobile-first figure defaults. Authored directly in pixels rather
    # than derived from a poster width: the figures autosize to the
    # column, so what has to stay readable on a 390 px screen is the
    # absolute type size and the margins.
    FONT_PX = 13
    MARGIN = dict(l=58, r=18, t=38, b=46)

    def base_layout(fig, *, height, legend_top=True, title=None):
        """Apply the shared look and make the figure fill its container."""
        fig.update_layout(
            autosize=True, height=height, margin=MARGIN,
            font=dict(size=FONT_PX, color=INK,
                      family="Helvetica Neue, Helvetica, Arial, sans-serif"),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            title=(dict(text=title, x=0, xref="paper", xanchor="left",
                        font=dict(size=FONT_PX + 2))
                   if title else None),
            hovermode="closest",
            dragmode=False,          # a touch drag should scroll the page
        )
        if legend_top:
            fig.update_layout(legend=dict(
                orientation="h", yanchor="bottom", y=1.0,
                xanchor="right", x=1.0, font=dict(size=FONT_PX - 1)))
        fig.update_xaxes(showgrid=False, zeroline=False, linecolor=GRID,
                         ticks="outside", tickcolor=GRID)
        fig.update_yaxes(gridcolor=GRID, zeroline=False, linecolor=GRID)
        return fig

    #: Plotly renders at the container width and keeps doing so on
    #: resize only if told to; marimo passes this config through.
    PLOT_CFG = {"responsive": True, "displayModeBar": False,
                "scrollZoom": False}

    return (
        ACTIVE, EXON_DARK, EXON_LIGHT, FONT_PX, GATE_IN, GATE_OUT, GRID,
        INK, MUTED, PLOT_CFG, SEED, UTR_TINT, base_layout,
    )


@app.cell(hide_code=True)
def _(mo):
    # Page chrome for phones: no sideways scrolling, readable body type,
    # and the wide intro table allowed to scroll inside itself.
    mo.Html("""
    <style>
      .fig { width: 100%; max-width: 860px; margin: .8rem auto 1.2rem; }
      .fig > svg { width: 100%; height: auto; display: block; }
      .markdown img, img { max-width: 100%; height: auto; }
      .markdown table { display: block; max-width: 100%; overflow-x: auto; }
      @media (max-width: 700px) {
        .markdown { font-size: 1.03rem; line-height: 1.58; }
        .markdown h1 { font-size: 1.7rem; line-height: 1.2; }
        .markdown h2 { font-size: 1.35rem; }
        .markdown h3 { font-size: 1.12rem; }
        .markdown p, .markdown li { overflow-wrap: break-word; }
      }
    </style>
    """)
    return


@app.cell(hide_code=True)
def _(IS_LIVE, META, mo):
    # The one sentence that differs between the two builds: on the static
    # snapshot the controls are rendered but inert, and claiming they are
    # live would be the page's only false statement.
    _controls = ("**The controls are live** — move them and the figures "
                 "and captions recompute."
                 if IS_LIVE else
                 "The controls below are shown at their default settings; "
                 "the interactive version recomputes as you move them.")
    mo.md(rf"""
    # Designing an siRNA against TTR

    ### A worked case study, with two approved drugs as the answer key

    Transthyretin is an unusually good gene to learn siRNA design on. It is
    short, it is almost entirely liver-expressed, and — unusually — it already
    has **two approved siRNA drugs against it**, developed a decade apart:

    | | **patisiran** (2018) | **vutrisiran** (2022) |
    |---|---|---|
    | duplex | 19+2 / 19+2, dTdT overhangs | 23 / 21 |
    | chemistry | a few 2′-OMe, nothing else | fully modified, 2′-OMe + 2′-F |
    | backbone | all phosphodiester | terminal phosphorothioate |
    | delivery | lipid nanoparticle, IV | GalNAc conjugate, subcutaneous |
    | dosing | every 3 weeks, with premedication | once every 3 months |

    Same gene, same mechanism, same company — and almost nothing in common
    chemically. That gap is the whole story of the last decade of the field.

    **How to read this.** Each section asks one design question, shows the
    figure that answers it, and checks the answer against where patisiran
    and vutrisiran actually landed. {_controls}

    Nothing here is a simulation: both sequences and both modification
    patterns are the published ones, scored by the same pipeline as every
    other candidate. All **{META['n_candidates']} candidates** across
    {META['gene']} {META['accession']} ({META['length']} nt) are in the
    page.
    """)
    return


@app.cell(hide_code=True)
def _(META, mo):
    mo.md(rf"""
    ## 1. Walk the transcript

    Every design starts by tiling the transcript into every guide it can
    accommodate — **{META['n_candidates']} candidates across
    {META['length']} nucleotides**, four exons, a 26 nt 5′UTR and a long
    3′UTR that turns out to matter. That is the honest denominator: both
    approved drugs are somewhere in this set, and so is every
    nonfunctional sequence.

    The first filter anyone reaches for is **GC content**. Too low and the
    duplex is unstable and promiscuous; too high and it is hard to unwind
    and prone to off-target hybridisation. The conventional window is
    15–56 %.

    **Drag the window and watch where the rejects fall.** They are not
    evenly spread — and the region both drugs bind is among the last to
    be lost.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    gc_window = mo.ui.range_slider(
        start=0, stop=100, step=1, value=[15, 56],
        label="**GC window (%)**", show_value=True, full_width=True,
        debounce=False,   # ~40 ms redraw, so it can track the handle live
    )
    gc_window
    return (gc_window,)


@app.cell(hide_code=True)
def _(
    CAND, DRUGS, EXON_DARK, EXON_LIGHT, GATE_IN, GATE_OUT, META, MUTED,
    PLOT_CFG, UTR_TINT, base_layout, gc_window, go, make_subplots, mo,
):
    def transcript_figure(lo, hi):
        """Transcript map above, GC against position below, shared x."""
        L = META["length"]
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                            row_heights=[0.3, 0.7], vertical_spacing=0.06)

        # --- row 1: exons to scale, UTRs tinted over the ends ---
        for i, (a, b) in enumerate(META["exons"]):
            fig.add_shape(type="rect", x0=a, x1=b, y0=0, y1=1,
                          fillcolor=EXON_DARK if i % 2 else EXON_LIGHT,
                          line=dict(width=0), row=1, col=1)
            fig.add_annotation(x=(a + b) / 2, y=0.5, text=str(i + 1),
                               showarrow=False, font=dict(color="white"),
                               row=1, col=1)
        for a, b in ((0, META["cds_start"]), (META["cds_end"], L)):
            fig.add_shape(type="rect", x0=a, x1=b, y0=0, y1=1,
                          fillcolor=UTR_TINT, opacity=0.55,
                          line=dict(width=0), row=1, col=1)
        fig.update_yaxes(visible=False, range=(0, 1), row=1, col=1)

        # --- row 2: every candidate at its position, coloured by gate ---
        inside = CAND[(CAND["gc"] >= lo) & (CAND["gc"] <= hi)]
        outside = CAND.drop(inside.index)
        fig.add_hrect(y0=lo, y1=hi, fillcolor=GATE_IN, opacity=0.09,
                      line_width=0, row=2, col=1)
        for frame, name, colour in ((outside, "outside window", GATE_OUT),
                                    (inside, "inside window", GATE_IN)):
            fig.add_trace(go.Scattergl(
                x=frame["pos"], y=frame["gc"], mode="markers", name=name,
                marker=dict(size=4.5, color=colour, opacity=0.85),
                hovertemplate="position %{x}<br>GC %{y:.0f}%<extra></extra>",
            ), row=2, col=1)

        # --- both drugs, marked in both rows ---
        for d in DRUGS:
            for r in (1, 2):
                fig.add_shape(type="line", x0=d["position"], x1=d["position"],
                              y0=0, y1=1, yref=f"y{'' if r == 1 else '2'} domain",
                              line=dict(color=d["color"], width=1.6,
                                        dash="dash"),
                              row=r, col=1)
            fig.add_annotation(x=d["position"], y=1.04, yref="y domain",
                               text=d["name"], showarrow=False,
                               font=dict(color=d["color"], size=11),
                               row=1, col=1)

        fig.update_yaxes(title_text="GC %", range=(0, 100), row=2, col=1)
        fig.update_xaxes(title_text=f"position on {META['accession']} (nt)",
                         range=(0, L), row=2, col=1)
        base_layout(fig, height=430)
        fig.update_layout(legend=dict(y=1.02, x=0, xanchor="left"))
        fig.update_annotations(font_size=11)
        return fig

    _lo, _hi = gc_window.value
    mo.ui.plotly(transcript_figure(_lo, _hi), config=PLOT_CFG)
    return


@app.cell(hide_code=True)
def _(CAND, DRUGS, META, gc_window, mo):
    _lo, _hi = gc_window.value
    _in = int(((CAND["gc"] >= _lo) & (CAND["gc"] <= _hi)).sum())
    _n = META["n_candidates"]
    _out = _n - _in
    _low = int((CAND["gc"] < _lo).sum())
    _high = int((CAND["gc"] > _hi).sum())
    _kept = [d["name"] for d in DRUGS if _lo <= (d["gc"] or -1) <= _hi]
    _lost = [d["name"] for d in DRUGS if d["name"] not in _kept]

    if _out == 0:
        _head = (f"At **{_lo:g}–{_hi:g} %** the window admits **all {_n} "
                 "candidates** — wider than the transcript's own GC range, "
                 "so it is not discriminating at all.")
    elif _in == 0:
        _head = (f"At **{_lo:g}–{_hi:g} %** the window admits **nothing**: "
                 f"all {_n} candidates fall outside it.")
    else:
        _bias = ("all of them GC-rich" if _low == 0 else
                 "all of them GC-poor" if _high == 0 else
                 f"{_high} GC-rich, {_low} GC-poor")
        _head = (f"At **{_lo:g}–{_hi:g} %**, **{_out} of {_n} candidates** "
                 f"fall outside the window — {_bias} — leaving **{_in}** "
                 f"(**{100.0 * _in / _n:.1f} %**).")

    if not _lost:
        _verdict = "Both approved drugs are still inside it."
    elif _kept:
        _verdict = (f"It keeps {_kept[0]} but **rejects {_lost[0]}** — a "
                    "window that excludes a molecule which became a drug.")
    else:
        _verdict = ("⚠️ **It rejects both approved drugs.** A filter no real "
                    "molecule survives is a filter to revisit, not a result.")

    mo.md(f"""
    {_head} {_verdict}

    *A composition flag, not a gate: nothing downstream is removed on this
    basis. GC content and predicted activity are independent.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Choose your candidates

    Composition describes a sequence; it does not predict whether it will
    work. Every candidate is scored on three independent axes:

    - **Predicted efficacy** — a random forest trained on fully modified
      siRNA knockdown data. *Plotted on x.*
    - **Thermodynamic asymmetry (ΔΔG)** — are the duplex ends lopsided
      enough that RISC loads the guide rather than the passenger strand?
      *Plotted on y.*
    - **Target accessibility** — is the site unpaired and reachable in the
      folded transcript? *Carried by colour.*

    Higher is better on all three: **upper, right and bright.**

    **Move the shortlist depth** and watch when each drug is admitted.
    """)
    return


@app.cell(hide_code=True)
def _(META, mo):
    n_top = mo.ui.slider(
        start=5, stop=min(300, META["n_candidates"]), step=5, value=48,
        label="**Shortlist depth (Top-N by consensus rank)**",
        show_value=True, full_width=True, debounce=False,
    )
    n_top
    return (n_top,)


@app.cell(hide_code=True)
def _(CAND, DRUGS, MUTED, PLOT_CFG, base_layout, go, mo, n_top):
    def scatter_figure(top_n):
        sel = CAND.nsmallest(top_n, "consensus")
        rest = CAND.drop(sel.index)
        fig = go.Figure()
        fig.add_trace(go.Scattergl(
            x=rest["rf"], y=rest["ddg"], mode="markers", name="candidate",
            marker=dict(size=5, color=rest["log_acc"], colorscale="Viridis",
                        opacity=0.55, line=dict(width=0)),
            hovertemplate="RF %{x:.3f}<br>ΔΔG %{y:.1f}<extra></extra>"))
        fig.add_trace(go.Scattergl(
            x=sel["rf"], y=sel["ddg"], mode="markers",
            name=f"top {top_n}",
            marker=dict(size=9, color=sel["log_acc"], colorscale="Viridis",
                        line=dict(width=1.4, color="#333"),
                        colorbar=dict(title=dict(text="log₁₀ acc.",
                                                 side="right"),
                                      thickness=11, len=0.85, x=1.005)),
            hovertemplate="RF %{x:.3f}<br>ΔΔG %{y:.1f}<extra></extra>"))
        for d in DRUGS:
            row = CAND[CAND["pos"] == d["position"]]
            if row.empty:
                continue
            fig.add_trace(go.Scattergl(
                x=row["rf"], y=row["ddg"], mode="markers+text",
                text=[d["name"]], textposition="top center",
                textfont=dict(color=d["color"], size=11),
                marker=dict(size=14, color="rgba(0,0,0,0)",
                            line=dict(width=2.6, color=d["color"])),
                showlegend=False, hoverinfo="skip"))
        fig.update_xaxes(title_text="RF P(effective)")
        fig.update_yaxes(title_text="ΔΔG (kcal·mol⁻¹)")
        base_layout(fig, height=420)
        return fig

    mo.ui.plotly(scatter_figure(int(n_top.value)), config=PLOT_CFG)
    return


@app.cell(hide_code=True)
def _(CAND, DRUGS, mo, n_top):
    _n = int(n_top.value)
    _cut = CAND.nsmallest(_n, "consensus")["consensus"].max()
    _rows = []
    for d in DRUGS:
        _r = d["consensus_rank"]
        _in = _r is not None and _r <= _n
        _rows.append(f"**{d['name']}** is rank **{int(_r)}** — "
                     + ("inside" if _in else "**outside**")
                     + f" a top-{_n} shortlist")
    mo.md(f"""
    {_rows[0]}. {_rows[1]}.

    Vutrisiran enters at 28; patisiran not until **155 of 597**. Its site
    is the more accessible of the two (rank 19, the best single number
    either drug posts), but its thermodynamic asymmetry is rank 483 — the
    bottom fifth. The naked duplex is biased the *wrong* way for
    guide-strand loading, and its chemistry does little to fix it.

    That is the case study in miniature: a first-generation design could
    pick a good site and a plausible sequence, but had no way to correct a
    duplex that loads the wrong strand. A shortlist deep enough to catch
    patisiran is deeper than most programmes would run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Plan your pre-clinical tox package

    A guide that is top-ranked against human TTR but absent from the NHP
    transcript cannot go through primate toxicology without switching
    molecules. Cross-species conservation is a **design constraint, not a
    downstream surprise** — and it is cheapest to apply here, before a
    lead is chosen.

    **Pick the species your programme intends to dose.** The candidate set
    is filtered to guides that are cross-reactive in all of them, and the
    strip shows where on the transcript the survivors sit.
    """)
    return


@app.cell(hide_code=True)
def _(SPECIES, mo):
    cons_species = mo.ui.multiselect(
        options=[s["key"] for s in SPECIES], value=["cynomolgus_monkey"],
        label="**Require cross-reactivity in**")
    cons_seed = mo.ui.switch(
        value=False, label="count **seed-only** as cross-reactive")
    mo.vstack([cons_species, cons_seed])
    return cons_seed, cons_species


@app.cell(hide_code=True)
def _(
    ACTIVE, CAND, DRUGS, GATE_IN, GATE_OUT, META, PLOT_CFG, SEED, SPECIES,
    base_layout, cons_seed, cons_species, go, make_subplots, mo,
):
    def survivors(keys, allow_seed):
        """Boolean mask: candidates cross-reactive in ALL chosen species."""
        ok = CAND.index == CAND.index  # all True
        allowed = {"active", "seed"} if allow_seed else {"active"}
        for k in keys:
            col = "hom_" + k
            if col in CAND.columns:
                ok = ok & CAND[col].isin(allowed)
        return ok

    def conservation_figure(keys, allow_seed):
        mask = survivors(keys, allow_seed)
        keep = CAND[mask]
        fig = make_subplots(rows=2, cols=1, row_heights=[0.62, 0.38],
                            vertical_spacing=0.22)

        # --- row 1: how permissive is each species, selected highlighted
        labels = [s["label"] for s in SPECIES]
        pct = [s["pct_active"] for s in SPECIES]
        chosen = [s["key"] in keys for s in SPECIES]
        fig.add_trace(go.Bar(
            x=labels, y=pct,
            marker_color=[ACTIVE if c else GATE_OUT for c in chosen],
            hovertemplate="%{x}: %{y:.1f}% active<extra></extra>",
            showlegend=False), row=1, col=1)
        fig.update_yaxes(title_text="% guides active", range=(0, 100),
                         row=1, col=1)
        fig.update_xaxes(tickangle=-35, row=1, col=1)

        # --- row 2: where the survivors are
        fig.add_trace(go.Scattergl(
            x=CAND["pos"], y=[0] * len(CAND), mode="markers",
            marker=dict(size=5, color=GATE_OUT, symbol="line-ns-open",
                        line=dict(width=1.1, color=GATE_OUT)),
            name="excluded", hoverinfo="skip", showlegend=False),
            row=2, col=1)
        if len(keep):
            fig.add_trace(go.Scattergl(
                x=keep["pos"], y=[0] * len(keep), mode="markers",
                marker=dict(size=9, color=GATE_IN, symbol="line-ns-open",
                            line=dict(width=1.5, color=GATE_IN)),
                name="survives", hoverinfo="skip", showlegend=False),
                row=2, col=1)
        for d in DRUGS:
            fig.add_shape(type="line", x0=d["position"], x1=d["position"],
                          y0=0, y1=1, yref="y2 domain",
                          line=dict(color=d["color"], width=1.6,
                                    dash="dash"), row=2, col=1)
        fig.update_yaxes(visible=False, range=(-1, 1), row=2, col=1)
        fig.update_xaxes(title_text="transcript position (nt)",
                         range=(0, META["length"]), row=2, col=1)
        base_layout(fig, height=430, legend_top=False)
        return fig

    _keys = list(cons_species.value)
    mo.ui.plotly(conservation_figure(_keys, cons_seed.value), config=PLOT_CFG)
    return (survivors,)


@app.cell(hide_code=True)
def _(CAND, DRUGS, META, cons_seed, cons_species, mo, survivors):
    _keys = list(cons_species.value)
    _mask = survivors(_keys, cons_seed.value)
    _k, _n = int(_mask.sum()), META["n_candidates"]
    _pos = set(CAND[_mask]["pos"])
    _kept = [d["name"] for d in DRUGS if d["position"] in _pos]
    _lost = [d["name"] for d in DRUGS if d["name"] not in _kept]

    if not _keys:
        _head = (f"**No requirement set** — all {_n} candidates survive. "
                 "Conservation only costs you something once you commit to "
                 "a species.")
    else:
        _names = " **and** ".join(s.replace("_", " ") for s in _keys)
        _head = (f"Requiring {_names} leaves **{_k} of {_n}** candidates "
                 f"(**{100.0 * _k / _n:.1f} %**).")

    if _lost and not _kept:
        _verdict = ("⚠️ **It rejects every approved drug** — "
                    + ", ".join(_lost) + ".")
    elif _lost:
        _verdict = (f"It keeps {', '.join(_kept)} but rejects "
                    f"{', '.join(_lost)}.")
    else:
        _verdict = "Both approved drugs survive it."

    mo.md(f"""
    {_head} {_verdict}

    Cynomolgus is the pharmacologically relevant species here, and the most
    permissive in the set — both programmes ran their NHP work there.
    **Add a rodent and watch the set collapse.** No wild-type mouse or rat
    can read out on-target biology for these sequences, which is why that
    work needs a **surrogate sequence** matched to the rodent transcript or
    a **human-transgenic** model — and both have to be planned at sequence
    selection, not discovered later.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Chemistry is everything

    An unmodified siRNA has a plasma half-life measured in minutes.
    Everything that makes one a drug — nuclease resistance, reduced immune
    sensing, tissue targeting, monthly dosing — is chemistry layered onto a
    sequence that was already chosen.

    Each circle is one nucleotide coloured by its sugar chemistry; ticks
    mark phosphorothioate linkages. *(This panel is a pre-rendered drawing
    — it is the one figure that cannot be redrawn in a browser.)*
    """)
    return


@app.cell(hide_code=True)
def _(DATA, mo):
    # Pre-exported SVG rather than a live draw: the duplex renderer needs
    # kaleido driving a chromium. As SVG it is 105 KB and scales to any
    # screen, where the equivalent PNG is 642 KB and goes soft on zoom.
    mo.Html(f'<div class="fig">{DATA["duplex_svg"]}</div>')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Patisiran is almost entirely unmodified.** Two 2′-OMe residues on the
    guide and nine on the sense strand — 11 of 38 positions — plus dTdT
    overhangs, an all-phosphodiester backbone, no 2′-F and no conjugate.
    Everything else is bare ribose, and the guide in particular is
    essentially naked. To compensate, it is delivered intravenously in a
    lipid nanoparticle: get as much to the liver as possible before it
    degrades.

    **Vutrisiran is modified at every single position** — all 44, 2′-OMe or
    2′-F, with phosphorothioate at both guide termini and the sense 5′ end.

    But the GalNAc conjugate is the game changer. It binds the
    asialoglycoprotein receptor, which is hepatocyte-specific and recycles
    every 15 minutes — so the drug delivers itself to the liver from a
    subcutaneous injection and stays active for months.

    Same target. Same binding site, nine nucleotides apart. A decade of
    chemistry in between.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. How do the other approved drugs stack up?

    The same pipeline, run on every approved siRNA against its own target
    transcript, with no knowledge that any of them is a drug. A sanity
    check: molecules that survived clinical development ought to rank well
    among the thousands of candidates they were selected from.

    There is a real weakness in that check, and it is worth naming.
    Consensus Rank's third axis is **ΔΔG on a naked duplex**, but every
    molecule here is fully chemically modified — it scores them as though
    their chemistry did not exist. So each gene was also re-scored under
    its drug's own registered pattern, which swaps that axis for
    modification-aware **ΔΔT<sub>m</sub>**.

    **Grey = scored naked. Green = scored under its own chemistry.**
    """)
    return


@app.cell(hide_code=True)
def _(RESCORE, mo):
    md_genes = mo.ui.multiselect(
        options=sorted(RESCORE["gene"].unique().tolist()),
        value=sorted(RESCORE["gene"].unique().tolist()),
        label="**genes**")
    md_genes
    return (md_genes,)


@app.cell(hide_code=True)
def _(ACTIVE, GATE_OUT, PLOT_CFG, RESCORE, base_layout, go, md_genes, mo):
    def rescore_figure(genes):
        sub = RESCORE[RESCORE["gene"].isin(genes)].dropna(
            subset=["pct_naked", "pct_modded"])
        sub = sub.sort_values("pct_modded")
        if sub.empty:
            return None
        labels = [f"{r['drug']}  ({r['gene']})" for _, r in sub.iterrows()]
        fig = go.Figure()
        for lab, (_, r) in zip(labels, sub.iterrows()):
            up = r["pct_modded"] >= r["pct_naked"]
            fig.add_trace(go.Scatter(
                x=[r["pct_naked"], r["pct_modded"]], y=[lab, lab],
                mode="lines", showlegend=False, hoverinfo="skip",
                line=dict(color=ACTIVE if up else "#b42318", width=3)))
        fig.add_trace(go.Scatter(
            x=sub["pct_naked"], y=labels, mode="markers", name="naked",
            marker=dict(size=10, color=GATE_OUT),
            hovertemplate="naked %{x:.1f}<extra></extra>"))
        fig.add_trace(go.Scatter(
            x=sub["pct_modded"], y=labels, mode="markers",
            name="own chemistry", marker=dict(size=10, color=ACTIVE),
            hovertemplate="modified %{x:.1f}<extra></extra>"))
        fig.add_vline(x=50, line=dict(color="#aaa", width=1, dash="dot"))
        fig.update_xaxes(title_text="percentile among candidates for its gene",
                         range=(0, 103))
        fig.update_layout(margin=dict(l=150, r=18, t=38, b=46))
        base_layout(fig, height=max(260, 46 * len(sub) + 110))
        fig.update_layout(margin=dict(l=150, r=18, t=38, b=46))
        return fig

    _fig = rescore_figure(list(md_genes.value))
    _out = (mo.ui.plotly(_fig, config=PLOT_CFG) if _fig is not None
            else mo.md("*No genes selected.*"))
    _out
    return


@app.cell(hide_code=True)
def _(RESCORE, md_genes, mo):
    _m = RESCORE[RESCORE["gene"].isin(md_genes.value)].dropna(
        subset=["delta_pct"])
    if _m.empty:
        _out = mo.md("*No genes selected.*")
    else:
        _up = _m[_m["delta_pct"] > 0]
        _dn = _m[_m["delta_pct"] < 0]
        _best = _m.loc[_m["delta_pct"].idxmax()]
        _worst = _m.loc[_m["delta_pct"].idxmin()]
        _out = mo.md(f"""
    **{len(_up)} of {len(_m)} drugs rank better under their own chemistry**,
    {len(_dn)} worse; mean move **{_m['delta_pct'].mean():+.1f} percentile
    points**.

    Biggest gain **{_best['drug']}** ({_best['pct_naked']:.1f} →
    {_best['pct_modded']:.1f}, rank {int(_best['rank_naked'])} →
    {int(_best['rank_modded'])}). Biggest loss **{_worst['drug']}**
    ({_worst['pct_naked']:.1f} → {_worst['pct_modded']:.1f}).

    So the objection does not sink the method — scoring these molecules
    naked was, for most of them, *pessimistic*. But it is not noise either:
    a drug can move a long way, so a naked ΔΔG ranking should not be read
    as the last word on a modified duplex.
    """)
    _out
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What the case study shows

    1. **Composition is structured along the transcript.** The candidates a
       GC window rejects cluster in the coding sequence, not the 3′UTR
       where both drugs ended up.
    2. **Ranking is three independent axes**, not one number. They don't
       correlate, and the disagreement is where the design decision lives.
    3. **Conservation is a property of the nucleotides you picked**, not of
       the gene — it decides which question each species in your tox plan
       can actually answer.
    4. **Both approved TTR drugs bind the 3′UTR**, nine nucleotides apart,
       found independently a decade apart. A pattern, not a rule.
    5. **Chemistry is where the decade went.** Same target, same site, same
       mechanism: unmodified-and-infused versus fully-modified,
       GalNAc-conjugated, dosed quarterly.
    """)
    return


@app.cell(hide_code=True)
def _(META, mo):
    mo.md(rf"""
    ---

    *Built with the siRNA Toolkit. Every figure on this page is drawn live
    in your browser from one {META['n_candidates']}-row data package
    produced by the same pipeline the toolkit runs on any gene you give it.
    Pipeline run: {META['source']}, frozen {META['generated']}.*
    """)
    return


if __name__ == "__main__":
    app.run()
