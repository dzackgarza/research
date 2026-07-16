r"""Moduli problems, moduli stacks, and concrete M_{g,I} / Mbar_{g,I}."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.rings.integer_ring import ZZ
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from ..categories.base import AffineScheme, check_z_scheme, spec
from ..categories.stacks import ModuliStacks
from ..geometry.stacks import (
    AffineAlgebraicSpace,
    AlgebraicSpace,
    AtlasMorphism,
    Boundary,
    CoarseModuliMorphism,
    Compactification,
    CompactifiedUniversalCurveAlgebraicSpace,
    DeligneMumfordStack,
    StackFiber,
    Variety,
)

if TYPE_CHECKING:
    from .atlas_ownership import OwnedAtlasPresentation


def _marking_set(I: object) -> tuple[object, ...]:
    from collections.abc import Iterable

    from sage.rings.integer import Integer

    if isinstance(I, (int, Integer)):
        return tuple(range(1, int(I) + 1))
    assert isinstance(I, Iterable), f"expected marking count or iterable; found {type(I)!r}"
    return tuple(I)


def _prime_is_unit(base: AffineScheme, prime: int) -> bool:
    r"""True when ``prime`` is a genuine unit in the base ring.

    Legendre needs ``2 ∈ Rˣ`` (finite étale ``M(Γ(2)) → M_{1,1}`` over ``Spec(R)``);
    Hesse needs ``3 ∈ Rˣ``. The older ``char ≠ p`` heuristic incorrectly treated
    ``Spec(ℤ)`` as Legendre-ready (``char 0 ≠ 2``) even though ``2`` is not a unit —
    over ``Spec(ℤ)`` the level covers are finite étale only after inverting the
    bad prime. Fail closed when ``is_unit`` is unavailable.
    """
    from typing import Any, cast

    ring = cast(Any, base.ring())
    try:
        element = ring(prime)
    except TypeError, ValueError, AttributeError, ArithmeticError:
        return False
    if not hasattr(element, "is_unit"):
        return False
    try:
        return bool(element.is_unit())
    except TypeError, ValueError, AttributeError, ArithmeticError:
        return False


def _two_is_invertible(base: AffineScheme) -> bool:
    r"""True when ``2`` is a unit (Legendre ``Γ(2)`` hypothesis)."""
    return _prime_is_unit(base, 2)


def _three_is_invertible(base: AffineScheme) -> bool:
    r"""True when ``3`` is a unit (Hesse ``Γ(3)`` hypothesis)."""
    return _prime_is_unit(base, 3)


def _legendre_and_hesse_unavailable(base: AffineScheme) -> bool:
    r"""True when neither Legendre nor Hesse level hypotheses hold.

    Concrete bases: ``Spec(ℤ)`` (neither ``2`` nor ``3`` is a unit). On fields this
    never holds: char ``2`` ⇒ ``3 = 1`` is a unit (Hesse); char ``3`` ⇒ ``2 = -1``
    is a unit (Legendre); otherwise both are units.
    """
    return not _two_is_invertible(base) and not _three_is_invertible(base)


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

    Special case ``n = 4`` of :func:`_knudsen_open_M0n_affine_scheme`.
    """
    return _knudsen_open_M0n_affine_scheme(base, 4)


def _knudsen_open_M0n_coordinate_names(dimension: int) -> tuple[str, ...]:
    r"""Coordinate names for the open Knudsen chart of dimension ``n - 3``.

    Matches historical special cases: ``λ`` (``n=4``), ``λ,μ`` (``n=5``),
    ``λ,μ,ν`` (``n=6``); for ``n ≥ 7`` uses ``t_1,…,t_{n-3}``.
    """
    if dimension == 1:
        return ("lambda",)
    if dimension == 2:
        return ("lambda", "mu")
    if dimension == 3:
        return ("lambda", "mu", "nu")
    return tuple(f"t{i}" for i in range(1, dimension + 1))


def _knudsen_open_M0n_affine_scheme(base: AffineScheme, n: int) -> AffineScheme:
    r"""Parametric Knudsen / configuration chart for open ``ℳ_{0,n}``, ``n ≥ 3``.

    Fix three markings at ``{0,1,∞}``. The remaining ``n - 3`` markings are
    coordinates ``t_1,…,t_{n-3}`` in ``𝔸^{n-3}`` minus the diagonals and the
    hyperplanes ``t_i ∈ {0,1}`` (pairwise distinct and avoiding ``{0,1,∞}``), so

    ``ℳ_{0,n} ≅ Spec( R[t_1,…,t_{n-3}]_S )``

    where ``S`` is the product of all ``t_i``, ``t_i - 1``, and ``t_i - t_j``
    (``i < j``). Special cases:

    * ``n = 3``: ``Spec(R)`` (a point),
    * ``n = 4``: ``Spec(R[λ]_{λ(λ-1)})``,
    * ``n = 5``: ``Spec(R[λ,μ]_{λ(λ-1)μ(μ-1)(λ-μ)})``,
    * ``n = 6``: ``Spec(R[λ,μ,ν]_{…})``.

    Literature: Knudsen's construction of ``M_{0,n}``; Fulton–MacPherson /
    configuration-space presentation. Owned for the **open** stack only —
    proper ``Mbar_{0,n}`` for ``3 ≤ n ≤ PROPER_M0N_OWNED_MAX`` is registered
    separately (parametric Kapranov); larger ``n`` stay fail-closed (named gap
    ``kapranov_iterated_blowup_P_{n-3}``).
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    n_int = int(n)
    assert n_int >= 3, f"open Knudsen chart requires n ≥ 3; got {n!r}"
    dimension = n_int - 3
    if dimension == 0:
        return base
    names = _knudsen_open_M0n_coordinate_names(dimension)
    ring = base.ring()
    poly = PolynomialRing(ring, names=names)
    gens = poly.gens()
    denom = poly.one()
    for t in gens:
        denom *= t * (t - 1)
    for i, ti in enumerate(gens):
        for tj in gens[i + 1 :]:
            denom *= ti - tj
    return AffineScheme(poly.localization(denom))


def _legendre_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Legendre parameter space ``Spec(R[λ]_{λ(λ-1)})`` for ``y² = x(x-1)(x-λ)``.

    Special case ``n = 1`` of :func:`_legendre_open_M1n_affine_scheme`.
    """
    return _legendre_open_M1n_affine_scheme(base, 1)


