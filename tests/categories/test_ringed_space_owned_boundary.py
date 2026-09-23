from dzack_research.preamble.all import QQ, ZZ, ProjectiveSpaces, Schemes
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    LocallyRingedSpaces,
    RingedSpaces,
)
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces


def test_ringed_space_hierarchy_is_owned_and_inhabited_by_actual_schemes() -> None:
    ringed = RingedSpaces()
    locally_ringed = LocallyRingedSpaces()
    affine = (ZZ).affine_spectrum()

    assert isinstance(ringed, OwnedCategory)
    assert isinstance(locally_ringed, OwnedCategory)
    assert ringed.an_object() in ringed
    assert locally_ringed.an_object() in locally_ringed
    assert affine in locally_ringed
    assert affine in ringed
    assert locally_ringed in Schemes(ZZ).all_super_categories()
    assert ringed in locally_ringed.all_super_categories()


def test_ringed_space_parent_methods_survive_the_owned_category_boundary() -> None:
    affine = (ZZ).affine_spectrum()
    sheaf = affine.structure_sheaf()
    space = affine.underlying_space()

    assert sheaf.ringed_space() is affine
    assert sheaf.global_sections() is ZZ
    assert space.ringed_space() is affine
    assert space in TopologicalSpaces()


def test_nonaffine_scheme_underlying_space_is_an_owned_topological_space() -> None:
    line = ProjectiveSpaces(QQ)(1)
    space = line.underlying_space()

    assert space in TopologicalSpaces()
    assert space.scheme() is line
