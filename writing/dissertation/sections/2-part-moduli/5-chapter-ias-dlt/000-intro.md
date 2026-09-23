## Integral Affine Geometry and Comparing Compactifications {#sec:chapter-5}

Sources for this chapter include [@FS86; @Kul77; @PP81; @Sca87; @MM83; @Fri84; @FM83] Let $T$ be an even lattice of signature $(2, n)$, and let $\Gamma \subset \Orth(T)$ be an arithmetic subgroup.
The period domain $\halfpd{T}$ parametrizes weight-two Hodge structures on $T$, and the modular varieties $\FG = \dmodgamma{ \halfpd{T} }{ \Gamma }$ serve as coarse moduli spaces for (marked) polarized K3 surfaces.
Given a one-parameter degeneration of K3 or Enriques surfaces, a **Kulikov model** arises after a ramified base change, and the possible types for $\mcx_0$ are:

- **Type** $\I$: $\mcx_0$ is a smooth K3 surface.

- **Type $\II$**: $\mcx_0 = V_0 \cup \ldots \cup V_k$ is a chain of surfaces, where

  - $V_0$ and $V_k$ are rational and $V_1,\cdots, V_{k-1}$ are birational to $E\times \PP^1$ and thus elliptically ruled,

  - The chain consists of components $V_0,\ldots,V_k$ glued along elliptic curves $E_i = V_{i-1} \cap V_i$ $(1 \leq i \leq k)$, all isomorphic to the same elliptic curve $E$, satisfying a compatibility condition on normal bundles, $\mcn_{E/V_i} \otimes \mcn_{E/V_{i+1}} \cong \OO_E$

  - The dual complex $\Gamma(\mcx_0)$ is a simplicial$\DD^1$, corresponding to a partition of the closed unit interval $[0, 1]$.

- **Type $\III$**: $\mcx_0 = \bigcup_{i=0}^r V_i$ is a union of rational surfaces glued along rational curves such the dual intersection complex $\Gamma(\mcx_0)$ is a simplicial $S^2$.
  The union of the double curves on each component $V_i$ forms an anticanonical divisor – that is, a (possibly reducible) cycle of smooth rational curves in $|-K_{V_i}|$

The dual intersection complex $\Delta$ of a Type $\III$ model is a triangulation of $S^2$ admitting the structure of a 2-dimensional **integral affine sphere with singularities** ($\IAS^2$) which correspond to a distinguished subset of vertices in $\Delta$, after passing to a suitably complete triangulation.
Away from this singular locus, the charts are locally modeled on open subsets of $\RR^2$ with transition functions in the orientation-preserving affine linear group $\SL_2(\ZZ) \ltimes \RR^2$.
The possible singularities are modeled on the local structure of the quotient of $\RR^2$ by the shearing matrices $\begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$ for some integer $n \geq 0$; these are called $I_n$ singularities, where $\I_1$ are generic and $I_0$ is the trivial (toric) case.
More general singularities arise as products of such shears, corresponding to collisions of the corresponding $\I_n$ singularities, see [@AE22; @Sym03]

By taking the star to obtain a fan, each vertex $v$ in $\Delta$ yields an **anticanonical pair** $(V, D)$, where $V$ is a rational surface and $D = \sum_{j} D_j \in |-K_V|$ is a cycle of rational curves in the anticanonical linear system.
The dual polytope of this fan encodes a *semitoric* variety: varieties which arise from toric varieties via sequences of blowups and blowdowns.
The data of these blowups is encoded in the following way: the **charge** at a vertex $v$, for the anticanonical pair $(V, D)$, is defined by $Q(V, D) \da  {1\over 2}\sum_j D_j^2 + 3$, where $D = \sum_j D_j$ is the (possibly reducible) anticanonical cycle, and $D_j^2$ is the self-intersection of component $D_j$ in $V$.
The charge  is precisely designed to measures the defect from being toric: $Q(V, D) = 0$ precisely when $(V, D)$ is toric.
More fundamentally, [@FS86, Prop. 2.11] asserts that $\sum_{v \in \Delta} Q(V_v, D_v) = 24$ for any Type $\III$ Kulikov model of a K3 surface, see [@FM83; @FS86].

