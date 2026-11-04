# A21 and the chamber clause: an elliptic-fibration model, a verified Noether–Lefschetz stratum, and the exact place where the proof stops

Member m6, swarm `smvz57fr3`, direction d6. Everything below is either proved here, cited to a named
statement of the repository at commit `cb48774f88`, or flagged as a hypothesis. Absolute repo paths are
given in the one-page summary at the end.

Conventions used throughout. `Y = P^1 x P^1` with rulings `h_1, h_2` (`h_1^2 = h_2^2 = 0`, `h_1.h_2 = 1`),
`tau(x,y) = (-x,-y)`, `p = (0,0)` the `tau`-fixed point at which the node of the branch curve sits,
`B = (f = 0)` a `tau`-invariant curve of bidegree `(4,4)` with a single ordinary node at `p` and smooth
elsewhere (`f` runs over the 13 monomials with `i+j` even; `a_00 = 0`, `a_20 x^2 + a_11 xy + a_02 y^2`
nondegenerate). `X^sharp = {z^2 = f}`, `X` its minimal resolution, `iota_dP = (x,y,-z)`,
`iota_Co = (-x,-y,-z)`, `omega = dx^dy/2z`.

---

## 0. Verdict

1. **Bullets 1,2,3,5 and the *labels* of the tuple are theorems**, for every pair of one-node members.
   §3 gives a proof that does **not** use the disputed connectedness of the one-node locus: it uses only
   that all resolved members are smooth members of one family of double covers of the *fixed* base
   `Y' = Bl_p Y`, whose parameter space is the complement of a discriminant hypersurface, hence connected.
   This is a repair of the repo's `thm:a21-labels`, whose given proof does use `prop:one-node-connected`.

2. **The chamber clause is false for the comparison isometry the whole programme uses, and the only
   sufficient condition the repo has for it is false.** The repo reduces the chamber clause
   (`prop:chamber-conditional`, path
   `writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md:662`) to: *the
   second member has no effective `(-2)`-class outside the transported set that cuts the transported
   chamber*, and records as its programme `prob:effective-cone-agreement` (`...md:591`): *the effective
   cones of the two members agree under the transport isometry.*

   * (a) **That statement is false on the one-node locus** (Theorem 4.2): §2 exhibits a one-node member
     `B` whose branch curve is bitangent to the ruling fibres `{x = 1}`, `{x = -1}`, and which carries four
     extra irreducible `(-2)`-curves `C_i` of **odd** degree against `H`; they lie outside
     `N = <L_1,L_2,D> = U(2) + <-2>`, on which `H` is even. Hence `rk Pic(X_B) >= 4 > 3 = rk Pic(X_A)` for
     a very general member `A`, and no isometry can carry `Eff(X_A)` to `Eff(X_B)`. The witness is
     computer-verified: one singular point on `B`, `f(+-1,y) = (y^2-1)^2`, and the fibre count of `B` and
     of the repo's own member.
   * (b) **The transported chamber is not the target chamber** (Theorem 4.4). For `A` very general
     (`Delta_A ⊂ N`) and `gamma` the label isometry of Lemma 3.1, there is an explicit one-parameter family
     of classes `z_t = gamma(y) + t u` (where `C_1 = (L_1+u)/2`, `u ⊥ N`, `u^2 = -8`) that lies in the
     transported chamber `gamma c_A` and violates the inequality `x.C_1 > 0` satisfied by every point of
     `c_B`. Hence `gamma c_A != c_B`.

3. **What that does and does not settle** (§4.5). The tuple statement quantifies over *all*
   `O(L_K3)`-isometries preserving the labels, i.e. over the coset `gamma.G` of the stabiliser `G` of
   `(I_Co, I_dP, H, alpha)`. So A21 for the pair is *equivalent* to the existence of `h in G` with
   `h(c_A) = gamma^{-1}c_B`, and Theorem 4.4 shows only that `h = 1` fails. I do **not** decide this coset
   question; it is a question about the action of the stabiliser on `22`-dimensional chambers, and it is
   not a statement about the construction or about periods. What *is* settled: the chamber clause is not
   a consequence of the labels, the natural sufficient condition fails, and the repo's slogan
   "more effective roots ⇒ chamber clause fails" is not valid as stated (§4.3) — the extra walls here
   contain the nef class `L_1` and so *support* the transported chamber rather than transparently cutting
   it.

