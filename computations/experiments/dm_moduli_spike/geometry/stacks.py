r"""Core geometric parents: stacks, immersions, compactifications, quotients.

Theorem-backed formal geometry: constructors establish category membership and
axioms; atlases/diagonals are formal morphisms with correct Hom membership.
"""

from __future__ import annotations

from sage.structure.parent import Parent
from sage.structure.element import Element
from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme, spec
from ..categories.stacks import (
    AlgebraicStacks,
    DeligneMumfordStacks,
    ModuliStacks,
    Stacks,
)
from ..categories.schemes import AlgebraicSpaces, Schemes, Varieties


class GeometricObject(UniqueRepresentation, Parent):
    r"""Base parent for theorem-backed geometric objects over a base scheme."""

    def __init__(self, base: AffineScheme, category: object, *, axioms: frozenset[str] | None = None) -> None:
        self._base = base
        self._axioms = frozenset(axioms or ())
        Parent.__init__(self, category=category)

    def base_scheme(self) -> AffineScheme:
        return self._base

    def declared_axioms(self) -> frozenset[str]:
        return self._axioms

    def is_proper(self) -> bool:
        return "Proper" in self._axioms

    def is_smooth(self) -> bool:
        return "Smooth" in self._axioms

    def is_projective(self) -> bool:
        return "Projective" in self._axioms

    def is_normal(self) -> bool:
        return "Normal" in self._axioms

    def is_finite_type(self) -> bool:
        return "FiniteType" in self._axioms


class Stack(GeometricObject):
    r"""Stack over a base scheme (theorem-backed formal parent)."""

    def __init__(
        self,
        base: AffineScheme,
        *,
        name: str = "Stack",
        axioms: frozenset[str] | None = None,
        category: object | None = None,
    ) -> None:
        self._name = name
        cat = category if category is not None else Stacks(base)
        GeometricObject.__init__(self, base, cat, axioms=axioms)

    def fiber(self, T: object) -> StackFiber:
        return StackFiber(self, T)

    def __call__(self, T: object) -> StackFiber:
        return self.fiber(T)

    def pullback(self, f: object) -> Stack:
        return self

    def _Hom_(self, other: object, category: object = None) -> StackHomset:
        return StackHomset(self, other)

    def _repr_(self) -> str:
        return self._name


class AlgebraicStack(Stack):
    def __init__(self, base: AffineScheme, *, name: str = "AlgebraicStack", axioms: frozenset[str] | None = None) -> None:
        Stack.__init__(self, base, name=name, axioms=axioms, category=AlgebraicStacks(base))

    def diagonal(self) -> StackMorphism:
        return StackMorphism(self, self, kind="diagonal")

    def atlas(self) -> StackMorphism:
        return StackMorphism(self, self, kind="atlas")


class DeligneMumfordStack(AlgebraicStack):
    def __init__(
        self,
        base: AffineScheme,
        *,
        name: str = "DeligneMumfordStack",
        axioms: frozenset[str] | None = None,
    ) -> None:
        ax = frozenset(axioms or ())
        cat = DeligneMumfordStacks(base)
        for a in sorted(ax):
            cat = getattr(cat, a)()
        Stack.__init__(self, base, name=name, axioms=ax, category=cat)

    def etale_atlas(self) -> StackMorphism:
        return StackMorphism(self, self, kind="etale_atlas")


class AlgebraicSpace(DeligneMumfordStack):
    def __init__(
        self,
        base: AffineScheme,
        *,
        name: str = "AlgebraicSpace",
        axioms: frozenset[str] | None = None,
    ) -> None:
        ax = frozenset(axioms or ())
        cat = AlgebraicSpaces(base)
        for a in sorted(ax):
            if hasattr(cat, a):
                cat = getattr(cat, a)()
        Stack.__init__(self, base, name=name, axioms=ax, category=cat)

    def as_stack(self) -> DeligneMumfordStack:
        return self


