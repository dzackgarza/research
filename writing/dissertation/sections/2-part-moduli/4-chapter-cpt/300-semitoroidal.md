
### Semitoroidal Compactifications {#setion-5-3}

Throughout this section, let $T$ be an even lattice of signature $(2, n)$, $\bdlattice{T}{\eta} \da  \bdlattice{T}{\eta} = \eta^{\perp T} / \langle \eta \rangle$ be the boundary lattice of signature $(1, n-1)$ at a $0$-cusp $\eta \in T$, and let $\Gamma\leq \Orth(T)$ be a neat arithmetic subgroup, and let $\eta \in T$ denote a primitive isotropic line in $T$ and $I\subseteq T$ a primitive isotropic plane, corresponding to a 0-cusp of $\bbcpt{\FG}$ and a 1-cusp respectively.
Let $W \da  W(\Gamma_\eta)$ denote the stable reflection group acting on $\bdlattice{T}{\eta}$. Let $\thecone{C} = \thecone{C}(\Gamma_\eta)$ be a fixed fundamental chamber for $W$ defined by the inequalities $(v, \alpha) \ge 0$ for all $\alpha \in \Phi(\Gamma\eta)$. Let $G(\Gamma_\eta)$ be the associated Coxeter diagram and $\Phi(\Gamma_\eta)$ be the set of simple roots for $W(\Gamma_\eta)$.
**Semitoroidal compactifications** ([@Loo85; @Loo03]) $\semitorcpt{\FG}$ generalize the construction of toroidal compactifications $\torcpt{\FG}$ by replacing each polyhedral fan $\Sigma_I$ with a $\Gamma$-admissible **semifan**. The local models are toroidal embeddings attached to semifans, compatibly glued over all cusps.
This section formalizes semifans and semitoroidal compactifications, describes admissibility and compatibility, and relates semitoroidal, toroidal, and Baily–Borel compactifications via a tower of birational morphisms:
$$
\bbcpt{\FG} \longleftarrow \semitorcpt{\FG} \longleftarrow \torcpt{\FG}
.$$
More precisely,

:::{.definition title="Semifans"}
let $V$ be a real finite-dimensional vector space, and let $C \subset V$ be an open, nondegenerate convex cone.
A **semifan** $\mcf$ in $C$ is a collection of closed, convex, rational polyhedral cones $\sigma \subset \thecone{C}_{\QQ}$ such that:

- every face of every $\sigma \in \mcf$ belongs to $\mcf$;
- for any $\sigma, \tau \in \mcf$, the intersection $\sigma \cap \tau$ is a face of both $\sigma$ and $\tau$;
- the interiors of the cones in $\mcf$ are pairwise disjoint.

Unlike a fan, $\mcf$ is not required to be locally finite, nor to cover all of $C$. In particular, $\mcf$ may be infinite and its support $\bigcup_{\sigma \in \mcf} \sigma$ may be a proper subset of $\thecone{C}_{\QQ}$.
This generalization allows, for example, arrangements arising from infinite or non-polyhedral wall structures, as well as dual complexes of degenerations; it thus extends the toroidal theory to situations where the properties of being globally polyhedral or locally finite fail.
:::

:::{.remark}
Recall that the positive cone associated to a primitive isotropic sublattice and its rational closure define a real hyperbolic space by projectivization:
$$
\HH_I \da  \PP(\thecone{C}_{I}) \da \ts{
   \gens{v}_{\RR_{>0}} \subset \bdlattice{T}{I, \RR} \st v^2 > 0
}
.$$
A **tiling** $\tiling_I$ of $\HH_I$ is a locally finite collection of convex polyhedral subsets $\{\tau_\alpha\}_{\alpha \in A}$ such that $\HH_I = \bigcup_\alpha \tau_\alpha^\circ$ is disjoint union of the relative interiors of the tiles, and for each $\alpha$, there is a cone $\sigma \in \mcf_I$ with $\tau_\alpha = \PP(\sigma)$ where $\mcf_I$ is a semifan in $\thecone{C}_{I, \QQ}$.
If for every cone $\sigma \in \mcf_I$ there is a decomposition $\sigma = P \times H_{I, \RR}$ where $P \subset \bdlattice{T}{I, \RR}$ is a convex polytope and $H_{I, \RR} \subset \bdlattice{T}{I, \RR}$ is a fixed real linear subspace, then we say the lattice $H_I \da  H_{I, \RR} \cap \bdlattice{T}{I}$ is the **coning direction**, and the semifan (or equivalently the tiling) is **coned in the direction of $H_I$**.
:::


