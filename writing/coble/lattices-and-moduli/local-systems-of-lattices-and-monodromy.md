# Local systems of lattices and monodromy {#sec-local-systems-of-lattices}

Throughout this chapter $B$ is an arcwise connected, locally simply connected topological space, and a *local system* on $B$ is a sheaf of abelian groups that is locally isomorphic to a constant sheaf [@Voi07a, Definition 9.8].

::: {.lemma #lem:local-system-on-interval title="A local system on an interval is constant"}

For a local system $\bL$ and a path $\gamma\colon[0,1]\to B$, the sheaf $\gamma^{-1}\bL$ is constant [@Voi07, Lemma 3.6], and both restriction maps
$$
\bL_{\gamma(0)}
\longleftarrow
\Gamma\qty{[0,1],\gamma^{-1}\bL}
\too
\bL_{\gamma(1)}
$$
are isomorphisms.
:::

::: {.definition #def:transport-and-monodromy title="Transport and the monodromy representation"}

The *transport along $\gamma$* is the composite
$$
\gamma^*\colon\bL_{\gamma(0)}\iso\bL_{\gamma(1)}
$$
of the inverse of the first isomorphism of @lem:local-system-on-interval with the second.
For $s\in B$, the *monodromy representation*
$$
\rho\colon\pi_1(B,s)\too\Aut(\bL_s)
$$
of $\bL$ sends the class of a loop $\gamma$ based at $s$ to $\gamma^*$ [@Voi07, Corollary 3.10, Definition 3.13].
The product on $\pi_1(B,s)$ is the one in which $\gamma\delta$ is the loop $\delta$ followed by the loop $\gamma$.
:::

::: {.proposition #prop:transport-homotopy-invariant title="Transport depends only on the homotopy class"}

1. The transport $\gamma^*$ depends only on the homotopy class of $\gamma$ relative to its endpoints [@Voi07, proof of Proposition 3.9].
2. If the path $\delta$ ends where the path $\gamma$ begins, the transport along $\delta$ followed by $\gamma$ is $\gamma^*\circ\delta^*$.
3. The monodromy representation $\rho$ is a well-defined group morphism.
:::

::: {.proof}

Statement (1) is cited.
For (2), let $\epsilon$ be the path $\delta$ followed by $\gamma$.
A section of $\epsilon^{-1}\bL$ over $[0,1]$ restricts to sections of $\delta^{-1}\bL$ and of $\gamma^{-1}\bL$ over $[0,1]$ under the two reparametrizations, with the same value at the common point, so $\epsilon^*=\gamma^*\circ\delta^*$.
Statement (3) follows from (1) and (2).
:::

## Local systems of lattices {#sec-local-systems-of-lattices-definition}

::: {.definition #def:local-system-of-lattices title="Local system of lattices"}

A *local system of lattices* on $B$ is a pair $(\bL,\beta)$ in which $\bL$ is a local system on $B$ whose stalks are finitely generated free abelian groups and
$$
\beta\colon\bL\tensor_{\underline{\ZZ}_B}\bL\too\underline{\ZZ}_B
$$
is a morphism of sheaves of abelian groups.
A *morphism* $(\bL,\beta)\to(\bL',\beta')$ is a morphism of sheaves $\phi\colon\bL\to\bL'$ with $\beta'\circ(\phi\tensor\phi)=\beta$.
:::

Each stalk $(\bL_b,\beta_b)$ of a local system of lattices is a $\ZZ$-lattice in the sense of @def:lattice.

::: {.proposition #prop:local-system-of-lattices-monodromy title="Transport is an isometry"}

Let $(\bL,\beta)$ be a local system of lattices on $B$ and let $s\in B$.

1. For every path $\gamma$ in $B$, the transport $\gamma^*\colon\bL_{\gamma(0)}\to\bL_{\gamma(1)}$ is an isometry for $\beta_{\gamma(0)}$ and $\beta_{\gamma(1)}$.
   The monodromy representation is therefore a group morphism
$$
\rho\colon\pi_1(B,s)\too\Aut(\bL_s,\beta_s).
$$
2. All stalks of $(\bL,\beta)$ are isometric.
   Symmetry, the alternating property and nondegeneracy of $\beta_b$ (@def:form-axioms), and the signature of a nondegenerate symmetric $\beta_b$ (@def:signature), are independent of $b$.
3. Let $(L,\beta_L)$ be a $\ZZ$-lattice and choose $\tilde s\in\widetilde B$ over $s$, where $\pi\colon\widetilde B\to B$ is the universal cover.
   Every group morphism $\rho\colon\pi_1(B,s)\to\Aut(L,\beta_L)$ is the monodromy representation of a local system of lattices $(\bL,\beta)$ on $B$, under an isometry $(\bL_s,\beta_s)\iso(L,\beta_L)$ determined by $\tilde s$.
:::

::: {.proof}

For (1), let $x,y\in\Gamma\qty{[0,1],\gamma^{-1}\bL}$.
The pullback $\gamma^{-1}\beta$ is a morphism of sheaves $\gamma^{-1}\bL\tensor\gamma^{-1}\bL\to\underline{\ZZ}_{[0,1]}$, so $(\gamma^{-1}\beta)(x\tensor y)$ is a section of $\underline{\ZZ}_{[0,1]}$: a locally constant function $[0,1]\to\ZZ$ whose value at $u$ is $\beta_{\gamma(u)}(x_u,y_u)$.
The interval is connected, so the values at $u=0$ and $u=1$ are equal:
$$
\beta_{\gamma(0)}(x_0,y_0)=\beta_{\gamma(1)}(x_1,y_1)=\beta_{\gamma(1)}(\gamma^*x_0,\gamma^*y_0).
$$

Statement (2) follows from (1), because $B$ is arcwise connected.

For (3), the local system with monodromy $\rho$ has sections
$$
\Gamma(O,\bL)=\theset{\sigma\colon\pi^{-1}(O)\to L\text{ locally constant}\st\sigma(\gamma u)=\rho(\gamma)\sigma(u)}
$$
over an open set $O\iscontainedin B$, and evaluation at $\tilde s$ is an isomorphism $\bL_s\iso L$ [@Voi07, proof of Corollary 3.10, (3.1)].
For two such sections, the function $u\mapsto\beta_L(\sigma(u),\tau(u))$ on $\pi^{-1}(O)$ is locally constant, and it is invariant under $\pi_1(B,s)$ because each $\rho(\gamma)$ is an isometry.
It is therefore the pullback of a unique locally constant function $O\to\ZZ$, and this defines $\beta$; evaluation at $\tilde s$ is an isometry by construction.
:::

When the stalks are symmetric, $\Aut(\bL_s,\beta_s)$ is the orthogonal group $\Orth(\bL_s)$ of @sec-isometry-groups; when they are alternating and nondegenerate, it is the symplectic group $\Sp(\bL_s)$.

::: {.lemma #lem:sublocal-system-of-constant-sheaf title="A local system inside a constant sheaf is constant"}

Let $M$ be a $\ZZ$-lattice, and let $(\bL,\beta)$ be a local system of lattices with $\bL\iscontainedin\underline M_B$ a subsheaf and $\beta$ the restriction of $\beta_M$.
Then the monodromy representation of $\bL$ is trivial, and $\bL$ is isomorphic to the constant sheaf $\underline{(\bL_s)}_B$.
:::

::: {.proof}

For a loop $\gamma$ at $s$, the sheaf $\gamma^{-1}\bL$ is a subsheaf of $\underline M_{[0,1]}$, whose sections over $[0,1]$ are the constant functions.
Hence $\gamma^*=\id_{\bL_s}$.
A local system with trivial monodromy representation is constant [@Voi07, Corollary 3.10].
:::

## The sheaves of orientation classes {#sec-orientation-sheaf}

In this section $(\bL,\beta)$ is a local system of lattices on $B$ whose stalks are symmetric and nondegenerate, and $\sigma_+,\sigma_-$ are the orientation characters of @def:orientation-characters for the real quadratic space $\bL_s\tensor\RR$.

::: {.definition #def:orientation-sheaf title="Sheaves of orientation classes of a local system of lattices"}

For $b\in B$, let $\operatorname{Or}^+_b$ be the two-element set of orientation classes of maximal positive-definite subspaces of $\bL_b\tensor\RR$.
By @prop:local-system-of-lattices-monodromy, the transport along a path $\gamma$ induces a bijection $\gamma^*\colon\operatorname{Or}^+_{\gamma(0)}\to\operatorname{Or}^+_{\gamma(1)}$.
The *sheaf of orientation classes of maximal positive-definite subspaces* $\operatorname{Or}^+_{\bL}$ is the sheaf of sets on $B$ with
$$
\Gamma\qty{O,\operatorname{Or}^+_{\bL}}
\definedas
\theset{(o_b)_{b\in O}\st o_b\in\operatorname{Or}^+_b,\ \gamma^*o_{\gamma(0)}=o_{\gamma(1)}\text{ for every path }\gamma\text{ in }O}.
$$
The sheaf $\operatorname{Or}^-_{\bL}$ of orientation classes of maximal negative-definite subspaces is $\operatorname{Or}^+$ of $(\bL,-\beta)$.
:::

::: {.proposition #prop:orientation-sheaf-section title="Monodromy lies in $\ker\sigma_+$ exactly when $\operatorname{Or}^+_{\bL}$ has a global section"}

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

::: {.corollary #cor:orientation-sheaf-orth-plus title="Monodromy lies in $\Orth^+$ exactly when $\operatorname{Or}^+_{\bL}$ has a global section"}

Let $(\bL,\beta)$ be a local system of lattices on $B$ with nondegenerate symmetric stalks.
The sheaf $\operatorname{Or}^+_{\bL}$ has a global section exactly when
$$
\rho\qty{\pi_1(B,s)}\iscontainedin\Orth^+(\bL_s).
$$
:::

::: {.proof}

The representation $\rho$ takes values in $\Orth(\bL_s)$, and $\Orth^+(\bL_s)=\Orth(\bL_s)\cap\ker\sigma_+$ by @prop:orientation-characters-reflections (4).
Apply @prop:orientation-sheaf-section.
:::

::: {.example #ex:monodromy-outside-orth-plus title="A local system of lattices with no global orientation class"}

Let $B=\CC^\times$, let $c\in\pi_1(B,1)\cong\ZZ$ be the class of the loop $\theta\mapsto e^{2\pi i\theta}$, which generates this group, and let $U$ be the hyperbolic plane.
By @prop:local-system-of-lattices-monodromy (3) there is a local system of lattices $(\bL,\beta)$ on $B$ with stalk $U$ and $\rho(c)=-\id_U$.
The signature of $U$ is $(1,1)$, so by @prop:orientation-characters-reflections (2) and @lem:minus-identity-spinor-norm,
$$
\sigma_+(-\id_U)=\spinornorm_\RR(-\id_U)=-1,
\qquad
\sigma_-(-\id_U)=\det(-\id_U)\,\sigma_+(-\id_U)=-1.
$$
The monodromy group is not contained in $\Orth^+(U)$, and neither $\operatorname{Or}^+_{\bL}$ nor $\operatorname{Or}^-_{\bL}$ has a global section (@prop:orientation-sheaf-section).
:::

## Polarized variations of Hodge structure {#sec-polarized-vhs}

::: {.definition #def:polarized-integral-vhs title="Polarized integral variation of Hodge structure"}

Let $k$ be an integer and let $(L,Q)$ be a $\ZZ$-lattice with $Q$ nondegenerate, symmetric if $k$ is even and alternating if $k$ is odd.
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
For $j\ge0$ define the real subspaces
$$
R_j\definedas\qty{H^{m+j,m-j}\oplus H^{m-j,m+j}}\cap L_\RR
$$
of $L_\RR$, so that $R_0=H^{m,m}\cap L_\RR$; only finitely many are nonzero.

1. $L_\RR=\bigoplus_{j\ge0}R_j$, the summands are pairwise orthogonal for $Q$, and $(-1)^{m+j}Q$ is positive definite on $R_j$.
2. The subspace
$$
W^{\mathrm{odd}}_F\definedas\bigoplus_{j\text{ odd}}R_j
$$
is a subspace of maximal dimension among those on which $\epsilon Q$ is positive definite, and
$$
W^{\mathrm{ev}}_F\definedas\bigoplus_{j\text{ even}}R_j
$$
is a subspace of maximal dimension among those on which $-\epsilon Q$ is positive definite.
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
Statement (2) follows: $L_\RR=W^{\mathrm{odd}}_F\perp W^{\mathrm{ev}}_F$ with $\epsilon Q$ positive definite on the first summand and negative definite on the second, so their dimensions are the two indices of the signature of $Q$ (@thm:sylvester).
:::

## Period domains and their components {#sec-period-domain-components}

Fix $k$, a $\ZZ$-lattice $(L,Q)$ as in @def:polarized-integral-vhs, and Hodge numbers $h^{p,q}$.
The *period domain* $D$ is the set of Hodge structures of weight $k$ on $L$ polarized by $Q$ with these Hodge numbers.
Put
$$
G_\RR\definedas\Aut(L_\RR,Q),
\qquad
G_\ZZ\definedas\Aut(L,Q)\iscontainedin G_\RR,
$$
and for $F\in D$ let $V_F\iscontainedin G_\RR$ be the stabilizer of $F$ for the action $g\cdot F^\bullet\definedas g_\CC F^\bullet$.

::: {.theorem #thm:period-domain-homogeneous title="The period domain is a homogeneous complex manifold"}

1. The set $D$ is a complex manifold, and $G_\RR$ acts transitively on it [@Sch73, §3].
2. For every $F\in D$ the group $V_F$ is compact, and $G_\ZZ$ is a discrete subgroup of $G_\RR$ [@Sch73, §3, (3.7), (3.8)].
3. Every $g\in V_F$ preserves each subspace $H^{p,q}_F=F^p\cap\overline{F^q}$ of $L_\CC$.
:::

::: {.proof}

Statements (1) and (2) are cited.
For (3), $g_\CC$ commutes with complex conjugation and $g_\CC F^p=F^p$ for all $p$, so $g_\CC\overline{F^q}=\overline{F^q}$.
:::

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

The subspaces $F^p$ and $\overline{F^q}$ depend continuously on $F\in D$, and their intersection $H^{p,q}_F$ has constant dimension, so it depends continuously on $F$; so do $W^{\mathrm{odd}}_F$ and $W^{\mathrm{ev}}_F$.
By @lem:hodge-real-pieces (3), $W^{\mathrm{odd}}_F$ is isomorphic to the complex vector space $\bigoplus_{j\text{ odd}}H^{m+j,m-j}_F$; let $o^{\mathrm{odd}}_F$ be the resulting complex orientation.
By @lem:hodge-real-pieces (2), the pair $\qty{W^{\mathrm{odd}}_F,o^{\mathrm{odd}}_F}$ is a point of the space $\widetilde\Gr^+(L_\RR,\epsilon Q)$ of @sec-orientation-characters, and
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
Let $\pi\colon\widetilde B\to B$ be the universal cover and choose $\tilde s\in\widetilde B$ over $s$.
The group $\pi_1(B,s)$ acts on $\widetilde B$ by the deck transformations used in the proof of @prop:local-system-of-lattices-monodromy (3).

::: {.proposition #prop:lifted-period-map title="The lifted period map"}

1. The sheaf $\pi^{-1}\bL$ is constant, and the restriction $\Gamma\qty{\widetilde B,\pi^{-1}\bL}\to\bL_s$ to the stalk at $\tilde s$ is an isomorphism [@Voi07, proof of Corollary 3.10].
2. For $\tilde t\in\widetilde B$, let $\widetilde\Phi(\tilde t)$ be the image of the filtration $F^\bullet_{\pi(\tilde t)}$ under the isomorphism $\bL_{\pi(\tilde t)}\iso\bL_s$ of (1). Then $\widetilde\Phi(\tilde t)\in D$ and $\widetilde\Phi(\tilde s)=F^\bullet_s$.
3. The map $\widetilde\Phi\colon\widetilde B\to D$ satisfies
$$
\widetilde\Phi(\gamma\tilde t)=\rho(\gamma)\,\widetilde\Phi(\tilde t)
\qquad\text{for }\tilde t\in\widetilde B,\ \gamma\in\pi_1(B,s)
$$ {#eq-period-map-equivariance}
[@Sch73, (3.24)].
4. The map $\widetilde\Phi$ is holomorphic [@Sch73, Theorem 3.27].
:::

::: {.proof}

Statements (1), (3) and (4) are cited.
For (2), the isomorphism of (1) is an isometry for $Q$, because $Q$ is a morphism of sheaves, so it carries a Hodge structure polarized by $Q_{\pi(\tilde t)}$ to one polarized by $Q_s$.
The Hodge numbers of $F^\bullet_b$ are the ranks of the bundles $F^p$ and their conjugates, which are constant on the connected manifold $B$.
:::

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
| $k$ odd | any | $\Sp(L)$ |

For $k$ odd the domain $D$ is connected, so $D^+=D$.
:::

::: {.proof}

The image $\widetilde\Phi(\widetilde B)$ is connected and contains $F^\bullet_s$, so it lies in $D^+$.
For $\gamma\in\pi_1(B,s)$, @eq-period-map-equivariance shows that $\rho(\gamma)$ maps a point of $D^+$ to a point of $D^+$.
The homeomorphism $\rho(\gamma)$ of $D$ permutes the components, so $\rho(\gamma)D^+=D^+$.
For $k$ even, the table is @thm:period-domain-component-stabilizer.
For $k$ odd, the form $Q$ is alternating and $G_\RR=\Sp(L_\RR)$ is the group of real points of a simply connected semisimple algebraic group [@Mil17, Example 23.61], so it is connected [@Mil17, Theorem 25.54].
It acts transitively on $D$, so $D$ is connected, and $\Stab_{G_\ZZ}(D)=G_\ZZ=\Sp(L)$.
:::

::: {.lemma #lem:weight-two-positive-subspace title="The subspace $W^{\mathrm{odd}}_F$ in weight $2$"}

Let $k=2$ and $F\in D$.
Then $\epsilon=+1$, and
$$
W^{\mathrm{odd}}_F
=\qty{H^{2,0}_F\oplus H^{0,2}_F}\cap L_\RR
=\theset{v+\bar v\st v\in H^{2,0}_F}
$$
is a subspace of $L_\RR$ of real dimension $2h^{2,0}$ on which $Q$ is positive definite.
:::

::: {.proof}

Here $m=1$, so $\epsilon=(-1)^{m+1}=+1$, and $R_j=0$ for $j\ge2$, so $W^{\mathrm{odd}}_F=R_1$.
By @lem:hodge-real-pieces (3) and its proof, $v\mapsto v+\bar v$ is an isomorphism of real vector spaces $H^{2,0}_F\to R_1$, and $H^{2,0}_F$ has real dimension $2h^{2,0}$.
By @lem:hodge-real-pieces (1), $(-1)^{m+1}Q=Q$ is positive definite on $R_1$.
:::

::: {.proposition #prop:component-stabilizer-versus-orth-plus title="$\Stab_{G_\ZZ}(D^+)$ and $\Orth^+(L)$"}

Let $k=2m$ and let $D^+$ be a connected component of $D$.

1. If $m$ is odd and $h^{m,m}>0$, then
$$
\Stab_{G_\ZZ}(D^+)=\Orth^+(L).
$$
2. If $m$ is even and $h^{m,m}>0$, then
$$
\Stab_{G_\ZZ}(D^+)=\Orth(L)\cap\ker\sigma_-=\Orth^+(L(-1)),
$$
and every $g\in\Orth(L)$ with $\det g=-1$ lies in exactly one of $\Stab_{G_\ZZ}(D^+)$ and $\Orth^+(L)$.
   Consequently $\Stab_{G_\ZZ}(D^+)=\Orth^+(L)$ exactly when $\det$ is trivial on $\Orth(L)$, and the two groups differ when the rank of $L$ is odd.
3. If $h^{m,m}=0$, then
$$
\Stab_{G_\ZZ}(D^+)=\Orth^+(L)\cap\ker\det,
$$
a subgroup of $\Orth^+(L)$ of index at most $2$, equal to $\Orth^+(L)$ exactly when $\det$ is trivial on $\Orth^+(L)$.
:::

::: {.proof}

By @prop:orientation-characters-reflections (2) and (4),
$$
\Orth^+(L)=\Orth(L)\cap\ker\sigma_+,
\qquad
\sigma_+\sigma_-=\det.
$$
The sign of @thm:period-domain-component-stabilizer is $\epsilon=(-1)^{m+1}$.

(1) Here $\epsilon=+1$, and the theorem gives $\Stab_{G_\ZZ}(D^+)=\Orth(L)\cap\ker\sigma_+$.

(2) Here $\epsilon=-1$, and the theorem gives $\Stab_{G_\ZZ}(D^+)=\Orth(L)\cap\ker\sigma_-$.
The lattice $L(-1)$ of @def:form-twist has $\Orth(L(-1))=\Orth(L)$, and the positive orientation character of $L(-1)_\RR$ is $\sigma_-$ (@def:orientation-characters), so $\Orth(L)\cap\ker\sigma_-=\Orth^+(L(-1))$.
If $\det g=-1$, then $\sigma_+(g)\neq\sigma_-(g)$, so exactly one of $\sigma_+(g)$, $\sigma_-(g)$ is $+1$.
If $\det$ is trivial on $\Orth(L)$, then $\sigma_+=\sigma_-$ on $\Orth(L)$ and the two kernels are equal.
The isometry $-\id_L$ has determinant $-1$ when the rank of $L$ is odd.

(3) The theorem gives $\Stab_{G_\ZZ}(D^+)=\Orth(L)\cap\ker\sigma_+\cap\ker\sigma_-$, and $\ker\sigma_+\cap\ker\sigma_-=\ker\sigma_+\cap\ker\det$.
The group $\Orth^+(L)\cap\ker\det$ is the kernel of $\det\colon\Orth^+(L)\to\theset{\pm1}$.
:::

::: {.corollary #cor:weight-two-component-stabilizer title="The component stabilizer in weight $2$"}

If $k=2$ and $h^{1,1}>0$, then
$$
\Stab_{G_\ZZ}(D^+)=\Orth^+(L).
$$
:::

::: {.proof}

This is @prop:component-stabilizer-versus-orth-plus (1) with $m=1$.
:::

::: {.example #ex:weight-zero-vhs title="A weight-zero variation with monodromy outside $\ker\sigma_{-\epsilon}$"}

Let $B=\CC^\times$ and $c\in\pi_1(B,1)$ be as in @ex:monodromy-outside-orth-plus, and let $(\bL,Q)$ be the local system of lattices on $B$ with stalk $(\ZZ,xy)$ and $\rho(c)=-1$ (@prop:local-system-of-lattices-monodromy).
With $F^0=\bL\tensor\OO_B$ and $F^1=0$, the triple $(\bL,Q,F^\bullet)$ is a polarized integral variation of Hodge structure of weight $0$ with $h^{0,0}=1$.
Here $m=0$ and $\epsilon=-1$.
The monodromy $-1$ is the reflection in a vector of positive square, so $\sigma_+(-1)=-1$ and $\sigma_-(-1)=+1$ (@prop:orientation-characters-reflections).
The monodromy group lies in $\ker\sigma_\epsilon$ and not in $\ker\sigma_{-\epsilon}$.
:::

## Cohomology of families {#sec-cohomology-of-families-monodromy}

Let $f\colon\mcx\to B$ be a proper holomorphic submersion of complex manifolds with $B$ connected and with fibres $X_b$ of dimension $n$, and let $\omega\in H^2(\mcx,\ZZ)$ be a class whose restriction to every fibre is a Kähler class.
For $0\le k\le2n$ put
$$
\bV^k\definedas R^kf_*\underline{\ZZ}_{\mcx}/\text{torsion},
$$
and let $L_\omega\colon\bV^k\to\bV^{k+2}$ be the cup product with $\omega$.
For $k\le n$ put
$$
\bV^k_{\mathrm{prim}}\definedas\ker\qty{L_\omega^{n-k+1}\colon\bV^k\too\bV^{2n-k+2}}
$$
and
$$
Q(\alpha,\beta)\definedas\int_{X_b}\omega^{n-k}\cupprod\alpha\cupprod\beta
\qquad\text{for }\alpha,\beta\in\bV^k_b.
$$

::: {.proposition #prop:primitive-cohomology-vhs title="Primitive cohomology of a polarized family"}

1. $(\bV^k,Q)$ is a local system of lattices on $B$, and $L_\omega$ is a morphism of local systems.
2. $\qty{\bV^k_{\mathrm{prim}},Q}$ with the Hodge filtration of the fibres is a polarized integral variation of Hodge structure of weight $k$.
:::

::: {.proof}

The local system $R^kf_*\underline\ZZ$ carries the cup product, and the monodromy representation is compatible with it [@Voi07, §3.1.2]; the class $\omega|_{X_b}$ is locally constant, so $L_\omega$ and $Q$ are compatible with the local identifications of the stalks [@Voi07a, §10.1.3].
This proves (1).

For (2), put $\mathcal H^j\definedas\bV^j\tensor_\ZZ\OO_B$, with its flat connection $\nabla$.
The Hodge filtrations of the fibres form a filtration of $\mathcal H^j$ by holomorphic subbundles $F^p\mathcal H^j$ with $\nabla F^p\mathcal H^j\iscontainedin F^{p-1}\mathcal H^j\tensor\Omega_B$ [@Voi07a, Theorem 10.3].
The operator $L_\omega^{n-k+1}$ is a flat morphism $\mathcal H^k\to\mathcal H^{2n-k+2}$ that maps $F^p\mathcal H^k$ to $F^{p+n-k+1}\mathcal H^{2n-k+2}$, because $\omega|_{X_b}$ has type $(1,1)$.
On each fibre the Lefschetz decomposition is a decomposition of Hodge structures [@Voi07a, §6.2.3, §7.1.2], so the kernel of $L_\omega^{n-k+1}$ on $F^pH^k(X_b,\CC)$ is $F^p\cap H^k(X_b,\CC)_{\mathrm{prim}}$, and its dimension is a sum of primitive Hodge numbers.
The Hodge numbers of the fibres are locally constant [@Voi07a, Proposition 9.20], and so are the primitive Hodge numbers, which are differences of Hodge numbers by the Lefschetz decomposition.
A morphism of holomorphic vector bundles of constant rank has a holomorphic subbundle as kernel, so
$$
F^p\mathcal H^k_{\mathrm{prim}}\definedas F^p\mathcal H^k\cap\qty{\bV^k_{\mathrm{prim}}\tensor_\ZZ\OO_B}
$$
is a holomorphic subbundle of $\bV^k_{\mathrm{prim}}\tensor_\ZZ\OO_B$.
The connection $\nabla$ preserves the flat subbundle $\bV^k_{\mathrm{prim}}\tensor_\ZZ\OO_B$, so condition (2) of @def:polarized-integral-vhs for $F^\bullet\mathcal H^k_{\mathrm{prim}}$ follows from the inclusion $\nabla F^p\mathcal H^k\iscontainedin F^{p-1}\mathcal H^k\tensor\Omega_B$.
Condition (1) is the pair of Hodge--Riemann bilinear relations for the primitive cohomology of each fibre [@Voi07a, Theorem 6.32, §7.1.2].
:::

::: {.corollary #cor:middle-cohomology-monodromy title="Monodromy of even-dimensional middle cohomology"}

Let $n=2m$, so that $Q$ is the intersection form on $\bV^n$, and let $\rho$ be the monodromy representation of $\bV^n$ at $s\in B$.

1. The restriction of $\rho$ to $\bV^n_{\mathrm{prim},s}$ takes values in $\ker\sigma_\epsilon$ with $\epsilon=(-1)^{m+1}$, and in $\ker\sigma_+\cap\ker\sigma_-$ if the Hodge number $h^{m,m}$ of $\bV^n_{\mathrm{prim}}$ is zero.
2. If $n=2$, then $\rho$ takes values in $\Orth\qty{H^2(X_s,\ZZ)/\text{torsion}}\cap\ker\sigma_+$.
:::

::: {.proof}

Statement (1) is @cor:vhs-monodromy-stabilizes-component for the variation of @prop:primitive-cohomology-vhs.

For (2), put $\kappa\definedas\omega|_{X_s}$.
Then $Q(\kappa,\kappa)=\int_{X_s}\omega^2>0$, the class $\kappa$ is fixed by $\rho$, and $\bV^2_{\mathrm{prim},s}=\kappa^\perp$.
Each $\rho(\gamma)$ is therefore $\id_{\RR\kappa}\oplus g$ on $\RR\kappa\perp\qty{\kappa^\perp}_\RR$, with $g$ the monodromy of the primitive part.
By (1) with $m=1$, $\sigma_+(g)=+1$, and @prop:orientation-characters-reflections (3) gives $\sigma_+(\rho(\gamma))=+1$.
:::

::: {.lemma #lem:k3-orientation-character title="The K3 orientation character is $\sigma_+$"}

For the K3 lattice, the character $\sigma_{\lkt}$ of @def:k3-positive-cone-orientation is the positive orientation character $\sigma_+$ of $\lkt_\RR$.
:::

::: {.proof}

Both are group morphisms $\Orth(\lkt_\RR)\to\theset{\pm1}$, and the reflections generate $\Orth(\lkt_\RR)$ (@def:spinor-norm), so it suffices to compare them on a reflection $s_w$.
If $w^2<0$, choose a positive-definite three-plane $W_3\iscontainedin w^\perp$; then $s_w$ fixes $W_3\sm\theset{0}$ pointwise, so it fixes the two group generators of $H_2\qty{W_3\sm\theset{0},\ZZ}\cong\ZZ$ and $\sigma_{\lkt}(s_w)=+1$.
If $w^2>0$, choose $W_3$ containing $w$; then $s_w$ preserves $W_3$ and reverses its orientation, so it exchanges these two group generators and $\sigma_{\lkt}(s_w)=-1$.
These are the values of $\sigma_+$ in @prop:orientation-characters-reflections (1).
:::

::: {.corollary #cor:k3-family-orientation-character title="Monodromy of a family of K3 surfaces with a class $\omega$"}

In @cor:middle-cohomology-monodromy let $n=2$, let the fibres be K3 surfaces, and let $\eta_s\colon H^2(X_s,\ZZ)\iso\lkt$ be an isometry.
Then for every $\gamma\in\pi_1(B,s)$,
$$
\sigma_{\lkt}\qty{\eta_s\,\rho(\gamma)\,\eta_s^{-1}}=+1.
$$
:::

::: {.proof}

The group $H^2(X_s,\ZZ)$ is torsion-free (@prop:k3-lattice), so $\sigma_+(\rho(\gamma))=+1$ by @cor:middle-cohomology-monodromy (2).
The isometry $\eta_s$ maps the orientation classes of maximal positive-definite subspaces of $H^2(X_s,\RR)$ to those of $\lkt_\RR$, so $\sigma_+\qty{\eta_s\,\rho(\gamma)\,\eta_s^{-1}}=\sigma_+(\rho(\gamma))$.
By @lem:k3-orientation-character, $\sigma_+=\sigma_{\lkt}$ on $\Orth(\lkt_\RR)$.
:::

@prop:k3-monodromy-positive treats the monodromy group of an arbitrary family of K3 surfaces over a connected base.

::: {.example #ex:picard-lefschetz-orientation title="Picard--Lefschetz reflections"}

Let $f\colon X\to\Delta$ be a Lefschetz degeneration with $X$ smooth of dimension $2m+1$, let $t\in\Delta^*$, and let $T$ be the monodromy of the class of the positively oriented loop, which generates the group $\pi_1(\Delta^*,t)$, on $H^{2m}(X_t,\ZZ)$ with its intersection form $\langle\ ,\ \rangle$.
Let $\delta$ be the class of a vanishing sphere.
The Picard--Lefschetz formula is
$$
T(\alpha)=\alpha+\epsilon_{2m+1}\langle\alpha,\delta\rangle\delta,
\qquad
\epsilon_{2m+1}=-(-1)^m,
\qquad
\langle\delta,\delta\rangle=2(-1)^m
$$
[@Voi07, Theorem 3.16, Remark 3.18, Remark 3.21]; here $\epsilon_{2m+1}$ is the sign of [@Voi07, Theorem 3.16] for the dimension $2m+1$ of $X$.
Hence $T$ is the reflection $s_\delta$, and by @prop:orientation-characters-reflections
$$
\sigma_+(T)=(-1)^{m+1},
\qquad
\sigma_-(T)=(-1)^m.
$$
With $\epsilon=(-1)^{m+1}$ this reads $\sigma_\epsilon(T)=+1$ and $\sigma_{-\epsilon}(T)=-1$.

A generic pencil of hyperplane sections of a smooth projective variety $Y\iscontainedin\PP^N$ of dimension $2m+1$ is a Lefschetz pencil [@Voi07, Corollary 2.10], and near each of its critical values it is a Lefschetz degeneration whose vanishing class is primitive [@Voi07, Corollary 2.25, Lemma 2.26].
Such a $T$ is therefore a monodromy operator of the variation $\bV^{2m}_{\mathrm{prim}}$ of @prop:primitive-cohomology-vhs over the set of regular values of the pencil.
For $m$ even, $T\notin\ker\sigma_+$, so the conclusion of @cor:middle-cohomology-monodromy (2) fails for $n=2m\ge4$ with $m$ even.
:::

## Monodromy that fixes a primitive sublattice {#sec-monodromy-fixing-sublattice}

In this section $\Lambda$ is a nondegenerate $\ZZ$-lattice with form $\beta$, also written $\beta$ on $\Lambda_\QQ$, and $\iota\colon S\injects\Lambda$ is a primitive embedding (@def:primitive-embedding) of a nondegenerate lattice.
The lattice $S$ is identified with $\iota(S)$, and
$$
T\definedas S^{\perp\Lambda}.
$$
The metric duals $S^\#\iscontainedin S_\QQ$ and $T^\#\iscontainedin T_\QQ$ are those of @def:metric-dual, and $\rho_T\colon\Orth(T)\to\Orth(A_T)$ is the discriminant representation with kernel $\widetilde\Orth(T)$ (@def:discriminant-rep).

::: {.lemma #lem:components-in-a-primitive-splitting title="The components of an element of $\Lambda$ along $S$ and $T$"}

1. $\Lambda_\QQ=S_\QQ\perp T_\QQ$, the lattice $T$ is nondegenerate, $T=\Lambda\cap T_\QQ$ and $S=T^{\perp\Lambda}$.
2. For $x\in\Lambda$, write $x=x_S+x_T$ with $x_S\in S_\QQ$ and $x_T\in T_\QQ$. Then $x_S\in S^\#$ and $x_T\in T^\#$.
3. If $\Lambda$ is unimodular (@def:unimodular), the map $\Lambda\to T^\#$, $x\mapsto x_T$, is surjective.
:::

::: {.proof}

For (1), $S$ is nondegenerate, so $\Lambda_\QQ=S_\QQ\perp S_\QQ^\perp$.
Every element of $S_\QQ^\perp$ has a nonzero integer multiple in $\Lambda\cap S_\QQ^\perp=T$, so $S_\QQ^\perp=T_\QQ$; this gives the decomposition and $T=\Lambda\cap T_\QQ$.
The form on $\Lambda_\QQ$ is nondegenerate and is the orthogonal sum of its restrictions to $S_\QQ$ and $T_\QQ$, so its restriction to $T_\QQ$ is nondegenerate.
Finally $T^{\perp\Lambda}=\Lambda\cap T_\QQ^\perp=\Lambda\cap S_\QQ$, and $\Lambda\cap S_\QQ=S$ because $\Lambda/S$ is torsion-free.

For (2), let $t\in T$.
Then $\beta(x_T,t)=\beta(x,t)\in\ZZ$, so $x_T\in T^\#$, and in the same way $x_S\in S^\#$.

For (3), let $y\in T^\#$.
By (1) the module $\Lambda/T$ is torsion-free; it is finitely generated, hence free, and $T$ is a direct summand of the module $\Lambda$.
The linear form $\beta(y,-)\colon T\to\ZZ$ therefore extends to a linear form $\lambda\colon\Lambda\to\ZZ$.
Since $\Lambda$ is unimodular, $\lambda=\beta(x,-)$ for some $x\in\Lambda$.
Then $\beta(x_T-y,t)=0$ for every $t\in T$, and $T$ is nondegenerate, so $x_T=y$.
:::

::: {.definition #def:pointwise-stabilizer-of-sublattice title="Pointwise stabilizer of a sublattice"}

The *pointwise stabilizer* of $S$ in $\Orth(\Lambda)$ is the subgroup
$$
\Fix_{\Orth(\Lambda)}(S)\definedas\theset{g\in\Orth(\Lambda)\st g\circ\iota=\iota}.
$$
:::

::: {.lemma #lem:restriction-from-pointwise-stabilizer title="Restriction from the pointwise stabilizer to $T$"}

Every $g\in\Fix_{\Orth(\Lambda)}(S)$ satisfies $g(T)=T$, and
$$
\operatorname{res}_T\colon\Fix_{\Orth(\Lambda)}(S)\too\Orth(T),
\qquad
g\longmapsto g|_T,
$$
is an injective group morphism.
:::

::: {.proof}

Let $g\in\Fix_{\Orth(\Lambda)}(S)$ and $t\in T$.
For $x\in S$, $\beta(g(t),x)=\beta(g(t),g(x))=\beta(t,x)=0$, so $g(T)\iscontainedin T$; the same holds for $g^{-1}$, so $g(T)=T$ and $g|_T\in\Orth(T)$.
Restriction is compatible with composition.
An element $g$ with $g|_S=\id_S$ and $g|_T=\id_T$ is the identity on $S_\QQ+T_\QQ$, which is $\Lambda_\QQ$ by @lem:components-in-a-primitive-splitting (1).
:::

::: {.theorem #thm:pointwise-stabilizer-is-discriminant-kernel title="For unimodular $\Lambda$, the pointwise stabilizer of $S$ is $\widetilde\Orth(T)$"}

Let $\Lambda$ be unimodular.
The image of the morphism $\operatorname{res}_T$ of @lem:restriction-from-pointwise-stabilizer is $\widetilde\Orth(T)$:
$$
\operatorname{res}_T\colon\Fix_{\Orth(\Lambda)}(S)\iso\widetilde\Orth(T).
$$
:::

::: {.proof}

Let $g\in\Fix_{\Orth(\Lambda)}(S)$ and $y\in T^\#$.
By @lem:components-in-a-primitive-splitting (3) there is $x\in\Lambda$ with $x_T=y$.
The isometry $g_\QQ$ is the identity on $S_\QQ$, so $g_\QQ(x)=x_S+g_\QQ(y)$ and
$$
g_\QQ(y)-y=g(x)-x\in\Lambda\cap T_\QQ=T.
$$
Hence $\rho_T\qty{\operatorname{res}_T(g)}=\id_{A_T}$, that is, $\operatorname{res}_T(g)\in\widetilde\Orth(T)$.

Let $b\in\widetilde\Orth(T)$ and put $g\definedas\id_{S_\QQ}\oplus b_\QQ\in\Orth(\Lambda_\QQ)$.
For $x\in\Lambda$,
$$
g(x)=x+\qty{b_\QQ(x_T)-x_T},
$$
and $b_\QQ(x_T)-x_T\in T$ because $x_T\in T^\#$ by @lem:components-in-a-primitive-splitting (2) and $\rho_T(b)=\id_{A_T}$.
Hence $g(\Lambda)\iscontainedin\Lambda$.
The same argument for $b^{-1}$ gives $g^{-1}(\Lambda)\iscontainedin\Lambda$, so $g$ restricts to an element of $\Fix_{\Orth(\Lambda)}(S)$ with $\operatorname{res}_T(g)=b$.
Injectivity is @lem:restriction-from-pointwise-stabilizer.
:::

::: {.proposition #prop:pointwise-stabilizer-gluing-stabilizer title="The image of $\operatorname{res}_T$ for a nondegenerate $\Lambda$"}

Let $h\colon(H,0)\injects A_{T\perp S}$ be the gluing datum of @def:gluing-datum-of-a-pair for $M=T$, $N=S$ and $L=\Lambda$.
The image of $\operatorname{res}_T$ is the group $\Stab_{\Orth(T)}(h)$ of @cor:liftable-automorphisms for $\Gamma=\Orth(T)$, and
$$
\widetilde\Orth(T)\iscontainedin\Stab_{\Orth(T)}(h)\iscontainedin\Orth(T).
$$
:::

::: {.proof}

The inclusions $T\injects\Lambda$ and $S\injects\Lambda$ are primitive with $S=T^{\perp\Lambda}$ by @lem:components-in-a-primitive-splitting (1), so @def:gluing-datum-of-a-pair applies.
By @cor:liftable-automorphisms, the elements of $\Stab_{\Orth(T)}(h)$ are exactly the isometries of $T$ that extend to an isometry of $\Lambda$ fixing $S$ pointwise, that is, the elements of the image of $\operatorname{res}_T$; the same corollary gives the two inclusions.
:::

::: {.remark #rmk:pointwise-stabilizer-mechanism title="The step that uses unimodularity"}

In the proof of @thm:pointwise-stabilizer-is-discriminant-kernel, an element $y\in T^\#$ is the component $x_T$ of an element $x\in\Lambda$, the isometry $g$ fixes the other component $x_S$, and $g_\QQ(y)-y$ is the difference $g(x)-x$ of two elements of $\Lambda$.
Unimodularity enters only through @lem:components-in-a-primitive-splitting (3).
No hypothesis of the theorem concerns the isometry class of $S$.
:::

::: {.proposition #prop:monodromy-fixing-sublattice title="Monodromy on the orthogonal complement of a sublattice of flat classes"}

Let $(\bL,\beta)$ be a local system of lattices on $B$ with symmetric stalks, let $s\in B$, and let $\rho$ be its monodromy representation.
Suppose that the stalk $\Lambda\definedas\bL_s$ is unimodular, that $S\iscontainedin\Lambda$ is a primitive nondegenerate sublattice with $T\definedas S^{\perp\Lambda}$, and that every element of $S$ is the value at $s$ of a global section of $\bL$.

1. $\rho\qty{\pi_1(B,s)}\iscontainedin\Fix_{\Orth(\Lambda)}(S)$.
2. The representation $\operatorname{res}_T\circ\rho$ on $T$ takes values in $\widetilde\Orth(T)$.
3. If $\rho$ takes values in $\Orth^+(\Lambda)$, then $\operatorname{res}_T\circ\rho$ takes values in
$$
\Orth^+(T)\cap\widetilde\Orth(T).
$$
:::

::: {.proof}

For (1), let $x\in S$, let $e$ be a global section of $\bL$ with $e(s)=x$, and let $\gamma$ be a loop at $s$.
The pullback of $e$ is a section of $\gamma^{-1}\bL$ over $[0,1]$ with value $x$ at both endpoints, so $\gamma^*x=x$ by @def:transport-and-monodromy.
The transport $\gamma^*=\rho(\gamma)$ is an isometry of $\Lambda$ by @prop:local-system-of-lattices-monodromy (1).
Statement (2) follows from (1) and @thm:pointwise-stabilizer-is-discriminant-kernel.

For (3), let $g\in\rho\qty{\pi_1(B,s)}$.
By (1), $g_\RR=\id_{S_\RR}\oplus\operatorname{res}_T(g)_\RR$ on $\Lambda_\RR=S_\RR\perp T_\RR$, so $\sigma_+(g)=\sigma_+\qty{\operatorname{res}_T(g)}$ by @prop:orientation-characters-reflections (3).
By @prop:orientation-characters-reflections (4), $\sigma_+(g)=+1$, and then $\operatorname{res}_T(g)\in\Orth^+(T)$.
:::

::: {.corollary #cor:lattice-polarized-k3-monodromy title="Monodromy of a family of K3 surfaces on the complement of a sublattice of flat classes"}

In @cor:k3-family-orientation-character, let $S\iscontainedin\lkt$ be a primitive nondegenerate sublattice with $T\definedas S^{\perp\lkt}$, and suppose that every element of $\eta_s^{-1}(S)$ is the value at $s$ of a global section of $R^2f_*\underline\ZZ_{\mcx}$.
Then the representation $\gamma\mapsto\eta_s\,\rho(\gamma)\,\eta_s^{-1}$ preserves $T$, and its restriction to $T$ takes values in
$$
\Orth^+(T)\cap\widetilde\Orth(T).
$$
:::

::: {.proof}

The lattice $\lkt$ is unimodular (@prop:k3-lattice).
By @cor:k3-family-orientation-character and @lem:k3-orientation-character, $\sigma_+\qty{\eta_s\,\rho(\gamma)\,\eta_s^{-1}}=+1$ for every $\gamma$, so the representation takes values in $\Orth^+(\lkt)$ by @prop:orientation-characters-reflections (4).
The sheaf $R^2f_*\underline\ZZ_{\mcx}$ with the cup product is a local system of lattices with symmetric stalks by @prop:primitive-cohomology-vhs (1).
Apply @prop:monodromy-fixing-sublattice (3) to it, with the identification $\eta_s$ of its stalk at $s$ with $\lkt$.
:::

::: {.example #ex:lattice-polarized-k3-monodromy-groups title="The group $\Orth^+(T)\cap\widetilde\Orth(T)$ for three sublattices"}

In @cor:lattice-polarized-k3-monodromy, a line bundle $\mcl$ on $\mcx$ has a class $c_1(\mcl)\in H^2(\mcx,\ZZ)$, and the image of $c_1(\mcl)$ under $H^2(\mcx,\ZZ)\to\Gamma\qty{B,R^2f_*\underline\ZZ_{\mcx}}$ is a global section with value $c_1(\mcl|_{X_s})$ at $s$.

1. For $S=\ZZ h$ with $h$ the vector of @def:degree-2d-k3-period-data, the lattice $T$ is $\lkttd$, and the group is $\Orth^+(\lkttd)\cap\widetilde\Orth(\lkttd)$.
   It is a subgroup of $\Orth^+(\lkttd)$, the group in which @prop:polarized-k3-monodromy-positive places the monodromy.
2. If $S$ is unimodular, then $A_T=0$ by the isometry $A_T\iso A_S(-1)$ of @cor:lifting-unimodular, which applies because $S=T^{\perp\lkt}$ (@lem:components-in-a-primitive-splitting (1)), and $\widetilde\Orth(T)=\Orth(T)$, so the group is $\Orth^+(T)$.
3. For a primitive sublattice $S$ isometric to $E_{10}(2)$, for the lattice $E_{10}$ of @def:enriques-lattice, the lattice $S$ is nondegenerate because $E_{10}$ is, and the group is again $\Orth^+(T)\cap\widetilde\Orth(T)$: the restricted monodromy acts as the identity on $A_T$, which is isometric to $A_S(-1)$ by @cor:lifting-unimodular.

For $T$ of signature $(2,n)$ with $n\ge1$, the group $\Orth^+(T)\cap\widetilde\Orth(T)$ is $\widetilde\Orth^+(T)$ of @def:simultaneous-discriminant-spinor-kernel, and it is the group $\Orth^+(T)^*$ of @def:type-iv-period-domain, in which $\discriminantkernel{T}$ denotes $\widetilde\Orth(T)$.
:::

## Monodromy and automorphisms of Hodge structures {#sec-monodromy-hodge-automorphisms}

Let $(\bL,Q,F^\bullet)$, $s$, $D$ and $\widetilde\Phi$ be as in @sec-period-domain-components.
For $F\in D$, an *automorphism of the polarized Hodge structure* $F$ is an element $g\in G_\ZZ$ with $gF^p=F^p$ for all $p$; these form the group $G_\ZZ\cap V_F$.

::: {.proposition #prop:k3-primitive-hodge-automorphisms title="Automorphisms of the primitive Hodge structure of a polarized K3 surface"}

Let $X$ be a K3 surface, let $h\in H^2(X,\ZZ)$ be a primitive ample class with $h^2=2d$, and let $G_h$ be the group of Hodge isometries of $H^2(X,\ZZ)$ (@sec-k3-automorphisms) that fix $h$.
Give $h^\perp$ the Hodge structure with $(p,q)$-part $H^{p,q}(X)\cap h^\perp_\CC$.

1. Restriction to $h^\perp$ is an injective group morphism from $G_h$ to the group of isometries of $h^\perp$ that preserve this Hodge structure.
2. The isometry $-\id_{h^\perp}$ preserves this Hodge structure, and it is the restriction of an element of $G_h$ exactly when $d=1$.
:::

::: {.proof}

An element $g\in G_h$ preserves $h^\perp$ and each $H^{p,q}(X)$, so its restriction preserves each $H^{p,q}(X)\cap h^\perp_\CC$.
Since $h^2\neq0$, $H^2(X,\QQ)=\QQ h\perp h^\perp_\QQ$, so $g$ is determined by $g(h)=h$ and $g|_{h^\perp}$.
This proves (1).

The map $-\id_{h^\perp}$ is an isometry that preserves every subspace of $h^\perp_\CC$.
Let $g$ be an isometry of $H^2(X,\ZZ)$ with $g(h)=h$ and $g|_{h^\perp}=-\id$.
For $x\in H^2(X,\ZZ)$ the vector $2dx-(x,h)h$ lies in $h^\perp$, so
$$
2d\,g(x)=(x,h)h-\qty{2dx-(x,h)h},
\qquad
d\,g(x)=(x,h)h-dx.
$$
Hence $(x,h)h\in d\,H^2(X,\ZZ)$, and $d$ divides $(x,h)$ because $h$ is primitive.
The lattice $H^2(X,\ZZ)$ is unimodular (@prop:k3-lattice) and $h$ is primitive, so $(x,h)=1$ for some $x$; hence $d=1$.
Conversely, if $d=1$ then $g(x)\definedas(x,h)h-x$ is the negative of the reflection $s_h$, so it is an isometry of $H^2(X,\ZZ)$; it fixes $h$, and it is $-\id$ on $h^\perp$.
It maps $H^{2,0}(X)\iscontainedin h^\perp_\CC$ to itself, so it is a Hodge isometry.
:::

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

Let $(X_t)_{t\in\PP^1}$ be a Lefschetz pencil of hyperplane sections of a smooth projective variety $Y\iscontainedin\PP^N$, let $T$ be the monodromy operator around a critical value on the primitive middle cohomology of the fibres, and let $\delta$ be the vanishing class, which is primitive [@Voi07, Corollary 2.25, Lemma 2.26].

If the fibres have odd dimension and $\delta$ is not torsion, then $T$ has infinite order [@Voi07, Corollary 3.17].
By @prop:monodromy-hodge-automorphism, $T$ is not an automorphism of the primitive Hodge structure of any fibre.

If the fibres have even dimension $2m$, the operator $T=s_\delta$ of @ex:picard-lefschetz-orientation has order $2$ and its $(-1)$-eigenspace is $\CC\delta$.
It is an automorphism of the Hodge structure $\widetilde\Phi(\tilde t)$ exactly when $\delta\in H^{m,m}$ for that Hodge structure: a one-dimensional sub-Hodge structure of weight $2m$ has type $(m,m)$, and conversely $s_\delta$ preserves each $H^{p,q}$ when $\delta\in H^{m,m}$, as in the proof of @thm:period-domain-component-stabilizer.
:::

## Global constraints on the monodromy group {#sec-global-monodromy-constraints}

In this section $B$ is a connected complex manifold that is a Zariski-open subset of a compact complex analytic space.

::: {.example #ex:quasi-projective-base title="Quasi-projective bases"}

A smooth connected quasi-projective variety $B$ is a Zariski-open subset of its closure $\overline B$ in a projective space, and $\overline B$ is a compact complex analytic space.
:::

Let $(\bL,Q,F^\bullet)$ be a polarized integral variation of Hodge structure of weight $k$ on $B$, with monodromy representation $\rho$ on $L\definedas\bL_s$, and for a field $K\in\theset{\QQ,\CC}$ write
$$
L_K^\rho\definedas\theset{v\in L_K\st\rho(\gamma)v=v\text{ for all }\gamma\in\pi_1(B,s)}
$$
for the space of invariants.

::: {.lemma #lem:flat-sections-invariants title="Flat global sections are the invariants"}

1. Evaluation at $s$ is a bijection from the set of flat global sections of $\bL\tensor\CC$ onto $L_\CC^\rho$.
2. $L_\CC^\rho=L_\QQ^\rho\tensor_\QQ\CC$.
:::

::: {.proof}

A flat global section $e$ of $\bL\tensor\CC$ is a global section of the local system $\bL\tensor_\ZZ\underline\CC_B$.
For a path $\gamma$ from $s$ to $b$, the pullback of $e$ is a section of $\gamma^{-1}\qty{\bL\tensor\underline\CC}$ over $[0,1]$, so $e(b)=\gamma^*e(s)$.
Hence $e$ is determined by $e(s)$, and $e(s)$ is fixed by the transport along every loop at $s$.
Conversely, for $v\in L_\CC^\rho$ the vector $\gamma^*v\in\bL_b\tensor\CC$ does not depend on the path $\gamma$ from $s$ to $b$, and $b\mapsto\gamma^*v$ is a global section, because on a simply connected open set on which $\bL$ is constant the transport is the identification of the stalks.
This proves (1).

For (2), choose a set $\Sigma$ of group generators of $\pi_1(B,s)$.
The space $L_\QQ^\rho$ is the kernel of the $\QQ$-linear map $L_\QQ\to\prod_{\gamma\in\Sigma}L_\QQ$ with components $\rho(\gamma)-\id$, and $L_\CC^\rho$ is the kernel of its complexification.
The functor $-\tensor_\QQ\CC$ is exact, and the intersection of the kernels of a family of linear maps on the finite-dimensional space $L_\QQ$ is the intersection of finitely many of them.
:::

::: {.theorem #thm:fixed-part title="Theorem of the fixed part"}

Let $e$ be a flat global section of $\bL\tensor\CC$.

1. The Hodge components $e^{p,q}$ of $e$ are flat global sections [@Sch73, Theorem (7.22)].
2. If $e(b)$ has type $(p,q)$ at one point $b\in B$, then it has type $(p,q)$ at every point [@Sch73, Corollary (7.23)].
:::

::: {.corollary #cor:invariants-sub-hodge-structure title="The invariants are a constant sub-Hodge structure"}

1. For every $\tilde t\in\widetilde B$, the subspace $L_\QQ^\rho\iscontainedin L_\QQ$ is a sub-Hodge structure of $\widetilde\Phi(\tilde t)$, and the induced Hodge structure on $L_\QQ^\rho$ is independent of $\tilde t$.
2. The restriction of $Q$ to $L_\QQ^\rho$ is nondegenerate, and
$$
L_\QQ=L_\QQ^\rho\perp\qty{L_\QQ^\rho}^\perp
$$
is a decomposition into $\pi_1(B,s)$-stable sub-Hodge structures of $\widetilde\Phi(\tilde t)$ for every $\tilde t$.
:::

::: {.proof}

Let $v\in L_\CC^\rho$ and let $e$ be the flat global section with $e(s)=v$.
By @thm:fixed-part (1) each $e^{p,q}$ is flat, so its pullback to $\widetilde B$ is a constant vector $v^{p,q}\in L_\CC^\rho$, and $v^{p,q}$ is the $(p,q)$-component of $v$ for the Hodge structure $\widetilde\Phi(\tilde t)$, for every $\tilde t$.
Hence $L_\CC^\rho=\bigoplus_{p+q=k}\qty{L_\CC^\rho\cap H^{p,q}_{\widetilde\Phi(\tilde t)}}$, and the summands do not depend on $\tilde t$.
This proves (1).

For (2), let $W\iscontainedin L_\QQ$ be a sub-Hodge structure of a Hodge structure $F$ polarized by $Q$, and put $W^{p,q}\definedas W_\CC\cap H^{p,q}_F$.
By @def:polarized-integral-vhs the Hermitian form $(v,w)\mapsto Q(v,\bar w)$ is definite on each $H^{p,q}_F$, and $H^{p,q}_F$ and $H^{r,s}_F$ are orthogonal for it when $(p,q)\neq(r,s)$.
It is therefore nondegenerate on $W_\CC=\bigoplus W^{p,q}$, so $Q$ is nondegenerate on $W$, and $W^\perp$ is a sub-Hodge structure with $L_\QQ=W\perp W^\perp$.
Apply this to $W=L_\QQ^\rho$; the complement is $\pi_1(B,s)$-stable because $\rho$ takes values in $\Aut(L,Q)$.
:::

::: {.theorem #thm:global-invariant-cycles title="Global invariant cycle theorem"}

Let $f\colon\mcx\to B$ be a smooth projective morphism of smooth quasi-projective varieties, let $s\in B$, and let $\overline{\mcx}$ be a smooth projective compactification of $\mcx$.

1. The space $H^k(X_s,\QQ)^\rho$ of monodromy invariants is the image of the restriction map $H^k\qty{\overline{\mcx},\QQ}\to H^k(X_s,\QQ)$ [@Voi07, Proposition 4.23, Theorem 4.24 and its proof].
2. The space $H^k(X_s,\QQ)^\rho$ is a sub-Hodge structure of $H^k(X_s,\QQ)$ [@Voi07, Proposition 3.14, Corollary 4.25].
:::

::: {.theorem #thm:monodromy-semisimple title="Deligne's semisimplicity theorem"}

The representation $\rho$ of $\pi_1(B,s)$ on $L_\CC$ is completely reducible [@Sch73, Theorem (7.25)].
:::

::: {.example #ex:unipotent-monodromy-not-global title="No unipotent global monodromy group"}

Let $T\in\Aut(L,Q)$ be unipotent with $T\neq\id$.
The cyclic group generated by $T$ is not the monodromy group of a polarized integral variation of Hodge structure on a base $B$ as above: the subspace $\ker(T-\id)\iscontainedin L_\CC$ is stable, nonzero and proper, and it has no stable complement, because $T$ would act on a complement with no fixed vector, whereas a unipotent operator on a nonzero space fixes a nonzero vector.
For fibres of odd dimension, the operator $T\neq\id$ of @ex:picard-lefschetz-not-hodge is unipotent: $\langle\delta,\delta\rangle=0$, so $(T-\id)^2=0$.
It is the monodromy operator of a variation on the punctured disc $\Delta^*$, which does not satisfy the hypothesis on $B$.
The set of regular values of the pencil does satisfy it, so by @thm:monodromy-semisimple the monodromy group of the pencil is not generated by $T$.
:::

### The Mumford--Tate group of a very general fibre {#sec-mumford-tate-monodromy}

Let $V$ be a rational vector space with a polarizable Hodge structure, and let $h\colon\CC^\times\to\GL(V_\RR)$ be the representation in which $z$ acts on $V^{p,q}$ by $z^p\bar z^q$ [@Huy16, Ch. 3, Remark 1.8].
The *Mumford--Tate group* $\MT(V)$ is the smallest algebraic subgroup of $\GL(V)$ over $\QQ$ whose group of real points contains $h(\CC^\times)$ [@Huy16, Ch. 3, §3.4].

::: {.proposition #prop:mumford-tate-sub-hodge-structures title="The Mumford--Tate group and sub-Hodge structures"}

A subspace of a tensor space $\bigoplus_iV^{\tensor n_i}\tensor(V^*)^{\tensor m_i}$ is a sub-Hodge structure exactly when $\MT(V)$ preserves it [@Huy16, Ch. 3, §3.4].
:::

For a family of polarized K3 surfaces $f\colon\mcx\to S$ over a smooth connected complex algebraic variety $S$, with monodromy representation $\rho\colon\pi_1(S,t)\to\Orth\qty{H^2(X_t,\QQ)}$, the *algebraic monodromy group* is the Zariski closure of $\rho\qty{\pi_1(S,t)}$ in $\Orth\qty{H^2(X_t,\QQ)}$ [@Huy16, Ch. 6, §4.3].

::: {.theorem #thm:mumford-tate-contains-monodromy title="The Mumford--Tate group contains the algebraic monodromy group up to finite index"}

Let $f\colon\mcx\to S$ be a family of polarized K3 surfaces over a smooth connected complex algebraic variety.
There is a countable union $S'\subsetneq S$ of proper closed subvarieties such that for $t\in S\sm S'$ the group $\MT\qty{H^2(X_t,\QQ)}$ is constant and contains a subgroup of finite index of the algebraic monodromy group; it contains the identity component of the algebraic monodromy group [@Huy16, Ch. 6, Theorem 4.9].
:::

::: {.corollary #cor:finite-index-monodromy-hodge-tensors title="Monodromy at a very general fibre of a family of polarized K3 surfaces"}

In @thm:mumford-tate-contains-monodromy let $t\in S\sm S'$, put $V\definedas H^2(X_t,\QQ)$ and $\Gamma\definedas\rho\qty{\pi_1(S,t)}$, and let
$$
\Gamma'\definedas\Gamma\cap\MT(V)(\QQ).
$$

1. The subgroup $\Gamma'$ has finite index in $\Gamma$.
2. Every element of $\Gamma'$ preserves every sub-Hodge structure of every tensor space $\bigoplus_iV^{\tensor n_i}\tensor(V^*)^{\tensor m_i}$.
3. The set of $g\in\Gamma$ with $g_\CC H^{2,0}(X_t)=H^{2,0}(X_t)$ is a finite subgroup of $\Gamma$; it contains no element of infinite order.
:::

::: {.proof}

Let $M$ be the algebraic monodromy group and let $H\iscontainedin M\cap\MT(V)$ be an algebraic subgroup of finite index in $M$, which exists by @thm:mumford-tate-contains-monodromy.
The map $\Gamma/\qty{\Gamma\cap H(\QQ)}\to M(\overline\QQ)/H(\overline\QQ)$ is injective and its target is finite, so $\Gamma\cap H(\QQ)$ has finite index in $\Gamma$; it is contained in $\Gamma'$.
This proves (1), and (2) is @prop:mumford-tate-sub-hodge-structures.

For (3), let $h\in H^2(X_t,\ZZ)$ be the class of the polarization.
It is the value of a flat section, so every $g\in\Gamma$ is an isometry of $H^2(X_t,\ZZ)$ with $g(h)=h$, and $g$ is determined by its restriction to $h^\perp$.
An isometry $g$ of $H^2(X_t,\ZZ)$ with $g_\CC H^{2,0}(X_t)=H^{2,0}(X_t)$ preserves $H^{0,2}(X_t)=\overline{H^{2,0}(X_t)}$ and $H^{1,1}(X_t)=\qty{H^{2,0}(X_t)\oplus H^{0,2}(X_t)}^\perp$.
The restrictions to $h^\perp$ of the elements $g$ in (3) therefore lie in the group $G_\ZZ\cap V_F$ for the polarized Hodge structure $F$ on $h^\perp$, which is finite by @prop:monodromy-hodge-automorphism (1).
:::
