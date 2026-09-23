# KSBA and semitoroidal compactifications of $\fentwo$

::: {.Remark}
### Orientation

This section records the degree-$2$ Enriques side of the KSBA--semitoroidal comparison: the compactification of $\fentwo$, the moduli space of degree-$2$ numerically polarized Enriques surfaces.
Here the comparison is a theorem, obtained by reducing to the recognizable-divisor machinery of Alexeev--Engel ([the recognizable-divisor semitoroidal theorem](#thm:recognizable-semitoroidal), [the tower semitoroidal theorem](#thm:tower-semitoroidal)); the ambient degree-$2$ Enriques KSBA compactification is itself settled [@AEGS25; @CDL25].
This is the established counterpart of the polarized *Coble* comparison, which remains an open program: see [the Coble KSBA--semitoroidal comparison conjecture](#conj:ksba_semitoroidal_comparison) for the Coble isomorphism target and [the restricted-ramification-semifan conjecture](#conj:restricted_ramification_semifan) for the Coble semifan-restriction analogue of the descent below.

:::

## The isomorphism theorem

::: {.Theorem #thm:ksba_semitoroidal_En2}
### Isomorphism between KSBA and semitoroidal compactifications of $\fentwo$

Let $\fentwo$ be the moduli space of degree-$2$ numerically polarized Enriques surfaces, and let $\ksbacpt{\fentwo}$ be its KSBA compactification.
There is an isomorphism
$$
\normalize{\semifancpt{\fentwo}{\semifans{F}}}
\xrightarrow{\ \sim\ }
\normksbacpt{\fentwo}
$$
where $(-)^\nu$ denotes normalization.
The left-hand side is the semitoroidal compactification corresponding to an explicit collection
$$
\semifans{F} = \{\, \semifan{F}_1,\ \torfan_2,\ \semifan{F}_3,\ \torfan_4,\ \semifan{F}_5 \,\}
$$
of semifans, one for each $0$-cusp of the Baily--Borel compactification $\bbcpt{\fentwo}$, and the right-hand side is the KSBA compactification.

:::

::: {.Remark}
### Fan versus strict-semifan bookkeeping

The five cusps of $\bbcpt{\fentwo}$ match Sterk's five $0$-cusps of the Enriques period space [@Ste91], one semifan per cusp.
Among the entries of $\semifans{F}$, the even-indexed entries $\torfan_2, \torfan_4$ are honest fans, while the odd-indexed entries $\semifan{F}_1, \semifan{F}_3, \semifan{F}_5$ are strict semifans (in the sense of [the generalized Coxeter-semifan definition](#def:generalized-coxeter-semifan), i.e.\ with infinite irrelevant subgroup, so not locally finite).

:::

::: {.proof}

The proof reduces to the recognizable-divisor theorem of Alexeev--Engel [@AE23]: for a recognizable divisor $R$, the normalization of the KSBA compactification of stable K3 pairs $(X, \varepsilon R)$ is isomorphic to a semitoroidal compactification ([the recognizable-divisor semitoroidal theorem](#thm:recognizable-semitoroidal), and the more general tower criterion of [the tower semitoroidal theorem](#thm:tower-semitoroidal)).
The relevant polarizing divisor here is the ramification divisor $R_\iota$ of the nonsymplectic Enriques involution, which is recognizable ([the recognizable-divisor example](#ex:recognizable-divisors)).
Applying the theorem produces a semitoroidal compactification on the normalization of $\ksbacpt{\fentwo}$, and identifying the resulting semifan cusp-by-cusp gives the explicit collection $\semifans{F}$, one semifan per $0$-cusp.
The passage from the ambient K3 picture to the Enriques space is [the semitoroidal-data descent conjecture](#conj:descent_semitoroidal_data_En2), which supplies the folded semifans $\mathcal{F}_k$ and their boundary stratification.

::: {.Warning}
The source note states the reduction to Alexeev--Engel but does not carry out the cusp-by-cusp identification of $\semifans{F}$ nor the descent of the semifan; these are recorded here (the descent as [the semitoroidal-data descent conjecture](#conj:descent_semitoroidal_data_En2)) rather than proved in full.
:::

:::

::: {.Remark}
### Role of the normalization

The normalization $(-)^\nu$ is a technical condition standard in KSBA compactifications: taking a Zariski closure can introduce non-normal points where distinct degenerations are identified, producing a non-separated stack.
Since the normalization morphism is finite, birational, and relatively smooth in codimension one, it confines the worst singularities to high-codimension sub-loci, which is what makes the isomorphism above an isomorphism of normal varieties.

:::

## Descent of semitoroidal data

::: {.Conjecture #conj:descent_semitoroidal_data_En2}
### Descent of semifans to $\normalize{B}$

The normalization $\normalize{B} \to B$ of the Noether--Lefschetz closure $B$ yields a normal projective variety.
The semitoroidal structure on $\semifancpt{\fttz}{\semifan{F}_{\ram}}$ defined by the ramification semifan $\semifan{F}_{\ram}$ restricts to $\normalize{B}$.
Imposing the involution constraints on this restricted structure produces a collection of *folded semifans* $\semifan{F}_k$.

:::

::: {.Remark}
### Folded semifans and the boundary stratification

The folded semifans $\semifan{F}_k$ determine the semitoroidal compactification $\semifancpt{\fentwo}{\semifans{F}}$ appearing in [the KSBA--semitoroidal isomorphism theorem](#thm:ksba_semitoroidal_En2), and they define the combinatorial stratification of its boundary, which maps directly onto the KSBA strata.
The ambient degree-$(2,2,0)$ K3 picture and the Noether--Lefschetz locus enter through the stable-pair family and the locally closed embeddings of [the Baily--Borel embedding lemma](#lem:locally_closed_embedding_BB); the descent here is the Enriques (involution-quotient) analogue of the Coble semifan restriction of [the restricted-ramification-semifan conjecture](#conj:restricted_ramification_semifan).

::: {.Warning}
The source note is tagged as a proposition but reproduces no proof or proof reference for the descent/restriction itself (that $\semifan{F}_{\ram}$ restricts to $\normalize{B}$ and folds to the $\semifan{F}_k$); it is recorded here as a conjecture pending that argument. Within the settled degree-$2$ Enriques package [@AEGS25] this descent is expected to hold, and the statement may be upgraded to a proposition once the restriction-and-folding argument is written or cited.
:::

:::

## The polarized Coble analogue

::: {.Remark}

The polarized Coble compactification records the same comparison as an open program rather than a theorem: after normalization the KSBA compactification of the polarized Coble locus is conjectured to agree with the semitoroidal compactification induced by the *restricted* ramification semifan ([the Coble KSBA--semitoroidal comparison conjecture](#conj:ksba_semitoroidal_comparison), [the restricted-ramification-semifan conjecture](#conj:restricted_ramification_semifan)).
Its extra difficulties are exactly the ones absent from the Enriques theorem above: branchwise root data, the ramification-semifan restriction identity, and [the no-moduli-loss conjecture](#conj:no_moduli_loss).

:::