def _hesse_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Hesse parameter space ``Spec(R[μ]_{μ³-1})`` for the level-``Γ(3)`` cover.

    Special case ``n = 1`` of :func:`_hesse_open_M1n_affine_scheme`.
    """
    return _hesse_open_M1n_affine_scheme(base, 1)


def _legendre_open_M1n_point_names(extra_marks: int) -> tuple[str, ...]:
    r"""Coordinate names for ``extra_marks`` Weierstrass points on the Legendre model."""
    if extra_marks == 1:
        return ("x", "y")
    names: list[str] = []
    for i in range(1, extra_marks + 1):
        names.extend((f"x{i}", f"y{i}"))
    return tuple(names)


def _hesse_open_M1n_point_names(extra_marks: int) -> tuple[str, ...]:
    r"""Coordinate names for ``extra_marks`` affine points on the Hesse cubic."""
    return _legendre_open_M1n_point_names(extra_marks)


def _legendre_open_M1n_affine_scheme(base: AffineScheme, n: int) -> AffineScheme:
    r"""Parametric Legendre / ``Γ(2)`` chart for open ``M_{1,n}``, ``n ≥ 1``.

    Forgetful ``M_{1,n} → M_{1,1}``; the fiber is a configuration of ``n - 1``
    extra marked points on the universal Legendre curve (first mark at the
    identity / zero section at infinity). Requires ``2 ∈ Rˣ``. Finite étale
    groupoid pulled back from ``M(Γ(2)) → M_{1,1}`` (Galois group ``S₃``).

    * ``n = 1``: ``Spec(R[λ]_{λ(λ-1)}) = M(Γ(2))``.
    * ``n = 2``: Weierstrass affine
      ``Spec(R[λ,x,y]_{λ(λ-1)}/(y²-x(x-1)(x-λ)))`` (historical chart).
    * ``n ≥ 3``: ``n - 1`` points ``(x_i,y_i)`` on the Legendre model, localized
      at ``λ(λ-1)``, at each ``y_i`` (away from nonzero 2-torsion / branch of
      the double cover), and at ``x_i - x_j`` (``i < j``; dense open of
      pairwise-distinct configurations with distinct ``x``-coordinates).

    Not a scheme isomorphism ``M_{1,n} ≅ U``. Proper compact charts live in
    :func:`_legendre_compact_M1n_covering_space`.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    n_int = int(n)
    assert n_int >= 1, f"open Legendre M_{{1,n}} chart requires n ≥ 1; got {n!r}"
    assert _two_is_invertible(base), "Legendre M_{1,n} chart requires 2 invertible"
    if n_int == 1:
        return _punctured_lambda_affine_scheme(base)

    extra = n_int - 1
    names = ("lambda",) + _legendre_open_M1n_point_names(extra)
    ring = base.ring()
    poly = PolynomialRing(ring, names=names)
    gens = poly.gens()
    lam = gens[0]
    denom = lam * (lam - 1)
    if n_int >= 3:
        xs = gens[1::2]
        ys = gens[2::2]
        for y in ys:
            denom *= y
        for i, xi in enumerate(xs):
            for xj in xs[i + 1 :]:
                denom *= xi - xj
    localized = poly.localization(denom)
    equations = []
    for i in range(extra):
        x = localized(gens[1 + 2 * i])
        y = localized(gens[2 + 2 * i])
        equations.append(y**2 - x * (x - 1) * (x - localized(lam)))
    if len(equations) == 1:
        return AffineScheme(localized.quo(equations[0]))
    return AffineScheme(localized.quo(localized.ideal(equations)))


def _hesse_open_M1n_affine_scheme(base: AffineScheme, n: int) -> AffineScheme:
    r"""Parametric Hesse / ``Γ(3)`` chart for open ``M_{1,n}``, ``n ≥ 1``.

    Parallel to :func:`_legendre_open_M1n_affine_scheme` under ``3 ∈ Rˣ``
    (including characteristic ``2``). Finite étale groupoid pulled back from
    ``M(Γ(3)) → M_{1,1}`` (Galois group ``SL₂(𝔽₃)``, order 24).

    * ``n = 1``: ``Spec(R[μ]_{μ³-1}) = M(Γ(3))``.
    * ``n = 2``: Hesse affine
      ``Spec(R[μ,x,y]_{μ³-1}/(x³+y³+1-3μxy))`` (historical chart).
    * ``n ≥ 3``: ``n - 1`` points on the ``Z = 1`` Hesse cubic, localized at
      ``μ³ - 1``, at each ``y_i``, and at pairwise ``x_i - x_j`` (dense open of
      collision-free configurations in the affine chart; zero section / flex
      identity stays on ``Z = 0``).

    Primitive cube roots of unity are not required in the base ring. Proper
    compact charts live in :func:`_hesse_compact_M1n_covering_space`.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    n_int = int(n)
    assert n_int >= 1, f"open Hesse M_{{1,n}} chart requires n ≥ 1; got {n!r}"
    assert _three_is_invertible(base), "Hesse M_{1,n} chart requires 3 invertible"
    ring = base.ring()
    if n_int == 1:
        poly = PolynomialRing(ring, names=("mu",))
        mu = poly.gen()
        return AffineScheme(poly.localization(mu**3 - 1))

    extra = n_int - 1
    names = ("mu",) + _hesse_open_M1n_point_names(extra)
    poly = PolynomialRing(ring, names=names)
    gens = poly.gens()
    mu = gens[0]
    denom = mu**3 - 1
    if n_int >= 3:
        xs = gens[1::2]
        ys = gens[2::2]
        for y in ys:
            denom *= y
        for i, xi in enumerate(xs):
            for xj in xs[i + 1 :]:
                denom *= xi - xj
    localized = poly.localization(denom)
    equations = []
    for i in range(extra):
        x = localized(gens[1 + 2 * i])
        y = localized(gens[2 + 2 * i])
        equations.append(x**3 + y**3 + 1 - localized(3) * localized(mu) * x * y)
    if len(equations) == 1:
        return AffineScheme(localized.quo(equations[0]))
    return AffineScheme(localized.quo(localized.ideal(equations)))


def _configuration_M05_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Affine scheme for open ``ℳ_{0,5}`` — special case of Knudsen ``n = 5``.

    Proper ``Mbar_{0,5}`` uses the Kapranov ``Bl₄(ℙ²)`` cover
    :class:`~dm_moduli_spike.geometry.stacks.KapranovBlowupFourPointsP2AlgebraicSpace`.
    """
    return _knudsen_open_M0n_affine_scheme(base, 5)


