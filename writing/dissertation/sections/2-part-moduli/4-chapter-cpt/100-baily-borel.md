### The Baily-Borel Compactification

#### Hermitian Symmetric Domains and Arithmetic Quotients

Let $G$ be a connected, simple linear algebraic group defined over $\QQ$ and fix a maximal compact subgroup $K \subset G(\RR)$. The quotient $D = G(\RR)/K$ is an irreducible symmetric space. This data defines a **Riemannian symmetric space** $(G,K)$ with a decomposition of the Lie algebra of $G(\RR)$:

\begin{align*}
\lieg = \liek \oplus \liep
,
.\end{align*}

where $\liep$ is the orthogonal complement to $\liek$ for an invariant symmetric bilinear form $\beta$ on $\lieg$. 
These spaces frequently arise in moduli problems: for an arithmetic subgroup $\Gamma \subset G(\QQ)$ acting properly discontinuously on $D \da G/K$, the quotient $\dmodgamma{ D }{ \Gamma }$ is a locally symmetric space.
It can be expressed as the double coset space
$$
\FG \da \dmodgamma{ D }{ \Gamma } \cong \Gamma \backslash G / K
= \ts{ \Gamma g K \st g \in G } 
,$$
which is a typically a non-proper, quasi-projective complex variety parameterizing representation-theoretic data such as Hodge structures of a fixed type.
Such symmetric spaces $(G,K)$ are classified by the restriction of $\beta$:

- **Euclidean type**: $\left.\beta\right|_{\liep} = 0$,
  
- **Compact type**: $\left.\beta\right|_{\liep} < 0$ (negative definite),

- **Non-compact type**: $\left.\beta\right|_{\liep} > 0$ (positive definite).

For non-compact types, $D$ is a **Hermitian symmetric domain** (HSD): a non-compact, irreducible symmetric space with a $G(\RR)$-invariant complex structure and Hermitian metric. All Hermitian symmetric domains can be realized as bounded domains in $\CC^n$ via the **Harish-Chandra embedding**. They admit a classification due to Cartan; the non-exceptional types are:

| Type      | Standard Description                           | Realization as Homogeneous Space                        |
|-----------|------------------------------------------------|--------------------------------------------------------|
| I$_{p,q}$ | Complex Grassmannian of $p$-dimensional subspaces | $\SU_{p,q}/S(\U_p\times\U_q)$ |
| II$_n$    | Lagrangian Grassmannian (orthogonal type)      | $\SO_{2n}^*(\RR)/\U_n$                      |
| III$_n$   | Siegel upper half space (symplectic type)      | $\Sp_{n}(\RR)/\U_n$              |
| IV$_n$    | Period domains                                 | $\Orth_{2,n}(\RR)/(\Orth_2(\RR)\times\Orth_n(\RR))$   |

: Cartan's classification of the non-exceptional Hermitian symmetric domains.


##### Type I

Type $\I$ domains arise as quotients $D_{p,q}^{\I} = \SU_{p,q}/S(\U_{p}\times\U_{q})$ where $p\leq q$, and consist of $p$-dimensional positive subspaces in $\CC^{p+q}$ with respect to the Hermitian form

\begin{align*}
h(z,w) = z_1 \overline{w}_1 + \cdots + z_p \overline{w}_p - z_{p+1} \overline{w}_{p+1} - \cdots - z_{p+q} \overline{w}_{p+q}.
.\end{align*}

A fundamental example is the **complex upper half-plane**,

\begin{align*}
\HH = \left\{ \tau \in \CC\st \Im(\tau) > 0 \right\} \cong \SL_2(\RR)/\SO_2(\RR)
,\end{align*}

where $\Im(\tau)$ is the imaginary part of $\tau$.
The action of $\SL_2(\ZZ)$ (or congruence subgroups $\Gamma\leq \SL_2(\ZZ)$ thereof) on $\HH$ via Möbius transformations

\begin{align*}
\gamma \cdot \tau = \frac{a\tau + b}{c\tau + d},\quad \gamma = 
\matt abcd \in \Gamma
.\end{align*}

gives rise to the **modular curves** $Y_\Gamma = \Gamma \backslash \HH$, which are coarse moduli spaces for elliptic curves with level structure.

##### Type $\III$

Type $\III$ domains take the form $D_g^{\III} = \Sp_g(\CC)/\U_g$ and consist of $g\times g$ symmetric complex matrices $Z$ whose imaginary part is positive definite -- otherwise known as the **Siegel upper half space**,
$$
\HH_g = \ts{ Z \in M_{g\times g}(\CC)\st  Z^t = Z,\, \Im(Z) > 0 }
,$$ 
where $\Im(Z)$ denotes the imaginary part of the matrix $Z$.
The group $\Sp_{2g}(\ZZ)$ acts by

