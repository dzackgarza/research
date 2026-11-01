### The Five Cusps {#sec:five-cusps}

This section provides an explicit, case-by-case analysis of the five 0-cusps of $\fentwo$, describing the structure of the corresponding semifans, dual complexes, integral-affine data, and involution symmetries arising in the boundary of the KSBA compactification, as described in @AEGS25. The semifans $\semifan{F}_k$ are defined by intersecting the ambient ramification semifan $\semifan{F}_{\ram}(\tdp)$ with the Enriques lattice subspace $\ten$, for each lattice polarization $\tdp$ occurring at a cusp.
By @sec:five-cusps, the resulting collection $\semifans{F} = \{\semifan{F}_k\}_{k=1}^{5}$ consists of generalized Coxeter semifans governing the semitoroidal structure at each cusp; the symbol $\semifan{F}_k$ is the one used throughout, and no other is.
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

Two symbols that look alike are used in different senses here and are kept apart throughout the chapter: $\Gamma$ is the arithmetic subgroup of $\Orth(T)$ of @sec:group-actions, fixed once and for all, and $\Gamma(\mcx_0)$ is the dual complex of the central fibre, a topological space. The parenthesis carries the whole distinction; a dual complex is never written $\Gamma$ alone, and the group is never written with an argument.

That there are five $0$-cusps is Sterk's count, not a convention of this chapter: for $L_- = H\oplus H(2)\oplus E_8(-2)$ the primitive isotropic vectors fall into five $\Gamma$-orbits, hence five $0$-cusps of the Baily--Borel compactification, and that is the enumeration the five subsections below run through. The transcription of his root data and the recomputation of the maximal parabolic subdiagrams are in `computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage`.
Let $(\mcz, \mcr_{\mcz})$ be a half-divisor model.
If a component $V_i \subset \mcz_0$ is covered by two irreducible components of $\mcx_0$, then (up to normalization) $V_i$ is isomorphic to both components.
If $V_i$ is instead covered by a single irreducible component $\widetilde{V}_i \subset \mcx_0$, then $\ienzero$ acts on $\widetilde{V}_i$ with exactly four fixed points, occurring as two pairs on double curves $\widetilde{D}_{ij}$, $\widetilde{D}_{ik}$.
We conclude this chapter with an analysis of the actual combinatorial data at each of the five zero cusps.
In particular, we exhibit orbit representatives of the maximal parabolic subdiagrams of each Coxeter diagram under diagram symmetries, which are the Type $\II$ rays, and the corresponding elliptic subdiagrams, which are in bijection with the Type $\III$ cones. The group is the one Alexeev--Engel--Garza--Schaffler write down: by [@Ste91] the induced groups acting on $e^\perp/e$ are $\Gamma_k = \Aut(G_r^k) \ltimes W(G_r^k)$, and their Lemma 5.2 counts the rays as a direct enumeration of the maximal parabolic and rank-$9$ elliptic subdiagrams of $G_r^k$ [@AEGS25, §5.1, Lem. 5.2]; the orbit counts below, taken under the labelled symmetries of the diagram, reproduce its numbers $4+4$, $2+8$, $3+15$, $4+12$, $5+17$. The passage between the two settings is not that the reflection factor fixes subdiagrams --- it acts on the fan, not on them --- but that $W(G_r^k)$ permutes the chambers, so every ray has a representative in the fundamental chamber, after which the residual ambiguity is $\Aut(G_r^k)$ permuting the subdiagrams: rays modulo $\Gamma_k$ are subdiagram classes modulo $\Aut(G_r^k)$, which is what Lemma 5.2 enumerates. Both counts are reproduced below for all five cusps, as the orbit counts of the one and of the other under the labelled symmetries of the diagram; the enumeration, the orbits, and the transport between this numbering and the reconstruction of Sterk's root data are in `computations/reports/sterk_type_iii_rays.py`. The symmetries meant are those of the Coxeter diagram itself, carrying each root to a root of the same square and preserving every pairing, and not the arithmetic group $\Gamma$ of @sec:group-actions: how the orbits of the one compare with the orbits of the other is not settled here, and the counts below are orbits of the diagram.
The semitoroidal rows below are the same two lists with the deletion rule of [@AEGS25, Lem. 5.8] applied --- a subdiagram carrying a connected component entirely of irrelevant roots is discarded --- and are recomputed that way, over the irrelevant sets of [@AEGS25, Def. 5.4] transported by the folding, in `computations/reports/sterk_semitoroidal_counts.py`; the finiteness of the irrelevant subgroup at each cusp, which decides whether the compactification is toroidal or strictly semitoroidal, is read from the inertia of the induced subdiagram in `computations/reports/sterk_irrelevant_inertia.py`.