def _configuration_M06_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Affine scheme for open ``ℳ_{0,6}`` — special case of Knudsen ``n = 6``.

    Proper ``Mbar_{0,6}`` uses the Kapranov ``Bl(ℙ³)`` cover
    :class:`~dm_moduli_spike.geometry.stacks.KapranovBlowupFivePointsP3AlgebraicSpace`.
    """
    return _knudsen_open_M0n_affine_scheme(base, 6)


def _igusa_open_M20_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Igusa / binary-sextic affine chart for open unmarked ``M_{2,0}``.

    Every genus-2 curve is hyperelliptic. After ``PGL₂``-normalizing three
    Weierstrass points to ``{0,1,∞}``, a dense open of binary sextics with
    distinct roots is the Knudsen configuration chart

    ``Spec(R[λ,μ,ν]_{S})``

    where ``S`` is the product of all pairwise differences among
    ``{0,1,λ,μ,ν}`` (equivalently the nonsingular locus of the model
    ``y² = x(x-1)(x-λ)(x-μ)(x-ν)``, the sixth branch point being ``∞``).

    Requires ``2 ∈ Rˣ`` (standard hyperelliptic double cover). This is an
    affine chart of the Igusa / binary-sextic presentation covering a dense
    open of open ``M_2`` — **not** a scheme isomorphism ``M_2 ≅ U``, and
    **not** a compact ``Mbar_2`` atlas. The finite étale groupoid is
    ``S₆`` permuting the six Weierstrass points (see
    :func:`_igusa_galois_group`).
    """
    assert _two_is_invertible(base), "Igusa binary-sextic M_{2,0} chart requires 2 invertible"
    return _knudsen_open_M0n_affine_scheme(base, 6)


def _legendre_M12_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Legendre universal-curve chart for open ``M_{1,2}``.

    Special case ``n = 2`` of :func:`_legendre_open_M1n_affine_scheme`. Proper
    ``Mbar_{1,2}`` uses :func:`_legendre_compact_M1n_algebraic_space`.
    """
    return _legendre_open_M1n_affine_scheme(base, 2)


def _hesse_M12_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Hesse universal-curve chart for open ``M_{1,2}`` (incl. char ``2``).

    Special case ``n = 2`` of :func:`_hesse_open_M1n_affine_scheme`. Proper
    ``Mbar_{1,2}`` uses :func:`_hesse_compact_M1n_algebraic_space`.
    """
    return _hesse_open_M1n_affine_scheme(base, 2)


def _legendre_compact_M1n_infinite_point_names(extra_marks: int) -> tuple[str, ...]:
    r"""Infinite-chart coordinate names for ``extra_marks`` Legendre Weierstrass points."""
    if extra_marks == 1:
        return ("X", "Y")
    names: list[str] = []
    for i in range(1, extra_marks + 1):
        names.extend((f"X{i}", f"Y{i}"))
    return tuple(names)


def _hesse_compact_M1n_infinite_point_names(extra_marks: int) -> tuple[str, ...]:
    r"""Infinite-chart coordinate names for ``extra_marks`` Hesse affine points."""
    return _legendre_compact_M1n_infinite_point_names(extra_marks)


