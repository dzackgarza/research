# Chain complexes, forms, and derived functors {#sec-chain-complexes}

Let $\mca$ be an additive category, let $R$ be a commutative ring, and let $W$ be an $R$-module.
Chain complexes in $\mca$, chain maps, and the additive category $\mathbf{Ch}(\mca)$ are @def:chain-complexes; abelian categories are @def:abelian-category.
Write $d^C_n\colon C_n\to C_{n-1}$ for the differentials of $C$.

## The category of chain complexes {#sec-chain-complex-category}

The object $C_n$ is the domain of $d^C_n$ and the codomain of $d^C_{n+1}$, so the differentials determine the objects.
A chain complex is therefore the same datum as a family of morphisms $(d_n)_{n\in\bZ}$ of $\mca$ in which the codomain of $d_{n+1}$ is the domain of $d_n$ and every composite $d_nd_{n+1}$ vanishes.

An additive functor $F\colon\mca\to\mathcal B$ induces $\mathbf{Ch}(F)\colon\mathbf{Ch}(\mca)\to\mathbf{Ch}(\mathcal B)$ with $\mathbf{Ch}(F)(C)_n=F(C_n)$ and differentials $F(d^C_n)$, and this assignment respects composition of additive functors.

::: {.theorem #thm:chain-complexes-abelian title="Complexes over an abelian category"}

If $\mca$ is abelian, then $\mathbf{Ch}(\mca)$ is abelian. A sequence
$$
0\to A\to B\to C\to0
$$
in $\mathbf{Ch}(\mca)$ is exact if and only if, for every $n$, the sequence
$$
0\to A_n\to B_n\to C_n\to0
$$
is exact in $\mca$ [@Wei94, Thm. 1.2.3, Ex. 1.2.4].
:::

::: {.proof}

This is [@Wei94, Thm. 1.2.3 and Ex. 1.2.4].
The reason it transfers is that every construction involved is degreewise: kernels and cokernels of a chain map are taken in each degree with the restricted differentials, which are well defined because $f$ intertwines them, and $\operatorname{Coim}\to\operatorname{Im}$ is degreewise the isomorphism of the abelian base and hence, by the degreewise criterion for a chain map to be an isomorphism, one of complexes.
Since kernels and cokernels are degreewise, monic, epic and exactness are checked in each degree, which is the second assertion.
:::

## Homology and exactness {#sec-homology-and-exactness}

Assume $\mca$ abelian for the remainder of the chapter.

::: {.definition #def:homology title="Cycles, boundaries, and homology"}

The *$n$-cycles* and *$n$-boundaries* of $C\in\mathbf{Ch}(\mca)$ are
$$
Z_n(C)=\ker d^C_n,
\qquad
B_n(C)=\im d^C_{n+1},
$$
and $d^C_nd^C_{n+1}=0$ gives $B_n(C)\iscontainedin Z_n(C)\iscontainedin C_n$.
The homology functor of @def:chain-complexes takes the value
$$
H_n(C)=Z_n(C)/B_n(C)
$$
[@Wei94, Def. 1.1.1]; a chain map sends cycles to cycles and boundaries to boundaries, which is what makes $H_n$ a functor [@Wei94, Ex. 1.1.2].
:::

::: {.definition #def:exact-complex title="Exactness"}

A complex $C$ is *exact at $n$* if $H_n(C)=0$, and *exact* if it is exact at every degree.
Exactness at $n$ and exactness are isomorphism-invariant properties of objects of $\mathbf{Ch}(\mca)$ and therefore define replete full subcategories (@def:subcategory), the second being the intersection over $n\in\bZ$ of the first.

A short exact sequence
$$
0\to A\xrightarrow{\,i\,}B\xrightarrow{\,p\,}C\to0
$$
is the complex concentrated in degrees $2,1,0$ with $d_2=i$ and $d_1=p$, together with the assertion that this complex is exact: exactness at $2$ says $i$ is monic, exactness at $1$ says $\im i$ and $\ker p$ are the same subobject of $B$, and exactness at $0$ says $p$ is epic.
:::

::: {.definition #def:quasi-isomorphism title="Quasi-isomorphisms"}

A chain map $u\colon C\to D$ is a *quasi-isomorphism* if $H_n(u)$ is an isomorphism for every $n$ [@Wei94, Def. 1.1.2].
These are the weak equivalences of the model structure of @thm:projective-model-structure.
:::

::: {.theorem #thm:homology-les title="The long exact homology sequence"}

Let
$$
0\to A\xrightarrow{\,f\,}B\xrightarrow{\,g\,}C\to0
$$
be a short exact sequence in $\mathbf{Ch}(\mca)$.
There are natural connecting morphisms $\del\colon H_n(C)\to H_{n-1}(A)$ for which
$$
\cdots\too H_n(A)\xrightarrow{\,H_n(f)\,}H_n(B)\xrightarrow{\,H_n(g)\,}H_n(C)
\xrightarrow{\ \del\ }H_{n-1}(A)\too\cdots
$$
is exact [@Wei94, Thm. 1.3.1].
:::

::: {.proof}

This is [@Wei94, Thm. 1.3.1], and the proof is the snake lemma applied to
```tikzcd
A_n/B_n(A) \arrow[r] \arrow[d, "d^A"] &
B_n/B_n(B) \arrow[r] \arrow[d, "d^B"] &
C_n/B_n(C) \arrow[r] \arrow[d, "d^C"] & 0 \\
Z_{n-1}(A) \arrow[r] &
Z_{n-1}(B) \arrow[r] &
Z_{n-1}(C) & {}
```
whose rows are exact by @thm:chain-complexes-abelian and whose two ends the snake lemma of @thm:diagram-lemmas identifies as $H_n(C)$ and $H_{n-1}(A)$.
Applying it to the translate $[n]$ gives the sequence in every degree at once, and naturality is functoriality of the snake lemma.
:::

## Translation, truncation, and the mapping cone {#sec-translation-cone}

::: {.definition #def:translation title="Translation"}

For $p\in\bZ$ the *$p$th translate* $C[p]$ of $C$ has $C[p]_n=C_{n+p}$ with differential $(-1)^pd^C$.
Setting $f[p]_n=f_{n+p}$ on chain maps makes $[p]$ an isomorphism of categories $\mathbf{Ch}(\mca)\to\mathbf{Ch}(\mca)$ with inverse $[-p]$, and
$$
H_n(C[p])=H_{n+p}(C)
$$
[@Wei94, 1.2.8].
:::

::: {.definition #def:good-truncation title="Good truncation"}

For $n\in\bZ$ let $\tau_{\ge n}C$ be the subcomplex of $C$ with
$$
(\tau_{\ge n}C)_i=
\begin{cases}
0,& i<n,\\
Z_n(C),& i=n,\\
C_i,& i>n,
\end{cases}
$$
and let $\tau_{<n}C=C/\tau_{\ge n}C$.
Then $H_i(\tau_{\ge n}C)=H_i(C)$ for $i\ge n$ and vanishes for $i<n$, while $H_i(\tau_{<n}C)=H_i(C)$ for $i<n$ and vanishes for $i\ge n$ [@Wei94, 1.2.7].
:::

::: {.definition #def:mapping-cone title="The mapping cone"}

Let $f\colon B\to C$ be a chain map.
The *mapping cone* of $f$ is the complex with
$$
\cone(f)_n=B_{n-1}\oplus C_n,
\qquad
d(b,c)=\bigl(-d^Bb,\;d^Cc-f(b)\bigr)
$$
[@Wei94, 1.5.1].
The inclusion of $C$ and the projection onto $B[-1]$ form a short exact sequence
$$
0\too C\too\cone(f)\too B[-1]\too0,
$$
and $f$ is a quasi-isomorphism if and only if $\cone(f)$ is exact [@Wei94, Cor. 1.5.4].
:::

## Forms on a chain complex {#sec-complex-forms}

Work in $\mathbf{Ch}(R\text{-}\mathbf{Mod})$.
A $W$-valued bilinear form on an $R$-module $M$ is an element of $\Hom_R(M\tensor_RM,W)$ (@def:module-bilinear-form), and the form categories $\mathcal B_{R,W}$ of @def:form-categories are the categories of elements of the presheaves so obtained.

::: {.definition #def:complex-tensor-product title="The tensor product of complexes"}

For $C,D\in\mathbf{Ch}(R\text{-}\mathbf{Mod})$ the *tensor product complex* $C\tensor_RD$ has
$$
(C\tensor_RD)_n=\bigoplus_{p+q=n}C_p\tensor_RD_q,
\qquad
d(x\tensor_R y)=d^Cx\tensor_R y+(-1)^p\,x\tensor_R d^Dy
$$
for $x\in C_p$ and $y\in D_q$ [@Wei94, 2.7.1, Thm. 3.6.3].

The transposition
$$
\tau\colon C\tensor_RD\too D\tensor_RC,
\qquad
\tau(x\tensor_R y)=(-1)^{pq}\,y\tensor_R x,
$$
commutes with the two differentials and is an isomorphism of complexes; it is the symmetry of @def:braided-symmetric for this tensor product.
:::

::: {.definition #def:value-complex title="Value complexes"}

For $n\in\bZ$ write $W[n]$ for the complex with $W$ in degree $n$, the zero module in every other degree, and zero differentials.
:::

::: {.definition #def:complex-form title="Bilinear forms on a complex"}

Let $C\in\mathbf{Ch}(R\text{-}\mathbf{Mod})$.
A *$W$-valued bilinear form of degree $n$ on $C$* is a chain map
$$
\beta\colon C\tensor_RC\too W[n].
$$

Since $W[n]$ vanishes outside degree $n$, such a chain map is one $R$-linear map
$$
\beta_n\colon\bigoplus_{p+q=n}C_p\tensor_RC_q\too W,
$$
equivalently a family of $R$-bilinear maps $\beta_{p,q}\colon C_p\times C_q\to W$ indexed by the pairs with $p+q=n$.
The differentials of $W[n]$ are zero, so the condition that $\beta$ be a chain map is $\beta_n\circ d_{n+1}=0$, which reads
$$
\beta_{p-1,q}(d^Cx,y)+(-1)^p\beta_{p,q-1}(x,d^Cy)=0
\qquad(x\in C_p,\ y\in C_q,\ p+q=n+1).
$$
This is the compatibility of the form with the differential.

The form is *symmetric* if $\beta\circ\tau=\beta$, that is if
$$
\beta_{q,p}(y,x)=(-1)^{pq}\beta_{p,q}(x,y)
\qquad(x\in C_p,\ y\in C_q,\ p+q=n).
$$
:::

::: {.proposition #prop:complex-form-adjoint title="The adjoint chain map and the $n$-dual"}

Let $W=R$ with the identity involution, and let $C^{n-*}$ be the $n$-dual complex of @def:n-dual-complex, so that $(C^{n-*})_r=\Hom_R(C_{n-r},R)$ with differential $(-1)^r(d^C)^{*}$.
For a bilinear form $\beta$ of degree $n$ on $C$ set
$$
\beta^{\sharp}_r\colon C_r\too(C^{n-*})_r,
\qquad
\beta^{\sharp}_r(x)=(-1)^{r}\,\beta_{r,n-r}(x,-).
$$
Then $\beta\mapsto\beta^{\sharp}$ is a bijection from the bilinear forms of degree $n$ on $C$ to the chain maps $C\to C^{n-*}$.

The condition that $\beta^{\sharp}$ be a chain equivalence is the Poincaré condition of @def:poincare-complex.
:::

::: {.proof}

For each $r$, an $R$-bilinear map $C_r\times C_{n-r}\to R$ is the same as an $R$-linear map $C_r\to\Hom_R(C_{n-r},R)$, by the universal property of the hom module, and the sign $(-1)^r$ is a bijection of each such set with itself, so the two families correspond.

It remains to match the two conditions.
For $x\in C_r$ and $y\in C_{n-r+1}$,
$$
\beta^{\sharp}_{r-1}(d^Cx)(y)=(-1)^{r-1}\beta_{r-1,n-r+1}(d^Cx,y),
\qquad
\bigl((-1)^r(d^C)^{*}\beta^{\sharp}_r(x)\bigr)(y)=(-1)^{2r}\beta_{r,n-r}(x,d^Cy),
$$
the second because the differential of the $n$-dual is $(-1)^r(d^C)^{*}$ by @def:n-dual-complex, and because $(-1)^r\beta^\sharp_r(x)$ evaluates at $y$ as $(-1)^r$ times $\beta^{\sharp}_r(x)(d^Cy)=(-1)^r\beta_{r,n-r}(x,d^Cy)$.
So $\beta^{\sharp}$ commutes with the differentials exactly when
$$
(-1)^{r-1}\beta_{r-1,n-r+1}(d^Cx,y)=(-1)^{2r}\beta_{r,n-r}(x,d^Cy),
$$
that is, multiplying by $(-1)^{r-1}$, exactly when $\beta_{r-1,n-r+1}(d^Cx,y)+(-1)^{r}\beta_{r,n-r}(x,d^Cy)=0$ for all $r$, which is the condition of @def:complex-form with $p=r$ and $q=n+1-r$.

A chain map $\beta^{\sharp}$ is a chain equivalence exactly when it is a quasi-isomorphism, and under the bijection that is the condition of @def:poincare-complex.
:::

::: {.proposition #prop:form-on-homology title="The induced pairing on homology"}

Let $\beta$ be a $W$-valued bilinear form of degree $n$ on $C$ and let $p+q=n$.
The assignment
$$
\bar\beta_{p,q}\bigl([x],[y]\bigr)=\beta_{p,q}(x,y)
\qquad(x\in Z_p(C),\ y\in Z_q(C))
$$
is a well-defined $R$-bilinear map $H_p(C)\times H_q(C)\to W$.
If $\beta_n=\gamma\circ d_{n+1}$ for some $R$-linear $\gamma\colon(C\tensor_RC)_{n+1}\to W$, then $\bar\beta_{p,q}=0$.
:::

::: {.proof}

Let $x\in Z_p(C)$ and $y\in C_{q+1}$.
In $(C\tensor_RC)_{n+1}$ one has $d(x\tensor_R y)=d^Cx\tensor_R y+(-1)^px\tensor_R d^Cy=(-1)^px\tensor_R d^Cy$, because $x$ is a cycle; so $0=\beta_n\bigl(d(x\tensor_R y)\bigr)=(-1)^p\beta_{p,q}(x,d^Cy)$, since $\beta$ is a chain map into a complex with zero differentials, and hence $\beta_{p,q}(x,d^Cy)=0$.
Similarly, for $x'\in C_{p+1}$ and $y\in Z_q(C)$ one has $d(x'\tensor_R y)=d^Cx'\tensor_R y$, so $\beta_{p,q}(d^Cx',y)=0$.
Thus $\beta_{p,q}$ annihilates $Z_p(C)\times B_q(C)$ and $B_p(C)\times Z_q(C)$, and $B_p\subseteq Z_p$ makes it descend to a pairing $H_p(C)\times H_q(C)\to W$, which is the assignment displayed.

If $\beta_n=\gamma\circ d_{n+1}$ and $x,y$ are cycles, then $d(x\tensor_Ry)=0$ by the first computation, so $\beta_{p,q}(x,y)=\gamma\bigl(d(x\tensor_Ry)\bigr)=0$ by the factorization.
:::

::: {.proposition #prop:degreewise-isometry title="Degreewise isometries"}

Let $C\in\mathbf{Ch}(R\text{-}\mathbf{Mod})$ and let $b_p\colon C_p\times C_p\to W$ be $R$-bilinear for every $p\in\bZ$.
Suppose every differential of $C$ preserves these forms:
$$
b_{p-1}(d^Cx,d^Cy)=b_p(x,y)
\qquad(x,y\in C_p,\ p\in\bZ).
$$
Then $b_p=0$ for every $p$.
:::

::: {.proof}

Apply the hypothesis in degree $p$, then in degree $p-1$ to the vectors $d^Cx,d^Cy\in C_{p-1}$, which is where that instance of the hypothesis lives; for $x,y\in C_p$,
$$
b_p(x,y)=b_{p-1}(d^Cx,d^Cy)=b_{p-2}\bigl((d^C)^2x,(d^C)^2y\bigr)=b_{p-2}(0,0)=0,
$$
the last step because $(d^C)^2=0$ and a bilinear form vanishes on a pair with a zero entry.
:::

::: {.proposition #prop:complex-form-degree-2m title="Forms of degree $2m$"}

Let $C\in\mathbf{Ch}(R\text{-}\mathbf{Mod})$ and let $n=2m$.

1. If $C$ is concentrated in degree $m$, then $(C\tensor_RC)_n=C_m\tensor_RC_m$, the compatibility condition of @def:complex-form is vacuous, and a $W$-valued bilinear form of degree $n$ on $C$ is a $W$-valued bilinear form on the module $C_m$ in the sense of @def:form-presheaves.

2. For every $C$, a symmetric form $\beta$ of degree $n$ induces on $H_m(C)$ a pairing satisfying
$$
\bar\beta_{m,m}(\eta,\xi)=(-1)^m\,\bar\beta_{m,m}(\xi,\eta),
$$
so that pairing is symmetric for even $m$ and skew-symmetric for odd $m$ (@def:form-axioms).
:::

::: {.proof}

For (1), $C_p=0$ for $p\neq m$, so the only summand $C_p\tensor_RC_q$ of $(C\tensor_RC)_n$ that can be nonzero is $C_m\tensor_RC_m$.
In the compatibility condition of @def:complex-form, $p+q=2m+1$, so $p\neq m$ or $q\neq m$; then $x=0$ or $y=0$, and both terms vanish.
A form of degree $n$ is therefore one $R$-linear map $C_m\tensor_RC_m\to W$, that is, an element of $\Bil_{R,W}(C_m)$ of @def:form-presheaves.

For (2), the pairing $\bar\beta_{m,m}$ on $H_m(C)$ is well defined and $R$-bilinear by @prop:form-on-homology.
The symmetry condition of @def:complex-form with $p=q=m$ gives $\beta_{m,m}(y,x)=(-1)^{m^2}\beta_{m,m}(x,y)$ for $x,y\in C_m$, and $(-1)^{m^2}=(-1)^m$.
For cycles $x,y$ with $\xi=[x]$ and $\eta=[y]$, this is the displayed identity.
:::

## Resolutions {#sec-resolutions}

::: {.definition #def:resolution title="Augmented complexes and resolutions"}

Let $M$ be an object of $\mca$.
A *left resolution* of $M$ is a complex $P$ with $P_i=0$ for $i<0$ together with a morphism $\epsilon\colon P_0\to M$ for which the augmented complex
$$
\cdots\too P_2\xrightarrow{\ d_2\ }P_1\xrightarrow{\ d_1\ }P_0
\xrightarrow{\ \epsilon\ }M\too0
$$
is exact.
It is a *projective resolution* if every $P_i$ is projective and a *free resolution* if every $P_i$ is free [@Wei94, Def. 2.2.4].
Every $R$-module has a projective resolution, and every object of an abelian category with enough projectives has one [@Wei94, Lem. 2.2.5].
A projective resolution of $M$ is a cofibrant replacement of $M$ in the model structure of @thm:projective-model-structure, and the bar construction of @def:comonad-resolution produces one from the free-module adjunction.
:::

::: {.theorem #thm:resolution-comparison title="Comparison of resolutions"}

Let $\epsilon\colon P\to M$ be a projective resolution and let $\eta\colon Q\to N$ be a resolution.
Every morphism $f'\colon M\to N$ lifts to a chain map $f\colon P\to Q$ with $\eta f_0=f'\epsilon$, and any two such lifts are chain homotopic [@Wei94, Thm. 2.2.6].
:::

::: {.proof}

This is [@Wei94, Thm. 2.2.6].
The lift is built degree by degree: $f_0$ lifts $f'\epsilon$ along the epimorphism $\eta$ because $P_0$ is projective, and $f_n$ lifts $f_{n-1}d^P_n$ along $Q_n\twoheadrightarrow\operatorname{im}d^Q_n$ for the same reason, the composite landing in $\ker d^Q_{n-1}=\operatorname{im}d^Q_n$ by exactness of $Q$ and $d^Pd^P=0$.
The homotopy is built by the same induction, from the observation that $d^Q_n\bigl(f_n-g_n-s_{n-1}d^P_n\bigr)=0$, so the difference lifts again.
Only projectivity of the $P_n$, exactness of both augmented complexes and additivity are used; the $Q_n$ need not be projective.
:::

::: {.definition #def:syzygy title="Syzygies"}

Let
$$
\cdots\too F_2\xrightarrow{\ \varphi_2\ }F_1\xrightarrow{\ \varphi_1\ }F_0
$$
be a free resolution of an $R$-module $M$, so that $\coker\varphi_1=M$.
The *$i$th syzygy module* of $M$ is $\im\varphi_i$ [@Eis95, §1.10].

A surjection $F_0\twoheadrightarrow M$ determines its kernel; a free module surjecting onto that kernel is a further choice, and the resolution records the whole sequence of such choices together with the chosen generating family of each syzygy module.
:::

::: {.theorem #thm:hilbert-syzygy title="The Hilbert syzygy theorem"}

Let $k$ be a field and $R=k[x_1,\dots,x_r]$.
Every finitely generated graded $R$-module has a graded free resolution of length at most $r$ by finitely generated free modules [@Eis95, Thm. 1.13].
:::

::: {.proof}

This is [@Eis95, Thm. 1.13].
The proof uses exactness of the Koszul complex $K(x_1,\dots,x_r)$ on a regular sequence, which makes it a free resolution of $k$ of length $r$ [@Eis95, Ch. 17], and the coincidence of the minimal resolution with the computation of Tor [@Eis95, Ch. 20].
With those, the bound is $\Tor^R_i(M,k)\cong F_i\tensor_Rk$ for the minimal resolution $F$ of $M$, which vanishes for $i>r$ because $K(x)$ does, so $F_i=0$ for $i>r$.
:::

::: {.definition #def:minimal-resolution title="Minimal free resolutions"}

Let $(R,\mathfrak m)$ be a local ring.
A free resolution $F$ of $M$ is *minimal* if $\im\varphi_n\iscontainedin\mathfrak mF_{n-1}$ for every $n$, equivalently if every differential of $F\tensor_RR/\mathfrak m$ is zero [@Eis95, Ch. 20].
For a finitely generated module over a local ring, and for a finitely generated graded module over a positively graded algebra over a field with its graded maximal ideal, the minimal free resolution is unique up to isomorphism, and every free resolution is the direct sum of the minimal one with a free resolution of the zero module [@Eis95, Ch. 20].
:::

## Derived functors, Ext, and Tor {#sec-derived-functors}

::: {.definition #def:derived-functor title="Left and right derived functors"}

Let $F\colon\mca\to\mathcal B$ be a right exact functor of abelian categories and let $\mca$ have enough projectives.
For $A\in\mca$ choose a projective resolution $P\to A$ and set
$$
L_iF(A)=H_i\bigl(F(P)\bigr).
$$
A second projective resolution gives a canonically isomorphic object, and the lift of @thm:resolution-comparison makes each $L_iF$ a functor $\mca\to\mathcal B$ [@Wei94, §2.4, Lem. 2.4.1, Lem. 2.4.4].
For a left exact $F$ and an $\mca$ with enough injectives, the *right derived functors* $R^iF$ are defined dually from injective resolutions [@Wei94, §2.5].
:::

::: {.definition #def:ext-tor title="Ext and Tor"}

For $R$-modules $A$ and $B$,
$$
\Ext^i_R(A,B)=R^i\Hom_R(A,-)(B),
\qquad
\Tor^R_n(A,B)=L_n(-\tensor_RB)(A)
$$
[@Wei94, Def. 2.5.2, Def. 2.6.4].
Then $\Ext^0_R(A,B)=\Hom_R(A,B)$ and $\Tor^R_0(A,B)\cong A\tensor_RB$, and $\Tor^R_n(A,B)=H_n(P\tensor_RB)$ for a projective resolution $P\to A$ [@Wei94, §2.6].
Resolving either variable gives the same result:
$$
L_*(A\tensor_R-)(B)\cong L_*(-\tensor_RB)(A)
$$
[@Wei94, §2.7].
For projective $A$, $\Tor^R_n(A,B)=0$ for $n\ne0$ [@Wei94, §2.6] and $\Ext^i_R(A,B)=0$ for $i\ne0$ [@Wei94, §2.5].

For a lattice $L$, projectivity kills $\Tor^R_1(L,K/R)$ and keeps $\Hom_R(L,-)$ exact on the coefficient sequence
$$
0\to R\to K\to K/R\to0.
$$
:::
