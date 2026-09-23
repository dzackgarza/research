---
title: The Coble cusp correspondence and the morphism chain to F_(2,2,0)
unit: research-program
status: conjectural
tags:
  - coble
  - cusps
  - baily-borel
  - morphisms
---

# The Coble cusp correspondence and the morphism chain

**Provenance.** `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/research-statements/canonical/my_research_statement/ResearchStatement.md` (author's own research statement, sections "Current Work" and "Compact moduli spaces of Coble surfaces") and `/home/dzack/gitclones/diss/000-writing/.archive/thesis-outline/part3/08_Future_Directions.md`. Neither source is in the finished dissertation, which mentions Coble surfaces only once in passing.

Statements below are the author's own claims of work in progress.
The archive marks the `08_Future_Directions.md` copy `audited: false` with `\todo` flags on the lattice identifications themselves.
Treat everything here as a claim to re-derive, not as a result.

## The chain of morphisms

::: {.Remark}
### The four-term chain

The claimed chain is
$$
\fco \too \fen \too \fent \longleftarrow F_{(2,2,0)} ,
$$
where $F_{(2,2,0)}$ is the moduli space of quartic hyperelliptic K3 surfaces used in AEGS. The purpose of the chain is to transport the KSBA/semitoroidal comparison proved for $\fentwo$ back to $\fco$.
:::

::: {.Construction}
### The embedding and its two extensions

An embedding $\fco \injects \fen$ into unpolarized Enriques moduli is claimed, together with two extensions to Baily-Borel compactifications:
$$
\eta: \bbcpt{\fco} \to \bbcpt{\fen},
\qquad
\tilde\eta: \bbcpt{\fco} \to \bbcpt{F_{(2,2,0)}} .
$$
The stratification of $\partial\bbcpt{\fco}$ is obtained by applying the *mirror moves* of AE22 to $S_{\Co} = (11,11,1)_1$.
The boundary correspondence induced by $\eta$ is claimed to be determined by the divisibility invariant.
:::

## The two cusp identifications

::: {.Conjecture}
### Coble cusps under the extension to F_(2,2,0)

Under $\tilde\eta$, the Coble cusps correspond to $U \oplus E_8^{\oplus 2}$, the lattice with invariants $(18,0,0)_1$.
:::

::: {.Conjecture}
### The Coble 0-cusp is Sterk cusp 2

The Coble 0-cusp corresponds to **cusp 2** of the Sterk cusp diagram of $\fentwo$.
The Sterk cusp diagram was first given by Sterk (1991).
:::

The second identification is not recorded in `content_pandoc/sections/Open_Problems/Open_Problems.md`, which states the cusp correspondence only in $(r,a,\delta)$ terms.
It is a directly checkable cross-project claim and should be reconciled with the $(9,9,1)$ / $(7,7,1)$ Coble cusp data recorded there.

::: {.Remark}
### A cheap consistency check on the whole correspondence

The dissertation proves that Sterk cusp 1 gives an $\RP^2$ integral-affine structure and that cusps 2 through 5 give $\DD^2$.
The author independently claims, from the divisibility computation, that **Coble degenerations are $\DD^2$-type rather than $\RP^2$-type**, which is the ingredient needed to build the correct dlt models.
Combined with the conjecture above, "Coble sits at Sterk cusp 2" *implies* $\DD^2$-type.
The two claims were derived by different routes, so their agreement is a real, and currently unexercised, consistency check on the entire cusp correspondence.
:::

## The lattice-theoretic method

::: {.Remark}
### Reduction to the discriminant group, and Eichler transformations

The stated method for the $\Gamma_{\Co}$-orbit classification, where $\Gamma_{\Co} \leq \Orth(T_{\Co})$ is the relevant subgroup and $D_{\Co}/\Gamma_{\Co}$ the relevant period domain:

1. Careful study of the discriminant groups $A_{T_{\Co}}$ and $A_{\ten}$.

2. Techniques reducing the classification of orbits of isotropic vectors in $T_{\Co}$ to finite computable problems in $A_{T_{\Co}}$.

3. **Explicit construction of Eichler transformations** proving that vectors with prescribed numerical invariants lie in one $\Gamma_{\Co}$-orbit.

This adapts Sterk's and Scattone's techniques to new lattices.
Eichler transvections are not named as a tool in the current `Open_Problems.md`, which cites Sterk lifting and $\Orth(q_{T_{\Co}})$-orbits instead.
:::

::: {.Remark}
### The GIT birational model

\fco \da D_{T_{\Co}}/\Orth(T_{\Co})$ is claimed birational to the GIT quotient $(\PP^2)^{10}\modmod\PGL_3$.
This gives an independent handle on the dimension 9 already asserted in the project, and an avenue for comparing GIT and KSBA compactifications.
:::

## Terminal Coble surfaces

::: {.Definition}
### Terminal

A Coble surface is **terminal** when it is not the image of any birational but not biregular morphism from another Coble surface.
The $n=1$ case, the blowup of a plane sextic at $N=10$ ordinary double points (some possibly infinitely near), is terminal.
:::

Related: [[coble-families-research-program]], [[coble-lattice-isotropic-candidates]], [[halphen-index-2-moduli-program]].
