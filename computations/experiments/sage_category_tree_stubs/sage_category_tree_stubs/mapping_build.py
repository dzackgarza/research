"""Build / refresh ``design/sage/mapping.yaml``.

Primary correspondence SSOT: authored sagecats ledger
(``design/sage/authored/``). Each public Sage category is evaluated by the
finite-limit constructibility checker (base + classifier applications).
Legacy ``correspondence.json`` still supplies edge-exception metadata.
Every observed immediate-supercategory edge receives exactly one disposition.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .authored_mapping import (
    authored_constructibility_record,
    evaluate_authored_request,
    iter_public_authored_requests,
    load_authored_manifest,
    resolve_classifier_id,
)
from .composed_identity import (
    build_dot_vertex_index,
    is_composed_cls_key,
    normalized_reading,
    seed_entity_for_reading,
)
from .constructibility import build_sketch, check_constructibility, constructibility_record
from .design_sources import DESIGN_ROOT, load_correspondence, load_json
from .observed_build import OBSERVED_PATH, _sage_axiom_id, _slug
from .seed_authored_sync import BASE_ID_ALIASES, resolve_base_id
from .semantic_seed import load_semantic_seed

MAPPING_PATH = DESIGN_ROOT / "sage" / "mapping.yaml"
ROUTES_PATH = DESIGN_ROOT / "routes" / "routes.yaml"

# Hand-reviewed construction targets (normalized construction ids).
_CONSTRUCTION_TARGETS: dict[str, tuple[str, str]] = {
    "Algebras": ("con.algebras", "partial_realization"),
    "CartesianProducts": ("con.category_products", "partial_realization"),
    "TensorProducts": ("con.tensor_products", "partial_realization"),
    "Dual": ("con.dual", "partial_realization"),
    "Quotients": ("con.quotients", "partial_realization"),
    "Subquotients": ("con.subquotients", "partial_realization"),
    "Homsets": ("con.homsets", "partial_realization"),
}


def _observed_id_index(observed: dict[str, Any]) -> dict[str, str]:
    out: dict[str, str] = {}
    for cat in observed.get("categories", []):
        out[cat["qualname"]] = cat["id"]
        inv = cat.get("inventory_category_id")
        if inv:
            out[inv] = cat["id"]
            out[inv.rsplit(".", 1)[-1]] = cat["id"]
    return out


def _relation_for(
    sage_name: str,
    *,
    aliases: set[str],
    corrected: set[str],
) -> str:
    if sage_name in aliases:
        return "presentation_alias"
    if sage_name in corrected:
        return "corrected_embedding"
    return "exact"


def _host_name_to_cat_id(host: str | None) -> str | None:
    if not host:
        return None
    simple = host.split("(", 1)[0].strip()
    return f"cat.{_slug(simple)}"


def _resolve_least_host_id(host: str | None, sketch: dict[str, Any]) -> str | None:
    """Resolve an authored host label to one unambiguous normalized category ID."""
    if not host:
        return None
    canonical_name = host.split("(", 1)[0].strip()
    matches: list[str] = []
    for entity in sketch["seed"].entities:
        entity_id = entity.get("id")
        if entity.get("canonical_name") == canonical_name and isinstance(entity_id, str):
            matches.append(entity_id)
    if len(matches) == 1:
        return matches[0]
    candidate = _host_name_to_cat_id(host)
    if candidate in sketch["nodes"]:
        return candidate
    return None


# The authored crosswalk already records, per axiom, whether a normalized classifier
# is owed at all. Reading those fields keeps a decided exclusion from being reported
# as a missing capability, and keeps a genuinely undecided row visible as one.
_AXIOM_ACTION_DISPOSITIONS: dict[str, str] = {
    "exclude": "excluded_test_only",
    "exclude from normalized mathematics": "excluded_engineering",
    "construction metadata, not classifier": "construction_owned",
    "split overloaded registry token": "split_by_host",
}


def _axiom_disposition(ax: dict[str, Any], target: str | None) -> str:
    """The disposition the ledger states for one Sage axiom.

    ``unsupported`` is reserved for rows the ledger says are owed a classifier and
    that the seed cannot supply; a decided exclusion is not a gap, and a token the
    ledger deliberately refused to globalize is not one either.
    """
    if str(ax.get("sage_status") or "").startswith("test-only"):
        return "excluded_test_only"
    decided = _AXIOM_ACTION_DISPOSITIONS.get(str(ax.get("mapping_action") or "").strip())
    if decided:
        return decided
    if target:
        return "rehosted" if ax.get("mapping_action") else "exact"
    return "unsupported"


def _resolve_parameter_binding(constraint: str | None, sketch: dict[str, Any]) -> dict[str, Any]:
    """Type an authored parameter constraint against the seed.

    A family applied at different parameters is different categories, so the
    constraint is part of a destination's identity and must be compared by
    identifier rather than by spelling: `R : CommutativeRings` and
    `R : CommutativeRings (intended Sage semantics)` are the same parameter category
    written two ways, and string comparison makes them different destinations.

    Only a constraint whose target resolves to a seed entity is typed. Anything else
    -- prose asides, several pieces of parameter data, an implicit constant field --
    is left unresolved with its text retained, because guessing which category was
    meant would silently identify or separate destinations on no evidence.
    """
    text = (constraint or "").strip()
    if not text:
        return {"constraints": "", "bindings": {}, "resolved": True}

    by_name: dict[str, str] = {}
    for entity in sketch["seed"].entities:
        eid = entity.get("id")
        if not isinstance(eid, str):
            continue
        for key in (entity.get("canonical_name"), *(entity.get("aliases") or [])):
            if isinstance(key, str):
                by_name.setdefault(key, eid)

    names, _, target = text.partition(":")
    target = target.strip()
    resolved_id = by_name.get(target)
    if resolved_id is None and target.endswith(")") and "(" in target:
        # `CommutativeAlgebras(R)` is the application spelling of a family the seed
        # declares with parameter R. Matching it to that family is the family's own
        # syntax, not an inference about which category was meant.
        head, _, args = target.partition("(")
        arity = len([a for a in args.rstrip(")").split(",") if a.strip()])
        for entity in sketch["seed"].entities:
            if entity.get("canonical_name") != head.strip():
                continue
            if len(entity.get("parameters") or []) == arity and isinstance(entity.get("id"), str):
                resolved_id = str(entity["id"])
                break
    if resolved_id is None:
        # Fall back to the ledger's established base-id identifications rather than
        # minting a new one: `AssociativeUnitalAlgebras` is already identified with
        # `cat.unital_algebras` there.
        head = target.partition("(")[0].strip()
        candidate = _host_name_to_cat_id(head)
        if candidate:
            entity_ids = {e["id"] for e in sketch["seed"].entities if isinstance(e.get("id"), str)}
            settled = resolve_base_id(candidate, entity_ids) or BASE_ID_ALIASES.get(candidate)
            if settled in entity_ids:
                resolved_id = str(settled)
    if not resolved_id or not target:
        return {"constraints": text, "bindings": {}, "resolved": False}
    # Follow spelling aliases to the canonical entity: `cat.commutativerings` and
    # `cat.commutative_rings` are one category, and comparing the two ids would split
    # a destination exactly as comparing the two prose spellings did.
    seen: set[str] = set()
    while resolved_id not in seen:
        seen.add(resolved_id)
        entity = next((e for e in sketch["seed"].entities if e.get("id") == resolved_id), None)
        definition = (entity or {}).get("definition") or {}
        if definition.get("operation") != "same_as":
            break
        nxt = definition.get("same_as") or definition.get("of") or definition.get("target")
        if not isinstance(nxt, str):
            break
        resolved_id = nxt
    bindings = {n.strip(): resolved_id for n in names.split(",") if n.strip()}
    if not bindings:
        return {"constraints": text, "bindings": {}, "resolved": False}
    return {"constraints": text, "bindings": bindings, "resolved": True}


def build_mapping(
    *,
    correspondence: dict[str, Any] | None = None,
    observed: dict[str, Any] | None = None,
    authored: dict[str, Any] | None = None,
) -> dict[str, Any]:
    corr = correspondence or load_correspondence()
    obs = observed or (load_json(OBSERVED_PATH) if OBSERVED_PATH.is_file() else {"categories": []})
    authored_manifest = authored or load_authored_manifest()
    obs_index = _observed_id_index(obs)
    obs_by_id = {c["id"]: c for c in obs.get("categories", [])}

    alias_names: set[str] = set()
    corrected_edges: dict[tuple[str, str], dict[str, Any]] = {}

    for row in corr.get("exceptions", []):
        kind = row.get("kind")
        sage = row.get("sage_name")
        parent = row.get("sage_parent")
        if kind == "alias":
            alias_names.add(sage)
        elif kind == "incorrect_parent" and sage and parent:
            corrected_edges[
                (
                    obs_index.get(sage, f"sage.category.{_slug(sage)}"),
                    obs_index.get(parent, f"sage.category.{_slug(parent)}"),
                )
            ] = row

    corrected_names = {obs_by_id[frm]["qualname"] for (frm, _to), row in corrected_edges.items() if frm in obs_by_id} | {
        row.get("sage_name") for row in corr.get("exceptions", []) if row.get("kind") == "incorrect_parent"
    }

    seed = load_semantic_seed()
    sketch = build_sketch(seed)
    dot_idx = build_dot_vertex_index(list(seed.entities))
    sage_to_entity = dict(corr.get("sage_to_graph", {}))

    category_mappings: list[dict[str, Any]] = []
    authored_names: set[str] = set()

    # --- Primary: authored sagecats ledger (179 public) ---
    for req in iter_public_authored_requests(authored_manifest, sketch=sketch):
        authored_names.add(req.sage_name)
        source_id = obs_index.get(req.sage_name, f"sage.category.{_slug(req.sage_name)}")
        result = evaluate_authored_request(req, sketch=sketch)
        construction = authored_constructibility_record(req, result)
        apps = (req.raw.get("normalized") or {}).get("classifier_applications") or []
        construction["authored_routes"] = [
            {
                "classifier": a.get("classifier"),
                "support_route": a.get("support_route"),
                "along": next(
                    (r.along for r in req.requests if r.occurrence_id and str(a.get("order")) in (r.occurrence_id.split("#")[-1:])),
                    None,
                ),
            }
            for a in apps
        ]
        named = seed_entity_for_reading(req.target_expression, entity_by_dot=dot_idx) or sage_to_entity.get(req.sage_name)

        kind = (req.mapping_kind or "").lower()
        if "alias" in kind:
            exact_relation = "presentation_alias"
        elif "backend" in kind or "exclusion" in kind or "compatibility" in kind:
            exact_relation = "removed"
        else:
            exact_relation = "exact"

        if result.status == "EXACT_BASE":
            category_mappings.append(
                {
                    "source": source_id,
                    "source_sage_name": req.sage_name,
                    "target": named or req.base_id,
                    "relation": exact_relation,
                    "normalized_reading": req.target_expression,
                    "construction": construction,
                    "sage_versions": {
                        "since": corr.get("version_label"),
                        "until": None,
                    },
                    "parameters": _resolve_parameter_binding(req.parameter_constraints, sketch),
                    "provenance": {
                        "status": "authored-exact",
                        "source": "design/sage/authored/",
                        "confidence": req.confidence,
                        "review_status": req.review_status,
                        "mapping_kind": req.mapping_kind,
                    },
                }
            )
            continue

        if result.status == "CONSTRUCTIBLE":
            category_mappings.append(
                {
                    "source": source_id,
                    "source_sage_name": req.sage_name,
                    "target": named or req.base_id,
                    "relation": "constructible",
                    "normalized_reading": req.target_expression,
                    "construction": construction,
                    "sage_versions": {
                        "since": corr.get("version_label"),
                        "until": None,
                    },
                    "parameters": _resolve_parameter_binding(req.parameter_constraints, sketch),
                    "provenance": {
                        "status": "authored-constructible",
                        "source": "design/sage/authored/ + constructibility",
                        "confidence": req.confidence,
                        "review_status": req.review_status,
                    },
                }
            )
            continue

        category_mappings.append(
            {
                "source": source_id,
                "source_sage_name": req.sage_name,
                "target": None,
                "relation": "unsupported",
                "normalized_reading": req.target_expression,
                "construction": construction,
                "sage_versions": {
                    "since": corr.get("version_label"),
                    "until": None,
                },
                "parameters": _resolve_parameter_binding(req.parameter_constraints, sketch),
                "provenance": {
                    "status": result.status.lower().replace("_", "-"),
                    "source": "design/sage/authored/ + constructibility",
                    "confidence": req.confidence,
                    "review_status": req.review_status,
                    "note": result.detail,
                },
            }
        )

    # Legacy aliases / corrections not already covered by the authored ledger.
    for sage_name, target in sorted(corr.get("sage_to_graph", {}).items()):
        if sage_name in authored_names:
            continue
        if sage_name not in alias_names and sage_name not in corrected_names:
            continue
        source_id = obs_index.get(sage_name, f"sage.category.{_slug(sage_name)}")
        relation = _relation_for(sage_name, aliases=alias_names, corrected=corrected_names)
        category_mappings.append(
            {
                "source": source_id,
                "source_sage_name": sage_name,
                "target": target,
                "relation": relation,
                "sage_versions": {
                    "since": corr.get("version_label"),
                    "until": None,
                },
                "parameters": _resolve_parameter_binding(req.parameter_constraints, sketch),
                "provenance": {
                    "status": "ledger",
                    "source": "correspondence.json exceptions",
                },
            }
        )

    mapped_sources = {r["source"] for r in category_mappings}
    mapped_names = {r.get("source_sage_name") for r in category_mappings}

    # Composed Base.Axiom towers observed at runtime (not in the 179 public ledger).
    for cat in obs.get("categories", []):
        qn = cat.get("qualname") or ""
        composed_meta = cat.get("composed")
        if not composed_meta and not is_composed_cls_key(qn):
            continue
        if cat["id"] in mapped_sources or qn in mapped_names:
            continue
        reading = (composed_meta or {}).get("normalized_reading") or normalized_reading(qn)
        constructibility = check_constructibility(qn, seed=seed, sage_to_entity=sage_to_entity)
        if constructibility.ok:
            category_mappings.append(
                {
                    "source": cat["id"],
                    "source_sage_name": qn,
                    "target": constructibility.base_id,
                    "relation": "constructible",
                    "normalized_reading": reading,
                    "construction": constructibility_record(constructibility),
                    "sage_versions": {
                        "since": corr.get("version_label"),
                        "until": None,
                    },
                    "parameters": _resolve_parameter_binding(req.parameter_constraints, sketch),
                    "provenance": {
                        "status": "constructible",
                        "source": "constructibility.check_constructibility",
                        "note": ("Ephemeral C.A… over normalized base; not in the authored public ledger"),
                    },
                }
            )
            continue
        named = seed_entity_for_reading(reading, entity_by_dot=dot_idx)
        if named:
            category_mappings.append(
                {
                    "source": cat["id"],
                    "source_sage_name": qn,
                    "target": named,
                    "relation": "exact",
                    "normalized_reading": reading,
                    "sage_versions": {
                        "since": corr.get("version_label"),
                        "until": None,
                    },
                    "parameters": _resolve_parameter_binding(req.parameter_constraints, sketch),
                    "provenance": {
                        "status": "composed-named",
                        "source": "seed dot_vertex match",
                        "note": constructibility.detail,
                    },
                }
            )
            continue
        category_mappings.append(
            {
                "source": cat["id"],
                "source_sage_name": qn,
                "target": None,
                "relation": "unsupported",
                "normalized_reading": reading,
                "construction": constructibility_record(constructibility),
                "sage_versions": {
                    "since": corr.get("version_label"),
                    "until": None,
                },
                "parameters": _resolve_parameter_binding(req.parameter_constraints, sketch),
                "provenance": {
                    "status": "not-constructible",
                    "source": "constructibility.check_constructibility",
                    "note": constructibility.detail,
                },
            }
        )

    mapped_sources = {r["source"] for r in category_mappings}
    mapped_names = {r.get("source_sage_name") for r in category_mappings}

    for cat in obs.get("categories", []):
        if cat["kind"] not in {"category_class", "named_wrapper"}:
            continue
        if cat["id"] in mapped_sources or cat.get("qualname") in mapped_names:
            continue
        category_mappings.append(
            {
                "source": cat["id"],
                "source_sage_name": cat["qualname"],
                "target": None,
                "relation": "unsupported",
                "sage_versions": {
                    "since": corr.get("version_label"),
                    "until": None,
                },
                "parameters": _resolve_parameter_binding(req.parameter_constraints, sketch),
                "provenance": {
                    "status": "pending",
                    "source": "auto-from-observed",
                    "note": "Not in authored public ledger",
                },
            }
        )

    nonpublic_dispositions: list[dict[str, Any]] = []
    for row in authored_manifest.get("nonpublic_source_class_dispositions") or []:
        nonpublic_dispositions.append(
            {
                "sage_class": row.get("sage_class"),
                "sage_module": row.get("sage_module"),
                "sage_role": row.get("sage_role"),
                "disposition": row.get("disposition"),
                "normalized_base": row.get("normalized_base"),
                "classifiers_or_construction": row.get("classifiers_or_construction"),
                "normalized_target_or_rule": row.get("normalized_target_or_rule"),
                "audit_note": row.get("audit_note"),
            }
        )

    axiom_mappings: list[dict[str, Any]] = []
    known_axioms: set[str] = set()
    for ax in authored_manifest.get("sage_axiom_crosswalk") or []:
        name = ax.get("sage_axiom")
        if not name:
            continue
        known_axioms.add(name)
        clf_name = ax.get("normalized_classifier_or_disposition")
        host = ax.get("normalized_least_host")
        host_id = _resolve_least_host_id(host, sketch)
        target = (
            resolve_classifier_id(
                classifier_id=None,
                classifier_name=clf_name,
                least_host=host,
                sketch=sketch,
                prefer_host=host_id,
                required_host_id=host_id,
            )
            if clf_name and isinstance(clf_name, str) and " " not in clf_name and host_id
            else None
        )
        axiom_mappings.append(
            {
                "source": _sage_axiom_id(name),
                "source_sage_name": name,
                "target": target,
                "least_normalized_host": host_id,
                "sage_defining_hosts": ([ax["sage_declared_at"]] if ax.get("sage_declared_at") else []),
                "transported_occurrences": [],
                "disposition": _axiom_disposition(ax, target),
                "note": ax.get("audit_note") or ax.get("mapping_action"),
            }
        )
    for ax in obs.get("axioms", []):
        name = ax["name"]
        if name in known_axioms:
            continue
        axiom_mappings.append(
            {
                "source": ax["id"],
                "source_sage_name": name,
                "target": None,
                "least_normalized_host": None,
                "sage_defining_hosts": list(ax.get("defining_categories") or []),
                "transported_occurrences": [],
                "disposition": "unsupported",
                "note": "Observed axiom; not in authored crosswalk",
            }
        )

    construction_mappings: list[dict[str, Any]] = []
    authored_cons = {c.get("sage_construction"): c for c in authored_manifest.get("sage_functorial_construction_crosswalk") or []}
    for cons in obs.get("constructions", []):
        name = cons["name"]
        if name in authored_cons:
            row = authored_cons[name]
            construction_mappings.append(
                {
                    "source": cons["id"],
                    "source_sage_name": name,
                    "target": None,
                    "relation": "authored_disposition",
                    "arity_map": cons.get("arity", "variadic"),
                    "parameter_map": {},
                    "result_category_mapping": {"rule": row.get("normalized_disposition")},
                    "note": row.get("audit_note"),
                }
            )
        elif name in _CONSTRUCTION_TARGETS:
            target, relation = _CONSTRUCTION_TARGETS[name]
            construction_mappings.append(
                {
                    "source": cons["id"],
                    "source_sage_name": name,
                    "target": target,
                    "relation": relation,
                    "arity_map": cons.get("arity", "variadic"),
                    "parameter_map": {},
                    "result_category_mapping": {"rule": None},
                    "note": "Specimen / provisional construction correspondence",
                }
            )
        else:
            construction_mappings.append(
                {
                    "source": cons["id"],
                    "source_sage_name": name,
                    "target": None,
                    "relation": "unsupported",
                    "arity_map": cons.get("arity", "variadic"),
                    "parameter_map": {},
                    "result_category_mapping": {"rule": None},
                    "note": "Observed construction; normalized target pending",
                }
            )

    return {
        "manifest": {
            "schema_version": 1,
            "sage_version_label": corr.get("version_label", "unknown"),
            "observed_ref": "design/sage/observed.json",
            "normalized_ref": "design/normalized/manifest/",
            "authored_ref": ("design/sage/authored/sage_normalized_category_mapping_manifest.json"),
            "note": (
                "Interpretation layer. Public category rows come from the "
                "authored sagecats ledger; constructibility certificates are "
                "finite-limit checker outputs. unsupported rows block a full "
                "Sage-parity claim (often missing seed bases/classifiers)."
            ),
        },
        "category_mappings": category_mappings,
        "axiom_mappings": axiom_mappings,
        "construction_mappings": construction_mappings,
        "nonpublic_dispositions": nonpublic_dispositions,
    }


def write_mapping(path: Path | None = None) -> Path:
    dest = path or MAPPING_PATH
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = build_mapping()
    dest.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return dest


def write_routes_stub(path: Path | None = None) -> Path:
    dest = path or ROUTES_PATH
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.is_file():
        existing = yaml.safe_load(dest.read_text(encoding="utf-8")) or {}
        if existing.get("routes"):
            return dest
    data = {
        "manifest": {
            "schema_version": 1,
            "note": ("Execution routing is separate from category meaning. Populate when wiring normalized operations to Sage methods."),
        },
        "routes": [],
    }
    dest.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return dest


def main() -> int:
    from .observed_build import write_observed

    write_observed()
    mpath = write_mapping()
    rpath = write_routes_stub()
    data = yaml.safe_load(mpath.read_text(encoding="utf-8"))
    print(
        f"wrote {mpath} "
        f"(categories={len(data['category_mappings'])} "
        f"axioms={len(data['axiom_mappings'])} "
        f"constructions={len(data['construction_mappings'])} "
        f"nonpublic={len(data.get('nonpublic_dispositions') or [])})"
    )
    print(f"wrote {rpath}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
