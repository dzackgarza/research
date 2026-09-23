r"""Owned-category boundaries for profinite and absolute Galois groups.

These specimens exercise the mathematical category graph itself.  The
finite-field absolute Galois group supplies a genuine profinite object, and
its canonical degree-two finite stage supplies a genuine open subgroup.
"""

from dzack_research.preamble.all import GF
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    TopologicalGroups,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    AbsoluteGaloisGroup,
)
from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import (
    AbsoluteGaloisGroups,
    AbsoluteGaloisGroupsOfFiniteFields,
    OpenAbsoluteGaloisSubgroups,
)
from dzack_research.preamble.categories.group.profinite.profinite_groups import (
    ProfiniteGroups,
)




def test_each_profinite_category_exhibits_a_real_mathematical_object() -> None:
    profinite = ProfiniteGroups()
    absolute = AbsoluteGaloisGroups()
    finite_field_absolute = AbsoluteGaloisGroupsOfFiniteFields()
    ambient = AbsoluteGaloisGroup(GF(2))
    open_absolute = OpenAbsoluteGaloisSubgroups(ambient)

    profinite_group = profinite.an_object()
    absolute_group = absolute.an_object()
    finite_field_group = finite_field_absolute.an_object()
    open_subgroup = open_absolute.an_object()

    assert profinite_group in profinite
    assert profinite_group in TopologicalGroups()
    assert profinite_group in OwnedGroups()

    assert absolute_group in absolute
    assert finite_field_group in finite_field_absolute
    assert finite_field_group.frobenius() in finite_field_group
    assert tuple(finite_field_group.topological_group_generators()) == (
        finite_field_group.frobenius(),
    )

    assert open_subgroup in open_absolute
    assert open_subgroup.supergroup() in finite_field_absolute
    assert open_subgroup.index() == 2
    assert open_subgroup.inclusion().domain() is open_subgroup
    assert open_subgroup.inclusion().codomain() is open_subgroup.supergroup()