\begin{align*}
\gamma \cdot Z = (AZ + B)(CZ + D)^{-1},\quad
\gamma = \matt ABCD \in \Sp_{2g}(\ZZ )
,
.\end{align*}

producing a coarse moduli space for complex principally polarized abelian varieties: $\Ag = \Sp_{2g}(\ZZ)\backslash \HH_g$. For genus $g > 1$, via the Torelli map, the moduli space of curves $\Mg$ embeds as an open subset of a suitable arithmetic quotient of a Siegel space.

##### Type IV

Type $\IV$domains are open subsets of quadric surfaces defined as

\begin{align*}
\halfpd{T} \da\ts{ [v]\in \PP(T_\CC) \st v^2 = 0, v\bar{v} > 0 }^\circ
.\end{align*}

where $L$ is a lattice of signature $(2,n)$ and $(\cdot,\cdot)$ denotes the complex *bilinear* extension of the intersection pairing to $L_\CC$. These domains can be realized as open subsets of quadric hypersurfaces in projective space, $Q = \ts{ [\omega] \in \PP^{n+1} \st (\omega, \omega) = 0 }$, and the boundary components of their Baily-Borel compactifications encode possible limiting mixed Hodge structures of varieties.

#### Cusps Parabolic Subgroups

To compactify $\FG$, one must analyze the boundary of $D$. This is achieved via the **Borel embedding**, a $G(\RR)$-equivariant holomorphic open immersion $D \injects D^\vee$, where $D^\vee$ is the **compact dual**. $D^\vee$ can be realized as $\widetilde{G}/K$, where $\widetilde{G}$ is the simply connected complex Lie group with Lie algebra $\widetilde{\lieg} \da  \liek + i\liep \subset \lieg \tensor_{\RR} \CC$.
The boundary of the closure of $D$ in $D^\vee$, denoted $\bd D$, decomposes as a disjoint union of maximal connected complex-analytic subsets, known as **boundary components** or **cusps**, $\bd D = \Disjoint F_i$.
For each such component $F$, its stabilizer in $G(\RR)$ is the parabolic subgroup
$$
N_F \da  \ts{ g \in G(\RR) \st  g F = F }
.$$
The maximal parabolic subgroups of $G(\RR)$ are precisely those arising as stabilizers $N_F$ of boundary components $F$, and thus there is a bijective correspondence

\begin{align*}
\left\{\text{Boundary components}\; F \subseteq \bd D\right\} \longleftrightarrow \left\{\text{Max. parabolic subgroups}\; P \leq G\right\}
.\end{align*}

A boundary component $F$ is **rational** if its stabilizer $N_F$ is defined over $\QQ$. Let $B(D)$ be the collection of proper rational boundary components. The set $B(D)$ is in a natural bijection with the set of proper maximal parabolic $\QQ$-subgroups of $G$. The boundary is thus stratified by its rational components:
$$
\bd D = \Disjoint_{F \in B(D)} F \subseteq D^{\vee}
$$

#### The Rational Closure

The Baily–Borel compactification of $\FG \da \dmodgamma{ D }{ \Gamma }$, denoted $\bbcpt{\FG}$, is constructed from the **rational closure** of $D$:

\begin{align*}
D^* \da  D \cup \bd D \da D\cup \Disjoint_{F \in B(D)} F
.\end{align*}

The arithmetic group $\Gamma$ acts naturally on $D^*$ with only finitely many orbits of boundary strata. The compactification is the quotient space, which can also be expressed as the quotient of $D$ with its boundary adjoined:

\begin{align*}
\bbcpt{\FG} \da \dmodgamma{D^*}{ \Gamma } 
= \dmodgamma{(D \cup \bd D)}{ \Gamma }
.
.\end{align*}

By the main theorem of Baily and Borel, $\bbcpt{\FG}$ is a compact and Hausdorff space that contains $\FG$ as a dense open subset whose boundary $\bd \bbcpt{\FG} \da \bbcpt{\FG} \setminus \FG$ is a finite disjoint union of closed, locally symmetric varieties:
$\bbcpt{\FG} \setminus \FG = \Disjoint{[F] \in \dmodgamma{B(D)}{\Gamma} } V_F$
where the indices $[F]$ run over $\Gamma$-orbits rational boundary components. Each component $F$ is itself a Hermitian symmetric domain (or possibly a point), and the stratum $V_F$ is its arithmetic quotient, and we can write
\begin{align*}
V_F &= F / N_\Gamma(F) \where
N_\Gamma(F) \da \Stab_\Gamma(F) / \Fix_\Gamma(F),
\\
\Aut(V_F) &= G_F \da \Stab_{G(\RR)}(F) / \Fix_{G(\RR)}(F)
.\end{align*}
Since $F$ is rational, $N_\Gamma(F)$ is a discrete arithmetic subgroup of the Lie group $G_F$. As $F$ is an HSD, the quotient $V_F$ inherits the structure of a locally symmetric variety.

