r"""Weil divisor class groups."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.divisors.divisor_groups import (
    _affine_line_over_integers,
    _cokernel_in_category,
    _integers,
    _zero_presentation,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    Modules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category_bases import Category


class ClassGroups(Category):
    r"""Weil divisor class groups \(\operatorname{Cl}(X)\) with a chosen presentation.

    An object is a framed abelian group presenting the divisor class group of
    one scheme \(X\).  Its underlying group is built by a module construction:
    \(\operatorname{coker}(\rho)\) of a principal-divisor morphism
    \(\rho\colon P \to \operatorname{Div}\) (the entry), or the biproduct
    \(\operatorname{Cl}(S) \oplus \mathbb{Z}[H]\) of the projective bundle
    formula.  This level adds \(X\).
    """

    def an_object(self):
        r"""The zero class group of \(\mathbb{A}^1_{\mathbb{Z}}\)."""
        return self.trivial(_affine_line_over_integers())

    @classmethod
    def _repr_object_names(cls):
        return "class groups"

    def super_categories(self):
        return [FramedModules(_own_ring(SageZZ))]

    def _call_(self, scheme, principal_divisors):
        r"""\(\operatorname{Div}/\operatorname{im}(\rho)\) for the principal-divisor morphism ``principal_divisors`` \(\rho\)."""
        return _cokernel_in_category(principal_divisors, self, class_group_scheme=scheme)

    def trivial(self, scheme):
        r"""The zero class group of ``scheme``.

        This is an explicit construction for a scheme whose class group is
        already known to vanish; it does not assert or decide that theorem.
        """
        return self(scheme, _zero_presentation())

    def projective_bundle(self, projective_space, base_class_group):
        r"""\(\operatorname{Cl}(\mathbb{P}^n_S) = \operatorname{Cl}(S) \oplus \mathbb{Z}[H]\).

        The base class group is required input, so a nontrivial base
        contribution is never replaced by zero.  The result is the biproduct
        itself, placed here with ``projective_space`` as its scheme; its
        injections are the pullback of base classes and the hyperplane class.
        """
        assert base_class_group in self, "the projective bundle formula starts from a class group"
        assert base_class_group.class_group_scheme() is projective_space.base_scheme(), (
            "the supplied class group is not attached to the projective base"
        )
        integers = _integers()
        hyperplane = integers.free_module(finite_ordered_set(("H",)))
        return Modules(integers).biproduct(
            (base_class_group, hyperplane),
            extra_categories=(self,),
            extra_construction_data={"class_group_scheme": projective_space},
        )

    class ParentMethods:
        def __init__(self, class_group_scheme, **rest) -> None:
            self._class_group_scheme = class_group_scheme
            super().__init__(**rest)

        def class_group_scheme(self):
            r"""The scheme whose divisor classes this group presents."""
            return self._class_group_scheme


__all__ = ["ClassGroups"]
