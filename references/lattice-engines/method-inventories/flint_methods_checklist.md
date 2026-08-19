# FLINT Method Test Gap Checklist

Tracks FLINT-relevant methods documented in `docs/flint/lattice/research_readme.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. LLL Context and Reduction

### Context Initialization

- [ ] `fmpz_lll_context_init_default(fl)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"Parameter manipulation"
- [ ] `fmpz_lll_context_init(fl, delta, eta, rt, gt)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"Parameter manipulation"
      Caveat: upstream parameter constraints are `delta in (0.25, 1)` and `eta in (0.5, sqrt(delta))` (both endpoints exclusive).
- [ ] `fmpz_lll_randtest(fl, state)`

### Main LLL Functions

- [ ] `fmpz_lll(B, U, fl)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"Main LLL functions"
- [ ] `fmpz_lll_with_removal(B, U, gs_B, fl)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"Main LLL functions"
      Returns: new dimension of `B` after removal.

### LLL Variants (Floating-Point)

- [ ] `fmpz_lll_d(B, U, fl)`
      Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_d_heuristic(B, U, fl)`
      Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_d_with_removal(B, U, gs_B, fl)`
      Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_d_heuristic_with_removal(B, U, gs_B, fl)`
      Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_mpf2(B, U, prec, fl)`
- [ ] `fmpz_lll_mpf(B, U, fl)`
      Returns: 0 on success, -1 if precision maxes out.
- [ ] `fmpz_lll_mpf_with_removal(B, U, gs_B, fl)`
- [ ] `fmpz_lll_wrapper(B, U, fl)`
- [ ] `fmpz_lll_wrapper_with_removal(B, U, gs_B, fl)`
- [ ] `fmpz_lll_d_with_removal_knapsack(B, U, gs_B, fl)`
      Caveat: heuristic — may return unreduced.
- [ ] `fmpz_lll_wrapper_with_removal_knapsack(B, U, gs_B, fl)`

### ULLL (Unscheduled LLL)

- [ ] `fmpz_lll_with_removal_ulll(FM, UM, new_size, gs_B, fl)`
- [ ] `fmpz_lll_storjohann_ulll(FM, new_size, fl)`
      Caveat: not tested, use at own risk.

### LLL Reducedness Checking

- [ ] `fmpz_lll_is_reduced(B, fl, prec)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Note: `prec` is `flint_bitcnt_t` bit precision for the internal float check; return value is always conclusive.
      Returns: conclusive (non-zero if reduced, zero if not).
- [ ] `fmpz_lll_is_reduced_d(B, fl)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Caveat: Heuristic - zero return is inconclusive.
      Returns: non-zero = definitely reduced, zero = inconclusive.
- [ ] `fmpz_lll_is_reduced_mpfr(B, fl, prec)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Caveat: Heuristic - zero return is inconclusive.
- [ ] `fmpz_lll_is_reduced_with_removal(B, fl, gs_B, newd, prec)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Note: Conclusive reducedness check with removal; `prec` is `flint_bitcnt_t`.
      Returns: conclusive.
- [ ] `fmpz_lll_is_reduced_d_with_removal(B, fl, gs_B, newd)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Caveat: Heuristic - zero return is inconclusive.
- [ ] `fmpz_lll_is_reduced_mpfr_with_removal(B, fl, gs_B, newd, prec)`
      Source: `docs/flint/upstream/fmpz_lll.rst` §"LLL-reducedness"
      Caveat: Heuristic - zero return is inconclusive.

### Reducedness Checking (Direct)

- [ ] `fmpz_mat_is_reduced(A, delta, eta)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"LLL reduction"
      Caveat: low-level floating variants (`fmpz_lll_d`, `fmpz_lll_mpf`) are documented as potentially returning non-reduced output in some cases.
      Note: `delta` and `eta` are `double` LLL parameters.
- [ ] `fmpz_mat_is_reduced_gram(A, delta, eta)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"LLL reduction"
      Note: Assumes `A` is the Gram matrix of the basis.
- [ ] `fmpz_mat_is_reduced_with_removal(A, delta, eta, gs_B, newd)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"LLL reduction"
      Note: Low-level with-removal predicate.
- [ ] `fmpz_mat_is_reduced_gram_with_removal(A, delta, eta, gs_B, newd)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"LLL reduction"
      Note: Gram matrix version with removal.

### Classical LLL

- [ ] `fmpz_mat_lll_original(A, delta, eta)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Classical LLL"
      Note: Classical LLL; `delta`, `eta` are `fmpq_t` rationals.
- [ ] `fmpz_mat_lll_storjohann(A, delta, eta)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Modified LLL"
      Note: Storjohann variant with improved dimension complexity; `delta`, `eta` are `fmpq_t`.

## 2. Hermite Normal Form

- [ ] `fmpz_mat_hnf(H, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
      Aliasing: allowed.
- [ ] `fmpz_mat_hnf_transform(H, T, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
      Returns: `H` and transformation matrix `U` where `UA = H`.
- [ ] `fmpz_mat_hnf_classical(H, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_hnf_xgcd(H, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_hnf_modular(H, A, D)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
      Constraint: `A` assumed rank `n`, `D` positive multiple of det of non-zero rows of `H`.
- [ ] `fmpz_mat_hnf_modular_eldiv(H, A, D)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
      Constraint: `A` rank `n`, `D` positive multiple of largest elementary divisor.
- [ ] `fmpz_mat_hnf_minors(H, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
      Constraint: `A` assumed rank `n`.
- [ ] `fmpz_mat_hnf_pernet_stein(H, A, state)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
- [ ] `fmpz_mat_is_in_hnf(A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Hermite normal form"
      Returns: 1 if in HNF, 0 otherwise.

## 3. Smith Normal Form

- [ ] `fmpz_mat_snf(S, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"
- [ ] `fmpz_mat_snf_diagonal(S, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"
      Constraint: `A` must be diagonal matrix.
- [ ] `fmpz_mat_snf_kannan_bachem(S, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"
- [ ] `fmpz_mat_snf_iliopoulos(S, A, mod)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"
      Caveat: requires `A` to be nonsingular `n×n`.
      Constraint: `A` must be nonsingular `n x n`.
- [ ] `fmpz_mat_is_in_snf(A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Smith normal form"
      Returns: 1 if in SNF, 0 otherwise.

## 4. Gram Matrix

- [ ] `fmpz_mat_gram(B, A)`
      Source: `docs/flint/upstream/fmpz_mat.rst` §"Gram matrix"
      Description: computes Gram matrix of lattice spanned by rows of `A`.

---

## Domain Caveat

- FLINT methods here are integer-matrix and Euclidean reduction/normal-form surfaces, not indefinite genus/isometry classification APIs.

---

## References

- `docs/flint/lattice/research_readme.md`
- FLINT `fmpz_lll` docs: `https://flintlib.org/doc/fmpz_lll.html`
- FLINT `fmpz_mat` docs: `https://flintlib.org/doc/fmpz_mat.html`
- FLINT docs index: `https://flintlib.org/doc/`

