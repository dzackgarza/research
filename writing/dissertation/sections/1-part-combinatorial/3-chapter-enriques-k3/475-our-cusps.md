### Enumeration of Baily–Borel 0-cusps via Diagram Folding {#sec:fent-zero-cusps}



The boundary lattices at 0-cusps $\eta$ have the form $\bdlattice{T}{\eta} = \eta^\perp/\gens{\eta}$ for each primitive isotropic vector $\eta$. 
The typical situation is two have some number $n$ of possible isometry classes for boundary lattices, and some number $m\geq n$ of *actual* boundary lattices, where $m$ depends on $\Gamma$, reflecting isometry classes splitting into further possibilities.
For $\fttz$, there are two isometry classes, each containing one sub-type of lattice, so the two cusps can be labeled
$$
\tilde\eta_1 \da (18, 2, 0)_1, \qquad 
\tilde \eta_2 \da (18, 0, 0)_1
.$$
For $\fent$, there are two isometry classes, one which does not split into further subclass corresponding to orbits of divisibility one vectors in $\ten$, the other splitting into four sub-classes, reflecting an $\Orth(\ten)$ orbit of divisibility two vectors that splits into 4 separate orbits.
We label the cusps $\eta_1,\cdots, \eta_5$, and note that the two isometry classes are given by
$$
\div_{\ten}(\eta) = 1\colon \EnriquesInvariants_1,
\qquad 
\div_{\ten}(\eta) = 2\colon (10, 8, 0)_1
$$


| $\fent$ Cusp | $\fttz$ Cusp | Involution | Folded Lattice |
|---|---|---|---|
| $\eta_1$ ($\div(\eta_1) = 1$) | $\tilde\eta_1 \da (18,2,0)_1$ | $180^\circ$ rotation | $\EnriquesInvariants_1$ |
| $\eta_2$ ($\div(\eta_2) = 2$) | $\tilde\eta_2 \da (18,0,0)_1$ | Vertical reflection | $(10,8,0)_1$ |
| $\eta_3$ ($\div(\eta_3) = 2$) | $\tilde\eta_1 \da (18,2,0)_1$ | Diagonal + reflection | $(10,8,0)_1$ |
| $\eta_4$ ($\div(\eta_4) = 2$) | $\tilde\eta_1 \da (18,2,0)_1$ | Horizontal reflection | $(10,8,0)_1$ |
| $\eta_5$ ($\div(\eta_5) = 2$) | $\tilde\eta_1 \da (18,2,0)_1$ | 8 commuting reflections | $(10,8,0)_1$ |

### Cusps by Folding

Following [@AEGS25, Lemmas 3.10, 3.19], the five 0-cusps of the Baily–Borel compactification $\bbcpt{\fent}$ correspond to five different involutions on the K3 lattice $\tdp$.
Let $T$ be an even indefinite lattice and let $\eta \in T$ be a primitive isotropic vector. Define the boundary lattice $\bdlattice{T}{\eta} \da  \eta^{\perp T} / \gen{\eta}$, which we will often simply write as $\bar T \da \eta^{\perp}/\eta$ when working with a fixed vector $\eta$.
Write $\Phi(\bar T)$ for the root system of $\bdlattice{T}{\eta}$.
Let $\Gamma\leq \Orth(T)$ be a fixed arithmetic subgroup acting on $T$.
For each such $\eta$, we write $U_\eta$ for the maximal unipotent subgroup of the stabilizer of $\eta$ in $\Gamma$ which acts trivially on $\bdlattice{T}{\eta}$.
This group thus fits into an exact sequence
$$
0 \to U_\eta \to \Stab_\Gamma(\eta) \to \Gamma_{\eta} \to 0
.$$
We refer to $\Gamma_\eta$ as the **stable boundary group at $\eta$** and its corresponding reflection subgroup $W(\Gamma_\eta)$ as the **stable reflection group at $\eta$**.
When $\Gamma = \Orth(T)$, we will write this as $W(\bar T)$.
We write $\thecone{C}( \Gamma_\eta )$ for the corresponding fundamental chamber of $W(\Gamma_\eta)$, and $G( \Gamma_\eta )$ for its Coxeter diagram.
When $\bdlattice{T}{\eta}$ is hyperbolic, it is known that $\Orth(\bdlattice{T}{\eta})$ is an extension of $W(\bdlattice{T}{\eta})$ by a subgroup of chamber symmetries $\Aut( \thecone{C}( \Gamma_\eta ))$, and
thus any diagram automorphism of $G(\Gamma_\eta)$ induces a chamber symmetry and thus an isometry of $\bdlattice{T}{\eta}$.
Let $J$ be an involution of $\bdlattice{T}{\eta}$, for example induced by an diagram involution on $G(\Gamma_\eta)$. We then write $G( \Gamma_\eta )^{J}$ for the corresponding folded diagram, $\thecone{C}( \Gamma_\eta )^J$ its folded fundamental chamber, and so on.

