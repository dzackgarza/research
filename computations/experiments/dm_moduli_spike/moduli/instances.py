r"""Moduli problems, moduli stacks, and concrete M_{g,I} / Mbar_{g,I}."""

from __future__ import annotations

from sage.rings.integer_ring import ZZ
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme, check_z_scheme, spec
from ..categories.stacks import ModuliStacks
from ..geometry.stacks import (
    AffineAlgebraicSpace,
    AlgebraicSpace,
    AtlasEvidence,
    AtlasMorphism,
    Boundary,
    CoarseModuliMorphism,
    Compactification,
    DeligneMumfordStack,
    FormallyEtaleSchemeCertificate,
    StackFiber,
    Variety,
    _proving_set_etale_certificates,
)


def _marking_set(I: object) -> tuple[object, ...]:
    from collections.abc import Iterable

    from sage.rings.integer import Integer

    if isinstance(I, (int, Integer)):
        return tuple(range(1, int(I) + 1))
    assert isinstance(I, Iterable), f"expected marking count or iterable; found {type(I)!r}"
    return tuple(I)


def _cross_ratio_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Affine scheme ``Spec(R[t]_{t(t-1)}) ≅ ℙ¹ ∖ {0,1,∞}`` (cross-ratio chart).

    Literature: ``ℳ_{0,4}`` is isomorphic to this affine scheme (Knudsen / standard
    moduli of 4-pointed genus-0 curves). Used only as an owned étale-atlas domain
    for the open stack ``M_{0,4}``, not for general ``(g,n)`` or ``Mbar``.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    ring = base.ring()
    poly = PolynomialRing(ring, names=("t",))
    t = poly.gen()
    return AffineScheme(poly.localization(t * (t - 1)))


def _moduli_affine_etale_domain(stack: ModuliStack) -> AffineAlgebraicSpace | None:
    r"""Owned affine étale-atlas domain for literature-backed proving-set cases.

    Returns an :class:`AffineAlgebraicSpace` when the open moduli stack is a scheme
    with an owned affine presentation:

    - ``M_{0,3}``: a point ``Spec(R)`` over the base,
    - ``M_{0,4}``: cross-ratio chart ``Spec(R[t]_{t(t-1)}) ≅ ℙ¹ ∖ {0,1,∞}``.

    Fail-closed (``None``) for ``M_{1,1}`` (stacky), all ``Mbar``, and general
    ``(g,n)`` — no fake affine charts.
    """
    if stack.is_proper():
        return None
    g = stack.genus()
    n = stack.number_of_markings()
    base = stack.base_scheme()
    if g == 0 and n == 3:
        return AffineAlgebraicSpace(base)
    if g == 0 and n == 4:
        return AffineAlgebraicSpace(_cross_ratio_affine_scheme(base))
    return None


class Groupoid(UniqueRepresentation, Parent):
    r"""Finite formal groupoid (objects + isomorphisms) for moduli fibers."""

    def __init__(self, name: str = "Groupoid", *, family_factory: object | None = None) -> None:
        from sage.categories.sets_cat import Sets

        self._name = name
        self._family_factory = family_factory
        Parent.__init__(self, category=Sets())

    def _element_constructor_(self, x: object = None) -> object:
        if x is not None:
            return x
        return self.an_element()

    def an_element(self) -> object:
        if self._family_factory is not None:
            assert callable(self._family_factory), f"family_factory must be callable; found {type(self._family_factory)!r}"
            return self._family_factory()
        return f"object of {self._name}"

    def _repr_(self) -> str:
        return self._name


class ModuliProblem(UniqueRepresentation):
    r"""Contravariant pseudofunctor-shaped moduli problem to groupoids.

    Smooth vs stable pointed-curve problems are distinct subclasses — not a
    ``stable=`` constructor flag (§13).
    """

    @staticmethod
    def __classcall__(cls: type[ModuliProblem], *args: object, **kwargs: object) -> ModuliProblem:
        r"""Normalize markings and cache; inherited by concrete subclasses.

        Must be ``__classcall__`` (not ``__classcall_private__``): Sage ignores
        private classcalls on subclasses, so ``StablePointedCurveModuliProblem(g, n, …)``
        would otherwise cache raw integer markings and break uniqueness vs tuple ``I``.
        """
        from .._typing_utils import as_int

        assert cls is not ModuliProblem, f"construct SmoothPointedCurveModuliProblem or StablePointedCurveModuliProblem; found bare ModuliProblem args={args!r}"
        assert len(args) >= 3, f"{cls.__name__}(g, I, base); found args={args!r}"
        g, I, base = args[0], args[1], args[2]
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        assert isinstance(base, AffineScheme), f"expected AffineScheme; found {type(base)!r}"
        result = UniqueRepresentation.__classcall__(cls, as_int(g), _marking_set(I), base)
        assert isinstance(result, ModuliProblem), f"classcall must return ModuliProblem; found {type(result)!r}"
        return result

    def __init__(self, g: int, I: object, base: AffineScheme) -> None:
        from .._typing_utils import as_int

        self._g = as_int(g)
        self._I = _marking_set(I) if not isinstance(I, tuple) else tuple(I)
        self._base = base

    def genus(self) -> int:
        return self._g

    def marking_set(self) -> tuple[object, ...]:
        return self._I

    def number_of_markings(self) -> int:
        return len(self._I)

    def base_scheme(self) -> AffineScheme:
        return self._base

    def is_stable(self) -> bool:
        r"""True for the stable pointed-curve moduli problem."""
        return isinstance(self, StablePointedCurveModuliProblem)

    def objects_over(self, T: object) -> Groupoid:
        raise NotImplementedError("implemented on SmoothPointedCurveModuliProblem / StablePointedCurveModuliProblem")

    def pullback(self, f: object) -> ModuliProblem:
        r"""Base change of this moduli problem along a morphism of bases.

        Returns a new problem of the same class over the new base — not ``self``.
        """
        from ..geometry.stacks import _base_scheme_along

        new_base = _base_scheme_along(f, self._base)
        return type(self)(self._g, self._I, new_base)

    def _repr_(self) -> str:
        tag = "StablePointedCurves" if self.is_stable() else "SmoothPointedCurves"
        return f"{tag}({self._g}, {len(self._I)})"


