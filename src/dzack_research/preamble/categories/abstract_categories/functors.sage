r"""The morphisms of \(\mathbf{Cat}\): the owned functor base and the
functor spaces \(\operatorname{Fun}(C,D)\).

Functors are the morphisms of \(\mathbf{Cat}\), and morphisms compose.
Sage's ``Functor`` carries actions on objects and morphisms but no
composition operator, and Sage's ``Hom`` between two categories falls back
to a generic id-equality homset.  This module owns both surfaces:

- :class:`Functor`, the base every preamble functor derives from: an
  ``Element`` of its functor space, plus composition (``G * F``, with
  identity absorption and chain flattening, so associativity holds on the
  nose) and faithfulness as a *declared* property.  Injectivity on homsets
  is not decidable in general, so faithfulness is declaration-by-placement
  — ``_faithful`` on the class — propagated through composites by the
  theorem that a composite of faithful functors is faithful.  No runtime
  injectivity check exists or lands.
- :class:`FunctorHomsets`, whose objects are the
  \(\operatorname{Hom}_{\mathbf{Cat}}(C,D)\) as first-class parents (method-placement
  doctrine puts existence questions on homsets).  ``cat.sage`` dispatches
  ``Hom(C, D)`` between categories here.

**The shape, which is the general one.**  A morphism of \(C\) is an element
of \(\operatorname{Hom}_C(A,B)\), and that homset is a parent: the homset is
a ``Parent``, the morphism is an ``Element`` of it, and the boundary is read
off the homset rather than stored on the morphism.  This module is that shape
with \(C=\mathbf{Cat}\).  Which Sage base a given arrow category takes is
settled by one question — **are the objects of \(C\) Sage parents?**  Where
they are, ``Morphism``/``Map`` is right and hands you composition for free.
Where they are not, as here, ``Map`` is closed off (it types the boundary as
``cdef Parent``) and ``Element`` is the base.

That is also why composition is written out below rather than inherited:
``Map._composition_`` exists, ``Element._composition_`` does not.  The
hand-written ``compose_functors`` is not a reimplementation of something
available — it is what remains once the platform's version is structurally
out of reach.  Do not "restore" it to ``Map``.

``Hom(C, D)`` reaches this module when the **domain** is an owned category,
parent or not: ``_Hom_`` arrives through ``subcategory_class``, the same
route the \(\mathbf{Cat}\) constructions take.  A Sage-native domain has no
such method and gets Sage's generic homset — measured, including the
asymmetry: ``Hom(OwnedRings().core(), CommutativeRings())`` is a functor
space, ``Hom(Groups(), Sets())`` is not.
"""

from typing import TYPE_CHECKING

from sage.categories.morphism import Morphism as SageMorphism
from sage.misc.cachefunc import cached_function
from sage.structure.element import Element as SageElement
from sage.categories.objects import Objects

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.owned_category_bases import Category as OwnedCategory
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryOf,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from dzack_research.preamble.owned_category import ConstructionData
    from sage.categories.category import Category
    from sage.categories.morphism import Morphism
    from sage.structure.parent import Parent


