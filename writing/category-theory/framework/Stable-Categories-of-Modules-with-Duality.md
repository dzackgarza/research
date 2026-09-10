# Stable categories of modules with duality {#sec-stable-duality}

The constructions of this chapter take place over the additive category of modules over a ring, and a form on a module is a morphism of that category.
@sec-form-morphisms lists the hypothesis each construction states, and @sec-hyperbolic-witt gives the hyperbolic forms and Witt classes that the zero-dimensional case reproduces.

## Rings with involution and duality {#sec-ring-with-involution}

::: {#def-ring-with-involution}
## Involutions and the duality functor

An *involution* on a ring $A$ is a ring isomorphism $A\to A^{\mathrm{op}}$, written $a\mapsto\bar a$, with $\bar{\bar a}=a$ for every $a\in A$.
It defines the *duality functor*
$$
(-)^{*}\colon A\text{-}\mathbf{Mod}\longrightarrow A\text{-}\mathbf{Mod},
\qquad
M^{*}=\operatorname{Hom}_A(M,A),
$$
where $M^{*}$ is an $A$-module by $(a\cdot f)(x)=f(x)\,\bar a$, and where the dual of $f\colon M\to N$ is $f^{*}\colon N^{*}\to M^{*}$, $g\mapsto g\circ f$.
For a finitely generated projective $A$-module $M$ the map
$$
\operatorname{can}_M\colon M\longrightarrow M^{**},
\qquad
\operatorname{can}_M(x)(f)=\overline{f(x)},
$$
is an isomorphism [@Ran98, §20].
:::

::: {#def-epsilon-symmetric-form}
## $\epsilon$-symmetric and $\epsilon$-quadratic forms

Let $\epsilon\in A$ be a central unit with $\bar\epsilon=\epsilon^{-1}$.
An *$\epsilon$-symmetric form* $(M,\phi)$ is a finitely generated projective $A$-module $M$ together with an $A$-module morphism $\phi\colon M\to M^{*}$ making the triangle

```{.tikz}
%%| filename: epsilon-symmetry-triangle
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
M
  \arrow[r,"\operatorname{can}_M"]
  \arrow[dr,"\phi"']
&
M^{**} \arrow[d,"\epsilon\,\phi^{*}"]
\\
& M^{*}
\end{tikzcd}
```

commute.
The form is *nonsingular* if $\phi$ is an isomorphism.
An *$\epsilon$-quadratic form* $(M,\psi)$ is a finitely generated projective $A$-module $M$ together with a class of morphisms $\psi\colon M\to M^{*}$ modulo the relation $\psi\sim\psi+\chi-\epsilon\chi^{*}$ for $\chi\in\operatorname{Hom}_A(M,M^{*})$; its *$\epsilon$-symmetrization* is $(M,\psi+\epsilon\psi^{*})$ [@Ran98, Def. 20.1].
In both formulas the dual $\chi^{*}\colon M^{**}\to M^{*}$ of a morphism $M\to M^{*}$ is precomposed with $\operatorname{can}_M$, as in the triangle above.
:::

Take $A=R$ commutative with the identity involution and $\epsilon=1$.
Then a $1$-symmetric form on $M$ is the adjoint map $b^{\sharp}$ of a symmetric $R$-bilinear form $b\colon M\times M\to R$ (@def-form-axioms, @def-polarization), and nonsingularity is the perfectness of @def-polarization.
For $M$ finitely generated projective, the hyperbolic form of @def-hyperbolic-form is a nonsingular $1$-symmetric form by @prp-hyperbolic-adjoint, and $0\oplus M^{*}$ is a lagrangian in the sense of @def-lagrangian by @prp-hyperbolic-metabolic.

## Complexes, duality, and $L$-groups {#sec-poincare-complexes}

::: {#def-chain-complexes}
## Chain complexes in an additive category

Let $\mathcal A$ be an additive category.
A *chain complex* in $\mathcal A$ is a family of objects $C_n$ together with morphisms $d_n\colon C_n\to C_{n-1}$ satisfying $d_{n-1}d_n=0$.
Chain maps are the degreewise morphisms commuting with the differentials, and $\mathbf{Ch}(\mathcal A)$ is again additive [@Wei94, §1.1–1.2].
:::

::: {#thm-dold-kan}
## The Dold–Kan correspondence

Let $\mathcal A$ be an abelian category and let $X$ be a simplicial object of $\mathcal A$, with face maps $d_i$.
The *normalized chain complex* has
$$
N(X)_n=\bigcap_{i=1}^{n}\ker\bigl(d_i\colon X_n\to X_{n-1}\bigr)
$$
and differential induced by $d_0$.
Then $N$ is an equivalence between the category of simplicial objects of $\mathcal A$ and $\mathbf{Ch}_{\geq0}(\mathcal A)$ [@Wei94, Thm. 8.4.1].
:::

::: {#def-comonad-resolution}
## Comonad resolutions and the bar construction

Let $F\colon\mathcal C\to\mathcal A$ be left adjoint to $U\colon\mathcal A\to\mathcal C$.
The composite $\bot=FU$, with counit $\varepsilon\colon\bot\Rightarrow\operatorname{id}_{\mathcal A}$ and comultiplication built from the unit, is a comonad on $\mathcal A$ [@Wei94, Def. 8.6.1, Main Application 8.6.2].
For an object $X$ of $\mathcal A$ the associated augmented simplicial object has $\bot^{\,n+1}X$ in degree $n$, with faces and degeneracies from $\varepsilon$ and the unit, and its chain complex is a resolution of $X$ [@Wei94, §8.6].
For $\mathcal A=A\text{-}\mathbf{Mod}$ and $F$ the free module functor this is the bar resolution, and it computes the derived functors of an additive functor out of $\mathcal A$.
:::

::: {#def-n-dual-complex}
## The $n$-dual of a complex

Let $A$ be a ring with involution and $C$ an $A$-module chain complex, and write $C^{r}=(C_r)^{*}$.
The *$n$-dual* $C^{n-*}$ is the $A$-module chain complex with
$$
(C^{n-*})_r=C^{\,n-r},
\qquad
d_{C^{n-*}}=(-1)^{r}(d_C)^{*},
$$
[@Ran98, §20].
:::

::: {#def-poincare-complex}
## Algebraic Poincaré complexes and $L$-groups

An *$n$-dimensional $\epsilon$-symmetric Poincaré complex* over a ring with involution $A$ is a pair $(C,\phi)$ consisting of an $n$-dimensional $A$-module chain complex $C$ and an $\epsilon$-symmetric structure $\phi$ on $C$ whose component $\phi_0\colon C^{n-*}\to C$ is a chain equivalence; the $\epsilon$-quadratic case replaces $\phi$ by an $\epsilon$-quadratic structure $\psi$ and requires $(1+T_{\epsilon})\psi_0$ to be a chain equivalence, where $T_{\epsilon}$ is the $\epsilon$-transposition involution on $C\otimes_AC$ given by $x\otimes y\mapsto(-1)^{pq}\epsilon\,y\otimes x$ for $x\in C_p$ and $y\in C_q$ [@Ran98, §20].
For a $*$-invariant subgroup $U\subseteq\widetilde K_0(A)$, the *$n$-dimensional $U$-intermediate $\epsilon$-symmetric $L$-group* $L^{n}_{U}(A,\epsilon)$ and its $\epsilon$-quadratic counterpart $L^{U}_{n}(A,\epsilon)$ are the cobordism groups of such complexes with $[C]\in U$ [@Ran98, Def. 20.10].
:::

::: {#thm-l-zero-is-witt}
## The zero-dimensional $L$-group

$L^{0}_{U}(A,\epsilon)$ is the Witt group of nonsingular $\epsilon$-symmetric forms over $A$, and $L^{U}_{0}(A,\epsilon)$ the Witt group of nonsingular $\epsilon$-quadratic forms; a form admitting a lagrangian is zero in it [@Ran98, Ex. 20.11].
:::

For $A=R$ a Dedekind domain with the identity involution and $\epsilon=1$, the group $L^{0}_{\widetilde K_0(R)}(R,1)$ is the additive group of the Witt ring $W(R)$ of @thm-witt-ring, and by @prp-hyperbolic-metabolic every hyperbolic form of @def-hyperbolic-form has the zero class in it.

## Model presentation {#sec-model-presentation}

::: {#def-model-category}
## Model categories

A *model category* is a category together with three classes of maps in it, the fibrations, the cofibrations, and the weak equivalences, satisfying the axioms of [@Qui67, Ch. I §1, Def. 1].
Its *homotopy category* is the localization at the weak equivalences [@Qui67, Ch. I §1, Def. 6].
:::

::: {#thm-projective-model-structure}
## The projective model structure on complexes

Let $\mathcal A$ be an abelian category with enough projectives and let $C_{+}(\mathcal A)$ be the category of chain complexes in $\mathcal A$ that are bounded below.
Then $C_{+}(\mathcal A)$ is a model category in which

- the weak equivalences are the maps inducing isomorphisms on homology,

- the fibrations are the epimorphisms, and

- the cofibrations are the injective maps $i$ for which $\operatorname{coker}i$ has a projective object of $\mathcal A$ in each degree

[@Qui67, Ch. I §1, Ex. B].
The cofibrant replacement of an object of $\mathcal A$ concentrated in degree $0$ is a projective resolution of that object.
:::

In a pointed model category the loop and suspension functors and the fibration and cofibration sequences are constructed on the homotopy category [@Qui67, Ch. I §§2–3].
The corresponding $\infty$-categorical constructions are @def-loops-suspension, and their adjunction is @sec-adjunctions.

## Stabilization {#sec-stabilization-of-modules}

::: {#def-stable-infinity-category}
## Stable $\infty$-categories

An $\infty$-category $\mathcal C$ is *stable* if it has a zero object, every morphism of $\mathcal C$ admits a kernel and a cokernel, and a triangle in $\mathcal C$ is exact if and only if it is coexact [@Lur09, Def. 2.9].
The homotopy category of a stable $\infty$-category is triangulated [@Lur09, Thm. 3.11], a stable $\infty$-category admits all finite limits and colimits [@Lur09, Prop. 4.4], and on it the suspension and loop functors of @def-loops-suspension are mutually inverse equivalences [@Lur09, §2].
:::

For a pointed $\infty$-category $\mathcal C$ admitting the relevant finite limits and colimits, @sec-adjunctions gives
$$
\adj{\mathcal C}{\mathcal C}{\Sigma}{\Omega},
\qquad \Sigma\dashv\Omega.
$$
A pointed $\mathcal C$ is stable if and only if it admits finite limits and colimits and a square in $\mathcal C$ is a pushout if and only if it is a pullback [@Lur09, Prop. 4.4].

::: {#def-prespectrum}
## Prespectrum and spectrum objects

Let $\mathcal C$ be an $\infty$-category.
A *prespectrum object* of $\mathcal C$ is a functor $X\colon\mathrm N(\mathbf Z\times\mathbf Z)\to\mathcal C$ whose value $X(i,j)$ is a zero object of $\mathcal C$ whenever $i\neq j$; write $E_n=X(n,n)$ [@Lur09, Def. 8.1, Rmk. 8.3].
The square of $X$ on the corners $(n,n)$, $(n,n+1)$, $(n+1,n)$, $(n+1,n+1)$ is

```{.tikz}
%%| filename: prespectrum-structure-square
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}
E_n
  \arrow[r]
  \arrow[d]
&
0 \arrow[d]
\\
0 \arrow[r] & E_{n+1}
\end{tikzcd}
```

By @def-loops-suspension the pushout of the span $0\leftarrow E_n\to0$ is $\Sigma E_n$, and the pullback of the cospan $0\to E_{n+1}\leftarrow0$ is $\Omega E_{n+1}$, so the square determines the *structure maps*
$$
\sigma_n\colon\Sigma E_n\longrightarrow E_{n+1},
\qquad
\varepsilon_n\colon E_n\longrightarrow\Omega E_{n+1},
$$
which correspond to one another under $\Sigma\dashv\Omega$.
The prespectrum is a *spectrum object* when every $\varepsilon_n$ is an equivalence; the spectrum objects span a full subcategory $\mathrm{Sp}(\mathcal C)\subseteq\mathrm{PSp}(\mathcal C)$ [@Lur09, Def. 8.4].
:::

::: {#thm-stabilization-universal}
## The universal property of the stabilization

For an $\infty$-category $\mathcal C$ the stabilization $\mathrm{Stab}(\mathcal C)$ is universal among stable $\infty$-categories equipped with a left exact functor to $\mathcal C$ [@Lur09, Prop. 10.12].
The $\infty$-category of spectra is $\mathrm{Sp}=\mathrm{Sp}(\mathcal S_{*})=\mathrm{Stab}(\mathcal S)$ [@Lur09, Def. 9.1], and it is freely generated under colimits, as a stable $\infty$-category, by the sphere spectrum [@Lur09, Cor. 15.6].
:::

::: {#thm-derived-category-heart}
## The derived $\infty$-category

Let $\mathcal A$ be an abelian category with enough projectives.
Then $\mathcal D^{-}(\mathcal A)$ is a stable $\infty$-category, the subcategories of complexes with vanishing homology in negative and in positive degrees determine a $t$-structure on it, and its heart is equivalent to the nerve of $\mathcal A$ [@Lur09, Prop. 13.10].
:::

Taking $\mathcal A=A\text{-}\mathbf{Mod}$ places the complexes of @def-poincare-complex in the stable $\infty$-category $\mathcal D^{-}(A\text{-}\mathbf{Mod})$, whose heart is $A\text{-}\mathbf{Mod}$, and the duality functor of @def-ring-with-involution extends to complexes by @def-n-dual-complex.

## Ring spectra and trace invariants {#sec-ring-spectra-trace}

::: {#def-ring-spectrum}
## Ring spectra and their modules

Let $B$ be a commutative $S$-algebra.
A *$B$-algebra* is a monoid in the symmetric monoidal category of $B$-modules under $\wedge_B$, and a module spectrum over it is a module for that monoid [@EKMM07].
The *enveloping $B$-algebra* of a $B$-algebra $A$ is $A^{e}=A\wedge_B A^{\mathrm{op}}$.
:::

::: {#def-thh}
## Topological Hochschild homology

For a $B$-algebra $A$ and an $(A,A)$-bimodule $M$, the *topological Hochschild homology* of $A$ with coefficients in $M$ is the derived smash product
$$
THH^{B}(A;M)=M\wedge_{A^{e}}A
$$
[@EKMM07, Ch. IX].
When $B$ is a discrete commutative ring and $A$ is a $B$-algebra that is flat as a $B$-module, $\pi_n THH^{B}(A;M)\cong HH^{B}_n(A;M)$ [@EKMM07, Ch. IX].
The simplicial construction of $THH^{B}(A)$ is cyclic, and $THH^{B}(A)$ is an $S^{1}$-equivariant $B$-module [@EKMM07, Ch. IX].
:::

Algebraic $K$-theory of a ring and of an exact category, and the groups $K_n(A)=\pi_nK(A)$, are those of [@Wei13].

## Open statements {#sec-open-statements}

A stabilization of $\mathbf{Lat}_R$ by an endofunctor $F_M$ of @def-hyperbolic-stabilization is asked to do two things at once: to become invertible, so that it presents a stable category, and to move the Witt class, so that it shifts an invariant.
@thm-invertible-summand shows that on $\mathbf{Lat}_R$ these two demands are incompatible: an $M$ with $[M]\neq0$ has $b_M\neq0$ and so $F_M$ is not an equivalence, while an $M$ for which $F_M$ is an equivalence has $[M]=0$ and induces the identity on $W(R)$.
The three statements below are not proved in this book.

**Question.** Let $R$ be a Dedekind domain with $4\cdot1_R\neq0$ and let $S=F_{H(R)}$ be the hyperbolic stabilization of $\mathbf{Lat}_R$ (@def-hyperbolic-stabilization).
Is there a pointed $\infty$-category $\mathcal C$, a functor $\iota\colon\mathbf{Lat}_R^{\simeq}\to\mathcal C^{\simeq}$, and an equivalence $\iota\circ S\simeq\Sigma\circ\iota$ with $\Sigma$ the suspension of @def-loops-suspension?

**Question.** Is there a symmetric monoidal structure on a category built from $\mathbf{Lat}_R$, other than the orthogonal sum of @def-orthogonal-sum, with an invertible object $M$ whose class in $W(R)$ is nonzero?
@thm-invertible-summand answers this for $(\mathbf{Lat}_R,\perp,0)$ itself.

**Question.** Does the discriminant construction of @sec-lattices-discriminant factor through the $\epsilon$-quadratic Poincaré complexes of @def-poincare-complex over $\mathbb Z$, and through which functor?
