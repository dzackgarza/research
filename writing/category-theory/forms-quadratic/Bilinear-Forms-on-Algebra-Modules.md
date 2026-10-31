# Bilinear forms on the underlying module of an algebra {#sec-algebra-module-forms}

Fix a commutative ring $R$.
Free modules $M\cong R^{(I)}$ are defined in @def:module-subcategories.
The tensor-hom adjunction of $R\text{-}\mathbf{Mod}$ identifies $R$-bilinear maps $M\times M\to R$ with $R$-module homomorphisms $M\tensor_R M\to R$ [@MM12]; the former are $\Bil_{R,R}(M)$ in @def:form-presheaves.

## Associative unital $R$-algebras {#sec-r-algebras}

::: {.definition #def:r-algebra title="Associative unital $R$-algebras"}

An *associative unital $R$-algebra* is a monoid in $(R\text{-}\mathbf{Mod},\tensor_R,R)$: an $R$-module $A$ together with $R$-linear maps
$$
\mu\colon A\tensor_R A\too A,
\qquad
\eta\colon R\too A
$$
satisfying the associativity and unitality diagrams [@nlab:associative_algebra].
Equivalently, $A$ is a ring equipped with a ring homomorphism $R\to A$ whose image lies in the centre of $A$.
A homomorphism of associative unital $R$-algebras is an $R$-linear map preserving $\mu$ and $\eta$.
Write $R\text{-}\mathbf{Alg}$ for the resulting category, and
$$
U\colon R\text{-}\mathbf{Alg}\too R\text{-}\mathbf{Mod}
$$
for the functor that retains the $R$-module.
Write $R\text{-}\mathbf{CAlg}$ for the full subcategory of $R\text{-}\mathbf{Alg}$ on commutative objects [@nlab:associative_algebra].
:::

The algebra $A$ is already an $R$-module; $U$ names that functor.

## Module bilinear forms and algebra bilinear forms {#sec-two-homs}

::: {.definition #def:module-bilinear-form title="Module bilinear forms"}

A *module bilinear form* on an $R$-module $M$, with values in $R$, is an element of
$$
\Hom_{R\text{-}\mathbf{Mod}}(M\tensor_R M,R).
$$
The tensor product is the tensor product of $R$-modules.
By the tensor-hom adjunction this Hom-module is $\Bil_{R,R}(M)$ (@def:form-presheaves).
:::

::: {.definition #def:algebra-bilinear-form title="Algebra bilinear forms"}

Let $A$ be an associative unital $R$-algebra.
The tensor product $A\tensor_R A$ in $R\text{-}\mathbf{Alg}$ is the monoid in $R\text{-}\mathbf{Mod}$ whose underlying module is $U(A)\tensor_R U(A)$ and whose multiplication is
$$
(a\tensor_R b)(c\tensor_R d)=ac\tensor_R bd
$$
[@nlab:associative_algebra].
An *algebra bilinear form* on $A$, with values in $R$, is an element of
$$
\Hom_{R\text{-}\mathbf{Alg}}(A\tensor_R A,R).
$$
The tensor product in this Hom is the tensor product of $R$-algebras.
:::

The forgetful functor $U$ sends an algebra bilinear form $\phi$ to a module bilinear form $U(\phi)$ on $U(A)$, using $U(A\tensor_R A)\cong U(A)\tensor_R U(A)$.

::: {.definition #def:algebra-generating-set title="Algebra generating sets and module bases"}

Let $A$ be an associative unital $R$-algebra.
The free unital associative $R$-algebra $R\langle S\rangle$ on a set $S$ represents $A\mapsto\mathbf{Set}(S,A)$: a function $S\to A$ of underlying sets extends uniquely to a homomorphism $R\langle S\rangle\to A$ in $R\text{-}\mathbf{Alg}$.

- $A$ is free as an $R$-module on a set $E=\{e_i\}_{i\in I}$ when $U(A)\cong R^{(I)}$ on that basis.
  Every $v\in A$ is then uniquely $v=\Sum_{i\in I} v^i e_i$ with finite support in $I$.

- A subset $S\subset A$ *generates $A$ as a unital $R$-algebra* when the unique homomorphism $R\langle S\rangle\to A$ sending each generator to the corresponding element of $S$ is surjective.

Finite algebra generation does not imply that $U(A)$ is finitely generated.
The polynomial ring $R[x]$ is generated as a unital $R$-algebra by $\{x\}$, and is free as an $R$-module on $\{x^n:n\ge 0\}$.
:::

## Gram matrices {#sec-gram-on-algebras}

The Gram matrix of a module bilinear form on a free module is @prop:gram-matrix-free-module, and its change under a change of basis is @prop:gram-congruence.
For an algebra $A$ free as an $R$-module on $E$, both apply to $U(A)$ with the module basis $E$.

::: {.remark}

Let $S$ generate $A$ as a unital $R$-algebra and let $\pi\colon R\langle S\rangle\to A$ be the surjection of @def:algebra-generating-set.
For $v,w\in A$ and any $f_v,f_w$ with $\pi(f_v)=v$ and $\pi(f_w)=w$ one has $B(v,w)=B(\pi f_v,\pi f_w)$, which is a restatement of $\pi f_v=v$ and carries no further information.
So algebra generators supply *expressions* for the two arguments of $B$; they do not supply its values, and by @prop:generators-insufficient the values on a generating set do not determine the form.
If $A$ is free on a module basis $E$, such an expression is expanded in $E$ and evaluated by @prop:gram-matrix-free-module, the Gram matrix being indexed by $E$ and not by $S$.
:::

## Associative bilinear forms {#sec-associative-forms}

::: {.definition #def:associative-bilinear-form title="Associative bilinear forms"}
Let $B$ be a module bilinear form on $U(A)$.
The form $B$ is *associative* if
$$
B\circ(\mu\tensor_R\id_A)
=
B\circ(\id_A\tensor_R\mu)
\colon
A\tensor_R A\tensor_R A\too R,
$$
equivalently $B(xy,z)=B(x,yz)$ for all $x,y,z\in A$.
:::

::: {.theorem #thm:associative-is-trace title="Associative forms and multiplication"}

Let $A$ be an associative unital $R$-algebra and $B$ a module bilinear form on $U(A)$.
The following are equivalent:

1. $B$ is associative;

2. there exists an $R$-linear map $\eps\colon A\to R$ such that $B(x,y)=\eps(xy)$ for all $x,y\in A$.

If these hold, then $\eps(x)=B(x,1_A)=B(1_A,x)$.
:::

::: {.proof}

From (1) to (2): set $\eps(x)\definedas B(x,1_A)$, which is $R$-linear in $x$.
Associativity of $B$ in the form $B(xy,z)=B(x,yz)$ applied with $z=1_A$ gives $B(x,y)=B(xy,1_A)=\eps(xy)$.
Applying it with $x=1_A$ gives $B(1_A,y)=B(1_A,y\,1_A)=B(y,1_A)=\eps(y)$, so the two readings agree.

From (2) to (1): if $B(x,y)=\eps(xy)$ then $B(xy,z)=\eps((xy)z)=\eps(x(yz))=B(x,yz)$, which is associativity by @def:associative-bilinear-form.
:::

::: {.remark}

The identification $\eps(x)=B(x,1_A)$ uses the unit of $A$: without $\eta$ there is no element $1_A$ to evaluate against, and $B(xy,z)=B(x,yz)$ need not be expressible as a single linear functional.
:::

::: {.definition #def:frobenius-form title="Frobenius forms"}
A linear form $\eps\colon A\to R$ is a *Frobenius form* when $(x,y)\mapsto\eps(xy)$ is perfect in the sense of @def:polarization: both adjoint maps $A\to\Hom_R(A,R)$ are isomorphisms [@nlab:frobenius_algebra].
:::

::: {.proposition #prop:structure-constants title="Structure constants"}

Suppose $A$ is free on $E=\{e_i\}_{i\in I}$, and write $e_j e_k=\Sum_i\mu^i_{jk}e_i$ with finite support in $i$.
Associativity of $B$ is equivalent to
$$
\Sum_k \mu^k_{ij} G_{kl}
=
\Sum_k \mu^k_{jl} G_{ik}
$$
for all $i,j,l\in I$, where $G_{ij}=B(e_i,e_j)$.
:::

::: {.proof}

By @thm:associative-is-trace, $B$ is associative exactly when $B(x,y)=\eps(xy)$ for a linear form $\eps$, and then
$$
G_{ij}=B(e_i,e_j)=\eps\qty{\Sum_k\mu^k_{ij}e_k}=\Sum_k\mu^k_{ij}\eps(e_k),
$$
a finite sum by the support condition on $\mu$.
So the Gram matrix is over-determined by the single family $\eps(e_k)_{k\in I}$, and $\eps$ is determined by that family because $E$ is a basis.

The displayed identity is associativity evaluated on a triple of basis vectors: with $z=e_l$,
$$
B(e_ie_j,e_l)=\Sum_k\mu^k_{ij}B(e_k,e_l)=\Sum_k\mu^k_{ij}G_{kl},
\qquad
B(e_i,e_je_l)=\Sum_k\mu^k_{jl}B(e_i,e_k)=\Sum_k\mu^k_{jl}G_{ik},
$$
and $B(xy,z)=B(x,yz)$ for all $x,y,z$ is equivalent to its holding on the basis, since both sides are trilinear.
:::

## Restriction to algebra generators {#sec-generators-do-not-determine}

::: {.example #ex:polynomial-forms title="Forms on $R[x]$"}

Let $A=R[x]$, generated as a unital $R$-algebra by $\{x\}$ and free as an $R$-module on $\{x^n:n\ge 0\}$.
Let $B_1$ be the zero module bilinear form, and let $B_2$ be the module bilinear form with $B_2(x^i,x^j)=5$ if $(i,j)=(2,2)$ and $B_2(x^i,x^j)=0$ otherwise.
Then $B_1$ and $B_2$ agree on $\operatorname{Span}_R\{1,x\}$, while $B_2(x^2,x^2)=5\neq 0$.

If $B$ is associative, @thm:associative-is-trace gives $B(x,y)=\eps(xy)$.
The values of $B$ on $\operatorname{Span}_R\{1,x\}$ determine $\eps$ on $\{1,x,x^2\}$, and leave $\eps(x^n)$ for $n\ge 3$ free, so $B(x^2,x^2)=\eps(x^4)$ is not determined by those values.
:::

::: {.proposition #prop:generators-insufficient title="Algebra generators do not determine module bilinear forms"}

Suppose $U(A)$ is free on a basis $E$ that is not finite, and let $M\subseteq U(A)$ be a finitely generated submodule.
Then there are distinct module bilinear forms on $U(A)$ that agree on $M\times M$.
In particular the values of $B$ on pairs drawn from a finite algebra generating set do not determine $B$.
:::

::: {.proof}

A finitely generated submodule of a free module is contained in the span of a finite subset $E_0\subseteq E$, since each of finitely many generators involves finitely many basis vectors; so it suffices to treat $M\subseteq\operatorname{Span}_R E_0$.
Choose $e\in E\setminus E_0$.
The forms
$$
B_1\definedas0,
\qquad
B_2(e,e)\definedas1,\quad B_2\text{ zero on every other pair of basis vectors},
$$
are distinct and both vanish on $M\times M$, because every element of $M$ is a combination of basis vectors in $E_0$ and the cross terms $B_2(e,\text{-})$ and $B_2(\text{-},e)$ vanish off $e$.
Both are bilinear by @prop:gram-matrix-free-module, applied to their Gram matrices.

A finite algebra generating set spans only finitely many basis vectors, so the same construction applies to the submodule it spans.
The hypothesis that $E$ is infinite is what supplies $e\notin E_0$; when $U(A)$ is finitely generated the argument has no $e$ to choose, which is why the statement excludes that case.
:::

## Algebra bilinear forms {#sec-algebra-morphisms-tensor}

::: {.proposition #prop:characters-pair title="Classification"}

Let $A$ be an object of $R\text{-}\mathbf{CAlg}$.
The tensor product $A\tensor_R A$ of @def:algebra-bilinear-form is the coproduct of $A$ with itself in $R\text{-}\mathbf{CAlg}$, with inclusions $a\mapsto a\tensor_R 1_A$ and $b\mapsto 1_A\tensor_R b$.
The coproduct universal property is
$$
\Hom_{R\text{-}\mathbf{CAlg}}(A\tensor_R A,R)
\cong
\Hom_{R\text{-}\mathbf{CAlg}}(A,R)
\times
\Hom_{R\text{-}\mathbf{CAlg}}(A,R).
$$
An algebra bilinear form $\phi\colon A\tensor_R A\to R$ is therefore $\phi(a\tensor_R b)=\chi_L(a)\chi_R(b)$ for the pair of $R$-algebra homomorphisms $\chi_L,\chi_R\colon A\to R$ given by $\chi_L(a)=\phi(a\tensor_R 1_A)$ and $\chi_R(b)=\phi(1_A\tensor_R b)$.

The same formulae classify algebra bilinear forms when $A$ is an object of $R\text{-}\mathbf{Alg}$, not necessarily commutative.
:::

::: {.proof}

Write $\iota_L(a)\definedas a\tensor_R1_A$, $\iota_R(b)\definedas1_A\tensor_Rb$ and $\chi_L\definedas\phi\circ\iota_L$, $\chi_R\definedas\phi\circ\iota_R$; both are $R$-linear, and $\phi$ is an $R$-algebra homomorphism, so multiplicative and unital.

The factorization $a\tensor_Rb=(a\tensor_R1_A)(1_A\tensor_Rb)=\iota_L(a)\iota_R(b)$ holds in $A\tensor_RA$ by the multiplication of @def:algebra-bilinear-form, hence
$$
\phi(a\tensor_Rb)=\phi\bigl(\iota_L(a)\iota_R(b)\bigr)=\phi(\iota_L a)\phi(\iota_R b)=\chi_L(a)\chi_R(b).
$$
So $\phi$ is determined by the pair, and $\chi_L(1_A)=\phi(1_A\tensor_R1_A)=1_R$ by unitality of $\phi$.

That each $\chi$ is itself multiplicative, which is what makes the classification a bijection onto pairs of algebra homomorphisms, uses the tensor product being that of $R\text{-}\mathbf{Alg}$ and the codomain $R$ being commutative:
$$
\chi_L(ab)=\phi\bigl(ab\tensor_R1_A\bigr)=\phi\bigl(\iota_L(a)\iota_L(b)\bigr)=\phi(\iota_La)\phi(\iota_Lb)=\chi_L(a)\chi_L(b),
$$
and likewise for $\chi_R$; conversely a pair of $R$-algebra homomorphisms defines $\phi(a\tensor_Rb)\definedas\chi_L(a)\chi_R(b)$, which is multiplicative because both factors are and $R$ is commutative.
:::

::: {.remark}
For objects $A,B,C$ of $R\text{-}\mathbf{CAlg}$, the product $A\times B$ and the coproduct $A\tensor_R B$ give
$$
\Hom_{R\text{-}\mathbf{CAlg}}(C,A\times B)
\cong
\Hom_{R\text{-}\mathbf{CAlg}}(C,A)
\times
\Hom_{R\text{-}\mathbf{CAlg}}(C,B),
$$
$$
\Hom_{R\text{-}\mathbf{CAlg}}(A\tensor_R B,C)
\cong
\Hom_{R\text{-}\mathbf{CAlg}}(A,C)
\times
\Hom_{R\text{-}\mathbf{CAlg}}(B,C).
$$

:::

::: {.remark}
If $\phi\circ\tau=\phi$ for the flip $\tau(a\tensor_R b)=b\tensor_R a$, then $\chi_L=\chi_R$.
:::

::: {.example #ex:two-characters-polynomials title="Evaluation at two points"}

Let $A=R[x]$ and define $\phi(f\tensor_R g)=f(0)\,g(1)$.
Multiplicativity is $\phi(fh\tensor_R gk)=f(0)h(0)\,g(1)k(1)=\phi(f\tensor_R g)\phi(h\tensor_R k)$, so $\phi$ is an algebra bilinear form on $A$.
Here $\chi_L(f)=f(0)$ and $\chi_R(g)=g(1)$.
These characters are distinct: $\chi_L(x)=0$ and $\chi_R(x)=1$.
Each is determined by the image of the algebra generator $x$.
:::

::: {.proposition #prop:character-gram title="Gram matrices from characters"}
If $A$ is free on $E$, the Gram matrix of the module bilinear form $U(\phi)$ is $G_{ij}=\chi_L(e_i)\chi_R(e_j)$.
If $A$ is generated as a unital $R$-algebra by a finite set $S$, each of $\chi_L$ and $\chi_R$ is determined by its values on $S$, subject to the relations of $A$.
:::

::: {.proof}

The first sentence is @prop:characters-pair evaluated on a pair of basis vectors: $G_{ij}=U(\phi)(e_i,e_j)=\phi(e_i\tensor_Re_j)=\chi_L(e_i)\chi_R(e_j)$.
So the Gram matrix of $U(\phi)$ is the rank-one matrix $\chi_L\chi_R^{\mathsf T}$ over the basis $E$, and in particular it has rank at most one whatever the size of $E$.

For the second, a unital $R$-algebra homomorphism $\chi\colon A\to R$ out of a generated algebra is determined by its restriction to the generators, since $\chi$ is $R$-linear and multiplicative and every element of $A$ is a polynomial in $S$.
Not every assignment extends: $\chi$ must kill the relations, which is exactly the content of the universal property of $R\langle S\rangle$ in @def:algebra-generating-set, and the assignments that extend are the homomorphisms $R\langle S\rangle/(\text{relations})\to R$.
:::
