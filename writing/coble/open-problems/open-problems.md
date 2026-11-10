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
The open questions below concern the stable group $\widetilde\Orth^+(T_\Co)$, which acts trivially on $A_{T_\Co}$; the discriminant form separates its orbits on lines and counts them (@prop:coble-cusp-count).
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

How many orbits of primitive isotropic vectors does $T_\Co$ have under the arithmetic group $\widetilde\Orth^+(T_\Co)$?
The discriminant kernel $\discriminantkernel{T_\Co}$ is larger, $\widetilde\Orth^+(T_\Co)$ being its component-preserving half of index $2$, and it has the *same* orbits: @prop:discriminant-kernel-orbits. So this is one question and not two, and the group-theoretic difference between the kernel and the stable group does not appear in the count.
The index alone would not have given that, and the first version of this item drew the wrong conclusion from it: whether two groups' orbit partitions agree is decided orbit by orbit, through their stabilizers, by @lem:character-kernel-orbits.
What is settled is the whole count: for $\Orth^+(T_\Co)$ it is one (@thm:unpolarized-cusps), and for $\widetilde\Orth^+(T_\Co)$, and so for the kernel, it is $527$, one orbit for each nonzero isotropic class of $A_{T_\Co}$ (@prop:coble-cusp-count, whose argument uses only triviality on $A_{T_\Co}$ and so applies to the kernel as well). By @sec-cusp-lifting the parabolic stabilizer's image is the whole finite stabilizer, so the $\widetilde\Orth^+(T_\Co)$-orbits of primitive isotropic lines are exactly the $527$ nonzero isotropic classes. Those are the $0$-cusp orbits of the stable quotient and not of $\fco$: $\fco = \bD(T_\Co)/\Gamma_\Co$ with $\Gamma_\Co = \Orth(T_\Co)$ (@prop:gamma-co-images(3)), and its $0$-cusp count is one, by @thm:unpolarized-cusps, computed by sage-extensions#286 in its $\Orth(T_\Co)$ row.
Both numbers are **proved in prose only**: no computation record decides them, and the library call that would is sage-extensions#286.
Sterk's technique [@Ste91] determines these by analyzing the orbits of the images (lifts) in the discriminant group $A_{T_\Co} \cong (\ZZ/2\ZZ)^{11}$ under $\Orth(q_{T_\Co})$: for an even indefinite $2$-elementary lattice $T$ with both signature indices nonzero the genus contains a unique class (@thm:two-elementary-classification) and $\Orth(T) \to \Orth(q_T)$ is surjective (@thm:two-elementary-surjectivity), so a primitive isotropic vector $v$ with $\div(v)=d$ is determined up to $\Orth(T)$ by the tuple $(\div(v),\, \bar v \in A_T,\, v^2 = 0)$.
The finite half is settled by @prop:coble-q-fibers and @thm:coble-isotropic-class-orbits: $A_{T_\Co}$ has $528$ isotropic classes, and $\Orth(q_{T_\Co})$ has two orbits of sizes $1$ and $527$. By @prop:coble-primitive-isotropic-classes every primitive isotropic vector of $T_\Co$ maps to the nonzero orbit. Under the degree-$2$ Enriques group, @thm:coble-heegner-finite-orbits gives the refinement $[1, 2, 120, 135, 270]$. The open work is the passage from these finite decompositions back to the lattice:

- the lifting is done in @sec-cusp-lifting: every nonzero isotropic class lifts, the zero one does not, and the index of the parabolic stabilizer's image is $1$, so the count is exactly $527$; what remains here is not the count — the same number as for the discriminant kernel, by @prop:discriminant-kernel-orbits; there are $527$, proved in prose only with sage-extensions#286 the computation owed — but which of the $527$ carry stable limits; the stabilizer of a primitive isotropic vector in $\Orth(T_\Co)$ maps onto the stabilizer of its class in $\Orth(q_{T_\Co})$, so the finite picture, in which the primitive isotropic vectors map onto the single nonzero orbit, does lift to one orbit per class (@prop:coble-cusp-count). The Eichler criterion is unavailable here because $T_\Co$ contains no copy of $U$ (the Eichler criterion (@thm:eichler-criterion) and the remark following it);

- decide whether the four nonzero orbits of $\gent$-induced classes lift to four orbits of primitive isotropic vectors or to more, an integral parabolic stabilizer being permitted to have proper image in the finite one;

- count the $\widetilde\Orth^+(T_\Co)$-orbits themselves, and decide which of them carry the Coble stable limits. The $\Orth(T)$-orbits do not coincide with the $\widetilde\Orth^+(T_\Co)$-orbits (@lem:stable-orthogonal-not-transitive), so the uniqueness of the Baily--Borel $0$-cusp fails for the arithmetic group of $\fco$, and the decomposition is now known: $\widetilde\Orth^+(T_\Co)$ has $527$ orbits of primitive isotropic lines, one per nonzero isotropic class of $A_{T_\Co}$ (@sec-cusp-lifting). What remains of this item is which of them carry the Coble stable limits, not the count.

