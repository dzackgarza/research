# Design hazard register {#design-hazard-register}

Status at this commit, for the reopened issue #289.

The ledger below was deleted from the book at `ada60ed3a2` ("move the agent and implementation
surfaces out of the book"), together with the rest of `writing/category-theory/contributing/`;
its intended home is the agent memory vault, to which `.agents` is a symlink. That symlink does
not resolve inside this project, so the vault copy cannot be read or written from here, and
nothing in this repository records what it holds.

What the sources support, and what this file is: `H1`-`H15` are recovered verbatim from history
at `ada60ed3a2^:writing/category-theory/contributing/Design-Hazard-Ledger.md`, and `H16`-`H19`
are new, written from the four drift modes the issue names as unguarded. The touchstone source
document `mathematical-simplicity-agent-touchstone.md` is not in this repository either, so the
four new entries transcribe the issue's own description of each mode and not the document's
sections; whoever restores the document should reconcile the wording against it.

This file is a working register, not book content: it is deliberately outside `writing/`.

---

## The ledger

### H1--H15, recovered

A recorded ledger of hazards observed in this program's formalization and design work — each one actually occurred, was corrected, and now has a standing guard.
Entries are forward-facing: the point of each row is the **guard** — the rule that makes the hazard detectable or inexpressible — not the history.
New contributions are checked against the guards, which live in the Contribution Guidelines, Categorical Presentation Principles, and the Language Style Guide.

Provenance for all entries: the [#251](https://github.com/dzackgarza/research/issues/251) record (2026-07-16/17). One meta-observation covers the whole ledger: every corrected defect had the same form — *a bespoke invention should have been a named standard construction*.

## H1 — Code-as-invariant {#sec-h1-code-as-invariant}

**Mechanism.** Work starts from "this declaration exists; what mathematics justifies it?"
instead of deriving the standard mathematics and deciding which declarations survive.
Mathematics becomes post-hoc justification for preserving code.
**Guard.** Contribution Guidelines step 1 (derive first, admit declarations second); right-to-exist decided before any identification is proved.

## H2 — Proof-carrying laundering {#sec-h2-proof-carrying-laundering}

**Mechanism.** A checked witness relating a local declaration to upstream mathematics is treated as legitimizing the declaration.
A proof that a bespoke accessor agrees with the standard invariant is evidence the accessor is redundant or misplaced — the proof can certify the defect more strongly.
**Guard.** Identification is never admission: right-to-exist first (Contribution Guidelines); level check (a declared item generable one level down is a defect).

## H3 — Capability-to-structure promotion {#sec-h3-capability-to-structure-promotion}

**Mechanism.** Backend requirements are promoted into mathematical structure: enumeration machinery becomes an "enumeration-equipped category", a chosen basis becomes object data, computational presentations become homes of the invariants they evaluate.
**Guard.** Witness discipline (mathematical-type convention: witness is a declared type; a presentation is never the home of the invariant it evaluates); layer quarantine (mathematics-before-realization convention).

## H4 — Exact-name fixation {#sec-h4-exact-name-fixation}

**Mechanism.** When no single upstream constant names a construction, the mathematics is experienced as missing, producing false gaps and false contribution opportunities.
Standard mathematics is frequently compositional.
**Guard.** Gap epistemics (Integration Model (in the vault)): a gap claim is a negative claim requiring search evidence with nearest notions distinguished; compositional expressions count as matches.

## H5 — Singleton reification {#sec-h5-singleton-reification}

**Mechanism.** A worked example is promoted into reusable vocabulary (a rank-two object becomes a concept instead of an instantiation of the general rank-n construction).
**Guard.** Define the general construction, recover instances; examples are instances, never vocabulary (Settled Rulings, relation kinds).

## H6 — Proxy optimization {#sec-h6-proxy-optimization}

**Mechanism.** The judgment "is every declaration legitimate?"
is replaced by tractable metrics — counts going down, mandatory reason strings, reclassification of hard cases out of the denominator.
Progress-shaped evidence accumulates while the mathematical question goes unresolved.
**Guard.** Falsified rows re-derive the population, never repair the row; every registry report names the most-canonical outstanding gap (Integration Model, gap epistemics).

## H7 — Correction-as-patch {#sec-h7-correction-as-patch}

**Mechanism.** A counterexample is treated as a defect at its site rather than evidence against the framework: each correction produces another local theorem, label, or reason field while the ambient scheme survives.
Patching looks like responsiveness; asking "what standard theory makes this unrepresentable?"
produces the required deletion.
**Guard.** A mathematical correction invalidates downstream classifications until the presentation is re-derived (Contribution Guidelines); one counterexample indicts the classifier.

## H8 — Novelty-as-progress {#sec-h8-novelty-as-progress}

**Mechanism.** Reinvention generates artifacts (coined vocabulary, hand-labeled diagrams, bespoke machinery); deference generates citations.
Artifacts read as work, so agents are drawn to reinvention even when the correct answer is "this is `FullSubcategory` + `HasForget₂` + `Aut`; there is nothing to invent."
**Guard.** The dictionary-image criterion (Categorical Presentation Principles): anything not the image of a named upstream construction under the dictionary is wrong by definition — reinvention is inexpressible, not merely audited.

## H9 — Context decay (prose has no diff) {#sec-h9-context-decay}

**Mechanism.** Artifacts living as prose are re-transcribed each session, and each transcription silently drops ratified constraints; invented vocabulary can only be audited for internal consistency, so the audit loop becomes self-referential.
**Guard.** Artifacts live as checked, machine-readable data with standard vocabulary; revisions edit the data and regenerate (Categorical Presentation Principles, generation discipline).

## H10 — Decorative higher machinery {#sec-h10-decorative-higher-machinery}

**Mechanism.** Higher-categorical language deployed where the truncation is the content, silently changing the object while looking like a simplification (the genus stated as a homotopy pullback when π₀ does not commute with homotopy pullbacks).
**Guard.** Level check in both directions — declared items sit at the lowest level at which they are generated; truncations are stated explicitly (style guide @sec-replacement-dictionary rules).

## H11 — Theorem-into-definition demotion {#sec-h11-theorem-into-definition-demotion}

**Mechanism.** A provable implication is encoded by restructuring definitions (nesting one property-defined subcategory inside another), baking a theorem into the presentation and diverging from upstream anchors.
**Guard.** Implication posets among properties are generated by theorem edges with witnesses; definitions follow the upstream anchor's siting (Settled Rulings, alt/skew).

## H12 — Lift ambiguity {#sec-h12-lift-ambiguity}

**Mechanism.** Structure consumed without naming which structure: one session proves something about ⊕ and a later session silently consumes it for ⊗, because both are "the monoidal structure."
**Guard.** Name every section (chosen-structure convention); unnamed structure-reference is grep-detectable red.
The name goes on the lift, never on the classifier — a classifier node per structure is the proliferation hazard one level up.

## H13 — Authority laundering {#sec-h13-authority-laundering}

**Mechanism.** Vocabulary with a rigorous definition in a literature the intended auditor does not command (model theory, type theory, PL theory) reads as authoritative but is unfalsifiable by the audience the artifact serves — worse than visible coinage.
**Guard.** Audience-relative admissibility (standard-terms convention); the corpus boundary is which literature, not how well-known.

## H14 — Stale-prior convention claims {#sec-h14-stale-prior-convention-claims}

**Mechanism.** Agents and automated reviewers assert a dependency's names or conventions from priors ("Mathlib's standard namespace is X") that contradict the pinned checkout; acting on them breaks building usage.
Recorded exemplar: a reviewer's "standard namespace is `Basis`, not `Module.Basis`" and "`Basis.toDual` is a `LinearEquiv`" — the live tree has `Module.Basis`, and `toDual` is a `LinearMap` whose equivalence is `toDualEquiv`. **Guard.** The pinned checkout is the naming authority for everyone; every convention claim carries the verification burden before acting (Contribution Guidelines, Lean style rules).

## H15 — Supervision inversion {#sec-h15-supervision-inversion}

**Mechanism.** After repeated corrections or forced stops, autonomy is *increased* ("the remaining work is mechanical") — exporting a malformed foundation multiplies the damage precisely when self-monitoring has demonstrably failed.
**Guard.** Repeated corrections escalate to specification review and tighter supervision (Contribution Guidelines: corrections reset); foundational defects are never deferred because remaining tasks are mechanical (never defer a foundational defect).

## H16 — Principle–action decoupling {#sec-h16-principle-action-decoupling}

**Mechanism.** The correct principle is stated and then violated in the next edit: doctrine is
held as material to quote rather than as the lens the same change is judged by. Verbal agreement
produces confidence that the work does not support, while the change continues on the old
invariant.
**Guard.** A principle invoked in a change must be shown applied at that change's own site: the
sentence that states it and the edit that must satisfy it are reviewed together, and a principle
asserted without its enforcement there is recorded as unverified rather than as settled.

## H17 — Formalization at typing speed {#sec-h17-formalization-at-typing-speed}

**Mechanism.** Code is written before variance, direction, morphisms, truncation and universal
properties are settled. Discretionary choices then become implicit in types, where they are later
defended as facts about the implementation.
**Guard.** No declaration lands before the standard construction it is an instance of is named,
with its variance and direction; a signature whose universality is undecided is recorded as
provisional and is not cited by later work.

## H18 — Flattening higher cells into engineering data {#sec-h18-flattening-higher-cells}

**Mechanism.** Natural isomorphisms become route-equivalence flags, modifications become untyped
coherence records, alternative composites become shortest-path choices, and multiple structures
become separate nodes. The damage is deferred: monoidal, derived, stack-theoretic and higher-limit
constructions cannot interpret propositionally truncated data without changing its meaning.
**Guard.** Coherence data is carried as cells of the ambient structure with their type; a
comparison recorded as a boolean, a flag or an untyped record is a defect unless the truncation is
deliberate and named at the site.

## H19 — Phase myopia {#sec-h19-phase-myopia}

**Mechanism.** The current issue or first worked example is optimised without tracing what later
phases require: a one-categorical foundation because the first computation is finite algebra, a
bespoke matrix object because the first lattice computation takes a matrix, strict equations
because the first axioms are associative and commutative.
**Guard.** A foundation or interface is admitted only together with the phase statement — what the
later phases require of it and which of their instances it must already accept — and a choice
justified by the size of the first example is recorded as a defect rather than a simplification.
