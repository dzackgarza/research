---
name: category-spec-style
description: Use when editing, reviewing, or authoring category specs, type packages,
  Sage wrappers, constructors, method ownership, category-obligation examples, or
  category-spec implementation code.
---

# Category Spec Style

This skill is the canonical agent-facing style authority for category-spec mathematical and implementation compliance.

## Canonical source

The source of truth is this skill plus `references/style.md`.

Read `references/style.md` before acting on category-spec content, code, specs,
category-obligation examples, or compliance questions.

## Use this skill for

- Type signatures, overloads, and variadic Sage constructors or methods.
- Standard type packages and `types.py` ownership.
- Category, object, element, morphism, Hom, End, and Aut objects and method classes.
- Constructor definitions and named constructor design.
- Sage wrappers and interop boundaries.
- Category-obligation example files and compliance checks.
- Minimal indirection, anti-slop, and mathematical ownership review.

## Hard reminders

- Every sentence about category-spec work should be expressible as one of: a
  definition, construction, theorem-shaped assertion, hypothesis, proof obligation,
  source citation, implementation witness, or implementation gap.
- For every Sage name, first write the mathematical statement in a standard category
  under explicit hypotheses; only then mention Sage realization, implementation gaps,
  tests, or workflow state.
- The spec defines a Sage-grounded mathematical category/refinement interface inside
  Sage's category/object universe, not an unconstrained ideal API and not a mirror of
  only current Sage coverage.
- Category membership determines method obligations. `Groups` gives group operations.
  `FinitelyGeneratedGroups` gives finite-generation structure and a generating-set
  witness. `FinitelyPresentedGroups` gives finite-presentation structure.
- Use Sage as implementation evidence and a realization witness: preserve inventoried
  Sage functionality, identify honest refinements, and expose missing implementations
  without weakening mathematically natural objects.
- Specced vocabulary must exist before implementation proceeds.
- Mathematical definitions are foundational; do not treat them as ordinary code style.
- A spec row is a mathematical claim before it is a Sage/source-map row. If it cannot
  be stated coherently in mathematical language, it is not grounded.
- For methods, ownership means the category of objects on which the operation is
  defined. The category of the constructed result is codomain/target data, not by
  itself the method owner.
- Every spec claim must be grounded in a canonical mathematical source before edit:
  repo theory, references, spec backups, Sage written docs/source, or an approved
  decision card. A migrated TODO/card is provenance only, not definition authority.
- If a term has multiple plausible meanings, or if an invariant/equivalence needs a
  proof or hypotheses, stop the leaf and route a decision/source-mining card instead of
  guessing the familiar meaning.
- Complexity belongs behind mathematical nouns, not helper sprawl.
- Do not weaken specs to make current code pass. A failed category assertion usually
  records an implementation, constructor/refinement, source, wrong-weakest-category, or
  missing-witness gap against the spec.
- A typing fix is a proof obligation, not a way to quiet mypy. Before changing an
  annotation, adding a cast, or narrowing a return, ask whether the change makes the
  mathematical claim more explicit. If the code already expresses the correct Sage
  category structure and the checker only fails to see dynamic inheritance,
  `category_of`, `_with_axiom`, `refine_category`, or method-container projection,
  the fix belongs in the static model, plugin, stub, or QC tooling task, not as a
  local cast-only patch.
- Do not rewrite specs unless the user explicitly requests that exact edit.

## Required output behavior

When a task reveals a missing definition, incorrect ownership boundary, Sage-mapping ambiguity, or style violation, do not patch around it silently. Route it to the project workflow by loading `category-spec-workflow` and either creating a real tracked card, adding a TODO scratchpad note, or requesting a human decision.
