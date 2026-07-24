# Modules and base change {#sec-module-categories}

Fix a commutative ring $R$.

::: {#def-modules-over-ring}
## Modules over a ring

For a ring $A$, write $A\text{-}\mathbf{Mod}$ for the category of left $A$-modules.
A right $A$-module is a left $A^{\mathrm{op}}$-module.
An $(A,B)$-bimodule therefore has forgetful functors
$$
A\text{-}\mathbf{Mod}\longleftarrow
{}_A\mathbf{Bimod}_B\longrightarrow
B^{\mathrm{op}}\text{-}\mathbf{Mod}.
$$
When $A$ is commutative, the identity $A=A^{\mathrm{op}}$ identifies left and right $A$-module conventions.
For a general ring, an equivalence between left and right module categories is additional data; it does not follow merely from notation.
:::

::: {#def-module-base-change}
## Base change

Let $\varphi\colon A\to B$ be a homomorphism of commutative rings.
Extension and restriction of scalars define an adjunction
$$
\adj{A\text{-}\mathbf{Mod}}{B\text{-}\mathbf{Mod}}
{B\otimes_A-}{\operatorname{Res}_{\varphi}},
\qquad B\otimes_A-\dashv\operatorname{Res}_{\varphi}.
$$
For an $A$-bilinear form $b\colon M\times M\to A$, its base change is the $B$-bilinear form on $B\otimes_A M$ determined by
$$
b_B(a\otimes x,c\otimes y)=ac\,\varphi(b(x,y)).
$$
:::

## Module properties {#sec-module-properties}

::: {#def-module-subcategories}
The following isomorphism-invariant properties define replete full subcategories of $R\text{-}\mathbf{Mod}$:

- finitely generated: some $R^n\twoheadrightarrow M$ is surjective;

- projective: $M$ is a direct summand of a free module;

- free: $M\cong R^{(I)}$ for some set $I$;

- finitely generated projective: both of the first two conditions hold.

If $R$ is an integral domain, $M$ is *torsion* when every element is annihilated by a nonzero element of $R$, and *torsion-free* when multiplication by every nonzero element of $R$ is injective.
Over a general ring, a torsion subcategory is used only after a torsion theory has been specified.
:::
