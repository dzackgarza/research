## Moduli of Coble Surfaces

::: {.remark}
We begin with a naive parameter space for Coble surfaces.
Following \cite{DK13}, by varying the coefficients of $p_i$ in the planar blowup construction, one can construct $F_\Co$ as a locally closed subvariety of $(\PP^2)^{10}/\PGL_3$, which is of dimension
\[
\dim (\PP^2)^{10}/\PGL_3 = \dim (\PP^2)^{10} - \dim \PGL_3 = 2\cdot 10 - (3^2-1) = 12
.\]
A posteriori, the number of moduli for a Coble surface is 9, which means that there should be 3 conditions imposed upon the configuration of 10 points. These 3 conditions are precisely the *discriminant conditions* described in \cite[\S 2,\,Prop. (10)]{Cob19}.
Letting $D$ be the corresponding discriminant locus, we can identify $F_{\Co}$ as an open subset of $\qty{ (\PP^2)^{10} \sm D }/\PGL_3$ at the level of coarse moduli spaces.
We note that \cite{DK13} shows that $F_\Co$ is rational by relating it to a codimension one subvariety of a moduli space of certain cuspidal quintics in $\PP^2$.
:::

::: {.remark}
Alternatively, Horikawa \cite{Hor78b} and more recently \cite{AEGS23} consider the following: let $Y\da \PP^1\times \PP^1$ and define an involution $\tau(x,y) \da (-x,-y)$. Let $B\in\abs{-2K_{Y}}^\tau$ be a $\tau$-invariant anti-bicanonical curve in $Y$. If $B$ passes through a $\tau$-fixed point $x,y\in \ts{0, \pm \infty}$, then the corresponding double branched cover branched over $B$ is a nodal K3 surface $X$ with covering involution $\iota_{\dP}$ such that $Y = X/\gens{\iota_{\dP}}$. Letting $\iota_{\En}$ be a lift of $\tau$, the quotient $Z\da X/\gens{\iota_{\En}}$ is a Coble surface. The case in which $B$ does not pass through a $\tau$-invariant point yields an Enriques surface $Z$, and an analysis of the corresponding moduli space is carried out in \cite{AEGS23}.
In this way, one realizes the moduli space $F_{\Co}$ of unpolarized Coble surfaces as a boundary divisor in $F_{\En}$, the 10-dimensional moduli space of unpolarized Enriques surfaces.
:::

::: {.remark}
By passing to the K3 cover, one can embed $F_\Co$ into an arithmetic quotient of a 9-dimensional Hermitian symmetric domain of type $\rm{IV}$. Let $\lkt = U^3 \oplus E_8^2$ be the canonical K3 lattice. We recall that for any primitively embedded lattice $S\injects \lkt$, letting $T \da S^{\perp \lkt}$, there is a Hodge-theoretic description of the coarse moduli space $F_S$ of $S$-polarized K3 surfaces given by
\[
F_S \da D_T/\tilde\Orth(T)
\]
where $\tilde \Orth(T) \da \ker\qty{\Orth(T) \to \Orth(q_T)}$ and $D_T$ is a connected component of
\[
\Omega_T \da \ts{[v]\in \PP(T_\CC) \st v^2=0,\, v\bar v > 0}
.\]
Letting $E_{10} \da U \oplus E_8$, one can consider the Enriques lattices $S_{\En} := E_{10}(2)$ with $T_{\En} \da U \oplus E_{10}(2)$. Letting
\[
\cH_{-2d} = \Union_{\delta^2 = -2d} \delta^{\perp D_T}
.\]
We note, as in \cite{DK13}, that $T_{\Co} \cong v^{\perp T_{\En}}$ for some $v^2=-2$, which implies that there is a birational isomorphism $F_{\Co} \birational \cH_{-2}/\Orth(T_{\En})$.
Thus up to birational isomorphism, one can present
\begin{align*}
F_{\En} &= \qty{D_{T_{\En}} \setminus \cH_{-2}} / \tilde \Orth(T_{\En}) \\
F_{\Co} &= \cH_{-2} / \tilde \Orth(T_{\En}) \\
\end{align*}
where surfaces along the divisor $\cH_{-2}$ in $F_{\En}$ correspond precisely to Coble surfaces. We note that surfaces along $\cH_{-4}\setminus \cH_{-2}$ correspond to nodal Enriques surfaces, an interesting divisor in its own right.
:::

::: {.remark}
We summarize the relevant moduli spaces:
\begin{align*}
F_{\En} &= D_{T_{\En}}/\tilde \Orth(T_{\En}) & 
F_{\En, 2} &= D_{T_{\En}}/\Gamma_{\En, 2} \\
F_\Co &= D_{T_{\Co}} / \tilde \Orth(T_{\Co}) & 
F_{\Co, 2} &= D_{T_{\Co}}/\Gamma_{\Co, 2} 
\end{align*}
where
\begin{align*}
\Gamma_{\En, 2} &= \Orth(T_{\En}) \intersect \Orth(T_\dP) \subseteq \Orth(\lkt) \\
\Gamma_{\Co, 2} &= \mathrm{Stab}_{\Orth(T_{\En})}(T_{\Co}) \subseteq \Orth(T_{\En})
\end{align*}
where $T_{\dP}$ is described in \cite{AEGS23}.
Note that we implicitly use the embedding $\eta: T_{\Co} \injects T_{\En}$ of \cref{lem:embedding_eta}.
:::

::: {.remark}
By \cref{lem:lattice-embeddings-induce-morphisms}, there are morphisms $\overline{F_{\Co}}^{\bb} \to \overline{F_{\En}}^{\bb}$ and $\overline{F_{\Co}}^{\bb} \to \overline{F_{(2,2,0)}}^{\bb}$ which induce correspondences between the boundary cusps.
:::

::: {.remark}
We set up the moduli space of KSBA stable pairs for Coble surfaces, possibly using the ramification divisor of the K3 involution (which is in this case not fixed-point free).
The above embeddings should allow us to take closures of stable pairs in already existing moduli spaces.
:::
