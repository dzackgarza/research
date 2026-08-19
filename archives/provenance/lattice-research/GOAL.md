# Computational Lattice Hurdles: Coble Moduli Project

This document outlines the lattice-theoretic and computational verification tasks required to establish the moduli space of terminal Coble surfaces of K3 type.

## Overall Staged Plan

The numbered Coble and lattice goals below are downstream research goals. They should
not be attacked by agents writing ad hoc matrix, polynomial, or group computations.
The project first needs a semantic mathematical substrate: a constrained DSL, expressed
through Sage-compatible categories and well-typed mathematical objects, in which later
research code reads like mathematics rather than opaque calculation scripts.

Phase transitions are gated. Each stage blocks the next until its vocabulary,
specifications, implementation surface, and mathematical review are adequate for
downstream work. QC is part of transition evidence for committed implementation work,
but it is not the main control loop during churn-heavy spec drafting; specs are settled
through human/LLM planning, audit, review, and rewrite before implementation gates apply.

Stage: category specs and uniform vocabulary.
Create specs extending Sage's categories so that standard constructions become uniform
and semantic. For example, $R^n$ should be treated as a genuine free $R$-module whose
underlying set is $R \times \cdots \times R$, not merely as a raw vector object with
incidental methods. The first pass is abstract: expose enough vocabulary for sets,
modules, Hom spaces, End spaces, Aut spaces, modules with forms, and refinements such
as lattices so future work can construct real mathematical objects, prescribe maps on
generators, and rely on hidden canonical matrix realization, validation, typing, and
invariant checks.

Stage: Sage refinement and gap discovery.
Refine existing Sage constructions into the new category layer wherever possible.
This phase is expected to surface implementation gaps. Those gaps are not excuses for
local ad hoc work; they become spec, backend-research, or implementation cards. The
goal is to discover precisely where Sage's current category philosophy can already be
used, where it needs thin wrappers, and where the repo must own missing categorical
semantics.

Stage: owned categorical implementation layer.
Implement or wrap Sage classes so the project owns objects satisfying its specs
directly, without a permanent refinement dance. The implementation should leverage
Sage, GAP, Singular, Macaulay2, Oscar/Julia, PARI/GP, CARAT, and other mature
open-source systems wherever they already provide exact algorithms, while closing the
semantic gaps needed by the specs. New code should mostly provide categorical
interfaces, coercions, validation, and bridge boundaries, not reimplement mathematical
kernels.

Stage: universal categorical algorithms.
Implement general algorithms at the highest valid categorical level. A basic example
is deterministic enumeration: $\mathbb{Z}$ has the canonical spiral enumeration
$0, 1, -1, 2, -2, \ldots$; finite products of explicitly countable sets should inherit
explicit countability; free modules over explicitly countable rings should inherit
deterministic enumeration; lattices over $\mathbb{Z}$ should then inherit bounded
enumeration of integral vectors in a canonical order. Sage currently lacks a
principled uniform path for this kind of free-module and lattice enumeration, but it is
needed for Vinberg's algorithm and exhaustive experimental searches. The correct
solution belongs in inheritable set/module/category algorithms, not in lattice-local
loops.

Stage: lattice-theoretic implementation.
Once universal boilerplate lives in sets, modules, modules with forms, and categorical
Hom/End/Aut objects, lattice work should focus on genuinely lattice-theoretic content.
This includes literature-backed and source-checked implementations of discriminant
forms, primitive embeddings, orthogonal complements, local invariants, and Nikulin-style
criteria. The desired interface should allow semantic operations such as base-changing
a lattice from $\mathbb{Z}$ to $\mathbb{Z}_p$ and computing standard invariants through
exact linear algebra over the appropriate ring, rather than forcing agents to manipulate
raw matrices and verify matrix equations by hand.

Stage: scheme, variety, curve, surface, and family interfaces.
After the lattice substrate is solid, expose cohesive category interfaces for schemes,
varieties, complex varieties, curves, surfaces, families, divisors, Picard groups, and
relative constructions. The vocabulary must be rich enough to express the Coble
construction semantically. For instance, $\operatorname{Pic}(\mathbb{P}^n)$ should be
known; for a sufficiently controlled blowup $X \to \mathbb{P}^n$, $\operatorname{Pic}(X)$
should be computable with explicit divisor generators; and for a controlled cover
$Y \to X$, such as a cyclic or double cover ramified in a divisor, $\operatorname{Pic}(Y)$
should be expressible through literal pullbacks, pushforwards, ramification data, and
group generators. This phase will likely require substantial wiring to commutative
algebra and algebraic-geometry software rather than bespoke local algorithms.

