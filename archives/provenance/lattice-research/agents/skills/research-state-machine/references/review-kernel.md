# Research Review Kernel

This is the canonical review protocol for the research repo. It formalizes the Replay/Attack and Promote/Reject stages from the execution kernel into a structured gate-based procedure that gates every card moving from `needs-agent-review` or `needs-human-input` toward `complete`/`done`.

## Operational directive

When you encounter a card with `status: needs-agent-review`, it is your work. But it is
NOT work you can do inline in your own session.

**You must delegate review to a fresh-context subagent.** This is mandatory. The
subagent must never have been exposed to the implementation session, implementing
agent's chat history, or the implementing agent's rationalizations. Its only inputs
are: the card body, the work artifacts (at known paths), the baseline artifacts (at
known paths), and this review kernel.

What the subagent does: read the card, read the artifacts, apply the ordered gates
below, and produce a review log with concrete findings. Concrete means: for every
gate that passes, the subagent names the exact file, line, command, or source it
checked. "Looks good" is a gate failure.

The gates are a review scaffold, not the review. The subagent must use them to
make a judgment about the work. A finding is not valid merely because a literal
line changed or an artifact is absent; the subagent must reconcile the card,
current repo policy, baseline artifacts, and actual diff before deciding whether
the issue is material. If a lower-level artifact appears to violate a gate but a
higher-priority policy explicitly requires that change, the review must cite the
policy and not report the required change as a defect.

What you (the coordinator) do afterward: verify the subagent's review for
box-checking behavior. See the coordinator verification step at the end of the
Review procedure section. If the review is substantively wrong or shallow, reject it
and re-dispatch.

When you encounter a card with `status: needs-human-input`, first verify that the card
contains an exact question that repo policy, source grounding, the DAG, and the review
kernel cannot answer. If the status merely means "clean review is awaiting approval,"
"an agent is unsure," or "closing this would feel like a human signoff," it is
misclassified workflow debt, not a blocker. Reclassify or route it through the
agent-executable state machine instead of surfacing it as a human decision.

## Core invariant

A card is not complete because the implementing agent says so. It is complete only
when every required gate in the ordered protocol was checked and every finding was
resolved. Human approval is a separate requirement for parent-plan, feature,
program-level, or explicitly human-gated promotion; do not invent a universal final
human gate for ordinary source-grounded task cards.

## Status extension

Two statuses are added to the standard Nimbalyst status set:

- `revision-required` is added to `task`, `spec`, `feature`, and `phase` schemas to represent a card that passed preliminary review but needs rework.
- `needs-human-input` is added to `feature`, `spec`, `phase`, `task`, and `plan` schemas to represent a card that specifically requires human review (as distinct from `needs-agent-review`, which indicates agent-executable gate-based review).

```yaml
- value: revision-required
  label: Revision Required
  icon: replay
  color: '#f59e0b'
```

```yaml
- value: needs-human-input
  label: Needs Human Input
  icon: person
  color: '#8b5cf6'
```

A `blocked_reason` text field is added to the same schemas, placed immediately after the `status` field. When a card is `blocked`, this field records the specific gap and the prerequisite card.

Semantics:

| Status | Meaning |
|---|---|---|
| `unstarted` | No work has been done. May have planned dependencies in `dependsOn`; read the DAG to determine start-readiness. |
| `in-progress` | Work actively underway |
| `needs-agent-review` | Work completed; awaiting gate-based review (agent-executable protocol) |
| `needs-human-input` | Work cannot proceed because a specific human-only decision, policy choice, or evaluation remains |
| `revision-required` | Review found defects; rework required within this card's scope |
| `complete`/`done` | All gates passed; accepted |
| `blocked` | Work was attempted (or preflighted); a specific blocker was discovered that requires a different card to be resolved first. The blocker is recorded in `blocked_reason`. |

`needs-agent-review` and `needs-human-input` are sibling states reached from `in-progress`. The distinction is the kind of review required:
- `needs-agent-review`: the card is ready for the ordered gate-based protocol (Gates 1-6), which an independent agent can execute.
- `needs-human-input`: the card specifically requires human attention -- a design decision, policy choice, or evaluation that cannot be delegated to an agent. A clean review awaiting closure, parent acceptance, or an approval-shaped yes/no on policy-determined work is not human input.