#### Cusp 1

\begin{tikzpicture}
\pic[root labels, subdiagram={0,1,2,4,5,6,7,8,11}] (A) at (0,0) {object=coxeter/sterk-cusp-1};
\pic[root labels, subdiagram={0,1,3,4,5,6,7,8,10,11}] (B) at (6,0) {object=coxeter/sterk-cusp-1};
\pic[root labels, subdiagram={0,1,2,3,5,6,7,8,11}] (C) at (0,6) {object=coxeter/sterk-cusp-1};
\pic[root labels, subdiagram={0,1,2,3,4,5,6,7,9,10}] (D) at (6,6) {object=coxeter/sterk-cusp-1};
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,10,0)_1$ of $\fen$, and $\Gamma(\mcz_0) = \RP^2$.

- **Lattice Data:** $\bar{\tdp} = (18,2,0)_1 = U(2)\oplus E_8^2$, with symmetry $J$ given by $180^\circ$ rotation; invariant sublattice $\bar{\tdp}^{J=1} = U(2) \oplus E_8(2)$. Both lattices are checked against the maintained two-elementary API in `writing/coble/scripts/certificates/enriques_cusp_lattice_data.py`: $U(2)\oplus E_8^2$ has invariants $(18,2,0)$ and $U(2)\oplus E_8(2)$ has rank $10$ with invariants $(10,10,0)$, the invariant sublattice being the diagonal $E_8$ halved, of determinant $2^8$.

- **Semifan Structure:** The irrelevant subgroup is infinite, noting that it contains the Weyl group of $\tilde A_1$ due to the presence of $r_9, r_{10}$ which are images of irrelevant roots in the corresponding K3 diagram, so $\semifan{F}_1$ is a strict semifan and the compactification at this 0-cusp is strictly semitoroidal [@AEGS25, Lem. 5.6, Lem. 5.7].

- **Rays in the Coxeter compactification:** 4 Type $\II$ rays, corresponding to the four orbits of maximal parabolic subdiagrams, which counted with labels are the nine subdiagrams of the diagram of $v = e$ reduced by its symmetry group of order $4$; the four subdiagrams displayed above are one representative of each of these orbits. 4 Type $\III$ rays, corresponding to the four orbits of elliptic subdiagrams of rank $9$ --- the rank is the one the correspondence forces, $10 - 1$ for a ray in a lattice of rank $10$ [@AET23, Thm. 4.3], and it is the rank Alexeev--Engel--Garza--Schaffler enumerate [@AEGS25, Lem. 5.2] ---: here $v^\perp/\ZZ v$ has rank $10$ and signature $(1,9)$, so an elliptic subdiagram has rank at most $9$, and a Type $\III$ ray is one of these maximal negative definite subsystems. The total is 8 rays.

- **Rays in the Semitoroidal compactification:** 2 Type $\II$ rays, 0 Type $\III$ rays; a total of 2 rays [@AEGS25, Lem. 5.8].
  These correspond to subdiagrams for the Coxeter compactification above, where any subdiagram which has a connected component of irrelevant roots is removed.

- **IAS Symmetry:** $\lambda \in \thecone{C}^J$ if and only if $\ell_i = \ell_{8+i}$ ($i=0,\ldots,7$), $\ell_{16} = \ell_{18}$, $\ell_{17} = \ell_{19}$; involution acts as $180^\circ$ rotation on each hemisphere, swapping $P$ and $P^{\opop}$.

