"""Load and validate the three related manifests (+ optional routes)."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .design_sources import DESIGN_ROOT, SEMANTIC_SEED_DIR, load_json
from .semantic_seed import load_semantic_seed

OBSERVED_PATH = DESIGN_ROOT / "sage" / "observed.json"
MAPPING_PATH = DESIGN_ROOT / "sage" / "mapping.yaml"
ROUTES_PATH = DESIGN_ROOT / "routes" / "routes.yaml"
NORMALIZED_MANIFEST = DESIGN_ROOT / "normalized" / "manifest"

CATEGORY_RELATIONS = frozenset(
    {
        "exact",
        "presentation_alias",
        "canonical_equivalence",
        "corrected_embedding",
        "constructible",
        "unsupported",
        "removed",
    }
)
AXIOM_DISPOSITIONS = frozenset(
    {
        "exact",
        "rehosted",
        "unsupported",
        # Settled rulings from the authored crosswalk, not pending work.
        "excluded_test_only",
        "excluded_engineering",
        "construction_owned",
        "split_by_host",
    }
)

HYGIENE_KINDS = frozenset(
    {
        "bad_axiom_disposition",
        "dangling_target",
        "target_collision",
        "duplicate_source",
        "bad_relation",
        "source_id_mismatch",
    }
)
PARITY_KINDS = frozenset(
    {
        "unsupported_mapping",
        "unsupported_axiom",
        "unsupported_construction",
    }
)


@dataclass(frozen=True, slots=True)
class ManifestFinding:
    kind: str
    subject: str
    detail: str


def load_observed(path: Path | None = None) -> dict[str, Any]:
    data = load_json(path or OBSERVED_PATH)
    assert isinstance(data, dict)
    return data


def load_mapping(path: Path | None = None) -> dict[str, Any]:
    data = yaml.safe_load((path or MAPPING_PATH).read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def load_routes(path: Path | None = None) -> dict[str, Any]:
    path_ = path or ROUTES_PATH
    if not path_.is_file():
        return {"manifest": {}, "routes": []}
    data = yaml.safe_load(path_.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def validate_three_manifests(
    *,
    observed: dict[str, Any] | None = None,
    mapping: dict[str, Any] | None = None,
    seed: Any | None = None,
    require_full_parity: bool = False,
) -> list[ManifestFinding]:
    """Bijection, relation, axiom and construction checks.

    Hygiene findings always returned. Parity findings (``unsupported_*``)
    are included when ``require_full_parity`` is true — they must fail a
    release that claims full Sage parity.
    """
    observed = observed or load_observed()
    mapping = mapping or load_mapping()
    seed = seed or load_semantic_seed()
    findings: list[ManifestFinding] = []

    obs_ids = {c["id"] for c in observed.get("categories", [])}
    seed_ids = set(seed.entity_by_id())

    targets_by_source: dict[str, str | None] = {}
    non_alias_targets: dict[str, list[str]] = {}
    for row in mapping.get("category_mappings", []):
        rel = row.get("relation")
        if rel not in CATEGORY_RELATIONS:
            findings.append(ManifestFinding("bad_relation", row.get("source", "?"), f"{rel!r}"))
        source = row["source"]
        target = row.get("target")
        if source in targets_by_source:
            findings.append(
                ManifestFinding(
                    "duplicate_source",
                    source,
                    f"already → {targets_by_source[source]}",
                )
            )
        targets_by_source[source] = target
        if target and target not in seed_ids:
            findings.append(ManifestFinding("dangling_target", source, f"target {target} missing"))
        if rel == "unsupported":
            findings.append(
                ManifestFinding(
                    "unsupported_mapping",
                    source,
                    "blocks full Sage parity claim",
                )
            )
        if (
            rel
            not in {
                "presentation_alias",
                "removed",
                "unsupported",
                "constructible",
            }
            and target
        ):
            non_alias_targets.setdefault(target, []).append(source)

    for target, sources in non_alias_targets.items():
        if len(sources) > 1:
            findings.append(
                ManifestFinding(
                    "target_collision",
                    target,
                    f"non-alias sources {sources}",
                )
            )

    for row in mapping.get("axiom_mappings", []):
        disp = row.get("disposition")
        if disp not in AXIOM_DISPOSITIONS:
            findings.append(ManifestFinding("bad_axiom_disposition", row.get("source", "?"), f"{disp!r}"))
        # A decided exclusion, a construction-owned axiom, and a token the ledger
        # deliberately refused to globalize are all settled: absence of a classifier
        # is the ruling, not a missing capability. Only a row owed a classifier the
        # seed cannot supply is a parity gap.
        if disp == "unsupported":
            findings.append(
                ManifestFinding(
                    "unsupported_axiom",
                    row.get("source", "?"),
                    "normalized classifier pending",
                )
            )

    for row in mapping.get("construction_mappings", []):
        if row.get("relation") == "unsupported" or row.get("target") is None:
            findings.append(
                ManifestFinding(
                    "unsupported_construction",
                    row.get("source", "?"),
                    "normalized construction pending",
                )
            )

    for row in mapping.get("category_mappings", []):
        src = row["source"]
        if src.startswith("sage.category.") and obs_ids and src not in obs_ids:
            sage_name = row.get("source_sage_name")
            if sage_name and any(c.get("qualname") == sage_name for c in observed["categories"]):
                findings.append(
                    ManifestFinding(
                        "source_id_mismatch",
                        src,
                        f"qualname {sage_name} exists under a different observed id",
                    )
                )

    if not require_full_parity:
        findings = [f for f in findings if f.kind not in PARITY_KINDS]
    return findings


def format_manifests_report(*, require_full_parity: bool = False) -> str:
    observed = load_observed()
    mapping = load_mapping()
    seed = load_semantic_seed()
    findings = validate_three_manifests(
        observed=observed,
        mapping=mapping,
        seed=seed,
        require_full_parity=require_full_parity,
    )
    all_findings = validate_three_manifests(
        observed=observed,
        mapping=mapping,
        seed=seed,
        require_full_parity=True,
    )
    n_imm = sum(len(c.get("immediate_supercategories") or []) for c in observed.get("categories", []))
    rels = Counter(r.get("relation") for r in mapping.get("category_mappings", []))
    lines = [
        "Three-manifest report (observed + normalized + correspondence)",
        f"  observed categories: {len(observed.get('categories', []))}",
        f"  observed axioms:     {len(observed.get('axioms', []))}",
        f"  observed constructions: {len(observed.get('constructions', []))}",
        f"  immediate edges:     {n_imm}",
        f"  normalized entities: {len(seed.entities)}",
        f"  category mappings:   {len(mapping.get('category_mappings', []))}",
        f"  axiom mappings:      {len(mapping.get('axiom_mappings', []))}",
        f"  construction maps:   {len(mapping.get('construction_mappings', []))}",
        f"  hygiene findings:    {len(findings)}",
        f"  parity findings:     {len(all_findings)}",
    ]
    if findings:
        lines.append("Hygiene finding counts:")
        for kind, n in sorted(Counter(f.kind for f in findings).items()):
            lines.append(f"  {kind}: {n}")
        for f in findings[:20]:
            lines.append(f"  - {f.kind}: {f.subject}: {f.detail}")
    else:
        lines.append("Mapping hygiene: no blocking findings")
    lines.append("Category mapping relations:")
    for rel, n in sorted(rels.items(), key=lambda x: (-x[1], x[0] or "")):
        lines.append(f"  {rel}: {n}")
    return "\n".join(lines)


def assert_manifest_files_present() -> None:
    missing = [p for p in (OBSERVED_PATH, MAPPING_PATH, NORMALIZED_MANIFEST, SEMANTIC_SEED_DIR) if not p.exists()]
    if missing:
        raise FileNotFoundError(f"manifest files missing: {missing}")


def main() -> int:
    assert_manifest_files_present()
    print(format_manifests_report())
    return 0 if not validate_three_manifests() else 1


if __name__ == "__main__":
    raise SystemExit(main())
