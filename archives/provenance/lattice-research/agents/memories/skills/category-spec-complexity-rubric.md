---
title: Category Spec Complexity Rubric
status: active
date: 2026-05-29
---
# Category Spec Complexity Rubric

Use this skill to set the numeric `complexity` metadata field and the card body's
`Complexity And Ownership` section.
Complexity measures execution burden and coupling; it does not order work.

## Core Policy

- Encode complexity as a number from 0 to 100 in `complexity`.
- Complexity is not priority, status, or sequencing.
- Score the actual card scope, not the importance of the parent plan.
- If a card hides multiple independent outcomes, split it before scoring.
- If the score is above 80, the item is usually not atomic; promote it to a plan or
  split it into leaf cards unless there is a specific reason to keep one card.

## Bands

Use `0-20` for trivial work:

- Metadata-only or formatting-only edits.
- Single-file documentation correction with no source-claim change.
- No mathematical ownership, API, dependency, or validation burden.

Use `21-40` for low-complexity bounded work:

- One narrow research lookup or source confirmation.
- One local implementation or spec edit with an obvious owner.
- Limited validation surface and no downstream semantic risk.

Use `41-60` for moderate work:

- Bounded public API cleanup, overload/signature split, or constructor-shape cleanup.
- Several related call sites inside one subsystem.
- Behavior should remain stable, but typing, imports, or compatibility require care.
- Verification is nontrivial but does not require new mathematical ownership decisions.

Use `61-80` for high-complexity work:

- Public category semantics, mathematical ownership, constructor routing, or inheritance
  changes.
- Multi-object work across category specs, mappings, wrappers, category-obligation
  examples, or tests.
- Downstream cards depend on the result, or mistakes can force redo.
- Validation must check the mathematical contract, not only local syntax.

Use `81-100` for plan-scale work:

- Foundational redesign, backend selection, theorem/proof burden, or cross-workstream
  migration.
- Multiple independently executable outcomes are bundled together.
- The work requires decisions, research, implementation, and validation stages.
- The correct action is normally to create or revise a plan and decompose it.

## Complexity And Ownership Section

For executable cards, include:

- Owner or role if known.
- Numeric complexity and band.
- Why the score fits this card.
- Item-specific evidence from source paths, affected surfaces, dependencies, or
  validation burden.
- Split/promote note when the card is near or above plan-scale complexity.

## Validation Checklist

- [ ] The card is minimal in the dependency poset before scoring.
- [ ] The score reflects coupling and verification burden.
- [ ] The body explains why the score is not just priority in disguise.
- [ ] Cards above 80 are split or explicitly justified as single executable units.
