# Clean proof for independent check

**Statement checked.** For every complex Coble surface S with |-2K_S|={C}, C one connected smooth curve, non-classical objects exist but no additional connected or irreducible component of the cover-retaining moduli stack exists. The classical ten-distinct-node substack is open, dense, connected and strict. No universal-stack anti-invariant monodromy identity is asserted. The unconditional invariant-lattice transport-and-isomorphism aggregate is W(E_10), not automatically the universal stack monodromy.

The following are the exact proof blocks to be checked. Page-internal labels name statements in `writing/coble/lattices-and-moduli/moduli-construction.md`; the external source statements are Dolgachev–Zhang Introduction, Lemma 1.2, Lemma 1.5, Corollary 1.6, Lemma 1.10, Theorem 4.3, Definition 6.1, Lemma 6.2, Theorem 6.3, Proposition 6.4, Theorems 6.5–6.7 and Example 6.10; Grivaux Proposition 3.1; Huybrechts Chapter 6 Remark 2.6, Corollary 2.7, Proposition 2.8 and §2.4; Harris–Morrison §6.E Initial reductions and (6.45) and Theorem (1.49)(1); Alexeev–Engel–Han Definition 2.2 and Lemma 2.7; Huybrechts Chapter 1 (2.5).

## Ordered-configuration freeness and connectedness

:::

