# Code Thrashing Analysis — 2026-03-30

## Summary

Detected one significant thrashing incident during refactoring work (14:00-15:00 UTC).

## Incident: Task 1.1 Sextic Scripts Refactoring Bug

**Timeline:**
- `53dfefd` (14:xx): Refactored `to_affine()` and `dehomogenize_at_one()` into
  `coble_geometry.sage`
- **Bug introduced**: Changed `K_a = FractionField(A)` to `K_a.<u> = PolynomialRing(A)`
- **Impact**: Broke generic injectivity test in all three task1_1_sextic scripts
- `0f9fe03` (14:xx): Fixed by restoring `K_a = FractionField(A)`
- `5c1dcb9` (14:xx): Regenerated `task1_1_example2_results.txt` with correct output

**Root cause:** Subagent refactoring work changed ring structure without understanding
mathematical requirements.
The fraction field `K_a = FractionField(A)` was needed for the generic fiber gcd
computation to work correctly.

**Damage:**
- 3 computation scripts temporarily broken
- 1 results file regenerated
- ~3 commits to fix the regression

**Prevention:** When delegating refactoring work to subagents, explicitly specify which
mathematical invariants must be preserved (e.g., "ring structure must remain
FractionField for generic fiber computation").

## Other High-Frequency Files

**PLAN.md (15 commits):** Not thrashing.
Progressive updates as plans complete.

**GAPS.md (13 commits):** Not thrashing.
Progressive updates as gaps resolve.

**Verification notes (4-7 commits each):** Not thrashing.
Citation weaving and inline attribution additions.

## Conclusion

Only one thrashing incident detected.
The refactoring bug was caught and fixed within the same work session.
No ongoing thrashing patterns observed.

**Recommendation:** Continue current delegation patterns but add explicit mathematical
invariant preservation requirements to refactoring task prompts.
