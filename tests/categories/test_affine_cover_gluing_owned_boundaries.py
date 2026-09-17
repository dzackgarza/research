r"""Affine-cover descent categories are owned and parameterized by actual covers."""

import pytest

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.schemes.gluing import (
    AlgebraGluingData,
    ModuleGluingData,
)
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    DistinguishedAffineCovers,
)


def _two_chart_cover():
    algebra = QQ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    scheme = (algebra).affine_spectrum()
    return scheme, scheme.distinguished_open_cover(x, algebra.one() - x)


def test_distinguished_affine_cover_is_an_owned_parameter_object() -> None:
    scheme, cover = _two_chart_cover()

    assert cover in DistinguishedAffineCovers()
    assert scheme not in DistinguishedAffineCovers()
    assert cover in DistinguishedAffineCovers(scheme)
    assert cover.defining_elements().index_set() is cover.index_set()
    assert cover.atlas() is cover.index_set()
    for label in cover.atlas():
        assert cover.open(label) is cover.member(label).domain().arrow().domain()
    span = cover.overlap_span(0, 1)
    assert span.apex().arrow().domain() is cover.overlap(0, 1)

    modules = ModuleGluingData(cover)
    algebras = AlgebraGluingData(cover)
    assert isinstance(modules, OwnedParameterizedCategory)
    assert isinstance(algebras, OwnedParameterizedCategory)
    assert modules.cover() is cover
    assert algebras.cover() is cover
    assert modules.base() is cover
    assert algebras.base() is cover
    assert ModuleGluingData(cover) is modules
    assert AlgebraGluingData(cover) is algebras


def test_descent_categories_reject_noncover_parameters() -> None:
    scheme, _cover = _two_chart_cover()

    with pytest.raises(AssertionError):
        ModuleGluingData(scheme)
    with pytest.raises(AssertionError):
        AlgebraGluingData(scheme)
