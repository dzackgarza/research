---
id: TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn:
- '[[TASK-INTEGRATE-VARIETIES-CATEGORY]]'
- '[[TASK-INTEGRATE-POLYTOPES-CATEGORY]]'
title: Research category integration for toric varieties with lattice categories
status: complete
priority: high
description: Research and prepare the category-spec integration path for toric varieties,
  explicitly including integration with the lattice category.
successCriteria:
- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut
  objects, and representative examples with category obligations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed
  to proceed.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
- PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
---
# Research category integration for toric varieties with lattice categories

## Summary

Research and prepare the category-spec integration path for toric varieties, explicitly including integration with the lattice category.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating toric varieties, explicitly including integration with the lattice category.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Acceptance Criteria

- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut objects, and representative examples with category obligations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Dependencies And Boundaries

This is a research/planning card, not an implementation card. Do not write category code or specs until the vocabulary, ownership boundaries, and dependencies are clear or an approved plan delegates that work.

## Research Result

Status: needs-agent-review. Toric varieties are source-grounded as normal varieties
associated to rational polyhedral fans in presented torus character or
cocharacter lattices. For a presented coordinate torus, the coordinate characters
give a selected basis and the identity Gram matrix gives a unimodular lattice.
The metric dual lattice `L^#` and `Hom_ZZ(L, ZZ)` are canonically identified in that
presentation. This card does not authorize implementation.

## Mathematical Definition

Source evidence:

- `TASK-INTEGRATE-VARIETIES-CATEGORY` records `Varieties(k)` as integral separated finite-type schemes over `k`.
- Sage toric lattice documentation, https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/toric_lattice.html, records toric lattices as objects isomorphic to `ZZ^n`, with paired dual lattices conventionally named `N` and `M`, designed to prevent mixing elements from incompatible lattices.
- Sage toric variety documentation, https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/variety.html, constructs `ToricVariety(fan, ...)` from a rational polyhedral fan and exposes the fan as structural data.
- Sage fan morphism documentation, https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/fan_morphism.html, defines fan morphisms as lattice morphisms compatible with specified fans and notes induced morphisms between associated toric varieties.
- OSCAR normal toric variety documentation, https://docs.oscar-system.org/v1/AlgebraicGeometry/ToricVarieties/NormalToricVarieties/, distinguishes affine normal toric varieties associated to cones from normal toric varieties associated to polyhedral fans, citing Cox-Little-Schenck notation `U_sigma` and `X_Sigma`.
- OSCAR toric morphism documentation, https://docs.oscar-system.org/v1.4/AlgebraicGeometry/ToricVarieties/ToricMorphisms/, states that compatible `ZZ`-linear maps of fan lattices induce exactly the toric morphisms.
- `SPEC-MAPPING-MODULES.md`, `SPEC-MAPPING-LATTICES.md`, and `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` record the current module/lattice split. The toric card uses this as a process warning: character and cocharacter groups inherit ordinary free-module methods, while a presented coordinate-character lattice also carries the identity Gram form and is unimodular. Sage's toric dual parent witnesses the module dual and the metric-dual compatibility path under that identity-form identification; it does not make the metric dual a category-theoretic `DualObjects()` owner.

Project vocabulary:

- Character and cocharacter groups of presented coordinate tori should use the ordinary free-module, selected-basis, and formed-lattice vocabulary. The coordinate-character basis supplies the identity Gram matrix, so these objects lie in the unimodular lattice surface rather than in a toric-specific lattice subcategory.
- The module dual `Hom_ZZ(L, ZZ)` and the metric dual lattice `L^#` coincide for the identity Gram form. This is a special unimodular identification: for arbitrary formed lattices, `Hom_R(L,R)` and `L^# = {v in L_K : b(v,L) subset R}` are distinct surfaces. `DualObjects()` means Hom-dual/evaluation-bearing objects; it is not the metric-dual owner. No form on `Hom_R(L,R)` should be asserted unless it is transported through a recorded isomorphism with the metric dual.
- `RationalPolyhedralFans(N)` should own cones, rays, faces, subdivisions, smoothness/simplicial/completeness predicates, and fan morphism compatibility.
- `NormalToricVarieties(k)` should be varieties over `k` constructed from fans in a cocharacter lattice, with fan and torus data retained as structure.
- `AffineNormalToricVarieties(k)` are cone-owned affine refinements; projective, complete, smooth, simplicial, orbifold, Fano, and CPR-Fano toric varieties are stricter refinements.

Boundary decisions:

