---
id: TASK-SOURCE-GROUND-POSETS-FINITE-AUTOMORPHISM-GROUP-HOMSET-ENUMERATION
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[TASK-AUDIT-POSETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[SPEC-MAPPING-POSETS]]'
title: Source-ground finite poset automorphism group enumeration before AutCategory admission
status: complete
priority: medium
description: Determine whether Sage Hasse-diagram automorphism machinery can ground
  an executable finite Posets AutCategory enumeration surface, or whether it must
  remain graph-backend interop only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- Sage finite poset and Hasse-diagram automorphism sources are audited for mathematical ownership and return-object semantics.
- The project owner is identified as Posets AutCategory, finite-poset parent validation, graph-backend interop, or rejected from public API.
- Any admitted API states domain, codomain, hypotheses, and how graph automorphisms become poset automorphisms without confusing graph and order owners.
complexity: 24
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Source-ground finite poset automorphism group enumeration before AutCategory admission

## Summary

Source-ground the Hasse-diagram automorphism evidence found during the Posets homset
mirroring audit before any executable finite Posets AutCategory enumeration surface is
admitted.

## Source Provenance

- `[[SPEC-MAPPING-POSETS]]`
- `category_specs/posets/homsets.py`
- Sage `sage/combinat/posets/hasse_diagram.py`
- Sage `sage/combinat/posets/posets.py`
- Sage generic homset and automorphism machinery as needed

## Context

The current Posets audit treats Hasse-diagram automorphism-group calls as backend
graph evidence only. Admitting finite poset automorphism enumeration requires a
separate proof that the graph automorphisms are exposed as order automorphisms with
the correct project owner and return object.

## Acceptance Criteria

- [x] The Sage source path from finite posets to Hasse-diagram automorphism groups is documented with line-level evidence.
- [x] The mathematical owner and return object for finite poset automorphism enumeration are specified or the surface is rejected from public API.
- [x] The result is reflected in the Posets mapping spec or in a follow-up decision card.

## Dependencies And Boundaries

- Do not admit graph automorphism APIs directly as Posets AutCategory methods.
- Do not implement enumeration until the source-grounded owner and codomain are settled.

## Work Log

- 2026-05-17: Created from the Posets homset mirroring audit to track finite
  automorphism-group enumeration separately from generic order-preserving map
  vocabulary.
- 2026-05-20: Source-mining complete. Findings below; SPEC-MAPPING-POSETS updated.

## Source Findings

**Sage source path:**

1. `FinitePoset` has NO public `automorphism_group()` method — confirmed via installed
   Sage 10.7 `sage/combinat/posets/posets.py`. No such method appears in
   `FinitePoset`, `FinitePosets.ParentMethods`, `FinitePosets.ElementMethods`, or
   `FiniteLatticePosets`.

2. `HasseDiagram(DiGraph)` at `sage/combinat/posets/hasse_diagram.py:74` inherits
   `automorphism_group()` from `GenericGraph` at
   `sage/graphs/generic_graph.py:24596`.

3. Return object (`sage/graphs/generic_graph.py:24965`):
   ```python
   return PermutationGroup(gens=gens, domain=int_to_vertex.values())
   ```
   Domain is vertex labels of the Hasse diagram graph — integer indices 0..n-1, NOT
   poset elements. Converting to poset elements requires `FinitePoset._list[index]`,
   which is a private API.

4. Internal use of `HasseDiagram.automorphism_group()` is at
   `sage/combinat/posets/hasse_diagram.py:2103` in orthocomplement computation —
   called as `self.automorphism_group(return_group=False, orbits=True)`. This is
   backend graph machinery, not a public poset-automorphism surface.

**Mathematical correctness note:** Graph automorphisms of the Hasse diagram equal
order automorphisms of the poset (the covering relation determines the partial order),
so the mathematical identity holds. However, the Sage API is graph-backend only.

**Decision — surface rejected from public API:**

- No public `FinitePoset.automorphism_group()` exists in Sage.
- The private route `P._hasse_diagram.automorphism_group()` returns an index-based
  `PermutationGroup`, not poset-element automorphisms.
- Admitting this as a project `Posets().AutCategory()` enumeration surface would
  require a poset-element wrapper over private Sage graph internals; that wrapper is
  not yet source-grounded and belongs to a separate implementation card if pursued.
- This surface remains **graph-backend interop only**; do not admit finite poset
  automorphism-group enumeration to the public AutCategory API without a separate
  source-grounded implementation card.