#### Projectivity via Automorphic Forms

A foundational result of @BB66 is that $\bbcpt{\FG}$ can alternatively be constructed from the space of automorphic forms for $\Gamma$ and a canonical automorphic line bundle, showing it is a normal projective variety.
Letting $D = G(\RR)/K$ be a Hermitian symmetric domain associated to a symmetric pair $(G, K)$, and $\Gamma \subset G(\QQ)$  be an arithmetic subgroup acting properly discontinuously on $D$ as above, there is a distinguished $G(\RR)$-equivariant ample line bundle $\mcl = \mcl_\chi$ on $D$ defined by a particular character $\chi: K\to \CCstar$. In cases of interest, such as the Siegel and Type $\IV$ cases $D = \Sp_g(\RR)/\U_g$ or $D = \Orth_{2,n}(\RR)/(\Orth_2(\RR)\times\Orth_n(\RR))$, the bundle $\mcl$ is the determinant of the Hodge bundle or the inverse tautological bundle, respectively, where for a smooth, proper family of $n$-dimensional varieties $\pi: X \to S$, the **Hodge bundle** is the vector bundle $\EE \da  \pi_*\Omega^n_{X/S}$ whose fiber over $s \in S$ is $H^0(\Omega^n_{X_s})$, the space of global holomorphic $n$-forms on the fiber $X_s$. For $\Mg$, this reduces to the pushforward $\pi_* \omega_{\mcc/\Mg}$ of the relative dualizing sheaf of the universal curve $\pi: \mcc \to \Mg$, and for $\Ag$ one often passes to its determinant, the **Hodge line bundle**.

For arithmetic groups $\Gamma$ as above, an **automorphic form of weight $k$ for $\Gamma$** (with *factor of automorphy* $j$) is a holomorphic section $f \in H^0( \mcl^{\tensor k})$ of the $k$th tensor power of $\mcl$ such that the $\gamma^* f = f$ for all $\gamma \in \Gamma$.
Locally, this recovers the familiar automorphy condition
$$
f(\gamma \cdot z) = j(\gamma, z)^k \cdot f(z) \qquad \text{for all } \gamma \in \Gamma, z\in D
.$$
We define the space of weight $k$ $\Gamma$-automorphic forms as the invariants sections of $\mcl^{\tensor k}$, which assemble to a graded ring:
$$
A_k(\Gamma) \da  H^0(D, \mcl^{\tensor k})^\Gamma,
\qquad
R_\Gamma \da \bigoplus_{k \geq 0} A_k(\Gamma)
.$$
@BB66 shows that that $R_\Gamma$ is a finitely generated $\CC$-algebra, and there is an identification $\bbcpt{\FG} \cong \Proj(R_\Gamma)$.
Moreover, $\mcl$ descends to an ample line bundle on $\bbcpt{\FG}$ and the sections of $\mcl^{\tensor k}$ satisfy the analytic growth conditions at cusps of $\FG$ in analogy to classical modular forms for $\SL_{2}(\ZZ)$.
This construction is canonical and functorial: any $(\Gamma_1, \Gamma_2)$-equivariant morphism $F_{\Gamma_1} \to F_{\Gamma_2}$ compatible with $\mcl_1$ and $\mcl_2$ extends uniquely to a morphism between their Baily–Borel compactifications. However, this typically introduces singularities on $\bd\bbcpt{\FG}$, motivating further refinements, e.g., semitoroidal or KSBA compactifications.

#### Cusps and Boundary Strata

Let $T$ be an even lattice of signature $(2, n)$, let $\Gamma\leq \Orth(L)$ be a (neat) arithmetic subgroup, and let $D \da \halfpd{T}$ be the corresponding period domain with arithmetic quotient $\FG \da \dmodgamma{ \halfpd{T} }{ \Gamma }$.
The rational boundary components of $D$ have dimensions $0$ ("Type $\III$") or $1$ ("Type $\II$"). There are canonical bijections between $\Gamma$-orbits of the following sets:

- Rational boundary components of $D$,
- Rational parabolic subgroups $P \leq \Orth(T_\QQ)$, and
- Primitive isotropic subspaces $I \subset T_\QQ$.

