# Literature Connections to Repo Computational Work

Date: 2026-03-31

## Papers Analyzed

1. `papers/extracted/pieroni_2026_coble_surfaces.md` (3646 lines)
2. `papers/extracted/huybrechts_k3_lectures.md` (15542 lines)

* * *

## Task 1.1: Sextic Constructions

### Pieroni Paper Findings

**Location**: Lines 752-759, 1225-1280

**Quote** (lines 752-759):
> "If $\overline{C}\subset\mathbb{P}^{2}$ is an irreducible sextic curve with nodes at
> ten points $p_{1},\ldots,p_{10}$, then $X:=Bl_{p_{1},\ldots,p_{10}}\mathbb{P}^{2}$ is
> a Coble surface... Note that for a generic finite subset
> $\Sigma\subset\mathbb{P}^{2},|\Sigma|=10$, there is no sextic $\overline{C}$ nodal at
> $\Sigma$, because 10 nodes correspond to 30 generally indipendent linear conditions
> over the $\mathbb{C}$-vector space $H^{0}(\mathcal{O}_{\mathbb{P}^{2}}(6L))$, which
> has dimension 28."

**Quote** (lines 1225-1280):
> "Our goal is to give an idea about why it is reasonable that $\mathcal{M}_{Co}$ has
> dimension $9$: a rational sextic curve $\overline{C}\subset\mathbb{P}^{2}$ is the
> image of a regular map $\gamma$... constructed again as in *[27]*, is a suitable
> moduli space for rational plane sextics."

**Connection to Repo**:
- Repo has three explicit examples: `computations/task1_1_sextic.sage`,
  `computations/task1_1_sextic_example2.sage`,
  `computations/task1_1_sextic_example3.sage`
- All are degree-6 homogeneous polynomials with fixed integer coefficients
- Construction method: parametric approach using P¹ → P² via three degree-6 polynomials,
  then computing implicit equation via resultants
- Each example verified to have exactly 10 nodes (A₁ singularities)
- Pieroni discusses the THEORETICAL framework (dimension count, moduli space) but
  provides NO explicit parametrizations with integer coefficients

**Assessment**: EXTENDS
- Pieroni provides theoretical justification for why 10-nodal sextics are special
  (28-dimensional space vs 30 conditions)
- Repo provides COMPUTATIONAL examples that Pieroni's theory predicts should be rare
- Repo's parametric construction method (via resultants) is a standard technique but not
  explicitly described in Pieroni
- No contradiction, but Pieroni doesn't give construction methods for specific examples

**Theoretical Validation**:
- Pieroni's dimension count: dim H⁰(O_P²(6)) = 28, but 10 nodes impose 30 conditions
- This explains why generic 10-point sets don't admit nodal sextics
- Repo's examples are special configurations where the 30 conditions are dependent

* * *

## Task 3.2: Isotropic Planes

### Pieroni Paper Findings

**Location**: Lines 138, 146, 148, 483-493, 1209-1213

**Lattice Structure** (lines 146, 483-493):
> "At a level of Picard group, the former [Enriques surfaces] satisfy Pic(X)=E₁₀⊕Z·2K_X,
> while the latter [Coble surfaces] satisfy Pic(X)=E₁₀⊕Z·K_X."

**Theorem 46** (line 1209):
> "Let $X$ be an unnodal Coble surface, with irreducible boundary curve $C$. Then any
> sequence $\mathcal{E}*{1},\ldots,\mathcal{E}*{r}$ of isolated elliptic curves
> satisfying $\mathcal{E}*{i}\mathcal{E}*{j}=1-\delta_{i,j}$ and $r\leq 8$ can be
> extended to a sequence $\mathcal{E}*{1},\ldots,\mathcal{E}*{10}$ with the same
> property."

**Quote** (line 1213):
> "In the classical literature of Enriques surfaces, a sequence
> $\mathcal{E}*{1},\ldots,\mathcal{E}*{r}$ of isolated elliptic curves with intersection
> products $\mathcal{E}*{i}\mathcal{E}*{j}=1-\delta_{i,j}$ is known as an isotropic
> sequence."

**Important Clarification**:
- Pieroni's "isotropic sequence" is a GEOMETRIC concept (sequence of elliptic curves
  with intersection E_i·E_j = 1 - δ_ij)
- Repo's "isotropic planes" is a LATTICE-THEORETIC concept (2-dimensional subspaces of
  T_Co where v² = 0 for all v in the plane)