class Functor(SageElement):
    r"""The owned functor base: a **morphism of** \(\mathbf{Cat}\).

    A functor is a morphism of \(\mathbf{Cat}\), and a morphism is an element
    of its homset, so a functor's ``parent()`` is
    \(\operatorname{Hom}_{\mathbf{Cat}}(C,D)=\) :class:`FunctorHomset`.

    Two Sage classes are deliberately *not* bases here, each for a measured
    reason.

    Sage's ``Functor`` cannot be one: it is a Cython extension type that
    conflicts with ``Morphism``, with ``Map`` and even with bare ``Element``
    (``TypeError: multiple bases have instance lay-out conflict``), so a
    ``SageFunctor`` cannot have a parent at all.  Sage having a notion of
    functor that is not a morphism is exactly the non-uniformity this layer
    exists to remove, so the mathematics stays and the obstacle is fixed where
    it occurs.

    Sage's ``Morphism`` cannot be one either, and this is the sharper point.
    ``Map.__init__`` assigns the boundary into ``cdef Parent`` slots, so
    ``Morphism`` requires a morphism's **domain and codomain to be parents**.
    A functor's boundary is two *categories*, and while an owned category is a
    parent under the Cat model, a Sage-native one such as ``CommutativeRings()``
    or ``Groups()`` never is and never should be -- the preamble does not
    reshape Sage's categories.  Deriving from ``Morphism`` therefore fails at
    construction for every functor with a Sage-native boundary
    (``TypeError: Cannot convert Cardinalities_with_category to Parent``).

    ``Element`` carries exactly what the mathematics asks and nothing that
    fights it: a parent, which is the homset.  Being a morphism of
    \(\mathbf{Cat}\) *is* being an element of \(\operatorname{Hom}_{\mathbf
    {Cat}}(C,D)\); Sage's ``Morphism`` is a narrower thing -- a morphism
    between parents -- and this is not one.  The boundary accessors come from
    the homset, where they belong.

    ``(G * F)(x) = G(F(x))``; composing with an identity returns the other
    operand itself.  Faithfulness is a declared mathematical property; its
    ``Sets``-valued case is exactly concreteness.
    """

    _faithful: bool = False

    def __init__(self, domain: "Category", codomain: "Category") -> None:
        SageElement.__init__(self, domain.FunctorCategory(codomain))

    def domain(self) -> "Category":
        r"""The source category, read off the homset this functor lives in."""
        return self.parent().domain()

    def codomain(self) -> "Category":
        r"""The target category, read off the homset this functor lives in."""
        return self.parent().codomain()

    def __call__(self, x: "Parent | Morphism") -> "Parent | Morphism":
        r"""Apply this functor to an object or a morphism of its domain.

        Reproduces ``Functor.__call__`` in ``sage/categories/functor.pyx``:
        dispatch on object-versus-morphism, check the argument lies in the
        domain, apply, and check the result lands in the codomain.  It is
        reproduced rather than inherited because ``SageFunctor`` cannot be a
        base here (see the class docstring), and it is *overridden* rather than
        left to ``Map.__call__`` because that coerces its argument into
        ``self.domain()`` -- correct when a domain is a parent and the argument
        is one of its elements, wrong here, where the domain is a category and
        the argument is one of its objects.
        """
        if x in self.domain().ArrowCategory():
            image = self._apply_functor_to_morphism(x)
            assert image in self.codomain().ArrowCategory(), (
                f"{self} sends {x} outside the arrows of {self.codomain()}"
            )
            return image
        assert x in self.domain(), (
            f"{x} is not an object of {self.domain()}, the domain of {self}"
        )
        image = self._apply_functor(x)
        assert image in self.codomain(), (
            f"{self} is ill-defined: it sends {x} outside {self.codomain()}"
        )
        return image

    def is_faithful(self) -> bool:
        r"""Whether this functor is injective on homsets, by declaration."""
        return self._faithful

    def _repr_(self) -> str:
        r"""The boundary, as Sage's ``Functor`` printed it.

        Restored here because ``Element``'s default -- "Generic element of a
        structure" -- says nothing about a functor, and a functor that does not
        name its own boundary is unreadable at a prompt.
        """
        return f"Functor from {self.domain()} to {self.codomain()}"

    def __mul__(self, first: "Functor") -> "Functor":
        return compose_functors(self, first)


class IdentityFunctor(Functor):
    r"""The identity morphism of a category in \(\mathbf{Cat}\)."""

    _faithful = True

    def __init__(self, category: "Category") -> None:
        Functor.__init__(self, category, category)

    def _apply_functor(self, obj: "Parent") -> "Parent":
        return obj

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        return morphism

    def _repr_(self) -> str:
        return f"Identity functor of {self.domain()}"


