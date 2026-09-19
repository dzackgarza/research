### DLT Models

This section gives a precise structural and combinatorial description of divisor models (for degenerations of K3 pairs) and half-divisor models (for Enriques quotients), connecting KSBA limits explicitly to integral-affine data on dual complexes.
Let $\pi: \mcx \to C$ be a degeneration of complex surfaces with $\mcx_0$ $\mcx_0$. The **dual complex** $\Gamma(\mcx_0)$ encodes the topology of $\mcx_0$: each vertex of $\Gamma(\mcx_0)$ corresponds to an irreducible component $V_i$, each edge to a double curve $D_{ij} = V_i \cap V_j$. When $\mcx_0$ has normal crossings, $\Gamma(\mcx_0)$ is a finite graph.
Given a Cartier divisor $\mcr \subset \mcx$ disjoint from the singular strata of $\mcx_0$ (i.e., $\mcr$ does not meet points where two or more components meet), the combinatorial geometry of $(\mcx_0, \mcr_0)$ is encoded by an **integral-affine divisor** $R_{\IA} \subset \Gamma(\mcx_0)$. This means:

- Each edge of $\Gamma(\mcx_0)$ (corresponding to a double curve $D_{ij}$) is assigned an integer weight $n_{ij}$, expressing the degree of intersection of $\mcr_0$ with $D_{ij}$.

- To each vertex $v_i$ (component $V_i$) one assigns a line bundle $L_i \in \Pic(V_i)$ so that, for any edge $v_{ij}$, $\deg(L_i|_{D_{ij}}) = n_{ij}$. The weighting must be compatible on edges and satisfy global compatibility conditions.

These weights obey a **balancing condition** at every vertex $v_i$. For a toric vertex, resp. a non-toric vertex arising from an internal blowup in the direction $\vec{e}$, we have 


\begin{align*}
\sum_j n_{ij} \vec{e}_{ij} = 0, \qquad 
\sum_j n_{ij} \vec{e}_{ij} \in \ZZ\,\vec{e}
.\end{align*}

where $\vec{e}_{ij}$ is the primitive integral direction associated to the corresponding edge. 
These constraints ensure that the line bundles patch together along double curves and that the data collectively define a global Cartier divisor structure in the smoothing.

