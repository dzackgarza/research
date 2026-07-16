# Moduli Spaces Summary

We summarize the relevant moduli spaces:

$$
\begin{aligned}
F_\En &= \bD(T_\En)/\Orth(T_\En) &
F_{\En, 2} &= \bD(T_\En)/\Gamma_{\En, 2} \\
F_\Co &= \bD(T_\Co) / \Orth(T_\Co) &
F_{\Co, 2} &= \bD(T_\Co)/\Gamma_{\Co, 2}
\end{aligned}
$$

where

$$
\begin{aligned}
\Gamma_{\En, 2} &= \Orth(T_\En) \intersect \Orth(T_\dP) \subseteq \Orth(\lkt) \\
\Gamma_{\Co, 2} &= \mathrm{Stab}_{\Orth(T_\En)}(T_\Co) \subseteq \Orth(T_\En) \\
F_{\Nod} &= \bD(T_\Nod)/\Orth(T_\Nod) \\
F_{\Nod, 2} &= ???
\end{aligned}
$$

where $T_{\dP}$ is described in [@AEGS23]. Note that we implicitly use the embedding $\eta: T_\Co \injects T_\En$.
We note, as in [@DK13], that $T_{\Co} \cong v^{\perp T_{\En}}$ for some $v^2=-2$, which implies that there is a birational isomorphism $F_{\Co} \birational \cH_{-2}/\Orth(T_\En)$.

# GIT Discussion

::: {.remark}

Following [@DK13], by varying the coefficients of $p_i$ in the planar blowup
construction, one can construct $F_\Co$ as a locally closed subvariety of
$(\PP^2)^{10}/\PGL_3$, which is of dimension

$$
\dim (\PP^2)^{10}/\PGL_3 = \dim (\PP^2)^{10} - \dim \PGL_3 = 2\cdot 10 - (3^2-1) = 12
.
$$

A posteriori, the number of moduli for a Coble surface is 9, which
means that there should be 3 conditions imposed upon the configuration
of 10 points.
These 3 conditions are precisely the _discriminant
conditions_ described in [@Cob19 §2, Prop. (10)].
:::

# Horikawa model

::: {.remark}

Alternatively, Horikawa [@Hor78] and more recently [@AEGS23] consider
the following: let $Y\da \PP^1\times \PP^1$ and define an involution
$\tau(x,y) \da (-x,-y)$.
Letting $B\in\abs{-2K_Y}^\tau$ be a
$\tau$-invariant anti-bicanonical curve in $Y$, if $B$ passes through a
$\tau$-fixed point $x,y\in \ts{0, \pm \infty}$, then the corresponding
double branched cover branched over $B$ is a K3 surface $X$ with $A_1$
singularities and involution $\iota_{\dP}$, and the quotient
$Z\da X/\gens{\iota}$ is a Coble surface.
The case in which $B$ does not
pass through a $\tau$-invariant point yields an Enriques surface $Z$,
and an analysis of the corresponding moduli is carried out in [@AEGS23].

It is well-known that there consequently exists a Coble surface $S$ and
a blowdown $S\to X/\iota$ along the strict transform of $B$.
In this
way, one realizes the moduli space $F_{\Co}$ of unpolarized Coble
surfaces as a divisor in $F_{\En}$, the 10-dimensional moduli space of
unpolarized Enriques surfaces.
:::

# Period Domains

By passing to the K3 cover, one can embed $F_\Co$ into an arithmetic quotient of a 9-dimensional Hermitian symmetric domain of type $\rm{IV}$.
Let $\lkt = U^3 \oplus E_8^2$ be the canonical K3 lattice.
We recall that for any primitively embedded lattice $S\injects \lkt$, letting $T \da S^{\perp \lkt}$, there is a Hodge-theoretic description of the coarse moduli space $F_S$ of $S$-polarized K3 surfaces given by $$F_S \da D_T/\Orth(T)^*$$

where $\Orth(T)^* \da \ker\qty{\Orth(T) \to \Orth(q_T)}$.
Letting $E_{10} \da U \oplus E_8$, one can similarly consider the Enriques lattices $S_\En := E_{10}(2)$ with $T_\En = U \oplus E_{10}(2)$.
Letting

$$
\cH_{-2d} = \Union_{\delta^2 = -2d} \delta^{\perp D_T}
,
$$

one can thus present

$$
\begin{aligned}
F_{\En} &= \qty{D_{T_\En} \setminus \cH_{-2}} / \Orth(T_\En) \\
F_{\Co} &= \cH_{-2} / \Orth(T_\En) \\
F_{\Nod} &= \qty{\cH_{-4} \setminus \cH_{-2}} / \Orth(T_\En)
\end{aligned}
$$

where surfaces along the divisor $\cH_{-2}$ in $F_\En$ correspond precisely to Coble surfaces and those along $\cH_{-4}\setminus \cH_{-2}$ correspond to Enriques surfaces with $A_1$ singularities.

Alternatively, one can construct the period domain for $F_\Co$ directly.
Following [@DK13 Prop. 3.1] almost verbatim, let $S$ be the blowup of $\PP^2$ along 10 $A_1$ singularities of a rational sextic curve $C$.
The double branched cover $f:X\to S$ branched along the proper transform of $C$ contains the pullback of ten exceptional classes $E_1,\cdots, E_{10}$ over the ten $A_1$ singularities, as well as $E_0$, the pullback of a hyperplane class.
Since $E_i^2 = -2$ for $1\leq i \leq 10$, and one can show that $E_0^2 = 2$, the $E_i$ generate a lattice isometric to

$$
S_\Co \da \gens{2}\oplus \gens{-2}^{10} = \latI_{1, 10}(2) = (11, 11, 1)_1 \cong \gens{-2} \oplus E_{10}(2)
.
$$

This follows from the fact that $S_{\Co}$ is a 2-elementary lattice of signature $(1, 10)$ with discriminant group $(\bZ/2\bZ)^{11}$ and thus uniquely determined up to isometry by its invariants $(r,a,\delta)$.
Similarly, its orthogonal complement $T_{\Co}$ in the K3 lattice $\lkt$ is a 2-elementary lattice of signature $(2, 9)$ and satisfies $q_{S_{\Co}} = -q_{T_{\Co}}$.
The isomorphism class of $q_{T_{\Co}}$ determines $T_\Co$, and thus one has

$$
T_\Co \da S_\Co^{\perp \lkt} = (11, 11, 1)_2 \cong \gens{2} \oplus E_{10}(2)
.
$$

Alternatively, this follows immediately from the mirror move $S\leadsto T$ of [@AE22 Thm. 5.10] applied to $S_\Co =(11, 11, 1)_1$.
We obtain $F_\Co$ as an open subset of the period domain $D_{T_\Co}/\Orth(T_\Co)$, a normal quasiprojective variety of dimension 9, by [@DK13 Prop. 3.2] and an application of the Torelli theorem for algebraic K3 surfaces from [@PS71]. We note that [@DK13] shows that $F_\Co$ is rational by relating it to a codimension one subvariety of a moduli space of certain $A_2$-singular quintics in $\PP^2$.

# KSBA Spaces
