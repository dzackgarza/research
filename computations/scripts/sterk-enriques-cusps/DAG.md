# Dependency DAG: Sterk's boundary complex

The target is the combinatorial structure of the boundary of the Baily–Borel
compactification of $\Omega_-/\Gamma$: five zero-dimensional strata, nine
one-dimensional strata, with the incidence relation of Sterk (3.4).
Equivalently, $\Gamma \backslash \mathcal{T}(G)$ for $G = \mathrm{O}(L_-\otimes\mathbb{Q})$,
whose Tits building over $\mathbb{Q}$ is one-dimensional because $G$ has
$\mathbb{Q}$-rank 2.

Source: H. Sterk, *Compactifications of the period space of Enriques surfaces*
(Nijmegen thesis, 1988), Chap. 2; published as Math. Z. 207 (1991) with §3.2,
§3.3 renumbered §4.2, §4.3.  Zotero `Ste95a` / `Ste91` / `Ste88a`.

Node status: **S** a numbered statement in Sterk; **U** an unnumbered
computation in Sterk carried by a figure; **X** external, cited to another
source; **M** requires substrate absent from Mathlib at the pinned revision.

## Stratum A — the arithmetic of $L_- = U \oplus U(2) \oplus E_8(-2)$

| Node | Statement | Depends on |
| --- | --- | --- |
| A0 | `S` (2.7), (2.8) — definition of $\Gamma$ and of the special sets | — |
| A1 | `S` 2.10 — $\Gamma$ is exactly the isometries whose induced map on $L_-^*/L_-$ respects the decomposition $(U(2)^*/U(2)) \oplus (E_8(-2)^*/E_8(-2))$ | A0 |
| A2 | `S` 2.13 — $G = O(L_-)$ | A1 |
| A3 | `X` Nikulin 1.13.2 — $L_-$ is determined up to isometry by its signature $(2,10)$ and its discriminant form | — |
| A4 | `S` 2.16 — for $\Lambda = U \oplus U(2)$ and $v$ primitive: $v \sim_{O(\Lambda)} e + kf$ if $(v,v) = 2k$, $v \notin 2\Lambda^*$; $v \sim e' + kf'$ if $(v,v) = 4k$, $v \in 2\Lambda^*$ | — |
| A5 | `S` 2.17 — the same under $O^*(\Lambda)$, with the extra branch $ke' + f'$ | A4 |
| A6 | `S` 2.18 — for $N = \Lambda \oplus P$, $P$ even nondegenerate: primitive $v, w$ with equal norm, equal divisor $p\mathbb{Z}$, and $v \equiv w \bmod pN$ are $O^*(N)$-equivalent | A5 |
| A7 | `S` 2.19 — $S_-$ is a single $\Gamma$-orbit | A1, A6 |

## Stratum B — the isotropic sublattices

| Node | Statement | Depends on |
| --- | --- | --- |
| B1 | `S` 3.2.1 — a primitive isotropic $v$ with $(v, L_-) = \mathbb{Z}$ satisfies $v \sim_\Gamma e$ | A6 |
| B2 | `S` 3.2.2 — otherwise $(v, L_-) = 2\mathbb{Z}$, and $\tfrac12 v$ is a nontrivial isotropic element of $L_-^*/L_-$; the isotropic elements of the discriminant form, modulo $\Gamma_q$, are the four listed | A1 |
| B3 | `S` 3.2.3 — every primitive isotropic vector is $\Gamma$-equivalent to exactly one of $e$, $e'$, $e'+f'+\omega$, $e'+2f'+\alpha$, $2e+2f+\alpha$ ($\alpha^2 = -8$, $\omega^2 = -4$ in $E_8(-2)$); hence $\lvert I_1(L_-)/\Gamma \rvert = 5$ | B1, B2, A6 |
| B4 | `S` 3.3.4 — $v^\perp/\mathbb{Z}v \cong U \oplus E_8(-2)$ for $v \ne e$, and $e^\perp/\mathbb{Z}e \cong U(2) \oplus E_8(-2)$ | B3, A6 |
| B5 | `S` 3.3.14 — $U(2) \oplus E_8(-1)$ is the largest even sublattice of $K$ | — |
| B6 | `S` 3.3.15 — every $g \in O(K(2))$ extends to an isometry of $\Lambda$ | B5 |
| B7 | `S` 3.3.16 — $K(2)$ is the unique rank-10 sublattice $\tilde\Lambda \subseteq \Lambda$ with $\tilde\Lambda^* = \tfrac12\tilde\Lambda$ and $\tfrac12\tilde\Lambda(2)$ odd | B5 |
| B8 | `U` 3.3.13 — the symmetries of each diagram lift to $\Gamma_v$ | B6, B7 |

