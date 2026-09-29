### DLT Models

This section recalls divisor models for degenerations of K3 pairs and half-divisor models for their Enriques quotients, and relates them to the integral-affine data used in @AEGS25.
Let $\pi: \mcx \to C$ be a degeneration of complex surfaces with simple normal-crossings central fiber $\mcx_0$. The **dual complex** $\Gamma(\mcx_0)$ has a vertex for each irreducible component, an edge for each double curve, and a $2$-simplex for each triple point; for a surface degeneration it is therefore in general a finite $2$-dimensional complex, not merely a graph.

For a divisor model $(\mcx,\mcr)\to(C,0)$, the flat-limit divisor $\mcr_0$ is encoded on the dual complex by the **integral-affine polarization** $R_{\IA}=\Gamma(\mcr_0)$, a weighted balanced graph which encodes the line bundle $\OO_{\mcx_0}(\mcr_0)$ [@AEGS25, §4.2]. The condition on a divisor model is that $\mcr$ **contains no stratum** of the fibers; it is not required to be disjoint from the double locus. Indeed, the integral-affine polarization may meet edges of $\Gamma(\mcx_0)$ and records the corresponding divisor data.

:::{.definition title="Divisor Model" #def:divisor-model}
A **divisor model** for a degeneration of polarized K3 surfaces is a Kulikov or quasipolarized nef model $(\mcx,\mcl)\to(C,0)$ together with a relatively big and nef effective divisor $\mcr\in|\mcl|$ extending the divisor on the general fiber, such that $\mcr$ contains no stratum of any fiber [@AEGS25, §4.2].
:::

Given a divisor model, the integral-affine polarization records the line bundle on the central fiber. It does not, by itself, assert that the isomorphism class of the algebraic stable pair is determined solely by the combinatorial dual complex; the KSBA model is obtained from the divisor model by the relative Proj construction below.

:::{.proposition title="Semitoroidal Compactification via Recognizable Divisors" #prop:semitoroidal-recognizable}
If $R$ is a recognizable divisor on a moduli space $F_S$ of lattice-polarized K3 surfaces, then the normalization of the associated KSBA compactification is a semitoroidal compactification for the uniquely determined semifan $\semifan{F}_R$ [@AE23, Thm. 9.1].
:::

:::{.theorem title="Polarized IAS data and divisor models [@AEGS25, Thm. 4.4]" #thm:explicit-construction}
Let $(B(\ell), R_{\IA})$ be one of the polarized integral-affine spheres constructed from $\ell = (\lambda \cdot \alpha_i)_{i \in G}$. Upon triangulating it into lattice simplices, one obtains

\begin{align*}
(B(\ell), R_{\IA}) = (\Gamma(\mcx_0), \Gamma(\mcr_0))
.\end{align*}

as the dual complex of the central fiber of a divisor model $(\mcx,\mcr)\to(C,0)$ with monodromy invariant $\lambda$ [@AEGS25, Thm. 4.4].
:::

:::{.definition title="Half-Divisor Model" #def:half-divisor-model}
Suppose $(\mcx, \mcr) \to (C,0)$ is a divisor model of Enriques K3 surfaces for which the Enriques involution $\ien$ is regular on $\mcx$ and preserves $\mcr$. The **half-divisor model** is the quotient

\begin{align*}
(\mcz, \mcr_\mcz) := (\mcx, \mcr)/\ien
.\end{align*}

as in [@AEGS25, Def. 4.7].
:::

:::{.proposition title="Geometric Types and Boundary Strata" #prop:geometric-types}
Let $(\mcz, \mcr_{\mcz}) \to (C,0)$ be a half-divisor model for $\fent$ as constructed above. Then the following properties hold:

- The fibers of $\mcz$ have semi-log canonical (slc) singularities.

- The divisor $K_{\mcz} + \epsilon \mcr_{\mcz}$ is relatively big and nef over $C$.

- The divisor $\mcr_{\mcz}$ contains no log canonical centers.

More precisely:

- In the case of Type $\III$ degenerations at cusp $1$, the dual complex $\Gamma(\mcz_0)$ is homeomorphic to $\RP^2$; each irreducible component $V_i$ of the $\mcx_0$ $\mcz_0$ is, after normalization, isomorphic to one of the preimage components of $\mcx_0$.

- For Type $\III$ degenerations at cusps $2$–$5$, the dual complex $\Gamma(\mcz_0)$ is homeomorphic to $\DD^2$. If a component $V_i$ lifts to two distinct components of $\mcx_0$, the normalized copies are isomorphic; if it arises from a single irreducible component, the involution $\ienzero$ acts on $V_i$ with precisely four fixed points.

- In the case of Type $\mathrm{II}$ degenerations, $\Gamma(\mcz_0)$ is a segment, and the action of $\ienzero$ on the components and double curves is as described in [@AEGS25, Prop. 4.8].
:::

:::{.proof}
This is [@AEGS25, Prop. 4.8]. Proposition 4.5 supplies the folding symmetry on the polarized integral-affine sphere; Proposition 4.8 analyzes the resulting half-divisor models and their quotients.
:::

:::{.corollary title="Computability of the KSBA Stable Limit" #cor:ksba-stable-limit}
Given a degeneration $(\mcz^*, \epsilon \mcr_{\mcz}^*) \to C^*$, the KSBA-stable limit is

\begin{align*}
\Proj_C \bigoplus_{n \geq 0} H^0(\mcz, n \mcr_{\mcz}),
.\end{align*}

where the right-hand side is computed from the data of the half-divisor model $(\mcz, \mcr_{\mcz}) \to (C, 0)$. This is [@AEGS25, Cor. 4.9].
:::

:::{.remark title="Integral-affine structure on the quotient dual complex"}
The quotient $\Gamma(\mcz_0) = \Gamma(\mcx_0) / \iota_{\En, \IA}$ inherits a natural integral-affine structure, with boundary in the $\DD^2$ case [@AEGS25, Rem. 4.10]. In that case the boundary components are exactly the images of the Enriques equator; they are the singular components of $\mcz_0$, each carrying four $A_1$ singularities.
:::

:::{.remark title="DLT models beyond generic half-divisor models"}
For a fixed Picard--Lefschetz transform $\lambda$, the construction above proves existence of a half-divisor model only for generic degenerations: in general the Enriques involution on the divisor model may be birational. Contracting the ADE configurations in the components which form its indeterminacy locus makes the involution regular, but the quotient pair is then only dlt. This is precisely the issue recorded in [@AEGS25, Rem. 4.11].
:::
