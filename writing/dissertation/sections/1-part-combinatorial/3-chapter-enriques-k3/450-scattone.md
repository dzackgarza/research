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
admits a natural right action by the arithmetic group $\Gamma_{2d} \subset \Orth^+(T_{2d})$, the image of the subgroup of $\Orth(\lkt)$ consisting of the isometries that fix $h$ and have spinor norm $1$ [@AET23, §3A]. With the spinor norm in the normalisation whose kernel $\Orth^+$ is [@GHS08, §1], restriction to $h^\perp$ and extension across the discriminant gluing identify $\Gamma_{2d}$ with the stable orthogonal group $\widetilde{\Orth}^+(T_{2d})$. The sublattice $\ZZ h \oplus T_{2d}$ of $\lkt$ has index $2d$ and determinant $-(2d)^2$ in signature $(3,19)$, of absolute value $(2d)^2$, against the unimodular determinant of $\lkt$, with $A_{T_{2d}} \cong A_{\ZZ h} \cong \ZZ/2d$; $\lkt$ is recovered by adjoining the graph of an anti-isometry of those discriminant groups, and preserving that graph forces an isometry of $T_{2d}$ to act trivially on $A_{T_{2d}}$. An isometry of $T_{2d}$ therefore extends over $\lkt$ fixing $h$ exactly when it acts trivially on $A_{T_{2d}}$, and the spinor norm of the extension agrees with that of its restriction, the line $\ZZ h$ being positive definite and fixed pointwise.
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
For $d=1$, Alexeev--Engel--Thompson, following Scattone, describe the boundary as follows: the boundary of $\bbcpt{F_2}$ consists of four curves meeting at a single point, the point is the Type $III$ boundary, and the curves correspond to four distinct orbits of rank $2$ primitive isotropic sublattices $J \subset h^\perp$; and, in their words, "for each of them, $J^\perp/J$ contains a finite index root sublattice, which can be used as a label for this $1$-cusp" [@AET23, §3B].
The four labels are
$$
A_{17}, \qquad D_{10}\oplus E_7, \qquad E_8^{\oplus 2}\oplus A_1, \qquad D_{16}\oplus A_1 .
$$
Each label is a root sublattice of finite index in the boundary lattice $J^\perp/J$ of its $1$-cusp.

#### The Degree-Four Case

For $d = 2$, $h^2 = 4$ and
$$
T_4 = \generators{-4} \oplus U^{\oplus 2} \oplus E_8^{\oplus 2},
$$
of rank $21$ and signature $(2,19)$, and $\Gamma_4 = \widetilde{\Orth}^+(T_4)$. A Sage computation gives an isometry $T_4 \cong \Lambda_{19} = U^{\oplus 2} \oplus D_{17}$; both lattices have determinant $-4$ and discriminant module $\ZZ/4$.

The boundary is then the one Laza--O'Grady compute for quartic surfaces. Their Proposition A.4 splits every rank two saturated isotropic sublattice $J \subset \Lambda_{19}$ off a unimodular $U \oplus U$, with $J^\perp/J$ in the genus of $D_{17}$; Corollary A.5 identifies the image of the map $[J] \mapsto [J^\perp/J]$ with that genus, Proposition A.11 makes it injective at $N = 19$, and Theorem A.12 with its table gives nine Type II components [@LO21, App. A]. Since $\Gamma_4$ is the stable orthogonal group and the stable orthogonal group has the same orbits on primitive isotropic sublattices as the full orthogonal group --- the central $-1$ lies in $\Orth^+$, fixes every such sublattice setwise, and the component quotient is met by the element of their Lemma A.10(1), which fixes $J$ and reverses the orientation of the positive plane --- the $1$-cusps of $\bbcpt{F_4}$ are nine, in bijection with the nine lattices in the genus of $D_{17}$, which their Theorem A.6 lists by root sublattice. Unlike the degree two labels, these are the boundary lattices themselves: Proposition A.4 produces $J^\perp/J$ as one of the nine.

