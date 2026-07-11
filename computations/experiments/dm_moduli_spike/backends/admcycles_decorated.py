r"""Adapter over the experimental ``admcycles.decorated_graph`` enumerator.

``admcycles.decorated_graph.stable_graphs`` is an optional, faster enumerator
that generates stable graphs up to isomorphism with explicit contraction
morphisms and an edge-count bound.  Its module is marked experimental upstream,
so it is kept behind this adapter with a pinned compatibility check: if the
module is absent (as in current ``admcycles`` releases) or its surface has
drifted, the adapter fails loudly rather than silently degrading.

``DecoratedGraph`` is never exposed as the public graph type; results are
converted to the spike's owned ``StableCurveType``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..objects.curve_types import StableCurveType, StableCurveTypes


def _require_decorated_module() -> object:
    try:
        import admcycles.decorated_graph as decorated_graph
    except ImportError as error:
        raise ImportError(
            "the admcycles-decorated backend requires 'admcycles.decorated_graph', which is not "
            "present in the installed admcycles release; use backend='admcycles-stable' or "
            "backend='pure-sage' instead"
        ) from error
    if not hasattr(decorated_graph, "stable_graphs"):  # pragma: no cover - version dependent
        raise ImportError("admcycles.decorated_graph is present but lacks the expected 'stable_graphs' enumerator (pinned-compatibility check failed)")
    return decorated_graph


class AdmcyclesDecoratedGraphBackend:
    r"""Optional faster enumerator via the experimental decorated-graph module."""

    def is_available(self) -> bool:
        try:
            _require_decorated_module()
        except ImportError:
            return False
        return True

    def stable_curve_types(self, curve_types: StableCurveTypes, max_codim: int | None = None) -> tuple[StableCurveType, ...]:
        from .admcycles_stable import _record_from_stable_graph

        decorated_graph = _require_decorated_module()
        g = curve_types.genus()
        n = curve_types.number_of_markings()
        dimension = curve_types.dimension()
        cap = dimension if max_codim is None else min(int(max_codim), dimension)
        result: dict[object, StableCurveType] = {}
        for decorated in decorated_graph.stable_graphs(g, n, cap):  # type: ignore[attr-defined]
            stable_graph = decorated.stable_graph() if hasattr(decorated, "stable_graph") else decorated
            record = _record_from_stable_graph(stable_graph, g, n)
            if record.num_edges() > cap:
                continue
            curve_type = curve_types.from_record(record)
            result[curve_type.canonical_key()] = curve_type
        return tuple(result.values())
