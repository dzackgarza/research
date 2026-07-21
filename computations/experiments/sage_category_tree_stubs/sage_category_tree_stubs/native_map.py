"""Map DOT vertices to native ``sage.categories`` instances where they exist."""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

import sage.categories.all as _sage_categories
from sage.categories.category import Category
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from .dot_parse import DotGraph, parse_dot
from .factory import _DOMAIN_LADDER
from .native_research_only import RESEARCH_ONLY_VERTICES
from .sage_to_stub import SAGE_AXIOM_TO_STUB, STUB_TO_SAGE
from .slugs import axiom_method_name, is_parameterized, short_name

# stub Magmas axiom → Sage Additive* name when walking the additive branch
_STUB_TO_SAGE_ADDITIVE_AXIOM: dict[str, str] = {stub: sage for sage, stub in SAGE_AXIOM_TO_STUB.items()}

# DOT id / short name → ``sage.categories.all`` export name.
_CALLABLE_NAME: dict[str, str] = {
    **{stub: sage for stub, sage in STUB_TO_SAGE.items()},
}

_BASE_RING: dict[str, object] = {
    "Modules(R)": ZZ,
    "LeftModules(R)": ZZ,
    "RightModules(R)": ZZ,
    "Bimodules(R)": (ZZ, ZZ),
    "VectorSpaces(K) = Modules.OverField": QQ,
    "Algebras(R)": QQ,
    "AlgebrasOverField = Algebras.OverField": QQ,
    "UnitalAlgebras = Algebras.Associative.Unital": QQ,
    "LieAlgebras(R)": QQ,
    "HopfAlgebras(R)": QQ,
    "Coalgebras(R)": QQ,
    "Bialgebras(R)": QQ,
    "CliffordAlgebras(R)": QQ,
    "SymmetricAlgebras(R)": QQ,
    "ExteriorAlgebras(R)": QQ,
    "TensorAlgebras(R)": QQ,
    "C∞Algebras(R)": QQ,
    "Schemes(S)": QQ,
    "Hypersurfaces(K)": QQ,
    "CompleteIntersections(K)": QQ,
    "ToricVarieties(K)": QQ,
    "ChainComplexes(C)": QQ,
    "CochainComplexes(C)": QQ,
}

_DOMAIN_LADDER_NAMES = {row[0] for row in _DOMAIN_LADDER}

# Named joins whose native export name differs from the DOT short name.
_NAMED_JOIN_NATIVE: dict[str, str] = {
    "GCDDomains = Rings.Commutative.GCDDomain": "GcdDomains",
    "UFDs = Rings.Commutative.UFD": "UniqueFactorizationDomains",
    "PIDs = Rings.Commutative.PID": "PrincipalIdealDomains",
    "Domains = Rings.Domain": "Domains",
    "IntegralDomains = Domains.Commutative": "IntegralDomains",
    "EuclideanDomains = Rings.Commutative.Euclidean": "EuclideanDomains",
}

# Categories not re-exported by ``sage.categories.all``.
_EXTRA_IMPORTS: dict[str, str] = {
    "MagmaticAlgebras": "sage.categories.magmatic_algebras.MagmaticAlgebras",
}


def _import_category(name: str) -> Callable[..., Category] | None:
    cls = _category_callable(name)
    if cls is not None:
        return cls
    path = _EXTRA_IMPORTS.get(name)
    if path is None:
        return None
    module_path, class_name = path.rsplit(".", 1)
    module = __import__(module_path, fromlist=[class_name])
    value = getattr(module, class_name, None)
    if value is None or not callable(value):
        return None
    return cast("Callable[..., Category]", value)


def dot_vertices(graph: DotGraph | None = None) -> tuple[str, ...]:
    graph = graph or parse_dot()
    return tuple(sorted(set(graph.solid_nodes) | set(graph.named_joins), key=str))


def _callable_name(vertex: str) -> str | None:
    sn = short_name(vertex)
    if vertex in _NAMED_JOIN_NATIVE:
        return _NAMED_JOIN_NATIVE[vertex]
    if vertex in _CALLABLE_NAME:
        return _CALLABLE_NAME[vertex]
    if sn in _NAMED_JOIN_NATIVE:
        return _NAMED_JOIN_NATIVE[sn]
    if sn in _CALLABLE_NAME:
        return _CALLABLE_NAME[sn]
    base = sn.split("(")[0]
    if _import_category(base) is not None:
        return base
    return None


def _base_ring(vertex: str) -> object | None:
    sn = short_name(vertex)
    if sn in _BASE_RING:
        return _BASE_RING[sn]
    if vertex in _BASE_RING:
        return _BASE_RING[vertex]
    if is_parameterized(vertex) or is_parameterized(sn):
        ring: object = QQ
        return ring
    return None


