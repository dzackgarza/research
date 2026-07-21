"""Live-kernel class walk for research#260 (axis 3 of the enumeration).

Imports every module under sage.categories, then transitively walks
Category.__subclasses__() to record EVERY loaded category class with its
module, qualname, and kind flags (axiom-generated, functorial-construction,
with_realizations, framework/base). This is the existence oracle for names:
exported-namespace membership (axis 1) and category_sample() instances
(axis 2) both undercount.

Run:  "$SAGE_BIN" -python dump_classes.py classes.json
"""

from __future__ import annotations

import importlib
import json
import pkgutil
import sys
from typing import Any

import sage.categories


def _force_load_category_modules() -> dict[str, str]:
    importlib.import_module("sage.categories.all")
    failures: dict[str, str] = {}
    for module in pkgutil.iter_modules(sage.categories.__path__, "sage.categories."):
        try:
            importlib.import_module(module.name)
        except Exception as exc:
            failures[module.name] = f"{type(exc).__name__}: {exc}"
    return failures


def _collect_rows() -> list[dict[str, Any]]:
    from sage.categories.category import Category
    from sage.categories.category_with_axiom import CategoryWithAxiom
    from sage.categories.covariant_functorial_construction import (
        FunctorialConstructionCategory,
    )

    rows: list[dict[str, Any]] = []
    seen: set[type] = set()
    stack: list[type] = [Category]
    while stack:
        base = stack.pop()
        for sub in base.__subclasses__():
            if sub in seen:
                continue
            seen.add(sub)
            stack.append(sub)
            rows.append(
                {
                    "cls": sub.__name__,
                    "qualname": sub.__qualname__,
                    "module": sub.__module__,
                    "axiom_generated": issubclass(sub, CategoryWithAxiom),
                    "construction": issubclass(sub, FunctorialConstructionCategory),
                }
            )
    return rows


def main() -> None:
    failures = _force_load_category_modules()
    rows = _collect_rows()
    assert len(rows) > 300, "class walk implausibly small"
    out = {
        "n_classes": len(rows),
        "import_failures": failures,
        "classes": sorted(rows, key=lambda row: (row["module"], row["qualname"])),
    }
    json.dump(out, open(sys.argv[1], "w"), indent=1)
    print("category classes:", len(rows), "| import failures:", len(failures))


if __name__ == "__main__":
    main()
