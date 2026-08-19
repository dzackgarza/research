"""
oscar_centralizer — Python wrapper for oscar_centralizer.jl (OSCAR backend).

Calls Julia/OSCAR to compute:
  - Invariant sublattice basis (L^f = ker(f - I))
  - Coinvariant sublattice basis (L_f = ker(f + I))
  - Generators of the image of Z_{O(L)}(f) in O(A_L, D_f)

Requires: Julia with Oscar.jl installed (the standard OSCAR package).
The Julia binary on PATH must have Oscar available in its default environment,
or set JULIA_PROJECT to a suitable environment.

Usage::

    from src.oscar_centralizer import oscar_centralizer_data
    result = oscar_centralizer_data(gram_matrix, isometry_matrix)
    # result["invariant_basis"]         -- list of lists (rational rows)
    # result["coinvariant_basis"]       -- list of lists (rational rows)
    # result["image_centralizer_gens"]  -- list of (list of lists) matrices
    # result["image_centralizer_order"] -- int, -1 if odd lattice (not computed)
"""

from __future__ import annotations

import ast
import subprocess
import tempfile
import textwrap
from pathlib import Path

_SCRIPT = Path(__file__).parent / "oscar_centralizer.jl"


def _write_int_matrix(path: Path, rows) -> None:
    """Write an integer matrix (list of lists) to a whitespace-separated file."""
    with open(path, "w") as f:
        for row in rows:
            f.write(" ".join(str(x) for x in row) + "\n")


def oscar_centralizer_data(gram_rows: list, isometry_rows: list) -> dict:
    """Call Julia/OSCAR to compute centralizer and eigenspace data.

    Parameters
    ----------
    gram_rows:
        Gram matrix as a list of lists of Python ints.
    isometry_rows:
        Isometry matrix as a list of lists of Python ints.

    Returns
    -------
    dict with keys:
        ``invariant_basis``         list of rational-entry rows (basis of L^f)
        ``coinvariant_basis``       list of rational-entry rows (basis of L_f)
        ``image_centralizer_gens``  list of integer matrix rows-of-rows
        ``image_centralizer_order`` int (order of image; -1 if not computed)

    """
    assert _SCRIPT.exists(), f"Missing Julia script: {_SCRIPT}"

    with tempfile.TemporaryDirectory() as tmp:
        gram_path = Path(tmp) / "gram.txt"
        isom_path = Path(tmp) / "isom.txt"
        out_path = Path(tmp) / "result.txt"

        _write_int_matrix(gram_path, gram_rows)
        _write_int_matrix(isom_path, isometry_rows)

        result = subprocess.run(
            [
                "julia",
                "--startup-file=no",
                str(_SCRIPT),
                str(gram_path),
                str(isom_path),
                str(out_path),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"oscar_centralizer.jl failed (exit {result.returncode}):\n" + textwrap.indent(
            result.stderr, "  "
        )

        raw = out_path.read_text()

    # Julia output is almost Python-literal; just eval it
    data = ast.literal_eval(raw)
    return data
