# KSBA and semitoroidal compactifications of $\fentwo$

## The isomorphism theorem

::: {.theorem #thm:ksba_semitoroidal_En2 title="Isomorphism between KSBA and semitoroidal compactifications of $\fentwo$"}

Let $\fentwo$ be the moduli space of degree-$2$ numerically polarized Enriques surfaces (@def:enriques-surface), and let $\ksbacpt{\fentwo}$ be its KSBA compactification (@def:ksba-compactification).
There is an isomorphism (@def:isomorphism-of-objects)
$$
\normalize{\semifancpt{\fentwo}{\semitorfan}}
\xrightarrow{\ \sim\ }
\normksbacpt{\fentwo}
$$
where $(-)^\nu$ denotes normalization.
The left-hand side is the semitoroidal compactification (@def:semitoroidal-compactification) corresponding to an explicit collection
$$
\semitorfan = \{\, \semifan{F}_1,\ \torfan_2,\ \semifan{F}_3,\ \torfan_4,\ \semifan{F}_5 \,\}
$$
of semifans, one for each $0$-cusp of the Baily--Borel compactification $\bbcpt{\fentwo}$, and the right-hand side is the KSBA compactification [@AEGS25, Thm. 1.1].
:::

::: {.proof}

The proof is [@AEGS25, proof of Thm. 5.9].
For a recognizable divisor (@def:recognizable-divisor) $R$, the normalization of the KSBA compactification of K3 pairs $(X, \eps R)$ is semitoroidal (@thm:recognizable-semitoroidal).
The ramification divisor of a nonsymplectic involution is recognizable (@ex:recognizable-divisors; [@AEH24, Thm. 3.24]).
For $\fttz$ the semifan of this compactification is the ramification semifan $\semifan{F}_{\ram}$ [@AE22, Thm. 9.10].

Let $B$ be the closure of the image of $\fentwo$ in $\ksbacpt{\fttz}$.
The Enriques involution extends to the pulled-back family over $B$, and there is a classifying morphism $\normalize{B}\to\ksbacpt{\fentwo}$ (@prop:enriques-involution-extends).
The normalization $\normalize{B}$ is the semitoroidal compactification of $B$ induced by $\semifan{F}_{\ram}$ (@prop:normalized-nl-closure-semitoroidal).
This gives a family of KSBA-stable pairs over the induced compactification of $\fentwo$, whose normalization is the semitoroidal compactification for the collection $\semitorfan$ of @prop:enriques-semifan-coarsening [@AEGS25, Def. 5.3, Lem. 5.5].

It remains to show that $\normalize{B}\to\ksbacpt{\fentwo}$ is finite.
By @prop:enriques-semifan-coarsening(1,2), it suffices to show that the maximal (@def:maximal-lattice) cones of the coarsening $\semifan{G}_k$ are the maximal cones of $\semifan{F}_k$.
If the coarsening were strict (@def:monoidal-category), a codimension-one cone of some $\semifan{F}_k$ would parametrize a $1$-dimensional family of pairs $(X, \eps R)$ that are not maximally degenerate (@def:definiteness), whose Enriques quotients $(Z, \eps R_Z)$ have the maximal number of double curves.
This contradicts @prop:enriques-semifan-coarsening(3).
The toroidal and strictly semitoroidal cusps are given by [@AEGS25, Lem. 5.7].
:::

## Descent of semitoroidal data

::: {.proposition #prop:normalized-nl-closure-semitoroidal title="Descent of semifans to $\normalize{B}$"}

Let $B$ be the closure of the image of $\fentwo$ in $\ksbacpt{\fttz}$ (@prop:enriques-involution-extends).

1. The normalization $\normalize{B}$ is the semitoroidal compactification (@def:semitoroidal-compactification) of the Noether--Lefschetz locus (@def:nl-locus-enriques) $B$ induced by the ramification semifan $\semifan{F}_{\ram}$, which gives the normalization $\normksbacpt{\fttz}$ [@AEGS25, proof of Thm. 5.9].

2. For each $0$-cusp of $\fentwo$, the semifan $\semifan{F}_k$ is the intersection of the semifan $\semifan{F}_{\ram}(\overline{T}_{\mathrm{dP}})$, for $\overline{T}_{\mathrm{dP}} = (18,0,0)_1$ or $(18,2,0)_1$, with the subspace $\overline{T}_{\mathrm{En}} = (10,10,0)_1$ or $(10,8,0)_1$ [@AEGS25, Def. 5.3].
   The subspace $\overline{T}_{\mathrm{En}}$ is the $(+1)$-eigenspace of the involution $J$ of $\overline{T}_{\mathrm{dP}}$ in @cons:fen2-cusp-involutions [@AEGS25, Def. 3.5].

3. The semifans $\semifan{F}_k$ are the generalized Coxeter semifans (@def:generalized-coxeter-semifan) of the folded Coxeter--Vinberg diagrams (@def:coxeter-vinberg-diagram) of @prop:fen2-folded-coxeter, in which the irrelevant roots are the foldings (@def:folding-bc) of the irrelevant roots of $\semifan{F}_{\ram}$ [@AEGS25, Sec. 5.2, Def. 5.4, Lem. 5.5].

4. The family of KSBA-stable pairs (@def:ksba-compactification) over $\normalize{B}$ gives a family over the induced compactification of $\fentwo$, and the normalization of this compactification is $\semifancpt{\fentwo}{\semitorfan}$ for the collection $\semitorfan = \theset{\semifan{F}_k}_{k=1}^5$ [@AEGS25, proof of Thm. 5.9].
:::

::: {.conjecture #conj:descent_semitoroidal_data_En2 title="Projectivity of $\normalize{B}$"}

The normalization $\normalize{B}$ of the Noether--Lefschetz closure (@def:nl-locus-enriques) $B$ is a projective (@def:module-subcategories) variety.
:::
