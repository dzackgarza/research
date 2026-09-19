r"""Morphisms of associative ``R``-algebras: linear and multiplicative.

Sited apart from the categories so that the module tree can name this Hom.
``End_R(F)`` is where a Hom object first has to choose between the linear maps
and the multiplicative ones, and it lives below the algebras.
"""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)


class AssociativeAlgebraMorphism(ModuleMorphism):
    r"""An \(R\)-linear map with \(f(xy)=f(x)f(y)\).

    The morphisms of the associative refinement ``Algebras(R).Associative()``.  No unit is preserved,
    because a non-unital algebra has none; the unital condition belongs to
    :class:`AlgebraMorphism`, whose category states it.
    """

    def __init__(
        self,
        parent,
        images,
        *,
        elementwise=False,
        verify_multiplicativity=True,
    ) -> None:
        domain = parent.domain()
        codomain = parent.codomain()
        linear_hom = domain.module_category().Mor(domain, codomain)
        underlying = (
            linear_hom.elementwise(images)
            if elementwise
            else linear_hom(images)
        )
        self._underlying_linearity_premise = underlying
        super().__init__(
            parent,
            lambda element: underlying(element),
            elementwise=True,
        )
        if self.linearity_decision() is not True:
            raise ValueError("an algebra morphism requires an established underlying linear map")
        if verify_multiplicativity:
            self._verify_multiplicativity_on_the_domain_framing()

    def _elementwise_linearity_derivation(self):
        return self._underlying_linearity_premise.linearity_decision()

    def _verify_multiplicativity_on_the_domain_framing(self) -> None:
        r"""Decide \(f(xy)=f(x)f(y)\) on the domain's module framing.

        Both sides are \(R\)-bilinear in \((x,y)\) -- the product by the
        algebra axioms, \(f\) by linearity -- so agreement on pairs from a
        module generating set is agreement on all of \(A\times A\).  This is
        the same argument, on the same data, that decides the bracket for a
        Lie morphism, and the same absence is stated where a domain has no
        finite module framing to decide it on.
        """
        domain = self.domain()
        codomain = self.codomain()
        assert domain.is_framed_module(), (
            f"multiplicativity of a map out of {domain} is decided on a module "
            "generating set, and this one states none"
        )
        labels = domain.module_generating_set()
        assert labels.cardinality().is_finite(), (
            f"multiplicativity of a map out of {domain} is not decidable here: "
            "its module generating set is infinite"
        )
        for left in labels:
            source_left = domain.module_generator(left)
            for right in labels:
                source_right = domain.module_generator(right)
                assert self(source_left * source_right) == codomain(
                    self(source_left) * self(source_right)
                ), (
                    f"the stated map does not preserve the product of "
                    f"{left!r} and {right!r}"
                )


class AssociativeAlgebraHomset(CategoricalHomset):
    r"""``Hom_{R-AssAlg}(A, B)``, the linear maps preserving the product."""

    Element = AssociativeAlgebraMorphism

    def __call__(self, images):
        if self._already_parented_arrow(images):
            return images
        return self._element_constructor_(images)

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def _repr_(self):
        return f"Mor_AssAlg({self.domain()}, {self.codomain()})"


class AssociativeAlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The fixed-endpoint Hom categories of associative ``R``-algebras."""

    FixedCategoryClass = AssociativeAlgebraHomset


__all__ = [
    "AssociativeAlgebraHomCategoryConstruction",
    "AssociativeAlgebraHomset",
    "AssociativeAlgebraMorphism",
]