def _legendre_compact_M1n_finite_lambda_chart(base: AffineScheme, n: int) -> AffineScheme:
    r"""Compact Legendre Weierstrass chart over ``𝔸¹_λ``, including nodal fibers.

    * ``n = 2``: ``Spec(R[λ,x,y] / (y² - x(x-1)(x-λ)))`` — historical cover; no
      localization at ``λ(λ-1)``.
    * ``n ≥ 3``: ``n - 1`` points on the same model; localize at each ``y_i`` and
      at ``x_i - x_j`` (collision-free marks on the smooth locus of fibers), but
      **not** at ``λ(λ-1)``, so discriminant-zero base points remain.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    n_int = int(n)
    assert n_int >= 2, f"compact Legendre finite chart requires n ≥ 2; got {n!r}"
    assert _two_is_invertible(base), "Legendre Mbar_{1,n} chart requires 2 invertible"
    extra = n_int - 1
    names = ("lambda",) + _legendre_open_M1n_point_names(extra)
    ring = base.ring()
    poly = PolynomialRing(ring, names=names)
    gens = poly.gens()
    lam = gens[0]
    if n_int == 2:
        x, y = gens[1], gens[2]
        return AffineScheme(poly.quo(y**2 - x * (x - 1) * (x - lam)))

    xs = gens[1::2]
    ys = gens[2::2]
    denom = poly.one()
    for y in ys:
        denom *= y
    for i, xi in enumerate(xs):
        for xj in xs[i + 1 :]:
            denom *= xi - xj
    localized = poly.localization(denom)
    equations = [
        localized(gens[2 + 2 * i]) ** 2 - localized(gens[1 + 2 * i]) * (localized(gens[1 + 2 * i]) - 1) * (localized(gens[1 + 2 * i]) - localized(lam)) for i in range(extra)
    ]
    return AffineScheme(localized.quo(localized.ideal(equations)))


def _legendre_compact_M1n_infinite_lambda_chart(base: AffineScheme, n: int) -> AffineScheme:
    r"""Compact Legendre chart near ``λ = ∞`` via ``ν = 1/λ``.

    From ``Y² Z = X(X-Z)(X-λ Z)`` with ``λ = 1/ν`` and affine ``Z = 1``:

    * ``n = 2``: ``Spec(R[ν,X,Y] / (ν Y² - X(X-1)(ν X - 1)))``.
    * ``n ≥ 3``: same fiber equation for each mark, localized at ``Y_i`` and
      ``X_i - X_j`` (not at ``ν``), so the nodal fiber ``ν = 0`` stays.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    n_int = int(n)
    assert n_int >= 2, f"compact Legendre infinite chart requires n ≥ 2; got {n!r}"
    assert _two_is_invertible(base), "Legendre Mbar_{1,n} chart requires 2 invertible"
    extra = n_int - 1
    names = ("nu",) + _legendre_compact_M1n_infinite_point_names(extra)
    ring = base.ring()
    poly = PolynomialRing(ring, names=names)
    gens = poly.gens()
    nu = gens[0]
    if n_int == 2:
        X, Y = gens[1], gens[2]
        return AffineScheme(poly.quo(nu * Y**2 - X * (X - 1) * (nu * X - 1)))

    Xs = gens[1::2]
    Ys = gens[2::2]
    denom = poly.one()
    for Y in Ys:
        denom *= Y
    for i, Xi in enumerate(Xs):
        for Xj in Xs[i + 1 :]:
            denom *= Xi - Xj
    localized = poly.localization(denom)
    equations = [
        localized(nu) * localized(gens[2 + 2 * i]) ** 2 - localized(gens[1 + 2 * i]) * (localized(gens[1 + 2 * i]) - 1) * (localized(nu) * localized(gens[1 + 2 * i]) - 1)
        for i in range(extra)
    ]
    return AffineScheme(localized.quo(localized.ideal(equations)))


def _legendre_compact_M1n_algebraic_space(base: AffineScheme, n: int) -> CompactifiedUniversalCurveAlgebraicSpace:
    r"""Compactified Legendre multi-mark cover of proper ``Mbar_{1,n}``, ``n ≥ 2``.

    Pullback of ``Mbar(Γ(2)) → Mbar_{1,1}`` along the forgetful map
    ``Mbar_{1,n} → Mbar_{1,1}``. Covering space is the compactified Legendre
    family with ``n - 1`` extra marked points (identity / zero section at
    infinity), affine charts including discriminant zero. Finite étale of
    degree 6 with group ``S₃``. Not a scheme isomorphism.

    * ``n = 2``: historical ``Mbar_Gamma2_univ_curve`` two-chart cover.
    * ``n ≥ 3``: same two-chart pattern with collision-free mark localizations.

    For ``n = 1`` use :func:`_legendre_compact_M1n_covering_space` (``ℙ¹``).
    """
    n_int = int(n)
    assert n_int >= 2, f"compact Legendre multi-mark cover requires n ≥ 2; got {n!r}"
    assert _two_is_invertible(base), "Legendre Mbar_{1,n} chart requires 2 invertible"
    role = "Mbar_Gamma2_univ_curve" if n_int == 2 else "Mbar_Gamma2_marked_configuration"
    return CompactifiedUniversalCurveAlgebraicSpace(
        base,
        role,
        (
            _legendre_compact_M1n_finite_lambda_chart(base, n_int),
            _legendre_compact_M1n_infinite_lambda_chart(base, n_int),
        ),
    )


def _legendre_compact_M1n_covering_space(base: AffineScheme, n: int) -> AlgebraicSpace:
    r"""Parametric compact Legendre covering space of proper ``Mbar_{1,n}``, ``n ≥ 1``.

    * ``n = 1``: ``Mbar(Γ(2)) ≅ ℙ¹``.
    * ``n ≥ 2``: :func:`_legendre_compact_M1n_algebraic_space`.
    """
    from ..geometry.stacks import ProjectiveLineAlgebraicSpace

    n_int = int(n)
    assert n_int >= 1, f"compact Legendre Mbar_{{1,n}} requires n ≥ 1; got {n!r}"
    assert _two_is_invertible(base), "Legendre Mbar_{1,n} chart requires 2 invertible"
    if n_int == 1:
        return ProjectiveLineAlgebraicSpace(base, "Mbar_Gamma2")
    return _legendre_compact_M1n_algebraic_space(base, n_int)


def _legendre_Mbar12_algebraic_space(base: AffineScheme) -> CompactifiedUniversalCurveAlgebraicSpace:
    r"""Historical alias: compact Legendre cover of proper ``Mbar_{1,2}``."""
    return _legendre_compact_M1n_algebraic_space(base, 2)


