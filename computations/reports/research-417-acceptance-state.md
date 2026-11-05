# research#417 acceptance: what remains, what ran, and the two owner handoffs

Read from the live issues (`#46`, `#417`) and executed in the declared shared runtime as a
consumer. No issue was written from here (the connector is read-only for issues), no
upstream checkout or edit, no shared-runtime mutation. `#606` is superseded and is not used
as a gate.

## The original acceptance, as written

- `#417`: "This issue keeps the cross-repository ordering among the milestones under
  dzackgarza/research#46 and the research-side acceptance: the expectation suite under
  `tests/` in this repository must pass on the realized library." Its 20 children are
  complete (`sub_issues_summary` 20/20).
- `#46` (ancestor): "Every open prerequisite precedes its consumer, including
  prerequisites of grouping issues. No ancestor blocks on a descendant." Also: "Final core
  acceptance dzackgarza/sage-extensions#238 and extension acceptance
  dzackgarza/sage-extensions#240 retain their full scopes", and `#417`'s row routes moved
  M1 acceptance to `sage-extensions#228`.

What remains for `#417` itself is therefore exactly one thing: the `tests/` expectation
suite passing on the realized library. It is **not** met, and this record does not claim
it.

## What ran (executed, not inferred)

1. Narrow import check in the deployed runtime (recorded in
   `deployed-runtime-readiness-20261104.md`, commit `beea37a7a5`): preamble imports;
   `Sets().PartiallyOrdered() is PartiallyOrderedSets()` and the totally-ordered analogue
   are **True**; `Sets().object_set` is **absent** from the session surface.
2. Attempt to run one original expectation file with the deployed recipe:
   `tests/constructions/test_set_ordering_and_mor_classification_construct.sage`, via
   `pytest` inside `/sage/.venv/bin/sage`. It **could not run**: `pyproject.toml`'s pytest
   `addopts` demand `--timeout`, `--timeout-method` and `--report-log`, i.e.
   `pytest-timeout` and `pytest-reportlog`, which the deployed venv does not have. With
   `addopts` overridden the invocation returned no usable output; I stopped rather than
   churn, and record it as unresolved harness absence, not as a test failure.

## The two precise owner handoffs

**sage-extensions (runtime owner) — `object_set` exposure.** `object_set` exists in source
(`categories/group/classifying_categories.py`, `categories/abstract_categories/functors.py`)
but `hasattr(Sets(), 'object_set')` is False on the deployed provider snapshot `6ad7a5ea`.
Required: deploy a provider whose `Sets()` (and its classifying categories) expose
`object_set` on the session surface. That is the prerequisite for sage-extensions#95's
runtime acceptance, and no consumer-side work can substitute for it.

**Acceptance harness (runtime/CI owner).** The suite cannot run in this deployment as
declared: `pyproject.toml` `addopts` require `pytest-timeout` and `pytest-reportlog`, and
the CI acceptance additionally uses `qc_sage_session`, `qc_xfail_issues`,
`qc_test_history`, `qc_unique_inventory` from `ai-review-ci` while pinning
`sage-extensions@441519c574cec12ada06ad586f6c3862fbca96d0` — a different pin from the
deployed `6ad7a5ea`. Required: either a deployment carrying those plugins at the matching
pin, or the suite run through that CI workflow.

## Criteria applied

- Advanced only items whose prerequisites are present: the owned-poset refinements
  (measured True) and the import surface (measured OK).
- Did not mark `#417`, `#95`, `#118` or anything else done: their stated acceptance is not
  met by this narrow pass.
- No broad T campaign is claimed. `#606` remains superseded and unused as a gate.
