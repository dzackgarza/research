r"""Free modules on finite totally ordered sets."""

from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module
    from sage.structure.element import Vector

from sage.rings.integer_ring import ZZ as SageZZ
from dzack_research.preamble.categories.sets.sets import _as_set
from dzack_research.preamble.categories.sets.sets import finite_ordered_set
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    from sage.rings.ring import Ring
    from sage.structure.element import RingElement

from dzack_research.preamble.owned_category import object_of
from sage.structure.unique_representation import UniqueRepresentation
from dzack_research.preamble.categories.rings.rings import ℤ
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from collections.abc import Iterable, Iterator, Mapping, Sequence
from typing import Self, TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import ElementConstructorInput, MembershipInput

from sage.rings.integer import Integer
from sage.categories.morphism import SetMorphism
from sage.matrix.constructor import matrix
from sage.modules.free_module_element import FreeModuleElement, vector
from sage.rings.integer import Integer as SageInteger
from sage.structure.element import Element, Element as SageElement, ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, richcmp
from dzack_research.preamble.categories.sets.cardinals import Cardinal

from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix
from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    from sage.categories.category import Category
    from sage.modules.free_module import FreeModule_generic

    # The admissible ways to name a map out of a finite framing, in the order
    # ``hom`` matches them: the generator morphism itself, a finite assignment
    # of generator images, or those images in the framing's order.
    GeneratorAssignment = SetMorphism | dict | list | tuple

    class FiniteFreeModuleParent(Protocol):
        r"""What a parent placed in ``FinitelyGeneratedFreeModules(R)``
        supplies: the finite framing, the ring underneath, the homset
        surface, and the coordinate route in."""

        def base_ring(self) -> "Ring": ...
        def module_generating_set(self) -> "OrderedSet": ...
        def module_generators(self) -> "OrderedSet": ...
        def is_zero(self) -> bool: ...
        def zero(self) -> "BasedFreeModuleElement": ...
        def rank(self) -> "Cardinal": ...
        def Hom(self, codomain: "Module", category: "Category | None" = ...) -> Parent: ...
        def _from_coordinates(self, coordinates: "Vector") -> "BasedFreeModuleElement": ...


def _finite_rank(module_generating_set: "OrderedSet") -> int:
    size = module_generating_set.cardinality()
    if isinstance(size, Cardinal):
        assert size.is_finite(), "a finitely generated module has finite rank"
        return int(size.finite_value())
    return int(size)


class BasedFreeModuleElement(ModuleElement):
    r"""An element represented in its parent's chosen ordered basis."""

    if TYPE_CHECKING:
        # The parent is the based free module the coordinates are read in;
        # ``Element.parent`` states only that it is some parent.  Declared,
        # never defined: the inherited implementation is the one that runs.
        def parent(self) -> "BasedFreeModule": ...

    def __init__(self, parent: "BasedFreeModule", coordinates: "Vector") -> None:
        ModuleElement.__init__(self, parent)
        coordinate_module = parent._coordinate_module()
        # Coordinate arithmetic already lands in the coordinate module, so a
        # sum, difference, negation or scaling arrives here as its own answer.
        # The module rejects a wrong-length assignment itself.
        self._coordinates_: FreeModuleElement = (
            coordinates
            if isinstance(coordinates, FreeModuleElement)
            and coordinates.parent() is coordinate_module
            else coordinate_module(coordinates)
        )

    def _coordinates(self) -> "Vector":
        return self._coordinates_

    def coefficients(self) -> Mapping["Element", "RingElement"]:
        return {
            element_of_S: coefficient
            for element_of_S, coefficient in zip(
                self.parent().module_generating_set(), self._coordinates_
            )
            if coefficient != 0
        }

    def underlying_set_element(self) -> "Element":
        r"""Recover \(s\) when this element is the canonical generator \([s]\)."""
        nonzero = tuple(self.coefficients().items())
        assert len(nonzero) == 1, (
            "only an element in the image of the canonical generator morphism "
            "has one underlying element of S"
        )
        element_of_S: "Element" = nonzero[0][0]
        coefficient = nonzero[0][1]
        assert coefficient == self.parent().base_ring().one(), (
            "only an element in the image of the canonical generator morphism "
            "has one underlying element of S"
        )
        return element_of_S

    def _add_(self, other: "BasedFreeModuleElement") -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(
                self._coordinates_ + other._coordinates_
            )

    def _sub_(self, other: "BasedFreeModuleElement") -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(
                self._coordinates_ - other._coordinates_
            )

    def _neg_(self) -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(-self._coordinates_)

    def _lmul_(self, factor: "RingElement") -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(
                self.parent().base_ring()(factor) * self._coordinates_
            )

    _rmul_ = _lmul_

    def _richcmp_(self, other: "BasedFreeModuleElement", op: int) -> bool:
        return bool(richcmp(self._coordinates_, other._coordinates_, op))


    def __eq__(self, other: "MembershipInput") -> bool:
        # Identification across parents is a stated morphism, never coercion
        # (AGENTS.md: coercion must not erase the element/image distinction),
        # so equality outside this parent is plain False and Sage's
        # conversion fallback never consults a constructor.
        if not (isinstance(other, BasedFreeModuleElement) and other.parent() is self.parent()):
            return False
        return bool(richcmp(self._coordinates_, other._coordinates_, op_EQ))

    def __ne__(self, other: "MembershipInput") -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(tuple(self._coordinates_))

    def __iter__(self) -> Iterator["RingElement"]:
        return iter(self._coordinates_)

    def _repr_(self) -> str:
        return repr(self._coordinates_)