This correspondence is explicitly as follows: to each primitive isotropic subspace $I \subset T_\QQ$ of rank $k$ (with $1 \leq k \leq 2$), associate the boundary component $F_I$ of dimension $k-1$ described as follows: writing $D$ as $G(\RR)/K$, a boundary component $F_I$ corresponds to an isotropic sublattice $I$ if and only if $\Stab_G(I) = \Stab_G(F_I)$.
If $k=1$, then $I$ is a line and $F_I$ is a point, and if $k=2$, the component $F_I$ is a modular curve with level structure.
These bijections are compatible with the natural poset structures: inclusion $I_1 \subset I_2$ induces $F_{I_2}$ contained in the closure of $F_{I_1}$, and parabolic subgroups are partially ordered by inclusion. We grade isotropic sublattices by rank, boundary components by dimension, and parabolic subgroups by the dimension of their unipotent radical.
The above bijection then extends to an isomorphism of $\ZZ$-graded posets, up to a shift: rank $k$ isotropic sublattices correspond to boundary components of dimension $k-1$.
This is the fundamental bijection which makes $\bbcpt{\FG}$ accessible by lattice-theoretic methods.

To conclude, let $\eta \in T$ be a primitive isotropic vector and set $\bdlattice{T}{\eta} \da  \eta^{\perp T}/\langle\eta\rangle$, which is an even lattice of signature $(1, n-1)$. Recall that the **stable boundary group** is defined as $\Gamma_\eta \da  \Stab_\Gamma(\eta)/U_\eta$, where $\Stab_\Gamma(\eta)$ is the stabilizer of $\eta$ in $\Gamma$ and $U_\eta$ is its unipotent radical. Associated to $\Gamma_\eta$ is its **stable reflection group** $W(\Gamma_\eta) \subseteq \Orth(\bdlattice{T}{\eta})$, generated by reflections in roots of $\bdlattice{T}{\eta}$ contained in $\Gamma_\eta$. Denote by $\thecone{C}(\Gamma_\eta)$ the *fundamental chamber*, which is the convex polyhedral cone in $\bdlattice{T}{\eta, \RR}$ consisting of those vectors $v$ satisfying $(\alpha, v) \geq 0$ for each simple root $\alpha$ corresponding to the chosen system of reflections.
The local data for a toroidal compactification at the $0$-cusp $F_\eta$ comes from attaching a toric variety constructed from the positive cone and its rational closure,

\begin{align*}
\thecone{C}_\eta \da  \ts{
v \in \bdlattice{T}{\eta, \RR} \st v^2 > 0
}
\qquad
\thecone{C}_{\eta,\QQ} \da  
\thecone{C}_{\eta, \RR} \union \ts{ v\in \bdlattice{T}{\eta, \QQ} \st v^2 = 0}
,
.\end{align*}

where we implicitly choose a component of the full cone satisfying $x\cdot h \geq 0$ for a fixed vector $h$.
After projectivization, $\PP(\thecone{C}_\eta) \cong \thecone{C}_\eta / \RR_{>0}$ is identified with $\HH^{n-1}$. The stable reflection group $W(\Gamma_\eta)$ acts discretely on this space by isometries, with fundamental chamber $\thecone{C}(\Gamma_\eta)$ yielding a convex (possibly non-compact) hyperbolic polytope bounded by the reflection hyperplanes in the roots of $\bdlattice{T}{\eta}$.

One must choose a $\Gamma_\eta$-invariant rational polyhedral fan $\Sigma(\eta)$ supported on $\thecone{C}_{\eta, \QQ}$. A particularly canonical choice, when $W(\Gamma_\eta)$ is sufficiently large enough and defines a locally finite arrangement, is the **Coxeter fan**: the rational polyhedral decomposition of $\thecone{C}_{\eta, \QQ}$ whose cones are in bijection with the $W(\Gamma_\eta)$-translates of $\thecone{C}(\Gamma_\eta)$.
This yields a tiling of $\HH^{n-1}$ by Coxeter polytopes, where each chamber is in bijection with a fan in $\thecone{C}_{\eta, \QQ}$ and their gluing data is determined by the combinatorics of $W(\Gamma_\eta)$.
In general, other $\Gamma_\eta$-invariant fans $\Sigma(\eta)$ may be chosen; however, when the Coxeter fan is well-defined and locally finite, it provides a natural, symmetric choice . 
Globally, the collection of all such fans $\{\Sigma(\eta)\}$ ranging over all $k$-cusps $\eta$ produces a **toroidal compactification** $\torcpt{\FG}$. Locally, analytic neighborhoods of cusps $\eta$ are described via open subsets in the respective toric varieties $X_{\Sigma(\eta)}$, which assemble to form a normal, complex algebraic space $\torcpt{\FG}$ that naturally maps to $\bbcpt{\FG}$.
