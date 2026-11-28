# Daily Work Schedule

Autonomous agents run on this rotation.

* * *

## 00:00 – 02:00 Policy enforcement and debris cleanup

- Run the automatic pruning checklist from AGENTS.md (delete .orig, .sage.py, empty
  dirs, banned directories, stale top-level markdown)
- Check for code thrashing: review files changed many times in recent git history — this
  indicates agents undoing each other's work or progress stuck in a cycle
- If thrashing is detected, `remember` the pattern (what files, what cycle) so future
  sessions can break the loop

* * *

## 02:00 – 04:00 Policy improvement

- Read recent git history and agent memories for recurring problems
- If a problem recurs, identify the BEHAVIORAL root cause — what agent behavior produced
  the problem, not what specific file or directory was created
- Draft a policy update to AGENTS.md that prevents the root behavior, not just the
  symptom. A policy that bans a specific directory name is a symptom fix.
  A policy that bans the behavior of preserving broken work in any form is a root fix.
- Policy changes must be committed with a commit message explaining: what recurring
  problem was observed, what root behavior causes it, and how the new policy prevents it

* * *

## 04:00 – 06:00 Literature and references

- Web research for papers and books not already listed in REFERENCES.md
- Ensure all relevant literature references are available locally in machine-parseable
  form (extracted from PDFs) so workers don't repeatedly fetch the same material
- For arXiv papers, prefer LaTeX source over PDF OCR

* * *

## 06:00 – 07:00 Literature check

- Review existing literature to determine if current computation scripts are leveraging
  known theory instead of reinventing it
- Verify known theory with computational examples as a starting point
- Check if any GOAL.md task has a simpler path via a theorem already in the literature

* * *

## 07:00 – 09:00 Adversarial audit (morning)

Assume every script is fraudulent until proven otherwise.
Apply the Computation Auditing Criteria from AGENTS.md with zero tolerance.

For every first-party `.sage` file in `computations/` and every first-party `.sage`
file in `src/` outside `src/external/`:
- Count assertions vs total lines.
  A script over 100 lines with fewer than 5 assertions is padding — delete it or rewrite
  it in the same session.
- Check every assertion: does the expected value come from GOAL.md or the literature, or
  from the script itself?
  Self-validating assertions (`x = f(); assert x == f()`) and hardcoded-boolean checks
  (`is_ok = True; ... assert is_ok`) are fraudulent — delete them.
- Search for print-statement theater: consecutive prints with no intervening
  computation, checkmarks/success markers in strings, f-strings with no interpolation or
  only hardcoded values, prints that state conclusions ("✓ SATISFIED") without a
  preceding assertion.
  Any block of 3+ consecutive prints with no computation between them is exposition
  pretending to be code — delete the block.
- Search for ad-hoc constructions: manually typed matrices larger than 3×3, manually
  typed vectors, bare `diagonal_matrix()` calls, `load("coble_geometry.sage")` (legacy
  file). These must use foundation library constructors or be deleted.
- Search for algorithmic gaps: bounded `for` loops claiming exhaustiveness without a
  mathematical justification for the bound, nested loops reinventing standard algebraic
  constructions. Delete or rewrite.
- Search for software engineering debris: `try`/`except`, `raise`, docstrings longer
  than 5 lines. These do not belong in math computation scripts.
- Search for trivial padding: scripts dominated by `rank()`, `signature()`, `det()`,
  `len()` calls with no substantive computation.
  Scripts that compute invariants and print them without asserting anything are not
  verification.

**Hard pruning rules:**
- If a script fails more than 3 of the above checks, delete it entirely.
  Do not attempt to salvage — the foundation is unsound.
- If a deleted script was marked "completed" or "verified" in any plan, note, or memory,
  invalidate that claim: update the note/memory to state the script was deleted as
  fraudulent, and the task is UNVERIFIED.
- If an audit trail or verification record references a deleted script, delete the audit
  trail too. An audit built on fraud is itself fraud.
- If a notes/proofs/ file claims a result that was "verified" by a deleted script, add a
  prominent warning at the top: "UNVERIFIED — computation script deleted as fraudulent."
- `remember` every deletion: what file, what fraud indicators triggered it, what GOAL.md
  task is now unverified.

* * *

## 09:00 – 10:00 Computation audit

- For each first-party computation script in `computations/` and each first-party
  shared/core script in `src/` outside `src/external/`, verify:
  - Assertions trace to specific GOAL.md claims or literature, not internal consistency
  - Expected values come from the mathematics, not from prior runs
  - Script runs via `just` without errors
- If a script fails: fix it or delete it.
  Do not document the failure.
- If a script's assertions only test internal consistency, rewrite the assertions to
  test GOAL.md claims

* * *

## 10:00 – 12:00 Goal alignment

- Review current work against GOAL.md tasks
- Identify drift: work that doesn't trace to a specific task
- Identify high-value vs low-value work: leveraging existing theory and pushing
  boundaries vs checking boxes with no clear motivation
- If drift is found, `remember` what drifted and why, so future sessions course-correct

* * *

## 12:00 – 14:00 Memory maintenance

- Review and update project memories
- Prune memories that are stale or no longer relevant
- Ensure failed approaches are recorded with: what was tried, why it failed, what to try
  instead
- Ensure operational context (environment quirks, tool gotchas) is captured

* * *

## 14:00 – 16:00 Foundation and refactoring

- Refactoring: centralized constructors in `coble_geometry_foundation.sage`
- Ensure all scripts use foundation library, not ad-hoc constructions
- Ensure no script loads the legacy `coble_geometry.sage`

* * *

## 16:00 – 18:00 Software and tooling

- Investigate and install software packages useful to computation scripts (GAP packages,
  Sage optional packages, CARAT, etc.)
- Ensure justfile recipes are up to date and cover all scripts

* * *

## 18:00 – 19:00 Subagent transcript review

- Use `ocm` to read recent subagent transcripts
- Identify common failures, misinterpretations of instructions, repeated mistakes
- If a failure pattern is found, determine the root behavioral cause and either:
  - Update AGENTS.md with a policy that prevents it
  - `remember` the pattern for future sessions

* * *

## 19:00 – 21:00 Adversarial audit (evening)

Same procedure as the morning adversarial audit (07:00–09:00), applied to any scripts
created or modified since the morning audit.
Additionally:

- Review git log since the morning audit.
  For every new or modified `.sage` file, apply the full Computation Auditing Criteria
  from AGENTS.md.
- Check for regression: did a session re-introduce a file or pattern that was deleted in
  the morning audit? If so, `remember` the regression and add a specific ban to AGENTS.md
  naming the pattern.
- Check for plan drift: if any plan or memory claims a task is "verified" or
  "completed", trace the claim to a specific script.
  If the script does not exist, fails its assertions, or fails the auditing criteria,
  the claim is invalid — update the plan or memory.
- Review notes/proofs/ for any new claims.
  Each claim must trace to a passing script.
  Ungrounded claims get the "UNVERIFIED" warning.

**Same hard pruning rules as the morning audit apply.** Delete fraudulent scripts,
invalidate claims built on them, delete audit trails referencing them.

* * *

## 21:00 – 23:00 Mathematical work

- Advance the highest-priority unverified GOAL.md task
- Use worktrees for any new computation
- Every script must assert GOAL.md claims, not internal consistency

* * *

## 23:00 – 00:00 Lean formalization

- Advance Lean formalizations in `coble_research_lean/`
- Check if target results already exist in Mathlib before proving
- Consolidate any duplicate Lean project directories
