"""Dump live Sage ``super_categories()`` (and related) into a probe file.

Empirical only. Does not correct Sage parents or assert mathematical character.
"""

from __future__ import annotations

import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .design_sources import DESIGN_ROOT

RUNTIME_PROBE_PATH = DESIGN_ROOT / "sage" / "runtime_probe.json"
PROBE_VERSION = "1.0.0"


def _cls_key(name: str) -> str:
    return name.removesuffix("_with_category")


def dump_runtime_probe() -> dict[str, Any]:
    """Enumerate ``category_sample()`` under the running Sage kernel."""
    import importlib

    importlib.import_module("sage.categories.all")
    from sage.categories.category import JoinCategory, category_sample
    from sage.categories.category_with_axiom import CategoryWithAxiom, all_axioms
    from sage.categories.covariant_functorial_construction import (
        FunctorialConstructionCategory,
    )
    from sage.version import version

    now = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    cats = sorted(set(category_sample()), key=str)
    instances: list[dict[str, Any]] = []
    for c in cats:
        supers = list(c.super_categories())
        kind = "category_instance"
        if isinstance(c, JoinCategory):
            kind = "join_category"
        elif isinstance(c, CategoryWithAxiom):
            kind = "category_with_axiom"
        instances.append(
            {
                "repr": str(c),
                "cls": type(c).__name__,
                "cls_key": _cls_key(type(c).__name__),
                "module": type(c).__module__,
                "kind": kind,
                "supers": [
                    {
                        "repr": str(s),
                        "cls": type(s).__name__,
                        "cls_key": _cls_key(type(s).__name__),
                        "module": type(s).__module__,
                    }
                    for s in supers
                ],
                "axioms": sorted(c.axioms()),
                "probe": "super_categories",
            }
        )

    constructions: dict[str, list[str]] = {}
    stack = [FunctorialConstructionCategory]
    seen: set[type] = set()
    while stack:
        base = stack.pop()
        for sub in base.__subclasses__():
            if sub in seen:
                continue
            seen.add(sub)
            stack.append(sub)
            tag = sub.__dict__.get("_functor_category")
            if tag:
                constructions.setdefault(str(tag), []).append(f"{sub.__module__}.{sub.__name__}")

    return {
        "probe": {
            "schema_version": 1,
            "probe_version": PROBE_VERSION,
            "sage_version": str(version),
            "generated_at": now,
            "python_version": sys.version.split()[0],
            "category_sample_count": len(instances),
            "note": ("Runtime axis from category_sample(). Parameterized categories appear via representative instances."),
        },
        "instances": instances,
        "all_axioms": sorted(all_axioms),
        "constructions": {k: sorted(v) for k, v in sorted(constructions.items())},
    }


def write_runtime_probe(path: Path | None = None) -> Path:
    dest = path or RUNTIME_PROBE_PATH
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = dump_runtime_probe()
    dest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return dest


def main() -> int:
    path = write_runtime_probe()
    data = json.loads(path.read_text(encoding="utf-8"))
    n_edges = sum(len(i["supers"]) for i in data["instances"])
    print(f"wrote {path} (instances={len(data['instances'])} edges={n_edges} sage={data['probe']['sage_version']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
