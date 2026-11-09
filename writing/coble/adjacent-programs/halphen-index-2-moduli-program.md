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

::: {.definition title="Index, Halphen pencil, Halphen surface"}

A **rational elliptic surface** is a smooth projective rational surface $Y$ with a relatively minimal fibration $\pi: Y\to\PP^1$ whose generic fiber is a smooth elliptic curve.
Its **index** is the minimal $m$ with $\pi$ given by $|-mK_Y|$.
A **Halphen pencil of index $m$** is a pencil of degree $3m$ curves in $\PP^2$ with 9 basepoints; minimally resolving its basepoints gives a **Halphen surface of index $m$**. Equivalently, $Y$ is Halphen of index $m$ when $|-mK_Y|$ has dimension 1, no fixed part, and is basepoint free.
Every relatively minimal rational elliptic surface is Halphen of some index.
:::

::: {.proposition #prop:known-halphen-moduli title="Moduli of rational elliptic surfaces of index $1$ and $2$"}

1. Marked rational elliptic surfaces of index $1$ depend on $8$ parameters and are parametrized by an open subset of the Grassmannian $\Gr(2,10)$ of pencils of plane cubics.
   Marked rational elliptic surfaces of index at least $2$ depend on $9$ parameters; the additional parameter is the choice of the multiple fiber [@MZ21, §1].

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

1. If $S = \HalphenInvariants$, then $Y$ is an index $2$ Halphen pencil, and the fixed locus $X^\iota$ is a smooth elliptic fiber that does not ramify over the unique multiple fiber of $Y$ [@AE22, Thm. 4.1(3)].

2. If $S = (10+k,\, 12-k,\, \delta)$ with $1\leq k\leq 9$, then $X$ is an index $2$ Halphen K3 surface with an $I_{2k}$ fiber, and contracting the $(-1)$-curves in the special fiber of $Y$ gives a rational index $2$ Halphen pencil with an $I_k$ fiber [@AE22, §4C].
:::

The lattices of @prop:halphen-k3-lattices(2) are the rows with $n = 1, \dots, 9$ of [the Coble lattice table](#sec-coble-lattice-table), both rows with $n = 8$ included.
The remaining row is $n = 10$, the lattice $(20,2,1)$.

## The program

::: {.conjecture title="Period domains and KSBA compactifications for $M_{H,2,k}$"}

These lattices can be used to construct period domains of index 2 Halphen pencils, yielding moduli spaces $M_{H,2,k}$ of index 2 Halphen surfaces with an $I_{2k}$ fiber, with the matching arising from a geometric comparison to Coble surfaces.
The normalizations of the stable pair compactifications $\overline{M_{H,2,k}}^R$ are then isomorphic to semitoroidal compactifications of the corresponding period domains, for a suitably canonical divisor $R$.
:::

::: {.conjecture title="The multiple fiber as the recognizable divisor"}

A Halphen surface of index $m\geq 2$ has a unique multiple fiber of multiplicity $m$.
That fiber can be used to construct a recognizable divisor $R$.
:::

## The program for $S = \HalphenInvariants$

Let $S \definedas \HalphenInvariants$.

1. Construct the period domain $F_S$.

2. Construct $\overline{F_S}^{\bb}$.

3. Study $\Orth(S)$-orbits of isotropic vectors $e_i$ in $S$.

4. Determine the cusp diagram of $\partial\overline{F_S}^{\bb}$ lattice-theoretically.

5. Compute $e_i^\perp/\generators{e_i}$ and the Coxeter diagrams at the corresponding 0-cusps.

6. Find a recognizable divisor $R$ and construct $\overline{F_S}^R$.

7. Use [@AE22] to construct dlt models and integral-affine structures classifying $\partial\overline{F_S}^R$.

Related: [Coble families research program](#sec-coble-families-research-program), [nodal Enriques moduli program](#sec-nodal-enriques-moduli-program), [computational toolchain and recipe](#sec-computational-toolchain-and-recipe).
