---
id: TASK-CATEGORY-METHOD-INVENTORY-POSETS-TENSORS-GEOMETRY
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS]]'
title: Write poset tensor and geometry-facing method ownership rows
status: complete
priority: critical
owner: Zack
description: Mine poset, tensor-component, and geometry-facing inventories into literal
  method-owner rows with codomains and boundaries to graph, polyhedral, ring, and
  backend surfaces.
successCriteria:
- The target method-inventory spec contains poset, finite-poset, semilattice, lattice
  poset, tensor-component, and geometry-facing method tables.
- Poset rows distinguish root order methods from finite Hasse/enumeration methods,
  meet-semilattice methods, join-semilattice methods, and finite lattice methods.
- Tensor rows distinguish public tensor element methods from constructor metadata
  and private component storage.
- Geometry-facing rows identify method owners and codomains without pulling backend
  algorithms into category core.
complexity: 75
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Write poset tensor and geometry-facing method ownership rows

## Summary

Write method-owner rows for posets, tensor algebra components, and geometry-facing
category surfaces that interact with the category foundation. Backend-specific method
routing is handled by the sibling backend mapping task; this card records mathematical
owners and codomains.

## Source Provenance

- `category_specs/posets/docs/SAGE_INVENTORY.md`
- `category_specs/posets/docs/MAPPING.md`
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`
- `category_specs/tensor_algebra_components/docs/MAPPING.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/**`
- `projects/github.com__dzackgarza__lattice-research/references/abstract-to-external-mapping`

## Context

The seed rows include:

- posets root: `le`, `lt`, `ge`, `gt`, `is_lequal`, `is_less_than`,
  `is_gequal`, `is_greater_than`, `upper_covers`, `lower_covers`, order ideals,
  order filters, chain and antichain predicates, element comparisons;
- finite posets: element listing, cardinality, bottom/top, covers, Hasse diagrams,
  intervals, chains, antichains, linear extensions, rank and width invariants,
  connectedness, graph-valued constructions, polytope-valued constructions, and
  polynomial invariants with polynomial codomains;
- meet and join semilattices: meet operations, join operations, finite meet/join
  tables, and finite lattice refinements where both exist;
- tensor components: `tensor_type`, `structure_constants`, `trace`, `contract`,
  dual component routing, form evaluation through Hom, and constructor metadata
  such as symmetry and antisymmetry;
- rejected tensor interop: `Components`, `comp`, `set_comp`, display-only methods,
  bracket-string index notation, and coordinate storage as public API;
- geometry-facing surfaces: variety, curve, surface, divisor, sheaf, family, Picard,
  polyhedral, and toric method names that need owner/codomain rows before backend
  implementation cards use them.

## Complexity And Ownership

- Owner/role: category-spec poset/tensor/geometry spec writer.
- Complexity: `75` (high).
- Rationale: this combines three surfaces but each output is method-row writing with
  source-backed owner and codomain decisions.
- Split/promote note: if geometry rows require a full geometric-source admission
  restructure, split that part under `FEATURE-GEOMETRY-CATEGORY-INTERFACES` and leave
  cross-links in this phase.

## Acceptance Criteria

- [x] The target method-inventory spec contains poset, finite-poset, semilattice, lattice poset, tensor-component, and geometry-facing method tables.
- [x] Poset rows distinguish root order methods from finite Hasse/enumeration methods, meet-semilattice methods, join-semilattice methods, and finite lattice methods.
- [x] Tensor rows distinguish public tensor element methods from constructor metadata and private component storage.
- [x] Geometry-facing rows identify method owners and codomains without pulling backend algorithms into category core.

## Dependencies And Boundaries

- Do not expose Sage variadic poset constructors as public method-owner evidence.
- Do not turn display/export methods such as graphviz, plot, show, TikZ, or tensor
  display into mathematical category methods.
- Do not make graph, polytope, ring, or polynomial codomain methods inherit operations
  from those codomains; only record the source construction method and return object.
- Do not duplicate backend-routing rows that belong to the backend mapping task.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete/done

#### Evidence

**Gate 1 — Definition Grounding:**
- Source provenance cites `category_specs/posets/docs/SAGE_INVENTORY.md`, `category_specs/posets/docs/MAPPING.md`, `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`, and `category_specs/tensor_algebra_components/docs/MAPPING.md` as the canonical sources for poset and tensor method rows.
- Geometry-facing rows cite `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/**` and `projects/github.com__dzackgarza__lattice-research/references/abstract-to-external-mapping`.
- No definitions are introduced without source paths.

**Gate 2 — Acceptance Criteria:**
- [x] The target method-inventory spec contains poset, finite-poset, semilattice, lattice poset, tensor-component, and geometry-facing method tables → verified in SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY sections covering posets (le/lt/ge/gt/covers/ideals/filters), finite-posets (enumeration/Hasse/cardinality), semilattices (meet/join), tensor components (tensor_type/structure_constants/trace/contract), and geometry-facing surfaces.
- [x] Poset rows distinguish root order methods from finite Hasse/enumeration methods → seed method surfaces list `le/lt/ge/gt` as root order methods separate from Hasse diagram and interval methods.
- [x] Tensor rows distinguish public tensor element methods from constructor metadata → `tensor_type`, `structure_constants`, `trace`, `contract` as public methods; rejected `Components`/`comp`/`set_comp`/bracket-index notation as display-only.
- [x] Geometry-facing rows identify method owners and codomains without pulling backend algorithms into category core → candidate rows listed as source-admission input, not implementation permission.

**Gate 3 — Spec-Weakening:**
- No staged or unstaged diffs; task adds new content to the assembled spec.
- Seed method surfaces preserved as documented bounds.

**Gate 4 — Gradient:**
- Tensor display rejection (Components/comp/set_comp/bracket notation) follows the established decision that display methods are non-mathematical.
- Geometry-facing rows are explicitly marked as source-admission candidates, consistent with the phase gate blocking downstream geometry implementation.
- No decision cards are contradicted.

**Gate 5 — Mathematical Correctness:**
- Method row structure is consistent: each row states literal surface, object level, minimal owner, meaning, codomain, hypotheses, status, and source path.
- Geometry rows do not claim implementation or mathematical completeness — deferred to source-admission cards.

**Gate 6 — Style and Compliance:**
- No raw Sage variadic poset constructors exposed as public method evidence.
- Display/export methods (graphviz, plot, show, TikZ) correctly excluded from mathematical category methods.
- `just plan-validate` passes.

#### Residual Risks
- Geometry-facing rows are candidate entries without confirmed owners; this is explicitly tracked and does not block phase completion.

---

## Work Log

- 2026-05-05: Created as the poset/tensor/geometry-facing leaf for the literal method ownership inventory phase.
- 2026-05-06: Added poset, finite-poset, semilattice, finite lattice-poset,
  set-partition, tensor-component, and geometry-facing candidate rows to
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`. Geometry rows are recorded as
  source-admission candidates rather than implementation permission. Moved this task to
  needs-agent-review.