class FinitelyGeneratedFreeModules(OwnedCategoryOverBaseRing):
    r"""Finite free modules whose framing set has a chosen total order."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated framed free modules"

    def super_categories(self: Self) -> list:
        # Local: at module level these close an import cycle; both categories
        # are built by the time supercategories are asked for.
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
        from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import FinitelyGeneratedModules

        return [
            FramedFreeModules(self.base_ring()),
            FinitelyGeneratedModules(self.base_ring()),
        ]

    class ParentMethods(UniqueRepresentation):

        Element = BasedFreeModuleElement

        def __init__(
            self,
            module_generating_set: "OrderedSet",
            **rest: "ConstructionData",
        ) -> None:
            match module_generating_set:
                case int() | SageInteger():
                    assert module_generating_set >= 0, (
                        "the canonical finite framing has nonnegative cardinality"
                    )
                    module_generating_set = Sets.Δ[module_generating_set - 1]
                case Parent():
                    pass
                case Iterable():
                    module_generating_set = _as_set(module_generating_set)
                case _:
                    assert False, (
                        "a generating set is a finite set, a finite iterable, or "
                        "a nonnegative cardinality"
                    )
            if module_generating_set in Sets().Finite():
                module_generating_set = finite_ordered_set(module_generating_set)
            else:
                module_generating_set = _as_set(module_generating_set)
            super().__init__(module_generating_set=module_generating_set, **rest)

        def _module_generator_element(self, element_of_S: SageElement) -> BasedFreeModuleElement:
            module_generating_set = self.__dict__.get("_module_generating_set")
            assert module_generating_set is not None, (
                "a framed free module stores its canonical generating set"
            )
            assert element_of_S in module_generating_set, (
                f"{element_of_S!r} is not in {module_generating_set}"
            )
            index = module_generating_set.index(element_of_S)
            return self._from_coordinates(self._coordinate_module().gen(index))

        def number_of_module_generators(self) -> int:
            return _finite_rank(self.module_generating_set())

        def _coordinate_module(self) -> "FreeModule_generic":
            r"""The engine's \(R^n\), where this module's coordinate vectors live.

            A standard basis vector and the zero vector are this module's own,
            and it decides what counts as a coordinate assignment.
            """
            # Local: at module level this closes an import cycle; the ring module
            # is built by the time coordinates are asked for.
            from dzack_research.preamble.categories.rings.rings import engine_ring

            cached: "FreeModule_generic | None" = self.__dict__.get("_coordinate_module_")
            if cached is None:
                cached = engine_ring(self.base_ring()) ** self.number_of_module_generators()
                self._coordinate_module_ = cached
            return cached

        def zero(self) -> BasedFreeModuleElement:
            return self._from_coordinates(self._coordinate_module().zero())

        def _from_coordinates(self, coordinates: "Vector") -> BasedFreeModuleElement:
            member: BasedFreeModuleElement = self.element_class(self, coordinates)
            return member

        def rank(self) -> "Cardinal":
            return self.module_generating_set().cardinality()

        def _element_constructor_(
            self,
            value: "ElementConstructorInput",
        ) -> BasedFreeModuleElement:
            if isinstance(value, BasedFreeModuleElement) and value.parent() is self:
                return value
            match value:
                case Sequence() | FreeModuleElement():
                    # A framing is exactly what makes a coordinate family name an
                    # element, so a module that has one reads its own coordinates.
                    assert len(value) == self.number_of_module_generators(), (
                        f"{self} has rank {self.number_of_module_generators()}, "
                        f"got {len(value)} coordinates"
                    )
                    return self._from_coordinates(value)
            if value == self.base_ring().zero():
                # $M(0)$ is the zero of $M$: a module has one, the additive
                # identity is what $0$ names in any of them, and writing it is
                # shorter than naming the module's own zero.
                return self.zero()
            assert False, f"{value} is not an element of {self}"

        def __contains__(self, value: "MembershipInput") -> bool:
            match value:
                case BasedFreeModuleElement() if value.parent() is self:
                    return True
                case Element() if (
                    "_structure_morphism" in self.__dict__
                    and value.parent() is self._structure_morphism.codomain()
                ):
                    return bool(self._structure_morphism.image_contains(value))
                case _:
                    return False

        def _stored_module_generating_set(self) -> "OrderedSet":
            r"""Return the generating set the constructor stored.

            Identity reads the stored set rather than
            ``module_generating_set()``, which derives it from the generator
            morphism.  Building that morphism constructs ``UnderlyingSet(self)``,
            a ``UniqueRepresentation`` whose cache looks ``self`` up by hash and
            equality -- so identity computed through the accessor would ask for
            identity to answer.
            """
            module_generating_set = self.__dict__.get("_module_generating_set")
            assert module_generating_set is not None, (
                "a based free module stores its canonical generating set"
            )
            return module_generating_set

        def __eq__(self, other: "MembershipInput") -> bool:
            return (
                type(other) is type(self)
                and self.base_ring() == other.base_ring()
                and tuple(self._stored_module_generating_set())
                == tuple(other._stored_module_generating_set())
            )

        def __hash__(self) -> int:
            return hash(
                (
                    type(self),
                    self.base_ring(),
                    tuple(self._stored_module_generating_set()),
                )
            )

        def _repr_(self) -> str:
            return (
                f"Free {self.base_ring()}-module on the ordered set "
                f"{self.module_generating_set()}"
            )
        def rank(self: "FiniteFreeModuleParent") -> "Cardinal":
            r"""Return the cardinality of the finite generating set."""
            return self.module_generating_set().cardinality()

        def relations(self: "FiniteFreeModuleParent") -> "OrderedSet":
            r"""Return the relations among the module generators: none.

            A free module is presented by its generating set and nothing else
            -- that is what free means -- so the Set is empty.  Empty is not
            the same as absent: a presentation with no relations is still a
            presentation, and a caller who asks a finitely presented module
            for its relations must get an answer when the module happens to
            be free.
            """
            return finite_ordered_set(())

        def relation_matrix(self: "FiniteFreeModuleParent") -> "MorphismMatrix":
            r"""Return the relations as the matrix a presentation asks for.

            The same answer as ``relations``, written the way a presentation
            reads it: $n$ columns for the generators and no rows, because
            there is nothing to impose on them.  A caller that presents this
            module -- a resolution, a normal form -- needs the matrix and
            gets it here rather than rebuilding it from the empty Set.
            """
            # Local: at module level this closes an import cycle; the ring
            # module is built by the time a relation matrix is asked for.
            from dzack_research.preamble.categories.rings.rings import engine_ring

            return MorphismMatrix(
                matrix(
                    engine_ring(self.base_ring()),
                    0,
                    _finite_rank(self.module_generating_set()),
                )
            )

        def number_of_module_generators(self: "FiniteFreeModuleParent") -> "Integer":
            count: "Integer" = self.module_generating_set().cardinality()
            return count

        def is_torsion(self: "FiniteFreeModuleParent") -> bool:
            return bool(self.is_zero())

        def invariants(self: "FiniteFreeModuleParent") -> tuple["Integer", ...]:
            r"""Return the invariant factors, which a free module has none of.

            The structure theorem writes $M\cong\bigoplus R/(d_i)\oplus R^r$
            and this repository's ``invariants`` names the $d_i$ exceeding a
            unit, so a free module answers the empty family -- not an
            absence.  The zero module is where it is asked: being free and
            torsion at once, it is the one object the torsion categories and
            this one share, and they ask the underlying module this.
            """
            return ()

        def Aut(self: "FiniteFreeModuleParent") -> "ModuleAutomorphismGroup":
            # Local: at module level this closes an import cycle; the morphism
            # module is built by the time automorphisms are asked for.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup

            cached = self.__dict__.get("_preamble_Aut")
            if cached is None:
                cached = ModuleAutomorphismGroup(self)
                self._preamble_Aut = cached
            return cached

        def subobject_on(self: "FiniteFreeModuleParent", module_generators: "OrderedSet") -> "Subobject":
            from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules

            module_generators = tuple(
                generator if isinstance(generator, Element)
                and generator.parent() is self
                else self._from_coordinates(generator)
                for generator in module_generators
            )
            return FramedModules.ParentMethods.subobject_on(self, module_generators)

        def hom(self: "FiniteFreeModuleParent", images: "GeneratorAssignment", codomain: "Module | None" = None) -> "ModuleMorphism":
            r"""Construct the map specified on the finite generating set."""
            # Local: at module level this closes an import cycle; the framed
            # module is built by the time a homomorphism is constructed.
            from dzack_research.preamble.categories.modules.framed.framed_modules import _finite_module_generator_assignment
            from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSets

            match images:
                case SetMorphism():
                    assert isinstance(images.codomain(), UnderlyingSets.ParentMethods), (
                        "a generator morphism lands in the underlying set of "
                        "its module codomain"
                    )
                    target = images.codomain().structured_parent()
                    assignment: "GeneratorAssignment" = images
                case dict() if images:
                    target = next(iter(images.values())).parent()
                    assignment = images
                case dict():
                    assert codomain is not None, (
                        "the empty assignment requires an explicitly named codomain"
                    )
                    target = codomain
                    assignment = images
                case list() | tuple():
                    target, assignment = _finite_module_generator_assignment(
                        self,
                        images,
                        codomain,
                    )
                case _:
                    assert False, (
                        "a homomorphism is specified by a generator morphism, "
                        "a finite assignment, or an ordered list of images"
                    )
            return self.Hom(target)(assignment)


def BasedFreeModule(
    base_ring: "Ring", module_generating_set: "OrderedSet"
) -> "Parent":
    r"""Construct \(F_R(S)\) for a finite, totally ordered \(S\).

    The order on \(S\) indexes a basis, which is what makes the module a
    *based* one and puts it in this category rather than the framed free one.
    """
    # Local: at module level this closes an import cycle; the ring module is
    # built by the time a free module is constructed.
    from dzack_research.preamble.categories.rings.rings import engine_ring

    return object_of(
        FinitelyGeneratedFreeModules(engine_ring(base_ring)),
        module_generating_set=module_generating_set,
    )


def Free_ZZ(module_generating_set: "OrderedSet") -> "Parent":
    r"""Construct the free \(\mathbb Z\)-module on ``module_generating_set``."""
    # Local: at module level this closes an import cycle; the general free
    # module is built by the time one is constructed over ZZ.
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOn

    return FreeModuleOn(ℤ, module_generating_set)