Stage: confined experimental research.
Only after the semantic vocabulary, categorical implementation layer, lattice theory,
and geometry interfaces are stable should agents proceed to the experimental research
goals below. The point is to confine experimentation inside a tested mathematical
language that recovers known primary-source results and prevents agents from computing
"in their heads" with explicit polynomials, Jacobian matrices, raw Gram matrices, or
untyped group actions. Most of the existing goals begin at this final stage.

## 1. Foundation: Coble Curves and Picard Lattices

### Background
A **Coble surface** $S$ is obtained via the blowup $\pi: S \to \mathbb{P}^2$ at the 10 $A_1$ nodes of an irreducible rational plane sextic $C = \{ F(x,y,z) = 0 \}$. The polynomial $F$ is a homogeneous sextic of the form:
$$F(x,y,z) = \sum_{i+j+k=6} a_{ijk} x^i y^j z^k$$
satisfying the **nodal conditions** $F(p_m) = \frac{\partial F}{\partial x}(p_m) = \frac{\partial F}{\partial y}(p_m) = \frac{\partial F}{\partial z}(p_m) = 0$ for 10 "special" point positions $p_1, \dots, p_{10} \in \mathbb{P}^2$. The moduli space of such sextics is 9-dimensional. Explicit equations can be derived from the **Steiner sextic** or configurations related to index-2 Halphen pencils.

The **K3 cover** $X \xrightarrow{2:1} S$ is the double cover of $\mathbb{P}^2$ branched along $C$, with equation $w^2 = F(x,y,z)$ in the weighted projective space $\mathbb{P}(1,1,1,3)$. The singularities of $X$ consist of ten $A_1$ nodes lying directly above the nodal positions $p_m$.

The **rank-11 lattice data on the Coble side** should be obtained from the geometry, not postulated in advance:
- **Blowup Picard lattice**: $\mathrm{Pic}(S)$ is generated by the pullback of a line class and the ten exceptional divisors $\{e_0, e_1, \dots, e_{10}\}$, where $e_0 = \pi^*L$ and $e_i = E_i$.
- **K3 pullback lattice**: if $f \colon X \to S$ is the K3 cover, then the first lattice to compute on the K3 side is $f^*\mathrm{Pic}(S) \subset H^2(X,\mathbb{Z})$. Because the cover doubles intersection numbers, the expected model is $I_{1,10}(2) \cong \langle 2 \rangle \oplus \langle -2 \rangle^{10}$ with Gram matrix $\mathrm{diag}(2,-2,\dots,-2)$, but this must be verified from the constructed surface.
- **Discriminant data**: the discriminant group and Nikulin invariants of the pullback lattice are computation targets. The expected outcome is a 2-elementary group of order $2^{11}$, plausibly $(\mathbb{Z}/2\mathbb{Z})^{11}$, but this is an output of the computation rather than an input axiom.
- **Orthogonal-complement lattice**: once the pullback lattice is computed inside $\Lambda_{\mathrm{K3}}$, compute its orthogonal complement and verify its signature, discriminant form, and complementarity relations.
- **Ambient lattices**: $T_{\mathrm{En}} \cong (12, 10, 0)_2$, $T_{\mathrm{dP}} \cong (20, 2, 0)_2$, and $\Lambda_{\mathrm{K3}} \cong (22, 0, 0)_1$.

### Technical Gap
The explicit **equations for $C$ and $X$** given a configuration of 10 points, the computation of $\mathrm{Pic}(S)$, the pullback lattice inside $H^2(X,\mathbb{Z})$, and the **primitivity of the lattice embeddings** all lack rigorous derivation in terms of coordinate bases. The discriminant group, Nikulin invariants, and genus cardinality of the resulting lattices must be computed from that geometric pipeline rather than assumed from notation.

