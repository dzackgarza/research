# Dependency DAG: Sterk's boundary complex

The target is the combinatorial structure of the boundary of the Baily–Borel
compactification of $\Omega_-/\Gamma$: five zero-dimensional strata, nine
one-dimensional strata, with the incidence relation of Sterk (3.4).
Equivalently, $\Gamma \backslash \mathcal{T}(G)$ for $G = \mathrm{O}(L_-\otimes\mathbb{Q})$,
whose Tits building over $\mathbb{Q}$ is one-dimensional because $G$ has
$\mathbb{Q}$-rank 2 — a clause that names two theorems and a computation, and is
AG17 over AG18 and AG19.

Source: H. Sterk, *Compactifications of the period space of Enriques surfaces*
(Nijmegen thesis, 1988), Chap. 2; published as Math. Z. 207 (1991) with §3.2,
§3.3 renumbered §4.2, §4.3.  Zotero `Ste95a` / `Ste91` / `Ste88a`.

Node status: **S** a numbered statement in Sterk; **U** an unnumbered
computation in Sterk carried by a figure; **X** external, cited to another
source; **M** requires substrate absent from Mathlib at the pinned revision;
**LC** a known implementation route through `lean-categories`, pending its
publication to Prove2Me (see *Implementation routes* below).

The strata, in the order they are read below: **A**, **B**, **C**, **D** are the
paper's own steps; **BB**, **Bo**, **Cl**, **E**, **Nk** are what its citations
open; **AF**, **AG**, **HS**, **Ky**, **Lo**, **Ni**, **Pa**, **Rt**, **V** and
the **F** rows are the foundations under those.

`check_dag.py` reads this file and fails on five things: a dependency cell that
names a node no row defines, one that names neither a node nor a substrate, an
empty one, a node in no terminality-verdict table, and a greenfield stratum with
no construction-floor row.  Each is a way for the graph to look complete while
hiding work — the last two because a node with no verdict is a node nobody has
asked who supplies, and a stratum with no floor reads as blocked on foundations
that exist.  Run it after editing a table.

**What it does not do, and what nothing here can do.**  Every one of those checks
asks whether a cell or a row is *present*.  None asks whether it is *true*.  A
terminality verdict is a claim about the pinned Mathlib and about several other
Lean repositories — that a named declaration exists, that it says what the node
says, that a corpus claim survives reading the corpus — and that is a question
about a large body of code no script here reads.  Those verdicts are established
by hand, and each row records what was read so the next reader can re-check it
rather than trust it.  Four of them were false while the script was green: F4.1's
substrate, `Commensurable` as the floor's one missing primitive, `JordanRing` in
HS16, and "no hyperbolic space in any model" under Lo.  A green run is a guard
against a stale or half-extended table.  It is not evidence that the graph bottoms
out.

## Implementation routes through lean-categories

`~/gitclones/lean-categories` is a sorry-free corpus of 236 modules (1.9 MB,
45,679 lines, 2,385 definitions and 1,486 theorems) whose `Lattices/Valued/`
subtree covers much of what this graph calls stratum F.  It imports only
`Mathlib`, `Lean` and itself, so the whole graph is publishable to Prove2Me as
platform definitions and theorems; a definition may only be submitted once its
dependencies are `PUBLISHED`, so publication is a bottom-up sweep of its 19
dependency layers.  **That refactor and publication is tracked as an issue on
`lean-categories`, not here.**  When it lands, the nodes below acquire a
supplier rather than becoming done, and the integration is wired then.

Implementation routes, with their evidence — a filename is not evidence, and a
route is not a satisfied node.  The `Lattices/Valued/` subtree holds about 110
files; the rows below are the ones read against a node.

| Node | lean-categories | Status |
| --- | --- | --- |
| F1.7 dual lattice, divisor, $v^*$ | `MetricDual`, `Discriminant.toMetricDualLattice` | route located — declarations read; **satisfies nothing yet** |
| F1.10 discriminant group and its forms | `Discriminant` (`discriminantModule` $= L^\sharp/L$, `discriminantBilinMap`, `discriminantSymBilWQuadraticMap`, `discriminantSymBilWFormIsCokernel`), `DiscriminantQuadratic` (`evenDiscriminantQuadraticMap` with its `polar` lemma) | route located — declarations read; **satisfies nothing yet** |
| F2.1 $\tau : O(L) \to O(G_L)$ | `DiscriminantAction` — an orthogonal-group element as a lattice automorphism, the contragredient action on the value dual, and "the general discriminant transport for the lattice automorphism"; `DiscriminantFunctor` — nonsingular finite torsion forms valued in $\mathrm{Frac}(R)/R$, and that a lattice isomorphism preserves its form | route located — declarations read.  This is $\tau$'s construction; what is missing is the statement that it is a **group homomorphism into $O(G_L)$**, which is F2.1 |
| F2.3 Cartan–Dieudonné for an indefinite rational form | `ReflectionGeneration` — the line of a nonsingular vector and its orthogonal complement split the carrier, an isometry fixing $v$ fixes its line, and the cross terms vanish; `Reflection`, `ReflectionTransitivity` | route located — declarations read.  These are the **induction step** of Cartan–Dieudonné, over an arbitrary base ring rather than the positive definite reals Mathlib restricts to.  The factorization theorem itself is not there |
| F2.4, F2.5 $O_-(L)$, $O^*(L)$ | `CanonicalSpinorNorm` — the canonical spinor norm of a nondegenerate finite symmetric form, that every spinor norm is that one, and its value on a reflection; `AdelicSpinorNorm` — the completed quadratic space at a finite place and its canonical spinor norm | route located — declarations read.  The spinor norm exists as a construction with its reflection value, which is what F2.3's Brieskorn form is stated in terms of.  Note the dyadic gate: `AdelicSpinorNorm` proves *two is invertible in a completion at a finite place* and works there |
| F3.1 genus | `Hasse`, `SpinorGenusAdelic`, `DyadicSymbol`, `Adele`; `ClassFiniteness` carries the geometry-of-numbers argument (a positive definite real matrix as $B^{\mathsf T}B$, convex cubes) | route located for the local invariants — declarations read; the **genus as an equivalence class** and its finiteness statement are the part to check next |
| F4.1 $R(L)$ and the type of $L$ | `RootLattice` — $R(L)$ as the vectors of self-pairing $\pm1$ or $\pm2$, with the root set as a union of four level sets; `SimplyLaced` — in an even negative definite lattice the four values reduce to one and the root graph is simply laced; `RootBase`, `RootBaseExists`, `DiagramBounds`, `ArmBounds`, `DiagramShape`, `ADERealization` | **the strongest route in the corpus.**  `DiagramShape.adeClassification` is sorry-free and states it outright: the graph of a root base of an even negative definite lattice, when connected, is a path through every vertex or a three-armed star whose arm lengths satisfy Mathlib's `ADEInequality.Admissible` — the ADE triples $(1,q,r)$, $(2,2,r)$, $(2,3,3)$, $(2,3,4)$, $(2,3,5)$.  Missing: the comparison of each shape with a **named** lattice (`ADERealization` supplies the reindexing and the Gram matrix and stops at that boundary), and the decomposition of a disconnected root graph into components |
| F4.1's objects; the summands named in F5.4, F5.5, F5.7 | `DefiniteNondegenerate` (`isRootLattice`, `RootLatticeCat`, `rootLatticeRootPairing`, `aRootLatticeObject`, `e8RootLatticeObject`), `DRootLattice` (`dRootLatticeObject`, $D_n$ for $4\le n$ with its Gram matrix proved negative definite) | route located — declarations read.  Supplies the **objects** $A_n$, $D_n$, $E_6$, $E_7$, $E_8$; supplies none of F5.4's embedding statements |
| F1.11, Ni1–Ni10 primitive embeddings | `Sublattice` — a formed embedding is primitive when injective with torsion-free cokernel, finite index when injective with finite cokernel, and the category of lattices admitting a primitive embedding into $M$ | route located — declarations read.  The **vocabulary** of Nikulin's statements, with none of his theorems |
| F1.12 the Minkowski–Siegel weight | `Mass` — $O(L)$ is finite for positive definite $L$, its order, and that the order is an invariant of the global isometry class; `LocalDensity`, `DensityProduct`, `Theta` | route located — declarations read.  The mass side of the formula has its terms; the formula is not stated |
| Pa9 the canonical decomposition of a $p$-adic lattice | `Jordan` — `JordanDecomposition L π n` over a DVR: an irreducible uniformizer, modular components with strictly increasing scale exponents, nonzero, and an orthogonal-sum isomorphism onto $L$; `JordanComponent.exists_isIModular_component`; `JordanLayer`, `JordanFiltration` (`changeUniformizer`, `layerSubmodule_decomposition`, `jump`), `JordanSplitting`, `JordanRecursion`, `JordanInvariants` (`scaleIdeal_eq_of_iso`, `invariants_eq_of_single`, `sum_rank_invariants_eq`) | **route located, and substantial** — seven sorry-free files.  Missing three things Pa9 asserts: global **existence** (`HasJordanDecomposition` is defined and not proved for every lattice), full **uniqueness** (proved for a single component and for the total rank, not for the invariant list), and the **dyadic case** — `JordanSplitting`, `JordanComponent` and `JordanRecursion` gate their splitting lemmas behind `Invertible (2 : R)`, which is exactly the case Pa9 says needs its own treatment |
| F2.10, F2.11 the transformations $E_{f,x}$ and $\mathcal{E}(L)$ | — | **absent.**  `Elementary.lean` is $I$- and $p$-elementary *lattices* — the ideal annihilating the discriminant module — a different notion, and `rg -i eichler` over the corpus returns nothing |
| F4.2, F5.1 Niemeier's 24 lattices | — | **absent.**  `rg -i niemeier` over the corpus returns nothing |

**No node in this graph is stated, let alone proved, and the corpus changes none
of that.** What the table records is a known implementation route: for some
nodes there is code elsewhere that plausibly supplies them, for others there is
not. A route becomes a satisfied node only after the node is stated from its
source, the corpus module is published to the platform, and the published
statement is checked against the node — three steps, none of which has been
taken.  Every "route located" above means declarations were read in another
repository and matched against the node's own statement, and each row says where
the match stops.

F2.10–F2.11 and F4.2 have no route at all, in Mathlib or the corpus.  Each candidate row
becomes verified only by reading the module and comparing it with the source
statement it is supposed to satisfy — the same obligation `FDC-09` places on
writing a node in the first place, since a correspondence asserted on a name is
a fabricated dependency edge.

## Stratum A — the arithmetic of $L_- = U \oplus U(2) \oplus E_8(-2)$

| Node | Statement | Depends on |
| --- | --- | --- |
| A0 | `S` (2.7), (2.8) — definition of $\Gamma$ and of the special sets.  $\Gamma$ is defined by how an isometry acts on $L_-^*/L_-$, so it cannot be stated before the discriminant form, and $L_-$ is an eigenlattice, so it cannot be stated before E6 | F1.7, F1.10, E6 |
| A1 | `S` 2.10 — $\Gamma$ is exactly the isometries whose induced map on $L_-^*/L_-$ respects the decomposition $(U(2)^*/U(2)) \oplus (E_8(-2)^*/E_8(-2))$ | A0 |
| A2 | `S` 2.13 — $G = O(L_-)$; an instance of Nk5, whose rank hypotheses must be checked for $L_-$ | A1, Nk5 |
| A3 | `X` Nikulin 1.13.2 — uniqueness of the even lattice with invariants $(2,10,q)$, **conditional**: see Nk4 for the three conditions, of which (2) and (3) must be checked for $L_-$ | Nk4 |
| A4 | `S` 2.16 — for $\Lambda = U \oplus U(2)$ and $v$ primitive: $v \sim_{O(\Lambda)} e + kf$ if $(v,v) = 2k$, $v \notin 2\Lambda^*$; $v \sim e' + kf'$ if $(v,v) = 4k$, $v \in 2\Lambda^*$ | F1.1, F1.7, F1.8 |
| A5 | `S` 2.17 — the same under $O^*(\Lambda)$, with the extra branch $ke' + f'$ | A4 |
| A6 | `S` 2.18 = Scattone Prop. 3.7.3 = F2.13; note the hypotheses that row omitted: $L$ even with **at least two hyperbolic planes**, criterion $v^* = w^*$ in the discriminant group | A5, F2.13 |
| A6a | `S` (2.15) — defines the special sets $R_- = \{x\in L_- : (x,x) = -2\}$ and $S_-$ — **the rest of the setup not transcribed** | A0 |
| A7 | `S` 2.19 — $S_-$ is a single $\Gamma$-orbit | A1, A6, A6a |
| A8 | `S` 2.21 — $R_-$ is a single $\Gamma$-orbit, by 2.18 | A6a, A6 |
| A1a | `S` 2.11 — a caveat on the definition in A1: $\Gamma$ is *not* the group one might expect — **the remark not transcribed** | A1 |

## Stratum B — the isotropic sublattices

| Node | Statement | Depends on |
| --- | --- | --- |
| B1 | `S` 3.2.1 — a primitive isotropic $v$ with $(v, L_-) = \mathbb{Z}$ satisfies $v \sim_\Gamma e$ | A6 |
| B2 | `S` 3.2.2 — otherwise $(v, L_-) = 2\mathbb{Z}$, and $\tfrac12 v$ is a nontrivial isotropic element of $L_-^*/L_-$; the isotropic elements of the discriminant form, modulo $\Gamma_q$, are the four listed | A1 |
| B3 | `S` 3.2.3 — every primitive isotropic vector is $\Gamma$-equivalent to exactly one of $e$, $e'$, $e'+f'+\omega$, $e'+2f'+\alpha$, $2e+2f+\alpha$ ($\alpha^2 = -8$, $\omega^2 = -4$ in $E_8(-2)$); hence $\lvert I_1(L_-)/\Gamma \rvert = 5$ | B1, B2, A6 |
| B4 | `S` 3.3.4 — $v^\perp/\mathbb{Z}v \cong U \oplus E_8(-2)$ for $v \ne e$, and $e^\perp/\mathbb{Z}e \cong U(2) \oplus E_8(-2)$ | B3, A6 |
| B0 | the ambient lattices of 3.3.14–3.3.16: $\Lambda$, which E6 identifies with $H_2$ of the $K3$ cover, and $K$ — **Sterk's definition of $K$ is not transcribed, and until it is, B5–B7 name a lattice this graph has not defined** | E6, F1.1 |
| B5 | `S` 3.3.14 — $U(2) \oplus E_8(-1)$ is the largest even sublattice of $K$ | B0, F1.2 |
| B6 | `S` 3.3.15 — every $g \in O(K(2))$ extends to an isometry of $\Lambda$ | B5 |
| B7 | `S` 3.3.16 — $K(2)$ is the unique rank-10 sublattice $\tilde\Lambda \subseteq \Lambda$ with $\tilde\Lambda^* = \tfrac12\tilde\Lambda$ and $\tfrac12\tilde\Lambda(2)$ odd | B5 |
| B8 | `U` 3.3.13 — the symmetries of each diagram lift to $\Gamma_v$ | B6, B7 |

## Stratum C — Vinberg's algorithm and the five diagrams

| Node | Statement | Depends on |
| --- | --- | --- |
| C1 | superseded — decomposed into stratum V (V1–V11); the content C1 named is V8 for the correspondence, V10 for the diagram classification, V11 for the algorithm | V8, V10, V11 |
| C2 | `X` the isotropic vector read off a parabolic subdiagram — **locator resolved**: Vinberg, *The two most algebraic K3 surfaces* (`4QDSPB92`), §1.9; see V12, V13 | V12, V13 |
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
C3–C7 all agree with Sterk’s labels once the p. 64 figure is read in full — see
the audit points.  C9 is why a formalization must state the labelling on flags
$(v, F)$, not on $F$.

## Stratum D — from sublattices to boundary components

Read from Scattone §2 (`SF7T3C8G`), which states these in the orthogonal-group
form.  Scattone states them and cites others for them, so stratum BB below
carries what they rest on.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| D1 | the boundary components of $D$: the maximal connected complex analytic subsets of $\bar D \setminus D$ | Scattone §2 | HS11, HS12 — whose definition differs; see there |
| D2 | a boundary component $F$ is **rational** when $N(F)_\mathbb{C}$ is defined over $\mathbb{Q}$; $\mathcal{B}(D)$ is the set of proper rational boundary components | Scattone §2 | D1, HS13, AG1 |
| D3 | realizing $G_\mathbb{R}$ as the orthogonal group of a bilinear form $Q$ on $L_\mathbb{R}$, there is a bijection between boundary components $F \subset D$ and isotropic subspaces $E \subset L_\mathbb{R}$: $E \leftrightarrow F$ **iff** $\mathrm{Stab}_{O(L_\mathbb{R})}(E) = \mathrm{Stab}_{G_\mathbb{R}}(F)$ | Scattone §2 | D1 |
| D4 | the basis and the realization may be chosen so that rationality is preserved: rational boundary components correspond to isotropic subspaces of $L_\mathbb{Q}$, identified with $I(L)$, the primitive isotropic sublattices of $L$ | Scattone §2 | D2, D3 |
| D5 | **the bijection $I(L) \leftrightarrow \mathcal{B}(D)$ preserves incidence**: if $E \leftrightarrow F$ and $E' \leftrightarrow F'$ then $E \subset E' \iff F \subseteq \partial F'$ | Scattone §2 | D4 |
| D6 | the action of $\Gamma$ on rational boundary components corresponds to its action on $I(L)$, so the boundary components of $D_k/\Gamma_k$ are in bijection with the $\Gamma$-equivalence classes of primitive isotropic sublattices | Scattone §2 | D5 |
| D7 | the Baily–Borel compactification: $D \cup \mathcal{B}(D)$ carries a topology making $\overline{D/\Gamma}$ a normal projective variety | Scattone §2; proved in Baily–Borel — see BB8 | D2, BB8 |
| D0 | `S` 3.2.4 — the five zero-dimensional **boundary components**; Sterk's own crossing from $\Gamma$-orbits of isotropic vectors to strata of the compactification, so it rests on D4, not on B3 alone | Sterk | B3, D4, D6 |
| D8 | `S` 3.3.19, 3.3.20 — $\Gamma(E) \cap SL(E) \cong \Gamma^1(2)$, so each one-dimensional component is $\mathbb{H}/\Gamma^1(2)$, with no identification among its cusps | Sterk | D6, C11, B3 |

**D5 is the node that was smuggled into `def Incident N P := N ≤ P`.**  It is a
stated theorem with a locator, and it is an *iff* between containment of
isotropic subspaces and closure of boundary components — precisely the content
that a definition made true by fiat.

D6 is what makes the target a statement about $\Gamma$-orbits at all.  D1 and D2
are the nodes with no Mathlib substrate whatever: they need complex analytic
sets and $\mathbb{Q}$-structures on algebraic groups.

### Stratum BB, from Baily–Borel — what D1, D2 and D7 rest on

Scattone §2 *states* the correspondence D1–D6 use; it does not prove it, and
cites others for it.  These are the nodes underneath, read from Baily–Borel 1966
(`Z9PM5MMD`).

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| BB1 | a parabolic $k$-subgroup: an algebraic subgroup $P \le G$ with $G/P$ projective; such a $P$ is connected, equal to its own normalizer, and is the normalizer of its unipotent radical | BB 2.2 | AG4, AG5 |
| BB2 | a parabolic subgroup of $G^0_\mathbb{R}$ is its intersection with an algebraic parabolic $P \le G$ defined over $\mathbb{R}$; every maximal proper parabolic subgroup of $G^0_\mathbb{R}$ is conjugate to one and only one of the $P_b$ | BB 1.3 | BB1, AG12, AG14 |
| BB3 | boundary components: $X_b = K_b\backslash L_b$ is hermitian symmetric with Harish-Chandra realization $D_b$; $\bar D = \bigcup_{0\le b\le t} o_b \cdot G^0_\mathbb{R}$; the orbit $F_b$ of $o_b$ under $L_b$ is $o_b + D_b$, and the boundary components are the transforms of the $F_b$ | BB 1.5, citing [27], [29], [30] | BB2; stratum HS below |
| BB4 | **Theorem 3.7**: a boundary component $F$ of $X$ is rational **iff** $N(F)_\mathbb{C}$ is defined over $\mathbb{Q}$; if $F$ is rational then $\Gamma(F)$ is of arithmetic type; and the map $F \mapsto N(F)_\mathbb{C}$ … — **tail not transcribed** | BB 3.7 | BB3 |
| BB5 | for a rational boundary component $F$, $N(F)_\mathbb{C}$ is a proper maximal parabolic $\mathbb{Q}$-subgroup of $G$ | BB §3 | BB4, BB2 |
| BB6 | **Theorem 3.8** — the structure statement in the notation of 3.3(ii); **located, not transcribed** | BB 3.8 | BB4 |
| BB7 | the Satake topology: $X^*$, the union of $X$ with its rational boundary components, carries a topology defined by a suitable fundamental set in $X$, for which each $g \in G_\mathbb{Q}$ acts continuously | BB introduction, after Satake [33] | BB4 |
| BB8 | **Theorem 10.11**: there is a weight $l$ and finitely many integral automorphic forms of weight $l$ whose extensions to $X^*$ are nowhere simultaneously zero, and the associated map embeds $V^* = X^*/\Gamma$ as a projective variety | BB 10.11 | BB7, AF1–AF13 |

BB3 is what D1 states, BB4 what D2 states, and BB8 is D7.  BB1–BB3 have no
Mathlib substrate: algebraic groups with their parabolic subgroups, hermitian
symmetric spaces, Harish-Chandra realizations.

BB8's automorphic forms are stratum AF below and BB3's hermitian symmetric
theory is stratum HS.  What is still not descended on this branch is Korányi–Wolf
[27] and the other references BB 1.5 cites for the boundary components
themselves; HS12 states their content with a different onward citation, to AMRT,
and whether the two agree is unchecked.

### Stratum AG, from Borel and Borel–Ji — what BB1, BB2, D2 and the goal rest on

BB1 states what a parabolic $k$-subgroup is and BB2 what a parabolic subgroup of
$G^0_\mathbb{R}$ is; D2 asks when $N(F)_\mathbb{C}$ is defined over $\mathbb{Q}$;
HS13 lands on maximal parabolic subgroups; Pa7 needs strong approximation.  All
four sit on the theory of reductive groups over a field, and **so does the goal's
own opening sentence** — "$\Gamma\backslash\mathcal{T}(G)$, whose Tits building
over $\mathbb{Q}$ is one-dimensional because $G$ has $\mathbb{Q}$-rank 2".  That
sentence names two theorems and one computation, none of which was a node.

Read from Borel, *Linear algebraic groups* (`5HRLF4GB`), §§11, 14, 20, 21, 23.4,
and Borel–Ji, *Compactifications of symmetric and locally symmetric spaces*
(`A5ASLV62`), §§I.2.18 and III.1.8.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| AG1 | $k$-structures on varieties, $k$-closed sets, and the Galois criteria for rationality: a $k$-closed subgroup normalized by a maximal $k$-torus is defined over $k$ when its root set is $\Gamma$-invariant | Borel AG §§11–14; Borel 20.3 | **AG22**, the descent datum split out of this row, over `Scheme.Over`, `pullback` and `IsGalois`; and AG3 for the maximal $k$-torus.  The bare "no Galois descent" this cell used to hold is now a node with a floor |
| AG2 | linear algebraic groups, their Lie algebras, and the Jordan decomposition | Borel §§1–4 | Mathlib `AlgebraicGeometry/Group/Affine.lean` — where `hopfSpec` is the fully faithful $(\mathbf{CommHopfAlg}_R)^{\mathrm{op}} \to \mathbf{Grp}(\mathbf{Sch}/\mathrm{Spec}\,R)$ — and `Group/Smooth.lean`; plus **AG21** for $\mathrm{Lie}(G)$, split out of this row.  The Jordan decomposition is over `Module.End` and the semisimple/unipotent parts |
| AG3 | diagonalizable groups and tori; $X^*(T)$, $X_*(T)$; a torus is **$k$-split** when it is diagonalizable over $k$ | Borel §8 | AG2; **absent** |
| AG4 | a **parabolic subgroup** of $G$ is a closed $P$ with $G/P$ complete — equivalently projective, since $G/P$ is always quasi-projective; and $P$ is parabolic **iff** it contains a Borel subgroup | Borel 11.2 and its Corollary | AG2; Mathlib `AlgebraicGeometry/Morphisms/Proper.lean`, `.../UniversallyClosed.lean` |
| AG5 | **Chevalley**: every parabolic subgroup equals its own normalizer and is connected; every parabolic is conjugate to one and only one parabolic containing a fixed $B$ | Borel 11.16, 11.17 | AG4 |
| AG6 | the root system $\Phi(T,G)$ with its one-dimensional root subgroups $U_\alpha$; and the **Tits system** $\mathcal{T} = (G,B,N,S)$, whence the Bruhat decomposition $G = \coprod_w BwB$ | Borel 14.8, 14.15 | AG4; Mathlib `LinearAlgebra/RootSystem/`, `GroupTheory/Coxeter/` |
| AG7 | **standard parabolic subgroups**: $P_I = B\cdot W_I\cdot B$ for $I\subseteq\Delta$; $P_I$ is the semidirect product of $Z_G(T_I)$ by its unipotent radical $U_{\Phi(I)}$; and every parabolic subgroup is conjugate to exactly one $P_I$ | Borel 14.16–14.18 | AG6 |
| AG8 | **Levi subgroups** of $P$ are the centralizers of the maximal tori of $\mathcal{R}P$, any two conjugate by a unique element of $\mathcal{R}_uP$; two parabolics are **opposite** when their intersection is a common Levi subgroup, and each $P$ with a chosen Levi has exactly one opposite containing it | Borel 14.19–14.21 | AG7 |
| AG9 | $G$ is **isotropic over $k$** when it contains a nontrivial $k$-split subtorus; and for any $k$-split subtorus $S$, the centralizer $Z(S)$ is the Levi subgroup of a parabolic $k$-subgroup | Borel 20.1, 20.4 | AG3, AG8 |
| AG10 | for $P$ parabolic and defined over $k$: $\mathcal{R}P$ and $\mathcal{R}_uP$ are defined over $k$; the Levi $k$-subgroups are the centralizers of the maximal $k$-tori of $\mathcal{R}P$, any two conjugate by a unique element of $\mathcal{R}_uP(k)$; the opposite $P^-$ containing a given Levi $k$-subgroup is defined over $k$; and $G(k)\to (G/P)(k)$ is **surjective** | Borel 20.5 | AG9, AG1 |
| AG11 | for a proper parabolic $k$-subgroup $P$ with Levi $k$-subgroup $L$ and $S$ the identity component of $Z(L)$: $L = Z(S_d)$; $G$ has a proper parabolic $k$-subgroup **iff** it has a non-central $k$-split torus; and $P$ is minimal **iff** $S_d$ is a maximal $k$-split torus | Borel 20.6 | AG10 |
| AG12 | the minimal parabolic $k$-subgroups are conjugate under $G(k)$; the maximal $k$-split tori are conjugate under $G(k)$; and parabolic $k$-subgroups conjugate under $G(K)$ are conjugate under $G(k)$ | Borel 20.9 | AG11 |
| AG13 | the **$k$-rank** $r_k(G)$: the common dimension of the maximal $k$-split tori, well defined by AG12; the relative roots ${}_k\Phi = \Phi(S,G)$, empty exactly when $\mathcal{D}G$ is anisotropic; and the relative Weyl group ${}_kW = N(S)/Z(S)$ | Borel 21.1 | AG12 |
| AG14 | ${}_kP_I = Z(S_I)\cdot U_{\psi(I)}$ for $I\subseteq{}_k\Delta$, with $S_I = (\bigcap_{\alpha\in I}\ker\alpha)^o$; these are distinct and are **all** the standard parabolic $k$-subgroups, and every parabolic $k$-subgroup is conjugate to one and only one of them by an element of $G(k)$ | Borel 21.11, 21.12 | AG13 |
| AG15 | $(G(k), P(k), N(k), R)$ is a Tits system, and $Q\mapsto Q(k)$ is a bijection between the parabolic $k$-subgroups of $G$ and the parabolic subgroups of that Tits system — so a parabolic $k$-subgroup is determined by its $k$-points | Borel 21.15, 21.16 | AG14, AG6 |
| AG16 | the **spherical Tits building** $\Delta_\mathbb{Q}(\mathbf{G})$: simplexes correspond bijectively to the proper rational parabolic subgroups, a proper maximal one is a vertex, and distinct maximal $\mathbf{Q}_0,\dots,\mathbf{Q}_k$ span a $k$-simplex **iff** $\mathbf{Q}_0\cap\cdots\cap\mathbf{Q}_k$ is a rational parabolic subgroup, that simplex being the intersection; $\mathbf{G}(\mathbb{Q})$ acts by conjugation | Borel–Ji III.1.8, citing Tits | AG14 |
| AG17 | $\Delta_\mathbb{Q}(\mathbf{G})$ is a countable set of points when $r_\mathbb{Q}(\mathbf{G}) = 1$, and otherwise a **connected infinite simplicial complex of dimension $r_\mathbb{Q}(\mathbf{G}) - 1$**; the rational parabolic subgroups containing a maximal $\mathbb{Q}$-split torus form an apartment, triangulating an $(r_\mathbb{Q}-1)$-sphere | Borel–Ji III.1.8 | AG16, AG13 |
| AG18 | for $\mathrm{SO}(Q)$ with $Q$ nondegenerate and isotropic over $k$ ($\mathrm{char}\,k\ne2$): $Q$ is isotropic over $k$ **iff** $\mathrm{SO}(Q)$ is, and $r_k(\mathrm{SO}(Q)) = q$, the **Witt index** of $Q$ over $k$; moreover $Z(S) = S\times \mathrm{SO}(Q_o)$ for the anisotropic kernel $Q_o$ | Borel 23.4 | AG13 |
| AG19 | $r_\mathbb{Q}\big(\mathrm{SO}(L_-\otimes\mathbb{Q})\big) = 2$ | AG18 plus the computation below | AG18 |
| AG20 | the **unipotent radical** $R_u(P)$: the maximal connected normal unipotent subgroup, and the Levi decomposition $P = R_u(P)\rtimes L$ | decomposed out of AG5 and BB1, which both name it | AG2, AG4; Mathlib `Subgroup.normalizer`, `Subgroup.closure`, `AlgebraicGeometry/Group/Smooth.lean`.  `rg -i 'unipotentRadical\|IsUnipotent'` over the pinned tree returns nothing, so unipotence itself is part of this node |
| AG21 | $\mathrm{Lie}(G)$ for an affine group scheme, with its bracket | decomposed out of AG2, whose verdict cell records this as absent | AG2; Mathlib `Derivation` with `Derivation.instLieAlgebra` (`RingTheory/Derivation/Lie.lean`), the differentials of `Algebra/Category/ModuleCat/Differentials/Presheaf.lean`, and `hopfSpec` (`AlgebraicGeometry/Group/Affine.lean`).  `Geometry/Manifold/GroupLieAlgebra.lean` is the same passage for a Lie *group* and is the model to follow |
| AG22 | a **descent datum** for a $k$-structure, and a twisted form as a Galois-cohomology class | decomposed out of AG1, whose verdict cell reads "no Galois descent for varieties" | AG2; Mathlib `Scheme.Over` (`AlgebraicGeometry/Over.lean`), `pullback` for base change, `IsGalois` (`FieldTheory/Galois/Basic.lean`), `CategoryTheory.MorphismProperty.Descent` and `AlgebraicGeometry/Morphisms/Descent.lean` — which descend morphism *properties*, so the datum and the form are the content here |

