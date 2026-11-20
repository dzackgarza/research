# Constructions of the moduli space {#sec-moduli-construction}

$$
\begin{aligned}
\fen &= \bD(\ten)/\Gamma_\En &
\fentwo &= \bD(\ten)/\gent \\
F^K_{\En} &= \bD(\ten)/\Gamma^K_{\En} \\
\fco &= \bD(T_\Co) / \Gamma_\Co &
F_{\Co, 2} &= \bD(T_\Co)/\Gamma_{\Co, 2}
\end{aligned}
$$

where

$$
\begin{aligned}
\gent &= \Orth(\ten) \intersect \Orth(\tdp) \iscontainedin \Orth(\lkt) \\
\Gamma_\En &= \widetilde\Orth^+(\ten) = \Orth^+(\ten)^* = \Orth^+(\ten)\intersect\discriminantkernel{\ten}, \qquad \Gamma^K_{\En} = \Orth(\ten) \\
\Gamma_\Co &= \text{the monodromy group of the family of unpolarized Coble surfaces} \\
\Gamma_{\Co, 2} &= \text{the monodromy group of the VHS of the degree-$2$ Coble family} \\
R_{\gent} &= \text{the image of } \Stab_{\gent}(\delta) \text{ in } \Orth(\delta^{\perp\ten}) = \Orth(T_\Co), \quad \delta^2 = -2 \\
F_{\Nod} &= \bD(T_\Nod)/\Orth^+(T_\Nod)^*
\end{aligned}
$$

Here $\tdp$ is the $(-1)$-eigenlattice of $I_\dP$ [@AEGS25, Def. 2.3], and $\eta\colon T_\Co\injects\ten$ is the embedding of @lem:primitive_embedding_eta.
The quotient $F^K_{\En} = \bD(\ten)/\Gamma^K_{\En}$, with $\Gamma^K_{\En} = \Orth(\ten)$ the group $\Gamma_{\mathrm{Enr}}$ of [@AEGS25, Def. 2.6], has two $0$-cusps $(10,10,0)_1$, $(10,8,0)_1$ and two $1$-cusps $(8,8,0)_0$, $(8,6,0)_0$ [@AEGS25, §3.2, Fig. 3]. The quotient $\fentwo = \bD(\ten)/\gent$, with $\gent = \Gamma^K_{\En}\intersect\Gamma_{\dP}$, has five $0$-cusps [@AEGS25, §3]. Throughout, $\Gamma_\En$ denotes the stable group $\widetilde\Orth^+(\ten)$, also written $\Orth^+(\ten)^*$ (@def:gamma-co-groups, @sec-heegner-line, @thm:normalization, @def:gamma-co-en).
The group $\Gamma_\Co$ is the monodromy group of the family of unpolarized Coble surfaces of @def:coble-family-unpolarized, and $\fco = \bD(T_\Co)/\Gamma_\Co$ (@def:gamma-co-groups).

The objects, bases, local systems of lattices and period maps of the two families on which $\Gamma_\Co$ and $\Gamma_{\Co,2}$ are taken are those of @sec-coble-families-d2: the unpolarized family with its three bases (@def:coble-family-unpolarized), whose period map on the first of them is the map of [@DK13, Prop. 3.2] (@lem:d2a-period-map), and the degree-$2$ family over the discriminant divisor (@def:coble-family-degree-two), whose base is the whole of that divisor (@lem:d2-degree-two-base).
The equality $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$ is @conj:gamma-co-stable, and on the labelled base, the base that @def:gamma-co-groups(1) assigns to $\Gamma_\Co$, it is proved (@thm:gamma-co-is-stable). It is not an equality on the other bases of D2a: on the unlabelled base the group is $\Gamma_{10A_1}$, which strictly contains $\widetilde\Orth^+(T_\Co)$ (@cor:gamma-co-inclusions(2)), and the coarse space carries no family, its tautological local system having group $\Orth^+(T_\Co)$ (@thm:gamma-co-is-full, @rmk:gamma-co-d2a).
The group $\Gamma_{\Co,2}$ of $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ is the monodromy group of the VHS of the degree-$2$ Coble family (@def:gamma-co-groups(5)). The group that the Enriques datum defines is $R_{\gent} = \bar\rho^{-1}(P)$, the image of the stabilizer of $\delta$ in $\gent$ (@prop:gamma-co-images(3)); it is not the monodromy group, and $\Gamma_{\Co,2} = R_{\gent}$ is false (@thm:coble-monodromy-versus-enriques(3)). The monodromy group lies in $R_{\gent}\intersect\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(4), from @lem:coble-monodromy-in-stabilizer conditional on (U) of @lem:coble-family-identification; (U) and (F) are D2 of research#786, and the definitions they ask for are @sec-coble-families-d2, the family, the base and the local system being those of @def:coble-family-degree-two and @lem:d2-local-system).
The stable subgroup $\widetilde\Orth^+(T_\Co)$ is the kernel of the action on $A_{T_\Co}$ of each of the groups $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ of @sec-gamma-co-comparison, and both inclusions are strict, of index $\abs{W(E_8)} = 696\,729\,600$ (@prop:gamma-co-heegner-strict, @prop:theta-co-index).

