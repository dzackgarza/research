# The moduli space $F_{\En,2}$: main results

Here we collect the principal structural results for the KSBA compactification $\overline{F_{\En, 2}}$ of the moduli space $F_{\En, 2}$ of degree-$2$ numerically polarized Enriques surfaces: the identification of the normalized compactification with a semitoroidal model, the realization of $F_{\En, 2}$ as a normalization inside the degree-$(2,2,0)$ K3 moduli space, and the enumeration of the five $0$-cusps together with their folded Coxeter data.
These describe the *ambient* degree-$2$ Enriques picture, into which the polarized Coble locus is later cut by an admissible root (cf. \cref{conj:restricted_ramification_semifan}).

## The main theorem

::: {.theorem ref="thm:fen2_main" title="Compactification of $F_{\En, 2}$"}

Let $\overline{F_{\En, 2}}$ denote the KSBA compactification of the moduli space $F_{\En, 2}$ of numerically polarized Enriques surfaces of degree $2$.
Let $\mathcal{F}_\bullet = \ts{\mathcal{F}_k}_{k=1}^5$ be the collection of folded semifans for the $0$-cusps.

1. The normalization $\overline{F_{\En, 2}}^\nu$ is isomorphic to the semitoroidal compactification $\overline{F_{\En, 2}}^{\mathcal{F}_\bullet}$ [@AEGS25 Thm. 1].

2. This compactification is toroidal over cusps $2$, $4$, their adjacent $1$-cusps, and cusp $35$, and strictly semitoroidal over all other cusps.

3. The isomorphism is established via an intermediate normalization $B^\nu$ of the Zariski closure of the Noether--Lefschetz locus inside the K3 compactification $\overline{F_{(2,2,0)}}$ [@AEGS25 Sec. 6].
:::

\todo{Part 2 as migrated says "cusp 35", read alongside cusps 2 and 4. This is inconsistent with the five-cusp enumeration of \cref{ex:fen2_five_cusps}, where cusps $3$ and $5$ are recorded as strictly semitoroidal (only cusps $2$ and $4$ are toroidal). "cusp 35" is reproduced verbatim from the source note; resolve whether it is a typo for "cusps $3$, $5$", a distinct $1$-cusp label, or a mis-transcription, and reconcile with the toroidal/semitoroidal split of the cusp enumeration.}

::: {.remark}

This theorem records the settled ambient degree-$2$ Enriques picture: the normalized KSBA compactification of $F_{\En, 2}$ coincides with an explicit semitoroidal model built from five folded semifans, one per $0$-cusp.
The proof runs through the K3 moduli space $F_{(2,2,0)}$ of the degree-$(2,2,0)$ problem, identifying $\overline{F_{\En, 2}}^\nu$ with a normalization of the closure of the relevant Noether--Lefschetz locus; see \cref{lem:fen2_normalization} for the corresponding period-domain statement.
:::

## Normalization inside $F_{(2,2,0)}$

::: {.lemma ref="lem:fen2_normalization" title="Normalization of $F_{\En, 2}$"}

There exists a closed subscheme $X \subset F_{(2,2,0)}$ such that $F_{\En, 2}$ is canonically isomorphic to the normalization of $X$.
:::

::: {.proof}

This is established via an algebraic morphism of period domains
$$
\Psi : F_{\En, 2} \to F_{(2,2,0)}
$$
induced by the unique lattice embedding $\tilde\Psi : T_\En \injects T_\dP$ defined by
$$
\tilde\Psi(u_1, u_2, v) \da (u_1, u_2, v, v).
$$
Restricting $\Psi$ to its scheme-theoretic image $X$ yields a finite, birational map from the normal variety $F_{\En, 2}$ to $X$, which by Zariski's Main Theorem exhibits $F_{\En, 2}$ as the normalization of $X$.
:::

## The five $0$-cusps

::: {.example ref="ex:fen2_five_cusps" title="The five $0$-cusps of $\overline{F_{\En, 2}}$"}

The boundary of the KSBA compactification $\overline{F_{\En, 2}}$ is stratified by $27$ rays across five $0$-cusps.
For each $0$-cusp we record the topological type of the reduced dual complex $\Gamma(\mathcal{Z}_0)$, the number of Type II and Type III rays, and the integral-affine-structure (IAS) involution.

