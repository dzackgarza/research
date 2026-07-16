r"""G-sets and the owned torsor refinement (issue #213, CP3).

The owned ``GSets(G)`` root integrates Sage's standard node and forwards
all generic set behavior through the underlying-set route, exactly like
the operation roots. ``Torsors(G)`` is the project-owned refinement by
the standard free transitive action: a nonempty torsor is identified
with ``G`` only through a CHOSEN element, and that identification is
executable — enumeration acts the group through the chosen element
(free + transitive makes it exhaustive and duplicate-free), cardinality
is exactly the group's, and the transporter ``(x, y) -> g`` with
``g . x == y`` exists uniquely. The concrete consumer is the finite
isometry homset: ``Isom(A2, M)`` for a conjugated copy ``M`` is a torsor
under ``O(A2)`` by precomposition.
"""

from __future__ import annotations

from sage.all import ZZ, matrix
from sage.categories.g_sets import GSets as SageGSets
from sage.structure.parent import Parent

from sage_lattice_category_spike.lattice_categories import Lattice
from sage_lattice_category_spike.objects.cardinals import Cardinal
from sage_lattice_category_spike.objects.g_sets import GSets, Torsors


def _conjugated_a2():
    a2 = Lattice("A2")
    change = matrix(ZZ, [[1, 1], [0, 1]])
    return a2, Lattice(change.transpose() * a2.gram_matrix() * change, label="A2-conjugate")


def test_torsors_refine_g_sets():
    group = Lattice("A2").isometry_group()
    assert Torsors(group).is_subcategory(GSets(group))
    assert Torsors(group).is_subcategory(SageGSets(group))
    assert Torsors(group).acting_group() is group


class IsometriesAsTorsor(Parent):
    r"""``Isom(A2, M)`` as a torsor under ``O(A2)`` by precomposition:
    supplies only the action and one chosen isometry — enumeration,
    cardinality, and transporters must arrive through the torsor
    contract."""

    def __init__(self, source, target):
        self._source = source
        self._target = target
        Parent.__init__(self, category=Torsors(source.isometry_group()).Finite())

    def an_element(self):
        return self._source.Isom(self._target).an_element()

    def act(self, group_element, element):
        return element * group_element


def test_a_finite_isometry_homset_enumerates_through_its_torsor_structure():
    a2, conjugate = _conjugated_a2()
    torsor = IsometriesAsTorsor(a2, conjugate)

    cardinality = torsor.cardinality()
    assert cardinality == 12
    assert isinstance(cardinality, Cardinal)
    assert cardinality == a2.isometry_group().order()

    isometries = list(torsor)
    assert len(isometries) == 12
    assert len(set(isometries)) == 12
    assert all(isometry.domain() == a2 and isometry.codomain() == conjugate for isometry in isometries)
    homset = a2.Isom(conjugate)
    assert all(isometry in homset for isometry in isometries)


def test_the_transporter_is_the_unique_group_element_between_two_points():
    a2, conjugate = _conjugated_a2()
    torsor = IsometriesAsTorsor(a2, conjugate)
    isometries = list(torsor)
    first, second = isometries[0], isometries[5]

    mover = torsor.transporter(first, second)
    assert mover in [g for g in a2.isometry_group()]
    assert torsor.act(mover, first) == second

    movers = [g for g in a2.isometry_group() if torsor.act(g, first) == second]
    assert len(movers) == 1
    assert torsor.transporter(first, first) == a2.identity_morphism()
