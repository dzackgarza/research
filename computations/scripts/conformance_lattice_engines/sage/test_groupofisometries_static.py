from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.all import IntegralLattice
from .conftest import assert_runtime_methods_covered


def test_groupofisometries_invariant_bilinear_form_matches_lattice():
    """
    method: invariant_bilinear_form

    invariant_bilinear_form() returns the preserved symmetric form matrix B.
    Assertion: Group form equals source lattice inner-product matrix.
    """
    L = IntegralLattice("A2")
    G = L.orthogonal_group()
    actual = G.invariant_bilinear_form()
    expected = L.inner_product_matrix()
    assert actual == expected, (
        f"GroupOfIsometries.invariant_bilinear_form mismatch: actual={actual}, expected={expected}"
    )


def test_groupofisometries_generators_are_isometries():
    """
    method: gens

    gens() returns generator matrices of the isometry group preserving B.
    Assertion: Every generator satisfies g*B*g^T = B.
    """
    L = IntegralLattice("A2")
    G = L.orthogonal_group()
    B = G.invariant_bilinear_form()
    for g in G.gens():
        M = g.matrix()
        actual = M * B * M.transpose()
        expected = B
        assert actual == expected, (
            f"GroupOfIsometries generator does not preserve form: actual={actual}, expected={expected}"
        )


def test_groupofisometries_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant GroupOfIsometries runtime method
    should correspond to at least one explicit test method tag in this module.
    """
    sample = IntegralLattice("A2").orthogonal_group()
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.groups.matrix_gps.isometries",),
    )
