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
from sage.structure.element import Element
from sage.structure.parent import Parent
import pytest
import dzack_research


def _ensure_preamble() -> None:
    """Load the preamble scripts once per test module."""
    if "FreeAlgebraOn" in globals():
        return
    preamble_path = Path(dzack_research.__file__).resolve().parent / "preamble"
    from dzack_research.preamble.install import install_preamble
    install_preamble(globals())
def _assert_algebra_membership(base: Parent, algebra: Parent, structure_map: Morphism) -> None:
    # A Sage ring is not asked owned questions: an R-algebra is the ring map
    # R -> A, and own_algebra constructs the object that answers them.
    owned = own_algebra(structure_map)
    assert owned in Algebras(base), (
        f"{algebra} is not an explicit object of Algebras({base})"
    )
    assert owned.algebra_structure_map() is structure_map


def _assert_fractional_ideal_generators(
    ideal: "FractionalIdeal",
    ring: Parent,
    expected_gens: "OrderedSet",
) -> None:
    """Check the ideal is the R-submodule its family generates.

    There is no second family to compare against: an ideal is an
    R-submodule of R, so the generators of the ideal are the generators of
    the module under one word.  What is checkable is that the family is the
    expected one, and -- when the ideal is integral -- that the submodule it
    names includes into R with the same image.

    Image, not family.  A supplied family need not be a basis: $(2)$ arrives
    from the order as $(2, 2a)$, while the submodule is free of rank one, so
    its inclusion has one column and could not list two generators.  Equal
    images is the statement that survives, and it is the statement that says
    the two objects are the same submodule.
    """
    module_category = Modules(ring)
    assert ideal in module_category, (
        f"{ideal} is not an explicit object of Modules({ring})"
    )
    module_generators = tuple(ideal.module_generators())
    expected = tuple(expected_gens)
    assert set(module_generators) == set(expected)

    if all(generator in ring for generator in module_generators):
        submodule = ideal.as_submodule()
        inclusion = submodule.embedding()
        assert inclusion.codomain().base_ring() is ring, (
            "an integral ideal includes into R read as a module over itself"
        )
        assert submodule.rank() == 1, (
            "a nonzero ideal of a domain is free of rank one as a module"
        )
        spanning, = inclusion.matrix()._sage_matrix().list()
        assert all(
            ring(generator) / spanning in ring
            for generator in module_generators
        ), "every generator of the ideal lies in the image of the inclusion"
        assert spanning in ideal, (
            "and the image lies in the ideal, so the two submodules are one"
        )


def test_free_algebra_on_delta_records_the_generating_set() -> None:
    """`FreeAlgebraOn(QQ, Δ[n])` exposes its generating set and algebra generators."""
    _ensure_preamble()
    S = Sets.Δ[2]
    A = FreeAlgebraOn(QQ, S)

    assert A.base_ring() == QQ
    assert A.algebra_generating_set() == S
    # The module framing is Mon(S), not S: the degree-two monomial x_0 x_1 is a
    # module generator, and the module generator it names is the product of the
    # two algebra generators.
    monomials = A.monomial_system()
    assert A.module_generator(monomials.generator(0) * monomials.generator(1)) == (
        A.algebra_generator(0) * A.algebra_generator(1)
    )
    assert A.algebra_generator_morphism().domain() == S
    assert tuple(A.algebra_generators()) == tuple(A.algebra_generator(s) for s in S)
    assert A.algebra_generator(0) in A
    assert A.algebra_generator_morphism()(S.an_element()) in A
    assert A.number_of_algebra_generators() == S.cardinality()
    assert A.number_of_module_generators() == A.module_generating_set().cardinality()


def test_free_algebra_delta_constructor_matches_algebras_free_category() -> None:
    """`Algebras(QQ).Free().on(Δ[n])` is the same object as `FreeAlgebraOn`."""
    _ensure_preamble()
    S = Sets.Δ[3]
    A = Algebras(QQ).Free().on(S)
    B = FreeAlgebraOn(QQ, S)

    assert A == B
    assert A.algebra_generating_set() == S
    assert A.algebra_generator(S.an_element()) == B.algebra_generator(S.an_element())


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

    with pytest.raises(AssertionError):
        _ = Sets.ℵ[2]


