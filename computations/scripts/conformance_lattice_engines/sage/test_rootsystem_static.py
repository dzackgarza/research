from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.all import CartanType, RootSystem
from .conftest import assert_runtime_methods_covered


def test_rootsystem_simple_root_scalar_recovers_cartan_entry():
    """
    method: scalar

    scalar(alpha, alphacheck) gives Cartan pairing <alpha, alpha^vee>.
    Assertion: For A2, an off-diagonal Cartan entry is -1.
    """
    L = RootSystem(["A", 2]).root_lattice()
    a = L.simple_roots()
    ac = L.simple_coroots()
    actual = a[1].scalar(ac[2])
    expected = -1
    assert actual == expected, (
        f"RootSystem.scalar Cartan entry mismatch: actual={actual}, expected={expected}"
    )


def test_rootsystem_positive_roots_count_matches_type_a2():
    """
    method: positive_roots

    positive_roots() returns all positive roots in the chosen realization.
    Assertion: Type A2 has exactly three positive roots.
    """
    L = RootSystem(["A", 2]).root_lattice()
    actual = len(list(L.positive_roots()))
    expected = 3
    assert actual == expected, (
        f"RootSystem.positive_roots count mismatch: actual={actual}, expected={expected}"
    )


def test_rootsystem_highest_root_is_positive():
    """
    method: highest_root

    highest_root() returns the maximal positive root in the root poset.
    Assertion: Returned root is contained in positive_roots().
    """
    L = RootSystem(["A", 2]).root_lattice()
    highest = L.highest_root()
    actual = highest in L.positive_roots()
    expected = True
    assert actual == expected, (
        f"RootSystem.highest_root membership mismatch: actual={actual}, expected={expected}, highest={highest}"
    )


def test_rootsystem_cartan_type_rank_matches_lattice_dimension():
    """
    method: root_lattice

    root_lattice() builds the free Z-module realization attached to the Cartan type.
    Assertion: Lattice dimension equals Cartan rank.
    """
    ct = CartanType(["A", 3])
    L = RootSystem(["A", 3]).root_lattice()
    actual = L.dimension()
    expected = ct.rank()
    assert actual == expected, (
        f"RootSystem.root_lattice dimension mismatch: actual={actual}, expected={expected}"
    )


def test_rootsystem_element_class_matches_element_parent():
    """
    method: element_class

    element_class is the runtime class used for root-lattice elements.
    Assertion: Basis element type equals element_class.
    """
    L = RootSystem(["A", 2]).root_lattice()
    e = L.an_element()
    actual = type(e)
    expected = L.element_class
    assert actual == expected, (
        f"RootSystem.element_class mismatch: actual={actual}, expected={expected}"
    )


def test_rootsystem_Element_constructor_builds_parent_element():
    """
    method: Element

    Element is the parent-level element constructor class attribute.
    Assertion: Element(parent, coords) has the same parent.
    """
    L = RootSystem(["A", 2]).root_lattice()
    coeffs = {1: 1}
    e = L.Element(L, coeffs)
    actual = e.parent()
    expected = L
    assert actual == expected, f"RootSystem.Element mismatch: actual={actual}, expected={expected}"


def test_rootsystem_to_ambient_space_morphism_preserves_parent():
    """
    method: to_ambient_space_morphism

    to_ambient_space_morphism() maps root-lattice vectors to ambient-space vectors.
    Assertion: Image parent is ambient space.
    """
    L = RootSystem(["A", 2]).root_lattice()
    R = RootSystem(["A", 2])
    f = L.to_ambient_space_morphism()
    x = L.simple_roots()[1]
    y = f(x)
    actual = y.parent()
    expected = R.ambient_space()
    assert actual == expected, (
        f"RootSystem.to_ambient_space_morphism mismatch: actual={actual}, expected={expected}"
    )


def test_rootsystem_to_coroot_space_morphism_preserves_parent():
    """
    method: to_coroot_space_morphism

    to_coroot_space_morphism() sends roots to coroot-space vectors.
    Assertion: Image parent is coroot space.
    """
    L = RootSystem(["A", 2]).root_lattice()
    f = L.to_coroot_space_morphism()
    x = L.simple_roots()[1]
    y = f(x)
    actual = y.parent()
    expected = L.coroot_lattice()
    assert actual == expected, (
        f"RootSystem.to_coroot_space_morphism mismatch: actual={actual}, expected={expected}"
    )


def test_rootsystem_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant root-lattice runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = RootSystem(["A", 3]).root_lattice()
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.combinat.root_system.root_space",),
    )
