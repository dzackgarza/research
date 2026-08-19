---
title: Research Planning Cleanup
status: active
date: 2026-05-29
---
# Research Planning Cleanup

Meta-review and cleanup of completed cards.
This skill operates one layer above gate-based per-card review.
Gate review (see `research-state-machine`) checks that the work satisfies formal
criteria. This skill asks: was the work substantively done, or did a subagent fill in
plausible text without doing the work?

## When to Use

Use this skill for:

- Scanning recently completed cards for Jerry-behaviour (paraphrase-as-review, checklist
  theater, evidence-shaped evidence, self-certification).
- Identifying cards where the evidence claims are plausible but the claimed work would
  have been impossible without evidence that is not present.
- Flagging completed cards whose reviewers produced zero findings — a structural Jerry
  signal (real artifacts have problems).
- Cleaning up planning debt: cards that are misclassified, oversized, duplicated, or
  blocking downstream work by sitting in the wrong state.
- Finding systemic patterns (three cards with the same shallow review, identical
  gate-justification text, no line numbers anywhere).

Do NOT use this skill for:

- Initial gate review of a `needs-agent-review` card.
  That is the review kernel's job.
- Plan approval. Plans are human-gated.
- Proving mathematical correctness.
  That is `research-proof-auditing`.

## Core Philosophy

Agents give their best effort.
We are not requiring every line to be proved.
We are looking for POSSIBLE positives for:

- **Task value blindness**: a review spends model judgment on checking receipts the user
  did not need a model for: file existence, checked boxes, row counts, or whether a
  worker reported doing the work.
  This is economically incoherent when the hard part is deciding whether the work is
  mathematically, technically, or strategically sound.
- **Self-certification**: the worker's own report is treated as evidence that the work
  happened correctly. In this failure mode, self-report is biased toward approval: the
  agent knows what a good report should say, whether or not it performed the underlying
  inspection.
- **Reward-hacking**: work that satisfies the formal shape of a task (status updated,
  gates marked, review log present) without the substance.
- **Brainless adherence**: a subagent given a task card follows the letter of the
  acceptance criteria but fills in plausible text rather than discovering the actual
  answer through research, computation, or inspection.
- **Confabulation of card content**: claims in the card body that read like work was
  done (commit hashes, source citations, evidence summaries) but which collapse under
  inspection — the commit doesn't contain what the card says, the source doesn't say
  what the card claims, the evidence is a paraphrase of the card's own claim.
- **Shallow work reported as complete**: a task that required reading 11 spec files
  produced a review log that could have been written without opening any of them.

## The Economic Argument

Falsified data, weak claims, and shallow reviews are not harmless shortcuts.
They are technical and process debt that accrues interest and compounds:

- A weak claim in card A becomes the foundation for card B.
- Card B's implementer trusts the claim and builds on it.
- Card C's review checks B against A, finds agreement, and passes.
- The error is now three layers deep and requires disproving an entire chain of
  dependent work to correct.

The compounding cost means weak pillars must be found and vetted early.
A card that took 10 minutes of shallow work to produce can cost hours to unwind if it
poisons downstream cards.
The meta-review pass is not bureaucracy; it is the cheapest possible intervention
against compounding process debt.

## Scanning Procedure

### 1. Select Cards

Scan cards with `status: complete` or `status: done` that were completed recently (last
N days, last review session, current phase).
Prioritize:

- Cards whose reviewers share a model family with the implementer.
- Cards whose review logs are short relative to the claimed work (a 5-line review for a
  card that claimed to audit 11 spec files).
- Cards where multiple reviews produced identical or near-identical gate justifications.
- Cards with zero negative findings across all gates.

### 2. Apply Jerry Signals

For each selected card, check the Jerry structural invariants (see
`jerry-behaviour/references/jerry-patterns.md`):

| Signal | What to check |
| --- | --- |
| Zero negative findings | Did every gate pass? Real artifacts have problems. |
| No line numbers or code excerpts | Does the review cite specific files and lines, or only card-body paraphrases? |
| No external cross-checks | Did the reviewer check any claim against a source outside the card body? |
| Generic gate justifications | Could the same gate text apply to any card of this type? |
| Convergent language | Do multiple cards share nearly identical review language? |
| Fluency-biased praise | Does the review evaluate presentation ("well-structured") rather than correctness? |
| Status-only card diff | Does `git diff` of the card file change only the `status` line? A real review adds evidence to the card body under ## Review Log — the card grows content. A status line change with no body growth is a box check, not a review. |

### 2.5. Demand Synthesis

Before spot-checking details, ask what synthesis the review produced.
A substantive review should change the reader's understanding of the source,
mathematical owner, implementation boundary, QC-tooling obligation, or failure mode.
It should state that change directly.

