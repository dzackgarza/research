---
id: TASK-01KQN9YGCQA3E2Y2RAMA2EHZPR-RESEARCH-UPSTREAM-SAGE-SUPPORT-OR-ISSUES-FOR-Q-ADIC-UNRAMIFIED-EXTENSION
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Research upstream Sage support or issues for q-adic unramified extensions with split
  lattice precision caps
status: complete
priority: high
description: Rings mapping records constructor namespace decisions, split p-adic and q-adic
  precision routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
  lattice-precision gaps.
successCriteria:
- The research result cites the exact sources searched and separates source evidence from
  inference.
- 'Negative findings use the repository five-field format: Searched, Found, Conclusion, Confidence,
  Gaps.'
- Any admitted design consequence is linked to a spec-work or design-decision item rather
  than buried in prose.
- For q-adic precision items, preserve the five-field negative finding format when updating
  evidence.
- For topological ring work, check both ring and topological-space category membership.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
---
# Research upstream Sage support or issues for q-adic unramified extensions with split lattice precision caps
## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
lattice-precision gaps.

## Source Provenance

- `category_specs/rings/docs/MAPPING.md`
- Original migrated line: `Research upstream Sage support or issues for q-adic unramified extensions with split lattice precision caps from category_specs/rings/docs/MAPPING.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- ZqWithPrecisionCaps and QqWithPrecisionCaps are retained admitted split names but remain deferred frontiers because installed Sage lacks a working unramified q-adic extension path with split lattice caps.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Acceptance Criteria

- [x] The research result cites the exact sources searched and separates source evidence from inference.
- [x] Negative findings use the repository five-field format: Searched, Found, Conclusion, Confidence, Gaps.
- [x] Any admitted design consequence is linked to a spec-work or design-decision item rather than buried in prose.
- [x] For q-adic precision items, preserve the five-field negative finding format when updating evidence.
- [x] For topological ring work, check both ring and topological-space category membership.

## Research Result

Source evidence:

- Sage 10.8 p-adics docs for `factory` document `Zq`/`Qq` as unramified q-adic
  constructors with integer precision examples and precision models capped-relative,
  capped-absolute, fixed-modulus, and floating-point; they do not document q-adic
  lattice-cap or lattice-float constructors.
- Sage 10.8 p-adics docs for `padic_base_leaves` document `pAdicRingLattice` and
  `pAdicFieldLattice` as base `Zp`/`Qp` lattice-precision parents whose `prec` is a
  pair `(relative_cap, absolute_cap)`.
- Sage 10.8 p-adics docs for `generic_nodes` document `PrecisionLattice`,
  `precision_cap_relative()`, and `precision_cap_absolute()` for base lattice p-adics.
- Sage `develop` raw `sage/rings/padics/factory.py` imports `pAdicRingLattice` and
  `pAdicFieldLattice`, but its `ext_table` has unramified extension entries only for
  capped-relative, capped-absolute, fixed-modulus, and floating-point bases.
- Sage `develop` raw `factory.py` still coerces `Zq`/`Qq` precision with
  `prec = Integer(prec)` in the q-adic constructor path, while `get_key_base` handles
  pair precision for base `Zp`/`Qp` lattice constructors.
- The stale `sagetrac-mirror` branch for issue `#25915` and draft PR `#34993`
  (`roed314/sage:general-extensions`) were also searched. They add relative/general
  p-adic extension machinery, but the searched `factory.py` branches still do not add
  unramified lattice extension leaves keyed by `pAdicRingLattice` or
  `pAdicFieldLattice`.

Repository and upstream issue evidence:

- Sage issue `#23505` is the closed base p-adic lattice-precision implementation
  ticket. It describes the precision datum as a lattice attached to the parent and
  implemented by `PrecisionLattice`.
- Sage issues `#24809` and `#30692` remain open lattice-precision follow-up/bug
  tickets, which supports treating lattice precision as an experimental/incomplete
  upstream surface even before q-adic extension support.
- Sage issue `#25915` is open and targets unramified extensions of arbitrary p-adic
  fields. Its public body does not claim lattice-precision q-adic support.
- Sage issue `#28466` and draft PR `#34993` are open general p-adic extension work.
  PR `#34993` is draft/needs-work and its searched branch still does not provide the
  q-adic split lattice-cap constructor route needed here.

Negative finding:

- Searched: Sage 10.8 p-adics docs for `factory`, `generic_nodes`, and
  `padic_base_leaves`; Sage `develop` raw source for `factory.py`,
  `padic_extension_leaves.py`, `padic_base_leaves.py`, and `generic_nodes.py`; GitHub
  issue/PR searches for `Zq Qq lattice-cap`, `pAdicLatticeGeneric unramified
  extension`, `lattice precision q-adic`, `pAdicRingLattice pAdicFieldLattice
  extension`, and `PrecisionLattice`; issues `#23505`, `#24809`, `#25915`, `#28466`,
  `#30692`; draft PR `#34993`; the stale `sagetrac-mirror` branch for `#25915`; and
  PR `#34993` branch `roed314/sage:general-extensions`.
