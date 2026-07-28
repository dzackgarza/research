# Sage startup file (SAGE_STARTUP_FILE), read by the terminal REPL *and* by every
# Jupyter sagemath kernel.
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

## Session preamble ##########################################################
#
# Vendor import paths and category hooks live in the repo, in
# dzack_research.preamble, NOT in a hand-placed .pth inside Sage's venv: a .pth
# there is untracked, unreviewable, and destroyed by any Sage rebuild. The
# package is pip-installed editable (`just sage-init-install` documents the
# wiring), so it follows the working tree.
#
# Interactive defaults (implicit multiplication, red tracebacks, GAP
# PackageManager) apply when ergonomics is imported — which install() does.
# Star-import session surfaces so new public names appear without editing this
# file; each module's ``__all__`` is the allowlist.

from dzack_research.preamble import install as _install_preamble
from dzack_research.preamble.catalogue import *
from dzack_research.preamble.ergonomics import *
from dzack_research.preamble.fixtures import (
    CROSS_CHECK_RECIPES,
    DIAGRAM_CONVENTION,
    STERK_POSITIONS,
    STERK_ROOT_COUNTS,
)
from dzack_research.preamble.sterk import *
from sage_lattice_category_spike import (
    CoxeterDiagramHomset,
    CoxeterDiagramMorphism,
    CoxeterDiagrams,
    FiniteCoxeterDiagram,
)

_preamble_report = _install_preamble()

## Implicit typesetting #######################################################

_ip = get_ipython()
if _ip is not None and getattr(_ip, "display_formatter", None) is not None:

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
    _ip.display_formatter.formatters["text/latex"].for_type(
        object, _latex_if_typesettable
    )

del _ip