4. **Under the alternative reading of the fourth bullet, A21 is a theorem** (§4.6): if the chamber is
   required to be a chamber of the arrangement cut by the *labels' own* lattice `N`, it is a function of
   `(H, alpha)` and is transported automatically. The two readings differ exactly on the members of
   Corollary 2.4.

---

## 1. The elliptic-fibration model of the construction

### 1.1 The fixed base

`X^sharp -> Y` has the single `A_1` point over `p`. Blow up `p`: `Y' = Bl_p Y`, `e` the exceptional
`(-1)`-curve. The strict transform `B~ = 4h_1 + 4h_2 - 2e` is smooth (the node had a nondegenerate
quadratic part, so the two branches become transverse points of `B~ ∩ e`), and

```
K_{Y'} = -2h_1 - 2h_2 + e,     O(B~) = O(-2K_{Y'}),     -K_{Y'} = 2h_1 + 2h_2 - e,
```

so `O(B~)` has the *fixed* square root `O(-K_{Y'})` and `X` is the double cover

```
pi : X -> Y'      branched along B~,      X = Spec(O_{Y'} + K_{Y'}),
```

which is smooth with `K_X = pi^*(K_{Y'} - K_{Y'}) = 0`, i.e. a K3. This is the repo's own model
(`prop:one-node-family`, part 1). Write

```
L_1 := pi^*h_1,   L_2 := pi^*h_2,   D := pi^*e = alpha,   H := pi^*(h_1+h_2) = L_1 + L_2,
N := <L_1, L_2, D>  =  U(2) + <-2>   (Gram: L_1^2 = L_2^2 = 0, L_1.L_2 = 2, D^2 = -2, D.L_i = 0).
```

`pi^*e = D` because the preimage of `e` is the double cover of `e` branched at `B~ ∩ e` (two points);
this is `lem:face-at-H` part 1. Then `D ≅ P^1`, `D^2 = 2e^2 = -2`, `H^2 = 4`, `H.D = 0`, `H` is nef and
big and not ample, and `alpha = [D]` is effective of square `-2` fixed by `iota_Co` — bullets 2 and 3 on
the resolved cover, as in `prop:tuple-of-the-construction`.

**Parity fact (used twice below).**

```
H.L_1 = 2,   H.L_2 = 2,   H.D = 0     ==>     H.x in 2Z  for every x in N.
```

### 1.2 Two genus-one fibrations, and their fibres

For `x_0 in P^1`: the fibre of `X -> P^1_x` (the map `pi_{x} = first ruling o pi`) is the curve
`C_{x_0} = {z^2 = f(x_0,y)}`, the double cover of `P^1_y` branched at the zero divisor of the binary
quartic `f(x_0, .)`. Its arithmetic genus is `1` because that divisor has degree `4`. Hence:

**Lemma 1.1.** `C_{x_0}` is singular iff `f(x_0,.)` is not reduced, i.e. iff the ruling fibre
`{x = x_0}` is *not* transverse to `B`; and `C_{x_0}` is then either a nodal rational curve (`I_1`) or
reducible. The analogous statements hold for the second ruling, with `L_2` in place of `L_1`.

*Proof.* `C_{x_0} -> P^1_y` is 2:1 of degree `2`; Riemann–Hurwitz for a degree-2 cover branched at a
divisor of degree `4` gives genus `1` when the divisor is reduced; a non-reduced branch divisor means a
ramification point of index `2` at a multiple point, and such a cover of `P^1` of degree `2` has genus `0`
with a node (as computed: write `f(x_0,y) = (y-a)^2 g(y)`, `deg g = 2`; then `z = (y-a)w` with
`w^2 = g(y)`, a degree-2 cover branched at the two zeros of `g`, which is a `P^1`, and the map back is
2:1 exactly at `y = a`, the node). Reducibility sets in for the other multiplicity patterns, and is
analysed in Lemma 2.1. Pathologies at `y = ∞` do not occur because `f(x_0,.)` has degree `4` in `y`. QED

**Lemma 1.2 (the fibre over `x = 0`, i.e. over the node).** Restricting to `x = 0` kills every monomial with
`x` in it, and `a_00 = 0` because `p in B`; hence `f(0,y) = y^2 (a_02 + a_04 y^2)`, which has a double root
at `y = 0`. In `X^sharp` the fibre over `x = 0` is therefore a nodal rational curve
with its node at the singular point of `X^sharp`; in the resolution `X` it becomes

