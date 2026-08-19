# PARI/GP Method Test Gap Checklist

Tracks PARI/GP-relevant methods documented in `docs/pari_gp/lattice/research_readme.md`.
Check a box when there is at least one `method:` tagged test covering that method.

**Source citations refer to local upstream docs under `docs/pari_gp/upstream/`**

---

## 1. Reduction, Decomposition, and Isometry APIs

- [ ] `qflll(x, {flag = 0})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qflll
- [ ] `qflllgram(G, {flag = 0})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qflllgram
      Caveat: accepts positive semidefinite forms (positive quadratic form, not necessarily definite); form need not have maximal rank.
- [ ] `qfcholesky(G)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfcholesky
      Caveat: no explicit positive-definite requirement in upstream; returns `[]` if decomposition fails (when G is not positive semidefinite).
- [ ] `qfjacobi(G)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfjacobi
      Caveat: no positive-definite requirement; applies to any real symmetric matrix. Returns `[L, V]` with eigenvalues and eigenvectors.
- [ ] `qfisom(G, H, {fl}, {grp})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfisom
- [ ] `qfisominit(G, {fl}, {m})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfisominit
- [ ] `qfauto(G, {fl})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfauto
- [ ] `qfautoexport(qfa, {flag})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfautoexport
- [ ] `qforbits(G, V)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qforbits
      Caveat: expects `G` to contain `-I` and `V` to contain one representative per pair `{v, -v}`.

## 2. Vector Search and Optimization

- [ ] `forqfvec(v, q, b, expr)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §forqfvec
      Caveat: requires positive-definite form; iterates over antipodal pairs {v, -v}.
- [ ] `qfminim(x, {B}, {m}, {flag = 0})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfminim
- [ ] `qfminimize(G)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfminimize
      Caveat: requires non-degenerate form (non-zero determinant), not positive-definite. Returns `[H, U, c]` with minimized integral form.
- [ ] `qfcvp(x, t, {B}, {m}, {flag = 0})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfcvp
- [ ] `qfrep(q, B, {flag = 0})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfrep
      Caveat: requires positive-definite form per upstream.
- [ ] `qfeval({q}, x, {y})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfeval
- [ ] `qfnorm(x, {q})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfeval (marked obsolete)
      Caveat: obsolete in upstream PARI docs; prefer `qfeval`.
- [ ] `qfbil(x, y, {q})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfbil
      Caveat: **OBSOLETE** in upstream PARI docs; superseded by `qfeval`.

## 3. Indefinite / Equation-Solving APIs

- [ ] `qfsolve(G)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfsolve
      Caveat: requires rational coefficients; returns vector, matrix (isotropic subspace), or integer (prime p/-1/-2 for no solution cases); no positive-definite requirement.
- [ ] `qfparam(G, sol, {flag = 0})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfparam
- [ ] `qfsign(G)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfsign
      Caveat: returns `[p, m]` (positive and negative eigenvalues); no positive-definite requirement.

## 4. Low-Dimensional and Structural APIs

- [ ] `qfgaussred(q, {flag = 0})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfgaussred
      Caveat: singular matrices supported; no positive-definite requirement.
- [ ] `qfgaussred_positive(q)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfgaussred (lines 2169-2172)
      Caveat: **requires positive-definite** input; returns NULL if negative norm occurs; faster than generic `qfgaussred`.
- [ ] `qfperfection(G)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §qfperfection

## 5. Matrix Normal Forms (HNF/SNF)

- [ ] `mathnf(M, {flag = 0})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §mathnf
      Caveat: returns upper triangular Hermite normal form; flags 0, 1, 4, 5 control algorithm and output format.
- [ ] `mathnfmod(x, d)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §mathnfmod
      Caveat: modular HNF algorithm using determinant multiple `d`; less memory than mathnf.
- [ ] `mathnfmodid(x, d)`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §mathnfmodid
      Caveat: HNF modulo ideal `d`; returns unimodular matrix.
- [ ] `matsnf(X, {flag = 0})`
      Source: `docs/pari_gp/upstream/vectors_matrices_linear_algebra.html` §matsnf
      Caveat: returns Smith normal form elementary divisors; flags control complete output and cleanup.

---

## Definiteness and Domain Caveats

- `qflllgram` accepts positive semidefinite forms (positive quadratic form, not necessarily definite).
- `qfminim`, `qfcvp`, `qfrep`, and `forqfvec` require positive-definite forms; behavior undefined otherwise.
- `qfauto`, `qfisom`, `qfisominit`, and `qfperfection` require positive-definite forms.
- `qfminimize` requires non-degenerate form (non-zero determinant), not positive-definite.
- `qfjacobi`, `qfsign`, `qfsolve`, and `qfgaussred` have no positive-definite requirement.
- `qfgaussred_positive` requires positive-definite input (faster variant).
- Indefinite arithmetic workflows should prioritize `qfsolve`/`qfparam`/`qfsign` and isometry tools (`qfisom`, `qfauto`).

---

## References

- `docs/pari_gp/lattice/research_readme.md`
- `docs/pari_gp/upstream/pari_gp_online_provenance_2026-02-17.md`
- PARI vectors/matrices reference: `https://pari.math.u-bordeaux.fr/dochtml/html-stable/Vectors__matrices__linear_algebra_and_sets.html`
- PARI function index: `https://pari.math.u-bordeaux.fr/dochtml/html-stable/`
- PARI docs home: `https://pari.math.u-bordeaux.fr/`
