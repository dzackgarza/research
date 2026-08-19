---
title: Research Proof Auditing
status: active
date: 2026-05-29
---
# Research Proof Auditing

This skill is the canonical proof, evidence, fraud-detection, and audit-sufficiency
authority for the research repo.

## Canonical source

The source of truth is this skill plus `references/proof-auditing.md`.

Read `references/proof-auditing.md` before auditing computation scripts, formal proofs,
proof claims, mathematical argument notes, mathematical verification output, adversarial
audit evidence, or acceptance claims.

## Core principle

Assertions with external sources are proof.
Print statements are theater.

A computation that prints success proves nothing.
A computation that asserts a sourced expected value proves the relevant claim when the
asserted predicate is mathematically adequate for the task.

## Argument-shape gate

Mathematical prose must expose the dependency chain.
Reject notes that replace construction with naming, cite authority instead of stating
theorem hypotheses, inflate immediate consequences into literature claims, or use vague
relational language where a map, embedding, quotient, pullback, or birational comparison
is required.

Immediate facts should be called immediate.
The audit burden belongs on the construction of the objects and maps that make those
facts relevant.

## Standardness calibration

Before accepting a "standard" claim, classify it:

- immediate consequence of a presentation;
- trivial first-principles derivation from definitions;
- standard foundational theorem with explicit hypotheses;
- niche research theorem requiring a precise citation and hypotheses;
- project-specific claim requiring construction or computation.

Do not let difficulty drift upward.
If a fact is immediate from rank, signature, a Gram matrix, a standard decomposition, or
a textbook construction, state it directly and move the proof burden to the upstream
construction that supplies the input.

Do not let progress accounting drift either.
A short derivation from definitions is not a milestone comparable to a niche theorem
that identifies the correct object, map, or moduli comparison.
Do the short derivation in place; reserve audit weight for the claims that smuggle in
assumptions.

## Required audit stance

- Check the exact `GOAL.md` obligation before judging evidence.
- Check the claim's visible status in the card, workstream report, and living paper.
  Reject polished prose whose margin notes or report links do not expose provenance,
  contentiousness, computation dependence, or human-review needs.
- Reject substitute computations, sampled evidence, bounded search without a proof of
  exhaustiveness, and prose claims presented as certificates.
- Reject authority chains, conclusion-smuggling names, and "standard" claims that do not
  state the standard theorem, hypotheses, and exact role in the argument.
- Reject public mathematical surfaces that return raw nonmathematical Sage base types
  such as `Parent` or `Element` unless the surface is a true deep base-category bridge.
  Most audited code should know the mathematical category of the returned object.
- When a broad Sage-facing type is genuinely required, require an explicit mathematical
  or interop alias such as `SageCategoryObject` or `SageElement` instead of leaking
  naked Sage infrastructure names into public proof, spec, or API surfaces.
- Reject mathematical research findings that depend on external or web sources but were
  left only in chat. Require a durable mathematical report memory with source links
  before treating the research as reusable audit input.
- Treat prior session claims, markdown summaries, and agent self-reports as unverified
  until backed by a passing script or formal proof.
- Require every assertion's expected value to trace to `GOAL.md`, literature,
  independent computation, or a cited derivation.
- Reject proof computations with zero assertions, self-computed expected values,
  hardcoded boolean verification, print-statement theater, or exception-swallowing
  verification.
- Formal proofs must have precise theorem statements, no `sorry`, and successful project
  build/check evidence.
- Treat reviewer consensus as evidence, not proof.
  If review appears to converge by weakening, obscuring, or restyling the claim instead
  of fixing it, flag false consensus.
  If review cycles do not reduce a precise disputed assertion, stop the loop and require
  escalation.

## Load with

- Load `research-orchestration` when the audit is part of state-machine execution or
  acceptance.
- Load `research-code-style` when audit findings concern code style, assertions,
  exceptions, constructors, or mathematical API design.
- Load `research-math-boundary` when audit findings concern the trusted mathematical
  base, backend ownership, Sage/GAP/Julia routing, or exact computation semantics.
- Load `category-spec-audit` when auditing category-spec plans, cards,
  category-obligation-example work, or implementations.

## Stop conditions

Stop acceptance and route follow-up when the evidence proves a cheaper proxy instead of
the requested claim, when exactness is replaced by numerics or sampling, when theorem
hypotheses are unchecked, when witnesses are missing, or when the target theorem has
drifted.

## Referenced documents

[Research Proof Auditing Reference](research-proof-auditing/proof-auditing)
