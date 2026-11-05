# Comment text for dzackgarza/research#417 (prepared; connector cannot post it)

> **Posting note.** The connected GitHub route for this project is read-only for issues —
> it can read issue details and comments but offers no comment-creation action, and no
> `gh` token exists in this VM. So this text is prepared verbatim for whoever holds the
> issue-write channel. It is the text intended for #417.

---

**Standing state of the research-side acceptance (#417).**

Every measurement below was taken on the **pre-maintenance live rootfs** with the
`sage-extensions` snapshot pin `6ad7a5ea` selected through `PYTHONPATH`, read-only, and is
now marked as taken on a **superseded runtime**: Sage's verified image replaces it, so none
of these numbers may be read as acceptance until re-run there.

| measurement | commit | pin / run | result |
| --- | --- | --- | --- |
| harness route reproduced (owner's recipe) | `beea37a7a5` | `6ad7a5ea`, `/sage/.venv/bin/python -m pytest`, `-o addopts=` | 2 passed in 0.37 s (`test_set_ordering_and_mor_classification_construct`) |
| set/order/cardinality population | `c5b07e2a49` | `6ad7a5ea`, same harness, 56 files | 50 passed, 27 failed in 13.41 s |
| functors + properties | `2165f88b03` | `6ad7a5ea`, same harness, 2 files | 161 failed, 6 passed, 3 errors in 225.32 s |
| functors triage | `bd20ad6d43` | `6ad7a5ea` | 147 failures grouped by cause; 39 provider / 38 research raise sites |
| placement adjudication | `f76e156083` | `6ad7a5ea` | `FreeModules(R)` placement and `de_rham_adjunction` are provider-side; the empty nullary population was the one verified research defect |
| nullary population rebuilt | `58b0a9c315` | `6ad7a5ea` | 5 executable entries (3 pass, 2 provider-failing) + 2 blocked with causes; `-k nullary`: 4 passed, 3 failed |
| stale-name audit | `7515187e99` | `6ad7a5ea` | `NumberFields`, `AbelianGroups`, `FinitelyPresentedTorsionModules` all need provider exports; no verified rename |
| provider repair verified (not adopted) | `a394be003a` | separate binding `ad436ca5` | `FractionFieldQuotients` exports and the file collects; harness/plugin divergence on the coercion |
| runtime checkpoint | `ecb9c8bf90` | — | this session stopped its last rootfs job; zero processes at the boundary |

**Blocked, and on what.**

- `lean-categories#95–#98` — formal remainder at that owner; not a gate on this repo.
- `sage-extensions` provider defects, each measured and listed in
  `research-417-functors-triage.md` and `research-417-set-layer-batch.md`: missing
  `is_zero` on the owned free-algebra parent, `de_rham_adjunction`, `Object.order`,
  `base must be a ring` guards, cokernel assertion, join-key `KeyError`s, unhashable
  `OwnedJoinCategory.element_class`.
- provider exports with no research-side rename: `OwnedAbelianGroups`,
  `FunctionSets`, a category-level `ring_of_integers`, a torsion-module constructor.
- retained construction data: `assert power.base_set() is three` and
  `assert product.family()[0] is three` fail because the provider rebuilds the supplied
  objects — the `is` here is the retention contract, not over-strictness.
- `hypothesis` and the `qc_*` harness plugins are per-process only; nothing is installed
  into the shared runtime.

**Exact command to run when the runtime resumes** (replace the image/binding as Sage
directs; keep the stream separation):

```
PYTHONPATH="<research>/src:<provider src>:<ai-review-ci>/tool-artifacts/pytest_plugins:<hypothesis target>"
  <venv>/bin/python -m pytest -o addopts= \
    -p qc_sage_session -p qc_xfail_issues -p qc_test_history -p qc_unique_inventory \
    --qc-history-dir <writable dir> \
    tests/constructions
```

Coverage accounting: 56 of 754 construction files measured, 0 on a verified image. #417 is
not accepted; nothing here closes it.
