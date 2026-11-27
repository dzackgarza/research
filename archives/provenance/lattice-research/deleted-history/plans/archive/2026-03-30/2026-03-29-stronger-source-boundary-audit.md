# Stronger-source boundary audit

## Goal

- Current defect/state: the broader explicit-family source audit is complete, but two
  stronger-source wording layers remain unresolved in canonical repo prose: the exact
  stronger Coolidge all-ten-from-any-nine theorem paraphrase and the primary source
  behind Dolgachev's archived `J. Thas` uniqueness attribution.
- Target state: the repo has one narrow active plan for resolving or explicitly fencing
  those stronger-wording layers, while keeping weaker primary-supported claims stable.
- Why this matters: the repo now knows more than it did before, but it still must not
  let archived secondary support or paraphrased theorem language drift upward into false
  primary verification.

## Constraints

- Required:
  - Keep `REFERENCES.md` and `GAPS.md` canonical for support levels.
  - Preserve the current splits already established in
    `reports/task1_1_family_report_audit.md` and
    `reports/desargues_thas_source_trace.md`.
  - Distinguish direct primary support, archived secondary support, unresolved wording,
    and unresolved full-text explicit-formula claims.
- Forbidden:
  - No upgrade of the stronger Coolidge theorem wording without direct primary-text
    isolation.
  - No upgrade of the archived `J. Thas` uniqueness attribution to primary support
    without a directly inspected underlying source.
  - No broad cleanup drift.

## Scope

- Included targets:
  - `PLAN.md`
  - `GAPS.md`
  - this plan file
  - `reports/task1_1_family_report_audit.md`
  - `reports/desargues_thas_source_trace.md`
  - `REFERENCES.md`
- Excluded for this slice:
  - new Task 5.1 computations
  - repo-native Task 1.1 construction changes
  - Lean work
  - general repo debris cleanup

## Phase 0: Close the broader source-audit thread

Goal: move the completed explicit-family source-audit plan out of the active slot.

- Location: `PLAN.md`, prior explicit-family source-audit plan
- Description:
  - mark the broader source-audit plan completed;
  - make the stronger-source boundary audit the active thread.
- Dependencies: none.
- Acceptance criteria: `PLAN.md` no longer lists
  `plans/2026-03-29-explicit-family-source-audit.md` as active.
- Validation: inspect
  `git diff -- PLAN.md plans/2026-03-29-explicit-family-source-audit.md plans/2026-03-29-stronger-source-boundary-audit.md`.

## Phase 1: Resolve or fence the stronger wording layers

Goal: determine whether either stronger wording layer can be upgraded further, or must
remain explicitly unresolved.

- Location: `reports/task1_1_family_report_audit.md`,
  `reports/desargues_thas_source_trace.md`, supporting source notes as needed
- Description:
  - inspect any additional direct source material for the stronger Coolidge theorem
    wording;
  - inspect any additional source trail clarifying the archived `J. Thas` uniqueness
    attribution;
  - if no stronger evidence is found, keep the wording explicitly fenced.
- Dependencies: Phase 0.
- Acceptance criteria: each stronger wording layer is either upgraded with direct source
  support or left explicitly unresolved with evidence-linked negative findings.
- Validation: updated report language cites inspected source text or uses the required
  five-field negative-finding format.

## Phase 2: Normalize canonical support language

Goal: keep canonical repo files aligned with the strongest evidence actually in hand.

- Location: `GAPS.md`, `REFERENCES.md`, any canonical note touched by Phase 1
- Description:
  - refresh canonical support levels after the stronger-wording audit;
  - keep literature-backed examples, archived secondary attributions, and repo-native
    constructions clearly separated.
- Dependencies: Phase 1.
- Acceptance criteria: no canonical file overstates the support level of the stronger
  Coolidge or `J. Thas` wording layers.
- Validation: inspect scoped diffs and grep for stale overclaiming language.

## System-Level Validation

- `PLAN.md` points at the stronger-source boundary audit as the active thread.
- Canonical files still distinguish primary support, archived secondary support, and
  unresolved stronger wording.
- The repo does not cite an explicit full-text polynomial family unless one is directly
  inspected.

## Risks / Rollback

- Risks:
  - OCR or archived text may tempt over-reading of theorem wording.
  - Secondary attributions may be mistaken for primary support.
- Mitigations:
  - require direct quotation or page-image confirmation before any upgrade;
  - treat missing underlying sources as unresolved, not implicitly verified.
- Rollback path:
  - if a stronger wording upgrade proves too aggressive, restore the previous explicit
    unresolved wording in a follow-up commit.

## Stop Rules

- Do not upgrade the stronger Coolidge statement without isolating the exact primary
  text.
- Do not upgrade the archived `J. Thas` uniqueness layer beyond secondary support
  without a directly inspected underlying source.
- Do not broaden into explicit-equation searches until these wording boundaries are set.

## Execution Progress

### Phase 0

- [x] Close the broader explicit-family source-audit thread in the directive layer

### Phase 1

- [x] Resolve or explicitly fence the stronger Coolidge theorem wording
- [x] Resolve or explicitly fence the archived `J. Thas` uniqueness attribution

### Phase 2

- [x] Normalize canonical support language after the stronger-source audit

### Quality Gates

- [x] A narrower literature-first follow-up thread is the active plan
- [x] Stronger wording layers are source-backed or explicitly unresolved
- [x] Canonical prose still separates primary, archived secondary, and repo-native
  claims
