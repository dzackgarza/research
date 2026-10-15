r"""Polarized varieties, the Lefschetz operator and primitive cohomology."""

from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.varieties import Varieties


class _PolarizedVarieties(OwnedCategoryOverBaseRing):
    r"""The full subcategory of ``int Pic`` on the pairs ``(X, L)`` with ``L`` ample.

    ``Pic : Var_k^{proj, op} -> Sets`` sends a projective variety ``X`` over
    ``k`` to the underlying set of its Picard group and ``f: X -> Y`` to
    ``f^*``.  An object of its category of elements is a pair ``(X, L)`` with
    ``L`` in ``Pic(X)``, and a morphism ``(X, L) -> (Y, M)`` is ``f: X -> Y``
    with ``f^* M = L``.  Ampleness of ``L`` is a property of the object of
    ``int Pic`` and cuts out this full subcategory.  Every member of
    ``int Pic`` lies over a projective variety, and conversely a variety over a
    field with an ample line bundle is projective, because a power of ``L`` is
    very ample (Hartshorne, *Algebraic Geometry*, II.7.6).
    """

    def _repr_object_names(self) -> str:
        return f"polarized varieties over {self.base_ring()}"

    def super_categories(self):
        return [Varieties(self.base_ring()).Projective().picard_functor().category_of_elements()]

    def _call_(self, variety, ample_line_bundle):
        r"""The pair ``(X, L)`` of a projective variety and an ample line bundle on it."""
        assert False, "construction of a polarized variety on PolarizedVarieties: not implemented"

    class ParentMethods:
        r"""A projective variety with its chosen ample line bundle."""

        def polarization(self):
            r"""The chosen ample line bundle ``L``, the element of ``Pic(X)`` in ``(X, L)``."""
            assert False, "polarization on PolarizedVarieties: not implemented"

        def polarization_class(self):
            r"""``h = c_1(L) in H^2(X(CC); ZZ)`` for ``k`` embedded in ``CC``.

            The first Chern class of ``L`` in the integral singular cohomology
            of the analytification ``X(CC)`` (Voisin, *Hodge Theory and Complex
            Algebraic Geometry I*, §7.1).
            """
            assert False, "polarization_class on PolarizedVarieties: not implemented"

        def lefschetz_operator(self):
            r"""``L_h = h cup (-) : H^*(X(CC); QQ) -> H^{*+2}(X(CC); QQ)``, for ``X`` smooth.

            Cup product with the polarization class ``h = c_1(L)``, a degree-2
            endomorphism of the graded ``QQ``-module ``H^*(X(CC); QQ)``.  For
            ``X`` smooth of dimension ``n`` the hard Lefschetz theorem states
            that ``L_h^{n-k} : H^k -> H^{2n-k}`` is an isomorphism for
            ``k <= n`` (Voisin, op. cit., §6.2).
            """
            assert False, "lefschetz_operator on PolarizedVarieties: not implemented"

        def primitive_cohomology(self, k):
            r"""``H^k_prim = ker(L_h^{n-k+1} : H^k -> H^{2n-k+2})`` for ``k <= n = dim X``, ``X`` smooth.

            A ``QQ``-submodule of ``H^k(X(CC); QQ)``, returned as the kernel
            inclusion.  The Lefschetz decomposition is
            ``H^k = sum_r L_h^r H^{k-2r}_prim`` (Voisin, op. cit., §6.2).
            """
            assert False, "primitive_cohomology on PolarizedVarieties: not implemented"