`revision-required` is distinct from `unstarted` (no work was ever done) and `blocked` (discovered blocker requiring external resolution). A card cycling through `needs-agent-review → revision-required → in-progress → needs-agent-review` is normal. Repetitive cycles indicate a deeper design problem, which should be escalated to a plan review or decision card rather than reworked in isolation.

### Blocked vs. unstarted vs. dependsOn

The `dependsOn` DAG already encodes the dependency graph. An intelligent agent reads it and infers that a card with unsatisfied upstream dependencies should not be started. This does not require `status: blocked`.

| Situation | Status | Mechanically captured by |
|---|---|---|
| Card was never attempted; its upstream dependencies in `dependsOn` are unsatisfied | `unstarted` | `dependsOn` → read upstream `status` |
| Card was attempted; review or preflight discovered a concrete blocker requiring another card | `blocked` | `blocked_reason` + the blocker card (linked in `dependsOn`) |
| Card was attempted; review found defects fixable within this card's scope | `revision-required` | Review log findings in card body |
| Card should logically follow X (narrative ordering), but only needs X's abstract output, not X's completion | `unstarted` or `in-progress` | Phase containment + priority; no `dependsOn` edge |

Cards that are currently `blocked` solely because a planned upstream dependency is unfinished should be audited and moved to `unstarted` (if work was never attempted) or `revision-required` (if work was attempted and found to require upstream resolution). The `dependsOn` field suffices to prevent premature execution; the `blocked` status is reserved for discovered blockers found during execution or review.

## Review state slice

```
unstarted → in-progress → needs-agent-review → [review gates applied]
                        → needs-human-input → [human input/review]
                                                │
                                ┌───────────────┼───────────────┐
                                ▼               ▼               ▼
                            complete        revision-        blocked
                            / done          required       (discovered
                                           (rework           blocker:
                                            needed)       blocked_reason
                                                           set)
                                │
                                └──→ in-progress (rework) → needs-agent-review → ...
```

An `unstarted` card with unsatisfied `dependsOn` entries stays `unstarted` -- this is a planned dependency, not a blocker. The DAG encodes it. Do not set `blocked` for planned upstream dependencies.

Cards route to `needs-agent-review` or `needs-human-input` based on the kind of review required:
- Route to `needs-agent-review` when the review can follow the ordered gate protocol (agent-executable).
- Route to `needs-human-input` only when a named human decision, policy choice, or
  evaluation is required and cannot be resolved by source review, mathematical
  grounding, repo policy, or the DAG.
- A card in `needs-agent-review` may be transitioned to `needs-human-input` only if
  the gate-based review records the exact non-agent-resolvable question. Passing Gates
  1-6 with no findings is not itself a reason to ask for human input.

## Review execution requirements

### Subagent isolation (mandatory)

Every review must be executed by a **fresh-context subagent** dispatched by the
coordinator. The subagent has never seen the implementation session. It receives:

- The card body (the task/spec/phase/plan file)
- Paths to work artifacts (files changed, branches, PRs, commits)
- Paths to baseline artifacts (decision cards, prior specs, category-obligation
  baselines — see Gate 4 for the full list)
- This review kernel

The subagent must not receive: the implementing agent's chat transcript, the
implementing agent's rationalizations, the coordinator's opinions about the work,
or any prior review logs (unless the card is cycling through a revision cycle, in
which case the subagent sees previous review logs as evidence).

The coordinator must not perform review inline in its own session. The
coordinator's context already contains the implementing state. Even if the
coordinator did not personally implement the work, its session may contain
delegation records, summaries, or ambient discussion that contaminates independent
judgment.

### Anti-boxchecking rules (applied by the review subagent)

Every gate pass must produce concrete, falsifiable evidence. Forbidden review
language:

- "Appears correct" / "looks good" / "seems fine" → re-do the check
- "I assume" / "probably" / "should be" → the gate is not checked yet
- "The test passes" without citing which test and showing its output → not checked
- "The spec is consistent" without naming the specific parts verified → not checked
- "No issues found" without describing what was specifically examined → not checked

For each gate that passes, the review log must include at least one concrete
artifact:

- Gate 1: the exact source path that grounds each definition
- Gate 2: each acceptance criterion listed with the artifact that satisfies it
- Gate 3: the git diff command run and the specific surfaces inspected
- Gate 4: the baseline artifact consulted and the comparison produced
- Gate 5: the test command run or the proof step verified
- Gate 6: the specific rule checked and the evidence that it is satisfied

### Synthesis requirement (applied by the review subagent)

Review exists because the user needs judgment, not receipt checking. File
existence, completed checklist rows, command names, and worker self-reports are
not evidence that the work is correct. They are only pointers to what the
reviewer must inspect.

Self-report is structurally biased toward approval in this repo's failure modes:
an implementing agent usually knows what a convincing report should say. Treat
the implementer's reported diligence as a claim to verify, not as evidence.

Every substantive review must state the synthesis produced by reading the card,
sources, artifacts, and diff. The synthesis must answer what understanding
changed and why that change matters for this card. Examples:

- "This patch is acceptable because source X makes Y the owner, while the
  apparent conflict at Z is only a checker-modeling gap."
- "This patch fails because the source says X under hypothesis H, but the card
  implements the broader claim Y."
- "This QC finding belongs to the plugin spec, not local source cleanup, because
  the code already expresses the category construction and mypy lacks model M."

Inventories, tables, and checklists can support a review, but they cannot be the
review. If the reviewer cannot produce a synthesis that would be hard to fake
without reading the sources and artifacts, the outcome is an evidence gap:
`revision-required` for fixable review insufficiency, or `blocked` if the
missing understanding requires a prerequisite source, decision, or executable
experiment.

### Judgment contract (applied by the review subagent)

Concrete evidence is necessary, but it is not sufficient. The reviewer is not a
schema validator, grep wrapper, or diff-presence script. It must use the gates to
make a judgment about the work.

Coordinator prompts for review subagents must include this contract:

- Decide whether each apparent issue is material for this card after reconciling
  the card objective, current repo policy, baseline artifacts, and actual diff.
- Identify the highest-priority applicable policy before treating a deletion,
  signature change, or missing artifact as a defect.
- Classify findings as one of: material defect, evidence gap, policy-required
  change, orthogonal change, or needs-human-input.
- Explain why a failed gate cannot be resolved by a higher policy, existing
  source grounding, or a narrower interpretation of the card.
- Do not emit findings that are only "line X changed" or "artifact Y is absent"
  unless the review also states why that fact matters for the card's
  mathematical or engineering acceptance.
- Name at least one plausible pass condition for each failed gate. If the
  reviewer cannot state what would make the work acceptable, it has not
  understood the defect.
- Start from synthesis, not inventory: explain what the reviewer's understanding
  of the mathematical, code, or QC-tooling situation is after reading the
  artifacts, then use concrete evidence to support that judgment.
- Treat worker self-reports as claims under review. Do not cite them as proof
  that a source was read, a test was meaningful, or a diff is scoped.

Do not prompt a review subagent merely to "apply the gates." That wording
produces checklist-shaped reports instead of review.

### Review subagent dispatch template

Use this shape for review prompts. Fill the path lists narrowly; do not paste
implementation rationale or coordinator opinions.