## Stratum C — Vinberg's algorithm and the five diagrams

| Node | Statement | Depends on |
| --- | --- | --- |
| C1 | `X` `M` Vinberg 1975 — for $N$ of signature $(1,n)$ and $G \le O_C(N)$ of finite index, the fundamental polyhedron of $W(G)$ and its Coxeter diagram $\Sigma(G)$; the vertices at infinity correspond to the parabolic subdiagrams of rank $n-1$ | — |
| C2 | `X` Vinberg 1983 (1.9) — the isotropic vector read off a parabolic subdiagram | C1 |
| C3 | `U` 3.3.5–3.3.7 — for $v = e$: the twelve roots, their Gram matrix, and the nine maximal parabolic subdiagrams in four types $\tilde E_8$, $\tilde D_8$, $\tilde E_7 \oplus \tilde A_1$, $\tilde A_7 \oplus \tilde A_1$ | B4, C1 |
| C4 | `U` 3.3.8–3.3.9 — for $v = e'$: ten roots, two maximal parabolic subdiagrams $\tilde E_8$, $\tilde B_8$ | B4, C1 |
| C5 | `U` 3.3.10 — for $v = e' + f' + \bar\alpha_8$: twelve roots, four maximal parabolic subdiagrams | B4, C1 |
| C6 | `U` 3.3.11 — for $v = 2e' + f' + \bar\alpha_1$: eleven roots, five maximal parabolic subdiagrams in four types $\tilde B_4 \oplus \tilde B_4$, $\tilde D_8$, $\tilde B_8$, $\tilde C_8$ | B4, C1 |
| C7 | `U` 3.3.12 — for $v = 2e + 2f + \bar\alpha_1$: the re-split basis, the diagram, and its maximal parabolic subdiagrams in four types $\tilde A_7 \oplus \tilde A_1$, $\tilde C_8$, $\tilde C_6 \oplus \tilde C_2$, $\tilde C_4 \oplus \tilde C_4$ | B4, C1 |
| C8 | `U` 3.3.9–3.3.12 — the cross-identifications: which labels in one diagram name the same $\Gamma$-class of planes as a label in another | C3–C7, B8 |
| C9 | `S` 3.3.17 — the labelling by parabolic subdiagram depends on the vertex, not on the plane: $\tilde B$ and $\tilde C$ diagrams can name one class, because $(G_v)_w$ and $(G_w)_v$ need not be isomorphic | C8 |
| C10 | `S` 3.3.18 — a plane's type is the pair of $\Gamma$-types of the isotropic vectors it contains | C8 |
| C11 | — $\lvert I_2(L_-)/\Gamma \rvert = 9$, separated by $F^\perp/F$ against Scattone's nine possibilities | C8, C10, X: Scattone 1984 5.6.10, §6, p. 100 |
| C12 | `S` 3.4 — the incidence relation between the five classes of lines and the nine of planes | B3, C11 |

C3–C7 are reconstructed and checked in `sterk_cusp_diagrams.sage`: the Gram
matrices are rebuilt from the root vectors and reproduce the printed diagrams.
C3–C6 agree with Sterk's labels; **C7 does not yet** — see the commit message of
`18213910`.  C9 is why a formalization must state the labelling on flags
$(v, F)$, not on $F$.

## Stratum D — from sublattices to boundary components

