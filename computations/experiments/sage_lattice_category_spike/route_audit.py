r"""Introspective category-route audit and on-demand route report (issue #197).

One introspection surface, two consumers: the parametrized audit tests
(``tests/core/test_route_audit.sage``) and the ephemeral route report
(``__main__`` below, exposed as the spike justfile's ``route-report``
recipe). Every fact is derived from the LIVE graph at invocation time —
there is no stored certificate, no committed record, no golden file, so
disagreement between report and tests is impossible by construction.

The one authored input is the frozen ownership table inside
``maintained_parent_inventory``: for each maintained parent, the declared
owner of every generic set operation — a contract node in the domain
algebra, the structured forwarding owner (``ViaUnderlyingSet``), the
foundation's axiom generics, or a sanctioned first concrete runtime
provider. The audit derives the ACTUAL defining implementation from the
parent's resolution order and compares; a leaf override turns the
provenance check red even when its answer is numerically correct — that
anti-bypass discrimination is what distinguishes this audit from
output-comparison testing.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from itertools import islice
from typing import Any, NamedTuple, cast

_SPIKE = "sage_lattice_category_spike"


class MaintainedParent(NamedTuple):
    r"""One inventory row: a maintained parent, its refinement
    classification, and its frozen per-operation ownership table."""

    label: str
    construct: Callable[[], Any]
    classification: str  # "finite" | "countably_infinite" | "uncountable"
    owners: dict[str, str]  # operation -> "module::qualname" of the declared owner
    # enumeration surface for the executable-refinement check: the parent
    # itself, or its underlying set (composition-pure structured facades
    # keep enumeration off the structured surface)
    enumeration_surface: str = "self"
    # a nonidentity endomorphism for the functor checks (None: the parent's
    # family carries no audited morphism factory)
    nonidentity_morphism: Callable[[Any], Any] | None = None


def _lattice(name: str) -> Any:
    from .lattice_categories import Lattice

    return Lattice(name)


def _lattice_owner(operation: str) -> str:
    return f"{_SPIKE}.algebra.domain_algebra::Lattice.{operation}"


def _group_owner(operation: str) -> str:
    return f"{_SPIKE}.algebra.domain_algebra::FiniteAbelianGroup.{operation}"


def _forwarding(operation: str) -> str:
    return f"{_SPIKE}.objects.underlying_sets::ViaUnderlyingSet.{operation}"


_LATTICE_OWNERS = {
    "cardinality": _lattice_owner("cardinality"),
    "is_finite": _lattice_owner("is_finite"),
    "is_infinite": _lattice_owner("is_infinite"),
    "is_countable": _lattice_owner("is_countable"),
    "is_uncountable": _lattice_owner("is_uncountable"),
    "__iter__": _lattice_owner("__iter__"),
    "__getitem__": _lattice_owner("__getitem__"),
    "index": _lattice_owner("index"),
    "underlying_set": _forwarding("underlying_set"),
}


def maintained_parent_inventory() -> tuple[MaintainedParent, ...]:
    r"""The complete maintained-parent inventory. Tests parametrize over
    this and the report iterates it: adding a parent here audits it
    everywhere, with no test edits."""
    from sage.rings.integer_ring import ZZ

    def _rank_zero() -> Any:
        from sage.matrix.constructor import matrix

        from .lattice_categories import Lattice

        return Lattice(matrix(ZZ, 0, 0, []), label="zero-lattice")

    def _first_isometry(lattice: Any) -> Any:
        return lattice.isometry_group().gens()[0]

    return (
        MaintainedParent(
            label="lattice A2 (definite)",
            construct=lambda: _lattice("A2"),
            classification="countably_infinite",
            owners=dict(_LATTICE_OWNERS),
            nonidentity_morphism=_first_isometry,
        ),
        MaintainedParent(
            label="lattice U (indefinite)",
            construct=lambda: _lattice("U"),
            classification="countably_infinite",
            owners=dict(_LATTICE_OWNERS),
        ),
        MaintainedParent(
            label="lattice of rank zero",
            construct=_rank_zero,
            classification="finite",
            owners=dict(_LATTICE_OWNERS),
        ),
        MaintainedParent(
            label="discriminant group of A2",
            construct=lambda: _lattice("A2").discriminant_group(),
            classification="finite",
            owners={
                "cardinality": _group_owner("cardinality"),
                "is_finite": _group_owner("is_finite"),
                "elements": _group_owner("elements"),
                "list": _group_owner("list"),
                "__iter__": _group_owner("__iter__"),
                "underlying_set": _forwarding("underlying_set"),
            },
        ),
        MaintainedParent(
            label="genus of A2",
            construct=lambda: _lattice("A2").genus(),
            classification="finite",
            owners={
                "cardinality": f"{_SPIKE}.algebra.domain_algebra::Genus.cardinality",
                "is_finite": f"{_SPIKE}.algebra.domain_algebra::Genus.is_finite",
                "__iter__": f"{_SPIKE}.algebra.domain_algebra::Genus.__iter__",
            },
        ),
        MaintainedParent(
            label="Isom(A2, A2)",
            construct=lambda: _lattice("A2").Isom(_lattice("A2")),
            classification="finite",
            owners={
                # sanctioned first concrete runtime provider: the homset's
                # empty-vs-torsor dispatcher, delegating to the general
                # node's typed torsor operations
                "cardinality": f"{_SPIKE}.morphisms.homsets::IsometryHomset.cardinality",
                "__iter__": f"{_SPIKE}.morphisms.homsets::IsometryHomset.__iter__",
                "transporter": f"{_SPIKE}.morphisms.homsets::IsometryHomset.transporter",
                "underlying_set": f"{_SPIKE}.morphisms.homsets::IsometryHomset.underlying_set",
            },
        ),
        MaintainedParent(
            label="O(A2)",
            construct=lambda: _lattice("A2").isometry_group(),
            classification="finite",
            owners={
                "cardinality": f"{_SPIKE}.algebra.domain_algebra::IsometryGroup.cardinality",
                # sanctioned first concrete runtime provider: the engine-
                # backed enumeration witness
                "__iter__": f"{_SPIKE}.morphisms.isometry_groups::SyntheticIsometryGroup.__iter__",
                "underlying_set": _forwarding("underlying_set"),
            },
        ),
        MaintainedParent(
            label="ZZ (fundamental)",
            construct=_integers,
            classification="countably_infinite",
            owners={
                "cardinality": _forwarding("cardinality"),
                "is_finite": _forwarding("is_finite"),
                "is_countable": _forwarding("is_countable"),
                "__iter__": f"{_SPIKE}.objects.fundamental_sets::Integers.__iter__",
                "underlying_set": _forwarding("underlying_set"),
            },
            enumeration_surface="underlying_set",
        ),
        MaintainedParent(
            label="RR (fundamental)",
            construct=_reals,
            classification="uncountable",
            owners={
                "cardinality": _forwarding("cardinality"),
                "is_countable": _forwarding("is_countable"),
                "is_uncountable": _forwarding("is_uncountable"),
                "underlying_set": _forwarding("underlying_set"),
            },
        ),
        MaintainedParent(
            label="Z/6 (fundamental)",
            construct=lambda: _zmod(6),
            classification="finite",
            owners={
                "cardinality": f"{_SPIKE}.objects.fundamental_sets::IntegerModRing.cardinality",
                "is_finite": _forwarding("is_finite"),
                "underlying_set": _forwarding("underlying_set"),
            },
            enumeration_surface="underlying_set",
        ),
    )


def _integers() -> Any:
    from .objects.fundamental_sets import Integers

    return Integers()


def _reals() -> Any:
    from .objects.fundamental_sets import Reals

    return Reals()


def _zmod(modulus: int) -> Any:
    from .objects.fundamental_sets import IntegerModRing

    return IntegerModRing(modulus)


# ---------------------------------------------------------------------------
# derivation from the live graph
# ---------------------------------------------------------------------------


def provenance_of_type(parent_type: type, operation: str) -> str:
    r"""``module::qualname`` of the implementation the resolution order
    actually selects for ``operation`` — the fact the ownership table is
    compared against. Provenance is a fact of the TYPE, which is what lets
    the anti-bypass test exercise a deliberately bypassed subclass."""
    implementation = getattr(parent_type, operation, None)
    if implementation is None:
        return "<missing>"
    return f"{getattr(implementation, '__module__', '<?>')}::{getattr(implementation, '__qualname__', '<?>')}"


def provenance(parent: Any, operation: str) -> str:
    return provenance_of_type(type(parent), operation)


def provenance_failures(parent_type: type, owners: dict[str, str]) -> list[str]:
    r"""Check 2's comparator: every audited operation's resolved
    implementation against its declared owner. A leaf override reds this
    even when its answer is numerically correct."""
    failures = []
    for operation, owner in sorted(owners.items()):
        actual = provenance_of_type(parent_type, operation)
        if actual != owner:
            failures.append(f"{operation}: resolved to {actual}, declared owner is {owner}")
    return failures


def derived_route(parent: Any) -> tuple[str, ...]:
    r"""The owned category nodes on the parent's route, in linearization
    order, ending at the owned ``Sets()`` when the route terminates."""
    return tuple(repr(node) for node in parent.category().all_super_categories() if type(node).__module__.startswith(_SPIKE))


def _audit_route(spec: MaintainedParent, parent: Any) -> list[str]:
    r"""Check 1: the route to the owned Sets() exists and terminates.
    Structured parents are deliberately NOT subcategories of Sets() (the
    forgetful functor is faithful, never an inclusion), so their route is
    the underlying-set functor's codomain; unstructured parents (a genus)
    are placed in Sets() directly."""
    from .objects.sets import Sets

    failures: list[str] = []
    if parent in Sets():
        return failures
    if "underlying_set" not in spec.owners:
        failures.append("no route to the owned Sets(): neither direct placement nor an underlying-set functor")
        return failures
    if parent.underlying_set() not in Sets():
        failures.append("the underlying-set route does not terminate at the owned Sets()")
    return failures


def _audit_provenance(spec: MaintainedParent, parent: Any) -> list[str]:
    return provenance_failures(type(parent), spec.owners)


def _audit_forgetful_functor(spec: MaintainedParent, parent: Any) -> list[str]:
    r"""Checks 3-5: honesty, morphism action, and functor laws, run where
    the parent carries the forwarding surface and a morphism factory."""
    from .objects.magmas import UnderlyingSetFunctor
    from .objects.sets import Sets
    from .objects.underlying_sets import UnderlyingSet

    failures: list[str] = []
    if "underlying_set" not in spec.owners:
        return failures
    underlying = parent.underlying_set()
    if not isinstance(underlying, UnderlyingSet):
        failures.append(f"underlying_set() returned {type(underlying).__name__}, not an UnderlyingSet")
        return failures
    if underlying is parent:
        failures.append("the forgetful functor returned the structured object unchanged")
    if underlying not in Sets():
        failures.append("the underlying set is not in the owned Sets()")
    if spec.classification == "uncountable":
        probe = parent.an_element()
    else:
        surface = parent if spec.enumeration_surface == "self" else parent.underlying_set()
        probe = next(iter(cast(Iterable[Any], surface)))
    if probe not in underlying:
        failures.append(f"element {probe!r} of the parent is not in its underlying set")

    if spec.nonidentity_morphism is None:
        return failures
    functor = UnderlyingSetFunctor(parent.category())
    if functor(parent) is not underlying:
        failures.append("the functor's object action disagrees with the forwarding route")
    morphism = spec.nonidentity_morphism(parent)
    image = functor(morphism)
    if image.domain() is not UnderlyingSet(morphism.domain()) or image.codomain() is not UnderlyingSet(morphism.codomain()):
        failures.append("the functor's morphism action has wrong boundaries")
    if image(probe) != morphism(probe):
        failures.append("the functor's morphism action disagrees with the morphism on an element")
    identity_image = functor(parent.identity_morphism())
    if identity_image(probe) != probe:
        failures.append("the functor does not preserve the identity on elements")
    composed = functor(morphism * morphism)
    if composed(probe) != image(image(probe)):
        failures.append("the functor does not preserve composition on elements")
    return failures


def _audit_route_coherence(spec: MaintainedParent, parent: Any) -> list[str]:
    r"""Check 6: where the parent's category reaches Sets() through more
    than one root (the ring additive/multiplicative diamond), the exposed
    forwarding is the single shared owner and the underlying set is one
    object regardless of route."""
    failures: list[str] = []
    if "underlying_set" not in spec.owners:
        return failures
    if spec.owners["underlying_set"].endswith("ViaUnderlyingSet.underlying_set") and not provenance(parent, "underlying_set").endswith("ViaUnderlyingSet.underlying_set"):
        failures.append("the forwarding owner is not the shared ViaUnderlyingSet block")
    if parent.underlying_set() is not parent.underlying_set():
        failures.append("the underlying set is not unique across routes")
    return failures


def _audit_refinement(spec: MaintainedParent, parent: Any) -> list[str]:
    r"""Check 7: the classification's executable consequences."""
    from .objects.cardinals import Cardinal, aleph0

    failures: list[str] = []
    cardinality = parent.cardinality()
    if not isinstance(cardinality, Cardinal):
        failures.append(f"cardinality is {type(cardinality).__name__}, not a Cardinal")
        return failures

    # predicates are asserted exactly where the ownership table declares
    # them — the table, not duck probing, decides the audited surface
    def _predicate(name: str, expected: bool) -> None:
        if name in spec.owners and bool(getattr(parent, name)()) is not expected:
            failures.append(f"{name}() is not {expected} under the {spec.classification} classification")

    if spec.classification == "finite":
        if not cardinality.is_finite():
            failures.append("finite classification with an infinite cardinality")
        _predicate("is_finite", True)
        _predicate("is_infinite", False)
        _predicate("is_countable", True)
        _predicate("is_uncountable", False)
        materialized = list(islice(cast(Iterable[Any], parent), int(cardinality.finite_value()) + 1))
        if len(materialized) != cardinality or len(set(materialized)) != len(materialized):
            failures.append(f"materialization ({len(materialized)} elements) disagrees with cardinality {cardinality}")
    elif spec.classification == "countably_infinite":
        if cardinality != aleph0:
            failures.append(f"countably-infinite classification with cardinality {cardinality}")
        _predicate("is_finite", False)
        _predicate("is_infinite", True)
        _predicate("is_countable", True)
        _predicate("is_uncountable", False)
        surface = parent if spec.enumeration_surface == "self" else parent.underlying_set()
        prefix = list(islice(cast(Iterable[Any], surface), 20))
        if len(set(prefix)) != 20:
            failures.append("enumeration prefix is not duplicate-free")
        for element in prefix[:5]:
            if surface[surface.index(element)] != element:
                failures.append(f"index round trip fails on {element!r}")
                break
    elif spec.classification == "uncountable":
        if not cardinality.is_uncountable():
            failures.append(f"uncountable classification with cardinality {cardinality}")
        _predicate("is_finite", False)
        _predicate("is_countable", False)
        _predicate("is_uncountable", True)
    else:
        failures.append(f"unknown classification {spec.classification!r}; fix the inventory row")
    return failures


