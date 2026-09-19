### Descent of Semitoroidal Data {#section-7-5}

In order to construct a modular compactification of the moduli space of stable Enriques pairs -- with explicit control of the boundary -- it is necessary to analyze the singularities along the boundary of the Noether–Lefschetz locus $B \subset \cpt{\fttz}$ and to pass to the normalization. This normalization process allows the descent of the ramification semifans from $\fttz$ to $\fent$, which defines $\semitorcpt{\fen}$.

:::{.proposition
    title="{Normalization and Pullback Family}"
    #prop:normalization-pullback-family
}
Let $\nu: \normalize{B} \to B$ be the normalization of $B$. Then:

- $\normalize{B}$ is a normal projective variety,

- The morphism $\nu$ is finite, surjective, birational, and proper,

- The pullback family $\nu^*(\mcz, \epsilon \mcr_Z)$ is a family of KSBA-stable Enriques pairs of degree two over the normal base $\normalize{B}$.
:::

:::{.proof}
By construction, $B$ is a closed subvariety of the projective stack $\cpt{\fttz}$; thus, the integral closure is finite, and normality follows. The KSBA stability of fibers is preserved under finite base change, giving the desired family.
:::

:::{.proposition
    title="{Non-normality of the Noether–Lefschetz Locus}"
    #prop:non-normality-nl-locus
}
Let $B \subset \mcm$ be a Noether–Lefschetz locus with compactification $\cpt{B} \subset \cpt{\mcm}$, and let $\Delta = \cpt{\mcm} \setminus \mcm$ denote the boundary divisor. The failure of normality of $\cpt{B}$ along $\Delta$ arises through three mechanisms:

- (1) There exist boundary divisors $D \subset \Delta$ such that the period map $\mathsf{P}: \mathcal{X} \to \mcm$ is not unramified over generic points of $D$; precisely, there exist points $x \in D$ for which the fiber $\mathsf{P}^{-1}(\mathsf{P}(x))$ contains multiple distinct analytic branches, so the local ring of $\cpt{B}$ at $x$ is not integrally closed. For example, if $D$ corresponds to a boundary component where the monodromy is not trivial, analytic local neighborhoods of $\cpt{B}$ near $x$ may be modeled by $\Spec \CC[u,v]/(uv)$ modulo a nontrivial group action.

- (2) If irreducible components $D_i, D_j \subset \Delta$ meet nontransversely, so that the intersection $D_i \cap D_j$ is singular or not snc, the locus $\cpt{B} \cap (D_i \cap D_j)$ acquires corresponding singularities, so that the local ring is not regular nor normal at such points, and normalization introduces ramification over this locus.

- (3) For monodromy representations $\rho: \pi_1(\mcm) \rightarrow \mathrm{Aut}(H^2_{\mathrm{prim}})$ with nontrivial global monodromy group $\Gamma$ acting on the vanishing cohomology parametrized by $B$, nontrivial identifications occur in the image $\cpt{\mathrm{Im}(B)} \subset \cpt{\mcm}$ along boundary strata, so that the normalization of $\cpt{B}$ is a finite ramified cover branched along these loci, and the structure sheaf is not normal at points over such identifications.

It follows that normalization of $\cpt{B}$ corresponds to resolving the branching and non-normal crossing behavior caused by failure of injectivity of the period map, singularities in the intersection of boundary divisors, and ramification induced by the global monodromy representation.
:::

Let $\mathsf{P}: \fent \to \fttz$ denote the period map between the moduli stack of lattice-polarized K3 (or Enriques) surfaces and its image in the period domain, extended to suitable toroidal or semi-toric compactifications $\cpt{\fent} \to \cpt{\fttz}$ as established in @AEGS25. Both source and target are Deligne–Mumford stacks, locally of finite type over $\CC$.

:::{.proposition}
The non-normality of the scheme-theoretic image of $\cpt{\fent} \to \cpt{\fttz}$ (and in particular for the closures of Noether–Lefschetz loci) along the boundary $\Delta = \cpt{\fttz} \setminus \fttz$ is a consequence of failures of separatedness and unramifiedness of the period map at points of $\Delta$, due to three mechanisms: (1) failure of injectivity of the period map at the boundary, (2) non-transversality of the intersection of irreducible components of $\Delta$, and (3) identifications arising from monodromy action.
:::

