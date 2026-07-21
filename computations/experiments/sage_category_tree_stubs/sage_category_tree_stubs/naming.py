r"""Three-layer naming model for \(\mathcal G\) (not Sage inventory).

Layers that must not be conflated:

1. **Identity** — the mathematical category (one object of \(\mathcal G\)).
2. **Standard name** — established noun / conventional notation, when one exists
   (``Groups``, ``AbelianGroups``, ``Modules(R)``, …).
3. **Classifier / definition expression** — how it is constructed
   (``Magmas.Associative.Unital.Inverse``, ``Groups.Commutative``,
   ``Algebras(R) ×_Sets Sets.Graded``, …).

Named-join DOT vertices ``Name = Classifier`` package layers 2 and 3 for one
identity. Sage aliases are metadata on an identity, never extra vertices.

This module *reports*; mass renames are downstream of a failing naming audit.
"""

from __future__ import annotations

import json
from collections.abc import Iterable
from dataclasses import asdict, dataclass, field

from .dot_parse import DotGraph, parse_dot
from .slugs import short_name

#══════════════════════════════════════════════════════════════════════════════
# Layer model
#══════════════════════════════════════════════════════════════════════════════


@dataclass(frozen=True, slots=True)
class CategoryIdentity:
    """One mathematical category with optional standard name and definition.

    ``classifier`` is the preferred constructive presentation (layer 3).
    ``sage_aliases`` are source spellings that are *not* distinct identities.
    """

    # Stable id used in reports (usually the standard name, else classifier).
    identity_id: str
    standard_name: str | None
    classifier: str
    sage_aliases: tuple[str, ...] = ()
    notes: str = ""


# Seed ledger: definitional presentations from the naming doctrine.
# Expand as audits land; do not invent species here.
CANONICAL_IDENTITIES: tuple[CategoryIdentity, ...] = (
    CategoryIdentity("Sets", "Sets", "Sets"),
    CategoryIdentity("Magmas", "Magmas", "Magmas"),
    CategoryIdentity(
        "Semigroups",
        "Semigroups",
        "Magmas.Associative",
    ),
    CategoryIdentity(
        "Monoids",
        "Monoids",
        "Magmas.Associative.Unital",
    ),
    CategoryIdentity(
        "Groups",
        "Groups",
        "Magmas.Associative.Unital.Inverse",
    ),
    CategoryIdentity(
        "AbelianGroups",
        "AbelianGroups",
        "Groups.Commutative",
        sage_aliases=("CommutativeAdditiveGroups",),
        notes="Prefer Groups.Commutative over fully expanded Magmas path",
    ),
    CategoryIdentity(
        "Rings",
        "Rings",
        "Rings",
    ),
    CategoryIdentity(
        "CommutativeRings",
        "CommutativeRings",
        "Rings.Commutative",
        notes="DOT may use CommRings as the standard-name spelling",
    ),
    CategoryIdentity(
        "IntegralDomains",
        "IntegralDomains",
        "CommutativeRings.Domain",
    ),
    CategoryIdentity(
        "PIDs",
        "PIDs",
        "IntegralDomains.PrincipalIdeal",
        notes="DOT may spell the classifier via Rings.Commutative.PID",
    ),
    CategoryIdentity(
        "FiniteFields",
        "FiniteFields",
        "Fields.Finite",
        notes="Pullback of Sets.Finite along Fields → Sets; not equal to Sets.Finite",
    ),
    CategoryIdentity(
        "FiniteRings",
        "FiniteRings",
        "Rings.Finite",
        notes="Pullback of Sets.Finite; not equal to Sets.Finite",
    ),
    CategoryIdentity(
        "Modules(R)",
        "Modules(R)",
        "Modules(R)",
    ),
    CategoryIdentity(
        "Algebras(R)",
        "Algebras(R)",
        "Algebras(R)",
        sage_aliases=("MagmaticAlgebras",),
        notes="Sage MagmaticAlgebras is transitional for this identity",
    ),
    CategoryIdentity(
        "Algebras(R).Graded",
        None,
        "Algebras(R).Graded",
        sage_aliases=("GradedAlgebras",),
        notes="Pullback Algebras(R)×_Sets Sets.Graded; GradedAlgebras is alias, not primitive",
    ),
    CategoryIdentity(
        "Surfaces(K)",
        "Surfaces(K)",
        "Schemes(K).RelativeDimension(2)",
    ),
    CategoryIdentity(
        "Curves(K)",
        "Curves(K)",
        "Schemes(K).RelativeDimension(1)",
    ),
)


