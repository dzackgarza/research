### The Five Cusps {#sec:five-cusps}

This section provides an explicit, case-by-case analysis of the five 0-cusps of $\fent$, describing the structure of the corresponding semifans, dual complexes, integral-affine data, and involution symmetries arising in the boundary of the KSBA compactification, as described in @AEGS25.
The semifans $\semifan{F}_k$ are defined by intersecting the ambient ramification semifan $\semifan{F}_{\ram}(\tdp)$ with the Enriques lattice subspace $\ten$, for each lattice polarization $\tdp$ occurring at a cusp. By @sec:five-cusps, the resulting collection $\semifans{F} = \{\semifan{F}_k\}_{k=1}^{5}$ consists of generalized Coxeter semifans governing the semitoroidal structure at each cusp.
Each semifan encodes the stratified boundary behavior of the compactification via its rays (corresponding to degenerations of Types $\II$ and $\III$) and the folding symmetries inherited from involutions on the integral-affine structures.
Let $(\mcz, \mcr_{\mcz}) \to (C,0)$ be a half-divisor model for $F_{\En,2}$ as in Proposition 4.5. The following facts hold for each such degeneration:

- The fibers of $\mcz$ have semi-log-canonical (slc) singularities.

- $K_{\mcz} + \epsilon \mcr_{\mcz}$ is relatively big and nef over $C$.

- The boundary $\mcr_{\mcz}$ contains no log canonical centers.

We recall some notation:

- $\ien$: the fixed-point-free Enriques involution of the total space $\mcx$ in a K3 surface degeneration;

- $\ienzero$: the restriction to the $\mcx_0$; when $\ienzero$ acts freely, $\mcz_0 = \mcx_0/\ienzero$ is an Enriques surface;

- $\iota_{\En,\IA}$: the involution acting on the integral-affine sphere $\IAS^2$ $B(\ell)$ or the dual complex $\Gamma(\mcx_0)$ by folding.

A dual complex $\Gamma(\mcx_0)$ or sphere $B(\ell)$ is said to be of *Enriques type* if and only if it admits such an involution $\iota_{\En, \IA}$.
Let $(\mcz, \mcr_{\mcz})$ be a half-divisor model.
If a component $V_i \subset \mcz_0$ is covered by two irreducible components of $\mcx_0$, then (up to normalization) $V_i$ is isomorphic to both components.
If $V_i$ is instead covered by a single irreducible component $\widetilde{V}_i \subset \mcx_0$, then $\ienzero$ acts on $\widetilde{V}_i$ with exactly four fixed points, occurring as two pairs on double curves $\widetilde{D}_{ij}$, $\widetilde{D}_{ik}$.
We conclude this chapter with an analysis of the actual combinatorial data at each of the five zero cusps.
In particular, we exhibit orbit representatives of the maximal elliptic subdiagrams of each Coxeter diagram under diagram symmetries, which are in bijection with Type $\III$ cones:

#### Cusp 1

\def\cusponelabels{1}
\begin{tikzpicture}
  \cuspone{0}{0}
\draw[highlight edge] (n0) -- (n1) -- (n2) -- (n3) -- (n4) -- (n11);
\draw[highlight edge] (n6) -- (n7) -- (n0);
\draw[highlight edge] (n0) -- (n8);
  \cuspone{6}{0}
\draw[highlight edge] (n0) -- (n1) -- (n2) -- (n3);
\draw[highlight edge] (n5) -- (n6) -- (n7) -- (n0);
\draw[highlight edge] (n0) -- (n8);
	\draw[highlight edge] (n10) -- (n11);
  \cuspone{0}{6}
\draw[highlight edge] (n0) -- (n1) -- (n2) -- (n3) -- (n4) -- (n5);
\draw[highlight edge] (n7) -- (n0);
\draw[highlight edge] (n0) -- (n8);
\draw[highlight edge] (n11) -- (n4);
  \cuspone{6}{6}
\draw[highlight edge] (n0) -- (n1) -- (n2) -- (n3) -- (n4) -- (n5) -- (n6) -- (n7) -- (n0);
\draw[highlight edge] (n9) -- (n10);
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,10,0)_1$ of $\fen$, and $\Gamma(\mcz_0) = \RP^2$.

- **Lattice Data:** $\bar{\tdp} = (18,2,0)_1 = U(2)\oplus E_8^2$, with symmetry $J$ given by $180^\circ$ rotation; invariant sublattice $\bar{\tdp}^{J=1} = U(2) \oplus E_8(2)$.