:::{.proof}
1. **Failure of injectivity over boundary divisors.**
   
   Let $x \in D \subset \Delta$ be a point lying on a boundary divisor. Consider the local behavior of $\cpt{\fent}$ and the period map over a small analytic neighborhood $U$ of $x$. The period map may send distinct limit points in $\cpt{\fent}$ (corresponding to non-isomorphic degenerations with the same mixed Hodge structure or period data) to the same point in $\cpt{\fttz}$, particularly when the monodromy representation around $D$ is nontrivial. Formally, there exist $y_1, y_2 \in \cpt{\fent}$ with $\mathsf{P}(y_1) = \mathsf{P}(y_2) = x$ but which are not identified scheme-theoretically in $\cpt{\fent}$. The completed local ring $\widehat{\mathcal{O}}_{\cpt{\fent},y_1} \times \widehat{\mathcal{O}}_{\cpt{\fent},y_2}$ then maps finitely (and possibly not surjectively) into $\widehat{\mathcal{O}}_{\cpt{\fttz},x}$, so the scheme-theoretic image is not normal at $x$: it has multiple analytic branches glued via the period map, and integral closure introduces a normalization that separates these branches.

2. **Non-transversality of boundary divisor intersections.**
   
   Suppose $x \in D_1 \cap D_2$, where $D_1, D_2 \subset \Delta$ are distinct irreducible components and their intersection is non-transverse. Locally, the structure of $\cpt{\fttz}$ near $x$ is modeled as $\operatorname{Spec} \CC[[u,v]]/(uv)$ or, for higher codimension intersections, as the vanishing locus of a product of local coordinates. If $\cpt{\fent}$ maps into $\cpt{\fttz}$ so that the scheme-theoretic fiber above $x$ is reducible or singular, then the local ring at $x$ fails Serre's condition $(R_1)$ or $(S_2)$ for normality, as integral closure may add missing functions or resolve multiple components. The normalization then corresponds to separating these intersection branches, producing a cover ramified along $D_1 \cap D_2$.

3. **Monodromy identifications and stack-theoretic quotients.**
   
   The global monodromy group $\Gamma \leq \mathrm{O}(L)$ acts on the boundary components and may have nontrivial stabilizer orbits in the boundary. This manifests locally as a finite group action (coming from automorphisms in the degenerating family or stacky structure in the moduli) on the germ $U$ of $\cpt{\fttz}$: the scheme-theoretic image is modeled by the quotient $U/G$, where $G$ is a subgroup of $\Gamma$. The resulting singularities are quotient singularities, and the local ring of invariants is not integrally closed unless the action is free. Thus, normalization corresponds to passing to the cover $U$ before forming the quotient, and non-normality reflects the presence of ramification or fixed points for the group action.

Each of these three mechanisms can be realized concretely in families of degenerating lattice-polarized K3 or Enriques surfaces (see [@AEGS25, §6], for explicit models). In each case, non-normality of the scheme-theoretic image of the period map along the boundary is a direct consequence of the existence of multiple branches, nontransverse intersections, or stacky (ramified) structure resulting from monodromy. The normalization resolves the non-normal behavior, yielding a finite (possibly ramified) cover of the image.
:::


:::{.theorem
    title="{Universal Family and Moduli Classification}"
    #thm:universal-family-moduli
}
The pulled-back family

\begin{align*}
(\mcz^\nu, \epsilon \mcr_Z^\nu) := \nu^*(\mcz, \epsilon \mcr_Z) \to \normalize{B}
.\end{align*}

satisfies:

- Every fiber is a KSBA-stable Enriques pair of degree two,
- The family is universal among stable families over normal bases mapping to $\cpt{\fent}$,
- There exists a canonical classifying morphism $\phi: \normalize{B} \to \cpt{\fent}$ compatible with the moduli functor.
:::

:::{.proof}
Stability is preserved by finite base change. The normalization $\normalize{B}$ is initial among all normalizations, so universality follows for any family over a normal base mapping to $B$. Existence of the classifying morphism is a consequence of functoriality and the representability of KSBA moduli stacks.
:::

