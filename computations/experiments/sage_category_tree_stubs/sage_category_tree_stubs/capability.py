"""Which Sage implementations can serve an object of a normalized category.

The bridge exists to answer one question. A user of the DSL constructs an object
``X`` of some normalized category ``C``; which parts of Sage can be used to compute
with it?

The map that answers it is

    sigma : SageCategory -> constructible normalized category

sending each named Sage category to the normalized category it implements. Sage's own
imprecision does not obstruct this: ``AdditiveMagmas`` is not quite the right axiom
join in Sage and still has a definite destination. sigma is *not* injective and is not
meant to be, because the operative direction is the other one: the **fiber** over a
normalized category is the set of Sage implementations that can supply algorithms for
its objects. Whether Sage regards two members of a fiber as equal or equivalent is not
this module's concern.

Nothing here validates, mirrors, or scores Sage's ``super_categories`` relation. That
relation is Sage's C3 linearization of a transitive order, so which pairs are
"immediate" is an artifact of the algorithm rather than a mathematical fact.

**Direction.** A method's availability follows the method's own domain and the
direction of the functor, never fiber membership. ``GradedModules`` implements
``Modules(R).Graded`` and the functor forgets the grading, so a graded module inherits
module methods while a plain module inherits no grading methods. Making an arbitrary
module graded is an explicit lift -- a named section of the grading fiber -- not
something inheritance supplies.
"""

from __future__ import annotations

from typing import Any

from .mapping_build import build_mapping

# Relations that keep a Sage category out of sigma's domain, for different reasons.
# `removed` is the ledger's ruling that the entry is not mathematics -- a dispatch or
# representation mechanism -- so it can supply no algorithm to a DSL object and is not
# a gap. `unsupported` is a genuine gap: a mathematical category with no destination.
_NOT_MATHEMATICS = "removed"
_GAP = "unsupported"


def sigma(mapping: dict[str, Any] | None = None) -> dict[str, str]:
    """Sage category name -> the normalized category it implements.

    Keyed on the authored target *expression*, not on its base. The base of
    ``GradedModules`` is ``Modules(R)``; keying there would record that the
    implementation lands somewhere over modules but not which category it serves.

    Sage categories the ledger rules non-mathematical are excluded rather than given a
    destination. ``Sets().Facade()`` is the standing example: a facade parent is one
    whose elements are not instances of its own element class, so the category is a
    dispatch bucket whose methods are element-construction and coercion plumbing.
    There is no category of facade sets to implement. Where an individual facade parent
    carries mathematical content it is a subobject -- a monomorphism into the parent
    its elements actually inhabit -- which is data on that object, not a category.
    """
    m = mapping or build_mapping()
    out: dict[str, str] = {}
    for row in m["category_mappings"]:
        if row.get("relation") in {_GAP, _NOT_MATHEMATICS}:
            continue
        expression = row.get("normalized_reading")
        name = row.get("source_sage_name")
        if expression and name:
            out[str(name)] = str(expression)
    return out


def excluded_as_non_mathematical(mapping: dict[str, Any] | None = None) -> dict[str, str]:
    """Sage categories that implement no normalized category, with the ledger's reason."""
    m = mapping or build_mapping()
    return {
        str(r["source_sage_name"]): str((r.get("provenance") or {}).get("mapping_kind") or r.get("normalized_reading") or "")
        for r in m["category_mappings"]
        if r.get("relation") == _NOT_MATHEMATICS
    }


def fibers(mapping: dict[str, Any] | None = None) -> dict[str, list[str]]:
    """Normalized category -> the Sage implementations that land on it."""
    out: dict[str, list[str]] = {}
    for name, expression in sigma(mapping).items():
        out.setdefault(expression, []).append(name)
    return {k: sorted(v) for k, v in sorted(out.items())}


def refinement_chain(expression: str) -> list[str]:
    """An expression and the expressions it refines, longest first.

    ``Modules(R).Graded.Finite`` refines ``Modules(R).Graded`` refines ``Modules(R)``.
    Each step forgets one authored classifier application, so the chain is read off the
    expression rather than searched for in a graph.

    This covers only the refinements the expression itself records. Structural
    functors between distinct bases -- a ring's underlying additive group, say -- are
    declared relations in the semantic seed and are deliberately not followed here;
    including them requires deciding what a canonical functor is when several exist,
    which is a coherence question and not a reachability one.
    """
    parts = expression.split(".")
    return [".".join(parts[: i + 1]) for i in range(len(parts) - 1, -1, -1)]


def providers_for(expression: str, mapping: dict[str, Any] | None = None) -> dict[str, list[str]]:
    """Sage implementations usable for an object of ``expression``.

    Returns the fiber over the expression and over each category it refines, since an
    object of ``Modules(R).Graded`` is in particular a module and may use module
    algorithms. The converse never holds, which is why nothing above the expression is
    consulted.
    """
    fib = fibers(mapping)
    return {step: fib[step] for step in refinement_chain(expression) if step in fib}


def coverage_report(mapping: dict[str, Any] | None = None) -> str:
    m = mapping or build_mapping()
    s = sigma(m)
    fib = fibers(m)
    unmapped = [r.get("source_sage_name") for r in m["category_mappings"] if r.get("relation") == _GAP]
    excluded = excluded_as_non_mathematical(m)
    shared = {k: v for k, v in fib.items() if len(v) > 1}
    lines = [
        "Sage capability map (sigma : Sage category -> normalized category)",
        f"  Sage categories with a destination: {len(s)}",
        f"  distinct normalized destinations:   {len(fib)}",
        f"  destinations with several implementations: {len(shared)}",
        f"  Sage categories with no destination (gap): {len(unmapped)}",
        f"  excluded as non-mathematical (not a gap):   {len(excluded)}",
    ]
    if excluded:
        lines.append("")
        lines.append("Not mathematics; supplies no algorithm to any DSL object:")
        for name, reason in sorted(excluded.items()):
            lines.append(f"  {name} -- {reason}")
    if shared:
        lines.append("")
        lines.append("Destinations served by more than one Sage category:")
        for dest, names in sorted(shared.items()):
            lines.append(f"  {dest}")
            lines.append(f"      {', '.join(names)}")
    if unmapped:
        lines.append("")
        lines.append("No destination (cannot supply algorithms to any DSL object):")
        for name in sorted(x for x in unmapped if x):
            lines.append(f"  {name}")
    return "\n".join(lines)


def main() -> int:
    print(coverage_report())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
