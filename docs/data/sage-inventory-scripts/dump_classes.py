"""Live-kernel class walk for research#260 (axis 3 of the enumeration).

Imports every module under sage.categories, then transitively walks
Category.__subclasses__() to record EVERY loaded category class with its
module, qualname, and kind flags (axiom-generated, functorial-construction,
with_realizations, framework/base). This is the existence oracle for names:
exported-namespace membership (axis 1) and category_sample() instances
(axis 2) both undercount.

Run:  "$SAGE_BIN" -python dump_classes.py classes.json
"""
import importlib
import json
import pkgutil
import sys

import sage.categories
import sage.categories.all  # noqa: F401

failures = {}
for m in pkgutil.iter_modules(sage.categories.__path__, "sage.categories."):
    try:
        importlib.import_module(m.name)
    except Exception as e:  # record, never skip silently
        failures[m.name] = f"{type(e).__name__}: {e}"

from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.covariant_functorial_construction import (
    FunctorialConstructionCategory,
)

rows = []
seen = set()
stack = [Category]
while stack:
    k = stack.pop()
    for s in k.__subclasses__():
        if s in seen:
            continue
        seen.add(s)
        stack.append(s)
        rows.append(
            {
                "cls": s.__name__,
                "qualname": s.__qualname__,
                "module": s.__module__,
                "axiom_generated": issubclass(s, CategoryWithAxiom),
                "construction": issubclass(s, FunctorialConstructionCategory),
            }
        )
assert len(rows) > 300, "class walk implausibly small"
out = {
    "n_classes": len(rows),
    "import_failures": failures,
    "classes": sorted(rows, key=lambda r: (r["module"], r["qualname"])),
}
json.dump(out, open(sys.argv[1], "w"), indent=1)
print("category classes:", len(rows), "| import failures:", len(failures))
