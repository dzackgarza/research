# The moduli space $\fentwo$: main results

## The main theorem

The degree-six polarized Enriques model arising from Enriques' original construction has a stable-pair compactification described for a four-dimensional subfamily [@Sch22]. The full family has dimension ten, and the larger polarization complicates its boundary. Numerical degree two is the smallest positive degree for an Enriques polarization. Its universal K3 cover also has a nonsymplectic involution whose fixed locus contains a curve, so the stable-pair theory of K3 surfaces with such involutions applies [@AE22].

::: {.theorem #thm:fen2_main title="Compactification of $\fentwo$"}

Let $\ksbacpt{\fentwo}$ denote the KSBA compactification (@def:ksba-compactification) of the moduli space $\fentwo$ of numerically polarized Enriques surfaces (@def:enriques-surface) of degree (@def:graded-object) (@def:numerical-polarization) $2$.
Let $\semitorfan = \theset{\semifan{F}_k}_{k=1}^5$ be the collection of folded semifans for the $0$-cusps.

1. The normalization $\normksbacpt{\fentwo}$ is isomorphic to the semitoroidal compactification (@def:semitoroidal-compactification) $\semifancpt{\fentwo}{\semitorfan}$ [@AEGS25, Thm. 1.1].

2. This compactification is toroidal over the $0$-cusps $2$ and $4$, their adjacent $1$-cusps, and the $1$-cusp $35$, and strictly semitoroidal over all other cusps [@AEGS25, Lem. 5.7].

3. Let $B$ be the closure of the image of $\fentwo$ in $\ksbacpt{\fttz}$.
   There is a classifying morphism $\normalize{B}\to\ksbacpt{\fentwo}$, and it is finite [@AEGS25, proof of Thm. 5.9].
:::

::: {.notation #not:sterk-cusp-labels title="Two indexings of the boundary" defines="$i_1\dots i_k$"}

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
induced by the distinguished lattice embedding $\tilde\Psi : \ten \injects \tdp$ defined by
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

::: {.lemma #lem:enriques-embedding-chain title="Uniqueness of the period-lattice embedding chain"}

The chain of primitive embeddings (@def:primitive-embedding)
$$
\ten=U\oplus U(2)\oplus E_8(2)
\hookrightarrow \tdp=U\oplus U(2)\oplus E_8^2
\hookrightarrow \lkt
$$
is unique up to the action of $\Orth(\lkt)$ [@AEGS25, Lem. 2.4].
:::

::: {.proof}

Taking orthogonal complements turns this into the chain $U(2)\hookrightarrow U(2)\oplus E_8(2)\hookrightarrow\lkt$. Nikulin's primitive embedding theorem gives uniqueness of the second inclusion [@Nik79, Thm. 1.14.4]. After scaling by $2$, uniqueness of the first reduces to the embedding $U\hookrightarrow U\oplus E_8$: its perpendicular is $E_8$, which determines the embedding up to isometry. Every isometry of $\tdp$ extends to one of $\lkt$ by the gluing and surjectivity results of [@Nik79, Props. 1.5.2, 3.6.3]. Thus an isometry taking one embedded copy of $\ten$ to another extends over the full chain [@AEGS25, proof of Lem. 2.4].
:::

::: {.construction #cons:fen2-cusp-involutions title="The five cusp folding involutions" defines="cusp folding involution; $\overline{T}_{\mathrm{En}}$; $\overline{T}_{\mathrm{dP}}$; $J$"}

Let $e\in\ten$ be a primitive (@def:primitive-embedding) isotropic (@def:orthogonal-complement) vector.
Let $\overline{T}_{\mathrm{En}} = e^\perp/e$ in $\ten$ and $\overline{T}_{\mathrm{dP}} = e^\perp/e$ in $\tdp$, so that $\overline{T}_{\mathrm{En}}\subset\overline{T}_{\mathrm{dP}}$.
Let $J = -\overline{I}_{\mathrm{En}}$ be the involution of $\overline{T}_{\mathrm{dP}}$ induced by $-\Ien$, whose $(+1)$-eigenspace is $\overline{T}_{\mathrm{En}}$ [@AEGS25, Def. 3.5].
The five involutions $J$ below are numbered by the $0$-cusps in Sterk's numbering, and the simple roots $\alpha_k$ of the Coxeter--Vinberg diagram $G(\overline{T}_{\mathrm{dP}})$ (@def:coxeter-vinberg-diagram) are numbered as in [@AEGS25, Fig. 5].

| Cusp | $\overline{T}_{\mathrm{dP}}$ | Involution $J$ | $\overline{T}_{\mathrm{dP}}^{J=1}$ |
| --- | --- | --- | --- |
| $1$ | $(18,2,0)_1$ | rotation of the diagram by $180^\circ$ | $U(2)\oplus E_8(2)$ |
| $2$ | $(18,0,0)_1$ | reflection $\alpha_k\mapsto\alpha_{20-k}$ of the diagram about the vertical line | $U\oplus E_8(2)$ |
| $3$ | $(18,2,0)_1$ | reflection of the diagram about the diagonal, followed by the reflection in the root $\alpha_{20}$ | $U\oplus E_8(2)$ |
| $4$ | $(18,2,0)_1$ | reflection of the diagram about a horizontal line | $U\oplus E_8(2)$ |
| $5$ | $(18,2,0)_1$ | composition of the $8$ commuting reflections in the roots $\alpha_1,\alpha_3,\dots,\alpha_{15}$ | $U\oplus E_8(2)$ |

[@AEGS25, Lem. 3.9, Lem. 3.10].
:::

::: {.lemma #lem:enriques-folding-lifts title="Lifting a cusp folding involution"}

For each of the five involutions $J$ of $\overline T_{\mathrm{dP}}$ in @cons:fen2-cusp-involutions, $J$ lifts to an involution $I$ of $\tdp$ whose fixed lattice is $\ten$ [@AEGS25, Lem. 3.11].
:::

::: {.proof}

At cusp $2$, decompose $\tdp=U(2)\oplus\overline T_{\mathrm{dP}}$ and act trivially on the first factor. At cusp $1$, use $\tdp=U\oplus\overline T_{\mathrm{dP}}$ in the same way. At cusps $3$, $4$, and $5$, $\overline T_{\mathrm{dP}}=U(2)\oplus E_8^2$ has fixed lattice $U\oplus E_8(2)$, and the trivial extension does not have the required fixed lattice.

Write $U=\langle e,f\rangle$, with $e^2=f^2=0$ and $e\cdot f=1$. A section of $\overline T_{\mathrm{dP}}$ into $\ZZ e\oplus\overline T_{\mathrm{dP}}$ is given by $a\in\overline T_{\mathrm{dP}}^*$, sending $x$ to $x+a(x)e$. Its perpendicular in $\tdp$ is $\langle e,2f-2a\rangle$ when $a\notin\overline T_{\mathrm{dP}}$; here $(2f-2a)^2=4a^2$. Choose $a=e'/2$ for a standard isotropic (@def:orthogonal-complement) basis (@def:based-module) vector $e'$ of the $U(2)$ summand of $\overline T_{\mathrm{dP}}$. Its discriminant value is integral, so this perpendicular is $U(2)$. Act by $J$ on the chosen section and trivially on its perpendicular. The resulting fixed lattice is
$$
\tdp^{I=1}\cong U(2)\oplus\overline T_{\mathrm{dP}}^{J=1}
\cong U\oplus U(2)\oplus E_8(2)=\ten.
$$
The embedding-chain uniqueness of @lem:enriques-embedding-chain identifies this lift with the required involution on the period lattice [@AEGS25, proof of Lem. 3.11].
:::

::: {.proposition #prop:fen2-folded-coxeter title="Folded Coxeter diagrams of $\fentwo$"}

Let $e$, $\overline{T}_{\mathrm{En}}\subset\overline{T}_{\mathrm{dP}}$ and $J$ be as in @cons:fen2-cusp-involutions.
The folded diagram $G(\overline{T}_{\mathrm{dP}})^J$ of the Coxeter--Vinberg diagram $G(\overline{T}_{\mathrm{dP}})$ (@def:coxeter-vinberg-diagram) has as nodes the folded vectors $\beta_{[\alpha]}$ (@def:folded-root) of the simple roots $\alpha$ for which these vectors are roots of $\overline{T}_{\mathrm{En}}$ [@AEGS25, Def. 3.7].

1. Let $\mathfrak{C}$ be a chamber (@cons:chamber-cone) of $W(\Gamma_{\mathrm{dP},e})$ in the positive cone (@not:reflection-groups-sign-convention) of $\overline{T}_{\mathrm{dP}}$ whose intersection with $\overline{T}_{\mathrm{En}}\otimes\RR$ has maximal dimension.
   Then $\mathfrak{C}^J = \mathfrak{C}\intersect\overline{T}_{\mathrm{En}}\otimes\RR$ is a fundamental chamber of $W(\Gamma_{\mathrm{En},2,e})$, and its Coxeter--Vinberg diagram is $G(\overline{T}_{\mathrm{dP}})^J$ [@AEGS25, Lem. 3.8].

2. The five involutions $J$ of @cons:fen2-cusp-involutions give the folded diagrams of the five $0$-cusps, in Sterk's numbering [@AEGS25, Lem. 3.9, Lem. 3.10].

3. These five folded diagrams are precisely the Coxeter--Vinberg diagrams of the reflection groups (@def:reflection-group) $W(\Gamma_{\mathrm{En},2,e})$, for the isotropic vectors (@def:isotropic-subspace) $e\in\ten$ up to $\Gamma_{\mathrm{En},2}$ [@AEGS25, Cor. 3.12].
:::

::: {.proof}

The root-folding criterion @lem:root-folding-tdp identifies the folded walls (@not:coxeter-polytope-faces) with root hyperplanes of $\overline T_{\mathrm{En}}$. Intersecting a chamber of the ambient reflection group with $\overline T_{\mathrm{En}}\otimes\RR$ gives the chamber in (1): the hyperplane of $\alpha$ restricts to that of $\alpha+J\alpha$ when $J\alpha\ne\alpha$, and a nonempty wall has negative folded norm. At cusp $2$, the orbit (@def:group-orbit) sums $\alpha_k+\alpha_{20-k}$, $1\le k\le8$, span $E_8(2)$, while $\alpha_{10}$ and the isotropic vector of the diagram relation span an orthogonal $U$ [@AEGS25, proof of Lem. 3.9]. For cusp $1$, the folded diagram contains $\widetilde E_8(2)$: half its null root and the disjoint simple root span $U(2)$ orthogonal to $E_8(2)$. At cusp $3$, the $E_7A_1(2)$ subsystem has index (@def:index) $2$ in $E_8(2)$, while half the null root of $\widetilde A_1(2)$ and its disjoint root span $U$. The diagrams at cusps $4$ and $5$ start from $\widetilde D_8(2)$ and $\widetilde A_7\widetilde A_1(2)$, respectively [@AEGS25, proofs of Lems. 3.9–3.10, printed pp. 594–595].

Each $J$ lifts to $\tdp$ by @lem:enriques-folding-lifts, so the five chambers correspond to Enriques cusp reflection groups. Sterk's classification gives exactly five $0$-cusps [@Ste91, §4.3]; hence the list is exhaustive [@AEGS25, proof of Cor. 3.12].
:::

::: {#rmk:archived-diagram-symmetries .remark title="The diagram symmetries in the archived computation"}

The $22$ nodes of the $(18,2,0)_1$ diagram in @fig-k3-cusp-18-2-0-vinberg are numbered $v_1,\ldots,v_{22}$, where $v_i=\alpha_{i-1}$ in the canonical root coordinates. Its diagram automorphism group is the dihedral group $D_4$, generated by the following permutations:
$$
\begin{aligned}
\rho={}&(5,9,13,1)(6,10,14,2)(7,11,15,3)\\
      &\qquad(8,12,16,4)(18,19,20,17)(21,22),\\
s={}&(1,9)(2,8)(3,7)(4,6)(10,16)(11,15)(12,14)(17,19).
\end{aligned}
$$
The three involutions used in the archived folding calculation are $r=\rho^2$, $d=s$, and $h=s\rho$, with permutation products read from right to left. The source lists them as
$$
\begin{aligned}
r={}&(1,9)(2,10)(3,11)(4,12)(5,13)(6,14)(7,15)(8,16)(17,19)(18,20),\\
d={}&(1,9)(2,8)(3,7)(4,6)(10,16)(11,15)(12,14)(17,19),\\
h={}&(1,5)(2,4)(6,16)(7,15)(8,14)(9,13)(10,12)(17,18)(19,20)(21,22).
\end{aligned}
$$
The generators preserve the norm marks and all $25$ weighted edges of the canonical diagram. The archive's geometric labels for the direction of $\rho$ and the intended lattice involutions were left under review; the cusp foldings above use the lattice involutions of [@AEGS25, Lems. 3.9–3.10, printed p. 594].
:::

### Root coordinates behind the cusp diagrams

The archived coordinate calculation uses the negative definite $E_8$ root basis
$\alpha_1,\ldots,\alpha_8$ and a second copy $\alpha'_1,\ldots,\alpha'_8$.
Write $\bar\alpha_i$ and $\bar\alpha'_i$ for their pairing-dual bases,
and let $e\cdot f=1$ in $U$ and $e'\cdot f'=2$ in $U(2)$.
The following roots lie in the boundary lattice
$U(2)\oplus E_8\oplus E_8\subset U\oplus U(2)\oplus E_8\oplus E_8$.
Here $v_i$ is the vertex $i$ of @fig-k3-cusp-18-2-0-vinberg, or
$\alpha_{i-1}$ in the numbering of [@AEGS25, Fig. 5].

| Root | Vector | Root | Vector |
| --- | --- | --- | --- |
| $v_1$ | $\alpha'_8$ | $v_{12}$ | $\alpha'_3$ |
| $v_2$ | $e'+f'+\bar\alpha_1+\bar\alpha'_8$ | $v_{13}$ | $\alpha'_4$ |
| $v_3$ | $\alpha_1$ | $v_{14}$ | $\alpha'_5$ |
| $v_4$ | $\alpha_3$ | $v_{15}$ | $\alpha'_6$ |
| $v_5$ | $\alpha_4$ | $v_{16}$ | $\alpha'_7$ |
| $v_6$ | $\alpha_5$ | $v_{17}$ | $e'+\bar\alpha'_8$ |
| $v_7$ | $\alpha_6$ | $v_{18}$ | $\alpha_2$ |
| $v_8$ | $\alpha_7$ | $v_{19}$ | $e'+\bar\alpha_8$ |
| $v_9$ | $\alpha_8$ | $v_{20}$ | $\alpha'_2$ |
| $v_{10}$ | $e'+f'+\bar\alpha_8+\bar\alpha'_1$ | $v_{21}$ | $f'-e'$ |
| $v_{11}$ | $\alpha'_1$ | $v_{22}$ | $5e'+3f'+2\bar\alpha_2+2\bar\alpha'_2$ |

The $19$ roots of the other K3 cusp, with boundary lattice
$U\oplus E_8\oplus E_8$, have a parallel coordinate list:

| Roots | Vectors |
| --- | --- |
| $w_1,\ldots,w_7$ | $\alpha_1,\alpha_3,\alpha_4,\alpha_5,\alpha_6,\alpha_7,\alpha_8$ |
| $w_8,w_9,w_{10}$ | $e+\bar\alpha_8,\ f-e,\ e+\bar\alpha'_8$ |
| $w_{11},\ldots,w_{17}$ | $\alpha'_8,\alpha'_7,\alpha'_6,\alpha'_5,\alpha'_4,\alpha'_3,\alpha'_1$ |
| $w_{18},w_{19}$ | $\alpha_2,\alpha'_2$ |

The archived row for $v_{10}$ has $f$ in place of $f'$ and $\alpha'_1$
in place of $\bar\alpha'_1$. The corrected vector above has square
$-2$ and lies in $U(2)\oplus E_8^2$; the archived one has square $-4$
and pairs nontrivially with $e$, so it cannot be this boundary root.
The corrected lists agree with the root construction in
`sage_extensions.sterk.Sterk` and with all $231$ pairings of the
$22$-root diagram and all $171$ pairings of the $19$-root diagram
against [@AEGS25, Fig. 5] (`computations/reports/sterk_figure5_adjacency.py`).

For cusp $1$, the first seven folded roots are the paired simple roots
$\alpha_i+\alpha'_i$ for $i=1,3,4,5,6,7,8$. The next two are
$v_2+v_{10}=2e'+2f'+\bar\alpha_1+\bar\alpha'_1+\bar\alpha_8+\bar\alpha'_8$
and $v_{17}+v_{19}=2e'+\bar\alpha_8+\bar\alpha'_8$.
The remaining roots are $v_{21}$, $v_{22}$, and $v_{18}+v_{20}$.
Thus the archived cusp-$1$ table's use of $e,f$ in those two middle
rows is a coordinate error. For cusp $2$, the corresponding folded
roots are $w_1+w_{17},\ldots,w_8+w_{10}$, then $w_9$ and
$w_{18}+w_{19}$. For cusps $3$--$5$, the corrected fold sums are
recorded in the exact pairing audit, and the published parabolic
incidences appear in @sec-cusp-diagrams-by-moduli-space. The archived
partial tables have unresolved
entries and do not determine those foldings.

::: {#rmk:nagoya-completeness-calculation .remark title="The alternate completeness calculation in the Nagoya draft"}

The earlier manuscript also attempts to enumerate the five cusp involutions without Sterk's cusp count. It starts with involutions $J$ of the boundary lattices $U\oplus E_8^2$ and $U(2)\oplus E_8^2$ whose fixed lattice has rank $10$ and type $U(2)\oplus E_8(2)$ or $U\oplus E_8(2)$. Up to the cases constructed in [@AEGS25, Lems. 3.9–3.10, printed p. 594], its remaining candidates are: eight commuting root reflections in $U\oplus E_8^2$; a diagonal symmetry of $U(2)\oplus E_8^2$ followed by reflection in one of $\alpha_0,\alpha_8,\alpha_{16},\alpha_{18},\alpha_{20},\alpha_{21}$; and eight commuting root reflections in $U(2)\oplus E_8^2$. The draft reports a SageMath fixed-lattice check that rejects the first case and retains only $\alpha_{20}$ in the second and $\{\alpha_1,\alpha_3,\ldots,\alpha_{15}\}$ in the third. That calculation is recorded in the draft but has no independently checked computation here; the completeness assertion in @prop:fen2-folded-coxeter uses Sterk's classification.
:::
