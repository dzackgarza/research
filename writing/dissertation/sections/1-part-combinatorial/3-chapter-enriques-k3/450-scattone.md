### Enumerating Cusps

As a starting point to any compactification procedure of lattice polarized K3 surfaces $F_S$, we must first find the cusps of $\bbcpt{F}_S$.
We give an overview here of various methods in the literature for similar moduli spaces, and how their cusps can be found and studied.

#### $\ftd$: Degree 2d Polarized K3 Surfaces (Scattone's Description)

Let $\lkt$ denote the K3 lattice, and let $h \in \lkt$ be a primitive vector of square $2d > 0$.
The lattice orthogonal to the polarization is defined as
$$
T_{2d} \definedas  h^\perp_{\lkt} \cong \generators{-2d} \oplus U^{\oplus 2} \oplus E_8^{\oplus 2},
$$
which is even and of signature $(2,19)$.
The Type $\IV$ Hermitian symmetric period domain for $T_{2d}$,
$$
\halfpd{T_{2d}} = \theset{ [\omega] \in \PP(T_{2d, \CC} ) \st (\omega, \omega) = 0,\, (\omega, \bar{\omega}) > 0 },
$$
admits a natural right action by the arithmetic group $\Gamma_{2d} \subset \Orth^+(T_{2d})$, the intersection of the original orthogonal group with the subgroup stabilizing $h$ (and, if necessary, a choice of connected component).
The arithmetic quotient
$$
\ftd \definedas  \dmodgamma{ \halfpd{T_{2d}} }{ \Gamma_{2d} }
$$
is the coarse moduli space parametrizing degree $2d$ polarized K3 surfaces.

The Baily–Borel compactification $\bbcpt{\ftd}$ is projective, and its boundary strata correspond bijectively to $\Gamma_{2d}$-orbits of primitive isotropic sublattices of $T_{2d}$ of ranks $1$ and $2$.
More precisely, $0$-cusps are in correspondence with orbits of primitive isotropic lines and $1$-cusps with orbits of primitive isotropic planes, up to the action of $\Gamma_{2d}$.
The incidence relations between cusps are set by lattice inclusions: any $0$-cusp (an isotropic line) is contained in the closure of all $1$-cusps (isotropic planes) in which it lies.

As a concrete and illustrative case, set $d = 1$.
Then $h^2 = 2$ and
$$
T_2 = \generators{-2} \oplus U^{\oplus 2} \oplus E_8^{\oplus 2}.
$$
Scattone shows that for squarefree $d$ (in particular, $d = 1$), there is exactly one $\Gamma_{2d}$-orbit of primitive isotropic lines in $T_{2d}$, so the Baily–Borel boundary of $F_2$ has a unique $0$-cusp.

The 1-cusps are determined by the negative-definite lattices $\bdlattice{T}{2d, I} \definedas  I^{\perp T}/I$, for $I \subset T$ a primitive isotropic plane.
Alexeev--Engel--Thompson describe the $d=1$ case in the terms this chapter needs, citing Scattone for it: the boundary of $\bbcpt{F_2}$ consists of four curves meeting at a single point, the point is the Type $III$ boundary, and the curves correspond to four distinct orbits of rank $2$ primitive isotropic sublattices $J \subset h^\perp$; and, in their words, "for each of them, $J^\perp/J$ contains a finite index root sublattice, which can be used as a label for this $1$-cusp" [@AET23, §3B].
The four labels are
$$
A_{17}, \qquad D_{10}\oplus E_7, \qquad E_8^{\oplus 2}\oplus A_1, \qquad D_{16}\oplus A_1 .
$$
So the labels name root sublattices and not the boundary lattices: $J^\perp/J$ itself is what a $1$-cusp corresponds to, and each labelled lattice sits in it with finite index.