def test_free_algebra_on_delta_aleph_zero_is_free_algebra_on_naturals() -> None:
    """`Δ[ℵ[0]]` constructs the same free algebra as `NN`."""
    _ensure_preamble()
    A = FreeAlgebraOn(QQ, Sets.Δ[Sets.ℵ[0]])

    assert A.algebra_generating_set() == NN
    assert A.algebra_generator(0) in A
    assert A.algebra_generator(7) in A
    assert A.number_of_algebra_generators() == NN.cardinality()
    assert A.number_of_module_generators() == A.module_generating_set().cardinality()

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
    assert A.algebra_generator(0).underlying_set_element() == 0
    assert A.algebra_generator(7).underlying_set_element() == 7
    assert A.number_of_algebra_generators() == NN.cardinality()
    assert A.number_of_module_generators() == A.module_generating_set().cardinality()


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

    def image_of_generator(label: Element) -> Element:
        match label:
            case 0:
                return cast("Element", target.algebra_generator(2))
            case 1:
                return cast("Element", target.algebra_generator(1))
            case 2:
                return cast("Element", target.algebra_generator(0))
            case 3:
                return cast("Element", target.algebra_generator(3))
            case _:
                assert False, f"unexpected generator label {label!r}"

    hom = source.hom(image_of_generator, target)

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

    # An assignment names where *every* generator goes: a map on $S$ is the
    # whole of an algebra map's data, so a partial one names nothing.
    forward = source.hom(
        {
            0: bridge.algebra_generator(1),
            1: bridge.algebra_generator(2),
            2: bridge.algebra_generator(0),
        }
    )
    backward = bridge.hom(
        {
            0: target.algebra_generator(0),
            1: target.algebra_generator(1),
            2: target.algebra_generator(1),
            3: target.algebra_generator(2),
        },
        target,
    )
    collapse = target.hom(
        {
            0: terminal.algebra_generator(0),
            1: terminal.algebra_generator(0),
            2: terminal.algebra_generator(1),
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

    # $f$ composes with the identity on *its own* codomain, which is the
    # bridge; $\mathrm{id}_{target}$ is not composable with $f$ at all.
    identity_bridge = bridge.Hom(bridge).identity()
    assert forward(source.algebra_generator(0)) == forward.then(identity_bridge)(source.algebra_generator(0))
    assert forward(source.algebra_generator(1)) == forward.then(identity_bridge)(source.algebra_generator(1))


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
    # $\Delta[2]=\{0,1,2\}$: three generators, and the quotient keeps all of
    # them -- a relation removes elements, not generators.
    assert tuple(presented.algebra_generators()) == (
        presented.algebra_generator(0),
        presented.algebra_generator(1),
        presented.algebra_generator(2),
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

    # $\QQ\subset\CC$, so a ring map to base-change along exists; the engine
    # produces it as the coercion.  Its absence would be a missing embedding,
    # not a missing test fixture, so it is asserted rather than guarded.
    ring_hom = ComplexField().coerce_map_from(QQ)
    assert ring_hom is not None, (
        "QQ embeds in CC, so there is a ring map QQ -> CC"
    )
    changed = presented.base_change(ring_hom)

    assert changed in FinitelyPresentedAlgebras(ComplexField())
    assert changed.base_ring() is ComplexField()
    assert changed.algebra_generating_set() == source.algebra_generating_set()
    assert changed.algebra_generator(0) in changed
    # $\pi$ and the ideal both live over the presentation ring; the
    # quotient's generators are their images, not their arguments.
    free = changed.presentation_ring()
    changed_relation = free.algebra_generator(0) * free.algebra_generator(1)
    assert changed.algebra_presentation_morphism()(changed_relation) == changed.zero()
    assert changed_relation in changed.presentation_ideal()


def test_finitely_presented_algebra_base_change_transports_coefficients() -> None:
    """Base-change on finitely presented algebras applies coefficient maps."""
    _ensure_preamble()
    source = FreeAlgebraOn(ZZ, Sets.Δ[1])
    relation = ZZ(2) * source.algebra_generator(0)
    presented = FinitelyPresentedAlgebra(source, [relation])

    ring_hom = ComplexField().coerce_map_from(ZZ)
    assert ring_hom is not None, (
        "ZZ embeds in CC, so there is a ring map ZZ -> CC"
    )
    changed = presented.base_change(ring_hom)

    # ``ComplexField(2)`` is the field with 2 bits of precision, not the
    # number 2; the transported coefficient is $2\in\mathbb C$.
    free = changed.presentation_ring()
    mapped_relation = ComplexField()(2) * free.algebra_generator(0)
    assert mapped_relation in changed.presentation_ideal()


def test_algebra_parent_base_change_rejects_invalid_map() -> None:
    """`Algebra.base_change` requires a morphism from the declared base ring."""
    _ensure_preamble()
    A = own_algebra(PolynomialRing(QQ, "t").coerce_map_from(QQ))
    # A real ring map, wrong for this algebra: $\ZZ\subset\RR$ gives a map,
    # and it does not start at $\QQ$, which is what makes it the test case.
    invalid_map = RealField().coerce_map_from(ZZ)
    assert invalid_map is not None, (
        "ZZ embeds in RR, so there is a ring map ZZ -> RR"
    )

    with pytest.raises(AssertionError):
        A.base_change(invalid_map)


def test_free_algebra_linear_combination_is_not_front_door() -> None:
    """`linear_combination` is not a user-facing constructor for free-algebra elements."""
    _ensure_preamble()
    A = FreeAlgebraOn(QQ, Sets.Δ[1])

    with pytest.raises(AssertionError):
        A.linear_combination({0: A.algebra_generator(0)})


def test_polynomial_ring_standard_syntax_and_isomorphism() -> None:
    """`R.<x,y> = PolynomialRing(QQ, 2)` drives explicit free-algebra maps."""
    _ensure_preamble()
    R.<x, y> = PolynomialRing(QQ, 2)
    # $\Delta[1]=\{0,1\}$: two generators, matching $x$ and $y$.  The
    # isomorphism is a statement about the two generating sets having the
    # same cardinality, so it does not survive a mismatch.
    source = FreeAlgebraOn(QQ, Sets.Δ[1])

    to_polynomial = source.hom({0: x, 1: y}, R)
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
    assert own_algebra(map_zz_to_qq) in Algebras(ZZ), (
        f"{algebra} is not an object of Algebras(ZZ)"
    )
    assert own_algebra(map_qq_to_qq) in Algebras(QQ), (
        f"{algebra} is not an object of Algebras(QQ)"
    )
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

    # A quotient of a free algebra is presented, not merely formed: the
    # preamble's constructor is the one that keeps the presenting ring and
    # the ideal, so $\QQ[x]/(x^2+1)$ arrives already knowing what it is a
    # quotient of.
    R.<x> = PolynomialRing(QQ, 1)
    algebra = FinitelyPresentedAlgebra(R, [x^2 + 1])
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)

    algebra = MatrixSpace(QQ, 3)
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)

    base = ZZ
    algebra = PolynomialRing(QQ, 2, "x")
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)

    algebra = MatrixSpace(ZZ, 2)
    structure_map = algebra.coerce_map_from(base)
    _assert_algebra_membership(base, algebra, structure_map)