| Node | Statement | Depends on |
| --- | --- | --- |
| D1 | `X` `M` for a $\mathbb{Q}$-algebraic group $G$, the Tits building $\mathcal{T}(G)$: the flag complex of proper parabolic $\mathbb{Q}$-subgroups | — |
| D2 | `X` `M` for $G = \mathrm{O}(L_-\otimes\mathbb{Q})$ of signature $(2,10)$: the maximal parabolic $\mathbb{Q}$-subgroups are the stabilizers of the isotropic $\mathbb{Q}$-subspaces, which have dimension 1 or 2; so $\mathcal{T}(G)$ is the bipartite incidence graph of isotropic lines and planes | D1 |
| D3 | `X` `M` Baily–Borel — the rational boundary components of a type IV domain $D$ correspond to the maximal parabolic $\mathbb{Q}$-subgroups, zero-dimensional to isotropic lines and one-dimensional to isotropic planes | D1, D2 |
| D4 | `X` `M` Baily–Borel — the boundary of $D/\Gamma$ is $\Gamma\backslash$(rational boundary components), with closure relations induced by incidence | D3 |
| D5 | `S` 3.3.19, 3.3.20 — $\Gamma(E) \cap SL(E) \cong \Gamma^1(2)$, so each one-dimensional component is $\mathbb{H}/\Gamma^1(2)$; no identification among its cusps occurs | D4, C11, B3 |

## Goal

| Node | Statement | Depends on |
| --- | --- | --- |
| G | the boundary complex of the Baily–Borel compactification of $\Omega_-/\Gamma$ — equivalently $\Gamma\backslash\mathcal{T}(G)$ — is the explicit finite graph with five vertices of one type, nine of the other, and the edges of 3.4 | B3, C11, C12, D4 |

## Stratum F — the foundations the other strata stand on

The nodes above are the paper's own steps.  Several of them are not leaves: they
rest on theory that the pinned Mathlib does not have, and that no node of A–D
states.  Substrate checked against the pinned revision `0df444a3`.

| Node | What it is | Needed by | Mathlib substrate |
| --- | --- | --- | --- |
| F1 | even lattices, the dual $L^*$, the discriminant group $L^*/L$, and the discriminant **form** $q : L^*/L \to \mathbb{Q}/2\mathbb{Z}$ with its orthogonal decomposition | **A0, A1** — the definition of $\Gamma$ — and C11, A3 | `ZLattice` and `dualSubmodule` exist; the discriminant form does not |
| F2 | $O^*(N)$: the isometries Sterk distinguishes from $O(N)$, by spinor norm / preserved component of the positive cone | A5, A6 (2.17, 2.18), B1 | absent — no spinor norm |
| F3 | affine Coxeter and Dynkin diagrams: the extended types, subdiagrams, parabolic subdiagrams and their rank | C1, and the explicit half of C3–C7 | finite Cartan matrices only (`Matrix/Cartan.lean`, through $E_8$); no affine types |
| F4 | hyperbolic reflection groups: Lobachevskii space, the fundamental polyhedron of $W(G)$, Vinberg's algorithm and its completeness | C1, C2 | absent |
| F5 | genus theory of even lattices — $p$-adic invariants — enough to state Scattone's nine possibilities for $F^\perp/F$ | C11 | absent |
| F6 | reductive groups over $\mathbb{Q}$, parabolic $\mathbb{Q}$-subgroups, spherical buildings; hermitian symmetric domains of type IV; the Baily–Borel construction and its topology | D1–D4 | absent |
| F7 | the upper half plane and congruence subgroups, for $\mathbb{H}/\Gamma^1(2)$ | D5 | present — `UpperHalfPlane`, `Gamma0`/`Gamma1` |

**Every row of this table is a subject, not a statement, and so violates
`FSC-06`.**  They are placeholders standing where sub-graphs belong, and until
each is decomposed the graph understates the work by an unknown amount — the
same defect as the "external, cited" leaves that `FDC-03` was written about,
one level down.  Two are worked below; the rest are outstanding.

### F5, rewritten from Scattone

`C11` needs: for $F \in I_2(L_4)$, the isomorphism type of $F^\perp/F$ is one of
nine.  Sterk states the list (thesis p. 59, citing Scattone 5.6.10 and §6, and
his p. 100):

$$E_8(-1)^{\oplus 2}\oplus\langle-4\rangle,\quad D_{16}(-1)\oplus\langle-4\rangle,
\quad E_8(-1)\oplus D_9(-1),\quad E_7(-1)^{\oplus 2}\oplus A_3(-1),$$
$$D_{17}(-1),\quad D_{12}(-1)\oplus D_5(-1),\quad D_8(-1)^{\oplus 2}\oplus\langle-4\rangle,
\quad A_{15}(-1)\oplus A_1(-1)^{\oplus 2},\quad E_6(-1)\oplus A_{11}(-1).$$

