# Bilinear and quadratic forms {#sec-form-theory}

Fix a commutative ring $R$ and an $R$-module $W$, the *value module* of the forms below.
The category $R\text{-}\mathbf{Mod}$ and extension of scalars are defined in @sec-module-categories.

::: {.definition #def:form-presheaves title="Bilinear and quadratic form presheaves"}

For $M\in R\text{-}\mathbf{Mod}$, write
$$
T_R(M)_2\definedas M\tensor_RM
$$
for the degree-two homogeneous summand of the tensor algebra $T_R(M)$. Define
$$
\Bil_{R,W}(M)
\definedas
\Hom_{R\text{-}\mathbf{Mod}}\qty{T_R(M)_2,W}.
$$
For $f\colon M\to N$, pullback is
$$
f^*\colon\Bil_{R,W}(N)\too\Bil_{R,W}(M),
\qquad
b\longmapsto b\circ(f\tensor_Rf),
$$
so
$$
\Bil_{R,W}\colon(R\text{-}\mathbf{Mod})^{\opop}\too R\text{-}\mathbf{Mod}
$$
is a presheaf.

For $M\in R\text{-}\mathbf{Mod}$, let $\Gamma_R^2(M)$ be the quotient of the free $R$-module on symbols $[x]$, $x\in M$, by the relations
$$
\begin{aligned}
[rx]&=r^2[x],\\
[x+y+z]-[x+y]-[x+z]-[y+z]+[x]+[y]+[z]&=0,\\
[rx+y]-[rx]-[y]&=r\qty{[x+y]-[x]-[y]}.
\end{aligned}
$$
The map $\gamma_M\colon M\to\Gamma_R^2(M)$, $x\mapsto[x]$, is universal among maps $q\colon M\to W$ satisfying $q(rx)=r^2q(x)$ and having $R$-bilinear polarization.
Hence
$$
\operatorname{Quad}_{R,W}(M)
\definedas
\Hom_{R\text{-}\mathbf{Mod}}\qty{\Gamma_R^2(M),W}.
$$
For $f\colon M\to N$, the morphism $\Gamma_R^2(f)[x]=[f(x)]$ gives pullback by precomposition, so
$$
\operatorname{Quad}_{R,W}\colon(R\text{-}\mathbf{Mod})^{\opop}\too R\text{-}\mathbf{Mod}
$$
is a presheaf.
:::

::: {.definition #def:form-categories title="Form categories"}

For fixed value module $W$, define $\mathcal B_{R,W}$ to have pairs $(M,b)$ with $b\in\Bil_{R,W}(M)$ and morphisms
$$
f\in\Hom_{R\text{-}\mathbf{Mod}}(M,N)
$$
satisfying
$$
b_M=b_N\circ(f\tensor_Rf).
$$
Define $\mcq_{R,W}$ similarly from $\operatorname{Quad}_{R,W}$.

Define the variable-value category $\mathbf{BilMod}_R$ to have triples $(M,W,b)$ and morphisms
$$
(f,u)\colon(M,W,b_M)\too(N,V,b_N)
$$
with $f\colon M\to N$, $u\colon W\to V$ in $R\text{-}\mathbf{Mod}$ and
$$
u\circ b_M=b_N\circ(f\tensor_Rf).
$$
The projection
$$
p_{\mathrm{Bil}}\colon\mathbf{BilMod}_R\too R\text{-}\mathbf{Mod},
\qquad
(M,W,b)\longmapsto W
$$
has fibre $p_{\mathrm{Bil}}^{-1}(W)=\mathcal B_{R,W}$.
Define $\mathbf{QuadMod}_R$ and $p_{\mathrm{Quad}}$ analogously using $\Gamma_R^2(M)$; its fibre over $W$ is $\mcq_{R,W}$.

The category-of-elements presentations of $\mathcal B_{R,W}$ and $\mcq_{R,W}$ are the fixed-value fibres of these projections, not additional form categories.
Kernel, cokernel, image, and exact-sequence notation below is always taken in the explicitly named form category.
:::

::: {.definition #def:form-axioms title="Symmetry, alternation, and evenness"}

Let $U\colon R\text{-}\mathbf{Mod}\to\mathbf{Set}$ be the forgetful functor and let
$$
\Delta_M\colon U(M)\too U(M\tensor_RM),
\qquad
x\longmapsto x\tensor x
$$
be the natural diagonal of underlying sets. For a bilinear map $b\colon M\tensor_RM\to W$, define
$$
q_b
\definedas
U(b)\circ\Delta_M\colon U(M)\too U(W).
$$
Let
$$
\tau\colon M\tensor_RM\isoto M\tensor_RM,
\qquad
x\tensor y\longmapsto y\tensor x.
$$

- $b$ is **symmetric** when $b\circ\tau=b$.

- $b$ is **skew-symmetric** when $b\circ\tau=-b$.

- $b$ is **alternating** when $q_b=0$.

- Let multiplication by $2$ have image factorization
  $$
  W\xrightarrow{2}W
  =
  W\twoheadrightarrow 2W\injects W.
  $$
  The form $b$ is **even** when there is a quadratic map $\widetilde q_b\in\operatorname{Quad}_{R,2W}(M)$ for which
  $$
  q_b
  =
  U(2W\injects W)\circ U(\widetilde q_b).
  $$

Alternating forms are skew-symmetric.
The converse holds when multiplication by $2$ on $W$ is a monomorphism.
When multiplication by $2$ is an epimorphism, every bilinear form is even; quadratic refinements retain additional information.
:::

::: {.definition #def:polarization title="Adjoints, radicals, and nondegeneracy"}

For a bilinear module $(M,W,b)$ define
$$
b^\sharp\colon M\too\Hom_R(M,W),
\qquad
{}^\sharp b\colon M\too\Hom_R(M,W)
$$
by
$$
b^\sharp(x)(y)=b(x,y),
\qquad
{}^\sharp b(y)(x)=b(x,y).
$$
Define the left and right radicals and coradicals by the exact sequences
$$
0\too\radic_{\mathrm L}(M)
\too M
\xrightarrow{b^\sharp}
\Hom_R(M,W)
\too\operatorname{corad}_{\mathrm L}(M)
\too0
$$
and
$$
0\too\radic_{\mathrm R}(M)
\too M
\xrightarrow{{}^\sharp b}
\Hom_R(M,W)
\too\operatorname{corad}_{\mathrm R}(M)
\too0.
$$
The form is **nondegenerate** exactly when
$$
\radic_{\mathrm L}(M)=0=\radic_{\mathrm R}(M).
$$
It is **perfect** exactly when
$$
\radic_{\mathrm L}(M)=\radic_{\mathrm R}(M)
=\operatorname{corad}_{\mathrm L}(M)=\operatorname{corad}_{\mathrm R}(M)=0.
$$

If $b$ is symmetric, $b^\sharp={}^\sharp b$, so the two exact sequences are the same and the common radical and coradical are written $\radic(M)$ and $\operatorname{corad}(M)$.
If $b$ is skew-symmetric, ${}^\sharp b=-b^\sharp$; multiplication by $-1$ on $\Hom_R(M,W)$ induces the unique isomorphisms between the corresponding kernels and cokernels.
:::

::: {.definition #def:orthogonal-sum title="Orthogonal sum"}

Let $\iota_M\colon M\to M\oplus N$ and $\iota_N\colon N\to M\oplus N$ be the biproduct injections.
The orthogonal sum $(M,b_M)\perp(N,b_N)$ is the unique bilinear module $(M\oplus N,b_{M\perp N})$ satisfying
$$
\begin{aligned}
b_{M\perp N}\circ(\iota_M\tensor\iota_M)&=b_M,
&
b_{M\perp N}\circ(\iota_N\tensor\iota_N)&=b_N,\\
b_{M\perp N}\circ(\iota_M\tensor\iota_N)&=0,
&
b_{M\perp N}\circ(\iota_N\tensor\iota_M)&=0.
\end{aligned}
$$
The biproduct coherence morphisms of $R\text{-}\mathbf{Mod}$ are form-preserving for these forms, giving the symmetric monoidal category
$$
\qty{
\mathcal B_{R,W},
\perp,
(0,0),
a^\perp,
\lambda^\perp,
\rho^\perp,
\sigma^\perp
}.
$$
The quadratic form category has the analogous orthogonal sum.
:::

## Orthogonality {#sec-orthogonality}

::: {.definition #def:orthogonal-complement title="Left and right orthogonal complements"}

Let $(M,W,b)$ be a bilinear module and let $\iota\colon T\injects M$ be a monomorphism of $R$-modules.
Define
$$
\lambda_{\iota}^{\mathrm L}\colon
M
\too
\Hom_R(T,W),
\qquad
\lambda_{\iota}^{\mathrm L}(x)(t)
=
b(x,\iota(t)),
$$
and
$$
\lambda_{\iota}^{\mathrm R}\colon
M
\too
\Hom_R(T,W),
\qquad
\lambda_{\iota}^{\mathrm R}(x)(t)
=
b(\iota(t),x).
$$
Define the **left orthogonal complement** \({}^{\perp_b}T\), the **right orthogonal complement** \(T^{\perp_b}\), and their coradicals by the exact sequences
$$
0
\too
{}^{\perp_b}T
\xrightarrow{\kappa_{\iota}^{\mathrm L}}
M
\xrightarrow{\lambda_{\iota}^{\mathrm L}}
\Hom_R(T,W)
\too\operatorname{corad}_{\mathrm L}(\iota)
\too0
$$
and
$$
0
\too
T^{\perp_b}
\xrightarrow{\kappa_{\iota}^{\mathrm R}}
M
\xrightarrow{\lambda_{\iota}^{\mathrm R}}
\Hom_R(T,W)
\too\operatorname{corad}_{\mathrm R}(\iota)
\too0.
$$
If $b$ is symmetric, then $\lambda_{\iota}^{\mathrm L}=\lambda_{\iota}^{\mathrm R}$; the universal properties of kernel and cokernel give unique isomorphisms
$$
{}^{\perp_b}T\isoto T^{\perp_b},
\qquad
\operatorname{corad}_{\mathrm L}(\iota)\isoto\operatorname{corad}_{\mathrm R}(\iota)
$$
commuting with the four structure morphisms above.

The subobject $\iota$ is **isotropic** when
$$
\iota^*b=0.
$$
Equivalently, there are unique lifts $\ell_{\iota}^{\mathrm L}$ and $\ell_{\iota}^{\mathrm R}$ in the commuting triangles
```tikzcd
& {}^{\perp_b}T \arrow[d,"\kappa_{\iota}^{\mathrm L}"]
&
& T^{\perp_b} \arrow[d,"\kappa_{\iota}^{\mathrm R}"] \\
T \arrow[ur,dashed,"\ell_{\iota}^{\mathrm L}"] \arrow[r,"\iota"']
& M
&
T \arrow[ur,dashed,"\ell_{\iota}^{\mathrm R}"] \arrow[r,"\iota"']
& M
```
so that
$$
\kappa_{\iota}^{\mathrm L}\circ\ell_{\iota}^{\mathrm L}=\iota,
\qquad
\kappa_{\iota}^{\mathrm R}\circ\ell_{\iota}^{\mathrm R}=\iota.
$$
:::

::: {.definition #def:nondegenerate-reduction title="Nondegenerate reduction"}

Let $B$ be a symmetric bilinear module and let
$$
\rho_B\colon\radic(B)\too B
$$
be its radical morphism.
Define
$$
B^{\mathrm{nd}}
\definedas
\coker_{\mathbf{BilMod}_R}(\rho_B).
$$
This defines the **nondegenerate-reduction endofunctor**
$$
(-)^{\mathrm{nd}}\colon
\mathbf{BilMod}_R
\too
\mathbf{BilMod}_R.
$$

If $L$ is nondegenerate and
$$
\iota\colon T\injects L
$$
is an isotropic sublattice over the commutative ring $R$, then in lattice-theoretic notation
$$
T^\perp
\definedas
\bigl(T^\perp_{\mathbf{BilMod}_R}\bigr)^{\mathrm{nd}}.
$$
Thus the orthogonal complement in the lattice category is the nondegenerate reduction of the right orthogonal-complement kernel in $\mathbf{BilMod}_R$.
:::

::: {.theorem #thm:orthogonal-decomposition title="Orthogonal decomposition"}

Let $(M,W,b)$ be symmetric and let
$$
\iota\colon T\injects M
$$
be a bilinear submodule on which the restricted form is perfect.
Then the canonical orthogonal-sum morphism
$$
T\perp T^\perp
\too
M
$$
is an isomorphism [@MH73, I §3.1].
:::

::: {.proof}

Write $b_T$ for the restricted form, which is symmetric and perfect by hypothesis, so that $b_T^{\sharp}\colon T\to\Hom_R(T,W)$ is an isomorphism by @def:polarization.
Here $T^{\perp}$ is the right orthogonal complement of @def:orthogonal-complement, carrying the restricted form; it is not the nondegenerate reduction of @def:nondegenerate-reduction, which is defined only for a nondegenerate ambient lattice.
The canonical morphism sends $(t,t')\mapsto\iota(t)+t'$.
For $t'\in T^{\perp_b}$ and $t\in T$ one has $b(\iota(t),t')=0$ by @def:orthogonal-complement, and $b(t',\iota(t))=0$ by symmetry, so the cross terms vanish and the map is a morphism of bilinear modules from $T\perp T^\perp$.

It is injective: if $\iota(t)+t'=0$ then $\iota(t)=-t'\in T\cap T^{\perp_b}$, and $T\cap T^{\perp_b}$ is the kernel of $b_T^{\sharp}$, which vanishes by perfection and injectivity of $\iota$.

It is surjective: for $m\in M$ the functional $t\mapsto b(m,\iota(t))$ lies in $\Hom_R(T,W)$, so by perfection there is $t_0\in T$ with $b(t_0,\iota(t))=b(m,\iota(t))$ for every $t\in T$; then $b(\iota(t),m-\iota(t_0))=b(m,\iota(t))-b(t_0,\iota(t))=0$, so $m-\iota(t_0)\in T^{\perp_b}$ and $m$ is the image of $(t_0,m-\iota(t_0))$.

A bijective morphism of bilinear modules is an isomorphism, and no hypothesis on $M$ was used: neither nondegeneracy nor freeness.
:::

## Gram matrices and the determinant {#sec-gram-determinant}

::: {.proposition #prop:gram-matrix-free-module title="Gram matrix"}

Let $M$ be free as an $R$-module on $E=\{e_i\}_{i\in I}$, and let $b$ be a bilinear form on $M$ with values in $R$.
The *Gram matrix* of $b$ with respect to $E$ is the family $G_{ij}=b(e_i,e_j)$ indexed by $I\times I$.
If $v=\Sum_i a_i e_i$ and $w=\Sum_j c_j e_j$, then
$$
b(v,w)=\Sum_{i,j\in I} a_i\, G_{ij}\, c_j,
$$
a finite sum by finite support of the coordinates.
Every family $(G_{ij})_{i,j\in I}$ in $R$ arises uniquely in this way.
:::

::: {.proof}

Both $v$ and $w$ are finite linear combinations, so $b(v,w)=\Sum_{i\in I}\Sum_{j\in I}a_ic_j\,b(e_i,e_j)$ is a finite sum of the displayed form, and bilinearity is what permits the rearrangement; this is the first claim.

For the second, fix a family $G$ and define $b(v,w)\definedas\Sum_{i,j}a_ic_jG_{ij}$.
The double sum has finitely many nonzero terms because $v$ and $w$ have finite support, so $b$ is well defined, and it is bilinear in $a$ and $c$; its Gram matrix is $G$ by the first claim applied to $v=e_i$ and $w=e_j$.
Uniqueness: a bilinear form is determined by its values on pairs of basis vectors, since those values determine it on finite combinations as displayed.
So the map from bilinear forms to families is a bijection.
:::

::: {.proposition #prop:gram-congruence title="Congruence"}

Let $M$ be free with basis $e_1,\dots,e_n$ and Gram matrix $G=\bigl(b(e_i,e_j)\bigr)$ as in @prop:gram-matrix-free-module.
Let $e'_1,\dots,e'_n$ be a second basis and let $P$ be the invertible matrix whose $j$-th column holds the coordinates of $e'_j$ in the basis $e$.
Then the Gram matrix in the basis $e'$ is
$$
G'=P^{\mathsf T}GP,
$$
and two Gram matrices present isomorphic forms exactly when they are congruent in this sense [@MH73, I §2.3].
:::

::: {.proof}

The $j$-th column of $P$ holds the coordinates of $e'_j$, that is, $e'_j=\Sum_i P_{ij}e_i$.
Then
$$
G'_{ij}=b(e'_i,e'_j)=b\qty{\Sum_k P_{ki}e_k,\ \Sum_l P_{lj}e_l}=\Sum_{k,l}P_{ki}\,G_{kl}\,P_{lj}=(P^{\mathsf T}GP)_{ij}
$$
by bilinearity, which is the displayed formula.

Conversely, let $P$ be invertible and define $e'_j\definedas\Sum_iP_{ij}e_i$; invertibility of $P$ makes $e'$ a basis, since the equations $e'_j=\Sum_iP_{ij}e_i$ solve for $e$ through $P^{-1}$.
The computation above shows that $G'=P^{\mathsf T}GP$ is the Gram matrix of the same form $b$ in the basis $e'$.
So congruent matrices are the Gram matrices of one form in two bases, and by the same computation every pair of Gram matrices of one form in two bases is congruent, the change-of-basis matrix being invertible as it is a change of basis.
:::

::: {.definition #def:cartan-matrix title="The Cartan matrix"}

Let $b$ be a symmetric bilinear form on $M$ with values in $R$, and let $\alpha_1,\dots,\alpha_\ell$ be an ordered family in $M$ with each $b(\alpha_j,\alpha_j)$ invertible in $R$.
The *Cartan matrix* of the family is
$$
A_{ij}=\frac{2\,b(\alpha_i,\alpha_j)}{b(\alpha_j,\alpha_j)} ,
$$
normalized by the second index.
For the simple roots of a root system these entries are the *Cartan integers* [@Hum72, §11.1].

Write $G$ for the Gram matrix of the family, as in @prop:gram-matrix-free-module, and put $d_j=b(\alpha_j,\alpha_j)/2$.
Then
$$
A=G\cdot\diag\!\left(\tfrac{2}{G_{jj}}\right),
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

::: {.definition #def:determinant-class title="The determinant"}

Write $R^{\bullet}$ for the group of units of $R$ and $(R^{\bullet})^{2}$ for the subgroup of squares of units.
By @prop:gram-congruence the determinant of a Gram matrix changes by the square of a unit under change of basis, so a perfect form on a free module has a well-defined
$$
\det(b)\in R^{\bullet}/(R^{\bullet})^{2},
$$
and a general form on a free module has a well-defined class in the quotient monoid $R/(R^{\bullet})^{2}$ [@MH73, I §2.5].
Under orthogonal sum the rank adds and the determinant multiplies [@MH73, I §3].
:::

::: {.proposition #prop:alternating-gram title="Alternating forms in a basis"}

Let $b$ be skew-symmetric on a free module with basis $e_1,\dots,e_n$.
Then $b$ is alternating if and only if $b(e_i,e_i)=0$ for every $i$.
:::

::: {.proof}

For $x=\Sum_ix_ie_i$, bilinearity gives
$$
b(x,x)=\Sum_i x_i^{2}\,b(e_i,e_i)+\Sum_{i<j}x_ix_j\bigl(b(e_i,e_j)+b(e_j,e_i)\bigr),
$$
a finite sum, and skew-symmetry makes $b(e_i,e_j)+b(e_j,e_i)=0$, so
$$
b(x,x)=\Sum_i x_i^{2}\,b(e_i,e_i).
$$
If every $b(e_i,e_i)$ vanishes then $b(x,x)=0$ for every $x$; conversely $b(e_i,e_i)=0$ is the case $x=e_i$.
:::

::: {.remark}
The symmetric form on $\bZ^{2}$ with Gram matrix $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ has vanishing diagonal and $b(e_1+e_2,e_1+e_2)=2$.
:::

## Tensor product and twisting {#sec-form-tensor}

::: {.definition #def:form-tensor title="Tensor product of forms"}

Let $b_M$ have value module $W_M$ and $b_N$ have value module $W_N$.
There is exactly one bilinear map
$$
b_M\tensor_R b_N\colon (M\tensor_RN)\times(M\tensor_RN)\too W_M\tensor_RW_N
$$
with
$$
(b_M\tensor_R b_N)(x\tensor_R u,\;y\tensor_R v)=b_M(x,y)\tensor_R b_N(u,v),
$$
induced by the morphism
$$
M\tensor_RN\tensor_RM\tensor_RN
\too
W_M\tensor_RW_N,
\qquad
x\tensor u\tensor y\tensor v
\longmapsto
b_M(x,y)\tensor b_N(u,v),
$$
after the symmetry isomorphism carrying $(M\tensor_RN)^{\tensor2}$ to $M\tensor_RM\tensor_RN\tensor_RN$ [@MH73, I §5.1].
For $W_M=W_N=R$ the value module is $R$.

Call a form $\eps$-symmetric when $b(x,y)=\eps\,b(y,x)$, so that $1$-symmetric means symmetric and $(-1)$-symmetric means skew-symmetric.
The tensor product of an $\eps$-symmetric and an $\eps'$-symmetric form is $\eps\eps'$-symmetric [@MH73, I §5.2].
If both forms are perfect and both modules are finitely generated projective, the tensor product is perfect [@MH73, I §5.3].
:::

::: {.proposition #prop:tensor-gram title="Gram matrix and determinant of a tensor product"}

If $M$ and $N$ are free of ranks $m$ and $n$ with Gram matrices $G_M$ and $G_N$, the Gram matrix of $b_M\tensor_R b_N$ in the product basis is the Kronecker product $G_M\tensor_R G_N$, and
$$
\det(b_M\tensor_R b_N)=\det(b_M)^{\,n}\det(b_N)^{\,m}.
$$
:::

::: {.proof}

In the product basis,
$$
(b_M\tensor b_N)(e_i\tensor f_a,\ e_j\tensor f_b)=b_M(e_i,e_j)\,b_N(f_a,f_b)=(G_M)_{ij}(G_N)_{ab}
$$
by @def:form-tensor, so with the product basis ordered lexicographically by the pair of indices the Gram matrix is the Kronecker product $G_M\tensor G_N$.

For the determinant, factor the Kronecker product as $G_M\tensor G_N=(G_M\tensor I_n)(I_m\tensor G_N)$, which is the defining property of the product of matrices in block form.
The second factor $I_m\tensor G_N$ is block diagonal with $m$ diagonal blocks $G_N$, so its determinant is $\det(G_N)^{m}$.
The first factor $G_M\tensor I_n$ becomes block diagonal with $n$ diagonal blocks $G_M$ after the permutation of the product basis that interchanges the two factors, and a permutation matrix has determinant $\pm1$ appearing on both sides of a conjugation, so $\det(G_M\tensor I_n)=\det(G_M)^{n}$.
Multiplicativity of the determinant gives $\det(G_M\tensor G_N)=\det(G_M)^{n}\det(G_N)^{m}$, which is the asserted identity since the Gram matrices present $\det(b_M)$ and $\det(b_N)$ by @def:determinant-class.
:::

::: {.definition #def:form-twist title="Twisting"}

For $\lambda\in R$ the *twist* $b(\lambda)$ of $(M,b)$ is the form $\lambda b$ on the same module, written $M(\lambda)$.
Its Gram matrix in a basis is $\lambda G$, its adjoint maps are $\lambda\,b^{\sharp}$ and $\lambda\,{}^{\sharp}b$, and on a free module of rank $n$
$$
\det\bigl(b(\lambda)\bigr)=\lambda^{\,n}\det(b).
$$

A morphism $f$ of @def:form-categories satisfies $f^{*}b_N=b_M$ and hence $f^{*}(\lambda b_N)=\lambda b_M$, so $(-)(\lambda)$ is an endofunctor of $\mathcal B_{R,W}$ which is the identity on underlying maps.
For $\lambda$ a unit it is an isomorphism of categories with inverse $(-)(\lambda^{-1})$, and $(-)(-1)$ is an involution.
:::

## Signatures at real places {#sec-signature}

::: {.definition #def:signature title="Signature"}

Let $F$ be an ordered field and let $b$ be a symmetric bilinear form on a finite-dimensional $F$-vector space $V$.
Define
$$
\operatorname{sig}(V,b)\definedas(p,q,r),
$$
where $p$ and $q$ are the maximal dimensions of positive- and negative-definite subspaces and
$$
r\definedas\dim_F\radic(V).
$$

For a commutative ring $R$, define the set of real places
$$
\Sigma_\infty(R)
\definedas
\Hom_{\mathbf{CRing}}(R,\bR).
$$
For
$$
\sigma\in\Sigma_\infty(R)
$$
let
$$
\operatorname{sig}_\sigma(M,b)
$$
be the signature of the scalar extension along $\sigma$ from @def:module-base-change.
The signature over $R$ is the tuple
$$
\operatorname{sig}_R(M,b)
\definedas
\bigl(\operatorname{sig}_\sigma(M,b)\bigr)_{\sigma\in\Sigma_\infty(R)}.
$$
For $R=\bZ$ there is one real place and the tuple is identified with its single component.

For a nondegenerate form every component has radical dimension $0$ and is written as a pair.
:::

::: {.theorem #thm:sylvester title="Sylvester's law of inertia"}

Let $F$ be an ordered field and let $b$ be a perfect symmetric bilinear form on a finite-dimensional $F$-vector space $V$.
Then $V\cong V^{+}\perp V^{-}$ with $b$ positive definite on $V^{+}$ and negative definite on $V^{-}$, and the two dimensions depend only on the isomorphism class of $(V,b)$: $\dim V^{+}$ is the greatest dimension of a positive definite subspace of $V$ [@MH73, III §2.5].
So the signature of @def:signature is $(\dim V^{+},\dim V^{-},0)$ and $p+q=\dim V$.

For a degenerate $b$, choose a complement $N$ to $\radic(V)$ in $V$.
Every pairing involving $\radic(V)$ vanishes, so $V\cong\radic(V)\perp N$ and $b|_N$ is nondegenerate, hence perfect because $N$ is finite dimensional.
Applying the above to $N$ gives $V\cong V^{+}\perp V^{-}\perp\radic(V)$, so $p+q+r=\dim V$ in every case.
:::

::: {.proof}

An ordered field has characteristic $0$, so $2$ is a unit and
$$
2\,b(u,v)=b(u+v,u+v)-b(u,u)-b(v,v).
$$

*Perfect case.*
Suppose first that $b$ is perfect.
If $V\neq0$ then $b\neq0$, since $b=0$ would put every vector in the radical; so $b(u,v)\neq0$ for some $u,v$, and the displayed identity shows that one of $u$, $v$, $u+v$ has nonzero square.
Take $u$ with $b(u,u)\neq0$; the line $L=\langle u\rangle$ has perfect restriction $b|_L$ because $b(u,u)$ is a unit, so @thm:orthogonal-decomposition gives $V=L\perp L^{\perp}$.
The restriction to $L^{\perp}$ is perfect: if $x\in L^{\perp}$ pairs to zero with $L^{\perp}$ then it pairs to zero with $L$ as well, so $x$ lies in the radical of $b$, which is zero.
Inducting on $\dim V$ gives an orthogonal basis $u_1,\dots,u_n$, that is, $b(u_i,u_j)=0$ for $i\neq j$.

Let $V^{+}$ be the span of those $u_i$ with $b(u_i,u_i)>0$ and $V^{-}$ the span of those with $b(u_i,u_i)<0$.
Orthogonality gives $V=V^{+}\perp V^{-}$ on the nose, and $b$ is positive definite on $V^{+}$ and negative definite on $V^{-}$: a vector there is $\Sum a_iu_i$ over $i$ in one index set, and $b(\Sum a_iu_i,\Sum a_iu_i)=\Sum a_i^{2}b(u_i,u_i)$ is a sum of terms of one sign, vanishing only when every coefficient does.
So $(V,b)\cong(V^{+},b|_{V^{+}})\perp(V^{-},b|_{V^{-}})$ with the two summands definite of the stated signs.

That $\dim V^{+}$ is the greatest dimension of a positive definite subspace: if $W$ is positive definite and $0\neq w\in W\cap V^{-}$, then $b(w,w)>0$ because $W$ is positive definite and $b(w,w)\leq0$ because $b$ is negative semidefinite on $V^{-}$, which is impossible; so $W\cap V^{-}=0$ and $\dim W\leq\dim V-\dim V^{-}=\dim V^{+}$, with equality for $W=V^{+}$.
An isometry carries a positive definite subspace to a positive definite subspace of the same dimension, so $\dim V^{+}$ and $\dim V^{-}$ depend only on the isomorphism class, and the signature of @def:signature is $(\dim V^{+},\dim V^{-},0)$ by @def:signature, with $p+q=\dim V$.

*Degenerate case.*
Let $r=\dim\radic(V)>0$ and choose a complement $N$ of $\radic(V)$ in $V$.
If $x\in\radic(V)$ then $b(x,-)=0$ by definition of the radical, and $b(-,x)=0$ by symmetry, so every pairing involving $\radic(V)$ vanishes and $V=\radic(V)\perp N$.
The restriction $b|_N$ is perfect: if $x\in N$ pairs to zero with all of $N$, then it pairs to zero with $\radic(V)$ as well, so $x\in\radic(V)\cap N=0$.
The perfect case applied to $N$ writes $N\cong V^{+}\perp V^{-}$, hence $V\cong V^{+}\perp V^{-}\perp\radic(V)$, and $p+q+r=\dim V$.
:::

::: {.definition #def:definiteness title="Definiteness"}

Let $b$ be a symmetric bilinear form of signature $(p,q,r)$ and set $n=p+q+r$.
Then $b$ is

- *degenerate* if $r>0$;

- *positive definite* if $(p,q,r)=(n,0,0)$, and *negative definite* if $(p,q,r)=(0,n,0)$;

- *definite* if it is positive definite or negative definite;

- *indefinite* if $p\geq1$ and $q\geq1$;

- *hyperbolic*, or of Lorentzian signature, if $n\geq2$ and $(p,q,r)=(1,n-1,0)$;

- *parabolic* if $n\geq2$ and $(p,q,r)=(0,n-1,1)$.

:::

::: {.convention}
Root lattices are taken negative definite here, so the forms on $A_n$, $D_n$ and $E_n$ are negative definite and the hyperbolic signature is $(1,n-1,0)$.
:::

## Isotropy and Witt decomposition {#sec-witt}

::: {.definition #def:hyperbolic-plane title="Rank one forms, the hyperbolic plane, and split forms"}

For a unit $u\in R^{\bullet}$ write $\langle u\rangle$ for the free module of rank $1$ on a generator $e$ with $b(e,e)=u$.
Then $\langle u\rangle\cong\langle u'\rangle$ if and only if $u'=\alpha^{2}u$ for some $\alpha\in R^{\bullet}$ [@MH73, I §2.4].

The *hyperbolic plane* $U$ over $R$ is the free module on $e,f$ with
$$
b(e,e)=b(f,f)=0,\qquad b(e,f)=b(f,e)=1,
$$
so its Gram matrix is $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$, its form is perfect and even, and its signature over an ordered field is $(1,1,0)$.

A perfect symmetric form $b$ on $M$ is *split* if $M$ has a direct summand $N$ with $N=N^{\perp_b}$ [@MH73, I §6.1].
Over a ring whose finitely generated projective modules are free and in which $2$ is a unit, a split form is an orthogonal sum of hyperbolic planes, which is @thm:metabolic-is-hyperbolic; this applies to a field of characteristic other than $2$.
:::

::: {.definition #def:witt-index title="Witt index"}

The *Witt index* $i(V)$ of a perfect symmetric form on a finite-dimensional vector space $V$ over a field is the greatest dimension of a totally isotropic subspace.
It satisfies
$$
0\leq i(V)\leq\tfrac12\dim V,
$$
with $i(V)=0$ exactly when the form is anisotropic and $i(V)=\tfrac12\dim V$ exactly when the form is split [@MH73, III §1.2].
:::

::: {.theorem #thm:witt-decomposition title="Witt decomposition"}

Every perfect symmetric form on a finite-dimensional vector space $V$ over a field $F$ decomposes as
$$
V\cong S\perp A
$$
with $S$ split and $A$ anisotropic [@MH73, III §1.1], and $A$ is determined up to isomorphism by the Witt class of $V$ [@MH73, III §1.7].
Here $\dim S=2\,i(V)$ and $\dim A=\dim V-2\,i(V)$.
:::

::: {.proof}

*Existence and the dimensions.*
Induct on $\dim V$. If $V$ has no isotropic vector it is anisotropic, and $S=0$, $A=V$ works.
Otherwise choose $0\neq v$ with $b(v,v)=0$. By perfection $b(v,-)$ is a nonzero functional, so there is $w$ with $b(v,w)=\lambda\neq0$; replacing $w$ by $\lambda^{-1}w$ gives $b(v,w)=1$.
Then $P\definedas\langle v,w\rangle$ has Gram matrix $\begin{pmatrix}0&1\\1&b(w,w)\end{pmatrix}$, whose determinant $-1$ is a unit, so $b|_P$ is perfect and @thm:orthogonal-decomposition gives $V=P\perp P^{\perp}$.

The plane $P$ is split in the sense of @def:hyperbolic-plane: the line $\langle v\rangle$ is a direct summand of $P$, being the first summand of $P=\langle v\rangle\oplus\langle w\rangle$, and for $x=\alpha v+\beta w$ one has $b(v,x)=\beta$, so $\langle v\rangle^{\perp_P}=\langle v\rangle$ whatever the value of $b(w,w)$.
The restriction to $P^{\perp}$ is perfect by the argument of @thm:sylvester, and $P^{\perp}$ has smaller dimension, so the induction hypothesis gives $P^{\perp}\cong S'\perp A$ with $S'$ split and $A$ anisotropic.
Then $V\cong(P\perp S')\perp A$, and $P\perp S'$ is split: if $N'$ is a lagrangian of $S'$ then $\langle v\rangle\perp N'$ is a lagrangian of $P\perp S'$, being a direct summand of a direct summand, isotropic because each summand is, and with $(\langle v\rangle\perp N')^{\perp}=\langle v\rangle^{\perp}\perp N'^{\perp}=\langle v\rangle\perp N'$ by @def:orthogonal-sum.
So $S\definedas P\perp S'$ and $A$ give the required decomposition.

For the dimensions, $i(S)=\tfrac12\dim S$: a lagrangian of $S$ is totally isotropic, and its dimension is $\tfrac12\dim S$ since $\dim N+\dim N^{\perp_b}=\dim S$ for a perfect form and $N=N^{\perp_b}$, while $i(S)\leq\tfrac12\dim S$ by @def:witt-index.
Also $i(A)=0$, a nonzero vector of a totally isotropic subspace having $b(x,x)=0$.

That $i(V)=i(S)$ for $V=S\perp A$ with $A$ anisotropic is the second cited step [@MH73, III §1.2]: it is a consequence of Witt's extension theorem, which moves a maximal totally isotropic subspace into $S$, and it is not derived here.
It fails without the hypothesis on $A$: $\langle1\rangle\perp\langle-1\rangle$ is hyperbolic, with $i=1$, while neither summand contains an isotropic vector, so the index is not additive over orthogonal sums in general.
Granting it, $\dim S=2\,i(V)$ and $\dim A=\dim V-\dim S=\dim V-2\,i(V)$.

*Uniqueness of $A$.*
This is Witt's cancellation theorem [@MH73, III §1.7]: if $X\perp Z\cong Y\perp Z$ for perfect symmetric forms over a field then $X\cong Y$, applied to the two decompositions of $V$.
It is the one step of this statement not derived above, and the reason is not bookkeeping: the standard proof splits a common rank-one summand off both sides, which needs a vector with nonzero square, and over a field of characteristic $2$ a symmetric form can have all squares zero.
:::

::: {.example #ex:witt-index-over-Q title="Witt index and signature"}

Over a real closed field every positive element is a square, so by @thm:sylvester a perfect symmetric form of signature $(p,q,0)$ is $p\langle1\rangle\perp q\langle-1\rangle$.
Each summand $\langle1\rangle\perp\langle-1\rangle$ is split [@MH73, I §6.1], so the Witt index is $\min(p,q)$.

Over $\bQ$ the Witt index can be strictly smaller.
The form $x^{2}+y^{2}-3z^{2}$ has signature $(2,1,0)$, so $\min(p,q)=1$, and it is anisotropic over $\bQ$, so its Witt index is $0$.
For a primitive integral solution of $x^{2}+y^{2}=3z^{2}$, reduction modulo $3$ forces $3\mid x$ and $3\mid y$ because $-1$ is not a square modulo $3$; then $9\mid3z^{2}$ gives $3\mid z$, contradicting primitivity.
:::

::: {.remark #rmk:three-integers title="Signature, signature difference, and Witt index"}
Three integers are attached to a nondegenerate symmetric form over an ordered field, and they are distinct invariants.
The pair $(p,q)$ is the signature of @def:signature.
The integer $p-q$ is called the signature of the form in [@MH73, III §2.5], where it is the value of a ring homomorphism from the Witt ring to $\bZ$.
The Witt index of @def:witt-index is a third quantity, equal to $\min(p,q)$ over a real closed field and smaller over $\bQ$ in the case above.
:::

## Diagonal and polarization {#sec-polarization-functors}

::: {.definition #def:polarization-functors title="Diagonal and polarization functors"}
Diagonal and polarization define natural transformations
$$
\diag\colon\Symbil_{R,W}
\Longrightarrow\operatorname{Quad}_{R,W},
\qquad
\operatorname{polar}\colon\operatorname{Quad}_{R,W}
\Longrightarrow\Symbil_{R,W},
$$
with
$$
\diag(b)(x)=b(x,x),
\qquad
\operatorname{polar}(q)(x,y)=q(x+y)-q(x)-q(y).
$$
Here $\Symbil_{R,W}$ is the $R$-submodule-valued presheaf of symmetric bilinear forms.
The composites satisfy
$$
\operatorname{polar}(\diag(b))=2b,
\qquad
\diag(\operatorname{polar}(q))=2q.
$$
If $2$ is invertible on $W$, division by $2$ gives inverse equivalences between symmetric bilinear forms and quadratic forms.
For a general value module, they define parallel functors whose composites are multiplication by $2$.

For discriminant forms, the isomorphism
$$
\bQ/2\bZ\too\bQ/\bZ,
\qquad w\longmapsto w/2,
$$
followed by polarization gives the bilinearization functor from $\bQ/2\bZ$-valued quadratic forms to $\bQ/\bZ$-valued symmetric bilinear forms.
:::

Bilinear forms on the underlying module of an associative unital $R$-algebra are treated in @sec-algebra-module-forms: module bilinear forms are $\Hom_{R\text{-}\mathbf{Mod}}(M\tensor_R M,R)$, and algebra bilinear forms are $\Hom_{R\text{-}\mathbf{Alg}}(A\tensor_R A,R)$ with the tensor product taken in $R\text{-}\mathbf{Alg}$.
