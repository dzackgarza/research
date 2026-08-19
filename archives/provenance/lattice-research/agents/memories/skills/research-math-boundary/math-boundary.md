# Research Math Boundary Reference

## Current lattice/module redesign plan

For the lattice/module redesign, current durable planning lives under the modules-with-forms feature in root `.agents/plans/`, and lattice-specific guidance lives in local skills:

- `.agents/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/FEATURE-MODULES-WITH-FORMS-AND-LATTICES.md`
- `.agents/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/plans/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP.md`
- `.agents/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/plans/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP/PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES/PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES.md`
- `.agents/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/plans/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP/PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS/PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS.md`
- `.agents/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/plans/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP/PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS/PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS.md`
- `.agents/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/plans/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP/PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT/PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT.md`
- `.agents/plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/plans/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP/PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER/PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER.md`
- `.agents/skills/lattice-redesign/SKILL.md`

If the task touches `src/lattices/`, `tests/lattice_spec/`, or `tests/sage_spec/`, read the relevant plan/skill before acting. The dependency order is: foundational rings/fields/finitely generated module semantics, then general bilinear-module category and nouns, then lattice/dual/discriminant specializations, then orthogonal/root/Weyl/Coxeter/Eichler and indefinite-isometry work, then final human-in-the-loop spec revision.

## Existing software first

Mathematical implementation starts by checking whether a mature open-source backend
already implements the operation. The canonical workflow is the `research-software-wiring`
skill plus `theory/backends/software-capability-map.md`.

Do not write local algorithms for group orbits, lattice isometries, Groebner workflows,
resolution, sheaf cohomology, polyhedral computations, exact number-theory routines, or
similar standard mathematical kernels until backend routing has been checked.

If no preferred wiring is documented, stop implementation and create backend-gap
research work. Bespoke implementation requires a documented `true-gap` finding and
explicit human approval.
## Shared code boundary

Trusted shared code must be a semantic mathematical base built from explicit nouns with methods, not a flat bag of helper functions.

Public mathematical vocabulary must be source-grounded before it enters a spec. For
each new or moved noun, method, predicate, invariant, or equivalence, record the
definition source, hypotheses, codomain/return object, and choice-independence or
equivalence proof obligation. If those cannot be stated, the correct artifact is a
decision or source-mining card, not a speculative spec edit.

Required public vocabulary:

- `FreeBilinearModule`
- `FreeBilinearModuleElement`
- `Lattice`
- `LatticeElement`
- `LatticeMorphism`
- `DiscriminantGroup`
- `DiscriminantGroupElement`
- `DiscriminantGroupMorphism`

Constructors, coercions, exact transforms, predicates, and invariant extractors live on these nouns as methods or class methods. If a public operation takes a lattice, lattice element, discriminant group, or morphism as its primary argument, that is a design smell. Attach the verb to the noun unless the operation is a true interop bridge.

Never add wrappers whose only effect is renaming or forwarding to a native upstream method on the same object in the same language. Public wrappers are allowed only when they hide language interop or expose exact functionality upstream does not already provide.

Raw matrices, vectors, dicts, and lists may appear inside implementations and backend bridges, but they are not the public mathematical vocabulary. Shared code should compose upstream exact implementations rather than restating them.

Do not expose nonmathematical Sage infrastructure names such as `Parent` or `Element`
as the public return type of mathematical surfaces unless the code is a true
base-category bridge. In nearly all audited cases the surface should know the
mathematical category of the result and return a typed noun such as `Lattice`,
`LatticeElement`, `DiscriminantGroup`, or another repo-level mathematical object.

If the correct abstraction level is still broader than a repo noun, use an explicit
interop alias such as `SageCategoryObject` or `SageElement`. This keeps the audit
surface honest: the code is admitting that the result is Sage-backed and broad, but it
is not pretending that raw infrastructure names are satisfactory mathematical API
design.

Good shared interfaces include canonical constructors such as `Lattice.hyperbolic_plane()`, exact methods such as `lattice.discriminant_group()` or `element.inner_product(other)`, and exact transforms such as `morphism.image()` or `lattice.orthogonal_complement(sublattice)`.

Bad shared interfaces include task-shaped helpers like `assert_primitive_embedding`, wrapper aliases like `lattice_determinant(L)` when `L.determinant()` already exists, free functions like `norm(v, L)` when the receiver is a mathematical noun, and `verify_*` functions that silently absorb mathematical burden.

## Argument-level boundary

The same boundary applies to mathematical prose and computational proof artifacts. A
claim should be expressible as a chain of public mathematical objects and morphisms, not
as a pile of representations with prose wrapped around it.

Required proof vocabulary:

- objects: schemes, varieties, curves, surfaces, divisors, line bundles, Picard groups,
  lattices, discriminant groups, period domains, moduli spaces;
- morphisms and constructions: blowups, covers, pullbacks, pushforwards, embeddings,
  orthogonal complements, primitive closures, quotients, period maps, birational maps;
- invariants as methods on the relevant nouns, not detached helper facts.

Boundary failures:

- a note names the expected lattice, group, moduli space, or period domain before
  constructing it;
- a proof says "associated to", "governed by", "correct for", or "right target" where
  the next object should be a named map or comparison morphism;
- code computes raw matrices, signatures, or invariants but cannot express the objects
  and maps that make those computations relevant;
- an immediate invariant is over-explained while the upstream construction that makes
  the invariant meaningful is left implicit.

When this happens, do not patch around it with a task-local helper or a vague note.
Create or update the vocabulary/spec/source-mining artifact needed to express the
mathematics at the right level.

## When the base is insufficient

If a task cannot be expressed cleanly using the public noun vocabulary, stop and surface that as a task-boundary failure.

Examples include a required verb that belongs on `Lattice`, `LatticeElement`, `DiscriminantGroup`, or a morphism noun but no such exact method exists; repeated raw matrix or vector manipulation because the base lacks the right semantic object; or multiple tasks needing the same foundational operation or convention.

Do not solve this inside the task with ad hoc helpers. Send it back through `research-state-machine` for trusted-base admission and card redesign.

## Non-Python computation tests

For computations in Julia, GAP, or other non-Python languages, use the language's native testing framework and invoke it from Python/Sage rather than reimplementing assertions in a wrapper.

Use SageMath's GAP interface for GAP. Use `PyCall.jl` from Julia or `juliacall` from Python to bridge Julia's `Test` stdlib. Other languages follow the same pattern: native test framework plus thin Python/Sage caller that fails loudly on non-zero exit or exception.

Never port language-native logic into a Python shim just to make it testable.

## Foundation library

All lattice constructions must use `src/coble_geometry_foundation.py` constructors. Never construct lattices with ad hoc `diagonal_matrix()` calls. The legacy `coble_geometry.sage` must not be loaded.

## Lean and Aristotle

Before every Aristotle use, first review the `aristotle` skill.

Any Aristotle formalization attempt must begin by checking whether the target result already exists upstream in mathlib or other imported dependencies. Do not spend Aristotle budget reproving upstream results when the correct action is to find and reuse an existing theorem.

## Literature

For arXiv papers, always prefer the arXiv LaTeX/source payload over PDF OCR whenever source is available. Use OCR only for non-source papers, scanned sources, or figures that the source does not capture.

## CARAT

For lattice computations, CARAT may be useful for exact computation of integral orthogonal groups, normalizers, or orbit/stabilizer data. Review `Aut_grp`, `Normalizer`, and `Orbit` before building custom search code for finite positive-definite cases.
