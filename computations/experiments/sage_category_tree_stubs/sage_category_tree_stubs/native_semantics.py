r"""Compare stub semantics against native ``sage.categories`` on the mapped fragment.

Frame (``stub-vs-sage-category-graph-comparison-frame``):

- \(\mathcal G_{\mathrm{Sage}}\subseteq\mathcal G\) with semantic bijection on objects
- compositional edge preservation (paths / composites), not immediate-edge equality
- known incorrect Sage parents live in ``exceptions.EMBED_EXCEPTIONS``, not silent remaps
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.rings.infinity import Infinity

from .exceptions import incorrect_parent_stub_edges, waived_native_stub_edges
from .factory import factory
from .graph_compare import (
    compare_axiom_graphs,
    compare_solid_graphs,
    native_axiom_digraph,
    native_solid_digraph,
    sage_axiom_digraph,
    sage_solid_digraph,
)
from .native_map import mapped_native_instances, sage_owned_vertices, undocumented_unmapped_vertices

if TYPE_CHECKING:
    from sage.graphs.digraph import DiGraph


def _has_directed_path(graph: DiGraph, src: str, tgt: str) -> bool:
    if src not in graph or tgt not in graph:
        return False
    if src == tgt:
        return True
    try:
        dist = graph.distance(src, tgt)
        return bool(dist < Infinity)
    except ValueError, TypeError:
        return False


def native_solid_edges_missing_stub_path() -> list[tuple[str, str]]:
    """Native immediate solid edges with no path in the stub digraph.

    Excludes ledger ``incorrect_parent`` rows and axiom→host solidifications.
    """
    stub = sage_solid_digraph()
    native = native_solid_digraph()
    shared = set(stub.vertices()) & set(native.vertices())
    waived = waived_native_stub_edges()
    missing: list[tuple[str, str]] = []
    for u, v, _ in native.edges(sort=True):
        if u not in shared or v not in shared:
            continue
        if (u, v) in waived:
            continue
        if not _has_directed_path(stub, u, v):
            missing.append((u, v))
    return missing


def is_subcategory_mismatches() -> list[tuple[str, str, bool, bool]]:
    """Solid edges where native ``is_subcategory`` holds but stub disagrees.

    Stub-only breadth (True, False) is expected under Stub⊇Sage and under
    parameterized base-ring mismatches; those are not failures.
    """
    fac = factory()
    mapped = mapped_native_instances()
    waived = incorrect_parent_stub_edges()
    failures: list[tuple[str, str, bool, bool]] = []
    for edge in fac.graph.solid_edges:
        if edge.src not in mapped or edge.tgt not in mapped:
            continue
        if (edge.src, edge.tgt) in waived:
            continue
        stub_child = fac.instance(edge.src)
        stub_parent = fac.instance(edge.tgt)
        native_child = mapped[edge.src]
        native_parent = mapped[edge.tgt]
        stub_ok = stub_child.is_subcategory(stub_parent)
        native_ok = native_child.is_subcategory(native_parent)
        if native_ok and not stub_ok:
            failures.append((edge.src, edge.tgt, stub_ok, native_ok))
    return failures


def named_join_axiom_gaps() -> list[tuple[str, frozenset[str], frozenset[str]]]:
    """Named joins where mapped stub axioms lack a Sage image in ``native.axioms()``.

    Stub-only vocabulary (Free, GCDDomain, Graded, …) is not a gap when Sage
    encodes the same object under a different axiom name or none — those belong
    in ``sage_to_stub.SAGE_AXIOM_TO_STUB`` / Domain↔NoZeroDivisors. Gaps are
    stub axioms that *do* have a Sage image which is missing on the instance.
    """
    from .sage_to_stub import SAGE_AXIOM_TO_STUB

    fac = factory()
    mapped = mapped_native_instances()
    stub_to_native: dict[str, set[str]] = {
        "Domain": {"NoZeroDivisors", "Domain"},
        "Associative": {"Associative", "AdditiveAssociative"},
        "Unital": {"Unital", "AdditiveUnital"},
        "Inverse": {"Inverse", "AdditiveInverse"},
        "Commutative": {"Commutative", "AdditiveCommutative"},
        "Free": {"WithBasis", "Free"},
    }
    for sage_ax, stub_ax in SAGE_AXIOM_TO_STUB.items():
        stub_to_native.setdefault(stub_ax, set()).add(sage_ax)

    skip = {
        "Additive",
        "Multiplicative",
        "IntegralDomain",
        "GCDDomain",
        "UFD",
        "PID",
        "Euclidean",
        "Noetherian",
        "Finite",
        "Graded",
        "Differential",
        "Integral",
        "FiniteType",
        "RelativeDimension",
        "RelativeDimension_1",
        "RelativeDimension_2",
        "Separated",
    }

    gaps: list[tuple[str, frozenset[str], frozenset[str]]] = []
    for join_name in fac.graph.named_joins:
        if join_name not in mapped:
            continue
        stub_axioms = frozenset(fac.instance(join_name).axioms())
        native_axioms = frozenset(mapped[join_name].axioms())
        missing = set()
        for ax in stub_axioms:
            if ax in skip:
                continue
            accepted = stub_to_native.get(ax)
            if accepted is None:
                continue
            if not (accepted & set(native_axioms)):
                missing.add(ax)
        if missing:
            gaps.append((join_name, frozenset(missing), native_axioms))
    return gaps


def native_semantics_report() -> dict[str, object]:
    """Full stub↔native diagnostic using the same graph comparison machinery."""
    mapped = mapped_native_instances()
    owned = sage_owned_vertices()
    solid = compare_solid_graphs(
        sage_solid_digraph(),
        native_solid_digraph(),
        left_name="stub",
        right_name="native",
    )
    axiom = compare_axiom_graphs(
        sage_axiom_digraph(),
        native_axiom_digraph(),
        left_name="stub",
        right_name="native",
    )
    return {
        "sage_owned_count": len(owned),
        "mapped_native_count": len(mapped),
        "undocumented_unmapped": undocumented_unmapped_vertices(),
        "solid_graph": solid,
        "axiom_graph": axiom,
        "native_missing_stub_path": native_solid_edges_missing_stub_path(),
        "is_subcategory_mismatches": is_subcategory_mismatches(),
        "named_join_axiom_gaps": named_join_axiom_gaps(),
    }
