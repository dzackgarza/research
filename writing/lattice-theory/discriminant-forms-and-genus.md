# Discriminant forms and the genus {#sec-discriminant-genus}

::: {.convention #conv:discriminant-lattice-notation title="Discriminant-form notation" defines="$A_L$; $A_{L,q}$"}

Throughout, $L\in\mathbf{Lat}_{\bZ}^{\mathrm{nd}}$.
Write $A_L$ and $A_{L,q}$ for the bilinear and quadratic discriminant objects of @def:discriminant.
:::

::: {.definition #def:coble-discriminant-forms title="Length of a lattice" defines="length of a finite $\bZ$-module; $\ell(A)$; length of a lattice; $\ell(L)$"}

For a finite $\bZ$-module $A$, let $\ell(A)$ be the minimal (@def:minimal-resolution) cardinality of a set of module generators of $A$ [@Nik80, §1.9].
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
The local spinor norms (@def:lattice-basic-invariants) of @def:spinor-norm assemble to
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
