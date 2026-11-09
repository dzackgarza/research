# Quadratic maps and divided powers {#sec-quadratic-divided-powers}

Fix a commutative ring $R$ and let $M,W\in R\text{-}\mathbf{Mod}$.

::: {.definition #def:R-quadratic-maps title="Quadratic maps of modules"}

For a map $q\colon M\to W$, define its cross-effect and its second scalar cross-action by
$$
\begin{aligned}
d_q\colon M\times M&\longrightarrow W,&
(x,y)&\longmapsto q(x+y)-q(x)-q(y),\\
q_{[r]}\colon M&\longrightarrow W,&
x&\longmapsto q(rx)-r^2q(x)
\qquad(r\in R).
\end{aligned}
$$
The map $q$ is **$R$-quadratic** when $d_q$ is $R$-bilinear and $q_{[r]}$ is a morphism in $R\text{-}\mathbf{Mod}$ for every $r\in R$. It is **homogeneous quadratic** when $q_{[r]}=0$ for every $r\in R$. Denote the corresponding $R$-modules of maps by $\operatorname{RQuad}_R(M,W)$ and $\operatorname{HQuad}_R(M,W)$, respectively.
:::

::: {.definition #def:quadratic-representing-modules title="Universal quadratic modules"}

The **universal $R$-quadratic module** $P_R^2(M)$ and the **degree-two divided-power module** $\Gamma_R^2(M)$ are the representing objects in $R\text{-}\mathbf{Mod}$ for the two functors of @def:R-quadratic-maps. Their universal quadratic maps are $p_M\colon M\to P_R^2(M)$ and $\gamma_M\colon M\to\Gamma_R^2(M)$, with natural isomorphisms
$$
\begin{aligned}
\Hom_{R\text{-}\mathbf{Mod}}\qty{P_R^2(M),W}
&\xrightarrow{\sim}\operatorname{RQuad}_R(M,W),&
f&\longmapsto f\circ p_M,\\
\Hom_{R\text{-}\mathbf{Mod}}\qty{\Gamma_R^2(M),W}
&\xrightarrow{\sim}\operatorname{HQuad}_R(M,W),&
g&\longmapsto g\circ\gamma_M.
\end{aligned}
$$
The latter representing object is the degree-two homogeneous component of the free divided-power algebra $\Gamma_R(M)$. Homogeneity of $\gamma_M$ gives a natural epimorphism $P_R^2(M)\twoheadrightarrow\Gamma_R^2(M)$ carrying $p_M(x)$ to $\gamma_M(x)$.
:::

::: {.proposition #prop:universal-quadratic-presentations title="Presentations of the quadratic representing modules"}

Let $F_R(M)$ be the free $R$-module on symbols $[x]$ indexed by $x\in M$. Let $K_R(M)\injects F_R(M)$ be the submodule generated, for $x,y,z\in M$ and $r,s\in R$, by
$$
\begin{aligned}
&[x+y+z]-[x+y]-[x+z]-[y+z]+[x]+[y]+[z],\\
&[rx+sy]-[rx]-[sy]-rs\qty{[x+y]-[x]-[y]},\\
&[rsx]-r^2[sx]-s[rx]+r^2s[x].
\end{aligned}
$$
Then there is an exact sequence in $R\text{-}\mathbf{Mod}$
$$
0\too K_R(M)\too F_R(M)
\xrightarrow{\pi_M}P_R^2(M)\too0,
$$
where $\pi_M([x])=p_M(x)$. The homogeneous quadratic module is presented by the corresponding cokernel with the additional relations $[rx]-r^2[x]$; equivalently, there is a natural epimorphism $P_R^2(M)\twoheadrightarrow\Gamma_R^2(M)$.
:::

::: {.proof}
An $R$-module morphism $F_R(M)\to W$ is uniquely determined by its values $q(x)$ on the generators. Its restriction to $K_R(M)$ vanishes if and only if the cross-effect $d_q$ is additive in both variables and satisfies $d_q(rx,sy)=rs\,d_q(x,y)$ and each second scalar cross-action $q_{[r]}$ is $R$-linear. These are the conditions of @def:R-quadratic-maps; the cokernel universal property establishes the first representing isomorphism. Adding $[rx]=r^2[x]$ forces homogeneity, giving the second representing isomorphism. The resulting degree-two homogeneous relations are the relations for the degree-two summand of the divided-power algebra.
:::

::: {.proposition #prop:quad-presheaf-homogeneous title="Quadratic forms are homogeneous quadratic maps"}

For $M\in R\text{-}\mathbf{Mod}$, precomposition with $\gamma_M$ is an isomorphism of $R$-modules
$$
\operatorname{Quad}_{R,W}(M)\xrightarrow{\sim}\operatorname{HQuad}_R(M,W),
\qquad
g\longmapsto g\circ\gamma_M,
$$
between the quadratic-form presheaf of @def:form-presheaves and the homogeneous quadratic maps of @def:R-quadratic-maps.
It is natural in $M$: for $f\colon M\to N$ it takes the pullback $f^*$ of @def:form-presheaves to precomposition with $f$.
:::

::: {.proof}

By @def:form-presheaves, $\operatorname{Quad}_{R,W}(M)$ is the $R$-module of $R$-linear maps $\Gamma_R^2(M)\to W$, and $\gamma_M$ is universal among maps $q\colon M\to W$ with $q(rx)=r^2q(x)$ for all $r\in R$ and $R$-bilinear polarization $d_q$.
These conditions say that $q_{[r]}=0$ for every $r$ and that $d_q$ is $R$-bilinear; since the zero map is a morphism of $R$-modules, they are exactly the conditions of @def:R-quadratic-maps for a homogeneous quadratic map.
So the universal property of $\gamma_M$ states that $g\mapsto g\circ\gamma_M$ is a bijection onto $\operatorname{HQuad}_R(M,W)$, and it is $R$-linear in $g$.
In particular the module $\Gamma_R^2(M)$ of @def:form-presheaves and the one of @def:quadratic-representing-modules represent the same functor through the same kind of universal map, so they are isomorphic by a unique isomorphism compatible with the two maps $\gamma_M$.

For $f\colon M\to N$ and $g\in\operatorname{Quad}_{R,W}(N)$, the definition $\Gamma_R^2(f)[x]=[f(x)]$ gives $\Gamma_R^2(f)\circ\gamma_M=\gamma_N\circ f$, so
$$
\bigl(f^*g\bigr)\circ\gamma_M=g\circ\Gamma_R^2(f)\circ\gamma_M=(g\circ\gamma_N)\circ f.
$$
:::
