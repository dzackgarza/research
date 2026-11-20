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

Here $\tdp$ is the lattice of [@AEGS25], and $\eta\colon T_\Co\injects\ten$ is the embedding of @lem:primitive_embedding_eta.
The quotient $F^K_{\En} = \bD(\ten)/\Gamma^K_{\En}$, with $\Gamma^K_{\En} = \Orth(\ten)$ the group $\Gamma_{\mathrm{Enr}}$ of [@AEGS25], has two $0$-cusps $(10,10,0)_1$, $(10,8,0)_1$ and two $1$-cusps $(8,8,0)_0$, $(8,6,0)_0$ [@AEGS25, §2]. The quotient $\fentwo = \bD(\ten)/\gent$, with $\gent = \Gamma^K_{\En}\intersect\Gamma_{\dP}$, has five $0$-cusps [@AEGS25, §3]. Throughout, $\Gamma_\En$ denotes the stable group $\widetilde\Orth^+(\ten)$, also written $\Orth^+(\ten)^*$ (@def:gamma-co-groups, @sec-heegner-line, @thm:normalization, @def:gamma-co-en).
The group $\Gamma_\Co$ is the monodromy group of the family of unpolarized Coble surfaces that the family of unpolarized Enriques surfaces induces, and $\fco = \bD(T_\Co)/\Gamma_\Co$ (@def:gamma-co-groups).

The objects, bases, local systems of lattices and period maps of the two families on which $\Gamma_\Co$ and $\Gamma_{\Co,2}$ are taken are those of @sec-coble-families-d2: the unpolarized family with its three bases (@def:coble-family-unpolarized), whose period map on the first of them is the map of [@DK13, Prop. 3.2, printed p. 513] (@lem:d2a-period-map), and the degree-$2$ family over the discriminant divisor (@def:coble-family-degree-two), whose base is the whole of that divisor (@lem:degree-two-base-is-delta-two).
The equality $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$ is @conj:gamma-co-stable: the sign half of $\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co)$ is proved (@lem:monodromy-is-spinor-positive), and on base 1 of D2a the equality is **false** (@thm:gamma-co-is-full), the discriminant half failing at the $(-4)$-reflection of @cor:gamma-co-inclusions; it survives only on bases 2 and 3 of D2a (@rmk:gamma-co-d2a).
The group $\Gamma_{\Co,2}$ of $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ is the monodromy group of the VHS of the degree-$2$ Coble family (@def:gamma-co-groups(5)). The group that the Enriques datum defines is $R_{\gent} = \bar\rho^{-1}(P)$, the image of the stabilizer of $\delta$ in $\gent$ (@prop:gamma-co-images(3)); it is not the monodromy group, and $\Gamma_{\Co,2} = R_{\gent}$ is false (@thm:coble-monodromy-versus-enriques(3)). The monodromy group lies in $R_{\gent}\intersect\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(4), from @lem:coble-monodromy-in-stabilizer conditional on (U) of @lem:coble-family-identification; (U) and (F) are D2 of research#786, and the definitions they ask for are @sec-coble-families-d2, with (U) supplied by @prop:d2-degree-two-supplies-U).
The stable subgroup $\widetilde\Orth^+(T_\Co)$ is the kernel of the action on $A_{T_\Co}$ of each of the groups $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ of @sec-gamma-co-comparison, and both inclusions are strict, of index $\abs{W(E_8)} = 696\,729\,600$ (@prop:gamma-co-heegner-strict, @prop:theta-co-index).

::: {.remark title="The group $\Gamma_{\Co,2}$, explicitly"}
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
The vertical map is $F_{\Co}\to F_{\Co,2}$, finite of degree $[\Gamma_{\Co,2}:\Gamma_\Co]$ once $\Gamma_\Co\subseteq\Gamma_{\Co,2}$; under @conj:gamma-co-stable together with @qst:coble-monodromy-equality, $\Gamma_\Co = \widetilde\Orth^+(T_\Co)\subseteq R_{\gent}\intersect\Orth^+(T_\Co) = \Gamma_{\Co,2}$ and the degree is $[\Gamma_{\Co,2}:\widetilde\Orth^+(T_\Co)] = \abs{W(E_8)} = 696\,729\,600$ (@rmk:coble-monodromy-counts), the index $2\abs{W(E_8)}$ of @thm:gamma-co-2-comparison(4) being the index of the larger group $R_{\gent}$. The identification $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$ is exactly the conjecture.

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

1. The double cover $\pi\colon X\to Y$ branched in $B$ is a K3 surface with a del Pezzo involution $\idp$ such that $Y = X/\idp$. The involution $\tau$ lifts to a basepoint-free involution $\ien$ of $X$ that commutes with $\idp$, and $Z = X/\ien$ is an Enriques surface [@AEGS25, §2.1, p. 584].
2. Certain mildly singular $\tau$-invariant equations $f(x,y)$ of bidegree $(4,4)$ that vanish at a torus-fixed point correspond to Coble surfaces, which are $\ZZ/2$ quotients of nodal K3 surfaces [@AEGS25, §2.1, p. 585; @Hor77].
3. There is a unique $(-2)$-vector $\alpha\in\ten$ modulo $\Orth(\ten)$. The divisor $\Delta = \alpha^\perp\iscontainedin\bD(\ten)/\Orth(\ten)$ parametrizes quotients of nodal K3 surfaces by an involution that fixes a node. These are rational Coble surfaces with a $\tfrac14(1,1)$ singularity [@AEGS25, §2.3, p. 587].

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
[@DK13, §3].
:::