def test_integral_and_fractional_Z_ideals_are_explicit_modules() -> None:
    """`ZZ` ideals and their inverses report the family they were built on."""
    _ensure_preamble()
    R = ZZ
    principal = R.ideal(12)
    principal_inverse = own_ideal(principal).inverse()
    second = own_ideal(R.ideal(7)).inverse()

    _assert_fractional_ideal_generators(own_ideal(principal), R, (R(12),))
    _assert_fractional_ideal_generators(
        principal_inverse, R, (QQ(1)/12,)
    )
    _assert_fractional_ideal_generators(
        second, R, (QQ(1)/7,)
    )


def test_fractional_ideals_in_quadratic_integer_rings_are_explicit_modules() -> None:
    """Quadratic-order ideals verify ideal generators equal module generators."""
    _ensure_preamble()
    K.<a> = QuadraticField(2, "a")
    R = K.ring_of_integers()

    # An ideal does not remember the family it was built from: the order
    # hands back a module basis, $(2)$ as $(2, 2a)$.  That family is the one
    # asserted -- reading the ideal's own answer back into the expectation
    # would compare it with itself -- and $2$ divides both of its members,
    # which is what $(2)$ being principal means.
    principal = own_ideal(R.ideal(2))
    assert principal.is_principal()
    assert principal.principal_generator() == R(2)
    _assert_fractional_ideal_generators(principal, R, (R(2), R(2) * R(a)))

    _assert_fractional_ideal_generators(
        principal.inverse(), R, (K(1) / 2,)
    )

    mixed = own_ideal(R.ideal([2, a]))
    _assert_fractional_ideal_generators(mixed, R, (R(2), R(a)))

    # $N(a+1) = -1$, so $a+1$ is a unit and $(3, a+1)$ is all of $R$.
    unit_ideal = own_ideal(R.ideal([3, a + 1]))
    assert unit_ideal.is_principal()
    assert unit_ideal.principal_generator().is_unit()


