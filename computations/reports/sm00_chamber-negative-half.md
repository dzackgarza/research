# A21's chamber clause is false: corrected section, with proofs

Member m2, swarm `smw0b9kmo`, direction d5. Repo cited by path; not modified. My own
computations are `verify_members.py` and its log `verify_members-run.txt`, in this
directory; every number quoted below is printed there (sympy over `Q`, Gröbner and
elimination over `Q`; an elimination ideal equal to `⟨1⟩` means *no* solution over any
extension field, i.e. over the algebraic closure).

Everything is proved; the only inputs I do not reprove are named and located in §9.
Nothing here asserts an integral eigensplitting of `H²(X,Z)`, and the "label-own"
reading is kept as one *named* alternative (§7, R1), not used as a substitute.

---

## 0. Verdict

1. **(Theorem 9, §6.)** Let `b₀`, `b★` be the two one-node members of §1, and let
   `𝔠₀`, `𝔠★` be the chambers carried by their tuples. There is **no** isometry
   `γ : H²(X_{b₀},Z) → H²(X_{b★},Z)` of `L_K3` with `γH₀ = H★`, `γα₀ = α★` and
   `γ(𝔠₀) = 𝔠★` — in every reading of the fourth authored bullet under which that
   bullet constrains the member's own cone (§7, R2–R5), **including the reading the
   corpus itself adopts** (`rmk:chamber-not-transported`,
   `writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md:651`,
   where the chamber is placed in `C_X ⊂ H²(X,R)`). Hence the authored claim of
   `writing/coble/heegner-report/coble-heegner-research-report.md:601–638`
   (rev `a145cea4a5`) is false, and the failure is exactly at the fourth bullet:
   `thm:a21-labels` (`…the-heegner-line…md:578`) already produces a `γ` preserving the
   labels, `H` and `α`, so only the chamber is left, and it is not transportable.
2. **(§7.)** The fourth bullet's quantifier: `H·α = 0` with `α` an effective `(−2)`-class
   is forced on every member, so `H` lies on a wall of the effective-root arrangement
   and is **never** interior to a chamber. The authored words "chamber in which … `H` is
   nef and big" can therefore only mean *a chamber whose closure contains `H`*, with
   "nef and big" a property of `H` itself. Every reading that survives the authored text
   is listed in §7; the corpus's adopted one is R5.
3. **What is new here relative to the tracked evidence** (§10): the facet step that the
   tracked proof left open at `b★` is proved *without* Grauert, Artin, or a contraction —
   by an explicit nef-and-big class `y = 2H★ − α★ + C₊ + e_b` (`y² = 24`, `y·C₊ = 0`,
   `y·δ ≥ 1` for *every* effective class `δ ∉ {0, C₊}`) together with an exact
   hyperbolic-distance lemma that converts "no other wall through `y`" into "no other
   wall near `y`" — which is precisely the step the incorporation review flagged as
   invalid. On the `b₀` side, `ν(b₀) = 0` is now proved by an elimination computation
   that also covers the **two rulings at infinity** (the tracked discriminant argument
   covers the affine rulings only, and its "irreducible nodal cubic" step does not follow
   from simplicity of a discriminant root).

---

## 1. The two members

Notation (as in `prop:one-node-family`, `…the-heegner-line…md:544`). `Y = P¹_x × P¹_y`,
`τ(x,y) = (−x,−y)`, `p = (0,0)`. The `τ`-invariant system of `O_Y(4,4)` is spanned by the
13 monomials `x^i y^j` with `0 ≤ i,j ≤ 4`, `i+j` even; `f(p) = 0` cuts out the hyperplane
`a₀₀ = 0`. For such an `f` with `B = {f = 0}` smooth away from `p` and an ordinary node
at `p`:

* `X^♯ = {z² = f} ⊂ Tot(O_Y(2,2)) → Y` is a double cover branched along `B`, so
  `K_{X^♯} = π^*(K_Y + O(2,2)) = 0`;
* `X̂ → X^♯` the blow-up of the node, `π̂ : X̂ → Ŷ = Bl_p Y` of degree 2;
* `D ⊂ X̂` the exceptional `(−2)`-curve, `α = [D] = π̂^*e` (`e ⊂ Ŷ` the exceptional curve);
* `e_b := π̂^*h₁`, `f_b := π̂^*h₂` (`h_i` the ruling classes on `Ŷ`), and
  `H := π̂^*O(1,1) = e_b + f_b`, `H² = 4`, `H·α = 0`;
* `ι_dP = (x,y,−z)`, `ι_Co = (−x,−y,−z)` are commuting nonsymplectic involutions with
  symplectic product, fixing `H`, and fixing `α` (as a class).

