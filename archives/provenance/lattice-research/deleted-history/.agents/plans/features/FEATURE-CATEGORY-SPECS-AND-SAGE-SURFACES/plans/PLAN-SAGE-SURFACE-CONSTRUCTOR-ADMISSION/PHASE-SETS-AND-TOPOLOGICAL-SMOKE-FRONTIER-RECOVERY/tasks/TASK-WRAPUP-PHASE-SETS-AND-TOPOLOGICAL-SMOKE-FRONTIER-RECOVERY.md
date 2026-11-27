---
id: TASK-WRAPUP-PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
trackerStatus:
  type: task
parents:
  - '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
dependsOn:
  - '[[TASK-01KQN9J3X04R2PWJADC8B4EF9A-FIX-SETS-ROOT-CONTAINMENT-REFINED-CONSTRUCTOR-RICHCMP-PRIMES-ITERATION-R]]'
  - '[[TASK-01KQN9YGCD23ZSZDA3VT3BJ92E-IMPLEMENT-REALSET-NAMED-CONSTRUCTORS-AND-SMOKE-RECOVERY-THROUGH-AMBIENT]]'
  - '[[TASK-01KQN9YGCE6EHG6Q2575YQGNR8-IMPLEMENT-IMAGESETS-CONSTRUCTION-CATEGORY-AND-SMOKE-AMBIENT-LIFT-RETRACT]]'
  - '[[TASK-01KQN9YGCHDRNXNEYEH2P134JD-IMPLEMENT-TOPOLOGICAL-RING-AND-FIELD-REFINEMENTS-FOR-TOPOLOGY-BEARING-RI]]'
  - '[[TASK-01KQN9YGCR3DR59Q6DHNRKTV0C-RESEARCH-SAGE-PRIMES-DOCUMENTATION-AND-INSTALLED-SOURCE-VERSION-SKEW-BEF]]'
  - '[[TASK-1777748120612-YVA6FX-REMOVE-STRICT-SUPERCATEGORY-LEAKS-FROM-IMAGE-SET-AND-SCHEMATIC-SET-CONSTRUCTORS]]'
title: Phase wrap-up — planning cleanup, skill updates, and card status audit
status: complete
priority: high
description: Wrap-up and cleanup for phase PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY. Audit card statuses, run
  meta-review on completed work, update skills and memories, and organize git history.
successCriteria:
- All cards in this phase have accurate and up-to-date statuses
- A research-planning-cleanup scan has been run on all recently-completed cards in this phase
- Any suspicious cards have been kicked back with specific, actionable feedback
- Local skills and IWE memories have been updated with lessons learned during this phase
- Git commits from this phase are reviewed and organized into a coherent narrative milestone
- The Research Log below documents what was found and what was done
- All cards in feature tree verified complete/done, decided, or superseded
- Version tag created on merge commit
- Completed feature tree moved to `plans/features/completed/`
- Feature branch created for next feature if applicable
tags:
  - FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
  - PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
  - PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
---

# Phase Wrap-Up: Planning Cleanup and Card Status Audit

This task runs after all other tasks in this phase are complete. It ensures that
the phase closes cleanly: card statuses are accurate, completed work has been
meta-reviewed for quality, and process improvements are captured.

Do NOT execute this task while sibling tasks are still `in-progress` or
`needs-agent-review`. This is a gatekeeper task — it verifies that work claimed as
complete was substantively done.

## Procedure

### 1. Card Status Audit

- [ ] List all cards in this phase and verify each has the correct status.
- [ ] Cards marked `complete` or `done` must have a Review Log with concrete
  evidence (file paths, line numbers, test output, source cross-checks).
- [ ] Cards still in `needs-agent-review` or `in-progress` must be accurate — if a
  card was abandoned, set it to `blocked` with a `blocked_reason`.
- [ ] Cards in `unstarted` with unmet `dependsOn` edges should stay `unstarted`;
  do not mark them `blocked` for planned upstream dependencies.

### 2. Meta-Review (Research Planning Cleanup)

Load `research-planning-cleanup` and run a scan on all cards in this phase
that are `complete` or `done`:

- [ ] Check each completed card for Jerry-behaviour signals:
  - Zero negative findings across all review gates
  - No line numbers or code excerpts in the review log
  - No external source cross-checks (claims verified only against the card body)
  - Generic gate justifications that could apply to any card
  - Reviewer and implementer share the same model family
- [ ] Spot-check at least one evidence claim per suspicious card:
  - If the review cites a commit hash, open that commit and verify the claim
  - If the review claims a source was checked, open the source
  - If the review claims a test passed, run the test
- [ ] For any suspicious card, kick back with `status: revision-required` and a
  dated Review Log entry documenting:
  - Which Jerry signal was triggered
  - What the spot-check found (quote the evidence and the actual content)
  - What concrete evidence would satisfy re-review
- [ ] If three or more cards show the same shallow-review pattern, flag the batch
  in this task's log and escalate to a phase-level note. Do not kick back all
  of them individually.

### 3. Skill and Memory Updates

- [ ] Review the work done in this phase. Identify any process improvements,
  discovered conventions, environment quirks, or mathematical insights that
  should survive context loss.
- [ ] Update relevant repo-local skills in `.agents/skills/` if the phase
  revealed gaps in existing skill coverage or incorrect guidance.
- [ ] Add durable memories via IWE for: decisions too small for a decision
  card, constraints discovered during the phase, non-obvious environment
  findings, current state notes that would help a future agent resume work.
- [ ] Prune stale IWE memories that have been superseded by work done in this
  phase. Replace, don't accumulate.

### 4. Git Milestone Organization

- [ ] Review `git log` for commits created during this phase.
- [ ] Identify the logical grouping: does the commit sequence tell a coherent
  story? Are there orphan commits that should be noted?
- [ ] If there are checkpoint or work-in-progress commits that can be logically
  grouped, add a milestone note in this task's log recording the commit range
  and what the group accomplished.
- [ ] Do NOT rebase, squash, or rewrite history. This is documentation, not
  history surgery.


## Feature Release

This is the final phase of **Category Specs and Sage Surfaces**. Before marking this feature
complete, verify:

### Versioned Release

- [ ] Create a version tag on the merge commit: `git tag -a vX.Y.Z -m "Category Specs and Sage Surfaces complete"`
- [ ] Run `just plan-validate` and confirm all cards in this feature are `complete`/`done`, `decided`, or `superseded`
- [ ] Move the completed feature tree to `plans/features/completed/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/`
- [ ] Update `plans/card-progress-report.md` via `just plan-progress-report`

### Feature Branch for Next Feature

If a subsequent feature is ready to begin development:

- [ ] Create a feature branch: `git checkout -b feature/next-feature-name`
- [ ] Do NOT attempt to back-organize existing commits onto the feature branch.
  The feature branch is for NEW work going forward.
- [ ] Record the branch name and purpose in the next feature's card body.
- [ ] If work has already started on `main` for the next feature, note it in the
  feature card and commit to the branch convention for subsequent commits.


## Research Log

Document findings from the card status audit, meta-review scan, skill/memory
updates, and git organization here.

### Card Status Audit

<!-- List each card and its verified status -->

### Meta-Review Findings

<!-- Document suspicious cards found, spot-checks performed, and kickback decisions -->

### Skill and Memory Updates

<!-- Record skills updated and IWE memories added/pruned -->

### Git Milestone Notes

<!-- Record commit ranges and their logical grouping -->
