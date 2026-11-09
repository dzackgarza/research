# Bilinear and quadratic forms {#sec-form-theory}

Fix a commutative ring $R$ and an $R$-module $W$, the *value module* of the forms below.

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
When multiplication by $2$ is an epimorphism, every bilinear form is even.
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

::: {.proposition #prop:orthogonal-galois-connection title="The orthogonal complement is an antitone Galois connection"}

Let $(M,W,b)$ be a symmetric bilinear module, and let $\operatorname{Sub}(M)$ be the poset of subobjects of $M$ in $R\text{-}\mathbf{Mod}$ (@def:subobject-relation), with $S\subseteq T$ when $S$ factors through $T$.
For a subobject $S$ represented by $\iota\colon S\injects M$, let $S^\perp$ be the subobject represented by $\kappa_\iota^{\mathrm R}\colon S^{\perp_b}\injects M$ of @def:orthogonal-complement.
Then $S\mapsto S^\perp$ is a well-defined order-reversing map $\operatorname{Sub}(M)\too\operatorname{Sub}(M)$, and for all $S,T\in\operatorname{Sub}(M)$
$$
S\subseteq T^\perp
\quad\Longleftrightarrow\quad
T\subseteq S^\perp .
$$
Thus $(-)^\perp$ is an antitone Galois connection of $\operatorname{Sub}(M)$ with itself, and
$$
S\subseteq S^{\perp\perp},
\qquad
S^\perp=S^{\perp\perp\perp}
$$
[@Mac98, §IV.5, Thm. 1].
:::

::: {.proof}

In $R\text{-}\mathbf{Mod}$ a subobject of $M$ is determined by the image of any representative, and $S\subseteq T$ holds exactly when the image of $S$ is contained in the image of $T$.
By the exact sequence that defines $S^{\perp_b}$, the image of $\kappa_\iota^{\mathrm R}$ is
$$
\{x\in M : b(y,x)=0\text{ for all }y\in\iota(S)\},
$$
which depends only on $\iota(S)$, so $S^\perp$ depends only on the subobject $S$.
If $\iota(S)\subseteq\iota'(T)$, every $x$ orthogonal to $\iota'(T)$ is orthogonal to $\iota(S)$, so $T^\perp\subseteq S^\perp$.

Both $S\subseteq T^\perp$ and $T\subseteq S^\perp$ state that $b(y,z)=0$ for all $y$ in the image of $T$ and $z$ in the image of $S$, the second after the symmetry $b(y,z)=b(z,y)$.
So the two conditions are equivalent.

Regard $(-)^\perp$ as two order-preserving maps $F\colon\operatorname{Sub}(M)\too\operatorname{Sub}(M)^{\mathrm{op}}$ and $G\colon\operatorname{Sub}(M)^{\mathrm{op}}\too\operatorname{Sub}(M)$.
The displayed equivalence states that $FS\supseteq T$ in $\operatorname{Sub}(M)$ if and only if $S\subseteq GT$, so $F$ is left adjoint to $G$ and the pair is a Galois connection [@Mac98, §IV.5, Thm. 1].
Taking $T=S^\perp$ gives $S\subseteq S^{\perp\perp}$.
Applying the order-reversing map to $S\subseteq S^{\perp\perp}$ gives $S^{\perp\perp\perp}\subseteq S^\perp$, and $S^\perp\subseteq(S^\perp)^{\perp\perp}$ is the previous inclusion for $S^\perp$.
Hence $S^\perp=S^{\perp\perp\perp}$.
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

This is [@MH73, I §3.1].
The argument needs nothing of $M$: for $m\in M$ the functional $t\mapsto b(m,\iota(t))$ equals $b(t_0,\iota(t))$ for a unique $t_0\in T$ by perfectness of $b|_T$, and then $m-\iota(t_0)\in T^{\perp}$; injectivity is that $T\cap T^{\perp}$ is the kernel of the perfect form $b_T$.
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

The first claim is bilinearity applied to two finite sums, and the second is that a bilinear form is determined by its values on pairs of basis vectors, with the displayed formula reconstructing it.
This is the standard bijection between forms and matrices on a free module [@MH73, I §2.1].
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

If $e'_j=\Sum_iP_{ij}e_i$ then
$$
G'_{ij}=b(e'_i,e'_j)=\Sum_{k,l}P_{ki}\,G_{kl}\,P_{lj}=(P^{\mathsf T}GP)_{ij}
$$
by bilinearity; and conversely an invertible $P$ defines a second basis $e'$ of the same form, so congruent matrices are the Gram matrices of one form in two bases [@MH73, I §2.3].
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

::: {.example #ex:symmetric-zero-diagonal-not-alternating title="A symmetric form with vanishing diagonal that is not alternating"}

Let $b$ be the symmetric form on $\bZ^{2}$ with Gram matrix $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ in the standard basis $e_1,e_2$.
Then $b(e_1,e_1)=b(e_2,e_2)=0$, and
$$
b(e_1+e_2,e_1+e_2)=b(e_1,e_1)+2\,b(e_1,e_2)+b(e_2,e_2)=2\neq0,
$$
so $b$ is not alternating (@def:form-axioms).
The form $b$ is not skew-symmetric, because $b(e_2,e_1)=1\neq-1=-b(e_1,e_2)$.
So @prop:alternating-gram fails without its skew-symmetry hypothesis.
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

The Gram matrix is the Kronecker product because $(b_M\tensor b_N)(e_i\tensor f_a,e_j\tensor f_b)=b_M(e_i,e_j)b_N(f_a,f_b)$ by @def:form-tensor, and the determinant identity follows from $\det(A\tensor B)=\det(A)^{n}\det(B)^{m}$ [@MH73, I §5.3], which is the multiplicativity of the determinant applied to the factorization $A\tensor B=(A\tensor I_n)(I_m\tensor B)$.
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
For a degenerate $b$ the same conclusions hold with $r=\dim\radic(V)$ nonzero, and $p+q+r=\dim V$.
:::

::: {.proof}

This is [@MH73, III §2.5].
An ordered field has characteristic $0$, hence $2$ is a unit and
$$
2\,b(u,v)=b(u+v,u+v)-b(u,u)-b(v,v).
$$
That identity gives a vector of nonzero square and hence, by @thm:orthogonal-decomposition, an orthogonal basis.
Given an orthogonal basis, $V=V^{+}\perp V^{-}$ with the two summands definite, and $\dim V^{+}$ is maximal among positive definite subspaces because such a subspace meets $V^{-}$ only at $0$.

For degenerate $b$, let $N$ be a complement of $\radic(V)$.
Every pairing with $\radic(V)$ vanishes, so $V\cong\radic(V)\perp N$; the restriction $b|_N$ is perfect, because an element of $N$ pairing to zero with $N$ pairs to zero with all of $V$; and the perfect case applied to $N$ gives $V\cong V^{+}\perp V^{-}\perp\radic(V)$ and $p+q+r=\dim V$.
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

This is [@MH73, III §1.1 and §1.7].

Existence does not need $2$ to be a unit: if $v$ is isotropic and $b(v,w)=\lambda\neq0$, then $P=\langle v,w\rangle$ has Gram matrix with determinant $-1$, a unit in every ring, so $P$ splits off by @thm:orthogonal-decomposition, and the line $\langle v\rangle$ is a lagrangian of $P$ because $b(v,\alpha v+\beta w)=\beta\lambda$ vanishes exactly on $\langle v\rangle$ — whatever $b(w,w)$ is.
So the induction produces $S\perp A$ with $A$ anisotropic over any field.

The proof uses (i) that $i(V)=i(S)$ when $A$ is anisotropic, which is Witt's extension theorem applied to a maximal totally isotropic subspace [@MH73, III §1.2], and (ii) the uniqueness of the anisotropic representative of a Witt class, which [@MH73, III Thm. 1.7] proves for every field, characteristic $2$ included.
Clause (i) needs the hypothesis on $A$: $\langle1\rangle\perp\langle-1\rangle$ is hyperbolic with index $1$, while neither summand contains an isotropic vector.
:::

::: {.example #ex:witt-index-over-Q title="Witt index and signature"}

Over a real closed field every positive element is a square, so by @thm:sylvester a perfect symmetric form of signature $(p,q,0)$ is $p\langle1\rangle\perp q\langle-1\rangle$.
Each summand $\langle1\rangle\perp\langle-1\rangle$ is split [@MH73, I §6.1], so the Witt index is $\min(p,q)$.

Over $\bQ$ the Witt index can be strictly smaller.
The form $x^{2}+y^{2}-3z^{2}$ has signature $(2,1,0)$, so $\min(p,q)=1$, and it is anisotropic over $\bQ$, so its Witt index is $0$.
For a primitive integral solution of $x^{2}+y^{2}=3z^{2}$, reduction modulo $3$ forces $3\mid x$ and $3\mid y$ because $-1$ is not a square modulo $3$; then $9\mid3z^{2}$ gives $3\mid z$, contradicting primitivity.
:::

::: {.notation title="The signature as a pair and as an integer"}
For a nondegenerate symmetric form over an ordered field $F$, the signature is the pair $(p,q)$ of @def:signature.
[@MH73, III §2.5] calls the integer $p-q$ the signature at the ordering; it depends only on the Witt class, is additive over orthogonal sums and multiplicative over tensor products, and so defines a ring homomorphism $W(F)\to\bZ$ [@MH73, III Lem. 2.6].
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
