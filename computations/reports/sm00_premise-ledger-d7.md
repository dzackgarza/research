# Premise ledger for A21, input side

m5, swarm `smw0b9kmo`, direction `d7`. Evidence state: repository
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo`
(read-only), `main@83403bc8`, authored statement at `a145cea4a5`.

This document audits the premises that the five authored bullets of
`prob:coble-rigidity` consume **on the construction's own side** — the tuple's
existence, its lattice/numerical content, the fixed loci of its two involutions,
the resolution of its node, and the effectivity of its root. It proves the ones
that are provable, computes the ones that are finite, and names the ones that
remain open with their exact boundary. The tracked documents
`computations/reports/sm57_lean-report.md` (m4) and
`computations/reports/sm57_README.md` already carry a ledger of the *arithmetic*
of the abstract lattices and list what they did not verify: "the geometry of the
fixed loci and the Lefschetz ranks k+2 and k+10" (`sm57_lean-report.md`, §7).
Those are among the premises closed below.

## 0. Result in one line per bullet

For the direct-projective construction with one node `p` at a `tau`-fixed point
of `Y = P^1 x P^1`:

| authored bullet | status on the construction | where |
|---|---|---|
| `I_Co`, `I_dP` commuting nonsymplectic involutions | **proved** (PL-5), incl. the product being symplectic | 3.5 |
| `H^2 = 4`, fixed by both | **proved** (PL-3) | 3.3 |
| `alpha^2 = -2`, `H.alpha = 0`, `alpha` fixed by `I_Co` | **proved**; `D^2 = -2` **computed** from the blow-up, not quoted (PL-4) | 3.4 |
| "chamber in which alpha is effective and H is nef and big" | `H` nef and big **proved** (PL-3); `alpha` effective **proved** (PL-4); the wall through `H` is **rigid**: `alpha^perp` is the only effective-root wall through `H` (PL-8). The chamber clause itself is *not* an input-side statement — see §4(b) |
| `I_Co I_dP` symplectic | **proved** (PL-5) | 3.5 |
| the tuple is nonempty | **proved**: explicit member, singular locus certified exactly (PL-1) | 3.1 |
| `rho(X) >= 11` on every one-node member | **proved** here from `rk S_Co = k+10` and `S_Co` inside `H^{1,1}` (PL-6) | 3.6 |

Every "computed" line is an exact finite computation over `Q` (or `Q(sqrt(-7))`)
in `verify_input_side.py`, log `inputpremises-run.txt`; the checks are labelled
`PL-n` and cited below.

## 1. The datum, with sources

* `Y = P^1 x P^1`, rulings `f_1 = {x_1 = 0}`, `f_2 = {y_1 = 0}`, `f_1.f_2 = 1`,
  `f_i^2 = 0`, `O_Y(1,1) = f_1 + f_2`, `(O(1,1))^2 = 2`.
* `tau = [-1] x [-1]` on `Y`; its fixed points are `(0,0), (0,inf), (inf,0), (inf,inf)`.
* `B in |O_Y(4,4)|^tau` with a single node at `p = (0,0)` and smooth elsewhere;
  `B` is the *one-node locus* of `prop:one-node-family`
  (`writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`, line 544).
* `X# = Spec(O_Y + O_Y(-2,-2))` with `z^2 = f`: the double cover `pi: X# -> Y`,
  branched along `B`; `iota_dP: (x,y,z) -> (x,y,-z)` and
  `iota_Co: (x,y,z) -> (-x,-y,-z)`, `rho = iota_Co iota_dP`, exactly as in
  `prop:local-operators` / `prop:tuple-of-the-construction` (lines 495-560).
* `X^ -> X#`: the minimal resolution of the node; `D` the exceptional curve;
  `H = pi^*O_Y(1,1)`, `alpha = [D]` (`prop:tuple-of-the-construction`).
* The authored tuple is at `a145cea4a5`, `writing/coble/heegner-report/coble-heegner-research-report.md`
  lines 601-638; the five bullets are quoted in `docs/a21-tuple-hypotheses.md`.

Throughout `pi` also denotes `X^ -> Y` (the composite with the resolution); this
is harmless because every statement below is about classes, and the resolution
changes `H^2` only by adding the `D_g`.

## 2. The ledger

