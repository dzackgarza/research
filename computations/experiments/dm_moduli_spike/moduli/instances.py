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
    ProjectiveLineAlgebraicSpace,
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


def _two_is_invertible(base: AffineScheme) -> bool:
    r"""True when ``2`` is a unit in the base ring (Legendre form needs char ≠ 2)."""
    from typing import Any, cast

    ring = cast(Any, base.ring())
    try:
        two = ring(2)
        if hasattr(two, "is_unit") and bool(two.is_unit()):
            return True
    except TypeError, ValueError, AttributeError, ArithmeticError:
        pass
    if not hasattr(ring, "characteristic"):
        return False
    characteristic = ring.characteristic
    if not callable(characteristic):
        return False
    try:
        char = int(characteristic())
    except TypeError, ValueError:
        return False
    return char != 2


def _punctured_lambda_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Affine scheme ``Spec(R[λ]_{λ(λ-1)}) ≅ 𝔸¹ ∖ {0,1}``.

    Shared coordinate ring for:

    - ``M_{0,4}`` cross-ratio chart (isomorphism of schemes),
    - Legendre level-``Γ(2)`` cover of ``M_{1,1}`` (finite étale of degree 6).

    Same ring, different morphisms to different stacks — not a claim that
    ``M_{0,4} ≅ M_{1,1}``.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    ring = base.ring()
    poly = PolynomialRing(ring, names=("lambda",))
    lam = poly.gen()
    return AffineScheme(poly.localization(lam * (lam - 1)))


def _cross_ratio_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Affine scheme ``Spec(R[λ]_{λ(λ-1)}) ≅ ℙ¹ ∖ {0,1,∞}`` (cross-ratio chart).

    Literature: ``ℳ_{0,4}`` is isomorphic to this affine scheme (Knudsen / standard
    moduli of 4-pointed genus-0 curves). Used only as an owned étale-atlas domain
    for the open stack ``M_{0,4}``, not for general ``(g,n)`` or ``Mbar``.
    """
    return _punctured_lambda_affine_scheme(base)


def _legendre_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Legendre parameter space ``Spec(R[λ]_{λ(λ-1)})`` for ``y² = x(x-1)(x-λ)``.

    Over bases with ``2`` invertible, this is ``M(Γ(2))``, and the forgetful map
    ``M(Γ(2)) → M_{1,1}`` is finite étale Galois of degree 6 with group
    ``S₃ ≅ SL₂(𝔽₂)`` (permuting the three nonzero 2-torsion points). Hence
    ``M_{1,1} ≅ [Spec(R[λ]_{λ(λ-1)}) / S₃]`` as Deligne–Mumford stacks — an owned
    affine étale atlas domain, not an isomorphism of stacks to an affine scheme.
    """
    assert _two_is_invertible(base), "Legendre form requires 2 invertible in the base ring"
    return _punctured_lambda_affine_scheme(base)


def _moduli_etale_atlas_domain(stack: ModuliStack) -> AlgebraicSpace | None:
    r"""Owned étale-atlas domain for literature-backed proving-set cases.

    Returns a concrete :class:`AlgebraicSpace` when an owned presentation exists:

    - ``M_{0,3}`` / ``Mbar_{0,3}``: a point ``Spec(R)`` (scheme isomorphism),
    - ``M_{0,4}``: cross-ratio chart ``Spec(R[λ]_{λ(λ-1)}) ≅ ℙ¹ ∖ {0,1,∞}``,
    - ``Mbar_{0,4}``: standard affine cover of ``ℙ¹`` (stack ≅ scheme; not the
      coarse-moduli map),
    - ``M_{1,1}`` (``2`` invertible): Legendre ``M(Γ(2))`` affine chart — finite
      étale cover of degree 6, not a scheme isomorphism,
    - ``Mbar_{1,1}`` (``2`` invertible): ``Mbar(Γ(2)) ≅ ℙ¹`` with the same
      ``S₃`` finite étale groupoid (affine opens of the covering space).

    Fail-closed (``None``) for general ``(g,n)`` and when ``2`` is not invertible
    on ``(1,1)`` — no fake charts / weighted-Proj shells.
    """
    g = stack.genus()
    n = stack.number_of_markings()
    base = stack.base_scheme()
    proper = stack.is_proper()
    if g == 0 and n == 3:
        return AffineAlgebraicSpace(base)
    if g == 0 and n == 4:
        if proper:
            return ProjectiveLineAlgebraicSpace(base, "Mbar_0_4")
        return AffineAlgebraicSpace(_cross_ratio_affine_scheme(base))
    if g == 1 and n == 1 and _two_is_invertible(base):
        if proper:
            return ProjectiveLineAlgebraicSpace(base, "Mbar_Gamma2")
        return AffineAlgebraicSpace(_legendre_affine_scheme(base))
    return None