class SmoothPointedCurveModuliProblem(ModuliProblem):
    r"""Moduli problem of smooth pointed curves of type `(g, I)`."""

    def objects_over(self, T: object) -> Groupoid:
        from ..curves.families import PointedCurveFamily

        g, I, base = self._g, self._I, self._base

        def _factory() -> object:
            return PointedCurveFamily(base, T, tuple(I), genus=g, marking_set=I)

        return Groupoid(
            f"smooth pointed curves of type ({self._g},{len(self._I)}) over {T!r}",
            family_factory=_factory,
        )


class StablePointedCurveModuliProblem(ModuliProblem):
    r"""Moduli problem of stable pointed curves of type `(g, I)`."""

    def objects_over(self, T: object) -> Groupoid:
        from ..curves.families import StablePointedCurveFamily

        g, I, base = self._g, self._I, self._base

        def _factory() -> object:
            return StablePointedCurveFamily(base, T, tuple(I), genus=g, marking_set=I)

        return Groupoid(
            f"stable pointed curves of type ({self._g},{len(self._I)}) over {T!r}",
            family_factory=_factory,
        )


class CoarseModuliSpace(AlgebraicSpace):
    r"""Coarse moduli space as an algebraic space over a general base."""

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
        AlgebraicSpace.__init__(self, base, name=name, axioms=axioms)

    def genus(self) -> int:
        return self._moduli_genus

    def number_of_markings(self) -> int:
        return len(self._moduli_markings)

    def marking_set(self) -> tuple[object, ...]:
        return self._moduli_markings