def audit_parent(spec: MaintainedParent) -> list[str]:
    r"""All checks for one inventory row; empty means green."""
    parent = spec.construct()
    return (
        _audit_route(spec, parent)
        + _audit_provenance(spec, parent)
        + _audit_forgetful_functor(spec, parent)
        + _audit_route_coherence(spec, parent)
        + _audit_refinement(spec, parent)
    )


def report() -> str:
    r"""The on-demand human-readable route report — same introspection,
    printed instead of asserted; ephemeral by construction."""
    lines: list[str] = []
    for spec in maintained_parent_inventory():
        parent = spec.construct()
        lines.append(f"== {spec.label} ==")
        lines.append(f"  constructor : {spec.construct!r}")
        lines.append(f"  category    : {parent.category()}")
        lines.append(f"  axioms      : {sorted(parent.category().axioms())}")
        lines.append("  owned route :")
        for node in derived_route(parent):
            lines.append(f"    - {node}")
        lines.append("  provenance  :")
        for operation, owner in sorted(spec.owners.items()):
            actual = provenance(parent, operation)
            marker = "ok " if actual == owner else "RED"
            lines.append(f"    [{marker}] {operation}: {actual}")
        failures = audit_parent(spec)
        lines.append(f"  audit       : {'green' if not failures else 'RED: ' + '; '.join(failures)}")
        lines.append(f"  refinement  : {spec.classification}, cardinality {parent.cardinality()}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())