| # | premise | status |
|---|---|---|
| PL-1 | the one-node locus is nonempty; the corpus's explicit member has exactly one singular point and it is a nondegenerate node | **proved by exact computation** (3.1) |
| PL-2 | `X^` is a K3 surface | **proved** (3.2), hypotheses named |
| PL-3 | `H^2 = 4`; `H` fixed by both involutions; `H` nef and big | **proved** (3.3) |
| PL-4 | `D^2 = -2`; `H.D = 0`; `D` fixed pointwise by `iota_Co`; `alpha` effective | **proved**, `D^2` computed (3.4) |
| PL-5 | both involutions nonsymplectic, product symplectic; the fixed loci | **proved** (3.5) |
| PL-6 | `rk S_dP = k+2`, `rk S_Co = k+10`; and `rho(X^) >= 11` for every member | **proved** (3.6) |
| PL-7 | the node-ruling fibre, **by the dichotomy**: `a_02 != 0` gives `L_1 = D + D'` (`D'^2 = -2`, `D.D' = 2`, `H`-degrees 0 and 2); `a_02 = 0` gives Kodaira IV (`D + C_1 + C_2`, `H`-degrees 0,1,1) | **proved with the hypothesis stated** (3.7); the previous version's "for every member" was false on the `a_02 = 0` stratum |
| PL-8 | `alpha` is the only effective `(-2)`-class orthogonal to `H` | **proved for every member** (3.8) |
| PL-9 | the fibre over the other `tau`-fixed ruling `x = inf` has arithmetic genus 1 for every member; it is smooth iff its branch quartic is squarefree (open, and true for the corpus and bitangent members, false for the member D of Appendix A) | **proved with the corrected quantifier** (3.9) |
| — | the family/transport/connectedness premises (`prop:one-node-family`, `prop:one-node-connected`, `thm:one-node-transport`) | not verified here; §4(a) |
| — | the chamber clause `prob:effective-cone-agreement` | not an input-side statement; §4(b) |
| A | the `H`-degree-1 census: the corrected universal formula (including the Kodaira-IV node ruling and reducible fibres at infinity), decided exactly on four members (`0`, `4`, `2`, `2`); the curve census `0` is generic; the class count is `1`, `5`, `5`, `3` | **proved + computed** (Appendix A) |
| — | saturation of `Lambda` in `S_dP` | **open**, sharpened in §4(c) |
| — | `prob:twist-identification` | open, not needed for A21; §4(d) |

## 3. Proofs and certificates

### 3.1 PL-1: the one-node locus is nonempty (exact certificate)

The corpus's member is
`f = 29x^4y^4 + 23x^4y^2 + 19x^4 + 17x^3y^3 + 13x^3y + 11x^2y^4 + 7x^2y^2 + x^2 + 5xy^3 + xy + 3y^4 + 2y^2`
(`coble-heegner-research-report.md`, `sec-explicit-curve`, line 2417).

* `PL-1b`: `f(-x,-y) = f(x,y)`, so `f in |O(4,4)|^tau`.
* `PL-1a`: bidegree `(4,4)` with no monomial beyond it.
* `PL-1c`: quadratic part at `p` is `x^2 + xy + 2y^2`, `b^2-4ac = -7`,
  `det Hess = 7 != 0`: `p` is a nondegenerate (ordinary) node.
* `PL-1d`: `f(p) = 0` while the leading `y`-coefficient of `f(0,y)`, the leading
  `x`-coefficient of `f(x,0)` and the coefficient of `x^4y^4` are `3, 19, 29`,
  all nonzero: `p` is the only `tau`-fixed point on `B`.
* `PL-2a`/`PL-2b`: in each of the three charts `(x, 1/v)`, `(1/u, y)`,
  `(1/u, 1/v)` the ideal `(G, G_s1, G_s2)` is the unit ideal (Groebner basis
  `[1]` in *two* monomial orders), so `B` is smooth there.
* `PL-2b` in the chart `(x,y)`: the ideal `(f, f_x, f_y)` equals `(x,y)`
  (Groebner basis `[x, y]` in two orders, and `x, y` reduce to zero against it),
  so `Sing(B)` in this chart is the single reduced point `(0,0)`.

Together: `Sing(B) = {p}`, `p` an ordinary node. Hence the locus of
`prop:one-node-family` is nonempty. This re-derives the corpus's claim
independently of the tracked Groebner run; the tracked run
`sm57_member_b0_full.py`/`-run.txt` concerns the *other* member `b0`, not this
one.

Dimension check used by the corpus: `h^0(O_Y(4,4)) = 25`, the `tau`-invariant
subspace is spanned by the monomials with `i+j` even, of which there are
`3*3 + 2*2 = 13`; so the invariant system has dimension `12` and the hyperplane
`{f(p) = 0}` dimension `11` (`prop:one-node-connected`), consistently with
`evaluation at p` being a nonzero functional on the invariant system.

### 3.2 PL-2: `X^` is a K3

Hypotheses: the double-cover adjunction formula; Kunneth for `P^1 x P^1`; the
Enriques-Kodaira classification table.

