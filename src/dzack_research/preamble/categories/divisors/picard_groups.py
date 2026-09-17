"""Picard groups."""

from dzack_research.preamble.categories.divisors.divisor_groups import (
    _integers,
    _module_in_role,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    BiproductModules,
    FramedModules,
    Modules,
)
from dzack_research.preamble.categories.schemes.schemes import Schemes
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category_bases import Category


class PicardGroups(Category):
    r"""Picard groups \(\operatorname{Pic}(X)\) with a chosen framed presentation.

    An object is a framed \(\mathbb{Z}\)-module presenting the Picard group
    of one scheme \(X\), its datum.  The projective-bundle presentation
    \(\operatorname{Pic}(\mathbb{P}^n_S) = \operatorname{Pic}(S) \oplus
    \mathbb{Z}[\mathcal{O}(1)]\) is the chosen biproduct of the base Picard
    group with the hyperplane factor, built as a biproduct placed in this
    category (:meth:`projective_bundle`), so its base inclusion and
    hyperplane class are the biproduct's own injections.
    """

    def an_object(self):
        r"""The trivial Picard group of the affine line."""
        return self.trivial(Schemes(_integers()).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "Picard groups"

    def super_categories(self):
        return [FramedModules(_integers())]

    def trivial(self, scheme):
        r"""Return the represented zero Picard group for ``scheme``.

        This is an explicit construction for a scheme whose Picard triviality
        is already known; it does not assert or decide that theorem.
        """
        return self(_integers().free_module(finite_ordered_set(())), scheme=scheme)

    def projective_bundle(self, projective_space, base_picard_group):
        r"""\(\operatorname{Pic}(\mathbb{P}^n_S) = \operatorname{Pic}(S) \oplus \mathbb{Z}[\mathcal{O}(1)]\).

        The base Picard group is required input.  In particular this
        construction never replaces it by zero merely because the total
        space is projective.  The result is the biproduct itself, placed here
        with ``projective_space`` as its scheme.
        """
        integers = _integers()
        assert base_picard_group in self, "the projective bundle formula starts from a Picard group"
        assert base_picard_group.picard_scheme() is projective_space.base_scheme(), (
            "the supplied Picard group is not attached to the projective base"
        )
        hyperplane = integers.free_module(finite_ordered_set(("O(1)",)))
        return Modules(integers).biproduct(
            (base_picard_group, hyperplane),
            extra_categories=(self,),
            extra_construction_data={"picard_scheme": projective_space},
        )

    def _call_(self, module, scheme):
        assert module in FramedModules(_integers()), (
            "a Picard group is presented on a framed abelian group"
        )
        return _module_in_role(module, self, picard_scheme=scheme)

    class ParentMethods:
        def __init__(self, picard_scheme, **rest) -> None:
            self._picard_scheme = picard_scheme
            super().__init__(**rest)

        def picard_scheme(self):
            r"""The scheme whose Picard group this presents."""
            return self._picard_scheme

        def projective_picard_biproduct(self):
            r"""This group as the chosen biproduct \(\operatorname{Pic}(S) \oplus \mathbb{Z}[\mathcal{O}(1)]\)."""
            assert self in BiproductModules(_integers()), (
                "the projective-bundle presentation of a Picard group is the chosen "
                "biproduct of the base Picard group with the hyperplane factor; this "
                "Picard group was not built by the projective bundle formula"
            )
            return self

        def projective_base_picard_group(self):
            return self.projective_picard_biproduct().biproduct_factor(0)

        def projective_hyperplane_factor(self):
            return self.projective_picard_biproduct().biproduct_factor(1)

        def base_picard_inclusion(self):
            r"""The inclusion \(\operatorname{Pic}(S) \to \operatorname{Pic}(\mathbb{P}^n_S)\) of the base summand."""
            return self.projective_picard_biproduct().injection(0)

        def hyperplane_class(self):
            r"""The class \([\mathcal{O}(1)]\) of the hyperplane summand."""
            factor = self.projective_hyperplane_factor()
            label = factor.module_generating_set()[0]
            return self.projective_picard_biproduct().injection(1)(factor.module_generator(label))
