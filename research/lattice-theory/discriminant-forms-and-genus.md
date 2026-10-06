# Discriminant forms and the genus

::: {.convention #conv:discriminant-lattice-notation title="Discriminant-form notation"}

Throughout, $L$ denotes a nondegenerate integral lattice.
Its bilinear discriminant form is
$$
A_L
=
\coker_{\mathbf{BilMod}_{\bZ}}(\boldsymbol\iota_L)
$$
from @def:discriminant.
If $L$ is even, its quadratic discriminant form is the separate object $A_{L,q}$.
Thus $A_L$ always means the bilinear discriminant form; the subscript $q$ is never omitted for the quadratic refinement.

If $N=N(L)$ is the arithmetic level of @def:lattice-level, then the value modules are
$$
A_L:\quad \tfrac1N\bZ/\bZ,
\qquad
A_{L,q}:\quad \tfrac2N\bZ/2\bZ.
$$
:::

::: {.definition #def:coble-discriminant-forms title="Discriminant bilinear and quadratic forms"}

This chapter uses the canonical objects of @def:discriminant without redefining them.
The carrier module of both $A_L$ and, when defined, $A_{L,q}$ is $L^\#/L$.
Define
$$
\ell(L)
\definedas
\ell(L^\#/L),
$$
the minimal number of generators of that finite-length $\bZ$-module.
:::

::: {.proposition #prop:discriminant-nondegenerate title="Nondegeneracy and polarization of discriminant forms"}

The bilinear discriminant form $A_L$ is nondegenerate.
If $L$ is even, the quadratic discriminant form $A_{L,q}$ is nondegenerate and its bilinearization is related to the bilinear discriminant form by the canonical value-module isomorphism
$$
\mu_{2,N}\colon
\tfrac1N\bZ/\bZ
\isoto
\tfrac2N\bZ/2\bZ,
\qquad
a+\bZ\longmapsto2a+2\bZ.
$$
Explicitly,
$$
b_{q_L}
=
\mu_{2,N}\circ\bar\beta_L.
$$
:::

::: {.proof}
Nondegeneracy of $A_L$ is the standard discriminant-pairing duality induced by the nondegenerate form on $L_\QQ$ [@Nik80, §1.1].
For $x,y\in L^\#$,
$$
q_L(x+y)-q_L(x)-q_L(y)
=
2\beta_{L_\QQ}(x,y)+2\bZ,
$$
which is exactly $\mu_{2,N}(\bar\beta_L(x+L,y+L))$.
:::

## Properties of the dual lattice

::: {.proposition #prop:dual-properties}

Let $L$ and $M$ be nondegenerate lattices.
The dual lattice $\dualof{L} = \Hom_\ZZ(L, \ZZ)$ satisfies the following.

1. Duality commutes with orthogonal direct sums: $\dualof{(L\oplus M)} = \dualof{L} \oplus \dualof{M}$.

2. If $L$ has Gram matrix $G_\beta$ in a basis $B_L$, then the dual basis is $B_{\dualof{L}} = \inverseof{(B_L^t)}$, and the Gram matrix of the dual form is $G_{\dualof{\beta}} = \inverseof{G_\beta}$.

3. The discriminant of the dual satisfies $\disc(\dualof{L}) = 1/\disc(L)$.

4. The dual of a twist is $\dualof{(L(m))}=\dualof{L}(1/m)$ for the twist $L(m)$ of @def:form-twist.
:::

::: {.proof}
Property (2) is the source of (3), since $\disc(\dualof{L}) = \det(\inverseof{G_\beta}) = 1/\det(G_\beta) = 1/\disc(L)$.
Property (1) induces the canonical discriminant decomposition $A_{L\oplus M}\isoto A_L\oplus A_M$ through the cokernel sequence of @def:discriminant.
:::

## Geometric identification of the dual lattice

::: {.theorem #thm:dual-geometric-identification title="The metric dual as a pullback"}
The adjoint isomorphism of the rational scalar extension
$$
\beta_{L_\QQ}^\sharp\colon L_\QQ\isoto L^\vee\tensor_\ZZ\QQ
$$
identifies the metric dual with the pullback
```tikzcd
L^\# \arrow[r] \arrow[d] & L_\QQ \arrow[d,"\beta_{L_\QQ}^\sharp"] \\
L^\vee \arrow[r] & L^\vee\tensor_\ZZ\QQ .
```
The left vertical morphism is therefore an isomorphism $L^\#\isoto L^\vee$, and the canonical maps form composable monomorphisms
$$
L\xrightarrow{\iota_L}L^\#\longrightarrow L_\QQ.
$$
:::

::: {.proof}
The lower horizontal morphism is scalar extension along $\ZZ\to\QQ$. By the defining pullback property of @def:metric-dual, its pullback along $\beta_{L_\QQ}^\sharp$ is $L^\#$; since the right vertical morphism is an isomorphism, projection to $L^\vee$ identifies the pullback with $L^\vee$. The composite $L\xrightarrow{\iota_L}L^\#\to L_\QQ$ is the scalar-extension monomorphism.
:::

## The genus, class set, and class number

::: {.definition #def:coble-genus title="Class set and class number"}
The genus $\operatorname{Gen}(L)$ is the pointed set of @def:genus. Write
$\cl(L)\definedas\operatorname{Gen}(L)$ for this **class set** of integral isometry classes, pointed by $[L]$.
Its **class number** is $h(L)\definedas\abs{\cl(L)}$.
:::

::: {.proposition #prop:eichler-spinor-class title="Eichler's theorem and class number"}
An indefinite spinor genus of rank at least $3$ contains a single integral isometry class [@CS10, Ch. 15, Thm. 14].
Hence for an indefinite lattice of rank at least $3$, $h(L)$ equals the number of spinor genera in $\operatorname{Gen}(L)$; in particular, $h(L)=1$ exactly when the genus contains one spinor genus.
For definite lattices, a spinor genus may contain several integral isometry classes.
:::

## Spinor genera and their class counts

::: {.definition #def:spinor-genus-partition title="Spinor genera and their class numbers"}

Let $V=L_\QQ$, and for every prime $p$ write $V_p=V\tensor_\QQ\QQ_p$ and $L_p=L\tensor\ZZ_p$.
Let $I_p\definedas\im(\theta_p)$ for the local spinor norm
$$
\theta_p\colon \Orth(V_p)\too \QQ_p^\times/(\QQ_p^\times)^2.
$$
Define $\Theta(V_p)$ by the short exact sequence
$$
1\too\Theta(V_p)\too\Orth(V_p)\xrightarrow{\theta_p}I_p\too1.
$$
Two lattices $L$ and $M$ in the same rational quadratic space lie in the same **spinor genus** if there is a rational isometry $g\in O(V)$ and elements $\sigma_p\in\Theta(V_p)$ for every prime $p$, with $\sigma_p$ equal to the identity for almost all $p$, such that
$$
g(M_p)=\sigma_p(L_p)
$$
for every $p$.
This is the improper spinor-genus convention; replacing $O(V)$ by $\SO(V)$ gives the proper spinor genus.
Equivalently one may use the spinor operators of [@CS10, Ch. 15, §9].
Thus every genus is a disjoint union of spinor genera, and each spinor genus is a union of isometry classes.

Write
$$
s(L)=\#\theset{\text{spinor genera contained in }\operatorname{Gen}(L)}
$$
and, for a spinor genus $\mathfrak s$, write
$$
h(\mathfrak s)=\#\theset{\text{isometry classes contained in }\mathfrak s}.
$$
The number $s(L)$ is a power of $2$ [@CS10, Ch. 15, §9.1], and
$$
h(\operatorname{Gen}(L))
=
\sum_{\mathfrak s\subset\operatorname{Gen}(L)}h(\mathfrak s).
$$
For indefinite lattices of rank at least $3$, Eichler's theorem gives one isometry class in each spinor genus under the improper-isometry convention [@CS10, Ch. 15, Thm. 14].
:::


::: {.proposition #prop:scattone-bound}

If $\rank(L) > 16 + \ell(L)$, where $\ell(L)$ is the length of the discriminant-form definition (@def:coble-discriminant-forms), then the class number satisfies $\abs{\cl(L)} \geq 2$.
:::

::: {.proof}

This is the bound of [@Sca87].
:::

## Local invariants and the Jordan decomposition

::: {.definition #def:scale-norm-volume title="Scale, norm, and volume"}

Let $(L, \beta_L)$ be a lattice.
Its **scale** is the ideal generated by all pairings and its **norm** the ideal generated by all squares,
$$
\mathfrak{s}(L) \definedas \gcd\theset{\beta_L(x, y) \mid x, y\in L}\,\ZZ,
\qquad
\mathfrak{n}(L) \definedas \gcd\theset{\beta_L(x, x) \mid x\in L}\,\ZZ
,
$$
and its **volume** is the index ideal $\mathfrak{v}(L)\definedas\abs{\det G_L}\,\ZZ = \abs{A_L}\,\ZZ$.
One has $\mathfrak{n}(L)\iscontainedin\mathfrak{s}(L)$, and $L$ is integral exactly when $\mathfrak{s}(L)\iscontainedin\ZZ$.
Under the twist of @def:form-twist, $\mathfrak{s}(L(m)) = m\,\mathfrak{s}(L)$, $\mathfrak{n}(L(m)) = m\,\mathfrak{n}(L)$ and $\mathfrak{v}(L(m)) = m^{r}\,\mathfrak{v}(L)$ for $r = \rank(L)$.
:::

::: {.definition #def:local-modular-lattice title="Local modular Jordan constituents"}

Let $M$ be a nondegenerate $\ZZ_p$-lattice.
It is **$p^s$-modular** when, under the natural identification of $M^\vee$ with a lattice in $M\tensor_{\ZZ_p}\QQ_p$,
$$
p^s M^\vee=M.
$$
This is the local homothetic notion used in a Jordan decomposition.
It should not be confused with the global notion of an $N$-modular integral lattice in the global modularity definition (@def:modular-lattice-global), where one asks for a similarity $L\iso L^\vee(N)$ rather than literal equality inside a fixed rational realization.
:::

::: {.theorem #thm:jordan-decomposition title="Jordan decomposition"}

Let $L$ be a nondegenerate lattice and $p$ a prime.
Then $L_{\ZZ_p} = L\tensor_\ZZ\ZZ_p$ admits an orthogonal decomposition
$$
L_{\ZZ_p} = L_1 \operatorname{\perp} L_2 \operatorname{\perp}\cdots\operatorname{\perp} L_k
,
$$
in which each $L_i$ is $p^{s_i}$-modular and $s_1 < s_2 < \cdots < s_k$.
Such a decomposition exists and is unique up to isometry, and the scales $p^{s_i}$ and the ranks $\rank(L_i)$ are invariants of $L$ at $p$.
:::

::: {.proposition #prop:genus-jordan-criterion title="Genus via Jordan decompositions"}
Two integral lattices lie in the same genus of @def:genus precisely when they have the same real signature and isometric Jordan decompositions at every prime.
For a $2$-elementary lattice only the primes $2$ and the archimedean place carry information, and the Jordan decomposition at $2$ is assembled from the rank-two $2$-adic lattices $V_k$ and $U_k$ from Nikulin's $V_k,U_k$ definition (@def:nikulin-Vk-Uk) together with rank-one summands.
:::

## Conway--Sloane genus symbols

::: {.definition #def:conway-sloane-genus-symbol title="Conway--Sloane genus symbol"}

For each prime $p$, write a Jordan decomposition of $L_p=L\tensor\ZZ_p$ as an orthogonal direct sum
$$
L_p\iso\bigoplus_j p^j L_{p,j},
$$
with each $L_{p,j}$ unimodular over $\ZZ_p$.
The **Conway--Sloane $p$-adic symbol** is the canonical symbol encoding the isometry classes of these Jordan constituents: for odd $p$ it records their scales, ranks, and determinant square classes, and for $p=2$ it additionally records the type-I/type-II and oddity data together with the canonical compartment conventions.
The **Conway--Sloane genus symbol** combines the real signature and parity of $L$ with these local symbols.
Only the primes dividing $2\disc L$ carry nontrivial local data beyond the unimodular constituent determined by the global invariants.
See [@CS10, Ch. 15, §§7.5--7.8].
:::


## The discriminant representation

::: {.definition #def:discriminant-representation-image title="Image and coset space of the quadratic discriminant representation"}

Let $L$ be a nondegenerate even lattice.
Use the quadratic discriminant representation of @def:discriminant-rep,
$$
\rho_{L,q}\colon\Orth(L)\too\Orth(A_{L,q}),
$$
and write
$$
\Orth(L)\twoheadrightarrow I_{L,q}\injects\Orth(A_{L,q})
$$
for its epi--mono factorization.
Define the pointed left-coset set
$$
\mathcal C_{L,q}
\definedas
\Orth(A_{L,q})/I_{L,q},
$$
pointed by $I_{L,q}$.
It is a quotient group exactly when $I_{L,q}\trianglelefteq\Orth(A_{L,q})$.
:::


## The mass formula as a class-number criterion

::: {.definition #def:mass title="The mass of a genus"}

Let $L$ be a positive definite lattice and let $L^{(1)}, \ldots, L^{(h)}$ be representatives of the isometry classes in the genus of $L$, so that $h = \abs{\cl(L)}$ in the notation of the genus definition (@def:coble-genus).
The **mass** of the genus is
$$
m(L) \definedas \Sum_{i=1}^{h} \frac{1}{\abs{\Orth(L^{(i)})}}
.
$$
:::

::: {.proposition #prop:mass-class-number-one title="Mass criterion for class number one"}
The mass is computable from local data alone: the Smith--Minkowski--Siegel mass formula expresses $m(L)$ as a product of an archimedean factor and one $p$-adic factor for each prime, each factor read off from the Jordan decomposition of the Jordan-decomposition theorem (@thm:jordan-decomposition); the explicit unimodular cases are tabulated in [@CS10 Ch. 16].
Since each summand of @def:mass is positive,
$$
m(L) = \frac{1}{\abs{\Orth(L)}}
\quad\Longleftrightarrow\quad
\abs{\cl(L)} = 1
.
$$
:::

## Surjectivity onto the discriminant group

::: {.theorem #thm:two-elementary-surjectivity title="$\Orth(H)\to\Orth(A_{H,q})$ is surjective for indefinite $2$-elementary $H$"}

Let $H$ be an indefinite even $2$-elementary lattice.
Then the quadratic discriminant representation
$$
\rho_{H,q}\colon\Orth(H)\twoheadrightarrow\Orth(A_{H,q})
$$
is surjective.
:::

::: {.proof}

This is [@Nik80]; see [@Ale22 §4] for the statement in this form.
:::


## Invariants that do not classify

::: {.theorem #thm:milgram title="Milgram's formula"}

Let $L$ be a nondegenerate even lattice with quadratic discriminant form $A_{L,q}$ and signature $(n_+,n_-)$.
Then
$$
\Sum_{\lambda\in L^\#/L}
e\!\left(\tfrac12 q_L(\lambda)\right)
=
\sqrt{\abs{L^\#/L}}\;
e\!\left(\frac{n_+-n_-}{8}\right),
\qquad
e(z)\definedas e^{2\pi i z}.
$$
In particular $A_{L,q}$ determines $n_+-n_-$ modulo $8$.
:::

::: {.proof}

This is the Gauss-sum formula of [@MH73 Appendix 4].
:::

::: {.proposition #prop:milgram-information title="Information carried by Milgram's formula"}
For an even lattice, the quadratic discriminant form $A_{L,q}$ determines $n_+-n_-$ modulo $8$ by @thm:milgram, but it does not determine the full signature or the integral isometry class.
The Arf invariant of the reduction of $q_L$ modulo $\ZZ$ loses information retained by $A_{L,q}$, while the Brown invariant records only $n_+-n_-$ modulo $8$.
The signature $(n_+,n_-)$ together with $A_{L,q}$ determines the genus [@Nik80], but a genus may contain several spinor genera and hence several integral isometry classes.
:::

::: {.corollary #cor:primitive-complement-signature title="Signature congruence for primitive complements"}
Let $\iota\colon S\injects\Lambda$ be a primitive embedding into an even unimodular lattice, and put $T\definedas S^{\perp\Lambda}$.
The gluing construction of @cons:embedding-gluing-data gives an anti-isometry
$$
A_{T,q}\isoto -A_{S,q}.
$$
Applying @thm:milgram gives
$$
\sign(S)+\sign(T)\equiv0\pmod8.
$$
:::

## Finiteness of orbits of vectors of fixed norm

::: {.theorem #thm:finiteness-fixed-norm-orbits title="Finitely many orbits in each norm"}

Let $L$ be an integral lattice and $n\in\ZZ$.
The norm shell $L[n]$ of @def:lattice-basic-invariants decomposes into finitely many $\Orth(L)$-orbits.
:::

::: {.proof}
For definite $L$, the shell $L[n]$ is finite. For indefinite $L$, finiteness of the $\Orth(L)$-orbit set of integral vectors of fixed norm is the classical finiteness theorem for representations by an indefinite integral quadratic form.
If $\operatorname{PrimEmb}(U^{\oplus2},L)$ contains an embedding whose image is an orthogonal direct summand, @thm:eichler-criterion makes the orbit classification effective: for fixed norm, a $\widetilde\Orth^+(L)$-orbit is determined by $v^*\in A_L$, so there are at most $\abs{L^\#/L}$ such orbits.
:::
