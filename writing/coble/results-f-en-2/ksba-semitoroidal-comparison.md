# KSBA and semitoroidal compactifications of $\fentwo$

## The isomorphism theorem

::: {.theorem #thm:ksba_semitoroidal_En2 title="Isomorphism between KSBA and semitoroidal compactifications of $\fentwo$"}

Let $\fentwo$ be the moduli space of degree-$2$ numerically polarized Enriques surfaces, and let $\ksbacpt{\fentwo}$ be its KSBA compactification.
There is an isomorphism
$$
\normalize{\semifancpt{\fentwo}{\semitorfan}}
\xrightarrow{\ \sim\ }
\normksbacpt{\fentwo}
$$
where $(-)^\nu$ denotes normalization.
The left-hand side is the semitoroidal compactification corresponding to an explicit collection
$$
\semitorfan = \{\, \semifan{F}_1,\ \torfan_2,\ \semifan{F}_3,\ \torfan_4,\ \semifan{F}_5 \,\}
$$
of semifans, one for each $0$-cusp of the Baily--Borel compactification $\bbcpt{\fentwo}$, and the right-hand side is the KSBA compactification [@AEGS25, Thm. 1.1].
:::

::: {.proof}

The proof is [@AEGS25, proof of Thm. 5.9].
For a recognizable divisor $R$, the normalization of the KSBA compactification of K3 pairs $(X, \eps R)$ is semitoroidal (@thm:recognizable-semitoroidal).
The ramification divisor of a nonsymplectic involution is recognizable (@ex:recognizable-divisors; [@AEH24]).
For $\fttz$ the semifan of this compactification is the ramification semifan $\semifan{F}_{\ram}$ [@AE22].

Let $B$ be the closure of the image of $\fentwo$ in $\ksbacpt{\fttz}$.
The Enriques involution extends to the pulled-back family over $B$, and there is a classifying morphism $\normalize{B}\to\ksbacpt{\fentwo}$ (@prop:enriques-involution-extends).
The normalization $\normalize{B}$ is the semitoroidal compactification of $B$ induced by $\semifan{F}_{\ram}$.
This gives a family of KSBA-stable pairs over the induced compactification of $\fentwo$, whose normalization is the semitoroidal compactification for the collection $\semitorfan$ of @prop:enriques-semifan-coarsening [@AEGS25, Def. 5.3, Lem. 5.5].

It remains to show that $\normalize{B}\to\ksbacpt{\fentwo}$ is finite.
By @prop:enriques-semifan-coarsening(1,2), it suffices to show that the maximal cones of the coarsening $\semifan{G}_k$ are the maximal cones of $\semifan{F}_k$.
If the coarsening were strict, a codimension-one cone of some $\semifan{F}_k$ would parametrize a $1$-dimensional family of pairs $(X, \eps R)$ that are not maximally degenerate, whose Enriques quotients $(Z, \eps R_Z)$ have the maximal number of double curves.
This contradicts @prop:enriques-semifan-coarsening(3).
The toroidal and strictly semitoroidal cusps are given by [@AEGS25, Lem. 5.7].
:::

## Descent of semitoroidal data

::: {.conjecture #conj:descent_semitoroidal_data_En2 title="Descent of semifans to $\normalize{B}$"}

The normalization $\normalize{B} \to B$ of the Noether--Lefschetz closure $B$ yields a normal projective variety.
The semitoroidal structure on $\semifancpt{\fttz}{\semifan{F}_{\ram}}$ defined by the ramification semifan $\semifan{F}_{\ram}$ restricts to $\normalize{B}$.
Imposing the involution constraints on this restricted structure produces a collection of *folded semifans* $\semifan{F}_k$.
:::
