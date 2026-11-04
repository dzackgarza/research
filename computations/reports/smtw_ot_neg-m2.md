# O-T: the twist identification — **negative**, with separating invariants

Member m2, direction d3, swarm `smw0dbvr6`. Repository
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo` (read-only),
evidence state `main@141058a8`. Citations by block id:

* *(A)* `writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`,
* *(H)* `writing/coble/heegner-report/coble-heegner-research-report.md`,
* *(S)* the companion document `.ultramath/smw0dbvr6/m2/O-S-saturation.md` of this run.

**Result.** The construction's pair `(I_Co,b, I_dP,b)` acting on `L_K3 = H^2(X_b,Z)` is
**not** `O(L_K3)`-conjugate to the reflection-twist pair of *(H)* `cons:reflection-twist`
— in either order of the two involutions, and regardless of how `H` is placed. The
separating invariant is the multiplicity table of the joint `(Z/2)^2` characters, or,
in its sharpest integral form, the rank of the anti-invariant lattice of the **product**
of the two involutions:

```
construction:  rank of the (-1)-eigenspace of I_Co,b I_dP,b  =  8   (det 256, negative definite)
twist:         rank of the (-1)-eigenspace of I_Co I_En      =  1   (spanned by the root, < -2 >)
```

Three further independent separating invariants are recorded in §5 (the second
involution's invariant-lattice rank `3` versus `10`; the placement of the root,
which lies in the `(+,+)`-eigenspace for the construction and in the `(-,+)`-eigenspace
for the twist; and the invariant-lattice discriminants `8` versus `1024`). §6 gives the
structural reason: the twist pair is not the pair of cohomological actions of commuting
*automorphisms* of any K3, because its product would be a reflection in a `(-2)`-vector,
and no involution of a K3 has a one-dimensional anti-invariant lattice.

Consequently `(A)` `prob:twist-identification` is **false as stated**, not merely open.
Nothing here changes the corpus's completed facts: the joint data used are the ranks of
three `+1`-eigenspaces, computed from Lefschetz/Atiyah–Bott fixed-point counts, and no
integral eigensplitting of `H^2(X,Z)` is assumed or claimed.

---

## 1. The two pairs, as defined

1.1 **The twist pair** (*(H)* §"The invariant lattice and the reflection twist",
`cons:reflection-twist` and `prop:coble-eigenspaces`). `I_En` is the Enriques
involution of the K3 lattice, `+1` on `S_En = U(2) + E_8(-2)` (rank 10, `det -1024`)
and `-1` on `T_En = U + U(2) + E_8(-2)` (rank 12); `alpha = e - f` is the root of the
first `U ⊂ T_En`, so `I_En(alpha) = -alpha`; `w_alpha` is the reflection in `alpha`;
`I_Co := w_alpha I_En`. The pair is `(I_Co, I_En)`. The two eigenlattices of `I_Co` are
computed integrally in *(H)* `prop:coble-eigenspaces`:

```
L_{K3}^{I_Co = +1} = S_En + Z.alpha  =  U(2) + E_8(-2) + <-2>   (rank 11, det 2048)
L_{K3}^{I_Co = -1} = alpha^perp_{T_En} =  <2> + U(2) + E_8(-2)  (rank 11, det -2048)
```

and the product is `I_Co . I_En = w_alpha I_En I_En = w_alpha`, a **single reflection**.
(Notation: *(H)* writes `E_8(2)` for the negative definite lattice obtained by scaling
the `E_8` form by `2`; it is `E_8(-2)` in the standard sign convention, which I use
throughout. `U(2)` has Gram matrix `[[0,2],[2,0]]`, so `U(2) = <2> + <-2>` is the
hyperbolic plane with its form doubled.)

1.2 **The construction's pair** (*(A)* `prop:local-operators`, `prop:tuple-of-the-construction`,
and *(S)* §1 for the resolved double cover `pi: X -> Yhat = Bl_p(P^1 x P^1)`, `X = X_hat_b`):

```
I_dP = deck involution (x,y,z) -> (x,y,-z),   I_Co = (x,y,z) -> (-x,-y,-z),
product  rho = I_Co I_dP = (x,y,z) -> (-x,-y,z).
H = pi^*O(1,1) (H^2 = 4),  alpha = [D] (D the exceptional (-2)-curve),  k = 1 node.
```

Their fixed loci, proved in *(A)* `prop:local-operators`, `prop:del-pezzo-type-on-the-resolution`,
`rmk:product-eight-points` (the proofs are substitution in the local model and I have
rechecked each):

```
Fix(I_dP) = B~ = normalization of B, a smooth curve of genus 9 - k = 8, chi = -14;
Fix(I_Co) = D  (the exceptional curve, fixed pointwise, chi = 2; no isolated fixed points);
Fix(rho)  = 8 isolated points  (2 over each of the three tau-fixed points of Y that
           B misses, and 2 = the points [1 : +- i : 0] of D over the node).