We recall the definitions
$$
\ten = U \oplus U(2) \oplus E_8(2) = (12,10,0)_2 \injects
\tdp = U \oplus U(2) \oplus E_8^2 = (20, 2, 0)_2
,$$
and write $\Ien, \Idp$, and $\Inik$ for the involutions on $\lkt$ induced by the geometric involutions $\ien, \idp$, and $\inik$ respectively.
In the decomposition $\lkt = U + U^2 \oplus E_8^2$, these involutions can be written in block form as follows:
$$
\Idp:
\begin{pmatrix}
-1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 & 0 \\
0 & 0 & 0 & 0 & -1
\end{pmatrix},
\quad
\Ien:
\begin{pmatrix}
-1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 0
\end{pmatrix},
\quad 
\Inik:
\begin{pmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & -1 \\
0 & 0 & 0 & -1 & 0
\end{pmatrix}
,$$ {#eq:involution-lattice-block-forms}
or as in @eq:three-lattice-involutions,
\begin{align*}
\Idp: (u_1,\ u_2,\ u_3,\ \alpha_1,\ \alpha_2) &\to (-u_1,\ u_3,\ u_2,\ -\alpha_1,\ -\alpha_2)
\\
\Ien:(u_1,\ u_2,\ u_3,\ \alpha_1,\ \alpha_2) &\to (-u_1,\ u_3,\ u_2,\ \alpha_2,\ \alpha_1)
\\
\Inik:(u_1,\ u_2,\ u_3,\ \alpha_1,\ \alpha_2) &\to (u_1,\ u_2,\ u_3,\ -\alpha_2,\ -\alpha_1)
\end{align*}
By [@AEGS25, Lem. 3.4], the coinvariant sublattice $\tdp^{\Ien = -1}\iso \ten$, and so to simplify matters we write $I \da - \Ien = \Inik$ and thus $\tdp^{I} \da \tdp^{I=1} = \ten$.
Fixing a primitive isotropic vector $\eta \in \ten$, we write $\bdlattice{\ten}{\eta} \da \eta^{\perp \ten}/\gens{\eta}_{\ten}$ and $\bdlattice{\tdp}{\eta} \da \eta^{\perp \tdp}/\gens{\eta}_{\tdp}$, and so on.
Under the primitive embedding $\ten\injects \tdp$, we can construct two distinct boundary lattices associated to $\eta$,

\begin{align*}
\bdlattice{\ten}{\eta} \da \eta^{\perp \ten}/\gens{\eta}, 
\qquad 
\bdlattice{\tdp}{\eta} \da \eta^{\perp \tdp}/\gens{\eta}
,
.\end{align*}

where we carefully identify $\eta$ with its image in $\tdp$ under the embedding.
There are two possible isometry classes possible for $\bdlattice{\tdp}{\eta}$:
$$
\bdlattice{\tdp}{\eta}:\quad 
(18, 2, 0)_1 = U(2) \oplus E_8^2
,\quad\textor\quad 
(18,0,0)_1 = U \oplus E_8^2
,$$
corresponding to the two 0-cusps of the Baily-Borel compactification $\bbcpt{\fttz}$, and distinguished by the divisibility $\div_{\tdp}(\eta)$ of $\eta$ in $\tdp$. 
From a similar analysis of $\bbcpt{\fen}$, the moduli space of *unpolarized* Enriques surfaces, one finds that there are similarly two possibilities
$$
\bdlattice{\ten}{\eta}: \quad
\EnriquesInvariants_1 = U(2) \oplus E_8(2)
,\quad\textor\quad 
(10,8,0)_1 = U \oplus E_8(2)
.$$
Both possibilities for $\bdlattice{\tdp}{\eta}$ are hyperbolic, 2-elementary lattices with induced involutions $\bar{I}_{\En}$ and $\bar{I}_{\dP}$, and if we write $J\da -\bar{I}_{\En}$ then we recover $\bdlattice{\tdp}{\eta}^J = \bdlattice{\ten}{\eta}$ as the invariant sublattice.
We immediately note that the involution $J$ is highly sensitive to the choice of $\eta$, as are the isometry classes of $\bdlattice{\tdp}{\eta}$ and thus $\bdlattice{\ten}{\eta}$ -- in our situation, this highly depends on the geometry of the moduli spaces $\fent$ and $\fttz$.
To make this dependence explicit, we define the arithmetic groups used to construct period domains for these spaces.
We define a distinguished polarization
$$
h = e + f \in \sdp \iso U(2) \injects \sen \iso U(2) \oplus E_8(2) = \EnriquesInvariants_1
,$$
and writing $\Psi: \Orth(\lkt) \to \Orth(\ten)$ for the restriction map,
$$
\Gamma_{\En, 2} \da \Psi\qty{\ts{ 
g\in \Orth(\lkt) \st g\circ \Ien = \Ien\circ g, \, g(h) = h
}},\,\,\, \Gamma_{\dP} \da \Orth(\tdp)
,$$
where we form $\Gamma_{\En, 2}$ by taking the intersection of the commutator of $\Ien$ in $\Orth(\lkt)$, intersecting it with the stabilizer of the polarization, and taking the image in $\Orth(\ten)$.
This is the correct monodromy group for $\fent$; the full details can be found e.g. in [@Ste91].
For any lattice $T$ of signature $(2, n)$, we define its period domain as
$$
\halfpd{T} \da\ts{ [v]\in \PP(T_\CC) \st v^2 = 0, v\bar{v} > 0 }\interior
,$$
where $(\wait)\interior$ denotes taking one connected component. 
We then define the two moduli spaces
$$
\fent \da \dmodgamma{ \halfpd{T} }{ \Gamma }_{\En, 2},
\qquad
\fttz \da \dmodgamma{ \halfpd{T} }{ \Gamma }_{\dP} = \halfpd{T}/\Orth(\tdp)
.$$
corresponding to degree 2 numerically polarized Enriques surfaces and quartic hyperelliptic K3 surfaces respectively.
To study the Baily-Borel compactification $\bbcpt{\fent}$, we will be interested in $\Gamma_{\En, 2}$-orbits of primitive isotropic vectors $\eta_i$, which correspond to 0-cusps, and the Coxeter diagrams for the stable reflection groups $\Gamma_{\En, 2, \eta_i}$ at each $\eta_i$, which can be used to determine the 1-cusps and their adjacencies.
We note that if $\alpha\in \Phi(\tdp)$ is a (negative) root of $\tdp$, then the folded root $\alpha_I$ is in $\Phi(\tdp^I) = \Phi(\ten)$ and is thus a root of $\ten$.
We can thus use the known stable reflection groups of $\tdp$ at its known 0-cusps to study those of $\ten$ and $\bar{\ten}_{\eta_i}$ at each cusp $\eta_i$.
We analyze the structure of reflection groups and invariant lattices associated to each $0$-cusp $\eta_i$ on the moduli space, using the correspondence between the (negative) roots of the covering domain and its foldings. The results are organized by cusp.

Let $\eta_1,\ldots,\eta_5$ denote the five distinguished $0$-cusps with the invariants, lattices, and automorphism relations described as follows:

#### Cusp $\eta_1 = e$ (divisor $1$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,2,0)_1, \qquad U(2)\oplus E_8^2 \\
&\text{Automorphism: rotation by } 180^\circ: && 
\begin{cases}
\alpha_i \leftrightarrow \alpha_{8+i}, & i=0,\ldots,7 \\
\alpha_{16} \leftrightarrow \alpha_{18} \\
\alpha_{17} \leftrightarrow \alpha_{19}
\end{cases} \\
&\text{Invariants:} && \EnriquesInvariants_1, \qquad U(2)\oplus E_8(2)
\end{aligned}
$$

#### Cusp $\eta_2 = e'$ (divisibility $2$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,0,0)_1, \qquad U\oplus E_8^2 \\
&\text{Automorphism: vertical reflection:} && 
\alpha_i \leftrightarrow \alpha_{20-i}, \quad i=1,\ldots,9 \\
&\text{Invariants:} && (10,8,0)_1, \qquad U\oplus E_8(2)
\end{aligned}
$$

#### Cusp $\eta_3 = e'+f'+\omega$, $\omega^2 = -4$ (divisibility $2$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,2,0)_1, \qquad U(2)\oplus E_8^2 \\
&\text{Automorphism: diagonal reflection:} && 
\begin{cases}
\alpha_i \leftrightarrow \alpha_{16-i}, & i=1,\ldots,7 \\
\alpha_{17} \leftrightarrow \alpha_{19} \\
s_{\alpha_{20}} \text{ fixes}
\end{cases} \\
&\text{Invariants:} && (10,8,0)_1, \qquad U\oplus E_8(2)
\end{aligned}
$$

#### Cusp $\eta_4 = e'+2f'+\alpha$, $\alpha^2 = -8$ (divisibility $2$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,2,0)_1, \qquad U(2)\oplus E_8^2 \\
&\text{Automorphism: horizontal reflection:} && 
\begin{cases}
\alpha_{14+i} \leftrightarrow \alpha_{14-i} \bmod 16 \\
\alpha_{19} \leftrightarrow \alpha_{16} \\
\alpha_{17} \leftrightarrow \alpha_{18} \\
\alpha_{20} \leftrightarrow \alpha_{21}
\end{cases} \\
&\text{Invariants:} && (10,8,0)_1, \qquad U\oplus E_8(2)
\end{aligned}
$$

#### Cusp $\eta_5 = 2e + 2f + \alpha$, $\alpha^2 = -8$ (divisibility $2$)

$$
\begin{aligned}
&\text{Transcendental lattice:} && (18,2,0)_1, \qquad U(2)\oplus E_8^2 \\
&\text{Automorphism:}\ 8\ \text{reflections:} && s_{\alpha_{2i+1}},\quad i=0,\ldots,7 \\
&\text{Invariants:} && (10,8,0)_1, \qquad U\oplus E_8(2)
\end{aligned}
$$

#### The main cusp correspondence


In this section, we record the cusp diagrams of the main moduli spaces of interest: $\fttz$ and $\fent$. 
The cusp diagram for $\fttz$ is shown below, which can be found in @AE22 or reconstructed using the mirror move algorithm.
The boundary lattices for $\fttz$ at its two 0-cusps are $(18,0,0)_1$ and $(18,2,0)_1$.
The cusps, their Coxeter diagrams, and the KSBA compactification $\ksbacpt{\fttz}$ were analyzed in detail in [@AE22, §10].
Consider the Enriques transcendental lattice

\begin{align*}
\ten \da U \oplus U(2) \oplus E_8(2)
.
.\end{align*}

The classification of $\gent$-orbits of primitive isotropic vectors in $\ten$ provides an enumeration of the 0-cusps in the Baily–Borel compactification of $\fent$.
We know by @Ste91 what the five 0-cusps $\eta_1,\cdots, \eta_5$ of $\bbcpt{\fent}$ are, as well as their stable reflection groups, Coxeter diagrams, and the associated 1-cusps. We collect below some of the lattice-theoretic calculations that will be relevant to showing that folding methods can be used to recover this data.
The following shows the cusp diagram for $\fent$, where we note that the mirror move algorithm does *not* apply, since it only determines cusps when $\Gamma$ is the full stable orthogonal group. We can instead appeal to @Ste91, who computed these cusps and their incidences in their entirety.
In the diagram below, we recapitulate these incidences, adding new information: recalling if $D$ is a $G$-space and $H\leq G$ is a subgroup, the chain of subgroups $1\injects H\injects G$ induces a chain of surjective morphisms $D\surjects \dmodgamma{D}{H}\surjects \dmodgamma{D}{G}$.
Thus there is a chain of maps $\halfpd{\ten}\to \fent\to \fen$, and we can consider the images of the cusps of $\fent$ in $\fen$ as well as their images in $\fttz$.

:::{#fig:fent-boundary-cusp-maps .figure}

\begin{tikzpicture}[cusp labels=eta]
% F_En (top), F_{En,2} (middle), F_{(2,2,0)} (bottom). The 0-cusp eta_1 of
% F_{En,2}, its 1-cusps, and their images in F_En are highlighted; the dashed
% arrows are cusp maps.
\pic (E) at (0.5,6.5) {object=bb-cusps/fen};
\pic (S) at (0,0) {object=bb-cusps/fen2};
\pic (K) at (0.6,-8) {object=bb-cusps/f220};
\begin{scope}[on background layer]
  \foreach \c in {12, 13, 14, 15} {\draw[cusp image] (S-1.center) -- (S-\c.center);}
  \draw[cusp image] (E-E10.center) -- (E-E8.center);
\end{scope}
\draw[cusp map] (S-1) -- (E-E10);
\draw[cusp map] (S-2) -- ([yshift=6mm]K-UE8E8.north);
\draw[cusp map] (S-5) -- ([yshift=6mm]K-U2E8E8.north);
\node[anchor=east] at (-1.3,6.5) {$F_{\En}$};
\node[anchor=east] at (-1.3,0) {$F_{\En, 2}$};
\node[anchor=east] at (-1.3,-8) {$F_{(2,2,0)}$};
\end{tikzpicture}
Mappings of boundary cusps under $\fen \from \fent \to \fttz$.

:::

We briefly describe the methods that go into finding these cusps, due to @Ste91.
The following result generalizes the Eichler transvection method:

:::{.theorem 
  title="Orbit Classification in $T = U \oplus \bdlattice{T}{\eta}$ [@Ste91, Cor. 3.3]" 
  #thm:orbit-classification-sterk
  }

Fix an even lattice $T$ with a splitting $T = U \oplus \bdlattice{T}{\eta}$ with $\bar T$ negative–definite and even.
Let $\eta_1,\;\eta_2\;\in T$ be primitive isotropic vectors satisfying

1. $\eta_1^2=\eta_2^2=k$;

2. $\div_T(\eta_1)=\div_T(\eta_2)=p>0$ (so $(\eta_i,T)=p\Bbb Z$);

3. $\eta_1\equiv \eta_2\pmod{pT}$.

Then there exists an isometry $\phi \in \OStab(T)$ such that $\phi(\eta_1) = \eta_2$. In particular, $\eta_1$ and $\eta_2$ lie in the same $\OStab(T)$-orbit.
:::

:::{.proof title="Sketch"} 
The idea is to let $\eta_i = a_i e + b_i e + c_i$ where $c_i\in \bdlattice{T}{\eta}$, and then put both $\eta_i$ into normal form.
Sterk shows that you can arrange for $\eta_1\cdot e = p$, so $a_1 = 0, b_1 = p$ by some $g\in \OStab(T)$, and that you can arrange for $\eta_2\cdot e =p$ simultaneously, so $a_2=0,v_2=p$.
Thus
$$
\eta_1 = pe + c_1, \eta_2 = pe + c_2, \qquad \eta_1 f = \eta_2 f = p
.$$
One then checks that
$$\eta_1 \equiv_{p T}\eta_2 \implies \eta_1 - \eta_2 \in pT \implies c_1 - c_2 = pc \in p\bdlattice{T}{\eta}$$ 
by canceling the now-identical $pf$ components, and writes 
$$\eta_1 - \eta_2 = pc \implies \eta_1 = \eta_2 + pc, \qquad c\in \bdlattice{T}{\eta}.$$
Constructing the Siegel-Eichler transvection
$$E_{f, c}(x) = x - (x, f)c + \left( (x, c) - {1\over 2}c^2 (x, f)\right)f,$$
one finds that

\begin{align*}
E_{f, c}(\eta_1) 
&\equiv_{\ZZ f} \eta_1 - (\eta_1, f)c  \\
&\equiv_{\ZZ f} (pe+ c_1) - pc  \\
&\equiv_{\ZZ f} (pe+ c_1) - (c_1 - c_2)  \\
&\equiv_{\ZZ f} pe + c_2  \\
&\equiv_{\ZZ f} \eta_2 \\
.\end{align*}
Writing $\eta_1 = \eta_2 + \lambda  f$, one concludes by checking that
$$
k = \eta_1^2 = E_{f, c}(\eta_1)^2 = (\eta_2 + \lambda f)^2 = \eta^2 + 2\lambda (\eta_2, f) + \lambda^2 f^2 = k + 2\lambda p
,$$
forcing $\lambda=0$ and $\eta_1 = \eta_2$.
:::

We then find that all divisibility one vectors are in the same orbit:

:::{.proposition
  title="[@Ste91, Lem. 4.2.1]"
}
If $\div_{\ten}(v)=1$, then $v \sim_{\gent } v_{1} \da e \in U$.
:::

:::{.proof}
We apply @thm:orbit-classification-sterk: since

- $v^{2}=e^{2}=0$,
- $\div_{\ten}(v)=\div_{\ten}(e)=1$, and
- $v \equiv e \bmod \ten$,

we have $v \sim_{\Orth^{*}\left(\ten\right)} e$ and thus $v \sim_{\gent} e$.
:::

The divisibility 2 vectors require a slightly finer analysis, but this quickly reduces to studying the large (but finite) discriminant group $A_{\ten}$:
[@Ste91, §4.2.2] first uses the fact that there is a decomposition
$$A_{\ten} = A\oplus B \da {1\over 2}U/U \oplus {1\over 2}E_8/E_8$$
and if $\div_{\ten}(\eta) = k \geq 2$ then $\eta/k \in \ten\dual$ induces a nontrivial class in $A_{\ten}$.
Any such class can be written as $g = a + b$ with $a\in A, b\in B$ and $q(g) = q_A(a) + q_B(b)$.
If $q(g) = 0\pmod{2\ZZ}$, there are exactly two possibilities:

1. $q_A(a) = q_B(b) = 0$, or
2. $q_A(a) = q_B(b) = 1$.

In the first case, one checks that the possibilities are 
$$a = 0, \quad {1\over 2}e', \quad {1\over 2}f', \qquad b = 0, \quad {1\over 2}\alpha, \quad \alpha\in E_8(2), \,\,\alpha^2 = -8,$$
using explicit computations for $U(2)$ and known facts about $E_8(2)$, and one can immediately rule out ${1\over 2}f'$ up to stable isometries.
In the second case, one has
$$a = {1\over 2}(e' + f'), \qquad b = {1\over 2}\omega,\quad \omega\in E_8(2),\,\, \omega^2 = -4.$$
This gives five possibilities, only four of which are new, which admit explicit lifts that are shown to be inequivalent under the action of $\Gamma_{\En, 2}$:
$$
A_T: \begin{cases}
  0 &\\
  {1\over 2}e' &\\
  {1\over 2}\alpha & (\alpha^2 = -8) \\
  {1\over 2}e' + {1\over 2}\alpha & (\alpha^2 = -8) \\
  {1\over 2}e' + {1\over 2}f' + {1\over 2}\omega & (\omega^2 = -4)
\end{cases}
\qquad\leadsto\,\,
T: \begin{cases}
  e &\\
  e' &\\
  2e + 2f + \alpha \quad &(\alpha^2 = -8) \\
  e' + 2f' + \alpha \quad &(\alpha^2 = -8) \\
  e' + f' + \omega \quad &(\omega^2 = -4)
\end{cases}
$$

Sterk then shows that under the full isometry group $\Orth(\ten)$, the four divisibility-two orbits collapse to a single orbit, and the divisibility-one orbit remains unique. Therefore, up to $O(\ten)$, there are exactly two orbits of primitive isotropic vectors, partially affirming the know cusp diagram of $\fen$ shown in the previous section.

#### Folded Coxeter Diagrams

We now describe—in precise terms following @AEGS25 -- how the Coxeter diagrams for the 0-cusps of $\fent$ are obtained by folding the Coxeter diagrams for the 0-cusps of the related quartic hyperelliptic K3 moduli $\fttz$ under the involution $I = -\Ien$.
Recall there are two $\Orth(\tdp)$-orbits of primitive isotropic vectors in $\tdp$, associated to the boundary lattices $(18,2,0)_1 = U(2)\oplus E_8^2$ and $(18,0,0)_1 = U\oplus E_8^2$. Each determines a *Coxeter diagram* encoding the walls of the fundamental chamber for the stable reflection group. The five 0-cusps of $\fent$ correspond to five distinct orbits of primitive isotropic vectors in $\ten$ (Sterk), and each is *realized as a folded image* of one of the K3 diagrams under the involution.

The fundamental fact is that the set of simple roots defining the faces of the Coxeter chamber are determined by @lem:which-roots-descend
The *folded chamber* for the reflection group in $\ten$ is the intersection
$$
\thecone{C}^I = \thecone{C} \intersect 
\bdlattice{T}{\eta, \RR}^{I = 1}
$$
where $\thecone{C}$ is the Coxeter chamber for $\tdp$, yielding a fundamental chamber for the reflection group in $\ten$ whose faces correspond to the roots described above.
Simple roots fixed by $I$ correspond to cases 1 and 2 above, and pass directly to the folded diagram as roots of the same norm.
Pairs of simple $(-2)$-roots swapped by the involution $I$ and orthogonal to their images, i.e. $I(\alpha) \in \alpha^{\perp}$, are "averaged" into a new $(-4)$-root wall of the folded diagram.
Moreover, every wall of the folded chamber, and hence every boundary divisor at each 0-cusp of $\fent$, arises by this procedure.
Maximal *parabolic subdiagrams* of the K3 diagrams invariant under $I$ (i.e., unions of nodes fixed or swapped under $I$ as above) yield, upon folding, the parabolic subdiagrams of the Enriques diagram, which can thus be used to find the 1-cusps and complete the full cusp diagram.

To summarize, the five Coxeter diagrams for the five 0-cusps of $\fent$ are obtained by explicit folding of the diagrams $G(18,2,0)$ and $G(18,0,0)$ of $\fttz$ under $I$.
This process precisely matches Sterk's list: each 0-cusp boundary lattice in $\ten$ is the fixed lattice under $I$ of the appropriate K3 boundary lattice for $\tdp$, and the combinatorics of simple roots and walls are gotten by descending them from $\tdp$ under the involution.
Moreover, each Coxeter diagram for each 0-cusp of $\fent$ arises from an explicit involution on a Coxeter diagram for $\fttz$, which we list below. In each diagram, a folding symmetry is defined by a combination of blue arrows and crossed out red nodes. 
Each folding involution is strictly speaking an element of $\Orth( \Phi(T) )$ for an appropriate lattice $T$, which decmoposes as the semidirect product of a reflection group and a subgroup of diagram symmetries, as described above. We can thus specify *some* isometries of $\Phi(T)$ by combining elements from each factor. In these diagrams, the blue decorations indicate isometries taken from the group of diagram symmetries, while red crossed-out nodes indicate elements taken from the Weyl group. Explicitly, in each case we have:

1. A counter-clockwise rotation by $\pi$,
2. A left-to-right reflection about the center,
3. A reflection about the line $y=x$, supposing the bottom-left node is at $(0, 0)$ in the plane,composed with a reflection in a single root,
4. A top-to-bottom reflection about the center, and
5. A composition of commuting reflections in 8 simple roots.

:::{#fig:fent-five-cusp-coverings .figure}

\begin{tikzpicture}
% First row: the five cusps. Second row: their K3 covers with the involution J_k.
\foreach \n/\x/\pos in {1/0/{(0,4)}, 3/17/{(17,1)}, 4/25.5/{(25.5,0)}, 5/34/{(34,4)}}
  \pic[root labels=none] at \pos {sterk cusp=\n};
\pic[root labels=none] at (8.4,2) {vinberg 10 8 0};
\foreach \n/\x in {1/0, 2/8.5, 3/17, 4/25.5, 5/34}
  \pic[root labels=index] at (\x,7) {sterk cusp cover=\n};
\foreach \x/\c/\name in {0/2/1, 8.5/3.6/2, 17/2.5/3, 25.5/2/4, 34/2/5} {
  \node[below] at (\x+\c,-0.7) {Cusp \name};
  \node[above] at (\x+\c,14) {Cover \name};
}
\end{tikzpicture}
The five 0-cusps $\eta_i$ in $\fent$, along with the five "covering" relations: each corresponds to one of the two 0-cusps of $\fttz$, along with an involution specific to each $\eta_i$.

:::
