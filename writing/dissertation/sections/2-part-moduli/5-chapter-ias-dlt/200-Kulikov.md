### Kulikov Models


#### Degenerations

Let $\pi\colon \mcx \to C$ be a flat, proper morphism, with $C$ a germ of a smooth complex curve (typically taken as a disk $\Delta = \{ t \in \CC \colon |t| < \epsilon\}$). The **$\mcx_0$** $\mcx_0 = \pi^{-1}(0)$ encodes the limiting geometry of the family as $t \to 0$. For $t \neq 0$, the fibers $\mcx_t$ are assumed smooth, often K3 or Enriques surfaces. The **punctured disk** $\Delta^* = \Delta \setminus \{0\}$ and the corresponding smooth locus $\mcx^* = \pi^{-1}(\Delta^*)$ are natural analytic settings for studying the variation of Hodge structures in the family. 
Over $\Delta^*$, the fibers $\mcx_t$ are smooth and give rise to a variation of Hodge structure on the local system $R^2 \pi_* \ZZ$. The behavior of $\mcx_0$ reflects the limiting geometry and possible singularities, providing key topological and moduli-theoretic invariants that determine both the topological degeneration type and the locus in the compactified moduli space.

###### Dual Complexes

If $\mcx_0$ is a simple normal crossings (snc) divisor, its **dual complex** $\Gamma(\mcx_0)$ is the finite simplicial complex constructed as follows:

- vertices correspond to irreducible components of $\mcx_0$;
- $k$-simplices correspond to connected components of nonempty intersections of $k+1$ distinct components.

This combinatorial invariant is stable under blowups and birational modifications that preserve the snc property. For degenerations with semi log canonical (slc) singularities, $\Gamma(\mcx_0)$ is defined up to homeomorphism and remains a meaningful measure of combinatorial complexity of $\mcx_0$.
For degenerations of Enriques surfaces constructed as quotients by a biregular, fiberwise involution (the **Enriques involution**), the dual complex comes in one of two types:

- a topological closed disk $\DD^2$, when the quotient preserves orientation, or
- a real projective plane $\RP^2$, when antipodal identification occurs.

This distinction can be read off from the intersection pairing on the lattice $\bdlattice{T}{I}$ attached to the relevant cusp $I$ and the structure of $\mcx_0$.

#### Kulikov Models

A **Kulikov model** of a family of projective surfaces is a degeneration $\mcx \to C$ in which:

1. The total space $\mcx$ is regular, and thus smooth as a threefold;
2. The central fiber $\mcx_0$ is a reduced snc divisor;
3. The relative dualizing sheaf is trivial: $\omega_{\mcx/C} \cong \OO_{\mcx}$.

This Calabi–Yau condition ensures that $\mcx$ is a Calabi–Yau threefold over $C$ and provides precise control over the limiting MHS (see [@Kul77; @PP81]). The condition ensures that the limits of periods and Hodge structures are controlled, and $\mcx_0$ is as geometrically simple as feasible under semistable reduction.

The variation of Hodge structure on the local system $R^2 \pi_* \ul{\ZZ}$ equips the family with a locally constant sheaf whose fibers are $H^2(\mcx_t; \ZZ)$ for $t \neq 0$. The monodromy transformation about $t = 0$ is given by the Picard-Lefschetz operator
$T \colon H^2(\mcx_t; \ZZ) \to H^2(\mcx_t; \ZZ).$
After passing to a finite ramified cover of $\Delta$, one reduces to the case where $T$ is unipotent and defines the logarithm $N = \log T$ which is nilpotent of order at most three. The index of nilpotency of $N$ determines both the geometry of $\mcx_0$ and the combinatorial type of the degeneration.

**Type I.** If $N = 0$, then $\mcx_0$ is a smooth K3 surface. The degeneration is locally analytically trivial, and the dual complex is a single point.

**Type $\II$.** If $N \neq 0$ and $N^2 = 0$, then $\mcx_0 = V_1 \cup \cdots \cup V_n$, where:

- $V_1, V_n$ are rational surfaces;
- Each intermediate $V_i$ ($2 \leq i \leq n-1$) is birational to $E \times \PP^1$ for a fixed elliptic curve $E$;
- The double locus $D_{i,i+1} = V_i \cap V_{i+1}$ is isomorphic to $E$;
- The self-intersection numbers satisfy
  $$
  D_{i,i+1}|_{V_i}^2 + D_{i,i+1}|_{V_{i+1}}^2 = 0
  .$$
  The dual complex is a closed interval $\IAD^1$, i.e. a decomposition of the interval $[0, 1]$ into sub-segments.

