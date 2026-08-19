from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.all import IntegralLattice, ZZ, matrix
from .conftest import assert_runtime_methods_covered


def _disc_module():
    L = IntegralLattice(matrix(ZZ, [[2]]))
    return L.discriminant_group()


def test_tqm_cardinality_matches_rank_one_discriminant():
    """
    method: cardinality

    cardinality() is the order of the finite discriminant module.
    Assertion: Rank-1 lattice with Gram [2] yields discriminant-module order 2.
    """
    T = _disc_module()
    actual = T.cardinality()
    expected = 2
    assert actual == expected, (
        f"TorsionQuadraticModule.cardinality mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_invariants_rank_one_even_lattice():
    """
    method: invariants

    invariants() returns finite abelian invariants of the module.
    Assertion: Rank-1 Gram [2] gives cyclic invariant tuple (2,).
    """
    T = _disc_module()
    actual = T.invariants()
    expected = (2,)
    assert actual == expected, (
        f"TorsionQuadraticModule.invariants mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_twist_multiplies_quadratic_values():
    """
    method: twist

    twist(c) rescales bilinear and quadratic forms by c on the same underlying group.
    Assertion: Generator quadratic value doubles after twist(2).
    """
    T = _disc_module()
    x = T.gens()[0]
    q0 = x.q()
    T2 = T.twist(2)
    x2 = T2.gens()[0]
    actual = x2.q()
    expected = 2 * q0
    assert actual == expected, (
        f"TorsionQuadraticModule.twist quadratic value mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_gens_nonempty_for_nontrivial_discriminant_group():
    """
    method: gens

    gens() returns a generating set for the finite module.
    Assertion: Rank-1 discriminant group has at least one generator.
    """
    T = _disc_module()
    actual = len(T.gens()) > 0
    expected = True
    assert actual == expected, f"TorsionQuadraticModule.gens mismatch: actual={actual}, expected={expected}"


def test_tqm_gram_matrix_bilinear_is_square():
    """
    method: gram_matrix_bilinear

    gram_matrix_bilinear() returns the bilinear pairing matrix on generators.
    Assertion: Returned matrix is square of size number_of_generators.
    """
    T = _disc_module()
    G = T.gram_matrix_bilinear()
    n = len(T.gens())
    actual = (G.nrows(), G.ncols())
    expected = (n, n)
    assert actual == expected, (
        f"TorsionQuadraticModule.gram_matrix_bilinear shape mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_gram_matrix_quadratic_has_same_shape_as_bilinear():
    """
    method: gram_matrix_quadratic

    gram_matrix_quadratic() returns quadratic-form matrix in the same generator basis.
    Assertion: Quadratic and bilinear Gram matrices have the same shape.
    """
    T = _disc_module()
    A = T.gram_matrix_bilinear()
    Q = T.gram_matrix_quadratic()
    actual = (Q.nrows(), Q.ncols())
    expected = (A.nrows(), A.ncols())
    assert actual == expected, (
        f"TorsionQuadraticModule.gram_matrix_quadratic shape mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_value_modules_are_defined():
    """
    method: value_module

    value_module() and value_module_qf() expose codomains for bilinear/quadratic values.
    Assertion: Generator bilinear/quadratic values lie in these codomains.
    """
    T = _disc_module()
    x = T.gens()[0]
    bil = T.value_module()
    qf = T.value_module_qf()
    actual = (x * x in bil, x.q() in qf)
    expected = (True, True)
    assert actual == expected, (
        f"TorsionQuadraticModule value modules mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_primary_part_of_two_group_is_itself():
    """
    method: primary_part

    primary_part(s) extracts the s-primary component.
    Assertion: For a 2-group discriminant module, 2-primary part has same cardinality.
    """
    T = _disc_module()
    P = T.primary_part(2)
    actual = P.cardinality()
    expected = T.cardinality()
    assert actual == expected, (
        f"TorsionQuadraticModule.primary_part mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_element_class_is_defined():
    """
    method: element_class

    element_class gives the runtime class of module elements.
    Assertion: Type of a generator equals element_class.
    """
    T = _disc_module()
    actual = type(T.gens()[0])
    expected = T.element_class
    assert actual == expected, (
        f"TorsionQuadraticModule.element_class mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_Element_constructor_symbol_present():
    """
    method: Element

    Element is the named constructor class on the parent.
    Assertion: Constructing from a lift reproduces generator quadratic data.
    """
    T = _disc_module()
    x = T.gens()[0]
    y = T.Element(T, x.lift())
    actual = (y == x, y.q())
    expected = (True, x.q())
    assert actual == expected, f"TorsionQuadraticModule.Element mismatch: actual={actual}, expected={expected}"


def test_tqm_all_submodules_nonempty():
    """
    method: all_submodules

    all_submodules() enumerates finite submodules.
    Assertion: Trivial and full submodules occur with cardinalities 1 and |T|.
    """
    T = _disc_module()
    S = T.all_submodules()
    cards = {U.cardinality() for U in S}
    actual = (1 in cards, T.cardinality() in cards)
    expected = (True, True)
    assert actual == expected, f"TorsionQuadraticModule.all_submodules mismatch: actual={actual}, expected={expected}"


def test_tqm_normal_form_returns_module():
    """
    method: normal_form

    normal_form() returns canonical discriminant-form normal form.
    Assertion: Result has same cardinality as source module.
    """
    T = _disc_module()
    N = T.normal_form()
    actual = N.cardinality()
    expected = T.cardinality()
    assert actual == expected, f"TorsionQuadraticModule.normal_form mismatch: actual={actual}, expected={expected}"


def test_tqm_orthogonal_group_has_generators():
    """
    method: orthogonal_group

    orthogonal_group() returns automorphism group preserving bilinear/quadratic form.
    Assertion: Group order is at least 1 (identity is always present).
    """
    T = _disc_module()
    G = T.orthogonal_group()
    actual = G.order() >= 1
    expected = True
    assert actual == expected, (
        f"TorsionQuadraticModule.orthogonal_group mismatch: actual={actual}, expected={expected}, order={G.order()}, gens={G.gens()}"
    )


def test_tqm_orthogonal_submodule_to_self_is_nonempty():
    """
    method: orthogonal_submodule_to

    orthogonal_submodule_to(S) computes orthogonal complement of submodule S.
    Assertion: Orthogonal complement of the full submodule is trivial (cardinality 1).
    """
    T = _disc_module()
    S = T.submodule_with_gens(T.gens())
    O = T.orthogonal_submodule_to(S)
    actual = O.cardinality()
    expected = 1
    assert actual == expected, (
        f"TorsionQuadraticModule.orthogonal_submodule_to mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_submodule_with_gens_cardinality_bound():
    """
    method: submodule_with_gens

    submodule_with_gens(gens) constructs submodule from explicit generators.
    Assertion: Submodule cardinality is <= ambient cardinality.
    """
    T = _disc_module()
    S = T.submodule_with_gens(T.gens()[:1])
    actual = S.cardinality() <= T.cardinality()
    expected = True
    assert actual == expected, (
        f"TorsionQuadraticModule.submodule_with_gens mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_value_module_qf_defined():
    """
    method: value_module_qf

    value_module_qf() returns codomain for quadratic values.
    Assertion: Generator quadratic value is an element of this codomain.
    """
    T = _disc_module()
    x = T.gens()[0]
    actual = x.q() in T.value_module_qf()
    expected = True
    assert actual == expected, f"TorsionQuadraticModule.value_module_qf mismatch: actual={actual}, expected={expected}"


def test_tqm_order_equals_cardinality_for_finite_module():
    """
    method: order

    order() is the finite module cardinality.
    Assertion: order equals cardinality on the discriminant module example.
    """
    T = _disc_module()
    actual = T.order()
    expected = T.cardinality()
    assert actual == expected, (
        f"TorsionQuadraticModule.order mismatch: actual={actual}, expected={expected}"
    )


def test_tqm_brown_invariant_is_defined_mod_8():
    """
    method: brown_invariant

    brown_invariant() returns the Brown invariant in Z/8Z.
    Assertion: Value lifts to an integer between 0 and 7.
    """
    T = _disc_module()
    b = T.brown_invariant()
    actual = int(b)
    expected = actual in range(8)
    assert expected, f"TorsionQuadraticModule.brown_invariant mismatch: actual={actual}, expected=in [0,7]"


def test_tqm_genus_matches_discriminant_cardinality_for_valid_signature():
    """
    method: genus

    genus(signature_pair) builds a global genus with this discriminant form.
    Assertion: For signature (1,0), determinant matches discriminant cardinality.
    """
    T = _disc_module()
    g = T.genus((1, 0))
    actual = g.determinant()
    expected = T.cardinality()
    assert actual == expected, f"TorsionQuadraticModule.genus mismatch: actual={actual}, expected={expected}"


def test_tqm_is_genus_true_exactly_for_valid_signature_example():
    """
    method: is_genus

    is_genus(signature_pair) checks global existence for this discriminant/signature.
    Assertion: (1,0) is valid while (0,1) is invalid in rank-1 [2] example.
    """
    T = _disc_module()
    actual = (T.is_genus((1, 0)), T.is_genus((0, 1)))
    expected = (True, False)
    assert actual == expected, f"TorsionQuadraticModule.is_genus mismatch: actual={actual}, expected={expected}"


def test_torsionquadraticmodule_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant TorsionQuadraticModule runtime
    method should correspond to at least one explicit test method tag.
    """
    sample = _disc_module()
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.modules.torsion_quadratic_module",),
    )
