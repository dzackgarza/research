---
title: Moduli of index 2 Halphen and rational elliptic surfaces
unit: research-program
status: conjectural
tags:
  - halphen
  - rational-elliptic
  - git
  - ksba
---

# Moduli of index 2 Halphen and rational elliptic surfaces

**Provenance.** `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/research-statements/canonical/my_research_statement/ResearchStatement.md`, section "Future Work / Halphen and rational elliptic surfaces".
Absent from the dissertation.

The geometric Coble-Halphen correspondence is **already recorded** in this project at `content_pandoc/sections/Degenerations/Halphen_Surfaces.md`, including the conjecture that the Coble families and the index 2 Halphen families match along the $g=0$ line of Nikulin's triangle.
This note records the moduli-theoretic program built on that observation, which is not recorded there.

## Definitions and known moduli

::: {.Definition}
### Index, Halphen pencil, Halphen surface

A **rational elliptic surface** is a smooth projective rational surface $Y$ with a relatively minimal fibration $\pi: Y\to\PP^1$ whose generic fiber is a smooth elliptic curve.
Its **index** is the minimal $m$ with $\pi$ given by $|-mK_Y|$.
A **Halphen pencil of index $m$** is a pencil of degree $3m$ curves in $\PP^2$ with 9 basepoints; minimally resolving its basepoints gives a **Halphen surface of index $m$**. Equivalently, $Y$ is Halphen of index $m$ when $|-mK_Y|$ has dimension 1, no fixed part, and is basepoint free.
Every relatively minimal rational elliptic surface is Halphen of some index.
:::

::: {.Remark}
### What is already constructed in the literature

- $M_{H,1}$ is an open subset of the Grassmannian $\Gr_2(10)$ of pencils of plane cubics, irreducible of dimension 8.

- $M_{H,m}$ for $m\geq 2$ fibers over $M_{H,1}$ with 1-dimensional fibers, conjecturally irreducible of dimension 9.

- Miranda (1981) compactifies $M_{H,1}$ by GIT applied to Weierstrass models.

- Miranda (2021) constructs $M_{H,2}$ and shows it is a **toric variety of dimension 9**.

- Zanardini (2023) studies GIT stability of index 2 Halphen pencils in $\PP^2$, toward a GIT compactification of $M_{H,2}$.
:::

## The lattice matching

::: {.Remark}
### Where the Coble lattices reappear

In AE22, the case $S = (10,10,1)$ corresponds to K3 surfaces $X$ with a nonsymplectic involution $\iota$ such that $Y \da X/\iota$ is an index 2 Halphen pencil.
More generally, by AE22 section 4C, the lattices $S = (10+n,\, 12-n,\, \delta)$ for $1\leq n\leq 9$ give index 2 Halphen K3 surfaces $X$ with an $I_{2k}$ fiber, and contracting the $(-1)$-curves in the special fiber yields index 2 Halphen pencils with an $I_k$ fiber.

These are **precisely the lattices of `tbl:coble-lattices`**, the ten Coble families of [the Coble families research program](../coble-moduli/coble-families-research-program.md).
The lattice coincidence is the whole content of the conjecture: two geometrically different families of surfaces are attached to one line of Nikulin's triangle.
:::

## The program

::: {.Conjecture}
### Period domains and KSBA compactifications for M_(H,2,k)

These lattices can be used to construct period domains of index 2 Halphen pencils, yielding moduli spaces $M_{H,2,k}$ of index 2 Halphen surfaces with an $I_{2k}$ fiber, with the matching arising from a geometric comparison to Coble surfaces.
The normalizations of the stable pair compactifications $\overline{M_{H,2,k}}^R$ are then isomorphic to semitoroidal compactifications of the corresponding period domains, for a suitably canonical divisor $R$.
:::

::: {.Conjecture}
### The multiple fiber as the recognizable divisor

A Halphen surface of index $m\geq 2$ has a unique multiple fiber of multiplicity $m$.
That fiber can be used to construct a recognizable divisor $R$.
This is the load-bearing conjecture: it is what supplies the $R$ the previous conjecture needs.
:::

## The stated starting point

The Coxeter diagram for $S \da (10,10,1)$ is well known and the K3 moduli theory is developed, so the program begins there:

1. Construct the period domain $F_S$.

2. Construct $\overline{F_S}^{\bb}$.

3. Study $\Orth(S)$-orbits of isotropic vectors $e_i$ in $S$.

4. Determine the cusp diagram of $\partial\overline{F_S}^{\bb}$ lattice-theoretically.

5. Compute $e_i^\perp/\gens{e_i}$ and the Coxeter diagrams at the corresponding 0-cusps.

6. Find a recognizable divisor $R$ and construct $\overline{F_S}^R$.

7. Use AE22 to construct dlt models and integral-affine structures classifying $\partial\overline{F_S}^R$.

Steps 3 through 5 are exactly the recipe recorded in [the computational toolchain and recipe](../computations/computational-toolchain-and-recipe.md), applied to a new lattice.

::: {.Remark}
### Why the program is stated as worth doing

It opens a comparison between GIT and KSBA compactifications, since $M_{H,1}$ and $M_{H,2}$ already have GIT compactifications in the literature while their KSBA compactifications do not exist.
Generalizing to $\overline{M_{H,m}}^R$ for $m>2$ would give new moduli spaces of general rational elliptic surfaces with no restriction on fiber type.
:::

Related: [Coble families research program](../coble-moduli/coble-families-research-program.md), [nodal Enriques moduli program](nodal-enriques-moduli-program.md), [computational toolchain and recipe](../computations/computational-toolchain-and-recipe.md).