:::{.definition title="{Divisor Model}" #def:divisor-model}
A **divisor model** for a degeneration $\pi: \mcx \to C$ of K3 (or Enriques) surfaces is a degeneration of pairs $(\mcx, \mcr) \to C$ such that:

- $\mcr$ is a Cartier divisor, with $\mcr_t = \mcr \cap \mcx_t$ effective for all $t \in C$,
- For $t \neq 0$, $\mcr_t$ is semiample,
- $\mcr$ does not meet the singular strata of $\mcx_0$ (i.e., is disjoint from double/triple intersections).
:::

Given a divisor model, the isomorphism class of $\OO_{\mcx_0}(\mcr_0)$ is encoded by its corresponding integral-affine divisor $R_{\IA}$ on $\Gamma(\mcx_0)$. The dual complex, together with $R_{\IA}$, captures all line bundle glueing data and allows for explicit calculation of limit objects.

:::{.proposition title="{Classification via Integral-Affine Data}" #prop:classification-ia-data}
Given a fixed Picard–Lefschetz monodromy invariant $\lambda$, the combinatorial type $(\Gamma(\mcx_0), R_{\IA})$—that is, the dual complex with its weighted, balanced subgraph—uniquely determines the KSBA stable limit $(\overline{\mcx}_0, \epsilon \overline{\mcr}_0)$. Furthermore, this combinatorial type is locally constant in families with fixed Picard–Lefschetz form.
:::

:::{.proposition title="{Semitoroidal Compactification via Recognizable Divisors}" #prop:semitoroidal-recognizable}
If $R$ is a recognizable divisor (such as the fixed locus of a nonsymplectic involution), then there exists a unique semifan $\semifan{F}_R$ whose semitoroidal compactification normalizes the KSBA compactification of the relevant moduli space $\fent$[6, Sec. 5C].
:::

:::{.theorem title="{Explicit Construction and Type Determination}" #thm:explicit-construction}
Given a polarized integral-affine structure $(B(\ell), R_{\IA})$ (with $\ell = (\lambda \cdot \alpha_i)_{i \in G}$), and an appropriate triangulation, one obtains

\begin{align*}
(B(\ell), R_{\IA}) = (\Gamma(\mcx_0), \Gamma(\mcr_0))
.\end{align*}

as the dual complex of the $\mcx_0$ of a divisor model with monodromy invariant $\lambda$.
:::

:::{.definition title="{Half-Divisor Model}" #def:half-divisor-model}
Suppose $(\mcx, \mcr) \to (C,0)$ is a divisor model for a family of K3 surfaces admitting an involution $\ien$ that preserves $\mcr$. The **half-divisor model** is the quotient

\begin{align*}
(\mcz, \mcr_\mcz) := (\mcx, \mcr)/\ien.
.\end{align*}

These models realize degenerations of Enriques pairs as quotients of K3 divisor models, and in generic settings, the quotient inherits slc singularities, and the divisor structure matches the normalization of the image of $\mcr$[2, Prop. 4.5].
:::

:::{.proposition title="{Geometric Types and Boundary Strata}" #prop:geometric-types}
Let $(\mcz, \mcr_{\mcz}) \to (C,0)$ be a half-divisor model for $\fent$ as constructed above. Then the following properties hold:

- The fibers of $\mcz$ have semi-log canonical (slc) singularities.
  
- The divisor $K_{\mcz} + \epsilon \mcr_{\mcz}$ is relatively big and nef over $C$.

- The divisor $\mcr_{\mcz}$ contains no log canonical centers.

More precisely:

- In the case of Type $\III$ degenerations at cusp $1$, the dual complex $\Gamma(\mcz_0)$ is homeomorphic to $\RP^2$; each irreducible component $V_i$ of the $\mcx_0$ $\mcz_0$ is, after normalization, isomorphic to one of the preimage components of $\mcx_0$.

- For Type $\III$ degenerations at cusps $2$–$5$, the dual complex $\Gamma(\mcz_0)$ is homeomorphic to $\DD^2$. If a component $V_i$ lifts to two distinct components of $\mcx_0$, the normalized copies are isomorphic; if it arises from a single irreducible component, the involution $\ienzero$ acts on $V_i$ with precisely four fixed points.

- In the case of Type $\mathrm{II}$ degenerations, $\Gamma(\mcz_0)$ is a segment, and the quotient is described by the action of $\ienzero$ as detailed in [2, Proposition 4.5].
:::

:::{.proof}
See detailed analyses in [@AEGS25, Prop. 4.5], which classify Enriques degenerations by their dual complex and describe the induced slc structure and divisor support in every case.
:::

:::{.corollary title="{Computability of the KSBA Stable Limit}" #cor:ksba-stable-limit}
Given a degeneration $(\mcz^*, \epsilon \mcr_{\mcz}^*) \to C^*$, the KSBA-stable limit is

\begin{align*}
\Proj_C \bigoplus_{n \geq 0} H^0(\mcz, n \mcr_{\mcz}),
.\end{align*}

where the right-hand side is computed from the data of the half-divisor model $(\mcz, \mcr_{\mcz}) \to (C, 0)$.
:::

:::{.remark}
The quotient $\Gamma(\mcz_0) = \Gamma(\mcx_0) / \iota_{\En, \IA}$ always inherits a natural integral-affine structure, encoding both the combinatorics and divisor data of the degeneration[2, Prop. 4.5]. In Type $\III$, certain boundary components are the images of the "Enriques equator" and are characterized by four $A_1$ singularities.
:::

:::{.remark}
For general monodromy invariant $\lambda$, half-divisor models exist only generically: the involution $\ien$ may be only birational on $\mcx_0$s. After contracting exceptional loci to resolve indeterminacies, one obtains only a dlt pair. This supports the broader philosophy (see , ) that dlt models, rather than strictly semistable ones, are the correct analogues of Kulikov models for $K$-trivial surface degenerations.
:::