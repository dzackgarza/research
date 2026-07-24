"""Public registry: DOT node id → Sage category instance."""

from __future__ import annotations

from collections.abc import Callable, Iterator

from sage.categories.category import Category

from .factory import factory
from .slugs import short_name

CATEGORY_FACTORIES: dict[str, Callable[[], Category]] = {}


def _populate() -> None:
    if CATEGORY_FACTORIES:
        return
    fac = factory()

    def _binder(n: str) -> Callable[[], Category]:
        return lambda: fac.instance(n)

    for node in sorted(fac.graph.solid_nodes, key=str):
        CATEGORY_FACTORIES[node] = _binder(node)
        CATEGORY_FACTORIES[short_name(node)] = _binder(node)
    for join in fac.graph.named_joins:
        CATEGORY_FACTORIES[join] = _binder(join)
        CATEGORY_FACTORIES[short_name(join)] = _binder(join)


def get_category(node: str) -> Category:
    _populate()
    if node not in CATEGORY_FACTORIES:
        # try short name / factory directly
        return factory().instance(node)
    return CATEGORY_FACTORIES[node]()


def instantiate_all() -> dict[str, Category]:
    _populate()
    fac = factory()
    out: dict[str, Category] = {}
    for node in sorted(fac.graph.solid_nodes, key=str):
        out[node] = fac.instance(node)
    for join in fac.graph.named_joins:
        out[join] = fac.instance(join)
    return out


def iter_solid_nodes() -> Iterator[str]:
    _populate()
    yield from sorted(factory().graph.solid_nodes, key=str)