```
C_0 = D + (L_1 - D),        D ≅ P^1,  (L_1 - D) ≅ P^1,  D^2 = (L_1-D)^2 = -2,  D.(L_1-D) = 2,
```

an `I_2` fibre (a 2-cycle) whose class is `L_1 = D + (L_1 - D)`.

*Proof.* Put `F_1 = {x = 0} ⊂ Y` (the ruling line through `p`), `F~_1 = h_1 - e` its strict transform in
`Y'`, `E = e` the exceptional curve, so `h_1 = F~_1 + E` in `H^2(Y',Z)` and, applying the linear `pi^*`,

```
L_1 = pi^*h_1 = pi^*F~_1 + pi^*e = pi^*F~_1 + D,
```

because `pi^{-1}(E) = D` (the preimage of `E ≅ P^1` is the double cover of `E` branched at
`E ∩ B~ = 2` points, hence a `P^1`, and it is the exceptional curve of the resolution). Now
`pi^*F~_1 = pi^*(h_1 - e) = L_1 - D` is the preimage of `F~_1`: `F~_1` meets `B~` in the two points of
`B ∩ F_1` other than `p` (there are exactly two, since `B.F_1 = 4` and the node consumes multiplicity `2`
at `p`; τ-invariance also forbids further points of `F_1` on `B` from being nodes), so `pi^*F~_1` is a 2:1
cover of `F~_1 ≅ P^1` branched at 2 points, i.e. a `P^1`, and it meets `D` at the two branch points. Hence
the fibre of `X -> P^1_x` over `x = 0`, which is `pi^{-1}(F_1) = pi^{-1}(F~_1) + pi^{-1}(E)`, is
`C_0 = (L_1 - D) + D`. Squares: `(L_1-D)^2 = 2F~_1^2 = -2`, `D.(L_1-D) = -D^2 + L_1.D = 2`, and
`(D + (L_1-D))^2 = L_1^2 = 0`. QED

**Corollary 1.3 (fibre count).** With `R = 22` the Riemann–Hurwitz number of the degree-4 map
`B^nu -> P^1_x` (`2.8 - 2 = 4(-2) + R`), the fibration `X -> P^1_x` has `R = 22` fibres of type `I_1`
generically, plus the fibre over `x = 0`, which has Euler characteristic `2` instead of `1`. Total
`22.1 + 2 = 24 = chi(K3)`. The same holds for the second fibration, with the fibre over `y = 0` equally
`D + (L_2 - D)`.

**Verified on the repo's explicit member** (`sec-explicit-curve`,
`writing/coble/heegner-report/coble-heegner-research-report.md:2407`):

```
disc_y(f) = x^2 * (a squarefree polynomial of degree 22),
```

