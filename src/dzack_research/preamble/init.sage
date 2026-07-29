# Notebook / IPython session startup (SAGE_STARTUP_FILE).
# ``just sage-init-install`` links ``${DOT_SAGE:-~/.sage}/init.sage`` -> this file.
# Loaded by Sage's IPython extension (REPL + Jupyter kernels), not by ``sage -c``.
#
# Implicit typesetting of cell results: a bare `X` at the end of a cell renders as
# LaTeX whenever X is something Sage can genuinely typeset, and stays plain text
# otherwise. This avoids having to write show(X) by hand.
#
# Why not `%display latex`: that mode typesets *everything*, and for objects it
# cannot typeset it emits a character-by-character fallback, so a plain string
# becomes \text{\texttt{a{ }plain{ }string}}, a numpy array becomes
# \text{\texttt{[1.5{ }2.5]}}, and an ordinary Python object becomes an unreadable
# run of {\char`\_} escapes. Those are worse than the plain repr.
#
# The test is therefore the object's own typesetting capability -- a `_latex_`
# method -- not the shape of the rendered string, which varies between Sage's
# rendering paths and across versions. Containers count as typesettable when their
# contents are (dicts: their values, so str keys do not disqualify them), since a
# list of polynomials typesets well.
#
# Only the text/latex slot is touched. text/plain is still emitted alongside, so
# nothing is lost; print(), tracebacks, plots and images are untouched.

from pathlib import Path
import os
import sys

# This file *is* the startup file (via symlink). Sibling scripts live next to it.
_PREAMBLE = Path(os.environ["SAGE_STARTUP_FILE"]).resolve().parent

_VENDOR_DIR = _PREAMBLE.parents[2] / "computations" / "vendor"

def _vendor_import_roots(vendor_dir):
    assert vendor_dir.is_dir(), f"vendor directory is missing: {vendor_dir}"
    roots = {vendor_dir}
    for path in vendor_dir.rglob("*"):
        if not path.is_dir():
            continue
        relative_parts = path.relative_to(vendor_dir).parts
        if any(part.startswith(".") or part == "__pycache__" for part in relative_parts):
            continue
        children = tuple(path.iterdir())
        exposes_loose_module = any(child.is_file() and child.suffix == ".py" for child in children)
        exposes_package = any(
            child.is_dir() and (child / "__init__.py").is_file()
            for child in children
        )
        if exposes_loose_module or exposes_package:
            roots.add(path)
    return tuple(sorted(roots))

for _vendor_root in _vendor_import_roots(_VENDOR_DIR):
    _vendor_entry = str(_vendor_root)
    if _vendor_entry not in sys.path:
        sys.path.append(_vendor_entry)

load(str(_PREAMBLE / "refine.sage"))
load(str(_PREAMBLE / "categories/gram_matrices.sage"))
load(str(_PREAMBLE / "categories/integrallattice/integral_lattices.sage"))
load(str(_PREAMBLE / "categories/integrallattice/subobjects.sage"))
load(str(_PREAMBLE / "categories/integrallattice/direct_sum_objects.sage"))
load(str(_PREAMBLE / "categories/lattice_homomorphisms.sage"))
load(str(_PREAMBLE / "categories/lattice_isometries.sage"))
load(str(_PREAMBLE / "categories/integrallattice/hyperbolic_lattices.sage"))
load(str(_PREAMBLE / "categories/torsionform/torsion_modules_with_form.sage"))
load(str(_PREAMBLE / "categories/torsionform/fgptorsionmodule.sage"))
load(str(_PREAMBLE / "categories/torsionform/discriminant_bilinear_modules.sage"))
load(str(_PREAMBLE / "categories/torsionform/discriminant_quadratic_modules.sage"))

install_integral_lattices()
install_fgp_torsionmodule()
install_discriminant_groups()
activate()

load(str(_PREAMBLE / "ergonomics.sage"))
load(str(_PREAMBLE / "catalogue.sage"))
load(str(_PREAMBLE / "sterk.sage"))

Lattices.install(globals())

from sage_julia_bridge import JuliaHandle, julia

julia.eval("using Oscar")

from sage_lattice_category_spike import (
    CoxeterDiagramHomset,
    CoxeterDiagramMorphism,
    CoxeterDiagrams,
    FiniteCoxeterDiagram,
)

## Implicit typesetting #######################################################

def _typesettable(obj):
    if hasattr(obj, "_latex_"):
        return True
    if isinstance(obj, (list, tuple, set, frozenset)):
        return bool(obj) and all(_typesettable(v) for v in obj)
    if isinstance(obj, dict):
        return bool(obj) and all(_typesettable(v) for v in obj.values())
    return False

def _latex_if_typesettable(obj):
    if not _typesettable(obj):
        return None
    return "$\\displaystyle " + str(latex(obj)) + "$"

# Both names must stay resident: the registered formatter looks _typesettable up
# by global name on every call, so deleting them breaks display with a NameError.
get_ipython().display_formatter.formatters["text/latex"].for_type(
    object, _latex_if_typesettable
)
