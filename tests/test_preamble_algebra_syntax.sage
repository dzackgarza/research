r"""Preamble syntax and algebra-contract tests for framed/free algebras.

These tests define the intended user-facing syntax for `R`-algebras in the
`preamble`, intentionally in positive form:

- `FreeAlgebraOn(R, S)` for arbitrary sets `S`, including `S = Δ[n]` and `S = NN`.
- Explicit access to algebra generators and their generating set as construction data.
- Free-algebra maps induced from finite/explicit generator data.
"""

from pathlib import Path

from sage.categories.homset import Hom
from sage.categories.morphism import Morphism, SetMorphism
from typing import cast
from sage.rings.ideal import Ideal_pid
from sage.structure.element import Element
from sage.structure.parent import Parent
import pytest
import dzack_research


def _ensure_preamble() -> None:
    """Load the preamble scripts once per test module."""
    if "FreeAlgebraOn" in globals():
        return
    preamble_path = Path(dzack_research.__file__).resolve().parent / "preamble"
    load(str(preamble_path / "install.sage"))


def _assert_algebra_membership(base: Parent, algebra: Parent, structure_map: Morphism) -> None:
    assert algebra in Algebras(base), (
        f"{algebra} is not an explicit object of Algebras({base})"
    )
    assert algebra.algebra_structure_map() is structure_map


def _assert_fractional_ideal_generators(ideal: Ideal_pid, ring: Parent, expected_gens: tuple) -> None:
    """Check that ideal generators and module generators are the same generating family."""
    module_category = Modules(ring)
    assert ideal in module_category, (
        f"{ideal} is not an explicit object of Modules({ring})"
    )
    module_generators = tuple(ideal.module_generators())
    ideal_gens = tuple(ideal.gens())
    expected = tuple(expected_gens)

    assert set(module_generators) == set(ideal_gens)
    assert set(module_generators) == set(expected)


def test_free_algebra_on_delta_records_the_generating_set() -> None:
    """`FreeAlgebraOn(QQ, Δ[n])` exposes its generating set and algebra generators."""
    _ensure_preamble()
    S = Sets.Δ[2]
    A = FreeAlgebraOn(QQ, S)

    assert A.base_ring() == QQ
    assert A.algebra_generating_set() == S
    assert A.generating_set() == S
    assert A.algebra_generator_morphism().domain() == S
    assert tuple(A.algebra_generators()) == tuple(A.algebra_generator(s) for s in S)
    assert A.algebra_generator(0) in A
    assert A.generator(0) == A.algebra_generator(0)
    assert A.algebra_generator_morphism()(S.an_element()) in A
    assert A.algebra_gens() == S.cardinality()
    assert A.module_gens() == A.module_generating_set().cardinality()


def test_free_algebra_delta_constructor_matches_algebras_free_category() -> None:
    """`Algebras(QQ).Free().on(Δ[n])` is the same object as `FreeAlgebraOn`."""
    _ensure_preamble()
    S = Sets.Δ[3]
    A = Algebras(QQ).Free().on(S)
    B = FreeAlgebraOn(QQ, S)

    assert A == B
    assert A.algebra_generating_set() == S
    assert A.generator(S.an_element()) == B.generator(S.an_element())


def test_delta_countable_alias_for_aleph_zero() -> None:
    """`Δ[ℵ[0]]` is the countable simplex indexing object."""
    _ensure_preamble()
    assert Sets.ℵ[0] == NN.cardinality()
    assert Sets.Δ[Sets.ℵ[0]] == NN


def test_aleph_indices_are_cardinalities() -> None:
    """`ℵ[n]` returns expected cardinalities for supported indices."""
    _ensure_preamble()
    assert Sets.ℵ[0] == NN.cardinality()
    assert Sets.ℵ[1] == RR.cardinality()


