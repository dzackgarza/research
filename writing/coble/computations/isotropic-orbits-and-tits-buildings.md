ter---
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
The paper's conclusion is $v_1\sim v_2$ under the group it denotes $\wh{S\Orth}^+(L)$, and the in-tree computation reproduces it.
:::

::: {.question #qst:dawes-example-22 title="The outcome on the first specimen, reconciled"}

Run on Example 2.2 of @ex:dawes-u-a3, the in-tree computation returns $v_1\not\sim v_2$, on the ground that $v_1^{\perp L}$ and $v_2^{\perp L}$ have different discriminants.
The record attributes the disagreement to a simplified isometry test, but a discriminant is an isometry invariant, so by @prop:orbit-necessary-conditions(3) unequal discriminants refute equivalence under $\Orth(L)$ and under every subgroup of it, whatever isometry test is used downstream.
The disagreement therefore lies in one of three places: the conclusion of [@Daw22], the transcription of the vectors or of the Gram matrix, or the computed complements.
The squares recorded in @ex:dawes-u-a3 are consistent with the stated Gram matrices, which settles the transcription of the vectors; recomputing the two complements and their discriminants settles the rest.

*The recorded ground is impossible, and the complements are isometric.*
Both vectors are primitive, with $q(v) = 20$ and $\div_L(v) = 4$, so by @lem:complement-determinant both complements have determinant $4\cdot 20/4^{2} = 5$: unequal discriminants are not something a correct computation could have found.
The recomputation in `computations/reports/coble_dawes-example-2-2_complements.py` finds more than equal determinants: both complements are rank $4$, negative definite, of determinant $5$, with $20$ roots of type $A_4$, and a rank-$4$ lattice whose roots are of type $A_4$ and whose determinant equals $\det A_4$ *is* the root lattice $A_4$, so the two complements are isometric.
Every invariant of @prop:orbit-necessary-conditions therefore agrees on the pair: equal squares, equal divisibilities, isometric complements, and — the last one, which the same record computes — the same class of $v/\div(v)$ in $A_L$, carrying $q = 5/4$ for both.

*What settles it, and how.*
The in-tree run is not evidence against the paper's conclusion: the invariant it named is false for this pair, and the complements it would have had to compute are isometric, so the recorded refutation is withdrawn.
The conclusion itself is then decided in the paper's favour, by the gluing rather than by an exhibited matrix.
For a primitive $v$ with $v^2\neq0$ the lattice $L$ is an overlattice of $\generators{v}\oplus N$ with $N = v^{\perp L}/v$, the overlattice being determined by the isotropic subgroup $\Lambda\leq A_{\generators{v}}\oplus A_N$ that it cuts out; isomorphisms of the pair $(L,v)$ carry $\Lambda$ to $\Lambda$ up to $\Orth(\generators{v})\times\Orth(N)$, so the $\Orth(L)$-orbit of $v$ *is* the class of $\Lambda$.
Here $\generators{v}$ has $v^2 = 20$ and $N = A_4$, so $\Lambda$ is an order-$5$ subgroup of $\ZZ/20\oplus\ZZ/5$, classified by a line of $\PP^1(\bF_5)$.
Two of the three classes are impossible: a "pure $N$" class would produce an element $bv+m$ with $m$ of order $5$ and $m^2\notin\ZZ$, $q$ on the nonzero classes of $A_{A_4}$ taking the values $4/5$ and $6/5$; and a "pure $\generators{v}$" class would produce $x$ with $5x = av$, $a\not\equiv0\pmod 5$, hence $b(x,L) = \frac{a}{5}\cdot4\ZZ\not\subseteq\ZZ$ against $\div_L(v) = 4$.
The remaining class is a diagonal line of $\PP^1(\bF_5)$, and the four diagonal lines form a single orbit under $\Orth(\generators{v})\times\Orth(A_4) = \set{\pm1}\times\set{\pm1}$, which acts by $(a,b)\mapsto(\pm a,\pm b)$.
So there is exactly one class of pair $(L,v)$ with $v^2 = 20$, $\div_L(v) = 4$ and $v^{\perp L}/v\cong A_4$, and $v_1\sim v_2$ under $\Orth(L)$: the paper's claim stands, and the sufficiency that an explicit matrix would have supplied is supplied by the count of gluing classes.
The computation is `computations/reports/coble_dawes-example-2-2_gluing-class.py` with its run, which prints the two complements, an isometry $N_1\iso N_2$ from the owner, the values of $q$ on $A_{A_4}$ and the two divisibilities.
What it does not print is a matrix for $g\in\Orth(L)$ with $g(v_1) = v_2$: exhibiting one is the job of `primitive_marking_classes` for the pointed shape in `sage_indefinite_port` together with `isometry` of marked lattices, which is not driven here and is recorded as the outstanding step rather than replaced by a search written for the occasion.

*The two complements, printed.* In $L = U\oplus A_3$ the complement of a primitive $v$ has rank $4$ (not $3$: $L$ has rank $5$), and its Gram matrix in a $\ZZ$-basis of $v^{\perp L}$ is, for $v_1$ and $v_2$ as in @ex:dawes-u-a3,
$$
G_1 = \begin{pmatrix} -2&-1&1&-1\\ -1&-2&1&-1\\ 1&1&-2&1\\ -1&-1&1&-2\end{pmatrix},
\qquad
G_2 = \begin{pmatrix} -182&-192&-445&-590\\ -192&-206&-476&-631\\ -445&-476&-1102&-1459\\ -590&-631&-1459&-1934\end{pmatrix},
$$
with $\det G_1 = \det G_2 = 5$, $20$ roots of type $A_4$ in each, and both negative definite of signature $(0,4)$; a rank-$4$ lattice whose roots are of type $A_4$ and whose determinant equals $\det A_4 = 5$ *is* the $A_4$ root lattice, so $v_1^{\perp L}\iso v_2^{\perp L}\iso -A_4$.
*The transcription.* $v_1 = (4,4,1,2,-1)$ and $v_2 = (36,144,5,-30,83)$ in the basis of @ex:dawes-u-a3 satisfy $v_i^2 = 20$ with the $U$-part contributing $2a b$ and the $A_3$-part the stated quadratic form, which is the paper's own data; the coordinates are primitive in both cases and the divisibility is $4$. So the transcription is consistent with the paper's Gram matrices and squares, and neither the transcription nor the paper's conclusion is the faulty step.
*Which step is wrong, and the corrected statement.* The computed complements are the faulty step: the recorded ground for $v_1\not\sim v_2$ — that the complements have different discriminants — is impossible by @lem:complement-determinant, and the complements it names are in fact isometric. The corrected statement is that of @qst:dawes-example-22 above: the in-tree refutation is withdrawn, and the paper's conclusion $v_1\sim v_2$ holds, by the single admissible gluing class and not by a matrix exhibited here.

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

The specification records the target lattice by the shorthand $U\oplus 2U\oplus 2E_8(-1)$, in which the prefix $2$ has two different meanings, and by two unambiguous invariants: rank $20$ and signature $(2,18)$.
Those invariants force the reading
$$
M \;=\; U\oplus U(2)\oplus E_8^{\oplus 2},
$$
with $E_8$ negative definite, since no other assignment of the shorthand to scalings and multiplicities of $U$ and $E_8$ has rank $20$.
This is the lattice $L_{20,2,0} = \tdp$ of two-elementary type $(20,2,0)$ in which the root configuration $\Phi_{(18,2,0)}$ and the folded Sterk diagrams are written ([root vectors and folded Sterk diagrams](#sec-root-vectors-and-folded-sterk-diagrams)), and in which the embedding chain $T_\Co\injects \ten\injects \tdp$ terminates ([Coble lattice isotropic candidates](#sec-coble-lattice-isotropic-candidates)). The isotropic-orbit algorithms are therefore already stated for the ambient lattice of this project, and the residue is their transport along that chain.
:::

::: {.remark title="Scope of the exercised cases"}

The orbit algorithm was exercised on the family $U\oplus U(2)\oplus X$ with $X$ successively $0$, $A_2$, $A_3$, $A_2^{\oplus 2}$ and $E_8^{\oplus 2}$, and on $U^{\oplus 2}\oplus E_7$, at target norm $0$; the last of the first family is $M$ itself.
The resulting orbit counts are not part of the record.
:::

::: {.remark title="The implementation named in the recipe"}

Step 6 of the recipe in [the computational toolchain and recipe](#sec-computational-toolchain-and-recipe) asks for orbit representatives through the function `vector_orbit_representatives`, which `sage-indefinite-port` owns. That is the second algorithm above, and the separating invariants the recipe pairs with it, $\div(v)$ and $v^{\perp}/v$ matched against the table of $2$-elementary lattices keyed by $(r,a,\delta)$, are the invariants under which the orbit representatives it returns are recognized.
:::

## What remains for the Coble lattices

::: {.remark title="The residue"}

The algorithms above decide orbit equivalence for a fixed indefinite form and a fixed group.
For $T_\Co = \generators{2}\oplus E_{10}(2)$ the remaining inputs are the group and the lift: the orbits are wanted for $\Orth(T_\Co)$, for $\discriminantkernel{T_\Co}$ and for $\Gamma_\Co$, which differ, and the reduction to $A_{T_\Co}\cong(\ZZ/2\ZZ)^{11}$ requires the surjectivity hypothesis above together with the lifting statement of @thm:sterk-orbit.
Every primitive isotropic vector of $T_\Co$ has $\div_{T_\Co}(v) = 2$ (@lem:divisibilityAlwaysTwoTco), so the divisibility half of condition (2) of @prop:orbit-necessary-conditions separates nothing there, and the class $[v^*]\in A_{T_\Co}$ is the whole of that invariant.
The candidate isotropic vectors of $T_\Co$ and the three-way transport of each along $T_\Co\injects \ten\injects \tdp$ are recorded in [Coble lattice isotropic candidates](#sec-coble-lattice-isotropic-candidates); running the orbit solver on them is the step that would replace the vector-by-vector table with a count.
:::

Related: [Scattone cusp method](#sec-scattone-cusp-method), [Coble lattice isotropic candidates](#sec-coble-lattice-isotropic-candidates), [computational toolchain and recipe](#sec-computational-toolchain-and-recipe), [cusp-correspondence morphism chain](#sec-cusp-correspondence-morphism-chain), [open problems](#sec-open-problems).