def test_degree_is_the_grading_and_holds_at_every_rank() -> None:
    r"""$\deg$ is the total degree, and $\deg_s$ the degree in each generator.

    $\operatorname{FreeAlg}_R(S)=R[\operatorname{Mon}(S)]$ is graded by the
    sum of exponents whatever $S$ is, and an element has finite support, so
    both are read off the framing with no engine and no chosen monomial order.
    """
    _ensure_preamble()

    A = FreeAlgebraOn(QQ, finite_ordered_set(["x"]))
    x = A.algebra_generators()[0]

    assert (x * x - 5 * A.one()).degree() == 2
    assert A.one().degree() == 0, "a nonzero constant has degree zero"
    assert A.zero().degree() == -Infinity, (
        "the zero element has no largest exponent"
    )
    assert ((x * x) * (x * x * x)).degree() == 5, (
        "the degree adds, which is the monoid operation in the framing"
    )

    space = FreeAlgebraOn(QQ, finite_ordered_set(["x", "y", "z"]))
    u, v, w = space.algebra_generators()
    f = u * u * v * w * w * w + v * v
    assert f.degree() == 6, (
        "x^2*y*z^3 has total degree six, and y^2 does not exceed it"
    )
    assert f.multidegree() == {"x": 2, "y": 2, "z": 3}, (
        "the degree in each generator is the largest exponent of it in the "
        "support, taken separately"
    )
    assert space.one().multidegree() == {}, (
        "a constant has degree zero in every generator, so nothing is nonzero"
    )


def test_roots_are_asked_only_of_an_algebra_of_rank_one() -> None:
    r"""Roots of $x^2-5$, and a refusal above rank one.

    Root finding is an algorithm, so it crosses to an engine once; the zeros
    of an element of rank two are a variety and not a set of roots, so the
    question is refused rather than answered with a coincidence.
    """
    _ensure_preamble()
    # ``AA`` in the preamble's namespace is ``AffineSpace``.
    from sage.rings.qqbar import AA as AlgebraicReals

    A = FreeAlgebraOn(QQ, finite_ordered_set(["x"]))
    x = A.algebra_generators()[0]

    over_the_reals = (x * x - 5 * A.one()).roots(ring=AlgebraicReals)
    assert [multiplicity for _, multiplicity in over_the_reals] == [1, 1], (
        "x^2 - 5 is separable, so both real roots are simple"
    )
    assert [root**2 for root, _ in over_the_reals] == [5, 5], (
        "each root squares to five, which is what makes it a root"
    )
    assert (x * x - 4 * A.one()).roots() == [(2, 1), (-2, 1)], (
        "left open, the ring is the base ring"
    )

    plane = FreeAlgebraOn(QQ, finite_ordered_set(["x", "y"]))
    refused = False
    try:
        plane.algebra_generators()[0].roots()
    except AssertionError:
        refused = True
    assert refused, (
        "the zero locus of x in QQ[x, y] is a line, and a line is not a "
        "list of roots"
    )