```markdown
## Identity
You are a fresh-context research review agent in /home/dzack/research.
Do not edit files unless this prompt explicitly says to write the review log.

## Mission
Review [CARD_PATH] for acceptance under the research review kernel.

## Required Background
Read before judging:
- AGENTS.md
- Any nested AGENTS.md for changed paths
- .agents/skills/research-state-machine/references/review-kernel.md
- Domain skills/references required by the card

## Work Artifacts
Inspect actual staged and unstaged diffs for:
- [CHANGED_PATHS]

Inspect baseline/source artifacts as needed:
- [BASELINE_PATHS]

## Judgment Contract
You are not a validator, grep wrapper, or diff-presence script. Use the gates as
a scaffold to make a judgment about the work.

Begin with synthesis: state what you now understand about the mathematical,
code, or QC-tooling issue after reading the card, sources, artifacts, and diff.
If you cannot produce that synthesis, report an evidence gap instead of filling
an inventory.

For each apparent issue, classify it as one of: material defect, evidence gap,
policy-required change, orthogonal change, or needs-human-input.

Before treating a deletion, cast, signature change, or missing artifact as a
defect, identify the highest-priority applicable policy and reconcile it with
the card objective and actual diff.

Do not report a finding that is only "line X changed" or "artifact Y is absent"
unless you explain why that fact matters for this card's mathematical or
engineering acceptance.

For every failed gate, name at least one plausible pass condition. If you cannot
state what would make the work acceptable, do not call it a defect.

Treat implementer self-reports, work logs, and checklist rows as claims to
verify, not as evidence of correctness.

## Output
If this is a dry run: return only the judgment table in chat and do not write.
If this is production review: write the review log into [CARD_PATH] and return
the changed path plus the highest-signal findings.
```

### Review-prompt evaluation loop

Changes to review-subagent instructions are not accepted because they sound
better. Evaluate them with live dry-run review trials before using them for
production status changes.

Use this loop when revising review prompts or this kernel:

1. Pick at least two representative cards with known review difficulty:
   - one containing an apparent diff violation that a higher-priority policy may
     require;
   - one containing a real material defect plus an evidence gap.
2. Dispatch fresh-context dry-run reviewers. They must not edit files or change
   statuses.
3. Read each subagent transcript with `reading-transcripts`; do not rely on the
   terminal summary.
4. Accept the prompt change only if transcripts show the reviewer:
   - reconciled policy hierarchy before reporting defects;
   - classified findings by materiality;
   - distinguished evidence gaps from code/design defects;
   - named plausible pass conditions;
   - produced at least one judgment that could not be generated by grep, schema
     validation, or diff-presence checks alone.
5. If a trial still produces checklist-shaped analysis, revise one instruction
   narrowly to address the observed failure and repeat the loop.

Do not promote a review prompt or kernel revision based only on a clean artifact
diff, a subagent final summary, or a single easy trial.

### Role boundaries

Gates 1-2 may be self-checked by the implementer before submitting to review, but
the review subagent must independently verify both gates from scratch.

Gates 3-6 require the review subagent. The implementer must not pre-check these
gates; the subagent approaches them with fresh context and no prior exposure to the
implementer's working assumptions.

The review subagent is not the adversarial auditor (that is a separate
state-machine stage governed by `research-proof-auditing`). The review subagent
applies the gates with rigor; it does not run a full attack.

## Ordered gates

Apply gates in order. Stop at the first failing gate (fail-fast). A failure at gate N invalidates any work that would be checked at gates N+1 through 6, so documenting those downstream gates after an upstream failure is wasted effort.

### Gate 1: Definition Grounding

Every mathematical definition, type, predicate, constructor, and method-owner claim must trace to a canonical source.

**Check:**
- For each definition the work introduces or depends on, the card body (or a linked card) records: source path or reference, exact definition, owner category, hypotheses, codomain/return object, and proof obligations for choice-independence or equivalence.
- For implementation code: public types correspond to grounded mathematical categories. Raw `Parent`/`Element` surface leaks are absent.

