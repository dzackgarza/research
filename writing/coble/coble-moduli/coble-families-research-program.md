---
title: The research program for F_(Co,n) with 2 <= n <= 10
unit: research-program
status: conjectural
tags:
  - coble
  - moduli
  - ksba
  - recognizable-divisor
---

# The research program for $F_{\Co,n}$, $2 \leq n \leq 10$

**Provenance.** `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/research-statements/canonical/my_research_statement/ResearchStatement.md`, section "Future Work / Coble surfaces with $1\leq n\leq 10$ boundary components".
Not in the dissertation.

The table of the ten lattices $M = (10+n,\, 12-n,\, \delta)$ and their orthogonal complements $N = M^\perp$ is **already recorded** in this project at `content_pandoc/tables/coble_lattices.md` (`tbl:coble-lattices`), sourced from Cossec-Dolgachev-Liedtke, *Enriques Surfaces I*, Table 5.1, p. 553. This note records only the research program built on it, which is not recorded elsewhere.

## Setting

::: {.Construction}
### The lattices from a Coble set

Let $\Sigma$ be a general **Coble set** of points in $\PP^2$, so that the blowup $S$ of $\PP^2$ along $\Sigma$ is a Coble surface double covered by a K3 surface $X$ branched along $C = C_1 + \cdots + C_n$.
The construction used for $n=1$ (the divisors $e_0,\ldots,e_{10}$ in $X$, with $e_0$ the pullback of the hyperplane class and $e_i$ the preimages of the exceptional divisors over the nodes) yields, in general, a collection of primitively embedded 2-elementary sublattices $L_1,\ldots,L_{10} \containedin \Pic(X)$ with invariants $(r,a,\delta) = (10+n,\, 12-n,\, \delta)$.
Applying the period domain construction to these lattices yields ten moduli spaces $F_{\Co,n}$.
:::

::: {.Remark}
### Position in Nikulin's triangle

This collection of ten lattices **coincides precisely with the $g=0$ line** of Nikulin's triangular table of 2-elementary lattices (AE22, Fig. 1). That identification is the organizing observation behind the whole program, and is also what ties the Coble families to the index 2 Halphen families; see [[halphen-index-2-moduli-program]].
:::

The moduli spaces $F_{\Co,n}$ for $n \geq 2$ have not appeared in the literature.
The $n=1$ case is the subject of the current project.

## The conjectural program

::: {.Conjecture}
### Boundary incidence diagrams are computable for all n

The Baily-Borel boundaries of all ten families can be described by the techniques used for $n=1$.
Several of the boundary incidence diagrams have already been computed by the author using the algorithms of AE22 (nonsymplectic involutions); the remaining ones are similarly computable.
This would be the first explicit study of these boundaries in the literature.
:::

::: {.Conjecture}
### Recognizability of the ramification locus

The ramification locus of the K3 cover of $S$ is described in *Enriques Surfaces I*, Eqn.
5.3.1. The conjecture has two parts:

1. the corresponding involutions are nonsymplectic;

2. a component of the ramification locus is a **recognizable divisor** in the sense of Alexeev's compact moduli of K3 surfaces and AEH21.

Under part 2, AEH21 Thm.
3.24 identifies the KSBA compactification with a semitoroidal compactification for a specific collection of semifans.
:::

::: {.Conjecture}
### The semifans refine or coarsen the Coxeter fans

These semifans are either refinements or coarsenings of the canonical Coxeter fans at the Baily-Borel cusps, and admit an explicit description via an extension of the theory of ADE surfaces (AT21). From that data one extracts a classification of dlt models for KSBA stable limits, hence a first description of $\partial\overline{F_{\Co,n}}$, as AEGS23 did for numerically polarized Enriques surfaces.
:::

::: {.Remark}
### Each family embeds into unpolarized Enriques moduli

By *Enriques Surfaces I*, Prop.
5.4.6, for each rank-$(10+n)$ lattice in `tbl:coble-lattices` there is an embedding
$$
F_{\Co,n} \injects \fen
$$
into the moduli space of Enriques surfaces, constructed from $E_{10}(2)$-polarized K3 surfaces.
Consequently the integral-affine structures, and hence the dlt and stable models, can be obtained by restricting the K3 boundary data of AE22. This is the mechanism that makes the whole family tractable at once, rather than one $n$ at a time.
:::

Related: [[cusp-correspondence-morphism-chain]], [[halphen-index-2-moduli-program]], [[nodal-enriques-moduli-program]].
