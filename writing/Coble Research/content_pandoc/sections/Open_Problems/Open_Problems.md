# Open problems and technical gaps

::: {.remark title="Orientation"}

This section records the known open problems and computational obstacles of the Coble moduli program.
Each entry is a genuine gap between the results established elsewhere in this document and the fully rigorous, coordinate-explicit statements one would want for parity with the Enriques degree-$2$ program of [@AEGS25]. The problems are grouped by theme: lattice-theoretic verifications, the enumeration of isotropic orbits and cusps together with the reflection-group combinatorics, the *dlt* and KSBA stable models, and the foundational equations and computational checks.
None of the statements below is claimed to be settled; several cross-reference partial results already in the text, and in each case the *residue* that remains open is stated explicitly.
:::

## Lattice-theoretic gaps

::: {.remark title="Open problem: isometry class and genus of the Coble lattices"}

The invariants $(r,a,\delta)$ of the geometric lattice $S_\Co \cong (11,11,1)_1$ (signature $(1,10)$, Gram matrix $\operatorname{diag}(2,-2,\dots,-2)$, equivalently $\gens{-2}\oplus E_{10}(2)$) and of the transcendental lattice $T_\Co = S_\Co^{\perp \lkt} \cong (11,11,1)_2$ (signature $(2,9)$) are recorded in the Coble lattice table (\cref{tbl:coble-lattices}), and both satisfy $q_{S_\Co} \cong q_{T_\Co} \cong (\ZZ/2\ZZ)^{11}$ with $q_{S_\Co} = -q_{T_\Co} \bmod 2\ZZ$.
What is not yet formally established is the *isometry-class verification* and the *genus decomposition*: whether the genus of $T_\Co$ contains a unique isometry class.
Concretely:

- compute the Gram matrices of $S_\Co$ and $T_\Co$ and verify their $(r,a,\delta)$ invariants and genus cardinality via Nikulin's classification (the $r > a$ check for a $2$-elementary lattice) [@Nik80];

- confirm that $r > a$ forces a unique class in the genus, so that the reduction of isotropic-orbit questions to the discriminant form $q_{T_\Co}$ (\cref{thm:sterk-orbit}) is justified.
:::

::: {.remark title="Open problem: explicit primitive embedding matrices"}

The chain of primitive embeddings
$$
T_\Co \injects T_\En \injects T_\dP \injects \lkt
$$
is used throughout (\cref{lem:sequence_of_embeddings}, \cref{lem:primitive_embedding_eta}), and Nikulin's apparatus [@Nik80 Prop. 1.14.4, 1.15.2] is the intended tool for the uniqueness of the primitive embedding $T_\Co \injects T_\En$ and for the surjectivity of $\Orth(L) \to \Orth(T_\Co)$.
What remains is to *exhibit the embedding matrices in coordinate bases*: derive the explicit primitive-embedding matrices realizing the chain above, and verify their primitivity directly rather than by invocation.
The same coordinate deficit affects the derivation of the explicit equations for $C$ and $X$ (below): the invariants are listed, but the primitivity of the lattice embeddings lacks a rigorous derivation in terms of coordinate bases.
:::

::: {.conjecture title="Open problem: the horizontal folding involution and its eigenspaces"}

There is an orthogonal involution $\theta$ on the K3 lattice $\lkt \cong U^{3}\oplus E_8^{2}$ whose invariant and coinvariant sublattices are
$$
\lkt^{\theta} \cong T_\Co,
\qquad
\lkt^{-\theta} \cong S_\Co,
$$
and whose action on roots induces the *horizontal folding* of the $(18,0,0)_1$ Coxeter diagram, as a functorial consequence of the lattice isometry (cf.
\cref{def:folded-root}, \cref{lem:root-folding-tdp}, and the invariant/coinvariant construction of \cref{def:invariant_coinvariant_lattices}). The involution should swap the polarization generators between sectors, $h_\En \leftrightarrow h_\Co$.
The open technical content is to *write down the $22\times 22$ matrix of $\theta$ on the standard basis of $U^{3}\oplus E_8^{2}$* and to verify the isometry classes of its $\pm 1$ eigenspaces by the $(r,a,\delta)$ comparison of \cref{prop:involution_eigenspaces}, confirming $\lkt^{+}\cong T_\Co$, $\lkt^{-}\cong S_\Co$ ($2$-elementary check), and that the induced embedding $T_\Co \injects T_\En$ is primitive.
:::

## Isotropic orbits, cusps, and reflection groups

::: {.question title="Open problem: enumeration of isotropic orbits by Sterk's technique"}