Alexeev--Engel--Thompson say what a cusp is, not only what its label is. The Coxeter diagram $G_{\text{cox}}$ of $N = H\oplus E_8^{\oplus 2}\oplus A_1$ is drawn on 24 roots, and up to $S_3$ it has exactly four maximal parabolic subdiagrams, the affine $\tilde A_{17}$, $\tilde D_{10}\tilde E_7$, $\tilde E_8^{\oplus 2}\tilde A_1$ and $\tilde D_{16}\tilde A_1$ of their Figure 1 [@AET23, Lem. 4.5]. By their Theorem 4.3 each of these corresponds to a null ray $\RR_{\ge 0}v$ of $N$ with $v^2 = 0$, and the $1$-cusp is the cone over that ray: with $I$ the unique $0$-cusp line and $\tilde v\in I^\perp$ a lift of $v$,
$$
J = I\oplus \ZZ\tilde v \subset T_2, \qquad J^\perp/J \cong v^\perp/\ZZ v \subset N .
$$
The label is then the finite diagram left by deleting the null root from the affine one, which is why the four labels of §3B are the four affine diagrams of the Coxeter fan reduced modulo that root. In these terms two of the four can be read off at once. Write $N = \generators{e,f}\oplus E_8^{\oplus 2}\oplus A_1$ with $e,f$ the isotropic basis of $H$. A vector of $N$ whose coefficient of $e$ is $1$ is isotropic exactly when it is $e + nf + w$ with $w\in E_8^{\oplus 2}\oplus A_1$ and $n = -w^2/2$; $w = 0$ gives $v = e$ and $v^\perp/\ZZ v = E_8^{\oplus 2}\oplus A_1$, the label of that cusp. Whether every one of the four null rays has a representative of this shape is a separate question, not needed for this one and not asserted here. The diagram gives the second: the first of the four small figures has the rim of the triangle black and the six interior nodes white, so the subdiagram is an $18$-cycle, an affine $A_{17}$, and its null root is the sum of the eighteen rim roots with all marks $1$; that the mark vector lies in the kernel of the rim Gram matrix and is isotropic is checked in `formalization/coble-enriques/CoxeterRim.lean` (`rim_mulVec_marks`, `rim_marks_isotropic`). Its ray gives the cusp labelled $A_{17}$. The four vertex subsets are transcribed from the figure's own vector artwork rather than from a raster reading: the e-print of [@AET23] assembles Figure 1 from five files, `fig-Vinberg` for the labelled diagram and `fig-wA17`, `fig-2wE8wA1`, `fig-wD10wE7`, `fig-wD16wA1` for the four small ones, in which the subdiagram's nodes are the black-filled disks. Reading the disks' coordinates against the labelled layout gives the subsets $\{0,\dots,17\}$ for $\tilde A_{17}$ (the rim), and the complements $\{8,16,21,22,23\}$, $\{3,12,21,22\}$, $\{2,4,20,21,22\}$ for $\tilde D_{10}\tilde E_7$, $\tilde E_8^{\oplus 2}\tilde A_1$ and $\tilde D_{16}\tilde A_1$; the transcription is `writing/coble/scripts/certificates/read_fig1.py`, which asserts that every black disk lands on a printed node position, and whose rim check reproduces the first subset. The marks of the other three are attached to the affine diagram's nodes and so still need the induced graph. Reading those edges off the same artwork gives the expected structure for one of them -- the eighteen rim vertices with eighteen edges, a cycle, as $\tilde A_{17}$ must be -- and not yet for the other three, where the extracted edge lists mix strokes that are not edges of $G_{\text{cox}}$ with edges that are missing; the cause is that the figure draws its edges as a few long polylines whose bend points need not be vertices. The marks will be taken from the affine Cartan type through the root-system API once the vertex correspondence is settled, not from a table written out here. The coordinates of the 24 roots are not printed in the source — Figure 1 gives the diagram and the intersection numbers, not the vectors — so the null vectors of the remaining two subdiagrams are a transcription of that figure and not a computation, and `writing/coble/scripts/certificates/cusps_degree_two.sage` holds the construction with those two entries left open rather than guessed.

