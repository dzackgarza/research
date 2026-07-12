r"""Subobjects are (lattice, monomorphism) pairs, formed from spans of elements
/ kernels / images -- never raw coordinate lists (issue #100, #6). A lattice is
just ``(R, G)``; its relationship to an ambient lives in the inclusion morphism.
The test subject is A_2 realized as a genuine subobject of ``I_{0,3}`` via its
Bourbaki embedding (ambient rank 3 > self rank 2), the case that broke the old
stored-ambient substrate.
"""
from __future__ import annotations

import pytest

import sage_lattice_category_spike.lattice_categories as lc


def _a2_in_i03():
    A2 = lc.Lattice("A2")
    embedding = A2.bourbaki_embedding()
    ambient = embedding.codomain()
    return ambient.subobject([embedding(A2.gen(0)), embedding(A2.gen(1))], label="A2_in_I03")


def test_bourbaki_realization_is_a_genuine_primitive_subobject():
    subobject = _a2_in_i03()
    assert subobject.rank() == 2
    assert subobject.gram_matrix() == lc.Lattice("A2").gram_matrix()   # -Cartan, negative definite
    assert subobject.ambient().is_unimodular() and subobject.ambient().rank() == 3
    assert subobject.is_primitive()                                     # cokernel Z, torsion-free


def test_orthogonal_complement_and_saturation_compose_the_inclusion():
    subobject = _a2_in_i03()
    complement = subobject.orthogonal_complement()
    assert complement.ambient() is subobject.ambient()
    assert complement.rank() == 1                                       # I_{0,3} = A2 (perp) <line>
    saturation = subobject.saturation()
    assert saturation.rank() == subobject.rank() and saturation.is_primitive()


def test_subobject_generators_must_be_elements_not_raw_lists():
    A2 = lc.Lattice("A2")
    with pytest.raises(AssertionError):
        A2.subobject([[1, 0]])                                          # raw list rejected (#6)
    assert A2.subobject([A2.gen(0)]).rank() == 1                        # element accepted
