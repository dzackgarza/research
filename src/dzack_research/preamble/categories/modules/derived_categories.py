r"""Derived categories of modules and the localization functor from cochain complexes."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.cochain_complexes import (
    CochainComplexes,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _owned_ring,
)


class DerivedCategories(OwnedCategoryOverBaseRing):
    r"""The derived category \(D(R)\) of the abelian category of \(R\)-modules.

    \(D(R) = \mathrm{Ch}(R)[W^{-1}]\) is the localization of the category
    \(\mathrm{Ch}(R)\) of \(\mathbb{Z}\)-graded cochain complexes of
    \(R\)-modules at the class \(W\) of quasi-isomorphisms, the cochain maps
    \(f\) for which every \(H^n(f)\) is an isomorphism.  It comes with the
    localization functor \(Q : \mathrm{Ch}(R) \to D(R)\), which is the
    identity on objects, sends every quasi-isomorphism to an isomorphism,
    and is initial among functors out of \(\mathrm{Ch}(R)\) with that
    property.  Mathlib states this as ``DerivedCategory C`` with
    ``DerivedCategory.Q : CochainComplex C ℤ ⥤ DerivedCategory C`` and the
    instance ``Q.IsLocalization`` for the quasi-isomorphisms
    (``Mathlib/Algebra/Homology/DerivedCategory/Basic.lean``).

    The cohomology functors \(H^n : \mathrm{Ch}(R) \to \mathrm{Mod}_R\)
    invert quasi-isomorphisms, so each factors uniquely as
    \(H^n = H^n_D \circ Q\).

    ``super_categories`` is not declared.  An object of \(D(R)\) is a
    cochain complex, but a morphism of \(D(R)\) is a roof
    \(X \xleftarrow{s} X' \to Y\) with \(s\) a quasi-isomorphism, not a
    cochain map, so \(D(R)\) is not a subcategory of
    ``CochainComplexes(R)``; and no category of triangulated \(R\)-linear
    categories is presented in this tree to receive it.  The category
    therefore refuses to construct until that placement is formalized.
    """

    def _repr_object_names(self):
        return f"objects of the derived category over {self.base_ring()}"

    def cohomology(self, degree):
        r"""``H^degree : D(R) -> Mod_R``, the factorization of cochain cohomology through ``Q``."""
        assert False, "cohomology on DerivedCategories: not implemented"

    class ParentMethods:
        def cohomology(self, degree):
            r"""``H^degree(K)`` of an object \(K\) of \(D(R)\), an object of ``Modules(R)``.

            It is \(H^{\mathrm{degree}}\) of any cochain complex representing
            \(K\); quasi-isomorphic representatives give isomorphic modules.
            """
            assert False, "cohomology on DerivedCategories: not implemented"

        def graded_cohomology(self):
            r"""\(\bigoplus_n H^n(K)\), an object of ``GradedModules(R)`` with \(H^n(K)\) in degree \(n\)."""
            assert False, "graded_cohomology on DerivedCategories: not implemented"


class _DerivedLocalizationFunctor(Functor):
    r"""``Q : Ch(R) -> D(R)``, the localization of cochain complexes at quasi-isomorphisms."""

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(
            CochainComplexes(self._base_ring),
            DerivedCategories(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, complex_):
        r"""A cochain complex \(C\) as an object \(Q(C)\) of \(D(R)\)."""
        assert False, "localization on CochainComplexes: not implemented"

    def _apply_morphism(self, morphism):
        r"""A cochain map \(f\) as the roof \(Q(f)\) with identity left leg."""
        assert False, "localization on CochainComplexes: not implemented"

    def _repr_(self):
        return f"Localization of cochain complexes over {self.base_ring()} at quasi-isomorphisms"


@cached_function
def _derived_localization_functor(base_ring) -> _DerivedLocalizationFunctor:
    return _DerivedLocalizationFunctor(base_ring)


__all__ = ["DerivedCategories"]
