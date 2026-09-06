"""Owned Lie-algebra categories."""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _proper_restriction_base_ring,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules


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
        assert domain.is_framed(), (
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


class LieAlgebras(OwnedCategoryOverBaseRing):
    r"""Lie algebras over a commutative owned base ring."""

    def an_object(self):
        r"""``End_R(Free_R([2]))`` with the commutator bracket."""
        from dzack_research.preamble.categories.algebras.algebras import MatrixAlgebras

        return MatrixAlgebras(self.base_ring()).an_object()

    @classmethod
    def _repr_object_names(cls):
        return "Lie algebras"

    def super_categories(self):
        ring = self.base_ring()
        if ring not in OwnedRings().Commutative():
            raise TypeError("a Lie algebra here is over a commutative base ring")

        # A Lie algebra over R is one over any ring R restricts to, exactly as
        # an associative algebra is, so the two towers have the same shape.
        base = _proper_restriction_base_ring(ring)
        if base is not None:
            return [Modules(ring), LieAlgebras(base)]
        return [Modules(ring)]

    # Without this the Hom family walks up to the one Modules declares and
    # reuses it, which is what a *full* subcategory of modules would want.
    # Lie algebras are not one: their morphisms are the linear maps that
    # respect the bracket.
    _HomCategory = LieAlgebraHomCategoryConstruction

    class ParentMethods:
        def bracket(self, left, right):
            return self(left).bracket(self(right))


class CommutatorLieAlgebras(LieAlgebras):
    r"""Associative algebras read as Lie algebras under \([x,y]=xy-yx\).

    The bracket is stated by
    :class:`~dzack_research.preamble.categories.algebras.algebras.AssociativeAlgebras`,
    which owns the product it is built from; this category adds the Lie
    structure that product determines.  The passage is named by
    ``AssociativeAlgebras(R).commutator_lie_algebra()``.

    Membership is a fact about every associative algebra over a commutative
    ring, and ``AssociativeAlgebras`` states it once for all of them.  This
    category does not name the associative algebras in turn: knowing that a
    bracket is a commutator does not hand back the product it came from, since
    many associative products share one commutator.  The passage in that
    direction is the functor, not an edge.
    """

    @classmethod
    def _repr_object_names(cls):
        return "commutator Lie algebras"

    def super_categories(self):
        ring = self.base_ring()
        base = _proper_restriction_base_ring(ring)
        if base is not None:
            return [LieAlgebras(ring), CommutatorLieAlgebras(base)]
        return [LieAlgebras(ring)]


def lie_algebra_homset(domain, codomain) -> LieAlgebraHomset:
    r"""``Hom_{R-Lie}(domain, codomain)`` for ``R`` the base of ``domain``.

    The session spelling, as ``algebra_homset`` is for algebras.  A
    subcategory of Lie algebras that states no morphisms of its own reaches
    this same object when asked, so which category is asked does not change
    the answer.
    """
    return LieAlgebras(domain.base_ring()).Mor(domain, codomain)


__all__ = [
    "CommutatorLieAlgebras",
    "LieAlgebraHomset",
    "LieAlgebraMorphism",
    "LieAlgebras",
    "lie_algebra_homset",
]
