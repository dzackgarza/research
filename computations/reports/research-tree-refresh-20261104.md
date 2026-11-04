# Tree refresh after the #219 closure and the #606/#384 reflow (2026-11-04)

Read from the live issues; no issue was written, closed or reordered from here.

## What closed

- **research#219** — `completed`, 2026-11-04T16:26:43Z, after the parent's independent
  review of `14b30805`. The 28-boundary survey and its reconciliation record stand as its
  evidence; no further action on this issue is available or needed from this repo.
- **research#606** — `not_planned` / label `superseded`, 16:11:46Z. Owner's closure
  comment: "no research code remains for this issue to migrate"; its obligations are
  re-filed at owners: lean-categories#95–#98 (formal remainder), sage-extensions#40/#79/
  #95/#118/#225 (Python presentation of sets), and research-side acceptance declared as
  the expectation suite in `tests/constructions` and `tests/user_simulations` (218 files
  already asserting cardinality and countability facts).
- **research#384** — `not_planned` / `superseded`, 16:15:49Z; `sub_issues_summary` 1/1.

## What is open now, in order

`#46`'s first child **#417 (Milestone M1 — Daily mathematical work) is open** with all 20
children complete. Its realization lives at `dzackgarza/sage-extensions#21`; what it
retains here is the cross-repository ordering among the milestones under #46 and **the
research-side acceptance: the expectation suite under `tests/` in this repository must
pass on the realized library.**

## What currently bounds execution here (corrected)

My first pass of this section over-read the phase. The parent's read of `CONTRIBUTING.md`
at `f30078e` stands: **DEV-58/`n` is not a blanket Sage or test ban.** The orchestrator
runs each issue's original acceptance once its source and actual prerequisites are
complete, M1 included; what defers are *broad* suites, QC and notebook campaigns, and
only until #417's source prerequisites are delivered. Corrections recorded:

- No broad run is implied by anything here, and none was made by me at any point.
- Whether #417's prerequisites are delivered is not readable from this session just now:
  its realization lives at `sage-extensions#21` and the Python-presentation issues
  `sage-extensions#40/#79/#95/#118/#225`, and the unauthenticated GitHub rate window is
  exhausted until its next reset. I therefore neither claim the set-expectation suite is
  runnable nor that it is not.
- Consistent with the corrected reading, this repository's CI runs issue-specific
  acceptance automatically: `.github/workflows/cat-runtime-acceptance.yml` executes the
  named `tests/constructions/...construct.sage` files in the Sage container when pushes
  touch them. Orchestrated acceptance is thus already scoped per specimen; my local role
  adds nothing executable there.

So: correct and more modest — the phase bounds *broad* campaigns, which I never needed;
issue-specific acceptance belongs to the orchestrator and CI; and the open question (are
#417's upstream prerequisites delivered?) is checkable on the next rate window, not by
guesswork here.

## Consequences for this repo's records

- #219 closure supersedes the former "issue write unavailable" blocker for that issue;
  its evidence stays where it is.
- The #606/#384 reflow supersedes their former blocked-by analysis: lean-categories
  #95–#98 and sage-extensions #40/#79/#95/#118/#225 keep their owners. The two prepared pro-topic
  patches (ordinal natural product; finite-subset inclusion registration) remain the
  artifacts waiting for the `lean-categories` publishing route; nothing here claims them.
- Next permissible owned work in actual issue order: none this instant beyond this record —
  the remaining acceptance is execution-bound to terminal T.

## Corroboration and the actual prerequisite picture

- `4056425eafc8b6ad73e782338d3e7cc2b569848c` (2026-10-26, ancestor of main) rewrote
  DEV-58: "Once an issue's source changes and actual construction prerequisites are
  complete, the orchestrator runs that issue's original mathematical acceptance
  assertions on the integrated committed source. This applies during M1. Unrelated
  unfinished M1 work does not block those checks." Broad programme execution still defers
  to terminal T. This is the controlling text; older copies of the blanket reading
  elsewhere are superseded.
- The runtime that would execute #417's suite must **carry the realized library**. This
  VM's canonical Sage rootfs has `sage-extensions` at `7b222e86214524a53802350f3cfda9c513707600`
  (read directly from the rootfs git metadata), older than the delivered main the parent's
  source evidence cites (`c94206fc`). Consumers must not update the shared rootfs; the
  dedicated Sage environment project owns it. That pin — not the phase — is what defers a
  meaningful local run.
- Upstream prerequisite state (`sage-extensions#21`, `#40/#79/#95/#118/#225`) is not
  readable this instant (unauthenticated window exhausted), so no claim is made that
  #417's acceptance is runnable or blocked; the two facts above are the ones this session
  can establish from source.
- Expectation population, for whoever executes: 234 files under `tests/constructions` and
  `tests/user_simulations` reference cardinality/countability.

## Parent's read-only audit of the set-boundary prerequisites (at research 496293 / sage-extensions dca789c)

Read-only source audit, none of it executed acceptance. It replaces my earlier crude
"are those issue numbers open?" test with actual prerequisite edges:

- `sage-extensions#40`: `End`/`Aut` exist; `sage-extensions#39` (constructing category) is
  the actual prerequisite even though no prose edge names it.
- `sage-extensions#95`: `object_set` exists; runtime acceptance still unexecuted.
- `sage-extensions#79`: source delivered; the final tests live in `sage-extensions#238`.
- `sage-extensions#118`: the `RegularPolytopes` text is stale; owned posets exist; the A2
  specimen plus `#116`'s six-route acceptance still need review.
- `sage-extensions#225`: class-based `Set` dispatch genuinely remains; tagged M2.

Lesson recorded: an open issue number is not evidence of naked prerequisite. Run-time
acceptance is allowed only when those edges, not the issue labels, say so. Accordingly,
the prerequisite-follow-through fetches the exact states of #39/#238/#116 at the same
window as the rest, and local acceptance is keyed to the realized runtime pin, not to the
stale one in this VM's canonical rootfs.