By @lem:divisibilityAlwaysTwoTco, every primitive isotropic $v \in T_\Co$ has $\div_{T_\Co}(v) = 2$; this fixes the divisibility datum but not the orbit count.
:::

::: {.remark title="Open problem: explicit generators of $\widetilde\Orth^+(T_\Co)$ and uniqueness of the 1-cusp"}

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
$\Gamma^\theta_\Co$ contains $\widetilde\Orth^+(T_\Co)$, and by @prop:gamma-co-in-theta-centralizer $\widetilde\Orth^+(T_\Co)$ is exactly the kernel of its action on $A_{T_\Co}$; the inclusion is *strict*, and its index is known exactly. By @prop:gamma-co-two-definitions the two groups agree exactly when $\rho_{T_\Co}(\Gamma^\theta_\Co)$, a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$, is trivial, and @prop:theta-co-gluing identifies that image with the $\gamma_\Co$-transport of the image of $\Stab_{\Orth(S_\Co)}(\tilde h_\Co)$; that image is nontrivial (@lem:coble-stabilizer-discriminant-nontrivial, whose witness is the reflection $s_v$ in $v = u-w$ for $\tilde h_\Co = u+w$) and its order is $\abs{W(E_8)}$, so $[\Gamma^\theta_\Co:\widetilde\Orth^+(T_\Co)] = 696\,729\,600$ by @prop:theta-co-index. The Enriques side is decided the same way: @lem:polarization-stabilizer-discriminant-nontrivial exhibits a reflection of $S_\En$ fixing $h$ and moving the class of $u_0/2$, and @prop:gamma-co-heegner-strict transports it — through the surjectivity of the discriminant representation for a $2$-elementary lattice, @thm:two-elementary-surjectivity — to an element of $\Stab_{\gent}(\ZZ\delta)$ with nontrivial image, so the Heegner description is strictly larger than $\widetilde\Orth^+(T_\Co)$, with the same index $\abs{W(E_8)} = 696\,729\,600$. Both candidate overgroups of $\widetilde\Orth^+(T_\Co)$ therefore sit at the same finite index over it, and under block-compatibility of the Heegner gluing, $\Gamma^{\mathrm{Hdg}}_\Co = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$, with the index $\abs{W(E_8)}$ inside $\Orth^+$ and $[\Gamma^{\mathrm{cong}}_{\Co,2}:\widetilde\Orth^+(T_\Co)] = 2\abs{W(E_8)} = 1\,393\,459\,200$ for the full preimage, both unconditional — which reduces item 1 of A20, the comparison recorded as blocked on explicit generators of $\gent$, to that one statement about the gluing. What remains open in @prob:group-identification is not that comparison: it is the comparison with the direct and geometric entries (@prob:coble-rigidity, @prob:B24, @prob:B25), which are not subgroup comparisons inside $\Orth(A_{T_\Co})$ at all, together with the block-compatibility of the two gluings, $\gamma$ and $\gamma_\Co$ — that a gluing anti-isometry carries the $U(2)$ summand to the $U(2)$ summand. That is a statement about a labeled primitive embedding rather than about the abstract pair of discriminant forms, so it is an instance of @prob:coble-rigidity, the same kind of input the comparison at @sec-gamma-co-comparison needs.
A second candidate, defined from the Enriques side by the Heegner line rather than by $\theta$, is $\widetilde\Orth^+(T_\Co)^\En(\delta)$ of @def:gamma-co-en; by @prop:gamma-co-in-heegner-group it too contains $\widetilde\Orth^+(T_\Co)$ as the kernel of its action on $A_{T_\Co}$, and that inclusion is *strict*: cut down to $\Orth^+(T_\Co)$ it is the group @prop:gamma-co-heegner-strict proves strictly larger, with index exactly $\abs{W(E_8)} = 696\,729\,600$.
Comparing the two candidates with *each other*, rather than each with $\widetilde\Orth^+(T_\Co)$, requires an isometry of $\lkt$ carrying the Coble-labeled structure to the Enriques-labeled one, which is @prob:coble-rigidity: both are extensions of the same $\widetilde\Orth^+(T_\Co)$ by subgroups of the finite group $\Orth(A_{T_\Co},q_{T_\Co})$, and it is those finite subgroups that such an isometry would have to match (@sec-gamma-co-comparison).
An explicit representation of $\widetilde\Orth^+(T_\Co)$ by *matrix generators* is presently a stub.
The open work is to:

