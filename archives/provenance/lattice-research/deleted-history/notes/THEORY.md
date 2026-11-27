# Theory: Reflective Two-Elementary Lattices

All definitions and results are sourced from **V. Alexeev, "Reflective Hyperbolic
2-Elementary Lattices, K3 Surfaces and Hyperkahler Manifolds"**
[@alexeev2024reflective], with section references given for each entry.

* * *

## Definitions

### Built on top of (a graph)

A Coxeter diagram $\Gamma$ is **built on top of** a simple graph $H$ if it contains a
subdiagram of the main roots isomorphic to $H$, and the additional roots are defined in
terms of the main roots by specified rules.
For the two-elementary lattices treated in this paper, the main roots are the
$(-2)$-roots of divisibility 1, and if a main root $\alpha$ and an additional root
$\beta$ are connected, then $\alpha \cdot \beta = 2$.

— [@alexeev2024reflective, Def.
9.1.3]

### C-even lattice

A two-elementary lattice $S$ is **coeven** ($\delta = 0$) if the doubled dual $S^\dagger
:= S^*(2)$ is even.

— [@alexeev2024reflective, §9.2]

### C-odd lattice

A two-elementary lattice $S$ is **coodd** ($\delta = 1$) if the doubled dual $S^\dagger
:= S^*(2)$ is odd.

— [@alexeev2024reflective, §9.2]

### Coparity

The invariant $\delta \in \{0, 1\}$ in the Nikulin classification $(r, a, \delta)$ of a
two-elementary lattice.
It distinguishes coeven ($\delta = 0$) from coodd ($\delta = 1$) lattices.
A direct sum of two-elementary lattices is coeven iff every summand is coeven.

— [@alexeev2024reflective, §9.2]

### Coxeter diagram

For an even hyperbolic lattice $S$, the **Coxeter diagram** $\Gamma_r$ encodes the
angles between the roots orthogonal to the facets of the fundamental polyhedron $P_r$ of
the full reflection group $W_r(S)$. The diagram $\Gamma_2$ is defined analogously for
the $(-2)$-reflection group $W_2(S)$.

Vertices denote roots.
Edge types specify the angle $\theta$ between roots $\alpha_i, \alpha_j$:
- single line: $\theta = \pi/3$,
- double line: $\theta = \pi/4$,
- no line: $\theta = \pi/2$,
- bold line: hyperplanes meet at an infinite point of hyperbolic space,
- broken line: hyperplanes are skew.

For two-elementary lattices, short $(-2)$-roots are white vertices and long $(-4)$-roots
are black vertices.

— [@alexeev2024reflective, §9.2]

### Divisibility

The **divisibility** $\mathrm{div}(\alpha)$ of a vector $\alpha \in S$ is defined by
$\alpha \cdot S = \mathrm{div}(\alpha)\mathbb{Z}$.

— [@alexeev2024reflective, §9.2]

### Edge $n$-fold graph

Let $G$ be a graph and $n \geq 2$. The **edge $n$-fold graph** $G^{(n)}$ is obtained by
subdividing each edge of $G$ into $n$ edges and inserting $n-1$ intermediate vertices.
Thus $G^{(n)}$ has $n|E_G|$ edges and $|V_G| + (n-1)|E_G|$ vertices.
The vertices of $G^{(2)}$ are in natural bijection with the set of vertices and edges of
$G$.

— [@alexeev2024reflective, Def.
9.1.2]

### Elementary hyperbolic summands

The three indecomposable even hyperbolic two-elementary lattices that appear as direct
summands in any even hyperbolic two-elementary lattice:
- $\langle 2 \rangle$ with $(r,a,\delta) = (1,1,1)$,
- $U$ with $(r,a,\delta) = (2,0,0)$,
- $U(2)$ with $(r,a,\delta) = (2,2,0)$.

— [@alexeev2024reflective, §9.2]

### Even lattice

A lattice is **even** if $x^2$ is even for all $x \in S$.

— [@alexeev2024reflective, §9.2]

### Hyperbolic lattice

A lattice of signature $(1, r - 1)$ is called **hyperbolic**. (This convention follows
the algebraic geometry direction.)

— [@alexeev2024reflective, §9.2]

### Isotropic vector (primitive)

A vector $\nu \in S$ is **primitive isotropic** if $\nu^2 = 0$ and $\nu$ is not a
multiple of another lattice vector.

— [@alexeev2024reflective, §9.2]

### Lattice

A **lattice** is a free abelian group $S \simeq \mathbb{Z}^r$ equipped with a
nondegenerate $\mathbb{Z}$-valued symmetric bilinear form.

— [@alexeev2024reflective, §9.2]

### Main roots

For the two-elementary lattices treated in this paper, the **main roots** are the
$(-2)$-roots $\alpha$ of divisibility 1, i.e., satisfying $\alpha \cdot L = \mathbb{Z}$.

