r"""First-class functors: the runtime kernel of the category of categories.

Functors are morphisms between categories. Sage's ``Functor`` class carries
actions on objects and morphisms but no composition operator, and Sage has
no functor spaces (``Hom`` between categories falls back to a generic
id-equality homset in ``Objects()``; verified against the running Sage at
kernel authoring). This module is the runtime authority for that owned
surface: composition with identity absorption, the functor spaces
``Fun(C, D)``, the twist endofunctor, scalar extension, and natural
isomorphisms with checked components. Contracts live in the lexicon.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TYPE_CHECKING, cast

from sage.categories.homset import Homset as SageHomset

from .. import lexicon

if TYPE_CHECKING:
    from .categories import Lattices
    from .parents import SyntheticLattice


class Functor(lexicon.SageFunctor):
    r"""Runtime functor base: Sage's ``Functor`` plus the kernel surface.

    ``(G * F)(x) = G(F(x))``; composing with an identity returns the other
    operand itself. Faithfulness (injectivity on homsets) is a declared
    mathematical property per the opt-in-with-trust membership model; its
    ``Sets``-valued case is exactly concreteness.
    """

    _faithful: bool = False

    def is_faithful(self) -> bool:
        r"""Whether this functor is injective on homsets, by declaration."""
        return self._faithful

    def __mul__(self, first: lexicon.SageFunctor) -> Functor:
        return compose(self, first)


class IdentityFunctor(Functor):
    r"""The identity morphism of a category in the category of categories."""

    _faithful = True

    def __init__(self, category: lexicon.SageCategory) -> None:
        lexicon.SageFunctor.__init__(self, category, category)

    def _apply_functor(self, obj: object) -> object:
        return obj

    def _apply_functor_to_morphism(self, morphism: lexicon.SageMorphism) -> lexicon.SageMorphism:
        return morphism


def compose(second: lexicon.SageFunctor, first: lexicon.SageFunctor) -> Functor:
    r"""The composite ``second . first``, with exact boundary agreement.

    Identities are absorbed exactly (the other operand is returned itself),
    and composite chains are flattened, so associativity holds by
    construction: both bracketings of a triple produce the same flattened
    chain.
    """
    assert first.codomain() == second.domain(), f"composition requires matching boundary; found codomain {first.codomain()} composed into domain {second.domain()}"
    if isinstance(first, IdentityFunctor):
        return cast(Functor, second)
    if isinstance(second, IdentityFunctor):
        return cast(Functor, first)
    first_factors = first.factors() if isinstance(first, ComposedFunctor) else (first,)
    second_factors = second.factors() if isinstance(second, ComposedFunctor) else (second,)
    return ComposedFunctor(first_factors + second_factors)


class ComposedFunctor(Functor):
    r"""A flattened chain of composable functors, applied left to right."""

    def __init__(self, factors: tuple[lexicon.SageFunctor, ...]) -> None:
        assert len(factors) >= 2, f"a composite needs at least two factors; found {len(factors)}"
        for early, late in zip(factors, factors[1:]):
            assert early.codomain() == late.domain(), f"composition requires matching boundary; found codomain {early.codomain()} composed into domain {late.domain()}"
        self._factors = factors
        lexicon.SageFunctor.__init__(self, factors[0].domain(), factors[-1].codomain())

    def factors(self) -> tuple[lexicon.SageFunctor, ...]:
        r"""The flattened chain of factors, in application order."""
        return self._factors

    def is_faithful(self) -> bool:
        r"""A composite of faithful functors is faithful."""
        return all(isinstance(factor, Functor) and factor.is_faithful() for factor in self._factors)

    def _apply_functor(self, obj: object) -> object:
        result = obj
        for factor in self._factors:
            result = factor(result)
        return result

    def _apply_functor_to_morphism(self, morphism: lexicon.SageMorphism) -> lexicon.SageMorphism:
        result = morphism
        for factor in self._factors:
            result = factor(result)
        return result


class Cat(lexicon.SageCategory):
    r"""The (mostly synthetic) category of categories.

    Its objects are the category instances of the graph — the owned
    ``Category`` classes are Python machinery (presentations), their
    INSTANCES are the objects of ``Cat`` — its morphisms are functors,
    and its homsets are the functor spaces. Owned categories carry this
    objecthood through the STANDARD protocols: their ``category()`` is
    ``Cat()`` and Sage's own ``Hom(C, D)`` dispatches to ``Fun(C, D)``
    via ``_Hom_`` (Sage-native categories, whose ``category()`` Sage
    hard-wires to ``Objects()``, are admitted through the membership
    adapter below). ``Cat`` is an object of ``Objects()``, not of
    itself: its objects form a proper class."""

    def super_categories(self) -> list[lexicon.SageCategory]:
        from sage.categories.objects import Objects

        return [Objects()]

    def _repr_object_names(self) -> str:
        return "categories"

    def __contains__(self, x: object) -> bool:
        # The type test alone cannot express the proper-class exclusion:
        # ``Cat`` is itself a ``SageCategory`` instance, so bare isinstance
        # would make ``Cat`` an object of itself. An object of ``Cat`` is any
        # category EXCEPT ``Cat`` (no Russell-flavored self-membership).
        return isinstance(x, lexicon.SageCategory) and not isinstance(x, Cat)

    def homset(self, domain: lexicon.SageCategory, codomain: lexicon.SageCategory) -> FunctorSpace:
        r"""``Hom_Cat(C, D) = Fun(C, D)``. (Convenience spelling; owned
        categories also reach this through Sage's standard ``Hom``. The
        boundary-membership guard lives on ``FunctorSpace`` itself, the one
        constructor every route reaches.)"""
        return FunctorSpace(domain, codomain)


class CatObject:
    r"""Mixin declaring that a category class's instances are objects of
    ``Cat`` through the standard protocols: ``category()`` answers
    ``Cat()`` and ``Hom(C, D)`` dispatches to the functor space. Every
    owned category class mixes this in; the class itself stays what it
    is — Python machinery presenting the object."""

    def category(self) -> Cat:
        return Cat()

    def _Hom_(self, codomain: lexicon.SageCategory, category: object = None) -> FunctorSpace:
        return FunctorSpace(cast(lexicon.SageCategory, self), codomain)


class FunctorSpace(lexicon.SageUniqueRepresentation, SageHomset):
    r"""``Fun(C, D)``: the functors ``C -> D`` as a first-class parent.

    A homset of ``Cat``, the category of categories — and therefore a
    subclass of Sage's OWN ``Homset`` machinery, from which the boundary
    accessors (``domain``/``codomain``, which Sage's Hom cache revalidates
    through) and homset semantics are INHERITED, never re-spelled here.
    Unique per boundary pair, membership is exact boundary agreement, and
    the endofunctor space owns its identity. Existence and element handling
    are the contract; no enumeration is promised.
    """

    def __init__(self, domain: lexicon.SageCategory, codomain: lexicon.SageCategory) -> None:
        cat = Cat()
        assert domain in cat and codomain in cat, f"a functor space's boundary must be objects of Cat; found {domain!r} and {codomain!r}"
        self._domain_category = domain
        self._codomain_category = codomain
        SageHomset.__init__(self, domain, codomain, category=cat, check=False)

    def _repr_(self) -> str:
        return f"Fun({self._domain_category}, {self._codomain_category})"

    def __contains__(self, functor: object) -> bool:
        return isinstance(functor, lexicon.SageFunctor) and functor.domain() == self._domain_category and functor.codomain() == self._codomain_category

    def identity(self) -> IdentityFunctor:
        assert self._domain_category == self._codomain_category, f"only an endofunctor space has an identity; found Fun({self._domain_category}, {self._codomain_category})"
        return IdentityFunctor(self._domain_category)


class NaturalIsomorphism(lexicon.NaturalIsomorphism):
    r"""A natural isomorphism between parallel functors, given as its
    component family.

    Components are isomorphisms ``eta_X: F(X) -> G(X)`` produced by a
    callable on objects; naturality squares ``G(f) . eta_X == eta_Y . F(f)``
    are checked on demand against real morphisms. No universal bijectivity
    decision procedure is required: inverse components are declared, per
    the declared-isomorphism discipline.
    """

    def __init__(
        self,
        source: lexicon.SageFunctor,
        target: lexicon.SageFunctor,
        components: Callable[..., lexicon.CategoryMorphism],
        inverse_components: Callable[..., lexicon.CategoryMorphism],
    ) -> None:
        parallel = source.domain() == target.domain() and source.codomain() == target.codomain()
        assert parallel, f"natural transformations require parallel functors; found {source.domain()} -> {source.codomain()} and {target.domain()} -> {target.codomain()}"
        assert inverse_components is not None, (
            "a natural isomorphism declares its inverse components at construction; a component family with no declared inverse is a natural transformation, not an isomorphism"
        )
        self._source = source
        self._target = target
        self._components = components
        self._inverse_components = inverse_components

    def component(self, obj: object) -> lexicon.CategoryMorphism:
        morphism = self._components(obj)
        assert morphism.domain() == self._source(obj), f"component at {obj} must start at the source image; found {morphism.domain()}"
        assert morphism.codomain() == self._target(obj), f"component at {obj} must land in the target image; found {morphism.codomain()}"
        return morphism

    def check_naturality_on(self, morphisms: Iterable[lexicon.CategoryMorphism]) -> bool:
        r"""Assert every naturality square against the given real morphisms."""
        for morphism in morphisms:
            left = self._target(morphism) * self.component(morphism.domain())
            right = self.component(morphism.codomain()) * self._source(morphism)
            assert left == right, f"naturality square fails on {morphism}"
        return True

    def inverse(self) -> NaturalIsomorphism:
        return NaturalIsomorphism(self._target, self._source, self._inverse_components, self._components)


class TwistFunctor(lexicon.TwistFunctor, Functor):
    r"""The twist endofunctor ``L -> L(a)`` of a lattice root.

    The bilinear form is scaled by a fixed nonzero scalar; the underlying
    module and every morphism matrix are unchanged (Nikulin's ``L(a)``).
    An isometry of ``L`` is therefore an isometry of ``L(a)``, so the twist
    is faithful.
    """

    _faithful = True

    def __init__(self, category: Lattices, scalar: lexicon.ExactScalar | int) -> None:
        assert scalar != 0, "the twist scalar must be nonzero: L(0) is not a lattice twist"
        self._scalar = scalar
        lexicon.SageFunctor.__init__(self, category, category)

    def domain(self) -> Lattices:
        r"""The lattice root this endofunctor twists."""
        return cast("Lattices", lexicon.SageFunctor.domain(self))

    def codomain(self) -> Lattices:
        r"""The same lattice root: a twist does not change the base ring."""
        return cast("Lattices", lexicon.SageFunctor.codomain(self))

    def scalar(self) -> lexicon.ExactScalar | int:
        r"""The fixed scalar the form is multiplied by."""
        return self._scalar

    def _apply_functor(self, lattice: lexicon.Lattice) -> lexicon.Lattice:
        return lattice.twist(self._scalar)

    def _apply_functor_to_morphism(self, morphism: lexicon.LatticeMorphism) -> lexicon.LatticeMorphism:
        category = self.codomain()
        domain = self._apply_functor(cast("SyntheticLattice", morphism.domain()))
        codomain = self._apply_functor(cast("SyntheticLattice", morphism.codomain()))
        return category.morphism(domain, morphism.matrix(), codomain=codomain)


class LatticeBaseChangeFunctor(lexicon.LatticeBaseChangeFunctor, Functor):
    r"""Scalar extension along a canonical map of supported base rings.

    The source category owns the functor. Its object action enters the target
    category through ``from_base_change`` so the target classifies the result
    from its own data; its morphism action constructs through the target's
    homset root. A lattice morphism is determined by its matrix, which scalar
    extension preserves, so the functor is faithful.
    """

    _faithful = True

    def __init__(self, domain: Lattices, codomain: Lattices) -> None:
        assert codomain.base_ring().coerce_map_from(domain.base_ring()) is not None, f"base change requires a canonical map {domain.base_ring()} -> {codomain.base_ring()}"
        lexicon.SageFunctor.__init__(self, domain, codomain)

    def domain(self) -> Lattices:
        r"""The source lattice category of this scalar-extension functor."""
        return cast("Lattices", lexicon.SageFunctor.domain(self))

    def codomain(self) -> Lattices:
        r"""The target lattice category of this scalar-extension functor."""
        return cast("Lattices", lexicon.SageFunctor.codomain(self))

    def source_base_ring(self) -> lexicon.BaseRing:
        return cast(lexicon.BaseRing, self.domain().base_ring())

    def target_base_ring(self) -> lexicon.BaseRing:
        return cast(lexicon.BaseRing, self.codomain().base_ring())

    def _apply_functor(self, lattice: lexicon.Lattice) -> lexicon.Lattice:
        target = self.codomain()
        return target.from_base_change(lattice)

    def _apply_functor_to_morphism(self, morphism: lexicon.LatticeMorphism) -> lexicon.LatticeMorphism:
        assert isinstance(morphism, lexicon.LatticeMorphism), f"base change acts on lattice morphisms; found={type(morphism)}"
        target = self.codomain()
        domain = self._apply_functor(morphism.domain())
        codomain = self._apply_functor(morphism.codomain())
        return target.morphism(domain, morphism.matrix(), codomain=codomain)
