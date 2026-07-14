---
exported: 2026-05-11T03:53:30.262Z
source: NotebookLM
type: note
title: "Unresolved Obstacles in the Coble Divisor Proof"
---

# Unresolved Obstacles in the Coble Divisor Proof

导出时间: 5/11/2026, 11:53:30 AM

* * *

Based on the sources, while the narrative has been significantly refined, several key areas remain **"suspicious"** or mathematically unverified.
These points represent the transition from a proposed "research program" to the actual work required for a rigorous proof.

### 1. Irreducibility and the Root Orbit Uniqueness

The most prominent suspicion concerns whether the **polarized Coble divisor** is actually irreducible.

**The** ΓEn,2​ **Gap:** It is established that Namikawa’s uniqueness statement for (−2)\-vector orbits applies only modulo the full Enriques group ΓEn​\[1\]. Because ΓEn,2​ is a finite-index subgroup, it could theoretically split the single unpolarized orbit into multiple polarized branches\[2\].

**Branch-wise vs. Global Definition:** Without a formal double-coset computation or a GIT proof involving the transitivity of the D4​ action on the four torus fixed points, the definition of the moduli space as a single quotient D(δ⊥)/ΓCo,2​ remains a **choice of one branch** rather than a confirmed description of the full space\[6\].

### 2. Cusp Classification and Incidence Proofs

The specific counts of 0-cusps and 1-cusps for the polarized case have not been definitively proven.

**Insufficiency of Discriminant Forms:** The sources caution that simple discriminant-form computations (using AT​) only provide **candidates** for cusps\[10\].

**Reliance on Unperformed Computations:** A rigorous proof still requires explicit lattice-orbit arguments using Sterk’s representatives, stabilizers, and direct enumeration via a period-domain package\[11\]. The earlier "numerical tables" were discarded as unproved claims\[16\].

### 3. The "Trace Fan" Identity

The construction of the Coble semifan as a "trace" of the Enriques fan introduces logical hurdles:

**The Vinberg Trap:** The sources warn that running **Vinberg’s algorithm** on the Coble hyperplane lattice Mk,r​ is not, by itself, a proof of the KSBA fan\[17\].

**Restriction Issues:** It remains to be proven that the trace of the Enriques ramification arrangement doesn't include **extra roots** or that some Enriques walls don't coincide or restrict trivially in a way that alters the expected Coxeter structure\[17\].

### 4. KSBA Comparison Hard Points

The comparison between the KSBA closure and the semitoroidal compactification relies on several **"hard points"** that have been identified but not yet executed:

**No-Moduli-Loss Argument:** It must be proven that the stable quotient "remembers" the marked Coble root (the 41​(1,1)\-point)\[18\]. This is necessary to prevent a **strict coarsening** of the fan, which would fail the theorem\[21\].

**Fixed-Point Combinatorics:** While the generic Coble locus involves one torus fixed point, the closure involves curves passing through multiple points\[22\]. The proof must rigorously show how the normalization of the Heegner divisor correctly separates these branches\[18\].

### 5. Integral-Affine (IAS) Structure Gaps

The relationship between the abstract Coxeter diagrams and the actual IAS construction is still considered delicate:

**Upstairs vs. Downstairs:** The sources state it is "unclear" if an IAS can be built purely from the Enriques Coxeter diagram\[25\]. The construction currently depends on the "upstairs" K3 side, requiring the Enriques diagram to be proven as the source of all necessary visible-curve data\[21\]\[25\].

## **Admissibility:** The exact criteria for "admissibility" of roots must be checked against the folded K3-to-Enriques Coxeter data, particularly involving the extra reflection data at Sterk cusps 3 and 5\[26\]\[27\].

## 引用来源

[1] KSBA Compactification and Coble.md [2] KSBA Compactification and Coble.md [6] KSBA Compactification and Coble.md [10] KSBA Compactification and Coble.md [11] KSBA Compactification and Coble.md [16] KSBA Compactification and Coble.md [17] KSBA Compactification and Coble.md [18] KSBA Compactification and Coble.md [21] KSBA Compactification and Coble.md [22] KSBA Compactification and Coble.md [25] KSBA Compactification and Coble.md [26] KSBA Compactification and Coble.md [27] KSBA Compactification and Coble.md
