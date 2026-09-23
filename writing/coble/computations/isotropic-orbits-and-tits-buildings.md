---
title: Orbits of isotropic vectors and the Tits building of a cusp configuration
unit: method
status: reusable
tags:
  - isotropic-orbits
  - cusps
  - baily-borel
  - tits-buildings
  - method
---

# Orbits of isotropic vectors and the Tits building of a cusp configuration

**Provenance.** `notes/papers/dawes-2022-orbits-in-lattices/research-notes.md` for the algorithms and examples of [@Daw22], and `notes/computations/enriques-moduli/` for those of [@SH23].

The enumeration of $\Orth(T)$- and $\Gamma$-orbits of primitive isotropic vectors in $T_\Co$ is left open in [open problems](../open-problems/open-problems.md), where it blocks the uniqueness of the Baily--Borel $0$-cusp.
Two published algorithm families answer that question for indefinite lattices; this page states what each computes and under which hypotheses.

## Why the orbit count is the cusp count

::: {.Remark}
### The correspondence and the invariants that separate orbits

[The Scattone cusp method](../compactifications/scattone-cusp-method.md) records the correspondence and its separating invariants: for $T$ of signature $(2,n)$ and an arithmetic $\Gamma\leq\Orth(T)$, the $0$-cusps of the Baily--Borel compactification are the $\Gamma$-orbits of primitive isotropic lines of $T$ and the $1$-cusps are the $\Gamma$-orbits of primitive isotropic planes, and the pair $\bigl(\div_T(v), [v^*]\bigr)$ of \longref{prop:divisibility-discriminant} separates those orbits under the hypotheses of \longref{thm:eichler-criterion} and \longref{thm:sterk-orbit}.
:::

::: {.Remark}
### The building of a lattice of signature $(2,n)$

For $T$ of signature $(2,n)$ a totally isotropic subspace has dimension at most $2$, so the Tits building of $\Orth(T)$ has rank $2$: its vertices are the isotropic lines and the isotropic planes, its edges are the containments $I\subset J$, and it is a bipartite graph.
The $\Gamma$-quotient is the incidence graph of the boundary of $\bbcpt{F}$, the $1$-cusps adjacent to a $0$-cusp $[I]$ being the isotropic planes containing $I$; these are the maximal parabolic subdiagrams of the Coxeter--Vinberg diagram at $[I]$ (\longref{def:parabolic-subdiagram}), equivalently the ideal vertices of the chamber there (\longref{cor:ideal-vertices-are-parabolic}).
Counting the cusps and computing the building are one computation at two levels of detail.
:::

::: {.Remark}
### The complement of a vector and what its computation produces

For a primitive $v$ in a nondegenerate lattice $L$ of rank $n$ with Gram matrix $G$, the pairing $\beta_L(v,-)\colon L\to\ZZ$ has matrix the row $v^{\mathsf T}G$.
Its invariant factor decomposition produces two things: the single invariant factor of that map, which is $\div_L(v)$, so that the image is $\div_L(v)\ZZ$; and an explicit basis of the kernel $v^{\perp L}$, a free module of rank $n-1$, whose Gram matrix is the restricted form.
The Smith normal form of $v^{\mathsf T}G$ is the standard means of producing both.
Every algorithm below descends through this step, and the invariants it compares are read off the result.
:::

## Deciding orbit equivalence of two vectors

