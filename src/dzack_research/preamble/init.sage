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
import IPython.core.ultratb
from sage.libs.gap.libgap import libgap

from dzack_research.preamble.display import install_implicit_typesetting

# One import, and it is the same one a script or a notebook cell makes: the
# categories and their install hooks, every name the preamble's modules export
# -- ``Lattices``, ``zipsum``, ``Sterk`` -- the named specimens, and the
# session's own ``ZZ`` and ``QQ``, which are the owned rings and not the
# engine's.  ``dzack_research.preamble.all`` is the analogue of ``sage.all``,
# so this file states the session in one line rather than keeping a second
# copy of the sequence that would drift from it.
#
# The ring names used to be bound by hand here, last, because any further
# ``load()`` re-imports Sage's namespace and would rebind them to the engine
# behind the session's back.  That is no longer an ordering fact to maintain:
# the ``load`` this import binds re-owns the scope it ran in, so the property
# holds wherever the line sits.
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

# Sage routes ``load(...)`` through its active preparser, so the interactive
# extension is installed only after every authored preamble file has loaded.
import sageparse.preparser.research  # noqa: F401