def _category_callable(name: str) -> Callable[..., Category] | None:
    value = getattr(_sage_categories, name, None)
    if value is None or not callable(value):
        return None
    return cast("Callable[..., Category]", value)


def _instantiate(name: str, vertex: str) -> Category | None:
    cls = _import_category(name)
    if cls is None:
        return None
    base = _base_ring(vertex)
    try:
        if base is None:
            return cls()
        if isinstance(base, tuple):
            return cls(*base)
        return cls(base)
    except TypeError, ValueError:
        try:
            return cls(QQ)
        except TypeError, ValueError:
            try:
                return cls(ZZ)
            except TypeError, ValueError:
                return None


def _walk_axiom_path(host: Category, path: tuple[str, ...], *, host_vertex: str) -> Category | None:
    """Walk a stub axiom path on a native Sage host (Additive* rename on Sage only)."""
    current = host
    additive = host_vertex == "Magmas.Additive" or (host_vertex == "Magmas" and path[:1] == ("Additive",))
    for axiom_name in path:
        raw = axiom_method_name(axiom_name)
        if raw == "Additive":
            additive = True
            cls = _category_callable("AdditiveMagmas")
            if cls is None:
                return None
            current = cls()
            continue
        if raw == "Multiplicative":
            continue  # Sage Magmas is already the multiplicative branch
        method_name = _STUB_TO_SAGE_ADDITIVE_AXIOM.get(raw, raw) if additive else raw
        method = getattr(current, method_name, None)
        if method is None:
            return None
        current = method()
    return current


def native_instance(vertex: str, graph: DotGraph | None = None) -> Category | None:
    """Return the native Sage category for ``vertex``, or ``None`` if unmappable."""
    if vertex in RESEARCH_ONLY_VERTICES:
        return None

    graph = graph or parse_dot()

    call = _callable_name(vertex)
    if call is not None and vertex not in graph.named_joins:
        return _instantiate(call, vertex)

    if vertex in graph.named_joins:
        native_name = _NAMED_JOIN_NATIVE.get(vertex) or _NAMED_JOIN_NATIVE.get(short_name(vertex))
        if native_name is not None:
            inst = _instantiate(native_name, vertex)
            if inst is not None:
                return inst
        if vertex in _DOMAIN_LADDER_NAMES:
            sn = short_name(vertex)
            inst = _instantiate(sn, vertex)
            if inst is not None:
                return inst
        sn = short_name(vertex)
        call = _callable_name(vertex) or sn
        inst = _instantiate(call, vertex)
        if inst is not None:
            return inst
        host, path = graph.named_joins[vertex]
        host_cat = native_instance(host, graph)
        if host_cat is None:
            host_res = _CALLABLE_NAME.get(host, host)
            host_cat = native_instance(host_res, graph)
        if host_cat is None:
            return None
        return _walk_axiom_path(host_cat, path, host_vertex=short_name(host))

    if "." in vertex and " = " not in vertex:
        host, ax = vertex.split(".", 1)
        host_cat = native_instance(host, graph)
        if host_cat is None:
            return None
        method = getattr(host_cat, axiom_method_name(ax), None)
        if method is None:
            return None
        return cast(Category, method())

    call = _callable_name(vertex)
    if call is not None:
        return _instantiate(call, vertex)
    sn = short_name(vertex)
    call = _callable_name(sn) or sn.split("(")[0]
    return _instantiate(call, vertex)


def mapped_native_instances(graph: DotGraph | None = None) -> dict[str, Category]:
    graph = graph or parse_dot()
    out: dict[str, Category] = {}
    for vertex in dot_vertices(graph):
        if vertex in RESEARCH_ONLY_VERTICES:
            continue
        try:
            cat = native_instance(vertex, graph)
        except (AttributeError, TypeError, ValueError):
            cat = None
        if cat is not None:
            out[vertex] = cat
    return out


def unmapped_native_vertices(graph: DotGraph | None = None) -> tuple[str, ...]:
    graph = graph or parse_dot()
    mapped = mapped_native_instances(graph)
    return tuple(v for v in dot_vertices(graph) if v not in mapped)


def sage_owned_vertices(graph: DotGraph | None = None) -> tuple[str, ...]:
    graph = graph or parse_dot()
    return tuple(v for v in dot_vertices(graph) if v not in RESEARCH_ONLY_VERTICES)


def undocumented_unmapped_vertices(graph: DotGraph | None = None) -> tuple[str, ...]:
    """Vertices with no native map and not catalogued as research-only."""
    graph = graph or parse_dot()
    mapped = mapped_native_instances(graph)
    return tuple(v for v in dot_vertices(graph) if v not in mapped and v not in RESEARCH_ONLY_VERTICES)
