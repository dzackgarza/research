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

import IPython.core.ultratb
from sage.libs.gap.libgap import libgap
from sage.repl.preparse import implicit_multiplication

Σ = sum
Π = prod

ℤ = ZZ
ℚ = QQ
ℝ = RR
ℂ = CC

# This file *is* the startup file (via symlink). Sibling scripts live next to it.
_PREAMBLE = Path(os.environ["SAGE_STARTUP_FILE"]).resolve().parent

# Mathematical brace literals: ``{a, b}`` is a Sage ``Set`` in notebook and
# REPL input; dictionaries remain dictionaries.
load(str(_PREAMBLE / "preparse_sets.py"))
from sage.sets.image_set import ImageSet
from sage.sets.condition_set import ConditionSet
from sage.repl import interpreter as _sage_interpreter
from sage.repl import preparse as _sage_preparse

install_set_literal_preparser(_sage_preparse, _sage_interpreter)

# Vendor paths, the category scripts, and their install hooks -- shared with the
# .sage tests so the two never drift apart.
load(str(_PREAMBLE / "install.sage"))

implicit_multiplication(True)
libgap.LoadPackage("PackageManager")
IPython.core.ultratb.VerboseTB._tb_highlight = "bg:ansired"

load(str(_PREAMBLE / "utilities.py"))
load(str(_PREAMBLE / "catalogue.sage"))
load(str(_PREAMBLE / "sterk.sage"))

Lattices.install(globals())

from sage_julia_bridge import JuliaHandle, julia

julia.eval("using Oscar")

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