— [@alexeev2024reflective, Def.
9.1.3]

### Maximal parabolic subdiagram

A maximal parabolic subdiagram of a Coxeter diagram $\Gamma_r$ corresponds to an
$O(L)$-orbit of primitive isotropic vectors.
If a parabolic subdiagram $\Gamma \subset \Gamma_r$ corresponds to a vector $\nu \in S$
with $\nu^2 = 0$, then its image in $\nu^\perp/\nu$ spans an elliptic root system.

— [@alexeev2024reflective, §9.2]

### Nikulin classification

An indefinite even two-elementary lattice is uniquely determined by its signature and a
triple of integers $(r, a, \delta)$, where $r$ is the rank, $a$ is the
$\mathbb{Z}_2$-rank of the discriminant group, and $\delta \in \{0, 1\}$ is the coparity
invariant.

— [@alexeev2024reflective, §9.2; @nikulin1979integral]

### Parabolic diagram

A **parabolic diagram** is an affine Coxeter diagram of type $\widetilde{A}_n$,
$\widetilde{D}_n$, $\widetilde{E}_n$, $\widetilde{B}_n$, $\widetilde{C}_n$, or
$\widetilde{F}_4$. For two-elementary lattices, these can consist of all short roots or
all long roots; the long-root versions are denoted with a $(2)$ suffix, e.g.,
$\widetilde{A}_n(2)$.

— [@alexeev2024reflective, §9.2]

### Reflective lattice

A lattice is **reflective** if the full reflection group $W_r(S)$ (generated by
reflections in all roots) has finite index in $O(S)$.

— [@alexeev2024reflective, §9.2]

### Reflection

The **reflection** in a vector $\alpha \in S$ is the linear transformation $$w_\alpha(v)
= v - 2\frac{v \cdot \alpha}{\alpha^2}\alpha.$$

— [@alexeev2024reflective, §9.2]

### Reflection group

- $W_2(S)$: the group generated by reflections in $(-2)$-vectors.
- $W_r(S)$: the group generated by reflections in all roots (both $(-2)$- and
  $(-4)$-roots).

Both are normal subgroups of $O(S)$ and of its index-2 subgroup $O^+(S)$ preserving the
light cone.

— [@alexeev2024reflective, §9.2]

### Root

A **root** is a vector $\alpha \in S$ such that $\alpha^2 < 0$ and $w_\alpha(S) = S$. In
an even two-elementary lattice, the roots are the $(-2)$-vectors and the $(-4)$-vectors
of divisibility 2.

— [@alexeev2024reflective, §9.2]

### Root lattice notation

- $A_n$, $D_n$, $E_n$: standard negative-definite root lattices generated by
  $(-2)$-roots.
- $U = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$: the hyperbolic plane.
- $H(n)$: the lattice $H$ with product scaled by $n$.
- $B_n(2)$, $C_n$, $F_4$: root lattices for $(-2)$-roots; as $(-2)$-root lattices these
  are $A_1^n$, $D_n$, and $D_4$ respectively.

— [@alexeev2024reflective, §9.2]

### Two-elementary lattice

A lattice is **two-elementary** if its discriminant group $A_S := S^*/S \simeq
\mathbb{Z}_2^a$ for some $a \geq 0$, where $S^* \subset S \otimes \mathbb{Q}$ is the
dual group.

— [@alexeev2024reflective, §9.2]

### Two-reflective lattice

A lattice is **two-reflective** if the $(-2)$-reflection group $W_2(S)$ has finite index
in $O(S)$.

— [@alexeev2024reflective, §9.2]

* * *

## Results

### Classification of isotropic vectors

Primitive isotropic vectors $\nu \in S$ with $\nu^2 = 0$ fall into three types.
Denoting $\overline{S} = \nu^\perp/\nu$:

1. **Odd**: $S = U \oplus \overline{S}$, $a_{\overline{S}} = a_S$,
   $\delta_{\overline{S}} = \delta_S$.
2. **Even ordinary**: $S = U(2) \oplus \overline{S}$, $a_{\overline{S}} = a_S - 2$,
   $\delta_{\overline{S}} = \delta_S$.
3. **Even characteristic**: $S = I_{1,1}(2) \oplus \overline{S}$, $a_{\overline{S}} =
   a_S - 2$, $\delta_S = 1$, and $\delta_{\overline{S}} = 0$.

— [@alexeev2024reflective, §9.2; @aegs2023compact, Prop.
5.5]

### Coxeter diagrams built on $K_n^{(2)}$