i.e. `x = 0` contributes multiplicity `2` (the node's fibre) and the remaining `22` points are precisely
the Riemann–Hurwitz tangencies of `B -> P^1_x`. This is a check of Corollary 1.3 independent of any
lattice statement.

### 1.3 The curve dictionary

```
D,  L_1 - D,  L_2 - D  : three smooth rational curves of square -2,
D.(L_1-D) = D.(L_2-D) = 2,      (L_1-D).(L_2-D) = 2 - 0 - 0 + (-2) = 0,
H.D = 0,        H.(L_1-D) = 2,   H.(L_2-D) = 2,       L_1 = D + (L_1-D),  L_2 = D + (L_2-D).
```

`D` is the root `alpha` of the tuple; `L_1 - D` and `L_2 - D` are the other two members of the *fixed*
part of the effective root system, present on every member. `H` is positive on the last two and vanishes
on `D`: this is `lem:face-at-H`, and it is why `alpha` is singled out among the three by the labels.

---

## 2. Bitangent ruling fibres: a nonempty Noether–Lefschetz stratum, verified

**Lemma 2.1 (splitting).** Let `x_0` be such that `f(x_0,y) = c (y-a)^2 (y-b)^2` with `a != b`, `c != 0`
(equivalently: the ruling fibre `{x = x_0}` is *bitangent* to `B`, at two distinct points, each tangency
simple). Then the fibre `C_{x_0}` splits,

```
C_{x_0} = C_1 + C_2,   C_i ≅ P^1 smooth,   C_i^2 = -2,   C_1.C_2 = 2,   C_i.L_1 = 0,   C_i.L_2 = 1,
```

hence

```
C_i . H = 1   (odd),      C_i ∉ N,      C_i is an irreducible effective class of square -2.
```

*Proof.* `z^2 = c(y-a)^2(y-b)^2` gives `z = +- sqrt(c) (y-a)(y-b)`: two graphs over `P^1_y`, each a
smooth `P^1`, meeting exactly where `z = 0`, i.e. over `y = a, b`; the intersections are transversal
(the two slopes are `+-sqrt(c)(a-b) != 0` and distinct) and both points are smooth points of `X` (they lie
over points where `B` is smooth). So `C_1.C_2 = 2`. Since `x_0 != 0` the ruling line `{x = x_0}` misses the
node, so the fibre of `X -> P^1_x` over `x_0` is `pi^*(h_1) = C_1 + C_2` (a fibre: square `2h_1^2 = 0`), and
each `C_i` maps isomorphically onto it (`x_0 != 0` and the two roots are simple in the second factor), so

```
C_i.L_1 = C_i.(C_1+C_2) = C_i^2 + 2 = 0,   hence  C_i^2 = -2,
C_i.L_2 = (pi_* C_i).h_2 = h_1.h_2 = 1,    hence  C_i.H = C_i.L_1 + C_i.L_2 = 1.
```

Odd degree forces `C_i ∉ N` by the parity fact of §1.1. QED

**Remark 2.2.** `tau`-invariance makes the bitangency at `x_0` reappear at `-x_0`; so a member with one
bitangent ruling fibre has at least two, hence at least four extra irreducible `(-2)`-curves.

**Theorem 2.3 (existence, with a verified member).** There is a one-node member whose branch curve is
bitangent to `{x = 1}` and `{x = -1}`. Explicitly, the `tau`-invariant

```
f_B = -2x^2 - xy - 6y^2 + x^2y^2 + x^3y - x^3y^3 + 4xy^3 - 3x^2y^4 - 4x^4y^4 + 3x^4y^2 + 3x^4 + 8y^4
```

(i.e. coefficients `a_20 = -2, a_11 = -1, a_02 = -6, a_22 = 1, a_31 = 1, a_33 = -4, a_13 = 4,
a_24 = -3, a_44 = -4, a_42 = 3, a_40 = 3, a_04 = 8, a_00 = 0`) satisfies

1. `f_B(0,0) = 0`, quadratic part `-2x^2 - xy - 6y^2` nondegenerate (discriminant `1 - 48 = -47`);
2. `B` has **exactly one** singular point, `(0,0)` in the chart `x_0 = y_0 = 1`, and is smooth on all
   three other standard charts (Gröbner basis of `(F, F_u, F_v)` in each chart, `solve_poly_system`;
   see `verify_members.py`, log `verify_members.log`);
3. no ruling line is a component of `B`;
4. `f_B(1,y) = y^4 - 2y^2 + 1 = (y^2-1)^2` and `f_B(-1,y) = f_B(1,-y) = (y^2-1)^2`;

so `B` is a one-node member of the direct construction, and by Lemma 2.1 it carries four extra irreducible
`(-2)`-curves `C_1, C_2` over `x = 1` and `C_1', C_2'` over `x = -1`, all of `H`-degree `1`.

**Verified corroboration of the fibre count** for this member:

```
disc_y(f_B) = -x^2 (x-1)^2 (x+1)^2 (degree-18 factor),
```

so of the `R = 22` Riemann–Hurwitz tangencies exactly `4` sit over `x = +-1` (two simple tangencies over
each), the remaining tangencies are the `18` roots of the last factor, and the node contributes `x = 0`
with multiplicity `2`: `4 + 18 = 22`. For the repo's member the same computation gives
`disc_y(f_A) = x^2 * (squarefree of degree 22)`, with `f_A(1,y)` having four distinct roots: the repo's
member has *no* bitangent ruling fibre.

**Corollary 2.4 (the family has a nonempty Noether–Lefschetz stratum).** `rk Pic(X_B) >= 4`, because
`N ⊂ Pic(X_B)` has rank `3` and `C_1 ∈ Pic(X_B)` satisfies `C_1 ∉ N`. On the other hand, for `b` outside
the Noether–Lefschetz locus of the family, `Pic(X_b) = N` and `rk Pic(X_b) = 3`. [Hypothesis, standard:
the Noether–Lefschetz locus of a non-isotrivial family of K3 surfaces is a countable union of proper
closed subsets — local Torelli makes each stratum proper, and a countable union of proper closed analytic
subsets of the (locally compact, hence Baire) parameter space is meagre. The family is non-isotrivial
because two of its members, `X_A` and `X_B`, have Picard lattices of different rank by the above.]

Hence the answer to the disputed question "does the family have an NL stratification" is **yes**, and its
strata are explicit: bitangency conditions of `B` with ruling fibres, of which bitangency at two points of
one fibre is codimension `2` in the `9`-dimensional family.

---

## 3. The labels: a proof that avoids the disputed connectedness

The repo proves `thm:a21-labels` (`.../the-heegner-line...md:578`) from `prop:one-node-connected`
(`...md:562`), which is the one geometric input listed as *disputed* in the swarm's problem statement.
The following proof uses no connectedness of the one-node locus. It replaces that input by the
connectivity of the complement of a discriminant hypersurface.

**Lemma 3.1.** For any two one-node members `b, b'` there is an isometry
`gamma : H^2(X_b,Z) -> H^2(X_{b'},Z)` carrying

```
I_Co -> I_Co,   I_dP -> I_dP,   H -> H,   alpha -> alpha,   L_1 -> L_1,   L_2 -> L_2.
```

*Proof.* By §1.1 both `X_b` and `X_{b'}` are double covers of the **same** base `Y' = Bl_p Y`, branched
along smooth divisors `B~_b, B~_{b'}` of the **same** class `-2K_{Y'}`, with the **same** square root
`O(-K_{Y'})` (the class `-K_{Y'}` is fixed because `K_{Y'}` is). Consider the family

```
Tot = { (s, x) : s in |O(-2K_{Y'})|,  x in the double cover branched along div(s) } -> |O(-2K_{Y'})|
```

(the relative `Spec` of `O + O(-K_{Y'})` with the algebra structure given by `s`). Over the complement of
the discriminant — the locus of singular divisors — the fibre is a smooth K3 and the family is smooth and
proper. The discriminant is a proper closed algebraic subset of the projective space
`|O(-2K_{Y'})|`, hence of real codimension at least `2`, so its complement is **connected** (indeed
path-connected). `H, alpha, L_1, L_2, D` are `pi^*` of classes fixed on `Y'` (`alpha = pi^*e`,
`H = pi^*(h_1+h_2)`, and the same for `L_i`), hence are flat sections of `R^2 pi_* Z` restricted to the
family; `I_dP` is the deck transformation of the family of double covers, and `I_Co` is the lift of the
fixed involution `tau~` of `Y'` (which acts on the total space because it preserves the linear system).
Ehresmann's theorem therefore gives, for any two members, a diffeomorphism of the total spaces over the
base of the family, and differential-geometric parallel transport along a path in the connected complement
of the discriminant is an isometry of `H^2` intertwining all of the listed structure. QED

**Corollary 3.2.** Bullets 1, 2, 3, 5 and the *labels* (`I_Co, I_dP, H, alpha`) of A21 are conjugate for
every pair of one-node members: after choosing markings, `gamma in O(L_K3)` as in `thm:a21-labels`, with
no reliance on `prop:one-node-connected`.

*Remark 3.3.* This is a strict improvement in the hypotheses, not a new conclusion: the conclusion is
`thm:a21-labels`. It matters because the connectedness argument is disputed in the problem statement
("two prior proofs failed"): with Lemma 3.1 the label clause no longer depends on it, and the whole of
A21's remaining content is the chamber.

---

## 4. The chamber clause

### 4.1 The definitions in force

As in `rmk:chamber-not-transported` (`...md:657`): for a K3 surface `X`, `C_X ⊂ H^2(X,R)` is a component of
`{x^2 > 0}`, `Delta_X ⊂ Pic(X)` is the set of effective classes of square `-2`, the Kähler cone is
`K_X = {x in C_X : x.delta > 0 for all delta in Delta_X}`, and the tuple's chamber is the component
`c_X` of `C_X minus the union of delta^perp`, `delta in Delta_X`, that contains `K_X`. `H` nef and big and
`alpha` effective are then conditions on the member. This is the reading under which the fourth bullet is
not vacuous and under which `prop:chamber-conditional` is stated.

### 4.2 Theorem (the effective cones do not agree)

Let `b` be a member with `Pic(X_b) = N` (Corollary 2.4) and let `B` be the member of Theorem 2.3. Let
`gamma` be the label isometry of Lemma 3.1. Then

```
gamma(Eff(X_b))  !=  Eff(X_B)  as cones,
```

indeed `dim span Eff(X_b) = rk Pic(X_b) = 3` while `dim span Eff(X_B) = rk Pic(X_B) >= 4`. More sharply,
and *without* any genericity: `Delta_B` contains the classes `C_i` with `C_i.H = 1`, while `gamma Delta_b`
consists of classes of even `H`-degree; so `C_i ∉ gamma Delta_b` for every label-preserving isometry
`gamma` (with `gamma H = H`, `gamma N = N` as in Lemma 3.1).

Consequently `prob:effective-cone-agreement` (`...md:591`), the statement the repo names as the content of
the chamber clause, is **false** as a statement about the one-node locus.

### 4.3 The extra classes are half-integral over `N`, and why "more roots" is not by itself decisive

Write `u := 2C_1 - L_1`. Using `C_1.L_1 = 0`, `C_1.L_2 = 1`, `C_1.D = 0`, `C_1^2 = -2` (Lemma 2.1) one
computes

```
u.L_1 = u.L_2 = u.D = 0   (so u is orthogonal to N),      u^2 = -8,      C_1 = (L_1 + u)/2,   u.C_1 = -4.
```

(In coordinates: `u = 2C_1 - L_1` is the integral class the bitangency produces; it is a `(-8)`-class in
`N^perp`, a rank-19 lattice.) Checked symbolically in `lattice_check.py`.

**Correction of the repo's remark.** The remark at `...md:657` concludes from `Delta_{b'} > gamma Delta_b`
that `gamma c_b` is "a union of chambers and not a chamber", hence that the chamber clause fails. As stated
that implication is not a theorem, and in this witness the extra classes are not of the expected kind: they
satisfy

```
C_i . L_1 = 0        with  L_1  nef,
```

so the new wall `C_i^perp` contains the nef boundary class `L_1` and *supports* the transported chamber
there. Whether a wall supports or cuts is not decided by the sets `Delta`; it needs the `22`-dimensional
cone. The next theorem decides it for the extra class by using the half-integrality of §4.3.

### 4.4 Theorem (the transported chamber is not the target chamber)

With `b` very general (`Delta_b ⊂ N`), `B` as in Theorem 2.3, and `gamma` the label isometry of Lemma 3.1
(so `gamma H = H`, `gamma N = N`, `gamma L_1 = L_1`):

```
gamma c_b  !=  c_B .
```

*Proof.* By §4.1 and the sign-pattern argument, a chamber is recovered from its defining half-spaces:

```
c_X = {x in C_X : x.delta > 0 for all delta in Delta_X}
```

(this set is convex and open in `C_X`, hence lies in exactly one component, so it *is* the component
containing the Kähler cone). Choose a Kähler class `y in K_b` with `y.L_1 = lambda` small: possible because
`K_b` is open in `N tensor R` and `y.L_1` is not invariant under all of `K_b` (subtracting a small multiple
of `L_2` from any Kähler class lowers `y.L_1` by `2s` and stays Kähler). Put

```
z_t := gamma(y) + t u ,      lambda/8 < t < |y|/sqrt(8).
```

Such a `t` exists once `lambda/8 < |y|/sqrt(8)`, i.e. `lambda < sqrt(8)|y|`; then (i)
`z_t^2 = y^2 + 2t gamma(y).u + t^2 u^2 = y^2 - 8 t^2 > 0`, because `gamma(y) in N tensor R` is orthogonal
to `u`; (ii) for every `delta in Delta_b`, `z_t . gamma(delta) = y.delta + t (u . gamma(delta)) = y.delta > 0`,
because `gamma(delta) in gamma N = N` and `u ⊥ N`; hence `z_t ∈ gamma c_b`; (iii)
`z_t.C_1 = gamma(y).C_1 - 4t = lambda/2 - 4t < 0`. But `C_1 in Delta_B`, so every point of `c_B` satisfies
`x.C_1 > 0`. Hence `z_t ∈ gamma c_b` while `z_t ∉ c_B`, i.e. `gamma c_b ≠ c_B`. QED

### 4.5 What remains: the coset question, stated exactly

A21 asks for *some* `g in O(L_K3)` with `g(I_Co) = I_Co'`, `g(I_dP) = I_dP'`, `gH = H'`, `g alpha = alpha'`
(these are automatic for the coset below) and `g c = c'`. By Lemma 3.1 the set of isometries carrying the
labels of `b` to those of `B` is the coset `gamma.G`, where

