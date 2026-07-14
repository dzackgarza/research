r"""Moduli problems, moduli stacks, and concrete M_{g,I} / Mbar_{g,I}."""

from __future__ import annotations

from sage.rings.integer_ring import ZZ
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme, check_z_scheme, spec
from ..categories.stacks import ModuliStacks
from ..geometry.stacks import (
    Boundary,
    CoarseModuliMorphism,
    Compactification,
    DeligneMumfordStack,
    StackFiber,
    Variety,
)


def _marking_set(I: object) -> tuple[object, ...]:
    from collections.abc import Iterable

    from sage.rings.integer import Integer

    if isinstance(I, (int, Integer)):
        return tuple(range(1, int(I) + 1))
    assert isinstance(I, Iterable), f"expected marking count or iterable; found {type(I)!r}"
    return tuple(I)


class Groupoid(UniqueRepresentation, Parent):
    r"""Finite formal groupoid (objects + isomorphisms) for moduli fibers."""

    def __init__(self, name: str = "Groupoid", *, family_factory: object | None = None) -> None:
        from sage.categories.sets_cat import Sets

        self._name = name
        self._family_factory = family_factory
        Parent.__init__(self, category=Sets())

    def an_element(self) -> object:
        if self._family_factory is not None:
            assert callable(self._family_factory), f"family_factory must be callable; found {type(self._family_factory)!r}"
            return self._family_factory()
        return f"object of {self._name}"

    def _repr_(self) -> str:
        return self._name


class ModuliProblem(UniqueRepresentation):
    r"""Contravariant pseudofunctor-shaped moduli problem to groupoids."""

    @staticmethod
    def __classcall_private__(cls: type[ModuliProblem], *args: object, **kwargs: object) -> ModuliProblem:
        from .._typing_utils import as_int

        assert len(args) >= 3, f"ModuliProblem(g, I, base, *, stable=False); found args={args!r}"
        g, I, base = args[0], args[1], args[2]
        stable = bool(kwargs.pop("stable", False))
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        assert isinstance(base, AffineScheme), f"expected AffineScheme; found {type(base)!r}"
        result = super().__classcall__(cls, as_int(g), _marking_set(I), base, stable=stable)
        assert isinstance(result, ModuliProblem), f"classcall must return ModuliProblem; found {type(result)!r}"
        return result

    def __init__(self, g: int, I: object, base: AffineScheme, *, stable: bool = False) -> None:
        from .._typing_utils import as_int

        self._g = as_int(g)
        self._I = _marking_set(I) if not isinstance(I, tuple) else tuple(I)
        self._base = base
        self._stable = bool(stable)

    def genus(self) -> int:
        return self._g

    def marking_set(self) -> tuple[object, ...]:
        return self._I

    def number_of_markings(self) -> int:
        return len(self._I)

    def base_scheme(self) -> AffineScheme:
        return self._base

    def objects_over(self, T: object) -> Groupoid:
        from ..curves.families import PointedCurveFamily, StablePointedCurveFamily

        kind = "stable" if self._stable else "smooth"
        g, I = self._g, self._I
        base = self._base
        stable = self._stable

        def _factory() -> object:
            sections = tuple(I)
            if stable:
                return StablePointedCurveFamily(base, T, sections, genus=g, marking_set=I)
            return PointedCurveFamily(base, T, sections, genus=g, marking_set=I, stable=False)

        return Groupoid(
            f"{kind} pointed curves of type ({self._g},{len(self._I)}) over {T!r}",
            family_factory=_factory,
        )

    def pullback(self, f: object) -> ModuliProblem:
        return self

    def _repr_(self) -> str:
        tag = "StablePointedCurves" if self._stable else "SmoothPointedCurves"
        return f"{tag}({self._g}, {len(self._I)})"


class CoarseModuliVariety(Variety):
    r"""Coarse space of a moduli stack, retaining combinatorial type ``(g, I)``."""

    def __init__(
        self,
        base: AffineScheme,
        *,
        genus: int,
        markings: tuple[object, ...],
        name: str,
        axioms: frozenset[str] | None = None,
    ) -> None:
        self._moduli_genus = int(genus)
        self._moduli_markings = tuple(markings)
        Variety.__init__(self, base, name=name, axioms=axioms)

    def genus(self) -> int:
        return self._moduli_genus

    def number_of_markings(self) -> int:
        return len(self._moduli_markings)

    def marking_set(self) -> tuple[object, ...]:
        return self._moduli_markings


class ModuliStackFiber(StackFiber):
    r"""Stack fiber with an attached moduli groupoid for ``an_element``."""

    def __init__(self, stack: ModuliStack, test_object: object, groupoid: Groupoid) -> None:
        self._groupoid = groupoid
        StackFiber.__init__(self, stack, test_object)

    def an_element(self) -> object:
        r"""A representative object of the moduli groupoid over the test object.

        Returns the concrete geometric object produced by the moduli problem
        (e.g. a pointed-curve family), not a bare :class:`StackObject` wrapper.
        """
        return self._groupoid.an_element()