class CoarseModuliVariety(Variety):
    r"""Coarse space over a field, strengthened to a variety when theorems apply."""

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
    r"""Stack equipped with a moduli problem.

    Properness is the ``Proper`` axiom, derived from whether the moduli problem
    is the stable (compactified) one — not a constructor boolean. Public
    constructors are :func:`M_gI` / :func:`Mbar_gI`.
    """

    @staticmethod
    def __classcall_private__(cls: type[ModuliStack], *args: object, **kwargs: object) -> ModuliStack:
        assert len(args) == 1, f"ModuliStack(problem, *, name=None); found args={args!r}"
        problem = args[0]
        name = kwargs.pop("name", None)
        assert not kwargs, f"unexpected kwargs {sorted(kwargs)!r}"
        assert isinstance(problem, ModuliProblem), f"expected ModuliProblem; found {type(problem)!r}"
        if name is None:
            name = ("Mbar" if problem.is_stable() else "M") + f"_{problem.genus()},{problem.number_of_markings()}"
        result = UniqueRepresentation.__classcall__(cls, problem, name=name)
        assert isinstance(result, ModuliStack), f"classcall must return ModuliStack; found {type(result)!r}"
        return result

    def __init__(
        self,
        problem: ModuliProblem,
        *,
        name: str | None = None,
    ) -> None:
        self._problem = problem
        base = problem.base_scheme()
        axioms = frozenset({"Smooth", "FiniteType"})
        if problem.is_stable():
            axioms = axioms | {"Proper"}
        from sage.categories.category import Category

        from ..categories.stacks import DeligneMumfordStacks

        # Sage category join (objects inhabiting both equipped moduli and DM).
        join = getattr(Category, "join")
        cat = join((ModuliStacks(base), DeligneMumfordStacks(base)))
        for a in sorted(axioms):
            if hasattr(cat, a):
                cat = getattr(cat, a)()
        label = name or ("Mbar" if problem.is_stable() else "M") + f"_{problem.genus()},{problem.number_of_markings()}"
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

    def coarse_space(self) -> AlgebraicSpace:
        r"""Coarse moduli space: algebraic space in general; variety over a field."""
        axioms = frozenset({"FiniteType", "Separated"})
        g, I = self.genus(), self.marking_set()
        if self.is_proper():
            axioms = axioms | {"Proper", "Normal", "Projective"}
        else:
            axioms = axioms | frozenset({"Integral"})
        base = self.base_scheme()
        ring = base.ring()
        from sage.categories.fields import Fields

        if ring in Fields():
            return CoarseModuliVariety(
                base,
                genus=g,
                markings=I,
                name=f"coarse({self!r})",
                axioms=axioms,
            )
        return CoarseModuliSpace(
            base,
            genus=g,
            markings=I,
            name=f"coarse({self!r})",
            axioms=axioms,
        )

    def coarse_moduli_morphism(self) -> CoarseModuliMorphism:
        space = self.coarse_space()
        return CoarseModuliMorphism(self, space)

    def etale_atlas(self) -> AtlasMorphism:
        r"""Étale atlas ``U → ℳ`` with owned affine domain on proving-set cases.

        For ``M_{0,3}`` / ``M_{0,4}`` (open stacks representable by owned affine
        schemes), the domain is an :class:`AffineAlgebraicSpace` with matching
        identity / localization :class:`FormallyEtaleSchemeCertificate` data and
        ``covering_kind="moduli_affine_etale_chart"``.

        For ``M_{1,1}``, ``Mbar``, and general ``(g,n)``: fail-closed formal
        :class:`~dm_moduli_spike.geometry.stacks.AtlasChart` (empty affine cover;
        equation-level certificate is ``False``). Never uses the coarse space as
        an étale atlas domain.
        """
        domain = _moduli_affine_etale_domain(self)
        if domain is None:
            return DeligneMumfordStack.etale_atlas(self)
        cover = domain.affine_cover()
        assert cover, "owned moduli affine étale domain must expose a nonempty affine cover"
        certs: list[FormallyEtaleSchemeCertificate] = []
        for chart in cover:
            certs.extend(_proving_set_etale_certificates(chart))
        scheme_certs = tuple(certs)
        primary = scheme_certs[0] if scheme_certs else None
        return AtlasMorphism(
            domain,
            self,
            etale=True,
            covering_kind="moduli_affine_etale_chart",
            representable_domain=True,
            evidence=AtlasEvidence(
                stack=self,
                domain=domain,
                covering_kind="moduli_affine_etale_chart",
                etale_stamp=True,
                representable_domain=True,
                diagonal=self.diagonal(),
                dm_diagonal_unramified_stamp=True,
                dm_diagonal_representable_stamp=True,
                scheme_certificate=primary,
                scheme_certificates=scheme_certs,
            ),
        )

    def compactification(self, kind: str = "stable-pointed-curves") -> Compactification:
        if self.is_proper():
            raise ValueError("already proper; compactification is the identity immersion")
        target = Mbar_gI(self.genus(), self.marking_set(), base=self.base_scheme())
        from typing import cast

        from ..geometry.stacks import Compactifications

        return cast(Compactification, Compactifications(self)(target, kind=kind))

    def compactify(self, kind: str = "stable-pointed-curves") -> ModuliStack:
        target = self.compactification(kind=kind).target()
        assert isinstance(target, ModuliStack), f"compactification target must be ModuliStack; found {type(target)!r}"
        return target

    def open_part(self) -> ModuliStack:
        if not self.is_proper():
            return self
        return M_gI(self.genus(), self.marking_set(), base=self.base_scheme())

    def open_immersion(self) -> Compactification:
        return self.open_part().compactification()

    def boundary(self) -> Boundary:
        if not self.is_proper():
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
        cached = build_dual_graph_stratification(self)
        self._cached_dual_graph_stratification = cached
        return cached

    def stratification(self, by: object | None = None) -> object:
        return self.stratify(by=by)

    def __call__(self, x: object = None, *args: object, **kwds: object) -> ModuliStackFiber:
        assert x is not None and not args and not kwds, (
            f"ModuliStack() expects a single test object T; found T={x!r} args={args!r} kwds={kwds!r}; owned boundary=ModuliStack.__call__"
        )
        return ModuliStackFiber(self, x, self.objects_over(x))

    def fiber(self, T: object) -> ModuliStackFiber:
        return self(T)


def M_gI(g: int, I: object, base: AffineScheme | None = None) -> ModuliStack:
    resolved = base if base is not None else spec(ZZ)
    check_z_scheme(resolved)
    return ModuliStack(SmoothPointedCurveModuliProblem(g, I, resolved))


def Mbar_gI(g: int, I: object, base: AffineScheme | None = None) -> ModuliStack:
    resolved = base if base is not None else spec(ZZ)
    check_z_scheme(resolved)
    return ModuliStack(StablePointedCurveModuliProblem(g, I, resolved))


def M_gn(g: int, n: int, base: AffineScheme | None = None) -> ModuliStack:
    return M_gI(g, n, base=base)


def Mbar_gn(g: int, n: int, base: AffineScheme | None = None) -> ModuliStack:
    return Mbar_gI(g, n, base=base)