::: {#rmk:coble-arithmetic-group-description .remark title="The group $\Gamma_{\Co,2}$, explicitly"}
@def:gamma-co-groups(5) defines $\Gamma_{\Co,2}$ as the monodromy group, and @thm:coble-monodromy-versus-enriques identifies the arithmetic group that contains it (@lem:coble-monodromy-in-stabilizer, conditional on (U) of @lem:coble-family-identification, which is D2 of research#786): $\Gamma_{\Co,2}\subseteq\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co) = \rho_{T_\Co}^{-1}(P)\intersect\Orth^+(T_\Co) = R_{\gent}\intersect\Orth^+(T_\Co)$, the preimage in $\Orth(T_\Co)$ of the stabilizer $P$ of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ of $A_{T_\Co}$ (@prop:gamma-co-images(3)), intersected with $\Orth^+(T_\Co)$, of index $[\Orth(T_\Co):\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)] = 2\cdot 67\,456 = 134\,912$. The intersection with $\Orth^+(T_\Co)$ cannot be dropped from that chain: the group $R_{\gent} = \rho_{T_\Co}^{-1}(P)$ of @thm:gamma-co-2-comparison(1) is not contained in $\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(2)), the two differ by the coset $s_\zeta\,(R_{\gent}\intersect\Orth^+(T_\Co))$ of a reflection in a primitive vector $\zeta$ of square $2$, so $R_{\gent} = \rho_{T_\Co}^{-1}(P)$ is the larger group and $\Gamma_{\Co,2} = R_{\gent}$ does not hold; whether $\Gamma_{\Co,2}$ is the whole arithmetic group is @qst:coble-monodromy-equality.
:::

```{.tikz}
%%| filename: moduli-tower
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}[column sep=large, row sep=large]
F_{\mathrm{Co},2}
  \arrow[r] &
F_{\mathrm{En},2}
  \arrow[r]
  \arrow[d] &
F_{(2,2,0)}
  \arrow[r, hook] &
F_4 \\
F_{\mathrm{Co}}
  \arrow[r]
  \arrow[u, "|W(E_8)|"'] &
F_{\mathrm{En}}
\end{tikzcd}
```

The tower relates the degree-$2$ numerically polarized Coble and Enriques moduli $F_{\Co,2}$, $\fentwo$, their unpolarized quotients $\fco$, $\fen$, and the degree-$(2,2,0)$ K3 moduli space $\fttz\injects F_4$.
The vertical map is $F_{\Co}\to F_{\Co,2}$, finite of degree $[\Gamma_{\Co,2}:\Gamma_\Co]$ once $\Gamma_\Co\subseteq\Gamma_{\Co,2}$. By @thm:gamma-co-is-stable, $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ up to $\pm\id$, and $\widetilde\Orth^+(T_\Co)\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$ unconditionally (@cor:gamma-co-inclusions(1), @prop:gamma-co-images(3)); so $\Gamma_\Co\subseteq\Gamma_{\Co,2}$ whenever $\Gamma_{\Co,2}$ contains $\widetilde\Orth^+(T_\Co)$, and the degree is $[\Gamma_{\Co,2}:\widetilde\Orth^+(T_\Co)]$, which divides $\abs{W(E_8)}=696\,729\,600$ and equals it exactly when @qst:coble-monodromy-equality holds (@rmk:coble-monodromy-counts).

## The GIT construction

::: {.proposition #prop:coble-moduli-git title="The GIT construction of the Coble moduli space"}

1. The moduli space $\mcm_\Co$ of blowups of $\PP^2$ at the ten nodes of an irreducible plane sextic is a locally closed subvariety of the GIT quotient of the variety $(\PP^2)^{10}$ of $10$-tuples of points in $\PP^2$ by $\PGL_3$ [@DK13, §3].
2. A general point of $(\PP^2)^{10}$ has trivial stabilizer in $\PGL_3$, so its $\PGL_3$-orbit has dimension $\dim\PGL_3 = 3^2-1 = 8$ and codimension
$$
\dim (\PP^2)^{10} - \dim \PGL_3 = 2\cdot 10 - 8 = 12
.
$$
3. The set of ten nodes of an irreducible plane sextic is subject to three conditions and contains nine absolute constants [@Cob19, §2, (10)].

:::

::: {.proof}

For (2), a general $10$-tuple contains four points $q_1, \ldots, q_4$, no three of them on a line.
Choose coordinates with $q_1 = [1:0:0]$, $q_2 = [0:1:0]$, $q_3 = [0:0:1]$ and $q_4 = [1:1:1]$.
A matrix $g\in\GL_3$ that fixes the lines spanned by the first three standard basis vectors is diagonal.
If $g$ also fixes the line spanned by $(1,1,1)$, its diagonal entries are equal, so $g$ is a scalar and its class in $\PGL_3$ is the identity.
So the stabilizer is trivial, and the orbit map $\PGL_3\to(\PP^2)^{10}$ has image of dimension $\dim\PGL_3$.

:::

## The Horikawa model

::: {.proposition #prop:horikawa-model title="The Horikawa model"}

Let $Y = \PP^1\times\PP^1$ with the involution $\tau(x,y) = (-x,-y)$, and let $B\in\abs{-2K_Y}$ be a $\tau$-invariant divisor with at worst ADE singularities that does not pass through the four points with $x, y\in\theset{0,\infty}$ fixed by $\tau$.

1. The double cover $\pi\colon X\to Y$ branched in $B$ is a K3 surface with a del Pezzo involution $\idp$ such that $Y = X/\idp$. The involution $\tau$ lifts to a basepoint-free involution $\ien$ of $X$ that commutes with $\idp$, and $Z = X/\ien$ is an Enriques surface (@def:enriques-surface) [@AEGS25, §2.1].
2. Certain mildly singular $\tau$-invariant equations $f(x,y)$ of bidegree $(4,4)$ that vanish at a torus-fixed point correspond to Coble surfaces (@def:coble-surface), which are $\ZZ/2$ quotients of nodal K3 surfaces [@AEGS25, §2.1; @Hor77].
3. There is a unique $(-2)$-vector $\alpha\in\ten$ modulo $\Orth(\ten)$. The divisor $\Delta = \alpha^\perp\iscontainedin\bD(\ten)/\Orth(\ten)$ parametrizes quotients of nodal K3 surfaces by an involution that fixes a node. These are rational Coble surfaces with a $\tfrac14(1,1)$ singularity [@AEGS25, §2.3].

:::

## Period domains

By passing to the K3 cover, one can embed $\fco$ into an arithmetic quotient of a 9-dimensional Hermitian symmetric domain of type $\rm{IV}$.
Let $\lkt = U^3 \oplus E_8^2$ be the canonical K3 lattice.

::: {.definition #def:type-iv-period-domain title="Type IV period domain and its arithmetic quotients"}

Let $T$ be a lattice of signature $(2,n)$ with $n\geq1$, and let $\Omega_T$ be the set of @def:period-component-character.
It has two connected components.
Fix one of them and call it $\bD(T)$.
By @prop:period-spinor-character, the group $\Orth^+(T)$ of @def:lattice-spinor-kernels is the stabilizer of $\bD(T)$ in $\Orth(T)$.
For a subgroup $\Gamma\iscontainedin\Orth(T)$, write
$$
\bD(T)/\Gamma\definedas\bD(T)/\qty{\Gamma\intersect\Orth^+(T)},
\qquad
\Orth^+(T)^*\definedas\Orth^+(T)\intersect\discriminantkernel{T}.
$$
:::

::: {.lemma #lem:period-quotient-full-domain title="Quotients of the full period domain"}

In the notation of @def:type-iv-period-domain, let $\Gamma\iscontainedin\Orth(T)$ contain an element that exchanges the two components of $\Omega_T$.
Then the inclusion $\bD(T)\injects\Omega_T$ induces a bijection
$$
\bD(T)/\Gamma\iso\Omega_T/\Gamma
.
$$
In particular $\Orth^+(T)$ has index two in $\Orth(T)$.
:::

::: {.proof}

Let $g\in\Gamma$ exchange the two components.
Every $\Gamma$-orbit in $\Omega_T$ meets $\bD(T)$: a point of the other component is mapped into $\bD(T)$ by $g$.
Let $x,y\in\bD(T)$ and $\gamma\in\Gamma$ with $\gamma x=y$.
The isometry $\gamma$ is a homeomorphism of $\Omega_T$, so it maps the component $\bD(T)$ of $x$ onto the component of $y$, which is $\bD(T)$.
Hence $\gamma\in\Gamma\intersect\Orth^+(T)$, and the map of orbit sets is injective.
The last statement is the case $\Gamma=\Orth(T)$: the component character $\Orth(T)\to\theset{\pm1}$ of @def:period-component-character is surjective, and its kernel is $\Orth^+(T)$.
:::

If $T$ has an orthogonal summand $U$, then $\Gamma$ contains such an element as soon as it contains $\sigma_U\definedas(-\id_U)\oplus\id_{U^{\perp T}}$.
Indeed $-\id_U=s_{e+f}\circ s_{e-f}$ for a hyperbolic basis $e,f$ of $U$, the vector $e+f$ is positive and $e-f$ is negative, so $\sigma_U$ is the product of one reflection in a positive vector and one in a negative vector, and @prop:period-spinor-character gives it component character $-1$.
The isometry $\sigma_U$ acts trivially on $A_T$, so it lies in $\discriminantkernel{T}$.

For any primitively embedded lattice $S\injects \lkt$, letting $T \definedas S^{\perp \lkt}$, there is a Hodge-theoretic description of the coarse moduli space $F_S$ of $S$-polarized K3 surfaces given by
$$
F_S \definedas \bD(T)/\Orth^+(T)^*
.
$$

::: {.proposition #prop:type-iv-dimension title="Dimension of a type IV domain"}

Let $T$ be a lattice of rank $r$ and signature $(2, r-2)$.
Then the type IV domain $\bD(T)$ has complex dimension $r - 2$.
:::

::: {.proof}

The complexification $T_\CC$ has dimension $r$, so $\PP(T_\CC)$ has dimension $r-1$.
The equation $v^2 = 0$ is a single nondegenerate quadratic equation and cuts out a smooth quadric hypersurface of dimension $r-2$ inside $\PP(T_\CC)$.
The condition $v\bar v > 0$ is open, so it selects an open subset of that quadric, and $\bD(T)$ is one of its connected components.
:::

::: {.corollary #cor:m-polarized-k3-dimension title="Dimension of $M$-polarized K3 moduli"}

Let $M\injects\lkt$ be a primitive embedding of a lattice of signature $(1, \rank(M) - 1)$ with orthogonal complement $T = M^{\perp\lkt}$.
Then
$$
\dim_\CC \bD(T) = \rank(T) - 2 = 20 - \rank(M)
.
$$
For the Coble lattices $\rank(S_\Co) = 11$, so $\dim_\CC \bD(T_\Co) = 9$.
:::

::: {.proof}

The K3 lattice has rank $22$ and signature $(3,19)$. The embedding is primitive, which gives a splitting over $\mathbb{Q}$ and not over $\mathbb{Z}$: $M$ and $T$ span $\lkt\otimes\QQ$ orthogonally, so their ranks and signatures add, while $M\oplus T$ has index $|\det M| = |\det T|$ in $\lkt$ and the integral statement is the gluing $A_M\cong A_T$ rather than a direct sum. Orthogonal decomposition over $\mathbb{Z}$ needs the embedded form to be perfect (@thm:orthogonal-decomposition), which $M = S_\Co$ is not: its determinant is $2^{11}$.
Ranks add, so $\rank(T)=22-\rank(M)$.
Signatures add too, by @def:signature applied to the orthogonal sum of the two real forms, so if $M$ has signature $(1,\rank(M)-1)$ then $T$ has signature $(3-1,\,19-(\rank(M)-1))=(2,\,20-\rank(M))$.
The first index is $2$, so $T$ is of type IV in the sense of @prop:type-iv-dimension, whose dimension for a type IV lattice of signature $(2,m)$ is $m$; with $m=20-\rank(M)$ that is the displayed dimension.
For $M=S_\Co$ of rank $11$ the complement has signature $(2,9)$, giving $\dim_\CC \bD(T_\Co)=9$.
:::

::: {.definition #def:heegner-divisor title="Heegner divisor"}

Let $N$ be an even lattice of signature $(2, m)$, and let $\bD(N)$ be its period domain (@def:type-iv-period-domain).
For $d\in\ZZ$, the **$(-2d)$-Heegner divisor** of $\bD(N)$ is
$$
\mch_{-2d} \definedas \Union_{\delta\in N,\ \delta^2 = -2d} \theset{[\omega]\in\bD(N) \suchthat \omega\cdot\delta = 0}
$$
[@DK13, (3.2)].
:::

::: {.proposition #prop:enriques-nodal-coble-heegner title="Enriques, nodal Enriques and Coble surfaces in the Enriques period domain"}

Let $\ten = U\oplus E_{10}(2)$ be the orthogonal complement in $\lkt$ of the pullback $E_{10}(2)$ of the numerical lattice of an Enriques surface (@def:enriques-surface) to its K3 cover.
The group $\Orth(\ten)$ is the group $\Gamma^K_\En$ of the opening display, and it contains the group $\Orth^+(\ten)^*$ of $\fen$.

1. The period point of the K3 cover of an Enriques surface does not lie in $\mch_{-2}$.
   The quotient $\bD(\ten)/\Orth(\ten)$ is a normal quasi-projective variety of dimension $10$, and $\qty{\bD(\ten)\sm\mch_{-2}}/\Orth(\ten)$ is the moduli space $\mcm_\En$ of Enriques surfaces [@DK13, §3].
2. There are two $\Orth(\ten)$-orbits of $(-4)$-vectors in $\ten$ [@AEGS25, §2.3].
   One orbit consists of the vectors $\delta$ with $\delta^{\perp\ten}\cong T_\Nod = U\oplus\generators{4}\oplus E_8(2)$; let $\mch^{\mathrm{nod}}_{-4}\iscontainedin\mch_{-4}$ be the union of their hyperplanes.
   The divisor $\mcm^{\mathrm{nod}}_\En \definedas \qty{\mch^{\mathrm{nod}}_{-4}\sm\mch_{-2}}/\Orth(\ten)$ parametrizes nodal Enriques surfaces [@AEGS25, §2.3].
   The quotient $\bD(T_\Nod)/\Orth(T_\Nod)$ is a quasi-projective variety of dimension $9$, and $\mcm^{\mathrm{nod}}_\En$ is birationally isomorphic to it [@DK13, §3, Prop. 3.1].
   The other orbit gives the divisor of unigonal Enriques surfaces (@prop:coble-and-unigonal-heegner-divisors).
3. The quotient $\mch_{-2}/\Orth(\ten)$ is birationally isomorphic to the moduli space $\mcm_\Co$ of Coble surfaces (@def:coble-surface) (@prop:coble-moduli-heegner-divisor).

:::

::: {#fig-period-domain-hyperplanes .figure}
\input{tikz/fig_type_iv_hsd.tex}

The period domain $D_{\ten}$ together with the hyperplanes $v_i^{\perp\ten}$ cut out by vectors $v_i$ of fixed negative norm.
The quotient by $\Orth(\ten)$ of the union $\mch_{-2}$ of the hyperplanes of the vectors of norm $-2$ is birationally isomorphic to $\mcm_\Co$ (@prop:coble-moduli-heegner-divisor).
:::

::: {.proposition #prop:coble-period-domain title="The period domain of Coble surfaces"}

Let $C\iscontainedin\PP^2$ be an irreducible plane sextic with ten nodes $p_1, \ldots, p_{10}$, let $S$ be the blowup of $\PP^2$ at $p_1, \ldots, p_{10}$, and let $X$ be the double cover of $S$ branched along the proper transform of $C$.
Let $E_0$ be the pullback to $X$ of a line in $\PP^2$, and let $E_1, \ldots, E_{10}$ be the inverse images in $X$ of the exceptional curves over $p_1, \ldots, p_{10}$.

1. $X$ is a K3 surface, and the classes $e_0, e_1, \ldots, e_{10}$ of $E_0, E_1, \ldots, E_{10}$ span a sublattice of $\Pic(X)$ isometric to
$$
S_\Co \definedas \generators{2}\oplus \generators{-2}^{10} = \latI_{1, 10}(2) = (11, 11, 1)_1 \cong \generators{-2} \oplus E_{10}(2)
.
$$
The lattice $S_\Co$ is $2$-elementary of signature $(1, 10)$ with $A_{S_\Co}\cong(\bZ/2\bZ)^{11}$ [@DK13, §3].
2. The orthogonal complement of this sublattice in $H^2(X,\ZZ)\cong\lkt$ is a $2$-elementary lattice of signature $(2, 9)$ with discriminant form $-q_{S_\Co}$ [@DK13, §3; @Nik80, Cor. 1.6.2]. Its isomorphism class is determined by $-q_{S_\Co}$ [@DK13, §3; @Nik80, Thm. 3.6.2], so
$$
T_\Co \definedas S_\Co^{\perp \lkt} = (11, 11, 1)_2 \cong \generators{2} \oplus E_{10}(2)
.
$$
3. The quotient $\bD(T_\Co)/\Orth(T_\Co)$ is a normal quasi-projective variety of dimension $9$, and the moduli space $\mcm_\Co$ of @prop:coble-moduli-git is isomorphic to an open subset of it (@lem:d2a-coble-moduli-quotient).

:::

::: {.lemma #lem:d2a-coble-moduli-quotient title="The Coble moduli space is an open subset of the orthogonal quotient"}

Let $T_\Co = \generators{2}\oplus E_{10}(2)$ be the lattice of [@DK13, (3.6)] and @prop:coble-period-domain(2), and let $\mcm_\Co$ be the moduli space of Coble surfaces of @prop:coble-moduli-git. Then $\mcm_\Co$ is isomorphic to an open subset of $\bD(T_\Co)/\Orth(T_\Co)$ [@DK13, Prop. 3.2], and that open subset is the image of the period map.
:::

::: {.proof}

This is [@DK13, Prop. 3.2], whose statement is that for $N=\generators{2}\oplus E(2)$ the moduli space $\mathcal M_{\mathrm{Co}}$ of Coble surfaces is isomorphic to an open subset of $\mathcal D(N)/\Orth(N)$; $\mathcal D(N)$ is the period domain of (3.1) there and $N$ is the lattice of (3.6) there, which is $T_\Co=\generators{2}\oplus E_{10}(2)$ by @prop:coble-period-domain(2).

Its hypotheses are the ones this book already checks on the fibres. The period domain is attached to an algebraic K3 surface: the double cover of @lem:d2-unpolarised-family(1) is a K3 surface $X_b$, and $h^{2,0}(X_b)=1$, so a point of $\bD(T_\Co)$ is the $2$-dimensional positive subspace $H^{2,0}(X_b)\subset T_\Co\otimes\CC$ of @prop:coble-period-domain(1). The lattice $N$ is the transcendental lattice of $X_b$: the classes $e_0,\dots,e_{10}$ of @prop:coble-period-domain(1) span $M$ primitively in $\lkt$, and $T_\Co=M^{\perp\lkt}$ (@prop:coble-transcendental). So the pair $(X_b,M\subset H^2(X_b,\ZZ))$ is an $M$-polarized K3 surface in the sense of the source, and the identity of periods it uses is the identity of the Hodge structures on $T_\Co$.

[@DK13, Prop. 3.2] obtains the statement from the Torelli-type theorem for algebraic K3 surfaces of Pyatetskii--Shapiro and Shafarevich, which the source cites in its proof; that theorem is therefore not an independent input of this book, and no numbered statement of it is cited here.
:::

::: {.proposition #prop:coble-moduli-heegner-divisor title="The Coble moduli space as a Heegner divisor"}

The lattice $T_\Co\cong\generators{2}\oplus E_{10}(2)$ is isometric to the orthogonal complement of a $(-2)$-vector in $\ten = U\oplus E_{10}(2)$.
The quotient of the $(-2)$-Heegner divisor $\mch_{-2}$ in $\bD(\ten)$ by $\Orth(\ten)$ is birationally isomorphic to $\mcm_\Co$ [@DK13, §3].

:::

::: {.theorem #thm:coble-moduli-rational title="Rationality of the Coble moduli space"}

Let $\mcm'_{5,\cusp}$ be the moduli space of plane quintics $C$ with a cusp $p$ such that the tangent line $L$ of $C$ at $p$ is tangent to $C$ at a nonsingular point $q$ of $C$.
Then $\mcm_\Co$ is birationally isomorphic to $\mcm'_{5,\cusp}$ [@DK13, §4, Thm. 6.3], and $\mcm_\Co$ is a rational variety [@DK13, Thm. 6.4].

:::

## The sextic moduli construction

::: {.notation #not:sextic-singular-type title="Moduli of sextics of a fixed singular type"}

For a singular type $T$ with root lattice $R$, write $\mcv_T$ for the space of sextic curves $Z\subset\PP^2$ with singularities exactly of type $T$, and
$$
\mcm_T \definedas \PP\mcv_T \modmod \SL_3
$$
for the moduli space of such curves, the quotient being taken in the sense of geometric invariant theory [@YZZ25 §2.1].
Let $\wh X$ be the double cover of $\PP^2$ branched along $Z$, let $X$ be its minimal resolution --- a K3 surface --- and let $H\in\Pic(X)$ be the pullback of the line class, so $H^2 = 2$.
The exceptional curves of $X\to\wh X$ span a copy $L\iscontainedin\Pic(X)$ of the root lattice $R$, with the exceptional classes as a base $\Delta$.
Write $P$ for the primitive hull of $\generators H\oplus L$ in $H^2(X;\ZZ)$ and $Q \definedas P^{\perp H^2(X;\ZZ)}$, of signatures $(1,\rank R)$ and $(2, 19 - \rank R)$ [@YZZ25 §2.3].
For a general member of $\mcv_T$ one has $\Pic(X) = P$ [@YZZ25 §3.3].
:::

::: {.proposition #prop:coble-is-the-ten-nodal-sextic-type title="The Coble lattices are the lattices of the type $10A_1$"}

Let $Z$ be an irreducible sextic of type $T = 10A_1$, so that $Z$ is rational by @lem:rational_sextic_ten_nodes, and $X$ is the K3 cover of the Coble surface (@def:coble-surface) $S = X/\iota$.
Then
$$
P = \generators{H}\oplus A_1^{\oplus 10} \cong \latI_{1,10}(2) = S_\Co,
\qquad
Q = P^{\perp\lkt} = T_\Co
.
$$
In particular $\dim D(Q) = 9$.
:::

::: {.proof}

The saturation of $\generators H\oplus L$ inside $H^2(X;\ZZ)$ is $(\ZZ/2)^{l'-1}$, where $l'$ is the number of irreducible components of $Z$ [@YZZ25 §5.3]; for an irreducible sextic $l' = 1$, so no saturation occurs and $P = \generators H\oplus L$.
With $H^2 = 2$ and $L = A_1^{\oplus 10} = \generators{-2}^{\oplus 10}$ this is $\generators 2\oplus\generators{-2}^{\oplus 10} = \latI_{1,10}(2)$, which is $S_\Co$ by @prop:coble-invariant-lattice.
Taking orthogonal complements in $\lkt$ gives $Q = T_\Co$, and the polarized-K3 dimension corollary (@cor:m-polarized-k3-dimension) gives the dimension.
:::

::: {.proposition #prop:sextic-cover-involution-on-root-lattice title="The covering involution on the root lattice"}

In the setting of @not:sextic-singular-type, let $\iota$ be the covering involution of $X$, let $p\colon X\to S = X/\iota$ be the quotient map, and let $f\colon S\to\PP^2$ be the minimal blowup such that the strict transform of $Z$ is smooth.
Then $H^2(S,\ZZ)\cong\generators{f^*h}\oplus\Lambda_S$, where $h$ is the class of a line and $\Lambda_S$ is the lattice that arises from the blowup $f$ [@YZZ25, §5.2].
Let $L^\iota$ be the sublattice of $L$ fixed by $\iota$.

1. $\iota = -w_0(L)$ as automorphisms of $L$, where $w_0(L)$ is the longest element of $W(L)$ with respect to $\Delta$ [@YZZ25, §5.2].
2. The map $p^*\colon H^2(S,\ZZ)(2)\to H^2(X,\ZZ)$ is an injective morphism of lattices that maps $f^*h$ to $H$, and it induces a finite-index extension $\Lambda_S(2)\injects L^\iota$ [@YZZ25, §5.3].
3. $L^\iota/\Lambda_S(2)\cong(\ZZ/2)^m$, where $m$ is the number of exceptional curves of $S$ that lie in the branch locus of $p$ [@YZZ25, §5.3].
4. If $Z$ has only singularities of types $A_1$, $D_{2n}$ with $n\geq 2$, $E_7$ and $E_8$, then $L^\iota = L$. If $Z$ has only singularities of type $A_1$, then $\Lambda_S(2)\cong L$ as lattices [@YZZ25, §5.3].

:::

::: {.theorem #thm:occult-period-map-sextics title="The occult period map and its image"}

Let $\Gamma_T$ be the image of
$$
\Orth\bigl(H^2(X;\ZZ),\, \Delta,\, H\bigr) \too \Orth(Q)
,
$$
restricted to the subgroup preserving a chosen component $D(Q)$; it is arithmetic of finite index in $\Orth(Q)$, and contains every isometry of $Q$ acting trivially on $A_Q$ [@YZZ25 §3.1].
The **occult period map**
$$
\per_T\colon \mcm_T \too \Gamma_T\backslash D(Q)
$$
is an algebraic open embedding with image $\Gamma_T\backslash\bigl(D(Q) - \mch_T\bigr)$, where $\mch_T$ is the arrangement of hyperplanes $r^{\perp Q}$ for roots $r$ orthogonal to $H$ and not lying in $L$.
When $T$ is a nodal type, $\per_T$ is moreover an isomorphism of orbifolds onto $P\Gamma_T\backslash(D(Q) - \mch_T)$ [@YZZ25 §1, §3.2, §3.3, §6.2].
:::

::: {.proof}

This is [@YZZ25, Prop. 3.2, Thms. 3.3, 3.4 and 4.11, Prop. 6.6].
:::

::: {.theorem #thm:git-equals-looijenga title="The GIT compactification is a Looijenga compactification"}

Let $\Lambda_1 \definedas H^{\perp\lkt}$, of signature $(2,19)$ with $A_{\Lambda_1}\cong\ZZ/2$, and let $\Gamma_1$ be the arithmetic group of the degree-$2$ K3 moduli space $\Gamma_1\backslash D(\Lambda_1)$.
The roots of $\Lambda_1$ fall into two $\Gamma_1$-orbits, of divisibility $1$ and $2$, cutting out arrangements $\mch_\Delta$ and $\mch_\infty$; the roots of $L$ all have divisibility $1$, so they contribute to $\mch_\Delta$ only [@YZZ25 §4.1, §4.2].
Set
$$
\mch^{*}_T \definedas \mch_\infty \intersect D(Q) \iscontainedin \mch_T
.
$$
Then $\per_T$ extends to an isomorphism
$$
\wh{\mcm}_T \;\cong\; \overline{\Gamma_T\backslash D(Q)}^{\,\mch^{*}_T}
$$
between the GIT compactification of $\mcm_T$ and the Looijenga compactification of @def:looijenga-compactification applied to $\Gamma_T\backslash(D(Q) - \mch^{*}_T)$, compatibly with the corresponding statement of Shah and Looijenga for the whole space of sextics, $\overline{\mcm}\cong\overline{\Gamma_1\backslash D(\Lambda_1)}^{\,\mch_\infty}$ [@Sha80; @Loo02]; the two vertical maps of the resulting square are normalizations onto their images [@YZZ25 §4.2].
:::

::: {.proof}

This is [@YZZ25, Thm. 4.1, Lem. 4.8 and Thm. 4.11].
:::

::: {.proposition #prop:sextic-group-as-normalizer title="The arithmetic group as a normalizer"}

Let $\Gamma_W$ be the normalizer of the Weyl group $W = W(L)$ in the group $\Gamma_1$ of @thm:git-equals-looijenga, transported to $H^2(X;\ZZ)$ by a marking.
Then $\Gamma_T$ is the restriction $\Gamma_W|_Q$ of $\Gamma_W$ to $Q$ [@YZZ25, §4.2].
For $T = 10A_1$, $L = \bigoplus_{i=1}^{10}\ZZ\alpha_i$ with $\alpha_i^2 = -2$, and $W(L)$ is generated by the reflections $s_{\alpha_i}$, each of which acts by $-1$ on $\ZZ\alpha_i$ and fixes the other summands, so
$$
W(L) = \theset{\pm 1}^{10},
\qquad
\Gamma_{10A_1} = \Gamma_W|_{Q},
\qquad
\Gamma_W = N_{\Gamma_1}\bigl(\theset{\pm1}^{10}\bigr)
.
$$

:::

::: {.lemma #lem:ten-a1-permutation-forces-strictness title="A permutation of the ten classes puts $\Gamma_{10A_1}$ outside the discriminant kernel"}

Let $\Lambda_1 = H^{\perp\lkt}$ with $A_{\Lambda_1}\cong\ZZ/2$ (@thm:git-equals-looijenga), let $P\definedas\generators{r_1,\dots,r_{10}}\cong A_1^{\oplus 10}$ be the span of the ten classes $r_i$ with $r_i^2 = -2$, and let $Q\definedas P^{\perp\Lambda_1}$ be the lattice $T_\Co$ of @thm:occult-period-map-sextics [@YZZ25, §3.1]. Then $\abs{A_P} = 2^{10}$, $\abs{A_Q} = 2^{11}$ and
$$[\Lambda_1 : P\oplus Q]^2 = \frac{\abs{A_P}\abs{A_Q}}{\abs{A_{\Lambda_1}}} = 2^{20},$$
so the gluing subgroup $H_0 = \Lambda_1/(P\oplus Q)\leq A_P\oplus A_Q$ has order $2^{10} = \abs{A_P}$ and, its projection to $A_P$ being injective [@Nik80, Prop. 1.5.1], it projects isomorphically onto $A_P$.
If some $g\in\Gamma_W$ acts nontrivially on $A_P$ --- in particular if its signed permutation of the ten classes is not a diagonal change of signs, so that it carries $r_i$ to $\pm r_j$ with $i\neq j$ --- then $\Gamma_{10A_1}\not\subseteq\discriminantkernel{T_\Co}$, and the inclusion $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{10A_1}$ is strict.
:::

::: {.proof}

Let $g\in\Gamma_W$ be such an element, with $\psi\definedas\restrictionof{g}{P}$, $\varphi\definedas\restrictionof{g}{Q}$ and class actions $\bar\psi$, $\bar\varphi$; here $g(P) = P$ because $\Gamma_W$ normalizes $W(L)$, whose generators determine the classes $r_i$ up to sign (@prop:sextic-group-as-normalizer). The isometry $g$ preserves $P\oplus Q$ and $\Lambda_1$, hence preserves $H_0$, which projects isomorphically onto $A_P$: put $\gamma\definedas p_Qp_P^{-1}$, so that $H_0$ is the graph of $\gamma$ over $A_P$. For $x\in A_P$ the class $(x,\gamma x)$ lies in $H_0$, hence so does $(\bar\psi x,\bar\varphi\gamma x)$, and a graph meets the fibre over $\bar\psi x$ in one point: $\bar\varphi\gamma x = \gamma\bar\psi x$. If $\bar\psi\neq\id$ then $\bar\varphi$ is not the identity on $\gamma(A_P)$, hence $\varphi\notin\discriminantkernel{Q} = \discriminantkernel{T_\Co}$. Since $\Gamma_{10A_1} = \Gamma_W|_Q$ (@prop:sextic-group-as-normalizer), it contains this $\varphi$; and $\widetilde\Orth^+(T_\Co)\subseteq\discriminantkernel{T_\Co}$ by its definition (@def:gamma-co-groups). Finally $\bar\psi[r_i/2] = [\pm r_j/2]\neq[r_i/2]$ for $i\neq j$, because $r_j\mp r_i$ has a coordinate equal to $1$ and so is not in $2P$.
:::

::: {.remark #rmk:coble-moduli-functor title="Two quotients in the source, and which one $\Gamma_\Co$ is the monodromy of"}

The source gives both quotients, one printed page apart. For lattice polarized K3 surfaces --- isomorphism classes of pairs $(X,j)$ with $j\colon M\injects\operatorname{Pic}(X)$ a primitive embedding --- the moduli space is
$$\mcm_{\mathrm{K3},M} = \mathcal D(N)/\Orth(N)^*, \qquad \Orth(N)^* = \ker\bigl(\Orth(N)\too\Orth(A_N)\bigr),$$
with $N = M^{\perp L_{\mathrm{K3}}}$ [@DK13, §3]; for the pair $M = \generators{2}\oplus\generators{-2}^{\oplus 10}$, $N = T_\Co$ of [@DK13, (3.6)] this is $\bD(T_\Co)/\discriminantkernel{T_\Co}$, the quotient by the discriminant kernel. For *unpolarized* Coble surfaces the same source gives $\mcm_\Co$ as an open subset of $\bD(N)/\Orth(N)$ [@DK13, Prop. 3.2], the quotient by the full orthogonal group.

The two differ by exactly the group whose action on $A_{T_\Co}$ decides @conj:gamma-co-stable and the $\Gamma_\Co$ form of @thm:coble-strong-lifting (@cor:gamma-co-lifting-criterion). @def:gamma-co-groups fixes which group $\Gamma_\Co$ is: the monodromy of the *unpolarized* family, that is, the second display. So the first display is not a statement about $\Gamma_\Co$ --- it is one about the monodromy of the lattice polarized family, a different group, and what it supplies is the containment of $\widetilde\Orth^+(T_\Co)$ in that other group, not in $\Gamma_\Co$ [@DK13]. For $\Gamma_\Co$ the containment in the discriminant kernel is exactly what @conj:gamma-co-stable asserts, so the $\Gamma_\Co$ form of the lifting is @prop:gamma-co-strong-lifting, which restates it under that conjecture; its sign half is unconditional (@lem:monodromy-is-spinor-positive) and its discriminant half is decided, when it can be decided at all, by the action on the ten exceptional classes (@cor:gamma-co-lifting-criterion).
:::

::: {.question #qst:sextic-group-comparison title="The comparison of the three bases"}

$\fco$ is the quotient of $D(T_\Co)$ by the monodromy group $\Gamma_\Co$ (@def:gamma-co-groups), and on the labelled base $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable), so $\fco$ has the coarse space of $D(T_\Co)/\widetilde\Orth^+(T_\Co)$ and the cusp counts of the stable quotient (@cor:gamma-co-inclusions(1)).
The unlabelled base $\bar B$ has monodromy $\Gamma_{10A_1}$, and
$$\widetilde\Orth^+(T_\Co)\;\iscontainedin\;\Gamma_{10A_1}\;\iscontainedin\;\Orth^+(T_\Co)$$
with both inclusions strict (@lem:ten-a1-permutation-forces-strictness and the index $12\,951\,552>1$ of @thm:gamma-co-sextic-group(3)); the index of $\Gamma_\Co$ in $\Gamma_{10A_1}$ is $10!$ (@lem:gamma-co-labelled-index), and that of $\Gamma_{10A_1}$ in $\Orth^+(T_\Co)$ is $12\,951\,552$ (@thm:gamma-co-sextic-group(3)).
What is not settled here is the map $\bar B\to M_\Co$ that forgets the sextic: whether a ten-nodal sextic is determined by its ten nodes, that is whether that map is birational, is @rmk:d2-what-is-open(2). The arithmetic model $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ of $\Gamma_{\Co,2}$ is a different group (@thm:coble-monodromy-versus-enriques), and no inclusion between it and $\Gamma_\Co$ is asserted here.
:::

::: {.proposition #prop:sextic-root-lattice-counts title="Root lattices of plane sextics"}

The root lattices $R$ that arise from a singular type of plane sextic with simple singularities have been classified [@Ura88; @Yan96].
The maximal rank of such an $R$ is $19$, and the number of such $R$ of rank $19$, $18$, $17$, $16$ is $519$, $987$, $975$, $782$ respectively [@YZZ25, §1; @Yan96, Thm. 2.1].

:::

## The two Coble families and their bases {#sec-coble-families-d2}

Statements D2a and D2b of research#786 ask for the two families whose variations of Hodge structure define $\Gamma_\Co$ and $\Gamma_{\Co,2}$: for each, a base, its fibres, and the local system of lattices with fibre $T_\Co = \generators{2}\oplus E(2)$ of [@DK13, (3.6)].
Both are defined here by constructing the family over a base given by explicit equations; the base is then identified with the one the source uses, for D2a with the moduli space of [@DK13, Prop. 3.2] (@lem:d2a-period-map) and for D2b with the divisor $\Delta_2$ of $\fentwo$ (@lem:d2-degree-two-base).
The family and its local system are thus objects of the definition and not of a later theorem (@lem:d2-unpolarised-family, @lem:d2-local-system), and the two things the symbol $\Gamma_\Co$ needs --- a base and a family over it --- are fixed before the group is named (@def:gamma-co-groups(1)).
@rmk:d2-what-is-open records what no source read supplies, and @rmk:d2-corrections what this section changes.

::: {.notation #not:d2-plane-sextic-base title="The plane-sextic base and its quotients"}

Let $\abs{\OO_{\PP^2}(6)}$ be the linear system of plane sextics and put
$$
V\definedas\theset{(Z;p_1,\dots,p_{10})\in\abs{\OO_{\PP^2}(6)}\times(\PP^2)^{10}\ \st\ p_1,\dots,p_{10}\ \text{are distinct},\ Z\ \text{is irreducible},\ \operatorname{Sing}Z=\{p_1,\dots,p_{10}\}\ \text{and each } p_i\ \text{is an ordinary double point}} .
$$
This is a locally closed analytic subset of a product of projective spaces: irreducibility is open, and so is the conjunction "the $p_i$ are distinct ordinary double points and there is no other singular point", the last because ordinary double points persist under small deformation of $Z$ (the equations $Z=\partial_xZ=\partial_yZ=0$ have invertible Jacobian, the Hessian, at an ordinary double point).
The effective group is $\PGL_3=\SL_3/\mu_3$: the scalars $\mu_3$ are the kernel of $\SL_3\to\PGL_3$ and act trivially on both factors, so $\SL_3$ acts through $\PGL_3$ and $V/\SL_3=V/\PGL_3$; freeness is a statement about $\PGL_3$. The action of $\PGL_3$ on $V$ is free, and the $\SL_3$-stabilizer of every point of $V$ is $\mu_3$: the fixed points of a non-identity projectivity lie in the union of a line and a point, a line carries at most three nodes of $Z$, and no non-identity projectivity fixes all ten nodes (@lem:d2-plane-sextic-freeness(1)--(2)). $S_{10}$ acts on the second factor and commutes with $\PGL_3$.
Write
$$B\definedas V/\PGL_3,\qquad \bar B\definedas[V/(\SL_3\times S_{10})]=[B/S_{10}]$$
so that $B$ is a complex analytic space and $V\to B$ is a principal $\PGL_3$-bundle (@lem:d2-plane-sextic-freeness(3)), while $\bar B$ is the quotient stack of $B$ by the finite group $S_{10}$, whose coarse space is $V/(\SL_3\times S_{10})$; $B\to\bar B$ is the quotient by $S_{10}$ (@lem:d2-labelling-cover).
Let $U\subset(\PP^2)^{10}$ be the image of $V$: the ordered ten-tuples that are the ten nodes of an irreducible sextic with ten ordinary double points. The quotient $M_\Co\definedas U/\PGL_3$ is the moduli space of Coble surfaces of [@DK13, §3], a locally closed subvariety of the GIT quotient of $(\PP^2)^{10}$ by $\PGL_3$ (@prop:coble-moduli-git), and $B\to M_\Co$ is the map forgetting the sextic.
The locus of irreducible sextics with ten nodes is irreducible, being the image of the irreducible variety of degree-$6$ rational maps $\PP^1\to\PP^2$, so $V$, $B$ and $\bar B$ are connected.
:::

::: {.lemma #lem:d2-plane-sextic-freeness title="The fixed locus of a projectivity, and the principal bundle $V\to B$"}

Let $V$ and $B=V/\PGL_3$ be as in @not:d2-plane-sextic-base.

1. The fixed points of a non-identity projectivity of $\PP^2$ lie in the union of a line and a point.
2. Every line carries at most three nodes of $Z$, and no non-identity projectivity fixes all ten nodes; hence $\PGL_3$ acts freely on $V$, and the $\SL_3$-stabilizer of every point of $V$ is $\mu_3$.
3. Every point of $V$ has four nodes with no three collinear; for the four-element subsets $I$ of the labels the charts $S_I\to B$ of the proof make $B$ a complex analytic space and $V\to B$ a principal $\PGL_3$-bundle.
4. The family and the local system of @lem:d2-unpolarised-family(3) and @lem:d2-local-system descend to $B$, and the monodromy group of $\bT$ over $B$ is $\rho\qty{\pi_1(B,s)}=\rho\qty{\pi_1(V,s)}$, the group $\Gamma_\Co$ of @def:coble-family-unpolarized.
:::

::: {.proof}

(1) A projectivity of $\PP^2$ has at most three eigenvalues. With three distinct eigenvalues its fixed points are the three eigenvectors; with two, they are the projectivized eigenspace of the repeated eigenvalue, a point or a line, together with the eigenvector of the other eigenvalue; with one, it is $\lambda(\id+N)$ with $N$ nilpotent, and the fixed points are the projectivized kernel of $N$, a point or a line. In every case the fixed locus lies in $L\cup\theset{P}$ for a line $L$ and a point $P$.

(2) If four nodes lay on a line $L$, then $Z\cdot L\ge4\cdot2=8>6=\deg Z$, so $L$ is a component of $Z$ by Bézout, against the irreducibility of $Z$; hence a line carries at most three nodes. By (1) a non-identity projectivity fixes at most three nodes on $L$ and at most one at $P$, so at most four of the ten and never all ten; hence the $\PGL_3$-stabilizer of a point of $V$ is trivial. The kernel of $\SL_3\to\PGL_3$ is $\mu_3$ and acts trivially, so the $\SL_3$-stabilizer is $\mu_3$.

(3) Three non-collinear nodes exist, since at most three lie on a line. For three non-collinear nodes $A,B,C$ the lines $AB$, $AC$, $BC$ carry at most three nodes each and contain $A,B,C$ twice each, so at most $3+3+3-3=6$ nodes lie on them and a fourth node $D$ lies outside; then $A,B,C,D$ have no three collinear. For a four-element subset $I$ of the labels let $V_I\subset V$ be the open set of configurations whose $I$-indexed nodes have no three collinear, fix a projective frame $q_1,\dots,q_4$, and let $S_I\subset V_I$ be the closed subset of configurations whose $I$-indexed nodes are $q_1,\dots,q_4$. The map $\PGL_3\times S_I\to V_I$, $(g,s)\mapsto g\cdot s$, is a bijection: a configuration $v\in V_I$ has a unique projectivity $g_v$ carrying its $I$-indexed nodes to $q_1,\dots,q_4$, because a projectivity is determined by the images of four points with no three collinear, and $v=g_v^{-1}(g_vv)$ with $g_vv\in S_I$. It is a homeomorphism because $v\mapsto g_v$ is given by solving a linear system whose determinant is nonzero on $V_I$. The composites $S_I\to V_I\to B$ are therefore charts; they cover $B$ by the first paragraph, and their transition maps are restrictions of the $\PGL_3$-action, hence analytic. So $B$ is a complex analytic space and $V\to B$ is a principal $\PGL_3$-bundle.

(4) The family and $\bT$ are $\PGL_3$-equivariant (@lem:d2-unpolarised-family(3)), so they descend to the base $B$ of the principal bundle $V\to B$. A loop of $B$ lifts to a path of $V$ by local triviality and compactness of $[0,1]$; the lift ends at $gs$ for some $g\in\PGL_3$, and since $\PGL_3$ is connected a path from $e$ to $g$ turns it into a loop of $V$ over the given loop. Hence $\pi_1(V,s)\to\pi_1(B,[s])$ is surjective. The monodromy group of the descended system on $B$ is $\rho\qty{\pi_1(B,[s])}$, and its pullback to $V$ is $\bT$, so it equals $\rho\qty{\pi_1(V,s)}$, which is $\Gamma_\Co$ (@lem:d2a-monodromy-of-the-stack).
:::

::: {.remark #qst:s10-free-on-B title="Freeness of $S_{10}$ on the labelled base, and why the index does not need it"}

The action of $S_{10}$ on $B$ need not be free: a labelled ten-nodal sextic $(Z;p_1,\dots,p_{10})$ together with a projectivity $g$ with $gZ=Z$ and $gp_i=p_{\sigma(i)}$ for some $\sigma\neq e$ would be a fixed point. The index of $\Gamma_\Co$ in $\Gamma_\Co(\bar B)$ is nevertheless $10!$, because $\bar B$ is read as the quotient stack $[B/S_{10}]$: @lem:d2-labelling-cover gives the principal $S_{10}$-bundle of stacks $B\to[B/S_{10}]$ and the exact sequence, and @lem:gamma-co-labelled-index computes the index from it, with the faithfulness of the label action on $A_M$. No freeness of the $S_{10}$-action on $B$ is used, and the coarse map $B\to V/(\SL_3\times S_{10})$ is not asserted to be a covering.
:::

::: {.definition #def:coble-family-unpolarized title="D2a: the family of unpolarized Coble surfaces"}

A *Coble surface* is a nonsingular projective rational surface $S$ with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}\neq\emptyset$ [@DZ99, Introduction; @DK13, §3].

**The objects.** Over a complex space $Y$, an object is a flat projective family $\mcs\to Y$ of classical Coble surfaces: a morphism whose geometric fibres are the surfaces $S=\Bl_{p_1,\dots,p_{10}}\PP^2$ of @lem:d2-unpolarised-family(1), together with the relative double cover $\mcx\to\mcs$ branched along the relative divisor $-2K_{\mcs/Y}$ and the covering involution $\iota$. Morphisms are Cartesian squares commuting with $\iota$.
A Coble surface is rational, so $h^{2,0}=0$ on every fibre and the degree-$2$ Hodge structure of $\mcs$ is of type $(1,1)$ throughout; the variation of Hodge structure on which the monodromy acts is that of the K3 *covers*, which is the local system of the next item.
The labelling of the ten exceptional curves is not part of the objects: the labelled base $B=V/\PGL_3$ is the space of sextics with their ten nodes *named* (@not:d2-plane-sextic-base), and the objects over the unlabelled base $\bar B$ are unlabelled (@lem:d2-labelling-cover).

**The bases** are three, and the choice among them is part of the definition; the family is the same over the space $B$ and the stack $\bar B$, and there is no family over the coarse space $M_\Co$.

1. *The coarse space.* $M_\Co=U/\PGL_3$ of @not:d2-plane-sextic-base, the moduli space of [@DK13, §3] (@prop:coble-moduli-git). It is a coarse space and carries no family: a Coble surface whose automorphism group acts nontrivially on $T_\Co$ has none. Statements about $\Gamma_\Co$ are therefore not statements about base 1.
2. *The unlabelled base.* the quotient stack $\bar B=[B/S_{10}]=[V/(\SL_3\times S_{10})]$ of @not:d2-plane-sextic-base, whose coarse space is the space $V/(\SL_3\times S_{10})$ and whose points are irreducible ten-nodal sextics without names for the nodes; the family over it is @lem:d2-unpolarised-family(3) and the local system is @lem:d2-local-system, with monodromy group $\Gamma_\Co(\bar B)\supseteq\Gamma_\Co$ of index $10!$ (@lem:d2-local-system(5), @lem:gamma-co-labelled-index).
3. *The labelled base.* the space $B=V/\PGL_3$ of @not:d2-plane-sextic-base, whose points are sextics with the ten nodes named, up to projectivity; the family over it is @lem:d2-unpolarised-family(3) and its local system is @lem:d2-local-system, and the eleven classes of the next item are $\SL_3$-invariant global sections over $V$, hence descend to $B$ (@lem:d2-local-system(2)). This is the base the definition assigns to $\Gamma_\Co$.

The family over $B$ is the descent of @lem:d2-unpolarised-family(2) along the principal bundle $V\to B$ (@lem:d2-plane-sextic-freeness(4)), and its local system is @lem:d2-local-system.

**The fibres** are the surfaces $S_b=\Bl_{p_1,\dots,p_{10}}\PP^2$ for $b=(Z;p_1,\dots,p_{10})$, with $C_b$ the proper transform of $Z$; then $[C_b]=-2K_{S_b}$, $C_b^2=-4$, and the double cover of $S_b$ branched along $C_b$ is a K3 surface $X_b$ with covering involution $\iota_b$ (@lem:d2-unpolarised-family(1)).

**The local system of lattices** is $\bT$ of @lem:d2-local-system: the orthogonal complement in $R^2f_*\underline{\ZZ}_{\mcx}$ modulo torsion of the span of the classes of the pullback of a line and of the ten exceptional curves. Its fibre is $T_\Co$, its rank is $11$, and its stalks have signature $(2,9)$.

**The group.** $\Gamma_\Co\leq\Orth(T_\Co)$ is the monodromy group of $\bT$ (@lem:d2-local-system) on the labelled base $B$: the image of the monodromy representation (@def:transport-and-monodromy) of $\bT$ (@def:local-system-of-lattices) on $\pi_1(B,s)$. By @lem:d2-plane-sextic-freeness(4) it is also $\rho\qty{\pi_1(V,s)}$, and it is a subgroup of $\Orth(T_\Co)$ because $\bT$ is a local system of lattices with fibre $T_\Co$ and transport along a path is an isometry (@prop:local-system-of-lattices-monodromy). Put $\fco\definedas\bD(T_\Co)/\Gamma_\Co$.
:::

::: {.lemma #lem:d2-unpolarised-family title="The family over the labelled base exists"}

Let $b=(Z;p_1,\dots,p_{10})\in V$ and $S_b=\Bl_{p_1,\dots,p_{10}}\PP^2$, with $H$ the class of the pullback of a line and $E_1,\dots,E_{10}$ the classes of the exceptional curves.

1. $S_b$ is a Coble surface, $[C_b]=-2K_{S_b}=6H-\sum_{i=1}^{10}2E_i$ for $C_b\subset S_b$ the proper transform of $Z$, $C_b^2=-4$, $\abs{-2K_{S_b}}=\{C_b\}$, that is $h^0(-2K_{S_b})=1$, and the double cover $\pi_b\colon X_b\to S_b$ branched along $C_b$ is a K3 surface with a covering involution $\iota_b$.
2. Over $V$ there are: the universal sextic $Z_V\subset\PP^2_V$, ten disjoint sections $\sigma_1,\dots,\sigma_{10}$ given by the $p_i$, the blowup $q\colon\mcs_V\definedas\Bl_{\sigma_1,\dots,\sigma_{10}}\PP^2_V\to V$, the exceptional divisors $\mcE_1,\dots,\mcE_{10}$, the pullback $\mcH$ of $\OO_{\PP^2}(1)$, and the proper transform $\mcC_V$ of $Z_V$. The morphism $\mcs_V\to V$ is smooth, projective and flat with fibre $S_b$, the divisor $\mcC_V$ is a Cartier divisor with $\mcC_V=-2K_{\mcs_V/V}$, and $\OO(\mcC_V)=\OO(2\mcD_V)$ for $\mcD_V\definedas3\mcH-\sum_i\mcE_i$. Hence the cyclic double cover $\mcx_V\to\mcs_V$ branched along $\mcC_V$ exists, is smooth and projective over $V$, and has fibre $X_b$; its covering involution $\iota_V$ restricts to $\iota_b$.
3. The morphisms and divisors of 2. are $\SL_3$-equivariant for the action on $V$ of @not:d2-plane-sextic-base, and the $S_{10}$-action of that notation, which permutes $\sigma_1,\dots,\sigma_{10}$ and commutes with $\SL_3$, sends $\mcE_i$ to $\mcE_{\sigma^{-1}(i)}$ and $\mcH$ to $\mcH$; hence they define the same data over the space $B=V/\PGL_3$ (@lem:d2-plane-sextic-freeness(3)--(4)) and over the quotient stack $\bar B=[B/S_{10}]$, the labelled and unlabelled bases of @def:coble-family-unpolarized(2)--(3).
:::

::: {.proof}

(1) $S_b$ is nonsingular, projective and rational. The class $-K_{S_b}=3H-\sum_iE_i$ has no effective representative: if $D$ were an effective divisor of that class, then $D$ is not a component of $Z$ (a curve of degree $3$ is not a sextic), so $Z\cdot D$ is defined and is at least $\sum_i2\operatorname{mult}_{p_i}D\ge20$, while $Z\cdot D = 6\cdot3=18$ by Bézout; so $\abs{-K_{S_b}}=\emptyset$. And $\abs{-2K_{S_b}}\ni C_b\neq\emptyset$ because $[C_b]=6H-2\sum_iE_i=-2K_{S_b}$. So $S_b$ is a Coble surface in the sense of [@DZ99, Introduction]. $C_b$ is the proper transform of the irreducible curve $Z$, hence irreducible, and $C_b^2=36-4\cdot10=-4$. The double cover branched along $C_b$ is a K3 surface with a covering involution: it is smooth because $C_b$ is, and its canonical class is $\pi_b^*(K_{S_b}+\tfrac12C_b)=0$, so it is a K3 surface, as in [@DK13, §3]. And $\abs{-2K_{S_b}}=\{C_b\}$: a section of $\OO_{S_b}(6H-2\sum_iE_i)$ is a plane sextic $Z'$ with $\operatorname{mult}_{p_i}Z'\ge2$ at each $i$, and if $Z'\neq Z$ then $Z\cdot Z'=36$ by Bézout while the ten points contribute intersection multiplicity at least $4$ each, that is at least $40$, a contradiction; so $Z'=Z$, the class $-2K_{S_b}$ has the single effective divisor $C_b$, and $h^0(-2K_{S_b})=1$.

(2) The ten sections are disjoint because the $p_i$ are distinct, so their union is a closed submanifold of $\PP^2_V$ and its blowup $q$ exists and is smooth and projective over $V$; blowing up a smooth centre commuting with a smooth morphism preserves smoothness of the morphism, so $\mcs_V\to V$ is smooth, and its fibre at $b$ is $S_b$ by construction. On the fibre the proper transform of $Z_b$ has class $6H-2\sum_iE_i$, which is $-2K_{S_b}$ by (1), and $K_{\mcs_V/V}=-3\mcH+\sum_i\mcE_i$ by the blowup formula; so $\mcC_V=-2K_{\mcs_V/V}$. The line bundle $\OO(\mcD_V)$ satisfies $\OO(\mcD_V)^{\tensor2}=\OO(\mcC_V)$, so $\mcC_V$ is $2$-divisible in $\Pic(\mcs_V)$, and a $2$-divisible Cartier divisor on a smooth family is the branch divisor of a cyclic double cover [@EV92, §3, Chapter I]; the total space is smooth because $\mcC_V$ is, and it is projective over $V$ because $\OO(\mcD_V)$ is relatively ample after twisting by $q^*\OO(1)$.

(3) Each of $Z_V$, $\sigma_i$, $\mcH$, $\mcE_i$ and $\mcC_V$ is carried to itself or to its translate by an element of $\SL_3$, because $Z_V$ is the universal sextic over the linear system on which $\SL_3$ acts and the $\sigma_i$ are the coordinate sections; so the data are $\SL_3$-equivariant, and, the action of $\PGL_3$ on $V$ being free with quotient $B$ (@lem:d2-plane-sextic-freeness(3)), descend to $B$. The stack $[V/\SL_3]$ is the moduli stack of the objects of @def:coble-family-unpolarized: a point of $V$ is a labelling of the ten nodes of an irreducible sextic, two such labelings of the same sextic differ by an element of $S_{10}$ (@lem:d2-labelling-cover), and the isomorphisms of the surfaces $S_b$ are those induced by the projectivities carrying one sextic to the other, that is by $\PGL_3$ (the scalars act trivially on $V$ and on the surfaces).
:::

::: {.lemma #lem:coble-family-base-change title="Base change changes the monodromy group by a subgroup"}

Let $p\colon B'\to B$ be a continuous map of arcwise connected, locally simply connected spaces, let $(\bL,\beta)$ be a local system of lattices on $B$, and let $s'\in B'$ with $p(s')=s$.
Then the monodromy group of $p^{-1}\bL$ is $\rho\qty{p_*\pi_1(B',s')}$, the image in $\Aut(\bL_s,\beta_s)$ of the subgroup $p_*\pi_1(B',s')$ of $\pi_1(B,s)$.
In particular it is contained in the monodromy group of $\bL$, and if $p$ is a covering of finite degree then it has finite index in it.
:::

::: {.proof}

The pullback $p^{-1}\bL$ has stalk $\bL_{p(s')}$ at $s'$, and transport along a path $\gamma$ in $B'$ is transport along $p\circ\gamma$ in $B$: both are computed on sections over the interval, and $p$ carries a trivializing open set of $\bL$ to an open set on which $p^{-1}\bL$ is trivial.
So the monodromy representation of $p^{-1}\bL$ is $\rho\circ p_*$ (@def:transport-and-monodromy).
The remaining statements are those of the image of a subgroup under a group morphism, and, for a covering of finite degree, of the finite index of $\pi_1(B',s')$ in $\pi_1(B,s)$.
:::

::: {.lemma #lem:d2-local-system title="The local system of lattices, and its monodromy group"}

Let $\mcx\to\mcs\to B$ be the family of @lem:d2-unpolarised-family(3).

1. $\bV\definedas R^2f_*\underline{\ZZ}_\mcx$ modulo torsion is a local system of lattices with the cup product (@prop:primitive-cohomology-vhs(1)), of rank $22$ and signature $(3,19)$.
2. The classes $\varepsilon_0$ of $\mcH$, and $\varepsilon_1,\dots,\varepsilon_{10}$ of $\mcE_1,\dots,\mcE_{10}$, are values of global sections of $\bV$, and their span $\bM$ is a local system of lattices with fibre $M=\generators{2}\oplus\generators{-2}^{\oplus10}\cong S_\Co$, primitive in $\bV$ and of signature $(1,10)$ (@prop:coble-is-the-ten-nodal-sextic-type).
3. $\bT\definedas\bM^{\perp\bV}$ is a local system of lattices with fibre $T_\Co=M^{\perp\lkt}\cong\generators{2}\oplus E(2)$ (@prop:coble-period-domain(2), [@DK13, (3.6)]), of rank $11$ and signature $(2,9)$.
Let $B=V/\PGL_3$ and $\bar B=[B/S_{10}]=[V/(\SL_3\times S_{10})]$ be the labelled and unlabelled bases of @def:coble-family-unpolarized(2)--(3). Then the quotient map $p\colon B\to\bar B$ is a principal $S_{10}$-bundle in the category of stacks: the morphism
$$S_{10}\times B\too B\times_{\bar B}B,\qquad (\sigma,b)\longmapsto (b,\sigma b)$$
is an equivalence, and $p$ is finite étale of degree $10!=3\,628\,800$. In particular
$$1\too\pi_1(B,s)\too\pi_1(\bar B,p(s))\too S_{10}\too1$$
is exact for every $s\in B$. The induced map of coarse spaces $V/\PGL_3\to V/(\SL_3\times S_{10})$ is not asserted to be a covering: the statement proved here is about the quotient stack, and no freeness of the $S_{10}$-action on $B$ is used.
:::

::: {.proof}

*The fibre product.* The two actions commute, so $[B/S_{10}]\cong[V/(\SL_3\times S_{10})]$, and it suffices to prove the statement for the quotient map $X\to[X/H]$ of a stack $X$ by a finite group $H$. An object of $X\times_{[X/H]}X$ over a test space $T$ is a pair $(x,x')$ of objects of $X(T)$ together with an isomorphism of their images in $[X/H](T)$; such an isomorphism is an $H$-arrow; an $H$-equivariant automorphism of the trivial $H$-torsor is right multiplication by an $h\in H$, so the arrow determines $h$, and $x'\cong hx$. So the fibre product is $H\times X$ and the displayed morphism is an equivalence; $X\to[X/H]$ is then a torsor under $H$, hence finite étale of degree $\abs{H}$.

*The exact sequence.* A loop of $\bar B$ at $[s]$ is represented, in the loop model of @lem:orbifold-monodromy-of-a-quotient (which is the groupoid model of the quotient and applies verbatim to a stack $X$ in place of $\widetilde U$), by a pair $(\sigma,\tilde\gamma)$ with $\sigma\in S_{10}$ and $\tilde\gamma$ a path in $B$ from $s$ to $\sigma s$. The assignment $[(\sigma,\tilde\gamma)]\mapsto\sigma$ is a homomorphism to $S_{10}$, because loops compose by $(\sigma,\tilde\gamma)(\sigma',\tilde\delta)=(\sigma\sigma',\tilde\gamma*(\sigma\tilde\delta))$; it is onto, the constant path at $s$ representing $\sigma$; and its kernel is the set of pairs $(e,\tilde\gamma)$, that is $\pi_1(B,s)$. A kernel is normal, so the sequence is exact.

*The coarse spaces.* What is used above is the quotient stack, not its coarse space. A projectivity $g$ with $gZ=Z$ and $gp_i=p_{\sigma(i)}$ carries $(Z;p_1,\dots,p_{10})$ to $\sigma(Z;p_1,\dots,p_{10})$ in $V$, so it makes the image of $(Z;p_1,\dots,p_{10})$ in $B$ fixed by $\sigma$ in the stack sense; this is an orbifold point of $[B/S_{10}]$, and it does not affect the torsor statement, which is a statement about quotient stacks. No freeness of the $S_{10}$-action on $B$ is used above.
:::


::: {.lemma #lem:d2a-monodromy-of-the-stack title="The monodromy of the labelled base is the monodromy on $V$"}

Let $G$ be a connected complex Lie group acting on a connected complex analytic space $V$, and let $\bL$ be a $G$-equivariant local system of lattices on $V$: a local system with isomorphisms $\varphi_g(v)\colon\bL_v\to\bL_{gv}$ for $g\in G$ and $v\in V$, continuous in $(g,v)$, with $\varphi_e=\id$ and $\varphi_{gh}(v)=\varphi_g(hv)\circ\varphi_h(v)$; this is the same datum as a local system of lattices on the quotient stack $[V/G]$. Let $s\in V$ and identify $\bL_s$ with a lattice $T$.

1. Every loop of $[V/G]$ at $[s]$ is homotopic, in the loop model of @lem:orbifold-monodromy-of-a-quotient, to a loop of $V$ at $s$.
2. The monodromy group of $\bL$ on $[V/G]$ equals the image $\rho\qty{\pi_1(V,s)}\leq\Orth(T)$ of the monodromy representation of $\bL$ on $V$.
3. For $G=\SL_3$ acting on $V$ as in @not:d2-plane-sextic-base and $\bL=\bT$ of @lem:d2-local-system, which is $\SL_3$-equivariant by @lem:d2-unpolarised-family(3), this gives $\Gamma_\Co=\rho\qty{\pi_1(V,s)}$: the group of @def:coble-family-unpolarized is the monodromy group of the family over the labelled base.
:::

::: {.proof}

*The loops of the stack.* In the loop model of @lem:orbifold-monodromy-of-a-quotient an orbifold loop of $V/G$ at $[s]$ is represented by a pair $(g,\tilde\gamma)$ with $g\in G$ and $\tilde\gamma$ a path in $V$ from $s$ to $gs$. What is used here is that model, an orbifold loop being a pair $(g,\tilde\gamma)$, and not the exact sequence stated in that lemma, whose quotient by $\Gamma$ is stated for a discrete group; for a connected $G$ the group element of a loop is homotopic to a path in $V$, which is what the next paragraph proves. The transport of $\bL$ along the pair is
$$\varphi_g(s)^{-1}\circ\tilde\gamma^*,$$
the second factor being the transport along $\tilde\gamma$ (@def:transport-and-monodromy) and the first the identification of the fibre at $gs$ with the fibre at $s$ given by the equivariance. A general loop of the stack is a finite concatenation of paths in $V$ and of such pairs, so it is enough to treat one pair.

*The group element is a path in $V$.* Because $G$ is connected, choose $\beta\colon[0,1]\to G$ with $\beta(0)=e$ and $\beta(1)=g$. For $x\in\bL_s$ the assignment $t\mapsto\varphi_{\beta(t)}(s)(x)$ is a section of the pullback of $\bL$ along $t\mapsto\beta(t)s$ over $[0,1]$, with value $x$ at $t=0$ because $\varphi_e=\id$; the transport of $\bL$ along that path is therefore $\varphi_g(s)$ (@def:transport-and-monodromy, @lem:local-system-on-interval). With $\sigma$ the path $t\mapsto\beta(1-t)s$ from $gs$ to $s$, the transport along the loop $\tilde\gamma\cdot\sigma$ of $V$ at $s$ is
$$\sigma^*\circ\tilde\gamma^*=\varphi_g(s)^{-1}\circ\tilde\gamma^*$$
(@prop:transport-homotopy-invariant(2)), which is the operator above.

*The monodromy group.* Every monodromy operator of $\bL$ on the stack is therefore the transport along a loop of $V$ at $s$, so the monodromy group of the stack is contained in $\rho\qty{\pi_1(V,s)}$. Conversely a loop of $V$ at $s$ is the loop of the stack with $g=e$, so it is contained in the monodromy group of the stack. This is (2).

*Homotopy.* The same computation on homotopy classes: for $u\in[0,1]$ the path $\sigma_u\colon t\mapsto\beta(1-ut)s$ runs from $gs$ to $\beta(1-u)s$, so the pairs $\bigl(\beta(1-u),\tilde\gamma\cdot\sigma_u\bigr)$ are a family of loops of the stack, from $(g,\tilde\gamma)$ at $u=0$ to the loop $\tilde\gamma\cdot\sigma$ of $V$ at $u=1$, with the group element varying continuously from $g$ to $e$. This is (1).

*The group and the space.* $\SL_3(\CC)$ is connected: $\SL_n(\CC)$ is generated by the elementary matrices $E_{ij}(\lambda)=\id+\lambda e_{ij}$ (Gaussian elimination), and $t\mapsto E_{ij}(t\lambda)$ is a path from the identity to $E_{ij}(\lambda)$. The space $V$ is connected (@not:d2-plane-sextic-base) and is a complex analytic space, hence locally contractible. The family and the eleven classes of @lem:d2-local-system are $\SL_3$-equivariant (@lem:d2-unpolarised-family(3)), so the isomorphisms $\varphi_g$ are defined for $\bT$ and (2) applies, which is (3).

*The choices.* A path from $s$ to $s'$ conjugates $\rho\qty{\pi_1(V,s)}$ to $\rho\qty{\pi_1(V,s')}$, and another isometry $\bL_s\iso T$ conjugates the subgroup in $\Orth(T)$; so the group is well defined up to conjugacy, and is a subgroup of $\Orth(T_\Co)$ once the isometry of @def:coble-family-unpolarized is fixed.
:::

::: {.lemma #lem:coble-family-labelled-monodromy title="The labelled family has monodromy in $\widetilde\Orth^+ (T_\Co)$"}

On base 3 of @def:coble-family-unpolarized, the labelled base, the monodromy group $\Gamma_\Co$ of $\bT$ is contained in $\widetilde\Orth^+(T_\Co)$.
:::

::: {.proof}

The eleven classes of @lem:d2-local-system(2) are values at $s$ of global sections of $\bV$, and $\bM$ is their span, primitive and nondegenerate of signature $(1,10)$ (@lem:d2-local-system(2), @prop:coble-is-the-ten-nodal-sextic-type).
So @cor:lattice-polarized-k3-monodromy applies: the restriction of the monodromy to $T_\Co=\bM^{\perp\bV}$ takes values in $\widetilde\Orth^+(T)$.
That group is $\Orth^+(T_\Co)\intersect\discriminantkernel{T_\Co}$, which is $\widetilde\Orth^+(T_\Co)$ (@def:gamma-co-groups(3), @prop:gamma-co-images(1)).
:::

::: {.lemma #lem:d2-labelling-cover title="The labels are a principal $S_{10}$-bundle of stacks"}

4. $\Gamma_\Co=\rho\qty{\pi_1(B,s)}$ is a subgroup of $\Orth(T_\Co)$ (@lem:d2-plane-sextic-freeness(4)), and it lies in $\Orth^+(T_\Co)$ (@lem:monodromy-is-spinor-positive).
5. On $\bar B$ the same construction gives a local system of lattices with fibre $T_\Co$ and monodromy group $\Gamma_\Co(\bar B)$ containing $\Gamma_\Co$, of index $10!$ (@lem:gamma-co-labelled-index); the classes $\varepsilon_i$ are permuted by the elements of $S_{10}$ and fixed by no other generator.
:::

::: {.proof}

(1) is [@prop:primitive-cohomology-vhs(1)], the fibres being K3 surfaces by @lem:d2-unpolarised-family(1). (2) Each $\mcE_i$ is a relative divisor, so its class is a global section of $\bV$; so is $\mcH$. The fibre of the span is spanned by the classes $e_0,\dots,e_{10}$ of [@DK13, §3], which is $M$ there, primitive in $L_{\mathrm{K3}}$ and of signature $(1,10)$; primitivity is an open condition on the fibre, so the span is primitive throughout (@prop:coble-is-the-ten-nodal-sextic-type). (3) is the orthogonal complement of (2) in (1). (4) Transport is an isometry (@prop:local-system-of-lattices-monodromy), and the monodromy of a family over a connected base lies in one component of the orthogonal group, the one preserving the period (@lem:monodromy-is-spinor-positive). (5) The map of quotient stacks $B\to\bar B$ is a principal $S_{10}$-bundle of stacks (@lem:d2-labelling-cover), so $\pi_1(B)$ is a normal subgroup of $\pi_1(\bar B)$ with quotient $S_{10}$, the pullback $\bT|_B$ is the system of $\bar B$ pulled back, and its monodromy is the restriction of that of $\bar B$ (@lem:coble-family-base-change); the index is $\abs{S_{10}}=10!$. The action of a permutation of the labels on the classes $\varepsilon_i$ is the permutation of the corresponding sections, and $\PGL_3$ acts trivially on the cohomology classes of the fibre.
:::

::: {.lemma #lem:d2a-period-map title="The period map of the base is the map of Dolgachev--Kondo"}

Let $\per_B\colon B\to\bD(T_\Co)/\Orth(T_\Co)$ be the period map of the family of @def:coble-family-unpolarized: fix $s\in B$ and an isometry $\bT_s\iso T_\Co$, and send $b$ to the class of the isometry-induced image of $H^{2,0}(X_b)$ (@prop:lifted-period-map(4)). Then:

1. $\per_B$ is holomorphic and equivariant for the monodromy representation of $\bT$, inducing $\per\colon B\to\bD(T_\Co)/\Gamma_\Co$ (@eq-period-map-equivariance).
2. The composite $B\to M_\Co\xrightarrow{\per_{\mathrm{DK}}}\bD(N)/\Orth(N)$, $N=T_\Co$, in which the first map forgets the sextic and the second is the map of [@DK13, Prop. 3.2], is $\per_B$: a Coble surface $S$ is carried to the Hodge structure $H^{2,0}(X)\subset H^2(X,\CC)$ of its K3 double cover, read through an isometry $T_\Co\cong N$ of [@DK13, (3.6)].
3. $\per_{\mathrm{DK}}$ is an isomorphism onto an open subset [@DK13, Prop. 3.2], and the hypotheses of that statement are those checked in @lem:d2-unpolarised-family(1): $X_b$ is an algebraic K3 surface, and $M_{X_b}\cong M$, $N_{X_b}\cong N$ [@DK13, §3].
:::

::: {.proof}

(1) is @prop:lifted-period-map(4) and @eq-period-map-equivariance. For (2), both maps send a point to the Hodge structure of the K3 double cover; the map of [@DK13, Prop. 3.2] is defined as the one "the Torelli-type theorem for algebraic K3 surfaces implies", that is by the Torelli theorem, which identifies a K3 surface with the Hodge structure on $H^2$; the period map of a family of K3 surfaces is that same assignment, so the two agree. (3) is the cited statement, whose hypotheses are those of the citation and are the ones listed.
:::

::: {.lemma #lem:d2-degree-two-polarization title="The degree-$2$ polarization of a Coble surface and the polarization vector of the Enriques quotient"}

Let $S=\Bl_{p_1,\dots,p_{10}}\PP^2$ be a classical Coble surface, $f\colon X\to S$ its K3 double cover, and $S_\Co\definedas f^*\Pic(S)\cong M$ and $K_S^{\perp}\cong E_{10}$ (@prop:canonical-perp-is-e10).

1. $f^*\colon\Pic(S)\to H^2(X)$ doubles the form, $f^*(x)\cdot f^*(y)=2\,x\cdot y$; its image is $S_\Co$; and $f^*(K_S^{\perp})$ is the orthogonal complement of $f^*H$ in $S_\Co$, of rank $10$, isometric to $U(2)\oplus E_8(2)$.
2. Let $h_\Co\in K_S^{\perp}$ be a degree-$2$ numerical polarization of @def:coble-polarization-classes(2), $h_\Co=F_1+F_2$ with $F_i^2=0$ and $F_1\cdot F_2=1$. Then $\tilde h\definedas f^*h_\Co$ has $\tilde h^2=4$, $\tilde h=f^*F_1+f^*F_2$ with $(f^*F_i)^2=0$ and $f^*F_1\cdot f^*F_2=2$, and $f^*$ identifies the sublattice $\generators{F_1,F_2}\cong U$ with $\generators{f^*F_1,f^*F_2}\cong U(2)$.
3. Consequently $\tilde h$ is the polarization vector $h=e+f$ of [@AEGS25, Def. 2.5], $e,f$ the basis of $U(2)$ with $e^2=f^2=0$ and $e\cdot f=2$: the degree-$2$ numerical polarization $h_\Co$ of the Coble surface and the degree-$2$ polarization vector that [@AEGS25, Def. 2.5] fixes are the same vector of $S_\Co$, namely $f^*(h_\Co)$.
4. No automorphism $g$ of $X$ with $g\circ\iota'=\iota'\circ g$ has $H^2(X)^g=f^*(K_S^{\perp})$: the invariant lattice $S_\En$ is not the invariant lattice of an effective involution of $X$ commuting with $\iota'$, so the two degree-$2$ structures are compared through $f^*$ and not through a second involution of the same K3.
:::

::: {.proof}

(1) For a divisor class $x$ on $S$, $f^*(x)\cdot f^*(y)=2\,x\cdot y$ by the projection formula and $\deg f=2$. The image is $S_\Co\cong M$ by [@DK13, §3], where the classes $e_0,\dots,e_{10}$ of $f^*H,f^*E_1,\dots,f^*E_{10}$ generate it. Since $H\cdot K_S^{\perp}=0$, the image $f^*(K_S^{\perp})$ is orthogonal to $f^*H=e_0$; it has rank $10$ and $S_\Co$ has rank $11$, so it equals $e_0^{\perp}\cap S_\Co$. Its isometry class is that of $K_S^{\perp}(2)\cong E_{10}(2)=U(2)\oplus E_8(2)$ (@prop:canonical-perp-is-e10).
(2) is the computation of (1) applied to $F_1,F_2$: $F_i^2=0$ gives $(f^*F_i)^2=0$, and $F_1\cdot F_2=1$ gives $f^*F_1\cdot f^*F_2=2$; $h_\Co^2=(F_1+F_2)^2=2$ gives $\tilde h^2=4$.
(3) In $U(2)$ with basis $e,f$ one has $e^2=f^2=0$, $e\cdot f=2$ and $(e+f)^2=4$, which is (2) under the isometry $\generators{f^*F_1,f^*F_2}\cong U(2)$; the vector $h=e+f\in U(2)=S_{\dP}\subset S_\En$ is the one [@AEGS25, Def. 2.5] fixes as the polarization in both of its period problems, and $S_\En=U(2)\oplus E_8(2)$ is the lattice of (1).
(4) Put $M\definedas H^2(X)^{\iota'}=f^*H^2(S)$, of rank $11$. The class $[R]$ of the ramification curve $R\subset X$ of $f$ is $f^*(-K_S)$: indeed $f^*C_b=2R$ with $C_b=-2K_{S_b}$ (@lem:d2-unpolarised-family(1)), so $R=f^*(-K_S)$, $R^2=2(-K_S)^2=-2$, and $R\cdot f^*(K_S^{\perp})=2(-K_S)\cdot K_S^{\perp}=0$. Hence $f^*(K_S^{\perp})$ and $[R]$ are orthogonal sublattices of $M$ of ranks $10$ and $1$, and their ranks sum to $\mathrm{rk}M$, so they span $M$. An automorphism $g$ with $g\circ\iota'=\iota'\circ g$ preserves $M=H^2(X)^{\iota'}$, and $H^2(X)^g=f^*(K_S^{\perp})$ forces $g^*=-1$ on the orthogonal complement of $f^*(K_S^{\perp})$ in $M$, that is $g^*[R]=-[R]$. Since $H^2(X)$ is unimodular and $g$ is an involution, $g_*=(g^*)^{-1}=g^*$, so for the nef and big class $e_0=f^*H$ one has $(g^*e_0)\cdot R=e_0\cdot(g_*R)=e_0\cdot(-R)=-2\,H\cdot(-K_S)=-6<0$, while $R$ is an effective curve; so $g^*e_0$ is not nef, and $g^*$ cannot be induced by an automorphism, which carries the nef cone to itself.
:::

::: {.definition #def:coble-family-degree-two title="D2b: the family of degree-$2$ polarized Coble surfaces"}

**The objects.** Over a complex space $Y$, an object is a tuple $\qty{\mcs\to Y,\ \mcx\to\mcs,\ \tilde h}$ in which

1. $\mcs\to Y$ is an object of @def:coble-family-unpolarized, with its K3 double cover $\mcx\to\mcs$ and involution $\iota$;
2. $\tilde h$ is a global section of the local system of lattices $f^*(K^\perp)$ of @lem:d2-degree-two-polarization(1), whose value at every $y\in Y$ is the pullback of a degree-$2$ numerical polarization of $S_y$ in the sense of @def:coble-polarization-classes(2): $\tilde h_y=f^*F_1+f^*F_2$ with $F_i^2=0$, $F_1\cdot F_2=1$, $\tilde h_y^2=4$, and $F_1,F_2$ nef.

By @lem:d2-degree-two-polarization(3) this is the same datum as a global section $h$ of the local system with fibre $S_\En=U(2)\oplus E_8(2)$ whose value is the vector $h=e+f$ of [@AEGS25, Def. 2.5]; the section is part of the objects and is not a marking: it is the polarization.

**The fibres** are the Coble surfaces $S_y$ of @def:coble-family-unpolarized with their degree-$2$ numerical polarization $h_{\Co,y}$; the K3 cover $X_y$ is a K3 surface with a marked class $\tilde h_y$ of square $4$.

**The base** is $\Delta_2\subset\fentwo$, the image of the hyperplanes $\alpha^{\perp}$ for $\alpha\in\ten$ a $(-2)$-vector, which is the whole base and not a sublocus of it (@lem:d2-degree-two-base).

**The local system of lattices** is $\bT$ of @lem:d2-local-system, the orthogonal complement of $\bM$ in $R^2f_*\underline\ZZ_\mcx$ modulo torsion; the polarization is a section of $\bM$, so $\bT$ is the same system for the polarized and the unpolarized family, and its fibre is $T_\Co$.

**The group.** $\Gamma_{\Co,2}\leq\Orth(T_\Co)$ is the image of the monodromy representation of $\bT$ (@def:gamma-co-groups(5)). It is a subgroup of the restricted stabilizer $R_{\gent}$ of @def:gamma-co-groups(4) (@lem:d2-degree-two-base(3)). Put $F_{\Co,2}\definedas\bD(T_\Co)/\Gamma_{\Co,2}$.
:::

::: {.lemma #lem:d2-degree-two-base title="The base of D2b is all of $\Delta_2$"}

Let $R_{\gent}$ be the restricted stabilizer of @def:gamma-co-groups(4) and $\Gamma_{\tilde h}$ the group of pairs of type $\tilde h$ of @prop:coble-polarized-moduli, and $\Delta_2=\mch_{-2}/\gent\subset\fentwo=\bD(\ten)/\gent$.

1. $\Gamma_{\tilde h}=R_{\gent}$ [@prop:coble-degree-two-space(2)], so $\bD(T_\Co)/\Gamma_{\tilde h}=\bD(T_\Co)/R_{\gent}$ is the moduli space of pairs $(S,h_\Co)$ of @def:coble-family-degree-two and, by @thm:normalization with $\Gamma=\gent$, it is the normalization of $\Delta_2$: the map $\bD(T_\Co)/R_{\gent}\to\fentwo$ is finite, its image is $\Delta_2$, and it is birational.
2. Hence $\Delta_2$ is the coarse space of @def:coble-family-degree-two up to normalization, and in particular it is the whole base: the period map of the family lands in $\bD(T_\Co)/\Gamma_{\Co,2}\to\bD(T_\Co)/R_{\gent}$, whose image is $\Delta_2$, and no proper sublocus of $\Delta_2$ contains it.
3. $\Gamma_{\Co,2}\leq R_{\gent}\cap\Orth^+(T_\Co)$.
4. $\Delta_2$ is irreducible.
:::

::: {.proof}

(1) The first identity is [@prop:coble-degree-two-space(2)], whose proof identifies the stabilizer of $\tilde h$ in the isometries of $\lkt$ preserving $S_\Co$ with the image of $\Stab_{\gent}(\delta)$ in $\Orth(T_\Co)$. The moduli interpretation is @prop:coble-polarized-moduli(2)--(3): the period of a pair of type $\tilde h$ is well defined in $\bD(T_\Co)/\Gamma_{\tilde h}$, two Picard-general pairs are isomorphic exactly when their periods agree, and every point of the fibre of $\bD(T_\Co)/\Gamma_{\tilde h}\to\bD(T_\Co)/\Orth(T_\Co)$ is the period of such a pair. The remaining statements are @thm:normalization with $\Gamma=\gent$, whose three hypotheses are its own: $R_{\gent}$ is the image of $\Stab_{\gent}(\delta)$ (@prop:gamma-co-images(3)), $T_\Co=\delta^{\perp\ten}$, and $\bD(T_\Co)/R_{\gent}$ is normal.
(2) A moduli problem whose marked period space is the normalization of a variety has that variety as its coarse space up to normalization; the composite $\bD(T_\Co)/R_{\gent}\to\Delta_2\hookrightarrow\fentwo$ is finite and surjective by (1), so its image is all of $\Delta_2$ and not a proper sublocus.
(3) A monodromy operator of the family of @def:coble-family-degree-two preserves the local system $\bM$ of @lem:d2-local-system(2) and its section $\tilde h$, so its image in $\Orth(T_\Co)$ is the restriction of an isometry $\gamma$ of $\lkt$ with $\gamma(S_\Co)=S_\Co$ and $\gamma(\tilde h)=\tilde h$, that is an element of $\Gamma_{\tilde h}=R_{\gent}$; and it lies in $\Orth^+(T_\Co)$ by @lem:d2-local-system(4).
(4) $\Delta_2$ is the image of the irreducible $\bD(T_\Co)$ under a finite morphism, hence irreducible; equivalently $\gent$ is transitive on the $(-2)$-vectors of $\ten$ [@Ste91, (2.10) and the paragraph after it].
:::

::: {.remark #rmk:d2-degree-two-vs-DK13 title="The moduli space $\mcm_\Co(2)$ of Dolgachev--Kondo"}

[@DK13, §8] considers, for an unnodal Coble surface, a polarization $h=[F_1+F_2]$ of degree $2$, corresponding to an embedding $U\injects E$ of the Enriques lattice into $K_S^{\perp}$, and writes the resulting moduli space $\mcm_\Co(2)$; the rational map $\Phi'\colon\mcm_\Co(2)\dashrightarrow\mcm_\Co$ has degree $2^7\cdot17\cdot31$ [@DK13, §8]. That is the same moduli problem as @def:coble-family-degree-two: by @lem:d2-degree-two-polarization the class $h_\Co=F_1+F_2$ is the vector $\tilde h$ of type $\Gamma_{\tilde h}$, so the marked space of $\mcm_\Co(2)$ is $\bD(T_\Co)/\Gamma_{\tilde h}$, which is the normalization of $\Delta_2$ by @lem:d2-degree-two-base(1); and the degree of $\Phi'$ is the index $[\Orth(T_\Co):\Gamma_{\tilde h}]=[\Orth(T_\Co):R_{\gent}]=2^7\cdot17\cdot31=67\,456$ of @prop:coble-degree-two-space(2), as it must be. The unnodal locus is the complement of the $(-2)$-Heegner divisors in $\bD(T_\Co)$, so $\mcm_\Co(2)$ is an open subset of the normalization of $\Delta_2$ and the two agree birationally. The two objects are therefore not different, as @rmk:degree-two-two-meanings(3) formerly recorded, but the same moduli problem read on the two sides of the cover.
:::

::: {.remark #rmk:degree-two-two-meanings title="The meanings of degree $2$"}

The phrase occurs in three senses, and two of them agree.

1. *The Coble polarization.* That of @def:coble-family-degree-two and of @def:coble-polarization-classes(2): a class $h_\Co\in K_S^{\perp}$ with $h_\Co^2=2$, split as $F_1+F_2$ with $F_i^2=0$, $F_1\cdot F_2=1$ [@DK13, §8]. This is the object D2b asks for, and its base is $\Delta_2$ (@lem:d2-degree-two-base).
2. *The Enriques polarization.* The same class read on the K3 cover: $\tilde h=f^*h_\Co\in S_\En=U(2)\oplus E_8(2)$, of square $4$, which is the vector $h=e+f$ of [@AEGS25, Def. 2.5] fixed by $\gent$ [@AEGS25, Def. 2.6] (@lem:d2-degree-two-polarization). Readings 1 and 2 are the same datum, which is why the divisor $\Delta_2$ of the Enriques period domain and the degree-$2$ polarized Coble moduli space coincide up to normalization; and it is why the base is a divisor of $\fentwo$ and not of the whole space.
3. *The plane model.* The degree is $H^2=2$ of the K3 double cover $X\to\PP^2$ itself, that is the statement that $X$ is a double plane whose branch sextic is $Z$ and whose Coble quotient is $S=\Bl_{10}\PP^2$ (@prop:coble-period-domain(1), @prop:coble-is-the-ten-nodal-sextic-type). It restricts nothing: every classical Coble surface has it, so on this reading the base is the whole of $B$ and not a divisor.

Readings 2 and 3 are not interchangeable: reading 2 is a condition on the Enriques quotient, which is one quotient of the K3 surface and is not the Coble surface, whereas reading 3 is automatic, and a definition that used it would define the unpolarized moduli problem again under another name.
:::

::: {.remark #rmk:d2-what-is-open title="What no source read supplies"}

1. **The coarse space and the family.** $M_\Co$ is a coarse space and carries no family; the family of D2a lives over $B$, which is what @lem:d2-unpolarised-family(3) and @lem:d2-plane-sextic-freeness(4) construct. Nothing here claims a universal family over $M_\Co$, and none exists: a Coble surface with nontrivial automorphism acting nontrivially on $T_\Co$ has no universal family over the coarse space. The local system over $M_\Co$ is accordingly not defined, and statements about $\Gamma_\Co$ are statements about the labelled base $B$.
2. **The comparison of the bases.** $B\to\bar B$ is the principal $S_{10}$-bundle of stacks of @lem:d2-labelling-cover, with coarse space $V/(\SL_3\times S_{10})$ over $B$, and $\bar B\to M_\Co$ forgets the sextic; whether the second is birational, that is whether a ten-nodal sextic is determined by its ten nodes, is not proved here. What is proved is that the labelled base has group $\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable) and the unlabelled one $\Gamma_{10A_1}$, and that the index $[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]$ is $10!$ (@thm:gamma-co-sextic-group(3)); that index is the degree of the comparison.
3. **The reverse inclusion for the degree-$2$ family.** @lem:d2-degree-two-base(3) gives $\Gamma_{\Co,2}\leq R_{\gent}\cap\Orth^+(T_\Co)$. The equality is @qst:coble-monodromy-equality and is not asserted; nothing in this section asserts it.
4. **Ample against nef.** [@AEGS25, §1] asks for an *ample* numerical polarization of degree $2$, whereas the degree-$2$ polarized Coble moduli space is defined with a *nef* class of square $2$ [@DK13, §7], called an almost polarization in [@Ste91, §2]. The two conditions differ on the boundary of the cone of curves: $h=F_1+F_2$ with $F_1,F_2$ nef is nef and big on a Picard-general surface (@prop:coble-degree-two-space(1)) but the degenerate split $h=2F_1+R$ with $R$ a $(-2)$-curve is not ample [@DK13, §7]. The base $\Delta_2$ of @def:coble-family-degree-two is the arithmetic divisor and needs neither adjective.
5. **The compactification.** Both definitions are stated over the open base. Their extensions over the boundary, and which boundary strata are Coble, are not part of D2 and are not asserted.
:::

::: {.remark #rmk:d2-corrections title="What this section corrects"}

Five corrections to the earlier form of this section, each at its file and line in the commit that introduces this remark.

1. *The family is constructed, not declared.* The earlier definition listed three bases and called the choice part of the definition, while the base named for $\Gamma_\Co$ carried no family; @lem:d2-unpolarised-family now constructs the family and @lem:d2-local-system its local system, and the group is the monodromy of that system.
2. *The labels are a torsor of stacks, not a principal bundle of coarse spaces.* The finite-cover statement, formerly introduced without proof, is @lem:d2-labelling-cover, which proves the torsor statement for the quotient stacks and records that the induced map of coarse spaces is not a covering.
3. *The degree-$2$ object is the Coble polarization.* The earlier definition took an ample degree-$2$ class on the Enriques quotient instead of the class $h_\Co\in K_S^{\perp}$ of @def:coble-polarization-classes(2); @lem:d2-degree-two-polarization proves that the two are the same class on the K3 cover, so the definition can and now does use the Coble class, which is the one @def:gamma-co-groups(5) names.
4. *The base is $\Delta_2$ by normalization, not by inheritance.* The earlier proof applied the pointwise description of the divisor in the full quotient $\bD(\ten)/\Orth(\ten)$ through the finite map $\fentwo\to\bD(\ten)/\Orth(\ten)$ in the wrong direction; @lem:d2-degree-two-base now identifies the two period spaces directly, through @thm:normalization and @prop:coble-degree-two-space(2).
5. *The reverse inclusion does not use a period map, and the label cover is a torsor of stacks.* The earlier proof of $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_\Co$ applied a period map $\per_M\colon V\to\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ and asserted that it is injective; it is not, since $\PGL_3$-orbits in $V$ give isomorphic $M$-marked K3 covers. The earlier form of @lem:d2-labelling-cover then asserted a principal $S_{10}$-bundle of the coarse spaces $B\to\bar B$, which need not be a covering: a projectivity carrying a sextic to itself and permuting its nodes identifies two points of $B$ over one point of $\bar B$. @lem:d2-labelling-cover now proves the torsor statement for the quotient stacks, @lem:gamma-co-labelled-index gives $\Gamma_\Co(B)=\Gamma_\Co(\bar B)\cap\ker\bar\rho$ and the index $10!$, and @thm:gamma-co-is-stable obtains the reverse inclusion from $\Gamma_\Co(\bar B)=\Gamma_{10A_1}$ (@thm:gamma-co-sextic-group), which is the period isomorphism on the unlabelled base.
:::
