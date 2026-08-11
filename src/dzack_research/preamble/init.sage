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

from dzack_research.preamble.categories.rings import rings as _owned_rings
from dzack_research.preamble.display import install_implicit_typesetting
from dzack_research.preamble.install import install_preamble

Σ = sum
Π = prod

# One call, one mechanism: the categories, their install hooks, and every name
# the preamble's modules export -- ``Lattices``, ``zipsum``, ``Sterk`` -- are
# bound into this session.  The ``.sage`` tests call the same function with
# their own namespace, so the two cannot drift apart.
install_preamble(globals())

libgap.LoadPackage("PackageManager")
IPython.core.ultratb.VerboseTB._tb_highlight = "bg:ansired"

Lattices.install(globals())

# The session's names for the owned rings, bound last.
#
# In code the owned rings are spelled so that a missing import fails loudly;
# nobody types those at a prompt, so a session gets them under the names it
# already uses.  This is the one place the two spellings meet, and it is the
# last act because any further loading re-imports Sage's namespace and would
# rebind these to the engine behind the session's back.
# Read off the module, not from names bound here: the code spellings
# normalize to ``Z``, ``Q``, ``R``, ``C`` under Python's identifier rules, and
# ``Lattices.install`` has just bound ``Z`` to the rank-one lattice
# $\langle 1\rangle$.  A bare ``ZZ = ℤ`` on this line reads that lattice.
ZZ = _owned_rings.ℤ
QQ = _owned_rings.ℚ
RR = _owned_rings.ℝ
CC = _owned_rings.ℂ

from sage_julia_bridge import JuliaHandle, julia

julia.eval("using Oscar")

install_implicit_typesetting(get_ipython())

# Sage routes ``load(...)`` through its active preparser, so the interactive
# extension is installed only after every authored preamble file has loaded.
import sageparse.preparser.research  # noqa: F401
