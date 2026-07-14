## Coble to Enriques Cusp Correspondence

:::{.theorem}
The embedding $\eta: F_{\Co}\to F_{\En}$ induces the correspondence on boundary cusps of the Baily-Borel compactifications shown in \cref{fig:enriques-coble-correspondence}.

\begin{figure}[H]
\centering
\input{tikz/coble-enriques-cusp-correspondence.tikz}
\caption{Cusp correspondence $F_{\Co} \to F_{\En}$.}
\label{fig:enriques-coble-correspondence}
\end{figure}
:::

:::{.remark}
We prove this correspondence by considering divisibilities at the corresponding 0-cusps and 1-cusps in both moduli spaces.
We first note that since $T_{\Co}$ can be written as $L(2)$ where $L = \gens{1} \oplus E_8$, every $v\in T_{\Co}$ satisfies $\div_{T_{\Co}}(v) = 2$.
:::

:::{.lemma}
\label{lem:divisibility_Tco_one}
Fixing notation,
\begin{align*}
    v_1 &\da e' & w_1 &\da \eta(v_1) = \tilde e' \\
    v_2 &\da 2h + \alpha_1 + \alpha_2 & w_2 &\da \eta(v_2) = 2\tilde e + 2\tilde f + \tilde\alpha_1 + \tilde\alpha_2 \\
    J &\da \gens{v_1, v_2} & \tilde J &\da \gens{w_1, w_2}
\end{align*}
We then have $\mathrm{div}_{T_{\En} }(w_1) = 2$.
:::

:::{.proof}
This follows from the fact that $\tilde e\in U(2)$ where 
$T_{\En} = U \oplus U(2) \oplus E_8(2)$ 
Noting that
$\tilde e' \tilde f' = 2$, and $\tilde e'$ is orthogonal to the remaining generators of in the $U$ and $E_8(2)$ summands, we thus have
\[
\mathrm{div}_{T_{\En} }(w_1) \da \mathrm{div}_{T_{\En} }(\eta(e'))  
 = \mathrm{div}_{T_{\En} }(\tilde e') = 2
.\]
Explicitly, one can check the pairing of $\tilde e'$ against an arbitrary vector. 
Write $x+y+z\in U \oplus U(2)\oplus E_8(2)$, then 
\[
\tilde e'\cdot(x+y+z) = \tilde e'\cdot y\in \ts{0, 2}
\]
since $y\in U(2)$ and $\tilde e'\in (U\oplus E_8(2))^{\perp T_{\En}}$.
Thus $\beta_{T_{\En}}(\tilde e', T_{\En}) = \beta_{T_{\En}}(\tilde e', U(2)) = 2\bZ$ since $\tilde e'\cdot\tilde f' = 2$.
:::


:::{.lemma}
\label{lem:w1_perp_calculation}
The 0-cusp $(9,9,1)_1$ in $F_{\Co}$ maps to the zero-cusp $(10, 8, 0)_1$ in $F_{\En}$.
:::

:::{.proof}
The cusp correspondence follows from computing the lattice $w_1^{\perp T_{\En}}/\gens{w_1}$ under the primitive embedding $\eta$, since $\eta(v_1) = w_1$ and $v_1$ is the isotropic vector corresponding to $(9,9,1)_1$ in $F_{\Co}$.
This particular case follows from a direct computation:
\begin{align*}
{
(\tilde e')^{\perp T_{\En}} \over \gens{\tilde e'}
}
&= {
\gens{\tilde e,\tilde f} \oplus \gens{\tilde e'} \oplus \gens{\tilde \alpha_1, \cdots, \tilde \alpha_8} \over \gens{\tilde e'}
} \\
&\cong \gens{\tilde e, \tilde f} \oplus \gens{\tilde \alpha_1, \cdots, \tilde \alpha_8} \\
&\cong U \oplus E_{8}(2) 
\cong (10,8,0)_1
.\end{align*}

Alternatively, by \cite[Prop. 5.5]{AE22nonsympinv}, the isomorphism type of $w_1^{\perp T_{\En}}/w_1$ is determined by $\mathrm{div}_{T_{\En}}(w_1)$; by \cref{lem:divisibility_Tco_one} $\mathrm{div}_{T_{\En}}(w_1) = 2$. 
Since the divisibility of the isotropic vector at the Enriques 0-cusp $(10, 8, 0)_1$ is also 2 and the two Enriques 0-cusps are distinguished by divisibility, the correspondence follows.
:::

:::{.lemma}
\label{lem:1_cusp_correspondence}
Cusp $(7,7,1)_0$ in $F_{\Co}$ maps to cusp $(8, 6, 0)_0$ in $F_{\En}$.
:::

:::{.proof}
The results follows from verifying that the unique orbit $J$ of a primitive isotropic plane in $T_{\Co}$ satisfies $J^{\perp T_{\Co}}/J \cong (7,7,1)$, and identifying the isomorphism type of its image $\tilde J^{\perp T_{\En}}/\tilde J$ in $T_{\En}$.
One checks that both $v_2$ and $w_2$ are isotropic, and $v_2 \in v_1^{\perp T_{\Co}}/v_1$, and so $J$ and $\tilde J$ define isotropic planes in $T_{\Co}$ and $T_{\En}$ respectively. By \cite[Prop. 5.5, Lem. 5.9]{AE22nonsympinv}, it suffices to show
\[
\mathrm{div}_{w_1^{\perp T_{\En}} /w_1}(w_2)  \da \mathrm{div}_{U \oplus E_8(2)}(2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2)= 2
,\]
since the isomorphism type of $\tilde J^\perp/\tilde J$ is uniquely determined by the isomorphism type of $w_2^{\perp T_{\En}}/w_2$ in $w_1^{\perp T_{\En}}/w_1$, which is in turn uniquely determined by the characterization of $w_2$ as odd, even ordinary, or even characteristic in $w_1^{\perp T_{\En}}/w_1$, which by \cref{lem:w1_perp_calculation} is isomorphic to $U \oplus E_8(2)$. One checks directly in coordinates: let $x+y\in U \oplus E_8(2)$ and consider its pairing with $w_2$:
\begin{align*}
(x+y)\cdot w_2 
= (x+y)\cdot (2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2 )
= 2x\cdot (\tilde e + \tilde f) + y\cdot (\tilde \alpha_1 + \tilde \alpha_2)
,\end{align*}
where we've used orthogonality relations. We note that the first term is evidently even, while the second term is even because all pairings are either zero or divisible by two in the $E_8(2)$ summand of $U \oplus E_8(2)$.
:::