class Variety(AlgebraicSpace):
    def __init__(
        self,
        base: AffineScheme,
        *,
        name: str = "Variety",
        axioms: frozenset[str] | None = None,
    ) -> None:
        ax = frozenset({"Integral", "Separated", "FiniteType"}) | frozenset(axioms or ())
        cat = Varieties(base)
        for a in sorted(ax):
            if hasattr(cat, a):
                cat = getattr(cat, a)()
        Stack.__init__(self, base, name=name, axioms=ax, category=cat)

    def scheme(self) -> Variety:
        return self


class StackFiber(UniqueRepresentation, Parent):
    r"""Groupoid of objects of a stack over a test scheme `T`."""

    def __init__(self, stack: Stack, test_object: object) -> None:
        from sage.categories.sets_cat import Sets

        self._stack = stack
        self._T = test_object
        Parent.__init__(self, category=Sets())

    def stack(self) -> Stack:
        return self._stack

    def base(self) -> object:
        return self._T

    def an_element(self) -> StackObject:
        return StackObject(self)

    def _repr_(self) -> str:
        return f"{self._stack!r}({self._T!r})"


class StackObject(Element):
    def __init__(self, parent: StackFiber) -> None:
        Element.__init__(self, parent)

    def _repr_(self) -> str:
        return f"Object of {self.parent()}"


class StackObjectIsomorphism(Element):
    def __init__(self, parent: object, source: StackObject, target: StackObject) -> None:
        self._source = source
        self._target = target
        Element.__init__(self, parent)


class StackHomset(UniqueRepresentation, Parent):
    def __init__(self, domain: object, codomain: object) -> None:
        from sage.categories.homsets import Homsets

        self._domain = domain
        self._codomain = codomain
        Parent.__init__(self, category=Homsets())

    def domain(self) -> object:
        return self._domain

    def codomain(self) -> object:
        return self._codomain

    def __call__(self, data: object = None, **kwargs: object) -> StackMorphism:
        if isinstance(data, StackMorphism):
            return data
        kind = str(kwargs.get("kind", "morphism"))
        return StackMorphism(self._domain, self._codomain, kind=kind)

    def an_element(self) -> StackMorphism:
        return StackMorphism(self._domain, self._codomain)

    def _repr_(self) -> str:
        return f"Hom({self._domain!r}, {self._codomain!r})"

    def __contains__(self, morph: object) -> bool:
        return (
            isinstance(morph, StackMorphism)
            and morph.domain() is self._domain
            and morph.codomain() is self._codomain
        )


class StackMorphism(Element):
    def __init__(self, domain: object, codomain: object, *, kind: str = "morphism") -> None:
        self._domain = domain
        self._codomain = codomain
        self._kind = kind
        parent = StackHomset(domain, codomain)
        Element.__init__(self, parent)

    def domain(self) -> object:
        return self._domain

    def codomain(self) -> object:
        return self._codomain

    def is_open_immersion(self) -> bool:
        return isinstance(self, OpenImmersion) or self._kind == "open_immersion"

    def is_closed_immersion(self) -> bool:
        return isinstance(self, ClosedImmersion) or self._kind == "closed_immersion"

    def _repr_(self) -> str:
        return f"StackMorphism({self._domain!r} -> {self._codomain!r}, {self._kind})"


class Stack2Isomorphism(Element):
    def __init__(self, parent: object, f: StackMorphism, g: StackMorphism) -> None:
        self._f = f
        self._g = g
        Element.__init__(self, parent)


class OpenImmersion(StackMorphism):
    def __init__(self, domain: object, codomain: object) -> None:
        StackMorphism.__init__(self, domain, codomain, kind="open_immersion")


class ClosedImmersion(StackMorphism):
    def __init__(self, domain: object, codomain: object) -> None:
        StackMorphism.__init__(self, domain, codomain, kind="closed_immersion")


class LocallyClosedImmersion(StackMorphism):
    def __init__(self, domain: object, codomain: object) -> None:
        StackMorphism.__init__(self, domain, codomain, kind="locally_closed_immersion")