Read from Scattone (Zotero `SF7T3C8G`), §6.3 *Degree four*, and Remark 5.1.4.
The argument is not a $p$-adic genus computation; it runs through **Niemeier
lattices and primitive embeddings of $D_7$**.

| Node | Statement | Source | Depends on |
| --- | --- | --- | --- |
| F5.1 | Niemeier's classification: the 24 even unimodular lattices of rank 24, by root system | Scattone (3.5.1), the table of $\mathcal{U}^{24}$ | — |
| F5.2 | for $E \in I_{2,e}(L)$, the lattice $E^\perp/E$ lies in the genus of $\langle -2k/e^2\rangle \oplus E_8 \oplus E_8$ | Scattone Remark 5.1.4 | genus of a lattice |
| F5.3 | Proposition 6.1.2 at $k=2$: $N \cong D_7$, and the classes are obtained from the primitive embeddings of $N$ into the members of $\mathcal{U}^{24}$ | Scattone Prop. 6.1.2 | F5.1 |
| F5.4 | $D_7 \subset E_8$, $D_7 \not\subset E_7$, $D_7 \not\subset A_m$ for every $m$ | Scattone §6.3 | — |
| F5.5 | hence only eight Niemeier lattices admit such an embedding: $E_8^3$, $E_8{+}D_{16}$, $E_7^2{+}D_{10}$, $D_{24}$, $D_{12}^2$, $D_8^3$, $D_9{+}A_{15}$, $E_6{+}D_7{+}A_{11}$ | Scattone §6.3 | F5.3, F5.4 |
| F5.6 | each embedding is unique up to equivalence **except** the two distinct embeddings into $E_8 + D_{16}$ — which is where the nine comes from | Scattone §6.3 | F5.5, Nikulin's primitive-embedding theory |
| F5.7 | the orthogonal complements are the nine generalized types $\langle-4\rangle{+}E_8{+}E_8$, $\langle-4\rangle{+}D_{16}$, $E_8{+}D_9$, $E_7^2{+}A_3$, $D_{17}$, $D_{12}{+}D_5$, $\langle-4\rangle{+}D_8^2$, $A_1^2{+}A_{15}$, $E_6{+}A_{11}$ | Scattone §6.3 | F5.6 |
| F5.8 | Corollary 5.6.10: for $k$ equal to 1, a prime, or the square of an odd prime, $I_2(L)/O^*(L) = I_2(L)/O_-(L)$, so the two compactifications have isomorphic boundaries | Scattone Cor. 5.6.10 | F5.7 |

F5.7 is Sterk's list, and it matches his p. 59 verbatim.  The count of nine is
**not** a genus-class count: it is eight lattices with one of them admitting two
inequivalent embeddings.  That is a fact about primitive embeddings, and I would
not have recovered it by reasoning about discriminant forms.

Scattone also records (§6.3) that the same root systems can be recovered "by
applying Vinberg's method to the lattice $L = \langle-4\rangle \oplus H \oplus
E_8^2$", with the Coxeter diagram in his Figure 6.3.1, noting that $O_r(L)$ has
infinite index in $O(L)$ — the same computation Sterk runs, on the degree-four
K3 side.  That is a cross-check on C3–C7 from an independent source, and it was
invisible to me while I was writing the node from memory.

### ⚠ F1, F2, F3, F4, F6 below are UNSOURCED and must be redone

The tables in the five subsections that follow were written from memory and
attributed to sources that were never opened — Nikulin for F1, Vinberg for F3
and F4, Baily–Borel for F6 — in violation of `FRM-02`, which forbids exactly
this.  The excuse recorded at the time, that the sources needed reading first,
was also false: Nikulin (`TTY9FFJS`), Vinberg 1975 (`73LVC9YS`), Scattone
(`SF7T3C8G`) and Baily–Borel (`Z9PM5MMD`) are all in the library with text
extractions.

