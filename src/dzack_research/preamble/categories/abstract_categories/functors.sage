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
- :class:`FunctorSpaces`, whose objects are the \(\operatorname{Fun}(C,D)\)
  as first-class parents: the homsets of \(\mathbf{Cat}\) (method-placement
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
from sage.categories.homset import Homset as SageHomset

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.owned_category_bases import Category as OwnedCategory
from dzack_research.preamble.refine import refine

if TYPE_CHECKING:
    from collections.abc import Callable

    from sage.categories.category import Category
    from sage.categories.morphism import Morphism
    from sage.structure.parent import Parent


class Functor(SageElement):
    r"""The owned functor base: a **morphism of** \(\mathbf{Cat}\).

    A functor is a morphism of \(\mathbf{Cat}\), and a morphism is an element
    of its homset, so a functor's ``parent()`` is
    \(\operatorname{Hom}_{\mathbf{Cat}}(C,D)=\) :class:`FunctorSpace`.

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
        SageElement.__init__(self, FunctorSpace(domain, codomain))

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
        if isinstance(x, SageMorphism) and not isinstance(x, Functor):
            return self._apply_functor_to_morphism(x)
        assert x in self.domain(), (
            f"{x} is not an object of {self.domain()}, the domain of {self}"
        )
        image = self._apply_functor(x)
        assert image in self.codomain() or image in self.codomain().Homsets(), (
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


class FunctorSpaces(OwnedCategory):
    r"""\(\operatorname{Fun}(C, D)\): the functors \(C\to D\) as a first-class parent.

    An object is a homset of \(\mathbf{Cat}\).  Membership is exact boundary
    agreement.  The endofunctor space owns its identity.  Existence and
    element handling are the contract; no enumeration is promised.

    **This category adopts a Sage parent; it does not construct one.**  Sage's
    ``Homset.__init__`` supplies the boundary accessors and the homset
    semantics, and it is also what decides the placement: its last act is
    ``Parent.__init__(category=category.Endsets() if X is Y else
    category.Homsets())``.  So a functor space is already an object of
    ``Cat().Homsets()`` before this category sees it, and the route in is
    :func:`~dzack_research.preamble.refine.refine`, which puts these methods
    ahead of ``Homset``'s own.  The construction chain is not available here:
    it would have to write ``Homset``'s private boundary fields by hand.

    The methods a functor space's *elements* have stay on :class:`Functor`
    below, which every owned functor derives from.
    """

    def _repr_object_names(self) -> str:
        return "functor spaces"

    def super_categories(self) -> list["Category"]:
        return [Cat().Homsets()]

    class ParentMethods:
        def _repr_(self) -> str:
            return f"Fun({self.domain()}, {self.codomain()})"

        def __contains__(self, functor: "Functor") -> bool:
            r"""Membership is parenthood: a functor lives in exactly one space.

            Not a type probe plus a boundary comparison.  A functor is an
            element of its homset, so the mathematical question -- is this a
            functor \(C\to D\)? -- is answered by the structure that already
            holds it.
            """
            return isinstance(functor, Functor) and functor.parent() is self

        def _element_constructor_(self, functor: "Functor") -> "Functor":
            r"""Admit a functor of this boundary.

            A functor is not assembled from raw data here: each owned functor
            is its own construction, declaring what it does to objects and to
            morphisms.  What this owns is the parenthood check.
            """
            assert functor in self, f"{functor} is not a functor in {self}"
            return functor

        def identity(self) -> "IdentityFunctor":
            assert self.domain() == self.codomain(), (
                f"only an endofunctor space has an identity; "
                f"found Fun({self.domain()}, {self.codomain()})"
            )
            return IdentityFunctor(self.domain())


@cached_function
def FunctorSpace(domain: "Category", codomain: "Category") -> "Parent":
    r"""Return \(\operatorname{Fun}(C, D)\), the functors \(C\to D\).

    One space per boundary pair, because a functor's parent is its identity:
    ``FunctorSpaces.ParentMethods.__contains__`` reads membership off
    ``parent() is self``, so two spaces on one boundary would make one functor
    fail to be in its own space.
    """
    cat = Cat()
    assert domain in cat and codomain in cat, (
        f"a functor space's boundary must be objects of Cat; "
        f"found {domain!r} and {codomain!r}"
    )
    space = SageHomset(domain, codomain, category=cat, check=False)
    functor_space: "Parent" = refine(space, FunctorSpaces())
    return functor_space


class NaturalIsomorphism:
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
        parallel = (
            source.domain() == target.domain()
            and source.codomain() == target.codomain()
        )
        assert parallel, (
            f"natural transformations require parallel functors; found "
            f"{source.domain()} -> {source.codomain()} and "
            f"{target.domain()} -> {target.codomain()}"
        )
        assert inverse_components is not None, (
            "a natural isomorphism declares its inverse components at "
            "construction"
        )
        self._source = source
        self._target = target
        self._components = components
        self._inverse_components = inverse_components

    def source(self) -> "Functor":
        r"""Return \(F\), the functor the components leave."""
        return self._source

    def target(self) -> "Functor":
        r"""Return \(G\), the functor the components land in."""
        return self._target

    def component(self, obj: "Parent") -> "Morphism":
        r"""Return \(\eta_X: F(X)\to G(X)\), the component at ``obj``."""
        morphism = self._components(obj)
        assert morphism.domain() == self._source(obj), (
            f"the component at {obj} must start at the source image; "
            f"found {morphism.domain()}"
        )
        assert morphism.codomain() == self._target(obj), (
            f"the component at {obj} must land in the target image; "
            f"found {morphism.codomain()}"
        )
        return morphism

    def inverse(self) -> "NaturalIsomorphism":
        r"""Return \(\eta^{-1}: G \Rightarrow F\), from the declared inverses."""
        return NaturalIsomorphism(
            self._target,
            self._source,
            self._inverse_components,
            self._components,
        )

    def __repr__(self) -> str:
        return (
            f"Natural isomorphism from {self._source} to {self._target}"
        )
