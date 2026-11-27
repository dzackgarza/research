# Explicit-family source audit

## Goal

- Current defect/state: repo reports now say the standard explicit-family routes for
  10-nodal rational sextics are mostly unsupported or retracted, but the directive layer
  still needs one active literature-first thread for verifying the surviving leads from
  primary sources.
- Target state: the repo has one narrow active plan for source-level verification of the
  remaining explicit-family leads, starting with Coolidge and the Thas attribution, and
  it records the safe fallback if those sources still cannot be verified.
- Why this matters: literature claims about explicit examples should be either primary-
  source verified or explicitly retired; letting them remain half-audited invites the
  same claim drift that previously affected Task 5.1.

## Constraints

- Required:
  - Keep `REFERENCES.md` and `audit/literature_claim_map.md` as the canonical citation
    spine for standard background.
  - Treat `reports/task1_1_family_report_audit.md` and
    `reports/desargues_thas_source_trace.md` as the current audited baseline.
  - Distinguish primary-source verification, secondary support, unsupported claims, and
    retracted claims.
- Forbidden:
  - No upgrading a claim from unsupported to verified without direct source inspection.
  - No presenting repo-native Task 1.1 examples as classical families unless a source is
    actually checked.
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
  - Lean formalization
  - general repo debris cleanup

## Phase 0: Close the Task 5.1 status-alignment thread

Goal: move the completed Task 5.1 prose-alignment work out of the active slot.

- Location: `PLAN.md`, `GAPS.md`, prior Task 5.1 status-alignment plan
- Description:
  - mark the Task 5.1 status-alignment plan as completed;
  - make the explicit-family source audit the active work thread.
- Dependencies: none.
- Acceptance criteria: `PLAN.md` no longer lists the Task 5.1 status-alignment plan as
  active.
- Validation: inspect
  `git diff -- PLAN.md GAPS.md plans/2026-03-28-task5_1-status-alignment.md plans/2026-03-29-explicit-family-source-audit.md`.

## Phase 1: Verify surviving primary-source leads

Goal: determine whether the surviving explicit-family leads can be upgraded from
unsupported to something stronger.

- Location: `reports/task1_1_family_report_audit.md`,
  `reports/desargues_thas_source_trace.md`, supporting literature notes as needed
- Description:
  - obtain direct access to Coolidge's cited theorem and any real source behind the Thas
    attribution, if possible;
  - record exact source language and downgrade or upgrade repo phrasing accordingly.
- Dependencies: Phase 0.
- Acceptance criteria: each surviving lead is explicitly classified using direct source
  evidence or a clearly scoped negative finding.
- Validation: updated report language cites exact inspected sources or uses the required
  five-field negative-finding format.

## Phase 2: Normalize repo phrasing for explicit families

Goal: make the literature status of explicit sextic families consistent across the repo.

- Location: `GAPS.md`, `REFERENCES.md`, any canonical claim/audit note touched by Phase
  1
- Description:
  - update repo wording so explicit-family claims match the new source audit;
  - keep repo-native Task 1.1 examples clearly separated from literature-backed
    examples.
- Dependencies: Phase 1.
- Acceptance criteria: no canonical file overstates the support level of Coolidge,
  Thas/Desargues, or comparable explicit-family claims.
- Validation: inspect scoped diffs and grep for stale unsupported phrasing.

## System-Level Validation

- `PLAN.md` points at the explicit-family source audit as the active thread.
- The support level of each surviving explicit-family lead is explicit and sourced.
- Canonical repo prose distinguishes literature-backed examples from repo-native ones.

## Risks / Rollback

- Risks:
  - primary sources may remain unavailable;
  - secondary summaries may tempt overclaiming.
- Mitigations:
  - treat inaccessible sources as unresolved, not as evidence;
  - prefer explicit negative findings over inferred verification.
- Rollback path:
  - if a claimed source turns out irrelevant, revert the wording in a follow-up commit
    and restore the prior unsupported classification.

## Stop Rules

- Do not upgrade a claim without direct source inspection.
- Do not broaden into new computational construction work in this thread.

## Execution Progress

### Phase 0

- [x] Close the Task 5.1 status-alignment thread in the directive layer

### Phase 1

- [x] Inspect Coolidge directly and downgrade the stronger theorem wording to the exact
  level supported by the primary text
- [x] Inspect the surviving Desargues/Thas primary-source lead directly and split the
  weaker existence claim from the stronger uniqueness wording

### Phase 2

- [x] Normalize canonical repo phrasing for explicit-family support levels, while
  keeping the remaining stronger-source wording explicitly unresolved

### Quality Gates

- [x] A literature-first source-audit thread is the active plan
- [x] Support levels are source-backed or explicitly unresolved
- [x] Canonical prose no longer blurs repo-native and literature-backed examples
