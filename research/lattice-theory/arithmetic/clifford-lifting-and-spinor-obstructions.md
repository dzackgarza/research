# Clifford lifting and spinor obstructions {#sec-clifford-lifting}

## Quadratic modules and Clifford lifts

Let $R$ be a commutative ring, let $M$ be a finitely generated projective $R$-module, and let $q\colon M\to R$ be a quadratic form. Write
$$
b_q(x,y)=q(x+y)-q(x)-q(y),\qquad
b_q^\sharp\colon M\longrightarrow M^\vee.
$$
The polar form is *perfect* if $b_q^\sharp$ is an isomorphism. For a free module of finite rank, perfectness is equivalent to the polar Gram determinant being a unit. Over an integral domain, injectivity of $b_q^\sharp$ is equivalent to nondegeneracy over the fraction field.

Hahn–O'Meara call the quadratic module *nonsingular* when its associated bilinear form is nonsingular; their bilinear definition requires an isomorphism to the dual. This is the hypothesis in their ring-valued spinor-norm construction, together with freeness of finite rank [@HO89, §5.1A, Proposition 5.1.5, §5.1D, and §7.2C, pp. 418–419].

The Clifford algebra is
$$
C(M,q)=T_R(M)/(v\otimes v-q(v)1\mid v\in M).
$$
It has a parity involution $c\mapsto c'$ and a Clifford conjugation $c\mapsto\bar c$, the anti-involution with $\bar v=-v$ for $v\in M$. Put $N(c)=c\bar c$. A homogeneous unit $c$ acts by the twisted adjoint formula
$$
v\longmapsto c v(c')^{-1}.
$$
For an $R$-algebra $A$, put $M_A=M\otimes_R A$ and $C_A=C(M_A,q_A)$. Define the group functor
$$
G(A)=\{c\in C_A^\times:
c\text{ is locally homogeneous},\quad
cM_A(c')^{-1}=M_A,\ c\bar c=1\}.
$$
Locally homogeneous means homogeneous on an open cover of $\operatorname{Spec}A$, with the degree allowed to vary between components. The twisted adjoint action defines $p\colon G\to O(q)$. A *norm-one Clifford lift* of $g\in O(q)(A)$ is an element of $p^{-1}(g)(A)$. Define $\operatorname{Spin}(M,q)(A)=G(A)\cap C_{A,0}$. Both functors are fppf sheaves.

## Lifting torsors

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

For the Clifford map $p\colon G\to O(q)$, the sheaf $I$ consists of isometries with fppf-local norm-one lifts, and $K$ consists of norm-one units acting trivially on $M$. The obstruction of $g\in I(R)$ is the torsor $p^{-1}(g)$.

## Discriminant modules and the classical exact sequence

A *discriminant module* over $R$ is a pair $(P,f)$ consisting of an invertible $R$-module and an isomorphism $f\colon P^{\otimes2}\simeq R$. Tensor product defines the group $\operatorname{Disc}(R)$ of their isomorphism classes. There are canonical identifications and an exact sequence
$$
\operatorname{Disc}(R)\simeq H^1_{\mathrm{fppf}}(R,\mu_2),\qquad
1\longrightarrow R^\times/(R^\times)^2
\longrightarrow\operatorname{Disc}(R)
\longrightarrow\operatorname{Pic}(R)[2]\longrightarrow1.
$$
The last map forgets $f$. The first sends $[a]$ to the trivial line with pairing $f(1,1)=a$. The fppf Kummer sequence gives these statements for every commutative ring [@stacks-03PK, Lemmas 59.28.3 and 59.28.5].

For $g\in O(M,q)$, define the graded intertwiner module by
$$
(L_g)_i=\{d\in C_i(M,q):g(x)d=(-1)^i d x\text{ for every }x\in M\},
\qquad L_g=(L_g)_0\oplus(L_g)_1.
$$
Suppose $M$ is free of finite rank and $b_q$ is perfect. Then $L_g$ is invertible, and Clifford conjugation gives a perfect pairing
$$
f_g\colon L_g^{\otimes2}\longrightarrow R,\qquad
d\otimes e\longmapsto d\bar e.
$$
The *spinor norm* is the homomorphism $\theta_R\colon O(M,q)(R)\to\operatorname{Disc}(R)$ defined by
$$
\theta_R(g)=[L_g,f_g]\in\operatorname{Disc}(R).
$$
Multiplication of intertwiner lines proves that this is a homomorphism. Its torsor consists of local generators $u$ with $u\bar u=1$. A generator of norm $a\in R^\times$ acquires norm one after adjoining a square root of $a$ and rescaling [@HO89, §7.2C, pp. 418–421].

Write $O_{\mathrm{rot}}(M)$ for the kernel of their Clifford residue, the locally constant parity of the intertwiner line. Their notation for this group is $O^+(M)$. Restricting to even lifts gives
$$
1\longrightarrow\mu_2(R)\longrightarrow\operatorname{Spin}(M)
\longrightarrow O_{\mathrm{rot}}(M)
\xrightarrow{\theta_R}\operatorname{Disc}(R).
$$
Exactness gives $\operatorname{im}\operatorname{Spin}(M)=O_{\mathrm{rot}}(M)\cap\ker\theta_R$. For $M$ free of finite rank with perfect polar form, $O_{\mathrm{rot}}(M)=SO(M)$ when $2$ is not a zero divisor [@HO89, 7.2.19 and Theorem 7.2.21].

## Square classes and change of base

If $\operatorname{Pic}(R)[2]=0$, the Kummer exact sequence identifies $\operatorname{Disc}(R)$ with $R^\times/(R^\times)^2$. This holds for $R=\mathbb Z$ and for fields.

Let $(V,q)$ be a finite-dimensional quadratic space over a field $F$ of characteristic different from $2$, with nondegenerate polar form. For an anisotropic vector $v$, the vector $v\in C(V,q)^\times$ lifts the reflection $s_v(x)=x-b_q(x,v)v/q(v)$. Consequently
$$
\theta_F(s_v)=[v\bar v]=[-q(v)],\qquad
\theta_F(s_{v_1}\cdots s_{v_r})=
\left[\prod_{i=1}^r(-q(v_i))\right].
$$
The first identity is [@HO89, §7.2C, Example 1, p. 421]; the second follows from multiplicativity.

Base change sends $(L_g,f_g)$ to $(L_g\otimes_R A,f_g\otimes_R A)$. Whenever the integral construction applies, it follows that
$$
\theta_A(g_A)=\operatorname{Disc}(R\to A)(\theta_R(g)).
$$
For a domain $R$ with fraction field $F$, a generically nondegenerate form has the *generic* obstruction $\theta_F(g_F)$.

Assume $\operatorname{char}F\ne2$ and put $V=M\otimes_R F$. Let $\operatorname{Pin}(V)$ denote the norm-one homogeneous Clifford group defined by Clifford conjugation. Define $E_R^{\mathrm{gen}}$ by the Cartesian square of groups

```tikzcd
E_R^{\mathrm{gen}} \arrow[r] \arrow[d] \arrow[dr, phantom, "\lrcorner", very near start]
  & \operatorname{Pin}(V)(F) \arrow[d,"p"] \\
O(M,q)(R) \arrow[r,"g\mapsto g_F"]
  & O(V,q_F)(F).
```

Thus
$$
E_R^{\mathrm{gen}}
=O(M,q)(R)\mathbin{\times}_{O(V,q_F)(F)}\operatorname{Pin}(V)(F).
$$
There is an exact sequence
$$
1\longrightarrow\mu_2(F)\longrightarrow E_R^{\mathrm{gen}}
\longrightarrow O(M,q)(R)
\xrightarrow{\,g\mapsto\theta_F(g_F)\,}F^\times/(F^\times)^2.
$$
Indeed, projection from the pullback has the same kernel as the field Clifford map, and its image consists precisely of isometries admitting a norm-one Clifford lift over $F$.

## Algebraic spinor morphisms and their kernels

::: {.definition #def:integral-clifford-lifting-subgroup title="Integral Clifford lifting subgroup"}

For the norm-one Clifford map $p\colon G\to O(q)$ over an arbitrary ring, define the *integral lifting subgroup*
$$
K_{\mathrm{lift},R}(M)=\operatorname{im}\bigl(G(R)\xrightarrow{p}O(M,q)(R)\bigr).
$$
With $I$ and $K$ as in @prop:clifford-lift-obstruction, this is the inverse image of the trivial torsor under the pointed-set map $\delta\colon I(R)\to H^1_{\mathrm{fppf}}(R,K)$. Its domain consists of the isometries admitting fppf-local lifts.
:::

::: {.definition #def:algebraic-spinor-kernels title="Full algebraic spinor kernel"}

For $M$ free of finite rank with perfect polar form, the *full algebraic spinor kernel* is
$$
K_R(M)=\ker\bigl(\theta_R\colon O(M,q)(R)\to\operatorname{Disc}(R)\bigr).
$$
:::

::: {.definition #def:even-algebraic-spinor-kernel title="Even algebraic spinor kernel"}

For $M$ free of finite rank with perfect polar form, the *even algebraic spinor kernel* is
$$
K_R^{\mathrm{ev}}(M)=K_R(M)\cap O_{\mathrm{rot}}(M).
$$
:::

The lifting interpretation gives
$$
K_R(M)=K_{\mathrm{lift},R}(M),\qquad
K_R^{\mathrm{ev}}(M)=\operatorname{im}\bigl(\operatorname{Spin}(M)(R)\to O(M,q)(R)\bigr).
$$
Thus the image of $\operatorname{Spin}$ is the residue-zero subgroup of the full spinor kernel.

::: {.definition #def:generic-spinor-kernel title="Generic spinor kernel"}

For a domain $R$ with fraction field $F$ of characteristic different from $2$, assume only that $q_F$ is nondegenerate. Define
$$
\theta_F^M\colon O(M,q)(R)\to F^\times/(F^\times)^2,\quad
g\mapsto\theta_F(g_F),\qquad
K_F(M)=\ker\theta_F^M.
$$
Then $K_F(M)$ is the image of $E_R^{\mathrm{gen}}$, and base change of lifts gives
$K_{\mathrm{lift},R}(M)\subseteq K_F(M)$.
:::

Over a field of characteristic different from $2$, reversion, the anti-involution fixing $V$, gives the alternative reflection value $[q(v)]$. Denote that character by $\theta_F^{\mathrm{rev}}$. If $\epsilon(g)\in\{0,1\}$ satisfies $\det(g)=(-1)^{\epsilon(g)}$, then
$$
\theta_F(g)=[-1]^{\epsilon(g)}\theta_F^{\mathrm{rev}}(g).
$$
Indeed, a product of $r$ reflections has determinant $(-1)^r$, and each reflection contributes one factor $[-1]$ to the ratio. The two characters agree on $SO(V)$, and on all of $O(V)$ if $-1$ is a square in $F$.

::: {.proposition #prop:spinor-kernel-base-change title="Exact comparison of kernels"}

Let $M$ be free of finite rank over $R$ with perfect polar form, and let $R\to A$ be a ring homomorphism. Write $j(g)=g_A$ and $c=\operatorname{Disc}(R\to A)$. Then $\theta_A\circ j=c\circ\theta_R$, and
$$
1\longrightarrow K_R(M)
\longrightarrow j^{-1}\bigl(K_A(M_A)\bigr)
\xrightarrow{\theta_R}
\operatorname{im}(\theta_R)\cap\ker(c)
\longrightarrow1
$$
is exact. In particular, the two kernels agree precisely when
$\operatorname{im}(\theta_R)\cap\ker(c)=\{1\}$.
:::

::: {.proof}

Assume the stated base change. We prove the exact sequence.

1. **Image.** The identity $\theta_A(j(g))=c(\theta_R(g))$ says that $j(g)\in K_A(M_A)$ exactly when $\theta_R(g)\in\ker c$. Thus the indicated restriction of $\theta_R$ maps onto $\operatorname{im}(\theta_R)\cap\ker c$.
2. **Kernel.** The kernel of that restriction is $\ker\theta_R=K_R(M)$.
3. **Conclusion.** Steps 1–2 give exactness and the equality criterion.
:::

For a nondegenerate integral lattice $L$, set
$$
\theta_{\mathbb Q}^L(g)=\theta_{\mathbb Q}(g_{\mathbb Q}),\qquad
\chi_{\mathrm{sp}}(g)=\operatorname{sgn}\bigl(\theta_{\mathbb Q}^L(g)\bigr),
\qquad K_{\mathbb R}(L)=\ker\chi_{\mathrm{sp}}.
$$
Here $\operatorname{sgn}\colon\mathbb Q^\times/(\mathbb Q^\times)^2\to\{+1,-1\}$ is induced by the real embedding; it identifies the real spinor norm with a sign. If $L$ is specified by a bilinear form $b$, use $q=b/2$ over $\mathbb Q$. This $q$ is integer-valued precisely when $L$ is even. The exact comparison is
$$
1\longrightarrow K_{\mathbb Q}(L)
\longrightarrow K_{\mathbb R}(L)
\xrightarrow{\theta_{\mathbb Q}^L}
\operatorname{im}(\theta_{\mathbb Q}^L)\cap
\bigl(\mathbb Q_{>0}^\times/(\mathbb Q^\times)^2\bigr)
\longrightarrow1.
$$
The proof is the image-and-kernel argument of @prop:spinor-kernel-base-change. Equality holds exactly when no nontrivial positive square class occurs in the rational spinor image.

If $L$ is even and its polar form is unimodular, the integral construction applies. Both maps
$$
\operatorname{Disc}(\mathbb Z)=\{[1],[-1]\}
\longrightarrow\operatorname{Disc}(\mathbb Q)
\longrightarrow\operatorname{Disc}(\mathbb R)=\{+1,-1\}
$$
are injective on the image of $\operatorname{Disc}(\mathbb Z)$. Therefore
$$
K_{\mathbb Z}(L)=K_{\mathbb Q}(L)=K_{\mathbb R}(L),
\qquad
\operatorname{im}\operatorname{Spin}(L)(\mathbb Z)
=SO(L)\cap K_{\mathbb R}(L).
$$
For a nonunimodular lattice, the rational-to-real equality criterion still applies. The integral lifting subgroup is @def:integral-clifford-lifting-subgroup.

## The moduli character and its algebraic identification

::: {.definition #def:period-component-character title="Period-component character"}

Let $L$ have signature $(2,n)$, with $n\geq1$, and let $b$ be its bilinear form. Its type-IV period domain is
$$
\Omega_L=\{[\omega]\in\mathbb P(L\otimes\mathbb C):
b(\omega,\omega)=0,\ b(\omega,\bar\omega)>0\}.
$$
The map $[\omega]\mapsto\langle\operatorname{Re}\omega,\operatorname{Im}\omega\rangle$, with this ordered orientation, identifies it with the space of oriented positive-definite real two-planes. It has two connected components. The action on them defines
$\chi_{\mathrm{per}}\colon O(L)\to\{+1,-1\}$, where $+1$ means that each component is preserved. Define
$$
O_{\mathrm{mod}}^+(L)=\ker\chi_{\mathrm{per}}
=\operatorname{Stab}_{O(L)}(\Omega_L^+)
$$
for either component $\Omega_L^+$.
:::

::: {.proposition #prop:period-spinor-character title="The period character is the real spinor character"}

With the conjugation normalization $\theta(s_v)=[-q(v)]$,
$$
\chi_{\mathrm{per}}=\chi_{\mathrm{sp}}
=\operatorname{sgn}\circ\theta_{\mathbb Q}^L,\qquad
O_{\mathrm{mod}}^+(L)=K_{\mathbb R}(L).
$$
In particular,
$$
O_{\mathrm{mod}}^+(L)=K_{\mathbb Q}(L)
\quad\Longleftrightarrow\quad
\operatorname{im}(\theta_{\mathbb Q}^L)\cap
\bigl(\mathbb Q_{>0}^\times/(\mathbb Q^\times)^2\bigr)=\{[1]\}.
$$
For the reflection normalization and component interpretation, see [@Daw22, §§1.3–1.4].
:::

::: {.proof}

Assume signature $(2,n)$. We compare the two real characters before restricting to $O(L)$.

1. **Negative reflection vector.** If $q(v)<0$, then $v^\perp$ contains a positive two-plane. The reflection fixes that plane pointwise and hence fixes its oriented point in $\Omega_L$. It preserves both components, so its component character is $+1=\operatorname{sgn}(-q(v))$.
2. **Positive reflection vector.** If $q(v)>0$, choose a positive vector $w\in v^\perp$. On the positive plane $\langle v,w\rangle$, the reflection reverses orientation. The two orientations lie in opposite components, so its component character is $-1=\operatorname{sgn}(-q(v))$.
3. **Conclusion.** Real orthogonal transformations are products of anisotropic reflections by Cartan–Dieudonné. Steps 1–2 identify the characters on generators; restriction to $O(L)$ and base change identify the asserted maps and kernels.
:::

For signature $(1,n)$ the analogous geometric character is the action on the two components of $\{x:b(x,x)>0\}$. The same reflection argument identifies it with $\chi_{\mathrm{sp}}$. The geometric spaces are the positive-cone components in signature $(1,n)$ and the oriented-positive-two-plane components in signature $(2,n)$.

For an even unimodular lattice $L$ of signature $(2,n)$,
$$
O_{\mathrm{rot}}(L)=SO(L)=\ker\det,\qquad
O_{\mathrm{mod}}^+(L)=\ker\chi_{\mathrm{sp}}.
$$
On a subgroup $\Gamma\subseteq O(L)$ their intersections agree exactly when
$\det|_\Gamma=\chi_{\mathrm{sp}}|_\Gamma$: two sign characters with the same kernel are equal. Their common intersection without this hypothesis is
$\ker(\det,\chi_{\mathrm{sp}})$.

::: {.example #ex:rotation-versus-period title="Distinct determinant and spinor kernels"}

Take $L=U\oplus U$, where $U=\mathbb Ze\oplus\mathbb Zf$ has $q(ae+bf)=ab$. Extend each isometry of the first summand by the identity on the second. Put $r=s_{e-f}$ and $s=s_{e+f}$. The reflection formulas give
$$
r(e)=f,\quad r(f)=e,\qquad
s(e)=-f,\quad s(f)=-e.
$$
Hence $\det r=-1$ and $\theta_{\mathbb Z}(r)=[1]$, so $r\in O_{\mathrm{mod}}^+(L)\setminus SO(L)$. Conversely, $\det(rs)=+1$ and $\theta_{\mathbb Z}(rs)=[-1]$, so $rs\in SO(L)\setminus O_{\mathrm{mod}}^+(L)$. The integral, rational, and real spinor kernels coincide here, but neither inclusion between the rotation and moduli groups holds.
:::

## Discriminant kernels and monodromy

For an even integral lattice $L$ of signature $(2,n)$, define
$$
L^\vee=\{x\in L_{\mathbb Q}:b(x,L)\subseteq\mathbb Z\},
\qquad A_L=L^\vee/L,\qquad
q_{A_L}([x])=q(x)\bmod\mathbb Z.
$$
The induced action is $\rho_L\colon O(L)\to O(A_L,q_{A_L})$. Define
$$
\widetilde O(L)=\ker\rho_L,\qquad
\widetilde O_{\mathrm{mod}}^+(L)
=\ker(\rho_L,\chi_{\mathrm{per}})
=\widetilde O(L)\cap K_{\mathbb R}(L).
$$
The notation $\widetilde O^+(L)$ denotes $\widetilde O_{\mathrm{mod}}^+(L)$ in [@Daw22, §§1.2–1.4], with discriminant form normalized as $b(x,x)\bmod2\mathbb Z$.

There is also a stable rational spinor kernel $\widetilde K_{\mathbb Q}(L)=\ker\rho_L\cap K_{\mathbb Q}(L)$. Their precise comparison is
$$
1\longrightarrow\widetilde K_{\mathbb Q}(L)
\longrightarrow\widetilde O_{\mathrm{mod}}^+(L)
\xrightarrow{\theta_{\mathbb Q}^L}
\theta_{\mathbb Q}^L(\ker\rho_L)\cap
\bigl(\mathbb Q_{>0}^\times/(\mathbb Q^\times)^2\bigr)
\longrightarrow1.
$$
If $L$ is even unimodular, $A_L=0$, and
$$
\widetilde K_{\mathbb Q}(L)=\widetilde O_{\mathrm{mod}}^+(L)
=K_{\mathbb Z}(L)=K_{\mathbb Q}(L)=K_{\mathbb R}(L).
$$

::: {.definition #def:vhs-monodromy title="Monodromy of a lattice-valued variation"}

Let $\mathbb V_{\mathbb Z}$ be a polarized integral variation of Hodge structure of weight two on a connected complex manifold $B$, with a base point $b$ and an isometry $\mathbb V_{\mathbb Z,b}\simeq L$. Its parallel transport defines
$$
m_{\mathbb V}\colon\pi_1(B,b)\longrightarrow O(L),\qquad
\Gamma_{\mathbb V}=\operatorname{im}m_{\mathbb V}.
$$
For a moduli stack, use its orbifold fundamental group. A different choice of fiber isometry conjugates $\Gamma_{\mathbb V}$ in $O(L)$.
:::

For a weight-two variation of K3 type, with Hodge numbers $(1,n,1)$ and the type-IV sign convention, the period map from the connected universal cover of $B$ lands in one component of $\Omega_L$. Equivariance implies $\Gamma_{\mathbb V}\subseteq O_{\mathrm{mod}}^+(L)$. If the induced discriminant local system is constant, then $\rho_L\circ m_{\mathbb V}=1$, and consequently
$$
\Gamma_{\mathbb V}\subseteq\widetilde O_{\mathrm{mod}}^+(L).
$$
### Lattice-polarized K3 periods

Fix a primitive embedding $P\hookrightarrow\Lambda_{\mathrm{K3}}$ of an even lattice of signature $(1,t)$, where $\Lambda_{\mathrm{K3}}$ is the even unimodular lattice of signature $(3,19)$. Put $T=P^\perp$. The group of changes of marking fixing the polarization pointwise is
$$
\Gamma(P)=\{\gamma\in O(\Lambda_{\mathrm{K3}}):\gamma|_P=1\}.
$$
Restriction to $T$ is injective. Its image $\Gamma_P$ is
$$
\Gamma_P=\ker\bigl(O(T)\to O(A_T,q_{A_T})\bigr)=\widetilde O(T),
\qquad
\operatorname{Stab}_{\Gamma_P}(\Omega_T^+)=\widetilde O_{\mathrm{mod}}^+(T).
$$
The first equality is [@Dol96, Proposition 3.3]; the second follows by intersecting with the period-component stabilizer. Dolgachev's ample lattice-polarized period space is the complement of the root hyperplanes in $\Omega_T$, modulo $\Gamma_P$ [@Dol96, §3, Corollary 3.2 and the discussion following Proposition 3.3].

### Kneser's comparison theorem

For a prime $p$, define $\operatorname{rank}_p(L)$ as the maximal rank of a sublattice whose Gram determinant is prime to $p$. Define the *rational spinorial kernel*
$$
O'(L)=SO(L)\cap K_{\mathbb Q}(L),\qquad
\widetilde{SO}_{\mathrm{mod}}^+(L)=SO(L)\cap\widetilde O_{\mathrm{mod}}^+(L).
$$

::: {.theorem #thm:kneser-spinor-comparison title="Kneser conditions"}

Let $L$ be an even lattice of signature $(2,n)$ with $n\geq2$. Suppose $L$ represents $-2$, $\operatorname{rank}_3(L)\geq5$, and $\operatorname{rank}_2(L)\geq6$. Then
$$
O'(L)=\widetilde{SO}_{\mathrm{mod}}^+(L)
=\langle s_u s_v:u,v\in L,\ b(u,u)=b(v,v)=-2\rangle.
$$
The generation statement is Kneser's theorem, as stated in [@GHS08, Theorem 1.1]; the equality with the stable real kernel is [@GHS08, Corollary 1.2].
:::

::: {.corollary #cor:kneser-full-spinor-kernel title="Integral and rational lifts under the Kneser conditions"}

Under the hypotheses of @thm:kneser-spinor-comparison,
$$
K_{\mathrm{lift},\mathbb Z}(L)=K_{\mathbb Q}(L)=\widetilde O_{\mathrm{mod}}^+(L)
=\langle s_a:a\in L,\ b(a,a)=-2\rangle.
$$
Moreover,
$$
\operatorname{im}\bigl(\operatorname{Spin}(L)(\mathbb Z)\to O(L)\bigr)
=O'(L)=\widetilde{SO}_{\mathrm{mod}}^+(L).
$$
:::

::: {.proof}

Assume the Kneser conditions and choose a root $a\in L$.

1. **Root reflection.** The formula $s_a(x)=x+b(x,a)a$ gives an integral isometry. For $x\in L^\vee$, its difference from $x$ lies in $L$, so $\rho_L(s_a)=1$. Also $\det(s_a)=-1$ and $\theta_{\mathbb Q}(s_a)=[1]$.
2. **Even parts.** The determinant-one parts of $K_{\mathbb Q}(L)$ and $\widetilde O_{\mathrm{mod}}^+(L)$ coincide and are generated by pairs of root reflections, by @thm:kneser-spinor-comparison.
3. **Odd parts.** Multiplication by $s_a$ identifies the determinant-minus-one part of each of these two groups with its determinant-one part, by step 1.
4. **Integral lifts.** The Clifford vector $a$ has $a^2=q(a)=-1$ and $a\bar a=1$. It is an integral norm-one lift of $s_a$. Products of these vectors lift the group generated by the root reflections; products of pairs lie in $\operatorname{Spin}(L)(\mathbb Z)$.
5. **Conclusion.** Steps 2–3 identify $K_{\mathbb Q}(L)$ with $\widetilde O_{\mathrm{mod}}^+(L)$ and give the stated generators. Step 4 and $K_{\mathrm{lift},\mathbb Z}(L)\subseteq K_{\mathbb Q}(L)$ identify the integral lifting subgroup. For the even subgroup, step 4 gives surjectivity onto $O'(L)$; scalar extension places the image of $\operatorname{Spin}(L)(\mathbb Z)$ in $O'(L)$.
:::

::: {.example #ex:polarized-k3-spinor-kernel title="The polarized K3 period lattice"}

For a primitive polarization of degree $2d$, $d>0$, the orthogonal complement in $\Lambda_{\mathrm{K3}}$ is
$$
L_{2d}=2U\oplus2E_8(-1)\oplus\langle-2d\rangle
$$
[@GHS08, equation (3)]. Its unimodular summand has rank $20$, so $\operatorname{rank}_2(L_{2d})$ and $\operatorname{rank}_3(L_{2d})$ are at least $20$. It contains $2U$ and a vector of square $-2$. Consequently @cor:kneser-full-spinor-kernel gives
$$
K_{\mathrm{lift},\mathbb Z}(L_{2d})
=K_{\mathbb Q}(L_{2d})=\widetilde O_{\mathrm{mod}}^+(L_{2d}).
$$
By [@Dol96, Proposition 3.3], this is the component-preserving period group for the fixed primitive polarization embedding.
:::

## Clifford groups for nonperfect forms

Let $M^\perp=\ker b_q^\sharp$, and let $O_{M^\perp}(M,q)$ denote the subgroup fixing $M^\perp$ pointwise. Zemel's Clifford group and twisted center are
$$
\Gamma(M,q)=\{c\in C(M,q)^\times:cM(c')^{-1}=M\},
\qquad
\widetilde Z(C)=\{c\in C:cx=xc'\text{ for every }x\in M\}.
$$
Twisted adjoint action gives
$$
1\longrightarrow\widetilde Z(C)^\times
\longrightarrow\Gamma(M,q)
\xrightarrow{\pi}O_{M^\perp}(M,q),
\qquad N(c)\in\widetilde Z(C)^\times.
$$
Suppose $O_{M^\perp}(M,q)$ is generated by the $e$-reflections and Euler transformations of [@Zem21, §2]. Suppose also that $R\hookrightarrow S$, that $M_S$ has an orthogonal basis $(x_i)$, and that every nonzero member of $\{2\}\cup\{q_S(x_i)\}$ is a non-zero-divisor in $S$. Then $\pi$ is surjective [@Zem21, Corollary 3.3, Proposition 3.7, and Theorem 3.8].

::: {.example #ex:spinor-integral-extension title="A generic spinor class which does not extend over the integers"}

Let $M=\mathbb Z^2$ with $q(x,y)=x^2-2y^2$. Its polar Gram matrix is $\operatorname{diag}(2,-4)$. The isometry $g(x,y)=(x,-y)$ is the reflection in $v=(0,1)$ over $\mathbb Q$.

1. **Generic obstruction.** The reflection formula gives $\theta_{\mathbb Q}(g)=[-q(v)]=[2]$.
2. **Integral discriminant classes.** Since $\operatorname{Pic}(\mathbb Z)=0$, the image of $\operatorname{Disc}(\mathbb Z)$ in $\operatorname{Disc}(\mathbb Q)$ consists of $[1]$ and $[-1]$. Each has even $2$-adic valuation, whereas $[2]$ has odd valuation.
3. **Conclusion.** No element of $\operatorname{Disc}(\mathbb Z)$ specializes to this generic spinor obstruction. In particular, a $\operatorname{Disc}(\mathbb Z)$-valued invariant on all integral isometries, compatible with the stated generic spinor norm, cannot exist for this quadratic module.

After passage to $\mathbb Z[1/2]$, the polar form is perfect and $2$ is a unit. The class is then represented by the discriminant line with pairing $2$, or equivalently by the $\mu_2$-torsor $t^2=2$.

To obtain a type-IV example, take $L=M\oplus\langle2\rangle$, where the last summand has bilinear Gram matrix $(2)$, and extend $g$ by the identity. Then $L$ has signature $(2,1)$ and $\theta_{\mathbb Q}^L(g)=[2]$. Thus $g\in O_{\mathrm{mod}}^+(L)\setminus K_{\mathbb Q}(L)$.
:::