#### Cusp 2

\begin{tikzpicture}
\pic (A) [subdiagram={1,2,3,4,5,6,7,8,9}] at (0,0) {object=coxeter/vinberg-10-8-0};
\pic (B) [subdiagram={2,3,4,5,6,7,8,9,10}] at (0,-2.5) {object=coxeter/vinberg-10-8-0};
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,8,0)_1$ of $\fen$; $\Gamma(\mcz_0) = \DD^2$.

- **Lattice Data:** $\bar{\tdp} = (18,0,0)_1 = U \oplus E_8^2$, $J$ is a vertical reflection; the invariant sublattice is $U \oplus E_8(2)$.

- **Semifan Structure:** The irrelevant subgroup is $S_2$, thus $\semifan{F}_2$ is a fan, giving a toroidal compactification over this cusp [@AEGS25, Lem. 5.6, Lem. 5.7].

- **Rays in the Coxeter compactification:** 2 Type $\II$, 8 Type $\III$; 10 total.

- **Rays in the Semitoroidal compactification:** 2 type $\mathrm{II}$, 7 type $\mathrm{III}$; 9 total [@AEGS25, Lem. 5.8].

- **IAS Symmetry:** $\lambda$ in $\thecone{C}^J$ iff $\ell_i = \ell_{20-i}$ $(i=1,\ldots,9)$; involution flips both hemispheres about the vertical axis.

#### Cusp 3

\begin{tikzpicture}
\pic[root labels, subdiagram={1,2,3,4,5,6,7,9,10,11}] (A) at (0,0) {object=coxeter/sterk-cusp-3};
\pic[root labels, subdiagram={0,1,3,4,5,6,7,8,9,10}] (B) at (6.5,0) {object=coxeter/sterk-cusp-3};
\pic[root labels, subdiagram={0,1,2,3,4,5,6,7,8}] (C) at (13,0) {object=coxeter/sterk-cusp-3};
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,8,0)_1$; $\Gamma(\mcz_0) = \DD^2$.

- **Lattice Data:** $\bar{\tdp} = (18,2,0)_1 = U(2)\oplus E_8^2$, $J$ is diagonal reflection followed by $\alpha_{20}$ reflection; $\bar{\tdp}^{J=1} = U(2)\oplus E_8(2)$.

- **Semifan Structure:** The Irrelevant subgroup is infinite since it again contains $W(\tilde A_1)$ due to the presence of $r_{10}, r_{11}$, so $\semifan{F}_3$ is strictly semitoroidal [@AEGS25, Lem. 5.6, Lem. 5.7].

- **Rays in the Coxeter compactification:** 3 Type $\II$, 15 Type $\III$; 18 total.

- **Rays in the Semitoroidal compactification:** 2 Type $\mathrm{II}$, 7 Type $\mathrm{III}$; 9 total [@AEGS25, Lem. 5.8].

- **IAS Symmetry:** $\lambda$ in $\thecone{C}^J$ iff $\ell_i = \ell_{16-i}$ $(i=1,\ldots,7)$, $\ell_{17}=\ell_{19}$, $\ell_{20}=0$ (folding symmetry requires $\ell_{20}=0$); the involution acts as diagonal flip.

#### Cusp 4

\begin{tikzpicture}
\pic[root labels, subdiagram={1,2,3,4,5,6,7,9,10}] (A) at (0,0) {object=coxeter/sterk-cusp-4};
\pic[root labels, subdiagram={0,1,2,3,4,5,6,7,10}] (B) at (6,0) {object=coxeter/sterk-cusp-4};
\pic[root labels, subdiagram={0,1,2,3,4,5,6,7,8}] (C) at (0,6) {object=coxeter/sterk-cusp-4};
\pic[root labels, subdiagram={0,1,2,3,5,6,7,8,9,10}] (D) at (6,6) {object=coxeter/sterk-cusp-4};
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,8,0)_1$; $\Gamma(\mcz_0) = \DD^2$.

