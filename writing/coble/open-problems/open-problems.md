# Open problems and technical gaps {#sec-open-problems}

::: {.remark title="Orientation"}

This section records the known open problems and computational obstacles of the Coble moduli program.
Each entry is a genuine gap between the results established elsewhere in this document and the fully rigorous, coordinate-explicit statements one would want for parity with the Enriques degree-$2$ program of [@AEGS25].
The problems are grouped by theme: lattice-theoretic verifications, the enumeration of isotropic orbits and cusps together with the reflection-group combinatorics, the *dlt* and KSBA stable models, and the foundational equations and computational checks.
None of the statements below is claimed to be settled; several cross-reference partial results already in the text, and in each case the *residue* that remains open is stated explicitly.
:::

## Lattice-theoretic gaps

::: {.remark title="The genus and the discriminant representation of the Coble lattices"}

The invariants $(r,a,\delta)$ of the geometric lattice $S_\Co \cong (11,11,1)_1$ (signature $(1,10)$, Gram matrix $\diag(2,-2,\dots,-2)$, equivalently $\generators{-2}\oplus E_{10}(2)$) and of the transcendental lattice $T_\Co = S_\Co^{\perp \lkt} \cong (11,11,1)_2$ (signature $(2,9)$) are recorded in [the Coble lattice table](#sec-coble-lattice-table), and both satisfy $q_{S_\Co} \cong q_{T_\Co} \cong (\ZZ/2\ZZ)^{11}$ with $q_{S_\Co} = -q_{T_\Co} \bmod 2\ZZ$.
Both lattices are even, indefinite and $2$-elementary, with both signature indices nonzero, so Nikulin's two theorems on $2$-elementary lattices apply with no further hypothesis: each is the unique lattice in its genus (@thm:two-elementary-classification, [@Nik80, Thm. 3.6.2]), and $\Orth(T_\Co)\to\Orth(q_{T_\Co})$ and $\Orth(S_\Co)\to\Orth(q_{S_\Co})$ are surjective (@thm:two-elementary-surjectivity, [@Nik80, Thm. 3.6.3]).
Neither theorem has a hypothesis $r > a$. The case $r > a$ is the one in which Nikulin's general criteria [@Nik80, Cor. 1.13.3 and Thm. 1.14.2] already give both conclusions, and the case $r = a$, which is that of $S_\Co$ and $T_\Co$ with $r = a = 11$, is treated separately in the proofs of Theorems 3.6.2 and 3.6.3.
So the orbits of $\Orth(T_\Co)$ on primitive vectors of given square and divisibility are read off the discriminant form.
The open questions below concern the stable group $\Gamma_\Co$, which acts trivially on $A_{T_\Co}$; the discriminant form separates its orbits (@prop:coble-stable-cusp-lower-bound) and does not count them.
:::

::: {.remark title="Open problem: explicit primitive embedding matrices"}

The chain of primitive embeddings
$$
T_\Co \injects \ten \injects \tdp \injects \lkt
$$
is used throughout (@lem:sequence_of_embeddings; @lem:primitive_embedding_eta), and Nikulin's apparatus [@Nik80 Prop. 1.14.4, 1.15.2] is the intended tool for the uniqueness of the primitive embedding $T_\Co \injects \ten$ and for the surjectivity of $\Orth(L) \to \Orth(T_\Co)$.
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
and whose action on roots induces the *horizontal folding* of the $(18,0,0)_1$ Coxeter diagram, as an immediate consequence of the lattice isometry (cf. @def:folded-root, @lem:root-folding-tdp, and @def:invariant_coinvariant_lattices). The involution should swap the polarization generators between sectors, $h_\En \leftrightarrow h_\Co$.
Existence and the eigenlattice description are settled by @prop:theta-co-exists: the pair $(-\id_{S_\Co}, \id_{T_\Co})$ preserves the gluing graph of the Coble primitive embedding and extends to an isometry $\theta_\Co$ of $\lkt$ with the stated eigenlattices. The open technical content is to *write down the $22\times 22$ matrix of $\theta_\Co$ on the standard basis of $U^{3}\oplus E_8^{2}$*, which requires exhibiting the primitive embedding and the gluing anti-isometry in coordinates, and then to compare the polarization classes and the roots of the Coxeter diagram in that basis.
:::

## Isotropic orbits, cusps, and reflection groups

::: {.question title="Open problem: enumeration of isotropic orbits by Sterk's technique"}

How many orbits of primitive isotropic vectors does $T_\Co$ have under the arithmetic group $\Gamma_\Co = \Orth^+(T_\Co)^*$?
The discriminant kernel $\discriminantkernel{T_\Co}$ is larger, $\Gamma_\Co$ being its component-preserving half of index $2$, and it has the *same* orbits: @prop:discriminant-kernel-orbits. So this is one question and not two, and the group-theoretic difference between the kernel and the stable group does not appear in the count.
The index alone would not have given that, and the first version of this item drew the wrong conclusion from it: whether two groups' orbit partitions agree is decided orbit by orbit, through their stabilizers, by @lem:character-kernel-orbits.
What is settled is the lower end: for $\Orth^+(T_\Co)$ the count is one (@thm:unpolarized-cusps); for $\Gamma_\Co$, and so for the kernel, it is at least $527$, one orbit for each nonzero isotropic class of $A_{T_\Co}$ (@prop:coble-stable-cusp-lower-bound, whose argument uses only triviality on $A_{T_\Co}$ and so applies to the kernel as well).
Nothing here gives an upper bound, and $\fco$ has at least $527$ $0$-cusps rather than one.
Sterk's technique [@Ste91] determines these by analyzing the orbits of the images (lifts) in the discriminant group $A_{T_\Co} \cong (\ZZ/2\ZZ)^{11}$ under $\Orth(q_{T_\Co})$: for an even indefinite $2$-elementary lattice $T$ with both signature indices nonzero the genus contains a unique class (@thm:two-elementary-classification) and $\Orth(T) \to \Orth(q_T)$ is surjective (@thm:two-elementary-surjectivity), so a primitive isotropic vector $v$ with $\div(v)=d$ is determined up to $\Orth(T)$ by the tuple $(\div(v),\, \bar v \in A_T,\, v^2 = 0)$.
The finite half is settled by @prop:coble-q-fibers and @thm:coble-isotropic-class-orbits: $A_{T_\Co}$ has $528$ isotropic classes, and $\Orth(q_{T_\Co})$ has two orbits of sizes $1$ and $527$. By @prop:coble-primitive-isotropic-classes every primitive isotropic vector of $T_\Co$ maps to the nonzero orbit. Under the degree-$2$ Enriques group, @thm:coble-heegner-finite-orbits gives the refinement $[1, 2, 120, 135, 270]$. The open work is the passage from these finite decompositions back to the lattice:

- lift the $\Orth(q_{T_\Co})$-orbits to $T_\Co$ and determine how many $\Gamma_\Co$-orbits lie in divisibility $2$ — the same number as for the discriminant kernel, by @prop:discriminant-kernel-orbits; there are at least $527$, and the count is exactly $527$ when the stabilizer of a primitive isotropic vector in $\Orth(T_\Co)$ maps onto the stabilizer of its class in $\Orth(q_{T_\Co})$ (@prop:coble-stable-cusp-lower-bound), so the finite picture, in which the primitive isotropic vectors map onto the single nonzero orbit, does not lift to a single orbit. The Eichler criterion is unavailable here because $T_\Co$ contains no copy of $U$ (the Eichler criterion (@thm:eichler-criterion) and the remark following it);

- decide whether the four nonzero orbits of $\gent$-induced classes lift to four orbits of primitive isotropic vectors or to more, an integral parabolic stabilizer being permitted to have proper image in the finite one;

- count the $\Gamma_\Co$-orbits themselves, and decide which of them carry the Coble stable limits. The $\Orth(T)$-orbits do not coincide with the $\Gamma_\Co$-orbits (@lem:stable-orthogonal-not-transitive), so the uniqueness of the Baily--Borel $0$-cusp fails for the arithmetic group of $\fco$; what is open is the decomposition, not whether it is trivial.

By @lem:divisibilityAlwaysTwoTco, every primitive isotropic $v \in T_\Co$ has $\div_{T_\Co}(v) = 2$; this fixes the divisibility datum but not the orbit count.
:::

::: {.remark title="Open problem: explicit generators of $\Gamma_\Co$ and uniqueness of the 1-cusp"}

The Coble-side description of the arithmetic group is the centralizer of the horizontal folding involution, cut by the polarization.
That centralizer cannot be taken inside $\Orth(\ten)$: the polarization $h_\Co\in K_S^{\perp\Pic(S)}\iscontainedin\Pic(S)$ is a class on the Coble surface, of square $2$, with K3 pullback $\tilde h_\Co = f^{*}h_\Co$ of square $4$ (@def:coble-polarization-classes), and $\theta_\Co$ is an isometry of $\lkt$, so the group has to be formed in $\Orth(\lkt)$ and then pushed to $T_\Co$.
With $\theta_\Co$ the sign involution of @prop:theta-co-exists, whose eigenspaces are $T_\Co$ and $S_\Co$, the group is
$$
\Gamma^\theta_\Co \definedas
\theset{\;
\varphi\in\Orth^+(T_\Co)
\;\middle|\;
\exists\, g\in Z_{\Orth(\lkt)}(\theta_\Co)\intersect\Stab_{\Orth(\lkt)}(\tilde h_\Co)
\ \text{with}\ \restrictionof{g}{T_\Co} = \varphi
\;}
,
$$
the part of the image of that intersection lying in $\Orth^+(T_\Co)$, which is the group of @prop:gamma-co-in-theta-centralizer; the component condition is imposed there because the intersection may contain isometries acting on the wrong component of $T_\Co$.
An earlier version of this item placed both operations inside $\Orth(\ten)$, where neither object lives.
The class $h_\Co$ is not the hyperplane class $H$, whose K3 pullback $e_0 = f^{*}H$ has square $2$; the two must be kept apart, and it is $h_\Co$ that is the analogue of the Enriques vector $h_\En = e + f\in U(2)$ of @prop:gamma-en-two-gluing.
$\Gamma^\theta_\Co$ contains $\Gamma_\Co$, and by @prop:gamma-co-in-theta-centralizer $\Gamma_\Co$ is exactly the kernel of its action on $A_{T_\Co}$; the inclusion is *strict*, and its index is known exactly. By @prop:gamma-co-two-definitions the two groups agree exactly when $\rho_{T_\Co}(\Gamma^\theta_\Co)$, a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$, is trivial, and @prop:theta-co-gluing identifies that image with the $\gamma_\Co$-transport of the image of $\Stab_{\Orth(S_\Co)}(\tilde h_\Co)$; that image is nontrivial (@lem:coble-stabilizer-discriminant-nontrivial, whose witness is the reflection $s_v$ in $v = u-w$ for $\tilde h_\Co = u+w$) and its order is $\abs{W(E_8)}$, so $[\Gamma^\theta_\Co:\Gamma_\Co] = 696\,729\,600$ by @prop:theta-co-index. The Enriques side is decided the same way: @lem:polarization-stabilizer-discriminant-nontrivial exhibits a reflection of $S_\En$ fixing $h$ and moving the class of $u_0/2$, and @prop:gamma-co-heegner-strict transports it — through the surjectivity of the discriminant representation for a $2$-elementary lattice, @thm:two-elementary-surjectivity — to an element of $\Stab_{\gent}(\ZZ\delta)$ with nontrivial image, so the Heegner description is strictly larger than $\Gamma_\Co$, with the same index $\abs{W(E_8)} = 696\,729\,600$. Both candidate overgroups of $\Gamma_\Co$ therefore sit at the same finite index over it, and under block-compatibility of the Heegner gluing, $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$, with the index $\abs{W(E_8)}$ inside $\Orth^+$ and $[\Gamma^{\mathrm{cong}}_{\Co,2}:\Gamma_\Co] = 2\abs{W(E_8)} = 1\,393\,459\,200$ for the full preimage, both unconditional — which reduces item 1 of A20, the comparison recorded as blocked on explicit generators of $\gent$, to that one statement about the gluing. What remains open in @prob:group-identification is not that comparison: it is the comparison with the direct and geometric entries (@prob:coble-rigidity, @prob:B24, @prob:B25), which are not subgroup comparisons inside $\Orth(A_{T_\Co})$ at all, together with the block-compatibility of the two gluings, $\gamma$ and $\gamma_\Co$ — that a gluing anti-isometry carries the $U(2)$ summand to the $U(2)$ summand. That is a statement about a labeled primitive embedding rather than about the abstract pair of discriminant forms, so it is an instance of @prob:coble-rigidity, the same kind of input the comparison at @sec-gamma-co-comparison needs.
A second candidate, defined from the Enriques side by the Heegner line rather than by $\theta$, is $\Gamma_\Co^\En(\delta)$ of @def:gamma-co-en; by @prop:gamma-co-in-heegner-group it too contains $\Gamma_\Co$ as the kernel of its action on $A_{T_\Co}$, and that inclusion is *strict*: cut down to $\Orth^+(T_\Co)$ it is the group @prop:gamma-co-heegner-strict proves strictly larger, with index exactly $\abs{W(E_8)} = 696\,729\,600$.
Comparing the two candidates with *each other*, rather than each with $\Gamma_\Co$, requires an isometry of $\lkt$ carrying the Coble-labeled structure to the Enriques-labeled one, which is @prob:coble-rigidity: both are extensions of the same $\Gamma_\Co$ by subgroups of the finite group $\Orth(A_{T_\Co},q_{T_\Co})$, and it is those finite subgroups that such an isometry would have to match (@sec-gamma-co-comparison).
An explicit representation of $\Gamma_\Co$ by *matrix generators* is presently a stub.
The open work is to:

- compute the stabilizer/centralizer intersection to produce a minimal set of matrix generators for the group above. The Enriques-side half is now settled: the reflections in $u_0-w_0$ and in the eight simple roots of $E_8(-1)$ generate the integral stabilizer $\Stab_{\Orth(S_\En)}(h)$, completeness decided by the owner's own subgroup comparison against $\abs{\Orth(h^{\perp C})} = 2\abs{W(E_8)}$, and their discriminant images generate the group of order $\abs{W(E_8)}$ that @thm:coble-heegner-finite-orbits (1) names, through `computations/reports/coble_stabilizer_generators.py`. What remains is (i) the corresponding finite image for the Coble-side group $\Gamma^\theta_\Co$, which has not been computed, so the two finite subgroups still have to be compared, and (ii) generators of $\Gamma_\Co$ itself. The reflective set of $\Gamma_\Co$ is now decided rather than exemplified: @prop:gamma-co-reflective-set shows that *every* short root of $T_\Co$ has its reflection in $\Gamma_\Co$, that no vector of positive square does, and that *no* long root does either — for $v^2 = -4$ the reflection is $x + b_B(x,v)v$ in the coordinates of the unimodular $B$, and some $x$ has $b_B(x,v) = 1$, so $s_v\not\equiv\id\bmod 2$ — so the reflective set is exactly the short roots. What is not settled is the index $[\Gamma_\Co : W(T_\Co)]$ of the group they generate; the formulation "this set with finitely many further isometries generates $\Gamma_\Co$" carries nothing, since $\Gamma_\Co$ is finitely generated as an arithmetic subgroup. The owner's contracts bound what can be concluded here: `Lattices.roots()` is the definite-lattice root set and refuses an indefinite lattice by contract, so its refusal is not evidence about the $(-2)$-vectors of $T_\Co$; `reflective_root_locus` is documented as possibly infinite for an indefinite lattice; `possible_root_lengths()` returns $\{1,2,4\}$; and `root_module_generating_set()` is a semi-decision for $L = \ZZ\Phi(L)$, which concerns the module the roots generate and not $\Orth^+(L)$ being generated by reflections. Nor is the route the research report names available for $T_\Co$ itself: Vinberg's algorithm is a statement about hyperbolic lattices, the owner accepts signature $(1,n)$ or $(n,1)$ only and refuses $T_\Co$ on its signature $(2,9)$, so what remains is the reflective-lattice question in signature $(2,9)$ and the cusp lattices are where the hyperbolic statement belongs. The remaining half — a theorem that the reflective set with finitely many further isometries generates $\Gamma_\Co$ — is recorded as open in the research report, and the computed state, including the runtime obstruction to any owner computation of it, is `computations/reports/coble_gamma_co_reflective_set.py` and `computations/reports/coble_owner_gap-blockers-20261105.md`;

- determine the $\Gamma_\Co$-orbits of primitive isotropic *planes*, and with them the $1$-cusps of $\fco$. For the full orthogonal group the transitivity is now a theorem of this book rather than a citation: @thm:plane-transitivity-tco proves that $\Orth^+(T_\Co)$ acts transitively on primitive isotropic planes, by splitting the unimodular model $B=\latI_{2,9}=\latI_{1,1}\perp\latI_{1,8}$ at a line and lifting isometries of the quotient as $\id\perp\varphi$ with the component read off @def:period-component-character. The boundary lattice of the exhibited plane is computed at the owner as well: $J^{\perp T_\Co}/J$ has rank $7$, signature $(0,7)$, determinant $-2^7$ and type $(7,7,1)$, i.e. $\latI_{0,7}(2)\cong A_1^{\oplus 7}$, in `computations/reports/one_cusp_plane_quotient.py`.
  The residue is the subgroup statement, which does not follow from the full-group one. What the earlier version of this item got wrong is that it declared a plane to have no discriminant invariant, on the ground that "a plane is not an element of $T_\Co$". The invariant exists, and the first repair of this item then named the wrong object: a plane's datum is not the dual of its restricted form, nor the *type* of anything, but the subspace
  $$\bar J \;=\; (T_\Co^\vee\cap J_\QQ)/J \;\subset\; A_{T_\Co},$$
  which under $A_{T_\Co}\cong T_\Co/2T_\Co\cong B/2B$ is simply the image of $J$, a two-dimensional totally isotropic subspace, and which is computed for the exhibited planes in `computations/reports/plane_gluing_subgroup.py`. It is $(\ZZ/2)^2$ with zero pairing for *every* primitive isotropic plane, by @thm:plane-transitivity-tco, so its isomorphism type is an isometry invariant and carries no information; the subspace itself does, because $\Gamma_\Co$ acts trivially on $A_{T_\Co}$ and an isometry does not: $\overline{g(J)} = g(\bar J)$. This is the plane analogue of $v\mapsto v^*$ for lines and it gives the same kind of lower bound, the number of $\Gamma_\Co$-orbits of planes being at least the number of subspaces attained; $A_{T_\Co}$ has $23\,715$ two-dimensional totally isotropic subspaces, so the invariant is very far from constant, and whether it separates is what remains open. Whether $\fco$ has one $1$-cusp or several is open with it, as is the $\Gamma_\Co$-orbit of the two exhibited planes, which would be decided by comparing their subspaces in one presentation of $T_\Co$.

This refines, at the level of orbits and generators, the $1$-cusp correspondence $(7,7,1)_0 \mapsto (8,6,0)_0$ established in @lem:1_cusp_correspondence.
:::

::: {.remark title="The maximal parabolic subdiagrams of $S_\Co$, and what they count"}

By @thm:coble-picard-parabolics, the Coxeter diagram $\Gamma_r$ of $S_\Co = (11,11,1)_1$ has $12$ roots, trivial automorphism group, and two maximal parabolic subdiagrams, $\wE_8(2)\wA_1$ and $\wB_9(2)$, both of even ordinary type. By @thm:parabolic-isotropic-correspondence these correspond to the two $\Orth^+(S_\Co)$-orbits of primitive isotropic vectors in $S_\Co$, and by @thm:isotropic-trichotomy both quotients $v^{\perp S_\Co}/v$ have invariants $(9,9,1)$, so the two orbits are not separated by the invariants of the boundary lattice.

By @thm:elliptic-fibrations-isotropic these orbits are elliptic fibrations of the K3 cover; they are not the $0$-cusps of the Coble period space, which are the orbits of primitive isotropic vectors in the transcendental lattice $T_\Co$ of signature $(2,9)$.
By @thm:unpolarized-cusps and @prop:tco-split-maximal, the latter form exactly one orbit under the full orthogonal group.
The two lattices share the invariant triple $(11,11,1)$ but not the signature, and a count taken in one is not a count in the other.

What remains open is the geometric identification: which of the two elliptic fibration classes of the K3 cover is distinguished by the Coble structure, and how the pair of maximal parabolic subdiagrams matches the boundary data of the degree-$2$ polarized moduli space.
:::

::: {.question title="Open problem: the reflection group of each Sterk fundamental domain"}

Sterk's published fundamental domains for the five cusps of $\fentwo$ have $12, 10, 12, 11, 14$ walls [@Ste91], while Vinberg's algorithm applied to the corresponding hyperbolic quotients $\eta_j^{\perp\ten}/\eta_j$ returns ten walls in each case.
The quotients for $j = 2,3,4,5$ are mutually isometric, so their full Weyl groups are conjugate and cannot account for four inequivalent published diagrams.
The open work is to identify, for each $j$, the reflection subgroup $W_j\leq W(\eta_j^{\perp\ten}/\eta_j)$ for which the published diagram bounds a fundamental domain, to exhibit that domain as a union of chambers of the full group, and to determine the index $[W(\eta_j^{\perp\ten}/\eta_j) : W_j]$ as a covolume ratio.
Cusp $2$, to which the Coble $0$-cusp is claimed to correspond, is the case in which the two computations agree.
The data and the derivation are in [Sterk's simple-root counts and the computed Vinberg chambers](#sec-sterk-root-counts-and-computed-chambers).
:::

::: {.remark title="Open problem: hyperbolic-quotient derivation of the cusp correspondence"}

The cusp correspondence between the Coble cusps $(9,9,1)$, $(7,7,1)$ and their Enriques predecessors is established in @thm:cusp_correspondence using @lem:w1_perp_calculation and @lem:1_cusp_correspondence. An independent *hyperbolic-quotient* derivation would place the correspondence on a self-contained lattice footing rather than resting on the alignment of invariants:

- compute the isometry type of the hyperbolic quotient $e^{\perp T_\Co}/e$ directly for a primitive isotropic $e \in T_\Co$;

- use $\div_{T_\Co}(e)$ to pin down the unique $\Orth(T_\Co)$-orbit and verify that the quotient matches the Enriques signatures $(10,8,0)_1$ for $0$-cusps and $(8,6,0)_0$ for $1$-cusps.

The residue that is genuinely open is the *orbit-uniqueness input*: the proof of the divisibility lemma used there (@lem:divisibilityTcoOne) presently *assumes* a unique $\Gamma_\Co$-orbit of isotropic vectors in $T_\Co$, which is exactly the enumeration left open above.
:::

### General questions on hyperbolic reflection groups

The entries above ask for specific subdiagram and orbit computations in the Coble and Enriques lattices.
The following are the corresponding questions asked of hyperbolic Coxeter diagrams in general; each is open, and each bears on how far the specific computations can be pushed.

::: {.question #qst:maximal-parabolic-complexity title="Open problem: the cost of enumerating maximal parabolic subdiagrams"}

Given a Coxeter--Vinberg diagram $\Sigma$ on $n$ vertices, what is the cost of determining its maximal parabolic subdiagrams, equivalently the ideal vertices of the chamber (the ideal-vertices/parabolic corollary (@cor:ideal-vertices-are-parabolic))?

Enumerating the $2^{n}$ subsets is an upper bound, and the subdiagram-inheritance corollary (@cor:subdiagram-inheritance) prunes it: a subset that fails to be elliptic can be discarded together with every subset containing it, so the search runs over the order ideal of elliptic subsets.
No lower bound is known, and no polynomial-time algorithm is known even for the decision problem asked of the whole diagram:

- decide whether a given hyperbolic Coxeter diagram has finite covolume by @thm:coxeter-polytope-volume without enumerating its maximal parabolic subdiagrams;

- exhibit a family of diagrams on which the elliptic order ideal is of exponential size, or show that it is polynomial for the diagrams of finite-covolume groups.

The concrete instance in this monograph is the uniqueness of $\wB_7(2)$ as a maximal parabolic subdiagram of the ten-node diagram $G_{S_\Co}$, stated above; the general question is whether such uniqueness claims admit an argument short of the subdiagram search.
:::

::: {.conjecture #conj:galois-invariance-parabolics title="Open problem: Galois invariance of the maximal parabolic count"}

Let $\Sigma$ be a Coxeter--Vinberg diagram whose Gram form is defined over a totally real number field $K$, and let $\sigma\in\gal(K/\QQ)$.
The conjecture is that $\Sigma$ and its conjugate $\sigma(\Sigma)$ have the same number of maximal parabolic subdiagrams.

By the Galois-conjugate Gram-form remark (@rmk:galois-conjugate-gram-form) the signature of $\sigma(G)$ is not determined by that of $G$, so the conjugate diagram need not be hyperbolic at all and the statement requires the hypothesis that it is.
The open work is to determine the action of $\gal(K/\QQ)$ on the set of maximal parabolic subdiagrams --- whether it permutes them, and if so with what orbits.
The diagrams of this monograph have Gram field $\QQ$ or $\QQ(\sqrt2)$, the latter arising from the $m_{ij} = 4$ bonds of the $B$-type diagrams, so the smallest instance is the nontrivial automorphism of $\QQ(\sqrt2)$ acting on the folded Sterk diagrams.
:::

::: {.question #qst:parabolic-count-growth title="Open problem: growth of the maximal parabolic count with the rank"}

How does the number of maximal parabolic subdiagrams of a hyperbolic Coxeter diagram grow with its rank $n$?

Is there a bound, exponential or otherwise, valid for all diagrams of rank $n$, and does the finite-covolume condition of @thm:coxeter-polytope-volume improve it?
The recorded data for this monograph is the count of vertices at infinity in the CoxIter runs on the five folded Sterk diagrams and the three $0$-cusp lattices, all of rank $9$ or $10$; a family of increasing rank is needed before a growth statement can be made.
:::

::: {.question #qst:arithmeticity title="Open problem: which finite-covolume reflection groups are arithmetic"}

Which finite-covolume hyperbolic Coxeter groups are arithmetic?

The datum available from the diagram is the Gram form over its base field $K$ of @def:coxeter-base-field together with its Galois conjugates from @rmk:galois-conjugate-gram-form. The open work is to decide arithmeticity from that datum, and to determine how the property interacts with the maximal parabolic structure of the diagram.
The reflection groups appearing in this monograph act on lattices defined over $\ZZ$, so they are arithmetic; the question governs whether the techniques used here extend to the non-crystallographic base-ring examples (@ex:noncrystallographic-base-rings).
:::

::: {.question #qst:exact-covolume title="Open problem: exact covolumes of hyperbolic Coxeter polytopes"}

Compute $\vol(P)$ exactly for a hyperbolic Coxeter polytope $P$ given by its diagram, with $\vol(P)$ as in @def:covolume.

In even dimension the volume is a rational multiple of the Euler characteristic and is computable from the diagram; in odd dimension the Euler characteristic vanishes and supplies no information, which is the case for every nine-dimensional chamber recorded in the Computations section.
The open work is:

- closed-form volume formulas for specific families, through Schläfli's volume differential or through polylogarithmic values;

- the relation between $\vol(P)$ and the maximal parabolic structure of $\Sigma$;

- a covolume computation sharp enough to decide the index $[W : W_j]$ of a reflection subgroup, which is the quantity that would settle the discrepancy between Sterk's published fundamental domains and the computed Vinberg chambers.
:::

::: {.question #qst:regularized-theta title="Open problem: theta series of indefinite lattices"}

For a positive-definite lattice the theta series $\theta_L(q) = \Sum_{v\in L} q^{v^2/2}$ converges and is a modular form.
For an indefinite lattice the set of vectors of square $k$ can be infinite (see the Lattice Theory section), the series does not converge, and a regularization is required before any modular statement can be made.

The open work is to define a regularized theta series for the hyperbolic lattices of this monograph, determine its transformation behaviour, and relate it to the lattice invariants --- discriminant form, genus, and the reflection group --- that the rest of this document computes.
:::

## The GIT and Looijenga models of the Coble moduli space

::: {.question #qst:coble-arrangement-empty title="Open problem: is the Coble arrangement $\mch^{*}_{10A_1}$ empty?"}

The GIT compactification of the moduli of ten-nodal sextics is the Looijenga compactification of $\Gamma_{10A_1}\backslash(D(T_\Co) - \mch^{*}_{10A_1})$, for the arrangement
$$
\mch^{*}_{10A_1} = \mch_\infty \intersect D(T_\Co)
$$
cut out by the divisibility-two roots of $\Lambda_1 = H^{\perp\lkt}$ by @thm:git-equals-looijenga. Whether that arrangement is empty decides the shape of the compactification:

- if $\mch^{*}_{10A_1} = \varnothing$, @def:looijenga-compactification returns the Baily--Borel compactification, so the GIT boundary of the ten-nodal sextics consists of the $0$-cusp point and the $1$-cusp curve and nothing else;

- if $\mch^{*}_{10A_1} \neq \varnothing$, the GIT compactification carries a boundary divisor for each $\Gamma_{10A_1}$-orbit in the arrangement, and is a proper semitoroidal model strictly between Baily--Borel and toroidal.

The question is a lattice computation in $\Lambda_1$: is there a divisibility-two root of $\Lambda_1$ whose orthogonal hyperplane meets $D(T_\Co)$ in a proper hyperplane section?
@lem:divisibilityAlwaysTwoTco computes divisibility inside $T_\Co$; the remaining question is divisibility inside the larger lattice $\Lambda_1$.
One reduction is available: every root of the root lattice $L$ has divisibility $1$ in $\Lambda_1$ [@YZZ25 §4.2], so no root arising from a node of the sextic contributes, which is why $\mch^{*}_{10A_1}$ is contained in the larger arrangement $\mch_{10A_1}$ of @thm:occult-period-map-sextics.
:::

::: {.question #qst:semifan-poset-position title="Open problem: the position of the three semifans"}

The Coxeter, KSBA, and Looijenga semifans of the Coble period domain arise from distinct inputs; @def:looijenga-compactification and the following remark record the Looijenga input.
Once $\mch^{*}_{10A_1}$ is computed, three questions remain:

- is the resulting Looijenga semifan the Coxeter semifan of a reflection group, as it would be if the traces of $\mch^{*}_{10A_1}$ on a cusp boundary were the walls of a chamber?

- does the Looijenga semifan refine the KSBA semifan, coarsen it, or is it incomparable?

- which sextic degenerations lie over which cusp?
  Shah's classification of the semistable sextics is explicit [@Sha80], and @thm:cusp_correspondence gives the cusp correspondence, so tracing a named degeneration such as a double cubic to the $0$-cusp $(9,9,1)_1$ or the $1$-cusp $(7,7,1)_0$ is a finite computation.
:::

## dlt and KSBA stable models

::: {.remark title="Open problem: Coble-specific dlt models and pot geometry"}

The degree-$2$ Enriques program modernizes Morrison's flowerpots [@Mor81] into *dlt* stable pairs, but the *Coble-specific dlt models* are not yet detailed.
The open geometric content is:

- **Coble pot geometry.** Define the explicit stable pair $(\mcv, \mcd)$ whose "Pot" component is a rational Coble surface, carrying a $\tfrac14(1,1)$ cyclic quotient singularity corresponding to the nodes of the rational sextic $C$.
  This is the local singularity package conjectured for the stable quotient in @conj:coble_quarter_singularity, seen here on the *dlt* model (cf. @def:dlt-involution-pair and @def:coble-divisor-model).

- **Stalk assembly.** Describe the transition of the stalk assembly and the integral-affine configuration as the Enriques surface log-collapses onto the discriminant divisor $\Delta$, where the K3 cover becomes nodal.
:::

::: {.remark title="Open problem: monodromy invariants and stable models $B(\lambda)$"}

Stable limits of Coble surfaces arise as $S_2$-quotients of nodal K3 surfaces, parameterized by a monodromy invariant $\ell \in \check{\mch}$ (surgery sizes) through the construction $B(\lambda)$ of [@AEGS25].
The open work is to:

- determine the map from the Coble polarization to the discretization $\ell$ on the dual complex.
  The surgery sizes are the pairings $\ell_i = h\cdot\alpha_i$ against the roots $\alpha_i$ of the relevant Coxeter diagram, so the first step is to record which polarization class is meant and in which lattice the pairing is taken: the downstairs class $h_\Co\in K_S^{\perp\Pic(S)}$ or its K3 pullback $\tilde h_\Co\in S_\Co$, as in @def:coble-polarization-classes, the roots living in the lattice of the chosen cusp.
  An orthogonal direct-sum presentation on its own does not make $\ell = 0$;

- verify the slc stability of the resulting stable pair $(Z, \eps C)$ for specific surgery vectors $\ell$.

This is the discrete-datum side of the KSBA program whose stability obligations are recorded in the quarter-singularity conjecture (@conj:coble_quarter_singularity) and the surrounding KSBA discussion.
:::

## Foundational equations and computational verification

::: {.remark title="Open problem: explicit equations for the Coble curve and its K3 cover"}

A Coble surface $S$ is the blowup of $\PP^2$ at the ten $A_1$ nodes of an irreducible rational plane sextic
$$
C = \theset{ F(x,y,z) = 0 },
\qquad
F(x,y,z) = \Sum_{i+j+k=6} a_{ijk}\, x^i y^j z^k,
$$
subject to the nodal conditions $F(p_m) = \del_x F(p_m) = \del_y F(p_m) = \del_z F(p_m) = 0$ at the ten special positions $p_1,\dots,p_{10} \in \PP^2$; the moduli space of such sextics is $9$-dimensional, and explicit models may be sought from the Steiner sextic or from index-$2$ Halphen pencils (cf. @lem:coble_halphen_blowdown and @lem:rational_sextic_ten_nodes). The K3 cover is the double cover $X \xrightarrow{2:1} S$ of $\PP^2$ branched along $C$, with equation $w^2 = F(x,y,z)$ in $\PP(1,1,1,3)$, whose ten $A_1$ nodes lie above the positions $p_m$ (at $w = 0$, $[x:y:z] = p_m$). What is missing is a *worked instance*: derive an explicit equation $F(x,y,z) = 0$ for a rational sextic with ten nodes together with the corresponding cover $w^2 = F$, realizing $C$ as the image of $\PP^1$ under a degree-$6$ map $(s:t) \mapsto [f_0 : f_1 : f_2]$.
Such an instance would anchor the coordinate derivations demanded by the lattice-embedding and involution problems above.
:::

::: {.remark title="Lattice and orbit anchors for the computations"}

The problems above share a small set of concrete starting data, recorded here for reference:

- **Isotropic vectors.** In $S_\Co$, primitive isotropic lines are represented by $v = e_0 \pm e_i$ (with $e_0^2 = 2$, $e_i^2 = -2$).

- **Polarization basis.** The degree-$2$ polarization is $h = e + f\in U(2) = \sdp\iscontainedin \sen$, with $e\cdot f = 2$ and $h^2 = 4$ (the discriminant description of $\gent$ (@prop:gamma-en-two-gluing)); it lies in the invariant lattice, not in $\ten$, and must be identified in a basis compatible with $\theta$.

- **Heegner line.** By @lem:coble-heegner-vector, the complement realizing $T_\Co$ inside $\ten$ is $\delta^{\perp\ten}$ for $\delta = u - w$ in the unimodular $U$ summand; by @thm:coble-heegner-line-unique, this line is unique up to $\gent$.

- **Discriminant forms.** $q_{S_\Co} \colon (\bF_2)^{11} \to \QQ/2\ZZ$ and $q_{T_\Co} \colon (\bF_2)^{11} \to \QQ/2\ZZ$, with isometry of complements forcing $q_{S_\Co} = -q_{T_\Co} \bmod 2\ZZ$.

- **Sterk orbit lift.** For the $2$-elementary $T_\Co$, an orbit is determined by the tuple $(\div(v),\, \bar v \in A_{T_\Co},\, v^2 = 0)$, reducing the search to $\bF_2$-vector-space orbits under $\Orth(q_{T_\Co})$.

- **$\Gamma_\Co$ generators.** Not known; the matrix representation is a stub. What is known is the reflective part: by @prop:gamma-co-reflective-set the reflections in the short roots of $T_\Co$ all lie in $\Gamma_\Co$ and no long root does, so the reflective set is exactly the short roots; what is open is the index $[\Gamma_\Co : W(T_\Co)]$. The candidate description of the whole group is the image in $\Orth^+(T_\Co)$ of the intersection of the reflection group $W(T)$ with the centralizer $Z(\theta_\Co)$ and with the stabilizer of the primitive vector $\tilde h_\Co = f^{*}h_\Co$, of square $4$ (@prop:gamma-co-in-theta-centralizer), whose eigenspace formulation is the one that can be written down at present.
:::
