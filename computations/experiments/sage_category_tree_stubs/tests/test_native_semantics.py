"""Stub↔native semantic parity under Stub⊇Sage + compositional paths."""

from sage_category_tree_stubs.graph_compare import compare_stub_vs_native_axiom
from sage_category_tree_stubs.native_map import (
    mapped_native_instances,
    sage_owned_vertices,
    undocumented_unmapped_vertices,
)
from sage_category_tree_stubs.native_semantics import (
    is_subcategory_mismatches,
    named_join_axiom_gaps,
    native_solid_edges_missing_stub_path,
)


def test_every_sage_owned_dot_vertex_is_native_mapped() -> None:
    undocumented = undocumented_unmapped_vertices()
    assert not undocumented, (
        "sage-owned DOT vertices with no native map (not in research-only catalog): "
        f"{undocumented}"
    )
    mapped = mapped_native_instances()
    owned = sage_owned_vertices()
    assert set(mapped.keys()) == set(owned), (
        f"mapped {len(mapped)} != sage-owned {len(owned)}: "
        f"missing={set(owned) - set(mapped.keys())}, "
        f"extra={set(mapped.keys()) - set(owned)}"
    )


def test_native_solid_is_compositional_subgraph_of_stub() -> None:
    """Every Sage solid edge (modulo known remaps) has a path in the stub digraph."""
    missing = native_solid_edges_missing_stub_path()
    assert not missing, (
        "native solid edges with no stub path "
        f"(after VectorSpaces/axiom remaps): {missing}"
    )


def test_native_axioms_are_subset_of_stub_axioms() -> None:
    """Stub may add axioms; Sage must not introduce host axioms absent from stub."""
    result = compare_stub_vs_native_axiom()
    assert result["only_in_native"] == set(), (
        f"native-only axiom attachments vs stub: {result['only_in_native']}"
    )


def test_native_is_subcategory_implies_stub() -> None:
    """If Sage says child ≤ parent on a mapped solid edge, the stub must agree."""
    failures = is_subcategory_mismatches()
    assert not failures, (
        "native is_subcategory without stub agreement "
        "(child, parent, stub_ok, native_ok):\n"
        + "\n".join(f"  {row}" for row in failures)
    )


def test_named_join_axioms_are_subset_of_native() -> None:
    gaps = named_join_axiom_gaps()
    assert not gaps, (
        "named joins whose stub axioms are not contained in native axioms:\n"
        + "\n".join(
            f"  {name}: stub={stub} native={native}"
            for name, stub, native in gaps
        )
    )