def _hesse_compact_M1n_finite_mu_chart(base: AffineScheme, n: int) -> AffineScheme:
    r"""Compact Hesse cubic chart over ``𝔸¹_μ``, including nodal fibers ``μ³ = 1``.

    * ``n = 2``: ``Spec(R[μ,x,y] / (x³ + y³ + 1 - 3μ x y))`` — no localization
      at ``μ³ - 1``.
    * ``n ≥ 3``: ``n - 1`` points; localize at ``y_i`` and ``x_i - x_j`` only.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    n_int = int(n)
    assert n_int >= 2, f"compact Hesse finite chart requires n ≥ 2; got {n!r}"
    assert _three_is_invertible(base), "Hesse Mbar_{1,n} chart requires 3 invertible"
    extra = n_int - 1
    names = ("mu",) + _hesse_open_M1n_point_names(extra)
    ring = base.ring()
    poly = PolynomialRing(ring, names=names)
    gens = poly.gens()
    mu = gens[0]
    if n_int == 2:
        x, y = gens[1], gens[2]
        return AffineScheme(poly.quo(x**3 + y**3 + 1 - poly(3) * mu * x * y))

    xs = gens[1::2]
    ys = gens[2::2]
    denom = poly.one()
    for y in ys:
        denom *= y
    for i, xi in enumerate(xs):
        for xj in xs[i + 1 :]:
            denom *= xi - xj
    localized = poly.localization(denom)
    equations = [
        localized(gens[1 + 2 * i]) ** 3 + localized(gens[2 + 2 * i]) ** 3 + 1 - localized(3) * localized(mu) * localized(gens[1 + 2 * i]) * localized(gens[2 + 2 * i])
        for i in range(extra)
    ]
    return AffineScheme(localized.quo(localized.ideal(equations)))


def _hesse_compact_M1n_infinite_mu_chart(base: AffineScheme, n: int) -> AffineScheme:
    r"""Compact Hesse chart near ``μ = ∞`` via ``ν = 1/μ`` and scaling.

    * ``n = 2``: ``Spec(R[ν,X,Y] / (X³ + Y³ + ν³ - 3 X Y))``.
    * ``n ≥ 3``: same for each mark, localized at ``Y_i`` and ``X_i - X_j``.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    n_int = int(n)
    assert n_int >= 2, f"compact Hesse infinite chart requires n ≥ 2; got {n!r}"
    assert _three_is_invertible(base), "Hesse Mbar_{1,n} chart requires 3 invertible"
    extra = n_int - 1
    names = ("nu",) + _hesse_compact_M1n_infinite_point_names(extra)
    ring = base.ring()
    poly = PolynomialRing(ring, names=names)
    gens = poly.gens()
    nu = gens[0]
    if n_int == 2:
        X, Y = gens[1], gens[2]
        return AffineScheme(poly.quo(X**3 + Y**3 + nu**3 - poly(3) * X * Y))

    Xs = gens[1::2]
    Ys = gens[2::2]
    denom = poly.one()
    for Y in Ys:
        denom *= Y
    for i, Xi in enumerate(Xs):
        for Xj in Xs[i + 1 :]:
            denom *= Xi - Xj
    localized = poly.localization(denom)
    equations = [
        localized(gens[1 + 2 * i]) ** 3 + localized(gens[2 + 2 * i]) ** 3 + localized(nu) ** 3 - localized(3) * localized(gens[1 + 2 * i]) * localized(gens[2 + 2 * i])
        for i in range(extra)
    ]
    return AffineScheme(localized.quo(localized.ideal(equations)))


def _hesse_compact_M1n_algebraic_space(base: AffineScheme, n: int) -> CompactifiedUniversalCurveAlgebraicSpace:
    r"""Compactified Hesse multi-mark cover of proper ``Mbar_{1,n}``, ``n ≥ 2``.

    Pullback of ``Mbar(Γ(3)) → Mbar_{1,1}`` along ``Mbar_{1,n} → Mbar_{1,1}``.
    Finite étale of degree ``|SL₂(𝔽₃)| = 24``. Used when Legendre is unavailable.

    * ``n = 2``: historical ``Mbar_Gamma3_univ_curve`` two-chart cover.
    * ``n ≥ 3``: same two-chart pattern with collision-free mark localizations.

    For ``n = 1`` use :func:`_hesse_compact_M1n_covering_space` (``ℙ¹``).
    """
    n_int = int(n)
    assert n_int >= 2, f"compact Hesse multi-mark cover requires n ≥ 2; got {n!r}"
    assert _three_is_invertible(base), "Hesse Mbar_{1,n} chart requires 3 invertible"
    role = "Mbar_Gamma3_univ_curve" if n_int == 2 else "Mbar_Gamma3_marked_configuration"
    return CompactifiedUniversalCurveAlgebraicSpace(
        base,
        role,
        (
            _hesse_compact_M1n_finite_mu_chart(base, n_int),
            _hesse_compact_M1n_infinite_mu_chart(base, n_int),
        ),
    )


def _hesse_compact_M1n_covering_space(base: AffineScheme, n: int) -> AlgebraicSpace:
    r"""Parametric compact Hesse covering space of proper ``Mbar_{1,n}``, ``n ≥ 1``.

    * ``n = 1``: ``Mbar(Γ(3)) ≅ ℙ¹``.
    * ``n ≥ 2``: :func:`_hesse_compact_M1n_algebraic_space`.
    """
    from ..geometry.stacks import ProjectiveLineAlgebraicSpace

    n_int = int(n)
    assert n_int >= 1, f"compact Hesse Mbar_{{1,n}} requires n ≥ 1; got {n!r}"
    assert _three_is_invertible(base), "Hesse Mbar_{1,n} chart requires 3 invertible"
    if n_int == 1:
        return ProjectiveLineAlgebraicSpace(base, "Mbar_Gamma3")
    return _hesse_compact_M1n_algebraic_space(base, n_int)


def _hesse_Mbar12_algebraic_space(base: AffineScheme) -> CompactifiedUniversalCurveAlgebraicSpace:
    r"""Historical alias: compact Hesse cover of proper ``Mbar_{1,2}``."""
    return _hesse_compact_M1n_algebraic_space(base, 2)


