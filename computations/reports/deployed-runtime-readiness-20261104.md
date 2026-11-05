# Deployed-runtime readiness, executed (2026-11-04)

Read-only, one narrow check under `DEV-58`'s operational exception, run in the declared
shared Sage runtime as a consumer. No installation, no rebuild, no mutation of the rootfs,
no upstream edit.

## Recipe actually used (taken from `smw0_maintained-gamma_container.sh`, not guessed)

- launcher `/sage/.venv/bin/sage` inside the rootfs (not `/sage/sage`, which fails with
  `No module named 'sage'`);
- `PYTHONPATH=/repo/src:/repo/.scratch/se-provider-6ad7a5ea/src` — so the provider research
  actually runs here is the **`6ad7a5ea` snapshot**, one pin behind the audited `dca789c`,
  and *not* the rootfs's own `/repos/sage-extensions` at `7b222e8`;
- proot at `.scratch/udocker_dir/bin/proot-x86_64`, binds `/proc /dev /sys` and the repo.

## Executed result

```
from dzack_research.preamble.all import Sets, PartiallyOrderedSets, TotallyOrderedSets
IMPORT OK
partially_ordered_is_owned: True
totally_ordered_is_owned: True
object_set_present: False
```

So on the deployed runtime:

- the preamble's set layer imports and the **owned order refinements are live**:
  `Sets().PartiallyOrdered() is PartiallyOrderedSets()` and the totally-ordered analogue
  both hold;
- `Sets().object_set` is **not** reachable as an attribute of a `Sets()` instance, even
  though `object_set` exists in source (`categories/group/classifying_categories.py`,
  `categories/abstract_categories/functors.py`). This is exactly the "source present,
  runtime acceptance remains" state recorded for sage-extensions#95 — now with a run
  behind it rather than an inference.

## Per-candidate readiness on this evidence

| candidate | deployed status | evidence |
| --- | --- | --- |
| #118 own posets | **present** — owned `PartiallyOrderedSets`/`TotallyOrderedSets` are the selected refinements of `Sets()` | executed above |
| #40 End | `class End` present in deployed `mor_categories.py` | source in the deployed tree; not yet exercised by a run |
| #95 `object_set` | source present, **not exposed** on the deployed `Sets()` surface | executed above |
| #79 Subsets | ownership question; final execution owned by #238 (M3) | not run here |
| #225 dispatch | class-based `Set` dispatch remains, M2 | not run |

## Exact remaining prerequisites (not labels)

1. `object_set` exposure must land in the deployed provider before #95's runtime
   acceptance can pass; the executed check shows it absent from the surface a session can
   reach.
2. The full expectation files need the CI harness, not plain pytest: the acceptance
   workflow runs `sage_python -m pytest -p qc_sage_session -p qc_xfail_issues
   -p qc_test_history -p qc_unique_inventory` with plugins from `ai-review-ci`, and pins
   `sage-extensions@441519c574cec12ada06ad586f6c3862fbca96d0`. That pin, that plugin set,
   and the matching deployment are the runtime owner's write; none was installed here.
3. `itree next` itself cannot run in this VM: it requires an authenticated `gh`, and no
   credential exists or was created. The tree state used above therefore comes from the
   live GitHub API/connector, not from `itree`.