**AG19 is the goal's missing hypothesis, and it is now checked.**  The goal
opens by saying the Tits building is one-dimensional "because $G$ has
$\mathbb{Q}$-rank 2", and that clause named no theorem and no computation.  It
is AG17 at $r_\mathbb{Q} = 2$, resting on AG18 and on the Witt index of $L_-$
over $\mathbb{Q}$.  Computed: $L_-$ has signature $(2,10)$ and determinant
$1024$, so the Witt index over $\mathbb{R}$ — hence over $\mathbb{Q}$ — is at
most $2$; and $\langle e, e'\rangle$, the isotropic generators of $U$ and of
$U(2)$, span a totally isotropic $\mathbb{Q}$-plane, so it is at least $2$.  It
is therefore exactly $2$, the $\mathbb{Q}$-rank is $2$, and
$\dim\Delta_\mathbb{Q} = 1$.  The one-dimensionality of the building is what
makes "five vertices of one type, nine of the other, and the edges of 3.4" the
*whole* of the boundary complex rather than its low-dimensional skeleton.

**AG10's surjectivity of $G(k)\to(G/P)(k)$ is the step that makes rational
boundary components a set of $\mathbb{Q}$-points at all**, and D4 uses it
silently.

Nothing in stratum AG has any substrate.  Mathlib has affine and smooth group
schemes (`AlgebraicGeometry/Group/`) and root systems and Coxeter groups
(`LinearAlgebra/RootSystem/`, `GroupTheory/Coxeter/`), but no torus, no Borel or
parabolic subgroup, no unipotent radical, no Levi decomposition, no $k$-rank and
no building; searching the tree for `parabolic` returns only the Möbius
classification on the upper half plane.  The registry has no algebraic-groups
corpus either.  `chrisflav/bruhat-tits` is the nearest listed repository and it
builds the Bruhat–Tits **tree** of $\mathrm{SL}_2$ over a local field, which is
neither the spherical building nor the general construction.

### Stratum HS, from Viviani — what BB3 and D1 rest on

BB3 names hermitian symmetric spaces, their Harish-Chandra realizations and
their boundary components, and D1 states the boundary components as "the
maximal connected complex analytic subsets of $\bar D\setminus D$".  Neither is
a leaf: both are theorems about bounded symmetric domains, with a definition of
boundary component that is not the one D1 quotes.  Read from Viviani, *A tour
on Hermitian symmetric manifolds* (`RSX977NH`), §§2 and 4 — a survey, so every
row below carries Viviani's own onward citation, mostly to Ash–Mumford–Rapoport–Tai
(`HLAKVB4J`) and Helgason (`3DSB9N5S`).

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| HS1 | a **complex manifold** is $(M,\mathcal{O}_M)$ locally isomorphic to $(\mathbb{C}^N,\mathcal{O}_{\mathbb{C}^N})$; a **quasi-complex manifold** is $(M,J)$ with $J$ a $(1,1)$-tensor field, $J_p^2 = -\mathrm{id}$ on $T_pM$ | Viviani Def. 2.1 | Mathlib `IsManifold` over `𝓘(ℂ, E)`, `TangentSpace`, **`ContMDiffSection`** (`Geometry/Manifold/VectorBundle/ContMDiffSection.lean`) and the hom-bundle of `.../VectorBundle/Hom.lean`: $J$ is a smooth section of $\mathrm{End}(TM)$ with $J\circ J = -\mathrm{id}$, and every piece of that sentence is in the pinned tree.  ATLAS has the pointwise version without smoothness — see the third sweep |
| HS2 | **Newlander–Nirenberg**: $J$ is induced by a complex structure iff $[JX,JY] = J[JX,Y]+J[X,JY]+[X,Y]$ for all vector fields, and then the complex structure is unique | Viviani Thm. 2.2, via Helgason VIII.1.2 | HS1; **absent** |
| HS3 | a **Hermitian structure** on $(M,J)$: equivalently a Hermitian metric $h$, a $J$-compatible Riemannian metric $g$, or a $J$-compatible positive $2$-form $\omega$, related by $g = \mathrm{Re}\,h = \omega(\cdot,J\cdot)$ and $\omega = -\mathrm{Im}\,h = g(J\cdot,\cdot)$ | Viviani Lemma-Def. 2.3 | HS1; Mathlib `Geometry/Manifold/Riemannian/Basic` |
| HS4 | $\mathrm{Aut}(M,J,h)$, the holomorphic isometries; $M$ is **homogeneous** when it acts transitively, and **symmetric** (a **HSM**) when in addition some $p$ carries $s_p\in\mathrm{Aut}$ with $s_p^2=\mathrm{id}$ and $p$ an isolated fixed point | Viviani Def. 2.4 | HS3 |
| HS5 | $s_p$ is the unique automorphism with $s_p(p)=p$ and $ds_p = -\mathrm{id}_{T_pM}$, hence the geodesic symmetry; a HSM is geodesically complete and $(M,J,\omega)$ is **Kähler** | Viviani Rmk. 2.5, via Helgason VIII.4.1 | HS4; geodesics, Kähler — **absent from Mathlib** |
| HS6 | Euclidean, irreducible, non-Euclidean, compact and non-compact **type**; the decomposition theorem $M = M_0\times M_-\times M_+$, unique, with $M_\pm$ simply connected | Viviani Def. 2.7, Thm. 2.9, via Helgason VIII.4.4–5.5 | HS4 |
| HS7 | the **rank** of a non-Euclidean HSM is the maximal dimension of a flat totally geodesic submanifold; it equals the dimension of any maximal $\mathbb{R}$-split torus of $G$ | Viviani Def. 2.10, Prop. 2.13 | HS5, HS6, AG3 |
| HS8 | $\mathrm{Aut}(M)^o$ is a semisimple **adjoint** Lie group and $\mathrm{Stab}(o)$ compact with $\mathrm{Fix}(\sigma)^o\subseteq\mathrm{Stab}(o)\subseteq\mathrm{Fix}(\sigma)$ for $\sigma = s_o(-)s_o$; $[g]\mapsto g\cdot o$ is a diffeomorphism $\mathrm{Aut}(M)^o/\mathrm{Stab}(o)\to M$; and $s_o$ lies in the identity component of the centre of $\mathrm{Stab}(o)$ | Viviani Thm. 2.11, via Helgason IV.3.3, VIII.4.5 | HS4; Mathlib `LieGroup`; **no semisimple Lie groups, no Cartan involution** |
| HS9 | the **Harish-Chandra embedding** $i_{HC} : M\hookrightarrow\mathfrak{p}_+$ and the **Borel embedding** into $G_\mathbb{C}/(P_-\rtimes K_\mathbb{C})$, a homogeneous projective variety; $i_{HC}$ is an open holomorphic embedding and $j$ a Zariski-open embedding | Viviani Thm. 2.22, via Helgason VIII.7 or Satake II.4 | HS8, AG4; complexification of a Lie group — **absent from Mathlib** |
| HS10 | bounded, homogeneous, symmetric and irreducible **domains**; $i_{HC}(M)$ is a bounded symmetric domain, and $M\mapsto i_{HC}(M)$, $D\mapsto (D,J_D,h_D)$ are mutually inverse bijections preserving irreducibility | Viviani Def. 2.23, Thm. 2.25, Thm. 2.30 | HS9 |
| HS11 | **boundary component**: an equivalence class in $\overline{D}$ for the relation $p\sim q$ iff $p$ and $q$ are joined by a finite chain of holomorphic disks $\lambda_i:\Delta\to\overline{D}$ with consecutive images meeting; and $F_2\le F_1$ iff $F_2\subseteq\overline{F_1}$ | Viviani Def. 4.1 | HS10 |
| HS12 | $\overline{D} = \coprod_{F\le D}F$ and $G = \mathrm{Hol}(D)^o$ preserves it; each $F$ is itself a HSM of non-compact type, $F\subset\langle F\rangle$ **is** its Harish-Chandra embedding and $F\subset F^c$ its Borel embedding, with the square of inclusions Cartesian; $\le$ is transitive; and boundary components of a product are products | Viviani Thm. 4.2, citing AMRT III.3.3 | HS11 |
| HS13 | $N(F) = \{g\in G : gF = F\}$; and $F\mapsto N(F)$ is a **bijection** from the boundary components of $D = D_1\times\cdots\times D_s$ onto the subgroups $P_1\times\cdots\times P_s$ with each $P_i$ either $G_i$ or a **maximal parabolic subgroup** of $G_i$ | Viviani Def. 4.4, Thm. 4.5, citing AMRT III.3.9 | HS12, AG4, AG5 |
| HS14 | the **5-term decomposition**: $N(F) = \{g : \lim_{t\to0}w_F(t)gw_F(t)^{-1}$ exists$\}$ for a one-parameter subgroup $w_F$; $N(F)^o = Z(w_F)^o\ltimes W(F)$ with $W(F)$ the unipotent radical, 2-step, $0\to U(F)\to W(F)\to V(F)\to 0$; and $Z(w_F)^o = G_h(F)\cdot G_l(F)\cdot M(F)$ modulo finite subgroups, $M(F)$ compact semisimple, $G_h(F)/Z\cong\mathrm{Aut}(F)^o$, $G_l(F)$ reductive without compact factors | Viviani Thm. 4.8, citing AMRT III.3.7, 3.10, §4.1 | HS13, HS6 |
| HS15 | $N(F)^o$ acts transitively on $D$; $G_h(F)$ has orbit $F$ through $o_F$ with stabilizer $K_h(F)$, so $G_h(F)/K_h(F)\cong F$; and $G_l(F)$ acting on $U(F)$ by conjugation has an open **cone** $C(F)$ as orbit, with $G_l(F)/K_l(F)\cong C(F)$ | Viviani Prop. 4.9, Thm. 4.10, citing AMRT III.4.1, 4.6 | HS14 |
| HS16 | $C(F)$ is a **symmetric cone** — homogeneous and self-dual — hence classified by a Euclidean Jordan algebra; and $D$ has the Siegel-domain-of-the-third-kind presentation $D\cong\{(x,y,z)\in U(F)_\mathbb{C}\times\mathbb{C}^k\times F : \mathrm{Im}\,x - h_z(y,y)\in C(F)\}$ | Viviani Def. 4.16, Thm. 4.26, Cor. 4.15 | HS15; Mathlib has Jordan rings (`Algebra/Jordan/Basic.lean`) and convex cones with duals, but **no trace form, no Euclidean Jordan algebra, no symmetric-cone classification** |

**HS13 is what BB3 and D3 are really made of, and it is not what D1 says.**  A
boundary component is defined by chains of holomorphic disks (HS11), not as a
maximal connected complex analytic subset; Viviani's Theorem 4.2 then makes each
one a bounded symmetric domain in its own right.  The bijection onto maximal
parabolic subgroups is a theorem (HS13), and it is the *real* form of what D3
states with stabilizers and what BB5 states over $\mathbb{Q}$.  Rationality is a
further condition on top of HS13, and that is stratum AG.

**D1's phrase "maximal connected complex analytic subsets" is a third
description**, and this graph has now seen three: Sterk's, Scattone's via
Baily–Borel, and Viviani's.  Whether they agree is an audit point, not a
substitution: nothing read here proves that the disk-chain classes are the
maximal analytic subsets.

HS1–HS5 are where the analytic substrate runs out.  Mathlib carries complex
manifolds only as `IsManifold` over a model with corners on $\mathbb{C}^n$, and
`Geometry/Manifold/Complex.lean`'s own header says "There is a whole theory to
develop here"; there is no almost-complex structure, no integrability, no
geodesic, no Kähler form, and no semisimple Lie group.  Every row of stratum HS
is greenfield.

#### Stratum AF — the automorphic forms BB8 and D7 rest on

BB8 is Baily–Borel's Theorem 10.11, and its "next dependency" read "BB7;
automorphic forms".  Everything under that phrase is Baily–Borel Part II and
§§9–10, read from `Z9PM5MMD`.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| AF1 | an **automorphy factor** for $H$ on a complex manifold $M$ with values in a complex Lie group $Q$: a map $\mu : M\times H\to Q$, holomorphic in $x$ for fixed $h$, satisfying the cocycle identity; the jacobian and its determinant $J(x,h)$ are automorphy factors, and the **canonical** one $\mu_b(x,g) = (e^x c_b g c_b^{-1})_0$ belongs to the unbounded realization $S_b$ | Baily–Borel 1.8 | HS9 |
| AF2 | functions of **type $\rho$** and of **finite type** with respect to $K$; the universal enveloping algebra as right-invariant differential operators, its centre $\mathcal{Z}(\mathfrak{g})$ as the bi-invariant ones, and **$\mathcal{Z}(\mathfrak{g})$-finiteness** | Baily–Borel 5.1, 5.2 | HS8; universal enveloping algebras — Mathlib `Algebra/Lie/UniversalEnveloping` |
| AF3 | Harish-Chandra's lemma: a $C^\infty$, $K$-finite, $\mathcal{Z}(\mathfrak{g})$-finite $f$ satisfies $f = f * \alpha$ for some conjugation-invariant $\alpha\in C_c^\infty(U)$ | Baily–Borel 5.3, citing Harish-Chandra | AF2 |
| AF4 | **Theorem 5.4**: for $\Gamma$ discrete in $H$ and $f\in L^1(H)\otimes V$ that is $\mathcal{Z}(\mathfrak{g})$-finite and $K$-finite on the right, the **Poincaré series** $p_f(g) = \sum_{\gamma\in\Gamma}f(g\gamma)$ and $p_{\|f\|}$ converge absolutely and uniformly on compacta and are bounded | Baily–Borel 5.4 | AF3 |
| AF5 | Theorem 6.2 and the **Poincaré–Eisenstein series** attached to a rational boundary component; Theorem 7.2: there is $l_0$ such that for every positive multiple $l$ of $l_0$ the series $E_{\varphi,l,\Gamma}\circ g$ converges absolutely and uniformly on compacta | Baily–Borel 6.2, 7.2 | AF4, BB4 |
| AF6 | Theorem 7.8: the growth estimate for $E$ on a **truncated Siegel domain** adapted to a rational boundary component | Baily–Borel 7.8 | AF5, Rt2 |
| AF7 | the operator $\Phi_F$; **Theorem 8.6**: a P–E series adapted to $F$ of weight $l$ is an **integral automorphic form**, $\Phi_{F^*}E = 0$ when $\dim F^*\le\dim F$ and $F^*\not\subset F\cdot\Gamma$, and $\Phi_F$ maps the module of P–E series adapted to $F$ onto the module of Poincaré series for $\Gamma(F)$ | Baily–Borel 8.2–8.6 | AF5 |
| AF8 | **integral automorphic form** (8.3, 8.4): $\omega$ of weight $l$ for $\Gamma_x$ on $X\cap N(x)$ is integral when it **extends** to an automorphic form on $F'\cap N(x)$ for every rational boundary component $F'$ meeting the good neighbourhood $N(x)$ | Baily–Borel 8.3, 8.4 | AF1, BB7 |
| AF9 | **Proposition 8.8, the separation statement**: for rational boundary components $F$, $F'$ with $\dim F\ge\dim F'$ and either $F = F'$ or $F\not\subset F'\cdot\Gamma$, and $x\in F$, $y\in F'$ inequivalent under $\Gamma$, there is $l_0$ such that for every multiple $l$ there is an integral automorphic form $E$ with $\Phi_F E(x)\ne0$ and $\Phi_{F'}E(y) = 0$ | Baily–Borel 8.8 | AF7 |
| AF10 | **Theorem 9.2, the analyticity criterion**: for $V$ a locally compact second-countable space, a locally finite disjoint union of irreducible normal analytic spaces $V_i$, the sheaf of $\mathcal{Q}$-functions makes $V$ an analytic space provided (i) each $V_{(d)}$ is closed with $V_0$ dense of full dimension, (ii) each point has a fundamental system of neighbourhoods meeting $V_0$ connectedly, (iii) the $\mathcal{Q}$-functions restrict to the structure sheaf of each $V_i$, and (iv) they separate points locally | Baily–Borel 9.1, 9.2 | Mathlib `Topology/Sheaves/`, `AnalyticOn`, `TopologicalSpace`, `SecondCountableTopology`, `LocallyCompactSpace` — the hypotheses of the criterion — with the normal analytic *space* the thing to define over them.  `BochaoKong/nullstellensatz`'s `LocalComplexGeometry` (local biholomorphisms, Weierstrass preparation) is the nearest read development and is the local theory |
| AF11 | 10.1–10.2: $V^* = X^*/\Gamma$ is the disjoint union of finitely many $V_i = F_i/\Gamma(F_i)$, each an irreducible normal analytic space, so 9.1 applies; and a quotient $\omega/\omega'$ of integral automorphic forms of equal weight with $\omega'$ nonvanishing is a $\mathcal{Q}$-function | Baily–Borel 10.1, 10.2 | AF8, AF10, D6 |
| AF12 | **Theorem 10.11 (= BB8)**: there are a weight $l$ and finitely many integral automorphic forms $E_i$ of weight $l$ whose extensions to $X^*$ never vanish simultaneously, and the associated map $V^*\to\mathbf{P}(N,\mathbb{C})$ is an isomorphism onto a **normally projective** subvariety | Baily–Borel 10.11 | AF9, AF11 |
| AF13 | Theorem 10.14: if $G$ has no normal $\mathbb{Q}$-subgroup of dimension 3, the direct image $i_*\mathcal{Q}_\rho$ is an algebraic coherent sheaf, the space of automorphic forms of type $\tilde\xi_\rho$ is **finite dimensional**, and the ring of automorphic forms of positive weight is **finitely generated** | Baily–Borel 10.14 | AF12 |

**AF9 is what makes the boundary complex a compactification rather than a
quotient.**  It is the statement that automorphic forms separate boundary
components of different dimension, and it is exactly the separation condition
(iv) that AF10 needs.  The strata this graph counts are the $V_i$ of AF11, and
the finiteness of that list is where "five and nine" acquires its meaning as a
statement about a projective variety.

$G$ here is $O(L_-)$, of dimension 66, so AF13's hypothesis is satisfied and the
ring of automorphic forms is finitely generated — worth recording since Sterk's
Chapter 3 works with that ring.

Substrate: Mathlib has universal enveloping algebras (`Algebra/Lie/
UniversalEnveloping`) and modular forms for $\mathrm{SL}_2(\mathbb{Z})$, and
nothing else on this list: no automorphy factor, no Poincaré series, no normal
analytic space, no coherent sheaf on one.  `CBirkbeck/ModularForms_Lean4` and
`loefflerd/ModularFormDimensions` are the nearest registry entries and are about
the rank-one case.

### Stratum Cl — the classical inputs Chap. 2 cites

The sweep for inputs the graph had left implicit, done over Chap. 2 rather than
for Borel alone.  Each is cited by Sterk and none was a node.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| Cl1 | = E6.  Horikawa I Thm 5.1: there exists an isometry $\mu : H^2(X;\mathbb{Z}) \to L$ with $I \circ \mu = \mu \circ I^*$ — **this is what makes $L_-$ the anti-invariant eigenlattice of the involution, so it is what ties the Gram matrix to the geometry** | Horikawa, *On the periods of Enriques surfaces I* (`6ZXI2FJ4`), Thm 5.1, via Sterk (2.1) | E2, E3 |
| Cl2 | = E10.  Horikawa II Thm 3.1: the statement about $R_- = \{x \in L_- : (x,x) = -2\}$ and the divisor $D_V/\Gamma$ — **tail not transcribed** | Horikawa, *On the periods of Enriques surfaces II* (`RQ2EG4F7`), Thm 3.1, via Sterk (2.15)ff | Cl1, A6a |
| Cl3 | = E9.  The global Torelli theorem for $K3$ surfaces, in the form used at (2.14): an isometry of $H^2$ preserving the relevant structure is induced by an isomorphism of surfaces | Barth–Peters–Van de Ven, *Compact Complex Surfaces* (`VQUIPQ4Y`), Chap. VIII, via Sterk (2.14) | E6 |
| Cl4 | the faithfulness of the representation of $\mathrm{Aut}(X)$ on $O(H^2(X;\mathbb{Z}))$, used at (2.14) to descend $\tilde f$ | Sterk (2.14) | E2 |
| Cl5 | = E11.  Kodaira’s projectivity criterion, used at (2.2) to conclude that an Enriques surface with a line bundle of positive self-intersection is projective | Barth–Peters–Van de Ven (`VQUIPQ4Y`), Chap. IV Thm 5.2, via Sterk (2.2) | E1 |
| Cl6 | Nikulin 1.13.2 and 1.14.2, as cited at (2.x) — the same nodes as Nk4, Nk5 | Sterk, citing Nikulin 1980 | Nk4, Nk5 |

Cl1 is the load-bearing one for this graph, and it was invisible: without it the
development can introduce $L_-$ by a Gram matrix but cannot say it is the
eigenlattice of anything.  Every earlier version of the Lean definitions did
exactly that.

Chapter 3's classical inputs — Meyer's theorem via Serre, Zariski's main
theorem, Riemann's extension theorem, Chow's theorem — are **not** listed as
nodes, because the goal names the Baily–Borel boundary complex and Chapter 3
proves a different theorem, the semi-toric compactification.  That exclusion is
valid under `FDC-08` only as long as the goal stays as stated, and it is
recorded here rather than left silent.

### Stratum Nk, from Nikulin 1980 — what A2, A3, F1.11, F1.12, F3.3 and Cl6 rest on

Read from Nikulin, *Integral symmetric bilinear forms and some of their
applications* (`TTY9FFJS`), §1.  Three of the graph's rows cited theorem numbers
taken from Scattone and Sterk; the statements have hypotheses those rows had
dropped.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| Nk1 | $A_q$ (resp. $A_b$): the finite abelian group carrying the quadratic form $q$ (bilinear form $b$); $\ell(A)$ is the minimal number of generators of $A$ | Nikulin §1, 9° | F1.2 |
| Nk2 | superseded — decomposed as stratum Pa | Pa1–Pa8 |
| Nk3 | **Theorem 1.10.1** (existence): an even lattice with invariants $(t_{(+)},t_{(-)},q)$ exists **iff** simultaneously (1) $t_{(+)}-t_{(-)} \equiv \operatorname{sign} q \pmod 8$; (2) $t_{(+)},t_{(-)} \ge 0$ and $t_{(+)}+t_{(-)} \ge \ell(A_q)$; (3) $(-1)^{t_{(-)}}\lvert A_q\rvert \equiv \operatorname{discr} K(q_p)$ … — **condition (3) not fully transcribed** | Nikulin Thm 1.10.1 | Nk1, Pa4 |
| Nk4 | **Theorem 1.13.2** (uniqueness): an even lattice $S$ with invariants $(t_{(+)},t_{(-)},q)$ is unique if simultaneously (1) $t_{(+)}\ge 1$, $t_{(-)}\ge 1$, $t_{(+)}+t_{(-)}\ge 3$; (2) for each $p\ne 2$, either $\operatorname{rk} S \ge 2+\ell(A_{q_p})$ or $q_p \cong q^{(p)}_{\theta_1}(p^k)\oplus q^{(p)}_{\theta_2}(p^k)\oplus q_p'$; (3) for $p=2$, either $\operatorname{rk} S \ge 2+\ell(A_{q_2})$, or $q_2 \cong u^{(2)}_+(2^k)\oplus q_2'$, or $q_2 \cong v^{(2)}_+(2^k)\oplus q_2'$, or … — **the final alternative not transcribed** | Nikulin Thm 1.13.2 | Nk1, Pa4, Nk3 |
| Nk5 | **Theorem 1.14.2**: for $T$ even and **indefinite** with (a) $\operatorname{rk} T \ge \ell(A_{T_p})+2$ for all $p\ne 2$, and (b) if $\operatorname{rk} T = \ell(A_{T_2})$ then $q_{T_2}\cong u^{(2)}_+(2)\oplus q_2'$ or $v^{(2)}_+(2)\oplus q_2'$ — **the genus of $T$ contains only one class, and $O(T)\to O(q_T)$ is surjective** | Nikulin Thm 1.14.2 | Nk1, Pa4, F3.1 |