def _tate_weierstrass_discriminant(a1: object, a2: object, a3: object, a4: object, a6: object) -> object:
    r"""Integral Tate discriminant of ``y² + a₁xy + a₃y = x³ + a₂x² + a₄x + a₆``."""
    from typing import Any, cast

    a1_, a2_, a3_, a4_, a6_ = cast(Any, a1), cast(Any, a2), cast(Any, a3), cast(Any, a4), cast(Any, a6)
    b2 = a1_**2 + 4 * a2_
    b4 = 2 * a4_ + a1_ * a3_
    b6 = a3_**2 + 4 * a6_
    b8 = a1_**2 * a6_ + 4 * a2_ * a6_ - a1_ * a3_ * a4_ + a2_ * a3_**2 - a4_**2
    return -(b2**2) * b8 - 8 * b4**3 - 27 * b6**2 + 9 * b2 * b4 * b6


def _weierstrass_M11_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Deligne–Rapoport / Katz–Mazur Weierstrass affine for open ``M_{1,1}``.

    ``U = Spec(R[a₁,a₂,a₃,a₄,a₆][Δ⁻¹])`` with Tate's integral discriminant ``Δ``.
    Weighted ``𝔾_m`` acts by ``λ·aᵢ = λⁱ aᵢ``; classically
    ``M_{1,1} ≅ [U / 𝔾_m]`` as Artin stacks. The covering ``U → [U/𝔾_m]`` is
    smooth of relative dimension ``1``, **not** finite étale — ``𝔾_m`` is
    infinite — so this is owned as fail-closed evidence for
    :meth:`ModuliStack.etale_atlas_gap`, not as an equation-level finite étale
    atlas. Used when neither Legendre nor Hesse applies (e.g. ``Spec(ℤ)``).
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    ring = base.ring()
    poly = PolynomialRing(ring, names=("a1", "a2", "a3", "a4", "a6"))
    a1, a2, a3, a4, a6 = poly.gens()
    delta = _tate_weierstrass_discriminant(a1, a2, a3, a4, a6)
    return AffineScheme(poly.localization(delta))


def _weierstrass_M12_affine_scheme(base: AffineScheme) -> AffineScheme:
    r"""Weierstrass universal-curve affine for open ``M_{1,2}`` (``𝔾_m`` presentation).

    ``U = Spec( R[a₁,…,a₆,x,y][Δ⁻¹] / (y² + a₁xy + a₃y - x³ - a₂x² - a₄x - a₆) )``.

    Same infinite-``𝔾_m`` obstruction as :func:`_weierstrass_M11_affine_scheme`:
    owned for gap evidence, not finite étale equation-level certification.
    """
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    ring = base.ring()
    poly = PolynomialRing(ring, names=("a1", "a2", "a3", "a4", "a6", "x", "y"))
    a1, a2, a3, a4, a6, x, y = poly.gens()
    delta = _tate_weierstrass_discriminant(a1, a2, a3, a4, a6)
    localized = poly.localization(delta)
    equation = (
        localized(y) ** 2
        + localized(a1) * localized(x) * localized(y)
        + localized(a3) * localized(y)
        - localized(x) ** 3
        - localized(a2) * localized(x) ** 2
        - localized(a4) * localized(x)
        - localized(a6)
    )
    return AffineScheme(localized.quo(equation))


def _moduli_etale_atlas_domain(stack: ModuliStack) -> AlgebraicSpace | None:
    r"""Owned étale-atlas domain via the atlas-ownership registry.

    Delegates to :mod:`dm_moduli_spike.moduli.atlas_ownership`. Returns
    ``None`` for unowned ``(g,n)`` and for ``(1,*)`` when neither Legendre nor
    Hesse hypotheses hold. Weierstrass ``𝔾_m`` is gap evidence only — never an
    étale-atlas domain here.
    """
    from .atlas_ownership import _domain_for_presentation, resolve_owned_etale_atlas

    row = resolve_owned_etale_atlas(stack)
    if row is None:
        return None
    return _domain_for_presentation(stack, row)


def _legendre_galois_group() -> object:
    r"""``S₃ ≅ SL₂(𝔽₂)`` acting on the Legendre ``Γ(2)`` cover of ``M_{1,1}``."""
    from typing import Any, cast

    from sage.groups.perm_gps.permgroup_named import SymmetricGroup

    return cast(Any, SymmetricGroup(3))


def _hesse_galois_group() -> object:
    r"""``SL₂(𝔽₃)`` (order 24, binary tetrahedral) for the Hesse ``Γ(3)`` cover.

    Parallel to Legendre's ``S₃ ≅ SL₂(𝔽₂)``: the forgetful map
    ``M(Γ(N)) → M_{1,1}`` is finite étale Galois of degree ``|SL₂(ℤ/Nℤ)|``.
    For ``N = 3`` that group is ``SL₂(𝔽₃)``, not ``PSL₂(𝔽₃) ≅ A₄`` (order 12),
    because stacky moduli retain the full symplectic level structure (cf.
    Deligne–Rapoport / Katz–Mazur).
    """
    from typing import Any, cast

    from sage.groups.matrix_gps.linear import SL
    from sage.rings.finite_rings.finite_field_constructor import GF

    return cast(Any, SL(2, GF(3)))


