### KSBA Compactifications {#setion-5-3}

#### Introduction

For higher-dimensional varieties, GIT, toroidal, and semitoroidal compactifcations are often inadequate, producing boundary points that lack modular interpretations and possibly corresponding to degenerations with excessively severe singularities. For instance, GIT compactification $F_2$ result in boundary strata containing highly singular, non-separated, or even non-reduced curves.
Such limiting surfaces may not be uniquely determined by one-parameter degenerations, violating the valuative criterion for properness and separatedness. Moreover, GIT boundaries often allow non-slc singularities, which are more severe than those typically permitted by the MMP (see e.g., [@Sha81], [@Loo86]).
In contrast, for curves of genus $g \geq 2$, Deligne and Mumford compactify $\Mg$ using **stable curves**: a (connected, reduced, projective) curve $C$ over an algebraically closed field is **stable** if all singularities of $C$ are nodes and every rational component of $C$ meets the rest of $C$ (including the marked points) in at least $3$ points. The moduli functor $\Mg^{\operatorname{DM}}$ assigning to each connected base $S$ the groupoid of flat, proper families $\mcc \to S$ whose fibers are stable curves, is represented by a proper Deligne–Mumford stack. The boundary $\bd\Mg$ parameterizes connected, nodal curves with finite automorphism groups, and every family $\open{C}$ over $\open{S} = S \setminus \ts{0}$ admits, after a ramified base change, a unique stable limit by semistable reduction and relative abundance of $\omega_{C/S}$ (see [@DM69], [@KM98]).
The **boundary strata** of $\bd\Mg$ are indexed by **dual graphs** recording the incidence data of components and their intersections -- each stable degeneration's combinatorial "type" corresponds to the dual graph of its $\mcx_0$, and each such graph describes a distinct boundary stratum.

To generalize this to higher dimension, one introduces **stable pairs** $(X, B)$, following @KS88, @Ale96.
Such a pair is **KSBA stable** if:

- $X$ is a projective, reduced, equidimensional, *demi-normal* variety of dimension $d \geq 2$,
- $B = \sum b_i B_i$ is an effective $\QQ$-divisor, $0 < b_i \leq 1$,
- The pair $(X, B)$ has **semi-log-canonical (slc) singularities**,
- $K_X + B$ is ample.

KSBA stability ensures:

- (**Properness**) Any flat family $(\mcx^*, \mcb^*) \to \Delta^*$ over the punctured disk extends, after finite base change, to a family $(\mcx, \mcb) \to \Delta$ of stable pairs with $\mcx_0$ $(X_0, B_0)$ slc and $K_{X_0} + B_0$ ample.

- (**Separatedness**) Any isomorphism over $\Delta^*$ extends uniquely over $\Delta$.

- (**Modularity**) Every point of the boundary parameterizes a unique, geometrically meaningful, slc limit.

For curves, setting $d=1$ and $B$ the be the sum of markings, this recovers the notion of stable curves as $\omega_C(\sum_i p_i)$ ample and only nodes allowed.
However, unlike the case of curves, where all stable curves are smoothable, not every stable variety is a limit of smooth ones.
Thus, boundary components can include non-smoothable varieties, yielding compactifications that potentially have multiple irreducible components.
Fixing discrete invariants -- the dimension $d$, a Hilbert polynomial $h$, boundary coefficients $\{b_i\}$, and the **volume** $(K_X + B)^d$ --, the **KSBA moduli functor**
$\cpt{\mcm}_{d, \vec{b}, v}:
\Sch^{\opop} \to \Set$
assigns to $S$ the set of isomorphism classes of flat families $(\mcx, \mcb) \to S$ of KSBA stable pairs with these invariants. This functor is represented by a proper, separated Deligne–Mumford stack $\mcm$, whose coarse moduli space $M$ is a projective scheme [@KS88, Thm. 1.1]. The closure of the locus of smooth pairs in $\mcm$ provides a geometrically meaningful compactification by stable pairs.

For K3 or Enriques surfaces, $K_X \equiv 0$ is numerically trivial, so to ensure ampleness one considers **pairs** $(X, \eps R)$ for $0 < \eps \ll 1$, $R$ ample divisor, and studies the stable pair locus for these data. The divisor $R$ is typically chosen to be the ramification divisor of an automorphism, and the compactification is independent of $\eps$ for $\eps$ sufficiently small ([@KS88, §5], [@Ale96a, §6], [@Kol23, Lemma VI.1.1], [@AET23]).
For $K3$ surfaces with polarization of degree $2d$, a **divisor model** refers to the representation of a $K3$ surface $X$ together with an ample Cartier divisor $L$ of degree $2d$ -- concretely, for $d = 1$, this is a double cover of $\PP^2$ branched along a sextic.
The stability condition requires $(X, L)$ to be log canonical with $K_X + L$ ample.
The KSBA compactification $\ksbacpt{F}_{2d}$ for such pairs compactifies the moduli space of smooth pairs $(X, L)$ by adding K3 surface pairs with at worst ADE/slc singularities.
These are parameterized by **integral affine spheres** $\IAS^2$ with 24 singularities.
For Enriques surfaces the boundary of the KSBA compactification naturally includes **half-divisor models**: pairs $(Z, \Delta)$, where $Z$ is an Enriques surface and $\Delta$ is an effective Weil divisor determined by the universal K3 cover $X\to Z$, often defined only up to numerical equivalence or descent $X$. These are in turn parametrized by $\IAS^2$ with involutions.


#### Singularities

