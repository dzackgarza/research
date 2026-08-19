# Bilinear Forms, Duals, and Morphisms

## Dual Basis and Adjoint Map

Assume $L$ is finite free over $R$, with basis $(e_1,\dots,e_n)$. Then $L^* =
\operatorname{Hom}_R(L,R)$ has the dual basis $(e_1^*,\dots,e_n^*)$, characterized by

$$ e_i^*(e_j) = \delta_{ij}. $$

Also $L_K = L \otimes_R K$ has basis $(e_1 \otimes 1,\dots,e_n \otimes 1)$.

Now define the adjoint map

$$ \operatorname{ad}_\beta: L \to L^*, \qquad v \mapsto \beta(v,-). $$

This requires no nondegeneracy.

For any $v \in L$, since $(e_i^*)$ is a basis of $L^*$, we can expand the functional
$\beta(v,-)$ uniquely as

$$ \beta(v,-) = \sum_{i=1}^n c_i(v) e_i^*. $$

The coefficients are determined by evaluation on the basis vectors $e_j$. But here it is
even more direct: because $e_i^*(e_j) = \delta_{ij}$, the coefficient of $e_i^*$ is
exactly the value of the functional on $e_i$. So

$$ c_i(v) = \beta(v,e_i). $$

Hence the actual abstract identity is

$$ \operatorname{ad}*\beta(v) = \sum*{i=1}^n \beta(v,e_i) e_i^*. $$

That is the clean formula, with no matrix language yet.

Now write

$$ v = \sum_{j=1}^n a_j e_j. $$

Then bilinearity gives

$$ \beta(v,e_i) = \sum_{j=1}^n a_j \beta(e_j,e_i), $$

so

$$ \operatorname{ad}*\beta(v) = \sum*{i=1}^n \left( \sum_{j=1}^n a_j \beta(e_j,e_i)
\right) e_i^*. $$

Only at this point do you extract a matrix.

If you define the Gram coefficients by

$$ G_{ij} := \beta(e_j,e_i), $$

then the matrix of $\operatorname{ad}_\beta: L \to L^*$ in the basis $e_j$ of $L$ and
$e_i^*$ of $L^*$ is exactly $G$.

If instead you use the more common convention

$$ \widetilde G_{ij} := \beta(e_i,e_j), $$

then the matrix of $\operatorname{ad}_\beta$ is $\widetilde G^{\,t}$.

So the "transpose issue" is purely a convention about how you index the Gram matrix.
The underlying morphism is always

$$ v \longmapsto \sum_i \beta(v,e_i) e_i^*. $$

That is the correct abstract statement.

## Dual Lattice Map

The same style applies to the map

$$ \lambda: L^\# \to L^*, \qquad x \mapsto \bigl( w \mapsto \beta_K(x,w \otimes 1)
\bigr). $$

Namely, for $x \in L^\#$,

$$ \lambda(x) = \sum_{i=1}^n \beta_K(x, e_i \otimes 1) e_i^*. $$

Again: first the abstract expansion in the dual basis, then matrix language only
afterward.

## Summary

The correct formulation is: $G$ represents the map $L \to L^*$, and the reason its
entries are the $\beta(e_j,e_i)$ is exactly that

$$ \operatorname{ad}_\beta(e_j) = \sum_i \beta(e_j,e_i) e_i^*. $$

That is the whole coordinate computation, done correctly.

## The Complete Diagram

The right way to express everything is with the single diagram:

$$ \begin{array}{ccccc} && L && \\
& \swarrow_{\operatorname{ad}_\beta} & \downarrow_i & \searrow^{j} & \\
L^* & \xleftarrow{\ \lambda\ } & L^\# & \xrightarrow{\ \iota\ } & L_K \end{array} $$

with

$$ j = \iota \circ i, \qquad \operatorname{ad}_\beta = \lambda \circ i. $$

Everything here is abstract.

## Choosing Bases and Defining the Matrix $G$

Now choose a basis $(e_1,\dots,e_n)$ of $L$, and let $(e_1^*,\dots,e_n^*)$ be the dual
basis of $L^*$. Do **not** define $G$ as a matrix of numbers first.
Define it as:

$$ G := [\operatorname{ad}*\beta]*{(e_j) \to (e_i^*)}. $$

So $G$ is the matrix representing the morphism $\operatorname{ad}_\beta: L \to L^*$.

