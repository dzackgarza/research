# Hyperbolic forms and Witt classes {#sec-hyperbolic-witt}

Fix a commutative ring $R$ and take the value module $W=R$, so that the form category is $\mathcal B_{R,R}$ as in @def:form-categories, and its objects are pairs $(M,b)$ with $b\colon M\times M\to R$ bilinear.
Lattices, unimodularity, dual lattices, and discriminant modules are those of @sec-lattices-discriminant.

## The hyperbolic form on a module and its dual {#sec-hyperbolic-form}

::: {.definition #def:hyperbolic-form title="Hyperbolic forms"}

Let $M$ be an $R$-module and write $M^{*}=\Hom_R(M,R)$.
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

::: {.proposition #prop:hyperbolic-adjoint title="The adjoint map of a hyperbolic form"}

Let $\operatorname{can}_M\colon M\to M^{**}$ be the evaluation map, $\operatorname{can}_M(x)(\psi)=\psi(x)$.
Under the canonical isomorphism $(M\oplus M^{*})^{*}\cong M^{*}\oplus M^{**}$, the adjoint map of @def:polarization is
$$
h_M^{\sharp}\colon M\oplus M^{*}\too M^{*}\oplus M^{**},
\qquad
h_M^{\sharp}(x,\varphi)=\bigl(\varphi,\operatorname{can}_M(x)\bigr).
$$
Hence $h_M$ is nondegenerate if and only if $\operatorname{can}_M$ is injective, and perfect if and only if $\operatorname{can}_M$ is an isomorphism.
:::

::: {.proof}

A functional on a biproduct restricts to its two summands, giving the isomorphism $\Hom_R(M\oplus M^{*},R)\cong M^{*}\oplus M^{**}$ that sends $\lambda$ to $(\lambda\circ\iota_M,\lambda\circ\iota_{M^{*}})$.
Apply it to $\lambda=h_M^{\sharp}(x,\varphi)$, whose value on $(y,\psi)$ is $\psi(x)+\varphi(y)$: the restriction to $M\oplus0$ is $y\mapsto\varphi(y)$, which is $\varphi$, and the restriction to $0\oplus M^{*}$ is $\psi\mapsto\psi(x)$, which is $\operatorname{can}_M(x)$.
So $h_M^{\sharp}$ is the morphism displayed, and its two components are $\varphi$ and $\operatorname{can}_M(x)$.

Under this identification $h_M^{\sharp}=\id_{M^{*}}\oplus\operatorname{can}_M$.
Its kernel is $0\oplus\ker\operatorname{can}_M$, so it is injective exactly when $\operatorname{can}_M$ is; and a morphism of $R$-modules is an isomorphism exactly when it is injective and surjective, so $h_M^{\sharp}$ is an isomorphism exactly when $\operatorname{can}_M$ is, the other component being $\id_{M^{*}}$.
By @def:polarization, nondegeneracy of $h_M$ is vanishing of $\ker h_M^{\sharp}$ and perfection is vanishing of $\ker h_M^{\sharp}$ and $\operatorname{coker}h_M^{\sharp}$, so the two equivalences asserted follow.
:::

::: {.lemma #lem:double-dual-fg-projective title="The double dual of a finitely generated projective module"}

For a finitely generated projective $R$-module $M$, the evaluation map $\operatorname{can}_M\colon M\to M^{**}$ is an isomorphism.
:::

::: {.proof}

Evaluation commutes with finite biproducts: $\operatorname{can}_{M\oplus M'}=\operatorname{can}_M\oplus\operatorname{can}_{M'}$, since a functional on a biproduct is a pair of functionals and evaluation is componentwise.
For a free module of finite rank, $\operatorname{can}_{R^{n}}\colon R^{n}\to(R^{n})^{**}\cong R^{n}$ is the identity, because a functional is determined by its values on a basis and evaluation against the dual basis returns those values.

A finitely generated projective module is a summand of a finitely generated free module, $M\oplus M'\cong R^{n}$.
Then $\operatorname{can}_M\oplus\operatorname{can}_{M'}\cong\operatorname{can}_{R^{n}}\cong\id$, and a summand of an isomorphism is an isomorphism: if $f\oplus g$ is invertible, its inverse has components $f^{-1}$ and $g^{-1}$ under the same biproduct decomposition.
Hence $\operatorname{can}_M$ is an isomorphism.
:::

::: {.proposition #prop:hyperbolic-lattice title="Hyperbolic lattices"}

Let $R$ be a Dedekind domain and let $M$ be a finitely generated projective $R$-module.
Then $H(M)$ is a unimodular $R$-lattice in the sense of @def:lattice and @def:unimodular, and its discriminant module (@def:discriminant) is $A_{H(M)}=0$.
:::

::: {.proof}

The dual $M^{*}=\Hom_R(M,R)$ of a finitely generated projective module is finitely generated projective: a decomposition $M\oplus M'\cong R^{n}$ gives $M^{*}\oplus M'^{*}\cong(R^{n})^{*}\cong R^{n}$, because $\Hom_R(-,R)$ carries finite biproducts to finite biproducts.
So $M\oplus M^{*}$ is finitely generated projective and $H(M)$ is an $R$-lattice in the sense of @def:lattice.

By @lem:double-dual-fg-projective the evaluation map $\operatorname{can}_M$ is an isomorphism, so by @prop:hyperbolic-adjoint the adjoint $h_M^{\sharp}$ is an isomorphism.
Vanishing of the radical and the coradical is then nondegeneracy and perfection by @def:polarization, so $h_M$ is perfect.

The discriminant module $A_{H(M)}$ is the cokernel of $h_M^{\sharp}$ by @def:two-witnesses, and the cokernel of an isomorphism is zero; so $A_{H(M)}=0$, which is unimodularity by @def:unimodular.
:::

::: {.example #ex:hyperbolic-plane title="The hyperbolic plane"}

Take $M=R$ and the basis $e=(1,0)$, $f=(0,\id_R)$ of $R\oplus R^{*}$.
Then
$$
h_R(e,e)=0,\qquad h_R(f,f)=0,\qquad h_R(e,f)=1,
$$
so $H(R)$ has Gram matrix
$$
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
For $R=\bZ$ the lattice $H(\bZ)$ is even (@def:even-lattice), unimodular, and of signature $(1,1)$.
:::

::: {.definition #def:hyperbolic-functor title="The hyperbolic functor"}

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
H\colon(R\text{-}\mathbf{Mod})^{\simeq}\too(\mathcal B_{R,R})^{\simeq}
$$
between the cores of @def:core.
:::

::: {.definition #def:lagrangian title="Lagrangians and metabolic forms"}

Let $(M,b)$ be an object of $\mathcal B_{R,R}$ and let $N\iscontainedin M$ be a submodule.
Write
$$
N^{\perp}=\{x\in M\mid b(x,y)=0\text{ for all }y\in N\}.
$$
A *lagrangian* of $(M,b)$ is a direct summand $N\iscontainedin M$ with $N=N^{\perp}$.
The form $(M,b)$ is *metabolic* if it admits a lagrangian [@MH73, §I.6; @Ran98, Def. 20.1].
:::

::: {.remark}
[@MH73] writes *split* for this condition and attributes the term *metabolic* to Knebusch.
:::

::: {.proposition #prop:hyperbolic-metabolic title="Hyperbolic forms are metabolic"}

Let $M$ be an $R$-module for which $\operatorname{can}_M$ is injective.
Then $0\oplus M^{*}$ is a lagrangian of $H(M)$.
:::

::: {.proof}

The submodule $0\oplus M^{*}$ is a direct summand of $M\oplus M^{*}$, with complement $M\oplus0$.
For $\psi\in M^{*}$,
$$
h_M\bigl((x,\varphi),(0,\psi)\bigr)=\psi(x)+\varphi(0)=\psi(x),
$$
so $(0\oplus M^{*})^{\perp}$ consists of the pairs $(x,\varphi)$ with $\psi(x)=0$ for every $\psi\in M^{*}$, that is, with $\operatorname{can}_M(x)=0$.
Injectivity of $\operatorname{can}_M$ gives $x=0$, so $(0\oplus M^{*})^{\perp}=0\oplus M^{*}$ and the submodule is a lagrangian in the sense of @def:lagrangian.
:::

::: {.proposition #prop:metabolic-closure title="Closure of metabolic forms"}

Let $(X,b_X)$ and $(Y,b_Y)$ be metabolic perfect forms over $R$ with lagrangians $N_X$ and $N_Y$, and let $(Z,b_Z)$ be perfect.
Then $X\perp Y$ is metabolic, with lagrangian $N_X\perp N_Y$, and $X\otimes Z$, with the tensor product form of @def:form-tensor, is metabolic, with lagrangian $N_X\otimes Z$.
:::

::: {.proof}

Both closures are [@MH73, Lem. I.7.2], which states that Witt equivalence is compatible with orthogonal sum and with tensor product, and proves the compatibility by exhibiting exactly these lagrangians.
What the book's version adds is that the tensor-product closure needs nothing of $N_X$ beyond being a lagrangian: the form of @def:form-tensor vanishes on $(N_X\tensor Z)^{\otimes2}$ immediately, and the converse uses only that $b_Z$ is perfect.
:::

::: {.proposition #prop:negation-is-metabolic title="A form orthogonally summed with its twist"}

Let $(X,b_X)$ be a perfect form over $R$.
Then $X\perp X(-1)$, with the twist of @def:form-twist, is metabolic, and
$$
N\definedas\theset{(x,x)\st x\in X}
$$
is a lagrangian.
:::

::: {.proof}

This is the standard construction of the additive inverse in $W(R)$ [@MH73, I §7]: the diagonal $N=\theset{(x,x)}$ is a direct summand split by $(x,y)\mapsto x$, it is isotropic because the two summands carry opposite forms, and an element of its orthogonal complement satisfies $b_X(x,z)=b_X(y,z)$ for all $z$, so $x=y$ by perfection.
:::

## Hyperbolic stabilization {#sec-hyperbolic-stabilization}

::: {.definition #def:hyperbolic-stabilization title="Orthogonal sum with a fixed object"}

With the orthogonal sum of @def:orthogonal-sum, an object $M$ of $\mathcal B_{R,R}$ defines
$$
F_M\colon\mathcal B_{R,R}\too\mathcal B_{R,R},
\qquad
F_M(X)=X\perp M,
\qquad
F_M(f)=f\oplus\id_{M},
$$
together with the inclusion of the first summand
$$
\iota^{M}_{X}\colon X\too F_M(X),
$$
a morphism of $\mathcal B_{R,R}$ natural in $X$.
The *hyperbolic stabilization* is
$$
S:=F_{H(R)} .
$$
For $R$ a Dedekind domain and $M$ an $R$-lattice, $F_M$ restricts to an endofunctor of $\mathbf{Lat}_R$.
:::

::: {.proposition #prop:orthogonal-sum-unimodular title="Nondegeneracy and unimodularity of orthogonal sums"}

Let $R$ be a ring and let $(L,b_L)$ and $(L',b_{L'})$ be forms over $R$ with finitely generated projective underlying modules.
If both are nondegenerate then $L\perp L'$ is nondegenerate, and if both are unimodular $R$-lattices then $L\perp L'$ is a unimodular $R$-lattice.
:::

::: {.proof}

Under $(L\oplus L')^{*}\cong L^{*}\oplus L'^{*}$ the adjoint of the orthogonal sum is $b_{L\perp L'}^{\sharp}=b_L^{\sharp}\oplus b_{L'}^{\sharp}$, by @def:orthogonal-sum: the mixed terms vanish, so the components of $b_{L\perp L'}^{\sharp}(x,x')$ are $b_L^{\sharp}(x)$ and $b_{L'}^{\sharp}(x')$.
A biproduct morphism has zero kernel exactly when both components do, and is an isomorphism exactly when both components are, so the two assertions follow from @def:polarization and @def:two-witnesses.
The underlying module of an orthogonal sum of lattices is finitely generated projective, being a biproduct of such.
:::

::: {.proposition #prop:stabilization-discriminant title="Stabilization preserves the discriminant"}

Let $R$ be a Dedekind domain with fraction field $K$, and let $L$ be an $R$-lattice.
Then
$$
A_{S(L)}\;\cong\;A_L ,
$$
the canonical isomorphism $(L\oplus H(R))^{*}\cong L^{*}\oplus H(R)^{*}$ identifying
$$
b_{S(L)}^{\sharp}=b_L^{\sharp}\oplus h_R^{\sharp}.
$$
For $R=\bZ$ it is an isomorphism in $\mathbf{DiscBil}_{\bZ}$ (@def:discbil), and for $L$ even it is an isomorphism in $\mathbf{DiscQuad}_{\bZ}$ (@def:discquad).
:::

::: {.proof}

The adjoint of an orthogonal sum is the orthogonal sum of the adjoints, as in @prop:orthogonal-sum-unimodular, and the canonical isomorphism of duals identifies $b_{S(L)}^{\sharp}$ with $b_L^{\sharp}\oplus h_R^{\sharp}$.
By @prop:hyperbolic-lattice, $h_R^{\sharp}$ is an isomorphism, so the cokernel of the sum is $\operatorname{coker}b_L^{\sharp}$, the cokernels being taken componentwise in @def:two-witnesses: $\operatorname{coker}(f\oplus g)\cong\operatorname{coker}f\oplus\operatorname{coker}g$, and $\operatorname{coker}h_R^{\sharp}=0$.
This gives $A_{S(L)}\cong A_L$.

For the forms, $H(R)$ is unimodular by @prop:hyperbolic-lattice, so $H(R)^{\#}=H(R)$ inside $H(R)\tensor_RK$ by @def:metric-dual, and
$$
S(L)^{\#}=L^{\#}\oplus H(R),
\qquad
S(L)^{\#}/S(L)=L^{\#}/L .
$$
The $K/R$-valued form of @def:discriminant on an orthogonal sum restricts to the orthogonal sum of the forms on the summands, because the mixed terms vanish, and it vanishes identically on the second summand, whose dual equals the summand itself.
So the identification is an isometry of discriminant forms, in $\mathbf{DiscBil}_{\bZ}$ when $R=\bZ$; when $L$ is even, $H(\bZ)$ is even by @ex:hyperbolic-plane, so $S(L)$ is even and $q_L$ is defined by the same formula, giving an isometry in $\mathbf{DiscQuad}_{\bZ}$ of @def:discquad.
:::

::: {.theorem #thm:stabilization-not-unimodular title="The discriminant along the stabilization tower"}

Let $R$ be a Dedekind domain and let $L$ be an $R$-lattice with $A_L\neq0$.
Then $A_{S^{n}(L)}\cong A_L$ for every $n\geq0$.
Consequently $S^{n}(L)$ is not unimodular, and $S^{n}(L)$ is not isometric to $H(P)$ for any finitely generated projective $R$-module $P$ and any $n\geq0$.
:::

::: {.proof}

Iterating @prop:stabilization-discriminant gives $A_{S^{n}(L)}\cong A_{S^{n-1}(L)}\cong\cdots\cong A_L$, and the hypothesis $A_L\neq0$ makes every term nonzero.
A unimodular lattice has vanishing discriminant module, by @def:unimodular and @def:two-witnesses, so $S^{n}(L)$ is not unimodular.
The discriminant module is carried along by isometries, since an isometry is an isomorphism of the defining exact sequences of @def:two-witnesses and hence induces an isomorphism of cokernels.
So if $S^{n}(L)$ were isometric to $H(P)$ for a finitely generated projective $P$, then $A_{S^{n}(L)}\cong A_{H(P)}=0$ by @prop:hyperbolic-lattice, contradicting $A_L\neq0$.
:::

::: {.example #ex:stabilizing-rank-one title="Stabilizing a rank-one lattice"}

Let $R=\bZ$ and let $L=\bZ e$ with $b(e,e)=2$.
Then $b^{\sharp}\colon\bZ\to\bZ^{*}\cong\bZ$ is multiplication by $2$, so $A_L\cong\bZ/2\bZ$, generated by the class of $e/2\in L^{\#}$, with
$$
\bar b_L\bigl(\overline{e/2},\overline{e/2}\bigr)=\tfrac12+\bZ .
$$
The lattice $L$ is even, and $q_L(\overline{e/2})=\tfrac12+2\bZ$.
By @thm:stabilization-not-unimodular, $A_{S^{n}(L)}\cong\bZ/2\bZ$ for every $n\geq0$.
:::

## Witt classes {#sec-witt-classes}

::: {.example #ex:rank-one-forms title="Rank-one forms"}

For $a\in R$ write $\langle a\rangle$ for the object $(R,b_a)$ of $\mathcal B_{R,R}$ with $b_a(x,y)=axy$.
Under the isomorphism $R^{*}\cong R$, $f\mapsto f(1)$, the adjoint map of @def:polarization is multiplication by $a$.
So $\langle a\rangle$ is nondegenerate exactly when $a$ is not a zero divisor, and unimodular exactly when $a$ is a unit.
In particular $\langle1\rangle$ is unimodular over every commutative ring.
Over $R=\bZ/4\bZ$ the form $\langle2\rangle$ has $\ker b_2^{\sharp}=2\bZ/4\bZ$, so it is degenerate.
:::

::: {.definition #def:witt-class title="Witt equivalence"}

Let $R$ be a Dedekind domain.
Two unimodular $R$-lattices $X$ and $X'$ have the same *Witt class*, written $X\sim X'$, if there are metabolic unimodular $R$-lattices $Y$ and $Y'$ with
$$
X\perp Y\;\cong\;X'\perp Y'
$$
[@MH73, Def. I.7.1].
That $\sim$ is an equivalence relation, and that it is compatible with orthogonal sum and with tensor product, is @lem:witt-equivalence.
:::

::: {.lemma #lem:witt-equivalence title="Witt equivalence is a congruence"}

Let $R$ be a Dedekind domain.
Witt equivalence is an equivalence relation on isometry classes of unimodular $R$-lattices, and it is a congruence: if $X\sim X'$ and $Z\sim Z'$ then $X\perp Z\sim X'\perp Z'$ and $X\otimes Z\sim X'\otimes Z'$ [@MH73, Lem. I.7.2].
:::

::: {.proof}

Reflexivity holds with $Y=Y'=0$, the zero lattice being metabolic with lagrangian $0$ by @def:lagrangian, and symmetry is symmetry of the defining condition.
Transitivity, and compatibility with orthogonal sum and tensor product, are [@MH73, Lem. I.7.2].
:::

::: {.theorem #thm:witt-ring title="The Witt ring"}

The set $W(R)$ of Witt classes of unimodular $R$-lattices is a commutative ring with $1$, with orthogonal sum as addition and tensor product as multiplication [@MH73, Thm. I.7.3].
:::

::: {.proof}

The two operations are well defined on Witt classes by @lem:witt-equivalence, and the axioms are [@MH73, Thm. I.7.3].
Two clauses are worth naming, because they are where the book's own hypotheses enter: the tensor product of unimodular lattices is unimodular by the perfectness clause of @def:form-tensor, and the additive inverse of $[X]$ is $[X(-1)]$, exhibited by @prop:negation-is-metabolic.
:::

::: {.proposition #prop:metabolic-witt-trivial title="Metabolic lattices have Witt class zero"}

Let $X$ be a metabolic unimodular $R$-lattice.
Then $[X]=0$ in $W(R)$.
In particular $[H(P)]=0$ for every finitely generated projective $R$-module $P$.
:::

::: {.proof}

The zero lattice is metabolic, with lagrangian $0$.
Taking $Y=0$ and $Y'=X$ in @def:witt-class, both metabolic by hypothesis, the isometry $X\perp0\cong0\perp X$ of the symmetric monoidal coherence exhibits $X\sim0$, so the class of $X$ is zero in $W(R)$ of @thm:witt-ring.

The hyperbolic lattice $H(P)$ is metabolic by @prop:hyperbolic-metabolic, applied with the isomorphism $\operatorname{can}_P$ of @lem:double-dual-fg-projective.
:::

::: {.theorem #thm:witt-shift-by-summand title="Which summand shifts the Witt class"}

Let $M$ be a unimodular $R$-lattice.
On unimodular lattices, $F_M$ of @def:hyperbolic-stabilization acts on Witt classes by
$$
\bigl[F_M(X)\bigr]=[X]+[M],
$$
so it induces translation by $[M]$ on $W(R)$.
This translation is the identity if and only if $[M]=0$.
For $M=H(R)$ it is the identity, so the Witt class is constant along
$$
L\xrightarrow{\ \iota_L\ }S(L)\xrightarrow{\ \iota_{S(L)}\ }S^{2}(L)\too\cdots.
$$
:::

::: {.proof}

The orthogonal sum of unimodular lattices is unimodular by @prop:orthogonal-sum-unimodular, so $F_M$ carries unimodular lattices to unimodular lattices and induces a map on $W(R)$.
On classes it is translation by $[M]$, because $[F_M(X)]=[X\perp M]=[X]+[M]$ by the definition of addition in @thm:witt-ring.

In a group, translation by an element is the identity exactly when the element is zero, so translation by $[M]$ is the identity if and only if $[M]=0$.
For $M=H(R)$ the class is zero by @prop:metabolic-witt-trivial, so $[S(L)]=[L]$ for every unimodular $L$ and, iterating, $[S^{n}(L)]=[L]$; the class is therefore constant along the displayed tower.
:::

::: {.theorem #thm:witt-group-of-z title="The Witt ring of $\mathbb Z$"}

The signature is a ring isomorphism
$$
\sigma\colon W(\bZ)\xrightarrow{\ \sim\ }\bZ,
\qquad
\sigma\bigl[\langle1\rangle\bigr]=1,
$$
with $\langle1\rangle$ as in @ex:rank-one-forms and [@MH73, Ch. II §4].
:::

::: {.proof}

The isomorphism is [@MH73, Ch. II §4].
The route recorded here is shorter and runs through this book: with $\sigma(L)=p-q$ for the signature of @def:signature, $\sigma$ is additive and multiplicative on representatives, because orthogonality concatenates diagonalizations and a tensor product of diagonalizations is diagonal (@thm:sylvester); it vanishes on metabolic forms, a lagrangian having dimension $\tfrac12\dim$ and a totally isotropic subspace of a real form of signature $(p,q)$ at most $\min(p,q)$; so it descends.
Surjectivity is $n\langle1\rangle$ for $n\geq0$ and $m\langle-1\rangle$ for $m\leq0$.
Injectivity is the one step that uses the book's own classification rather than a computation: a unimodular lattice with $\sigma(L)=0$ is $0$, or definite of rank $0$, or indefinite with $p=q$, hence a sum of copies of $\langle1\rangle\perp\langle-1\rangle$ or of the hyperbolic plane by @thm:indefinite-unimodular-classification, both metabolic.
That classification is stated later in the volume, and the part landing page records the forward reference.
:::

::: {.example #ex:witt-classes-over-z title="Witt classes over $\mathbb Z$"}

By @thm:witt-group-of-z the class $[\langle1\rangle]$ has infinite order in $W(\bZ)$, and $\sigma[\langle-1\rangle]=-1$, so $[\langle-1\rangle]=-[\langle1\rangle]$.
The lattice $H(\bZ)$ has signature $(1,1)$, so $\sigma[H(\bZ)]=0$, in agreement with @prop:metabolic-witt-trivial.
By @thm:witt-shift-by-summand, $F_{\langle1\rangle}$ translates $W(\bZ)$ by $1$ and $F_{H(\bZ)}$ acts as the identity.
:::

::: {.theorem #thm:metabolic-is-hyperbolic title="Metabolic forms when $2$ is a unit"}

Let $R$ be a ring over which every finitely generated projective module is free and in which $2$ is a unit.
Then every metabolic unimodular form over $R$ is isometric to an orthogonal sum of copies of $H(R)$ [@MH73, Lem. I.6.3].
Conversely such an orthogonal sum is metabolic over any $R$, by @prop:hyperbolic-metabolic and the closure of metabolic forms under orthogonal sum (@prop:metabolic-closure) [@MH73, Lem. I.6.2].
:::

::: {.proof}

This is [@MH73, Lem. I.6.3].
The computation is kept because it is short and it shows where the hypothesis on $2$ is spent: nothing else in it uses that $2$ is a unit.

Let $(M,b)$ be metabolic and perfect with lagrangian $N$ and complement $W$, so $M=N\oplus W$ with $\rank N=\rank W=n$.
In an adapted basis the Gram matrix is
$$
G=\begin{pmatrix}0&A\\A^{T}&B\end{pmatrix},
$$
$A$ being the matrix of $w\mapsto b(w,-)|_{N}$ and $B$ that of $b|_{W}$.
Injectivity of $w\mapsto b(w,-)|_{N}$ makes $A$ invertible, and $\det G=(-1)^{n}\det(A)^{2}$.
Put $\psi\definedas-\tfrac12A^{-T}B$ and $P\definedas\begin{pmatrix}I&\psi\\0&I\end{pmatrix}$; then $A^{T}\psi=-\tfrac12B=\psi^{T}A$, so
$$
P^{T}GP=\begin{pmatrix}0&A\\A^{T}&\psi^{T}A+A^{T}\psi+B\end{pmatrix}=\begin{pmatrix}0&A\\A^{T}&0\end{pmatrix},
$$
and $\operatorname{diag}(A^{-T},I)$ conjugates this to $\begin{pmatrix}0&I\\I&0\end{pmatrix}$, the Gram matrix of $H(R)^{\perp n}$ by @ex:hyperbolic-plane.
The halving in $\psi$ is the whole use of the hypothesis.
:::

::: {.example #ex:metabolic-over-z title="A metabolic lattice over $\mathbb Z$"}

Let $X=\langle1\rangle\perp\langle-1\rangle=\bZ e_1\oplus\bZ e_2$, so that
$$
b(e_1,e_1)=1,\qquad b(e_2,e_2)=-1,\qquad b(e_1,e_2)=0 .
$$
The submodule $N=\bZ(e_1+e_2)$ is a direct summand, and $b(ae_1+be_2,e_1+e_2)=a-b$, so $N^{\perp}=N$ and $X$ is metabolic.
Both $X$ and $H(\bZ)$ are unimodular of signature $(1,1)$.
Since $b(e_1,e_1)=1$, the lattice $X$ is odd, while $H(\bZ)$ is even, so $X$ and $H(\bZ)$ are not isometric.
In $\bZ$ the element $2$ is not a unit, and the hypothesis of @thm:metabolic-is-hyperbolic fails.
:::

The Witt group of nonsingular $\epsilon$-symmetric forms over a ring with involution is the zero-dimensional $L$-group of that ring, and a form admitting a lagrangian is zero in it [@Ran98, Ex. 20.11].
The homological setting in which the $L$-groups of every dimension are defined is @sec-stable-duality.