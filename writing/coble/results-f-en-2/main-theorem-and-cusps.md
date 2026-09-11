# The moduli space $F_{\En,2}$: main results

Here we collect the principal structural results for the KSBA compactification $\overline{F_{\En, 2}}$ of the moduli space $F_{\En, 2}$ of degree-$2$ numerically polarized Enriques surfaces: the identification of the normalized compactification with a semitoroidal model, the realization of $F_{\En, 2}$ as a normalization inside the degree-$(2,2,0)$ K3 moduli space, and the enumeration of the five $0$-cusps together with their folded Coxeter data.
These describe the *ambient* degree-$2$ Enriques picture, into which the polarized Coble locus is later cut by an admissible root (cf. \longref{conj:restricted_ramification_semifan}).

## The main theorem

::: {.Theorem #thm:fen2_main}
### Compactification of $F_{\En, 2}$

Let $\overline{F_{\En, 2}}$ denote the KSBA compactification of the moduli space $F_{\En, 2}$ of numerically polarized Enriques surfaces of degree $2$.
Let $\mathcal{F}_\bullet = \ts{\mathcal{F}_k}_{k=1}^5$ be the collection of folded semifans for the $0$-cusps.

1. The normalization $\overline{F_{\En, 2}}^\nu$ is isomorphic to the semitoroidal compactification $\overline{F_{\En, 2}}^{\mathcal{F}_\bullet}$ [@AEGS25 Thm. 1].

2. This compactification is toroidal over cusps $2$, $4$, their adjacent $1$-cusps, and cusp $35$, and strictly semitoroidal over all other cusps.

3. The isomorphism is established via an intermediate normalization $B^\nu$ of the Zariski closure of the Noether--Lefschetz locus inside the K3 compactification $\overline{F_{(2,2,0)}}$ [@AEGS25 Sec. 6].
:::

::: {.Notation #not:sterk-cusp-labels}
### Two indexings of the boundary

The $0$-cusps carry Sterk's numbering $1,\dots,5$, as in \longref{ex:fen2_five_cusps}.
A $1$-cusp is denoted $i_1\dots i_k$ when its closure contains the $0$-cusps
$i_1,\dots,i_k$ [@AEGS25 Not. 3.1]; there are nine of them,
$$
12,\quad 13,\quad 14,\quad 15,\quad 245,\quad 34,\quad 35,\quad 45,\quad 55 .
$$
So "cusp $35$" in part 2 is the $1$-cusp whose closure contains the $0$-cusps $3$ and $5$,
not the pair of $0$-cusps: part 2 is [@AEGS25 Lem. 5.7] verbatim, and the $0$-cusps $3$
and $5$ are strictly semitoroidal, as \longref{ex:fen2_five_cusps} records.
:::

::: {.Remark}

This theorem records the settled ambient degree-$2$ Enriques picture: the normalized KSBA compactification of $F_{\En, 2}$ coincides with an explicit semitoroidal model built from five folded semifans, one per $0$-cusp.
The proof runs through the K3 moduli space $F_{(2,2,0)}$ of the degree-$(2,2,0)$ problem, identifying $\overline{F_{\En, 2}}^\nu$ with a normalization of the closure of the relevant Noether--Lefschetz locus; see \longref{lem:fen2_normalization} for the corresponding period-domain statement.
:::

## Normalization inside $F_{(2,2,0)}$

::: {.Lemma #lem:fen2_normalization}
### Normalization of $F_{\En, 2}$

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

```{.tikz}
%%| filename: bb-boundary-correspondence
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz}
\usetikzlibrary{arrows.meta}
\begin{tikzpicture}[>={Stealth[round]}, thick, every node/.style={font=\small}]
  % the Enriques Baily--Borel boundary
  \node[circle,fill,inner sep=1.6pt,label=left:$2$]      (e2) at (0,3) {};
  \node[circle,fill,inner sep=1.6pt]                     (e1) at (6,3) {};
  \draw (e2) to[bend left=38]  node[above] {$12$}  (e1);
  \draw (e2) to[bend right=38] node[below] {$245$} (e1);
  \node at (3,3) {$\overline{F}_{\mathrm{En},2}^{\,\mathrm{BB}}$};
  \draw[purple] (e1) -- ++(35:0.9);
  \draw[purple] (e1) -- ++(-35:0.9);
  \node[right,xshift=6pt] at (e1) {$13,\ 14$};

  % the degree-(2,2,0) K3 Baily--Borel boundary
  \node[circle,fill,inner sep=1.6pt,label=left:$2$]      (k2) at (0,0) {};
  \node[circle,fill,inner sep=1.6pt]                     (k1) at (6,0) {};
  \draw (k2) to[bend left=38]  node[above] {$12\mathrm{A}$} (k1);
  \draw (k2) to[bend right=38] node[below] {$12\mathrm{B}$} (k1);
  \node at (3,0) {$\overline{F}_{(2,2,0)}^{\,\mathrm{BB}}$};
  \draw[purple] (k1) -- ++(35:0.9);
  \draw[purple] (k1) -- ++(-35:0.9);
  \node[right,xshift=6pt] at (k1) {$1\mathrm{A},\ 1\mathrm{B}$};

  % the map on 0-cusps
  \draw[->,red] (e2) ++(0,-0.35) -- ++(0,-2.3);
  \draw[->,red] (e1) ++(0,-0.35) -- ++(0,-2.3);
\end{tikzpicture}
```

The correspondence of Baily--Borel boundaries under $\Psi\colon F_{\En, 2}\to F_{(2,2,0)}$:
the $0$-cusps of $\overline{F_{\En,2}}^{\bb}$ (top) map to the $0$-cusps of
$\overline{F_{(2,2,0)}}^{\bb}$ (bottom), and the $1$-cusps to $1$-cusps, by
[@AEGS25 Lem. 3.2].
The $0$-cusps of $F_{(2,2,0)}$ are distinguished by the divisibility
$\mathrm{div}(e)\in\ts{1,2}$ of the isotropic vector, and the map is read off from the
divisibilities of Sterk's $e_1,\dots,e_5$ taken in $T_\En$ and in $T_\dP$ separately; the
Enriques $1$-cusps are labelled as in \longref{not:sterk-cusp-labels}.


## The five $0$-cusps

::: {.Example #ex:fen2_five_cusps}
### The five $0$-cusps of $\overline{F_{\En, 2}}$

The boundary of the KSBA compactification $\overline{F_{\En, 2}}$ has $27$ divisors across five
$0$-cusps: $6$ of Type II and $21$ of Type III [@AEGS25 Lem. 5.8].
The counts recorded per cusp below are *rays*, and a Type II divisor contributes one ray at
each $0$-cusp it meets, so the per-cusp Type II counts sum to $13$ rather than to $6$.
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

::: {.Remark}
The per-cusp counts above are exactly the ones of [@AEGS25 Lem. 5.8], obtained there from
the Coxeter-fan counts $4+4,\ 2+8,\ 3+15,\ 4+12,\ 5+17$ of [@AEGS25 Lem. 5.2] by
discarding the subgraphs with a connected component of irrelevant vertices. The Type III
counts $0,7,7,7,0$ sum to the $21$ distinct Type III divisors; the Type II counts
$2,2,2,4,3$ sum to $13$ rays carried by $6$ distinct Type II divisors, each of which is a
curve through several $0$-cusps.
:::

::: {.Remark}

This enumeration is the boundary data underlying the folded semifans $\mathcal{F}_\bullet$ of \longref{thm:fen2_main}: each $0$-cusp carries a reduced dual complex, a partition of its rays into the Type II (adjacent $1$-cusp) and Type III (deeper) strata, and the involution of its integral affine structure that folds the covering K3 data onto the Enriques data.
The precise per-cusp ray counts and IAS involutions are migrated from the working notes and, as with the cusp tables discussed in \longref{conj:ksba_semitoroidal_comparison}, should be regarded as provisional pending an independent cusp computation.
:::

## Folded Coxeter diagrams of the five cusps

::: {.Remark #rmk:fen2_folded_coxeter}
### Folded Coxeter diagrams of $F_{\En, 2}$

The five $0$-cusps of $F_{\En, 2}$ are expected to correspond to five distinct orbits of primitive isotropic vectors in $T_\En$, each realized as a folded image of a Coxeter diagram for $F_{(2,2,0)}$ under the involution $I = -I_\En$ (the root-folding criterion of \longref{lem:root-folding-tdp}, in the sense of \longref{def:folded-root}):

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

::: {.Remark}

The folded chamber $\mathfrak{C}^I = \mathfrak{C} \cap \overline{T}_{\eta, \mathbf{R}}^{I = 1}$ has walls defined by the roots descending from the covering domain (cf. the classical foldings of \longref{ex:classical-foldings}).

The polarized Coble boundary problem uses this folded Enriques data only as ambient input.
The extra marked-root refinement -- the admissibility test for Coble roots at a cusp and the restriction of the ramification semifan to the polarized Coble locus -- is recorded separately in \longref{que:coble_cusp_admissibility} and \longref{conj:restricted_ramification_semifan}.
:::