def test_aleph_index_two_is_undefined() -> None:
    """`ℵ[n]` is only defined for `n=0` and `n=1`."""
    _ensure_preamble()

    with pytest.raises(ValueError):
        _ = Sets.ℵ[2]


def test_free_algebra_on_delta_aleph_zero_is_free_algebra_on_naturals() -> None:
    """`Δ[ℵ[0]]` constructs the same free algebra as `NN`."""
    _ensure_preamble()
    A = FreeAlgebraOn(QQ, Sets.Δ[Sets.ℵ[0]])

    assert A.algebra_generating_set() == NN
    assert A.algebra_generator(0) in A
    assert A.algebra_generator(7) in A
    assert A.generator(0) == A.algebra_generator(0)
    assert A.generator(7) == A.algebra_generator(7)
    assert A.algebra_gens() == NN.cardinality()
    assert A.module_gens() == A.module_generating_set().cardinality()

    shift = SetMorphism(
        Hom(NN, NN, Sets()),
        lambda n: n + 1,
    )
    shifted = A.induced_hom(shift, A)
    assert shifted(A.algebra_generator(0) * A.algebra_generator(7)) == (
        A.algebra_generator(1) * A.algebra_generator(8)
    )


def test_free_algebra_on_delta_aleph_zero_and_NN_match_via_free_category() -> None:
    """`Algebras(QQ).Free().on(Δ[ℵ[0]])` matches `Algebras(QQ).Free().on(NN)`."""
    _ensure_preamble()
    A = Algebras(QQ).Free().on(Sets.Δ[Sets.ℵ[0]])
    B = Algebras(QQ).Free().on(NN)
    NN_generators = Set(NN)

    assert A.algebra_generating_set() == NN
    assert B.algebra_generating_set() == NN
    assert A.algebra_generator_morphism().domain() == NN_generators
    assert B.algebra_generator_morphism().domain() == NN_generators


def test_free_algebra_on_natural_numbers_has_countable_generators() -> None:
    """`FreeAlgebraOn(QQ, NN)` accepts an infinite indexing set."""
    _ensure_preamble()
    A = FreeAlgebraOn(QQ, NN)

    assert A.algebra_generating_set() == NN
    assert A.algebra_generator(0) in A
    assert A.algebra_generator(7) in A
    assert A.generator(0) == A.algebra_generator(0)
    assert A.generator(7) == A.algebra_generator(7)
    assert A.generator(0).underlying_set_element() == 0
    assert A.generator(7).underlying_set_element() == 7
    assert A.algebra_gens() == NN.cardinality()
    assert A.module_gens() == A.module_generating_set().cardinality()


def test_free_algebra_does_not_treat_lists_or_tuples_as_elements() -> None:
    """Numeric vectors and tuples are not algebra elements by construction."""
    _ensure_preamble()
    A = FreeAlgebraOn(QQ, Sets.Δ[2])

    assert (1, 0) not in A
    assert [1, 0] not in A
    assert (A.algebra_generator(0), A.algebra_generator(1)) not in A


def test_free_algebra_map_from_set_morphism_is_generator_determined() -> None:
    """`induced_hom` is determined on generators and extends multiplicatively."""
    _ensure_preamble()
    source = Sets.Δ[1]
    target = Sets.Δ[2]
    A = FreeAlgebraOn(QQ, source)
    B = FreeAlgebraOn(QQ, target)

    embedding = SetMorphism(Hom(source, target, Sets()), lambda s: s + 1)
    induced = A.induced_hom(embedding, B)

    assert induced(A.algebra_generator(0)) == B.algebra_generator(1)
    assert induced(A.algebra_generator(1)) == B.algebra_generator(2)
    assert (
        induced(A.algebra_generator(0) * A.algebra_generator(1))
        == B.algebra_generator(1) * B.algebra_generator(2)
    )


