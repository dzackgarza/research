r"""Picard groups."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
from dzack_research.preamble.categories.divisors.divisor_groups import (
    _affine_line_over_rationals,
    _cokernel_in_category,
    _integers,
    _zero_presentation,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    BiproductModules,
    FramedModules,
    Modules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category_bases import Category


class PicardGroups(Category):
    r"""Picard groups \(\operatorname{Pic}(X)\) with a chosen presentation.

    An object is a framed abelian group presenting the Picard group of one
    scheme \(X\).  Its underlying group is built by a module construction:
    \(\operatorname{coker}(\rho)\) of a principal Cartier divisor morphism
    \(\rho\colon P \to \operatorname{CDiv}\) (the entry), or the biproduct
    \(\operatorname{Pic}(S) \oplus \mathbb{Z}[\mathcal{O}(1)]\) of the projective
    bundle formula, whose injections are the base inclusion and the hyperplane
    class.  This level adds \(X\).
    """

    def an_object(self):
        r"""The zero Picard group of \(\mathbb{A}^1_{\mathbb{Q}}\)."""
        return self.trivial(_affine_line_over_rationals())

    @classmethod
    def _repr_object_names(cls):
        return "Picard groups"

    def super_categories(self):
        return [FramedModules(_own_ring(SageZZ))]

    def _call_(self, scheme, principal_divisors):
        r"""\(\operatorname{CDiv}/\operatorname{im}(\rho)\) for the principal Cartier divisor morphism ``principal_divisors`` \(\rho\)."""
        return _cokernel_in_category(principal_divisors, self, picard_scheme=scheme)

    def trivial(self, scheme):
        r"""The zero Picard group of ``scheme``.

        This is an explicit construction for a scheme whose Picard triviality
        is already known; it does not assert or decide that theorem.
        """
        return self(scheme, _zero_presentation())

    def projective_bundle(self, projective_space, base_picard_group):
        r"""\(\operatorname{Pic}(\mathbb{P}^n_S) = \operatorname{Pic}(S) \oplus \mathbb{Z}[\mathcal{O}(1)]\).

        The base Picard group is required input.  In particular this
        construction never replaces it by zero merely because the total
        space is projective.  The result is the biproduct itself, placed here
        with ``projective_space`` as its scheme.
        """
        assert base_picard_group in self, "the projective bundle formula starts from a Picard group"
        assert base_picard_group.picard_scheme() is projective_space.base_scheme(), (
            "the supplied Picard group is not attached to the projective base"
        )
        integers = _integers()
        hyperplane = integers.free_module(finite_ordered_set(("O(1)",)))
        return Modules(integers).biproduct(
            (base_picard_group, hyperplane),
            extra_categories=(self,),
            extra_construction_data={"picard_scheme": projective_space},
        )

    def picard_to_class_group_morphism(
        self,
        scheme,
        principal_to_cartier,
        principal_to_weil,
        cartier_to_weil,
    ):
        r"""\(\operatorname{Pic}(X) \to \operatorname{Cl}(X)\) induced by a Cartier-to-Weil morphism.

        The principal divisors \(\rho_C\colon P \to \operatorname{CDiv}\) and
        \(\rho_W\colon P \to \operatorname{Div}\) present
        \(\operatorname{Pic}(X) = \operatorname{coker}\rho_C\) and
        \(\operatorname{Cl}(X) = \operatorname{coker}\rho_W\).  A morphism
        \(c\colon \operatorname{CDiv} \to \operatorname{Div}\) with
        \(c \circ \rho_C = \rho_W\) sends \(\operatorname{im}\rho_C\) into
        \(\operatorname{im}\rho_W\) and so induces the returned morphism of
        cokernels.  Its domain and codomain are the two groups, and their
        ``cokernel_projection()`` are the Cartier and Weil class projections.
        """
        principal = principal_to_cartier.domain()
        assert principal_to_weil.domain() is principal, (
            "the Cartier and Weil principal-divisor morphisms have one source"
        )
        cartier = principal_to_cartier.codomain()
        assert cartier_to_weil.domain() is cartier, (
            "the Cartier-to-Weil morphism starts at the Cartier divisors"
        )
        assert cartier_to_weil.codomain() is principal_to_weil.codomain(), (
            "the Cartier-to-Weil morphism ends at the Weil divisors"
        )
        assert all(
            cartier_to_weil(principal_to_cartier(principal.module_generator(label)))
            == principal_to_weil(principal.module_generator(label))
            for label in principal.module_generating_set()
        ), "the principal/Cartier/Weil triangle does not commute"
        picard = self(scheme, principal_to_cartier)
        classes = ClassGroups()(scheme, principal_to_weil)
        weil_class_projection = classes.cokernel_projection()
        return picard.module_category().Mor(picard, classes)(
            {
                label: weil_class_projection(cartier_to_weil(cartier.module_generator(label)))
                for label in picard.module_generating_set()
            }
        )

    class ParentMethods:
        def __init__(self, picard_scheme, **rest) -> None:
            self._picard_scheme = picard_scheme
            super().__init__(**rest)

        def picard_scheme(self):
            r"""The scheme whose Picard group this presents."""
            return self._picard_scheme

        def projective_base_picard_group(self):
            r"""The summand \(\operatorname{Pic}(S)\) of \(\operatorname{Pic}(\mathbb{P}^n_S) = \operatorname{Pic}(S) \oplus \mathbb{Z}[\mathcal{O}(1)]\)."""
            assert self in BiproductModules(_integers()), _NOT_A_PROJECTIVE_BUNDLE
            return self.biproduct_factor(0)

        def projective_hyperplane_factor(self):
            r"""The summand \(\mathbb{Z}[\mathcal{O}(1)]\) of the projective-bundle presentation."""
            assert self in BiproductModules(_integers()), _NOT_A_PROJECTIVE_BUNDLE
            return self.biproduct_factor(1)

        def base_picard_inclusion(self):
            r"""The inclusion \(\operatorname{Pic}(S) \to \operatorname{Pic}(\mathbb{P}^n_S)\) of the base summand."""
            assert self in BiproductModules(_integers()), _NOT_A_PROJECTIVE_BUNDLE
            return self.injection(0)

        def hyperplane_class(self):
            r"""The class \([\mathcal{O}(1)]\) of the hyperplane summand."""
            factor = self.projective_hyperplane_factor()
            label = factor.module_generating_set()[0]
            return self.injection(1)(factor.module_generator(label))


_NOT_A_PROJECTIVE_BUNDLE = (
    "the projective-bundle presentation of a Picard group is the biproduct of the "
    "base Picard group with the hyperplane factor; this Picard group was not built "
    "by the projective bundle formula"
)


__all__ = ["PicardGroups"]
