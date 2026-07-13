---
title: "YZZ25 Report: Relevance to Coble Moduli Project"
paper: "Yu–Zheng–Zhong, Moduli spaces of sextic curves with simple singularities and their compactifications (arXiv:2505.16727)"
date: 2026-05-17
source: knowledge/papers/YZZ25.md
---

# YZZ25 — Detailed Relevance Report

## Overview

YZZ25 studies moduli spaces $\mathcal{M}_T$ of sextic curves with prescribed simple (ADE) singularity type $T$, and identifies their GIT compactifications with Looijenga compactifications of arithmetic quotients of type IV domains.
The paper applies to **all** ADE singular types $T$, including the case $T = 10A_1$ (irreducible rational sextic with 10 nodes), which is the Coble case.

## The Coble Case: $T = 10A_1$

### Setup (§2, YZZ25.md:247–399)

For $T = 10A_1$:
- $Z$ is an irreducible sextic with 10 nodes $p_1, \ldots, p_{10}$
- $\widehat{X}$ is the double cover of $\mathbb{P}^2$ branched along $Z$, with 10 $A_1$ singularities
- $X$ is the minimal resolution — a K3 surface
- $S = X/\iota$ is a Coble surface (the quotient by the covering involution)
- $L = A_1^{\oplus 10}$, with base $\Delta = \{e_1, \ldots, e_{10}\}$

### Picard Lattice Identification

**Corollary 35** (YZZ25.md:1333–1335): When only $A_1$ singularities appear, $\iota$ acts as the identity on $L$ (since $-w_0(A_1) = \mathrm{Id}$), and $T(2) \cong L$.