F5 above has since been rewritten from Scattone and shows what the difference
costs: the fabricated version had the nine arising from a $p$-adic genus
computation through Nikulin 1.13.2 and 1.14.2, and the source has it arising
from primitive embeddings of $D_7$ into Niemeier lattices, with the ninth class
coming from $E_8+D_{16}$ admitting two inequivalent embeddings.  The
dependencies were wrong, the mechanism was wrong, and the shape of the work was
wrong.

Treat every row below as a guess about what the source might say, not as a node.
Each is to be rewritten from its source in turn, as F5 was.

### F1 (unsourced): discriminant forms

| Node | Statement | Depends on |
| --- | --- | --- |
| F1.1 | for a nondegenerate lattice $L$, the dual $L^* = \{x\in L\otimes\mathbb{Q} : (x,L)\subseteq\mathbb{Z}\}$ is a lattice, containing $L$ when $L$ is integral | — |
| F1.2 | the discriminant group $A_L = L^*/L$ is finite of order $\lvert\det\mathrm{Gram}(L)\rvert$ | F1.1 |
| F1.3 | the discriminant bilinear form $b_L : A_L\times A_L\to\mathbb{Q}/\mathbb{Z}$ is well defined and nondegenerate | F1.2 |
| F1.4 | for $L$ **even**, the discriminant quadratic form $q_L : A_L\to\mathbb{Q}/2\mathbb{Z}$, $q_L(x+L)=(x,x)\bmod 2\mathbb{Z}$, is well defined and satisfies $q(x+y)-q(x)-q(y)=2b(x,y)$ | F1.3 |
| F1.5 | $A_{L\oplus M}\cong A_L\oplus A_M$ orthogonally, with $q_{L\oplus M}=q_L\oplus q_M$ | F1.4 |
| F1.6 | $O(q_L)$: the automorphisms of $A_L$ preserving $q_L$ | F1.4 |
| F1.7 | the natural homomorphism $O(L)\to O(q_L)$ | F1.6 |
| F1.8 | $A_U=0$; $A_{U(2)}\cong(\mathbb{Z}/2)^2$ with its form; $A_{E_8(-2)}\cong(\mathbb{Z}/2)^8$ | F1.4, F1.5 |
| F1.9 | hence $A_{L_-}\cong\tfrac12 U(2)/U(2)\oplus\tfrac12 E_8(-2)/E_8(-2)$ — the decomposition $\Gamma$ is defined to respect | F1.5, F1.8 |

Nine elementary nodes from the root of stratum F to the object A1 (Sterk 2.10)
quantifies over.

### F2 (unsourced): $O^*$, and the transformations 2.18 runs on

Sterk works with $O^*$ rather than $O$ throughout 2.17, 2.18 and 3.2.1, and the
proof of 2.18 is built from Siegel–Eichler transformations.  Neither was in the
graph.

| Node | Statement | Depends on |
| --- | --- | --- |
| F2.1 | Sterk's definition of $O^*(N)$ — **locate in Chap. 2 §1; not present in the text read so far** | — |
| F2.2 | the Siegel–Eichler transformation $E_{u,y}$ for isotropic $u$ and $y\perp u$, and that it is an isometry | F1.1 |
| F2.3 | $E_{u,y}\in O^*(N)$ | F2.1, F2.2 |
| F2.4 | $E_{u,y}$ acts trivially on $A_N$, so lies in the kernel of $O(N)\to O(q_N)$ | F2.2, F1.7 |
| F2.5 | for $\Lambda = U\oplus U(2)$, the involution $e'\mapsto f'$, $f'\mapsto e'$, $e\mapsto e$, $f\mapsto f$ generates $O(\Lambda)/O^*(\Lambda)$ — stated in the proof of 2.17 | F2.1 |

### F3 (unsourced): affine diagrams and parabolic subdiagrams

