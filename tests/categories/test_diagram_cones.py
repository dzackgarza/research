import pytest

from dzack_research.preamble.all import (
    Cocone,
    Cone,
    DiscreteCategory,
    DiscreteDiagram,
    Sets,
)


def test_cones_and_cocones_are_natural_transformations_with_commuting_apex_maps() -> None:
    index = DiscreteCategory(Sets.Δ[1])
    x = Sets.Δ[1]
    y = Sets.Δ[2]
    diagram = DiscreteDiagram(
        index,
        Sets(),
        lambda position: x if position == 0 else y,
    )

    point = Sets.Δ[0]
    two_points = Sets.Δ[1]
    cone_point = Cone(
        diagram,
        point,
        lambda index_object: Sets().mor(point, diagram(index_object))(lambda _value: diagram(index_object)(0 if index_object.value() == 0 else 1)),
    )
    cone_two = Cone(
        diagram,
        two_points,
        lambda index_object: Sets().mor(two_points, diagram(index_object))(lambda _value: diagram(index_object)(0 if index_object.value() == 0 else 1)),
    )
    collapse = Sets().mor(two_points, point)(lambda _value: point(0))
    cone_map = cone_two.cone_category().mor(cone_two, cone_point)(collapse)
    assert cone_map.apex_map()(two_points(1)) == point(0)

    with pytest.raises(ValueError):
        noncommuting = Sets().mor(two_points, point)(lambda _value: point(0))
        bad_cone = Cone(
            diagram,
            two_points,
            lambda index_object: Sets().mor(two_points, diagram(index_object))(lambda value: diagram(index_object)(
                    value if index_object.value() == 0 else value + 1
                )),
        )
        bad_cone.cone_category().mor(bad_cone, cone_point)(noncommuting)

    cocone_point = Cocone(
        diagram,
        point,
        lambda index_object: Sets().mor(diagram(index_object), point)(lambda _value: point(0)),
    )
    cocone_two = Cocone(
        diagram,
        two_points,
        lambda index_object: Sets().mor(diagram(index_object), two_points)(lambda _value: two_points(0)),
    )
    include_point = Sets().mor(point, two_points)(lambda _value: two_points(0))
    cocone_map = cocone_point.cocone_category().mor(cocone_point, cocone_two)(include_point)
    assert cocone_map.apex_map()(point(0)) == two_points(0)
