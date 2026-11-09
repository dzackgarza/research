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
notes: |-
  Provenance: the Dawes-2022 orbit-algorithm research notes for the algorithms and examples of [@Daw22], and the Enriques-moduli computation notes for those of [@SH23].
---

# Orbits of isotropic vectors and the Tits building of a cusp configuration {#sec-isotropic-orbits-and-tits-buildings}


The enumeration of $\Orth(T)$- and $\Gamma$-orbits of primitive isotropic vectors in $T_\Co$ is left open in [open problems](#sec-open-problems), where it blocks the uniqueness of the Baily--Borel $0$-cusp.
Two published algorithm families answer that question for indefinite lattices; this page states what each computes and under which hypotheses.

## Why the orbit count is the cusp count

::: {.remark title="The correspondence and the invariants that separate orbits"}

[The Scattone cusp method](#sec-scattone-cusp-method) records the correspondence and its separating invariants: for $T$ of signature $(2,n)$ and an arithmetic $\Gamma\leq\Orth(T)$, the $0$-cusps of the Baily--Borel compactification are the $\Gamma$-orbits of primitive isotropic lines of $T$ and the $1$-cusps are the $\Gamma$-orbits of primitive isotropic planes, and the pair $\bigl(\div_T(v), [v^*]\bigr)$ of @prop:coble-divisibility-discriminant separates those orbits under the hypotheses of @thm:eichler-criterion and @thm:sterk-orbit.
:::

::: {.remark title="The building of a lattice of signature $(2,n)$"}

For $T$ of signature $(2,n)$ a totally isotropic subspace has dimension at most $2$, so the Tits building of $\Orth(T)$ has rank $2$: its vertices are the isotropic lines and the isotropic planes, its edges are the containments $I\subset J$, and it is a bipartite graph.
The $\Gamma$-quotient is the incidence graph of the boundary of $\bbcpt{F}$, the $1$-cusps adjacent to a $0$-cusp $[I]$ being the isotropic planes containing $I$; these are the maximal parabolic subdiagrams of the Coxeter--Vinberg diagram at $[I]$ (@def:parabolic-subdiagram), equivalently the ideal vertices of the chamber there (@cor:ideal-vertices-are-parabolic).
Counting the cusps and computing the building are one computation at two levels of detail.
:::

::: {.remark title="The complement of a vector and what its computation produces"}

For a primitive $v$ in a nondegenerate lattice $L$ of rank $n$ with Gram matrix $G$, the pairing $\beta_L(v,-)\colon L\to\ZZ$ has matrix the row $v^{\mathsf T}G$.
Its invariant factor decomposition produces two things: the single invariant factor of that map, which is $\div_L(v)$, so that the image is $\div_L(v)\ZZ$; and an explicit basis of the kernel $v^{\perp L}$, a free module of rank $n-1$, whose Gram matrix is the restricted form.
The Smith normal form of $v^{\mathsf T}G$ is the standard means of producing both.
Every algorithm below descends through this step, and the invariants it compares are read off the result.
:::

## Deciding orbit equivalence of two vectors

::: {.proposition #prop:orbit-necessary-conditions title="Conditions necessary for equivalence"}

Let $L$ be a nondegenerate lattice, $\Gamma\leq\Orth(L)$, and $v_1, v_2\in L$ primitive with $\phi(v_1) = v_2$ for some $\phi\in\Gamma$.
Then

1. $v_1^2 = v_2^2$;

2. $\div_L(v_1) = \div_L(v_2)$, and the isometry induced by $\phi$ on $A_L$ carries $[v_1^*]$ to $[v_2^*]$;

3. $\phi$ restricts to an isometry $v_1^{\perp L}\to v_2^{\perp L}$, so the two complements are isometric and in particular have equal discriminants.

Each holds a fortiori for any subgroup of $\Orth(L)$, so a failure of any one of them refutes equivalence under every group considered here.
:::

::: {.proof}

All three are invariance under an isometry, and none needs $v_i$ isotropic.

(1) $\phi$ preserves the form, so $v_2^2=\phi(v_1)^2=v_1^2$.

(2) $\phi$ induces an isomorphism of the dual lattices, so $\beta_{L}(\phi v_1,\phi x)=\beta_L(v_1,x)$ shows that the divisibility ideals of @def:lattice-divisibility agree, hence $\div_L(v_1)=\div_L(v_2)$ as positive generators of the same ideal.
For the classes: $\phi$ carries $v_1/\div_L(v_1)$ to $v_2/\div_L(v_2)$ because it is linear and preserves the divisibility, and it passes to the quotient $A_L=L^\#/L$ because it maps $L$ to $L$; so the induced automorphism of $A_L$ sends $[v_1^*]$ to $[v_2^*]$ by @def:lattice-discriminant-class.

(3) $\phi(v_1)=v_2$ gives $\phi(v_1^{\perp L})=v_2^{\perp L}$: if $x\perp v_1$ then $\beta(\phi x,v_2)=\beta(x,v_1)=0$, and conversely by applying $\phi^{-1}$.
The restriction is an isometry onto, hence an isometry of lattices, so the complements are isometric and by @def:discriminant they have the same discriminant form.

The last sentence is the practical content: each condition is a necessary condition on any orbit, so a pair failing one is separated by every subgroup of $\Orth(L)$ at once, and the computations of this page use that to discard candidates without knowing the group.

The necessary conditions on an isotropic orbit are the invariants of `prop:coble-divisibility-discriminant` together with the building-theoretic restriction that an isotropic vector lies in a chamber of the Tits building determined by its class.
:::

::: {.lemma #lem:complement-determinant title="The determinant of a complement is fixed by the square and the divisibility"}

Let $L$ be a nondegenerate integral lattice and $v\in L$ primitive with $q(v)\neq0$.
Then
$$
\abs{\det\bigl(v^{\perp L}\bigr)}
=
\abs{\det L}\cdot\frac{\abs{q(v)}}{\div_L(v)^{2}}
.
$$
:::

::: {.proof}

The map $\varphi\colon L\to\ZZ$, $x\mapsto\beta(x,v)$, has image $\div_L(v)\ZZ$ and kernel $v^{\perp L}$, and it carries $\ZZ v$ onto $q(v)\ZZ$; so
$$
L\big/\bigl(\ZZ v+v^{\perp L}\bigr) \;\iso\; \div_L(v)\ZZ\big/ q(v)\ZZ
,\qquad
\bigl[L:\ZZ v+v^{\perp L}\bigr] = \frac{\abs{q(v)}}{\div_L(v)}
,$$
the quotient on the right being finite of that order because $q(v)\in\div_L(v)\ZZ$.
On the other hand $\det(\ZZ v\oplus v^{\perp L}) = q(v)\cdot\det(v^{\perp L})$ and $\det(\ZZ v\oplus v^{\perp L}) = [L:\ZZ v+v^{\perp L}]^{2}\cdot\det L$; substituting the index gives the formula.
:::

Two primitive vectors of one lattice with the same square and the same divisibility therefore have complements of equal determinant, and condition (3) of @prop:orbit-necessary-conditions cannot be violated through the determinant alone: a difference between two complements, if there is one, is finer than its discriminant.

::: {.remark title="The definite case"}

Algorithm 2.1 of [@Daw22] decides $\Gamma$-equivalence of $v_1, v_2$ with $v_1^2 = v_2^2 \neq 0$ under the hypothesis that $v_1^{\perp L}$ is definite.
That hypothesis is what makes the decision terminate: the isometry group of a definite lattice is finite, so the isometries $v_1^{\perp L}\to v_2^{\perp L}$ form a finite set which can be enumerated, and each is tested for extension to an element of $\Gamma$ compatible with $v_1\mapsto v_2$.
The complement and its form come from the invariant factor decomposition above.
:::

::: {.remark title="The indefinite case"}

Algorithm 2.3 of [@Daw22] treats $v_1^{\perp L}$ indefinite, where the isometry group is infinite and the enumeration of the definite case is unavailable.
The decision is made on the discriminant form instead, under the hypothesis that
$$
\Orth(L)\too\Orth(q_L)
$$
is surjective.
For an even indefinite $2$-elementary lattice this surjectivity holds with no further hypothesis (@thm:two-elementary-surjectivity), so it is available for $T_\Co$, and it is the hypothesis under which [open problems](#sec-open-problems) reduces the $\Orth(T_\Co)$-orbit problem to $A_{T_\Co}$.
Without it the discriminant data does not determine the orbit, and the algorithm decides nothing.
:::

::: {.example #ex:dawes-u-a3 title="Two specimens in $U\oplus A_3$"}

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
The paper's conclusion is $v_1\sim v_2$ under the group it denotes $\wh{S\Orth}^+(L)$.
:::

::: {.question #qst:dawes-example-22 title="The orbit of the first specimen"}

For Example 2.2 of @ex:dawes-u-a3, both vectors are primitive, with $q(v) = 20$ and $\div_L(v) = 4$, so by @lem:complement-determinant both complements $v_1^{\perp L}$ and $v_2^{\perp L}$ have determinant $4\cdot 20/4^{2} = 5$.
`computations/reports/coble_dawes-example-2-2_complements.py` computes both complements: each is rank $4$, negative definite, of determinant $5$, with $20$ roots of type $A_4$, and a rank-$4$ lattice whose roots are of type $A_4$ and whose determinant equals $\det A_4$ *is* the root lattice $A_4$, so the two complements are isometric.
The same script computes the class of $v/\div(v)$ in $A_L$, which carries $q = 5/4$ for both vectors.
So every invariant of @prop:orbit-necessary-conditions agrees on the pair: equal squares, equal divisibilities, isometric complements, and equal classes in $A_L$.

Deciding the conclusion $v_1\sim v_2$ of [@Daw22] needs an explicit isometry carrying $v_1$ to $v_2$, equivalently the decision of the orbit of a primitive vector of square $20$ in $L$.
:::

::: {.remark title="Buildings by descent along a subgroup"}

[@Daw22] also computes the building $B(G_1)$ of a subgroup $G_1\subset G_2$ from $B(G_2)$, and specializes this to split maximal lattices of signature $(2,n)$, where the building is described directly by its isotropic lines and planes.
Descent along a subgroup is the shape the Coble problem takes: $\Gamma_\Co$ is cut out of $\Orth(\ten)$ as a stabilizer intersected with a centralizer (@sec-open-problems), so its building is a refinement of one already computed for a larger group.
The paper's stated applications are the configuration of boundary components of orthogonal modular varieties and the arithmetic of orthogonal modular forms, where a Fourier expansion consumes orbit *representatives* and a multiplication is organized by them.
:::

## The polarized Enriques computation and its lattice

::: {.remark title="Three algorithms for indefinite forms"}

[@SH23] carries out the corresponding computation for moduli of polarized Enriques surfaces, using three algorithms for indefinite quadratic forms:

1. representatives for the intersection $G_1\intersect G_2$ of two subgroups of $\GL_n(\ZZ)$;

2. representatives for the orbits of vectors $v$ with $Q(v) = c$ for a fixed indefinite $Q$ and a fixed value $c$, the isotropic case being $c = 0$;

3. a criterion deciding whether a given $g\in\Orth(L)$ is an Eichler transvection, that is, one of the generators of the group $E(L)$ of @thm:eichler-transvection.

The results reported there are that the arithmetic groups arising from polarized Enriques moduli fall into exactly $87$ conjugacy classes, that every such moduli space is dominated by the one of polarization degree $1240$, and that the Tits buildings of those groups are computed.
:::

::: {.observation #obs:enriques-orbit-lattice-is-tdp title="The lattice of that computation is $\tdp$"}

The target lattice is written $U\oplus 2U\oplus 2E_8(-1)$, a shorthand in which the prefix $2$ has two different meanings; its rank $20$ and signature $(2,18)$ are unambiguous.
Those invariants force the reading
$$
M \;=\; U\oplus U(2)\oplus E_8^{\oplus 2},
$$
with $E_8$ negative definite, since no other assignment of the shorthand to scalings and multiplicities of $U$ and $E_8$ has rank $20$.
This is the lattice $L_{20,2,0} = \tdp$ of two-elementary type $(20,2,0)$ in which the root configuration $\Phi_{(18,2,0)}$ and the folded Sterk diagrams are written ([root vectors and folded Sterk diagrams](#sec-root-vectors-and-folded-sterk-diagrams)), and in which the embedding chain $T_\Co\injects \ten\injects \tdp$ terminates ([Coble lattice isotropic candidates](#sec-coble-lattice-isotropic-candidates)). The isotropic-orbit algorithms are therefore already stated for the ambient lattice of this project, and the residue is their transport along that chain.
:::

::: {.remark title="The implementation named in the recipe"}

Step 6 of [the computational toolchain and recipe](#sec-computational-toolchain-and-recipe) computes orbit representatives with the function `vector_orbit_representatives` of `sage-indefinite-port`. That is the second algorithm above; the recipe recognizes the representatives it returns by the separating invariants $\div(v)$ and $v^{\perp}/v$, matched against the table of $2$-elementary lattices keyed by $(r,a,\delta)$.
:::

## What remains for the Coble lattices

::: {.remark title="The residue"}

The algorithms above decide orbit equivalence for a fixed indefinite form and a fixed group.
For $T_\Co = \generators{2}\oplus E_{10}(2)$ the remaining inputs are the group and the lift: the orbits are wanted for $\Orth(T_\Co)$, for $\discriminantkernel{T_\Co}$ and for $\Gamma_\Co$, which differ, and the reduction to $A_{T_\Co}\cong(\ZZ/2\ZZ)^{11}$ requires the surjectivity hypothesis above together with the lifting statement of @thm:sterk-orbit.
Every primitive isotropic vector of $T_\Co$ has $\div_{T_\Co}(v) = 2$ (@lem:divisibilityAlwaysTwoTco), so the divisibility half of condition (2) of @prop:orbit-necessary-conditions separates nothing there, and the class $[v^*]\in A_{T_\Co}$ is the whole of that invariant.
The candidate isotropic vectors of $T_\Co$ and the three-way transport of each along $T_\Co\injects \ten\injects \tdp$ are recorded in [Coble lattice isotropic candidates](#sec-coble-lattice-isotropic-candidates); running the orbit solver on them is the step that would replace the vector-by-vector table with a count.
:::

Related: [Scattone cusp method](#sec-scattone-cusp-method), [Coble lattice isotropic candidates](#sec-coble-lattice-isotropic-candidates), [computational toolchain and recipe](#sec-computational-toolchain-and-recipe), [cusp-correspondence morphism chain](#sec-cusp-correspondence-morphism-chain), [open problems](#sec-open-problems).