```
G := { h in O(L_K3) : h commutes with both I_Co, I_dP,  hH = H,  h alpha = alpha } .
```

So, for the witness pair,

```
A21 holds  <=>  there exists h in G with h(c_b) = gamma^{-1} c_B .
```

Theorem 4.4 says that `h = 1` does not work; it does **not** decide the coset. The proof of A21 therefore
stops exactly here, and this is the missing statement:

> **(C-coset)** For every pair of one-node members `b, b'`, the coset `gamma.G` contains an isometry
> carrying the chamber `c_b` to `c_{b'}`. Equivalently (by `prop:chamber-conditional`): some isometry in
> the coset has the property that no effective `(-2)`-class of `b'` outside its transported set cuts the
> transported chamber.

Two further facts about (C-coset), both established here.

1. Its natural sufficient condition is **false**: agreement of the effective root systems fails
   (Theorem 4.2). And the *canonical* choice `h = 1` fails (Theorem 4.4).
2. It *does* hold whenever both chambers are pinned by the labels, i.e. whenever the non-accumulation
   hypothesis of `prop:chamber-pinned` (`...md:643`) holds at both members: then `c_X` is a function of
   `(H, alpha)`, and `gamma.G` acts trivially on `(H, alpha)`. For members with `Pic = N` the hypothesis
   holds (finitely many effective roots, all of `H`-degree `>= 2` or `0`); for members with larger Picard
   lattice it fails, since effective roots have `|delta.H| >= 1` with `|delta|` unbounded, so their walls
   accumulate at `H`. Hence (C-coset) is *not* vacuous, and A21 is not a consequence of the local system.

