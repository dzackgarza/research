r"""Implicit typesetting: a cell's result renders as LaTeX when it can.

A bare ``X`` at the end of a cell renders as LaTeX whenever ``X`` knows how to
typeset itself, and stays plain text otherwise, so ``show(X)`` need not be
written by hand.

Not ``%display latex``: that typesets everything, and for an object that
cannot typeset it emits a character-by-character fallback -- a plain string
becomes ``\text{\texttt{a{ }plain{ }string}}``, a numpy array becomes
``\text{\texttt{[1.5{ }2.5]}}``. Those are worse than the plain repr.

The test is therefore the object's own capability. That capability is a
``_latex_`` method and nothing else: ``SageObject`` does not define one, so
being a Sage object is not the question -- ``latex()`` of a ``SageObject``
without ``_latex_`` produces exactly the escaped-text fallback this avoids.
Containers count when their contents do (dicts: their values, so string keys
do not disqualify them), since a list of polynomials typesets well.

Only the ``text/latex`` slot is registered. ``text/plain`` is still emitted
alongside, so nothing is lost; ``print()``, tracebacks, plots and images are
untouched.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from IPython.core.interactiveshell import InteractiveShell
from sage.misc.latex import latex

if TYPE_CHECKING:
    from sage.structure.parent import ElementConstructorInput


def typesets_itself(obj: object) -> bool:
    r"""Return whether ``obj`` can render itself as LaTeX.

    The capability is ``_latex_`` on the type. Asked of the type rather than
    the instance so a stray attribute on one object cannot answer for its
    class, and so the question is the same one Sage's ``latex()`` dispatches
    on.
    """
    if hasattr(type(obj), "_latex_"):
        return True
    if isinstance(obj, (list, tuple, set, frozenset)):
        return bool(obj) and all(typesets_itself(member) for member in obj)
    if isinstance(obj, dict):
        return bool(obj) and all(typesets_itself(value) for value in obj.values())
    return False


def latex_if_typesettable(obj: ElementConstructorInput) -> str | None:
    r"""Return ``obj`` as displayed LaTeX, or ``None`` to leave it plain."""
    if not typesets_itself(obj):
        return None
    return "$\\displaystyle " + str(latex(obj)) + "$"


def install_implicit_typesetting(shell: InteractiveShell) -> None:
    r"""Register the rule on ``shell``, an IPython session.

    Takes the shell rather than calling ``get_ipython()`` so this is callable
    from anywhere and does nothing surprising outside a session. The functions
    it registers live in this module, so they resolve in module scope: the
    earlier version defined them in the session namespace, where deleting
    either broke every subsequent display with ``NameError``.
    """
    shell.display_formatter.formatters["text/latex"].for_type(
        object, latex_if_typesettable
    )