def _legendre_galois_group() -> object:
    r"""``S₃ ≅ SL₂(𝔽₂)`` acting on the Legendre ``Γ(2)`` cover of ``M_{1,1}``."""
    from typing import Any, cast

    from sage.groups.perm_gps.permgroup_named import SymmetricGroup

    return cast(Any, SymmetricGroup(3))


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

    def legendre_quotient_presentation(self) -> dict[str, object] | None:
        r"""Inspectable ``(U, S₃)`` data when a Legendre ``Γ(2)`` presentation is owned.

        Returns ``None`` unless this is ``M_{1,1}`` / ``Mbar_{1,1}`` over a base
        with ``2`` invertible.

        - Open: ``U = Spec(R[λ]_{λ(λ-1)}) = M(Γ(2))``.
        - Proper: ``U = ℙ¹ = Mbar(Γ(2))`` (standard affine cover).

        ``G = S₃`` acts by permuting ``{0,1,∞}``. Does **not** claim a scheme
        isomorphism ``M_{1,1} ≅ U`` / ``Mbar_{1,1} ≅ U``.
        """
        if self.genus() != 1 or self.number_of_markings() != 1:
            return None
        if not _two_is_invertible(self.base_scheme()):
            return None
        domain = _moduli_etale_atlas_domain(self)
        if domain is None:
            return None
        group = _legendre_galois_group()
        from typing import Any, cast

        if self.is_proper():
            presentation = "Mbar_1_1 ≅ [P1 / S3]"
            level_structure = "Mbar(Gamma(2))"
        else:
            presentation = "M_1_1 ≅ [Legendre_U / S3]"
            level_structure = "Gamma(2)"
        return {
            "covering_space": domain,
            "group": group,
            "group_order": int(cast(Any, group).order()),
            "finite_etale_groupoid": True,
            "covering_unramified_stamp": True,
            "covering_smooth_stamp": True,
            "covering_formally_etale_stamp": True,
            "degree": 6,
            "level_structure": level_structure,
            "presentation": presentation,
        }

    def etale_atlas(self) -> AtlasMorphism:
        r"""Étale atlas ``U → ℳ`` with owned domain on proving-set cases.

        - ``M_{0,3}`` / ``Mbar_{0,3}``: scheme-isomorphic point ``Spec(R)``;
          ``covering_kind="moduli_affine_etale_chart"``.
        - ``M_{0,4}``: cross-ratio affine chart;
          ``covering_kind="moduli_affine_etale_chart"``.
        - ``Mbar_{0,4}``: standard affine cover of ``ℙ¹`` (stack ≅ scheme);
          ``covering_kind="moduli_scheme_affine_cover"``. Never the coarse space.
        - ``M_{1,1}`` (``2`` invertible): affine Legendre ``M(Γ(2))`` finite
          étale cover; ``covering_kind="legendre_finite_etale_cover"``.
        - ``Mbar_{1,1}`` (``2`` invertible): ``Mbar(Γ(2)) ≅ ℙ¹`` finite étale
          cover; ``covering_kind="legendre_compact_finite_etale_cover"``.
          Stackiness retained as finite étale groupoid evidence.

        For general ``(g,n)`` and ``(1,1)`` when ``2`` is not invertible:
        fail-closed formal :class:`~dm_moduli_spike.geometry.stacks.AtlasChart`.
        Never uses the coarse space as an étale atlas domain.
        """
        domain = _moduli_etale_atlas_domain(self)
        if domain is None:
            return DeligneMumfordStack.etale_atlas(self)
        cover = domain.affine_cover()
        assert cover, "owned moduli étale domain must expose a nonempty affine cover"
        certs: list[FormallyEtaleSchemeCertificate] = []
        for chart in cover:
            certs.extend(_proving_set_etale_certificates(chart))
        scheme_certs = tuple(certs)
        primary = scheme_certs[0] if scheme_certs else None
        is_legendre = self.genus() == 1 and self.number_of_markings() == 1
        if is_legendre:
            from typing import Any, cast

            covering_kind = "legendre_compact_finite_etale_cover" if self.is_proper() else "legendre_finite_etale_cover"
            group = _legendre_galois_group()
            group_order = int(cast(Any, group).order())
            return AtlasMorphism(
                domain,
                self,
                etale=True,
                covering_kind=covering_kind,
                representable_domain=True,
                evidence=AtlasEvidence(
                    stack=self,
                    domain=domain,
                    covering_kind=covering_kind,
                    etale_stamp=True,
                    representable_domain=True,
                    diagonal=self.diagonal(),
                    dm_diagonal_unramified_stamp=True,
                    dm_diagonal_representable_stamp=True,
                    scheme_certificate=primary,
                    scheme_certificates=scheme_certs,
                    covering_space=domain,
                    quotient_group=group,
                    finite_etale_groupoid=True,
                    group_order=group_order,
                    covering_unramified_stamp=True,
                    covering_smooth_stamp=True,
                    covering_formally_etale_stamp=True,
                ),
            )
        if isinstance(domain, ProjectiveLineAlgebraicSpace):
            covering_kind = "moduli_scheme_affine_cover"
        else:
            covering_kind = "moduli_affine_etale_chart"
        return AtlasMorphism(
            domain,
            self,
            etale=True,
            covering_kind=covering_kind,
            representable_domain=True,
            evidence=AtlasEvidence(
                stack=self,
                domain=domain,
                covering_kind=covering_kind,
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