:::{.definition title="$\Gamma$-admissible semifans"}
Let $T$ be an even lattice of signature $(2, n)$ and $\Gamma \leq \Orth(T)$ a neat arithmetic group. Let $\FG$ be the arithmetic quotient, and $\bbcpt{\FG}$ its Baily–Borel compactification. Each cusp of $\bbcpt{\FG}$ corresponds to a primitive isotropic subspace $I \subset T$. Let $\bdlattice{T}{I} = I^\perp / I$ be the associated boundary lattice and $\thecone{C}_{I, \QQ}$ the rational closure of the positive cone in $\bdlattice{T}{I, \RR}$.
A **$\Gamma$-admissible semifan at the cusp determined by $I$** is a semifan $\mcf_I$ in $\thecone{C}_{I, \QQ}$, invariant under $\Stab_\Gamma(I)$ with finitely many $\Stab_\Gamma(I)$-orbits of cones. The support of $\mcf_I$ need not cover all of $\thecone{C}_{I, \QQ}$ nor be locally finite.
A **compatible system of $\Gamma$-admissible semifans** is a collection $\semifans{F}$, one for each cusp $I$, such that for every inclusion of cusps $I \subset J$ (that is, for inclusions of the underlying isotropic subspaces), the natural projection $\pi_{IJ} \colon \bdlattice{T}{I, \RR} \to \bdlattice{T}{J, \RR}$
satisfies
$$
\mcf_J = \left\{ \pi_{IJ}(\sigma) \st \sigma \in \mcf_I,\, \pi_{IJ}(\sigma) \text{ a cone of positive dimension} \right\}
.$$
:::

As an example, any fan is a semifan, and if a semifan is not a fan, we say it is a **strict semifan**. In particular, the classical toroidal case is recovered by choosing for each $I$ a rational polyhedral fan $\Sigma_I$ supported on $\thecone{C}_{I, \QQ}$ and requiring $\Sigma_I$ to be invariant under $\Stab_\Gamma(I)$ with finitely many orbits. The corresponding compactification is the toroidal compactification $\torcpt{\FG}$.
The "trivial" semifan consists of, for each $I$, the full positive cone $\thecone{C}_{I, \QQ}$ in $\bdlattice{T}{I, \RR}$, which yields $\bbcpt{\FG}$, and thus we will refer to this as the **Baily-Borel semifan** $\mcf^{\BB}$. In this case each local model is essentially the "one-point" (or "one-orbit") compactification, and $\mcf^{\BB}$ is a fan in the toroidal sense.
Generalized Coxeter semifans, defined below, provide intermediate examples of strict semifans. For instance, partial wall data associated to a set of relevant roots yields a semifan that is a coarsening of the Coxeter fan. These may fail to be locally finite -- the boundary decomposition then glues together chambers along the omitted (irrelevant) walls.

----------------------------

#### Construction

:::{.theorem title="Existence of semitoroidal compactifications [@Loo03]"}
Let $T$ be an even lattice of signature $(2, n)$, $\Gamma \leq \OStab(T)$ a neat arithmetic group, and $\FG$ the associated locally symmetric modular variety. Let $\semifans{F}$ be a compatible system of $\Gamma$-admissible semifans ranging over Baily-Borel cusps $I$ of $\bd\bbcpt{\FG}$, as defined above.
Then there exists a normal compactification $\semitorcpt{\FG}$ containing $\FG$ as an open dense subset, called the **semitoroidal compactification** associated to $\semifans{F}$, with the following properties:

1. The boundary strata are in bijection with the set of $\Gamma$-orbits of pairs $(I, \sigma)$, where $I$ is a cusp and $\sigma$ is the class of a cone in $\mcf_I$, modulo the stabilizer in $\Gamma$.

2. If $\sigma \subset \mcf_\eta$ is a cone with $\eta$ an isotropic line corresponding to a Type $\III$ cusp, let $L_{\eta, \sigma} = \eta^{\perp T}/\gens{\eta, \sigma}$.
Then the corresponding stratum is a finite quotient of $L_{\eta, \sigma, \CCstar}$.

