r"""Tier-4 internal consistency: pickling and JSON round-trip preservation."""

from __future__ import annotations

import json

from dm_moduli_spike.objects.model import DMCompactificationModel
from dm_moduli_spike import StableGraphTypes


def test_json_schema_shape():
    types = StableGraphTypes(2, 1)
    gamma = types.from_vertices(genera=(1, 0), markings=((1,), ()), edges=((0, 1), (1, 1)))
    data = gamma.to_json()
    assert data["schema"] == 1
    assert data["ambient"] == {"g": 2, "n": 1}
    assert {v["id"] for v in data["vertices"]} == {0, 1}
    assert len(data["edges"]) == gamma.num_edges()


def test_parent_is_unique_representation():
    assert StableGraphTypes(2, 1) is StableGraphTypes(2, 1)
    assert DMCompactificationModel(2, 1) is DMCompactificationModel(2, 1)


def test_from_json_rejects_unsupported_schema():
    types = StableGraphTypes(2, 1)
    payload = {
        "schema": 99,
        "ambient": {"g": 2, "n": 1},
        "vertices": [{"id": 0, "genus": 2, "markings": [1]}],
        "edges": [],
    }
    try:
        types.from_json(payload)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for unsupported schema")


def test_from_json_rejects_duplicate_vertex_ids():
    types = StableGraphTypes(2, 1)
    payload = {
        "schema": 1,
        "ambient": {"g": 2, "n": 1},
        "vertices": [
            {"id": 0, "genus": 1, "markings": [1]},
            {"id": 0, "genus": 1, "markings": []},
        ],
        "edges": [],
    }
    try:
        types.from_json(payload)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for duplicate vertex ids")


def test_from_json_rejects_unknown_edge_endpoints():
    types = StableGraphTypes(2, 1)
    payload = {
        "schema": 1,
        "ambient": {"g": 2, "n": 1},
        "vertices": [{"id": 0, "genus": 2, "markings": [1]}],
        "edges": [{"id": 0, "ends": [0, 9]}],
    }
    try:
        types.from_json(payload)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for unknown edge endpoint")


def test_from_json_rejects_malformed_vertex_object():
    types = StableGraphTypes(2, 1)
    payload = {
        "schema": 1,
        "ambient": {"g": 2, "n": 1},
        "vertices": [{"id": 0, "genus": "bad", "markings": [1]}],
        "edges": [],
    }
    try:
        types.from_json(payload)
    except (AssertionError, TypeError, ValueError):
        pass
    else:
        raise AssertionError("expected failure for malformed vertex genus")


def test_from_json_rejects_missing_required_keys():
    types = StableGraphTypes(2, 1)
    for payload in (
        {"ambient": {"g": 2, "n": 1}, "vertices": [], "edges": []},
        {"schema": 1, "vertices": [], "edges": []},
        {"schema": 1, "ambient": {"g": 2, "n": 1}, "edges": []},
        {"schema": 1, "ambient": {"g": 2, "n": 1}, "vertices": []},
    ):
        try:
            types.from_json(payload)
        except (AssertionError, KeyError, TypeError):
            pass
        else:
            raise AssertionError(f"expected failure for payload {payload!r}")


def test_from_json_rejects_bad_marking_labels():
    types = StableGraphTypes(2, 1)
    payload = {
        "schema": 1,
        "ambient": {"g": 2, "n": 1},
        "vertices": [{"id": 0, "genus": 2, "markings": [2]}],
        "edges": [],
    }
    try:
        types.from_json(payload)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for noncontiguous marking labels")


def test_canonical_form_certificate_commutes_with_contraction():
    types = StableGraphTypes(0, 5)
    gamma = types.from_vertices(
        genera=(0, 0, 0),
        markings=((1, 2), (3,), (4, 5)),
        edges=((0, 1), (1, 2)),
    )
    graph = gamma.canonical_representative()
    _, first = graph.contract(graph.internal_edges()[0])
    intermediate = first.codomain()
    relabeled = types.from_vertices(
        genera=intermediate.vertex_genera,
        markings=tuple(tuple(reversed(intermediate.markings_at(vertex))) for vertex in range(intermediate.num_vertices())),
        edges=tuple(
            (intermediate.flag_vertex[flag], intermediate.flag_vertex[partner])
            for flag, partner in intermediate.internal_edges()
        ),
    ).canonical_representative()
    _, canonical, certificate = relabeled.canonical_form()
    edge = relabeled.internal_edges()[0]
    canonical_edge = (certificate[edge[0]], certificate[edge[1]])
    assert relabeled.contract(edge)[0] == canonical.contract(canonical_edge)[0]