def test_finitely_generated_free_algebra_hom_from_generator_images() -> None:
    """A finite free algebra map is specified by a generator-function."""
    _ensure_preamble()
    source = FreeAlgebraOn(QQ, Sets.Δ[3])
    target = FreeAlgebraOn(QQ, Sets.Δ[3])

    def image_of_monomial(monomial: Element) -> Element:
        exponent_profile = monomial.dict()
        assert len(exponent_profile) == 1
        generator_label, exponent = next(iter(exponent_profile.items()))
        assert exponent == 1
        match generator_label:
            case 0:
                return cast("Element", target.algebra_generator(2))
            case 1:
                return cast("Element", target.algebra_generator(1))
            case 2:
                return cast("Element", target.algebra_generator(0))
            case _:
                raise ValueError(f"unexpected generator label {generator_label!r}")

    hom = source.hom(image_of_monomial, target)

    assert hom(source.algebra_generator(0)) == target.algebra_generator(2)
    assert hom(source.algebra_generator(1)) == target.algebra_generator(1)
    assert hom(source.algebra_generator(2)) == target.algebra_generator(0)


def test_free_algebra_morphism_composition_and_identity() -> None:
    """Algebra maps compose in order and preserve identities."""
    _ensure_preamble()
    source = FreeAlgebraOn(QQ, Sets.Δ[2])
    bridge = FreeAlgebraOn(QQ, Sets.Δ[3])
    target = FreeAlgebraOn(QQ, Sets.Δ[2])
    terminal = FreeAlgebraOn(QQ, Sets.Δ[1])

    forward = source.hom({0: bridge.algebra_generator(1), 1: bridge.algebra_generator(2)})
    backward = bridge.hom(
        {
            0: target.algebra_generator(0),
            1: target.algebra_generator(1),
            2: target.algebra_generator(1),
        },
        target,
    )
    collapse = target.hom(
        {
            0: terminal.algebra_generator(0),
            1: terminal.algebra_generator(0),
        },
        terminal,
    )
    composed = forward.then(backward)
    collapsed = composed.then(collapse)
    staged = forward.then(backward.then(collapse))

    assert composed(source.algebra_generator(0)) == target.algebra_generator(1)
    assert composed(source.algebra_generator(1)) == target.algebra_generator(1)
    assert composed(source.algebra_generator(0) * source.algebra_generator(1)) == (
        target.algebra_generator(1) * target.algebra_generator(1)
    )
    assert collapsed(source.algebra_generator(0)) == terminal.algebra_generator(0)
    assert collapsed(source.algebra_generator(1)) == terminal.algebra_generator(0)
    assert collapsed(source.algebra_generator(0) * source.algebra_generator(1)) == (
        terminal.algebra_generator(0) ^ 2
    )
    assert collapsed(source.algebra_generator(0) * source.algebra_generator(1)) == staged(
        source.algebra_generator(0) * source.algebra_generator(1)
    )

    assert composed.domain() is source
    assert composed.codomain() is target

    identity = source.Hom(source).identity()
    assert identity(source.algebra_generator(0)) == source.algebra_generator(0)
    assert forward.then(backward)(source.algebra_generator(0)) == composed(source.algebra_generator(0))
    assert forward.then(backward)(source.algebra_generator(1)) == composed(source.algebra_generator(1))

    assert collapsed(source.algebra_generator(0)) == staged(source.algebra_generator(0))
    assert collapsed(source.algebra_generator(1)) == staged(source.algebra_generator(1))

    identity_terminal = terminal.Hom(terminal).identity()
    assert identity_terminal(terminal.algebra_generator(0)) == terminal.algebra_generator(
        0
    )
    assert forward.then(backward.then(collapse))(source.algebra_generator(0)) == collapsed(
        source.algebra_generator(0)
    )

    identity_target = target.Hom(target).identity()
    assert forward(source.algebra_generator(0)) == forward.then(identity_target)(source.algebra_generator(0))
    assert forward(source.algebra_generator(1)) == forward.then(identity_target)(source.algebra_generator(1))