(i) `X#` is smooth away from `pi^{-1}(Sing B)`: a double cover branched along a
smooth divisor is smooth (local form `w^2 = u`).
(ii) `K_{X#} = pi^*(K_Y + O_Y(2,2)) = pi^*(O(-2,-2) + O(2,2)) = O`. This is the
standard canonical class of a double cover branched along `B in |2L|` with
`pi_*O_{X#} = O_Y + L^{-1}`.
(iii) `q = h^1(O_{X#}) = h^1(O_Y) + h^1(O_Y(-2,-2)) = 0`, by Kunneth
(`H^1(P^1, O(a)) = 0` for all `a`).
(iv) `chi(O_{X#}) = chi(O_Y) + chi(O_Y(-2,-2)) = 1 + 1 = 2` using
`chi(O_Y(a,b)) = (a+1)(b+1)`; hence `p_g = chi - 1 + q = 1`.
(v) `X#` is projective (finite over the projective `Y`), `X^` is its minimal
resolution, `K_{X^}` is trivial because the resolution of an `A_1` point is
crepant, and `q, p_g` are unchanged by resolving rational double points. So `X^`
is a smooth projective surface with `K = O`, `q = 0`, `p_g = 1`, which is a K3
surface by the classification.
Cross-check: `H^2 = 4` and the lattice `U(2) + <-2>` of §3.7 sit in `H^2(X^,Z)`
of rank 22, signature `(3,19)`, as a K3 lattice requires.

### 3.3 PL-3: the degree-4 class

(1) `H^2 = 4`. For a finite morphism of degree 2 and classes `A, B` on `Y`,
`pi^*A . pi^*B = 2 (A.B)` (projection formula `pi_*(pi^*A . pi^*B) = A.B . pi_*[X]`).
With `A = B = O(1,1)` and `(O(1,1))^2 = 2f_1.f_2 = 2`: `H^2 = 2*2 = 4`
(`PL-4a`).
(2) `H` is fixed by both involutions. Both satisfy `pi o iota = iota' o pi` with
`iota' = id_Y` for `iota_dP` and `iota' = tau` for `iota_Co`; and
`tau^*O(1,1) = O(1,1)` because `[-1]^*O(1) = O(1)` on each factor. Hence
`iota^*H = pi^*(iota')^*O(1,1) = H`. Both involutions fix the node `p` and hence
lift to the blow-up `X^ -> X#` (`PL-6d` for the equation-level statement).
(3) `H` is nef: for a curve `C` on `X^`, `H.C = O(1,1).pi_*C >= 0` since
`pi_*C` is an effective 1-cycle and `O(1,1)` is nef (very ample: the Segre
embedding).
(4) `H` is big: `H^2 = 4 > 0` and `H` nef; on a projective surface a nef class
with positive square is big (Riemann-Roch: `chi(O(mH)) = m^2 H^2/2 + O(m)`, so
`h^0(mH)` grows quadratically).
(5) `H` is not ample: `H.D = 0` with `D` a curve (§3.4).

### 3.4 PL-4: the root

(1) `D^2 = -2`, **computed**. The singularity at `p` is `A_1`: by `PL-1c` the
quadratic part of `f` at `p` is nondegenerate, and over `C` a nondegenerate
binary quadratic form is linearly equivalent to `XY` (`PL-3a`, with
`x^2+xy+2y^2 = (x - a y)(x - b y)`, `a = (-1+sqrt(-7))/2`, `b = (-1-sqrt(-7))/2`,
`a != b`). So locally `X# = {Z^2 = XY}` and the resolution is the blow-up of
`C^3` at the origin. In the chart `X != 0`, writing `Y = x u`, `Z = x v`, the
proper transform is `{v^2 = u}` (smooth, `PL-3b`); in the chart `Y != 0`,
`X = y u'`, `Z = y v'`, it is `{v'^2 = u'}` (`PL-3c`). On the exceptional curve
`E` the chart relation is `v' = 1/v` (`PL-3d`), hence the transition function of
`O(E)|_E` is `y/x = 1/u = v^{-2}` (`PL-3e`): `O(E)|_E = O_{P^1}(-2)` and
`E^2 = deg = -2`.
Cross-check (independent): `E` is a smooth rational curve and the resolution of
a du Val (`A_1`) point is crepant, so `K_{X^}.E = 0` and adjunction
`(K+E).E = -2` gives `E^2 = -2`. `PL-4b` records the number.
(2) `H.D = 0`: `pi_*D = 0` because `pi` contracts `D` to `p`; so
`H.D = O(1,1).pi_*D = 0` (`PL-4c`).
(3) `alpha = [D]` is effective (it is a curve) and is fixed by `iota_Co`: on the
exceptional `P^2` the involution `(X,Y,Z) -> (-X,-Y,-Z)` is the identity
(`PL-6e`), so `D` is fixed pointwise. For `iota_dP` the action is
`(X,Y,Z) -> (X,Y,-Z)` (`PL-6f`), which preserves the conic `D = {Z^2 = X^2+Y^2}`
and hence the class `[D]`: `alpha in S_dP` as well.

### 3.5 PL-5: the characters, and the fixed loci

Let `omega` be the nowhere-vanishing holomorphic 2-form on `X^` (trivial
canonical class, §3.2), and let `iota` be an involution with `iota^*omega = eps omega`,
`eps in {+1,-1}`; `eps = -1` is "nonsymplectic". If `Fix(iota)` contains a
smooth curve `C`, then at a general point of `C` the differential `d iota` has
eigenvalues `(1,-1)` on the tangent space, hence `det d iota = -1`, and because
`omega` is nonzero there `eps = det d iota = -1`. (*Local model*: `omega = du ^ dv / z`
and `z -> -z`; `PL-6a`.)