Whether (C-coset) is true is, in my judgement, the honest open question behind the authored chamber
clause; the reduction above is exactly the form in which it can be attacked.

### 4.6 The other reading of the fourth bullet, under which A21 is closed

If instead the chamber of the tuple is defined as a chamber of the arrangement cut by the classes of the
*labels' own* lattice `N = <L_1, L_2, D>` — a reading that uses only data the tuple carries up to the
labels, and that makes `c` comparable across members — then by `lem:face-at-H` the only wall through `H` is
`alpha^perp`, exactly two components have `H` in their closure, and exactly one of them is positive on
`alpha`; so `c` is a *function* of `(H, alpha)`, hence transported by `gamma`, and A21 holds in full (labels
by Corollary 3.2, chamber by this paragraph).

The two readings differ exactly on the members with larger effective root systems (Corollary 2.4). A21 is a
theorem under the second reading and open under the first, and the difference is a statement about how the
tuple's fourth item is defined — not a missing computation about the construction.

---

## 5. Clause-by-clause status of the authored tuple, with sources

| clause | status | where |
|---|---|---|
| (1) `I_Co`, `I_dP` commuting nonsymplectic involutions | theorem | `prop:local-operators`; `iota_Co^* omega = -omega`, `iota_dP^* omega = -omega`, product `+1` |
| (2) `H^2 = 4`, fixed by both | theorem | `H = pi^*(h_1+h_2)`, `pi` of degree 2, `tau^*(h_1+h_2) = h_1+h_2`, deck acts trivially on pullbacks |
| (3) `alpha^2 = -2`, `H.alpha = 0`, `alpha` fixed by `I_Co` | theorem | §1.1, §1.3; `lem:face-at-H` (1); `iota_Co` fixes `D` pointwise |
| (4) chamber `c`, `alpha` effective, `H` nef and big | definition; exists | §4.1; `H` nef and big because `O(1,1)` is ample and `H^2 = 4 > 0`; `alpha = [D]` |
| (5) product symplectic | theorem | §0 and `prop:product-of-involutions` |
| **labels conjugate for all pairs** | **theorem** | Lemma 3.1 + Corollary 3.2 (independent of `prop:one-node-connected`) |
| **chamber clause for all pairs** | **open**; false for the canonical (transport) comparison, and not a consequence of agreeing effective roots | §4; `prob:effective-cone-agreement` false (Theorem 4.2, verified witness); `gamma c != c'` for the transport isometry (Theorem 4.4); residual = (C-coset) of §4.5 |
| saturation of `N` in `S_dP` / twist identification | not my object | repo `rmk:a21-open`, `prob:twist-identification` |