def test_finitely_presented_algebra_remembers_presentation_data() -> None:
    """A finitely presented algebra exposes its free presentation explicitly."""
    _ensure_preamble()

    source = FreeAlgebraOn(QQ, Sets.Δ[2])
    relation = source.algebra_generator(0) * source.algebra_generator(1)
    presented = FinitelyPresentedAlgebra(source, [relation])

    assert presented in FinitelyPresentedAlgebras(QQ)
    assert presented.presentation_ring() is source
    assert presented.presentation_ideal()
    assert presented.algebra_generator_morphism().domain() == source.algebra_generating_set()
    assert presented.algebra_generating_set() == source.algebra_generating_set()
    assert tuple(presented.algebra_generators()) == (
        presented.algebra_generator(0),
        presented.algebra_generator(1),
    )
    assert presented.algebra_framing_morphism() is presented.algebra_presentation_morphism()
    assert presented.algebra_presentation_morphism()(relation) == presented.zero()
    assert relation in presented.presentation_ideal()
    assert tuple(presented.relations()) == (relation,)

    free_for_shortcut = FreeAlgebraOn(QQ, Sets.Δ[2])
    by_generators = FGAlgebra(
        QQ,
        Sets.Δ[2],
        [
            free_for_shortcut.algebra_generator(0)
            * free_for_shortcut.algebra_generator(1),
        ],
    )
    assert by_generators in FinitelyPresentedAlgebras(QQ)
    assert by_generators.presentation_ring().algebra_generating_set() == free_for_shortcut.algebra_generating_set()


def test_finitely_presented_algebra_accepts_ideal_input_as_relations() -> None:
    """Passing an ideal as relations stores its ideal module_generators."""
    _ensure_preamble()

    source = FreeAlgebraOn(QQ, Sets.Δ[2])
    rel0 = source.algebra_generator(0) * source.algebra_generator(1)
    rel1 = source.algebra_generator(0) ** 2
    presentation_ideal = source.ideal((rel0, rel1))
    presented = FinitelyPresentedAlgebra(source, presentation_ideal)

    assert len(presented.relations()) == 2
    assert presented.presentation_ideal() is presentation_ideal
    assert rel0 in presented.relations()
    assert rel1 in presented.relations()


def test_finitely_presented_algebra_base_change_is_explicit() -> None:
    """Base-changing a finitely presented algebra transports its relations explicitly."""
    _ensure_preamble()
    source = FreeAlgebraOn(QQ, Sets.Δ[2])
    relation = source.algebra_generator(0) * source.algebra_generator(1)
    presented = FinitelyPresentedAlgebra(source, [relation])

    ring_hom = ComplexField().coerce_map_from(QQ)
    if ring_hom is None:
        raise AssertionError("expected QQ-to-ComplexField coerce map")
    changed = presented.base_change(ring_hom)

    assert changed in FinitelyPresentedAlgebras(ComplexField())
    assert changed.base_ring() is ComplexField()
    assert changed.algebra_generating_set() == source.algebra_generating_set()
    assert changed.algebra_generator(0) in changed
    assert changed.algebra_presentation_morphism()(changed.algebra_generator(0) * changed.algebra_generator(1)) == changed.zero()
    assert changed.presentation_ideal().contains(
        changed.algebra_generator(0) * changed.algebra_generator(1)
    )


def test_finitely_presented_algebra_base_change_transports_coefficients() -> None:
    """Base-change on finitely presented algebras applies coefficient maps."""
    _ensure_preamble()
    source = FreeAlgebraOn(ZZ, Sets.Δ[1])
    relation = ZZ(2) * source.algebra_generator(0)
    presented = FinitelyPresentedAlgebra(source, [relation])

    ring_hom = ComplexField().coerce_map_from(ZZ)
    if ring_hom is None:
        raise AssertionError("expected ZZ-to-ComplexField coerce map")
    changed = presented.base_change(ring_hom)

    mapped_relation = ComplexField(2) * changed.algebra_generator(0)
    assert changed.presentation_ideal().contains(mapped_relation)