- **Semifan Structure:** The irrelevant subgroup is infinite, noting that it contains the Weyl group of $\tilde A_1$ due to the presence of $r_9, r_{10}$ which are images of irrelevant roots in the corresponding K3 diagram, so $\mcf_1$ is a strict semifan and the compactification at this 0-cusp is strictly semitoroidal.

- **Rays in the Coxeter compactification:** 4 Type $\II$ rays corresponding to the 4 elliptic subdiagrams above; 4 type $\III$ rays corresponding to maximal parabolic subdiagrams; a total of 8 rays.

- **Rays in the Semitoroidal compactification:** 2 Type $\II$ rays, 0 Type $\III$ rays; a total of 2 rays. These correspond to subdiagrams for the Coxeter compactification above, where any subdiagram which has a connected component of irrelevant roots is removed.

- **IAS Symmetry:** $\lambda \in \thecone{C}^J$ if and only if $\ell_i = \ell_{8+i}$ ($i=0,\ldots,7$), $\ell_{16} = \ell_{18}$, $\ell_{17} = \ell_{19}$; involution acts as $180^\circ$ rotation on each hemisphere, swapping $P$ and $P^{\opop}$.

#### Cusp 2

\def\cusptwolabels{1}
\begin{tikzpicture}
  \cusptwo{0}{0}
\draw[highlight edge] (n8) -- (n6) -- (n9) -- (n6) -- (n1);
  \cusptwo{4}{0}
\draw[highlight edge] (n7) -- (n6) -- (n9) -- (n6) -- (n0);
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,8,0)_1$ of $\fen$; $\Gamma(\mcz_0) = \DD^2$.

- **Lattice Data:** $\bar{\tdp} = (18,0,0)_1 = U \oplus E_8^2$, $J$ is a vertical reflection; the invariant sublattice is $U \oplus E_8(2)$.

- **Semifan Structure:** The irrelevant subgroup is $S_2$, thus $\Sigma_2$ is a fan, giving a toroidal compactification over this cusp.

- **Rays in the Coxeter compactification:** 2 Type $\II$, 8 Type $\III$; 10 total.

- **Rays in the Semitoroidal compactification:** 2 type $\mathrm{II}$, 7 type $\mathrm{III}$; 9 total.

- **IAS Symmetry:** $\lambda$ in $\thecone{C}^J$ iff $\ell_i = \ell_{20-i}$ $(i=1,\ldots,9)$; involution flips both hemispheres about the vertical axis.

#### Cusp 3

\def\cuspthreelabels{1}
\begin{tikzpicture}
  \cuspthree{0}{0}
\draw[highlight edge] (n2) -- (n3) -- (n4) -- (n5) -- (n6) -- (n7) -- (n8);
\draw[highlight edge] (n5) -- (n9);
\draw[highlight edge] (n10) -- (n11);
  \cuspthree{5}{0}
\draw[highlight edge] (n2) -- (n3) -- (n4) -- (n5) -- (n6) -- (n7) -- (n8);
\draw[highlight edge] (n5) -- (n9);
\draw[highlight edge] (n8) -- (n1);
\draw[highlight edge] (n2) -- (n0);
  \cuspthree{10}{0}
  \draw[highlight edge] (n9) -- (n5) -- (n6) -- (n5) -- (n4) -- (n0);
\draw[highlight edge] (n8) -- (n1);
\draw[highlight edge] (n11) -- (n1);
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,8,0)_1$; $\Gamma(\mcz_0) = \DD^2$.

- **Lattice Data:** $\bar{\tdp} = (18,2,0)_1 = U(2)\oplus E_8^2$, $J$ is diagonal reflection followed by $\alpha_{20}$ reflection; $\bar{\tdp}^{J=1} = U(2)\oplus E_8(2)$.

- **Semifan Structure:** The Irrelevant subgroup is infinite since it again contains $W(\tilde A_1)$ due to the presence of $r_{10}, r_{11}$, so $\mcf_3$ is strictly semitoroidal.

- **Rays in the Coxeter compactification:** 3 Type $\II$, 15 Type $\III$; 18 total.

- **Rays in the Semitoroidal compactification:** 2 Type $\mathrm{II}$, 7 Type $\mathrm{III}$; 9 total.

- **IAS Symmetry:** $\lambda$ in $\thecone{C}^J$ iff $\ell_i = \ell_{16-i}$ $(i=1,\ldots,7)$, $\ell_{17}=\ell_{19}$, $\ell_{20}=0$ (folding symmetry requires $\ell_{20}=0$); the involution acts as diagonal flip.

#### Cusp 4

\def\cuspfourlabels{1}
\begin{tikzpicture}
  \cuspfour{0}{0}
