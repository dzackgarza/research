"""Stable identities for Sage axiom-/construction-composed categories.

Sage parents are often ``Base.Axiom`` or ``Base.Axiom.Axiom`` (and sometimes
``Base.Construction``), not a top-level named class. The inventory census
misses those; this module mints empirical ids and a normalized *reading*
(Additive* rehost → flat Magmas path) without inventing mathematics.
"""

from __future__ import annotations

import re
from typing import Any

# Sage Additive* axiom → flat Magmas axiom (same table as correspondence).
ADDITIVE_AXIOM_TO_FLAT: dict[str, str] = {
    "AdditiveAssociative": "Associative",
    "AdditiveUnital": "Unital",
    "AdditiveInverse": "Inverse",
    "AdditiveCommutative": "Commutative",
}

# Sage axiom name → the normalized classifier that names the same condition.
# Sage's FiniteDimensional is module-relative, so the condition it states is finite rank;
# the authored ledger already normalizes every FiniteDimensional* row that way.
SAGE_AXIOM_TO_CLASSIFIER: dict[str, str] = {
    "FiniteDimensional": "FiniteRank",
}


# Named additive bases → Magmas.Additive… classifier prefixes.
ADDITIVE_BASE_TO_MAGMAS: dict[str, str] = {
    "AdditiveMagmas": "Magmas.Additive",
    "AdditiveSemigroups": "Magmas.Additive.Associative",
    "AdditiveMonoids": "Magmas.Additive.Associative.Unital",
    "AdditiveGroups": "Magmas.Additive.Associative.Unital.Inverse",
    "CommutativeAdditiveSemigroups": "Magmas.Additive.Associative.Commutative",
    "CommutativeAdditiveMonoids": "Magmas.Additive.Associative.Unital.Commutative",
    "CommutativeAdditiveGroups": "AdditiveGroups.Commutative",
}

# Functorial construction tags (not axioms) appearing in dotted cls keys.
CONSTRUCTION_TAGS: frozenset[str] = frozenset(
    {
        "Algebras",
        "CartesianProducts",
        "TensorProducts",
        "Dual",
        "Quotients",
        "Subquotients",
        "Homsets",
        "Subcategories",
        "IsomorphicObjects",
        "QuotientFields",
    }
)


def _slug(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "_", text)
    return text.strip("_").lower() or "anon"


def is_composed_cls_key(cls_key: str) -> bool:
    return "." in (cls_key or "")


def composed_sage_id(cls_key: str) -> str:
    """Stable observed id for a dotted Sage cls key."""
    parts = [p for p in cls_key.split(".") if p]
    return "sage.category.with_axiom." + ".".join(_slug(p) for p in parts)


def parse_composed(cls_key: str) -> tuple[str, tuple[str, ...]]:
    parts = tuple(p for p in cls_key.split(".") if p)
    if not parts:
        return "", ()
    return parts[0], parts[1:]


def rename_step(step: str) -> str:
    """Sage axiom name → normalized classifier name, operation role preserved.

    ``Additive*`` is flattened only by :func:`normalized_reading` and only under an
    additive base, where there is one operation and it is the additive one. On a base
    with two operations the prefix is the operation role, and dropping it collides the
    additive and multiplicative forms of the same law.
    """
    return SAGE_AXIOM_TO_CLASSIFIER.get(step, step)


def normalized_reading(cls_key: str) -> str:
    """Classifier-style reading under flat Magmas Additive* rehosting.

    Example: ``AdditiveMagmas.AdditiveCommutative`` → ``Magmas.Additive.Commutative``.
    """
    base, steps = parse_composed(cls_key)
    if not base:
        return cls_key
    if base in ADDITIVE_BASE_TO_MAGMAS:
        path = ADDITIVE_BASE_TO_MAGMAS[base]
        for step in steps:
            path = f"{path}.{ADDITIVE_AXIOM_TO_FLAT.get(step, rename_step(step))}"
        return path
    # Not an additive base: the Additive prefix carries the operation role and stays.
    return ".".join([base, *(rename_step(s) for s in steps)])


def composed_kind(cls_key: str) -> str:
    _base, steps = parse_composed(cls_key)
    if steps and steps[-1] in CONSTRUCTION_TAGS:
        return "construction_category"
    return "category_with_axiom"


def expression_for(cls_key: str) -> str:
    """Sage probe expression, e.g. ``AdditiveMagmas().AdditiveCommutative()``."""
    base, steps = parse_composed(cls_key)
    expr = f"{base}()"
    for step in steps:
        expr += f".{step}()"
    return expr


def make_composed_category_record(
    cls_key: str,
    *,
    repr_text: str | None = None,
    module: str | None = None,
) -> dict[str, Any]:
    base, steps = parse_composed(cls_key)
    return {
        "id": composed_sage_id(cls_key),
        "kind": composed_kind(cls_key),
        "symbol": f"sage.categories.composed.{cls_key}",
        "module": module or "composed",
        "qualname": cls_key,
        "inventory_category_id": None,
        "parameters": [],
        "representative": {
            "expression": expression_for(cls_key),
            "repr": repr_text,
            "bindings": {},
            "note": "axiom-/construction-composed; not a top-level inventory class",
        },
        "source": {"path": None, "line_start": None, "content_hash": None},
        "immediate_supercategories": [],
        "declared_supercategories": [],
        "observed_supercategories": [],
        "defined_axioms": [],
        "available_axioms": [],
        "satisfied_axioms": list(steps),
        "defined_constructions": [],
        "available_constructions": [],
        "aliases": [],
        "deprecated_aliases": [],
        "defining_relation": None,
        "composed": {
            "base": base,
            "steps": list(steps),
            "normalized_reading": normalized_reading(cls_key),
        },
        "notes": ("Empirical identity for Sage Base.Axiom(…) parent. Character is not asserted here."),
    }


def seed_entity_for_reading(
    reading: str,
    *,
    entity_by_dot: dict[str, str],
) -> str | None:
    """Match a normalized reading against seed ``dot_vertex`` indexes."""
    if reading in entity_by_dot:
        return entity_by_dot[reading]
    return None


def build_dot_vertex_index(entities: list[dict[str, Any]]) -> dict[str, str]:
    out: dict[str, str] = {}
    for e in entities:
        eid = e["id"]
        dv = e.get("dot_vertex") or ""
        if not dv:
            continue
        out[dv] = eid
        if " = " in dv:
            name, expr = dv.split(" = ", 1)
            out.setdefault(name, eid)
            out.setdefault(expr, eid)
    return out
