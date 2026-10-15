r"""The category of elements of a set-valued functor."""

from __future__ import annotations

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.lexicon.category_theory import ObjectOfCategory


class _CategoryOfElements(OwnedCategory):
    r"""The category of elements ``int F`` of a functor ``F`` to ``Sets``.

    For a covariant ``F: C -> Sets`` an object is a pair ``(X, x)`` with ``X``
    an object of ``C`` and ``x`` an element of ``F(X)``; a morphism
    ``(X, x) -> (Y, y)`` is a morphism ``f: X -> Y`` of ``C`` with
    ``F(f)(x) = y``.  For a presheaf ``F: C^op -> Sets`` an object is again a
    pair ``(X, x)`` with ``x`` in ``F(X)``, and a morphism ``(X, x) -> (Y, y)``
    is ``f: X -> Y`` with ``F(f)(y) = x``.  Forgetting ``x`` is the projection
    functor ``int F -> C``, a discrete fibration (discrete opfibration in the
    covariant case); see Mac Lane, *Categories for the Working Mathematician*,
    II.6, and Riehl, *Category Theory in Context*, Definition 2.4.1.

    In the covariant case ``int F`` is the comma category ``(* | F)`` of the
    point ``* -> Sets`` and ``F``.  For a representable ``F = Mor(*, -)`` it is
    isomorphic to the coslice ``*/C``.  No comma construction is presented in
    the tree, so ``super_categories`` is left abstract.
    """

    def __init__(self, functor: Functor) -> None:
        self._functor = functor
        super().__init__()

    def _make_named_class_key(self, name):
        return self._functor

    def _repr_object_names(self) -> str:
        return f"elements of {self._functor}"

    def functor(self) -> Functor:
        r"""The functor ``F`` whose elements are the objects."""
        return self._functor

    def object(self, underlying_object: ObjectOfCategory, element) -> ObjectOfCategory:
        r"""The pair ``(X, x)`` of an object ``X`` and an element ``x`` of ``F(X)``."""
        assert False, "object on CategoryOfElements: not implemented"

    def projection_functor(self) -> Functor:
        r"""The projection ``int F -> C``, ``(X, x) |-> X`` and ``f |-> f``."""
        assert False, "projection_functor on CategoryOfElements: not implemented"

    class ParentMethods:
        r"""A pair ``(X, x)`` with ``x`` an element of ``F(X)``."""

        def underlying_object(self) -> ObjectOfCategory:
            r"""The object ``X``, the image of ``(X, x)`` under the projection functor."""
            assert False, "underlying_object on CategoryOfElements: not implemented"

        def element(self):
            r"""The chosen element ``x`` of ``F(X)``."""
            assert False, "element on CategoryOfElements: not implemented"