- **Lattice Data:** $\bar{\tdp} = (18,2,0)_1 = U(2)\oplus E_8^2$, $J$ is horizontal reflection; $\bar{\tdp}^{J=1} = U(2)\oplus E_8(2)$.

- **Semifan Structure:** The irrelevant subgroup is $W(A_1)\times W(A_1) \cong S_2^2$ which is finite, and thus $\semifan{F}_4$ is a fan and the compactification is toroidal [@AEGS25, Lem. 5.6, Lem. 5.7].

- **Rays in the Coxeter compactification:** 4 Type $\II$, 12 Type $\III$; 16 total.

- **Rays in the Semitoroidal compactification:** 4 Type $\mathrm{II}$, 7 Type $\mathrm{III}$; 11 total [@AEGS25, Lem. 5.8].

- **IAS Symmetry:** $\lambda$ in $\thecone{C}^J$ iff each hemisphere of $B(\ell)$ is symmetric under a horizontal flip; the involution reflects across this axis.

#### Cusp 5

\begin{tikzpicture}
\pic[root labels, subdiagram={0,1,2,3,4,5,6,7,12,13}] (A) at (0,0) {object=coxeter/sterk-cusp-5};
\pic[root labels, subdiagram={0,1,2,3,4,5,6,8,11}] (B) at (6,0) {object=coxeter/sterk-cusp-5};
\pic[root labels, subdiagram={0,2,3,4,5,6,8,9,11,12}] (C) at (12,0) {object=coxeter/sterk-cusp-5};
\pic[root labels, subdiagram={0,2,3,4,6,7,8,9,10,11}] (D) at (4,6) {object=coxeter/sterk-cusp-5};
\pic[root labels, subdiagram={1,2,3,5,6,7,8,9,10,11,12}] (E) at (10,6) {object=coxeter/sterk-cusp-5};
\end{tikzpicture}

- **Boundary Type:** Maps to cusp $(10,8,0)_1$; $\Gamma(\mcz_0) = \DD^2$.

- **Lattice Data:** $\bar{\tdp} = (18,2,0)_1 = U(2)\oplus E_8^2$, $J$ is composition of eight commuting reflections $\alpha_1,\ldots,\alpha_{15}$; $\bar{\tdp}^{J=1} = U(2)\oplus E_8(2)$.

- **Semifan Structure:** The irrelevant subgroup contains $W(\tilde A_1)$ due to $r_{12}, r_{13}$, thus $\semifan{F}_5$ is a semifan and this yields a semitoroidal compactification [@AEGS25, Lem. 5.6, Lem. 5.7].

- **Rays in the Coxeter compactification:** 5 Type $\II$, 17 Type $\III$; 22 total.

- **Rays in the Semitoroidal compactification:** 3 Type $\mathrm{II}$, 0 Type $\mathrm{III}$; 3 total [@AEGS25, Lem. 5.8].

- **IAS Symmetry:** $\lambda \in \thecone{C}^J$ iff $\ell_{2i+1}=0$ for $i=0,\ldots,7$; the involution flips hemispheres of $B(\lambda)$.

We conclude with the following summary:

| $\eta$ | $\Gamma(\mcz_0)$ | $W_{\irrelevant}$ | $\semifan{F}$ | Type $\mathrm{II}$ | Type $\mathrm{III}$ | Total |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | $\RP^2$ | Infinite | Semi. | 2 | 0 | 2 |
| 2 | $\DD^2$ | $S_2$ | Tor. | 2 | 7 | 9 |
| 3 | $\DD^2$ | Inf. | Semi. | 2 | 7 | 9 |
| 4 | $\DD^2$ | $S_2^2$ | Tor. | 4 | 7 | 11 |
| 5 | $\DD^2$ | Inf. | Semi. | 3 | 0 | 3 |

: Summary of the five cusps: dual complex, irrelevant Weyl group, semifan type, and boundary divisor counts.