Alexeev--Engel--Thompson describe each $1$-cusp through the Coxeter diagram. The Coxeter diagram $G_{\text{cox}}$ of $N = H\oplus E_8^{\oplus 2}\oplus A_1$ is drawn on 24 roots, and up to $S_3$ it has exactly four maximal parabolic subdiagrams, the affine $\tilde A_{17}$, $\tilde D_{10}\tilde E_7$, $\tilde E_8^{\oplus 2}\tilde A_1$ and $\tilde D_{16}\tilde A_1$ of their Figure 1 [@AET23, Lem. 4.5]. By their Theorem 4.3 each of these corresponds to a null ray $\RR_{\ge 0}v$ of $N$ with $v^2 = 0$, and the $1$-cusp is the cone over that ray: with $I$ the unique $0$-cusp line and $\tilde v\in I^\perp$ a lift of $v$,
$$
J = I\oplus \ZZ\tilde v \subset T_2, \qquad J^\perp/J \cong v^\perp/\ZZ v \subset N .
$$
The label is then the finite diagram left by deleting the null root from the affine one, which is why the four labels of §3B are the four affine diagrams of the Coxeter fan reduced modulo that root. Two of the four null rays can be read off directly. Write $N = \generators{e,f}\oplus E_8^{\oplus 2}\oplus A_1$ with $e,f$ the isotropic basis of $H$. A vector of $N$ whose coefficient of $e$ is $1$ is isotropic exactly when it is $e + nf + w$ with $w\in E_8^{\oplus 2}\oplus A_1$ and $n = -w^2/2$; $w = 0$ gives $v = e$ and $v^\perp/\ZZ v = E_8^{\oplus 2}\oplus A_1$, the label of that cusp. For the second, the rim of the triangle in [@AET23, Fig. 1] is an $18$-cycle, an affine $A_{17}$, and its null root is the sum of the eighteen rim roots, all with mark $1$; its ray gives the cusp labelled $A_{17}$. In the numbering of the roots in [@AET23, Fig. 1], the four maximal parabolic subdiagrams have vertex sets $\{0,\dots,17\}$ for $\tilde A_{17}$, and the complements of $\{8,16,21,22,23\}$, $\{3,12,21,22\}$ and $\{2,4,20,21,22\}$ for $\tilde D_{10}\tilde E_7$, $\tilde E_8^{\oplus 2}\tilde A_1$ and $\tilde D_{16}\tilde A_1$.

