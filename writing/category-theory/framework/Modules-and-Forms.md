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
Let $W$ be an $A$-module and let $b\colon M\times M\to W$ be $A$-bilinear.
Its base change is the $B$-bilinear map
$$
b_B\colon(B\otimes_AM)\times(B\otimes_AM)\longrightarrow B\otimes_AW,
\qquad
b_B(c\otimes x,d\otimes y)=cd\otimes b(x,y),
$$
whose value module is $B\otimes_AW$.
For $W=A$ the isomorphism $B\otimes_AA\cong B$ rewrites this as
$b_B(c\otimes x,d\otimes y)=cd\,\varphi(b(x,y))$.
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

::: {#def-based-module}
## Bases

Fix a set $I$.
A *basis* of an $R$-module $M$ indexed by $I$ is an isomorphism $e\colon R^{(I)}\xrightarrow{\ \sim\ }M$, and a *based* module is a pair $(M,e)$.
Write $\operatorname{Bas}_I(M)$ for the set of such isomorphisms.

The group $\operatorname{Aut}_R(R^{(I)})$ acts on $\operatorname{Bas}_I(M)$ by precomposition, and the action is simply transitive whenever the set is nonempty: for $e,e'\in\operatorname{Bas}_I(M)$ the automorphism $e^{-1}e'$ is the unique one taking $e$ to $e'$.
So $\operatorname{Bas}_I(M)$ is either empty or a torsor under $\operatorname{Aut}_R(R^{(I)})$, and it is nonempty exactly when $M\cong R^{(I)}$.

Let $R\text{-}\mathbf{Mod}^{\mathrm{bas}}_I$ be the category whose objects are based modules $(M,e)$ with index set $I$ and whose morphisms $(M,e)\to(N,f)$ are the $R$-linear maps $u\colon M\to N$ satisfying $ue=f$.
Since $e$ and $f$ are isomorphisms, such a $u$ both exists and is forced to be $fe^{-1}$, so every hom-set is a singleton and the category is equivalent to the terminal category.
The forgetful functor
$$
U_{\mathrm{bas}}\colon R\text{-}\mathbf{Mod}^{\mathrm{bas}}_I\longrightarrow R\text{-}\mathbf{Mod}
$$
is faithful.
It is not full: the hom-set from $(R,\operatorname{id})$ to itself is $\{\operatorname{id}\}$, while $\operatorname{Hom}_R(R,R)=R$.
:::

::: {#prp-basis-is-structure}
## A basis is structure

The fibre of $U_{\mathrm{bas}}$ over $M$ is the discrete category on $\operatorname{Bas}_I(M)$.

An object of that fibre is a pair $\bigl((N,f),\varphi\bigr)$ with $\varphi\colon N\xrightarrow{\ \sim\ }M$, and a morphism to $\bigl((N',f'),\varphi'\bigr)$ is a morphism $u$ of $R\text{-}\mathbf{Mod}^{\mathrm{bas}}_I$ with $\varphi'u=\varphi$.
Sending $\bigl((N,f),\varphi\bigr)$ to the basis $\varphi f\in\operatorname{Bas}_I(M)$ identifies the objects of the fibre with $\operatorname{Bas}_I(M)$, and the condition $\varphi'u=\varphi$ together with $u=f'f^{-1}$ reads $\varphi'f'=\varphi f$, so a morphism of the fibre exists exactly between objects with equal associated basis, and is then unique.

By @def-property-structure-stuff a faithful functor with discrete fibres presents structure: a basis is a chosen object of the fibre, while freeness of @def-module-subcategories is the property that the fibre be nonempty for some $I$.
The simply transitive $\operatorname{Aut}_R(R^{(I)})$-action above is the action on that fibre, and a construction defined on a based module is stated together with its transformation rule under that action.

Dropping the requirement that $e$ be an isomorphism and asking only that it be surjective gives the generating frames of @def-generating-frame, for which the same argument runs and reaches the same conclusion by @prp-generating-frame-is-structure.
A basis is the case of a generating frame whose structure map is an isomorphism.
:::

::: {#def-free-module-orientation}
## Orientation of a free module

Let $R$ be a commutative ring and let $M$ be a free $R$-module of finite rank $n$.
The top exterior power $\det(M)\coloneqq\bigwedge^n M$ is a free $R$-module of rank $1$.
An *orientation* of $M$ is an isomorphism of $R$-modules
$$
\omega\colon R\xrightarrow{\ \sim\ }\det(M).
$$
Fix a subgroup of units $U\le R^\times$.
An *orientation modulo $U$* is an orbit of such isomorphisms under the action of $U$ by scalar multiplication.
Two ordered bases $(e_1,\dots,e_n)$ and $(f_1,\dots,f_n)$ of $M$ determine the same orientation modulo $U$ if and only if the change-of-basis matrix $A\in\operatorname{GL}_n(R)$, defined by $f_j=\sum_{i=1}^n A_{ij}e_i$, satisfies $\det(A)\in U$.
:::

