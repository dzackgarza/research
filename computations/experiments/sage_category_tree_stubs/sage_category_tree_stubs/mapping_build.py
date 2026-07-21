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


def _edge_key(frm: str, to: str) -> tuple[str, str]:
    return (frm, to)


def _host_name_to_cat_id(host: str | None) -> str | None:
    if not host:
        return None
    simple = host.split("(", 1)[0].strip()
    return f"cat.{_slug(simple)}"


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
    subdivided_edges: dict[tuple[str, str], dict[str, Any]] = {}

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
        elif kind == "composite_edge" and sage and parent:
            subdivided_edges[
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
                    "parameters": {},
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
                    "parameters": {},
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
                "parameters": {},
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
                "parameters": {},
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
                    "parameters": {},
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
                    "parameters": {},
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
                "parameters": {},
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
                "parameters": {},
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

    edge_mappings: list[dict[str, Any]] = []
    seen_edges: set[tuple[str, str]] = set()
    cat_target = {r["source"]: r.get("target") for r in category_mappings if r.get("relation") not in {"unsupported", "removed"}}
    alias_ids = {obs_index[n] for n in alias_names if n in obs_index} | {r["source"] for r in category_mappings if r.get("relation") == "presentation_alias"}

    for cat in obs.get("categories", []):
        frm = cat["id"]
        for edge in cat.get("immediate_supercategories") or []:
            to = edge.get("target")
            sage_to_name = edge.get("sage_name")
            if not to and sage_to_name:
                to = obs_index.get(sage_to_name, f"sage.category.{_slug(sage_to_name)}")
            if not to:
                continue
            key = _edge_key(frm, to)
            if key in seen_edges:
                continue
            seen_edges.add(key)

            sage_from = cat.get("qualname")
            sage_to_short = sage_to_name or (obs_by_id.get(to) or {}).get("qualname")

            if key in corrected_edges:
                row = corrected_edges[key]
                edge_mappings.append(
                    {
                        "source_edge": {
                            "from": frm,
                            "to": to,
                            "sage_names": {"from": sage_from, "to": sage_to_short},
                        },
                        "disposition": "corrected",
                        "normalized": {"kind": "forgetful", "path": []},
                        "reason": row.get("detail"),
                    }
                )
                continue
            if key in subdivided_edges:
                row = subdivided_edges[key]
                edge_mappings.append(
                    {
                        "source_edge": {
                            "from": frm,
                            "to": to,
                            "sage_names": {"from": sage_from, "to": sage_to_short},
                        },
                        "disposition": "subdivided",
                        "normalized": {"kind": "forgetful", "path": []},
                        "reason": row.get("detail"),
                    }
                )
                continue
            if frm in alias_ids or to in alias_ids:
                edge_mappings.append(
                    {
                        "source_edge": {
                            "from": frm,
                            "to": to,
                            "sage_names": {"from": sage_from, "to": sage_to_short},
                        },
                        "disposition": "alias_artifact",
                        "normalized": None,
                        "reason": "Endpoint is a presentation alias",
                    }
                )
                continue
            if frm in cat_target and to in cat_target and cat_target[frm] and cat_target[to]:
                edge_mappings.append(
                    {
                        "source_edge": {
                            "from": frm,
                            "to": to,
                            "sage_names": {"from": sage_from, "to": sage_to_short},
                        },
                        "disposition": "preserved",
                        "normalized": {
                            "kind": "forgetful",
                            "path": [],
                            "from_target": cat_target[frm],
                            "to_target": cat_target[to],
                            "note": ("Both endpoints reviewed; path ids pending functor census"),
                        },
                        "reason": None,
                    }
                )
                continue
            edge_mappings.append(
                {
                    "source_edge": {
                        "from": frm,
                        "to": to,
                        "sage_names": {"from": sage_from, "to": sage_to_short},
                    },
                    "disposition": "unsupported",
                    "normalized": None,
                    "reason": "No reviewed disposition yet",
                }
            )

    for key, row in {**corrected_edges, **subdivided_edges}.items():
        if key in seen_edges:
            continue
        frm, to = key
        disp = "corrected" if key in corrected_edges else "subdivided"
        edge_mappings.append(
            {
                "source_edge": {
                    "from": frm,
                    "to": to,
                    "sage_names": {
                        "from": row.get("sage_name"),
                        "to": row.get("sage_parent"),
                    },
                },
                "disposition": disp,
                "normalized": {"kind": "forgetful", "path": []},
                "reason": row.get("detail"),
                "note": "ledger-only; not present in current observed immediate edges",
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
        target = None
        if clf_name and isinstance(clf_name, str) and " " not in clf_name:
            cands = [c for c in sketch["classifiers"].values() if c.name == clf_name]
            target = cands[0].id if cands else None
        axiom_mappings.append(
            {
                "source": _sage_axiom_id(name),
                "source_sage_name": name,
                "target": target,
                "least_normalized_host": _host_name_to_cat_id(host),
                "sage_defining_hosts": ([ax["sage_declared_at"]] if ax.get("sage_declared_at") else []),
                "transported_occurrences": [],
                "disposition": ("rehosted" if ax.get("mapping_action") else ("exact" if target else "unsupported")),
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
        "edge_mappings": edge_mappings,
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
        f"edges={len(data['edge_mappings'])} "
        f"axioms={len(data['axiom_mappings'])} "
        f"constructions={len(data['construction_mappings'])} "
        f"nonpublic={len(data.get('nonpublic_dispositions') or [])})"
    )
    print(f"wrote {rpath}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