- Do not conflate the standard identity form on a presented coordinate-character lattice with later Coble/Nikulin bilinear forms. They are all formed lattice objects, but the form and presentation data differ and must remain explicit.
- Do not attach toric fan methods to all varieties. The fan is extra toric structure; only toric refinements own `fan()`, `rays()`, `cones()`, `orbit_closure(...)`, fan subdivision, and toric resolution surfaces.
- Do not treat a lattice polytope, normal fan, cone, or fan as the same object as the toric variety. These are constructor or structural inputs with their own polyhedral owners.
- Toric morphisms are not arbitrary scheme morphisms: the toric-refinement owner is compatible lattice/fan morphism data, with the induced scheme morphism as codomain evidence.
- Picard, class-group, Cartier/Weil divisor, and invariant-divisor methods should inherit broad variety/divisor/Picard owners where possible and add toric combinatorial routes only on toric refinements.

## Sage Surface Survey

Source evidence:

- Sage `ToricLattice(rank, name, dual_name, ...)` constructs named dual free abelian lattices and prevents accidental mixing of elements from different toric lattices.
- Sage `ToricVariety(fan, coordinate_names=None, base_ring=..., base_field=...)` constructs toric varieties from rational polyhedral fans and a field-like base.
- Sage toric varieties expose `fan()`, `orbit_closure(cone)`, `embedding_morphism()`, `rational_class_group()`, `resolve(...)`, `resolve_to_orbifold()`, `is_smooth()`, and `is_orbifold()`.
- Sage fan morphisms expose domain/codomain fans, compatibility checks, dominance, fibration, and injectivity predicates for lattice maps between fans.

Inference:

Sage is strong implementation evidence for toric lattices, fans, toric varieties, orbit closures, class groups, and fan-subdivision resolution routes. The project should translate this into mathematical owners rather than copying Sage's constructor shapes as the public spec.

## Backend Survey

Source evidence:

- OSCAR `NormalToricVariety` and `AffineNormalToricVariety` provide fan/cone constructors, famous toric varieties, affine open coverings, Q-Gorenstein checks, character lattices, class groups, Picard-group maps, and torus-invariant divisor groups.
- OSCAR toric morphisms construct morphisms from mapping matrices or finite-generated abelian group homomorphisms when the lattice map is compatible with the fans.
- `projects/github.com__dzackgarza__lattice-research/references/software-capability-map` lists polymake, Normaliz, Sage wrappers, and Oscar candidates for cones, Hilbert bases, lattice-point enumeration, toric and polyhedral work.
- Polymake toric documentation, https://polymake.org/doku.php/user_guide/tutorials/apps_fulton, provides a toric/fan-oriented backend route for polyhedral and toric computations.

Inference:

Sage and OSCAR are preferred candidates for toric varieties and toric morphisms. Polymake/Normaliz remain candidate backends for polyhedral fan/cone/lattice-point kernels. No local toric or polyhedral algorithm should be implemented before a backend audit picks the exact route.

## Local Category-Spec Dependencies

Source evidence:

- `TASK-INTEGRATE-VARIETIES-CATEGORY` supplies the variety substrate.
- `TASK-INTEGRATE-POLYTOPES-CATEGORY` and `TASK-INTEGRATE-POLYHEDRA-2D-POLYTOPES-CATEGORY` still need to admit polytope/polyhedron/fan-related vocabulary.
- `SPEC-MAPPING-MODULES.md` supplies finite-rank free module ownership for the underlying free-module operations.
- `SPEC-MAPPING-LATTICES.md` and the ModulesWithForms roadmap are source material for how the repo handles lattice identity, elements, morphisms, duals, and formed refinements. If their current public endpoint cannot express a presented coordinate-character lattice with identity Gram form, the correct conclusion is that the lattice vocabulary needs that ordinary unimodular presentation surface, not a toric-specific lattice type.
- `theory/references/literature/aegs_2023.md` contains downstream Coble/K3 references where toric surfaces, polytopes, and altered lattices appear as source material, but those are downstream geometry claims rather than generic toric API authority.

Inference:

The toric card should stabilize the lattice/fan/toric-variety boundary now and leave detailed polytope/fan constructors to polyhedral source-admission cards. It should route character/cocharacter groups through ordinary free-module, basis, and formed-lattice vocabulary, with the identity Gram form explicit for presented coordinate-character lattices.

## Method Ownership Guidance

Admit these as toric-level or toric-refinement surfaces when downstream specs are written:

- `character_lattice()` and `cocharacter_lattice()`: owned by toric varieties or torus/fan data; codomains are presented finite-rank free `ZZ`-modules/lattices. For coordinate-character presentations, the coordinate basis and identity Gram form make these unimodular lattices, with metric `dual_lattice()` and `Hom_ZZ(L, ZZ)` canonically identified.
- `fan()`: owned by normal toric varieties, returning a rational polyhedral fan in the cocharacter lattice.
- `rays()`, `cones()`, `maximal_cones()`, `faces()`, `subdivide(...)`, and `normal_fan(...)`: owned by fan/polyhedral refinements, not by all varieties.
- `torus()`, `dense_torus()`, and `torus_action()`: owned by toric varieties with algebraic torus codomain.
- `orbit_closure(cone)`: owned by toric varieties with fan cone input; codomain is a toric subvariety plus embedding morphism where exposed.
- `toric_morphism(lattice_map, codomain)`: owned by compatible fan/lattice morphism data; codomain is a toric morphism/scheme morphism.
- `resolve_by_fan_subdivision(...)` or toric `resolve(...)`: owned by toric varieties via fan subdivisions; generic `resolve_singularities()` remains a broader singular-variety surface with characteristic/backend hypotheses.
- `is_smooth()`, `is_complete()`, `is_projective()`, `is_simplicial()`, `is_q_gorenstein()`, `is_fano()`: toric refinements may provide combinatorial decision routes, but the underlying mathematical property owners remain the relevant variety/divisor/singularity categories.
- `class_group()`, `picard_group()`, torus-invariant Weil/Cartier divisor groups, and maps among them: toric refinements of broad divisor/Picard surfaces with combinatorial backends.

## Downstream Work Unblocked Or Routed

This card gives source-grounded input to these sibling cards and downstream specs:

- Polytope/polyhedron source-admission cards must admit cones/fans/lattice polytopes before toric constructor specs harden.
- Coble/K3 toric-surface references must state whether the object is a toric variety, fan, polytope, or altered free abelian lattice.
- Backend-routing work should prefer Sage/OSCAR for toric varieties and morphisms, with polymake/Normaliz for fan/cone kernels after audit.
- Lattice/ModulesWithForms implementation work is not a blocker for toric source admission, but toric specs must still depend on the lattice/free-module vocabulary enough to express character and cocharacter lattices, lattice points, lattice homomorphisms, the identity Gram form on coordinate-character presentations, duals, and evaluation pairings.

## Follow-Up Routing

No new card is needed from this toric source-admission pass.

- Polyhedral constructor details remain in the existing polytope/polyhedron source-admission cards.
- Backend implementation routing remains future work after source specs decide the exact toric object surfaces.
- Do not create a public `ToricLattice` type merely because a lattice appears in toric geometry. Use the ordinary presented lattice/module type, with the identity Gram form when supplied by the coordinate-character presentation, and attach toric structure at the torus, fan, or toric-variety level.

## Acceptance Evidence

- Mathematical convention recorded from Sage toric lattice/fan/toric variety docs, OSCAR toric variety and morphism docs, and local module/lattice ownership specs.
- Sage surfaces surveyed for toric lattices, fans, toric varieties, orbit closures, class groups, and fan-subdivision resolution.
- Backend surfaces surveyed for OSCAR toric varieties/morphisms and polymake/Normaliz polyhedral routing.
- Local dependency on lattice/free-module vocabulary recorded, with a guard against inventing toric-specific lattice types and with the identity Gram form recorded for presented coordinate-character lattices.
- Follow-up routing records that no new card is needed because existing polytope/polyhedron and backend-routing cards own specialization.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete

#### Evidence

**Gate 1 — Definition Grounding:** Sage toric docs, OSCAR toric docs, local module/lattice ownership specs cited.
**Gate 2 — Acceptance Criteria:** Toric lattice/fan/variety convention recorded; Sage surfaces surveyed (lattices, fans, orbit closures, class groups, subdivisions); OSCAR/polymake/Normaliz backends surveyed; dependency on lattice vocabulary guarded against toric-specific lattice type invention.
**Gate 3-6:** No issues. Correct boundary decision: toric variety = fan-owned normal variety refinement, character lattices use ordinary lattice types with identity Gram form, not a custom ToricLattice type.

---

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for toric varieties with lattice categories, routing character/cocharacter lattices through ordinary lattice/free-module vocabulary and toric varieties to fan-owned normal variety refinements.
- 2026-05-06: Corrected over-narrow ownership text that falsely excluded toric lattices from the lattice category. The lattices appearing in toric geometry are generated by torus characters/cocharacters; for presented coordinate-character lattices, the coordinate basis supplies the identity Gram form, making them unimodular formed lattices with metric dual `L^#` canonically identified with `Hom_ZZ(L, ZZ)`.
- 2026-05-06: Added explicit DAG prerequisite edges for source-admission substrate dependencies. These are sequencing edges, not blockers; the card should wait until the prerequisite source cards are accepted.