:::{.definition title="Demi-normal Variety" #sing-deminormal}
A variety $X$ is **demi-normal** if $X$ is reduced, $X$ is $S_2$ and normal crossing in codimension one (every codimension one singularity is analytically isomorphic to a normal crossing or ordinary node).
:::

:::{.definition title="Serre’s $S_2$ Condition" #sing-s2}
A Noetherian scheme $X$ satisfies **Serre’s $S_2$ condition** if, for every $x\in X$,
$\operatorname{depth}\, \OO_{X,x} \geq \min\{2, \dim \OO_{X,x}\}.$
For surfaces, $S_2$ implies $X$ is Cohen–Macaulay in codimension one.
:::

:::{.definition title="Simple Normal Crossings (snc)" #sing-snc}
A variety $X$ has **simple normal crossings (snc)** singularities if, at each point $x \in X$, there exists an analytic or étale neighborhood isomorphic to

\begin{align*}
(x_1 x_2 \cdots x_k = 0)\subset \AA^n
\end{align*}

for some $k \leq n$, i.e., $X$ locally looks like $k$ coordinate hyperplanes.
:::

:::{.definition title="Gorenstein and $\QQ$-Gorenstein Varieties" #sing-gor-qgor}
A scheme $X$ of pure dimension is **Gorenstein** if it is Cohen–Macaulay and its dualizing sheaf $\omega_X$ is invertible.
$X$ is **$\QQ$-Gorenstein** if $\omega_X$ is $\QQ$-Cartier, i.e., some positive tensor power $\omega_X^{\otimes m}$ is invertible for $m > 0$.
:::

:::{.definition title="ADE Singularities (Du Val, Rational Double Points)" #pairs-ade}
An **ADE singularity** (Du Val or rational double point) is a normal surface singularity whose minimal resolution has exceptional curves intersecting according to an ADE Dynkin diagram with analytic forms:

\begin{align*}
A_n &\colon x^2 + y^2 + z^{n+1} = 0 \\
D_n &\colon x^2 + y^{n-1} + y z^2 = 0 \\
E_6 &\colon x^2 + y^3 + z^4 = 0 \\
E_7 &\colon x^2 + y^3 + y z^3 = 0 \\
E_8 &\colon x^2 + y^3 + z^5 = 0
\end{align*}

:::

:::{.definition title="Normalization and Double Locus" #sing-normalization}
Let $X$ be a reduced, demi-normal scheme, as defined above.
The **normalization** of $X$ is a finite birational morphism

\begin{align*}
\nu\colon \cpt{X} \to X
.\end{align*}

with $\normalize{X}$ normal, universal among morphisms from normal schemes to $X$.
:::

:::{.definition title="The Conductor Subscheme and Double Locus"}
Let $X$ be a reduced scheme and let $\nu: \widetilde{X} \to X$ denote its normalization. The **conductor ideal sheaf** is defined as

\begin{align*}
\mathcal{C}_X := \operatorname{Ann}_{\OO_X}\big( \nu_* \OO_{\widetilde{X}} / \OO_X \big).
.\end{align*}


This ideal sheaf gives rise to two closed subschemes:

- The **conductor subscheme** (or **conductor locus**) on $X$, defined by $\mathcal{C}_X \subseteq \OO_X$. This locus coincides with the points where $\nu$ is not an isomorphism, i.e., where $X$ is not normal.
- The **conductor divisor** on $\widetilde{X}$, which is the closed subscheme cut out by pulling back the conductor ideal via $\nu$.

The **double locus** of $X$ is the support of the conductor subscheme on $X$. Equivalently, it is the locus where $X$ fails to be normal—typically, the set of points where two or more local analytic branches of the normalization are identified in $X$.


:::

For algebraic surfaces, the double locus is a (possibly reducible) disjoint union of curves (i.e., it is of pure codimension one). In higher dimensions, the conductor always has pure codimension one in $X$. The preimage of the conductor divisor in $\widetilde{X}$ records the precise locations where the gluing occurs in the normalization, thus encoding the identification data required to reconstruct $X$ from its normalization.
Normalization replaces a reduced scheme $X$ with a normal scheme $\normalize{X}$ up to birational equivalence, and the fibers of $\normalize{X}\to X$ encode the branching behavior of the singularity at that point. 
Its practical implications by dimension are as follows:

- $\dim(X) = 1:$ The normalization of a reduced curve $C$ is a smooth curve $\widetilde{C}$.

- $\dim(X) = 2:$ Normalization resolves all non-normal singularities, such as double curves and cusps, and more generally all 1-dimensional singularities, leaving only singularities at isolated points (which are typically ADE or quotient singularities).

- $\dim(X) \geq 3:$ The singular locus of $\normalize{X}$ is of codimension at least 2, and consists of *normal singularities* -- these can generally be complicated.


:::{.theorem title="Zariski's Main Theorem (Recognition Theorem for Normalizations)"}
Let $X$ be a reduced, separated, Noetherian scheme, and let $f \colon Y \to X$ be a morphism. Then $f$ is (up to unique isomorphism) the normalization of $X$ if and only if:

1. $Y$ is normal,
2. $f$ is finite and birational,
3. $f$ restricts to an isomorphism over the open subset of $X$ where $X$ is normal (i.e., over the normal locus of $X$).

In other words, any morphism with these three properties realizes $Y$ as the normalization of $X$.
In particular, if $X$ is an irreducible, reduced, separated variety over $\CC$ such that

1. $Y$ is normal and irreducible, and
2. $f$ is finite and birational,

then $Y$ is the normalization of $X$ and $f$ is the normalization morphism. In this case, $f$ is an isomorphism over the smooth locus of $X$.
:::

#### Pairs

:::{.definition title="Log Pair $(X, D)$" #pairs-logpair}
A **log pair** is a pair $(X, D)$, where $X$ is a normal variety over $\CC$ and $D = \sum d_i D_i$ is an effective $\QQ$-divisor on $X$ with coefficients $0 \leq d_i \leq 1$.
:::

:::{.definition title="Log Canonical (lc) Singularities" #pairs-lc}
Let $X$ be a normal variety over $\CC$, and let $R = \sum r_i R_i$ be an effective $\QQ$-divisor with $0 \leq r_i \leq 1$.
For any log resolution $f\colon Y \to X$, and for each prime divisor $E$ on $Y$, the **discrepancy** $a(E, X, R)$ is defined by

\begin{align*}
K_Y = f^*(K_X + R) + \sum_E a(E, X, R)\, E.
.\end{align*}

Let $(X, D)$ be a log pair, where $X$ is a normal variety and $D$ is a $\QQ$-divisor. The pair is said to be **log canonical** (lc) if $K_X + D$ is $\QQ$-Cartier and, for every log resolution $f: Y \to X$ and every prime divisor $E$ on $Y$, the discrepancy satisfies $a(E, X, D) \geq -1$. A **log canonical center** of $(X, D)$ is the image $f(E) \subseteq X$ of a prime divisor $E$ on some log resolution $f: Y \to X$ with discrepancy $a(E, X, D) = -1$; this locus is precisely where the singularities of the pair are exactly log canonical.
:::

### Classes of Singularities for Pairs $(X, D)$

The minimal model program (MMP) distinguishes four main classes of singularities for pairs, ordered by the values their discrepancies may attain. Let $f: Y \to X$ be any log resolution and $E$ a prime divisor on $Y$.
Let $(X, D)$ be a normal pair with $K_X + D$ $\QQ$-Cartier. For a birational morphism $f : Y \to X$, and a prime divisor $E \subset Y$, the discrepancy $a(E, X, D)$ is defined via the relation
$$
K_Y + D_Y = f^*(K_X + D) + \sum_E a(E, X, D) \cdot E,
$$
where $D_Y$ is the strict transform of $D$. The classification of singularities according to the discrepancy function is given below.

| **Class**                   | **Discrepancy** $a = a(E, X, D)$ | **Typical Applications**                              |
| --------------------------- | -------------------------------- | ----------------------------------------------------- |
| Terminal                    | $a > 0$                          | Minimal models in $\dim \geq 3$                       |
| Canonical                   | $a \geq 0$                       | Canonical models; moduli of varieties of general type |
| Kawamata log terminal (klt) | $a > -1$                         | Singularities allowed in the MMP                      |
| Log canonical (lc)          | $a  \geq -1$                     | Stable pairs; compactifications                       |

: Classification of singularities of a pair by the discrepancy function.

* **Terminal:** All discrepancies are strictly positive. Such singularities are the mildest allowed in the context of minimal models in dimension at least three, ensuring $\QQ$-factoriality and smoothness in codimension two.

* **Canonical:** Discrepancies are nonnegative. Canonical singularities permit discrepancies to vanish but exclude boundary contributions with coefficient one. They are characteristic of canonical models and appear naturally in the classification of varieties of general type.

* **Kawamata log terminal (klt):** All discrepancies satisfy $a(E, X, D) > -1$. These include quotient singularities and allow boundary divisors with coefficients in $(0,1)$. klt pairs form the primary class of singularities admissible in the Minimal Model Program.

* **Log canonical (lc):** Discrepancies satisfy $a(E, X, D) \geq -1$. This is the broadest class considered in the birational classification of pairs, accommodating boundary components with coefficient one. lc singularities are essential in the theory of stable pairs and in the construction of compactified moduli spaces.

When the condition $a(E, X, D) \geq -1$ is enforced, the essential steps of the MMP -- flips, divisorial contractions, and the extraction of minimal and canonical models -- can be performed, and the canonical ring remains finitely generated. If one allows singularities with discrepancies less than $-1$, these procedures can fail, and fundamental theorems such as the existence of minimal models or the finiteness of the canonical ring may break down. Thus, log canonical singularities constitute the maximal class for which the program is expected to be valid.
Canonical and log canonical singularities appear naturally on canonical models of varieties of general type, and this inclusion ensures that the canonical ring has the necessary finiteness properties. The MMP is specifically designed so that, under finite generation, canonical models admit at worst lc singularities, which are thus the natural endpoint for varieties of general type constructed via the MMP.

:::{.definition title="Divisorial Log Terminal (dlt) Singularities" #pairs-dlt}
A pair $(X, D)$, where $X$ is normal and $D$ is an effective $\QQ$-divisor, is said to be **divisorial log terminal (dlt)** if $K_X + D$ is $\QQ$-Cartier, and there exists a log resolution $f \colon Y \to X$ such that:

- for every $f$-exceptional divisor $E$, the discrepancy $a(E, X, D) > -1$,
- the union of the strict transform of $D$ with the $f$-exceptional divisors is a simple normal crossings (snc) divisor,
- all log canonical centers are contained in the support of the strict transform of $D$.

:::

:::{.definition title="Semi-Log Canonical (slc) Pairs" #pairs-slc}
Let $X$ be a demi-normal scheme and $R = \sum r_i R_i$ an effective $\QQ$-divisor on $X$ with $0 \leq r_i \leq 1$. The pair $(X, R)$ is called **semi-log canonical (slc)** if:

1. $K_X + R$ is $\QQ$-Cartier.

2. $(\normalize{X}, R^\nu)$ is log canonical, where $\nu\colon \normalize{X} \to X$ is the normalization of $X$ and
   
\begin{align*}
R^\nu \da  D + \sum r_i\, \nu^*(R_i).
\end{align*}

   where $D$ be the conductor divisor on $\normalize{X}$.

:::

Semi-log canonical singularities generalize lc singularities to possibly non-normal varieties. In this setting, $X$ is allowed to have certain mild singularities, notably double crossings in codimension one. The normalization $\nu: \widetilde{X} \to X$ separates these non-normal loci, and the conductor divisor $D \subset \widetilde{X}$ records the preimage of the non-normal (double) locus of $X$. The pair $(\widetilde{X}, R^\nu)$ combines the pullback of $R$ and the conductor divisor, and being lc in this setting captures the requirement that singularities of the normalization and the identifications along the conductor divisor are at worst log canonical; that is, all discrepancies for the pair $(\widetilde{X}, R^\nu)$ are at least $-1$, both on the components of $\widetilde{X}$ and along the loci where the components are glued together via the conductor.
This allows the extension of the MMP and moduli of pairs to schemes that are not necessarily normal or irreducible. In particular, slc pairs arise naturally as stable limits of pairs in families where the total space acquires non-normal singularities, making them central objects in the compactification of moduli spaces of pairs.


:::{.definition title="Quasi-polarized Minimal Resolutions and Deformation Types" #pairs-qp-minimalres}
Given a pair $(X, R)$, where $X$ is a surface with at worst ADE or quotient singularities and $R$ is a nef (or ample) divisor, the **quasi-polarized minimal resolution** is the pair $(\tilde{X}, f^* R)$, where $f \colon \tilde{X} \to X$ is the minimal crepant resolution of $X$.
The **deformation type** of a (possibly singular) surface with an ample line bundle (or quasi-polarization) is the isomorphism class (up to analytic or algebraic equivalence) of its quasi-polarized minimal resolution.
:::

#### Numerical Conditions and Models

:::{.definition title="Big and Nef Divisors" #div-big-nef}
Let $D$ be a $\QQ$-Cartier divisor on a projective surface $X$:

- $D$ is **nef** (numerically effective) if $D \cdot C \geq 0$ for every irreducible curve $C \subset X$.

- $D$ is **big** if its volume is positive,

  \begin{align*}
  \operatorname{vol}_X(D) \da  \limsup_{m \to \infty} \frac{h^0(X, \OO_X(mD))}{m^{\dim X}/\dim X!} > 0
  .\end{align*}

:::

:::{.definition title="Polarizing, Primitive, and Quasi-Polarizing Divisors" #div-polarization}
Let $X$ be a projective variety.
A **polarizing divisor** is an ample Cartier divisor $R$ on $X$.
We say $R$ is a **quasi-polarizing divisor** if it is only big and nef, but not necessarily ample.
It is **primitive** if its class in $\operatorname{Pic}(X)$ cannot be written as $kL'$ for any integer $k > 1$ and any divisor $L'$.
:::

Ample divisors guarantee that $X$ is projective. making polarizations especially common in moduli problems, where it ensures that the moduli stack is proper and separated. Nefness provides a numerical positivity condition that yields well-defined numerical invariants, and since it is preserved under birational equivalence, it ensures that the singularities of degenerations are mild enough to be controlled by the MMP. Bigness is a maximality condition, selecting divisors whose sections grow like ample divisors.
Quasi-polarizations arise naturally as limits of polarizations: degenerations of polarized KSBA pairs can induce a loss of ampleness, while bigness and nefness persist. Finally, primitivity imposes a minimality and uniqueness condition (up to isomorphism) on the divisor class, ensuring that each isomorphism class is represented exactly once in the corresponding moduli problem, avoiding redundancies due to rescaling.

:::{.definition title="Nef Model" #hdm-nefmodel}
Let $\mcx^* \to \Delta^*$ be a flat family over a punctured disk, and let $\mcl^*$ be a relatively big and nef line bundle on $\mcx^*$. A **nef model** for $(\mcx^*, \mcl^*)$ is a pair $(\mcx, \mcl)$ where:

- $\mcx \to \Delta$ is a flat extension of $\mcx^* \to \Delta^*$ (often a Kulikov or semistable model),
- $\mcl$ is a line bundle on $\mcx$ extending $\mcl^*$,
- $\mcl$ is relatively nef and big over $\Delta$.
:::

Given a family $\mathcal{X}^* \to \Delta^*$ of smooth varieties over a punctured disk and a relatively big and nef line bundle $\mathcal{L}^*$ or an effective divisor $\mcr^* \subset \mathcal{X}^*$, the problem is to construct canonical extensions of this data over the whole disk $\Delta$, especially over the $\mcx_0$ $\mathcal{X}_0$.

Such extensions must satisfy several requirements dictated by the geometry of degenerations and the construction of compactified moduli spaces:

- The extension $(\mathcal{X}, \mathcal{L})$ or $(\mathcal{X}, \mcr)$ must be flat over $\Delta$, so that the fibers capture the correct limit structure as the family degenerates.
   Note that flatness of a family ensures that the fibers vary in a "continuous" manner from a scheme-theoretic perspective, yielding equidimensionality and consistent Hilbert polynomial across the family.

- The positivity properties of the line bundle or divisor—such as nefness and ampleness—must be preserved on the total space to ensure that the relevant moduli functor remains separated and proper.
- In the case of divisors, compatibility with the stratification of the $\mcx_0$ is essential: the $\mcx_0$ of the divisor should avoid all strata of the possibly singular $\mcx_0$, so as not to introduce unwanted components or increase the complexity of the limit.

Precisely formulating these extensions is essential for defining and constructing stable limits. They form the starting point for constructing stable limits, which are stable pairs arising as canonical limits of smooth pairs in families.
The following definition captures the precise requirements for extending divisors across degenerations:

:::{.definition title="Divisor Model" #hdm-divmodel}
Let $\mcx^* \to \Delta^*$ be a family of varieties over a punctured disk and let $\mcr^* \subset \mcx^*$ be an effective divisor (usually a section of a relatively nef and big line bundle). A **divisor model** for $(\mcx^*, \mcr^*)$ is a pair $(\mcx, \mcr)$, where:

- $\mcx \to \Delta$ is a flat family extending $\mcx^* \to \Delta^*$,
- $\mcr$ is an effective divisor on $\mcx$ restricting to $\mcr^*$ on $\mcx^*$,
- $\mcr$ is relatively nef over $\Delta$,
- The $\mcx_0$ $\mcr_0$ does **not contain any stratum** of the $\mcx_0$ $\mcx_0$; that is, $\mcr_0$ does not contain any irreducible component or singular locus (double curves, triple points, etc.) of $\mcx_0$.
:::

:::{.proposition title="Existence and Uniqueness of Stable Limits via Divisor Models" #hdm-exuniq-prop}
Let $(\mcx^*, \mcr^*)$ be a flat family of smooth pairs over $\Delta^*$. After finite base change, there exists a divisor model $(\mcx, \mcr)$ as above. The associated **stable model** is the pair $(\cpt{\mcx}, \cpt{\mcr} )$, where
$$
(\cpt{\mcx}, \cpt{\mcr}) \da  \Proj_\Delta \left(\bigoplus_{n \geq 0} H^0(\mcx, \OO_{\mcx}(n \mcr))\right)
.$$
For $0 < \eps \ll 1$, the pair $(\cpt{\mcx}, \eps \cpt{\mcr})$ is KSBA-stable: $\cpt{\mcx}$ has slc singularities and $K_{\cpt{\mcx}} + \eps \cpt{\mcr}$ is ample.

This stable limit is unique up to isomorphism (after base change), and the construction is functorial in families. It provides a canonical procedure for extending any family of smooth pairs to a stable pair in the boundary of the KSBA moduli space, ensuring the properness of the compactification.
:::

:::{.definition title="Half-Divisor Model" #hdm-halfdivisor}
A **half-divisor model** is a pair $(\mcz, \mcr_{\mcz})$ consisting of a flat family $\mcz \to C$ over a base curve $C$, together with a divisor $\mcr_{\mcz} \subset \mcz$, such that the pair arises as the quotient of a divisor model $(\mcx, \mcr) \to C$ by a fixed-point-free involution $\tau$ with $\mcr$ anti-invariant (i.e., $\mcr$ does not descend as a Cartier divisor, but $2\mcr$ does).
Equivalently, $(\mcz, \mcr_{\mcz})$ is locally modeled as $(\mcx/\tau, \mcr/\tau)$ where $\mcr$ is a "half" of a Weil divisor that becomes Cartier only after passing to the double cover.
:::

Let $\mathcal{X} \to C$ be a flat family of K3 surfaces over a smooth curve, equipped with a fixed-point-free involution $\tau$, and let $\mcr \subset \mathcal{X}$ be an effective Cartier divisor that is anti-invariant under $\tau$ (i.e., $\tau^* \mcr = -\mcr$). The quotient family

\begin{align*}
\pi \colon (\mathcal{X}, \mcr) \to (\mcz, \mcr_{\mcz})
.\end{align*}

with $\mcz = \mathcal{X} / \langle \tau \rangle$, yields a family of Enriques surfaces together with a divisor $\mcr_{\mcz}$ defined as the scheme-theoretic image of $\mcr$.
In general, $\mcr_{\mcz}$ is a Weil divisor on $\mcz$ that is not Cartier, but its double $2\mcr_{\mcz}$ is always Cartier. This reflects a fundamental feature of Enriques surfaces: the divisor defining the marking or polarization typically does not descend to a Cartier divisor through a degree two étale cover with empty branch locus. Instead, the presence of the involution ensures there is global 2-torsion in the divisor class group, leading to the condition $2\mcr_{\mcz}\in \operatorname{CaDiv}(\mcz) \quad \text{but} \quad \mcr_{\mcz}\notin \operatorname{CaDiv}(\mcz).$
This half-divisibility characterizes polarized Enriques surfaces and persists in their degenerations.
When the $\mcx_0$ degenerates ($(\mathcal{X}_0, \mcr_0)$), it may become reducible, and the involution specializes to $\tau_0$ on $\mathcal{X}_0$. The quotient $\mcz_0 = \mathcal{X}_0 / \langle \tau_0 \rangle$ is then a demi-normal surface, and the induced divisor $\mcr_{\mcz_0}$ remains a Weil divisor with $2\mcr_{\mcz_0}$ Cartier. In the context of the KSBA compactification, every boundary stratum corresponding to a stable limit of Enriques surfaces is thus naturally modeled by half-divisor pairs $(\mcz_0, \frac{1}{2} \mcr_{\mcz_0})$, with log-canonical polarization $K_{\mcz_0} + \frac{1}{2} \mcr_{\mcz_0}$ ample, and with semi-log-canonical singularities that may arise both from the quotient construction and from singularities already present in the K3 $\mcx_0$. As discussed in @AEGS25, the structure of degenerations of Enriques surfaces are thus governed by half-divisor models in this way.

#### The KSBA Moduli Stack

:::{.definition title="KSBA Stable Pair"}
Let $X$ be a projective, demi-normal (in particular, $S_2$ and normal crossing in codimension one) variety over an algebraically closed field of characteristic $0$, and let $D = \sum_j a_j D_j$ be an effective $\QQ$-divisor with $0 < a_j < 1$ and each component $D_j$ a Weil divisor whose support does not contain any component of the double locus of $X$.
The pair $(X, D)$ is called a **(KSBA) stable pair** if:

- $(X, D)$ is semi-log-canonical (slc): $X$ is $S_2$; $(X, D)$ is slc as previously described, i.e., the normalization with the conductor plus pullbacks of $D$ is log canonical, and $K_X + D$ is $\QQ$-Cartier,
- $K_X + D$ is ample,
- $\Aut(X, D)$ is finite (which follows from ampleness and $X$ reduced).
:::


:::{.definition title="Dual Complex of a Stable Degeneration"}
Let $\bar{X}$ be a reduced, finite-type, possibly reducible variety arising as the $\mcx_0$ of a degeneration of KSBA stable pairs. The **dual complex** $\Gamma(\bar{X})$ is the simplicial complex defined by:

- **Vertices:** Each irreducible component $\bar{V}_i$ of $\bar{X}$ corresponds to a vertex.

- **$k$-Simplices:** For every connected component of the intersection of $k+1$ distinct irre0ducible components $\bar{V}_{i_0} \cap \bar{V}_{i_1} \cap \cdots \cap \bar{V}_{i_k}$ (with nonempty intersection), include a $k$-simplex whose vertices correspond to the involved components.

- **Faces and Gluing:** The simplices are glued according to inclusions of the corresponding strata.

The dual complex $\Gamma(\bar{X})$ thus encodes precisely the combinatorics of how the irreducible components of the degeneration $\bar{X}$ meet along their strata of higher codimension.
:::


:::{.definition title="KSBA Moduli Functor" #moduli-functor}
Fix numerical invariants (such as dimension $d$, Hilbert polynomial $h$, coefficients $\{a_j\}$, and volume $v = (K_X+D)^d$). The **KSBA moduli functor** is
$$
\mcm\uksba_{d,\vec{a},v} \colon (\Sch/k)^{\opop} \to \Set
$$
assigning to each $S$ the set of isomorphism classes of families of KSBA stable pairs $(\mcx, \mcd ) \to S$ with the fixed invariants.
:::

:::{.definition title="KSBA Moduli Stack and Coarse Moduli Space" #moduli-dmstack}
There exists a Deligne–Mumford stack $\mcm\uksba_{d, \vec{a}, v}$ of finite type over $k$, whose geometric points parametrize KSBA stable pairs with the chosen invariants. The associated **coarse moduli space** $M\uksba_{d, \vec{a}, v}$ is an algebraic space, which is a projective scheme in many important cases.
:::

:::{.theorem title="Properness and Projectivity of the KSBA Moduli Space" #moduli-properness}
The stack $\mcm\uksba_{d, \vec{a},v}$ is separated and proper, and its coarse moduli space $M\uksba_{d, \vec{a}, v}$ is projective. Any family of smooth (or slc) stable pairs over a punctured disk extends (after finite base change) to a family over the disk with a unique stable pair as $\mcx_0$; any isomorphism over the $\mcx_t$ extends uniquely. Thus, $M\uksba_{d, \vec{a}, v}$ is a modular compactification of the moduli of smooth pairs.
:::


#### The KSBA Stack of $K$-Trivial Pairs

<!-- [AET19, Prop. 3.8] -->

Varieties with $K_X\sim 0$ numerically trivial, such as $K3$ and Enriques surfaces, are said to be **$K$-trivial**.
They require special treatment in the theory of KSBA stable pairs and compactifications because the stability condition (ampleness of $K_X + R$) can not hold when $R=0$.
So one must *always* choose a nontrivial divisor $R$ for such varieties, and the positivity must be entirely supplied by $R$ in order to achieve any kind of stability.
We are thus lead, as a first approximation, to consider pairs $(X, R)$.
However, the MMP and KSBA compactification require pairs $(X, D)$ where each component $D_i$ of $D$ appears with coefficient $a_i < 1$, noting that this must be a *strict* inequality.
This ensures that limits have only slc singularities and that stability is preserved in families, and avoids the complications that arise in the $a_i = 1$ case -- infinite stabilizers leading to Artin stacks instead of Deligne-Mumford stacks, more severe non-slc singularities in degenerations, a potential loss of separatedness, and so on.
Thus, in the $K$-trivial setting, one "perturbs" the canonical class by achieve the necessary positivity, by considering pairs $(X, \eps R)$ with a small rational coefficient $0 < \eps \ll 1$. For sufficiently small $\eps$, the sum $K_X + \eps R$ becomes ample and thus $(X, \eps R)$ is KSBA stable.
With this setup, the moduli of stable $K$-trivial pairs is realized as a special locus in the general KSBA moduli stack described above, and all the foundational results (properness, separatedness, projectivity, etc.) apply directly.

:::{.definition title="Stable $K$-Trivial Pair"}
Let $X$ be a projective, Gorenstein, connected, reduced variety with $K_X \cong \OO_X$ (that is, $K_X$ is trivial; for example, a $K3$ or Enriques surface). Fix a discrete invariant $e > 0$ (e.g., $e = R^2$ for surfaces), and let $0 < \eps \ll 1$ be a (sufficiently small) rational number.
A **stable $K$-trivial pair of type $(e, \eps)$** is a KSBA stable pair $(X, \eps R)$ such that:

- $R$ is an effective Cartier divisor on $X$ with $R^2 = e$,

- $(X, \eps R)$ is semi-log-canonical,

- $K_X + \eps R$ is ample,

- $\Aut(X, \eps R)$ is finite.

:::

:::{.definition title="Family and Moduli Functor for Stable $K$-Trivial Pairs" #ktriv-moduli-functor}
Let $e > 0$ and $0 < \eps \ll 1$.
A **family of stable $K$-trivial pairs** over a scheme $S$ is a flat, projective morphism
$f\colon (\mcx, \eps \mcr) \to S$
such that every geometric fiber $(\mcx_s, \eps\mcr_s)$ is a stable $K$-trivial pair of type $(e, \eps)$ as above.
The corresponding moduli functor $\mcm_e\uktriv(\eps)$ assigns to $S$ the set of isomorphism classes of such families over $S$.
:::

The moduli functor for stable $K$-trivial pairs $\mcm_e\uktriv(\eps)$ arises as a subfunctor of the previously discussed KSBA functor for stable pairs. Specifically, $\mcm_e\uktriv(\eps)$ parametrizes those families where each fiber $(X, \eps R)$ satisfies $K_X \cong \OO_X$, the $K$-trivial condition, and $R$ is an effective divisor of fixed primitive numerical class $e$ appearing in the boundary with weight $\eps \ll 1$.
This is a closed locus in the moduli stack $\mcm\uksba_{d, \vec{a}, v}$, where $d = \dim X$, the polarization type $e$ is fixed for the divisor $R$, the boundary coefficients $\vec{a}$ have $a_j = \eps$ at $R$ and zero otherwise, and $K_X$ is trivial as a line bundle or divisor.
The relevance of this construction is that the general results of KSBA theory—separatedness, properness, finite automorphism group property, and the existence of projective coarse moduli spaces—are inherited by this subfunctor. Thus:

- Every family of stable $K$-trivial pairs admits unique stable limits in one-parameter degenerations, guaranteeing the moduli stack is proper.
- The moduli stack is of finite type, separated, and Deligne–Mumford, with a projective coarse moduli space $M_e\uktriv(\eps)$.
- Extension and uniqueness of isomorphisms in families follow directly from the established machinery for stable pairs.

Thus by construction, the functor $\mcm_e\uktriv(\eps)$ ensures that the moduli problem for stable $K$-trivial pairs is embedded as a closed substack in the general KSBA stack, inheriting all of the necessary geometric properties. The existence of universal stable limits in families, the finiteness and separatedness of isomorphism classes, and the projectivity of the coarse moduli space are immediate consequences of this embedding.

:::{.lemma title="Independence from Small Boundary $\eps$" #ktriv-eps-independence}
Given $e>0$, there exists $\eps_0(e) > 0$ such that for all $0 < \eps \leq \eps_0$, the stacks and spaces
$$
\mcm_e\uktriv(\eps) \cong \mcm_e\uktriv(\eps_0),\qquad
M_e\uktriv(\eps) \cong M_e\uktriv(\eps_0)
$$
are canonically isomorphic; that is, passing to small boundary does not affect the structure of the moduli problem or its compactification.
:::

Thus $\mcm_e\uktriv(\eps)$ is a locus in a general KSBA moduli stack cut out by the condition $K_X \cong \OO_X$ and a the specification of a single boundary divisor $R$ of degree $e$ with small coefficient $\eps$.


#### Boundaries of KSBA compactifications

:::{.remark title="Combinatorial Organization of the Boundary" #boundary-organization-remark}
For moduli spaces such as $F_S$ of $S$-polarized K3 surfaces, and thus for spaces like $\fttz$ and $\fent$, the boundary of the KSBA compactification is stratified by SLC combinatorial type. Each stratum corresponds to a distinct type of geometric degeneration, classified via monodromy and combinatorial invariants which are encoded in dual complexes, fans, or semifans in related semitoroidal compactifications.
:::

:::{.definition title="Boundary Strata and Combinatorial Types" #boundary-stratum}
A **boundary stratum** in a KSBA compactification $\cpt{X}$ of $X$ is a locally closed subset parameterizing stable pairs $(X, R)$ that are not smoot, i.e., those lying in the boundary $\bd\cpt{X} \da \cpt{X} \setminus X$, where $X$ is the locus of smooth KSBA stable pairs.
The **slc combinatorial type** of a stable KSBA limit $(\cpt{X}, \eps \cpt{R})$ is the discrete data given by the simplicial complex $\Gamma(\cpt{X})$, along with the deformation type of the quasi-polarized minimal resolution $(V_i, D_i, L_i)$ of each irreducible component $\cpt{V}_i$ of $\cpt{X}$, where $L_i = \OO_{V_i}(R_i)$ is the line bundle associated to the pullback $R_i$ of the boundary divisor to the resolution.
An **slc stratum** is a boundary stratum of $\cpt{X}$ consisting of all stable pairs $(X, R)$ with the same slc combinatorial type.
:::


Given a nonzero vector $\lambda$ in a lattice $T$, its **projective class** is $[\lambda] \da \ts{ a\lambda \st a\in \RR_{>0}}$, i.e. the ray it generates in $T_\RR$.
Letting $T$ be the polarization lattice for a polarized moduli problem $\FG$ of K3 surfaces, we consider degenerations at a cusp $I$ in $\bd\bbcpt{\FG}$. 
The logarithmic mondromy $N$ at $I$ determines, up to the monodromy group and scaling, elements $\eta\in T$ and $\lambda\in \eta^{\perp T}$ by the explicit formula
$$
N(\gamma) = (\gamma \cdot \eta)\lambda - (\gamma \cdot \lambda)\eta, 
\,\,
\eta^2 = 0,\,\,
\lambda^2 = 
\begin{cases}
t > 0 & \text{if $I$ is a type $\III$ $0$-cusp  } \\
t = 0 & \text{if $I$ is a type $\II$ $1$-cusp }
\end{cases}
,$$
where $t$ is the number of triple points in $\mcx_0$ in the type $\III$ case.
Arcs in $\bbcpt{\FG}$ approaching a 0-cusp $\eta$ are asymptotic to translates of co-characters determined by the class of $\lambda \in \bdlattice{T}{\eta} = \eta^{\perp T}/\eta$, and thus $\lambda$ called the "monodromy invariant" of the degeneration.
We finally arrive at the key results that make our combinatorial analysis of $\fent$ possible:

:::{.theorem
   title="Dependence of boundary strata on monodromy invariants [@AE23, Cor. 8.13]"
   #boundary-monodromy-dependence}
Suppose $R$ is a recognizable divisor for $F_S$. Let $(\cpt{X}^*, \eps \cpt{R}^*) \to C^*$ be a family of stable pairs over a punctured curve with monodromy invariant $\lambda$. Then the slc combinatorial type of the unique KSBA stable limit $(\cpt{X}_0, \eps \cpt{R}_0)$ depends only on the projective class $[\lambda]$.
Thus there is a well-defined **stratum function**
$$
\SS\colon \{\text{monodromy invariants } \lambda\} \longrightarrow \{\text{slc boundary strata in } \cpt{X}\}
,$$
which assigns to each projective monodromy class the corresponding slc boundary stratum.
:::

:::{.proposition
   title="Normalization and Semitoroidal Strata [@AE23, Thm. 9.1, Cor. 9.2, Thm. 9.3]"
   #normalization-semitoroidal}

Let $F_S$ denote the moduli space of $S$-polarized K3 surfaces, and suppose $R$ is a recognizable divisor for $F_S$.
Then there exists a KSBA compactification $F_S^R$ by stable pairs associated to $R$, a unique semifan $\semifan{F}_R$ with a morphism
$$
\Psi_R\colon \semifancpt{F_S}{F_R} \to \cpt{F}_S^R
$$
from a semitoroidal compactification realizing it as the normalization of $\cpt{F}_S^R$.
For each cusp $I\in \bbcpt{F_S}$, writing $\bdlattice{T}{I}$ for the corresponding stable boundary lattice and $\thecone{C}_I$ for the corresponding positive cone, let

\begin{align*}
\thecone{C}_S^{\BB} \da \coprod_{I\in \bd\bbcpt{F_S} }\qty{ \thecone{C}_I \intersect \bdlattice{T}{I} }
.\end{align*}

and let $D$ be the polyhedral decomposition of $\thecone{C}_S^{\BB}$ induced by the level sets of $\SS$, i.e. whose tiles are the loci of all monodromy invariants $\lambda$ on which $\SS(\lambda)$ is constant.
Then the *maximal* cones of $D$ and $\semifan{F}_R$ are in bijection, and $\Psi_R$ sends each stratumm in $\bd \cpt{F}_S^{\semifan{F}_R}$ to the corresponding slc stratum of $\bd \cpt{F}_S^R$.
:::


#### Conclusion

The main takeaway of this section is that the boundary of the KSBA compactifications of moduli spaces such as $F_S$ of $S$-polarized K3 surfaces and related spaces like $\fttz$ and $\fent$ admit a precise, combinatorial description:

- The boundary $\cpt{F}_S^R$ is stratified according by slc combinatorial type, which encodes both the deformation type of the minimal resolution (with its corresponding divisor) of a stable pair $(X, R)$ and its simplicial dual complex,

- Each stratum corresponds to degenerations sharing the same monodromy data up to scaling, which is captured by the projective classes $[\lambda]$ of monodromy invariants in the stable boundary lattices $\bdlattice{T}{I}$ . There is thus a well-defined stratum function $\SS$ assigning to every monodromy class $\lambda$ the associated slc boundary stratum in $\cpt{F}_S$.

The stratification of $\cpt{F}_S^R$ is thus canonically organized by combinatorial data: dual complexes, semifans, and monodromy invariants. In geometric terms:

- There exists a semitoroidal compactification $\cpt{F}_S^{\semifan{F}_R}$ whose normalization maps onto the KSBA compactification $\cpt{F}_S^{R}$,

- Polyhedral decompositions and maximal cones of the semifan $\semifan{F}_R$ correspond bijectively to the maximal slc strata of the KSBA boundary, and

- The normalization morphism sends each combinatorial stratum of the semitoroidal model to the corresponding slc stratum on the KSBA side.

Thus the boundary of $\cpt{F}_S^R$ (and similar KSBA compactifications) is controlled by combinatorial invariants and is indexed purely in terms of discrete monodromy and combinatorial data.

The KSBA approach has a range of pros and cons. On the one hand, it yields a proper, separated, and projective moduli space and captures all stable degenerations (slc pairs). It is compatible with the MMP, and the corresponding coarse moduli space structure is always available. However, the approach is often abstract: explicit descriptions of the boundary and singularities are rare, and few algorithmic tools exist. The geometry of the boundary strata can be highly complicated, non-smoothable components and pathologies are generic in higher dimensions, and there is virtually no uniform combinatorial structure in those settings.

KSBA compactifications extend to surfaces of general type ($\kappa=2$), but for $\kappa = 0$ surfaces in full generality, i.e. K3, Enriques, abelian, and bielliptic surfaces, as well as for $\kappa=-\infty$ (ruled and rational surfaces), these require significant modification.
Moving to higher dimensions, compactifications for general $K$-trivial varieties like Calabi–Yau threefolds remains a major open problem. While the KSBA theory guarantees the existence of a good compact moduli space for varieties of log general type, the construction of projective and separated moduli spaces for $K$-trivial threefolds or Calabi–Yau varieties remains largely conjectural. The core technical obstacles here include the lack smoothability results, the failure of Torelli-type theorems, and much more complex limiting varieties which may be non-reduced or have infinite automorphism groups.
For varieties $X$ of general type with $\dim(X) \geq 3$, many results for surfaces generalize via the MMP -- however, explicit combinatorial classifications of the boundary are almost entirely missing.

Several parts of the KSBA theory have broad applicability. Universally valid points include the projectivity and properness of the moduli functor for slc varieties of (log) general type, yielding finite automorphism groups for stable pairs and thus a separated proper Deligne-Mumford stack.
However, in higher dimensions, these stacks are generally expected to be non-irreducible and highly singular, and even the deformation spaces of smooth objects can possess arbitrarily bad singularities -- a phenomenon encapsulated in Vakil’s "Murphy’s law." Unlike curves, where every stable limit is smoothable, smoothability fails in general: not every slc variety arises as a limit of smooth varieties. Combinatorial invariants such as dual complexes rapidly become complicated and lose the inductive or graph-like simplicity seen in the curve or surface cases as the dimension increases.
For K3 and Enriques surfaces, the boundary components of $\cpt{F}_S$ reflect geometric degenerations that align with period domain descriptions and semitoroidal constructions.

There is also an increasing interest in the relationship between $K$-stability and KSBA stability, particularly in the Fano and $K$-trivial settings. Heuristically, $K$-stability is a the link between GIT and KSBA stability -- for instance, any (GIT) $K$-semistable polarized variety has slc singularities, and any slc variety polarized by an ample canonical divisor is $K$-stable. Similarly, $K$-trivial, slc polarized pairs are $K$-semistable. In the Fano and Calabi-Yau cases, $K$-stability is necessary for establishing moduli that carry the expected differential-geometric invariants, namely, Kähler–Einstein metrics.
However, $K$-stability is not an open or constructible condition in general, and so explicit construction of moduli stacks via $K$-stability remains conjectural for many classes. Recent work by Xu, Li, Wang, and others have constructed projective moduli spaces for Fano varieties using the $K$-stability criterion.

Some key open directions for future research include:

- Extending the success of explicit boundary classifications, as seen in K3 and Enriques surfaces, to Calabi–Yau threefolds and higher-dimensional Fano varieties;

- Exploiting deeper connections with period maps and Hodge theory to construct and better understand compactification in higher dimensions;

- Clarifying the exact relationships between KSBA and $K$-stability, and developing effective, algorithmic, or combinatorial tools for KSBA (or related) compactifications beyond the few well-understood special cases.