### Computational Verification
- **Task 1.1**: Derive an explicit equation $F(x,y,z)=0$ for a rational sextic with 10 nodes and the corresponding K3 surface $w^2 = F(x,y,z)$.
- **Task 1.2**: Compute $\mathrm{Pic}(S)$, compute its pullback lattice in $H^2(X,\mathbb{Z})$, compute the orthogonal-complement lattice in $\Lambda_{\mathrm{K3}}$, and verify the Gram matrices, discriminant groups, $(r, a, \delta)$ invariants, and **genus cardinality** of the resulting lattices.
- **Task 1.3**: Using the lattice data computed in Task 1.2, derive the explicit primitive embedding matrices for the relevant Coble-side lattice and its orthogonal complement along the chain into $T_{\mathrm{En}}$, $T_{\mathrm{dP}}$, and $\Lambda_{\mathrm{K3}}$.

---

## 2. Isotropic Orbit Enumeration (Sterk's Technique)

### Background
The 0-cusp classification relies on the orbits of primitive isotropic vectors $v \in T_{\mathrm{Co}}$ under $O(T)$, $O^*(T)$, and the arithmetic group $\Gamma_{\mathrm{Co}}$, where here $T_{\mathrm{Co}}$ denotes the orthogonal-complement lattice produced in Task 1.2. **Sterk's Technique** (Sterk 1991) determines these orbits by analyzing the orbits of their images (lifts) in the **discriminant group** $A_T = T^*/T$ under $O(q_T)$. For 2-elementary lattices with the required hypotheses checked explicitly, the genus contains a **unique isometry class**, and $O(T) \to O(q_T)$ is surjective (Nikulin 1.5.2).

### Technical Gap
The number of isotropic orbits in $A_{T_{\mathrm{Co}}}$ is not yet computed from the actual lattice produced in Task 1.2. **Nikulin's classification** (Nikulin 1.5.2) implies that for a 2-elementary lattice $(r, a, \delta)$, any primitive isotropic vector $v$ with $\operatorname{div}(v)=d$ is uniquely determined up to $O(T)$ by the image $v/d + T \in A_T$, but those hypotheses must be checked on the computed lattice. One must formally verify the **lifting of isotropic orbits** from $A_T$ to $T_{\mathrm{Co}}$ using Sterk's lifting theorems. One must also verify that $O(T)$ orbits coincide with $\Gamma_{\mathrm{Co}}$ orbits to ensure the BB 0-cusp is unique.

### Computational Verification
- **Task 2.1**: Enumerate isotropic vectors in $A_{T_{\mathrm{Co}}}$ and compute their orbits under $O(q_T)$.
- **Task 2.2**: Lift these orbits to $T_{\mathrm{Co}}$ and verify that exactly one $O^*(T)$-orbit exists for divisibility 2.

---

## 3. Uniqueness of 1-Cusps and $\Gamma_{\mathrm{Co}}$ Stabilizer

### Background
The arithmetic group $\Gamma_{\mathrm{Co}}$ is the **stabilizer of the typed Coble polarization data**, further constrained by the horizontal folding involution $\theta$. Downstairs on a Coble surface $S$, the degree-2 Coble polarization is the Enriques-type class
$$h_{\mathrm{Co}}\in K_S^\perp\subset \mathrm{Pic}(S),\qquad h_{\mathrm{Co}}^2=2.$$
In the non-degenerate case, $h_{\mathrm{Co}}=F_1+F_2$ with $F_i^2=0$ and $F_1\cdot F_2=1$. Its K3 pullback
$$\widetilde h_{\mathrm{Co}}=f^*h_{\mathrm{Co}}\in f^*(K_S^\perp)\subset S_{\mathrm{Co}}$$
has square $4$. This mirrors the Enriques convention: the downstairs degree-2 numerical polarization has square $2$, while the K3-side vector $h=e+f\in U(2)\subset S_{\mathrm{En}}$ has square $4$. The plane-line class $E_0=f^*H$ in the Coble K3 pullback lattice is a different class: $H^2=1$ on the blowup and $E_0^2=2$ on the K3 cover.
In the blowup basis, $K_S=-3H+\sum_iE_i$, so
$D=aH-\sum_i b_iE_i$ lies in $K_S^\perp$ exactly when $\sum_i b_i=3a$.