1. **Cusp 1**: Semitoroidal.
   $\Gamma(\mathcal{Z}_0) = \mathbf{RP}^2$.
   $2$ Type II rays, $0$ Type III. IAS involution: $180^\circ$ rotation $+$ flip hemispheres.

2. **Cusp 2**: Toroidal.
   $\Gamma(\mathcal{Z}_0) = \mathbf{D}^2$.
   $2$ Type II rays, $7$ Type III. IAS involution: vertical flip of both hemispheres.

3. **Cusp 3**: Semitoroidal.
   $\Gamma(\mathcal{Z}_0) = \mathbf{D}^2$.
   $2$ Type II rays, $7$ Type III. IAS involution: diagonal flip.

4. **Cusp 4**: Toroidal.
   $\Gamma(\mathcal{Z}_0) = \mathbf{D}^2$.
   $4$ Type II rays, $7$ Type III. IAS involution: horizontal flip.

5. **Cusp 5**: Semitoroidal.
   $\Gamma(\mathcal{Z}_0) = \mathbf{D}^2$.
   $3$ Type II rays, $0$ Type III. IAS involution: flip hemispheres.
:::

\todo{The header records "27 rays" in total, but the per-cusp counts sum to $2 + 9 + 9 + 11 + 3 = 34$ Type II$+$Type III rays. The discrepancy is plausibly explained by Type II rays being shared between adjacent $0$-cusps (they correspond to $1$-cusps, each incident to several $0$-cusps), so that the total of $27$ counts distinct rays while the per-cusp sum double-counts shared Type II rays; confirm the intended bookkeeping.}

::: {.remark}

This enumeration is the boundary data underlying the folded semifans $\mathcal{F}_\bullet$ of \cref{thm:fen2_main}: each $0$-cusp carries a reduced dual complex, a partition of its rays into the Type II (adjacent $1$-cusp) and Type III (deeper) strata, and the involution of its integral affine structure that folds the covering K3 data onto the Enriques data.
The precise per-cusp ray counts and IAS involutions are migrated from the working notes and, as with the cusp tables discussed in \cref{conj:ksba_semitoroidal_comparison}, should be regarded as provisional pending an independent cusp computation.
:::

## Folded Coxeter diagrams of the five cusps

::: {.remark ref="rmk:fen2_folded_coxeter" title="Folded Coxeter diagrams of $F_{\En, 2}$"}

The five $0$-cusps of $F_{\En, 2}$ are expected to correspond to five distinct orbits of primitive isotropic vectors in $T_\En$, each realized as a folded image of a Coxeter diagram for $F_{(2,2,0)}$ under the involution $I = -I_\En$ (the root-folding criterion of \cref{lem:root-folding-tdp}, in the sense of \cref{def:folded-root}):

1. **$\eta_1$**: Divisibility $1$, derived from $\tilde\eta_1$ via $180^\circ$ rotation.
   (Boundary lattice: $U(2) \oplus E_8(2)$.)

2. **$\eta_2$**: Divisibility $2$, derived from $\tilde\eta_2$ via vertical reflection.
   (Boundary lattice: $U \oplus E_8(2)$.)

3. **$\eta_3$**: Divisibility $2$, derived from $\tilde\eta_1$ via diagonal reflection $+$ root swap.
   (Boundary lattice: $U \oplus E_8(2)$.)

4. **$\eta_4$**: Divisibility $2$, derived from $\tilde\eta_1$ via horizontal reflection.
   (Boundary lattice: $U \oplus E_8(2)$.)

5. **$\eta_5$**: Divisibility $2$, derived from $\tilde\eta_1$ via $8$ commuting reflections.
   (Boundary lattice: $U \oplus E_8(2)$.)
:::

::: {.remark}

The folded chamber $\mathfrak{C}^I = \mathfrak{C} \cap \overline{T}_{\eta, \mathbf{R}}^{I = 1}$ has walls defined by the roots descending from the covering domain (cf. the classical foldings of \cref{ex:classical-foldings}).

The polarized Coble boundary problem uses this folded Enriques data only as ambient input.
The extra marked-root refinement -- the admissibility test for Coble roots at a cusp and the restriction of the ramification semifan to the polarized Coble locus -- is recorded separately in \cref{que:coble_cusp_admissibility} and \cref{conj:restricted_ramification_semifan}.
:::
