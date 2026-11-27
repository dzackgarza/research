---
id: TASK-FORMED-COKERNEL-DESCENDED-FORM
trackerStatus:
  type: task
parents:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
dependsOn:
- '[[SPEC-MAPPING-LATTICES]]'
- '[[SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE]]'
title: Specify formed cokernel with descended form data
status: complete
priority: critical
description: Specify the category-spec surface for the generic formed-module cokernel
  required by lattice discriminant descent, including projection morphism and descended
  bilinear or quadratic form data.
activityType: synthesis
uncertaintyState: ordinary-open
workstreamRole: theory
claimStatus: source-backed
successCriteria:
- Sage FGP morphism kernel/image/lift evidence and the absence of a Sage formed cokernel
  are rechecked before closing the spec surface.
- '`f.cokernel()` is specified on the correct module or formed-module Hom-category
  element owner, not on lattice objects or raw Sage morphisms.'
- The specified object is `codomain(f) / image(f)` with projection morphism and includes
  descended bilinear or quadratic form data only under verified descent hypotheses.
- Lattice discriminant descent `A_L = coker(L -> L^#)` is routed through this generic
  cokernel spec path and records quotient-valued codomains `K/R` and `K/2R`.
- Category-obligation examples and mapping rows exercise public Hom/category APIs and do not use raw Sage
  morphisms or private project classes.
complexity: 75
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION
- PHASE-HOM-END-AUT-WORK-QUEUE
---
# Specify Formed Cokernel With Descended Form Data

## Summary

Specify the generic formed-module cokernel operation that the lattice mapping requires
for discriminant descent. The public operation is a morphism operation in the
module/formed-module Hom-category layer: for a morphism `f: M -> N`, the spec records
`coker(f) = N / image(f)` with its projection morphism, and names the richest correct
formed category when the form descends.

This card preserves the mathematical obligation that the mapping document cannot satisfy
by Sage FGP helpers alone: Sage exposes kernel, image, inverse-image, and lift surfaces,
but the category spec must name the quotient object together with descended bilinear or
quadratic form data.

## Source Provenance

- `[[SPEC-MAPPING-LATTICES]]`, especially the inherited FGP morphism row and G5/G6
  obligation routing.
- `category_specs/lattices/docs/SAGE_INVENTORY.md`, inherited FGP module and morphism
  inventory.
- Sage reference page for `sage.modules.fg_pid.fgp_morphism`.
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/modules/fg_pid/fgp_morphism.py:299`
  for `kernel()`.
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/modules/fg_pid/fgp_morphism.py:327`
  for `inverse_image()`.
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/modules/fg_pid/fgp_morphism.py:368`
  for `image()`.
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/modules/fg_pid/fgp_morphism.py:386`
  for `lift()`.
- `[[SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE]]`, which specifies
  `f.cokernel()` as `codomain(f) / image(f)` and requires descended form data when the
  descent hypotheses hold.
- `mem:projects/github.com__dzackgarza__lattice-research/context/bilinear-forms-duals-morphisms`, which records the
  coefficient-cokernel stage and the additional quotient by cross-term images.
- `mem:projects/github.com__dzackgarza__lattice-research/advice/category-spec-epistemic-foundation`.

## Context

The object-level claim is not a lattice-local method. It is the cokernel of a morphism
in the module or formed-module category. Lattice discriminant descent is a special use:
for the inclusion `i: L -> L^#`, the discriminant group is `A_L = coker(i)` and carries
quotient-valued form data when the nondegenerate integral finite-free hypotheses make the
descent valid.

The spec owner is the Hom-category element surface for modules with forms, with lattice
Hom surfaces inheriting or refining that operation. The spec must not expose raw Sage
coordinate quotients as the public object and must not attach this as a direct method on
lattice parents.

The descent gate is mathematical, not an option bag:

- the underlying module quotient `N / image(f)` exists;
- the projection morphism is part of the returned data;
- the form-codomain map contributes a coefficient cokernel;
- the descended codomain further quotients by cross-term images from
  `image(f)` paired with `codomain(f)`;
- bilinear or quadratic values are well-defined on cosets with values in that final
  quotient codomain;
- the specified quotient parent lies in the richest correct category whose hypotheses
  have actually been verified.

For lattice discriminant descent, the quotient-valued codomains are `K/R` for bilinear
data and `K/2R` for quadratic data.

## Mathematical Grounding

- Sage evidence: the `fgp_morphism` reference and installed source expose the FGP
  morphism element methods `im_gens`, `__call__`, `kernel`, `inverse_image`, `image`,
  and `lift`, but not a formed cokernel surface.
- Owner theorem: ordinary FGP `kernel`, `image`, `inverse_image`, and `lift` live on
  `Modules(R).HomCategory().ElementMethods`; the formed quotient `cokernel()` first
  requires form data, so it lives on
  `Modules(R).WithForms().HomCategory().ElementMethods`.
- Recovery formula: for `f: M -> N`, the carrier is `Q = N / image(f)` with projection
  `N -> Q`.
- Codomain formula: if the form codomain map is `h: S_M -> S_N`, first form
  `N_0 = coker(h)`, then quotient `N_0` by the images of
  `b_N(image(f), N)`; the descended bilinear or quadratic form has values in that final
  quotient.