* `Fix(iota_dP) = {z = 0} = B~`, the proper transform of `B`, i.e. the
  normalization of `B`: `(x,y,z) -> (x,y,-z)` fixes exactly `z = 0`, which on
  `X#` is the reduced curve `B`; the resolution replaces the node by the curve
  `D`, which still lies on the proper transform of `B` at its two points over the
  node. So `Fix(iota_dP)` is a smooth curve, and by the paragraph above
  `eps_dP = -1`. (`PL-6d` shows the equation is preserved.)
* `Fix(iota_Co)`: `(-x,-y,-z) = (x,y,z)` forces `tau(x,y) = (x,y)` and `z = 0`,
  that is, `pi(x,y) = p` and `(x,y) in B`; for a one-node member the only
  `tau`-fixed point on `B` is `p` (`PL-1d`), so `Fix(iota_Co)` is the curve over
  `p`, and on `X^` that is `D`, fixed pointwise. Hence `eps_Co = -1`.
* `rho = iota_Co iota_dP` acts by `(x,y,z) -> (-x,-y,z)`: on `omega` it acts by
  `eps_Co eps_dP = +1` (`PL-6c`), so `rho` is symplectic. (Consistency: a
  symplectic involution of a K3 fixes finitely many points, and the count
  `2*3 + 2 = 8` over the four `tau`-fixed points matches `rk S_rho = 14` via
  (3.6); this is a cross-check only, not used.)

The general statement "every `tau`-fixed point of `B` is singular" is worth
recording, since it is what makes the one-node condition *equivalent* to
"exactly one `tau`-fixed point on `B`": at a `tau`-fixed point `q in Y` the
involution acts on the tangent space by `-id` in suitable local coordinates, so
`f(-x,-y) = f(x,y)` kills every odd-degree term, in particular the linear part;
hence `df_q = 0`. (For the explicit member this shows up as `PL-1c`/`PL-1d`.)

### 3.6 PL-6: Lefschetz ranks, and `rho(X^) >= 11`

Hypotheses: the Lefschetz fixed point formula for a holomorphic involution of a
compact complex surface whose fixed set is a disjoint union of points and smooth
curves (the standard hypothesis; at isolated fixed points `d iota` has no
eigenvalue `1`, since its eigenvalues are roots of unity and `iota^2 = id`).

`p_a(B) = 1 + (B^2 + K_Y.B)/2 = 1 + (32 - 16)/2 = 9` (`PL-7a`), using
`B^2 = (4,4)^2 = 2*4*4 = 32` and `K_Y = O(-2,-2)`.

* `iota_dP`: `Fix = B~ = normalization(B)`, of geometric genus `9-k`; so
  `chi(Fix) = 2 - 2(9-k) = 2k - 16`.
* `iota_Co`: `Fix =` the disjoint union of the `k` curves `D_g`, each `P^1`; so
  `chi(Fix) = 2k`.

On a K3, `H^0` and `H^4` contribute trace `1` each and `H^1 = H^3 = 0`, so
`L(iota) = 2 + tr(iota^*|H^2) = chi(Fix)`. Over `Q` the involution splits
`H^2 = S + T` into its `(+1)`, `(-1)` eigenspaces, so
`tr = rk S - rk T = 2 rk S - 22`, and
`rk S = (chi(Fix) + 20)/2`. Hence
`rk S_dP = (2k-16+20)/2 = k+2`, `rk S_Co = (2k+20)/2 = k+10` (`PL-7b`).
**Only ranks are asserted**: the eigensplitting is over `Q`, and no integral
decomposition of `H^2(X^,Z)` is claimed or used; the integral refinement is a
sublattice of finite index (the corpus's `@prop:rank-one-slot` records index
`2^11` for the analogous pair).

Consequence (the `rho >= 11` premise for every one-node member). `iota_Co` is
nonsymplectic, so its action on `H^0(K_{X^})` is by `-1`; a class fixed by
`iota_Co` has no `(2,0)` or `(0,2)` component and hence is of type `(1,1)`.
Therefore `S_Co` inside `H^{1,1}(X^,R) cap H^2(X^,Z) = NS(X^) = Pic(X^)` (the
last equality is the Lefschetz `(1,1)` theorem for a projective K3), and
`rho(X^) >= rk S_Co = k + 10 = 11` for the one-node case `k = 1`.
This is the premise the corpus's rigidity statement uses; it is a theorem here.

### 3.7 PL-7 (corrected): the node-ruling fibre, by the dichotomy

The earlier version of this section asserted, "for every one-node member", that
the node-ruling fibre is `L_1 = D + D'` with `H`-degrees `0` and `2`. **That is
false**: it holds exactly on the stratum `a_02 != 0`, and the proof used that
condition silently (it called `f|_{f_1}` a double root at `p`). The correct
statement is a dichotomy, with the hypothesis named where the argument uses it.