| Node | Statement | Depends on |
| --- | --- | --- |
| F3.1 | the Coxeter diagram of a finite set of roots: vertices the roots, edge datum $(\alpha_i,\alpha_j)^2/\big((\alpha_i,\alpha_i)(\alpha_j,\alpha_j)\big)$, with value $1$ drawn $\infty$ | — |
| F3.2 | a diagram is *parabolic* when the restricted form is negative semidefinite with a one-dimensional radical per connected component | F3.1 |
| F3.3 | the rank of a parabolic diagram is $\#\text{vertices}-\#\text{components}$ | F3.2 |
| F3.4 | the extended Dynkin diagrams $\tilde A_n,\tilde B_n,\tilde C_n,\tilde D_n,\tilde E_{6,7,8},\tilde F_4,\tilde G_2$, each as an explicit Gram matrix in a fixed convention | F3.1 |
| F3.5 | **classification**: every connected parabolic diagram is one of F3.4 | F3.2, F3.4; needs Vinberg read |
| F3.6 | the type of a parabolic subdiagram is determined by its Gram matrix up to isomorphism, and vertex norms together with edge data separate $\tilde B_n$ from $\tilde C_n$ | F3.4 |

F3.6 is the node the Sage reconstruction already needs and that the namer there
got wrong twice: the path with two short end nodes is not $\tilde B_n$ in the
Bourbaki convention, and Sterk follows Vinberg's table.  Whichever convention
F3.4 fixes is the one C3–C7 must be stated in.

### F4 (unsourced): Vinberg's algorithm

| Node | Statement | Depends on |
| --- | --- | --- |
| F4.1 | for $N$ of signature $(1,n)$: the positive cone $C$ and the Lobachevskii space $\Lambda(N)=C/\mathbb{R}_+$ | — |
| F4.2 | points at infinity of $\Lambda(N)$ correspond to isotropic lines in $N_\mathbb{R}$ | F4.1 |
| F4.3 | for $G\le O_C(N)$ of finite index: the reflection subgroup $W(G)$ and its fundamental polyhedron $P$ | F4.1 |
| F4.4 | the algorithm: from $x\in C\cap N$, mirrors are enumerated by minimizing $(x,y)^2/\lvert(y,y)\rvert$ subject to nonnegativity against those already chosen | F4.3; needs Vinberg read |
| F4.5 | **completeness**: the enumeration gives every wall of $P$ | F4.4; needs Vinberg read |
| F4.6 | vertices at infinity of $P$ correspond to parabolic subdiagrams of $\Sigma(G)$ of rank $n-1$ | F4.5, F3.5; needs Vinberg read |
| F4.7 | the isotropic vector a parabolic subdiagram represents, as a nonnegative combination of its vertices | F4.6; needs Vinberg 1983 (1.9) read |

F4.5 is the expensive node and the only one C3–C7 genuinely need: without it the
five diagrams are lists of mirrors that may be incomplete, and every count of
isotropic planes is a lower bound rather than a classification.

### F6 (unsourced): from isotropic subspaces to boundary strata

| Node | Statement | Depends on |
| --- | --- | --- |
| F6.1 | the type IV domain $\Omega=\{[\omega]\in\mathbb{P}(L\otimes\mathbb{C}) : (\omega,\omega)=0,\ (\omega,\bar\omega)>0\}$ for $L$ of signature $(2,n)$, with two connected components | — |
| F6.2 | an arithmetic $\Gamma\le O(L)$ acts properly discontinuously on $\Omega$ | F6.1 |
| F6.3 | boundary components of $\Omega$ are indexed by isotropic subspaces of $L\otimes\mathbb{R}$, and are rational exactly when the subspace is defined over $\mathbb{Q}$ | F6.1 |
| F6.4 | in signature $(2,n)$ an isotropic subspace has dimension $1$ or $2$, giving a point or a half-plane — Sterk asserts exactly this at (3.1) | F6.3 |
| F6.5 | the Baily–Borel topology on $\Omega^*$, and that $\Omega^*/\Gamma$ is a normal projective variety | F6.2, F6.3; needs Baily–Borel read |
| F6.6 | the boundary strata of $\Omega^*/\Gamma$ are the $\Gamma$-orbits of rational boundary components | F6.5 |
| F6.7 | one stratum lies in the closure of another exactly when the isotropic subspaces are nested | F6.5 |
| F6.8 | equivalently, the boundary complex is $\Gamma\backslash\mathcal{T}(G)$ | F6.6, F6.7 |

F6.4 is what makes the target finite — it is why the building is
one-dimensional.  F6.6 and F6.7 are what D0 (3.2.4) and the incidence diagram
(3.4) rest on, and they are exactly what was smuggled into `def Incident`.

### Reading owed