- Lattice specialization: for `L -> L^#`, the coefficient cokernel is `K/R`, the
  cross-term quotient is trivial because `b(L, L^#) <= R`, and the discriminant
  bilinear/quadratic codomains are `K/R` and `K/2R`.
- Non-claim: this card does not require runtime construction.

## Acceptance Criteria

- [x] Reconfirm from Sage docs/source that FGP morphisms provide `kernel()`, `image()`,
      `inverse_image()`, and `lift()` but no formed cokernel operation with descended form
      data.
- [x] Specify `cokernel()` at the module/formed-module Hom-category element owner and
      route lattice Hom use through that owner.
- [x] Record the quotient object as `codomain(f) / image(f)` together with its projection
      morphism.
- [x] Preserve descended bilinear or quadratic form data only under explicit verified
      descent hypotheses; otherwise record the mathematical boundary rather than an
      unformed approximation.
- [x] Specify the lattice discriminant descent path `A_L = coker(L -> L^#)` through the
      generic formed cokernel operation.
- [x] Add or update category-obligation example/mapping evidence through public category/Hom APIs, not raw Sage
      morphism classes or private project classes.
- [x] Update `[[SPEC-MAPPING-LATTICES]]` and any affected forms/modules mapping rows if
      source grounding shows the owner must be split more finely.

## Dependencies And Boundaries

- This is a category-spec synthesis card, not a license to change the pure lattice
  mapping without source grounding.
- If specification exposes a missing quotient-valued codomain category or a missing
  formed-module quotient category, split a prerequisite source-mining or decision card
  instead of inventing an ad hoc helper.
- Do not specify a lattice-only cokernel shortcut. The generic operation belongs to the
  module/formed-module Hom layer and lattice discriminant descent is a specialization.
- Runtime bridge work, backend construction, or compatibility shims are downstream work
  outside this card. This card settles the mathematical owner, quotient formula, and
  descent hypotheses.

## Complexity And Ownership

- Owner/role: theory/spec-synthesis task under the Hom/End/Aut structural-admission
  plan, with forms/modules and lattice mapping surfaces as source constraints.
- Complexity: 75/100, high but below plan-scale.
- Why this score: the task changes a public categorical morphism specification and must
  coordinate module quotient objects, formed-module descent, projection morphisms,
  lattice discriminant descent, and public-API category-obligation examples.
- Item-specific evidence: Sage FGP source supplies adjacent morphism operations but not
  the formed cokernel; historical discriminant specs already name the required object and
  descent hypotheses; the lattice mapping G5/G6 audit requires a tracked category-spec
  obligation.

## Work Log

- 2026-06-02: Addressed fresh review findings: replaced the discriminant-group category-obligation example
  evidence with public `Lattices(ZZ).DiscriminantGroups()` category-route checks,
  corrected the discriminant projection codomain from lattice morphism to formed-module
  morphism, and removed the optional `domain_subset` widening from the formed Hom
  `image()` surface. The Sage submodule-image `__call__` branch is recorded as a
  separate module Hom/subobject source-mining obligation rather than an optional
  `image()` argument. A later focused review found a `super_categories()` style
  violation from an explicit join; the touched torsion/discriminant supercategory
  methods now use plain single-chain category entries instead.
- 2026-06-02: Fresh focused review verified the public discriminant-group category-obligation example route,
  formed projection type, zero-argument formed `image()`, no-join supercategory shape,
  and finite-presentation-over-PID invariant-factor inheritance. A final narrow
  fresh-source review checked installed Sage `fgp_morphism.py` and `fgp_module.py`:
  `FGP_Morphism` exposes `im_gens`, `__call__`, `kernel`, `inverse_image`, `image`, and
  `lift`, while neither checked FGP source file exposes `cokernel`; the requested local
  HTML doc path was absent. Task-level review passed.
- 2026-06-02: Added formed-Hom cokernel/projection/lift spec obligations and
  discriminant-group cokernel-diagram spec surfaces. Corrected invariant-factor
  ownership: `invariants()` is inherited from
  `Modules(R).FinitelyPresented().OverPID()`, not redeclared on torsion formed or
  discriminant-group categories.
- 2026-06-02: Created to route the `SPEC-MAPPING-LATTICES` G5/G6 formed-cokernel gap to
  an executable category-spec card without claiming the spec review is complete.
- 2026-06-02: Moved to `needs-agent-review`. Review evidence to attack:
  official Sage `sage.modules.fg_pid.fgp_morphism` docs list `im_gens()`, `image()`,
  `inverse_image(A)`, `kernel()`, and `lift(x)` on `FGP_Morphism`; installed source
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/modules/fg_pid/fgp_morphism.py`
  has `kernel`, `inverse_image`, `image`, and `lift` definitions but no `cokernel`
  definition in `FGP_Morphism`. The project owner/formula evidence is visible in
  `category_specs/forms/subcategories/with_forms.py`, `[[SPEC-MAPPING-FORMS]]`, and
  `[[SPEC-MAPPING-LATTICES]]`; the public route category-obligation example is the `FormedModules(ZZ)` Hom,
  End, and Aut category-object assertion in `category_specs/forms/category_obligations.sage`.
  This is a review handoff, not an acceptance claim.