def compose_functors(second: "Functor", first: "Functor") -> "Functor":
    r"""The composite ``second . first``, with exact boundary agreement.

    Identities are absorbed exactly (the other operand is returned itself)
    and composite chains are flattened, so associativity holds by
    construction: both bracketings of a triple produce the same flattened
    chain.
    """
    assert first.codomain() == second.domain(), (
        f"composition requires matching boundary; found codomain "
        f"{first.codomain()} composed into domain {second.domain()}"
    )
    if isinstance(first, IdentityFunctor):
        composite: Functor = second
        return composite
    if isinstance(second, IdentityFunctor):
        composite = first
        return composite
    first_factors = first.factors() if isinstance(first, ComposedFunctor) else (first,)
    second_factors = second.factors() if isinstance(second, ComposedFunctor) else (second,)
    return ComposedFunctor(first_factors + second_factors)


class ComposedFunctor(Functor):
    r"""A flattened chain of composable functors, applied left to right."""

    def __init__(self, factors: tuple["Functor", ...]) -> None:
        assert len(factors) >= 2, (
            f"a composite needs at least two factors; found {len(factors)}"
        )
        for early, late in zip(factors, factors[1:]):
            assert early.codomain() == late.domain(), (
                f"composition requires matching boundary; found codomain "
                f"{early.codomain()} composed into domain {late.domain()}"
            )
        self._factors = factors
        Functor.__init__(self, factors[0].domain(), factors[-1].codomain())

    def factors(self) -> tuple["Functor", ...]:
        r"""The flattened chain of factors, in application order."""
        return self._factors

    def is_faithful(self) -> bool:
        r"""A composite of faithful functors is faithful."""
        return all(
            isinstance(factor, Functor) and factor.is_faithful()
            for factor in self._factors
        )

    def _apply_functor(self, obj: "Parent") -> "Parent":
        result = obj
        for factor in self._factors:
            result = factor(result)
        return result

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        result = morphism
        for factor in self._factors:
            result = factor(result)
        return result

    def _repr_(self) -> str:
        return " . ".join(str(factor) for factor in reversed(self._factors))


class FunctorCategory(OwnedCategory):
    r"""The category \([C,D]\) of functors and natural transformations."""

    ElementType = Functor

    def __init__(self, domain: "Category", codomain: "Category") -> None:
        self._domain = domain
        self._codomain = codomain
        super().__init__()

    def domain(self) -> "Category":
        return self._domain

    def codomain(self) -> "Category":
        return self._codomain

    def _repr_(self) -> str:
        return f"Functor category [{self._domain}, {self._codomain}]"

    def super_categories(self) -> list["Category"]:
        return [Objects()]

    def __contains__(self, candidate: "Functor") -> bool:
        return (
            candidate.parent() is self
            and candidate.domain() == self._domain
            and candidate.codomain() == self._codomain
        )

    class _HomCategory(HomCategoryOf):
        r"""Category-valued hom objects of a functor category."""

        @property
        def ObjectType(self) -> type:
            return NaturalTransformationCategory

        def Of(
            self,
            source: "Functor",
            target: "Functor",
        ) -> "NaturalTransformationCategory":
            assert source in self.base_category()
            assert target in self.base_category()
            return NaturalTransformations(source, target)

        def _object(
            self,
            source: "Functor",
            target: "Functor",
            placement: "Category",
        ) -> "NaturalTransformationCategory":
            return NaturalTransformations(source, target)


