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

| Subject | What it is | Needed by | Mathlib substrate |
| --- | --- | --- | --- |
| S1 | even lattices, the dual $L^*$, the discriminant group $L^*/L$, and the discriminant **form** $q : L^*/L \to \mathbb{Q}/2\mathbb{Z}$ with its orthogonal decomposition | **A0, A1** — the definition of $\Gamma$ — and C11, A3 | `ZLattice` and `dualSubmodule` exist; the discriminant form does not |
| S2 | $O^*(N)$: the isometries Sterk distinguishes from $O(N)$, by spinor norm / preserved component of the positive cone | A5, A6 (2.17, 2.18), B1 | absent — no spinor norm |
| S3 | affine Coxeter and Dynkin diagrams: the extended types, subdiagrams, parabolic subdiagrams and their rank | C1, and the explicit half of C3–C7 | finite Cartan matrices only (`Matrix/Cartan.lean`, through $E_8$); no affine types |
| S4 | hyperbolic reflection groups: Lobachevskii space, the fundamental polyhedron of $W(G)$, Vinberg's algorithm and its completeness | C1, C2 | absent |
| S5 | genus theory of even lattices — $p$-adic invariants — enough to state Scattone's nine possibilities for $F^\perp/F$ | C11 | absent |
| S6 | reductive groups over $\mathbb{Q}$, parabolic $\mathbb{Q}$-subgroups, spherical buildings; hermitian symmetric domains of type IV; the Baily–Borel construction and its topology | D1–D4 | absent |
| S7 | the upper half plane and congruence subgroups, for $\mathbb{H}/\Gamma^1(2)$ | D5 | present — `UpperHalfPlane`, `Gamma0`/`Gamma1` |

**These rows are subjects, not statements, so none is a node.**  They are placeholders standing where sub-graphs belong, and until
each is decomposed the graph understates the work by an unknown amount — the
same defect as the "external, cited" leaves that `FDC-03` was written about,
one level down.  They survey what Mathlib has and lacks; the node numbering below is independent of them.

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

### Stratum F, rebuilt from Scattone §3

The five subsections that stood here were written from memory and attributed to
sources never opened.  They are deleted rather than kept as guesses.  What
replaces them is read from Scattone (`SF7T3C8G`), whose §3 *is* this stratum,
developed systematically — the theory Sterk uses, written out with numbers and
proofs.  Its table of contents alone settles what the foundations are:

    3.1 Lattices                          3.5 (Niemeier lattices)
    3.2 Discriminant-quadratic forms      3.6 Orthogonal groups
    3.3 Genera of lattices                3.7 Elementary transformations
    3.4 The Minkowski–Siegel formula

**A node is terminal only when its next dependency is in Mathlib.**  None of the
nodes below is terminal; the *next* column names what each descends into, and
where that is another source, the descent continues there.

