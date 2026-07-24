"""Live-kernel category *instances* for research#260 (semantic layer).

Dynamic `<Base>_with_category` classes are machinery shadows of category
instances; the mathematics is the instances. Enumerates every Category
instance alive after a full import, with special handling for joins
(real meets in the category lattice: repr + factor list).

Run:  "$SAGE_BIN" -python dump_instances.py instances.json
"""

import gc
import json
import sys

import sage.categories.all  # noqa: F401
from sage.categories.category import Category, JoinCategory
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.covariant_functorial_construction import (
    FunctorialConstructionCategory,
)

insts = [x for x in gc.get_objects() if isinstance(x, Category)]
seen: set[str] = set()
joins: list[dict[str, object]] = []
kinds: dict[str, int] = {}
for x in insts:
    r = str(x)
    if r in seen:
        continue
    seen.add(r)
    k = "join" if isinstance(x, JoinCategory) else "construction" if isinstance(x, FunctorialConstructionCategory) else "axiom" if isinstance(x, CategoryWithAxiom) else "plain"
    kinds[k] = kinds.get(k, 0) + 1
    if k == "join":
        joins.append({"repr": r, "factors": sorted(str(s) for s in x.super_categories())})
assert joins, "a full import constructs join categories"
out = {
    "n_instances": len(seen),
    "kinds": kinds,
    "joins": sorted(joins, key=lambda j: str(j["repr"])),
}
json.dump(out, open(sys.argv[1], "w"), indent=1)
print("instances:", len(seen), "| kinds:", kinds, "| joins:", len(joins))
