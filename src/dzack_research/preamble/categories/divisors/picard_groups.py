r"""The Picard functor ``Pic : C^op -> Mod_ZZ`` on a category of schemes.

For a scheme ``X`` the Picard group ``Pic(X)`` is the abelian group of
isomorphism classes of invertible ``O_X``-modules under tensor product, and a
morphism ``f: X -> Y`` induces the pullback ``f^* : Pic(Y) -> Pic(X)``,
``[L] |-> [f^* L]`` (Hartshorne, *Algebraic Geometry*, II.6).  An abelian group
is a ``ZZ``-module, so the values are objects of ``Modules(ZZ)``.  The value at
one scheme is that scheme's ``picard_group()``; this module holds the functor
and the represented values that the projective-bundle formula and the field
case build.
"""

from sage.categories.map import Map
from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent

from dzack_research.preamble.categories.divisors.divisor_groups import _integers
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _owned_integers
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.lexicon.category_theory import ObjectOfCategory
from dzack_research.preamble.owned_category_bases import Category


class _PicardFunctor(Functor):
    r"""``Pic : C^op -> Mod_ZZ`` on a category ``C`` of schemes over a base ring.

    ``op(X) |-> Pic(X)``, the group of isomorphism classes of invertible
    ``O_X``-modules under tensor product, and ``op(f) |-> f^*`` for
    ``f: X -> Y`` (Hartshorne, *Algebraic Geometry*, II.6).  Pullback
    preserves tensor products, so ``f^*`` is a group homomorphism, and
    ``(g f)^* = f^* g^*``, so ``Pic`` is contravariant.
    """

    def __init__(self, scheme_category: Category) -> None:
        self._scheme_category = scheme_category
        super().__init__(scheme_category.opposite(), Modules(_owned_integers()))

    def _apply_object(self, opposite_scheme: ObjectOfCategory) -> Parent:
        r"""``Pic(X)`` for the object ``op(X)`` of ``C^op``."""
        return opposite_scheme.underlying_object().picard_group()

    def _apply_morphism(self, morphism: Map) -> Map:
        r"""``f^* : Pic(Y) -> Pic(X)``, ``[L] |-> [f^* L]``, for the arrow ``op(f): op(Y) -> op(X)`` of ``f: X -> Y``."""
        assert False, "pullback f^* on the Picard functor: not implemented"

    @cached_method
    def category_of_elements(self):
        r"""``int Pic`` over ``C``: the pairs ``(X, L)`` with ``L`` in ``Pic(X)``.

        ``Pic`` is a presheaf on ``C``, so a morphism ``(X, L) -> (Y, M)`` is
        ``f: X -> Y`` with ``f^* M = L``.
        """
        from dzack_research.preamble.categories.schemes.polarized_varieties import (
            _PicardCategoryOfElements,
        )

        return _PicardCategoryOfElements(self, self._scheme_category)

    def _repr_(self) -> str:
        return "Pic"


def _zero_picard_group() -> Parent:
    r"""``Pic(X) = 0``, the free ``ZZ``-module on no classes.

    The value for ``X = Spec k`` with ``k`` a field, and more generally for
    the schemes whose invertible sheaves are all trivial, such as ``A^n_k``:
    there ``Pic = Cl`` (Hartshorne, II.6.16), and ``Cl = 0`` because
    ``k[x_1, ..., x_n]`` is a unique factorization domain.
    """
    return _integers().free_module(finite_ordered_set(()))


def _projective_bundle_picard_group(base_picard_group: Parent) -> Parent:
    r"""``Pic(P^n_S) = Pic(S) + ZZ[O(1)]``, the biproduct of ``Pic(S)`` and the hyperplane summand.

    The base Picard group is required input, so this never replaces it by
    zero.  The injection of the second factor sends its generator ``O(1)``
    to the hyperplane class ``[O(1)]`` (Hartshorne, II.6.17 and II,
    Exercise 6.1).
    """
    integers = _integers()
    hyperplane = integers.free_module(finite_ordered_set(("O(1)",)))
    return Modules(integers).biproduct((base_picard_group, hyperplane))


__all__ = []
