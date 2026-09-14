r"""AT21 toric ADE admission and branch sections use the live divisor/polytope owners."""

import pytest

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.schemes.ade_surfaces import AT21ADEPair


def _vertices(polytope):
    return {
        tuple(int(coordinate) for coordinate in vertex)
        for vertex in polytope.vertices()
    }


def test_source_admission_keeps_parity_and_affine_ranges_distinct() -> None:
    assert AT21ADEPair("A", 3, QQ).source_variant() == "pure"
    assert AT21ADEPair("A", 2, QQ, variant="short").source_variant() == "short"
    assert AT21ADEPair("D", 5, QQ, variant="short").dynkin_rank() == 5
    assert AT21ADEPair("D", 6, QQ, affine=True).is_affine_type()
    assert AT21ADEPair("E", 7, QQ, affine=True).is_affine_type()

    with pytest.raises(ValueError, match="tilde A is nontoric"):
        AT21ADEPair("A", 3, QQ, affine=True)
    with pytest.raises(ValueError, match="tilde D_even, tilde E7 and tilde E8"):
        AT21ADEPair("E", 6, QQ, affine=True)
    with pytest.raises(ValueError, match="even one-short A"):
        AT21ADEPair("A", 2, QQ)


def test_branch_divisor_is_twice_the_complement_and_full_section_has_newton_polygon_q() -> None:
    pair = AT21ADEPair("D", 4, QQ)

    assert pair.branch_divisor_class() == 2 * pair.complementary_divisor()
    section = pair.full_newton_branch_section()
    assert _vertices(pair.branch_newton_polygon(section)) == _vertices(pair.polygon())
    branch = pair.branch_subscheme(section)
    assert branch.inclusion().codomain() is pair.scheme()


def test_table_five_e8_specialization_retains_the_source_exponent_support() -> None:
    pair = AT21ADEPair("E", 8, QQ)
    generic = pair.source_normal_form_section(constant=1)
    singular = pair.source_normal_form_section(constant=0)

    assert _vertices(pair.branch_newton_polygon(generic)) == _vertices(pair.polygon())
    singular_vertices = _vertices(pair.branch_newton_polygon(singular))
    assert singular_vertices == {(2, 2), (0, 3), (5, 0)}
