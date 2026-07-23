"""Extract the interface demand this repository places on the generic Lean layer.

The authored sagecats ledger records how each public Sage category reads as a
normalized expression. Everything that reading *names* — a base, a classifier at
a least host reached along a support route, a constructor, a finite-limit cone, a
coherence obligation, an alias, a presentation equivalence — must exist in the
released ``CategoryGraph`` registry before this repository can evaluate the row.

This module turns that ledger into a machine-checkable list of those stable
references, so the receiving repository validates a released registry against an
artifact rather than against prose. It is a *demand*: it records which identifiers
must resolve, never what they mean. Nothing here defines generic mathematics, and
no doctrine question deferred upstream is answered by extracting it.

Extraction fails rather than degrades. A ledger row that names no target, a
classifier occurrence with no host, or a source file whose content hash no longer
matches the recorded one is an error, because a partial demand read as complete
would let the receiving repository report success against requirements this
repository never actually stated.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

from .authored_mapping import AUTHORED_DIR
from .design_sources import DESIGN_ROOT

LEDGER_PATH = AUTHORED_DIR / "sage_normalized_category_mapping_manifest.json"
REQUIREMENTS_PATH = DESIGN_ROOT / "sage" / "authored" / "lean_requirement_manifest.json"

SCHEMA_VERSION = 1

# Requirement kinds. Each names a class of stable reference the released registry
# must resolve; they are not a taxonomy of mathematics.
KIND_CATEGORY = "category"
KIND_CLASSIFIER = "classifier"
KIND_TARGET_EXPRESSION = "target_expression"
KIND_CONSTRUCTOR = "constructor"
KIND_FINITE_LIMIT_CONE = "finite_limit_cone"
KIND_COHERENCE = "coherence"
KIND_ALIAS = "alias"
KIND_PRESENTATION_EQUIVALENCE = "presentation_equivalence"


class StaleExtractionError(RuntimeError):
    """The ledger changed under a recorded hash, or a row could not be read."""


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git_commit(path: Path) -> str:
    """The commit that last touched ``path``, or the tree state if it is dirty.

    A dirty ledger is recorded as such: pinning a clean commit while extracting
    uncommitted content would misattribute the demand to a revision that does not
    contain it.
    """
    root = path.resolve().parent
    head = subprocess.run(
        ["git", "log", "-1", "--format=%H", "--", str(path)],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    dirty = subprocess.run(
        ["git", "status", "--porcelain", "--", str(path)],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    return f"{head}-dirty" if dirty else head


def _requirement(
    kind: str,
    stable_id: str,
    *,
    display: str | None = None,
    demanded_by: str,
    detail: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "kind": kind,
        "stable_id": stable_id,
        "display": display,
        "demanded_by": demanded_by,
        "detail": detail or {},
    }


def _category_mapping_requirements(row: dict[str, Any]) -> list[dict[str, Any]]:
    """Every stable reference one public ledger row needs in order to evaluate."""
    source = row.get("source") or {}
    sage_name = source.get("name")
    if not sage_name:
        raise StaleExtractionError(f"ledger row {row.get('index')} names no Sage source")

    normalized = row.get("normalized") or {}
    kind = str(normalized.get("mapping_kind") or "").lower()
    out: list[dict[str, Any]] = []

    base_id = normalized.get("base_id")
    if base_id:
        out.append(
            _requirement(
                KIND_CATEGORY,
                str(base_id),
                display=normalized.get("base"),
                demanded_by=sage_name,
                detail={"parameter_constraints": normalized.get("parameter_constraints") or None},
            )
        )

    for app in normalized.get("classifier_applications") or []:
        classifier_id = app.get("classifier_id")
        if not classifier_id:
            raise StaleExtractionError(f"{sage_name}: classifier application {app.get('order')} has no stable id")
        least_host = app.get("least_host")
        if not least_host:
            raise StaleExtractionError(f"{sage_name}: classifier {classifier_id} names no least host")
        out.append(
            _requirement(
                KIND_CLASSIFIER,
                str(classifier_id),
                display=app.get("classifier"),
                demanded_by=sage_name,
                detail={
                    # Order matters: classifier applications compose in sequence, so
                    # a registry that has the classifiers but not at these hosts and
                    # routes cannot replay the expression.
                    "order": app.get("order"),
                    "least_host": least_host,
                    "support_route": app.get("support_route"),
                    "semantic_character": app.get("semantic_character"),
                },
            )
        )

    target_id = normalized.get("target_id")
    target_expression = normalized.get("target_expression")
    if not target_expression:
        raise StaleExtractionError(f"{sage_name}: row names no target expression")
    if target_id:
        requirement_kind = KIND_TARGET_EXPRESSION
        if "alias" in kind:
            requirement_kind = KIND_ALIAS
        elif "presentation" in kind or "equivalence" in kind:
            requirement_kind = KIND_PRESENTATION_EQUIVALENCE
        out.append(
            _requirement(
                requirement_kind,
                str(target_id),
                display=target_expression,
                demanded_by=sage_name,
                detail={
                    "mapping_kind": normalized.get("mapping_kind"),
                    "target_visibility": normalized.get("target_visibility"),
                },
            )
        )

    return out


def _unstated_construction_demands(ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """Functorial constructions the ledger demands but has not given a stable id.

    Every crosswalk row that is treated as a genuine functorial construction is a
    real obligation on the released registry, but the ledger records its resolution
    as prose rather than a ``con.*`` identifier. Minting an id here would invent the
    reference this manifest exists to transmit, and dropping the row would report a
    demand of zero constructors against seventeen crosswalk entries. They are carried
    as explicitly unstated demands instead.
    """
    out: list[dict[str, Any]] = []
    for row in ledger.get("sage_functorial_construction_crosswalk") or []:
        name = row.get("sage_construction")
        disposition = str(row.get("normalized_disposition") or "").strip()
        if not name or not disposition:
            raise StaleExtractionError(f"construction crosswalk row {row.get('index')} is incomplete")
        if disposition.lower().startswith(("not a construction", "no normalized", "excluded")):
            continue
        out.append(
            {
                "kind": KIND_CONSTRUCTOR,
                "sage_construction": str(name),
                "sage_flavor": row.get("sage_flavor"),
                "normalized_disposition": disposition,
                "missing": "no stable normalized constructor id in the authored ledger",
            }
        )
    return out


def _cone_and_coherence_requirements(ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """Finite-limit cones and coherence obligations the ledger's rows depend on.

    A row whose base is a named pullback cannot be replayed without that cone, and a
    normalization rule that requires two routes to agree is a coherence obligation on
    the registry, not a comment.
    """
    out: list[dict[str, Any]] = []
    for row in ledger.get("normalized_base_inventory") or []:
        base = row.get("normalized_base")
        rationale = str(row.get("audit_rationale") or "")
        if not base:
            continue
        if "pullback" in rationale.lower() or "×" in rationale:
            out.append(
                _requirement(
                    KIND_FINITE_LIMIT_CONE,
                    f"cat_expr.{_slug_id(str(base))}",
                    display=str(base),
                    demanded_by="normalized_base_inventory",
                    detail={
                        "audit_rationale": rationale,
                        "used_by_rows": row.get("used_by_rows"),
                        "dot_status": row.get("current_dot_status"),
                    },
                )
            )
    for row in ledger.get("audit_exceptions") or []:
        topic = row.get("topic")
        resolution = str(row.get("normalized_resolution") or "")
        finding = str(row.get("finding") or "")
        haystack = f"{resolution} {finding}".lower()
        if topic and ("coheren" in haystack or "commut" in haystack or "route" in haystack):
            out.append(
                _requirement(
                    KIND_COHERENCE,
                    f"coherence.{_slug_id(str(topic))}",
                    display=str(topic),
                    demanded_by="audit_exceptions",
                    detail={"resolution": resolution, "affected_rows": row.get("affected_rows")},
                )
            )
    return out


def _slug_id(text: str) -> str:
    keep = [c.lower() if c.isalnum() else "_" for c in text]
    return "".join(keep).strip("_").replace("__", "_")


def build_requirement_manifest(*, ledger_path: Path | None = None) -> dict[str, Any]:
    """Extract the full interface demand; raise rather than emit a partial one."""
    path = ledger_path or LEDGER_PATH
    if not path.is_file():
        raise StaleExtractionError(f"authored ledger missing: {path}")
    ledger = json.loads(path.read_text(encoding="utf-8"))

    rows = ledger.get("category_mappings") or []
    declared = (ledger.get("validation") or {}).get("public_count")
    if declared is not None and int(declared) != len(rows):
        raise StaleExtractionError(f"ledger declares {declared} public rows but carries {len(rows)}")

    requirements: list[dict[str, Any]] = []
    for row in rows:
        requirements.extend(_category_mapping_requirements(row))
    requirements.extend(_cone_and_coherence_requirements(ledger))
    unstated = _unstated_construction_demands(ledger)

    # One stable id may be demanded by many rows; keep every demand visible so the
    # receiving repository can report which rows a missing id blocks.
    by_id: dict[tuple[str, str], dict[str, Any]] = {}
    for req in requirements:
        key = (req["kind"], req["stable_id"])
        entry = by_id.setdefault(
            key,
            {
                "kind": req["kind"],
                "stable_id": req["stable_id"],
                "display": req["display"],
                "demanded_by": [],
                "occurrences": [],
            },
        )
        if req["demanded_by"] not in entry["demanded_by"]:
            entry["demanded_by"].append(req["demanded_by"])
        if req["detail"] and req["detail"] not in entry["occurrences"]:
            entry["occurrences"].append(req["detail"])

    ordered = sorted(by_id.values(), key=lambda r: (r["kind"], r["stable_id"]))
    covered = {r["source"]["name"] for r in rows if (r.get("source") or {}).get("name")}
    if len(covered) != len(rows):
        raise StaleExtractionError(f"{len(rows)} rows reduced to {len(covered)} distinct Sage sources")

    return {
        "schema_version": SCHEMA_VERSION,
        "title": "Lean CategoryGraph interface demand extracted from the authored Sage ledger",
        "authority": (
            "Interface demand only. This manifest records which stable identifiers a "
            "released registry must resolve for this repository to evaluate its rows. "
            "It is not an authority for generic Lean definitions."
        ),
        "source": {
            "path": str(path.resolve().relative_to(DESIGN_ROOT.parent.resolve())),
            "sha256": _sha256(path),
            "git_commit": _git_commit(path),
            "ledger_schema_version": ledger.get("schema_version"),
            "sage_source_commit": (ledger.get("scope") or {}).get("sage_source_commit"),
        },
        "coverage": {
            "public_rows": len(rows),
            "distinct_sage_sources": len(covered),
            "requirements": len(ordered),
            "unstated_demands": len(unstated),
            "by_kind": {kind: sum(1 for r in ordered if r["kind"] == kind) for kind in sorted({r["kind"] for r in ordered})},
        },
        "requirements": ordered,
        # Obligations the ledger states in prose only. The receiving repository cannot
        # validate these by identifier; they are listed so a release is never reported
        # as satisfying a demand this repository never managed to state.
        "unstated_demands": unstated,
    }


def check_requirement_manifest(*, path: Path | None = None) -> list[str]:
    """Findings that make the committed manifest unusable as a demand.

    A stale manifest is worse than none: the receiving repository would validate a
    release against requirements this ledger no longer states.
    """
    target = path or REQUIREMENTS_PATH
    if not target.is_file():
        return [f"requirement manifest missing: {target}"]
    committed = json.loads(target.read_text(encoding="utf-8"))
    findings: list[str] = []

    recorded_hash = (committed.get("source") or {}).get("sha256")
    live_hash = _sha256(LEDGER_PATH)
    if recorded_hash != live_hash:
        findings.append(f"recorded ledger sha256 {recorded_hash} does not match live ledger {live_hash}")

    fresh = build_requirement_manifest()
    if fresh["requirements"] != committed.get("requirements"):
        findings.append("committed requirements differ from a fresh extraction of the live ledger")
    if fresh["coverage"]["public_rows"] != (committed.get("coverage") or {}).get("public_rows"):
        findings.append("committed row coverage does not match the live ledger")
    return findings


def write_requirement_manifest(path: Path | None = None) -> Path:
    target = path or REQUIREMENTS_PATH
    payload = build_requirement_manifest()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return target


def main() -> int:
    out = write_requirement_manifest()
    payload = json.loads(out.read_text(encoding="utf-8"))
    cov = payload["coverage"]
    print(f"wrote {out.relative_to(DESIGN_ROOT.parent)}")
    print(f"  public rows:  {cov['public_rows']}")
    print(f"  requirements: {cov['requirements']}")
    for kind, count in sorted(cov["by_kind"].items()):
        print(f"    {kind}: {count}")
    print(f"  ledger sha256: {payload['source']['sha256']}")
    print(f"  ledger commit: {payload['source']['git_commit']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
