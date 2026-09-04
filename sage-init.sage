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
import sys
from pathlib import Path

import IPython.core.ultratb
from sage.env import SAGE_STARTUP_FILE
from sage.libs.gap.libgap import libgap
from sage.misc.latex import latex

# Sage loads this file with ``run_cell(source)``, so ``__file__`` is never
# set.  ``SAGE_STARTUP_FILE`` is the symlink (or the file itself); resolve
# it to the tracked copy in the repo.
_VENDOR_DIR = Path(SAGE_STARTUP_FILE).resolve().parent / "computations" / "vendor"
if _VENDOR_DIR.is_dir():
    _vendor = str(_VENDOR_DIR)
    if _vendor not in sys.path:
        sys.path.append(_vendor)


def typesets_itself(obj):
    if hasattr(type(obj), "_latex_"):
        return True
    if isinstance(obj, (list, tuple, set, frozenset)):
        return bool(obj) and all(typesets_itself(member) for member in obj)
    if isinstance(obj, dict):
        return bool(obj) and all(typesets_itself(value) for value in obj.values())
    return False


def latex_if_typesettable(obj):
    if not typesets_itself(obj):
        return None
    return "$\\displaystyle " + str(latex(obj)) + "$"


def install_implicit_typesetting(shell):
    shell.display_formatter.formatters["text/latex"].for_type(
        object, latex_if_typesettable
    )


# One import, and it is the same one a script or a notebook cell makes.
# ``dzack_research.preamble.all`` is the analogue of ``sage.all``, so this
# file states the session in one line rather than keeping a second copy of
# the sequence that would drift from it.
from dzack_research.preamble.all import *

Σ = sum
Π = prod

libgap.LoadPackage("PackageManager")
IPython.core.ultratb.VerboseTB._tb_highlight = "bg:ansired"

# Before the Julia bridge, because a session that cannot reach Julia is still
# a session and should still typeset.  The bridge is a computational backend
# and its absence is loud -- Sage prints the startup traceback -- but it used
# to take this line down with it, and then nothing in the session rendered.
install_implicit_typesetting(get_ipython())

from sage_julia_bridge import JuliaHandle, julia

julia.eval("using Oscar")

import sageparse.preparser.research  # noqa: F401
