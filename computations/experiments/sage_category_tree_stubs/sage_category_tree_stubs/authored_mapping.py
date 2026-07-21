"""Load the authored sagecats mapping ledger and evaluate constructibility.

The ledger is the correspondence SSOT: each public Sage category is a
normalized base plus ordered classifier applications (with optional support
routes). The finite-limit checker derives certificates; it does not invent
mappings from Sage names.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .constructibility import (
    ClassifierRequest,
    Constructibility,
    ConstructibilityResult,
    build_sketch,
    check_requests,
    constructibility_record,
)
from .design_sources import DESIGN_ROOT, load_json

AUTHORED_DIR = DESIGN_ROOT / "sage" / "authored"
AUTHORED_MANIFEST = AUTHORED_DIR / "sage_normalized_category_mapping_manifest.json"


def load_authored_manifest(path: Path | None = None) -> dict[str, Any]:
    data = load_json(path or AUTHORED_MANIFEST)
    assert isinstance(data, dict)
    return data


def support_route_to_along(route: str | None) -> str | None:
    """Map ledger support_route strings to checker semantic roles.

    ``operation_role:additive`` excludes the multiplicative Magmas port when
    several routes exist (Additive presentation). ``operation_port:*`` selects
    a concrete multi-port forgetful.
    """
    if not route:
        return None
    text = route.lower().replace("-", "_")
    if text.startswith("operation_role:additive"):
        return "additive_presentation"
    if text.startswith("operation_role:"):
        return None
    if "underlying_set" in text:
        return "underlying_set"
    if "underlying_module" in text:
        return None
    if "multiplicative" in text or "ring_multiplication" in text:
        return "multiplicative_operation"
    if "algebra_multiplication" in text:
        return "multiplicative_operation"
    if text.startswith("operation_port:") and "additive" in text:
        return "additive_operation"
    return None


def _seed_has_entity(entity_id: str, sketch: dict[str, Any]) -> bool:
    if entity_id in sketch["nodes"]:
        return True
    seed = sketch["seed"]
    return any(e["id"] == entity_id for e in seed.entities)


def resolve_classifier_id(
    *,
    classifier_id: str | None,
    classifier_name: str | None,
    least_host: str | None,
    sketch: dict[str, Any],
    prefer_host: str | None = None,
) -> str | None:
    """Resolve authored classifier id against the seed (id, then name+host)."""
    classifiers = sketch["classifiers"]
    # Prefer mature Magmas.Additive over a bare authored clf.additive id.
    if classifier_id == "clf.additive" and "clf.magmas.additive" in classifiers:
        return "clf.magmas.additive"
    if classifier_id == "clf.commutative" and "clf.magmas.commutative" in classifiers:
        return "clf.magmas.commutative"
    if classifier_id and classifier_id in classifiers:
        return classifier_id
    # Host-specific finitely generated minted for Magmas/Semigroups
    if classifier_id == "clf.finitelygenerated" and prefer_host:
        for cand in (
            f"clf.{prefer_host.removeprefix('cat.')}.finitelygenerated",
            "clf.magmas.finitelygenerated",
            "clf.semigroups.finitelygenerated",
        ):
            if cand in classifiers and (prefer_host is None or classifiers[cand].host == prefer_host):
                return cand
        for c in classifiers.values():
            if c.name == "FinitelyGenerated" and c.host == prefer_host:
                cid = c.id
                assert isinstance(cid, str)
                return cid
    aliases = {
        "clf.withbasis": "WithBasis",
        "clf.finiterank": "FiniteRank",
        "clf.finite": "Finite",
        "clf.commutative": "Commutative",
        "clf.associative": "Associative",
        "clf.unital": "Unital",
        "clf.inverse": "Inverse",
        "clf.additive": "Additive",
        "clf.graded": "Graded",
        "clf.finitelygenerated": "FinitelyGenerated",
        "clf.enumerated": "Enumerated",
        "clf.filtered": "Filtered",
        "clf.super": "Super",
    }
    name = classifier_name or aliases.get(classifier_id or "")
    if not name:
        return None
    cands = [c for c in classifiers.values() if c.name == name]
    if not cands:
        return None

    sig_specific = (least_host or "").lower().startswith("signature-specific")

    def host_rank(c: Any) -> int:
        if prefer_host and c.host == prefer_host:
            return -1
        if sig_specific and prefer_host and c.host == prefer_host:
            return -1
        if not least_host or sig_specific:
            return 1
        host_base = least_host.split("(", 1)[0].strip()
        expected = f"cat.{host_base.lower().replace(' ', '_')}"
        if c.host == expected:
            return 0
        if c.host.endswith(f".{host_base.lower()}") or c.host == host_base:
            return 1
        return 2

    ranked = sorted(
        cands,
        key=lambda c: (
            host_rank(c),
            0 if "modules" in c.id and name in {"WithBasis", "FiniteRank"} else 1,
            1 if c.id.startswith("clf.ax_") else 0,
            1 if "additive" in c.id and least_host == "Magmas" else 0,
            0 if c.id.startswith("clf.magmas.") and least_host == "Magmas" else 1,
            c.id,
        ),
    )
    return ranked[0].id if isinstance(ranked[0].id, str) else str(ranked[0].id)


@dataclass(frozen=True, slots=True)
class AuthoredRequest:
    sage_name: str
    sage_symbol: str | None
    base_id: str | None
    base_display: str | None
    requests: tuple[ClassifierRequest, ...]
    target_expression: str
    target_id: str | None
    mapping_kind: str | None
    missing_base: bool
    missing_classifiers: tuple[str, ...]
    confidence: str | None
    review_status: str | None
    parameter_constraints: str | None
    raw: dict[str, Any]


def _entity_id_set(sketch: dict[str, Any]) -> set[str]:
    ids = set(sketch["nodes"])
    for e in sketch["seed"].entities:
        ids.add(e["id"])
    return ids


def authored_row_to_request(
    row: dict[str, Any],
    *,
    sketch: dict[str, Any] | None = None,
) -> AuthoredRequest:
    from .seed_authored_sync import resolve_base_id

    sketch = sketch or build_sketch()
    source = row.get("source") or {}
    normalized = row.get("normalized") or {}
    audit = row.get("audit") or {}
    raw_base = normalized.get("base_id")
    base_display = normalized.get("base")
    entity_ids = _entity_id_set(sketch)
    base_id: str | None = None
    if raw_base:
        base_id = resolve_base_id(str(raw_base), entity_ids) or (str(raw_base) if str(raw_base) in entity_ids else None)
        if base_id is None and str(raw_base) in entity_ids:
            base_id = str(raw_base)
        if base_id is None:
            # Opaque id present after sync even if not in nodes set
            base_id = str(raw_base) if _seed_has_entity(str(raw_base), sketch) else None
    missing_base = base_id is None
    missing: list[str] = []
    reqs: list[ClassifierRequest] = []
    for app in normalized.get("classifier_applications") or []:
        cid = resolve_classifier_id(
            classifier_id=app.get("classifier_id"),
            classifier_name=app.get("classifier"),
            least_host=app.get("least_host"),
            sketch=sketch,
            prefer_host=base_id,
        )
        label = app.get("classifier_id") or app.get("classifier") or "?"
        if cid is None:
            missing.append(str(label))
            continue
        along = support_route_to_along(app.get("support_route"))
        occ = f"{cid}#{app.get('order', len(reqs))}"
        reqs.append(ClassifierRequest(cid, along=along, occurrence_id=occ))
    return AuthoredRequest(
        sage_name=str(source.get("name") or ""),
        sage_symbol=source.get("symbol"),
        base_id=base_id,
        base_display=str(base_display) if base_display else None,
        requests=tuple(reqs),
        target_expression=str(normalized.get("target_expression") or ""),
        target_id=normalized.get("target_id"),
        mapping_kind=normalized.get("mapping_kind"),
        missing_base=missing_base,
        missing_classifiers=tuple(missing),
        confidence=(audit.get("confidence") if audit else None),
        review_status=(audit.get("review_status") if audit else None),
        parameter_constraints=normalized.get("parameter_constraints"),
        raw=row,
    )


def evaluate_authored_request(
    req: AuthoredRequest,
    *,
    sketch: dict[str, Any] | None = None,
) -> ConstructibilityResult:
    """Run the finite-limit checker on one authored row."""
    sketch = sketch or build_sketch()
    if req.missing_base:
        return ConstructibilityResult(
            status="MISSING_SEED",
            base_id=req.base_id,
            certificate={},
            remaining=tuple(r.occurrence_id or r.classifier_id for r in req.requests),
            reachable=(),
            detail=f"missing seed base {req.base_id or req.base_display}",
            expression=req.target_expression,
        )
    if req.missing_classifiers:
        return ConstructibilityResult(
            status="MISSING_SEED",
            base_id=req.base_id,
            certificate={},
            remaining=req.missing_classifiers,
            reachable=(),
            detail="missing seed classifiers: " + ", ".join(req.missing_classifiers),
            expression=req.target_expression,
        )
    assert req.base_id is not None
    if not req.requests:
        # Base-only: exact named entity when present in seed.
        return ConstructibilityResult(
            status="EXACT_BASE",
            base_id=req.base_id,
            certificate={},
            remaining=(),
            reachable=(req.base_id,),
            detail="base-only mapping; named seed entity",
            expression=req.target_expression,
        )
    result = check_requests(req.base_id, req.requests, sketch=sketch)
    return ConstructibilityResult(
        status=result.status,
        base_id=result.base_id,
        certificate=result.certificate,
        remaining=result.remaining,
        reachable=result.reachable,
        detail=result.detail,
        expression=req.target_expression or result.expression,
    )


def authored_constructibility_record(
    req: AuthoredRequest,
    result: ConstructibilityResult,
) -> dict[str, Any]:
    """Certificate dict for mapping.yaml construction field."""
    if result.status == "EXACT_BASE":
        return {
            "kind": "finite_limit_constructibility",
            "ok": True,
            "status": "EXACT_BASE",
            "base": result.base_id,
            "classifiers": [],
            "expression": result.expression,
            "detail": result.detail,
            "certificate": [],
        }
    # Reuse Constructibility summary shape for CONSTRUCTIBLE / failures
    summary = Constructibility(
        ok=result.ok,
        base_id=result.base_id,
        classifier_ids=tuple(r.classifier_id for r in req.requests),
        expression=result.expression,
        detail=f"{result.status}: {result.detail}" if not result.ok else result.detail,
        host_paths=tuple((k, v.target) for k, v in result.certificate.items()),
    )
    rec = constructibility_record(summary)
    rec["status"] = result.status
    if result.status == "MISSING_SEED":
        rec["ok"] = False
        rec["missing"] = list(result.remaining)
    return rec


def iter_public_authored_requests(
    manifest: dict[str, Any] | None = None,
    *,
    sketch: dict[str, Any] | None = None,
) -> list[AuthoredRequest]:
    manifest = manifest or load_authored_manifest()
    sketch = sketch or build_sketch()
    return [authored_row_to_request(row, sketch=sketch) for row in manifest.get("category_mappings", [])]


def evaluate_all_public(
    manifest: dict[str, Any] | None = None,
    *,
    sketch: dict[str, Any] | None = None,
) -> list[tuple[AuthoredRequest, ConstructibilityResult]]:
    sketch = sketch or build_sketch()
    out: list[tuple[AuthoredRequest, ConstructibilityResult]] = []
    for req in iter_public_authored_requests(manifest, sketch=sketch):
        out.append((req, evaluate_authored_request(req, sketch=sketch)))
    return out
