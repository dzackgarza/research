# Monoidal structure and internal algebraic objects {#sec-monoidal}

A tensor product on a category is chosen structure on it (@def-chosen-structure), and the algebraic objects of the later chapters are defined inside a category equipped with such a structure.

## Monoidal, braided, and symmetric structures {#sec-monoidal-categories}

::: {#def-monoidal-category}
## Monoidal categories

A *monoidal category* is a tuple $\langle B,\otimes,e,\alpha,\lambda,\varrho\rangle$ consisting of a category $B$, a bifunctor $\otimes\colon B\times B\to B$, an object $e\in B$, and natural isomorphisms
$$
\alpha_{a,b,c}\colon a\otimes(b\otimes c)\;\cong\;(a\otimes b)\otimes c,
\qquad
\lambda_a\colon e\otimes a\;\cong\;a,
\qquad
\varrho_a\colon a\otimes e\;\cong\;a,
$$
such that the pentagon diagram in $\alpha$ commutes for all $a,b,c,d$, the triangle
$$
(1\otimes\lambda_c)\circ\alpha_{a,e,c}
=\varrho_a\otimes 1_c
\colon a\otimes(e\otimes c)\longrightarrow a\otimes c
$$
commutes for all $a,c$, and $\lambda_e=\varrho_e$.
The category is *strict* when $\otimes$ is associative and unital on the nose and $\alpha,\lambda,\varrho$ are identities [@Mac98, §VII.1].
:::

::: {#thm-coherence}
## Coherence

In a monoidal category, every diagram built from instances of $\alpha$, $\lambda$, $\varrho$, identities, and $\otimes$ commutes; equivalently, every monoidal category is monoidally equivalent to a strict one [@Mac98, §VII.2].
:::

Coherence is what licenses the notation $a_1\otimes\cdots\otimes a_n$ without parentheses.
A construction that transports data along $\alpha$, $\lambda$, or $\varrho$ names the comparison it uses, in the sense of [Equivalences and witnesses](Identification.md#sec-canonical-identification).

::: {#exm-cartesian-monoidal}
## Cartesian and cocartesian structures

A category with finite products is monoidal with $a\otimes b$ a chosen product $a\times b$ and $e$ a terminal object, the three isomorphisms being the unique ones commuting with the projections; this is the *cartesian* monoidal structure.
Dually, finite coproducts and an initial object give the *cocartesian* structure [@Mac98, §VII.1].
For a commutative ring $R$, the tensor product and the direct sum give two different monoidal structures on $R\text{-}\mathbf{Mod}$, namely $(R\text{-}\mathbf{Mod},\otimes_R,R)$ and $(R\text{-}\mathbf{Mod},\oplus,0)$, and a statement about "the" monoidal structure names which one it uses.
:::

::: {#def-braided-symmetric}
## Braided and symmetric structures

A *braiding* on a monoidal category is a natural isomorphism $\gamma_{a,b}\colon a\otimes b\cong b\otimes a$ satisfying the two hexagon conditions relating $\gamma$ to $\alpha$.
A monoidal category is *symmetric* when it is equipped with a braiding satisfying
$$
\gamma_{a,b}\circ\gamma_{b,a}=1,
\qquad
\varrho_b=\lambda_b\circ\gamma_{b,e},
$$
together with the hexagon [@Mac98, §VII.7 and §XI.1].
These conditions again imply that all diagrams built from $\alpha,\lambda,\varrho,\gamma$ commute.
A cartesian or cocartesian monoidal structure is symmetric, with $\gamma$ the isomorphism commuting with the projections or injections.
:::

::: {#def-closed-monoidal}
## Closed structure and internal hom

A monoidal category $V$ is *closed* when it is symmetric and each functor $-\otimes b\colon V\to V$ has a specified right adjoint $[b,-]\colon V\to V$,
$$
\adj{V}{V}{-\otimes b}{[b,-]},
\qquad
-\otimes b\dashv[b,-],
$$
so that there are bijections
$$
\operatorname{Hom}_V(a\otimes b,\,c)\;\cong\;\operatorname{Hom}_V(a,\,[b,c]),
$$
natural in $a$ and $c$.
The value $[b,c]$ is the *internal hom*.
For a commutative ring $R$, $(R\text{-}\mathbf{Mod},\otimes_R,R)$ is closed with $[B,A]=\operatorname{Hom}_R(B,A)$, and $\mathbf{Set}$ and $\mathbf{Cat}$ are closed for their cartesian structures [@Mac98, §VII.7].
The *dual object* of $a$ in a closed monoidal category is $[a,e]$; that the canonical morphism $a\to[[a,e],e]$ is an isomorphism is a hypothesis on $a$, stated where it is used.
:::

## Internal algebraic objects {#sec-internal-objects}

::: {#def-monoid-object}
## Monoid objects

A *monoid in a monoidal category* $\langle B,\otimes,e\rangle$ is a triple $\langle c,\mu,\eta\rangle$ consisting of an object $c\in B$ and morphisms
$$
\mu\colon c\otimes c\longrightarrow c,
\qquad
\eta\colon e\longrightarrow c,
$$
such that the associativity diagram
$$
\mu\circ(\mu\otimes 1)\circ\alpha_{c,c,c}=\mu\circ(1\otimes\mu)
\colon c\otimes(c\otimes c)\longrightarrow c
$$
and the two unit diagrams
$$
\mu\circ(\eta\otimes 1)=\lambda_c\colon e\otimes c\to c,
\qquad
\mu\circ(1\otimes\eta)=\varrho_c\colon c\otimes e\to c
$$
commute.
A morphism of monoids is a morphism of $B$ commuting with $\mu$ and $\eta$ [@Mac98, §VII.3].
:::

::: {#exm-monoid-object-instances}
## Instances

A monoid in $(\mathbf{Set},\times,1)$ is a monoid in the sense of @def-semigroup-monoid, the two unit laws for $\eta$ becoming the unit laws for the element $\eta(*)$.

For a commutative ring $R$, a monoid in $(R\text{-}\mathbf{Mod},\otimes_R,R)$ is an associative unital $R$-algebra.
A monoid in the strict monoidal category of endofunctors of a category, with $\otimes$ composition, is a monad [@Mac98, §VII.3 and §VI.1].
:::

::: {#def-group-object}
## Group objects

Let $\mathcal C$ have finite products and a terminal object $1$.
A *group object* of $\mathcal C$ is a monoid $\langle c,\mu,\eta\rangle$ for the cartesian structure together with a morphism $\zeta\colon c\to c$ such that
$$
\mu\circ(1\times\zeta)\circ\delta=\eta\circ{!}_c
\qquad\text{and}\qquad
\mu\circ(\zeta\times 1)\circ\delta=\eta\circ{!}_c,
$$
where $\delta\colon c\to c\times c$ is the diagonal and $!_c\colon c\to 1$ [@Mac98, §III.6].
Group objects of $\mathbf{Set}$, of $\mathbf{Top}$, and of the category of smooth manifolds are groups, topological groups, and Lie groups.
:::

The inverse axiom uses the diagonal, which the cartesian structure supplies; group objects are therefore defined for a cartesian monoidal structure, while monoid objects need only the data of @def-monoidal-category.

## The Grothendieck group of a monoidal structure {#sec-k0}

::: {#def-k0-monoidal}
## $K_0$ of a symmetric monoidal category

Let $S$ be a symmetric monoidal category whose isomorphism classes of objects form a set $S^{\mathrm{iso}}=\pi_0(S^{\simeq})$.
Then $\otimes$ makes $S^{\mathrm{iso}}$ an abelian monoid with identity $[e]$, and
$$
K_0^{\otimes}(S)
$$
is its group completion: the abelian group with one generator $[s]$ for each isomorphism class and the relations $[s\otimes t]=[s]+[t]$ [@Wei13, §II.5.1.2].

When $S$ has a second symmetric monoidal product that distributes over the first, the group completion inherits a multiplication from it.
For a commutative ring $R$ and the category of finitely generated projective $R$-modules under $\oplus$, the tensor product makes $K_0(R)$ a commutative ring with unit $[R]$ [@Wei13, §II.2].
:::

The set $S^{\mathrm{iso}}$ is $\pi_0$ of the core $S^{\simeq}$ (@def-core), so $K_0^{\otimes}$ is an invariant of isomorphism classes and is functorial for symmetric monoidal functors.
