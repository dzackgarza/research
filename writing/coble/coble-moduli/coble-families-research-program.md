---
unit: research-program
status: partial
tags:
- coble
- moduli
- ksba
- recognizable-divisor
notes: |-
  Provenance: `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/research-statements/canonical/my_research_statement/ResearchStatement.md`, section "Future Work / Coble surfaces with $1\leq n\leq 10$ boundary components".
  Not in the dissertation.
  The table of the lattices $M = (10+n,\, 12-n,\, \delta)$ and their orthogonal complements $N = M^\perp$ is **already recorded** in [[coble-lattice-table|the Coble lattice table]], sourced from Cossec-Dolgachev-Liedtke, *Enriques Surfaces I*, Table 5.1, p. 553. This note records only the research program built on it, which is not recorded elsewhere.
---

# The research program for $F_{\Co,n}$, $2 \leq n \leq 10$ {#sec-coble-families-research-program}

## Setting

::: {#cons:coble-set-lattices .construction title="The lattices from a Coble set" defines="$M$; $N$; $F_{\Co,n}$"}

Let $S$ be a terminal (@def:coble-surface) Coble surface (@def:coble-surface) of K3 type with $n$ boundary components, and let $X$ be its K3 double cover (@not:coble-ten-point-blowup), branched along $C = C_1 + \cdots + C_n$.
For a general such $S$, $\Pic(X)$ is the $2$-elementary lattice $M$ of @tbl-coble-lattices with invariants $(r,a,\delta) = (10+n,\, 12-n,\, \delta)$.
The period domain construction of @sec-moduli-construction, applied to $M$ and its orthogonal complement $N = M^{\perp\lkt}$, gives the moduli spaces $F_{\Co,n}$.
:::

::: {.corollary #cor:coble-lattices-genus-zero title="The Coble lattices have $g = 0$"}

For each lattice $M$ of @tbl-coble-lattices, the invariant $g = \tfrac12(22-r-a)$ of @prop:nikulin-fixed-locus is $0$, and $k = \tfrac12(r-a) = n-1$.

:::

::: {.proof}

By @prop:coble-table-invariants, $r = 10+n$ and $a = 12-n$, so $22-r-a = 0$ and $r-a = 2n-2$.

:::

::: {.proposition #prop:coble-families-in-enriques-moduli title="Each Coble family lies in the Coble divisor of Enriques moduli"}

For each lattice $M$ of rank $10+n$ in @tbl-coble-lattices, the moduli functor of $M$-polarized K3 surfaces of [@CDL25, §5.4] embeds into the moduli functor of $E_{10}(2)$-polarized K3 surfaces.
Its image is an open subset of an irreducible closed subset (@def:irreducible-closed-subset) (@def:closed-subset) of codimension $n-1$ of the quotient $\Gamma^\sharp_{\mathrm{Enr}}\backslash\mch(-2)$ of the $(-2)$-Heegner divisor of the Enriques period domain, and it is a coarse moduli space of Coble surfaces (@def:coble-surface) with $n$ boundary components [@CDL25, §5.4, Prop. 5.4.6 and the paragraph after it].
For $n = 1$, the image under the period map (@def:period-map) is an open subset of $\mcm_{\mathrm{Coble}}$, and the coarse moduli space is the coarse moduli space of marked Coble surfaces with $n = 1$ [@CDL25, Prop. 5.4.6].

:::

## The row of Nikulin's triangle {#sec-coble-row}

The programme's organizing observation is that the lattices of @tbl-coble-lattices are the $g = 0$ row of Nikulin's triangle.
This section derives that row from the existence theorem for even $2$-elementary lattices, so that the objects are the row's and not a transcription, and records what the derivation corrects.

::: {.notation title="The triangle and its edge" defines="Nikulin triangle; $(r, a, \delta)$; $(t_+, t_-)$"}

For an even $2$-elementary lattice $S$ write $(r, a, \delta)$ for the rank, the generator length $a(S)$ of @def:p-elementary and the coparity $\delta_S$, and $(t_+, t_-)$ for its signature; thus $r = t_+ + t_-$.
Nikulin's Theorem 3.6.2 [@Nik80, Thm. 3.6.2, printed pp. 144--145] gives the conditions for the existence of an even $2$-elementary lattice with prescribed $(\delta; t_+, t_-, a)$, and it determines the lattice up to isometry once $t_+ > 0$ and $t_- > 0$.
The two conditions used below read $a \leq t_+ + t_-$ and $t_+ + t_- + a \equiv 0 \pmod 2$.

On the rows of @tbl-coble-lattices the lattice $M$ is $\Pic(X)$ of the K3 cover, so it contains the ample class of @prop:nikulin-fixed-locus and lies in $H^{1,1}(X)$ of signature $(1,19)$; hence $t_+ = 1$ and $t_- = r - 1$.
With $t_+ = 1$ the two conditions become $a \leq r$ and $r + a \equiv 0 \pmod 2$, and the fixed-locus formula $g = \tfrac12(22 - r - a)$, $k = \tfrac12(r - a)$ of @prop:nikulin-fixed-locus, whose $g$ is a genus and so is not negative, adds
$$
a \leq r, \qquad r + a \leq 22 .
$$
The region these bound in the $(r, a)$-plane is the triangle; its edge $r + a = 22$ is the $g = 0$ row, and every row of @tbl-coble-lattices satisfies $r + a = 22$ by @cor:coble-lattices-genus-zero.
:::

::: {.theorem #thm:coble-row-is-g-zero title="The $g = 0$ row, and the rows of the Coble table"}

Let $M$ be an even $2$-elementary lattice of signature $(1, r-1)$ with invariants $(r, a, \delta)$ and $r + a = 22$, and suppose $M = \Pic(X)$ for a K3 surface $X$ with a non-symplectic involution acting as $-\id$ on $T(X)$ (@prop:nikulin-fixed-locus).

1. Then either $\delta = 1$ and $2 \leq a \leq 11$, or $\delta = 0$ and $a = 4$.
2. The eleven triples so obtained are $(11,11,1)$, $(12,10,1)$, $(13,9,1)$, $(14,8,1)$, $(15,7,1)$, $(16,6,1)$, $(17,5,1)$, $(18,4,0)$, $(18,4,1)$, $(19,3,1)$ and $(20,2,1)$, and each is the invariant data of exactly one isometry class.
3. They are the rows of @tbl-coble-lattices.
:::

::: {.proof}

$M$ is even and primitive in $\lkt$ of rank $r$, so $N \definedas M^{\perp\lkt}$ is even of rank $22 - r = a$ and signature $(2,\, 19 - (r-1)) = (2,\, a-2)$, and its discriminant form is $q_N \cong -q_M$ [@Nik80, Cor. 1.6.2, printed p. 112].
So $N$ is $2$-elementary with $a(N) = a$ and $\delta(N) = \delta$, and two applications of @thm:two-elementary-classification are needed: one to $M$, with $(\delta; t_+, t_-, a) = (\delta; 1, 21-a, a)$, and one to $N$, with $(\delta; 2, a-2, a)$.

*On $M$.* The condition $a \leq t_+ + t_-$ reads $a \leq 22 - a$, and the parity condition reads $22 \equiv 0$.
The conditions attached to $a = 0$ and to $a = 1$ exclude both: at $a = 0$ the condition is $\delta = 0$ with $t_+ - t_- \equiv 0 \pmod 8$, but $1 - 21 = -20 \equiv 4 \pmod 8$; at $a = 1$ it is $t_+ - t_- \equiv \pm 1 \pmod 8$, but $1 - 20 = -19 \equiv 5 \pmod 8$.
For $\delta = 0$ the condition $t_+ - t_- \equiv 0 \pmod 4$ reads $a - 20 \equiv 0 \pmod 4$, which at $a = 11$, the only $a$ with $a = t_+ + t_-$, fails; so no $\delta = 0$ row has $a = 11$.

*On $N$.* The condition $a \leq t_+ + t_-$ is an equality, $a \leq 2 + (a-2)$, and the parity condition is $2a \equiv 0$.
The condition attached to $a = t_+ + t_-$ therefore holds identically on $N$, and for $\delta = 0$ the two conditions read $2 - (a-2) = 4 - a \equiv 0 \pmod 8$, that one, and $4 - a \equiv 0 \pmod 4$.
Since $N$ is a lattice of signature $(2, a-2)$, one has $a \geq 2$, which excludes $a = 0$ and $a = 1$ a second time.

So $\delta = 1$ gives $2 \leq a \leq 11$, that is the ten triples $(12-a,\, a,\, 1)$; and $\delta = 0$ gives $a \equiv 0 \pmod 4$ from $M$ and $a \equiv 4 \pmod 8$ from $N$, hence $a = 4$ and $r = 18$, the single triple $(18,4,0)$.
Uniqueness is the uniqueness clause of @thm:two-elementary-classification, applicable to $M$ because $t_- = 21 - a \geq 10 > 0$.
Each triple is a row of @tbl-coble-lattices by @prop:coble-table-invariants.
:::

::: {.corollary #cor:coble-row-ten-and-eleven title="Ten values of $n$, eleven lattices"}

Write $n \definedas 12 - a$. The ten triples with $\delta = 1$ are the lattices $(10+n,\, 12-n,\, 1)$ for $n = 1, \dots, 10$, and the eleventh is $(18,4,0)$, which has $n = 8$.
Hence @tbl-coble-lattices has one row for each $n$ from $1$ to $10$ and two rows at $n = 8$, the family $(10+n,\, 12-n,\, \delta)$ is a family of ten values of $n$ and eleven lattices, and the "ten lattices" of the programme's organizing observation counts $n$ and not lattices.
The triple $(14,8,0)$ lies on the edge and is a lattice, but it is not one of the eleven: by (2) of the proof the complement $N$ of $(14,8,0)$ would be an even lattice (@def:even-lattice) of signature $(2,6)$ with $(\delta; t_+, t_-, a) = (0; 2, 6, 8)$, and the condition attached to $a = t_+ + t_-$, which holds there with equality, requires $2 - 6 = -4 \equiv 0 \pmod 8$, which fails.
:::

::: {.proof}

The substitution $n = 12 - a$ bijects $\{2, \dots, 11\}$ with $\{10, \dots, 1\}$ and carries $(12-a, a, 1)$ to $(10+n, 12-n, 1)$; $a = 4$ is $n = 8$.
The exclusion of $(14,8,0)$ is the computation of the proof of @thm:coble-row-is-g-zero read at its complement.
:::

::: {.remark #rmk:coble-row-forces-the-cdl-corrections title="The row forces the two corrections to the published table"}

The two entries of [@CDL25, Table 5.1, p. 553] that @prop:coble-table-cdl-corrections corrects are forced by @thm:coble-row-is-g-zero rather than independent repairs: at $n = 2$ the row carries $a = 10$, so the lattice $\mathrm{E}_{10}(2)\oplus \mathrm{A}_1^{\oplus 2}$ of generator length $12$ that the proposition rules out cannot be its entry, and at $n = 10$ the row carries $a = 2$ and hence $r = 20$, so the number of blown-up points is $19$ and not the $20$ that the table prints.
:::

## The three conjectures of the programme, and their verdicts

The programme stated three conjectures for the families $F_{\Co,n}$.  Each is settled below, two of them negatively as stated, and the residue of each is named.

### The Baily--Borel boundaries {#sec-coble-n-boundaries}

::: {.proposition #prop:coble-n-twist-form title="The period lattice of every Coble family is a twist of a unimodular lattice"}

For each row of @tbl-coble-lattices let $M_n$ be the lattice $M$ and $N_n = M_n^{\perp\lkt}$ its orthogonal complement (@prop:coble-table-invariants).
Then $N_n = B_n(2)$ with $B_n$ unimodular of signature $(2,\, 10-n)$: $B_n = \latI_{2,10-n}$ in the ten rows with $\delta = 1$ and $B_n = U^{\oplus 2}$ in the row $(18,4,0)$.
Consequently:

1. $A_{N_n} \cong B_n/2B_n$, and under this identification the discriminant quadratic form (@def:discquad) is $q_{N_n}([x/2]) = b_{B_n}(x,x) \bmod 2$ and the discriminant representation (@def:discriminant-rep) is reduction modulo $2$;
2. every primitive vector $v\in N_n$ has divisibility (@def:lattice-divisibility) exactly $2$ in $N_n$, so the class $[v/2]\in A_{N_n}$ is defined and nonzero;
3. $\bD(N_n)$ has complex dimension $10 - n$.
:::

::: {.proof}

The complement column of @tbl-coble-lattices is @prop:coble-table-invariants, namely $N_n = \latI_{2,10-n}(2)$ in the ten rows with $\delta = 1$, and $N_n = U(2)^{\oplus 2} = (U^{\oplus 2})(2)$ in the row $(18,4,0)$, whose negative index (@def:negative-index) is $10 - 8 = 2$.
The lattice $\latI_{2,10-n}$ is odd unimodular of signature $(2, 10-n)$ and $U^{\oplus 2}$ is even (@def:form-axioms) unimodular of signature $(2,2)$, so in each row $N_n = B_n(2)$ with $B_n$ unimodular of that signature.

(1) For a unimodular $B$ the dual of $T = B(2)$ is $\tfrac12 B$: the form of $T$ is $2b_B$, its inverse form is $\tfrac12 b_B^{-1}$, and in a basis (@def:based-module) of $B$ the matrix of $b_B^{-1}$ is unimodular; so
$$
A_T = (\tfrac12 B)/B \cong B/2B .
$$
For $x\in B$ one has $(x,x)_T = 2\,b_B(x,x)$, so $q_T([x/2]) = \tfrac12(x,x)_T = b_B(x,x) \bmod 2$.
An isometry of $T$ is an isometry of $B$, because the two forms differ by the scalar $2$, and it carries $\tfrac12 v$ to $\tfrac12 gv$; so its action on $A_T$ is its own reduction modulo $2$.
(2) A primitive $v\in T$ is primitive in $B$, the two lattices having the same underlying abelian group; so $(v,B) = \ZZ$ and $(v,T) = 2\,(v,B) = 2\ZZ$, that is $\div_T(v) = 2$, and $[v/2]\neq 0$ because $v\notin 2B$.
(3) $\rank N_n = 12-n$ and the signature of $N_n$ is $(2,\,10-n) = (2,\,(12-n)-2)$, so @prop:type-iv-dimension gives $\dim_\CC\bD(N_n) = (12-n)-2 = 10-n$.
:::

::: {.theorem #thm:coble-n-boundaries-verdict title="Verdict on the boundary conjecture"}

The conjecture was that the Baily--Borel boundaries of all ten families are computable by the techniques used at $n = 1$, which were three: the reduction of the cusp orbits (@def:group-orbit) through the discriminant kernel, a computation on the finite group $A_N$ (@thm:coble-zero-cusp-count); Vinberg's algorithm at each cusp, which produces the chamber and its diagram (@cor:vinberg-terminates-reflective); and the Tits incidence between the orbits of lines and of planes (@prop:coble-arithmetic-flag-incidence).

1. The structural input of the first step transfers to every row: by @prop:coble-n-twist-form the period lattice $N_n$ is a twist $B_n(2)$ of a unimodular lattice, so its discriminant group, its quadratic form and its discriminant representation (@def:discriminant-rep) have the same description as at $n = 1$.
   What does not transfer with it is the pair of statements that the $n = 1$ computation uses to identify the fibres over the classes, and those are stated only for $B = \latI_{2,9}$ (@lem:I29-plus-line-transitivity, @lem:cusp-vector-stabilizer-image); for another row they must be proved again, and no row of this chapter proves them.
2. The second step fails in three rows: for $M = (17,5,1)$, $(18,4,1)$ and $(19,3,1)$ the group $W_r(M)$ has infinite index (@thm:nonreflective-r-plus-a-22), Vinberg's algorithm does not terminate (@cor:vinberg-terminates-reflective), and the reflection semifan (@def:semitoroidal-compactification) of $W_r(M)$ is not a fan (@def:coxeter-semifan, from [@AE22, Def. 3.5, printed p. 10]).
   These three families have no chamber at any cusp, so no boundary diagram of them is computed by the $n = 1$ technique; what replaces it is the mirror-move classification of their $0$-cusps and boundary lattices (@prop:coble-table-cusp-boundary-lattices), which is an application of [@AE22, Def. 5.6 and Thm. 5.8, printed p. 23] and not of the $n = 1$ technique.
3. Two rows have no boundary of the shape the comparison needs: for $n = 9$ the lattice $N_9 = \latI_{2,1}(2)$ has negative index (@def:negative-index) one, so it has primitive isotropic vectors (@def:isotropic-subspace) and no primitive isotropic plane, and $F_{\Co,9}$ has no $1$-cusp and no Tits edge; for $n = 10$ the lattice $N_{10} = \latI_{2,0}(2)$ is positive definite, $\bD(N_{10})$ is one point, the family is zero-dimensional and it has no $0$-cusp (@prop:coble-table-cusp-boundary-lattices, with @prop:type-iv-dimension).

So the conjecture is false as stated.
The ten families, which are the ten values of $n$, fall into four classes, each named by its values of $n$:

- $n = 1$: established --- its $0$-cusps and $1$-cusps for the stable group are @thm:coble-zero-cusp-count and @thm:plane-fibre, each of them a count of lattice orbits through @thm:coble-integral-lifting-fibre, and @conj:gamma-co-stable carries them to $\fco$.
- $n = 2, 3, 4, 5, 6$: unproved, because @lem:I29-plus-line-transitivity and @lem:cusp-vector-stabilizer-image are stated for $B = \latI_{2,9}$ alone, and no row of this chapter proves them for another $B_n$.
- $n = 7$, $n = 8$ with $\delta = 1$, and $n = 9$: non-reflective (@thm:nonreflective-r-plus-a-22), so the $n = 1$ chamber technique does not apply to them.
- $n = 9$ and $n = 10$: no boundary of the shape the comparison needs, by (3).

A family that fails for two reasons is named under both reasons and counted once in the total: the count is $1 + 5 + 3 + 2 - 1 = 10$, the subtracted family being $n = 9$, the only one that lies in two of the four classes.
:::

::: {.proof}

(1) is @prop:coble-n-twist-form(1) and the observation that @lem:I29-plus-line-transitivity and @lem:cusp-vector-stabilizer-image are statements about $\latI_{2,9}$.
(2) is the cited non-reflectivity together with @cor:vinberg-terminates-reflective and @def:coxeter-semifan, from [@AE22, Def. 3.5, printed p. 10]; a Coxeter chamber is the fundamental domain (@def:fundamental-domain) of $W_r$, which does not exist when $W_r$ has infinite index.
(3) the negative index of $N_9$ is one by @prop:coble-table-invariants, so a totally isotropic subspace (@def:isotropic-subspace) has dimension at most one; the statement about $n = 10$ is the last sentence of @prop:coble-table-cusp-boundary-lattices.
:::

### The ramification divisor {#sec-coble-n-recognizable}

::: {.lemma #lem:coble-cover-involution-nonsymplectic title="The covering involution is non-symplectic"}

For every $n$ the covering involution $\sigma$ of the K3 cover $f\colon X\to S$ of @prop:coble-k3-cover is non-symplectic.
:::

::: {.proof}

At a smooth point of the branch divisor $C_i\subset S$ the map $f$ is, in suitable coordinates, $(u,v)\mapsto (u,v^2)$, so $\sigma(u,w) = (u,-w)$ and $\sigma^*(\dd u\wedge \dd w) = -\dd u\wedge \dd w$.
The form $\dd u\wedge\dd w$ is a local generator of $\omega_X = \OO_X$, so $\sigma$ acts as $-1$ on $H^{0}(X,\Omega^2_X)$.
:::

::: {.theorem #thm:coble-n-recognizable-verdict title="Verdict on the recognizable-divisor conjecture"}

The conjecture was that a divisor constructed from the ramification locus of the K3 cover is recognizable in the sense of @def:recognizable-divisor, in a way that gives a semitoroidal compactification by @thm:recognizable-semitoroidal.

1. The ramification divisor $R = X^\sigma$ is, in every row, a disjoint union of $n$ smooth rational curves of square $-2$: the involution is non-symplectic (@lem:coble-cover-involution-nonsymplectic), so @prop:nikulin-fixed-locus applies, with $g = 0$ and $k = n-1$ by @cor:coble-lattices-genus-zero, and the fixed components are the $\bar C_i$ of @prop:coble-k3-cover(3).
2. Since $K_X = 0$, one has $(K_X + \eps R)\cdot \bar C_i = \eps\,\bar C_i^2 = -2\eps < 0$ for every component, so $K_X + \eps R$ is not nef and the pair $(X, \eps R)$ fails the ampleness condition of @def:ksba-compactification for every $\eps \in (0,1]$.
   The ramification locus therefore cannot be the polarizing divisor of the \KSBA compactification whose normalization @thm:recognizable-semitoroidal identifies with a semitoroidal compactification.
The disproof is item (2), and item (2) alone carries it: it uses only $K_X = 0$ and $\bar C_i^2 = -2$. The verdict makes no claim about recognizability, for which no printed page covering the $g = 0$ fixed locus is recorded here; what is recorded for this corner of the literature is @rmk:coble-g-zero-outside-ae22.

So the conjecture is false as stated, and its content moves to the choice of a divisor that is positive on the fixed components: see @qst:coble-n-polarizing-divisor.
:::

::: {.proof}

(1) is @prop:coble-k3-cover(3), which gives the $\bar C_i$ as disjoint $(-2)$-curves, together with @prop:nikulin-fixed-locus at the invariants of @tbl-coble-lattices, for which @cor:coble-lattices-genus-zero gives $g = 0$ and $k = n-1$.
(2) is the computation $R\cdot\bar C_i = \bar C_i^2 = -2$ from the disjointness in (1), and the ampleness condition of @def:ksba-compactification, which for $K_X = 0$ is the ampleness of $R$.
The verdict stops at (2): $K_X = 0$ and $\bar C_i^2 = -2$ give $(K_X + \eps R)\cdot\bar C_i < 0$, and nothing about recognizability is needed for it.
:::

::: {.remark #rmk:coble-g-zero-outside-ae22 title="Why the literature's identification does not cover these rows"}
The identification of the \KSBA compactification of a family of K3 surfaces with a non-symplectic involution with a semitoroidal one is recorded for the families on which the fixed locus has a component of genus at least $2$, by the ramification-divisor semifan [@AE22, Thm. 9.10, printed p. 56]; the rows of @tbl-coble-lattices have $g = 0$. The same restriction is recorded in @qst:coble-nonreflective-semifans, with the reading [@AE22, §4C, printed pp. 16--17] of the ramification divisor on the line $g = 0$: there the ramification divisor is "the union of the $n$ curves $E_{2i}$", a union of rational curves and not a positive-genus component, and the recognizability theorem recorded for the fixed curve is [@AEH24, Thm. 3.24, p. 12], stated for the fixed curve of genus at least two.
:::

::: {.question #qst:coble-n-polarizing-divisor title="A polarizing divisor for the $g = 0$ rows"}

Which divisor on the K3 covers of the Coble families is recognizable in the sense of @def:recognizable-divisor and positive on the components $\bar C_i$ of the ramification divisor, so that @thm:recognizable-semitoroidal applies to the pairs $(X, \eps(R + a f^*H))$?
For an ample $H$ on $S$ one has $(f^*H)\cdot \bar C_i = 2\,H\cdot C_i > 0$, so the positivity in @thm:coble-n-recognizable-verdict(2) is met by a combination of $R$ and $f^*H$; recognizability of such a combination is not covered by @ex:recognizable-divisors.
:::

### The semifans and the Coxeter fans {#sec-coble-n-semifans}

::: {.theorem #thm:coble-n-semifan-verdict title="Verdict on the semifan conjecture"}

The conjecture was that the semifans are either refinements or coarsenings of the canonical Coxeter fans at the Baily--Borel cusps.

1. Where a Coxeter chamber exists and a marking into relevant and irrelevant roots is given, the semifan compared with the fan is a coarsening and never a refinement: the generalized Coxeter semifan is $C_{\mathrm{gen}} = \bigcup_{h\in W_{\mathrm{irr}}} hC$, obtained from the fan $\mathcal F^{\mathrm{cox}}$ by deleting the faces spanned by irrelevant roots [@AEGS25, p. 610].
   This is a construction from the chamber and the marking, and not a statement that the semifan of the semitoroidal compactification of a Coble family equals it.
2. In the three non-reflective rows $n = 7$, $8$ with $\delta = 1$ and $9$ there is no Coxeter fan: $W_r(M)$ has infinite index (@thm:nonreflective-r-plus-a-22), Vinberg's algorithm does not terminate (@cor:vinberg-terminates-reflective), and the reflection semifan of $W_r(M)$ is not a fan (@def:coxeter-semifan, from [@AE22, Def. 3.5, printed p. 10]).
   The comparison has no left-hand side there, and the replacement that the chapter records for those rows is the mirror-move classification of @prop:coble-table-cusp-boundary-lattices.

So the conjecture is false as stated for three of the ten families, and where it is not, its first alternative does not occur and its second is the definition of the semifan rather than an identification of it: which semifan the semitoroidal compactification of a Coble family uses is @qst:semifan-poset-position and @qst:coble-nonreflective-semifans.
:::

::: {.proof}

(1) is the definition of the generalized Coxeter semifan as recorded on [@AEGS25, p. 610]: the faces it deletes are the ones spanned by irrelevant roots, so its faces are faces of $\mathcal F^{\mathrm{cox}}$.
(2) is the non-reflectivity of @thm:nonreflective-r-plus-a-22, the termination criterion of @cor:vinberg-terminates-reflective, and @def:coxeter-semifan, from [@AE22, Def. 3.5, printed p. 10].
:::

Related: [The Coble cusp correspondence and the morphism chain](#sec-cusp-correspondence-morphism-chain), [Moduli of index 2 Halphen and rational elliptic surfaces](#sec-halphen-index-2-moduli-program), [The nodal Enriques moduli program](#sec-nodal-enriques-moduli-program).
