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
app = marimo.App(width="medium", app_title="Designing an siRNA against TTR")


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
    # DATA["clinical"] -- unmodified percentile, rank and sponsor per drug --
    # is in the package but deliberately not unpacked: the section 5
    # grouped bars already plot the unmodified percentile.
    # Unpack it if a plain percentile bar chart is ever wanted back.
    RESCORE = pd.DataFrame(DATA["rescore"])
    return CAND, DATA, DRUGS, META, RESCORE, SPECIES, go, make_subplots


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
        ACTIVE,
        EXON_DARK,
        EXON_LIGHT,
        GATE_IN,
        GATE_OUT,
        PLOT_CFG,
        UTR_TINT,
        base_layout,
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

    **Clinical motivation.** Transthyretin is a liver-made protein
    that ferries thyroxine and retinol through the blood. Destabilising
    point mutations disrupt protein folding which leads to progressive
    sensorimotor and autonomic **polyneuropathy**, a restrictive
    **cardiomyopathy**, or both. If left untreated, the disease is fatal.

    **Why an siRNA is a suitable drug modality here** — three things
    line up:

    - **The protein is the problem.** This is a gain-of-toxic-function
      disease: nothing is missing, something harmful is accumulating. So
      lowering the protein *is* the therapy, which is precisely what RNAi
      does. 
    - **One tissue makes it.** Essentially all circulating TTR comes from
      hepatocytes — and hepatocytes are the one cell type oligonucleotide
      delivery has genuinely solved, via GalNAc conjugation.
    - **The target is dispensable.** Deep, sustained knockdown is well
      tolerated: thyroxine transport is redundant, and retinol transport
      is covered by vitamin A supplementation.

    Transthyretin is an unusually good gene to learn siRNA design on. It is
    short, it is almost entirely liver-expressed, and it already
    has **two** approved siRNA drugs against it, developed a decade apart:

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
    evenly spread, and the two bounds bite in opposite places: tightening
    from above cuts the GC-rich coding sequence, while raising the floor
    eats into the AT-rich 3′UTR — the very region both drugs bind. At the
    conventional setting only the upper bound fires at all.
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
    CAND,
    DRUGS,
    EXON_DARK,
    EXON_LIGHT,
    GATE_IN,
    GATE_OUT,
    META,
    PLOT_CFG,
    UTR_TINT,
    base_layout,
    gc_window,
    go,
    make_subplots,
    mo,
):
    def transcript_figure(lo, hi):
        """Transcript map, GC against position, admitted strip.

        Three rows on one shared x axis, so a candidate lines up
        vertically across all of them. The bottom strip repeats the
        verdict as a tick at each transcript position -- the same idiom
        section 3 uses for conservation survivors -- because the scatter
        answers "how many and at what GC" while the strip answers "where
        along the transcript", which is the question a count cannot.
        """
        L = META["length"]
        fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                            row_heights=[0.26, 0.56, 0.18],
                            vertical_spacing=0.05)

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
        # Admitted candidates are drawn large, bright and opaque; rejected
        # ones shrink to faint grey dots. Size carries the verdict as well
        # as colour, so dragging the handle produces an obvious swell or
        # collapse of the cloud rather than a hue shift a reader has to
        # hunt for -- and it still reads for anyone who cannot separate
        # the green from the grey.
        for frame, name, colour, size, alpha in (
            (outside, "outside window", GATE_OUT, 3.0, 0.45),
            (inside, "inside window", GATE_IN, 8.5, 0.95),
        ):
            fig.add_trace(go.Scattergl(
                x=frame["pos"], y=frame["gc"], mode="markers", name=name,
                marker=dict(size=size, color=colour, opacity=alpha,
                            line=dict(width=0)),
                hovertemplate="position %{x}<br>GC %{y:.0f}%<extra></extra>",
            ), row=2, col=1)

        # --- both drugs, marked in every row ---
        # The two sites are nine nucleotides apart on a 616 nt axis, so
        # centred labels at a common height overprint each other into an
        # unreadable smudge. Stack them instead, nearest site lowest, and
        # give each a leader down to its own dashed line.
        for i, d in enumerate(sorted(DRUGS, key=lambda x: x["position"])):
            for r in (1, 2, 3):
                fig.add_shape(type="line", x0=d["position"], x1=d["position"],
                              y0=0, y1=1,
                              yref=f"y{'' if r == 1 else r} domain",
                              line=dict(color=d["color"], width=1.6,
                                        dash="dash"),
                              row=r, col=1)
            fig.add_annotation(
                x=d["position"], y=1.10 + 0.42 * i, yref="y domain",
                text=d["name"], showarrow=True, arrowhead=0, arrowwidth=1,
                arrowcolor=d["color"], ax=0, ay=-10,
                font=dict(color=d["color"], size=11),
                xanchor="center", row=1, col=1)

        # --- row 3: the same verdict as a tick strip along the transcript
        # Every candidate is a faint grey tick; the admitted ones are
        # overdrawn taller and green. Where the window bites is then read
        # off the transcript directly, rather than inferred from a cloud.
        fig.add_trace(go.Scattergl(
            x=CAND["pos"], y=[0] * len(CAND), mode="markers",
            marker=dict(size=5, color=GATE_OUT, symbol="line-ns-open",
                        line=dict(width=1.1, color=GATE_OUT)),
            hoverinfo="skip", showlegend=False), row=3, col=1)
        if len(inside):
            fig.add_trace(go.Scattergl(
                x=inside["pos"], y=[0] * len(inside), mode="markers",
                marker=dict(size=9, color=GATE_IN, symbol="line-ns-open",
                            line=dict(width=1.5, color=GATE_IN)),
                hoverinfo="skip", showlegend=False), row=3, col=1)
        fig.update_yaxes(visible=False, range=(-1, 1), row=3, col=1)

        fig.update_yaxes(title_text="GC %", range=(0, 100), row=2, col=1)
        fig.update_xaxes(title_text=f"position on {META['accession']} (nt)",
                         range=(0, L), row=3, col=1)
        base_layout(fig, height=520)
        # Extra headroom: the stacked drug labels sit above the top row.
        fig.update_layout(margin=dict(l=58, r=18, t=62, b=46),
                          legend=dict(y=1.06, x=0, xanchor="left"))
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
def _(CAND, DRUGS, PLOT_CFG, base_layout, go, mo, n_top):
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
    bottom fifth. The unmodified duplex is biased the *wrong* way for
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
    ACTIVE,
    CAND,
    DRUGS,
    GATE_IN,
    GATE_OUT,
    META,
    PLOT_CFG,
    SPECIES,
    base_layout,
    cons_seed,
    cons_species,
    go,
    make_subplots,
    mo,
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
    mark phosphorothioate linkages.
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
    essentially unmodified. To compensate, it is delivered intravenously
    in a
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
    Consensus Rank's third axis is **ΔΔG on an unmodified duplex**, but every
    molecule here is fully chemically modified — it scores them as though
    their chemistry did not exist. So each gene was also re-scored under
    its drug's own registered pattern, which swaps that axis for
    modification-aware **ΔΔT<sub>m</sub>**.

    **Grey = scored unmodified. Green = scored under its own chemistry.**
    Switch the view to see either ranking on its own, or both side by
    side with the move printed at the end of each pair. The dotted line
    is the 50th percentile — below it, a drug ranks worse than half the
    sequences it was selected from.
    """)
    return


@app.cell(hide_code=True)
def _(RESCORE, mo):
    md_genes = mo.ui.multiselect(
        options=sorted(RESCORE["gene"].unique().tolist()),
        value=sorted(RESCORE["gene"].unique().tolist()),
        label="**genes**")
    md_view = mo.ui.radio(
        options={
            "Scored unmodified": "unmodified",
            "Scored with its own chemistry": "modded",
            "Both, and the move between them": "both",
        },
        value="Both, and the move between them",
        label="**view**", inline=True)
    mo.vstack([md_view, md_genes])
    return md_genes, md_view


@app.cell(hide_code=True)
def _(
    ACTIVE,
    GATE_OUT,
    PLOT_CFG,
    RESCORE,
    base_layout,
    go,
    md_genes,
    md_view,
    mo,
):
    LOSS = "#b42318"

    def rescore_figure(genes, view):
        """Percentile per drug, as bars, in one of three framings.

        Bars rather than dots: the quantity is a percentile out of 100,
        so a bar carries the "how far along the scale" reading directly
        and a reader can compare lengths across drugs at a glance. The
        "both" view groups the two bars per drug and prints the move at
        the end, so the comparison stays a bar chart rather than turning
        into a second chart type.
        """
        sub = RESCORE[RESCORE["gene"].isin(genes)].dropna(
            subset=["pct_unmodified", "pct_modded"])
        if sub.empty:
            return None
        # Sort by whatever the view is actually about, so the bars read
        # as a ranking rather than an arbitrary order.
        sort_key = {"unmodified": "pct_unmodified", "modded": "pct_modded",
                    "both": "delta_pct"}[view]
        sub = sub.sort_values(sort_key)
        labels = [f"{r['drug']}  ({r['gene']})" for _, r in sub.iterrows()]

        fig = go.Figure()
        if view in ("unmodified", "modded"):
            col = "pct_unmodified" if view == "unmodified" else "pct_modded"
            colour = GATE_OUT if view == "unmodified" else ACTIVE
            name = "scored unmodified" if view == "unmodified" else "own chemistry"
            fig.add_trace(go.Bar(
                x=sub[col], y=labels, orientation="h", name=name,
                marker=dict(color=colour),
                text=[f"{v:.1f}" for v in sub[col]],
                textposition="outside", textfont=dict(size=11),
                hovertemplate="%{y}<br>%{x:.1f}th percentile<extra></extra>",
                showlegend=False))
        else:
            fig.add_trace(go.Bar(
                x=sub["pct_unmodified"], y=labels, orientation="h",
                name="scored unmodified", marker=dict(color=GATE_OUT),
                hovertemplate="%{y}<br>unmodified %{x:.1f}<extra></extra>"))
            # The move is the result of this section, so it is printed
            # on the bar that moved rather than left to be eyeballed.
            fig.add_trace(go.Bar(
                x=sub["pct_modded"], y=labels, orientation="h",
                name="own chemistry", marker=dict(color=ACTIVE),
                text=[f"{d:+.1f}" for d in sub["delta_pct"]],
                textposition="outside", textfont=dict(size=11),
                hovertemplate="%{y}<br>modified %{x:.1f}<extra></extra>"))
            fig.update_layout(barmode="group", bargap=0.28,
                              bargroupgap=0.06)
            # Colour the delta text by direction -- green gained, red lost.
            fig.data[1].textfont = dict(
                size=11,
                color=[ACTIVE if d >= 0 else LOSS for d in sub["delta_pct"]])

        # Median of the candidate pool: a drug below this ranks worse
        # than half the sequences it was chosen from.
        fig.add_vline(x=50, line=dict(color="#aaa", width=1, dash="dot"),
                      annotation_text="50th", annotation_position="top",
                      annotation_font=dict(size=10, color="#888"))
        fig.update_xaxes(title_text="percentile among candidates for its gene",
                         range=(0, 112))
        rows = len(sub)
        base_layout(fig, height=max(280, (58 if view == "both" else 40)
                                    * rows + 120))
        # Room on the left for "fitusiran  (SERPINC1)"-length labels.
        fig.update_layout(margin=dict(l=150, r=22, t=38, b=46),
                          legend=dict(orientation="h", yanchor="bottom",
                                      y=1.0, xanchor="right", x=1.0))
        return fig

    _fig = rescore_figure(list(md_genes.value), md_view.value)
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

    Biggest gain **{_best['drug']}** ({_best['pct_unmodified']:.1f} →
    {_best['pct_modded']:.1f}, rank {int(_best['rank_unmodified'])} →
    {int(_best['rank_modded'])}). Biggest loss **{_worst['drug']}**
    ({_worst['pct_unmodified']:.1f} → {_worst['pct_modded']:.1f}).

    So the objection does not sink the method — scoring these molecules
    unmodified was, for most of them, *pessimistic*. But it is not noise
    either:
    a drug can move a long way, so an unmodified ΔΔG ranking should not be
    read
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

    *This demo was built with a snapshot from the siRNA Toolkit pipeline. Run: {META['source']}, frozen {META['generated']}.*

    *Ready to design your own siRNAs? Head to the [siRNA Toolkit](https://sirna-toolkit.streamlit.app)*
    """)
    return


if __name__ == "__main__":
    app.run()