Set-up. For a `tau`-invariant `f` with `f(p) = 0`, the terms with `x^0` are
`a_00 + a_02 y^2 + a_04 y^4` with `a_00 = 0`, because every monomial has `i+j`
even. So `f(0,y) = y^2 (a_02 + a_04 y^2)` and the intersection multiplicity of
`B` with the node ruling `f_1 = {x = 0}` at `p` is `2` iff `a_02 != 0`, and `4`
iff `a_02 = 0` (every valid member has `a_04 != 0`).

Chart. Blow up `p` in `X#` (chart `Y != 0` of `Bl_0 C^3`): `x = y u`, `z = y v`.
The proper transform of `X#` is `S~: v^2 = a_02 + a_04 y^2 + O(y)`, the
exceptional curve is `D = {y = 0}`, and the fibre divisor is
`pi^*f_1 = (x) = (y) + (u) = D + ({u = 0} cap S~)`. On `{u = 0}` the equation
is exactly

```
v^2 = a_02 + a_04 y^2.                                                 (*)
```

**Case I_2 (`a_02 != 0`).** (*) is an irreducible conic, so
`{u = 0} cap S~ = D'` is a single component: `pi^*f_1 = D + D'`, `D' ≅ P^1`,
and from `0 = (pi^*f_1)^2 = D^2 + 2 D.D' + D'^2`, `D^2 = D'^2 = -2`,
`D.D' = 2`; also `H.D = 0` (§3.4(2)) and `H.D' = H.L_1 - H.D = 2`. The
components have `H`-degrees `0` and `2`.

**Case IV (`a_02 = 0`).** (*) is `v^2 = a_04 y^2`, two lines `v = +-sqrt(a_04) y`,
so `pi^*f_1 = D + C_1 + C_2`: three components, each a `P^1`, all three passing
through the single point `(y,u,v) = 0` and pairwise transverse there. Hence
`C_1.C_2 = C_1.D = C_2.D = 1` (indeed `0 = (pi^*f_1)^2 = 3(-2) + 2*3`),
`C_i^2 = -2` (adjunction on a K3), and `H.C_1 = H.C_2 = 1`, `H.D = 0`: the
total has `H`-degree `2`, and `iota_dP` (which preserves `H`, fixes `D` and
swaps `C_1`, `C_2`) forces the two degrees to be equal. This is Kodaira type
IV with `chi_top = 3*2 - 2 = 4`.

The same dichotomy holds in the `y`-family with `a_20` in place of `a_02` (the
node ruling there is `{y = 0}`, and `f(x,0) = x^2(a_20 + a_40 x^2)`).

Both cases are verified exactly on explicit members in Appendix A
(`PL-10e`, `PL-10f`): for the corpus member `(*)` is `v^2 = 3y^2 + 2`
(irreducible), for the `a_02 = 0` member C it is `v^2 = 2y^2` (two lines).
Consequences: the `H`-degrees `0`/`2` statement of the previous run remains
valid for the members it is used on (`b0`, `bstar` are on the `I_2` side), but it
is *not* a statement about every one-node member; on the `IV` stratum the node
ruling itself carries two `H`-degree-`1` `(-2)`-curves, which is what Appendix A
now counts.

### 3.8 PL-8: `alpha` is the only effective `(-2)`-class orthogonal to `H`

Statement (every member, any `k`). If `delta` is an effective divisor class on
`X^` with `H.delta = 0`, then `delta` is a nonnegative integer combination of the
exceptional curves `D_1, ..., D_k`. In particular for the one-node case
`delta in Z_{>=0} alpha`, and `alpha` is the only effective `(-2)`-class
orthogonal to `H`.

Proof. `H = L_1 + L_2` with `L_i = pi^*f_i`. Each `L_i` is nef (pullback of a
nef class, §3.3(3)), so `L_i.delta >= 0` and `H.delta = 0` forces
`L_1.delta = L_2.delta = 0`, hence `L_i.C = 0` for every irreducible component
`C` of `delta`. If `pi(C)` were a curve `Z` of bidegree `(a,b)`, then
`pi_*C = m Z` with `m >= 1`, and `L_1.C = m (f_1.Z) = m b`,
`L_2.C = m (f_2.Z) = m a`; both zero would give `a = b = 0`. Hence `pi(C)` is a
point, so `C` is contracted by `pi`; the only curves contracted by `pi` are the
exceptional curves of the resolution. ∎

Consequence used by the corpus and by the swarm's obstruction: the only
effective-root wall through `H` is `alpha^perp` (`@lem:face-at-H`'s uniqueness
clause, there asserted; here proved). Disagreement between two members'
chambers therefore cannot come from walls through `H`: it must come from
`(-2)`-classes with `H`-degree `!= 0`, i.e. from the member's own effective cone
away from the polarization.

### 3.9 PL-9 (corrected quantifier): the fibre over the other `tau`-fixed ruling

For every member of the one-node locus the fibre over `x = inf` is a connected
curve of arithmetic genus `1`: the ruling `{inf} x P^1` meets `B` in 4 points
counted with multiplicity, and Riemann-Hurwitz gives
`2g - 2 = 2(-2) + 4 = 0`.

