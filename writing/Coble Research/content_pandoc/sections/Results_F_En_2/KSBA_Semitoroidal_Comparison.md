# KSBA and semitoroidal compactifications of $F_{\En,2}$

::: {.remark title="Orientation"}

This section records the degree-$2$ Enriques side of the KSBA--semitoroidal comparison: the compactification of $F_{\En, 2}$, the moduli space of degree-$2$ numerically polarized Enriques surfaces.
Here the comparison is a theorem, obtained by reducing to the recognizable-divisor machinery of Alexeev--Engel (\cref{thm:recognizable-semitoroidal}, \cref{thm:tower-semitoroidal}); the ambient degree-$2$ Enriques KSBA compactification is itself settled [@AEGS25; @CDL25].
This is the established counterpart of the polarized *Coble* comparison, which remains an open program: see \cref{conj:ksba_semitoroidal_comparison} for the Coble isomorphism target and \cref{conj:restricted_ramification_semifan} for the Coble semifan-restriction analogue of the descent below.

:::

## The isomorphism theorem

::: {.theorem ref="thm:ksba_semitoroidal_En2" title="Isomorphism between KSBA and semitoroidal compactifications of $F_{\En,2}$"}

Let $F_{\En, 2}$ be the moduli space of degree-$2$ numerically polarized Enriques surfaces, and let $\overline{F_{\En, 2}}$ be its KSBA compactification.
There is an isomorphism
$$
\left(\overline{F_{\En, 2}}^{\mathcal{F}_{\bullet}}\right)^{\nu}
\xrightarrow{\ \sim\ }
\left(\overline{F_{\En, 2}}\right)^{\nu}
$$
where $(-)^\nu$ denotes normalization.
The left-hand side is the semitoroidal compactification corresponding to an explicit collection
$$
\mathcal{F}_{\bullet} = \{\, \mathcal{F}_1,\ \Sigma_2,\ \mathcal{F}_3,\ \Sigma_4,\ \mathcal{F}_5 \,\}
$$
of semifans, one for each $0$-cusp of the Baily--Borel compactification $\overline{F_{\En, 2}}^{\operatorname{BB}}$, and the right-hand side is the KSBA compactification.

:::

::: {.remark title="Fan versus strict-semifan bookkeeping"}

The five cusps of $\overline{F_{\En, 2}}^{\operatorname{BB}}$ match Sterk's five $0$-cusps of the Enriques period space [@Ste91], one semifan per cusp.
Among the entries of $\mathcal{F}_{\bullet}$, the even-indexed entries $\Sigma_2, \Sigma_4$ are honest fans, while the odd-indexed entries $\mathcal{F}_1, \mathcal{F}_3, \mathcal{F}_5$ are strict semifans (in the sense of \cref{def:generalized-coxeter-semifan}, i.e.\ with infinite irrelevant subgroup, so not locally finite).

:::

::: {.proof}

The proof reduces to the recognizable-divisor theorem of Alexeev--Engel [@AE23]: for a recognizable divisor $R$, the normalization of the KSBA compactification of stable K3 pairs $(X, \varepsilon R)$ is isomorphic to a semitoroidal compactification (\cref{thm:recognizable-semitoroidal}, and the more general tower criterion of \cref{thm:tower-semitoroidal}).
The relevant polarizing divisor here is the ramification divisor $R_\iota$ of the nonsymplectic Enriques involution, which is recognizable (\cref{ex:recognizable-divisors}).
Applying the theorem produces a semitoroidal compactification on the normalization of $\overline{F_{\En, 2}}$, and identifying the resulting semifan cusp-by-cusp gives the explicit collection $\mathcal{F}_\bullet$, one semifan per $0$-cusp.
The passage from the ambient K3 picture to the Enriques space is the descent of \cref{conj:descent_semitoroidal_data_En2}, which supplies the folded semifans $\mathcal{F}_k$ and their boundary stratification.
\todo{The source note states the reduction to Alexeev--Engel but does not carry out the cusp-by-cusp identification of $\mathcal{F}_\bullet$ nor the descent of the semifan; these are recorded here (the descent as \cref{conj:descent_semitoroidal_data_En2}) rather than proved in full.}

:::

::: {.remark title="Role of the normalization"}

The normalization $(-)^\nu$ is a technical condition standard in KSBA compactifications: taking a Zariski closure can introduce non-normal points where distinct degenerations are identified, producing a non-separated stack.
Since the normalization morphism is finite, birational, and relatively smooth in codimension one, it confines the worst singularities to high-codimension sub-loci, which is what makes the isomorphism above an isomorphism of normal varieties.

:::

## Descent of semitoroidal data

::: {.conjecture ref="conj:descent_semitoroidal_data_En2" title="Descent of semifans to $B^\nu$"}

The normalization $B^\nu \to B$ of the Noether--Lefschetz closure $B$ yields a normal projective variety.
The semitoroidal structure on $\overline{F_{(2,2,0)}}$ defined by the ramification semifan $\mathcal{F}_{\operatorname{ram}}$ restricts to $B^\nu$.
Imposing the involution constraints on this restricted structure produces a collection of *folded semifans* $\mathcal{F}_k$.

:::

::: {.remark title="Folded semifans and the boundary stratification"}

The folded semifans $\mathcal{F}_k$ determine the semitoroidal compactification $\overline{F_{\En, 2}}^{\mathcal{F}_\bullet}$ appearing in \cref{thm:ksba_semitoroidal_En2}, and they define the combinatorial stratification of its boundary, which maps directly onto the KSBA strata.
The ambient degree-$(2,2,0)$ K3 picture and the Noether--Lefschetz locus enter through the stable-pair family and the locally closed embeddings of \cref{lem:locally_closed_embedding_BB}; the descent here is the Enriques (involution-quotient) analogue of the Coble semifan restriction of \cref{conj:restricted_ramification_semifan}.
\todo{The source note is tagged as a proposition but reproduces no proof or proof reference for the descent/restriction itself (that $\mathcal{F}_{\operatorname{ram}}$ restricts to $B^\nu$ and folds to the $\mathcal{F}_k$); it is recorded here as a conjecture pending that argument. Within the settled degree-$2$ Enriques package [@AEGS25] this descent is expected to hold, and the statement may be upgraded to a proposition once the restriction-and-folding argument is written or cited.}

:::

## The polarized Coble analogue

::: {.remark}

The polarized Coble compactification records the same comparison as an open program rather than a theorem: after normalization the KSBA compactification of the polarized Coble locus is conjectured to agree with the semitoroidal compactification induced by the *restricted* ramification semifan (\cref{conj:ksba_semitoroidal_comparison}, \cref{conj:restricted_ramification_semifan}).
Its extra difficulties are exactly the ones absent from the Enriques theorem above: branchwise root data, the ramification-semifan restriction identity, and the no-moduli-loss problem (\cref{conj:no_moduli_loss}).

:::
