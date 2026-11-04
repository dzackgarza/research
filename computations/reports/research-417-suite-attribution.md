# #417 acceptance: source attribution corrected, and the first whole-directory findings

Continues `research-417-set-layer-run.md`. Read-only over the live rootfs; no installs, no
upstream edit, no issue write.

## Correction: which research source was under test

The first suite attempt (`jmw2fot47`) ran with `PYTHONPATH` naming only the provider
snapshot and the plugins, so `dzack_research` resolved to the rootfs's own copy at
`/repos/research` (commit `ec1333eeb0`), not to the bind-mounted repo. Verified directly:

- `src/dzack_research/preamble/all.py` is byte-identical between `/repos/research` and this
  repo (`a0ab38a6dfc6…`), which is why the earlier measurements happened to hold;
- with `PYTHONPATH="/repo/src:…"` first, `import dzack_research.preamble.all` resolves to
  `/repo/src/dzack_research/preamble/all.py` and `sage_extensions` to the `6ad7a5ea`
  snapshot.

Re-measured under that corrected attribution:

- `test_set_ordering_and_mor_classification_construct.sage` → **2 passed in 0.34 s**
  (owner: 2 passed in 0.35 s);
- the four-file set batch → **9 passed, 4 failed in 0.93 s**.

So the earlier results stand, now with the right source named.

## First whole-directory attempt (`tests/constructions`, 754 files)

Aborted with exit 4 after 2 m 18 s: pytest refuses to continue past collection errors.
Three distinct findings, only one of which belongs to the queued handoffs:

1. **Policy violation, harness-level:** `POLICY.NO_SKIP_MASK` —
   `test_functors_construct.sage::test_a_nullary_functor_sends_an_object_into_its_codomain[NOTSET]`
   "skip is never sanctioned". A skipped test in the population, reported by the project's
   own plugin.
2. **Collection error, own import surface:** `test_fraction_field_quotient_arithmetic_regression.sage`
   — `ImportError: cannot import name 'FractionFieldQuotients' from 'dzack_research.preamble.all'`.
3. **Collection error, test-side name:** `test_properties_construct.sage` —
   `ImportError: cannot import name 'COMMUTATIVE_RINGS' from 'conftest'`.

None of these is the subset-read failure or `object_set`; they are independent obligations
in this repository's own test surface, and they are recorded as such rather than folded
into the queued source-owner items.

## What is running now

`jmw2ftfaq`: the whole `tests/constructions` population with the corrected attribution and
`--continue-on-collection-errors`, so each file reports independently. Results will be
categorized per obligation when it completes.

## State

`#417` remains unaccepted: the suite has not passed. Nothing here closes it, no broad T
claim is made, and the pins are untouched (`6ad7a5ea` provider snapshot; rootfs `/repos`
copies unchanged; CI's `441519c5` still unmeasured).