Two auxiliary facts proved here that the repo records as open or as slogans:

* the construction's family has **nonempty NL strata**, explicitly: bitangency of `B` with a ruling fibre
  gives four extra irreducible `(-2)`-curves of odd `H`-degree (Theorem 2.3, Corollary 2.4);
* the implication "larger effective root system ⇒ chamber clause fails" is **not valid as stated**; the
  correct criterion is (C-coset) of §4.5, and the canonical comparison fails by §4.4.

---

## 6. One-page summary: sources, and where each premise comes from

**The problem.** Authored A21 tuple and the direct projective construction:
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo/writing/coble/heegner-report/coble-heegner-research-report.md`,
lines 341-470 (construction), 470-700 (lattice package, tuple, rigidity problem), 2407-2425 (explicit
member). Repository at commit `cb48774f88`.

**Repo statements used, with their own status.**

* `lem:node-condition`, `sec-invariant-system` (dimension 13, `a_00 = 0`, nondegenerate quadratic part):
  report lines 355-380. Used as the definition of the one-node locus.
* `prop:one-node-family` part 1: the simultaneous resolution, `X = Spec(O + K_{Y'})`. Used in §1.1, §3.
* `lem:face-at-H` (1),(2),(4) (`.../writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md:621`):
  `alpha = pi^*e`; the curves contracted by `pi` are the ray of `alpha`; the only effective `(-2)`-class
  orthogonal to `H` is `alpha`. Used in §1.1, §1.3, §4.6.
* `prop:chamber-conditional` (`...md:662`) and `rmk:chamber-not-transported` (`...md:657`): the definition
  of the chamber and the reduction of the chamber clause. Used in §4; the remark's implication is
  corrected in §4.3.
* `prop:chamber-pinned` (`...md:643`): pinning under non-accumulation. Used in §4.5.
* `prob:effective-cone-agreement` (`...md:591`): the sufficient condition. **Refuted** in Theorem 4.2.
* `thm:a21-labels` (`...md:578`), `prop:one-node-connected` (`...md:562`): the repo's label theorem and its
  disputed input. The conclusion is re-proved without the disputed input in Lemma 3.1.
* `rmk:a21-open`, `prob:twist-identification`: untouched here.
* `sec-explicit-curve` (report line 2407): the repo's explicit member, used as member A.

**Premises that are hypotheses, not theorems, and are named as such.**

1. *Noether–Lefschetz genericity* (§2.4): `Pic(X_b) = N` for `b` outside a countable union of proper
   closed subsets. Standard (local Torelli + Baire); not re-proved here. Used only for the *rank* `3`
   half of Theorem 4.2; the parity half (`C_i ∉ gamma Delta_b`) uses no genericity.
2. *The chamber is the `rmk:chamber-not-transported` chamber* (§4.1). This is a reading of the fourth
   bullet, the one the repo adopts; §4.6 states the alternative reading under which A21 is closed.
3. *Ehresmann's theorem* and *path-connectedness of the complement of a complex hypersurface* (§3).
   Standard differential topology, applied to an explicit family.

**Computations (all in `.ultramath/smvz57fr3/m6/`, run with `python3` + `sympy`).**

* `verify_members.py`, log `verify_members.log`: for member A (the repo's polynomial) and member B
  (Theorem 2.3), the singular locus of `B` on all four standard affine charts of `P^1 x P^1` by Gröbner
  bases (`solve_poly_system`); `tau`-invariance; the quadratic part and its discriminant; the roots of
  `f(+-1,y)`, `f(0,y)`; the factorization of `disc_y(f)`. Results: exactly one singular point each, at
  `p`; member A `disc = x^2 * (degree 22, squarefree)`; member B `disc = -x^2(x-1)^2(x+1)^2 * (degree 18)`
  and `f(+-1,y) = (y^2-1)^2`.
* `extra.py`: squarefreeness of the degree-22 factor for member A, and the discriminant of `f(1,y)` for
  both members (`82523781968 != 0` for A, `0` for B).
* `lattice_check.py`: the class identities of §4.3 — `C_1 = (L_1+u)/2` with `u = 2C_1 - L_1` orthogonal to
  `N`, `u^2 = -8`, `u.C_1 = -4`, and `C_i.L_1 = 0`, `C_i.L_2 = 1`, `C_i.H = 1` in the Gram matrix of `N`.

**What I did not do.** I did not compute the chambers `c_b` (they are cones in `R^22` cut by infinitely
many walls); I did not decide (C) for the witness pair; I did not touch the saturation question for
`S_dP` or the twist identification.
