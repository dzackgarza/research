# Design Hazard Ledger

A recorded ledger of hazards observed in this program's formalization and design work — each one actually occurred, was corrected, and now has a standing guard.
Entries are forward-facing: the point of each row is the **guard** — the rule that makes the hazard detectable or inexpressible — not the history.
New contributions are checked against the guards, which live in the [Contribution Guidelines](Contribution-Guidelines.md), [Categorical Presentation Principles](Categorical-Presentation-Principles.md), and the [Mathematical Language Style Guide](Mathematical-Language-Style-Guide.md).

Provenance for all entries: the [#251](https://github.com/dzackgarza/research/issues/251) record (2026-07-16/17). One meta-observation covers the whole ledger: every corrected defect had the same form — *a bespoke invention should have been a named standard construction*.

## H1 — Code-as-invariant {#sec-h1-code-as-invariant}

**Mechanism.** Work starts from "this declaration exists; what mathematics justifies it?"
instead of deriving the standard mathematics and deciding which declarations survive.
Mathematics becomes post-hoc justification for preserving code.
**Guard.** Contribution Guidelines step 1 (derive first, admit declarations second); right-to-exist decided before any identification is proved.

## H2 — Proof-carrying laundering {#sec-h2-proof-carrying-laundering}

**Mechanism.** A checked witness relating a local declaration to upstream mathematics is treated as legitimizing the declaration.
A proof that a bespoke accessor agrees with the standard invariant is evidence the accessor is redundant or misplaced — the proof can certify the defect more strongly.
**Guard.** Identification is never admission: right-to-exist first ([Contribution Guidelines](Contribution-Guidelines.md)); level check (a declared item generable one level down is a defect).

## H3 — Capability-to-structure promotion {#sec-h3-capability-to-structure-promotion}

**Mechanism.** Backend requirements are promoted into mathematical structure: enumeration machinery becomes an "enumeration-equipped category", a chosen basis becomes object data, computational presentations become homes of the invariants they evaluate.
**Guard.** Witness discipline (style guide [P2](Mathematical-Language-Style-Guide.md#p2): witness is a declared type; a presentation is never the home of the invariant it evaluates); layer quarantine ([P6](Mathematical-Language-Style-Guide.md#p6)).

## H4 — Exact-name fixation {#sec-h4-exact-name-fixation}

**Mechanism.** When no single upstream constant names a construction, the mathematics is experienced as missing, producing false gaps and false contribution opportunities.
Standard mathematics is frequently compositional.
**Guard.** Gap epistemics ([Integration Model](Lean-Sage-Integration-Model.md)): a gap claim is a negative claim requiring search evidence with nearest notions distinguished; compositional expressions count as matches.

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
**Guard.** A mathematical correction invalidates downstream classifications until the presentation is re-derived ([Contribution Guidelines](Contribution-Guidelines.md)); one counterexample indicts the classifier.

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
**Guard.** Name every section (style guide [P4](Mathematical-Language-Style-Guide.md#p4)); unnamed structure-reference is grep-detectable red.
The name goes on the lift, never on the classifier — a classifier node per structure is the proliferation hazard one level up.

## H13 — Authority laundering {#sec-h13-authority-laundering}

**Mechanism.** Vocabulary with a rigorous definition in a literature the intended auditor does not command (model theory, type theory, PL theory) reads as authoritative but is unfalsifiable by the audience the artifact serves — worse than visible coinage.
**Guard.** Audience-relative admissibility (style guide [P1](Mathematical-Language-Style-Guide.md#p1), Class A); the corpus boundary is which literature, not how well-known.

## H14 — Stale-prior convention claims {#sec-h14-stale-prior-convention-claims}

**Mechanism.** Agents and automated reviewers assert a dependency's names or conventions from priors ("Mathlib's standard namespace is X") that contradict the pinned checkout; acting on them breaks building usage.
Recorded exemplar: a reviewer's "standard namespace is `Basis`, not `Module.Basis`" and "`Basis.toDual` is a `LinearEquiv`" — the live tree has `Module.Basis`, and `toDual` is a `LinearMap` whose equivalence is `toDualEquiv`. **Guard.** The pinned checkout is the naming authority for everyone; every convention claim carries the verification burden before acting (Contribution Guidelines, Lean style rules).

## H15 — Supervision inversion {#sec-h15-supervision-inversion}

**Mechanism.** After repeated corrections or forced stops, autonomy is *increased* ("the remaining work is mechanical") — exporting a malformed foundation multiplies the damage precisely when self-monitoring has demonstrably failed.
**Guard.** Repeated corrections escalate to specification review and tighter supervision; foundational defects are never deferred because remaining tasks are mechanical ([Contribution Guidelines](Contribution-Guidelines.md)).