If the review only inventories files, confirms rows, quotes worker reports, or restates
the card's acceptance criteria, classify it as shallow even if every listed item is
true. Inventories may support synthesis; they do not replace it.

### 3. Spot-Check Evidence

For cards that trigger Jerry signals, do one spot-check:

- If the review cites a commit hash, open that commit and verify it contains what the
  review claims.
- If the review claims a source was checked, open the source and verify the specific
  claim.
- If the review claims a test passed, run the test and verify the output.
- If the card claims a certain input shape, configuration, or behavior was assumed,
  check whether that assumption was stated in the task card or was silently invented by
  the agent. An agent that assumes facts not in evidence is confabulating certainty.
  The Karpathy observation: "The most common category is that the models make wrong
  assumptions on your behalf and just run along with them without checking."

One disproven claim is sufficient to flag the entire card as suspicious.
You do not need to verify every claim — the goal is to find grounds for kicking back.

### 4. Classify Findings

For each suspicious card, classify the finding:

| Classification | Description | Action |
| --- | --- | --- |
| **Confabulated evidence** | A specific evidence claim is false (commit doesn't contain claimed change, source doesn't say what card claims). | Kick back with the disproven claim cited. |
| **Shallow review** | The review log passes gates but contains no evidence of actual inspection (no line numbers, no source cross-checks, zero findings). | Kick back. Require re-review by a different model family. |
| **Undersized work** | The task scope required substantial work (audit 11 files, implement a new category surface), but the evidence suggests a subagent filled in plausible prose. | Kick back. Require specific evidence: file-and-line findings, test output, diff excerpts. |
| **Wrong assumptions** | The agent assumed facts not stated in the task card (a specific input shape, a configuration value, a behavior contract) and proceeded without surfacing the assumption. The output is plausible but built on premises the task never supplied. | Kick back. Ask: "Where in the task card did you find this assumption?" If the agent cannot point to it, the work is confabulated. |
| **Systemic pattern** | Multiple cards from the same session show the same shallow-review pattern. | Flag the batch. Kick back the weakest exemplars. Create a phase-level note. |
| **Genuine but thin** | The card is probably correct but the review is too thin to be confident. | Kick back with a request for specific evidence. Not a rejection — a request for proof of work. |

### 5. Kick Back

When kicking back a card:

1. Set `status: revision-required`.
2. Add a dated entry to the card's Review Log explaining:
   - Which specific Jerry signal was triggered (cite the invariant).
   - What the spot-check found (quote the disproven claim, show the actual source
     content, show the test output).
   - What concrete evidence would satisfy re-review (specific files to check, values to
     verify, tests to run with expected output).
   - What made the card suspicious — not "this looks bad" but "the review claims X but
     the commit only contains Y" or "the review cites no line numbers despite claiming
     to audit 11 files."
3. Do NOT punish. The implementer and reviewer were acting in good faith.
   The feedback should be: "This specific claim needs verification.
   Here is how to verify it.
   When you have done so, resubmit with the evidence."

### 6. Avoid Churn

This scan is surgical, not bureaucratic.
Do not:

- Kick back cards because the review could have been more thorough, when the existing
  review is substantively adequate.
- Require re-review of every card in a batch when only some are suspicious.
- Create new process rules, tracking systems, or metadata fields to "prevent this from
  happening again." The Jerry patterns are already documented.
- Turn the scan into a checklist.
  If you find yourself checking items off a list rather than reading cards and thinking
  about whether the work was real, you have become the next Jerry.

A good scan kicks back 2-5 suspicious cards and leaves the rest alone.
A scan that kicks back 20 cards is either identifying a systemic crisis (which should be
escalated to a phase-level note, not 20 individual kicks) or is itself a Jerry scan —
checking boxes rather than reading evidence.

## Cross-References

- **jerry-behaviour**: The structural invariants, detection signals, and countermeasure
  principles. Load before scanning.
- **anti-slop**: Surface-level slop patterns (boilerplate prose, generic names).
  Jerry-behaviour is the meta-level evaluator failure; anti-slop is the surface-level
  artifact failure. Both are relevant.
- **research-state-machine/references/review-kernel.md**: The gate protocol that every
  card passes through before reaching `complete`. The meta-review checks whether the
  gate review was substantive or performative.
- **research-proof-auditing**: For spot-checking mathematical claims.
  Use when the suspicious card contains mathematical assertions to verify.
- **category-spec-audit**: For Red Flag Log requirements.
  A card whose review includes no introspection red flags despite touching
  implementation code is suspicious — real code has `isinstance`/`hasattr` patterns, and
  a reviewer who found none was not looking.
