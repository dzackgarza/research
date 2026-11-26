---
unit: research-program
status: conjectural
tags:
  - halphen
  - rational-elliptic
  - git
  - ksba
notes: |-
  Provenance: the research statement, section "Future Work / Halphen and rational elliptic surfaces".
  Absent from the dissertation. The geometric Coble-Halphen correspondence is already recorded in the Halphen-surfaces note; this note records the moduli-theoretic program built on it.
---

# Moduli of index 2 Halphen and rational elliptic surfaces {#sec-halphen-index-2-moduli-program}


## Definitions and known moduli

::: {#def:halphen-surface-index .definition title="Index, Halphen pencil, Halphen surface" defines="rational elliptic surface; rational genus-one surface; Halphen index; Halphen pencil of index $m$; Halphen surface of index $m$"}

A **rational genus-one surface** is a smooth projective rational surface $Y$ with a relatively minimal fibration (@def:relatively-minimal-fibration) $\pi: Y\to\PP^1$ whose generic fiber (@def:fiber-cofiber) is a smooth geometrically integral curve of genus one. The term *rational elliptic surface* is also used here without requiring a section; a section makes the fibration Jacobian.
Its **index (@def:index) (@def:halphen-surface-index)** is the minimal $m$ with $\pi$ given by $|-mK_Y|$.
A **Halphen pencil of index $m$** is a pencil of degree (@def:graded-object) $3m$ curves in $\PP^2$ with 9 basepoints (@def:based-loop); minimally resolving its basepoints gives a **Halphen surface of index $m$**. Equivalently, $Y$ is Halphen of index $m$ when $|-mK_Y|$ has dimension 1, no fixed part, and is basepoint free.
Every relatively minimal rational elliptic surface is Halphen of some index.
:::

::: {.proposition #prop:known-halphen-moduli title="Moduli of rational elliptic surfaces of index $1$ and $2$"}

1. Marked rational elliptic surfaces (@def:halphen-surface-index) of index (@def:index) (@def:halphen-surface-index) $1$ depend on $8$ parameters and are parametrized by an open subset of the Grassmannian $\Gr(2,10)$ of pencils of plane cubics.
   Marked rational elliptic surfaces of index at least $2$ depend on $9$ parameters; the additional parameter is the choice of the multiple fiber (@def:fiber-cofiber) [@MZ21, §1].

2. A rational Weierstrass fibration $X\to\PP^1$ is defined by a pair of forms $(A,B)$, up to the action of $k^*\times\SL(V_1)$.
   The point of the GIT quotient of [@Mir81, §4] represented by $(A,B)$ is stable if and only if $X$ has a smooth generic fibre and the associated elliptic surface has only reduced fibres [@Mir81, Thm. 6.2].
   The stable locus $W_1$ is a coarse moduli space for stable rational Weierstrass fibrations, and the GIT quotient of [@Mir81, §4] is a compactification $\overline W_1$ of it [@Mir81, Thm. 7.2 and §7].

3. A moduli space for marked rational elliptic surfaces of index $2$ exists as a noncomplete toric variety of dimension $9$, the quotient of an affine toric variety by an action of $\mathbb G_m$.
   It has compactifications that are complete toric varieties, the quotients of $\mathbb A^{12}$ by actions of $\mathbb G_m^3$ [@MZ21, Thm. 1.1].

4. Let $V = H^0(\PP^2,\mathcal O_{\PP^2}(1))$.
   A Halphen pencil of index $2$ is a point of $\Gr(2, S^6V^*)$, and [@Zan23, Thms. 1.4--1.6] give the criteria for its stability and semistability under $\SL(V)$ by the types of the singular fibers of its rational elliptic surface.
:::

## The lattice matching

::: {.proposition #prop:halphen-k3-lattices title="The $2$-elementary lattices of Halphen K3 surfaces"}

Let $X$ be a K3 surface with a nonsymplectic involution $\iota$ and $2$-elementary Picard lattice $S$, and let $Y \definedas X/\iota$.

1. If $S = \HalphenInvariants$, then $Y$ is an index (@def:index) (@def:halphen-surface-index) $2$ Halphen pencil, and the fixed locus $X^\iota$ is a smooth elliptic fiber (@def:fiber-cofiber) that does not ramify over the unique multiple fiber of $Y$ [@AE22, Thm. 4.1(3)].

2. If $S = (10+k,\, 12-k,\, \delta)$ with $1\leq k\leq 9$, then $X$ is an index $2$ Halphen K3 surface with an $I_{2k}$ fiber, and contracting the $(-1)$-curves in the special fiber of $Y$ gives a rational index $2$ Halphen pencil with an $I_k$ fiber [@AE22, §4C].
:::

The lattices of @prop:halphen-k3-lattices(2) are the rows with $n = 1, \dots, 9$ of [the Coble lattice table](#sec-coble-lattice-table), both rows with $n = 8$ included.
The remaining row is $n = 10$, the lattice $(20,2,1)$.

## The program

::: {#conj:halphen-index-2-period-domains .conjecture title="Period domains and KSBA compactifications for $M_{H,2,k}$"}

These lattices can be used to construct period domains of index (@def:index) (@def:halphen-surface-index) 2 Halphen pencils, yielding moduli spaces $M_{H,2,k}$ of index 2 Halphen surfaces with an $I_k$ fiber (@def:fiber-cofiber), whose K3 covers have an $I_{2k}$ fiber, with the matching arising from a geometric comparison to Coble surfaces (@def:coble-surface).
The normalizations of the stable pair compactifications $\overline{M_{H,2,k}}^R$ are then isomorphic to semitoroidal compactifications (@def:semitoroidal-compactification) of the corresponding period domains, for a suitably canonical divisor $R$.
:::

::: {#qst:halphen-multiple-fiber-divisor .question title="A divisor constructed from the multiple fiber"}

A Halphen surface of index $m\geq 2$ has a unique multiple fiber of multiplicity $m$.
Can that fiber, together with a suitable canonical horizontal divisor,
be used to construct a recognizable polarizing divisor $R$?
:::

Write $F$ for the fiber class of the Halphen fibration, so that
$F=-mK_Y$ and $F^2=0$. Every divisor supported on fibers has degree
zero on the generic fiber. Hence $K_Y+\epsilon R$ has degree zero
there when $R$ is vertical, and cannot be big: a big divisor has a
multiple whose complete linear system defines a birational rational
map, which cannot be constant on the generic fiber. A line bundle of
nonpositive degree on a smooth projective integral curve has at most
one independent global section. This obstruction is stronger than
the failure of the multiple fiber itself to be big.

::: {.proposition #prop:halphen-translation-polarization-obstruction title="Mordell--Weil translation obstruction to an unmarked polarization"}

Let $Y$ be a complex Halphen surface of index $m$, with relatively
minimal genus-one fibration $f:Y\to\PP^1$ and fiber class $F$.
Set $K=\mathbb C(\PP^1)$, $C=Y_\eta$ and
$J=\operatorname{Pic}^0_{C/K}$. If $J(K)$ has positive rank, then:

1. Every effective divisor with finite orbit under
   $\operatorname{Aut}_{\PP^1}(Y)$ is vertical.
2. Every integral divisor class of finite orbit under this group
   has intersection zero with $F$. No big rational divisor class
   has finite orbit.
3. The same statements hold after marking any finite collection of
   fibers, including the multiple fiber, and their components.
   They also hold for a functorial polarization on a finite
   representable marking cover of the unmarked moduli stack.
:::

::: {.proof}
The Mordell--Weil group $J(K)$ acts on its genus-one torsor $C$ by
translations. Relative minimality extends each translation uniquely
to an automorphism over the base (Dolgachev--Martin,
[*Automorphism groups of rational elliptic and quasi-elliptic surfaces in all characteristics*](https://doi.org/10.1016/j.aim.2022.108274),
Adv. Math. 400 (2022), 108274, §1.1, p. 2).
Choose a nontorsion point $a\in J(K)$. Over an algebraic closure of
$K$, choose an origin on $C$ to identify it with $J$.

If an effective divisor $R$ has finite orbit, some power $t_{na}$
($n>0$) of translation fixes $R$. A horizontal component of $R$
would give a nonempty finite support on the geometric generic
fiber. The induced permutation of this support would have finite
order, giving a fixed point of a translation by a nonzero multiple
of $a$. A translation has a fixed point only when its translating
point is zero, a contradiction.

If a line bundle $\mathcal O_Y(D)$ has finite orbit, choose $n>0$
with $t_{na}^*\mathcal O_Y(D)\simeq\mathcal O_Y(D)$. Represent its
restriction to the geometric generic fiber by $\sum_i d_i[P_i]$.
Its degree is $d=\sum_i d_i=D\cdot F$. Pullback replaces $P_i$ by
$P_i-na$, so the difference of the two divisor classes corresponds
to $-dna$ in the degree-zero Picard group, by the degree-and-sum
criterion [@Sil09, III, Cor. 3.5, p. 63]. Thus $dna=0$, forcing
$d=0$. On the rational surface, numerical equivalence of integral
divisor classes is equality in the Picard group: the total-transform
basis for the blowup of the nine basepoints has intersection form
$\operatorname{diag}(1,-1^9)$. Clearing denominators proves the
rational-class assertion. A big class has positive degree on the
generic fiber by the birational-map argument above.

All translations fix the base pointwise. The induced permutation of
the finite sets of marked fiber components has finite order, so a
positive power of $t_a$ preserves all the markings and is still
nontorsion. For a finite representable cover of the stack, the
automorphisms of an object act on the finite set of geometric
points of the fiber of the cover. The image of the stabilizer of a
lift is the stabilizer of its fiber point and has finite index.
It therefore contains a positive power of $t_a$. Functorial divisor
classes are fixed by that stabilizer, so the same degree argument
applies.
:::

The locus on which this obstruction applies is determined by the
fiber configuration. Write $b_v$ for the number of distinct
irreducible components of the fiber at $v$. Dolgachev--Martin,
[loc. cit.](https://doi.org/10.1016/j.aim.2022.108274), Lem. 5.1,
p. 20, identify $J(K)$ with $E_8/T$, where $T$ is generated by the
fiber components modulo the reduced fiber class in
$(-K_Y)^\perp/\mathbb Z(-K_Y)$. Each reducible fiber contributes a
root lattice of rank $b_v-1$ (the intersection form has precisely
the fiber relation); distinct fibers are orthogonal in this
negative definite quotient. Thus
\[
\operatorname{rk} J(K)=8-\sum_v(b_v-1).
\]
Their §2.2, p. 9, identifies the zero-rank case with extremality.
If one fiber has type $I_k$ and all other fibers have irreducible
support, the rank is $9-k$, so the obstruction applies for
$1\leq k\leq8$. Additional reducible fibers must be included in
the sum. For $k=9$ in this configuration the rank is zero, and
this argument does not decide existence of a canonical polarization.
General unnodal Halphen surfaces of index two have no reducible
fibers and rank eight; see [@CD12, Prop. 2.5, Rem. 2.9 and
Thm. 2.10] (published pp. 871--873).

::: {.corollary #cor:halphen-double-base-change-polarization-obstruction title="The obstruction on the double-base-change K3 cover"}

Suppose $X$ is the smooth relatively minimal K3 model of a connected
double base change of a Halphen fibration as in
@prop:halphen-translation-polarization-obstruction. No big class on
$X$ has finite orbit under automorphisms preserving the fibration
and commuting with the deck involution.
:::

::: {.proof}
Over the quadratic function-field extension, $a$ remains
nontorsion, and the translation by its base change extends to
the relatively minimal regular model. Uniqueness of the minimal
regular model for a smooth curve of genus one gives this
extension (Liu, *Algebraic Geometry and Arithmetic Curves*,
Thm. 9.3.21 and Cor. 9.3.24). On the generic fiber the translation
commutes with the deck action because it is defined over $K$;
hence their extensions commute. The degree-and-sum argument of
@prop:halphen-translation-polarization-obstruction applies to
the base-changed generic fiber. Numerical and linear equivalence
agree for integral line bundles on a K3 surface: if a numerically
trivial line bundle is not trivial, neither it nor its inverse
can have a nonzero section (an effective nonzero divisor has
positive intersection with an ample divisor), whereas
Riemann--Roch and Serre duality give
$h^0(L)+h^0(L^{-1})\geq\chi(L)=2$.
Thus the finite-orbit claim holds for numerical classes as well.
A big class has positive generic-fiber degree.
:::

Consequently the proposed canonical divisor in
@qst:halphen-multiple-fiber-divisor does not exist on the
nonextremal locus if it is required to be functorial for the
unmarked surface (or for the indicated finite marking covers).
For any invariant effective boundary $R$, the class
$K_Y+\epsilon R$ has zero fiber degree, so this fails already on
the smooth locus, before constructing a stable degeneration.
The same conclusion on the K3 side concerns the actual
double-base-change construction, not an identification of every
period stratum with that moduli functor.

This does not rule out KSBA compactifications of a moduli problem
with a chosen plane model or horizontal multisection, or a
coarse-space construction which does not descend a functorial
polarization to the unmarked stack. To realize
@conj:halphen-index-2-period-domains in that way one must specify
the additional structure, prove the associated recognizable-divisor
statement, and compare the resulting moduli problem with the
unmarked period domain. The extremal locus requires a separate
analysis; finiteness of the translation group alone is not a
polarization theorem.

## The program for $S = \HalphenInvariants$

Let $S \definedas \HalphenInvariants$ and let
$T=S^{\perp\lkt}$ for a chosen primitive embedding.

1. Construct the period domain $F_S$.

2. Construct $\overline{F_S}^{\bb}$.

3. Specify the arithmetic group $\Gamma\leq\Orth(T)$ for the chosen
   moduli problem, and study its orbits of primitive isotropic lines and
   planes in $T$.

4. Determine the cusp diagram of $\partial\overline{F_S}^{\bb}$ lattice-theoretically.

5. Compute $e_i^{\perp T}/\generators{e_i}$ and the Coxeter diagrams at the corresponding 0-cusps.

6. Find a recognizable divisor $R$ and construct $\overline{F_S}^R$.

7. Use [@AE22] to construct dlt models and integral-affine structures classifying $\partial\overline{F_S}^R$.

Related: [Coble families research program](#sec-coble-families-research-program), [nodal Enriques moduli program](#sec-nodal-enriques-moduli-program), [computational toolchain and recipe](#sec-computational-toolchain-and-recipe).