**A3 was stated without its hypotheses.**  It read "$L_-$ is determined up to
isometry by its signature $(2,10)$ and its discriminant form", cited to 1.13.2.
The theorem is conditional: three numbered conditions, of which the first —
$t_{(+)}\ge 1$, $t_{(-)}\ge 1$, $t_{(+)}+t_{(-)}\ge 3$ — is satisfied by
$(2,10)$, while (2) and (3) are conditions on $\operatorname{rk} S$ against
$\ell(A_{q_p})$ at each prime and must be **checked for $L_-$**, not assumed.
That check is itself a node, and it is not yet written.

**Nk5 is Scattone's Theorem 3.3.1** and is what A2 ("$G = O(L_-)$") rests on:
surjectivity of $O(T)\to O(q_T)$ holds under a rank condition, and Sterk's A2 is
an instance of it whose hypothesis needs verifying for $L_-$.  Scattone states
the rank condition as $\operatorname{rk} L > \ell(G_L)+2$; Nikulin's is
$\operatorname{rk} T \ge \ell(A_{T_p})+2$ per odd prime plus a separate
condition at $2$.  **They are not the same condition, and they disagree on
$L_-$**: Nikulin's holds and Scattone's fails.  Computed under stratum Ni below.

Nk2 is where this branch descends into $p$-adic lattice theory, and neither it
nor $\ell(A)$ has any Mathlib substrate.

### Stratum Pa — the $p$-adic layer under Nk2, F3.1 and F3.2

