### Enumerating Cusps

As a starting point to any compactification procedure of lattice polarized K3 surfaces $F_S$, we must first find the cusps of $\bbcpt{F}_S$.
We give an overview here of various methods in the literature for similar moduli spaces, and how their cusps can be found and studied.

#### $\ftd$: Degree 2d Polarized K3 Surfaces (Scattone's Description)

\todo{Separate the Hodge-theoretic work}

Let $\lkt$ denote the K3 lattice, and let $h \in \lkt$ be a primitive vector of square $2d > 0$. The lattice orthogonal to the polarization is defined as
$$
T_{2d} \da  h^\perp_{\lkt} \cong \gens{-2d} \oplus U^{\oplus 2} \oplus E_8^{\oplus 2},
$$
which is even and of signature $(2,19)$. The Type $\IV$ Hermitian symmetric period domain for $T_{2d}$,
$$
\halfpd{T_{2d}} = \ts{ [\omega] \in \PP(T_{2d, \CC} ) \st (\omega, \omega) = 0,\, (\omega, \bar{\omega}) > 0 },
$$
admits a natural right action by the arithmetic group $\Gamma_{2d} \subset \Orth^+(T_{2d})$, the intersection of the original orthogonal group with the subgroup stabilizing $h$ (and, if necessary, a choice of connected component). The arithmetic quotient
$$
\ftd \da  \dmodgamma{ \halfpd{T_{2d}} }{ \Gamma_{2d} }
$$
is the coarse moduli space parametrizing degree $2d$ polarized K3 surfaces.

The Baily–Borel compactification $\bbcpt{\ftd}$ is projective, and its boundary strata correspond bijectively to $\Gamma_{2d}$-orbits of primitive isotropic sublattices of $T_{2d}$ of ranks $1$ and $2$. More precisely, $0$-cusps are in correspondence with orbits of primitive isotropic planes up to the action of $\Gamma_{2d}$. The incidence relations between cusps are set by lattice inclusions: any $0$-cusp (an isotropic line) is contained in the closure of all $1$-cusps (isotropic planes) in which it lies.

As a concrete and illustrative case, set $d = 1$. Then $h^2 = 2$ and
$$
T_2 = \gens{-2} \oplus U^{\oplus 2} \oplus E_8^{\oplus 2}.
$$
Scattone shows that for squarefree $d$ (in particular, $d = 1$), there is exactly one $\Gamma_{2d}$-orbit of primitive isotropic lines in $T_{2d}$, so the Baily–Borel boundary of $F_2$ has a unique $0$-cusp.