Ten nodes are marked as needing a source read: F3.5, F4.4–F4.7 (Vinberg 1975,
1983), F5.3–F5.6 (Scattone, Nikulin), F6.5 (Baily–Borel).  F2.1 needs a
definition located in Sterk himself.  Every other node of F1–F6 is statable from
what is in hand.

**F1 is the root of the whole tree, not a side condition.** $\Gamma$ is defined
by how an isometry acts on $L_-^*/L_-$ respecting a decomposition of the
discriminant form; without F1 the group cannot be stated, so neither can any
theorem that mentions it — which is every theorem here.  Any formalization
begins with F1 or begins by inventing a surrogate for it.

F3 has a consequence for the C stratum that the earlier "cheap half" reading
missed.  Stating that a set of vertices is a parabolic subdiagram *of type
$\tilde E_8$, of rank 8* needs the affine classification.  What is genuinely
free of F3 is smaller: the roots, their Gram matrix, and that the restricted
form is negative semidefinite with a one-dimensional radical per component.
Naming the type is not.

## Coverage: every labelled statement of Chap. 2

The DAG above is a subgraph of the paper, not the whole of it.  This table is
the complete list of labelled statements in Chap. 2 §§1–3, so that a reader can
see which are carried and which are deliberately not, with the reason.  A blank
disposition would mean the filtering was done silently.

| Item | Kind | Disposition |
| --- | --- | --- |
| 1.1–1.4 | setup | out — the $K3$ lattice $L$, the involution $I$, and the eigenlattices; ambient notation, carried implicitly by the coordinates of $L_-$ |
| 2.1 | Definition | out — almost polarization and its degree; names the surfaces whose period space this is, needed for the mission description, not for the boundary complex |
| 2.2, 2.3 | setup | out — the $K3$ double cover and its marking |
| 2.4 | Proposition | out — identifies the two elliptic fibrations; geometry of the double cover |
| 2.5 | Proposition | out — the same two pencils in terms of $\bar E'$ |
| 2.6 | Remark | out — commentary on 2.4 |
| 2.7, 2.8 | Definitions | **A0** |
| 2.9 | Proposition | out — the period map is well defined; needed to call $\Omega_-/\Gamma$ a period space, not to compute its boundary |
| 2.10 | Lemma | **A1** |
| 2.11 | Remark | **A1a** — $\Gamma$ is *not* the group one might expect; a caveat on the definition in A1 |
| 2.12 | setup | out — the period point and its image in $\Omega_-/\Gamma$ |
| 2.13 | Lemma | **A2** |
| 2.14 | Proposition | out — $P$ is injective; the Torelli half of the paper |
| 2.15 | setup | **A6a** — defines the special sets $R_-$ and $S_-$ |
| 2.16 | Lemma | **A4** |
| 2.17 | Corollary | **A5** |
| 2.18 | Corollary | **A6** |
| 2.19 | Lemma | **A7** |
| 2.20 | Proposition | out — characterizes special Enriques surfaces |
| 2.21 | Remark | **A8** — $R_-$ is a single $\Gamma$-orbit, by 2.18 |
| 3.1 | setup | out — recollection of the Satake–Baily–Borel construction; the content is D3, D4 |
| 3.2.1 | Lemma | **B1** |
| 3.2.2 | computation | **B2** |
| 3.2.3 | Proposition | **B3** |
| 3.2.4 | Remark | **D0** — five zero-dimensional *boundary components*; Sterk's own crossing from orbits to strata, so it depends on D4, not on B3 alone |
| 3.3.1–3.3.3 | setup | **C1**, **C2** — the statement of Vinberg's results as used |
| 3.3.4 | Lemma | **B4** |
| 3.3.5–3.3.12 | computations | **C3**–**C8** |
| 3.3.13 | method | **B8** |
| 3.3.14 | Lemma | **B5** |
| 3.3.15 | Proposition | **B6** |
| 3.3.16 | Proposition | **B7** |
| 3.3.17 | Remark | **C9** |
| 3.3.18 | Remark | **C10** |
| 3.3.19, 3.3.20 | computations | **D5** |
| 3.4 | — | **C12**, **G** |