def test_division_and_factorisation_come_back_as_algebra_elements() -> None:
    r"""$(x-1)(x-2)(x-3)$, taken apart by the engine and returned owned.

    Division with remainder, gcd, xgcd and factorisation are algorithms, so
    they cross to the engine at the algebra's presentation -- and what comes
    back is elements of the algebra, not of the ring the engine used.
    """
    _ensure_preamble()

    A = FreeAlgebraOn(QQ, finite_ordered_set(["x"]))
    x = A.algebra_generators()[0]
    cubic = x * x * x - 6 * x * x + 11 * x - 6 * A.one()
    quadratic = x * x - 3 * x + 2 * A.one()

    quotient, remainder = cubic.quo_rem(quadratic)
    assert quotient * quadratic + remainder == cubic, (
        "quo_rem returns the division identity, in this algebra"
    )
    assert remainder == A.zero(), "the quadratic divides the cubic"
    assert quotient.parent() is A, "the quotient is an element of the algebra"

    assert cubic.gcd(quadratic) == quadratic, (
        "their gcd is the quadratic, up to the unit convention"
    )
    common, left, right = cubic.xgcd(quadratic)
    assert left * cubic + right * quadratic == common, (
        "xgcd returns a Bezout identity that holds in the algebra"
    )

    factors = cubic.irreducible_factors()
    assert len(factors) == 3 and all(
        multiplicity == 1 for _, multiplicity in factors
    ), "the cubic has three distinct linear factors"
    product = A.one()
    for factor, multiplicity in factors:
        product = product * factor**multiplicity
    assert product == cubic, "the factors multiply back to the element"
    assert not quadratic.is_irreducible()
    assert (x * x + A.one()).is_irreducible(), "x^2 + 1 is irreducible over QQ"
    assert quadratic.discriminant() == 1, "(x-1)(x-2) has discriminant one"
    assert cubic.resultant(quadratic) == 0, "they share roots, so the "\
        "resultant vanishes"


def test_evaluation_and_derivation_are_asked_by_generator() -> None:
    r"""$\partial_s$ and substitution, at any rank.

    Evaluation is the universal property of a free algebra, so it is an
    assignment on generators and a partial one leaves the others standing.
    Differentiation is a derivation, determined the same way.
    """
    _ensure_preamble()

    space = FreeAlgebraOn(QQ, finite_ordered_set(["x", "y"]))
    u, v = space.algebra_generators()
    f = u * u * v + v * v

    assert f.derivative("x") == 2 * u * v, "d/dx (x^2 y + y^2) = 2xy"
    assert f.derivative("y") == u * u + 2 * v, "d/dy (x^2 y + y^2) = x^2 + 2y"
    assert f.subs({"y": QQ(1)}) == u * u + space.one(), (
        "substituting one generator leaves the other in place"
    )
    assert f(QQ(2), QQ(3)) == QQ(21), "x^2 y + y^2 at (2, 3) is 12 + 9"

    line = FreeAlgebraOn(QQ, finite_ordered_set(["x"]))
    x = line.algebra_generators()[0]
    cubic = x * x * x - 6 * x * x + 11 * x - 6 * line.one()
    assert cubic(QQ(1)) == QQ(0) and cubic(QQ(4)) == QQ(6), (
        "the cubic vanishes at one of its roots and not elsewhere"
    )
    assert cubic.derivative() == 3 * x * x - 12 * x + 11 * line.one(), (
        "at rank one the generator to differentiate in may be left open"
    )


def test_a_number_field_is_the_quotient_by_its_defining_polynomial() -> None:
    r"""$K=\QQ[x]/(f)$, and what makes it a field is that $f$ is irreducible.

    Nothing structural is added to the quotient: the free algebra presents it,
    the ideal reduces, and $[K:\QQ]=\deg f$ because reduction leaves the
    monomials below that degree.  A reducible $f$ is refused at construction
    rather than failing later at a division.
    """
    _ensure_preamble()

    A = FreeAlgebraOn(QQ, finite_ordered_set(["x"]))
    x = A.algebra_generators()[0]
    K = own_number_field(x * x - 5 * A.one())

    assert K in OwnedNumberFields() and K in OwnedFields(), (
        "a number field is placed as a field, on the irreducibility witness"
    )
    assert K.degree() == 2, "[QQ(sqrt 5) : QQ] = deg(x^2 - 5)"
    assert K.defining_polynomial() == x * x - 5 * A.one()

    a = K.primitive_element()
    assert a * a == K(5 * A.one()), (
        "the primitive element is a root of f, which is what the quotient says"
    )
    assert (a + K(A.one()))**2 == K(6 * A.one()) + 2 * a, (
        "(1 + sqrt 5)^2 = 6 + 2 sqrt 5, after reduction"
    )

    cubic_field = own_number_field(x * x * x - 2 * A.one())
    assert cubic_field.degree() == 3, "QQ(2^(1/3)) has degree three"

    refused = False
    try:
        own_number_field(x * x - 4 * A.one())
    except AssertionError:
        refused = True
    assert refused, (
        "x^2 - 4 factors, so the quotient has zero divisors and is not a field"
    )


