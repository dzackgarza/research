#!/usr/bin/env python3
"""Generate the Sage category inventory pages from the tracked audit data.

Two measurements feed the pages, and they are different things:

  * the *source axis* -- an AST audit of the SageMath 10.9 distribution at a pinned
    commit, giving the category classes, the axiom registry, the functorial
    constructions, the feature declarations and the aliases;
  * the *runtime axis* -- a full-import walk of SageMath 10.10.beta0, giving which
    source classes actually load, the classes the framework generates from axioms and
    constructions, and the category instances constructed at import.

Neither is regenerated here. The source generator needs an unpacked 10.9 distribution
that is not on this machine, and re-running the runtime dumps would measure whatever
Sage is installed today, which is a different measurement from the one recorded. Both
axes are tracked as data under writing/data/, and this script only renders them.

Every input row reaches a page: the run fails if any is left unplaced.

Run: just sage-inventory
"""
from __future__ import annotations

import json
import shutil
from collections import defaultdict
from pathlib import Path

DATA = Path("writing/data")
AUDIT = DATA / "sage-source-audit-10.9/sagemath-10.9-category-inventory.json"
RUNTIME = DATA / "sage-runtime-10.10.beta0/sagemath-10.10.beta0-runtime-inventory.json"
OUT = Path("writing/category-theory/sage/inventory")

SEP = "; "          # every multi-valued audit field except `bases`
BASE_SEP = ","      # `bases` alone


def split(value: str, sep: str = SEP) -> list[str]:
    return [part.strip() for part in str(value).split(sep) if part.strip()]


def code(text: str) -> str:
    return f"`{text}`"