@dataclass(frozen=True, slots=True)
class NamedPresentation:
    """A DOT ``standard_name = classifier`` vertex (layers 2+3 for one identity)."""

    vertex: str
    standard_name: str
    classifier: str
    host: str
    axioms: tuple[str, ...]


def parse_named_presentation(vertex: str) -> NamedPresentation | None:
    if " = " not in vertex:
        return None
    name, classifier = vertex.split(" = ", 1)
    parts = classifier.split(".")
    if len(parts) < 2:
        return None
    return NamedPresentation(
        vertex=vertex,
        standard_name=name,
        classifier=classifier,
        host=parts[0],
        axioms=tuple(parts[1:]),
    )


def presentations_from_graph(graph: DotGraph | None = None) -> tuple[NamedPresentation, ...]:
    graph = graph or parse_dot()
    out: list[NamedPresentation] = []
    seen: set[str] = set()
    for vertex in sorted(graph.named_joins):
        pres = parse_named_presentation(vertex)
        if pres is None or vertex in seen:
            continue
        seen.add(vertex)
        out.append(pres)
    return tuple(out)


def identity_by_standard_name() -> dict[str, CategoryIdentity]:
    return {
        ident.standard_name: ident
        for ident in CANONICAL_IDENTITIES
        if ident.standard_name is not None
    }


def identity_by_sage_alias() -> dict[str, CategoryIdentity]:
    out: dict[str, CategoryIdentity] = {}
    for ident in CANONICAL_IDENTITIES:
        for alias in ident.sage_aliases:
            out[alias] = ident
    return out


#══════════════════════════════════════════════════════════════════════════════
# Audits
#══════════════════════════════════════════════════════════════════════════════


@dataclass(frozen=True, slots=True)
class NamingFinding:
    kind: str
    subject: str
    detail: str
    expected: str | None = None
    observed: str | None = None


# Host of a named presentation must be the category the standard name refines,
# not the least host of a *transported* classifier (Sets for Finite*, etc.).
_FORBIDDEN_EQUATION_HOSTS: dict[str, str] = {
    # standard_name → required host of the definition expression
    "FiniteRings": "Rings",
    "FiniteFields": "Fields",
    "FiniteGroups": "Groups",
    "GradedAlgebras": "Algebras(R)",
    "GradedModules": "Modules(R)",
}


# Independent Sage-style species names that should only appear as aliases /
# standard names of pullbacks, never as primitive solid nodes.
_FORBIDDEN_PRIMITIVE_SPECIES: frozenset[str] = frozenset(
    {
        "GradedAlgebras",
        "GradedModules",
        "FiniteGroups",
        "FiniteRings",
        "FiniteFields",
        "SmoothVarieties",
        "ProperSurfaces",
        "GroupFinite",
        "RingFinite",
        "AlgebraFinite",
    }
)


# Chosen-structure classifiers: surface form is OK only if read as chosen data.
_CHOSEN_STRUCTURE_CLASSIFIERS: frozenset[str] = frozenset(
    {
        "WithBasis",
        "WithGenerators",
        "Graded",
    }
)


def audit_definition_hosts(graph: DotGraph | None = None) -> list[NamingFinding]:
    """Named joins whose RHS host is not the category being named (pullback abuse)."""
    findings: list[NamingFinding] = []
    for pres in presentations_from_graph(graph):
        required = _FORBIDDEN_EQUATION_HOSTS.get(pres.standard_name)
        if required is None:
            continue
        if short_name(pres.host) != required and pres.host != required:
            findings.append(
                NamingFinding(
                    kind="wrong_definition_host",
                    subject=pres.vertex,
                    detail=(
                        f"{pres.standard_name} must be defined as a transport/pullback "
                        f"on {required} (e.g. {required}.{pres.axioms[-1] if pres.axioms else 'A'}), "
                        f"not equated to a classifier on {pres.host}"
                    ),
                    expected=f"{pres.standard_name} = {required}."
                    + (".".join(pres.axioms) if pres.axioms else "A"),
                    observed=pres.classifier,
                )
            )
    return findings


