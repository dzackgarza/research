### Kulikov Models

#### Degenerations

Let $\pi\colon \mcx \to C$ be a flat, proper morphism, with $C$ a germ of a smooth complex curve (typically taken as a disk $\Delta = \{ t \in \CC \colon |t| < \epsilon\}$). The **$\mcx_0$** $\mcx_0 = \pi^{-1}(0)$ encodes the limiting geometry of the family as $t \to 0$.
For $t \neq 0$, the fibers $\mcx_t$ are assumed smooth, often K3 or Enriques surfaces.
The **punctured disk** $\Delta^* = \Delta \setminus \{0\}$ and the corresponding smooth locus $\mcx^* = \pi^{-1}(\Delta^*)$ are natural analytic settings for studying the variation of Hodge structures in the family.
Over $\Delta^*$, the fibers $\mcx_t$ are smooth and give rise to a variation of Hodge structure on the local system $R^2 \pi_* \ZZ$.
The behavior of $\mcx_0$ reflects the limiting geometry and possible singularities, providing key topological and moduli-theoretic invariants that determine both the topological degeneration type and the locus in the compactified moduli space.

##### Dual Complexes

If $\mcx_0$ is a simple normal crossings (snc) divisor, its **dual complex** $\Gamma(\mcx_0)$ is the finite simplicial complex constructed as follows:

- vertices correspond to irreducible components of $\mcx_0$;

- $k$-simplices correspond to connected components of nonempty intersections of $k+1$ distinct components.

This combinatorial invariant is stable under blowups and birational modifications that preserve the snc property.
For degenerations with semi log canonical (slc) singularities, $\Gamma(\mcx_0)$ is defined up to homeomorphism and remains a meaningful measure of combinatorial complexity of $\mcx_0$.
For degenerations of Enriques surfaces constructed as quotients by a biregular, fiberwise involution (the **Enriques involution**), the dual complex comes in one of two types:

- a topological closed disk $\DD^2$, when the quotient preserves orientation, or

- a real projective plane $\RP^2$, when antipodal identification occurs.

This distinction can be read off from the intersection pairing on the lattice $\bdlattice{T}{I}$ attached to the relevant cusp $I$ and the structure of $\mcx_0$.

#### Kulikov model definition and types

A **Kulikov model** of a family of projective surfaces is a degeneration $\mcx \to C$ in which:

1. The total space $\mcx$ is regular, and thus smooth as a threefold;

2. The central fiber $\mcx_0$ is a reduced snc divisor;

3. The relative dualizing sheaf is trivial: $\omega_{\mcx/C} \cong \OO_{\mcx}$.

This Calabi–Yau condition ensures that $\mcx$ is a Calabi–Yau threefold over $C$ and provides precise control over the limiting MHS (see [@Kul77; @PP81]). The condition ensures that the limits of periods and Hodge structures are controlled, and $\mcx_0$ is as geometrically simple as feasible under semistable reduction.

The variation of Hodge structure on the local system $R^2 \pi_* \underline{\ZZ}$ equips the family with a locally constant sheaf whose fibers are $H^2(\mcx_t; \ZZ)$ for $t \neq 0$.
The monodromy transformation about $t = 0$ is given by the Picard-Lefschetz operator $T \colon H^2(\mcx_t; \ZZ) \to H^2(\mcx_t; \ZZ).$ After passing to a finite ramified cover of $\Delta$, one reduces to the case where $T$ is unipotent and defines the logarithm $N = \log T$ which is nilpotent of order at most three.
The index of nilpotency of $N$ determines both the geometry of $\mcx_0$ and the combinatorial type of the degeneration.

##### Type I
If $N = 0$, then $\mcx_0$ is a smooth K3 surface.
The degeneration is locally analytically trivial, and the dual complex is a single point.

##### Type $\II$
If $N \neq 0$ and $N^2 = 0$, then $\mcx_0 = V_1 \cup \cdots \cup V_n$, where:

- $V_1, V_n$ are rational surfaces;

- Each intermediate $V_i$ ($2 \leq i \leq n-1$) is birational to $E \times \PP^1$ for a fixed elliptic curve $E$;

- The double locus $D_{i,i+1} = V_i \cap V_{i+1}$ is isomorphic to $E$;

- The self-intersection numbers satisfy
  $$
  D_{i,i+1}|_{V_i}^2 + D_{i,i+1}|_{V_{i+1}}^2 = 0
  .$$
  The dual complex is a closed interval $\IAD^1$, i.e. a decomposition of the interval $[0, 1]$ into sub-segments.

##### Type $\III$
If $N^3 = 0$ with $N^2 \neq 0$, then $\mcx_0$ is a union of smooth rational surfaces, with irreducible components meeting along rational curves, such that:

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

##### Picard–Lefschetz Transformations