It is *smooth* iff the quartic `f|_{x = inf} = a_44 y^4 + a_42 y^2 + a_40` is
squarefree. That is an open condition on the member, satisfied by the corpus
member (`29y^4 + 23y^2 + 19`, squarefree: `PL-5c`) and by the bitangent member
(`y^4 + 2`), but **not by every member**: smoothness of `B` at a point of the
ruling at infinity does not force the ruling to be transverse to `B` there, and
tangency at a smooth point of `B` is allowed. Member D of Appendix A is an
explicit counterexample to the "every member" quantifier: there
`f|_{x = inf} = (y^2+1)^2`, so the fibre at infinity is reducible into two `P^1`
components of `H`-degree `1` each, and `B` is still smooth away from `p`
(`PL-10d`). The reducible case is counted in Appendix A.2.

The earlier version asserted smoothness "for every member"; the correct
statement is the one above. What survives unchanged: at the node's own ruling,
§3.7's dichotomy governs, and §3.8's census of `H`-orthogonal classes is
unaffected.

## 4. What is not verified here, with its exact boundary

(a) **The family, connectivity and transport premises.**
`prop:one-node-family`, `prop:one-node-connected`, `thm:one-node-transport`
(lines 544, 562, 609) are not verified here; they are the positive spine
(direction `d4`), and their own hypotheses are named there. My ledger uses none
of them: PL-1, PL-5 to PL-9 are statements about a single member.

(b) **The chamber clause is not an input-side statement.**
`prob:effective-cone-agreement` (line 589) quantifies over the *member's own*
effective cone, and its content is `prop:chamber-conditional` (line 662). The
input side contributes two things to it: PL-8 (at `H` itself there is only one
effective-root wall, so the clause cannot fail "at `H`"), and Appendix A below
(the `H`-degree-1 census, decided exactly there on four members: `nu_curve = 0`
on the corpus's member, `2` on a Kodaira-IV member and on an infinity-tangent
member, `4` on an explicit bitangent member). Anything that fails must fail by
roots of nonzero `H`-degree, which are not determined by the authored bullets'
data. So the ledger is consistent with, and does not itself
decide, the swarm's finding that the chamber clause is false as the corpus reads
it.

(c) **The saturation of `Lambda` in `S_dP` — a named open point, sharpened.**
`Lambda := pi^*Pic(Y) + Z D = U(2) + <-2>` has rank `2 + k = 3` for `k = 1`,
`det Lambda = 8`, and is contained in `S_dP` (the summand `pi^*Pic(Y)` because
`iota_dP` acts trivially on `Y`, the summand `ZD` because `iota_dP` preserves
`D`, §3.4(3)); `rk S_dP = 3` by §3.6. So `[S_dP : Lambda]^2 = 8 / det S_dP`,
and since `S_dP` is even of rank `3` and signature `(1,2)`, only two values are
possible:
`det S_dP = 8`, i.e. `S_dP = Lambda` (discriminant group `(Z/2)^3`, `a = 3`), or
`det S_dP = 2`, i.e. `S_dP` is isometric to `U + <-2>` (discriminant group
`Z/2`, `a = 1`). [Exact check, `lattice_saturation.py` + log: `A_Lambda = (Z/2)^3` on
`e/2, f/2, g/2` with `q(e/2) = q(f/2) = 0`, `q(g/2) = -1/2`, `q((e+f)/2) = 1`,
`b(e/2,f/2) = 1/2`; the isotropic elements of order `2` are exactly `e/2` and
`f/2`; for each the index-`2` superlattice has Gram `[[0,1,0],[1,0,0],[0,0,-2]]`
in a suitable basis, i.e. is `U + <-2>` up to isometry, even, signature `(1,2)`,
det `2`, discriminant `Z/2`. So there are exactly two candidates.]
The corpus's identification `S_dP = U(2) + <-2>` therefore requires
`det S_dP = 8`, which the Lefschetz rank count does not supply, and which is
`@rmk:a21-open`'s "saturation" in exact form. Since `rk S_Co = 11 > 3`, the same
question for `S_Co` is wider and not reducible to a determinant.
This is an open point of the corpus, unharmed by the five bullets and irrelevant
to the labels, but it is what any claim of the form "`S_dP` is the lattice
`U(2) + <-2>`" needs.

(d) **`prob:twist-identification`** (line 597): open, and by the corpus's own
decomposition not needed for A21, which quantifies only over tuples of the
construction.

(e) **The `H`-degree-1 census** used by the swarm's obstruction is *decided* on
four members and characterized structurally in Appendix A: the census is not
determined by the construction's data but by the member's effective cone (see
(b)); PL-8 shows why `H`-degree `0` is rigid while `H`-degree `!= 0` is not, and
A.2 gives the exact universal formula, including the Kodaira-IV node ruling
(`a_02 = 0`) and reducible fibres at the `tau`-fixed rulings at infinity, with
A.5 recording the relation between the curve census and the class count. What
Appendix A does not and cannot settle is the *reading* of the authored fourth
bullet, which decides whether a difference in the census refutes it.

