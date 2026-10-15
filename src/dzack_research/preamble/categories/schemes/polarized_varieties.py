r"""The category of elements of the Picard functor, polarized varieties, the Lefschetz operator and primitive cohomology."""

from sage.categories.category_with_axiom import all_axioms
from sage.structure.element import Element

from dzack_research.preamble.categories.abstract_categories.categories_of_elements import (
    _CategoryOfElements,
    _object_of_elements,
)
from dzack_research.preamble.lexicon.category_theory import ObjectOfCategory
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom

if "Ample" not in all_axioms:
    all_axioms.add("Ample")


class _PicardCategoryOfElements(_CategoryOfElements):
    r"""``int Pic`` over a category ``C`` of schemes.

    ``Pic : C^op -> Mod_ZZ`` is read through the forgetful functor to
    ``Sets``.  An object is a pair ``(X, L)`` with ``X`` an object of ``C`` and
    ``L`` a class in ``Pic(X)``; a morphism ``(X, L) -> (Y, M)`` is
    ``f: X -> Y`` with ``f^* M = L``.  Whether ``L`` is ample is a property of
    the element, so the pairs with ``L`` ample are the full subcategory
    ``Ample()`` (``CAT-30``).
    """

    class SubcategoryMethods:
        def Ample(self):
            r"""The full subcategory on the pairs ``(X, L)`` with ``L`` ample."""
            return self._with_axiom("Ample")

    class Ample(CategoryWithAxiom):
        r"""The full subcategory of ``int Pic`` on the pairs ``(X, L)`` with ``L`` ample.

        Over a category ``C`` of projective varieties over a field ``k``
        these are the polarized varieties: a projective variety ``X`` with
        the class of an ample line bundle ``L``.  A morphism
        ``(X, L) -> (Y, M)`` is ``f: X -> Y`` with ``f^* M = L``.  A variety
        over ``k`` with an ample line bundle is projective, because a power
        of ``L`` is very ample (Hartshorne, *Algebraic Geometry*, II.7.6).
        """

        def object(self, underlying_object: ObjectOfCategory, element: Element) -> ObjectOfCategory:
            r"""The pair ``(X, L)`` of an object ``X`` of ``C`` and an ample class ``L`` in ``Pic(X)``.

            Ampleness of ``L`` is the caller's datum; construction stores
            the pair and does not decide it.
            """
            return _object_of_elements(self, self.base_category(), underlying_object, element)

        __call__ = object

        def an_object(self) -> ObjectOfCategory:
            r"""``(P^1, [O(1)])`` over the base ring of ``C``; ``O(1)`` is very ample on ``P^n`` (Hartshorne, II.7)."""
            from dzack_research.preamble.categories.schemes.schemes import ProjectiveSpaces

            schemes = self.base_category().projection_functor().codomain()
            line = ProjectiveSpaces(schemes.base_ring())(1)
            assert line in schemes, (
                f"the witness (P^1, [O(1)]) of {self} needs P^1 to be an object of {schemes}, but it is not"
            )
            return self(line, line.hyperplane_class())

        class ParentMethods:
            r"""An object ``X`` of ``C`` with its chosen ample class ``L``."""

            def polarization(self) -> Element:
                r"""The ample class ``L`` in ``Pic(X)`` of the pair ``(X, L)``."""
                return self.element()

            def polarization_class(self):
                r"""``h = c_1(L) in H^2(X(CC); ZZ)`` for ``k`` embedded in ``CC``.

                The first Chern class of ``L`` in the integral singular
                cohomology of the analytification ``X(CC)`` (Voisin, *Hodge
                Theory and Complex Algebraic Geometry I*, §7.1).
                """
                assert False, "polarization_class on polarized varieties: not implemented"

        class Smooth(CategoryWithAxiom):
            r"""The polarized pairs ``(X, L)`` with ``X`` smooth."""

            class ParentMethods:
                r"""A smooth projective variety ``X`` with its chosen ample class ``L``."""

                def lefschetz_operator(self):
                    r"""``L_h = h cup (-) : H^*(X(CC); QQ) -> H^{*+2}(X(CC); QQ)``.

                    Cup product with the polarization class ``h = c_1(L)``, a
                    degree-2 endomorphism of the graded ``QQ``-module
                    ``H^*(X(CC); QQ)``.  For ``X`` smooth of dimension ``n`` the
                    hard Lefschetz theorem states that
                    ``L_h^{n-k} : H^k -> H^{2n-k}`` is an isomorphism for
                    ``k <= n`` (Voisin, op. cit., §6.2).
                    """
                    assert False, "lefschetz_operator on smooth polarized varieties: not implemented"

                def primitive_cohomology(self, k):
                    r"""``H^k_prim = ker(L_h^{n-k+1} : H^k -> H^{2n-k+2})`` for ``k <= n = dim X``.

                    A ``QQ``-submodule of ``H^k(X(CC); QQ)``, returned as the
                    kernel inclusion.  The Lefschetz decomposition is
                    ``H^k = sum_r L_h^r H^{k-2r}_prim`` (Voisin, op. cit.,
                    §6.2).
                    """
                    assert False, "primitive_cohomology on smooth polarized varieties: not implemented"
