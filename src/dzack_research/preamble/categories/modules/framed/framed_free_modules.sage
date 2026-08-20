r"""Free modules on arbitrary sets.

``FreeModuleOnSet(R, S)`` realizes

\[
    F_R(S)=\{a:S\to R\mid \operatorname{supp}(a)\text{ is finite}\}.
\]

The set \(S\) is construction data.  It need not be finite, countable, or
ordered.  Finite ordered free modules are the specialization implemented by
``BasedFreeModule``.
"""


from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import ElementConstructorInput, MembershipInput
from dzack_research.preamble.lexicon import Element
if TYPE_CHECKING:
    from sage.categories.modules import Module

from sage.categories.modules import Modules
from dzack_research.preamble.categories.sets.sets import _as_set
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.refine import refine
if TYPE_CHECKING:
    from sage.categories.category import Category
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from sage.rings.ring import Ring
    from sage.structure.element import RingElement

from dzack_research.preamble.categories.rings.rings import engine_ring
from dzack_research.preamble.categories.rings.rings import OwnedBaseRing
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from typing import Self, TYPE_CHECKING

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.structure.element import ModuleElement
from sage.rings.integer import Integer as SageInteger
from sage.structure.parent import Parent
from sage.structure.element import Element as SageElement
from sage.structure.unique_representation import UniqueRepresentation
from collections.abc import Mapping

if TYPE_CHECKING:
    from collections.abc import Callable

    from dzack_research.preamble.owned_category import ConstructionData
    from dzack_research.preamble.categories.sets.cardinals import Cardinal
    from sage.categories.sets_cat import Set
    from dzack_research.preamble.lexicon import OrderedSet

    # The admissible ways to name a map out of a free framing, in the order
    # ``hom`` matches them: the generator morphism itself, a finite assignment
    # of generator images, or any function on the framing set.
    GeneratorAssignment = SetMorphism | dict | Callable

    class FreeModuleParent(Protocol):
        r"""What a parent placed in ``FramedFreeModules(R)`` supplies: the
        framing set it was built on, the ring underneath, the homset surface,
        and the canonical generator naming a label."""

        def base_ring(self) -> "Ring": ...
        def module_generating_set(self) -> "OrderedSet": ...
        def module_generator_morphism(self) -> SetMorphism: ...
        def Hom(self, codomain: "Module", category: "Category | None" = ...) -> Parent: ...
        def _module_generator_element(self, element_of_S: SageElement) -> "FramedFreeModules.ElementMethods": ...
from sage.structure.richcmp import richcmp

from dzack_research.preamble.categories.sets.owned_sets import placement_of
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.underlying_sets import (
    UnderlyingSet,
    UnderlyingSets,
)

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet


def _free_module_placement(
    base_ring: "Ring", module_generating_set: "OrderedSet"
) -> Sets:
    r"""The owned ``Sets()`` placement of \(F_R(S)=\bigoplus_S R\).

    Read off the placements of \(R\) and of \(S\), which is what decides the
    question and what a general ring states.  \(R\) is the owned ring and not
    the engine's: countability and uncountability are what the owned rings
    add, and \(\mathbb R\) reaches the engine declaring only that it is
    infinite.  The exact count is
    :meth:`FramedFreeModules.ParentMethods.cardinality`; it is not asked
    here, because Sage equips only some rings to say how big they are -- a
    maximal order in a number field does not -- and a construction must not
    depend on that.  Such a ring leaves the module unplaced, which is the
    honest answer rather than a size nobody computed.
    """
    ring = frozenset(placement_of(base_ring).axioms())
    framing = frozenset(placement_of(module_generating_set).axioms())
    finite_framing = "Finite" in framing
    if finite_framing and module_generating_set.cardinality() == 0:
        # \(F_R(\emptyset)=0\): the singleton, over any ring at all.
        return Sets().Finite()
    if "Finite" in ring:
        # A finite ring states its order, so both finite cases are decided
        # exactly -- including the zero ring, over which every module is zero.
        if base_ring.cardinality() == 1 or finite_framing:
            return Sets().Finite()
        return Sets().Infinite()
    if "Uncountable" in ring:
        return Sets().Uncountable()
    if "Infinite" in ring:
        return Sets().Infinite()
    return Sets()



