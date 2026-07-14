r"""Compactifications of ordinary schemes (independent of moduli of curves)."""

from __future__ import annotations

from sage.rings.rational_field import QQ

from ..categories.base import AffineScheme, spec
from .stacks import Compactification, Stack
from .stratification import Stratification, scheme_compactification_stratification


class SchemeStack(Stack):
    r"""A scheme regarded as a stack (representable Deligne--Mumford stack).

    Used for general compactification examples independent of moduli of curves
    (e.g. `\mathbf A^1\hookrightarrow\mathbf P^1`).
    """

    def __init__(self, scheme: object, base: AffineScheme, *, proper: bool, name: str) -> None:
        axioms = frozenset({"FiniteType", "Separated"})
        if proper:
            axioms = axioms | {"Proper"}
        self._scheme = scheme
        Stack.__init__(self, base, name=name, axioms=axioms)

    def sage_scheme(self) -> object:
        return self._scheme

    def as_stack(self) -> SchemeStack:
        return self

    def stratify(self, pieces: list[object] | None = None) -> Stratification:
        if pieces is None or len(pieces) != 2:
            raise ValueError("scheme stratify expects [open, boundary]")
        return scheme_compactification_stratification(pieces[0], pieces[1], self)


def scheme_open_immersion_compactification(open_scheme: object, proper_scheme: object) -> Compactification:
    r"""Compactification of an open scheme into a proper scheme (e.g. A^1 ↪ P^1)."""
    base = spec(QQ)
    source = SchemeStack(open_scheme, base, proper=False, name=repr(open_scheme))
    target = SchemeStack(proper_scheme, base, proper=True, name=repr(proper_scheme))
    return Compactification(source, target, kind="scheme-open-immersion")
