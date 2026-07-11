r"""Pickling and JSON round trips preserve parent and equality."""

from __future__ import annotations

import json
import pickle

from dm_moduli_spike import DMCompactificationModel, StableCurveTypes


def test_pickle_round_trip_preserves_parent_and_equality():
    model = DMCompactificationModel(2, 1)
    for level in model.stratification().curve_type_levels():
        for gamma in level:
            revived = pickle.loads(pickle.dumps(gamma))
            assert revived == gamma
            assert revived.parent() == gamma.parent()
            assert revived.canonical_key() == gamma.canonical_key()


def test_json_round_trip_preserves_equality():
    types = StableCurveTypes(2, 1)
    model = DMCompactificationModel(2, 1)
    for level in model.stratification().curve_type_levels():
        for gamma in level:
            blob = json.dumps(gamma.to_json())
            revived = types.from_json(json.loads(blob))
            assert revived == gamma
            assert revived.canonical_key() == gamma.canonical_key()


def test_json_schema_shape():
    types = StableCurveTypes(2, 1)
    gamma = types.from_vertices(genera=(1, 0), markings=((1,), ()), edges=((0, 1), (1, 1)))
    data = gamma.to_json()
    assert data["schema"] == 1
    assert data["ambient"] == {"g": 2, "n": 1}
    assert {v["id"] for v in data["vertices"]} == {0, 1}
    assert len(data["edges"]) == gamma.num_edges()


def test_parent_is_unique_representation():
    assert StableCurveTypes(2, 1) is StableCurveTypes(2, 1)
    assert DMCompactificationModel(2, 1) is DMCompactificationModel(2, 1)
