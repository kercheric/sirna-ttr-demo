#!/usr/bin/env python3
"""Build both published versions of the TTR demo from poster_demo.py.

Two builds from one source, so they can never disagree:

  /            interactive  -- WebAssembly, ~12 MB first load, live controls
  /fast/       lightweight  -- single 300 KB file, controls frozen

The poster QR code should point at /fast/ (it loads instantly on venue
wifi); the homepage link should point at /.

The notebook detects which build it is in (Pyodide sets sys.platform to
"emscripten") and renders its own cross-link and its own description of
whether the controls work -- so no HTML post-processing is needed here.
A banner injected into <body> would not work anyway: marimo mounts its
app over the whole body and paints straight over it.

Requires marimo in the environment:
    pip install marimo pandas plotly
    python build.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE / "poster_demo.py"
FAST = HERE / "fast"

#: Dropped from the WASM bundle: marimo ships its own CLAUDE.md with the
#: frontend assets. Harmless, but it is noise in a public repo.
JUNK = ("CLAUDE.md",)

def run(*args: str) -> None:
    print("  $", " ".join(args))
    subprocess.run(args, check=True, cwd=HERE)


def main() -> int:
    if not NOTEBOOK.exists():
        print(f"error: {NOTEBOOK.name} not found", file=sys.stderr)
        return 1

    # --- interactive, at the repo root ------------------------------
    # Everything except our own files is regenerated, so clear the
    # previous asset tree rather than letting stale hashes accumulate.
    for p in HERE.glob("*"):
        if p.name in {".git", "build.py", "README.md", "poster_demo.py",
                      "fast", ".gitignore"}:
            continue
        shutil.rmtree(p) if p.is_dir() else p.unlink()

    print("building interactive (WebAssembly) ->  /")
    run("marimo", "export", "html-wasm", NOTEBOOK.name,
        "-o", ".", "--mode", "run", "--no-show-code", "-f")

    for name in JUNK:
        junk = HERE / name
        if junk.exists():
            junk.unlink()
            print(f"  removed {name}")

    # --- lightweight, in /fast --------------------------------------
    print("building lightweight (static) ->  /fast/")
    if FAST.exists():
        shutil.rmtree(FAST)
    FAST.mkdir()
    run("marimo", "export", "html", NOTEBOOK.name,
        "-o", "fast/index.html", "--no-include-code", "-f")

    # GitHub Pages must not run Jekyll over the asset tree: Jekyll
    # ignores directories beginning with an underscore and would mangle
    # the build. marimo writes this for the wasm export; make sure it
    # survives for the whole site.
    (HERE / ".nojekyll").touch()

    n = sum(1 for _ in HERE.rglob("*") if _.is_file()
            and ".git" not in _.parts)
    mb = sum(p.stat().st_size for p in HERE.rglob("*") if p.is_file()
             and ".git" not in p.parts) / 1048576
    print(f"\ndone: {n} files, {mb:.1f} MB")
    print("  /          interactive")
    print("  /fast/     lightweight")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
