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
in $\mathbf{Ch}(\mca)$ is exact (@def:exact-complex) if and only if, for every $n$, the sequence
$$
0\to A_n\to B_n\to C_n\to0
$$
is exact in $\mca$ [@Wei94, Thm. 1.2.3, Ex. 1.2.4].
:::

::: {.proof}

This is [@Wei94, Thm. 1.2.3 and Ex. 1.2.4].
The reason it transfers is that every construction involved is degreewise: kernels (@def:kernel-cokernel) and cokernels (@def:kernel-cokernel) of a chain map (@def:chain-complexes) are taken in each degree (@def:graded-object) with the restricted differentials, which are well defined because $f$ intertwines them, and $\operatorname{Coim}\to\operatorname{Im}$ is degreewise the isomorphism (@def:isomorphism-of-objects) of the abelian base (@def:abelian-category) and hence, by the degreewise criterion for a chain map to be an isomorphism, one of complexes.
Since kernels and cokernels are degreewise, monic, epic and exactness are checked in each degree, which is the second assertion.
:::

## Homology and exactness {#sec-homology-and-exactness}

Assume $\mca$ abelian for the remainder of the chapter.

::: {.definition #def:homology title="Cycles, boundaries, and homology" defines="$n$-cycle; $n$-boundary; homology; $Z_n(C)$; $B_n(C)$; $H_n(C)$"}

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

::: {.definition #def:exact-complex title="Exactness" defines="exact at $n$; exact; short exact sequence"}

A complex $C$ is *exact at $n$* if $H_n(C)=0$, and *exact* if it is exact at every degree (@def:graded-object).
Exactness at $n$ and exactness are isomorphism-invariant properties of objects of $\mathbf{Ch}(\mca)$ and therefore define replete full subcategories (@def:subcategory), the second being the intersection over $n\in\bZ$ of the first.

A short exact sequence
$$
0\to A\xrightarrow{\,i\,}B\xrightarrow{\,p\,}C\to0
$$
is the complex concentrated in degrees $2,1,0$ with $d_2=i$ and $d_1=p$, together with the assertion that this complex is exact: exactness at $2$ says $i$ is monic, exactness at $1$ says $\im i$ and $\ker p$ are the same subobject of $B$, and exactness at $0$ says $p$ is epic.
:::

::: {.definition #def:quasi-isomorphism title="Quasi-isomorphisms" defines="quasi-isomorphism"}

A chain map (@def:chain-complexes) $u\colon C\to D$ is a *quasi-isomorphism* if $H_n(u)$ is an isomorphism (@def:isomorphism-of-objects) for every $n$ [@Wei94, Def. 1.1.2].
These are the weak equivalences (@def:quasi-isomorphism) of the model structure of @thm:projective-model-structure.
:::

::: {.theorem #thm:homology-les title="The long exact homology sequence"}

Let
$$
0\to A\xrightarrow{\,f\,}B\xrightarrow{\,g\,}C\to0
$$
be a short exact sequence (@def:exact-complex) in $\mathbf{Ch}(\mca)$.
There are natural connecting morphisms $\del\colon H_n(C)\to H_{n-1}(A)$ for which
$$
\cdots\too H_n(A)\xrightarrow{\,H_n(f)\,}H_n(B)\xrightarrow{\,H_n(g)\,}H_n(C)
\xrightarrow{\ \del\ }H_{n-1}(A)\too\cdots
$$
is exact (@def:exact-complex) [@Wei94, Thm. 1.3.1].
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
Applying it to the translate $[n]$ gives the sequence in every degree (@def:graded-object) at once, and naturality is functoriality of the snake lemma.
:::

## Translation, truncation, and the mapping cone {#sec-translation-cone}

::: {.definition #def:translation title="Translation" defines="$p$th translate; $C[p]$"}

For $p\in\bZ$ the *$p$th translate* $C[p]$ of $C$ has $C[p]_n=C_{n+p}$ with differential $(-1)^pd^C$.
Setting $f[p]_n=f_{n+p}$ on chain maps (@def:chain-complexes) makes $[p]$ an isomorphism (@def:isomorphism-of-objects) of categories $\mathbf{Ch}(\mca)\to\mathbf{Ch}(\mca)$ with inverse $[-p]$, and
$$
H_n(C[p])=H_{n+p}(C)
$$
[@Wei94, 1.2.8].
:::

::: {.definition #def:good-truncation title="Good truncation" defines="good truncation; $\tau_{\ge n}C$; $\tau_{<n}C$"}

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

::: {.definition #def:mapping-cone title="The mapping cone" defines="mapping cone; $\cone(f)$"}

Let $f\colon B\to C$ be a chain map (@def:chain-complexes).
The *mapping cone* of $f$ is the complex with
$$
\cone(f)_n=B_{n-1}\oplus C_n,
\qquad
d(b,c)=\bigl(-d^Bb,\;d^Cc-f(b)\bigr)
$$
[@Wei94, 1.5.1].
The inclusion of $C$ and the projection onto $B[-1]$ form a short exact sequence (@def:exact-complex)
$$
0\too C\too\cone(f)\too B[-1]\too0,
$$
and $f$ is a quasi-isomorphism (@def:quasi-isomorphism) if and only if $\cone(f)$ is exact (@def:exact-complex) [@Wei94, Cor. 1.5.4].
:::

## Forms on a chain complex {#sec-complex-forms}

Work in $\mathbf{Ch}(R\text{-}\mathbf{Mod})$.
A $W$-valued bilinear form on an $R$-module $M$ is an element of $\Hom_R(M\tensor_RM,W)$ (@def:module-bilinear-form), and the form categories $\mathcal B_{R,W}$ of @def:form-categories are the categories of elements of the presheaves so obtained.

::: {.definition #def:complex-tensor-product title="The tensor product of complexes" defines="tensor product complex; $C\tensor_RD$"}

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
commutes (@def:commutative-diagram) with the two differentials and is an isomorphism (@def:isomorphism-of-objects) of complexes; it is the symmetry of @def:braided-symmetric for this tensor product.
:::

::: {.definition #def:value-complex title="Value complexes" defines="value complex; $W\langle n\rangle$"}

Regard $W$ as the complex concentrated in degree zero. For $n\in\bZ$ define $W\langle n\rangle:=W[-n]$, using @def:translation; thus $W\langle n\rangle$ has $W$ in degree $n$, zero modules elsewhere, and zero differentials. This placement notation is distinct from the translate $W[n]$, which is concentrated in degree $-n$.
:::

::: {.definition #def:complex-form title="Bilinear forms on a complex" defines="$W$-valued bilinear form of degree $n$ on $C$"}

Let $C\in\mathbf{Ch}(R\text{-}\mathbf{Mod})$.
A *$W$-valued bilinear form of degree (@def:graded-object) $n$ on $C$* is a chain map (@def:chain-complexes)
$$
\beta\colon C\tensor_RC\too W\langle n\rangle.
$$

Since $W\langle n\rangle$ vanishes outside degree $n$, such a chain map is one $R$-linear map
$$
\beta_n\colon\bigoplus_{p+q=n}C_p\tensor_RC_q\too W,
$$
equivalently a family of $R$-bilinear maps $\beta_{p,q}\colon C_p\times C_q\to W$ indexed by the pairs with $p+q=n$.
The differentials of $W\langle n\rangle$ are zero, so the condition that $\beta$ be a chain map is $\beta_n\circ d_{n+1}=0$, which reads
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
For a bilinear form $\beta$ of degree (@def:graded-object) (@def:complex-form) $n$ on $C$ set
$$
\beta^{\sharp}_r\colon C_r\too(C^{n-*})_r,
\qquad
\beta^{\sharp}_r(x)=(-1)^{r}\,\beta_{r,n-r}(x,-).
$$
Then $\beta\mapsto\beta^{\sharp}$ is a bijection from the bilinear forms of degree $n$ on $C$ to the chain maps (@def:chain-complexes) $C\to C^{n-*}$.

The condition that $\beta^{\sharp}$ be a chain equivalence (@def:equivalence-of-objects) is the Poincaré condition of @def:poincare-complex.
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
So $\beta^{\sharp}$ commutes (@def:commutative-diagram) with the differentials exactly when
$$
(-1)^{r-1}\beta_{r-1,n-r+1}(d^Cx,y)=(-1)^{2r}\beta_{r,n-r}(x,d^Cy),
$$
that is, multiplying by $(-1)^{r-1}$, exactly when $\beta_{r-1,n-r+1}(d^Cx,y)+(-1)^{r}\beta_{r,n-r}(x,d^Cy)=0$ for all $r$, which is the condition of @def:complex-form with $p=r$ and $q=n+1-r$.

A chain map $\beta^{\sharp}$ is a chain equivalence exactly when it is a quasi-isomorphism (@def:quasi-isomorphism), and under the bijection that is the condition of @def:poincare-complex.
:::

::: {.proposition #prop:form-on-homology title="The induced pairing on homology"}

Let $\beta$ be a $W$-valued bilinear form of degree (@def:graded-object) (@def:complex-form) $n$ on $C$ and let $p+q=n$.
The assignment
$$
\bar\beta_{p,q}\bigl([x],[y]\bigr)=\beta_{p,q}(x,y)
\qquad(x\in Z_p(C),\ y\in Z_q(C))
$$
is a well-defined $R$-bilinear map $H_p(C)\times H_q(C)\to W$.
Put $T=C\tensor_RC$ and denote its differential by $d_n^T\colon T_n\to T_{n-1}$. If $\beta_n=\gamma\circ d_n^T$ for an $R$-linear $\gamma\colon T_{n-1}\to W$, then $\bar\beta_{p,q}=0$.
:::

::: {.proof}

Let $x\in Z_p(C)$ and $y\in C_{q+1}$.
In $(C\tensor_RC)_{n+1}$ one has $d(x\tensor_R y)=d^Cx\tensor_R y+(-1)^px\tensor_R d^Cy=(-1)^px\tensor_R d^Cy$, because $x$ is a cycle; so $0=\beta_n\bigl(d(x\tensor_R y)\bigr)=(-1)^p\beta_{p,q}(x,d^Cy)$, since $\beta$ is a chain map (@def:chain-complexes) into a complex with zero differentials, and hence $\beta_{p,q}(x,d^Cy)=0$.
Similarly, for $x'\in C_{p+1}$ and $y\in Z_q(C)$ one has $d(x'\tensor_R y)=d^Cx'\tensor_R y$, so $\beta_{p,q}(d^Cx',y)=0$.
Thus $\beta_{p,q}$ annihilates $Z_p(C)\times B_q(C)$ and $B_p(C)\times Z_q(C)$, and $B_p\subseteq Z_p$ makes it descend to a pairing $H_p(C)\times H_q(C)\to W$, which is the assignment displayed.

If $\beta_n=\gamma\circ d_n^T$ and $x,y$ are cycles with $p+q=n$, then $d_n^T(x\tensor_R y)=d^Cx\tensor_R y+(-1)^px\tensor_R d^Cy=0$. Hence $\beta_{p,q}(x,y)=\gamma\bigl(d_n^T(x\tensor_R y)\bigr)=0$.
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

Apply the hypothesis in degree (@def:graded-object) $p$, then in degree $p-1$ to the vectors $d^Cx,d^Cy\in C_{p-1}$, which is where that instance of the hypothesis lives; for $x,y\in C_p$,
$$
b_p(x,y)=b_{p-1}(d^Cx,d^Cy)=b_{p-2}\bigl((d^C)^2x,(d^C)^2y\bigr)=b_{p-2}(0,0)=0,
$$
the last step because $(d^C)^2=0$ and a bilinear form vanishes on a pair with a zero entry.
:::

::: {.proposition #prop:complex-form-degree-2m title="Forms of degree $2m$"}

Let $C\in\mathbf{Ch}(R\text{-}\mathbf{Mod})$ and let $n=2m$.

1. If $C$ is concentrated in degree (@def:graded-object) $m$, then $(C\tensor_RC)_n=C_m\tensor_RC_m$, the compatibility condition of @def:complex-form is vacuous, and a $W$-valued bilinear form of degree $n$ on $C$ is a $W$-valued bilinear form on the module $C_m$ in the sense of @def:form-presheaves.

2. For every $C$, a symmetric form $\beta$ of degree $n$ induces on $H_m(C)$ a pairing satisfying
$$
\bar\beta_{m,m}(\eta,\xi)=(-1)^m\,\bar\beta_{m,m}(\xi,\eta),
$$
so that pairing is symmetric for even $m$ and skew-symmetric for odd (@def:form-axioms) $m$.
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

::: {.definition #def:resolution title="Augmented complexes and resolutions" defines="left resolution; projective resolution; free resolution"}

Let $M$ be an object of $\mca$.
A *left resolution* of $M$ is a complex $P$ with $P_i=0$ for $i<0$ together with a morphism $\epsilon\colon P_0\to M$ for which the augmented complex
$$
\cdots\too P_2\xrightarrow{\ d_2\ }P_1\xrightarrow{\ d_1\ }P_0
\xrightarrow{\ \epsilon\ }M\too0
$$
is exact (@def:exact-complex).
It is a *projective resolution* if every $P_i$ is projective (@def:module-subcategories) and a *free resolution* if every $P_i$ is free (@def:module-subcategories) [@Wei94, Def. 2.2.4].
Every $R$-module has a projective resolution, and every object of an abelian category (@def:abelian-category) with enough projectives has one [@Wei94, Lem. 2.2.5].
A projective resolution of $M$ is a cofibrant replacement of $M$ in the projective model structure on bounded-below complexes. For modules, the **free-on-sets cotriple** of @def:comonad-resolution produces an ordinary free resolution [@Wei94, 8.6.14]; the relative bar cotriple of [@Wei94, 8.6.12] gives an exact resolution whose terms need not be projective.
:::

::: {.theorem #thm:resolution-comparison title="Comparison of resolutions"}

Let $\epsilon\colon P\to M$ be a projective resolution (@def:resolution) and let $\eta\colon Q\to N$ be a resolution.
Every morphism $f'\colon M\to N$ lifts to a chain map (@def:chain-complexes) $f\colon P\to Q$ with $\eta f_0=f'\epsilon$, and any two such lifts are chain homotopic [@Wei94, Thm. 2.2.6].
:::

::: {.proof}

This is [@Wei94, Thm. 2.2.6].
The lift is built degree (@def:graded-object) by degree: $f_0$ lifts $f'\epsilon$ along the epimorphism $\eta$ because $P_0$ is projective (@def:module-subcategories), and $f_n$ lifts $f_{n-1}d^P_n$ along $Q_n\twoheadrightarrow\operatorname{im}d^Q_n$ for the same reason, the composite landing in $\ker d^Q_{n-1}=\operatorname{im}d^Q_n$ by exactness of $Q$ and $d^Pd^P=0$.
The homotopy is built by the same induction, from the observation that $d^Q_n\bigl(f_n-g_n-s_{n-1}d^P_n\bigr)=0$, so the difference lifts again.
Only projectivity of the $P_n$, exactness of both augmented complexes and additivity are used; the $Q_n$ need not be projective.
:::

::: {.definition #def:syzygy title="Syzygies" defines="$i$th syzygy module"}

Let
$$
\cdots\too F_2\xrightarrow{\ \varphi_2\ }F_1\xrightarrow{\ \varphi_1\ }F_0
$$
be a free resolution (@def:resolution) of an $R$-module $M$, so that $\coker\varphi_1=M$.
The *$i$th syzygy module* of $M$ is $\im\varphi_i$ [@Eis95, §1.10].

A surjection $F_0\twoheadrightarrow M$ determines its kernel (@def:kernel-cokernel); a free (@def:module-subcategories) module surjecting onto that kernel is a further choice, and the resolution records the whole sequence of such choices together with the chosen generating family (@def:generating-frame) of each syzygy module.
:::

::: {.theorem #thm:hilbert-syzygy title="The Hilbert syzygy theorem"}

Let $k$ be a field and $R=k[x_1,\dots,x_r]$.
Every finitely generated (@def:module-subcategories) graded $R$-module has a graded free resolution (@def:resolution) of length at most $r$ by finitely generated free (@def:module-subcategories) modules [@Eis95, Thm. 1.13].
:::

::: {.proof}

This is [@Eis95, Thm. 1.13].
The proof uses exactness of the Koszul complex $K(x_1,\dots,x_r)$ on a regular sequence, which makes it a free resolution of $k$ of length $r$ [@Eis95, Cor. 17.5], and the coincidence of the minimal (@def:minimal-resolution) resolution with the computation of Tor [@Eis95, Cor. 19.5].
With those, the bound is $\Tor^R_i(M,k)\cong F_i\tensor_Rk$ for the minimal resolution $F$ of $M$ supplied by @thm:minimal-free-resolution-existence-splitting, which vanishes for $i>r$ because $K(x)$ does, so $F_i=0$ for $i>r$.
:::

::: {.definition #def:minimal-resolution title="Minimal free resolutions" defines="minimal free resolution"}

Let $(R,\mathfrak m)$ be a commutative local ring, or a nonnegatively graded commutative algebra over a field $k$ with $R_0=k$ and $\mathfrak m=R_{>0}$ (in the latter case all modules and maps in the resolution are graded).
A free resolution (@def:resolution) $F$ of $M$ is *minimal* if $\im\varphi_n\iscontainedin\mathfrak mF_{n-1}$ for every $n\geq1$, equivalently if every differential of the unaugmented complex $F\tensor_R R/\mathfrak m$ is zero [@Eis95, §19.1, Definition before Lem. 19.4, pp. 472–473].
This definition does not assert existence over arbitrary local rings.

:::

::: {.theorem #thm:minimal-free-resolution-existence-splitting title="Existence, uniqueness, and splitting of finite-term minimal free resolutions"}

Let $(R,\mathfrak m)$ be a commutative Noetherian local ring and $M$ a finitely generated $R$-module. There exists a minimal free resolution $F\to M$ with every $F_i$ finite free. More generally, the construction works over an arbitrary commutative local ring whenever $M$ and all successive kernels in the construction are finitely generated.

The same existence statement holds in the graded category when $R$ is a Noetherian nonnegatively graded commutative $k$-algebra, $R_0=k$ is a field, $\mathfrak m=R_{>0}$, and $M$ is finitely generated as a graded module.

In either the local or graded setting, **if** $M$ admits a degreewise finite free minimal resolution $F\to M$, then every free resolution $G\to M$ (with no finite-rank requirement on $G_i$) is isomorphic, as an augmented complex, to $F\oplus C$, where $C$ is a contractible complex of free modules resolving zero. Every minimal free resolution is therefore isomorphic to $F$. This is the conditional splitting principle of [@Eis95, Thm. 20.2, p. 491]; the finiteness condition on $F_i$ is part of the argument.

:::

::: {.proof}

Write $K_0=M$. In the local case, choose lifts of a basis of the finite-dimensional residue vector space $K_i/\mathfrak m K_i$ and let $F_i\to K_i$ be the map from the free module on those lifts. Nakayama's lemma ([Stacks Project, Lemma 10.20.1(4), Tag 00DV](https://stacks.math.columbia.edu/tag/00DV)) proves that the map is onto when $K_i$ is finitely generated. Since the induced residue-space map is an isomorphism, its kernel $K_{i+1}$ is contained in $\mathfrak m F_i$. Noetherianity ensures that $K_{i+1}$ is finitely generated. Iterating, and composing $F_{i+1}\to K_{i+1}$ with the inclusion in $F_i$, gives the required exact minimal complex. The same induction proves the stated more general sufficient condition. In the graded case choose homogeneous residue-space bases and give each free generator the degree of its lift. Each finite graded module over a nonnegatively graded ring is bounded below in internal degree; if a bounded-below graded module $N$ satisfies $N=R_{>0}N$, its least nonzero homogeneous degree would be strictly greater than itself. Thus $N=0$, giving graded Nakayama and the same induction in graded modules. Noetherianity again ensures that each kernel is finite.

For splitting, use @thm:resolution-comparison to choose chain maps $a:F\to G$ and $b:G\to F$ lifting the identity of $M$, in the indicated category. Their composite $ba$ is chain homotopic to $\id_F$. Minimality implies $(ba)_i\equiv\id_{F_i}\pmod{\mathfrak m}$, since both terms of the homotopy formula contain a differential of $F$. In the local case the determinant of $(ba)_i$ is a unit (finite freeness is essential here). In the graded case its cokernel is a bounded-below graded module and is zero by graded Nakayama, so $(ba)_i$ is surjective; since $F_i$ is finite free, a right inverse gives a unit determinant and hence invertibility. Its inverse is graded since the map is graded and bijective. Thus $ba$ is a chain automorphism, and replacing $b$ by $(ba)^{-1}b$ makes $ba=\id_F$. In particular $a$ identifies $F$ with a direct summand complex of $G$, with complementary complex $C=\ker b$.

Here is why the complementary terms are free, even for infinite-rank $G_i$. A split injection $F_i\to G_i$ remains injective modulo $\mathfrak m$. The images of a finite basis of $F_i$ have finite support in a basis of $G_i$, and some square minor of size $\operatorname{rank}F_i$ is invertible modulo $\mathfrak m$. In the local case this minor has unit determinant. In the graded case choose the minor separately for each residue-space degree, with homogeneous coordinates of the same degrees as the source generators; the selected free summand then has the same multiset of generator degrees as $F_i$. Its projection matrix has determinant of degree zero, nonzero modulo $R_{>0}$, so its determinant is a unit in $k$. The projection of $a(F_i)$ to that selected free summand is therefore an isomorphism. In the decomposition of $G_i$ into the selected summand and the span of the remaining basis vectors, $a(F_i)$ is the graph of a linear map out of the selected summand. The quotient $G_i/a(F_i)$ is isomorphic to the span of the remaining basis vectors, so is free (graded free in the graded case). Since $C_i\simeq G_i/a(F_i)$, this proves freeness without a finite-rank assumption on $G_i$.

The augmentations of $F$ and $G$ agree under $a$, hence $C$ is exact, with zero augmentation. A bounded-below exact complex of projective modules is contractible: writing $Z_i=\ker(d_i:C_i\to C_{i-1})$ with $C_{-1}=0$, the exact sequences $0\to Z_i\to C_i\to Z_{i-1}\to0$ split inductively starting at $Z_0=C_0$, since each previous $Z_{i-1}$ is projective and then $Z_i$ is a direct summand of $C_i$. The splittings provide the contracting homotopy; this argument also works in graded modules. Finally if $G$ is minimal, its direct summand $C$ is minimal. Exactness and minimality give $C_0=\mathfrak m C_0$, which forces $C_0=0$ because a nonzero free module, of any rank, has nonzero residue vector space. Inductively $C_{i-1}=0$ gives $C_i=\im d_{i+1}\subseteq\mathfrak m C_i$, so $C_i=0$. Thus $C=0$ and the minimal resolution is unique up to isomorphism.

:::

::: {.example #ex:minimal-resolution-nonexistence-idempotent-maximal-ideal title="Failure of minimal free resolutions over a non-Noetherian local domain"}

For a field $k$, take the compatible union
$$
R=\bigcup_{j\geq0}k[[t^{1/2^j}]],\qquad
\mathfrak m=\bigcup_{j\geq0}t^{1/2^j}k[[t^{1/2^j}]]
$$
inside the union of the corresponding Laurent-series fields, with $t^{1/2^j}=(t^{1/2^{j+1}})^2$. Then $R$ is a local domain with residue field $k$ and nonzero idempotent maximal ideal $\mathfrak m^2=\mathfrak m$. The cyclic module $k=R/\mathfrak m$ admits no minimal free resolution, even allowing infinite free ranks.

Indeed the compatible constant-term maps have kernel $\mathfrak m$ and every element outside it is already a unit in one of the power-series rings. If $x=t^{1/2^j}u\in\mathfrak m$, it is the product of $t^{1/2^{j+1}}$ and $t^{1/2^{j+1}}u$, both in $\mathfrak m$; hence $\mathfrak m^2=\mathfrak m\ne0$. Suppose a minimal free resolution $F\to k$ exists. Then
$$
\mathfrak m F_0\subseteq\ker\epsilon=\im d_1\subseteq\mathfrak m F_0,
$$
so $F_0/\mathfrak m F_0\cong k$. Since $F_0$ is free it has rank one, and under a basis whose image in $k$ is $1$, $\epsilon:R\to k$ is the residue map. Now $d_1(F_1)=\mathfrak m$, and
$$ d_1(\mathfrak m F_1)=\mathfrak m d_1(F_1)=\mathfrak m^2=\mathfrak m. $$
Given $x\in F_1$, choose $y\in\mathfrak m F_1$ with $d_1(y)=d_1(x)$. Then $x-y\in\ker d_1=\im d_2\subseteq\mathfrak m F_1$, so $F_1=\mathfrak m F_1$. A free module of arbitrary rank reduces to a direct sum of copies of the residue field, one per basis element; thus $F_1=0$, contrary to $d_1(F_1)=\mathfrak m\ne0$. No application of Nakayama's lemma to an infinitely generated module is involved.

:::

## Derived functors, Ext, and Tor {#sec-derived-functors}

::: {.definition #def:derived-functor title="Left and right derived functors" defines="left derived functors; $L_iF$; right derived functors; $R^iF$"}

Let $F\colon\mca\to\mathcal B$ be a right exact functor of abelian categories and let $\mca$ have enough projectives (@def:module-subcategories).
For $A\in\mca$ choose a projective resolution (@def:resolution) $P\to A$ and set
$$
L_iF(A)=H_i\bigl(F(P)\bigr).
$$
A second projective resolution gives a canonically isomorphic object, and the lift of @thm:resolution-comparison makes each $L_iF$ a functor $\mca\to\mathcal B$ [@Wei94, §2.4, Lem. 2.4.1, Lem. 2.4.4].
For a left exact $F$ and an $\mca$ with enough injectives (@def:injective-map), the *right derived functors* $R^iF$ are defined dually from injective resolutions [@Wei94, §2.5].
:::

::: {.definition #def:ext-tor title="Ext and Tor" defines="Ext; $\Ext^i_R$; Tor; $\Tor^R_n$"}

For $R$-modules $A$ and $B$,
$$
\Ext^i_R(A,B)=R^i\Hom_R(A,-)(B),
\qquad
\Tor^R_n(A,B)=L_n(-\tensor_RB)(A)
$$
[@Wei94, Def. 2.5.2, Def. 2.6.4].
Then $\Ext^0_R(A,B)=\Hom_R(A,B)$ and $\Tor^R_0(A,B)\cong A\tensor_RB$, and $\Tor^R_n(A,B)=H_n(P\tensor_RB)$ for a projective resolution (@def:resolution) $P\to A$ [@Wei94, §2.6].
Resolving either variable gives the same result:
$$
L_*(A\tensor_R-)(B)\cong L_*(-\tensor_RB)(A)
$$
[@Wei94, §2.7].
For projective (@def:module-subcategories) $A$, $\Tor^R_n(A,B)=0$ for $n\ne0$ [@Wei94, §2.6] and $\Ext^i_R(A,B)=0$ for $i\ne0$ [@Wei94, §2.5].

For a lattice $L$, projectivity kills $\Tor^R_1(L,K/R)$ and keeps $\Hom_R(L,-)$ exact (@def:exact-complex) on the coefficient sequence
$$
0\to R\to K\to K/R\to0.
$$
:::
