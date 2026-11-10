# Local systems of lattices and monodromy {#sec-local-systems-of-lattices}

Throughout this chapter $B$ is an arcwise connected, locally simply connected topological space, and a *local system* on $B$ is a sheaf of abelian groups that is locally isomorphic to a constant sheaf [@Voi07a, Definition 9.8].
For a local system $\bL$ and a path $\gamma\colon[0,1]\to B$, the sheaf $\gamma^{-1}\bL$ is constant [@Voi07, Lemma 3.6], so both restriction maps
$$
\bL_{\gamma(0)}
\xleftarrow{\ \sim\ }
\Gamma\qty{[0,1],\gamma^{-1}\bL}
\xrightarrow{\ \sim\ }
\bL_{\gamma(1)}
$$
are isomorphisms.
Their composite
$$
\gamma^*\colon\bL_{\gamma(0)}\iso\bL_{\gamma(1)}
$$
is the *transport along $\gamma$*; it depends only on the homotopy class of $\gamma$ relative to its endpoints [@Voi07, proof of Proposition 3.9].
For $s\in B$, transport along loops based at $s$ is the *monodromy representation*
$$
\rho\colon\pi_1(B,s)\too\Aut(\bL_s)
$$
of $\bL$ [@Voi07, Corollary 3.10, Definition 3.13].

## Local systems of lattices {#sec-local-systems-of-lattices-definition}

