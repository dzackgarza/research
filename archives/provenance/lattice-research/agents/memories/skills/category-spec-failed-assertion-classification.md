---
title: Category Assertion Failure Classification
status: active
date: 2026-05-29
---

# Category Assertion Failure Classification

Use this memory when category-obligation examples fail or when cards/specs discuss
objects claimed to instantiate category definitions.

## Required references

Read `mem:skills/category-spec-workflow` and load `category-spec-style` before changing category-obligation examples, failed-assertion cards, or specs.

## Rules

- Do not run category-obligation examples while known definition or category-graph errors remain unresolved.
- Passing tests is not the goal; the examples exhibit whether representative objects satisfy declared category obligations.
- Do not weaken a category definition, bypass a constructor, suppress an exception, or check a shallow implementation detail merely to make an example pass.
- A failed assertion should be classified as missing implementation, missing constructor/refinement, wrong weakest category, missing definition, missing source evidence, or invalid assertion.
- Record failed category assertions as Nimbalyst cards, not local classification
  reports.

## Claim Classes

- Missing methods, missing implementations, and structural blockers go to implementation cards.
- Missing category definitions or missing obligations go to spec cards.
- Weakest-category, naming, or constructor-boundary ambiguity goes to decision cards.
- Evidence gaps go to research cards.
- Vague tangential findings go to `.agents/TODO.md`.