def test_the_arithmetic_of_a_number_field_is_answered_in_owned_terms() -> None:
    r"""$\QQ(\sqrt5)$ and $\QQ(2^{1/3})$, against their recorded invariants.

    Each of these is a computation rather than a definition, so each crosses
    to an engine once; what is checked here is the mathematics, which is
    independent of that: $d_K=5$ and $h=1$ for $\QQ(\sqrt5)$, and the cubic
    has one real place and two complex ones with $r+2s=3$.
    """
    _ensure_preamble()
    from sage.rings.qqbar import AA as AlgebraicReals

    A = FreeAlgebraOn(QQ, finite_ordered_set(["x"]))
    x = A.algebra_generators()[0]
    real_quadratic = own_number_field(x * x - 5 * A.one())
    cubic = own_number_field(x * x * x - 2 * A.one())

    assert real_quadratic.discriminant() == 5, (
        "the field discriminant of QQ(sqrt 5) is 5, not the polynomial's 20"
    )
    assert real_quadratic.signature() == (2, 0), "both places are real"
    assert real_quadratic.class_number() == 1, "QQ(sqrt 5) is principal"
    assert real_quadratic.ramified_primes() == (5,), (
        "only 5 divides the discriminant, so only 5 ramifies"
    )
    assert real_quadratic.is_galois(), "a degree-two extension is normal"

    galois = real_quadratic.galois_group()
    assert galois.cardinality() == 2, "|Gal| = [K : QQ] for a Galois extension"
    assert galois in OwnedGroups(), "the Galois group is returned as a group"

    images = real_quadratic.embedding_images(AlgebraicReals)
    assert len(images) == real_quadratic.signature()[0], (
        "an embedding into the reals is a real root of f, so there are r of them"
    )
    assert [image**2 for image in images] == [5, 5], (
        "each embedding sends the primitive element to a square root of 5"
    )

    assert cubic.signature() == (1, 1) and 1 + 2 * 1 == cubic.degree(), (
        "r + 2s = [K : QQ] is what makes the signature a decomposition"
    )
    assert cubic.discriminant() == -108
    assert not cubic.is_galois(), "x^3 - 2 does not split in QQ(2^(1/3))"
    assert cubic.galois_group().cardinality() == 6, (
        "the group of the normal closure is S_3, which is why the extension "
        "is not normal"
    )


def test_an_integral_basis_is_a_basis_of_an_underlying_R_algebra() -> None:
    r"""$K=A\otimes_R\operatorname{Frac}(R)$, and the basis is $A$'s.

    An integral basis is not a number-field notion.  $K$ is a
    $\operatorname{Frac}(R)$-algebra, an $R$-algebra underlying it is one with
    the same presentation over $R$, and an integral basis is an $R$-basis of
    that -- so the field answers by naming the algebra, and the relation
    between the two is the base change rather than a resemblance.

    Which $R$-form is a choice: the presentation names $R[\alpha]$, and the
    maximal one is a different object.
    """
    _ensure_preamble()

    A = FreeAlgebraOn(QQ, finite_ordered_set(["x"]))
    x = A.algebra_generators()[0]
    K = own_number_field(x * x - 5 * A.one())

    order = K.underlying_algebra(ZZ)
    assert order.base_ring() is ZZ, "the underlying algebra is over R"
    assert order.relations() == (
        (x * x - 5 * A.one()).change_ring(ZZ),
    ), "presented by the same f, over R"

    base_change = K.base_change_functor(ZZ)
    assert order in base_change.domain() and K in base_change.codomain(), (
        "the functor goes from R-algebras to Frac(R)-algebras, and the two "
        "objects sit at its ends"
    )
    assert base_change(order).relations() == K.relations(), (
        "F(A) = K for F = - (x)_R Frac(R): the field is a value of the "
        "functor, not merely similar to a base change of the algebra"
    )

    basis = K.integral_basis(ZZ)
    assert len(basis) == K.degree(), (
        "reduction leaves the powers below deg f, and there are [K : QQ] of them"
    )
    assert basis[0] == K(A.one()) and basis[1] == K.primitive_element(), (
        "the R-basis of R[alpha] is the power basis"
    )
    assert all(element.is_integral() for element in basis), (
        "every member of an R-basis of an R-algebra is integral over R"
    )