**Symington surgeries** are local modifications of $\IAS^2$ structures that manipulate the placement and type of singularities, and there are two main types: performing a *toric blowup* corresponds to the standard blowup in toric geometry attained by inserting rays into a fan or deleting triangles from its dual polytope.
It increases the number of vertices in $\Delta$, but preserves the total charge.
A *non-toric* (interior) blowup is a surgery that increases the charge at an interior vertex and modifies the integral-affine structure locally by adding the data of a distinguished *monodromy ray*, where the transition functions across the ray are generically described by monodromy matrices as described above.
A toric blowup is thus a blowup at a node of the cycle, corresponding to a torus-invariant point in a toric model, while a nontoric/interior blowup is a blowup at a smooth point of the surface, either on or off the anticanonical cycle.
Such moves are necessary to build arbitrary $\IAS^2$ with prescribed collections of $I_n$ singularities and total charge 24 from a standard simplicial sphere.

Symington’s theory explicitly produces $\IAS^2$ by sequences of such surgeries, along with *cuts* and *nodal slides*. Thus, the charge, and the combinatorial data of surgeries, encode all allowable dual complexes for Type $\III$ degenerations.
Arbitrary $\IAS^2$s with prescribed ($I_{n_1},\ldots,I_{n_k}$) of total charge 24 are built by sequences of toric and nontoric starting from a convex polygon.
This defines the base of a Lagrangian torus fibration, and we refer to the total space as a *semitoric variety* – a variety that is birationally equivalent to a toric variety, differing by only finitely many nontoric blowups.
Whenever the data $(B(\lambda), Q )$ arise from such construction, there exists a corresponding Kulikov model $\mcx_0$ with $\Gamma(\mcx_0) = B(\lambda)$.

Any such $\IAS^2$ satisfying a $d$-semistability condition $\mathsf{Ext}^1_{\OO_{\mcx_0 }}(\Omega_{\mcx_0}, \OO_{\mcx_0} ) \cong \OO_{\mcx_0^{\sing } }$ admits a smoothing $\mcx \to \Delta$ to a (possibly singular) K3 surface.
The $d$-semistability condition is necessary and sufficient for (local) smoothability; for global smoothings to K3 surfaces, the central fiber must also satisfy the additional conditions of being a Kulikov model.
@GHK15, for example, relate this to the existence of Lagrangian torus fibrations on the nearby fibers, mirroring the affine geometry of $B(\lambda)$.

Every Type $\III$ Kulikov degeneration carries a *projective monodromy invariant* $[\lambda]$ in (projectivized) boundary lattice $\PP( \bdlattice{T}{\eta}) =\PP( \eta^{\perp}/\eta)$.
This invariant records the monodromy around $\mcx_0$ and, crucially, determines the gluing data for reconstructing the degeneration from the $\IAS^2$ and its singularities.
A Eichler transvection relates $[\lambda]$, the vanishing cycle.
The local system $H^2$ carries a monodromy operator$T$, computed via a primitive isotropic vector $\delta$, the *vanishing cycle*, and the monodromy invariant $\lambda$:
$$
T(x) = x + (x, \delta) \lambda - (\lambda, x) \delta, \qquad x\in H^2(\mcx_t; \ZZ)
$$
where $\lambda^2$ counts the number of triple points (see [@PP81; @Sca87]).

