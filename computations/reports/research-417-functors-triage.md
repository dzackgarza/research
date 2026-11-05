# `test_functors_construct.sage`: 147 failures triaged by concrete cause

Run: the repaired file, deployed provider `6ad7a5ea`, read-only, no exclusions. Full log
`.scratch/functors-failures.txt` (800 lines). Two attributions are recorded per cause:
**raise site** (which frame pytest reports) and **defect owner** (where the behaviour must
change). They differ for missing attributes, where our test line raises because the
provider object lacks a method.

## Causes, by count

| # | cause (first failure text) | raise site | defect owner |
| --- | --- | --- | --- |
| 31 | `AttributeError: 'Owned_NativeFreeAlgebraParent_with_category' object has no attribute 'is_zero'` (with 31 `KeyError: 'is_zero'`) | test line | **provider** — the owned free-algebra parent lacks `is_zero` |
| 27 | `ValueError: base must be a ring or a subcategory of Rings()` | provider | **provider** guard rejecting a base the tests supply |
| 25 | `AssertionError: the cokernel of Generic morphism: …` | provider frame | **provider** internal assertion |
| 16 | `AttributeError: 'CommutativeAlgebras_with_category' object has no attribute 'de_rham_adjunction'` | our test line | **provider** — missing `de_rham_adjunction` |
| 10 | `ValueError: base must be a subring of this ring` | provider | **provider** guard |
| 10 | `TypeError: category() needs an argument` | provider | **provider** |
| 5 | `TypeError: cannot use OwnedJoinCategory.element_class[_SparseFreeModuleElement] as a dict key (unhashable)` | provider | **provider** — unhashable element class |
| 3 | `RecursionError: maximum recursion depth exceeded` | provider | **provider** (to confirm per case) |
| 3 | `KeyError: ((Modules, Order of rank 2 …), ())` | provider | **provider** join key |
| ~17 | `assert Free module on {…} over K in Category of vector spaces with basis over K` | our test line | **research** expectation vs provider placement — needs per-case adjudication |

## What is repaired, and what is not

- No exclusion, no skip masking, no weakened assertion was used to reach this triage.
- The research-side candidates are the ~17 category-placement assertions. They are *not*
  repaired here: each asserts an exact category name, and deciding whether the expectation
  or the provider's placement is right requires the per-case catalog comparison. Changing
  them on the strength of a count would be the weakening the brief forbids.
- Everything else is provider-owned and belongs to the existing sage-extensions channel;
  these join `FractionFieldQuotients` export as *distinct* findings, not one blended gate.

## Coverage reported honestly

This is coverage of **one file** out of 754 in `tests/constructions`; 3 errors of that file
are separate from the 147 failures. `#417`'s "the expectation suite must pass" is still not
met and is not claimed.