| Node | Statement | Read? | Next dependency |
| --- | --- | --- | --- |
| F1.1 | §3.1, the lattice notions Scattone fixes: divisor of a vector, $v^*$, primitive sublattice, $I_{2,e}(L)$ | section **not read** | Mathlib `ZLattice`, `QuadraticForm` |
| F1.2 | §3.2, the discriminant-quadratic form $q : G_L \to \mathbb{Q}/2\mathbb{Z}$ and the invariant $\ell(G_L)$ | section **not read** | F1.1; Nikulin §1 |
| F1.3 | Thm 3.2.1 (= Nikulin 1.10.2): an even lattice with signature $(n_+,n_-)$ and discriminant form $q$ exists iff … | statement read, condition **not** transcribed | Nikulin 1.10.2 |
| F1.4 | Thm 3.2.2 (Nikulin): an even lattice with signature $(t_+,t_-)$ and discriminant form $q$ can be primitively embedded … | statement read, conclusion **not** transcribed | Nikulin |
| F2.1 | §3.6, the orthogonal groups $O(L)$, $O^*(L)$, $O_-(L)$ as Scattone defines them — **the definition node A5, A6 and B1 need, and it is here, not in Sterk** | section **not read** | F1.2 |
| F2.2 | Lemma 3.6.1: for $L = \langle-2k\rangle \oplus H^2 \oplus E_8^2$, $\lvert O(G_L)\rvert = 2^{p(k)}$ with $p(k)$ the number of distinct … | statement read, tail **not** transcribed | F2.1, F1.2 |
| F2.3 | §3.7, the group $\mathcal{E}(L)$ of elementary (Eichler) transformations | section **not read** | F1.1 |
| F2.4 | Lemma 3.7.1 (Eichler): $\mathcal{E}(L) \subseteq O^*(L)$ for every even lattice $L$ | statement read | F2.1, F2.3 |
| F2.5 | Prop 3.7.3: for $L$ even containing **at least two hyperbolic planes** and $v,w$ primitive with $(v,v)=(w,w)$ — some $\phi\in\mathcal{E}(L)$ carries $v$ to $w$ **iff** $v^* = w^*$ | statement read | F2.3, F2.4, F1.1 |
| F3.1 | §3.3, the genus of a lattice | section **not read** | F1.2; $p$-adic quadratic forms |
| F3.2 | Thm 3.3.1 (Nikulin): for $L$ even, nondegenerate, indefinite with $\mathrm{rk}\,L > \ell(G_L)+2$ — (i) the genus of $L$ contains one class, and (ii) $O(L)\to O(G_L)$ is **surjective** | statement read | Nikulin; F3.1 |
| F3.3 | §3.4, the Minkowski–Siegel formula | section **not read** | F3.1 |
| F4.1 | Thm 3.5.1 (Niemeier): exactly 24 even unimodular negative-definite lattices of rank 24 up to isomorphism, with the root type $R(L)$ a complete invariant; and the table of the 24 types | statement and table read | F3.1, F3.3 |

**F2.5 is Sterk's 2.18 (node A6)**, in a cleaner form and with its hypothesis
visible: *at least two hyperbolic planes*.  So A6 is not a leaf, its real content
is Eichler's criterion, and the condition is equality of the images $v^*$ in the
discriminant group — exactly the invariant F1.2 constructs.

**F3.2 is what Sterk's 2.10 and 2.13 rest on.**  Surjectivity of
$O(L)\to O(G_L)$ is Nikulin's theorem under a rank condition, not a fact about
$L_-$, and A2 ("$G = O(L_-)$") is an instance of it.

**F4.1 is where F5 descends**, so the Niemeier classification is a node of this
graph with its own descent, not a citation to lean on.

Three things this makes visible that the invented version hid.  Scattone §3
answers F2 completely, where the guessed version had "locate Sterk's definition
of $O^*$" standing as an open problem.  The genus (F3.1) sits under both the
Niemeier classification and F5, so it is load-bearing twice.  And every *not
read* in the third column is a section of a memoir sitting in the library — the
work is reading, and it has not been done.

### Still missing from this stratum

Vinberg's algorithm and Baily–Borel had subsections here that were fabricated
and are now deleted.  Both sources are in the library — Vinberg 1975
(`73LVC9YS`), Baily–Borel 1966 (`Z9PM5MMD`) — and both need the treatment
Scattone §3 just received: read the section, take the numbered statements, name
the next dependency of each.  Until then C1, C2 and D1–D4 have no foundations
recorded beneath them.

**The discriminant form (F1.2) is the root of the whole tree, not a side
condition.** $\Gamma$ is defined by how an isometry acts on $L_-^*/L_-$
respecting a decomposition of the discriminant form; without it the group cannot
be stated, so neither can any theorem that mentions it — which is every theorem
here.  Any formalization begins at F1.1–F1.2 or begins by inventing a surrogate
for them.

The affine classification has a consequence for stratum C that an earlier
"cheap half" reading missed.  Stating that a set of vertices is a parabolic
subdiagram *of type $\tilde E_8$, of rank 8* needs it.  What is genuinely free
of it is smaller: the roots, their Gram matrix, and that the restricted form is
negative semidefinite with a one-dimensional radical per component — which is
what the Sage reconstruction computes.  Naming the type is not free, and the
node that would carry the classification is one of the two deleted as
fabricated, so it is currently unrecorded.

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
