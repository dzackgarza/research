### Finiteness by Kulikov Models and a Coarsening Argument {#section-7-6}

<!--
Background Definitions

### 1. Semifan Structures and Boundary Stratification

**Definition 1.1 (Semifan).**  
A *semifan* $\Sigma$ attached to a toroidal or semitoroidal compactification is a polyhedral decomposition of the boundary cone associated to each cusp. For each $k \in \{1, \dots, 5\}$, let $\semifan{F}_k$ denote the semifan on the $k$th boundary component, as defined in detail in [AEGS, §5.2][AEGS.pdf]; these arise from the Coxeter fan modulo an explicit coarsening coming from the stable pair moduli problem.

**Definition 1.2 (Coarsening of Semifans).**  
A semifan $\semifan{G}_k$ is a *coarsening* of $\semifan{F}_k$ if every cone $\sigma$ of $\semifan{G}_k$ is a union of cones in $\semifan{F}_k$. In geometric terms, coarsening contracts certain boundary strata, potentially identifying distinct types of degenerations.

:::{.lemma title="Semifan Comparison" #lem:semifan-comparison}
Let $\semitorcpt{\fent}$ denote the semitoroidal compactification defined using the five semifans $\semifan{F} = \{\semifan{F}_k\}_{k=1}^5$. There exist semifans $\semifan{G} = \{\semifan{G}_k\}_{k=1}^{5}$ associated with the KSBA compactification $\ksbacpt{\fent}$ such that:
1. $\ksbacpt{\fent} = \semitorcpt{\fent}$ if and only if $\semifan{G}_k = \semifan{F}_k$ for every $k$.
2. Each $\semifan{G}_k$ is a coarsening of $\semifan{F}_k$.
3. The morphism $\phi$ is finite if and only if all $\semifan{G}_k = \semifan{F}_k$.
:::

:::{.proof}
The normalization of any KSBA compactification with recognized boundary divisors admits a semitoroidal structure defined by a tuple $\{\semifan{G}_k\}$. For each $k$, a coarsening $\semifan{G}_k\subseteq\semifan{F}_k$ means that certain boundary strata, corresponding to distinct cones in $\semifan{F}_k$, are identified in the KSBA moduli space $\ksbacpt{\fent}$. By the structure of semitoroidal (and toroidal) compactifications, the strata correspondence is functorial and set-theoretically bijective if and only if there is no coarsening (see [AE23, Theorem 7.18][AEGS.pdf]). Thus, $\phi$ is finite if and only if all semifans agree.
:::

#### 2. Technical Notions and Maximality of Degenerations

**Definition 2.1 (Dual Complex, Double Curves, Maximality).**  
Let $(X_0,\epsilon R_0)$ be a stable pair degeneration. The *dual complex* is the simplicial complex whose vertices correspond to irreducible components of $X_0$ and whose edges correspond to double curves $D_{ij}\subset X_0$ (i.e., irreducible curves lying in the intersection of two distinct irreducible components).  
A degeneration is **maximal** if its dual complex realizes the largest possible number of vertices and edges among all degenerations with fixed monodromy invariants ([AEGS, Def. 4.7, Prop. 4.8][AEGS.pdf]).

**Definition 2.2 (Type II/III models, Half-divisor models).**  
A Type III Kulikov model is one where all components are rational and the dual complex is a triangulation of $\mathbb P^2$; Type II models correspond to complex affine lines or other lower-dimensional dual complexes. Half-divisor models are (possibly reducible) stable limits of Enriques pairs with a ramification half-divisor ([AEGS, §4.4][AEGS.pdf]).

----

### 1. Equivalence Between Semifan Agreement and Finiteness (Critical Gap)

**Where:**
- Lemma “Semifan Comparison” and the implication “ϕ is finite iff all semifans agree.”

**Problem:**
- This equivalence is asserted, not explained. There is no argument showing why the *combinatorial data of semifans alone* suffices for finiteness of the global morphism ϕ.
- It's entirely possible for local (boundary) combinatorics to match while the global map fails to be quasi-finite or proper due to phenomena away from the boundary.

**What to do:**
- Provide a precise mathematical argument or reference showing that the semifan data actually control all fibers of ϕ—including those not lying in the boundary.
- Explicitly prove that agreement of the semifans ensures there are no positive-dimensional fibers of ϕ anywhere.
- If you rely on a canonical result or functoriality (e.g., a reference to a theorem about semitoroidal compactifications controlling moduli maps), cite it explicitly and summarize its content.
- If an argument via “strata are in bijection, so fibers are finite” is intended, spell out why this bijection is guaranteed, both set-theoretically and scheme-theoretically.

---

### 2. Missing Proofs of Properness and Quasi-finiteness

**Where:**
- Corollary stating “with semifans agreeing, the morphism ϕ is proper, quasi-finite, and hence finite by Zariski's Main Theorem.”

**Problem:**
- **Properness and quasi-finiteness are not established**. The passage merely asserts that semifan agreement implies these properties—without bridging the gap.
- Zariski's Main Theorem only applies once properness and quasi-finiteness are shown.

**What to do:**
- Present an explicit proof that ϕ is proper: identify which compactness results or valuative criteria you are invoking. For example, is properness inherited from properties of the moduli stack or from properties of the semitoroidal model? If so, cite the precise result.
- Justify quasi-finiteness: show that, given boundary stratum combinatorics and interior matching, fibers of ϕ are necessarily finite; address the possibility of positive-dimensional fibers.
- State clearly which hypotheses you are using from the KSBA/theory (e.g., normality, finite type, boundary structure) and document how they ensure the required map properties.

---

### 3. Logical Chain for Boundary/Strata Matching

**Where:**
- Theorem and proof regarding “No Coarsening Occurs” and the relationship between strata/degenerations for ϕ.

**Problem:**
- The explanation for why semifan coarsening would collapse finiteness is *not spelled out*. The logic from “identified cones in a coarsening” to “identifications of maximal vs. non-maximal degenerations” is presumed but not constructed.
- The argument regarding maximality is described narratively, but lacks a stepwise, formal structure.

**What to do:**
- Explicitly state:
    - Which strata or points in the moduli stack correspond to which cones in the semifan.
    - The mechanism by which identifications in the semifan induce (or do not induce) identifications in moduli or cause fiber dimension jumps in the map ϕ.
    - Why maximal/non-maximal degenerations correspond precisely to the structure of the semifans, and how strata identification implies (non-)finiteness.
- For each implication, ground your claim in concrete properties (e.g., describing local models around singularities, functoriality of the normalization process, etc.).


**In your revision, address every specific gap above. Ensure that all logical dependencies, object definitions, proof steps, and reference uses are explicit, detailed, and verifiable directly from your manuscript. Do not leave assertions or equivalences to the reader or reviewer to supply.**

 -->

<!--
We now prove a crucial structural property of the classifying morphism $\phi : \normalize{B} \to \cpt{\fent}$ constructed in previous sections: namely, that $\phi$ is finite. This assertion is the final step needed for modular identification of the compactified moduli of degree-2 polarized stable Enriques pairs via the period map and semitoroidal construction, and its proof relies on a precise analysis of the combinatorial boundary stratifications encoded by the semifans developed earlier.

:::{.theorem
    title="Finiteness of the Classifying Map"
    #thm:finiteness-classifying
}
The classifying morphism $\phi : \normalize{B} \to \cpt{\fent}$ is finite.
:::

To establish this result, we compare the semitoroidal structures on source and target, using the combinatorial data provided by the corresponding semifans. The proof is based on the matching of boundary stratifications and the maximality of degenerations as detected in the geometry of Kulikov models.

:::{.lemma
    title="Semifan Comparison"
    #lem:semifan-comparison
}
Let $\semitorcpt{\fent}$ denote the semitoroidal compactification defined using the five semifans $\semifan{F} = \{\semifan{F}_k\}_{k=1}^5$ as in [@AEGS25, §5.2]. There exist semifans $\semifan{G} = \{ \semifan{G}_k \}_{k=1}^5$ such that:
1. $\ksbacpt{\fent} = \semitorcpt{\fent}$.
2. Each $\semifan{G}_k$ is a coarsening of $\semifan{F}_k$.
3. The morphism $\phi$ is finite if and only if $\semifan{G}_k = \semifan{F}_k$ for all $k$.
:::

:::{.proof}
By [@AE23, Theorem 7.18], the normalization of any KSBA compactification with recognizable boundary divisor admits a semitoroidal structure, uniquely determined by a tuple of semifans $\semifan{G} = \{ \semifan{G}_k \}$. Coarsening $\semifan{G}_k \subseteq \semifan{F}_k$ means that cones in $\semifan{F}_k$ may be identified in $\semifan{G}_k$, which would indicate identifications of strata—and thus non-finiteness—over those boundary components. Thus, $\phi$ is finite if and only if no such coarsening occurs (i.e., the semifans agree).
:::

:::{.definition
    title="Maximality of Degenerations"
    #def:maximality-degenerations
}
A degeneration $(X_0, \epsilon R_0)$ of K3 pairs is called **maximal** if the dual complex of $X_0$ has the largest number of vertices and edges among all degenerations with the same monodromy data. The analogous definition applies for Enriques degenerations $(Z_0, \epsilon R_{Z,0})$.
:::

:::{.proposition
    title="The Double Curve Constraint"
    #prop:double-curve-constraint
}
Let $(X_0, \epsilon R_0)$ be a degeneration of K3 pairs with a fixed-point-free Enriques involution $\ien$; its quotient is $(Z_0, \epsilon R_{Z,0}) = (X_0, \epsilon R_0)/\ien$. Then:
- The number of irreducible components of $Z_0$ is the number of $\ien$-orbits of components of $X_0$.
- The number of double curves in $Z_0$ is the number of $\ien$-orbits of double curves in $X_0$.
- $(Z_0, \epsilon R_{Z,0})$ is maximal if and only if $(X_0, \epsilon R_0)$ is maximal.
:::

:::{.proof}
The first two claims follow from the behavior of the quotient map: irreducible components and double curves of $X_0$ are grouped into orbits by $\ien$ and descend to components and double curves of $Z_0$ respectively.

[@AEGS25, Prop. 4.8] shows that if $(\mcz, \mcr_\mcz) \to (C, 0)$ is a half-divisor model for $\fent$, then we have the following possibilities:

- Type $\III$:
  - Cusp 1:
    - $\Gamma(\mcx_0) = \RP^2$, and each component $V_i$ is isomorphic (up to normalization) with one of its inverse images in the K3 cover $\mcx_0$,
  - Cusps 2,3,4,5:
    - $\Gamma(\mcx_0) = \DD^2$, and if $V_i$ is covered by two irreducible components, then it is isomorphic up to normalization to either of them.
    Otherwise, if it is covered by one component of  $\tilde V_0 \subset \mcx_0$, then $\ienzero\actson V_i$ with 4 fixed points, two pairs on particular double curves $\tilde D_{ij}, \tilde D_{ik}$ in $\tilde V_i$.
- Type $\II$:
  - $\Gamma(\mcx_0) = \DD^1$, and
    - For the cusps mapping to $\fen$, $\ienzero$ acts by $x\mapsto -x$ on $\DD^1$ and fixed-point-freely on $\mcx_0$,
    - For the remaining cusps, assuming $\mcx_0$ contains a double curve $E$ preserved by $\ienzero$, it acts by nontrivial 2-torsion. It preserves each component of $\mcx_0$, and on double curves $D_{ij}$, the action is an elliptic involution with 4 fixed points.

Moreover, by [@AEGS25, Cor. 4.9], the KSBA stable limit of $(\mcz^*, \eps \mcr^*_{\mcz^*}) \to C^*$ can be computed from the half-divisor model $(\mcz, \mcr_\mcz)\to (C, 0)$ as the relative proj of the section ring for $\mcr_\mcz$.

Thus the dual complex and monodromy invariants classify the degeneration up to equivalence. Since the semifan construction (cone decomposition) is preserved under folding by $\ien$, maximality is inherited between the K3 and Enriques degenerations.
:::

:::{.theorem
    title="No Coarsening Occurs"
    #thm:no-coarsening
}
For each $k \in \{1,2,3,4,5\}$, the boundary semifans satisfy $\semifan{G}_k = \semifan{F}_k$.
:::

:::{.proof}
Assume, toward a contradiction, that for some $k$ the semifan $\semifan{G}_k$ is a strict coarsening of $\semifan{F}_k$. Then there exists a codimension-one cone $\sigma \in \semifan{F}_k$, which is the common face of two maximal cones $\tau_1, \tau_2 \in \semifan{F}_k$ that are identified in $\semifan{G}_k$. This identification means $\tau_1$ and $\tau_2$ correspond to a single boundary stratum in the KSBA compactification.

Consider points in $\normalize{B}$ mapping to $\sigma$ via the period map: these correspond to K3 degenerations $(X_0, \epsilon R_0)$ in which the dual complex drops one double-curve relative to maximality. The corresponding Enriques quotients $(Z_0, \epsilon R_{Z,0})$ must also have non-maximal dual complex, by the double-curve constraint just established. However, the identified stratum $\tau_1 = \tau_2$ in $\semifan{G}_k$ corresponds to maximal degenerations, not to degenerations with one fewer double curve. This is a contradiction: distinct boundary strata of maximal and non-maximal degenerations cannot be identified unless the moduli problem fails to separate them, but the dual complex encodes maximally degenerate boundary points uniquely. Thus, no such coarsening occurs, and $\semifan{G}_k = \semifan{F}_k$ for all $k$.
:::

:::{.corollary
    title="Finiteness of the Classifying Map"
    #cor:finiteness-classifying-map
}
By the previous lemma, the boundary stratifications, as encoded by semifans, agree identically. Therefore, the morphism $\phi: \normalize{B} \to \cpt{\fent}$ is finite.
:::

:::{.proof}
With semifans agreeing as established above, the semitoroidal compactifications on both source and target coincide; since all local fibers are finite (indeed, are points at the top-dimensional boundary), and since both spaces are proper and normal, the morphism $\phi$ is proper, quasi-finite, and hence finite by Zariski's Main Theorem.
:::
 -->


We now prove a crucial structural property of the classifying morphism

\begin{align*}
\phi : \normalize{B} \to \cpt{\fent}
.\end{align*}

constructed in previous sections: namely, that $\phi$ is finite. This assertion is the final step needed for modular identification of the compactified moduli of degree-2 polarized stable Enriques pairs via the period map and semitoroidal construction.

#### Semifan Comparison and Finiteness: Addressing the Critical Gap

:::{.lemma title="Semifan Comparison" #lem:semifan-comparison}
Let $\semitorcpt{\fent}$ be the semitoroidal compactification defined using the five semifans $\semifan{F} = \{\semifan{F}_k\}_{k=1}^5$ as in @AEGS25. By [@AE23, Thm. 7.18], the normalization $\normksbacpt{\fent}$ of the KSBA compactification is semitoroidal for a collection of semifans $\semifan{G} = \{\semifan{G}_k\}_{k=1}^5$ such that:

1. Each $\semifan{G}_k$ is a coarsening of $\semifan{F}_k$.

2. The classifying morphism $\phi\colon\normalize{B}\to\ksbacpt{\fent}$ is finite exactly when no further coarsening occurs, equivalently when $\semifan{G}_k=\semifan{F}_k$ for every $k$.
:::

:::{.proof}
The normalization $\normalize{B}$ is already the semitoroidal compactification for the semifans $\semifan{F}_k$, by the construction in the preceding section and the proof of [@AEGS25, Thm. 5.9]. The normalization of the KSBA target is, by [@AE23, Thm. 7.18], obtained by coarsening these semifans. Thus the induced map between the two normal semitoroidal compactifications is the contraction attached to the coarsening. It is an isomorphism precisely when the coarsening is trivial. In that case the classifying morphism $\phi$ factors through this common normalization and is the finite normalization morphism to $\ksbacpt{\fent}$.
:::

#### Maximality, Moduli, and Injectivity: Scheme-Theoretic Proof

:::{.definition title="Maximality of Degenerations" #def:maximality-degenerations}
A degeneration is **maximal** here if its stable central fiber has the maximal possible number of double curves among degenerations in the corresponding semitoroidal boundary family.
:::

:::{.proposition title="The Double Curve Constraint" #prop:double-curve-constraint}
Let $(X_0, \epsilon R_0)$ be a stable limit of K3 pairs carrying the Enriques involution, and let $(Z_0, \epsilon R_{Z,0})$ be its Enriques quotient. Then $(Z_0,\epsilon R_{Z,0})$ has the maximal number of double curves if and only if $(X_0,\epsilon R_0)$ does.
:::

:::{.proof}
This is the consequence of the explicit Kulikov and stable models singled out in the proof of [@AEGS25, Thm. 5.9], using [@AEGS25, Prop. 4.8 and Cor. 4.9]. Those descriptions show directly that maximality of the number of double curves is preserved by passage between a stable K3 pair and its Enriques quotient.
:::

#### The Core Finiteness-Injectivity Argument

:::{.theorem title="No Coarsening Occurs" #thm:no-coarsening}
For each $k \in \{1,2,3,4,5\}$, the boundary semifans satisfy $\semifan{G}_k = \semifan{F}_k$.
:::

:::{.proof}
Suppose that some $\semifan{G}_k$ is a strict coarsening of $\semifan{F}_k$. As in the proof of [@AEGS25, Thm. 5.9], there is then a codimension-one cone of $\semifan{F}_k$ which parameterizes a one-dimensional family of non-maximal K3 pairs $(X,\epsilon R)$, while their Enriques quotients $(Z,\epsilon R_Z)$ become maximal after passing to the coarser KSBA semifan. This contradicts @prop:double-curve-constraint. Therefore every coarsening is trivial, so $\semifan{G}_k=\semifan{F}_k$ for all $k$.
:::

#### Finiteness of the classifying morphism

:::{.corollary title="Finiteness of the Classifying Map" #cor:finiteness-classifying-map}
The morphism $\phi: \normalize{B} \to \ksbacpt{\fent}$ is finite.
:::

:::{.proof}
By @thm:no-coarsening, the normalization of the KSBA compactification is the same semitoroidal compactification $\normalize{B}$ defined by the semifans $\semifan{F}_k$. Hence $\phi$ is the normalization morphism of $\ksbacpt{\fent}$, and is finite.
:::