::: {.Proposition #prop:orbit-necessary-conditions}
### Conditions necessary for equivalence

Let $L$ be a nondegenerate lattice, $\Gamma\leq\Orth(L)$, and $v_1, v_2\in L$ primitive with $\phi(v_1) = v_2$ for some $\phi\in\Gamma$.
Then

1. $v_1^2 = v_2^2$;

2. $\div_L(v_1) = \div_L(v_2)$, and the isometry induced by $\phi$ on $A_L$ carries $[v_1^*]$ to $[v_2^*]$;

3. $\phi$ restricts to an isometry $v_1^{\perp L}\to v_2^{\perp L}$, so the two complements are isometric and in particular have equal discriminants.

Each holds a fortiori for any subgroup of $\Orth(L)$, so a failure of any one of them refutes equivalence under every group considered here.
:::

::: {.Remark}
### The definite case

Algorithm 2.1 of [@Daw22] decides $\Gamma$-equivalence of $v_1, v_2$ with $v_1^2 = v_2^2 \neq 0$ under the hypothesis that $v_1^{\perp L}$ is definite.
That hypothesis is what makes the decision terminate: the isometry group of a definite lattice is finite, so the isometries $v_1^{\perp L}\to v_2^{\perp L}$ form a finite set which can be enumerated, and each is tested for extension to an element of $\Gamma$ compatible with $v_1\mapsto v_2$.
The complement and its form come from the invariant factor decomposition above.
:::

::: {.Remark}
### The indefinite case

Algorithm 2.3 of [@Daw22] treats $v_1^{\perp L}$ indefinite, where the isometry group is infinite and the enumeration of the definite case is unavailable.
The decision is made on the discriminant form instead, under the hypothesis that
$$
\Orth(L)\too\Orth(q_L)
$$
is surjective.
This is the same surjectivity that Nikulin's criteria supply for a $2$-elementary lattice with $r > a$ [@Nik80], and it is the hypothesis under which [open problems](../open-problems/open-problems.md) reduces the $T_\Co$ orbit problem to $A_{T_\Co}$.
Without it the discriminant data does not determine the orbit, and the algorithm decides nothing.
:::

::: {.Example #ex:dawes-u-a3}
### Two specimens in $U\oplus A_3$

Both specimens are stated in $L = U\oplus A_3$ with the Gram matrices
$$
G_U = \begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
G_{A_3} = \begin{pmatrix}-2&-1&0\\-1&-2&-1\\0&-1&-2\end{pmatrix},
$$
the coordinates below being taken in that basis.

For Example 2.2 of [@Daw22], $v_1 = (4,4,1,2,-1)$ and $v_2 = (36,144,5,-30,83)$, and both have $v^2 = 20$: the $U$-part contributes $32$ and $10368$, the $A_3$-part $-12$ and $-10348$.
The paper's conclusion is $v_1\sim v_2$ under the group it denotes $\wh{\Orth}^+(L)$.

For Example 2.6, $v_1 = (1,-1,0,0,0)$ and $v_2 = (1,0,1,0,0)$, and both have $v^2 = -2$.
The paper's conclusion is $v_1\sim v_2$ under the group it denotes $\wh{S\Orth}^+(L)$, and the in-tree computation reproduces it.
:::

::: {.Question #qst:dawes-example-22}
### An unreconciled outcome on the first specimen

Run on Example 2.2 of \longref{ex:dawes-u-a3}, the in-tree computation returns $v_1\not\sim v_2$, on the ground that $v_1^{\perp L}$ and $v_2^{\perp L}$ have different discriminants.
The record attributes the disagreement to a simplified isometry test, but a discriminant is an isometry invariant, so by \longref{prop:orbit-necessary-conditions}(3) unequal discriminants refute equivalence under $\Orth(L)$ and under every subgroup of it, whatever isometry test is used downstream.
The disagreement therefore lies in one of three places: the conclusion of [@Daw22], the transcription of the vectors or of the Gram matrix, or the computed complements.
The squares recorded in \longref{ex:dawes-u-a3} are consistent with the stated Gram matrices, which settles the transcription of the vectors; recomputing the two complements and their discriminants settles the rest.
:::

::: {.Remark}
### Buildings by descent along a subgroup

[@Daw22] also computes the building $B(G_1)$ of a subgroup $G_1\subset G_2$ from $B(G_2)$, and specializes this to split maximal lattices of signature $(2,n)$, where the building is described directly by its isotropic lines and planes.
Descent along a subgroup is the shape the Coble problem takes: $\Gamma_\Co$ is cut out of $\Orth(T_\En)$ as a stabilizer intersected with a centralizer ([open problems](../open-problems/open-problems.md)), so its building is a refinement of one already computed for a larger group.
The paper's stated applications are the configuration of boundary components of orthogonal modular varieties and the arithmetic of orthogonal modular forms, where a Fourier expansion consumes orbit *representatives* and a multiplication is organized by them.
:::

## The polarized Enriques computation and its lattice

::: {.Remark}
### Three algorithms for indefinite forms

[@SH23] carries out the corresponding computation for moduli of polarized Enriques surfaces, using three algorithms for indefinite quadratic forms:

1. representatives for the intersection $G_1\intersect G_2$ of two subgroups of $\GL_n(\ZZ)$;

2. representatives for the orbits of vectors $v$ with $Q(v) = c$ for a fixed indefinite $Q$ and a fixed value $c$, the isotropic case being $c = 0$;

3. a criterion deciding whether a given $g\in\Orth(L)$ is an Eichler transvection, that is, one of the generators of the group $E(L)$ of \longref{thm:eichler-transvection}.

The results reported there are that the arithmetic groups arising from polarized Enriques moduli fall into exactly $87$ conjugacy classes, that every such moduli space is dominated by the one of polarization degree $1240$, and that the Tits buildings of those groups are computed.
:::

::: {.Observation #obs:enriques-orbit-lattice-is-tdp}
### The lattice of that computation is $\tdp$

The specification records the target lattice by the shorthand $U\oplus 2U\oplus 2E_8(-1)$, in which the prefix $2$ has two different meanings, and by two unambiguous invariants: rank $20$ and signature $(2,18)$.
Those invariants force the reading
$$
M \;=\; U\oplus U(2)\oplus E_8^{\oplus 2},
$$
with $E_8$ negative definite, since no other assignment of the shorthand to scalings and multiplicities of $U$ and $E_8$ has rank $20$.
This is the lattice $L_{20,2,0} = \tdp$ of two-elementary type $(20,2,0)$ in which the root configuration $\Phi_{(18,2,0)}$ and the folded Sterk diagrams are written ([root vectors and folded Sterk diagrams](root-vectors-and-folded-sterk-diagrams.md)), and in which the embedding chain $T_\Co\injects \ten\injects \tdp$ terminates ([Coble lattice isotropic candidates](coble-lattice-isotropic-candidates.md)).
The isotropic-orbit algorithms are therefore already stated for the ambient lattice of this project, and the residue is their transport along that chain.
:::

::: {.Remark}
### Scope of the exercised cases

The orbit algorithm was exercised on the family $U\oplus U(2)\oplus X$ with $X$ successively $0$, $A_2$, $A_3$, $A_2^{\oplus 2}$ and $E_8^{\oplus 2}$, and on $U^{\oplus 2}\oplus E_7$, at target norm $0$; the last of the first family is $M$ itself.
The resulting orbit counts are not part of the record.
:::

::: {.Remark}
### The implementation named in the recipe

Step 6 of the recipe in [the computational toolchain and recipe](computational-toolchain-and-recipe.md) invokes `INDEF_FORM_GetOrbitRepresentative` from the C++ library `polyhedral_common` of the same authors, through GAP.
That is the second algorithm above, and the separating invariants the recipe pairs with it, $\div(v)$ and $v^{\perp}/v$ matched against the two-elementary registry, are the invariants under which the orbit representatives it returns are recognized.
:::

## What remains for the Coble lattices

::: {.Remark}
### The residue

The algorithms above decide orbit equivalence for a fixed indefinite form and a fixed group.
For $T_\Co = \gens{2}\oplus E_{10}(2)$ the remaining inputs are the group and the lift: the orbits are wanted for $\Orth(T_\Co)$, for $\OStab(T_\Co)$ and for $\Gamma_\Co$, which differ, and the reduction to $A_{T_\Co}\cong(\ZZ/2\ZZ)^{11}$ requires the surjectivity hypothesis above together with the lifting statement of \longref{thm:sterk-orbit}.
Every primitive isotropic vector of $T_\Co$ has $\div_{T_\Co}(v) = 2$ (\longref{lem:divisibilityAlwaysTwoTco}), so the divisibility half of condition (2) of \longref{prop:orbit-necessary-conditions} separates nothing there, and the class $[v^*]\in A_{T_\Co}$ is the whole of that invariant.
The candidate isotropic vectors of $T_\Co$ and the three-way transport of each along $T_\Co\injects \ten\injects \tdp$ are recorded in [Coble lattice isotropic candidates](coble-lattice-isotropic-candidates.md); running the orbit solver on them is the step that would replace the vector-by-vector table with a count.
:::

Related: [Scattone cusp method](../compactifications/scattone-cusp-method.md), [Coble lattice isotropic candidates](coble-lattice-isotropic-candidates.md), [computational toolchain and recipe](computational-toolchain-and-recipe.md), [cusp-correspondence morphism chain](../coble-moduli/cusp-correspondence-morphism-chain.md), [open problems](../open-problems/open-problems.md).