Accordingly, formulas for $\Gamma_{\mathrm{Co}}$ must specify whether they stabilize the downstairs class $h_{\mathrm{Co}}$, its K3 pullback $\widetilde h_{\mathrm{Co}}$, or the corresponding transported class in the Enriques comparison lattice:
$$\Gamma_{\mathrm{Co}} = \text{Stab}(\text{typed polarization data}) \cap Z(\theta).$$

### Technical Gap
An explicit representation of $\Gamma_{\mathrm{Co}}$ in terms of **matrix generators** is currently a stub. Construction requires the centralizer/stabilizer intersection in the Enriques sector:
$$\Gamma_{\mathrm{Co}} = \text{Stab}_{O(\Lambda)}(\widetilde h_{\mathrm{Co}}\ \text{or its transported Enriques-side class}) \cap Z_{O(\Lambda)}(\theta),$$
with all parent lattices and pullback/transport maps named. One must also verify the **uniqueness of the 1-cusp** by checking the negative-definite quotient $J^\perp/J$ for all orbits of isotropic primitive planes $J \subset T_{Co}$ and confirming isometry with $A_1^{\oplus 7}$.

### Computational Verification
- **Task 3.1**: Compute the stabilizer/centralizer intersection in the Enriques lattice to find a minimal set of generators for $\Gamma_{\mathrm{Co}}$.
- **Task 3.2**: Enumerate all $O(T_{\mathrm{Co}})$-orbits of isotropic planes $J$ and compute $J^\perp/J$.

---

## 4. Combinatorial Search for Coxeter Parabolics

### Background
The reflection group $W(S_{\mathrm{Co}})$ acts on the period domain. The 0-cusp $(9,9,1)_1$ is described by a maximal parabolic subdiagram in the Coxeter diagram $G_{S_{\mathrm{Co}}}$.

### Technical Gap
The 10-node Coxeter diagram $G_{S_{\mathrm{Co}}}$ is highly connected. Confirming that $\widetilde{B}_7(2)$ is the **only** maximal parabolic subdiagram is essential to the "one 0-cusp" claim.

### Computational Verification
- **Task 4.1**: Implement a subdiagram search on the $10 \times 10$ Gram matrix of roots to identify all possible maximal parabolic configurations.

---

## 5. Explicit Involution Matrix and Sublattice Invariants

### Background
The "horizontal folding" $\theta$ must act on $\Lambda_{\mathrm{K3}}$ such that its **invariant and coinvariant sublattices** are correctly identified with the two rank-11 lattices computed in Task 1.2: the pullback lattice coming from $\mathrm{Pic}(S)$ and its orthogonal complement. It compares the polarization generators only after the relevant K3-side pullback/transport data has been fixed: the Enriques-side K3 vector has square $4$, and the Coble-side K3 vector is $\widetilde h_{\mathrm{Co}}=f^*h_{\mathrm{Co}}$ with square $4$.

### Technical Gap
The explicit matrix for $\theta$ on the standard basis of $U^3 \oplus E_8^2$ is missing. One must verify the **isometry classes** of the $\pm 1$ eigenspaces against the lattices computed in Task 1.2, and verify that the relevant embedding into $T_{\mathrm{En}}$ is primitive.

### Computational Verification
- **Task 5.1**: Construct the $22 \times 22$ matrix $\theta$ and compute the signature and invariants of its fixed sublattice to confirm isometry (2-elementary check).

---

## 6. Monodromy Invariants and Stable Models $B(\lambda)$

### Background
Stable limits of Coble surfaces correspond to $S_2$-quotients of nodal K3 surfaces. These models are parameterized by the monodromy invariant $\ell \in \check{\mathcal{H}}$ (surgery sizes) via the construction $B(\lambda)$ (AEGS23).

### Technical Gap
The stability of the slc pair $(Z, \epsilon C)$ for specific surgery vectors $\ell$ must be verified. One must determine the mapping from the typed Coble polarization data, usually the K3-side class $\widetilde h_{\mathrm{Co}}$, to the discretization $\ell$ on the dual complex.

### Computational Verification
- **Task 6.1**: Map the typed Coble polarization data, usually the K3-side class $\widetilde h_{\mathrm{Co}}$, to the surgery vector $\ell$ and verify the slc stability of the resulting stable limit.

