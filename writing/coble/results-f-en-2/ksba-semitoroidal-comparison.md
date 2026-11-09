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
of semifans, one for each $0$-cusp of the Baily--Borel compactification $\bbcpt{\fentwo}$, and the right-hand side is the KSBA compactification.
:::

::: {.proof}

This is [@AEGS25].

Cited from AEGS, in the section the statement names. The book uses the comparison as the target of its own normalization theorem, so it is quoted.
:::

::: {.remark title="Fan versus strict-semifan bookkeeping"}

The five cusps of $\bbcpt{\fentwo}$ match Sterk's five $0$-cusps of the Enriques period space [@Ste91], one semifan per cusp.
Among the entries of $\semitorfan$, the even-indexed entries $\torfan_2, \torfan_4$ are honest fans, while the odd-indexed entries $\semifan{F}_1, \semifan{F}_3, \semifan{F}_5$ are semifans that are not fans, the irrelevant roots generating an infinite reflection group [@AE22].
:::

::: {.proof}

The proof reduces to the recognizable-divisor theorem of Alexeev--Engel [@AE23]: for a recognizable divisor $R$, the normalization of the KSBA compactification of stable K3 pairs $(X, \varepsilon R)$ is isomorphic to a semitoroidal compactification (@thm:recognizable-semitoroidal, and the more general tower criterion of @thm:tower-semitoroidal).
The relevant polarizing divisor here is the ramification divisor $R_\iota$ of the nonsymplectic Enriques involution, which is recognizable (@ex:recognizable-divisors).
Applying the theorem produces a semitoroidal compactification on the normalization of $\ksbacpt{\fentwo}$, and identifying the resulting semifan cusp-by-cusp gives the explicit collection $\semitorfan$, one semifan per $0$-cusp.
The passage from the ambient K3 picture to the Enriques space is the semitoroidal-data descent conjecture (@conj:descent_semitoroidal_data_En2), which supplies the folded semifans $\mathcal{F}_k$ and their boundary stratification.
:::

::: {.warning}
The reduction to Alexeev--Engel leaves two steps open: the cusp-by-cusp identification of $\semitorfan$, and the descent of the semifan (@conj:descent_semitoroidal_data_En2).
:::

::: {.remark title="Role of the normalization"}

The normalization $(-)^\nu$ is a technical condition standard in KSBA compactifications: taking a Zariski closure can introduce non-normal points where distinct degenerations are identified, producing a non-separated stack.
Since the normalization morphism is finite, birational, and an isomorphism in codimension one, it confines the worst singularities to high-codimension sub-loci, which is what makes the isomorphism above an isomorphism of normal varieties.
:::

## Descent of semitoroidal data

::: {.conjecture #conj:descent_semitoroidal_data_En2 title="Descent of semifans to $\normalize{B}$"}

The normalization $\normalize{B} \to B$ of the Noether--Lefschetz closure $B$ yields a normal projective variety.
The semitoroidal structure on $\semifancpt{\fttz}{\semifan{F}_{\ram}}$ defined by the ramification semifan $\semifan{F}_{\ram}$ restricts to $\normalize{B}$.
Imposing the involution constraints on this restricted structure produces a collection of *folded semifans* $\semifan{F}_k$.
:::

::: {.remark title="Folded semifans and the boundary stratification"}

The folded semifans $\semifan{F}_k$ determine the semitoroidal compactification $\semifancpt{\fentwo}{\semitorfan}$ appearing in the KSBA--semitoroidal isomorphism theorem (@thm:ksba_semitoroidal_En2), and they define the combinatorial stratification of its boundary, which maps directly onto the KSBA strata.
The ambient degree-$(2,2,0)$ K3 picture and the Noether--Lefschetz locus enter through the stable-pair family and the locally closed embeddings of @lem:locally_closed_embedding_BB; the descent here is the Enriques (involution-quotient) analogue of the Coble semifan restriction of @conj:restricted_ramification_semifan.

:::

## The polarized Coble analogue

::: {.remark}

For the polarized Coble compactification the same comparison is conjectural: after normalization the KSBA compactification of the polarized Coble locus is conjectured to agree with the semitoroidal compactification induced by the *restricted* ramification semifan (@conj:ksba_semitoroidal_comparison, @conj:restricted_ramification_semifan). Its extra difficulties are exactly the ones absent from the Enriques theorem above: the root stabilizers of the branches, the ramification-semifan restriction identity, and the absence of moduli loss (@conj:no_moduli_loss).
:::
