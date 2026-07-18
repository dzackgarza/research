"""Live-kernel enumeration for research#260.

Dumps, from the running Sage kernel (no hand lists):
  - the category inventory from category_sample() (name, class, supers, axioms)
  - the exported category-like names in sage.categories.all (namespace cross-check)
  - the canonical axiom registry (all_axioms)
  - functorial-construction categories discovered by walking
    FunctorialConstructionCategory subclasses
  - the Modules(ZZ) -> ... -> Objects() super_categories edge list (first specimen)

Run:  "$SAGE_BIN" -python dump_categories.py out.json
"""
import json
import sys

import sage.categories.all as A  # force-load every category module
from sage.categories.category import Category, category_sample
from sage.categories.category_with_axiom import all_axioms
from sage.categories.covariant_functorial_construction import (
    FunctorialConstructionCategory,
)
from sage.categories.modules import Modules
from sage.categories.objects import Objects
from sage.rings.integer_ring import ZZ
from sage.version import version

out = {"sage_version": version}

cats = sorted(set(category_sample()), key=str)
assert len(cats) > 50, "category_sample() implausibly small"
out["categories"] = [
    {
        "repr": str(c),
        "cls": type(c).__name__,
        "module": type(c).__module__,
        "supers": sorted(str(s) for s in c.super_categories()),
        "axioms": sorted(c.axioms()),
    }
    for c in cats
]

names = []
for n in sorted(dir(A)):
    obj = getattr(A, n)
    if isinstance(obj, Category):
        names.append({"name": n, "kind": "instance"})
    elif isinstance(obj, type) and issubclass(obj, Category):
        names.append({"name": n, "kind": "class"})
    elif callable(obj) and n[:1].isupper():
        names.append({"name": n, "kind": "callable"})
out["namespace"] = names

out["all_axioms"] = sorted(all_axioms)

cons = {}
stack = [FunctorialConstructionCategory]
seen = set()
while stack:
    k = stack.pop()
    for s in k.__subclasses__():
        if s in seen:
            continue
        seen.add(s)
        stack.append(s)
        fc = s.__dict__.get("_functor_category")
        if fc:
            cons.setdefault(fc, []).append(f"{s.__module__}.{s.__name__}")
out["constructions"] = {k: sorted(v) for k, v in sorted(cons.items())}

edges = set()
todo = [Modules(ZZ)]
visited = set()
while todo:
    c = todo.pop()
    if str(c) in visited:
        continue
    visited.add(str(c))
    for s in c.super_categories():
        edges.add((str(c), str(s)))
        todo.append(s)
assert any(str(Objects()) == b for _, b in edges), "chain must reach Objects()"
out["modules_ZZ_edges"] = sorted(edges)

json.dump(out, open(sys.argv[1], "w"), indent=1)
print(
    "categories:", len(out["categories"]),
    "| namespace names:", len(names),
    "| axioms:", len(out["all_axioms"]),
    "| construction kinds:", len(cons),
    "| specimen edges:", len(edges),
)