## 5. Reproduction

```
python3 verify_input_side.py      # 33 checks, exact over Q / Q(sqrt(-7))
python3 census_hdegree.py         # 13 checks, the H-degree-1 census (Appendix A)
python3 lattice_saturation.py     #     the two candidates for S_dP (§4(c))
```

`verify_input_side.py`, `census_hdegree.py`, `lattice_saturation.py` and their
logs (`inputpremises-run.txt`, `census_hdegree-run.txt`,
`lattice_saturation-run.txt`) are in this directory. What the certificates mean: each `PL-2*` check is an identity of
ideals in `Q[x,y]` (unit ideal, or `(x,y)`), hence holds over `C`; each `PL-3*`
check is an identity of rational functions in the two blow-up charts; each
`PL-4*`, `PL-8a`, `PL-9a` check is exact integer arithmetic on the Gram matrix
`[[0,2,0],[2,0,0],[0,0,-2]]` of `(L_1, L_2, D)`, which is derived, not assumed
(§3.3(1), §3.4, §3.7). The proofs of §3.2-§3.9 are ordinary mathematics; the
computations certify only the finite statements attached to them.

## Appendix A (corrected). The `H`-degree-1 census

This appendix carries the input-side datum the chamber clause consumes. Two
different counts live here, and the previous version of this appendix conflated
them, and additionally asserted the `I_2` picture at the node ruling for *all*
members. Both defects are corrected below.

### A.0 Two counts

`nu_curve(X) = #{C in X : C an irreducible curve, C^2 = -2, H.C = 1}` — the
census of `(-2)`-curves of `H`-degree 1, i.e. of the facet-normal candidates.

`nu_class(X) = #{delta in Pic(X) : delta^2 = -2, delta.H = 1}` — the count of
all classes, which is the phrasing of the earlier run. This set is finite: the
`(-2)`-classes lie in the compact set `{x : x.H = 1, x^2 = -2} cap Pic(X)`, and
`Pic(X)` is discrete (the fibre classes `F_c` are all equal in `Pic`, since
`(x - c)/(x - c')` is a function with divisor `F_c - F_c'`).

`nu_class != nu_curve`, already on the corpus member: the class `D + F`
(`F` the ruling-fibre class, `F^2 = 0`, `H.F = 1`, `D.F = 0`) has
`(D+F)^2 = -2 - 0 + 0 = -2` and `H.(D+F) = 1`. So `nu_class >= 1` always, and
`nu_class = 0` is impossible. The obstruction's facet fingerprint uses the
*curve* census; A.5 records the exact relation.

### A.1 Effectivity

If `delta^2 = -2` and `delta.H = 1` then `h^0(delta) >= 1`: `chi(O(delta)) = 1`
on a K3 and `h^2(delta) = h^0(-delta) = 0` because `(-delta).H < 0` and `H` is
nef. So `nu_class` counts effective classes.

### A.2 The corrected universal formula

**Lemma A.2.1.** Let `delta` be an effective class with `delta.H = 1`. Then
`delta = mD + C`, where `D` is the exceptional curve, `C` is effective,
`L_2.C = 1`, `L_1.C = 0`, and `C` is supported in a fibre of one of the two
rulings. Consequently every `(-2)`-curve of `H`-degree `1` is a component of a
ruling fibre, and:

```
nu_curve = 2 * #{c in P^1 \ {0} : the x-fibre over c is reducible}
         + 2 * [a_02 = 0]
         + 2 * #{c in P^1 \ {0} : the y-fibre over c is reducible}
         + 2 * [a_20 = 0]                                              (*)
```

where in each family `P^1 \ {0}` excludes that family's node ruling (`x = 0`
resp. `y = 0`) but **includes the point at infinity**, and `a_ij` are the
coefficients of `f`. This is the referee's phrase made exact: "reducible ruling
fibres away from the node's ruling, in either ruling family" is the two sums
(with the fibres at infinity included, since they can be reducible, §3.9), and
"plus 2 in the `a_02 = 0` case at the node ruling" is stated in each family
separately — `a_02 = 0` for the `x`-family, `a_20 = 0` for the `y`-family.