def _igusa_galois_group() -> object:
    r"""``S₆ ≅ Sp₄(𝔽₂)`` acting on the Igusa level-``2`` cover of open ``M_2``.

    Six labeled Weierstrass / branch points of a genus-2 hyperelliptic curve;
    ``Sp₄(𝔽₂)`` is the symplectic group of the 2-torsion of the Jacobian and is
    isomorphic to ``S₆``. Degree ``720``. The coarse space is ``M_{0,6}/S₆``;
    the covering space is a dense open of ``M_{0,6}``. Does **not** erase the
    residual hyperelliptic involution of the DM stack — the presentation is
    the finite étale groupoid ``[U / S₆]``, not a scheme isomorphism.
    """
    from typing import Any, cast

    from sage.groups.perm_gps.permgroup_named import SymmetricGroup

    return cast(Any, SymmetricGroup(6))


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

        Returns ``None`` unless this is open ``M_{1,n}`` or proper ``Mbar_{1,n}``
        (``n ≥ 1``) over a base with ``2`` invertible.

        - Open ``M_{1,n}``: parametric Legendre chart
          :func:`_legendre_open_M1n_affine_scheme`.
        - Proper ``Mbar_{1,1}``: compact ``ℙ¹ = Mbar(Γ(2))``.
        - Proper ``Mbar_{1,n}`` (``n ≥ 2``): compact multi-mark Legendre cover
          :func:`_legendre_compact_M1n_algebraic_space`.

        ``G = S₃`` acts by permuting ``{0,1,∞}`` on the level structure.
        Does **not** claim a scheme isomorphism ``M_{1,*} ≅ U``.
        """
        if self.genus() != 1:
            return None
        n = int(self.number_of_markings())
        if n < 1:
            return None
        if not _two_is_invertible(self.base_scheme()):
            return None
        domain = _moduli_etale_atlas_domain(self)
        if domain is None:
            return None
        group = _legendre_galois_group()
        from typing import Any, cast

        if self.is_proper():
            if n == 1:
                presentation = "Mbar_1_1 ≅ [P1 / S3]"
                level_structure = "Mbar(Gamma(2))"
            elif n == 2:
                presentation = "Mbar_1_2 ≅ [compact_Legendre_univ_curve / S3]"
                level_structure = "Mbar(Gamma(2))_universal_curve"
            else:
                presentation = f"Mbar_1_{n} ≅ [compact_Legendre_marked_configuration / S3]"
                level_structure = "Mbar(Gamma(2))_marked_configuration"
        elif n == 1:
            presentation = "M_1_1 ≅ [Legendre_U / S3]"
            level_structure = "Gamma(2)"
        elif n == 2:
            presentation = "M_1_2 ≅ [Legendre_univ_curve_minus_0 / S3]"
            level_structure = "Gamma(2)_universal_curve"
        else:
            presentation = f"M_1_{n} ≅ [Legendre_marked_configuration / S3]"
            level_structure = "Gamma(2)_marked_configuration"
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

    def hesse_quotient_presentation(self) -> dict[str, object] | None:
        r"""Inspectable ``(U, SL₂(𝔽₃))`` data when a Hesse ``Γ(3)`` presentation is owned.

        Returns ``None`` unless this is open ``M_{1,n}`` or proper ``Mbar_{1,n}``
        (``n ≥ 1``) over a base with ``2`` **not** invertible and ``3`` invertible
        (Legendre preferred whenever available).

        - Open ``M_{1,n}``: parametric Hesse chart :func:`_hesse_open_M1n_affine_scheme`.
        - Proper ``Mbar_{1,1}``: compact ``ℙ¹ = Mbar(Γ(3))``.
        - Proper ``Mbar_{1,n}`` (``n ≥ 2``): compact multi-mark Hesse cover
          :func:`_hesse_compact_M1n_algebraic_space`.

        ``G = SL₂(𝔽₃)`` has order 24. Does **not** claim a scheme isomorphism
        ``M_{1,*} ≅ U``.
        """
        if self.genus() != 1:
            return None
        n = int(self.number_of_markings())
        if n < 1:
            return None
        base = self.base_scheme()
        if _two_is_invertible(base) or not _three_is_invertible(base):
            return None
        domain = _moduli_etale_atlas_domain(self)
        if domain is None:
            return None
        group = _hesse_galois_group()
        from typing import Any, cast

        if self.is_proper():
            if n == 1:
                presentation = "Mbar_1_1 ≅ [P1 / SL2(F3)]"
                level_structure = "Mbar(Gamma(3))"
            elif n == 2:
                presentation = "Mbar_1_2 ≅ [compact_Hesse_univ_curve / SL2(F3)]"
                level_structure = "Mbar(Gamma(3))_universal_curve"
            else:
                presentation = f"Mbar_1_{n} ≅ [compact_Hesse_marked_configuration / SL2(F3)]"
                level_structure = "Mbar(Gamma(3))_marked_configuration"
        elif n == 1:
            presentation = "M_1_1 ≅ [Hesse_U / SL2(F3)]"
            level_structure = "Gamma(3)"
        elif n == 2:
            presentation = "M_1_2 ≅ [Hesse_univ_curve_minus_0 / SL2(F3)]"
            level_structure = "Gamma(3)_universal_curve"
        else:
            presentation = f"M_1_{n} ≅ [Hesse_marked_configuration / SL2(F3)]"
            level_structure = "Gamma(3)_marked_configuration"
        return {
            "covering_space": domain,
            "group": group,
            "group_order": int(cast(Any, group).order()),
            "finite_etale_groupoid": True,
            "covering_unramified_stamp": True,
            "covering_smooth_stamp": True,
            "covering_formally_etale_stamp": True,
            "degree": 24,
            "level_structure": level_structure,
            "presentation": presentation,
        }

    def igusa_quotient_presentation(self) -> dict[str, object] | None:
        r"""Inspectable ``(U, S₆)`` data when the Igusa binary-sextic cover is owned.

        Returns ``None`` unless this is open unmarked ``M_{2,0}`` over a base with
        ``2`` invertible. Covering space
        :func:`_igusa_open_M20_affine_scheme` (dense open of ``M_{0,6}`` /
        binary sextics after ``PGL₂`` normalization); ``G = S₆ ≅ Sp₄(𝔽₂)`` of
        order ``720``. Covers a dense open of open ``M_2`` — **not** a scheme
        isomorphism, and **not** a compact ``Mbar_2`` atlas.
        """
        if self.genus() != 2 or self.number_of_markings() != 0 or self.is_proper():
            return None
        if not _two_is_invertible(self.base_scheme()):
            return None
        domain = _moduli_etale_atlas_domain(self)
        if domain is None:
            return None
        group = _igusa_galois_group()
        from typing import Any, cast

        return {
            "covering_space": domain,
            "group": group,
            "group_order": int(cast(Any, group).order()),
            "finite_etale_groupoid": True,
            "covering_unramified_stamp": True,
            "covering_smooth_stamp": True,
            "covering_formally_etale_stamp": True,
            "degree": 720,
            "level_structure": "Igusa_binary_sextic_Sp4_F2",
            "presentation": "M_2 ≅ [Igusa_binary_sextic_U / S6] (dense open)",
            "construction": "igusa_binary_sextic_PGL2",
            "coverage": "dense_open_of_open_M_2",
        }

    def weierstrass_gm_presentation(self) -> dict[str, object] | None:
        r"""Owned Weierstrass ``𝔾_m`` presentation when Legendre/Hesse are unavailable.

        Returns inspectable evidence for ``(1,1)`` / ``(1,2)`` over bases where
        neither ``2`` nor ``3`` is a unit (prototype: ``Spec(ℤ)``):

        - Open ``M_{1,1}``: Tate–Weierstrass affine
          ``Spec(R[a₁,…,a₆][Δ⁻¹])`` with weighted ``𝔾_m``.
        - Open ``M_{1,2}``: Weierstrass universal-curve affine over that base.
        - Proper ``Mbar_{1,*}``: same open affine as covering evidence; compact
          Deligne–Rapoport likewise uses non-finite ``𝔾_m`` (no finite étale
          groupoid stamp).

        Always stamps ``finite_etale_groupoid=False``, ``equation_level=False``,
        ``group_infinite=True``: ``𝔾_m`` is not a finite group, so this cannot
        enter the finite-étale-groupoid proving set used for Legendre / Hesse.
        The covering ``U → [U/𝔾_m]`` is smooth of relative dimension ``1``, not
        étale — so :meth:`etale_atlas` stays formal. Does **not** stamp
        equation-level True.
        """
        if self.genus() != 1 or self.number_of_markings() not in (1, 2):
            return None
        base = self.base_scheme()
        if not _legendre_and_hesse_unavailable(base):
            return None
        n = self.number_of_markings()
        if n == 1:
            domain = AffineAlgebraicSpace(_weierstrass_M11_affine_scheme(base))
            if self.is_proper():
                presentation = "Mbar_1_1 ≅ [Weierstrass_U / Gm] (smooth Artin; Gm infinite)"
                level_structure = "Deligne-Rapoport_Weierstrass_compact"
            else:
                presentation = "M_1_1 ≅ [Weierstrass_U / Gm] (smooth Artin; Gm infinite)"
                level_structure = "Deligne-Rapoport_Weierstrass"
        else:
            domain = AffineAlgebraicSpace(_weierstrass_M12_affine_scheme(base))
            if self.is_proper():
                presentation = "Mbar_1_2 ≅ [Weierstrass_univ_curve / Gm] (smooth Artin; Gm infinite)"
                level_structure = "Deligne-Rapoport_Weierstrass_universal_curve_compact"
            else:
                presentation = "M_1_2 ≅ [Weierstrass_univ_curve / Gm] (smooth Artin; Gm infinite)"
                level_structure = "Deligne-Rapoport_Weierstrass_universal_curve"
        return {
            "covering_space": domain,
            "group_kind": "Gm",
            "group_infinite": True,
            "group_order": None,
            "finite_etale_groupoid": False,
            "covering_unramified_stamp": False,
            "covering_smooth_stamp": True,
            "covering_formally_etale_stamp": False,
            "equation_level": False,
            "covering_kind": "weierstrass_gm_smooth_quotient",
            "level_structure": level_structure,
            "presentation": presentation,
            "proof_not_finite_etale": (
                "Weighted Gm acting on the Weierstrass affine is an infinite group scheme; "
                "U → [U/Gm] is smooth of relative dimension 1, not finite étale. "
                "Finite-étale-groupoid equation-level certificates require finite G "
                "(Legendre S3 / Hesse SL2(F3))."
            ),
        }

    def etale_atlas_gap(self) -> dict[str, object] | None:
        r"""Named fail-closed gap when no equation-level étale atlas is owned.

        Dispatches through :mod:`dm_moduli_spike.moduli.atlas_ownership`.
        Returns ``None`` precisely when :meth:`etale_atlas` matches an owned
        proving-set presentation. For ``(1,*)`` when neither Legendre nor Hesse
        applies, Weierstrass ``𝔾_m`` is owned as fail-closed evidence (not
        equation-level). Remaining pre-#225 atlas debt is general ``(g,n)``.
        """
        from .atlas_ownership import etale_atlas_gap_from_registry

        return etale_atlas_gap_from_registry(self)

    def owned_etale_atlas_presentation(self) -> OwnedAtlasPresentation | None:
        r"""Matched :class:`~.atlas_ownership.OwnedAtlasPresentation` row, or ``None``."""
        from .atlas_ownership import resolve_owned_etale_atlas

        return resolve_owned_etale_atlas(self)

    def etale_atlas(self) -> AtlasMorphism:
        r"""Étale atlas ``U → ℳ`` via the owned-presentation registry.

        Single dispatch: :func:`~.atlas_ownership.dispatch_etale_atlas`. Owned
        ``(g,n,proper)`` rows (see
        :func:`~.atlas_ownership.owned_etale_atlas_presentations`) yield
        equation-level domains; unowned types and failed genus-1 base hypotheses
        fail closed to a formal
        :class:`~dm_moduli_spike.geometry.stacks.AtlasChart` with
        :meth:`etale_atlas_gap`. Never uses the coarse space as an étale domain.
        """
        from .atlas_ownership import dispatch_etale_atlas

        return dispatch_etale_atlas(self)

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
