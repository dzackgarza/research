# `test_properties_construct.sage` under the owner's Hypothesis recipe

Read-only over the live rootfs, consumer-owned install, pins unchanged
(provider `6ad7a5ea`, rootfs `/repos` untouched, shared venv untouched).

## Recipe, as applied

The owner's route installs Hypothesis into a consumer-owned directory. Two corrections
were needed to run it from this workspace:

1. the venv interpreter exists only inside the rootfs, so `uv` must run **inside proot**
   against `/sage/.venv/bin/python`. A host-side `uv pip install --target` succeeds but
   produces `hypothesis._native` built for the host ABI, and the container then fails with
   `ModuleNotFoundError: No module named 'hypothesis._native'`;
2. `uv` is a binary, so it is executed as `/uv` under proot, not through the venv python.

Verified install: `hypothesis 6.170.14` + `sortedcontainers 2.4.0` into
`.scratch/py-hypothesis`, satisfying `pyproject.toml`'s `hypothesis>=6.167.1`.

```
PYTHONPATH="/repo/src:/repo/.scratch/se-provider-6ad7a5ea/src:/home/ai-review-ci/tool-artifacts/pytest_plugins:/repo/.scratch/py-hypothesis"
/sage/.venv/bin/python -m pytest -o addopts= -p qc_sage_session … test_properties_construct.sage
```

## Measured

**13 failed, 2 passed in 97.75 s** (log `.scratch/properties-run.txt`). The owner measured
15 failed in 310 s; the difference is reported rather than smoothed over — same recipe,
same pins, so at least two cases behave differently across the two runs (Hypothesis
example database state and its default example budget are the likely cause, not the
runtime).

Failure causes observed, all provider/namespace, none a missing import:

- `TypeError: unable to coerce <class 'fractions.Fraction'> to an integer` (2);
- `ValueError: cannot run a definite-lattice algorithm on Integral lattice of rank 2 …` (1);
- `TypeError: a GAP whole group map is private engine output; give generator images` (1);
- `NameError: name 'FinitelyPresentedTorsionModules' is not defined` (1);
- `NameError: name 'AbelianGroups' is not defined` (1);
- the owner's reported `FixedIsoCategory`/`KeyError: 'order'` family also appears.

The two `NameError`s are the same class of defect the nullary-functor probe found with
`NumberFields`: the expectation names a session category that the deployed provider does
not define. Those are research-side names to adjudicate against the provider's actual
exports, exactly as `OwnedNumberFields` was.

## Coverage

Two of 754 construction files have now been run under the verified harness
(`test_functors_construct`, `test_properties_construct`). `#417` remains unaccepted.
