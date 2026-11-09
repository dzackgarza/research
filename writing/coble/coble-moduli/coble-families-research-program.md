---
unit: research-program
status: conjectural
tags:
  - coble
  - moduli
  - ksba
  - recognizable-divisor
notes: |-
  Provenance: `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/research-statements/canonical/my_research_statement/ResearchStatement.md`, section "Future Work / Coble surfaces with $1\leq n\leq 10$ boundary components".
  Not in the dissertation.
  The table of the ten lattices $M = (10+n,\, 12-n,\, \delta)$ and their orthogonal complements $N = M^\perp$ is **already recorded** in [[coble-lattice-table|the Coble lattice table]], sourced from Cossec-Dolgachev-Liedtke, *Enriques Surfaces I*, Table 5.1, p. 553. This note records only the research program built on it, which is not recorded elsewhere.
---

# The research program for $F_{\Co,n}$, $2 \leq n \leq 10$ {#sec-coble-families-research-program}

## Setting

::: {.construction title="The lattices from a Coble set"}

Let $S$ be a terminal Coble surface of K3 type with $n$ boundary components, and let $X$ be its K3 double cover, branched along $C = C_1 + \cdots + C_n$.
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
Its image is an open subset of an irreducible closed subset of codimension $n-1$ of the quotient $\Gamma^\sharp_{\mathrm{Enr}}\backslash\mch(-2)$ of the $(-2)$-Heegner divisor of the Enriques period domain, and it is a coarse moduli space of Coble surfaces with $n$ boundary components [@CDL25, §5.4, Prop. 5.4.6 and the paragraph after it].
For $n = 1$, the image under the period map is an open subset of $\mcm_{\mathrm{Coble}}$, and the coarse moduli space is the coarse moduli space of marked Coble surfaces with $n = 1$ [@CDL25, Prop. 5.4.6].

:::

## The conjectural program

::: {.conjecture title="Boundary incidence diagrams are computable for all n"}

The Baily-Borel boundaries of all ten families can be described by the techniques used for $n=1$.
The boundary incidence diagrams are computable by the algorithms of [@AE22] for nonsymplectic involutions.
:::

::: {.conjecture title="Recognizability of the ramification locus"}

The ramification locus of the K3 cover of $S$ is described in @prop:nikulin-fixed-locus. The conjecture has two parts:

1. the corresponding involutions are nonsymplectic;

2. a component of the ramification locus is a **recognizable divisor** in the sense of Alexeev's compact moduli of K3 surfaces and AEH21.

Under part 2, AEH21 Thm.
3.24 identifies the KSBA compactification with a semitoroidal compactification for a specific collection of semifans.
:::

::: {.conjecture title="The semifans refine or coarsen the Coxeter fans"}

These semifans are either refinements or coarsenings of the canonical Coxeter fans at the Baily-Borel cusps, and admit an explicit description via an extension of the theory of ADE surfaces (AT21). From that data one extracts a classification of dlt models for KSBA stable limits, hence a first description of $\partial\overline{F}_{\Co,n}$, as AEGS23 did for numerically polarized Enriques surfaces.
:::

Related: [The Coble cusp correspondence and the morphism chain](#sec-cusp-correspondence-morphism-chain), [Moduli of index 2 Halphen and rational elliptic surfaces](#sec-halphen-index-2-moduli-program), [The nodal Enriques moduli program](#sec-nodal-enriques-moduli-program).