How many orbits of primitive isotropic vectors does $T_\Co$ have under $\Orth(T_\Co)$, $\Orth^{*}(T_\Co)$, and the arithmetic group $\Gamma_\Co$?
Sterk's technique [@Ste91] determines these by analyzing the orbits of the images (lifts) in the discriminant group $A_{T_\Co} \cong (\ZZ/2\ZZ)^{11}$ under $\Orth(q_{T_\Co})$: for a $2$-elementary lattice with $r > a$ the genus contains a unique class and $\Orth(T) \to \Orth(q_T)$ is surjective [@Nik80], so a primitive isotropic vector $v$ with $\operatorname{div}(v)=d$ is determined up to $\Orth(T)$ by the tuple $(\operatorname{div}(v),\, \bar v \in A_T,\, v^2 = 0)$.
The number of such orbits in $A_{T_\Co}$ is not yet computed.
The open work is to:

- enumerate the isotropic vectors of $A_{T_\Co}$ and compute their orbits under $\Orth(q_{T_\Co})$;

- lift these orbits to $T_\Co$ using Sterk's lifting theorems and verify that exactly one $\Orth^{*}(T)$-orbit exists in divisibility $2$;

- verify that the $\Orth(T)$-orbits coincide with the $\Gamma_\Co$-orbits, so that the Baily--Borel $0$-cusp is unique.

That every primitive isotropic $v \in T_\Co$ has $\operatorname{div}_{T_\Co}(v) = 2$ is already known (\cref{lem:divisibilityAlwaysTwoTco}), which fixes the divisibility datum but not the orbit count.
:::

::: {.remark title="Open problem: explicit generators of $\Gamma_\Co$ and uniqueness of the 1-cusp"}

The arithmetic group governing the Coble locus is the stabilizer of the polarization $h_\Co$ inside $\Orth(T_\En)$, cut further by the horizontal folding involution $\theta$,
$$
\Gamma_\Co = \operatorname{Stab}_{\Orth(T_\En)}(h_\Co) \cap Z_{\Orth(T_\En)}(\theta),
$$
where in the Enriques sector $h_\En = e + f$ is the degree-$2$ polarization ($h^2 = 2$) and $h_\Co$ is induced by the hyperplane class $E_0$.
An explicit representation of $\Gamma_\Co$ by *matrix generators* is presently a stub.
The open work is to:

- compute the stabilizer/centralizer intersection in the Enriques (equivalently $\lkt$) lattice to produce a minimal set of matrix generators for $\Gamma_\Co$, as the intersection of the reflection group $W(T)$ with the centralizer $Z(\theta)$ and the stabilizer of the primitive vector $h_\Co$ ($h_\Co^2 = 2$);

- verify the *uniqueness of the $1$-cusp* by enumerating all $\Orth(T_\Co)$-orbits of primitive isotropic planes $J \subset T_\Co$, computing the negative-definite quotient $J^{\perp}/J$ for each, and confirming isometry with $A_1^{\oplus 7}$.

This refines, at the level of orbits and generators, the $1$-cusp correspondence $(7,7,1)_0 \mapsto (8,6,0)_0$ established in \cref{lem:1_cusp_correspondence}.
:::

::: {.conjecture title="Open problem: uniqueness of the maximal parabolic subdiagram"}

The reflection group $W(S_\Co)$ acts on the period domain, and the $0$-cusp $(9,9,1)_1$ is described by a maximal parabolic subdiagram of the Coxeter diagram $G_{S_\Co}$.
The claim underlying "one $0$-cusp" is that $\widetilde{B}_7(2)$ is the *only* maximal parabolic subdiagram of the highly connected $10$-node diagram $G_{S_\Co}$.
Establishing this requires a subdiagram search on the $10\times 10$ Gram matrix of roots to identify all maximal parabolic configurations and confirm that $\widetilde{B}_7(2)$ is unique.
(The underlying finite root system is of type $B_7$, matching the double-edge $B$/$C$-type diagram at the $0$-cusp rather than the simply-laced $A_7$.)
:::

::: {.remark title="Open problem: hyperbolic-quotient derivation of the cusp correspondence"}

The cusp correspondence between the Coble cusps $(9,9,1)$, $(7,7,1)$ and their Enriques predecessors is established in \cref{thm:cusp_correspondence} (via the divisibility computations of \cref{lem:w1_perp_calculation} and \cref{lem:1_cusp_correspondence}). The migrated notes propose an independent *hyperbolic-quotient* derivation that would place the correspondence on a self-contained lattice footing rather than resting on the alignment of invariants:

- compute the isometry type of the hyperbolic quotient $e^{\perp}/e$ directly for a primitive isotropic $e \in T_\Co$;

- use $\operatorname{div}_{T_\Co}(e)$ to pin down the unique $\Orth(T_\Co)$-orbit and verify that the quotient matches the Enriques signatures $(10,8,0)_1$ for $0$-cusps and $(8,6,0)_0$ for $1$-cusps.

The residue that is genuinely open is the *orbit-uniqueness input*: the proof of \cref{lem:divisibilityTcoOne} presently *assumes* a unique $\Gamma_\Co$-orbit of isotropic vectors in $T_\Co$, which is exactly the enumeration left open above.
:::

