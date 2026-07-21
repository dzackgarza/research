"""Rebuild the interactive category-parent-graph viewer from the DOT source.

The HTML page at ``sage_lattice_category_spike/category_parent_graph.html``
fetches ``category_parent_graph.svg``. Editing the DOT without regenerating
that SVG leaves the browser on a stale drawing — every test session rebuilds it.
"""

from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
from pathlib import Path

_STUBS_ROOT = Path(__file__).resolve().parent.parent
_DOT = _STUBS_ROOT / "design" / "normalized_category_graph" / "category_parent_graph.dot"
_SPIKE_ROOT = _STUBS_ROOT.parent / "sage_lattice_category_spike"
_SPIKE_DOT = _SPIKE_ROOT / "category_parent_graph.dot"
_SPIKE_SVG = _SPIKE_ROOT / "category_parent_graph.svg"
_SPIKE_HTML = _SPIKE_ROOT / "category_parent_graph.html"


def viewer_paths() -> dict[str, Path]:
    return {
        "dot": _DOT,
        "spike_dot": _SPIKE_DOT,
        "svg": _SPIKE_SVG,
        "html": _SPIKE_HTML,
    }


def rebuild_viewer(*, cache_bust: int | None = None) -> dict[str, Path | int]:
    """Copy DOT → lattice spike, run Graphviz, bump the HTML ``?v=`` cache-bust."""
    if not _DOT.is_file():
        raise FileNotFoundError(_DOT)
    if not _SPIKE_ROOT.is_dir():
        raise FileNotFoundError(_SPIKE_ROOT)
    if shutil.which("dot") is None:
        raise RuntimeError("graphviz `dot` is required to rebuild category_parent_graph.svg")

    shutil.copy2(_DOT, _SPIKE_DOT)
    subprocess.run(
        ["dot", "-Tsvg", str(_SPIKE_DOT), "-o", str(_SPIKE_SVG)],
        check=True,
    )
    bust = int.from_bytes(hashlib.sha256(_DOT.read_bytes()).digest()[:8], "big") if cache_bust is None else cache_bust
    html = _SPIKE_HTML.read_text(encoding="utf-8")
    html, n = re.subn(
        r"category_parent_graph\.svg\?v=\d+",
        f"category_parent_graph.svg?v={bust}",
        html,
        count=1,
    )
    if n != 1:
        raise RuntimeError(f"{_SPIKE_HTML} missing category_parent_graph.svg?v=… fetch URL to bump")
    _SPIKE_HTML.write_text(html, encoding="utf-8")
    return {"dot": _DOT, "svg": _SPIKE_SVG, "html": _SPIKE_HTML, "cache_bust": bust}