class FramedFreeModules(OwnedCategoryOverBaseRing):
    r"""Free modules equipped with the canonical map \(S\to U(F_R(S))\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed free modules"

    def super_categories(self) -> list:
        # Local: at module level this closes an import cycle; the free-module
        # category is built by the time supercategories are asked for.
        from dzack_research.preamble.categories.modules.pure.free_modules import FreeModules
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules

        return [FreeModules(self.base_ring()), FramedModules(self.base_ring())]

    class ElementMethods:
        r"""A finitely supported coefficient function on the set \(S\).

        The coefficient function is what this level adds to an element, so
        this level takes it and sends the remainder up.
        """

        if TYPE_CHECKING:
            # The parent is the free module this coefficient function is read in;
            # ``Element.parent`` states only that it is some parent.  Declared,
            # never defined.
            def parent(self) -> "FreeModuleOnSet": ...

            # Negation is parent-preserving on a module element; ``Element.__neg__``
            # is deliberately wider, for the extended reals where it is not.
            def __neg__(self) -> "FramedFreeModules.ElementMethods": ...

        def __init__(
            self,
            parent: "FreeModuleOnSet",
            coefficients: dict,
            **rest: "ConstructionData",
        ) -> None:
            super().__init__(parent, **rest)
            coefficients = dict(coefficients)
            assert all(
                element_of_S in parent.module_generating_set()
                for element_of_S in coefficients
            ), f"the coefficient function is not supported on {parent.module_generating_set()}"
            self._coefficients: dict["Element", "RingElement"] = {
                element_of_S: coefficient
                for element_of_S, value in coefficients.items()
                if (coefficient := parent.base_ring()(value)) != 0
            }

        def coefficients(self) -> Mapping["Element", "RingElement"]:
            return dict(self._coefficients)

        def _add_(self, other: "FramedFreeModules.ElementMethods") -> "FramedFreeModules.ElementMethods":
            zero = self.parent().base_ring().zero()
            support = self._coefficients.keys() | other._coefficients.keys()
            total: "FramedFreeModules.ElementMethods" = self.parent().element_class(
                self.parent(),
                {
                    element_of_S: (
                        self._coefficients.get(element_of_S, zero)
                        + other._coefficients.get(element_of_S, zero)
                    )
                    for element_of_S in support
                },
            )
            return total

        def _sub_(self, other: "FramedFreeModules.ElementMethods") -> "FramedFreeModules.ElementMethods":
            return self._add_(-other)

        def _neg_(self) -> "FramedFreeModules.ElementMethods":
            negated: "FramedFreeModules.ElementMethods" = self.parent().element_class(
                self.parent(),
                {
                    element_of_S: -coefficient
                    for element_of_S, coefficient in self._coefficients.items()
                },
            )
            return negated

        def _lmul_(self, factor: "RingElement") -> "FramedFreeModules.ElementMethods":
            factor = self.parent().base_ring()(factor)
            scaled: "FramedFreeModules.ElementMethods" = self.parent().element_class(
                self.parent(),
                {
                    element_of_S: factor * coefficient
                    for element_of_S, coefficient in self._coefficients.items()
                },
            )
            return scaled

        _rmul_ = _lmul_

        def _richcmp_(self, other: "FramedFreeModules.ElementMethods", op: int) -> bool:
            return richcmp(self._coefficients, other._coefficients, op)

        def __hash__(self) -> int:
            return hash(frozenset(self._coefficients.items()))

        def underlying_set_element(self) -> "Element":
            r"""Recover \(s\) when this element is the canonical generator \([s]\)."""
            assert len(self._coefficients) == 1, (
                "only an element in the image of the canonical generator morphism "
                "has one underlying element of S"
            )
            element_of_S, coefficient = next(iter(self._coefficients.items()))
            assert coefficient == self.parent().base_ring().one(), (
                "only an element in the image of the canonical generator morphism "
                "has one underlying element of S"
            )
            return element_of_S

        def _repr_(self) -> str:
            if not self._coefficients:
                return "0"
            return " + ".join(
                f"{coefficient}*[{element_of_S!r}]"
                for element_of_S, coefficient in self._coefficients.items()
            )

    class ParentMethods(UniqueRepresentation):
        r"""The free \(R\)-module on the actual set \(S\).

        ``UniqueRepresentation`` is named here because \(F_R(S)\) must be
        *the* free module on \((R,S)\).  \(F_R(S)=F_R(S')\) exactly when
        \(S=S'\), so two parents on one \((R,S)\) would print alike and
        refuse to coerce each other's elements.  It is a Sage implementation
        class, so naming it states how this chain reaches Sage rather than
        patching the class graph.
        """

        # Installed by the constructor.
        _module_generating_set: "OrderedSet"
        _framing_morphism: "FramingMorphism"

        def __init__(
            self,
            module_generating_set: "OrderedSet",
            **rest: "ConstructionData",
        ) -> None:
            # Local: at module level these close an import cycle; the finite
            # free and morphism modules are built by the time one is.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism

            self._module_generating_set = _as_set(module_generating_set)
            super().__init__(**rest)
            # Finite *and* totally ordered, because the category refined into
            # is the based free modules and an ordering is what it adds.  An element
            # here is the finitely supported \(a:S\to R\); what a chosen total
            # order buys is a way to write that function down, as the
            # coordinate vector indexed by the order.  Finiteness of \(S\) is a
            # property of \(S\) and orders it not at all, so admitting a
            # finite unordered framing to that level gives an object whose
            # elements are asked for coordinates no order exists to produce:
            # the exterior algebra, framed by the subsets of \(S\), and every
            # algebra on the empty label set, framed by \(\{1\}\), both arrive
            # that way.  This is the same test the constructor
            # :func:`FreeModuleOn` applies, and the two must agree.
            placement = self._module_generating_set.category()
            if placement.is_subcategory(
                Sets().Finite()
            ) and placement.is_subcategory(Sets().TotallyOrdered()):
                refine(self, FinitelyGeneratedFreeModules(self.base_ring()))
            # The underlying set: a module that cannot say whether it is
            # finite or infinite is unusable to every construction that ranges
            # over its elements, and the free module's own \(R\) and \(S\)
            # decide it.
            refine(
                self,
                _free_module_placement(
                    self.base_ring(), self._module_generating_set
                ),
            )
            self._framing_morphism = framing_morphism(
                self, self, self._module_generator_element
            )

        def module_generating_set(self: "FreeModuleParent") -> "Parent":
            framing: "Parent" = self._module_generating_set
            return framing

        def framing_morphism(self: "FreeModuleParent") -> "FramingMorphism":
            return self._framing_morphism

        def _module_generator_element(
            self: "FreeModuleParent", element_of_S: SageElement
        ) -> FramedFreeModules.ElementMethods:
            assert element_of_S in self._module_generating_set, (
                f"{element_of_S!r} is not in {self._module_generating_set}"
            )
            generator: FramedFreeModules.ElementMethods = self.element_class(
                self, {element_of_S: self.base_ring().one()}
            )
            return generator

        def zero(self: "FreeModuleParent") -> FramedFreeModules.ElementMethods:
            zero_element: FramedFreeModules.ElementMethods = self.element_class(self, {})
            return zero_element

        def _element_constructor_(
            self: "FreeModuleParent", value: FramedFreeModules.ElementMethods
        ) -> FramedFreeModules.ElementMethods:
            assert (
                isinstance(value, FramedFreeModules.ElementMethods)
                and value.parent() is self
            ), f"{value} is not an element of {self}"
            return value

        def __contains__(
            self: "FreeModuleParent", value: "MembershipInput"
        ) -> bool:
            return (
                isinstance(value, FramedFreeModules.ElementMethods)
                and value.parent() is self
            )

        def _repr_(self: "FreeModuleParent") -> str:
            return (
                f"Free {self.base_ring()}-module on "
                f"{self._module_generating_set}"
            )

        def module_generators(self: "FreeModuleParent") -> "Set":
            r"""Return the framed generators, as a set, without counting them.

            The general framed version leaves injectivity to be probed, and
            Sage probes it by asking this module for a cardinality an
            infinite module has no reason to answer.  On a *free* module the
            framing is injective by construction -- distinct labels index
            distinct basis elements -- so saying so is honest, and it is what
            lets $\ZZ^{\infty}$ answer at all.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from sage.sets.image_set import ImageSubobject

            return ImageSubobject(
                self.module_generator_morphism(),
                self.module_generating_set(),
                is_injective=True,
            )

        def module_generator_morphism(self: "FreeModuleParent") -> SetMorphism:
            r"""Return the canonical set morphism \(S\to U(F_R(S))\)."""
            morphism: SetMorphism | None = self.__dict__.get("_free_module_generator_morphism")
            if morphism is None:
                module_generating_set = self.__dict__.get("_module_generating_set")
                assert (
                    module_generating_set is not None
                ), "a framed free module stores its framing set"
                morphism = SetMorphism(
                    Hom(module_generating_set, UnderlyingSet(self), Sets()),
                    self._module_generator_element,
                )
                self._free_module_generator_morphism = morphism
            return morphism

        def hom(self: "FreeModuleParent", images: "GeneratorAssignment", codomain: "Module | None" = None) -> "ModuleMorphism":
            r"""Extend a set morphism \(S\to U(N)\) \(R\)-linearly."""
            match images:
                case SetMorphism():
                    assert isinstance(images.codomain(), UnderlyingSets.ParentMethods), (
                        "a generator morphism lands in the underlying set of "
                        "its module codomain"
                    )
                    target = images.codomain().structured_parent()
                case dict():
                    assert images, (
                        "an empty assignment does not determine its codomain; "
                        "construct it through M.Hom(N)"
                    )
                    target = next(iter(images.values())).parent()
                case _ if callable(images):
                    assert codomain is not None, (
                        "a generator function requires its codomain"
                    )
                    target = codomain
                case _:
                    assert False, (
                        "a map from a general free module is specified by a "
                        "set morphism from its generating set"
                    )
            return self.Hom(target)(images)

        def is_torsion_free(self: Self) -> bool:
            return True

        def cardinality(self: "FreeModuleParent") -> "Cardinal":
            r"""Return \(|F_R(S)|\), which the construction determines.

            An element is a finitely supported \(a:S\to R\), so for a finite
            \(S\) the underlying set is \(R^{|S|}\) and the count is
            \(|R|^{|S|}\).  For an infinite \(S\) finite support is what keeps
            the count down: with at least two coefficients to choose from the
            finitely supported functions number \(\max(|R|,|S|)\), and *not*
            \(|R|^{|S|}\), which counts the product \(\prod_S R\) -- a
            different module.  Over the zero ring every module is zero, so
            the count is \(1\) whatever \(S\) is.
            """
            # Local: at module level this closes an import cycle; the cardinals
            # are built by the time a module is asked how big it is.
            from dzack_research.preamble.categories.sets.cardinals import Cardinalities, cardinal

            framing_size = cardinal(self.module_generating_set().cardinality())
            if framing_size == 0:
                # \(F_R(\emptyset)\) is the zero module over any ring at all,
                # so this answers before the ring is asked anything.
                return cardinal(1)
            ring_size = cardinal(self.base_ring().cardinality())
            if framing_size.is_finite():
                return Cardinalities().power(ring_size, framing_size)
            if ring_size == 1:
                return cardinal(1)
            return Cardinalities().supremum(ring_size, framing_size)


def FreeModuleOn(
    base_ring: "Ring", module_generating_set: "OrderedSet"
) -> "Parent":
    r"""Construct \(F_R(S)\) on the supplied set \(S\).

    One object per \((R,S)\): free modules are rigid, and \(F_R(S)=F_R(S')\)
    exactly when \(S=S'\).  The ``ParentMethods`` of these categories name
    ``UniqueRepresentation``, so that holds however the module is reached and
    not only through this constructor.  Two parents that print alike and
    cannot coerce is what it prevents.

    The category is the choice this makes.  A finite, totally ordered
    generating set indexes a basis, so the module is a *based* one and the
    finitely generated free category is where it belongs; any other set gives
    the framed free category.  The old class-level ``__classcall__`` said the
    same thing by returning a different class.
    """
    # Local: at module level these close an import cycle; the finite ordered
    # specialization is built by the time a free module is constructed.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules

    # A ring and the owned view of it are one ring, so they key one module:
    # \(F_R(S)\) built over the session's ``ZZ`` and over the engine's must be
    # the same object, or their elements refuse to coerce while both print as
    # the integers.
    base_ring = engine_ring(base_ring)
    # A count names the standard set of that many slots: ``R^n`` says how many
    # generators, not which, and \(\Delta[n-1]\) is that set.
    if isinstance(module_generating_set, (int, SageInteger)):
        module_generating_set = Sets.Δ[module_generating_set - 1]
    module_generating_set = _as_set(module_generating_set)
    set_category = module_generating_set.category()
    based = set_category.is_subcategory(
        Sets().Finite()
    ) and set_category.is_subcategory(Sets().TotallyOrdered())
    category = (
        FinitelyGeneratedFreeModules(base_ring)
        if based
        else FramedFreeModules(base_ring)
    )
    return object_of(category, module_generating_set=module_generating_set)