\draw[highlight edge] (n1) -- (n2) -- (n3) -- (n4) -- (n5) -- (n6) -- (n7);
\draw[highlight edge] (n2) -- (n9);
\draw[highlight edge] (n6) -- (n10);
  \cuspfour{6}{0}
\draw[highlight edge] (n1) -- (n0);
\draw[highlight edge] (n1) -- (n2) -- (n3) -- (n4) -- (n5) -- (n6) -- (n7);
\draw[highlight edge] (n6) -- (n10);
  \cuspfour{0}{6}
\draw[highlight edge] (n1) -- (n0);
\draw[highlight edge] (n1) -- (n2) -- (n3) -- (n4) -- (n5) -- (n6) -- (n7) -- (n8);
  \cuspfour{6}{6}
\draw[highlight edge] (n1) -- (n0);
\draw[highlight edge] (n1) -- (n2) -- (n3);
\draw[highlight edge] (n5) -- (n6) -- (n7) -- (n8);
\draw[highlight edge] (n2) -- (n9);
\draw[highlight edge] (n6) -- (n10);
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,8,0)_1$; $\Gamma(\mcz_0) = \DD^2$.

- **Lattice Data:** $\bar{\tdp} = (18,2,0)_1 = U(2)\oplus E_8^2$, $J$ is horizontal reflection; $\bar{\tdp}^{J=1} = U(2)\oplus E_8(2)$.

- **Semifan Structure:** The irrelevant subgroup is $W(A_1)\times W(A_1) \cong S_2^2$ which is finite, and thus $\Sigma_4$ is a fan and the compactification is toroidal.

- **Rays in the Coxeter compactification:** 4 Type $\II$, 12 Type $\III$; 16 total.

- **Rays in the Semitoroidal compactification:** 4 Type $\mathrm{II}$, 7 Type $\mathrm{III}$; 11 total.

- **IAS Symmetry:** $\lambda$ in $\thecone{C}^J$ iff each hemisphere of $B(\ell)$ is symmetric under a horizontal flip; the involution reflects across this axis.

#### Cusp 5

\def\cuspfivelabels{1}
\begin{tikzpicture}
  \cuspfive{0}{0}
\draw[highlight edge] (n0) -- (n1) -- (n2) -- (n3) -- (n4) -- (n5) -- (n6) -- (n7) -- (n0);
\draw[highlight edge] (n12) -- (n13);
  \cuspfive{6}{0}
\draw[highlight edge] (n0) -- (n1) -- (n2) -- (n3) -- (n4) -- (n5) -- (n6) -- (n7) -- (n0);
\draw[highlight edge] (n2) -- (n9);
\draw[highlight edge] (n4) -- (n10);
  \cuspfive{12}{0}
\draw[highlight edge] (n0) -- (n1) -- (n2);
\draw[highlight edge] (n4) -- (n10);
\draw[highlight edge]  (n6) -- (n7) -- (n0);
\draw[highlight edge] (n2) -- (n9);
\draw[highlight edge] (n6) -- (n11);
\draw[highlight edge] (n12) -- (n13);
\draw[highlight edge] (n9) -- (n12);
\draw[highlight edge] (n11) -- (n12);
\draw[highlight edge] (n10) -- (n13);
  \cuspfive{4}{6}
\draw[highlight edge] (n2) -- (n3) -- (n4);
\draw[highlight edge] (n6) -- (n7) -- (n0);
\draw[highlight edge] (n0) -- (n8);
\draw[highlight edge] (n2) -- (n9);
\draw[highlight edge] (n4) -- (n10);
\draw[highlight edge] (n6) -- (n11);
  \cuspfive{10}{6}
\draw[highlight edge] (n1) -- (n2) -- (n3);
\draw[highlight edge] (n5) -- (n6) -- (n7);
\draw[highlight edge] (n2) -- (n9);
\draw[highlight edge] (n6) -- (n11);
\draw[highlight edge] (n8) -- (n13);
\draw[highlight edge] (n10) -- (n13);
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,8,0)_1$; $\Gamma(\mcz_0) = \DD^2$.

- **Lattice Data:** $\bar{\tdp} = (18,2,0)_1 = U(2)\oplus E_8^2$, $J$ is composition of eight commuting reflections $\alpha_1,\ldots,\alpha_{15}$; $\bar{\tdp}^{J=1} = U(2)\oplus E_8(2)$.

- **Semifan Structure:** The irrelevant subgroup contains $W(\tilde A_1)$ due to $r_{12}, r_{13}$, thus $\mcf_5$ is a semifan and this yields a semitoroidal compactification.