```

`I_dP` and `I_Co` are nonsymplectic and `rho` is symplectic
(*(A)* `prop:local-operators(2)`).

---

## 2. The conjugacy invariant used

2.1 **Multiplicities.** Let `L` be a free `Z`-module of rank 22 and `i_1, i_2` two
commuting involutions of `L`. For `eps, del ∈ {+1,-1}` let

```
L_{eps,del} = { x in L_{Q} : i_1 x = eps x,  i_2 x = del x },     n(eps,del) = rk L_{eps,del}.
```

Then `L_Q = ⊕ L_{eps,del}` and the function `n` is an `O(L)`-**conjugacy invariant of
the pair**: an isometry `phi` with `phi i_1 phi^{-1} = j_1`, `phi i_2 phi^{-1} = j_2`
maps `L_{eps,del}(i_1,i_2)` onto `L_{eps,del}(j_1,j_2)` — the joint eigenspaces are
characterised by the two linear conditions, and `phi` carries one solution space to
the other. This needs no integral eigensplitting: only the `Q`-dimensions of kernels
of integral endomorphisms are compared.

2.2 **From traces.** With `tr_1 = tr(i_1|L)`, `tr_2 = tr(i_2|L)`, `tr_p = tr(i_1 i_2|L)`,

```
4 n(+,+) = 22 + tr_1 + tr_2 + tr_p,     4 n(+,-) = 22 + tr_1 - tr_2 - tr_p,
4 n(-,+) = 22 - tr_1 + tr_2 - tr_p,     4 n(-,-) = 22 - tr_1 - tr_2 + tr_p,
```

which inverts to `rk L^{i_1=+1} = n(+,+) + n(+,-)`, `rk L^{i_2=+1} = n(+,+) + n(-,+)`,
`rk L^{(i_1 i_2)=+1} = n(+,+) + n(-,-)`; the four numbers are non-negative integers by
construction.

2.3 **Traces of geometric involutions.** For an involution `g` of a K3 surface with
fixed locus a disjoint union of points and smooth curves,
`tr(g|H^2) = chi(Fix g) - 2`: the Lefschetz fixed point formula reads
`chi(Fix g) = 2 + tr(g|H^2)` because `H^0, H^4` contribute `1` each and
`H^1 = H^3 = 0`. This is the count used in *(A)* `prop:tuple-of-the-construction(5)`;
it uses no eigensplitting.

2.4 **Traces of lattice involutions.** For an integral involution `g` of a rank-22
lattice, `tr(g) = rk(ker(g-1)) - rk(ker(g+1)) = 2 rk L^{g=+1} - 22`.

---

## 3. The twist pair's table

3.1 **(Direct computation, integral.)** With `i_1 = I_En`, `i_2 = I_Co = w_alpha I_En`:

* `x ∈ S_En` ⟹ `i_2 x = w_alpha x = x` (as `alpha ⊥ S_En`): `S_En ⊆ L_{+,+}`; and
  `L_{+,+} ⊆ L^{I_En=+1} = S_En`, so `L_{+,+} = S_En`, `n(+,+) = 10`.
* `x ∈ S_Co = S_En + Z alpha` with `x ∈ T_En = L^{I_En=-1}`: intersecting the two
  `Q`-spaces gives `Z alpha` (because `S_En ∩ T_En = 0`), so `L_{-,+} = Z alpha`,
  `n(-,+) = 1`.
* `L_{+,-} = S_En ∩ T_Co = 0`: every element of `S_En` is `I_Co`-fixed (first bullet),
  so an element that is also `I_Co`-anti-invariant vanishes; `n(+,-) = 0`.
* `L_{-,-} = T_Co = alpha^perp_{T_En}`, `n(-,-) = 11` (this is *(H)*
  `prop:coble-eigenspaces`).

So the twist's table is `(n(+,+), n(+,-), n(-,+), n(-,-)) = (10, 0, 1, 11)` in the
ordering `(I_En, I_Co)`.

3.2 **(Trace check.)** `I_En` is fixed-point-free, so `tr = 0 - 2 = -2`; `rk S_Co = 11`
gives `tr(I_Co) = 0`; `w_alpha` has `+1` on the hyperplane `alpha^perp` (rank 21), so
`tr(w_alpha) = 20`. The formulas of 2.2 then give `(10, 0, 1, 11)` — the same table,
by an independent route.

---

## 4. The construction's table

4.1 **Traces.** By 2.3 and 1.2, with `k = 1`:

```
tr(I_Co) = chi(D) - 2 = 2 - 2 = 0                 (rk S_Co = 11)
tr(I_dP) = chi(B~) - 2 = (2 - 2.8) - 2 = -16       (rk S_dP = 3)
tr(rho)  = chi(8 points) - 2 = 8 - 2 = 6           (rk S_rho = 14)
```

The ranks `11` and `3` are exactly *(A)* `prop:tuple-of-the-construction(5)`
(`k + 10` and `k + 2`), so this step is a restatement of proven corpus facts plus one
new number, `rk S_rho = 14`, which *(A)* `rmk:product-eight-points` also records.

4.2 **Multiplicities.** With `i_1 = I_Co,b`, `i_2 = I_dP,b` and 2.2:

```
n(+,+) = (22 + 0 - 16 + 6)/4 = 3,     n(+,-) = (22 + 0 + 16 - 6)/4 = 8,
n(-,+) = (22 - 0 - 16 - 6)/4 = 0,     n(-,-) = (22 + 0 + 16 + 6)/4 = 11.
```

4.3 **Independent checks.**

* `n(+,+) = 3 = rk(S_Co ∩ S_dP)` — and *(A)* `rmk:a21-open` computes that rank
  geometrically, `rk(S_Co ∩ S_dP) = k + 2 = 3`, by exhibiting `pi^*Pic(Y) + Z D`. The
  two computations agree, which is a nontrivial check on the trace `tr(rho) = 6`.
* `n(-,+) = 0`, i.e. `S_dP ⊆ S_Co` — again in agreement with *(A)* `rmk:a21-open`
  (equal ranks `3 = 3`). Note that this containment is a *consequence* here, not an
  input: the corpus records that the naive argument for it fails.
* `rk S_rho = 14 = n(+,+) + n(-,-)` ✓.
* Arithmetic: `.ultramath/smw0dbvr6/m2/scripts/verify_os_ot.py`, output §D.

4.4 **The `k = 0` member.** For a smooth branch curve (`k = 0`) the same computation
gives `tr(I_Co) = -2` (fixed-point-free Enriques involution), `tr(I_dP) = -18`
(genus-9 fixed curve), `tr(rho) = 6`, so `(n(+,+), n(+,-), n(-,+), n(-,-)) = (2, 8, 0, 12)`
with `rk S_Co = 10`, `rk S_dP = 2`, `rk S_rho = 14`. The conclusion of §5 is therefore
the same for the general (smooth) member as for the one-node member.

---

## 5. The separation

5.1 **Theorem.** There is no `phi ∈ O(L_K3)` with `phi I_Co,b phi^{-1} = I_Co` and
`phi I_dP,b phi^{-1} = I_En`; and there is none with `phi I_Co,b phi^{-1} = I_En` and
`phi I_dP,b phi^{-1} = I_Co` either.

*Proof.* By 2.1 a conjugacy of pairs preserves the multiplicity table read in the
corresponding ordering. For the **natural** correspondence `(I_Co,b, I_dP,b) <->
(I_Co, I_En)` the two tables are

```
construction, order (I_Co,b, I_dP,b) :  (n(+,+), n(+,-), n(-,+), n(-,-)) = (3, 8, 0, 11)
twist,        order (I_Co, I_En)     :  (10, 1, 0, 11)
```

(the second is §3.1's `(10, 0, 1, 11)` in the order `(I_En, I_Co)`, i.e. with the two
entries exchanged); they differ in `n(+,+)` (`3 != 10`) and in `n(+,-)` (`8 != 1`).
For the **swapped** correspondence `(I_Co,b, I_dP,b) <-> (I_En, I_Co)` the two tables are
`(3, 0, 8, 11)` (the construction's, read in the order `(I_dP,b, I_Co,b)`) and
`(10, 0, 1, 11)`; they differ in `n(+,+)` (`3 != 10`) and in `n(-,+)` (`8 != 1`). In
both cases the `(+,+)` entry alone separates. ∎

5.2 **The sharpest witness: the anti-invariant lattice of the product.** The product is
part of the pair's structure (`phi (i_1 i_2) phi^{-1} = j_1 j_2`), so its `(-1)`-eigenspace
rank is an invariant of the pair under either correspondence. It is `22 - 14 = 8` for
the construction and `22 - 21 = 1` for the twist. Integrally: for the construction this
eigenspace is a rank-8 negative-definite lattice (`rho` is symplectic, so its
anti-invariant classes are of type `(1,1)` and orthogonal to a `rho`-invariant Kähler
class, hence negative definite by the Hodge index theorem); for the twist it is
`Z.alpha ≅ <-2>`, of rank 1. Lattices of ranks `8` and `1` are not isometric, so the
products' eigenspace lattices cannot be matched either. (The construction's rank-8
lattice has determinant `256` and is `E_8(-2)` by Nikulin's classification of symplectic
K3 involutions — see 6.3; neither fact is needed, the rank suffices.)

5.3 **The second involution.** `rk S_dP = 3` (§4.1, *(A)* `prop:tuple-of-the-construction(5)`)
against `rk S_En = 10` (*(H)* `prop:coble-eigenspaces`, `S_En = U(2) + E_8(-2)`); in the
swapped correspondence, `rk S_Co,b = 11` against `rk S_En = 10`, and `rk S_dP = 3`
against `rk S_Co = 11`. Additionally the discriminants are known on both sides and
differ: `|det S_dP| = 8` with `S_dP ≅ U(2) + <-2>` (proved in *(S)*), against
`|det S_En| = 4.256 = 1024`.

5.4 **The placement of the root, and of `H`.** Both constructions have a distinguished
`(-2)`-class named `alpha`, and `(A)` `prob:twist-identification` asks for it to be
matched up to sign. For the construction:

* `alpha = [D]` is fixed by `I_Co` (*(A)* `rmk:a21-open`: `D` is fixed pointwise) and
  preserved by `I_dP` (`I_dP` acts on `D` as `[X:Y:Z] -> [X:Y:-Z]`, *(A)*
  `prop:del-pezzo-type-on-the-resolution(2)`, so `I_dP(D) = D` and `I_dP^* alpha = alpha`).
  Hence `alpha ∈ L_{+,+}`, and in fact `S_dP = Lambda = <e,f,D>` (*(S)*) with
  `alpha` one of its three generators.
* For the twist, `I_En alpha = -alpha` and `w_alpha alpha = -alpha`, so
  `I_Co alpha = w_alpha I_En alpha = +alpha`: `alpha ∈ L_{-,+}`, the `1`-dimensional
  `(-,+)`-eigenspace.

Now suppose `phi` conjugates the pairs in the natural ordering and, as
`(A)` `prob:twist-identification` demands, `phi(alpha) = ± alpha` (the two roots in
their respective lattices). Then `± alpha = phi(alpha)` would lie in `phi(L_{+,+}) =
L_{+,+}` of the twist, i.e. in `S_En`; but the twist's root is `I_En`-anti-invariant,
so it lies in `T_En`, and `S_En ∩ T_En = 0`. Contradiction. Equivalently: in the
natural ordering the construction's `(-,+)`-eigenspace is `0` while the twist's is
spanned by its root, so no non-zero vector is carried to the twist's root at all. The
requirement "`alpha` maps to `±` the twist's root" is therefore not merely unproved:
it is incompatible with the multiplicities.
`H in S_Co ∩ S_dP` (fixed by both involutions, *(A)* `prop:tuple-of-the-construction(1)`),
so `H` lies in the `3`-dimensional `(+,+)`-eigenspace; in the twist the `(+,+)`-eigenspace
is `S_En`, of rank 10, which does represent `4` (`(h_1+h_2)^2 = 4` in `U(2) ⊂ S_En`), so
the square of `H` alone separates nothing — the multiplicities above do.

5.5 **What survives of the corpus's hope.** Exactly two statements of the expected
"matching piecewise data" are true, and they are worth keeping:

* `rk S_Co,b = 11 = rk S_Co(twist)` (both Coble slots have rank 11);
* `S_dP ≅ U(2) + <-2>` (*(S)*) is *the `U(2) + <-2>` piece* of the twist's
  `S_Co = U(2) + E_8(-2) + <-2>`; that is, the construction's del-Pezzo slot embeds
  into the twist's Coble slot as the orthogonal summand `U(2) + <-2>`. What fails is
  the *second* involution: rank `3` (construction) against `10` (twist), and the
  product's anti-invariant rank `8` against `1`.

---

## 6. Structural reason: the twist pair is not a geometric pair

6.1 **Lemma.** Let `X` be a K3 surface and `g ∈ Aut(X)` an involution, `g != id`. Then
the `(-1)`-eigenspace of `g^*` in `H^2(X,Q)` has rank `≠ 1`; in fact it has rank `>= 2`
if `g` is nonsymplectic and rank `8` if `g` is symplectic.

*Proof.* If `g^* omega = -omega`, then `H^{2,0} ⊕ H^{0,2} ⊆ T_g ⊗ C`, so `rk T_g >= 2`.
If `g^* omega = omega`, then `T_g ⊆ H^{1,1}(X)`, `g` has isolated fixed points, and at
each fixed point `dg_p` has no eigenvalue `1`, hence `dg_p = -id` and
`det(1 - dg_p) = 4`. The holomorphic Lefschetz formula gives
`sum_i (-1)^i tr(g|H^i(O_X)) = |Fix| / 4`; the left side is `1 + 1 = 2` (the action on
`H^0` is trivial, `H^1(O) = 0`, and on `H^2(O_X) = C omega-bar` it is dual to the action
on `H^0(K_X)`, which is trivial). Hence `|Fix| = 8`, and then the topological Lefschetz
formula gives `tr(g|H^2) = 8 - 2 = 6`, i.e. `rk T_g = (22 - 6)/2 = 8`. ∎

6.2 **Corollary.** The twist pair `(I_Co, I_En)` is not of the form `(g_1^*, g_2^*)` for
two commuting automorphisms of one K3 surface: its product `g_1 g_2` would be an
automorphism whose `(-1)`-eigenspace has rank `1`. So the failure recorded in §5 is not
an accident of the numbers `k`, `g(B)`: no geometric pair whatsoever can realise the
twist's joint multiplicities `(10, 0, 1, 11)` with a rank-1 product eigenspace. (The
construction's own character pattern — both involutions nonsymplectic, their product
symplectic with the rank-8 anti-invariant lattice of 5.2 — is exactly what the
constraint allows.)

6.3 **Remark (not used).** By §6.1 the construction's `rho` has `rk T_rho = 8` and, by
Nikulin's classification of symplectic K3 involutions, `S_rho ≅ U^3 + E_8(-2)`,
`T_rho ≅ E_8(-2)`. That identification is *not* needed anywhere above — only the rank
`8`, which is forced by the fixed-point count — and it is stated here only to record
that the integral witness of §5.2 (det `256`, negative definite) is exactly `E_8(-2)`.

---

## 7. What is not claimed

7.1 **No claim about the type of `S_Co,b`.** The construction's Coble slot has rank 11
and contains `S_dP = U(2) + <-2>`; whether its type is the twist's `I_{1,10}(2)`
(the corpus's hypothesis `H1` in `computations/reports/sm00_arithmetic-core.md`) is
*not* decided here, in either direction. §5 removes the pair-level identification, not
that single-lattice question. Note that `S_dP = U(2)+<-2>` is an orthogonal summand of
`U(2)+E_8(-2)+<-2>`, so nothing in §5 contradicts `H1`.

7.2 **No statement about chambers, effectivity cones, or `H`-degree censuses.** The
only geometric inputs are the fixed loci of §1.2 and the ranks of *(A)*.

7.3 **No uniqueness claim about the twist's own root.** *(H)* `prop:coble-eigenspaces`
already records that the twist depends on the chosen root `alpha = e - f` of `T_En` and
that twisting by another root is not compared there. §5 rules out the identification of
`(A)` `prob:twist-identification` with the twist as constructed at *(H)*
`cons:reflection-twist`; it does not rule out that some *other* pair of lattice
involutions, built from a different root or a different Enriques involution, could be
conjugate to the construction's pair — but §6.2 shows that no such pair can come from
two commuting automorphisms of one K3 while having a rank-1 product eigenspace, so any
such alternative must have a product with an 8-dimensional anti-invariant lattice, i.e.
must not be a reflection twist at all.

---

## 8. Reproducing the numbers

* Tables, traces, ranks, and the twist's direct decomposition:
  `.ultramath/smw0dbvr6/m2/scripts/verify_os_ot.py`, output §D–E. The script only does
  integer arithmetic; the mathematical content (that the ranks are those of the
  eigenspaces) is proved in §§2–4.
* The construction's fixed loci: *(A)* `prop:local-operators`,
  `prop:del-pezzo-type-on-the-resolution`, `rmk:product-eight-points` (proofs checked by
  substitution in the local model; recorded also in
  `computations/reports/sm00_premise-ledger-d7.md` §3.5–3.6, whose `PL-6`/`PL-7b` give
  the same ranks `k+2`, `k+10`).
* The twist's eigenlattices: *(H)* `prop:coble-transcendental` and
  `prop:coble-eigenspaces`, with the discriminant/`delta` computations there.