## 7. Authoritative References
- **Nikulin (1979)**: *Integer symmetric bilinear forms and some of their geometric applications*. (Uniqueness of embeddings, genus cardinality).
- **Sterk (1991)**: *Compactifications of the moduli space of Enriques surfaces*. (Isotropic orbits in discriminant groups, degree 2 numerical polarization, lifting orbits).
- **Dolgachev & Kondyrev (2013)**: *Moduli of Coble surfaces*. (Geometric lattices $S_{Co}, T_{Co}$).
- **Alexeev, Engel, Garza, Schaffler (2023)**: *Compact moduli of Enriques surfaces*. (Modernized flowerpots, Horikawa models, IAS on discs, nodal K3 covers).

## 8. Formulaic Anchors and Technical Examples

### 8.1. Example Equations
- **Coble Curve Configuration**: A rational sextic $C$ with 10 nodes can be realized as the image of $\mathbb{P}^1$ under a map $(s:t) \mapsto [f_0:f_1:f_2]$ where $f_i$ are polynomials of degree 6.
- **K3 Cover $X$**: For nodal positions $\{p_m\}$, the K3 surface $w^2 = F(x,y,z)$ has $A_1$ singularities at $w=0, [x:y:z]=p_m$.

### 8.2. Lattice Anchors
- **Isotropic Vectors**: In $S_{\mathrm{Co}}$, primitive isotropic lines can be represented by vectors such as $v = e_0 \pm e_i$ (where $e_0^2=2, e_i^2=-2$).
- **Polarization Basis**: The downstairs degree-2 Enriques and Coble polarizations have square $2$. Their K3-side representatives have square $4$: on the Enriques side this is $h=e+f\in U(2)$, and on the Coble side this is $\widetilde h_{\mathrm{Co}}=f^*h_{\mathrm{Co}}$ with $h_{\mathrm{Co}}\in K_S^\perp\subset\mathrm{Pic}(S)$. The Coble plane-line class $e_0=f^*H$ has square $2$ and is not the moduli polarization.
- **Discriminant Forms**:
  - Compute the discriminant form of the pullback lattice $f^*\mathrm{Pic}(S)$ on the K3 cover.
  - Compute the discriminant form of its orthogonal complement in $\Lambda_{\mathrm{K3}}$.
  - Verify the complementarity relation $q_S = -q_T \pmod{2\mathbb{Z}}$ from the computed pair.

### 8.3. Orbits and Stabilizers
- **Sterk Orbit Lift**: For the 2-elementary lattice $T$, the orbits are uniquely determined by the tuple $(\operatorname{div}(v), \bar{v} \in A_T, v^2=0)$. The search reduces to checking $\mathbb{F}_2$-vector space orbits under the orthogonal group of the quadratic form $q_T$.
- **$\Gamma_{\mathrm{Co}}$ Generators**: Computation involves finding the intersection of the group of reflections $W(T)$ with the centralizer $Z(\theta)$ and the stabilizer of the primitive vector $h$.

## Autonomous execution entry point

The repo process is distributed across skills loaded at startup (`AGENTS.md`,
`research-state-machine`, `research-project-workflow`, etc.). A `/goal` prompt
does not need to encode the process — it needs to encode what "done" means and
where to start reading. The process loads progressively from the files the agent
hits as it advances: you can't review without the review kernel, can't promote
without ACs, can't jump the DAG without unmet dependencies blocking you.

Use goalcraft (load `goalcraft` skill) to refine the entry point, then set it
with `/goal`. A compact starting template:

```
Destination: ./.agents/plans/card-progress-report.md shows all cards complete,
needs-human-input, or phase-gated.

Starting point: Read .agents/memories/current-goal-handoff.md for
checkpoint, AGENTS.md for routing rules, then follow the DAG.

Done when: No executable cards remain — every card is complete, decided,
needs-human-input, or blocked by phase gate.

Stop conditions: A card in needs-human-input with no further
agent-executable path. Do not pivot to unrelated features.
```

The goal should be short enough to survive compaction. Everything else — the
6-gate review, the DAG, the handoff rhythm — lives in the skills and card bodies
the agent loads on demand.