**Proposition 40** (YZZ25.md:1516–1540): For an irreducible sextic ($l' = 1$), the primitive hull $P = \langle H \rangle \oplus L$.
No extra saturation is needed.

So for $T = 10A_1$: $$P = \langle H \rangle \oplus A_1^{\oplus 10}, \quad H^2 = 2$$

This has signature $(1, 10)$ and rank 11.

### Transcendental Lattice = YZZ25's $Q$

The orthogonal complement $Q = P^\perp$ in $\Lambda_{K3}$ has signature $(2, 9)$ and rank 11.

**This is exactly the lattice $T_{\mathrm{Co}}$ from the Coble paper.** The identification is: $$Q_{10A_1} = P^\perp = T_{\mathrm{Co}} \cong \langle 2 \rangle \oplus E_{10}(2)$$

(The discriminant groups must match: $A_P \cong A_Q$, both $(\mathbb{Z}/2)^{11}$.)

### Period Domain and Arithmetic Group

**Definition 10** (YZZ25.md:481–485): The period domain $\mathbb{D}_T = \mathbb{D}(Q)$ is a 9-dimensional type IV domain.

**Proposition 11** (YZZ25.md:506–517): $\Gamma_T$ contains all elements of $\mathrm{O}(Q)$ acting trivially on $A_Q$.
It is an arithmetic group of finite index in $\mathrm{O}(Q)$.

For $T = 10A_1$, by the pattern at YZZ25.md:1973–1977 (shown for $T_0 = 5A_1$): $$\Gamma_{10A_1} = \{ g \in \mathrm{O}(Q) \mid g \text{ acts on } A_Q \text{ through the } \mathfrak{S}_{10}\text{-action on } A_P \}$$

where $\mathfrak{S}*{10}$ permutes the 10 roots $e_1, \ldots, e*{10}$.

**Lemma 25** (YZZ25.md:1030–1060): $\Gamma_T$ equals the normalizer of $W(L)$ restricted to $P^\perp$.
Equivalently, $\Gamma_T$ is the normalizer of the Weyl group $W(A_1^{\oplus 10}) = \{\pm 1\}^{10}$ inside $\Gamma_1$ (the degree-2 K3 monodromy group).

**This gives an explicit characterization of $\Gamma_{\mathrm{Co}}$ in terms of the larger degree-2 K3 group.**

* * *

## Main Theorems Applied to $T = 10A_1$

### Theorem 12 — Global Torelli (YZZ25.md:560–603)

The occult period map $\mathscr{P}_T \colon \mathcal{M}_T \to \Gamma_T \backslash \mathbb{D}_T$ is **injective** for all $T$, including $T = 10A_1$.

**Proof technique** (YZZ25.md:564–603): Construct an ample class $\alpha_F = \beta_F + cH_F$ lying in $\langle H_F \rangle \oplus L_F$ (using the Weyl chamber of $L_F$), then apply global Torelli for K3 surfaces.

{>>This is a clean proof of injectivity for the Coble period map that could be cited directly.<<}

### Theorem 13 — Image of Period Map (YZZ25.md:620–623)

$$\mathcal{M}*{10A_1} \cong \Gamma*{10A_1} \backslash (\mathbb{D}*{10A_1} - \mathcal{H}*{10A_1})$$

where $\mathcal{H}_{10A_1}$ is the union of hyperplanes $r^\perp$ for roots $r \perp H$, $r \notin L$.

{>>This identifies the image of the Coble period map precisely as the complement of a hyperplane arrangement.<<}

### Theorem 31 — GIT = Looijenga (YZZ25.md:1155–1183)

$$\widehat{\mathcal{M}}*{10A_1} \cong \overline{\Gamma*{10A_1} \backslash \mathbb{D}*{10A_1}}^{\mathcal{H}^**{10A_1}}$$

The GIT compactification of the Coble moduli is isomorphic to the **Looijenga compactification** with respect to the hyperplane arrangement $\mathcal{H}^*_{10A_1}$ (roots of divisibility 2).

The proof uses the commutative diagram (YZZ25.md:1162): $$\begin{tikzcd} \widehat{\mathcal{M}}*{10A_1} \ar[r, "\cong"] \ar[d, "j_T"] & \overline{\Gamma*{10A_1} \backslash \mathbb{D}*{10A_1}}^{\mathcal{H}^**{10A_1}} \ar[d, "\pi_T"] \\
\overline{\mathcal{M}} \ar[r, "\cong"] & \overline{\Gamma_1 \backslash \mathbb{D}*1}^{\mathcal{H}*\infty} \end{tikzcd}$$

Both vertical maps are **normalizations** onto their images.
The bottom row is Shah–Looijenga for smooth sextics.

### Proposition 50 — Orbifold Structure Preserved (YZZ25.md:1825–1826)

For **all nodal singular types** (including $10A_1$), the period map preserves orbifold structures: $$\mathcal{M}*{10A_1} \cong P\Gamma*{10A_1} \backslash (\mathbb{D}*{10A_1} - \mathcal{H}*{10A_1}) \quad \text{as orbifolds}$$

**Proof** (Lemma 51, YZZ25.md:1831–1838): For irreducible nodal types, $\mathrm{O}(P, H, \Delta) \cong \mathfrak{S}_m$ acts faithfully on $A_P \cong \mathbb{Z}/2 \times (\mathbb{Z}/2)^m$ by permuting the $m$ generators.
Criterion of Proposition 49 (YZZ25.md:1777–1816) is satisfied.

{>>The orbifold preservation means the period map is not just a bijection but preserves all automorphism/stabilizer information.
This is the strongest form of the period map identification.<<}

* * *

## Critical Open Question: What is $\mathcal{H}^*_{10A_1}$?

The Looijenga compactification depends on the hyperplane arrangement $\mathcal{H}^**T = \mathcal{H}*\infty \cap \mathbb{D}_T$.

**Proposition 27** (YZZ25.md:1075): $\mathcal{H}^*_T \subset \mathcal{H}_T$.

**Lemma 28** (YZZ25.md:1078–1095): Roots in $L$ have divisibility 1 in $H^\perp$, so they do NOT contribute to $\mathcal{H}^*_T$.

Two cases:
- If $\mathcal{H}^*_{10A_1} = \emptyset$: GIT = Baily–Borel compactification (as happens for $T_0 = 5A_1$, see YZZ25.md:1979–1988)
- If $\mathcal{H}^*_{10A_1} \neq \emptyset$: GIT is a **proper** Looijenga compactification, intermediate between Baily–Borel and toroidal

{>>Determining whether $\mathcal{H}^*_{10A_1}$ is empty or not is a concrete computational question that would immediately tell us the relationship between GIT and Baily–Borel for Coble moduli.
If non-empty, the Looijenga compactification is a specific blowdown of the toroidal compactification, giving a concrete comparison target for KSBA.<<}

**To compute this**: Check whether there exist $(-2)$-vectors $r \in Q = T_{\mathrm{Co}}$ with divisibility 2 in $\Lambda_1 = H^\perp \cong A_1 \oplus U^2 \oplus E_8^2$.
This is equivalent to: does $T_{\mathrm{Co}}$ contain $(-2)$-vectors whose image in $A_{\Lambda_1} \cong \mathbb{Z}/2$ is nontrivial?

* * *

## Advancing the Coble Paper

### Directly Citable Results

- **Global Torelli for Coble period map**: Theorem 12 (YZZ25.md:560) gives injectivity of $\mathscr{P}_{10A_1}$.
- **Image characterization**: Theorem 13 (YZZ25.md:620) gives $\mathrm{Im}(\mathscr{P}*{10A_1}) = \Gamma*{10A_1} \backslash (\mathbb{D}*{10A_1} - \mathcal{H}*{10A_1})$.
- **GIT = Looijenga**: Theorem 31 (YZZ25.md:1155) gives a concrete compactification isomorphism.
- **Orbifold preservation**: Proposition 50 (YZZ25.md:1825) for the Coble (nodal) case.
- **Arithmetic group**: Lemma 25 (YZZ25.md:1030) characterizes $\Gamma_{10A_1}$ as the normalizer of $W(A_1^{10})$ in $\Gamma_1$.
- **Lattice characterization**: $P = \langle H \rangle \oplus A_1^{10}$, $Q = P^\perp = T_{\mathrm{Co}}$ (Corollary 18, YZZ25.md:814; Proposition 40, YZZ25.md:1516).
- **Involution on root lattice**: Proposition 33 (YZZ25.md:1293): $\iota = -w_0(L)$ on $L$.
  For $A_1$, $-w_0 = \mathrm{Id}$.

### Results That Advance Open Problems

**Blocker #5 (IAS Construction Gaps)**: The GIT = Looijenga identification provides a **concrete compactification** of $\mathcal{M}*{10A_1}$.
The Looijenga compactification is semitoroidal for a specific admissible semifan determined by $\mathcal{H}^**{10A_1}$.
This gives:
- An explicit comparison target for the KSBA compactification
- A concrete relationship to the Baily–Borel compactification (the Looijenga compactification maps to BB via a contraction)

**Blocker #1 (Root Orbit Uniqueness)**: The paper's Lemma 25 (YZZ25.md:1030) shows that $\Gamma_T$ is the normalizer of $W(L)$ in $\Gamma_1$.
For $L = A_1^{10}$, $W(L) = \{\pm 1\}^{10}$, and the normalizer includes both $W(L)$ and $\mathfrak{S}_{10}$ (permuting the 10 copies).
This characterization of the arithmetic group is relevant to root orbit analysis.

**Blocker #3 (Trace Fan Identity)**: The commutative diagram (Theorem 31) gives the relationship between the Coble-level Looijenga compactification and the smooth-sextic Looijenga compactification (= Shah's GIT). The map $\pi_T$ from the Coble compactification to the Shah compactification is a normalization of its image.
This is relevant to understanding the trace of the Coble divisor in the Enriques compactification.

### Connection to Polarized Case ($F_{\mathrm{Co},2}$)

YZZ25's framework applies to the **unpolarized** Coble moduli (period map via the double cover K3). The polarized case $F_{\mathrm{Co},2}$ involves an additional polarization class.
However:
- The arithmetic group $\Gamma_{10A_1}$ described here constrains the possible arithmetic groups for the polarized case
- The lattice $P = \langle H \rangle \oplus A_1^{10}$ is the Picard lattice of the generic K3 cover, which is the starting point for the polarized embedding

* * *

## Literature Not Yet in the Coble Paper

### Core references from YZZ25 that may be missing

- **Urabe** (classification of root lattices arising from sextic singular types): foundational for the classification of all possible $T$
- **Yang** (extending Urabe's classification): complete enumeration of singular types up to rank 19
- **Degtyarev** (equisingularity, Theorem 3.4.1): alternative proof of surjectivity of the period map; also Zariski pairs
- **Shah** (GIT stability of sextic curves): classification of stable/semistable sextic curves, foundational for the GIT side
- **Looijenga** (compactification theory): the original construction of Looijenga compactifications and their functoriality (Theorem A.13 cited at YZZ25.md:211, 1106)
- **Kudla–Rapoport**: origin of the term "occult period map"
- **Yu–Zheng** (earlier paper by first two authors): nodal sextic curves specifically, including the $10A_1$ case
- **Laza**: the $T_0 = 5A_1$ case (quintic + line), related to $N_{16}$ singularity

### The earlier Yu–Zheng paper is likely the most directly relevant missing reference

YZZ25 cites their earlier paper (referenced as "?" due to extraction issues) which specifically studied **nodal** sextic curves and proved the GIT = Looijenga identification for those cases.
The present paper generalizes to arbitrary ADE types.

* * *

## Specific Interesting Tie-ins

### Remark 9 (YZZ25.md:452–458) — Elliptic Fibrations

Every K3 surface $X_F$ associated to a nontrivial singular type admits natural elliptic fibrations via pencils of lines through singularities.
For $T = 10A_1$, there are **10 such fibrations** (one per node).
These may connect to the Halphen surface structure discussed in the Coble paper.

### The Occult Period Map vs. the Usual Period Map

The "occult" period map $\mathscr{P}*T$ goes from the sextic moduli $\mathcal{M}*T$ to $\Gamma_T \backslash \mathbb{D}*T$, while the "usual" period map goes from K3 moduli to $\Gamma_1 \backslash \mathbb{D}*1$.
The Coble paper constructs $F*{\mathrm{Co}}$ as a divisor in $F*{\mathrm{En}}$ via the $(-2)$-hyperplane $\mathcal{H}*{-2}$.
YZZ25 constructs it directly as a moduli space of singular sextics.
The identification should be: $$F*{\mathrm{Co}} = \mathcal{M}*{10A_1} \cong \Gamma*{10A_1} \backslash (\mathbb{D}*{10A_1} - \mathcal{H}*{10A_1})$$

This gives a **third construction** of $F_{\mathrm{Co}}$ (alongside the period domain quotient and the GIT quotient), and importantly, the GIT = Looijenga identification gives a compactification not available from the other two.

### Divisibility Dichotomy (YZZ25.md:903–907)

In $\Lambda_1 = H^\perp$, roots split into exactly two $\Gamma_1$-orbits: divisibility 1 (defining $\mathcal{H}*\Delta$) and divisibility 2 (defining $\mathcal{H}*\infty$). The divisibility-1 roots correspond to ADE singularities appearing in the sextic; the divisibility-2 roots correspond to the boundary of the GIT compactification.
This dichotomy is the same one appearing in the Coble paper's analysis of $(-2)$-vectors in $T_{\mathrm{Co}}$.

### Footnote on Proposition 3.7 (YZZ25.md:1982–1983)

The footnote corrects a small typo in an earlier paper: "$\Sigma_T$" should be "$\overline{\Sigma}_T$" (the closure in the GIT compactification).
The corrected criterion holds for **all ADE singular types**. This is relevant for determining whether $\mathcal{H}^*_T$ is empty.

* * *

## Clarification: GIT vs KSBA vs Coxeter — Three Different Semifans

The identification GIT = Looijenga does NOT directly help study the KSBA compactification.
Both are semitoroidal compactifications, but for **different semifans**. The relevant structure is a **poset of admissible semifans** (ordered by refinement), within which several named semifans sit:

```
toroidal (finest, all walls)
        ↓                  ↓
   Coxeter fan        GIT/Looijenga semifan
   (reflection          (determined by H*_T)
    group fund.              |
    domain + tiling)         |
        |                    |
        ↓                    |
   KSBA semifan              |
   (determined by            |
    stable pair              |
    degenerations;           |
    typically a wall         |
    removal from Coxeter)    |
        \                   /
         \                 /
          ↓               ↓
      Baily–Borel (coarsest)
```

The KSBA and GIT semifans are **independently determined** — the KSBA by degeneration theory of stable pairs, the GIT by $\mathcal{H}^*_T$.
Their relative position in the poset (does one refine the other?
are they incomparable?)
is an open question.
The typical setup in the literature is that the KSBA semifan is a specific coarsening of the Coxeter semifan (removing walls).
The GIT semifan's position relative to either the Coxeter or KSBA fan is unknown.
The interesting questions are:

- **What semifan does GIT correspond to?** Is it associated to a reflection group?
  Which walls are present/removed?
- **What is the relative position** of the GIT semifan and the KSBA semifan?
  Is one a refinement of the other?
  Are they incomparable?
- **How does either fiber over Baily–Borel?** Which boundary divisors get contracted to which cusps?

* * *

## What the Paper Does and Does Not Address

### What YZZ25 establishes

- **Abstract isomorphism** $\widehat{\mathcal{M}}_T \cong \overline{\Gamma_T \backslash \mathbb{D}_T}^{\mathcal{H}^*_T}$ for all ADE types $T$
- The map $\pi_T$ to the Shah compactification is a normalization
- The functorial property (Looijenga, Theorem A.13) that allows extending from the open part

### What YZZ25 does NOT compute (for any specific $T$)

- The actual semifan (fan structure at each cusp) corresponding to $\mathcal{H}^*_T$
- The boundary strata correspondence (GIT degenerations → cusps)
- Which specific GIT-semistable curves lie over which boundary components
- The relationship between the Looijenga fan and the Coxeter/KSBA fans
- Whether the GIT semifan is associated to a reflection group

These are **open questions** that the paper's framework makes precise but does not resolve.

* * *

## Deeper Questions Raised by the Paper

### Q1: What semifan does the Looijenga compactification correspond to?

A Looijenga compactification $\overline{\Gamma \backslash \mathbb{D}}^{\mathcal{H}}$ is obtained by:
1. Start with BB, which has cusps $F_0$ (0-cusps) and $F_1$ (1-cusps)
2. At each 0-cusp, the toroidal compactification is determined by a fan in the rational closure of the cone $C(F_0)$
3. The Looijenga compactification corresponds to a **specific coarsening** of this fan, determined by which hyperplanes from $\mathcal{H}$ intersect the boundary component

For $T = 10A_1$ (Coble):
- $\mathcal{H}^**{10A_1}$ consists of div-2 roots in $Q = T*{\mathrm{Co}}$ (if any exist)
- The fan at each cusp is the quotient of the hyperplane arrangement induced by $\mathcal{H}^*_{10A_1}$ restricted to the boundary of the tube domain
- **Is this fan a Coxeter fan?** It would be if $\mathcal{H}^*_{10A_1}$ is the full root system of some reflection group acting on the boundary lattice.
  Given that these are $(-2)$-vectors, this is plausible — they may generate a reflection group whose Coxeter fan IS the GIT semifan.

### Q2: How does GIT map to Baily–Borel?

The map $\overline{\Gamma_T \backslash \mathbb{D}_T}^{\mathcal{H}^*_T} \to \overline{\Gamma_T \backslash \mathbb{D}_T}^{\mathrm{bb}}$ contracts boundary divisors.

**If $\mathcal{H}^*_{10A_1} = \emptyset$**: GIT = BB. There are no boundary divisors to contract.
The GIT boundary consists only of the 0-cusp point and the 1-cusp curve.
This would mean GIT-semistable degenerations of 10-nodal sextics are already classified by the two cusps.

**If $\mathcal{H}^*_{10A_1} \neq \emptyset$**: The Looijenga compactification has boundary divisors (one for each $\Gamma_T$-orbit in $\mathcal{H}^*_T$). These get contracted to cusps.
The fibers of the contraction over each cusp tell us which GIT boundary strata lie over that cusp.

The concrete question: **Which sextic degenerations get sent to the $(9,9,1)_1$ zero-cusp vs. the $(7,7,1)_0$ one-cusp?**

### Q3: GIT boundary strata as explicit curve degenerations

For $T = 10A_1$, the GIT boundary $\widehat{\mathcal{M}}*{10A_1} \setminus \mathcal{M}*{10A_1}$ consists of limits of 10-nodal irreducible sextics in the closure $\overline{\mathcal{V}}_{10A_1}$.
These include:

- **Reducible limits**: e.g., an irreducible 10-nodal sextic degenerating into two cubics (each smooth or nodal, meeting at 9 points → producing $9 A_1$ from intersections + existing nodes)
- **Higher-singularity limits**: nodes coalescing to $A_2$, $A_3$, etc.
- **Double cubic**: $2C_3$ (a cubic counted with multiplicity 2) — this is a notable GIT-semistable orbit in Shah's classification

The map $j_T: \widehat{\mathcal{M}}_{10A_1} \to \overline{\mathcal{M}}$ sends these limits into Shah's classification.
The specific Shah orbit (e.g., "double cubic") determines which Looijenga boundary stratum (and hence which cusp) the degeneration maps to.

**Why should a lattice-theoretic cusp correspond to a specific geometric degeneration?** The period map identifies the sextic moduli with a locally symmetric variety.
At the boundary:
- A 0-cusp corresponds to a maximal isotropic subspace — geometrically, a Type III degeneration of the K3 surface (semistable reduction gives a surface with du Val singularities)
- A 1-cusp corresponds to a rank-1 isotropic subspace — geometrically, a Type II degeneration (elliptic fibration structure)

The double cubic $2C_3$ gives a K3 surface that is a double cover of $\mathbb{P}^2$ branched along $2C_3$ — this has a non-isolated singularity along $C_3$, which after resolution should give a Type III degeneration.
The lattice data (discriminant, signature of the boundary lattice) should match the cusp data.

### Q4: Enumerating all configurations $T$ — Severi varieties and their compactifications

**Urabe–Yang classification** (Remark 2, YZZ25.md:152–157): All root lattices $R$ arising from singular types of sextics have been classified.
The maximal rank is 19. The number of types:
- rank 19: 519 types
- rank 18: 987 types
- rank 17: 975 types
- rank 16: 782 types

**Expected dimension formula** (YZZ25.md:281–282): $$\dim \mathbb{P}\mathcal{V}_T = \binom{8}{2} - 1 - \mathrm{rank}(R) = 27 - \mathrm{rank}(R)$$ $$\dim \mathcal{M}_T = 19 - \mathrm{rank}(R)$$

For each $T$, YZZ25 gives:
- An open embedding $\mathcal{M}_T \hookrightarrow \Gamma_T \backslash \mathbb{D}_T$ (this IS a compactification of the Severi variety mod PGL₃)
- A GIT compactification $\widehat{\mathcal{M}}_T$ identified with a Looijenga compactification

**So yes**: YZZ25 provides BB-type compactifications of ALL Severi varieties (for sextics with simple singularities), and GIT = Looijenga for all of them.

**But**: the paper does NOT compute the boundary strata correspondence for any specific $T$.
It doesn't tell us what the Looijenga boundary looks like geometrically.

### Q5: How does $\pi_T$ behave at the boundary?

The map $\pi_T: \overline{\Gamma_T \backslash \mathbb{D}_T}^{\mathcal{H}^*_T} \to \overline{\Gamma_1 \backslash \mathbb{D}*1}^{\mathcal{H}*\infty}$ extends the inclusion $\mathbb{D}_T \hookrightarrow \mathbb{D}_1$.
At the boundary:

- A cusp $F$ of $\Gamma_T \backslash \mathbb{D}*T$ (determined by an isotropic subspace of $Q = T*{\mathrm{Co}}$) maps to a cusp of $\Gamma_1 \backslash \mathbb{D}_1$ (determined by the same isotropic vectors viewed in $\Lambda_1$)
- This is exactly the **cusp map** from the Coble paper: $(9,9,1)_1 \mapsto (10,8,0)_1$ and $(7,7,1)_0 \mapsto (8,6,0)_0$
- The boundary strata of the Looijenga compactification over each cusp map to the corresponding boundary strata of Shah's compactification

**Key insight**: If we understand Shah's boundary strata over Sterk cusps (10,8,0) and (8,6,0), and we know the cusp map from the Coble paper, then we can trace GIT degenerations of 10-nodal sextics all the way to specific Coble cusps.

* * *

## What the Paper Actually Helps With

### It helps with: Understanding the Baily–Borel boundary

- The commutative diagram (Theorem 31, YZZ25.md:1162) shows that the image of $\pi_T$ in Shah's compactification is exactly $\overline{\mathcal{M}}_T$ (the closure of the Coble locus in Shah's GIT). The boundary of this closure consists of **Shah-semistable sextics** that are limits of 10-nodal sextics.
- Shah's classification of semistable sextics is known explicitly.
  Cross-referencing Shah's classification with the Coble locus closure would identify exactly which GIT boundary points are accessible from 10-nodal sextics.

### It helps with: The cusp enumeration (Blocker #2)

For the **unpolarized** case, the BB cusps of $\Gamma_{10A_1} \backslash \mathbb{D}*{10A_1}$ are the cusps of the Coble moduli.
If we can identify which Shah semistable orbits are in $\overline{\mathcal{M}}*{10A_1}$ and where they go in the BB of $\Gamma_1 \backslash \mathbb{D}_1$, then via the cusp map we can confirm the Coble cusp structure.

### It does NOT directly help with: IAS or KSBA construction

The GIT/Looijenga semifan and the KSBA semifan are **independently determined** objects — the KSBA by the degeneration theory of stable pairs (integral affine structures), the GIT by $\mathcal{H}^*_T$.
Knowing the GIT semifan does not constrain or determine the KSBA semifan.

What remains structurally interesting is the relative positions of these objects in the **poset of admissible semifans**:
- The Coxeter fan (from the reflection group of the cusp lattice)
- The KSBA semifan (once the Coble conjectures are resolved, this is determined)
- The GIT/Looijenga semifan (determined by $\mathcal{H}^*_T$)

Whether any of these refine, coarsen, or are incomparable to the others is an open question with potential structural significance, but it is orthogonal to the problem of constructing the KSBA compactification itself.

* * *

## Revised Action Items

- **Compute $\mathcal{H}^*_{10A_1}$**: Does $T_{\mathrm{Co}} \cong \langle 2 \rangle \oplus E_{10}(2)$ contain $(-2)$-vectors with divisibility 2 in $\Lambda_1$?
  This determines whether GIT = BB or GIT is a proper Looijenga compactification.
- **If $\mathcal{H}^*_{10A_1} \neq \emptyset$**: Determine the fan structure at each cusp.
  Is it a Coxeter fan?
  For which reflection group?
- **Identify Shah semistable orbits in $\overline{\mathcal{M}}_{10A_1}$**: What explicit sextic degenerations (double cubic, reducible sextics, etc.) lie in the closure of the 10-nodal locus?
  This is a GIT computation.
- **Trace boundary correspondence**: For each Shah orbit in $\overline{\mathcal{M}}_{10A_1}$, determine which cusp of BB it maps to via the cusp map.
  Does the double cubic land on the zero-cusp $(9,9,1)_1$ or the one-cusp $(7,7,1)_0$?
- **Locate the earlier Yu–Zheng paper on nodal sextics**: It may contain explicit boundary computations for specific cases.
- **Locate the GIT semifan in the poset of admissible semifans**: Once the GIT semifan is computed, determine where it sits relative to both the Coxeter fan and the KSBA semifan.
  In the typical literature setup, the KSBA semifan is a coarsening/refinement of the Coxeter semifan (wall removal).
  The GIT semifan is independently determined by $\mathcal{H}^*_T$.
  Implicit conjecture: whether the GIT semifan refines, coarsens, or is incomparable to either.
  (Note: the KSBA semifan is independently determined by the degeneration theory of stable pairs — it is NOT constrained by the GIT semifan.
  The interest is purely in whether their poset relationship is informative.)
- **Urabe–Yang enumeration**: Obtain the full classification of configurations $T$.
  For each $T$, the paper provides a lattice-polarized K3 moduli space $\mathcal{M}_T$ and a GIT = Looijenga compactification.
  Questions: (a) Does enumerating all $T$ enumerate all Severi varieties $\mathbb{P}\mathcal{V}_T$ of sextics with simple singularities?
  (b) Does YZZ25 thereby provide BB compactifications of each such Severi variety (mod PGL₃)? (c) Is GIT = semitoroidal established for all $T$, or only for specific cases?