For $n = 3, 4, 5, 6$, the Coxeter diagram $\Gamma_r$ of the even two-elementary lattice
$(10+n, 12-n, 1)$ is built on top of $K_n^{(2)}$. The diagram for $(18,4,0)$ is built on
top of $K_{4,4}^{(2)}$. The diagram for $(14,8,0)$ is built on top of $D_4^{(2)}$. In
all cases, $\operatorname{Aut}\Gamma_r = \operatorname{Aut}G$ and $O^+(S) =
\operatorname{Aut}G \ltimes W_r$.

— [@alexeev2024reflective, Thm.
9.1.4]

### Duality for coeven lattices

If $S = (r, a, 0)$ is coeven, then $S^\dagger = S^*(2) = (r, r - a, 0)$ is also coeven.
Their Coxeter diagrams are dual, with $(-2)$ and $(-4)$ roots interchanged, and there is
a bijection between their maximal parabolic subdiagrams.

— [@alexeev2024reflective, §9.3]

### K3 automorphism exact sequence

For a two-elementary K3 lattice $S \neq (10,10,0)$, with Coxeter diagram $\Gamma_r$ and
K3 surface $X$ with $S_X = S$: $$0 \to \langle \iota \rangle \times
\operatorname{Aut}'(Y, B) \to \operatorname{Aut}X \to \operatorname{Sym}\Gamma_r \ltimes
W(\Gamma_4) \to 0,$$ where $\iota$ is the canonical nonsymplectic involution, $Y =
X/\iota$, $B$ is the branch divisor, and $\Gamma_4 \subset \Gamma_r$ is the subdiagram
of $(-4)$-roots.

— [@alexeev2024reflective, Lemma 9.4.1]

### Nonreflective lattices on the $r + a = 22$ line

The two-elementary lattices $(17,5,1)$, $(18,4,1)$, and $(19,3,1)$ are not reflective.
All other even two-elementary lattices on the line $r + a = 22$ are reflective.

— [@alexeev2024reflective, Thm.
9.1.1]

### $(-4)$-subdiagrams for $r + a = 22$

| Lattice | $\operatorname{Aut}\Gamma_r$ | $\Gamma_4$ |
| --- | --- | --- |
| $(11,11,1)$ | 1 | $T_{2,3,7}$ |
| $(12,10,1)$ | 1 | $T_{2,4,6} \sqcup A_1$ |
| $(13,9,1)$ | $S_3$ | $T_{4,4,4}$ |
| $(14,8,1)$ | $S_4$ | 10-vertex trivalent tree with 6 ends |
| $(15,7,1)$ | $S_5$ | Petersen graph |
| $(16,6,1)$ | $S_6$ | Diagram with $10 + 15$ vertices |
| $(18,4,0)$ | $S_2 \ltimes (S_4 \times S_4)$ | Diagram with 24 vertices |
| $(20,2,1)$ | $S_5$ | $K_5$ with bold edges |

Here $T_{p,q,r}$ denotes a tree with legs of lengths $p, q, r$.

— [@alexeev2024reflective, Table 9.1]

### Maximal parabolic subdiagram counts

| Lattice | Total parabolics | Modulo $\operatorname{Aut}\Gamma_r$ |
| --- | --- | --- |
| $(11,11,1)$ | 2 | 2 |
| $(12,10,1)$ | 5 | 5 |
| $(13,9,1)$ | 22 | 7 |
| $(14,8,0)$ | 11 | 5 |
| $(14,8,1)$ | 127 | 15 |
| $(15,7,1)$ | 1027 | 20 |
| $(16,6,1)$ | 8917 | 28 |
| $(18,4,0)$ | 5244 | 17 |
| $(20,2,1)$ | 581 | 13 |
| $(13,11,1)$ | 9 | 5 |
| $(14,10,1)$ | 69 | 12 |
| $(15,9,1)$ | 2114 | 20 |
| $(18,6,0)$ | 90,897,634 | 28 |
| $(22,2,0)$ | 1,095,990 | 18 |
| $(14,12,1)$ | 16 | 9 |
| $(15,11,1)$ | 522 | 16 |
| $(15,13,1)$ | 46 | 10 |
| $(16,14,1)$ | 115 | 14 |

— [@alexeev2024reflective, §9.3]

### Vinberg's algorithm

The Coxeter diagrams $\Gamma_2$ and $\Gamma_r$ are computed via Vinberg's algorithm,
which terminates in finitely many steps for reflective lattices.
Each lattice is written as $U \oplus \Lambda$ or $U(2) \oplus \Lambda$ for a root
lattice $\Lambda$, with a control vector $\nu_0$ chosen in the first summand ($\nu_0^2 =
2$ for $U$, $\nu_0^2 = 4$ for $U(2)$). Completeness is verified by confirming that the
cones defined by the roots of $\Gamma_r$ lie entirely in $\overline{C}$.

— [@alexeev2024reflective, §9.3; @vinberg1972units; @vinberg1975arithmetical]