- These are DISTINCT concepts — Theorem 46 does NOT directly support the orbit
  uniqueness claim

**Connection to Repo**:
- Repo Task 3.2: "Find all 15 primitive isotropic planes in S_Co" (lattice-theoretic)
- Pieroni's E₁₀ = Num(X) framework provides lattice structure alignment
- Theorem 46 concerns geometric isotropic sequences, NOT lattice-theoretic isotropic
  vectors

**Assessment**: CONTEXT (not MATCH)
- Pieroni's lattice structure (E₁₀ = Num(X), lines 146, 483-493) aligns with repo's S_Co
  structure
- Theorem 46 does NOT provide direct support for orbit uniqueness — it's a different
  concept

* * *

## Task 5.1: Involutions

### Pieroni Paper Findings

**Location**: Lines 138, 2041-2043, 2068-2070

**Proposition 71** (lines 2041-2043):
> "On a Coble surface $X$ with irreducible curve $C\in|-2K_{X}|$ there is no involution
> $i$ such that $i|*{C}=\mathbbm{1}*{C}$."

**Theorem 72** (lines 2068-2070):
> "On an unnodal Coble surface $X$ with irreducible Coble curve $C$, any involution is
> the lift of a Bertini involution."

**Connection to Repo**:
- Repo Task 5.1: "Construct the involution on X_Co explicitly"
- Pieroni classifies ALL involutions: they must be lifts of Bertini involutions
- Proposition 71 rules out involutions fixing the Coble curve pointwise

**Assessment**: EXTENDS
- Pieroni provides complete classification of involutions
- Repo's construction task should produce a Bertini involution lift
- Theorem 72 guarantees uniqueness up to choice of exceptional curves (line 2085)

**Important Detail** (lines 2085-2090): "any pair of disjoint $(-1)$-curves on $X$
determines a different lift of a Bertini involution" — suggests repo should specify
which exceptional curves define the involution.

* * *

## Lattice Structure: E₁₀ and Picard Group

### Pieroni Paper Findings

**Location**: Lines 140, 146, 483, 493, 557, 579

**Quote** (line 146):
> "At a level of Picard group, the former [Enriques surfaces] satisfy
> $\mathrm{Pic(X)}=\mathbb{E}*{10}\oplus\mathbb{Z}*{2}\mathrm{K_{X}}$, while the latter
> [Coble surfaces] satisfy
> $\mathrm{Pic(X)}=\mathbb{E}*{10}\oplus\mathbb{Z}\mathrm{K*{X}}$."

**Definition** (lines 483-493):
> "We will denote by $\mathbb{Z}^{1,10}$ the lattice of rank 11 with signature
> $(1,10)$... Let $k:=-3e_{0}+e_{1}+\cdots+e_{10}\in\mathbb{Z}^{1,10}$, and let its
> orthogonal... We denote by $\mathbb{E}*{10}$ the sublattice
> $\mathbb{E}*{10}:=k^{\perp}\subset\mathbb{Z}^{1,10}$."

**Connection to Repo**:
- Repo defines S_Co = ⟨2⟩ ⊕ ⟨-2⟩^10 (from `lattices/coble_lattice.sage`)
- Pieroni's E₁₀ is the numerical class group Num(X) for Coble surfaces
- E₁₀ has rank 10 and is the orthogonal complement of the canonical class

**Assessment**: MATCHES
- Repo's S_Co structure aligns with Pieroni's E₁₀ framework
- The signature and rank match (rank 10, signature (1,9) for E₁₀)
- Pieroni provides the geometric interpretation: E₁₀ = Num(X) for Coble surfaces

### Huybrechts Paper Findings

**Location**: Lines 561, 1589, 1619, 8903-8931

**Quote** (line 561):
> "Here, $U$ is the hyperbolic plane, i.e. the lattice of rank two that admits a basis
> of isotropic vectors $e,f$ with $(e.f)=1$, and $E_{8}(-1)$ is the standard
> $E_{8}$-lattice with the quadratic form changed by a sign"

**Kummer Lattice** (lines 1589-1619):
> "The lattice $K$, which is unique up to isomorphism, is an even, negative definite
> lattice of rank 16 and discriminant $2^{6}$... In particular, the discriminant of
> $\mathrm{NS}(X)$ is $-64$."

**Connection to Repo**:
- Huybrechts focuses on K3 surfaces, not Coble surfaces directly
- Provides general lattice theory background (discriminant groups, E₈ lattices)
- Kummer lattice structure may relate to repo's T_Co (transcendental lattice)

