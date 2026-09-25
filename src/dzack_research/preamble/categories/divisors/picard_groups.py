r"""Picard groups."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.divisors.class_groups import ClassGroups
from dzack_research.preamble.categories.divisors.divisor_groups import (
    _affine_line_over_rationals,
    _cokernel_in_category,
    _free_presentation,
    _integers,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    BiproductModules,
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
        return [Modules(_own_ring(SageZZ))]

    def _call_(self, scheme, principal_divisors):
        r"""\(\operatorname{CDiv}/\operatorname{im}(\rho)\) for the principal Cartier divisor morphism ``principal_divisors`` \(\rho\)."""
        return _cokernel_in_category(principal_divisors, self, picard_scheme=scheme)

    def free(self, scheme, generators):
        r"""The free abelian group on the set ``generators`` of line-bundle classes of ``scheme``, presented by \(0 \to \mathbb{Z}^{(S)}\).

        This is an explicit construction for a scheme whose Picard group is
        already known to be free on these classes; it does not assert or
        decide that theorem.
        """
        return self(scheme, _free_presentation(generators))

    def trivial(self, scheme):
        r"""The zero Picard group of ``scheme``, the free group on no classes."""
        return self.free(scheme, finite_ordered_set(()))

    def projective_bundle(self, projective_space, base_picard_group):
        r"""\(\operatorname{Pic}(\mathbb{P}^n_S) = \operatorname{Pic}(S) \oplus \mathbb{Z}[\mathcal{O}(1)]\).

        The base Picard group is required input.  In particular this
        construction never replaces it by zero merely because the total
        space is projective.  The result is the biproduct itself, placed here
        with ``projective_space`` as its scheme.
        """
        assert base_picard_group in self, (
            f"cannot apply Pic(P^n_S) = Pic(S) + Z[O(1)] to {base_picard_group}: the second "
            f"argument must be the Picard group Pic(S) of the base, but it is not a Picard group"
        )
        assert base_picard_group.picard_scheme() is projective_space.base_scheme(), (
            f"cannot apply Pic(P^n_S) = Pic(S) + Z[O(1)] to {projective_space}: the given "
            f"Picard group is Pic({base_picard_group.picard_scheme()}), not the Picard group "
            f"of the base {projective_space.base_scheme()}"
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
            f"cannot induce Pic({scheme}) -> Cl({scheme}): the principal Cartier divisors "
            f"are indexed by {principal}, but the principal Weil divisors by "
            f"{principal_to_weil.domain()}; both must come from the same group of rational functions"
        )
        cartier = principal_to_cartier.codomain()
        assert cartier_to_weil.domain() is cartier, (
            f"cannot induce Pic({scheme}) -> Cl({scheme}): the map from Cartier to Weil "
            f"divisors has domain {cartier_to_weil.domain()}, not the Cartier divisor group {cartier}"
        )
        assert cartier_to_weil.codomain() is principal_to_weil.codomain(), (
            f"cannot induce Pic({scheme}) -> Cl({scheme}): the map from Cartier to Weil "
            f"divisors has codomain {cartier_to_weil.codomain()}, not the Weil divisor group "
            f"{principal_to_weil.codomain()}"
        )
        assert all(
            cartier_to_weil(principal_to_cartier(principal.module_generator(label)))
            == principal_to_weil(principal.module_generator(label))
            for label in principal.module_generating_set()
        ), (
            f"cannot induce Pic({scheme}) -> Cl({scheme}): the Cartier-to-Weil map "
            f"{cartier_to_weil} does not send the Cartier divisor of each rational function "
            f"to its Weil divisor"
        )
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
            assert self in BiproductModules(_integers()), (
                f"{self} has no base summand Pic(S): it was not built as "
                f"Pic(P^n_S) = Pic(S) + Z[O(1)], so it is not a direct sum of a base Picard "
                f"group and the hyperplane class"
            )
            return self.biproduct_factor(0)

        def projective_hyperplane_factor(self):
            r"""The summand \(\mathbb{Z}[\mathcal{O}(1)]\) of the projective-bundle presentation."""
            assert self in BiproductModules(_integers()), (
                f"{self} has no hyperplane summand Z[O(1)]: it was not built as "
                f"Pic(P^n_S) = Pic(S) + Z[O(1)], so it is not a direct sum of a base Picard "
                f"group and the hyperplane class"
            )
            return self.biproduct_factor(1)

        def base_picard_inclusion(self):
            r"""The inclusion \(\operatorname{Pic}(S) \to \operatorname{Pic}(\mathbb{P}^n_S)\) of the base summand."""
            assert self in BiproductModules(_integers()), (
                f"{self} has no inclusion Pic(S) -> Pic(P^n_S): it was not built as "
                f"Pic(P^n_S) = Pic(S) + Z[O(1)], so it is not a direct sum of a base Picard "
                f"group and the hyperplane class"
            )
            return self.injection(0)

        def hyperplane_class(self):
            r"""The class \([\mathcal{O}(1)]\) of the hyperplane summand."""
            factor = self.projective_hyperplane_factor()
            label = factor.module_generating_set()[0]
            return self.injection(1)(factor.module_generator(label))


__all__ = ["PicardGroups"]
