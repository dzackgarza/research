# Recomputation for entry 6

PASS.

1. `python3` exact symbolic rerun (exit 0), output `checks/exact-symbolic.txt`: both substituted polynomials P match the displayed formulas; Z8 residual discriminant -128 and Z64 residual discriminant 1024 are nonzero, so neither P is a square in C(w). The displayed E_8 Gram matrix has determinant 1.
2. `Singular -q < computations/reports/coble_807-nonclassical-sextics.sing` (exit 0), full output `checks/singular-run.txt`: absolute factor count 1 and genus 0 for both projective sextics; restriction to z=0 is x^6; singularity computations return A_15,A_1,A_1 for Z8 and A_15,A_1,A_2 for Z64, with the listed delta invariants.
3. `pandoc --from=markdown --to=native` (exit 0): the edited page parses with an empty warning log. The large native output was deleted after the check.
4. `scripts/docs_check.py --source` was run on the edited worktree and on detached omm/main with the same bibliography assets (both exit 1 for the same pre-existing corpus citations). The two outputs are byte-for-byte identical: 28 findings on other pages, none on moduli-construction.md. The earlier Har86 uses on the dependent connectedness proof were replaced by the registered HM98 source.
5. `git diff --check` exits 0. The edited page has balanced fenced-div marker count and no remaining @Har86 use.
6. The two targeted pytest commands were attempted but did not run: tests/conftest.py raises ModuleNotFoundError for dzack_research during collection (pytest exit 4). Outputs are `checks/pytest-docs-citation.txt` and `checks/pytest-printed-pages.txt`. No CI gate or Sage suite result is claimed.
