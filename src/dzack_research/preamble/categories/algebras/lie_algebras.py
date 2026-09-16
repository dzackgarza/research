"""Owned Lie-algebra categories."""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)


class LieAlgebraMorphism(ModuleMorphism):
    r"""An \(R\)-linear map with \(f([x,y])=[f(x),f(y)]\).

    A Lie morphism is a module morphism that additionally respects the
    bracket, so it is constructed as one and the condition is checked on top.
    Every linear-map question -- matrix, kernel, cokernel, composition -- is
    then answered by the module level rather than restated here.
    """

    def __init__(
        self,
        parent,
        images,
        *,
        elementwise=False,
        verify_linearity=True,
        verify_bracket=True,
    ) -> None:
        super().__init__(
            parent,
            images,
            elementwise=elementwise,
            verify_linearity=verify_linearity,
        )
        if verify_bracket:
            self._verify_bracket_on_the_domain_framing()

    def _verify_bracket_on_the_domain_framing(self) -> None:
        r"""Decide \(f([x,y])=[f(x),f(y)]\) on the domain's module framing.

        Both sides are \(R\)-bilinear in \((x,y)\): the bracket is bilinear by
        the Lie axioms and \(f\) is linear.  Two bilinear maps that agree on
        pairs from a module generating set agree on all of \(L\times L\), so
        this decides the condition rather than sampling it.

        It is the *module* generating set that decides, not an algebra
        generating set: \(f\) is linear and not multiplicative, so the images
        of algebra generators do not determine it.  A polynomial ring read
        under its commutator states no module framing at all, and the
        underlying module of a free algebra states an infinite one; neither
        has a decision procedure here, and each is told so rather than
        guessed at.  Ranging over the algebra is not the alternative, and is
        not what the finite case does either.
        """
        domain = self.domain()
        codomain = self.codomain()
        assert domain.is_framed_module(), (
            f"the bracket condition on a map out of {domain} is decided on a "
            "module generating set, and this one states none"
        )
        labels = domain.module_generating_set()
        assert labels.cardinality().is_finite(), (
            f"the bracket condition on a map out of {domain} is not decidable "
            "here: its module generating set is infinite, and the images of "
            "algebra generators do not determine a linear map"
        )
        for left in labels:
            source_left = domain.module_generator(left)
            for right in labels:
                source_right = domain.module_generator(right)
                assert self(domain.bracket(source_left, source_right)) == codomain.bracket(
                    self(source_left),
                    self(source_right),
                ), (
                    f"the stated map does not preserve the bracket of "
                    f"{left!r} and {right!r}"
                )


class LieAlgebraHomset(CategoricalHomset):
    r"""``Hom_{R-Lie}(L, L')``, the bracket-preserving linear maps."""

    Element = LieAlgebraMorphism

    def __call__(self, images):
        return self._element_constructor_(images)

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def _repr_(self):
        return f"Mor_Lie({self.domain()}, {self.codomain()})"


class LieAlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The fixed-endpoint Hom categories of Lie algebras over ``R``."""

    FixedCategoryClass = LieAlgebraHomset


LieAlgebras = Algebras.Lie


class CommutatorLieAlgebras(OwnedCategoryOverBaseRing):
    r"""Associative algebras read as Lie algebras under \([x,y]=xy-yx\).

    The bracket is stated by
    associative refinement ``Algebras(R).Associative()``,
    which owns the product it is built from; this category adds the Lie
    structure that product determines.  The passage is named by
    ``Algebras(R).Associative().commutator_lie_algebra()``.

    Membership is a fact about every associative algebra over a commutative
    ring, and the associative refinement states it once for all of them.  This
    category does not name the associative algebras in turn: knowing that a
    bracket is a commutator does not hand back the product it came from, since
    many associative products share one commutator.  The passage in that
    direction is the functor, not an edge.
    """

    def an_object(self):
        r"""``gl_2(R)``, the commutator Lie algebra of the two-by-two matrices."""
        return Algebras(self.base_ring()).Lie().an_object()

    @classmethod
    def _repr_object_names(cls):
        return "commutator Lie algebras"

    def super_categories(self):
        return [Algebras(self.base_ring()).Lie()]


__all__ = [
    "CommutatorLieAlgebras",
    "LieAlgebraHomset",
    "LieAlgebraMorphism",
    "LieAlgebras",
]
