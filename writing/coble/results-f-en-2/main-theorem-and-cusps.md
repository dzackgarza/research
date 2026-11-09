# The moduli space $\fentwo$: main results

## The main theorem

::: {.theorem #thm:fen2_main title="Compactification of $\fentwo$"}

Let $\ksbacpt{\fentwo}$ denote the KSBA compactification of the moduli space $\fentwo$ of numerically polarized Enriques surfaces of degree $2$.
Let $\semitorfan = \theset{\semifan{F}_k}_{k=1}^5$ be the collection of folded semifans for the $0$-cusps.

1. The normalization $\normksbacpt{\fentwo}$ is isomorphic to the semitoroidal compactification $\semifancpt{\fentwo}{\semitorfan}$ [@AEGS25, Thm. 1.1].

2. This compactification is toroidal over the $0$-cusps $2$ and $4$, their adjacent $1$-cusps, and the $1$-cusp $35$, and strictly semitoroidal over all other cusps [@AEGS25, Lem. 5.7].

3. Let $B$ be the closure of the image of $\fentwo$ in $\ksbacpt{\fttz}$.
   There is a classifying morphism $\normalize{B}\to\ksbacpt{\fentwo}$, and it is finite [@AEGS25, proof of Thm. 5.9].
:::

::: {.notation #not:sterk-cusp-labels title="Two indexings of the boundary"}

The $0$-cusps carry Sterk's numbering $1,\dots,5$, as in the five-cusp example (@ex:fen2_five_cusps). A $1$-cusp is denoted $i_1\dots i_k$ when its closure contains the $0$-cusps $i_1,\dots,i_k$ [@AEGS25 Not. 3.1]; there are nine of them,
$$
12,\quad 13,\quad 14,\quad 15,\quad 245,\quad 34,\quad 35,\quad 45,\quad 55 .
$$
The $1$-cusp $35$ is the one whose closure contains the $0$-cusps $3$ and $5$, and the $0$-cusps $3$ and $5$ are strictly semitoroidal (@ex:fen2_five_cusps).
:::

## Normalization inside $\fttz$

::: {.lemma #lem:fen2_normalization title="Normalization of $\fentwo$"}

There exists a closed subscheme $X \subset \fttz$ such that $\fentwo$ is canonically isomorphic to the normalization of $X$.
:::

::: {.proof}

This is established via an algebraic morphism of period domains
$$
\Psi : \fentwo \to \fttz
$$
induced by the unique lattice embedding $\tilde\Psi : \ten \injects \tdp$ defined by
$$
\tilde\Psi(u_1, u_2, v) \definedas (u_1, u_2, v, v).
$$
Restricting $\Psi$ to its scheme-theoretic image $X$ yields a finite, birational map from the normal variety $\fentwo$ to $X$, which by Zariski's Main Theorem exhibits $\fentwo$ as the normalization of $X$.
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

The correspondence of Baily--Borel boundaries under $\Psi\colon \fentwo\to \fttz$: the $0$-cusps of $\bbcpt{\fentwo}$ (top) map to the $0$-cusps of $\bbcpt{\fttz}$ (bottom), and the $1$-cusps to $1$-cusps, by [@AEGS25 Lem. 3.2].
The $0$-cusps of $\fttz$ are distinguished by the divisibility $\mathrm{div}(e)\in\theset{1,2}$ of the isotropic vector, and the map is read off from the divisibilities of Sterk's $e_1,\dots,e_5$ taken in $\ten$ and in $\tdp$ separately; the Enriques $1$-cusps are labelled as in the Sterk cusp-label notation (@not:sterk-cusp-labels).

## The five $0$-cusps

::: {.example #ex:fen2_five_cusps title="The five $0$-cusps of $\ksbacpt{\fentwo}$"}

The boundary of the KSBA compactification $\ksbacpt{\fentwo}$ has $27$ divisors across five $0$-cusps: $6$ of Type II and $21$ of Type III [@AEGS25 Lem. 5.8].
The per-cusp counts below are counts of *rays*. A Type II divisor contributes one ray at each $0$-cusp it meets, so the per-cusp Type II counts sum to $13$, not to $6$.
These counts are obtained from the numbers $4+4$, $2+8$, $3+15$, $4+12$, $5+17$ of Type II and Type III rays of the Coxeter fans [@AEGS25, Lem. 5.2] by removing the subgraphs that contain a connected component of irrelevant vertices [@AEGS25, proof of Lem. 5.8].
Each item gives the topological type of the reduced dual complex $\Gamma(\mcz_0)$ [@AEGS25, Prop. 4.8], the numbers of Type II and Type III rays, and the integral-affine-structure (IAS) involution $\iota_{\En,\IA}$ [@AEGS25, Prop. 4.5].
The toroidal and semitoroidal cusps are those of @thm:fen2_main(2).

1. **Cusp 1**: Semitoroidal.
   $\Gamma(\mcz_0) = \RP^2$.
   $2$ Type II rays, $0$ Type III. IAS involution: $180^\circ$ rotation $+$ flip hemispheres.

2. **Cusp 2**: Toroidal.
   $\Gamma(\mcz_0) = \Dc^2$.
   $2$ Type II rays, $7$ Type III. IAS involution: vertical flip of both hemispheres.

3. **Cusp 3**: Semitoroidal.
   $\Gamma(\mcz_0) = \Dc^2$.
   $2$ Type II rays, $7$ Type III. IAS involution: diagonal flip.

4. **Cusp 4**: Toroidal.
   $\Gamma(\mcz_0) = \Dc^2$.
   $4$ Type II rays, $7$ Type III. IAS involution: horizontal flip.

5. **Cusp 5**: Semitoroidal.
   $\Gamma(\mcz_0) = \Dc^2$.
   $3$ Type II rays, $0$ Type III. IAS involution: flip hemispheres.
:::

## Folded Coxeter diagrams of the five cusps

::: {.proposition #prop:fen2-folded-coxeter title="Folded Coxeter diagrams of $\fentwo$"}

Let $e\in\ten$ be a primitive isotropic vector.
Let $\overline{T}_{\mathrm{En}} = e^\perp/e$ in $\ten$ and $\overline{T}_{\mathrm{dP}} = e^\perp/e$ in $\tdp$, so that $\overline{T}_{\mathrm{En}}\subset\overline{T}_{\mathrm{dP}}$.
Let $J = -\overline{I}_{\mathrm{En}}$ be the involution of $\overline{T}_{\mathrm{dP}}$ induced by $-\Ien$, whose $(+1)$-eigenspace is $\overline{T}_{\mathrm{En}}$ [@AEGS25, Def. 3.5].
The folded diagram $G(\overline{T}_{\mathrm{dP}})^J$ of the Coxeter diagram $G(\overline{T}_{\mathrm{dP}})$ has as nodes the folded roots $\alpha + J(\alpha)$ (@def:folded-root) of the simple roots $\alpha$ for which these vectors are roots of $\overline{T}_{\mathrm{En}}$ (@lem:root-folding-tdp) [@AEGS25, Def. 3.7].

1. Let $\mathfrak{C}$ be a chamber of $W(\Gamma_{\mathrm{dP},e})$ in the positive cone of $\overline{T}_{\mathrm{dP}}$ whose intersection with $\overline{T}_{\mathrm{En}}\otimes\RR$ has maximal dimension.
   Then $\mathfrak{C}^J = \mathfrak{C}\intersect\overline{T}_{\mathrm{En}}\otimes\RR$ is a fundamental chamber of $W(\Gamma_{\mathrm{En},2,e})$, and its Coxeter diagram is $G(\overline{T}_{\mathrm{dP}})^J$ [@AEGS25, Lem. 3.8].

2. The following five involutions $J$ give the folded diagrams of the five $0$-cusps, in Sterk's numbering.
   The simple roots $\alpha_k$ are numbered as in [@AEGS25, Fig. 5].

   | Cusp | $\overline{T}_{\mathrm{dP}}$ | Involution $J$ | $\overline{T}_{\mathrm{dP}}^{J=1}$ |
   | --- | --- | --- | --- |
   | $1$ | $(18,2,0)_1$ | rotation of the diagram by $180^\circ$ | $U(2)\oplus E_8(2)$ |
   | $2$ | $(18,0,0)_1$ | reflection $\alpha_k\mapsto\alpha_{20-k}$ of the diagram about the vertical line | $U\oplus E_8(2)$ |
   | $3$ | $(18,2,0)_1$ | reflection of the diagram about the diagonal, followed by the reflection in the root $\alpha_{20}$ | $U\oplus E_8(2)$ |
   | $4$ | $(18,2,0)_1$ | reflection of the diagram about a horizontal line | $U\oplus E_8(2)$ |
   | $5$ | $(18,2,0)_1$ | composition of the $8$ commuting reflections in the roots $\alpha_1,\alpha_3,\dots,\alpha_{15}$ | $U\oplus E_8(2)$ |

   [@AEGS25, Lem. 3.9, Lem. 3.10].

3. These five folded diagrams are precisely the Coxeter diagrams of the reflection groups $W(\Gamma_{\mathrm{En},2,e})$, for the isotropic vectors $e\in\ten$ up to $\Gamma_{\mathrm{En},2}$ [@AEGS25, Cor. 3.12].
:::
