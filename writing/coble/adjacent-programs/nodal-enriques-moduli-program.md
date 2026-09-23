---
title: The nodal Enriques moduli program
unit: research-program
status: conjectural
tags:
  - nodal-enriques
  - non-2-elementary
  - moduli
---

# The nodal Enriques moduli program

**Provenance.** `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/research-statements/canonical/my_research_statement/ResearchStatement.md`, section "Future Work / Nodal Enriques surfaces", together with `/home/dzack/gitclones/diss/000-writing/.archive/thesis-outline/part3/08_Future_Directions.md` and `.../past_writing/mathematical_tools_and_concepts/730_nodal_enriques.md`. Absent from the dissertation entirely.

The lattices themselves are **already recorded** in this project at `content_pandoc/sections/Lattices_and_Moduli/Nodal_Enriques_Lattices.md`. This note records the research program and one discrepancy.

## Setting

::: {.Definition}
### Nodal and unnodal

An Enriques surface $Y$ is **nodal** if it contains a rational $(-2)$-curve, and **unnodal** otherwise.
A generic Enriques surface is unnodal, and $F_{\En,\mathrm{Nod}}$ is an irreducible hypersurface in $F_{\En}$.
:::

$$
S_{\Nod} = \gens{-4}\oplus U \oplus E_8(2),
\qquad
T_{\Nod} \da S_{\Nod}^\perp \cong \gens{4}\oplus U \oplus E_8(2),
$$
the generic Picard lattice of the K3 cover $X$ and its transcendental lattice.
$F_{\Nod}$ is realized as the divisor $\cH_{-4}/\Orth(T_{\En})$, a 9-dimensional irreducible quasiprojective variety.

::: {.Remark}
### Discrepancy to reconcile: two forms of the embedding

This project's `Nodal_Enriques_Lattices.md` records the primitive embedding $S_{\En}\injects S_{\Nod}$ as
$$
((e,f), x) \mapsto \big((2\tilde f + \tilde g + h,\ \tilde g),\ x\big),
$$
attributed to Cossec-Dolgachev-Liedtke p. 561. The research statement records it, citing *Enriques Surfaces I* Def.
5.6.3, as
$$
((e_1,f_1), x) \mapsto \big(f_2,\ 2e_2+f_2+h,\ x\big),
$$
with $h$ a generator of $\gens{-4}$.
Both are the identity on the $E_8(2)$ factor and both are claimed to exhibit $F_{\Nod}\injects F_{\En}$.
They are written in different bases and have not been checked against each other.
Reconciling them, or identifying which is correct, is a small and worthwhile task.
:::

## The program

::: {.Conjecture}
### Baily-Borel boundary by the same techniques

Orbits under $\Orth(T_{\Nod})$ of isotropic vectors and planes can be classified, yielding a boundary incidence diagram; and the lattice embedding above allows AEGS23 to be leveraged to construct the KSBA compactification, its dlt models, and the integral-affine structures classifying KSBA stable limits of nodal Enriques surfaces.
:::

::: {.Remark}
### Why this needs genuinely new machinery

$T_{\Nod}$ is **not 2-elementary**. The entire Sterk-Nikulin apparatus that both this project and the dissertation rely on assumes 2-elementarity, so the classification of boundary components requires developing orbit techniques for non-2-elementary discriminant forms.
This is the single structural obstruction distinguishing the nodal case from every other family in this program, including the Coble families of [the Coble families research program](../coble-moduli/coble-families-research-program.md), which are all 2-elementary.
:::

## Literature anchors recorded with the program

- Cossec (1985) computes the automorphism group at a generic point of $F_{\En,\mathrm{Nod}}$ by non-transcendental methods, showing it equals a normal subgroup of the Weyl group $W(T_{2,4,6})$ containing its 2-congruence subgroup, and that up to $\Aut(S)$ there is a unique smooth rational curve on such a surface.
  With Barth-Peters on the unnodal case this describes $\Aut$ at a generic point of $F_{\En}$.

- Ingalls et al. (2015) study semiorthogonal decompositions of $D^b(Y)$ for nodal Enriques surfaces.

- Martin (2024) shows every nodal Enriques surface, not merely a generic one, is a **Reye congruence**: with $F_i^{\pm}$ the multiple fibers of the ten elliptic pencils, the image of the Fano model defined by $|\tfrac13\sum F_i^+|$ lies on a quadric.

- Dolgachev-Kondo (2013) show $F_{\En,\mathrm{Nod}}$ is rational.

Related: [Coble families research program](../coble-moduli/coble-families-research-program.md), [Halphen index-2 moduli program](halphen-index-2-moduli-program.md).
