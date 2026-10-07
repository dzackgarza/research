# Clifford lifting and spinor obstructions {#sec-clifford-lifting}

The spinor norm records an obstruction to lifting an isometry to a norm-one Clifford element. A square class is one description of that obstruction under additional hypotheses. Over a ring, the distinction matters twice: the obstruction can involve a nontrivial line module, and a nonperfect form can fail to admit the local lifts needed for a torsor description.

## Quadratic modules and Clifford lifts

Let $R$ be a commutative ring, let $M$ be a finitely generated projective $R$-module, and let $q\colon M\to R$ be a quadratic form. Write
$$
b_q(x,y)=q(x+y)-q(x)-q(y),\qquad
b_q^\sharp\colon M\longrightarrow M^\vee.
$$
We distinguish injectivity of $b_q^\sharp$ from its being an isomorphism. We call the latter condition **perfectness of the polar form**. For a free module of finite rank, it says that the polar Gram determinant is a unit. A nonzero Gram determinant over an integral domain need not be a unit.

Hahn–O'Meara call the quadratic module *nonsingular* when its associated bilinear form is nonsingular; their bilinear definition requires an isomorphism to the dual. This is the hypothesis in their ring-valued spinor-norm construction, together with freeness of finite rank. [Hahn–O'Meara, §5.1A, Proposition 5.1.5, §5.1D, and §7.2C, pp. 418–419](https://doi.org/10.1007/978-3-662-13152-7).

The Clifford algebra is
$$
C(M,q)=T_R(M)/(v\otimes v-q(v)1\mid v\in M).
$$
It has a parity involution $c\mapsto c'$ and a Clifford conjugation $c\mapsto\bar c$, the anti-involution with $\bar v=-v$ for $v\in M$. Our norm convention is $N(c)=c\bar c$. A homogeneous unit $c$ acts by the twisted adjoint formula
$$
v\longmapsto c v(c')^{-1}.
$$
A **norm-one Clifford lift** of an isometry is such a unit, preserving $M$ under this action, with $N(c)=1$. Homogeneity is understood locally on the base. Even lifts give the spin group. The conjugation convention fixes the sign in the reflection formula below.

## The lifting obstruction before its target is simplified

The following construction applies to sheaves of groups on the fppf site of $S=\operatorname{Spec}R$. Here *fppf locally* means after a faithfully flat cover locally of finite presentation. A torsor under a group sheaf $K$ is a sheaf with a $K$-action which is locally isomorphic to $K$ acting on itself. Its class lies in the pointed set $H^1_{\mathrm{fppf}}(S,K)$; the distinguished class is the trivial torsor.

::: {.proposition #prop:clifford-lift-obstruction title="Local existence and global lifting"}

Let $p\colon G\to H$ be a homomorphism of fppf sheaves of groups. Put $K=\ker p$ and let $I\subseteq H$ be its sheaf image. Then
$$
1\longrightarrow K\longrightarrow G\longrightarrow I\longrightarrow1
$$
is exact. For $g\in I(S)$, the fiber $P_g=p^{-1}(g)$ is a right $K$-torsor. There is an exact sequence of pointed sets
$$
1\longrightarrow K(S)\longrightarrow G(S)\longrightarrow I(S)
\xrightarrow{\delta}H^1_{\mathrm{fppf}}(S,K),\qquad
\delta(g)=[P_g].
$$
Thus $g$ lifts globally if and only if $\delta(g)$ is trivial. Membership in $I(S)$ is the preceding, separate condition that $g$ lifts locally. If $K$ is central in $G$, then $\delta$ is a homomorphism to the abelian group $H^1_{\mathrm{fppf}}(S,K)$.
:::

::: {.proof}

Assume the stated sheaf data. We prove the assertions by describing the fibers.

1. **Local trivialization.** Membership in the sheaf image means that a cover admits lifts $u_i$ of $g$. On each member of this cover, $k\mapsto u_i k$ identifies $K$ with $P_g$: two lifts differ by a unique element of $\ker p$.
2. **Exactness.** The fiber has a global section precisely when $g\in p(G(S))$. A torsor has a global section precisely when it is trivial. This proves exactness at $I(S)$; the preceding terms follow from $K=\ker p$.
3. **Central case.** For local lifts $u_i$ of $g$ and $v_i$ of $h$, write $u_j=u_i k_{ij}$ and $v_j=v_i\ell_{ij}$. Centrality gives $u_jv_j=u_iv_i k_{ij}\ell_{ij}$. The cocycle of the product is therefore the product of the cocycles.
4. **Conclusion.** Steps 1–2 give the torsor and its vanishing criterion. Step 3 gives the homomorphism assertion.
:::

For Clifford lifting, take $G$ to be the sheaf of norm-one homogeneous Clifford units and $H=O(q)$. This formulation still makes sense without perfectness of $b_q$. It does **not** assert that $I=O(q)$ or that $K=\mu_2$. Those are mathematical assertions about the chosen integral Clifford construction, not consequences of the word “spinor.”

## Discriminant modules and the classical exact sequence

A **discriminant module** over $R$ is a pair $(P,f)$ consisting of an invertible $R$-module and an isomorphism $f\colon P^{\otimes2}\simeq R$. Tensor product defines the group $\operatorname{Disc}(R)$ of their isomorphism classes. There are canonical identifications and an exact sequence
$$
\operatorname{Disc}(R)\simeq H^1_{\mathrm{fppf}}(R,\mu_2),\qquad
1\longrightarrow R^\times/(R^\times)^2
\longrightarrow\operatorname{Disc}(R)
\longrightarrow\operatorname{Pic}(R)[2]\longrightarrow1.
$$
The last map forgets $f$. The first sends $[a]$ to the trivial line with pairing $f(1,1)=a$. These statements hold even when $2$ is not invertible; this is why the fppf topology is used. [Stacks Project, §59.28, Lemmas 59.28.3 and 59.28.5](https://stacks.math.columbia.edu/tag/03PK).

For $g\in O(M,q)$, define the graded intertwiner module by
$$
(L_g)_i=\{d\in C_i(M,q):g(x)d=(-1)^i d x\text{ for every }x\in M\},
\qquad L_g=(L_g)_0\oplus(L_g)_1.
$$
Under the hypotheses of Hahn–O'Meara's §7.2C, $L_g$ is invertible. Clifford conjugation gives a perfect pairing
$$
f_g\colon L_g^{\otimes2}\longrightarrow R,\qquad
d\otimes e\longmapsto d\bar e.
$$
Their spinor norm is
$$
\theta_R(g)=[L_g,f_g]\in\operatorname{Disc}(R).
$$
Multiplication of intertwiner lines proves that this is a homomorphism. Its torsor consists of local generators $u$ with $u\bar u=1$. Thus the discriminant module and the norm-one lifting torsor describe the same obstruction. A generator of norm $a\in R^\times$ acquires norm one after adjoining a square root of $a$ and rescaling. [Hahn–O'Meara, §7.2C, pp. 418–421](https://doi.org/10.1007/978-3-662-13152-7).

Write $O_{\mathrm{rot}}(M)$ for the kernel of their Clifford residue, the locally constant parity of the intertwiner line. Their notation for this group is $O^+(M)$. Restricting to even lifts gives
$$
1\longrightarrow\mu_2(R)\longrightarrow\operatorname{Spin}(M)
\longrightarrow O_{\mathrm{rot}}(M)
\xrightarrow{\theta_R}\operatorname{Disc}(R).
$$
Exactness identifies the image of $\operatorname{Spin}(M)$ with the spinor kernel **inside the rotation group**. No surjectivity onto $\operatorname{Disc}(R)$ is asserted. Under these same hypotheses, $O_{\mathrm{rot}}(M)=SO(M)$ when $2$ is not a zero divisor. [Hahn–O'Meara, Theorems 7.2.19 and 7.2.21](https://doi.org/10.1007/978-3-662-13152-7).

## Square classes and change of base

If $\operatorname{Pic}(R)[2]=0$, the displayed exact sequence identifies $\operatorname{Disc}(R)$ with unit square classes. This holds for $R=\mathbb Z$ and for fields. It removes the line-module obstruction; it does not establish the hypotheses needed to construct $L_g$ for a given form.

Over a field $F$ of characteristic different from $2$, let $q$ have nondegenerate polar form. For an anisotropic vector $v$, the vector $v\in C(V,q)^\times$ lifts the reflection $s_v$. Consequently
$$
\theta_F(s_v)=[v\bar v]=[-q(v)],\qquad
\theta_F(s_{v_1}\cdots s_{v_r})=
\left[\prod_{i=1}^r(-q(v_i))\right].
$$
These are descriptions of the preceding obstruction, not an independent choice of its meaning. [Hahn–O'Meara, §7.2C, Example 1, p. 421](https://doi.org/10.1007/978-3-662-13152-7).

Base change sends $(L_g,f_g)$ to $(L_g\otimes_R A,f_g\otimes_R A)$. Whenever the integral construction applies, it follows that
$$
\theta_A(g_A)=\operatorname{Disc}(R\to A)(\theta_R(g)).
$$
For a domain $R$ with fraction field $F$, a generically nondegenerate form therefore always has the *generic* obstruction $\theta_F(g_F)$. Its vanishing means a norm-one lift over $F$, not necessarily over $R$.

The further map $\mathbb Q^\times/(\mathbb Q^\times)^2\to\mathbb R^\times/(\mathbb R^\times)^2$ retains only the sign. Its kernel contains every positive rational square class. Thus rational and real spinor kernels need not agree. For signature $(2,n)$, the real character with the reflection normalization above detects preservation of a connected component of the type-IV domain; this is the $O^+(L)$ used in that setting. [Dawes, *Orbits in lattices*, §§1.3–1.4](https://arxiv.org/html/2205.10601).

## Nonperfect forms: what changes

General Clifford groups do extend beyond perfect forms. Zemel constructs a map from the Clifford group to isometries fixing the radical pointwise, with kernel the units of the twisted center. Proposition 3.7 places Clifford norms in this kernel, which can exceed the scalar units. His Theorem 3.8 proves surjectivity under generation by generalized reflections and Euler transformations, together with an orthogonal-basis hypothesis after an injective ring extension and non-zero-divisor conditions. These hypotheses must be checked; the theorem is not a surjectivity statement for all integral lattices. [Zemel, *Clifford Groups of Arbitrary Quadratic Modules over Commutative Rings*, Corollary 3.3, Proposition 3.7, Theorem 3.8, and Remark 3.18](https://arxiv.org/html/2112.05046).

For a specified norm-one Clifford map, @prop:clifford-lift-obstruction gives the corresponding exact sequence with its actual kernel sheaf $K$ and image sheaf $I$. Determining these sheaves is the substantive extension problem. A computation of their $R$-points alone does not determine their behavior after base change, especially at primes where the polar form degenerates.

::: {.example #ex:spinor-integral-extension title="A generic spinor class which does not extend over the integers"}

Let $M=\mathbb Z^2$ with $q(x,y)=x^2-2y^2$. Its polar Gram matrix is $\operatorname{diag}(2,-4)$. The isometry $g(x,y)=(x,-y)$ is the reflection in $v=(0,1)$ over $\mathbb Q$.

1. **Generic obstruction.** The reflection formula gives $\theta_{\mathbb Q}(g)=[-q(v)]=[2]$.
2. **Integral discriminant classes.** Since $\operatorname{Pic}(\mathbb Z)=0$, the image of $\operatorname{Disc}(\mathbb Z)$ in $\operatorname{Disc}(\mathbb Q)$ consists of $[1]$ and $[-1]$. Each has even $2$-adic valuation, whereas $[2]$ has odd valuation.
3. **Conclusion.** No element of $\operatorname{Disc}(\mathbb Z)$ specializes to this generic spinor obstruction. In particular, a $\operatorname{Disc}(\mathbb Z)$-valued invariant on all integral isometries, compatible with the stated generic spinor norm, cannot exist for this quadratic module.

After passage to $\mathbb Z[1/2]$, the polar form is perfect and $2$ is a unit. The class is then represented by the discriminant line with pairing $2$, or equivalently by the $\mu_2$-torsor $t^2=2$.
:::

Thus two distinct simplifications lead to the familiar target: the Clifford lifting problem must first have the required local existence and scalar kernel, and the resulting discriminant line must then be trivializable to obtain a unit square class. Keeping the lifting problem itself as the defining object separates these requirements and preserves the meaning of the kernel when the hypotheses change.