3. If $\sigma \subset \mcf_I$ with $I$ an isotropic plane corresponding to a a Type $\II$ cusp, there is a subspace $H_I$  depending on $\sigma$ and an algebraic group $\mce$ defined in @Loo03. Let $L_{I, \sigma} \da I^{\perp}/\gens{I, H_I}$, then the corresponding stratum is a finite quotient of $L_{I, \sigma, \mce}$.

4. For any compatible system of semifans $\semifans{G}$ refining $\semifans{F}$, there is a natural morphism $\semifancpt{\FG}{\semifans{G}} \to \semifancpt{\FG}{\semifans{F}}$ which maps strata to strata according to inclusion of cones: for $\tau \subset \sigma$, the stratum indexed by $(I,\tau)$ maps to the stratum indexed by $(I,\sigma)$.

Note that unlike for fans, strata corresponding to Type $\III$ cones of a semifan may have infinite stabilizer in $\Stab_\Gamma(\eta)$ -- however, the stratum is still a finite quotient of $L_{\eta, \sigma, \CCstar}$.
:::

:::{.definition
    title="{ Semitoroidal compactifications}"
}
Given a compatible system $\semifans{F}$ of $\Gamma$-admissible semifans, the local model of the semitoroidal compactification near the cusp associated to $I$ is a toroidal embedding constructed from $\mcf_I$, typically a finite quotient of a toric embedding $X(\semifans{F})$ associated with the semifan.
For $0$-cusps, the local neighborhood is modeled on such a quotient of a torus fibration, and the boundary strata correspond to cones of $\semifans{F}$. For higher rank cusps ($\rank(I) > 1$), the local model is, locally in the analytic or formal topology, a toric fibration over the boundary stratum corresponding to $I$, whose fibers are toroidal embeddings associated to semifans.
The boundary of $\semitorcpt{\FG}$ is stratified by the cones and faces of all semifans $\semifans{F}$, with strata glued compatibly respecting the combinatorial morphisms given by face projections.
This local-to-global structure enables interpolation between the $\bbcpt{\FG}$ and the maximal $\torcpt{\FG}$ by allowing the semifans to vary from trivial to polyhedral and locally finite.
:::

:::{.theorem title="Birational tower characterization [@AE23, Theorem 5.14]"}
Let $\FG$ be a Type $\IV$ arithmetic quotient, and let $\cpt{\FG}$ be any normal compactification of $\FG$. The following are equivalent:

1. There exist proper morphisms of normal compactifications
   $$
   \torcpt{\FG} \longrightarrow \cpt{\FG} \longrightarrow \bbcpt{\FG}
   $$
   where $\torcpt{\FG}$ is a toroidal compactification and $\bbcpt{\FG}$ is the Baily–Borel compactification.

2. There exists a collection of $\Gamma$-admissible semifans $\semifans{F}$ such that $\semitorcpt{\FG} \iso \cpt{\FG}$.

:::

:::{.theorem title="Recognition theorem for KSBA compactifications [@AE23, Theorem 9.1]"}
Let $R$ be a recognizable divisor in the moduli space of $S$-polarized K3 surfaces (in the sense of [@AE23]) corresponding to the moduli space $F_{\Gamma}$, where $\Gamma$ is the appropriate arithmetic subgroup of $\Orth(T)$ and $T\da S^{\perp \lkt}$. Then there exists a unique semifan $\mcf_R$ such that the normalization morphism $\semifancpt{\FG}{\mcf_R} \to \ksbacpt{\FG}^R$ identifies $\semifancpt{F_M}{\mcf_R}$ as the normalization of the KSBA compactification $\ksbacpt{\FG}^R$ associated to $R$.
The cones of $\mcf_R$ are precisely the maximal subsets in which the combinatorial type of slc stable pairs is constant as a function of the *monodromy invariant* $\lambda$.
:::

:::{.remark}
For any recognizable divisor $R$ on $F_S$, the normalization of the KSBA compactification $\cpt{F}^R$ is a semitoroidal compactification, with the associated semifan $\mcf_R$ determined by $R$.
A fundamental example of a recognizable divisor is the **rational curves divisor** $R_{\rcop}$ for moduli of degree $2d$ K3 surfaces:

\begin{align*}
R_{\rcop} \da  \sum_{i=1}^{n_d} R_i \in |n_d L|
.\end{align*}

