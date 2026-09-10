# Bilinear and quadratic forms {#sec-form-theory}

Fix a commutative ring $R$ and an $R$-module $W$, the *value module* of the forms below.
The category $R\text{-}\mathbf{Mod}$ and extension of scalars are defined in @sec-module-categories.

::: {#def-form-presheaves}
## Bilinear and quadratic form presheaves

Let $\operatorname{Bil}_{R,W}(M)$ be the $R$-module of $R$-bilinear maps $M\times M\to W$, with pointwise operations.
Pullback along $f\colon M\to N$ sends $b$ to
$$
f^*b(x,y)=b(fx,fy),
$$
and defines a presheaf $\operatorname{Bil}_{R,W}\colon(R\text{-}\mathbf{Mod})^{\mathrm{op}}
\to R\text{-}\mathbf{Mod}$.

Let $\operatorname{Quad}_{R,W}(M)$ be the $R$-module, under pointwise operations, of maps $q\colon M\to W$ for which $q(rx)=r^2q(x)$ and
$$
b_q(x,y)=q(x+y)-q(x)-q(y)
$$
is $R$-bilinear.
Pullback defines the presheaf $\operatorname{Quad}_{R,W}\colon(R\text{-}\mathbf{Mod})^{\mathrm{op}}
\to R\text{-}\mathbf{Mod}$.
:::

::: {#def-form-categories}
## Form categories

Let $U\colon R\text{-}\mathbf{Mod}\to\mathbf{Set}$ be the forgetful functor.
Define
$$
\mathcal B_{R,W}=\int_{R\text{-}\mathbf{Mod}}(U\circ\operatorname{Bil}_{R,W}),
\qquad
\mathcal Q_{R,W}=\int_{R\text{-}\mathbf{Mod}}(U\circ\operatorname{Quad}_{R,W}).
$$
An object of $\mathcal B_{R,W}$ is a pair $(M,b)$.
A morphism $(M,b_M)\to(N,b_N)$ is an $R$-linear map $f\colon M\to N$ satisfying $f^*b_N=b_M$.
The projection to $R\text{-}\mathbf{Mod}$ is the discrete fibration of @def-category-of-elements.
The quadratic category uses the same convention.
:::

## Properties of bilinear forms {#sec-form-properties}

::: {#def-form-axioms}
For $b\colon M\times M\to W$:

- $b$ is *symmetric* if $b(x,y)=b(y,x)$;

- $b$ is *skew-symmetric* if $b(x,y)=-b(y,x)$;

- $b$ is *alternating* if $b(x,x)=0$;

- $b$ is *even* if $b(x,x)\in 2W$ for every $x$.

Alternating forms are skew-symmetric.
The converse holds when multiplication by $2$ is injective on $W$.
When $2W=W$, every bilinear form satisfies the evenness condition; quadratic refinements retain additional information in the discriminant setting.
:::

::: {#def-polarization}
## The adjoint maps and the radicals

The bilinear form $b$ determines two $R$-linear maps to $\operatorname{Hom}_R(M,W)$,
$$
b^\sharp(x)(y)=b(x,y),
\qquad
{}^\sharp b(y)(x)=b(x,y).
$$
Their kernels are the *left radical* and the *right radical*
$$
\operatorname{rad}_{\mathrm L}(M)=\{x\in M\mid b(x,M)=0\},
\qquad
\operatorname{rad}_{\mathrm R}(M)=\{y\in M\mid b(M,y)=0\}.
$$
The form is *left nondegenerate* if $b^\sharp$ is injective, *right nondegenerate* if ${}^\sharp b$ is injective, and *nondegenerate* if both hold.
It is *perfect* if $b^\sharp$ and ${}^\sharp b$ are isomorphisms.
Perfect forms are nondegenerate; the converse requires additional hypotheses.

If $b$ is symmetric then ${}^\sharp b=b^\sharp$, and if $b$ is skew-symmetric then ${}^\sharp b=-b^\sharp$.
In both cases the two radicals coincide, are written $\operatorname{rad}(M)$, and the one condition $\operatorname{rad}(M)=0$ is nondegeneracy.

In [@MH73] a module equipped with a perfect form is called an *inner product space*.
:::

::: {#exm-two-radicals}
**Example.** Let $b$ be the form on $R^{2}$ with Gram matrix $\left(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\right)$ in the basis $e_1,e_2$.
Then $b(e_1,w)=w_1+2w_2$ while $b(w,e_1)=w_1+3w_2$, so the two conditions $b(e_1,w)=0$ and $b(w,e_1)=0$ cut out different submodules of $R^{2}$.
:::

::: {#def-orthogonal-sum}
## Orthogonal sum

The orthogonal sum of $(M,b_M)$ and $(N,b_N)$ is
$$
(M,b_M)\perp(N,b_N)
=
(M\oplus N,b_M\oplus b_N),
$$
where the mixed terms vanish.
With zero module as unit and the standard associativity, symmetry, and unit isomorphisms, this defines a symmetric monoidal structure on $\mathcal B_{R,W}$.
The quadratic form category has the analogous orthogonal sum.
:::

## Orthogonality {#sec-orthogonality}

::: {#def-orthogonal-complement}
## Orthogonal complements and isotropy

For a submodule $N\subseteq M$ set
$$
N^{\perp_{\mathrm L}}=\{x\in M\mid b(x,N)=0\},
\qquad
N^{\perp_{\mathrm R}}=\{x\in M\mid b(N,x)=0\}.
$$
When $b$ is symmetric or skew-symmetric these agree and are written $N^{\perp}$.

An element $x\in M$ is *isotropic* if $b(x,x)=0$, and $b$ is *anisotropic* if $0$ is its only isotropic element.
A submodule $N$ is *totally isotropic* if $b|_{N\times N}=0$, equivalently $N\subseteq N^{\perp}$.
The radical of the restricted form is
$$
\operatorname{rad}(N)=N\cap N^{\perp},
$$
so $N$ is totally isotropic exactly when $\operatorname{rad}(N)=N$ and the restriction $b|_{N\times N}$ is nondegenerate exactly when $N\cap N^{\perp}=0$.
:::

::: {#thm-orthogonal-decomposition}
## Orthogonal decomposition

Let $b$ be symmetric or skew-symmetric on $M$ and let $N\subseteq M$ be a submodule on which $b$ restricts to a perfect form.
Then $M=N\oplus N^{\perp}$ and the sum is orthogonal, so
$$
(M,b)\cong(N,b|_N)\perp(N^{\perp},b|_{N^{\perp}})
$$
in the sense of @def-orthogonal-sum [@MH73, I §3.1].
If $x_1,\dots,x_k\in M$ have invertible Gram matrix $\bigl(b(x_i,x_j)\bigr)$, then they are linearly independent and this applies to the free submodule they span [@MH73, I §3.2].
:::

::: {#prp-quotient-form}
## Forms on quotients

Let $b$ be symmetric on $M$ and let $N\subseteq M$ be a submodule.

The rule $\bar b(x+N,y+N)=b(x,y)$ defines a form on $M/N$ if and only if $N\subseteq\operatorname{rad}(M)$.
For well-definedness one needs $b(x+n,y+n')=b(x,y)$ for all $n,n'\in N$; taking $n'=0$ gives $b(n,y)=0$ for every $y\in M$, which is $N\subseteq\operatorname{rad}(M)$, and that condition conversely kills all three correction terms.

The same rule defines a form on $N^{\perp}/N$ whenever $N$ is totally isotropic: for $x,y\in N^{\perp}$ and $n,n'\in N$,
$$
b(x+n,y+n')=b(x,y)+b(x,n')+b(n,y)+b(n,n')=b(x,y).
$$

Taking $N=\operatorname{rad}(M)$ gives the *radical quotient* $M/\operatorname{rad}(M)$, whose induced form is nondegenerate.
:::

## Gram matrices and the determinant {#sec-gram-determinant}

::: {#prp-gram-matrix-free-module}
## Gram matrix

Let $M$ be free as an $R$-module on $E=\{e_i\}_{i\in I}$, and let $b$ be a bilinear form on $M$ with values in $R$.
The *Gram matrix* of $b$ with respect to $E$ is the family $G_{ij}=b(e_i,e_j)$ indexed by $I\times I$.
If $v=\sum_i a_i e_i$ and $w=\sum_j c_j e_j$, then
$$
b(v,w)=\sum_{i,j\in I} a_i\, G_{ij}\, c_j,
$$
a finite sum by finite support of the coordinates.
Every family $(G_{ij})_{i,j\in I}$ in $R$ arises uniquely in this way.
:::

::: {#prp-gram-congruence}
## Congruence

Let $M$ be free with basis $e_1,\dots,e_n$ and Gram matrix $G=\bigl(b(e_i,e_j)\bigr)$ as in @prp-gram-matrix-free-module.
Let $e'_1,\dots,e'_n$ be a second basis and let $P$ be the invertible matrix whose $j$-th column holds the coordinates of $e'_j$ in the basis $e$.
Then the Gram matrix in the basis $e'$ is
$$
G'=P^{\mathsf T}GP,
$$
and two Gram matrices present isomorphic forms exactly when they are congruent in this sense [@MH73, I §2.3].
:::

::: {#def-cartan-matrix}
## The Cartan matrix

Let $b$ be a symmetric bilinear form on $M$ with values in $R$, and let $\alpha_1,\dots,\alpha_\ell$ be an ordered family in $M$ with each $b(\alpha_j,\alpha_j)$ invertible in $R$.
The *Cartan matrix* of the family is
$$
A_{ij}=\frac{2\,b(\alpha_i,\alpha_j)}{b(\alpha_j,\alpha_j)} ,
$$
normalized by the second index.
For the simple roots of a root system these entries are the *Cartan integers* [@Hum72, §11.1].

Write $G$ for the Gram matrix of the family, as in @prp-gram-matrix-free-module, and put $d_j=b(\alpha_j,\alpha_j)/2$.
Then
$$
A=G\cdot\operatorname{diag}\!\left(\tfrac{2}{G_{jj}}\right),
\qquad
G_{ij}=d_j\,A_{ij}.
$$

Normalizing by the first index instead produces the transpose of $A$, and the second identity then reads $G_{ij}=d_iA_{ij}$.
The two conventions give transposed matrices and different symmetrization indices; this book uses the one displayed above.

$G$ is symmetric, while $A$ need not be, so a Cartan matrix with $d_i\neq d_j$ is not a Gram matrix.
Take $\ell=2$ with
$$
G=\begin{pmatrix}-2&2\\2&-4\end{pmatrix},
\qquad
d=(-1,-2),
\qquad
A=\begin{pmatrix}2&-1\\-2&2\end{pmatrix}.
$$
Here $d_2A_{12}=(-2)(-1)=2=G_{12}$, whereas $d_1A_{12}=(-1)(-1)=1$, so only the second index recovers $G$ from $A$.
:::

::: {#def-determinant-class}
## The determinant

Write $R^{\bullet}$ for the group of units of $R$ and $(R^{\bullet})^{2}$ for the subgroup of squares of units.
By @prp-gram-congruence the determinant of a Gram matrix changes by the square of a unit under change of basis, so a perfect form on a free module has a well-defined
$$
\det(b)\in R^{\bullet}/(R^{\bullet})^{2},
$$
and a general form on a free module has a well-defined class in the quotient monoid $R/(R^{\bullet})^{2}$ [@MH73, I §2.5].
Under orthogonal sum the rank adds and the determinant multiplies [@MH73, I §3].
:::

::: {#prp-alternating-gram}
## Alternating forms in a basis

Let $b$ be skew-symmetric on a free module with basis $e_1,\dots,e_n$.
Then $b$ is alternating if and only if $b(e_i,e_i)=0$ for every $i$.
For $x=\sum_ix_ie_i$,
$$
b(x,x)=\sum_i x_i^{2}\,b(e_i,e_i)+\sum_{i<j}x_ix_j\bigl(b(e_i,e_j)+b(e_j,e_i)\bigr),
$$
and skew-symmetry kills the second sum.

**Remark.** The symmetric form on $\mathbb Z^{2}$ with Gram matrix $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ has vanishing diagonal and $b(e_1+e_2,e_1+e_2)=2$.
:::

## Tensor product and twisting {#sec-form-tensor}

::: {#def-form-tensor}
## Tensor product of forms

Let $b_M$ have value module $W_M$ and $b_N$ have value module $W_N$.
There is exactly one bilinear map
$$
b_M\otimes b_N\colon (M\otimes_RN)\times(M\otimes_RN)\longrightarrow W_M\otimes_RW_N
$$
with
$$
(b_M\otimes b_N)(x\otimes u,\;y\otimes v)=b_M(x,y)\otimes b_N(u,v),
$$
obtained by factoring the four-linear map $(x,u,y,v)\mapsto b_M(x,y)\otimes b_N(u,v)$ through the tensor products [@MH73, I §5.1].
For $W_M=W_N=R$ the value module is $R$.

Call a form $\varepsilon$-symmetric when $b(x,y)=\varepsilon\,b(y,x)$, so that $1$-symmetric means symmetric and $(-1)$-symmetric means skew-symmetric.
The tensor product of an $\varepsilon$-symmetric and an $\varepsilon'$-symmetric form is $\varepsilon\varepsilon'$-symmetric [@MH73, I §5.2].
If both forms are perfect and both modules are finitely generated projective, the tensor product is perfect [@MH73, I §5.3].
:::

::: {#prp-tensor-gram}
## Gram matrix and determinant of a tensor product

If $M$ and $N$ are free of ranks $m$ and $n$ with Gram matrices $G_M$ and $G_N$, the Gram matrix of $b_M\otimes b_N$ in the product basis is the Kronecker product $G_M\otimes G_N$, and
$$
\det(b_M\otimes b_N)=\det(b_M)^{\,n}\det(b_N)^{\,m}.
$$
:::

::: {#def-form-twist}
## Twisting

For $\lambda\in R$ the *twist* $b(\lambda)$ of $(M,b)$ is the form $\lambda b$ on the same module, written $M(\lambda)$.
Its Gram matrix in a basis is $\lambda G$, its adjoint maps are $\lambda\,b^{\sharp}$ and $\lambda\,{}^{\sharp}b$, and on a free module of rank $n$
$$
\det\bigl(b(\lambda)\bigr)=\lambda^{\,n}\det(b).
$$

A morphism $f$ of @def-form-categories satisfies $f^{*}b_N=b_M$ and hence $f^{*}(\lambda b_N)=\lambda b_M$, so $(-)(\lambda)$ is an endofunctor of $\mathcal B_{R,W}$ which is the identity on underlying maps.
For $\lambda$ a unit it is an isomorphism of categories with inverse $(-)(\lambda^{-1})$, and $(-)(-1)$ is an involution.
:::

## Signature at a real place {#sec-signature}

::: {#def-signature}
## Signature

Let $F$ be an ordered field and let $b$ be a symmetric bilinear form on a finite-dimensional $F$-vector space $V$.
Write $p$ for the greatest dimension of a subspace on which $b$ is positive definite, $q$ for the greatest dimension of a subspace on which $b$ is negative definite, and $r=\dim\operatorname{rad}(V)$.
The triple $(p,q,r)$ is the *signature* of $b$.

For an $R$-module with form and a ring embedding $\sigma\colon R\hookrightarrow\mathbb R$, the signature of $(M,b)$ at $\sigma$ is the signature of the base change along $\sigma$ of @def-module-base-change.
For $R=\mathbb Z$ there is one such embedding and the qualifier is omitted.

For a nondegenerate form $r=0$, and the signature is then written as the pair $(p,q)$.
:::

::: {#thm-sylvester}
## Sylvester's law of inertia

Let $F$ be an ordered field and let $b$ be a perfect symmetric bilinear form on a finite-dimensional $F$-vector space $V$.
Then $V\cong V^{+}\perp V^{-}$ with $b$ positive definite on $V^{+}$ and negative definite on $V^{-}$, and the two dimensions depend only on the isomorphism class of $(V,b)$: $\dim V^{+}$ is the greatest dimension of a positive definite subspace of $V$ [@MH73, III §2.5].
So the signature of @def-signature is $(\dim V^{+},\dim V^{-},0)$ and $p+q=\dim V$.

For a degenerate $b$, choose a complement $N$ to $\operatorname{rad}(V)$ in $V$.
Every pairing involving $\operatorname{rad}(V)$ vanishes, so $V\cong\operatorname{rad}(V)\perp N$ and $b|_N$ is nondegenerate, hence perfect because $N$ is finite dimensional.
Applying the above to $N$ gives $V\cong V^{+}\perp V^{-}\perp\operatorname{rad}(V)$, so $p+q+r=\dim V$ in every case.
:::

::: {#def-definiteness}
## Definiteness

Let $b$ be a symmetric bilinear form of signature $(p,q,r)$ and set $n=p+q+r$.
Then $b$ is

- *degenerate* if $r>0$;

- *positive definite* if $(p,q,r)=(n,0,0)$, and *negative definite* if $(p,q,r)=(0,n,0)$;

- *definite* if it is positive definite or negative definite;

- *indefinite* if $p\geq1$ and $q\geq1$;

- *hyperbolic*, or of Lorentzian signature, if $n\geq2$ and $(p,q,r)=(1,n-1,0)$;

- *parabolic* if $n\geq2$ and $(p,q,r)=(0,n-1,1)$.

**Convention.** Root lattices are taken negative definite here, so the forms on $A_n$, $D_n$ and $E_n$ are negative definite and the hyperbolic signature is $(1,n-1,0)$.
:::

## Isotropy and Witt decomposition {#sec-witt}

::: {#def-hyperbolic-plane}
## Rank one forms, the hyperbolic plane, and split forms

For a unit $u\in R^{\bullet}$ write $\langle u\rangle$ for the free module of rank $1$ on a generator $e$ with $b(e,e)=u$.
Then $\langle u\rangle\cong\langle u'\rangle$ if and only if $u'=\alpha^{2}u$ for some $\alpha\in R^{\bullet}$ [@MH73, I §2.4].

The *hyperbolic plane* $U$ over $R$ is the free module on $e,f$ with
$$
b(e,e)=b(f,f)=0,\qquad b(e,f)=b(f,e)=1,
$$
so its Gram matrix is $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$, its form is perfect and even, and its signature over an ordered field is $(1,1,0)$.

A perfect symmetric form on $M$ is *split* if $M$ has a direct summand $N$ with $N=N^{\perp}$ [@MH73, I §6.1].
Over a ring whose finitely generated projective modules are free and in which $2$ is a unit, a split form is an orthogonal sum of hyperbolic planes [@MH73, I §6.3]; this applies to a field of characteristic other than $2$.
:::

::: {#def-witt-index}
## Witt index

The *Witt index* $i(V)$ of a perfect symmetric form on a finite-dimensional vector space $V$ over a field is the greatest dimension of a totally isotropic subspace.
It satisfies
$$
0\leq i(V)\leq\tfrac12\dim V,
$$
with $i(V)=0$ exactly when the form is anisotropic and $i(V)=\tfrac12\dim V$ exactly when the form is split [@MH73, III §1.2].
:::

::: {#thm-witt-decomposition}
## Witt decomposition

Every perfect symmetric form on a finite-dimensional vector space $V$ over a field $F$ decomposes as
$$
V\cong S\perp A
$$
with $S$ split and $A$ anisotropic [@MH73, III §1.1], and $A$ is determined up to isomorphism by the Witt class of $V$ [@MH73, III §1.7].
Here $\dim S=2\,i(V)$ and $\dim A=\dim V-2\,i(V)$.
:::

::: {#exm-witt-index-over-Q}
## Witt index and signature

Over a real closed field every positive element is a square, so by @thm-sylvester a perfect symmetric form of signature $(p,q,0)$ is $p\langle1\rangle\perp q\langle-1\rangle$.
Each summand $\langle1\rangle\perp\langle-1\rangle$ is split [@MH73, I §6.1], so the Witt index is $\min(p,q)$.

Over $\mathbb Q$ the Witt index can be strictly smaller.
The form $x^{2}+y^{2}-3z^{2}$ has signature $(2,1,0)$, so $\min(p,q)=1$, and it is anisotropic over $\mathbb Q$, so its Witt index is $0$.
For a primitive integral solution of $x^{2}+y^{2}=3z^{2}$, reduction modulo $3$ forces $3\mid x$ and $3\mid y$ because $-1$ is not a square modulo $3$; then $9\mid3z^{2}$ gives $3\mid z$, contradicting primitivity.
:::

::: {#rem-three-integers}
**Remark.** Three integers are attached to a nondegenerate symmetric form over an ordered field, and they are distinct invariants.
The pair $(p,q)$ is the signature of @def-signature.
The integer $p-q$ is called the signature of the form in [@MH73, III §2.5], where it is the value of a ring homomorphism from the Witt ring to $\mathbb Z$.
The Witt index of @def-witt-index is a third quantity, equal to $\min(p,q)$ over a real closed field and smaller over $\mathbb Q$ in the case above.
:::

## Diagonal and polarization {#sec-polarization-functors}

::: {#def-polarization-functors}
Diagonal and polarization define natural transformations
$$
\operatorname{diag}\colon\operatorname{SymBil}_{R,W}
\Longrightarrow\operatorname{Quad}_{R,W},
\qquad
\operatorname{polar}\colon\operatorname{Quad}_{R,W}
\Longrightarrow\operatorname{SymBil}_{R,W},
$$
with
$$
\operatorname{diag}(b)(x)=b(x,x),
\qquad
\operatorname{polar}(q)(x,y)=q(x+y)-q(x)-q(y).
$$
Here $\operatorname{SymBil}_{R,W}$ is the $R$-submodule-valued presheaf of symmetric bilinear forms.
The composites satisfy
$$
\operatorname{polar}(\operatorname{diag}(b))=2b,
\qquad
\operatorname{diag}(\operatorname{polar}(q))=2q.
$$
If $2$ is invertible on $W$, division by $2$ gives inverse equivalences between symmetric bilinear forms and quadratic forms.
For a general value module, they define parallel functors whose composites are multiplication by $2$.

For discriminant forms, the isomorphism
$$
\mathbb Q/2\mathbb Z\longrightarrow\mathbb Q/\mathbb Z,
\qquad w\longmapsto w/2,
$$
followed by polarization gives the bilinearization functor from $\mathbb Q/2\mathbb Z$-valued quadratic forms to $\mathbb Q/\mathbb Z$-valued symmetric bilinear forms.
:::

Bilinear forms on the underlying module of an associative unital $R$-algebra are treated in @sec-algebra-module-forms: module bilinear forms are $\operatorname{Hom}_{R\text{-}\mathbf{Mod}}(M\otimes_R M,R)$, and algebra bilinear forms are $\operatorname{Hom}_{R\text{-}\mathbf{Alg}}(A\otimes_R A,R)$ with the tensor product taken in $R\text{-}\mathbf{Alg}$.