Two things about $J^\perp/J$ follow without further input. It has rank $21-2\cdot 2 = 17$, since $J$ is maximal isotropic; and it is negative definite, again because $J$ is a maximal isotropic subspace of the space $h^\perp \otimes \RR$ of signature $(2,19)$.
Its determinant is $\det R/k^2$, where $R$ is the labelled root lattice and $k = [J^\perp/J : R]$, so the index and the determinant are one unknown per orbit. A second relation removes the unknown. Alexeev--Engel--Thompson show that an isotropic plane $J$ has a complementary isotropic plane $J'$, with $J' = \Hom(J,\ZZ)$ under the pairing, so that $J\oplus J' \cong U^{\oplus 2}$ [@AET23, Prop. 4.13]. That lattice is unimodular, and a unimodular sublattice of an integral lattice splits it orthogonally with no index: for every $x \in T_2$ the functional $y\mapsto x\cdot y$ on $J\oplus J'$ is realised by an element $w \in J\oplus J'$, so that $x - w \perp J\oplus J'$, with both $w$ and $x-w$ integral. Hence $J\oplus J'\oplus J^\perp/J$ is all of $T_2$ and not a proper sublattice, and
$$
\det(J^\perp/J) = \det(J\oplus J')^{-1}\det(T_2) = \det(T_2) = -2 .
$$
Both steps are formalized in `formalization/coble-enriques/Splitting.lean`: `splits_of_unimodular` is the splitting, whose integrality comes from `exists_mulVec_eq_of_unimodular` (the inverse of a unimodular integral matrix is integral), `det_eq_mul_of_unimodular_block_diagonal` is the determinant, and `det_hyperbolic4` is the $\det(J\oplus J') = \det(U^{\oplus 2}) = 1$ that makes the relation an equality and not merely equality of absolute values; the file also records that a scaled pairing fails the hypothesis. For the cusp $J = \generators{f_1,f_2}$ the quotient has rank $17$ and signature $(0,17)$, hence determinant $-2$ as computed, which agrees. So the index is forced, not free: with $\det R$ equal to $2$, $8$, $8$, $18$ it is $k = 1$ for $A_1\oplus E_8^{\oplus 2}$, $k = 2$ for $E_7\oplus D_{10}$ and for $A_1\oplus D_{16}$, and $k = 3$ for $A_{17}$.

All four are computed on the maintained Sage baseline, from the numbered roots of the source itself: $P$ is the presentation with the 24 generators and their Gram matrix, $P\to P/\rad P = N$ its radical quotient, and each cusp's plane comes from the source's null vector through that projection. The four boundary lattices come out the same shape and differ in the index of the label:

| cusp | label | $\det$ label | $J^\perp/J$ | $\det(J^\perp/J)$ | $A_{J^\perp/J}$ | $k$ |
| --- | --- | --- | --- | --- | --- | --- |
| $\tilde A_{17}$ | $A_{17}$ | $-18$ | rank $17$, sig $(0,17)$ | $-2$ | $\ZZ/2$ | $3$ |
| $\tilde D_{10}\tilde E_7$ | $D_{10}\oplus E_7$ | $-8$ | rank $17$, sig $(0,17)$ | $-2$ | $\ZZ/2$ | $2$ |
| $\tilde E_8^{\oplus 2}\tilde A_1$ | $E_8^{\oplus 2}\oplus A_1$ | $-2$ | rank $17$, sig $(0,17)$ | $-2$ | $\ZZ/2$ | $1$ |
| $\tilde D_{16}\tilde A_1$ | $D_{16}\oplus A_1$ | $-8$ | rank $17$, sig $(0,17)$ | $-2$ | $\ZZ/2$ | $2$ |

Every entry is negative definite and even, and the determinant is $-2$ in all four rows, which is the splitting lemma's prediction $\det(J^\perp/J) = \det(T_2)$ confirmed on the source data; the index that follows, $k = 1, 2, 2, 3$, is the one the lemma forces. The four scripts are `cusps_from_presentation.py`, `cusp_null_vectors.py`, `check_fig1_gram.py` and `read_fig1.py` in `writing/coble/scripts/certificates/`, with their transcripts beside them.

That row is computed, not only argued, on the maintained Sage baseline: for $J = \generators{f_1, f_2}$ in $T_2 = U\oplus U\oplus E_8^{\oplus 2}\oplus \generators{-2}$, the library's isotropic reduction of $J$ gives a lattice of rank $17$, signature $(0,17)$ and determinant $-2$, negative definite and even, whose single even overlattice inclusion has index $1$ from the label $A_1\oplus E_8^{\oplus 2}$; its discriminant module has order $2$ and invariant factors $[2]$, so the nontriviality of the discriminant is not the same thing as a glue index. The script is `writing/coble/scripts/certificates/cusps_degree_two_run.py` with its transcript beside it.

One row is thereby determined as a lattice. For $A_1\oplus E_8^{\oplus 2}$ the index is $1$, so the boundary lattice is the label itself; the two isotropic basis vectors $e_1, e_2$ of the two hyperbolic summands of $T_2$ realize this row, since $x\cdot e_1$ and $x\cdot e_2$ are the coefficients of $f_1$ and $f_2$, so that $J^\perp = \generators{a, e_1, e_2}\oplus E_8^{\oplus 2}$ and $J^\perp/J \cong \generators{-2}\oplus E_8^{\oplus 2}$. For the other three the index is $3$, $2$, $2$, and the lattice itself is not determined here: the discriminant group of $A_{17}$ is $\ZZ/18\ZZ$, in which the subgroup of order $3$ is unique, while those of $E_7\oplus D_{10}$ and of $A_1\oplus D_{16}$ are $(\ZZ/2)^{\oplus 3}$, which has several subgroups of order $2$. Enumerating the even overlattices a subgroup can give does not decide which one a cusp carries.

An index that must not be transferred here: for the Type $III$ stratum Alexeev--Engel--Thompson take $N = I^\perp/I = H\oplus E_8^{\oplus 2}\oplus A_1$ and $M = N^*$, and their Lemma 4.14 computes $M_G/R_G = \ZZ/6\ZZ$ for the $A_{17}$ root lattice inside $M$, and $\ZZ/2\ZZ$ for $A_{9}$, $A_{15}$, $D_{10}$, $D_{16}$ and others [@AET23, Prop. 4.13; @AET23, Lem. 4.14]. Those saturations live in $M = (I^\perp/I)^*$, the $0$-cusp's dual quotient, and not in the rank-$17$ lattice $J^\perp/J$ of a Type $II$ cusp, so no index for the four labels follows from them, and $6$ is in no case one of the values $k = 1, 2, 3$ that the splitting forces above.

Which even overlattice of its label each of those three boundary lattices is — the glue, and the discriminant form of $J^\perp/J$ — is not settled here. Scattone's own account is on pp.~78--80 with Proposition 6.1.1, and p.~81 with \S6.2; those pages were pointed out to me and have not been read, so nothing in this chapter rests on them.

#### Limiting mixed Hodge structures at the boundary

The cusp enumeration above is lattice-theoretic. That those cusps are the ones the period map reaches, and what Hodge-theoretic data each carries, is a separate matter, governed by the asymptotics of the period map and by limiting mixed Hodge structures, following @FS86. For a one-parameter degeneration $\mcx \to \Delta$ of polarized degree $2d$ K3 surfaces over a punctured disk $\Delta^*$, the unipotent monodromy operator $T \in O(T_{2d})$ determines the degeneration structure.
Its nilpotent logarithm $N = \log T \in \Endo(T_{2d, \QQ })$ induces the canonical monodromy weight filtration $\incfiltration{W}$ on $T_{2d, \QQ}$, uniquely characterized by the properties $N(W_k) \iscontainedin W_{k-2}$ for all $k$, and that for each $j > 0$, the maps $N^j: \Gr^W_{k+j} \to \Gr^W_{k-j}$ are isomorphisms.
Schmid's Nilpotent Orbit Theorem establishes that the period map asymptotically approaches a nilpotent orbit, defining a limiting Hodge filtration $\decfiltration{F^{\lim}}$ on $T_{2d, \CC}$ which, together with $\incfiltration{W}$, constitutes the limiting mixed Hodge structure (LMHS). This framework provides the connection between geometric degenerations and arithmetic lattice structures.

The boundary components of $\bbcpt{\ftd}$ are classified by the nilpotency index of $N$.
The Type $\II$ boundary components (1-cusps) correspond to degenerations where $N \neq 0$ but $N^2 = 0$.
For such degenerations, associated with a primitive isotropic plane $I \subset T_{2d}$, is a three-step monodromy weight filtration:
$$
0 = W_0 \subset W_1 = I_{\QQ} \subset W_2 = I^{\perp T_{2d}}_{\QQ} \subset W_3 = T_{2d, \QQ}
.$$
The LMHS induces a pure polarized Hodge structure of weight 2 on the graded piece $\Gr_2^W = I^{\perp}/I$, which is precisely the boundary lattice $\bdlattice{T}{I}$ arising in Scattone's combinatorial classification.
This identification reveals that $\bdlattice{T}{I}$ is not merely a lattice-theoretic invariant, but rather the natural target of the weight-2 component of the limiting mixed Hodge structure.

For Type $\III$ degenerations (0-cusps), where $N^2 \neq 0$ but $N^3 = 0$, the weight filtration is of maximal length.
The classifying space of such Hodge structures on $\bdlattice{T}{I}$ is itself a Type $\IV$ Hermitian symmetric domain $\halfpd{\bdlattice{T}{I}}$ and the boundary component itself is a modular variety $F_{\Gamma_I}$ for an appropriate arithmetic subgroup $\Gamma_I \leq \Orth^+(\bdlattice{T}{I})$.
These degenerations correspond to normal crossing varieties whose dual complex is a triangulation of $S^2$.
The computational accessibility of these mixed Hodge structures relies on several key tools developed in the work starting in @FS86: the Clemens-Schmid exact sequence relating the cohomology of central and $\mcx_t$s, and the Steenbrink weight spectral sequence, which for K3 surfaces degenerates integrally at the $E_2$-page.
This integral degeneration is a special property of K3 surface degenerations that enables explicit computation of the limiting mixed Hodge structure components.
The vanishing cycle analysis developed by Friedman and Scattone provides detailed control over how cohomology classes behave under degeneration.
Through Mayer-Vietoris techniques and careful analysis of the dual complex structure, they established the precise relationship between the geometric combinatorics of singular fibers and the arithmetic invariants encoded in LMHS. The stratification $\bbcpt{\ftd}$ is thus realized by the asymptotic behavior of the period map at the various boundary cusps.

#### $F_2$: Scattone's Description

For the specific case $d=1$, @Sca87 finds exactly four possible isometry classes for $\bdlattice{T}{I}$ determined by a 1-cusp $I$ adjacent to the unique 0-cusp $\eta$, distinguished by their root sublattices as defined above.
These correspond to the four distinct Type $\II$ modular curves in the boundary of $\bbcpt{F_2}$.
The unique 0-cusp $\eta$ correspond to a Type $\III$ component, and thus a degeneration where $N^2 \neq 0$ but $N^3=0$, yielding a weight filtration of maximal length.
The geometric inclusion of the 0-cusp in the closure of each 1-cusp reflects the lattice-theoretic fact that any primitive isotropic plane $I$ contains the primitive isotropic line $\eta$, all up to $\Gamma_{T_{2d}}$-invariance.
This incidence structure is encoded combinatorially in the Coxeter diagram of the lattice $\bdlattice{T}{2d, \eta}$ associated to the 0-cusp, whose maximal parabolic subdiagrams are in bijection with the possible isomorphism classes of the lattices $\bdlattice{T}{I}$ for the adjacent 1-cusps.

The cusps in $\bbcpt{F_2}$ are obtained by classifying primitive isotropic sublattices of the lattice
$$
T_{2} \definedas \generators{-2}\oplus U^{\oplus2}\oplus E_{8}^{\oplus2}
$$
using discriminant–form methods, from which Scattone shows:

- There is a single $\Gamma_{2}$-orbit of primitive isotropic lines $\eta$ in $T_2$, giving one 0-cusp (Type $\III$);

- There are four $\Gamma_{2}$-orbits of primitive isotropic planes $I$ in $T_2$, whose corresponding boundary lattices $\bdlattice{T}{I}$ are the rank-$17$, negative-definite lattices listed above, yielding four Type $\II$ boundary curves;

- These four curves meet transversely at the unique Type $\III$ point.

We assemble this data into the following **cusp diagram**:

::: {#fig:f2-cusp-diagram .figure}

\begin{tikzpicture}
\pic[cusp labels=eta] {object=bb-cusps/f2};
\end{tikzpicture}
The cusp diagram of $F_2$, the moduli space of degree 2 polarized K3 surfaces, which contains one 0-cusp $\eta$ adjacent to four 1-cusps.

:::

The general enumeration of $\bd\bbcpt{ F_{2d} }$ reduces to finite problems in the discriminant group $A_{T_{2d}}$: cusps can be classified by studying isotropic subgroups of the finite discriminant group $A_{T_{2d}} \definedas  (T_{2d})^*/T_{2d}$, and applying Nikulin's theorem that the genus of an even lattice is determined by its signature and the isomorphism class of its discriminant form [@Nik80]. The classification proceeds by associating to a primitive isotropic sublattice $I \subset T_{2d}$ an isotropic subgroup of $A_{T_{2d}}$.
The problem of classifying orbits of such sublattices under the infinite group $\Gamma_{2d}$ is thereby reduced to classifying orbits of isotropic subgroups of the finite group $A_{T_{2d}}$ under the action of a subgroup of $\discriminantcokernel{A_{T_{2d}}}$.
For the case $d=1$, the four isomorphism classes of the rank-$17$ lattice $\bdlattice{T}{I}$ are constructed by leveraging the classification of the $24$ Niemeier lattices: an isometry class of $\bdlattice{T}{I}$ is realized as the orthogonal complement $E_7^\perp \subset M$, where $M$ is a Niemeier lattice that admits a primitive embedding of the $E_7$ root lattice [@Sca87].
Three of the four are accounted for by the visible complements $A_{17}\subset A_{17}E_7$, $D_{10}\oplus E_7\subset D_{10}E_7^2$ and $A_1\oplus E_8^{\oplus2}\subset E_8^3$.
The fourth is not, and the reason is a limitation of the criterion rather than of the list: deleting nodes of a fixed simple-root diagram does not enumerate the root embeddings of a lattice.
The smallest witness is $D_7\subset E_8$, which exists — in the model of $E_8$ whose roots are the $\pm e_i\pm e_j$ and the half-spinors, the simple roots $e_1-e_2,\dots,e_6-e_7,e_6+e_7$ generate $D_7$ inside the coordinates $1,\dots,7$ — although $D_7$ is not a subdiagram of the standard $E_8$ diagram.
So the Niemeier description of Scattone's four lattices is not settled here, and the enumeration rests on the four root sublattices he lists rather than on that description.
For general $d$, cusp enumeration becomes a number-theoretic problem, since structure of $A_{T_{2d}}$ is highly dependent on the arithetic properties of $d$ itself, including various the numbers of solutions to various congruences, as well as the prime factorization of $d$.
@Sca87 uses these techniques to explicitly describe cusp diagrams for certain (sparse) families of values of $d$.
For further details and the explicit Coxeter diagrams, see [@Sca87, §6.2] and [@AET23, Fig. 2].


#### $\fell$: Elliptic Surfaces

The moduli space $\fell$ parametrizes elliptic K3 surfaces with a chosen section, a condition that fixes a primitive embedding of a hyperbolic plane $U_1 \subset \lkt$.
The relevant period map is thus defined on the orthogonal complement $\tell \definedas  U_1^{\perp_{\lkt}} \cong U^2 \oplus E_8^2$, and the moduli space is the 18-dimensional arithmetic quotient $\fell$.
A geometric description of the compactifications of $\fell$ is given in @ABE22, who construct KSBA compactifications and prove their isomorphism to specific semitoroidal compactifications.
There a unique $\fell$-orbit of 0-cusps in $\tell$, repsented by $\eta = e$, and the analysis falls on $\bar{(\tell)}_\eta \cong \II_{1, 17}$ Semitoroidal compactifications are defined by fans constructed in the rational closure $\thecone{C}_{\eta, \QQ}$ of the positive cone in $\II_{1, 17}$.
Two separate KSBA compactifications are constructed:

1. **The Ramification Divisor Compactification ($\cpt{F}^{\ram}$):** The polarization is given by the class of the ramification divisor $R$ from the representation of the K3 surface as a double cover of $\PP(1,1,4)$, so that $[R] = 3(s+2f)$, where $s$ is the section class and $f$ is the fiber class.
   This defines a KSBA compactification parametrizing pairs $(X, \epsilon R)$ with $X$ an slc K3 surface.

2. **The Rational Curve Divisor Compactification ($\cpt{F}^{\rcop}$):** The polarization is taken to be $R = s + m \Sum_{i=1}^{24} f_i$, where the $f_i$ are the 24 singular fibers of the elliptic fibration for a generic elliptic K3 surface.

The core result [@ABE22] is the identification of these KSBA moduli spaces with semitoroidal compactifications defined by specific fans in $\thecone{C}_{\QQ}$.
The fundamental fan is the **Coxeter fan** $F^{\cox}$, whose cones are the chambers of the reflection group $W(\II_{1,17})$.
The **ramification fan** $F^{\ram}$ is a coarsening of $F^{\cox}$ whose fundamental chamber is a union of four Coxeter chambers.
The **rational curve fan** $F^{\rcop}$ is a refinement of $F^{\cox}$ obtained by subdividing its fundamental chamber into nine sub-chambers.
@ABE22 prove that the normalizations of $\cpt{F}^{\ram}$ and $\cpt{F}^{\rcop}$ are isomorphic to the semitoroidal compactifications defined by the fans $F^{\ram}$ and $F^{\rcop}$, respectively, laying the groundwork for our main result on $\fentwo$.

The geometric models for the boundary strata are constructed using the theory of **integral-affine spheres with 24 singularities ($\IAS^2$)**. A Type $\III$ Kulikov degeneration of an elliptic K3 surface corresponds bijectively to a triangulated $\IAS^2$, and the monodromy of a one-parameter degeneration determines a vector $\lambda \in \thecone{C}_{\QQ}$, the **monodromy invariant**, which determines the combinatorial type of the stable limit $(X_0, \epsilon R)$ and is constant for all $\lambda$ within the interior of a cone of the relevant fan.
This provides a description of the boundary strata as unions of rational surfaces with prescribed singularities determined by the $\IAS^2$.

Its Baily–Borel boundary contains a unique 0-cusp and two 1-cusps.
The latter correspond to the two $\gell$-orbits of primitive isotropic planes $I \subset \tell$, distinguished by the isomorphism class of the negative-definite rank-16 lattice $\bdlattice{T}{I} = I^\perp/I$.
These two classes are $E_8 \oplus E_8$ and $D_{16}^+$, respectively, and the cusp diagram is as follows:

::: {#fig:fell-cusp-diagram .figure}

\begin{tikzpicture}
\pic[cusp labels=eta] {object=bb-cusps/fell};
\end{tikzpicture}
The cusp diagram of $\fell$, the moduli space of elliptic K3 surfaces, which contains one 0-cusp $\eta$ adjacent to two 1-cusps.

:::

#### $\fen$: Unpolarized Enriques Surfaces {#sec:fen-unpolarized-cusps}

The moduli space of *unpolarized* Enriques surfaces corresponds to the lattice $\ten$ and $\Gamma_{\En} \definedas \Orth^+(\ten)$, yielding the orthogonal modular variety $\fen$.
To enumerate the 0-cusps of $\bbcpt{\fen}$, one can replace $\ten$ by an auxiliary lattice $K = U \oplus E_8 \oplus \I_{1,1}$ and utilize a bijection
$$
\ten/\Orth(\ten) \cong K/\Orth(K)
,$$
allowing for a classification in terms of simpler lattices.
A primitive isotropic vector $\eta \in \I_{1,1}\subset K$ yields a unimodular lattice $\bdlattice{T}{\eta}$ of signature $(1,9)$.
There are precisely two such lattices up to isometry, $\I_{1, 9}$ and $\II_{1, 9}$.
Pulling back, some slightly finer analysis shows there are exactly two $\Gamma_{\En}$-orbits of primitive isotropic lines in $\ten$, corresponding to two 0-cusps $\eta_1, \eta_2$.
A direct approach for **1-cusps** is analytic: any isotropic plane $P \subset K$ must contain an odd primitive isotropic vector $\eta$, due to the indefinite form $\I_{1,1}$.
There is only one orbit of such under the full orthogonal group, so $P$ can always be assumed to contain $\eta$.
The remaining problem is to classify the possible isometry classes of primitive isotropic lines in $\bdlattice{T}{\eta} \cong \I_{1,9}$.
By examining the parities of a basis $\{w, w'\}$ for $P$, one finds two inequivalent types: planes where both generators have the same parity (even/even or odd/odd), and planes where the two have different parity (even/odd).
Hence, there are exactly two distinct $\Orth(\ten)$-orbits of primitive isotropic planes, corresponding to two 1-cusps.

Explicit representatives can be given as follows.
The 0-cusps correspond to the isotropic lines $\generators{e}$ and $\generators{e'}$, where $U = \generators{e,f}$ and $U(2) = \generators{e', f'}$ as sublattices of $\ten$.
The 1-cusps can be represented by the planes $\generators{e, e'}$, and $\generators{e', 2e + 2f + \alpha_1 + \alpha_2}$, where $\alpha_1, \alpha_2 \in E_8(2)$ are orthogonal roots of square $-4$.
We thus obtain the following cusp diagram:

::: {#fig:fen-unpolarized-cusp-diagram .figure}

\begin{tikzpicture}
\pic[cusp labels=none] (E) {object=bb-cusps/fen};
% The isotropic vectors spanning each cusp.
\foreach \c/\v in {E10/{\eta_1 = e}, E8/{I_{1,2} = \generators{e, e'}}, UE8/{\eta_2 = e'},
    D8/{I_2 = \generators{e', 2e + 2f + \alpha_1 + \alpha_2}}}
  {\node[below=2mm] at (E-\c.south) {$\v$};}
\end{tikzpicture}
The cusp diagram of $\fen$, the moduli space of unpolarized Enriques surfaces.

:::

##### Mirror Moves

All of the above situations involved somewhat ad-hoc analyses, which can be verified by computing the Coxeter-Vinberg diagrams $G(\Gamma_\eta)$ at the 0-cusps $\eta$ associated to the arithmetic subgroup $\Gamma$ and classifying their maximal elliptic and parabolic subdiagrams.
This can be computationally difficult, so we note a algorithm that can unify most of the above situations when $\Gamma$ is the full (stable) orthogonal group.
Let $T$ be a 2-elementary, nondegenerate, even unimodular lattice of signature $(2, n)$ embedding into the K3 lattice $\lkt$, let $\Gamma = \discriminantkernel{T}$, and consider the corresponding arithmetic quotient $\FG = \dmodgamma{ \halfpd{T} }{ \Gamma }$.
All such lattices are encoded in Nikulin’s pyramid diagram (see [@AE22]) of 2-elementary lattices.
The **cusp diagram** of $\cpt{F}_\Gamma$ is a labeled, directed graph whose vertices are boundary points and curves in $\cpt{F}_\Gamma$, corresponding (up to $\Gamma$-equivalence) with primitive isotropic vectors $\eta, I$ in $T$ and their associated boundary lattices $\bdlattice{T}{\eta}$, $\bdlattice{T}{I}$, with an edge $v_1 \to v_2$ between vertices if the corresponding boundary stratum $F_1$ is contained in the closure of $F_2$.
The cusp diagram is computed as follows.

A **mirror move** is a lattice-theoretic operation governed by the existence of a primitive isotropic vector $\eta \in T$ of a specified type and splitting as proved in @AE22:

- **Odd/simple:** $\div_T(\eta) = 1$, and $T \cong U \oplus K$

- **Even, ordinary:** $\div_T(\eta) = 2$ and $\eta^*$ is ordinary in $A_T$, and $T \cong U(2) \oplus K$

- **Even, characteristic:** $\div_T(\eta) = 2$ and $\eta^*$ is characteristic, and $T \cong I_{1,1}(2) \oplus K$

The move replaces $T$ with $\bdlattice{T}{\eta}$, computing the new invariants in each case.
A mirror move is only possible if the resulting lattice is realized (i.e., if the corresponding node exists in Nikulin's pyramid, see [@AE22, Fig. 1]) and admits the required splitting.

###### Step 1: Find All Orbits of $0$-Cusps $\eta$

1. **Start at the node $(r_0, a_0, \delta_0)$** in Nikulin’s pyramid associated to $T$.

2. **For every admissible mirror move,** check for outgoing arrows (*mirror moves*) from this node, corresponding to possible splittings of boundary lattices $T_{\eta_a}$ for isotropic vectors $\eta_a$.
   Each outgoing arrow from $(r_0, a_0, \delta_0)$ will be of one of the following types:
   
| Type of $\eta_a \in T$ | Destination $(r_1, a_1, \delta_1)$ | Splitting of $\bdlattice{T}{\eta_a}$ |
|---|---|---|
| Odd/simple | $(r_0-2,\, a_0,\, 1)$ | $U \oplus K$ |
| Even, ordinary | $(r_0-2,\, a_0-2,\, 1)$ | $U(2) \oplus K$ |
| Even, characteristic | $(r_0-2,\, a_0-2,\, 0)$ | $I_{1,1}(2) \oplus K$ |

**A $0$-cusp $\eta_a$ exists** if the arrow exists: the destination represents a realizable, hyperbolic, 2-elementary lattice $\bdlattice{T}{\eta_a}$ in Nikulin’s table, and the node at the head of the arrow gives the invariants $(r_1, a_1, \delta_1)$ of the boundary lattice $\bdlattice{T}{\eta_a}$.

###### Step 2: All $1$-Cusps and Incidence Structure

1. For each $0$-cusp $\eta_a$ determined in Step 1, recursively use $\bdlattice{T}{\eta_a}$ with invariants $(r_1, a_1, \delta_1)$ as a new starting point and consider all outgoing arrows from $(r_1, a_1, \delta_1)$ to construct $(r_2, a_2, \delta_2)$.
   Each move corresponds to a splitting of $\bdlattice{T}{I} \definedas  \overline{(T_{\eta_a})}_{\eta_b}$ for a primitive isotropic vector $\eta_b \in \bdlattice{T}{\eta_a}$:

| Type of $\eta_b \in \bdlattice{T}{\eta_a}$ | Destination $(r_2, a_2, \delta_2)$ | Splitting of $\bdlattice{T}{I} = \cpt{(T_{\eta_a})}_{\eta_b}$ |
|---|---|---|
| Odd/simple | $(r_1 - 2,\, a_1,\, \delta_1)$ | $U \oplus K'$ |
| Even, ordinary | $(r_1 - 2,\, a_1 - 2,\, \delta_1)$ | $U(2) \oplus K'$ |
| Even, characteristic | $(r_1 - 2,\, a_1 - 2,\, 0)$ | $I_{1,1}(2) \oplus K'$ |

2. **A $1$-cusp $I$ of type $(\eta_a, \eta_b)$ exists** if and only if the move $(r_1, a_1, \delta_1) \to (r_2, a_2, \delta_2)$ exists, corresponding to a 2-elementary lattice $\bdlattice{T}{I}$ with the specified invariants.
   The $1$-cusp $I$ is incident to $\eta_a$ if and only if it arises from such a two-step sequence.

###### Step 3: Diagram Extraction

The **nodes for $0$-cusps** are given by a single admissible mirror move from $(r_0, a_0, \delta_0)$, labeled by $(r_1, a_1, \delta_1)$, the corresponding lattice splitting, and the root system $\Phi(\bdlattice{T}{\eta})$.
The **nodes for $1$-cusps** are determined by two-step sequences $(r_0, a_0, \delta_0) \to (r_1, a_1, \delta_1) \to (r_2, a_2, \delta_2)$, with associated lattice splitting and root system $\Phi(\bdlattice{T}{I})$.
Each $1$-cusp is incident to every $0$-cusp $(r_1, a_1, \delta_1)$ that occurs as an intermediate node in such a sequence.
While the boundary lattice $\bdlattice{T}{I}$ for a $1$-cusp is determined up to isometry by invariants $(r_2, a_2, \delta_2)$, distinct $\Gamma$-orbits of $1$-cusps are distinguished by their root lattices $\Phi(\bdlattice{T}{I})$, either tabulated in @AE22 or computed via Vinberg’s algorithm.
We conclude by tabulating several useful references to use when carrying out this algorithm:

| Cusp | Invariants | Existence Condition |
|---|---|---|
| $0$-cusp $\eta$ | $(r_1, a_1, \delta_1)$ | $\exists\, (r_0, a_0, \delta_0) \to (r_1, a_1, \delta_1)$ |
| $1$-cusp $I$ | $(r_2, a_2, \delta_2)$, $\Phi(\bdlattice{T}{I})$ | $\exists\, (r_0, a_0, \delta_0) \to (r_1, a_1, \delta_1) \to (r_2, a_2, \delta_2)$ |

| Step 1 Type, $\eta_a$ | Step 2 Type, $\eta_b$ | $(r_1, a_1, \delta_1)$ | $(r_2, a_2, \delta_2)$ |
|---|---|---|---|
| Odd/simple | Odd/simple | $(r_0 - 2,\, a_0,\, 1)$ | $(r_0 - 4,\, a_0,\, 1)$ |
| Odd/simple | Even, ordinary | $(r_0 - 2,\, a_0,\, 1)$ | $(r_0 - 4,\, a_0 - 2,\, 1)$ |
| Odd/simple | Even, characteristic | $(r_0 - 2,\, a_0,\, 1)$ | $(r_0 - 4,\, a_0 - 2,\, 0)$ |
| Even, ordinary | Odd/simple | $(r_0 - 2,\, a_0 - 2,\, 1)$ | $(r_0 - 4,\, a_0 - 2,\, 1)$ |
| Even, ordinary | Even, ordinary | $(r_0 - 2,\, a_0 - 2,\, 1)$ | $(r_0 - 4,\, a_0 - 4,\, 1)$ |
| Even, ordinary | Even, characteristic | $(r_0 - 2,\, a_0 - 2,\, 1)$ | $(r_0 - 4,\, a_0 - 4,\, 0)$ |
| Even, characteristic | Odd/simple | $(r_0 - 2,\, a_0 - 2,\, 0)$ | $(r_0 - 4,\, a_0 - 2,\, 0)$ |
| Even, characteristic | Even, ordinary | $(r_0 - 2,\, a_0 - 2,\, 0)$ | $(r_0 - 4,\, a_0 - 4,\, 0)$ |
| Even, characteristic | Even, characteristic | $(r_0 - 2,\, a_0 - 2,\, 0)$ | $(r_0 - 4,\, a_0 - 4,\, 0)$ |

: Change of invariants under 2-step mirror moves.

Carrying out this algorithm for $\fen$ shows that there are exactly two 1-cusps and two 0-cusps.
The following diagram encodes the mirror-move procedure, recording a sequence of moves starting from a primitive sublattice $S\injects \lkt$, computing $T\definedas S^{\perp \lkt}$, finding $\bar{T}$, the first type of boundary lattice corresponding to a 1-step mirror move (corresponding to $0$-cusps) and finally finding $\overline{\bar T}$, the target of a 2-step mirror move.
We find that there are two possibilities for $\bar{T}$, indicated in the $\bar{T}$ column as $(10,10,0)_1$ and $(10, 8, 0)_1$, and two possibilities present in the $\overline{\bar{T}}$ column.
There are three 2-step paths through the diagram, but only two possibilities for $\overline{\bar{T}}$, yielding two $1$-cusps and two $0$-cusps.
We record the resulting cusp diagram below as well.

::: {#fig:fen-mirror-move-summary .figure}

\begin{tikzpicture}
\pic {object=mirror-moves/enriques};
\end{tikzpicture}

A concise summary of the mirror move algorithm applied to $\EnriquesInvariants_1$, corresponding to $\fen$.

:::

::: {#fig:fen-cusp-diagram-summary .figure}

\begin{tikzpicture}
\pic[cusp labels=eta] {object=bb-cusps/fen};
\end{tikzpicture}
The cusp diagram of $\fen$, indicating two 0-cusps $\eta_{1}, \eta_2$ and two 1-cusps $I_{1,2}, I_2$.
We note that this recovers the known cusp diagram shown in @sec:fen-unpolarized-cusps.

:::