If $\lambda: L^\# \to L^*$ is an isomorphism, for example in the usual nondegenerate
finite free situation, define elements $(f_1,\dots,f_n \in L^\#)$ by

$$ \lambda(f_i) = e_i^*. $$

This gives a basis of $L^\#$.

Also $L_K$ has the basis $(e_1 \otimes 1,\dots,e_n \otimes 1)$.

Now the matrices of the five arrows are:

- $[j]_{(e_j) \to (e_j \otimes 1)} = I$
- $[\lambda]_{(f_j) \to (e_i^*)} = I$
- $[\operatorname{ad}*\beta]*{(e_j) \to (e_i^*)} = G$
- $[i]_{(e_j) \to (f_i)} = G$
- $[\iota]_{(f_j) \to (e_i \otimes 1)} = G^{-1}$

And these are forced by the commutative diagram:

From $\operatorname{ad}_\beta = \lambda \circ i$, we get $G = I \cdot [i]$, so $[i] =
G$.

From $j = \iota \circ i$, we get $I = [\iota] \cdot G$, so $[\iota] = G^{-1}$.

That is the clean abstract meaning of "$G$" and "$G^{-1}$" in this picture:

- **$G$** is the matrix of the morphism $L \to L^*$, and equally of $L \to L^\#$ once
  $L^\#$ is based via $\lambda$.
- **$G^{-1}$** is the matrix of the inclusion $L^\# \hookrightarrow L_K$ in those chosen
  bases.
- **$G^{-1}$** is **not** defining $L^\#$; it is only the matrix of that inclusion after
  the basis of $L^\#$ has been chosen through $\lambda^{-1}(e_i^*)$.

One should not write things like $G^t x \in R^n$ unless one has already fixed
identifications with free coordinate modules.
The invariant content is in the morphisms; the matrices come only afterward.

## The Non-Isomorphic Case

The one caveat is that none of the $G^{-1}$ language exists unless $\lambda$ is an
isomorphism. Without that, the diagram still exists, but there is no basis of $L^\#$
induced from $L^*$, and no inverse matrix to discuss.

## Categorical Formulation: Fibered Categories over $R$-Alg

The mistake in naive formulations is treating everything as though it already lived in
one ambient module category.
It does not.
The objects live over varying coefficient rings, so the right framework is a
category fibered over $R$-Alg, or equivalently a pseudofunctor

$$ S \longmapsto \mathrm{BilForm}(S), $$

where $\mathrm{BilForm}(S)$ is the category of $S$-modules equipped with $S$-valued
$S$-bilinear forms.

### Definition for a Fixed Base Ring

Concretely, for a fixed $R$-algebra $S$, an object is $(L, b)$ with $L \in S$-Mod and
$b: L \otimes_S L \to S$ an $S$-module morphism.

### Base Change and Morphisms

Now let $g: S_1 \to S_2$ be a morphism in $R$-Alg.
As usual, $g$ gives a base-change functor

$$ G = g_* := S_2 \otimes_{S_1}(-): S_1\text{-Mod} \to S_2\text{-Mod}. $$

So the right notion of morphism $(L_1, b_1) \to (L_2, b_2)$ lying over $g$ is not
directly a square between $L_1 \otimes_{S_1} L_1$ and $L_2 \otimes_{S_2} L_2$, because
those live in different categories.
The correct datum is an $S_2$-module morphism

$$ \varphi: S_2 \otimes_{S_1} L_1 \to L_2 $$

such that the following diagram in the single category $S_2$-Mod commutes:

$$ \begin{array}{ccc} (S_2 \otimes_{S_1} L_1) \otimes_{S_2} (S_2 \otimes_{S_1} L_1) &
\xrightarrow{\ \varphi\otimes\varphi\ } & L_2\otimes_{S_2}L_2\\
\downarrow & & \downarrow b_2\\
S_2\otimes_{S_1}(L_1\otimes_{S_1}L_1) & \xrightarrow{\ S_2\otimes b_1\ } &
S_2\otimes_{S_1}S_1\cong S_2 \end{array} $$

where the left vertical arrow is the canonical associativity/base-change isomorphism.

That is the honest one-category statement.

### Unpacking to Semilinear Maps

Now, if you unpack $\varphi$, it is equivalent by adjunction to an $R$-linear map $f:
L_1 \to L_2$ satisfying

$$ f(sx) = g(s)f(x) \qquad (s\in S_1, x\in L_1), $$

so $f$ is $g$-semilinear.
In those terms, the commutative diagram above becomes exactly

$$ b_2(fx,fy) = g\!\left(b_1(x,y)\right).
$$

### Summary: Clean Categorical Definition

The correction is right in two ways:

1. One should not say "restrict scalars and draw a square" unless one has explicitly
   chosen to work in $R$-Mod.
   The more natural formulation is to work in the target category $S_2$-Mod after
   applying the base-change functor determined by $g$.

2. The object really is not just an $R$-module with an $R$-bilinear map.
   It is an $R$-module together with an $S$-module structure and an $S$-bilinear form
   $b\in\operatorname{Hom}_S(L\otimes_SL,S)$.

**Clean definition:**

- **Objects over $S$**: pairs $(L,b)$ with $L\in S$-Mod and $b:L\otimes_SL\to S$ in
  $S$-Mod;
- **Morphisms over $g:S_1\to S_2$**: maps $\varphi:S_2\otimes_{S_1}L_1\to L_2$ in
  $S_2$-Mod making the base-changed form diagram commute.

That is the precise categorical version of what was described above.

## Canonical Definition: Triple Morphisms

The correct categorical definition is:

An object is a pair $(L, \beta)$, where $\beta \in
\operatorname{Hom}_S(\operatorname{Sym}^2_S(L), M)$, where the typing of $\beta$ already
implicitly includes:

- a commutative $R$-algebra $S$,
- the $S$-module structure on $L$,
- the $S$-module structure on $M$,
- hence also all induced $R$-module structures via $R \to S$.

A morphism $(L_1, \beta_1) \to (L_2, \beta_2)$ is a triple $(f, g, h)$, where:

- $g: S_1 \to S_2$ is an $R$-algebra morphism,
- $f, h$ are maps compatible with the structure maps after base change along $g$.

Precisely: let $G_g := S_2 \otimes_{S_1}(-): S_1\text{-Mod} \to S_2\text{-Mod}$. Then
the actual data are $S_2$-linear maps

$$ \widetilde f: G_g(L_1) \to L_2, \qquad \widetilde h: G_g(M_1) \to M_2, $$

such that the square in the single category $S_2$-Mod commutes:

$$ \begin{array}{ccc} G_g(\operatorname{Sym}^2_{S_1}(L_1)) & \xrightarrow{\
G_g(\beta_1)\ } & G_g(M_1) \\
\downarrow^{\operatorname{Sym}^2(\widetilde f)} & & \downarrow^{\widetilde h} \\
\operatorname{Sym}^2_{S_2}(L_2) & \xrightarrow{\ \beta_2\ } & M_2. \end{array} $$

The conditions that $f$ and $h$ "respect scalar multiplication via $g$" are not extra
axioms beyond this. They are exactly what it means for the relevant squares with the
structure morphisms $R \to S_i$, the $S_i$-actions on $L_i$, and the $S_i$-actions on
$M_i$ to commute after base change.

The elementwise formulas like

$$ f(sx) = g(s)f(x), \qquad h(sm) = g(s)h(m) $$

are just the unpacking of the commuting-structure-morphism condition, not additional
data.

## Cokernel of a Triple Morphism

Let $(f, g, h): (L_1, \beta_1) \to (L_2, \beta_2)$ be a morphism, and let $g: S_1 \to
S_2$ be the ring map.

Then first base-change to the target fiber over $S_2$:

$$ f_{S_2}: S_2\otimes_{S_1} L_1 \to L_2, \qquad h_{S_2}: S_2\otimes_{S_1} M_1 \to M_2.
$$

Now the cokernel is computed in two stages.

**First module stage:**

$$ Q := \operatorname{coker}*{S_2}(f*{S_2}) = L_2 / \operatorname{im}(f_{S_2}). $$

**Second coefficient stage:**

$$ N_0 := \operatorname{coker}*{S_2}(h*{S_2}) = M_2 / \operatorname{im}(h_{S_2}). $$

So the first approximation to the cokernel object is exactly $(Q, \text{something valued
in } N_0)$.

Then the only extra step is to force the form to descend from $L_2$ to $Q$. That means
you must kill the image in $N_0$ of the symmetric cross-terms involving $E :=
\operatorname{im}(f_{S_2}) \subseteq L_2$.

Because the form is symmetric, the relevant submodule is the image of

$$ E\cdot L_2 \subseteq \operatorname{Sym}^2_{S_2}(L_2) $$

under

$$ \operatorname{Sym}^2_{S_2}(L_2) \xrightarrow{\beta_2} M_2 \twoheadrightarrow N_0. $$

So the actual coefficient module is

$$ N := N_0 \Big/ \operatorname{im}\!\big(E\cdot L_2 \to
\operatorname{Sym}^2_{S_2}(L_2)\xrightarrow{\beta_2} N_0\big).
$$

Equivalently,

$$ N = \operatorname{coker}(h_{S_2}) \Big/ \big\langle \beta_2(e\cdot x) \bmod
\operatorname{im}(h_{S_2}) : e\in E,\ x\in L_2\big\rangle_{S_2}. $$

Then $\beta_2$ descends uniquely to

$$ \bar\beta: \operatorname{Sym}^2_{S_2}(Q) \to N. $$

So the simplification is right, with one correction:

- Yes, first take $\operatorname{coker}(f_{S_2})$ and $\operatorname{coker}(h_{S_2})$;
- But the extra quotient is **not** by an $S_2$-submodule of $L_2$;
- It is by the $S_2$-submodule of $\operatorname{coker}(h_{S_2})$ generated by the
  images of the cross-terms $\beta_2(E\cdot L_2)$.

So the cokernel object is

$$ \boxed{ \left( \operatorname{coker}(f_{S_2}),\ \bar\beta:
\operatorname{Sym}^2_{S_2}\big(\operatorname{coker}(f_{S_2})\big) \to
\frac{\operatorname{coker}(h_{S_2})}{\big\langle \beta_2(E\cdot L_2) \big\rangle}
\right) } $$

with $E = \operatorname{im}(f_{S_2})$.

That is the clean version.

## Recovering the Discriminant Form

To recover the **discriminant form**, the specialization is not $S_1 = \mathbb{Z}$, $S_2
= \mathbb{Q}$.

It is $R = \mathbb{Z}$, $S_1 = S_2 = \mathbb{Z}$, with different coefficient modules
$M_1 = \mathbb{Z}$, $M_2 = \mathbb{Q}$.

Why: the second source module is $L^\#$, and $L^\#$ is generally only a
$\mathbb{Z}$-module, not a $\mathbb{Q}$-module.
So it does not define an object over $S_2 = \mathbb{Q}$.

The correct two objects are:

- $(L, \beta_1)$, with $\beta_1 \in
  \operatorname{Hom}*{\mathbb{Z}}(\operatorname{Sym}^2*{\mathbb{Z}}(L), \mathbb{Z})$,
- $(L^\#, \beta_2)$, with $\beta_2 \in
  \operatorname{Hom}*{\mathbb{Z}}(\operatorname{Sym}^2*{\mathbb{Z}}(L^\#), \mathbb{Q})$,

where $\beta_2$ is just the extended rational form restricted to $L^\#$.

**The morphism is:**

- $g = \mathrm{id}_{\mathbb{Z}}$,
- $f = \iota_L: L \to L^\#$,
- $h: \mathbb{Z} \hookrightarrow \mathbb{Q}$.

Now apply the cokernel construction in the symmetric category.

**First module cokernel:**

$$ Q = \operatorname{coker}_{\mathbb{Z}}(f) = L^\#/L = A_L. $$

**First coefficient cokernel:**

$$ N_0 = \operatorname{coker}_{\mathbb{Z}}(h) = \mathbb{Q}/\mathbb{Z}. $$

Now check the extra cross-term quotient.
Here $E = \operatorname{im}(f) = L \subseteq L^\#$. The cross-terms are

$$ \beta_2(E \cdot L^\#) = \beta_2(L \cdot L^\#) \subseteq \mathbb{Z} $$

by the definition of $L^\#$. Therefore their image in $N_0 = \mathbb{Q}/\mathbb{Z}$ is
already zero.

So there is **no further quotient** to take.

**Hence the cokernel object is exactly**

$$ \left( A_L, \bar\beta \right), \qquad \bar\beta \in
\operatorname{Hom}*{\mathbb{Z}}\big(\operatorname{Sym}^2*{\mathbb{Z}}(A_L),
\mathbb{Q}/\mathbb{Z}\big), $$

with

$$ \bar\beta([x], [y]) = \beta_2(x, y) \bmod \mathbb{Z}. $$

So in the enlarged category, the discriminant form is recovered as the cokernel of

$$ (L, \beta: \operatorname{Sym}^2_{\mathbb{Z}}(L) \to \mathbb{Z}) \longrightarrow
(L^\#, \beta: \operatorname{Sym}^2_{\mathbb{Z}}(L^\#) \to \mathbb{Q}). $$

The mistake in choosing $S_2 = \mathbb{Q}$ was that it gives the rational ambient
object, but **not** the discriminant object.