**The out-of-scope column above is not yet valid, and the reason it gave was
wrong.**  Those rows — the period map, the $K3$ double cover, Torelli, almost
polarizations — are inputs to the boundary computation exactly when the goal
mentions Enriques surfaces or their period space, which the goal as stated
does.  Excluding them while keeping the name is a narrowing of the target
disguised as a scope judgment (`FDC-08`).  It runs deeper than the propositions
listed: $L_-$ is not a Gram matrix in the source but the anti-invariant
eigenlattice of the involution on $H^2(X,\mathbb{Z})$ of the $K3$ cover, tied to
it by Horikawa's isometry $\mu : H^2(X;\mathbb{Z}) \to L$ with
$I \circ \mu = \mu \circ I^*$.  Introducing $L_-$ by its Gram matrix severs that
tie and leaves the development unable to say what $L_-$ is.

Substrate for that layer, searched at revision `0df444a3`: no complex manifolds,
no compact complex surfaces, no $K3$ surfaces, no Hodge structures, no line
bundles, no period maps, no Torelli.  Stratum **E** below is therefore as absent
as stratum F, and larger.

| Node | What it is | Needed by |
| --- | --- | --- |
| E1 | complex manifolds, compact complex surfaces, divisors and line bundles, the canonical bundle | E2–E6 |
| E2 | $K3$ surfaces and Enriques surfaces; the $K3$ double cover and its involution $I$ | 2.1–2.5, 2.9 |
| E3 | $H^2$ with its intersection form; Horikawa's isometry identifying it with $L$, and $L_-$ as the anti-invariant eigenlattice | the definition of $L_-$ itself |
| E4 | Hodge structures of weight 2 and the period point | 2.9, 2.12 |
| E5 | the period map and its domain $\Omega_-$ | 2.9, 2.14 |
| E6 | Torelli for $K3$ surfaces | 2.14 |

**The target does not change.**  There is one target node — Sterk's theorem as
stated — and every gap discovered between it and Mathlib adds nodes.  Size is
an output of this graph, never an input to the goal.  So there is no
out-of-scope column: the rows above marked "out" are E-stratum nodes, and the
dispositions stand only as an ordering, not as exclusions.

An earlier revision of this file called stratum E "a decades-scale program".
That was off by about three orders of magnitude, and it was load-bearing: it
was the premise for offering a smaller target.

Comparable completed work, September 2026.  Fermat's Last Theorem was formalized
end to end in **11 days**, largely autonomously, with human input limited to
occasional high-level instructions: 13 million lines of Lean, 30,300 theorems,
about six billion output tokens — over five times the size of Mathlib, for a
substrate (automorphic forms, Galois representations, Shimura varieties) far
larger than anything here.  The Navier–Stokes finite-time blowup was formalized
in 17 hours after a proof produced in about 88.

Two things follow for this graph.  Its size — hundreds of nodes, not tens of
thousands — puts it well inside what that record makes routine.  And the
mechanism matters: the FLT attempts that **failed** did so because agents lost
track of the project's state, and the successful run was the one that moved to
Prove2Me, whose DAG of theorem statements is what kept the state.  The graph is
not preliminary paperwork before the real work; it is the artifact that makes
the work possible at this scale.

The loop body here is: formalize one definition or lemma from a standard text,
with its citation.  Hours per node at most, most nodes mutually independent.
The correct description is a grind of known size.

Nodes added by this table and not in the strata above: **A1a** (2.11),
**A6a** (2.15), **A8** (2.21), **D0** (3.2.4).

## What the DAG says about scope

Strata A and B are ordinary lattice theory and are within reach of the pinned
Mathlib.  Stratum C needs Vinberg's algorithm, which Mathlib does not have;
C3–C7 can be stated as explicit root data with their Gram matrices and their
parabolic subdiagrams, which is checkable without Vinberg, but the *completeness*
of each diagram — that these are all the mirrors — is C1 and is not.  Stratum D
is absent from Mathlib entirely: no buildings, no parabolic subgroups of
algebraic groups, no Baily–Borel, no Satake.

So the tree has two natural frontiers.  A solver can attack A, B, and the
explicit parts of C immediately.  D is where the mission is a formalization
campaign rather than a lattice computation, and it is where the goal theorem
gets its meaning: without D the count is a statement about orbits of
sublattices, and calling those orbits boundary components — rather than proving
they correspond — is the failure `FRM-01` names.