def write(path: Path, title: str, body: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    page = [f"# {title}", ""] + body
    path.write_text("\n".join(page).rstrip() + "\n", encoding="utf-8")


def table(header: list[str], rows: list[list[str]]) -> list[str]:
    if not rows:
        return []
    out = ["| " + " | ".join(header) + " |",
           "| " + " | ".join("---" for _ in header) + " |"]
    out += ["| " + " | ".join(cell or "—" for cell in row) + " |" for row in rows]
    return out + [""]


def fields(pairs: list[tuple[str, str]]) -> list[str]:
    """A two-column table of the populated fields of one entity."""
    return table(["field", "value"], [[k, v] for k, v in pairs if v])


audit = json.loads(AUDIT.read_text(encoding="utf-8"))
runtime = json.loads(RUNTIME.read_text(encoding="utf-8"))

categories = audit["categories"]
axioms = audit["axioms"]
constructions = audit["functorial_constructions"]
declarations = audit["feature_declarations"]
aliases = audit["aliases"]

# --- the link table -------------------------------------------------------------
# A name links only when its page exists. Seven `functorial construction` feature
# names (Complex, DualCategory, Endsets, FinitelyGenerated, Lie, Morphism, Semisimple)
# name no registered construction, and a link for them would point at nothing.
CATEGORY_PAGE = {c["constructor"]: f"categories/{c['constructor']}.md" for c in categories}
CONSTRUCTOR_OF = {c["category_id"]: c["constructor"] for c in categories}
AXIOM_PAGE = {a["axiom"]: f"axioms/{a['axiom']}.md" for a in axioms}
CONSTRUCTION_PAGE = {c["construction"]: f"constructions/{c['construction']}.md"
                     for c in constructions}


def link(name: str, pages: dict[str, str], depth: int) -> str:
    """Link `name` into `pages` from a page `depth` directories below OUT."""
    target = pages.get(name)
    if target is None:
        return code(name)
    return f"[{code(name)}]({'../' * depth}{target})"


def link_all(value: str, pages: dict[str, str], depth: int, sep: str = SEP) -> str:
    return ", ".join(link(part, pages, depth) for part in split(value, sep))


# --- runtime facts, attributed to the source class that owns them ------------------
loaded = runtime["loaded_at_runtime"]
by_constructor = {c["constructor"]: c for c in categories}

axiom_generated: dict[str, list[dict[str, str]]] = defaultdict(list)
construction_generated: dict[str, list[dict[str, str]]] = defaultdict(list)
orphan_generated: list[dict[str, str]] = []

for entry, bucket, key in (
    *[(e, axiom_generated, "axiom") for e in runtime["axiom_generated_classes"]],
    *[(e, construction_generated, "construction") for e in runtime["construction_generated_classes"]],
):
    owner = entry["qualname"].split(".")[0].removesuffix("_with_category")
    if owner in by_constructor:
        bucket[owner].append(entry)
    else:
        orphan_generated.append({**entry, "generated_by": key})

declared_by = defaultdict(list)
for d in declarations:
    declared_by[d["category_id"]].append(d)

axiom_declared_in = defaultdict(list)
construction_declared_in = defaultdict(list)
for d in declarations:
    target = axiom_declared_in if d["feature_type"] == "axiom" else construction_declared_in
    target[d["feature_name"]].append(d)

placed: set[int] = set()   # id() of every input row rendered onto some page

if OUT.exists():
    shutil.rmtree(OUT)

# --- one page per category --------------------------------------------------------
for cat in categories:
    name = cat["constructor"]
    body: list[str] = []
    body += fields([
        ("module", code(cat["module"])),
        ("role", cat["role"]),
        ("implementation", cat["implementation_kind"]),
        ("defined by", cat["defining_relation"]),
        ("direct defining axiom", link_all(cat["direct_defining_axiom"], AXIOM_PAGE, 2)),
        ("syntactic axiom chain", link_all(cat["syntactic_defining_axiom_chain"], AXIOM_PAGE, 2)),
        ("defining construction", link_all(cat["defining_functorial_construction"], CONSTRUCTION_PAGE, 2)),
        ("bound as", code(cat["bound_as"]) if cat["bound_as"] else ""),
        ("bases", link_all(cat["bases"], CATEGORY_PAGE, 2, BASE_SEP)),
        ("source", f"[{code(cat['source'])}]({cat['source_url']})"),
        ("loads at 10.10", "yes" if loaded.get(cat["category_id"]) else "no"),
        ("notes", cat["notes"]),
    ])
    placed.add(id(cat))

    for label, field, pages in (
        ("Local axiom paths", "local_axiom_paths", AXIOM_PAGE),
        ("Local construction paths", "local_functorial_construction_paths", CONSTRUCTION_PAGE),
        ("Other local category paths", "other_local_category_paths", CATEGORY_PAGE),
    ):
        paths = split(cat[field])
        if paths:
            body += [f"## {label}", ""]
            body += [f"- {code(p)}" for p in paths] + [""]

    own = declared_by.get(cat["category_id"], [])
    if own:
        body += [f"## Declared features ({len(own)})", ""]
        body += table(
            ["feature", "type", "declaration", "target or expansion", "source"],
            [[link(d["feature_name"],
                   AXIOM_PAGE if d["feature_type"] == "axiom" else CONSTRUCTION_PAGE, 2),
              d["feature_type"], d["declaration_kind"],
              code(d["target_or_expansion"]) if d["target_or_expansion"] else "",
              f"[{code(d['source'])}]({d['source_url']})"] for d in own])
        placed.update(id(d) for d in own)

    for label, entries, column in (
        ("Axiom-generated classes", axiom_generated.get(name, []), "axiom"),
        ("Construction-generated classes", construction_generated.get(name, []), "construction"),
    ):
        if entries:
            body += [f"## {label} at 10.10 ({len(entries)})", ""]
            body += table(["class", "module", column],
                          [[code(e["qualname"]), code(e["module"]), code(e[column])]
                           for e in entries])
            placed.update(id(e) for e in entries)

    write(OUT / "categories" / f"{name}.md", name, body)

# --- one page per axiom -----------------------------------------------------------
for ax in axioms:
    name = ax["axiom"]
    body = fields([
        ("status", ax["status"]),
        ("registry entry", f"[{code(ax['registry_source'])}]({ax['registry_source_url']})"),
        ("defining categories", link_all(ax["defining_named_categories"], CATEGORY_PAGE, 2)),
        ("interface declarations", code(ax["interface_declarations"]) if ax["interface_declarations"] else ""),
        ("implementation or binding", code(ax["implementation_or_binding_declarations"]) if ax["implementation_or_binding_declarations"] else ""),
        ("method expansions", code(ax["method_expansions"]) if ax["method_expansions"] else ""),
    ])
    placed.add(id(ax))

    where = axiom_declared_in.get(name, [])
    if where:
        body += [f"## Declared in ({len(where)})", ""]
        body += table(["category", "declaration", "source"],
                      [[link(CONSTRUCTOR_OF[d["category_id"]], CATEGORY_PAGE, 2),
                        d["declaration_kind"], f"[{code(d['source'])}]({d['source_url']})"]
                       for d in where])

    generated = [e for entries in axiom_generated.values() for e in entries if e["axiom"] == name]
    if generated:
        body += [f"## Classes the framework generates at 10.10 ({len(generated)})", ""]
        body += table(["class", "module"],
                      [[code(e["qualname"]), code(e["module"])] for e in generated])

    write(OUT / "axioms" / f"{name}.md", name, body)

# --- one page per functorial construction -----------------------------------------
for con in constructions:
    name = con["construction"]
    body = fields([
        ("flavor", con["flavor"]),
        ("implementation class", code(con["category_implementation_class"])),
        ("implementation", f"[{code(con['implementation_source'])}]({con['implementation_source_url']})"),
        ("other classes with the same functor tag", code(con["other_classes_with_same_functor_tag"]) if con["other_classes_with_same_functor_tag"] else ""),
        ("interface declarations", code(con["interface_declarations"]) if con["interface_declarations"] else ""),
        ("specialized implementations", code(con["specialized_implementation_declarations"]) if con["specialized_implementation_declarations"] else ""),
        ("named result categories", code(con["named_result_categories"]) if con["named_result_categories"] else ""),
    ])
    placed.add(id(con))

    where = construction_declared_in.get(name, [])
    if where:
        body += [f"## Declared in ({len(where)})", ""]
        body += table(["category", "declaration", "source"],
                      [[link(CONSTRUCTOR_OF[d["category_id"]], CATEGORY_PAGE, 2),
                        d["declaration_kind"], f"[{code(d['source'])}]({d['source_url']})"]
                       for d in where])

    generated = [e for entries in construction_generated.values()
                 for e in entries if e["construction"] == name]
    if generated:
        body += [f"## Classes the framework generates at 10.10 ({len(generated)})", ""]
        body += table(["class", "module"],
                      [[code(e["qualname"]), code(e["module"])] for e in generated])

    write(OUT / "constructions" / f"{name}.md", name, body)

# --- aliases ----------------------------------------------------------------------
write(OUT / "aliases.md", "Category aliases",
      ["Names kept for backward compatibility, each resolving to a canonical category.", ""]
      + table(["alias", "canonical", "status", "source"],
              [[code(a["alias"]), link(a["canonical"], CATEGORY_PAGE, 1), a["status"],
                f"[{code(a['source'])}]({a['source_url']})"] for a in aliases]))
placed.update(id(a) for a in aliases)

# --- runtime-only material --------------------------------------------------------
counts = runtime["metadata"]["instance_counts"]
body = [
    f"A full import of SageMath {runtime['metadata']['sage_version']} constructs "
    f"{counts['total']} distinct category instances: {counts['plain']} plain, "
    f"{counts['axiom_refined']} axiom-refined, {counts['construction_derived']} "
    f"construction-derived, and {counts['joins']} joins. It also synthesizes "
    f"{counts['dynamic_with_category_classes']} dynamic `<Base>_with_category` "
    "implementation classes.", "",
    "Sage operates on category instances; the generated classes above them are "
    "machinery. Joins are meets in Sage's category lattice: they intersect their "
    "factors.", "",
    f"## Join categories ({len(runtime['join_categories'])})", "",
]
join_header = list(runtime["join_categories"][0])
body += table([h.replace("_", " ") for h in join_header],
              [[j[h] for h in join_header] for j in runtime["join_categories"]])
placed.update(id(j) for j in runtime["join_categories"])

body += [f"## Framework classes outside `sage.categories` ({len(runtime['framework_classes'])})", ""]
body += table(["class", "module", "note"],
              [[code(f["qualname"]), code(f["module"]), f["note"]]
               for f in runtime["framework_classes"]])
placed.update(id(f) for f in runtime["framework_classes"])

if orphan_generated:
    body += [f"## Generated classes with no source class of that name ({len(orphan_generated)})", ""]
    body += table(["class", "module", "generated by"],
                  [[code(e["qualname"]), code(e["module"]), e["generated_by"]]
                   for e in orphan_generated])
    placed.update(id(e) for e in orphan_generated)

write(OUT / "runtime.md", "Runtime category enumeration", body)

# --- index ------------------------------------------------------------------------
meta = audit["metadata"]
by_role: dict[str, list[dict[str, str]]] = defaultdict(list)
for cat in categories:
    by_role[cat["role"]].append(cat)

body = [
    "Every category class, axiom and functorial construction Sage declares, each on "
    "its own page, generated from the tracked audit data. Two measurements feed it.",
    "",
    f"**Source axis.** An AST audit of the SageMath {meta['sage_version']} distribution "
    f"at commit [`{meta['sage_commit'][:7]}`](https://github.com/sagemath/sage/commit/{meta['sage_commit']}), "
    f"scope: {meta['scope'].rstrip('.')}.",
    "",
    f"**Runtime axis.** A full-import walk of SageMath {runtime['metadata']['sage_version']}, "
    f"measured {runtime['metadata']['measured']}, recording which of those classes load "
    "and what the framework generates from them.",
    "",
    "The narrative reading of both is [the framework reference](../Sage-Category-Framework-Inventory.md).",
    "",
]
body += table(["catalogue", "entries"], [
    ["[Categories](#categories)", str(len(categories))],
    ["[Axioms](#axioms)", str(len(axioms))],
    ["[Functorial constructions](#functorial-constructions)", str(len(constructions))],
    ["[Aliases](aliases.md)", str(len(aliases))],
    ["[Runtime enumeration](runtime.md)", f"{counts['total']} instances, {counts['joins']} joins"],
])
body += ["## Categories", ""]
for role in sorted(by_role, key=lambda r: -len(by_role[r])):
    entries = sorted(by_role[role], key=lambda c: c["constructor"])
    body += [f"### {role.capitalize()} ({len(entries)})", ""]
    body += [", ".join(link(c["constructor"], CATEGORY_PAGE, 0) for c in entries), ""]
body += ["## Axioms", "",
         ", ".join(link(a["axiom"], AXIOM_PAGE, 0) for a in sorted(axioms, key=lambda a: a["axiom"])), ""]
body += ["## Functorial constructions", "",
         ", ".join(link(c["construction"], CONSTRUCTION_PAGE, 0)
                   for c in sorted(constructions, key=lambda c: c["construction"])), ""]

write(OUT / "index.md", "Sage category inventory", body)

# --- nothing may be dropped -------------------------------------------------------
inputs = {"categories": categories, "axioms": axioms,
          "functorial_constructions": constructions, "feature_declarations": declarations,
          "aliases": aliases, "join_categories": runtime["join_categories"],
          "framework_classes": runtime["framework_classes"],
          "axiom_generated_classes": runtime["axiom_generated_classes"],
          "construction_generated_classes": runtime["construction_generated_classes"]}
missing = {name: len([r for r in rows if id(r) not in placed]) for name, rows in inputs.items()}
unplaced = {name: n for name, n in missing.items() if n}
if unplaced:
    raise SystemExit(f"build-sage-inventory: rows reached no page: {unplaced}")

pages = sorted(OUT.rglob("*.md"))
print(f"build-sage-inventory: {len(pages)} pages under {OUT}")
print("  " + ", ".join(f"{name} {len(rows)}" for name, rows in inputs.items()))