The lattice $J^\perp/J$ has rank $21-2\cdot 2 = 17$, and it is negative definite, since $J$ is a maximal isotropic subspace of the space $h^\perp \otimes \RR$ of signature $(2,19)$.
Its determinant is $\det R/k^2$, where $R$ is the labelled root lattice and $k = [J^\perp/J : R]$. Alexeev--Engel--Thompson show that an isotropic plane $J$ has a complementary isotropic plane $J'$, with $J' = \Hom(J,\ZZ)$ under the pairing, so that $J\oplus J' \cong U^{\oplus 2}$ [@AET23, Prop. 4.13]. That lattice is unimodular, and a unimodular sublattice of an integral lattice is an orthogonal summand: for every $x \in T_2$ the functional $y\mapsto x\cdot y$ on $J\oplus J'$ is realised by an element $w \in J\oplus J'$, so that $x - w \perp J\oplus J'$, with both $w$ and $x-w$ integral. Hence $T_2 = (J\oplus J')\oplus (J\oplus J')^{\perp}$ with $(J\oplus J')^{\perp} \cong J^\perp/J$, and, since $\det(J\oplus J') = \det(U^{\oplus 2}) = 1$,
$$
\det(J^\perp/J) = \det(J\oplus J')^{-1}\det(T_2) = \det(T_2) = -2 .
$$
With $\det R$ equal to $2$, $8$, $8$, $18$, the index is $k = 1$ for $A_1\oplus E_8^{\oplus 2}$, $k = 2$ for $E_7\oplus D_{10}$ and for $A_1\oplus D_{16}$, and $k = 3$ for $A_{17}$.

The following table is computed in Sage from the 24 roots of [@AET23, Fig. 1]. Let $P$ be the lattice presented by the 24 generators and their Gram matrix, and $P\to P/\rad P = N$ its radical quotient. The plane of each cusp comes from the null vector of its parabolic subdiagram through that projection, and $S$ is the sublattice of $J^\perp/J$ spanned by the images of the label roots.

| cusp | label roots | $J^\perp/J$ | $\det$ | $S$, the span of the label roots in it | $\det S$ | $[J^\perp/J : S]$ | glue $A_S/\generators{\cdot}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $\tilde A_{17}$ | 18 | rank $17$, sig $(0,17)$ | $-2$ | rank $17$ | $-18$ | $3$ | $\ZZ/3$ |
| $\tilde D_{10}\tilde E_7$ | 19 | rank $17$, sig $(0,17)$ | $-2$ | rank $17$ | $-8$ | $2$ | $\ZZ/2$ |
| $\tilde E_8^{\oplus 2}\tilde A_1$ | 20 | rank $17$, sig $(0,17)$ | $-2$ | rank $17$ | $-2$ | $1$ | trivial |
| $\tilde D_{16}\tilde A_1$ | 19 | rank $17$, sig $(0,17)$ | $-2$ | rank $17$ | $-8$ | $2$ | $\ZZ/2$ |

Every boundary lattice is even and negative definite of determinant $-2$, as the splitting gives. The last three columns describe the inclusion $S\hookrightarrow J^\perp/J$: its index, and the gluing subgroup of that inclusion in $A_S$. The index is $3$, $2$, $1$, $2$ row by row, with $[J^\perp/J : S]^2 = \det S/\det(J^\perp/J)$, and the glue is trivial exactly in the row $E_8^{\oplus 2}\oplus A_1$, where the label is the boundary lattice.

For that row the boundary lattice can be written down. Write $T_2 = \generators{a}\oplus U\oplus U\oplus E_8^{\oplus 2}$ with $a^2 = -2$ and $e_i, f_i$ the isotropic basis of the $i$-th summand $U$, and let $J = \generators{e_1, e_2}$. Then $x\cdot e_i$ is the coefficient of $f_i$ in $x$, so $J^\perp = \generators{a, e_1, e_2}\oplus E_8^{\oplus 2}$ and $J^\perp/J \cong \generators{-2}\oplus E_8^{\oplus 2}$. In the other three rows, $J^\perp/J$ is the overlattice of $S$ that corresponds to the gluing subgroup in the table.

The saturation indices of [@AET23, Lem. 4.14] are different invariants. There $N = I^\perp/I = H\oplus E_8^{\oplus 2}\oplus A_1$ and $M = N^*$, and $M_G/R_G = \ZZ/6\ZZ$ for the $A_{17}$ root lattice inside $M$, and $\ZZ/2\ZZ$ for $A_{9}$, $A_{15}$, $D_{10}$, $D_{16}$ and others [@AET23, Prop. 4.13; @AET23, Lem. 4.14]. These saturations are taken in $M = (I^\perp/I)^*$, the dual of the $0$-cusp quotient, and not in the rank-$17$ lattice $J^\perp/J$ of a Type $II$ cusp; for $A_{17}$ the index in $M$ is $6$, and the index $k$ in $J^\perp/J$ is $3$.

#### Limiting mixed Hodge structures at the boundary

The Hodge-theoretic data at each cusp are governed by the asymptotics of the period map and by limiting mixed Hodge structures, following @FS86. For a one-parameter degeneration $\mcx \to \Delta$ of polarized degree $2d$ K3 surfaces over a punctured disk $\Delta^*$, the unipotent monodromy operator $T \in O(T_{2d})$ determines the degeneration structure.
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
The Baily–Borel stratum at such a cusp is a single point [@AET23, §3B]: it is neither a modular variety nor a period domain.
The lattice attached to the cusp is $\bdlattice{T}{\eta} = \eta^\perp/\eta$, of rank $19$ and signature $(1,18)$.
Over the boundary point lie the lattice $\eta^\perp/\eta$, with the polarized Hodge structure of weight $2$ that the limiting mixed Hodge structure places on it, and the fan data, which is a choice although the stratum is zero dimensional. Alexeev--Engel--Thompson put the fan there explicitly: for a $0$-cusp $I$ the lattice $\Lambda_I = I^\perp/I$ has signature $(1,18)$, its positive cone $C_I$ has a rational closure $\overline{C}_I$, and $F_I$ is a collection of closed convex rational polyhedral cones supported on $\overline{C}_I$, locally finite on $C_I$ and invariant under $\Gamma_I$ with finitely many orbits [@AET23, §3C]; for the unique $0$-cusp of $F_2$ they take it to be the Coxeter fan [@AET23, §4A, §4C]. The codimension of a stratum in the Baily--Borel compactification differs from its codimension in the toroidal one. The toric boundary of $X(F_I)$ is built from the cones of $F_I$: a ray of $F_I$ lying in the open positive cone $C_I$ has positive square and contributes a toric divisor, whose image under $\overline{F}_{2d}^{\,tor} \to \overline{F}_{2d}^{\,BB}$ lies over the Type $III$ point $P_I$; a *null* ray lies on the rational boundary $\overline{C}_I \setminus C_I$ rather than in the open cone, and the strata of $X(F_I)$ that Alexeev--Engel--Thompson's open set $V_I$ does not fully contain are exactly those of the null rays and the origin [@AET23, §3C]. The Type $II$ attachment is indexed by the norm of a ray, not by the dimension of a cone: the strata are described through the Coxeter diagram, an elliptic subdiagram giving the torus quotient $\operatorname{Hom}(M_G, \CC^*)/S_G \ltimes W(G)$ and a maximal parabolic one the fibre product $\mathcal{E}^{17} \to \mathcal{A}_1^{j}$, these being the Type $III$ and the Type $II$ strata respectively [@AET23, Prop. 4.13].
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

The orbit of a primitive isotropic sublattice $I \subset T_{2d}$ is classified by the quotient $J = I^\perp/I$ together with the gluing of $J$ into $T_{2d}$. When $I$ is a plane, $J$ is negative definite of rank $\rank T_{2d} - 4$. For the lattices $\Lambda_N = U^2\oplus D_{N-2}$ with $3 \le N$, a rank two *saturated* isotropic $I$ for which $\Lambda_N \to \operatorname{Hom}(I,\ZZ)$ is surjective sits inside a unimodular $U\oplus U$ with $\Lambda_N = (U\oplus U)\oplus L$ [@LO21, Prop. A.4 (1)], and this surjectivity holds for every saturated $I$ when $N \not\equiv 2 \pmod 8$. Then $J \cong L$, $A_{\Lambda_N} \cong A_L$ because $U\oplus U$ is unimodular, and the gluing is the isometry class of the embedding $L \subset \Lambda_N$. This applies to $T_4 \cong \Lambda_{19}$, since $19 \equiv 3 \pmod 8$.

The discriminant group does not separate the orbits. At $d = 1$ there are four orbits, while $A_{T_2} \cong \ZZ/2$ has one nonzero element, the class of $a/2$ with $a^2 = -2$, and its discriminant square $-1/2 \bmod 2\ZZ$ is nonzero; so $A_{T_2}$ has only the trivial isotropic subgroup. At $d = 2$ the nine orbits of [@LO21, Thm. A.12] lie in one genus of rank-$17$ lattices, and the isometry class of $J$ separates them, since $[I] \mapsto [J]$ is injective [@LO21, Prop. A.11]. By Nikulin's theorem, the signature and the discriminant form of an even lattice determine its genus [@Nik80]; equality of genera is therefore necessary, and not sufficient, for two orbits to coincide.
For general $d$, cusp enumeration becomes a number-theoretic problem, since structure of $A_{T_{2d}}$ is highly dependent on the arithetic properties of $d$ itself, including various the numbers of solutions to various congruences, as well as the prime factorization of $d$.
@Sca87 uses these techniques to explicitly describe cusp diagrams for certain (sparse) families of values of $d$.
For further details and the explicit Coxeter diagrams, see [@Sca87, §6.2] and [@AET23, Fig. 2].


#### $\fell$: Elliptic Surfaces

The moduli space $\fell$ parametrizes elliptic K3 surfaces with a chosen section, a condition that fixes a primitive embedding of a hyperbolic plane $U_1 \subset \lkt$.
The relevant period map is thus defined on the orthogonal complement $\tell \definedas  U_1^{\perp_{\lkt}} \cong U^2 \oplus E_8^2$, and the moduli space is the 18-dimensional arithmetic quotient $\fell$.
A geometric description of the compactifications of $\fell$ is given in @ABE22, who construct KSBA compactifications and prove their isomorphism to specific semitoroidal compactifications.
There a unique $\fell$-orbit of 0-cusps in $\tell$, repsented by $\eta = e$, and the analysis falls on $\overline{(\tell)}_\eta \cong \II_{1, 17}$ Semitoroidal compactifications are defined by fans constructed in the rational closure $\thecone{C}_{\eta, \QQ}$ of the positive cone in $\II_{1, 17}$.
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
The 0-cusps and 1-cusps of $\bbcpt{\fen}$ are the $\Gamma_{\En}$-orbits of primitive isotropic lines and planes in $\ten$.

::: {.proposition #prop:fen-two-zero-cusps title="The 0-cusps of the unpolarized Enriques moduli space"}

The lattice $\ten$ has exactly two $\Gamma_{\En}$-orbits of primitive isotropic lines. They are the odd class, represented by the isotropic generator $e$ of the $U$ summand, and the even ordinary class, represented by the isotropic generator $e'$ of the $U(2)$ summand. The corresponding boundary lattices are
$$
\bdlattice{T}{e} \cong U(2)\oplus E_8(2) = (10,10,0)_1,
\qquad
\bdlattice{T}{e'} \cong U\oplus E_8(2) = (10,8,0)_1,
$$
which are not isometric. Hence $\bbcpt{\fen}$ has exactly two 0-cusps, $\eta_1 \definedas e$ and $\eta_2 \definedas e'$.
:::

::: {.proof}

The lattice $\ten$ is even $2$-elementary of invariants $(12,10,0)_2$: its discriminant group is $A_{\ten} = \tfrac12 M/M \cong (\ZZ/2)^{10}$ with $M \definedas U(2)\oplus E_8(2)$, and $q_{\ten}$ takes integral values on it, because $x^2 \in 4\ZZ$ for every $x \in M$, so that $q_{\ten}(x/2) = x^2/4 \in \ZZ$. Hence $\delta(\ten) = 0$ in the sense of @thm:two-elementary-classification, the functional $q_{\ten} \bmod \ZZ$ vanishes, and $A_{\ten}$ has no nonzero characteristic class: such a class $x$ would satisfy $\bar\beta(x,y) = q_{\ten}(y)\bmod\ZZ$ for every $y$, so it would lie in the radical of a nondegenerate form. The third case of [@AE22, Prop. 5.5] requires $\delta = 1$ and therefore does not occur, and every primitive isotropic vector of $\ten$ is of the first or the second type.

The first type gives $\ten \cong U \perp \bdlattice{T}{\eta}$ with $\bdlattice{T}{\eta}$ of signature $(1,9)$ and invariants $(10,10,0)$, and the second gives $\ten \cong U(2)\perp \bdlattice{T}{\eta}$ with $\bdlattice{T}{\eta}$ of signature $(1,9)$ and invariants $(10,8,0)$. Both lattices exist, namely $U(2)\oplus E_8(2)$ and $U\oplus E_8(2)$, and each is the unique even $2$-elementary lattice of its signature and invariants up to isometry by @thm:two-elementary-classification; the determinants $2^2\cdot 2^8$ and $2^8$ and the generator lengths $2 + 8$ and $8$ are those read off the two splittings. The representatives $e$ and $e'$ realize the two types: $\divisibility_{\ten}(e) = 1$ because $e\cdot f = 1$, and $\divisibility_{\ten}(e') = 2$ because $e'$ is orthogonal to $U \oplus E_8(2)$ and $e'\cdot U(2) = 2\ZZ$; and the class of $e'/2$ is ordinary because no class of $A_{\ten}$ is characteristic. By the existence and uniqueness clause of [@AE22, Prop. 5.5] --- an isotropic vector of a given type exists if and only if a $2$-elementary lattice with the corresponding invariants exists, and it is then unique up to $\Orth(\ten)$ --- each type contributes exactly one $\Orth(\ten)$-orbit of primitive isotropic vectors, and there are no other types. The two orbits are distinct because an isometry carries $\eta^{\perp \ten}/\eta$ isometrically onto $(\eta')^{\perp \ten}/\eta'$, whereas the two quotients have unequal generator lengths, $10$ and $8$. This agrees with [@Ste91, Prop. 4.5].

The count is the same for $\Gamma_{\En} = \Orth^+(\ten)$ as for $\Orth(\ten)$. Let $\eta$ be $e$ or $e'$, and let $H$ be the summand $U$ or $U(2)$ of $\ten$ that contains it, so that $\ten = H \perp H^{\perp \ten}$. The isometry $\tau \definedas -\id_H \oplus \id_{H^{\perp \ten}}$ maps $\eta$ to $-\eta$, so it fixes the line $\generators{\eta}$. By @prop:spinor-norm-orientation-classes (3), the real spinor norm of $\tau$ is that of $-\id_H$, and $H$ has signature $(1,1)$, so this spinor norm is $[-1]$ by @lem:minus-identity-spinor-norm and $\tau \notin \Gamma_{\En}$. The real spinor norm is therefore a surjective group morphism $\Orth(\ten) \to \theset{\pm 1}$ with kernel $\Gamma_{\En}$, and $\Gamma_{\En}$ has index two in $\Orth(\ten)$. If $g \in \Orth(\ten)$ carries $\generators{\eta}$ onto a primitive isotropic line $\ell$, then so does $g\tau$, and exactly one of $g$ and $g\tau$ lies in $\Gamma_{\En}$. So the orbits of the two groups on primitive isotropic lines agree.
:::

::: {.proposition #prop:fen-two-one-cusps title="The 1-cusps of the unpolarized Enriques moduli space"}

Write $U = \generators{e,f}$ and $U(2) = \generators{e',f'}$ for the summands of $\ten$, and let $\alpha = \alpha_1 + \alpha_2$ with $\alpha_1, \alpha_2 \in E_8(2)$ orthogonal roots of square $-4$. The lattice $\ten$ has exactly two $\Gamma_{\En}$-orbits of primitive isotropic planes, represented by
$$
I_{1,2} \definedas \generators{e, e'},
\qquad
I_2 \definedas \generators{e', 2e + 2f + \alpha}.
$$
Hence $\bbcpt{\fen}$ has exactly two 1-cusps. The closure of the 1-cusp of $I_{1,2}$ contains both 0-cusps $\eta_1$ and $\eta_2$, and the closure of the 1-cusp of $I_2$ contains $\eta_2$ only.
:::

::: {.proof}

With $\ten$ the lattice $L_- = \mathbf{H}\oplus\mathbf{H}(2)\oplus E_8(-2)$ of @Ste91, written there with the opposite sign on $E_8$, there are exactly two $\Orth(\ten)$-orbits of primitive isotropic planes [@Ste91, Prop. 4.6].

The planes $I_{1,2}$ and $I_2$ are isotropic: the only nonzero pairing among $e$, $f$, $e'$ and the summand $E_8(2)$ is $e\cdot f = 1$, so $(2e+2f+\alpha)^2 = 8 + \alpha^2 = 0$ and $e'\cdot(2e+2f+\alpha) = 0$. They are primitive. For $I_{1,2}$ this holds because $e$ and $e'$ are basis vectors of $\ten$. For $I_2$, the vector $\alpha$ is primitive in $E_8(2)$, since $\alpha/n$ has square $-8/n^2 \notin 4\ZZ$ for $n \ge 2$; so $a e' + b(2e+2f+\alpha)$ is divisible by $n$ in $\ten$ only if $n$ divides $a$ and $b$.

The two planes lie in different $\Orth(\ten)$-orbits. The plane $I_{1,2}$ contains $e$, and $\divisibility_{\ten}(e) = 1$. Every primitive vector of $I_2$ pairs into $2\ZZ$ with $\ten$ and is primitive in $\ten$. Its divisibility is therefore $2$, since $A_{\ten}$ has exponent two. By @prop:fen-two-zero-cusps, the primitive isotropic vectors of divisibility $1$ form the orbit of $e$, and those of divisibility $2$ form the orbit of $e'$. This also gives the incidences: the closure of the 1-cusp of a plane $I$ contains the 0-cusps of the primitive isotropic lines in $I$.

The $\Gamma_{\En}$-orbits are the $\Orth(\ten)$-orbits. Let $\tau_U \definedas -\id_U \oplus \id_{U^{\perp \ten}}$ and $\tau_{U(2)} \definedas -\id_{U(2)} \oplus \id_{U(2)^{\perp \ten}}$. By the proof of @prop:fen-two-zero-cusps, both have real spinor norm $[-1]$, and $\Gamma_{\En}$ has index two in $\Orth(\ten)$. The isometry $\tau_U$ maps $e$ to $-e$ and fixes $e'$, so it preserves $I_{1,2}$. The isometry $\tau_{U(2)}$ maps $e'$ to $-e'$ and fixes $2e+2f+\alpha$, so it preserves $I_2$. If $g \in \Orth(\ten)$ carries one of the two planes onto a plane $P$, and $\tau$ is the isometry that preserves that plane, then $g\tau$ also carries it onto $P$, and exactly one of $g$ and $g\tau$ lies in $\Gamma_{\En}$.
:::

These representatives give the following cusp diagram:

::: {#fig:fen-unpolarized-cusp-diagram .figure}

\begin{tikzpicture}
\pic[cusp labels=none] (E) {object=bb-cusps/fen};
\foreach \c/\v in {E10/{\eta_1 = e}, E8/{I_{1,2} = \generators{e, e'}}, UE8/{\eta_2 = e'},
    D8/{I_2 = \generators{e', 2e + 2f + \alpha_1 + \alpha_2}}}
  {\node[below=2mm] at (E-\c.south) {$\v$};}
\end{tikzpicture}
The cusp diagram of $\fen$, the moduli space of unpolarized Enriques surfaces.

:::

##### Mirror Moves

Let $S$ be a primitive hyperbolic $2$-elementary sublattice of the K3 lattice $\lkt$, and let $T=S^{\perp\lkt}$ have signature $(2,n)$. For the action of $\Orth(T)$, a mirror move classifies a primitive isotropic line $\ell=\ZZ\eta$ by the splitting $T=H\perp K$ with $\ell\subset H$ and $K\cong\ell^\perp/\ell$ [@AE22, Def. 5.6 and Thm. 5.8]. The boundary points correspond to line orbits, the boundary curves to plane orbits, and incidence to containment of representatives.

Write $(r,a,\delta)$ for the rank, discriminant length and coparity of $T$. The isotropic vector classification [@AE22, Prop. 5.5] gives the following splittings. A row occurs when its target is realized by a lattice $K$ of signature $(1,n-1)$ with the indicated invariants.

| Type of $\eta$ | $\divisibility_T(\eta)$ | $H$ | Invariants of $K$ |
|---|---|---|---|
| Odd (simple) | $1$ | $U$ | $(r-2,a,\delta)$ |
| Even ordinary | $2$ | $U(2)$ | $(r-2,a-2,\delta)$ |
| Even characteristic ($\delta=1$) | $2$ | $I_{1,1}(2)$ | $(r-2,a-2,0)$ |

The discriminant form of $U$ is trivial. That of $U(2)$ is integral-valued, so removing either summand preserves coparity. Only the characteristic move changes it. For an isotropic flag $\ell\subset I$, apply the same splitting rule to the primitive line $I/\ell$ of $\ell^\perp/\ell$. Its boundary lattice is $I^\perp/I$, now negative definite. The second step uses the coparity of $\ell^\perp/\ell$. In particular a characteristic move cannot follow a characteristic move. To pass from flags to plane orbits one must identify the underlying planes. The rank, discriminant length and coparity of a definite lattice in general specify only its genus [@AE22, Lemma 5.9 and Thm. 5.10].

For $T=\ten$, the basis lines of $U$ and $U(2)$ give the two targets $(10,10,0)_1$ and $(10,8,0)_1$ of @prop:fen-two-zero-cusps. The plane $I_{1,2}$ contains a line of each type. Every primitive line in $I_2$ has divisibility two. Thus the three incidences in the diagram belong to the two plane orbits of @prop:fen-two-one-cusps. Both propositions show that the same orbits occur for $\Gamma_{\En}=\Orth^+(\ten)$.

For the discriminant kernel, write $\rho\colon\Orth(\ten)\to\Orth(A_{\ten},q_{\ten})$ for the discriminant action. The class $c(\ell)=[v/\divisibility_{\ten}(v)]$ of a primitive isotropic line $\ell=\ZZ v$ is independent of the sign of $v$ since $2A_{\ten}=0$. On the two line orbits of @prop:fen-two-zero-cusps it takes the values $0$ and a nonzero isotropic class, respectively.

To see why the class determines a kernel orbit, write $\ten=U\perp M(2)$ with $M=U\perp E_8$. Identify $A_{\ten}$ with $M/2M$ by $\bar m\mapsto[m/2]$. In these coordinates $q(\bar m)=m^2/2\bmod 2$, with the square taken in $M$. The isometries of $M(2)$ fix $e$ in the first summand and induce the full finite orthogonal group [@Nik80, Thm. 3.6.3]. For $e'$ in the second hyperbolic summand, use the unscaled form of $M$ and write $M=\ZZ e'\oplus\ZZ f'\oplus E_8$, with $(e',f')=1$. A finite isometry fixing $\bar e'$ sends $\bar f'$ to $\bar f'+\bar z+q(\bar z)\bar e'$ for some $\bar z\in E_8/2E_8$, since it preserves the pairing with $\bar e'$ and the square of $\bar f'$. For a lift $z\in E_8$ this action on $\bar f'$ lifts to the integral isometry of $M$ given by
$$
e'\mapsto e',\qquad f'\mapsto f'+z-\tfrac{z^2}{2}e',\qquad
x\mapsto x-(x,z)e'\quad(x\in E_8).
$$
After composing with its inverse the finite isometry fixes both $\bar e'$ and $\bar f'$. Its restriction to their orthogonal complement lifts because $W(E_8)\to\Orth(E_8/2E_8,q)$ is onto [@CDL25, Remark 0.8.17]. Extending both lifts by the identity on the first $U$ proves $\rho(\Stab_{\Orth(\ten)}(\ell))=\Stab_{\Orth(A_{\ten},q_{\ten})}(c(\ell))$ for the second representative as well.

If $c(g\ell)=c(\ell)$, choose $s$ fixing $\ell$ with $\rho(s)=\rho(g)$. Then $gs^{-1}\in\ker\rho$ takes $\ell$ to $g\ell$. Thus each attained class gives one kernel orbit.

The finite quadratic space $A_{\ten}$ is the split space of dimension ten over $\mathbb F_2$. In hyperbolic coordinates its isotropic classes are the pairs $(x,y)\in\mathbb F_2^5\times\mathbb F_2^5$ with $x\cdot y=0$. The full finite orthogonal group is transitive on the nonzero isotropic classes by Witt's theorem. All are therefore attained from the divisibility-two representative. The component-reversing isometry used in @prop:fen-two-zero-cusps acts trivially on $A_{\ten}$ for either representative, since it is minus the identity on one summand and the discriminant group has exponent two. Hence restricting the kernel to $\Orth^+(\ten)$ preserves each line orbit as well.

| Acting group on $\ten$ | Divisibility one | Divisibility two | Total line orbits |
|---|---:|---:|---:|
| $\Orth(\ten)$ or $\Gamma_{\En}$ | $1$ | $1$ | $2$ |
| $\ker\rho$ or $\ker\rho\cap\Gamma_{\En}$ | $1$ | $32+31\cdot16-1=527$ | $528$ |

::: {#fig:fen-mirror-move-summary .figure}

\begin{tikzpicture}
\pic {object=mirror-moves/enriques};
\end{tikzpicture}

The two first moves preserve $\delta=0$. Their common second target $(8,8,0)_0$ represents the plane $I_{1,2}$ incident to both line orbits.

:::

::: {#fig:fen-cusp-diagram-summary .figure}

\begin{tikzpicture}
\pic[cusp labels=eta] {object=bb-cusps/fen};
\end{tikzpicture}
The cusp diagram of $\fen$, indicating two 0-cusps $\eta_{1}, \eta_2$ and two 1-cusps $I_{1,2}, I_2$.
The plane $I_2$ meets only the divisibility-two cusp $\eta_2$.

:::