**Type $\III$.** If $N^3 = 0$ with $N^2 \neq 0$, then $\mcx_0$ is a union of smooth rational surfaces, with irreducible components meeting along rational curves, such that:

- On each $V_i$ the sum of the double curves forms an anticanonical cycle:
  $$
  \sum_{j \neq i} D_{ij} \sim -K_{V_i},
  $$
- The intersection numbers satisfy
  $$
  d_{ij} + d_{ji} = -2, \qquad d_{ij} = -2p_a(D_{ij}) - (D_{ij})^2,
  $$
  where $p_a(D_{ij})$ is the arithmetic genus of $D_{ij}$.

The dual complex of $\mcx_0$ is a triangulation of the 2-sphere $\IAS^2$ [@FS86; @Fri83].
These types are naturally stratified by the rank of isotropic subspaces in the boundary lattice $\bdlattice{T}{I}$ and correspond to geometric monodromy vectors in the rational closure of $\thecone{C}_I$ in $\bdlattice{T}{I, \RR}$:

- Type $\I$ degenerations correspond to interior points of $\thecone{C}_I$;
- Type $\II$ degenerations arising from rank 1 isotropic sublattices $I$ correspond to rational boundary rays in $\thecone{C}_{I, \QQ}$ and thus to parabolic/$\tADE$ subdiagrams of the Vinberg-Coxeter diagram $G_I$ and yield integral-affine segments,
- Type $\III$ degenerations arising from rank 2 isotropic sublattices $I$ correspond to elliptic/$\ADE$ subdiagrams of $G_I$ and yield integral-affine spheres.

#### Picard-Lefschetz Theory

###### Picard–Lefschetz Transformations

