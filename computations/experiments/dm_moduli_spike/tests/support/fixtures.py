"""Named structural fixtures for small moduli-space regression tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dm_moduli_spike.objects.graph_types import StableGraphType
    from dm_moduli_spike.objects.strata import DMStratum
    from dm_moduli_spike.objects.stratification import DMStratification


def m11_types(stratification: DMStratification) -> tuple[DMStratum, DMStratum]:
    """Smooth and nodal strata of Mbar(1, 1)."""
    poset = stratification.specialization_poset()
    smooth = next(x for x in poset if x.curve_type().num_edges() == 0)
    nodal = next(x for x in poset if x.curve_type().num_edges() == 1)
    return smooth, nodal


def m12_types(stratification: DMStratification) -> dict[str, DMStratum]:
    """Markwig's five genus-one two-marked combinatorial types."""
    return {
        "A": stratification.find_unique_type(
            vertex_genera=(1,),
            marking_blocks=((1, 2),),
        ),
        "B": stratification.find_unique_type(
            vertex_genera=(0,),
            loops=(1,),
            marking_blocks=((1, 2),),
        ),
        "C": stratification.find_unique_type(
            vertex_genera=(0, 1),
            edge_multiset=((0, 1, 1),),
            marking_blocks=((1, 2), ()),
        ),
        "D": stratification.find_unique_type(
            vertex_genera=(0, 0),
            loops=(1, 0),
            edge_multiset=((0, 1, 1),),
            marking_blocks=((), (1, 2)),
        ),
        "E": stratification.find_unique_type(
            vertex_genera=(0, 0),
            edge_multiset=((0, 1, 2),),
            marking_blocks=((1,), (2,)),
        ),
    }


def m20_types(stratification: DMStratification) -> dict[str, DMStratum]:
    """Chan's seven stable genus-two combinatorial types."""
    from dm_moduli_spike import DMCompactificationModel

    types = DMCompactificationModel(stratification.genus(), stratification.number_of_markings()).curve_types()
    fixtures = {
        "VII": types.from_vertices(genera=(2,), markings=((),), edges=()),
        "V": types.from_vertices(genera=(1,), markings=((),), edges=((0, 0),)),
        "VI": types.from_vertices(genera=(1, 1), markings=((), ()), edges=((0, 1),)),
        "III": types.from_vertices(genera=(0,), markings=((),), edges=((0, 0), (0, 0))),
        "IV": types.from_vertices(genera=(1, 0), markings=((), ()), edges=((0, 1), (1, 1))),
        "I": types.from_vertices(genera=(0, 0), markings=((), ()), edges=((0, 1), (0, 1), (0, 1))),
        "II": types.from_vertices(genera=(0, 0), markings=((), ()), edges=((0, 0), (0, 1), (1, 1))),
    }
    by_key = {stratum.curve_type().canonical_key(): stratum for stratum in stratification.strata()}
    return {name: by_key[curve_type.canonical_key()] for name, curve_type in fixtures.items()}


def genus_six_counterexample() -> StableGraphType:
    """Stable genus-six graph with distinct Aut edge orbits sharing a contraction target."""
    from dm_moduli_spike import StableGraphTypes

    types = StableGraphTypes(6, 0)
    return types.from_vertices(
        genera=(1, 0, 1, 0, 1, 0),
        markings=((), (), (), (), (), ()),
        edges=((0, 1), (0, 4), (1, 2), (1, 5), (2, 3), (3, 4), (3, 5), (4, 5)),
    )