class ProductStack(DeligneMumfordStack):
    @staticmethod
    def __classcall_private__(cls, factors: tuple[Stack, ...] | list[Stack], *, base: AffineScheme | None = None) -> ProductStack:
        factors_t = tuple(factors)
        return super().__classcall__(cls, factors_t, base=base)

    def __init__(self, factors: tuple[Stack, ...], *, base: AffineScheme | None = None) -> None:
        if not factors:
            raise ValueError("ProductStack requires at least one factor")
        base = base if base is not None else factors[0].base_scheme()
        self._factors = factors
        DeligneMumfordStack.__init__(
            self,
            base,
            name=f"ProductStack({len(factors)})",
            axioms=frozenset({"Smooth", "FiniteType"}),
        )

    def factors(self) -> tuple[Stack, ...]:
        return self._factors


class QuotientStack(DeligneMumfordStack):
    def __init__(self, space: Stack, group: object, action: object | None = None) -> None:
        self._space = space
        self._group = group
        self._action = action
        DeligneMumfordStack.__init__(
            self,
            space.base_scheme(),
            name=f"QuotientStack({space!r}/{group!r})",
            axioms=frozenset({"Smooth", "FiniteType"}),
        )

    def space(self) -> Stack:
        return self._space

    def group(self) -> object:
        return self._group


class Compactifications(UniqueRepresentation, Parent):
    def __init__(self, source: Stack) -> None:
        from sage.categories.sets_cat import Sets

        self._source = source
        Parent.__init__(self, category=Sets())

    def source(self) -> Stack:
        return self._source

    def __contains__(self, obj: object) -> bool:
        return isinstance(obj, Compactification) and obj.source() is self._source

    def _repr_(self) -> str:
        return f"Compactifications({self._source!r})"


class Compactification(OpenImmersion):
    r"""Open immersion `j: X ↪ X̄` with proper target (Stacks Project 0F44)."""

    def __init__(self, source: Stack, target: Stack, *, kind: str = "compactification") -> None:
        if not target.is_proper():
            # theorem-backed parents must declare Proper
            raise ValueError("compactification target must be proper over the base")
        self._kind_name = kind
        OpenImmersion.__init__(self, source, target)

    def source(self) -> Stack:
        return self._domain  # type: ignore[return-value]

    def target(self) -> Stack:
        return self._codomain  # type: ignore[return-value]

    def domain(self) -> Stack:
        return self.source()

    def codomain(self) -> Stack:
        return self.target()

    def boundary(self, reduced: bool = True) -> Boundary:
        return Boundary(self, reduced=reduced)

    def _repr_(self) -> str:
        return f"Compactification({self.source()!r} ↪ {self.target()!r})"


class Boundary(GeometricObject):
    r"""Closed complement of a compactification open immersion."""

    def __init__(self, compactification: Compactification, *, reduced: bool = True) -> None:
        self._compactification = compactification
        self._reduced = reduced
        ambient = compactification.target()
        GeometricObject.__init__(
            self,
            ambient.base_scheme(),
            category=ambient.category(),
            axioms=ambient.declared_axioms(),
        )

    def compactification(self) -> Compactification:
        return self._compactification

    def ambient_space(self) -> Stack:
        return self._compactification.target()

    def open_complement(self) -> Stack:
        return self._compactification.source()

    def closed_immersion(self) -> ClosedImmersion:
        return ClosedImmersion(self, self.ambient_space())

    def underlying_space(self) -> Boundary:
        return self

    def stratification_poset(self, order: str = "specialization") -> object:
        from .stratification import dual_graph_boundary_poset

        return dual_graph_boundary_poset(self, order=order)

    def _repr_(self) -> str:
        return f"Boundary({self.ambient_space()!r})"


class CoarseModuliMorphism(StackMorphism):
    def __init__(self, stack: Stack, space: AlgebraicSpace) -> None:
        self._stack = stack
        self._space = space
        StackMorphism.__init__(self, stack, space, kind="coarse_moduli")

    def stack(self) -> Stack:
        return self._stack

    def space(self) -> AlgebraicSpace:
        return self._space
