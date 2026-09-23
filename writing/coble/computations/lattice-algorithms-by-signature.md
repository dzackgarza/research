---
title: Which lattice algorithms apply in which signature
unit: method
status: reusable
tags:
  - lattices
  - signature
  - subdiagrams
  - method
---

# Which lattice algorithms apply in which signature

**Provenance.** `notes/computations/coxeter-algorithms/`, seven survey documents landed 2026-08-20, and the decomposition search of `notes/computations/scripts/Isometry_Searching_LLM.md`.

Every lattice this project computes with is indefinite: the period lattices have signature $(2,n)$, and the cusp lattices $\eta^{\perp}/\eta$ are hyperbolic.
Most named lattice algorithms are stated for definite forms.
This page records where the two disagree, because that boundary is what leaves several of the entries in [[open-problems]] open.

## The definite and indefinite cases

::: {.Remark}
### Level sets

For a definite lattice $L$ and $c\in\ZZ$ the level set $\ts{v\in L : v^2 = c}$ is finite, and enumerating it is the basic primitive from which short-vector, closest-vector and automorphism computations are built.
For an indefinite lattice it can be infinite: in $U$ with $\beta_U(v,w) = x_1y_2+x_2y_1$ the isotropic vectors are $\ts{(x,0)}\union\ts{(0,y)}$, so the level set at $c = 0$ is infinite.
An algorithm whose output is a list of the vectors of a given square is therefore available only in the definite case, and its indefinite counterpart returns orbit representatives together with generators for the acting group ([[isotropic-orbits-and-tits-buildings]]).
:::

::: {.Remark}
### Theta series

The theta series $\Sum_{v\in L} q^{v^2}$ has, as the coefficient of $q^c$, the cardinality of the level set at $c$.
For definite $L$ every coefficient is finite and the series converges for $\lvert q\rvert < 1$.
For $U$ the coefficient of $q^0$ is already infinite, so the series is undefined, and any convergent replacement is a regularization.
:::

::: {.Remark}
### Automorphism groups

$\Orth(L)$ is finite for definite $L$, and is computed by its action on a level set.
For indefinite $L$ it is in general infinite and is presented by generators; the reflection subgroup $W(L)$ of \longref{def:reflection} is presented by the simple roots that Vinberg's algorithm returns, which is the one indefinite case this project computes in full.
:::

| Question | Definite $L$ | Indefinite $L$ |
| --- | --- | --- |
| Vectors of square $c$ | finite list | orbit representatives and group generators |
| Theta series | convergent | undefined without regularization |
| $\Orth(L)$ | finite, by level-set action | infinite, by generators |
| $W(L)$ | finite Weyl group | simple roots by Vinberg's algorithm |
| Isometry class | reduction and finite search | genus invariants and Nikulin's criteria [@Nik80] |
| Primitive embedding $L_1\injects L_2$ | finite search | genus criteria [@Nik80] |
| Finite covolume of $W(L)$ | vacuous | CoxIter certificate [@Gug15] |

::: {.Remark}
### Where this leaves the open problems

The entries of [[open-problems]] that ask for orbit counts, for explicit primitive-embedding matrices, and for generators of $\Gamma_\Co$ are all in the right-hand column.
None of them is a search that has not been run; each requires the genus-theoretic or reflection-group input that replaces the search.
:::

## Deciding the type of a subdiagram

::: {.Remark}
### The tests are exact integer computations

\longref{def:coxeter-system-type} classifies a subdiagram $\Sigma_I$ by the signature of the Gram form $G[I,I]$: elliptic when it is negative definite, parabolic when it is negative semidefinite with a one-dimensional kernel on each component, hyperbolic when it is nondegenerate of signature $(1,\lvert I\rvert - 1)$.
For a subdiagram of a diagram of an integral lattice, $G[I,I]$ is an integer matrix, so each of the three conditions is a definiteness test decided exactly, by the leading principal minors or by an exact symmetric decomposition, with no eigenvalue approximation.
:::

::: {.Remark}
### Consequence for the enumeration

\longref{cor:subdiagram-inheritance}(1) prunes the search over the $2^{\lvert S\rvert}$ subsets in step 5 of [[computational-toolchain-and-recipe]]: once a subset fails to be elliptic, every superset of it is excluded without a further definiteness test.
The elliptic subdiagrams form a downward-closed family in the subset poset, whose maximal elements are the maximal elliptic subdiagrams the recipe asks for.
The elliptic subdiagram counts $121, 65, 67, 78, 119$ for the five Sterk cusps in [[coxiter-results-for-cusp-lattices]] are the cardinalities of those families before the diagram automorphism group is quotiented out.
:::

## Recognizing a lattice as a sum of standard blocks

::: {.Construction #cons:decomposition-search}
### Search over signature-additive multisets

Signature is additive over orthogonal direct sums, so a decomposition $L\cong\bigoplus_i L_i$ satisfies $\Sum_i (p_i,q_i) = (p,q)$ where $(p,q)$ is the signature of $L$.
Fixing a catalogue $\mathcal B$ of standard blocks, a decomposition of $L$ within $\mathcal B$ is found by

1. grouping $\mathcal B$ by signature;

2. enumerating the multisets of signatures from that grouping whose sum is $(p,q)$;

3. forming the direct sum of each choice of blocks realizing such a multiset;

4. testing each sum for isometry with $L$.

The catalogue used here is $A_n$, $D_n$ and $E_n$ up to rank $20$, the odd and even unimodular lattices $I_{p,q}$ and $II_{p,q}$, and the $2$-twists of all of these.
The even unimodular lattices are indexed by the signatures with $p\equiv q \bmod 8$.
:::

::: {.Remark}
### The step the search defers to

Step 4 is an isometry test between indefinite lattices, which is the entry in the right-hand column of the table above.
The search reduces recognition to that test and does not replace it; in a Sage session the route through `genus().representatives()` calls out to Magma, so it is unavailable where Magma is not installed, and the genus-symbol comparison of [[discriminant-forms-and-genus]] is the available substitute for a two-elementary lattice.
:::

Related: [[computational-toolchain-and-recipe]], [[isotropic-orbits-and-tits-buildings]], [[coxiter-results-for-cusp-lattices]], [[open-problems]].
