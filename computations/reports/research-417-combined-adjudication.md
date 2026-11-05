# Combined harness run: exact counts, raise sites, and adjudication

Both runnable-by-contract files together, under the verified route
(`/sage/.venv/bin/python -m pytest`, provider pin `6ad7a5ea`, `-o addopts=`), read-only:

```
tests/constructions/test_functors_construct.sage
tests/constructions/test_properties_construct.sage
161 failed, 6 passed, 3 errors in 225.32 s
```

Log: `.scratch/two-file-run.txt`. Raise sites split **39 provider / 38 research test** of
the failures that carry a traceback line; the remainder are assertion failures reported on
their own test lines.

## Cause census (both files)

| count | cause | owner |
| --- | --- | --- |
| 31 (+31 `KeyError: 'is_zero'`) | `Owned_NativeFreeAlgebraParent…` has no `is_zero` | provider |
| 27 | `base must be a ring or a subcategory of Rings()` | provider |
| 25 | cokernel assertion raised in provider code | provider |
| 16 | `CommutativeAlgebras…` has no `de_rham_adjunction` | provider |
| 10 | `base must be a subring of this ring` | provider |
| 10 | `category() needs an argument` | provider |
| 15 (9+6) | `KeyError: ((Modules, Free module …), ())` join keys | provider |
| 5 | `OwnedJoinCategory.element_class[…]` unhashable | provider |
| rest | assertion-level, previously adjudicated: `assert free in FreeModules(ring)` (16), stale names `NumberFields`/`AbelianGroups`/`FinitelyPresentedTorsionModules` | provider placement / provider export / missing constructor |

## Repairs made in this pass

**None, and none is justified on this evidence.** Every research-test raise site traced to
one of the already-adjudicated classes: a provider object lacking a method
(`is_zero`, `de_rham_adjunction`, `order`), a provider guard rejecting a base the catalogue
should accept, a provider join-key error, or one of the three stale names whose
replacements either do not exist or are unexported. No case was dropped and no assertion
was changed to move any count.

## Exact state

- files that run under the harness: 2; both fail
  (161 failed / 6 passed / 3 errors combined);
- a third file (`test_fraction_field_quotient_arithmetic_regression`) collects only against
  the separate `ad436ca5` binding, not the pin;
- `#417` remains unaccepted; the measured source revisions stay separate (pin `6ad7a5ea`,
  measurement binding `ad436ca5`, rootfs `/repos` copies untouched);
- no consumer pin change, no shared-runtime write, no issue write.