Recall that a divisor $R$ is **recognizable** [@AE23a; @AEH24] for $\FG$ if, for any K3 surface $X = \mcx_0$ and any smooth $\mcx$ to a Kulikov model, the flat limit $R_0$ on $\mcx_0$ is uniquely determined up  to automorphism.
Given a recognizable divisor $R$, the KSBA compactification $\cpt{F}_\Gamma^R$ can be formed, as well as a the corresponding normalizing semitoroidal compactification $\semifancpt{\FG}{\semifan{F}_R}$.
By way of the strata functions $\SS(\lambda)$ from [Chapter 4](#sec:chapter-4) for decorated intersection complexes $B(\lambda)$ constructed from monodromy invariants $\lambda$, boundary strata on both sides correspond to possible $\IAS^2$ with singularities.

Mirror symmetry supplies a *Lagrangian torus fibration* over $B(\lambda)$, and the intersection complex $\Gamma(\mcx_0)$ of a Kulikov model coincides with the $\IAS^2$ $B(\lambda)$ constructed from the monodromy data.
The smoothability of the singularities then produces a family $\mcx \to \Delta$, whose general fiber is smooth, and an explicit contraction algorithm (mirroring the MMP) yields the KSBA stable model.
For K3 surfaces with a nonsymplectic involution, the construction of $\IAS^2$s is mirrored by gluing a polygon $P$ to its *opposite* $P^{\opop}$, forming an $\IAS^2$, $B(\lambda)$, with an induced involution.

Given a degeneration at a 0-cusp $\eta$, the cusp is classified by the boundary lattice $\bdlattice{T}{\eta}$ and the group$\Gamma_\eta$.
The associated Coxeter polytope $P(\Gamma_\eta)$ specifies a Coxeter-Vinberg diagram $G(\Gamma_\eta)$.
To build the intersection complex $\Gamma(\mcx_0)$(for a degeneration with monodromy invariant$[\lambda]$),

- Compute $[\lambda] \in \thecone{C}_\eta$,

- Write barycentric coordinates $\ell_i = (\lambda,\alpha_i)$,

- Form the convex (planar) polygon $B_1(\lambda) = \ConvOp {v_i} \subset \RR^2$ where $v_i$ are specified by the Coxeter diagram and$\ell_i$ govern their lengths,

- Obtain the full $\IAS^2$ by gluing $B_1(\lambda)$ to its opposite:$B(\lambda) = B_1(\lambda) \cup -B_1(\lambda)$, yielding an $\IAS^2$.

We summarize this process in the following algorithm to construct Type $\III$ degenerations for $\FG$, which we in turn specialize to $\fttz$ and $\fent$ to construct dlt models for KSBA stable limits:

1. **Build the Coxeter polygon $P(\Gamma_\eta)$** from the Coxeter–Vinberg diagram, using the configuration of simple roots $\alpha_i$.

2. **Compute barycentric coordinates** $\ell_i = (\lambda, \alpha_i)$ from the monodromy invariant $[\lambda]$.

3. **Construct the monodromy polytope** $B_1(\lambda)$ in $\RR^2$ using vertices $v_i$ and these lengths.

4. **Form the $\IAS^2$** $B(\lambda) = B_1(\lambda) \cup -B_1(\lambda)$, with $I_n$ singularities at prescribed locations, with total charge 24.

5. **Produce the corresponding Kulikov model** $\mcx_0$ where $\Gamma(\mcx_0)$ matches $B(\lambda)$, and smooth $\mcx_0$ to a family $\mcx\to\Delta$.

6. **Contract** $\mcx$ to the KSBA stable model $\bar\mcx$.

For Enriques surfaces, the above theory must be quotiented by a fixed-point-free involution on $\IAS^2$, reflecting the covering $K3$ surface structure.
This mandates working with "half-divisor" models ([definition](#hdm-halfdivisor)) and searching for $\IAS^2$s invariant under a group generated by two commuting involutions, one corresponding to $\idp$, corresponding to K3 surfaces $X$ in $\fttz$, and another fixed-point-free involution corresponding to $\ien$, coming from the embedded locus $\fent$, those $X$ arising as K3 covers $X\to Z$ of Enriques surfaces.
We impose the condition that the periods and dual complex of $(X_0, R_0)$ are involution invariant – then the Torelli theorem for anticanonical pairs shows that $(V_i, D_i, R_i)$ admits an involution $\iota_{\En, i}$ and the quotient $(V_i, D_i, R_i)/\iota_{\En,i}$ is a log Calabi–Yau pair.
We note that $\ien$ is only a birational involution in general, and so we obtain half-divisor models for generic degenerations with a given monodromy invariant $\lambda$.

<!--  [@Ale02], [@MZ08], [@AMRT10] -->