The two members (the first is m5's `b₀`, the second m5's bitangent `b★`/m6's member B):

```
f₀ = 5x⁴y⁴ − 2x⁴y² + 3x⁴ + x³y³ − 4x³y + 2x²y⁴ + x²y² + 2x² − 3xy³ + 7xy − y⁴ − 5y²
f★ = 8x⁴y⁴ + 7x⁴y² + 6x⁴ + 5x³y³ + 4x³y + 3x²y⁴ + 2x²y² + 3x² − 13xy³ − 28xy − 10y⁴ + 13y²
```

**Proposition 1.1 (verified).** For `f = f₀` and `f = f★`:
1. `f` is `τ`-invariant (12 nonzero monomials, all with `i+j` even, `0 ≤ i,j ≤ 4`);
2. `f(p) = 0`, and the quadratic part is nondegenerate — `2x² + 7xy − 5y²`
   (disc `89`) resp. `3x² − 28xy + 13y²` (disc `628`); so `p` is an ordinary node;
3. `B` is smooth away from `p`: the Gröbner basis of `(F, ∂F)` is `⟨1⟩` in the charts
   `X₁=1,Y₀=1`, `X₀=1,Y₁=1`, `X₀=1,Y₀=1`, and `⟨X₀,Y₀⟩` in the chart `X₁=Y₁=1`.

Proof. One computation, `verify_members.py` §(1); exact rational arithmetic.

So both are members of the locus `B` of `prop:one-node-family` with `k = 1`, and by
`prop:tuple-of-the-construction` (`…the-heegner-line…md:524`) the tuples attached to them
satisfy all five authored bullets: `H² = 4` fixed by both involutions; `α² = −2`,
`H·α = 0`, `α` fixed by `ι_Co`; `H` nef and big and `α` the class of an effective curve;
both involutions nonsymplectic with symplectic product. (Bullet 4 is the subject of §7:
the chamber exists and `H` lies in its closure, on the wall `α^⊥`.)

---

## 2. Lemma 2 (signs of `(−2)`-classes; period-free)

Let `X` be a smooth projective K3, `H` a nef class. If `δ ∈ Pic(X)` with `δ² = −2`, then
`δ` or `−δ` is effective; and if `H·δ > 0` then `δ` is effective.

*Proof.* `χ(O(δ)) = 2 + δ²/2 = 1`, and Serre duality gives `h²(δ) = h⁰(−δ)`, so
`h⁰(δ) + h⁰(−δ) ≥ h⁰(δ) − h¹(δ) + h⁰(−δ) = 1`. If `−δ` is effective and `H` is nef then
`H·(−δ) ≥ 0`, i.e. `H·δ ≤ 0`. ∎

**Corollary 2.1.** For a member `b`, `{δ ∈ Pic(X̂_b) : δ² = −2, H_b·δ = 1} ⊆ Δ_b`, the
set of effective roots; and `H_b·δ ≥ 0` for every `δ ∈ Δ_b` (`H_b` nef). Hence

```
ν(b) := #{δ ∈ Pic(X̂_b) : δ² = −2, H_b·δ = 1} = #{δ ∈ Δ_b : H_b·δ = 1}.
```

---

## 3. Lemma 3 (a root of `H`-degree 1 forces a reducible ruling fibre)

Let `b` be a member, `C ∈ Pic(X̂_b)` effective with `C² = −2`, `H_b·C = 1`. Then
`k := C·e_b` and `m := C·f_b` are `≥ 0` (`e_b, f_b` are pullbacks of the nef ruling
classes `h₁, h₂`, hence nef) and `k + m = C·H_b = 1`, so `(k,m) ∈ {(1,0),(0,1)}`.

*Case `(k,m) = (0,1)`.* Every irreducible component `D` of `C` has `D·e_b = 0`, so `D` is
contracted by the `e_b`-fibration and lies in a fibre `F`. No component is a whole fibre:
if `F ≤ C` then `H_b·(C−F) = 1 − H_b·e_b = 1 − 2 < 0` contradicts nefness of `H_b`. So
`F` is reducible, and `D·f_b = 1` for exactly one component. The node's `e_b`-fibre is
`D_b + (L₁ − D_b)` with `L₁ = π̂^*h₁`, whose components have `f_b`-degrees `0` and `2`;
so `F` is a reducible fibre over a ruling **other than** the node's.
*Case `(k,m) = (1,0)`.* Symmetrically with `f_b` and the node's `f_b`-fibre
`D_b + (L₂ − D_b)`, whose components have `e_b`-degrees `0` and `2`. ∎

(Finite inputs: `H_b·e_b = H_b·f_b = 2`, `e_b·D_b = f_b·D_b = 0`,
`f_b·(L₁ − D_b) = e_b·(L₂ − D_b) = 2`; all read off `π̂_*D_b = 0`, `h_i·h_j = δ_ij`.)

---

## 4. Proposition 4: `ν(b₀) = 0`

**Criterion 4.1.** Let `c ∈ P¹ ∖ {0}` (so the ruling `{x = c}` misses `p` and the
resolution does not touch the fibre over it). The `e_b`-fibre over `c` is reducible **iff**
`f(c,·)`, as a section of `O_{P¹_y}(4)`, is the square of a section of `O_{P¹_y}(2)`.

*Proof.* The fibre is the double cover `z² = f(c,y)` of `{x = c} ≅ P¹` branched along
`div f(c,·)` (degree 4; `f(c,·) ≢ 0` for our members, see below). A degree-2 cover
`s : Σ → P¹` splits iff `s = id ⊔ id`, iff the branch divisor is `2D`, iff
`f(c,·) = ℓ²` — with a scalar absorbed into `ℓ` after passing to `C̄`. ∎

**Proposition 4.2 (computed).** `b₀` has **no** reducible ruling fibre away from the two
rulings through the node (`x = 0`, `y = 0`).

*Proof.* (i) `x`-family, affine rulings. Solving
`f₀(x,·) = (s₂y² + s₁y + s₀)²` identically in `y` and eliminating `(s₂,s₁,s₀)` gives the
elimination ideal `⟨1⟩` in `Q[x]`: no `x` in the algebraic closure makes the fibre a
square. (Degenerate cases `s₂ = 0` — a square of a linear section — are solutions of the
same system and are excluded too; a ruling contained in `B` would give the trivial
solution and is excluded as well.) (ii) `x`-family, `x = ∞`. In the chart `u = 1/x` the
equation is `ζ² = h(u,y)` with `h(u,y) = u⁴f₀(1/u,y)`, so the fibre over `∞` is
`ζ² = h(0,y) = 5y⁴ − 2y² + 3`, whose `y`-discriminant is `752640 ≠ 0`: smooth, hence
irreducible. (iii) `y`-family: the same elimination gives `⟨1⟩` in `Q[y]`, and the fibre
over `y = ∞` is `ζ² = 5x⁴ + 2x² − 1` with `x`-discriminant `−46080 ≠ 0`. The
elimination is cross-checked independently at 60 digits in `crosscheck_squares.py`: at
all 22 singular rulings the square-residual of `f₀` is `≥ 0.748`, while the same test at
the bitangent split of `f★` returns residual `0` at `x = ±1`. (iv) The node's
own rulings: `f₀(0,y) = −y²(y²+5)` and `f₀(x,0) = x²(3x²+2)`, each of degree 4 with a
double root, and their resolved components have degrees `(0,2)` and `(2,0)` as in §3, so
no effective root of `H`-degree 1 sits over them. ∎

**Corollary 4.3.** `ν(b₀) = 0`.

*Proof.* Lemma 3 + Proposition 4.2. ∎

(For orientation, `ν(b★) ≥ 4`: `f★(1,y) = (y−1)²(y−3)²` gives two components `C₊, C₋`
over `x = 1`, each a `P¹` with `C_±² = −2`, `H★·C_± = 1`, `C₊·C₋ = 2`
(`C₊ + C₋ = π̂^*{x=1}`, whose square is `0`), and `ι_Co` gives another pair over `x = −1`:
`f★(−1,y) = (y+1)²(y+3)²`. Only `≥ 2` is used below.)

---

## 5. Lemma 5 (exact distance to a wall) and Proposition 6 (the facet of `𝔠★`)

**Lemma 5.1.** Let `V` be a real vector space with a form `q(v) = v·v` of signature
`(1, n−1)`, `C` a component of `{q > 0}`, and give `C` the hyperbolic metric on `{q = 1}`.
For `x ∈ C` and `w` with `w² < 0`, the hyperbolic distance `d` from the ray `[x]` to the
hyperplane `w^⊥ ∩ C` satisfies

```
sinh d = |x·w| / sqrt(x² · (−w²)).
```

In particular, if `x² > 0`, `δ² = −2` and `x·δ ≥ c₀ > 0`, then
`d([x], [δ^⊥]) ≥ arcsinh(c₀ / sqrt(2x²))`.

*Proof.* The geodesic from `[x]` to the hyperplane lies in the totally geodesic plane
spanned by `x` and `w`, where the form has signature `(1,1)`; so it suffices to do the
`(1,1)` case. Normalize `x² = 1`, `w² = −1` (write `w = √(−w²)·u`, `u² = −1`) and put
`c = x·w = x·u`. Decompose `u = c x + u_⊥` with `u_⊥ ⊥ x`; then
`u_⊥² = u² − c² = −1 − c²`. The geodesic `z(t) = cosh t · x + sinh t · v` with
`v = u_⊥/sqrt(1+c²)` (so `v² = −1`) stays on `{q = 1}`, and `z(t)·u = 0` iff
`c cosh t = sinh t·sqrt(1+c²)`, i.e. `sinh t = c`. Rescaling back,
`sinh d = c/sqrt(2)` in the normalization `x² = 1, w² = −2`; in general
`sinh d = |x·w|/sqrt(x²(−w²))`. ∎

**Lemma 5.2 (`L := 2H − α` is ample on every member).** With `N := 2(h₁+h₂) − e ∈ Pic(Ŷ)`,
`L = π̂^*N`, and `N` is ample on `Ŷ`; so `L` is ample (pullback under the finite `π̂`),
`L² = 14`, `L·H = 8`, `L·α = 2`, `L·e_b = L·f_b = 4`, `L·C₊ = 2`.

*Proof.* Nakai–Moishezon on the smooth projective surface `Ŷ`. For an irreducible
`C ⊂ Ŷ`, `C ≠ e`, let `C_V` be its image in `Y`, of bidegree `(a,b)`, with multiplicity
`m` at `p`; then `C·h₁ = b`, `C·h₂ = a`, `C·e = m`, and `m ≤ a+b` (a ruling through `p`
gives `m = 1 = a+b`; otherwise `a ≥ m` and `b ≥ m` from the intersections with the two
rulings through `p`, so `m ≤ min(a,b) ≤ a+b`). Hence `N·C = 2(a+b) − m ≥ a+b > 0`, and
`N·e = 1 > 0`, `N² = 8 − 1 = 7 > 0`. So `N` is ample, `L² = 2N² = 14`,
`L·H = N·(h₁+h₂)·2 = 2·2·2 = 8`, `L·α = 2N·e = 2`, `L·e_b = L·f_b = 2N·h_i = 4`. Finally
`L·C₊ = 2(H·C₊) − α·C₊ = 2·1 − 0 = 2` (all of `C₊·e_b = 0`, `C₊·f_b = 1`, `C₊·α = 0`
since `π̂_*C₊ = {x=1}` and `{x=1}·e = 0`, `{x=1}·h₂ = 1`, `{x=1}·h₁ = 0`). ∎

**Lemma 5.3 (multiplicity bound).** For every nonzero *effective* class `δ ∈ Pic(X̂_b)`
one has `α_b·δ ≤ H_b·δ`; and `H_b·δ = 0` forces `δ = mα_b`, `m ≥ 1`.

*Proof.* `α·δ = e·π̂_*δ = mult_p(π̂_*δ)` and `H·δ = (h₁+h₂)·π̂_*δ`; both are additive over
components and the multiplicity at `p` of an effective cycle of bidegree `(a,b)` is
`≤ a+b`, by the argument of Lemma 5.2. For the second part, if `H·δ = 0` then every
component `D` has `H·D = 0`, so `π̂_*D` is a curve of degree `0` against the nef class
`O(1,1)`, whose only null curves are `e`; so `π̂_*D = 0`, `D ⊆ D_b`, `D = D_b` (`D_b` is
irreducible), and `δ = mα`. ∎

**Proposition 6.** On `X̂★`, put `y := L + C₊ + e_b = 2H★ − α★ + C₊ + e_b`. Then

```
y² = 24,   y·H★ = 11 > 0,   y·C₊ = 0,
y·δ ≥ 1 for every nonzero effective class δ ≠ C₊,   y·δ = 0 iff δ ∈ {0, C₊}.
```

Moreover `C₊^⊥` supports a **facet** of `𝔠̄★`, the closure of the chamber of the tuple at
`b★`; equivalently `C₊` is (up to sign) a facet normal with `|H★·C₊| = 1`.

*Proof.* `y² = L² + C₊² + e_b² + 2L·C₊ + 2L·e_b + 2C₊·e_b = 14 − 2 + 0 + 4 + 8 + 0 = 24`;
`y·H★ = 8 + 1 + 2 = 11`; `y·C₊ = L·C₊ + C₊² + e_b·C₊ = 2 − 2 + 0 = 0`. As `y² > 0`,
`y·H★ > 0` and `H★² = 4 > 0`, we get `y ∈ C★` (the positive cone).

Let `δ ≠ 0` be effective, and put `k := C₊·δ`. Since `C₊` is a smooth rational curve,
`k ≥ −2`, and `k = −2` forces `δ = C₊ + δ''` with `δ''` effective (a curve meeting `C₊`
negatively contains it). Cases:
1. `H·δ = 0`: then `δ = mα` (`m ≥ 1`) by Lemma 5.3, and
   `y·δ = m(L·α + C₊·α + e_b·α) = m(2 + 0 + 0) ≥ 2`.
2. `H·δ ≥ 1` and `k ≥ 0`: `y·δ = L·δ + k + e_b·δ ≥ (2H·δ − α·δ) ≥ H·δ ≥ 1` by
   Lemma 5.3 and nefness of `e_b`.
3. `k = −1`: then `y·δ ≥ (2H·δ − α·δ) − 1 + e_b·δ ≥ 1 − 1 + e_b·δ`, and `e_b·δ ≥ 1`:
   if `e_b·δ = 0` then every component of `δ` lies in a fibre of the `e_b`-ruling, and
   `k = −1 < 0` forces the component `C₊` to occur, together with further components
   meeting `C₊` positively; such a component lies in the same fibre, whose components are
   `C₊` and `C₋` with `C₊·C₊ = −2` and `C₊·C₋ = 2`, so `k = −2a + 2b` is even —
   contradiction with `k = −1`.
4. `k = −2`: `y·δ = y·δ''` (`y·C₊ = 0`, and `C₊·δ'' = 0`). If `δ'' = 0` then `δ = C₊`
   and `y·δ = 0`. If `δ'' ≠ 0`: either `e_b·δ'' ≥ 1`, whence `y·δ ≥ 1`, or
   `e_b·δ'' = 0`, whence every component of `δ''` lies in a fibre and
   `H·δ'' = f_b·δ'' ≥ 1`, so by Lemma 5.3 and nefness
   `y·δ = L·δ'' + e_b·δ'' ≥ (2 − 1)H·δ'' ≥ 1`.
So `y·δ ≥ 0` always, `y·δ ≥ 1` for `δ ∉ {0,C₊}`, and `= 0` exactly for `δ = C₊`.

Hence `y ∈ 𝔠̄★`: the chamber closure is `{x ∈ C̄★ : x·δ ≥ 0 ∀δ ∈ Δ★}` (`⊆` by continuity
along paths in the chamber; `⊇` because for `x ∈ C★` with `x·δ ≥ 0` for all roots and
`ε > 0`, the class `x + εL` has all pairings `> 0` — `L` is ample — and tends to `x`).
By Lemma 5.1 with `x² = 24`, `c₀ = 1`, the hyperbolic ball of radius
`ρ = arcsinh(1/√48) ≈ 0.1438` about `[y]` in `C★` meets **no** wall `δ^⊥`,
`δ ∈ Δ★ ∖ {C₊}`, while `C₊^⊥ ∋ y`. Intersecting that ball with the totally geodesic
hyperplane `[C₊^⊥ ∩ C★]` gives a nonempty relatively open subset of `C₊^⊥ ∩ C★` lying in
`𝔠̄★` (the sign of `x·δ` on the ball is constant for each `δ ≠ C₊`, since the ball is
connected and misses `δ^⊥`, and it is `+` at `y`). Hence `𝔠̄★ ∩ C₊^⊥` has nonempty
relative interior in `C₊^⊥`, i.e. it is a facet, and its supporting hyperplane is
`C₊^⊥`, so its primitive normal is `±C₊`. ∎

**Remark 6.1 (what makes this work, and what it replaces).** The tracked text reached the
facet in two steps: a contraction of `C₊` with an ample `A'` on the target
(`sm57_proof-m5.md`, addendum B) and then "the point `e_b` lies in `𝔠̄ ∩ C₊^⊥`, interior
points satisfy `x·C₊ > 0`, hence a facet". Neither is needed and the second is not a
proof: a point of `𝔠̄ ∩ C₊^⊥` with `x² = 0` does not show the face is a facet. What makes
it a facet is a point `y` with `y² > 0` **plus** the uniform pairing bound
`y·δ ≥ 1`, which Lemma 5.1 turns into a uniform *distance* bound. This also answers the
review's objection that "infinitely many strict half-spaces can have empty interior": here
they cannot, and the reason is quantitative, not finiteness of the arrangement.

**Remark 6.2 (reading-independence).** Proposition 6 is stated in whichever ambient space
the chamber lives — `Pic(X̂★)_R`, `H^{1,1}(X̂★,R)`, or `H²(X̂★,R) ⊃ H^{1,1}` — verbatim:
`y ∈ Pic`, the formula of Lemma 5.1 only sees the restriction of the form to
`span(y, δ)`, and `dim` never enters. This is why the refutation does not depend on
identifying the chamber with the nef cone or on any chamber-decomposition theorem.

---

## 6. Theorem 9: the chamber clause is false

Throughout, `γ ∈ O(L_K3)` is an isometry `H²(X̂₀,Z) → H²(X̂★,Z)` (a lattice isometry; not
assumed to be a Hodge isometry — `thm:a21-labels` supplies lattice isometries, and the
Gauss–Manin transport is not a Hodge isometry), with `γH₀ = H★`, `γα₀ = α★`.
`𝔠_b` denotes the chamber of the tuple at `b` in the stated ambient space, and
`γ(𝔠₀) = 𝔠★` is the fourth bullet's "preserving the chosen chamber".

**Lemma 8.** Suppose `γ(𝔠₀) = 𝔠★`. Then `ν(b₀) ≥ 1`.
*Proof.* In all three cases it suffices to show that `δ₀ := γ^{-1}(C₊)` lies in
`Pic(X̂₀)`; then `δ₀² = −2` and `H₀·δ₀ = γH₀·C₊ = H★·C₊ = 1`, and Lemma 2 makes `δ₀`
effective, so `ν(b₀) ≥ 1`. (Note `Pic(X̂₀) = (Pic(X̂₀)⊗R) ∩ L_K3`: `Pic` is
`H^{1,1} ∩ L_K3` and `H^{1,1}` is a real subspace, so `Pic` is primitive in `L_K3`.)

*(i) `𝔠_b = Nef(X̂_b)`, or `𝔠_b` a chamber of the arrangement inside
`P(X̂_b) ∩ Pic(X̂_b)_R` (ambient `Pic_R`).* Such a chamber is a nonempty open subset of
`Pic_b ⊗ R` (it contains the ample cone, which is open and nonempty since `L` is ample),
so `span 𝔠₀ = Pic₀ ⊗ R`; likewise `span 𝔠★ = Pic★ ⊗ R`. From `γ(𝔠₀) = 𝔠★`:
`γ(Pic₀ ⊗ R) = Pic★ ⊗ R`, hence `δ₀ ∈ γ^{-1}(Pic★⊗R) = Pic₀⊗R`, and `δ₀ ∈ L_K3`; by
primitivity `δ₀ ∈ Pic₀`.

*(ii) `𝔠_b` a chamber of the arrangement in `H^{1,1}(X̂_b,R)`.* It is open there, so
`γ(H^{1,1}(X̂₀,R)) = H^{1,1}(X̂★,R)`, hence
`δ₀ ∈ γ^{-1}(H^{1,1}_★) ∩ L_K3 = H^{1,1}_₀ ∩ L_K3 = Pic₀`.

*(iii) `𝔠_b` a chamber of the arrangement in `H²(X̂_b,R)` (the corpus's reading,
`…the-heegner-line…md:651`).* Here spans carry no information (`𝔠₀` is open in `H²`), so
use facets. By Proposition 6, `F★ := 𝔠̄★ ∩ C₊^⊥` is a facet of the closed convex cone
`𝔠̄★`, with supporting hyperplane `C₊^⊥`. Since `γ` is a linear bijection of the ambient
spaces with `γ(𝔠₀) = 𝔠★`, `F₀ := γ^{-1}(F★) = 𝔠̄₀ ∩ (γ^{-1}C₊)^⊥` is a facet of `𝔠̄₀`
with supporting hyperplane `(γ^{-1}C₊)^⊥`, and `x := γ^{-1}(y)` lies in `F₀` with
`x² = y² = 24 > 0`, so `x ∈ C₀`; by Proposition 6 transported (same ball, same bound),
`x ∈ relint F₀`. Now `F₀ ⊆ ∂𝔠̄₀` and `x ∈ C₀`, so `x ∈ ⋃_{δ∈Δ₀} δ^⊥`; pick `δ`
with `x·δ = 0`. Since `𝔠̄₀ ⊆ {z·δ ≥ 0}`, the face `𝔠̄₀ ∩ δ^⊥` contains `x`, hence
contains the face through `x`, i.e. `F₀ ⊆ 𝔠̄₀ ∩ δ^⊥ ⊆ δ^⊥`. As `F₀` is a facet,
`(γ^{-1}C₊)^⊥ = aff F₀ = δ^⊥`; two classes with the same orthogonal hyperplane are
proportional, and equal squares (`−2`) force `γ^{-1}C₊ = ±δ`. If `γ^{-1}C₊ = −δ` then
`H₀·γ^{-1}C₊ = −H₀·δ ≤ 0` (`H₀` nef, `δ` effective), contradicting
`H₀·γ^{-1}C₊ = 1`. Hence `γ^{-1}C₊ = δ ∈ Pic₀`. ∎

**Theorem 9.** There is **no** `γ ∈ O(L_K3)` with `γH₀ = H★`, `γα₀ = α★` and
`γ(𝔠₀) = 𝔠★` — in any of the three settings (i), (ii), (iii) of Lemma 8.
Hence the labeled Coble rigidity claim of the authored statement (any two tuples
conjugate by an element of `O(L_K3)` preserving labels, degree-4 class, effective root
**and the chosen chamber**) is **false** for the pair `(b₀, b★)`.

*Proof.* Lemma 8 gives `ν(b₀) ≥ 1`; Corollary 4.3 gives `ν(b₀) = 0`. ∎

**Corollary 9.1.** `prob:effective-cone-agreement` (`…the-heegner-line…md:589`) fails for
the pair `(b₀,b★)`: in the form the corpus gives it (the connecting isometry `γ` of
`thm:a21-labels` transports the chamber, equivalently no extra effective root of `b★`
cuts `γ𝔠_{b₀}`), it is exactly `γ(𝔠₀) = 𝔠★`, which Theorem 9 refutes. So for **every**
isometry with `γH₀ = H★`, `γα₀ = α★` the transported chamber is not the chamber of
`b★` — the two members' effective cones do *not* agree under `γ`.

**Remark 9.2 (why `ν` is *not* transported along the family — a trap).** The tracked
argument (`sm57_proof-m5.md`, Corollary 5.2) states the invariance of `ν` only under
isometries with `γ(Pic) = Pic(·)`, and that proviso cannot be dropped. By
`thm:a21-labels:578` there **is** a lattice isometry `γ` with `γH₀ = H★`, `γα₀ = α★`;
by Theorem 9 it does not transport the chamber; and by Corollary 4.3 together with
`ν(b★) ≥ 2` it does not carry `Pic₀` onto `Pic★` either (otherwise
`{δ : δ²=−2, H·δ=1}` would be carried bijectively, giving `0 = ν(b₀) = ν(b★) ≥ 2`).
So the parallel transport of the family is an isometry of *lattices* that preserves
neither the chamber nor the Picard lattice: the Gauss–Manin connection does not preserve
`H^{2,0}`, and a lattice class orthogonal to the period at `b★` need not be algebraic at
`b₀`. Any argument that transports `ν` along the one-node family is invalid; the argument
above uses `ν`-invariance only under the *extra* hypothesis `γ(𝔠₀) = 𝔠★`, which is
exactly the hypothesis being refuted.

---

## 7. The fourth bullet's quantifier: the readings, and which one the corpus adopts

The authored bullet (`writing/coble/heegner-report/coble-heegner-research-report.md`,
rev `a145cea4a5`, lines 601–638) reads: "`𝔠` the chosen positive/nef chamber in which
`α` is effective and `H` is nef and big".

**Fact 7.1 (`H` is always on a wall).** On every member, `α` is an effective `(−2)`-class
and `H·α = 0` (`prop:tuple-of-the-construction:524`). Hence `H ∈ α^⊥`, while every chamber
`𝔠` of the effective-root arrangement lies in the open half-space `α > 0` (the chamber of
the tuple contains the Kähler cone, and a Kähler class is positive on the effective curve
`D`). So `H ∉ 𝔠` — always, for every member. Moreover `H` is not merely on the
boundary: `H² = 4 > 0`, and by `lem:face-at-H` (`…the-heegner-line…md:621`, parts 1–4)
the only wall through `H` is `α^⊥` and `H` lies in the *relative interior* of the face
`{v ∈ Nef : v·α = 0}`. Therefore "chamber in which `H` is nef and big" can only be the
reading

> `𝔠` is a chamber whose **closure** contains `H`, and "`H` nef and big" is a property of
> `H` itself (equivalently: of the member), not of `𝔠`.

This is a semantics statement, not a defect: it is exactly how `lem:face-at-H` states it.

**The readings.** `P_b` is a component of `{x² > 0}`; the walls of a member are
`δ^⊥`, `δ ∈ Δ_b` (its own effective roots — this is what makes the arrangement
member-dependent: `rmk:chamber-not-transported:651`):

| | ambient space of `𝔠_b` | survives the authored text? | `γ(𝔠₀)=𝔠★` forces | refuted? |
|---|---|---|---|---|
| R1 | a lattice built only from the labels (`N = ⟨e,f,α⟩`), not the member | yes; but the clause then says nothing about the member | nothing (the chamber is a function of `H,α`) | not addressed here (m6 §4.6; kept as the named alternative) |
| R2 | `Nef(X̂_b) ⊂ Pic_R` ("the positive/nef chamber" literally) | yes, literally (`H ∈ Nef`) | `γ(Pic₀) = Pic★` | **yes**, Lemma 8(i) |
| R3 | chamber of the arrangement in `P_b ∩ Pic_b ⊗ R` | yes, with `H ∈ 𝔠̄` | `γ(Pic₀) = Pic★` | **yes**, Lemma 8(i) |
| R4 | chamber of the arrangement in `P_b ∩ H^{1,1}(X̂_b,R)` | yes, with `H ∈ 𝔠̄` | `γ(H^{1,1}₀) = H^{1,1}★` | **yes**, Lemma 8(ii) |
| R5 | chamber of the arrangement in `P_b ∩ H²(X̂_b,R)` — **the corpus's own reading** | yes, with `H ∈ 𝔠̄` | facet normal of `𝔠̄₀` of `|H·|`-degree 1 | **yes**, Lemma 8(iii) |
| — | all `(−2)`-classes of `L_K3` (transcendental ones too) | **no**: those hyperplanes are not walls of any cone of curves, and "`α` effective" has no meaning in it | — | not a reading |
| — | the Kähler (ample) cone | **no**: `H` is not ample (`H·α = 0`) | — | not a reading |

Which one the corpus adopts: **R5**, by `rmk:chamber-not-transported` (`:651`):
"let `C_X ⊂ H²(X,R)` be a component of `{x² > 0}` … The fourth bullet's `𝔠` is this
chamber, the one containing the Kähler cone." So the corpus's own semantics is refuted by
Lemma 8(iii). Readings R2 and R3 are the "nef cone itself" reading named in the task;
R4 is the `H^{1,1}` version; all three are also refuted.

**Remark 7.2 (one correction to the displayed formula at `:651`).** That remark writes
`K_X = {x ∈ C_X : x·δ > 0 for every δ ∈ Δ_X}` with `C_X ⊂ H²(X,R)`. As written this is
not the Kähler cone: it is invariant under adding any `z ⊥ Pic(X)`, and such `z` exist
(`Pic^⊥ ⊂ H²` has rank `22 − ρ ≥ 2`). The correct statement has the ambient restricted:
`K_X = {x ∈ C_X ∩ H^{1,1}(X,R) : x·δ > 0 ∀δ ∈ Δ_X}`, equivalently `𝔠 ∩ H^{1,1} = K_X`
for the chamber `𝔠 ⊂ H²`. (The identification of that set with the ample cone is the
standard K3 chamber theorem; it is the one standard input I do **not** use — none of
Lemma 8's three cases needs the chamber to be the ample cone, only that it is an open
cone of the indicated ambient space cut by the member's effective roots. This correction
is a defect-1 item; I record it here only because it fixes the meaning of R5.)

---

## 8. Not claimed, and the exact open points

1. **`ν(b★)` is not computed exactly** (I only need `≥ 2`; in fact `≥ 4`, from
   `x = ±1`). No claim is made about which divisors carry `ν > 0`, nor about `ν` on the
   whole locus.
2. **R1 is not addressed.** Under the label-own reading the clause is vacuous about the
   member and A21 holds (m6's §4.6 in `sm57_chamber-obstruction-m6.md`); I did not
   re-verify that reading and do not use it.
3. **Members with `k ≥ 2`, or nodes off the `τ`-fixed points, are not treated.** The
   members here are exactly the `k = 1`, node-at-`p` ones of `prop:one-node-family`.
4. **No contraction and no Grauert/Artin input is asserted anywhere** (Proposition 6
   needs none), so this document takes no position on the projectivity of the
   contraction of a `(−2)`-curve (defect 2, direction d3).
5. The *positive* half (the labels are conjugate; `ρ ≥ 11`; period map rank 9; `Pic =
   S_Co` for a very general member) is not re-proved here; I use only
   `thm:a21-labels`'s existence statement as the *contrast*, and Theorem 9 does not
   depend on it (it is a statement about a fixed `γ`).

---

## 9. Hypothesis ledger

| premise | status |
|---|---|
| `π̂ : X̂_b → Ŷ = Bl_p Y` is finite of degree 2, `α = π̂^*e`, `H = π̂^*(h₁+h₂)`, `H² = 4`, `H·α = 0` | `prop:one-node-family:544`, `prop:tuple-of-the-construction:524`; the members' membership and smoothness are **Proposition 1.1** (computed) |
| five authored bullets hold for both tuples | `prop:tuple-of-the-construction:524` with `k = 1` |
| `δ² = −2 ⟹ ±δ` effective; `H` nef `⟹` `H·δ > 0` forces `δ` effective | **Lemma 2**, proved (Riemann–Roch + Serre duality + nefness) |
| a root of `H`-degree 1 forces a reducible ruling fibre away from the node's rulings | **Lemma 3**, proved |
| `b₀` has no reducible ruling fibre away from the node's rulings | **Proposition 4.2**, computed (`verify_members.py` §(2)): two eliminations `⟨1⟩`, two infinity discriminants `752640`, `−46080`, two node rulings |
| `ν(b₀) = 0` | **Corollary 4.3** |
| `ν(b★) ≥ 2` (in fact `≥ 4`) | `f★(±1,y)` are squares of quadratics; `C_±² = −2`, `C_±·H = 1`, `C₊·C₋ = 2` from `(C₊+C₋)² = (π̂^*{x=1})² = 0` — computed, `verify_members.py` §(3) |
| `L = 2H − α` is ample on every member, `L² = 14`, `L·H = 8`, `L·α = 2`, `L·e_b = L·f_b = 4`, `L·C₊ = 2` | **Lemma 5.2**, proved (Nakai–Moishezon on `Ŷ`) |
| `α·δ ≤ H·δ` for effective `δ`, and `H·δ = 0 ⟹ δ = mα` | **Lemma 5.3**, proved |
| `sinh d([x],[δ^⊥]) = |x·δ|/sqrt(2x²)` | **Lemma 5.1**, proved |
| `C₊^⊥` supports a facet of `𝔠̄★`, normal `±C₊`, `|H★·C₊| = 1` | **Proposition 6**, proved (Lemmas 5.1, 5.2, 5.3); `y² = 24`, `sinh ρ = 1/√48` |
| every facet of `𝔠̄₀` with a relative interior point in `C₀` has hyperplane `δ^⊥`, `δ ∈ ±Δ₀` | elementary convexity, proved inside Lemma 8(iii) |
| a lattice isometry `γ` with `γH₀ = H★`, `γα₀ = α★` exists | `thm:a21-labels:578` — used only as the contrast, not needed by Theorem 9 |
| **not used** | integral eigensplittings; the contractibility/projectivity of the contraction of `(−2)`-curves; the period map's rank; existence of a member with `Pic = S_Co`; the chamber-decomposition theorem identifying the chamber with the ample cone; the connectedness of the one-node locus |

---

## 10. Corrections to the tracked evidence

1. `sm57_proof-m5.md` §6, "the other 22 singular fibres are irreducible nodal cubics":
   what is computed there is `disc = x²·q(x)` with `q` squarefree of degree 22, i.e. the
   *singular* fibres are at `x = 0` and at 22 simple roots. Passing from that to
   *irreducibility* needs one further argument — a square fibre `f(c,·) = ℓ²` has
   `x = c` as a root of `disc` of order `≥ 2` (each of the two double roots of `ℓ²` splits
   into a pair of roots whose difference is `~√(x−c)`, contributing order 1 each), so a
   simple root cannot support one. That argument is missing there, and I replace it by
   the direct elimination test (Proposition 4.2), which needs no such lemma.
   Conclusion `ν(b₀) = 0` survives — for a correct reason.
2. Both documents' half of the fibre audit stops at the affine rulings `x = c`,
   `y = c`; the rulings of `P¹` also include `x = ∞`, `y = ∞`, and the claim
   `ν(b₀) = 0` needs them. They are computed here (`disc = 752640`, `−46080`).
   (Cross-reference: this is the infinity half of the node/infinity audit, direction d2.)
3. `sm57_proof-m5.md` addendum B: the contraction-plus-ample-`A'` route is not needed
   (Proposition 6), and its conclusion "interior points satisfy `x·C₊ > 0`, hence a
   facet" is not a proof; Lemma 5.1 + the explicit `y` is the replacement.
4. `sm57_proof-m5.md` Corollary 5.2 must keep its `γ(Pic) = Pic(·)` proviso for the
   reason in Remark 9.2.
5. `rmk:chamber-not-transported:651`: the displayed Kähler-cone formula needs the
   `H^{1,1}` ambient (Remark 7.2).