:::{.definition title="Picard–Lefschetz Transformation" #def:picard-lefschetz-transformation}
Let $p\colon \mcx \to \Delta$ be a Kulikov model (or a semistable degeneration) with $\mcx_0$ $\mcx_0$. The sheaf $\RR^2 p_*\underline{\ZZ}_{\Delta}$ restricts to a locally constant system over the punctured disk $\Delta^*$, whose fiber over $t \in \Delta^*$ is $H^2(\mcx_t; \ZZ)$.
After trivializing the pullback of this local system to the universal cover $\widetilde{\Delta^*}$, the fundamental group $\pi_1(\Delta^*, t)$ acts via monodromy 
$\pi_1(\Delta^*, t) \longrightarrow \operatorname{Aut}(H^2(\mcx_t; \ZZ)).$
The image of a simple closed loop $\gamma$ generating $\pi_1(\Delta^*, t)$ is the **Picard–Lefschetz transformation**:
$$
T_\gamma \colon H^2(\mcx_t; \ZZ) \to H^2(\mcx_t; \ZZ)
,$$
represented by the **monodromy matrix** $T \in \GL_n(\ZZ)$ where $n = \Pic\ H^2(\mcx_t; \ZZ)$ [@Kul77], [@FS86].
:::

:::{.theorem title="Quasi-Unipotency and Log Monodromy" #thm:quasi-unipotent-monodromy}
If $\mcx_0$ is a simple normal crossings (semistable) degeneration, the monodromy $T$ is **quasi-unipotent**: that is, there exist positive integers $k, n$ such that $(T^k - \id)^n = 0$. For semistable degenerations, one can take $k = 1$. The logarithm of the unipotent part of $T$ defines the **log monodromy operator**:
$$
N = \log(T) = (T-\id) - {1\over 2}(T-\id)^2 + \frac{1}{3}(T-\id)^3 - \cdots + \frac{(-1)^{n+1}}{n}(T-\id)^n
,$$
where $n$ is the index of nilpotency [@Kul77], [@PP81].
:::

:::{.definition title="Monodromy Around Singularities" #def:monodromy-singularities}
Let $B$ be an integral affine manifold with singularities. The **monodromy** of $B$ around a singularity $p$ is the element of $\operatorname{Aff}(\ZZ^n)$ defined by parallel transport around a loop encircling $p$.
For an $I_1$ singularity in dimension $2$, the monodromy matrix is
$T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$
This affine monodromy encodes the classical Picard–Lefschetz transformation for such degenerations [@KS06], [@Sym03].
:::

:::{.remark 
  title="Monodromy Invariant as Structural Parameter" #rem:monodromy-invariant-parameter}
For a Type $\III$ Kulikov degeneration with $\mcx_0$ $\mcx_0$, the **monodromy invariant** $\lambda \in \bar{T}_\eta = \eta^\perp / \eta$ determines:

1. The number of triple points of $\mcx_0$, with $\lambda^2 = \#\{\text{triple points}\}$;

2. The *barycentric coordinates* $\lambda = (\ell_i)$,which  determine $B(\lambda)$, an explicit $\IAS^2$. 

For more details, see [@AEGS25; @GHK15; @Eng18].
:::

:::{.definition title="Weight Filtration on Cohomology" #def:weight-filtration-cohomology}
Let $N = \log(T)$ be the logarithm of the unipotent monodromy operator. The **weight filtration** $\incfiltration{W }$ on $H^2(\mcx_t; \CC)$ is defined by:
$$
W_k H^2 = \ts{ v \in H^2 \st N^{j} v = 0 \text{ for } j > k }
,$$
yielding a canonical increasing filtration
$$
0 = W_{-1} \subset W_0 \subset W_1 \subset W_2 \subset W_3 \subset W_4 = H^2(\mcx_t; \CC)
.$$
The **graded pieces** are $\Gr_k^W H^2 \da  W_k / W_{k-1}$, and carry the limiting mixed Hodge structure by @Del71.
:::

In the case of K3 surfaces, we can explicitly recover the filtration in terms of the order of nilpotency:

:::{.theorem title="Weight Filtration and Kulikov Type" #thm:weight-filtration-kulikov-types}
Let $N$ be the logarithm of the monodromy in a degeneration of K3 (or analogous) surfaces. Then:

- **Type I** (trivial monodromy, $N = 0$): $W_2 = H^2$, and all higher pieces vanish.
- **Type $\II$** ($N^2 = 0,\ N \neq 0$): $W_0 = \ker(N)$; $W_2 = H^2$; $W_4 = 0$.
- **Type $\III$** ($N^3 = 0,\ N^2 \neq 0$): all steps in the filtration are nontrivial.

The geometric interpretations are as follows:

- $\Gr_0^W$ encodes contributions from singular or reducible components;
- $\Gr_2^W$ corresponds to the part of the cohomology preserved in the degeneration;
- $\Gr_4^W$ arises from new cycles present in Type $\III$ degenerations.

This filtration packages the mixed Hodge structure obtained from the Clemens–Schmid exact sequence and classifies degenerations according to their limit behavior by @Kul77.
:::

Degenerations with unipotent monodromy give rise to *monodromy invariants*, which we now describe.

:::{.definition title="Monodromy Invariant and Barycentric Coordinates"}
Let $\lambda \in \bar{T}_\eta \da \eta^\perp / \eta$ denote the monodromy invariant associated to a degenerating family of K3 surfaces. Let $\{ \alpha_i \} \subset L$ be a set of simple roots defining a rational polyhedral chamber $\thecone{C} \subset L_{\RR}$, with wall hyperplanes $\alpha_i^\perp$.
We define the **barycentric coordinates** of $\lambda$ by:
$$
\ell_i \da  \lambda \cdot \alpha_i
.$$
The vector $\ell = (\ell_i)$ determines the affine geometry of the dual complex and the positions of singularities under the integral-affine structure.
:::

Let $\pi \colon \mcx \to C$ be a flat projective family of K3 surfaces over a smooth curve $C$, endowed with a biregular involution $\ien$ acting on $\mcx$ such that for every $t \ne 0$, the restriction $\ien |_{\mcx_t}$ is a fixed-point-free involution. Thus, for $t \ne 0$, the fibers $\mcx_t$ are K3 surfaces and the quotients $\mcx_t/\ien$ are nonsingular Enriques surfaces.
The specialization of $\ien$ to $\mcx_0$, denoted $\ienzero$, may acquire fixed points even if it acts freely on $\mcx_t$. This can result in additional singularities in $\mcx_0$, and consequently, in the quotient
$$
\mcz_0 \da  \mcx_0/\ienzero.
$$
Here, $\mcx_0$ denotes the central fiber of the degeneration, and $\mcz_0$ is its quotient by the specialized involution.
The dual complex $\Gamma(\mcz_0)$ of the central fiber $\mcz_0$ is topologically determined by the action of $\ienzero$ on the dual complex $\Gamma(\mcx_0)$ of the original Kulikov fiber. Specifically, if $\Gamma(\mcx_0)$ is a triangulated $2$-sphere, then if $\ienzero$ is free on $\Gamma(\mcx_0)$, the quotient dual complex $\Gamma(\mcz_0)$ is homeomorphic to the real projective plane $\RP^2$, as occurs when the involution acts antipodally on the sphere.
If $\ienzero$ has fixed points on $\Gamma(\mcx_0)$ or preserves a region, then the quotient dual complex $\Gamma(\mcz_0)$ is a disk $\DD^2$, corresponding to a boundary stratum where the involution admits fixed locus or acts with boundary preserves.

