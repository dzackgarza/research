# Modules and form categories {#sec-module-categories}

Fix a commutative ring $R$ and an $R$-module $W$.

::: {#def-modules-over-ring}
## Modules over a ring

For a ring $A$, write $A\text{-}\mathbf{Mod}$ for the category of left $A$-modules.
A right $A$-module is a left $A^{\mathrm{op}}$-module. An $(A,B)$-bimodule therefore
has forgetful functors
$$
A\text{-}\mathbf{Mod}\longleftarrow
{}_A\mathbf{Bimod}_B\longrightarrow
B^{\mathrm{op}}\text{-}\mathbf{Mod}.
$$
When $A$ is commutative, the identity $A=A^{\mathrm{op}}$ identifies left and right
$A$-module conventions. For a general ring, an equivalence between left and right
module categories is additional data; it does not follow merely from notation.
:::

## Module properties {#sec-module-properties}

::: {#def-module-subcategories}
The following isomorphism-invariant properties define replete full subcategories of
$R\text{-}\mathbf{Mod}$:

- finitely generated: some $R^n\twoheadrightarrow M$ is surjective;
- projective: $M$ is a direct summand of a free module;
- free: $M\cong R^{(I)}$ for some set $I$;
- finitely generated projective: both of the first two conditions hold.

If $R$ is an integral domain, $M$ is *torsion* when every element is annihilated by a
nonzero element of $R$, and *torsion-free* when multiplication by every nonzero element
of $R$ is injective. Over a general ring, a torsion subcategory is used only after a
torsion theory has been specified.
:::

::: {#def-form-presheaves}
## Bilinear and quadratic form presheaves

Let $\operatorname{Bil}_{R,W}(M)$ be the set of $R$-bilinear maps
$M\times M\to W$. Pullback along $f\colon M\to N$ sends $b$ to
$$
f^*b(x,y)=b(fx,fy),
$$
and defines a presheaf
$\operatorname{Bil}_{R,W}\colon(R\text{-}\mathbf{Mod})^{\mathrm{op}}\to\mathbf{Set}$.

Let $\operatorname{Quad}_{R,W}(M)$ be the set of maps $q\colon M\to W$ for which
$q(rx)=r^2q(x)$ and
$$
b_q(x,y)=q(x+y)-q(x)-q(y)
$$
is $R$-bilinear. Pullback defines the presheaf
$\operatorname{Quad}_{R,W}$.
:::

::: {#def-form-categories}
## Form categories

Define
$$
\mathcal B_{R,W}=\operatorname{El}(\operatorname{Bil}_{R,W}),
\qquad
\mathcal Q_{R,W}=\operatorname{El}(\operatorname{Quad}_{R,W}).
$$
An object of $\mathcal B_{R,W}$ is a pair $(M,b)$. A morphism
$(M,b_M)\to(N,b_N)$ is an $R$-linear map $f\colon M\to N$ satisfying
$f^*b_N=b_M$. The projection to $R\text{-}\mathbf{Mod}$ is the discrete fibration
of @def-category-of-elements. The quadratic category uses the same convention.
:::

## Properties of bilinear forms {#sec-form-properties}

::: {#def-form-axioms}
For $b\colon M\times M\to W$:

- $b$ is *symmetric* if $b(x,y)=b(y,x)$;
- $b$ is *skew-symmetric* if $b(x,y)=-b(y,x)$;
- $b$ is *alternating* if $b(x,x)=0$;
- $b$ is *even* if $b(x,x)\in 2W$ for every $x$.

Alternating forms are skew-symmetric. The converse holds when multiplication by $2$ is
injective on $W$.
When $2W=W$, every bilinear form satisfies the evenness condition; quadratic refinements
retain additional information in the discriminant setting.
:::

::: {#def-polarization}
## The adjoint map

The bilinear form $b$ determines
$$
b^\sharp\colon M\longrightarrow\operatorname{Hom}_R(M,W),
\qquad
b^\sharp(x)(y)=b(x,y).
$$
The form is *nondegenerate* if $b^\sharp$ is injective. It is *perfect* if
$b^\sharp$ is an isomorphism. These conditions agree only under additional hypotheses.
:::

::: {#def-orthogonal-sum}
## Orthogonal sum

The orthogonal sum of $(M,b_M)$ and $(N,b_N)$ is
$$
(M,b_M)\perp(N,b_N)
=
(M\oplus N,b_M\oplus b_N),
$$
where the mixed terms vanish. With zero module as unit and the standard associativity,
symmetry, and unit isomorphisms, this defines a symmetric monoidal structure on
$\mathcal B_{R,W}$. The quadratic form category has the analogous orthogonal sum.
:::

## Diagonal and polarization {#sec-polarization-functors}

::: {#def-polarization-functors}
There are natural transformations
$$
\operatorname{diag}(b)(x)=b(x,x),
\qquad
\operatorname{polar}(q)(x,y)=q(x+y)-q(x)-q(y).
$$
They satisfy
$$
\operatorname{polar}(\operatorname{diag}(b))=2b,
\qquad
\operatorname{diag}(\operatorname{polar}(q))=2q.
$$
If $2$ is invertible on $W$, division by $2$ gives inverse equivalences between
symmetric bilinear forms and quadratic forms. For a general value module, they define
parallel functors whose composites are multiplication by $2$.

For discriminant forms, the isomorphism
$$
\mathbb Q/2\mathbb Z\longrightarrow\mathbb Q/\mathbb Z,
\qquad w\longmapsto w/2,
$$
followed by polarization gives the bilinearization functor from
$\mathbb Q/2\mathbb Z$-valued quadratic forms to
$\mathbb Q/\mathbb Z$-valued symmetric bilinear forms.
:::
