"""Helpers for cluster modules."""

from __future__ import annotations

from sage.categories.category import Category

from ..factory import factory


def cat(node: str) -> Category:
    return factory().instance(node)


def axiom(host: str, name: str) -> Category:
    return factory().axiom_instance(host, name)
