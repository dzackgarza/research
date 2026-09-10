# Hyperbolic forms and Witt classes {#sec-hyperbolic-witt}

Fix a commutative ring $R$ and take the value module $W=R$, so that the form category of @def-form-categories is $\mathcal B_{R,R}$ and its objects are pairs $(M,b)$ with $b\colon M\times M\to R$ bilinear.
Lattices, unimodularity, dual lattices, and discriminant modules are those of @sec-lattices-discriminant.

## The hyperbolic form on a module and its dual {#sec-hyperbolic-form}

::: {#def-hyperbolic-form}
## Hyperbolic forms

Let $M$ be an $R$-module and write $M^{*}=\operatorname{Hom}_R(M,R)$.
The *hyperbolic form* on $M\oplus M^{*}$ is
$$
h_M\bigl((x,\varphi),(y,\psi)\bigr)=\psi(x)+\varphi(y).
$$
It is $R$-bilinear and symmetric, and
$$
H(M):=(M\oplus M^{*},h_M)
$$
is an object of $\mathcal B_{R,R}$.
:::

::: {#prp-hyperbolic-adjoint}
## The adjoint map of a hyperbolic form

Let $\operatorname{can}_M\colon M\to M^{**}$ be the evaluation map, $\operatorname{can}_M(x)(\psi)=\psi(x)$.
Under the canonical isomorphism $(M\oplus M^{*})^{*}\cong M^{*}\oplus M^{**}$, the adjoint map of @def-polarization is
$$
h_M^{\sharp}\colon M\oplus M^{*}\longrightarrow M^{*}\oplus M^{**},
\qquad
h_M^{\sharp}(x,\varphi)=\bigl(\varphi,\operatorname{can}_M(x)\bigr).
$$
Hence $h_M$ is nondegenerate if and only if $\operatorname{can}_M$ is injective, and perfect if and only if $\operatorname{can}_M$ is an isomorphism.
:::

Restricting the functional $h_M^{\sharp}(x,\varphi)$ to $M\oplus0$ gives $y\mapsto\varphi(y)$, and restricting it to $0\oplus M^{*}$ gives $\psi\mapsto\psi(x)$, which is the value of $\operatorname{can}_M(x)$.
The two components of $h_M^{\sharp}$ are therefore $\varphi$ and $\operatorname{can}_M(x)$, and the first component is an isomorphism onto $M^{*}$.

For a finitely generated projective $R$-module $M$ the map $\operatorname{can}_M$ is an isomorphism.
Indeed $\operatorname{can}_{R^{n}}$ is an isomorphism, and $\operatorname{can}_{M\oplus M'}=\operatorname{can}_M\oplus\operatorname{can}_{M'}$, so both summands of a decomposition $M\oplus M'\cong R^{n}$ have $\operatorname{can}$ an isomorphism.

::: {#prp-hyperbolic-lattice}
## Hyperbolic lattices

Let $R$ be a Dedekind domain and let $M$ be a finitely generated projective $R$-module.
Then $H(M)$ is a unimodular $R$-lattice in the sense of @def-lattice and @def-unimodular, and its discriminant module (@def-discriminant) is $A_{H(M)}=0$.
:::

::: {#exm-hyperbolic-plane}
## The hyperbolic plane

Take $M=R$ and the basis $e=(1,0)$, $f=(0,\operatorname{id}_R)$ of $R\oplus R^{*}$.
Then
$$
h_R(e,e)=0,\qquad h_R(f,f)=0,\qquad h_R(e,f)=1,
$$
so $H(R)$ has Gram matrix
$$
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
For $R=\mathbb Z$ the lattice $H(\mathbb Z)$ is even (@def-even-lattice), unimodular, and of signature $(1,1)$.
:::

::: {#def-hyperbolic-functor}
## The hyperbolic functor

For an isomorphism $u\colon M\to N$ of $R$-modules set
$$
H(u)(x,\varphi)=\bigl(u(x),\varphi\circ u^{-1}\bigr).
$$
Then
$$
h_N\bigl(H(u)(x,\varphi),H(u)(y,\psi)\bigr)
=\bigl(\psi\circ u^{-1}\bigr)\bigl(u(x)\bigr)+\bigl(\varphi\circ u^{-1}\bigr)\bigl(u(y)\bigr)
=\psi(x)+\varphi(y),
$$
so $H(u)$ is an isometry $H(M)\to H(N)$.
The assignment defines a functor
$$
H\colon(R\text{-}\mathbf{Mod})^{\simeq}\longrightarrow(\mathcal B_{R,R})^{\simeq}
$$
between the cores of @def-core.
:::

::: {#def-lagrangian}
## Lagrangians and metabolic forms

Let $(M,b)$ be an object of $\mathcal B_{R,R}$ and let $N\subseteq M$ be a submodule.
Write
$$
N^{\perp}=\{x\in M\mid b(x,y)=0\text{ for all }y\in N\}.
$$
A *lagrangian* of $(M,b)$ is a direct summand $N\subseteq M$ with $N=N^{\perp}$.
The form $(M,b)$ is *metabolic* if it admits a lagrangian [@MH73, §I.6; @Ran98, Def. 20.1].

**Remark.** [@MH73] writes *split* for this condition and attributes the term *metabolic* to Knebusch.
:::

::: {#prp-hyperbolic-metabolic}
## Hyperbolic forms are metabolic

Let $M$ be an $R$-module for which $\operatorname{can}_M$ is injective.
Then $0\oplus M^{*}$ is a lagrangian of $H(M)$.
:::

The submodule $0\oplus M^{*}$ is a direct summand of $M\oplus M^{*}$, and
$$
h_M\bigl((x,\varphi),(0,\psi)\bigr)=\psi(x),
$$
so $(0\oplus M^{*})^{\perp}$ consists of the pairs $(x,\varphi)$ with $\psi(x)=0$ for every $\psi\in M^{*}$, that is, with $\operatorname{can}_M(x)=0$.
Injectivity of $\operatorname{can}_M$ gives $x=0$, so $(0\oplus M^{*})^{\perp}=0\oplus M^{*}$.

## Hyperbolic stabilization {#sec-hyperbolic-stabilization}

::: {#def-hyperbolic-stabilization}
## Orthogonal sum with a fixed object

With the orthogonal sum of @def-orthogonal-sum, an object $M$ of $\mathcal B_{R,R}$ defines
$$
F_M\colon\mathcal B_{R,R}\longrightarrow\mathcal B_{R,R},
\qquad
F_M(X)=X\perp M,
\qquad
F_M(f)=f\oplus\operatorname{id}_{M},
$$
together with the inclusion of the first summand
$$
\iota^{M}_{X}\colon X\longrightarrow F_M(X),
$$
a morphism of $\mathcal B_{R,R}$ natural in $X$.
The *hyperbolic stabilization* is
$$
S:=F_{H(R)} .
$$
For $R$ a Dedekind domain and $M$ an $R$-lattice, $F_M$ restricts to an endofunctor of $\mathbf{Lat}_R$.
:::

Since $b_{L\perp L'}^{\sharp}$ is identified with $b_L^{\sharp}\oplus b_{L'}^{\sharp}$ under $(L\oplus L')^{*}\cong L^{*}\oplus L'^{*}$, an orthogonal sum of nondegenerate forms is nondegenerate and an orthogonal sum of unimodular forms is unimodular.

::: {#prp-stabilization-discriminant}
## Stabilization preserves the discriminant

Let $R$ be a Dedekind domain with fraction field $K$, and let $L$ be an $R$-lattice.
The canonical isomorphism $(L\oplus H(R))^{*}\cong L^{*}\oplus H(R)^{*}$ identifies
$$
b_{S(L)}^{\sharp}=b_L^{\sharp}\oplus h_R^{\sharp},
$$
and $h_R^{\sharp}$ is an isomorphism by @prp-hyperbolic-lattice.
Taking cokernels in @def-two-witnesses gives
$$
A_{S(L)}\;\cong\;A_L .
$$
Concretely, $H(R)^{\#}=H(R)$ inside $H(R)\otimes_RK$, so
$$
S(L)^{\#}=L^{\#}\oplus H(R),
\qquad
S(L)^{\#}/S(L)=L^{\#}/L,
$$
and the mixed terms of the form on an orthogonal sum vanish, so the isomorphism respects the $K/R$-valued forms of @def-discriminant.
For $R=\mathbb Z$ it is an isomorphism in $\mathbf{DiscBil}_{\mathbb Z}$ (@def-discbil), and for $L$ even it is an isomorphism in $\mathbf{DiscQuad}_{\mathbb Z}$ (@def-discquad).
:::

::: {#thm-stabilization-not-unimodular}
## The discriminant along the stabilization tower

Let $R$ be a Dedekind domain and let $L$ be an $R$-lattice with $A_L\neq0$.
Then $A_{S^{n}(L)}\cong A_L$ for every $n\geq0$.
Consequently $S^{n}(L)$ is not unimodular, and $S^{n}(L)$ is not isometric to $H(P)$ for any finitely generated projective $R$-module $P$ and any $n\geq0$.
:::

Iterating @prp-stabilization-discriminant gives the isomorphism.
A unimodular lattice has vanishing discriminant module by @def-unimodular and @def-two-witnesses, and $H(P)$ is unimodular by @prp-hyperbolic-lattice.
The discriminant module is an invariant of the isomorphism class, by the functors on cores recorded in @sec-lattices-discriminant.

::: {#exm-stabilizing-rank-one}
## Stabilizing a rank-one lattice

Let $R=\mathbb Z$ and let $L=\mathbb Ze$ with $b(e,e)=2$.
Then $b^{\sharp}\colon\mathbb Z\to\mathbb Z^{*}\cong\mathbb Z$ is multiplication by $2$, so $A_L\cong\mathbb Z/2\mathbb Z$, generated by the class of $e/2\in L^{\#}$, with
$$
\bar b_L\bigl(\overline{e/2},\overline{e/2}\bigr)=\tfrac12+\mathbb Z .
$$
The lattice $L$ is even, and $q_L(\overline{e/2})=\tfrac12+2\mathbb Z$.
By @thm-stabilization-not-unimodular, $A_{S^{n}(L)}\cong\mathbb Z/2\mathbb Z$ for every $n\geq0$.
:::

## Witt classes {#sec-witt-classes}

::: {#exm-rank-one-forms}
## Rank-one forms

For $a\in R$ write $\langle a\rangle$ for the object $(R,b_a)$ of $\mathcal B_{R,R}$ with $b_a(x,y)=axy$.
Under the isomorphism $R^{*}\cong R$, $f\mapsto f(1)$, the adjoint map of @def-polarization is multiplication by $a$.
So $\langle a\rangle$ is nondegenerate exactly when $a$ is not a zero divisor, and unimodular exactly when $a$ is a unit.
In particular $\langle1\rangle$ is unimodular over every commutative ring.
Over $R=\mathbb Z/4\mathbb Z$ the form $\langle2\rangle$ has $\ker b_2^{\sharp}=2\mathbb Z/4\mathbb Z$, so it is degenerate.
:::

::: {#def-witt-class}
## Witt equivalence

Let $R$ be a Dedekind domain.
Two unimodular $R$-lattices $X$ and $X'$ have the same *Witt class*, written $X\sim X'$, if there are metabolic unimodular $R$-lattices $Y$ and $Y'$ with
$$
X\perp Y\;\cong\;X'\perp Y'
$$
[@MH73, Def. I.7.1].
This is an equivalence relation, and it is compatible with orthogonal sum and with tensor product [@MH73, Lem. I.7.2].
:::

::: {#thm-witt-ring}
## The Witt ring

The set $W(R)$ of Witt classes of unimodular $R$-lattices is a commutative ring with $1$, with orthogonal sum as addition and tensor product as multiplication [@MH73, Thm. I.7.3].
:::

::: {#prp-metabolic-witt-trivial}
## Metabolic lattices have Witt class zero

Let $X$ be a metabolic unimodular $R$-lattice.
Then $[X]=0$ in $W(R)$.
In particular $[H(P)]=0$ for every finitely generated projective $R$-module $P$.
:::

The zero lattice is metabolic, with lagrangian $0$.
Taking $Y=0$ and $Y'=X$ in @def-witt-class, the isometry $X\perp0\cong0\perp X$ gives $X\sim0$.
The hyperbolic lattices are metabolic by @prp-hyperbolic-metabolic.

::: {#thm-witt-shift-by-summand}
## Which summand shifts the Witt class

Let $M$ be a unimodular $R$-lattice.
On unimodular lattices, $F_M$ of @def-hyperbolic-stabilization acts on Witt classes by
$$
\bigl[F_M(X)\bigr]=[X]+[M],
$$
so it induces translation by $[M]$ on $W(R)$.
This translation is the identity if and only if $[M]=0$.
For $M=H(R)$ it is the identity, so the Witt class is constant along
$$
L\xrightarrow{\ \iota_L\ }S(L)\xrightarrow{\ \iota_{S(L)}\ }S^{2}(L)\longrightarrow\cdots.
$$
:::

The displayed identity is the compatibility of Witt equivalence with orthogonal sum (@def-witt-class), and the last statement combines it with @prp-metabolic-witt-trivial.

::: {#thm-witt-group-of-z}
## The Witt ring of $\mathbb Z$

The signature is a ring isomorphism
$$
\sigma\colon W(\mathbb Z)\xrightarrow{\ \sim\ }\mathbb Z,
\qquad
\sigma\bigl[\langle1\rangle\bigr]=1,
$$
with $\langle1\rangle$ as in @exm-rank-one-forms [@MH73, Ch. II §4].
:::

::: {#exm-witt-classes-over-z}
## Witt classes over $\mathbb Z$

By @thm-witt-group-of-z the class $[\langle1\rangle]$ has infinite order in $W(\mathbb Z)$, and $\sigma[\langle-1\rangle]=-1$, so $[\langle-1\rangle]=-[\langle1\rangle]$.
The lattice $H(\mathbb Z)$ has signature $(1,1)$, so $\sigma[H(\mathbb Z)]=0$, in agreement with @prp-metabolic-witt-trivial.
By @thm-witt-shift-by-summand, $F_{\langle1\rangle}$ translates $W(\mathbb Z)$ by $1$ and $F_{H(\mathbb Z)}$ acts as the identity.
:::

::: {#thm-metabolic-is-hyperbolic}
## Metabolic forms when $2$ is a unit

Let $R$ be a ring over which every finitely generated projective module is free and in which $2$ is a unit.
Then every metabolic unimodular form over $R$ is isometric to an orthogonal sum of copies of $H(R)$ [@MH73, Lem. I.6.3].
Conversely such an orthogonal sum is metabolic over any $R$, by @prp-hyperbolic-metabolic and the closure of metabolic forms under orthogonal sum [@MH73, Lem. I.6.2].
:::

::: {#exm-metabolic-over-z}
## A metabolic lattice over $\mathbb Z$

Let $X=\langle1\rangle\perp\langle-1\rangle=\mathbb Ze_1\oplus\mathbb Ze_2$, so that
$$
b(e_1,e_1)=1,\qquad b(e_2,e_2)=-1,\qquad b(e_1,e_2)=0 .
$$
The submodule $N=\mathbb Z(e_1+e_2)$ is a direct summand, and $b(ae_1+be_2,e_1+e_2)=a-b$, so $N^{\perp}=N$ and $X$ is metabolic.
Both $X$ and $H(\mathbb Z)$ are unimodular of signature $(1,1)$.
Since $b(e_1,e_1)=1$, the lattice $X$ is odd, while $H(\mathbb Z)$ is even, so $X$ and $H(\mathbb Z)$ are not isometric.
In $\mathbb Z$ the element $2$ is not a unit, and the hypothesis of @thm-metabolic-is-hyperbolic fails.
:::

The Witt group of nonsingular $\epsilon$-symmetric forms over a ring with involution is the zero-dimensional $L$-group of that ring, and a form admitting a lagrangian is zero in it [@Ran98, Ex. 20.11].
The homological setting in which the $L$-groups of every dimension are defined is @sec-stable-duality.