Proof. `0 <= L_i.delta` and `L_1.delta + L_2.delta = 1`, so
`(L_1.delta, L_2.delta)` is `(1,0)` or `(0,1)`. Say `(0,1)`. Components with
`H`-degree `0` are exactly the exceptional curves (PL-8), so
`delta = mD + C` with `C` a *single* curve of `H`-degree `1` and multiplicity
`1` (the degrees are non-negative integers summing to `1`). An irreducible `C`
with `L_1.C = 0`, `L_2.C = 1` has `pi(C)` equal to a single ruling, hence is a
component of a fibre (the `c != 0` case of the earlier version; at `c = 0` the
component may meet `D`, which is exactly the `m` of `delta = mD + C`). For `c` off the node ruling every component has
`H`-degree `1` and `C^2 <= 0`, with `C^2 = -2` iff `C` is a `P^1` iff the fibre
is reducible into two components (a fibre `z^2 = g(y)` is reducible iff
`g = lambda h^2`). At the node ruling §3.7 applies: `a_02 != 0` gives components
of `H`-degrees `0` and `2` (nothing of degree `1`), `a_02 = 0` gives Kodaira IV
with two components of `H`-degree `1` and square `-2`. The fibre at infinity of
each family obeys the same "reducible iff `lambda h^2`" rule: tangency at a
smooth point of `B` is allowed, so it can be reducible (§3.9). ∎

### A.3 Four members, decided exactly

`census_hdegree.py`, log `census_hdegree-run.txt` (13/13 checks). Each member's
one-node validity is certified by `(f, f_x, f_y)` in the four standard charts
(`[x,y]` in the `(x,y)` chart, unit ideal in the other three).

| member | `f` | `nu_curve` | why |
|---|---|---|---|
| A: corpus (`sec-explicit-curve`) | `29x^4y^4 + 23x^4y^2 + 19x^4 + 17x^3y^3 + 13x^3y + 11x^2y^4 + 7x^2y^2 + x^2 + 5xy^3 + xy + 3y^4 + 2y^2` | `0` | no reducible ruling fibre anywhere off the node rulings, `a_02 = 2 != 0` |
| B: bitangent | `x^4y^4 + 2x^4 - x^3y^3 - x^3y + x^2y^4 - 8x^2y^2 + x^2 + xy^3 + xy + y^4 + 2y^2` | `4` | `f(+-1,y) = 3(y^2-1)^2`: two reducible `x`-rulings, `I_2` at the node |
| C: Kodaira IV | `x^4y^4 + x^4 - x^3y - 3x^2y^2 + x^2 + xy + 2y^4` | `2` | `a_02 = 0`: the node ruling is IV |
| D: infinity-tangent | `x^4y^4 + 2x^4y^2 + x^4 + x^3y^3 - 3x^2y^2 + x^2 + xy + y^4 + 2y^2` | `2` | `f|_{x=inf} = (y^2+1)^2`: the fibre at `x = inf` is reducible; `I_2` at the node |

The square-fibre test for C returns the parameter `c = 0` (because
`f(0,y) = 2y^4` is a square); that term is *excluded* from the "off the node
ruling" sum and represented instead by `[a_02 = 0]`, which is a consistency
check of the two terms of (*). In the blow-up chart of §3.7 the dichotomy is
visible directly: `PL-10e` (member A: `v^2 = 3y^2+2`, irreducible) versus
`PL-10f` (member C: `v^2 = 2y^2`, two lines).

So the one-node locus carries members with `nu_curve = 0`, `2` and `4`, and the
value `2` arises in two structurally different ways (IV node ruling; reducible
fibre at infinity) — the census formula (*) distinguishes them.

### A.4 `nu_curve = 0` is generic

`{nu_curve >= 2}` is the union of three closed subsets of the one-node locus:
the image of the incidence variety `{(b,c) : f_b(c,.) = lambda h^2}` (closed, and
closed image because `B x P^1 -> B` is proper), `{a_02 = 0}` and `{a_20 = 0}`.
It is proper, since it misses member A. Hence `nu_curve = 0` on a nonempty
Zariski-open dense subset, and the "0 vs >= 2" of the earlier run is the shadow
of that statement.

### A.5 `nu_class` in terms of `nu_curve`

For a member whose node-ruling multiplicity at `p` is `2` or `4` (every
`tau`-invariant member), `delta = mD + C` with `delta.H = 1` satisfies
`delta^2 = -2` in exactly these cases: `m = 0` and `C` an `(-2)`-component
(giving `nu_curve` classes); `m = 1` and `C = F` the fibre class (giving
`D + F`); `m = 1` and `C` an IV component at the node ruling (giving two more
per such family, since `C.D = 1` there). No other cases occur: an
`H`-degree-`1` component meets `D` at most once, so `m >= 2` is excluded. Hence

```
nu_class = nu_curve + 1 + 2*[a_02 = 0] + 2*[a_20 = 0].
```

On member A this gives `nu_class = 1`, on B `5`, on C `5`, on D `3`.

### A.6 What this does and does not settle

Settled: the one-node locus carries members with `nu_curve = 0` and members with
`nu_curve >= 2`, `nu_curve = 0` is generic, and the census is computed exactly,
in general, by (*) — with the `IV` stratum at the node ruling and reducible
fibres at infinity both accounted for. The earlier per-example claim and its
"off the tau-fixed ones" phrasing are superseded by (*).

Not settled: whether a difference in `nu_curve` refutes the authored fourth
bullet. That depends on the reading of "chosen chamber" and on what "preserving
the chamber" asks of the isometry — direction `d1`'s object, and the corpus's
`prob:chamber-conditional` (line 662) is its own form of the question.
