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
For $s\in B$, the *monodromy representation*
$$
\rho\colon\pi_1(B,s)\too\Aut(\bL_s)
$$
of $\bL$ sends the class of a loop $\gamma$ based at $s$ to $\gamma^*$ [@Voi07, Corollary 3.10, Definition 3.13].
It is a group morphism for the product on $\pi_1(B,s)$ in which $\gamma\delta$ is the loop $\delta$ followed by the loop $\gamma$, since transport along a concatenation is the composite of the transports.

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

Condition (1) says that the monodromy group lies in $\Orth^+(\bL_s)$ (@prop:orientation-characters-reflections).

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
The pullback $\pi^{-1}\bL$ is constant, and $\tilde s$ determines an isomorphism of it with the constant sheaf of stalk $\bL_s$ [@Voi07, proof of Corollary 3.10].
Under this isomorphism the pullback of $F^\bullet$ is a map
$$
\widetilde\Phi\colon\widetilde B\too D
$$
that satisfies $\widetilde\Phi(\tilde s)=F^\bullet_s$ and
$$
\widetilde\Phi(\gamma\tilde t)=\rho(\gamma)\,\widetilde\Phi(\tilde t)
\qquad\text{for }\tilde t\in\widetilde B,\ \gamma\in\pi_1(B,s)
$$ {#eq-period-map-equivariance}
[@Sch73, (3.24)], where $\pi_1(B,s)$ acts on $\widetilde B$ by the deck transformations used in the proof of @prop:local-system-of-lattices-monodromy (3).
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

For weight $2$ the sign is $\epsilon=+1$, and $W^{\mathrm{odd}}_F=\qty{H^{2,0}\oplus H^{0,2}}\cap L_\RR$ is the positive-definite real subspace of dimension $2h^{2,0}$ spanned by the real and imaginary parts of the vectors of $H^{2,0}$.
The primitive local system of a family of polarized K3 surfaces has $h^{1,1}>0$, and the first row of the table is @prop:polarized-k3-monodromy-positive.

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

Statement (1) covers every weight-$2$ period domain with $h^{1,1}>0$, for every value of $h^{2,0}$.

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

By @lem:k3-orientation-character, @cor:middle-cohomology-monodromy (2) proves the conclusion of @prop:k3-monodromy-positive for the families of K3 surfaces that admit a class $\omega$.

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

## Monodromy and automorphisms of Hodge structures {#sec-monodromy-hodge-automorphisms}

Let $(\bL,Q,F^\bullet)$, $s$, $D$ and $\widetilde\Phi$ be as in @sec-period-domain-components.
For $F\in D$, an *automorphism of the polarized Hodge structure* $F$ is an element $g\in G_\ZZ$ with $gF^p=F^p$ for all $p$; these form the group $G_\ZZ\cap V_F$.
For the primitive Hodge structure on $h^\perp\iscontainedin H^2(X,\ZZ)$ of a K3 surface $X$ with an ample class $h$, these are the restrictions to $h^\perp$ of the Hodge isometries of $H^2(X,\ZZ)$ (@sec-k3-automorphisms) that fix $h$.

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

@cor:vhs-monodromy-stabilizes-component and @prop:monodromy-hodge-automorphism hold on every connected complex manifold $B$.
The results of this section need a hypothesis on $B$: it is a Zariski-open subset of a compact complex analytic space.
A smooth connected quasi-projective variety satisfies it.

Let $(\bL,Q,F^\bullet)$ be a polarized integral variation of Hodge structure of weight $k$ on such a $B$, with monodromy representation $\rho$ on $L\definedas\bL_s$, and write
$$
L_\QQ^\rho\definedas\theset{v\in L_\QQ\st\rho(\gamma)v=v\text{ for all }\gamma\in\pi_1(B,s)}
$$
for the space of invariants.
Evaluation at $s$ identifies the flat global sections of $\bL\tensor\CC$ with $L_\CC^\rho=L_\QQ^\rho\tensor\CC$.

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

For the cohomology of the fibres of a smooth projective morphism $f\colon\mcx\to B$ of smooth quasi-projective varieties, @cor:invariants-sub-hodge-structure (1) is [@Voi07, Proposition 3.14, Corollary 4.25], and the invariants are the image of the restriction map $H^k\qty{\overline{\mcx},\QQ}\to H^k(X_s,\QQ)$ for every smooth projective compactification $\overline{\mcx}$ of $\mcx$ [@Voi07, Proposition 4.23, Theorem 4.24].

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
A subspace of a tensor space $\bigoplus_iV^{\tensor n_i}\tensor(V^*)^{\tensor m_i}$ is a sub-Hodge structure exactly when $\MT(V)$ preserves it [@Huy16, Ch. 3, §3.4].

For a family of polarized K3 surfaces $f\colon\mcx\to S$ over a smooth connected complex algebraic variety $S$, with monodromy representation $\rho\colon\pi_1(S,t)\to\Orth\qty{H^2(X_t,\QQ)}$, the *algebraic monodromy group* is the Zariski closure of $\rho\qty{\pi_1(S,t)}$ in $\Orth\qty{H^2(X_t,\QQ)}$ [@Huy16, Ch. 6, §4.3].

::: {.theorem #thm:mumford-tate-contains-monodromy title="The Mumford--Tate group contains the algebraic monodromy group up to finite index"}

Let $f\colon\mcx\to S$ be a family of polarized K3 surfaces over a smooth connected complex algebraic variety.
There is a countable union $S'\subsetneq S$ of proper closed subvarieties such that for $t\in S\sm S'$ the group $\MT\qty{H^2(X_t,\QQ)}$ is constant and contains a subgroup of finite index of the algebraic monodromy group; it contains the identity component of the algebraic monodromy group [@Huy16, Ch. 6, Theorem 4.9].
:::

@prop:monodromy-hodge-automorphism bounds the monodromy operators that preserve the Hodge structure of one fibre: they form a finite group.
@thm:mumford-tate-contains-monodromy is the statement in the other direction: at a very general point $t$, a subgroup of finite index of the monodromy group preserves every sub-Hodge structure of every tensor space of $H^2(X_t,\QQ)$, although its elements of infinite order do not preserve the Hodge structure of $H^2(X_t,\QQ)$ itself.