::: {.definition title="Picard–Lefschetz Transformation" #def:picard-lefschetz-transformation}
Let $p\colon \mcx \to \Delta$ be a Kulikov model (or a semistable degeneration) with $\mcx_0$ $\mcx_0$.
The sheaf $\RR^2 p_*\underline{\ZZ}_{\Delta}$ restricts to a locally constant system over the punctured disk $\Delta^*$, whose fiber over $t \in \Delta^*$ is $H^2(\mcx_t; \ZZ)$.
After trivializing the pullback of this local system to the universal cover $\widetilde{\Delta^*}$, the fundamental group $\pi_1(\Delta^*, t)$ acts via monodromy $\pi_1(\Delta^*, t) \longrightarrow \operatorname{Aut}(H^2(\mcx_t; \ZZ)).$ The image of a simple closed loop $\gamma$ generating $\pi_1(\Delta^*, t)$ is the **Picard–Lefschetz transformation**:
$$
T_\gamma \colon H^2(\mcx_t; \ZZ) \to H^2(\mcx_t; \ZZ)
,$$
represented by the **monodromy matrix** $T \in \GL_n(\ZZ)$ where $n = \Pic\ H^2(\mcx_t; \ZZ)$ [@Kul77], [@FS86].
:::

::: {.theorem title="Quasi-Unipotency and Log Monodromy" #thm:quasi-unipotent-monodromy}
If $\mcx_0$ is a simple normal crossings (semistable) degeneration, the monodromy $T$ is **quasi-unipotent**: that is, there exist positive integers $k, n$ such that $(T^k - \id)^n = 0$.
For semistable degenerations, one can take $k = 1$.
The logarithm of the unipotent part of $T$ defines the **log monodromy operator**:
$$
N = \log(T) = (T-\id) - {1\over 2}(T-\id)^2 + \frac{1}{3}(T-\id)^3 - \cdots + \frac{(-1)^{n+1}}{n}(T-\id)^n
,$$
where $n$ is the index of nilpotency [@Kul77], [@PP81].
:::

::: {.proof}

This is the monodromy theorem in the semistable case [@Kul77; @PP81]: the local monodromy of a semistable family is unipotent, so $k = 1$ may be taken, and then $N = \log T$ is the displayed finite sum because $T-\id$ is nilpotent of index $n$.
:::

::: {.definition title="Monodromy Around Singularities" #def:monodromy-singularities}
Let $B$ be an integral affine manifold with singularities.
The **monodromy** of $B$ around a singularity $p$ is the element of $\operatorname{Aff}(\ZZ^n)$ defined by parallel transport around a loop encircling $p$.
For an $I_1$ singularity in dimension $2$, the monodromy matrix is $T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$ This affine monodromy encodes the classical Picard–Lefschetz transformation for such degenerations [@KS06], [@Sym03].
:::

::: {.remark 
  title="Monodromy Invariant as Structural Parameter" #rem:monodromy-invariant-parameter}
For a Type $\III$ Kulikov degeneration with $\mcx_0$ $\mcx_0$, the **monodromy invariant** $\lambda \in \bar{T}_\eta = \eta^\perp / \eta$ determines:

1. The number of triple points of $\mcx_0$, with $\lambda^2 = \#\{\text{triple points}\}$;

2. The *barycentric coordinates* $\lambda = (\ell_i)$,which determine $B(\lambda)$, an explicit $\IAS^2$.

For more details, see [@AEGS25; @GHK15; @Eng18].
:::

::: {.definition title="Weight Filtration on Cohomology" #def:weight-filtration-cohomology}
Let \(V=H^2(\mcx_t;\QQ)\) and let \(N=\log T\) be the nilpotent logarithm of the unipotent monodromy. The **monodromy weight filtration centred at weight \(2\)** is the unique increasing filtration
$$
0=W_{-1}\subseteq W_0\subseteq W_1\subseteq W_2\subseteq W_3\subseteq W_4=V
$$
satisfying
$$
N(W_k)\subseteq W_{k-2},
\qquad
N^\ell:\Gr^W_{2+\ell}V\iso\Gr^W_{2-\ell}V\quad(\ell=0,1,2),
$$
where \(W_k=0\) for \(k<0\), and \(\Gr_k^WV=W_k/W_{k-1}\) [@Sch73, Lemma 6.4, printed p. 247]. Extend \(W\) to \(H^2(\mcx_t;\CC)\) by scalar extension. This is the weight filtration of the limiting mixed Hodge structure. In particular, it is **not** given by the sequence of kernels of powers of \(N\): that sequence has a different indexing and in general different steps.
:::

In the case of Kulikov degenerations of K3 surfaces, the filtration is as follows.

::: {.theorem title="Weight Filtration and Kulikov Type" #thm:weight-filtration-kulikov-types}
Put \(V=H^2(\mcx_t;\QQ)\), with \(N=\log T\).

1. **Type I** (\(N=0\)): \(W_0=W_1=0\), \(W_2=W_3=W_4=V\). Only \(\Gr^W_2\) is nonzero.
2. **Type \(\II\)** (\(N\neq0,\ N^2=0\)): \(W_0=0\), \(W_1=\im N\), \(W_2=\ker N\), \(W_3=W_4=V\). The nonzero graded pieces are \(\Gr^W_1,\Gr^W_2,\Gr^W_3\).
3. **Type \(\III\)** (\(N^2\neq0,\ N^3=0\)): \(W_0=W_1=\im N^2\), \(W_2=W_3=\ker N^2\), \(W_4=V\). The only nonzero graded pieces are \(\Gr^W_0,\Gr^W_2,\Gr^W_4\), of dimensions \(1,20,1\).

The Type \(\III\) assertion uses the special monodromy form of a **K3 Kulikov degeneration**; the condition \(N^3=0\) alone, for an arbitrary nilpotent endomorphism, does not exclude Jordan blocks of size two and does not imply vanishing of \(\Gr^W_1,\Gr^W_3\). The Type \(\II\) middle graded piece \(\ker N/\im N\) is the weight-two boundary lattice space \(I^\perp/I\) appearing in @prop:weight-filtration-by-type and the discussion of the Type \(\II\) cusp in @sec-kulikov-models.
:::

::: {.proof}
Schmid's uniqueness criterion [@Sch73, Lemma 6.4, printed p. 247] is the definition above. In Type I, it forces all of \(V\) to have weight \(2\).

In Type \(\II\), \(N^2=0\) implies \(\im N\subseteq\ker N\). With the displayed filtration, \(N(W_k)\subseteq W_{k-2}\), and
$$
N: \Gr^W_3=V/\ker N\;\iso\;\im N=\Gr^W_1
$$
by the first isomorphism theorem; all the other required \(N^\ell\) isomorphisms are either the identity for \(\ell=0\) or between zero spaces. This proves the claimed filtration without treating \(\ker N\) as \(W_0\).

For a Type \(\III\) K3 Kulikov degeneration, the monodromy formula of @prop:type-iii-monodromy-triple-points (from [@FS86, Lemma 1.1 and Proposition 7.1]) gives
$$
Nx=(x\cdot\delta)\lambda-(x\cdot\lambda)\delta,\quad
\delta^2=\delta\cdot\lambda=0,\quad
N^2x=-\lambda^2(x\cdot\delta)\delta,
$$
with \(\lambda^2\neq0\). Thus \(\im N^2=\QQ\delta\), \(\ker N^2=\delta^\perp\), and \(N(\delta^\perp)\subseteq\QQ\delta\). The displayed filtration satisfies Schmid's conditions: \(\Gr^W_1=\Gr^W_3=0\), and \(N^2:V/\ker N^2\iso\im N^2\). The dimensions follow from \(\dim V=22\) and \(\rank N^2=1\).
:::

Degenerations with unipotent monodromy give rise to *monodromy invariants*, which we now describe.

::: {.definition title="Monodromy Invariant and Barycentric Coordinates"}
Let $\lambda \in \bar{T}_\eta \definedas \eta^\perp / \eta$ denote the monodromy invariant associated to a degenerating family of K3 surfaces.
Let $\{ \alpha_i \} \subset L$ be a set of simple roots defining a rational polyhedral chamber $\thecone{C} \subset L_{\RR}$, with wall hyperplanes $\alpha_i^\perp$.
We define the **barycentric coordinates** of $\lambda$ by:
$$
\ell_i \definedas  \lambda \cdot \alpha_i
.$$
The vector $\ell = (\ell_i)$ determines the affine geometry of the dual complex and the positions of singularities under the integral-affine structure.
:::

Let $\pi \colon \mcx \to C$ be a flat projective family of K3 surfaces over a smooth curve $C$, endowed with a biregular involution $\ien$ acting on $\mcx$ such that for every $t \ne 0$, the restriction $\ien |_{\mcx_t}$ is a fixed-point-free involution.
Thus, for $t \ne 0$, the fibers $\mcx_t$ are K3 surfaces and the quotients $\mcx_t/\ien$ are nonsingular Enriques surfaces.
The specialization of $\ien$ to $\mcx_0$, denoted $\ienzero$, may acquire fixed points even if it acts freely on $\mcx_t$.
This can result in additional singularities in $\mcx_0$, and consequently, in the quotient
$$
\mcz_0 \definedas  \mcx_0/\ienzero.
$$
Here, $\mcx_0$ denotes the central fiber of the degeneration, and $\mcz_0$ is its quotient by the specialized involution.
The dual complex $\Gamma(\mcz_0)$ of the central fiber $\mcz_0$ is topologically determined by the action of $\ienzero$ on the dual complex $\Gamma(\mcx_0)$ of the original Kulikov fiber.
Specifically, if $\Gamma(\mcx_0)$ is a triangulated $2$-sphere, then if $\ienzero$ is free on $\Gamma(\mcx_0)$, the quotient dual complex $\Gamma(\mcz_0)$ is homeomorphic to the real projective plane $\RP^2$, as occurs when the involution acts antipodally on the sphere.
If $\ienzero$ has fixed points on $\Gamma(\mcx_0)$ or preserves a region, then the quotient dual complex $\Gamma(\mcz_0)$ is a disk $\DD^2$, corresponding to a boundary stratum where the involution admits fixed locus or acts with boundary preserves.
