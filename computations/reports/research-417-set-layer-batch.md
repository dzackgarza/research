# Set-layer batch, cause census, and the bindings correction

## Correction: my earlier "outside the harness" comparison was not the same binding

Sage's measurement at `66ac2466e0b8` settles it: `qc_sage_session` injects
`vars(sage.all_cmdline)` into builtins, so an unqualified `ZZ` in a test file is **global
Sage's** ring, not the provider's session ring. My probe imported `ZZ` from the preamble in
a plain, non-preparsed script — a different binding — so "the identical expressions succeed
outside the harness" was not like-for-like. The accurate statement is the provider's: under
the harness bindings the coercion is rejected at `ring_foundation.py`, and Sage-preparser
`Integer` literals are the correct form. The test is unchanged; this is a provider contract
question, not a research repair.

## Wider measurement than two files

56 construction files of the set/order/cardinality population, one harness pass, pin
`6ad7a5ea`, read-only:

**50 passed, 27 failed in 13.41 s** (log `.scratch/set-layer-batch.txt`).

Cause census of the 27:

| count | cause | owner |
| --- | --- | --- |
| 8 | `KeyError: ((N-dimensional cone with rays …), …)` toric join keys | provider |
| 5 | `assert {…} is {…}` identity assertions on two constructed sets | **to adjudicate** |
| 3 | `NameError: name 'FunctionSets' is not defined` | stale name → provider export (class exists at `set_categories.py:3663`, not exported) |
| 3 | `AssertionError: cannot give the morphism N -> N of cardinals` | provider |
| 2 | `ValueError: the whole-algebra map for Free module …` | provider |
| 2 | `KeyError: 'factors'` | provider |
| 2 | `OwnedJoinCategory.parent_class` has no attribute | provider |

## Original collection blockers, accounted for

| blocker | state |
| --- | --- |
| `POLICY.NO_SKIP_MASK` (empty parametrization) | repaired `32519d79e8`; population 5 executable + 2 blocked |
| `COMMUTATIVE_RINGS` from `conftest` | repaired `32519d79e8` |
| `hypothesis` | resolved per-process in `.scratch/py-hypothesis`; no shared install |
| `FractionFieldQuotients` export | repaired upstream `ad436ca5`, verified via separate binding, **not adopted** |

## Coverage

Measured: 56 of 754 construction files (as part of the population, not a suite). 698 remain
unmeasured. `#417` stays unaccepted; isolated measurement against a current-provider
binding is not adoption, and no pin or shared-runtime change was made.