def audit_canonical_presentations(graph: DotGraph | None = None) -> list[NamingFinding]:
    """Where the ledger prefers a shorter classifier than the DOT expands."""
    by_name = {p.standard_name: p for p in presentations_from_graph(graph)}
    findings: list[NamingFinding] = []
    for ident in CANONICAL_IDENTITIES:
        if ident.standard_name is None:
            continue
        # Accept CommRings as spelling of CommutativeRings
        candidates = [ident.standard_name]
        if ident.standard_name == "CommutativeRings":
            candidates.append("CommRings")
        observed = None
        for name in candidates:
            if name in by_name:
                observed = by_name[name]
                break
        if observed is None:
            # Finite* may be present under wrong host; still reported elsewhere
            if ident.standard_name in _FORBIDDEN_EQUATION_HOSTS:
                continue
            # Primitives (classifier == name) need only a solid vertex, not a join
            if ident.classifier == ident.standard_name:
                continue
            findings.append(
                NamingFinding(
                    kind="missing_standard_name",
                    subject=ident.identity_id,
                    detail="Ledger identity has no DOT named-join presentation",
                    expected=f"{ident.standard_name} = {ident.classifier}",
                )
            )
            continue
        # Preferred classifier need not equal full Magmas expansion; flag only
        # when the ledger classifier is a *prefix rename* the DOT missed.
        if ident.classifier == "Groups.Commutative" and observed.classifier != ident.classifier:
            if not observed.classifier.endswith(".Commutative"):
                findings.append(
                    NamingFinding(
                        kind="noncanonical_classifier",
                        subject=observed.vertex,
                        detail=ident.notes or "Prefer ledger classifier presentation",
                        expected=ident.classifier,
                        observed=observed.classifier,
                    )
                )
            else:
                findings.append(
                    NamingFinding(
                        kind="expanded_classifier",
                        subject=observed.vertex,
                        detail=(
                            "Definitionally ok; preferred public presentation is "
                            f"{ident.classifier}"
                        ),
                        expected=ident.classifier,
                        observed=observed.classifier,
                    )
                )
    return findings


def audit_forbidden_primitives(graph: DotGraph | None = None) -> list[NamingFinding]:
    """Species names that must not appear as bare solid nodes (no ``=``)."""
    graph = graph or parse_dot()
    findings: list[NamingFinding] = []
    for node in sorted(graph.solid_nodes):
        name = short_name(node)
        if " = " in node:
            # Named join: ok as standard name *if* definition host is correct
            continue
        if name in _FORBIDDEN_PRIMITIVE_SPECIES:
            findings.append(
                NamingFinding(
                    kind="forbidden_primitive_species",
                    subject=node,
                    detail=(
                        f"{name} must be a standard name / alias of a pullback, "
                        "not an independently declared solid species"
                    ),
                    expected=f"named join or alias → {_FORBIDDEN_EQUATION_HOSTS.get(name, 'Host.A')}",
                )
            )
    return findings


def audit_duplicate_classifiers(graph: DotGraph | None = None) -> list[NamingFinding]:
    """Two distinct standard names must not claim identical classifier strings
    unless one is an intentional synonym (tracked later).
    """
    by_clf: dict[str, list[NamedPresentation]] = {}
    for pres in presentations_from_graph(graph):
        by_clf.setdefault(pres.classifier, []).append(pres)
    findings: list[NamingFinding] = []
    for clf, rows in sorted(by_clf.items()):
        names = sorted({r.standard_name for r in rows})
        if len(names) <= 1:
            continue
        # FiniteRings and FiniteFields both wrongly = Sets.Finite is a finding
        findings.append(
            NamingFinding(
                kind="shared_classifier_collision",
                subject=clf,
                detail=f"Distinct standard names share one classifier: {', '.join(names)}",
                observed=", ".join(r.vertex for r in rows),
            )
        )
    return findings