def test_algebra_parent_base_change_rejects_invalid_map() -> None:
    """`Algebra.base_change` requires a morphism from the declared base ring."""
    _ensure_preamble()
    A = PolynomialRing(QQ, "t")
    invalid_map = RealField().coerce_map_from(ZZ)
    if invalid_map is None:
        raise AssertionError("expected invalid-map precondition to produce a map")

    with pytest.raises(AssertionError):
        A.base_change(invalid_map)


def test_free_algebra_linear_combination_is_not_front_door() -> None:
    """`linear_combination` is not a user-facing constructor for free-algebra elements."""
    _ensure_preamble()
    A = FreeAlgebraOn(QQ, Sets.Δ[1])

    with pytest.raises(NotImplementedError):
        A.linear_combination({0: A.algebra_generator(0)})


def test_polynomial_ring_standard_syntax_and_isomorphism() -> None:
    """`R.<x,y> = PolynomialRing(QQ, 2)` drives explicit free-algebra maps."""
    _ensure_preamble()
    R.<x, y> = PolynomialRing(QQ, 2)
    source = FreeAlgebraOn(QQ, Sets.Δ[2])
    images = {0: x, 1: y}

    def monomial_to_polynomial(monomial: Element) -> Element:
        polynomial = R.one()
        for generator_label, exponent in monomial.dict().items():
            assert generator_label in images
            polynomial *= images[generator_label] ** exponent
        return polynomial

    to_polynomial = source.hom(monomial_to_polynomial, R)
    from_polynomial = R.hom([source.algebra_generator(0), source.algebra_generator(1)], source)

    element = source.algebra_generator(0)^2 + source.algebra_generator(1)
    polynomial = x^2 + y
    assert to_polynomial(element) == polynomial
    assert from_polynomial(polynomial) == element
    assert to_polynomial(from_polynomial(polynomial)) == polynomial
    assert from_polynomial(to_polynomial(element)) == element


def test_finite_free_algebra_set_permutation_is_isomorphism() -> None:
    """A set permutation induces an explicit algebra isomorphism."""
    _ensure_preamble()
    source = FreeAlgebraOn(QQ, Sets.Δ[3])
    target = FreeAlgebraOn(QQ, Sets.Δ[3])

    forward_set_map = SetMorphism(
        Hom(source.algebra_generating_set(), target.algebra_generating_set(), Sets()),
        lambda i: (i + 1) % 3,
    )
    backward_set_map = SetMorphism(
        Hom(target.algebra_generating_set(), source.algebra_generating_set(), Sets()),
        lambda i: (i - 1) % 3,
    )

    forward = source.induced_hom(forward_set_map, target)
    backward = target.induced_hom(backward_set_map, source)

    element = source.algebra_generator(0) * source.algebra_generator(2)
    assert forward(element) == target.algebra_generator(1) * target.algebra_generator(0)
    assert backward(forward(element)) == element