- Found: base `Zp`/`Qp` lattice precision is documented and implemented; q-adic
  `Zq`/`Qq` docs and source still route precision as an integer and do not expose
  split lattice-cap q-adic constructors. Public upstream work exists for base lattice
  precision, arbitrary unramified p-adic extensions, and general extensions, but the
  searched issue bodies and branches do not provide a usable unramified q-adic
  extension parent with split relative/absolute lattice precision caps.
- Conclusion: inference -- the existing mapping is still correct: retain
  `ZqWithPrecisionCaps(...)` and `QqWithPrecisionCaps(...)` as admitted but deferred
  frontier names, and make any implementation body report the Sage gap instead of
  passing through to a broken constructor path.
- Confidence: High for public Sage docs, current `develop`, public GitHub issue/PR
  metadata, and the searched public branches.
- Gaps: GitHub issue comments could not be loaded through `gh issue view --comments`
  because GitHub's classic-project GraphQL field failed; private branches and
  non-GitHub developer discussions were not searched.

Design consequence:

- No new decision card is needed. The consequence is already represented by
  `[[TASK-01KQN9YGCJ26WJ2044DVNVNE87-IMPLEMENT-Q-ADIC-LATTICE-PRECISION-CAP-CONSTRUCTORS-AS-EXPLICIT-BLOCKED]]`
  and by the retained deferred names in `[[SPEC-MAPPING-RINGS]]`.
- This is not topological-ring implementation work. No ring/topological-space category
  membership changed; the topological inheritance rule remains the mapping table row
  for `Zp(...)`, `Qp(...)`, `Zq(...)`, `Qq(...)`, and named split precision routes in
  `[[SPEC-MAPPING-RINGS]]`.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06: Completed upstream Sage docs/source/issue/PR research. Confirmed public
  Sage sources still lack a q-adic unramified extension route with split lattice
  precision caps; preserved the deferred admitted names and linked the implementation
  gap card.

## Review Log

### Review 2026-05-07 (Codex)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3
Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and
Compliance
**Gates failed:** None
**Outcome:** reviewed; leave `status: needs-review` for human acceptance rather than
agent-side closure.

- Gate 1: The card grounds the constructor names and q-adic lattice-precision gap in
  `[[SPEC-MAPPING-RINGS]]`, Sage p-adic/q-adic docs/source, and the linked upstream
  issue/PR evidence. The source evidence distinguishes base `Zp`/`Qp` lattice precision
  from q-adic unramified extension constructors.
- Gate 2: All task acceptance criteria are satisfied: exact sources are listed, the
  negative finding uses the required five-field format, and the admitted design
  consequence is linked to
  `[[TASK-01KQN9YGCJ26WJ2044DVNVNE87-IMPLEMENT-Q-ADIC-LATTICE-PRECISION-CAP-CONSTRUCTORS-AS-EXPLICIT-BLOCKED]]`
  plus `[[SPEC-MAPPING-RINGS]]`.
- Gate 3: No code, spec, or smoke surface is weakened by this research result. The
  review checked the clean staged and unstaged diffs before this log entry; the result
  preserves the admitted `ZqWithPrecisionCaps(...)` and `QqWithPrecisionCaps(...)`
  names as deferred Sage-gap frontiers instead of shrinking the ideal interface.
- Gate 4: Refreshed public upstream evidence on 2026-05-07 is consistent with the
  existing finding: Sage issues `#25915`, `#24809`, `#28466`, and `#30692` remain open,
  PR `#34993` remains open/draft/needs-work, issue `#23505` remains the closed base
  lattice-precision implementation ticket, and Sage `develop` still has no unramified
  extension lattice parent route in the q-adic extension table.
- Gate 5: The conclusion is scoped correctly as an upstream-support research finding,
  not a theorem or implementation claim. It supports retaining mathematically meaningful
  split q-adic lattice-cap constructor names while treating current Sage realization as
  a deferred implementation gap.
- Gate 6: The review prose avoids smoke-driven spec weakening, records sources and
  inference separately, and keeps the blocker semantics path-local rather than treating
  this deferred implementation surface as a global phase blocker.

### Review 2026-05-07 (opencode-go subagent)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3
Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and
Compliance
**Gates failed:** None
**Outcome:** all gates pass; leave `status: needs-review` for human acceptance per
category-spec policy (never mark native items done without human approval).