def audit_chosen_structure_labels(graph: DotGraph | None = None) -> list[NamingFinding]:
    """Informational: classifiers that denote chosen structure, not Boolean axioms."""
    graph = graph or parse_dot()
    findings: list[NamingFinding] = []
    for node_id, label in sorted(graph.axiom_labels.items()):
        bare = label.split("(", 1)[0]
        if bare not in _CHOSEN_STRUCTURE_CLASSIFIERS:
            continue
        findings.append(
            NamingFinding(
                kind="chosen_structure_classifier",
                subject=node_id,
                detail=(
                    f"Classifier {label!r} denotes chosen structure/stuff "
                    "(forgetful generally not full); not a Boolean property axiom"
                ),
                observed=label,
            )
        )
    return findings


@dataclass(frozen=True, slots=True)
class NamingReport:
    presentations: tuple[NamedPresentation, ...]
    findings: tuple[NamingFinding, ...]
    by_kind: dict[str, int] = field(default_factory=dict)

    @property
    def blocking_ok(self) -> bool:
        """True when no definition-host / collision / forbidden-primitive findings."""
        blocking = {
            "wrong_definition_host",
            "shared_classifier_collision",
            "forbidden_primitive_species",
            "missing_standard_name",
        }
        return not any(f.kind in blocking for f in self.findings)

    def to_dict(self) -> dict[str, object]:
        return {
            "presentation_count": len(self.presentations),
            "blocking_ok": self.blocking_ok,
            "by_kind": self.by_kind,
            "findings": [asdict(f) for f in self.findings],
            "presentations": [asdict(p) for p in self.presentations],
            "canonical_identities": [asdict(i) for i in CANONICAL_IDENTITIES],
        }


def naming_report(graph: DotGraph | None = None) -> NamingReport:
    graph = graph or parse_dot()
    findings = (
        audit_definition_hosts(graph)
        + audit_duplicate_classifiers(graph)
        + audit_forbidden_primitives(graph)
        + audit_canonical_presentations(graph)
        + audit_chosen_structure_labels(graph)
    )
    by_kind: dict[str, int] = {}
    for f in findings:
        by_kind[f.kind] = by_kind.get(f.kind, 0) + 1
    return NamingReport(
        presentations=presentations_from_graph(graph),
        findings=tuple(findings),
        by_kind=by_kind,
    )


def format_naming_report(report: NamingReport) -> str:
    lines = [
        "𝒢 naming report (identity ≠ standard name ≠ classifier)",
        f"  named presentations: {len(report.presentations)}",
        f"  blocking_ok:         {report.blocking_ok}",
        "",
        "Finding counts:",
    ]
    for kind, n in sorted(report.by_kind.items()):
        lines.append(f"  {kind}: {n}")
    blocking = [
        f
        for f in report.findings
        if f.kind
        in {
            "wrong_definition_host",
            "shared_classifier_collision",
            "forbidden_primitive_species",
            "missing_standard_name",
        }
    ]
    if blocking:
        lines.append("")
        lines.append("BLOCKING:")
        for f in blocking:
            lines.append(f"  [{f.kind}] {f.subject}")
            lines.append(f"    {f.detail}")
            if f.expected:
                lines.append(f"    expected: {f.expected}")
            if f.observed:
                lines.append(f"    observed: {f.observed}")
    advisory = [f for f in report.findings if f not in blocking]
    if advisory:
        lines.append("")
        lines.append("Advisory:")
        for f in advisory:
            lines.append(f"  [{f.kind}] {f.subject}: {f.detail}")
    return "\n".join(lines)


def _cli(argv: Iterable[str] | None = None) -> int:
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help", "help"}:
        print(__doc__)
        print("commands: report | json | presentations | ledger")
        return 0
    cmd = args[0]
    if cmd == "ledger":
        for ident in CANONICAL_IDENTITIES:
            aliases = ",".join(ident.sage_aliases) if ident.sage_aliases else "-"
            print(
                f"{ident.identity_id}\tname={ident.standard_name}\t"
                f"clf={ident.classifier}\tsage_aliases={aliases}"
            )
        return 0
    if cmd == "presentations":
        for p in presentations_from_graph():
            print(f"{p.standard_name}\t{p.classifier}\t{p.vertex}")
        return 0
    if cmd == "report":
        print(format_naming_report(naming_report()))
        return 0
    if cmd == "json":
        print(json.dumps(naming_report().to_dict(), indent=2, sort_keys=True))
        return 0
    print(f"unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(_cli())
