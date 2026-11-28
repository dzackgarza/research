# Discriminant forms and the genus {#sec-discriminant-genus}

::: {.convention #conv:discriminant-lattice-notation title="Discriminant-form notation" defines="$A_L$; $A_{L,q}$"}

Throughout, $L\in\mathbf{Lat}_{\bZ}^{\mathrm{nd}}$.
Write $A_L$ and $A_{L,q}$ for the bilinear and quadratic discriminant objects of @def:discriminant.
:::

::: {.definition #def:rank-of-free-module title="Rank of a free module" defines="rank of a free module"}

Let $R$ be a commutative ring with identity.
Any two bases (@def:based-module) of a free $R$-module have the same cardinality [@Hun74, Ch. IV, Cor. 2.12].
This cardinality is the **rank** of the free module (@def:module-subcategories) [@Hun74, Ch. IV, Def. 2.8].
:::

::: {.definition #def:module-of-finite-length title="Module of finite length" defines="module of finite length; length of a module"}

A module $M$ over a ring is **of finite length** if $M=0$ or $M$ admits a finite filtration $M=M_1\supset M_2\supset\cdots\supset M_r=0$ in which each quotient $M_i/M_{i+1}$ is simple, meaning nonzero with no submodules other than $0$ and itself.
By the Jordan–Hölder theorem the number $r$ of steps of such a filtration is uniquely determined by $M$; it is the **length** of $M$ [@Lan05, Ch. III, §8].
:::

::: {.definition #def:exponent-of-abelian-group title="Exponent of a finite abelian group" defines="exponent of a finite abelian group; exponent of a group"}

Let $A$ be an abelian group (@def:group), written additively.
A positive integer $m$ is an exponent of $A$ if $mx=0$ for every $x\in A$ [@Lan05, Ch. I, §4].
For a finite abelian group $A$, the **exponent** of $A$ is the least positive integer $n$ with $na=0$ for every $a\in A$.
:::

::: {.definition #def:split-short-exact-sequence title="Split short exact sequence" defines="split short exact sequence; split exact sequence"}

Let $0\to A\xrightarrow{f}B\xrightarrow{g}C\to0$ be a short exact sequence (@def:exact-complex) of modules (@def:modules-over-ring).
The sequence is **split** if there is a homomorphism $\varphi\colon C\to B$ with $g\circ\varphi=\mathrm{id}_C$.
In that case $B=\operatorname{Im}f\oplus\operatorname{Im}\varphi$ and $B\cong A\oplus C$ [@Lan05, Ch. III, §3, Prop. 3.2].
Equivalently, $B=f(A)\oplus C'$ for the submodule $C'=\operatorname{Im}\varphi\cong C$.
:::

::: {.definition #def:characteristic-of-field title="Characteristic of a field" defines="characteristic of a field"}

Let $K$ be a field.
The ring homomorphism $\mathbb Z\to K$, $n\mapsto n\cdot1$, has kernel (@def:kernel-cokernel) $n_0\mathbb Z$ for a unique integer $n_0\ge0$.
The **characteristic** of $K$ is $n_0$: the least $n>0$ with $n\cdot1=0$ in $K$ if such $n$ exists, and $0$ otherwise.
It is $0$ or a prime number $p$ [@Lan05, Ch. II, §1].
:::

::: {.definition #def:algebraically-closed-field title="Algebraically closed field" defines="algebraically closed field"}

A field $k$ is **algebraically closed** if every polynomial in $k[X]$ of degree (@def:graded-object) $\ge1$ has a root in $k$ [@Lan05, Ch. IV, §1].
:::

::: {.definition #def:degree-of-polynomial title="Degree of a polynomial" defines="degree of a polynomial"}

For a nonzero polynomial $f=\sum_{i=0}^{n}a_iX^i$ with $a_n\ne0$, the **degree (@def:graded-object)** of $f$ is $n$, the largest exponent occurring in $f$ [@Lan05, Ch. II, §3].
:::

::: {.definition #def:degree-of-field-extension title="Degree of a field extension" defines="degree of a field extension; $[E:F]$"}

For an extension field $E$ of a field $F$, the **degree (@def:graded-object)** $[E:F]$ is the dimension of $E$ as a vector space over $F$, possibly infinite [@Lan05, Ch. V, §1].
:::

::: {.definition #def:primitive-root-of-unity title="Primitive root of unity" defines="primitive root of unity; primitive $m$-th root of unity; $m$-th root of unity"}

Let $k$ be a field.
An element $\zeta\in k$ with $\zeta^m=1$ for some integer $m\ge1$ is an $m$-th root of unity.
If $m$ is not divisible by the characteristic of $k$ (@def:characteristic-of-field), the $m$-th roots of unity in an algebraic closure of $k$ form a cyclic group (@def:group) of order $m$, and a generator of it is a **primitive $m$-th root of unity**, that is, an $m$-th root of unity of exact (@def:exact-complex) multiplicative order $m$ [@Lan05, Ch. VI, §3].
:::

::: {.definition #def:maximal-real-subfield-cyclotomic title="Maximal real subfield of a cyclotomic field" defines="maximal real subfield of a cyclotomic field; maximal totally real subfield of a cyclotomic field; $K^+$"}

Let $\zeta_n$ be a primitive $n$-th root of unity (@def:primitive-root-of-unity) in $\bC$ and let $K=\bQ(\zeta_n)$ be the cyclotomic field of $n$-th roots of unity.
Complex conjugation restricts to the automorphism $\zeta_n\mapsto\zeta_n^{-1}$ of $K$.
The subfield of real elements of $K$ is $K^+=\bQ(\zeta_n+\zeta_n^{-1})$, the **maximal real subfield** of $K$ [@DF04, §14.5, Exercise 7].
:::

::: {.definition #def:norm-element title="Norm element of a group ring" defines="norm element of a group ring; norm element"}

Let $G$ be a finite group (@def:group).
The **norm element** of the group ring $\bZ G$ is the sum $N=\sum_{g\in G}g$.
It is central in $\bZ G$ and satisfies $hN=N=Nh$ for every $h\in G$ [@Wei94, 6.1.8].
:::

::: {.definition #def:nilpotency-index title="Index of nilpotency" defines="nilpotency index; index of nilpotency; nilpotent element"}

An element $z$ of a ring is **nilpotent** if $z^t=0$ for some $t\ge1$.
The **index of nilpotency** of $z$ is the smallest $t$ with $z^t=0$, so that $z^{t-1}\neq0$ [@Jac85, §4.4, exercises].
For an endomorphism $N$ of a module, this is the least $t$ with $N^t=0$ in the ring of endomorphisms.
:::

::: {.definition #def:minimal-prime-ideal title="Minimal prime ideal" defines="minimal prime ideal"}

A prime ideal of a commutative (@def:operation-axioms) ring $A$ is a **minimal prime ideal** if it is a minimal element, for inclusion, of the set of prime ideals of $A$.
If $A\ne0$, this set has minimal elements [@AM18, Ch. 1, Ex. 8].
:::

::: {.definition #def:integrally-closed-ring title="Integrally closed domain" defines="integrally closed ring; integrally closed domain"}

An element of the field of fractions $K$ of an integral domain $A$ is integral over $A$ if it satisfies a monic polynomial with coefficients in $A$.
The domain $A$ is **integrally closed** if every element of $K$ integral over $A$ lies in $A$ [@AM18, Ch. 5].
:::

::: {.definition #def:coble-discriminant-forms title="Length of a lattice" defines="length of a finite $\bZ$-module; minimal number of generators of a finite abelian group; $\ell(A)$; length of a lattice; $\ell(L)$"}

For a finite $\bZ$-module $A$, let $\ell(A)$ be the minimal cardinality of a set of module generators of $A$ [@Nik80, §1.9].
Define $\ell(L)\definedas\ell(A_L)$.
:::

::: {.proposition #prop:discriminant-nondegenerate title="Nondegeneracy and polarization of discriminant forms"}

The bilinear discriminant form (@def:discriminant) $A_L$ is nondegenerate (@def:polarization).
For even (@def:form-axioms) $L$, the quadratic refinement $A_{L,q}$ has bilinearization given by postcomposition of $\bar{\beta}_L$ with
$$
d_L\colon
\tfrac1{N_b(L)}\bZ/\bZ
\too
\tfrac2{N_q(L)}\bZ/2\bZ,
\qquad
a+\bZ\longmapsto2a+2\bZ.
$$
Thus $b_{q_L}=d_L\circ\bar{\beta}_L$.
:::

::: {.proof}
Nondegeneracy is discriminant-pairing duality for the nondegenerate form on $L_\QQ$ [@Nik80, §1.1].
For $x,y\in L^\#$,
$$
q_L\qty{\pi_L(x+y)}
-q_L\qty{\pi_L(x)}
-q_L\qty{\pi_L(y)}
=
2\beta_{L_\QQ}(x,y)+2\bZ
=
d_L\qty{\bar{\beta}_L\qty{\pi_L(x),\pi_L(y)}}.
$$
:::

## Metric-dual identities

::: {.proposition #prop:dual-properties title="Orthogonal sums and twists of metric duals"}

Let $L,M\in\mathbf{Lat}_{\bZ}^{\mathrm{nd}}$ and let $m\in\bZ\setminus\theset{0}$.
Then
$$
\begin{aligned}
(L\perp M)^\#&\isoto L^\#\perp M^\#,\\
(L(m))^\#&\isoto L^\#(1/m),\\
\disc{L(m)}&=m^{\rank L}\disc{L}.
\end{aligned}
$$
:::

::: {.proof}
The first two isomorphisms (@def:isomorphism-of-objects) follow by applying the metric-dual pullback (@def:pullback-square) of @def:metric-dual to the orthogonal-sum and twist functors of @def:form-twist.
The determinant of the twisted adjoint (@def:adjoint-morphism) is $m^{\rank L}$ times the determinant of the original adjoint, which gives the discriminant identity.
:::

## The genus, class set, and spinor genera

::: {.definition #def:spinor-genus-partition title="Spinor genera" defines="$V$; $\mathbb A_{K,f}$; $\widehat R$; $\widehat L$; $V_{\mathbb A_f}$; $\spinornorm_{\mathbb A_f}$; adelic spinor kernel; $\Theta_{\mathbb A_f}(V)$; spinor genus; $\operatorname{SpinGen}(L)$"}

Let $R$ be the ring of integers of a global field $K$, let
$L\in\mathbf{Lat}_R^{\mathrm{nd}}$, put $V\definedas L\tensor_RK$, and let
$\mathbb A_{K,f}$ be the finite adeles of $K$.
Write
$$
\widehat R\definedas\prod_{v\nmid\infty}R_v,
\qquad
\widehat L\definedas L\tensor_R\widehat R,
\qquad
V_{\mathbb A_f}\definedas V\tensor_K\mathbb A_{K,f}.
$$
The local spinor norms (@def:lattice-basic-invariants) (@def:spinor-norm) of @def:spinor-norm assemble to
$$
\spinornorm_{\mathbb A_f}\colon
\Orth(V_{\mathbb A_f})
\too
\mathbb A_{K,f}^{\times}/(\mathbb A_{K,f}^{\times})^2,
$$
and define the adelic spinor kernel by the exact (@def:exact-complex) sequence
$$
1
\too
\Theta_{\mathbb A_f}(V)
\too
\Orth(V_{\mathbb A_f})
\xrightarrow{\spinornorm_{\mathbb A_f}}
\operatorname{im}(\spinornorm_{\mathbb A_f})
\too
1.
$$
For $M\in\operatorname{Gen}(L)$ choose
$\alpha\in\Orth(V_{\mathbb A_f})$ with
$\alpha(\widehat L)=\widehat M$.
The lattices $L$ and $M$ lie in the same **spinor genus** exactly when
$$
\alpha
\in
\Orth(V)\,
\Theta_{\mathbb A_f}(V)\,
\Orth(\widehat L).
$$
The resulting equivalence (@def:equivalence-of-objects) classes partition $\Cl(L)$; their set is denoted
$\operatorname{SpinGen}(L)$.
:::

::: {.proposition #prop:spinor-genus-representative-independent title="The spinor genus does not depend on the adelic representative"}
In @def:spinor-genus-partition, let $\alpha,\alpha'\in\Orth(V_{\mathbb A_f})$ both satisfy $\alpha(\widehat L)=\widehat M=\alpha'(\widehat L)$.
Then $\alpha\in\Orth(V)\,\Theta_{\mathbb A_f}(V)\,\Orth(\widehat L)$ if and only if $\alpha'\in\Orth(V)\,\Theta_{\mathbb A_f}(V)\,\Orth(\widehat L)$.
:::

::: {.proof}
Put $u\definedas\alpha^{-1}\alpha'$.
Then $u(\widehat L)=\alpha^{-1}(\widehat M)=\widehat L$, so $u\in\Orth(\widehat L)$, and $\alpha'=\alpha u$.
Since $\Orth(\widehat L)$ is a group (@def:group), $\Orth(V)\,\Theta_{\mathbb A_f}(V)\,\Orth(\widehat L)\,u=\Orth(V)\,\Theta_{\mathbb A_f}(V)\,\Orth(\widehat L)$.
So $\alpha$ lies in this set if and only if $\alpha u=\alpha'$ does.
:::

::: {.example #ex:binary-same-genus-not-isometric title="Two binary lattices of one genus but distinct isometry classes"}

Let $L$ and $M$ have Gram matrices $\operatorname{diag}(1,55)$ and $\operatorname{diag}(5,11)$, respectively. They belong to the same genus but are not integrally isometric. This is the specimen attributed to Milnor--Husemoller, §II, Example 3, p. 44 in the [original lattice-research assertion](https://github.com/dzackgarza/research/blob/889f214f54198fb4e46fce69be1d80a84b062230/computations/scripts/lattice-research/specs/tests/test_lattices.py#L280-L292).

:::

::: {.proof}

For every odd prime $p$, the matrix
$$
P=\frac14\begin{pmatrix}1&-11\\1&5\end{pmatrix}
$$
belongs to $\operatorname{SL}_2(\ZZ_p)$ and satisfies $P^{\mathsf T}\operatorname{diag}(5,11)P=\operatorname{diag}(1,55)$. For $p=2$, the unit $-43/5$ is congruent to $1$ modulo $8$ and hence is a square in $\ZZ_2$: starting with an odd square root modulo $8$, a root modulo $2^n$ for $n\ge3$ can be adjusted by $2^{n-1}$ to obtain a root modulo $2^{n+1}$, since the change in its square is $2^n$ modulo $2^{n+1}$. The resulting sequence converges in $\ZZ_2$. Choose $a\in\ZZ_2$ with $a^2=-43/5$. Then
$$
Q=\begin{pmatrix}a&-22\\2&5a\end{pmatrix}
$$
has determinant $5a^2+44=1$ and satisfies $Q^{\mathsf T}\operatorname{diag}(5,11)Q=\operatorname{diag}(1,55)$. Both real forms are positive definite. Thus $L$ and $M$ are locally isometric at all places. But $L$ represents $1$ and every nonzero integral vector of $M$ has norm at least $5$, so no integral isometry exists.

:::

::: {.example #ex:rank16-genus-spinor-partition title="A rank-16 genus and its spinor partition"}

Let $L_{16}\definedas E_8^{\perp2}$.
Under @conv:root-sign, $L_{16}$ and $D_{16}^+$ are the two negative-definite even unimodular lattices of rank $16$ up to isometry: this is the $(-1)$-twist of the classical rank-$16$ classification [@CS10, Table 2.2], with $D_{16}^+$ as in @def:plus-construction.
Hence
$$
\Cl(L_{16})
=
\theset{[E_8^{\perp2}],[D_{16}^+]}.
$$
The genus of an even unimodular $\bZ$-lattice is a single spinor genus [@CS10, Ch. 15], so
$$
\operatorname{SpinGen}(L_{16})
=
\theset{\Cl(L_{16})}.
$$
:::

::: {.proposition #prop:eichler-spinor-class title="Eichler's theorem on indefinite spinor genera"}

For $R=\bZ$, every spinor genus (@def:spinor-genus-partition) of an indefinite (@def:definiteness) lattice of rank at least $3$ contains one integral isometry class [@CS10, Ch. 15, Thm. 14].
:::

::: {.proof}

This is [@CS10, Ch. 15, Thm. 14].
:::
## Mass

::: {.definition #def:mass title="Mass of a lattice genus" defines="mass of a lattice genus; $m(L)$"}

When the genus groupoid (@def:genus) $\operatorname{Gen}(L)$ is essentially finite in the sense of @def:groupoid-cardinality, its **mass** is the groupoid cardinality
$m(L)\definedas\cardinality{\operatorname{Gen}(L)}$.
:::
## Brown invariant and Milgram's formula

::: {.definition #def:brown-invariant title="Brown invariant" defines="normalized Gauss sum; $\gamma(A,q)$; Brown invariant; $\operatorname{Br}(A,q)$"}

Let $(A,q)$ be a nondegenerate (@def:polarization) finite quadratic module with $q\colon A\too\bQ/2\bZ$.
Its normalized Gauss sum is
$$
\gamma(A,q)
\definedas
\frac{1}{\sqrt{\cardinality{A}}}
\sum_{x\in A}
\exp\qty{\pi i\,q(x)}
\in\mu_8.
$$
The **Brown invariant** $\operatorname{Br}(A,q)\in\bZ/8\bZ$ is defined by
$$
\gamma(A,q)
=
\exp\qty{2\pi i\,\operatorname{Br}(A,q)/8}.
$$
:::

::: {.theorem #thm:milgram title="Milgram's formula"}

Let $L$ be a nondegenerate (@def:polarization) even lattice (@def:even-lattice) of signature (@def:signature) $(n_+,n_-)$.
Then
$$
\operatorname{Br}(A_{L,q})
\equiv
n_+-n_-
\pmod 8
$$
[@MH73, Ch. II §5, Rem. 2].
:::

::: {.proof}

This is Milgram's theorem [@MH73, Ch. II §5, Rem. 2], proved in Appendix 4 of the same book.
:::

::: {.corollary #cor:primitive-complement-signature title="Signature congruence for primitive complements"}

Let $\iota\colon S\injects\Lambda$ be a primitive embedding into an even unimodular lattice (@def:unimodular), and let $\kappa\colon T\injects\Lambda$ represent its orthogonal complement.
The gluing construction of @cons:embedding-gluing-data gives an isometry $A_{S,q}\isoto A_{T,q}(-1)$.
Hence
$$
\operatorname{Br}(A_{S,q})
=
-\operatorname{Br}(A_{T,q})
\quad\text{in }\bZ/8\bZ,
$$
and @thm:milgram gives $\signature{S}+\signature{T}\equiv0\pmod8$.
:::

::: {.proof}

The signature of a primitive complement is the difference of signatures, which is additivity of @def:signature over the orthogonal splitting (@def:lattice-split) of @thm:orthogonal-decomposition, applied to the embedding whose complement is primitive.
:::
