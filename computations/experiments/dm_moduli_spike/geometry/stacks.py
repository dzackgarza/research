r"""Core geometric parents: stacks, immersions, compactifications, quotients.

Theorem-backed formal geometry: constructors establish category membership and
axioms. Atlases are morphisms from a scheme/algebraic space into the stack
(never self-maps). Base change returns a structured :class:`BaseChangeStack`.
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

    def pullback(self, f: object) -> BaseChangeStack:
        r"""Base change of this stack along a morphism of bases.

        Returns a structured :class:`BaseChangeStack` recording ``f``, the
        original stack, and the projection — not ``self`` and not a nameless
        formal shell. Full 2-categorical pullback coherence waits on PR #225.
        """
        return BaseChangeStack(self, f)

    def fiber_product(self, other: Stack, *, over: object | None = None) -> Stack:
        r"""Formal fiber product ``self ×_S other`` (theorem-backed parent)."""
        base = over if over is not None else self.base_scheme()
        if not isinstance(base, AffineScheme):
            if hasattr(base, "base_scheme"):
                base = base.base_scheme()
        assert isinstance(base, AffineScheme), f"fiber_product requires AffineScheme base; found {type(base)!r}"
        return Stack(
            base,
            name=f"FiberProduct({self!r}, {other!r})",
            axioms=self.declared_axioms() & other.declared_axioms(),
            category=self.category(),
        )

    def _Hom_(self, other: object, category: object = None) -> StackHomset:
        return StackHomset(self, other)

    def _repr_(self) -> str:
        return self._name


class BaseChangeStack(Stack):
    r"""Stack obtained by base change of ``original`` along ``base_morphism``.

    Records the original stack, the base morphism, and both legs of the
    base-change square:

    - ``π₁: X ×_S S' → X`` (projection to the original),
    - ``π₂: X ×_S S' → S'`` (structure map to the new base).

    Structural equality is UniqueRepresentation on ``(original, base_morphism)``.
    Full 2-categorical pullback coherence (universal property of the square)
    waits on PR #225.
    """

    @staticmethod
    def __classcall_private__(cls: type, original: Stack, base_morphism: object) -> BaseChangeStack:
        assert isinstance(original, Stack), f"BaseChangeStack requires Stack; found {type(original)!r}"
        # Moduli stacks get a moduli-aware base change preserving (g, I, problem class).
        from ..moduli.instances import ModuliStack

        if cls is BaseChangeStack and isinstance(original, ModuliStack):
            return ModuliBaseChangeStack(original, base_morphism)
        result = UniqueRepresentation.__classcall__(cls, original, base_morphism)
        assert isinstance(result, BaseChangeStack), f"classcall must return BaseChangeStack; found {type(result)!r}"
        return result

    def __init__(self, original: Stack, base_morphism: object) -> None:
        self._original = original
        self._base_morphism = base_morphism
        self._cached_projection: StackMorphism | None = None
        self._cached_to_new_base: StackMorphism | None = None
        new_base = _base_scheme_along(base_morphism, original.base_scheme())
        axioms = original.declared_axioms()
        cat: object = original.category()
        Stack.__init__(
            self,
            new_base,
            name=f"BaseChange({original!r})",
            axioms=axioms,
            category=cat,
        )

    def original_stack(self) -> Stack:
        return self._original

    def base_morphism(self) -> object:
        return self._base_morphism

    def new_base(self) -> AffineScheme:
        return self.base_scheme()

    def projection(self) -> StackMorphism:
        r"""First leg ``π₁: X_{S'} → X`` of the base-change square."""
        cached = self._cached_projection
        if cached is None:
            cached = StackMorphism(self, self._original, kind="base_change_projection")
            self._cached_projection = cached
        return cached

    def structure_morphism_to_new_base(self) -> StackMorphism:
        r"""Second leg ``π₂: X_{S'} → S'`` — structure map of the base-changed stack."""
        cached = self._cached_to_new_base
        if cached is None:
            cached = StackMorphism(self, self.base_scheme(), kind="structure_morphism_to_new_base")
            self._cached_to_new_base = cached
        return cached

    def pullback_of_structure_morphism(self) -> StackMorphism:
        r"""Alias for the second leg (pullback of ``X → S`` along ``S' → S``)."""
        return self.structure_morphism_to_new_base()

    def projections(self) -> tuple[StackMorphism, ...]:
        r"""Both legs ``(π₁: X' → X, π₂: X' → S')`` of the base-change square."""
        return (self.projection(), self.structure_morphism_to_new_base())

    def structure_map(self) -> StackMorphism:
        return self.projection()

    def square_corners(self) -> tuple[object, object, object, object]:
        r"""Corners ``(X', X, S', S)`` of the base-change square."""
        old_base = self._original.base_scheme()
        return (self, self._original, self.base_scheme(), old_base)


# Acceptance / literature name for the structured base-change object.
PullbackStack = BaseChangeStack


class ModuliBaseChangeStack(BaseChangeStack):
    r"""Base change of a :class:`~dm_moduli_spike.moduli.instances.ModuliStack`.

    Preserves genus, markings, and moduli-problem class over the new base.
    Not the identity and not a nameless shell.
    """

    @staticmethod
    def __classcall_private__(cls: type, original: Stack, base_morphism: object) -> ModuliBaseChangeStack:
        from ..moduli.instances import ModuliStack

        assert isinstance(original, ModuliStack), f"ModuliBaseChangeStack requires ModuliStack; found {type(original)!r}"
        result = UniqueRepresentation.__classcall__(cls, original, base_morphism)
        assert isinstance(result, ModuliBaseChangeStack), f"classcall must return ModuliBaseChangeStack; found {type(result)!r}"
        return result

    def __init__(self, original: Stack, base_morphism: object) -> None:
        from ..moduli.instances import ModuliStack

        assert isinstance(original, ModuliStack), f"ModuliBaseChangeStack requires ModuliStack; found {type(original)!r}"
        self._original = original
        self._base_morphism = base_morphism
        self._cached_projection = None
        self._cached_to_new_base = None
        new_base = _base_scheme_along(base_morphism, original.base_scheme())
        problem = original.moduli_problem()
        problem_cls = type(problem)
        self._base_changed_problem = problem_cls(problem.genus(), problem.marking_set(), new_base)
        axioms = original.declared_axioms()
        from sage.categories.category import Category

        from ..categories.stacks import DeligneMumfordStacks, ModuliStacks

        join = getattr(Category, "join")
        cat = join((ModuliStacks(new_base), DeligneMumfordStacks(new_base)))
        for a in sorted(axioms):
            if hasattr(cat, a):
                cat = getattr(cat, a)()
        Stack.__init__(
            self,
            new_base,
            name=f"BaseChange({original!r})",
            axioms=axioms,
            category=cat,
        )

    def moduli_problem(self) -> object:
        return self._base_changed_problem

    def genus(self) -> int:
        return int(self._base_changed_problem.genus())

    def number_of_markings(self) -> int:
        return int(self._base_changed_problem.number_of_markings())

    def marking_set(self) -> tuple[object, ...]:
        return tuple(self._base_changed_problem.marking_set())

    def original_moduli_stack(self) -> Stack:
        return self._original


def _base_scheme_along(base_morphism: object, fallback: AffineScheme) -> AffineScheme:
    r"""Infer the new base scheme from a base-change morphism when possible."""
    if isinstance(base_morphism, AffineScheme):
        return base_morphism
    if hasattr(base_morphism, "domain"):
        domain = base_morphism.domain()
        if isinstance(domain, AffineScheme):
            return domain
        if hasattr(domain, "base_scheme"):
            base = domain.base_scheme()
            if isinstance(base, AffineScheme):
                return base
    if hasattr(base_morphism, "base_scheme"):
        base = base_morphism.base_scheme()
        if isinstance(base, AffineScheme):
            return base
    return fallback


class AlgebraicStack(Stack):
    def __init__(self, base: AffineScheme, *, name: str = "AlgebraicStack", axioms: frozenset[str] | None = None) -> None:
        Stack.__init__(self, base, name=name, axioms=axioms, category=AlgebraicStacks(base))

    def diagonal(self) -> StackMorphism:
        r"""Diagonal ``Δ: X → X ×_S X`` (formal fiber-product codomain)."""
        return StackMorphism(self, self.fiber_product(self), kind="diagonal")

    def atlas_domain(self) -> AlgebraicSpace:
        r"""Scheme/algebraic-space domain of the atlas morphism ``U → X``.

        For moduli stacks with a coarse space, that coarse space is the atlas
        domain. Otherwise a dedicated :class:`AtlasChart` is used. Never ``self``.
        """
        if hasattr(self, "coarse_space"):
            space = self.coarse_space()
            assert isinstance(space, AlgebraicSpace), f"coarse_space() must return AlgebraicSpace; found {type(space)!r}"
            return space
        return AtlasChart(self, etale=False)

    def atlas(self) -> AtlasMorphism:
        r"""Atlas ``U → X`` with ``U`` a scheme/algebraic space, not ``X`` itself."""
        domain = self.atlas_domain()
        covering = "coarse_moduli" if hasattr(self, "coarse_space") and domain is self.coarse_space() else "atlas_chart"
        return AtlasMorphism(
            domain,
            self,
            etale=False,
            covering_kind=covering,
            representable_domain=isinstance(domain, AlgebraicSpace),
        )


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

    def etale_atlas(self) -> AtlasMorphism:
        r"""Étale atlas ``U → X`` with a scheme/algebraic-space domain distinct from ``X``.

        Uses a dedicated étale atlas chart — not the coarse moduli space (the
        coarse map ``X → X_c`` is not étale in general) and not a self-map.
        Étaleness is a DM theorem stamp with attached :class:`AtlasEvidence`
        (diagonal data), not an equation-level verification.
        """
        domain = AtlasChart(self, etale=True)
        return AtlasMorphism(
            domain,
            self,
            etale=True,
            covering_kind="etale_atlas_chart",
            representable_domain=True,
            evidence=AtlasEvidence.from_dm_stack(self, domain=domain, covering_kind="etale_atlas_chart"),
        )


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


class AtlasChart(AlgebraicSpace):
    r"""Algebraic-space chart serving as the domain of an atlas morphism ``U → X``.

    Distinct from the stack itself. For moduli stacks, :meth:`AlgebraicStack.atlas`
    prefers the coarse moduli space as atlas domain when available; this chart is
    the fallback for stacks without a coarse space, and the dedicated domain for
    :meth:`DeligneMumfordStack.etale_atlas` (never the coarse space).
    """

    @staticmethod
    def __classcall_private__(cls: type, stack: Stack, *, etale: bool = False) -> AtlasChart:
        result = UniqueRepresentation.__classcall__(cls, stack, etale)
        assert isinstance(result, AtlasChart), f"classcall must return AtlasChart; found {type(result)!r}"
        return result

    def __init__(self, stack: Stack, etale: bool = False) -> None:
        self._presented_stack = stack
        self._etale_chart = bool(etale)
        tag = "EtaleAtlasChart" if etale else "AtlasChart"
        AlgebraicSpace.__init__(
            self,
            stack.base_scheme(),
            name=f"{tag}({stack!r})",
            axioms=frozenset({"FiniteType", "Separated"}),
        )

    def presented_stack(self) -> Stack:
        return self._presented_stack

    def is_etale_chart(self) -> bool:
        return self._etale_chart


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
        return cast(StackObject, self.element_class(self))

    def isomorphism(self, source: StackObject, target: StackObject) -> StackObjectIsomorphism:
        r"""Formal isomorphism in this fiber groupoid between ``source`` and ``target``."""
        return StackObjectIsomorphism(self, source, target)

    def _repr_(self) -> str:
        return f"{self._stack!r}({self._T!r})"


class StackObject(Element):
    def __init__(self, parent: StackFiber) -> None:
        Element.__init__(self, parent)

    def _repr_(self) -> str:
        return f"Object of {self.parent()}"


StackFiber.Element = StackObject


class StackObjectIsomorphism(Element):
    r"""Isomorphism in a stack fiber groupoid ``X(T)`` between two objects.

    Formal certificate: domain/codomain objects live in the same
    :class:`StackFiber`. This is the 1-cell invertibility data inside the fiber,
    not an equation-level check of atlases.
    """

    def __init__(self, parent: StackFiber, source: StackObject, target: StackObject) -> None:
        if source.parent() is not parent or target.parent() is not parent:
            raise ValueError(f"fiber isomorphisms require objects of {parent!r}; found {source.parent()!r} and {target.parent()!r}")
        self._source = source
        self._target = target
        Element.__init__(self, parent)

    def source(self) -> StackObject:
        return self._source

    def target(self) -> StackObject:
        return self._target

    def _repr_(self) -> str:
        return f"StackObjectIsomorphism({self._source!r} ≃ {self._target!r})"


class Stack2Isomorphism:
    r"""2-isomorphism between parallel stack morphisms ``f, g: X → Y``.

    Stacks form a 2-category: 1-morphisms may be isomorphic without being equal.
    A 2-cell is **not** an element of the 1-Hom-set ``Hom(X,Y)``; it relates two
    1-morphisms. Full Hom-category structure waits on PR #225.
    """

    def __init__(self, f: StackMorphism, g: StackMorphism) -> None:
        if f.domain() is not g.domain() or f.codomain() is not g.codomain():
            raise ValueError(f"parallel 2-isomorphism requires shared domain/codomain; found {f!r} and {g!r}")
        if f.parent() is not g.parent():
            raise ValueError(f"2-isomorphisms require morphisms of the same Hom-set; found {f.parent()!r} and {g.parent()!r}")
        self._f = f
        self._g = g
        self._homset = f.parent()

    def source(self) -> StackMorphism:
        return self._f

    def target(self) -> StackMorphism:
        return self._g

    def hom_category(self) -> object:
        r"""The 1-Hom-set whose objects are related by this 2-cell."""
        return self._homset

    def _repr_(self) -> str:
        return f"Stack2Isomorphism({self._f!r} ⇒ {self._g!r})"


class StackHomset(UniqueRepresentation, Parent):
    r"""Hom-set parent ``Hom(X, Y)`` of stack **1**-morphisms only."""

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

    def isomorphism(self, f: StackMorphism, g: StackMorphism) -> Stack2Isomorphism:
        r"""Formal 2-isomorphism between parallel 1-morphisms (not a Hom-set element)."""
        return Stack2Isomorphism(f, g)

    def _repr_(self) -> str:
        return f"Hom({self._domain!r}, {self._codomain!r})"

    def __contains__(self, morph: object) -> bool:
        if isinstance(morph, StackMorphism):
            return morph.domain() is self._domain and morph.codomain() is self._codomain
        return False


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


class AtlasEvidence:
    r"""Inspectable evidence attached to an atlas morphism.

    Records covering/representability data and links to DM diagonal properties
    already claimed on the target stack. This is **not** an equation-level proof
    of étaleness — it is structured evidence tests can inspect when full
    verification is unfinished.
    """

    def __init__(
        self,
        *,
        stack: Stack,
        domain: object,
        covering_kind: str,
        etale_stamp: bool,
        representable_domain: bool,
        diagonal: StackMorphism | None,
        dm_diagonal_unramified_stamp: bool,
    ) -> None:
        self._stack = stack
        self._domain = domain
        self._covering_kind = covering_kind
        self._etale_stamp = bool(etale_stamp)
        self._representable_domain = bool(representable_domain)
        self._diagonal = diagonal
        self._dm_diagonal_unramified_stamp = bool(dm_diagonal_unramified_stamp)

    @staticmethod
    def from_dm_stack(stack: Stack, *, domain: object, covering_kind: str) -> AtlasEvidence:
        diagonal: StackMorphism | None = None
        dm_stamp = isinstance(stack, DeligneMumfordStack)
        if isinstance(stack, AlgebraicStack):
            diagonal = stack.diagonal()
        return AtlasEvidence(
            stack=stack,
            domain=domain,
            covering_kind=covering_kind,
            etale_stamp=True,
            representable_domain=isinstance(domain, AlgebraicSpace) or isinstance(domain, ProductStack),
            diagonal=diagonal,
            dm_diagonal_unramified_stamp=dm_stamp,
        )

    def stack(self) -> Stack:
        return self._stack

    def domain(self) -> object:
        return self._domain

    def covering_kind(self) -> str:
        return self._covering_kind

    def etale_stamp(self) -> bool:
        return self._etale_stamp

    def representable_domain(self) -> bool:
        return self._representable_domain

    def diagonal(self) -> StackMorphism | None:
        r"""Diagonal ``Δ: X → X ×_S X`` of the target, when the target is algebraic."""
        return self._diagonal

    def dm_diagonal_unramified_stamp(self) -> bool:
        r"""True when the target carries the DM stamp (unramified diagonal, theorem-level)."""
        return self._dm_diagonal_unramified_stamp

    def _repr_(self) -> str:
        return (
            f"AtlasEvidence(covering={self._covering_kind!r}, etale={self._etale_stamp}, "
            f"representable={self._representable_domain}, dm_diagonal={self._dm_diagonal_unramified_stamp})"
        )


class AtlasMorphism(StackMorphism):
    r"""Atlas morphism ``U → X`` from a scheme/algebraic space into a stack.

    Domain is never the stack itself. The ``etale`` flag is a theorem stamp for
    DM existence of an étale atlas — not a claim that the coarse moduli map is
    étale (it is not, in general). Covering/representability data and
    :class:`AtlasEvidence` are inspectable even when equation-level étaleness
    is unfinished.
    """

    def __init__(
        self,
        domain: object,
        codomain: object,
        *,
        etale: bool = False,
        covering_kind: str | None = None,
        representable_domain: bool | None = None,
        evidence: AtlasEvidence | None = None,
    ) -> None:
        if domain is codomain:
            raise ValueError(f"atlas domain must not be the stack itself; found domain=codomain={codomain!r}")
        self._etale = bool(etale)
        kind = "etale_atlas" if self._etale else "atlas"
        if covering_kind is None:
            covering_kind = "etale_atlas_chart" if self._etale else "atlas"
        self._covering_kind = covering_kind
        if representable_domain is None:
            representable_domain = isinstance(domain, AlgebraicSpace) or isinstance(domain, ProductStack)
        self._representable_domain = bool(representable_domain)
        if evidence is None and self._etale and isinstance(codomain, Stack):
            evidence = AtlasEvidence.from_dm_stack(codomain, domain=domain, covering_kind=self._covering_kind)
        self._evidence = evidence
        StackMorphism.__init__(self, domain, codomain, kind=kind)

    def is_etale(self) -> bool:
        return self._etale

    def is_atlas(self) -> bool:
        return True

    def covering_kind(self) -> str:
        r"""Named covering presentation: ``coarse_moduli``, ``etale_atlas_chart``, ``quotient_cover``, …"""
        return self._covering_kind

    def domain_is_representable(self) -> bool:
        r"""True when the atlas domain is an algebraic space / product of such (representable)."""
        return self._representable_domain

    def is_covering(self) -> bool:
        r"""True: atlas morphisms are covering maps by construction (theorem stamp)."""
        return True

    def evidence(self) -> AtlasEvidence | None:
        r"""Structured evidence (diagonal link, covering kind, representability); may be ``None`` for non-étale atlases."""
        return self._evidence

    def covering_data(self) -> dict[str, object]:
        r"""Inspectable covering/representability record for tests."""
        data: dict[str, object] = {
            "covering_kind": self._covering_kind,
            "etale": self._etale,
            "representable_domain": self._representable_domain,
            "domain": self.domain(),
            "codomain": self.codomain(),
            "is_covering": True,
        }
        if self._evidence is not None:
            data["dm_diagonal_unramified_stamp"] = self._evidence.dm_diagonal_unramified_stamp()
            data["diagonal"] = self._evidence.diagonal()
        return data


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


class ProductStack(Stack):
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
        axioms = frozenset.intersection(*(f.declared_axioms() for f in factors))
        all_dm = all(isinstance(f, DeligneMumfordStack) for f in factors)
        cat: object = DeligneMumfordStacks(base) if all_dm else Stacks(base)
        for a in sorted(axioms):
            if hasattr(cat, a):
                cat = getattr(cat, a)()
        Stack.__init__(
            self,
            base,
            name=f"ProductStack({len(factors)})",
            axioms=axioms,
            category=cat,
        )

    def factors(self) -> tuple[Stack, ...]:
        return self._factors

    def atlas_domain(self) -> AlgebraicSpace | ProductStack:
        r"""Product of coarse spaces of moduli factors when available; else an atlas chart."""
        coarse_factors: list[AlgebraicSpace] = []
        for factor in self._factors:
            if hasattr(factor, "coarse_space"):
                space = factor.coarse_space()
                assert isinstance(space, AlgebraicSpace), f"coarse_space() must return AlgebraicSpace; found {type(space)!r}"
                coarse_factors.append(space)
            else:
                return AtlasChart(self, etale=False)
        # Product of algebraic spaces as a ProductStack of AlgebraicSpace factors.
        return ProductStack(tuple(coarse_factors), base=self.base_scheme())

    def atlas(self) -> AtlasMorphism:
        domain = self.atlas_domain()
        return AtlasMorphism(
            domain,
            self,
            etale=False,
            covering_kind="product_of_coarse",
            representable_domain=True,
        )


class QuotientStack(Stack):
    r"""Quotient stack ``[space / group]`` determined by an action ``ρ``.

    When ``ρ`` exposes ``act`` / ``_act_`` (e.g. :class:`AutProductStackAction`),
    :meth:`act_on_covering` consumes that action. The étale atlas domain is the
    covering space (standard ``U → [U/G]``), not a self-map.
    """

    @staticmethod
    def __classcall_private__(cls: type, *args: object, **kwargs: object) -> QuotientStack:
        assert len(args) >= 3, f"QuotientStack(space, group, action) requires three arguments; found args={args!r}"
        space, group, action = args[0], args[1], args[2]
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        assert isinstance(space, Stack), f"expected Stack; found {type(space)!r}"
        if action is None:
            raise TypeError("QuotientStack requires a genuine group action; action=None is forbidden")
        obj = UniqueRepresentation.__classcall__(cls, space, group, action)
        assert isinstance(obj, QuotientStack), f"classcall must return QuotientStack; found {type(obj)!r}"
        return obj

    def __init__(self, space: Stack, group: object, action: object) -> None:
        if action is None:
            raise TypeError("QuotientStack requires a genuine group action; action=None is forbidden")
        self._space = space
        self._group = group
        self._action = action
        axioms = space.declared_axioms()
        base = space.base_scheme()
        cat: object = DeligneMumfordStacks(base) if isinstance(space, DeligneMumfordStack) else Stacks(base)
        for a in sorted(axioms):
            if hasattr(cat, a):
                cat = getattr(cat, a)()
        Stack.__init__(
            self,
            base,
            name=f"QuotientStack({space!r}/{group!r})",
            axioms=axioms,
            category=cat,
        )

    def space(self) -> Stack:
        return self._space

    def covering_product(self) -> Stack:
        return self._space

    def group(self) -> object:
        return self._group

    def action(self) -> object:
        return self._action

    def act_on_covering(self, group_element: object) -> Stack:
        r"""Apply the stored action to the covering space (consumes ``ρ`` meaningfully)."""
        action = self._action
        if hasattr(action, "act"):
            result = action.act(group_element)
            assert isinstance(result, Stack), f"action.act must return Stack; found {type(result)!r}"
            return result
        if hasattr(action, "_act_"):
            result = action._act_(group_element, self._space)
            assert isinstance(result, Stack), f"action._act_ must return Stack; found {type(result)!r}"
            return result
        raise TypeError(f"quotient action must expose act/_act_; found {type(action)!r}")

    def atlas_domain(self) -> Stack:
        r"""Covering space ``U`` of ``[U/G]`` — the natural atlas domain."""
        return self._space

    def atlas(self) -> AtlasMorphism:
        return AtlasMorphism(
            self._space,
            self,
            etale=False,
            covering_kind="quotient_cover",
            representable_domain=isinstance(self._space, (AlgebraicSpace, ProductStack)),
        )

    def etale_atlas(self) -> AtlasMorphism:
        r"""Étale atlas ``U → [U/G]`` with domain the covering space (not a self-map).

        Étaleness of ``U → [U/G]`` for finite group actions is a theorem stamp with
        attached :class:`AtlasEvidence`; equation-level verification unfinished.
        """
        domain = self._space
        representable = isinstance(domain, (AlgebraicSpace, ProductStack))
        dm = isinstance(domain, DeligneMumfordStack) or (isinstance(domain, ProductStack) and all(isinstance(f, DeligneMumfordStack) for f in domain.factors()))
        diagonal = StackMorphism(self, self.fiber_product(self), kind="diagonal") if dm else None
        return AtlasMorphism(
            domain,
            self,
            etale=True,
            covering_kind="quotient_cover",
            representable_domain=representable,
            evidence=AtlasEvidence(
                stack=self,
                domain=domain,
                covering_kind="quotient_cover",
                etale_stamp=True,
                representable_domain=representable,
                diagonal=diagonal,
                dm_diagonal_unramified_stamp=dm,
            ),
        )


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

    def boundary(self) -> Boundary:
        r"""Closed complement of this compactification's open immersion."""
        return Boundary(self)

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


class StratifiedSpace(GeometricObject):
    r"""Geometric space equipped with a finite stratification.

    Concrete objects in :class:`~dm_moduli_spike.categories.stratified.StratifiedSpaces`
    (boundaries, stratified schemes, …) inherit this type so stratification is part
    of the object, not a free-floating descriptor.
    """

    def stratification(self, by: object | None = None) -> object:
        raise NotImplementedError(f"{type(self).__name__}.stratification")

    def stratification_poset(self, order: str = "specialization") -> object:
        strat = self.stratification()
        assert hasattr(strat, "specialization_poset"), f"stratification must expose specialization_poset(); found {type(strat)!r}"
        poset = strat.specialization_poset()
        if order == "closure":
            return poset.dual()
        return poset

    def underlying_space(self) -> StratifiedSpace:
        return self


class Boundary(StratifiedSpace):
    r"""Closed complement of a compactification open immersion."""

    def __init__(self, compactification: Compactification) -> None:
        self._compactification = compactification
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