The 1-cusps are determined by the negative-definite lattices $\bdlattice{T}{2d, I} \da  I^{\perp T}/I$, for $I \subset T$ a primitive isotropic plane. Scattone showed that, up to isomorphism and the action of the arithmetic group, there are exactly four possible such lattices, each of rank $18$ and discriminant $2$, characterized by their root sublattices:
$$
A_1 \oplus E_8^{\oplus 2}, \qquad E_7 \oplus D_{10}, \qquad A_1 \oplus D_{16}, \qquad A_{17}.
$$ {#eq:ft-four-lattices}
These emerge as orthogonal complements to embeddings of $E_7$ into the four Niemeier lattices $U$ of rank $24$ that admit such sublattices. Each of these possibilities labels a modular curve in the boundary of $\bbcpt{F_2}$, and the closure of each of these modular curves contains the unique $0$-cusp as every isotropic line is contained in some isotropic plane.

The structure of $\bd \bbcpt{\ftd}$ can be studied through the asymptotic behavior of the period map, governed by limiting mixed Hodge structures and their associated monodromy operators, following the work of @FS86. For a one-parameter degeneration $\mcx \to \Delta$ of polarized degree $2d$ K3 surfaces over a punctured disk $\Delta^*$, the unipotent monodromy operator $T \in O(T_{2d})$ determines the degeneration structure. Its nilpotent logarithm $N = \log T \in \Endo(T_{2d, \QQ })$ induces the canonical monodromy weight filtration $\incfiltration{W}$ on $T_{2d, \QQ}$, uniquely characterized by the properties $N(W_k) \containedin W_{k-2}$ for all $k$, and that for each $j > 0$, the maps $N^j: \Gr^W_{k+j} \to \Gr^W_{k-j}$ are isomorphisms.
Schmid's Nilpotent Orbit Theorem establishes that the period map asymptotically approaches a nilpotent orbit, defining a limiting Hodge filtration $\decfiltration{F^{\lim}}$ on $T_{2d, \CC}$ which, together with $\incfiltration{W}$, constitutes the limiting mixed Hodge structure (LMHS). This framework provides the connection between geometric degenerations and arithmetic lattice structures.

The boundary components of $\bbcpt{\ftd}$ are classified by the nilpotency index of $N$. The Type $\II$ boundary components (1-cusps) correspond to degenerations where $N \neq 0$ but $N^2 = 0$. For such degenerations, associated with a primitive isotropic plane $I \subset T_{2d}$, is a three-step monodromy weight filtration:
$$
0 = W_0 \subset W_1 = I_{\QQ} \subset W_2 = I^{\perp T_{2d}}_{\QQ} \subset W_3 = T_{2d, \QQ}
.$$
The LMHS induces a pure polarized Hodge structure of weight 2 on the graded piece $\Gr_2^W = I^{\perp}/I$, which is precisely the boundary lattice $\bdlattice{T}{I}$ arising in Scattone's combinatorial classification. This identification reveals that $\bdlattice{T}{I}$ is not merely a lattice-theoretic invariant, but rather the natural target of the weight-2 component of the limiting mixed Hodge structure.

For Type $\III$ degenerations (0-cusps), where $N^2 \neq 0$ but $N^3 = 0$, the weight filtration is of maximal length. The classifying space of such Hodge structures on $\bdlattice{T}{I}$ is itself a Type $\IV$ Hermitian symmetric domain $\halfpd{\bdlattice{T}{I}}$ and the boundary component itself is a modular variety $F_{\Gamma_I}$ for an appropriate arithmetic subgroup $\Gamma_I \leq \Orth^+(\bdlattice{T}{I})$. These degenerations correspond to normal crossing varieties whose dual complex is a triangulation of $S^2$.
The computational accessibility of these mixed Hodge structures relies on several key tools developed in the work starting in @FS86: the Clemens-Schmid exact sequence relating the cohomology of central and $\mcx_t$s, and the Steenbrink weight spectral sequence, which for K3 surfaces degenerates integrally at the $E_2$-page. This integral degeneration is a special property of K3 surface degenerations that enables explicit computation of the limiting mixed Hodge structure components.
The vanishing cycle analysis developed by Friedman and Scattone provides detailed control over how cohomology classes behave under degeneration. Through Mayer-Vietoris techniques and careful analysis of the dual complex structure, they established the precise relationship between the geometric combinatorics of singular fibers and the arithmetic invariants encoded in LMHS. The stratification $\bbcpt{\ftd}$ is thus realized by the asymptotic behavior of the period map at the various boundary cusps.

#### $F_2$: Scattone's Description

For the specific case $d=1$, @Sca87 finds exactly four possible isometry classes for $\bdlattice{T}{I}$ determined by a 1-cusp $I$ adjacent to the unique 0-cusp $\eta$, distinguished by their root sublattices as defined above. These correspond to the four distinct Type $\II$ modular curves in the boundary of $\bbcpt{F_2}$. The unique 0-cusp $\eta$ correspond to a Type $\III$ component, and thus a degeneration where $N^2 \neq 0$ but $N^3=0$, yielding a weight filtration of maximal length. The geometric inclusion of the 0-cusp  in the closure of each 1-cusp reflects the lattice-theoretic fact that any primitive isotropic plane $I$ contains the primitive isotropic line $\eta$, all up to $\Gamma_{T_{2d}}$-invariance. This incidence structure is encoded combinatorially in the Coxeter diagram of the lattice $\bdlattice{T}{2d, \eta}$ associated to the 0-cusp, whose maximal parabolic subdiagrams are in bijection with the possible isomorphism classes of the lattices $\bdlattice{T}{I}$ for the adjacent 1-cusps.

The cusps in $\bbcpt{F_2}$ are obtained by classifying primitive isotropic sublattices of the lattice  
$$
T_{2} \da \gens{-2}\oplus U^{\oplus2}\oplus E_{8}^{\oplus2}
$$ 
using discriminant–form methods, from which Scattone shows:

-  There is a single $\Gamma_{2}$-orbit of primitive isotropic lines $\eta$ in $T_2$, giving one 0-cusp (Type $\III$);  

-  There are four $\Gamma_{2}$-orbits of primitive isotropic planes $I$ in $T_2$, whose corresponding boundary lattices $\bdlattice{T}{I}$ are the rank-18, negative-definite lattices given in @eq:ft-four-lattices, yielding four Type $\II$ boundary curves;  

-  These four curves meet transversely at the unique Type $\III$ point.

We assemble this data into the following **cusp diagram**:

:::{#fig:f2-cusp-diagram .figure}

\begin{tikzpicture}
\pic[cusp labels=eta] {object=bb-cusps/f2};
\end{tikzpicture}
The cusp diagram of $F_2$, the moduli space of degree 2 polarized K3 surfaces, which contains one 0-cusp $\eta$ adjacent to four 1-cusps.

:::

The general enumeration of $\bd\bbcpt{ F_{2d} }$ reduces to finite problems in the discriminant group $A_{T_{2d}}$: cusps can be classified by studying isotropic subgroups of the finite discriminant group $A_{T_{2d}} \da  (T_{2d})^*/T_{2d}$, and applying Nikulin's theorem that the genus of an even lattice is determined by its signature and the isomorphism class of its discriminant form [Nikulin 1980].
The classification proceeds by associating to a primitive isotropic sublattice $I \subset T_{2d}$ an isotropic subgroup of $A_{T_{2d}}$. The problem of classifying orbits of such sublattices under the infinite group $\Gamma_{2d}$ is thereby reduced to classifying orbits of isotropic subgroups of the finite group $A_{T_{2d}}$ under the action of a subgroup of $\OStab( A_{T_{2d}} )$.
For the case $d=1$, he four isomorphism classes of the rank-18 lattice $\bdlattice{T}{I}$ are constructed by leveraging the classification of the 24 Niemeier lattices: each isometry class of $\bdlattice{T}{I}$ is realized as the orthogonal complement $E_7^\perp \subset M$, where $M$ is one of the Niemeier lattices that admit a primitive embedding of the $E_7$ root lattice [Scattone 1987]. This reduces the classification to a relatively well-known, finite set of possibilities.
For general $d$, cusp enumeration becomes a number-theoretic problem, since structure of $A_{T_{2d}}$ is highly dependent on the arithetic properties of $d$ itself, including various the numbers of solutions to various congruences, as well as the prime factorization of $d$. @Sca87 uses these techniques to explicitly describe cusp diagrams for certain (sparse) families of values of $d$.
For further details and the explicit Coxeter diagrams, see [@Sca87, §6.2] and [@AET23, Fig. 2].


<!-- 
# Separating Scattone's Methods: F₂d Paper vs. Type $\III$ Degenerations Paper

Based on my research, I can now provide a clear separation between what Scattone accomplished in his two main papers: the 1987 memoir on F₂d compactifications and the 1986 collaboration with Friedman on Type $\III$ degenerations.

## Scattone's 1987 F₂d Paper: "On the Compactification of Moduli Spaces for Algebraic K3 Surfaces"

### Core Methods and Focus

**Primary Approach: Lattice-Theoretic Classification**
- **Discriminant Form Analysis**: Scattone's main innovation was using discriminant quadratic forms to systematically classify boundary components
- **Isotropic Sublattice Classification**: Established bijective correspondence between boundary components and Γ₂d-orbits of primitive isotropic sublattices of T₂d
- **Arithmetic Group Theory**: Used properties of orthogonal groups O⁺(T₂d) and their action on isotropic sublattices

**Specific Technical Methods**:
1. **Eichler Criterion Application**: Used to classify primitive isotropic vectors and their orbits under arithmetic group action
2. **Discriminant Group Computations**: Exploited the finite discriminant group A_{T₂d} = (T₂d)*/T₂d to reduce infinite classification problems to finite ones
3. **Niemeier Lattice Connections**: For degree 2 case, used embeddings into the 24 Niemeier lattices to classify the four types of rank-18 lattices

**Key Results for F₂d**:
- Complete classification of boundary components for general degree 2d
- Explicit enumeration for d=1: exactly one 0-cusp and four 1-cusps with specific root lattice structures
- **Cusp Counting Formula**: Number of cusps depends on arithmetic properties of d (square-free factorization, congruences)

**Notable Absence**: The 1987 paper does **not** contain extensive Hodge-theoretic machinery - it's primarily combinatorial and arithmetic.

## Friedman-Scattone 1986 Paper: "Type $\III$ Degenerations of K3 Surfaces"

### Core Methods and Focus

**Primary Approach: Mixed Hodge Structure Analysis**
- **Limiting Mixed Hodge Structures**: Systematic study of Steenbrink-Schmid theory for Type $\III$ degenerations
- **Monodromy Weight Filtrations**: Detailed analysis of nilpotent monodromy operators N with N³=0 but N²≠0
- **Vanishing Cycle Analysis**: Study of how cohomology classes behave under degeneration

**Specific Technical Methods**:
1. **Clemens-Schmid Exact Sequence**: Used to relate cohomology of smooth and singular fibers
2. **Weight Spectral Sequence**: Proved integral degeneration at E₂ for K3 surface degenerations
3. **Mayer-Vietoris Analysis**: For computing cohomology of normal crossing varieties

**Key Results**:
- **Complete Classification**: All Type $\III$ degenerations correspond to triangulations of S² with specific combinatorial constraints
- **Cohomological Invariants**: Showed how dual complex structure determines lattice-theoretic invariants
- **Monodromy Structure**: Established precise relationship between geometric degenerations and monodromy representations

## Critical Distinctions

### What Belongs to the F₂d Paper:
```
• Discriminant form techniques for boundary classification
• Isotropic sublattice orbit analysis  
• Arithmetic group computations
• Cusp enumeration formulas
• Connection to Niemeier lattices (degree 2 case)
• Lattice genus theory applications
```

### What Belongs to the Friedman-Scattone Type $\III$ Paper:
```
• Mixed Hodge structure machinery
• Monodromy weight filtrations
• Limiting Hodge filtration analysis
• Clemens-Schmid exact sequences
• Weight spectral sequence degeneration
• Vanishing cycle computations
• Connection to triangulations of S²
```

## The Text Analysis

Looking at the provided text, the **lattice-theoretic portions** (discriminant forms, isotropic sublattices, Niemeier lattice connections, cusp classification) clearly belong to **Scattone's 1987 F₂d work**.

The **Hodge-theoretic portions** (limiting mixed Hodge structures, monodromy weight filtrations, Steenbrink weight spectral sequences) belong to the **1986 Friedman-Scattone collaboration**.

The text appears to conflate methods from both papers, presenting them as if they were unified in a single approach, when in fact they represent distinct but complementary methodologies developed in separate works.
 -->

#### $\fell$: Elliptic Surfaces

The moduli space $\fell$ parametrizes elliptic K3 surfaces with a chosen section, a condition that fixes a primitive embedding of a hyperbolic plane $U_1 \subset \lkt$. The relevant period map is thus defined on the orthogonal complement $\tell \da  U_1^{\perp_{\lkt}} \cong U^2 \oplus E_8^2$, and the moduli space is the 18-dimensional arithmetic quotient $\fell$. 
A geometric description of the compactifications of $\fell$ is given in @ABE22, who construct KSBA compactifications and prove their isomorphism to specific semitoroidal compactifications. There a unique $\fell$-orbit of 0-cusps in $\tell$, repsented by $\eta = e$, and the analysis falls on $\bar{(\tell)}_\eta \cong \II_{1, 17}$
Semitoroidal compactifications are defined by fans constructed in the rational closure $\thecone{C}_{\eta, \QQ}$ of the positive cone in $\II_{1, 17}$.
Two separate KSBA compactifications are constructed:

1.  **The Ramification Divisor Compactification ($\cpt{F}^{\ram}$):** The polarization is given by the class of the ramification divisor $R$ from the representation of the K3 surface as a double cover of $\PP(1,1,4)$, so that $[R] = 3(s+2f)$, where $s$ is the section class and $f$ is the fiber class. This defines a KSBA compactification parametrizing pairs $(X, \epsilon R)$ with $X$ an slc K3 surface.

2.  **The Rational Curve Divisor Compactification ($\cpt{F}^{\rcop}$):** The polarization is taken to be $R = s + m \Sum_{i=1}^{24} f_i$, where the $f_i$ are the 24 singular fibers of the elliptic fibration for a generic elliptic K3 surface.

The core result [@ABE22] is the identification of these KSBA moduli spaces with semitoroidal compactifications defined by specific fans in $\thecone{C}_{\QQ}$. The fundamental fan is the **Coxeter fan** $F^{\cox}$, whose cones are the chambers of the reflection group $W(\II_{1,17})$. The **ramification fan** $F^{\ram}$ is a coarsening of $F^{\cox}$ whose fundamental chamber is a union of four Coxeter chambers. The **rational curve fan** $F^{\rcop}$ is a refinement of $F^{\cox}$ obtained by subdividing its fundamental chamber into nine sub-chambers. @ABE22 prove that the normalizations of $\cpt{F}^{\ram}$ and $\cpt{F}^{\rcop}$ are isomorphic to the semitoroidal compactifications defined by the fans $F^{\ram}$ and $F^{\rcop}$, respectively, laying the groundwork for our main result on $\fent$.

The geometric models for the boundary strata are constructed using the theory of **integral-affine spheres with 24 singularities ($\IAS^2$)**. A Type $\III$ Kulikov degeneration of an elliptic K3 surface corresponds bijectively to a triangulated $\IAS^2$, and  the monodromy of a one-parameter degeneration determines a vector $\lambda \in \thecone{C}_{\QQ}$, the **monodromy invariant**, which determines the combinatorial type of the stable limit $(X_0, \epsilon R)$ and is constant for all $\lambda$ within the interior of a cone of the relevant fan. This provides a description of the boundary strata as unions of rational surfaces with prescribed singularities determined by the $\IAS^2$.

Its Baily–Borel boundary contains a unique 0-cusp and two 1-cusps. The latter correspond to the two $\gell$-orbits of primitive isotropic planes $I \subset \tell$, distinguished by the isomorphism class of the negative-definite rank-16 lattice $\bdlattice{T}{I} = I^\perp/I$. These two classes are $E_8 \oplus E_8$ and $D_{16}^+$, respectively, and the cusp diagram is as follows:

:::{#fig:fell-cusp-diagram .figure}

\begin{tikzpicture}
\pic[cusp labels=eta] {object=bb-cusps/fell};
\end{tikzpicture}
The cusp diagram of $\fell$, the moduli space of elliptic K3 surfaces, which contains one 0-cusp $\eta$ adjacent to two 1-cusps.

:::

#### $\fen$: Unpolarized Enriques Surfaces {#sec:fen-unpolarized-cusps}

The moduli space of *unpolarized* Enriques surfaces corresponds to the lattice $\ten$ and $\Gamma_{\En} \da \Orth^+(\ten)$, yielding the orthogonal modular variety $\fen$.
To enumerate the 0-cusps of $\bbcpt{\fen}$, one can replace $\ten$ by an auxiliary lattice $K = U \oplus E_8 \oplus \I_{1,1}$ and utilize a bijection
$$
\ten/\Orth(\ten) \cong K/\Orth(K)
,$$
allowing for a classification in terms of simpler lattices. A primitive isotropic vector $\eta \in \I_{1,1}\subset K$ yields a unimodular lattice $\bdlattice{T}{\eta}$ of signature $(1,9)$. There are precisely two such lattices up to isometry, $\I_{1, 9}$ and $\II_{1, 9}$. Pulling back, some slightly finer analysis shows there are exactly two $\Gamma_{\En}$-orbits of primitive isotropic lines in $\ten$, corresponding to two 0-cusps $\eta_1, \eta_2$.
A direct approach for **1-cusps** is analytic: any isotropic plane $P \subset K$ must contain an odd primitive isotropic vector $\eta$, due to the indefinite form $\I_{1,1}$. There is only one orbit of such under the full orthogonal group, so $P$ can always be assumed to contain $\eta$. The remaining problem is to classify the possible isometry classes of primitive isotropic lines in $\bdlattice{T}{\eta} \cong \I_{1,9}$. By examining the parities of a basis $\{w, w'\}$ for $P$, one finds two inequivalent types: planes where both generators have the same parity (even/even or odd/odd), and planes where the two have different parity (even/odd). Hence, there are exactly two distinct $\Orth(\ten)$-orbits of primitive isotropic planes, corresponding to two 1-cusps.

Explicit representatives can be given as follows. The 0-cusps correspond to the isotropic lines $\gens{e}$ and $\gens{e'}$, where $U = \gens{e,f}$ and $U(2) = \gens{e', f'}$ as sublattices of $\ten$. The 1-cusps can be represented by the planes $\gens{e, e'}$, and $\gens{e', 2e + 2f + \alpha_1 + \alpha_2}$, where $\alpha_1, \alpha_2 \in E_8(2)$ are orthogonal roots of square $-4$. We thus obtain the following cusp diagram:

:::{#fig:fen-unpolarized-cusp-diagram .figure}

\begin{tikzpicture}
\pic[cusp labels=none] (E) {object=bb-cusps/fen};
% The isotropic vectors spanning each cusp.
\foreach \c/\v in {E10/{\eta_1 = e}, E8/{I_{1,2} = \gens{e, e'}}, UE8/{\eta_2 = e'},
    D8/{I_2 = \gens{e', 2e + 2f + \alpha_1 + \alpha_2}}}
  {\node[below=2mm] at (E-\c.south) {$\v$};}
\end{tikzpicture}
The cusp diagram of $\fen$, the moduli space of unpolarized Enriques surfaces.

:::

##### Mirror Moves

All of the above situations involved somewhat ad-hoc analyses, which can be verified by computing the Coxeter-Vinberg diagrams $G(\Gamma_\eta)$ at the 0-cusps $\eta$ associated to the arithmetic subgroup $\Gamma$ and classifying their maximal elliptic and parabolic subdiagrams.
This can be computationally difficult, so we note a algorithm that can unify most of the above situations when $\Gamma$ is the full (stable) orthogonal group.
Let $T$ be a 2-elementary, nondegenerate, even unimodular lattice of signature $(2, n)$ embedding into the K3 lattice $\lkt$, let $\Gamma = \OStab(T)$, and consider the corresponding arithmetic quotient $\FG = \dmodgamma{ \halfpd{T} }{ \Gamma }$. All such lattices are encoded in Nikulin’s pyramid diagram (see [@AE22]) of 2-elementary lattices. The **cusp diagram** of $\cpt{F}_\Gamma$ is a labeled, directed graph whose vertices are boundary points and curves in $\cpt{F}_\Gamma$, corresponding (up to $\Gamma$-equivalence) with primitive isotropic vectors $\eta, I$ in $T$ and their associated boundary lattices $\bdlattice{T}{\eta}$, $\bdlattice{T}{I}$, with an edge $v_1 \to v_2$ between vertices if the corresponding boundary stratum $F_1$ is contained in the closure of $F_2$. The cusp diagram is computed as follows.

A **mirror move** is a lattice-theoretic operation governed by the existence of a primitive isotropic vector $\eta \in T$ of a specified type and splitting as proved in @AE22:

- **Odd/simple:** $\div_T(\eta) = 1$, and $T \cong U \oplus K$
- **Even, ordinary:** $\div_T(\eta) = 2$ and $\eta^*$ is ordinary in $A_T$, and $T \cong U(2) \oplus K$
- **Even, characteristic:** $\div_T(\eta) = 2$ and $\eta^*$ is characteristic, and $T \cong I_{1,1}(2) \oplus K$

The move replaces $T$ with $\bdlattice{T}{\eta}$, computing the new invariants in each case. A mirror move is only possible if the resulting lattice is realized (i.e., if the corresponding node exists in Nikulin's pyramid, see [@AE22, Fig. 1]) and admits the required splitting.

###### Step 1: Find All Orbits of $0$-Cusps $\eta$

1. **Start at the node $(r_0, a_0, \delta_0)$** in Nikulin’s pyramid associated to $T$.

2. **For every admissible mirror move,** check for outgoing arrows (*mirror moves*) from this node, corresponding to possible splittings of boundary lattices $T_{\eta_a}$ for isotropic vectors $\eta_a$. Each outgoing arrow from $(r_0, a_0, \delta_0)$ will be of one of the following types:
   
| Type of $\eta_a \in T$ | Destination $(r_1, a_1, \delta_1)$ | Splitting of $\bdlattice{T}{\eta_a}$ |
|---|---|---|
| Odd/simple | $(r_0-2,\, a_0,\, 1)$ | $U \oplus K$ |
| Even, ordinary | $(r_0-2,\, a_0-2,\, 1)$ | $U(2) \oplus K$ |
| Even, characteristic | $(r_0-2,\, a_0-2,\, 0)$ | $I_{1,1}(2) \oplus K$ |

   **A $0$-cusp $\eta_a$ exists** if the arrow exists: the destination represents a realizable, hyperbolic, 2-elementary lattice $\bdlattice{T}{\eta_a}$ in Nikulin’s table, and the node at the head of the arrow gives the invariants $(r_1, a_1, \delta_1)$ of the boundary lattice $\bdlattice{T}{\eta_a}$.

###### Step 2: All $1$-Cusps and Incidence Structure

1. For each $0$-cusp $\eta_a$ determined in Step 1, recursively use $\bdlattice{T}{\eta_a}$ with invariants $(r_1, a_1, \delta_1)$ as a new starting point and consider all outgoing arrows from $(r_1, a_1, \delta_1)$ to construct $(r_2, a_2, \delta_2)$. Each move corresponds to a splitting of $\bdlattice{T}{I} \da  \overline{(T_{\eta_a})}_{\eta_b}$ for a primitive isotropic vector $\eta_b \in \bdlattice{T}{\eta_a}$:

| Type of $\eta_b \in \bdlattice{T}{\eta_a}$ | Destination $(r_2, a_2, \delta_2)$ | Splitting of $\bdlattice{T}{I} = \cpt{(T_{\eta_a})}_{\eta_b}$ |
|---|---|---|
| Odd/simple | $(r_1 - 2,\, a_1,\, \delta_1)$ | $U \oplus K'$ |
| Even, ordinary | $(r_1 - 2,\, a_1 - 2,\, \delta_1)$ | $U(2) \oplus K'$ |
| Even, characteristic | $(r_1 - 2,\, a_1 - 2,\, 0)$ | $I_{1,1}(2) \oplus K'$ |

2. **A $1$-cusp $I$ of type $(\eta_a, \eta_b)$ exists** if and only if the move $(r_1, a_1, \delta_1) \to (r_2, a_2, \delta_2)$ exists, corresponding to a 2-elementary lattice $\bdlattice{T}{I}$ with the specified invariants. The $1$-cusp $I$ is incident to $\eta_a$ if and only if it arises from such a two-step sequence.

###### Step 3: Diagram Extraction

The **nodes for $0$-cusps** are given by a single admissible mirror move from $(r_0, a_0, \delta_0)$, labeled by $(r_1, a_1, \delta_1)$, the corresponding lattice splitting, and the root system $\Phi(\bdlattice{T}{\eta})$.
The **nodes for $1$-cusps** are determined by two-step sequences $(r_0, a_0, \delta_0) \to (r_1, a_1, \delta_1) \to (r_2, a_2, \delta_2)$, with associated lattice splitting and root system $\Phi(\bdlattice{T}{I})$. Each $1$-cusp is incident to every $0$-cusp $(r_1, a_1, \delta_1)$ that occurs as an intermediate node in such a sequence.
   While the boundary lattice $\bdlattice{T}{I}$ for a $1$-cusp is determined up to isometry by invariants $(r_2, a_2, \delta_2)$, distinct $\Gamma$-orbits of $1$-cusps are distinguished by their root lattices $\Phi(\bdlattice{T}{I})$, either tabulated in @AE22 or computed via Vinberg’s algorithm. We conclude by tabulating several useful references to use when carrying out this algorithm:

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

Carrying out this algorithm for $\fen$ shows that there are exactly two 1-cusps and two 0-cusps. The following diagram encodes the mirror-move procedure, recording a sequence of moves starting from a primitive sublattice $S\injects \lkt$, computing $T\da S^{\perp \lkt}$, finding $\bar{T}$, the first type of boundary lattice corresponding to a 1-step mirror move (corresponding to $0$-cusps) and finally finding $\overline{\bar T}$, the target of a 2-step mirror move. We find that there are two possibilities for $\bar{T}$, indicated in the $\bar{T}$ column as $(10,10,0)_1$ and $(10, 8, 0)_1$, and two possibilities present in the $\overline{\bar{T}}$ column.
There are three 2-step paths through the diagram, but only two possibilities for $\overline{\bar{T}}$, yielding two $1$-cusps and two $0$-cusps.
We record the resulting cusp diagram below as well.

:::{#fig:fen-mirror-move-summary .figure}

\input{tikz/mirror_moves_enriques_simplified.tex}

A concise summary of the mirror move algorithm applied to $\EnriquesInvariants_1$, corresponding to $\fen$.

:::

:::{#fig:fen-cusp-diagram-summary .figure}

\begin{tikzpicture}
\pic[cusp labels=eta] {object=bb-cusps/fen};
\end{tikzpicture}
The cusp diagram of $\fen$, indicating two 0-cusps $\eta_{1}, \eta_2$ and two 1-cusps $I_{1,2}, I_2$. We note that this recovers the known cusp diagram shown in @sec:fen-unpolarized-cusps.

:::