## dlt and KSBA stable models

::: {.remark title="Open problem: Coble-specific dlt models and pot geometry"}

The degree-$2$ Enriques program modernizes Morrison's flowerpots [@Mor81] into *dlt* stable pairs, but the *Coble-specific dlt models* are not yet detailed.
The open geometric content is:

- **Coble pot geometry.** Define the explicit stable pair $(\mathcal V, \mathcal D)$ whose "Pot" component is a rational Coble surface, carrying a $\tfrac14(1,1)$ cyclic quotient singularity corresponding to the nodes of the rational sextic $C$.
  This is the local singularity package already conjectured for the stable quotient in \cref{conj:coble_quarter_singularity}, seen here on the *dlt* model (cf.
  \cref{def:dlt-involution-pair}, \cref{def:divisor-model}).

- **Stalk assembly.** Describe the transition of the stalk assembly and the integral-affine configuration as the Enriques surface log-collapses onto the discriminant divisor $\Delta$, where the K3 cover becomes nodal.
:::

::: {.remark title="Open problem: monodromy invariants and stable models $B(\lambda)$"}

Stable limits of Coble surfaces arise as $S_2$-quotients of nodal K3 surfaces, parameterized by a monodromy invariant $\ell \in \check{\cH}$ (surgery sizes) through the construction $B(\lambda)$ of [@AEGS25]. The open work is to:

- determine the map from the transcendental polarization $h_\Co$ to the discretization $\ell$ on the dual complex;

- verify the slc stability of the resulting stable pair $(Z, \varepsilon C)$ for specific surgery vectors $\ell$.

This is the discrete-datum side of the KSBA program whose stability obligations are recorded in \cref{conj:coble_quarter_singularity} and the surrounding KSBA discussion.
:::

## Foundational equations and computational verification

::: {.remark title="Open problem: explicit equations for the Coble curve and its K3 cover"}

A Coble surface $S$ is the blowup of $\PP^2$ at the ten $A_1$ nodes of an irreducible rational plane sextic
$$
C = \ts{ F(x,y,z) = 0 },
\qquad
F(x,y,z) = \sum_{i+j+k=6} a_{ijk}\, x^i y^j z^k,
$$
subject to the nodal conditions $F(p_m) = \partial_x F(p_m) = \partial_y F(p_m) = \partial_z F(p_m) = 0$ at the ten special positions $p_1,\dots,p_{10} \in \PP^2$; the moduli space of such sextics is $9$-dimensional, and explicit models may be sought from the Steiner sextic or from index-$2$ Halphen pencils (cf.
\cref{lem:coble_halphen_blowdown}, \cref{lem:rational_sextic_ten_nodes}). The K3 cover is the double cover $X \xrightarrow{2:1} S$ of $\PP^2$ branched along $C$, with equation $w^2 = F(x,y,z)$ in $\PP(1,1,1,3)$, whose ten $A_1$ nodes lie above the positions $p_m$ (at $w = 0$, $[x:y:z] = p_m$). What is missing is a *worked instance*: derive an explicit equation $F(x,y,z) = 0$ for a rational sextic with ten nodes together with the corresponding cover $w^2 = F$, realizing $C$ as the image of $\PP^1$ under a degree-$6$ map $(s:t) \mapsto [f_0 : f_1 : f_2]$.
Such an instance would anchor the coordinate derivations demanded by the lattice-embedding and involution problems above.
:::

::: {.remark title="Lattice and orbit anchors for the computations"}

The problems above share a small set of concrete starting data, recorded here for reference:

- **Isotropic vectors.** In $S_\Co$, primitive isotropic lines are represented by $v = e_0 \pm e_i$ (with $e_0^2 = 2$, $e_i^2 = -2$).

- **Polarization basis.** The degree-$2$ polarization $h \in T_\En$ is $h = e + f$ in a standard $U$-basis, which must be identified in a basis compatible with $\theta$.

- **Discriminant forms.** $q_{S_\Co} \colon (\mathbb{F}_2)^{11} \to \QQ/2\ZZ$ and $q_{T_\Co} \colon (\mathbb{F}_2)^{11} \to \QQ/2\ZZ$, with isometry of complements forcing $q_{S_\Co} = -q_{T_\Co} \bmod 2\ZZ$.

- **Sterk orbit lift.** For the $2$-elementary $T_\Co$, an orbit is determined by the tuple $(\operatorname{div}(v),\, \bar v \in A_{T_\Co},\, v^2 = 0)$, reducing the search to $\mathbb{F}_2$-vector-space orbits under $\Orth(q_{T_\Co})$.

- **$\Gamma_\Co$ generators.** Computed as the intersection of the reflection group $W(T)$ with the centralizer $Z(\theta)$ and the stabilizer of the primitive vector $h_\Co$.
:::