def test_an_element_of_a_number_field_is_a_QQ_linear_endomorphism() -> None:
    r"""$N$, $\operatorname{Tr}$, the minimal polynomial and the inverse.

    Multiplication by $a$ is $\QQ$-linear on $K$, so $a$ *is* that
    endomorphism: its norm is the determinant and its trace the trace, which
    is why neither depends on the presentation.  The inverse comes from a
    Bezout identity with $f$, irreducibility being exactly what makes the gcd
    a unit.
    """
    _ensure_preamble()
    from sage.rings.qqbar import AA as AlgebraicReals

    A = FreeAlgebraOn(QQ, finite_ordered_set(["x"]))
    x = A.algebra_generators()[0]
    K = own_number_field(x * x - 5 * A.one())
    one = K(A.one())
    root_of_five = K.primitive_element()

    assert root_of_five.norm() == -5 and root_of_five.trace() == 0, (
        "N(sqrt 5) = -5 and Tr(sqrt 5) = 0, being det and tr of its matrix"
    )
    assert (one + root_of_five).norm() == -4, "N(1 + sqrt 5) = 1 - 5"
    assert (one + root_of_five).trace() == 2, "Tr(1 + sqrt 5) = 2"

    assert root_of_five.minimal_polynomial() == x * x - 5 * A.one(), (
        "sqrt 5 generates K, so its minimal polynomial is f"
    )
    assert one.minimal_polynomial() == x - A.one(), (
        "1 does not generate K, so its minimal polynomial has degree one"
    )
    assert one.characteristic_polynomial() == (x - A.one()) * (x - A.one()), (
        "the characteristic polynomial has degree [K : QQ] whatever the element"
    )

    assert root_of_five.is_integral(), "sqrt 5 is an algebraic integer"
    assert not (K((QQ(1) / 2) * A.one()) * root_of_five).is_integral(), (
        "sqrt(5)/2 is not: its minimal polynomial is x^2 - 5/4"
    )

    inverse = root_of_five.inverse()
    assert root_of_five * inverse == one, (
        "the Bezout cofactor is the inverse, which is what irreducibility buys"
    )

    conjugates = root_of_five.conjugates(AlgebraicReals)
    assert len(conjugates) == 2 and [c**2 for c in conjugates] == [5, 5], (
        "the conjugates of sqrt 5 are its two real embeddings"
    )
    assert sum(conjugates) == root_of_five.trace(), (
        "the trace is the sum over the embeddings, for a separable extension"
    )


def test_a_polynomial_factors_over_an_extension_it_gains_a_root_in() -> None:
    r"""$x^2-5=(x-\sqrt5)(x+\sqrt5)$ over $\QQ(\sqrt5)$, irreducible over $\QQ$.

    Base change is the free construction applied to $\QQ\hookrightarrow K$, so
    the algebra over $K$ is the same generating set with new coefficients --
    and factorisation there crosses to an engine that computes over $K$, with
    the coefficients translated both ways.
    """
    _ensure_preamble()

    A = FreeAlgebraOn(QQ, finite_ordered_set(["x"]))
    x = A.algebra_generators()[0]
    K = own_number_field(x * x - 5 * A.one())
    root_of_five = K.primitive_element()

    assert (x * x - 5 * A.one()).is_irreducible(), (
        "x^2 - 5 has no rational root"
    )

    over_the_extension = (x * x - 5 * A.one()).change_ring(K)
    factors = over_the_extension.irreducible_factors()
    assert len(factors) == 2 and all(
        multiplicity == 1 for _, multiplicity in factors
    ), "over K it splits into two distinct linear factors"

    product = over_the_extension.parent().one()
    for factor, multiplicity in factors:
        assert factor.degree() == 1, "each factor is linear"
        product = product * factor**multiplicity
    assert product == over_the_extension, (
        "the factors multiply back to the polynomial, over K"
    )

    generator_over_K = over_the_extension.parent().algebra_generators()[0]
    assert set(factors) == {
        (generator_over_K - root_of_five * over_the_extension.parent().one(), 1),
        (generator_over_K + root_of_five * over_the_extension.parent().one(), 1),
    }, "the factors are x - sqrt 5 and x + sqrt 5"
