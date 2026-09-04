# Bilinear forms on the underlying module of an algebra {#sec-algebra-module-forms}

Fix a commutative ring $R$.
Free modules $M\cong R^{(I)}$ are defined in @def-module-subcategories.
The tensor-hom adjunction of $R\text{-}\mathbf{Mod}$ identifies $R$-bilinear maps $M\times M\to R$ with $R$-module homomorphisms $M\otimes_R M\to R$ [@Mac94]; the former are $\operatorname{Bil}_{R,R}(M)$ in @def-form-presheaves.

## Associative unital $R$-algebras {#sec-r-algebras}

::: {#def-r-algebra}
## Associative unital $R$-algebras

An *associative unital $R$-algebra* is a monoid in $(R\text{-}\mathbf{Mod},\otimes_R,R)$: an $R$-module $A$ together with $R$-linear maps
$$
\mu\colon A\otimes_R A\longrightarrow A,
\qquad
\eta\colon R\longrightarrow A
$$
satisfying the associativity and unitality diagrams [@nlab:associative_algebra].
Equivalently, $A$ is a ring equipped with a ring homomorphism $R\to A$ whose image lies in the centre of $A$.
A homomorphism of associative unital $R$-algebras is an $R$-linear map preserving $\mu$ and $\eta$.
Write $R\text{-}\mathbf{Alg}$ for the resulting category, and
$$
U\colon R\text{-}\mathbf{Alg}\longrightarrow R\text{-}\mathbf{Mod}
$$
for the functor that retains the $R$-module.
Write $R\text{-}\mathbf{CAlg}$ for the full subcategory of $R\text{-}\mathbf{Alg}$ on commutative objects [@nlab:associative_algebra].
:::

The algebra $A$ is already an $R$-module; $U$ names that functor.

## Module bilinear forms and algebra bilinear forms {#sec-two-homs}

::: {#def-module-bilinear-form}
## Module bilinear forms

A *module bilinear form* on an $R$-module $M$, with values in $R$, is an element of
$$
\operatorname{Hom}_{R\text{-}\mathbf{Mod}}(M\otimes_R M,R).
$$
The tensor product is the tensor product of $R$-modules.
By the tensor-hom adjunction this Hom-module is $\operatorname{Bil}_{R,R}(M)$ (@def-form-presheaves).
:::

::: {#def-algebra-bilinear-form}
## Algebra bilinear forms

Let $A$ be an associative unital $R$-algebra.
The tensor product $A\otimes_R A$ in $R\text{-}\mathbf{Alg}$ is the monoid in $R\text{-}\mathbf{Mod}$ whose underlying module is $U(A)\otimes_R U(A)$ and whose multiplication is
$$
(a\otimes b)(c\otimes d)=ac\otimes bd
$$
[@nlab:associative_algebra].
An *algebra bilinear form* on $A$, with values in $R$, is an element of
$$
\operatorname{Hom}_{R\text{-}\mathbf{Alg}}(A\otimes_R A,R).
$$
The tensor product in this Hom is the tensor product of $R$-algebras.
:::

The forgetful functor $U$ sends an algebra bilinear form $\phi$ to a module bilinear form $U(\phi)$ on $U(A)$, using $U(A\otimes_R A)\cong U(A)\otimes_R U(A)$.

::: {#def-algebra-generating-set}
## Algebra generating sets and module bases

Let $A$ be an associative unital $R$-algebra.
The free unital associative $R$-algebra $R\langle S\rangle$ on a set $S$ represents $A\mapsto\mathbf{Set}(S,A)$: a function $S\to A$ of underlying sets extends uniquely to a homomorphism $R\langle S\rangle\to A$ in $R\text{-}\mathbf{Alg}$.

- $A$ is free as an $R$-module on a set $E=\{e_i\}_{i\in I}$ when $U(A)\cong R^{(I)}$ on that basis.
  Every $v\in A$ is then uniquely $v=\sum_{i\in I} v^i e_i$ with finite support in $I$.

- A subset $S\subset A$ *generates $A$ as a unital $R$-algebra* when the unique homomorphism $R\langle S\rangle\to A$ sending each generator to the corresponding element of $S$ is surjective.

Finite algebra generation does not imply that $U(A)$ is finitely generated.
The polynomial ring $R[x]$ is generated as a unital $R$-algebra by $\{x\}$, and is free as an $R$-module on $\{x^n:n\ge 0\}$.
:::

## Gram matrices {#sec-gram-on-algebras}

::: {#prp-gram-matrix-free-module}
## Gram matrix

Let $A$ be free as an $R$-module on $E=\{e_i\}_{i\in I}$, and let $B$ be a module bilinear form on $A$.
The *Gram matrix* of $B$ with respect to $E$ is the family $G_{ij}=B(e_i,e_j)$ indexed by $I\times I$.
If $v=\sum_i a_i e_i$ and $w=\sum_j c_j e_j$, then
$$
B(v,w)=\sum_{i,j\in I} a_i\, G_{ij}\, c_j,
$$
a finite sum by finite support of the coordinates.
Every family $(G_{ij})_{i,j\in I}$ in $R$ arises uniquely in this way.
:::

::: {#prp-eval-via-algebra-map}
## Evaluation through algebra generators

Let $S$ generate $A$ as a unital $R$-algebra, and let $v,w\in A$.
Choose elements $f_v,f_w\in R\langle S\rangle$ with images $v,w$ under $R\langle S\rangle\to A$.
Then $B(v,w)$ is the value of $B$ on those images.
If $A$ is free on a module basis $E$, expand the images in $E$ and apply @prp-gram-matrix-free-module.
The Gram matrix remains indexed by the module basis $E$.
Algebra generators give expressions for the two elements of $A$ on which $B$ is evaluated.
:::

## Associative bilinear forms {#sec-associative-forms}

::: {#def-associative-bilinear-form}
Let $B$ be a module bilinear form on $U(A)$.
The form $B$ is *associative* if
$$
B\circ(\mu\otimes\operatorname{id}_A)
=
B\circ(\operatorname{id}_A\otimes\mu)
\colon
A\otimes_R A\otimes_R A\longrightarrow R,
$$
equivalently $B(xy,z)=B(x,yz)$ for all $x,y,z\in A$.
:::

::: {#thm-associative-is-trace}
## Associative forms and multiplication

Let $A$ be an associative unital $R$-algebra and $B$ a module bilinear form on $U(A)$.
The following are equivalent:

1. $B$ is associative;

2. there exists an $R$-linear map $\varepsilon\colon A\to R$ such that $B(x,y)=\varepsilon(xy)$ for all $x,y\in A$.

If these hold, then $\varepsilon(x)=B(x,1_A)=B(1_A,x)$.

Given (1), set $\varepsilon(x)=B(x,1_A)$.
Then $B(x,y)=B(x,y\cdot 1_A)=B(xy,1_A)=\varepsilon(xy)$, and
$B(1_A,y)=B(1_A,y\cdot 1_A)=B(y,1_A)$.
Given (2), $B(xy,z)=\varepsilon((xy)z)=\varepsilon(x(yz))=B(x,yz)$.
:::

The identification $\varepsilon(x)=B(x,1_A)$ uses the unit of $A$.

::: {#def-frobenius-form}
A linear form $\varepsilon\colon A\to R$ is a *Frobenius form* when $(x,y)\mapsto\varepsilon(xy)$ is perfect in the sense of @def-polarization: the adjoint $A\to\operatorname{Hom}_R(A,R)$ is an isomorphism [@nlab:frobenius_algebra].
:::

::: {#prp-structure-constants}
## Structure constants

Suppose $A$ is free on $E=\{e_i\}_{i\in I}$, and write $e_j e_k=\sum_i\mu^i_{jk}e_i$ with finite support in $i$.
Associativity of $B$ is equivalent to
$$
\sum_k \mu^k_{ij} G_{kl}
=
\sum_k \mu^k_{jl} G_{ik}
$$
for all $i,j,l\in I$.
Under @thm-associative-is-trace this is $G_{ij}=\varepsilon(e_i e_j)=\sum_k\mu^k_{ij}\varepsilon(e_k)$.
The linear form $\varepsilon$ is determined by the family $(\varepsilon(e_i))_{i\in I}$.
:::

## Restriction to algebra generators {#sec-generators-do-not-determine}

::: {#exm-polynomial-forms}
## Forms on $R[x]$

Let $A=R[x]$, generated as a unital $R$-algebra by $\{x\}$ and free as an $R$-module on $\{x^n:n\ge 0\}$.
Let $B_1$ be the zero module bilinear form, and let $B_2$ be the module bilinear form with $B_2(x^i,x^j)=5$ if $(i,j)=(2,2)$ and $B_2(x^i,x^j)=0$ otherwise.
Then $B_1$ and $B_2$ agree on $\operatorname{Span}_R\{1,x\}$, while $B_2(x^2,x^2)=5\neq 0$.

If $B$ is associative, @thm-associative-is-trace gives $B(x,y)=\varepsilon(xy)$.
The values of $B$ on $\operatorname{Span}_R\{1,x\}$ determine $\varepsilon$ on $\{1,x,x^2\}$, and leave $\varepsilon(x^n)$ for $n\ge 3$ free, so $B(x^2,x^2)=\varepsilon(x^4)$ is not determined by those values.
:::

::: {#prp-generators-insufficient}
The restriction of a module bilinear form on $U(A)$ to a finitely generated $R$-submodule does not determine the form on $U(A)$, unless $U(A)$ itself is finitely generated.
The values of $B$ on pairs drawn from a finite algebra generating set therefore do not determine $B$.
:::

## Algebra bilinear forms {#sec-algebra-morphisms-tensor}

::: {#prp-characters-pair}
## Classification

Let $A$ be an object of $R\text{-}\mathbf{CAlg}$.
The tensor product $A\otimes_R A$ of @def-algebra-bilinear-form is the coproduct of $A$ with itself in $R\text{-}\mathbf{CAlg}$, with inclusions $a\mapsto a\otimes 1_A$ and $b\mapsto 1_A\otimes b$.
The coproduct universal property is
$$
\operatorname{Hom}_{R\text{-}\mathbf{CAlg}}(A\otimes_R A,R)
\cong
\operatorname{Hom}_{R\text{-}\mathbf{CAlg}}(A,R)
\times
\operatorname{Hom}_{R\text{-}\mathbf{CAlg}}(A,R).
$$
An algebra bilinear form $\phi\colon A\otimes_R A\to R$ is therefore $\phi(a\otimes b)=\chi_L(a)\chi_R(b)$ for the pair of $R$-algebra homomorphisms $\chi_L,\chi_R\colon A\to R$ given by $\chi_L(a)=\phi(a\otimes 1_A)$ and $\chi_R(b)=\phi(1_A\otimes b)$.

The same formulae classify algebra bilinear forms when $A$ is an object of $R\text{-}\mathbf{Alg}$.
The tensor product is the monoidal tensor of @def-algebra-bilinear-form, and
$$
\phi(a\otimes b)=\phi\bigl((a\otimes 1_A)(1_A\otimes b)\bigr)=\phi(a\otimes 1_A)\phi(1_A\otimes b),
$$
$$
\chi_L(ab)=\phi(ab\otimes 1_A)=\phi\bigl((a\otimes 1_A)(b\otimes 1_A)\bigr)=\chi_L(a)\chi_L(b),
$$
with $\chi_L(1_A)=1_R$, and likewise for $\chi_R$.
The codomain $R$ is commutative.
:::

**Remark.** For objects $A,B,C$ of $R\text{-}\mathbf{CAlg}$, the product $A\times B$ and the coproduct $A\otimes_R B$ give
$$
\operatorname{Hom}_{R\text{-}\mathbf{CAlg}}(C,A\times B)
\cong
\operatorname{Hom}_{R\text{-}\mathbf{CAlg}}(C,A)
\times
\operatorname{Hom}_{R\text{-}\mathbf{CAlg}}(C,B),
$$
$$
\operatorname{Hom}_{R\text{-}\mathbf{CAlg}}(A\otimes_R B,C)
\cong
\operatorname{Hom}_{R\text{-}\mathbf{CAlg}}(A,C)
\times
\operatorname{Hom}_{R\text{-}\mathbf{CAlg}}(B,C).
$$

**Remark.** If $\phi\circ\tau=\phi$ for the flip $\tau(a\otimes b)=b\otimes a$, then $\chi_L=\chi_R$.

::: {#exm-two-characters-polynomials}
## Evaluation at two points

Let $A=R[x]$ and define $\phi(f\otimes g)=f(0)\,g(1)$.
Multiplicativity is $\phi(fh\otimes gk)=f(0)h(0)\,g(1)k(1)=\phi(f\otimes g)\phi(h\otimes k)$, so $\phi$ is an algebra bilinear form on $A$.
Here $\chi_L(f)=f(0)$ and $\chi_R(g)=g(1)$.
These characters are distinct: $\chi_L(x)=0$ and $\chi_R(x)=1$.
Each is determined by the image of the algebra generator $x$.
:::

::: {#prp-character-gram}
If $A$ is free on $E$, the Gram matrix of the module bilinear form $U(\phi)$ is $G_{ij}=\chi_L(e_i)\chi_R(e_j)$.
If $A$ is generated as a unital $R$-algebra by a finite set $S$, each of $\chi_L$ and $\chi_R$ is determined by its values on $S$, subject to the relations of $A$.
:::