- compute the stabilizer/centralizer intersection to produce a minimal set of matrix generators for the group above. The Enriques-side half is now settled: the reflections in $u_0-w_0$ and in the eight simple roots of $E_8(-1)$ generate the integral stabilizer $\Stab_{\Orth(S_\En)}(h)$, completeness decided by the owner's own subgroup comparison against $\abs{\Orth(h^{\perp C})} = 2\abs{W(E_8)}$, and their discriminant images generate the group of order $\abs{W(E_8)}$ that @thm:coble-heegner-finite-orbits (1) names, through `computations/reports/coble_stabilizer_generators.py`. What remains is (i) the corresponding finite image for the Coble-side group $\Gamma^\theta_\Co$, which has not been computed, so the two finite subgroups still have to be compared, and (ii) generators of $\widetilde\Orth^+(T_\Co)$ itself. The reflective set of $\widetilde\Orth^+(T_\Co)$ is now decided rather than exemplified: @prop:gamma-co-reflective-set shows that *every* short root of $T_\Co$ has its reflection in $\widetilde\Orth^+(T_\Co)$, that no vector of positive square does, and that *no* long root does either — for $v^2 = -4$ the reflection is $x + b_B(x,v)v$ in the coordinates of the unimodular $B$, and some $x$ has $b_B(x,v) = 1$, so $s_v\not\equiv\id\bmod 2$ — so the reflective set is exactly the short roots. What is not settled is the index $[\widetilde\Orth^+(T_\Co) : W(T_\Co)]$ of the group they generate; the formulation "this set with finitely many further isometries generates $\widetilde\Orth^+(T_\Co)$" carries nothing, since $\widetilde\Orth^+(T_\Co)$ is finitely generated as an arithmetic subgroup. The owner's contracts bound what can be concluded here: `Lattices.roots()` is the definite-lattice root set and refuses an indefinite lattice by contract, so its refusal is not evidence about the $(-2)$-vectors of $T_\Co$; `reflective_root_locus` is documented as possibly infinite for an indefinite lattice; `possible_root_lengths()` returns $\{1,2,4\}$; and `root_module_generating_set()` is a semi-decision for $L = \ZZ\Phi(L)$, which concerns the module the roots generate and not $\Orth^+(L)$ being generated by reflections. Nor is the route the research report names available for $T_\Co$ itself: Vinberg's algorithm is a statement about hyperbolic lattices, the owner accepts signature $(1,n)$ or $(n,1)$ only and refuses $T_\Co$ on its signature $(2,9)$, so what remains is the reflective-lattice question in signature $(2,9)$ and the cusp lattices are where the hyperbolic statement belongs. The remaining half — a theorem that the reflective set with finitely many further isometries generates $\widetilde\Orth^+(T_\Co)$ — is recorded as open in the research report, and the computed state, including the runtime obstruction to any owner computation of it, is `computations/reports/coble_gamma_co_reflective_set.py` and `computations/reports/coble_owner_gap-blockers-20261105.md`;

