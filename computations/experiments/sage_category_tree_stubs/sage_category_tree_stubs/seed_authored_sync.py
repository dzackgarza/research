"""Materialize semantic-seed entities/classifiers/arrows required by the authored ledger.

The sagecats ledger is the build spec: every public ``base_id`` and
``classifier_id`` it names must exist in the normalized sketch (as a real
entity, an alias of one, or a newly declared opaque interface).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .authored_mapping import load_authored_manifest
from .design_sources import NORMALIZED_MANIFEST_DIR, load_json

_MANIFEST = NORMALIZED_MANIFEST_DIR


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# Authored base_id → existing seed entity id (spelling / rename).
BASE_ID_ALIASES: dict[str, str] = {
    "cat.associativeunitalalgebras_r": "cat.unital_algebras",
    "cat.associativeunitalalgebras_k": "cat.algebras_over_field",
    "cat.hopfalgebras_r": "cat.hopf_algebras_r",
    "cat.liealgebras_r": "cat.lie_algebras_r",
    "cat.integraldomains": "cat.integral_domains",
    "cat.divisionrings": "cat.division_rings",
    "cat.commutativerings": "cat.commutative_rings",
    "cat.coxetergroups": "cat.coxeter_groups",
    "cat.weylgroups": "cat.weyl_groups",
    "cat.bimodules_r_s": "cat.bimodules_r",
    "cat.modules_rop": "cat.right_modules_r",
    "cat.modules_a": "cat.modules_r",
    "cat.modules_k": "cat.vector_spaces_k",
    "cat.schemes_k": "cat.schemes_s",
    "cat.chaincomplexes_c": "cat.chaincomplexes",
    "cat.homsets_c": "cat.homsets",
}


# New opaque bases: authored_id → (canonical_name, dot_vertex, forgetful_target, notes)
OPAQUE_BASES: dict[str, tuple[str, str, str, str]] = {
    "cat.crystals": ("Crystals", "Crystals", "cat.sets", "authored ledger base"),
    "cat.loopcrystals": ("LoopCrystals", "LoopCrystals", "cat.crystals", "authored ledger base"),
    "cat.supercrystals": ("SuperCrystals", "SuperCrystals", "cat.crystals", "authored ledger base"),
    "cat.magmaswithtwooperations": (
        "MagmasWithTwoOperations",
        "MagmasWithTwoOperations",
        "cat.sets",
        "least host for two-operation distributivity",
    ),
    "cat.groupswithsimplereflections": (
        "GroupsWithSimpleReflections",
        "GroupsWithSimpleReflections",
        "cat.groups",
        "exceptional common-data host for reflection/Coxeter package",
    ),
    "cat.generalizedcoxetergroups": (
        "GeneralizedCoxeterGroups",
        "GeneralizedCoxeterGroups",
        "cat.groupswithsimplereflections",
        "authored ledger base",
    ),
    "cat.complexreflectiongroups": (
        "ComplexReflectionGroups",
        "ComplexReflectionGroups",
        "cat.groupswithsimplereflections",
        "authored ledger base",
    ),
    "cat.permutationgroups": (
        "PermutationGroups",
        "PermutationGroups",
        "cat.groups",
        "authored ledger base",
    ),
    "cat.liegroups": ("LieGroups", "LieGroups", "cat.groups", "authored ledger base"),
    "cat.lieconformalalgebras_r": (
        "LieConformalAlgebras",
        "LieConformalAlgebras(R)",
        "cat.modules_r",
        "authored ledger base",
    ),
    "cat.lambdabracketalgebras_r": (
        "LambdaBracketAlgebras",
        "LambdaBracketAlgebras(R)",
        "cat.modules_r",
        "authored ledger base",
    ),
    "cat.kacmoodyalgebras_r": (
        "KacMoodyAlgebras",
        "KacMoodyAlgebras(R)",
        "cat.lie_algebras_r",
        "authored ledger base",
    ),
    "cat.monoidalgebras_r": (
        "MonoidAlgebras",
        "MonoidAlgebras(R)",
        "cat.algebras_r",
        "authored ledger base",
    ),
    "cat.groupalgebras_r": (
        "GroupAlgebras",
        "GroupAlgebras(R)",
        "cat.algebras_r",
        "authored ledger base",
    ),
    "cat.coxetergroupalgebras_r": (
        "CoxeterGroupAlgebras",
        "CoxeterGroupAlgebras(R)",
        "cat.algebras_r",
        "authored ledger base",
    ),
    "cat.semisimplealgebras_r": (
        "SemisimpleAlgebras",
        "SemisimpleAlgebras(R)",
        "cat.algebras_r",
        "authored ledger base",
    ),
    "cat.superalgebras_r": (
        "SuperAlgebras",
        "SuperAlgebras(R)",
        "cat.algebras_r",
        "authored ledger base",
    ),
    "cat.algebraideals_a": (
        "AlgebraIdeals",
        "AlgebraIdeals(A)",
        "cat.modules_r",
        "authored ledger base",
    ),
    "cat.ringideals_r": (
        "RingIdeals",
        "RingIdeals(R)",
        "cat.modules_r",
        "authored ledger base",
    ),
    "cat.discretevaluationrings": (
        "DiscreteValuationRings",
        "DiscreteValuationRings",
        "cat.integral_domains",
        "authored ledger base",
    ),
    "cat.discretevaluationfields": (
        "DiscreteValuationFields",
        "DiscreteValuationFields",
        "cat.fields",
        "authored ledger base",
    ),
    "cat.abelianvarieties_k": (
        "AbelianVarieties",
        "AbelianVarieties(K)",
        "cat.schemes_s",
        "authored ledger base",
    ),
    "cat.latticeposets": (
        "LatticePosets",
        "LatticePosets",
        "cat.posets",
        "authored ledger base",
    ),
    "cat.setswithpartialmaps": (
        "SetsWithPartialMaps",
        "SetsWithPartialMaps",
        "cat.sets",
        "authored ledger base",
    ),
    "cat.simplicialcomplexes": (
        "SimplicialComplexes",
        "SimplicialComplexes",
        "cat.sets",
        "authored ledger base",
    ),
    "cat.simplicialsets": (
        "SimplicialSets",
        "SimplicialSets",
        "cat.sets",
        "authored ledger base",
    ),
    "cat.vectorbundles_x_r": (
        "VectorBundles",
        "VectorBundles(X,R)",
        "cat.modules_r",
        "authored ledger base",
    ),
    "cat.drinfeldmodules_gamma_f_q_t_k": (
        "DrinfeldModules",
        "DrinfeldModules",
        "cat.modules_r",
        "authored ledger base",
    ),
    "cat.groupoidson_g": (
        "GroupoidsOn",
        "GroupoidsOn(G)",
        "cat.sets",
        "provisional fiber; authored ledger",
    ),
    "cat.sagebackendobjects": (
        "SageBackendObjects",
        "SageBackendObjects",
        "cat.sets",
        "compatibility-layer host only; not ordinary mathematics",
    ),
    "cat.polyhedra_r": (
        "Polyhedra",
        "Polyhedra(R)",
        "cat.sets",
        "authored ledger base",
    ),
    "cat.metricspaces": (
        "MetricSpaces",
        "MetricSpaces",
        "cat.sets",
        "host for Complete classifier",
    ),
    "cat.manifolds": (
        "Manifolds",
        "Manifolds",
        "cat.sets",
        "host for complex-analytic structure",
    ),
}


# Authored classifier_id → (name, host_entity_id)
# Hosts use seed ids (after alias resolution).
NEW_CLASSIFIERS: dict[str, tuple[str, str]] = {
    "clf.enumerated": ("Enumerated", "cat.sets"),
    "clf.filtered": ("Filtered", "cat.modules_r"),
    "clf.super": ("Super", "cat.modules_r"),
    "clf.aperiodic": ("Aperiodic", "cat.semigroups"),
    "clf.cwstructure": ("CWStructure", "cat.sets"),
    "clf.discretevaluation": ("DiscreteValuation", "cat.fields"),
    "clf.division": ("Division", "cat.rings"),
    "clf.nozerodivisors": ("NoZeroDivisors", "cat.rings"),
    "clf.functionfield": ("FunctionField", "cat.fields"),
    "clf.gaction": ("GAction", "cat.sets"),
    "clf.htrivial": ("HTrivial", "cat.semigroups"),
    "clf.heckemodulestructure": ("HeckeModuleStructure", "cat.modules_r"),
    "clf.jtrivial": ("JTrivial", "cat.semigroups"),
    "clf.ltrivial": ("LTrivial", "cat.semigroups"),
    "clf.rtrivial": ("RTrivial", "cat.semigroups"),
    "clf.lattice": ("Lattice", "cat.posets"),
    "clf.complexanalytic": ("ComplexAnalytic", "cat.manifolds"),
    "clf.finiteextensionof_q": ("FiniteExtensionOf", "cat.fields"),
    "clf.oremodulestructure_sigma_delta": ("OreModuleStructure", "cat.modules_r"),
    "clf.compatiblepartialorder": ("CompatiblePartialOrder", "cat.sets"),
    "clf.faithfulpermutationaction": ("FaithfulPermutationAction", "cat.groups"),
    "clf.pointed": ("Pointed", "cat.sets"),
    "clf.quantumgrouprepresentation": ("QuantumGroupRepresentation", "cat.modules_r"),
    "clf.fractionfieldpresentation": ("FractionFieldPresentation", "cat.integral_domains"),
    # Signature-specific finitely generated (hosted on Magmas / Semigroups).
    "clf.magmas.finitelygenerated": ("FinitelyGenerated", "cat.magmas"),
    "clf.semigroups.finitelygenerated": ("FinitelyGenerated", "cat.semigroups"),
    "clf.distributive_twooperations": ("Distributive", "cat.magmaswithtwooperations"),
    "clf.distributive_lattice": ("Distributive", "cat.latticeposets"),
    "clf.nilpotent": ("Nilpotent", "cat.lie_algebras_r"),
    "clf.finitelygenerated_lambdabracket": (
        "FinitelyGenerated",
        "cat.lambdabracketalgebras_r",
    ),
    "clf.ka_hlerpackage": ("KahlerPackage", "cat.algebras_r"),
    "clf.matrixalgebra": ("MatrixAlgebra", "cat.algebras_r"),
    "clf.modular": ("Modular", "cat.abelianvarieties_k"),
    "clf.jacobian": ("Jacobian", "cat.abelianvarieties_k"),
    "clf.semisimple": ("Semisimple", "cat.algebras_r"),
    "clf.shephard": ("Shephard", "cat.groupswithsimplereflections"),
    "clf.supercommutative": ("Supercommutative", "cat.superalgebras_r"),
    "clf.super_crystal": ("Super", "cat.crystals"),
    "clf.triangulardecomposition": ("TriangularDecomposition", "cat.kacmoodyalgebras_r"),
    "clf.complete": ("Complete", "cat.metricspaces"),
    "clf.lambdabracketalgebras_r.finitelygenerated": (
        "FinitelyGenerated",
        "cat.lambdabracketalgebras_r",
    ),
}


def resolve_base_id(authored_id: str, entity_ids: set[str]) -> str | None:
    """Map an authored base_id to a seed entity id, if possible."""
    if authored_id in entity_ids:
        return authored_id
    if authored_id in BASE_ID_ALIASES:
        alias = BASE_ID_ALIASES[authored_id]
        if alias in entity_ids:
            return alias
    compact = authored_id.replace("_", "")
    for eid in entity_ids:
        if eid.replace("_", "") == compact:
            return eid
    return None


# Crosswalk actions that rule out a classifier rather than name one.
_NON_CLASSIFIER_ACTIONS: frozenset[str] = frozenset(
    {
        "exclude",
        "exclude from normalized mathematics",
        "construction metadata, not classifier",
        "split overloaded registry token",
    }
)


def _authored_host_id(host_display: str, entity_ids: set[str]) -> str | None:
    """Resolve a crosswalk least-host display to a seed entity id.

    Hosts are written either as a plain family (``Manifolds``, ``Coalgebras(R)``) or
    as a refinement path (``Coalgebras(R).Super``). A refinement path names the total
    category of its last classifier, so it resolves only when that classifier's
    domain is already seeded; returning None keeps the row an honest gap instead of
    silently attaching the classifier to the wrong host.
    """
    head, _, tail = host_display.partition(".")
    base = head.split("(", 1)[0].strip().lower().replace(" ", "_")
    candidate = f"cat.{base}"
    resolved = resolve_base_id(candidate, entity_ids) or BASE_ID_ALIASES.get(candidate, candidate)
    for alt in (resolved, f"{resolved}_r", f"{resolved}_s", f"{resolved}_k"):
        if alt in entity_ids:
            resolved = alt
            break
    else:
        return None
    if not tail:
        return resolved
    for part in tail.split("."):
        domain = f"clf.{resolved.removeprefix('cat.')}.{part.lower()}.domain"
        if domain not in entity_ids:
            return None
        resolved = domain
    return resolved


def _axiom_classifier_id(classifier_name: str, host_id: str) -> str:
    """Host-qualified classifier id, so one Sage token never spans two hosts."""
    host = host_id.removeprefix("cat.").removesuffix(".domain").replace("clf.", "")
    return f"clf.{host}.{classifier_name.lower()}"


def _existing_classifier_id(classifier_name: str, host_id: str, classifiers: list[dict[str, Any]]) -> str | None:
    """A seeded classifier of this name already hosted here, if there is one."""
    wanted = classifier_name.lower()
    for c in classifiers:
        if str(c.get("name") or "").lower() != wanted:
            continue
        if c.get("host_id") == host_id or c.get("host") == host_id:
            cid = c.get("id")
            return str(cid) if cid else None
    return None


def sync_seed_from_authored(*, manifest: dict[str, Any] | None = None) -> dict[str, int]:
    """Append missing entities/classifiers/arrows; return counts added."""
    manifest = manifest or load_authored_manifest()
    entities_path = _MANIFEST / "entities.json"
    classifiers_path = _MANIFEST / "classifiers.json"
    arrows_path = _MANIFEST / "arrows.json"

    entities_doc = load_json(entities_path)
    classifiers_doc = load_json(classifiers_path)
    arrows_doc = load_json(arrows_path)

    entities: list[dict[str, Any]] = entities_doc["entities"]
    classifiers: list[dict[str, Any]] = classifiers_doc["classifiers"]
    arrows: list[dict[str, Any]] = arrows_doc["arrows"]

    entity_ids = {e["id"] for e in entities}
    clf_ids = {c["id"] for c in classifiers}
    arrow_ids = {a["id"] for a in arrows}

    added = {"entities": 0, "classifiers": 0, "arrows": 0, "alias_entities": 0}

    # Alias entities for authored ids that resolve to existing ones (stable base_id).
    needed_bases: set[str] = set()
    for row in manifest.get("category_mappings") or []:
        bid = (row.get("normalized") or {}).get("base_id")
        if bid:
            needed_bases.add(str(bid))

    for authored_id in sorted(needed_bases):
        resolved = resolve_base_id(authored_id, entity_ids)
        if resolved and authored_id != resolved and authored_id not in entity_ids:
            target_ent = next(e for e in entities if e["id"] == resolved)
            entities.append(
                {
                    "id": authored_id,
                    "kind": "alias",
                    "canonical_name": authored_id.removeprefix("cat."),
                    "parameters": [],
                    "definition": {
                        "operation": "same_as",
                        "of": resolved,
                        "notes": "authored ledger base_id spelling alias",
                    },
                    "aliases": [],
                    "dot_vertex": target_ent.get("dot_vertex"),
                    "provenance": "authored sagecats ledger",
                }
            )
            entity_ids.add(authored_id)
            added["alias_entities"] += 1
            # Structural equivalence edge for transport when needed
            eq_id = f"arr.alias.{authored_id.removeprefix('cat.')}"
            if eq_id not in arrow_ids:
                arrows.append(
                    {
                        "id": eq_id,
                        "source": authored_id,
                        "target": resolved,
                        "kind": "equivalence",
                        "preferred": True,
                        "provenance": "authored base_id alias",
                    }
                )
                arrow_ids.add(eq_id)
                added["arrows"] += 1

    # Opaque bases not yet present
    for authored_id, (cname, dot, forget_to, notes) in OPAQUE_BASES.items():
        if authored_id in entity_ids:
            continue
        # Ensure forget target exists (or will)
        if forget_to not in entity_ids and forget_to in OPAQUE_BASES:
            # defer — insert dependency first in a second pass
            pass
        entities.append(
            {
                "id": authored_id,
                "kind": "category_family",
                "canonical_name": cname,
                "parameters": [],
                "definition": {"notes": notes, "opaque": True},
                "aliases": [],
                "dot_vertex": dot,
                "provenance": "authored sagecats ledger",
            }
        )
        entity_ids.add(authored_id)
        added["entities"] += 1
        edge_id = f"fun.{authored_id.removeprefix('cat.')}_to_{forget_to.removeprefix('cat.')}"
        if edge_id not in arrow_ids and forget_to in entity_ids:
            arrows.append(
                {
                    "id": edge_id,
                    "source": authored_id,
                    "target": forget_to,
                    "kind": "forgetful",
                    "preferred": True,
                    "provenance": f"opaque interface: {notes}",
                }
            )
            arrow_ids.add(edge_id)
            added["arrows"] += 1

    # Second pass: forgetfuls whose targets were added in the same run
    for authored_id, (_cname, _dot, forget_to, notes) in OPAQUE_BASES.items():
        edge_id = f"fun.{authored_id.removeprefix('cat.')}_to_{forget_to.removeprefix('cat.')}"
        if edge_id in arrow_ids:
            continue
        if authored_id in entity_ids and forget_to in entity_ids:
            arrows.append(
                {
                    "id": edge_id,
                    "source": authored_id,
                    "target": forget_to,
                    "kind": "forgetful",
                    "preferred": True,
                    "provenance": f"opaque interface: {notes}",
                }
            )
            arrow_ids.add(edge_id)
            added["arrows"] += 1

    # Posets → Sets (Finite transport)
    if "fun.posets_to_sets" not in arrow_ids and "cat.posets" in entity_ids:
        arrows.append(
            {
                "id": "fun.posets_to_sets",
                "source": "cat.posets",
                "target": "cat.sets",
                "kind": "forgetful",
                "preferred": True,
                "provenance": "underlying set of a poset",
                "notes": "underlying_set",
            }
        )
        arrow_ids.add("fun.posets_to_sets")
        added["arrows"] += 1

    # Two Magmas ports from MagmasWithTwoOperations
    if "cat.magmaswithtwooperations" in entity_ids:
        for role, eid in (
            ("additive_operation", "fun.twoops_to_magmas_additive"),
            ("multiplicative_operation", "fun.twoops_to_magmas_multiplicative"),
        ):
            if eid in arrow_ids:
                continue
            arrows.append(
                {
                    "id": eid,
                    "source": "cat.magmaswithtwooperations",
                    "target": "cat.magmas",
                    "kind": "forgetful",
                    "preferred": role == "multiplicative_operation",
                    "provenance": role,
                    "notes": role,
                }
            )
            arrow_ids.add(eid)
            added["arrows"] += 1

    # Classifiers used by rows + NEW_CLASSIFIERS table
    needed_clfs: set[str] = set(NEW_CLASSIFIERS)
    for row in manifest.get("category_mappings") or []:
        for app in (row.get("normalized") or {}).get("classifier_applications") or []:
            cid = app.get("classifier_id")
            if cid:
                needed_clfs.add(str(cid))

    # The axiom crosswalk names a classifier and its least host for every Sage axiom
    # the ledger rules is owed one. Those are demands on the seed exactly as the
    # category rows' classifiers are; omitting them left the axiom surface reporting
    # a pending classifier for a decision the ledger had already made.
    for ax in manifest.get("sage_axiom_crosswalk") or []:
        if str(ax.get("mapping_action") or "").strip() in _NON_CLASSIFIER_ACTIONS:
            continue
        if str(ax.get("sage_status") or "").startswith("test-only"):
            continue
        clf_name = ax.get("normalized_classifier_or_disposition")
        host_disp = ax.get("normalized_least_host")
        if not clf_name or not host_disp:
            continue
        # A prose disposition is a ruling, not a classifier name.
        if " " in str(clf_name) or " " in str(host_disp):
            continue
        host_id = _authored_host_id(str(host_disp), entity_ids)
        if host_id is None:
            continue
        # Reuse the classifier the seed already carries for this name on this host.
        # Minting a host-qualified id unconditionally would duplicate the same
        # mathematics under two ids -- exactly the `clf.division` /
        # `clf.rings.division` split this project has already had to repair.
        existing = _existing_classifier_id(str(clf_name), host_id, classifiers)
        cid = existing or _axiom_classifier_id(str(clf_name), host_id)
        if cid not in clf_ids:
            NEW_CLASSIFIERS.setdefault(cid, (str(clf_name), host_id))
        needed_clfs.add(cid)

    # Map generic authored ids to host-specific ones when we minted them
    clf_aliases = {
        "clf.finitelygenerated": None,  # resolved per host at request time
    }

    for cid in sorted(needed_clfs):
        if cid in clf_ids or cid in clf_aliases:
            continue
        if cid in NEW_CLASSIFIERS:
            name, host = NEW_CLASSIFIERS[cid]
        else:
            # Try vocabulary
            vocab = {c["classifier"]: c for c in manifest.get("normalized_classifier_vocabulary") or []}
            # cid like clf.enumerated → Enumerated
            guess = cid.removeprefix("clf.").replace("_", "")
            entry = None
            for vname, v in vocab.items():
                if vname.lower().replace(" ", "") == guess.lower():
                    entry = v
                    break
            if entry is None:
                continue
            name = entry["classifier"]
            host_disp = entry.get("least_host") or "Sets"
            host_base = host_disp.split("(", 1)[0].strip()
            host_candidate = f"cat.{host_base.lower().replace(' ', '_')}"
            resolved = resolve_base_id(host_candidate, entity_ids)
            if resolved is None:
                resolved = BASE_ID_ALIASES.get(host_candidate, host_candidate)
            assert resolved is not None
            host = resolved
            if host not in entity_ids:
                # try Modules(R) → cat.modules_r
                alt = {
                    "cat.modules": "cat.modules_r",
                    "cat.schemes": "cat.schemes_s",
                    "cat.algebras": "cat.algebras_r",
                }.get(host)
                if alt is not None and alt in entity_ids:
                    host = alt
            if host not in entity_ids:
                continue
            NEW_CLASSIFIERS[cid] = (name, host)
            name, host = NEW_CLASSIFIERS[cid]

        domain = f"{cid}.domain" if not cid.endswith(".domain") else cid
        # For ids like clf.magmas.finitelygenerated, domain is clf.magmas.finitelygenerated.domain
        if not domain.endswith(".domain"):
            domain = f"{cid}.domain"
        leg = f"arr.{cid}"

        if domain not in entity_ids:
            entities.append(
                {
                    "id": domain,
                    "kind": "classifier_domain",
                    "canonical_name": f"{name}@{host}",
                    "parameters": [],
                    "definition": {"classifier_id": cid},
                    "aliases": [],
                    "dot_vertex": None,
                    "provenance": "authored sagecats ledger",
                }
            )
            entity_ids.add(domain)
            added["entities"] += 1

        if cid not in clf_ids:
            classifiers.append(
                {
                    "id": cid,
                    "name": name,
                    "host_id": host,
                    "domain_id": domain,
                    "leg_arrow_id": leg,
                    "transport": None,
                    "notes": "authored sagecats ledger",
                }
            )
            clf_ids.add(cid)
            added["classifiers"] += 1

        if leg not in arrow_ids:
            arrows.append(
                {
                    "id": leg,
                    "source": domain,
                    "target": host,
                    "kind": "classifier_leg",
                    "preferred": True,
                    "provenance": f"ι_{name} : {host}.{name} → {host}",
                }
            )
            arrow_ids.add(leg)
            added["arrows"] += 1

    # Also register generic clf.finitelygenerated as alias note — requests resolve
    # via prefer_host. Mint a catch-all on CatObject only if needed — skip.

    # Valuation / completeness structural interfaces
    for src, tgt, eid in (
        ("cat.discretevaluationrings", "cat.fields", "fun.dvr_to_fields"),
        ("cat.discretevaluationfields", "cat.fields", "fun.dvf_to_fields"),
        ("cat.discretevaluationrings", "cat.metricspaces", "fun.dvr_to_metricspaces"),
        ("cat.discretevaluationfields", "cat.metricspaces", "fun.dvf_to_metricspaces"),
        ("cat.integraldomains", "cat.fields", "fun.integral_domains_to_fields"),
        (
            "cat.lieconformalalgebras_r",
            "cat.lambdabracketalgebras_r",
            "fun.lieconformal_to_lambdabracket",
        ),
    ):
        if eid in arrow_ids:
            continue
        if src in entity_ids and tgt in entity_ids:
            arrows.append(
                {
                    "id": eid,
                    "source": src,
                    "target": tgt,
                    "kind": "forgetful",
                    "preferred": True,
                    "provenance": "authored ledger structural interface",
                }
            )
            arrow_ids.add(eid)
            added["arrows"] += 1

    # Alias cat.integraldomains if only underscore form exists — handled by BASE_ID_ALIASES

    entities_doc["entities"] = entities
    classifiers_doc["classifiers"] = classifiers
    arrows_doc["arrows"] = arrows
    _write_json(entities_path, entities_doc)
    _write_json(classifiers_path, classifiers_doc)
    _write_json(arrows_path, arrows_doc)
    return added


def main() -> int:
    counts = sync_seed_from_authored()
    print("seed sync from authored:", counts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