::: {.lemma #lem:d2-plane-sextic-freeness title="The fixed locus of a projectivity, and the principal bundle $V\to B$"}

Let $V$ and $B=V/\PGL_3$ be as in @not:d2-plane-sextic-base.

1. The fixed points of a non-identity projectivity of $\PP^2$ lie in the union of a line and a point.
2. Every line carries at most three nodes of $Z$, and no non-identity projectivity fixes all ten nodes; hence $\PGL_3$ acts freely on $V$, and the $\SL_3$-stabilizer of every point of $V$ is $\mu_3$.
3. Every point of $V$ has four nodes with no three collinear; for the four-element subsets $I$ of the labels the charts $S_I\to B$ of the proof make $B$ a complex analytic space and $V\to B$ a principal $\PGL_3$-bundle.
:::

::: {.proof}

(1) A projectivity of $\PP^2$ has at most three eigenvalues. With three distinct eigenvalues its fixed points are the three eigenvectors; with two, they are the projectivized eigenspace of the repeated eigenvalue, a point or a line, together with the eigenvector of the other eigenvalue; with one, it is $\lambda(\id+N)$ with $N$ nilpotent, and the fixed points are the projectivized kernel (@def:kernel-cokernel) of $N$, a point or a line. In every case the fixed locus lies in $L\cup\theset{P}$ for a line $L$ and a point $P$.

(2) If four nodes lay on a line $L$, then $Z\cdot L\ge4\cdot2=8>6=\deg Z$, so $L$ is a component of $Z$ by Bézout, against the irreducibility of $Z$; hence a line carries at most three nodes. By (1) a non-identity projectivity fixes at most three nodes on $L$ and at most one at $P$, so at most four of the ten and never all ten; hence the $\PGL_3$-stabilizer of a point of $V$ is trivial. The kernel of $\SL_3\to\PGL_3$ is $\mu_3$ and acts trivially, so the $\SL_3$-stabilizer is $\mu_3$.

(3) Three non-collinear nodes exist, since at most three lie on a line. For three non-collinear nodes $A,B,C$ the lines $AB$, $AC$, $BC$ carry at most three nodes each and contain $A,B,C$ twice each, so at most $3+3+3-3=6$ nodes lie on them and a fourth node $D$ lies outside; then $A,B,C,D$ have no three collinear. For a four-element subset $I$ of the labels let $V_I\subset V$ be the open set of configurations whose $I$-indexed nodes have no three collinear, fix a projective frame $q_1,\dots,q_4$, and let $S_I\subset V_I$ be the closed subset (@def:closed-subset) of configurations whose $I$-indexed nodes are $q_1,\dots,q_4$. The map $\PGL_3\times S_I\to V_I$, $(g,s)\mapsto g\cdot s$, is a bijection: a configuration $v\in V_I$ has a unique projectivity $g_v$ carrying its $I$-indexed nodes to $q_1,\dots,q_4$, because a projectivity is determined by the images of four points with no three collinear, and $v=g_v^{-1}(g_vv)$ with $g_vv\in S_I$. It is a homeomorphism because $v\mapsto g_v$ is given by solving a linear system whose determinant is nonzero on $V_I$. The composites $S_I\to V_I\to B$ are therefore charts; they cover $B$ by the first paragraph, and their transition maps are restrictions of the $\PGL_3$-action, hence analytic. So $B$ is a complex analytic space and $V\to B$ is a principal $\PGL_3$-bundle.
:::

::: {.lemma #lem:d2-incidence-connected title="The labelled ten-nodal sextics are path connected; so are $B$, $U$ and $M_\Co$, and $\bar B$ is connected"}

In the notation of @not:d2-plane-sextic-base, let
$$
q\colon V\too\Sigma,\qquad(Z;p_1,\dots,p_{10})\longmapsto Z,
$$
be the map that forgets the labels, onto its image $\Sigma\subset\abs{\OO_{\PP^2}(6)}$. Then:

1. $\Sigma$ is the set of reduced and irreducible plane sextics of geometric genus $0$ whose only singular points are nodes, the locus $U_{6,0}$ of [@HM98, Definition (1.48)]. The group $S_{10}$ acts freely on $V$ by permuting the labels, the fibres of $q$ are its orbits, and $q$ is a covering map.
2. $V$ is path connected (@def:path-connectedness). Equivalently, $\Sigma$ is path connected and the monodromy group of the covering $q$ at a sextic $Z_0\in\Sigma$, a group of permutations of the ten nodes of $Z_0$, is the full symmetric group.
3. $B=V/\PGL_3$, $U$ and $M_\Co=U/\PGL_3$ are path connected and their closures are irreducible, and the stack $\bar B=[B/S_{10}]$ is connected.
:::

::: {.proof}

1. *The image and the fibres.* The sextic $Z$ of a point of $V$ is irreducible, hence reduced, its singular points are ten ordinary double points (@def:ordinary-double-point), and its geometric genus is $0$ (@lem:rational_sextic_ten_nodes). Conversely, a reduced and irreducible sextic of geometric genus $0$ with only nodes has exactly ten nodes by the same lemma, and each ordering of them is a point of $V$ over it. Two points of $V$ over one sextic differ by a permutation of the labels, and a permutation that fixes a point of $V$ is the identity, the ten nodes being distinct.

*The covering.* Let $Z_0\in\Sigma$ have the nodes $p^0_1,\dots,p^0_{10}$. For each $i$ take affine coordinates $(x,y)$ of $\PP^2$ at $p^0_i$ and, for $Z$ near $Z_0$, an equation $F_Z(x,y)$ of $Z$ whose coefficients are analytic functions of $Z$. The Jacobian matrix in $(x,y)$ of the map $(Z,x,y)\mapsto(\partial_xF_Z,\partial_yF_Z)$ at $(Z_0,p^0_i)$ is the Hessian of $F_{Z_0}$ at $p^0_i$, which is invertible. By the implicit function theorem there are a neighbourhood $N_i$ of $Z_0$ in $\abs{\OO_{\PP^2}(6)}$, an open neighbourhood $D_i$ of $p^0_i$ and an analytic map $\pi_i\colon N_i\to D_i$ such that, for $Z\in N_i$, the point $\pi_i(Z)$ is the only point of $D_i$ at which $\partial_xF_Z=\partial_yF_Z=0$; take the $D_i$ pairwise disjoint. The set of pairs $(Z,p)$ with $p\in\Sing Z$ is closed in $\abs{\OO_{\PP^2}(6)}\times\PP^2$, and $\PP^2\sm\bigcup_iD_i$ is compact, so there is a neighbourhood $N\subset\bigcap_iN_i$ of $Z_0$ such that $\Sing Z\subset\bigcup_iD_i$ for all $Z\in N$. A sextic $Z\in\Sigma\intersect N$ has ten singular points, all of them in $\bigcup_iD_i$ and at most one of them in each $D_i$, namely $\pi_i(Z)$; so $\Sing Z=\theset{\pi_1(Z),\dots,\pi_{10}(Z)}$. Hence
$$
q^{-1}(\Sigma\intersect N)=\bigsqcup_{\sigma\in S_{10}}\theset{\qty(Z;\pi_{\sigma(1)}(Z),\dots,\pi_{\sigma(10)}(Z))\st Z\in\Sigma\intersect N},
$$
each of the $10!$ sets on the right is open in $q^{-1}(\Sigma\intersect N)$, being cut out by the conditions $p_j\in D_{\sigma(j)}$, and $q$ maps it homeomorphically onto $\Sigma\intersect N$, with the continuous inverse $Z\mapsto\qty(Z;\pi_{\sigma(1)}(Z),\dots,\pi_{\sigma(10)}(Z))$. So $q$ is a covering map.

2. *The equivalence.* Fix $v_0=(Z_0;p^0_1,\dots,p^0_{10})\in V$. By (1) a loop $\gamma$ of $\Sigma$ at $Z_0$ lifts to a path of $V$ from $v_0$ to $\sigma_\gamma v_0$ for exactly one $\sigma_\gamma\in S_{10}$. The permutation of the nodes of $Z_0$ along $\gamma$ determines $\sigma_\gamma$ and is determined by it, so the monodromy group is the full symmetric group if and only if every $\sigma\in S_{10}$ is a $\sigma_\gamma$. If $V$ is path connected, then so is its image $\Sigma$, and a path of $V$ from $v_0$ to $\sigma v_0$ projects to a loop $\gamma$ with $\sigma_\gamma=\sigma$. Conversely, let $\Sigma$ be path connected and let every $\sigma$ be a $\sigma_\gamma$. For $v\in V$, a path of $\Sigma$ from $q(v)$ to $Z_0$ lifts to a path of $V$ from $v$ to a point $\sigma v_0$ of the fibre over $Z_0$, and the lift of a loop $\gamma$ with $\sigma_\gamma=\sigma$ joins $v_0$ to $\sigma v_0$.

*The statement.* In [@HM98, §6.E, *Initial reductions*], $V_{d,g}$ is the variety of irreducible nodal plane curves of degree $d$ and geometric genus $g$, and $m=\binom{d-1}{2}$; so $\Sigma=V_{6,0}$ and $m=10$. The statement of [@HM98, §6.E, the paragraph that precedes the uniform position principle (6.45)] is: for every two curves $C_0$ and $C_1$ of $V_{d,0}$ and every bijection between their nodes there is a family $\theset{C_t}$ of nodal curves of $V_{d,0}$ that joins $C_0$ to $C_1$, in which the nodes trace arcs $p_1(t),\dots,p_m(t)$ that induce that bijection; that is, the monodromy in the family $V_{d,0}$ acts on the nodes of $C_0$ as the full symmetric group on $m$ letters. The monodromy assertion is established in the passage just cited. Let $v_0=(C_0;p_1,\dots,p_{10})$ and $v_1=(C_1;p'_1,\dots,p'_{10})$ be two points of $V$, and take the family for the bijection $p_i\mapsto p'_i$. Then $t\mapsto(C_t;p_1(t),\dots,p_{10}(t))$ is a path of $V$ from $v_0$ to $v_1$.

*The proof in the source.* A rational nodal curve of degree $d$ is the projection of the rational normal curve $X\subset\PP^d$ from a subspace $\Lambda\cong\PP^{d-3}$, and its nodes correspond to the points in which $\Lambda$ meets the chordal variety of $X$. The uniform position principle [@HM98, (6.45)] states that, for a nondegenerate irreducible variety of dimension $k$ and degree $d$ in $\PP^n$, the monodromy acts as the full symmetric group on its $d$ points of intersection with a subspace $\Lambda\cong\PP^{n-k}$, as $\Lambda$ varies over the subspaces transverse to the variety. For a curve and its hyperplane sections this is the lemma in the second proof of the general position theorem of [@ACGH85, Chapter III, §1].

3. Smoothness of $\Sigma$ is [@HM98, Theorem (1.49)(1)], so $V$ is a complex manifold because $q$ is a covering. It is connected by 2, and a connected complex manifold is irreducible. The spaces $B$, $U$ and $M_\Co$ are continuous quotient images of $V$, so they are irreducible; the same quotient images are path connected because $V$ is path connected. Finally $\bar B=[B/S_{10}]$ has the path connected space $B$ as a smooth cover, so it is connected.
:::


::: {.proposition #prop:d2a-family-is-universal-nowhere title="The D2a family is universal over no open substack of $\mcM_\Co$"}

Let $\varphi\colon\bar B=[B/S_{10}]\to\mcM_\Co$ be the classifying morphism of the family of @def:coble-family-unpolarized(2), $\bar B$ the unlabelled base, and let $\psi\colon B\to\mcM_\Co$ be the classifying morphism of the same family over the labelled base $B$ of @def:coble-family-unpolarized(3), so that $\psi$ is the composite of $B\to\bar B$ with $\varphi$.

A family over a base is *universal over an open substack* $W$ when its classifying morphism is an equivalence onto $W$; this is the notion of a moduli stack and a universal family used throughout this page (@def:coble-moduli-functor, and @lem:d2a-moduli-stack, where $[V/\SL_3]$ is the moduli stack of @def:coble-family-unpolarized with universal family that of @lem:d2-unpolarised-family(3)).

Then:


## Objects and classification

::: {.definition #def:coble-moduli-functor title="The moduli functor of Coble surfaces"}

Let $\mathfrak{C}$ be the category of complex spaces. The functor
$$
\mcM_\Co\colon\mathfrak{C}^{\mathrm{op}}\too\mathfrak{Grpd}
$$
assigns to $Y$ the groupoid whose **objects** are triples $\qty{\mcs\xrightarrow{f}Y,\ \mcx\xrightarrow{\pi}\mcs,\ \iota}$ with:

1. $f$ flat, proper and of finite presentation (@def:finite-presentation), whose geometric fibres are Coble surfaces $S$ in the sense of [@DZ99, Introduction] — nonsingular projective rational with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}\neq\emptyset$ — **with $\abs{-2K_S}$ consisting of one connected smooth curve $C$**. Both halves of that condition are forced
by the owner's object, and neither implies the other: a disjoint union of two smooth curves is smooth and disconnected, and smoothness alone therefore does not give a single curve. Smoothness: the cover branched along a non-reduced member is neither normal nor a $\mathrm{K3}$ surface, so a non-reduced member is not admissible. Connectedness: the volume's Coble moduli is $F_{\Co}=F_{\Co,1}$, the $n=1$ case of $F_{\Co,n}$, where $\abs{-2K_S}=C_1+\cdots+C_n$ (@prop:coble-k3-cover); a smooth divisor with $n>1$ components has $\chi(\operatorname{Fix}\iota)=2n$ and invariant lattice (@def:invariant_coinvariant_lattices) of rank $10+n$. Indeed, $C^2=-4n=4K_S^2$, so $K_S^2=-n$, and the rank is $b_2(S)=10-K_S^2$; the $n=1$ type is $(11,11,1)$ [@DZ99, §6, Proposition 6.4(2); @DK13, §3];
2. $\pi$ the relative double cover branched along $\mcC$, that single smooth member; since $\mcC=2\mcD$ for $\mcD=-\K_{\mcs/Y}$, the cover exists, is smooth because $\mcC$ is, its canonical class is $\pi^*(K_{\mcs/Y}+\mcD)=0$, so its fibres are $\mathrm{K3}$ surfaces [@DK13, §3], and their invariant lattice is $M$ of type $(11,11,1)$ because the fixed curve is a single smooth rational curve (@prop:coble-period-domain(1)--(2));
3. $\iota$ the covering involution of $\pi$;

and whose **morphisms** $\qty{f,\pi,\iota}\to\qty{f',\pi',\iota'}$ over $Y$ are Cartesian squares over $Y$ commuting with $\pi$ and $\iota$. The **pullback** along $g\colon Y'\to Y$ is the fibre product $(-\times_Y Y')$, with the induced $\pi$ and $\iota$.
:::

::: {.lemma #lem:coble-moduli-functor-stack title="$\mcM_\Co$ is a stack"}

$\mcM_\Co$ is a stack for the étale topology on $\mathfrak{C}$, hence also for the analytic topology.

1. *Isomorphisms are a sheaf.* For two objects over $Y$ the isomorphisms form a subsheaf of the sheaf of isomorphisms of the underlying families of spaces, cut out by the equations expressing the commutativity with $\pi$ and $\iota$; a map of complex spaces is determined by its restrictions to an open cover.
2. *Objects descend.* Let $Y'\to Y$ be étale and surjective with its two projections, and let an object over $Y'$ with a descent datum be given. Étale morphisms of complex spaces are local analytic isomorphisms. Choose an open cover $\{Y_i\}$ of $Y$ with local analytic isomorphisms $U_i\iso Y_i$ from open $U_i\subseteq Y'$. Restrict $\mcs'$ and $\mcx'$ to the $U_i$. The descent datum provides isomorphisms of these objects on $U_i\cap U_j$, satisfying the triple-overlap cocycle. Glue the underlying complex spaces and their structure sheaves along these isomorphisms, and glue $f'$, $\pi'$ and $\iota'$ as holomorphic maps. Flatness, properness and finite presentation are local for this cover, and every geometric fibre of the glued family is a geometric fibre of the original one.
3. *The fibre condition and the branch divisor descend.* The condition of @def:coble-moduli-functor(1), that a geometric fibre is a Coble surface whose anti-bicanonical system consists of one connected smooth curve, is a condition on each geometric fibre, hence checked after the étale cover; it does not refer to a plane model. The divisor $-2K_{\mcs/Y}$ is defined by the relative canonical sheaf, so it descends with $f$; and the double cover of (2) is $\Spec_{\OO_\mcs}\qty(\OO_\mcs\oplus\OO_\mcs(-\mcD))$ for any $\mcD$ with $\OO(2\mcD)=\OO(-2K_{\mcs/Y})$, which is canonical in $\mcD$ up to the sign of the summand, so it and its involution are determined by the descended family.
:::

::: {.proof}

(1) is the sheaf property of the presheaf of isomorphisms of two spaces over $Y$, restricted by closed conditions.

(2) Each $U_i\iso Y_i$ is a local section of the étale cover, so its inverse is an open immersion to $Y'$. On $Y_i\cap Y_j$ the two sections need not agree, but the descent datum identifies the two restricted objects; on triple overlaps these identifications satisfy the cocycle. Consequently the topological spaces and the rings of holomorphic functions glue compatibly, and the resulting ringed spaces are complex spaces because this holds on every $Y_i$. This is direct analytic gluing, not an application of SGA 1, Exposé VIII, which is a statement about schemes. The properties of the descended morphism are checked on the same cover; no global projectivity of $f$ is required by @def:coble-moduli-functor, only projectivity of its geometric fibres.

(3) A geometric fibre of $f$ is a geometric fibre of $f'$ with the same base change, so the first condition is unaffected; the argument uses the fibre condition only as a property of the fibre. For the second, $K_{\mcs/Y}$ is $\det\Omega^1_{\mcs/Y}$ in the smooth case and is computed from the descended $f$; the cyclic cover is the construction used in the proof of @lem:d2-unpolarised-family(2) [@EV92, §3, Chapter I], whose input is the branch divisor and a line bundle $\OO(\mcD)$ with $\OO(2\mcD)=\OO(-2K_{\mcs/Y})$, and which uses no plane model. The morphisms $\pi$ and $\iota$ are part of the object and descend with it by (2).
:::

::: {.definition #def:coble-moduli-functor-z title="The Coble functor over $\ZZ[1/2]$"}

Let $S_0=\Spec\ZZ[1/2]$. On the category of $S_0$-schemes of finite presentation (@def:finite-presentation) the functor
$$
\mcM_\Co\colon\qty(\mathbf{Sch}_{/S_0})^{\mathrm{op}}\too\mathfrak{Grpd}
$$
assigns to $Y$ the groupoid of triples $\qty{\mcs\xrightarrow{f}Y,\ \mcx\xrightarrow{\pi}\mcs,\ \iota}$ in which

1. $f$ is flat and projective of finite presentation, and each geometric fibre is a Coble surface in the sense of [@DZ99, Introduction] — nonsingular, projective, rational, $\abs{-K}=\emptyset$, $\abs{-2K}\neq\emptyset$ — **with $\abs{-2K}$ a single smooth curve** $\mcC$; the classical members $\Bl_{p_1,\dots,p_{10}}\PP^2$ of @lem:d2-unpolarised-family(1), where $\abs{-2K}$ is a single smooth rational curve, are the subfamily D2a uses;
2. $\pi$ is the cyclic double cover branched along $-2K_{\mcs/Y}$, that is the $\mu_2$-torsor $\Spec_{\OO_\mcs}\qty(\OO_\mcs\oplus\OO_\mcs(-\mcD))$ for $\mcD$ with $\OO(2\mcD)=\OO(-2K_{\mcs/Y})$, which exists because $2$ is invertible on $S_0$ and the class $-K_{\mcs/Y}$ is integral (@lem:d2-unpolarised-family(2));
3. $\iota$ is the involution of $\pi$;

with morphisms the Cartesian squares over $Y$ commuting with $\pi$ and $\iota$, and pullback the fibre product. The number $N=2$ is the only one needed: the node condition is defined over $\ZZ$, the ordinary-double-point condition is the nonvanishing of the Hessian determinant, the divisor $-2K_{\mcs/Y}$ is defined by the relative canonical sheaf, and the cover of (2) is a $\mu_2$-torsor precisely because $2\in\OO_{S_0}^{\times}$.
:::

::: {.remark #rmk:coble-class-smooth-antinbicanonical title="Which Coble surfaces the functor admits, and the question whether this is the classical class"}

@def:coble-moduli-functor and @def:coble-moduli-functor-z admit the Coble surfaces of [@DZ99, Introduction] **with $\abs{-2K}$ a single smooth curve** — the $n=1$ members of $F_{\Co,n}$ (@prop:coble-k3-cover), which are the owner's object, and exactly those whose double cover is a $\mathrm{K3}$ surface with invariant lattice $M$ of type $(11,11,1)$ [@DK13, §3].

*Departure, and the repair it forced.* An earlier form of these two definitions asked only that $\abs{-2K}$ *contain* a smooth member, and that is false as a description of one lattice: [@DZ99, §6, Proposition 6.4(2)] gives Coble surfaces whose unique anti-bicanonical divisor is smooth but is a disjoint union of $(-4)$-curves, so a smooth divisor with $n>1$ components satisfies the weaker condition and has $\chi(\operatorname{Fix}\iota)=2n$. Since $C^2=-4n=4K_S^2$, one has $K_S^2=-n$ and the invariant rank is $b_2(S)=10-K_S^2=10+n$; the fixed-locus formula for $n=1$ gives the different type $(11,11,1)$ [@DK13, §3], so it is not an object of @def:involution-stack. The condition is therefore a single smooth curve, not a smooth member, and the earlier statement that every object of the functor is labellable was proved only for the $n=1$ case it silently assumed.

This class is not the classical class $\Bl_{p_1,\dots,p_{10}}\PP^2$ of ten distinct nodes. Its objects are the blow-ups of the ten double points of the irreducible rational sextics whose singular points are double points (@thm:coble-smooth-antibicanonical-is-a-plane-blowup, @prop:coble-plane-models-are-double-point-sextics); a double point can be a cusp and centres can be infinitely near (@ex:coble-sextics-with-an-a15-point); and some objects have no plane presentation by ten distinct nodes (@prop:coble-e8-configuration-excludes-ten-distinct-centres). The classical objects form an open dense substack, so the widening adds no component to $\mcM_\Co$ (@thm:coble-classical-substack-is-open-dense-and-proper).
:::

::: {.theorem #thm:coble-smooth-antibicanonical-is-a-plane-blowup title="A Coble surface with a single smooth anti-bicanonical curve is a blow-up of the plane at ten double points of an irreducible sextic"}

Let $S$ be a Coble surface in the sense of [@DZ99, Introduction] — a nonsingular projective rational surface with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}\neq\emptyset$ — and suppose that $\abs{-2K_S}=\theset{C}$ consists of one connected smooth curve $C$. Then:

1. $C$ is rational, $C^2=-4$, $K_S^2=-1$, and $S$ is minimal as a Coble surface in the sense of [@DZ99, §1.1].
2. $S$ is *basic* in the sense of [@DZ99, §4.1]: it admits a birational morphism onto $\PP^2$, and so is a blow-up $\Bl_{p_1,\dots,p_{10}}\PP^2$ at ten points, each $p_i$ a point of the blow-up at $p_1,\dots,p_{i-1}$, so that a centre can be infinitely near to an earlier one. With $H$ the pullback of $\OO_{\PP^2}(1)$ and $E_1,\dots,E_{10}$ the total transforms in $S$ of the exceptional curves of the ten centres, $\Pic(S)=\ZZ H\oplus\bigoplus_i\ZZ E_i$ with $H^2=1$, $E_i^2=-1$ and all other products zero, $-K_S=3H-\tsum_iE_i$ and $C=-2K_S=6H-2\tsum_iE_i$.
3. The image $Z\definedas\pi(C)\subset\PP^2$ of $C$ is an irreducible plane sextic; the map $C\to Z$ is the normalisation; every singular point of $Z$ is the image of one of the ten centres, and $Z$ has multiplicity $2$ there. In particular $\delta(Z)=\pa(Z)-\pa(C)=10$, so the singular points of $Z$ are the whole of its arithmetic genus.
4. Suppose the ten $p_i$ are distinct points of $\PP^2$. Then $Z$ has exactly ten double points, each of $\delta=1$, and each is an ordinary node or an ordinary cusp; the node occurs exactly when $C$ meets $E_i$ in two distinct points and the cusp exactly when it meets it in one point of multiplicity two (@lem:coble-double-point-of-the-sextic). In the plane model of [@DZ99, §5.1] the ten points are distinct as soon as the nine base points of the Halphen pencil are, which is the case of the classical class (@rmk:which-coble-surfaces-have-a-plane-model).
:::

::: {.proof}

*1.* By hypothesis $C\equiv-2K_S$. Since $S$ is rational, [@DZ99, Lemma 1.2(1)] computes the arithmetic genus of a divisor as $\pa(D)=h^0(D+K_S)$, so $\pa(C)=h^0(-K_S)=0$ because $\abs{-K_S}=\emptyset$; a smooth connected curve of arithmetic genus $0$ is $\PP^1$. Adjunction on $S$ then gives $-2=2\pa(C)-2=C^2+K_S\cdot C=4K_S^2-2K_S^2$, that is $K_S^2=-1$ and $C^2=4K_S^2=-4$. For minimality, a nontrivial birational morphism of $S$ onto another Coble surface $S'$ presents $S$ as the blow-up of $S'$ at $k\geq1$ points, so $K_S^2=K_{S'}^2-k$, which with $K_{S'}^2\leq-1$ for every Coble surface [@DZ99, §1.1] contradicts $K_S^2=-1$; that is the statement of [@DZ99, §1.1] that a Coble surface with $K^2=-1$ is minimal.

*2.* By [@DZ99, Lemma 1.10] a Coble surface admits a blow-down, so $S$ carries a $(-1)$-curve $E$; let $\pi\colon S\to Y$ be the blow-down of $E$. Since $S$ is minimal in the sense of clause 1, [@DZ99, Corollary 1.6] gives $\pa(D+2E)=1$ for every $D\in\abs{-2K_S}$; in particular $\pa(C+2E)=1$.

*3.* Write $C_Y\definedas\pi(C)$. Since $-2K_S=\pi^*(-2K_Y)-2E$, equivalently $-2K_S+2E=\pi^*(-2K_Y)$, we have $\pi_*C=C_Y\in\abs{-2K_Y}$, and $C_Y$ is reduced: $\pi$ is an isomorphism away from $E$, and $C$ is reduced. By [@DZ99, Lemma 1.5(1)] $\pa(C+2E)=h^0(-K_Y)$, so $h^0(-K_Y)=1$ and $\abs{-K_Y}=\theset{D_0}$ for an effective divisor $D_0\neq0$. Then $2D_0\in\abs{-2K_Y}$ as well, and $2D_0\neq C_Y$ because $C_Y$ is reduced and $2D_0$ is not; hence $h^0(-2K_Y)\geq2$. Pullback along $\pi$ is an isomorphism on sections, so $h^0(-2K_S+2E)=h^0(-2K_Y)\geq2$, and the decomposition $\abs{-2K_S+2E}=M+P$ of [@DZ99, §2.1], with $M$ the mobile part, has $M\neq0$.

*4.* By [@DZ99, Lemma 1.2(1)] a subdivisor has no larger arithmetic genus, so $\pa(M)\leq\pa(M+P)=\pa(C+2E)=1$, and $\pa(M)\in\theset{0,1}$; these are the two values by which [@DZ99, §2.1] defines the elliptic and the rational type with respect to $E$. If $\pa(M)=0$ then $S$ is of rational type with respect to $E$, and [@DZ99, Theorem 6.3] says that such a surface is never of $\mathrm{K3}$-type; but $C$ is a reduced member of $\abs{-2K_S}$, so $S$ *is* of $\mathrm{K3}$-type [@DZ99, Definition 6.1; @lem:dz-k3-type-double-cover]. Hence $\pa(M)=1$: $S$ is of elliptic type with respect to $E$, and [@DZ99, Theorem 4.3] gives that $S$ is basic, that is, admits a birational morphism onto $\PP^2$ [@DZ99, §4.1; @thm:coble-elliptic-type-classification, last sentence].

*5.* Such a morphism $\pi\colon S\to\PP^2$ is a composition of $k$ blow-ups at points: the $i$-th centre $p_i$ is a point of the surface $S_{i-1}$ obtained from $S_0=\PP^2$ by blowing up $p_1,\dots,p_{i-1}$, and it can lie on an earlier exceptional curve. Let $E_i\subset S$ be the total transform of the exceptional curve of $p_i$. Then $\Pic(S)=\ZZ H\oplus\bigoplus_i\ZZ E_i$ with $H^2=1$, $E_i^2=-1$ and all other products zero, $K_S=\pi^*K_{\PP^2}+\tsum_{i=1}^kE_i=-3H+\tsum_iE_i$ (@prop:canonical-class-of-blowup at each blow-up), and $9-k=K_S^2=-1$, that is $k=10$. Then $C=-2K_S=6H-2\tsum_{i=1}^{10}E_i$, so $C\cdot E_i=2$ and $C\cdot H=6$. The image $Z=\pi(C)$ has degree $C\cdot H=6$; it is irreducible because $C$ is; $C\to Z$ is an isomorphism away from the images in $\PP^2$ of the ten centres because $\pi$ is, and there $Z$ is smooth because $C$ is. Let $C_{i-1}\subset S_{i-1}$ be the image of $C$, so that $C_0=Z$. The blow-up at $p_i$ subtracts $\mult_{p_i}C_{i-1}$ times the exceptional curve from the total transform of $C_{i-1}$, so $[C]=6H-\tsum_i\qty(\mult_{p_i}C_{i-1})E_i$, and comparison with $[C]=6H-2\tsum_iE_i$ gives $\mult_{p_i}C_{i-1}=2$ for every $i$; for a centre $p_i$ that is a point of $\PP^2$ this is $\mult_{p_i}Z=2$. Since $C$ is smooth and proper, $C\to Z$ is the normalisation: it factors through the normalisation $\widetilde Z\to Z$, and the factor $C\to\widetilde Z$ is a birational morphism of smooth projective curves and so an isomorphism. So the geometric genus of $Z$ is that of $C$, which is $\pa(C)=0$. A plane sextic has $\pa(Z)=10$, so $\delta(Z)=\pa(Z)-\pa(C)=10$. When the ten centres are distinct points of $\PP^2$, $\Sing Z=\theset{p_1,\dots,p_{10}}$ and $\delta(Z)=\tsum_i\delta(Z,p_i)$ with each term $\geq1$, so $\delta(Z,p_i)=1$ for every $i$; with $\mult_{p_i}Z=2$ what is left is read off at @lem:coble-double-point-of-the-sextic. That is clause 4. (A centre lying on the exceptional curve of an earlier one makes that image a double point with an infinitely near double point over it; this occurs, @ex:coble-sextics-with-an-a15-point.)
:::

::: {.lemma #lem:coble-double-point-of-the-sextic title="A double point of the sextic is a node exactly when the preimage of its exceptional curve is a smooth $(-2)$-curve"}

In the situation of @thm:coble-smooth-antibicanonical-is-a-plane-blowup let $X\to S$ be the double cover branched along $C$ (@def:coble-moduli-functor(2)), and let $E\subset S$ be a $(-1)$-curve with $C\cdot E=2$. Then:

1. $C\cap E$ consists of two distinct points if and only if the preimage $\pi^{-1}(E)\subset X$ is a smooth rational curve, of square $-2$.
2. If $C\cap E$ is one point, of multiplicity two, then $\pi^{-1}(E)$ is the union of two rational curves of square $-2$ meeting in one point.
3. Hence the double point of $Z$ over $E$ is an ordinary node in case 1 and an ordinary cusp in case 2; in particular the ten double points of @thm:coble-smooth-antibicanonical-is-a-plane-blowup(3) are all ordinary nodes if and only if $C$ meets each of the ten exceptional curves in two distinct points.
:::

::: {.proof}

$C$ is the branch divisor, so the preimage of $E$ is $\pi^*E$, of square $2E^2=-2$. Away from $C\cap E$ the covering $\pi$ is étale, so $\pi^{-1}(E)$ is smooth there and of degree two over $E\cong\PP^1$. Over a point of $C\cap E$ the equation of $\pi$ is $w^2=s$ for a local equation $s$ of $C$, so $\pi^{-1}(E)$ is $w^2=s=0$. A double cover of $\PP^1$ branched at two distinct points is a $\PP^1$, which is 1; branched at one point of multiplicity two it is two copies of $\PP^1$ glued at that point, which is 2. For 3, step 5 of @thm:coble-smooth-antibicanonical-is-a-plane-blowup gives $\mult_{p_i}Z=C\cdot E_i=2$. The local branches of $Z$ at $p_i$ correspond to the points of $C\cap E_i$. Two distinct points give two smooth branches with distinct tangent directions, hence an ordinary node. In case 2, $C$ is smooth and meets $E_i$ in one point with multiplicity two, so the double point is an ordinary cusp: a higher $A_{2k}$ singularity ($k>1$) would remain singular after one blow-up.
:::

::: {.lemma #lem:coble-negative-curves title="The irreducible curves of negative square"}

Let $S$ be as in @thm:coble-smooth-antibicanonical-is-a-plane-blowup. An irreducible curve $D\subset S$ with $D^2<0$ is $C$, or a $(-1)$-curve with $D\cdot C=2$, or a $(-2)$-curve with $D\intersect C=\emptyset$ [@CD12, Lemma 2.1(2)]. If $\pi\colon S\to\PP^2$ is a birational morphism and a centre $p_j$ of $\pi$ lies on the strict transform of the exceptional curve of an earlier centre $p_i$, then the strict transform in $S$ of the exceptional curve of $p_i$ is a $(-2)$-curve.
:::

::: {.proof}

Let $D\neq C$. Then $D\cdot C\geq0$, so $D\cdot K_S\leq0$, and $2\pa(D)-2=D^2+D\cdot K_S<0$ gives $\pa(D)=0$ and $D^2+D\cdot K_S=-2$. So $D$ is a smooth rational curve with $(D^2,D\cdot K_S)$ equal to $(-1,-1)$ or $(-2,0)$, and $D\cdot C=-2D\cdot K_S$ is $2$ or $0$. The strict transform $R$ of the exceptional curve of $p_i$ is a smooth rational curve with $R^2\leq-2$, and $R\neq C$ because $\pi$ contracts $R$ and does not contract $C$.
:::

::: {.proposition #prop:coble-plane-models-are-double-point-sextics title="The plane models are the irreducible rational sextics whose singular points are double points"}

1. Let $S$ be as in @thm:coble-smooth-antibicanonical-is-a-plane-blowup, and let $\pi\colon S\to\PP^2$ be a birational morphism with centres $p_1,\dots,p_{10}$, the point $p_i$ lying on the surface $S_{i-1}$ obtained from $S_0=\PP^2$ by blowing up $p_1,\dots,p_{i-1}$. Let $C_i\subset S_i$ be the image of $C$, so that $C_0=Z=\pi(C)$. Then $\mult_{p_i}C_{i-1}=2$ for every $i$, and $p_1,\dots,p_{10}$ are all the singular points of $C_0,\dots,C_9$. So every singular point of $Z$ is a double point all of whose infinitely near singular points are double points, that is, a singularity of type $A_k$, and $\tsum_{x\in\Sing Z}\delta(Z,x)=10$.
2. Let $Z\subset\PP^2$ be an irreducible rational sextic whose singular points, the infinitely near ones included, are double points, and let $S_Z\to\PP^2$ be the composite of the blow-ups at the singular points of $Z$ and of its successive strict transforms. Then $S_Z$ is a blow-up of $\PP^2$ at ten points, the strict transform $C$ of $Z$ is a smooth rational curve, $\abs{-2K_{S_Z}}=\theset{C}$ and $\abs{-K_{S_Z}}=\emptyset$. So $S_Z$, with the double cover branched along $C$ and its involution, is an object of $\mcM_\Co$ over $\CC$ (@def:coble-moduli-functor).
:::

::: {.proof}

*1.* Let $E_i\subset S$ be the total transform of the exceptional curve of $p_i$ and $m_i\definedas\mult_{p_i}C_{i-1}$. Each blow-up subtracts $m_i$ times the exceptional curve from the total transform of $C_{i-1}$, so $[C]=6H-\tsum_im_iE_i$ in $\Pic(S)=\ZZ H\oplus\bigoplus_i\ZZ E_i$. By @thm:coble-smooth-antibicanonical-is-a-plane-blowup(2), whose step *5* uses only that $\pi$ is a birational morphism onto $\PP^2$, $[C]=6H-2\tsum_iE_i$; hence $m_i=2$. A singular point of some $C_i$ that is not a later centre has a neighbourhood mapped isomorphically from $S$, and $C$ is smooth; so every singular point of every $C_i$ is a centre. The count is @thm:coble-smooth-antibicanonical-is-a-plane-blowup(3).

*2.* A blow-up at a double point of a reduced curve lowers its $\delta$-invariant by $1$, and $\delta(Z)=\pa(Z)-0=10$ because $Z$ is a rational sextic. So the process ends after ten blow-ups, with $C$ smooth, and $[C]=6H-2\tsum_{i=1}^{10}E_i=-2K_{S_Z}$ (@prop:canonical-class-of-blowup). Then $C^2=36-40=-4$, and an irreducible curve of negative square is the only effective divisor in its class, so $\abs{-2K_{S_Z}}=\theset{C}$. If $D\in\abs{-K_{S_Z}}$ then $2D=C$, and $C$ is reduced; so $\abs{-K_{S_Z}}=\emptyset$. The surface $S_Z$ is nonsingular, projective and rational, so it is a Coble surface [@DZ99, Introduction] with $\abs{-2K}$ one connected smooth curve; the cover is that of @def:coble-moduli-functor(2), and it is a $\mathrm{K3}$ surface because $C$ is smooth (@lem:dz-k3-type-double-cover).
:::

::: {.example #ex:coble-sextics-with-an-a15-point title="Two sextics with an $A_{15}$ point: infinitely near centres, and a cusp"}

Put $w_1=y^2z-x^3-3xz^2+4z^3$ and $w_2=y^2z-x^3+15xz^2-22z^3$, and let
$$
Z_8\colon\ w_1^2+8z^3\qty(w_1+6(x-z)z^2)=0,\qquad
Z_{64}\colon\ w_2^2+64z^3\qty(w_2-3(x-2z)z^2)=0 .
$$
Both are irreducible rational sextics. The singular points of $Z_8$ are $o=(0:1:0)$, of type $A_{15}$, and the ordinary nodes $(1:0:1)$ and $(0:0:1)$. The singular points of $Z_{64}$ are $o$, of type $A_{15}$, the ordinary node $(2:0:1)$ and the ordinary cusp $(-3:0:1)$. By @prop:coble-plane-models-are-double-point-sextics(2) the surfaces $S_{Z_8}$ and $S_{Z_{64}}$ are objects of $\mcM_\Co$ over $\CC$. Eight of the ten centres of each are $o=p^{(1)}$ and points $p^{(2)},\dots,p^{(8)}$ with $p^{(i+1)}$ on the exceptional curve of $p^{(i)}$ and on the strict transform of no earlier one; and the exceptional curve of $S_{Z_{64}}$ over $(-3:0:1)$ meets $C$ in one point, with multiplicity $2$ (@lem:coble-double-point-of-the-sextic(2)--(3)).

On each of the two surfaces let $R_i$, $1\leq i\leq7$, be the strict transform of the exceptional curve of $p^{(i)}$, and $L$ the strict transform of the line $z=0$. Their classes are $[R_i]=E_i-E_{i+1}$ and $[L]=H-E_1-E_2-E_3$, they are $(-2)$-curves, and their only nonzero intersection numbers are $R_i\cdot R_{i+1}=1$ and $L\cdot R_3=1$: the dual graph is the Dynkin diagram $E_8$.

*Verification.* In the chart $z=1$ write $w=y^2-p(x)$, with $p=x^3+3x-4$ and $(x_0,c,t)=(1,6,8)$ for $Z_8$, and $p=x^3-15x+22$ and $(x_0,c,t)=(2,-3,64)$ for $Z_{64}$. In both cases $p(x_0)=0$, $c=p'(x_0)$, and the equation is $w^2+t\qty(w+c(x-x_0))=0$. On the curve $x=x_0-w(w+t)/(tc)$, so $(x,y)\mapsto(w,y)$ is an isomorphism of the affine curve onto $\theset{y^2=P(w)}$ with $P(w)=w+p\qty(x_0-w(w+t)/(tc))$, and expansion gives
$$
P_8(w)=-48^{-3}\,w^2(w-4)^2\qty(w^2+32w+288),\qquad
P_{64}(w)=192^{-3}\,w^2(w+40)^3(w+72).
$$
Neither polynomial is a square, so each affine curve is irreducible, and it is birational to a conic, $u^2=-48^{-3}(w^2+32w+288)$ and $u^2=192^{-3}(w+40)(w+72)$, hence rational. Its singular points are the multiple roots of $P$: for $Z_8$ the nodes $w=0$ and $w=4$, which are $(x,y)=(1,0)$ and $(0,0)$; for $Z_{64}$ the node $w=0$, which is $(2,0)$, and the cusp $w=-40$, where $P$ has a triple root, which is $(-3,0)$. Each curve meets the line $z=0$ only at $o$, where the equation restricts to $x^6$, so $z=0$ is not a component; together with irreducibility of the affine curve, this proves that the projective sextic is irreducible. In the chart $y=1$ its term of lowest degree at $o$ is $z^2$, so $o$ is a double point. An irreducible rational sextic has $\tsum\delta=10$, so $\delta(o)=8$, and $o$ has two branches, the two points at infinity of the conic; a double point with two branches and $\delta=8$ is $A_{15}$. An $A_{15}$ point $\eta^2=\xi^{16}$ is resolved by eight blow-ups, the strict transform after $i<8$ of them having an $A_{15-2i}$ point at the origin of the chart $\eta=\xi^i\eta_i$, which lies on the last exceptional curve $\theset{\xi=0}$ and not on the strict transform of the one before; that is the statement on $p^{(1)},\dots,p^{(8)}$, and it gives $[R_i]=E_i-E_{i+1}$. The line $z=0$ meets $Z$ at $o$ with multiplicity $6$ and nowhere else. A blow-up at a point of multiplicity $1$ on the line and $2$ on the curve lowers their intersection number by $2$, and the strict transform of $Z$ meets the exceptional curve of $p^{(i)}$ only at $p^{(i+1)}$; so the strict transforms of the line pass through $p^{(1)},p^{(2)},p^{(3)}$, and after the third blow-up they do not meet the strict transform of $Z$, hence not $p^{(4)}$. So $[L]=H-E_1-E_2-E_3$. The intersection numbers follow from $H^2=1$, $E_i^2=-1$.

The Singular run `computations/reports/coble_807-nonclassical-sextics.sing`, recorded in `computations/reports/coble_807-nonclassical-sextics-run.txt`, computes the same data independently: genus $0$, one absolute factor, restriction $x^6$ to the line, and the normal forms $A_{15},A_1,A_1$ for $Z_8$ and $A_{15},A_1,A_2$ for $Z_{64}$.
:::

::: {.lemma #lem:e8-classes-of-roots-modulo-two title="Modulo $2E_8$, every class of square $\equiv2\pmod 4$ contains a root"}

Let $d\in E_8$ with $d^2\equiv2\pmod4$. Then $d=\alpha+2y$ with $\alpha\in E_8$ a root and $y\in E_8$.
:::

::: {.proof}

The form $\bar q_{E_8}$ of @lem:even-unimodular-mod-two-form has $136$ zeros on the $256$ classes of $E_8/2E_8$, so it takes the value $1$ on $120$ classes, and $d$ lies in one of them. A root $\alpha$ has $\bar q_{E_8}(\alpha)=1$. If two roots $\alpha\neq\beta$ are congruent modulo $2E_8$, then $(\alpha-\beta)^2\leq-8$, a nonzero element of $2E_8$ having square at most $-8$, so $\alpha\cdot\beta=-2-\tfrac12(\alpha-\beta)^2\geq2$ and $\beta=-\alpha$ by the Cauchy--Schwarz inequality. So the $240$ roots (@ex:E8-roots) fill $120$ classes, which are all the classes on which $\bar q_{E_8}=1$.
:::

::: {.proposition #prop:coble-e8-configuration-excludes-ten-distinct-centres title="A Coble surface with an $E_8$-configuration of $(-2)$-curves is not a blow-up of ten distinct points"}

Let $S$ be as in @thm:coble-smooth-antibicanonical-is-a-plane-blowup, and suppose that $S$ contains $(-2)$-curves $N_1,\dots,N_8$ whose dual graph is the Dynkin diagram $E_8$. Then $S$ contains no ten pairwise disjoint $(-1)$-curves. In particular no birational morphism $S\to\PP^2$ has ten distinct centres, and $S$ is not classical.
:::

::: {.proof}

*The lattice.* The Gram matrix of the classes $[N_k]$ is the negative of the Cartan matrix of $E_8$, of determinant $1$; so they span an even negative-definite unimodular sublattice $\Lambda\subset\Pic(S)$ of rank $8$, which is $E_8$ (@thm:E8-characterization); so $\Pic(S)=\Lambda\oplus\Lambda^{\perp}$ with $\Lambda^{\perp}$ of rank $3$, and $K_S\in\Lambda^{\perp}$ because $N_k\cdot K_S=0$ (@lem:coble-negative-curves).

*The lift to the cover.* Let $\pi\colon X\to S$ be the double cover branched along $C$, with involution $\iota$. Each $N_k$ is disjoint from $C$ (@lem:coble-negative-curves) and isomorphic to $\PP^1$, so $\pi^{-1}(N_k)$ is the disjoint union of two curves mapped isomorphically to $N_k$ and exchanged by $\iota$. The dual graph is a tree, so the two curves can be named $N_k^+,N_k^-$ with $N_k^+\cdot N_l^+=N_k\cdot N_l$ and $N_k^+\cdot N_l^-=0$ for all $k,l$. For $\lambda=\tsum_ka_k[N_k]\in\Lambda$ put $\lambda^+\definedas\tsum_ka_k[N_k^+]\in\Pic(X)$. Then, for $\lambda,\lambda'\in\Lambda$ and $x\in\Pic(S)$,
$$
\lambda^+\cdot\lambda'^+=\lambda\cdot\lambda',\qquad \lambda^++\iota^*\lambda^+=\pi^*\lambda,\qquad \lambda^+\cdot\pi^*x=\lambda\cdot x,
$$
the last because $\pi^*x\cdot N_k^+=\pi^*x\cdot N_k^-$ and their sum is $\pi^*x\cdot\pi^*N_k=2\,x\cdot N_k$.

*Two congruent classes.* Suppose $E_1,\dots,E_{10}$ are pairwise disjoint $(-1)$-curves, and write $[E_i]=\lambda_i+\mu_i$ with $\lambda_i\in\Lambda$, $\mu_i\in\Lambda^{\perp}$. The map $x\mapsto x\cdot K_S\bmod2$ is a linear form on $\Lambda^{\perp}/2\Lambda^{\perp}\cong\bF_2^3$, and it takes the value $1$ on every $\mu_i$, because $\mu_i\cdot K_S=E_i\cdot K_S=-1$. Its fibre over $1$ has four elements, so there are $i\neq j$ and $\nu\in\Lambda^{\perp}$ with $\mu_i-\mu_j=2\nu$. Put $d\definedas\lambda_i-\lambda_j$. Then $-2=\qty([E_i]-[E_j])^2=d^2+4\nu^2$, so $d^2\equiv2\pmod4$, and by @lem:e8-classes-of-roots-modulo-two $d=\alpha+2y$ with $\alpha$ a root of $\Lambda$ and $y\in\Lambda$. With $x\definedas y+\nu$,
$$
[E_i]-[E_j]=\alpha+2x,\qquad -2=\alpha^2+4\,\alpha\cdot x+4x^2,\quad\text{so}\quad \alpha\cdot x+x^2=0 .
$$

*A class of square $-2$.* Put $\Gamma\definedas\alpha^++\pi^*x\in\Pic(X)$. Then
$$
\Gamma+\iota^*\Gamma=\pi^*\alpha+2\pi^*x=\pi^*\qty([E_i]-[E_j]),\qquad \Gamma^2=\alpha^2+2\,\alpha\cdot x+2x^2=-2 .
$$
By the Riemann--Roch formula $\chi(X,\OO(\Gamma))=\tfrac12\Gamma^2+2=1$ [@Huy16, Ch. 1, (2.5)] and Serre duality, $\Gamma$ or $-\Gamma$ is effective. Exchanging $i$ and $j$ replaces $(\alpha,x,\Gamma)$ by $(-\alpha,-x,-\Gamma)$, so let $\Gamma$ be the class of an effective divisor $G$. Then $\pi^*E_j+G+\iota^*G$ is an effective divisor linearly equivalent to $\pi^*E_i$. Push forward by $\pi$: this sends $\operatorname{div}(g)$ to the divisor of the norm of $g$, and $\pi_*\pi^*=2$ on divisors, so $2E_j+2\pi_*G$ is linearly equivalent to $2E_i$, and $E_j+\pi_*G$ to $E_i$ because $\Pic(S)$ is torsion free. The curve $E_i$ is irreducible of negative square, hence the only effective divisor in its class; so $E_j+\pi_*G=E_i$ as divisors, which is false for two distinct prime divisors $E_i,E_j$.

*The plane models.* The exceptional curves of a birational morphism $S\to\PP^2$ with ten distinct centres are ten pairwise disjoint $(-1)$-curves, and a classical $S$ has such a morphism.
:::

::: {.theorem #thm:coble-classical-substack-is-open-dense-and-proper title="The classical substack is open and dense in $\mcM_\Co$, and it is not all of $\mcM_\Co$"}

Let $S$ be an object of $\mcM_\Co$ over $\CC$, with cover $\pi\colon X\to S$, involution $\iota$ and anti-bicanonical curve $C$, and put $\Pic(X)^-\definedas\theset{x\in\Pic(X)\st\iota^*x=-x}$. Let $\mcN$ be the class of objects that contain a $(-2)$-curve, $\mcT$ the class of objects that contain a $(-1)$-curve meeting $C$ in one point, and $\mcH$ the class of objects for which $\Pic(X)^-$ contains a class of square $-4$ or $-6$.

1. $\mcN\union\mcT\subseteq\mcH$, and for $S\notin\mcN\union\mcT$ every birational morphism $S\to\PP^2$ is the blow-up of the ten ordinary nodes, at ten distinct points, of an irreducible sextic. So
$$\mcM_\Co\sm\mcH\ \subseteq\ \mcM_\Co\sm(\mcN\union\mcT)\ \subseteq\ \mcM^{\mathrm{cl}}_\Co ,$$
and an object with $\Pic(X)^-=0$ is classical in each of its plane presentations.
2. *Open.* In every family of objects of $\mcM_\Co$ the classical fibres form an open subset of the base.
3. *Dense.* Every object $S_0$ is the fibre over $0$ of a holomorphic family of objects of $\mcM_\Co$ over a neighbourhood $U$ of $0$ in $\CC^9$ whose period map is an open embedding $U\to\Omega_{T_\Co}$ (@def:type-iv-period-domain). In $U$ the fibres in $\mcH$ form a locally finite union of proper closed analytic hypersurfaces, and the fibres with $\Pic(X)^-=0$ are dense. So the classical fibres form an open dense subset of $U$.
4. *Proper.* The object $S_{Z_8}$ of @ex:coble-sextics-with-an-a15-point is not classical, and neither is $S_{Z_{64}}$.

Consequently $\mcM^{\mathrm{cl}}_\Co$ is an open dense substack of $\mcM_\Co$ and $\mcM^{\mathrm{cl}}_\Co\neq\mcM_\Co$. Every object of $\mcM_\Co$ is a limit of classical objects, so $\mcM_\Co$ has no connected or irreducible component other than the closure of $\mcM^{\mathrm{cl}}_\Co$, and $\mcM_\Co$ is connected because $\mcM^{\mathrm{cl}}_\Co$ is (@prop:coble-stack-smooth-connected(2)).
:::

::: {.proof}

*1.* A $(-2)$-curve $N\subset S$ is disjoint from $C$ (@lem:coble-negative-curves), so $\pi^{-1}(N)=N^+\sqcup N^-$ with $\iota(N^+)=N^-$, and $\delta\definedas[N^+]-[N^-]\in\Pic(X)^-$ has $\delta^2=-2-2-0=-4$. If a $(-1)$-curve $E$ meets $C$ in one point, then $\pi^{-1}(E)=E'\union E''$ with $E',E''$ two $(-2)$-curves meeting in one point (@lem:coble-double-point-of-the-sextic(2)); $\iota$ acts on $\pi^{-1}(E)$ as the covering involution of $\pi^{-1}(E)\to E$, which exchanges $E'$ and $E''$, so $\delta\definedas[E']-[E'']\in\Pic(X)^-$ has $\delta^2=-2-2-2=-6$. Hence $\mcN\union\mcT\subseteq\mcH$. Let $S\notin\mcN\union\mcT$ and let $\pi_0\colon S\to\PP^2$ be a birational morphism; one exists by @thm:coble-smooth-antibicanonical-is-a-plane-blowup(2). Its centres are distinct points of $\PP^2$, by the second statement of @lem:coble-negative-curves; so its ten exceptional curves are $(-1)$-curves, each meets $C$ in two distinct points because $S\notin\mcT$, and $\pi_0(C)$ has ten ordinary nodes and no other singular point (@lem:coble-double-point-of-the-sextic(3), @thm:coble-smooth-antibicanonical-is-a-plane-blowup(3)).

*2.* Let a family of $\mcM_\Co$ have a classical fibre $S_b=\Bl_{p_1,\dots,p_{10}}\PP^2$. The $\PGL_3$-stabilizer of $(p_1,\dots,p_{10})$ is trivial (@lem:d2-plane-sextic-freeness(2)), so the family of blow-ups of $\PP^2$ over the configuration space of ordered, possibly infinitely near, ten-tuples is a complete deformation of $S_b$ [@Gri18, Prop. 3.1]: near $b$ the family of surfaces is its pullback along a map to that configuration space. Ten distinct points form an open subset of it, so on the nearby fibres the ten centres are distinct; the anti-bicanonical curve is the strict transform of a sextic with a double point at each centre, and the ten Hessians, nonzero at $b$, stay nonzero. This is the argument of the proof of @prop:coble-stack-as-quotient.

*3.* Let $\mathcal X\to\operatorname{Def}(X_0)$ be the universal deformation of the cover $X_0$ of $S_0$; its base is smooth of dimension $20$ [@Huy16, Ch. 6, Cor. 2.7], and its period map $\mathcal P\colon\operatorname{Def}(X_0)\to D\subset\PP\qty(H^2(X_0,\CC))$ is a local isomorphism [@Huy16, Ch. 6, Prop. 2.8]. The automorphism $\iota_0$ acts on $\mathcal X\to\operatorname{Def}(X_0)$ [@Huy16, Ch. 6, Rem. 2.6], and $\mathcal P$ intertwines its action on the base with $\iota_0^*$ on $D$. The fixed locus of $\iota_0^*$ on $\PP\qty(H^2(X_0,\CC))$ is $\PP(M_\CC)\sqcup\PP\qty((T_\Co)_\CC)$, and $\mathcal P(0)=H^{2,0}(X_0)\in\PP\qty((T_\Co)_\CC)$. The fixed locus $U\subset\operatorname{Def}(X_0)$ of the holomorphic involution $\iota_0$ is a complex submanifold. Its tangent space is the $(+1)$-eigenspace of $d\iota_0$; since $\mathcal P$ is $\iota_0$-equivariant and $d\mathcal P_0$ is an isomorphism, $d\mathcal P_0$ identifies this tangent space with the tangent space of $D\intersect\PP\qty((T_\Co)_\CC)=\Omega_{T_\Co}$. The latter has dimension $9$, so $d(\mathcal P|_U)_0$ is an isomorphism, and after shrinking, $\mathcal P|_U$ maps $U$ isomorphically onto an open subset of $\Omega_{T_\Co}$. Over $U$ the action of $\iota_0$ is an involution $\iota_u$ of each fibre $X_u$, with $\iota_u^*=\iota_0^*=\id_M\oplus(-\id_{T_\Co})$ under the transport of $H^2$. By @thm:coble-period-surjectivity(4), applied to $X_u$ with the marking by transport and the automorphism $\iota_u$, the conclusions (1)--(3) of that theorem hold: $\Fix(\iota_u)$ is one smooth rational curve and $S_u\definedas X_u/\iota_u$ is an object of $\mcM_\Co$ over $\CC$. The relative quotient construction of @rmk:marked-coble-covers-after-huybrechts makes these quotients, their double covers and their involutions a family of objects of @def:coble-moduli-functor over $U$.

A class $\ell\in H^2(X_0,\ZZ)$ is of type $(1,1)$ on $X_u$ if and only if $\mathcal P(u)\in\ell^{\perp}$ [@Huy16, Ch. 6, §2.4], so $\Pic(X_u)^-=T_\Co\intersect\mathcal P(u)^{\perp}$. Hence the fibres in $\mcH$ are those with $\mathcal P(u)\in\delta^{\perp}$ for some $\delta\in T_\Co$ with $\delta^2\in\theset{-4,-6}$. Each $\delta^{\perp}\intersect\Omega_{T_\Co}$ is a proper closed analytic hypersurface, the quadric $\omega^2=0$ of $\PP\qty((T_\Co)_\CC)$ being irreducible and not contained in a hyperplane, and the union is locally finite by the argument of @prop:the-coble-locus-in-the-period-domain(1), which uses only that the squares of the classes are bounded. The fibres with $\Pic(X_u)^-\neq0$ lie on the countably many hypersurfaces $\ell^{\perp}$, $0\neq\ell\in T_\Co$, whose complement is dense by the Baire category theorem. The last sentence is 1 and 2.

*4.* By @ex:coble-sextics-with-an-a15-point both surfaces contain eight $(-2)$-curves with dual graph $E_8$; apply @prop:coble-e8-configuration-excludes-ten-distinct-centres.

*The consequences.* Openness is 2. For density and for the limits, 3 gives for every object $S_0$ a family through $S_0$ whose classical fibres are dense. In particular $S_0$ is joined to a classical object by a path in $U$; @lem:d2-incidence-connected(3) makes the classical locus path connected, so $\mcM_\Co$ is path connected. Moreover @lem:d2-incidence-connected(3) makes the classical locus irreducible as well. Its closure is therefore irreducible. Density makes that closure all of $\mcM_\Co$, so there is no further connected or irreducible component.
:::

::: {.remark #rmk:coble-widened-family-source-scope title="Dolgachev--Zhang §6 and the decision for the whole widened family"}
The source hypotheses, the answer to research#807, and the remaining monodromy question are distinct.

1. *The smooth-member hypothesis is the reduced, $\mathrm{K3}$-type case.* In the notation of @thm:coble-smooth-antibicanonical-is-a-plane-blowup, $C$ is reduced, so $S$ is of $\mathrm{K3}$-type by [@DZ99, Definition 6.1], and @lem:dz-k3-type-double-cover records the normal $\mathrm{K3}$ double cover of [@DZ99, Lemma 6.2]; here that cover is smooth. Moreover $C$ is a single smooth $(-4)$-curve, so $S$ is terminal by the converse in [@DZ99, Proposition 6.4(2)]. [@DZ99, Theorem 6.3] excludes rational type, and [@DZ99, Theorem 4.3] makes an elliptic-type Coble surface basic. This is the exact reduction behind @thm:coble-smooth-antibicanonical-is-a-plane-blowup; it does not make the ten centres distinct or their double points ordinary nodes.
2. *What §6.5--§6.7 do and do not decide.* [@DZ99, Theorem 6.5] is a fibre-type criterion for $\mathrm{K3}$-type, and [@DZ99, Theorem 6.6] constructs a non-minimal rational Jacobian elliptic double cover in a non-$\mathrm{K3}$-type case, not a $\mathrm{K3}$ cover. [@DZ99, Theorem 6.7] assumes over $\CC$ an elliptic, terminal, $\mathrm{K3}$-type surface which is general in the further sense that every divisor class on its $\mathrm{K3}$ cover is invariant under the covering involution; its conclusion is finiteness of the $\Aut(S)$-orbits of negative rational curves. It is not a plane-model or connected-component theorem. The non-classical objects established here do not satisfy that generality hypothesis: each has a nonzero anti-invariant divisor class coming from a $(-2)$-curve (part 1 of the proof of @thm:coble-classical-substack-is-open-dense-and-proper).
3. *The later example is outside the question, for a stated reason.* In [@DZ99, Example 6.10] the unique anti-bicanonical divisor is
   $$R_1+R_2+R_3+R_4+2R_5,$$
   which is non-reduced, although the anti-bicanonical system is nonempty. Its $I_0^*$ fibre also places it on the non-$\mathrm{K3}$-type side of [@DZ99, Theorem 6.5]. Thus its infinitely many automorphism-orbits of $(-1)$-curves do not produce an object of @def:coble-moduli-functor. The distinctions matter: an empty system is already excluded by the definition of a Coble surface; a reduced but non-smooth member can be of $\mathrm{K3}$-type but fails the smoothness hypothesis here; and a system whose only member is non-reduced fails both that hypothesis and, by [@DZ99, Definition 6.1], the $\mathrm{K3}$-type hypothesis.
4. *The decision.* @thm:coble-smooth-antibicanonical-is-a-plane-blowup and @prop:coble-plane-models-are-double-point-sextics describe every admitted surface by ten double-point blow-ups, infinitely near centres included. @ex:coble-sextics-with-an-a15-point and @prop:coble-e8-configuration-excludes-ten-distinct-centres then prove that $S_{Z_8}$ and $S_{Z_{64}}$ are admitted but have no presentation as the blow-up of $\PP^2$ at ten distinct ordinary nodes of an irreducible sextic. On the other hand @thm:coble-classical-substack-is-open-dense-and-proper proves that the classical objects form an open, dense, connected substack strictly smaller than $\mcM_\Co$: openness uses the stabilizer-freeness of @lem:d2-plane-sextic-freeness(2) and the complete deformation of [@Gri18, Proposition 3.1], density uses the fixed-involution deformation and the Noether--Lefschetz hypersurfaces, and connectedness and irreducibility of the classical locus use smoothness of $U_{6,0}$ and the full symmetric monodromy on its nodes [@HM98, Theorem (1.49)(1); @HM98, §6.E, *Initial reductions*; @HM98, (6.45)]. So **non-classical objects exist, but they form no further connected or irreducible component**. The issue's all-classical-or-new-component dichotomy is therefore false; $\mcM_\Co$ is not identified with its classical quotient.
5. *Monodromy.* Since there is no additional component, there is no additional component whose monodromy remains to be determined. Independently, @cor:coble-monodromy-on-m-of-the-whole-stack(1) computes the aggregate generated by transports in families and isomorphisms of objects on the **invariant** lattice to be $W(E_{10})$ without identifying it with universal-stack monodromy. Its stack-local-system conclusion is explicitly conditional on its chart hypothesis (A). Nothing here determines $\Gamma_\Co$ on the **anti-invariant** lattice or substitutes a plane-model automorphism group for the monodromy of the cover-retaining stack.
:::

::: {.lemma #lem:coble-canonical-class-and-ample-component-in-families title="Transport in a family of Coble covers carries the canonical class to the canonical class and the ample component to the ample component"}

For an object $(S,\ \pi\colon X\to S,\ \iota)$ of $\mcM_\Co$ over $\CC$ put

## Supporting local finiteness


*What this would give for (iii), and what it does not.* With 1--4 and pseudo-ampleness --- the step clause 3 records as open --- [@Dol96, Thm. 3.1] would give that the period map of *marked pseudo-ample* $M$-polarized $\mathrm{K3}$ surfaces is **surjective** onto $\bD(T_\Co)$, with fibre over $\pi$ in bijection with $W_\pi(N)$; the theorem is recorded as false as stated at @rmk:coble-period-surjectivity-sources, and the replacement used below is @thm:coble-period-surjectivity. That would be a statement about the ambient moduli, and it is exactly what would make the passage to an open set unnecessary *there*: the image would be everything. It would **not** give the same for the Coble subfamily: the D2a family is a subfamily, so what would follow is that $\bD(T_\Co)$ is exhausted by pseudo-ample $M$-polarized $\mathrm{K3}$ surfaces and that the complement of the Coble period image is the image of the pseudo-ample points that are not Coble covers. Whether that complement is a proper closed *analytic* subset -- what finding (iii) needs for connectedness -- is therefore the same reconstruction question as before, not a consequence of the theorem. What the theorem would remove is the *openness* half of (iii): since the ambient image would be all of $\bD(T_\Co)$, the Coble image would be the complement of a subset of the discriminant, and its openness is [@DK13, Prop. 3.2] read on the quotient.

::: {.remark #rmk:where-the-sign-is-a-loop title="Reconciling `thm:no-loop-carries-the-sign` with $-\id\in\Gamma_\Co(B)$: they are two moduli problems"}
Two theorems of the volume, both proved, appear to disagree about the sign, and the reconciliation is that they concern different moduli problems -- which is finding (iv) again.

- @thm:coble-block-sign-in-w proves $-\id_{T_\Co}\in W(T_\Co)$, the reflection group generated by the $(-2)$-vectors; @lem:d2-vanishing-reflections(4) proves $W(T_\Co)\subseteq\Gamma_\Co(B)$, the meridians of the nodal degenerations being the reflections (Picard--Lefschetz, [@Voi07, Thm. 3.16]). Composing the two, $-\id\in\Gamma_\Co(B)$ for the labelled presentation of @def:coble-family-unpolarized, and its monodromy is carried by *loops*: the meridian about a nodal divisor is a loop of the base.
- @thm:no-loop-carries-the-sign says that over the coarse moduli space of *labelled direct, polarized* Coble data the monodromy is $\Gamma^{\mathrm{dir}}_{\Co,2}/\{\pm\id\}$: no loop carries $\iota$.

These are consistent only because the objects differ: the first is the unpolarized family over the base $B=V/\PGL_3$, the second the degree-$2$ polarized construction, and the map between them is not an isomorphism of local systems. The consequence for this page is that the phrase "the loop monodromy is an index-two subgroup" is *not* available for the unpolarized family: there the sign is a reflection word, hence a loop, and no index-two gap is asserted. The stabilizer comparison @qst:coble-monodromy-equality is false (@prop:coble-monodromy-equality-false); that negative answer does not settle the sign question for the two moduli problems.
:::

::: {.proposition #prop:the-coble-locus-in-the-period-domain title="Which pseudo-ample $M$-polarized $\mathrm{K3}$ surfaces are Coble covers, and why the bad locus is a closed analytic subset"}
Let $\bD=\bD(T_\Co)^+$, let $\Delta(T_\Co)=\theset{\delta\in T_\Co:\delta^2=-2}$, and let
$$Z\definedas\bigcup_{\delta\in\Delta(T_\Co)}\qty(H_\delta\intersect\bD),\qquad H_\delta=\theset{\pi\in\bD:\delta\perp\pi}.$$
Then:

1. $Z$ is a closed analytic subset of $\bD$, locally finite: every compact $K\subset\bD$ meets $H_\delta$ for only finitely many $\delta\in\Delta(T_\Co)$.
2. For $\pi\in\bD\sm Z$ the marked surface (@def:flower-pot-degeneration) $X_\pi$ is a labelled Coble cover.
3. For $\pi\in Z$ the marked surface $X_\pi$ is *not* a Coble cover: the class $\delta$ is algebraic of type $(1,1)$ on $X_\pi$ and $\sigma=\id_M\oplus(-\id_{T_\Co})$ acts on it as $-1$, so $\sigma$ is not an automorphism.
4. Hence the locus of periods realised by *some* Coble cover is exactly $\bD\sm Z$; it is open, and it is connected. This is a statement about the period domain. It is **not** a statement about the base $B$ of the D2a family, which is the complement of a strictly larger arrangement; see @rmk:two-arrangements-two-bases.
:::

::: {.proof}
1. *Local finiteness.* Let $K\subset\bD$ be compact. A period in $K$ is a positive $2$-plane, and the family of these is bounded; choose $\pi_0\in\bD$ and let $\beta$ be the positive definite form $\beta(x)=-(x,x)_{\pi_0^{\perp}}+(x,x)_{\pi_0}$ on $T_\Co\otimes\RR$. On the compact $K$ the forms $\beta_\pi$ obtained by replacing $\pi_0$ by $\pi$ are uniformly equivalent to $\beta$: there is $c>0$ with $c^{-1}\beta\le\beta_\pi\le c\beta$ for all $\pi\in K$. If $\delta\perp\pi$ then $\delta\in\pi^{\perp}$, so $\beta_\pi(\delta)=-|\delta|^2$ and the uniform equivalence gives $\beta(\delta)\le c\,\beta_\pi(\delta)=c\abs{\delta}^2$. Since $\Delta(T_\Co)$ is discrete in $T_\Co\otimes\RR$ and $\beta$ is positive definite, the set of $\delta$ with $\beta(\delta)$ bounded is finite. So only finitely many hyperplanes meet $K$, and $Z$ is closed and analytic.
2. This is @thm:coble-period-surjectivity: for $\pi\notin Z$ a marking with period $\pi$ exists for which $\sigma$ is induced by an involution, its fixed locus is one smooth rational curve, and the quotient is a Coble surface whose anti-bicanonical system is a single smooth curve, with $X$ as its double cover. The marking is one whose Kähler chamber meets $M\tensor\RR$ (@thm:coble-period-surjectivity(4)); a $(-2)$-class of $\pi^{\perp}$ need not lie in $M$, and the proof does not use that. Here *labelled* means that the surface carries the isometry $\restrictionof{\varphi^{-1}}{M}$ of $M$ onto its invariant lattice; the theorem does not show that the ten classes $e_1,\dots,e_{10}$ are the classes of exceptional curves of a plane model (@rmk:coble-period-surjectivity-sources).
3. If $\pi\in H_\delta$ then $\delta\in(\pi^{\perp}\intersect T_\Co)$ is of type $(1,1)$, hence algebraic on $X_\pi$; $\sigma$ acts on it as $-1$. An automorphism of a $\mathrm{K3}$ surface preserves the effective cone, but $\delta$ and $-\delta$ cannot both be effective for $\delta^2=-2$, so a $\sigma$ realising the isometry would send an effective class to an anti-effective one, which no automorphism does. So $\sigma$ is not an automorphism and $X_\pi$ is not a Coble cover.
4. is 2 and 3 together. Connectedness is the argument of @thm:gamma-co-is-full: $Z$ is a proper closed analytic subset, a ball minus a proper analytic subset is connected, and a path meeting $Z$ can be diverted inside such a ball.
:::


## Monodromy boundary

::: {.corollary #cor:coble-monodromy-on-m-of-the-whole-stack title="On $\mcM_\Co$ the transports of the invariant lattice generate $W(E_{10})$; this is the monodromy group of the stack conditional on a chart"}

Use the notation of @lem:coble-canonical-class-and-ample-component-in-families. Let $x$ be a classical object over $\CC$, the fibre over a point $s\in B$ of the family of @lem:d2-unpolarised-family(3), and identify $M_x$ with $M=\generators{e_0,\dots,e_{10}}$ by the plane frame at $s$, as in @thm:coble-monodromy-on-m-classical; put $K=-3e_0+\tsum_ie_i$. Let $\mathcal T_x\subseteq\Orth(M_x)$ be the set of the composites
$$M_x=M_{x_0}\too M_{x_1}\too\cdots\too M_{x_n}=M_x$$
of isometries of the following two kinds, between the invariant lattices of objects $x_0,\dots,x_n$ of $\mcM_\Co$ over $\CC$: the transport, along a path of the base, of the system $\bM$ of a family of objects of $\mcM_\Co$ over an arcwise connected, locally simply connected complex space (@lem:coble-invariant-lattice-in-families(1)); and the isometry induced by an isomorphism of objects over $\CC$. The set $\mathcal T_x$ is a subgroup of $\Orth(M_x)$: the inverse of a transport is the transport along the reversed path, and the inverse of the isometry of an isomorphism is the isometry of the inverse isomorphism.

1. *Families and isomorphisms, without a stack.* $\mathcal T_x=G_x$, and the plane frame identifies it with
$$\Stab_{\Orth(M)}(K)\intersect\Orth^+(M)\cong\Orth^+\qty(K^{\perp M})=W(E_{10}) .$$
The transports of the family over $B$ and the isomorphisms between its fibres already generate this group. In particular the monodromy group on the invariant lattice of every family of objects of $\mcM_\Co$ over an arcwise connected, locally simply connected complex space, classical or not, is contained in $W(E_{10})$. This clause uses no local system on a stack and no descent.

For the stack $\mcM_\Co$ assume the chart hypothesis (A); the descent formerly listed beside it as (D) is proved below.

(A) The stack $\mcM_\Co$ has a chart $p\colon X\to\mcM_\Co$ by a locally simply connected complex space $X$, the map $p$ being a family of objects over $X$, for which the hypotheses of @not:paths-of-a-groupoid-quotient hold; so $\pi_1(\mcM_\Co,x)$ is defined and @lem:g-paths-exhaust-the-fundamental-groupoid applies to $p$.

The descent formerly called hypothesis (D) is supplied by @thm:quotient-local-system-descent(1). Indeed, with $R=X\times_{\mcM_\Co}X$, the system $\bM_p$ on $X$ and the isometries induced by isomorphisms of families form an $R$-equivariant local system: the comparison along a $2$-morphism is the isometry induced by the underlying isomorphism, and its cocycle condition is functoriality on invariant lattices. Descent gives one local system of lattices $\bM$ on $\mcM_\Co$. For $f\colon Y\to\mcM_\Co$, the pullback groupoid $R_f=Y\times_{\mcM_\Co}R$ has one system obtained by pulling back $\bM_p$ from $X$, and base naturality in @thm:quotient-local-system-descent(1) identifies the descent of that system with $f^*\bM$; that system is exactly $\bM_f$, so $f^*\bM=\bM_f$ by the canonical comparison. So, in the notation of @not:paths-of-a-groupoid-quotient, the transport of $\bM$ along $[f\alpha]$, for a path $\alpha$ of $Y$, is the transport of $\bM_f$ along $\alpha$, because both are the transport of the same system on $Y$ after pullback along $\alpha$; and the transport of $\bM$ along $[\rho]$ is the isometry induced by $\rho$, because $\rho$ is already an arrow of $R$, and the action of its image under the groupoid comparison is the $R$-action of $\bM_p$.

Hypothesis (A) belongs to research#797, item 1: the volume constructs a chart for $\mcM^{\mathrm{cl}}_\Co$ only (@prop:coble-stack-as-quotient), and the algebraicity of $\mcM_\Co$ is open (@rmk:stacks-line-by-line(6)). Clause 2 is conditional on (A), and clause 3 on (A).

2. *The stack.* Under (A), the monodromy group of $\bM$ on $\mcM_\Co$ at $x$ is $\mathcal T_x$:
$$\operatorname{Mon}_{\mcM_\Co}(\bM)=W(E_{10}) .$$
This is the group that @thm:coble-monodromy-on-m-classical computes on the classical substack.
3. $\mcM_\Co\sm\mcH$ is an open substack contained in $\mcM^{\mathrm{cl}}_\Co$ whose complement is, in the period coordinates of @thm:coble-classical-substack-is-open-dense-and-proper(3), a locally finite union of proper closed analytic hypersurfaces. So @prop:the-generic-locus-sees-the-whole-group applies to it, and under (A) and the hypotheses of that proposition $\pi_1\qty(\mcM^{\mathrm{cl}}_\Co)\to\pi_1\qty(\mcM_\Co)$ is onto.
:::

::: {.proof}

*1.* Each step of a composite carries the class $\kappa$ and the component $C$ of its source to those of its target (@lem:coble-canonical-class-and-ample-component-in-families(3)--(4)); so the composite fixes $\kappa_x$ and $C_x$, that is $\mathcal T_x\subseteq G_x$, and the plane frame identifies $G_x$ with the displayed groups (@lem:coble-canonical-class-and-ample-component-in-families(2)). For the other inclusion let $r=(g,\tilde g)\colon b\to b'$ be a point of the groupoid $R_B$, an isomorphism between the fibres over $b$ and $b'$ of the family over $B$ (@lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(1)). The base $B$ is path connected (@lem:d2-incidence-connected(3)), and the transport of the system $\bM$ of the family over $B$ along every path of $B$ is the identity in the global frame $\varepsilon_0,\dots,\varepsilon_{10}$ (@lem:coble-invariant-lattice-in-families(2)). So the composite of the transport along a path of $B$ from $s$ to $b$, the isometry of $r$, and the transport along a path of $B$ from $b'$ to $s$ is, in that frame, the matrix $m(r)$ of @lem:transport-order-on-the-classical-coble-stack, and $m(r)\in\mathcal T_x$. The reflections $s_{\delta_1},\dots,s_{\delta_9}$ are the matrices $m(r)$ of the relabelling arrows of the transpositions $(i\ i+1)$, and $s_{\delta_c}$ is, up to a relabelling, the matrix $m(r)$ of the arrow that the quadratic Cremona transformation of three nodes defines at a general point of $B$ (@lem:cremona-second-plane-model-general, @lem:coble-image-on-m-is-the-weyl-group(2)); the ten reflections generate $W(E_{10})$ (@lem:coble-image-on-m-is-the-weyl-group(1)--(2)). This is the paragraph *Lower bound* of the proof of @thm:coble-monodromy-on-m-classical, which computes with the matrices of isomorphisms of surfaces. Hence $W(E_{10})\subseteq\mathcal T_x$. The statement on the families is @lem:coble-canonical-class-and-ample-component-in-families(4).

*2.* By (A) the chart $p$ is an epimorphism, so there are a point $a\in X$ and an identification of $x$ with $p(a)$, and by @lem:g-paths-exhaust-the-fundamental-groupoid(1) every element of $\pi_1(\mcM_\Co,x)$ is a product of that identification, of classes $[p\alpha]$ of paths $\alpha$ of $X$, of classes $[\rho]$ of identifications of objects over $\CC$, and of the inverse of that identification. A path of $X$ lies in one path component of $X$, which is an arcwise connected, locally simply connected complex space. By @thm:quotient-local-system-descent(1), the transport of $\bM$ along the loop is a composite of transports of the system $\bM_p$ of the family $p$ along paths and of isometries induced by isomorphisms of objects: it is an element of $\mathcal T_x$. Conversely, let $P\colon B\to\mcM_\Co$ be the family over $B$ and $r\colon b\to b'$ a point of $R_B$. Naturality of the descended system makes the composite displayed in the proof of 1 the transport of $\bM$ along the loop $[Pc_b]\,[r]\,[Pc_{b'}]^{-1}$ of $\mcM_\Co$ at $x$, for paths $c_b$, $c_{b'}$ of $B$ from $s$ to $b$ and to $b'$. So the monodromy group contains every $m(r)$, and with 1 it is $\mathcal T_x=W(E_{10})$.

*3.* The inclusion is @thm:coble-classical-substack-is-open-dense-and-proper(1) and the description of the complement is (3) there; a loop of $\mcM_\Co$ that is moved into $\mcM_\Co\sm\mcH$ lies in $\mcM^{\mathrm{cl}}_\Co$.
:::