Read from Nikulin §1, 8°–9°.  This is what "the canonical $p$-adic forms"
abbreviated, and it is where the genus and every one of Nikulin's numbered
theorems actually bottom out.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| Pa1 | $\mathrm{qu}(\mathbb{Z}_p)$, $\mathrm{qu}(\mathbb{Z})$, $\mathrm{bil}(\mathbb{Z})$: the semigroups of quadratic and bilinear forms in which the relations below are stated | Nikulin §1, 8° | Mathlib `PadicInt` and `Padics`; and for the semigroup operation `QuadraticMap.prod` with `Isometry.inl`/`inr` (`QuadraticForm/Prod.lean`) modulo `QuadraticMap.IsometryEquiv` — **not** the `AddCommMonoid (QuadraticMap R M N)` instance, which adds two forms on one module pointwise |
| Pa2 | $K^{(p)}_\theta(p^k)$: the one-dimensional $p$-adic lattice with matrix $\langle\theta p^k\rangle$, $k\ge 0$ and $\theta\in\mathbb{Z}_p^*$ taken mod $(\mathbb{Z}_p^*)^2$ | Nikulin §1, 8° | Pa1 |
| Pa3 | $U^{(2)}(2^k)$ and $V^{(2)}(2^k)$: the two-dimensional 2-adic lattices with matrices $\begin{pmatrix}0&2^k\\2^k&0\end{pmatrix}$ and $\begin{pmatrix}2^{k+1}&2^k\\2^k&2^{k+1}\end{pmatrix}$, $k\ge 0$ | Nikulin §1, 8° | Pa1 |
| Pa4 | $q^{(p)}_\theta(p^k)$, $u^{(2)}_+(2^k)$, $v^{(2)}_+(2^k)$: the discriminant-quadratic forms of Pa2 and Pa3 for $k\ge 1$; and $b^{(p)}_\theta(p^k)$, $u^{(2)}_-$, $v^{(2)}_-$ their bilinear forms | Nikulin §1, 8° | Pa2, Pa3, F1.10 |
| Pa5 | **Proposition 1.8.2**: the relations among these in $\mathrm{qu}(\mathbb{Z}_p)$, $\mathrm{qu}(\mathbb{Z})$ and $\mathrm{bil}(\mathbb{Z})$ — (a) $K^{(p)}_\theta(p^k)^2 \simeq K^{(p)}_{\theta'}(p^k)^2$ for $p\ne2$; (b) $U^{(2)}(2^k)^2\simeq V^{(2)}(2^k)^2$; (c)–(k) the remaining identities — **the full list is not transcribed** | Nikulin Prop. 1.8.2 | Pa4 |
| Pa6 | Propositions 1.8.1 and 1.8.3, used in the canonical-decomposition arguments — **located, not transcribed** | Nikulin Props. 1.8.1, 1.8.3 | Pa4 |
| Pa7 | $\ell(A)$, the minimal number of generators of a finite abelian group, and $\lvert A\rvert$ its order | Nikulin §1, 9° | Nk1 |
| Pa8 | **Theorem 1.9.1**: for $q_p\in\mathrm{qu}(\mathbb{Z})_p$ there is a **unique** $p$-adic lattice $K(q_p)$ of rank $\ell(A_{q_p})$ with discriminant form $q_p$ — **except** when $p = 2$ and $q_2 = q^{(2)}_\theta(2)\oplus q_2'$, where there are exactly **two**, $K_{\alpha_1}(q_2)$ and $K_{\alpha_2}(q_2)$, with $\operatorname{discr} = \alpha_i\lvert A_{q_2}\rvert(\mathbb{Z}_2^*)^2$ and $\alpha_1\alpha_2 = 5(\mathbb{Z}_2^*)^2$ | Nikulin Thm. 1.9.1 | Pa5, Pa6, Pa7 |
| Pa9 | **Corollary 1.9.3, the canonical decomposition**: every $p$-adic lattice (even when $p=2$) has a unique expression $K_1^{(p)}(1)^{t_p-v_p}\oplus K_{\theta_p}^{(p)}(1)^{v_p}\oplus K(q_p)$ with $0\le v_p\le1$ (three cases, according to $p$ and whether $q_2$ has a $q^{(2)}_\theta(2)$ summand); **in particular $\operatorname{rk}K_p$, $\operatorname{discr}(K_p\otimes\mathbb{Q}_p)$ and $q_{K_p}$ determine $K_p$** | Nikulin Cor. 1.9.3 | Pa8 |
| Pa10 | **Corollary 1.9.4**: the invariants $(t_{(+)},t_{(-)},q)$ determine the **genus** of an even lattice | Nikulin Cor. 1.9.4 | Pa9 |
| Pa11 | **Theorem 1.9.5**: an isomorphism $q_{K_p}\to q_{K'_p}$ of the discriminant forms of isomorphic $p$-adic lattices is induced by an isomorphism $K_p\to K'_p$; **Corollary 1.9.6**: $O(K_p)\to O(q_{K_p})$ is surjective; **Corollary 1.9.7**: an isomorphism between two primitive sublattices of a unimodular $p$-adic lattice extends to an automorphism of it | Nikulin Thm. 1.9.5, Cors. 1.9.6, 1.9.7 | Pa9, Ni4 |

Pa5 is the computational engine: every one of Nikulin's classification proofs
proceeds by reducing to these relations, and the graph had been carrying it as
the phrase "the canonical $p$-adic forms".

**Pa7 said this branch descends into strong approximation for algebraic groups.
It does not.**  Nikulin's 9° is *titled* "The strong approximation theorem in the
even case", and the graph took the title for the content.  What the section
actually proves is Theorem 1.9.1 and its corollaries: a $p$-adic classification
of the minimal-rank lattice realizing a discriminant form, with a single
exceptional 2-adic case admitting exactly two.  No algebraic group appears in
any numbered statement.  Where strong approximation does enter Nikulin's proofs
is 1.14.2, which cites his reference [13]; that citation is unread, and it is
where the branch would descend if it descends at all.

**Pa10 is F3.2, and this is its proof.**  "Same genus iff same signature and
same discriminant form" — the row the F-stratum calls the bridge the whole graph
turns on — is Corollary 1.9.4, and it follows from the canonical decomposition
Pa9, which follows from Theorem 1.9.1.  F3.2 cited Scattone, who states it; the
descent ends here.

**Pa11 is the local model of the two theorems A2 rests on.**  Corollary 1.9.6 is
surjectivity of $O(K_p)\to O(q_{K_p})$ over $\mathbb{Z}_p$, which is what
Nk5/Nikulin 1.14.2 globalizes, and Corollary 1.9.7 is the local Witt statement
Ni8 globalizes.  Remark 1.9.8 attributes the $p\ne2$ half to Durfee.

Pa1–Pa4 are explicit matrices and are terminal against Mathlib's $\mathbb{Z}_p$
and quadratic forms.

### Stratum Ni, from Nikulin §1 — what F5.6, F1.12 and Ni-dependent rows rest on

F5.6 ended with "Nikulin's primitive-embedding theory", and F1.12 recorded a
Nikulin theorem whose conclusion was "not transcribed".  Read from Nikulin
(`TTY9FFJS`), §1, subsections 5°, 6°, 12°, 14° and 15°.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| Ni1 | an embedding $S\subset M$ is **primitive** when $M/S$ is free; two primitive embeddings $S\hookrightarrow M$, $S\hookrightarrow M'$ are **isomorphic** when some isomorphism $M\cong M'$ restricts to the identity on $S$, and define **isomorphic primitive sublattices** when some isomorphism carries $S$ to itself | Nikulin §1, 5° | F1.8 |
| Ni2 | **Proposition 1.5.1**: a primitive embedding of an even $S$ into an even lattice with discriminant form $q$ and orthogonal complement $K$ is determined by a pair $(H,\gamma)$ — $H\subseteq A_S$ a subgroup, $\gamma : H\to A_K$ a monomorphism with $q_K\circ\gamma = -q_S|H$ and $\big((q_S\oplus q_K)|\Gamma_\gamma^\perp\big)/\Gamma_\gamma \simeq q$, where $\Gamma_\gamma$ is the pushout of $\gamma$ in $A_S\oplus A_K$.  Two pairs give **isomorphic embeddings** iff $H = H'$ and $\gamma,\gamma'$ are conjugate by an automorphism of $K$, and **isomorphic sublattices** iff $\gamma\circ\overline\varphi = \overline\psi\circ\gamma'$ for some $\varphi\in O(S)$, $\psi\in O(K)$ | Nikulin Prop. 1.5.1 | Ni1, F1.10 |
| Ni3 | Corollary 1.5.2: an isomorphism $\varphi : S_1\cong S_2$ of primitive sublattices of $M$ extends to an automorphism of $M$ **iff** there is $\psi : K_1\cong K_2$ between the complements with $\overline\psi\circ\gamma^M_{S_1,K_1} = \gamma^M_{S_2,K_2}\circ\overline\varphi$ | Nikulin Cor. 1.5.2 | Ni2 |
| Ni4 | **Proposition 1.6.1**: into an even **unimodular** lattice, a primitive embedding of $S$ with complement $K$ is determined by an isomorphism $\gamma : q_S\to -q_K$, with the same two equivalence criteria | Nikulin Prop. 1.6.1 | Ni2 |
| Ni5 | $S\perp K$: two even lattices are **orthogonal** when there is an even unimodular $L$ and a primitive $S\subset L$ with $(S)^\perp_L\cong K$ | Nikulin §1, 6° | Ni4 |
| Ni6 | Corollary 1.12.3 (existence): a primitive embedding of $S$ with invariants $(t_{(+)},t_{(-)},q)$ into an even unimodular lattice of signature $(l_{(+)},l_{(-)})$ exists if $l_{(+)}-l_{(-)}\equiv0\pmod 8$, $l_{(\pm)}-t_{(\pm)}\ge0$, and $l_{(+)}+l_{(-)}-t_{(+)}-t_{(-)} > \ell(A_q)$ | Nikulin Cor. 1.12.3 | Nk3, Ni4 |
| Ni7 | **Theorem 1.12.4**: *every* even lattice of signature $(t_{(+)},t_{(-)})$ embeds primitively into some even unimodular lattice of signature $(l_{(+)},l_{(-)})$ **iff** $l_{(+)}-l_{(-)}\equiv0\pmod8$, $t_{(+)}\le l_{(+)}$ and $t_{(-)}\le l_{(-)}$ | Nikulin Thm. 1.12.4 | Ni6 |
| Ni8 | **Theorem 1.14.4, the analogue of Witt's theorem**: for $M$ even of signature $(t_{(+)},t_{(-)})$ and $L$ even unimodular of signature $(l_{(+)},l_{(-)})$ there is a **unique** primitive embedding $M\hookrightarrow L$ provided (1) $l_{(\pm)}-t_{(\pm)} > 0$; (2) $l_{(+)}+l_{(-)}-t_{(+)}-t_{(-)} \ge 2+\ell(A_{M_p})$ for every $p\ne2$; (3) if $l_{(+)}+l_{(-)}-t_{(+)}-t_{(-)} = \ell(A_{M_2})$ then $q_M\cong u^{(2)}_+(2)\oplus q'$ or $v^{(2)}_+(2)\oplus q'$.  Remark 1.14.5: (3) is automatic when $A_M\cong(\mathbb{Z}/2)^3\oplus A'$ | Nikulin Thm. 1.14.4, Rmk. 1.14.5 | Ni4, Nk5 |
| Ni9 | Remark 1.14.6: for $M$ negative definite, generated by vectors of square $-2$ and primitively embedded in $E_8$, the complement $K\cong(M)^\perp_{E_8}$ has **one class in its genus** and $O(K)\to O(q_K)$ is **surjective**; the embedding $M\hookrightarrow E_8$ is unique up to isomorphism | Nikulin Rmk. 1.14.6 | Ni8, F4.1 |
| Ni10 | **Proposition 1.15.1** (the non-unimodular case): primitive embeddings of $S$ into an even lattice with invariants $(m_{(+)},m_{(-)},q)$ are determined by tuples $(H_S,H_q,\gamma;K,\gamma_K)$ — $H_S\subseteq A_S$ and $H_q$ subgroups, $\gamma : q_S|H_S\to q|H_q$ an isomorphism preserving the restricted forms, $K$ an even lattice with invariants $(m_{(+)}-t_{(+)},\,m_{(-)}-t_{(-)},\,-\delta)$ where $\delta\cong\big((q_S\oplus(-q))|\Gamma_\gamma^\perp\big)/\Gamma_\gamma$ for $\Gamma_\gamma$ the pushout of $\gamma$, and $\gamma_K : q_K\xrightarrow{\ \sim\ }-\delta$ | Nikulin Prop. 1.15.1 | Ni2, Nk3 |

**F5.6 is Ni4 counted.**  Scattone's "each embedding is unique up to equivalence
except the two distinct embeddings into $E_8+D_{16}$" is a count of the
isomorphisms $\gamma : q_{D_7}\to -q_K$ modulo $\mathrm{Aut}(K)$, by Ni4.  That
is why the nine of C11 is eight lattices with one of them contributing twice,
and not a genus-class count: the extra class comes from a second $\gamma$-orbit,
not from a second lattice.

Ni9 is the mechanism behind the $E_8$-specific facts F5.4 uses.

Transcription caution: the extracted text of Prop. 1.15.1 writes the second
subgroup as $H_q\subseteq A_S$, which cannot be right, since $\gamma$ is an
isomorphism onto $q|H_q$; read $H_q\subseteq A_q$.  The row above records the
reading, and the node is not settled until it is checked against print.

#### The Nikulin and Scattone rank conditions differ, and they differ **here**

The Nk stratum recorded that Scattone's Theorem 3.3.1 asks
$\operatorname{rk}L > \ell(G_L)+2$ while Nikulin's Theorem 1.14.2 asks
$\operatorname{rk}T \ge \ell(A_{T_p})+2$ at each odd $p$ plus a separate
condition at $2$, and left "which one the graph needs" open.  Computed for
$L_-$: the Smith normal form of the Gram matrix has elementary divisors
$1,1,2,2,\dots,2$, so $A_{L_-} = (\mathbb{Z}/2)^{10}$, $\ell(A_{L_2}) = 10$ and
$\ell(A_{L_p}) = 0$ for $p$ odd, against $\operatorname{rk} = 12$.

- **Nikulin 1.14.2 applies.**  Condition (a) is $12\ge 0+2$ at every odd prime.
  Condition (b) is hypothetical on $\operatorname{rk}T = \ell(A_{T_2})$, and
  $12\ne10$, so it is **vacuous**.  No 2-adic structure needs checking.
- **Scattone's Theorem 3.3.1 does not.**  It asks $12 > 10+2$, which is false.

So they are **not** the same condition, and A2 — "$G = O(L_-)$", which is
surjectivity of $O(L_-)\to O(q_{L_-})$ together with one class in the genus —
holds by Nikulin's theorem and **not** by Scattone's version of it.  A node
citing Scattone 3.3.1 for A2 would be citing a hypothesis $L_-$ fails.  The
audit point is closed against Scattone's form.

This is the second place where $L_-$ sits exactly on a boundary: A3 needs
Nikulin 1.13.2 rather than Corollary 1.13.3 because $12 > 12$ is false by one,
and A2 needs 1.14.2 rather than Scattone 3.3.1 for the same reason.  Both
margins are one, and both come from $\ell(A_{L_-}) = 10$ against rank 12.

### Stratum Bo, from Borel 1972 — the extension theorem Sterk leans on

Sterk uses this at Chap. 2 §4: "by Borel's extension theorem [Borel 1972].  The
limit point $\bar p(0)$ will be an element of a type II Satake–Baily–Borel
boundary component which we shall determine."  It is how a degenerating family
over a punctured disc acquires a limit *in the compactification*, and it was
missing from this graph entirely.  Borel, *Some metric properties of arithmetic
quotients of symmetric spaces and an extension theorem*, J. Diff. Geometry 6
(1972), 543–560; Zotero `W6PPVK2D`.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| Bo1 | **Theorem A**: $X$ a bounded symmetric domain, $\Gamma$ an arithmetically defined **torsion-free** group of automorphisms, $V^*$ the compactification of $V = X/\Gamma$ of Baily–Borel; then every holomorphic $f : D^{*a}\times D^b \to V$ extends to a holomorphic map $D^{a+b} \to V^*$ | Borel 1972, Thm A | Bo3, BB8 |
| Bo2 | **Theorem 3.7**: for $Z$ a normal hyperbolic space and $f : D^{*a}\times Z \to V$ *locally liftable* holomorphic, $f$ extends to a holomorphic map $D^a \times Z \to V^*$ | Borel 1972, 3.7 | Bo1 |
| Bo3 | Kwack's extension theorem, in the variant Borel uses, and the Kobayashi pseudo-distance making $X$ hyperbolic | Borel 1972 §3, citing Kwack [12] and [9]; Kobayashi [10] | Ky1–Ky3 |
| Bo4 | Theorems B and C: the Siegel-set and arithmetic-group properties Borel proves in §§1–2 and uses in §3.5 | Borel 1972 §§1–2 | Rt1–Rt10 |
| Bo5 | the consequence Borel records: for $S$ an algebraic variety and $h : S \to V$ holomorphic, $h$ is a morphism of algebraic varieties, $V$ carrying its quasi-projective structure | Borel 1972, introduction, citing BB Thm 3.10 | Bo1, BB8 |

**Bo1 assumes $\Gamma$ torsion-free.**  Sterk's $\Gamma$ is not obviously
torsion-free — it contains $-1$ — so either the hypothesis is met by passing to
a subgroup, or Sterk is using the theorem in a form that tolerates torsion.
Borel's own Remark 3.8 notes that when $\Gamma$ has torsion, $V$ need not be
hyperbolically imbedded in $V^*$.  **This is an audit point, not a resolved
one**: the node cannot be stated until it is settled which form Sterk needs.

This stratum sits under Sterk Chap. 2 §4, which the coverage table below
dispositioned out of scope.  That disposition is invalid while the goal names
the period space (`FDC-08`), and Bo1 is the concrete cost of it: a classical
input, with a hypothesis that may not hold, invisible to the graph because the
section using it had been excluded.

### Stratum Rt, from Borel–Harish-Chandra — what Bo4 rests on

Bo4 said "the Siegel-set and arithmetic-group properties Borel proves in §§1–2",
naming a section rather than a statement.  Read from Borel–Harish-Chandra,
*Arithmetic subgroups of algebraic groups* (`BRDFP5YR`), §§1, 4, 6, 7, 9 and 11 —
the paper that established this theory and that Borel 1972 rests on.  Borel 1972's
own §§1–2 remain untranscribed; what follows is the theory they use, from its
source, not a transcription of Borel's versions.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| Rt1 | the **Iwasawa decomposition** $G = K\cdot A\cdot N$ of an open subgroup of a real algebraic reductive group, and $\Sigma$ the simple restricted roots in the ordering making the roots of $\mathrm{ad}_\mathfrak{g}\mathfrak{a}$ in $\mathfrak{n}$ positive; the choice presupposes a Cartan involution $\theta$, a maximal subalgebra on which $\theta = -\mathrm{Id}$, and an ordering | Borel–Harish-Chandra 1.11, 4.1 | HS8; **absent from Mathlib** |
| Rt2 | a **Siegel domain** $\mathfrak{S}_{t,\omega} = K\cdot A_t\cdot\omega$, with $A_t = \{a\in A : \lambda(\log a)\le t\ \forall\lambda\in\Sigma\}$ and $\omega\subset N$ compact; the union of all of them is $G$, and any finite union lies inside one | Borel–Harish-Chandra 4.1 | Rt1 |
| Rt3 | for $a\in A_t$ and $n\in\omega$ the set of conjugates $a\,n\,a^{-1}$ is relatively compact in $N$ | Borel–Harish-Chandra 4.2 | Rt2 |
| Rt4 | for $G$ semisimple every Siegel domain has **finite Haar measure**, computed against $dg = \exp[\sigma(\log a)]\,dk\,da\,dn$ with $\sigma$ the sum of the positive restricted roots | Borel–Harish-Chandra 4.3 | Rt2 |
| Rt5 | $G_\mathbb{Z}$ is discrete in $G_\mathbb{R}$, and its **commensurability class is independent of the $\mathbb{Q}$-embedding** | Borel–Harish-Chandra 6.1 | AG1 |
| Rt6 | the subgroup of $G_\mathbb{Z}$ preserving a lattice $\Gamma\subset V_\mathbb{Q}$ has finite index in $G_\mathbb{Z}$ | Borel–Harish-Chandra 6.2 | Rt5 |
| Rt7 | **Theorem 6.5, the fundamental set**: for $G$ reductive over $\mathbb{Q}$ there are $b_1,\dots,b_m\in\mathrm{SL}(n,\mathbb{Z})$ such that the interior $U$ of $\bigcup_i(a^{-1}\mathfrak{S}b_i)\cap G_\mathbb{R}$ satisfies (i) $G_\mathbb{R} = U\cdot G_\mathbb{Z}$, (ii) $K\cdot U = U$ for a maximal compact $K$, (iii) $U^{-1}U\cap x G_\mathbb{Z} y$ is finite for all $x,y\in G_\mathbb{Q}$; and $G_\mathbb{Z}$ is **finitely generated** | Borel–Harish-Chandra 6.5 | Rt2, Rt6, AG9 |
| Rt8 | Theorem 6.12: the same conclusion for an arbitrary algebraic $\mathbb{Q}$-group | Borel–Harish-Chandra 6.12 | Rt7 |
| Rt9 | Theorem 9.4: $G_\mathbb{R}$ is unimodular and $G_\mathbb{R}/G_\mathbb{Z}$ has **finite invariant measure iff $X_\mathbb{Q}(G^0) = 1$**; for $G$ semisimple this is automatic (Thm. 7.8) | Borel–Harish-Chandra 7.8, 9.4 | Rt4, Rt7 |
| Rt10 | Theorem 11.6: $G_\mathbb{R}/G_\mathbb{Z}$ is **compact iff** $X_\mathbb{Q}(G^0) = 1$ and $G_\mathbb{Q}$ consists of semisimple elements — equivalently (11.8) every unipotent element of $G_\mathbb{Q}$ lies in the radical | Borel–Harish-Chandra 11.6, 11.8 | Rt9 |

**Rt10 is why this graph exists.**  $\Gamma$ is arithmetic in $G = O(L_-)$, which
is $\mathbb{Q}$-isotropic by AG19, so $G_\mathbb{Q}$ contains unipotent elements
outside the radical and the quotient is **not** compact.  The boundary the whole
target describes is the price of that non-compactness; Rt9 says the volume is
nevertheless finite, which is what makes a compactification with a
finite boundary complex possible at all.

Rt7 is the fundamental set Bo4 names, and Rt5 is what lets "$\Gamma$ arithmetic"
be a property of $\Gamma$ rather than of a chosen matrix realization — which
A0's definition of $\Gamma$ by its action on $L_-^*/L_-$ silently uses.

Substrate: nothing.  Iwasawa decompositions, restricted roots, Haar measure on a
Lie group and arithmetic subgroups are all absent; Mathlib has Haar measure on
locally compact groups but no Lie-group structure theory to apply it to here.

### Stratum Ky, from Kiernan–Kobayashi — what Bo3 rests on, and audit point 5

Bo3 said "Kwack's extension theorem, in the variant Borel uses, and the
Kobayashi pseudo-distance making $X$ hyperbolic", with no statement.  Read from
Kiernan–Kobayashi, *Satake compactification and extension of holomorphic
mappings* (`TCZ83KBC`), §§1 and 5 — a paper proving Borel's kind of theorem
from the hyperbolic side, on the same compactification.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| Ky1 | the intrinsic (Kobayashi) pseudo-distance $d_M$ of a complex space; $M$ is **hyperbolic** when $d_M$ is a distance | Kiernan–Kobayashi §1 (1), after Kobayashi 1970 | HS1; **absent from Mathlib** |
| Ky2 | $M\subseteq Y$ is **hyperbolically imbedded** when (1) $M$ is hyperbolic, (2) $\overline M$ is compact in $Y$, and (3) for every $p\in\partial M$ and neighbourhood $U$ of $p$ there is a neighbourhood $V$ with $\overline V\subset U$ and $d_M\big(M\cap(Y-U),\,M\cap V\big) > 0$ | Kiernan–Kobayashi §1 (1)–(3) | Ky1 |
| Ky3 | **Kwack**: a holomorphic $X - A\to M$ extends to $X\to Y$ when $M$ is compact and $X$ is nonsingular; extended by Kobayashi to $X$, $A$ both nonsingular and $M$ not necessarily compact, and by Kiernan to $A$ with normal-crossing singularities.  For singular $X$ the statement is **false**, with counterexamples | Kiernan–Kobayashi §1, citing Kwack 1969, Kobayashi 1970, Kiernan | Ky2 |
| Ky4 | **Kobayashi–Ochiai**: if $M = \mathcal{D}'/\Gamma'$ for an arithmetic $\Gamma'$ and $Y$ is its Satake–Baily–Borel compactification, then $M$ is hyperbolically imbedded in $Y$ | Kiernan–Kobayashi §1, citing Kobayashi–Ochiai 1971 — **that paper not read, and not in the library** | Ky2, BB8 |
| Ky5 | **the torsion clause**: when $\Gamma'$ does not act freely on $\mathcal{D}'$, the distance $d_M$ in conditions (1) and (3) is replaced by the distance $d'_M$ induced from the intrinsic distance $d_{\mathcal{D}'}$ of the domain, and Ky4 holds in that form | Kiernan–Kobayashi §1 parenthesis and Thm. 2 proof, citing Kobayashi–Ochiai | Ky4 |
| Ky6 | **Theorem 1**: for $\mathcal{D}$ symmetric bounded and $\Gamma$ arithmetic, every holomorphic $f : \mathcal{D}/\Gamma\to M$ into a complex space hyperbolically imbedded in $Y$ extends to $\mathcal{D}^*/\Gamma\to Y$ | Kiernan–Kobayashi Thm. 1 | Ky2, BB8 |
| Ky7 | **Theorem 2**: every holomorphic $\mathcal{D}/\Gamma\to\mathcal{D}'/\Gamma'$ that lifts to $\mathcal{D}\to\mathcal{D}'$ extends to the compactifications, and the extension **sends each boundary component into a boundary component** | Kiernan–Kobayashi Thm. 2 | Ky6, Ky5, HS11 |
| Ky8 | the proof of Theorem 2 uses Pyatetzki-Shapiro's topology on $\mathcal{D}^*/\Gamma$ and Borel's theorem that it **coincides** with Baily–Borel's; for Theorem 1 it is enough that it is at least as coarse | Kiernan–Kobayashi §3 | BB7 |

**Ky5 settles audit point 5, and settles it against passing to a subgroup.**  The
graph recorded that Borel's Theorem A assumes $\Gamma$ torsion-free, that Sterk's
$\Gamma$ contains $-\mathrm{id}$ and so is not, and that "the standard repair is
to pass to a neat finite-index subgroup and descend".  Kiernan and Kobayashi say
in one parenthesis what the repair actually is: keep the group, and replace the
intrinsic pseudo-distance of the quotient — which need not be a distance when the
action is not free — by the distance induced from the domain above it.  That is a
change of *metric*, not of *group*, and it is the form of the hyperbolic-imbedding
statement that applies to Sterk's $\Gamma$.

The audit point is therefore **narrowed, not closed**: what remains is to read
Kobayashi–Ochiai 1971 for the modified condition (3) and to check that the
extension Sterk uses — Borel's, over a punctured polydisc — follows from Ky6 in
that form.  Kobayashi–Ochiai, *Satake compactification and the great Picard
theorem*, J. Math. Soc. Japan **23** (1971), 340–350, is not in the library.

Ky7's last clause is worth its own row for a different reason: it says the
extension respects the boundary-component structure, which is the compatibility
D5 and D6 need on the analytic side.

Substrate: nothing.  Mathlib has no Kobayashi pseudo-distance, no hyperbolic
complex space, and no big Picard theorem; the registry has no complex-hyperbolic
corpus.  `kebekus/ProjectVD` covers Nevanlinna value-distribution theory, whose
subject is adjacent — the great Picard theorem is Ky3's ancestor — but it does
not supply these statements.

## Goal

| Node | Statement | Depends on |
| --- | --- | --- |
| G | the boundary complex of the Baily–Borel compactification of $\Omega_-/\Gamma$ — equivalently $\Gamma\backslash\mathcal{T}(G)$ — is the explicit finite graph with five vertices of one type, nine of the other, and the edges of 3.4 | B3, C11, C12, D4, AG17, AG19 |

The two rows the goal sentence needs and did not name are AG17, that
$\dim\Delta_\mathbb{Q}(\mathbf{G}) = r_\mathbb{Q}(\mathbf{G}) - 1$, and AG19,
that $r_\mathbb{Q}$ is $2$ here.  Without them "one-dimensional" is an
assertion, and a graph is the whole boundary complex only because the building
has no higher simplices.

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

**These rows are subjects, not statements, so none is a node.**  They are
placeholders standing where sub-graphs belong, and each is now decomposed:

| Subject | The stratum that carries it |
| --- | --- |
| S1 the discriminant form | F1.7, F1.9, F1.10 |
| S2 $O^*(N)$ | F2.3–F2.5 |
| S3 affine Coxeter and Dynkin diagrams | V10 |
| S4 hyperbolic reflection groups | V1–V13 over Lo1–Lo9 |
| S5 genus theory | F3.1–F3.4 over Pa1–Pa8 |
| S6 reductive groups, buildings, hermitian domains, Baily–Borel | AG1–AG19, HS1–HS16, BB1–BB8, AF1–AF13 |
| S7 the upper half plane | terminal against Mathlib |

So the survey no longer understates the work by an unknown amount; it understates
it by the amount stated in those strata.  The node numbering is independent of
these rows and they are kept only as the index above.

### F2, rewritten from Scattone §§3.6–3.7

Read from Scattone §3.6 *Orthogonal groups* and §3.7 *Elementary
transformations*.  These replace the rows that named the sections without
stating them, and they settle what $O^*$ is — the definition A5, A6 and B1 all
depend on, which was previously an open node saying "locate in Sterk".

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| F2.1 | $\tau : O(L) \to O(G_L)$, the canonical homomorphism to the isometries of the discriminant form | Scattone §3.6 | F1.2, F1.7, **F1.13, F2.14** — its domain and codomain, added when reading showed neither group existed |
| F2.2 | $\tilde O(L) = \ker\tau$, equivalently $\{\phi \in O(L) : \phi v - v \in \mathrm{div}(v)\cdot L \text{ for all } v \in L\}$ | Scattone §3.6 | F2.1, F1.7 |
| F2.3 | the **spinor norm** $\sigma_- : O(L) \to \{\pm 1\}$: writing $\phi = R_{v_1}\cdots R_{v_m}$ as a product of reflections in $O(L_\mathbb{Q})$ (not necessarily integral), $\sigma_-(\phi) = \prod_j\big(-\mathrm{sign}(v_j,v_j)\big)$, i.e. $+1$ exactly when $(v_j,v_j) > 0$ for an even number of the $v_j$.  **Scattone follows Brieskorn [6] and notes this is a modified form of the usual spinor norm** | Scattone §3.6 | F1.1; Cartan–Dieudonné for an **indefinite** rational form — Mathlib has only the positive definite real case, see the terminality note |
| F2.4 | $O_-(L) = \ker\sigma_-$ | Scattone §3.6 | F2.3 |
| F2.5 | **$O^*(L) = \tilde O(L)\cap O_-(L)$** | Scattone §3.6 | F2.2, F2.4 |
| F2.6 | for $v \in R(L)$ and $z \in L^*$, $R_v(z) = z + (v,z)v \in z + L$, so $R_v$ induces the identity on $L^*/L$; hence $O_r(L)\subseteq O^*(L)$, and $O_r(L)\subseteq \hat O_r(L)\subseteq O_-(L)$ | Scattone §3.6 | F2.5 |
| F2.7 | $\tilde O(L)\not\subset O_-(L)$, since it contains the reflections $R_v$ with $(v,v)=2$; consequently $O^*(L)$ has index 2 in $\tilde O(L)$ | Scattone §3.6 | F2.5, F2.6 |
| F2.8 | Lemma 3.6.1: for $L = \langle-2k\rangle\oplus H^2\oplus E_8^2$, $\lvert O(G_L)\rvert = 2^{p(k)}$ with $p(k)$ the number of distinct … — **tail not transcribed** | Scattone Lemma 3.6.1 | F2.1 |
| F2.9 | with 3.6.1: $\tau : O_-(L)\to O(G_L)$ is **surjective** | Scattone §3.6 | F2.8, F2.4 |
| F2.10 | the **elementary (Eichler) transformation**: for $f\in L$ isotropic and $x \perp f$, $E_{f,x} : y \mapsto y + (y,x)f - \tfrac12(x,x)(y,f)f - (y,f)x$; each $E_{f,x}$ is an isometry of $L$ | Scattone §3.7 | F1.1 |
| F2.11 | $\mathcal{E}(L)$, the subgroup generated by the $E_{f,x}$, is **normal** in $O(L)$, since $\phi E_{f,x}\phi^{-1} = E_{\phi f,\phi x}$ | Scattone §3.7 | F2.10 |
| F2.12 | **Lemma 3.7.1 (Eichler)**: $\mathcal{E}(L)\subseteq O^*(L)$ for every even lattice $L$ | Scattone Lemma 3.7.1 | F2.11, F2.5 |
| F2.13 | **Proposition 3.7.3** (= Sterk 2.18 = node A6): for $L$ even containing at least two hyperbolic planes and $v,w$ primitive with $(v,v)=(w,w)$, some $\phi\in\mathcal{E}(L)$ carries $v$ to $w$ **iff** $v^* = w^*$ | Scattone Prop. 3.7.3 | F2.12, F1.2 |
| F2.14 | $O(q)$ **as a group** for a finite quadratic form: the automorphisms of the finite abelian group preserving $q$, under composition; $O(G_L)$ is this at $q = q_L$ | decomposed out of F2.1, whose $\tau$ has this as its codomain and had no definition for it | F1.9, F1.15, F1.13's construction; Mathlib `AddEquiv`, `Subgroup`, `GroupTheory/FiniteAbelian/Basic.lean` |

Three consequences for rows already in the graph.

**F2.5 closes the node that said "locate Sterk's definition of $O^*$".**  It is
$\tilde O(L)\cap O_-(L)$: kernel of the action on the discriminant form,
intersected with kernel of the spinor norm.  A5, A6 and B1 are all statements
about this group, and none of them could be stated before it.

**F2.3 carries a convention warning from the source itself** — Scattone follows
Brieskorn and says outright that this is a *modified* spinor norm.  Any node
stated with "the spinor norm" unqualified would be ambiguous between two
conventions, and the graph earlier had exactly such a row.

**F2.13 is A6.**  Sterk's 2.18 is Scattone's 3.7.3, and the two hypotheses
Sterk's row omitted are visible here: $L$ even with **at least two hyperbolic
planes**, and the criterion is equality of images $v^*$ in the discriminant
group rather than a congruence mod $pN$.

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
| F5.1 | Niemeier's classification: the 24 even unimodular lattices of rank 24, by root system | Scattone (3.5.1), the table of $\mathcal{U}^{24}$ | F4.2 — the same theorem |
| F5.2 | for $E \in I_{2,e}(L)$, the lattice $E^\perp/E$ lies in the genus of $\langle -2k/e^2\rangle \oplus E_8 \oplus E_8$ | Scattone Remark 5.1.4 | F3.1, F3.2 |
| F5.3 | Proposition 6.1.2 at $k=2$: $N \cong D_7$, and the classes are obtained from the primitive embeddings of $N$ into the members of $\mathcal{U}^{24}$ | Scattone Prop. 6.1.2 | F5.1 |
| F5.4 | $D_7 \subset E_8$, $D_7 \not\subset E_7$, $D_7 \not\subset A_m$ for every $m$ | Scattone §6.3 | F4.1, Ni1 |
| F5.5 | hence only eight Niemeier lattices admit such an embedding: $E_8^3$, $E_8{+}D_{16}$, $E_7^2{+}D_{10}$, $D_{24}$, $D_{12}^2$, $D_8^3$, $D_9{+}A_{15}$, $E_6{+}D_7{+}A_{11}$ | Scattone §6.3 | F5.3, F5.4 |
| F5.6 | each embedding is unique up to equivalence **except** the two distinct embeddings into $E_8 + D_{16}$ — which is where the nine comes from | Scattone §6.3 | F5.5, Ni4 |
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

### F1, F3, F4, rewritten from Scattone §§3.1–3.5

Read from Scattone §3.1 *Lattices*, §3.2 *Discriminant-quadratic forms*,
§3.3 *Genera*, §3.4 *The Minkowski–Siegel formula*, §3.5.  These replace the
rows that carried section titles.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| F1.1 | a **lattice** is a finitely generated free abelian group $L$ with a symmetric bilinear form $b : L\times L\to\mathbb{Z}$; $\langle B\rangle$ denotes the lattice with basis $v_1,\dots,v_n$ and $(v_i,v_j)=b_{ij}$; two are isomorphic iff $B' = {}^tABA$ for some $A\in GL(n;\mathbb{Z})$; $O(L)$ is the group of automorphisms | Scattone §3.1 | Mathlib `Module.Free ℤ` with `Module.Finite ℤ` and a `Basis (Fin n) ℤ`, `LinearMap.BilinForm ℤ` with `LinearMap.IsSymm` (`SesquilinearForm/Basic.lean`), `Matrix.toBilin` for $\langle B\rangle$, `LinearMap.BilinForm.toMatrix_comp` for ${}^tABA$, `Matrix.GeneralLinearGroup (Fin n) ℤ`.  $O(L)$ is **F1.13**, split out because no group of isometries exists in the tree |
| F1.2 | the associated quadratic form $q(v)=(v,v)$; $L$ is **even** when $q$ takes even values, equivalently all diagonal entries of $B$ are even | Scattone §3.1 | F1.1 |
| F1.3 | definiteness, and the **signature** $(n_+,n_-)$ as the maximal ranks of positive- and negative-definite sublattices; $L$ is **nondegenerate** when $\mathrm{rk}\,L = n_+ + n_-$, and the index is $\min(n_+,n_-)$ | Scattone §3.1 | F1.1 |
| F1.4 | the **discriminant** $d(L)=\lvert\det((v_i,v_j))\rvert$ over any basis; $L$ is nondegenerate iff $d(L)\ne 0$, **unimodular** when $d(L)=1$; an even unimodular lattice satisfies $n_+\equiv n_-\pmod 8$ | Scattone §3.1 | F1.3 |
| F1.5 | $H = \langle\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\rangle$ and $E_8$ := $\mathbb{Z}^8$ with the **negative** of the $E_8$ Cartan matrix — so Scattone's $E_8$ is negative definite | Scattone §3.1 | F1.4 |
| F1.6 | every even indefinite unimodular lattice is an orthogonal sum of copies of $H$, $E_8$ and $-E_8$, uniquely up to the relation $E_8\oplus(-E_8)\cong H^8$ | Scattone §3.1, citing [31] | F1.5 |
| F1.7 | the **dual** $L^* \subseteq L_\mathbb{Q}$, and the **divisor** $\mathrm{div}(v)=d \iff (v,L)=d\mathbb{Z}$; $L^*$ is spanned by the $v/\mathrm{div}(v)$, and $v^* = v/\mathrm{div}(v) + L \in G_L$ | Scattone §3.1 | F1.4 |
| F1.8 | an embedding $M\subset L$ is **primitive** when $L/M$ is torsion free; a vector is primitive when $\mathbb{Z}v$ is, and a primitive vector need not have divisor 1 | Scattone §3.1 | F1.7 |
| F1.9 | a **quadratic form on a finite abelian group** $G$: $q : G\to\mathbb{Q}/2\mathbb{Z}$ with $q(ax)=a^2q(x)$ and $q(x+y)\equiv q(x)+q(y)+2b(x,y) \bmod 2\mathbb{Z}$ for a symmetric $b : G\times G\to\mathbb{Q}/\mathbb{Z}$; nondegenerate when $b$ is | Scattone §3.2, after Nikulin | F1.1 |
| F1.10 | for even nondegenerate $L$: $G_L = L^*/L$ is finite, and $b_L : G_L\times G_L\to\mathbb{Q}/\mathbb{Z}$, $q_L : G_L\to\mathbb{Q}/2\mathbb{Z}$ are induced by the rational extension of $b$ — the **discriminant-quadratic form** | Scattone §3.2 | F1.7, F1.9 |
| F1.11 | Thm 3.2.1 (= Nikulin 1.10.2): an even lattice with signature $(n_+,n_-)$ and discriminant form $q$ exists iff … — **condition not transcribed**; Nk3 carries Nikulin's three | Scattone Thm 3.2.1 | F1.10, Nk3 |
| F1.12 | Thm 3.2.2 (Nikulin): an even lattice with signature $(t_+,t_-)$ and discriminant form $q$ can be primitively embedded … — **conclusion not transcribed** | Scattone Thm 3.2.2 | F1.10, F1.8 |
| F1.13 | $O(L)$ **as a group**: the $\mathbb{Z}$-linear automorphisms of $L$ preserving $b$, under composition, and its matrix description $\{M : {}^tM G_L M = G_L\}$ through a basis | decomposed out of F1.1, whose row asserted $O(L)$ with no definition | F1.1; Mathlib `LinearEquiv`, `Subgroup`, and `QuadraticMap.IsometryEquiv`'s `refl`/`symm`/`trans`, which are the group operations with no `Group` instance over them |
| F1.14 | $\mathrm{div}(v)$, the positive generator of $(v,L)\subseteq\mathbb{Z}$, and $v^* = v/\mathrm{div}(v) + L \in G_L$ | decomposed out of F1.7, which states both and rests on a dual that supplies neither | F1.7, F1.10; Mathlib `Ideal.span`, `Int.gcd`, and `BilinForm.dualSubmoduleParing` for the pairing that produces the generator |
| F1.15 | the doubling $\mathbb{Q}/\mathbb{Z}\to\mathbb{Q}/2\mathbb{Z}$, and that $q(x+y)-q(x)-q(y)$ equals $2b(x,y)$ through it | decomposed out of F1.9, whose axiom relates a $\mathbb{Q}/2\mathbb{Z}$-valued $q$ to a $\mathbb{Q}/\mathbb{Z}$-valued $b$ | F1.9; Mathlib `AddCircle (1 : ℚ)` and `AddCircle (2 : ℚ)`, `QuotientAddGroup.map` for the induced map, `QuadraticMap.polar` for the left side |
| F1.16 | Milgram: for $L$ even unimodular, $n_+ - n_- \equiv 0 \pmod 8$; and in general the Gauss sum of $q_L$ computes $\mathrm{sign}(q_L)$ | decomposed out of F1.4, whose last clause is this theorem | F1.10, F1.15; Mathlib `gaussSum` (`NumberTheory/GaussSum.lean`) over `AddChar` and `MulChar`, `QuadraticForm/Signature.lean` |
| F3.1 | for $\mathbb{Z}_p$ the $p$-adic integers with the convention $\mathbb{Z}_\infty=\mathbb{R}$, and $L_p = L\otimes\mathbb{Z}_p$: lattices $L$, $M$ are in the same **genus** when $L_p\cong M_p$ for every $p = 2,3,5,7,\dots,\infty$ | Scattone §3.3 | F1.1; $p$-adic integers |
| F3.2 | even lattices are in the same genus **iff** they have the same signature and the same discriminant-quadratic form | Scattone §3.3; proved as Nikulin Cor. 1.9.4 | F3.1, F1.10, Pa10 |
| F3.3 | Theorem 3.3.1 (Nikulin, = Nk5): for $L$ even nondegenerate indefinite with $\mathrm{rk}\,L > \ell(G_L)+2$, the genus of $L$ contains one class and $O(L)\to O(G_L)$ is surjective | Scattone Thm 3.3.1, citing Nikulin 1.14.2 | F3.2, Nk5 |
| F3.4 | for definite $L$, $O(L)$ is finite of order $o(L)$; the **weight** of a genus $\mathcal{G}$ is $w(\mathcal{G}) = \sum_i 1/o(L_i)$ over its classes — the Minkowski–Siegel mass | Scattone §3.4 | F3.1 |
| F3.5 | the **genus** as an object: the equivalence relation "same signature and same discriminant form" on even nondegenerate lattices, and the quotient by it | decomposed out of F3.1 and F3.2, which quantify over a genus that no supplier defines | F1.10, F1.3, Pa10; Mathlib `Setoid` and `Quotient`.  The relation's two components are F1.3's signature and F1.10's form, so the definition bottoms out even though F3.3's one-class theorem does not |
| F4.1 | $R(L)$, the roots of a negative definite even lattice, and the **type** of $L$: the decomposition of the sublattice spanned by $R(L)$ into irreducible root lattices $A_m$, $D_m$, $E_m$ | Scattone §3.5 | F1.5; root systems |
| F4.2 | Theorem 3.5.1 (Niemeier): there are exactly 24 even unimodular negative definite lattices of rank 24 up to isomorphism, with the type $R(L)$ a **complete invariant**; and the table of the 24 types | Scattone Thm 3.5.1, citing Niemeier [24] | F4.1, F1.6 |

**F3.2 is the bridge the whole graph turns on**: same genus $\iff$ same
signature and same discriminant-quadratic form.  It is what makes the
discriminant form the carrier of the arithmetic, and it is where F1 and F3 meet.

**F1.5 is a convention hazard.**  Scattone's $E_8$ is $\mathbb{Z}^8$ with the
*negative* of the Cartan matrix, and he flags this as "a slight deviation from
the general convention".  Sterk writes $E_8(-2)$ and $E_8(-1)$; the Sage
reconstruction uses $-2\times$ the (positive) Cartan matrix.  **Which sign
convention each node is stated in has to be fixed once and checked**, because
$U\oplus U(2)\oplus E_8(-2)$ means different lattices under the two readings.

F3.1 is where this branch descends into $p$-adic lattices, and F4.1 into root
systems; neither has Mathlib substrate for lattices over $\mathbb{Z}_p$, though
Mathlib does have root systems and $p$-adic integers separately.

### Stratum V, from Vinberg — the hyperbolic reflection-group foundations

Read from Vinberg, *Some arithmetical discrete groups in Lobačevskiĭ spaces*
(`73LVC9YS`), §§2–4, and Vinberg, *The groups of units of certain quadratic
forms* (`73KFL5DK`), §3.  One locator recorded earlier does not resolve:
**the algorithm is in the 1972 paper, not the 1975 one**, which contains no
occurrence of the word.  A node citing the 1975 paper for it would fail an
audit against the source.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| V1 | $C^+$-matrices: nondecomposable positive matrices of order $n$, each the Gram matrix of a unique simplicial angle in $E^n$, with all entries of the inverse positive | 1975 §2 | Mathlib `Matrix`, `Matrix.PosDef` and `PosSemidef` (`LinearAlgebra/Matrix/PosDef.lean`), `Matrix.det`, `Matrix.nonsing_inv` (`Matrix/NonsingularInverse.lean`) for the condition on the inverse's entries, `Matrix.rank` |
| V2 | $C^0$-matrices: nondecomposable nonnegative matrices of order $n+1$, each the Gram matrix of a simplex in $E^n$ unique up to similitude, all principal submatrices of order $n$ positive | 1975 §2 | V1 |
| V3 | every $C$-polyhedron decomposes as a direct product of a simplicial angle and simplexes | 1975 §2 | V1, V2 |
| V4 | $A(F)$: for a face $F$ of a $C$-polyhedron, the Gram submatrix of the $e_i$ orthogonal to $F$ | 1975 §2 | V1 |
| V5 | a convex $P\subset\Lambda^n$ is a **$C^-$-polyhedron** when it has finite volume and every angle between bounding hyperplanes is $\le 90°$; its Gram matrix has all off-diagonal entries $\le 0$ | 1975 §3 | V4 |
| V6 | Lemma 2: the Gram matrix of a $C^-$-polyhedron is nondecomposable | 1975 Lemma 2 | V5 |
| V7 | Lemma 3: for an ordinary $s$-dimensional face $F$, $A(F)$ is a $C^+$-matrix; for an infinitely distant vertex, $A(F)$ is a $C^0$-matrix of rank $n-1$ | 1975 Lemma 3 — **rank convention to re-check against print** | V4, V5 |
| V8 | Lemma 5 (converse): a principal $C^+$-submatrix of rank $n-s$ is $A(F)$ for an $s$-dimensional ordinary face; **a principal $C^0$-submatrix of rank $n-1$ is $A(F)$ for an infinitely distant vertex** | 1975 Lemma 5 | V7 |
| V9 | **Theorem 1**: a symmetric $A=(a_{ij})$ is the Gram matrix of a $C^-$-polyhedron of $\Lambda^n$ **iff** it satisfies (L1) rank $n+1$ with negative inertial index 1; (L2) $a_{ii}=1$ and $a_{ij}\le 0$ for $i\ne j$; (L3) $A$ nondecomposable; (L4) $A$ has a principal submatrix that is either a $C^+$-matrix of rank $n$ or a $C^0$-matrix of rank $n-1$, called a **nodal** matrix; (L5) for every nodal $B_1$ and every $C^+$-submatrix $B$ of it of rank $n-1$ there is a nodal $B_2 \ne B_1$ containing $B$.  Such matrices are the $C^-$-matrices | Vinberg 1975 Thm 1 | V6, V8 |
| V9a | in the resulting polyhedron the **vertices correspond to the nodal submatrices** and the **edges to the $C^+$-submatrices of rank $n-1$**; (L4) says $P$ has vertices and (L5) that each edge lies on two | Vinberg 1975, proof of Thm 1 | V9 |
| V10 | Coxeter's classification: the nondecomposable $C^+$ and $C^0$ matrices with $a_{ij} = -\cos(\pi/m_{ij})$, by diagram, with rank subscripts | 1975 §4 | V1, V2 |
| V11 | the **algorithm** (Vinberg 1972 §3.2): fix $p_0\in\Lambda^n$, let $\Gamma_0\le\Gamma$ be generated by the reflections whose mirrors pass through $p_0$ — a finite group with $k\le n$ generators — and $P_0$ a cell of it; $P$ is the unique cell of $\Gamma$ agreeing with $P_0$ near $p_0$.  Put $\mathfrak{R} = \{e\in V : (e,e)>0,\ R_e\in\Theta\}$ and build $e_1,e_2,\dots\in\mathfrak{R}$ by: (1) $e_1,\dots,e_k$ with $P_0 = \bigcap_{i\le k}\Pi^-_{e_i}$; (2) for $l>k$, choose $e_l$ among the $e\in\mathfrak{R}$ with $(e,e_i)\le 0$ for all $i<l$, minimizing the distance $\rho(p_0,\Pi_{e_l})$; (3) orient each $e_i$ so that $p_0\in\Pi^-_{e_i}$ | Vinberg 1972 §3.2, (37)–(41) | V9, V9a |
| V11a | the quantity actually minimized: $\sinh^2\rho(p_0,\Pi_e) = -\dfrac{(e,v_0)^2}{(e,e)(v_0,v_0)}$, so $\rho(p_0,\Pi_e)$ and $\nu(e) = \dfrac{(e,v_0)^2}{(e,e)}$ are minimized together; and $p_0\in\Pi^-_e$ means $(e,v_0)\le 0$ | Vinberg 1972 (42)–(44) | V11 |
| V11b | **Proposition 4** (correctness): $P = \bigcap_i \Pi^-_{e_i}$, the upper limit of $i$ being the length of the sequence, **possibly infinite** | Vinberg 1972 Prop. 4 | V11, V11a |
| V12 | §1.9: for $L$ of signature $(1,n)$ and $T \subset O'(L)$ generated by reflections, with fundamental polyhedron $P$ given by the inequalities without extras and the $e_i$ primitive — how to recover an infinite vertex $q \in P$ from its parabolic subscheme $\Sigma_q$: for each connected component $\Sigma_0$, the $e_i$ with $i \in I_0$ span a parabolic subspace $E_0$ tangent to the cone, yielding the vector $u(\Sigma_0)$ | Vinberg 1983 (`4QDSPB92`) §1.9 | V8 |
| V13 | **Lemma (Vinberg 1983 §1.9)**: in general $u(\Sigma_0)$ **need not be a primitive element of $L$**; it is primitive when $T$ contains all 2-reflections (1-reflections) of $O(L)$ and at least one $e_i$, $i \in I_0$, is a 2-root (1-root) | Vinberg 1983 §1.9, Lemma | V12 |

**V8 is what C1 actually needs** — the correspondence between infinitely distant
vertices of the fundamental polyhedron and principal $C^0$-submatrices of rank
$n-1$, which is "parabolic subdiagram of maximal rank" in Sterk's language.  C1
bundled V8, V10 and V11 into one row whose locator covered only part of what it
claimed, so two thirds of it was uncheckable.

Still unlocated: **C2**, Sterk's citation to Vinberg 1983 (1.9) for the isotropic
vector read off a parabolic subdiagram.  Neither paper read here is the 1983 one;
the library holds Vinberg 1983 *The two most algebraic K3 surfaces*
(`4QDSPB92`), which is a plausible but unchecked match for that citation.

#### Stratum Lo — the Lobachevskii space stratum V stands in

Every row of stratum V names $\Lambda^n$, a $C$-polyhedron, a finite volume, an
infinitely distant vertex or a distance $\rho(p_0,\Pi_e)$, and none of those was
a node.  Read from Vinberg 1975 (`73LVC9YS`) §§1 and 3 — the same paper stratum
V is read from, one section earlier — and from Iversen, *Hyperbolic geometry*
(`ZE8F8SEY`), §§I.6 and II.4 for the metric.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| Lo1 | $E^{n,1}$: a real $(n+1)$-space with a nondegenerate scalar product of **negative inertial index 1**, and the cone $V = \{x : (x,x) < 0\}$, which has two connected components $V_\pm$ | Vinberg 1975 §3, (7) | Mathlib `QuadraticForm`, and `QuadraticForm/Signature.lean` for `sigPos`/`sigNeg` and Sylvester's law of inertia |
| Lo2 | $\Lambda^n$: its points are the rays from the origin lying in $V_+$, and its motions are the maps induced by the automorphisms of $E^{n,1}$ leaving $V_+$ invariant | Vinberg 1975 §3 | Lo1 |
| Lo3 | a subspace of $E^{n,1}$ is **hyperbolic**, **elliptic** or **parabolic** as the induced product is nondegenerate indefinite, positive, or degenerate; orthogonal complement exchanges hyperbolic with elliptic and preserves parabolic, in complementary dimension | Vinberg 1975 §3 | Lo1 |
| Lo4 | an $s$-plane $\Pi\subset\Lambda^n$ corresponds to an $(s+1)$-dimensional hyperbolic subspace $\widehat\Pi$; a halfspace to a halfspace bounded by a hyperbolic hyperplane; a **convex polyhedron** $P$ is an intersection of halfspaces, and $\widehat P$ is the corresponding polyhedral angle with vertex at the origin, not containing it | Vinberg 1975 §3 | Lo3 |
| Lo5 | $P$ is **bounded** iff $\widehat P\subset V_+$, and has **finite volume** iff $\widehat P\subset\overline{V}_+$; in the latter case the edges of $\widehat P$ lying on $\partial V_+$ are the **infinitely distant vertices** of $P$ | Vinberg 1975 §3, (8), (9) | Lo4 |
| Lo6 | the outward normals $e_i$ to the bounding hyperplanes, normalized by $(e_i,e_i) = 1$ — possible because the $\widehat H_i$ are hyperbolic — and the **Gram matrix** of $P$; for hyperplanes meeting at angle $\alpha$, $a_{ij} = -\cos\alpha$ | Vinberg 1975 §2 (1), §3 (10) | Lo4 |
| Lo7 | the hyperboloid model: in a space of Sylvester type $(-n,1)$ the vectors of norm 1 form a two-sheeted hyperboloid, $H^n$ is one sheet, $\langle P,Q\rangle\ge1$ for $P,Q\in H^n$, and $\cosh d(P,Q) = \langle P,Q\rangle$ defines a metric — the triangle inequality by the factorization $\Delta = 4\,\mathrm{sh}\,p\,\mathrm{sh}(p-a)\,\mathrm{sh}(p-b)\,\mathrm{sh}(p-c)$ of the Gram determinant | Iversen II.4.1–4.4 | Lo1 |
| Lo8 | the tangent space at $A$ is $A^\perp$, of type $(-n,0)$; and any $B$ is $A\cosh d(A,B) + U\sinh d(A,B)$ for a unit tangent vector $U$ at $A$ | Iversen II.4.5, 4.6 | Lo7 |
| Lo9 | for $\Gamma$ discrete and generated by finitely many reflections, the mirrors cut $\Lambda^n$ into **$\Gamma$-cells**, each a fundamental region, and the reflections in the walls of one cell generate $\Gamma$; a convex polyhedron is a $\Gamma$-cell **iff** all its dihedral angles are submultiples of $\pi$ | Vinberg 1975 §1, condition (R) | Lo4, Lo6 |
| Lo10 | the negative cone $V=\{x:(x,x)<0\}$ of a form of negative inertial index 1 has exactly **two** connected components, interchanged by $x\mapsto -x$ | decomposed out of Lo1, whose last clause is this theorem | Lo1; Mathlib `IsConnected`, `IsPreconnected`, `Convex` and `ConnectedComponents`, over `sigNeg` |

**The two sources use opposite signs**, and stratum V is stated in Vinberg's.
Vinberg puts $\Lambda^n$ inside a form of negative inertial index 1 and takes the
rays with $(x,x) < 0$; Iversen takes the norm-${+}1$ sheet of a form of Sylvester
type $(-n,1)$.  V9's condition (L1) — "rank $n+1$ with negative inertial index 1"
— is Vinberg's convention, and Lo7's metric is Iversen's; a node mixing them is
wrong by a global sign.  This is the same class of defect as audit point 1 and it
is settled the same way, by fixing the convention once.

**$n = 9$ throughout stratum C.**  Sterk runs Vinberg's algorithm not on $L_-$ —
which has signature $(2,10)$ and is not hyperbolic — but on $v^\perp/\mathbb{Z}v$,
which B4 identifies as $U\oplus E_8(-2)$ or $U(2)\oplus E_8(-2)$: rank 10,
signature $(1,9)$.  So $E^{n,1}$ has $n+1 = 10$, the space is $\Lambda^9$, and
V8's "principal $C^0$-submatrix of rank $n-1$" is rank 8 — which is exactly the
`rank=8` the reconstruction passes to `maximal_parabolic_subdiagrams`.  The
graph had never recorded which $n$ stratum V is about.

Substrate: Mathlib has quadratic forms with `sigPos`, `sigNeg` and Sylvester's
law of inertia (`LinearAlgebra/QuadraticForm/Signature.lean`), and a substantial
convex-geometry tree including convex cones and their duals
(`Analysis/Convex/`, `Analysis/Convex/Cone/`).  It has **no hyperbolic space**
in any model, no reflection group acting on one, no polyhedral angle and no
volume.  So Lo1 and Lo3 are within reach and Lo2, Lo4–Lo9 are greenfield.

### Still missing from this stratum

Baily–Borel is decomposed as stratum BB above; its own next descents are BB SSSS5–8
and Korányi–Wolf.  Niemeier’s classification (F4.1) has no
is closed: F4.2, Niemeier via Scattone Thm 3.5.1.  Remaining unread: the
p-adic layer under Nk2 and F3.1, and the surface theory under stratum E.
(sources for E1–E6 are now assigned: BPV VQUIPQ4Y, Horikawa 6ZXI2FJ4 and RQ2EG4F7.)


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
node that carries the classification is **V10**, Coxeter's list of the
nondecomposable $C^+$ and $C^0$ matrices by diagram with their rank subscripts,
cited to Vinberg 1975 §4.  This paragraph previously said the node was
unrecorded; V10 records it.

## Terminality verdicts

A node is **terminal** when its next dependency is available: in Mathlib at the
pinned revision, or in a Lean corpus listed in the `lean-categories`
formalization source registry (`AGENTS.md` §"Formalization source registry",
resolved 2026-08-14).  Everything else is **greenfield** — no formalization
exists anywhere the registry knows of, so the node must be authored.

The revision.  The `lean-categories` Mathlib checkout is at `db584cd6d4`, the
bump to toolchain v4.33.0; the revision `0df444a3` named above is its **child**,
the bump to v4.33.1, one commit later.  Every substrate claim below was checked
against the checkout, so where the two differ the claims are the weaker,
earlier ones.

**Which checkout, exactly.**  There are two Mathlib clones on this machine and
only one of them is the pinned one:

- `~/gitclones/lean-categories/.lake/packages/mathlib` — **the pinned checkout,
  `db584cd6d4`, 2026-08-10.**  Every claim in this file means this tree.
- `~/gitclones/lean-reference-corpus/leanprover-community__mathlib4` —
  `81a5d257c8`, 2026-07-13, a month older.  It is the corpus clone, and it is
  the wrong tree to audit against.

The difference is not cosmetic: `Mathlib/AlgebraicGeometry/Group/Affine.lean`
exists in the pinned tree (23 KB, the Hopf-algebra/`Spec` anti-equivalence) and
does not exist in the corpus clone at all.  An audit run against the older tree
reports AG2's substrate as a fabricated path when it is a real file.  Check the
revision with `git -C <tree> log -1` before believing an absence.

Registry surfaces swept: the Mathlib subtrees table; *Quadratic forms, lattices,
sphere packing*; *Algebra, number theory, algebraic geometry*; *Analysis,
probability, geometry, dynamics*; *Category theory, higher structures*.  The
third sweep below then read the registry **as cloned source** in
`~/gitclones/lean-reference-corpus`, which is where the two repositories the
first two sweeps never mentioned turned up.

### Terminal against Mathlib

| Nodes | Mathlib substrate |
| --- | --- |
| F1.1's notion, $\langle B\rangle$, and the congruence criterion | a lattice is `Module.Free ℤ L` and `Module.Finite ℤ L` — equivalently a `Basis (Fin n) ℤ L` — with a `LinearMap.BilinForm ℤ L` satisfying `LinearMap.IsSymm` (`SesquilinearForm/Basic.lean`, a structure on `B : M →ₛₗ[I] M →ₗ[R] R`).  $\langle B\rangle$ from a matrix is `Matrix.toBilin` through a basis, or `Matrix.toBilin'` on `Fin n → ℤ` (`LinearAlgebra/Matrix/BilinearForm.lean`).  $B' = {}^tABA$ is **`LinearMap.BilinForm.toMatrix_comp`**, whose statement is literally $\mathrm{toMatrix}\,c\,(B.\mathrm{comp}\ l\ r) = ({}^t\mathrm{toMatrix}\,l)\cdot\mathrm{toMatrix}\,B\cdot\mathrm{toMatrix}\,r$, at $l = r =$ the basis change; `toMatrix_basisFun` covers the standard basis.  Note the namespace: `BilinForm.toMatrix` and `BilinForm.toMatrix_comp` are **deprecated aliases** as of 2026-01-16, and the live names are `LinearMap.BilinForm.toMatrix` and `Matrix.toBilin`; $\mathrm{GL}(n;\mathbb{Z})$ is `Matrix.GeneralLinearGroup (Fin n) ℤ` |
| F1.2 | `QuadraticMap.polar` and `QuadraticMap.polarBilin` (`QuadraticForm/Basic.lean`) relate $q(v)=(v,v)$ to $b$; evenness is a condition on the diagonal of `BilinForm.toMatrix`, stated over `Int.even_iff` |
| F1.3 | `QuadraticForm.sigPos` and `sigNeg` (`QuadraticForm/Signature.lean`) are **the same definition F1.3 gives** — the maximal dimension of a subspace on which $Q$ is positive (resp. negative) definite — and they are stated for `[CommRing R] [LinearOrder R] [Module R M]`, so they apply over $\mathbb{Z}$ with no base change.  Sylvester's law, `sigPos_of_equiv_weightedSumOfSquares`, is field-only, which is where $L\otimes\mathbb{R}$ enters |
| F1.4's definitions | $d(L)$ is `Matrix.det` of `BilinForm.toMatrix`; nondegeneracy and unimodularity are conditions on it.  **Its last clause is not here** — that an even unimodular lattice has $n_+\equiv n_-\pmod 8$ is Milgram's theorem, and `rg -i 'milgram\|oddity'` over the pinned tree finds only Lax–Milgram, a functional-analysis false friend.  That clause is greenfield |
| F1.7's dual | **`BilinForm.dualSubmodule`** (`LinearAlgebra/BilinearForm/DualLattice.lean`): for $N \le M$ over $S \supseteq R$, $\{x \mid \forall y \in N,\ B\,x\,y \in (1 : \mathrm{Submodule}\ R\ S)\}$ — which at $R=\mathbb{Z}$, $S=\mathbb{Q}$, $M=L_\mathbb{Q}$ is exactly $L^*\subseteq L_\mathbb{Q}$, with `dualSubmoduleParing` for the pairing.  $\mathrm{div}(v)$ and $v^*$ are definitions over it |
| F1.8 | `Submodule.torsion` and `RingTheory/Flat/TorsionFree.lean`: primitivity of $M\subset L$ is torsion-freeness of the quotient, which is the definition F1.8 gives |
| F1.9, F1.10 | finite abelian groups with `GroupTheory/FiniteAbelian/Basic.lean`; **the value groups are `AddCircle`** — `AddCircle p := 𝕜 ⧸ zmultiples p` (`Topology/Instances/AddCircle/Defs.lean`), so $\mathbb{Q}/2\mathbb{Z}$ is `AddCircle (2 : ℚ)` and $\mathbb{Q}/\mathbb{Z}$ is `AddCircle (1 : ℚ)`, both `AddCommGroup` and so both `ℤ`-modules.  $q$ is then a `QuadraticMap ℤ G (AddCircle (2:ℚ))`, whose `toFun_smul` **is** F1.9's $q(ax)=a^2q(x)$, and `QuadraticMap.polar` supplies $q(x+y)-q(x)-q(y)$.  What must be authored is the doubling $\mathbb{Q}/\mathbb{Z}\to\mathbb{Q}/2\mathbb{Z}$ that turns that into $2b(x,y)$, and the induced forms on $L^*/L$ |
| F4.1's root set | `LinearAlgebra/RootSystem/` and `Matrix/Cartan.lean`, which holds the Cartan **matrices** of $A$, $B$, $C$, $D$, $E_6$, $E_7$, $E_8$, $F_4$, $G_2$ with their determinants, and `ADEInequality.Admissible`.  The *type* of $L$ — the decomposition of the sublattice spanned by $R(L)$ into irreducibles — is **not** here: Mathlib has `RootPairing.IsIrreducible` as a predicate and lemmas its own files call "necessary for the classification", no decomposition theorem and no direct sum of root pairings.  That half of F4.1 goes through `lean-categories`' `adeClassification`; see the routes table |
| F1.3, and the inertial index in Lo1 | `LinearAlgebra/QuadraticForm/Signature.lean` — `sigPos`, `sigNeg`, and Sylvester's law of inertia |
| Lo3 | the trichotomy of a subspace by its induced product, over `QuadraticMap.restrict` (`QuadraticForm/Basic.lean`), `BilinForm.restrict`, `LinearMap.BilinForm.orthogonal` for the complement (`BilinearForm/Orthogonal.lean`), `Nondegenerate` (`SesquilinearForm/Basic.lean`) and the same signature file.  Lo1 and Lo3 are the two nodes of stratum Lo that are definitions over what exists, which the floor already records |
| AG4's completeness | `AlgebraicGeometry/Morphisms/Proper.lean`, `.../UniversallyClosed.lean` |
| D8's ingredients | `UpperHalfPlane` with `MoebiusAction`, `CongruenceSubgroup.Gamma1 2` (`NumberTheory/ModularForms/CongruenceSubgroups.lean`), and — better than the row knew — **`IsCusp` and `CuspOrbits`** (`NumberTheory/ModularForms/Cusps.lean`: the cusps of a subgroup of $\mathrm{GL}(2,\mathbb{R})$ as the fixed points of its parabolic elements, those of $\mathrm{SL}(2,\mathbb{Z})$ identified with $\mathbb{P}^1(\mathbb{Q})$, the same for any arithmetic subgroup, and the orbit type).  **The quotient $\mathbb{H}/\Gamma^1(2)$ is not an object**: no modular curve, no quotient of $\mathbb{H}$ by a congruence subgroup anywhere in the pinned tree.  D8 says each one-dimensional component *is* that quotient, so the quotient is the piece to author, over an action and a cusp theory that exist |
| Pa1 | `PadicInt` and `Padics` for $\mathbb{Z}_p$; and the semigroup operation is **`QuadraticMap.prod`** (`QuadraticForm/Prod.lean`, with `Isometry.inl`/`inr` and `IsometryEquiv.prod`), not the `AddCommMonoid (QuadraticMap R M N)` instance — that instance adds two forms on *one* module pointwise, while Nikulin's $\mathrm{qu}(\mathbb{Z}_p)$ is isomorphism classes under **orthogonal sum**, so the semigroup is `prod` on the classes `IsometryEquiv` cuts out.  Both halves exist; assembling them into the semigroup is the small piece to author |
| Nk1, Pa7 | `AddGroup.rank` (`GroupTheory/Rank.lean`) is exactly $\ell(A)$ — "the minimum size of a generating set", `to_additive` from `Group.rank`, defined for `FG` groups — and $\lvert A\rvert$ is `Nat.card`; the form on $A_q$ is the F1.9/F1.10 substrate |

**`ZLattice` was in the F1 row and is not this notion.**  Mathlib's `ZLattice`
(`Algebra/Module/ZLattice/Basic.lean`) is a *discrete subgroup of full rank in a
finite-dimensional vector space over a normed linearly ordered field* — an
embedded lattice with a topology, built for geometry of numbers, and it carries
**no bilinear form at all**.  F1.1's lattice is an abstract finitely generated
free $\mathbb{Z}$-module *with* a symmetric form, of signature $(2,10)$ in the
case that matters, and no ambient space.  `ZLattice` is the right tool for the
volume side of Rt4 and Rt9, and for the geometry-of-numbers argument
`lean-categories` runs in `ClassFiniteness`; it supplies nothing in F1.

**$O(L)$ was in the F1 row and is not in Mathlib.**  `Matrix.orthogonalGroup n R`
is an abbreviation for `unitaryGroup n R` (`LinearAlgebra/UnitaryGroup.lean`) —
the matrices with ${}^tM = M^{-1}$, which is the orthogonal group of the
*identity* Gram matrix.  $O(L)$ is $\{M : {}^tM G_L M = G_L\}$ for the lattice's
own Gram matrix, and nothing in the pinned tree defines it.  It is a short
definition over `Matrix` or over `LinearEquiv`, and it is greenfield.

**F2.3 and F2.4 were in this table and do not belong here.**  The row read
"reflections and Cartan–Dieudonné live in `LinearAlgebra/QuadraticForm/`".
They do not: that directory contains no reflection at all.  Mathlib's
Cartan–Dieudonné is `LinearIsometryEquiv.reflections_generate_dim` in
`Analysis/InnerProductSpace/Projection/FiniteDimensional.lean`, whose own
docstring calls it a *special case*, and it is stated for a finite-dimensional
**real inner product space** — a positive definite form.  `LinearAlgebra/
Reflection.lean` has reflections attached to a root pairing, not to a quadratic
form.  F2.3 needs the factorization of an element of $O(L_\mathbb{Q})$ into
reflections for an **indefinite** rational form, of signature $(2,10)$, and
nothing in the pinned Mathlib supplies it.  Both rows move to greenfield.

### Terminal against a registry corpus

A row belongs here only if the supplier **exists now**: read in a clone, free of
`sorry` in the part the node uses, and not waiting on anything.  Three rows that
used to sit here do not meet that and have moved to *Routes that are not
suppliers* below — the table was a list of hopes in those three places, which is
the failure this section is supposed to catch.

| Nodes | Corpus | Status |
| --- | --- | --- |
| F1.5 ($E_8$), F4.1 (root lattices) | [`thefundamentaltheor3m/Sphere-Packing-Lean`](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean) — Viazovska dimension-8, $E_8$ lattice | **already integrated, and the integration is a proved comparison** — read: `LeanCategoriesSpherePacking/E8/Comparison.lean` imports `SpherePacking.Basic.E8` beside the project's `Standard`, gives the explicit basis change and its inverse between the external basis and the selected simple-root basis, proves the two products are the identity, carries the external Gram matrix to the project's, and concludes that Sphere-Packing-Lean's *positive* $E_8$ is the **opposite** of the project lattice, with the sign change explicit on every pair.  Sorry-free.  `Integration/SpherePacking/` itself is only the build harness — a lakefile, a manifest and a toolchain pin |
| Pa2–Pa5, Pa8's exceptional 2-adic case, and the $p=2$ conditions in Nk3–Nk5 | [`roed-math/gq2-lean`](https://github.com/roed-math/gq2-lean) — dyadic Hilbert symbol over $\mathbb{Q}_2$, Serre's evaluation formula, 2-adic square-class facts | **the layer Pa uses is proved and axiom-free**, checked in the clone: `GQ2/HilbertSymbol.lean` and `GQ2/DyadicSquares.lean` import only `Mathlib.NumberTheory.Padics.{RingHoms,Hensel}`, and `HilbertSymbolDyadic.lean` says of itself that it sits upstream of the axioms file; none of the six dyadic files contains a `sorry`.  Two things the earlier "sorry-free" verdict left out: the library declares **nine `axiom`s**, all quarantined in `GQ2/Foundations/Axioms.lean` as classical literature inputs (local reciprocity, Tate duality, the local Euler characteristic, …) under an enforced one-file rule, and four proof-position `sorry`s live in `Challenge.lean` and `ChallengePalomar.lean`, which *state the open problem* rather than leaving a gap.  Apache 2.0 |

#### Routes that are not suppliers

Each of these was in the table above.  None is available now, and the reason
differs in each case — a `sorry` where the node needs a theorem, a repository
that turned out to be about something else, and a corpus waiting on
publication.  For F3.1, F3.2 and E2 this means **no supplier exists**, so they
are greenfield; the `lean-categories` row keeps its nodes' verdicts, since a
route pending publication is still the route.

| Nodes | Corpus | Why it is not available |
| --- | --- | --- |
| F3.1, F3.2 (the local invariants under the genus) | [`mariainesdff/HassePrinciple`](https://github.com/mariainesdff/HassePrinciple) — Hilbert symbols, Hasse–Minkowski over general fields | definitions in place and **38 proof-position `sorry`s**, counted in the clone.  Eleven of them are in `HilbertSymbol/Basic.lean`, so it is the symbol's own basic properties that are open, not only a choice-independence lemma at the top; the rest are spread over `Padics/Lemmas` (9), `QuadraticForm/HasseMinkowskiInvariant` (6), `QuadraticForm/Basic` (5) and four more files.  A partial route, and further from being a supplier than the earlier verdict said |
| E2 (the $K3$ double cover as a covering space) | [`AlexKontorovich/CoveringSpacesProject`](https://github.com/AlexKontorovich/CoveringSpacesProject) | **read, and it is not covering spaces.**  Its live files are winding numbers and the fundamental theorem of algebra: `ComplexPathWinding`, `RootsMathlib` (the winding number of a polynomial on a large circle, leading-term domination, `eventually_windingNumber_eq_natDegree`).  The covering-space material — `ExpCovering`, `UniquePathLifting` — is in a `Legacy/` subtree that holds the repository's only `sorry`s, next to a `SectionTwo.lean` whose content is `theorem TheoremTwo : True`.  For E2 the better route is Mathlib itself: `IsCoveringMap`, `IsEvenlyCovered` and `IsCoveringMapOn` in `Topology/Covering/Basic.lean`, with `Topology/Covering/Quotient.lean` and `Topology/Homotopy/Lifting.lean`.  Neither supplies $K3$ surfaces or the covering involution |
| F1.10, F1.7, F2.1, F2.4–F2.5, F3.1, F4.1 | `lean-categories` itself — `Discriminant`, `DiscriminantQuadratic`, `MetricDual`, `DiscriminantAction`, `CanonicalSpinorNorm`, `Hasse`, `DyadicSymbol`, `ClassFiniteness`, and the root-lattice objects of `DefiniteNondegenerate` and `DRootLattice` | sorry-free; **pending publication to Prove2Me**, and three of the correspondences unverified (see the routes table) |

### Registry sweep for the strata added after the first pass

The first sweep covered the strata that existed then.  AG, HS, AF, Rt, Ky, Lo
and Ni were added afterwards and needed their own, against the same registry
(`lean-categories` `AGENTS.md` §"Formalization source registry").  What follows
is the result of that sweep, with the near misses named — a repository is more
useful recorded as *not* a supplier than left unmentioned, because the next
reader would otherwise sweep for it again.

**Every row below has now been read.**  Six of these repositories are in the
local corpus; the other seven were cloned and read for this pass, and one of them
changed its verdict — see the `bruhat-tits` row, which turns out to supply
lattice theory over a discrete valuation ring rather than only a tree.  What each
reading found, beyond the row's own cell:

- `chrisflav/bruhat-tits` is **sorry-free**, and its `Lattice/` subtree is not
  about the tree at all: `IsLattice` for $R$-submodules of $\iota\to K$ over a
  DVR, the $K^\times$-action, and in `Lattice/Distance.lean` the **elementary
  divisor theorem for a pair of lattices** — `exists_normal_basis_uniformizer`
  gives bases with $b_L(i) = \varpi^{f(i)}b_M(i)$ and $f$ antitone, through a
  Cartan decomposition, and `signature_unique` proves $f$ independent of the
  uniformizer and of both bases.  `signature`, `dist`, and $L/\varpi L$ over the
  residue field follow.  This is the rank-two case of the invariant factors of
  one lattice relative to another, which is the step under Pa9 and under
  `lean-categories`' `JordanFiltration`.  Two restrictions: rank is fixed at
  `Fin 2` throughout, and these lattices carry **no bilinear form**, so nothing
  here decomposes a *quadratic* lattice.
- `BochaoKong/nullstellensatz` has a `LocalComplexGeometry/` tree with local
  biholomorphisms and a Weierstrass-preparation bridge, one file carrying
  `sorry`s.  It confirms the row: the local theory, and the natural floor for
  AF10 and for stratum E's local structure.
- `Jun2M/Main-theorem-of-polytopes` is sorry-free and bundles `Halfspace` as a
  **norm-one dual functional plus a level**, with convexity, closedness and full
  affine span.  That norm-one condition is exactly what ties it to the Euclidean
  structure and away from Lo4.
- `singerng/steinberg-formalization` is sorry-free and is `A3`, `B3Small`,
  `B3Large` — Steinberg relations for named root systems, which is a
  presentation, as the row says.
- `mccorvie/classification-of-surfaces` is 681 files of Jordan curve and
  Schoenflies theory with three `sorry` files: a serious development, and of
  topological surfaces.
- `dwrensha/Rupert.lean` is quaternion-to-rotation-matrix machinery and the snub
  cube.  Sorry-free, and unrelated to anything here.
- `smmercuri/adele-ring_locally-compact` supplies uniformizers in adic
  completions and imports local class field theory, with one `sorry` file.

| Stratum | Nearest thing in the registry | Why it is not a supplier |
| --- | --- | --- |
| AG | [`chrisflav/bruhat-tits`](https://github.com/chrisflav/bruhat-tits); [`singerng/steinberg-formalization`](https://github.com/singerng/steinberg-formalization) | the Bruhat–Tits **tree** of $\mathrm{SL}_2$ over a local field is an affine building for one group, not the spherical building of AG16; Steinberg groups are a presentation, not the parabolic structure theory |
| HS, Ky | `Mathlib/Geometry/Manifold/Riemannian/` with [`leanprover-community/physlib`](https://github.com/leanprover-community/physlib) for pseudo-Riemannian metrics | Riemannian metrics and path length exist; the almost-complex structure, integrability, geodesics and Kähler form of HS1–HS5 do not |
| HS, E, AF10 | [`BochaoKong/nullstellensatz`](https://github.com/BochaoKong/nullstellensatz) | local complex-analytic geometry — germs, the Rückert Nullstellensatz.  The nearest thing to a normal analytic space, and it is the local theory, not the space |
| E | [`mccorvie/classification-of-surfaces`](https://github.com/mccorvie/classification-of-surfaces) | compact **topological** surfaces.  A false friend: stratum E is about compact complex surfaces, which are real four-manifolds |
| Lo, V | [`Jun2M/Main-theorem-of-polytopes`](https://github.com/Jun2M/Main-theorem-of-polytopes); [`dwrensha/Rupert.lean`](https://github.com/dwrensha/Rupert.lean) | convex polytopes in Euclidean space; Lo4's polyhedra live in a Lorentz space and are cut out by the light cone |
| AF | [`CBirkbeck/ModularForms_Lean4`](https://github.com/CBirkbeck/ModularForms_Lean4), [`loefflerd/ModularFormDimensions`](https://github.com/loefflerd/ModularFormDimensions), [`CBirkbeck/WeilConverse`](https://github.com/CBirkbeck/WeilConverse), [`ANR-FALSE/PadicModForms`](https://github.com/ANR-FALSE/PadicModForms) | all rank one — forms on $\mathbb{H}$ for congruence subgroups of $\mathrm{SL}_2$.  AF is automorphic forms on a bounded symmetric domain of rank 2 |
| Rt | — | nothing: no Iwasawa decomposition, no Siegel set, no arithmetic-group reduction theory anywhere in the registry |
| Ni, Pa | [`smmercuri/adele-ring_locally-compact`](https://github.com/smmercuri/adele-ring_locally-compact), [`roed-math/gq2-lean`](https://github.com/roed-math/gq2-lean), [`chrisflav/bruhat-tits`](https://github.com/chrisflav/bruhat-tits) | `gq2-lean` supplies Pa's dyadic layer; the adele ring is a route for F3.1's adelic phrasing, not for Nikulin's theorems.  **`bruhat-tits` is a partial supplier for Pa9's first step** and was missed by both earlier sweeps: the elementary divisor theorem for a pair of DVR lattices, existence and uniqueness of the antitone signature, sorry-free — in rank two only, and for lattices with no form.  Pa9 needs it in every rank and for a quadratic lattice, which is where `lean-categories`' `Jordan*` files continue |

Two general observations from the sweep.  The registry's strength is
**arithmetic**: number fields, adeles, modular forms, class field theory,
$p$-adic analysis.  Its weakness is this graph's upper half — Lie theory,
algebraic groups, symmetric spaces and complex geometry — with one qualification
the third sweep adds: ATLAS covers a great deal of that ground in *statement
shape*, sorry-laden and under-specified, so the weakness is in proved
mathematics rather than in vocabulary.  The second is that the near misses
cluster one level below what is needed: an affine building instead of a
spherical one, local analytic geometry instead of analytic spaces, rank-one
automorphic forms instead of rank two, topological surfaces instead of complex
ones.  That is what a frontier looks like from underneath.

**This table is about suppliers, not about foundations**, and the two are easy to
confuse.  Nothing in the registry proves any statement in these strata, and that
is what "greenfield" means.  It does not mean the statements cannot be written:
the primitives they are written over are almost all in the pinned Mathlib, and
*The construction floor* below names them node by node.

### Third sweep: the local reference corpus

Both earlier sweeps read the registry as a list of links.  `~/gitclones/lean-reference-corpus`
is that registry **cloned** — 111 repositories, 3,894 `.lean` files outside Mathlib — so the
claims below are grep-and-read against source, not against a description.

Two of those repositories were never swept at all, and one of them changes verdicts.

**A search trap first, because it produced the omission.**  `rg` honours ignore rules inside
these clones and silently returns nothing; `rg -i "root lattice" -g '*.lean' .` finds zero
files where `rg -i --no-ignore` finds many.  Every search in this subsection used
`--no-ignore`.  A negative result obtained without it is not a negative result.

#### ATLAS — [`facebookresearch/atlas-lean`](https://github.com/facebookresearch/atlas-lean)

Textbook mathematics autoformalized by LLMs (companion paper arXiv:2605.29955), 2,654 files,
with whole books on exactly this graph's upper half: `Atlas/Buildings/` (331 files),
`Atlas/LieGroups/` (107), `Atlas/GeometryOfManifolds/` (83).  Its provenance passes the
registry's check — Meta Platforms, Apache-licensed, published pipeline — but its declarations
are machine-written, so a name in it is worth even less than a name elsewhere.  Each row
below was read.

| Node | What ATLAS has | Why it is not a supplier |
| --- | --- | --- |
| AG6 | `BNPair G M` and `BNPairAxioms` (`Buildings/code/BNPair/Basic.lean`) — a faithful Tits system over Mathlib's `CoxeterMatrix`/`CoxeterSystem`: $B$, $N$, $T = B\cap N$, $\pi : N \twoheadrightarrow W$ with kernel $T$, $\langle B\cup N\rangle = G$, and the cell rules $C(w)C(s)\subseteq C(ws)$, $\subseteq C(ws)\cup C(w)$ with the non-normality condition.  Bruhat cells are `BNPair.bruhatCell`.  The `BNPair` subtree carries 3 `sorry`s, all in `BNPair/Generalized/Defs.lean` | a **route located, and a real one**: this is the abstract Tits system, which AG6 states.  What is missing is the input — that $G(\mathbb{Q})$ with its parabolic $\mathbb{Q}$-subgroups *is* a BN-pair.  That is AG4–AG7's algebraic-group content and nothing here touches it |
| AG16 | `poset_isomorphism_specialSubsets_properParabolics` and `BuildingAxiomsFromBNPairs` (`Buildings/code/BNPair/`) — the building of a BN-pair, as the poset of parabolics, with the building axioms derived | the abstract form of AG16's construction.  AG16 needs it for the parabolic $\mathbb{Q}$-subgroups of a reductive $\mathbb{Q}$-group; the group-theoretic half is supplied, the algebraic-group half is not |
| HS1 | `AlmostComplexStructure` (`GeometryOfManifolds/code/AlmostComplexManifolds.lean`): `J : ∀ x : M, TangentSpace I x →L[ℝ] TangentSpace I x` with `J x (J x v) = -v` | the docstring says "a smooth field of fiberwise endomorphisms"; the structure **imposes no smoothness**.  It is the pointwise algebra of HS1 and not its analytic content — which is why the floor still routes HS1 through `ContMDiffSection` |
| HS2 | `Integrable` in the same file | it takes the Nijenhuis tensor `N` as a **parameter** and asserts `N x u v = 0`.  `N` is never constructed from `J`, so the declaration says nothing about `J` and the Newlander–Nirenberg content is absent |
| Rt1 | `IwasawaData` and `CartanDecomposition` (`LieGroups/code/IwasawaDecomposition.lean`) — $K$ compact, $A$ commutative, $N$, with existence and uniqueness of $g = kan$; `CartanDecomposition` has $\mathfrak{k}\oplus\mathfrak{p}$ with both bracket rules | $N$ carries **no condition at all** — not nilpotent, not unipotent — $A$ only commutativity, and nothing relates either to the Cartan decomposition or to restricted roots.  `iwasawa_decomposition_exists` asserts the decomposition for *every* topological group and is `sorry`.  The definition is under-specified, so the statement it would satisfy is not Rt1 |

The pattern is uniform and worth stating once: ATLAS supplies **statement shapes** typed against
Mathlib, frequently under-specified against the theorem they are named for, and its proofs are
`sorry` wherever the mathematics is hard.  It is a drafting aid for the greenfield strata and a
supplier for none of them.  AG6 and AG16 are the closest, and what they are close to is the
abstract Tits-system layer rather than the algebraic groups underneath it.

#### `jonhanke/quadratic_forms_in_lean` — a skeleton

The name is the strongest candidate in the corpus for F3 and Pa, and the repository is empty
of them: `Basic.lean` holds 8 declarations, and `Isometry.lean`, `HilbertSymbol.lean`,
`Hyperbolic.lean`, `LocalTheory.lean` and `LocalGlobalHassePrinciple.lean` are 8-to-10-line
files with a namespace, a comment naming the intended content, and no declaration at all.
Recorded so the next reader does not sweep it twice.

#### Absent from the whole local corpus

Searched with `--no-ignore` across all 3,894 non-Mathlib `.lean` files: Niemeier's
classification, the Kobayashi pseudo-distance, Poincaré and Poincaré–Eisenstein series, Siegel
sets, hyperbolic space in any model, normal analytic spaces, $K3$ and Enriques surfaces, the
canonical decomposition of a $p$-adic lattice, and the genus of a lattice.  Every one of those
is a node in this graph, and none of them has a formalization anywhere the registry reaches.

### Fourth sweep: the registry's own list, counted

The three earlier sweeps read the registry's *tables of interest* — the Mathlib
subtree table and four domain tables — and the corpus as cloned.  Neither is the
registry's full list.  `~/gitclones/lean-categories/AGENTS.md` §"Formalization
source registry" links **277 repositories**, and 245 of them are named nowhere in
this file.  Most are irrelevant by subject (combinatorics, quantum information,
type theory, machine learning, competition benchmarks).  Five are not, and were
cloned and read for this pass.  All five are sorry-free.

| Node | Repository | What it supplies, read |
| --- | --- | --- |
| F1.10's computation; the $\ell(A_{L_-})=10$ in the A2 and A3 audit points | [`JJYYY-JJY/lean-normal-forms`](https://github.com/JJYYY-JJY/lean-normal-forms) | the Lean 4 artifact for arXiv:2607.22524: a verified Kannan–Bachem Smith reduction returning a canonical Smith matrix with four explicit transformation matrices, the uniqueness of the invariant factors through the classical minor characterisation (`diagPrefixProduct_dvd_minor`, `first_invariantFactor_eq_of_two_sided_equiv`), and polynomial cost bounds.  Its maintained scope is **square integer matrices with $\det \ne 0$** — which is exactly a nondegenerate Gram matrix, so $G_L = L^*/L$ as the cokernel is inside it, and $\ell(A_q)$ is the count of invariant factors above 1.  What it does **not** give is the discriminant *form*: the group's invariant factors are not $q_L$, and F1.10 is the form |
| F3.1, F3.2 in rank three | [`MichaelStollBayreuth/LegendreQF`](https://github.com/MichaelStollBayreuth/LegendreQF) | Legendre's theorem on diagonal ternary forms: for $a,b,c$ squarefree and pairwise coprime, $ax^2+by^2+cz^2=0$ has a nontrivial integral solution iff the local conditions hold.  Sorry-free in Lean 4, with `IsSquareMod` under it.  This is the ternary case of Hasse–Minkowski, and it is **further along than `HassePrinciple`**, whose own `QuadraticForm/RankThree.lean` carries a `sorry`.  Rank three only, and diagonal only |
| V11–V13, and Lo's basis work | [`leanprover/hex-lll`](https://github.com/leanprover/hex-lll) | LLL over `Matrix Int n m`: the $(\delta,\eta)$-reducedness predicate `isLLLReduced` with its short-vector bounds, decidable linear independence through an integer Gram–Schmidt, row operations proved to preserve the lattice, a checker and a native path.  Vinberg's algorithm needs a reduced basis of a hyperbolic lattice and a distance order on candidate roots; this is the reduction half over $\mathbb{Z}$, with no form of signature $(n,1)$ anywhere in it.  It is one of a family (`hex-gram-schmidt`, `hex-determinant`, `hex-bareiss`, `hex-row-reduce`, each also in a `-mathlib` variant) that the registry lists and this graph had never looked at |
| Ky1, Ky2's ambient | [`vbeffara/RMT4`](https://github.com/vbeffara/RMT4) | the Riemann mapping theorem, `RMT` in `RMT4/Main.lean`: an open connected $U \ne \mathbb{C}$ admitting primitives is biholomorphic to the disc.  Sorry-free.  Ky1's pseudo-distance is an infimum over chains of *holomorphic maps from the disc*, so this is the uniformisation fact behind treating the disc as the model, and no part of Ky's own statements |

Two of those five change a verdict recorded above: `lean-normal-forms` gives the
computational step under F1.10 that the F1 rows had assigned to `Matrix.det`
alone, and `LegendreQF` displaces `HassePrinciple` as the nearest thing to F3 in
rank three.  Neither becomes a supplier of a node, for the reason each row gives.

**The 240 that remain unnamed.** They were judged by subject from the registry's
own one-line descriptions, not read.  That is a weaker standard than the rest of
this file and it is the right one here: a repository on the Feit–Thompson
theorem, on quantum resource theories or on Putnam problems cannot supply a node
about hermitian symmetric domains, and reading 240 repositories to confirm that
would buy nothing.  If a stratum later needs a capability this graph has not
named, the registry list is the place to look before concluding it is absent —
that is what this sweep found, twice.

### Fifth sweep: every public Lake package, for the nine atoms

The registry's own first instruction is to search [Reservoir](https://reservoir.lean-lang.org/)
before any general GitHub search, and Reservoir is cloned here too:
`~/gitclones/lean-reference-corpus/reservoir-sources` holds **734 packages,
94,764 `.lean` files, 3.1 GB**, cloned 2025-08-15.  The four earlier sweeps never
touched it.  It is the widest surface available for the question the nine atoms
raise — whether the thing is absent, or merely absent from the places already
looked.

Searched with `rg -l --no-ignore -g '*.lean'` across all 734 packages:

| Sought | Result |
| --- | --- |
| `AlmostComplex` | **no file, in any package** |
| `AnalyticSpace` | **no file** |
| `WeilDivisor`, `CartierDivisor` | **no file** |
| `DeckTransformation` | **no file** |
| `Niemeier` | **no file** |
| the genus of a lattice | **no file** |
| Eichler | **no file** |
| Siegel sets, fundamental domains for arithmetic groups | **no file** |
| bounded symmetric domains | two false friends: a Putnam solution and a linguistics library |
| `HyperbolicSpace`, `LorentzianMetric`, `MinkowskiSpace` | `physicslib__physicslib4`'s AQFT tree only — `StandardMinkowskiSpacetime` as the base of a Haag–Kastler net, not a form of signature $(n,1)$ |
| "divisor" as a word | unrelated: SU(2) matter content in `seiberg-witten`, hyperreals in `hyper-lean`, competition problems |

**Positive control.** The same search finds `QuadraticForm` in 66 packages, so the
method reaches the corpus rather than silently failing — which is the trap
recorded above, where ignore rules made every search return nothing.

**Scope of these negatives, stated exactly.**  What was searched: 94,764 `.lean`
files in 734 packages, the Reservoir index as cloned on 2025-08-15.  How:
identifier and word search, case-insensitive where noted, no build.  What this
does **not** cover: a package added to Reservoir since that clone; a
formalization under a name none of these searches guessed; work in progress on a
branch, in a Zulip thread, or unpublished.  The registry's own refresh
instruction — sweep the Reservoir index, Lean Pool and the community projects
page — is the procedure for the first of those, and it has not been re-run here.

**The live index, too.**  The snapshot above is from 2025-08-15, so the
registry's own refresh procedure was run against the current index —
`just source-sweep` in `lean-categories`, which clones `leanprover/reservoir-index`
and prints the Mathlib-dependent packages it does not already link.  **338
packages** came back.  By description exactly two could bear on the nine atoms,
and neither does: `Xiyou-Wu/RiemannianGeometry` **no longer resolves on GitHub**
— a dead index entry — and `pitmonticone/Hochster` is two files, one of them
`Example.lean`, with no declarations.  Everything else in the 338 is complexity
theory, verification benchmarks, course material or puzzles; the word "complex"
in that list is computational complexity every time.

**What this settles.**  The nine atoms are not absent from the places already
looked; they are absent from every public Lean package this machine can see, and
so from Mathlib, from the 277 registry repositories, and from Reservoir.  A leaf
of this graph cannot bottom out in existing external code for the same reason:
for these notions there is no existing external code, anywhere, to bottom out in.
That is a fact about the state of formalization, not about this file, and the
right response to it is to write the nine.

### Greenfield — no formalization in Mathlib or the registry

| Nodes | What must be authored | Nearest thing that exists |
| --- | --- | --- |
| F2.3–F2.9 | Cartan–Dieudonné for an indefinite rational form, the modified Brieskorn spinor norm, $O^*(L) = \tilde O(L)\cap O_-(L)$, its index-2 relation, and surjectivity of $\tau$ on $O_-(L)$ | Mathlib's Cartan–Dieudonné is the positive-definite real case; `lean-categories` spinor-norm files are an unverified route |
| F2.1, F2.2, F2.10, F2.11 | $\tau : O(L)\to O(G_L)$, its kernel $\tilde O(L)$, the Eichler transformation $E_{f,x}$ and the normality of $\mathcal{E}(L)$ | these were terminal against Mathlib on the strength of "group homomorphisms and explicit formulas", and the groups $\tau$ runs between do not exist.  `QuadraticMap.IsometryEquiv` has `refl`, `symm` and `trans` — the groupoid operations — and **no `Group` instance on `Q.IsometryEquiv Q`**, so neither $O(L)$ nor $O(G_L)$ is a group anywhere in the pinned tree, and a homomorphism between them cannot yet be stated.  $E_{f,x}$'s formula is direct over `BilinForm` once $O(L)$ exists to receive it |
| F1.13, F1.14, F1.15, F1.16, F2.14, F3.5, E14, E15, E16, AG20, AG21, AG22, Lo10 | the eleven decomposition nodes: $O(L)$ and $O(q)$ as groups, $\mathrm{div}(v)$ and $v^*$, the doubling $\mathbb{Q}/\mathbb{Z}\to\mathbb{Q}/2\mathbb{Z}$, Milgram's congruence, the genus as an object, a degree-two covering with its deck involution, a Weil divisor, the unipotent radical, $\mathrm{Lie}(G)$, and a descent datum | **no supplier for any of them, and a read substrate for each** — which is what these nodes exist to record.  They were the clauses their parents asserted with nothing under them; each now names, in its own row, the declarations it is written over.  Ten are definitions and one, F1.16, is a theorem.  E15 is the deepest: `rg -i 'WeilDivisor\|Chow\|algebraicCycle'` returns nothing in the pinned tree, and all of E and Cl stands on it |
| F3.1, F3.2 | the genus as an equivalence class, and the local invariants that cut it out | **no supplier**, after both candidates were read: `HassePrinciple` has 38 proof-position `sorry`s with eleven in the Hilbert symbol's own basic file, and `lean-categories`' `Hasse`/`SpinorGenusAdelic`/`DyadicSymbol` are sorry-free but unpublished and their correspondence with these nodes is unverified.  `LegendreQF` settles the ternary diagonal case only |
| E2 | Enriques surfaces and their $K3$ universal cover with the covering involution | **no supplier**: `CoveringSpacesProject` is winding numbers, not covering spaces.  Mathlib's `IsCoveringMap` (`Topology/Covering/Basic.lean`) is the language; the $K3$ double cover needs stratum E's surfaces first |
| F2.12, F2.13 | Eichler's lemma and Proposition 3.7.3 | nothing; the corpus has no Eichler |
| F3.3, F3.4, Nk3–Nk5, F1.11, F1.12, Ni1–Ni10 | Nikulin's existence, uniqueness and one-class-plus-surjectivity theorems; his primitive-embedding classification and the analogue of Witt's theorem; the Minkowski–Siegel weight | nothing |
| F4.2 | Niemeier's classification of the 24 lattices | nothing |
| V1–V13 | $C^\pm$/$C^0$ matrices, $C^-$-polyhedra, Lemmas 2–5, Theorem 1 with (L1)–(L5), Coxeter's diagram classification, Vinberg's algorithm and Proposition 4, the infinite-vertex recovery and its primitivity lemma | Mathlib has finite Cartan matrices and Coxeter groups; **no affine classification, no fundamental polyhedron**.  V10's *spherical* half — that a connected simply-laced diagram is a path or an ADE star — is `adeClassification` in `lean-categories`, proved for the root base of an even negative definite lattice; the affine diagrams $\tilde A$, $\tilde B$, $\tilde C$, $\tilde D$, $\tilde E$ that every one of C3–C7 is stated in are not classified anywhere |
| Lo2, Lo4–Lo9 | Lobachevskii space as the rays in the negative cone, its planes and halfspaces, polyhedral angles, boundedness and finite volume, the hyperboloid metric, and reflection cells | Mathlib has quadratic forms with `sigPos`/`sigNeg` and Sylvester's law of inertia, and convex cones with duals, so Lo1 and Lo3 are within reach.  There is **no hyperbolic $n$-space, and nothing in the hyperboloid model these nodes use** — but dimension two is not missing: `Analysis/Complex/UpperHalfPlane/Metric.lean` puts the hyperbolic metric on $\mathbb{H}$ as a `MetricSpace`, with `dist_eq` in `arsinh`, the half-distance formulas in `sinh`, `cosh` and `tanh`, and hyperbolic circles, beside `MoebiusAction`, `FixedPoints`, `ProperAction` and `Measure`.  That is the rank-one instance of what stratum Lo needs in rank $n$, in a different model |
| BB1–BB8 | parabolic $\mathbb{Q}$-subgroups, hermitian symmetric domains, Harish-Chandra realizations, rational boundary components, the Satake topology, Baily–Borel's Theorem 10.11 | nothing — the registry has no algebraic-groups-with-parabolics corpus and no symmetric-space corpus |
| AF1–AF13 | automorphy factors, $\mathcal{Z}(\mathfrak{g})$-finiteness, Poincaré and Poincaré–Eisenstein series, integral automorphic forms and the $\Phi$ operator, the analyticity criterion, and the projective embedding | Mathlib has universal enveloping algebras and modular forms for $\mathrm{SL}_2(\mathbb{Z})$; `CBirkbeck/ModularForms_Lean4` and `loefflerd/ModularFormDimensions` are the nearest registry entries, both rank one |
| AG1–AG19 | $k$-structures and Galois descent, tori and $k$-split tori, Borel and parabolic subgroups, unipotent radicals and Levi decompositions, Tits systems, the relative root system and $k$-rank, the spherical Tits building and its dimension | Mathlib has affine and smooth group schemes, root systems and Coxeter groups, and nothing above them.  The nearest thing anywhere is **ATLAS's `BNPair`/`BNPairAxioms`** — the abstract Tits system and the building of its parabolics, read-checked in the third sweep — which supplies the group-theoretic layer and none of the algebraic-group input to it; `chrisflav/bruhat-tits` builds the Bruhat–Tits tree of $\mathrm{SL}_2$ over a local field |
| HS1–HS16 | almost-complex structures and Newlander–Nirenberg, Hermitian and Kähler structures, geodesic symmetries, semisimple Lie groups with their Cartan involutions, the Harish-Chandra and Borel embeddings, boundary components and the 5-term decomposition of a normalizer, symmetric cones and Euclidean Jordan algebras | Mathlib has `IsManifold` over `𝓘(ℂ, E)`, the `LieGroup` class, and a two-file Riemannian tree (`Riemannian/Basic`, `Riemannian/PathELength`) with no geodesics; `Geometry/Manifold/Complex.lean` says of itself "There is a whole theory to develop here".  ATLAS has a smoothness-free `AlmostComplexStructure` and an `Integrable` predicate parameterized by the Nijenhuis tensor it never builds — see the third sweep |
| Bo1–Bo5, Ky1–Ky8 | Borel's extension theorem, Kwack's theorem, the Kobayashi pseudo-distance and hyperbolic imbedding | nothing; `kebekus/ProjectVD` covers Nevanlinna theory, adjacent but not these statements |
| Rt1–Rt10 | Iwasawa decompositions, restricted roots, Siegel domains, fundamental sets for arithmetic groups, and the finite-volume and compactness criteria | Mathlib has Haar measure on locally compact groups and no Lie structure theory to apply it to; the rank-one case of the reduction theory *is* there, in `UpperHalfPlane`'s `ProperAction` and `Measure` files under `CongruenceSubgroup`.  `rg -i 'SiegelSet'` finds nothing, and every "Siegel" hit in the pinned tree is Siegel's lemma or Siegel's theorem; ATLAS's `IwasawaData` is a $KAN$ factorization whose $N$ carries no condition, over a `sorry` existence theorem asserted for every topological group |
| E1, E3–E13 | compact complex surfaces, Enriques and $K3$ surfaces, elliptic pencils, Horikawa's isometry, global Torelli, the period map | nothing; `nullstellensatz` gives local complex-analytic geometry only |
| F1.1's $O(L)$, F1.4's signature congruence | $O(L) = \{M : {}^tM G_L M = G_L\}$ as a group, and Milgram's theorem that an even unimodular lattice has $n_+\equiv n_-\pmod 8$ | for $O(L)$, `Matrix.orthogonalGroup` is the unitary group and so the orthogonal group of the identity form only — the general definition is a few lines over `Matrix` and is not written.  For the congruence, nothing: no Milgram, no Gauss sum, no oddity invariant anywhere in the pinned tree |
| F1.6 | Milnor's classification of the even indefinite unimodular lattices as sums of $H$, $E_8$ and $-E_8$ | nothing.  `E_8` arrives as an object through Sphere-Packing-Lean and F1.5; the classification over it is nowhere |
| F5.1 | Niemeier's 24 lattices — the same theorem as F4.2 | nothing; `rg -i --no-ignore niemeier` over Mathlib and all 111 cloned repositories returns no file |
| F5.2, F5.8 | Scattone's Remark 5.1.4 and Corollary 5.6.10, both statements about a **genus** | nothing: the genus of a lattice has no formalization anywhere the registry reaches.  `HassePrinciple` supplies Hilbert symbols with its key proofs `sorry`, which is below these |
| F5.3–F5.7 | Scattone Prop. 6.1.2 and §6.3: $N\cong D_7$, its embeddings into the members of $\mathcal{U}^{24}$, the eight that admit one, the uniqueness failure at $E_8+D_{16}$, and the nine complements | the root lattices $A_n$, $D_n$, $E_6$, $E_7$, $E_8$ are objects in `lean-categories` (`DefiniteNondegenerate`, `DRootLattice`), which is what F4.1 records.  Not one **embedding** statement between root lattices exists there or anywhere else |
| Pa6, Pa9, Pa10, Pa11 | Nikulin §1.8–1.9: Props. 1.8.1 and 1.8.3, the canonical decomposition of a $p$-adic lattice, that $(t_{(+)},t_{(-)},q)$ determines the genus, and the surjectivity and extension corollaries | **Pa9 has a real route**, in `lean-categories`' seven sorry-free `Jordan*` files: the decomposition as data, a modular component, the layer filtration, uniformizer change, and the scale ideal as an isometry invariant.  What is missing there is global existence, uniqueness of the invariant list, and the dyadic case — see the routes table, where the `Invertible (2 : R)` gates are named.  For Pa6, Pa10 and Pa11, nothing.  `gq2-lean` supplies the dyadic Hilbert symbol and 2-adic square classes, which is the layer Pa2–Pa5 and Pa8 sit on and stops strictly below a decomposition theorem for $p$-adic lattices.  Its one occurrence of "Jordan" is Jordan-block concavity in a freeness bound, not a Jordan splitting |
| A1a, A6a, A8, B0, C2, D0 | the paper's own content, in the rows the earlier passes added after this table was written: the 2.11 caveat, the (2.15) special sets, 2.21, the ambient $\Lambda$ and $K$ of 3.3.14–3.3.16, the isotropic vector of Vinberg §1.9, and the crossing of 3.2.4 from orbits to strata | by construction |
| V9a, V11a, V11b | the vertex/edge correspondence in Vinberg's polyhedron, the quantity his algorithm minimizes, and Proposition 4 | with the rest of stratum V: Mathlib has finite Cartan matrices and Coxeter groups, no affine classification and no fundamental polyhedron |
| A0–A7, B1–B8, C3–C12, D1–D7, Cl1–Cl6 | the paper's own content | by construction |

### The two nodes that carry no verdict, and why

`C1` and `Nk2` are marked *superseded* in their own rows: C1's content was
decomposed into stratum V, Nk2's into stratum Pa.  Asking who supplies a node
that has been replaced by other nodes is a question about nothing, so neither
appears in the three tables above, and `check_dag.py` exempts exactly these two.
Their dependency cells point at the nodes that replaced them, which is what makes
the decomposition checkable: if V or Pa lost a node, the edge would dangle.

### What the classification says

Every node of strata A, B, C and D is greenfield **by construction** — they are
the paper's own results, and the point of the project is to prove them.

The foundations split cleanly.  The **lattice-theoretic base is essentially
solved**: F1 is Mathlib plus `lean-categories`, $E_8$ arrives through
Sphere-Packing-Lean, the root lattices $A_n$, $D_n$, $E_6$, $E_7$, $E_8$ are
objects in the corpus already, and the 2-adic layer has a sorry-free supplier in
`gq2-lean`.  The **classification theorems are not**: Nikulin, Niemeier,
Minkowski–Siegel and Eichler have no formalization anywhere the registry knows,
and neither does Cartan–Dieudonné for an indefinite form.

Seven whole strata are greenfield — no supplier for any of their statements,
though *The construction floor* below shows the primitives to write them in are
almost all present: **V** and **Lo**
(hyperbolic reflection groups, Lobachevskii space, Vinberg), **AG** (reductive
groups over a field, parabolic subgroups, the Tits building), **HS** (hermitian
symmetric domains and their boundary components), **AF** (automorphic forms and
the projective embedding), **Rt** and **Ky** (reduction theory, and hyperbolic
imbedding for the extension theorem), and **E** (complex surfaces, $K3$,
Torelli).  **BB** and **Bo** are the paper-level statements sitting on top of
them.  Those are the real cost of the target, and each is a formalization
programme in its own right rather than a node.

Three floors carry everything above them, and each is shared.

**HS, Ky and E share the complex-analytic floor**: an almost-complex structure
on Mathlib's `IsManifold` tree, integrability, a Hermitian metric and a geodesic.
Nothing in those three strata can start before it exists, and whatever pays for
one pays for all three.  It is four definitions over `ContMDiffSection`,
`mlieBracket`, `ContMDiffRiemannianMetric` and `riemannianEDist`, all of which
are in the checkout; see the floor table.

**AG carries HS, Rt, AF and BB.**  HS13 lands on maximal parabolic subgroups,
Rt1 on the Iwasawa decomposition, AF2 on $\mathcal{Z}(\mathfrak{g})$, BB1 on
parabolic $k$-subgroups, and the goal's own $\mathbb{Q}$-rank clause on AG17.
There is no route to the boundary of the Baily–Borel compactification that does
not pass through reductive groups over a field.

**Pa carries Nk, Ni and F3.**  Every one of Nikulin's numbered theorems reduces
to the relations of Pa5 and the canonical decomposition of Pa9, and F3.2 — the
bridge — is Pa10.


## The construction floor

A verdict of "greenfield" says a node has no supplier.  It does not say the node
rests on nothing: a statement that must be authored is still *written over*
something, and if that something does not exist either then the graph has not
bottomed out.  This section names, for every greenfield stratum, the Mathlib
declarations its nodes are constructed from, checked against the checkout.

Strata A, B, C and D have no row and need none: they are the paper's own
results, and what they are written over is the other strata, which the
dependency tables already say node by node.  Every stratum whose nodes are
foundations has a row.

The result is one sentence: **Mathlib supplies the primitives and none of the
statements** — with one exception, stratum E, recorded at the end.  There is no stratum here whose nodes cannot be *written* today;
what is missing is the mathematics, not the vocabulary to say it in.  Where a
primitive is genuinely missing it is called out, and each of those is small.

### Floor for HS, Ky and E — the complex-analytic stratum

| Node | Written over | What must be authored |
| --- | --- | --- |
| HS1 | `TangentSpace`, `ContMDiffSection` (`Geometry/Manifold/VectorBundle/ContMDiffSection.lean`), the hom-bundle of `.../VectorBundle/Hom.lean`, `IsManifold` with `𝓘(ℂ, E)` | $J$ as a section of $\mathrm{End}(TM)$ with $J\circ J = -\mathrm{id}$, and its API |
| HS2 | `mlieBracket`, `mlieBracketWithin` (`Geometry/Manifold/VectorField/LieBracket.lean`) | the Newlander–Nirenberg **equation is writable today**; the theorem is the analysis |
| HS3 | `ContMDiffRiemannianMetric`, `ContinuousRiemannianMetric` (`Geometry/Manifold/VectorBundle/Riemannian.lean`) | $J$-compatibility, and the three-way equivalence of $h$, $g$, $\omega$ |
| HS4 | `Diffeomorph`, `Isometry`, `Subgroup` | $\mathrm{Aut}(M,J,h)$ and the symmetry condition at a point |
| HS5 | `pathELength`, `riemannianEDist` (`Geometry/Manifold/Riemannian/PathELength.lean`) | a geodesic — Mathlib has the length functional and the distance, not the curves that realize it |
| HS8 | `LieGroup` (`Geometry/Manifold/Algebra/LieGroup.lean`), **`GroupLieAlgebra`** (`Geometry/Manifold/GroupLieAlgebra.lean`, the tangent space at the identity, with the bracket built from invariant vector fields and the `LieRing`/`LieAlgebra` instances on it), `LieAlgebra.IsSemisimple` (`Algebra/Lie/Semisimple/Defs.lean`), `killingForm` (`Algebra/Lie/Killing.lean`), `LieAlgebra.IsCartanSubalgebra` | the Cartan involution, and the adjoint-group statement.  The passage from the group to its Lie algebra is in place — which is what separates HS8 from AG2, where the same passage for a group *scheme* is the missing definition |
| HS9 | `Algebra/Lie/BaseChange.lean` for $\mathfrak{g}_\mathbb{C}$, `NormedSpace.exp` (`Analysis/Normed/Algebra/Exponential.lean`), AG4 | $G_\mathbb{C}$ as a group, and the two embeddings |
| HS16 | `ProperCone` (`Analysis/Convex/Cone/Basic.lean`), `dual` (`.../Cone/Dual.lean`), `IsJordan` and `IsCommJordan` (`Algebra/Jordan/Basic.lean`; there is no `JordanRing` — the file states the Jordan identity as a `Prop`-valued class on a `Mul`, not a bundled structure) | the trace form, hence Euclidean Jordan algebras and symmetric cones |
| Ky1, Ky2 | `Complex.UnitDisc` (`Analysis/Complex/UnitDisc/Basic.lean`), `EMetricSpace`, `Metric.infDist`, `iInf` | the Kobayashi pseudo-distance as an infimum over chains of disks — **writable today** |
| E1 | HS1, HS3, `Matrix`, `QuadraticForm/Signature.lean` for the Hodge index | divisors, line bundles, the canonical bundle |

### Floor for AG

| Node | Written over | What must be authored |
| --- | --- | --- |
| AG1 | `Scheme.Over` (`AlgebraicGeometry/Over.lean`, an abbreviation for `OverClass X S`), `IsGalois` (`FieldTheory/Galois/Basic.lean`), `pullback` for base change, and `CategoryTheory.MorphismProperty.Descent` with `AlgebraicGeometry/Morphisms/Descent.lean` | a $k$-structure, and Galois descent **of objects**.  Mathlib's descent is of morphism *properties* — `HasRingHomProperty.descendsAlong` and its siblings — with no descent datum and no twisted form, so the descent AG1 needs is the thing to author, over the $S$-scheme and Galois vocabulary that exists |
| AG2, AG3 | `HopfAlgebra` (`RingTheory/HopfAlgebra/Basic.lean`), `AlgebraicGeometry/Group/Affine.lean` — where `hopfSpec` is the fully faithful $(\mathbf{CommHopfAlg}_R)^{\mathrm{op}} \to \mathbf{Grp}(\mathbf{Sch}/\mathrm{Spec}\,R)$ — `Group/Smooth.lean`, `Scheme`; and for the Lie algebra, `Derivation` with `Derivation.instLieAlgebra` (`RingTheory/Derivation/Lie.lean`) and the differentials of `Algebra/Category/ModuleCat/Differentials/Presheaf.lean` | tori, $k$-split tori, $X^*(T)$ and $X_*(T)$; and $\mathrm{Lie}(G)$, which AG2's verdict cell records as absent.  It is absent as a **definition**: `rg -i 'LieAlgebra\|tangentSpace'` over `Mathlib/AlgebraicGeometry` returns nothing, while the derivations that carry the bracket are in place |
| AG4, AG5 | `AlgebraicGeometry.IsProper` (`Morphisms/Proper.lean`), `UniversallyClosed`, `Subgroup.normalizer` | Borel and parabolic subgroups, Chevalley's theorem |
| AG6, AG7 | `RootPairing`, `RootSystem` (`LinearAlgebra/RootSystem/`), `CoxeterMatrix`, `CoxeterSystem` (`GroupTheory/Coxeter/`) | root subgroups, the Tits system, Bruhat decomposition |
| AG13 | `Module.rank`, `Subgroup`, AG3 | the $k$-rank, over the conjugacy theorem AG12 |
| AG16, AG17 | `SimplicialComplex` (`Analysis/Convex/SimplicialComplex/Basic.lean`; also the abstract one in `AlgebraicTopology/SimplicialComplex/Basic.lean`) | the building from the poset of parabolic $\mathbb{Q}$-subgroups, and its dimension |

### Floor for Rt and AF

| Node | Written over | What must be authored |
| --- | --- | --- |
| Rt1 | `NormedSpace.exp`, `Algebra/Lie/Weights/` for restricted roots | the Iwasawa decomposition |
| Rt2, Rt3 | `IsCompact`, `Set` algebra, Rt1 | the Siegel domain |
| Rt4, Rt9 | `MeasureTheory.Measure.haar`, `IsHaarMeasure` (`MeasureTheory/Measure/Haar/Basic.lean`); `Analysis/Complex/UpperHalfPlane/{ProperAction,Measure}.lean` for the rank-one case already carried out | the finite-volume theorems |
| Rt5 | `Subgroup.Commensurable`, `Subgroup.commensurator` (`GroupTheory/Commensurable.lean`), `Subgroup.index`, `Subgroup.FG` | **nothing** — commensurability of subgroups is Mathlib's own definition, with the commensurator and its `refl`/`symm`/`trans` API |
| AF2 | `UniversalEnvelopingAlgebra` (`Algebra/Lie/UniversalEnveloping.lean`), `Subalgebra.center` | $\mathcal{Z}(\mathfrak{g})$-finiteness |
| AF4, AF5 | `Summable`, `tsum`, `TendstoUniformlyOn`, `MeasureTheory` convolution | the Poincaré series and its convergence — **the statement is writable today** |
| AF10 | `Topology/Sheaves/`, `AnalyticOn`, `TopologicalSpace` | normal analytic spaces, and the criterion over them |
| AF12 | `Projectivization` (`LinearAlgebra/Projectivization/Basic.lean`), `AlgebraicGeometry.Scheme` | the embedding theorem |

### Floor for Lo and V

| Node | Written over | What must be authored |
| --- | --- | --- |
| Lo1, Lo3 | `QuadraticForm`, `sigPos`, `sigNeg` (`LinearAlgebra/QuadraticForm/Signature.lean`) | **nothing** — these are definitions over what exists |
| Lo2, Lo4, Lo5 | `Convex`, `Submodule`, `Set.iInter`, `IsOpen` | $\Lambda^n$ as rays in the cone, polyhedral angles, finite volume as a closure condition |
| Lo6, Lo9 | `Matrix`, `Matrix.rank`, `Real.cos`, `Subgroup.closure` | the Gram matrix of a polyhedron, reflection cells |
| Lo7, Lo8 | `Real.cosh`, `Real.sinh`, **`Real.arcosh` (`Analysis/SpecialFunctions/Arcosh.lean`)**, `Matrix.det`; and `Analysis/Complex/UpperHalfPlane/Metric.lean` as the worked model, where the same shape is carried out in `arsinh` for $\mathbb{H}$ | the hyperbolic distance is $\mathrm{arcosh}\langle P,Q\rangle$ — **writable today**, and the upper-half-plane file shows how far the API around such a definition is expected to go |
| V1–V10 | `Matrix`, `Matrix.rank`, `CoxeterMatrix`, `QuadraticForm/Signature.lean` | the $C^{\pm}$/$C^0$ conditions, Theorem 1, the affine classification |
| V11–V13 | Lo7, `Nat.rec`, `sInf` | the algorithm as a recursion, and Proposition 4 |

### Floor for BB and Bo — the paper-level statements

| Node | Written over | What must be authored |
| --- | --- | --- |
| BB1–BB4 | AG4 and AG5's parabolics, `AlgebraicGeometry.IsProper`, `Subgroup.normalizer` (`Algebra/Group/Subgroup/Defs.lean`) | parabolic $k$-subgroups, the unipotent radical — `rg -i 'unipotentRadical\|IsUnipotent'` over the pinned tree returns **nothing**, so this one is a definition to write over `Subgroup` and the group-scheme tree — and rational boundary components |
| BB5–BB8 | `instTopologicalSpaceQuotient` and `TopologicalSpace.coinduced` (`Topology/Constructions.lean`, `Topology/Order.lean`), `Setoid`, `Projectivization` | the Satake topology as a topology on the disjoint union of $X$ with its rational boundary components, and Baily–Borel's Theorem 10.11 — that the quotient carries a projective structure |
| Bo1–Bo5 | Ky1's pseudo-distance, `Complex.UnitDisc` (`Analysis/Complex/UnitDisc/Basic.lean`), `MDifferentiable` (`Geometry/Manifold/MFDeriv/Defs.lean`) over `𝓘(ℂ, E)` | holomorphic maps out of a product of punctured discs, and the extension theorem over a hyperbolically imbedded target |

### Floor for the greenfield F rows, and for Ni and Nk

| Node | Written over | What must be authored |
| --- | --- | --- |
| F2.1, F2.2, F2.10, F2.11 | `QuadraticMap.IsometryEquiv` with its `refl`/`symm`/`trans`, `LinearEquiv`, `Subgroup`, `MonoidHom`, `BilinForm` | $O(L)$ and $O(G_L)$ **as groups** first — the group structure follows from the three groupoid operations and is a few lines — then $\tau$ between them, then $E_{f,x}$, whose formula needs nothing further |
| F2.3–F2.9 | **`Module.preReflection` and `Module.reflection`** (`LinearAlgebra/Reflection.lean`): $y \mapsto y - f(y)\,x$ for $x \in M$ and $f \in M^\vee$ over any `CommRing`, involutive once $f x = 2$, with `preReflection_preReflection` for conjugates.  Plus `LinearMap.BilinForm.orthogonal`, `MonoidHom.ker`, `Subgroup.index` | the factorization of an element of $O(L_\mathbb{Q})$ into reflections for an **indefinite** rational form, the Brieskorn spinor norm over it, and the index-2 relations.  The reflection itself needs no work: the file sits in the root-system neighbourhood but its definition is general, and $f$ is the correlation applied to $x$ |
| F3.3, F3.4, Nk3–Nk5, F1.11, F1.12, Ni1–Ni10 | F1.10's discriminant form, `ZLattice`, `AddGroup.rank`, `Nat.card`, `Submodule.torsion` and `RingTheory/Flat/TorsionFree.lean` for a free quotient, `GroupTheory/FiniteAbelian/Basic.lean` for the structure of $A_q$, `Matrix.det`, and the signature file for $\mathrm{sign}\,q$ | Nikulin's existence, uniqueness, one-class-plus-surjectivity and primitive-embedding theorems.  Every hypothesis in them — $\ell(A_q)$, the sign condition mod 8, torsion-freeness of $M/S$ — is expressible in the vocabulary above; the theorems are the work |
| F4.2, F5.1–F5.8 | `Matrix/Cartan.lean`, `ADEInequality.Admissible` (`NumberTheory/ADEInequality.lean`), injective `LinearMap` with `Submodule.map` for an embedding, `Submodule.torsion` for primitivity | Niemeier's classification, and Scattone §6.3's embeddings of $D_7$ into its members with their complements.  An embedding of root lattices is a linear map with a form condition, which is writable; that these eight admit one and that $E_8+D_{16}$ admits two are the theorems |

### Floor for the decomposition nodes

These eleven were split out of parents whose rows asserted them without a
definition.  Each is greenfield, and the point of splitting them is that what
each is written over is now named and read.

| Node | Written over | What must be authored |
| --- | --- | --- |
| F1.13, F2.14 | `LinearEquiv`, `AddEquiv`, `Subgroup`, and `QuadraticMap.IsometryEquiv`'s `refl`, `symm`, `trans` (`QuadraticForm/IsometryEquiv.lean`) | the `Group` instance on the self-isometries of a form, for a lattice and for a finite quadratic form.  The three operations are there; **no `Group` instance over them is**, which is why F2.1's $\tau$ could not be stated |
| F1.14 | `BilinForm.dualSubmodule` and `dualSubmoduleParing` (`BilinearForm/DualLattice.lean`), `Ideal.span`, `Int.gcd` | $\mathrm{div}(v)$ as the generator of the ideal $(v,L)$, and $v^*$ in $G_L$ |
| F1.15 | `AddCircle (1 : ℚ)`, `AddCircle (2 : ℚ)` (`Topology/Instances/AddCircle/Defs.lean`), `QuotientAddGroup.map`, `QuadraticMap.polar` | the doubling map and the compatibility that makes F1.9's second axiom sayable |
| F1.16 | `gaussSum` (`NumberTheory/GaussSum.lean`) over `AddChar` and `MulChar`, `sigPos`/`sigNeg` | the Gauss sum of a discriminant form, its absolute value, and the congruence.  Everything in the statement exists; the theorem is Milgram's |
| F3.5 | `Setoid`, `Quotient`, with F1.3's signature and F1.10's form as the two components | the relation and the quotient.  Both components are read-verified, so the genus as an **object** bottoms out even though F3.3's one-class theorem is a Nikulin theorem |
| E14 | `IsCoveringMap`, `IsEvenlyCovered`, `IsCoveringMapOn` (`Topology/Covering/Basic.lean`), `Topology/Covering/Quotient.lean`, `Topology/Homotopy/Lifting.lean` | the fibre-cardinality-two condition, and the **deck involution** — `rg -i deck` over that tree returns nothing, so the automorphism over the base is the content |
| E15 | `Finsupp`, `Order.height` (`Order/KrullDimension.lean`), `Scheme.functionField` and `germToFunctionField_injective` (`AlgebraicGeometry/FunctionField.lean`), `IsIntegral` | the free abelian group on the codimension-one points, the principal divisor of a rational function, and linear equivalence.  The pieces are a free group, a height and a function field, all present; the divisor is not |
| Lo10 | `IsConnected`, `IsPreconnected`, `ConnectedComponents`, `Convex`, with `sigNeg` fixing the index | that the negative cone has two components.  Each sheet is convex, which is the usual route, and no part of it is in the tree |
| E16 | `IsDiscreteValuationRing` with `addVal` (`RingTheory/DiscreteValuationRing/Basic.lean`), `IsIntegrallyClosed`, `Order.height` | that the local ring at a codimension-one point of a normal integral scheme is a DVR, and the valuation it gives on the function field |
| AG20 | `Subgroup.normalizer`, `Subgroup.closure`, `AlgebraicGeometry/Group/Smooth.lean` | unipotence itself, the radical as the maximal connected normal unipotent subgroup, and the Levi splitting |
| AG21 | `Derivation` with `Derivation.instLieAlgebra` (`RingTheory/Derivation/Lie.lean`), the presheaf of differentials, `hopfSpec` (`AlgebraicGeometry/Group/Affine.lean`) | $\mathrm{Lie}(G)$ as the tangent space at the identity with the bracket.  `Geometry/Manifold/GroupLieAlgebra.lean` does exactly this for a Lie group and is the model |
| AG22 | `Scheme.Over` (`AlgebraicGeometry/Over.lean`), `pullback`, `IsGalois` (`FieldTheory/Galois/Basic.lean`), `MorphismProperty.Descent`, `AlgebraicGeometry/Morphisms/Descent.lean` | the descent datum and the twisted form.  Mathlib's descent is of morphism properties, so the objects are the content |

### Floor for Pa

| Node | Written over | What must be authored |
| --- | --- | --- |
| Pa6, Pa9, Pa10, Pa11 | `PadicInt`, `Padics`, `IsDiscreteValuationRing` (`RingTheory/DiscreteValuationRing/Basic.lean`), `Irreducible` for a uniformizer, `Ideal.span`, `QuadraticForm`, `legendreSym` (`NumberTheory/LegendreSymbol/`) for the square classes | the canonical decomposition and the genus corollaries.  Note what is **not** in the pinned tree: no Hilbert symbol — `rg -i hilbertSymbol` returns nothing — and no quadratic form over $\mathbb{Z}_p$ anywhere in `Mathlib/LinearAlgebra`.  Both exist outside it, the Hilbert symbol in `gq2-lean` and `HassePrinciple`, the $p$-adic lattice in `lean-categories`' `Jordan*` files, which is why Pa's verdicts point at corpora rather than at Mathlib |

### Floor for E and Cl — the surfaces

| Node | Written over | What must be authored |
| --- | --- | --- |
| E3–E13, Cl1–Cl6 | HS1 and HS3's complex-analytic floor, `Projectivization`, `AlgebraicGeometry.Scheme`, `Complex` | divisors, line bundles and the canonical bundle first — `rg -i divisor` over `Mathlib/AlgebraicGeometry` returns only elliptic-curve and function-field files, with **no Weil or Cartier divisor** — then Enriques and $K3$ surfaces, elliptic pencils with multiple fibres, Horikawa's isometry, global Torelli and the period map.  This is the deepest floor in the graph: everything above the first cell is a formalization programme |

### What this changes

Nothing in the terminality verdicts: no greenfield node acquired a supplier, and
`check_dag.py` is unaffected.  What it removes is the reading that the greenfield
strata are blocked on missing foundations.  They are not.  Six rows above are
marked writable today — Newlander–Nirenberg's equation, the Kobayashi
pseudo-distance, the Poincaré series, the hyperbolic metric, Lo1 and Lo3 — and
the rest need definitions over primitives that exist, not primitives that do not.

`Commensurable` was once listed here as the single missing primitive and is
not missing: it is `Subgroup.Commensurable` in `GroupTheory/Commensurable.lean`,
and the search that reported it absent was `rg "def Commensurable"` against a
declaration that reads `def Subgroup.Commensurable`.

What the enlarged table does show missing splits in two, and the split is the
whole point of the section.

**Definitions to author over primitives that exist.**  $\mathrm{Lie}(G)$ for a
group scheme is nowhere in `Mathlib/AlgebraicGeometry`, and the bracket it would
carry is `Derivation.instLieAlgebra`.  Galois descent of objects is nowhere, and
the $S$-scheme and Galois vocabulary it would be stated in is in place.  The
unipotent radical is nowhere, over a `Subgroup` tree that is.  Each of the three
is a short definition, and none of them is infrastructure.

**One genuine gap in the infrastructure**, and it is under E and Cl: Mathlib has
no Weil or Cartier divisor, so it has no line bundles on a surface and no
canonical bundle.  Every statement of stratum E is about those, so E is not in
the position of the other strata: it needs the vocabulary built first.  That is
recorded in the E1 row and in the floor for E and Cl.

So the cost has two shapes, not one.  For **AG, HS, Ky, Rt, AF, Lo, V, BB, Bo, F,
Ni and Nk** it is **theorems, not infrastructure**: the analysis in
Newlander–Nirenberg, the structure theory in Borel §§20–21, the convergence
estimates in Baily–Borel §§5–8, Vinberg's Theorem 1 and Nikulin's classification
are the work, while the tangent bundles, Lie brackets, Haar measures, Hopf
algebras, simplicial complexes, proper morphisms, reflections, root systems,
cones, quotient topologies and hyperbolic functions they are written over are all
in the pinned checkout.  For **E and Cl** it is infrastructure first and theorems
after.

## The leaves, clause by clause

A leaf of this graph is a node whose dependency cell names no other node, so the
graph stops there and the cell's declarations are the whole of what it rests on.
Naming declarations is not the same as those declarations *supplying* the node:
a node's statement has several clauses, and the interesting case is a cell that
supplies four of five.  Every leaf is taken apart below.  Seven nodes, twenty-six
clauses, of which fifteen are supplied by a declaration read in the pinned tree
and eleven are the content to author.  Two clauses turned out to be distinct
statements with their own dependencies and became nodes, Lo10 and E16.

**Lo1** — $E^{n,1}$ and its cone.

| Clause | Supplied? |
| --- | --- |
| a real $(n+1)$-space with a scalar product | `QuadraticForm ℝ E` with `Module.finrank ℝ E = n+1` — **yes** |
| **nondegenerate** | **yes, and not by the obvious name**: nondegeneracy is `QuadraticMap.radical Q = ⊥` (`QuadraticForm/Radical.lean`).  It is *not* `Anisotropic`, which says no nonzero vector is isotropic and is **false for $E^{n,1}$** — the light cone is exactly its isotropic vectors.  A row citing `QuadraticForm` without saying which predicate invites that substitution |
| negative inertial index 1 | `sigNeg Q = 1` — **yes**, and over $\mathbb{R}$ Sylvester's law is available to compute it |
| the cone $V = \{x : (x,x)<0\}$ | a `Set`, from the form — **yes** |
| $V$ has exactly **two** connected components $V_\pm$ | **no.** This is a theorem about the topology of the negative cone of a form of index 1, and nothing in the pinned tree states it.  It is now **Lo10** |

**V1** — $C^+$-matrices.

| Clause | Supplied? |
| --- | --- |
| positive matrices of order $n$ | `Matrix.PosDef` (`LinearAlgebra/Matrix/PosDef.lean`) — **yes** |
| **nondecomposable** | **no.** `Matrix.blockDiagonal` builds a block matrix; no predicate says a matrix is *not* one after a permutation of the index set.  The condition is a few lines over `Equiv.Perm` and `blockDiagonal`, and it is unwritten |
| all entries of the inverse positive | `Matrix.nonsing_inv` (`Matrix/NonsingularInverse.lean`) with an entrywise inequality — **yes** |
| each is the Gram matrix of a **unique simplicial angle** in $E^n$ | **no.** A bijection between such matrices and simplicial angles; the angle itself is Lo2's territory and the uniqueness is Vinberg's |

**Pa1** — the semigroups of forms.

| Clause | Supplied? |
| --- | --- |
| $\mathbb{Z}_p$ | `PadicInt` — **yes** |
| forms over it | `QuadraticMap ℤ_[p]` — **yes** |
| the **semigroup operation** | `QuadraticMap.prod` with `Isometry.inl`/`inr` — **yes**, and the row already records that the pointwise `AddCommMonoid` is the wrong operation |
| a semigroup of **isomorphism classes** | **no, and there is a size condition in the way.** Nikulin's $\mathrm{qu}(\mathbb{Z}_p)$ ranges over all forms on all finitely generated modules, which is not a set.  It becomes one by fixing representatives — forms on `Fin n → ℤ_[p]` indexed by `n : ℕ`, quotiented by `QuadraticMap.IsometryEquiv` — and that choice is the construction to write |

**HS1** — complex and quasi-complex manifolds.

| Clause | Supplied? |
| --- | --- |
| a complex manifold as $(M,\mathcal{O}_M)$ locally isomorphic to $(\mathbb{C}^N,\mathcal{O}_{\mathbb{C}^N})$ | **in a different formulation.** Mathlib's complex manifold is `IsManifold` over `𝓘(ℂ, E)` — an atlas of holomorphic charts, not a structure sheaf.  The two agree, and that agreement is a theorem nobody here has stated.  Viviani's definition is the sheaf one |
| $J$ a $(1,1)$-tensor field | a section of $\mathrm{End}(TM)$: `ContMDiffSection` over the hom-bundle of `.../VectorBundle/Hom.lean` — **yes** |
| $J_p^2 = -\mathrm{id}$ on $T_pM$ | pointwise over `TangentSpace` — **yes** |

**AF10** — the analyticity criterion.

| Clause | Supplied? |
| --- | --- |
| $V$ locally compact, second countable | `LocallyCompactSpace`, `SecondCountableTopology` — **yes** |
| a locally finite disjoint union | `Set` and filter language — **yes** |
| **irreducible normal analytic space** | **no**, and this is the row's own admission |
| the stratification $V_{(d)}$ by **dimension**, with $V_0$ dense of full dimension | **no.** A dimension function on an analytic space; the row did not mention this clause at all |
| the sheaf of $\mathcal{Q}$-functions | **no.** `Topology/Sheaves/` gives sheaves on a space; the $\mathcal{Q}$-functions are Baily–Borel's own construction |
| conditions (ii) and (iv), on neighbourhood systems and local separation | expressible in filter and `Set` language once the objects above exist — **yes, conditionally** |

**E14** — a degree-two covering with its deck involution.

| Clause | Supplied? |
| --- | --- |
| a covering map | `IsCoveringMap` (`Topology/Covering/Basic.lean`) — **yes** |
| fibres with **two** elements | **yes, exactly**: `IsEvenlyCovered f x (Fin 2)` is `DiscreteTopology (Fin 2)` together with a local trivialization $f^{-1}(U) \simeq_{\mathrm t} U \times \mathrm{Fin}\ 2$ over $x$, and `IsEvenlyCovered.fiberHomeomorph` identifies `Fin 2` with the fibre.  This is a better match than the row claimed |
| the **deck involution** | **no.** `rg -i deck` over `Topology/Covering/` returns nothing; the automorphism over the base, and that it is an involution, are the content |

**E15** — a Weil divisor.

| Clause | Supplied? |
| --- | --- |
| the codimension-one points | `Specializes` (`Topology/Defs/Filter.lean`, $\mathfrak{n} \leadsto$) with `Order.height` in that order — **yes** |
| the free abelian group on them | `Finsupp` — **yes** |
| the **order of vanishing** of a rational function at such a point | **conditionally, and it needs a hypothesis the node did not state**: `IsDiscreteValuationRing.addVal` (`RingTheory/DiscreteValuationRing/Basic.lean`) is the valuation, and it applies once the local ring at a codimension-one point *is* a DVR, which needs normality.  That chain is now **E16** |
| the principal divisor, and linear equivalence | over E16 and a quotient — **yes, once E16 exists** |

### Eight atoms, Lo10, and F1.16's Gauss sum now exist in `lean/Atoms.lean`

The searching stopped where it had to: five sweeps established that these
notions are in no indexed Lean code.  The remedy for that is to write them, and
eight are written — `lean/Atoms.lean`, beside this file, compiled against the
pinned Mathlib with `lake env lean` from the `lean-categories` checkout, no
error, no warning, no `sorry` and no `axiom`.

| Node or clause | Declaration |
| --- | --- |
| F1.13, $O(L)$ as a group | `Sterk.orthogonalGroup (B : LinearMap.BilinForm R M) : Subgroup (M ≃ₗ[R] M)`, with `mem_orthogonalGroup_iff` |
| F2.14, $O(q)$ as a group | `Sterk.quadraticOrthogonalGroup (Q : QuadraticMap R M N) : Subgroup (M ≃ₗ[R] M)`, with its membership lemma.  At $Q = q_L$ this is $O(G_L)$, so F2.1's $\tau$ now has both a domain and a codomain |
| F1.14, $\mathrm{div}(v)$ | `Sterk.divisorIdeal (B) (v) : Ideal R` as the range of $y \mapsto B\,v\,y$, with `mem_divisorIdeal_iff` and `HasDivisorOne` — the hypothesis of Sterk 3.2.1 |
| F1.15, the doubling $\mathbb{Q}/\mathbb{Z}\to\mathbb{Q}/2\mathbb{Z}$ | `Sterk.doubling : AddCircle (1 : ℚ) →+ AddCircle (2 : ℚ)`, through `QuotientAddGroup.map` on `AddMonoidHom.mulLeft 2` |
| E14's deck involution | `Sterk.DeckTransformation (f : E → X)` — a homeomorphism of the total space with `over_base` — its `CoeFun`, `id`, `IsInvolution`, and `IsInvolution.symm_apply` |
| V1's nondecomposability | `Sterk.Matrix.IsDecomposable` and `IsIndecomposable`: a re-indexing $n \simeq \iota \oplus \kappa$ with both parts nonempty and the off-diagonal blocks zero |
| Pa1's semigroup of classes | `Sterk.PadicForm` (a rank and a form on `Fin rank → ℤ_[p]`, which is the choice of representatives that makes the collection a set), `Isometric` with its refl/symm/trans, `isometricSetoid`, `orthogonalSum` — `QuadraticMap.prod` carried along `finSumFinEquiv` and `sumArrowLequivProdArrow` — and `PadicFormClasses` as the quotient |
| F1.16's Gauss sum, and eight steps of its proof | `Sterk.ratCircleToRealCircle : AddCircle (2 : ℚ) →+ AddCircle ((2 : ℚ) : ℝ)`, because a discriminant form is valued in `ℚ/2ℤ` while the circle character is stated for a real period; **`Sterk.discriminantGaussSum`**, the sum over `AddCircle.toCircle_addChar`; `discriminantGaussSum_zero`, that the zero form's sum is the group's order; and `MilgramStatement`, the theorem written out as a proposition about the data.  Mathlib's `gaussSum` is for a `MulChar`/`AddChar` pair on a finite ring, which a discriminant form is not, so this object existed nowhere.  Four steps of the proof are now proved on top of it: `norm_gaussTerm` (each term has modulus one), `discriminantGaussSum_mul_conj` (the sum times its conjugate expands over pairs — the identity Milgram's proof starts from), `gaussTerm_add` with `gaussTerm_zero` (the terms are multiplicative in the value, so a difference of values contributes one term), and `conj_gaussTerm` (conjugation inverts a term, proved through `Complex.mul_conj` and the modulus).  Four more carry it further: `gaussTerm_sub`, `sum_gaussTerm_reindex` (the substitution $b = a+c$, by `Fintype.sum_equiv (Equiv.addLeft a)`), `discriminantGaussSum_mul_conj_eq_sum_diff` (so the squared modulus is a double sum over a point and a **difference**), and `sum_gaussTerm_diff_factor` — under the polar identity, which is what F1.15's doubling makes sayable and which the theorem takes as a **hypothesis** rather than assuming about $q$, the $a$-sum factors into a term in $c$ alone times a character sum in $a$.  What is left is `AddChar.sum_eq_ite` on that character sum, which needs `fun a => -(\mathrm{pol}\ a\ c)` packaged as an `AddChar`, and then the count of radical elements against the signature |
| Lo10, **complete** | `Sterk.lorentz` (the standard form $-x_0^2+\sum_{i>0}x_i^2$ on `Fin (n+1) → ℝ`, which is Vinberg's $E^{n,1}$), `negativeCone` with `upper` and `lower`, `lorentz_continuous`, and the substantive lemma **`ne_zero_of_mem_negativeCone`** — on the cone the zeroth coordinate never vanishes, since if it did the form would be a sum of squares there.  From it: `negativeCone_eq_union`, `upper_disjoint_lower`, `isOpen_upper`, `isOpen_lower`.  Together these say the cone is disconnected by the sign of the zeroth coordinate, which is the half Sterk and Vinberg use when they fix $V_+$.  The other half is proved too: `lorentzPair` with `lorentz_smul_add`, then **`lorentzPair_neg_of_mem_upper`** — the reverse Cauchy–Schwarz inequality, that the pairing of two future-directed vectors is negative, over `Finset.sum_mul_sq_le_sq_mul_sq` — and from it `convex_upper` and `convex_lower`, the second by negation through `lorentz_neg`.  `negativeCone_two_components` collects the six facts that say **exactly two components**: each sheet preconnected, disjoint, open, and covering |
| E15's Weil divisors | `Sterk.codimOnePoints` and `Sterk.WeilDivisor (X : Scheme) := codimOnePoints X →₀ ℤ` with its `AddCommGroup` instance and `WeilDivisor.single`.  **The order convention is the substance here**: Mathlib's `specializationPreorder` has $x \le y \iff y \leadsto x$, so a generic point is a *greatest* element and codimension is `Order.coheight`, not `Order.height` — the floor row for E15 had named `height`, which is the wrong end |

These are **definitions**, and that is the point: each was a clause a leaf
asserted with nothing under it, and each now resolves to a declaration that
compiles.  What they are not is the mathematics above them — `orthogonalGroup`
does not prove Sterk 2.13, and `DeckTransformation` does not produce the $K3$
double cover.  A definition existing is exactly what "bottoms out" can mean for
a node nobody has proved.

**One definition remains, and it is a programme rather than a declaration.**
AF10's normal analytic space needs a local model — the zero set of finitely many
holomorphic functions with the quotient of the structure sheaf — and the chain
under it is: the structure sheaf and its locally-ringed packaging **exist**
(`ChartedSpace.locallyRingedSpace`, `Mathlib/Geometry/Manifold/Sheaf/LocallyRingedSpace.lean`,
with the stalks proved local, and `smoothSheaf` in `Sheaf/Smooth.lean`); the ideal
sheaf and its quotient do **not**, though `CategoryTheory.Sites.Sheafification`
supplies the machine for the quotient.  So the definition is reachable and is
several files of work, not ten lines, and writing it badly — a definition whose
class of models is empty — would be worse than leaving it named.  The dimension
stratification and the $\mathcal{Q}$-functions sit above it.

Lo10 is **done**, both halves.  F1.16 now has its **object** — the Gauss sum of
a discriminant form, which existed nowhere — and `MilgramStatement` writes the
theorem out as a proposition, marked in the file as a statement and not a proof.
Eight steps of the proof are proved on it, down to the point where the sum
factors.  Two things are left: packaging `fun a => -(\mathrm{pol}\ a\ c)` as an
`AddChar` so that `AddChar.sum_eq_ite` evaluates the inner sum, and counting the
radical against the signature.  Neither needs a new object, and the file carries
the route step by step, which is what makes the remainder a list rather than a
name.

### Where the decomposition stops, and why it stops there

Eleven clauses above are content rather than substrate.  Two of them were
composites and became nodes with dependencies of their own — Lo10, because "the
cone has two components" is a theorem about the topology of a form of index 1,
and E16, because "the order of vanishing" needs the local ring to be a DVR and
so needs normality.  The other nine cannot be split again:

| Atom | Its kind | Written over |
| --- | --- | --- |
| the deck involution of a two-sheeted covering | one definition | `IsCoveringMap`, `IsEvenlyCovered` |
| nondecomposability of a matrix | one definition | `Equiv.Perm`, `Matrix.blockDiagonal` |
| a normal analytic space | one definition | `Topology/Sheaves/`, `AnalyticOn` |
| the dimension stratification $V_{(d)}$ | one definition | a dimension function on the above |
| the sheaf of $\mathcal{Q}$-functions | one definition | `Topology/Sheaves/`, over the above |
| the semigroup of isometry classes of $p$-adic forms | one construction, with a choice of representatives | `QuadraticMap.prod`, `IsometryEquiv`, `Fin n → ℤ_[p]` |
| the Gram-matrix/simplicial-angle bijection | one theorem | V1, Lo2 |
| chart-atlas and structure-sheaf complex manifolds agree | one theorem | `IsManifold` over `𝓘(ℂ, E)`, `Topology/Sheaves/` |
| $O(L)$, $O(q)$, $\mathrm{div}$, $v^*$, the doubling, Milgram, the genus, $R_u(P)$, $\mathrm{Lie}(G)$, the descent datum, the Weil divisor | one definition each, and one theorem (Milgram) | their own nodes, F1.13–F1.16, F2.14, F3.5, E15, AG20–AG22 |

Each of those is a single definition or a single theorem, stated over
declarations read in the pinned tree.  There is nothing left to split: a
definition is not a composite of smaller nodes, and the recursion has reached
what must be *written* rather than what must be *found*.  That is the sense in
which this graph now bottoms out — not that every statement is supplied, since
no node in this graph is supplied and the project exists to prove them, but that
no cell anywhere defers to something unlocated.

The distinction worth keeping: **found** versus **written**.  Everything the four
sweeps could find has been found, and each row says which declaration and where
the match stops.  What is left is authorship, and the eleven atoms above plus the
theorem nodes are its unit of work.

## Open audit points

Questions about statements already in the graph, not missing nodes.

1. ~~Sign convention~~ — **settled by computation.**  Scattone's $E_8$ (his
   §3.1: $\mathbb{Z}^8$ with the *negative* Cartan matrix, flagged there as a
   deviation) is **equal** to Sterk's $E_8(-1)$; both are even, negative
   definite, determinant 1.  $E_8(-2) = -2C$ has determinant 256 and elementary
   divisors all 2, so its discriminant group is $(\mathbb{Z}/2)^8$ — which
   independently confirms the $\ell(A_{L_-}) = 10$ the A2 and A3 checks rest on.
   The readings agree, and the Sage reconstruction already uses $-2C$.
2. **Spinor norm convention.** Scattone's $\sigma_-$ follows Brieskorn and is a
   modified form of the usual spinor norm; he says so at §3.6.  Any node reading
   "the spinor norm" unqualified is ambiguous.
3. ~~Rank hypotheses~~ — **settled below**.
4. ~~A3's conditions~~ — **settled below**.
5. **Borel's torsion-free hypothesis (Bo1) fails as stated** — narrowed by
   stratum Ky, not closed.  $-\mathrm{id}$ lies in $O(L_-)$, acts trivially on
   the discriminant form and so lies in $\Gamma$, and has order 2 — so $\Gamma$
   is **not** torsion-free and Theorem A does not apply to it directly.  Borel's
   Remark 3.8 records that with torsion $V$ need not be hyperbolically imbedded
   in $V^*$.  The repair is **not** passing to a neat subgroup: Kiernan and
   Kobayashi record (Ky5) that for a non-free action one replaces the intrinsic
   pseudo-distance of the quotient by the distance induced from the domain, and
   the hyperbolic-imbedding statement holds in that form.  What is left is to
   read Kobayashi–Ochiai 1971 for the modified condition, and to check that the
   extension Sterk invokes follows from Ky6 in it.  That paper is open access at
   `10.2969/jmsj/02320340` and needs one manual download — Project Euclid blocks
   scripted requests; see `REFERENCES.md`.
6. ~~V13's primitivity hypothesis~~ — **settled below, and it fires.**
7. ~~C7 disagrees with the source~~ — **settled; the error was in the reading.**
   The figure on p. 64 lists **five** parabolic subdiagrams for (3.3.12), not
   four: $\tilde A_7\oplus\tilde A_1$, $\tilde C_4\oplus\tilde C_4$,
   $\tilde C_6\oplus\tilde C_2$, $\tilde B_3\oplus\tilde B_3\oplus\tilde C_2$,
   $\tilde C_8$.  The count of four came from a text line quoting only part of
   the list.  The reconstruction'''s thirteen subdiagrams collapse to exactly
   these five, including the three-component one; the residual differences are
   $\tilde B$ where Sterk writes $\tilde C$, which is audit point 2 and not a
   mathematical discrepancy.

### Two settled by computation

$L_-$ has signature $(2,10)$, rank 12, discriminant group
$(\mathbb{Z}/2)^2\oplus(\mathbb{Z}/2)^8 = (\mathbb{Z}/2)^{10}$, so
$\ell(A_{L_-}) = 10$ concentrated at $p=2$ and $\ell(A_{q_p}) = 0$ for odd $p$.

**A3 cannot use Nikulin's Corollary 1.13.3**, the convenient
existence-and-uniqueness form: it requires $t_{(+)}+t_{(-)} > 2+\ell(A_q)$, and
$12 > 12$ is **false by exactly one**.  A3 must go through the full Theorem
1.13.2, whose conditions are alternatives — (2) is vacuous for odd $p$ since
$12 \ge 2+0$, and (3) at $p=2$ offers $\mathrm{rk}\,S \ge 2+\ell(A_{q_2}) = 12$,
which holds **with equality**.  The theorem applies through its first
alternative at 2, with a margin of one.

**A2's hypothesis holds.**  Nikulin 1.14.2 needs $\mathrm{rk}\,T \ge
\ell(A_{T_p})+2$ for odd $p$ — $12\ge 2$ — and a condition at 2 firing only when
$\mathrm{rk}\,T = \ell(A_{T_2})$; since $12\ne 10$ it is vacuous.  So the genus
of $L_-$ has one class and $O(L_-)\to O(q_{L_-})$ is surjective.

This resolves the discrepancy between the two rank conditions.  They differ, and
here it decides: Scattone's $\mathrm{rk}\,L > \ell(G_L)+2$ reads $12>12$ and
**fails**; Nikulin's is satisfied.  **Nikulin's is the one that applies**, and a
node stated with Scattone's phrasing would be unusable for $L_-$.

## Coverage: every labelled statement of Chap. 2

The DAG above is a subgraph of the paper, not the whole of it.  This table is
the complete list of labelled statements in Chap. 2 §§1–3, so that a reader can
see which are carried and which are deliberately not, with the reason.  A blank
disposition would mean the filtering was done silently.

| Item | Kind | Disposition |
| --- | --- | --- |
| 1.1–1.4 | setup | **E6** — the $K3$ lattice, the involution, and the eigenlattices; where $L_-$ comes from |
| 2.1 | Definition | **E2** — almost polarization and its degree; names the surfaces whose period space this is |
| 2.2, 2.3 | setup | **E2** — the $K3$ double cover and its marking |
| 2.4 | Proposition | **E2** — the two elliptic fibrations on the double cover |
| 2.5 | Proposition | **E2** — the same two pencils |
| 2.6 | Remark | **E2** — commentary on 2.4 |
| 2.7, 2.8 | Definitions | **A0** |
| 2.9 | Proposition | **E13** — the period map is well defined; what makes $\Omega_-/\Gamma$ a period space at all |
| 2.10 | Lemma | **A1** |
| 2.11 | Remark | **A1a** — $\Gamma$ is *not* the group one might expect; a caveat on the definition in A1 |
| 2.12 | setup | **E12** — the period point and its image |
| 2.13 | Lemma | **A2** |
| 2.14 | Proposition | **E8**, **E9** — $P$ is injective; rests on Torelli for $K3$ |
| 2.15 | setup | **A6a** — defines the special sets $R_-$ and $S_-$ |
| 2.16 | Lemma | **A4** |
| 2.17 | Corollary | **A5** |
| 2.18 | Corollary | **A6** |
| 2.19 | Lemma | **A7** |
| 2.20 | Proposition | **E2** — characterizes special Enriques surfaces |
| 2.21 | Remark | **A8** — $R_-$ is a single $\Gamma$-orbit, by 2.18 |
| 3.1 | setup | **D1–D7**, **BB1–BB8** — the Satake–Baily–Borel construction |
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

**There is no out-of-scope column.**  An earlier revision carried one, marking
the period map, the $K3$ double cover, Torelli and the almost polarizations as
not needed.  They are needed exactly when the goal mentions Enriques surfaces or
their period space, which it does, so excluding them while keeping the name was
a narrowing of the target disguised as a scope judgment (`FDC-08`).  Every row
above now names the node that carries it.

It ran deeper than those propositions: $L_-$ is not a Gram matrix in the source
but the anti-invariant eigenlattice of the involution on $H^2(X,\mathbb{Z})$ of
the $K3$ cover, tied to it by Horikawa's isometry — node Cl1 — and introducing
$L_-$ by its Gram matrix severs that tie, leaving the development unable to say
what $L_-$ is.

Substrate for that layer, searched at revision `0df444a3`: no complex manifolds,
no compact complex surfaces, no $K3$ surfaces, no Hodge structures, no line
bundles, no period maps, no Torelli.  Stratum **E** below is therefore as absent
as stratum F, and larger.

### Stratum E, from Horikawa and BPV — the surface theory

Read from Horikawa, *On the periods of Enriques surfaces I* (`6ZXI2FJ4`) and
*II* (`RQ2EG4F7`), with Barth–Peters–Van de Ven, *Compact Complex Surfaces*
(`VQUIPQ4Y`) for the general surface theory.  These replace the six subject
rows.

| Node | Statement | Source | Next dependency |
| --- | --- | --- | --- |
| E1 | compact complex surfaces: divisors, line bundles, the canonical bundle, $H^2$ with its intersection form, and the Hodge index theorem | BPV Chaps. I–IV | HS1, HS3 |
| E2 | Enriques surfaces and their $K3$ universal covering $T \to S$, with the covering involution | Horikawa I §§3–6; BPV Chap. VIII | E1, **E14** |
| E3 | Horikawa I Thm 3.1: an Enriques surface $S$ has an elliptic pencil $\lvert D\rvert$, and the associated $g : S\to\mathbb{P}^1$ has exactly two multiple fibres, each of multiplicity 2 | Horikawa I Thm 3.1 | E2 |
| E4 | Horikawa I Thms 4.1, 4.2: an Enriques surface not of special type is birationally a double covering of $\Sigma_0$ with branch locus $\Gamma_1+\Gamma_2+B_0$; one of special type is birationally a double covering of $\Sigma_2$ | Horikawa I Thms 4.1, 4.2 | E2, E3 |
| E5 | Horikawa I Thm 4.3: any two Enriques surfaces are deformations of each other | Horikawa I Thm 4.3 | E4 |
| E6 | **Horikawa I Thm 5.1** (= node Cl1): for $T$ a $K3$ surface which is the universal covering of an Enriques surface $S$, and $\tau : H_2(T,\mathbb{Z})\to H_2(T,\mathbb{Z})$ the involution induced by the covering transformation, **there exists an isomorphism $\varphi : H_2(T,\mathbb{Z})\to\Lambda$ of lattices with $\varphi\circ\tau = \varrho\circ\varphi$** — this is what makes $L_-$ an eigenlattice rather than a Gram matrix | Horikawa I Thm 5.1 | E2, E5, F1.1 |
| E7 | Horikawa I Thms 6.1, 6.2: the universal covering $T$ described explicitly as a pull-back, in the non-special and special cases | Horikawa I Thms 6.1, 6.2 | E4 |
| E8 | Horikawa I Thm 7.1 (Torelli for Enriques surfaces): distinguished Enriques surfaces with proportional periods are isomorphic | Horikawa I Thm 7.1 | E9, E6 |
| E9 | Piatetski-Shapiro–Shafarevich, quoted as Horikawa I Thm 7.2: an isomorphism of $K3$ lattices satisfying (i) and (ii) is induced by an isomorphism of surfaces — **global Torelli for $K3$**, and the node Cl3 names | Horikawa I Thm 7.2, citing [17] | E1 |
| E10 | Horikawa II Thm 3.1 (= node Cl2): the statement about $R_-$ and the divisor $D_V/\Gamma$ — **not transcribed**; Horikawa II is `RQ2EG4F7` | Horikawa II Thm 3.1 | E6, A6a |
| E11 | Kodaira's projectivity criterion (= node Cl5): a surface carrying a line bundle of positive self-intersection is projective | BPV Chap. IV Thm 5.2 | E1 |
| E12 | Hodge structures of weight 2 on $H^2$, and the period point | BPV Chap. I; Horikawa I §7 | E1 |
| E13 | the period map for Enriques surfaces and its domain $\Omega_-$ | Horikawa I §7, Horikawa II | E12, E6 |
| E14 | a **degree-two covering with its deck involution**: a covering map whose fibres have two elements, the nontrivial automorphism over the base, and that it is an involution | decomposed out of E2, whose covering claim had no supplier once `CoveringSpacesProject` was read | Mathlib `IsCoveringMap`, `IsEvenlyCovered` (`Topology/Covering/Basic.lean`), `Topology/Covering/Quotient.lean`, `Topology/Homotopy/Lifting.lean`; deck transformations are **not** in that tree and are the content here |
| E15 | a **Weil divisor** on an integral scheme: the free abelian group on the codimension-one points, the principal divisor of a rational function, and linear equivalence | decomposed out of E1, whose row asks for divisors, line bundles and the canonical bundle with nothing under them | Mathlib `Finsupp` for the free group, `Order.height` (`Order/KrullDimension.lean`) for codimension, `Scheme.functionField` and `Scheme.germToFunctionField_injective` (`AlgebraicGeometry/FunctionField.lean`) for the rational functions.  `rg -i 'WeilDivisor\|Chow\|algebraicCycle'` over the pinned tree returns **nothing**, so this is the deepest greenfield node in the graph and everything in E and Cl sits on it |
| E16 | the **order of vanishing** at a codimension-one point: that the local ring there is a discrete valuation ring, and the resulting valuation on the function field | decomposed out of E15, whose principal-divisor clause needs it and whose row did not state the hypothesis | E15; Mathlib `IsDiscreteValuationRing` with `IsDiscreteValuationRing.addVal` (`RingTheory/DiscreteValuationRing/Basic.lean`), `IsIntegrallyClosed`, `Order.height`.  The DVR property at a height-one prime needs **normality**, which is the hypothesis E15 was missing |

**E6 is the load-bearing node of this stratum**, and note what it actually says:
the isomorphism is onto $\Lambda$ intertwining $\tau$ with a fixed involution
$\varrho$.  So $L_-$ is the $(-1)$-eigenlattice of $\varrho$ on $\Lambda$, and
every statement in strata A and B that begins "let $L_- = U\oplus U(2)\oplus
E_8(-2)$" is downstream of it.

**E9 is not Horikawa's.**  He quotes it as Theorem 7.2, attributing it to
Piatetski-Shapiro and Shafarevich [17], and derives his Enriques Torelli (E8)
from it.  So Cl3, which the graph recorded as "global Torelli, via BPV Chap.
VIII", has its statement here and its proof elsewhere again — the descent
continues into [17].

E1 has no Mathlib substrate at all, and it is the base of this whole stratum.


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

Nodes this table added: **A1a** (2.11), **A6a** (2.15), **A8** (2.21) and
**D0** (3.2.4).  They were named here and had no row of their own until
`check_dag.py` found A6a referenced by Cl2 and E10 with nothing defining it;
all four now have rows in strata A and D.

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

### V13's primitivity, checked on all five diagrams

Vinberg 1983 §1.9 warns that the vector $u(\Sigma_0)$ read off a connected
parabolic component need not be primitive, and gives a sufficient condition for
it to be.  Computed for every maximal parabolic component of all five diagrams
(`sterk_cusp_diagrams.sage`, `primitivity_report`): **the warning fires
constantly.**

Every $\tilde E_8$, $\tilde E_7$ and $\tilde D_8$ component yields
$u(\Sigma_0)$ of **content 2**, not 1.  The components that do give a primitive
vector are the small ones — the $\tilde A_1$ pairs joined by an $\infty$ edge,
and the $\tilde B$/$\tilde C$ components in the diagrams of (3.3.10)–(3.3.12).
For $v = e$ the split is nine non-primitive against three primitive.

This is consistent with Sterk where he shows his work: at (3.3.10) he reads off
$\alpha_9+\alpha_{10} = e'+f'+\bar\alpha_8$, a coefficient-one sum on an
$\tilde A_1$ component — one of the primitive cases.  For the large components
the isotropic vector he wants is $u(\Sigma_0)/2$, and **the division is nowhere
stated**.

Two consequences.  A node stating "the isotropic vector represented by a
parabolic subdiagram" must carry the content, since here it is 2 more often than
1.  And the source of the factor is structural: $U(2)$ and $E_8(-2)$ are
2-scaled, so a radical generator with coefficient-one support inherits a factor
2 — which is also why Vinberg's sufficient condition, requiring a 2-root among
the $e_i$, fails for exactly these components.