::: {.definition #def:local-system-of-lattices title="Local system of lattices"}

A *local system of lattices* on $B$ is a pair $(\bL,\beta)$ in which $\bL$ is a local system on $B$ whose stalks are free abelian groups of finite rank and
$$
\beta\colon\bL\tensor_{\underline{\ZZ}_B}\bL\too\underline{\ZZ}_B
$$
is a morphism of sheaves of abelian groups.
Each stalk $(\bL_b,\beta_b)$ is a $\ZZ$-lattice in the sense of @def:lattice.
A *morphism* $(\bL,\beta)\to(\bL',\beta')$ is a morphism of sheaves $\phi\colon\bL\to\bL'$ with $\beta'\circ(\phi\tensor\phi)=\beta$.
:::

::: {.proposition #prop:local-system-of-lattices-monodromy title="Transport is an isometry"}

Let $(\bL,\beta)$ be a local system of lattices on $B$ and let $s\in B$.

1. For every path $\gamma$ in $B$, the transport $\gamma^*\colon\bL_{\gamma(0)}\to\bL_{\gamma(1)}$ is an isometry for $\beta_{\gamma(0)}$ and $\beta_{\gamma(1)}$.
   All stalks of $(\bL,\beta)$ are therefore isometric, and the monodromy representation is a group morphism
$$
\rho\colon\pi_1(B,s)\too\Aut(\bL_s,\beta_s).
$$
2. Let $(L,\beta_L)$ be a $\ZZ$-lattice whose underlying module is free.
   Every group morphism $\rho\colon\pi_1(B,s)\to\Aut(L,\beta_L)$ is the monodromy representation of a local system of lattices on $B$ whose stalk at $s$ is isometric to $(L,\beta_L)$.
:::

::: {.proof}

For (1), let $x,y\in\Gamma\qty{[0,1],\gamma^{-1}\bL}$.
The pullback $\gamma^{-1}\beta$ is a morphism of sheaves $\gamma^{-1}\bL\tensor\gamma^{-1}\bL\to\underline{\ZZ}_{[0,1]}$, so $(\gamma^{-1}\beta)(x\tensor y)$ is a section of $\underline{\ZZ}_{[0,1]}$: a locally constant function $[0,1]\to\ZZ$ whose value at $u$ is $\beta_{\gamma(u)}(x_u,y_u)$.
The interval is connected, so the values at $u=0$ and $u=1$ are equal:
$$
\beta_{\gamma(0)}(x_0,y_0)=\beta_{\gamma(1)}(x_1,y_1)=\beta_{\gamma(1)}(\gamma^*x_0,\gamma^*y_0).
$$

For (2), let $\pi\colon\widetilde B\to B$ be the universal cover.
The local system with monodromy $\rho$ has sections
$$
\Gamma(U,\bL)=\theset{\sigma\colon\pi^{-1}(U)\to L\text{ locally constant}\st\sigma(\gamma u)=\rho(\gamma)\sigma(u)}
$$
over an open set $U$ [@Voi07, proof of Corollary 3.10, (3.1)].
For two such sections, the function $u\mapsto\beta_L(\sigma(u),\tau(u))$ on $\pi^{-1}(U)$ is locally constant, and it is invariant under $\pi_1(B,s)$ because each $\rho(\gamma)$ is an isometry.
It is therefore the pullback of a unique locally constant function $U\to\ZZ$, and this defines $\beta$.
:::

Symmetry, the alternating property and nondegeneracy of $\beta_b$ (@def:form-axioms), and the signature of a nondegenerate symmetric $\beta_b$ (@def:signature), are therefore independent of $b$.
When the stalks are symmetric, $\Aut(\bL_s,\beta_s)$ is the orthogonal group $\Orth(\bL_s)$ of @sec-isometry-groups; when they are alternating and nondegenerate, it is the symplectic group $\Sp(\bL_s)$.

::: {.example #ex:sublocal-system-of-constant-sheaf title="A local system inside a constant sheaf is constant"}

Let $M$ be a $\ZZ$-lattice, and let $(\bL,\beta)$ be a local system of lattices with $\bL\iscontainedin\underline M_B$ a subsheaf and $\beta$ the restriction of $\beta_M$.
For a loop $\gamma$ at $s$, the sheaf $\gamma^{-1}\bL$ is a subsheaf of $\underline M_{[0,1]}$, whose sections over $[0,1]$ are the constant functions.
Hence $\gamma^*=\id_{\bL_s}$, the monodromy representation is trivial, and $\bL$ is the constant sheaf $\underline{(\bL_s)}_B$ [@Voi07, Corollary 3.10].
:::

## The orientation sheaf {#sec-orientation-sheaf}

In this section $(\bL,\beta)$ is a local system of lattices on $B$ whose stalks are symmetric and nondegenerate, and $\sigma_+,\sigma_-$ are the orientation characters of @def:orientation-characters for the real quadratic space $\bL_s\tensor\RR$.

::: {.definition #def:orientation-sheaf title="Orientation sheaf of a local system of lattices"}

For $b\in B$, let $\operatorname{Or}^+_b$ be the two-element set of orientation classes of maximal positive-definite subspaces of $\bL_b\tensor\RR$.
By @prop:local-system-of-lattices-monodromy, the transport along a path $\gamma$ induces a bijection $\gamma^*\colon\operatorname{Or}^+_{\gamma(0)}\to\operatorname{Or}^+_{\gamma(1)}$.
The *positive orientation sheaf* $\operatorname{Or}^+_{\bL}$ is the sheaf of sets on $B$ with
$$
\Gamma\qty{U,\operatorname{Or}^+_{\bL}}
\definedas
\theset{(o_b)_{b\in U}\st o_b\in\operatorname{Or}^+_b,\ \gamma^*o_{\gamma(0)}=o_{\gamma(1)}\text{ for every path }\gamma\text{ in }U}.
$$
The *negative orientation sheaf* $\operatorname{Or}^-_{\bL}$ is the positive orientation sheaf of $(\bL,-\beta)$.
:::

::: {.proposition #prop:orientation-sheaf-section title="Monodromy lies in $\ker\sigma_+$ exactly when the orientation sheaf has a global section"}

The following are equivalent.

1. $\rho\qty{\pi_1(B,s)}\iscontainedin\ker\sigma_+$.
2. The sheaf $\operatorname{Or}^+_{\bL}$ has a global section.

When they hold, $\operatorname{Or}^+_{\bL}$ has exactly two global sections.
The same statements hold for $\sigma_-$ and $\operatorname{Or}^-_{\bL}$.
:::

::: {.proof}

Since $B$ is arcwise connected, a global section $(o_b)$ is determined by $o_s$, through $o_b=\gamma^*o_s$ for any path $\gamma$ from $s$ to $b$.
A class $o_s\in\operatorname{Or}^+_s$ extends to a global section exactly when $\gamma^*o_s$ depends only on the endpoint of $\gamma$, that is, when every loop $\gamma$ at $s$ has $\gamma^*o_s=o_s$.
The transport along a loop of class $\gamma$ is $\rho(\gamma)$, and $\rho(\gamma)$ fixes $o_s$ exactly when $\sigma_+(\rho(\gamma))=+1$.
The condition does not depend on which of the two classes $o_s$ is chosen.
:::

If $\bL_s$ is indefinite, condition (1) says that the monodromy group lies in $\Orth^+(\bL_s)$ (@prop:orientation-characters-reflections).

::: {.example #ex:monodromy-outside-orth-plus title="A local system of lattices with no orientation section"}

Let $B=\CC^\times$, so that $\pi_1(B,1)\cong\ZZ$, and let $U$ be the hyperbolic plane.
By @prop:local-system-of-lattices-monodromy there is a local system of lattices on $B$ with stalk $U$ whose monodromy representation sends a generator to $-\id_U$.
The signature of $U$ is $(1,1)$, so $\sigma_+(-\id_U)=\spinornorm_\RR(-\id_U)=-1$ by @lem:minus-identity-spinor-norm.
The monodromy group is not contained in $\Orth^+(U)$, and neither orientation sheaf has a global section.
:::

## Polarized variations of Hodge structure {#sec-polarized-vhs}

::: {.definition #def:polarized-integral-vhs title="Polarized integral variation of Hodge structure"}

Let $k$ be an integer and let $(L,Q)$ be a $\ZZ$-lattice with $L$ free and $Q$ nondegenerate, symmetric if $k$ is even and alternating if $k$ is odd.
A *Hodge structure of weight $k$ on $L$ polarized by $Q$* is a decreasing filtration $F^\bullet$ of $L_\CC$ by complex subspaces such that the subspaces
$$
H^{p,q}\definedas F^p\cap\overline{F^q},\qquad p+q=k,
$$
satisfy $L_\CC=\bigoplus_{p+q=k}H^{p,q}$ and
$$
Q\qty{H^{p,q},H^{r,s}}=0\ \text{ unless }(r,s)=(q,p),
\qquad
(-1)^{\frac{k(k-1)}2}\,i^{p-q}\,Q(v,\bar v)>0\ \text{ for }0\neq v\in H^{p,q}
$$
[@Voi07a, Definition 7.7 and §10.1.3].
Its *Hodge numbers* are $h^{p,q}\definedas\dim_\CC H^{p,q}$.

Let $B$ be a connected complex manifold.
A *polarized integral variation of Hodge structure of weight $k$* on $B$ is a triple $(\bL,Q,F^\bullet)$ in which $(\bL,Q)$ is a local system of lattices on $B$ and $F^\bullet$ is a decreasing filtration of the holomorphic vector bundle $\bL\tensor_\ZZ\OO_B$ by holomorphic subbundles, such that

1. for every $b\in B$, the fibre $F^\bullet_b$ is a Hodge structure of weight $k$ on $\bL_b$ polarized by $Q_b$;
2. $\nabla F^p\iscontainedin F^{p-1}\tensor\Omega^1_B$ for every $p$, where $\nabla$ is the flat connection on $\bL\tensor_\ZZ\OO_B$ with $\ker\nabla=\bL\tensor_\ZZ\underline{\CC}_B$

[@Sch73, §2].
The polarization form of [@Sch73, (2.10)] is $S=(-1)^{k(k-1)/2}Q$.
:::

::: {.lemma #lem:hodge-real-pieces title="Signs of the polarization on the real Hodge pieces"}

Let $F^\bullet$ be a Hodge structure of even weight $k=2m$ on $L$ polarized by $Q$, and put $\epsilon\definedas(-1)^{m+1}$.
For $0\le j\le m$ define the real subspaces
$$
R_j\definedas\qty{H^{m+j,m-j}\oplus H^{m-j,m+j}}\cap L_\RR
$$
of $L_\RR$, so that $R_0=H^{m,m}\cap L_\RR$.

1. $L_\RR=\bigoplus_{j=0}^mR_j$, the summands are pairwise orthogonal for $Q$, and $(-1)^{m+j}Q$ is positive definite on $R_j$.
2. The subspace
$$
W^{\mathrm{odd}}_F\definedas\bigoplus_{j\text{ odd}}R_j
$$
is a maximal $\epsilon$-definite subspace of $(L_\RR,Q)$, and
$$
W^{\mathrm{ev}}_F\definedas\bigoplus_{j\text{ even}}R_j
$$
is a maximal $(-\epsilon)$-definite subspace.
3. For $j>0$, the map $R_j\to H^{m+j,m-j}$ sending $x$ to its component in $H^{m+j,m-j}$ is an isomorphism of real vector spaces.
:::

::: {.proof}

Complex conjugation exchanges $H^{p,q}$ and $H^{q,p}$, so the components $x^{p,q}$ of a real vector $x$ satisfy $\overline{x^{p,q}}=x^{q,p}$.
This gives the decomposition in (1) and the isomorphism in (3), whose inverse is $v\mapsto v+\bar v$.
Orthogonality holds because $Q$ pairs $H^{p,q}$ nontrivially only with $H^{q,p}$.
For $j>0$ and $x=v+\bar v$ with $v\in H^{m+j,m-j}$, one has $Q(v,v)=Q(\bar v,\bar v)=0$, so
$$
Q(x,x)=2Q(v,\bar v),
\qquad
(-1)^{\frac{k(k-1)}2}\,i^{2j}=(-1)^{m+j},
$$
and the positivity condition of @def:polarized-integral-vhs gives $(-1)^{m+j}Q(x,x)>0$ for $x\neq0$.
For $j=0$ the same condition applied to $v=x\in R_0$ gives $(-1)^mQ(x,x)>0$.
Statement (2) follows: $L_\RR=W^{\mathrm{odd}}_F\perp W^{\mathrm{ev}}_F$ with $Q$ definite of sign $\epsilon$ on the first summand and of sign $-\epsilon$ on the second, so their dimensions are the two indices of the signature of $Q$ (@thm:sylvester).
:::

## Period domains and their components {#sec-period-domain-components}

Fix $k$, a $\ZZ$-lattice $(L,Q)$ as in @def:polarized-integral-vhs, and Hodge numbers $h^{p,q}$.
The *period domain* $D$ is the set of Hodge structures of weight $k$ on $L$ polarized by $Q$ with these Hodge numbers; it is a complex manifold [@Sch73, §3].
Put
$$
G_\RR\definedas\Aut(L_\RR,Q),
\qquad
G_\ZZ\definedas\Aut(L,Q)\iscontainedin G_\RR.
$$
The group $G_\RR$ acts transitively on $D$, the stabilizer $V_F\iscontainedin G_\RR$ of a point $F\in D$ is compact, and $G_\ZZ$ is discrete in $G_\RR$ [@Sch73, §3, (3.7), (3.8)].
Every $g\in V_F$ preserves each $H^{p,q}$ of $F$ [@Sch73, §3].

::: {.theorem #thm:period-domain-component-stabilizer title="The stabilizer of a component of an even-weight period domain"}

Let $k=2m$, let $\epsilon=(-1)^{m+1}$, and let $D^+$ be a connected component of $D$.

1. If $h^{m,m}>0$, then
$$
\Stab_{G_\RR}(D^+)=\ker\sigma_\epsilon.
$$
2. If $h^{m,m}=0$, then
$$
\Stab_{G_\RR}(D^+)=\ker\sigma_+\cap\ker\sigma_-=G_\RR^\circ.
$$
:::

::: {.proof}

The subspaces $H^{p,q}_F$ have constant dimension, so they depend continuously on $F\in D$, and so do $W^{\mathrm{odd}}_F$ and $W^{\mathrm{ev}}_F$.
By @lem:hodge-real-pieces (3), $W^{\mathrm{odd}}_F$ is isomorphic to the complex vector space $\bigoplus_{j\text{ odd}}H^{m+j,m-j}_F$; let $o^{\mathrm{odd}}_F$ be the resulting complex orientation.
By @lem:hodge-real-pieces (2), the pair $\qty{W^{\mathrm{odd}}_F,o^{\mathrm{odd}}_F}$ is a point of the space $\widetilde\Gr^+$ of @lem:positive-grassmannian for the quadratic space $(L_\RR,\epsilon Q)$, and
$$
\Psi\colon D\too\widetilde\Gr^+(L_\RR,\epsilon Q),
\qquad
F\longmapsto\qty{W^{\mathrm{odd}}_F,o^{\mathrm{odd}}_F}
$$
is continuous.
It is $G_\RR$-equivariant, because $g\in G_\RR$ maps $H^{p,q}_F$ complex-linearly onto $H^{p,q}_{gF}$.

Let $g\in\Stab_{G_\RR}(D^+)$.
The connected set $\Psi(D^+)$ lies in one orientation class, and $g$ maps $\Psi(D^+)$ to itself, so $g$ fixes that class: $\sigma_\epsilon(g)=+1$.
If $h^{m,m}=0$, then $W^{\mathrm{ev}}_F=\bigoplus_{j>0\text{ even}}R_j$ carries a complex orientation in the same way, and the same argument for $(L_\RR,-\epsilon Q)$ gives $\sigma_{-\epsilon}(g)=+1$.
This proves the inclusions $\iscontainedin$.

For the reverse inclusions, fix $F\in D^+$.
The connected group $G_\RR^\circ$ maps $D^+$ to itself, and $V_F$ fixes the point $F$ and permutes the components of $D$, so
$$
G_\RR^\circ\cdot V_F\iscontainedin\Stab_{G_\RR}(D^+).
$$
By @lem:orientation-characters-identity-component, $\ker\sigma_+\cap\ker\sigma_-=G_\RR^\circ$, which proves (2).
For (1), let $g\in\ker\sigma_\epsilon$.
If $\sigma_{-\epsilon}(g)=+1$, then $g\in G_\RR^\circ$.
Otherwise choose $0\neq w\in R_0$.
By @lem:hodge-real-pieces, $Q(w,w)$ has sign $-\epsilon$ and $w$ is orthogonal to $H^{p,q}_F$ for $(p,q)\neq(m,m)$.
The reflection $s_w$ therefore fixes those subspaces pointwise and preserves $H^{m,m}_F$, so $s_w\in V_F$.
By @prop:orientation-characters-reflections, $\sigma_{-\epsilon}(s_w)=-1$ and $\sigma_\epsilon(s_w)=+1$.
Hence $gs_w\in\ker\sigma_+\cap\ker\sigma_-=G_\RR^\circ$, and $g\in G_\RR^\circ\cdot V_F$.
:::

Let $(\bL,Q,F^\bullet)$ be a polarized integral variation of Hodge structure of weight $k$ on a connected complex manifold $B$, let $s\in B$, and let $D$ be the period domain of $(\bL_s,Q_s)$ for the Hodge numbers of $F^\bullet_s$.
Let $\pi\colon\widetilde B\to B$ be the universal cover.
The pullback $\pi^{-1}\bL$ is constant with stalk $\bL_s$, and the pullback of $F^\bullet$ is a map
$$
\widetilde\Phi\colon\widetilde B\too D
$$
that satisfies
$$
\widetilde\Phi(\gamma\tilde t)=\rho(\gamma)\,\widetilde\Phi(\tilde t)
\qquad\text{for }\tilde t\in\widetilde B,\ \gamma\in\pi_1(B,s)
$$ {#eq-period-map-equivariance}
[@Sch73, (3.24)].
It is holomorphic [@Sch73, Theorem 3.27].

::: {.corollary #cor:vhs-monodromy-stabilizes-component title="Monodromy stabilizes the component of the period domain"}

Put $L\definedas\bL_s$, and let $D^+$ be the connected component of $D$ that contains $F^\bullet_s$.
Then
$$
\rho\qty{\pi_1(B,s)}\iscontainedin\Stab_{G_\ZZ}(D^+).
$$
The subgroup $\Stab_{G_\ZZ}(D^+)$ of $G_\ZZ$ is the following.

| weight | Hodge numbers | $\Stab_{G_\ZZ}(D^+)$ |
| --- | --- | --- |
| $k=2m$ | $h^{m,m}>0$ | $\Orth(L)\cap\ker\sigma_\epsilon$, with $\epsilon=(-1)^{m+1}$ |
| $k=2m$ | $h^{m,m}=0$ | $\Orth(L)\cap\ker\sigma_+\cap\ker\sigma_-$ |

For $k$ odd the form $Q$ is alternating and the monodromy group lies in $G_\ZZ=\Sp(L)$.
If $m$ is odd, $h^{m,m}>0$ and $L$ is indefinite, then $\Stab_{G_\ZZ}(D^+)=\Orth^+(L)$.
:::

::: {.proof}

The image $\widetilde\Phi(\widetilde B)$ is connected and contains $F^\bullet_s$, so it lies in $D^+$.
For $\gamma\in\pi_1(B,s)$, @eq-period-map-equivariance shows that $\rho(\gamma)$ maps a point of $D^+$ to a point of $D^+$.
The homeomorphism $\rho(\gamma)$ of $D$ permutes the components, so $\rho(\gamma)D^+=D^+$.
The table is @thm:period-domain-component-stabilizer, and the last statement is @prop:orientation-characters-reflections (4).
:::

For weight $2$ the sign is $\epsilon=+1$, and $W^{\mathrm{odd}}_F=\qty{H^{2,0}\oplus H^{0,2}}\cap L_\RR$ is the positive-definite real plane spanned by the real and imaginary parts of the vectors of $H^{2,0}$.
The primitive local system of a family of polarized K3 surfaces has $h^{1,1}>0$, and the first row of the table is @prop:polarized-k3-monodromy-positive.

::: {.example #ex:weight-zero-vhs title="The character $\sigma_{-\epsilon}$ is not constrained when $h^{m,m}>0$"}

Let $B=\CC^\times$ and let $(\bL,Q)$ be the local system of lattices on $B$ with stalk $(\ZZ,xy)$ whose monodromy representation sends a generator of $\pi_1(B,1)$ to $-1$ (@prop:local-system-of-lattices-monodromy).
With $F^0=\bL\tensor\OO_B$ and $F^1=0$, the triple $(\bL,Q,F^\bullet)$ is a polarized integral variation of Hodge structure of weight $0$ with $h^{0,0}=1$.
Here $m=0$ and $\epsilon=-1$.
The monodromy $-1$ is the reflection in a vector of positive square, so $\sigma_+(-1)=-1$ and $\sigma_-(-1)=+1$ (@prop:orientation-characters-reflections).
:::

## Cohomology of families {#sec-cohomology-of-families-monodromy}

Let $f\colon\mcx\to B$ be a proper holomorphic submersion of complex manifolds with $B$ connected and with fibres $X_b$ of dimension $n$, and let $\omega\in H^2(\mcx,\ZZ)$ be a class whose restriction to every fibre is a Kähler class.
For $k\le n$ put
$$
\bV^k\definedas R^kf_*\underline{\ZZ}_{\mcx}/\text{torsion},
\qquad
\bV^k_{\mathrm{prim}}\definedas\ker\qty{L^{n-k+1}\colon\bV^k\too\bV^{2n-k+2}},
$$
where $L$ is the cup product with $\omega$, and
$$
Q(\alpha,\beta)\definedas\int_{X_b}\omega^{n-k}\cupprod\alpha\cupprod\beta
\qquad\text{for }\alpha,\beta\in\bV^k_b.
$$

::: {.proposition #prop:primitive-cohomology-vhs title="Primitive cohomology of a polarized family"}

1. $(\bV^k,Q)$ is a local system of lattices on $B$, and $L$ is a morphism of local systems.
2. $\qty{\bV^k_{\mathrm{prim}},Q}$ with the Hodge filtration of the fibres is a polarized integral variation of Hodge structure of weight $k$.
:::

::: {.proof}

The local system $R^kf_*\underline\ZZ$ carries the cup product, and the monodromy representation is compatible with it [@Voi07, §3.1.2]; the class $\omega|_{X_b}$ is locally constant, so $L$ and $Q$ are compatible with the local identifications of the stalks [@Voi07a, §10.1.3].
The Lefschetz decomposition of each fibre is a decomposition of Hodge structures, and on the primitive part the Hodge filtration satisfies the orthogonality and positivity conditions of @def:polarized-integral-vhs [@Voi07a, Theorem 6.32, §10.1.3].
The Hodge filtration is a filtration by holomorphic subbundles that satisfies condition (2) of @def:polarized-integral-vhs [@Sch73, §2].
:::

::: {.corollary #cor:middle-cohomology-monodromy title="Monodromy of even-dimensional middle cohomology"}

Let $n=2m$, so that $Q$ is the intersection form on $\bV^n$, and let $\rho$ be the monodromy representation of $\bV^n$ at $s\in B$.

1. The restriction of $\rho$ to $\bV^n_{\mathrm{prim},s}$ takes values in $\ker\sigma_\epsilon$ with $\epsilon=(-1)^{m+1}$, and in $\ker\sigma_+\cap\ker\sigma_-$ if $h^{m,m}_{\mathrm{prim}}=0$.
2. If $n=2$, then $\rho$ takes values in $\ker\sigma_+\iscontainedin\Orth\qty{H^2(X_s,\ZZ)/\text{torsion}}$.
:::

::: {.proof}

Statement (1) is @cor:vhs-monodromy-stabilizes-component for the variation of @prop:primitive-cohomology-vhs.

For (2), put $h\definedas\omega|_{X_s}$.
Then $Q(h,h)=\int_{X_s}\omega^2>0$, the class $h$ is fixed by $\rho$, and $\bV^2_{\mathrm{prim},s}=h^\perp$.
Each $\rho(\gamma)$ is therefore $\id_{\RR h}\oplus g$ on $\RR h\perp\qty{h^\perp}_\RR$, with $g$ the monodromy of the primitive part.
By (1) with $m=1$, $\sigma_+(g)=+1$, and @prop:orientation-characters-reflections (3) gives $\sigma_+(\rho(\gamma))=+1$.
:::

For the K3 lattice, $\sigma_+$ is the character $\sigma_{\lkt}$ of @def:k3-positive-cone-orientation: both are group morphisms $\Orth(\lkt_\RR)\to\theset{\pm1}$ that take the value $-1$ on the reflections in vectors of positive square and $+1$ on the reflections in vectors of negative square.
@prop:k3-monodromy-positive is the statement of @cor:middle-cohomology-monodromy (2) for families of K3 surfaces without a class $\omega$.

::: {.example #ex:picard-lefschetz-orientation title="Picard--Lefschetz reflections"}

Let $f\colon X\to\Delta$ be a Lefschetz degeneration with $X$ smooth of dimension $2m+1$, let $t\in\Delta^*$, and let $T$ be the monodromy of the positive generator of $\pi_1(\Delta^*,t)$ on $H^{2m}(X_t,\ZZ)$ with its intersection form $\langle\ ,\ \rangle$.
Let $\delta$ be the class of a vanishing sphere.
The Picard--Lefschetz formula is
$$
T(\alpha)=\alpha+\epsilon_{2m+1}\langle\alpha,\delta\rangle\delta,
\qquad
\epsilon_{2m+1}=-(-1)^m,
\qquad
\langle\delta,\delta\rangle=2(-1)^m
$$
[@Voi07, Theorem 3.16, Remark 3.18, Remark 3.21].
Hence $T$ is the reflection $s_\delta$, and by @prop:orientation-characters-reflections
$$
\sigma_+(T)=(-1)^{m+1},
\qquad
\sigma_-(T)=(-1)^m.
$$
With $\epsilon=(-1)^{m+1}$ this reads $\sigma_\epsilon(T)=+1$ and $\sigma_{-\epsilon}(T)=-1$.
For $m$ even, $T$ does not lie in $\ker\sigma_+$: the statement of @cor:middle-cohomology-monodromy (2) does not extend to middle cohomology of fibres of dimension $4$.

A generic pencil of hyperplane sections of a smooth projective variety $Y\iscontainedin\PP^N$ of dimension $2m+1$ is a Lefschetz pencil [@Voi07, Corollary 2.10], and near each of its critical values it is a Lefschetz degeneration whose vanishing class is primitive [@Voi07, Corollary 2.25, Lemma 2.26].
Such a $T$ is therefore a monodromy operator of the variation $\bV^{2m}_{\mathrm{prim}}$ of @prop:primitive-cohomology-vhs over the set of regular values of the pencil.
:::

## Monodromy and automorphisms of Hodge structures {#sec-monodromy-hodge-automorphisms}

Let $(\bL,Q,F^\bullet)$, $s$, $D$ and $\widetilde\Phi$ be as in @sec-period-domain-components.
For $F\in D$, an *automorphism of the polarized Hodge structure* $F$ is an element $g\in G_\ZZ$ with $gF^p=F^p$ for all $p$; these form the group $G_\ZZ\cap V_F$.
For a K3 surface these are the Hodge isometries of @sec-k3-automorphisms.

::: {.proposition #prop:monodromy-hodge-automorphism title="When a monodromy operator is an automorphism of the Hodge structure"}

1. For every $F\in D$, the group $G_\ZZ\cap V_F$ is finite.
2. For $\gamma\in\pi_1(B,s)$ and $\tilde t\in\widetilde B$, the isometry $\rho(\gamma)$ is an automorphism of the polarized Hodge structure $\widetilde\Phi(\tilde t)$ exactly when
$$
\widetilde\Phi(\gamma\tilde t)=\widetilde\Phi(\tilde t).
$$
3. If $\rho(\gamma)$ has infinite order, then it is not an automorphism of $\widetilde\Phi(\tilde t)$ for any $\tilde t\in\widetilde B$.
:::

::: {.proof}

The group $G_\ZZ\cap V_F$ is a discrete subgroup of the compact group $V_F$, so it is finite.
Statement (2) is @eq-period-map-equivariance, and (3) follows from (1) and (2).
:::

::: {.example #ex:picard-lefschetz-not-hodge title="Picard--Lefschetz operators"}

Let $f\colon X\to\Delta$ be a Lefschetz degeneration with fibres of odd dimension whose vanishing class $\delta$ is not torsion.
Then $T$ has infinite order [@Voi07, Corollary 3.17].
If $f$ is the restriction of a Lefschetz pencil as in @ex:picard-lefschetz-orientation, then by @prop:monodromy-hodge-automorphism the operator $T$ is not an automorphism of the Hodge structure of any fibre.

For fibres of even dimension $2m$, the operator $T=s_\delta$ has order $2$ and its $(-1)$-eigenspace is $\CC\delta$.
It is an automorphism of the Hodge structure $\widetilde\Phi(\tilde t)$ exactly when $\delta\in H^{m,m}$ for that Hodge structure: a one-dimensional sub-Hodge structure of weight $2m$ has type $(m,m)$, and conversely $s_\delta$ preserves each $H^{p,q}$ when $\delta\in H^{m,m}$, as in the proof of @thm:period-domain-component-stabilizer.
:::
