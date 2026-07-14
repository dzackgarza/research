r"""Core geometric parents: stacks, immersions, compactifications, quotients.

Theorem-backed formal geometry: constructors establish category membership and
axioms; atlases/diagonals are formal morphisms with correct Hom membership.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme
from ..categories.schemes import AlgebraicSpaces, Varieties
from ..categories.stacks import (
    AlgebraicStacks,
    DeligneMumfordStacks,
    Stacks,
)
from ..categories.stratified import StratifiedSpaces, StratifiedStacks

if TYPE_CHECKING:
    # Stacks use ``__call__(T)`` for fibers (parents), not element conversion.
    _GeometricParent = Parent[object]
else:
    _GeometricParent = Parent


class GeometricObject(UniqueRepresentation, _GeometricParent):
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

    def __call__(self, x: object = None, *args: object, **kwds: object) -> StackFiber:
        assert x is not None and not args and not kwds, f"Stack() expects a single test object T; found T={x!r} args={args!r} kwds={kwds!r}; owned boundary=Stack.__call__"
        return self.fiber(x)

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

    Element: type[StackObject]

    def __init__(self, stack: Stack, test_object: object) -> None:
        from sage.categories.sets_cat import Sets

        self._stack = stack
        self._T = test_object
        Parent.__init__(self, category=Sets())

    def stack(self) -> Stack:
        return self._stack

    def base(self) -> object:
        return self._T

    def _element_constructor_(self, x: object = None) -> StackObject:
        if isinstance(x, StackObject):
            if x.parent() is self:
                return x
            raise ValueError(f"{x!r} is not an object of {self!r}")
        if x is None:
            return cast(StackObject, self.element_class(self))
        raise TypeError(f"cannot construct a stack object from {type(x).__name__}")

    def an_element(self) -> object:
        return cast(StackObject, self())

    def _repr_(self) -> str:
        return f"{self._stack!r}({self._T!r})"


class StackObject(Element):
    def __init__(self, parent: StackFiber) -> None:
        Element.__init__(self, parent)

    def _repr_(self) -> str:
        return f"Object of {self.parent()}"


StackFiber.Element = StackObject


class StackObjectIsomorphism(Element):
    def __init__(self, parent: object, source: StackObject, target: StackObject) -> None:
        self._source = source
        self._target = target
        Element.__init__(self, cast(Parent, parent))


class StackHomset(UniqueRepresentation, Parent):
    r"""Hom-set parent ``Hom(X, Y)`` of stack morphisms."""

    Element: type[StackMorphism]

    def __init__(self, domain: object, codomain: object) -> None:
        from sage.categories.homsets import Homsets

        self._domain = domain
        self._codomain = codomain
        Parent.__init__(self, category=Homsets())

    def domain(self) -> object:
        return self._domain

    def codomain(self) -> object:
        return self._codomain

    def _element_constructor_(self, x: object = None, **kwds: object) -> StackMorphism:
        if isinstance(x, StackMorphism):
            if x.domain() is self._domain and x.codomain() is self._codomain:
                return x
            raise ValueError(f"{x!r} is not a morphism in {self!r}")
        kind = kwds.pop("kind", None)
        if kwds:
            raise TypeError(f"unexpected keyword arguments {sorted(kwds)!r}")
        if kind is None:
            if x is None:
                kind = "morphism"
            else:
                raise TypeError(f"StackHomset() requires kind=... or an existing StackMorphism; got positional data of type {type(x).__name__}")
        return StackMorphism(self._domain, self._codomain, kind=str(kind))

    def an_element(self) -> StackMorphism:
        return cast(StackMorphism, self(kind="morphism"))

    def _repr_(self) -> str:
        return f"Hom({self._domain!r}, {self._codomain!r})"

    def __contains__(self, morph: object) -> bool:
        return isinstance(morph, StackMorphism) and morph.domain() is self._domain and morph.codomain() is self._codomain


class StackMorphism(Element):
    def __init__(self, domain: object, codomain: object, *, kind: str) -> None:
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


StackHomset.Element = StackMorphism


class Stack2Isomorphism(Element):
    def __init__(self, parent: object, f: StackMorphism, g: StackMorphism) -> None:
        self._f = f
        self._g = g
        Element.__init__(self, cast(Parent, parent))


class OpenImmersion(StackMorphism):
    def __init__(self, domain: object, codomain: object) -> None:
        StackMorphism.__init__(self, domain, codomain, kind="open_immersion")


class ClosedImmersion(StackMorphism):
    def __init__(self, domain: object, codomain: object) -> None:
        StackMorphism.__init__(self, domain, codomain, kind="closed_immersion")


class LocallyClosedImmersion(StackMorphism):
    def __init__(self, domain: object, codomain: object) -> None:
        StackMorphism.__init__(self, domain, codomain, kind="locally_closed_immersion")


class OpenSubstack(Stack):
    r"""Open substack of an ambient stack via an open immersion."""

    def __init__(self, ambient: Stack, underlying: Stack, immersion: OpenImmersion | None = None) -> None:
        self._ambient = ambient
        self._underlying = underlying
        self._immersion = immersion or OpenImmersion(underlying, ambient)
        Stack.__init__(
            self,
            ambient.base_scheme(),
            name=f"OpenSubstack({underlying!r} ⊂ {ambient!r})",
            axioms=underlying.declared_axioms(),
            category=ambient.category(),
        )

    def ambient(self) -> Stack:
        return self._ambient

    def underlying_stack(self) -> Stack:
        return self._underlying

    def immersion(self) -> OpenImmersion:
        return self._immersion


class ClosedSubstack(Stack):
    def __init__(self, ambient: Stack, underlying: Stack, immersion: ClosedImmersion | None = None) -> None:
        self._ambient = ambient
        self._underlying = underlying
        self._immersion = immersion or ClosedImmersion(underlying, ambient)
        Stack.__init__(
            self,
            ambient.base_scheme(),
            name=f"ClosedSubstack({underlying!r} ⊂ {ambient!r})",
            axioms=underlying.declared_axioms(),
            category=ambient.category(),
        )

    def ambient(self) -> Stack:
        return self._ambient

    def underlying_stack(self) -> Stack:
        return self._underlying

    def immersion(self) -> ClosedImmersion:
        return self._immersion


class LocallyClosedSubstack(Stack):
    def __init__(
        self,
        ambient: Stack,
        underlying: Stack,
        immersion: LocallyClosedImmersion | None = None,
    ) -> None:
        self._ambient = ambient
        self._underlying = underlying
        self._immersion = immersion or LocallyClosedImmersion(underlying, ambient)
        Stack.__init__(
            self,
            ambient.base_scheme(),
            name=f"LocallyClosedSubstack({underlying!r} ⊂ {ambient!r})",
            axioms=underlying.declared_axioms(),
            category=ambient.category(),
        )

    def ambient(self) -> Stack:
        return self._ambient

    def underlying_stack(self) -> Stack:
        return self._underlying

    def immersion(self) -> LocallyClosedImmersion:
        return self._immersion


class LocallyClosedSubstacks(UniqueRepresentation, Parent):
    r"""Parent of locally closed substacks of an ambient stack ``X``."""

    def __init__(self, ambient: Stack) -> None:
        from sage.categories.sets_cat import Sets

        self._ambient = ambient
        Parent.__init__(self, category=Sets())

    def ambient(self) -> Stack:
        return self._ambient

    def _element_constructor_(
        self,
        underlying: object,
        immersion: LocallyClosedImmersion | None = None,
    ) -> LocallyClosedSubstack:
        if isinstance(underlying, LocallyClosedSubstack):
            if underlying.ambient() is self._ambient:
                return underlying
            raise ValueError(f"{underlying!r} is not a locally closed substack of {self._ambient!r}")
        from .stratification import Stratum

        if isinstance(underlying, Stratum):
            if underlying.stratification().space() is not self._ambient:
                raise ValueError(f"{underlying!r} is not a stratum of {self._ambient!r}")
            return underlying.as_substack()
        if not isinstance(underlying, Stack):
            raise TypeError(f"expected Stack, LocallyClosedSubstack, or Stratum; found {type(underlying)!r}")
        return LocallyClosedSubstack(self._ambient, underlying, immersion=immersion)

    def __contains__(self, obj: object) -> bool:
        if isinstance(obj, LocallyClosedSubstack):
            return obj.ambient() is self._ambient
        # Geometric strata of ``ambient`` are locally closed substacks.
        from .stratification import Stratum

        if isinstance(obj, Stratum):
            return obj.stratification().space() is self._ambient
        return False

    def _repr_(self) -> str:
        return f"LocallyClosedSubstacks({self._ambient!r})"


class OpenSubspace(AlgebraicSpace):
    def __init__(self, ambient: AlgebraicSpace, underlying: AlgebraicSpace) -> None:
        self._ambient = ambient
        self._underlying = underlying
        AlgebraicSpace.__init__(
            self,
            ambient.base_scheme(),
            name=f"OpenSubspace({underlying!r})",
            axioms=underlying.declared_axioms(),
        )

    def ambient(self) -> AlgebraicSpace:
        return self._ambient

    def underlying_space(self) -> AlgebraicSpace:
        return self._underlying


class ClosedSubspace(AlgebraicSpace):
    def __init__(self, ambient: AlgebraicSpace, underlying: AlgebraicSpace) -> None:
        self._ambient = ambient
        self._underlying = underlying
        AlgebraicSpace.__init__(
            self,
            ambient.base_scheme(),
            name=f"ClosedSubspace({underlying!r})",
            axioms=underlying.declared_axioms(),
        )

    def ambient(self) -> AlgebraicSpace:
        return self._ambient

    def underlying_space(self) -> AlgebraicSpace:
        return self._underlying


class LocallyClosedSubspace(AlgebraicSpace):
    def __init__(self, ambient: AlgebraicSpace, underlying: AlgebraicSpace) -> None:
        self._ambient = ambient
        self._underlying = underlying
        AlgebraicSpace.__init__(
            self,
            ambient.base_scheme(),
            name=f"LocallyClosedSubspace({underlying!r})",
            axioms=underlying.declared_axioms(),
        )

    def ambient(self) -> AlgebraicSpace:
        return self._ambient

    def underlying_space(self) -> AlgebraicSpace:
        return self._underlying


class ProductStack(DeligneMumfordStack):
    @staticmethod
    def __classcall_private__(cls: type, *args: object, **kwargs: object) -> ProductStack:
        assert len(args) == 1, f"ProductStack(factors, *, base=None); found args={args!r}"
        factors = args[0]
        base = kwargs.pop("base", None)
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        assert isinstance(factors, (tuple, list)), f"factors must be a sequence of stacks; found {type(factors)!r}"
        factors_t = tuple(factors)
        result = UniqueRepresentation.__classcall__(cls, factors_t, base=base)
        assert isinstance(result, ProductStack), f"classcall must return ProductStack; found {type(result)!r}"
        return result

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
    r"""Quotient stack ``[space / group]``.

    Uniqueness is by ``(space, group)``. The Sage ``Action`` is stored but not
    part of the ``UniqueRepresentation`` key: ephemeral action wrappers rebuilt
    on each call must not fracture presentation identity.
    """

    @staticmethod
    def __classcall_private__(cls: type, *args: object, **kwargs: object) -> QuotientStack:
        assert len(args) >= 2, f"QuotientStack(space, group, action=None); found args={args!r}"
        space, group = args[0], args[1]
        action = args[2] if len(args) > 2 else kwargs.pop("action", None)
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        assert isinstance(space, Stack), f"expected Stack; found {type(space)!r}"
        obj = UniqueRepresentation.__classcall__(cls, space, group)
        assert isinstance(obj, QuotientStack), f"classcall must return QuotientStack; found {type(obj)!r}"
        if action is not None:
            obj._action = action
        return obj

    def __init__(self, space: Stack, group: object, action: object | None = None) -> None:
        self._space = space
        self._group = group
        self._action: object | None = action
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

    def action(self) -> object | None:
        return self._action


class Compactifications(UniqueRepresentation, Parent):
    r"""Parent of compactifications of a fixed open object ``X``.

    Elements are equipped open immersions `j: X ↪ X̄` with proper target
    (Stacks Project 0F44). The Sage parent of each element is this
    :class:`Compactifications` instance; the underlying open immersion is
    recovered by :meth:`Compactification.open_immersion` and lives in
    ``Hom(X, X̄)``.
    """

    Element: type[Compactification]

    def __init__(self, source: object) -> None:
        from sage.categories.sets_cat import Sets

        self._source = source
        Parent.__init__(self, category=Sets())

    def source(self) -> object:
        return self._source

    def _element_constructor_(
        self,
        target: object,
        moduli_problem: object | None = None,
        kind: str = "compactification",
        open_immersion: OpenImmersion | None = None,
    ) -> Compactification:
        if isinstance(target, Compactification):
            assert target.source() is self._source, f"cannot re-parent compactification of {target.source()!r} into {self!r}"
            return target
        return cast(
            Compactification,
            self.element_class(
                self,
                target,
                moduli_problem=moduli_problem,
                kind=kind,
                open_immersion=open_immersion,
            ),
        )

    def __contains__(self, obj: object) -> bool:
        return isinstance(obj, Compactification) and obj.parent() is self

    def _repr_(self) -> str:
        return f"Compactifications({self._source!r})"


class Compactification(Element):
    r"""Compactification `j: X ↪ X̄`: equipped open immersion with proper target.

    Construct via ``Compactifications(X)(Xbar)``.
    """

    def __init__(
        self,
        parent: Compactifications,
        target: object,
        moduli_problem: object | None = None,
        *,
        kind: str = "compactification",
        open_immersion: OpenImmersion | None = None,
    ) -> None:
        assert hasattr(target, "is_proper"), f"compactification target must expose is_proper(); found {type(target)!r}; owned boundary=Compactification.__init__"
        if not target.is_proper():
            raise ValueError("compactification target must be proper over the base")
        self._kind_name = kind
        self._moduli_problem = moduli_problem
        immersion = open_immersion if open_immersion is not None else OpenImmersion(parent.source(), target)
        assert immersion.domain() is parent.source(), f"open immersion domain must be parent.source(); found {immersion.domain()!r}"
        assert immersion.codomain() is target, f"open immersion codomain must be the compactification target; found {immersion.codomain()!r}"
        self._immersion = immersion
        Element.__init__(self, parent)

    def open_immersion(self) -> OpenImmersion:
        return self._immersion

    def is_open_immersion(self) -> bool:
        return True

    def source(self) -> object:
        return self._immersion.domain()

    def target(self) -> GeometricObject:
        target = self._immersion.codomain()
        assert isinstance(target, GeometricObject), f"compactification target must be GeometricObject; found {type(target)!r}; owned boundary=Compactification.target"
        return target

    def domain(self) -> object:
        return self.source()

    def codomain(self) -> object:
        return self.target()

    def moduli_problem(self) -> object:
        assert self._moduli_problem is not None, f"compactification has no moduli_problem; kind={self._kind_name!r}; owned boundary=Compactification.moduli_problem"
        return self._moduli_problem

    def boundary(self, reduced: bool = True) -> Boundary:
        return Boundary(self, reduced=reduced)

    def coarse_compactification(self) -> Compactification:
        r"""Coarse-space compactification commuting with coarse moduli morphisms.

        If ``j: X ↪ X̄`` is this compactification and ``π``, ``π̄`` are the coarse
        moduli morphisms of source and target, the returned ``j_c: X_c ↪ X̄_c``
        satisfies ``j_c.source() is π.space()`` and ``j_c.target() is π̄.space()``,
        so the formal square ``π̄ ∘ j = j_c ∘ π`` has matching corners.
        """
        source = self.source()
        target = self.target()
        if hasattr(source, "coarse_moduli_morphism") and hasattr(target, "coarse_moduli_morphism"):
            pi = source.coarse_moduli_morphism()
            pi_bar = target.coarse_moduli_morphism()
            coarse_source = pi.space()
            coarse_target = pi_bar.space()
            if not coarse_target.is_proper():
                raise ValueError("coarse compactification target must be proper")
            return cast(
                Compactification,
                Compactifications(coarse_source)(coarse_target, kind=f"coarse({self._kind_name})"),
            )
        if hasattr(source, "coarse_space") and hasattr(target, "coarse_space"):
            coarse_source = source.coarse_space()
            coarse_target = target.coarse_space()
            if not coarse_target.is_proper():
                raise ValueError("coarse compactification target must be proper")
            return cast(
                Compactification,
                Compactifications(coarse_source)(coarse_target, kind=f"coarse({self._kind_name})"),
            )
        raise TypeError("coarse_compactification requires moduli stacks with coarse_space()")

    def coarse_moduli_square_commutes(self) -> bool:
        r"""True when ``coarse_compactification`` matches ``coarse_moduli_morphism`` corners."""
        source = self.source()
        target = self.target()
        if not (hasattr(source, "coarse_moduli_morphism") and hasattr(target, "coarse_moduli_morphism")):
            return False
        pi = source.coarse_moduli_morphism()
        pi_bar = target.coarse_moduli_morphism()
        j_c = self.coarse_compactification()
        return (
            pi.domain() is source
            and pi_bar.domain() is target
            and j_c.source() is pi.space()
            and j_c.target() is pi_bar.space()
            and j_c.domain() is pi.codomain()
            and j_c.codomain() is pi_bar.codomain()
        )

    def _repr_(self) -> str:
        return f"Compactification({self.source()!r} ↪ {self.target()!r})"


# Forward Element class assignment (Sage Parent.element_class).
Compactifications.Element = Compactification


class Boundary(GeometricObject):
    r"""Closed complement of a compactification open immersion."""

    def __init__(self, compactification: Compactification, *, reduced: bool = True) -> None:
        self._compactification = compactification
        self._reduced = reduced
        ambient = compactification.target()
        assert hasattr(ambient, "base_scheme") and hasattr(ambient, "declared_axioms"), (
            f"compactification target must expose base_scheme/declared_axioms; found {type(ambient)!r}; owned boundary=Boundary.__init__"
        )
        base = ambient.base_scheme()
        assert isinstance(base, AffineScheme), f"base_scheme() must return AffineScheme; found {type(base)!r}"
        # Stack-level compactifications live in StratifiedStacks; coarse spaces in StratifiedSpaces.
        if isinstance(ambient, AlgebraicSpace) and not hasattr(ambient, "moduli_problem"):
            cat: object = StratifiedSpaces(base)
        else:
            cat = StratifiedStacks(base)
        axioms = ambient.declared_axioms()
        assert isinstance(axioms, frozenset), f"declared_axioms() must return frozenset; found {type(axioms)!r}"
        for a in sorted(axioms):
            if hasattr(cat, a):
                cat = getattr(cat, a)()
        GeometricObject.__init__(self, base, category=cat, axioms=axioms)

    def compactification(self) -> Compactification:
        return self._compactification

    def ambient_space(self) -> object:
        return self._compactification.target()

    def as_stack(self) -> Stack:
        r"""Stack presentation of this closed complement for stratification strata."""
        return Stack(
            self.base_scheme(),
            name=f"Boundary({self.ambient_space()!r})",
            axioms=self.declared_axioms(),
        )

    def open_complement(self) -> object:
        return self._compactification.source()

    def closed_immersion(self) -> ClosedImmersion:
        return ClosedImmersion(self, self.ambient_space())

    def underlying_space(self) -> Boundary:
        return self

    def stratification(self, by: object | None = None) -> object:
        from .stratification import build_dual_graph_stratification

        ambient = self.ambient_space()
        if hasattr(ambient, "stratification"):
            full = ambient.stratification(by=by)
            return full.restrict(self)
        assert isinstance(ambient, Stack), f"boundary ambient for dual-graph stratification must be Stack; found {type(ambient)!r}; owned boundary=Boundary.stratification"
        return build_dual_graph_stratification(ambient).restrict(self)

    def stratification_poset(self, order: str = "specialization") -> object:
        r"""Boundary strata poset of the dual-graph stratification of this boundary.

        Owned by the equipped boundary (not by an arbitrary proper space). Uses the
        Γ thinification with the open stratum removed — the combinatorial model of
        the closed complement of the open immersion defining this boundary.
        """
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