**Sources to consult:** `category_specs/*/docs/MAPPING.md`, `category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, `theory/references/index.md`, and any linked decision cards.

**Failure modes:**
- **Ungrounded definition** (definition present but not sourced) → `revision-required`. Record the missing source.
- **Missing definition** (speculative spec writing, no definition recorded) → `revision-required`. Split a source-mining or decision leaf.
- **Ambiguous term** (multiple plausible meanings, no decision recorded) → `revision-required`. Split a decision card. Parent blocked until decided.
- **Raw Sage type leak** (`Parent`/`Element` on public API without mathematical alias) → `revision-required`.

### Gate 2: Acceptance Criteria

The work must satisfy its own acceptance criteria and every applicable parent criterion.

**Check:**
- Card's `successCriteria` or `acceptanceCriteria` -- verify each item against the artifacts.
- Parent card's `successCriteria` -- verify each item that applies to this child.
- If this card claims to discharge a parent-plan obligation: is the claim explicit and backed by evidence?

**Failure modes:**
- **Own criteria unmet** → `revision-required`. List each unmet item.
- **Parent criteria violated** → `revision-required`. This is a backsliding offense; see also Gate 4. List the parent criteria and how they are violated.
- **Discharge claim unbacked** → `revision-required`. Card claims to discharge a parent obligation but evidence is missing.

### Gate 3: Spec-Weakening (category-spec cards)

No spec obligation may be deleted, weakened, narrowed, or relocated without a source-grounded replacement owner.

**Check (patch-level):**
```
git diff --cached
git diff
# and any commits created during the work, via git show <commit>
```
Inspect with a patch view. Flag:
- Deleted abstract methods or `@abstract_method` decorators
- Removed constructor/category obligations from `Constructors()` namespaces
- Narrowed category assertions (fewer checks, weaker predicates, shallower probes)
- Weakened acceptance criteria in any touched card body
- Moved obligations to a card/phase/plan without a source-grounded replacement owner
- Sage-gap-driven interface shrinkage (the category-obligation examples got quieter but
  the spec got smaller)
- **Orthogonal changes**: modifications to code, comments, or configuration outside the
  stated task scope. An agent asked to fix one method's owner may silently "clean up"
  unrelated imports, reformat adjacent functions, or remove comments it considers stale.
  These are spec-weakening because they change surfaces the reviewer is not expecting
  to audit. Flag any change to a file that was not in the task's declared scope.
  The Karpathy observation: "They still sometimes change/remove comments and code they
  don't like or don't sufficiently understand as side effects, even if it is orthogonal
  to the task at hand."

**Failure modes:**
- **Any of the above** → `revision-required`. Document the exact deletion/weakening and the missing replacement owner. The rework must either restore the obligation verbatim or provide a grounded replacement card.
- **Category-obligation improvement paired with interface shrinkage** →
  `revision-required`. This is a spec-regression task failure regardless of command
  output.
- **Orthogonal changes** → `revision-required`. Any diff outside the task's declared scope must be reverted unless the change is justified in a separate task or the card body documents why it was necessary for the scoped work. The test: every changed line should trace directly to the task's stated objective. If a line was changed because the agent "thought it looked better" or "was cleaning up," it's orthogonal.

### Gate 4: Gradient (Backsliding Detection)

The work must not reverse, weaken, or contradict any previously established truth.

**Baseline artifacts (in priority order):**

1. **Decided decision cards** -- Scan `.agents/plans/features/*/decisions/` for cards with `status: decided` or `status: implemented`. Does the work reverse the chosen outcome? Does it reintroduce a rejected alternative?
2. **Previously approved specs** -- Are `specs/*.md` files modified? Does `git diff` show removal of accepted requirements?
3. **Previously passing category-obligation examples** -- Does
   `just --justfile category_specs/justfile category-obligations` produce new failures
   on assertions that previously passed? Compute against the last known-good
   category-obligation baseline.
4. **Previously resolved TODO entries** -- Has a resolved observation from `.agents/TODO.md` history been reintroduced?
5. **Git history of committed work** -- Does `git log` show previous commits that established invariants, tests, or properties the current work implicitly reverts?
6. **Approved plans and phase cards** -- Do modified `PHASE-*.md` or `PLAN-*.md` files show removed or weakened phase gates?

**Gradient computation:**
```
gradient(dimension) = post_state(dimension) - baseline_state(dimension)
```
A negative gradient on any dimension is a finding. The review records which dimension, the baseline value, and the post-work value.

**Decision-card gradient check (explicit procedure):**
1. List all decided decision cards in the owning feature tree.
2. For each decision, extract the `chosen` value and the implications described in the card body.
3. Check the work artifacts for any action, definition, naming, or structure that contradicts a chosen outcome or adopts a rejected alternative.
4. If a contradiction is found AND no superseding decision card exists → `revision-required`.
5. If a contradiction is found and a superseding decision card exists → the gradient is intentional. Note it in the review log but do not block.

**Category-obligation gradient check:**
```bash
# Record baseline (from last known-good commit or a cached snapshot)
just --justfile category_specs/justfile category-obligations 2>&1 | tee /tmp/category-obligations-baseline.txt

# Post-work
just --justfile category_specs/justfile category-obligations 2>&1 | tee /tmp/category-obligations-post.txt

# Compute gradient
diff /tmp/category-obligations-baseline.txt /tmp/category-obligations-post.txt
```
- New failures → negative gradient → flag.
- New passes → positive gradient.
- Disappeared assertions (the category-obligation example file itself changed) → Gate 3
  violation, not a gradient finding.

**Failure modes:**
- **Decision reversal without superseding card** → `revision-required`. Design-level defect.
- **Previously passing category-obligation example now fails** → `revision-required` or
  `blocked` (if the failure reveals a genuine prerequisite gap).
- **Previously resolved TODO reappears** → `revision-required`.
- **Previously approved spec surface removed** → `revision-required`. May overlap with Gate 3.
- **Implicit decision contradicting repo policy** → `revision-required`. Examples: creating a local workaround when `research-software-wiring` requires backend-first routing; introducing variadic option-bag constructors after `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT` was approved.

### Gate 5: Mathematical Correctness

The mathematical content must be correct and the evidence must match the claim's escalation tier.

**Check by card type:**
- **Spec cards:** Are claims well-typed? Do they form a coherent interface (no missing required methods, no contradictory obligations)? Are hypotheses explicit?
- **Implementation tasks:** Do tests pass? Does the implementation actually implement what the spec requires? Is the algorithm correct for the claimed generality?
- **Research tasks:** Does the evidence support the claim at the appropriate escalation tier (exploratory, local-promotion, GOAL-discharge)?

Use `research-proof-auditing` for evidence sufficiency. The argument-shape gate applies: reject notes that replace construction with naming, cite authority without stating hypotheses, or inflate immediate consequences into claims. The standardness calibration memory applies: do not flag trivial derivations as gaps, and do not accept niche claims without precise citations and hypothesis checks.

**Failure modes:**
- **Tests fail** → `revision-required`.
- **Mathematical error in spec** (contradictory axioms, ill-typed method signatures) → `revision-required`.
- **Cheaper proxy evidence** (proves a weaker claim, uses numerics where exactness is required) → `revision-required`.
- **Escalation tier mismatch** (GOAL-discharge language on exploratory evidence) → `revision-required` or `blocked` (if additional evidence infrastructure is needed).

### Gate 6: Style and Compliance

The work must follow repo style and compliance rules.

**Check:** Load `category-spec-style`, `clean-code`, and `anti-slop`. Verify:
- No raw `ConditionSet` on public API surfaces (must be wrapped in project aut/subobject objects)
- No broad variadic option-bag constructors as public surface
- Import hygiene (no unused imports, no lazy-import bloat)
- Type annotations present and correct
- No AI-slop patterns (boilerplate docstrings, placeholder prose, fake tests)
- Task-local agent-authored commit messages follow Conventional Commit format

**Failure modes:**
- **Style violations** → `revision-required`. Minor fixes; document which rule is violated.
- **Anti-slop patterns** → `revision-required`. May require rewriting generated prose.
- **Multiple style violations** → aggregate into a single checklist in the revision-required card.

**Commit-history scope:**
- Gate 6 commit-message compliance applies to the commits created to discharge the
  card under review, especially agent-authored implementation, spec, migration, or
  review commits.
- Historical human checkpoint commits that are already ancestors of `origin/main`
  are provenance, not per-card style failures. Do not convert every card touched by
  such a checkpoint into `blocked` or `revision-required`.
- If a historical checkpoint introduced a substantive defect, fail the gate that
  covers the defect itself: Gate 1 for ungrounded definitions, Gate 3 for spec
  weakening, Gate 4 for backsliding, Gate 5 for mathematical error, or Gate 6 for
  current style/content defects. The commit message alone is not the blocker.
- Published commits that used forbidden git operations such as `--no-verify` may
  still be recorded as process findings, but do not treat them as global blockers
  for unrelated ready leaves. Scope the finding to the card whose reviewed work
  actually depends on that commit and continue other DAG-ready work.

## Review procedure

This is the procedure executed by the **review subagent** (a fresh-context agent
dispatched by the coordinator):

```
1. Receive the card body, work artifact paths, and baseline artifact paths from
   the coordinator.
2. Verify the card is not oversized. If it hides major theorem, algorithm,
   convention, or trusted-base work, report this to the coordinator and do not
   proceed with gates.
3. Read the card body.
4. Read the work artifacts and baseline artifacts.
5. Apply Gates 1-6 in order:
   a. Run the checks for the current gate.
   b. Interpret the evidence against the current repo policy hierarchy and the
      card's actual objective. Separate policy-required changes, evidence gaps,
      material defects, and unrelated cleanup.
   c. If the gate passes, record the concrete evidence and the reason it is
      sufficient for this card; then proceed.
   d. If the gate fails, stop. Record findings. Set outcome. Do not continue to
      later gates.
6. If all gates pass → outcome is complete/done.
7. If any gate fails → outcome is revision-required or blocked:
   - revision-required: the work can be fixed within this card's scope.
   - blocked: a new prerequisite card (decision, source-mining, backend-gap) must
     be created and resolved before this card can proceed.
8. Write the review log into the card body under ## Review Log and return it to
   the coordinator.
```

This is the procedure executed by the **coordinator** after the review subagent
completes:

```
1. Receive the review log from the subagent.
2. Read the subagent transcript before accepting, routing, or summarizing the
   review. Do not rely on the terminal summary. Use the transcript tooling
   required by the active subagent harness, and compare the transcript to the
   review log and actual git diff.
3. Verify the review for box-checking:
   a. Every gate pass has an associated concrete artifact (file path, command run,
      diff inspected, source consulted).
   b. The review contains no forbidden language: "looks good", "appears correct",
      "seems fine", "no issues found" without specific examination.
   c. Failures cite specific code, line numbers, source paths, or test output.
   d. The outcome is supported by the findings (a list of passed gates with no
      failures should not produce revision-required; a gate failure should not
      produce complete/done).
   e. The review reconciles apparent conflicts instead of reporting literal
      mismatches blindly. It must not flag a change as weakening when a
      higher-priority repo policy explicitly requires that change.
   f. Evidence gaps are labeled as evidence gaps, not automatically promoted to
      code or design defects.
   g. Findings distinguish material defects from merely automatable checks. A
      review that could have been produced by a schema validator, grep, or
      diff-presence script is not substantive.
   h. At least one finding or pass rationale contains a non-automatable judgment:
      it reconciles two sources of authority, explains why a plausible defect is
      not a defect, or changes the apparent severity after reading the source.
      If every finding is only a missing file, changed line, schema mismatch, or
      command result, reject the review as insufficiently intelligent.
   i. Status-only diff check: if the only change to the card file is the `status`
      line (e.g., `needs-agent-review` → `complete`), the review is fraudulent. A real
      review writes its findings into the card body under ## Review Log. Cards are
      evidence containers, not checklists. If the card body grew no review content,
      no review happened. Reject and demand specific evidence.
4. If the review is substantive → apply the status change (or prepare it for human
   approval if the final gate requires it).
5. If the review is a box-checking exercise → reject it. Document the specific
   deficiencies. Re-dispatch to the same review subagent when possible with a
   tightened prompt that quotes the anti-boxchecking rules, names the shallow or
   invalid findings, and demands a judgment-level review rather than another
   checklist pass.
```

## Review Log format

Each review produces a dated entry in the card body:

```markdown
## Review Log

### Review YYYY-MM-DD (Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, ...
**Gates failed:** Gate 3 Spec-Weakening, ...
**Outcome:** revision-required

#### Gate 3 Findings: Spec-Weakening

- `category_specs/rings/subcategories/fields.py:42` -- Deleted `KroneckerSymbolField`
  from `Constructors()` without a replacement card. This surface must be restored or a
  grounded replacement card must be created before re-review.

- `category_specs/rings/subcategories/fields.py:78` -- Category assertion narrowed from
  `check_method_surface(R, expected_methods=15)` to `check_method_surface(R,
  expected_methods=12)`. The deleted methods (`torsion_subgroup`, `class_group`,
  `class_number`) were category-spec obligations. Missing grounded replacement card.

**Required fixes:**
1. Either restore `KroneckerSymbolField` to `Constructors()` or create a source-grounded
   card that replaces it.
2. Restore the category assertion to 15 expected methods or document where each of the
   3 removed methods was moved with a grounded replacement owner.

**Re-review criteria:**
- `git diff` from the rework must show no net deletion of `Constructors()` entries
  without grounded replacement cards.
- Category-obligation method count must match or exceed the previous baseline of 15, OR
  the 3 removed methods must have explicit grounded replacement cards.

---
```

## Escalation during review

If a review reveals findings that cannot be resolved within the current card:

- **Human input needed** (the review determines that a human decision, policy choice,
  or evaluation is required that an agent cannot provide) → Set
  `status: needs-human-input`, record the specific question or decision needed in the
  card body, and optionally link a decision card. The question must be substantive:
  "approve this reviewed work," "may I stop," "should policy-forced routing be
  accepted," and other closure-shaped prompts are not valid human-input blockers.
- **Discovered blocker** (a prerequisite decision, source-mining result, or backend gap is needed to proceed) → Set `status: blocked`, set `blocked_reason` to a one-line description of the gap and the prerequisite card ID, create the prerequisite card, and link it in `dependsOn`.
- **Design-level defect** (the card's fundamental approach is wrong, not the implementation) → Set `status: revision-required`, but note that the rework may require plan-level redesign. Create a decision card or plan-review task.
- **Pattern repeated across multiple cards** (same gate failure on N cards) → Create a phase-level corrective card. Do not rework N cards independently for the same systemic issue.

Do not set `status: blocked` for planned upstream dependencies already expressed in `dependsOn`. Those cards remain `unstarted` until their dependencies resolve.

Do not set `status: blocked` for planned upstream dependencies already expressed in `dependsOn`. Those cards remain `unstarted` until their dependencies resolve.

## What this kernel does not govern

- **Plan approval** -- Plans are human-gated before decomposition; the review kernel applies to their child cards after execution.
- **Feature, spec, and plan gating** -- These cards are approved through the upstream gate protocol in `upstream-gates.md`, not the task review kernel. Features, specs, and plans are synchronous human+agent artifacts; they gate into each other (feature → spec → plan) before autonomous task execution begins.
- **Feature approval** -- Features are always human-gated.
- **GOAL.md discharge** -- Requires the full composed-goal audit described in the execution kernel; the review kernel handles card-level review, not program-level discharge.
- **QC transition gate** -- QC is phase-transition evidence, not a per-card review step. QC failures during review should be recorded but do not by themselves block a spec card during spec-phase work.
- **Adversarial audit** -- The review kernel's reviewer is independent but focused on gate compliance. Full adversarial attack (trying to break the strongest claim by any means) is a separate state-machine stage following card-level review, governed by `research-proof-auditing`.
- **Completed-card meta-review** -- After cards pass gate review and reach `complete`/`done`, a post-hoc scan checks whether the gate review was substantive or performative (Jerry-behaviour). Governed by `research-planning-cleanup`. This is a separate, periodic pass, not part of the per-card gate protocol.

## Load with

- Load `research-proof-auditing` for proof, evidence, and fraud checks within Gate 5.
- Load `category-spec-style` for style and compliance checks within Gate 6.
- Load `category-spec-audit` for mathematical ownership, spec surface, and downstream-poisoning checks across Gates 3-5.
- Load `research-orchestration` for delegation of review to independent agent sessions.
- Load `jerry-behaviour` before performing any review. The anti-boxchecking rules are necessary but not sufficient — an agent who has internalized Jerry patterns will recognize when its own output is becoming paraphrase-as-review or checklist theater.
