# #417 acceptance, executed on the deployed runtime: harness route reproduced, 9 passed / 4 failed

Continues `research-417-acceptance-state.md`. Read-only over the live rootfs with the
consumer's own per-process bindings; no installation, no runtime change, no upstream edit,
no issue write. Source of the route: the runtime owner's
`results/research-harness-route.md` (Sage project, commit `f0782b0e8f29…`).

## Route, reproduced

```
PYTHONPATH="/repo/.scratch/se-provider-6ad7a5ea/src:/home/ai-review-ci/tool-artifacts/pytest_plugins"
/sage/.venv/bin/python -m pytest -o addopts= \
  -p qc_sage_session -p qc_xfail_issues -p qc_test_history -p qc_unique_inventory \
  --qc-history-dir /repo/.scratch/qc-history <files>
```

`/sage/.venv/bin/sage` is a `#!/sage/.venv/bin/python` script and takes no `-m`; the
interpreter is the entry point. `qc_*` are plain modules on that PYTHONPATH, bound in from
`$HOME/ai-review-ci` (not present inside the rootfs, so the host path is bound to
`/home/ai-review-ci`).

Reproduction of the owner's measurement:
`tests/constructions/test_set_ordering_and_mor_classification_construct.sage` →
**2 passed in 0.37s** (owner measured 2 passed in 0.35s).

## Measured batch (the boundary whose prerequisites the deployment carries)

`test_set_ordering_and_mor_classification_construct`, `test_sets_construct`,
`test_partially_ordered_sets_construct`, `test_totally_ordered_sets_construct`:

**9 passed, 4 failed in 1.29s.** Full log: `.scratch/set-layer-acceptance-run.txt`.

| failing test | first failure |
| --- | --- |
| `test_sets_construct.sage::test_sets_of_sets` | provider assertion: "cannot read {1, 2} as a subset of {1, 2, 3}: a set is read as a subset here only through its elements, which needs it finite and enumerated" (`set_categories.py:3467`) |
| `test_function_sets_between_finite_sets` | same subset-read path |
| `test_infinite_sets_and_their_constructions` | same file, later construction |
| `test_cardinal_arithmetic` | same file |

These are research's original expectations failing against the deployed provider — findings,
not harness errors: collection succeeded, the other 9 tests ran and passed in the same
session.

## Caveat recorded as required

`-o addopts=` removes only the missing-instrumentation options from `pyproject.toml`
(`--timeout=60 --timeout-method=signal`, `--durations`, `--junit-xml`, `--report-log`).
**No assertion was weakened and no test was skipped**: the run has no per-test time limit
and no junit/report-log artifact. Reporting and time-limit differences are exactly that.

## Pin reconciliation (441519c5 vs deployed)

CI pins `sage-extensions@441519c574cec12ada06ad586f6c3862fbca96d0`; the deployed provider
research imports here is `.scratch/se-provider-6ad7a5ea/src` (source pin `6ad7a5ea`), and
the rootfs's own `/repos/sage-extensions` sits at `7b222e8`. **The results above are
evidence for the deployed `6ad7a5ea` and for nothing else**; whether `441519c5` shares the
four failures is unmeasured here.

## State of #417

Not met, and not marked done. The suite does not pass on the realized library: 4 of 13 set
-boundary tests fail on the deployed provider.

## Handoffs that remain owner-specific

1. **sage-extensions (source owner):** the subset-read contract in
   `set_categories.py:3467` rejects `{1,2} ⊆ {1,2,3}`, which four research expectations
   require; and `object_set` is still absent from the `Sets()` session surface though
   present in source. Both are source-owner items, not harness gates.
2. **Harness:** none — the owner's route works and needs no shared-runtime write. The only
   open harness question is whether `441519c5` behaves like `6ad7a5ea`, which is a CI run,
   not a local one.
