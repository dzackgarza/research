r"""Moduli problems, moduli stacks, and concrete M_{g,I} / Mbar_{g,I}."""

from __future__ import annotations

from sage.rings.integer_ring import ZZ
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme, check_z_scheme, spec
from ..categories.stacks import DeligneMumfordStacks, ModuliStacks
from ..categories.schemes import AlgebraicSpaces, Varieties
from ..geometry.stacks import (
    AlgebraicSpace,
    Boundary,
    CoarseModuliMorphism,
    Compactification,
    Compactifications,
    DeligneMumfordStack,
    StackFiber,
    Variety,
)


def _marking_set(I: object) -> tuple[object, ...]:
    from sage.rings.integer import Integer

    if isinstance(I, (int, Integer)):
        return tuple(range(1, int(I) + 1))
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
            return self._family_factory()
        return f"object of {self._name}"

    def _repr_(self) -> str:
        return self._name


class ModuliProblem(UniqueRepresentation):
    r"""Contravariant pseudofunctor-shaped moduli problem to groupoids."""

    @staticmethod
    def __classcall_private__(
        cls,
        g: int,
        I: object,
        base: AffineScheme,
        *,
        stable: bool = False,
    ) -> ModuliProblem:
        return super().__classcall__(cls, int(g), _marking_set(I), base, stable=bool(stable))

    def __init__(self, g: int, I: tuple[object, ...], base: AffineScheme, *, stable: bool = False) -> None:
        self._g = int(g)
        self._I = tuple(I)
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


class ModuliStack(DeligneMumfordStack):
    r"""Stack equipped with a moduli problem."""

    @staticmethod
    def __classcall_private__(
        cls,
        problem: ModuliProblem,
        *,
        proper: bool = False,
        name: str | None = None,
    ) -> ModuliStack:
        proper = bool(proper)
        if name is None:
            name = ("Mbar" if proper else "M") + f"_{problem.genus()},{problem.number_of_markings()}"
        return super().__classcall__(cls, problem, proper=proper, name=name)

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

    def coarse_space(self) -> Variety | AlgebraicSpace:
        axioms = frozenset({"FiniteType", "Separated"})
        g, I = self.genus(), self.marking_set()
        if self._proper:
            axioms = axioms | {"Proper", "Normal", "Projective"}
            space: Variety | AlgebraicSpace = Variety(
                self.base_scheme(), name=f"coarse({self!r})", axioms=axioms
            )
        else:
            space = Variety(
                self.base_scheme(),
                name=f"coarse({self!r})",
                axioms=axioms | frozenset({"Integral"}),
            )
        # Preserve moduli type so coarse boundary posets recover dual-graph indexing.
        space._moduli_genus = g  # type: ignore[attr-defined]
        space._moduli_markings = I  # type: ignore[attr-defined]
        space.genus = lambda: g  # type: ignore[method-assign]
        space.number_of_markings = lambda: len(I)  # type: ignore[method-assign]
        space.marking_set = lambda: I  # type: ignore[method-assign]
        return space

    def coarse_moduli_morphism(self) -> CoarseModuliMorphism:
        space = self.coarse_space()
        return CoarseModuliMorphism(self, space)  # type: ignore[arg-type]

    def compactification(self, kind: str = "stable-pointed-curves") -> Compactification:
        if self._proper:
            raise ValueError("already proper; compactification is the identity immersion")
        target = Mbar_gI(self.genus(), self.marking_set(), base=self.base_scheme())
        return Compactification(self, target, kind=kind)

    def compactify(self, kind: str = "stable-pointed-curves") -> ModuliStack:
        return self.compactification(kind=kind).target()  # type: ignore[return-value]

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
        cached = getattr(self, "_cached_dual_graph_stratification", None)
        if cached is not None:
            return cached
        cached = build_dual_graph_stratification(self, compact=self._proper)
        self._cached_dual_graph_stratification = cached
        return cached

    def stratification(self, by: object | None = None) -> object:
        return self.stratify(by=by)

    def __call__(self, T: object) -> StackFiber:
        fiber = StackFiber(self, T)
        groupoid = self.objects_over(T)
        fiber._groupoid = groupoid  # type: ignore[attr-defined]

        def _an_element() -> object:
            return groupoid.an_element()

        fiber.an_element = _an_element  # type: ignore[method-assign]
        return fiber


def M_gI(g: int, I: object, base: AffineScheme | None = None) -> ModuliStack:
    base = base if base is not None else spec(ZZ)
    check_z_scheme(base)
    problem = ModuliProblem(g, I, base, stable=False)
    return ModuliStack(problem, proper=False)


def Mbar_gI(g: int, I: object, base: AffineScheme | None = None) -> ModuliStack:
    base = base if base is not None else spec(ZZ)
    check_z_scheme(base)
    problem = ModuliProblem(g, I, base, stable=True)
    return ModuliStack(problem, proper=True)


def M_gn(g: int, n: int, base: AffineScheme | None = None) -> ModuliStack:
    return M_gI(g, n, base=base)


def Mbar_gn(g: int, n: int, base: AffineScheme | None = None) -> ModuliStack:
    return Mbar_gI(g, n, base=base)
