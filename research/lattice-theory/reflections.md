# Reflections and integral isometries {#sec-reflections}

Let $R$ be a Dedekind domain with fraction field $K$.

::: {.definition #def:reflection-in-a-vector title="Reflection in an anisotropic vector"}

Let $L\in\mathbf{Lat}_R$ and let $v\in L$ satisfy $\beta_L(v,v)\ne0$. The **reflection in $v$** is the $K$-linear morphism
$$
\begin{aligned}
s_v\colon L_K&\longrightarrow L_K,\\
x&\longmapsto x-\frac{2\,\beta_{L_K}(x,v)}{\beta_L(v,v)}\,v,
\end{aligned}
$$
where $L_K$ is the scalar extension of @def:module-base-change.
:::

::: {.proposition #prop:reflection-rational-isometry title="The reflection is an involutive isometry"}

The reflection $s_v$ is an involution in $\Orth(L_K)$, sends $v$ to $-v$, and restricts to the identity on the orthogonal-complement kernel $v^{\perp L_K}\hookrightarrow L_K$ of @def:orthogonal-complement.
:::

::: {.proof}
Put $c(x)=2\beta_{L_K}(x,v)/\beta_L(v,v)$. Then $c(v)=2$ and $c(x)=0$ when $x\in v^{\perp L_K}$. Furthermore,
$$
c(s_v(x))=c(x)-c(x)c(v)=-c(x),
$$
hence $s_v^2(x)=x$.
For $x,y\in L_K$, symmetry and bilinearity give
$$
\begin{aligned}
\beta_{L_K}(s_v(x),s_v(y))
={}&\beta_{L_K}(x,y)
-c(y)\beta_{L_K}(x,v)\\
&-c(x)\beta_{L_K}(v,y)
+c(x)c(y)\beta_L(v,v)
=\beta_{L_K}(x,y).
\end{aligned}
$$
Thus $s_v\in\Orth(L_K)$.
:::

::: {.definition #def:reflection-pairing-ideal title="Pairing ideal of a vector"}

For $L\in\mathbf{Lat}_R$ and $v\in L$, the **pairing ideal** is the image submodule
$$
I_v\definedas\operatorname{im}\qty{
\beta_L(-,v)\colon U(L)\longrightarrow R}
\hookrightarrow R.
$$
For $R=\bZ$, it equals $\div_L(v)\bZ$ by @def:lattice-divisibility.
:::

::: {.proposition #prop:reflection-integrality title="Integral reflections and their obstruction"}

Let $L\in\mathbf{Lat}_R$ and let $v\in L$ be anisotropic. Write the exact sequence in $R\text{-}\mathbf{Mod}$
$$
0\too U(L)\xrightarrow{\iota_L}L_K
\xrightarrow{q_L}\operatorname{coker}(\iota_L)\too0.
$$
The reflection $s_v\in\Orth(L_K)$ is induced by a unique integral isometry $\widetilde s_v\in\Orth(L)$ if and only if
$$
q_L\circ s_v\circ\iota_L=0.
$$
If the rank-one morphism $R\to U(L)$ determined by $1\mapsto v$ is primitive, this condition is equivalent to the ideal monomorphism
$$
2I_v\hookrightarrow\beta_L(v,v)R
$$
inside $R$.
:::

::: {.proof}
The displayed vanishing is exactly the condition that $s_v\circ\iota_L$ admit a unique lift along the kernel $\iota_L$:
```tikzcd
U(L) \arrow[r,dashed,"\widetilde s_v"] \arrow[d,"\iota_L"'] &
U(L) \arrow[d,"\iota_L"]\\
L_K \arrow[r,"s_v"'] & L_K.
```
Faithfulness of extension of scalars, together with $s_v^2=\id_{L_K}$ and the isometry identity of @prop:reflection-rational-isometry, gives $\widetilde s_v^2=\id_{U(L)}$ and preservation of $\beta_L$.

Suppose the rank-one embedding $R\to U(L)$ is primitive. Its cokernel is finitely generated torsion-free, hence projective over the Dedekind domain $R$. Thus the sequence splits, and there is an $R$-linear retraction $r\colon U(L)\to R$ with $r(v)=1$. For $x\in U(L)$ put $c_x=2\beta_L(x,v)/\beta_L(v,v)\in K$. The formula $s_v(x)=x-c_xv$ lies in $U(L)$ exactly when $c_xv\in U(L)$. Applying the retraction proves that this is equivalent to $c_x\in R$. Requiring this for every $x$ is precisely $2I_v\hookrightarrow\beta_L(v,v)R$.
:::
