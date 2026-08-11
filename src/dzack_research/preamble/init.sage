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

# Nothing standard is imported here.  This file is Sage's startup file, so it
# runs in a session that has already imported ``sage.all``: ``ZZ``, ``QQ``,
# ``RR``, ``CC``, ``latex``, ``prod`` and ``SageObject`` are present, and
# importing them again only creates a second name for the same object -- or,
# as happened with ``RR``, a line that names a module which does not export it
# and takes the whole startup down with it.
from pathlib import Path
import os

import IPython.core.ultratb
from sage.libs.gap.libgap import libgap

Σ = sum
Π = prod

# This file *is* the startup file (via symlink). Sibling scripts live next to it.
_PREAMBLE = Path(os.environ["SAGE_STARTUP_FILE"]).resolve().parent

# The category modules, their install hooks, and the export sweep that puts
# their names in this session -- shared with the .sage tests so the two never
# drift apart.  ``utilities`` and ``catalogue`` are in the module list it
# imports, so this is where ``Lattices`` and ``zipsum`` come from; loading
# either again would build a second copy of the catalogue.
load(str(_PREAMBLE / "install.sage"))

libgap.LoadPackage("PackageManager")
IPython.core.ultratb.VerboseTB._tb_highlight = "bg:ansired"

# Not in that module list, so it is still loaded on its own.
load(str(_PREAMBLE / "sterk.sage"))

Lattices.install(globals())

# After the install, which is where ``ZZ`` becomes the session's name for the
# ring: these are the same names written the way a paper writes them, so they
# must name the same objects.
ℤ = ZZ
ℚ = QQ
ℝ = RR
ℂ = CC

from sage_julia_bridge import JuliaHandle, julia

julia.eval("using Oscar")

## Implicit typesetting #######################################################

def _typesettable(obj):
    if isinstance(obj, SageObject):
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

# Sage routes ``load(...)`` through its active preparser, so the interactive
# extension is installed only after every authored preamble file has loaded.
import sageparse.preparser.research  # noqa: F401