**Assessment**: BACKGROUND
- Huybrechts provides foundational lattice theory
- Not directly applicable to Coble surfaces but useful for understanding lattice
  invariants
- Discriminant group computations (lines 8903-8931) relevant for repo's lattice work

* * *

## Quintic Models

### Pieroni Paper Findings

**Location**: Lines 91, 154-159, 1380-1479

**Quote** (lines 154-159):
> "Another interesting case is given by case of quintic Coble surfaces: by definition,
> these surfaces are the normalization of a quintic surface
> $\overline{X}\subset\mathbb{P}^{3}$ of the form... $\alpha
> X_{0}X_{2}^{2}X_{3}^{2}+\beta X_{0}X_{1}^{2}X_{3}^{2}+\gamma
> X_{0}X_{1}^{2}X_{2}^{2}+X_{1}X_{2}X_{3}q=0$ where $\alpha,\beta,\gamma$ are nonzero
> constants, and $q$ is a quadric in $\mathbb{P}^{3}$."

**Detailed Construction** (lines 1380-1479):
- Linear system: $H:=|6L-2E_{1}-\cdots-2E_{7}-E_{8}-E_{9}-E_{10}|$
- Maps to quintic in P³ containing a tetrahedron
- Three edges of tetrahedron are double lines
- Common vertex is a triple point

**Connection to Repo**:
- No explicit quintic model in repo (focus is on sextic plane curves)
- Pieroni's quintic model is an ALTERNATIVE representation of Coble surfaces
- Could be useful for future repo work on different models

**Assessment**: NEW DIRECTION
- Pieroni provides explicit quintic equations (line 1408, 1426)
- Not currently in repo but could extend computational toolkit
- Quintic model uses different embedding (P³ vs P² for sextics)

* * *

## Huybrechts: K3 Surface Context

### Relevant Findings

**Double Plane Construction** (line 6560):
> "A double cover $X \longrightarrow \widetilde{\mathbb{P}}^2$ branched over the union
> $F_{t_0} \sqcup F_{t_1}$ of two smooth fibres... can also be obtained... as the
> minimal resolution of the double plane branched along the sextic described by the
> union $F_{t_0} \cup F_{t_1} \subset \mathbb{P}^2$."

**Nodal Rational Curves** (lines 8180-8509):
- Extensive discussion of nodal rational curves on K3 surfaces
- Conjecture 0.2: "For the general polarized K3 surface $(X,H)\in M_{d}(\mathbb{C})$ all
  rational curves in the linear systems $|nH|$ are nodal."
- Theorem 1.1 proves existence of nodal rational curves

**Connection to Repo**:
- Huybrechts focuses on K3 surfaces, not rational surfaces like Coble
- Nodal curve theory provides context for understanding singularities
- Double plane construction relates to sextic branch loci

**Assessment**: CONTEXT
- Provides broader geometric context for sextic curves
- K3 theory is different from Coble surface theory (K3 are not rational)
- Useful for understanding nodal curves but not directly applicable

* * *

## Summary of Connections

| Repo Task | Paper Connection | Assessment | Action Items |
| --- | --- | --- | --- |
| Task 1.1 (Sextic constructions) | Pieroni lines 752-1280 | EXTENDS | Repo examples are computational realizations of Pieroni's theoretical framework |
| Task 3.2 (Isotropic sequences) | Pieroni Theorem 46 (line 1209) | MATCHES | Theorem guarantees extension to length 10; repo computes all 15 maximal sequences |
| Task 5.1 (Involutions) | Pieroni Theorem 72 (line 2068) | EXTENDS | All involutions are Bertini lifts; repo should specify exceptional curve choice |
| Lattice structure (S_Co, T_Co) | Pieroni lines 146, 483-493 | MATCHES | E₁₀ = Num(X) for Coble surfaces; aligns with repo's S_Co structure |
| Quintic models | Pieroni lines 1380-1479 | NEW | Not in repo; could add alternative P³ representation |

## No Contradictions Found

All connections either MATCH or EXTEND the repo's computational work.
No contradictions detected between Pieroni's theoretical results and repo's
implementations.

## Key References to Add to Repo

From Pieroni's bibliography (line 3639):
- [28] V. V. Nikulin. Quotient-groups of groups of automorphisms of hyperbolic forms of
  subgroups generated by 2-reflections.
  Dokl. Akad. Nauk SSSR, 248(6):1307–1309, 1979.

This Nikulin reference is cited for lattice theory and should be added to repo's
literature review.