- **Rays in the Coxeter compactification:** 5 Type $\II$, 17 Type $\III$; 22 total.

- **Rays in the Semitoroidal compactification:** 3 Type $\mathrm{II}$, 0 Type $\mathrm{III}$; 3 total.

- **IAS Symmetry:** $\lambda \in \thecone{C}^J$ iff $\ell_{2i+1}=0$ for $i=0,\ldots,7$; the involution flips hemispheres of $B(\lambda)$.

We conclude with the following summary:

| $\eta$ | $\Gamma(\mcz_0)$ | $W_{\irrelevant}$ | $\semifan{F}$ | Type $\mathrm{II}$ | Type $\mathrm{III}$ | Total |
|--------|------------------|-------------------|---------------|--------------------|---------------------|-------|
| 1      | $\RP^2$          | Infinite          | Semi.         | 2                  | 0                   | 2     |
| 2      | $\DD^2$          | $S_2$             | Tor.          | 2                  | 7                   | 9     |
| 3      | $\DD^2$          | Inf.              | Semi.         | 2                  | 7                   | 9     |
| 4      | $\DD^2$          | $S_2^2$           | Tor.          | 4                  | 7                   | 11    |
| 5      | $\DD^2$          | Inf.              | Semi.         | 3                  | 0                   | 3     |

: Summary of the five cusps: dual complex, irrelevant Weyl group, semifan type, and boundary divisor counts.


<!-- CUSP DATA

#### # Cusp 1

- Coxeter diagram @fig:fen2-coxeter-1
- Relation to $\fen$: maps to cusp $(10,10, 0)_1$ in $\fen$
    - $\implies \Gamma(\mcz_0) = \RP^2$.
- $\bar{\tdp} = (18, 2, 0)_1 = U(2) \oplus E_8^2$
    - $J$: rotation by $180^\circ$
    - $\bar{\tdp}^{J=1} = U(2) \oplus E_8(2)$
- Semifan data:
    - The irrelevant subgroup is infinite.
    - $\mcf_1$ is a semifan, the compactification is semitoroidal.
- Diagram data
    - 2 type $\II$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-parabolic-1
    - 0 type $\III$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-ell-1
    - 2 total rays.
- IAS data
  - $\lambda \in \thecone{C}^J \iff$
      - $\lambda \in \thecone{C}^J$ if and only if
      - $\ell_i = \ell_{8+i}$ for all $i=0, \ldots, 7$,
      - $\ell_{16} = \ell_{18}$,
      - $\ell_{17} = \ell_{19}$.
  - $\iota_{\En, \IA} \actson B(\lambda):$
      - Rotate each hemisphere by $180^\circ$,
      - Then flip the two hemispheres $P$ and $P^{\opop}$.
  - $\iota_{\En, 0} \actson \Gamma(\mcz_0)$:
      - ?

#### # Cusp 2

- Coxeter diagram @fig:fen2-coxeter-2
- Relation to $\fen$: maps to cusp $(10,8, 0)_1$ in $\fen$
    - $\implies \Gamma(\mcz_0) = \DD^2$ (closed 2-disk).
- $\bar{\tdp}= (18, 0, 0)_1 = U \oplus E_8^2$
    - $J$: vertical reflection.
    - $\bar{\tdp}^{J=1} = U\oplus E_8(2)$
- Semifan data:
    - The irrelevant subgroup is $S_2$.
    - $\mcf_2$ is a fan, the compactification is strictly toroidal.
- Diagram data
    - 2 type $\II$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-parabolic-2
    - 7 type $\III$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-ell-2
    - 9 total rays.
- IAS data
    - $\lambda \in \thecone{C}^J \iff$
        - $\lambda \in \thecone{C}^J$ if and only if $\ell_i = \ell_{20-i}$ for all $i=1, \ldots, 9$.
    - $\iota_{\En, \IA} \actson B(\lambda):$
        - Flip both the hemisphere $P$ and its opposite $P^{\opop}$ across the vertical line bisecting the bottom and top edges.
    - $\iota_{\En, 0} \actson \Gamma(\mcz_0)$:
      - ? 

#### # Cusp 3

- Coxeter diagram @fig:fen2-coxeter-3
- Relation to $\fen$: maps to cusp $(10,8, 0)_1$ in $\fen$
    - $\implies \Gamma(\mcz_0) = \DD^2$.
- $\bar{\tdp} = (18, 2, 0)_1 = U(2) \oplus E_8^2$
    - $J$: diagonal reflection composed with a reflection in the root $\alpha_{20}$
    - $\bar{\tdp}^{J=1} = U(2) \oplus E_8(2)$
