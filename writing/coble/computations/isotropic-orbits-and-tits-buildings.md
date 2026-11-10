---
title: Orbits of isotropic vectors and the Tits building of a cusp configuration
unit: method
status: reusable
tags:
  - isotropic-orbits
  - cusps
  - baily-borel
  - tits-buildings
  - method
notes: |-
  Provenance: the Dawes-2022 orbit-algorithm research notes for the algorithms and examples of [@Daw22], and the Enriques-moduli computation notes for those of [@SH23].
---

# Orbits of isotropic vectors and the Tits building of a cusp configuration {#sec-isotropic-orbits-and-tits-buildings}

## The Tits building of a lattice of signature $(2,n)$

::: {.lemma #lem:signature-two-isotropic-dimension title="Totally isotropic subspaces in signature $(2,n)$"}

Let $T$ be a nondegenerate lattice of signature $(2,n)$.
Every totally isotropic subspace of $T\tensor\RR$ has dimension at most $2$.
:::

::: {.proof}

Write $T\tensor\RR = P\perp N$ with $P$ positive definite of dimension $2$ and $N$ negative definite of dimension $n$.
A totally isotropic subspace $W$ meets $N$ only in $0$, because every nonzero vector of $N$ has negative square.
Hence $\dim W\leq\dim(T\tensor\RR)-\dim N = 2$.
:::

::: {.definition #def:signature-two-tits-building title="The Tits building of a lattice of signature $(2,n)$"}

Let $T$ be a nondegenerate lattice of signature $(2,n)$.
The **Tits building** of $T$ is the bipartite graph whose vertices are the primitive isotropic lines and the primitive totally isotropic planes of $T$, with an edge from a line $I$ to a plane $J$ when $I\subset J$.
A subgroup $\Gamma\leq\Orth(T)$ acts on it by graph automorphisms.
By @lem:signature-two-isotropic-dimension these are all the nonzero primitive totally isotropic sublattices of $T$.
:::

## Deciding orbit equivalence of two vectors

::: {.proposition #prop:orbit-necessary-conditions title="Conditions necessary for equivalence"}

Let $L$ be a nondegenerate lattice, $\Gamma\leq\Orth(L)$, and $v_1, v_2\in L$ primitive with $\phi(v_1) = v_2$ for some $\phi\in\Gamma$.
Then

1. $v_1^2 = v_2^2$;

2. $\div_L(v_1) = \div_L(v_2)$, and the isometry induced by $\phi$ on $A_L$ carries $[v_1^*]$ to $[v_2^*]$;

3. $\phi$ restricts to an isometry $v_1^{\perp L}\to v_2^{\perp L}$, so the two complements are isometric and in particular have equal discriminants.
:::

::: {.proof}

All three are invariance under an isometry, and none needs $v_i$ isotropic.

(1) $\phi$ preserves the form, so $v_2^2=\phi(v_1)^2=v_1^2$.

(2) $\phi$ induces an isomorphism of the dual lattices, so $\beta_{L}(\phi v_1,\phi x)=\beta_L(v_1,x)$ shows that the divisibility ideals of @def:lattice-divisibility agree, hence $\div_L(v_1)=\div_L(v_2)$ as positive generators of the same ideal.
For the classes: $\phi$ carries $v_1/\div_L(v_1)$ to $v_2/\div_L(v_2)$ because it is linear and preserves the divisibility, and it passes to the quotient $A_L=L^\#/L$ because it maps $L$ to $L$; so the induced automorphism of $A_L$ sends $[v_1^*]$ to $[v_2^*]$ by @def:lattice-discriminant-class.

(3) $\phi(v_1)=v_2$ gives $\phi(v_1^{\perp L})=v_2^{\perp L}$: if $x\perp v_1$ then $\beta(\phi x,v_2)=\beta(x,v_1)=0$, and conversely by applying $\phi^{-1}$.
The restriction is an isometry onto, hence an isometry of lattices, so the complements are isometric and by @def:discriminant they have the same discriminant form.
:::

::: {.lemma #lem:complement-determinant title="The determinant of a complement is fixed by the square and the divisibility"}

Let $L$ be a nondegenerate integral lattice and $v\in L$ primitive with $q(v)\neq0$.
Then
$$
\abs{\det\bigl(v^{\perp L}\bigr)}
=
\abs{\det L}\cdot\frac{\abs{q(v)}}{\div_L(v)^{2}}
.
$$
:::

::: {.proof}

The map $\varphi\colon L\to\ZZ$, $x\mapsto\beta(x,v)$, has image $\div_L(v)\ZZ$ and kernel $v^{\perp L}$, and it carries $\ZZ v$ onto $q(v)\ZZ$; so
$$
L\big/\bigl(\ZZ v+v^{\perp L}\bigr) \;\iso\; \div_L(v)\ZZ\big/ q(v)\ZZ
,\qquad
\bigl[L:\ZZ v+v^{\perp L}\bigr] = \frac{\abs{q(v)}}{\div_L(v)}
,$$
the quotient on the right being finite of that order because $q(v)\in\div_L(v)\ZZ$.
On the other hand $\det(\ZZ v\oplus v^{\perp L}) = q(v)\cdot\det(v^{\perp L})$ and $\det(\ZZ v\oplus v^{\perp L}) = [L:\ZZ v+v^{\perp L}]^{2}\cdot\det L$; substituting the index gives the formula.
:::

::: {.proposition #prop:dawes-orbit-decision title="Deciding equivalence of non-isotropic vectors"}

Let $L$ be an even nondegenerate lattice, let $\Gamma\leq\Orth(L)$, and let $v_1, v_2\in L\tensor\QQ$ with $v_1$ non-isotropic.
Whether $g(v_1) = v_2$ for some $g\in\Gamma$ is decidable in each of the following cases:

1. $v_1^{\perp}$ is definite [@Daw22, Alg. 2.1];

2. $v_1^{\perp}$ is indefinite, $\Gamma$ is the preimage in $\Orth(L)$ of a subgroup $\mathcal A\leq\Orth(q_L)$, and $\Orth(L)\too\Orth(q_L)$ is surjective [@Daw22, Alg. 2.2, Alg. 2.3].
:::

::: {.corollary #cor:dawes-orbit-decision-two-elementary title="The surjectivity hypothesis for $2$-elementary lattices"}

Let $L$ be an even indefinite nondegenerate $2$-elementary lattice.
Then $\Orth(L)\too\Orth(q_L)$ is surjective, so case 2 of @prop:dawes-orbit-decision applies to every non-isotropic $v_1\in L\tensor\QQ$ with $v_1^\perp$ indefinite.
In particular it applies to $L = T_\Co$.
:::

::: {.proof}

The surjectivity is @thm:two-elementary-surjectivity.
:::

::: {.example #ex:dawes-u-a3 title="Two specimens in $U\oplus A_3$"}

Both specimens are stated in $L = U\oplus A_3$ with the Gram matrices
$$
G_U = \begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
G_{A_3} = \begin{pmatrix}-2&-1&0\\-1&-2&-1\\0&-1&-2\end{pmatrix},
$$
the coordinates below being taken in that basis.

For Example 2.2 of [@Daw22], $v_1 = (4,4,1,2,-1)$ and $v_2 = (36,144,5,-30,83)$, and both have $v^2 = 20$: the $U$-part contributes $32$ and $10368$, the $A_3$-part $-12$ and $-10348$.
The paper's conclusion is $v_1\sim v_2$ under the group it denotes $\wh{\Orth}^+(L)$.

For Example 2.6, $v_1 = (1,-1,0,0,0)$ and $v_2 = (1,0,1,0,0)$, and both have $v^2 = -2$.
The paper's conclusion is $v_1\sim v_2$ under the group it denotes $\wh{S\Orth}^+(L)$.
:::

::: {.proposition #prop:dawes-example-22 title="The two vectors of Example 2.2 are equivalent"}

Let $L$, $v_1$ and $v_2$ be as in Example 2.2 of @ex:dawes-u-a3, and let $\wh{\Orth}^+(L)$ be the subgroup of $\Orth(L)$ of the isometries that act trivially on $A_L$ and preserve each component of $\set{x\in L\tensor\RR : x^2>0}$.
Then $g(v_1) = v_2$ for some $g\in\wh{\Orth}^+(L)$.
:::

::: {.proof}

*The complements.*
Both vectors are primitive, with $v^2 = 20$ and $\div_L(v) = 4$, so by @lem:complement-determinant both complements $N_i = v_i^{\perp L}$ have determinant $4\cdot 20/4^{2} = 5$.
In $\ZZ$-bases of $N_1$ and $N_2$ their Gram matrices are
$$
G_1 = \begin{pmatrix} -2&-1&1&-1\\ -1&-2&1&-1\\ 1&1&-2&1\\ -1&-1&1&-2\end{pmatrix},
\qquad
G_2 = \begin{pmatrix} -182&-192&-445&-590\\ -192&-206&-476&-631\\ -445&-476&-1102&-1459\\ -590&-631&-1459&-1934\end{pmatrix}.
$$
Each is negative definite with $20$ roots of type $A_4$, and a rank-$4$ lattice whose roots are of type $A_4$ and whose determinant equals $\det A_4 = 5$ is the root lattice $A_4$; so $N_1\iso N_2\iso -A_4$.
The discriminant group $A_{N_i}$ is $\ZZ/5$, and for a generator $m_i$ the form $q_{N_i}$ takes the value $6/5$ on $\pm m_i$ and $4/5$ on $\pm 2m_i$.

*An isometry of $L$ carrying $v_1$ to $v_2$.*
Since $|A_{\generators{v_i}}|\cdot|A_{N_i}| = 20\cdot 5 = 5^2\cdot|A_L|$, the lattice $L$ is an overlattice of index $5$ of $\generators{v_i}\oplus N_i$, and it corresponds to an isotropic subgroup $\Lambda_i\leq A_{\generators{v_i}}\oplus A_{N_i}\iso\ZZ/20\oplus\ZZ/5$ of order $5$.
Since $\generators{v_i} = L\intersect\QQ v_i$ and $N_i = L\intersect(N_i\tensor\QQ)$, the subgroup $\Lambda_i$ meets neither summand, so it is the graph of an isomorphism from the subgroup generated by the class of $v_i/5$ onto $A_{N_i}$: $\Lambda_i = \set{(j\,v_i/5,\ j c_i m_i)}$ for some $c_i\in(\ZZ/5)^\times$.
Isotropy at $j = 1$ requires $q(v_i/5) + q_{N_i}(c_i m_i) = 4/5 + q_{N_i}(c_i m_i)\in 2\ZZ$, so $q_{N_i}(c_im_i) = 6/5$ and $c_i = \pm1$.
Choose an isometry $h\colon N_1\to N_2$; composing it with $-1$ if necessary, its action on discriminant groups carries $c_1m_1$ to $c_2m_2$.
Then $v_1\mapsto v_2$ together with $h$ is an isometry $\generators{v_1}\oplus N_1\to\generators{v_2}\oplus N_2$ carrying $\Lambda_1$ to $\Lambda_2$, so it extends to an isometry $g$ of the overlattice $L$ with $g(v_1) = v_2$.

*The isometry lies in $\wh{\Orth}^+(L)$.*
The group $A_L\iso A_{A_3}\iso\ZZ/4$ has $q$ equal to $5/4$ on its two generators and $1$ on its element of order $2$.
The class of $v_1/4$ has $q = 20/16 = 5/4$, so it generates $A_L$.
Since $v_2 - v_1 = 4\,(8,35,1,-8,21)\in 4L$, the classes of $v_1/4$ and $v_2/4$ in $A_L$ are equal, so $g$ fixes a generator of $A_L$ and acts trivially on $A_L$.
Since $(v_1, v_2) = 820 > 0$, the vectors $v_1$ and $v_2$ of positive square lie in the same component of $\set{x^2>0}$, and $g$ preserves each component.
So $g\in\wh{\Orth}^+(L)$.
:::

::: {.proposition #prop:dawes-building-descent title="Computing quotients of the Tits building"}

Let $T$ be an even nondegenerate lattice of signature $(2,n)$, and for a subgroup $G\leq\Orth^+(T\tensor\QQ)$ let $G\backslash\mathcal B(T)$ be the quotient by $G$ of the Tits building of @def:signature-two-tits-building.

1. If $G_1\leq G_2\leq\Orth^+(T\tensor\QQ)$ with $[G_2:G_1]<\infty$, then $G_1\backslash\mathcal B(T)$ is computable from $G_2\backslash\mathcal B(T)$ and a transversal of $G_2/G_1$ [@Daw22, Alg. 3.1].

2. If $T$ is maximal and $T\iso U\oplus U\oplus T_0$ for a lattice $T_0$, and $n\geq2$, then $\Orth^+(T)\backslash\mathcal B(T)$ is computable [@Daw22, Alg. 3.2].
:::

## The polarized Enriques computation

::: {.theorem #thm:sh23-enriques-moduli-groups title="The arithmetic groups of polarized Enriques moduli"}

Let $\ten = U\oplus U(2)\oplus E_8(2)$, of signature $(2,10)$.
For a polarization $h$ of an Enriques surface, let $\Gamma_h^+\leq\Orth^+(\ten)$ be the arithmetic group with $\mathcal M_{\En,h} = \Gamma_h^+\backslash\mathcal D_{\ten}$ [@SH23, §2].

1. The groups $\Gamma_h^+$ fall into exactly $87$ conjugacy classes [@SH23, Thm. 3.5].

2. Every moduli space $\mathcal M_{\En,h}$ is dominated by a moduli space of polarized Enriques surfaces of degree $1240$ [@SH23, §3.4].

3. The $0$- and $1$-dimensional cusps of $\mathcal M_{\En,h}$ are the $\Gamma_h^+$-orbits of primitive isotropic lines and planes of $\ten$, and $\Gamma_h^+\backslash\mathcal B(\ten)$ is computed for every $h$ [@SH23, §3.6, Tables 1 and 2].
:::