- determine the $\widetilde\Orth^+(T_\Co)$-orbits of primitive isotropic *planes*, and with them the $1$-cusps of the stable quotient; the $1$-cusps of $\fco$ itself are the $\Gamma_\Co$-orbits of planes with $\Gamma_\Co = \Orth(T_\Co)$ (@prop:gamma-co-images(3)), and that count is one, by @thm:plane-transitivity-tco, certified by the same operation. For the full orthogonal group the transitivity is now a theorem of this book rather than a citation: @thm:plane-transitivity-tco proves that $\Orth^+(T_\Co)$ acts transitively on primitive isotropic planes, by splitting the unimodular model $B=\latI_{2,9}=\latI_{1,1}\perp\latI_{1,8}$ at a line and lifting isometries of the quotient as $\id\perp\varphi$ with the component read off @def:period-component-character. The boundary lattice of the exhibited plane is computed at the owner as well: $J^{\perp T_\Co}/J$ has rank $7$, signature $(0,7)$, determinant $-2^7$ and type $(7,7,1)$, i.e. $\latI_{0,7}(2)\cong A_1^{\oplus 7}$, in `computations/reports/one_cusp_plane_quotient.py`.
  The residue is the subgroup statement, which does not follow from the full-group one. What the earlier version of this item got wrong is that it declared a plane to have no discriminant invariant, on the ground that "a plane is not an element of $T_\Co$". The invariant exists, and the first repair of this item then named the wrong object: a plane's datum is not the dual of its restricted form, nor the *type* of anything, but the subspace
  $$\bar J \;=\; (T_\Co^\vee\cap J_\QQ)/J \;\subset\; A_{T_\Co},$$
  which under $A_{T_\Co}\cong T_\Co/2T_\Co\cong B/2B$ is simply the image of $J$, a two-dimensional totally isotropic subspace, and which is computed for the exhibited planes in `computations/reports/plane_gluing_subgroup.py`. It is $(\ZZ/2)^2$ with zero pairing for *every* primitive isotropic plane, by @thm:plane-transitivity-tco, so its isomorphism type is an isometry invariant and carries no information; the subspace itself does, because $\widetilde\Orth^+(T_\Co)$ acts trivially on $A_{T_\Co}$ and an isometry does not: $\overline{g(J)} = g(\bar J)$. This is the plane analogue of $v\mapsto v^*$ for lines and it gives the same kind of lower bound, the number of $\widetilde\Orth^+(T_\Co)$-orbits of planes being at least the number of subspaces attained; $A_{T_\Co}$ has $23\,715$ two-dimensional totally isotropic subspaces, so the invariant is very far from constant, and whether it separates is what remains open. Whether the stable quotient has one $1$-cusp or several is open with it, as is the $\widetilde\Orth^+(T_\Co)$-orbit of the two exhibited planes, which would be decided by comparing their subspaces in one presentation of $T_\Co$; the number of $1$-cusps of $\fco$ is the number of $\Gamma_\Co$-orbits of planes, which is one (@thm:plane-transitivity-tco, certified by sage-extensions#286).

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

The residue that is genuinely open is the *orbit-uniqueness input*: the proof of the divisibility lemma used there (@lem:divisibilityTcoOne) presently *assumes* a unique $\widetilde\Orth^+(T_\Co)$-orbit of isotropic vectors in $T_\Co$, which is exactly the enumeration left open above.
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

- a covolume computation sharp enough to decide the index $[W : W_j]$ of a reflection subgroup. What is settled without it is the group: by [@AEGS25] each published diagram is the folded Enriques diagram $G(\bar T_\dP)^{J_j}$, the diagram of $W(\Gamma_{\En,2,\eta_j})$, and @thm:sterk-reflection-subgroups checks that identification against every root Sterk prints and against his five diagrams' vertex counts. What the covolume would add is the index itself; the chamber as a polyhedron is owed at cusps $1$, $3$ and $4$ (sage-extensions#312, #297).
:::

::: {.question #qst:regularized-theta title="Open problem: theta series of indefinite lattices"}

For a positive-definite lattice the theta series $\theta_L(q) = \Sum_{v\in L} q^{v^2/2}$ converges and is a modular form.
For an indefinite lattice the set of vectors of square $k$ can be infinite (see the Lattice Theory section), the series does not converge, and a regularization is required before any modular statement can be made.

The open work is to define a regularized theta series for the hyperbolic lattices of this monograph, determine its transformation behaviour, and relate it to the lattice invariants --- discriminant form, genus, and the reflection group --- that the rest of this document computes.
:::

## The GIT and Looijenga models of the Coble moduli space

::: {.theorem #thm:coble-arrangement-nonempty title="The Coble arrangement is nonempty, and the GIT compactification is not Baily--Borel"}
For a singular type $T$, write $\overline{\Sigma}_T$ for the Zariski closure of the nodal stratum in $\PP(\operatorname{Sym}^6 V^\vee)$. The arrangement $\mch_T^*$ is empty if and only if $\overline{\Sigma}_T$ contains no cube $Q^3$ of a **smooth** conic $Q$. This is Yu--Zheng's Proposition 3.7 [@YZ23, p. 10], read together with Remark 2.2 [@YZ23, p. 5] and diagram (8) [@YZ23, p. 9].

For $T=10A_1$, the closure contains such a cube, and hence
$$
\mch^{*}_{10A_1} = \mch_\infty \intersect D(T_\Co) \neq \varnothing
.
$$
Consequently the GIT compactification is the proper Looijenga model for this nonempty arrangement, not the Baily--Borel compactification of $\Gamma_{10A_1}\backslash D(T_\Co)$. Its arrangement-indexed boundary divisors are indexed by the $\Gamma_{10A_1}$-orbits on $\mch^{*}_{10A_1}$, whose decomposition is computed in @thm:coble-looijenga-coxeter.
:::

::: {.proof}
**Step 1: the type, its lattices, and its group agree with the period setting in this section.** A singular type $T$ in Yu--Zheng is an irreducible component of $\Sigma_n$, whose members are plane sextics with $n$ distinct nodes ([@YZ23, beginning of §3, p. 5]), and the GIT construction uses its Zariski closure and normalization ([@YZ23, §3.1, p. 6]). For $T=10A_1$, @prop:coble-is-the-ten-nodal-sextic-type gives $P=S_\Co$ and $Q=T_\Co$, with $Q=P^{\perp\lkt}$. Yu--Zheng's period lattice $\Lambda_T$ is the same orthogonal complement, so the arrangement in Proposition 3.7 is the arrangement denoted $\mch^*_{10A_1}$ here. The normalizer description of the arithmetic group agrees with $\Gamma_{10A_1}$: [@YZZ25, Lemma 4.5, p. 13] identifies $\Gamma_W|_Q$ with $\Gamma_T$, and the Weyl group is $\{\pm1\}^{10}$, as recorded after @not:sextic-singular-type. Moreover, [@YZZ25, Lemma 4.8, p. 14] proves that every root of $L$ has divisibility $1$, whereas the roots in $\mch^*_{10A_1}$ have divisibility $2$, so no sextic-node root lies in this arrangement.

**Step 2: the good parametrizations are dense in the space of degree-six nets.** Let $\mathbb G=\operatorname{Gr}(3,H^0(\PP^1,\OO(6)))$, let $B\subset\mathbb G$ be the open subset of base-point-free nets, and let $c\colon B\to\PP(\operatorname{Sym}^6 V^\vee)$ take a net to its image cycle. Let $U\subset B$ consist of the nets for which $\phi_N\colon\PP^1\to\PP^2$ is birational onto its image and that image has only ordinary nodes. This condition is open: at a node with preimage points $p\neq q$, transversality of the two branches makes the two equations $\phi_N(p)=\phi_N(q)$ regular at $(p,q)$, so the node and its two preimage points persist under a small perturbation; properness and compactness exclude new identifications away from these pairs and the diagonal.

Dolgachev places the Winger curve at $(\lambda:\mu)=(27,5)$ in the pencil
$$
\mu(xy+z^2)^3+\lambda z(x^5+y^5+z^5+5x^2y^2z-5xyz^3+z^5)
$$
and, in his coordinates $(x,y,z)=(A_1,A_2,A_0)$, parametrizes it by
$$
[u:v]\longmapsto[-v^6+3u^5v:\;u^6+3uv^5:\;-5u^3v^3]
$$
[@Dol18, §7, pp. 13--14]. The three forms have no common zero. The ten nodes already account for the total defect $\delta=10$ in the genus formula used to prove @lem:rational_sextic_ten_nodes, so they are the curve's only singularities. The Winger curve therefore belongs to $U$ and to $\Sigma_{10A_1}$. Every other member of $U$ likewise has exactly ten nodes by the same genus count. Since $\mathbb G$ is irreducible, the nonempty open set $U$ is dense in $B$.

**Step 3: a triple smooth conic is in the closure.** The base-point-free net
$$
N_0=\generators{u^6,\,-v^6,\,u^3v^3}\in B
$$
gives the map $[u:v]\mapsto[u^6:-v^6:u^3v^3]$, the composite of the degree-three map $[u:v]\mapsto[u^3:v^3]$ with the conic parametrization $[a:b]\mapsto[a^2:-b^2:ab]$. Its image cycle is therefore $Q^3$, where
$$
Q=(xy+z^2=0)
$$
is smooth because its defining quadratic form is nondegenerate. Density of $U$ and continuity of $c$ give $Q^3=c(N_0)\in\overline{c(U)}$. Also $c(U)$ is irreducible and contains the Winger curve, so $c(U)\subseteq\Sigma_{10A_1}$. Thus $Q^3\in\overline{\Sigma}_{10A_1}$, and the criterion in the statement gives $\mch^*_{10A_1}\neq\varnothing$.

**Step 4: the resulting compactification.** @thm:git-equals-looijenga identifies the GIT compactification with the Looijenga model of $\Gamma_{10A_1}\backslash D(T_\Co)$ ([@YZZ25, Theorem 4.11, p. 15]). The nonempty-arrangement case is not the Baily--Borel case described immediately before Proposition 3.7 [@YZ23, p. 10]. The construction above decides nonemptiness only; it does not determine the $\Gamma_{10A_1}$-orbits.
:::

::: {.question #qst:semifan-poset-position title="The position of the three semifans: degeneration cusps and the Looijenga comparison settled, KSBA open"}

The Coxeter, KSBA, and Looijenga semifans of the Coble period domain arise from distinct inputs; @def:looijenga-compactification and the following remark record the Looijenga input. By @thm:coble-arrangement-nonempty the arrangement is nonempty and the compactification is a proper Looijenga model. The orbit decomposition and the Coxeter comparison are settled by @thm:coble-looijenga-coxeter.

**(1) Closure and cusps of Shah's semistable degenerations.** Shah's Theorem 2.4 [@Sha80, pp. 491--492] lists the minimal-orbit curves, and his Theorem 3.2 [@Sha80, p. 493] supplies the nilpotence exponents; the first theorem does not itself assign a cusp. The double smooth cubic in Group II(4) is **not** in $\overline{\Sigma}_{10A_1}$, so it receives no Coble cusp. The remaining rows have the following proved assignments. Only the orbit information shown is claimed.

| Shah row | membership in $\overline{\Sigma}_{10A_1}$ | cusp level |
|:---|:---|:---|
| Group I, irreducible ten-nodal curves | the stratum itself | interior |
| Group II(1), three distinct nonsingular conics $\prod_{i=1}^3(x_0x_2+a_ix_1^2)$ | included | a $1$-cusp |
| Group II(2), a double line and four distinct lines | included | a $1$-cusp |
| Group II(3), the double conic $(x_0x_2+x_1^2)^2f_2$ with a quadric $f_2$ meeting it in four distinct points | included | a $1$-cusp |
| Group III(1), $(x_0x_2+x_1^2)^2(x_0x_2+ax_1^2)$, $a\neq1$ | included | the unique $0$-cusp $(9,9,1)_1$ |
| Group III(2), three distinct double lines $x_0^2x_1^2x_2^2$ | included | the unique $0$-cusp $(9,9,1)_1$ |
| Group IV, the cube $Q^3$ of a nonsingular conic | included | the special Looijenga point, not a Baily--Borel cusp |

In particular the **double smooth cubic is excluded**, rather than assigned to either cusp. Group II gives *a* $1$-cusp, without selecting a $\Gamma_\Co$-orbit. For Group III, $\Gamma_\Co=\Orth(T_\Co)$ by @prop:gamma-co-images(3), and @thm:unpolarized-cusps gives the unique $\Orth(T_\Co)$-orbit of primitive isotropic vectors, computed in its $\Orth(T_\Co)$ row at commit `963843f735`; that justifies "the" $0$-cusp, whose boundary type is $(9,9,1)_1$ by @thm:cusp_correspondence. Group IV has no family-independent Baily--Borel assignment because Shah's Remark 3.3 [@Sha80, p. 497] permits every exponent $1$, $2$, and $3$; it is the contraction point of [@YZ23, Remark 2.2, p. 5].

**(2) Is the Looijenga semifan the Coxeter semifan of a reflection group? Yes.** @thm:coble-looijenga-coxeter identifies every hyperplane as a pure root. At each $0$-cusp, only roots orthogonal to the cusp line contribute; their boundary traces are primitive $(-2)$-roots and are exactly the mirrors of the reflection group they generate. The induced semifan is therefore Coxeter. This reflection group has only $(-2)$-mirrors; the full $W^{(2,4)}$-Coxeter semifan of @thm:coble-coxeter-semifan additionally has $(-4)$-mirrors.

**(3) Does the Looijenga semifan refine or coarsen the KSBA semifan, or are they incomparable? Open.** The Coble KSBA semifan to which the comparison applies has not yet been formed: @thm:coble-coxeter-semifan explicitly leaves the generalized semifan unformed because the divisor of the Coble stable pair is undefined, and @warn:coble-marking records the missing dictionary from the nine simple roots to curves on the Coble surface. A comparison requires the universal stable pair, the relevance marking of the roots, and the resulting cones of combinatorial constancy; the nonemptiness of $\mch^{*}_{10A_1}$ supplies none of these data. No refinement, coarsening, or incomparability is asserted.
:::

::: {.proof}
**The image-cycle criterion.** Put $M=\overline M_{0,0}(\PP^2,6)$ and write $\Phi(\mu)=\mu_*[D]$ for the image cycle of a stable map $\mu:D\to\PP^2$, with multiplicities retained. Chen--Coskun's Theorem 1.4 [@CC11, p. 4; proof pp. 9--10] makes this a morphism to $\operatorname{Chow}_{6,0,2}$. Fulton--Pandharipande's §0.4 and Theorems 1--3 [@FulPan97, pp. 6--7, 11--12] show that $M$ is irreducible and that its smooth-domain locus is dense.

Let $U\subset M$ consist of birational maps from $\PP^1$ whose images have only ordinary nodes. Transversality makes this condition open: a node has two regular identification equations at its preimage pair, compactness excludes new identifications away from those pairs and the diagonal, and the immersion condition is open. Dolgachev's Winger parametrization ([@Dol18, §7, pp. 13--14]) supplies a point of $U$, so $U$ is dense in $M$. Normalization gives $\Phi(U)=\Sigma_{10A_1}$: the image is an irreducible rational sextic, whose total $\delta$-invariant is $10$, and therefore has exactly ten $A_1$ singularities. Hence continuity and properness of $M$ give
$$
\Phi(M)=\overline{\Sigma}_{10A_1}.
$$
Every central stable map below therefore certifies closure; curve selection turns it into an algebraic arc whose general members are irreducible ten-nodal sextics.

**Included rows.** Let $h_m(u:v)=(u^m:v^m)$, of degree $m$. For a line $L$ or smooth conic $Q$ choose a birational parametrization $\rho_L$ or $\rho_Q$. Then $(\rho_L\circ h_m)_*[\PP^1]=m[L]$ and $(\rho_Q\circ h_m)_*[\PP^1]=m[Q]$. A nodal tree of $\PP^1$'s has arithmetic genus zero, and the following stable maps have the exact displayed central cycles:

- **II(1).** Three maps $\rho_{Q_i}$ form a chain, glued at the two common points of the conics, with image cycle $Q_1+Q_2+Q_3$. Explicitly, $\rho_{Q_a}(u:v)=[au^2:uv:-v^2]$ parametrizes $Q_a=(x_0x_2+ax_1^2=0)$ birationally.
- **II(2).** A main map $\rho_L\circ h_2$ and four maps $\rho_{L_i}$, each leaf attached at $L\cap L_i$, give image cycle $2L+\sum_iL_i$.
- **II(3).** A double cover $\rho_Q\circ h_2$ and a map $\rho_R$ onto the quadric $R$, joined at one of the four points of $Q\cap R$, give image cycle $2Q+R$. If $R$ splits as two lines, use birational parametrizations of those two lines instead of $\rho_R$.
- **III(1).** The same two-component construction with a double cover of $Q$ and a birational parametrization of the other conic gives image cycle $2Q+R$.
- **III(2).** Three double covers $\rho_{L_i}\circ h_2$, joined in a chain at $L_1\cap L_2$ and $L_2\cap L_3$, give image cycle $2L_1+2L_2+2L_3$.
- **IV.** A single $\rho_Q\circ h_3$ gives image cycle $3Q$, the degree-three conic cover already used in @thm:coble-arrangement-nonempty.

**Exclusion of II(4).** Suppose the double smooth cubic $2E$ belonged to $\overline{\Sigma}_{10A_1}$. The image-cycle criterion would give a stable map $\mu:D\to\PP^2$ with $\mu_*[D]=2[E]$. Every domain component has rational normalization, since the connected nodal domain has arithmetic genus zero. At least one nonconstant component must therefore map onto $E$, producing a nonconstant morphism $\PP^1\to E$. No such morphism exists when $E$ is a smooth elliptic cubic. Hence $2E\notin\overline{\Sigma}_{10A_1}$.

**The cusp directions.** Shah's Theorem 3.2 [@Sha80, p. 493] gives exponents $1$, $2$, and $3$ to Groups I, II, and III. Those exponents match Types I, II, and III in Alexeev--Engel--Thompson's Definition 2.2 [@AET23, p. 6]. Their §3B [@AET23, pp. 15--16] then gives the rank-one/Type III/$0$-cusp and rank-two/Type II/$1$-cusp convention. It does not by itself identify a particular $\Gamma_\Co$-orbit, which is why only a $1$-cusp is asserted for Group II. The unique $0$-cusp asserted for Group III uses the full-group record at `963843f735` stated above, not a cusp correspondence between stable orbit sets.
:::

::: {.theorem #thm:coble-looijenga-coxeter title="The ten-nodal Looijenga semifan is a Coxeter semifan"}
With $P=\generators H\oplus L$ and $Q=P^{\perp\lkt}=T_\Co$ as in the sextic construction, put $c=\gamma([H/2])\in A_Q$. Every hyperplane of $\mch^{*}_{10A_1}$ is cut out by a pure root $r\in Q$ of square $-2$ satisfying the divided-class condition $[r/2]=c$. These hyperplanes form one $\Gamma_{10A_1}$-orbit, and already one orbit of the discriminant kernel.

At a $0$-cusp represented by a primitive isotropic vector $\eta$, the contributing traces form the complete mirror arrangement of the group generated by their integral reflections. Consequently the Looijenga semifan of $\Gamma_{10A_1}\backslash D(T_\Co)$ at every $0$-cusp is the Coxeter semifan of that reflection group. Its mirrors all have normal square $-2$; the full $W^{(2,4)}$-Coxeter semifan of @thm:coble-coxeter-semifan also has $(-4)$-mirrors.
:::

::: {.proof}
**Pure roots.** Let $\Lambda_1=H^{\perp\lkt}$. A root $r\in\Lambda_1$ has divisibility two there exactly when $u=(H+r)/2$ is integral in the K3 lattice [@YZZ25, Lemma 4.8, p. 14, and its proof]. Decompose $r=t+s$ with $t\in L_\QQ$ and $s\in Q_\QQ$, and write $t=\tfrac12\sum_i n_i\ell_i$ for the node roots $\ell_i$ of $L$. Integrality of $r$ makes $t\in L^*$, so $n_i\in\ZZ$. Since $r^2=s^2-\tfrac12\sum_i n_i^2=-2$, a nonempty hyperplane section of $D(Q)$ has $s^2<0$; indeed $s^\perp$ has signature $(2,8)$ exactly when $s^2<0$. Thus $\sum_i n_i^2<4$, so each nonzero $n_i$ is $\pm1$. But $u\cdot\ell_i=-n_i/2$ is an integer, forcing every $n_i$ to be even. Consequently $t=0$. The root therefore lies in $Q$ itself, and the graph of the discriminant gluing shows that $u$ is integral exactly when $[r/2]=\gamma([H/2])$ in $A_Q$ (with the quadratic-form twist suppressed in this notation).

**The orbit calculation.** Put $B=U_1\perp U_2\perp I_{0,7}$ and let $\rho$ be reduction modulo $2$ on $B$. Wall's Theorem 1.2 and §1.3 [@Wal62] classify the primitive vectors of an indefinite unimodular lattice by norm and ordinary/characteristic type. A norm-$(-1)$ vector of $B$ is ordinary: a characteristic vector has odd square congruent to $\sigma(B)=2-9\equiv1\pmod8$, whereas $-1\equiv7\pmod8$. Hence these vectors form one $O(B)$-orbit. Let $F=\Stab_{O(A_Q)}(\gamma[H/2])$ and let $R$ be the image in $F$ of the stabilizer of a root $r$ in this orbit. Since $B=\ZZ r\perp r^\perp$, this stabilizer is $O(r^\perp)$; surjectivity for the even $2$-elementary twist $r^\perp(2)$ identifies $R$ with $O(r^\perp/2r^\perp)$ (@thm:two-elementary-surjectivity). The discriminant kernel's orbits over the fixed class are the right cosets $F/R$.

The finite image of $\Gamma_{10A_1}$ is the group $H_{10}$ obtained from the ten node permutations through the same gluing, and the $\Gamma_{10A_1}$-orbits are the double cosets $H_{10}\backslash F/R$. Indeed, the normalizer description in [@YZZ25, Lemma 4.5, p. 13] reduces the action on $A_P$ to node permutations: the sign changes in $W(A_1^{10})$ are trivial modulo $2$. Every permutation lifts by the two discriminant-surjectivity theorems, and the discriminant kernel on $Q$ is contained in $\Gamma_{10A_1}$. Passing to the component-preserving subgroup causes no further split: $r^\perp$ is odd unimodular of signature $(2,8)$, so it contains a positive norm-one vector, whose reflection is discriminant-trivial, component-reversing, and fixes the root. The sign map $-\id$ also lies in the kernel, so root vectors and their hyperplanes have the same orbits. The transcript `computations/reports/coble_10a1-looijenga-cusp-run.txt` computes these finite groups and double cosets, rather than enumerating the infinite root lattice. It returns $|F|=|R|=94\,755\,225\,600$, hence $[F:R]=1$, and exactly one double coset $H_{10}\backslash F/R$. Thus both orbit counts in the theorem are $1$.

**The boundary traces.** At an isotropic line $I=\ZZ\eta$, Looijenga's Example 6.4 uses exactly the hyperplanes containing $I$ to decompose the cone $C_{I,+}$ [@Loo02, printed p. 30]. Thus a contributing root satisfies $(r,\eta)=0$, and its normal in $K=\eta^\perp/\ZZ\eta$ is $\bar r=r\bmod\ZZ\eta$, with $\bar r^2=-2$. It is primitive: if $\bar r=kv$ in the even lattice $K$, then $-2=k^2v^2$ forces $k=\pm1$. Its reflection is therefore an integral $(-2)$-reflection of $K$.

Write $\mathcal R_{c,\eta}$ for this set of trace roots. For any such $r$, the formula $s_r(x)=x+(x,r)r$ shows that $s_r$ fixes $\eta$ and induces $s_{\bar r}$ on $K$. Because pairings in $Q=B(2)$ are even, $s_r(x)-x\in2Q$; hence $s_r$ acts trivially on $A_Q$. If $r'$ is another contributing root, it follows that $s_r(r')$ has square $-2$, divided class $c$, and remains orthogonal to $\eta$. Thus $s_{\bar r}(\bar r')$ again belongs to $\mathcal R_{c,\eta}$. The group $W_{c,\eta}$ generated by all $s_{\bar r}$ therefore preserves $\mathcal R_{c,\eta}$. Let $\mathscr H$ be the set of mirrors furnished by these roots. I claim there are no other reflection mirrors of $W_{c,\eta}$. Argue by induction on the length of a reflection $t\in W_{c,\eta}$ as a word in the generators. The case of one generator is immediate. If $t=s_{\bar r_1}\cdots s_{\bar r_k}$, then $t'=s_{\bar r_1}ts_{\bar r_1}=s_{\bar r_2}\cdots s_{\bar r_k}$ is a shorter reflection, so its mirror $M'$ belongs to $\mathscr H$ by the induction hypothesis. Since $t=s_{\bar r_1}t's_{\bar r_1}$, its mirror is $s_{\bar r_1}M'$, which belongs to $\mathscr H$ by stability of the trace set. The trace arrangement is therefore exactly the complete mirror arrangement of $W_{c,\eta}$. Since $W_{c,\eta}\leq O(K)$ is discrete, the standard chamber theorem for discrete reflection groups applies: the complete mirror arrangement decomposes the hyperbolic space into $W_{c,\eta}$-equivalent cells, each a fundamental domain, with the wall reflections generating the group [@Vin75, §1(1)--(3), printed p. 325]. Its chambers therefore give the stated Coxeter semifan in the sense of [@AEGS25, Definition 5.1, printed p. 609]. All these mirrors have normal square $-2$; the full $W^{(2,4)}$-Coxeter semifan additionally has $(-4)$-mirrors.
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

- **$\widetilde\Orth^+(T_\Co)$ generators.** Not known; the matrix representation is a stub. What is known is the reflective part: by @prop:gamma-co-reflective-set the reflections in the short roots of $T_\Co$ all lie in $\widetilde\Orth^+(T_\Co)$ and no long root does, so the reflective set is exactly the short roots; what is open is the index $[\widetilde\Orth^+(T_\Co) : W(T_\Co)]$. The candidate description of the whole group is the image in $\Orth^+(T_\Co)$ of the intersection of the reflection group $W(T)$ with the centralizer $Z(\theta_\Co)$ and with the stabilizer of the primitive vector $\tilde h_\Co = f^{*}h_\Co$, of square $4$ (@prop:gamma-co-in-theta-centralizer), whose eigenspace formulation is the one that can be written down at present.
:::