- **Gate 1 (Definition Grounding):** Checked each definition against canonical
  sources. The constructor names `ZqWithPrecisionCaps`/`QqWithPrecisionCaps` are
  grounded in `SPEC-MAPPING-RINGS.md` lines 214 and 385 (deferred admitted names).
  Installed implementation at `category_specs/rings/__init__.py` lines 1297-1329 and
  1464-1497 confirms the constructors exist with project vocabulary. The Sage gap
  evidence cites exact paths: Sage 10.8 p-adics docs (`factory`, `generic_nodes`,
  `padic_base_leaves`), Sage `develop` `factory.py` line 74 (`prec = Integer(prec)`
  coercion in q-adic path vs. `get_key_base` pair handling), `ext_table` entries
  (capped-relative/capped-absolute/fixed-modulus/floating-point only — no lattice
  extension leaves). GitHub issues `#23505`, `#24809`, `#25915`, `#28466`, `#30692`
  and PR `#34993` statuses are cited. Topological ring and matrix-ring ownership
  claims are grounded in `SPEC-MAPPING-RINGS.md` lines 441-477 and 332-356
  respectively. No raw Sage type leaks or ungrounded definitions found.

- **Gate 2 (Acceptance Criteria):** Verified all 5 acceptance criteria independently:
  (1) Exact sources searched are listed in lines 61-94 and 98-105; source evidence
  vs. inference separation in lines 59-94 (evidence) vs. lines 112-115 (Conclusion
  explicitly labeled "inference"). (2) Five-field negative finding format at lines
  96-120: Searched, Found, Conclusion (labeled inference), Confidence, Gaps. (3)
  Design consequence at lines 122-130 links to
  `TASK-01KQN9YGCJ26WJ2044DVNVNE87-IMPLEMENT-Q-ADIC-LATTICE-PRECISION-CAP-CONSTRUCTORS-AS-EXPLICIT-BLOCKED`
  (verified on disk) and `SPEC-MAPPING-RINGS`. (4) Q-adic precision negative finding
  at lines 96-120 uses five-field format. (5) Topological ring check at lines 127-130
  explicitly states no topological work was done and confirms the existing rule.

- **Gate 3 (Spec-Weakening):** Ran `git diff` and `git diff --cached` for all spec
  files (`SPEC-MAPPING-RINGS.md`, `MAPPING.md`, `SAGE_INVENTORY.md`) and the task
  file itself — no changes. The task file is committed (commit `01cf23a`). No
  abstract methods deleted, no constructor obligations removed, no smoke assertions
  narrowed, no obligations moved without replacement owner, no Sage-gap-driven
  interface shrinkage. The deferred names `ZqWithPrecisionCaps`/`QqWithPrecisionCaps`
  are preserved and their implementation raises an explicit `AssertionError` with a
  clear message about the Sage gap rather than a broken pass-through.

- **Gate 4 (Gradient/Backsliding):** Checked all 6 baseline artifact categories:
  (1) Decision cards under `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/`
  — 12 files reviewed; none address q-adic lattice precision (they cover algebra
  involution, Nikulin invariants, Picard group, module sidedness, etc.) so no
  reversal risk. (2) Previously approved specs — `SPEC-MAPPING-RINGS.md` unmodified
  by this task. (3) Previously passing smokes — no smoke changes from this card;
  companion implementation task explicitly preserves frontier labels. (4) Previously
  resolved TODOs — none reintroduced. (5) Git log (`bce8eb2`, `752533a`, `4512be8`,
  `c4bca6a`, `b215cfe`) shows no prior q-adic precision invariant that this card
  reverses. (6) Approved phase card `PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES.md`
  unchanged. Gradient is non-negative in all dimensions.

- **Gate 5 (Mathematical Correctness):** The research claim — "installed Sage lacks a
  working unramified q-adic extension path with split lattice caps" — is supported by
  cited evidence: Sage 10.8 docs document only integer precision for `Zq`/`Qq`; Sage
  `develop` `factory.py` coerces `prec = Integer(prec)` in q-adic path while
  `get_key_base` handles pair precision only for base `Zp`/`Qp`; `ext_table` entries
  lack lattice extension leaves; issues `#24809`/`#30692` remain open (lattice
  precision incomplete); issues `#25915`/`#28466`/PR `#34993` don't yet provide the
  needed route. The conclusion preserves mathematically meaningful split-cap names as
  deferred. Confidence: High — appropriate for public-source research. Gaps honestly
  stated (GitHub comment loading failure, private branches not searched). Escalation
  tier is exploratory/research, not GOAL-discharge.

- **Gate 6 (Style and Compliance):** The card body follows Nimbalyst task format
  (frontmatter with id/status/parents/dependsOn/tags, summary, source provenance,
  context, acceptance criteria, research result with separated evidence/inference,
  negative finding, design consequence, dependencies, work log, review log). No raw
  `ConditionSet`, no variadic option-bag constructors, no AI-slop patterns (prose is
  specific with exact source paths, issue numbers, and code observations). No code
  changes to audit for import hygiene or type annotations.
