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
\Gamma_\Co &= \text{the monodromy group of the VHS on the universal family over } \mcM_\Co \\
\Gamma_{\Co, 2} &= \text{the monodromy group of the VHS of the degree-$2$ Coble family} \\
R_{\gent} &= \text{the image of } \Stab_{\gent}(\delta) \text{ in } \Orth(\delta^{\perp\ten}) = \Orth(T_\Co), \quad \delta^2 = -2 \\
F_{\Nod} &= \bD(T_\Nod)/\Orth^+(T_\Nod)^*
\end{aligned}
$$

Here $\tdp$ is the $(-1)$-eigenlattice of $I_\dP$ [@AEGS25, Def. 2.3], and $\eta\colon T_\Co\injects\ten$ is the embedding of @lem:primitive_embedding_eta.
The quotient $F^K_{\En} = \bD(\ten)/\Gamma^K_{\En}$, with $\Gamma^K_{\En} = \Orth(\ten)$ the group $\Gamma_{\mathrm{Enr}}$ of [@AEGS25, Def. 2.6], has two $0$-cusps $(10,10,0)_1$, $(10,8,0)_1$ and two $1$-cusps $(8,8,0)_0$, $(8,6,0)_0$ [@AEGS25, §3.2, Fig. 3]. The quotient $\fentwo = \bD(\ten)/\gent$, with $\gent = \Gamma^K_{\En}\intersect\Gamma_{\dP}$, has five $0$-cusps [@AEGS25, §3]. Throughout, $\Gamma_\En$ denotes the stable group $\widetilde\Orth^+(\ten)$, also written $\Orth^+(\ten)^*$ (@def:gamma-co-groups, @sec-heegner-line, @thm:normalization, @def:gamma-co-en).
The group $\Gamma_\Co$ is the monodromy group of the VHS on the universal family over the moduli stack $\mcM_\Co$ (@def:coble-moduli-functor, @def:gamma-co-groups(1)), and $\fco = \bD(T_\Co)/\Gamma_\Co$; the labelled base of @def:coble-family-unpolarized is a presentation of that stack, and the group of the presentation is $\Gamma_\Co(B)$.

The objects, bases, local systems of lattices and period maps of the two families on which $\Gamma_\Co$ and $\Gamma_{\Co,2}$ are taken are those of @sec-coble-families-d2: the unpolarized family with its three bases (@def:coble-family-unpolarized), whose period map on the first of them is the map of [@DK13, Prop. 3.2] (@lem:d2a-period-map), and the degree-$2$ family over the discriminant divisor (@def:coble-family-degree-two), whose base is the whole of that divisor (@lem:d2-degree-two-base).
The equality $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$ is @conj:gamma-co-stable. On the labelled base it is proved in one direction: $\Gamma_\Co(B)=\rho(\pi_1(B,s))\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)), the reverse inclusion being @qst:gamma-co-sign-is-realised. The identification $\Gamma_\Co=\Gamma_\Co(B)$, of the group of the stack with that of the presentation, is research#797, item 6 (@def:gamma-co-groups(1), @thm:gamma-co-is-stable(2)); no statement below depends on it except @thm:gamma-co-is-the-stack-monodromy, where it is hypothesis (A4), and the paragraph after the diagram below, which states what the degree of the vertical map would be under it. It is not an equality on the other bases of D2a either: on the unlabelled base $\Gamma_\Co(\bar B)$ contains $\Gamma_\Co(B)$ with index $10!$ and is not contained in $\widetilde\Orth^+(T_\Co)$ (@cor:gamma-co-inclusions(2), @lem:relabelling-discriminant-action(3)), while it is contained in $\Gamma_{10A_1}$, which strictly contains $\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-sextic-group(4)); and the coarse space carries no family, its tautological local system having group $\Orth^+(T_\Co)$ (@thm:gamma-co-is-full, @rmk:gamma-co-d2a).
The group $\Gamma_{\Co,2}$ of $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ is the monodromy group of the VHS of the degree-$2$ Coble family (@def:gamma-co-groups). The group that the Enriques datum defines is $R_{\gent} = \bar\rho^{-1}(P)$, the image of the stabilizer of $\delta$ in $\gent$ (@prop:gamma-co-images(3)); it is not the monodromy group, and $\Gamma_{\Co,2} = R_{\gent}$ is false (@thm:coble-monodromy-versus-enriques(3)). The monodromy group lies in $R_{\gent}\intersect\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(4), from @lem:coble-monodromy-in-stabilizer conditional on (U) of @lem:coble-family-identification; (U) and (F) are D2 of research#786, and the definitions they ask for are @sec-coble-families-d2, the family, the base and the local system being those of @def:coble-family-degree-two and @lem:d2-local-system).
The stable subgroup $\widetilde\Orth^+(T_\Co)$ is the kernel of the action on $A_{T_\Co}$ of each of the groups $\Gamma^{\mathrm{Hdg}}_\Co$ and $\Gamma^\theta_\Co$ of @sec-gamma-co-comparison, and both inclusions are strict, of index $\abs{W(E_8)} = 696\,729\,600$ (@prop:gamma-co-heegner-strict, @prop:theta-co-index).

::: {#rmk:coble-arithmetic-group-description .remark title="The group $\Gamma_{\Co,2}$, explicitly"}
@def:gamma-co-groups defines $\Gamma_{\Co,2}$ as the monodromy group, and @thm:coble-monodromy-versus-enriques identifies the arithmetic group that contains it (@lem:coble-monodromy-in-stabilizer, conditional on (U) of @lem:coble-family-identification, which is D2 of research#786): $\Gamma_{\Co,2}\subseteq\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co) = \rho_{T_\Co}^{-1}(P)\intersect\Orth^+(T_\Co) = R_{\gent}\intersect\Orth^+(T_\Co)$, the preimage in $\Orth(T_\Co)$ of the stabilizer $P$ of the decomposition $[h/2]^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ of $A_{T_\Co}$ (@prop:gamma-co-images(3)), intersected with $\Orth^+(T_\Co)$, of index $[\Orth(T_\Co):\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)] = 2\cdot 67\,456 = 134\,912$. The intersection with $\Orth^+(T_\Co)$ cannot be dropped from that chain: the group $R_{\gent} = \rho_{T_\Co}^{-1}(P)$ of @thm:gamma-co-2-comparison(1) is not contained in $\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(2)), the two differ by the coset $s_\zeta\,(R_{\gent}\intersect\Orth^+(T_\Co))$ of a reflection in a primitive vector $\zeta$ of square $2$, so $R_{\gent} = \rho_{T_\Co}^{-1}(P)$ is the larger group and $\Gamma_{\Co,2} = R_{\gent}$ does not hold; it is not the whole arithmetic group: @qst:coble-monodromy-equality is false (@prop:coble-monodromy-equality-false).
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
The vertical map is $F_{\Co}\to F_{\Co,2}$; it exists, and is finite of degree $[\Gamma_{\Co,2}:\Gamma_\Co]$, exactly when $\Gamma_\Co\subseteq\Gamma_{\Co,2}$, and that containment is not proved. Each of its two inputs is open: $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ is @conj:gamma-co-stable (research#780), of which the labelled base supplies only the inclusion $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)), and $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$ is open as well (@prop:d2b-index-exact); unconditional is only the containment in the supergroup, $\widetilde\Orth^+(T_\Co)\subseteq R_{\gent}\intersect\Orth^+(T_\Co)$ (@cor:gamma-co-inclusions(1), @prop:gamma-co-images(3)). So no inclusion, no degree and no divisibility is asserted here for that vertical map. Under $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ together with $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$ the degree is $[\Gamma_{\Co,2}:\widetilde\Orth^+(T_\Co)]$, and under those hypotheses it divides $10!=\qty[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]$, because $\Gamma_{\Co,2}\subseteq\Gamma_{10A_1}$ there (@prop:d2b-index-exact(3)--(4)); a degree read off the labelled base rather than off $\Gamma_\Co$ needs in addition $\Gamma_\Co=\Gamma_\Co(B)$, which is research#797, item 6. No value of the degree is known: it is not $\abs{W(E_8)}=696\,729\,600$, which would put $\Gamma_{\Co,2}$ at $R_{\gent}\intersect\Orth^+(T_\Co)$ (@qst:coble-monodromy-equality, false by @prop:coble-monodromy-equality-false).

## The GIT construction

::: {.proposition #prop:coble-moduli-git title="The GIT construction of the Coble moduli space"}

1. The moduli space $\mcm_\Co$ of blowups of $\PP^2$ at the ten nodes of an irreducible plane sextic is a locally closed (@def:locally-closed-subset) subvariety (@def:closed-subvariety) of the GIT quotient of the variety $(\PP^2)^{10}$ of $10$-tuples of points in $\PP^2$ by $\PGL_3$ [@DK13, §3].
2. A general point of $(\PP^2)^{10}$ has trivial stabilizer (@def:group-orbit) in $\PGL_3$, so its $\PGL_3$-orbit has dimension $\dim\PGL_3 = 3^2-1 = 8$ and codimension
$$
\dim (\PP^2)^{10} - \dim \PGL_3 = 2\cdot 10 - 8 = 12
.
$$
3. The set of ten nodes of an irreducible plane sextic is subject to three conditions and contains nine absolute constants [@Cob19, §2, (10)].

:::

::: {.proof}

For (2), a general $10$-tuple contains four points $q_1, \ldots, q_4$, no three of them on a line.
Choose coordinates with $q_1 = [1:0:0]$, $q_2 = [0:1:0]$, $q_3 = [0:0:1]$ and $q_4 = [1:1:1]$.
A matrix $g\in\GL_3$ that fixes the lines spanned by the first three standard basis (@def:based-module) vectors is diagonal.
If $g$ also fixes the line spanned by $(1,1,1)$, its diagonal entries are equal, so $g$ is a scalar and its class in $\PGL_3$ is the identity.
So the stabilizer is trivial, and the orbit (@def:group-orbit) map $\PGL_3\to(\PP^2)^{10}$ has image of dimension $\dim\PGL_3$.

:::

## The Horikawa model

::: {.proposition #prop:horikawa-model title="The Horikawa model"}

Let $Y = \PP^1\times\PP^1$ with the involution $\tau(x,y) = (-x,-y)$, and let $B\in\abs{-2K_Y}$ be a $\tau$-invariant divisor with at worst ADE singularities that does not pass through the four points with $x, y\in\theset{0,\infty}$ fixed by $\tau$.

1. The double cover $\pi\colon X\to Y$ branched in $B$ is a K3 surface with a del Pezzo involution $\idp$ such that $Y = X/\idp$. The involution $\tau$ lifts to a basepoint-free involution $\ien$ of $X$ that commutes (@def:commutative-diagram) with $\idp$, and $Z = X/\ien$ is an Enriques surface (@def:enriques-surface) [@AEGS25, §2.1].
2. Certain mildly singular $\tau$-invariant equations $f(x,y)$ of bidegree $(4,4)$ that vanish at a torus-fixed point correspond to Coble surfaces (@def:coble-surface), which are $\ZZ/2$ quotients of nodal K3 surfaces (@def:nodal-k3-surface) [@AEGS25, §2.1; @Hor77].
3. There is a unique $(-2)$-vector $\alpha\in\ten$ modulo $\Orth(\ten)$. The divisor $\Delta = \alpha^\perp\iscontainedin\bD(\ten)/\Orth(\ten)$ parametrizes quotients of nodal K3 surfaces by an involution that fixes a node. These are rational Coble surfaces with a $\tfrac14(1,1)$ singularity [@AEGS25, §2.3].

:::

## Period domains

By passing to the K3 cover, one can embed $\fco$ into an arithmetic quotient of a 9-dimensional Hermitian symmetric domain of type $\rm{IV}$.
Let $\lkt = U^3 \oplus E_8^2$ be the canonical K3 lattice.

::: {.definition #def:type-iv-period-domain title="Type IV period domain and its arithmetic quotients" defines="$\Omega_T$; $\bD(T)$; $\bD(T)/\Gamma$; $\Orth^+(T)^*$"}

Let $T$ be a lattice of signature (@def:signature) $(2,n)$ with $n\geq1$, and let $\Omega_T$ be the set of @def:period-component-character.
It has two connected components.
Fix one of them and call it $\bD(T)$.
By @prop:period-spinor-character, the group (@def:group) $\Orth^+(T)$ of @def:lattice-spinor-kernels is the stabilizer (@def:group-orbit) of $\bD(T)$ in $\Orth(T)$.
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
In particular $\Orth^+(T)$ has index (@def:index) two in $\Orth(T)$.
:::

::: {.proof}

Let $g\in\Gamma$ exchange the two components.
Every $\Gamma$-orbit in $\Omega_T$ meets $\bD(T)$: a point of the other component is mapped into $\bD(T)$ by $g$.
Let $x,y\in\bD(T)$ and $\gamma\in\Gamma$ with $\gamma x=y$.
The isometry $\gamma$ is a homeomorphism of $\Omega_T$, so it maps the component $\bD(T)$ of $x$ onto the component of $y$, which is $\bD(T)$.
Hence $\gamma\in\Gamma\intersect\Orth^+(T)$, and the map of orbit (@def:group-orbit) sets is injective (@def:injective-map).
The last statement is the case $\Gamma=\Orth(T)$: the component character $\Orth(T)\to\theset{\pm1}$ of @def:period-component-character is surjective, and its kernel (@def:kernel-cokernel) is $\Orth^+(T)$.
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

Let $T$ be a lattice of rank $r$ and signature (@def:signature) $(2, r-2)$.
Then the type IV domain $\bD(T)$ has complex dimension $r - 2$.
:::

::: {.proof}

The complexification $T_\CC$ has dimension $r$, so $\PP(T_\CC)$ has dimension $r-1$.
The equation $v^2 = 0$ is a single nondegenerate quadratic equation and cuts out a smooth quadric hypersurface of dimension $r-2$ inside $\PP(T_\CC)$.
The condition $v\bar v > 0$ is open, so it selects an open subset of that quadric, and $\bD(T)$ is one of its connected components.
:::

::: {.corollary #cor:m-polarized-k3-dimension title="Dimension of $M$-polarized K3 moduli"}

Let $M\injects\lkt$ be a primitive (@def:primitive-embedding) embedding of a lattice of signature $(1, \rank(M) - 1)$ with orthogonal complement $T = M^{\perp\lkt}$.
Then
$$
\dim_\CC \bD(T) = \rank(T) - 2 = 20 - \rank(M)
.
$$
For the Coble lattices $\rank(S_\Co) = 11$, so $\dim_\CC \bD(T_\Co) = 9$.
:::

::: {.proof}

The K3 lattice has rank $22$ and signature $(3,19)$. The embedding is primitive, which gives a splitting over $\mathbb{Q}$ and not over $\mathbb{Z}$: $M$ and $T$ span $\lkt\otimes\QQ$ orthogonally, so their ranks and signatures add, while $M\oplus T$ has index (@def:index) $|\det M| = |\det T|$ in $\lkt$ and the integral statement is the gluing $A_M\cong A_T$ rather than a direct sum. Orthogonal decomposition over $\mathbb{Z}$ needs the embedded form to be perfect (@def:polarization) (@thm:orthogonal-decomposition), which $M = S_\Co$ is not: its determinant is $2^{11}$.
Ranks add, so $\rank(T)=22-\rank(M)$.
Signatures add too, by @def:signature applied to the orthogonal sum (@def:orthogonal-sum) of the two real forms, so if $M$ has signature $(1,\rank(M)-1)$ then $T$ has signature $(3-1,\,19-(\rank(M)-1))=(2,\,20-\rank(M))$.
The first index is $2$, so $T$ is of type IV in the sense of @prop:type-iv-dimension, whose dimension for a type IV lattice of signature $(2,m)$ is $m$; with $m=20-\rank(M)$ that is the displayed dimension.
For $M=S_\Co$ of rank $11$ the complement has signature $(2,9)$, giving $\dim_\CC \bD(T_\Co)=9$.
:::

::: {.definition #def:heegner-divisor title="Heegner divisor" defines="$(-2d)$-Heegner divisor; $\mch_{-2d}$"}

Let $N$ be an even lattice (@def:even-lattice) of signature (@def:signature) $(2, m)$, and let $\bD(N)$ be its period domain (@def:type-iv-period-domain).
For $d\in\ZZ$, the **$(-2d)$-Heegner divisor** of $\bD(N)$ is
$$
\mch_{-2d} \definedas \Union_{\delta\in N,\ \delta^2 = -2d} \theset{[\omega]\in\bD(N) \suchthat \omega\cdot\delta = 0}
$$
[@DK13, (3.2)].
:::

::: {.proposition #prop:enriques-nodal-coble-heegner title="Enriques, nodal Enriques and Coble surfaces in the Enriques period domain"}

Let $\ten = U\oplus E_{10}(2)$ be the orthogonal complement in $\lkt$ of the pullback $E_{10}(2)$ of the numerical lattice of an Enriques surface (@def:enriques-surface) to its K3 cover.
The group (@def:group) $\Orth(\ten)$ is the group $\Gamma^K_\En$ of the opening display, and it contains the group $\Orth^+(\ten)^*$ of $\fen$.

1. The period point of the K3 cover of an Enriques surface does not lie in $\mch_{-2}$.
   The quotient $\bD(\ten)/\Orth(\ten)$ is a normal quasi-projective variety (@def:projective-variety) of dimension $10$, and $\qty{\bD(\ten)\sm\mch_{-2}}/\Orth(\ten)$ is the moduli space $\mcm_\En$ of Enriques surfaces [@DK13, §3].
2. There are two $\Orth(\ten)$-orbits of $(-4)$-vectors in $\ten$ [@AEGS25, §2.3].
   One orbit (@def:group-orbit) consists of the vectors $\delta$ with $\delta^{\perp\ten}\cong T_\Nod = U\oplus\generators{4}\oplus E_8(2)$; let $\mch^{\mathrm{nod}}_{-4}\iscontainedin\mch_{-4}$ be the union of their hyperplanes.
   The divisor $\mcm^{\mathrm{nod}}_\En \definedas \qty{\mch^{\mathrm{nod}}_{-4}\sm\mch_{-2}}/\Orth(\ten)$ parametrizes nodal (@def:nodal-enriques-surface) Enriques surfaces [@AEGS25, §2.3].
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

Let $C\iscontainedin\PP^2$ be an irreducible plane sextic with ten nodes $p_1, \ldots, p_{10}$, let $S$ be the blowup of $\PP^2$ at $p_1, \ldots, p_{10}$, and let $X$ be the double cover of $S$ branched along the proper transform (@def:strict-transform) of $C$.
Let $E_0$ be the pullback to $X$ of a line in $\PP^2$, and let $E_1, \ldots, E_{10}$ be the inverse images in $X$ of the exceptional curves over $p_1, \ldots, p_{10}$.

1. $X$ is a K3 surface, and the classes $e_0, e_1, \ldots, e_{10}$ of $E_0, E_1, \ldots, E_{10}$ span a sublattice of $\Pic(X)$ isometric to
$$
S_\Co \definedas \generators{2}\oplus \generators{-2}^{10} = \latI_{1, 10}(2) = (11, 11, 1)_1 \cong \generators{-2} \oplus E_{10}(2)
.
$$
The lattice $S_\Co$ is $2$-elementary of signature $(1, 10)$ with $A_{S_\Co}\cong(\bZ/2\bZ)^{11}$ [@DK13, §3].
2. The orthogonal complement of this sublattice in $H^2(X,\ZZ)\cong\lkt$ is a $2$-elementary lattice of signature $(2, 9)$ with discriminant form $-q_{S_\Co}$ [@DK13, §3; @Nik80, Cor. 1.6.2]. Its isomorphism (@def:isomorphism-of-objects) class is determined by $-q_{S_\Co}$ [@DK13, §3; @Nik80, Thm. 3.6.2], so
$$
T_\Co \definedas S_\Co^{\perp \lkt} = (11, 11, 1)_2 \cong \generators{2} \oplus E_{10}(2)
.
$$

:::

::: {.lemma #lem:d2a-coble-moduli-quotient title="The Coble moduli space is an open subset of the orthogonal quotient"}

Let $T_\Co = \generators{2}\oplus E_{10}(2)$ be the lattice of [@DK13, (3.6)] and @prop:coble-period-domain(2), and let $\mcm_\Co$ be the moduli space of Coble surfaces of @prop:coble-moduli-git. Then $\mcm_\Co$ is isomorphic to an open subset of $\bD(T_\Co)/\Orth(T_\Co)$ [@DK13, Prop. 3.2], and that open subset is the image of the period map (@def:period-map).
:::

::: {.proof}

This is [@DK13, Prop. 3.2], whose statement is that for $N=\generators{2}\oplus E(2)$ the moduli space $\mathcal M_{\mathrm{Co}}$ of Coble surfaces is isomorphic to an open subset of $\mathcal D(N)/\Orth(N)$; $\mathcal D(N)$ is the period domain of (3.1) there and $N$ is the lattice of (3.6) there, which is $T_\Co=\generators{2}\oplus E_{10}(2)$ by @prop:coble-period-domain(2).

Its hypotheses are the ones this book already checks on the fibres. The period domain is attached to an algebraic K3 surface: the double cover of @lem:d2-unpolarised-family(1) is a K3 surface $X_b$, and $h^{2,0}(X_b)=1$, so a point of $\bD(T_\Co)$ is the $2$-dimensional positive subspace $H^{2,0}(X_b)\subset T_\Co\otimes\CC$ of @prop:coble-period-domain(1). The lattice $N$ is the transcendental lattice (@not:k3-automorphism-data) of $X_b$: the classes $e_0,\dots,e_{10}$ of @prop:coble-period-domain(1) span $M$ primitively in $\lkt$, and $T_\Co=M^{\perp\lkt}$ (@prop:coble-transcendental). So the pair $(X_b,M\subset H^2(X_b,\ZZ))$ is an $M$-polarized K3 surface in the sense of the source, and the identity of periods it uses is the identity of the Hodge structures on $T_\Co$.

[@DK13, Prop. 3.2] obtains the statement from the Torelli-type theorem for algebraic K3 surfaces of Pyatetskii--Shapiro and Shafarevich, which the source cites in its proof; that theorem is therefore not an independent input of this book, and no numbered statement of it is cited here.
:::

::: {.remark #rmk:coble-orthogonal-quotient title="The orthogonal quotient of the Coble period domain"}

The quotient $\bD(T_\Co)/\Orth(T_\Co)$ is a normal quasi-projective variety (@def:projective-variety) of dimension $9$, and the moduli space $\mcm_\Co$ of @prop:coble-moduli-git is isomorphic to an open subset of it (@lem:d2a-coble-moduli-quotient).
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

::: {.notation #not:sextic-singular-type title="Moduli of sextics of a fixed singular type" defines="$\mcv_T$; $\mcm_T$; $\wh X$; $X$; $H$; $L$; $\Delta$; $P$; $Q$"}

For a singular type $T$ with root lattice $R$, write $\mcv_T$ for the space of sextic curves $Z\subset\PP^2$ with singularities exactly of type $T$, and
$$
\mcm_T \definedas \PP\mcv_T \modmod \SL_3
$$
for the moduli space of such curves, the quotient being taken in the sense of geometric invariant theory [@YZZ25 §2.1].
Let $\wh X$ be the double cover of $\PP^2$ branched along $Z$, let $X$ be its minimal resolution (@def:minimal-resolution-of-surface-singularity) --- a K3 surface --- and let $H\in\Pic(X)$ be the pullback of the line class, so $H^2 = 2$.
The exceptional curves of $X\to\wh X$ span a copy $L\iscontainedin\Pic(X)$ of the root lattice $R$, with the exceptional classes as a base (@def:root-system-base) $\Delta$.
Write $P$ for the primitive (@def:primitive-embedding) hull of $\generators H\oplus L$ in $H^2(X;\ZZ)$ and $Q \definedas P^{\perp H^2(X;\ZZ)}$, of signatures (@def:signature) $(1,\rank R)$ and $(2, 19 - \rank R)$ [@YZZ25 §2.3].
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

The saturation (@def:saturation) of $\generators H\oplus L$ inside $H^2(X;\ZZ)$ is $(\ZZ/2)^{l'-1}$, where $l'$ is the number of irreducible components of $Z$ [@YZZ25 §5.3]; for an irreducible sextic $l' = 1$, so no saturation occurs and $P = \generators H\oplus L$.
With $H^2 = 2$ and $L = A_1^{\oplus 10} = \generators{-2}^{\oplus 10}$ this is $\generators 2\oplus\generators{-2}^{\oplus 10} = \latI_{1,10}(2)$, which is $S_\Co$ by @prop:coble-invariant-lattice.
Taking orthogonal complements in $\lkt$ gives $Q = T_\Co$, and the polarized-K3 dimension corollary (@cor:m-polarized-k3-dimension) gives the dimension.
:::

::: {.proposition #prop:sextic-cover-involution-on-root-lattice title="The covering involution on the root lattice"}

In the setting of @not:sextic-singular-type, let $\iota$ be the covering involution of $X$, let $p\colon X\to S = X/\iota$ be the quotient map, and let $f\colon S\to\PP^2$ be the minimal blowup such that the strict transform (@def:strict-transform) of $Z$ is smooth.
Then $H^2(S,\ZZ)\cong\generators{f^*h}\oplus\Lambda_S$, where $h$ is the class of a line and $\Lambda_S$ is the lattice that arises from the blowup $f$ [@YZZ25, §5.2].
Let $L^\iota$ be the sublattice of $L$ fixed by $\iota$.

1. $\iota = -w_0(L)$ as automorphisms of $L$, where $w_0(L)$ is the longest element of $W(L)$ with respect to $\Delta$ [@YZZ25, §5.2].
2. The map $p^*\colon H^2(S,\ZZ)(2)\to H^2(X,\ZZ)$ is an injective (@def:injective-map) morphism of lattices that maps $f^*h$ to $H$, and it induces a finite-index extension $\Lambda_S(2)\injects L^\iota$ [@YZZ25, §5.3].
3. $L^\iota/\Lambda_S(2)\cong(\ZZ/2)^m$, where $m$ is the number of exceptional curves of $S$ that lie in the branch locus of $p$ [@YZZ25, §5.3].
4. If $Z$ has only singularities of types $A_1$, $D_{2n}$ with $n\geq 2$, $E_7$ and $E_8$, then $L^\iota = L$. If $Z$ has only singularities of type $A_1$, then $\Lambda_S(2)\cong L$ as lattices [@YZZ25, §5.3].

:::

::: {.theorem #thm:occult-period-map-sextics title="The occult period map and its image"}

Let $\Gamma_T$ be the image of
$$
\Orth\bigl(H^2(X;\ZZ),\, \Delta,\, H\bigr) \too \Orth(Q)
,
$$
restricted to the subgroup preserving a chosen component $D(Q)$; it is arithmetic of finite index (@def:index) in $\Orth(Q)$, and contains every isometry of $Q$ acting trivially on $A_Q$ [@YZZ25 §3.1].
The **occult period map (@def:period-map)**
$$
\per_T\colon \mcm_T \too \Gamma_T\backslash D(Q)
$$
is an algebraic open embedding with image $\Gamma_T\backslash\bigl(D(Q) - \mch_T\bigr)$, where $\mch_T$ is the arrangement of hyperplanes $r^{\perp Q}$ for roots $r$ orthogonal to $H$ and not lying in $L$.
When $T$ is a nodal (@def:nodal-enriques-surface) type, $\per_T$ is moreover an isomorphism of orbifolds onto $P\Gamma_T\backslash(D(Q) - \mch_T)$ [@YZZ25 §1, §3.2, §3.3, §6.2].
:::

::: {.proof}

This is [@YZZ25, Prop. 3.2, Thms. 3.3, 3.4 and 4.11, Prop. 6.6].
:::

::: {.theorem #thm:git-equals-looijenga title="The GIT compactification is a Looijenga compactification"}

Let $\Lambda_1 \definedas H^{\perp\lkt}$, of signature (@def:signature) $(2,19)$ with $A_{\Lambda_1}\cong\ZZ/2$, and let $\Gamma_1$ be the arithmetic group (@def:arithmetic-group) (@def:group) of the degree-$2$ K3 moduli space $\Gamma_1\backslash D(\Lambda_1)$.
The roots of $\Lambda_1$ fall into two $\Gamma_1$-orbits, of divisibility (@def:lattice-divisibility) $1$ and $2$, cutting out arrangements $\mch_\Delta$ and $\mch_\infty$; the roots of $L$ all have divisibility $1$, so they contribute to $\mch_\Delta$ only [@YZZ25 §4.1, §4.2].
Set
$$
\mch^{*}_T \definedas \mch_\infty \intersect D(Q) \iscontainedin \mch_T
.
$$
Then $\per_T$ extends to an isomorphism (@def:isomorphism-of-objects)
$$
\wh{\mcm}_T \;\cong\; \overline{\Gamma_T\backslash D(Q)}^{\,\mch^{*}_T}
$$
between the GIT compactification of $\mcm_T$ and the Looijenga compactification of @def:looijenga-compactification applied to $\Gamma_T\backslash(D(Q) - \mch^{*}_T)$, compatibly with the corresponding statement of Shah and Looijenga for the whole space of sextics, $\overline{\mcm}\cong\overline{\Gamma_1\backslash D(\Lambda_1)}^{\,\mch_\infty}$ [@Sha80; @Loo02]; the two vertical maps of the resulting square are normalizations onto their images [@YZZ25 §4.2].
:::

::: {.proof}

This is [@YZZ25, Thm. 4.1, Lem. 4.8 and Thm. 4.11].
:::

::: {.proposition #prop:sextic-group-as-normalizer title="The arithmetic group as a normalizer"}

Let $\Gamma_W$ be the normalizer of the Weyl group (@def:weyl-group) (@def:group) $W = W(L)$ in the group $\Gamma_1$ of @thm:git-equals-looijenga, transported to $H^2(X;\ZZ)$ by a marking.
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
so the gluing subgroup $H_0 = \Lambda_1/(P\oplus Q)\leq A_P\oplus A_Q$ has order $2^{10} = \abs{A_P}$ and, its projection to $A_P$ being injective (@def:injective-map) [@Nik80, Prop. 1.5.1], it projects isomorphically onto $A_P$.
If some $g\in\Gamma_W$ acts nontrivially on $A_P$ --- in particular if its signed permutation of the ten classes is not a diagonal change of signs, so that it carries $r_i$ to $\pm r_j$ with $i\neq j$ --- then $\Gamma_{10A_1}\not\subseteq\discriminantkernel{T_\Co}$, and the inclusion $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{10A_1}$ is strict.
:::

::: {.proof}

Let $g\in\Gamma_W$ be such an element, with $\psi\definedas\restrictionof{g}{P}$, $\varphi\definedas\restrictionof{g}{Q}$ and class actions $\bar\psi$, $\bar\varphi$; here $g(P) = P$ because $\Gamma_W$ normalizes $W(L)$, whose generators determine the classes $r_i$ up to sign (@prop:sextic-group-as-normalizer). The isometry $g$ preserves $P\oplus Q$ and $\Lambda_1$, hence preserves $H_0$, which projects isomorphically onto $A_P$: put $\gamma\definedas p_Qp_P^{-1}$, so that $H_0$ is the graph of $\gamma$ over $A_P$. For $x\in A_P$ the class $(x,\gamma x)$ lies in $H_0$, hence so does $(\bar\psi x,\bar\varphi\gamma x)$, and a graph meets the fibre over $\bar\psi x$ in one point: $\bar\varphi\gamma x = \gamma\bar\psi x$. If $\bar\psi\neq\id$ then $\bar\varphi$ is not the identity on $\gamma(A_P)$, hence $\varphi\notin\discriminantkernel{Q} = \discriminantkernel{T_\Co}$. Since $\Gamma_{10A_1} = \Gamma_W|_Q$ (@prop:sextic-group-as-normalizer), it contains this $\varphi$; and $\widetilde\Orth^+(T_\Co)\subseteq\discriminantkernel{T_\Co}$ by its definition (@def:gamma-co-groups). Finally $\bar\psi[r_i/2] = [\pm r_j/2]\neq[r_i/2]$ for $i\neq j$, because $r_j\mp r_i$ has a coordinate equal to $1$ and so is not in $2P$.
:::

::: {.remark #rmk:coble-moduli-functor title="Two quotients in the source, and which one $\Gamma_\Co$ is the monodromy of"}

The source gives both quotients, in the same section. For lattice polarized K3 surfaces --- isomorphism classes of pairs $(X,j)$ with $j\colon M\injects\operatorname{Pic}(X)$ a primitive embedding --- the moduli space is
$$\mcm_{\mathrm{K3},M} = \mathcal D(N)/\Orth(N)^*, \qquad \Orth(N)^* = \ker\bigl(\Orth(N)\too\Orth(A_N)\bigr),$$
with $N = M^{\perp L_{\mathrm{K3}}}$ [@DK13, §3]; for the pair $M = \generators{2}\oplus\generators{-2}^{\oplus 10}$, $N = T_\Co$ of [@DK13, (3.6)] this is $\bD(T_\Co)/\discriminantkernel{T_\Co}$, the quotient by the discriminant kernel. For *unpolarized* Coble surfaces the same source gives $\mcm_\Co$ as an open subset of $\bD(N)/\Orth(N)$ [@DK13, Prop. 3.2], the quotient by the full orthogonal group.

The two differ by exactly the group whose action on $A_{T_\Co}$ decides @conj:gamma-co-stable and the $\Gamma_\Co$ form of @thm:coble-strong-lifting (@cor:gamma-co-lifting-criterion). @def:gamma-co-groups fixes which group $\Gamma_\Co$ is: the monodromy of the *unpolarized* family, that is, the second display. So the first display is not a statement about $\Gamma_\Co$ --- it is one about the monodromy of the lattice polarized family, a different group, and what it supplies is the containment of $\widetilde\Orth^+(T_\Co)$ in that other group, not in $\Gamma_\Co$ [@DK13]. For $\Gamma_\Co$ the containment in the discriminant kernel is exactly what @conj:gamma-co-stable asserts, so the $\Gamma_\Co$ form of the lifting is @prop:gamma-co-strong-lifting, which restates it under that conjecture; its sign half is unconditional (@lem:monodromy-is-spinor-positive) and its discriminant half is decided, when it can be decided at all, by the action on the ten exceptional classes (@cor:gamma-co-lifting-criterion).
:::

::: {.question #qst:sextic-group-comparison title="The comparison of the three bases"}

$\fco$ is the quotient of $D(T_\Co)$ by the monodromy group $\Gamma_\Co$ (@def:gamma-co-groups), and on the labelled base $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)), the equality being @qst:gamma-co-sign-is-realised and the identification $\Gamma_\Co=\Gamma_\Co(B)$ being research#797, item 6 (@def:gamma-co-groups(1)); accordingly, only under both is the coarse space that of $D(T_\Co)/\widetilde\Orth^+(T_\Co)$ and are the cusp counts those of the stable quotient.
The unlabelled base $\bar B$ has $\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1}$, and
$$\widetilde\Orth^+(T_\Co)\;\iscontainedin\;\Gamma_{10A_1}\;\iscontainedin\;\Orth^+(T_\Co)$$
with both inclusions strict (@lem:ten-a1-permutation-forces-strictness and the index $12\,951\,552>1$ of @thm:gamma-co-sextic-group(3)); the index of $\Gamma_\Co(B)$ in $\Gamma_\Co(\bar B)$ is $10!$ (@lem:gamma-co-labelled-index), the index of $\Gamma_{10A_1}$ in $\Orth^+(T_\Co)$ is $12\,951\,552$ (@thm:gamma-co-sextic-group(3)), and that of $\Gamma_\Co(B)$ in $\Gamma_{10A_1}$ is $10!$ times the open index $[\widetilde\Orth^+(T_\Co):\Gamma_\Co(B)]$, which is @qst:gamma-co-sign-is-realised.
What is not settled here is the map $\bar B\to M_\Co$ that forgets the sextic: whether a ten-nodal sextic is determined by its ten nodes, that is whether that map is birational, is @rmk:d2-what-is-open(2). The arithmetic model $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ of $\Gamma_{\Co,2}$ is a different group (@thm:coble-monodromy-versus-enriques).
The comparison with the polarized group is bounded on both sides: the degree-$2$ family over the labelled base has monodromy $\Gamma_\Co(B)$, so the question whether $\Gamma_\Co(B)\subseteq\Gamma_{\Co,2}$ holds is open and its recorded proof needs $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$ (@lem:d2b-family-over-the-labelled-base(4), @qst:gamma-co-sign-is-realised; this is the containment @lem:d2b-family-over-the-labelled-base(4) does not assert), while every degree-$2$ family forgets to an unpolarized one and so $\Gamma_{\Co,2}\subseteq\Gamma_\Co(\bar B)$ (@lem:d2b-forgets-to-d2a(2)); read against $R_{\gent}$, @prop:coble-monodromy-equality-false(4) gives $384\le[R_{\gent}:\Gamma_{\Co,2}]$; @prop:d2b-index-exact makes its formula and upper bound $1\,393\,459\,200$ conditional on the same open stable inclusion, and leaves $[\Gamma_{\Co,2}:\widetilde\Orth^+(T_\Co)]$ open under that inclusion. So the comparison of $\Gamma_{\Co,2}$ with $\Gamma_{10A_1}$ is the index $[\Gamma_{10A_1}:\Gamma_{\Co,2}]$ and is open, and that with $\widetilde\Orth^+(T_\Co)$ is settled only conditionally: $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$ rests on @lem:d2b-family-over-the-labelled-base(4) and hence on @qst:gamma-co-sign-is-realised, while $\Gamma_{\Co,2}\subseteq\Gamma_\Co(\bar B)$ does not.
:::

::: {.proposition #prop:sextic-root-lattice-counts title="Root lattices of plane sextics"}

The root lattices $R$ that arise from a singular type of plane sextic with simple singularities have been classified [@Ura88; @Yan96].
The maximal rank of such an $R$ is $19$, and the number of such $R$ of rank $19$, $18$, $17$, $16$ is $519$, $987$, $975$, $782$ respectively [@YZZ25, §1; @Yan96, Thm. 2.1].

:::

## The two Coble families and their bases {#sec-coble-families-d2}

Statements D2a and D2b of research#786 ask for the two families whose variations of Hodge structure define $\Gamma_\Co$ and $\Gamma_{\Co,2}$: for each, a base, its fibres, and the local system of lattices with fibre $T_\Co = \generators{2}\oplus E(2)$ of [@DK13, (3.6)].
Both are defined here by constructing the family over a base given by explicit equations; the base is then identified with the one the source uses, for D2a with the moduli space of [@DK13, Prop. 3.2] (@lem:d2a-period-map) and for D2b with the divisor $\Delta_2$ of $\fentwo$ (@lem:d2-degree-two-base).
The family and its local system are thus objects of the definition and not of a later theorem (@lem:d2-unpolarised-family, @lem:d2-local-system), and the two things the symbol $\Gamma_\Co$ needs --- a base and a family over it --- are fixed before the group is named (@def:gamma-co-groups).
@rmk:d2-what-is-open records what no source read supplies, and @rmk:d2-corrections what this section changes.

::: {.notation #not:d2-plane-sextic-base title="The plane-sextic base and its quotients" defines="$V$; $B$; labelled base; $\bar B$; unlabelled base; $U$; $M_\Co$"}

Let $\abs{\OO_{\PP^2}(6)}$ be the linear system of plane sextics and put
$$
V\definedas\theset{(Z;p_1,\dots,p_{10})\in\abs{\OO_{\PP^2}(6)}\times(\PP^2)^{10}\ \st\ p_1,\dots,p_{10}\ \text{are distinct},\ Z\ \text{is irreducible},\ \operatorname{Sing}Z=\{p_1,\dots,p_{10}\}\ \text{and each } p_i\ \text{is an ordinary double point}} .
$$
This is a locally closed (@def:locally-closed-subset) analytic subset (@def:closed-analytic-subset) of a product of projective spaces (@def:projective-morphism-of-schemes): irreducibility is open, and so is the conjunction "the $p_i$ are distinct ordinary double points (@def:ordinary-double-point) and there is no other singular point", the last because ordinary double points persist under small deformation of $Z$ (the equations $Z=\partial_xZ=\partial_yZ=0$ have invertible Jacobian, the Hessian, at an ordinary double point).
The effective group (@def:group) is $\PGL_3=\SL_3/\mu_3$: the scalars $\mu_3$ are the kernel (@def:kernel-cokernel) of $\SL_3\to\PGL_3$ and act trivially on both factors, so $\SL_3$ acts through $\PGL_3$ and $V/\SL_3=V/\PGL_3$; freeness is a statement about $\PGL_3$. The action of $\PGL_3$ on $V$ is free, and the $\SL_3$-stabilizer of every point of $V$ is $\mu_3$: the fixed points of a non-identity projectivity lie in the union of a line and a point, a line carries at most three nodes of $Z$, and no non-identity projectivity fixes all ten nodes (proved below). $S_{10}$ acts on the second factor and commutes (@def:commutative-diagram) with $\PGL_3$.
Write
$$B\definedas V/\PGL_3,\qquad \bar B\definedas[V/(\SL_3\times S_{10})]=[B/S_{10}]$$
so that $B$ is a complex analytic space and $V\to B$ is a principal $\PGL_3$-bundle (proved below), while $\bar B$ is the quotient stack of $B$ by the finite group $S_{10}$, whose coarse space is $V/(\SL_3\times S_{10})$; $B\to\bar B$ is the quotient by $S_{10}$.
Let $U\subset(\PP^2)^{10}$ be the image of $V$: the ordered ten-tuples that are the ten nodes of an irreducible sextic with ten ordinary double points. The quotient $M_\Co\definedas U/\PGL_3$ is the moduli space of Coble surfaces of [@DK13, §3], a locally closed subvariety (@def:closed-subvariety) of the GIT quotient of $(\PP^2)^{10}$ by $\PGL_3$ (@prop:coble-moduli-git), and $B\to M_\Co$ is the map forgetting the sextic.
$V$ is path connected, so $B$, $U$ and $M_\Co$ are path connected (@lem:d2-incidence-connected).
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
2. $V$ is path connected (@def:path-connectedness). Equivalently, $\Sigma$ is path connected and the monodromy group of the covering $q$ at a sextic $Z_0\in\Sigma$, a group of permutations of the ten nodes of $Z_0$, is the full symmetric group [@Har86, Lemma (1.2)].
3. $B=V/\PGL_3$, $U$ and $M_\Co=U/\PGL_3$ are path connected, and the stack $\bar B=[B/S_{10}]$ is connected.
:::

::: {.proof}

1. *The image and the fibres.* The sextic $Z$ of a point of $V$ is irreducible, hence reduced, its singular points are ten ordinary double points (@def:ordinary-double-point), and its geometric genus is $0$ (@lem:rational_sextic_ten_nodes). Conversely, a reduced and irreducible sextic of geometric genus $0$ with only nodes has exactly ten nodes by the same lemma, and each ordering of them is a point of $V$ over it. Two points of $V$ over one sextic differ by a permutation of the labels, and a permutation that fixes a point of $V$ is the identity, the ten nodes being distinct.

*The covering.* Let $Z_0\in\Sigma$ have the nodes $p^0_1,\dots,p^0_{10}$. For each $i$ take affine coordinates $(x,y)$ of $\PP^2$ at $p^0_i$ and, for $Z$ near $Z_0$, an equation $F_Z(x,y)$ of $Z$ whose coefficients are analytic functions of $Z$. The Jacobian matrix in $(x,y)$ of the map $(Z,x,y)\mapsto(\partial_xF_Z,\partial_yF_Z)$ at $(Z_0,p^0_i)$ is the Hessian of $F_{Z_0}$ at $p^0_i$, which is invertible. By the implicit function theorem there are a neighbourhood $N_i$ of $Z_0$ in $\abs{\OO_{\PP^2}(6)}$, an open neighbourhood $D_i$ of $p^0_i$ and an analytic map $\pi_i\colon N_i\to D_i$ such that, for $Z\in N_i$, the point $\pi_i(Z)$ is the only point of $D_i$ at which $\partial_xF_Z=\partial_yF_Z=0$; take the $D_i$ pairwise disjoint. The set of pairs $(Z,p)$ with $p\in\Sing Z$ is closed in $\abs{\OO_{\PP^2}(6)}\times\PP^2$, and $\PP^2\sm\bigcup_iD_i$ is compact, so there is a neighbourhood $N\subset\bigcap_iN_i$ of $Z_0$ such that $\Sing Z\subset\bigcup_iD_i$ for all $Z\in N$. A sextic $Z\in\Sigma\intersect N$ has ten singular points, all of them in $\bigcup_iD_i$ and at most one of them in each $D_i$, namely $\pi_i(Z)$; so $\Sing Z=\theset{\pi_1(Z),\dots,\pi_{10}(Z)}$. Hence
$$
q^{-1}(\Sigma\intersect N)=\bigsqcup_{\sigma\in S_{10}}\theset{\qty(Z;\pi_{\sigma(1)}(Z),\dots,\pi_{\sigma(10)}(Z))\st Z\in\Sigma\intersect N},
$$
each of the $10!$ sets on the right is open in $q^{-1}(\Sigma\intersect N)$, being cut out by the conditions $p_j\in D_{\sigma(j)}$, and $q$ maps it homeomorphically onto $\Sigma\intersect N$, with the continuous inverse $Z\mapsto\qty(Z;\pi_{\sigma(1)}(Z),\dots,\pi_{\sigma(10)}(Z))$. So $q$ is a covering map.

2. *The equivalence.* Fix $v_0=(Z_0;p^0_1,\dots,p^0_{10})\in V$. By (1) a loop $\gamma$ of $\Sigma$ at $Z_0$ lifts to a path of $V$ from $v_0$ to $\sigma_\gamma v_0$ for exactly one $\sigma_\gamma\in S_{10}$. The permutation of the nodes of $Z_0$ along $\gamma$ determines $\sigma_\gamma$ and is determined by it, so the monodromy group is the full symmetric group if and only if every $\sigma\in S_{10}$ is a $\sigma_\gamma$. If $V$ is path connected, then so is its image $\Sigma$, and a path of $V$ from $v_0$ to $\sigma v_0$ projects to a loop $\gamma$ with $\sigma_\gamma=\sigma$. Conversely, let $\Sigma$ be path connected and let every $\sigma$ be a $\sigma_\gamma$. For $v\in V$, a path of $\Sigma$ from $q(v)$ to $Z_0$ lifts to a path of $V$ from $v$ to a point $\sigma v_0$ of the fibre over $Z_0$, and the lift of a loop $\gamma$ with $\sigma_\gamma=\sigma$ joins $v_0$ to $\sigma v_0$.

*The statement.* In [@HM98, §6.E, *Initial reductions*], $V_{d,g}$ is the variety of irreducible nodal plane curves of degree $d$ and geometric genus $g$, and $m=\binom{d-1}{2}$; so $\Sigma=V_{6,0}$ and $m=10$. The statement of [@HM98, §6.E, the paragraph that precedes the uniform position principle (6.45)] is: for every two curves $C_0$ and $C_1$ of $V_{d,0}$ and every bijection between their nodes there is a family $\theset{C_t}$ of nodal curves of $V_{d,0}$ that joins $C_0$ to $C_1$, in which the nodes trace arcs $p_1(t),\dots,p_m(t)$ that induce that bijection; that is, the monodromy in the family $V_{d,0}$ acts on the nodes of $C_0$ as the full symmetric group on $m$ letters. The monodromy statement is [@Har86, Lemma (1.2)]. Let $v_0=(C_0;p_1,\dots,p_{10})$ and $v_1=(C_1;p'_1,\dots,p'_{10})$ be two points of $V$, and take the family for the bijection $p_i\mapsto p'_i$. Then $t\mapsto(C_t;p_1(t),\dots,p_{10}(t))$ is a path of $V$ from $v_0$ to $v_1$.

*The proof in the sources.* Both sources prove the statement in the same way. A rational nodal curve of degree $d$ is the projection of the rational normal curve $X\subset\PP^d$ from a subspace $\Lambda\cong\PP^{d-3}$, and its nodes correspond to the points in which $\Lambda$ meets the chordal variety of $X$. The uniform position principle [@HM98, (6.45)] states that, for a nondegenerate irreducible variety of dimension $k$ and degree $d$ in $\PP^n$, the monodromy acts as the full symmetric group on its $d$ points of intersection with a subspace $\Lambda\cong\PP^{n-k}$, as $\Lambda$ varies over the subspaces transverse to the variety. For a curve and its hyperplane sections this is the lemma in the second proof of the general position theorem of [@ACGH85, Chapter III, §1].

3. $B$ is the image of $V$ under the quotient map, $U$ is the image of $V$ under the projection to $(\PP^2)^{10}$, and $M_\Co$ is the image of $U$ under the quotient map; a continuous image of a path connected space is path connected. $\bar B=[B/S_{10}]$ has the path connected space $B$ as a smooth cover, so it is connected.
:::


::: {.lemma #lem:d2-s10-not-free title="The $S_{10}$-action on the labelled base is not free"}

The action of $S_{10}$ on $B=V/\PGL_3$ is not free. The sextic
$$
G=4x^6-12x^5y-12x^5z-3x^4y^2+30x^4yz+13x^4z^2+26x^3y^3-12x^3y^2z-26x^3yz^2-6x^3z^3-3x^2y^4-12x^2y^3z+39x^2y^2z^2+9x^2yz^3+x^2z^4-12xy^5+30xy^4z-26xy^3z^2+9xy^2z^3-xyz^4+4y^6-12y^5z+13y^4z^2-6y^3z^3+y^2z^4
$$
is irreducible and has exactly the ten ordinary double points (@def:ordinary-double-point)
$$
[0:0:1],\ [1:0:1],\ [0:1:1],\ [-1:-1:1],\ [1:0:2],\ [0:1:2],\ [-1:-1:2],\ [1:2:0],\ [-2:-1:0],\ [1:-1:0],
$$
and it is invariant under the projectivity $R$ of order $3$ with matrix
$$
R=\begin{pmatrix}0&-1&0\\1&-1&0\\0&0&1\end{pmatrix},
$$
which permutes the ten points by the cycle $(A\,B\,C)(A'\,B'\,C')(X\,Y\,Z)$ and fixes $[0:0:1]$. Hence the class in $B$ of the labelled sextic is fixed by that $3$-cycle of $S_{10}$, and $S_{10}$ does not act freely on $B$; in particular the map of coarse spaces $B\to V/(\SL_3\times S_{10})$ is not a covering.
:::

::: {.proof}

The ten points are the vertices $A=[1:0:1]$, $B=[0:1:1]$, $C=[-1:-1:1]$ and $A'=[1:0:2]$, $B'=[0:1:2]$, $C'=[-1:-1:2]$ of two triangles in perspective from the centre $[0:0:1]$, together with the intersections $X=BC\intersect B'C'$, $Y=CA\intersect C'A'$, $Z=AB\intersect A'B'$ of corresponding sides. The projectivity $R$ cycles $A,B,C$ and $A',B',C'$ and fixes the centre, so it permutes the ten points. The thirty conditions that the sextic have a double point at each of the ten points form a $30\times28$ matrix over $\QQ$; the computation `computations/reports/coble_787-s10-symmetric-sextic.py`, recorded in `computations/reports/coble_787-s10-symmetric-sextic-run.txt`, verifies in exact (@def:exact-complex) rational arithmetic that the ten points are distinct, that the matrix has rank $27$, that its one-dimensional kernel (@def:kernel-cokernel) is spanned by $G$, that $G$ is irreducible over $\QQ$, that each of the ten points is an ordinary double point (the $2\times2$ Hessian of a dehomogenized equation is nonsingular there), and that $G\circ R=G$. An irreducible plane sextic has arithmetic genus $10$, and ten ordinary double points account for all of it, so $G$ has no further singular point and the ten points are its nodes. Since $G$ is invariant, $R$ carries the labelled sextic to the relabelling of its nodes by the cycle $(A\,B\,C)(A'\,B'\,C')(X\,Y\,Z)\neq e$, so that permutation fixes the class of the labelled sextic in $B$.
:::

::: {.remark #qst:s10-free-on-B title="Freeness of $S_{10}$ on the labelled base, and why the index does not need it"}

The action of $S_{10}$ on $B$ is not free (@lem:d2-s10-not-free): a labelled ten-nodal sextic $(Z;p_1,\dots,p_{10})$ together with a projectivity $g$ with $gZ=Z$ and $gp_i=p_{\sigma(i)}$ for some $\sigma\neq e$ is a fixed point, and one is exhibited there. The index $[\Gamma_\Co(\bar B):\Gamma_\Co(B)]$ is nevertheless $10!$, because $\bar B$ is read as the quotient stack $[B/S_{10}]$: @lem:d2-labelling-cover gives the principal $S_{10}$-bundle of stacks $B\to[B/S_{10}]$ and the exact sequence, and @lem:gamma-co-labelled-index computes the index from it, with the faithfulness of the label action on $A_M$. This is an index of the presentation groups; no index involving $\Gamma_\Co$ is asserted, since $\Gamma_\Co=\Gamma_\Co(B)$ is research#797, item 6. No freeness of the $S_{10}$-action on $B$ is used, and the coarse map $B\to V/(\SL_3\times S_{10})$ is not asserted to be a covering.
:::

::: {.remark #rmk:d2-involution-moduli-of-ae22 title="The moduli of $\mathrm{K3}$ surfaces with a nonsymplectic involution of type $(11,11,1)$, and the coarse space of the Coble problem"}

Research#797 asks for the moduli functor of Coble surfaces, its stack property, its Deligne--Mumford property and its coarse space. This remark records what the sources give for the last two, in the language of the involution rather than of the sextic, and states the comparison; the functor itself and the universality of the family over $B$ are separate deliverables.

*The dictionary.* A Coble surface $S$ with its $\mathrm{K3}$ double cover is the same datum as a $\mathrm{K3}$ surface $X$ with a nonsymplectic involution $\iota$ whose quotient $X/\iota$ has $\abs{-K}=\emptyset$ and $\abs{-2K}\neq\emptyset$; the involution is part of the data and $S=X/\iota$ is recovered from it (@lem:d2-unpolarised-family(1)--(2)). The invariant lattice is $S_\Co=M=\generators{2}\oplus\generators{-2}^{\oplus10}$, of $2$-elementary type $(11,11,1)$ (@prop:coble-period-domain(1)--(2)); the anti-invariant lattice is $T_\Co=(11,11,1)_2$ (@prop:coble-period-domain(2)), which is the $T$ of the involution. The coparity $\delta$ is that of [@AE22, Def. 2.3].

*The moduli of the involution.* For a $2$-elementary hyperbolic lattice $S=(r,a,\delta)$ with $T=S^{\perp}=(22-r,a,\delta)_2$ and $\rho$ the corresponding involution of $\Lambda_{\mathrm{K3}}$, [@AE22, §2C] constructs the moduli of $\mathrm{K3}$ surfaces with a $\rho$-marking: $D_S$ is the period domain in $T\otimes\CC$, a $\rho$-marking is an isometry $\varphi\colon H^2(X,\ZZ)\iso\Lambda_{\mathrm{K3}}$ with $\iota^*=\varphi^{-1}\rho\varphi$, the $\rho$-markings of one surface are a torsor over
$$\Gamma_\rho=\theset{\gamma\in\Orth(\Lambda_{\mathrm{K3}})\ \mid\ \gamma\rho=\rho\gamma},$$
and $F_S=(D_S-\Delta)/\Gamma_\rho$ is *the coarse space* of $\mathrm{K3}$ surfaces that admit a $\rho$-marking [@AE22, §2C]. Since $\Orth(S)\to\Orth(A_S,q)$ and $\Orth(T)\to\Orth(A_T,q)$ are onto and $\Orth(A_S,q)=\Orth(A_T,q)$, the same source records $D_S/\Gamma_\rho=D_S/\Orth(T)$: the quotient is by the **full** isometry group of $T$ [@AE22, §2C].

*Consequence for the Coble coarse space.* With $S=M$ of type $(11,11,1)$ and $T=T_\Co$, the coarse space of the Coble problem is the image in $F_S$ of the Coble locus, that is of the period points at which $\abs{-2K_{X/\iota}}\neq\emptyset$. Its identification with the classical construction is [@DK13, Prop. 3.2], which places $\mcm_\Co$ as an open subset of $\bD(N)/\Orth(N)$ with $N=T_\Co$ — the same quotient by the full $\Orth(T_\Co)$ that [@AE22, §2C] names. So the coarse space of the problem is the classical one, and the group of that quotient is $\Orth(T_\Co)$, not $\widetilde\Orth^+(T_\Co)$: on the labelled presentation $\Gamma_\Co(B)$ is a subgroup of it (@thm:gamma-co-is-stable(1)); the corresponding inclusion for $\Gamma_\Co$ requires research#797, item 6, and identifying the resulting subgroup is research#780.

*A convention to check in the source.* [@AE22, §2C] defines $\Delta$ as the union of $\delta^{\perp}\cap D_S$ over the $(-2)$-vectors $\delta$ of $S$. A period point lies in $T\otimes\CC$, and $T=S^{\perp}$, so every such hyperplane contains $D_S$ and $\Delta$ would be all of $D_S$; the locus that must be removed is the one cut by the $(-2)$-vectors of $T$, which is what the application of the same section at [@AE22, §5C] uses ($0$-cusps are the $\Orth(T)$-orbits of isotropic lines in $T$). The citation is recorded here for the construction of $F_S$ and of $\Gamma_\rho$, both of which are independent of that sentence, and the discriminant is taken from the $(-2)$-vectors of $T$, as in @lem:d2-vanishing-reflections(2).

*Deligne--Mumford.* Let $\underline{\mathrm{Cob}}$ be the functor of research#797: over a scheme or complex space $Y$, objects are flat families $S\to Y$ of Coble surfaces together with the relative double cover $X\to S$ branched along the relative divisor $-2K_{S/Y}$ and its involution, and morphisms are isomorphisms of such families commuting with pullback. Two of its properties are settled without the functor's formal construction, and one is not.

First, *the stabiliser of a geometric point is $\operatorname{Aut}(S_b)$.* The double cover and its involution are determined by $S_b$ (@lem:d2-unpolarised-family(1)--(2)), so an automorphism of the object is an automorphism of the surface; and the group is never trivial, because for every choice of eight of the ten nodes the Bertini involution of those nodes is an automorphism of $S_b$ induced by no projectivity (@prop:coble-plane-model-comparison(2)). So the diagonal of $\underline{\mathrm{Cob}}$ is ramified over every point, and the stack is not an algebraic space.

Second, *the ampleness argument for finiteness is unavailable.* The standard argument — an automorphism of a $\mathrm{K3}$ surface fixing an ample class is the identity on cohomology, hence the identity by faithfulness on $H^2$ — needs an ample class, and there is none that the automorphisms preserve: the class $H=f^*\OO_{\PP^2}(1)$ is nef and **not** ample, since $H\cdot\ell_i=0$ for the ten nonzero $(-2)$-curves $\ell_i=f^*E_i$ (@lem:d2-arrangement-classes(2)), and $\sigma_I^*(H)=17H-6\sum_{i\in I}E_i\neq H$ (@prop:coble-plane-model-comparison(2)). An earlier form of this paragraph concluded finiteness, and Deligne--Mumford-ness, from the ampleness of $H$; that step is withdrawn.

Third, *the Deligne--Mumford property fails*, and it is not merely unproved: @lem:coble-automorphism-group-is-infinite exhibits two of the $45$ Bertini involutions whose product has infinite order in $\Orth(\Pic(S_b))$ at every member, so $\operatorname{Aut}(S_b)$ is infinite at every geometric point. A Deligne--Mumford stack has finite reduced stabilisers at geometric points, so $\mcM_\Co$, and every nonempty open substack of it, is not Deligne--Mumford. An earlier form of this paragraph concluded finiteness, and the property, from the ampleness of $H$; that step is withdrawn and what replaces it is the refutation.

:::

## The moduli functor of Coble surfaces {#sec-coble-moduli-functor}

@def:coble-family-unpolarized describes a class of families and then chooses a parameter space; it states no functor and no property of that parameter space as a moduli object. This section states the functor and proves the one property of it that needs no comparison with $B$.

::: {.definition #def:involution-stack title="The stack of $\mathrm{K3}$ surfaces with a nonsymplectic involution of type $(11,11,1)$"}

On $S_0=\Spec\ZZ[1/2]$-schemes of finite presentation (@def:finite-presentation), let $\mathfrak{Inv}$ assign to $Y$ the groupoid of pairs $\qty{\mcx\xrightarrow{f}Y,\ \iota}$ with $f$ flat projective of finite presentation, each geometric fibre a $\mathrm{K3}$ surface, $\iota$ an involution of $\mcx$ over $Y$, and each geometric fibre satisfying:

1. the invariant lattice (@def:invariant_coinvariant_lattices) $H^2(X_b)^{\iota_b}$ is isometric to $M=\generators{2}\oplus\generators{-2}^{\oplus10}$, of $2$-elementary type $(11,11,1)$ (@prop:coble-period-domain(1)--(2), [@AE22, §2A]);
2. $\operatorname{Fix}(\iota_b)$ is either empty or a smooth rational curve $R_b$ with $R_b^2=-2$;

with morphisms the $\iota$-equivariant Cartesian squares and pullback the fibre product.
:::

::: {.lemma #lem:sym-cotangent-birational title="$\mathrm{Sym}^m$ of the cotangent sheaf has no sections on a rational surface"}

Let $S$ be a smooth projective rational surface and $m\geq1$. Then $H^0\qty(S,\operatorname{Sym}^m\Omega^1_S)=0$.

:::

::: {.proof}

*On $\PP^2$.* The Euler sequence $0\to\Omega^1\to\OO(-1)^{\oplus3}\to\OO\to0$ embeds $\Omega^1$ in $\OO(-1)^{\oplus3}$, hence $\operatorname{Sym}^m\Omega^1$ in $\operatorname{Sym}^m\qty(\OO(-1)^{\oplus3})\cong\OO(-m)^{\oplus N}$, whose sections vanish for $m\geq1$. So $H^0\qty(\PP^2,\operatorname{Sym}^m\Omega^1)=0$.

*Invariance under a blow-up.* Let $\pi\colon S'\to S$ be the blow-up at a point with exceptional curve $E$. Since $\pi$ is an isomorphism (@def:isomorphism-of-objects) over $S\sm\theset{p}$, a section of $\operatorname{Sym}^m\Omega^1_{S'}$ restricts to a section over $S\sm\theset{p}$; conversely a section $\omega$ over $S\sm\theset{p}$ pulls back to $\pi^*\omega$, which is a section of $\operatorname{Sym}^m\Omega^1$ on $S'\sm E$ and extends across $E$ because $\omega$ extends across $p$, $S$ being smooth there. Both directions are inverse on sections, so
$$H^0\qty(S',\operatorname{Sym}^m\Omega^1_{S'})\cong H^0\qty(S\sm\theset{p},\operatorname{Sym}^m\Omega^1_S)=H^0\qty(S,\operatorname{Sym}^m\Omega^1_S),$$
the last equality because $S$ is smooth and a section over a dense open set of a vector bundle extends uniquely.

*The Hirzebruch surfaces.* Let $F_n$ be the ruled surface $\PP\qty(\OO_{\PP^1}\oplus\OO_{\PP^1}(n))$ over $\PP^1$ with $n\neq1$, with cotangent sequence
$$0\too f^*\Omega^1_{\PP^1}\too\Omega^1_{F_n}\too\Omega^1_{F_n/\PP^1}\too0 .$$
A surjection onto a sheaf with no sections says nothing about the source (@def:globular-boundary), so the argument goes through the **filtration** of $\operatorname{Sym}^m\Omega^1_{F_n}$ induced by this extension: its graded pieces are
$$\operatorname{Sym}^k\qty(f^*\Omega^1_{\PP^1})\tensor\operatorname{Sym}^{m-k}\qty(\Omega^1_{F_n/\PP^1}),\qquad k=0,1,\dots,m .$$
On a fibre $F\cong\PP^1$ one has $f^*\Omega^1_{\PP^1}|_F=\OO$ and $\Omega^1_{F_n/\PP^1}|_F=\Omega^1_F=\OO(-2)$, so the $k$-th piece restricts to $\OO(-2(m-k))$:

- for $k<m$ this has negative degree (@def:graded-object), so a section of the piece restricts to $0$ on **every** fibre, hence vanishes at every point of $F_n$ and is zero;
- for $k=m$ the piece is $f^*\OO_{\PP^1}(-2m)$, and $H^0\qty(F_n,f^*\OO(-2m))=H^0\qty(\PP^1,\OO(-2m))=0$.

The graded pieces of the filtration therefore have no sections, and $H^0$ of an extension with both ends section-free is zero, so by induction along the filtration $H^0\qty(F_n,\operatorname{Sym}^m\Omega^1)=0$.

*A rational surface.* Every minimal rational surface is $\PP^2$ or a Hirzebruch surface $F_n$ with $n\neq1$ [@Bea96, Chapter III, the classification of minimal rational surfaces], and every rational surface is obtained from one of them by a sequence of blow-ups. The invariance under blow-ups above and the two computations give $H^0\qty(S,\operatorname{Sym}^m\Omega^1_S)=0$.
:::

::: {.remark #rmk:marked-coble-covers-after-huybrechts title="Marked Coble covers, modelled on the moduli of marked $\mathrm{K3}$ surfaces"}

The unpolarized K3 problem is *not* modelled on a polarized stack. Huybrechts, *Lectures on K3 Surfaces*, Ch. 5, §1 defines the polarized functor $M_d$ and Ch. 5, §3.3 the marked space; Ch. 7 carries the period and monodromy theorems used below. The unpolarized problem is done through **marked** surfaces: $N$ is the set of isomorphism classes of pairs $(X,\varphi)$ with $\varphi\colon H^2(X,\ZZ)\iso\Lambda$ a marking Ch. 5, §3.3, it is a fine moduli space, a $20$-dimensional complex manifold which is **not Hausdorff** [@Huy16, §3.3, the warning after the construction], it carries the universal family $f\colon\mathcal X\to N$ with a marking $R^2f_*\underline\ZZ\iso\underline\Lambda$, and the global period map $\mathcal P\colon N\to\bD$ is a local isomorphism by local Torelli [@Huy16, Proposition 2.8] and is **surjective** [@Huy16, Theorem 3.1]. Global Torelli is [@Huy16, Theorem 7.5.3]. The monodromy enters at [@Huy16, Proposition 5.4]: if $\Orth(H^2(X,\ZZ))/\operatorname{Mon}(X)$ is generated by $-\id$ then $N$ has at most two connected components and $\mathcal P$ is generically injective on each; and $\Lambda$ is unimodular of signature $(3,19)$ [@Huy16, §5.4], so there is no discriminant kernel and $\widetilde\Orth^+(\Lambda)=\Orth^+(\Lambda)$.

*The Coble analogue.* Let $\rho$ be the involution of $\Lambda$ with $(+1)$-part $M=\generators{2}\oplus\generators{-2}^{\oplus10}$ and $(-1)$-part $T_\Co$. A **marked Coble cover** is a triple $(X,\iota,\varphi)$ with $\iota$ a nonsymplectic involution of the K3 surface $X$, $\varphi\colon H^2(X,\ZZ)\iso\Lambda$ an isometry with
$$\varphi\,\iota^*\,\varphi^{-1}=\rho,$$
and the quotient $X/\iota$ a Coble surface of @def:coble-moduli-functor (so $\operatorname{Fix}\iota$ is a single smooth rational curve of square $-2$). The marking is compatible with $\iota$ by construction. Let $N_\Co$ be the moduli space of these, with its period map
$$\mathcal P_\Co\colon N_\Co\too\bD(T_\Co),\qquad (X,\iota,\varphi)\longmapsto\varphi\qty(H^{2,0}(X))\subset T_\Co\tensor\CC,$$
the image lying in the $(-1)$-eigenspace because $\iota$ is nonsymplectic.

*Which Huybrechts statements carry over, step by step, to the composition of the stack monodromy.*
- *The moduli space exists and is a fine analytic space, not Hausdorff.* The construction of [@Huy16, §3.3] is local (glue the universal deformations along their intersections), and the $\rho$-compatibility is a closed condition on the marking; so the same construction gives $N_\Co$ as a complex manifold with a universal family, not Hausdorff for the same reason.
- *Local Torelli.* [@Huy16, Proposition 2.8] is a statement about the universal deformation, and it restricts to the $\iota$-invariant deformations, giving that $\mathcal P_\Co$ is a local isomorphism onto its image.
- *Surjectivity.* [@Huy16, Theorem 3.1] is the surjectivity of $\mathcal P\colon N\to\bD$; it does not by itself give the surjectivity of $\mathcal P_\Co$ onto $\bD(T_\Co)$, because a Hodge structure in $T_\Co$ has to be extended to one on $\Lambda$ admitting the involution $\rho$ and a Coble quotient. That extension is exactly the step that @rmk:coble-class-smooth-antinbicanonical and the period-map item of research#797 leave open, and it is where the Coble problem departs from Huybrechts's.
- *The monodromy group.* The argument of [@Huy16, Proposition 5.4] identifies the connected components of $N$ through $\operatorname{Mon}$, and the unimodularity of $\Lambda$ [@Huy16, §5.4] removes the discriminant kernel. Applied to $N_\Co$ it gives the monodromy group of the marked family as the subgroup of $\Orth(\Lambda,\rho)$ acting on $T_\Co$, which is $\Orth(T_\Co)$ on the nose; and the group of @def:gamma-co-groups is its restriction to $T_\Co$, which is the content of @thm:gamma-co-is-the-stack-monodromy. What the Coble problem adds, and Huybrechts's $N$ does not have, is the passage from the *marked* space $N_\Co$ to the unmarked stack $\mcM_\Co$: the marking group acting on $N_\Co$ is $\Orth(T_\Co)$, whereas the isotropy of $\mcM_\Co$ is $\Aut(S_b)$, infinite.
:::

::: {.remark #rmk:stacks-line-by-line title="Each stack in the chain: its base, its properties, and the source of each"}

The functor of @def:coble-moduli-functor-z is modelled on the groupoid formulation of Huybrechts, *Lectures on K3 Surfaces*, Ch. 5, §1, where the functor $M_d$ of degree-$2d$ polarized K3 surfaces is a category fibred in groupoids over $(\mathbf{Sch}/S)$. The lines below give, for each stack the programme uses, its base, each property, and the proof or the numbered statement. The literature record is `computations/reports/797-unmarked-moduli-literature.md`.

1. **$M_d$, degree-$2d$ polarized K3.** Base: a general $S$, and `Spec ℂ` for the coarse variety. Properties: separated **Deligne--Mumford of finite type** (Huybrechts, Ch. 5, **Theorem 5.1.3**); smooth over $\ZZ[1/2d]$ (Ch. 5, **Remark 5.4.11**). The quasi-polarized functor $M'_d$ of the same section is **not separated** (Ch. 5, §1).
2. **Marked K3 surfaces, unpolarized.** Base: $\CC$. A fine moduli space $N$, **smooth, non-Hausdorff, 20-dimensional**, with a universal family and an étale period map (Huybrechts, Ch. 6, §3.3; Kondo, *K3 Surfaces*, **Definition 6.8** and **Remark 6.10**; Alexeev--Engel, *On lattice-polarized K3 surfaces*, arXiv:2505.22557v4, **Theorem 3.11**: "a fine moduli space of marked analytic K3 surfaces, a non-separated, smooth complex analytic space of dimension 20 ... admitting a universal family"). Hausdorff reduction: Ch. 7, **Proposition 2.1**. The unmarked object is not a stack in any source read: it is the **set** $\Orth(\Lambda)\backslash N$, and the period map between quotients is a bijection (Huybrechts, Ch. 6, **Remark 3.6(iii)**) while $\Omega/\Orth(L)$ "does not have the structure of a complex analytic space" (Kondo, **Remark 6.7**). **No unpolarized unmarked moduli functor is defined in Huybrechts, Kondo, Liedtke or Alexeev--Engel.** An earlier version of this line drew from that the stronger claim that no algebraic moduli stack of unpolarized $\mathrm{K3}$ surfaces of finite type exists; that is withdrawn, the absence being one of definitions in the sources read and not of such a stack.
3. **Lattice-polarized K3, and the same with $\mathrm{ADE}$ singularities.** Base: $\CC$. Marked $(\Lambda,h)$-quasi-polarized functors: Alexeev--Engel, **Definition 4.6**; unmarked quasi-polarized stack $F^q_{\Lambda,\sigma}$: **Definition 4.21**; the marked space $M_{\Lambda,h}$ "non-separated, smooth complex analytic of dimension $20-\rank\Lambda$": **Theorem 4.7**; $F^q_{\Lambda,\sigma}=\qty[M_{\Lambda,\sigma}:\Gamma]$ with $\Gamma$ the changes of marking fixing $\Lambda$ pointwise: **Theorem 4.22**. The **lattice-polarized stack with $\mathrm{ADE}$ singularities** is the separated Deligne--Mumford stack $\qty[\bD_\Lambda:{}_W\Gamma]$ with coarse space $\bD_\Lambda/\Gamma$: **Theorem 5.5** ("the moduli stack $\mathcal{F}_{\Lambda,h}$ is isomorphic to the separated DM stack $[\bD_\Lambda:{}_W\Gamma]$"), properly discontinuous and Baily--Borel by **Remark 4.23**.
4. **Enriques, unpolarized.** Base: `Spec ℤ`. $\mcM_{\mathrm{Enriques}}$ is **a stack whose diagonal is not quasi-compact**, i.e. not quasi-separated (Liedtke, arXiv:1007.0787, Introduction and **Remark 5.3**: "the automorphism group of a generic Enriques surface is infinite and discrete ... although M_Enriques is a stack, its diagonal will not be quasi-compact"). Smooth, unirational, 10-dimensional over $\ZZ[1/2]$ is *argued* there from Proposition 5.4, not proved (**Remark 5.7**). Kondo **Remark 9.27(iii)**: "no algebraic construction of this space is known"; quasi-affine by Borcherds (**Remark 9.27(iv)**).
5. **Enriques, Cossec--Verra polarized.** Base: `Spec ℤ`. $M_{CV,\mathrm{smooth}}$ is a **quasi-separated Artin stack of finite type**, Deligne--Mumford over $\ZZ[1/2]$ (Liedtke, **Corollary 5.2**); the ample version is **Theorem 4.12**.
6. **$\mcM_\Co$, the Coble stack** of @def:coble-moduli-functor-z. Base $\ZZ[1/2]$: the only denominator in the definition is the $\mu_2$-torsor of @def:coble-moduli-functor-z(2), no polarization enters it, and so nothing divides by $2d$. fppf stack: @lem:coble-moduli-functor-fppf. **Not Deligne--Mumford, not separated**: $\Aut(S)=W_{10}(2)$ is infinite and discrete ([@CD12, §5]; @rmk:coble-automorphisms-infinite). Smooth: @prop:coble-stack-smooth-connected(1). Connected given the labelled period surjectivity: @prop:coble-stack-smooth-connected(3). **The classical complex substack is algebraic**, with smooth atlas $\bar B$: @prop:coble-stack-as-quotient proves the comparison smooth and gives its quotient presentation. **The wider class is the plane-model class over $\CC$**: every object with a single smooth anti-bicanonical curve is a blow-up of $\PP^2$ at ten double points of an irreducible rational sextic (@thm:coble-smooth-antibicanonical-is-a-plane-blowup), so over $\CC$ the comparison is essentially surjective onto the objects whose ten centres are ten distinct nodes, which form an open dense substack and not the whole of $\mcM_\Co$ (@thm:coble-classical-substack-is-open-dense-and-proper); $\bar B$ is in any case a complex base. Algebraicity and boundedness of the functor of @def:coble-moduli-functor-z over $\ZZ[1/2]$ remain open.
7. **The involution stack** @def:involution-stack and **the partial compactification** @def:enriques-partial-compactification. Base $\ZZ[1/2]$; fppf stacks (@lem:involution-stack(1), @lem:enriques-partial-compactification-stack); no further property claimed.
8. **The labelled stack.** Base $\CC$; analytic; the period map and Torelli of research#797's items 3--4; isotropy $\theset{\id,\iota}$, finite.
:::

::: {.proposition #prop:coble-stack-smooth-connected title="$\mcM_\Co$ is smooth, and connected on the classical subfamily; where the isotropy is larger"}

1. *Smoothness.* Every geometric fibre $S_b$ is a rational surface, so $H^0(S_b,\Omega^1)=0$ and, by Serre duality $H^2(S_b,T_{S_b})\cong H^0(S_b,\Omega^1_{S_b})^*$, the obstruction space $H^2(S_b,T_{S_b})$ vanishes. Deformations of $S_b$ are therefore unobstructed, and $\mcM_\Co$ is a smooth stack at every point.
2. *Connectedness on the classical subfamily.* $V$ is path connected (@lem:d2-incidence-connected(2)), hence $B=V/\PGL_3$ and $\bar B=\qty[B/S_{10}]$ are connected (@lem:d2-incidence-connected(3)); the classical objects are exactly the image of $\bar B$ (@prop:coble-plane-model-comparison(1)), so the piece of $\mcM_\Co$ carried by the classical subfamily is connected.
3. *Connectedness of the whole functor*, given the labelled step of research#797's items 3 and 4: if the period map of the labelled stack is onto $\bD(T_\Co)\sm Z$ and an equivalence onto an open part of $\qty[\qty(\bD(T_\Co)\sm Z)/G]$, then the labelled stack is connected, being the continuous image of the connected space $\bD(T_\Co)\sm Z$; and the map from the labelled stack to $\mcM_\Co$ is onto, every object admitting a labelling. A continuous image of a connected space is connected, so $\mcM_\Co$ is connected. **No plane-model argument is needed**, and the classical-subfamily restriction of @prop:coble-plane-model-comparison(1) is not used. Without the labelled step, $\mcM_\Co$ is connected by @thm:coble-classical-substack-is-open-dense-and-proper.
4. *The larger-isotropy locus.* The points whose isotropy strictly contains $\theset{\id,\iota}$ are those whose period lies in a hyperplane fixed by an extra isometry; the image of $\Aut(S_b)$ in $\Orth(T_\Co)$ is finite (@lem:period-stabiliser-finite), so the locus is a countable union of proper closed analytic subsets of the period domain, one for each nontrivial element of the finitely many possible stabilisers. It is therefore nowhere dense, and it is not shown here to be closed or to be finite in number.
:::

::: {.proof}

(1) Serre duality on a smooth projective surface gives $H^2(S,T_S)\cong H^0(S,\Omega^1_S\otimes K_S)^*$, so it suffices to show that $H^0(S,\Omega^1\otimes K_S)$ vanishes, and the vanishing of $H^0(\Omega^1)$ alone does **not** give it: tensoring by $K_S$ can create sections. The argument is instead: a nonzero section $s$ of $\Omega^1\otimes K_S$ has $s^2\neq0$ in $H^0\qty(S,\operatorname{Sym}^2\Omega^1\otimes 2K_S)$; the anti-bicanonical curve $C$ is a section of $\OO(-2K_S)$, so $s^2\cdot C$ is a nonzero section of $\operatorname{Sym}^2\Omega^1$; and that space has no sections on a rational surface by @lem:sym-cotangent-birational. Hence $H^0(S,\Omega^1\otimes K_S)=0$, the obstruction space vanishes, deformations are unobstructed, and the stack is smooth by the standard criterion that a stack locally of finite presentation with vanishing obstruction spaces is formally smooth over $\CC$.

(2) $B$ and $\bar B$ are connected (@lem:d2-incidence-connected(3)), and the image of a connected space under an essentially surjective map of stacks is connected.

(3) The labelled stack is the image of the connected period domain under the period map, and the map to $\mcM_\Co$ forgetting the labelling is onto by construction, since a labelling is extra structure on an object and not a condition. So $\mcM_\Co$ is connected once the labelled step is granted, and the only input is that step.

(4) An isometry of $T_\Co$ fixing a period point is determined by its action on that point's Hodge structure, and the extra automorphisms occur exactly where the period lies in the fixed locus of a nontrivial isometry; each such fixed locus is a proper closed analytic subset, and there are countably many isometries. Their union is therefore meagre, and the claim that it is closed, or that finitely many of them occur on the Coble locus, is not proved.
:::

::: {.lemma #lem:involution-stack title="$\mathfrak{Inv}$ is a stack, and the Coble stack sits in it"}

1. $\mathfrak{Inv}$ satisfies fppf descent, hence étale descent, by the argument of @lem:enriques-partial-compactification-stack: the fibre conditions of @def:involution-stack are conditions on geometric fibres, and the involution descends as a morphism.
2. The assignment $(S\to Y,\ X\to S,\ \iota)\mapsto(X\to Y,\ \iota)$ of @def:coble-moduli-functor-z is a morphism $\mcM_\Co\to\mathfrak{Inv}$ which is **fully faithful**: an isomorphism of $(X,\iota)$ with $(X',\iota')$ over $Y$ is the same datum as an isomorphism of the quotients $S=X/\iota$ with $S'=X'/\iota'$ compatible with the covers, because the quotient, the cover and its involution are determined by one another.
3. Its essential image over $Y$ is the locus of objects whose fixed locus is nonempty and whose quotient $X/\iota$ is a Coble surface in the narrowed sense of @rmk:coble-class-smooth-antinbicanonical — that is, the image of $R_b$ in $S_b$ is a smooth member of $\abs{-2K_{S_b}}$. So $\mcM_\Co$ is the closed-and-open piece of $\mathfrak{Inv}$ where the involution has a fixed curve, and the piece where it is free is the Enriques locus of @def:enriques-partial-compactification.
:::

::: {.proof}

(1) The geometric fibre conditions are checked after the cover; $f$ being flat and projective is local and base-change stable; $\iota$ descends as a morphism because morphisms of schemes descend (SGA 1, Exposé VIII), and the equations $\iota^2=\id$ and $f\iota=f$ hold after descent.

(2) An isomorphism $\varphi\colon(X,\iota)\to(X',\iota')$ over $Y$ induces $X/\iota\to X'/\iota'$ over $Y$, and two such $\varphi$ inducing the same map on the quotients differ by an element of $\theset{\id,\iota}$, which is the identity on the quotient; conversely a Cartesian square of the quotients commuting with the covers and involutions is an isomorphism of $X$ with $X'$ commuting with $\iota$, since $X\to S$ is the relative double cover and is determined by $(S,\iota)$. Hence the map on isomorphism groupoids is a bijection.

(3) That the quotient of an involution with a smooth fixed curve of square $-2$ is a Coble surface with a smooth anti-bicanonical member is the computation of @def:coble-moduli-functor(2); the converse is the same computation read backwards. The free locus is the Enriques case of @def:enriques-partial-compactification(1).
:::

::: {.lemma #lem:d0-coble-stack-in-involution-stack title="The Coble stack inside the moduli of $\mathrm{K3}$ surfaces with a nonsymplectic involution of type $(11,11,1)$"}

Let $\mcM_\Co$ be the functor of @def:coble-moduli-functor, a stack by @lem:coble-moduli-functor-stack, and let $\mathfrak{Inv}$ be the moduli of $\mathrm{K3}$ surfaces with a nonsymplectic involution of invariant lattice of type $(11,11,1)$ in the sense of [@AE22, §2A] and [@AE22, §2C]. Then:

1. The assignment $(S\xrightarrow{f}Y,\ X\xrightarrow{\pi}S,\ \iota)\longmapsto(X\xrightarrow{f\pi}Y,\ \iota)$ is a fully faithful morphism $\mcM_\Co\to\mathfrak{Inv}$.
2. Over $\CC$ the morphism is essentially surjective, so it is an equivalence on the groupoids of objects over a point. For every object $(X,\iota)$ of $\mathfrak{Inv}$ over $\CC$: (i) $\Fix(\iota)$ is one smooth rational curve $R$, so the quotient $X/\iota$ is rational rather than Enriques; (ii) $S\definedas X/\iota$ is a nonsingular projective rational surface with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}=\theset{C}$, where $C$ is the image of $R$, a smooth rational curve of self-intersection $-4$, and $X\to S$ is the double cover branched along $C$; so $(S,\ X\to S,\ \iota)$ is an object of $\mcM_\Co$ over $\CC$; (iii) $S$ is a blow-up of $\PP^2$ at ten points, infinitely near ones allowed, which are the double points, the infinitely near ones included, of an irreducible rational plane sextic $Z$, and $C$ is the strict transform of $Z$. The surface $S$ has a presentation (iii) by ten distinct points of $\PP^2$ that are ordinary nodes of $Z$ exactly when the object is classical; the classical objects form an open dense substack of $\mcM_\Co$, and the objects $S_{Z_8}$ and $S_{Z_{64}}$ are not classical (@thm:coble-classical-substack-is-open-dense-and-proper). Over a base $Y$, an object $(\mcx\to Y,\iota)$ of $\mathfrak{Inv}$ lies in the essential image exactly when $\qty(\mcx/\iota\to Y,\ \mcx\to\mcx/\iota,\ \iota)$ is an object of $\mcM_\Co$ over $Y$; its geometric fibres are objects of $\mcM_\Co$ over $\CC$ by (i)--(ii).
3. On that image the monodromy representation is the explicit composite
$$\rho\colon\pi_1(\mcM_\Co,s)\too\Gamma_\rho\longrightarrow\Orth(T_\Co),\qquad \Gamma_\rho=\theset{\gamma\in\Orth(\Lambda_{\mathrm{K3}})\mid\gamma\rho=\rho\gamma},$$
whose first map is given by the $\rho$-markings, a $\Gamma_\rho$-torsor over each surface [@AE22, §2C], and whose second is the restriction to $T_\Co=S^{\perp}$.
:::

::: {.proof}

1. As before: $S=X/\iota$ and $\iota$ is recovered from $(X,\iota)$, and $\pi$ is determined by $\iota$, so the functor is injective on objects up to unique isomorphism and bijective on morphism sets.

2. *From $\mcM_\Co$ to $\mathfrak{Inv}$.* Let $(S\to Y,X\to S,\iota)$ be an object of $\mcM_\Co$. Each geometric fibre $S_b$ is a Coble surface with $\abs{-2K_{S_b}}=\theset{C_b}$ one connected smooth curve, and $X_b$ is the double cover branched along $C_b$, a $\mathrm{K3}$ surface (@def:coble-moduli-functor(1)--(2)). The involution $\iota_b$ fixes the preimage of $C_b$ pointwise; its differential at a point of that curve has the eigenvalues $1$ and $-1$, so $\iota_b$ acts on $H^{2,0}(X_b)$ by $-1$ and is nonsymplectic. Its invariant lattice is of type $(11,11,1)$ (@lem:coble-invariant-lattice-in-families(1)). So $(X\to Y,\iota)$ is an object of $\mathfrak{Inv}$.

*From $\mathfrak{Inv}$ to $\mcM_\Co$, over $\CC$.* Let $(X,\iota)$ be an object of $\mathfrak{Inv}$ over $\CC$. Its invariant lattice has rank $11$ and discriminant group $(\ZZ/2)^{11}$, and steps 4--6 of the proof of @thm:coble-period-surjectivity use nothing else about $\iota$. Step 4 gives (i) [@AN06, §2.3; @AE22, §2A, (1)]. Steps 5 and 6 give (ii): $S=X/\iota$ is a nonsingular projective rational surface, $X\to S$ is the double cover branched along the image $C$ of $R$, a smooth rational curve with $C^2=-4$, $\abs{-K_S}=\emptyset$, $\abs{-2K_S}=\theset{C}$, and $\iota$ is the covering involution. So $(S,X\to S,\iota)$ is an object of $\mcM_\Co$ over $\CC$ (@def:coble-moduli-functor), and it maps to $(X,\iota)$. For (iii), @thm:coble-smooth-antibicanonical-is-a-plane-blowup(2)--(3) gives a birational morphism $S\to\PP^2$ with ten centres and with $Z$ the image of $C$, and @prop:coble-plane-models-are-double-point-sextics(1) gives that the centres are the singular points of $Z$ and of its successive strict transforms and that each of them is a double point. Over a base $Y$, a preimage of $(\mcx\to Y,\iota)$ is isomorphic to $\qty(\mcx/\iota\to Y,\ \mcx\to\mcx/\iota,\ \iota)$ by the proof of 1; this is the last sentence of the clause.

3. $\bT$ has fibre $T_\Co$ (@lem:d2-local-system) and its transport is the action of isometries on $T_\Co$ (@prop:local-system-of-lattices-monodromy); the markings give a $\Gamma_\rho$-torsor [@AE22, §2C], so a loop acts by an element of $\Gamma_\rho$ and on $T_\Co$ by its restriction. That the ambient group is $\Orth(T_\Co)$ and not $\widetilde\Orth^+(T_\Co)$ is @rmk:d2-involution-moduli-of-ae22.

*The classical objects.* A presentation (iii) by ten distinct nodes is a further condition on the object and does not follow from (i) and (ii). It holds for the classical objects, whose fibre data are those of @lem:d2-unpolarised-family(1), and these form an open dense substack. It fails for $S_{Z_8}$ and $S_{Z_{64}}$, each of which contains eight $(-2)$-curves with dual graph $E_8$ (@ex:coble-sextics-with-an-a15-point, @prop:coble-e8-configuration-excludes-ten-distinct-centres). An object for which it fails has a class of square $-4$ or $-6$ in $\Pic(X)^-$; in the period coordinates this condition cuts out a locally finite union of hypersurfaces (@thm:coble-classical-substack-is-open-dense-and-proper(1), (3)).
:::


::: {.definition #def:coble-moduli-functor title="The moduli functor of Coble surfaces"}

Let $\mathfrak{C}$ be the category of complex spaces. The functor
$$
\mcM_\Co\colon\mathfrak{C}^{\mathrm{op}}\too\mathfrak{Grpd}
$$
assigns to $Y$ the groupoid whose **objects** are triples $\qty{\mcs\xrightarrow{f}Y,\ \mcx\xrightarrow{\pi}\mcs,\ \iota}$ with:

1. $f$ flat, proper and of finite presentation (@def:finite-presentation), whose geometric fibres are Coble surfaces $S$ in the sense of [@DZ99, Introduction] — nonsingular projective rational with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}\neq\emptyset$ — **with $\abs{-2K_S}$ consisting of one connected smooth curve $C$**. Both halves of that condition are forced 
by the owner's object, and neither implies the other: a disjoint union of two smooth curves is smooth and disconnected, and smoothness alone therefore does not give a single curve. Smoothness: the cover branched along a non-reduced member is neither normal nor a $\mathrm{K3}$ surface, so a non-reduced member is not admissible. Connectedness: the volume's Coble moduli is $F_{\Co}=F_{\Co,1}$, the $n=1$ case of $F_{\Co,n}$, where $\abs{-2K_S}=C_1+\cdots+C_n$ (@prop:coble-k3-cover); a smooth divisor with $n>1$ components has $\chi(\operatorname{Fix}\iota)=2n$ and invariant lattice (@def:invariant_coinvariant_lattices) of rank $10+n$, not the $M$ of type $(11,11,1)$ [@DZ99, §6, Proposition 6.4(2)];
2. $\pi$ the relative double cover branched along $\mcC$, that single smooth member; since $\mcC=2\mcD$ for $\mcD=-\K_{\mcs/Y}$, the cover exists, is smooth because $\mcC$ is, its canonical class is $\pi^*(K_{\mcs/Y}+\mcD)=0$, so its fibres are $\mathrm{K3}$ surfaces [@DK13, §3], and their invariant lattice is $M$ of type $(11,11,1)$ because the fixed curve is a single smooth rational curve (@prop:coble-period-domain(1)--(2));
3. $\iota$ the covering involution of $\pi$;

and whose **morphisms** $\qty{f,\pi,\iota}\to\qty{f',\pi',\iota'}$ over $Y$ are Cartesian squares over $Y$ commuting with $\pi$ and $\iota$. The **pullback** along $g\colon Y'\to Y$ is the fibre product $(-\times_Y Y')$, with the induced $\pi$ and $\iota$.
:::

::: {.lemma #lem:coble-moduli-functor-stack title="$\mcM_\Co$ is a stack"}

$\mcM_\Co$ is a stack for the étale topology on $\mathfrak{C}$, hence also for the analytic topology.

1. *Isomorphisms are a sheaf.* For two objects over $Y$ the isomorphisms form a subsheaf of the sheaf of isomorphisms of the underlying families of spaces, cut out by the equations expressing the commutativity with $\pi$ and $\iota$; a map of complex spaces is determined by its restrictions to an open cover.
2. *Objects descend.* Let $Y'\to Y$ be étale and surjective with its two projections, and let an object over $Y'$ with a descent datum be given. The underlying spaces $\mcs'$ and $\mcx'$ and the morphisms $f'$, $\pi'$, $\iota'$ descend to $Y$ by faithfully flat descent for complex spaces (SGA 1, Exposé VIII, *Descente fidèlement plate*); the descended $f$ is flat and proper because these are local on the base and stable under base change.
3. *The fibre condition and the branch divisor descend.* The condition of @def:coble-moduli-functor(1), that a geometric fibre is a Coble surface whose anti-bicanonical system consists of one connected smooth curve, is a condition on each geometric fibre, hence checked after the étale cover; it does not refer to a plane model. The divisor $-2K_{\mcs/Y}$ is defined by the relative canonical sheaf, so it descends with $f$; and the double cover of (2) is $\Spec_{\OO_\mcs}\qty(\OO_\mcs\oplus\OO_\mcs(-\mcD))$ for any $\mcD$ with $\OO(2\mcD)=\OO(-2K_{\mcs/Y})$, which is canonical in $\mcD$ up to the sign of the summand, so it and its involution are determined by the descended family.
:::

::: {.proof}

(1) is the sheaf property of the presheaf of isomorphisms of two spaces over $Y$, restricted by closed conditions.

(2) SGA 1, Exposé VIII, is the descent statement for faithfully flat morphisms of finite presentation (@def:finite-presentation); an étale surjection is such a morphism, and the effectivity of the descent datum is its conclusion for the pair of spaces and the morphisms between them. Flatness and properness of the descended morphism are local on the base in the étale topology.

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

*Departure, and the repair it forced.* An earlier form of these two definitions asked only that $\abs{-2K}$ *contain* a smooth member, and that is false as a description of one lattice: [@DZ99, §6, Proposition 6.4(2)] gives Coble surfaces whose unique anti-bicanonical divisor is smooth but is a disjoint union of $(-4)$-curves, so a smooth divisor with $n>1$ components satisfies the weaker condition, has $\chi(\operatorname{Fix}\iota)=2n$ and invariant lattice of rank $10+n$, and is not an object of @def:involution-stack. The condition is therefore a single smooth curve, not a smooth member, and the earlier statement that every object of the functor is labellable was proved only for the $n=1$ case it silently assumed.

This class is not the classical class $\Bl_{p_1,\dots,p_{10}}\PP^2$ of ten distinct nodes. Its objects are the blow-ups of the ten double points of the irreducible rational sextics whose singular points are double points (@thm:coble-smooth-antibicanonical-is-a-plane-blowup, @prop:coble-plane-models-are-double-point-sextics); a double point can be a cusp and centres can be infinitely near (@ex:coble-sextics-with-an-a15-point); and some objects have no plane presentation by ten distinct nodes (@prop:coble-e8-configuration-excludes-ten-distinct-centres). The classical objects form an open dense substack, so the widening adds no component to $\mcM_\Co$ (@thm:coble-classical-substack-is-open-dense-and-proper).
:::

::: {.theorem #thm:coble-smooth-antibicanonical-is-a-plane-blowup title="A Coble surface with a single smooth anti-bicanonical curve is a blow-up of the plane at ten double points of an irreducible sextic"}

Let $S$ be a Coble surface in the sense of [@DZ99, Introduction] — a nonsingular projective rational surface with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}\neq\emptyset$ — and suppose that $\abs{-2K_S}=\theset{C}$ consists of one connected smooth curve $C$. Then:

1. $C$ is rational, $C^2=-4$, $K_S^2=-1$, and $S$ is minimal as a Coble surface in the sense of [@DZ99, §1.1].
2. $S$ is *basic* in the sense of [@DZ99, §4.1]: it admits a birational morphism onto $\PP^2$, and so is a blow-up $\Bl_{p_1,\dots,p_{10}}\PP^2$ at ten points, each $p_i$ a point of the blow-up at $p_1,\dots,p_{i-1}$, so that a centre can be infinitely near to an earlier one. With $H$ the pullback of $\OO_{\PP^2}(1)$ and $E_1,\dots,E_{10}$ the total transforms in $S$ of the exceptional curves of the ten centres, $\Pic(S)=\ZZ H\oplus\bigoplus_i\ZZ E_i$ with $H^2=1$, $E_i^2=-1$ and all other products zero, $-K_S=3H-\tsum_iE_i$ and $C=-2K_S=6H-2\tsum_iE_i$.
3. The image $Z\definedas\pi(C)\subset\PP^2$ of $C$ is an irreducible plane sextic; the map $C\to Z$ is the normalisation; every singular point of $Z$ is the image of one of the ten centres, and $Z$ has multiplicity $2$ there. In particular $\delta(Z)=\pa(Z)-\pa(C)=10$, so the singular points of $Z$ are the whole of its arithmetic genus.
4. Suppose the ten $p_i$ are distinct points of $\PP^2$. Then $Z$ has exactly ten double points, each of $\delta=1$, and each is an ordinary node or an ordinary cusp; the node occurs exactly when $C$ meets $E_i$ in two distinct points and the cusp exactly when it meets it in one point of multiplicity two (@lem:coble-double-point-of-the-sextic). In the plane model of [@DZ99, Theorem 2.5] the ten points are distinct as soon as the nine base points of the Halphen pencil are, which is the case of the classical class (@rmk:which-coble-surfaces-have-a-plane-model).
:::

::: {.proof}

*1.* By hypothesis $C\equiv-2K_S$. Since $S$ is rational, [@DZ99, Lemma 1.2(1)] computes the arithmetic genus of a divisor as $\pa(D)=h^0(D+K_S)$, so $\pa(C)=h^0(-K_S)=0$ because $\abs{-K_S}=\emptyset$; a smooth connected curve of arithmetic genus $0$ is $\PP^1$. Adjunction on $S$ then gives $-2=2\pa(C)-2=C^2+K_S\cdot C=4K_S^2-2K_S^2$, that is $K_S^2=-1$ and $C^2=4K_S^2=-4$. For minimality, a nontrivial birational morphism of $S$ onto another Coble surface $S'$ presents $S$ as the blow-up of $S'$ at $k\geq1$ points, so $K_S^2=K_{S'}^2-k$, which with $K_{S'}^2\leq-1$ for every Coble surface [@DZ99, §1.1] contradicts $K_S^2=-1$; that is the statement of [@DZ99, §1.1] that a Coble surface with $K^2=-1$ is minimal.

*2.* By [@DZ99, Lemma 1.10] a Coble surface admits a blow-down, so $S$ carries a $(-1)$-curve $E$; let $\pi\colon S\to Y$ be the blow-down of $E$. Since $S$ is minimal in the sense of clause 1, [@DZ99, Corollary 1.6] gives $\pa(D+2E)=1$ for every $D\in\abs{-2K_S}$; in particular $\pa(C+2E)=1$.

*3.* Write $C_Y\definedas\pi(C)$. Since $-2K_S=-2\pi^*K_Y-2E=\pi^*(-2K_Y)$ we have $\pi_*C=C_Y\in\abs{-2K_Y}$, and $C_Y$ is reduced: $\pi$ is an isomorphism away from $E$, and $C$ is reduced. By [@DZ99, Lemma 1.5(1)] $\pa(C+2E)=h^0(-K_Y)$, so $h^0(-K_Y)=1$ and $\abs{-K_Y}=\theset{D_0}$ for an effective divisor $D_0\neq0$. Then $2D_0\in\abs{-2K_Y}$ as well, and $2D_0\neq C_Y$ because $C_Y$ is reduced and $2D_0$ is not; hence $h^0(-2K_Y)\geq2$. Pullback along $\pi$ is an isomorphism on sections, so $h^0(-2K_S+2E)=h^0(-2K_Y)\geq2$, and the decomposition $\abs{-2K_S+2E}=M+P$ of [@DZ99, §2.1], with $M$ the mobile part, has $M\neq0$.

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

$C$ is the branch divisor, so the preimage of $E$ is $\pi^*E$, of square $2E^2=-2$. Away from $C\cap E$ the covering $\pi$ is étale, so $\pi^{-1}(E)$ is smooth there and of degree two over $E\cong\PP^1$. Over a point of $C\cap E$ the equation of $\pi$ is $w^2=s$ for a local equation $s$ of $C$, so $\pi^{-1}(E)$ is $w^2=s=0$. A double cover of $\PP^1$ branched at two distinct points is a $\PP^1$, which is 1; branched at one point of multiplicity two it is two copies of $\PP^1$ glued at that point, which is 2. For 3: $\mult_{p_i}Z=C\cdot E_i$ is the multiplicity of $C$ at the point of $E_i$ lying over $p_i$ [@DZ99, Remark 3.3], and $C$ is smooth, so the two branches of $Z$ at $p_i$ are the images of the points of $C\cap E_i$: two distinct tangent directions in case 1, giving an ordinary node, and one direction with the tangent cone a double line in case 2, giving an ordinary cusp.
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
Neither polynomial is a square, so each affine curve is irreducible, and it is birational to a conic, $u^2=-48^{-3}(w^2+32w+288)$ and $u^2=192^{-3}(w+40)(w+72)$, hence rational. Its singular points are the multiple roots of $P$: for $Z_8$ the nodes $w=0$ and $w=4$, which are $(x,y)=(1,0)$ and $(0,0)$; for $Z_{64}$ the node $w=0$, which is $(2,0)$, and the cusp $w=-40$, where $P$ has a triple root, which is $(-3,0)$. Each curve meets the line $z=0$ only at $o$, where the equation restricts to $x^6$, so the sextic is irreducible; in the chart $y=1$ its term of lowest degree at $o$ is $z^2$, so $o$ is a double point. An irreducible rational sextic has $\tsum\delta=10$, so $\delta(o)=8$, and $o$ has two branches, the two points at infinity of the conic; a double point with two branches and $\delta=8$ is $A_{15}$. An $A_{15}$ point $\eta^2=\xi^{16}$ is resolved by eight blow-ups, the strict transform after $i<8$ of them having an $A_{15-2i}$ point at the origin of the chart $\eta=\xi^i\eta_i$, which lies on the last exceptional curve $\theset{\xi=0}$ and not on the strict transform of the one before; that is the statement on $p^{(1)},\dots,p^{(8)}$, and it gives $[R_i]=E_i-E_{i+1}$. The line $z=0$ meets $Z$ at $o$ with multiplicity $6$ and nowhere else. A blow-up at a point of multiplicity $1$ on the line and $2$ on the curve lowers their intersection number by $2$, and the strict transform of $Z$ meets the exceptional curve of $p^{(i)}$ only at $p^{(i+1)}$; so the strict transforms of the line pass through $p^{(1)},p^{(2)},p^{(3)}$, and after the third blow-up they do not meet the strict transform of $Z$, hence not $p^{(4)}$. So $[L]=H-E_1-E_2-E_3$. The intersection numbers follow from $H^2=1$, $E_i^2=-1$.

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

*3.* Let $\mathcal X\to\operatorname{Def}(X_0)$ be the universal deformation of the cover $X_0$ of $S_0$; its base is smooth of dimension $20$ [@Huy16, Ch. 6, Cor. 2.7], and its period map $\mathcal P\colon\operatorname{Def}(X_0)\to D\subset\PP\qty(H^2(X_0,\CC))$ is a local isomorphism [@Huy16, Ch. 6, Prop. 2.8]. The automorphism $\iota_0$ acts on $\mathcal X\to\operatorname{Def}(X_0)$ [@Huy16, Ch. 6, Rem. 2.6], and $\mathcal P$ intertwines its action on the base with $\iota_0^*$ on $D$. The fixed locus of $\iota_0^*$ on $\PP\qty(H^2(X_0,\CC))$ is $\PP(M_\CC)\sqcup\PP\qty((T_\Co)_\CC)$, and $\mathcal P(0)=H^{2,0}(X_0)\in\PP\qty((T_\Co)_\CC)$; so, after shrinking, $\mathcal P$ maps the fixed locus $U\subset\operatorname{Def}(X_0)$ of $\iota_0$ isomorphically onto an open subset of $D\intersect\PP\qty((T_\Co)_\CC)=\Omega_{T_\Co}$, of dimension $9$. Over $U$ the action of $\iota_0$ is an involution $\iota_u$ of each fibre $X_u$, with $\iota_u^*=\iota_0^*=\id_M\oplus(-\id_{T_\Co})$ under the transport of $H^2$. By @thm:coble-period-surjectivity(4), applied to $X_u$ with the marking by transport and the automorphism $\iota_u$, the conclusions (1)--(3) of that theorem hold: $\Fix(\iota_u)$ is one smooth rational curve and $S_u\definedas X_u/\iota_u$ is an object of $\mcM_\Co$ over $\CC$. This is the family.

A class $\ell\in H^2(X_0,\ZZ)$ is of type $(1,1)$ on $X_u$ if and only if $\mathcal P(u)\in\ell^{\perp}$ [@Huy16, Ch. 6, §2.4], so $\Pic(X_u)^-=T_\Co\intersect\mathcal P(u)^{\perp}$. Hence the fibres in $\mcH$ are those with $\mathcal P(u)\in\delta^{\perp}$ for some $\delta\in T_\Co$ with $\delta^2\in\theset{-4,-6}$. Each $\delta^{\perp}\intersect\Omega_{T_\Co}$ is a proper closed analytic hypersurface, the quadric $\omega^2=0$ of $\PP\qty((T_\Co)_\CC)$ being irreducible and not contained in a hyperplane, and the union is locally finite by the argument of @prop:the-coble-locus-in-the-period-domain(1), which uses only that the squares of the classes are bounded. The fibres with $\Pic(X_u)^-\neq0$ lie on the countably many hypersurfaces $\ell^{\perp}$, $0\neq\ell\in T_\Co$, whose complement is dense by the Baire category theorem. The last sentence is 1 and 2.

*4.* By @ex:coble-sextics-with-an-a15-point both surfaces contain eight $(-2)$-curves with dual graph $E_8$; apply @prop:coble-e8-configuration-excludes-ten-distinct-centres.

*The consequences.* Openness is 2. For density and for the limits, 3 gives for every object $S_0$ a family through $S_0$ whose classical fibres are dense; in particular $S_0$ is joined to a classical object by a path in $U$, which with the connectedness of $\mcM^{\mathrm{cl}}_\Co$ gives that of $\mcM_\Co$.
:::

::: {.lemma #lem:coble-canonical-class-and-ample-component-in-families title="Transport in a family of Coble covers carries the canonical class to the canonical class and the ample component to the ample component"}

For an object $(S,\ \pi\colon X\to S,\ \iota)$ of $\mcM_\Co$ over $\CC$ put
$$M_S\definedas H^2(X,\ZZ)^{\iota},\qquad \kappa_S\definedas\pi^*K_S\in M_S,\qquad P_S\definedas\theset{x\in M_S\tensor\RR\st x^2>0},$$
and let $C_S$ be the connected component of $P_S$ that contains the classes $\pi^*a$, $a$ an ample class of $S$.

1. *The ample component.* $M_S$ has signature $(1,10)$ (@lem:coble-invariant-lattice-in-families(1)), so $P_S$ has two connected components. The classes of the $\iota$-invariant Kähler forms of $X$ lie in one of them, and it contains every $\pi^*a$; so $C_S$ is well defined, and it is the component that contains the classes of the $\iota$-invariant Kähler forms.
2. *Frames.* Let $\pi_0\colon S\to\PP^2$ be a birational morphism, $H$ the pullback of a line and $E_1,\dots,E_{10}$ the total transforms of the exceptional curves of its ten centres (@thm:coble-smooth-antibicanonical-is-a-plane-blowup(2)). Then $e_0\definedas\pi^*H$, $e_i\definedas\pi^*E_i$ is a basis of $M_S$ with Gram matrix $\diag(2,-2,\dots,-2)$, $\kappa_S=-3e_0+\tsum_ie_i$, and $e_0\in C_S$. So the frame is an isometry of $M_S$ with $M=\generators{e_0,\dots,e_{10}}$ that carries $\kappa_S$ to $K=-3e_0+\tsum_ie_i$ and $C_S$ to the component of the positive cone of $M$ that contains $e_0$. It identifies the group
$$G_S\definedas\theset{g\in\Orth(M_S)\st g\kappa_S=\kappa_S,\ g\,C_S=C_S}$$
with $\Stab_{\Orth(M)}(K)\intersect\Orth^+(M)$, and restriction to $K^{\perp M}$ maps that group isomorphically onto $\Orth^+\qty(K^{\perp M})=W(E_{10})$.
3. *Isomorphisms.* An isomorphism of objects $(S,X,\iota)\to(S',X',\iota')$ over $\CC$ induces an isometry $M_S\to M_{S'}$ that carries $\kappa_S$ to $\kappa_{S'}$ and $C_S$ to $C_{S'}$.
4. *Families.* Let $\qty{f\colon\mcs\to Y,\ \pi\colon\mcx\to\mcs,\ \iota}$ be an object of $\mcM_\Co$ over an arcwise connected, locally simply connected complex space $Y$, and let $\bM$ be its local system of invariant lattices (@lem:coble-invariant-lattice-in-families(1)), with fibre $\bM_y=M_{\mcs_y}$. The transport of $\bM$ along a path from $y$ to $y'$ carries $\kappa_{\mcs_y}$ to $\kappa_{\mcs_{y'}}$ and $C_{\mcs_y}$ to $C_{\mcs_{y'}}$. Hence the monodromy group of $\bM$ on $Y$ at $y$ is contained in $G_{\mcs_y}$, which every plane frame of $\mcs_y$ identifies with $W(E_{10})$.
:::

::: {.proof}

*1.* The surface $X$ is projective, because $\pi$ is finite and $S$ is projective; so $X$ has Kähler forms, and for a Kähler form $\omega$ the form $\tfrac12(\omega+\iota^*\omega)$ is Kähler and $\iota$-invariant. The class of an $\iota$-invariant Kähler form is an $\iota^*$-invariant real class of positive square, so it lies in $P_S$, the space $M_S\tensor\RR$ being the $\iota^*$-invariant part of $H^2(X,\RR)$. These classes form a convex set, so they lie in one component of $P_S$. For an ample class $a$ of $S$ the class $\pi^*a$ is ample, because $\pi$ is finite; so it is the class of a Kähler form $\omega$, and of the $\iota$-invariant Kähler form $\tfrac12(\omega+\iota^*\omega)$, because $\iota^*\pi^*a=\pi^*a$.

*2.* The classes $H,E_1,\dots,E_{10}$ are a basis of $\Pic(S)=H^2(S,\ZZ)$ with $H^2=1$, $E_i^2=-1$ and all other products zero, and $K_S=-3H+\tsum_iE_i$ (@thm:coble-smooth-antibicanonical-is-a-plane-blowup(2) and step *5* of its proof). The map $\pi^*\colon H^2(S,\ZZ)\to M_S$ is injective and multiplies the form by $2$ (@lem:coble-invariant-lattice-in-families(1)), so $e_0,\dots,e_{10}$ have Gram matrix $\diag(2,-2,\dots,-2)$, of determinant $2^{11}$, and they span a sublattice of finite index $d$ in $M_S$. The lattice $M_S$ is isometric to $M$ (@lem:coble-invariant-lattice-in-families(1), @lem:every-object-of-the-functor-is-labellable), of determinant $2^{11}$; from $2^{11}=d^2\cdot2^{11}$ one gets $d=1$. Then $\kappa_S=\pi^*K_S=-3e_0+\tsum_ie_i$. For an ample class $a$ of $S$ one has $e_0\cdot\pi^*a=2\,H\cdot a>0$, because $H$ is the class of a nonzero effective divisor; and $e_0^2=2>0$. In a lattice of signature $(1,10)$ a vector of positive square has positive product with the vectors of exactly one component of the positive cone, its own (the fact used at @lem:transport-order-on-the-classical-coble-stack(4)); so $e_0$ lies in the component of $\pi^*a$, which is $C_S$. An isometry of $M$ preserves the component of $e_0$ exactly when it lies in $\Orth^+(M)$ (@prop:spinor-plus-cone-components), which is the identification of $G_S$. Restriction to $K^{\perp M}$ is injective on $\Stab_{\Orth(M)}(K)$, one has $M=K^{\perp M}\oplus\ZZ K$, and an element of $\Stab_{\Orth(M)}(K)\intersect\Orth^+(M)$ restricts to an element of $\Orth^+\qty(K^{\perp M})$ (@lem:transport-order-on-the-classical-coble-stack(5)). Conversely an element of $\Orth^+\qty(K^{\perp M})$ extends by the identity on $\ZZ K$ to an isometry of $M$ that fixes $K$; it preserves the component of the positive cone of $K^{\perp M}$ that lies in the component of $e_0$, so it preserves the component of $e_0$. The equality $\Orth^+\qty(K^{\perp M})=W(E_{10})$ is $K^{\perp M}\cong E_{10}(2)$ (@lem:transport-order-on-the-classical-coble-stack(5)) with [@Dol07, (5.12)], as in the paragraph *The orthochronous part of the stabilizer* of the proof of @thm:coble-monodromy-on-m-classical. These are statements about the lattice $M$ and use no local system.

*3.* An isomorphism of objects is a pair of isomorphisms $g\colon S\to S'$ and $\tilde g\colon X\to X'$ with $\pi'\tilde g=g\pi$ and $\tilde g\iota=\iota'\tilde g$ (@def:coble-moduli-functor). The isometry $\tilde g_*=(\tilde g^*)^{-1}$ of $H^2(X,\ZZ)$ with $H^2(X',\ZZ)$ commutes with the involutions, so it maps $M_S$ onto $M_{S'}$. It satisfies $\tilde g_*\pi^*=\pi'^*g_*$, and $g_*K_S=K_{S'}$, so $\tilde g_*\kappa_S=\kappa_{S'}$. For an ample class $a$ of $S$ the class $g_*a$ is ample on $S'$, so $\tilde g_*\pi^*a=\pi'^*g_*a\in C_{S'}$; an isometry carries a component of $P_S$ onto a component of $P_{S'}$, so $\tilde g_*C_S=C_{S'}$.

*4.* *The canonical class.* The morphism $f$ is flat with nonsingular fibres, hence smooth, and the relative canonical sheaf is a line bundle on $\mcs$ whose first Chern class in $H^2(\mcs,\ZZ)$ restricts to $K_{\mcs_y}$ on every fibre. A class in $H^2(\mcs,\ZZ)$ defines a section of $R^2f_*\underline\ZZ$ whose values are its restrictions to the fibres; so $y\mapsto\pi^*K_{\mcs_y}$ is a section of $\bM$, and transport carries the value of a section at one end of a path to its value at the other (@def:transport-and-monodromy).

*The ample component: what is to be proved.* It is enough to prove:

($\ast$) every $y_0\in Y$ has a simply connected open neighbourhood $O$ such that, for every $y\in O$, the transport $T$ of $\bM$ along a path of $O$ from $y_0$ to $y$ carries $C_{\mcs_{y_0}}$ to $C_{\mcs_y}$.

Indeed, for $y,y'\in O$ the transport along a path of $O$ from $y$ to $y'$ is then the composite of the inverse of the transport from $y_0$ to $y$ with the transport from $y_0$ to $y'$ (@prop:transport-homotopy-invariant), so it carries $C_{\mcs_y}$ to $C_{\mcs_{y'}}$; and by the Lebesgue number lemma a path of $Y$ is a concatenation of finitely many paths, each inside one such $O$, whose transports compose (@prop:transport-homotopy-invariant(2)).

*A family over a complex manifold.* Let $g\colon\mathcal Z\to D$ be a proper holomorphic submersion of complex manifolds with fibres $Z_d$ of complex dimension $2$, let $d_0\in D$, and let $\omega_0$ be a Kähler form on $Z_{d_0}$. Then $d_0$ has a simply connected open neighbourhood $D'$ such that, for every $d\in D'$ and every Kähler form $\omega_d$ on $Z_d$, every class
$$s\,T[\omega_0]+(1-s)[\omega_d]\in H^2(Z_d,\RR),\qquad 0\leq s\leq1,$$
has positive square, where $T$ is the transport of $R^2g_*\underline\RR$ along a path of $D'$ from $d_0$ to $d$. For the proof, $Z_{d_0}$ is a compact submanifold of $\mathcal Z$, so it has an open neighbourhood $W$ with a smooth retraction $r\colon W\to Z_{d_0}$, a tubular neighbourhood. The form $\Omega\definedas r^*\omega_0$ is a closed real $2$-form on $W$ with $\Omega|_{Z_{d_0}}=\omega_0$. Let $J$ be the complex structure of $\mathcal Z$ and $V\definedas\ker(dg)$ the bundle of tangent vectors of the fibres, which $J$ preserves. The function $v\mapsto\Omega(v,Jv)$ is continuous on $V|_W$, and it is positive on the nonzero vectors of $V|_{Z_{d_0}}$ because $\omega_0$ is a Kähler form. Fix a Riemannian metric on $\mathcal Z$ and a compact neighbourhood $N$ of $d_0$. The unit vectors of $V$ over $g^{-1}(N)$ form a compact set, because $g$ is proper; those that lie over a point outside $W$, or on which $\Omega(v,Jv)\leq0$, form a closed subset of it, whose image in $D$ is compact and does not contain $d_0$. So there is a simply connected open neighbourhood $D'$ of $d_0$, a ball of a chart, with $g^{-1}(D')\subseteq W$ and $\Omega(v,Jv)>0$ for every nonzero $v\in V$ over $g^{-1}(D')$. Let $d\in D'$, put $\Omega_d\definedas\Omega|_{Z_d}$, and let $\omega_d$ be a Kähler form on $Z_d$. For $0\leq s\leq1$ the form $\theta_s\definedas s\,\Omega_d+(1-s)\,\omega_d$ is closed and satisfies $\theta_s(v,Jv)>0$ for every nonzero tangent vector $v$ of $Z_d$. So $\theta_s$ is nondegenerate, and $\theta_s\wedge\theta_s$ is a nowhere vanishing $4$-form that depends continuously on $s$. It is positive for the orientation of the complex structure at $s=0$, where it is the square of a Kähler form; so it is positive for every $s$, and $[\theta_s]^2=\int_{Z_d}\theta_s\wedge\theta_s>0$. Finally the class of $\Omega$ on $g^{-1}(D')$ defines a section of $R^2g_*\underline\RR$ over $D'$ whose value at $d$ is $[\Omega_d]$ and whose value at $d_0$ is $[\omega_0]$; so $[\Omega_d]=T[\omega_0]$ (@def:transport-and-monodromy), and $[\theta_s]=s\,T[\omega_0]+(1-s)[\omega_d]$.

*Proof of ($\ast$).* Let $y_0\in Y$ and $X_0\definedas\mcx_{y_0}$. The morphism $\mcx\to Y$ is flat and proper with fibres $\mathrm{K3}$ surfaces, so near $y_0$ it is a deformation of $X_0$. Let $g\colon\mathcal Z\to\operatorname{Def}(X_0)$ be the universal deformation of $X_0$; its base is smooth [@Huy16, Ch. 6, Cor. 2.7], so, after shrinking the base, $g$ is a proper holomorphic submersion of complex manifolds with fibres $\mathrm{K3}$ surfaces. By the universal property there are an open neighbourhood $O_1$ of $y_0$ and a holomorphic map $h\colon O_1\to\operatorname{Def}(X_0)$ with $h(y_0)=0$ such that $\mcx|_{O_1}$ is the pullback of $\mathcal Z$ along $h$. Then the fibre of $\mcx$ over $y$ is $Z_{h(y)}$, the local system $R^2(f\pi)_*\underline\RR$ on $O_1$ is the pullback of $R^2g_*\underline\RR$ along $h$, and its transport along a path $\alpha$ of $O_1$ is the transport of $R^2g_*\underline\RR$ along $h\circ\alpha$ (the argument of @lem:coble-family-base-change). Let $\omega_0$ be an $\iota_{y_0}$-invariant Kähler form on $X_0$, let $D'$ be the neighbourhood of $0$ that the preceding paragraph gives for $g$, $d_0=0$ and $\omega_0$, and let $O\subseteq h^{-1}(D')$ be a simply connected open neighbourhood of $y_0$, which exists because $Y$ is locally simply connected. Let $y\in O$, let $T$ be the transport along a path of $O$ from $y_0$ to $y$, and let $\omega_y$ be an $\iota_y$-invariant Kähler form on $\mcx_y$. By the preceding paragraph the classes $s\,T[\omega_0]+(1-s)[\omega_y]$, $0\leq s\leq1$, have positive square. The involution $\iota$ acts on the local system $R^2(f\pi)_*\underline\ZZ$ (@lem:coble-invariant-lattice-in-families(1)), so $\iota^*$ commutes with transport, and $T[\omega_0]$ is $\iota_y^*$-invariant because $[\omega_0]$ is $\iota_{y_0}^*$-invariant; and $[\omega_y]$ is $\iota_y^*$-invariant. So these classes form a segment in $P_{\mcs_y}$, and $T[\omega_0]$ lies in the component of $[\omega_y]$, which is $C_{\mcs_y}$ by 1. Since $[\omega_0]\in C_{\mcs_{y_0}}$ by 1, and the isometry $T$ carries a component of $P_{\mcs_{y_0}}$ onto a component of $P_{\mcs_y}$, one gets $T\,C_{\mcs_{y_0}}=C_{\mcs_y}$.

*The monodromy group.* The transport along a loop at $y$ is an isometry of $\bM_y$ that fixes $\kappa_{\mcs_y}$ and $C_{\mcs_y}$; this is the definition of $G_{\mcs_y}$, and the identification with $W(E_{10})$ is 2.
:::

::: {.corollary #cor:coble-monodromy-on-m-of-the-whole-stack title="On $\mcM_\Co$ the transports of the invariant lattice generate $W(E_{10})$; this is the monodromy group of the stack conditional on a chart and on the descent (D)"}

Use the notation of @lem:coble-canonical-class-and-ample-component-in-families. Let $x$ be a classical object over $\CC$, the fibre over a point $s\in B$ of the family of @lem:d2-unpolarised-family(3), and identify $M_x$ with $M=\generators{e_0,\dots,e_{10}}$ by the plane frame at $s$, as in @thm:coble-monodromy-on-m-classical; put $K=-3e_0+\tsum_ie_i$. Let $\mathcal T_x\subseteq\Orth(M_x)$ be the set of the composites
$$M_x=M_{x_0}\too M_{x_1}\too\cdots\too M_{x_n}=M_x$$
of isometries of the following two kinds, between the invariant lattices of objects $x_0,\dots,x_n$ of $\mcM_\Co$ over $\CC$: the transport, along a path of the base, of the system $\bM$ of a family of objects of $\mcM_\Co$ over an arcwise connected, locally simply connected complex space (@lem:coble-invariant-lattice-in-families(1)); and the isometry induced by an isomorphism of objects over $\CC$. The set $\mathcal T_x$ is a subgroup of $\Orth(M_x)$: the inverse of a transport is the transport along the reversed path, and the inverse of the isometry of an isomorphism is the isometry of the inverse isomorphism.

1. *Families and isomorphisms, without a stack.* $\mathcal T_x=G_x$, and the plane frame identifies it with
$$\Stab_{\Orth(M)}(K)\intersect\Orth^+(M)\cong\Orth^+\qty(K^{\perp M})=W(E_{10}) .$$
The transports of the family over $B$ and the isomorphisms between its fibres already generate this group. In particular the monodromy group on the invariant lattice of every family of objects of $\mcM_\Co$ over an arcwise connected, locally simply connected complex space, classical or not, is contained in $W(E_{10})$. This clause uses no local system on a stack and no descent.

For the stack $\mcM_\Co$ assume the following two hypotheses.

(A) The stack $\mcM_\Co$ has a chart $p\colon X\to\mcM_\Co$ by a locally simply connected complex space $X$, the map $p$ being a family of objects over $X$, for which the hypotheses of @not:paths-of-a-groupoid-quotient hold; so $\pi_1(\mcM_\Co,x)$ is defined and @lem:haefliger-paths-exhaust-the-fundamental-groupoid applies to $p$.

(D) The systems $\bM_f$ of the families $f\colon Y\to\mcM_\Co$ over spaces are the pullbacks of one local system of lattices $\bM$ on $\mcM_\Co$, including the comparisons along $2$-morphisms and their cocycle conditions, the comparison along an isomorphism of families being the isometry that it induces on the invariant lattices. So, in the notation of @not:paths-of-a-groupoid-quotient, the transport of $\bM$ along $[f\alpha]$, for a path $\alpha$ of $Y$, is the transport of $\bM_f$ along $\alpha$, and the transport of $\bM$ along the class $[\rho]$ of an identification $\rho$ of two objects over $\CC$ is the isometry induced by the isomorphism $\rho$.

Hypothesis (D) is the descent along the $2$-morphisms, research#797, item 4, left open by @rmk:the-descent-stops-at-the-2-morphisms. For a quotient stack it is the hypothesis (D) of @lem:orbifold-monodromy-of-a-nonfree-quotient: clauses 1--2 of that lemma compute the transport of each loop without it, as clause 1 does here, and its clause 3 is the descent. Hypothesis (A) belongs to research#797, item 1: the volume constructs a chart for $\mcM^{\mathrm{cl}}_\Co$ only (@prop:coble-stack-as-quotient), and the algebraicity of $\mcM_\Co$ is open (@rmk:stacks-line-by-line(6)). Neither hypothesis is proved here. Clause 2 is conditional on both, and clause 3 on (A).

2. *The stack.* Under (A) and (D), the monodromy group of $\bM$ on $\mcM_\Co$ at $x$ is $\mathcal T_x$:
$$\operatorname{Mon}_{\mcM_\Co}(\bM)=W(E_{10}) .$$
This is the group that @thm:coble-monodromy-on-m-classical computes on the classical substack.
3. $\mcM_\Co\sm\mcH$ is an open substack contained in $\mcM^{\mathrm{cl}}_\Co$ whose complement is, in the period coordinates of @thm:coble-classical-substack-is-open-dense-and-proper(3), a locally finite union of proper closed analytic hypersurfaces. So @prop:the-generic-locus-sees-the-whole-group applies to it, and under (A) and the hypotheses of that proposition $\pi_1\qty(\mcM^{\mathrm{cl}}_\Co)\to\pi_1\qty(\mcM_\Co)$ is onto.
:::

::: {.proof}

*1.* Each step of a composite carries the class $\kappa$ and the component $C$ of its source to those of its target (@lem:coble-canonical-class-and-ample-component-in-families(3)--(4)); so the composite fixes $\kappa_x$ and $C_x$, that is $\mathcal T_x\subseteq G_x$, and the plane frame identifies $G_x$ with the displayed groups (@lem:coble-canonical-class-and-ample-component-in-families(2)). For the other inclusion let $r=(g,\tilde g)\colon b\to b'$ be a point of the groupoid $R_B$, an isomorphism between the fibres over $b$ and $b'$ of the family over $B$ (@lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(1)). The base $B$ is path connected (@lem:d2-incidence-connected(3)), and the transport of the system $\bM$ of the family over $B$ along every path of $B$ is the identity in the global frame $\varepsilon_0,\dots,\varepsilon_{10}$ (@lem:coble-invariant-lattice-in-families(2)). So the composite of the transport along a path of $B$ from $s$ to $b$, the isometry of $r$, and the transport along a path of $B$ from $b'$ to $s$ is, in that frame, the matrix $m(r)$ of @lem:transport-order-on-the-classical-coble-stack, and $m(r)\in\mathcal T_x$. The reflections $s_{\delta_1},\dots,s_{\delta_9}$ are the matrices $m(r)$ of the relabelling arrows of the transpositions $(i\ i+1)$, and $s_{\delta_c}$ is, up to a relabelling, the matrix $m(r)$ of the arrow that the quadratic Cremona transformation of three nodes defines at a general point of $B$ (@lem:cremona-second-plane-model-general, @lem:coble-image-on-m-is-the-weyl-group(2)); the ten reflections generate $W(E_{10})$ (@lem:coble-image-on-m-is-the-weyl-group(1)--(2)). This is the paragraph *Lower bound* of the proof of @thm:coble-monodromy-on-m-classical, which computes with the matrices of isomorphisms of surfaces. Hence $W(E_{10})\subseteq\mathcal T_x$. The statement on the families is @lem:coble-canonical-class-and-ample-component-in-families(4).

*2.* By (A) the chart $p$ is an epimorphism, so there are a point $a\in X$ and an identification of $x$ with $p(a)$, and by @lem:haefliger-paths-exhaust-the-fundamental-groupoid(1) every element of $\pi_1(\mcM_\Co,x)$ is a product of that identification, of classes $[p\alpha]$ of paths $\alpha$ of $X$, of classes $[\rho]$ of identifications of objects over $\CC$, and of the inverse of that identification. A path of $X$ lies in one path component of $X$, which is an arcwise connected, locally simply connected complex space. So by (D) the transport of $\bM$ along the loop is a composite of transports of the system $\bM_p$ of the family $p$ along paths and of isometries induced by isomorphisms of objects: it is an element of $\mathcal T_x$. Conversely, let $P\colon B\to\mcM_\Co$ be the family over $B$ and $r\colon b\to b'$ a point of $R_B$. By (D) the composite displayed in the proof of 1 is the transport of $\bM$ along the loop $[Pc_b]\,[r]\,[Pc_{b'}]^{-1}$ of $\mcM_\Co$ at $x$, for paths $c_b$, $c_{b'}$ of $B$ from $s$ to $b$ and to $b'$. So the monodromy group contains every $m(r)$, and with 1 it is $\mathcal T_x=W(E_{10})$.

*3.* The inclusion is @thm:coble-classical-substack-is-open-dense-and-proper(1) and the description of the complement is (3) there; a loop of $\mcM_\Co$ that is moved into $\mcM_\Co\sm\mcH$ lies in $\mcM^{\mathrm{cl}}_\Co$.
:::

::: {.lemma #lem:coble-moduli-functor-fppf title="$\mcM_\Co$ is a stack for the fppf topology over $S_0$"}

$\mcM_\Co$ satisfies fppf descent, hence étale descent: isomorphisms are a sheaf; objects descend; the fibre conditions and the branch divisor descend.

:::

::: {.proof}

Let $Y'\to Y$ be faithfully flat of finite presentation, with the two projections, and let an object over $Y'$ with a descent datum be given. The underlying schemes and the morphisms $f'$, $\pi'$, $\iota'$ descend to $Y$ by faithfully flat descent (SGA 1, Exposé VIII), the descended $f$ being flat and projective because both are local on the base and stable under base change. The condition of clause (1) — nonsingular, projective, rational, $\abs{-K}=\emptyset$, $\abs{-2K}\neq\emptyset$ — is a condition on geometric fibres, so it is checked after $Y'\to Y$; widening the class from the classical subfamily to the whole of [@DZ99, Introduction] changes nothing in this argument, because no step used the narrower description. The divisor $-2K_{\mcs/Y}$ is defined by the relative canonical sheaf of the descended $f$, and the $\mu_2$-torsor of clause (2) is $\Spec(\OO\oplus\OO(-\mcD))$, determined by that divisor and by the choice of $\mcD$ up to the sign of the second summand; so $\pi$ and $\iota$ descend with $f$. Isomorphisms are a subsheaf of the sheaf of isomorphisms of the underlying $Y$-schemes cut out by closed conditions, as in @lem:coble-moduli-functor-stack(1).
:::

::: {.definition #def:enriques-partial-compactification title="The partial compactification of the Enriques stack by involutions with empty or curve fixed locus"}

Let $S_0=\Spec\ZZ[1/2]$. On $S_0$-schemes of finite presentation (@def:finite-presentation) the functor $\mcM^{\partial}_\En$ assigns to $Y$ the groupoid of pairs $\qty{\mcx\xrightarrow{f}Y,\ \iota}$ in which $f$ is a flat projective family of $\mathrm{K3}$ surfaces and $\iota$ an involution of $\mcx$ over $Y$ whose geometric fibres satisfy exactly one of:

1. $\operatorname{Fix}(\iota_b)=\emptyset$, the Enriques case;
2. $\operatorname{Fix}(\iota_b)$ is a smooth rational curve $R_b$ with $R_b^2=-2$, the Coble case (over $\CC$ the quotient $X_b/\iota_b$ is then a Coble surface whose anti-bicanonical system is the single smooth rational curve that is the image of $R_b$, and $R_b$ is the ramification curve: steps 5 and 6 of the proof of @thm:coble-period-surjectivity; the quotient is a blow-up of $\PP^2$ at the ten double points, the infinitely near ones included, of an irreducible rational sextic (@prop:coble-plane-models-are-double-point-sextics(1)), and it has such a presentation by ten distinct nodes exactly when it is classical);

with morphisms the $\iota$-equivariant Cartesian squares over $Y$ and pullback the fibre product. The two conditions of (1) and (2) are complementary, so $\mcM^{\partial}_\En$ is the disjoint union of its two loci.
:::

::: {.lemma #lem:enriques-partial-compactification-stack title="$\mcM^{\partial}_\En$ is a stack over $\ZZ[1/2]$"}

$\mcM^{\partial}_\En$ satisfies fppf descent, hence étale descent: isomorphisms are a sheaf, objects descend, and the fixed-locus condition descends.
:::

::: {.proof}

Let $Y'\to Y$ be faithfully flat of finite presentation with a descent datum for an object. The scheme $\mcx'$, the morphism $f'$ and the involution $\iota'$ descend by faithfully flat descent (SGA 1, Exposé VIII), $f$ remaining flat and projective because both are local on the base and stable under base change. Being a $\mathrm{K3}$ surface and the two alternatives of @def:enriques-partial-compactification are conditions on geometric fibres, hence checked after $Y'\to Y$: the fixed locus of an involution is computed fibrewise, and whether it is empty, or a smooth rational curve of self-intersection $-2$, is a property of the fibre alone. Isomorphisms form a subsheaf of the sheaf of isomorphisms of the underlying $Y$-schemes, cut out by the equations expressing equivariance for $\iota$, as in @lem:coble-moduli-functor-stack(1).
:::

::: {.proposition #lem:coble-is-the-boundary-divisor title="The Coble stack is the boundary divisor over $\delta^{\perp}$"}

1. The locus of @def:enriques-partial-compactification(1) is the stack of smooth Enriques surfaces; the locus of (2) is $\mcM_\Co$, by $S_b=X_b/\iota_b$ with $X_b\to S_b$ the double cover of @def:coble-moduli-functor(2).
2. The period map (@def:period-map) of $\mcM^{\partial}_\En$ lands in $\bD(\ten)/\Orth(\ten)$, and the image of the Enriques locus is $\qty{\bD(\ten)\sm\mch_{-2}}/\Orth(\ten)$, the moduli space of Enriques surfaces [@DK13, §3] (@prop:enriques-nodal-coble-heegner(1)).
3. The image of the Coble locus is the Heegner divisor $\mch_{-2}/\Orth(\ten)$, birationally isomorphic to $\mcm_\Co$ (@prop:enriques-nodal-coble-heegner(3)), so $\mcM_\Co$ is a divisor of $\mcM^{\partial}_\En$ and its image is $\mch_{-2}$.
4. The normal data are the class of the fixed curve: at a point of the Coble locus the fixed locus is a smooth rational curve $R_b$ of square $-2$ in $X_b$, with $[R_b]$ spanning the $(-2)$-line orthogonal to $\ten$ in $H^2(X_b)$, and $f^*[C_b]=2R_b$ for the anti-bicanonical curve $C_b$ of $S_b$ (step 5 of the proof of @thm:coble-period-surjectivity).
:::

::: {.proof}

(1) For a fixed-point-free involution the quotient is an Enriques surface, and conversely the K3 cover of an Enriques surface is a fixed-point-free invariant; for an involution of a complex $\mathrm{K3}$ surface whose fixed locus is a smooth rational curve $R$, the differential at a point of $R$ has the eigenvalues $1$ and $-1$, so the involution is nonsymplectic; the quotient $S$ is then a nonsingular projective rational surface with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}=\theset{C}$, where $C$ is the image of $R$ and is a smooth rational curve, by steps 5 and 6 of the proof of @thm:coble-period-surjectivity, which use only that $\Fix(\iota)$ is the smooth rational curve $R$. So the quotient with its double cover is an object of @def:coble-moduli-functor over $\CC$. Its plane models are those of @prop:coble-plane-models-are-double-point-sextics(1), and a plane model whose ten centres are ten distinct nodes of the sextic exists for the classical objects only (@thm:coble-classical-substack-is-open-dense-and-proper).

(2) is the cited statement, whose hypothesis is that the periods of the K3 covers of Enriques surfaces avoid $\mch_{-2}$, which is [@DK13, §3] and @prop:enriques-nodal-coble-heegner(1).

(3) is @prop:enriques-nodal-coble-heegner(3), the quotient $\mch_{-2}/\Orth(\ten)$ being birationally isomorphic to $\mcm_\Co$; the identification of the Coble locus with $\mcM_\Co$ is (1).

(4) For every object $S_b$ the ramification curve of the double cover is $R_b=f^*(-K_{S_b})$, of square $2(-K_{S_b})^2=-2$ because $K_{S_b}^2=-1$ (@thm:coble-smooth-antibicanonical-is-a-plane-blowup(1)), and $C_b=-2K_{S_b}$ gives $f^*C_b=2R_b$; its class is orthogonal to $f^*\Pic(S_b)\supseteq\ten$-side and spans the line $\QQ R_b$ in $H^2(X_b)$, which is the direction in which the period leaves $\ten$ when the Enriques condition fails.
:::

::: {.remark #rmk:dm-route-through-ae22-fails title="The Deligne--Mumford property cannot be deduced from the comparison with the involution moduli as the sources stand"}

The quickest route to the Deligne--Mumford property of $\mcM_\Co$ would be to pull it back along the fully faithful $\mcM_\Co\to\mathfrak{Inv}$ of @lem:d0-coble-stack-in-involution-stack: a monomorphism has the diagonal of its target as the diagonal, so DM-ness of $\mathfrak{Inv}$ would give an unramified diagonal for $\mcM_\Co$.

That route has no input. The construction in [@AE22, §2C] produces the $\rho$-marked period domain $\bD_S$, the discriminant $\Delta=\bigcup_\delta\delta^{\perp}$ over the $(-2)$-vectors of $S$, the torsor $\Gamma_\rho=\theset{\gamma\in\Orth(\lk)\mid\gamma\rho=\rho\gamma}$, and then states that $F_S=\qty(\bD_S\sm\Delta)/\Gamma_\rho$ is **the coarse space** of $\mathrm{K3}$ surfaces that admit a $\rho$-marking. It is a quotient of a domain by a group, i.e. an analytic space, and no Deligne--Mumford statement for a stack of $\mathrm{K3}$ surfaces with involution occurs in that source. (The one DM statement in the group's papers is [@AE23, §2], for the stack $F_{2d}$ of *polarized* $\mathrm{K3}$ surfaces, which is a different moduli problem.)

So the only route left is the first one in the item: finite automorphism groups and an unramified diagonal, whose missing input is the finiteness of the group generated by the 45 Bertini involutions in $\Orth(\Pic(S_b))$ (@rmk:d2-involution-moduli-of-ae22).
:::

::: {.proposition #prop:coble-stack-as-quotient title="The classical Coble substack as the quotient of $\bar B$ by the plane-model groupoid"}

Let $\mcM^{\mathrm{cl}}_\Co$ be the full substack of $\mcM_\Co$ on the classical objects of @def:coble-family-unpolarized, equivalently the essential image of the comparison $\varphi$ of @prop:coble-plane-model-comparison. Then $\varphi\colon\bar B\to\mcM_\Co$ is smooth, and its restriction to $\mcM^{\mathrm{cl}}_\Co$ is a smooth cover. Consequently
$$
\mcM^{\mathrm{cl}}_\Co\ \cong\ \qty[\bar B\big/R],\qquad R=\bar B\times_{\mcM^{\mathrm{cl}}_\Co}\bar B,
$$
where the groupoid $R\rightrightarrows\bar B$ is the *plane-model groupoid*: its objects over $Y$ are pairs of plane presentations of one family of Coble surfaces, its morphisms the isomorphisms of such pairs, and the two maps to $\bar B$ are the two projections. The Cremona plane model of @prop:coble-plane-model-comparison(3) and the Bertini automorphisms of (2) are morphisms of $R$ over the points where they act. The display does not present $\mcM_\Co$: $\mcM^{\mathrm{cl}}_\Co$ is an open dense substack of $\mcM_\Co$ and not all of it (@thm:coble-classical-substack-is-open-dense-and-proper).
:::

::: {.proof}

*Smoothness.* At $b=(Z;p_1,\dots,p_{10})\in V$ the $\PGL_3$-stabilizer is trivial (@lem:d2-plane-sextic-freeness(2)). Grivaux's configuration space $\mathfrak S_{10}$ of ordered, possibly infinitely near, ten-tuples carries the family $\mathfrak X_{10}$ of blowups, and $\mathfrak X_{10}$ is a complete deformation at every point of the locus $\mathfrak S_{10}^{\dagger}$ where $\PGL_3$ acts freely [@Gri18, Prop. 3.1]. Thus every deformation of the surface $S_b$ is locally the pullback of $\mathfrak X_{10}$ along a map to $\mathfrak S_{10}$ through the configuration $(p_1,\dots,p_{10})$. After shrinking the base, that map factors through the locus of ten distinct points.

Now let a family of $\mcM_\Co$ restrict at a point to $S_b$, and take the local map supplied by completeness. On every fibre the blowup canonical formula gives $-2K=6H-2\sum_iE_i$ (@prop:canonical-class-of-blowup), so the anti-bicanonical divisor is the proper transform of a plane sextic having multiplicity at least two at the ten blown-up points. Its ten Hessians are nonzero at the centre, hence remain nonzero nearby; smoothness away from those points and irreducibility of the proper transform likewise hold because the relative anti-bicanonical curve is a single smooth curve. The nearby fibres therefore give points of $V$, with the ten blown-up points as ordered nodes. Pulling back @lem:d2-unpolarised-family(2) recovers the surface, and its canonical anti-bicanonical double cover and involution recover the rest of the object. This local lifting of every object and of its square-zero deformation diagrams is exactly the versality criterion for smoothness of the classifying morphism. Essential surjectivity onto $\mcM^{\mathrm{cl}}_\Co$ is @prop:coble-plane-model-comparison(1), so the restriction is a smooth cover. No general-position or unnodal hypothesis enters this argument.

*The quotient.* A stack is the quotient of any smooth cover by its Čech groupoid; applied to $\varphi\colon\bar B\to\mcM^{\mathrm{cl}}_\Co$ this gives the display with $R$ the fibre product. By @prop:coble-plane-model-comparison(3) two distinct ten-nodal sextics can present the same surface, so $R$ is not the trivial groupoid, and the difference is exactly the plane-model equivalence of @prop:coble-plane-model-comparison(4); the Bertini involution of (2) is an automorphism of the same point of $\bar B$ only when the sextic is invariant under it, so it contributes automorphisms of $R$ rather than a second presentation. The final clause is @thm:coble-classical-substack-is-open-dense-and-proper.
:::

::: {.remark #rmk:coble-automorphisms-infinite title="The automorphism groups of Coble surfaces are discrete and infinite, so the stack is not of finite type"}

The finiteness input that @rmk:d2-involution-moduli-of-ae22 asked for is unavailable, and the reason is a theorem: the automorphism groups are infinite.

1. *Unnodal case.* $\Aut(X)^*$ contains the subgroup $W_{10}(2)=\theset{w\in W_{10}\mid w(v)-v\in 2E_{10}\ \text{for all } v\in\Pic(X)}$ of the Weyl group $W_{10}=W(E_{10})$, under the natural identification $W_X=W_{10}$ [@CD12, §5, the theorem labelled `autocoble`], a normal subgroup with quotient the finite group $O^+(10,\bF_2)$ [@CD12, §5, the remark after that theorem]; for a general Coble surface in the sense of moduli the automorphism group *is* $W_{10}(2)$ [@CD12, §5, the remark at the end of the same subsection]. So $\Aut(S)$ is a $2$-congruence subgroup of $W_{10}$, hence infinite.
2. *Consequence for the group scheme.* Since $H^0(S,T_S)=0$ for a rational surface, $\Aut(S)$ is a discrete group scheme over $\CC$; it is not finite. The Bertini involutions lie in it, so the group they generate is infinite as well: finiteness cannot be the route to the Deligne--Mumford property, and the question of @rmk:d2-involution-moduli-of-ae22 is closed in the negative.
3. *Which properties hold.* The fibres of the diagonal of $\mcM_\Co$ are the group schemes $\Aut(S_b)$, discrete and infinite. The diagonal is representable with reduced, discrete fibres — unramified in the sense that its fibres are disjoint unions of reduced points — but it is not quasi-compact and not of finite type over the base. Consequently:
   - $\mcM_\Co$ is a stack (@lem:coble-moduli-functor-stack, @lem:coble-moduli-functor-fppf);
   - it is *not* locally of finite type over $\CC$, because the discrete fibre $\Aut(S_b)$ is infinite;
   - it is therefore *not* a Deligne--Mumford stack in the standard sense, which requires an unramified diagonal **and** local finite type, and it is not quasi-separated, hence not separated, in the sense in which a separated stack has quasi-compact diagonal;
   - what remains true is that its inertia is discrete: every automorphism group scheme is a disjoint union of reduced points, so the higher isotropy is trivial.
4. *Departure.* This contradicts the expectation recorded in @rmk:d2-involution-moduli-of-ae22 that the subgroup of $\Orth(\Pic(S_b))$ generated by the $45$ Bertini involutions is finite, and it contradicts the Deligne--Mumford claim made for the involution moduli in earlier rounds. It is reported as a departure, not as a new answer: the DM property of $\mcM_\Co$ is false as stated, and the correct statement is item 3.
:::

::: {.remark #rmk:coble-labelled-versus-unlabelled title="Where the quotient presentation and the automorphism groups disagree: the labelling"}

The period-map presentation of research#797's items 3 and 4 works with the groupoid of **labelled** Coble covers, whose objects are $(S,\ X\xrightarrow{\pi}S,\ \iota;\ e_0,e_1,\dots,e_{10})$ with the eleven classes part of the data, and it presents that groupoid by $[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]$. The stack of @def:coble-moduli-functor, by contrast, has no labelling. The two descriptions are of different stacks, and the difference is exactly the marking.

1. *The labelled isotropy is $\theset{\id,\iota}$, not trivial.* An automorphism of a labelled object fixes $e_0,\dots,e_{10}$, hence acts on $M=f^*\Pic(S)$ as the identity. It need not act trivially on $H^2(X)$: $M$ is the invariant lattice and says nothing about the rank-$11$ complement. The covering involution $\iota$ is a nontrivial automorphism of every labelled object — it preserves each $e_i$, preserves the period, and acts as $-\id$ on $T_\Co$ (@prop:coble-transcendental) — so the isotropy of $\mcM^{\mathrm{lab}}_\Co$ contains $\theset{\id,\iota}\cong\ZZ/2$ at every object. It is finite, and $[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]$ is a Deligne--Mumford stack locally of finite type, but its isotropy is not trivial.
2. *The unlabelled stack does not.* The automorphism group of a Coble surface is $W_{10}(2)$, infinite and discrete (@rmk:coble-automorphisms-infinite(1)--(2)), so $\mcM_\Co$ has infinite isotropy, is not locally of finite type, and is not separated.
3. *The map between them.* The forgetful map $\mcM^{\mathrm{lab}}_\Co\to\mcM_\Co$ has, over a surface, the set of labellings as fibre: the orbit of the labelling under the group of automorphisms of the unlabelled object, which is infinite. So the map is not of finite type either, and it exhibits $\mcM_\Co$ as the quotient of the labelled stack by a group that acts with infinite orbits on the label.
4. *Which statements hold where.* Separatedness, quasi-compactness, local finite type and the Deligne--Mumford property hold for the labelled stack and for $[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]$; they fail for $\mcM_\Co$. A statement of any of them must name the stack, and the monodromy group $\Gamma_\Co$ is a group-theoretic statement that does not distinguish the two, because both stacks have the same coarse period quotient.

The disagreement is therefore not a mathematical contradiction: the two descriptions are of the marked and the unmarked stacks, and everything that the programme's items 3 and 4 prove is about the marked one.
:::

::: {.lemma #lem:period-stabiliser-finite title="The stabiliser of a period point in the orthogonal group of the lattice is finite"}

Let $T$ be a lattice of signature (@def:signature) $(2,n)$ and $P\subset T\tensor\RR$ a positive definite (@def:definiteness) $2$-plane (a point of $\bD(T)$). Then
$$
\Stab_{\Orth(T)}(P)=\theset{g\in\Orth(T)\mid g(P)=P}
$$
is finite.
:::

::: {.proof}

An isometry of $T$ acts on $T\tensor\RR$ preserving the form, and $\Orth(T)$ is a discrete subgroup of the Lie group (@def:group) $\Orth(T\tensor\RR)$: a neighbourhood of the identity in the latter contains no non-identity lattice isometry, because such an isometry would move some lattice vector by less than its length. An element of the stabiliser preserves $P$ and therefore its orthogonal complement $P^{\perp T\tensor\RR}$, which is negative definite (@def:definiteness) of dimension $n$; so the stabiliser maps to the compact group $\Orth(P)\times\Orth(P^{\perp})$, injectively, because an isometry fixing $P$ and $P^{\perp}$ pointwise is the identity. A discrete subgroup of a compact group is finite, and the stabiliser is closed in $\Orth(T)$, hence discrete. So it is finite.
:::

::: {.lemma #lem:relabelling-discriminant-action title="A relabelling acts on $T_\Co$ by the conjugate of the permutation, and never trivially"}

Let $M=\generators{e_0,\dots,e_{10}}=\pi^*\Pic(S_b)\cong\generators{2}\oplus\generators{-2}^{\oplus10}$ be the span of the eleven classes of @lem:d2-local-system(2) and $T_\Co=M^{\perp\lkt}$ (@lem:d2-local-system(3), @prop:coble-period-domain(1)--(2)), and let $\gamma\colon A_M\isoto A_{T_\Co}(-1)$ be the gluing isometry of @lem:coble-discriminant-actions-conjugate. Let $\sigma$ be a permutation of $e_1,\dots,e_{10}$ fixing $e_0$, read as an isometry of $M$, and let $\Theta=\gamma\bar\rho_M(\mathfrak S_{10})\gamma^{-1}\le\Orth(q_{T_\Co})$ be the group of @prop:gamma-co-geometric-bound(2). Then:

1. $[L_{\mathrm{K3}}:M\oplus T_\Co]=2^{11}$, and no isometry of $L_{\mathrm{K3}}$ restricts to $\sigma$ on $M$ and to the identity on $T_\Co$ unless $\sigma=\id$: the pair $(\sigma,\id_{T_\Co})$ is an isometry of the proper sublattice $M\oplus T_\Co$ which fails the compatibility condition of @cor:lifting-unimodular.
2. $\sigma$ does extend to an isometry $g_\sigma\in\Orth(\lkt)$, and the class of $\restrictionof{g_\sigma}{T_\Co}$ in $\Orth(T_\Co)/\widetilde\Orth(T_\Co)$ does not depend on the extension. The resulting map
$$\mathfrak S_{10}\too\Orth(T_\Co)/\widetilde\Orth(T_\Co)\iso\Orth(q_{T_\Co}),\qquad \sigma\longmapsto \gamma\,\bar\rho_M(\sigma)\,\gamma^{-1}$$
is an injective homomorphism with image $\Theta$; so $\abs{\Theta}=10!=3\,628\,800$.
3. The relabelling arrows of @lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(1) act on $T_\Co$ by isometries whose images in $\Orth(q_{T_\Co})$ are exactly the elements of $\Theta$; the arrow $b\to\sigma b$ is marked by $\sigma$ or by $\sigma^{-1}$ according to the product convention of @def:transport-and-monodromy, which @lem:d2-label-lift(2) fixes, and the set of images is the subgroup $\Theta$ either way. Hence $\bar\rho\qty(\Gamma_\Co(\bar B))=\Theta$ and $[\Gamma_\Co(\bar B):\Gamma_\Co(B)]=10!$ (@lem:gamma-co-labelled-index).
:::

::: {.proof}

1. By @prop:coble-period-domain(1) $M\cong S_\Co$ is $2$-elementary of signature $(1,10)$ with $A_M\cong(\ZZ/2)^{11}$, and by @prop:coble-period-domain(2) $T_\Co=M^{\perp\lkt}$ is $2$-elementary of signature $(2,9)$ with discriminant form $-q_M$; in particular $\abs{A_M}=\abs{A_{T_\Co}}=2^{11}$. The index-discriminant relation of @cons:embedding-gluing-data, applied with $L=L_{\mathrm{K3}}$ unimodular and $S=M$ primitive in it (@lem:d2-local-system(2)), reads $\abs{\disc{T_\Co}}=\abs{\disc{L_{\mathrm{K3}}}}\,\cardinality{H_j}^2/\abs{\disc M}$, that is $[L_{\mathrm{K3}}:M\oplus T_\Co]^2=\abs{A_M}\abs{A_{T_\Co}}=2^{22}$; so the index is $2^{11}$ and $M\oplus T_\Co\subsetneq L_{\mathrm{K3}}$. The pair $(\sigma,\id_{T_\Co})$ is an isometry of $M\oplus T_\Co$, and by @cor:lifting-unimodular it extends to $L_{\mathrm{K3}}$ exactly when $\bar\rho_{T_\Co}(\id_{T_\Co})=\gamma\bar\rho_M(\sigma)\gamma^{-1}$, that is exactly when $\bar\rho_M(\sigma)=\id$. That fails for every $\sigma\neq\id$: choose $i$ with $\sigma(i)\neq i$; then $\bar\rho_M(\sigma)[e_i/2]=[e_{\sigma(i)}/2]\neq[e_i/2]$, because $e_{\sigma(i)}-e_i$ has a coordinate equal to $1$ in the basis $e_0,\dots,e_{10}$ and so does not lie in $2M$ (@lem:coble-discriminant-actions-conjugate). In particular the sum $\sigma\oplus\id_{T_\Co}$ is an isometry of the proper sublattice $M\oplus T_\Co$ and not of $L_{\mathrm{K3}}$.

2. *Existence and independence.* $L_{\mathrm{K3}}$ is even unimodular, $M$ is primitive in it, nondegenerate of signature $(1,10)$, and $T_\Co$ is indefinite and $2$-elementary, so @cor:twoelementary-complement-lifting applies: every element of $\Orth(M)$ extends to an element of $\Orth(\lkt)$ preserving $M$, and the exact sequence displayed there, $1\too\widetilde\Orth(T_\Co)\too\Stab_{\Orth(\lkt)}(M)\xrightarrow{\ \res_M\ }\Orth(M)\too1$, says that two extensions of $\sigma$ differ by an element of $\widetilde\Orth(T_\Co)$. Hence the class of $\restrictionof{g_\sigma}{T_\Co}$ modulo $\widetilde\Orth(T_\Co)$ is well defined. *The class.* For an extension $g_\sigma$ preserving $M$ and $T_\Co$, @lem:coble-discriminant-actions-conjugate gives $\bar\rho_{T_\Co}\qty(\restrictionof{g_\sigma}{T_\Co})=\gamma\bar\rho_M(\sigma)\gamma^{-1}$, and $\bar\rho_{T_\Co}\colon\Orth(T_\Co)\too\Orth(q_{T_\Co})$ is onto with kernel $\widetilde\Orth(T_\Co)$ (@thm:two-elementary-surjectivity), which identifies the quotient with $\Orth(q_{T_\Co})$ and shows the map to be well defined as displayed. It is a homomorphism because $\bar\rho_M$ is one and $\gamma$ is an isometry, and it is injective because $\bar\rho_M(\sigma)\neq\id$ for $\sigma\neq\id$ by the coordinate argument of 1. Its image is $\Theta$ by the definition of $\Theta$ in @prop:gamma-co-geometric-bound(2), so $\abs{\Theta}=\abs{\mathfrak S_{10}}=10!$.

3. *The relabelling arrow.* Let $\psi_b,\psi_{\sigma b}\colon H^2(X_b,\ZZ)\isoto\lkt$ be the labelled markings at $b$ and at its relabelling, each carrying the classes of $E_0,\dots,E_{10}$ to $e_0,\dots,e_{10}$. Both are markings of one surface: a point of $\bar B$ is a sextic with its ten nodes as a set (@not:d2-plane-sextic-base), $b$ and $\sigma b$ have the same Coble surface and the same double cover, the class of the pullback of a line is the value of a global section and so is carried to $e_0$ by both, and the two differ only in which of $E_1,\dots,E_{10}$ is called $E_i$ (@lem:d2-local-system(2), (4)). So $\psi_b^{-1}(M)=\psi_{\sigma b}^{-1}(M)$ is one sublattice of $H^2(X_b)$; the relabelling arrow $b\to\sigma b$ is the pair $(\id_{S_b},\id_{X_b})$ (@lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(1)), so its transport on $\bV$ is the identity on $H^2(X_b)$, and its matrix in the two labelled frames is the isometry $\psi_{\sigma b}\psi_b^{-1}$ of $\lkt$, which fixes $e_0$ and permutes $e_1,\dots,e_{10}$. That is an extension of a permutation in the sense of 2, so the images of the relabelling arrows in $\Orth(q_{T_\Co})$ are the elements of $\Theta$. Which of $\sigma$ and $\sigma^{-1}$ marks the arrow $b\to\sigma b$ depends on the convention of @lem:d2-label-lift(2), where the group element of a composite is the product in the order opposite to traversal (@def:transport-and-monodromy); the set of classes is $\Theta$ either way, $\Theta$ being a subgroup, and the inverse of $\gamma\bar\rho_M(\sigma)\gamma^{-1}$ is $\gamma\bar\rho_M(\sigma^{-1})\gamma^{-1}$. *The generation.* The relabelling arrows are points of $R_B$, and the subgroup of $\pi_1(\mcM^{\mathrm{cl}}_\Co,P(s))$ that they generate together with $P_*\pi_1(B,s)$ is the image of $\pi_1(\bar B,[s])$ (@lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(3)); hence $\Theta\subseteq\bar\rho\qty(\Gamma_\Co(\bar B))$, and with $\bar\rho\qty(\Gamma_\Co(\bar B))\subseteq\Theta$ (@prop:gamma-co-geometric-bound(2)) the two are equal. The index is $[\Gamma_\Co(\bar B):\Gamma_\Co(B)]=\abs{\bar\rho\qty(\Gamma_\Co(\bar B))}$ (@lem:gamma-co-labelled-index(2)), that is $10!$.
:::

::: {.proposition #prop:gamma-co-from-the-labelled-stack title="$\Gamma_\Co$ assembled from the labelled stack: the exact sequence, the isotropy and the relabellings"}

Let $S_{10}$ act on the labelled stack $\mcM^{\mathrm{lab}}_\Co$ of @rmk:coble-labelled-versus-unlabelled by permuting the ten exceptional classes, and put $\mcM^{\mathrm{lab},S_{10}}_\Co\definedas\qty[\mcM^{\mathrm{lab}}_\Co/S_{10}]$; this is the quotient by the labelling alone. The stack $\mcM_\Co$ of @def:coble-moduli-functor is the further quotient by the plane-model groupoid (@prop:coble-plane-model-comparison(4), @prop:coble-stack-as-quotient), so
$$\mcM_\Co=\qty[\mcM^{\mathrm{lab},S_{10}}_\Co/G],\qquad G=\text{the plane-model groupoid},$$
and it is *not* $[\mcM^{\mathrm{lab}}_\Co/S_{10}]$: that intermediate quotient forgets the labellings but keeps the plane presentation fixed. The items below are asserted for the classical labelled base $B$ of @not:d2-plane-sextic-base, the base that @def:coble-family-unpolarized assigns to the family, whose $S_{10}$-torsor and connectedness are proved (@lem:d2-labelling-cover, @lem:d2-incidence-connected(3)); the identification of $\mcM^{\mathrm{lab}}_\Co$ with $B$ is research#797, item 6 (@def:gamma-co-groups(1)), and nothing here uses it.

1. *The sequence for the labelling.*
$$1\too\pi_1(B,s)\too\pi_1(\bar B,[s])\too S_{10}\too1$$
is exact (@lem:d2-label-lift(2), whose inputs are the principal $S_{10}$-bundle of @lem:d2-labelling-cover and the path connectedness of $B$). This is the sequence of the torsor $B\to\bar B=[B/S_{10}]$. The corresponding sequence for $\mcM^{\mathrm{lab}}_\Co\to\mcM^{\mathrm{lab},S_{10}}_\Co$ is *not* asserted: it needs an identification of the labelled stack $\mcM^{\mathrm{lab}}_\Co$ with the classical presentation $B$, which is research#797, item 6 (@def:gamma-co-groups(1)), and connectedness of $\mcM^{\mathrm{lab}}_\Co$ is not proved. The further quotient by the plane-model groupoid has infinite stabilisers and its own sequence, which is not written here either.
2. *The labelled part.* $\rho\qty(\pi_1(B,s))=\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$, this being @lem:d2a-monodromy-of-the-stack(3) with @thm:gamma-co-is-stable(1). The period-map presentation $[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]$ carries the same inclusion and not an equality: the equality is @qst:gamma-co-sign-is-realised, and it is open.
3. *The relabellings act on $T_\Co$, by the group $\Theta$ of discriminant classes.* A permutation of $e_1,\dots,e_{10}$ is an isometry $\sigma$ of $M=f^*\Pic(S)$ fixing $e_0$, and by @lem:relabelling-discriminant-action the relabelling it defines acts on $T_\Co$ by an isometry whose class in $\Orth(q_{T_\Co})$ is the conjugate $\gamma\bar\rho_M(\sigma)\gamma^{-1}$, or its inverse, according to which of $\sigma,\sigma^{-1}$ marks the arrow (@lem:d2-label-lift(2), @def:transport-and-monodromy); the set of these classes is $\Theta$ either way. No isometry of $L_{\mathrm{K3}}$ acts as $\sigma$ on $M$ and as the identity on $T_\Co$: $M\oplus T_\Co$ has index $2^{11}$ in $L_{\mathrm{K3}}$, so the sum $\sigma\oplus\id$ is an isometry of that proper sublattice and does not extend. The relabelling arrows therefore have discriminant image $\Theta\cong\mathfrak S_{10}$, of order $10!$, and the part they contribute to $\Gamma_\Co(\bar B)$ is all of it.
4. *The isotropy: what is proved, and the discordant step.* Let $g\in\Aut(S_b)$. It preserves $-2K_{S_b}$ and the unique member $C_b\in\abs{-2K_{S_b}}$ (@lem:d2-unpolarised-family(1)), hence the branch divisor of $\pi_b\colon X_b\to S_b$; the double cover is determined by its branch divisor (@lem:d2-unpolarised-family(2)), so $g$ lifts to an automorphism of $X_b$, uniquely up to $\iota_b$, and preserves the Hodge structure. Its image in $\Orth(T_\Co)$ therefore fixes the period $2$-plane $P\subset T_\Co\tensor\RR$ and lies in $\Stab_{\Orth(T_\Co)}(P)$, which is **finite** (@lem:period-stabiliser-finite); it contains the class of $\iota_b$, which is $-\id$ (@prop:coble-transcendental). For the group: write $\Aut(S_b)^*$ for the image of $\Aut(S_b)$ in $\Orth(\Pic(S_b))$. [@CD12, Thm. 3.5] gives that $\Aut(S_b)^*$ contains $W_{10}(2)$ when $S_b$ is unnodal, and [@CD12, Rem. 3.11] that the two are equal for a general Coble surface in moduli; both statements are about the image in $\Orth(\Pic S_b)$, and neither is a statement about $\Aut(S_b)$ itself without a faithfulness or section argument, which is not supplied here. What is *not* established either is the image of that finite group in the discriminant group, and the earlier form of this item deduced it from a step that does not work: $W_{10}(2)$ acts trivially on $E_{10}/2E_{10}$, but $\abs{E_{10}/2E_{10}}=2^{10}$ while $\abs{A_M}=2^{11}$, so the former is not a quotient of the latter and the triviality does not transport to $A_M$ through @lem:coble-discriminant-actions-conjugate; and [@CD12, Thm. 3.5, Rem. 3.11] give the equality $\Aut(S_b)^*=W_{10}(2)$ at a general member only. The image of the isotropy in $\Orth(q_{T_\Co})$ is left open, and (5) does not use it.
5. *Conclusion.* The subgroup generated by the labelled part and by the relabellings *is* $\Gamma_\Co(\bar B)$: that subgroup is the image of $\pi_1(\bar B,[s])$ (@lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(3), with @lem:d2-label-lift(2) for the sequence it sits in). By (2) and (3),
$$\bar\rho\qty(\Gamma_\Co(\bar B))=\Theta,\qquad [\Gamma_\Co(\bar B):\Gamma_\Co(B)]=\abs{\Theta}=10!,$$
so the relabelling half of the $\mathfrak S_{10}$ of @lem:d2-label-lift(2) is an additional generator of the discriminant image, not an element that contributes nothing, and it puts $\Gamma_\Co(\bar B)$ outside $\widetilde\Orth^+(T_\Co)$. The isotropy adds a finite subgroup of $\Orth(T_\Co)$ whose discriminant image is not computed (4). On the classical substack the monodromy group of $\bT$ is generated by $\Gamma_\Co(\bar B)$ and the transports of the arrows of the plane-model groupoid between distinct points of $\bar B$ (@prop:pi1-of-the-plane-model-quotient(4)); this reduction does not treat those transports, and that this group is $\Gamma_\Co$ of @def:gamma-co-groups(1) is research#797, item 6, which nothing here uses. **The equality $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ is @conj:gamma-co-stable and is not proved**; what is proved is the inclusion $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ of @thm:gamma-co-is-stable(1).
:::

::: {.proof}

(1) is @lem:d2-label-lift(2): the torsor of @lem:d2-labelling-cover is over a path connected $B$ (@lem:d2-incidence-connected(3)), and the sequence is that lemma's. Nothing is asserted for $\mcM^{\mathrm{lab}}_\Co$, whose identification with $B$ is research#797, item 6 (@def:gamma-co-groups(1)) and whose connectedness is not proved; the fibre-product computation of @lem:d2-labelling-cover is what makes the sequence available for the base it is made over.

(2) is @lem:d2a-monodromy-of-the-stack(3) with @def:gamma-co-groups(1): the monodromy group of the labelled presentation is $\rho(\pi_1(B,s))=\Gamma_\Co(B)$, and $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ is @thm:gamma-co-is-stable(1). The monodromy group of a quotient $[\Gamma\backslash D^+]$ is $\Gamma$, so reading the presentation $[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]$ as the labelled stack *is* the equality $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$, which is @qst:gamma-co-sign-is-realised and is not proved; what the presentation supplies is the inclusion.

(3) is @lem:relabelling-discriminant-action(1)--(3). The error of the earlier form of this item is worth naming, because it is the reason the item read the way it did: a relabelling *is* a change of marking and not an automorphism of the surface, and that is exactly why it moves $T_\Co$. The transport along the relabelling arrow is the identity on $H^2(X_b)$ in the frame of the surface, while the frame of the lattice $T_\Co$ is the labelled marking; changing the labelling changes that frame by $\psi_{\sigma b}\psi_b^{-1}$, whose restriction to $T_\Co$ is not the identity (@lem:relabelling-discriminant-action(3)). And $\sigma\oplus\id_{T_\Co}$ is an isometry of the proper sublattice $M\oplus T_\Co$ of index $2^{11}$, not of $L_{\mathrm{K3}}$ (@lem:relabelling-discriminant-action(1)). The surface's $H^2$ does not change; the monodromy group is a subgroup of $\Orth(T_\Co)$, and in it the frame change is the element.

(4) The lift and the finiteness are the argument displayed: what a $g\in\Aut(S_b)$ acts on is the double cover, because the branch divisor is preserved, and an isometry of $X_b$ preserving the Hodge structure fixes the period $2$-plane; @lem:period-stabiliser-finite is stated for a lattice of signature $(2,n)$ and a positive definite $2$-plane, which is $P\subset T_\Co\tensor\RR$ for $T_\Co$ of signature $(2,9)$ (@prop:coble-period-domain(2)). The two claims about the group are quoted from the numbered statements of [@CD12], and both are statements about $\Aut(S_b)^*$, the image in $\Orth(\Pic S_b)$: Theorem 3.5 for the containment at an unnodal member and Remark 3.11 for the equality at a general one. The discordant step is named in the statement: $E_{10}/2E_{10}$ has $2^{10}$ elements and $A_M$ has $2^{11}$, so no map between them carries the triviality of the $W_{10}(2)$-action on the first to the second, and @lem:coble-discriminant-actions-conjugate compares $A_M$ with $A_{T_\Co}$ and not with $E_{10}/2E_{10}$. Nothing below uses the image of the isotropy in $\Orth(q_{T_\Co})$.

(5) $\pi_1(\bar B,[s])$ is generated by the image of $\pi_1(B,s)$ and the classes $\lambda_\sigma$ of the relabelling arrows (@lem:d2-label-lift(2) with @lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(3)), so the subgroup those generate is $\rho\qty(\pi_1(\bar B,[s]))=\Gamma_\Co(\bar B)$; its part $P_*\pi_1(B,s)$ has image $\Gamma_\Co(B)\subseteq\ker\bar\rho$ (@thm:gamma-co-is-stable(1)) and its relabelling part has discriminant image all of $\Theta$ (3), whence $\bar\rho\qty(\Gamma_\Co(\bar B))=\Theta$ and the index is $\abs{\Theta}=10!$ (@lem:gamma-co-labelled-index(2)). That $\Theta\neq\theset{1}$ is what puts $\Gamma_\Co(\bar B)$ outside $\ker\bar\rho$, and @prop:gamma-co-geometric-bound(2) supplies the other inclusion. The isotropy is a different family of arrows — the points of $R_B$ with $b'=b$ — and it is not part of $\Gamma_\Co(\bar B)$; its image is finite (4) and is not computed. The generation of the monodromy group of the classical substack is @prop:pi1-of-the-plane-model-quotient(3)--(4); the identification of that group with $\Gamma_\Co$ of @def:gamma-co-groups(1) is research#797, item 6, and is not used.
:::

::: {.remark #rmk:universal-object-of-the-coble-stack title="The universal object over the stack, and why no family over a scheme presents it"}

Item 1 of research#797 asks for the universal family over the Coble stack, and item 2 for that over the partial compactification. Two different things are at stake.

1. *The universal object over the stack.* A moduli stack in groupoids carries the object given by its identity morphism, the tautological family over itself; so $\mcM_\Co$ and $\mcM^{\partial}_\En$ each carry a universal object, and this part is formal.
2. *A family over a scheme presenting it.* What an explicit construction supplies is a family over a scheme together with a smooth surjection from that scheme: the family of @lem:d2-unpolarised-family(2) over $V$, descending to $B$ and to $\bar B$. That map is essentially surjective onto the classical substack but not an equivalence (@prop:coble-plane-model-comparison(1)--(3)), and it is smooth by @prop:coble-stack-as-quotient, so the family over $\bar B$ **presents** the universal object of $\mcM^{\mathrm{cl}}_\Co$ as a presentation; it is not a universal family over a scheme in the sense of representing the functor. The family is not essentially surjective onto the wider class: every object is a blow-up of $\PP^2$ at the ten double points of an irreducible rational sextic (@thm:coble-smooth-antibicanonical-is-a-plane-blowup), and the objects in the image of this family form an open dense substack that omits $S_{Z_8}$ (@thm:coble-classical-substack-is-open-dense-and-proper). What also remains open is whether some other scheme — necessarily not one dominating $\bar B$ in the plane-model direction — carries a family representing the restricted functor on an open substack, and no such scheme is constructed in the volume.
3. *The Enriques locus.* Over the Enriques part of $\mcM^{\partial}_\En$ no presentation by a family of K3 surfaces with a fixed-point-free involution is constructed here; the period-domain description of [@DK13, §3] and the quotient presentation of item 3 of the programme are the routes, and neither is written.
:::

::: {.remark #rmk:coble-enriques-not-a-map title="There is no morphism from the Coble stack to the Enriques stack of smooth families"}

Item 2 of research#797 asks for a morphism $\text{Coble}\to\text{Enriques}$. Between the moduli of *smooth* families there is none, and the relation the sources give is a boundary one: the moduli space of Coble surfaces is identified with a **codimension-one component of the boundary** of the moduli space of Enriques surfaces [@DK13, §1]. The reason is in the objects: a Coble surface is the quotient $X/\iota$ of a K3 surface by an involution with a fixed curve, while an Enriques surface is the quotient by a fixed-point-free one; a family of the first kind does not become a family of the second by any map of bases, and the Coble locus is reached only in the limit in which the branch curve of $X/\iota$ is contracted — which is the degeneration [@DK13, §1] and [@DK13, §3] describe.

What does exist as a morphism of stacks is the map to the $\mathrm{K3}$-with-involution moduli, $\mcM_\Co\to\mathfrak{Inv}$, which is fully faithful onto an explicitly described image (@lem:d0-coble-stack-in-involution-stack). The comparison with Enriques goes through that stack and the involution $I_\En$ rather than through a map of bases, and it is the comparison this programme's item 2 asks for only after the reduction: the correct statement is that the Coble moduli is a boundary stratum of the Enriques moduli, not the source of a morphism between them.
:::

::: {.lemma #lem:cremona-second-plane-model-general title="A second plane model by quadratic Cremona on a nonempty open locus"}
There is a nonempty open subset $V^\circ\subset V$ of the base of @not:d2-plane-sextic-base such that for every $(Z;p_1,\dots,p_{10})\in V^\circ$, after relabelling the first three nodes, the following hold. The points $p_1,p_2,p_3$ are not collinear, no fourth node lies on a line $L_{ij}=\overline{p_ip_j}$ with $1\le i<j\le3$, and for every such line
$$
i(Z,L_{ij};p_i)=i(Z,L_{ij};p_j)=2,
$$
while its two remaining intersection points with $Z$ are simple, distinct, and disjoint from $p_1,p_2,p_3$.

For such a point put $S=\Bl_{p_1,\dots,p_{10}}\PP^2$ and let $q$ be the standard quadratic Cremona involution with fundamental points $p_1,p_2,p_3$. Then $q$ lifts to an isomorphism from $S$ to the blowup of $\PP^2$ at ten points, with line class and ten exceptional classes
$$
A=2H-E_1-E_2-E_3,\qquad
G_{12}=H-E_1-E_2,\quad G_{13}=H-E_1-E_3,\quad G_{23}=H-E_2-E_3,\quad G_k=E_k\ (4\le k\le10).
$$
The three $G_{ij}$ are the strict transforms of the $L_{ij}$, smooth disjoint $(-1)$-curves. The strict transform of $q(Z)$ is $-2K_S$, and $q(Z)$ is an irreducible sextic with exactly ten ordinary double points. In particular, $q$ gives a second plane presentation of the same classical Coble surface, and $3A-\tsum_{i<j}G_{ij}-\tsum_{k\ge4}G_k=-K_S$.
:::

::: {.proof}

*The nonempty good locus.* Collinearity is the vanishing of a determinant, tangency at a base node is failure of the join restriction to split off exactly a double factor there, and failure of the residual intersection to be reduced is vanishing of its discriminant. These are closed algebraic conditions on the integral parameter family of rational sextics, so their complement is open. The computation `computations/reports/coble_799-cremona-general-point.py`, recorded in `computations/reports/coble_799-cremona-general-point-run.txt`, exhibits an integral regular birational parametrization whose image after reduction modulo $101$ satisfies all their complements simultaneously. It computes a squarefree zero-dimensional Jacobian algebra of vector-space dimension $10$, hence ten geometric ordinary double points; the rational parametrization forces any further singularity to raise the total $\delta$-invariant above the arithmetic-genus deficit $10$, so there is none. At three actual nodes in the splitting field, it checks noncollinearity, excludes every other node on the three joins, and divides each join restriction twice by each endpoint before checking that its residual quadratic has nonzero discriminant. The special fibre therefore lies in the open good locus. If the characteristic-zero good locus were empty, the complementary closed locus would contain the generic characteristic-zero point and hence every integral special fibre after almost every reduction, against the exhibited fibre at $101$. Thus the good locus is nonempty in characteristic zero. No density or irreducibility statement for the labelled base is needed: $V^\circ$ is this nonempty open subset, and an arbitrary member of $V$ need not belong to it.

*The lifted isomorphism.* After a projective change of coordinates the map is $q([x:y:z])=[yz:xz:xy]$. The closure of its graph is the blowup at the three coordinate vertices, and the second projection contracts the strict transforms of the three coordinate lines: in each standard chart the graph equations are those of the blowup, and gluing the charts proves both assertions. Because no other $p_k$ lies on a fundamental line, blowing up those seven points as well gives the displayed lift to $S$, with $A$ the line class of the target and the ten $G$'s its exceptional curves. Each $G_{ij}$ is the strict transform of a line through two blown-up points, hence a smooth rational curve with $G_{ij}^2=1-1-1=-1$; two of them meet only above a fundamental point and their strict transforms are disjoint. For $k\ge4$, $G_k=E_k$ is disjoint from the three line curves. Thus all ten $G$'s are disjoint smooth $(-1)$-curves. Intersections with $A$ and expansion in the original frame give $A^2=1$, $A\cdot G=0$ for every $G$, and
$$3A-\tsum_{i<j}G_{ij}-\tsum_{k\ge4}G_k=3H-\tsum_{i=1}^{10}E_i=-K_S.$$

*Nodality of the image.* Let $C\subset S$ be the strict transform of $Z$, smooth because every singularity of $Z$ is an ordinary double point. For an old exceptional curve $E_i$, the two distinct tangent directions at the node give two simple points of $C\cap E_i$. For $G_{ij}$, Bézout and removal of the two base points give $C\cdot G_{ij}=2$; the general-position condition makes these two intersection points simple and distinct, and puts them away from every old exceptional curve. Blowing down the ten disjoint curves $G$ therefore gives ten distinct points. At each point the two simple intersections give two smooth branches whose tangent directions correspond to the two distinct points on the contracted exceptional curve, so the image has an ordinary double point. Away from the contracted curves the blowdown is an isomorphism and creates no further singularity. The image is irreducible because $C$ is, its degree is $A\cdot C=-2K_S\cdot A=6$, and the class calculation just displayed identifies $[C]$ with $-2K_S$ in both frames. This proves the second plane presentation.
:::

::: {.proposition #prop:coble-plane-model-comparison title="The map from $\bar B$ to $\mcM_\Co$: the classical substack in its essential image, not full, not injective"}

Let $\bar B=[B/S_{10}]$ be the unlabelled base of @def:coble-family-unpolarized(2) and let $\varphi\colon\bar B\to\mcM_\Co$ send a labelled ten-nodal sextic to the Coble surface it defines with its K3 double cover (@def:coble-moduli-functor).

1. $\varphi$ has the classical substack in its essential image: every object of $\mcM^{\mathrm{cl}}_\Co$ of @prop:coble-stack-as-quotient is, on a connected component of its base, of that form (@lem:d2-unpolarised-family(1)), and the ten nodes determine the sextic in a fixed plane (@rmk:d2-what-is-open(2)). The essential image is not the whole of $\mcM_\Co$: it is the open dense substack $\mcM^{\mathrm{cl}}_\Co$, which omits the object $S_{Z_8}$ (@thm:coble-classical-substack-is-open-dense-and-proper).
2. $\varphi$ is not full: at **every** irreducible ten-nodal sextic there is an automorphism of the associated Coble surface induced by no projectivity, namely the Bertini involution of any eight of the ten nodes [@Pie26, Prop. 59], whose action sends the line class to $17H-6\tsum_{i\le8}E_i$, a class of square $1$ with $H\cdot\sigma^*H=17$.
3. $\varphi$ is not injective on isomorphism classes: at a general point of $V$ the quadratic Cremona involution centred at three nodes presents $S$ again with line class $A=2H-E_1-E_2-E_3$, whose exceptional curves are $H-E_1-E_2$, $H-E_1-E_3$, $H-E_2-E_3$, $E_4,\dots,E_{10}$; there $3A-\tsum_kG_k=-K_S$ and $A\cdot(-2K_S)=6$, and the plane branch curve is again an irreducible ten-nodal sextic, different from $Z$ because $A\neq H$ (@lem:cremona-second-plane-model-general).
4. Hence, on the classical substack, $\mcM^{\mathrm{cl}}_\Co$ is the quotient of $\bar B$ by the *plane-model equivalence*, the equivalence on plane presentations generated by the Cremona transformations carrying one ten-nodal plane model of $S$ to another, and is not equivalent to $\bar B$; by @thm:coble-classical-substack-is-open-dense-and-proper the stack $\mcM_\Co$ contains this quotient as an open dense substack. What that means for the monodromy of @def:coble-moduli-functor is item 6 of research#797, not a change of definition: $\Gamma_\Co$ is the monodromy of the variation of Hodge structure on the universal family over $\mcM_\Co$, write $\Gamma_\Co(B)\definedas\rho\qty{\pi_1(B,s)}$ (@def:gamma-co-groups(1)) for the group computed over the plane presentations; it is a group that item 6 must compare with $\Gamma_\Co$.
:::

::: {.proof}

(1) The objects of the classical substack have, by the first clause of @def:coble-moduli-functor together with the plane model that defines the substack, geometric fibres of the form $\Bl_{p_1,\dots,p_{10}}\PP^2$, which are the fibres of @lem:d2-unpolarised-family(1); the ten points are the nodes of the unique member of $\abs{-2K_S}$, by the Bézout count inside @lem:d2-unpolarised-family(1) (two distinct sextics through them with multiplicity two would meet in $36<40$), so the sextic is recovered from the surface and a plane model. This is the assertion of @rmk:d2-what-is-open(2), which the count settles.

(2) [@Pie26, Prop. 59] states that the Bertini involution associated with eight of the ten double points of a reduced sextic fixes the remaining two, hence lifts to $S=\Bl_{10}\PP^2$. Write $Y=\Bl_8\PP^2$ for the blowup at the eight, so that $K_Y=K_S-E_9-E_{10}$ and $\sigma^*(E_i)=-2K_Y-E_i$ for $i\le8$ while $\sigma^*(E_9+E_{10})=E_9+E_{10}$; then, from $H=\tfrac13\qty(\tsum_{i\le10}E_i-K_S)$,
$$\sigma^*(H)=\tfrac13\qty(\tsum_{i\le8}(-2K_Y-E_i)+E_9+E_{10}-K_S)=17H-6\tsum_{i\le8}E_i,$$
of square $17^2-36\cdot8=1$. Since $H\cdot\sigma^*H=17\neq1=H^2$, the class $H$ is not preserved. An automorphism induced by a projectivity preserves $H$, because $H$ is the pullback of $\OO_{\PP^2}(1)$; so $\sigma$ is induced by none, and $\operatorname{Aut}(S)$ strictly contains the projectivity stabiliser of $Z$ at every ten-nodal $Z$.

(3) At one general point the geometric realization is @lem:cremona-second-plane-model-general: the three line classes and the seven unchanged exceptional classes are actual pairwise disjoint smooth $(-1)$-curves, their contraction gives $S$ a plane model with line class $A$, and the transformed branch sextic has exactly ten ordinary double points. The numerical companion `computations/reports/coble_797-plane-models.py`, recorded in `computations/reports/coble_797-plane-models-run.txt`, checks $A^2=1$, $A\cdot G_k=0$, $A\cdot(-2K_S)=6$ and $3A-\tsum_kG_k=-K_S$ over $\ZZ$; those identities are not used as a substitute for the curve and singularity argument. A single such point already proves noninjectivity, and the relabelling arrows move the first three labels to any other triple.

(4) is (1)--(3) read as a statement about the fibres of $\varphi$; the last clause names the group of @def:coble-family-unpolarized, whose base is a presentation rather than the stack.
:::

::: {.lemma #lem:coble-automorphism-group-is-infinite title="The automorphism group of a ten-nodal Coble surface is infinite"}
Let $S=\Bl_{p_1,\dots,p_{10}}\PP^2$ be the surface of @lem:d2-unpolarised-family(1) at an irreducible ten-nodal sextic $Z$, with $\Pic(S)=\ZZ\generators{H,E_1,\dots,E_{10}}$ of squares $(1,-1,\dots,-1)$ and $K_S=-3H+\tsum_iE_i$. For $I\subset\theset{1,\dots,10}$ with $\abs I=8$, let $\{a,b\}$ be its complement and let $\sigma_I$ be the Bertini involution of the eight nodes $I$, an automorphism of $S$ induced by no projectivity (@prop:coble-plane-model-comparison(2)). Then:

1. The action of $\sigma_I$ on $\Pic(S)$ is
$$\sigma_I^*(H)=17H-6\tsum_{i\in I}E_i,\qquad \sigma_I^*(E_i)=6H-3E_i-2\tsum_{j\in I,\ j\neq i}E_j\quad(i\in I),\qquad \sigma_I^*(E_a)=E_a,\quad \sigma_I^*(E_b)=E_b,$$
and each of the $45$ matrices is an isometry of $\Pic(S)$ and an involution.
2. For $I=\theset{1,\dots,8}$ and $J=\theset{1,2,3,4,5,6,9,10}$ the product $\sigma_I^*\sigma_J^*$ has characteristic polynomial
$$(t-1)^7(t+1)^2(t^2-14t+1),$$
whose quadratic factor is irreducible over $\QQ$ with roots $7\pm4\sqrt3$, neither of which is a root of unity; so $\sigma_I^*\sigma_J^*$ has infinite order.
3. Hence the image of $\operatorname{Aut}(S)$ in $\Orth(\Pic(S))$ is infinite, and $\operatorname{Aut}(S)$ is infinite.
:::

::: {.proof}

1. The image of $H$ is @prop:coble-plane-model-comparison(2), which cites [@Pie26, Prop. 59]. For the rest, [@CD12, Thm. 3.5 and its proof] display the involution $\tau$ of a Coble surface as $\tau^*=\id_U\oplus\qty(-\id_{E_8})$ on $K_S^{\perp}=\generators{f_a,f_b}\perp E_8$, the first summand being a hyperbolic plane $U$, where $f_j=E_j-K_S$ is the class of the cubic through the nine nodes other than $p_j$; that is, $\tau$ fixes $K_S$, $f_a$, $f_b$ and acts as $-1$ on their orthogonal complement $W$ in $K_S^{\perp}$. Write $x=x_\parallel+x_\perp$ in $\langle K_S,f_a,f_b\rangle\oplus W$ and use $K_S\cdot K_S=-1$, $K_S\cdot f_j=0$, $f_a\cdot f_b=1$, $E_i\cdot K_S=-1$, $E_i\cdot f_a=E_i\cdot f_b=1$: then $H=3K_S+3f_a+3f_b+u$ and $E_i=K_S+f_a+f_b+w$ with $u,w\in W$, and $\tau^*(x)=2x_\parallel-x$ gives
$$\tau^*(H)=17H-6\tsum_{i\in I}E_i,\qquad \tau^*(E_i)=2\qty(E_a+E_b-K_S)-E_i=6H-3E_i-2\tsum_{j\in I,\ j\neq i}E_j,$$
while $E_a=f_a+K_S$ and $E_b=f_b+K_S$ are fixed. That $\tau=\sigma_I$ is [@Pie26, Prop. 59], and the value on $H$ is the one proved independently in @prop:coble-plane-model-comparison(2), which is the check that this action is the action of the family and not only of the abstract lattice. The eigenspace condition is what pins the action: without it the exponents $(-3,-2,\dots,-2)$ on $I$ may be permuted by an involution of $I$, and that permutation is not the one realized.
2. Direct computation over $\ZZ$: `computations/reports/coble_797-bertini-infinite-order.py`, whose record is `computations/reports/coble_797-bertini-infinite-order-run.txt`. It checks all $45$ matrices for the isometry and involution conditions and for the $H$-image of @prop:coble-plane-model-comparison(2), and it computes the characteristic polynomial of the stated product. A matrix of finite order has a cyclotomic characteristic polynomial; $t^2-14t+1$ is irreducible over $\QQ$ with roots $7\pm4\sqrt3$, and a real root of unity is $\pm1$, where the factor takes the values $-12$ and $16$. So the product has infinite order.
3. The two involutions are automorphisms of $S$ (@prop:coble-plane-model-comparison(2)), so their product lies in the image of $\operatorname{Aut}(S)$ in $\Orth(\Pic(S))$, which is therefore infinite; the kernel of that map is irrelevant to the conclusion, and no injectivity is used. The argument is lattice-theoretic and does not vary with the sextic: every irreducible ten-nodal sextic carries the same $45$ involutions.
:::

::: {.definition #def:coble-family-unpolarized title="D2a: the family of unpolarized Coble surfaces" defines="$\Gamma_\Co$; $\fco$"}

A *Coble surface* is a nonsingular projective rational surface $S$ with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}\neq\emptyset$ [@DZ99, Introduction; @DK13, §3].

**The objects.** Over a complex space $Y$, an object is a flat projective family $\mcs\to Y$ of classical Coble surfaces: a morphism whose geometric fibres are the surfaces $S=\Bl_{p_1,\dots,p_{10}}\PP^2$ for $(Z;p_1,\dots,p_{10})\in V$ of @not:d2-plane-sextic-base, together with the relative double cover $\mcx\to\mcs$ branched along the relative divisor $-2K_{\mcs/Y}$ and the covering involution $\iota$. Morphisms are Cartesian squares commuting with $\iota$.
A Coble surface is rational, so $h^{2,0}=0$ on every fibre and the degree-$2$ Hodge structure of $\mcs$ is of type $(1,1)$ throughout; the variation of Hodge structure on which the monodromy acts is that of the K3 *covers*, which is the local system of the next item.

**The bases** are three, and the choice among them is part of the definition; the family is the same over the space $B$ and the stack $\bar B$, and there is no family over the coarse space $M_\Co$.

1. *The coarse space.* $M_\Co=U/\PGL_3$ of @not:d2-plane-sextic-base, the moduli space of [@DK13, §3] (@prop:coble-moduli-git). It is a coarse space and carries no family: a Coble surface whose automorphism group (@def:endomorphism-monoid) acts nontrivially on $T_\Co$ has none. Statements about the monodromy group of a presentation are therefore not statements about base 1.
2. *The unlabelled base.* the quotient stack $\bar B=[B/S_{10}]=[V/(\SL_3\times S_{10})]$ of @not:d2-plane-sextic-base, whose coarse space is the space $V/(\SL_3\times S_{10})$ and whose points are irreducible ten-nodal sextics without names for the nodes, with monodromy group (@def:transport-and-monodromy) $\Gamma_\Co(\bar B)\supseteq\Gamma_\Co(B)$ (@lem:d2-local-system(4)).
3. *The labelled base.* the space $B=V/\PGL_3$ of @not:d2-plane-sextic-base, whose points are sextics with the ten nodes named, up to projectivity. This is the base whose monodromy group is $\Gamma_\Co(B)=\rho(\pi_1(B,s))$; whether that group is $\Gamma_\Co$ is research#797, item 6.



**The local system of lattices** is $\bT$ of @lem:d2-local-system: the orthogonal complement in $R^2f_*\underline{\ZZ}_{\mcx}$ modulo torsion of the span of the classes of the pullback of a line and of the ten exceptional curves. Its fibre is $T_\Co$, its rank is $11$, and its stalks (@def:stalk) have signature $(2,9)$.

**The group.** $\Gamma_\Co\leq\Orth(T_\Co)$ is the monodromy group (@def:transport-and-monodromy) of $\bT$ (@lem:d2-local-system) over the moduli stack $\mcM_\Co$ of @def:coble-moduli-functor, that is the image of the monodromy representation (@def:transport-and-monodromy) of $\bT$ (@def:local-system-of-lattices) on $\pi_1(\mcM_\Co)$. The group of the labelled base is $\Gamma_\Co(B)=\rho(\pi_1(B,s))$, and the identification $\Gamma_\Co=\Gamma_\Co(B)$ of the group of the stack with that of the presentation is research#797, item 6; it is open, and no statement on this page uses it except as hypothesis (A4) of @thm:gamma-co-is-the-stack-monodromy. Put $\fco\definedas\bD(T_\Co)/\Gamma_\Co$.
:::

::: {.lemma #lem:d2-unpolarised-family title="The family over the labelled base exists"}

Let $b=(Z;p_1,\dots,p_{10})\in V$ and $S_b=\Bl_{p_1,\dots,p_{10}}\PP^2$, with $H$ the class of the pullback of a line and $E_1,\dots,E_{10}$ the classes of the exceptional curves.

1. $S_b$ is a Coble surface, $[C_b]=-2K_{S_b}=6H-\sum_{i=1}^{10}2E_i$ for $C_b\subset S_b$ the proper transform (@def:strict-transform) of $Z$, $C_b^2=-4$, $\abs{-2K_{S_b}}=\{C_b\}$, that is $h^0(-2K_{S_b})=1$, and the double cover $\pi_b\colon X_b\to S_b$ branched along $C_b$ is a K3 surface with a covering involution $\iota_b$.
2. Over $V$ there are: the universal sextic $Z_V\subset\PP^2_V$, ten disjoint sections $\sigma_1,\dots,\sigma_{10}$ given by the $p_i$, the blowup $q\colon\mcs_V\definedas\Bl_{\sigma_1,\dots,\sigma_{10}}\PP^2_V\to V$, the exceptional divisors $\mcE_1,\dots,\mcE_{10}$, the pullback $\mcH$ of $\OO_{\PP^2}(1)$, and the proper transform $\mcC_V$ of $Z_V$. The morphism $\mcs_V\to V$ is smooth, projective and flat with fibre $S_b$, the divisor $\mcC_V$ is a Cartier divisor with $\mcC_V=-2K_{\mcs_V/V}$, and $\OO(\mcC_V)=\OO(2\mcD_V)$ for $\mcD_V\definedas3\mcH-\sum_i\mcE_i$. Hence the cyclic double cover $\mcx_V\to\mcs_V$ branched along $\mcC_V$ exists, is smooth and projective over $V$, and has fibre $X_b$; its covering involution $\iota_V$ restricts to $\iota_b$.
3. The morphisms and divisors of 2. are $\SL_3$-equivariant for the action on $V$ of @not:d2-plane-sextic-base, and the $S_{10}$-action of that notation, which permutes $\sigma_1,\dots,\sigma_{10}$ and commutes (@def:commutative-diagram) with $\SL_3$, sends $\mcE_i$ to $\mcE_{\sigma^{-1}(i)}$ and $\mcH$ to $\mcH$, the pushforward $\sigma_*\mcE_i=\mcE_{\sigma^{-1}(i)}$, which is the action on the points $(\sigma b)_j=b_{\sigma(j)}$ of the proof of @lem:d2-labelling-cover read on the classes; hence they define the same data over the space $B=V/\PGL_3$ (@lem:d2-plane-sextic-freeness(3)) and over the quotient stack $\bar B=[B/S_{10}]$, the labelled and unlabelled bases of @not:d2-plane-sextic-base.
:::

::: {.proof}

(1) $S_b$ is nonsingular, projective and rational. The class $-K_{S_b}=3H-\sum_iE_i$ has no effective representative: if $D$ were an effective divisor of that class, then $D$ is not a component of $Z$ (a curve of degree (@def:graded-object) $3$ is not a sextic), so $Z\cdot D$ is defined and is at least $\sum_i2\operatorname{mult}_{p_i}D\ge20$, while $Z\cdot D = 6\cdot3=18$ by Bézout; so $\abs{-K_{S_b}}=\emptyset$. And $\abs{-2K_{S_b}}\ni C_b\neq\emptyset$ because $[C_b]=6H-2\sum_iE_i=-2K_{S_b}$. So $S_b$ is a Coble surface in the sense of [@DZ99, Introduction]. $C_b$ is the proper transform of the irreducible curve $Z$, hence irreducible, and $C_b^2=36-4\cdot10=-4$. The double cover branched along $C_b$ is a K3 surface with a covering involution: it is smooth because $C_b$ is, and its canonical class is $\pi_b^*(K_{S_b}+\tfrac12C_b)=0$, so it is a K3 surface, as in [@DK13, §3]. And $\abs{-2K_{S_b}}=\{C_b\}$: a section of $\OO_{S_b}(6H-2\sum_iE_i)$ is a plane sextic $Z'$ with $\operatorname{mult}_{p_i}Z'\ge2$ at each $i$, and if $Z'\neq Z$ then $Z\cdot Z'=36$ by Bézout while the ten points contribute intersection multiplicity at least $4$ each, that is at least $40$, a contradiction; so $Z'=Z$, the class $-2K_{S_b}$ has the single effective divisor $C_b$, and $h^0(-2K_{S_b})=1$.

(2) The ten sections are disjoint because the $p_i$ are distinct, so their union is a closed submanifold of $\PP^2_V$ and its blowup $q$ exists and is smooth and projective over $V$; blowing up a smooth centre commuting with a smooth morphism preserves smoothness of the morphism, so $\mcs_V\to V$ is smooth, and its fibre at $b$ is $S_b$ by construction. On the fibre the proper transform of $Z_b$ has class $6H-2\sum_iE_i$, which is $-2K_{S_b}$ by (1), and $K_{\mcs_V/V}=-3\mcH+\sum_i\mcE_i$ by the blowup formula; so $\mcC_V=-2K_{\mcs_V/V}$. The line bundle $\OO(\mcD_V)$ satisfies $\OO(\mcD_V)^{\tensor2}=\OO(\mcC_V)$, so $\mcC_V$ is $2$-divisible in $\Pic(\mcs_V)$, and a $2$-divisible Cartier divisor on a smooth family is the branch divisor of a cyclic double cover [@EV92, §3, Chapter I]; the total space is smooth because $\mcC_V$ is, and it is projective over $V$ because $\OO(\mcD_V)$ is relatively ample after twisting by $q^*\OO(1)$.

(3) Each of $Z_V$, $\sigma_i$, $\mcH$, $\mcE_i$ and $\mcC_V$ is carried to itself or to its translate by an element of $\SL_3$, because $Z_V$ is the universal sextic over the linear system on which $\SL_3$ acts and the $\sigma_i$ are the coordinate sections; so the data are $\SL_3$-equivariant, and, the action of $\PGL_3$ on $V$ being free with quotient $B$ (@lem:d2-plane-sextic-freeness(3)), descend to $B$.
:::

::: {.lemma #lem:d2a-moduli-stack title="The quotient stack is the moduli stack of D2a"}

The stack $[V/\SL_3]$ is the moduli stack of the objects of @def:coble-family-unpolarized, with universal family (@def:classifying-object) that of @lem:d2-unpolarised-family(3).
:::

::: {.proof}

A point of $V$ is a labelling of the ten nodes of an irreducible sextic, two such labelings of the same sextic differ by an element of $S_{10}$ (@lem:d2-labelling-cover), and the isomorphisms (@def:isomorphism-of-objects) of the surfaces $S_b$ are those induced by the projectivities carrying one sextic to the other, that is by $\PGL_3$ (the scalars act trivially on $V$ and on the surfaces).
:::

::: {.remark #rmk:d2a-family-over-the-bases title="The family and the local system over the bases of D2a"}

Over the labelled base and the unlabelled base of @def:coble-family-unpolarized the family is that of @lem:d2-unpolarised-family(3) and the local system is that of @lem:d2-local-system; the eleven classes of @lem:d2-local-system(2) are $\SL_3$-invariant global sections over $V$, hence descend to $B$.
The family over $B$ is the descent of @lem:d2-unpolarised-family(2) along the principal bundle $V\to B$ (@lem:d2-labelled-base-monodromy), and its local system is @lem:d2-local-system.

The fibres are the surfaces $S_b=\Bl_{p_1,\dots,p_{10}}\PP^2$ for $b=(Z;p_1,\dots,p_{10})$, with $C_b$ the proper transform (@def:strict-transform) of $Z$; then $[C_b]=-2K_{S_b}$, $C_b^2=-4$, and the double cover of $S_b$ branched along $C_b$ is a K3 surface $X_b$ with covering involution $\iota_b$ (@lem:d2-unpolarised-family(1)).
The labelling of the ten exceptional curves is not part of the objects: the labelled base $B=V/\PGL_3$ is the space of sextics with their ten nodes *named* (@not:d2-plane-sextic-base), and the objects over the unlabelled base $\bar B$ are unlabelled (@lem:d2-labelling-cover).
By @lem:d2-labelled-base-monodromy the group $\Gamma_\Co(B)$ of the presentation is also $\rho\qty{\pi_1(V,s)}$; that it is $\Gamma_\Co$ of @def:coble-family-unpolarized is the comparison of the presentation with the stack, research#797, item 6, and is not used. It is a subgroup of $\Orth(T_\Co)$ because $\bT$ is a local system of lattices with fibre $T_\Co$ and transport along a path (@def:path-connectedness) is an isometry (@prop:local-system-of-lattices-monodromy).
:::

::: {.lemma #lem:coble-family-base-change title="Base change changes the monodromy group by a subgroup"}

Let $p\colon B'\to B$ be a continuous map of arcwise connected, locally simply connected spaces, let $(\bL,\beta)$ be a local system of lattices (@def:local-system-of-lattices) on $B$, and let $s'\in B'$ with $p(s')=s$.
Then the monodromy group (@def:transport-and-monodromy) of $p^{-1}\bL$ is $\rho\qty{p_*\pi_1(B',s')}$, the image in $\Aut(\bL_s,\beta_s)$ of the subgroup $p_*\pi_1(B',s')$ of $\pi_1(B,s)$.
In particular it is contained in the monodromy group (@def:transport-and-monodromy) of $\bL$, and if $p$ is a covering of finite degree (@def:graded-object) then it has finite index (@def:index) in it.
:::

::: {.proof}

The pullback $p^{-1}\bL$ has stalk (@def:stalk) $\bL_{p(s')}$ at $s'$, and transport along a path (@def:path-connectedness) $\gamma$ in $B'$ is transport along $p\circ\gamma$ in $B$: both are computed on sections over the interval, and $p$ carries a trivializing open set of $\bL$ to an open set on which $p^{-1}\bL$ is trivial.
So the monodromy representation of $p^{-1}\bL$ is $\rho\circ p_*$ (@def:transport-and-monodromy).
The remaining statements are those of the image of a subgroup under a group morphism, and, for a covering of finite degree, of the finite index of $\pi_1(B',s')$ in $\pi_1(B,s)$.
:::

::: {.lemma #lem:d2-local-system title="The local system of lattices, and its monodromy group"}

Let $\mcx\to\mcs\to B$ be the family of @lem:d2-unpolarised-family(3).

1. $\bV\definedas R^2f_*\underline{\ZZ}_\mcx$ modulo torsion is a local system of lattices with the cup product (@prop:primitive-cohomology-vhs(1)), of rank $22$ and signature $(3,19)$.
2. The classes $\varepsilon_0$ of $\mcH$, and $\varepsilon_1,\dots,\varepsilon_{10}$ of $\mcE_1,\dots,\mcE_{10}$, are values of global sections of $\bV$, and their span $\bM$ is a local system of lattices with fibre $M=\generators{2}\oplus\generators{-2}^{\oplus10}\cong S_\Co$, primitive (@def:primitive-embedding) in $\bV$ and of signature $(1,10)$ (@prop:coble-is-the-ten-nodal-sextic-type).
3. $\bT\definedas\bM^{\perp\bV}$ is a local system of lattices with fibre $T_\Co=M^{\perp\lkt}\cong\generators{2}\oplus E(2)$ (@prop:coble-period-domain(2), [@DK13, (3.6)]), of rank $11$ and signature $(2,9)$.
4. On $\bar B$ the same construction gives a local system of lattices $\bT_{\bar B}$ with fibre $T_\Co$ and monodromy group $\Gamma_\Co(\bar B)$, and $\Gamma_\Co(B)\subseteq\Gamma_\Co(\bar B)$ because $\bT_{\bar B}|_B=\bT$; the classes $\varepsilon_i$ are permuted by the elements of $S_{10}$ and fixed by no other generator. No containment involving $\Gamma_\Co$ is asserted here: $\Gamma_\Co$ is the monodromy group of the universal family over $\mcM_\Co$, and $\Gamma_\Co\subseteq\Gamma_\Co(\bar B)$ would follow from $\Gamma_\Co=\Gamma_\Co(B)$, which is research#797, item 6 and is not proved (@def:gamma-co-groups(1); see also @thm:gamma-co-sextic-group(4)).
:::

::: {.proof}

(1) is [@prop:primitive-cohomology-vhs(1)], the fibres being K3 surfaces by @lem:d2-unpolarised-family(1). (2) Each $\mcE_i$ is a relative divisor, so its class is a global section of $\bV$; so is $\mcH$. The fibre of the span is spanned by the classes $e_0,\dots,e_{10}$ of [@DK13, §3], which is $M$ there, primitive in $L_{\mathrm{K3}}$ and of signature $(1,10)$; primitivity is an open condition on the fibre, so the span is primitive throughout (@prop:coble-is-the-ten-nodal-sextic-type). (3) is the orthogonal complement of (2) in (1). (4) The map of quotient stacks $B\to\bar B$ is a principal $S_{10}$-bundle of stacks (@lem:d2-labelling-cover), so $\pi_1(B)$ is a normal subgroup of $\pi_1(\bar B)$ with quotient $S_{10}$ (@lem:d2-label-lift(2)), the pullback $\bT_{\bar B}|_B$ is $\bT$, and the monodromy group of $\bT$ is the image of $p_*\pi_1(B)$ in that of $\bT_{\bar B}$ (@lem:coble-family-base-change); hence $\Gamma_\Co(B)\subseteq\Gamma_\Co(\bar B)$, and no statement is made about $\Gamma_\Co$ itself. The action of a permutation of the labels on the classes $\varepsilon_i$ is the permutation of the corresponding sections, and $\PGL_3$ acts trivially on the cohomology classes of the fibre.
:::


::: {.lemma #lem:d2-labelled-base-monodromy title="The family and the local system over the labelled base"}

The family and the local system of @lem:d2-unpolarised-family(3) and @lem:d2-local-system descend to the base $B$ of the principal bundle of @lem:d2-plane-sextic-freeness(3), and the monodromy group (@def:transport-and-monodromy) of $\bT$ over $B$ is $\rho\qty{\pi_1(B,s)}=\rho\qty{\pi_1(V,s)}$, the group $\Gamma_\Co(B)$ of the presentation $B$ (@def:gamma-co-groups(1)). That $\Gamma_\Co(B)$ is $\Gamma_\Co$ of @def:coble-family-unpolarized is the comparison of the presentation with the stack, research#797, item 6, and is not asserted here. The group is a subgroup of $\Orth(T_\Co)$ and lies in $\Orth^+(T_\Co)$ (@lem:monodromy-is-spinor-positive).
:::

::: {.proof}

The family and $\bT$ are $\PGL_3$-equivariant (@lem:d2-unpolarised-family(3)), so they descend to the base $B$ of the principal bundle $V\to B$. A loop of $B$ lifts to a path (@def:path-connectedness) of $V$ by local triviality and compactness of $[0,1]$; the lift ends at $gs$ for some $g\in\PGL_3$, and since $\PGL_3$ is connected a path from $e$ to $g$ turns it into a loop of $V$ over the given loop. Hence $\pi_1(V,s)\to\pi_1(B,[s])$ is surjective. The monodromy group (@def:transport-and-monodromy) of the descended system on $B$ is $\rho\qty{\pi_1(B,[s])}$, and its pullback to $V$ is $\bT$, so it equals $\rho\qty{\pi_1(V,s)}$, which is $\Gamma_\Co(B)$ (@lem:d2a-monodromy-of-the-stack); no identification with $\Gamma_\Co$ of @def:gamma-co-groups(1) is used, that being research#797, item 6. Transport is an isometry (@prop:local-system-of-lattices-monodromy), so $\Gamma_\Co(B)\leq\Orth(T_\Co)$, and the monodromy of a family over a connected base lies in the component of the orthogonal group that preserves the period (@lem:monodromy-is-spinor-positive).
:::

::: {.lemma #lem:d2a-monodromy-of-the-stack title="The monodromy of the labelled base is the monodromy on $V$, conditional on quotient descent"}

Let $G$ be a connected complex Lie group (@def:group) acting on a connected complex analytic space $V$, and let $\bL$ be a $G$-equivariant local system of lattices on $V$: a local system with isomorphisms (@def:isomorphism-of-objects) $\varphi_g(v)\colon\bL_v\to\bL_{gv}$ for $g\in G$ and $v\in V$, continuous in $(g,v)$, with $\varphi_e=\id$ and $\varphi_{gh}(v)=\varphi_g(hv)\circ\varphi_h(v)$. Assume the quotient-descent hypothesis

(D) $G$-equivariant local systems of lattices on $V$ are equivalent to local systems of lattices on $[V/G]$, with pullback along $V\to[V/G]$ inverse to descent, including the comparisons along $2$-morphisms and their cocycle conditions.

Write $\bL_{[V/G]}$ for the local system corresponding to $\bL$ under (D). Hypothesis (D) is research#797, item 4, the descent left open by @rmk:the-descent-stops-at-the-2-morphisms, and is not proved here; clauses (1)--(3) are conditional on it. Let $s\in V$ and identify $\bL_s$ with a lattice $T$.

1. Under (D), every loop of $[V/G]$ at $[s]$ is homotopic, in the loop model of the quotient stack (pairs $(g,\widetilde\gamma)$, as in @lem:orbifold-monodromy-of-a-nonfree-quotient), to a loop of $V$ at $s$.
2. Under (D), the monodromy group (@def:transport-and-monodromy) of $\bL_{[V/G]}$ on $[V/G]$ equals the image $\rho\qty{\pi_1(V,s)}\leq\Orth(T)$ of the monodromy representation of $\bL$ on $V$.
3. Under (D), for $G=\SL_3$ acting on $V$ as in @not:d2-plane-sextic-base and $\bL=\bT$ of @lem:d2-local-system, which is $\SL_3$-equivariant by @lem:d2-unpolarised-family(3), this gives $\Gamma_\Co(B)=\rho\qty{\pi_1(V,s)}$: the labelled base of @def:coble-family-unpolarized is the presentation over which that group is computed. What the clause does not give is the monodromy of the stack $\mcM_\Co$ of @def:coble-moduli-functor: the identification of the labelled stack with that presentation, and with it $\Gamma_\Co=\Gamma_\Co(B)$ for $\Gamma_\Co$ of @def:gamma-co-groups(1), is research#797, item 6, it is unproved, and no statement on this page uses it except as hypothesis (A4) of @thm:gamma-co-is-the-stack-monodromy.
:::

::: {.proof}

*The loops (@def:loops-suspension) of the stack.* Hypothesis (D) is what supplies the descended local system $\bL_{[V/G]}$ whose monodromy is being computed; the per-loop lemma alone does not supply it. In the loop model of the quotient stack (the description recorded in @lem:orbifold-monodromy-of-a-nonfree-quotient for a discrete group, and valid here for the $G$-torsor $V\to[V/G]$) an orbifold loop of $V/G$ at $[s]$ is represented by a pair $(g,\tilde\gamma)$ with $g\in G$ and $\tilde\gamma$ a path (@def:path-connectedness) in $V$ from $s$ to $gs$. What is used here is that model, an orbifold loop being a pair $(g,\tilde\gamma)$, and not the exact (@def:exact-complex) sequence stated in that lemma, whose quotient by $\Gamma$ is stated for a discrete group; for a connected $G$ the group element of a loop is homotopic to a path in $V$, which is what the next paragraph proves. The transport of $\bL_{[V/G]}$ along the pair is
$$\varphi_g(s)^{-1}\circ\tilde\gamma^*,$$
the second factor being the transport along $\tilde\gamma$ (@def:transport-and-monodromy) and the first the identification of the fibre at $gs$ with the fibre at $s$ given by the equivariance. A general loop of the stack is a finite concatenation of paths in $V$ and of such pairs, so it is enough to treat one pair.

*The group element is a path in $V$.* Because $G$ is connected, choose $\beta\colon[0,1]\to G$ with $\beta(0)=e$ and $\beta(1)=g$. For $x\in\bL_s$ the assignment $t\mapsto\varphi_{\beta(t)}(s)(x)$ is a section of the pullback of $\bL$ along $t\mapsto\beta(t)s$ over $[0,1]$, with value $x$ at $t=0$ because $\varphi_e=\id$; the transport of $\bL$ along that path is therefore $\varphi_g(s)$ (@def:transport-and-monodromy, @lem:local-system-on-interval). With $\sigma$ the path $t\mapsto\beta(1-t)s$ from $gs$ to $s$, the transport along the loop $\tilde\gamma\cdot\sigma$ of $V$ at $s$ is
$$\sigma^*\circ\tilde\gamma^*=\varphi_g(s)^{-1}\circ\tilde\gamma^*$$
(@prop:transport-homotopy-invariant(2)), which is the operator above.

*The monodromy group.* Every monodromy operator of $\bL_{[V/G]}$ on the stack is therefore the transport along a loop of $V$ at $s$, so the monodromy group of the stack is contained in $\rho\qty{\pi_1(V,s)}$. Conversely a loop of $V$ at $s$ is the loop of the stack with $g=e$, so it is contained in the monodromy group of the stack. This is (2), under (D).

*Homotopy.* The same computation on homotopy classes: for $u\in[0,1]$ the path $\sigma_u\colon t\mapsto\beta(1-ut)s$ runs from $gs$ to $\beta(1-u)s$, so the pairs $\bigl(\beta(1-u),\tilde\gamma\cdot\sigma_u\bigr)$ are a family of loops of the stack, from $(g,\tilde\gamma)$ at $u=0$ to the loop $\tilde\gamma\cdot\sigma$ of $V$ at $u=1$, with the group element varying continuously from $g$ to $e$. This is (1).

*The group and the space.* $\SL_3(\CC)$ is connected: $\SL_n(\CC)$ is generated by the elementary matrices $E_{ij}(\lambda)=\id+\lambda e_{ij}$ (Gaussian elimination), and $t\mapsto E_{ij}(t\lambda)$ is a path from the identity to $E_{ij}(\lambda)$. The space $V$ is connected (@not:d2-plane-sextic-base) and is a complex analytic space, hence locally contractible. The family and the eleven classes of @lem:d2-local-system are $\SL_3$-equivariant (@lem:d2-unpolarised-family(3)), so the isomorphisms $\varphi_g$ are defined for $\bT$ and (2) applies under (D), which is (3). The clause stops there: $\rho\qty{\pi_1(V,s)}$ is the group of the presentation $B$, and identifying it with $\Gamma_\Co$ of @def:gamma-co-groups(1) is the comparison of the labelled stack with that presentation, which is research#797, item 6 and is not proved here.

*The choices.* A path from $s$ to $s'$ conjugates $\rho\qty{\pi_1(V,s)}$ to $\rho\qty{\pi_1(V,s')}$, and another isometry $\bL_s\iso T$ conjugates the subgroup in $\Orth(T)$; so the group is well defined up to conjugacy, and is a subgroup of $\Orth(T_\Co)$ once the isometry of @def:coble-family-unpolarized is fixed.
:::

::: {.lemma #lem:coble-family-labelled-monodromy title="The labelled family has monodromy in $\widetilde\Orth^+ (T_\Co)$"}

On base 3 of @def:coble-family-unpolarized, the labelled base, the monodromy group (@def:transport-and-monodromy) of $\bT$, that is $\Gamma_\Co(B)=\rho\qty{\pi_1(B,s)}$ (@def:gamma-co-groups(1)), is contained in $\widetilde\Orth^+(T_\Co)$. That this group is $\Gamma_\Co$ is the comparison of the presentation with the stack, research#797, item 6, and is not asserted here.
:::

::: {.proof}

The eleven classes of @lem:d2-local-system(2) are values at $s$ of global sections of $\bV$, and $\bM$ is their span, primitive (@def:primitive-embedding) and nondegenerate (@def:polarization) of signature $(1,10)$ (@lem:d2-local-system(2), @prop:coble-is-the-ten-nodal-sextic-type).
So @cor:lattice-polarized-k3-monodromy applies: the restriction of the monodromy to $T_\Co=\bM^{\perp\bV}$ takes values in $\widetilde\Orth^+(T)$.
That group is $\Orth^+(T_\Co)\intersect\discriminantkernel{T_\Co}$, which is $\widetilde\Orth^+(T_\Co)$ (@def:gamma-co-groups, @prop:gamma-co-images(1)).
:::

::: {.lemma #lem:d2-label-lift title="A path from $s$ to every $S_{10}$-translate, and the fundamental-group sequence"}

Let $B=V/\PGL_3$ be the labelled base, a path connected complex analytic space on which $S_{10}$ acts (@not:d2-plane-sextic-base, @lem:d2-incidence-connected(3)), let $\bar B=[B/S_{10}]$ be the quotient stack, and let $s\in B$ map to $[s]\in\bar B$. Then:

1. For every $\sigma\in S_{10}$ there is a path (@def:path-connectedness) of $B$ from $s$ to $\sigma s$.
2. The assignment that sends an orbifold loop $(\sigma,\tilde\gamma)$ of $\bar B$ at $[s]$ to $\sigma^{-1}$ is a surjective homomorphism $\pi_1(\bar B,[s])\to S_{10}$ whose kernel is the image of $\pi_1(B,s)$; equivalently, the assignment to the pair of its group element $\sigma$ is a surjective anti-homomorphism for the product convention of @def:transport-and-monodromy. In particular
$$1\too\pi_1(B,s)\too\pi_1(\bar B,[s])\too S_{10}\too1$$
is exact.
:::

::: {.proof}

1. $B$ is path connected (@lem:d2-incidence-connected(3)), so any two of its points are joined by a path; take the endpoints $s$ and $\sigma s$. This is the whole content of the clause, and it is not a formality: a *constant* path joins $s$ to $\sigma s$ only when $\sigma s=s$, so surjectivity in 2. cannot be read off the constant loop.

2. An orbifold loop of $\bar B$ at $[s]$ is a pair $(\sigma,\tilde\gamma)$ with $\tilde\gamma$ a path of $B$ from $s$ to $\sigma s$ --- this is the loop model of @lem:orbifold-monodromy-of-a-nonfree-quotient, which is the groupoid model of $[B/S_{10}]$ --- and such a pair exists for every $\sigma$ by 1. The class of $(\sigma,\tilde\gamma)$ depends only on $\sigma$ and on the homotopy class of $\tilde\gamma$ rel endpoints. For two loops $(\sigma,\tilde\gamma)$ and $(\sigma',\tilde\delta)$, the composite with the convention of @def:transport-and-monodromy, in which the left loop is traversed after the right, lifts from $s$ by $\tilde\delta$ followed by the $\sigma'$-translate of $\tilde\gamma$, and ends at $\sigma'\sigma s$; so the group element of the composite is $\sigma'\sigma$, the assignment to the pair of its group element is an anti-homomorphism, and $(\sigma,\tilde\gamma)\mapsto\sigma^{-1}$ is a homomorphism. It is onto by 1. A loop in its kernel has $\sigma=e$, so it is a pair $(e,\tilde\gamma)$ with $\tilde\gamma$ a loop of $B$ at $s$: the kernel is the image of $\pi_1(B,s)$. A loop of $B$ that becomes null-homotopic in $\bar B$ is null-homotopic in $B$, because $B\to\bar B$ is the quotient by the finite group $S_{10}$ and a null-homotopy of the image lifts at the loop. So $\pi_1(B,s)\to\pi_1(\bar B,[s])$ is injective (@def:injective-map) with that image, and the sequence is exact.
:::

::: {.lemma #lem:d2-labelling-cover title="The labels are a principal $S_{10}$-bundle of stacks"}

Let $B=V/\PGL_3$ and $\bar B=[B/S_{10}]=[V/(\SL_3\times S_{10})]$ be the labelled and unlabelled bases of @not:d2-plane-sextic-base. Then the quotient map $p\colon B\to\bar B$ is a principal $S_{10}$-bundle in the category of stacks: the morphism
$$S_{10}\times B\too B\times_{\bar B}B,\qquad (\sigma,b)\longmapsto (b,\sigma b)$$
is an equivalence, and $p$ is finite étale of degree (@def:graded-object) $10!=3\,628\,800$. In particular
Consequently the fundamental-group sequence of @lem:d2-label-lift(2) applies. The induced map of coarse spaces $V/\PGL_3\to V/(\SL_3\times S_{10})$ is not asserted to be a covering: the statement proved here is about the quotient stack, and no freeness of the $S_{10}$-action on $B$ is used.
:::

::: {.proof}

*The fibre product.* The two actions commute, so $[B/S_{10}]\cong[V/(\SL_3\times S_{10})]$, and it suffices to prove the statement for the quotient map $X\to[X/H]$ of a stack $X$ by a finite group $H$. An object of $X\times_{[X/H]}X$ over a test space $T$ is a pair $(x,x')$ of objects of $X(T)$ together with an isomorphism of their images in $[X/H](T)$; such an isomorphism is an $H$-arrow; an $H$-equivariant automorphism of the trivial $H$-torsor is right multiplication by an $h\in H$, so the arrow determines $h$, and $x'\cong hx$. So the fibre product is $H\times X$ and the displayed morphism is an equivalence; $X\to[X/H]$ is then a torsor under $H$, hence finite étale of degree $\abs{H}$.

*The exact sequence.* The fibre product above shows that $B\to\bar B$ is a torsor under the finite group $S_{10}$, and a quotient of a locally compact space by a finite group has the path-lifting and homotopy-lifting properties. With those two properties the fundamental-group sequence, including the existence of a path (@def:path-connectedness) from $s$ to $\sigma s$ for each $\sigma$, is @lem:d2-label-lift(2), whose hypotheses are the path connectedness of $B$ (@lem:d2-incidence-connected(3)) and the description of $\bar B$ as $[B/S_{10}]$.

*The coarse spaces.* What is used above is the quotient stack, not its coarse space. A projectivity $g$ with $gZ=Z$ and $gp_i=p_{\sigma(i)}$ carries $(Z;p_1,\dots,p_{10})$ to $\sigma(Z;p_1,\dots,p_{10})$ in $V$, so it makes the image of $(Z;p_1,\dots,p_{10})$ in $B$ fixed by $\sigma$ in the stack sense; this is an orbifold point of $[B/S_{10}]$, and it does not affect the torsor statement, which is a statement about quotient stacks. No freeness of the $S_{10}$-action on $B$ is used above.
:::

::: {.lemma #lem:coble-invariant-lattice-in-families title="The invariant lattice of a family of Coble covers: the marking on the labelled base, and the isotropy of the stack"}

Let $\qty{f\colon\mcs\to B,\ \pi\colon\mcx\to\mcs,\ \iota}$ be a family of Coble covers over a connected base, that is an object of the functor $\mcM_\Co$ of @def:coble-moduli-functor over $B$, with $B$ an arcwise connected and locally simply connected complex space, and put
$$
\bM_b \definedas H^2(\mcx_b,\ZZ)^{\iota_b} = \ker\qty(\iota_b^* - \id).
$$

1. $\bM$ is a local system of lattices (@def:local-system-of-lattices) of fibre $M=\generators{2}\oplus\generators{-2}^{\oplus10}$, of $2$-elementary type $(11,11,1)$, rank $11$ and signature $(1,10)$, primitive (@def:primitive-embedding) in $R^2(f\pi)_*\underline\ZZ_\mcx$. The pullback $\pi_b^*\colon H^2(\mcs_b,\ZZ)\to\bM_b$ is injective, is an isomorphism after $\tensor\QQ$, and satisfies $\pi_b^*\alpha\cdot\pi_b^*\beta=2(\alpha\cdot\beta)$; on the labelled family of @def:coble-family-unpolarized it is an isomorphism over $\ZZ$.
2. On the labelled base $B$ of @not:d2-plane-sextic-base the eleven classes $\varepsilon_0,\dots,\varepsilon_{10}$ of @lem:d2-local-system(2) are global sections of $\bM$ whose values span $\bM_b$ at every $b$; hence the transport along any path (@def:local-system-of-lattices) is the identity in that frame, $\bM$ is isomorphic to the constant system $\underline M$, and the eleven classes are a **marking of $M$ in families**. In particular the monodromy representation $\pi_1(B,s)\to\Aut(M)$ of $\bM$ is trivial. Since $\pi_1(B,s)$ is the kernel of $\pi_1(\bar B,[s])\to S_{10}$ (@lem:d2-label-lift(2)), that kernel acts trivially on $\bM$.
3. For this clause assume the descent hypothesis $(\mathrm D_{S_{10}})$: $S_{10}$-equivariant local systems of lattices on $B$ are equivalent to local systems of lattices on $\bar B=[B/S_{10}]$, with pullback along $B\to\bar B$ inverse to descent, including the comparisons along $2$-morphisms and their cocycle conditions. This is research#797, item 4, the descent left open by @rmk:the-descent-stops-at-the-2-morphisms, and is not proved here. Under $(\mathrm D_{S_{10}})$, on the plane-sextic quotient stack $\bar B$ the monodromy group of the descended system $\bM$ is exactly $S_{10}$, of order $10!=3\,628\,800$, acting by permutation of $\varepsilon_1,\dots,\varepsilon_{10}$ with $\varepsilon_0$ fixed; $\bM$ is there the constant $\underline M$ twisted by the finite étale $S_{10}$-torsor $p\colon B\to\bar B$ of @lem:d2-labelling-cover, and is not itself constant. This is a statement about $\bar B$ and **not** about $\mcM_\Co$: it sees neither the plane-model equivalences nor the automorphisms of a fibre.
4. On $\mcM_\Co$ the isotropy contributes, and its contribution is infinite. An automorphism $g$ of $S_b$ fixes $K_{S_b}$, hence preserves the unique anti-bicanonical curve $C_b$, hence lifts to an automorphism $\tilde g$ of the cover commuting with $\iota_b$, unique up to $\iota_b$; and $\tilde g^*\pi_b^*=\pi_b^*g^*$. So in the frame $e_0=\pi^*H$, $e_i=\pi^*E_i$ the isotropy acts on $\bM_b$ by the action of $g^*$ on $\Pic(S_b)=\generators{H,E_1,\dots,E_{10}}$, read in the same coordinates. For the Bertini involution $\sigma_I$ of @lem:coble-automorphism-group-is-infinite(1) that is
$$
e_0\longmapsto 17e_0-6\tsum_{i\in I}e_i,\qquad e_i\longmapsto 6e_0-3e_i-2\tsum_{j\in I,\ j\neq i}e_j\ \ (i\in I),\qquad e_a, e_b\longmapsto e_a, e_b,
$$
and $\sigma_I^*\sigma_J^*$ has characteristic polynomial $(t-1)^7(t+1)^2(t^2-14t+1)$, of infinite order (@lem:coble-automorphism-group-is-infinite(2)); the image contains $W_{10}(2)$ ([@CD12, §5]; @rmk:coble-automorphisms-infinite). The monodromy group of $\bM$ on the classical substack is generated by the contributions of @lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions: the image of $\pi_1(\bar B,[x])$, the loops attached to the plane-model arrows, and the isotropy. By (2) the kernel $\pi_1(B,s)$ of $\pi_1(\bar B,[s])\to S_{10}$ acts trivially, and by (3) the first contribution is exactly the relabelling group $S_{10}$; the effective contributions are therefore the relabellings of (3), the plane-model equivalences, and this image of the isotropy. The first and third of them already give a group that is **not** contained in $S_{10}$, the Bertini action on $M$ not being a permutation of the frame; hence $\bM$ is **not** the constant system on $\mcM_\Co$. The image of $\Aut(S_b)$ in $\Aut(M)$ is **infinite**: the product $\sigma_I^*\sigma_J^*$ of two Bertini involutions displayed above has infinite order (@lem:coble-automorphism-group-is-infinite(2)), and it lies in that image because the Bertini involutions are automorphisms of $S_b$ at every irreducible ten-nodal sextic (@prop:coble-plane-model-comparison(2)); at unnodal members the image contains the whole subgroup $W_{10}(2)$ (@rmk:coble-automorphisms-infinite(1)). The period argument gives finiteness on the *other* summand and not on this one: an automorphism preserves the splitting $H^2(X_b,\ZZ)=M_b\oplus T_\Co$ of @lem:d2-local-system(2)--(3) and acts on $T_\Co$ through a map fixing the period $2$-plane $P=H^{2,0}(X_b)$, so its image in $\Orth(T_\Co)$ lies in $\Stab_{\Orth(T_\Co)}(P)$, finite by @lem:period-stabiliser-finite. That lemma is about a lattice of signature $(2,n)$ with $P$ positive definite, which is $T_\Co$ of signature $(2,9)$ and **not** $M$ of signature $(1,10)$. The plane-model contribution is not computed here, and no generation statement is made for the class of @def:coble-moduli-functor beyond that; on the classical substack the exact group is @thm:coble-monodromy-on-m-classical. Every conclusion in this clause that uses (3), including the identification of the first contribution with $S_{10}$ and the resulting lower bound for the monodromy group, is conditional on $(\mathrm D_{S_{10}})$; the Bertini and isotropy computations do not use it.

*Departure, and the repair it forced.* An earlier form of this lemma concluded from (3) that $\operatorname{Mon}_{\mcM_\Co}(\bM)=S_{10}$ and that every family over a connected base has monodromy inside $S_{10}$, transferring (3) along the comparison $\bar B\to\mcM_\Co$. Both conclusions are withdrawn: the essential surjectivity of @prop:coble-plane-model-comparison(1) is proved only for the classical subfamily (@rmk:coble-class-smooth-antinbicanonical), so the smooth atlas of @prop:coble-stack-as-quotient gives no transfer to the whole widened stack, and (4) exhibits the isotropy as a contribution (3) does not see.
:::

::: {.proof}

(1) $\iota$ is an involution of the local system $R^2(f\pi)_*\underline\ZZ_\mcx$: the involution of each fibre, $\iota_b^2=\id_{\mcx_b}$ being a morphism of the family. A fixed sublattice of a free $\ZZ$-module under an involution is saturated (if $nx\in\ker(\iota^*-1)$ then $n(\iota^*-1)x=0$ and $\iota^*-1$ is a homomorphism of free modules, so $(\iota^*-1)x=0$), so $\bM$ is a primitive local subsystem, and it is a local system of lattices once its rank is constant and the restricted form is nondegenerate. For the fibre: $\iota_b$ has the single smooth rational curve $\pi_b^{-1}(C_b)$ as fixed locus, so $\chi(\Fix\iota_b)=2$ and Lefschetz gives $\trace(\iota_b^*\mid H^2)=0$, hence rank $11$ in each eigenspace; the $(+1)$-eigenspace is $\pi_b^*\Pic(\mcs_b)=S_\Co\cong M$ of type $(11,11,1)$ (@prop:coble-invariant-lattice), and that type is unique by @thm:two-elementary-classification, whose hypothesis that both signature entries be nonzero holds, the signature being $(1,10)$. Nondegeneracy: over $\QQ$ the two eigenspaces are orthogonal and the involution preserves the form, so each is nondegenerate, that of $\bM_b$ of signature $(1,10)$. For the pullback, $\pi_{b*}\pi_b^*=2\id$ gives injectivity, $\pi_{b*}\pi_b^*=\id+\iota_b^*$ gives $x=\tfrac12\pi_b^*\pi_{b*}x$ for $x$ fixed by $\iota_b^*$, and the projection formula gives $\pi_b^*\alpha\cdot\pi_b^*\beta=\deg(\pi_b)(\alpha\cdot\beta)=2(\alpha\cdot\beta)$; the integral statement on the labelled family is the basis computation of @prop:coble-invariant-lattice. (2) The sections are @lem:d2-local-system(2), and they descend from $V$ to $B$ because they are $\SL_3$-invariant (@rmk:d2a-family-over-the-bases); their values span the fibre by the same item. Transport along a path carries the value at one end of a section to its value at the other (@def:transport-and-monodromy), so in the frame they give every transport matrix is the identity; the monodromy representation is trivial, and a local system with trivial monodromy on a connected and locally simply connected base is constant [@Voi07, Corollary 3.10], as in @lem:sublocal-system-of-constant-sheaf. Since @lem:d2-label-lift(2) identifies $\pi_1(B,s)$ with the kernel of $\pi_1(\bar B,[s])\to S_{10}$, that kernel acts trivially on $\bM$. (3) Assume $(\mathrm D_{S_{10}})$. By @lem:d2-labelling-cover the map $p\colon B\to\bar B$ is a principal $S_{10}$-bundle in the category of stacks and its pullback of $\bM$ is $\bM$, which (2) trivializes. An orbifold loop of $\bar B$ at $[s]$ is a pair $(\sigma,\tilde\gamma)$ with $\tilde\gamma$ a path of $B$ from $s$ to $\sigma s$, in the loop model of @lem:orbifold-monodromy-of-a-nonfree-quotient used at @lem:d2-label-lift(2). The local system $\bM$ on $\bar B$ is the descent of the constant system $\underline M$ on $B$ with the $S_{10}$-equivariant structure of @lem:d2-unpolarised-family(3); let $\varphi_\sigma\in\Aut(M)$ be the action of $\sigma$ on the frame, so that $\sigma\mapsto\varphi_\sigma$ is the representation of the descent and $\varphi_\sigma(\varepsilon_i)=\varepsilon_{\sigma(i)}$, the inverse of the index convention $\mcE_i\mapsto\mcE_{\sigma^{-1}(i)}$ written there, which is an anti-homomorphism in $\sigma$ and so the inverse of the homomorphism of the descent. By @lem:orbifold-monodromy-of-a-nonfree-quotient(2) the transport along $(\sigma,\tilde\gamma)$ is $\varphi_\sigma^{-1}$, the permutation $\varepsilon_i\mapsto\varepsilon_{\sigma^{-1}(i)}$; for two loops $(\sigma,\tilde\gamma)$ and $(\tau,\tilde\delta)$ the group element of the composite is $\tau\sigma$ (@lem:d2-label-lift(2)) and $\varphi_{\tau\sigma}^{-1}=\varphi_\sigma^{-1}\varphi_\tau^{-1}$, so the transport is a homomorphism in the pair. The map $\pi_1(\bar B,[s])\to S_{10}$, $(\sigma,\tilde\gamma)\mapsto\sigma^{-1}$, is a surjective homomorphism (@lem:d2-label-lift(2)), so the monodromy group is exactly $S_{10}$, and $\sigma$ permutes $\varepsilon_1,\dots,\varepsilon_{10}$ while fixing $\varepsilon_0$ (@lem:d2-local-system(4)), so the system is not constant on $\bar B$. (4) The lifts: $g$ acts on $H^0(-2K)$ in one dimension, so $g^*C_b=C_b$ for the unique member $C_b$ of $\abs{-2K_{\mcs_b}}=\theset{C_b}$ (@def:coble-moduli-functor(1)); the double cover is branched along $C_b$, so $g$ lifts, and two lifts differ by the deck transformation $\iota_b$. Then $\tilde g^*\pi_b^*=\pi_b^*g^*$ because both sides are the pullback of $g^*$ along $\pi_b$, and the displayed matrix is @lem:coble-automorphism-group-is-infinite(1) transported by $\pi_b^*$ into the frame $e_i=\pi_b^*E_i$, $e_0=\pi_b^*H$ of @prop:coble-invariant-lattice; the characteristic polynomial and the infinite order are @lem:coble-automorphism-group-is-infinite(2). That the system on $\mcM_\Co$, on which the isotropy acts, is the descent of the system of the family: an isomorphism of objects is an isomorphism of the covers commuting with the involutions, hence an isometry carrying $M_b$ to $M_{b'}$, which is the argument the volume uses for $\bT$ (@prop:gamma-co-on-the-coble-stack). Hence, under $(\mathrm D_{S_{10}})$, the monodromy group on $\mcM_\Co$ contains $S_{10}$ by (3); independently of that hypothesis it contains the Bertini image of $\Aut(S_b)$ by the computation above, and that image is not a permutation of the frame. Its image on $M$ is **infinite**, the product $\sigma_I^*\sigma_J^*$ computed above having infinite order, and no finiteness on $M$ is used or available: what the period bounds is the action on the other summand, where the image fixes the period $2$-plane $P\subset T_\Co\tensor\RR$ and so lies in $\Stab_{\Orth(T_\Co)}(P)$, finite by @lem:period-stabiliser-finite, whose hypotheses --- signature $(2,9)$ and $P$ positive definite --- hold for $T_\Co$ and fail for $M$ of signature $(1,10)$. So the group is not contained in $S_{10}$, and a constant system has trivial isotropy action, so $\bM$ is not constant on $\mcM_\Co$.
:::

::: {.lemma #lem:coble-monodromy-group-on-m-is-the-canonical-stabilizer title="The group acting on the invariant lattice: the canonical class is fixed, and the stabilizer of its class bounds it on both sides"}

Let $M=\generators{e_0,\dots,e_{10}}$ be the invariant lattice $\pi^*\Pic(S_b)=\generators{2}\oplus\generators{-2}^{\oplus10}$ of @prop:coble-invariant-lattice, and
$$
K \definedas -3e_0+\tsum_{i=1}^{10}e_i = \pi^*K_{S_b},\qquad K^2=2\cdot 9-2\cdot 10=-2,
$$
the class $\pi^*K_{S_b}=-[\Fix\iota_b]$ of @lem:d2-unpolarised-family(1), the negative of the fixed curve, of square $-2$. Let $G\subseteq\Orth(M)$ be the image of the group generated by the relabellings of the ten classes (@lem:d2-local-system(2)), the plane-model equivalences (@prop:coble-plane-model-comparison(4)) and $\Aut(S_b)$, which contains $W_{10}(2)$ ([@CD12, Thm. 3.5], stated there for unnodal members, and @rmk:coble-automorphisms-infinite).

1. **Every generator fixes $K$.** The relabellings permute $e_1,\dots,e_{10}$ and fix $e_0$, so they fix $K$. An automorphism of $S_b$ preserves $K_{S_b}$, hence $K$; on the Bertini generator this reads, from the display of @lem:coble-automorphism-group-is-infinite(1),
$$
-3\qty(17H-6\tsum_{i\in I}E_i)+\tsum_{i\in I}\qty(6H-3E_i-2\tsum_{j\in I,\ j\neq i}E_j)+E_a+E_b=-3H+\tsum_{i=1}^{10}E_i=K_{S_b}.
$$
Every plane-model equivalence fixes $K$, and by an argument that does not inspect any particular one. A plane presentation of $S_b$ is a blowup presentation $S_b\cong\Bl_{p_1,\dots,p_{10}}\PP^2$, contributing the frame $H,E_1,\dots,E_{10}$ of $\Pic(S_b)$ of Gram matrix $\diag(1,-1,\dots,-1)$; two presentations give two frames of one lattice, and the plane-model equivalence between them is the change of basis carrying one frame to the other (@prop:coble-plane-model-comparison(4)). The canonical class is intrinsic to $S_b$, and in *each* frame the blowup formula gives it by the same combination,
$$
K_{S_b}=-3H+\tsum_{i=1}^{10}E_i=-3H'+\tsum_{i=1}^{10}E'_i,
$$
so the change of basis carries $K_{S_b}$ to itself, and hence carries $K=\pi^*K_{S_b}$ to itself in $M$. The quadratic Cremona involution of three nodes is the instance where the second frame is written out at @prop:coble-plane-model-comparison(3), and there the same identity reads
$$
-3\qty(2H-E_1-E_2-E_3)+(H-E_2-E_3)+(H-E_1-E_3)+(H-E_1-E_2)+\tsum_{i=4}^{10}E_i=-3H+\tsum_{i=1}^{10}E_i=K_{S_b}.
$$
2. **Upper bound.** Hence $G\subseteq\Stab_{\Orth(M)}(K)$. This is a proper subgroup of $\Orth(M)$, and of the stabilizer of the orientation class: the reflection $s_{e_1}\in\Orth(M)$ in the $(-2)$-class $e_1$ has $s_{e_1}(K)=K-2e_1\neq K$, since $K\cdot e_1=-2$ and $s_{e_1}(x)=x-2(x\cdot e_1)e_1/(e_1\cdot e_1)=x+(x\cdot e_1)e_1$, while it fixes $e_1^{\perp}\supseteq\RR e_0$, the positive line of the signature $(1,10)$ form, pointwise. So neither $\Orth(M)$ nor the subgroup fixing the orientation class is $G$: the image lies in the stabilizer of the $(-2)$-class $K$, a proper subgroup of both.
3. **Lower bound.** $G$ contains the $45$ Bertini involutions of @prop:coble-plane-model-comparison(2), which are automorphisms of $S_b$ at every irreducible ten-nodal sextic (@lem:coble-automorphism-group-is-infinite(3)), hence $G$ contains $\Aut(S_b)$'s subgroup $W_{10}(2)$, which by its definition is the subgroup of $W_{10}$ whose elements satisfy $w(v)-v\in 2K^{\perp}$ for every $v$ (@rmk:coble-automorphisms-infinite), so they fix $K$ and act trivially on $K^{\perp}/2K^{\perp}$, hence act trivially on $M/2M$. And $G$ is **not** contained in that subgroup: a transposition $\sigma$ of two of the ten labels sends the class of $\tfrac12e_1$ to that of $\tfrac12e_2$, and these differ because $e_2-e_1\notin 2M$, its $e_1$-coordinate being $1$. So the image is neither the stabilizer of $K$ alone nor a subgroup of the $2$-congruence kernel.
4. **The gap.** $G$ is therefore a subgroup of $\Stab_{\Orth(M)}(K)$ containing $W_{10}(2)$ and an element outside the $2$-congruence kernel. Its exact value is the index $\qty[\Stab_{\Orth(M)}(K):G]$, which is not determined here: restriction to $K^{\perp M}$, of rank $10$ and signature $(1,9)$, injects the stabilizer, and the index is at most $\qty[\Orth(K^{\perp}):W_{10}(2)]=\qty[\Orth(K^{\perp}):W_{10}]\cdot\qty[W_{10}:W_{10}(2)]$, whose second factor is at most $\abs{\Orth(q,F_2^{10})}$ by the level-$2$ definition and whose first is the finite-index statement for the reflection group of $K^{\perp}\cong E_{10}(2)$, which is not verified here.
:::

::: {.proof}

(1) is the three computations displayed in the statement: for the relabellings because $K=-3e_0+\sum e_i$ is symmetric in the $e_i$; for the automorphisms because $K_S$ is the canonical class, with the Bertini check carried out coordinatewise in $\Pic(S_b)=\generators{H,E_1,\dots,E_{10}}$ of squares $(1,-1,\dots,-1)$, where the eight summands contribute $6\cdot 8=48$ to the coefficient of $H$, $18-3-2\cdot 7=1$ to each of the eight $E_i$ with $i\in I$, and the two fixed classes stay; for the plane-model equivalences by the change of frame displayed in the statement: both frames are blowup frames of one surface, the canonical class is intrinsic, and the blowup formula expresses it by the same combination in each, so the change of basis fixes it; the displayed quadratic Cremona identity is the instance computed in the coordinates of @prop:coble-plane-model-comparison(3), where the second frame is $A,H-E_2-E_3,H-E_1-E_3,H-E_1-E_2,E_4,\dots,E_{10}$. (2) $s_{e_1}$ is the reflection in the $(-2)$-class $e_1$, the integral isometry $s_{e_1}(x)=x+(x\cdot e_1)e_1$ of $M$, with $s_{e_1}^2=\id$. It fixes $e_1^{\perp}$ pointwise, and $e_1^{\perp}$ contains $\RR e_0$ because $e_0\cdot e_1=0$ and $\RR e_0$ is the positive line of the form $\diag(2,-2,\dots,-2)$; it moves $K$ by the computation above. So the stabilizer of $K$ is strictly smaller than $\Orth(M)$ and than the subgroup fixing the positive line. (3) The definition of $W_{10}(2)$ quoted in @rmk:coble-automorphisms-infinite reads $W_{10}(2)=\theset{w\in W_{10}\st w(v)-v\in 2E_{10}\ \text{for all } v\in\Pic(X)}$, which is the subgroup acting trivially on $K^{\perp}/2K^{\perp}$, with $E_{10}=K^{\perp}$; the action on $M/2M$ is then trivial as well, $K$ being fixed; and $e_2-e_1\notin 2M$ because its coordinate on $e_1$ is $1$, which is odd. (4) An isometry of $M$ fixing $K$ is determined by its restriction to $K^{\perp}$ because $K$ is primitive, and $K^{\perp}$ has rank $10$ and signature $(1,9)$ since $M$ has signature $(1,10)$ and $K^2<0$.
:::

::: {.lemma #lem:coble-image-on-m-is-the-weyl-group title="The image of the relabellings, the plane-model equivalences and $\Aut(S_b)$ on $M$ is $W(E_{10})$, and the stabilizer exceeds it by the sign"}

Let $M=\generators{e_0,\dots,e_{10}}=\pi^*\Pic(S_b)=\generators{2}\oplus\generators{-2}^{\oplus10}$ (@prop:coble-invariant-lattice) and $K=\pi^*K_{S_b}=-[\Fix\iota_b]$, of square $-2$, as in @lem:coble-monodromy-group-on-m-is-the-canonical-stabilizer, and let $G\subseteq\Orth(M)$ be the image of the group generated by the relabellings of the ten classes, the plane-model equivalences and $\Aut(S_b)$, which contains $W_{10}(2)$ (@rmk:coble-automorphisms-infinite; [@CD12, Thm. 3.5] gives the containment, for unnodal members). Then
$$
G=W(E_{10})=\Orth^+\qty(K^{\perp M})\subseteq\Orth\qty(K^{\perp M})\cong\Orth(E_{10}),\qquad \qty[\Stab_{\Orth(M)}(K):G]\le2,
$$
with equality when the restriction $\Stab_{\Orth(M)}(K)\to\Orth(K^{\perp M})$ is onto.

1. *The ten classes are the simple system of $E_{10}$.* Put $\delta_i\definedas\pi^*(E_i-E_{i+1})$ for $i=1,\dots,9$ and $\delta_c\definedas\pi^*(H-E_1-E_2-E_3)$. Each lies in $K^{\perp M}$, because $K_{S_b}\cdot(E_i-E_{i+1})=-1+1=0$ and $K_{S_b}\cdot(H-E_1-E_2-E_3)=-3+3=0$, and each has square $2\cdot(-2)=-4$; the only nonzero pairings are
$$
\delta_i\cdot\delta_{i+1}=2\quad(1\le i\le8),\qquad \delta_c\cdot\delta_3=2 .
$$
So the rescaled Gram matrix $\tfrac12\qty(\delta\cdot\delta)$ is $-2I+\operatorname{Adj}(T_{2,3,7})$: a chain of nine with the tenth class joined to the third vertex, which is the diagram of $E_{10}$ (@not:coxeter-polytope-faces, @def:reflection-group).
2. *Their reflections lie in $G$.* For a class of square $-4$ the reflection is $s_\delta(x)=x-\tfrac{2(x\cdot\delta)}{(\delta\cdot\delta)}\delta=x+\tfrac12(x\cdot\delta)\delta$, integral on $M$ because every $x\cdot\delta_i$ is even. The reflection in $\delta_i$ is the transposition of the labels $i,i+1$: $s_{\delta_i}(e_i)=e_{i+1}$, $s_{\delta_i}(e_{i+1})=e_i$, $e_0$ fixed. The reflection in $\delta_c$ is realized at one general plane presentation by the quadratic Cremona involution of @lem:cremona-second-plane-model-general, because in the coordinates of $\Pic(S_b)$ one has $s(H-E_1-E_2-E_3)(H)=H+(H-E_1-E_2-E_3)=2H-E_1-E_2-E_3$ and $s(H-E_1-E_2-E_3)(E_i)=E_i+(E_i\cdot(H-E_1-E_2-E_3))(H-E_1-E_2-E_3)=H-E_j-E_k$ for $i\in\theset{1,2,3}$, with $E_4,\dots,E_{10}$ fixed, which is the frame change displayed at @prop:coble-plane-model-comparison(3). The reflections in the simple system generate the reflection group (@def:reflection-group), so $W(E_{10})\subseteq G$. No arbitrary-point Cremona assertion is needed: $G$ is generated with the arrows at all points of $B$.
3. *The upper bound is the orthochronous part; the sign is outside.* By @lem:coble-monodromy-group-on-m-is-the-canonical-stabilizer, $G\subseteq\Stab_{\Orth(M)}(K)$, and restriction injects that stabilizer into $\Orth(K^{\perp M})\cong\Orth(E_{10})$. The isometry group of $E_{10}$ is $\set{\pm1}\times W(E_{10})$ with $W(E_{10})=\Orth^+(E_{10})$, which is the imported input (I) of @thm:coble-monodromy-on-m-classical; the citation [@Vin72, Table 5] carried here earlier does not give it, that paper's tables being for the odd forms (1) and (3) of its introduction. Every generator of $G$ maps the positive cone of $M$ to itself, which is what orthochrony means here. The relabelling $\sigma$ fixes $e_0$, and $e_0^2=2>0$, so it fixes an interior point of the positive cone and therefore permutes its two sheets trivially. A plane-model change is a birational map between plane models of one smooth projective surface, so it pulls a nef and big class back to a nef and big class (@prop:coble-plane-model-comparison(3), where the substitute line class $A=2H-E_1-E_2-E_3$ of the quadratic Cremona is nef and big like $H$); carried to $M$ by $\pi^*$ and halved, that class has positive square, so the induced isometry of $M$ again fixes an interior point of the positive cone. An automorphism of $X_b$ preserves the Kähler cone, which lies in the positive cone, so it too maps the positive cone to itself. Hence every element of $G$ is orthochronous. Hence $G\subseteq\Orth^+(E_{10})=W(E_{10})$, and with (2) that is the equality. The other sign element $-\id_{K^{\perp M}}$ negates the positive line of $K^{\perp M}\tensor\RR$, so it is not orthochronous and lies outside $G$; $-\id_M$ does not fix $K$.
:::

::: {.proof}

(1) The squares are $2\qty(E_i-E_{i+1})^2=2\cdot(-2)$ and $2\qty(H-\tsum_{1}^{3}E_i)^2=2(1-3)$, the factor $2$ being the degree of $\pi$. For the pairings, $\delta_i\cdot\delta_{i+1}=2\qty((E_i-E_{i+1})\cdot(E_{i+1}-E_{i+2}))=2\cdot1$, and $\delta_i\cdot\delta_j=0$ for $j\neq i\pm1$; and $(H-E_1-E_2-E_3)\cdot(E_i-E_{i+1})$ is $1$ for $i=3$ and $0$ for every other $i$, since $H$ is orthogonal to the $E$'s and exactly one of $E_i,E_{i+1}$ meets exactly one of $E_1,E_2,E_3$. (2) The reflection formula is the standard reflection computation, and $\tfrac12(x\cdot\delta)$ is an integer because $M$ is even: in the frame $e_0,\dots,e_{10}$ where the form is $\diag(2,-2,\dots,-2)$ every $x\cdot y$ is even, $x\cdot\delta_i=-2(x_{i+1}-x_i)$ and $x\cdot\delta_c=2(x_0+x_1+x_2+x_3)$; the displayed values on a basis determine a reflection. The last clause is @def:reflection-group. (3) Injectivity is because $K$ is primitive (@def:primitive-embedding) in $M$; $\set{\pm1}\times W(E_{10})$ is the input (I); for the relabelling, $e_0^2=2$ makes $e_0$ an interior point of the positive cone, and an isometry of a lattice of signature $(1,n)$ fixing an interior point of the positive cone preserves that cone; for the plane-model change, its image on $M$ is the reflection $s_{\delta_c}$ of (2), which fixes $\delta_c^{\perp}$ pointwise, and $\delta_c^{\perp}$ has signature $(1,9)$ because $\delta_c^2=-4<0$, so it contains a class of positive square fixed by $s_{\delta_c}$, and the same argument applies; geometrically that class is the one carried from a nef and big class, which a birational map of smooth surfaces preserves, as displayed at @prop:coble-plane-model-comparison(3); and an automorphism of $X_b$ is a Hodge isometry preserving the Kähler cone, which lies in the positive cone, so it is orthochronous on $M$.
:::

::: {.notation #not:paths-of-a-groupoid-quotient title="The fundamental groupoid of a topological stack with a chart" defines="$\Pi_1(\mcY)$; $[p\alpha]$; $[\rho]$"}

Let $\mcY$ be a topological stack [@Noo05, Definition 13.8] for a class of local fibrations under which the inclusions of finite CW complexes are local trivial cofibrations [@Noo05, §17, first paragraph], let $p\colon X\to\mcY$ be a chart by a topological space $X$ [@Noo05, Definition 7.1], and let
$$s,t\colon R\definedas X\times_{\mcY}X\rightrightarrows X$$
be its groupoid, so that $\mcY\cong[X/R]$ [@Noo05, Proposition 3.4].
By the definition of the $2$-fibre product, a point $\rho$ of $R$ is an identification $\rho\colon p(s(\rho))\rightsquigarrow p(t(\rho))$ of points of $\mcY$, and a map $h\colon W\to R$ from a space is an identification $p\circ s\circ h\Rightarrow p\circ t\circ h$.

A path of $\mcY$ from a point $y$ to a point $y'$ is a triple $(\gamma,\epsilon_0,\epsilon_1)$ of a map $\gamma\colon[0,1]\to\mcY$ and identifications $\epsilon_0\colon y\rightsquigarrow\gamma(0)$ and $\epsilon_1\colon\gamma(1)\rightsquigarrow y'$ [@Noo05, Definition 17.2].
$\Pi_1(\mcY)$ is the fundamental groupoid of $\mcY$ [@Noo05, Definition 17.2]: its objects are the points of $\mcY$, and its morphisms $y\to y'$ are the paths from $y$ to $y'$ modulo homotopy relative to the endpoints, that is, homotopy of maps of pairs $([0,1],\theset{0,1})\to(\mcY,y\sqcup y')$ [@Noo05, Definition 17.2].
The composite of $(\gamma,\epsilon_0,\epsilon_1)\colon y\to y'$ and $(\gamma',\epsilon_0',\epsilon_1')\colon y'\to y''$ is $(\gamma\vee_\varphi\gamma',\epsilon_0,\epsilon_1')$, the gluing of $\gamma$ and $\gamma'$ along $\varphi=\epsilon_0'\circ\epsilon_1\colon\gamma(1)\rightsquigarrow\gamma'(0)$ [@Noo05, Proposition 16.1], reparametrized to $[0,1]$.
The group $\pi_1(\mcY,y)$ of [@Noo05, Definition 17.5] is $\Pi_1(\mcY)(y,y)$, a pointed map from the circle being a path from $y$ to $y$ by the same gluing, and the groupoid axioms are verified as the group axioms are verified there.
Products in $\Pi_1(\mcY)$ are written in the order of traversal.
For a path $\alpha$ of $X$ from $a$ to $b$ and a point $\rho$ of $R$, put
$$[p\alpha]\definedas[(p\circ\alpha,\id,\id)]\in\Pi_1(\mcY)\qty(p(a),p(b)),\qquad [\rho]\definedas[(\mathrm{const}_{p(s(\rho))},\id,\rho)]\in\Pi_1(\mcY)\qty(p(s(\rho)),p(t(\rho))),$$
the second being the constant path with the identification $\rho$ at its end [@Noo05, Remark 17.3].
:::

::: {.definition #def:haefliger-path title="Haefliger path of a groupoid" defines="Haefliger path; $[w]$"}

In the notation of @not:paths-of-a-groupoid-quotient, a *Haefliger path* of $[R\rightrightarrows X]$ from $a\in X$ to $b\in X$ is a sequence
$$w=(\alpha_0,\rho_1,\alpha_1,\dots,\rho_n,\alpha_n),\qquad n\geq0,$$
of paths $\alpha_i\colon[0,1]\to X$ and points $\rho_i\in R$ with
$$\alpha_0(0)=a,\qquad s(\rho_i)=\alpha_{i-1}(1),\qquad t(\rho_i)=\alpha_i(0),\qquad\alpha_n(1)=b$$
[@Col09, §3.1, where the sequence is written $(g_0,\alpha_1,g_1,\dots,\alpha_n,g_n)$ with an arrow at each end; the two forms differ by constant paths and identity arrows].
Its class is
$$[w]\definedas[p\alpha_0]\,[\rho_1]\,[p\alpha_1]\cdots[\rho_n]\,[p\alpha_n]\in\Pi_1(\mcY)\qty(p(a),p(b)).$$
A Haefliger path from $x$ to $x$ is a Haefliger loop at $x$.
The fundamental groupoid of a Lie groupoid in the sense of Haefliger is the groupoid of homotopy classes of these sequences [@Col09, Definitions 3.2 and 3.3].
:::

::: {.lemma #lem:haefliger-paths-exhaust-the-fundamental-groupoid title="Every path of $[X/R]$ is a Haefliger path, and $\pi_1([X/R])$ is generated by the loops of $X$ and the arrows of $R$"}

In the notation of @not:paths-of-a-groupoid-quotient and @def:haefliger-path:

1. For $a,b\in X$, every element of $\Pi_1(\mcY)\qty(p(a),p(b))$ is the class $[w]$ of a Haefliger path $w$ from $a$ to $b$.
   Explicitly, let $(\gamma,\epsilon_0,\epsilon_1)$ be a path from $p(a)$ to $p(b)$, and let $0=t_0<t_1<\dots<t_m=1$, $\beta_j\colon[t_{j-1},t_j]\to X$ and $\theta_j\colon p\circ\beta_j\Rightarrow\gamma|_{[t_{j-1},t_j]}$ be a subdivision with lifts of $\gamma$ on its intervals. Then
   $$[(\gamma,\epsilon_0,\epsilon_1)]=[\rho_0]\,[p\beta_1]\,[\rho_1]\,[p\beta_2]\cdots[p\beta_m]\,[\rho_m],$$
   $$\rho_0=\theta_1(t_0)^{-1}\circ\epsilon_0,\qquad\rho_j=\theta_{j+1}(t_j)^{-1}\circ\theta_j(t_j)\quad(0<j<m),\qquad\rho_m=\epsilon_1\circ\theta_m(t_m),$$
   where $\rho_0$ is an arrow from $a$ to $\beta_1(t_0)$, $\rho_j$ an arrow from $\beta_j(t_j)$ to $\beta_{j+1}(t_j)$, and $\rho_m$ an arrow from $\beta_m(t_m)$ to $b$. Such a subdivision with lifts exists for every path.
2. Let $X$ be path connected, fix $x\in X$, and for every $z\in X$ fix a path $c_z$ of $X$ from $x$ to $z$, with $c_x$ constant. For a path $\alpha$ of $X$ from $a$ to $b$ and a point $\rho$ of $R$ put
   $$\ell_\alpha\definedas[pc_a]\,[p\alpha]\,[pc_b]^{-1}=p_*\qty[c_a\alpha c_b^{-1}]\in p_*\pi_1(X,x),\qquad\lambda_\rho\definedas[pc_{s(\rho)}]\,[\rho]\,[pc_{t(\rho)}]^{-1}\in\pi_1(\mcY,p(x)).$$
   Then every Haefliger loop $w=(\alpha_0,\rho_1,\alpha_1,\dots,\rho_n,\alpha_n)$ at $x$ has
   $$[w]=\ell_{\alpha_0}\,\lambda_{\rho_1}\,\ell_{\alpha_1}\cdots\lambda_{\rho_n}\,\ell_{\alpha_n},$$
   and $\pi_1(\mcY,p(x))$ is generated by the subgroup $p_*\pi_1(X,x)$ and the elements $\lambda_\rho$, $\rho\in R$. For $\rho$ with $s(\rho)=t(\rho)=z$, an element of the isotropy group of $p(z)$, the element $\lambda_\rho=[pc_z]\,[\rho]\,[pc_z]^{-1}$ is the conjugate by $[pc_z]$ of the inertial loop $\omega_{p(z)}(\rho)$ of [@Noo05, §17]; the isotropy groups enter the generation through these $\lambda_\rho$.
3. If $h\colon[0,1]\to R$ is a path from $\rho$ to $\rho'$, then
   $$[\rho]=[p(s\circ h)]\,[\rho']\,[p(t\circ h)]^{-1},\qquad\lambda_\rho=\ell_{s\circ h}\,\lambda_{\rho'}\,\ell_{t\circ h}^{-1},$$
   so in (2) one point $\rho$ from each path component of $R$ suffices.
:::

::: {.proof}

*The rules for paths.* Let $(\gamma,\epsilon_0,\epsilon_1)$ be a path from $y$ to $y'$.

(a) For an identification $\Theta\colon\gamma\Rightarrow\gamma'$ of maps $[0,1]\to\mcY$,
$$[(\gamma,\epsilon_0,\epsilon_1)]=[(\gamma',\ \Theta(0)\circ\epsilon_0,\ \epsilon_1\circ\Theta(1)^{-1})]:$$
$\Theta$ is an identification of the two as maps of pairs [@Noo05, Definition 17.1], and an identification is a homotopy [@Noo05, Remark 17.3].

(b) For a continuous $r\colon[0,1]\to[0,1]$ with $r(0)=0$ and $r(1)=1$, $[(\gamma\circ r,\epsilon_0,\epsilon_1)]=[(\gamma,\epsilon_0,\epsilon_1)]$, by the homotopy $\gamma\circ K$ with $K(u,t)=(1-u)r(t)+ut$, which is constant on $u\mapsto(u,0)$ and on $u\mapsto(u,1)$.

(c) A point of an interval is the inclusion of a finite CW complex in another, hence a local trivial cofibration. So gluing data $(\gamma,\gamma',\varphi\colon\gamma(1)\rightsquigarrow\gamma'(0))$ have a glued map $\gamma\vee_\varphi\gamma'$, unique up to a unique identification; and identifications $\Theta\colon\gamma\Rightarrow\delta$, $\Theta'\colon\gamma'\Rightarrow\delta'$ with $\psi\circ\Theta(1)=\Theta'(0)\circ\varphi$ glue to one identification $\gamma\vee_\varphi\gamma'\Rightarrow\delta\vee_\psi\delta'$ restricting to $\Theta$ and $\Theta'$ [@Noo05, Theorem 16.2: the restriction functor to gluing data is an equivalence].

(d) For identifications $\varphi\colon y\rightsquigarrow y'$ and $\varphi'\colon y'\rightsquigarrow y''$ put $[\varphi]\definedas[(\mathrm{const}_y,\id,\varphi)]$. Then $[\varphi]\,[\varphi']=[\varphi'\circ\varphi]$, so $[\id]$ is an identity and $[\varphi^{-1}]=[\varphi]^{-1}$. Indeed the left side is the class of $(\mathrm{const}_y\vee_\varphi\mathrm{const}_{y'},\id,\varphi')$; the pair $(\id,\varphi^{-1})$ is an isomorphism from the gluing data $(\mathrm{const}_y,\mathrm{const}_{y'},\varphi)$ to $(\mathrm{const}_y,\mathrm{const}_y,\id)$, whose glued map is $\mathrm{const}_y$; so (c) gives $\Theta\colon\mathrm{const}_y\vee_\varphi\mathrm{const}_{y'}\Rightarrow\mathrm{const}_y$ with $\Theta$ the identity at the start and $\varphi^{-1}$ at the end, and (a) gives the class of $(\mathrm{const}_y,\id,\varphi'\circ\varphi)$.

(e) $[(\gamma,\epsilon_0,\epsilon_1)]=[\epsilon_0]\,[(\gamma,\id,\id)]\,[\epsilon_1]$. The right side is the class of $(\mathrm{const}_y\vee_{\epsilon_0}\gamma\vee_{\id}\mathrm{const}_{\gamma(1)},\id,\epsilon_1)$. The triple $(\epsilon_0,\id,\id)$ is an isomorphism from its gluing data to the data $(\mathrm{const}_{\gamma(0)},\gamma,\mathrm{const}_{\gamma(1)};\id,\id)$, whose glued map is $\gamma\circ c$ for the map $c\colon[0,3]\to[0,1]$ that is $0$ on $[0,1]$, $t-1$ on $[1,2]$ and $1$ on $[2,3]$. So (c) gives an identification of the glued map with $\gamma\circ c$ that is $\epsilon_0$ at the start and the identity at the end; (a) turns the right side into the class of $(\gamma\circ c,\epsilon_0,\epsilon_1)$, and (b) into that of $(\gamma,\epsilon_0,\epsilon_1)$.

(f) For $0<t<1$, $[(\gamma,\id,\id)]=[(\gamma|_{[0,t]},\id,\id)]\,[(\gamma|_{[t,1]},\id,\id)]$: the map $\gamma$ is the glued map of its two restrictions along the identity, by the uniqueness in (c), and (b) removes the reparametrization.

*(1).* The chart $p$ is an epimorphism [@Noo05, Definitions 7.1 and 3.1]: there are an open cover $\theset{U_i}$ of $[0,1]$, maps $a_i\colon U_i\to X$ and identifications $p\circ a_i\Rightarrow\gamma|_{U_i}$. By the Lebesgue number lemma there is a subdivision $0=t_0<\dots<t_m=1$ with each $[t_{j-1},t_j]$ inside one $U_{i(j)}$, and the restrictions of $a_{i(j)}$ and of its identification are $\beta_j$ and $\theta_j$; this is the existence statement. Now let a subdivision with lifts be given and write $\gamma_j\definedas\gamma|_{[t_{j-1},t_j]}$. By (a) for $\theta_j$, then (e) and (d),
$$[p\beta_j]=[(\gamma_j,\ \theta_j(t_{j-1}),\ \theta_j(t_j)^{-1})]=[\theta_j(t_{j-1})]\,[(\gamma_j,\id,\id)]\,[\theta_j(t_j)]^{-1}.$$
By (e), then (f), then this equation solved for $[(\gamma_j,\id,\id)]$,
$$[(\gamma,\epsilon_0,\epsilon_1)]=[\epsilon_0]\,\prod_{j=1}^m[(\gamma_j,\id,\id)]\,[\epsilon_1]
=[\epsilon_0]\,[\theta_1(t_0)]^{-1}\,[p\beta_1]\,[\theta_1(t_1)]\,[\theta_2(t_1)]^{-1}\,[p\beta_2]\cdots[p\beta_m]\,[\theta_m(t_m)]\,[\epsilon_1],$$
and (d) collects each product of two identification classes into one: $[\epsilon_0]\,[\theta_1(t_0)]^{-1}=[\rho_0]$, $[\theta_j(t_j)]\,[\theta_{j+1}(t_j)]^{-1}=[\rho_j]$ and $[\theta_m(t_m)]\,[\epsilon_1]=[\rho_m]$. Each $\rho_j$ is an identification between the images under $p$ of two points of $X$, that is a point of $R$ with the stated source and target (@not:paths-of-a-groupoid-quotient). The right side is the class of the Haefliger path $(\mathrm{const}_a,\rho_0,\beta_1,\rho_1,\dots,\beta_m,\rho_m,\mathrm{const}_b)$, with each $\beta_j$ reparametrized to $[0,1]$ by (b), since the class of a constant path of $X$ is an identity.

*(2).* The equality $\ell_\alpha=p_*[c_a\alpha c_b^{-1}]$ holds because $\alpha\mapsto[p\alpha]$ is compatible with composition and with homotopy of paths of $X$. In the product $\ell_{\alpha_0}\lambda_{\rho_1}\ell_{\alpha_1}\cdots\lambda_{\rho_n}\ell_{\alpha_n}$ the factor $[pc_{\alpha_{i-1}(1)}]^{-1}$ that ends $\ell_{\alpha_{i-1}}$ cancels the factor $[pc_{s(\rho_i)}]$ that begins $\lambda_{\rho_i}$, the factor $[pc_{t(\rho_i)}]^{-1}$ that ends $\lambda_{\rho_i}$ cancels the factor $[pc_{\alpha_i(0)}]$ that begins $\ell_{\alpha_i}$, and the two outer factors are classes of the constant path $c_x$; what remains is $[p\alpha_0]\,[\rho_1]\,[p\alpha_1]\cdots[\rho_n]\,[p\alpha_n]=[w]$, every $[\rho_i]$ being kept inside its $\lambda_{\rho_i}$. By (1) every element of $\pi_1(\mcY,p(x))=\Pi_1(\mcY)(p(x),p(x))$ is such a $[w]$, hence a product of elements of $p_*\pi_1(X,x)$ and elements $\lambda_\rho$. For $s(\rho)=t(\rho)=z$ the class $[\rho]$ is the class of the constant path at $p(z)$ with the identification $\rho$, which is $\omega_{p(z)}(\rho)$.

*(3).* The map $h$ is an identification $\eta\colon p\circ s\circ h\Rightarrow p\circ t\circ h$ with $\eta(0)=\rho$ and $\eta(1)=\rho'$ (@not:paths-of-a-groupoid-quotient). By (a), then (e) and (d),
$$[p(s\circ h)]=[(p\circ t\circ h,\ \rho,\ \rho'^{-1})]=[\rho]\,[p(t\circ h)]\,[\rho']^{-1},$$
which is the first equation; the second follows by multiplying on the left by $[pc_{s(\rho)}]$ and on the right by $[pc_{t(\rho)}]^{-1}$ and inserting $[pc_{s(\rho')}]^{-1}[pc_{s(\rho')}]$ and $[pc_{t(\rho')}]^{-1}[pc_{t(\rho')}]$ around $[\rho']$.
:::

::: {.lemma #lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions title="Generators of $\pi_1$ of the classical Coble substack: the loops of the labelled base and the arrows of the plane-model groupoid"}

Let $P\colon B\to\bar B\xrightarrow{\ \varphi\ }\mcM^{\mathrm{cl}}_\Co$ be the composite of the $S_{10}$-torsor of @lem:d2-labelling-cover with the smooth cover of @prop:coble-stack-as-quotient, let
$$R_B\definedas B\times_{\mcM^{\mathrm{cl}}_\Co}B\rightrightarrows B$$
be its groupoid, and let $\pi_1(\mcM^{\mathrm{cl}}_\Co,P(s))$, $s\in B$, be the fundamental group of the quotient stack $[B/R_B]$ of the underlying topological groupoid [@Noo05, Definitions 3.3 and 17.5].

1. A point of $R_B$ with source $b$ and target $b'$ is an isomorphism of the objects of @def:coble-moduli-functor over $b$ and $b'$: a pair $(g,\tilde g)$ of an isomorphism $g\colon S_b\to S_{b'}$ and an isomorphism $\tilde g\colon X_b\to X_{b'}$ with $\pi_{b'}\tilde g=g\pi_b$. Every isomorphism $g$ has exactly the two lifts $\tilde g$ and $\tilde g\iota_b$. The points of $R_B$ with $b'=b$ form the isotropy group of $P(b)$, which maps onto $\Aut(S_b)$ with kernel $\theset{\id,\iota_b}$. The points with $b'=\sigma b$, $g=\id_{S_b}$ and $\tilde g=\id_{X_b}$, for $\sigma\in S_{10}$, are the image of $B\times_{\bar B}B=S_{10}\times B$ (@lem:d2-labelling-cover); they are the *relabelling arrows*.
2. $\pi_1(\mcM^{\mathrm{cl}}_\Co,P(s))$ is generated by $P_*\pi_1(B,s)$ and the elements $\lambda_\rho=[Pc_b]\,[\rho]\,[Pc_{b'}]^{-1}$ of @lem:haefliger-paths-exhaust-the-fundamental-groupoid(2), $\rho\colon b\to b'$ running over the points of $R_B$; every element is a product $\ell_{\alpha_0}\lambda_{\rho_1}\ell_{\alpha_1}\cdots\lambda_{\rho_n}\ell_{\alpha_n}$ in which every arrow $\rho_i$ of the loop is kept.
3. The subgroup generated by $P_*\pi_1(B,s)$ and the $\lambda_\rho$ of the relabelling arrows is the image of $\pi_1(\bar B,[s])$. A point of $R_B$ with source $b$ and target $b'$ is a point of the plane-model groupoid $R=\bar B\times_{\mcM^{\mathrm{cl}}_\Co}\bar B$ of @prop:coble-stack-as-quotient over the points $[b]$ and $[b']$ of $\bar B$, and conversely. Hence $\pi_1(\mcM^{\mathrm{cl}}_\Co,P(s))$ is generated by the image of $\pi_1(\bar B,[s])$ and the elements $\lambda_\rho$ of the arrows $\rho$ of $R$; the elements of the isotropy groups are the arrows with $b'=b$, and they enter through their $\lambda_\rho$.
:::

::: {.proof}

*The hypotheses of @lem:haefliger-paths-exhaust-the-fundamental-groupoid.* $B$ is a complex space (@lem:d2-plane-sextic-freeness(3)). By @prop:coble-stack-as-quotient and @lem:d2-labelling-cover, $P$ is a smooth cover of $\mcM^{\mathrm{cl}}_\Co$ by a complex space: $R_B$ is a complex space and its two projections to $B$ are smooth. A smooth morphism of complex spaces is, locally on its source, the projection of a product with a polydisc, so the source and target maps of the underlying topological groupoid are locally cartesian with Euclidean fibres, the class of [@Noo05, Example 13.1($3'$)]. The quotient stack $[B/R_B]$ has the chart $B$ [@Noo05, §7, the paragraph after Corollary 7.6], and the groupoid of that chart is $R_B$: the map from the presheaf of groupoids $\lfloor B/R_B\rfloor$ to its stackification $[B/R_B]$ is fully faithful over every space [@Noo05, Propositions 3.6 and 3.7, Definition 3.1], so the identifications between the images of two points of $B$ are the points of $R_B$ over them. The base change of the chart along itself is therefore the source map of $R_B$, so $[B/R_B]$ is a topological stack for that class [@Noo05, Definition 13.8]; this is the construction that [@Noo05, §20] carries out for an algebraic stack with a smooth presentation. For that class the inclusions of finite CW complexes are local trivial cofibrations [@Noo05, §17, first paragraph; Example 13.7($3'$)]. $B$ is path connected (@lem:d2-incidence-connected(3)).

(1) A point of the $2$-fibre product over $(b,b')$ is an identification $P(b)\rightsquigarrow P(b')$, that is an isomorphism of the two objects, which by @def:coble-moduli-functor is a pair of isomorphisms of the surfaces and of the covers commuting with the covering maps; it commutes with the involutions as well, because $\tilde g\iota_b\tilde g^{-1}$ is a deck transformation of $\pi_{b'}$ other than the identity. An isomorphism $g$ carries the unique member $C_b$ of $\abs{-2K_{S_b}}$ to $C_{b'}$ (@lem:d2-unpolarised-family(1)), so it lifts to the double covers branched along them, and two lifts differ by the deck transformation $\iota_b$; this is the argument of @lem:coble-invariant-lattice-in-families(4). The relabelling arrows are the image of the groupoid $B\times_{\bar B}B\rightrightarrows B$ of the chart $B\to\bar B$, which is $S_{10}\times B$ by @lem:d2-labelling-cover: $b$ and $\sigma b$ are the same sextic with its nodes renamed, and they have the same surface and the same cover.

(2) is @lem:haefliger-paths-exhaust-the-fundamental-groupoid(2) for the chart $P$.

(3) By @lem:haefliger-paths-exhaust-the-fundamental-groupoid(2) for the chart $B\to\bar B$, whose groupoid is $S_{10}\times B\rightrightarrows B$, the group $\pi_1(\bar B,[s])$ is generated by the image of $\pi_1(B,s)$ and the elements $\lambda_\sigma$ of the points of $S_{10}\times B$; the map $\varphi_*$ carries the first to $P_*\pi_1(B,s)$ and each $\lambda_\sigma$ to the $\lambda_\rho$ of the relabelling arrow $\rho$ that is the image of $\sigma$, because $\varphi_*[qc]=[Pc]$ for a path $c$ of $B$ and the chart $q\colon B\to\bar B$, and $\varphi_*$ carries the class of an identification to the class of its image. So the image of $\pi_1(\bar B,[s])$ is the subgroup named, and the generation statement follows from (2). A point of $R$ over the points $[b]$ and $[b']$ of $\bar B$ is an identification $\varphi([b])\rightsquigarrow\varphi([b'])$, which is a point of $R_B$ with source $b$ and target $b'$.
:::

::: {.lemma #lem:transport-order-on-the-classical-coble-stack title="Path order and the orthochrony of the generators on $M$"}
Use the notation of @lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions, put $\bL=\bM$ of @lem:coble-invariant-lattice-in-families, and for a path of $\mcM^{\mathrm{cl}}_\Co$ let $T$ be transport along it (@def:transport-and-monodromy). For $r=(g,\tilde g)\colon b\to b'$ a point of $R_B$, let $H,H'$ be the line classes in the plane frames at $b,b'$, and let $m(r)$ be the matrix of $\tilde g_*$ between the global frames of $\bM$ at $b$ and $b'$, as in @lem:coble-invariant-lattice-in-families(2).

1. *Path order.* The product on $\pi_1(\mcM^{\mathrm{cl}}_\Co,P(s))$ is written in the order of traversal (@not:paths-of-a-groupoid-quotient), whereas the product on $\pi_1(B,s)$ is the one in which $\gamma\delta$ traverses $\delta$ and then $\gamma$ (@def:transport-and-monodromy). Transport reverses concatenation, so on loop classes of the stack
$$
T(\omega\eta)=T(\eta)\circ T(\omega).
$$
Thus $T$ is an anti-homomorphism on that loop group. The map $\omega\mapsto T(\omega^{-1})$ is a homomorphism with the same image.
2. *The arrow loops.* For $\lambda_r=[Pc_{s(r)}]\,[r]\,[Pc_{t(r)}]^{-1}$, whose convention is the traversal order of @not:paths-of-a-groupoid-quotient, the path segments $Pc_{s(r)}$ and $Pc_{t(r)}$ have identity transport in the frame of @lem:coble-invariant-lattice-in-families(2). Therefore
$$
T(\lambda_r)=T([Pc_{t(r)}]^{-1})\circ T([r])\circ T([Pc_{s(r)}])=m(r),
\qquad
T(\lambda_r^{-1})=m(r)^{-1}=m(r^{-1}).
$$
Since $R_B$ is a groupoid, $r\mapsto r^{-1}$ permutes its points, and the subgroup generated by $\{m(r)\st r\in R_B\}$ is unchanged whether one reads the loop group through $T$ or through the homomorphism of 1.
3. *The canonical class.* Every $m(r)$ fixes $K=-3e_0+\sum_i e_i$. Indeed $e_0=\pi_b^*H$ and $m(r)e_0=\pi_{b'}^*g_*H$, and the canonical class is intrinsic to the surface, so
$$
m(r)K=\pi_{b'}^*g_*K_{S_b}=\pi_{b'}^*K_{S_{b'}}=K.
$$
4. *Orthochrony.* Every $m(r)$ preserves the positive cone of $M$. The class $e_0$ has square $2$, hence is interior to one component. Its image $m(r)e_0=\pi_{b'}^*g_*H$ also has square $2$. The class $g_*H$ is the pushforward of a curve class under an isomorphism, and $H'$ is nef, so $g_*H\cdot H'\geq0$; equality would put the positive-square class $g_*H$ in the negative-definite lattice $H'^{\perp M}$, so
$$
m(r)e_0\cdot e_0=2\,g_*H\cdot H'>0.
$$
An isometry of a lattice of signature $(1,10)$ carries positive vectors into positive vectors, and a positive vector has positive pairing with exactly one of the two components; the inequality therefore puts $m(r)e_0$ in the component of $e_0$. Hence $m(r)\in\Orth^+(M)$ (@prop:spinor-plus-cone-components).
5. *Restriction to $K^{\perp M}$.* The sublattice $K^{\perp M}$ is nondegenerate of signature $(1,9)$ because $K^2=-2<0$. Since every $m(r)$ fixes $K$ and preserves a component $C_M$ of the positive cone of $M$, it restricts to an isometry of $K^{\perp M}$ preserving $C_M\cap K^{\perp M}_{\bR}$, one component of the positive cone of $K^{\perp M}$. Hence
$$
m(r)|_{K^{\perp M}}\in\Orth^+\qty(K^{\perp M}).
$$
Consequently the subgroup $H\definedas\langle m(r):r\in R_B\rangle\subseteq\Orth^+(M)$ maps under restriction into $\Orth^+(K^{\perp M})=W(E_{10})$; restriction is injective because $K$ is primitive (@def:primitive-embedding), and $M=K^{\perp M}\oplus\ZZ K$ because $(x\cdot K)/K^2\in\ZZ$ for every $x\in M$: in the frame where the form is $\diag(2,-2,\dots,-2)$ one has $x\cdot K=-6x_0-2\tsum_{i\geq1}x_i$, so $x\cdot K$ is even and $(x\cdot K)/K^2=-(x\cdot K)/2$ is an integer. Primitivity alone does not give this --- on $M=\diag(2,2)$ and $K=e_1+e_2$ the sum $K^{\perp M}+\ZZ K$ has index $2$ (record `computations/reports/coble_799-element-lattice-checks-run.txt`).
:::

::: {.proof}

(1) The identity $T(\omega\eta)=T(\eta)\circ T(\omega)$ is @prop:transport-homotopy-invariant(2) for the concatenation $\omega$ followed by $\eta$, which is the product convention of @not:paths-of-a-groupoid-quotient. The assignment $\omega\mapsto T(\omega^{-1})$ is multiplicative because
$T((\omega\eta)^{-1})=T(\eta^{-1}\omega^{-1})=T(\omega^{-1})\circ T(\eta^{-1})$.

(2) Expanding $\lambda_r$ in traversal order gives $c_{s(r)}$, then $r$, then the inverse of $c_{t(r)}$; transport composes in the reverse function order, with both path transports the identity. The inverse formula follows from the group identity $(ABC)^{-1}=C^{-1}B^{-1}A^{-1}$ in the same traversal convention.

(3) The equality $e_0=\pi_b^*H$ is @prop:coble-invariant-lattice; under the matrix $m(r)$ it goes to $\pi_{b'}^*g_*H$. The canonical classes are related by $g_*K_{S_b}=K_{S_{b'}}$, and $K$ is the pullback of each, so this is the displayed computation.

(4) The pushforward of the nef class $H$ under the isomorphism $g$ is nef, and $H'$ is nef, so their product is nonnegative. Both have square $1$, so $g_*H$ has square $1$; if the product were zero then $g_*H\in H'^{\perp M}$, which is negative definite because $M$ has signature $(1,10)$ and $(H')^2=1>0$. This is impossible for a vector of square $1$, so the product is positive. The factor $2$ is the degree of the K3 cover in $e_0\cdot e_0=2H\cdot H$. The last sentence is @prop:spinor-plus-cone-components.

(5) On $K^{\perp M}_{\bR}$, the set of positive vectors has two components. A positive vector of $K^{\perp M}$ is positive in $M$, so exactly one of those components lies in the chosen component $C_M$; this intersection is $C_M\cap K^{\perp M}_{\bR}$. An isometry preserving both $K^{\perp M}$ and $C_M$ preserves that intersection, and $\Orth^+$ is exactly the subgroup preserving each cone component (@prop:spinor-plus-cone-components). The identification $\Orth^+(K^{\perp M})=W(E_{10})$ is the imported input (I) of @thm:coble-monodromy-on-m-classical, not a computation; that $K^{\perp M}$ is $E_{10}(2)$ is one: the ten classes $\delta_1,\dots,\delta_9,\delta_c$ of @lem:coble-image-on-m-is-the-weyl-group(1) lie in $K^{\perp M}$, are independent, and have Gram matrix $2\qty(-2I+\operatorname{Adj}(T_{2,3,7}))$, twice the Gram matrix of $E_{10}$, of determinant $2^{10}\cdot(-1)=-2^{10}$, while $\det K^{\perp M}=\det M/K^2=2^{11}/(-2)=-2^{10}$; equal determinants of equal rank force $\langle\delta\rangle=K^{\perp M}$, and scaling the form does not change the integral orthogonal group (record `computations/reports/coble_799-element-lattice-checks-run.txt`). Injectivity of the restriction is @lem:coble-monodromy-group-on-m-is-the-canonical-stabilizer(4), and the decomposition $M=K^{\perp M}\oplus\ZZ K$ used for it and for surjectivity is the computation of the clause.
:::

::: {.theorem #thm:coble-monodromy-on-m-classical title="The monodromy group of the invariant lattice on the classical Coble substack is $W(E_{10})$"}

Let $\mcM^{\mathrm{cl}}_\Co$ be the classical Coble substack of @prop:coble-stack-as-quotient, let $\bM$ be the local system of invariant lattices $H^2(\mcx)^\iota$ of @lem:coble-invariant-lattice-in-families on its universal family, let $x=P(s)$, $s\in B$, be a base point, with $\bM_x\cong M$ the identification by the frame $\varepsilon_0(s),\dots,\varepsilon_{10}(s)$ of @lem:coble-invariant-lattice-in-families(2), and let
$$\rho\colon\pi_1(\mcM^{\mathrm{cl}}_\Co,x)\too\Aut(M),\qquad M=\generators{e_0,\dots,e_{10}}=\generators{2}\oplus\generators{-2}^{\oplus10},$$
be its monodromy representation, read through the homomorphism $\rho(\omega)=T(\omega^{-1})$ of @lem:transport-order-on-the-classical-coble-stack(1), because the products on $\pi_1(\mcM^{\mathrm{cl}}_\Co,x)$ are written in the order of traversal (@not:paths-of-a-groupoid-quotient) and transport reverses them (@prop:transport-homotopy-invariant(2)); inversion is a bijection of the loop group, so the image is the monodromy group of @def:transport-and-monodromy. Then, with
$$G\definedas\rho\qty(\pi_1(\mcM^{\mathrm{cl}}_\Co,x)),$$
$$G=W(E_{10})=\Orth^+\qty(K^{\perp M}),\qquad K=-3e_0+\tsum_{i=1}^{10}e_i .$$
The group $G$ is generated by the image of $\pi_1(B,s)$ and by the classes $\lambda_\rho$ of the arrows $\rho$ of the plane-model groupoid $R_B$ (@lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(2)), and each of these acts on $M$ by an isometry that fixes $K$ and is orthochronous: the image of $\pi_1(B,s)$ trivially, in the global frame of @lem:coble-invariant-lattice-in-families(2), and an arrow $r$ as the matrix $m(r)$ of an isomorphism of surfaces between two plane frames (@lem:transport-order-on-the-classical-coble-stack(3)--(4)). That is
$$G\subseteq\Stab_{\Orth(M)}(K)\intersect\Orth^+(M).$$
That stabilizer is $W(E_{10})$: restriction to $K^{\perp M}$ is an isomorphism onto $\Orth(K^{\perp M})$, $-\id_{K^{\perp M}}\oplus\id_K$ being one extension, and its orthochronous part $\Orth^+(K^{\perp M})$ is $W(E_{10})$ [@Dol07, (5.12)], the group generated by the ten simple reflections. The index is
$$\qty[\Stab_{\Orth(M)}(K):G]=2,$$
the equality case of the index bound of @lem:coble-image-on-m-is-the-weyl-group. The other inclusion is the ten simple reflections of @lem:coble-image-on-m-is-the-weyl-group(1)--(2), the nine transpositions together with the quadratic Cremona involution at the general point of @lem:cremona-second-plane-model-general.
Every family of Coble covers over an arcwise connected, locally simply connected complex space, classical or not, has monodromy on its invariant lattice contained in $W(E_{10})$; this is a statement about a local system on a space, and its proof uses no stack (@lem:coble-canonical-class-and-ample-component-in-families(4)). The containing group is **infinite**, so no finite group bounds this monodromy: $W(E_{10})=W_{10}$ contains the image of $\Aut(S_b)$ (@rmk:coble-automorphisms-infinite(1)), which contains the infinite-order element $\sigma_I^*\sigma_J^*$ (@lem:coble-automorphism-group-is-infinite(2)), and by the display the universal family over $\mcM^{\mathrm{cl}}_\Co$ has monodromy exactly $W(E_{10})$. The finite bound in this picture is on the anti-invariant summand, where the isotropy image fixes the period and lies in a finite stabilizer (@lem:coble-invariant-lattice-in-families(4), @lem:period-stabiliser-finite). This is the statement on the classical substack. On the whole of $\mcM_\Co$ the transports of the families over spaces and the isometries of the isomorphisms of objects generate the same group $W(E_{10})$, and that group is the monodromy group of $\bM$ on $\mcM_\Co$ conditional on a chart of $\mcM_\Co$ and on the descent (D) (@cor:coble-monodromy-on-m-of-the-whole-stack).
:::

::: {.proof}

Take the base point $x=P(s)$, $s\in B$, in the notation of @lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions, and write $r=(g,\tilde g)\colon b\to b'$ for a point of $R_B$. Let $T$ be transport and put $\rho(\omega)=T(\omega^{-1})$; this is the monodromy representation in the path-order convention checked in @lem:transport-order-on-the-classical-coble-stack(1).

*Generators and their transports.* By @lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(2), $\pi_1(\mcM^{\mathrm{cl}}_\Co,x)$ is generated by $P_*\pi_1(B,s)$ and the elements $\lambda_r=[Pc_b]\,[r]\,[Pc_{b'}]^{-1}$, $r\in R_B$. The system $\bM$ on $\mcM^{\mathrm{cl}}_\Co$ is the descent of the system of the family over $B$ (@lem:coble-invariant-lattice-in-families(4), whose proof states the descent for a general arrow): its transport along $P\circ\alpha$ is the transport of the system on $B$ along the path $\alpha$ of $B$, and its transport along the identification $r$ is the isometry $\tilde g_*=(\tilde g^*)^{-1}\colon\bM_b\to\bM_{b'}$ of the isomorphism of covers. In the global frame $\varepsilon_0,\dots,\varepsilon_{10}$ of $\bM$ over $B$ the transport along every path of $B$ is the identity matrix (@lem:coble-invariant-lattice-in-families(2)). Hence $\rho$ is trivial on $P_*\pi_1(B,s)$, and @lem:transport-order-on-the-classical-coble-stack(2) gives, for every arrow,
$$
T(\lambda_r)=m(r),\qquad \rho(\lambda_r)=m(r)^{-1}=m(r^{-1}),
$$
where $m(r)$ is the matrix of $g_*\colon\Pic(S_b)\to\Pic(S_{b'})$ in the frames $H,E_1,\dots,E_{10}$ of the two plane presentations; it does not depend on the choice between the two lifts of $g$. The product of @def:transport-and-monodromy and the traversal product of @not:paths-of-a-groupoid-quotient are opposite on the loop group, which is why $\rho=T\circ\mathrm{inv}$ is the homomorphism here; in particular $P_*\colon\pi_1(B,s)\to\pi_1(\mcM^{\mathrm{cl}}_\Co,x)$ is an anti-homomorphism, and every use of $P_*$ below is through the subgroup it generates. Because the arrows are closed under inverse, the image is the subgroup
$$\rho\qty(\pi_1(\mcM^{\mathrm{cl}}_\Co,x))=H\definedas\langle m(r)\st r\in R_B\rangle\subseteq\Orth(M).$$
For a relabelling arrow $b\to\sigma b$ the matrix $m(r)$ is the permutation of $e_1,\dots,e_{10}$ by $\sigma^{-1}$, that is the map $\varepsilon_i\mapsto\varepsilon_{\sigma^{-1}(i)}$ of the frame. The transport is the identity on the classes of one surface, and the two frames differ by the relabelling $\varepsilon_j(\sigma b)=\varepsilon_{\sigma(j)}(b)$, which is the pushforward $\sigma_*\mcE_i=\mcE_{\sigma^{-1}(i)}$ of @lem:d2-unpolarised-family(3) read at the points $(\sigma b)_j=b_{\sigma(j)}$ of the proof of @lem:d2-labelling-cover, and it is the same permutation that @lem:coble-invariant-lattice-in-families(3) computes as the transport along the orbifold loop. Every relabelling arrow used below is a transposition $(i\ i+1)$, for which the permutation and its inverse agree; for a point with $b'=b$ it is the action of $g\in\Aut(S_b)$ of @lem:coble-invariant-lattice-in-families(4); and for every $r$ it is the change of frame between the plane presentation $b$ of $S_b$ and the plane presentation that $g$ carries back from $b'$, the plane-model equivalence of @lem:coble-monodromy-group-on-m-is-the-canonical-stabilizer(1). These are the relabellings, the automorphisms and the plane-model equivalences of @lem:coble-image-on-m-is-the-weyl-group, taken at all points of $B$.

*Upper bound.* By @lem:transport-order-on-the-classical-coble-stack(3)--(5), every $m(r)$ fixes $K$, lies in $\Orth^+(M)$, and restricts to $\Orth^+(K^{\perp M})$. Restriction therefore identifies $H$ with a subgroup of $\Orth^+(K^{\perp M})$. That group is $W(E_{10})$ by the input (I), with $K^{\perp M}\cong E_{10}(2)$ the computation of @lem:transport-order-on-the-classical-coble-stack(5). Since $\rho$ has the same image as $T$ and the generators of $\pi_1(\mcM^{\mathrm{cl}}_\Co,x)$ are those above, $\rho(\pi_1(\mcM^{\mathrm{cl}}_\Co,x))\subseteq W(E_{10})$. Restriction is onto $\Orth(K^{\perp M})$: by @lem:transport-order-on-the-classical-coble-stack(5) one has $M=K^{\perp M}\oplus\ZZ K$, so an isometry of $K^{\perp M}$ extends by the identity on $\ZZ K$. Since by (5) the restriction of $\Stab_{\Orth(M)}(K)\intersect\Orth^+(M)$ lands in $\Orth^+(K^{\perp M})$, and that group has cardinality $\tfrac12\abs{\Orth(K^{\perp M})}$, the two indices in the statement follow: the restriction image of $\Stab_{\Orth(M)}(K)\intersect\Orth^+(M)$ is $\Orth^+(K^{\perp M})$, which is the restriction image of $H$.

*The orthochronous part of the stabilizer.* The group $\Orth^+(\latII_{1,9})$ is $W(E_{10})$. For an Enriques surface $X$ one has $S_X(-1)=U\perp E_8\cong E_{10}$ [@Dol07, §5.4]; the lattice $E_{10}$ is $E_{2,3,7}$ of [@Dol07, Example 4.3], generated by the fundamental root vectors of the Coxeter group $W(2,3,7)$ of [@Dol07, Example 2.7], whose Coxeter graph $T_{2,3,7}$ is the ten-node diagram of $E_{10}$; its fundamental polytope has no non-trivial symmetry, so
$$\Orth(E_{10})^+=\mathrm{Ref}(E_{10})\cong W(2,3,7)$$
[@Dol07, (5.12)], which is the group generated by the ten simple reflections, that is $W(E_{10})$. The sign of the form does not change the isometry group, so the same holds for $\latII_{1,9}$, and scaling by $2$ does not change the integral orthogonal group, so it holds for $K^{\perp M}\cong E_{10}(2)$.

*Lower bound.* The reflections $s_{\delta_1},\dots,s_{\delta_9}$ are the matrices $m(r)$ of the relabelling arrows of the transpositions $(i\ i+1)$, and $s_{\delta_c}$ is, up to a relabelling, the matrix $m(r)$ of the arrow that the quadratic Cremona transformation of three nodes defines at one general point of $B$ where it gives a second plane presentation (@lem:cremona-second-plane-model-general, @lem:coble-image-on-m-is-the-weyl-group(2)). The ten reflections generate $W(E_{10})$ (@lem:coble-image-on-m-is-the-weyl-group(1)--(2)). Since each is an involution, the inverse in the relabelling convention of the preceding paragraph does not change it. Hence $W(E_{10})\subseteq\rho(\pi_1(\mcM^{\mathrm{cl}}_\Co,x))$, and this proves the equality.

*Families.* For a family over an arcwise connected, locally simply connected complex space, the transport of its system $\bM$ along a path carries the canonical class to the canonical class and the ample component to the ample component (@lem:coble-canonical-class-and-ample-component-in-families(4)); so its monodromy group lies in the group $G_S$ of that lemma, which a plane frame identifies with $W(E_{10})$ (@lem:coble-canonical-class-and-ample-component-in-families(2)). The final scope sentence is @prop:coble-stack-as-quotient and @rmk:coble-class-smooth-antinbicanonical: the presentation used is the classical substack only.
:::

::: {.proposition #prop:pi1-of-the-plane-model-quotient title="$\pi_1$ of the plane-model quotient: the atlas is not onto on $\pi_1$, and a monodromy group is generated by that of $\bar B$ and the transports of the arrows"}

Let $\varphi\colon\bar B\to\mcM^{\mathrm{cl}}_\Co$ be the smooth cover of @prop:coble-stack-as-quotient, $R$ its plane-model groupoid, and $s\in B$ a base point with images $[s]\in\bar B$ and $x=\varphi([s])=P(s)$. Let $\bL$ be one of the two local systems of lattices on $\mcM^{\mathrm{cl}}_\Co$, the system $\bM$ of invariant lattices (@lem:coble-invariant-lattice-in-families) or the system $\bT$ with fibre $T_\Co$ (@lem:d2-local-system), and let $\rho$ be the monodromy representation of $\pi_1(\mcM^{\mathrm{cl}}_\Co,x)$ on its fibre at $x$, read through the homomorphism $\rho(\omega)=T(\omega^{-1})$ of @lem:transport-order-on-the-classical-coble-stack(1), as in @thm:coble-monodromy-on-m-classical.

1. *The systems agree by pullback.* $\varphi^*\bL$ is the corresponding system of the family over $\bar B$, and its monodromy representation is $\rho^{\bar B}=\rho\circ\varphi_*$.
2. *$\varphi_*$ is not onto.* $\pi_1(\mcM^{\mathrm{cl}}_\Co,x)$ is generated by $\varphi_*\pi_1(\bar B,[s])$ and the elements $\lambda_r$ of the arrows $r$ of $R$ (@lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(3)), and $\varphi_*\pi_1(\bar B,[s])$ is a proper subgroup: for $\bL=\bM$ its image under $\rho$ lies in the finite group of the permutations of $e_1,\dots,e_{10}$, and $\rho\qty(\pi_1(\mcM^{\mathrm{cl}}_\Co,x))$ contains an element of infinite order.
3. *The image.* The monodromy group $\rho\qty(\pi_1(\mcM^{\mathrm{cl}}_\Co,x))$ is generated by the monodromy group $\rho^{\bar B}\qty(\pi_1(\bar B,[s]))$ of $\bar B$ and the transports $\rho(\lambda_r)$ of the arrows $r$ of $R$. It is the image of a representation, and $\rho^{\bar B}$ is trivial on $\ker\varphi_*$.
4. *Consequence for $\Gamma_\Co$.* The monodromy group of $\bT$ on the classical substack is generated by $\Gamma_\Co(\bar B)$ and the transports $\rho(\lambda_r)$ on $T_\Co$ of the arrows of $R$. A determination of that group from the monodromy of the labelled base or of the unlabelled base needs those transports as a further input.
:::

::: {.proof}

(1) The system on $\mcM^{\mathrm{cl}}_\Co$ is the descent of the system of the family over the base (@lem:d2-local-system, @lem:coble-invariant-lattice-in-families(4)), so its pullback along $\varphi$ is that system; transport along a loop of $\bar B$ is transport along its image loop (@lem:coble-family-base-change, whose argument uses only that the system is a pullback).

(2) The generation is @lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(3), which also identifies $\varphi_*\pi_1(\bar B,[s])$ with the subgroup generated by $P_*\pi_1(B,s)$ and the $\lambda_r$ of the relabelling arrows. For $\bL=\bM$ the representation $\rho$ is trivial on $P_*\pi_1(B,s)$, and it carries the $\lambda_r$ of the relabelling arrow $b\to\sigma b$ to the permutation of $e_1,\dots,e_{10}$ by $\sigma$: by @lem:transport-order-on-the-classical-coble-stack(2) the transport is $m(r)$ and $\rho(\lambda_r)=m(r)^{-1}$, and $m(r)$ is the permutation by $\sigma^{-1}$ of @thm:coble-monodromy-on-m-classical, *Generators and their transports*, which is the pushforward of the divisor at @lem:d2-unpolarised-family(3). So $\rho\qty(\varphi_*\pi_1(\bar B,[s]))$ lies in the group of those permutations, of order $10!$. The product $g=\sigma_I\sigma_J$ of two Bertini involutions is an automorphism of $S_s$ (@prop:coble-plane-model-comparison(2)). A lift of $g$ to the cover is an arrow $r$ of $R$ from $[s]$ to $[s]$ (@lem:pi1-of-a-groupoid-quotient-is-generated-by-three-contributions(1), (3)), and $\rho(\lambda_r)$ is the matrix of $g_*$ in the frame $H,E_1,\dots,E_{10}$, which has infinite order for the pair $I,J$ of @lem:coble-automorphism-group-is-infinite(2). Hence $\lambda_r\notin\varphi_*\pi_1(\bar B,[s])$.

(3) Apply $\rho$ to the generators of (2) and use (1). A loop in $\ker\varphi_*$ has trivial image class, and $\rho^{\bar B}=\rho\circ\varphi_*$.

(4) is (3) for $\bL=\bT$, with $\Gamma_\Co(\bar B)=\rho^{\bar B}\qty(\pi_1(\bar B,[s]))$ (@def:gamma-co-groups(1)).
:::

::: {.proposition #prop:gamma-co-on-the-coble-stack title="The statement for the classical substack, given the labelled result"}

Assume **(L)**: the labelled period map is fully faithful onto its image and the monodromy of the tautological system on that image is $\widetilde\Orth^+(T_\Co)$, so that the labelled monodromy is all of $\widetilde\Orth^+(T_\Co)$; this is the content of research#797's items 3 and 4, proved on that branch and not on this tree, and it contains the open equality of @thm:gamma-co-is-stable(2). Then the monodromy group of $\bT$ on $\mcM^{\mathrm{cl}}_\Co$ contains $\widetilde\Orth^+(T_\Co)$, and it is generated by $\Gamma_\Co(\bar B)$ and the transports $\rho(\lambda_r)$ of the arrows $r$ of the plane-model groupoid (@prop:pi1-of-the-plane-model-quotient(4)).
:::

::: {.proof}

The system of the labelled family is the pullback of $\bT$ along the map from the labelled stack to $\mcM^{\mathrm{cl}}_\Co$ that forgets the labels, so each transport of the labelled family is the transport of $\bT$ along the image loop (the argument of @prop:pi1-of-the-plane-model-quotient(1)). Hence the monodromy group of $\bT$ on $\mcM^{\mathrm{cl}}_\Co$ contains the labelled monodromy, which is $\widetilde\Orth^+(T_\Co)$ by (L). The generation is @prop:pi1-of-the-plane-model-quotient(4).
:::

::: {.lemma #lem:d2a-period-map title="The period map of the base is the map of Dolgachev--Kondo"}

Let $\per_B\colon B\to\bD(T_\Co)/\Orth(T_\Co)$ be the period map (@def:period-map) of the family of @def:coble-family-unpolarized: fix $s\in B$ and an isometry $\bT_s\iso T_\Co$, and send $b$ to the class of the isometry-induced image of $H^{2,0}(X_b)$ (@prop:lifted-period-map(4)). Then:

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
3. Consequently $\tilde h$ is the polarization vector (@def:polarization-vector) $h=e+f$ of [@AEGS25, Def. 2.5], $e,f$ the basis (@def:based-module) of $U(2)$ with $e^2=f^2=0$ and $e\cdot f=2$: the degree-$2$ numerical polarization $h_\Co$ of the Coble surface and the degree-$2$ polarization vector that [@AEGS25, Def. 2.5] fixes are the same vector of $S_\Co$, namely $f^*(h_\Co)$.
4. No automorphism $g$ of $X$ with $g\circ\iota'=\iota'\circ g$ has $H^2(X)^g=f^*(K_S^{\perp})$: the invariant lattice (@def:invariant_coinvariant_lattices) $S_\En$ is not the invariant lattice of an effective involution of $X$ commuting with $\iota'$, so the two degree-$2$ structures are compared through $f^*$ and not through a second involution of the same K3.
:::

::: {.proof}

(1) For a divisor class $x$ on $S$, $f^*(x)\cdot f^*(y)=2\,x\cdot y$ by the projection formula and $\deg f=2$. The image is $S_\Co\cong M$ by [@DK13, §3], where the classes $e_0,\dots,e_{10}$ of $f^*H,f^*E_1,\dots,f^*E_{10}$ generate it. Since $H\cdot K_S^{\perp}=0$, the image $f^*(K_S^{\perp})$ is orthogonal to $f^*H=e_0$; it has rank $10$ and $S_\Co$ has rank $11$, so it equals $e_0^{\perp}\cap S_\Co$. Its isometry class is that of $K_S^{\perp}(2)\cong E_{10}(2)=U(2)\oplus E_8(2)$ (@prop:canonical-perp-is-e10).
(2) is the computation of (1) applied to $F_1,F_2$: $F_i^2=0$ gives $(f^*F_i)^2=0$, and $F_1\cdot F_2=1$ gives $f^*F_1\cdot f^*F_2=2$; $h_\Co^2=(F_1+F_2)^2=2$ gives $\tilde h^2=4$.
(3) In $U(2)$ with basis $e,f$ one has $e^2=f^2=0$, $e\cdot f=2$ and $(e+f)^2=4$, which is (2) under the isometry $\generators{f^*F_1,f^*F_2}\cong U(2)$; the vector $h=e+f\in U(2)=S_{\dP}\subset S_\En$ is the one [@AEGS25, Def. 2.5] fixes as the polarization in both of its period problems, and $S_\En=U(2)\oplus E_8(2)$ is the lattice of (1).
(4) Put $M\definedas H^2(X)^{\iota'}=f^*H^2(S)$, of rank $11$. The class $[R]$ of the ramification curve $R\subset X$ of $f$ is $f^*(-K_S)$: indeed $f^*C_b=2R$ with $C_b=-2K_{S_b}$ (@lem:d2-unpolarised-family(1)), so $R=f^*(-K_S)$, $R^2=2(-K_S)^2=-2$, and $R\cdot f^*(K_S^{\perp})=2(-K_S)\cdot K_S^{\perp}=0$. Hence $f^*(K_S^{\perp})$ and $[R]$ are orthogonal sublattices of $M$ of ranks $10$ and $1$, and their ranks sum to $\mathrm{rk}M$, so they span $M$. An automorphism $g$ with $g\circ\iota'=\iota'\circ g$ preserves $M=H^2(X)^{\iota'}$, and $H^2(X)^g=f^*(K_S^{\perp})$ forces $g^*=-1$ on the orthogonal complement of $f^*(K_S^{\perp})$ in $M$, that is $g^*[R]=-[R]$. Since $H^2(X)$ is unimodular and $g$ is an involution, $g_*=(g^*)^{-1}=g^*$, so for the nef and big class $e_0=f^*H$ one has $(g^*e_0)\cdot R=e_0\cdot(g_*R)=e_0\cdot(-R)=-2\,H\cdot(-K_S)=-6<0$, while $R$ is an effective curve; so $g^*e_0$ is not nef, and $g^*$ cannot be induced by an automorphism, which carries the nef cone (@def:nef-cone) to itself.
:::

::: {.lemma #lem:d2b-polarization-is-a-class title="The degree-$2$ datum is a class: the decomposition is a case, not a definition"}

1. Let $X$ be an Enriques surface and $h\in E\definedas K_X^{\perp}\isoto U\oplus E_8$ a nef class (@def:nef-cone) with $h^2=2$. Then $h=F_1+F_2$ with $F_1,F_2$ nef, $F_i^2=0$, $F_1\cdot F_2=1$, or $h=2F_1+R$ with $F_1^2=0$ and $R$ a $(-2)$-curve [@CD89, Cor. 4.5.1], quoted in [@DK13, §7], where $h$ is called *non-degenerate* in the first case and *degenerate* otherwise.
2. In the degenerate case $F_1\cdot R=1$ and $h\cdot R=0$. In particular $h$ is not ample, and $X$ carries a $(-2)$-curve.
3. The dichotomy is stated for Enriques surfaces, and for Coble surfaces the source treats only the unnodal case, where by (2) the degenerate alternative cannot occur [@DK13, §8]. A moduli problem of degree-$2$ polarized Coble surfaces therefore does not have the nondegenerate decomposition available as a definition, and the datum is the class: a nef $h_\Co\in K_S^{\perp}$ with $h_\Co^2=2$ (@def:coble-polarization-classes(2), and item 2 of @def:coble-family-degree-two).
4. The degenerate locus of the base of @def:coble-family-unpolarized is not empty: at a point whose sextic has three collinear nodes, the proper transform (@def:strict-transform) of the line through them is a $(-2)$-curve with class $R=H-E_1-E_2-E_3\in K_S^{\perp}$ (@lem:d2-s10-not-free).
:::

::: {.proof}

(1) is the cited dichotomy, in the form in which [@DK13, §7] states it.

(2) By (1) $h=2F_1+R$ with $F_1^2=0$ and $R^2=-2$, so
$$h^2=4F_1\cdot R+R^2=4F_1\cdot R-2=2,\qquad h\cdot R=2F_1\cdot R+R^2=2F_1\cdot R-2,$$
hence $F_1\cdot R=1$ and $h\cdot R=0$. Since $R$ is an effective curve meeting $h$ in $0$, $h$ is not ample. The deposited extraction of [@DK13, §7] prints $F_1\cdot R=0$ at this point, which with $R^2=-2$ gives $h^2=-2$; the two displayed equations are what the stated hypotheses $h^2=2$ and $R^2=-2$ force, and they are what is used below. The arithmetic is verified on the lattice $E$ by `computations/reports/coble_787-degenerate-polarization.py`, recorded in `computations/reports/coble_787-degenerate-polarization-run.txt`.

(3) is a statement about the two cited sources: the dichotomy of (1) is [@CD89, Cor. 4.5.1] for Enriques surfaces, and the Coble case is treated in [@DK13, §8] under the hypothesis that $S$ has no $(-2)$-curve, which by (2) excludes the degenerate alternative. Nothing read supplies the dichotomy for a nodal Coble surface, so a definition that required the nondegenerate decomposition would exclude a case that no theorem excludes.

(4) Let $p_1,p_2,p_3$ be collinear nodes and $L$ the line they span. Since $L$ is a line and $\deg Z=6$, $L$ is not a component of $Z$, so its proper transform is a curve $R\subset S$ with class $H-E_1-E_2-E_3$; then $R^2=1-3=-2$ and $R\cdot K_S=-3+3=0$, so $R$ is a $(-2)$-curve with class in $K_S^{\perp}$. The sextic of @lem:d2-s10-not-free has exactly three nodes on the line $z=0$; the computation cited in (2) verifies that the three are collinear and that $R^2=-2$ and $R\cdot K_S=0$.
:::

::: {.remark #rmk:d2b-decomposition-locus title="Where the degree-$2$ class decomposes"}

For the family of @def:coble-family-degree-two the polarization is a class and not a decomposition (@lem:d2-degree-two-polarization(2), @lem:d2b-polarization-is-a-class). On the locus where $h_{\Co,y}$ is nondegenerate it splits as $F_1+F_2$ with $F_i$ nef and $F_i^2=0$, and then $\tilde h_y=f^*F_1+f^*F_2$ is the vector $h=e+f$ of [@AEGS25, Def. 2.5] (@lem:d2-degree-two-polarization(3), @lem:d2b-polarization-is-a-class(2)); on the degenerate locus it does not (@lem:d2b-polarization-is-a-class(3)), and that case is part of that moduli problem.
:::

::: {.definition #def:coble-family-degree-two title="D2b: the family of degree-$2$ polarized Coble surfaces" defines="degree-$2$ polarized Coble surface; $\Delta_2$"}

**The objects.** Over a complex space $Y$, an object is a tuple $\qty{\mcs\to Y,\ \mcx\to\mcs,\ \tilde h}$ in which

1. $\mcs\to Y$ is an object of @def:coble-family-unpolarized, with its K3 double cover $\mcx\to\mcs$ and involution $\iota$;
2. $\tilde h$ is a global section of the local system of lattices $f^*(K^\perp)$ of @lem:d2-degree-two-polarization(1) whose value at every $y\in Y$ is the pullback $\tilde h_y=f^*h_{\Co,y}$ of a nef class (@def:nef-cone) $h_{\Co,y}\in K_{S_y}^{\perp}$ with $h_{\Co,y}^2=2$: a degree-$2$ numerical polarization in the sense of @def:coble-polarization-classes(2).

The section is part of the objects and is not a marking: it is the polarization.

**The fibres** are the Coble surfaces $S_y$ of @def:coble-family-unpolarized with their degree-$2$ numerical polarization $h_{\Co,y}$; the K3 cover $X_y$ is a K3 surface with a marked class $\tilde h_y$ of square $4$.

**The local system of lattices** is $\bT$ of @lem:d2-local-system, the orthogonal complement of $\bM$ in $R^2f_*\underline\ZZ_\mcx$ modulo torsion; the polarization is a section of $\bM$, so $\bT$ is the same system for the polarized and the unpolarized family, and its fibre is $T_\Co$.

:::

::: {.lemma #lem:d2-degree-two-base title="The period image of the degree-$2$ family is all of $\Delta_2$, up to normalization"}

Let $R_{\gent}$ be the restricted stabilizer (@def:group-orbit) of @def:gamma-co-groups and $\Gamma_{\tilde h}$ the group (@def:group) of pairs of type $\tilde h$ of @prop:coble-polarized-moduli, and $\Delta_2=\mch_{-2}/\gent\subset\fentwo=\bD(\ten)/\gent$.

1. $\Gamma_{\tilde h}=R_{\gent}$ [@prop:coble-degree-two-space(2)], so $\bD(T_\Co)/\Gamma_{\tilde h}=\bD(T_\Co)/R_{\gent}$ is the moduli space of pairs $(S,h_\Co)$ of @def:coble-family-degree-two and, by @thm:normalization with $\Gamma=\gent$, it is the normalization of $\Delta_2$: the map $\bD(T_\Co)/R_{\gent}\to\fentwo$ is finite, its image is $\Delta_2$, and it is birational.
2. Hence $\Delta_2$ is the image of the period map of @def:coble-family-degree-two up to normalization, and no proper sublocus of $\Delta_2$ contains it: the period map of the family lands in $\bD(T_\Co)/\Gamma_{\Co,2}\to\bD(T_\Co)/R_{\gent}$, and the composite with $\bD(T_\Co)/R_{\gent}\to\Delta_2\hookrightarrow\fentwo$ is finite and surjective by (1).
3. $\Gamma_{\Co,2}\leq R_{\gent}\cap\Orth^+(T_\Co)$.
4. $\Delta_2$ is irreducible.
:::

::: {.proof}

(1) The first identity is [@prop:coble-degree-two-space(2)], whose proof identifies the stabilizer of $\tilde h$ in the isometries of $\lkt$ preserving $S_\Co$ with the image of $\Stab_{\gent}(\delta)$ in $\Orth(T_\Co)$. The moduli interpretation is @prop:coble-polarized-moduli(2)--(3): the period of a pair of type $\tilde h$ is well defined in $\bD(T_\Co)/\Gamma_{\tilde h}$, two Picard-general (@def:picard-general-coble) pairs are isomorphic exactly when their periods agree, and every point of the fibre of $\bD(T_\Co)/\Gamma_{\tilde h}\to\bD(T_\Co)/\Orth(T_\Co)$ is the period of such a pair. The remaining statements are @thm:normalization with $\Gamma=\gent$, whose three hypotheses are its own: $R_{\gent}$ is the image of $\Stab_{\gent}(\delta)$ (@prop:gamma-co-images(3)), $T_\Co=\delta^{\perp\ten}$, and $\bD(T_\Co)/R_{\gent}$ is normal.
(2) A moduli problem whose marked period space is the normalization of a variety has that variety as its coarse space up to normalization; the composite $\bD(T_\Co)/R_{\gent}\to\Delta_2\hookrightarrow\fentwo$ is finite and surjective by (1), so its image is all of $\Delta_2$ and not a proper sublocus.
(3) A monodromy operator of the family of @def:coble-family-degree-two preserves the local system $\bM$ of @lem:d2-local-system(2) and its section $\tilde h$, so its image in $\Orth(T_\Co)$ is the restriction of an isometry $\gamma$ of $\lkt$ with $\gamma(S_\Co)=S_\Co$ and $\gamma(\tilde h)=\tilde h$, that is an element of $\Gamma_{\tilde h}=R_{\gent}$; and it lies in $\Orth^+(T_\Co)$ by @lem:d2-labelled-base-monodromy.
(4) $\Delta_2$ is the image of the irreducible $\bD(T_\Co)$ under a finite morphism, hence irreducible; equivalently $\gent$ is transitive on the $(-2)$-vectors of $\ten$ [@Ste91, (2.10) and the paragraph after it].
:::

::: {.lemma #lem:d2b-forgets-to-d2a title="The degree-$2$ family is the unpolarized family with a flat section, and $\Delta_2$ is its period image"}

Let $Y$ be a connected complex space, $y\in Y$, and let $\qty{\mcs\to Y,\ \mcx\to\mcs,\ \iota,\ \tilde h}$ be an object of @def:coble-family-degree-two.

1. Dropping $\tilde h$ leaves an object of @def:coble-family-unpolarized over the same $Y$, with the same K3 cover, the same $\iota$ and the same local system $\bT$ of @lem:d2-local-system. Hence the two monodromy representations $\pi_1(Y,y)\to\Orth(T_\Co)$ coincide, and the monodromy group of a degree-$2$ family over $Y$ is the monodromy group of the underlying unpolarized family.
2. The underlying unpolarized family is the pullback of the family of @lem:d2-unpolarised-family along a morphism $Y\to\bar B$ classifying it, so
$$
\rho\qty{\pi_1(Y,y)}\subseteq\rho\qty{\pi_1(\bar B,p(y))}=\Gamma_\Co(\bar B),
$$
and in particular $\Gamma_{\Co,2}\subseteq\Orth^+(T_\Co)$.
3. Read as the orbifold $\bD(T_\Co)/R_{\gent}$ of @lem:d2-degree-two-base(1), $\Delta_2$ carries no family of Coble surfaces whose local system is the tautological one: the tautological system has monodromy $\varphi(R_{\gent})=R_{\gent}$ for the defining action $\varphi\colon R_{\gent}\injects\Orth(T_\Co)$ (@lem:orbifold-monodromy-of-a-nonfree-quotient(2) for the transports per loop, and the descent along the $2$-morphisms for the reading of them as the monodromy of a local system on the quotient, @rmk:the-descent-stops-at-the-2-morphisms, research#797, item 4), and $R_{\gent}$ contains $s_\zeta\notin\Orth^+(T_\Co)$ (@thm:coble-monodromy-versus-enriques(2)), whereas the monodromy of every family of Coble surfaces lies in $\Orth^+(T_\Co)$ (@lem:monodromy-is-spinor-positive).
4. Hence the two bases are compared by the forgetful morphism of (1)--(2) and by the period maps
$$
\bD(T_\Co)/\Gamma_{\Co,2}\too\bD(T_\Co)/R_{\gent}\too\fentwo ,
$$
and not by an identification: the marked period space of the degree-$2$ family is $\bD(T_\Co)/\Gamma_{\Co,2}$, and $\Delta_2$ is its image under the quotient by $R_{\gent}$.
:::

::: {.proof}

(1) is the first item of @def:coble-family-degree-two: an object of that definition consists of an object $\mcs\to Y$ of @def:coble-family-unpolarized together with the section $\tilde h$. The local system $\bT$ of @lem:d2-local-system is built from $\mcx\to\mcs\to Y$ and the eleven relative divisors alone, so it is the same local system for the two structures, and transport along a loop of $Y$ (@def:transport-and-monodromy) is computed from $\bT$ alone; hence the two monodromy representations are the same map.

(2) By @lem:d2a-moduli-stack, $\bar B$ is the moduli stack of the objects of @def:coble-family-unpolarized, so the underlying object is the pullback of the universal family along a morphism $p\colon Y\to\bar B$. The argument of @lem:coble-family-base-change applies with the stack $\bar B$ in place of the space $B$: the pullback is trivialized over the inverse image of a trivializing open set of the universal family, and transport along a loop $\gamma$ of $Y$ is transport along $p\circ\gamma$, both being read on sections over the interval (@def:transport-and-monodromy). So the monodromy group is the image of $p_*\pi_1(Y,y)$ in that of $\bar B$, which is the display. The inclusion in $\Orth^+(T_\Co)$ is @lem:monodromy-is-spinor-positive applied to the underlying family, whose periods lie in one component because $Y$ is connected.

(3) By @lem:orbifold-monodromy-of-a-nonfree-quotient(2), applied to the defining action $\varphi\colon R_{\gent}\injects\Orth(T_\Co)$ on $T_\Co$, which is injective, the per-loop transport of the tautological system of $\bD(T_\Co)/R_{\gent}$ is $\varphi\circ\psi^{-1}$, so the image is $\varphi(R_{\gent})=R_{\gent}$; calling that the monodromy of a local system on the quotient is the descent named in the statement and is research#797, item 4. By @thm:coble-monodromy-versus-enriques(2) there is a primitive $\zeta\in T_\Co$ of square $2$ with $s_\zeta\in R_{\gent}$ and $s_\zeta\notin\Orth^+(T_\Co)$. A family of Coble surfaces over that orbifold with the tautological system as its $\bT$ would have monodromy group $R_{\gent}$ by (1), against @lem:monodromy-is-spinor-positive, which puts the monodromy of every Coble family in $\Orth^+(T_\Co)$.

(4) By (1) and (2) the forgetful morphism and the period maps are the only comparison available. The period map of the degree-$2$ family lands in $\bD(T_\Co)/\Gamma_{\Co,2}$ by the definition of $\Gamma_{\Co,2}$ as the monodromy group (@def:gamma-co-groups(5), @eq-period-map-equivariance), and the second arrow is the quotient by the subgroup $R_{\gent}$ of @lem:d2-degree-two-base(1); the composite is finite with image $\Delta_2$ (@lem:d2-degree-two-base(2)). Since $\Gamma_{\Co,2}\subseteq\Orth^+(T_\Co)$ by (2) and $s_\zeta\in R_{\gent}$ lies outside $\Orth^+(T_\Co)$, $\Gamma_{\Co,2}\neq R_{\gent}$, which is @thm:coble-monodromy-versus-enriques(3); so the first arrow is not an isomorphism and $\Delta_2$ is the image, not the marked space.
:::

::: {.remark #rmk:d2b-base-and-group title="The base and the group of D2b"}

The base of a family of @def:coble-family-degree-two carries the underlying unpolarized family and maps to $\bar B$ (@lem:d2b-forgets-to-d2a(1)--(2)). The base is compared with the D2a base through that forgetful morphism and the period maps, and its marked period space is $\bD(T_\Co)/\Gamma_{\Co,2}$; the divisor $\Delta_2\subset\fentwo$, the image of the hyperplanes $\alpha^{\perp}$ for $\alpha\in\ten$ a $(-2)$-vector, is the image of that period space under the quotient by $R_{\gent}$ (@lem:d2-degree-two-base(2), @lem:d2b-forgets-to-d2a(4)) and not the marked space itself.

The group $\Gamma_{\Co,2}$ is a subgroup of $\Orth^+(T_\Co)$, unconditionally, because a family of @def:coble-family-degree-two forgets to a family of Coble surfaces (@lem:d2b-forgets-to-d2a(1)--(2)); the further containment in the restricted stabilizer (@def:group-orbit) $R_{\gent}$ is @lem:d2-degree-two-base(3).
:::

::: {.lemma #lem:d2b-family-over-the-labelled-base title="A family of degree-$2$ polarized Coble surfaces over the labelled base"}

Let $b=(Z;p_1,\dots,p_{10})\in V$ and, for each label $i$, let $C_i\subset\PP^2$ be the cubic through the nine nodes other than $p_i$, with class $F_i=3\varepsilon_0-\sum_{k\neq i}\varepsilon_k$ in the local system $\bM$ of @lem:d2-local-system(2).

1. $F_i^2=0$ and $F_i\cdot K_S=0$; $F_i$ is nef on the locus where $C_i$ is irreducible.
2. For $i\neq j$ the class $h_{ij}\definedas F_i+F_j$ is primitive, nef, of square $2$, and lies in $K_S^{\perp}$; hence $(S_b,h_{ij})$ is a degree-$2$ polarized Coble surface in the sense of @def:coble-polarization-classes(2) and @lem:d2b-polarization-is-a-class.
3. The classes $F_i$ are values of global sections of $\bM$, so the $\tilde h_{ij}\definedas f^*h_{ij}$ are flat sections of the local system $f^*(K^{\perp})$ and $(\mcs_V\to V,\ \mcx_V\to\mcs_V,\ \iota_V,\ \tilde h_{ij})$ is an object of @def:coble-family-degree-two over $V$, descending to the labelled base $B$.
4. Its monodromy group is that of the underlying unpolarized family (@lem:d2b-forgets-to-d2a(1)), namely $\Gamma_\Co(B)$, which lies in $\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)). Of the two comparisons with $\Gamma_{\Co,2}$, one is unconditional and one is not: $\Gamma_{\Co,2}\subseteq\Gamma_\Co(\bar B)$ by @lem:d2b-forgets-to-d2a(2), while $\Gamma_\Co(B)\subseteq\Gamma_{\Co,2}$ is *not* asserted here, because its recorded proof passes through $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$, which is @qst:gamma-co-sign-is-realised and is open (@qst:sextic-group-comparison).
5. The period map of this family lands in $\bD(T_\Co)/\Gamma_{\Co,2}$ and its composite with the quotient to $\bD(T_\Co)/R_{\gent}$ has open image, since the period map of the underlying family is an isomorphism onto an open subset (@lem:d2a-period-map(3)). So the family is a family of degree-$2$ polarized Coble surfaces over the open part of the normalization of $\Delta_2$ (@lem:d2-degree-two-base(1)).
:::

::: {.proof}

(1) The class of the proper transform of $C_i$ is $3\varepsilon_0-\sum_{k\neq i}\varepsilon_k$; its square is $9-9=0$ and its intersection with $K_S=-3H+\sum_kE_k$ is $-9+9=0$. An irreducible curve meets every effective divisor it does not contain in a nonnegative number, and its own self-intersection is $0$, so its class is nef; hence $F_i$ is nef wherever $C_i$ is irreducible, which is an open condition on $V$.

(2) $F_i\cdot F_j=9-8=1$ for $i\neq j$, so $h_{ij}^2=0+2\cdot1+0=2$, and $h_{ij}\cdot K_S=0+0=0$. The coefficient vector has a coordinate $1$ at $E_i$ and at $E_j$, so it is primitive. Nef is the sum of two nef classes. The identification of $(S_b,h_{ij})$ with a degree-$2$ polarized Coble surface is @def:coble-polarization-classes(2) together with the class reading of @lem:d2b-polarization-is-a-class(3).

(3) The eleven classes $\varepsilon_0,\dots,\varepsilon_{10}$ are values of global sections of $\bV$ (@lem:d2-local-system(2)), so $F_i$ is a global section of $\bM$ and $\tilde h_{ij}$ one of $f^*(K^{\perp})$; the family is @lem:d2-unpolarised-family(2) with the section added, and it descends to $B$ by @lem:d2-unpolarised-family(3).

(4) By @lem:d2b-forgets-to-d2a(1) the monodromy group of the family is that of the underlying unpolarized family, which is $\Gamma_\Co(B)=\rho(\pi_1(B,s))$ (@def:gamma-co-groups(1)); it lies in $\widetilde\Orth^+(T_\Co)$ by @thm:gamma-co-is-stable(1) and not by an equality, which is @qst:gamma-co-sign-is-realised. By @lem:d2b-forgets-to-d2a(2) the monodromy group of any degree-$2$ family is contained in $\Gamma_\Co(\bar B)$. Those are the two bounds of the statement; the bound $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$ is not one of them, and would need the equality.

(5) The period map of a degree-$2$ family is the map of its underlying unpolarized family, which is an isomorphism onto an open subset of $\bD(T_\Co)/\Orth(T_\Co)$ (@lem:d2a-period-map(3)); its lift to $\bD(T_\Co)/\Gamma_{\Co,2}$ is therefore a homeomorphism onto an open subset, and the image under the quotient by $R_{\gent}\supseteq\Gamma_{\Co,2}$ is open in $\bD(T_\Co)/R_{\gent}$, whose quotient by $R_{\gent}$ is the normalization of $\Delta_2$ (@lem:d2-degree-two-base(1)). The computation `computations/reports/coble_787-explicit-d2b-family.py`, recorded in `computations/reports/coble_787-explicit-d2b-family-run.txt`, verifies items (1)--(3) for all $90$ ordered pairs of labels.
:::

::: {.proposition #prop:d2b-base-covers-delta title="$\Delta_2$ is a proper quotient of the base of the degree-$2$ family"}

Assume $\Gamma_{\Co,2}\subseteq R_{\gent}$ (@lem:d2-degree-two-base(3)).

1. $\Gamma_{\Co,2}\subsetneq R_{\gent}$, and the map
$$
\bD(T_\Co)/\Gamma_{\Co,2}\too\bD(T_\Co)/R_{\gent}
$$
of the marked period space of @def:coble-family-degree-two onto the normalization of $\Delta_2$ (@lem:d2-degree-two-base(1)) is a covering of degree $[R_{\gent}:\Gamma_{\Co,2}]\geq 2$. No finiteness of that degree is asserted without the additional inclusion $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$ of @prop:d2b-index-exact(2).
2. Hence $\Delta_2$ is not the base of the degree-$2$ family, but a proper quotient of it: two marked periods in the same $R_{\gent}$-orbit and in different $\Gamma_{\Co,2}$-orbits have the same image in $\Delta_2$ and different monodromy markings.
3. The base itself is the moduli of degree-$2$ polarized Coble surfaces, over which the family exists (@lem:d2b-family-over-the-labelled-base(3)), and the number $[R_{\gent}:\Gamma_{\Co,2}]$ is the degree of the map from the base to $\Delta_2$.
:::

::: {.proof}

(1) By @lem:d2b-forgets-to-d2a(2) every element of $\Gamma_{\Co,2}$ lies in $\Orth^+(T_\Co)$, and by @thm:coble-monodromy-versus-enriques(2) the group $R_{\gent}$ contains an element outside $\Orth^+(T_\Co)$. So $\Gamma_{\Co,2}\neq R_{\gent}$, and with the hypothesis $\Gamma_{\Co,2}\subsetneq R_{\gent}$. The quotient map of a domain by a subgroup is a covering of that index, proper here because the subgroup is strict. Under the additional inclusion $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$, @prop:d2b-index-exact(2) makes the index finite; without it no finiteness is asserted.

(2) The marked period space of the family is $\bD(T_\Co)/\Gamma_{\Co,2}$ by the definition of $\Gamma_{\Co,2}$ as the monodromy group (@def:gamma-co-groups, @eq-period-map-equivariance), and $\bD(T_\Co)/R_{\gent}$ is the normalization of $\Delta_2$ (@lem:d2-degree-two-base(1)). Points of $\bD(T_\Co)$ in one $R_{\gent}$-orbit but in different $\Gamma_{\Co,2}$-orbits are the marked periods of the same point of $\Delta_2$ and of different points of the base; such pairs exist by (1).

(3) The existence of the family over the moduli base is @lem:d2b-family-over-the-labelled-base(3) together with @lem:d2b-forgets-to-d2a(1)--(2), and the degree of the induced map from the base to the normalization of $\Delta_2$ is the index of (1).
:::

::: {.proposition #prop:d2b-index-exact title="The index $[R_{\gent}:\Gamma_{\Co,2}]$, exactly"} 

Assume $\Gamma_{\Co,2}\subseteq R_{\gent}$ (@lem:d2-degree-two-base(3)), and in (2)--(4) in addition $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$, which is open and not proved: the recorded argument for it passes through $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$ (@qst:gamma-co-sign-is-realised) together with $\Gamma_\Co(B)\subseteq\Gamma_{\Co,2}$, and @lem:d2b-family-over-the-labelled-base(4) asserts neither. Then

1. $[R_{\gent}:R_{\gent}\intersect\Orth^+(T_\Co)]=2$ and $[R_{\gent}\intersect\Orth^+(T_\Co):\widetilde\Orth^+(T_\Co)]=\abs{P}=696\,729\,600$, so
$$
[R_{\gent}:\widetilde\Orth^+(T_\Co)] = 2\abs{P} = 1\,393\,459\,200 .
$$
2. If, in addition, $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}$, then
$$
[R_{\gent}:\Gamma_{\Co,2}] = \frac{2\abs{P}}{[\Gamma_{\Co,2}:\widetilde\Orth^+(T_\Co)]} = \frac{1\,393\,459\,200}{[\Gamma_{\Co,2}:\widetilde\Orth^+(T_\Co)]}.
$$
That additional inclusion is open: its recorded proof would use $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$, which is @qst:gamma-co-sign-is-realised (@lem:d2b-family-over-the-labelled-base(4)).
3. Under the same additional inclusion,
$$
\widetilde\Orth^+(T_\Co)\subseteq\Gamma_{\Co,2}\subseteq\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1},
$$
so
$$
384\ \leq\ [R_{\gent}:\Gamma_{\Co,2}]\ \leq\ 1\,393\,459\,200,
$$
with $[R_{\gent}:\Gamma_{\Co,2}]=384$ if and only if $\Gamma_{\Co,2}=\Gamma_{10A_1}$.
4. Unconditionally, @prop:coble-monodromy-equality-false(4) gives $[R_{\gent}:\Gamma_{\Co,2}]\geq384$. Under the additional inclusion of (2), the index is finite and is determined by the single unknown $[\Gamma_{\Co,2}:\widetilde\Orth^+(T_\Co)]$, a divisor of $10!$ by (3); without that inclusion, finiteness and the upper bound are open.
:::

::: {.proof}

(1) The first index is @thm:coble-monodromy-versus-enriques(2). For the second, $R_{\gent}=\bar\rho^{-1}(P)$ (@prop:gamma-co-images(3)) and $\widetilde\Orth^+(T_\Co)=\Orth^+(T_\Co)\intersect\ker\bar\rho$ (@def:gamma-co-groups), so
$$R_{\gent}\intersect\Orth^+(T_\Co) = \Orth^+(T_\Co)\intersect\bar\rho^{-1}(P),$$
and the index of this in $\Orth^+(T_\Co)$ over $\widetilde\Orth^+(T_\Co)$ is $\abs{\bar\rho(\Orth^+(T_\Co))\intersect P}$. The map $\bar\rho\colon\Orth^+(T_\Co)\to\Orth(q_{T_\Co})$ is onto: $[\Orth^+(T_\Co):\widetilde\Orth^+(T_\Co)]=\abs{\Orth(q_{T_\Co})}$ by @thm:gamma-co-sextic-group(3), whose two factors $[\Orth^+:\Gamma_{10A_1}]=\abs{\Orth(q)}/10!$ and $[\Gamma_{10A_1}:\widetilde\Orth^+]=10!$ multiply to $\abs{\Orth(q)}$. Hence the intersection is $P$ and the index is $\abs{P}=\abs{\Orth(q_{T_\Co})}/[\Orth(q_{T_\Co}):P]=\abs{\Orth(q_{T_\Co})}/(2^7\cdot17\cdot31)$, the second factor being the arithmetic of @prop:gamma-co-images(3). The value $\abs{P}=696\,729\,600$ is the quotient of the two displayed numbers, computed in `computations/reports/coble_787-index-of-gamma-co-2.py` and its run record.

(2) assumes the additional inclusion, so the chain $\widetilde\Orth^+\subseteq\Gamma_{\Co,2}\subseteq R_{\gent}\intersect\Orth^+\subseteq R_{\gent}$ exists, and multiplicativity with (1) gives the formula.

(3) also assumes the additional inclusion, which is what @lem:d2b-family-over-the-labelled-base(4) leaves open; $\Gamma_{\Co,2}\subseteq\Gamma_\Co(\bar B)$ is @lem:d2b-forgets-to-d2a(2); $\Gamma_\Co(\bar B)\subseteq\Orth^+(T_\Co)$ is @lem:monodromy-is-spinor-positive and $\bar\rho(\Gamma_\Co(\bar B))\subseteq\Theta$ is @prop:gamma-co-geometric-bound(2), so $\Gamma_\Co(\bar B)\subseteq\Orth^+(T_\Co)\intersect\bar\rho^{-1}(\Theta)=\Gamma_{10A_1}$ (@thm:gamma-co-sextic-group(2)); and $[\Gamma_{10A_1}:\widetilde\Orth^+]=10!$ is @thm:gamma-co-sextic-group(3). Dividing $2\abs{P}$ by an index between $1$ and $10!$ gives the display, the lower end at $10!$ and the upper at $1$.

(4) The lower bound is @prop:coble-monodromy-equality-false(4), whose containment is supplied independently by @lem:d2-degree-two-base(3). Under the additional inclusion, (2) determines the index by $[\Gamma_{\Co,2}:\widetilde\Orth^+(T_\Co)]$ alone, and (3) bounds that unknown between $1$ and $10!$; no statement read fixes it. This is the comparison with the polarized group posed in @qst:sextic-group-comparison: (1) is unconditional arithmetic, (2)--(3) are conditional on the additional inclusion, and what that question still asks is the index $[\Gamma_{10A_1}:\Gamma_{\Co,2}]$ and, without it, finiteness and the upper bound.
:::

::: {.remark #rmk:d2b-index-not-the-reverse-inclusion title="The unknown index is not the reverse inclusion"}

The index of @prop:d2b-index-exact(4) is not the reverse inclusion of @qst:coble-monodromy-equality, which is false (@prop:coble-monodromy-equality-false): that inclusion would put $\Gamma_{\Co,2}$ at $R_{\gent}\intersect\Orth^+(T_\Co)$, of index $2^7\cdot17\cdot31$ in $\Orth^+(T_\Co)$, whereas what is unknown here is the index of $\Gamma_{\Co,2}$ in $\Gamma_{10A_1}$, of index $2^{13}\cdot3\cdot17\cdot31$; the two differ because $R_{\gent}\intersect\Orth^+(T_\Co)$ is not contained in $\Gamma_{10A_1}$ (@prop:coble-monodromy-equality-false(2)).
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

1. **The coarse space and the family.** $M_\Co$ is a coarse space and carries no family; the family of D2a lives over $B$, which is what @lem:d2-unpolarised-family(3) and @lem:d2-labelled-base-monodromy construct. Nothing here claims a universal family over $M_\Co$, and none exists: a Coble surface with nontrivial automorphism acting nontrivially on $T_\Co$ has no universal family over the coarse space. The local system over $M_\Co$ is accordingly not defined, and statements about $\Gamma_\Co$ are statements about the labelled base $B$.
2. **The comparison of the bases.** $B\to\bar B$ is the principal $S_{10}$-bundle of stacks of @lem:d2-labelling-cover, with coarse space $V/(\SL_3\times S_{10})$ over $B$, and $\bar B\to M_\Co$ forgets the sextic; whether the second is birational, that is whether a ten-nodal sextic is determined by its ten nodes, is settled: in a fixed plane it is, by the Bézout count, and the map to the moduli of surfaces is not injective, because a Coble surface has several plane models (@prop:coble-plane-model-comparison(1) and (3)). What is proved is that the labelled base has group $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ and the unlabelled one $\Gamma_\Co(\bar B)\subseteq\Gamma_{10A_1}$, with $[\Gamma_\Co(\bar B):\Gamma_\Co(B)]=10!$ and $[\Gamma_{10A_1}:\widetilde\Orth^+(T_\Co)]=10!$ (@thm:gamma-co-is-stable(1), @lem:gamma-co-labelled-index, @thm:gamma-co-sextic-group(3)--(4)); both inclusions are open as equalities, at @qst:gamma-co-sign-is-realised.
3. **The reverse inclusion for the degree-$2$ family.** @lem:d2-degree-two-base(3) gives $\Gamma_{\Co,2}\leq R_{\gent}\cap\Orth^+(T_\Co)$. The equality is @qst:coble-monodromy-equality and is false (@prop:coble-monodromy-equality-false); nothing in this section asserts it.
4. **Ample against nef.** [@AEGS25, §1] asks for an *ample* numerical polarization of degree $2$, whereas the degree-$2$ polarized Coble moduli space is defined with a *nef* class of square $2$ [@DK13, §7], called an almost polarization in [@Ste91, §2]. The two conditions differ on the boundary of the cone of curves: $h=F_1+F_2$ with $F_1,F_2$ nef is nef and big on a Picard-general surface (@prop:coble-degree-two-space(1)) but the degenerate split $h=2F_1+R$ with $R$ a $(-2)$-curve is not ample [@DK13, §7]. The base $\Delta_2$ of @def:coble-family-degree-two is the arithmetic divisor and needs neither adjective.
5. **The compactification.** Both definitions are stated over the open base. Their extensions over the boundary, and which boundary strata are Coble, are not part of D2 and are not asserted.
:::

::: {.remark #rmk:d2-corrections title="What this section corrects"}

Five corrections to the earlier form of this section, each at its file and line in the commit that introduces this remark.

1. *The family is constructed, not declared.* The earlier definition listed three bases and called the choice part of the definition, while the base named for $\Gamma_\Co$ carried no family; @lem:d2-unpolarised-family now constructs the family and @lem:d2-local-system its local system, and the group is the monodromy of that system.
2. *The labels are a torsor of stacks, not a principal bundle of coarse spaces.* The finite-cover statement, formerly introduced without proof, is @lem:d2-labelling-cover, which proves the torsor statement for the quotient stacks and records that the induced map of coarse spaces is not a covering.
3. *The degree-$2$ object is the Coble polarization.* The earlier definition took an ample degree-$2$ class on the Enriques quotient instead of the class $h_\Co\in K_S^{\perp}$ of @def:coble-polarization-classes(2); @lem:d2-degree-two-polarization proves that the two are the same class on the K3 cover, so the definition can and now does use the Coble class, which is the one @def:gamma-co-groups names.
4. *The base is $\Delta_2$ by normalization, not by inheritance.* The earlier proof applied the pointwise description of the divisor in the full quotient $\bD(\ten)/\Orth(\ten)$ through the finite map $\fentwo\to\bD(\ten)/\Orth(\ten)$ in the wrong direction; @lem:d2-degree-two-base now identifies the two period spaces directly, through @thm:normalization and @prop:coble-degree-two-space(2).
5. *The label cover is a torsor of stacks, and the reverse inclusion is not proved.* The earlier proof of $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_\Co$ applied a period map $\per_M\colon V\to\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ and asserted that it is injective; it is not, since $\PGL_3$-orbits in $V$ give isomorphic $M$-marked K3 covers. The earlier form of @lem:d2-labelling-cover then asserted a principal $S_{10}$-bundle of the coarse spaces $B\to\bar B$, which need not be a covering: a projectivity carrying a sextic to itself and permuting its nodes identifies two points of $B$ over one point of $\bar B$. @lem:d2-labelling-cover now proves the torsor statement for the quotient stacks, and @lem:d2-label-lift proves the fundamental-group sequence from the connectedness of $B$ (@lem:d2-incidence-connected). What those give is the kernel identity $\Gamma_\Co(B)=\Gamma_\Co(\bar B)\cap\ker\bar\rho$ and the index $\abs{\bar\rho(\Gamma_\Co(\bar B))}$, which is $10!$ (@lem:gamma-co-labelled-index); they do not give the reverse inclusion, which is open (@thm:gamma-co-is-stable, @qst:gamma-co-sign-is-realised).
:::

## Quotient-stack presentations and monodromy {#sec-quotient-stack-presentations}

Research#797 asks, as its items 3 and 4, for two statements: that the moduli stack of lattice-polarized $\mathrm{K3}$ surfaces is a quotient stack of the period domain, and that the monodromy of a local system on a stack is the quotient of its fundamental group that the exact sequence records. This section states both, checks the hypotheses against the numbered statements of the sources, and says where a source stops short.

### Item 3: the quotient-stack presentation

*The data.* Let $M$ be an even lattice of signature $(1,t)$ with $t\leq19$ and a primitive embedding $M\injects L$ into the $\mathrm{K3}$ lattice, and put $N=M^{\perp L}$, of signature $(2,19-t)$ [@Dol96, §3]. Let $\bD_M$ be the period domain of [@Dol96, §3], the set of positive oriented $2$-planes in $N_\RR$, which has two connected components; let $\Delta(N)=\theset{\delta\in N:\delta^2=-2}$ and let $\bD^\circ_M\definedas\bD_M\setminus\bigcup_{\delta\in\Delta(N)}H_\delta$ be the complement of the hyperplanes of the $(-2)$-vectors of $N$ [@Dol96, §3]. Write $\Orth(N)^*\definedas\ker\qty(\Orth(N)\to\Aut(A(N)))$ for the discriminant kernel [@Dol96, Prop. 3.3] and $\Orth(N)^{+,*}\definedas\Orth(N)^*\intersect\Orth^+(N)$ for the subgroup preserving the components of $\bD_M$.

::: {.proposition #prop:quotient-stack-of-periods title="The moduli stack of lattice-polarized $\mathrm{K3}$ surfaces as a quotient stack"}
Let $M$ be as above, and assume:
(i) $K_M$ is a fine moduli space for marked $M$-polarized $\mathrm{K3}$ surfaces in the sense of [@Dol96, §3], the group (@def:group) $\Gamma(M)\definedas\theset{\sigma\in\Orth(L):\sigma(m)=m\ \text{for all}\ m\in M}$ acting on it by $\varphi\mapsto\varphi\circ\sigma$;
(ii) the period map (@def:period-map) $p\colon K^a_M\to\bD^\circ_M$ is bijective [@Dol96, Cor. 3.2], and $p\colon K^{pa}_M\to\bD_M$ is surjective with fibre over $\pi$ in bijection with the reflection subgroup $W_\pi(N)$ [@Dol96, Thm. 3.1];
(iii) $\Gamma_M=\Orth(N)^*$, where $\Gamma_M$ is the image of $\Gamma(M)$ in $\Orth(N)$ [@Dol96, Prop. 3.3].
Then:

1. The moduli stack of ample $M$-polarized $\mathrm{K3}$ surfaces is the quotient stack $\qty[\Orth(N)^*\backslash\bD^\circ_M]$, and that of pseudo-ample ones is $\qty[\Orth(N)^*\backslash\bD_M]$.
2. If $M^{\perp}=N$ contains an $m$-admissible isotropic vector (@def:isotropic-subspace) with $m\leq2$ in the sense of [@Dol96, §5], then $\Orth(N)^*$ acts transitively on the two components of $\bD_M$, and
$$\qty[\Orth(N)^*\backslash\bD_M]=\qty[\Orth(N)^{+,*}\backslash\bD^+_M],$$
with the same identity for $\bD^\circ_M$ in place of $\bD_M$.
:::

::: {.proof}

1. *The markings are a torsor.* Let $(X,j)$ be an $M$-polarized $\mathrm{K3}$ surface and let $\varphi,\varphi'\colon H^2(X,\ZZ)\to L$ be two markings of it, that is $\varphi^{-1}|_M=\varphi'^{-1}|_M=j$, in the notation of [@Dol96, §3], where a marked surface (@def:flower-pot-degeneration) is a pair $(X,\varphi)$ with $\varphi^{-1}(M)\subset\Pic(X)$ and $j_\varphi=\varphi^{-1}|_M$. Then $\sigma\definedas\varphi'^{-1}\circ\varphi$ is an isometry of $L$ fixing $M$ pointwise, that is $\sigma\in\Gamma(M)$; So $\sigma\in\Gamma(M)$, and $\varphi\circ\sigma=\varphi$ forces $\sigma=\id$; the action is transitive on the markings of one surface by construction. Hence the markings of a family are a $\Gamma(M)$-torsor.

2. *The stack is the quotient.* By (i) a marked family over $S$ is the same datum as a map $S\to K_M$, and by 1 the markings of the underlying $M$-polarized family are a $\Gamma(M)$-torsor over $S$; so the moduli stack is $\qty[K_M/\Gamma(M)]$, and on the ample locus $\qty[K^a_M/\Gamma(M)]$. By (ii) the period map is bijective there and $\Gamma(M)$-equivariant by the definition of the action; by (iii) its image in $\Aut(\bD^\circ_M)$ is $\Orth(N)^*$, and an isometry of $N$ acts on $\bD_M$ through its image in $\Orth(N)$. Quotient stacks by equivalent actions are equivalent, so $\qty[K^a_M/\Gamma(M)]=\qty[\Orth(N)^*\backslash\bD^\circ_M]$.

3. *The pseudo-ample case.* Here $p$ is only surjective: over $\pi\in\bD_M$ its fibre is in bijection with the subgroup $W_\pi(N)$ generated by the reflections in $\Delta_\pi\cap N$ [@Dol96, Thm. 3.1], a group acting transitively on that fibre, and $W_\pi(N)\subset\Gamma(M)$ because those reflections fix $M$ pointwise; so each fibre lies in a single $\Gamma(M)$-orbit, and the quotient by $\Gamma(M)$ is again $\qty[\Orth(N)^*\backslash\bD_M]$. The argument of 2 applies with $K_M$ in place of $K^a_M$.

4. *The components.* [@Dol96, Prop. 5.6] proves, under the stated hypothesis, that $K_M$ is irreducible, and its proof exhibits the isometry $-\id_{U(m)}\oplus\id_{M'}$ of $M^{\perp}=U(m)\oplus M'$, which lies in $\Gamma(M)$ by [@Dol96, Prop. 3.3] and switches the two components of $\bD_M$. A group acting on a set with two orbits-components and containing an element exchanging them acts transitively, and for a group $G$ acting transitively on the components of $\bD$ with stabilizer (@def:group-orbit) $G^+$ of one component $X$, the equivalence (@def:equivalence-of-objects) $\qty[G\backslash\bD]=\qty[G^+\backslash X]$ is exhibited by restricting a $G$-torsor with equivariant map to $X$. This gives 2.
:::

::: {.proposition #prop:coble-quotient-presentation title="The quotient presentation of the $S_\Co$-polarized moduli stack"}
Let $M=S_\Co=\generators{2}\oplus\generators{-2}^{\oplus10}$ and $N=T_\Co=\generators{2}\oplus U(2)\oplus E_8(2)$, primitively embedded with $N=M^{\perp L}$ (@prop:coble-period-domain(1)--(2), @prop:coble-transcendental). Then:

1. *Condition (U) of [@Dol96, §3] holds.* $M$ admits a primitive embedding in $L$, unique up to an isometry of $L$, by [@Dol96, Prop. 5.1]: its existence hypothesis $l(A(M))\leq20-t$ **or** $t\leq10$ is met through the second disjunct at $t=10$, and its uniqueness hypothesis is met because $A(M)$ is a $2$-group, so the condition at odd primes is vacuous, and because $l(A(M)_2)=11=21-t$ and $A(M)_2$ contains the discriminant form of $U(2)$ as an orthogonal summand.
2. *The hypotheses of @prop:quotient-stack-of-periods hold:* (i) is [@Dol96, §3], the fine moduli space of marked $M$-polarized $\mathrm{K3}$ surfaces; (ii) is [@Dol96, Cor. 3.2] on the ample locus with [@Dol96, Thm. 3.1] on the pseudo-ample one; (iii) is [@Dol96, Prop. 3.3], which is unconditional.
3. *The presentation.* The ample moduli stack of $M$-polarized $\mathrm{K3}$ surfaces is $\qty[\Orth(N)^*\backslash\bD^\circ_M]$, and the pseudo-ample one $\qty[\Orth(N)^*\backslash\bD_M]$. Moreover $\Orth(N)^*$ acts transitively on the two components of $\bD_M$: $T_\Co$ contains the summand $U(2)$, whose basis $e,f$ has $e^2=f^2=0$ and $e\cdot f=2$, so $e$ is $2$-admissible and [@Dol96, Prop. 5.6] applies with $m=2$. Hence
$$F_S=\qty[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]=\qty[\Orth(T_\Co)^{*,+}\backslash\bD(T_\Co)^+].$$
4. *What this does not give.* The non-emptiness of the ample locus is not from [@Dol96, Prop. 5.1]: it would be [@Dol96, Cor. 5.2], whose hypothesis $t\leq9$ fails at $t=10$, and for the Coble lattice it is the existence of the surfaces (@lem:d2-unpolarised-family(1)). And the identification is one of coarse spaces and components; for automorphism groups it needs the cone-preservation statement discussed after this proposition.
:::

::: {.proof}
1. $M$ is even of signature $(1,10)$, so $t=10\leq19$; the embedding is the explicit one of @prop:coble-period-domain. In $A(M)=\generators{e_0,\dots,e_{10}}$ with $q(e_0)=\tfrac12$ and $q(e_i)=-\tfrac12$ for $i\geq1$, the classes $u=e_0+e_1$ and $v=e_0+e_2$ are isotropic with $b(u,v)=1$, so they span a nondegenerate $(\ZZ/2)^2$ whose form is $q(a,b)=ab$, that of $A(U(2))$ [@Dol96, §5], and their orthogonal complement has order $2^9$; this is checked in `computations/reports/coble_797-u-condition.py` with its record. So the uniqueness hypothesis of [@Dol96, Prop. 5.1] is met at the one prime where it is not vacuous.
2. is the list of hypotheses of @prop:quotient-stack-of-periods, each with its source.
3. is @prop:quotient-stack-of-periods(1)--(2) together with its clause 2, and $\Orth(N)^{+,*}=\widetilde\Orth^+(T_\Co)$ is @def:gamma-co-groups(3).
4. $t=10>9$, so [@Dol96, Cor. 5.2] does not apply; the clause about automorphism groups is the paragraph that follows.
:::

*The stabiliser, which is what a stack statement is about.* The identification above is a statement about points and components; for the moduli *stack* it must be a statement about automorphisms. The stabiliser of a period $\pi$ in $\Orth(N)^*$ has to be compared with $\operatorname{Aut}(X,j)$, and a Hodge isometry of $N$ fixing $\pi$ is realised by an automorphism of $X$ exactly when it preserves the Kähler cone. That is the strong Torelli theorem, and [@Dol96] does not state it: it invokes the global Torelli theorem inside the proof of [@Dol96, Thm. 3.1] to describe the fibres by the data $(V^+_\pi,\Delta^+_\pi)$, not to identify stabilisers. So the equivalence $F_S=\qty[\Orth(N)^*\backslash\bD_M]$ is proved here for the underlying coarse space and the components, and for the automorphism groups it holds on the locus where that comparison is available. For $M=S_\Co$ the central isometry $\sigma=\id_M\oplus(-\id_N)$ *is* realised at every member — it is the covering involution of the Coble $\mathrm{K3}$ cover, which acts as $+1$ on $M$ and $-1$ on $T_\Co$ (@prop:coble-transcendental) — and on the ample locus, where $\Delta_\pi\intersect N=\emptyset$ by [@Dol96, Cor. 3.2], the classes of $\Delta_\pi$ lie in $M$, are fixed by $\sigma$, and $\sigma$ preserves the chamber; so there the period quotient and the moduli stack have the same generic automorphism group $\{\pm\id\}$. For a general lattice $M$ this fails: a generic $M$-polarized $\mathrm{K3}$ has trivial automorphism group while $-\id_N$ lies in every stabiliser of the quotient, so the period-domain quotient is then an ineffective quotient of the moduli stack and not equal to it.

*The unpolarized case, and where it stops.* For $M=0$ the statement would be the same one with $N=L$ and $\Orth(L)^*=\Orth(L)$, the $\mathrm{K3}$ lattice being unimodular; but [@Dol96, §3] does not cover it, because its lattice $M$ has signature $(1,t)$ and $M=0$ has signature $(0,0)$. The period map it uses there is the one for marked Kähler $\mathrm{K3}$ surfaces, taken from the sources it cites, and not its own marked lattice-polarized period map. What the unpolarized case needs is therefore the global Torelli theorem for $\mathrm{K3}$ surfaces together with the surjectivity of their period map, each cited by number; no numbered statement of either has been read in this repository, [@Voi07] carrying the generic Torelli theorem for hypersurfaces (Thm. 6.29) and not this one. So the unpolarized half of item 3 is *reduced* to those two inputs, and it is not proved here.

### Item 4: monodromy from a local system on a stack

::: {.theorem #thm:monodromy-exact-sequence title="The monodromy sequence of a local system on a stack, and the covering it defines"}
Let $X$ be a pointed connected topological stack which is locally path connected and semilocally $1$-connected, in the sense of Noohi, *Foundations of topological stacks I* (arXiv:math/0503247), Definition 18.2, and let $\bL$ be a local system of lattices (@def:local-system-of-lattices) on $X$ with fibre $T$ at $x$, with monodromy representation $\rho\colon\pi_1(X,x)\to\Aut(T)$ (@def:transport-and-monodromy). Put $\operatorname{Mon}(\bL)\definedas\rho\qty{\pi_1(X,x)}$ and $K_\bL\definedas\ker\rho$. Then:

1. The sequence
$$1\too K_\bL\too\pi_1(X,x)\too\operatorname{Mon}(\bL)\too1$$
is exact (@def:exact-complex).
2. By Noohi, Theorem 18.19, the Galois correspondence between coverings and $\pi_1$-sets, together with Corollary 18.20 there, the subgroup $K_\bL$ corresponds to a pointed connected covering $p\colon(\widetilde X,\tilde x)\to(X,x)$ of topological stacks in the sense of Noohi, Definition 18.10, with $p_*\pi_1(\widetilde X,\tilde x)=K_\bL$; its group of deck transformations is $\operatorname{Mon}(\bL)$, and $X$ is the quotient of $\widetilde X$ by that group.
:::

::: {.proof}
1. is the first isomorphism theorem for $\rho$.
2. Coverings of $X$ correspond to $\pi_1(X,x)$-sets by Noohi, Theorem 18.19, whose hypotheses are the local ones imposed; the transitive set $\pi_1(X,x)/K_\bL$, on which $\pi_1(X,x)$ acts through $\rho$, corresponds to a connected covering, and Noohi, Corollary 18.20 identifies the subgroup as $p_*\pi_1(\widetilde X,\tilde x)$ and supplies the universal cover. The deck transformations of a covering corresponding to a subgroup $K$ are the automorphisms of the $\pi_1$-set $\pi_1/K$, that is $N(K)/K$ by right translations; here $K=K_\bL$ is a kernel (@def:kernel-cokernel) and hence normal, so the deck group is $\pi_1(X,x)/K_\bL=\operatorname{Mon}(\bL)$ and the covering is Galois with that group, so $X$ is its quotient. The exact sequence is a corollary of Theorem 18.19 and is not stated in that paper.
:::

*The case the programme uses, per loop.* Let $\widetilde U$ be a connected manifold and $\Gamma$ a group acting on it properly discontinuously with finite stabilizers, $U=\widetilde U/\Gamma$ the quotient orbifold (@def:orbifold-quotient-structure), $T$ a $\Gamma$-module whose structure $\varphi\colon\Gamma\to\Aut(T)$ is injective, and $\bT=(\widetilde U\times T)/\Gamma$ the equivariant system whose per-loop transport is @lem:orbifold-monodromy-of-a-nonfree-quotient. Then the transport of every loop is $\pi_1^{\mathrm{orb}}(U,\tilde x)\to\Aut(T)$, $(g,\widetilde\gamma)\mapsto\varphi(g)^{-1}$, with image $\varphi(\Gamma)=\Gamma$ and kernel $\pi_1(\widetilde U,\tilde x)$, so the exact sequence is
$$1\too\pi_1(\widetilde U,\tilde x)\too\pi_1^{\mathrm{orb}}(U,\tilde x)\too\Gamma\too1$$
(@lem:orbifold-monodromy-of-a-nonfree-quotient(1)--(2)). Applied to the presentation of item 3, $U=\bD(T_\Co)^+$ and $\Gamma=\widetilde\Orth^+(T_\Co)$ with its defining action on $T_\Co$, this gives:

::: {.corollary #cor:monodromy-of-the-tautological-system title="The monodromy of the tautological system of $F_S$ is all of $\widetilde\Orth^+(T_\Co)$"}
Let $F_S=\qty[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]$ be the presentation of @prop:coble-quotient-presentation(3) for the Coble lattice. Then, given the descent of the equivariant system $(\bD(T_\Co)^+\times T_\Co)/\widetilde\Orth^+(T_\Co)$ along the $2$-morphisms of the site of $F_S$ (@rmk:the-descent-stops-at-the-2-morphisms, research#797, item 4), the monodromy group of the tautological local system of $F_S$ is $\widetilde\Orth^+(T_\Co)$ itself --- the action of $\widetilde\Orth^+(T_\Co)$ on $T_\Co$ being its defining one --- with kernel $\pi_1\qty(\bD(T_\Co)^+)$. Without that input the lemma below gives the transport of every loop and not the monodromy of a local system on $F_S$.
:::

::: {.proof}
This is @lem:orbifold-monodromy-of-a-nonfree-quotient with $\widetilde U=\bD(T_\Co)^+$, $\Gamma=\widetilde\Orth^+(T_\Co)$, $T=T_\Co$ and $\varphi$ the defining action of $\Gamma$ on $T_\Co$, which is injective, the action of $\Gamma$ on $\bD$ being the one of @prop:quotient-stack-of-periods; the image of the per-loop transport is $\varphi(\Gamma)=\Gamma$ by clause 2 of that lemma, not a subgroup of it. That the transports are the monodromy of a local system on $F_S$ is the descent named in the statement, and is research#797, item 4.
:::

### Item 5: Torelli, and the route that supplies it

::: {.proposition #prop:torelli-for-the-coble-lattice title="Torelli in the form the presentation needs, and the route that supplies it"}
What @prop:coble-quotient-presentation needs is that the period map from the labelled Coble covers to $\bD(T_\Co)$ is injective on isomorphism classes and that its differential is an isomorphism at every point. Then:

1. *Route (b), the transfer along $X\to X/\iota$, supplies it at the level of coarse spaces.* [@DK13, Prop. 3.2] states that the moduli space of Coble surfaces is isomorphic to an open subset of $\bD(N)/\Orth(N)$ for $N=\generators{2}\oplus E(2)$, and deduces it from the Torelli theorem for algebraic $\mathrm{K3}$ surfaces [@DK13, §3]. The transfer is the argument of [@DK13, §5], carried out there for $M=U\oplus D_9$ and concluded as [@DK13, Thm. 5.2]: the $M$-marking determines the involution on $H^2$, two $M$-polarized $\mathrm{K3}$ surfaces with the same period admit a Hodge isometry preserving the marking, the Torelli theorem gives an isomorphism $\varphi$ with $\varphi^*=\phi$, and $\varphi\circ\tau=\tau'\circ\varphi$, so $\varphi$ descends to an isomorphism $X/\tau\iso X'/\tau'$ of the quotients. That is precisely the transfer along a quotient morphism that the item asks for. It is not a numbered statement for the Coble lattice: the numbered statement is [@DK13, Prop. 3.2], and its argument is §5 and the proof of [@DK13, Thm. 5.2].
2. *Local Torelli* is [@Dol96, §3], where the differential of the period map is the bijection displayed there, and injectivity on marked ample objects is [@Dol96, Cor. 3.2].
3. *Route (a) has no object.* The Coble periods are the image of the $(-2)$-Heegner divisor of the Enriques period domain under the quotient by $\Orth(U\oplus E(2))$ [@DK13, the paragraph after Prop. 3.2], so the Enriques moduli occupies the complement of the Coble locus and a Torelli statement for Enriques surfaces restricts to nothing there. What route (a) would need is an extension of Torelli across that divisor, which is not a numbered statement in the sources read, together with a comparison of the monodromy of a degenerating Enriques family with $\Gamma_\Co$, which is the step recorded as failing in @rmk:d2-routes-for-the-equality(3).
4. *What route (b) leaves open:* the surjectivity of the period map onto $\bD(T_\Co)$, and the identification of stabilisers with automorphism groups, which is the cone-preservation step after @prop:coble-quotient-presentation.
:::

::: {.proof}
1. is [@DK13, Prop. 3.2] with the transfer of [@DK13, §5], restated in the terms of this section; the descent of $\varphi$ to the quotients is the universal property of the quotient. 2. is the two numbered statements named. 3. is [@DK13, the paragraph after Prop. 3.2] for the description of the Coble locus, and @rmk:d2-routes-for-the-equality(3) for the monodromy step. 4. names what neither source states: [@DK13, Prop. 3.2] maps the moduli space *into* the period quotient and does not claim that the image is everything, and the stabiliser comparison is the paragraph after @prop:coble-quotient-presentation.
:::

::: {.lemma #lem:coble-deformations-are-not-all-of-Def-S title="The equivariant deformations are the Coble directions, and not all of them"}
Let $\iota\colon X\to S=X/\iota$ be the Coble cover, with $X$ a $\mathrm{K3}$ surface and $S=\Bl_{10}\PP^2$. Then:

1. $h^1(X,\Theta_X)=20$ and its $\iota$-invariant part is $9$-dimensional. Under the identification $\Theta_X\iso\Omega^1_X$ by contraction with the holomorphic $2$-form, which anti-commutes with $\iota$ because $\iota^*\omega=-\omega$, the eigenspaces are exchanged, so $H^1(X,\Theta_X)^{\iota}\iso H^{1,1}(X)^{-}=\Pi^{\perp}\intersect\qty(T_\Co\otimes\RR)$, of dimension $\rank T_\Co-2=9$.
2. $h^1(S,\Theta_S)=12$. Riemann--Roch for the tangent bundle of a surface gives $\chi(\Theta_S)=(7K_S^2-5e(S))/6$, and $K_S^2=-1$, $e(S)=13$ give $\chi(\Theta_S)=-12$; $h^0(\Theta_S)=0$ and $h^2(\Theta_S)=h^0(\Omega^1_S\otimes K_S)^*=0$, the latter because $\Omega^1_S\otimes K_S$ pulls back to $\Omega^1_X$ under the cover, so $h^1(\Theta_S)=12$.
3. Hence the map $H^1(X,\Theta_X)^{\iota}\to H^1(S,\Theta_S)$ induced by passing to the quotient is neither surjective nor an isomorphism (@def:isomorphism-of-objects): $9\neq12$, and the Coble locus has codimension $3$ in $\mathrm{Def}(S)=\Ext^1(\Omega^1_S,\OO_S)$.
:::

::: {.proof}
1. $h^1(\Theta_X)=20$ for a $\mathrm{K3}$ surface; $H^2(X,\CC)=M_\CC\oplus(T_\Co)_\CC$ with $\rank M=11$, and the period plane $\Pi$ is a positive $2$-plane inside $(T_\Co)_\RR$, so $H^{1,1}(X)$ has dimension $20$ and splits as $M_\CC$ of dimension $11$ and $\Pi^{\perp}\intersect(T_\Co)_\RR$ of dimension $11-2=9$; since $\iota$ acts as $-1$ on $T_\Co$, the anti-invariant part is the second summand. The contraction $\Theta_X\iso\Omega^1_X$ sends $w$ to $\iota_w\omega$, and $\alpha_{\iota_*w}=\iota^*\iota_w\omega=-\iota_w\iota^*\omega=-\iota^*\alpha_w$ because $\iota^*\omega=-\omega$; so the invariant part of $H^1(\Theta_X)$ is the anti-invariant part of $H^{1,1}$.
2. $\chi(\Theta_S)=(7K_S^2-5e(S))/6$ is Riemann--Roch: with $c_1(\Theta_S)=-K_S$ and $c_2(\Theta_S)=e(S)$, the Chern character and Todd class give $\chi=(K_S^2-2e(S))/2+K_S^2/2+(K_S^2+e(S))/6$, which is that expression; for $\PP^2$ it gives $8=h^0(\Theta_{\PP^2})$, so the form is right. Then $K_S^2=9-10=-1$ and $e(S)=3+10=13$ give $-12$, and the two vanishing cohomology groups (@def:group) give $h^1=12$.
3. Passing to the quotient is compatible with base change (@def:module-base-change) for a finite group, so a family of $\mathrm{K3}$ surfaces with a fibrewise involution has a quotient family and the map exists; the dimensions of 1. and 2. give the rest, and $\mathrm{Def}(S)$ is that $\Ext^1$ by the deformation--obstruction sequence, unobstructed because $h^2(\Theta_S)=0$.
:::

### The transfer at the level of the stacks

@prop:torelli-for-the-coble-lattice cites the transfer from [@DK13, Prop. 3.2] and the argument of [@DK13, §5]. That source states it for coarse spaces, and for the Coble lattice the transfer is not separately numbered; so it is proved here, for the stack and not only for its coarse space.

::: {.theorem #thm:coble-period-map-of-the-stack title="The period map of the Coble stack: it is defined, injective on labelled objects, locally an isomorphism, and descends to the quotients"}
Let $\mcM^{\mathrm{lab}}_\Co$ be the groupoid of labelled Coble covers: an object is $(S,X\xrightarrow{\pi}S,\iota;e_0,e_1,\dots,e_{10})$ with $S=\Bl_{p_1,\dots,p_{10}}\PP^2$ at an irreducible ten-nodal sextic, $\pi$ the double cover branched along the proper transform $C_b\subset S$, $\iota$ its covering involution, and $e_0,e_1,\dots,e_{10}$ the eleven classes -- the pullback of a line and the ten exceptional curves -- named as in @lem:d2-local-system(2); a morphism is a Cartesian square over $\CC$ commuting with $\pi$, with $\iota$, and with the eleven classes. Let $M=\generators{2}\oplus\generators{-2}^{\oplus10}$, $T_\Co=M^{\perp\lkt}$, and let $\bD(T_\Co)^+$ be the period domain of @prop:coble-period-domain(1). Then:

1. *The period map is defined.* $\iota^*$ is $+\id$ on $M$ and $-\id$ on $T_\Co$ (@prop:coble-transcendental), so $H^{2,0}(X)\subset T_\Co\otimes\CC$ and the line $H^{2,0}(X)$ is a point of $\bD(T_\Co)^+$; assigning it to an object, with the transport of @lem:d2-local-system(3), defines a morphism of stacks $\mathfrak p\colon\mcM^{\mathrm{lab}}_\Co\to\bD(T_\Co)^+$.
2. *Injectivity on objects, and what the isomorphisms are.* Two labelled Coble covers with the same period are isomorphic; the isomorphisms between them form the automorphism group of either, which contains the covering involution $\iota$ and is therefore *not* trivial. So the period map is injective on objects but is not an isomorphism on groupoids without matching that isotropy, which is what clause 4 needs and what a review has found unproved.
3. *Local Torelli.* The differential of $\mathfrak p$ at an object is an isomorphism from the tangent space of the stack onto the tangent space of $\bD(T_\Co)^+$; both have dimension $9$.
4. *Descent to the quotients.* The group $\Gamma(M)=\theset{\sigma\in\Orth(\lkt):\sigma(m)=m\ \text{for all}\ m\in M}$ acts on $\mcM^{\mathrm{lab}}_\Co$ by $\varphi\mapsto\varphi\circ\sigma$ on markings, its image in $\Orth(T_\Co)$ is $\Orth(T_\Co)^*$ [@Dol96, Prop. 3.3], the period map is $\Gamma(M)$-equivariant, and the induced morphism of quotient stacks
$$\overline{\mathfrak p}\colon\qty[\Gamma(M)\backslash\mcM^{\mathrm{lab}}_\Co]\too\qty[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]$$
is fully faithful, with essential image the image of the ample locus.
:::

::: {.proof}
1. is @prop:coble-transcendental with @prop:coble-period-domain(1): the unique $(-1)$-eigenspace of $\iota^*$ is $T_\Co$, and since $\iota$ is holomorphic and non-symplectic, $\iota^*\omega=-\omega$, so $H^{2,0}(X)\subset T_\Co\otimes\CC$; the line is isotropic and positive, that is a point of $\bD(T_\Co)^+$ by @prop:coble-period-domain(1). Naturality in a family is @lem:d2-local-system(3), which identifies the local system with fibre $T_\Co$.
2. A labelled object determines a marking $\varphi\colon H^2(X,\ZZ)\to L$ sending $e_0,\dots,e_{10}$ to the classes of @lem:d2-local-system(2) and $H$ to the pullback of a line, and $M$ to $\Pic(X)$. If two objects have the same period, then under these markings the two Hodge structures on $L$ coincide, so $\phi=\id_L$ is a Hodge isometry $H^2(X)\to H^2(X')$. It carries the polarization of the one to that of the other, because both are generated by the same eleven classes; the class those classes generate is $e_0=f^*\OO_{\PP^2}(1)$, which is nef and **not** ample (@lem:d2-arrangement-classes(2)), so the strong Torelli hypothesis is not checked here and this clause's injectivity is conditional on the chamber/ample-class finding (ii) of @rmk:findings-ii-iii-and-the-isotropy; so the strong Torelli theorem in the form stated for this use at @lem:chamber-from-marked-period [@BHPV04, Ch. VIII, Thm. 11.1] gives an isomorphism $f\colon X'\iso X$ with $f^*=\phi=\id$. The involution is determined by its action on $H^2$, which is $+\id$ on $M$ and $-\id$ on $T_\Co$ (@prop:coble-transcendental), and the two objects have the same action, so $f\iota'=\iota f$ and $f$ descends to $S'\iso S$; it fixes the eleven classes, hence is an isomorphism of labelled objects. Uniqueness: an automorphism of a $\mathrm{K3}$ surface acting trivially on $H^2$ is the identity (its action on $H^2$ determines it because $H^{2,0}\oplus H^{0,2}$ is its nonzero part), so an isomorphism inducing a given isometry of $L$ is unique.
3. The tangent space of $\mcM^{\mathrm{lab}}_\Co$ at an object is the space of $\iota$-invariant first-order deformations, $H^1(X,\Theta_X)^{\iota}$, of dimension $9$ by @lem:coble-deformations-are-not-all-of-Def-S(1). The differential of the period map of marked $\mathrm{K3}$ surfaces is the bijection $d_1\colon H^1(X,\Theta_X)\to\operatorname{Hom}(H^{2,0}(X),H^{1,1}(X))$ displayed in [@Dol96, §3]; it is $\iota$-equivariant, and $\iota$ acts as $-1$ on $H^{2,0}$ and as $-1$ on $H^{1,1}(X)^{-}$, so on the invariant parts it is a bijection $H^1(X,\Theta_X)^{\iota}\to\operatorname{Hom}(H^{2,0}(X),H^{1,1}(X)^{-})$, and the target is the tangent space of $\bD(T_\Co)^+$ at the period. Both sides have dimension $9$ by @lem:coble-deformations-are-not-all-of-Def-S(1).
4. $\Gamma(M)$ acts on markings by composition, hence on $\mcM^{\mathrm{lab}}_\Co$; the period map is equivariant because the period depends on the marking only through $\varphi|_{T_\Co}$, and $\sigma\in\Gamma(M)$ acts on $T_\Co$ as an isometry. The image of $\Gamma(M)$ in $\Orth(T_\Co)$ is $\Orth(T_\Co)^*$ by [@Dol96, Prop. 3.3], and $\Orth(T_\Co)^{+,*}=\widetilde\Orth^+(T_\Co)$ by @def:gamma-co-groups(3), which is the group acting on $\bD(T_\Co)^+$ by @prop:coble-quotient-presentation(3). Full faithfulness: 2 gives injectivity on objects up to a unique isomorphism, 3 gives the isomorphism on tangent spaces, and a morphism of quotient stacks between two objects is a group element carrying one marking to the other, which exists exactly when the two lie in the same $\Gamma(M)$-orbit. The essential image is the image of the ample locus by @prop:coble-quotient-presentation(2).
:::

::: {.proposition #prop:coble-enriques-maps-and-the-vhs title="The two maps of item 2, and what each does to the local system"}
1. *The map to the Enriques side is a closed embedding of period domains and a normalization of a Heegner divisor, never an open immersion.* Because $T_\Co=\delta^{\perp T_\En}$ (@prop:gamma-co-images), the period domain of the Coble problem is the locus where the period is orthogonal to $\delta$, a closed complex submanifold of $\bD(T_\En)$; on the quotients the map
$$f^{\Gamma}\colon F^{\Gamma}_\Co=\bD(T_\Co)/R_\Gamma\too\bD(\ten)/\Gamma$$
induced by $\eta$ is finite and birational onto the $(-2)$-Heegner divisor $\mch_{-2}/\Gamma$, and exhibits $F^{\Gamma}_\Co$ as the normalization of that divisor (@thm:normalization), for $\Gamma$ one of $\Gamma_\En$, $\Gamma^K_\En$, $\gent$.
2. *What the meridian of that divisor does.* The local monodromy of the Enriques local system about the divisor is the reflection $s_\delta$ (@lem:d2-vanishing-reflections(3)), and $s_\delta$ acts trivially on its own hyperplane $\delta^{\perp T_\En}=\eta(T_\Co)$. So the restriction of the Enriques local system to the divisor is a local system with fibre $T_\Co$, and its monodromy group is the image of the stabilizer $\Stab_{\Gamma_\En}(\delta)$, which is $R_{\Gamma_\En}=\widetilde\Orth^+(T_\Co)$ (@prop:gamma-co-images(1)). That is an upper bound for $\Gamma_\Co$; it is not $\Gamma_\Co$, and the step that would identify them is the one recorded as failing in @rmk:d2-routes-for-the-equality(3).
3. *The map to the K3 side is a quotient, and it does not move the local system.* The other map of item 2 is $(S,X\xrightarrow{\pi}S,\iota)\mapsto X$; its image is the $\mathrm{K3}$ covers, and $S$ is recovered as $X/\iota$, so the map is fully faithful on the groupoids (@lem:d0-coble-stack-in-involution-stack). On cohomology it neither pulls back nor pushes forward the local system of the Coble problem: that system has fibre $T_\Co$, the $\iota$-anti-invariant summand of the $\mathrm{K3}$ system of rank $22$ (@lem:d2-local-system(3), @prop:coble-transcendental), so it is a sub-local-system of the $\mathrm{K3}$ system, and $\pi$ is not a morphism of variations of Hodge structure to be functorial for it.
:::

::: {.proof}
1. is @thm:normalization, whose hypothesis is that $\eta$ embeds $T_\Co$ primitively in $\ten$ (@lem:primitive_embedding_eta) and whose proof identifies $R_\Gamma$ with the restriction of $\Stab_\Gamma(\delta)$ (@prop:gamma-co-images); the image is the Heegner divisor because every period of $T_\Co$ is orthogonal to the $(-2)$-vector $\delta$. 2. is @lem:d2-vanishing-reflections(3) for the meridian and the definition of a reflection for the triviality on its hyperplane; the monodromy of the restricted system is the image of the subgroup of $\Gamma_\En$ preserving the divisor, that is of the stabilizer, by @lem:coble-family-base-change applied to the inclusion of the divisor. 3. is @lem:d0-coble-stack-in-involution-stack for the full faithfulness, with $X/\iota=S$ the recovery of the quotient (@lem:d2-unpolarised-family(1)--(2)), and @lem:d2-local-system(3) for the fibre and rank of the Coble system.
:::

::: {.proposition #prop:coble-monodromy-is-the-marking-group title="The torsor argument for the monodromy of the labelled stack, and the inputs it needs"}
Let $\mathfrak p\colon\mcM^{\mathrm{lab}}_\Co\to\qty[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]$ be the period map of @thm:coble-period-map-of-the-stack, let $[U/G]$ be its essential image, with $G=\widetilde\Orth^+(T_\Co)$, and let $\bT$ be the local system with fibre $T_\Co$ of @lem:d2-local-system(3). Suppose that

(H1) $\mathfrak p$ is an equivalence of stacks onto its essential image $[U/G]$, which is an open substack of $\qty[G\backslash\bD(T_\Co)^+]$, with the isotropy group at a point matched to the stabiliser of its period --- the stack-level Torelli with inertia of @rmk:findings-ii-iii-and-the-isotropy, whose ample-class input enters through @thm:coble-period-map-of-the-stack(2) --- and
(H2) $U$ is connected, and
(H3) the tautological system of $\qty[G\backslash\bD(T_\Co)^+]$ is a local system on the stack, whose pullback along the chart $\bD(T_\Co)^+\to\qty[G\backslash\bD(T_\Co)^+]$ is the equivariant system $(\bD(T_\Co)^+\times T_\Co)/G$: the descent along the $2$-morphisms of the site, which @lem:tautological-system-descends does not construct (@rmk:the-descent-stops-at-the-2-morphisms, research#797, item 4).

Then:

1. Under (H1), $[U/G]$ is an open substack of $\qty[G\backslash\bD(T_\Co)^+]$ and $\mathfrak p$ is an equivalence onto it.
2. $U\to[U/G]$ is a $G$-torsor in the sense of stacks, and
$$1\too\pi_1(U)\too\pi_1([U/G])\too G\too1$$
is exact, and in particular $\pi_1([U/G])\to G$ is onto. Connectedness of $U$ (H2) is what the surjectivity uses: for $g\in G$ it is produced by a path of $U$ from $x$ to $gx$, so a group acting transitively on the components of a disconnected $U$ would not suffice.
3. Under (H3), $\bT$ is the pullback of the tautological local system $(\bD(T_\Co)^+\times T_\Co)/G$ along $\mathfrak p$, and the monodromy representation of that local system is $\pi_1([U/G])\to G\to\Aut(T_\Co)$, with image $G$: its transports are those of @lem:orbifold-monodromy-of-a-nonfree-quotient(2), computed per loop, and (H3) is what makes them the monodromy of a local system on the stack.
4. Consequently, under (H1)--(H3), the *orbifold* monodromy of the labelled Coble stack is $G=\widetilde\Orth^+(T_\Co)$. This is the monodromy of @def:geometric-monodromy and it is the reading in which the sign is present, as the isotropy: $\iota=-\id_{T_\Co}$ acts on $T_\Co$ at every object of the direct construction (@thm:sign-is-isotropy), and its transfer to this stack is finding (iv) of @rmk:findings-ii-iii-and-the-isotropy. Two steps beyond that conclusion are owed and are taken here as neither proved nor used. First, $\Gamma_\Co=G$ for $\Gamma_\Co$ of @def:gamma-co-groups(1) needs in addition the identification of the labelled stack's monodromy with the monodromy of the universal family over $\mcM_\Co$ (@prop:gamma-co-from-the-universal-family(1)), which is research#797, item 6. Second, the *loop* monodromy over a base is a different group, and this proposition computes it nowhere: in the direct construction no loop carries $\iota$ (@thm:no-loop-carries-the-sign), whereas on the labelled base $B$ of @def:coble-family-unpolarized a loop does carry $-\id_{T_\Co}$ (@prop:sign-is-a-loop-of-the-labelled-base), so the index-two reading does not transfer to $B$ and, stated universally, is false. What is known about $\Gamma_\Co(B)$ is the inclusion $\Gamma_\Co(B)\subseteq G$ (@thm:gamma-co-is-stable(1)), together with $-\id_{T_\Co}\in\Gamma_\Co(B)$ and an index in $G$ that is finite and bounded by the reflection index (@rmk:the-sign-is-a-loop-not-a-missing-sign(3)); whether it is $G$ is @qst:gamma-co-sign-is-realised and @conj:gamma-co-stable.
:::

::: {.proof}
1. is @thm:coble-period-map-of-the-stack(4): a fully faithful morphism of stacks is an equivalence onto its essential image, which is open because the map is.
2. The map $U\to[U/G]$ is the quotient of $U$ by $G$, so $U\times_{[U/G]}U\cong G\times U$ and it is a $G$-torsor over the stack, hence a covering of topological stacks in the sense of Noohi, *Foundations of topological stacks I* (arXiv:math/0503247), Definition 18.10; by the Galois correspondence, Theorem 18.19 with Corollary 18.20, a subgroup of $\pi_1$ corresponds to a pointed connected covering with deck group the quotient, so this torsor corresponds to $\pi_1(U)$ with deck group $\pi_1([U/G])/\pi_1(U)=G$, which is the sequence. The last sentence is the reason for the hypothesis: an element $g$ lies in the image only if some $x\in U$ can be joined to $gx$ inside $U$.
3. The period map classifies the variation, the Hodge structures of the family being marked into the fixed lattice (@prop:lifted-period-map(3), @lem:d2-local-system(3)); for the tautological system the monodromy representation is $(g,[\widetilde\gamma])\mapsto\varphi(g)^{-1}$, with $\varphi$ the defining action of $G=\widetilde\Orth^+(T_\Co)$ on $T_\Co$, so its image is $\varphi(G)=G$ (@lem:orbifold-monodromy-of-a-nonfree-quotient(2) applied to $\widetilde U\to U$). The computation is per loop, in the transport system of that clause; that these transports are the monodromy of a local system on the stack is (H3), assumed and not proved.
4. is 1--3, which give the orbifold monodromy of the labelled stack; the two further steps the clause excludes --- the identification of that group with $\Gamma_\Co$ of @def:gamma-co-groups(1), and any statement about loop monodromy --- are not proved in them and are stated as excluded.
:::

::: {.lemma #lem:every-ample-m-polarized-k3-is-a-coble-cover title="Reconstruction: every $M$-polarized $\mathrm{K3}$ surface with period in the ample locus is a Coble cover"}
Let $M=S_\Co$, let $X$ be an $M$-polarized $\mathrm{K3}$ surface with the marking of $M$ fixed, whose period lies in the ample locus $\bD^\circ(T_\Co)$ -- the complement of the hyperplanes of the $(-2)$-vectors of $T_\Co$ -- and put $\sigma\definedas\id_M\oplus(-\id_{T_\Co})\in\Orth(L)$. Then:

1. $\sigma$ is a Hodge isometry of $L$ and is realised by an automorphism of $X$.
2. Its invariant lattice is $M$, of rank $11$, and its fixed locus is a smooth rational curve.
3. $X/\sigma$ is a Coble surface, and $X$ is its $\mathrm{K3}$ double cover branched along that curve.
:::

::: {.proof}
1. $\sigma$ fixes $M$ pointwise, and $M\subset\Pic(X)$ consists of classes of type $(1,1)$; it acts as $-1$ on $T_\Co$, which contains $H^{2,0}(X)\oplus H^{0,2}(X)$ because $M\subset\Pic(X)$ forces $H^{2,0}\subset T_\Co\otimes\CC$. So $\sigma$ preserves the Hodge decomposition. It preserves the polarization class, which lies in $M$ and is ample by the hypothesis that the period is in $\bD^\circ(T_\Co)$; so by the strong Torelli theorem in the form used at @lem:chamber-from-marked-period [@BHPV04, Ch. VIII, Thm. 11.1], $\sigma$ is the pullback of an automorphism. (Equivalently: the period avoids the $(-2)$-hyperplanes of $T_\Co$, so every $(-2)$-class of $\pi^{\perp}$ lies in $M$ and is fixed by $\sigma$, whence $\sigma$ preserves the chamber and the Kähler cone.)
2. The invariant lattice of $\sigma$ on $H^2(X,\ZZ)$ is $\{x:\sigma x=x\}=M$, since $L\otimes\QQ=M\otimes\QQ\oplus T_\Co\otimes\QQ$; it has rank $11$. For a nonsymplectic involution the Lefschetz fixed point formula gives $\chi(\Fix\sigma)=2+\tr\qty(\sigma^*|_{H^2})$, and with $\tr=2\rank M-22=0$ one gets $\chi(\Fix\sigma)=2$. A fixed locus of Euler characteristic $2$ on a $\mathrm{K3}$ surface is a smooth rational curve: the fixed locus of a nonsymplectic involution is a disjoint union of a curve and isolated points, and $\chi=2-2g+\#\{\text{points}\}=2$ forces $g=0$ and no points.
3. For an involution with fixed curve $R$ the quotient is a smooth rational surface with $\abs{-K}=\emptyset$ and $\abs{-2K}=\abs{C}$ nonempty, by the adjunction computation of @lem:d2-unpolarised-family(1) read on the quotient, and $R$ is the branch curve of the double cover $X\to X/\sigma$; such a surface is a Coble surface, and $X$ is its $\mathrm{K3}$ double cover. The ten classes $e_1,\dots,e_{10}$ of $M$ supply the labels.
:::

*What this settles, and what it corrects.* Taken with @thm:sign-is-isotropy, clause 4 separates the two readings of the group of research#780 item 16, under (H1)--(H3), which the volume keeps apart under different names and which the routes of @rmk:d2-routes-for-the-equality ran together:

- the *orbifold* monodromy of the Coble stack is $\widetilde\Orth^+(T_\Co)$, the sign being the isotropy $\iota$ that every object carries (@thm:sign-is-isotropy);
- the *loop* monodromy over a base is a different group, and this proposition does not compute it: in the direct construction no loop carries $\iota$ (@thm:no-loop-carries-the-sign), while on the labelled base a loop does (@prop:sign-is-a-loop-of-the-labelled-base), and the transfer of the first statement to that base is finding (iv) of @rmk:findings-ii-iii-and-the-isotropy.

So, under (H1)--(H3), the equality $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$ holds for the monodromy of the universal family over the stack -- the definition of @def:gamma-co-groups(1) -- once the labelled stack's monodromy is identified with that of the universal family, which is research#797, item 6 and is not used here. It is not proved for loops over a parameter space in either direction: the labelled loop group satisfies $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ with $-\id_{T_\Co}\in\Gamma_\Co(B)$ and finite index (@thm:gamma-co-is-stable(1), @prop:sign-is-a-loop-of-the-labelled-base, @rmk:the-sign-is-a-loop-not-a-missing-sign(3)), and whether it is the whole group is @qst:gamma-co-sign-is-realised. An earlier form of this proposition asserted $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$, and asserted at the same time that no loop carries $\iota$; the two cannot both hold on $B$, since $-\id_{T_\Co}\in\widetilde\Orth^+(T_\Co)$ and a loop of $B$ carries it (@prop:sign-is-a-loop-of-the-labelled-base), and both are corrected here. What the three routes of @rmk:d2-routes-for-the-equality computed was the loop monodromy, and none of them closes the reverse inclusion --- not for want of the sign, which is a loop on $B$, but at the step named for each in that remark. What remains open is $\Gamma_\Co(B)=\widetilde\Orth^+(T_\Co)$ (@qst:gamma-co-sign-is-realised, a case of @conj:gamma-co-stable), the identification of that group with the one named in @prop:gamma-co-from-the-universal-family(1) (research#797, item 6), and the comparison of $\Gamma_{\Co,2}$ with $R_{\gent}$, which is settled in the negative (@qst:coble-monodromy-equality, @prop:coble-monodromy-equality-false).

::: {.conjecture #conj:gamma-co-orbifold-equality title="The orbifold monodromy of the Coble stack is $\widetilde\Orth^+(T_\Co)$"}
Let $\mcM^{\mathrm{lab}}_\Co\to\mcM_\Co$ be the forgetful map from the labelled stack to the stack of Coble surfaces (@def:coble-surface), and read $\Gamma_\Co$ as the monodromy of $T_\Co$ on $\pi_1$ of the stack. Then $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$.
:::

*What is proved, and what is not.* The inclusion proved is $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$, @thm:gamma-co-is-stable(1), and it is a statement about the labelled presentation; for $\Gamma_\Co$ of @def:gamma-co-groups(1) what is proved is $\Gamma_\Co\subseteq\Orth^+(T_\Co)$ (@lem:monodromy-is-spinor-positive), the containment in the discriminant kernel being exactly what @conj:gamma-co-stable asserts. Equality is that conjecture, of which this is the stack reading. The assembly that would give it is *conditional*, on four statements none of which is proved here:

1. *Stack-level Torelli with its inertia.* @thm:coble-period-map-of-the-stack gives that two labelled covers with equal periods are isomorphic and that the differential is an isomorphism; its clause 2 does **not** give a unique isomorphism, because the covering involution is an automorphism of every labelled object. What the argument needs is that the period map be an equivalence of stacks onto its image with the inertia groups matched, which is the stabiliser-equals-automorphism statement the page records as unavailable from [@Dol96] (the paragraph after @prop:coble-quotient-presentation).
2. *An ample class in the period proof.* The strong Torelli input has to be applied with a genuinely ample class in $M$; the class $e_0=f^*\OO(1)$ used for the labelling is nef and not ample (@lem:d2-arrangement-classes(2)), so the hypothesis is not checked at the place the proof uses it.
3. *Connectedness of the image.* The passage from a constructible period image to a complement that is a proper closed analytic subset needs a theorem, and the alternative route through @lem:every-ample-m-polarized-k3-is-a-coble-cover does not reconstruct the ten-nodal plane presentation as written.
4. *The descent to the stack.* The monodromy is computed per loop, in the transport system on $S^1$, and the step that turns the transports into the monodromy of a local system on the quotient is the comparison along the $2$-morphisms of the site, which @lem:tautological-system-descends does not construct (@rmk:the-descent-stops-at-the-2-morphisms); this is the (H3) of the proposition and research#797, item 4.

*Given* 1--4 the argument runs as follows, and this is what @prop:coble-monodromy-is-the-marking-group records: $U\to[U/G]$ is a $G$-torsor, Noohi's Theorem 18.19 with Corollary 18.20 (*Foundations of topological stacks I*, arXiv:math/0503247) give $1\to\pi_1(U)\to\pi_1([U/G])\to G\to1$, and the local system, being the pullback of the tautological one, has monodromy all of $G$. The relabellings contribute the group $\Theta$ of discriminant classes, of order $10!$ (@prop:gamma-co-from-the-labelled-stack(3)) and the isotropy a finite subgroup (@prop:gamma-co-from-the-labelled-stack(4)). None of that closes 1--4.

*Review findings recorded here, in the order they were raised, with the step each blocks.* (i) $\iota$ is a nontrivial automorphism of every labelled cover, so the labelled stack does not have trivial isotropy and the uniqueness assertion fails; (ii) no ample class is constructed where the period proof needs one; (iii) the step from a constructible image to a proper closed analytic complement needs a theorem; (iv) the lift of $\Aut(S)$ to the cover, and the identification of the isotropy at *every* member rather than at a general one, is not proved; (v) the descent of the equivariant system along the $2$-morphisms of the site, which @lem:tautological-system-descends does not construct (@rmk:the-descent-stops-at-the-2-morphisms), is the (H3) of @prop:coble-monodromy-is-the-marking-group and research#797, item 4. The first two are being taken by the Torelli/ample-class workstream, the last three by the isotropy and descent workstream; until they are, this page asserts the inclusion and the conjecture, and not the equality.

::: {.remark #rmk:is-iota-a-loop title="Is $\iota$ a loop, or the isotropy?"}
The covering involution acts as $-1$ on $T_\Co$. It is an automorphism of every labelled cover, so it is the *isotropy* of the stack at every object and lies in the orbifold fundamental group there (@thm:sign-is-isotropy, for the direct construction; transferring that statement to this stack is finding (iv) above). What it is not, in general, is the image of a loop: on the coarse space of the direct construction no loop carries $\iota$ (@thm:no-loop-carries-the-sign, again for the direct construction), whereas on the labelled base $B$ of @def:coble-family-unpolarized a loop does carry $-\id_{T_\Co}$ (@prop:sign-is-a-loop-of-the-labelled-base). So "$\iota$ is the loop" is false where it is asserted for that coarse space and true on $B$; the two readings are related by a quotient and not necessarily by a subgroup, and the quotient is by $\{\pm\id\}$ only where no loop carries the sign. Every use of either theorem on this stack is conditional on that transfer.
:::

::: {.remark #rmk:findings-ii-iii-and-the-isotropy title="Findings (ii), (iii) and the descent with the isotropy $\{\id,\iota\}$: the route each needs"}
**(ii) The ample class.** The strong Torelli theorem is quoted in its ample form [@BHPV04, Ch. VIII, Thm. 11.1], and the class the labelling supplies, $e_0=f^*\OO_{\PP^2}(1)$, is nef and not ample (@lem:d2-arrangement-classes(2): $e_0\cdot e_i=0$ with $e_i\neq0$). Two routes, and neither is closed here. *(a) An ample class in $M$.* A class $x=a e_0-\sum_{i=1}^{10}c_i e_i$ with $c_i>0$ has $x\cdot e_i=2c_i>0$ and $x^2=2a^2-2\sum c_i^2$, so it is positive on the ten $(-2)$-curves and has positive square as soon as $a^2>\sum c_i^2$, for instance $x=4e_0-\sum_{i=1}^{10}e_i$ with $x^2=12$; what is missing is that it be positive on *every* curve, that is that it lie in the Kähler chamber of the marked period, which is the chamber datum @lem:chamber-from-marked-period attaches to a marked period for the direct construction. *(b) Quasi-polarized Torelli.* [@Dol96, Thm. 3.1] is stated for **pseudo-ample** $M$-polarized $\mathrm{K3}$ surfaces, which is exactly the nef-and-big case, and the chamber enters as the data $(V^+_\pi,\Delta^+_\pi)$ that its fibre description uses; taking that theorem as the Torelli input, rather than the ample form, is the route that matches the class the family carries. Which of (a) and (b) to use is open, and the page asserts neither.

**(iii) Constructible image to an open set with closed analytic complement.** Two candidate inputs, and both fail on a hypothesis the page itself has recorded. *Chevalley:* the image of a morphism of finite type is constructible, and $\mcM_\Co$ is not locally of finite type (@rmk:d2-involution-moduli-of-ae22 records the infinite automorphism groups and the resulting failure), so the period map is not a morphism of finite type and Chevalley does not apply as stated. *Baily--Borel:* the quotient $\bD(T_\Co)/\Gamma$ is a quasi-projective variety and the period map is algebraic once the moduli problem is algebraic, which is item 1's open algebraicity statement. So (iii) is not independent of the programme: it reduces to the algebraicity of $\mcM_\Co$, which is not established.

**The descent with isotropy.** The correct form of the descent clause is not "an equivalence onto $[U/G]$" but: the period map is fully faithful on objects (@thm:coble-period-map-of-the-stack(2), with its clause corrected), its image is $[U/G]$ *as an orbifold quotient with inertia*, and the inertia at a point with period $\pi$ is the stabiliser $\Stab_G(\pi)$, which contains $\iota=-\id_{T_\Co}$ (@thm:sign-is-isotropy, for the direct construction; the transfer to this stack is finding (iv)). The map $\pi_1([U/G])\to G$ then contains that stabiliser in its image, and it is onto $G$ only if the stabiliser generates $G$ together with the loops — which is what connectedness of $U$ supplies at the level of the torsor, and what the inertia supplies at the level of the sign. Writing the isotropy as $\{\id,\iota\}$ at every point is the genericity statement that is *not* proved: a member with extra automorphisms has a larger stabiliser, and the volume records $\Aut(S)=W_{10}(2)$ only for a general member (@prop:gamma-co-from-the-labelled-stack(4)).
:::

::: {.proposition #prop:d2a-family-is-pseudo-ample title="The D2a family is $M$-polarized with $e_0$ nef and big; pseudo-ampleness is open"}
Let $M=S_\Co=\generators{2}\oplus\generators{-2}^{\oplus10}$ and let $X_b\to S_b\to\PP^2$ be the fibre of @lem:d2-unpolarised-family(1), with $e_0=f^*H$ and $e_i=f^*E_i$ the eleven classes of @lem:d2-local-system(2). Then:

1. $j\colon M\injects\Pic(X_b)$, $e_0\mapsto e_0$, $e_i\mapsto e_i$, is a primitive embedding of lattices, so $(X_b,j)$ is an $M$-polarized $\mathrm{K3}$ surface in the sense of [@Dol96, §1].
2. $e_0$ is nef and big.
3. **Open.** The step from 2 to pseudo-ampleness does not follow, and is recorded here as the defect it is: pseudo-ampleness requires $j(C(M)^+)\intersect\Pic(X_b)^+\neq\emptyset$ in the sense of [@Dol96, §1], whose $C(M)^+$ asks for strict positivity against the chosen positive roots, whereas $e_0\cdot e_i=0$ for every one of the ten classes $e_i$ of @lem:d2-local-system(2). So $e_0\notin C(M)^+$, and being nef and big does not place it there; whether some other class of $\Pic(X_b)^+$ meets the image $j(C(M)^+)$ is not decided. The candidate $4e_0-\tsum_{i}e_i$ would need positivity against every relevant curve, which no argument on the page supplies.
4. The marked period determines the chamber $(V^+_\pi,\Delta^+_\pi)$ that [@Dol96, Thm. 3.1] uses for its fibre description.
:::

::: {.proof}
1. is @lem:d2-local-system(2) with @prop:coble-period-domain(1)--(2): the eleven classes are global sections, they span a primitive sublattice of signature $(1,10)$ isometric to $M$, and $e_0^2=2$, $e_i^2=-2$. (Primitivity is the content of @prop:coble-period-domain(2), where $T_\Co$ is computed as the orthogonal complement.)
2. $H=\OO_{\PP^2}(1)$ is nef, and $e_0=f^*H$ is the pullback along the finite morphism $f$, so it is nef; $e_0^2=2H^2=2>0$ because $f$ has degree $2$ and $H^2=1$ on $\PP^2$. A nef class with positive square on a surface is big.
3. $C(M)^+$ is the chamber of the positive cone of $M$ cut out by a choice of positive roots $\Delta(M)^+$ [@Dol96, §1]; $e_0$ lies in the positive cone of $M$ because $e_0^2=2>0$, and $e_0\in\Pic(X_b)^+$ by 2, but $e_0\notin C(M)^+$ because $e_0\cdot e_i=0$ for the ten classes $e_i$ of @lem:d2-local-system(2), whereas $C(M)^+$ asks for strict positivity against the positive roots. Whether another class of $\Pic(X_b)^+$ meets $j(C(M)^+)$ is not decided, so pseudo-ampleness is not proved.
4. is @lem:chamber-from-marked-period: the chamber is a function of the marked period, and the marking of $M$ is carried by the eleven named classes, so the data $(V^+_\pi,\Delta^+_\pi)$ of [@Dol96, Thm. 3.1] are determined by the period point.
:::

*What this would give for (iii), and what it does not.* With 1--4 and pseudo-ampleness --- the step clause 3 records as open --- [@Dol96, Thm. 3.1] would give that the period map of *marked pseudo-ample* $M$-polarized $\mathrm{K3}$ surfaces is **surjective** onto $\bD(T_\Co)$, with fibre over $\pi$ in bijection with $W_\pi(N)$; the theorem is recorded as false as stated at @rmk:coble-period-surjectivity-sources, and the replacement used below is @thm:coble-period-surjectivity. That would be a statement about the ambient moduli, and it is exactly what would make the passage to an open set unnecessary *there*: the image would be everything. It would **not** give the same for the Coble subfamily: the D2a family is a subfamily, so what would follow is that $\bD(T_\Co)$ is exhausted by pseudo-ample $M$-polarized $\mathrm{K3}$ surfaces and that the complement of the Coble period image is the image of the pseudo-ample points that are not Coble covers. Whether that complement is a proper closed *analytic* subset -- what finding (iii) needs for connectedness -- is therefore the same reconstruction question as before, not a consequence of the theorem. What the theorem would remove is the *openness* half of (iii): since the ambient image would be all of $\bD(T_\Co)$, the Coble image would be the complement of a subset of the discriminant, and its openness is [@DK13, Prop. 3.2] read on the quotient.

::: {.remark #rmk:where-the-sign-is-a-loop title="Reconciling `thm:no-loop-carries-the-sign` with $-\id\in\Gamma_\Co(B)$: they are two moduli problems"}
Two theorems of the volume, both proved, appear to disagree about the sign, and the reconciliation is that they concern different moduli problems -- which is finding (iv) again.

- @thm:coble-block-sign-in-w proves $-\id_{T_\Co}\in W(T_\Co)$, the reflection group generated by the $(-2)$-vectors; @lem:d2-vanishing-reflections(4) proves $W(T_\Co)\subseteq\Gamma_\Co(B)$, the meridians of the nodal degenerations being the reflections (Picard--Lefschetz, [@Voi07, Thm. 3.16]). Composing the two, $-\id\in\Gamma_\Co(B)$ for the labelled presentation of @def:coble-family-unpolarized, and its monodromy is carried by *loops*: the meridian about a nodal divisor is a loop of the base.
- @thm:no-loop-carries-the-sign says that over the coarse moduli space of *labelled direct, polarized* Coble data the monodromy is $\Gamma^{\mathrm{dir}}_{\Co,2}/\{\pm\id\}$: no loop carries $\iota$.

These are consistent only because the objects differ: the first is the unpolarized family over the labelled base, the second the degree-$2$ polarized construction, and the map between them is not an isomorphism of local systems. The consequence for this page is that the phrase "the loop monodromy is an index-two subgroup" is *not* available for the unpolarized family: there the sign is a reflection word, hence a loop, and no index-two gap is asserted. The stabilizer comparison @qst:coble-monodromy-equality is false (@prop:coble-monodromy-equality-false); that negative answer does not settle the sign question for the two moduli problems.
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
1. *Local finiteness.* Let $K\subset\bD$ be compact. A period in $K$ is a positive $2$-plane, and the family of these is bounded; choose $\pi_0\in\bD$ and let $\beta$ be the positive definite form $\beta(x)=-(x,x)_{\pi_0^{\perp}}+(x,x)_{\pi_0}$ on $T_\Co\otimes\RR$. On the compact $K$ the forms $\beta_\pi$ obtained by replacing $\pi_0$ by $\pi$ are uniformly equivalent to $\beta$: there is $c>0$ with $c^{-1}\beta\le\beta_\pi\le c\beta$ for all $\pi\in K$. If $\delta\perp\pi$ then $\delta\in\pi^{\perp}$, so $\beta_\pi(\delta)=-|\delta|^2$ and $\beta(\delta)\ge c^{-1}\abs{\delta}^2$. Since $\Delta(T_\Co)$ is discrete in $T_\Co\otimes\RR$ and $\beta$ is positive definite, the set of $\delta$ with $\beta(\delta)$ bounded is finite. So only finitely many hyperplanes meet $K$, and $Z$ is closed and analytic.
2. This is @thm:coble-period-surjectivity: for $\pi\notin Z$ a marking with period $\pi$ exists for which $\sigma$ is induced by an involution, its fixed locus is one smooth rational curve, and the quotient is a Coble surface whose anti-bicanonical system is a single smooth curve, with $X$ as its double cover. The marking is one whose Kähler chamber meets $M\tensor\RR$ (@thm:coble-period-surjectivity(4)); a $(-2)$-class of $\pi^{\perp}$ need not lie in $M$, and the proof does not use that. Here *labelled* means that the surface carries the isometry $\restrictionof{\varphi^{-1}}{M}$ of $M$ onto its invariant lattice; the theorem does not show that the ten classes $e_1,\dots,e_{10}$ are the classes of exceptional curves of a plane model (@rmk:coble-period-surjectivity-sources).
3. If $\pi\in H_\delta$ then $\delta\in(\pi^{\perp}\intersect T_\Co)$ is of type $(1,1)$, hence algebraic on $X_\pi$; $\sigma$ acts on it as $-1$. An automorphism of a $\mathrm{K3}$ surface preserves the effective cone, but $\delta$ and $-\delta$ cannot both be effective for $\delta^2=-2$, so a $\sigma$ realising the isometry would send an effective class to an anti-effective one, which no automorphism does. So $\sigma$ is not an automorphism and $X_\pi$ is not a Coble cover.
4. is 2 and 3 together. Connectedness is the argument of @thm:gamma-co-is-full: $Z$ is a proper closed analytic subset, a ball minus a proper analytic subset is connected, and a path meeting $Z$ can be diverted inside such a ball.
:::

*The one input that is not a numbered statement.* Local finiteness in 1 is proved above from the discreteness of $T_\Co$ and the compactness of $K$, not cited; the same fact underlies the arrangement $\calH_T$ of [@YZZ25, Thm. 3.4], whose right-hand side is the complement of that arrangement in $\bD_T$. What is *not* claimed is that $Z$ is a finite union: it is countable, and it is closed because it is locally finite. That is what allows $\bD\sm Z$ to be open -- a countable union of closed sets need not be closed, and the local finiteness is doing the work.

::: {.theorem #thm:coble-period-surjectivity title="Every period off $Z$ is the period of a marked Coble cover"}
Fix a primitive embedding $M\oplus T_\Co\subset\lkt$ with $M=\generators{2}\oplus\generators{-2}^{\oplus10}$ and $T_\Co=M^{\perp\lkt}$ (@prop:coble-period-domain), and put
$$\sigma\definedas\id_M\oplus(-\id_{T_\Co})\in\Orth(\lkt),\qquad
\Omega\definedas\theset{[\omega]\in\PP(T_\Co\tensor\CC)\ :\ \omega^2=0,\ \omega\cdot\bar\omega>0},\qquad
Z_\Omega\definedas\bigcup_{\delta\in\Delta(T_\Co)}\qty(\delta^{\perp}\intersect\Omega),$$
with $\Delta(T_\Co)=\theset{\delta\in T_\Co:\delta^2=-2}$. So $\Omega$ is the set $\Omega_{T_\Co}$ of @def:type-iv-period-domain, with both components, and the $Z$ of @prop:the-coble-locus-in-the-period-domain is $Z_\Omega\intersect\bD(T_\Co)^+$.

Let $\pi\in\Omega\sm Z_\Omega$. Then there are a $\mathrm{K3}$ surface $X$, a marking $\varphi\colon H^2(X,\ZZ)\iso\lkt$ with $\varphi_\CC\qty(H^{2,0}(X))=\pi$, and an involution $\iota$ of $X$ with $\iota^*=\varphi^{-1}\sigma\varphi$, such that:

1. $\iota$ is nonsymplectic, and $\Fix(\iota)$ is one smooth rational curve $R$.
2. $S\definedas X/\iota$ is a nonsingular projective rational surface. The quotient map $p\colon X\to S$ is the double cover branched along $C\definedas p(R)$, a smooth rational curve with $C^2=-4$, and $K_S^2=-1$.
3. $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}=\theset{C}$. So $S$ is a Coble surface in the sense of [@DK13, §3] whose anti-bicanonical system is a single smooth curve, and $(S,\ p,\ \iota)$ is an object of $\mcM_\Co$ over a point (@def:coble-moduli-functor).

Moreover:

4. *(Which markings.)* Let $(X,\varphi)$ be any marked $\mathrm{K3}$ surface with period $\pi\in\Omega\sm Z_\Omega$, and let $\mathcal K_X$ be its Kähler cone. Then $\varphi^{-1}\sigma\varphi$ is induced by an automorphism of $X$ if and only if $\varphi(\mathcal K_X)\intersect\qty(M\tensor\RR)\neq\emptyset$. For every such $(X,\varphi)$ the conclusions 1--3 hold.
5. *(Necessity.)* If $(X,\iota)$ is a $\mathrm{K3}$ surface with an involution and $\varphi$ is a marking with $\iota^*=\varphi^{-1}\sigma\varphi$, then the period $\varphi_\CC\qty(H^{2,0}(X))$ lies in $\Omega\sm Z_\Omega$.

So the set of periods of marked Coble covers is exactly $\Omega\sm Z_\Omega$.
:::

::: {.proof}
*The involution of the lattice.* The group $\lkt/(M\oplus T_\Co)$ is a subgroup of $A_M\oplus A_{T_\Co}$, and both summands are $2$-elementary, so $\id_M\oplus(-\id_{T_\Co})$ acts on $A_M\oplus A_{T_\Co}$ as the identity and preserves $\lkt$. This is the involution of [@AN06, §2.3] and [@AE22, §2A].

*Step 1: a marked surface with period $\pi$ and a prescribed chamber.* The point $\pi$ lies in the period domain of $\lkt$, so by the surjectivity of the period map [@Huy16, Theorem 7.4.1] there is a marked $\mathrm{K3}$ surface $(X,\varphi_0)$ with period $\pi$. Put
$$N_\pi\definedas\pi^{\perp}\intersect\lkt,\qquad V_\pi\definedas\pi^{\perp}\intersect\qty(\lkt\tensor\RR),\qquad \Delta_\pi\definedas\theset{\delta\in N_\pi:\delta^2=-2}.$$
Then $\varphi_0(\operatorname{NS}(X))=N_\pi$ by the Lefschetz $(1,1)$-theorem [@AEH24, §2A], $\varphi_0\qty(H^{1,1}(X,\RR))=V_\pi$, and $V_\pi$ has signature $(1,19)$ [@AEH24, §2B]. The set of vectors of positive square in $V_\pi$ has two components $P_\pi$ and $-P_\pi$. A *chamber* is a connected component of $\qty(P_\pi\sqcup-P_\pi)\sm\bigcup_{\delta\in\Delta_\pi}\delta^{\perp}$ [@AEH24, §2B, (1)].

The image $\varphi_0(\mathcal K_X)$ is a chamber. Indeed, let $\mathcal C_X\subset H^{1,1}(X,\RR)$ be the positive cone. For a class $\delta\in\operatorname{NS}(X)$ with $\delta^2=-2$, one of $\pm\delta$ is effective by the Riemann--Roch theorem [@AN06, §2.3], so a Kähler class is nonzero on $\delta$; hence $\mathcal K_X$, which is connected, lies in one connected component $\mathcal C_0$ of $\mathcal C_X\sm\bigcup\delta^{\perp}$. For a smooth rational curve $E\subset X$ the class $[E]$ has square $-2$, so $\alpha\mapsto\alpha\cdot E$ has no zero on $\mathcal C_0$; it is positive on $\mathcal K_X\subseteq\mathcal C_0$, hence positive on $\mathcal C_0$. By the description of the Kähler cone [@Huy16, Theorem 8.5.2], $\mathcal C_0\subseteq\mathcal K_X$. So $\mathcal K_X=\mathcal C_0$.

Let $\mathcal C$ be any chamber. The Weyl group $W_X$, generated by the reflections in the classes of square $-2$ of $\operatorname{NS}(X)$, acts simply transitively on the set of chambers of $\mathcal C_X$ [@Huy16, Proposition 8.5.5], and $-\id$ exchanges $\mathcal C_X$ and $-\mathcal C_X$. So there are $w\in W_X$ and $\epsilon\in\theset{\pm1}$ with $\epsilon\,\varphi_0\qty(w(\mathcal K_X))=\mathcal C$. Put $\varphi\definedas\epsilon\,\varphi_0\circ w$. It is a marking of $X$ with $\varphi(\mathcal K_X)=\mathcal C$. Its period is $\pi$: each reflection of $W_X$ is the identity on $H^{2,0}(X)$ [@Huy16, §8.5.2], and $\epsilon$ acts trivially on $\PP(\lkt\tensor\CC)$.

*Step 2: a chamber that meets $M\tensor\RR$.* The space $M\tensor\RR$ lies in $V_\pi$, because $M\perp T_\Co$ and $\pi\in\PP(T_\Co\tensor\CC)$; it has signature $(1,10)$, so its set $P^M$ of vectors of positive square is open and nonempty in it. Let $\delta\in\Delta_\pi$. If $M\tensor\RR\subseteq\delta^{\perp}$, then $\delta\in M^{\perp\lkt}=T_\Co$, so $\delta\in\Delta(T_\Co)$ and $\delta\perp\pi$, that is $\pi\in Z_\Omega$, which is excluded. Hence $\delta^{\perp}\intersect\qty(M\tensor\RR)$ is a proper linear subspace of $M\tensor\RR$ for every $\delta\in\Delta_\pi$. The set $\Delta_\pi$ is countable, and a countable union of proper linear subspaces has empty interior. So there is $h\in P^M$ with $h\cdot\delta\neq0$ for all $\delta\in\Delta_\pi$, and $h$ lies in exactly one chamber $\mathcal C_h$.

This step uses only that no element of $\Delta_\pi$ lies in $T_\Co$. An element of $\Delta_\pi$ outside $M\cup T_\Co$ is allowed: its hyperplane meets $M\tensor\RR$ in a proper subspace and subdivides the chambers, and it does not obstruct the argument.

*Step 3: $\sigma$ is induced by an involution.* By step 1 take $\varphi$ with $\varphi(\mathcal K_X)=\mathcal C_h$, and put $\sigma_X\definedas\varphi^{-1}\sigma\varphi$. It is a Hodge isometry of $H^2(X,\ZZ)$, because $\sigma$ acts on $T_\Co\tensor\CC$ as $-1$ and so fixes the point $\pi$. The class $\kappa\definedas\varphi^{-1}(h)$ is a Kähler class, and $\sigma_X(\kappa)=\kappa$ because $h\in M\tensor\RR$. So $\sigma_X(\mathcal K_X)\intersect\mathcal K_X\neq\emptyset$, and by the global Torelli theorem [@Huy16, Theorem 7.5.3] there is a unique automorphism $\iota$ of $X$ with $\iota^*=\sigma_X$. Then $(\iota^2)^*=\id$, so $\iota^2=\id$ [@Huy16, Proposition 15.2.1], and $\iota\neq\id$. It acts on $H^{2,0}(X)$ as $-1$, so it is nonsymplectic.

*Step 4: the fixed locus.* The invariant lattice $H^2(X,\ZZ)^{\iota}=\varphi^{-1}(M)$ has rank $r=11$ and discriminant group $(\ZZ/2)^{11}$, so $a=11$. Since $(r,a)$ is neither $(10,8)$ nor $(10,10)$, the fixed locus is $C_g+E_1+\dots+E_k$, a disjoint union of a nonsingular curve of genus $g=(22-r-a)/2$ and $k=(r-a)/2$ nonsingular rational curves [@AN06, §2.3; @AE22, §2A, (1)]. Here $g=0$ and $k=0$: the fixed locus is one smooth rational curve $R$. This is 1.

*Step 5: the quotient.* The pair $\qty(S=X/\iota,\ C=p(R))$ is a right DPN pair [@AN06, §2.1]: $S$ is a nonsingular projective surface with $q(S)=0$, and $C\in\abs{-2K_S}$ is nonsingular [@AN06, Definition 2.1]; since $C\neq\emptyset$, $S$ is rational [@AN06, §2.1]; and $p$ is a double cover branched along $C$, given by a line bundle $L^{-1}$ on $S$ with $L^{-2}\cong\OO_S(C)$ and $p^*L^{-1}\sim R$ [@AN06, §2.1]. The Picard group of a rational surface has no torsion, so $L^{-1}=-K_S$: $p$ is the double cover branched along $C$ defined by $-K_S$, and $p^*(-K_S)\sim R$. The map $p$ restricts to an isomorphism $R\to C$, so $C$ is a smooth rational curve. From $p^*C=2R$, $(p^*C)^2=2C^2$ and $R^2=-2$ one gets $C^2=-4$, and $C\sim-2K_S$ gives $K_S^2=-1$. This is 2.

*Step 6: the anti-canonical systems.* Pullback of sections is an injection $H^0\qty(S,\OO_S(C))\injects H^0\qty(X,\OO_X(2R))$. Let $D\in\abs{2R}$. Then $D\cdot R=-4<0$, so $R$ is a component of $D$; and $(D-R)\cdot R=-2<0$, so $R$ is a component of $D-R$; then $D-2R$ is effective and linearly equivalent to $0$, so $D=2R$. Hence $h^0\qty(X,\OO_X(2R))=1$, so $h^0\qty(S,\OO_S(-2K_S))=1$ and $\abs{-2K_S}=\theset{C}$. If $D'\in\abs{-K_S}$, then $2D'\in\abs{-2K_S}$, so $2D'=C$; this is impossible because $C$ is reduced. Hence $\abs{-K_S}=\emptyset$. So $S$ is a nonsingular projective rational surface with $\abs{-K_S}=\emptyset$ and $\abs{-2K_S}\neq\emptyset$, which is the definition of a Coble surface [@DK13, §3], and $\abs{-2K_S}$ is the single smooth curve $C$. The triple $(S,p,\iota)$ meets the three clauses of @def:coble-moduli-functor over a point: $p$ is the double cover branched along $C$ defined by $-K_S$, and $\iota$ is its covering involution. This is 3.

*Proof of 4.* If $\varphi(\mathcal K_X)$ contains a point $h\in M\tensor\RR$, then step 3 applies to this $\varphi$ and gives $\iota$; steps 4--6 use only $\iota^*=\varphi^{-1}\sigma\varphi$. Conversely, let $\varphi^{-1}\sigma\varphi=\iota^*$ for an automorphism $\iota$, and let $\kappa\in\mathcal K_X$. An automorphism preserves the Kähler cone, which is convex, so $\kappa+\iota^*\kappa\in\mathcal K_X$; this class is $\iota^*$-invariant, so $\varphi(\kappa+\iota^*\kappa)$ is $\sigma$-invariant and lies in $M\tensor\RR$.

*Proof of 5.* Let $\delta\in\Delta(T_\Co)$ be orthogonal to the period. Then $\varphi^{-1}(\delta)\in\operatorname{NS}(X)$ has square $-2$, so one of $\pm\varphi^{-1}(\delta)$ is effective, and $\iota^*$ maps it to its negative. An automorphism maps effective classes to effective classes, and a nonzero class and its negative are not both effective, because a Kähler class is positive on every effective class. So no such $\delta$ exists [@AN06, §2.3].
:::

::: {.remark #rmk:coble-period-surjectivity-sources title="What the sources give for the surjectivity onto $\bD\sm Z$, and what the theorem does not state"}
- *The same statement for a general isometry.* For an isometry $\rho$ of finite order of $\lkt$, [@AEH24, Lemma 2.6] states that a marking of a surface with period $x$ is a $\rho$-marking if and only if $x\in\mathbb D_\rho\sm\Delta_\rho$ and the image of the marking contains an ample class in the invariant lattice, and its proof shows that for each $x\in\mathbb D_\rho\sm\Delta_\rho$ a chamber that meets the invariant lattice exists. For $\rho=\sigma$ the domain $\mathbb D_\rho$ is $\Omega$ and the discriminant $\Delta_\rho$ of [@AEH24, Definition 2.5], taken over the roots of the orthogonal complement of the invariant lattice, is $Z_\Omega$. Steps 1--3 above are that proof, with each input referred to a numbered statement of [@Huy16]. For involutions the statement is also the sentence of [@AN06, §2.3] that lifts the lattice involution to the surface by the global Torelli theorem when the orthogonal complement of $S$ in the Picard lattice has no element of square $-2$.
- *The quotient type.* The fixed locus and the rationality of the quotient for the invariants $(r,a,\delta)=(11,11,1)$ are Nikulin's classification as stated in [@AN06, §2.1, §2.3] and [@AE22, §2A]. Step 6 is proved here.
- *What [@DK13] gives.* [@DK13, Prop. 3.2] states that the moduli space of the classical Coble surfaces is isomorphic to an open subset of $\mathcal D(N)/\Orth(N)$. It does not say which open subset, and the source restricts itself to the blow-ups of the ten nodes of a plane sextic [@DK13, §3]. It does not give @thm:coble-period-surjectivity.
- *No lattice-polarized period theorem is used.* The proof uses neither [@Dol96, Thm. 3.1] nor a pseudo-ample polarization. [@AEH24, Remark 2.10] records that [@Dol96, Thm. 3.1] is false as stated.
- *What the theorem does not state.* It does not state that $S$ is the blow-up of $\PP^2$ at the ten nodes of an irreducible sextic. @def:coble-moduli-functor does not ask for a plane model, so the theorem needs none. Every surface of clause 3 has one: it is the blow-up of $\PP^2$ at ten points carrying double points of an irreducible rational sextic (@thm:coble-smooth-antibicanonical-is-a-plane-blowup). The ten double points are ten distinct nodes for the objects of an open dense substack, and not for all objects (@thm:coble-classical-substack-is-open-dense-and-proper).
- *It does not state that the marking is unique.* By clause 4 the marked surfaces over $\pi$ that carry the involution correspond to the chambers that meet $M\tensor\RR$; there is more than one.
:::

::: {.remark #rmk:two-arrangements-two-bases title="Two arrangements, two objects: the Coble locus in the period domain, and the base of the D2a family"}
@prop:the-coble-locus-in-the-period-domain and @lem:d2-vanishing-reflections(2) are both true and are about different things, and the difference is recorded by the volume itself.

- *The Coble locus.* $Z$ is the union of the hyperplanes of the $(-2)$-vectors **of $T_\Co$** (@prop:the-coble-locus-in-the-period-domain). Its complement is the set of periods realised by some Coble cover, because the criterion for the marking's involution to be an automorphism is that no $(-2)$-class of $T_\Co$ become algebraic.
- *The base of the family.* The arrangement of the D2a family, $\calH_T$, is strictly larger: its components are the $\gamma^{\perp}$ for the classes $\gamma$ with $\gamma^2\in\set{0,-4,-6,-8}$ of @lem:d2-arrangement-classes, and the components of $\calH_T$ are the divisors along which a member degenerates (@lem:d2-vanishing-reflections(2)). So $B$ is *not* the complement of $Z$; the page already records the weaker and correct statement, that @lem:d2a-family-is-yzz gives $B$ as the labelled moduli space of the family and @lem:d2a-period-map gives its classifying map into $\bD(T_\Co)/\Gamma_\Co$, with $\calH_T$ not identified with a locus in the period domain independently of the family.

So the D2a base $B$ is **not** all of $\bD\sm Z$ modulo $\Gamma_\Co$: it is the complement of the larger arrangement, and it is a proper open subset of the Coble locus as soon as $Z\neq\calH_T$, which is what @lem:d2-arrangement-classes shows. The passage from the family's base to the whole Coble locus is exactly the reconstruction step that @conj:gamma-co-orbifold-equality needs, not a consequence of either arrangement being closed.

*Why $Z$ is closed.* The argument is the one in the proof of @prop:the-coble-locus-in-the-period-domain, and its mechanism is the proper discontinuity of the lattice action rather than a compactness count: $\Orth(T_\Co)$ acts properly discontinuously on $\bD(T_\Co)$, so every compact set meets only finitely many of the hyperplanes $H_\delta$ with $\delta\in\Delta(T_\Co)$; the union is therefore locally finite, and a locally finite union of closed analytic subsets is closed analytic. What is *not* used, and would be false, is that the union is finite: it is countable, and it is closed only because it is locally finite.
:::

*The index $\qty[\widetilde\Orth^+(T_\Co):\Gamma_\Co(B)]$, which is now this page's.* Three facts are in place: $\Gamma_\Co(B)\subseteq\widetilde\Orth^+(T_\Co)$ (@thm:gamma-co-is-stable(1)); $W(T_\Co)\subseteq\Gamma_\Co(B)$ (@lem:d2-vanishing-reflections(4)); and $-\id_{T_\Co}\in W(T_\Co)$ (@thm:coble-block-sign-in-w), so $-id$ lies in $\Gamma_\Co(B)$ for the unpolarized labelled family, the sign being carried by a meridional loop (@rmk:where-the-sign-is-a-loop). The index is therefore a divisor of $\qty[\widetilde\Orth^+(T_\Co):W(T_\Co)]$, and no longer constrained to be two: the earlier "index-two" reading is withdrawn (@rmk:where-the-sign-is-a-loop). Whether it is $1$ is @qst:gamma-co-sign-is-realised; the further identification of $\Gamma_\Co(B)$ with the stack group in @conj:gamma-co-orbifold-equality is research#797, item 6.

::: {.remark #rmk:the-two-steps-and-where-they-fail title="Surjectivity onto $\bD\sm Z$ and the torsor with isotropy $\{\id,\iota\}$: the first step that fails"}
Two steps would give @conj:gamma-co-orbifold-equality outright. Neither is closed, and the first failure is inside the first step.

**Step 1, surjectivity onto $\bD\sm Z$.** This step is @thm:coble-period-surjectivity. For $\pi\in\bD\sm Z$ there is a marked $\mathrm{K3}$ surface $(X_\pi,\varphi)$ with period $\pi$ on which $\sigma=\id_M\oplus(-\id_{T_\Co})$ is induced by an involution; its fixed locus is one smooth rational curve, and $S_\pi=X_\pi/\sigma$ is a rational surface with $\abs{-K}=\emptyset$ and $\abs{-2K}$ a single smooth curve, so it is an object of @def:coble-moduli-functor. The proof takes the surface from the surjectivity of the period map of marked $\mathrm{K3}$ surfaces and the involution from the global Torelli theorem; it uses no lattice-polarized period theorem.

**What step 1 does not give.** It does not show that $S_\pi$ is $\Bl_{p_1,\dots,p_{10}}\PP^2$ at the ten nodes of an irreducible sextic with the ten marked classes $e_1,\dots,e_{10}$ realised by the exceptional curves. @def:coble-moduli-functor does not ask for that, so the surjectivity onto $\bD\sm Z$ holds for the functor as it is defined. A plane model always exists (@thm:coble-smooth-antibicanonical-is-a-plane-blowup), but a statement about the labelled plane-model family needs the ten blown-up points to be ten distinct nodes, which holds on an open dense substack and fails at $S_{Z_8}$ (@thm:coble-classical-substack-is-open-dense-and-proper).

**Step 2, the torsor with isotropy $\{\id,\iota\}$.** Granting step 1, the period map from the labelled stack to $\qty[\widetilde\Orth^+(T_\Co)\backslash(\bD\sm Z)]$ is bijective on objects up to isomorphism and exhibits the labelled stack as a torsor over the quotient. The isotropy is **not** $\{\id,\iota\}$ everywhere, and this is the second failure: at a special member the stabiliser of the period is strictly larger than $\{\pm\id\}$, the plane-model image being the full isotropy there and not only the sign. So the torsor statement holds over the dense open locus where the stabiliser is exactly $\{\pm\id\}$ and not over all of $\bD\sm Z$.

**What that leaves.** Over that open locus the orbifold argument gives the equality, and there the monodromy group is the full group; globally it does not. So @conj:gamma-co-orbifold-equality stays a conjecture. Step 1 is closed by @thm:coble-period-surjectivity for the functor of @def:coble-moduli-functor; step 2, the description of the stabiliser at the special members of the period domain, is not closed.
:::

::: {.remark #rmk:which-coble-surfaces-have-a-plane-model title="Which Coble surfaces are blow-ups of the ten nodes of a plane sextic: the functor's class, and the wider class it is not"}
The reconstruction that @rmk:the-two-steps-and-where-they-fail needs is @thm:coble-smooth-antibicanonical-is-a-plane-blowup: every object of @def:coble-moduli-functor is a blow-up of $\PP^2$ at ten double points of an irreducible rational sextic. What this remark records is that this is a theorem about the functor's class and not about the whole class of Coble surfaces, which is where the earlier doubt about it came from.

[@DZ99, Rem. 2.9] divides Coble surfaces into two classes, those of *elliptic type* and those of *rational type*, according to the mobile part of $\abs{-2K}$; the classical surfaces of @def:coble-family-unpolarized are the blow-ups of $\PP^2$ at the ten nodes of an irreducible rational plane sextic of degree $6$. The class is strictly larger: [@DZ99] notes that for each $n$ there are Coble surfaces of rational type admitting no birational morphism to the minimal ruled surface $F_n$, hence no plane model at all, and [@DZ99, Ex. 6.10] exhibits a Coble surface on which the finiteness of negative rational curves modulo automorphisms fails, so it is not one of the classical ones either.

Consequently the two objects on this page are different classes, and the strictness just recalled is a statement about the first and not about the second:

- @def:coble-family-unpolarized defines a Coble surface as a nonsingular projective rational surface with $\abs{-K}=\emptyset$ and $\abs{-2K}\neq\emptyset$ --- [@DZ99, Introduction] --- which is the whole class;
- @def:coble-moduli-functor admits as objects the families whose geometric fibres are the Coble surfaces with $\abs{-2K}$ a single smooth curve; the surfaces $\Bl_{p_1,\dots,p_{10}}\PP^2$ of @lem:d2-unpolarised-family(1), with the ten classes of @lem:d2-local-system(2) present as the exceptional curves, are the classical members of that class.

So step 1 of @rmk:the-two-steps-and-where-they-fail produces an object of the functor for every period in $\bD\sm Z$ (@thm:coble-period-surjectivity). Each of these objects has a plane model, by @thm:coble-smooth-antibicanonical-is-a-plane-blowup: it is the blow-up of $\PP^2$ at ten double points of an irreducible rational sextic, which are ten distinct nodes exactly for the classical objects, an open dense substack (@thm:coble-classical-substack-is-open-dense-and-proper). The period map of the D2a family reaches the classical members.

*`[@DZ99, Prop. 6.4(1)]` read exactly, and what it does not give.* The statement is: the minimal resolution $X$ of a rational log Enriques surface $\bar X$ of index $2$ is a Coble surface with $h^0(-2K_X)=1$ whose only anti-bicanonical divisor is a reduced divisor with one connected component, either a single $(-4)$-curve or the chain $(-3)$-$(-2)$-$(-2)$-$(-3)$; the converse also holds. Its conclusion is thus about *resolutions of log Enriques surfaces*, not about plane models, and it does not say that a Coble surface with $h^0(-2K)=1$ and a single smooth $(-4)$-curve is the blow-up of ten nodes of an irreducible sextic. For the $S_\pi$ of @rmk:the-two-steps-and-where-they-fail, $h^0(-2K_{S_\pi})=1$ holds by @thm:coble-period-surjectivity(3), and the anti-bicanonical divisor is a single $(-4)$-curve. So Prop. 6.4(1) identifies $S_\pi$ as the minimal resolution of a rational log Enriques surface of index $2$, which by [@DZ99, Prop. 6.4(3)] is the same as being the resolution of a rational surface with a single $\tfrac14(1,1)$ point; that is not the statement that $S_\pi$ is $\Bl_{p_1,\dots,p_{10}}\PP^2$ at the ten nodes of an irreducible sextic. The identification of the classical Coble surfaces with the resolution of a $\tfrac14(1,1)$-point quotient of a plane is the content that would give the plane model, and it is not in that proposition. What gives it is [@DZ99, Theorem 4.3]: the surfaces of the functor are of elliptic type with respect to a $(-1)$-curve, and that theorem makes them basic — step *4* of @thm:coble-smooth-antibicanonical-is-a-plane-blowup. The ten centres need not be ten distinct nodes (@ex:coble-sextics-with-an-a15-point).

:::

::: {.lemma #lem:every-object-of-the-functor-is-labellable title="Every object of the functor carries a marking of $M$, and $\iota$ preserves it"}
Let $(S,X\xrightarrow{\pi}S,\iota)$ be an object of @def:coble-moduli-functor in the narrowed class of the functor -- a Coble surface whose anti-bicanonical system has a smooth member $C$ that is **connected** -- with $\pi$ the double cover branched along it. Then the invariant lattice $H^2(X,\ZZ)^{\iota}$ is isometric to $M=S_\Co=\generators{2}\oplus\generators{-2}^{\oplus10}$, so the object admits a marking $\psi\colon M\iso H^2(X,\ZZ)^{\iota}$, and every such marking is preserved by $\iota$. Without the connectedness hypothesis the statement is false, and the functor as written admits the counterexample: for $C=C_1\sqcup\dots\sqcup C_n$ a disjoint union of $n$ smooth $(-4)$-curves the fixed locus has Euler characteristic $2n$, so the Lefschetz count gives $\rank H^2(X,\ZZ)^{\iota}=10+n$, not $11$, and the marking of $M$ does not exist. The functor must therefore be restricted to $n=1$ for this lemma, and that restriction is not yet part of @def:coble-moduli-functor.
:::

::: {.proof}
The fixed locus of $\iota$ is the branch curve $C$, a smooth rational curve, so $\chi(\Fix\iota)=2$; the Lefschetz count $\chi(\Fix\iota)=2\rank H^2(X,\ZZ)^{\iota}-20$ gives rank $11$. The invariant lattice of a nonsymplectic involution is even and $2$-elementary, of signature $(1,10)$ here, and its discriminant form is that of the $(-1)$-eigenspace with the sign reversed; by Nikulin's classification of $2$-elementary lattices [@Nik80, Thm. 3.6.2] the invariants $(\delta;t_+,t_-,a)=(1;1,10,11)$ determine it, and the lattice with those invariants is $\generators{2}\oplus\generators{-2}^{\oplus10}=M$ (@prop:coble-invariant-lattice, @prop:coble-period-domain(1)). A marking is an isometry onto that lattice, and it exists because the two lattices are isometric. Finally $\iota$ acts as $+\id$ on its own invariant lattice, so it preserves every marking of it.
:::

::: {.theorem #thm:gamma-co-labelled-equality title="The labelled equality: $\rho^{\mathrm{lab}}\qty(\pi_1)=\widetilde\Orth^+(T_\Co)$ over the locus where the isotropy is the sign"}
Let $\mcM^{\mathrm{lab}}_\Co$ be the stack whose objects are the objects of @def:coble-moduli-functor together with a marking $\psi$ of @lem:every-object-of-the-functor-is-labellable, let $U=\bD(T_\Co)^+\sm Z$ be the complement of the $(-2)$-arrangement (@prop:the-coble-locus-in-the-period-domain), and let $\mcM^{\mathrm{gen}}\subseteq\mcM^{\mathrm{lab}}_\Co$ be the substack where the automorphism group of a labelled object is exactly $\{\id,\iota\}$. Assume that

(i) $\mcM^{\mathrm{gen}}$ is open and nonempty,
(ii) every period of $U$ is realised by an object of $\mcM^{\mathrm{gen}}$,
(iii) two labelled objects of $\mcM^{\mathrm{gen}}$ with the same period are isomorphic,
(iv) the image $U^{\mathrm{gen}}$ of $\mcM^{\mathrm{gen}}$ is open and connected, and
(v) the tautological system of $\qty[\widetilde\Orth^+(T_\Co)\backslash U^{\mathrm{gen}}]$ is a local system on the stack whose pullback along the chart $U^{\mathrm{gen}}\to\qty[\widetilde\Orth^+(T_\Co)\backslash U^{\mathrm{gen}}]$ is the equivariant system $(U^{\mathrm{gen}}\times T_\Co)/G$ --- the descent along the $2$-morphisms of the site, which @lem:tautological-system-descends does not construct (@rmk:the-descent-stops-at-the-2-morphisms, research#797, item 4).

Then:

1. the period map induces an equivalence $\mcM^{\mathrm{gen}}\to\qty[\widetilde\Orth^+(T_\Co)\backslash U^{\mathrm{gen}}]$ onto an open substack, with the isotropy $\{\id,\iota\}$ on both sides;
2. the monodromy representation of $T_\Co$ on $\pi_1\qty(\mcM^{\mathrm{gen}})$ has image $\widetilde\Orth^+(T_\Co)$;
3. hence $\rho^{\mathrm{lab}}\qty(\pi_1)=\widetilde\Orth^+(T_\Co)$ there. What is not asserted, here or anywhere on this page, is the identification of that group with $\Gamma_\Co$ of @def:gamma-co-groups(1): that is the comparison of the labelled stack with the stack of @def:coble-moduli-functor, it is research#797, item 6, and it is open. This is *not* a computation of the global group and no "closure" or "enlargement by the isotropy of the special members" is asserted: monodromy is not continuous for dense open inclusions, a nontrivial local system on $S^1$ having trivial monodromy on $S^1\setminus\pt$, so a generic computation does not give the group on the whole stack.
:::

::: {.proof}
1. Surjectivity onto $U$: a period off $Z$ is realised by an object of the functor (@rmk:the-two-steps-and-where-they-fail with the narrowed class of the functor), and @lem:every-object-of-the-functor-is-labellable supplies the marking. Injectivity on objects and uniqueness up to the isotropy: two labelled objects with the same period are isomorphic (@thm:coble-period-map-of-the-stack(2)), and the isomorphisms are the automorphisms of either, which are $\{\id,\iota\}$ on $\mcM^{\mathrm{gen}}$ by definition. So the period map is an equivalence onto an open substack with the same isotropy, and $U^{\mathrm{gen}}$ is its image.
2. $U^{\mathrm{gen}}\to[U^{\mathrm{gen}}/G]$ is a $G$-torsor with $G=\widetilde\Orth^+(T_\Co)$, a covering of topological stacks in the sense of Noohi's Definition 18.10, so Noohi's Theorem 18.19 with Corollary 18.20 give $1\to\pi_1(U^{\mathrm{gen}})\to\pi_1([U^{\mathrm{gen}}/G])\to G\to1$, and the local system is the pullback of the tautological one, whose monodromy has image $G$ for the defining action of $G$ on $T_\Co$: the monodromy is the per-loop transport $\varphi(g)^{-1}$ on the pair $(g,\widetilde\gamma)$ (@lem:orbifold-monodromy-of-a-nonfree-quotient(2)), with image $\varphi(G)=G$, and that these transports are those of a local system on the quotient is (v), assumed and not proved.
3. is 1 and 2. The group obtained is the monodromy of the labelled generic substack; identifying it with $\Gamma_\Co$ of @def:gamma-co-groups(1) is research#797, item 6 and is not done.
:::

*The hypotheses, all stated in the theorem and none proved.* Clause 1 needs $\Aut$ of a labelled object to be exactly $\{\id,\iota\}$, which is a genericity statement at a special member strictly larger (@thm:sign-is-isotropy's normaliser and the plane-model image of 18c07a9cd7); it needs no object with $n>1$ anti-bicanonical components, since @lem:every-object-of-the-functor-is-labellable requires connectedness of $C$ and the functor does not impose it; and it needs openness, nonemptiness and connectedness of $\mcM^{\mathrm{gen}}$ and $U^{\mathrm{gen}}$, none of which is proved; and it needs (v), because $\qty[\widetilde\Orth^+(T_\Co)\backslash U^{\mathrm{gen}}]$ is a stack with isotropy, so the descent along the $2$-morphisms is exactly what makes its tautological system a local system on it. A generic open substack is also not the owner's object: @def:gamma-co-groups(1) defines $\Gamma_\Co$ on the universal family over the whole stack. So this theorem is a statement about $\mcM^{\mathrm{gen}}$ and about nothing else, and @conj:gamma-co-orbifold-equality remains the global statement with all of the above open.

::: {.proposition #prop:the-generic-locus-sees-the-whole-group title="The generic substack's fundamental group surjects, so the generic monodromy is the global monodromy"}
Let $\mcM$ be the stack of @def:coble-moduli-functor over $\CC$ with the analytic topology, assumed smooth and connected, and let $\mcM^{\mathrm{gen}}\subseteq\mcM$ be an open substack whose complement is a closed analytic substack of positive codimension. Then:

1. The map $i_*\colon\pi_1(\mcM^{\mathrm{gen}})\to\pi_1(\mcM)$ induced by the inclusion is **onto**.
2. Consequently, for the local system $T_\Co$ on $\mcM$ and its restriction to $\mcM^{\mathrm{gen}}$, $\rho^{\mathrm{gen}}=\rho\circ i_*$ and
$$\Gamma_\Co=\rho\qty(\pi_1(\mcM))=\rho^{\mathrm{gen}}\qty(\pi_1(\mcM^{\mathrm{gen}})).$$
A computation on the generic substack therefore computes the global monodromy group (@def:transport-and-monodromy), and no "enlargement" is involved.
:::

::: {.proof}
1. A loop (@def:based-loop) of $\mcM$ is a compact one-dimensional object and the complement $Z=\mcM\sm\mcM^{\mathrm{gen}}$ is a closed analytic substack of positive codimension, so the loop can be perturbed off $Z$ rel base point, and the perturbation is a homotopy of loops in $\mcM$; hence every class in $\pi_1(\mcM)$ has a representative lying in $\mcM^{\mathrm{gen}}$, which is exactly the surjectivity. For the scheme case this is [SGA 1, Exposé X, Corollaire 3.3], which states more: for $X$ locally noetherian and normal and $Z\subset X$ closed of codimension $\ge2$, the map $\pi_1(X\sm Z)\to\pi_1(X)$ is an isomorphism, and it is therefore onto under the weaker hypothesis of codimension $\ge1$ used here, the proof being the same perturbation.
2. $\rho^{\mathrm{gen}}=\rho\circ i_*$ is the definition of the restriction of a local system; with $i_*$ onto by 1, the two images coincide.
:::

*Why the review's $S^1$ example does not apply.* There the dense open is $S^1\sm\pt$, whose complement is a point in a one-dimensional space, that is of codimension $0$; the map $\pi_1(S^1\sm\pt)\to\pi_1(S^1)$ is $1\to\ZZ$ and is not onto, so the example illustrates precisely the hypothesis that clause 1 needs and satisfies it in no way. In a complex space a closed analytic substack of positive codimension has real codimension at least $2$, a loop can be moved off it, and the example has no analogue.

::: {.lemma #lem:the-special-isotropy-locus-is-proper title="The special-isotropy locus is a proper closed analytic substack, so its complement has positive codimension"}
Let $G=\widetilde\Orth^+(T_\Co)$ act on $\bD=\bD(T_\Co)^+$, and let
$$Z_{\mathrm{sp}}\definedas\bigcup_{g\in G,\ g\neq\pm\id}\Fix(g)$$
be the locus of periods whose stabiliser is strictly larger than $\{\pm\id\}$. Then each $\Fix(g)$ is a proper closed analytic subset (@def:closed-analytic-subset) of $\bD$, the union is locally finite, $Z_{\mathrm{sp}}$ is a proper closed analytic subset, and its complement has positive codimension. Hence $\mcM^{\mathrm{gen}}$ has complement of positive codimension in $\mcM$, and @prop:the-generic-locus-sees-the-whole-group applies to it.
:::

::: {.proof}
$\Fix(g)$ is the fixed locus of an isometry of the period domain: it is closed analytic, and it is proper because an isometry of $\bD$ which fixes an open set is the identity, so for $g\neq\id$ the fixed locus has empty interior. Local finiteness: $G$ acts properly discontinuously on $\bD$, so for a compact $K\subset\bD$ only finitely many $g$ satisfy $gK\intersect K\neq\emptyset$, and only those can fix a point of $K$; hence only finitely many of the sets $\Fix(g)$ meet $K$. A locally finite union of proper closed analytic subsets is closed analytic and proper, so its complement is open and dense, with complement of positive codimension. The last sentence is @prop:the-generic-locus-sees-the-whole-group(1) applied with $\mcM^{\mathrm{gen}}$ the complement of $Z_{\mathrm{sp}}$.
:::

::: {.theorem #thm:gamma-co-is-the-stack-monodromy title="The monodromy group of the Coble moduli stack: $\Gamma_\Co=\widetilde\Orth^+(T_\Co)$, with every input listed"}
Let $\mcM_\Co$ be the stack of @def:coble-moduli-functor, in the class the definition now states (a single smooth anti-bicanonical curve, invariant lattice $M$ of the $(11,11,1)$ type), let $\bD=\bD(T_\Co)^+$, $Z$ the $(-2)$-arrangement of @prop:the-coble-locus-in-the-period-domain and $\mcM^{\mathrm{gen}}$ the complement of the special-isotropy locus of @lem:the-special-isotropy-locus-is-proper. Assume that

(A1) $\mcM_\Co$ is smooth and connected,
(A2) the hypotheses (H1)--(H3) of @prop:coble-monodromy-is-the-marking-group hold for the generic substack,
(A3) the quotient-descent equivalence holds for the equivariant local systems used below: $G$-equivariant local systems of lattices on $U^{\mathrm{gen}}$ correspond to local systems of lattices on $[U^{\mathrm{gen}}/G]$, with pullback along $U^{\mathrm{gen}}\to[U^{\mathrm{gen}}/G]$ inverse to descent, including the comparisons along $2$-morphisms and their cocycle conditions. This is research#797, item 4, the descent left open by @rmk:the-descent-stops-at-the-2-morphisms, and is not proved here, and
(A4) the generic substack $\mcM_\Co^{\mathrm{gen}}$ is equivalent to the generic substack of the labelled stack $\mcM_\Co^{\mathrm{lab}}$ of @thm:coble-period-map-of-the-stack, and under the equivalence the local system $\bT$ of the VHS on the universal family over $\mcM_\Co$ is the local system of the labelled stack. This is the comparison of the labelled presentation with the stack, research#797, item 6; on the generic locus it includes $\Gamma_\Co=\Gamma_\Co(B)$, and it is not proved here.

Then
$$\Gamma_\Co=\rho\qty(\pi_1(\mcM_\Co))=\widetilde\Orth^+(T_\Co).$$
:::

::: {.proof}
*The chain.* By (A4), the generic substack on which the computation is made is the generic labelled stack of steps (a)--(e), and its local system is that of the universal family over $\mcM_\Co$. (a) Every period in $\bD\sm Z$ is realised by an object of $\mcM_\Co$, and every object has a marking of $M$ preserved by $\iota$: @thm:coble-period-surjectivity for existence, and @lem:every-object-of-the-functor-is-labellable for the marking. (b) Two labelled objects with the same period are isomorphic up to the isotropy (@thm:coble-period-map-of-the-stack(2)), and the differential is an isomorphism (@thm:coble-period-map-of-the-stack(3)). (c) On $\mcM^{\mathrm{gen}}$ the isotropy is exactly $\{\id,\iota\}$, so the period map is an equivalence onto an open substack of $\qty[\widetilde\Orth^+(T_\Co)\backslash\bD]$ (@prop:coble-monodromy-is-the-marking-group(1)). (d) the $G$-torsor is $U^{\mathrm{gen}}\to\qty[U^{\mathrm{gen}}/G]$ with $G=\widetilde\Orth^+(T_\Co)$, hence a covering of topological stacks, and Noohi's Theorem 18.19 with Corollary 18.20 (*Foundations of topological stacks I*, arXiv:math/0503247; Definition 18.10 for the coverings) give $1\to\pi_1(U^{\mathrm{gen}})\to\pi_1(\qty[U^{\mathrm{gen}}/G])\to G\to1$ with the last map onto (@prop:coble-monodromy-is-the-marking-group(2)); the period map is not a further torsor, and by (c) it is an equivalence, so this is the sequence of $\mcM^{\mathrm{gen}}$ as well. (e) Given (A2), hence (H3), together with the full equivalence (A3), the local system is the pullback (@def:pullback-of-local-system) of a local system on the quotient, and its monodromy is the per-loop transport $\varphi(g)^{-1}$ (@lem:orbifold-monodromy-of-a-nonfree-quotient(2)), with image $G$ for the defining action of $G$ on $T_\Co$; the transports are what @lem:tautological-system-descends constructs, and that they are the monodromy of a local system on the stack is (H3), with (A3) stating the underlying equivariant-system/stack-system equivalence explicitly, not a conclusion of that lemma (@rmk:the-descent-stops-at-the-2-morphisms, research#797, item 4). (f) The inclusion $\mcM^{\mathrm{gen}}\subset\mcM_\Co$ induces a surjection on $\pi_1$, the complement being a closed analytic substack of positive codimension and the loop being compact one-dimensional (@prop:the-generic-locus-sees-the-whole-group(1), with @lem:the-special-isotropy-locus-is-proper). Hence, with (A4), $\rho(\pi_1(\mcM_\Co))=\rho^{\mathrm{gen}}(\pi_1(\mcM^{\mathrm{gen}}))=G$.

*Every input, with its status.*

| input | supplies | status |
|---|---|---|
| @def:coble-moduli-functor (narrowed class) | the objects, a single smooth anti-bicanonical curve | definition; the narrowing is a modification of the definition and is kof5's |
| @thm:coble-period-surjectivity | every period in $\bD\sm Z$ is realised by an object of $\mcM_\Co$ | proved, and it uses neither [@Dol96, Thm. 3.1] nor pseudo-ampleness (@rmk:coble-period-surjectivity-sources) |
| @prop:d2a-family-is-pseudo-ample | $e_0$ nef and big | proved; pseudo-ampleness is open there |
| [@Dol96, Prop. 3.3] | $\Gamma_M=\Orth(T_\Co)^*$ | cited |
| @lem:every-object-of-the-functor-is-labellable | a marking of $M$, preserved by $\iota$ | proved, on the $n=1$ class the functor now states |
| @prop:the-coble-locus-in-the-period-domain | $Z$ closed analytic, $\bD\sm Z$ open and connected | proved |
| @thm:coble-period-map-of-the-stack(2) | injectivity on objects, isomorphisms $=$ automorphisms of a member | proved, with @lem:pseudo-ample-injectivity-from-the-chamber supplying the strong Torelli hypothesis from the chamber |
| @thm:coble-period-map-of-the-stack(3) | local Torelli | proved |
| @prop:coble-quotient-presentation | the presentation $\qty[\widetilde\Orth^+(T_\Co)\backslash\bD]$ | proved given (U) and the component computation |
| @prop:coble-monodromy-is-the-marking-group(1)--(3) | the equivalence (its (H1)), the torsor, the tautological system | the equivalence is (H1); the torsor proved, its surjectivity using (H2); the tautological system proved only per loop, its being a local system on the stack being (H3) |
| (A4) the labelled-stack comparison | identifies $\mcM_\Co^{\mathrm{gen}}$ and its local system with the generic labelled stack and the local system of the universal family | assumed, research#797, item 6, not proved; it is the comparison of the presentation with the stack, in group form $\Gamma_\Co=\Gamma_\Co(B)$ on the generic locus |
| Noohi, Def. 18.10, Thm. 18.19, Cor. 18.20 | the Galois correspondence and the exact sequence | cited, verified against the fetched paper |
| @lem:orbifold-monodromy-of-a-quotient | the free quotient: the descended local system and its monodromy group $\varphi(\Gamma)$ | proved, by ordinary covering-space theory in @sec-local-systems-of-a-free-quotient |
| @lem:orbifold-monodromy-of-a-nonfree-quotient | the non-free quotient: per-loop transport, and its descent | clauses 1--2 proved directly; clause 3 assumes the descent (D), research#797, item 4, and is the input (A2)/(H3) and (A3) below |
| @lem:tautological-system-descends | the pullbacks of the equivariant system along maps from spaces are local systems, with the per-loop transport as their monodromy | proved for the strict maps; the $2$-morphisms are @rmk:the-descent-stops-at-the-2-morphisms, research#797, item 4, assumed for the tautological system as (A2)/(H3) and as the full equivariant-system/stack-system equivalence in (A3) |
| @lem:the-special-isotropy-locus-is-proper | the special-isotropy locus is proper closed analytic | proved |
| @prop:the-generic-locus-sees-the-whole-group(1) | $\pi_1(\mcM^{\mathrm{gen}})\to\pi_1(\mcM_\Co)$ onto | proved, given smoothness and connectedness of $\mcM_\Co$ |
| smoothness and connectedness of $\mcM_\Co$ | the hypotheses of the surjectivity | assumed (A1), not proved, and kof5's

*The SGA 1 statement, kept exact.* [SGA 1, Exposé X, Corollaire 3.3] states that for $X$ locally noetherian and normal and $Z\subset X$ closed of codimension at least $2$, the map $\pi_1(X\sm Z)\to\pi_1(X)$ is an **isomorphism**. What is used here is only surjectivity, and under the weaker hypothesis of positive codimension; the proof is the perturbation of a compact loop off a nowhere dense closed analytic subset, and the citation is recorded in that weaker form, not as an isomorphism available at codimension one.

*What remains owed.* The hypotheses (A1)--(A4) are not proved here: smoothness and connectedness of $\mcM_\Co$ is kof5's; (A2) is the input of @prop:coble-monodromy-is-the-marking-group --- (H1) the stack-level Torelli with inertia, (H2) connectedness of the period image, and (H3) the descent of the tautological system along the $2$-morphisms; (A3) is the full equivalence between $G$-equivariant local systems on $U^{\mathrm{gen}}$ and local systems on $[U^{\mathrm{gen}}/G]$, including the $2$-morphism comparisons and cocycle conditions; and (A4) is the comparison of the generic labelled stack and its local system with the generic substack of the universal family, research#797, item 6, in group form $\Gamma_\Co=\Gamma_\Co(B)$ on the generic locus. The two descent hypotheses are research#797, item 4. With (A1)--(A4) the chain above proves the equality. The chamber/ample-class step that @thm:coble-period-map-of-the-stack(2) needs for injectivity is supplied by @lem:pseudo-ample-injectivity-from-the-chamber -- the chamber, not $e_0$, is what enters strong Torelli -- and the surjectivity step is @thm:coble-period-surjectivity, which does not use [@Dol96, Thm. 3.1].
:::

::: {.lemma #lem:pseudo-ample-injectivity-from-the-chamber title="Injectivity for marked pseudo-ample $M$-polarized $\mathrm{K3}$ surfaces, with the chamber in place of the ample class"}
Let $(X,j,\varphi)$ and $(X',j',\varphi')$ be two marked pseudo-ample $M$-polarized $\mathrm{K3}$ surfaces with the same period $\pi$ and the same chamber $\Delta^+_\pi$. Then there is an isomorphism $f\colon X'\iso X$ with $f^*=\varphi^{-1}\circ\varphi'$, and it is unique.
:::

::: {.proof}
Under the markings both $H^2$ are identified with $L$, so the two Hodge structures on $L$ coincide, and $\phi\definedas\varphi^{-1}\circ\varphi'$ is a Hodge isometry. It remains to see that $\phi$ satisfies the hypothesis of the strong Torelli theorem, and this is where the chamber replaces the ample class: an ample class need not exist in $M$, since $e_0=f^*\OO_{\PP^2}(1)$ is nef and not ample (@lem:d2-arrangement-classes(2)), but the Kähler cone does not need one -- it is the chamber of the positive cone of $H^{1,1}(X,\RR)$ cut out by the effective $(-2)$-classes, and the chamber $\Delta^+_\pi$ *is* that choice of signs, by definition of the data $(V^+_\pi,\Delta^+_\pi)$ that [@Dol96, Thm. 3.1] attaches to a period. The chamber is a function of the marked period (@lem:chamber-from-marked-period), so $\phi$, being a Hodge isometry fixing $\pi$, carries $\Delta^+_\pi$ to itself and hence carries the Kähler cone of $X'$ onto that of $X$. A Kähler class $\omega$ of $X'$ is then carried to the Kähler class $\phi(\omega)$ of $X$, and the strong Torelli theorem [@BHPV04, Ch. VIII, Thm. 11.1] in its ample form applies to the pair $(\omega,\phi(\omega))$: it produces an isomorphism $f\colon X'\iso X$ with $f^*=\phi$. So the pseudo-ample hypothesis is no obstruction, the ample class being supplied by the chamber rather than by $e_0$. Uniqueness is the faithfulness of the action on $H^2$.
:::

*What this closes.* @thm:coble-period-map-of-the-stack(2)'s injectivity uses exactly this: two labelled objects with the same period have the same chamber (the marking determines it), so they are isomorphic, and the isomorphisms between them are the automorphisms of either. The chamber/ample-class item of @thm:gamma-co-is-the-stack-monodromy's ledger is therefore supplied by @lem:pseudo-ample-injectivity-from-the-chamber, and is no longer owed.

::: {.remark #rmk:the-huybrechts-model title="The marked-$\mathrm{K3}$ model of Huybrechts, *Lectures on K3 Surfaces*, Ch. 7, and the Coble problem as its $\iota$-anti-invariant part"}
The Coble computation can be modelled on the unpolarized marked problem, and every step of @thm:gamma-co-is-the-stack-monodromy has a counterpart there.

| step | the Coble route on this page | the marked-$\mathrm{K3}$ model, by number |
|---|---|---|
| objects | labelled Coble covers with a marking of $M$ (§@lem:every-object-of-the-functor-is-labellable) | pairs $(X,\varphi)$, $\varphi\colon H^2(X,\ZZ)\iso\Lambda$ a marking: Huybrechts, *Lectures on K3 Surfaces*, §3.3 |
| the space | a stack with infinite isotropy ($\Aut(S)\neq1$) | the moduli space $N$ of marked $\mathrm{K3}$ surfaces, a fine $20$-dimensional complex manifold, not Hausdorff: Huybrechts, *Lectures on K3 Surfaces*, §3.3 |
| the period map | $\mathfrak p\colon\mcM^{\mathrm{lab}}_\Co\to\qty[\widetilde\Orth^+(T_\Co)\backslash\bD]$ | the global period map of the universal family over $N$: Huybrechts, *Lectures on K3 Surfaces*, §3.3 |
| injectivity | @lem:pseudo-ample-injectivity-from-the-chamber | Huybrechts, *Lectures on K3 Surfaces*, Thm. 3.4, the global Torelli theorem, the period map of marked polarized $\mathrm{K3}$ surfaces being an open embedding; and Huybrechts, *Lectures on K3 Surfaces*, §7.5.2 for the lifting of a Hodge isometry carrying a polarization to a polarization |
| local Torelli | @thm:coble-period-map-of-the-stack(3) | local Torelli, used to glue the deformation spaces into $N$: Huybrechts, *Lectures on K3 Surfaces*, §3.3 |
| existence | [@Dol96, Thm. 3.1] | Huybrechts, *Lectures on K3 Surfaces*, Thm. 3.1, surjectivity of the period map |
| monodromy | the torsor plus Noohi's Theorem 18.19 | the monodromy group is $\operatorname{Im}\rho$ for $\rho\colon\pi_1(S,t)\to\Orth(H^2(X_t,\QQ))$: Huybrechts, *Lectures on K3 Surfaces*, §4.3, with the discussion of Huybrechts, *Lectures on K3 Surfaces*, §7.5.3 |

*What the model gives, and the one place the analogy is not an identity.* In the unpolarized marked problem the monodromy group is $\widetilde\Orth^+(\Lambda_{\mathrm{K3}})=\Orth^+(\Lambda_{\mathrm{K3}})$, and the two agree because $\Lambda_{\mathrm{K3}}$ is unimodular, so the discriminant kernel is everything. Here $T_\Co$ is not unimodular: its discriminant group is $(\ZZ/2)^{11}$ (@prop:coble-discriminant-group), so the group that the same argument produces is the *discriminant kernel* $\widetilde\Orth^+(T_\Co)=\Orth^+(T_\Co)\intersect\ker\bar\rho$, not $\Orth^+(T_\Co)$. That is the precise sense in which $\Gamma_\Co$ is the anti-invariant analogue: it is the monodromy of the $\iota$-anti-invariant part $T_\Co$, and the discriminant condition is forced by the gluing $T_\En=(\T_\Co\perp\ZZ\delta)_H$, whose overlattice exacts the kernel. The model thus supplies nothing new for the steps already proved here, and it confirms the shape: the same period-map-and-torsor argument, run on the anti-invariant lattice rather than on all of $H^2$.
:::

### Item 6: the groups from the universal families

::: {.proposition #prop:gamma-co-from-the-universal-family title="What the universal families give, and what a restriction gives instead"}
1. $\Gamma_\Co$ is the monodromy of the VHS on the universal family over the moduli stack $\mcM_\Co$ (@def:gamma-co-groups(1)). For a parameter space $B'$ carrying the pulled-back family with a map $B'\to\mcM_\Co$, the monodromy of the pulled-back system is the image of $\pi_1(B')$ under the composite (@lem:coble-family-base-change), and it is $\Gamma_\Co$ exactly when that map sees all of $\pi_1(\mcM_\Co)$; the labelled base $B$ of @def:coble-family-unpolarized gives the group $\Gamma_\Co(B)=\rho\qty{\pi_1(B,s)}$ computed in this book, and whether it sees all of $\pi_1(\mcM_\Co)$, equivalently whether $\Gamma_\Co=\Gamma_\Co(B)$, is research#797, item 6.
2. *A restriction from the Enriques side gives a stabiliser, not $\Gamma_\Co$.* The Coble locus is the image of the $(-2)$-Heegner divisor of the Enriques period domain (@prop:torelli-for-the-coble-lattice(3)), and $T_\Co=\delta^{\perp T_\En}$ is cut out of $T_\En$ (@prop:gamma-co-images). The monodromy of the restricted family is the image of $\Stab_{\Gamma_\En}(\delta)$, which is $\widetilde\Orth^+(T_\Co)$ on the Enriques side (@prop:gamma-co-images(1)--(3)); it is *not* thereby $\Gamma_\Co$, because a loop of the Coble base does not give an element of that stabilizer without knowing that the Coble base is the divisor modulo it, which is the step recorded as failing in @rmk:d2-routes-for-the-equality(3).
3. $\Gamma_{\Co,2}$ is defined in the same way from the degree-$2$ family of @def:coble-family-degree-two (@def:gamma-co-groups(5)); what it is not is the restricted Enriques stabilizer $\bar\rho^{-1}(P)$, which is a different group (@thm:coble-monodromy-versus-enriques(3)), and the two do not agree (@prop:coble-monodromy-equality-false). So item 6 gives both groups as monodromy groups of universal families, and identifies neither with a lattice group by restriction: for $\Gamma_\Co$ that identification is research#780, and for $\Gamma_{\Co,2}$ the question is answered in the negative by @prop:coble-monodromy-equality-false.
:::

::: {.proof}
1. is @def:gamma-co-groups(1) with @lem:coble-family-base-change, which computes the monodromy of a pullback as the image of the subgroup of $\pi_1$; the comparison with $B$ is @lem:d2-labelled-base-monodromy. 2. is @prop:gamma-co-images for the lattice and the stabilizer, with @rmk:d2-routes-for-the-equality(3) for the step that fails. 3. is the definition and the two numbered statements named.
:::

*What that does and does not give.* For a free quotient, ordinary covering-space theory gives item 4 outright: @lem:orbifold-monodromy-of-a-quotient states the descended local system and its monodromy group, and @cor:monodromy-of-the-tautological-descent is the faithful case. For the non-free quotient stacks of item 3, the per-loop transport is @lem:orbifold-monodromy-of-a-nonfree-quotient(1)--(2), and item 4 holds only under the descent (D) of that lemma, which is research#797, item 4: under (D), a point of $\bD(T_\Co)$ with nontrivial stabilizer contributes an orbifold point and the descended tautological local system still has monodromy image $\Gamma$. Without (D) the statement of item 4 is not asserted; what remains is the per-loop transport. It does *not* identify the local system of the VHS on the universal family over $\mcM_\Co$ with that tautological system: the universal family over the stack is research#797, item 1, and the comparison of its local system with the tautological one is item 6. For an arbitrary local system on an arbitrary stack the general statement above is the first isomorphism theorem and needs no more; what the Galois correspondence adds is the covering stack. That correspondence exists as a numbered statement for topological stacks: $\pi_1$ of a pointed topological stack is Noohi, *Foundations of topological stacks I* (arXiv:math/0503247), Definition 17.5; a covering of stacks is Definition 18.10 there; the functor from coverings of a pointed connected locally path connected and semilocally $1$-connected stack to $\pi_1$-sets is an equivalence by Theorem 18.19, which is the Galois correspondence; and the bijection between subgroups of $\pi_1$ and pointed connected coverings, with the existence of a universal cover, is Corollary 18.20. (The paper carries no key in this book's bibliography; it is cited in words, as is the other source without a key.) The exact sequence of this section is a corollary of Theorem 18.19 and is not stated there. For the quotient stack of item 3, under the same descent (D), the kernel is trivial: $K_\bT=\pi_1\qty(\bD(T_\Co)^+)$, and $\bD(T_\Co)^+$ is a bounded symmetric domain, hence contractible, so the monodromy representation is an isomorphism $\pi_1(F_S)\iso\widetilde\Orth^+(T_\Co)$.