def test_standard_rings_have_explicit_base_maps() -> None:
    """Standard rings are explicit objects of the expected algebra categories."""
    _ensure_preamble()

    base = ZZ
    algebra = QQ
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(2)) == algebra(2)
    assert structure_map(base(-3)) == algebra(-3)

    base = QQ
    algebra = QQ
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(2)) == algebra(2)
    assert structure_map(base(-3)) == algebra(-3)

    base = ZZ
    algebra = GF(7)
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(2)) == algebra(2)
    assert structure_map(base(6)) == algebra(-1)

    base = GF(7)
    algebra = GF(7)
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(3)) == algebra(3)
    assert structure_map(base(6)) == algebra(-1)

    R.<x, y> = PolynomialRing(QQ, 2)
    base = QQ
    algebra = R
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(2)) == algebra(2)
    assert structure_map(base(3)) in algebra

    S = LaurentPolynomialRing(QQ, "t")
    base = QQ
    algebra = S
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(2)) == algebra(2)
    assert structure_map(base(3)) in algebra

    K.<a> = QuadraticField(2, "a")
    base = QQ
    algebra = K
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(-1)) == algebra(-1)
    assert structure_map(base(2)) == algebra(2)

    base = ZZ
    algebra = K
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(3)) == algebra(3)
    assert structure_map(base(-4)) == algebra(-4)

    real = RealField()
    complex_ = ComplexField()
    base = ZZ
    algebra = real
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(2)) == algebra(2)

    base = QQ
    algebra = real
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(2)) == algebra(2)

    base = QQ
    algebra = complex_
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(2)) == algebra(2)

    base = QQ
    algebra = QQbar
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)
    assert structure_map(base.zero()) == algebra.zero()
    assert structure_map(base.one()) == algebra.one()
    assert structure_map(base(2)) == algebra(2)
    assert structure_map(base(-1)) == algebra(-1)


def test_standard_ring_has_distinct_base_maps() -> None:
    """The same ring can be explicit in multiple base categories."""
    _ensure_preamble()
    algebra = QQ
    map_zz_to_qq = algebra.coerce_map_from(ZZ)
    map_qq_to_qq = algebra.coerce_map_from(QQ)
    assert algebra in Algebras(ZZ), f"{algebra} is not an object of Algebras(ZZ)"
    assert algebra in Algebras(QQ), f"{algebra} is not an object of Algebras(QQ)"
    assert map_zz_to_qq.domain() is ZZ
    assert map_qq_to_qq.domain() is QQ
    assert map_zz_to_qq(ZZ(3)) == algebra(3)
    assert map_qq_to_qq(QQ(3)) == algebra(3)


def test_constructed_rings_are_explicit_objects_of_expected_algebra_categories() -> None:
    """Standard algebra constructions carry explicit algebra-membership checks."""
    _ensure_preamble()

    base = QQ
    algebra = PowerSeriesRing(QQ, "t")
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)

    algebra = FractionField(PolynomialRing(QQ, "x"))
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)

    R.<x> = PolynomialRing(QQ, 1)
    algebra = R.quotient(x^2 + 1)
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)

    algebra = MatrixAlgebra(QQ, 3)
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)

    base = ZZ
    algebra = PolynomialRing(QQ, 2)
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)

    algebra = MatrixAlgebra(ZZ, 2)
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)


def test_integral_and_fractional_Z_ideals_are_explicit_modules() -> None:
    """`ZZ` ideals and their inverses match `module_generators()` with `gens()`."""
    _ensure_preamble()
    R = ZZ
    principal = R.ideal(12)
    principal_inverse = principal.inverse()
    second = R.ideal(7).inverse()

    _assert_fractional_ideal_generators(principal, R, (R(12),))
    _assert_fractional_ideal_generators(
        principal_inverse, R, (QQ(1, 12),)
    )
    _assert_fractional_ideal_generators(
        second, R, (QQ(1, 7),)
    )


def test_fractional_ideals_in_quadratic_integer_rings_are_explicit_modules() -> None:
    """Quadratic-order ideals verify ideal generators equal module generators."""
    _ensure_preamble()
    K.<a> = QuadraticField(2, "a")
    R = K.ring_of_integers()

    principal = R.ideal(2)
    principal_inverse = principal.inverse()
    mixed = R.ideal(2, a)
    shifted = R.ideal(3, a + 1)

    _assert_fractional_ideal_generators(principal, R, (R(2),))
    _assert_fractional_ideal_generators(principal_inverse, R, (K(1) / 2,))
    _assert_fractional_ideal_generators(
        mixed, R, (R(2), R(a))
    )
    _assert_fractional_ideal_generators(
        shifted, R, (R(3), R(a + 1))
    )
