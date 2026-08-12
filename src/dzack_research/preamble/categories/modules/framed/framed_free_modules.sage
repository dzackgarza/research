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
from dzack_research.preamble.lexicon import Element
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Module

from sage.categories.modules import Modules
from dzack_research.preamble.categories.sets.sets import _as_set
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

if TYPE_CHECKING:
    from collections.abc import Callable

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleHomset
    from dzack_research.preamble.lexicon import OrderedSet, Set

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
        def Hom(self, codomain: "Module", category: "Category | None" = ...) -> "ModuleHomset": ...
        def _module_generator_element(self, element_of_S: SageElement) -> "FreeModuleOnSetElement": ...
from sage.structure.richcmp import richcmp

from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet


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

    class ParentMethods:
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
                    assert isinstance(images.codomain(), UnderlyingSet), (
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


class FreeModuleOnSetElement(ModuleElement):
    if TYPE_CHECKING:
        # The parent is the free module this coefficient function is read in;
        # ``Element.parent`` states only that it is some parent.  Declared,
        # never defined.
        def parent(self) -> "FreeModuleOnSet": ...

        # Negation is parent-preserving on a module element; ``Element.__neg__``
        # is deliberately wider, for the extended reals where it is not.
        def __neg__(self) -> "FreeModuleOnSetElement": ...

    r"""A finitely supported coefficient function on the set \(S\)."""

    def __init__(self, parent: "FreeModuleOnSet", coefficients: dict) -> None:
        ModuleElement.__init__(self, parent)
        coefficients = dict(coefficients)
        assert all(
            element_of_S in parent.module_generating_set()
            for element_of_S in coefficients
        ), f"the coefficient function is not supported on {parent.module_generating_set()}"
        self._coefficients = {
            element_of_S: coefficient
            for element_of_S, value in coefficients.items()
            if (coefficient := parent.base_ring()(value)) != 0
        }

    def coefficients(self) -> dict:
        return dict(self._coefficients)

    def _add_(self, other: "FreeModuleOnSetElement") -> "FreeModuleOnSetElement":
        zero = self.parent().base_ring().zero()
        support = self._coefficients.keys() | other._coefficients.keys()
        total: "FreeModuleOnSetElement" = self.parent().element_class(
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

    def _sub_(self, other: "FreeModuleOnSetElement") -> "FreeModuleOnSetElement":
        return self._add_(-other)

    def _neg_(self) -> "FreeModuleOnSetElement":
        negated: "FreeModuleOnSetElement" = self.parent().element_class(
            self.parent(),
            {
                element_of_S: -coefficient
                for element_of_S, coefficient in self._coefficients.items()
            },
        )
        return negated

    def _lmul_(self, factor: "RingElement") -> "FreeModuleOnSetElement":
        factor = self.parent().base_ring()(factor)
        scaled: "FreeModuleOnSetElement" = self.parent().element_class(
            self.parent(),
            {
                element_of_S: factor * coefficient
                for element_of_S, coefficient in self._coefficients.items()
            },
        )
        return scaled

    _rmul_ = _lmul_

    def _richcmp_(self, other: "FreeModuleOnSetElement", op: int) -> bool:
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


class FreeModuleOnSet(UniqueRepresentation, OwnedBaseRing, Parent):
    r"""The free \(R\)-module on the actual set \(S\)."""

    @staticmethod
    def __classcall__(
        cls: type["FreeModuleOnSet"],
        base_ring: "Ring",
        module_generating_set: "OrderedSet",
        *arguments: object,
        **keywords: object,
    ) -> "FreeModuleOnSet":
        r"""Return *the* free module on \((R,S)\).

        $F_R(S)=F_R(S')$ exactly when $S=S'$, so there is one object per
        $(R,S)$ and not one per spelling.  The finite ordered case has its own
        class, and the choice is made here rather than in a constructor
        function: reaching the class directly must give the same object, or
        two parents exist on one $(R,S)$ and elements of the two refuse to
        coerce.
        """
        # Local: at module level this closes an import cycle; the finite
        # ordered specialization is built by the time a free module is.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule

        # A ring and the owned view of it are one ring, so they key one
        # module: $F_R(S)$ built over the session's ``ZZ`` and over the
        # engine's must be the same object, or their elements refuse to
        # coerce while both print as the integers.
        base_ring = engine_ring(base_ring)
        # A count names the standard set of that many slots: ``R^n`` says
        # how many generators, not which, and $\Delta[n-1]$ is that set.
        if isinstance(module_generating_set, (int, SageInteger)):
            module_generating_set = Sets.Δ[module_generating_set - 1]
        module_generating_set = _as_set(module_generating_set)
        set_category = module_generating_set.category()
        if cls is FreeModuleOnSet and set_category.is_subcategory(
            Sets().Finite()
        ) and set_category.is_subcategory(Sets().TotallyOrdered()):
            cls = BasedFreeModule
        module: "FreeModuleOnSet" = super(FreeModuleOnSet, cls).__classcall__(
            cls, base_ring, module_generating_set, *arguments, **keywords
        )
        return module

    Element = FreeModuleOnSetElement

    def __init__(
        self,
        base_ring: "Ring",
        module_generating_set: "OrderedSet",
        category: "Category | None" = None,
    ) -> None:
        r"""Frame a free module on ``module_generating_set``.

        ``category`` is what a subclass already knows itself to be: a free
        algebra is one at construction, not after a later refinement, and
        Sage installs a parent's structural surface -- the coercion from the
        base ring among it -- from the category ``Parent.__init__`` is given.
        """
        # Local: at module level these close an import cycle; the ring, finite
        # free and morphism modules are built by the time one is constructed.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism

        # Intake: the module is built over the ring the engine computes in,
        # whichever of the two names for it arrived.  A module over the owned
        # view would carry a base its category, its matrices and its Smith
        # forms do not share.  ``base_ring`` reports the name back.
        base_ring = engine_ring(base_ring)
        module_generating_set = _as_set(module_generating_set)
        self._module_generating_set = module_generating_set
        if category is None:
            category = FramedFreeModules(base_ring)
        Parent.__init__(self, base=base_ring, category=category)
        refine(self, category)
        if module_generating_set in Sets().Finite():
            refine(self, FinitelyGeneratedFreeModules(base_ring))
        self._framing_morphism = framing_morphism(
            self,
            self,
            self._module_generator_element,
        )

    def module_generating_set(self) -> Parent:
        framing: Parent = self._module_generating_set
        return framing

    def framing_morphism(self) -> "FramingMorphism":
        return self._framing_morphism

    def _module_generator_element(self, element_of_S: SageElement) -> FreeModuleOnSetElement:
        assert element_of_S in self._module_generating_set, (
            f"{element_of_S!r} is not in {self._module_generating_set}"
        )
        generator: FreeModuleOnSetElement = self.element_class(
            self,
            {element_of_S: self.base_ring().one()},
        )
        return generator

    def zero(self) -> FreeModuleOnSetElement:
        zero_element: FreeModuleOnSetElement = self.element_class(self, {})
        return zero_element

    def _element_constructor_(self, value: FreeModuleOnSetElement) -> FreeModuleOnSetElement:
        assert isinstance(value, FreeModuleOnSetElement) and value.parent() is self, (
            f"{value} is not an element of {self}"
        )
        return value

    def __contains__(self, value: object) -> bool:
        return isinstance(value, FreeModuleOnSetElement) and value.parent() is self

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, FreeModuleOnSet)
            and self.base_ring() == other.base_ring()
            and self._module_generating_set == other._module_generating_set
        )

    def __hash__(self) -> int:
        return hash((type(self), self.base_ring(), self._module_generating_set))

    def _repr_(self) -> str:
        return f"Free {self.base_ring()}-module on {self._module_generating_set}"


def FreeModuleOn(base_ring: "Ring", module_generating_set: "OrderedSet") -> FreeModuleOnSet:
    r"""Construct \(F_R(S)\) on the supplied set \(S\).

    One object per \((R,S)\): free modules are rigid, and $F_R(S)=F_R(S')$
    exactly when $S=S'$.  The classes are ``UniqueRepresentation`` so that
    holds however the module is reached, not only through this constructor --
    two parents that print alike and cannot coerce is what it prevents.
    """
    # Local: at module level this closes an import cycle; the finite ordered
    # specialization is built by the time a free module is constructed.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule

    return FreeModuleOnSet(base_ring, module_generating_set)
