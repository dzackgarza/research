r"""Polarized varieties, the Lefschetz operator and primitive cohomology."""

from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.varieties import Varieties
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom


class PolarizedVarieties(OwnedCategoryOverBaseRing):
    r"""Pairs ``(X, L)`` of a projective variety ``X`` over ``k`` and an ample line bundle ``L`` on ``X``.

    A pair ``(X, L)`` with ``L`` in ``Pic(X)`` is an object of the category of
    elements of ``Pic : Var_k^op -> Set``, and ampleness of ``L`` cuts out a
    full subcategory of it; a morphism ``(X, L) -> (Y, M)`` is a morphism
    ``f: X -> Y`` with ``f^* M = L`` in ``Pic(X)``.  The polarization is a
    chosen datum, so this is a data subcategory, not an axiom.  Forgetting
    ``L`` lands in ``Varieties(k).Projective()``: a variety over a field with
    an ample line bundle is projective, because a power of ``L`` is very ample
    (Hartshorne, *Algebraic Geometry*, II.7.6).
    """

    def _repr_object_names(self) -> str:
        return f"polarized varieties over {self.base_ring()}"

    def super_categories(self):
        return [Varieties(self.base_ring()).Projective()]

    def _call_(self, variety, ample_line_bundle):
        r"""The pair ``(X, L)`` of a projective variety and an ample line bundle on it."""
        assert False, "construction of a polarized variety on PolarizedVarieties: not implemented"

    class ParentMethods:
        r"""A projective variety with its chosen ample line bundle."""

        def polarization(self):
            r"""The chosen ample line bundle ``L``, an element of ``Pic(X)``."""
            assert False, "polarization on PolarizedVarieties: not implemented"

        def polarization_class(self):
            r"""``h = c_1(L) in H^2(X(CC); ZZ)`` for ``k`` embedded in ``CC``.

            The first Chern class of ``L`` in the integral singular cohomology
            of the analytification ``X(CC)`` (Voisin, *Hodge Theory and Complex
            Algebraic Geometry I*, §7.1).
            """
            assert False, "polarization_class on PolarizedVarieties: not implemented"

    class Smooth(CategoryWithAxiom):
        r"""Polarized varieties ``(X, L)`` with ``X`` smooth over ``k``."""

        class ParentMethods:
            def lefschetz_operator(self):
                r"""``L_h = h cup (-) : H^*(X(CC); QQ) -> H^{*+2}(X(CC); QQ)``.

                Cup product with the polarization class ``h = c_1(L)``, a
                degree-2 endomorphism of the graded ``QQ``-module
                ``H^*(X(CC); QQ)``.  For ``n = dim X`` the hard Lefschetz
                theorem states that ``L_h^{n-k} : H^k -> H^{2n-k}`` is an
                isomorphism for ``k <= n`` (Voisin, op. cit., §6.2).
                """
                assert False, "lefschetz_operator on PolarizedVarieties.Smooth: not implemented"

            def primitive_cohomology(self, k):
                r"""``H^k_prim = ker(L_h^{n-k+1} : H^k -> H^{2n-k+2})`` for ``k <= n = dim X``.

                A ``QQ``-submodule of ``H^k(X(CC); QQ)``, returned as the
                kernel inclusion.  The Lefschetz decomposition is
                ``H^k = sum_r L_h^r H^{k-2r}_prim`` (Voisin, op. cit., §6.2).
                """
                assert False, "primitive_cohomology on PolarizedVarieties.Smooth: not implemented"


__all__ = ["PolarizedVarieties"]
