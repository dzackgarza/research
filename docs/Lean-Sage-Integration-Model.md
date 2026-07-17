# Lean–Sage Integration Model

The ratified layering and working discipline for the alignment work, distilled from the [#251](https://github.com/dzackgarza/research/issues/251) record (2026-07-16/17; the A/B/C model is user-ratified and canonical).
This page is the implementation map from the mathematical presentation to code — implementation vocabulary (manifest, conformance, dispatch, realization owner) is legal here and only here (style-guide P6).

## Layering

**Lean/Mathlib owns mathematical meaning** — definitions, hypotheses, functoriality, coherence, and proof status.
**Sage owns executable realization** — representations, dispatch, method placement, runtime validation, algorithms.
Neither side invents a second common ontology.
The bridge is narrow: a generated manifest tying real Lean declarations to the facts Lean cannot verify itself (Sage realization owners, backend trust status, genuinely unresolved gaps).
It never duplicates Lean's namespace, term language, or instance system in a parallel ID/reference/claim schema.

Lean is a **coherence engine, not a standardness oracle**: kernel checks, tethers, equivalences, and green builds establish internal consistency, never that the definitions model the intended mathematics.
Only anchors into Mathlib and the literature can fail against the world — the anchors are the work.

## The A/B/C model — the DSL is a routing layer, never a definitional layer

For every notion a contribution needs:

- **(A) Mathlib provides it** → wrap/decorate slightly; the DSL holds only the declaration of how the object sits in its conservative functor graph (distinguished routes, realization owners, conformance).
  The default and overwhelming majority (≈85–90% of surveyed rows).

- **(B) Mathlib lacks it** → make the honest upstream contribution by proxy in the shipped `ForMathlib/` layer — establish the category, its formal properties, its property-defined subcategories, and the needed functors — then **loop back to (A)**. The DSL never ends up holding the definition.

- **(C) escape hatch, user-approved only** → if (B) genuinely fails repeatedly: (B) with `sorry`s — statements still kernel-checked, proofs pending — isolated in a Synthetic layer, carrying a written account of why the sanctioned route failed.
  Expected instances are sorry'd *statements of literature theorems* needed as hypotheses (the indefinite genus + spinor decision theorem; Nikulin surjectivity/uniqueness), not failed definitions.

**(C) is a queue, not a resting state.** Membership in `Synthetic/` *is* the queue annotation; the ideal end-state is `Synthetic/` empty.
Two draining queues, one direction: Synthetic → ForMathlib → Mathlib.

**The test for what moves to Lean:** any claim of the form "this square commutes / this family is natural / this is a limit / these two routes agree / this action is free and transitive" is proof-shaped.
In Python it can only be spot-checked (a naturality check on three sample objects passes on many non-natural families), so its statement belongs in Lean; Sage keeps executable conformance.

**Deferral is forbidden.** "Developed later" without an assignment violates the model: the disposition for missing theory is (B) statement-level definitions now, with (C)-queued proofs visible in the cop-out report — never an unassigned "later."
Do not defer a foundational defect because remaining tasks are mechanical; exporting a malformed foundation multiplies the damage.

## The ForMathlib layer contract

Per file: imports Mathlib only (mechanically gated); follows Mathlib's organization; names the intended upstream target per declaration; graduation = contribute upstream, then delete-and-realias locally.
Prefer self-contained files — intra-ForMathlib imports couple graduation order (upstream PRs go per-file); note unavoidable coupling in the layer-contract docstring.

Module layers, with import direction mechanically enforced: **Foundation** (thin Mathlib-facing facade — categories, functors, naturals, object properties, full subcategories are real Mathlib constructions, never a parallel categorical kernel or resolver), **ForMathlib** (upstream-destined missing theory), **Categories** (the corpus, derived from the standard presentation), **Manifest** (the narrow bridge).

Cataloguing is mathematical research, not inventory transcription: the presentation is forward-looking toward schemes, sheaves, stacks, opposites, arrow categories, functor categories, hom-categories, coherence data, and 2-categorical constructions, expressed as real Lean declarations — the rejected alternative was administrative machinery (dimension tags, placement-sort enums, a bespoke concept-reference language).

## Registry semantics

The manifest's gap rows follow the recording discipline in [Contribution Guidelines §5](Contribution-Guidelines.md): a `pending`/no-analog row is a negative claim about Mathlib, admissible only with search evidence.
The standing prior the registry encodes: every notion here is standard mathematics with an upstream anchor at ingredient level — absence of a single prepackaged name is not a gap (compositional constructions count), and a wrong alias at the root of the single auditable source is poison where a pending row is honest.

The per-contributor workflow — the authoring checkpoint, dictionary-first generation, Lean authoring rules, and correction handling — lives in the [Contribution Guidelines](Contribution-Guidelines.md); the failure modes it guards are catalogued in the [Design Hazard Ledger](Design-Hazard-Ledger.md).

## Cop-out visibility

A **report, never a gate**, makes every common Lean cop-out visible tree-wide: `sorry`/`admit` per declaration with queue annotation and no-go link; axioms beyond `propext`, `Classical.choice`, `Quot.sound`; `native_decide`; `unsafe`/`implemented_by`/ `extern`; `partial def`. The hard gate (exact axiom count, prohibited tokens) stays scoped to the non-Synthetic layers, red-on-violation; the report covers everything, so the (C) queue is always enumerable without blocking first-round work.