:::{.proposition
    title="{Restriction of Semifans and Semitoroidal Compactification}"
    #prop:restriction-semifans
}
The embedding $B \hookrightarrow \cpt{\fttz}$ induces on $\normalize{B}$ a semitoroidal structure as follows:

- The period domain $\halfpd{B}$ for $\normalize{B}$ embeds as a closed linear subdomain of the period domain for $\fttz$, determined by additional constraints imposed by symmetry under the involution,
- The rational polyhedral cones from the ramification semifan $\semifan{F}_{\ram}$ on $\cpt{\fttz}$ restrict to produce a semifan $\semifan{F}_B$ on $\normalize{B}$,
- The normalization $\normalize{B}$ is isomorphic, as a modular compactification, to the semitoroidal compactification associated to $\semifan{F}_B$.
:::

:::{.proof}
The restriction of the period domain reflects the imposition of involution-invariant lattice conditions cutting out Enriques double covers. The restriction of the polyhedral structure from $\cpt{\fttz}$ follows functorially from intersecting the hyperplane arrangements of $\semifan{F}_{\ram}$ with the subdomain $\halfpd{B}$, as the arrangement is defined by orthogonality to lattice roots/divisors that may be fixed or permuted by the involution. The unique semitoroidal compactification is then determined by the induced semifan structure on the normalization.
:::

:::{.construction
    title="{Folded Semifans and Complete Boundary Stratification}"
    #const:folded-semifans
}
The classifying morphism $\phi: \normalize{B} \to \cpt{\fent}$ transports the combinatorial structure of $\semifan{F}_B$ to the boundary stratification on $\cpt{\fent}$.
According to the explicit construction in [@AEGS25, §2.2], the semitoroidal compactification $\ksbacpt{\fent}$ is isomorphic to $\cpt{\fent}^{\semifan{F}}$, where $\mathcal{F} = \{\semifan{F}_k\}_{k=1}^5$ is the collection of semifans assigned to the five $0$-cusps (maximal boundary components) of $\cpt{\fent}$.
Each semifan $\semifan{F}_k$ associated to the five 0-cusps of the moduli space $\mathcal{F}_{\mathrm{En},2}$ is defined by intersecting the ambient ramification semifan $\semifan{F}_{\mathrm{ram}}$ for the K3 covering with the period subdomain corresponding to the cusp, followed by folding under the involution. This folding identifies cones related by involution-invariant lattice automorphisms.
For each $k$, the combinatorial structure is given by the following:

- The semifan $\semifan{F}_k$ is a *generalized Coxeter semifan* in the sense that it is a coarsening of the corresponding folded Coxeter semifan. Its maximal cones are indexed by faces not in the orbits of *irrelevant roots*.
- For $\semifan{F}_2$ and $\semifan{F}_4$, the subgroup generated by the irrelevant roots is finite, and so the semifan is a finite rational polyhedral fan; these cusps correspond to genuinely toroidal strata in the compactification.
- For $\semifan{F}_1$, $\semifan{F}_3$, and $\semifan{F}_5$, the subgroup generated by the irrelevant roots is infinite, and the resulting semifan is infinite but locally finite. The boundary strata corresponding to these cusps are strictly semitoroidal.
- The precise structure of all boundary strata is completely determined by the maximal cones of these semifans, together with the folding data by the involution.
:::

:::{.proposition
    title="{Properties of the Classifying Morphism}"
    #prop:properties-classifying
}
The classifying morphism $\phi : \normalize{B} \to \cpt{\fent}$ has the following properties:

- $\phi$ is birational and an isomorphism over the interior moduli stack $\fent$,
- $\phi$ is proper as a morphism between proper Deligne–Mumford stacks,
- $\phi$ respects the combinatorial boundary stratification induced by the semitoroidal structures: the combinatorial types of boundary strata, as encoded by cones of the folded semifans, correspond under $\phi$, so that degeneration types are preserved.
:::

:::{.proof}
Birationality and identification on the open locus is a consequence of the moduli interpretation and the universal property of normalization. Properness follows from the properness of the moduli stacks and the modular representability. Compatibility with the combinatorial stratification is a consequence of the construction of the semifans and their folding, and is treated in full detail in @AEGS25.
:::