class NaturalTransformation(SageElement):
    r"""A natural transformation, given by its component morphisms.

    Naturality is declared structure.  The general categorical layer does
    not decide equality between the two composites in every naturality square.
    """

    def __init__(self, parent: "Parent", components: "Callable") -> None:
        self._components = components
        SageElement.__init__(self, parent)

    def domain(self) -> "Functor":
        return self.parent().domain()

    def codomain(self) -> "Functor":
        return self.parent().codomain()

    def source(self) -> "Functor":
        return self.domain()

    def target(self) -> "Functor":
        return self.codomain()

    def component(self, obj: "Parent") -> "Morphism":
        morphism = self._components(obj)
        assert morphism.domain() == self.source()(obj), (
            f"the component at {obj} must start at the source image; "
            f"found {morphism.domain()}"
        )
        assert morphism.codomain() == self.target()(obj), (
            f"the component at {obj} must land in the target image; "
            f"found {morphism.codomain()}"
        )
        return morphism

    def __mul__(self, first: "NaturalTransformation") -> "NaturalTransformation":
        r"""Compose natural transformations componentwise."""
        assert first.target() is self.source(), (
            "natural transformations compose only when the middle functor agrees"
        )
        transformations = NaturalTransformations(first.source(), self.target())
        return transformations(
            lambda obj: self.component(obj) * first.component(obj)
        )

    def _repr_(self) -> str:
        return f"Natural transformation from {self.source()} to {self.target()}"


class NaturalTransformationCategory(OwnedCategory):
    r"""The category of natural transformations between parallel functors."""

    ElementType = NaturalTransformation

    def __init__(self, source: Functor, target: Functor) -> None:
        parallel = (
            source.domain() == target.domain()
            and source.codomain() == target.codomain()
        )
        assert parallel, (
            f"natural transformations require parallel functors; found "
            f"{source.domain()} -> {source.codomain()} and "
            f"{target.domain()} -> {target.codomain()}"
        )
        self._source = source
        self._target = target
        super().__init__()

    def super_categories(self) -> list["Category"]:
        return [Objects()]

    def domain(self) -> Functor:
        return self._source

    def codomain(self) -> Functor:
        return self._target

    def __contains__(self, transformation: NaturalTransformation) -> bool:
        return transformation.parent() is self

    def __call__(self, components: "Callable") -> NaturalTransformation:
        return self.ElementType(self, components)

    def identity(self) -> NaturalTransformation:
        assert self._source is self._target, (
            "only an endomorphism category has an identity transformation"
        )
        return self(
            lambda obj: self._source(obj).End().identity()
        )

    def _repr_(self) -> str:
        return f"Natural transformations from {self._source} to {self._target}"


@cached_function
def NaturalTransformations(
    source: Functor,
    target: Functor,
) -> NaturalTransformationCategory:
    r"""Return the category of natural transformations from ``source`` to ``target``."""
    return NaturalTransformationCategory(source, target)


class NaturalIsomorphism(NaturalTransformation):
    r"""A natural isomorphism between parallel functors, as its component data.

    The 2-cells of \(\mathbf{Cat}\): for parallel functors
    \(F, G: C \to D\), a natural isomorphism \(\eta\) assigns each object
    \(X\) an isomorphism \(\eta_X: F(X)\to G(X)\).  The components are the
    *data*; the naturality squares
    \(G(f)\circ\eta_X = \eta_Y\circ F(f)\) are the stated contract the
    supplier of the components owes -- a theorem about the family, carried,
    never re-proved at runtime (a CAS is not a proof assistant).  No
    universal bijectivity decision procedure exists either, so the inverse
    components are declared at construction: a component family with no
    declared inverse is a natural transformation, not an isomorphism.
    """

    def __init__(
        self,
        source: "Functor",
        target: "Functor",
        components: "Callable",
        inverse_components: "Callable",
    ) -> None:
        assert inverse_components is not None, (
            "a natural isomorphism declares its inverse components at "
            "construction"
        )
        self._inverse_components = inverse_components
        NaturalTransformation.__init__(
            self,
            NaturalTransformations(source, target),
            components,
        )

    def inverse(self) -> "NaturalIsomorphism":
        r"""Return \(\eta^{-1}: G \Rightarrow F\), from the declared inverses."""
        return NaturalIsomorphism(
            self.target(),
            self.source(),
            self._inverse_components,
            self._components,
        )

    def is_isomorphism(self) -> bool:
        return True

    def __repr__(self) -> str:
        return (
            f"Natural isomorphism from {self.source()} to {self.target()}"
        )
