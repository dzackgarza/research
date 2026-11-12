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

| cusp | label roots | $J^\perp/J$ | $\det$ | $S$, the span of the label roots in it | $\det S$ | $[J^\perp/J : S]$ | glue $A_S/\angles{\cdot}$ |
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

The orbit of a primitive isotropic sublattice $I \subset T_{2d}$ is classified by the quotient $J = I^\perp/I$ together with the gluing of $J$ into $T_{2d}$. When $I$ is a plane, $J$ is negative definite of rank $\rk T_{2d} - 4$. For the lattices $\Lambda_N = U^2\oplus D_{N-2}$ with $3 \le N$, a rank two *saturated* isotropic $I$ for which $\Lambda_N \to \operatorname{Hom}(I,\ZZ)$ is surjective sits inside a unimodular $U\oplus U$ with $\Lambda_N = (U\oplus U)\oplus L$ [@LO21, Prop. A.4 (1)], and this surjectivity holds for every saturated $I$ when $N \not\equiv 2 \pmod 8$. Then $J \cong L$, $A_{\Lambda_N} \cong A_L$ because $U\oplus U$ is unimodular, and the gluing is the isometry class of the embedding $L \subset \Lambda_N$. This applies to $T_4 \cong \Lambda_{19}$, since $19 \equiv 3 \pmod 8$.

The discriminant group does not separate the orbits. At $d = 1$ there are four orbits, while $A_{T_2} \cong \ZZ/2$ has one nonzero element, the class of $a/2$ with $a^2 = -2$, and its discriminant square $-1/2 \bmod 2\ZZ$ is nonzero; so $A_{T_2}$ has only the trivial isotropic subgroup. At $d = 2$ the nine orbits of [@LO21, Thm. A.12] lie in one genus of rank-$17$ lattices, and the isometry class of $J$ separates them, since $[I] \mapsto [J]$ is injective [@LO21, Prop. A.11]. By Nikulin's theorem, the signature and the discriminant form of an even lattice determine its genus [@Nik80]; equality of genera is therefore necessary, and not sufficient, for two orbits to coincide.
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

The lattice $\ten$ is even $2$-elementary of invariants $(12,10,0)_2$: its discriminant group is $A_{\ten} = \tfrac12 M/M \cong (\ZZ/2)^{10}$ with $M \definedas U(2)\oplus E_8(2)$, and $q_{\ten}$ takes integral values on it, because $x^2 \in 4\ZZ$ for every $x \in M$, so that $q_{\ten}(x/2) = x^2/4 \in \ZZ$. Hence $\delta(\ten) = 0$ in the sense of @thm:two-elementary-classification, the functional $q_{\ten} \bmod \ZZ$ vanishes, and $A_{\ten}$ has no nonzero characteristic class: such a class $x$ would satisfy $\bar\beta(x,y) = q_{\ten}(y)\bmod\ZZ$ for every $y$, so it would lie in the radical of a nondegenerate form. The third case of @thm:isotropic-trichotomy requires $\delta = 1$ and therefore does not occur, and every primitive isotropic vector of $\ten$ is of the first or the second type.

The first type gives $\ten \cong U \perp \bdlattice{T}{\eta}$ with $\bdlattice{T}{\eta}$ of signature $(1,9)$ and invariants $(10,10,0)$, and the second gives $\ten \cong U(2)\perp \bdlattice{T}{\eta}$ with $\bdlattice{T}{\eta}$ of signature $(1,9)$ and invariants $(10,8,0)$. Both lattices exist, namely $U(2)\oplus E_8(2)$ and $U\oplus E_8(2)$, and each is the unique even $2$-elementary lattice of its signature and invariants up to isometry by @thm:two-elementary-classification; the determinants $2^2\cdot 2^8$ and $2^8$ and the generator lengths $2 + 8$ and $8$ are those read off the two splittings. The representatives $e$ and $e'$ realize the two types: $\div_{\ten}(e) = 1$ because $e\cdot f = 1$, and $\div_{\ten}(e') = 2$ because $e'$ is orthogonal to $U \oplus E_8(2)$ and $e'\cdot U(2) = 2\ZZ$; and the class of $e'/2$ is ordinary because no class of $A_{\ten}$ is characteristic. By the existence and uniqueness clause of @thm:isotropic-trichotomy --- an isotropic vector of a given type exists if and only if a $2$-elementary lattice with the corresponding invariants exists, and it is then unique up to $\Orth(\ten)$ --- each type contributes exactly one $\Orth(\ten)$-orbit of primitive isotropic vectors, and there are no other types. The two orbits are distinct because an isometry carries $\eta^{\perp \ten}/\eta$ isometrically onto $(\eta')^{\perp \ten}/\eta'$, whereas the two quotients have unequal generator lengths, $10$ and $8$. This agrees with [@Ste91, Prop. 4.5].

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

The two planes lie in different $\Orth(\ten)$-orbits. The plane $I_{1,2}$ contains $e$, and $\div_{\ten}(e) = 1$. Every vector of $I_2$ has divisibility $2$, because $e'$ and $2e+2f+\alpha$ pair into $2\ZZ$ with every vector of $\ten$. By @prop:fen-two-zero-cusps, the primitive isotropic vectors of divisibility $1$ form the orbit of $e$, and those of divisibility $2$ form the orbit of $e'$. This also gives the incidences: the closure of the 1-cusp of a plane $I$ contains the 0-cusps of the primitive isotropic lines in $I$.

The $\Gamma_{\En}$-orbits are the $\Orth(\ten)$-orbits. Let $\tau_U \definedas -\id_U \oplus \id_{U^{\perp \ten}}$ and $\tau_{U(2)} \definedas -\id_{U(2)} \oplus \id_{U(2)^{\perp \ten}}$. By the proof of @prop:fen-two-zero-cusps, both have real spinor norm $[-1]$, and $\Gamma_{\En}$ has index two in $\Orth(\ten)$. The isometry $\tau_U$ maps $e$ to $-e$ and fixes $e'$, so it preserves $I_{1,2}$. The isometry $\tau_{U(2)}$ maps $e'$ to $-e'$ and fixes $2e+2f+\alpha$, so it preserves $I_2$. If $g \in \Orth(\ten)$ carries one of the two planes onto a plane $P$, and $\tau$ is the isometry that preserves that plane, then $g\tau$ also carries it onto $P$, and exactly one of $g$ and $g\tau$ lies in $\Gamma_{\En}$.
:::

These representatives give the following cusp diagram:

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