where $R_i$ runs over all irreducible rational curves in the linear system $|L|$ of the polarization and $n_d$ is given by the Yau–Zaslow formula ([@AE23, Thm. 10.2]). In @AE23, $R_{\rcop}$ is shown to be recognizable for all $d$, so there exists a canonical semifan $\mcf^{\rcop}$ with

\begin{align*}
\semitorcpt{F_{2d}} \cong \ksbacpt{F_{2d}}
.
.\end{align*}

In degree $2$, $\mcf_{\rcop}$ is a semifan but not a fan, and coarsens the Coxeter fan. For elliptic K3 surfaces with divisor $s + \sum_{i=1}^{24} f_i$, the semifan is in fact a fan, which further refines the maximal cone of the Coxeter fan.
It is currently a widely open problem to describe the semifan $\mcf_R$ for a recognizable divisor in full generality, and is still open in the case of $R = R^{\rcop}$ -- these are currently only characterized only as the coarsest subdivision such that the combinatorial type of stable pairs is constant on its cones.
Our work in @AEGS25 relies on the fact that recognizability was proved for ramification loci of non-symplectic automorphisms in @AE22, and explicit constructions of the corresponding semifans are provided.
:::

#### Generalized Coxeter Semifans and Relevant Roots

:::{.definition #def:relevant-irrelevant title="Relevant and irrelevant roots"}
Let $\bdlattice{T}{\eta}$ be the boundary lattice of signature $(1, n-1)$ for a $0$-cusp $\eta$, with stable reflection group $W = W(\Gamma_\eta)$, simple root system $\Phi = \Phi(\Gamma_\eta)$, and fundamental chamber $\thecone{C} = \thecone{C}_\eta$. The Coxeter diagram is $G = G(\Gamma_\eta)$.
A partition $\Phi = \Phi^{\relevant} \sqcup \Phi^{\irrelevant}$ into **relevant** and **irrelevant** simple roots is defined as follows:

- The roots in $\Phi^{\irrelevant}$ (the **irrelevant roots**) are those for which, in every Kulikov model over the cusp $\eta$, the faces of $\thecone{C}$ defined using only mirrors from $\Phi^{\irrelevant}$ correspond to strata that are contracted in the KSBA stable model over $\eta$.

- The **relevant roots** are those in $\Phi^{\relevant} = \Phi \setminus \Phi^{\irrelevant}$.

:::

:::{.definition title="Generalized Coxeter Semifan [@AET23, Def. 4.16]"}
Fix a partition $\Phi = \Phi^{\irrelevant} \sqcup \Phi^{\relevant}$.
Let $W^{\irrelevant} = \langle w_\alpha \st \alpha \in \Phi^{\irrelevant} \rangle \subset W$ denote the reflection subgroup generated by reflections in the irrelevant roots. The corresponding generalized chamber is
$$
\thecone{L} = \bigcup_{h \in W^{\irrelevant}} h(\thecone{C})
$$
The corresponding **generalized Coxeter semifan** $\mcf_{\genop}$ is the semifan whose maximal cones are $g(\thecone{C}_{\genop} )$ for $g \in W$, with faces given by all intersections of maximal cones not contained in any wall $\alpha^\perp$ for $\alpha \in \Phi^{\relevant}$.
:::

:::{.remark}
Passing from the Coxeter fan to the generalized Coxeter semifan corresponds to deleting nodes of $G(\Gamma_\eta)$ representing the irrelevant roots: walls $\alpha^\perp$ for $\alpha \in \Phi^{\irrelevant}$ are omitted, so maximal cones become unions of Weyl chambers glued along these "inactive mirrors".
If $\Phi^{\irrelevant} = \varnothing$, this recovers the Coxeter fan, while if $\Phi^{\relevant} = \varnothing$, there is a single chamber and this recovers the Baily–Borel fan.
Moreover, if $|W^{\irrelevant}| = \infty$, the resulting semifan is not locally finite, and the compactification is strictly semitoroidal.
Crossing a relevant wall $\alpha^\perp$ corresponds to a birational transformation -- such as a flip, flop, or divisorial contraction -- between KSBA stable models. The chambers cut out by relevant walls in $\thecone{C}$ correspond to regions where the combinatorial type of Kulikov (and hence stable) models remains constant.
:::

#### Generalized Coxeter compactifications

We thus obtain a natural, purely combinatorial way to interpolate between the maximal and minimal compactifications of $\FG$, which can be encoded in a single combinatorial object that we now describe.

:::{.definition #def:semifanposet title="{The semifan poset of a cone}"}
Let $V$ be a real finite-dimensional vector space and $\thecone{C} \subset V$ an open convex cone.
The **semifan poset** $\mathrm{SFan}(\thecone{C})$ is the set of all semifans in $\thecone{C}$, partially ordered by refinement: $\mcf \leq \mcf'$ if every cone of $\mcf$ is contained in a cone of $\mcf'$. The maximal (finest) and minimal (coarsest) elements correspond to the finest locally polyhedral subdivision and the single full cone, respectively.
:::

:::{.definition #def:semitoroidalposet title="{The semitoroidal compactification poset}"}
The **semitoroidal compactification poset** $\theposet{S}_\Gamma$ of $\FG$ is the set of isomorphism classes of semitoroidal compactifications $\semitorcpt{\FG, \semifans{F}}$ constructed from compatible systems of $\Gamma$-admissible semifans $\semifans{F}$ ranging over the cusps $I$ of $\bbcpt{\FG}$.
$\theposet{S}_\Gamma$ is partially ordered: $\semifancpt{\FG}{ \semifans{F} } \leq \semifancpt{\FG}{ \semifans{G} }$ if $\semifan{F}_I$ refines $\semifan{G}_I$ for all $I$.
This order is reversed under induced morphisms, i.e., coarser semifans yield "smaller" compactifications.
The maximal element corresponds to the maximal toroidal compactification; the minimal to the Baily–Borel compactification.
:::

:::{.definition #def:coxetersemiposet title="{The Coxeter semitoroidal compactification poset}"}
For each $0$-cusp $\eta$ of $\bbcpt{\FG}$, let $G(\Gamma_\eta)$ be the stable Coxeter diagram, and $\theposet{P}_{G(\Gamma_\eta)}$ the poset of subdiagrams under inclusion.
Define the **Coxeter semitoroidal compactification poset** of $\FG$ as the coproduct poset
$$
\theposet{P}_\Gamma \da  \coprod_{\eta \in \bd\bbcpt{\FG}} \theposet{P}_{G(\Gamma_\eta)}
.$$
An element $(D_\eta) \in \theposet{P}_\Gamma$ specifies, for each $0$-cusp, a subdiagram $D_\eta \subset G(\Gamma_\eta)$ and thus a set of irrelevant roots at each cusp.
:::

:::{.proposition #prop:coxsemiposetmap title="{Coxeter semifan system and main identification}"}
There is a canonical poset morphism
$\Psi\colon \theposet{P}_\Gamma \longrightarrow \theposet{S}_\Gamma$
which sends a tuple $(D_\eta)$ of subdiagrams, one for each $0$-cusp $\eta$, to the induced semitoroidal compactification, constructed by gluing together maximal cones of generalized Coxeter semifans (as in @def:coxetersemiposet) along all omitted walls, corresponding to the nodes omitted in $D_\eta$.
The maximal element of $\theposet{P}_\Gamma$, where no nodes are omitted, corresponds to the Coxeter fan and thus the toroidal compactification.
The minimal element, where all nodes are omitted at each cusp, corresponds to the Baily–Borel fan $\BBfan$ and thus $\bbcpt{\FG}$.
Morphisms in $\theposet{P}_\Gamma$ corresponding to deleting more nodes correspond to coarsenings of the semifans and thus to proper birational morphisms between the corresponding semitoroidal compactifications.
:::

:::{.remark}
The poset $\theposet{S}_\Gamma$ of semitoroidal compactifications organizes all normal compactifications arising from systems of $\Gamma$-admissible semifans over the boundary strata of $\FG$.
The Coxeter semitoroidal subposet $\theposet{P}_\Gamma$ parameterizes those compactifications obtained as Coxeter-type (generalized Coxeter semifan) coarsenings of local reflection decompositions, and is canonically identified with the product of subdiagram posets at all $0$-cusps.
The product $\theposet{P}_\Gamma$ thus parameterizes exactly the semitoroidal compactifications of $\FG$ arising from generalized Coxeter semifans, distinguished in the full semitoroidal poset $\theposet{S}_\Gamma$.
Note that the latter may contain other compactifications, and the author is not aware of any choices of $\FG$ for which $\Psi$ is known to be surjective or bijective.
:::