::: {.proposition #prop:enriques-nodal-coble-heegner title="Enriques, nodal Enriques and Coble surfaces in the Enriques period domain"}

Let $\ten = U\oplus E_{10}(2)$ be the orthogonal complement in $\lkt$ of the pullback $E_{10}(2)$ of the numerical lattice of an Enriques surface to its K3 cover.
The group $\Orth(\ten)$ is the group $\Gamma^K_\En$ of the opening display, and it contains the group $\Orth^+(\ten)^*$ of $\fen$.

1. The period point of the K3 cover of an Enriques surface does not lie in $\mch_{-2}$.
   The quotient $\bD(\ten)/\Orth(\ten)$ is a normal quasi-projective variety of dimension $10$, and $\qty{\bD(\ten)\sm\mch_{-2}}/\Orth(\ten)$ is the moduli space $\mcm_\En$ of Enriques surfaces [@DK13, §3].
2. There are two $\Orth(\ten)$-orbits of $(-4)$-vectors in $\ten$ [@AEGS25, §2.3].
   One orbit consists of the vectors $\delta$ with $\delta^{\perp\ten}\cong T_\Nod = U\oplus\generators{4}\oplus E_8(2)$; let $\mch^{\mathrm{nod}}_{-4}\iscontainedin\mch_{-4}$ be the union of their hyperplanes.
   The divisor $\mcm^{\mathrm{nod}}_\En \definedas \qty{\mch^{\mathrm{nod}}_{-4}\sm\mch_{-2}}/\Orth(\ten)$ parametrizes nodal Enriques surfaces [@AEGS25, §2.3].
   The quotient $\bD(T_\Nod)/\Orth(T_\Nod)$ is a quasi-projective variety of dimension $9$, and $\mcm^{\mathrm{nod}}_\En$ is birationally isomorphic to it [@DK13, §3, Prop. 3.1, p. 512].
   The other orbit gives the divisor of unigonal Enriques surfaces (@prop:coble-and-unigonal-heegner-divisors).
3. The quotient $\mch_{-2}/\Orth(\ten)$ is birationally isomorphic to the moduli space $\mcm_\Co$ of Coble surfaces (@prop:coble-moduli-heegner-divisor).

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
2. The orthogonal complement of this sublattice in $H^2(X,\ZZ)\cong\lkt$ is a $2$-elementary lattice of signature $(2, 9)$ with discriminant form $-q_{S_\Co}$ [@DK13, §3; @Nik80, Cor. 1.6.2, printed p. 112]. Its isomorphism class is determined by $-q_{S_\Co}$ [@DK13, §3; @Nik80, Thm. 3.6.2, printed p. 144], so
$$
T_\Co \definedas S_\Co^{\perp \lkt} = (11, 11, 1)_2 \cong \generators{2} \oplus E_{10}(2)
.
$$
3. The quotient $\bD(T_\Co)/\Orth(T_\Co)$ is a normal quasi-projective variety of dimension $9$. By the Torelli theorem for algebraic K3 surfaces [@PS71], the moduli space $\mcm_\Co$ of @prop:coble-moduli-git is isomorphic to an open subset of $\bD(T_\Co)/\Orth(T_\Co)$ [@DK13, §3, Prop. 3.2, p. 513].

:::

::: {.proposition #prop:coble-moduli-heegner-divisor title="The Coble moduli space as a Heegner divisor"}

The lattice $T_\Co\cong\generators{2}\oplus E_{10}(2)$ is isometric to the orthogonal complement of a $(-2)$-vector in $\ten = U\oplus E_{10}(2)$.
The quotient of the $(-2)$-Heegner divisor $\mch_{-2}$ in $\bD(\ten)$ by $\Orth(\ten)$ is birationally isomorphic to $\mcm_\Co$ [@DK13, §3].

:::

::: {.theorem #thm:coble-moduli-rational title="Rationality of the Coble moduli space"}

Let $\mcm'_{5,\cusp}$ be the moduli space of plane quintics $C$ with a cusp $p$ such that the tangent line $L$ of $C$ at $p$ is tangent to $C$ at a nonsingular point $q$ of $C$.
Then $\mcm_\Co$ is birationally isomorphic to $\mcm'_{5,\cusp}$ [@DK13, §4, Thm. 6.3, p. 518], and $\mcm_\Co$ is a rational variety [@DK13, Thm. 6.4, p. 518].

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

Let $Z$ be an irreducible sextic of type $T = 10A_1$, so that $Z$ is rational by @lem:rational_sextic_ten_nodes, and $X$ is the K3 cover of the Coble surface $S = X/\iota$.
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

This is [@YZZ25 §3.1; §1, §3.2, §3.3, §6.2].
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

This is [@YZZ25 §4.1, §4.2; @Sha80; @Loo02].
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
so the gluing subgroup $H_0 = \Lambda_1/(P\oplus Q)\leq A_P\oplus A_Q$ has order $2^{10} = \abs{A_P}$ and, its projection to $A_P$ being injective [@Nik80, Prop. 1.5.1, printed p. 111], it projects isomorphically onto $A_P$.
If some $g\in\Gamma_W$ acts nontrivially on $A_P$ --- in particular if its signed permutation of the ten classes is not a diagonal change of signs, so that it carries $r_i$ to $\pm r_j$ with $i\neq j$ --- then $\Gamma_{10A_1}\not\subseteq\discriminantkernel{T_\Co}$, and the inclusion $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{10A_1}$ is strict.
:::

::: {.proof}

Let $g\in\Gamma_W$ be such an element, with $\psi\definedas\restrictionof{g}{P}$, $\varphi\definedas\restrictionof{g}{Q}$ and class actions $\bar\psi$, $\bar\varphi$; here $g(P) = P$ because $\Gamma_W$ normalizes $W(L)$, whose generators determine the classes $r_i$ up to sign (@prop:sextic-group-as-normalizer). The isometry $g$ preserves $P\oplus Q$ and $\Lambda_1$, hence preserves $H_0$, which projects isomorphically onto $A_P$: put $\gamma\definedas p_Qp_P^{-1}$, so that $H_0$ is the graph of $\gamma$ over $A_P$. For $x\in A_P$ the class $(x,\gamma x)$ lies in $H_0$, hence so does $(\bar\psi x,\bar\varphi\gamma x)$, and a graph meets the fibre over $\bar\psi x$ in one point: $\bar\varphi\gamma x = \gamma\bar\psi x$. If $\bar\psi\neq\id$ then $\bar\varphi$ is not the identity on $\gamma(A_P)$, hence $\varphi\notin\discriminantkernel{Q} = \discriminantkernel{T_\Co}$. Since $\Gamma_{10A_1} = \Gamma_W|_Q$ (@prop:sextic-group-as-normalizer), it contains this $\varphi$; and $\widetilde\Orth^+(T_\Co)\subseteq\discriminantkernel{T_\Co}$ by its definition (@def:gamma-co-groups). Finally $\bar\psi[r_i/2] = [\pm r_j/2]\neq[r_i/2]$ for $i\neq j$, because $r_j\mp r_i$ has a coordinate equal to $1$ and so is not in $2P$.
:::

::: {.remark #rmk:coble-moduli-functor title="Two quotients in the source, and which one $\Gamma_\Co$ is the monodromy of"}

The source gives both quotients, one printed page apart. For lattice polarized K3 surfaces --- isomorphism classes of pairs $(X,j)$ with $j\colon M\injects\operatorname{Pic}(X)$ a primitive embedding --- the moduli space is
$$\mcm_{\mathrm{K3},M} = \mathcal D(N)/\Orth(N)^*, \qquad \Orth(N)^* = \ker\bigl(\Orth(N)\too\Orth(A_N)\bigr),$$
with $N = M^{\perp L_{\mathrm{K3}}}$ [@DK13, §3, printed p. 512]; for the pair $M = \generators{2}\oplus\generators{-2}^{\oplus 10}$, $N = T_\Co$ of [@DK13, (3.6), printed p. 513] this is $\bD(T_\Co)/\discriminantkernel{T_\Co}$, the quotient by the discriminant kernel. For *unpolarized* Coble surfaces the same source gives $\mcm_\Co$ as an open subset of $\bD(N)/\Orth(N)$ [@DK13, Prop. 3.2, printed p. 513], the quotient by the full orthogonal group.

The two differ by exactly the group whose action on $A_{T_\Co}$ decides @conj:gamma-co-stable and the $\Gamma_\Co$ form of @thm:coble-strong-lifting (@cor:gamma-co-lifting-criterion). @def:gamma-co-groups fixes which group $\Gamma_\Co$ is: the monodromy of the *unpolarized* family, that is, the second display. So the first display is not a statement about $\Gamma_\Co$ --- it is one about the monodromy of the lattice polarized family, a different group, and what it supplies is the containment of $\widetilde\Orth^+(T_\Co)$ in that other group, not in $\Gamma_\Co$ [@DK13, printed p. 512]. For $\Gamma_\Co$ the containment in the discriminant kernel is exactly what @conj:gamma-co-stable asserts, so the $\Gamma_\Co$ form of the lifting is @prop:gamma-co-strong-lifting, which restates it under that conjecture; its sign half is unconditional (@lem:monodromy-is-spinor-positive) and its discriminant half is decided, when it can be decided at all, by the action on the ten exceptional classes (@cor:gamma-co-lifting-criterion).
:::

::: {.question #qst:sextic-group-comparison title="Which quotient of $D(T_\Co)$ is $\fco$?"}

$\fco$ is the quotient of $D(T_\Co)$ by the monodromy group $\Gamma_\Co$ (@def:gamma-co-groups), and $\mcm_\Co$ is an open subset of $F^{\mathrm{un}}_\Co = D(T_\Co)/\Orth(T_\Co)$ (@prop:coble-period-domain).
The moduli space $\mcm_{10A_1}$ is a quotient of an open subset of $D(T_\Co)$ by $\Gamma_{10A_1}$, and
$$
\widetilde\Orth^+(T_\Co) \;\iscontainedin\; \Gamma_{10A_1} \;\iscontainedin\; \Orth(T_\Co)
$$
(@thm:occult-period-map-sextics).
Is either inclusion an equality?
How does $\Gamma_\Co$ compare with $\Gamma_{10A_1}$, with $\widetilde\Orth^+(T_\Co)$ (@conj:gamma-co-stable) and with the arithmetic model $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ of the monodromy group $\Gamma_{\Co,2}$ (@thm:coble-monodromy-versus-enriques)?

The second comparison has a criterion on its discriminant side. The inclusion $\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co)$ asks for triviality of the monodromy action on $A_{T_\Co}$, and for the family whose local system is the $N$-summand of the $H^2$ local system of the K3 double covers that triviality is equivalent to triviality of the monodromy action on $A_M$, where $M = \generators{2}\oplus\generators{-2}^{\oplus 10}$ is the Picard lattice generated by the classes of $E_0,\dots,E_{10}$ (@cor:gamma-co-lifting-criterion). So $\Gamma_\Co$ is not contained in $\widetilde\Orth^+(T_\Co)$ as soon as some loop of the family exchanges two of the ten exceptional classes, and then @conj:gamma-co-stable and the $\Gamma_\Co$ form of the strong lifting of @thm:coble-strong-lifting both fail.
@lem:ten-a1-permutation-forces-strictness gives the same criterion for the first inclusion: by [@YZZ25, Prop. 3.2] every isometry of $T_\Co$ acting trivially on $A_{T_\Co}$ lies in $\widetilde\Gamma_T$, so the discriminant kernel is the part of $\Gamma_{10A_1}$ that is accounted for, and the inclusion $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{10A_1}$ is strict as soon as one of the permutations that $\Orth(P,H,\Delta)\cong\mathfrak S_{10}$ realizes on $A_P$ ([@YZZ25, Lemma 6.7 and its proof]) extends to an isometry of $\Lambda_1$ preserving $H$. Whether one does is not decided by [@YZZ25], whose statements give the contained side only. @rmk:coble-moduli-functor records that the source itself has both quotients, $\bD(T_\Co)/\discriminantkernel{T_\Co}$ for the lattice polarized family [@DK13, printed p. 512] and $\bD(T_\Co)/\Orth(T_\Co)$ for the unpolarized one [@DK13, printed p. 513], so the group asked about here depends on which family the symbol $\Gamma_\Co$ denotes.
:::

::: {.proposition #prop:sextic-root-lattice-counts title="Root lattices of plane sextics"}

The root lattices $R$ that arise from a singular type of plane sextic with simple singularities have been classified [@Ura88; @Yan96].
The maximal rank of such an $R$ is $19$, and the number of such $R$ of rank $19$, $18$, $17$, $16$ is $519$, $987$, $975$, $782$ respectively [@YZZ25, §1; @Yan96, Thm. 2.1].

:::

## The two Coble families and their bases {#sec-coble-families-d2}

Statements D2a and D2b of research#786 ask what the two families are whose variations of Hodge structure define $\Gamma_\Co$ and $\Gamma_{\Co,2}$.
@def:gamma-co-groups defines both symbols as monodromy groups of a family, so what it presupposes is a base, a local system and a period map; this section supplies them.
@def:coble-family-unpolarized states the moduli problem of unpolarized Coble surfaces, with the three bases a source describes; @def:coble-family-degree-two states the degree-$2$ one, and it is the definition that hypothesis (U) of @lem:coble-family-identification asks for, so that (U) holds by @prop:d2-degree-two-supplies-U.
@rmk:d2-what-is-open records the steps that no source read supplies.
Neither definition uses @conj:gamma-co-stable, and no statement here identifies $\Gamma_\Co$ or $\Gamma_{\Co,2}$ with a prescribed lattice group: the comparison of $\Gamma_\Co$ with a lattice group is research#780 and that of $\Gamma_{\Co,2}$ with one is @thm:coble-monodromy-versus-enriques.

::: {.definition #def:coble-family-unpolarized title="D2a: the family of unpolarized Coble surfaces"}

A *Coble surface* is a nonsingular projective rational surface $S$ with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}\neq\emptyset$ [@DZ99, Introduction, printed p. 79; @DK13, §3, printed p. 512].
The examples that [@DK13, §3, printed p. 513] works with, and to which it restricts itself, are the blowups $S=\mathrm{Bl}_{p_1,\dots,p_{10}}\PP^2$ of the projective plane at the ten nodes $p_1,\dots,p_{10}$ of an irreducible plane sextic $Z$.
For such an $S$ let $h$ be the class of a line and $E_1,\dots,E_{10}$ the classes of the exceptional curves.
The proper transform $C\subset S$ of $Z$ has
$$
[C]=-2K_S=6h-\sum_{i=1}^{10}2E_i,\qquad C^2=36-4\cdot10=-4,
$$
and the double cover $\pi\colon X\to S$ branched along $C$ is a K3 surface with a covering involution $\iota$, $S=X/\iota$ [@DK13, §3, printed p. 513].

The **moduli problem** is the category fibred in groupoids over complex schemes whose objects over a base $B$ are flat families $\mcs\to B$ of Coble surfaces together with the double covers $\mcx\to\mcs$ branched along the relative $\abs{-2K}$ curve; morphisms are Cartesian squares.
A Coble surface is rational, so $h^{2,0}=0$ on each fibre and the Hodge structure in degree $2$ is of type $(1,1)$ throughout: the variation of Hodge structure of a family of Coble surfaces is trivial in degree $2$, and the one the monodromy group is taken on is that of the K3 *covers*, which the next two items record.

The **base** is one of the following, and the choice among them is part of the definition.

1. *Surfaces.* The coarse space $\mcm_\Co$ of @prop:coble-moduli-git, a locally closed subvariety of the GIT quotient of $(\PP^2)^{10}$ by $\PGL_3$ [@DK13, §3, printed p. 513]. It is the coarse space of the source, which constructs no stack over it; its period map is an isomorphism onto an open subset of $\bD(T_\Co)/\Orth(T_\Co)$ (@lem:d2a-period-map), and no family over it is constructed there.
2. *Sextics.* The space $\mcm_{10A_1}$ of plane sextics of type $10A_1$ modulo $\SL_3$ (@not:sextic-singular-type). It is the quotient orbifold of $\bD(T_\Co)-\mch_{10A_1}$ by the arithmetic group $\Gamma_{10A_1}$ (@thm:occult-period-map-sextics), hence a Deligne--Mumford stack whose coarse space it is, and its period map is an isomorphism of orbifolds onto that quotient.
3. *Sextics with ordered nodes.* The same locus as in 1., read with the ten nodes labelled $p_1,\dots,p_{10}$, that is before the quotient by the symmetric group on the labels: a finite cover of the coarse space of 1. over the locus where the nodes are distinct. [@DK13, §3, printed p. 513] constructs $\mcm_\Co$ by way of the ordered ten-tuples, and the labelling is what makes the eleven classes of the next item locally constant. The whole GIT quotient of $(\PP^2)^{10}$ by $\PGL_3$ is not a base for Coble surfaces: its points are ten points, not the nodes of a sextic.

The **local system of lattices** is defined on base 3., where the ten nodes are labelled and the family of K3 covers exists; bases 1. and 2. carry the local system of the same construction, attached to their own period maps, with the same fibre.
On the family $\mcx\to B$ of K3 covers the sheaf $\bV\definedas R^2f_*\underline{\bZ}_\mcx$ modulo torsion is a local system of lattices with the cup product (@prop:primitive-cohomology-vhs(1)).
Because the ten nodes are labelled, the class $H$ of the pullback of a line and the classes $r_1,\dots,r_{10}$ of the exceptional curves of the minimal resolution $X\to\bar X$ of the double cover of $\PP^2$ branched along $Z$ are the values of global sections of $\bV$: each is the class of a divisor on $\mcx$ flat over $B$.
Their span is a primitive sublattice isometric to $M\definedas\generators{2}\oplus\generators{-2}^{\oplus 10}\cong S_\Co$ (@prop:coble-is-the-ten-nodal-sextic-type), and
$$
\bT\definedas\underline M^{\perp\bV}
$$
is a local system of lattices whose fibre is $T_\Co=M^{\perp\lkt}\cong\generators{2}\oplus E(2)$ (@prop:coble-period-domain(2), [@DK13, (3.6), printed p. 513]).
This $\bT$ is the local system of lattices of the family; its rank is $11$ and its stalks have signature $(2,9)$.

The **period map** is read in a marking, that is on the universal cover: fix a base point $s\in B$ and an isometry $\bT_s\iso T_\Co$; the isometry carries the class of $H^{2,0}(X_{\tilde b})$ to a point of $\bD(T_\Co)$, and the resulting map
$$
\widetilde\per\colon\widetilde B\too\bD(T_\Co)
$$
is holomorphic (@prop:lifted-period-map(4)) and equivariant for the monodromy representation of $\bT$ (@eq-period-map-equivariance); it induces
$$
\per\colon B\too\bD(T_\Co)/\Gamma_\Co .
$$

$\Gamma_\Co$ is the monodromy group of the family of @def:gamma-co-groups(1), that is: on bases 2. and 3. the group $\rho\qty{\pi_1(B,s)}$ of $\bT$ (@def:transport-and-monodromy), and on base 1. the monodromy group of the local system of lattices obtained by pulling the tautological local system of $\bD(T_\Co)/\Orth(T_\Co)$ back along $\per$.
In each case it is a subgroup of $\Orth(T_\Co)$, and the three are related as @lem:coble-family-base-change says.
:::

::: {.lemma #lem:d2a-period-map title="The period map of base 1 is the map of Dolgachev--Kondo"}

The map of [@DK13, Prop. 3.2, printed p. 513] from $\mcm_\Co$ to $\bD(N)/\Orth(N)$, $N=\generators 2\oplus E(2)$, is the period map of @def:coble-family-unpolarized on base 1: a Coble surface $S$ is carried to the Hodge structure $H^{2,0}(X)\iscontainedin H^2(X,\CC)$ of its K3 double cover, read through the isometry $T_\Co\cong N$ of [@DK13, (3.6), printed p. 513].
It is an isomorphism onto an open subset.
:::

::: {.proof}

[@DK13, §3, printed p. 513] defines the map as the one that "the Torelli-type theorem for algebraic K3 surfaces, due to Pyatetskii-Shapiro and Shafarevich, implies", applied to the K3 covers $X$ of @def:coble-family-unpolarized; the Torelli theorem identifies a K3 surface with the Hodge structure on $H^2$, and the period map of any family of K3 surfaces is the same assignment.
The hypotheses are those of the citation: $X$ is an algebraic K3 surface, $M_X$ is the sublattice spanned by the classes $e_0,\dots,e_{10}$ and is isomorphic to $M=\generators 2\oplus\generators{-2}^{\oplus 10}$ [@DK13, §3, printed p. 513], and its orthogonal complement $N_X$ is isometric to $N$ (@prop:coble-period-domain(2)), so the Hodge structure is a point of $\bD(N)$.
The last sentence is [@DK13, Prop. 3.2, printed p. 513].
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

::: {.lemma #lem:coble-family-labelled-monodromy title="The labelled family has monodromy in $\widetilde\Orth^+ (T_\Co)$"}

On the base of @def:coble-family-unpolarized, item 3., the monodromy group of $\bT$ is contained in $\widetilde\Orth^+(T_\Co)$.
:::

::: {.proof}

The eleven classes of the definition are values at $s$ of global sections of $\bV$, and $M$ is their span, primitive and nondegenerate of signature $(1,10)$ (@prop:coble-is-the-ten-nodal-sextic-type).
So @cor:lattice-polarized-k3-monodromy applies: the restriction of the monodromy to $T=M^{\perp\lkt}$ takes values in $\widetilde\Orth^+(T)$.
That group is $\Orth^+(T_\Co)\intersect\discriminantkernel{T_\Co}$, which is $\widetilde\Orth^+(T_\Co)$ (@def:gamma-co-groups(3)).
:::

::: {.lemma #lem:coble-family-sextic-monodromy title="The sextic base has monodromy $\Gamma_{10A_1}$"}

On the base of @def:coble-family-unpolarized, item 2., the monodromy group of $\bT$ is $\Gamma_{10A_1}$, the image of $\Orth\qty{H^2(X;\bZ),\Delta,H}$ in $\Orth(T_\Co)$ restricted to the subgroup preserving a chosen component $\bD(T_\Co)$, and
$$
\widetilde\Orth^+(T_\Co)\iscontainedin\Gamma_{10A_1}\iscontainedin\Orth(T_\Co),
$$
the first inclusion being [@YZZ25, Prop. 3.2] together with [@YZZ25, §3.1].
:::

::: {.proof}

By @thm:occult-period-map-sextics the period map of the family is an isomorphism of orbifolds of $\mcm_{10A_1}$ with $\Gamma_{10A_1}\backslash(\bD(T_\Co)-\mch_{10A_1})$.
That quotient is a global quotient of a domain by $\Gamma_{10A_1}$, so its orbifold fundamental group is $\Gamma_{10A_1}$, and the local system $\bT$ is the flat bundle $\qty{\bD(T_\Co)-\mch_{10A_1}}\times T_\Co$ modulo $\Gamma_{10A_1}$; its monodromy group is the defining image of $\Gamma_{10A_1}$ in $\Orth(T_\Co)$.
The period map is that of the variation of the family (@prop:lifted-period-map), so this is the monodromy group of the family.
The inclusion $\widetilde\Orth^+(T_\Co)\iscontainedin\Gamma_{10A_1}$ is [@YZZ25, Prop. 3.2], which states that every isometry of $T_\Co$ acting trivially on $A_{T_\Co}$ lies in the group, as recorded in @thm:occult-period-map-sextics.
:::

::: {.remark #rmk:coble-family-three-bases title="The three bases give three groups, and no source compares them"}

@lem:coble-family-labelled-monodromy puts the monodromy of base 3. inside $\widetilde\Orth^+(T_\Co)$ and @lem:coble-family-sextic-monodromy identifies that of base 2. with $\Gamma_{10A_1}$, which contains $\widetilde\Orth^+(T_\Co)$.
Since base 3. is a finite cover of base 1., @lem:coble-family-base-change puts the monodromy of 3. inside that of 1.; but no source read relates either base to base 2., and neither statement gives the monodromy group of base 1.
Which of the three the symbol $\Gamma_\Co$ denotes is therefore not fixed by a convention of the sources: it is what @qst:sextic-group-comparison asks, and @def:gamma-co-groups names the unpolarized family, that is base 1.

The containment of @lem:coble-family-labelled-monodromy is not in tension with the open discriminant half of $\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co)$ (@rmk:gamma-co-status): the lemma's base is the labelled one, on which the eleven classes are flat by construction, whereas the unpolarized family of @def:gamma-co-groups(1) carries no such labelling and a loop of it may carry one configuration of ten curves to another.
:::

::: {.definition #def:coble-family-degree-two title="D2b: the family of degree-$2$ Coble surfaces"}

The objects are the Coble quotients of the degree-$2$ Enriques families of [@AEGS25, §2], with the marking that names the Coble lattice.
Over a base $B$, an object is a tuple $\qty{\mcx\to B,\ \ien,\ \iota',\ \varphi}$ in which

1. $\mcx\to B$ is a flat family of K3 surfaces, smooth over $B$, and $\ien$ is a fixed-point-free involution of it such that $\mcZ\definedas\mcx/\ien$ is a family of Enriques surfaces carrying an ample numerical polarization $[L_Z]$ of degree $2$, equivalently a $2$-divisible polarization $M=L_Z^{\tensor 2}$ of degree $8$ [@AEGS25, §1, printed p. 582];
2. $\iota'$ is an involution of $\mcx$ over $B$ whose quotient $\mcs\definedas\mcx/\iota'$ is a family of rational Coble surfaces with a $\tfrac14(1,1)$-singularity [@AEGS25, §2.3, printed p. 587];
3. the $\iota'$-invariant part $\qty{R^2f_*\underline{\bZ}_\mcx}^{\iota'}$ is a local system of lattices whose stalks are isometric to $S_\Co\definedas\generators{2}\oplus\generators{-2}^{\oplus 10}$; a *marking* is an isometry $\varphi$ onto it from the constant local system $\underline{S_\Co}$, whose images of the standard basis are written $e_0,e_1,\dots,e_{10}$. No global marking need exist: since $\iota'$ acts on $H^2$ of a fibre, the invariant local system may carry nontrivial monodromy, and a marking then exists on a finite pullback of the base. It is a comparison device and is not part of the objects.

The fibre of the family is the Coble surface $S_b=X_b/\iota'_b$; it is singular, and blowing down the proper transform $C$ of the sextic in a smooth Coble surface produces it [@DK13, §1, printed p. 509], $C$ being the $(-4)$-curve of @def:coble-family-unpolarized.
The invariant lattice is the one computed in [@DK13, §3, printed p. 513]: for the double cover $\pi\colon X\to S$ the invariant part of $H^2(X;\bZ)$ is $\pi^*H^2(S;\bZ)$, a primitive sublattice on which $\iota'$ acts trivially, and the classes $e_0,\dots,e_{10}$ of the line and of the ten exceptional curves are its values on a basis of $H^2(S;\bZ)$; they span a lattice isomorphic to $M=\generators 2\oplus\generators{-2}^{\oplus 10}=S_\Co$, with orthogonal complement $T_\Co$ (@prop:coble-period-domain(2)).

The **base** is the discriminant divisor, written $\Delta$ in @lem:coble-family-identification and here $\Delta_2$ to distinguish it from the divisor of [@AEGS25, Def. 2.7].
Let $\mcm_2$ be the moduli stack of Enriques surfaces with an ample numerical polarization of degree $2$; it is Deligne--Mumford and its coarse space is $\fentwo$ away from the discriminant [@AEGS25, §2.4, printed p. 588; §2.3, printed p. 587], and let $\overline{\mcm}_2$ be its KSBA compactification, with its universal family [@AEGS25, §5.3, printed p. 612].
The base is
$$
\Delta\definedas\theset{x\in\mcm_2 \st \text{the K3 cover } X_x \text{ is nodal}}\iscontainedin\overline{\mcm}_2,
$$
a divisor whose image in the coarse space is
$$
\Delta_2\definedas\mch_{-2}/\gent=D_{R_-}/\gent\iscontainedin\fentwo=\bD(\ten)/\gent,\qquad
\gent=\Orth(\ten)\intersect\Orth(\tdp),
$$
with $R_-=\theset{x\in\ten \st x^2=-2}$ [@Ste91, (2.10), printed p. 8] and $\gent$ the group of [@AEGS25, Def. 2.6, printed p. 587].
Equivalently $\Delta_2$ is the image of the hyperplanes $\alpha^{\perp}$ for $\alpha\in\ten$ a $(-2)$-vector, that is the preimage of the divisor $\alpha^\perp$ of [@AEGS25, Def. 2.7, printed p. 587] under the finite map $\fentwo\to\bD(\ten)/\Orth(\ten)$ of [@AEGS25, Lem. 2.8, printed p. 587].
It is an irreducible divisor (@lem:degree-two-base-is-delta-two(3)), and it is the whole of the base and not a proper sublocus of it (@lem:degree-two-base-is-delta-two(2)).

The **family** over $\Delta$ is the restriction of the universal family of K3 surfaces with the Enriques involution over $\mcm_2$ and over its compactification: the universal family over the compactified moduli stack restricts to the closure $B$ of the image of $\fentwo$, and the normalization $B^\nu$ of $B$ is a compactification of $\fentwo$ admitting a universal family of pairs [@AEGS25, §5.3, printed p. 612].
The Coble family is its quotient by $\iota'$.

The **local system of lattices** is the $\delta^{\perp}$-part of the restriction to $\Delta$ of the local system with fibre $\ten$: at $x\in\Delta$ the class $\alpha_x$ of the node is a $(-2)$-vector of $\ten$, and
$$
\bT\definedas\underline{\alpha}^{\perp}\iscontainedin\underline{\ten}|_{\Delta}
$$
is a local system of lattices of rank $11$ and signature $(2,9)$ with fibre $\eta(T_\Co)=\delta^{\perp\ten}\cong T_\Co$ (@lem:primitive_embedding_eta).
Geometrically it is the orthogonal complement in $R^2f_*\underline\bZ_\mcx$ of the invariant lattice $S_\Co$ of $\iota'$, which the marking of the objects identifies with $\underline{S_\Co}$.

The **period map** is the restriction of the period map of $\fentwo$:
$$
\per_2\colon\Delta\iso\bD(\alpha^\perp)/\Stab_{\gent}(\alpha)\too\bD(T_\Co)/\Gamma_{\Co,2},
$$
the first isomorphism being the description of the divisor as the image of one hyperplane.

$\Gamma_{\Co,2}$ is the monodromy group of $\bT$ on $\Delta$, that is $\rho\qty{\pi_1(\Delta,s)}\iscontainedin\Orth(T_\Co)$ (@def:gamma-co-groups(5)).
:::

::: {.lemma #lem:degree-two-base-is-delta-two title="Every point of $\Delta_2$ is a Coble surface's period, and conversely"}

1. A point of $\fentwo$ lies in $\Delta_2$ exactly when the corresponding K3 cover carries a $(-2)$-class, that is exactly when its period is orthogonal to a vector $\alpha$ of $\ten$ with $\alpha^2=-2$.
2. Every such point is the period of a quotient of a nodal K3 surface by an involution fixing a node, that is of a rational Coble surface with a $\tfrac14(1,1)$-singularity, and conversely every such quotient has such a period [@AEGS25, §2.3, printed p. 587].
3. $\Delta_2$ is irreducible.
:::

::: {.proof}

For (1), $\Delta_2=\mch_{-2}/\gent$ is by definition the union of the images of the hyperplanes $\alpha^\perp$ over the $(-2)$-vectors $\alpha\in\ten$ (@def:heegner-divisor), that is the set of periods orthogonal to one of them; a period orthogonal to $\alpha$ lies in the image of $\bD(\alpha^\perp)$, and the corresponding K3 surface has $\alpha$ in its Picard group.
For (2), the first sentence is [@AEGS25, §2.3, printed p. 587], which states that $\alpha^{\perp}\iscontainedin\bD(\ten)/\Orth(\ten)$ parameterizes the quotients of nodal K3 surfaces by an involution fixing a node, these being the rational Coble surfaces with a $\tfrac14(1,1)$-singularity; the passage from $\bD(\ten)/\Orth(\ten)$ to $\fentwo$ is the finite map of [@AEGS25, Lem. 2.8, printed p. 587], so each point of $\Delta_2$ lies over a point of that divisor and inherits the surface.
The converse is the same statement read backwards: a quotient of a nodal K3 surface by an involution fixing the node has the node's class in its Picard group, so its period is orthogonal to a $(-2)$-class.
For (3), $\Orth(\ten)$ is transitive on the $(-2)$-vectors [@AEGS25, Def. 2.7, printed p. 587] and $\gent$ is transitive on them as well [@Ste91, (2.10) and the paragraph following it, printed p. 8], which is exactly the irreducibility of the image of the union of their hyperplanes in $\fentwo$.
:::

::: {.proposition #prop:d2-degree-two-supplies-U title="Hypothesis (U) of the family identification holds"}

For the moduli problem of @def:coble-family-degree-two, hypothesis (U) of @lem:coble-family-identification is satisfied: the degree-$2$ Coble family over $\Delta$ and its marking are defined, its base is the restriction to $\Delta$ of the universal family over the moduli stack of degree-$2$ numerically polarized Enriques surfaces whose coarse space is $\fentwo$, $\Gamma_{\Co,2}$ is its monodromy group on the local system with fibre $T_\Co$, and on every fibre the covering involution $\iota'$ has invariant lattice $S_\Co$, spanned by the classes $e_0,\dots,e_{10}$.
Consequently statement (F) of that lemma holds, and so does $\Gamma_{\Co,2}\iscontainedin R_{\gent}\intersect\Orth^+(T_\Co)$ of @thm:coble-monodromy-versus-enriques(4).
:::

::: {.proof}

The objects, the base, the family, the marking and the local system are those of @def:coble-family-degree-two, clause by clause: clause 1 is the Enriques half, clause 2 the Coble quotient, clause 3 the invariant lattice with its marking, and the paragraph after them the computation of that lattice and the local system.
The invariant lattice is computed in [@DK13, §3, printed p. 513]: the classes $e_0,\dots,e_{10}$ of the line and of the ten exceptional curves are the values on a basis of $H^2(S;\bZ)$ of the isomorphism $\pi^*$, so they span the invariant part $\qty{H^2(X;\bZ)}^{\iota'}=\pi^*H^2(S;\bZ)$ of the covering involution of the double cover $\pi\colon X\to S$, which is isomorphic to $M=\generators 2\oplus\generators{-2}^{\oplus 10}=S_\Co$.
The two statements (F) and $\Gamma_{\Co,2}\iscontainedin R_{\gent}\intersect\Orth^+(T_\Co)$ are then the conclusions of @lem:coble-family-identification and of @thm:coble-monodromy-versus-enriques(4), whose only other hypothesis is (U).
:::

::: {.remark #rmk:degree-two-two-meanings title="The meanings of degree $2$"}

The phrase occurs in three senses in the sources and in this book, and they are conditions on different objects.

1. *The Enriques polarization.* That of @def:coble-family-degree-two: the degree is $L_Z^2=2$ of an ample numerical polarization of the Enriques quotient $Z=X/\ien$, equivalently $\deg M=8$ for $M=L_Z^{\tensor2}$ [@AEGS25, §1, printed p. 582]. It restricts the base: the Coble surfaces are the fibre of $\fentwo$ over the divisor $\Delta_2$, a codimension-one locus.
2. *The plane model.* The degree is $H^2=2$ of the K3 double cover $X\to\PP^2$ itself, that is the statement that $X$ is a double plane whose branch sextic is $Z$ and whose Coble quotient is $S=\mathrm{Bl}_{10}\PP^2$ (@prop:coble-period-domain(1), @prop:coble-is-the-ten-nodal-sextic-type). It restricts nothing: every classical Coble surface has it, so on this reading the base is the whole of any of the three bases of @def:coble-family-unpolarized and not a divisor.
3. *A class on the Coble surface.* @def:coble-polarization-classes states a degree-$2$ numerical polarization as a class $h_\Co\in K_S^{\perp\Pic(S)}$ with $h_\Co^2=2$, of Enriques type. That is the notion of [@DK13, §8, printed p. 522]: for an unnodal Coble surface the orthogonal complement of $K_S$ in $\Pic(S)$ is isomorphic to the Enriques lattice $\EE$, and a polarization $h=[F_1+F_2]$ of degree $2$ corresponds to an embedding $U\injects\EE$. The source writes $\mcm_\Co(2)$ for the resulting moduli space and computes the degree of the rational map $\Phi'\colon\mcm_\Co(2)\dashrightarrow\mcm_\Co$ as $2^7\cdot17\cdot31$ [@DK13, §8, printed p. 523]. No source read identifies $\mcm_\Co(2)$ with the divisor $\Delta_2$ of @def:coble-family-degree-two, and the two are different objects: $\mcm_\Co(2)$ is a cover of the unpolarized Coble moduli space, whereas $\Delta_2$ is a divisor in the Enriques period quotient. The definition above uses 1., the reading whose base is $\Delta_2$ and the one research#786, D2b, states.

Readings 1. and 2. are not interchangeable: reading 1. is a condition on the Enriques quotient, which is one quotient of the K3 surface and is not the Coble surface, whereas reading 2. is automatic, and a definition that used it would define the unpolarized moduli problem again under another name.
:::

::: {.remark #rmk:d2-what-is-open title="What no source read supplies"}

1. **The local system of base 1.** @lem:d2a-period-map gives the period map of $\mcm_\Co$ as an isomorphism onto an open subset of $\bD(T_\Co)/\Orth(T_\Co)$, and [@DK13, printed p. 513] constructs no family over $\mcm_\Co$ and no local system; a coarse space does not determine monodromy. The local system of @def:coble-family-unpolarized on base 1 is therefore the pullback of the tautological one along the period map: that is a definition, not a theorem, and whether it is the local system of an actual family is open.
2. **Which base is $\Gamma_\Co$.** Base 3. gives a subgroup of $\widetilde\Orth^+(T_\Co)$ (@lem:coble-family-labelled-monodromy) and base 2. gives $\Gamma_{10A_1}\supseteq\widetilde\Orth^+(T_\Co)$ (@lem:coble-family-sextic-monodromy); nothing read compares the two bases, and nothing read compares either with base 1. Hence the equality of any two of the three groups is open, and @qst:sextic-group-comparison is where that question sits. In particular the sentence of @def:gamma-co-groups(1) that the family of unpolarized Enriques surfaces *induces* the Coble family and its local system is not proved by anything read here: it is the comparison of base 1 with the induced Enriques family.
3. **The marking of the degree-$2$ family.** @prop:d2-degree-two-supplies-U supplies (U), so (F) and the inclusion of @thm:coble-monodromy-versus-enriques(4) hold. What stays open is the reverse inclusion, @qst:coble-monodromy-equality, which no printed statement supplies; nothing in this section asserts it.
4. **Ample against nef.** [@AEGS25, §1, printed p. 582] asks for an *ample* numerical polarization of degree $2$, whereas the degree-$2$ polarized Enriques moduli space is defined with a *nef* class $h$ of square $2$ [@DK13, §7, printed p. 518], and [@Ste91, §2] calls the same datum an almost polarization. [@DK13, §7, printed p. 518] splits $h=F_1+F_2$ with $F_i^2=0$, $F_1\cdot F_2=1$ from the degenerate $h=2F_1+R$ with $R$ a $(-2)$-curve and $F_1\cdot R=0$, and the second is not ample. [@AEGS25, §1, printed p. 582] covers both, its $W$ having $4A_1$ or $A_3+2A_1$ singularities, so the adjective does not by itself separate the two problems; whether the ample problem and the nef problem have the same coarse space is not decided by the sentences read. The base of @def:coble-family-degree-two is the arithmetic divisor $\Delta_2$, which needs neither adjective.
5. **The sources named for the plane model.** research#786 cites [AET23, Thm. 1.1] and [AE23, Thm. 9.1, Prop. 9.4] for reading 2 of @rmk:degree-two-two-meanings. A full-text search of the two files in the corpus finds no occurrence of "Coble" in either, and [@AET23]'s main theorem is numbered 1.2, its subject being a semifan and the normalization of $\overline{F_2}$; [@AE23, Thm. 9.1] and Prop. 9.4 concern K3 surfaces with a non-symplectic involution, not Coble surfaces. Reading 2 therefore rests on @thm:occult-period-map-sextics alone, and those two citations do not support it as the plan states them.
6. **Which involution fixes the node.** [@AEGS25, §2.3, printed p. 587] names the involution only as one fixing a node, and its Diagram (2.1) on printed p. 584 carries three commuting involutions $\idp,\ien,\inik$ of the Enriques K3. The definition above takes $\iota'$ as part of the objects, subject to clause 3, and does not decide which of them it is.
7. **Cantat--Dolgachev, and the primary definition.** Cantat--Dolgachev is not among the sources read here, and nothing in this section needs it. The definition of a Coble surface used above is the primary one: [@DZ99, Introduction, printed p. 79] states it, and [@DK13, §3, printed p. 512] repeats it, its own reference [8] being that paper. Cantat--Dolgachev is reference [10] of [@DK13], and is used there in §8 for the del Pezzo model of a polarized Coble surface.
8. **The compactified families.** Both definitions are stated over the open bases. Their extensions over the boundary, and which boundary strata are Coble, are not part of D2 and are not asserted.
:::
