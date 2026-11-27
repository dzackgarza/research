r"""Lattices over the integer ring."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .over_pid import _LatticesOverPID

if TYPE_CHECKING:
    from ...types import Integer, Matrix, RingElement, SetFamily


class _LatticesOverIntegers(CategoryWithAxiom_over_base_ring):
    r"""Integral lattices over ``ZZ``.

    Canonical chain: ``Lattices(R).OverDedekindDomain().OverPID().OverIntegers()``.
    """

    _base_category_class_and_axiom = (_LatticesOverPID, "OverIntegers")
    _defining_predicates = ("is_over_integers",)

    class ParentMethods:
        @final
        def is_over_integers(self) -> bool:
            return True

        @abstract_method
        def genus(self): ...

        @abstract_method
        def minimum(self) -> RingElement: ...

        @abstract_method
        def short_vectors(self, bound: RingElement) -> SetFamily:
            r"""Return vectors ``v`` whose norm ``b(v, v)`` is at most ``bound``."""
            ...

        @final
        def short_vectors_up_to_sign(self, bound: RingElement) -> SetFamily:
            r"""Return representatives for the sign orbits ``{v, -v}`` in ``short_vectors(bound)``."""
            return self.short_vectors(bound, up_to_sign_flag=True)

        @abstract_method
        def LLL(
            self,
            delta: RingElement | None = None,
            eta: RingElement | None = None,
            algorithm: str = "fpLLL:wrapper",
            fp: str | None = None,
            prec: Integer = 0,
            early_red: bool = False,
            use_givens: bool = False,
            use_siegel: bool = False,
            transformation: bool = False,
        ) -> Matrix: ...

    class ElementMethods: ...
    class MorphismMethods: ...
