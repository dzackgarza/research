# Constructions of the moduli space {#sec-moduli-construction}

$$
\begin{aligned}
\fen &= \bD(\ten)/\Orth^+(\ten)^* &
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
\Gamma^K_{\En} &= \Orth(\ten), \qquad \Orth^+(\ten)^* = \Orth^+(\ten)\intersect\discriminantkernel{\ten} \\
\Gamma_\Co &= \text{the image of } \Stab_{\Orth(\ten)}(\delta) \text{ in } \Orth(\delta^{\perp}), \quad \delta^2 = -2,\ \delta^{\perp T_\En} = T_\Co \\
\Gamma_{\Co, 2} &= \text{the same image for } \gent \text{ in place of } \Orth(\ten) \\
F_{\Nod} &= \bD(T_\Nod)/\Orth^+(T_\Nod)^*
\end{aligned}
$$

Here $\tdp$ is the lattice of [@AEGS25], and $\eta\colon T_\Co\injects\ten$ is the embedding of @lem:primitive_embedding_eta.
The quotient $F^K_{\En} = \bD(\ten)/\Gamma^K_{\En}$, with $\Gamma^K_{\En} = \Orth(\ten)$ the group $\Gamma_{\mathrm{Enr}}$ of [@AEGS25], has two $0$-cusps $(10,10,0)_1$, $(10,8,0)_1$ and two $1$-cusps $(8,8,0)_0$, $(8,6,0)_0$ [@AEGS25, §2]. The quotient $\fentwo = \bD(\ten)/\gent$, with $\gent = \Gamma^K_{\En}\intersect\Gamma_{\dP}$, has five $0$-cusps [@AEGS25, §3]. Throughout, $\Gamma_\En$ denotes $\Orth^+(\ten)^*$ (@sec-heegner-line, @thm:normalization, @def:gamma-co-en).
The quotients $\fco = \bD(T_\Co)/\Gamma_\Co$ and $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ are the quotients by the images of the stabilizers of $\delta$ (@def:gamma-co-groups, @prop:gamma-co-images).
The stable subgroup $\widetilde\Orth^+(T_\Co)$ is the kernel of the action on $A_{T_\Co}$ of each of the groups $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ of @sec-gamma-co-comparison, and both inclusions are strict, of index $\abs{W(E_8)} = 696\,729\,600$ (@prop:gamma-co-heegner-strict, @prop:theta-co-index).

::: {.question}
What is an explicit description of $\Gamma_{\Co, 2}$?
:::

```{.tikz}
%%| filename: moduli-tower
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}[column sep=large, row sep=large]
F_{\mathrm{Co},2}
  \arrow[r]
  \arrow[d, "?"'] &
F_{\mathrm{En},2}
  \arrow[r]
  \arrow[d] &
F_{(2,2,0)}
  \arrow[r, hook] &
F_4 \\
F_{\mathrm{Co}}
  \arrow[r] &
F_{\mathrm{En}}
\end{tikzcd}
```

The tower relates the degree-$2$ numerically polarized Coble and Enriques moduli $F_{\Co,2}$, $\fentwo$, their unpolarized quotients $\fco$, $\fen$, and the degree-$(2,2,0)$ K3 moduli space $\fttz\injects F_4$.
The map $F_{\Co,2}\to \fco$ marked $?$ is undetermined, since $\Gamma_{\Co,2}$ has no explicit description.

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
   The quotient $\bD(T_\Nod)/\Orth(T_\Nod)$ is a quasi-projective variety of dimension $9$, and $\mcm^{\mathrm{nod}}_\En$ is birationally isomorphic to it [@DK13, §3, Prop. 3.1].
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
2. The orthogonal complement of this sublattice in $H^2(X,\ZZ)\cong\lkt$ is a $2$-elementary lattice of signature $(2, 9)$ with discriminant form $-q_{S_\Co}$ [@DK13, §3; @Nik80, Cor. 1.6.2]. Its isomorphism class is determined by $-q_{S_\Co}$ [@DK13, §3; @Nik80, Thm. 3.6.2], so
$$
T_\Co \definedas S_\Co^{\perp \lkt} = (11, 11, 1)_2 \cong \generators{2} \oplus E_{10}(2)
.
$$
3. The quotient $\bD(T_\Co)/\Orth(T_\Co)$ is a normal quasi-projective variety of dimension $9$. By the Torelli theorem for algebraic K3 surfaces [@PS71], the moduli space $\mcm_\Co$ of @prop:coble-moduli-git is isomorphic to an open subset of $\bD(T_\Co)/\Orth(T_\Co)$ [@DK13, §3, Prop. 3.2].

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

::: {.question #qst:sextic-group-comparison title="Which quotient of $D(T_\Co)$ is $\fco$?"}

$\fco$ is the quotient of $D(T_\Co)$ by $\Gamma_\Co = \Orth(T_\Co)$ (@def:gamma-co-groups, @prop:gamma-co-images), and $\mcm_\Co$ is an open subset of it (@prop:coble-period-domain).
The moduli space $\mcm_{10A_1}$ is a quotient of an open subset of $D(T_\Co)$ by $\Gamma_{10A_1}$, which contains $\widetilde\Orth^+(T_\Co)$ (@thm:occult-period-map-sextics).
In the chain
$$
\widetilde\Orth^+(T_\Co) \;\iscontainedin\; \Gamma_\Co \;\iscontainedin\; \Gamma_{10A_1} \;\iscontainedin\; \Orth(T_\Co)
,
$$
is either inclusion an equality?
How do these groups compare with the polarized group $\Gamma_{\Co,2}$?
:::

::: {.proposition #prop:sextic-root-lattice-counts title="Root lattices of plane sextics"}

The root lattices $R$ that arise from a singular type of plane sextic with simple singularities have been classified [@Ura88; @Yan96].
The maximal rank of such an $R$ is $19$, and the number of such $R$ of rank $19$, $18$, $17$, $16$ is $519$, $987$, $975$, $782$ respectively [@YZZ25, §1; @Yan96, Thm. 2.1].

:::