class ModuliStack(DeligneMumfordStack):
    r"""Stack equipped with a moduli problem."""

    @staticmethod
    def __classcall_private__(cls: type[ModuliStack], *args: object, **kwargs: object) -> ModuliStack:
        assert len(args) == 1, f"ModuliStack(problem, *, proper=False, name=None); found args={args!r}"
        problem = args[0]
        proper = bool(kwargs.pop("proper", False))
        name = kwargs.pop("name", None)
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        assert isinstance(problem, ModuliProblem), f"expected ModuliProblem; found {type(problem)!r}"
        if name is None:
            name = ("Mbar" if proper else "M") + f"_{problem.genus()},{problem.number_of_markings()}"
        result = super().__classcall__(cls, problem, proper=proper, name=name)
        assert isinstance(result, ModuliStack), f"classcall must return ModuliStack; found {type(result)!r}"
        return result

    def __init__(
        self,
        problem: ModuliProblem,
        *,
        proper: bool = False,
        name: str | None = None,
    ) -> None:
        self._problem = problem
        self._proper = bool(proper)
        base = problem.base_scheme()
        axioms = frozenset({"Smooth", "FiniteType"})
        if self._proper:
            axioms = axioms | {"Proper"}
        cat = ModuliStacks(base)
        for a in sorted(axioms):
            cat = getattr(cat, a)()
        label = name or ("Mbar" if self._proper else "M") + f"_{problem.genus()},{problem.number_of_markings()}"
        from sage.structure.parent import Parent

        self._name = label
        self._base = base
        self._axioms = axioms
        self._cached_dual_graph_stratification: object | None = None
        Parent.__init__(self, category=cat)

    def moduli_problem(self) -> ModuliProblem:
        return self._problem

    def objects_over(self, T: object) -> Groupoid:
        return self._problem.objects_over(T)

    def genus(self) -> int:
        return self._problem.genus()

    def number_of_markings(self) -> int:
        return self._problem.number_of_markings()

    def marking_set(self) -> tuple[object, ...]:
        return self._problem.marking_set()

    def dimension(self) -> int:
        return 3 * self.genus() - 3 + self.number_of_markings()

    def coarse_space(self) -> CoarseModuliVariety:
        axioms = frozenset({"FiniteType", "Separated"})
        g, I = self.genus(), self.marking_set()
        if self._proper:
            axioms = axioms | {"Proper", "Normal", "Projective"}
        else:
            axioms = axioms | frozenset({"Integral"})
        return CoarseModuliVariety(
            self.base_scheme(),
            genus=g,
            markings=I,
            name=f"coarse({self!r})",
            axioms=axioms,
        )

    def coarse_moduli_morphism(self) -> CoarseModuliMorphism:
        space = self.coarse_space()
        return CoarseModuliMorphism(self, space)

    def compactification(self, kind: str = "stable-pointed-curves") -> Compactification:
        if self._proper:
            raise ValueError("already proper; compactification is the identity immersion")
        target = Mbar_gI(self.genus(), self.marking_set(), base=self.base_scheme())
        return Compactification(self, target, kind=kind)

    def compactify(self, kind: str = "stable-pointed-curves") -> ModuliStack:
        target = self.compactification(kind=kind).target()
        assert isinstance(target, ModuliStack), f"compactification target must be ModuliStack; found {type(target)!r}"
        return target

    def open_part(self) -> ModuliStack:
        if not self._proper:
            return self
        return M_gI(self.genus(), self.marking_set(), base=self.base_scheme())

    def open_immersion(self) -> Compactification:
        return self.open_part().compactification()

    def boundary(self) -> Boundary:
        if not self._proper:
            raise ValueError("boundary is relative to a compactification of the open moduli stack")
        c = self.open_part().compactification()
        return c.boundary()

    def stratify(self, by: object | None = None) -> object:
        r"""Return the dual-graph stratification of this stack.

        The stratification is a total property of the stack: repeated calls
        return the same object. Rebuilds must not produce unequal quotient
        presentations for the same stratum.
        """
        from ..geometry.stratification import StableDualGraph, build_dual_graph_stratification

        assert by is None or isinstance(by, StableDualGraph), (
            f"stratification indexer must be StableDualGraph (or omitted); found {by!r}; "
            "owned boundary=ModuliStack.stratify; "
            "use Mbar_gn(...).stratification() or stratification(by=StableDualGraph())"
        )
        cached = self._cached_dual_graph_stratification
        if cached is not None:
            return cached
        cached = build_dual_graph_stratification(self, compact=self._proper)
        self._cached_dual_graph_stratification = cached
        return cached

    def stratification(self, by: object | None = None) -> object:
        return self.stratify(by=by)

    def __call__(self, x: object = None, *args: object, **kwds: object) -> ModuliStackFiber:
        assert x is not None and not args and not kwds, (
            f"ModuliStack() expects a single test object T; found T={x!r} args={args!r} kwds={kwds!r}; owned boundary=ModuliStack.__call__"
        )
        return ModuliStackFiber(self, x, self.objects_over(x))


def M_gI(g: int, I: object, base: AffineScheme | None = None) -> ModuliStack:
    resolved = base if base is not None else spec(ZZ)
    check_z_scheme(resolved)
    problem = ModuliProblem(g, I, resolved, stable=False)
    return ModuliStack(problem, proper=False)


def Mbar_gI(g: int, I: object, base: AffineScheme | None = None) -> ModuliStack:
    resolved = base if base is not None else spec(ZZ)
    check_z_scheme(resolved)
    problem = ModuliProblem(g, I, resolved, stable=True)
    return ModuliStack(problem, proper=True)


def M_gn(g: int, n: int, base: AffineScheme | None = None) -> ModuliStack:
    return M_gI(g, n, base=base)


def Mbar_gn(g: int, n: int, base: AffineScheme | None = None) -> ModuliStack:
    return Mbar_gI(g, n, base=base)