- Semifan data:
    - The irrelevant subgroup is infinite.
    - $\mcf_3$ is a semifan, the compactification is semitoroidal.
- Diagram data
    - 2 type $\II$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-parabolic-3
    - 7 type $\III$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-ell-3
    - 9 total rays.
- IAS data
- $\lambda \in \thecone{C}^J \iff$
    - $\lambda \in \thecone{C}^J$ if and only if
    - $\ell_i = \ell_{16-i}$ for all $i=1,\ldots,7$,
    - $\ell_{17} = \ell_{19}$,
    - $\ell_{20} = 0$.
      - This is because the folding symmetry reflecting in the root $\alpha_{20}$, since $w_{\alpha_{20}}(\lambda) = \lambda$ implies $\ell_{20} = \lambda \cdot \alpha_{20} = 0$.
      - $\ell_{20}$ measures the signed lattice distance between the two singularities from Symington surgeries on the edges parallel to $(1,-1)$ and $(-1,1)$. $B(\ell)$ is constructed so these two singularities coincide.
- $\iota_{\En, \IA} \actson B(\lambda):$
    - The involution $\iota_{\En, \IA}$ acts by flipping each hemisphere $P$ and $P^{\opop}$ diagonally.
- $\iota_{\En, 0} \actson \Gamma(\mcz_0)$:
    - ?


#### # Cusp 4

- Coxeter diagram @fig:fen2-coxeter-4
- Relation to $\fen$: maps to cusp $(10,8, 0)_1$ in $\fen$
    - $\implies \Gamma(\mcz_0) = \DD^2$.
- $\bar{\tdp} = (18, 2, 0)_1 = U(2) \oplus E_8^2$
    - $J$: horizontal reflection
    - $\bar{\tdp}^{J=1} = U(2) \oplus E_8(2)$
- Semifan data:
    - The irrelevant subgroup is $S_2^2$.
    - $\mcf_4$ is a fan, the compactification is strictly toroidal.
- Diagram data
    - 4 type $\II$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-parabolic-4
    - 7 type $\III$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-ell-4
    - 11 total rays.
- IAS data
- $\lambda \in \thecone{C}^J \iff$
    - $\lambda \in \thecone{C}^J$ if and only if
    - Each hemisphere of $B(\ell)$ is symmetric under a flip along the horizontal line bisecting the edges $\ell_6(0,1)$ and $\ell_{14}(0,-1)$.
    - TODO MAKE PRECISE
- $\iota_{\En, \IA} \actson B(\lambda):$
    - The involution is reflection across this horizontal axis of the hemisphere.
- $\iota_{\En, 0} \actson \Gamma(\mcz_0)$:
    - ?

#### # Cusp 5

- Coxeter diagram @fig:fen2-coxeter-5
- Relation to $\fen$: maps to cusp $(10,8, 0)_1$ in $\fen$
    - $\implies \Gamma(\mcz_0) = \DD^2$.
- $\bar{\tdp} = (18, 2, 0)_1 = U(2) \oplus E_8^2$
    - $J$: composition of 8 commuting reflections in the roots $\alpha_1, \cdots, \alpha_{15}$
    - $\bar{\tdp}^{J=1} = U(2) \oplus E_8(2)$
- Semifan data:
    - The irrelevant subgroup is infinite.
    - $\mcf_5$ is a semifan, the compactification is semitoroidal.
- Diagram data
    - 3 type $\II$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-parabolic-5
    - 0 type $\III$ rays, corresponding to elliptic subdiagrams in @fig:fen2-coxeter-ell-5
    - 3 total rays.
- IAS data
- $\lambda \in \thecone{C}^J \iff$
    - $\ell_{2i+1} = 0$ for $i = 0, \ldots, 7$.
    - The eight $\times$-marked nodes correspond to eight collisions of pairs of $I_1$ singularities along the equator of $B(\ell)$.
- $\iota_{\En, \IA} \actson B(\lambda):$
    - The involution $\iota_{\En, \IA}$ acts by flipping the two hemispheres $P$ and $P^{\opop}$ mirroring the extension of $\iota_{\dP}$ to $\mcx_0$.
- $\iota_{\En, 0} \actson \Gamma(\mcz_0)$:
    - ?

#### # Conclusion

- Semifan data:
    - 6 Type $\II$ rays,
    - 21 Type $\III$ rays,
    - 27 total rays,

\todo{Example
No explicit worked example of a Type III degeneration and its associated $\IAS^2$ is provided. Including at least one fully annotated example (e.g., standard toric, or a non-toric case) would clarify constructions.
}
 

-->
