---
id: TASK-1777748120612-YVA6FX-REMOVE-STRICT-SUPERCATEGORY-LEAKS-FROM-IMAGE-SET-AND-SCHEMATIC-SET-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
dependsOn: []
title: Remove strict-supercategory leaks from image-set and schematic-set constructors
status: complete
priority: critical
description: Remove strict-supercategory leaks from image-set and schematic-set constructors
successCriteria:
- The card names the tracked mapping rows that define the image-subobject and real-set
  constructor boundaries.
- Sets().Constructors().ImageSubobject exposes only the public set-map and
  domain-subset input data, not Sage-only category, injectivity, inverse, or generic
  Set-wrapper knobs.
- Real-subset constructors use named interval/ray/point/finite-interval-union routes
  and do not expose Sage's variadic `RealSet(...)`, `normalized`, or manifold option
  bags.
- Literal diagram-set or schematic-set surfaces are either found and routed or a
  five-field negative finding records that no current category-spec surface exists.
- Relevant set smoke output is recorded without weakening smokes, mapping decisions,
  or public mathematical constructor obligations.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
---
# Remove strict-supercategory leaks from image-set and schematic-set constructors
Source: pasted backlog 2026-05-02.

Task: remove strict-supercategory leakage from diagram-set/image-set/schematic-set constructors, restrict inputs to the correct base category.

## Source Provenance

- Canonical set mapping:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`.
- Image-subobject admission row: `ImageSubobject(f, X)` maps to `ImageSets`, with
  public input `f: SetMorphism` and `domain_subset: Subset`; Sage's generic callable
  wrapping, arbitrary `Set(X)` fallback, and constructor options are interop details,
  not public project call shapes.
- Real-subset constructor rows in `SPEC-MAPPING-SETS` and
  `SPEC-MAPPING-TOPOLOGICAL-SPACES` admit named set constructors:
  `RealSetFromIntervals`, `RealSetInterval`, named open/closed/half-open intervals,
  rays, points, and the real line. They reject public variadic `RealSet(...)`,
  `normalized`, and manifold option bags in this subtree.
- Implementation surfaces:
  `category_specs/sets/__init__.py` and `category_specs/sets/subcategories/image.py`.

## Grounded Boundary

The executable obligation is to keep set-constructor surfaces attached to the smallest
mathematical input data that defines the object. Image subobjects are images of set
maps on domain subsets; the project constructor therefore takes exactly the map and
domain subset and refines the result through `Sets().Subobjects()` and
`Sets().Subquotients()`. Real subsets are subsets of the real line represented through
finite interval data or named interval/ray/point constructors; they may refine into
topological categories, but their constructor namespace remains `Sets().Constructors()`.

The migrated `diagram-set` and `schematic-set` words are treated as stale backlog
labels unless a current category-spec constructor, type, mapping row, or code surface
is found.

## Complexity Justification
- Owner: C61
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Remove strict-supercategory leaks from image-set and schematic-set constructors
- Why this specific score:
  - This task likely edits multiple constructor categories (`diagram-set`, `image-set`, `schematic-set`) and their inheritance constraints. Tightening category restrictions can break typed and runtime assumptions across callers, so coupling and verification cost are high but still localized to category wiring.
- Item-specific evidence:
  - The task statement directly names supercategory leak removal as the mechanism, implying non-local effect on constructor input validation paths rather than only one function.
  - The explicit owner 61 maps cleanly to this high-but-bounded migration risk.

## Implementation Notes
- Restricted `Sets().Constructors().ImageSubobject(...)` to the documented public inputs
  `f: SetMorphism` and `domain_subset: Subset`, and stopped exposing Sage-only
  `category`, `is_injective`, and `inverse` constructor knobs.
- Removed the public catch-all `Sets().Constructors().RealSet(...)` entry and the
  Sage `normalized` option from the real-line subset constructors. The remaining
  public surface now matches the documented interval, ray, point, and real-line
  constructors in `category_specs/topological_spaces/docs/MAPPING.md`.
- Parent integration review added the non-catch-all
  `Sets().Constructors().RealSetFromIntervals(intervals)` route for finite unions of
  Sage `InternalRealInterval` components, updated the set mapping to name that
  constructor, and updated regression call sites away from removed public option bags.

## Smoke Output

2026-05-06 targeted smoke rerun:

```text
$ just --justfile category_specs/justfile smoke-file sets/smoketest.sage
<exit 0>
stderr: repeated Sage warning that Sets.Topological is expected to be a
CategoryWithAxiom subclass and Sage is ignoring the axiom-shaped registration.
```

The warning is the known topological axiom-shape warning tracked separately by
`DECISION-20260505-REALSET-SAGE-TOPOLOGICAL-AXIOM-WARNING`; this card does not claim a
phase transition or resolve that separate warning.

## Negative Finding: Literal `diagram-set` / `schematic-set` surfaces
- Searched: `npx -y @probelabs/probe search "schematic" . -o plain --max-results 40`; `npx -y @probelabs/probe search "diagram set" . ext:md -o plain --max-results 40`; `npx -y @probelabs/probe search "SchematicSet DiagramSet" category_specs -l python -o plain --max-results 40`
- Found: no current `category_specs` constructor, type, mapping-doc, or code surface named `schematic-set`, `SchematicSet`, `diagram-set`, or `DiagramSet`; the only live constructor leaks in scope were `Sets().Constructors().ImageSubobject(...)` and the real-subset constructor family in `category_specs/sets/__init__.py`
- Conclusion: inference — the migrated task wording appears stale, and the current set/topology constructor leak work is represented by the image-subobject and real-subset constructor surfaces rather than any literal `diagram-set` or `schematic-set` constructor
- Confidence: High
- Gaps: did not inspect unrelated non-`category_specs` mathematical subtrees in depth beyond the broad repo search results because the user limited write ownership to set/topology constructor leak work

## Review Log

### Review 2026-05-06 (parent)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** parent review passed; human approval still required before completion

#### Evidence

- Gate 1: the card now grounds its constructor boundary in `SPEC-MAPPING-SETS` and
  `SPEC-MAPPING-TOPOLOGICAL-SPACES`, with exact image-subobject and real-subset
  constructor ownership.
- Gate 2: success criteria are concrete, and this card records the targeted set smoke
  command, exit status, and warning output.
- Gate 3: implementation notes describe scoped constructor-surface cleanup only; no
  unrelated typing cleanup, formatter churn, or API redesign is claimed here.
- Gate 4: current mapping keeps ImageSubobject and RealSet obligations, rejects only
  Sage-only option bags and catch-all routes, and records a five-field negative finding
  for stale literal `diagram-set` / `schematic-set` labels.
- Gate 5: `just --justfile category_specs/justfile smoke-file sets/smoketest.sage`
  exited `0`; the known topological axiom warning remains separately tracked.
- Gate 6: residual risk is limited to the stale migrated wording and the separate
  topological axiom-shape warning; neither is a blocker for this constructor-leak card.
