---
exported: 2026-05-11T03:52:50.841Z
source: NotebookLM
type: allChat
title: "NotebookLM Chat"
---


# NotebookLM Chat

导出时间: 5/11/2026, 11:52:50 AM

---

---

## � Today • 9:28 AM

### 🧑 **用户**

What were the explicit gaps identified and confirmed by the model in this conversation?

### 🤖 **助手**

In the course of this conversation, the user identified a series of critical mathematical and logical gaps in the initial research program, which the model subsequently confirmed and corrected. The explicit gaps identified and confirmed include:

**Lack of Root Uniqueness Statement:** The user pointed out there was no canonical or logical choice for the **Coble root** δ without a uniqueness statement\[1\]. The model later admitted it had incorrectly conflated **Namikawa’s** ΓEn​**\-orbit uniqueness** with the ΓEn,2​**\-orbit uniqueness** required for the degree-two polarized case\[2\]. Without proving that the pullback of the unpolarized Coble divisor to FEn,2​ is irreducible, TCo,2​\=δ⊥ represents only one branch of the moduli space rather than the full space\[5\]\[6\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: remark; status: source-backed; action: merge; reason: user identified conflation of Namikawa's Γ_En orbit uniqueness with Γ_En,2-orbit uniqueness; model admitted error; vault note now defines moduli space branchwise as a consequence; locator: Turn 1 item 1 <<}

**Insufficient Justification for the Arithmetic Group:** The user challenged the definition and relevance of the arithmetic group ΓCo,2​\[1\]. The model subsequently revised the definition to be the image of the **stabilizer of the Coble root** in ΓEn,2​, noting the previous definition was too large\[7\]\[8\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: remark; status: source-backed; action: merge; reason: user challenged definition of Γ_Co,2; model revised it to image of stabilizer of Coble root in Γ_En,2, replacing too-large previous definition; locator: Turn 1 item 2 <<}

**Oversimplification of the Branch-Curve Model:** The model initially claimed Coble degenerations were controlled by curves passing through exactly one torus fixed point\[9\]. The user noted this lacked justification and that the acting group was more complex\[1\]. The model corrected this, stating that passing through one fixed point only describes the **generic locus**; in the closure/normalization, curves may pass through several fixed points\[10\]\[11\]. It also confirmed the symmetry group is D4​⋉(C∗)2\[12\]\[13\].

{>> route: [[02_Moduli/Branch-curve model for polarized Coble surfaces]]; unit: remark; status: source-backed; action: merge; reason: captures correction from naive "one fixed point" model to generic locus only; closure involves multiple fixed points; symmetry group confirmed as D_4 ⋉ (C*)^2; locator: Turn 1 item 3 <<}

**Hand-waving of KSBA Stability:** The user noted the model skipped essential details regarding **ampleness and Cartier checks** for the stable pairs\[1\]\[14\]. The model provided a corrected narrative proving that the ramification divisor RX​ is ample, its descent RSˉ​ is Q\-Cartier and ample, and the quotient pair is **semi-log-canonical (slc)**\[15\].

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces]]; unit: remark; status: source-backed; action: merge; reason: user noted missing ampleness/Cartier checks; model replaced hand-waving with corrected narrative proving R_X ample, R_overline{S} Q-Cartier and ample, and quotient pair slc; locator: Turn 1 item 4 <<}

**Unsupported Cusp Counts and Orbit Enumeration:** The user criticized the model for "kicking the can" on actual root orbit computations and providing a "meaningless" incidence diagram\[1\]\[14\]. The model acknowledged these were unproved and discarded the initial tables\[20\]. It confirmed that valid counts require **Sterk's existing arguments**, explicit lattice representatives, or direct period-domain package enumeration rather than just discriminant-form shortcuts\[21\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: remark; status: source-backed; action: merge; reason: user criticized unsupported cusp counts and meaningless incidence diagram; model discarded initial tables; confirmed valid counts require Sterk arguments or period-domain enumeration, not discriminant-form shortcuts; locator: Turn 1 item 5 <<}

**Vague Semifan Construction:** The model's use of "expected dimension" was identified as meaningless\[1\]. The model replaced this with the concept of a **trace fan**, defining the Coble semifan as the intersection of the Enriques ramification semifan with the Coble Noether–Lefschetz subspace\[25\].

{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: remark; status: source-backed; action: merge; reason: user flagged "expected dimension" as meaningless; model replaced with trace fan concept as intersection of Enriques ramification semifan with Coble NL subspace; locator: Turn 1 item 6 <<}

**Incorrect Use of the "Maximal" Condition:** The user questioned whether "maximal" was necessary for Type III elliptic subdiagrams\[1\]\[28\]. The model clarified that while Type II rays are in bijection with **maximal parabolic subdiagrams**, Type III divisors are specifically defined by **rank-8 elliptic subdiagrams** in the nine-dimensional Coble space\[29\].

{>> route: [[03_Compactifications/Elliptic and Parabolic Subdiagrams]]; unit: remark; status: source-backed; action: merge; reason: captures correction that Type II rays correspond to maximal parabolic subdiagrams while Type III divisors are defined by rank-8 elliptic subdiagrams in 9-dimensional Coble space; locator: Turn 1 item 7 <<}

**Missing Mechanism for Integral-Affine Structures (IAS):** The user noted the lack of a clear relationship between the abstract Coxeter diagrams and the IAS\[1\]\[28\]. The model corrected this by grounding the IAS construction in the **K3-side data**, where the Coble condition is imposed as a **marked zero-length root** on a folded Enriques IAS\[32\].

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Upstairs-before-downstairs principle]]; unit: remark; status: source-backed; action: merge; reason: captures correction that IAS construction must be grounded in K3-side data, with Coble condition imposed as marked zero-length root on folded Enriques IAS; replaces unclear abstract-Coxeter-diagram approach; locator: Turn 1 item 8 <<}

**Equivariance of the Period Map:** The user noted that the equivariance of the map on period domains was "hand-waved"\[14\]. The model responded by explicitly formulating the equivariant inclusion ιδ​:D(δ⊥)↪D(TEn​) to justify the morphism of arithmetic quotients\[8\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Equivariance issue]]; unit: remark; status: source-backed; action: merge; reason: user flagged period-map equivariance as hand-waved; model replaced with explicit Γ_Co,2-equivariant inclusion ι_δ: D(δ^⊥) ↪ D(T_En) to justify morphism of arithmetic quotients; locator: Turn 1 item 9 <<}

> **来源：**
> [1] KSBA Compactification and Coble.md
> [2] KSBA Compactification and Coble.md
> [5] KSBA Compactification and Coble.md
> [6] KSBA Compactification and Coble.md
> [7] KSBA Compactification and Coble.md
> [8] KSBA Compactification and Coble.md
> [9] KSBA Compactification and Coble.md
> [10] KSBA Compactification and Coble.md
> [11] KSBA Compactification and Coble.md
> [12] KSBA Compactification and Coble.md
> [13] KSBA Compactification and Coble.md
> [14] KSBA Compactification and Coble.md
> [15] KSBA Compactification and Coble.md
> [20] KSBA Compactification and Coble.md
> [21] KSBA Compactification and Coble.md
> [25] KSBA Compactification and Coble.md
> [28] KSBA Compactification and Coble.md
> [29] KSBA Compactification and Coble.md
> [32] KSBA Compactification and Coble.md

### 🧑 **用户**

What remains suspicious?

### 🤖 **助手**

Based on the sources, while the narrative has been significantly refined, several key areas remain **"suspicious"** or mathematically unverified. These points represent the transition from a proposed "research program" to the actual work required for a rigorous proof.

### 1\. Irreducibility and the Root Orbit Uniqueness

The most prominent suspicion concerns whether the **polarized Coble divisor** is actually irreducible.

**The** ΓEn,2​ **Gap:** It is established that Namikawa’s uniqueness statement for (−2)\-vector orbits applies only modulo the full Enriques group ΓEn​\[1\]. Because ΓEn,2​ is a finite-index subgroup, it could theoretically split the single unpolarized orbit into multiple polarized branches\[2\].

**Branch-wise vs. Global Definition:** Without a formal double-coset computation or a GIT proof involving the transitivity of the D4​ action on the four torus fixed points, the definition of the moduli space as a single quotient D(δ⊥)/ΓCo,2​ remains a **choice of one branch** rather than a confirmed description of the full space\[6\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#How uniqueness could still be proved]]; unit: question; status: open; action: merge; reason: restates the Γ_En,2 gap: Namikawa's uniqueness applies only to Γ_En, not Γ_En,2; without double-coset computation or D_4 transitivity argument, D(δ^⊥)/Γ_Co,2 is just one branch; aligns with vault note's two safe routes; locator: Turn 2 item 1 <<}

### 2\. Cusp Classification and Incidence Proofs

The specific counts of 0-cusps and 1-cusps for the polarized case have not been definitively proven.

**Insufficiency of Discriminant Forms:** The sources caution that simple discriminant-form computations (using AT​) only provide **candidates** for cusps\[10\].

**Reliance on Unperformed Computations:** A rigorous proof still requires explicit lattice-orbit arguments using Sterk’s representatives, stabilizers, and direct enumeration via a period-domain package\[11\]. The earlier "numerical tables" were discarded as unproved claims\[16\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: question; status: open; action: merge; reason: observes that discriminant-form (A_T) analysis only provides cusp candidates; rigorous proof requires explicit lattice-orbit arguments using Sterk representatives, stabilizers, or period-domain package; locator: Turn 2 item 2 <<}

### 3\. The "Trace Fan" Identity

The construction of the Coble semifan as a "trace" of the Enriques fan introduces logical hurdles:

**The Vinberg Trap:** The sources warn that running **Vinberg’s algorithm** on the Coble hyperplane lattice Mk,r​ is not, by itself, a proof of the KSBA fan\[17\].

**Restriction Issues:** It remains to be proven that the trace of the Enriques ramification arrangement doesn't include **extra roots** or that some Enriques walls don't coincide or restrict trivially in a way that alters the expected Coxeter structure\[17\].

{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Proof obligations]]; unit: question; status: open; action: merge; reason: warns that Vinberg's algorithm on M_k,r is not a proof of the KSBA fan; must prove no extra roots appear and Enriques walls do not restrict/coincide incorrectly; locator: Turn 2 item 3 <<}

### 4\. KSBA Comparison Hard Points

The comparison between the KSBA closure and the semitoroidal compactification relies on several **"hard points"** that have been identified but not yet executed:

**No-Moduli-Loss Argument:** It must be proven that the stable quotient "remembers" the marked Coble root (the 41​(1,1)\-point)\[18\]. This is necessary to prevent a **strict coarsening** of the fan, which would fail the theorem\[21\].

**Fixed-Point Combinatorics:** While the generic Coble locus involves one torus fixed point, the closure involves curves passing through multiple points\[22\]. The proof must rigorously show how the normalization of the Heegner divisor correctly separates these branches\[18\].

{>> route: [[05_Results/KSBA vs. semitoroidal comparison for polarized Coble moduli#Why this is a conjecture]]; unit: question; status: open; action: merge; reason: no-moduli-loss argument needed to prove stable quotient remembers the 1/4(1,1) Coble root point; fixed-point combinatorics proof needed for normalization separating multi-point branches; locator: Turn 2 item 4 <<}

### 5\. Integral-Affine (IAS) Structure Gaps

The relationship between the abstract Coxeter diagrams and the actual IAS construction is still considered delicate:

**Upstairs vs. Downstairs:** The sources state it is "unclear" if an IAS can be built purely from the Enriques Coxeter diagram\[25\]. The construction currently depends on the "upstairs" K3 side, requiring the Enriques diagram to be proven as the source of all necessary visible-curve data\[21\]\[25\].

**Admissibility:** The exact criteria for "admissibility" of roots must be checked against the folded K3-to-Enriques Coxeter data, particularly involving the extra reflection data at Sterk cusps 3 and 5\[26\]\[27\].

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Upstairs-before-downstairs principle]]; unit: question; status: open; action: merge; reason: observes it is unclear if IAS can be built purely from Enriques Coxeter diagram; construction depends on K3-side data; admissibility criteria must be checked against folded K3-to-Enriques Coxeter data, especially at Sterk cusps 3 and 5; locator: Turn 2 item 5 <<}

> **来源：**
> [1] KSBA Compactification and Coble.md
> [2] KSBA Compactification and Coble.md
> [6] KSBA Compactification and Coble.md
> [10] KSBA Compactification and Coble.md
> [11] KSBA Compactification and Coble.md
> [16] KSBA Compactification and Coble.md
> [17] KSBA Compactification and Coble.md
> [18] KSBA Compactification and Coble.md
> [21] KSBA Compactification and Coble.md
> [22] KSBA Compactification and Coble.md
> [25] KSBA Compactification and Coble.md
> [26] KSBA Compactification and Coble.md
> [27] KSBA Compactification and Coble.md

### 🧑 **用户**

This conversation churned because of gaps and issues. Reconstruct a detailed coherent list of claims, implications, and references to the proof sketch in the original document. Every nontrivial fact or claim must be present on this list

### 🤖 **助手**

Drawing on the provided source, which documents the refinement of a research program into a rigorous proof sketch, the following is a detailed and coherent list of claims, implications, and references regarding the **KSBA compactification of the polarized Coble moduli space**.

### I. Ambient Lattice and Period Setup

**The Enriques Lattice:** The base for the construction is the degree-two Enriques period lattice TEn​\=U⊕U(2)⊕E8​(−2)\[1\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates T_En = U⊕U(2)⊕E8(−2) lattice identity; content already routed from Turn 1 items 1-2 and vault note's Corrected framework section; preserved for provenance of initial claim-list reconstruction; locator: Turn 3 Section I Enriques Lattice item <<}

**The Arithmetic Group:** The relevant group is the degree-two arithmetic group ΓEn,2​\=O(TEn​)∩O(TdP​), which captures the K3-lattice isometries fixing the degree-two polarization\[2\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates Γ_En,2 = O(T_En) ∩ O(T_dP) as the degree-two arithmetic group; content already routed from Turn 1 items 1-2 and vault note's Corrected framework section; preserved for provenance; locator: Turn 3 Section I Arithmetic Group item <<}

**The Moduli Space:** The ambient space is FEn,2​\=D(TEn​)/ΓEn,2​, which embeds via a Noether–Lefschetz (NL) condition into the ten-dimensional space F(2,2,0)\[2\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates F_En,2 = D(T_En)/Γ_En,2 as NL locus in F(2,2,0); content already routed from Turn 1 items 1-2 and vault note's Corrected framework section; preserved for provenance; locator: Turn 3 Section I Moduli Space item <<}


### II. Definition and Normalization of the Coble Moduli Space

**The Coble Divisor:** The Coble divisor HCo,2​ is defined as the Heegner divisor in FEn,2​ whose hyperplanes correspond to the nodal K3/Coble condition\[3\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates Coble divisor H_Co,2 as Heegner divisor in F_En,2 whose hyperplanes correspond to the nodal K3/Coble condition; already covered in vault note's Corrected framework section; locator: Turn 3 Section II Coble Divisor item <<}

**Normalization and Orbits:** The polarized Coble moduli space FCo,2​ is the **normalization** of this divisor\[4\]. Because ΓEn,2​ is a finite-index subgroup, it may split the unique unpolarized root orbit into multiple branches; thus, FCo,2​ is defined as a disjoint union of quotients D(ra⊥​)/Γa​ over these orbits \[ra​\]\[4\]\[5\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates branchwise normalization definition: F_Co,2 as disjoint union of D(r_a^⊥)/Γ_a over root orbits, due to Γ_En,2 finite-index splitting the unpolarized orbit; already covered in vault note's Corrected framework section; locator: Turn 3 Section II Normalization item <<}

**Arithmetic Group for Coble:** The group Γa​ (or ΓCo,2​ for a specific root δ) is the image of the stabilizer of the root in ΓEn,2​ acting on the orthogonal complement ra⊥​\[4\]\[6\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates Γ_a as image of root stabilizer in Γ_En,2 acting on r_a^⊥; already covered in vault note's Corrected framework section; locator: Turn 3 Section II Arithmetic Group item <<}
**Lattice Identity:** The transcendental lattice for a polarized Coble surface is TCo,2​≃⟨2⟩⊕E10​(2), identified as the orthogonal complement δTEn​⊥​ of a vanishing root δ\[7\].

{>> route: [[01_Lattices/Coble lattice]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: states T_Co,2 ≃ ⟨2⟩ ⊕ E10(2) as δ^⊥ in T_En; already covered in Coble lattice note Basic properties section; preserved for provenance; locator: Turn 3 Section II Lattice Identity item <<}

**Equivariance:** The map FCo,2​→FEn,2​ is a well-defined morphism of arithmetic quotients because the inclusion D(δ⊥)↪D(TEn​) is ΓCo,2​\-equivariant\[5\]\[6\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Equivariance issue]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates equivariance claim from Turn 1 item 9; already routed in vault note's Equivariance issue section; locator: Turn 3 Section II Equivariance paragraph <<}

### III. The Branch-Curve Model and Geometry

{>> route: [[02_Moduli/Branch-curve model for polarized Coble surfaces]]; unit: construction; status: duplicate; action: preserve-source-visible; reason: restates Horikawa model Y=P1×P1 with τ(x,y)=(−x,−y) from Turn 1 item 3; content already in vault note; locator: Turn 3 Section III Horikawa Model item <<}
**Horikawa Model:** The geometric model uses Y\=P1×P1 with the involution τ(x,y)\=(−x,−y)\[8\].

{>> route: [[02_Moduli/Branch-curve model for polarized Coble surfaces]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates acting group D4⋉(C*)2 from Turn 1 item 3; content already in vault note; locator: Turn 3 Section III Quotient Group item <<}
**Quotient Group:** The acting group on the space of invariant (4,4) polynomials is D4​⋉(C∗)2\[8\]\[9\].

{>> route: [[02_Moduli/Branch-curve model for polarized Coble surfaces]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates open Coble condition (one fixed point, det(q2)≠0 inducing A1-node) from Turn 1 item 3; content already in vault note; locator: Turn 3 Section III Coble Locus Condition item <<}
**Coble Locus Condition:** The open Coble locus corresponds to invariant curves B passing through **exactly one** of the four torus fixed points pi​ with an ordinary node (local expansion f\=q2​+O(4) with det(q2​)\=0)\[9\]\[10\].

{>> route: [[02_Moduli/Branch-curve model for polarized Coble surfaces]]; unit: fact; status: duplicate; action: preserve-source-visible; reason: restates closure behavior (multiple fixed points, normalization marks root) from Turn 1 item 3; content already in vault note; locator: Turn 3 Section III Closure Behavior item <<}
**Closure Behavior:** In the KSBA closure, curves may pass through multiple fixed points; the normalization of the divisor separates these branches by marking a specific Coble root\[10\]\[11\].

### IV. KSBA Stability and Stable Pairs

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates stable pair definition (S̄, ϵR_S̄) from source [12]; content already in vault note's Stable-pair package checklist; preserved for provenance; locator: Turn 3 Section IV Stable Pair Definition item <<}

**Stable Pair Definition:** The open Coble stable pair is (Sˉ,ϵRSˉ​) for 0<ϵ≪1\[12\].

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Conjectural local package]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates 1/4(1,1) cyclic quotient singularity claim from source [13][14]; content already in vault note's Conjectural local package; preserved for provenance; locator: Turn 3 Section IV Singularities item <<}

**Singularities:**Sˉ is the quotient of a nodal K3 surface by the Enriques involution; it contains a **cyclic quotient singularity of type** 41​(1,1) at the fixed node\[13\]\[14\].

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates ampleness of R_X on K3 cover and descent to Q-Cartier ample R_S̄ from source [13][14]; content already in vault note's Stable-pair package checklist; preserved for provenance; locator: Turn 3 Section IV Ampleness and Descent item <<}

**Ampleness and Descent:** The ramification divisor RX​ is ample on the K3 cover X; its descent RSˉ​ is Q\-Cartier and ample, ensuring KSˉ​+ϵRSˉ​ is ample for small ϵ\[13\]\[14\].

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Conjectural local package]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates slc condition reasoning from du Val singularities and finite quasi-étale quotient from source [15]; content already in vault note's Conjectural local package; preserved for provenance; locator: Turn 3 Section IV SLC Condition item <<}

**SLC Condition:** The pairs are semi-log-canonical (slc) because the cover X has du Val singularities and the quotient is finite and quasi-étale in codimension one\[15\].

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates anti-bicanonical (−4)-curve C contraction to 1/4(1,1) point from source [12]; content already in vault note's Stable-pair package (track how curve is seen); preserved for provenance; locator: Turn 3 Section IV Resolution Relation item <<}

**Resolution Relation:** On the minimal resolution S, there is an exceptional anti-bicanonical (−4)\-curve C, which is **contracted** in the KSBA model back to the 41​(1,1) point\[12\].


{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates cusp-pair definition (I,r) and (J,r) as Γ_En,2-orbits; already routed from Turn 1 item 5; locator: Turn 3 Section V Cusp Data item <<}

### V. Baily–Borel Cusp Classification

**Cusp Data:** 0-cusps and 1-cusps are defined as ΓEn,2​\-orbits of pairs (I,r) and (J,r), where I and J are primitive isotropic lines and planes, respectively, and r is a perpendicular Coble root\[16\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates mapping to Sterk's five 0-cusps and nine 1-cusps; already routed from Turn 1 item 5 and Turn 7 item 2; locator: Turn 3 Section V Reduction to Sterk item <<}
**Reduction to Sterk:** These cusps map to Sterk’s five 0-cusps and nine 1-cusps of the Enriques space\[17\]\[18\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates admissibility criterion for roots in cusp lattice M_k = I_k^⊥/I_k; already routed from Turn 1 item 5; locator: Turn 3 Section V Admissibility item <<}
**Admissibility:** A root in the cusp lattice Mk​\=Ik⊥​/Ik​ is admissible if it lifts to a primitive (−2)\-root in TEn​ that belongs to the designated Coble orbit\[18\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Discarded numerical attempts]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates requirement for explicit lattice-orbit enumeration; already routed from Turn 1 item 5, Turn 2 item 2, Turn 6; locator: Turn 3 Section V Verification item <<}
**Verification:** Numerical cusp tables and incidence diagrams require explicit lattice-orbit enumeration or the period-domain package rather than simple discriminant-form counts\[19\].

### VI. The Coble Semifan and Boundary Strata

**Trace Construction:** The Coble semifan Fk,rCo​ is the **trace** of the Enriques ramification semifan FkEn​ onto the hyperplane Mk,r​\=rMk​⊥​\[23\].
{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates trace construction definition; already routed from Turn 1 items 6-7; locator: Turn 3 Section VI Trace Construction <<}

**Relevance Rule:** A Coble wall is irrelevant if and only if every Enriques wall restricting to it is irrelevant\[24\].
{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates relevance inheritance rule; already routed from Turn 1 items 6-7; locator: Turn 3 Section VI Relevance Rule <<}

**Strata Dictionary:**

**Type II Divisors:** Correspond to rational isotropic rays surviving the coarsening, which are in bijection with maximal parabolic subdiagrams\[24\].
{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates Type II = maximal parabolic subdiagrams; already routed from Turn 1 items 6-7; locator: Turn 3 Section VI Type II <<}

**Type III Divisors:** Correspond to rank-8 elliptic subdiagrams (since the Coble space dimension is 9)\[25\].
{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates Type III = rank-8 elliptic subdiagrams; already routed from Turn 1 items 6-7; locator: Turn 3 Section VI Type III <<}

**Type III Strata:** Higher-codimension strata correspond to lower-rank elliptic subdiagrams\[25\]\[26\].
{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates higher-codimension strata claim; already routed from Turn 1 items 6-7; locator: Turn 3 Section VI Type III Strata <<}

### VII. The KSBA Comparison Theorem

{>> route: [[05_Results/KSBA vs. semitoroidal comparison for polarized Coble moduli#Proposed statement]]; unit: conjecture; status: duplicate; action: preserve-source-visible; reason: states the conjectural KSBA comparison theorem: normalization of KSBA closure ≅ semitoroidal compactification from trace semifans; target note frames this proposed statement as a conjecture with open proof obligations; locator: Turn 3 Section VII Theorem Statement <<}

**Theorem Statement:** The normalization of the KSBA closure (FCo,2KSBA​)ν is isomorphic to the semitoroidal compactification defined by the trace semifans FCo​\[27\].

{>> route: [[05_Results/KSBA vs. semitoroidal comparison for polarized Coble moduli#Proof architecture in the inbox]]; unit: construction; status: duplicate; action: preserve-source-visible; reason: proof mechanism: restrict universal K3 stable-pair family to Coble NL-locus, then extend Enriques involution over stable limits via uniqueness of KSBA limits; construction step for the comparison proof; already covered in vault note's Proof architecture section; locator: Turn 3 Section VII Core Proof Mechanism <<}

**Core Proof Mechanism:**

Restrict the universal K3 stable-pair family over F(2,2,0) to the Coble NL-locus\[28\].

Extend the Enriques involution over the stable limits by the uniqueness of KSBA limits\[28\].

{>> route: [[05_Results/KSBA vs. semitoroidal comparison for polarized Coble moduli#Why this is a conjecture]]; unit: conjecture; status: duplicate; action: preserve-source-visible; reason: no-moduli-loss: must prove stable quotient remembers the 1/4(1,1) Coble root point to prevent strict coarsening of trace fan; open proof obligation; already listed in vault note's Why this is a conjecture section; locator: Turn 3 Section VII No-Moduli-Loss <<}

**No-Moduli-Loss:** Prove the stable quotient "remembers" the Coble root (the 41​(1,1) point), which prevents any fan coarsening beyond the trace fan\[29\].

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Upstairs-before-downstairs principle]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates upstairs construction (K3-first), zero-length root λ·r=0, geometric sequence (K3→Enriques→Coble), and A1-node interpretation from Turn 1 item 8 and Turn 2 item 5; no new claims; locator: Turn 3 Section VIII <<}
### VIII. Integral-Affine Structures (IAS)

**Upstairs Construction:** IAS data must be assigned on the K3 side first\[29\].

**Coble Constraint:** The Coble condition is imposed by marking a **zero-length root**r (satisfying λ⋅r\=0) in the K3 Coxeter chamber\[30\].

**Geometric Sequence:** The construction follows a sequence from K3 Coxeter/IAS data to folded Enriques data, and finally to Coble marked-root trace data\[31\].

**Local Interpretation:** The marked root represents the A1​\-node on the K3 cover fixed by the involution\[30\]\[31\].

> **来源：**
> [1] KSBA Compactification and Coble.md
> [2] KSBA Compactification and Coble.md
> [3] KSBA Compactification and Coble.md
> [4] KSBA Compactification and Coble.md
> [5] KSBA Compactification and Coble.md
> [6] KSBA Compactification and Coble.md
> [7] KSBA Compactification and Coble.md
> [8] KSBA Compactification and Coble.md
> [9] KSBA Compactification and Coble.md
> [10] KSBA Compactification and Coble.md
> [11] KSBA Compactification and Coble.md
> [12] KSBA Compactification and Coble.md
> [13] KSBA Compactification and Coble.md
> [14] KSBA Compactification and Coble.md
> [15] KSBA Compactification and Coble.md
> [16] KSBA Compactification and Coble.md
> [17] KSBA Compactification and Coble.md
> [18] KSBA Compactification and Coble.md
> [19] KSBA Compactification and Coble.md
> [23] KSBA Compactification and Coble.md
> [24] KSBA Compactification and Coble.md
> [25] KSBA Compactification and Coble.md
> [26] KSBA Compactification and Coble.md
> [27] KSBA Compactification and Coble.md
> [28] KSBA Compactification and Coble.md
> [29] KSBA Compactification and Coble.md
> [30] KSBA Compactification and Coble.md
> [31] KSBA Compactification and Coble.md



### 🧑 **用户**

That was far, FAR too short to be rigorous and detailed enough

### 🤖 **助手**

To provide the level of rigor and detail required, the following is a comprehensive reconstruction of the proof sketch for the **KSBA compactification of the polarized Coble moduli space**, incorporating the mathematical mechanisms, logical dependencies, and specific citations from the source.



### I. Ambient Lattice and Arithmetic Framework

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: fact; status: duplicate; action: preserve-source-visible; reason: restates T_En = U⊕U(2)⊕E8(−2) lattice identity from source [1]; already routed from Turn 1 item 1 and vault note's Corrected framework section; preserved for provenance; locator: Turn 4 Section I Enriques Lattice item <<}

**The Enriques Lattice:** The construction begins with the degree-two Enriques period lattice TEn​\=U⊕U(2)⊕E8​(−2)\[1\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: fact; status: duplicate; action: preserve-source-visible; reason: restates Γ_En,2 = Γ_En ∩ Γ_dP as the degree-two arithmetic group from source [2]; already routed from Turn 1 item 2 and vault note's Corrected framework section; preserved for provenance; locator: Turn 4 Section I Polarized Arithmetic Group item <<}

**The Polarized Arithmetic Group:** The group governing the degree-two moduli problem is ΓEn,2​\=ΓEn​∩ΓdP​, which consists of K3-lattice isometries that commute with the Enriques involution and fix the degree-two polarization h\[2\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: fact; status: duplicate; action: preserve-source-visible; reason: restates F_En,2 = D(T_En)/Γ_En,2 as NL locus in F(2,2,0) from source [2]; already routed from Turn 1 items 1-2 and vault note's Corrected framework section; preserved for provenance; locator: Turn 4 Section I Noether-Lefschetz Embedding item <<}

**The Noether–Lefschetz Embedding:** The resulting period space FEn,2​\=D(TEn​)/ΓEn,2​ is identified as a Noether–Lefschetz (NL) locus inside the ten-dimensional space F(2,2,0)\[2\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: fact; status: duplicate; action: preserve-source-visible; reason: restates Heegner-normalization definition and branchwise formulation from Turn 1 items 1-2; already covered in vault note's Corrected framework section; Equivariance and Lattice Transcendental Identity items routed separately; locator: Turn 4 Section II Heegner-normalization and branchwise paragraphs <<}

### II. Rigorous Definition of the Coble Moduli Space

**The Coble Divisor as a Heegner Normalization:** Let RCo,2​⊂TEn​ be the set of primitive (−2)\-roots whose Heegner hyperplanes correspond to the nodal K3/Coble condition\[3\]. The polarized Coble moduli space is defined as the **normalization** of the associated Heegner divisor: FCo,2​:=HCo,2ν​\[4\].

**Branchwise Formulation:** Due to the potential for ΓEn,2​ (a finite-index subgroup) to split the unique unpolarized root orbit, the space is rigorously defined as a disjoint union of branches: FCo,2​\=⨆a\=1m​D(ra⊥​)/Γa​, where Γa​ is the image of the root stabilizer in ΓEn,2​ acting on the orthogonal complement ra⊥​\[4\].

**Equivariance of the Period Map:** The map FCo,2​→FEn,2​ is well-defined because the inclusion ιδ​:D(δ⊥)↪D(TEn​) is equivariant for the stabilizer: for g∈Stab(Zδ), ιδ​(gω)\=gιδ​(ω)\[5\]\[6\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Equivariance issue]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates equivariance claim from Turn 1 item 9; already routed in vault note's Equivariance issue section; locator: Turn 4 Section II Equivariance paragraph <<}

**Lattice Transcendental Identity:** The transcendental lattice for a polarized Coble surface is TCo,2​≃⟨2⟩⊕E10​(2), which is geometrically identified with the orthogonal complement δ⊥ of the vanishing Coble root\[7\]\[8\].

{>> route: [[01_Lattices/Coble lattice]]; unit: fact; status: duplicate; action: preserve-source-visible; reason: states T_Co,2 ≃ ⟨2⟩ ⊕ E10(2) as δ⊥; already covered in Coble lattice note Basic properties section; preserved for provenance; locator: Turn 4 Section II Lattice Transcendental Identity item <<}

{>> route: [[02_Moduli/Branch-curve model for polarized Coble surfaces]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates acting group D4⋉(C*)2, local expansion at torus fixed points, generic Coble locus condition (one fixed point, det(q2)≠0 inducing A1-node), and normalization logic from Turn 1 item 3; no new claims; locator: Turn 4 Section III <<}
### III. The Branch-Curve Model and GIT

**Acting Group:** The geometric model uses Y\=P1×P1 with involution τ. The acting group on the space of invariant (4,4) polynomials is G\=D4​⋉(C∗)2\[9\].

**Local Expansion at Torus Fixed Points:** At a torus fixed point pi​, a τ\-invariant curve B\=(f\=0) has an expansion f\=q2​+q4​+q6​+… because the linear part vanishes under the involution\[10\].

**The Generic Coble Locus:** The generic point of the Coble divisor corresponds to curves passing through **exactly one** torus fixed point pi​ such that det(q2​)\=0\[10\]\[11\]. This condition induces an A1​\-singularity on the K3 double cover X\={z2\=f(u,v)}\[10\].

**Normalization Logic:** In the KSBA closure, curves may pass through multiple points. The normalization of the Heegner divisor separates these branches by marking exactly one of the vanishing fixed-node roots\[10\].

### IV. Stability of the Coble Pairs

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: construction; status: conjectural; action: preserve-source-visible; reason: proposes the stable surface as the quotient S̄ = X/⟨ι_En⟩ with a 1/4(1,1) cyclic quotient singularity at the fixed node; the target note records this as part of the intended stable-pair package and conjectural local package, not as a settled definition; locator: Turn 4 Section IV Stable Surface item <<}
**The Stable Surface** Sˉ**:** The stable surface in the KSBA problem is the quotient Sˉ\=X/⟨ιEn​⟩, which contains a cyclic quotient singularity of type 41​(1,1) at the fixed node\[12\]\[13\].

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: question; status: open; action: preserve-source-visible; reason: states the intended ampleness argument via R_X as pullback of O(2,2), descent to R_S̄, and ampleness of K_S̄+ϵR_S̄; the target note records this as a proof obligation to prove Q-Cartier descent and ampleness, not as an established fact; locator: Turn 4 Section IV Ampleness item <<}
**Ampleness of the Ramification Divisor:** The ramification divisor RX​ is the pullback of OY​(2,2), making it ample on X\[12\]. Because the quotient map q:X→Sˉ is finite and RX​ descends to RSˉ​, the log canonical divisor KSˉ​+ϵRSˉ​ is ample for 0<ϵ≪1\[13\].

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: question; status: open; action: preserve-source-visible; reason: states the proposed slc argument through du Val singularities on the K3 cover and a finite quasi-etale quotient in codimension one; the target note explicitly frames slc verification as still needing proof; locator: Turn 4 Section IV SLC item <<}
**SLC Condition:** The pair (Sˉ,ϵRSˉ​) is semi-log-canonical (slc) because the cover X has du Val (canonical) singularities and the quotient is finite and quasi-étale in codimension one\[14\].

{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: question; status: open; action: preserve-source-visible; reason: states that the exceptional (−4)-curve C on the minimal resolution satisfies 2K_S+C∼0 and is contracted in the KSBA model; the target note treats this as something to track between the resolution and stable model within the conjectural local package; locator: Turn 4 Section IV Resolution item <<}
**Minimal Resolution Relation:** On the resolution S, the exceptional anti-bicanonical (−4)\-curve C satisfies 2KS​+C∼0. The KSBA model **contracts** C back to the 41​(1,1) point\[15\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates cusp pairs (I,r) and (J,r), reduction to Sterk, admissibility, and incidence mechanism (I⊂J) from Turn 1 item 5 and Turn 2 item 2; no new claims; locator: Turn 4 Section V <<}
### V. Baily–Borel Cusp Classification

**Cusp Pairs:** Baily–Borel 0-cusps and 1-cusps of FCo,2​ are ΓEn,2​\-orbits of pairs (I,r) and (J,r), where I and J are primitive isotropic lines and planes in TEn​ and r is a perpendicular Coble root\[16\].

**Reduction to Sterk:** These map to Sterk's five 0-cusps (1−5) and nine 1-cusps of the Enriques space via (I,r)↦I\[17\].

**Admissibility of Roots:** A root rˉ in the cusp lattice Mk​\=Ik⊥​/Ik​ is admissible if and only if it lifts to a primitive root r∈TEn​ that has square −2 and belongs to the designated Coble root orbit\[17\]\[18\].

**Incidence Mechanism:** Incidence between a 1-cusp (J,r) and 0-cusp (I,r) occurs if and only if I⊂J\[17\]\[19\].

{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates trace rule, relevance inheritance, strata definitions (Type II=parabolic, Type III=elliptic subdiagrams) from Turn 1 items 6-7 and Turn 2 item 3; no new claims; locator: Turn 4 Section VI <<}
### VI. The Trace Semifan Construction

**The Trace Rule:** At a Coble cusp (Ik​,r), the Coble semifan Fk,rCo​ is defined as the **trace** of the Enriques ramification semifan FkEn​ onto the hyperplane Mk,r​\=rMk​⊥​\[20\].

**Relevance Inheritance:** A wall in the Coble fan is **irrelevant** if and only if every Enriques wall restricting to it is irrelevant\[19\].

**Strata Definitions:**

**Type II Divisors:** Correspond to surviving **maximal parabolic subdiagrams** (which generate rational isotropic rays)\[19\].

**Type III Divisors:** Correspond to surviving **rank-8 elliptic subdiagrams**\[21\].

**Higher Codimension:** Higher-codimension Type III strata correspond to lower-rank elliptic subdiagrams\[21\].

{>> route: [[05_Results/KSBA vs. semitoroidal comparison for polarized Coble moduli#Why this is a conjecture]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates theorem statement, hard points (Heegner normalization, stable limit extension, trace fan stability, no-moduli-loss) from Turn 2 item 4 and Turn 7 item 4; no new claims; locator: Turn 4 Section VII <<}
### VII. The KSBA Comparison Theorem

**Theorem Statement:** The normalization of the KSBA closure (FCo,2KSBA​)ν is isomorphic to the semitoroidal compactification defined by the trace semifans FCo​\[22\].

**Hard Points of the Proof:**

**Validity of Heegner Normalization:** Proving FCo,2​ is the correct period quotient for the polarized open locus\[23\].

**Stable Limit Extension:** Extending the Enriques involution over the stable limits of K3 pairs by the uniqueness of KSBA limits\[23\].

**Trace Fan Stability:** Showing no additional Coxeter walls are required beyond the trace of the Enriques ramification fan\[23\].

**No-Moduli-Loss:** Proving the stable quotient "remembers" the marked Coble root (the 41​(1,1) point), which prevents a strict coarsening of the trace fan\[24\].

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Upstairs-before-downstairs principle]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates construction direction (K3-first), zero-length root constraint λ·r=0, geometric chain K3→Enriques→Coble, and vanishing cycle interpretation from Turn 1 item 8 and Turn 2 item 5; no new claims; locator: Turn 4 Section VIII <<}
### VIII. Integral-Affine Structures (IAS)

**Construction Direction:** IAS data must be assigned first to the K3 Coxeter/IAS data\[25\].

**The Coble Constraint:** The Coble condition is imposed by marking a **zero-length root**r (satisfying λ⋅r\=0) in the K3 Coxeter chamber\[26\].

**Geometric Chain:** The construction follows the sequence: K3 Coxeter/IAS data → folded Enriques IAS data → Coble marked-root trace data\[25\].

**Vanishing Cycle:** Geometrically, the marked root represents the A1​\-node on the K3 cover that is fixed by the Enriques involution\[25\].

> **来源：**
> [1] KSBA Compactification and Coble.md
> [2] KSBA Compactification and Coble.md
> [3] KSBA Compactification and Coble.md
> [4] KSBA Compactification and Coble.md
> [5] KSBA Compactification and Coble.md
> [6] KSBA Compactification and Coble.md
> [7] KSBA Compactification and Coble.md
> [8] KSBA Compactification and Coble.md
> [9] KSBA Compactification and Coble.md
> [10] KSBA Compactification and Coble.md
> [11] KSBA Compactification and Coble.md
> [12] KSBA Compactification and Coble.md
> [13] KSBA Compactification and Coble.md
> [14] KSBA Compactification and Coble.md
> [15] KSBA Compactification and Coble.md
> [16] KSBA Compactification and Coble.md
> [17] KSBA Compactification and Coble.md
> [18] KSBA Compactification and Coble.md
> [19] KSBA Compactification and Coble.md
> [20] KSBA Compactification and Coble.md
> [21] KSBA Compactification and Coble.md
> [22] KSBA Compactification and Coble.md
> [23] KSBA Compactification and Coble.md
> [24] KSBA Compactification and Coble.md
> [25] KSBA Compactification and Coble.md
> [26] KSBA Compactification and Coble.md



### 🧑 **用户**

Formulate as a list of claims

### 🤖 **助手**

Based on the sources, the following claims constitute the rigorous framework for the **KSBA compactification of the polarized Coble moduli space**:

### I. Period Space and Moduli Definition

**Ambient Lattice and Group:** The construction is rooted in the degree-two Enriques period lattice TEn​\=U⊕U(2)⊕E8​(−2), with the arithmetic group ΓEn,2​\=ΓEn​∩ΓdP​ governing the moduli problem\[1\]\[2\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: names Enriques period lattice T_En and polarized arithmetic group Γ_En,2; already in vault note's Corrected framework section; locator: Turn 5 Section I Ambient Lattice and Group <<}

**Coble Moduli as a Heegner Normalization:** The polarized Coble moduli space FCo,2​ is formally defined as the **normalization of the Heegner divisor**HCo,2​ in FEn,2​\[3\]\[4\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: defines F_Co,2 as normalization of Heegner divisor H_Co,2; already in vault note's Corrected framework section; locator: Turn 5 Section I Heegner normalization <<}

**Branchwise Identification:** Because ΓEn,2​ is a finite-index subgroup, it may split the unique unpolarized root orbit into multiple branches; thus, FCo,2​ is rigorously a disjoint union of quotients D(ra⊥​)/Γa​ over these orbits\[4\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Corrected framework]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: defines F_Co,2 as disjoint union of D(r_a^⊥)/Γ_a due to finite-index splitting; already in vault note's Corrected framework section; locator: Turn 5 Section I Branchwise Identification <<}

**Equivariance of the Period Map:** The map FCo,2​→FEn,2​ is a well-defined morphism of arithmetic quotients because the inclusion ιδ​:D(δ⊥)↪D(TEn​) is equivariant for the stabilizer of the Coble root\[7\]\[8\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#Equivariance issue]]; unit: proposition; status: duplicate; action: preserve-source-visible; reason: asserts that the stabilizer-equivariant period-domain inclusion induces a well-defined map of arithmetic quotients; target section records this quotient-map condition; locator: Turn 5 Section I Equivariance item <<}

**Lattice Identity:** The transcendental lattice for a polarized Coble surface is TCo,2​≃⟨2⟩⊕E10​(2), identified geometrically as the orthogonal complement δ⊥ of the vanishing fixed-node root\[9\].

{>> route: [[01_Lattices/Coble lattice#Basic properties]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: states T_Co,2 ≃ ⟨2⟩ ⊕ E10(2) as δ⊥ identification; already in Coble lattice note Basic properties section; locator: Turn 5 Section I Lattice Identity <<}

{>> route: [[02_Moduli/Branch-curve model for polarized Coble surfaces]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates Horikawa model setup and generic-locus vs. closure conditions from Turn 1 item 3; already routed to Branch-curve model note; locator: Turn 5 Section II branch-curve items <<}

### II. Geometric Model and Stability

**The Branch-Curve Model:** In the Horikawa model on Y\=P1×P1, the acting group is G\=D4​⋉(C∗)2\[12\]\[13\].

**Generic vs. Closure Conditions:** The generic Coble locus involves curves passing through **exactly one torus fixed point** with a nondegenerate quadratic part q2​; however, the closure and its normalization must account for curves passing through multiple fixed points\[14\].

**The Stable Pair** (Sˉ,ϵRSˉ​)**:** The open Coble stable pair consists of a surface Sˉ with a **cyclic quotient singularity of type** 41​(1,1) and an ample ramification divisor RSˉ​\[17\].
{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Conjectural local package]]; unit: construction; status: conjectural; action: preserve-source-visible; reason: proposes the stable pair with 1/4(1,1) singularity; the target note already records this in the Conjectural local package as pending formal verification rather than as a settled definition; locator: Turn 5 Section II Stable Pair item <<}

**Ampleness and Descent:** The ramification divisor RX​ is ample on the K3 cover X and descends to a Q\-Cartier ample divisor RSˉ​, ensuring KSˉ​+ϵRSˉ​ is ample\[20\].
{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: question; status: open; action: preserve-source-visible; reason: restates ampleness/descent claim from Turn 1 item 4; target note's Stable-pair package records Q-Cartier and ampleness as open proof obligations, not established facts; locator: Turn 5 Section II Ampleness item <<}

**SLC Singularity Condition:** The pairs are semi-log-canonical (slc) because the cover X has du Val singularities and the quotient map is finite and quasi-étale in codimension one\[23\]\[24\].
{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: question; status: open; action: preserve-source-visible; reason: restates slc condition via du Val singularities and quasi-étale quotient; target note records slc as a proof obligation in the stable-pair checklist; locator: Turn 5 Section II SLC item <<}

**Resolution and Contraction:** On the minimal resolution S, the exceptional anti-bicanonical (−4)\-curve C is **contracted** in the KSBA model back to the 41​(1,1) point\[19\]\[25\].
{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces#Stable-pair package]]; unit: question; status: open; action: preserve-source-visible; reason: restates anti-bicanonical (−4)-curve contraction to 1/4(1,1) point; target note's Stable-pair package tracks this as something to prove between resolution and stable model; locator: Turn 5 Section II Resolution item <<}

### III. Baily–Borel and Semifan Construction

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates Coble cusp classification as Γ_En,2-orbits of pairs (I,r) and (J,r) with I,J isotropic in T_En; already routed in Turn 1 item 5; locator: Turn 5 Section III Cusp Classification <<}

**Cusp Classification:** Baily–Borel 0-cusps and 1-cusps of FCo,2​ are ΓEn,2​\-orbits of pairs (I,r) and (J,r), where I and J are primitive isotropic subspaces of TEn​ and r is a perpendicular Coble root\[26\]\[27\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: fact; status: duplicate; action: preserve-source-visible; reason: restates mapping to Sterk's five 0-cusps and nine 1-cusps with I⊂J incidence; already routed in Turn 1 item 5; locator: Turn 5 Section III Reduction to Sterk <<}

**Reduction to Sterk:** These cusps map to Sterk's five 0-cusps and nine 1-cusps of the Enriques space; incidence is defined by I⊂J while maintaining the same root r\[28\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates admissibility criterion for roots in cusp lattices lifting to primitive (−2)-roots in designated Coble orbit; already routed in Turn 1 item 5; locator: Turn 5 Section III Admissibility Criterion <<}

**Admissibility Criterion:** A root in a cusp lattice is admissible if it lifts to a primitive (−2)\-root in TEn​ belonging to the designated Coble orbit, a condition verified via folded K3-to-Enriques Coxeter data\[32\].

{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: construction; status: duplicate; action: preserve-source-visible; reason: restates trace construction defining Coble semifan F_{k,r}^{Co} as trace of Enriques ramification semifan onto M_{k,r} = r^⊥ ∩ M_k; already routed in Turn 1 item 6; locator: Turn 5 Section III Trace Semifan Rule <<}

**Trace Semifan Rule:** The Coble semifan Fk,rCo​ is the **trace** of the Enriques ramification semifan onto the hyperplane Mk,r​\=rMk​⊥​\[35\]\[36\].

{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: conjecture; status: duplicate; action: preserve-source-visible; reason: restates the conjectural relevance-inheritance criterion that a Coble wall is irrelevant iff every Enriques wall restricting to it is irrelevant; already routed in Turn 1 item 7 and preserved in a conjectural target note; locator: Turn 5 Section III Relevance Inheritance <<}

**Relevance Inheritance:** A wall in the Coble fan is irrelevant if and only if every Enriques wall restricting to it is irrelevant\[37\]\[38\].

{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Relevance after restriction]]; unit: definition; status: duplicate; action: preserve-source-visible; reason: restates Type II = maximal parabolic subdiagrams, Type III = rank-8 elliptic subdiagrams in 9-dim Coble space; already routed in Turn 1 item 7; locator: Turn 5 Section III Strata Definitions <<}

**Strata Definitions:** Type II boundary divisors correspond to rational isotropic rays (maximal parabolic subdiagrams), while Type III divisors correspond to **rank-8 elliptic subdiagrams** in the nine-dimensional Coble period space\[38\].

### IV. Comparison and Integral-Affine Structure

{>> route: [[05_Results/KSBA vs. semitoroidal comparison for polarized Coble moduli#Why this is a conjecture]]; unit: conjecture; status: duplicate; action: preserve-source-visible; reason: restates KSBA comparison theorem statement (normalization of KSBA closure ≅ semitoroidal compactification from trace semifans); already routed in Turn 2 item 4; locator: Turn 5 Section IV KSBA Comparison Theorem item <<}
**KSBA Comparison Theorem:** The normalization of the KSBA closure is isomorphic to the semitoroidal compactification defined by the trace semifans\[41\]\[42\].

{>> route: [[05_Results/KSBA vs. semitoroidal comparison for polarized Coble moduli#Why this is a conjecture]]; unit: question; status: duplicate; action: preserve-source-visible; reason: restates no-moduli-loss requirement (stable quotient remembers 1/4(1,1) point to prevent fan coarsening); already routed in Turn 2 item 4; locator: Turn 5 Section IV No-Moduli-Loss item <<}
**No-Moduli-Loss Mechanism:** The proof requires that the stable quotient "remembers" the marked Coble root (the 41​(1,1) point), which prevents a strict coarsening of the trace fan\[43\].

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Upstairs-before-downstairs principle]]; unit: construction; status: duplicate; action: preserve-source-visible; reason: restates IAS zero-length-root construction in K3 IAS with Enriques symmetry, representing A1-node fixed by involution; already routed in Turn 1 item 8; locator: Turn 5 Section IV IAS item <<}
**Integral-Affine Structure (IAS):** The Coble IAS is constructed by marking a **zero-length root** in a K3 IAS that admits Enriques symmetry, representing the A1​\-node fixed by the involution\[46\].

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Upstairs-before-downstairs principle]]; unit: construction; status: duplicate; action: preserve-source-visible; reason: restates geometric chain K3→Enriques→Coble marked-root trace data; already routed in Turn 1 item 8; locator: Turn 5 Section IV Geometric Sequence item <<}
**Geometric Sequence:** The construction follows a formal sequence from K3 Coxeter/IAS data to folded Enriques data, and finally to Coble marked-root trace data\[49\]\[50\].

> **来源：**
> [1] KSBA Compactification and Coble.md
> [2] KSBA Compactification and Coble.md
> [3] KSBA Compactification and Coble.md
> [4] KSBA Compactification and Coble.md
> [7] KSBA Compactification and Coble.md
> [8] KSBA Compactification and Coble.md
> [9] KSBA Compactification and Coble.md
> [12] KSBA Compactification and Coble.md
> [13] KSBA Compactification and Coble.md
> [14] KSBA Compactification and Coble.md
> [17] KSBA Compactification and Coble.md
> [19] KSBA Compactification and Coble.md
> [20] KSBA Compactification and Coble.md
> [23] KSBA Compactification and Coble.md
> [24] KSBA Compactification and Coble.md
> [25] KSBA Compactification and Coble.md
> [26] KSBA Compactification and Coble.md
> [27] KSBA Compactification and Coble.md
> [28] KSBA Compactification and Coble.md
> [32] KSBA Compactification and Coble.md
> [35] KSBA Compactification and Coble.md
> [36] KSBA Compactification and Coble.md
> [37] KSBA Compactification and Coble.md
> [38] KSBA Compactification and Coble.md
> [41] KSBA Compactification and Coble.md
> [42] KSBA Compactification and Coble.md
> [43] KSBA Compactification and Coble.md
> [46] KSBA Compactification and Coble.md
> [49] KSBA Compactification and Coble.md
> [50] KSBA Compactification and Coble.md



### 🧑 **用户**

Doesn't that report have completely made-up results

### 🤖 **助手**

The conversation history confirms that several earlier claims and tables were indeed **unverified** or **insufficiently proven**, a point the model eventually conceded. If the report includes specific numerical tables for cusp counts or incidence diagrams, those are part of what the model explicitly **discarded** and identified as "unproved"\[1\]\[2\].

The sources show a progression where the initial "research program" provided unverified data, which was then systematically deconstructed and replaced by a **rigorous theoretical framework**. The "results" that remain valid in the final narrative are not the numerical counts, but the **mathematical mechanisms** and **claims** required for the proof:


{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Discarded numerical attempts]]; unit: remark; status: source-backed; action: merge; reason: model confirms earlier cusp tables and incidence diagrams were based on insufficient discriminant-form arguments and explicitly discarded as unproved; locator: Turn 6 intro <<}

**Retraction of Numerical "Facts":** The model admitted that the earlier numerical cusp tables and the incidence diagram were based on insufficient discriminant-form arguments and should be discarded\[1\]\[2\]. It clarified that these counts must be the output of an **explicit lattice-orbit computation** using the period-domain package, not a-priori assumptions\[3\].
{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Discarded numerical attempts]]; unit: remark; status: source-backed; action: merge; reason: model admitted cusp tables and incidence diagram based on insufficient discriminant-form arguments, explicitly discarded; per-item split; locator: Turn 6 bullet 1 <<}

**Correction of the Coble Root Uniqueness:** The model initially "hand-waved" the uniqueness of the Coble root orbit under ΓEn,2​ by misapplying a result from Namikawa that only applies to the full Enriques group ΓEn​\[6\]\[7\]. The final narrative corrects this by defining the moduli space **branchwise** until uniqueness is formally proven via a double-coset computation or geometric transitivity argument\[8\]\[9\].
{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#How uniqueness could still be proved]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates Gamma_En,2 orbit-uniqueness gap and double-coset/transitivity routes; already routed from Turn 1 item 1; per-item split; locator: Turn 6 bullet 2 <<}

**The "Trace Fan" Identity:** The report’s claim that the Coble fan is the **trace** of the Enriques fan on a hyperplane is the established mechanism, but the model notes that the specific Coxeter diagrams resulting from this trace are **theorems to be proven** by computation, not inputs to the setup\[10\]\[11\].
{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Proof obligations]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates that Coxeter diagrams from trace are theorems to be proven, not inputs; already routed from Turn 2 item 3; per-item split; locator: Turn 6 bullet 3 <<}

**Stability and Singularity Proofs:** Unlike the initial "made-up" version, the final narrative provides rigorous checks for **KSBA stability**, proving that the ramification divisor RSˉ​ is Q\-Cartier and ample, and that the quotient pairs are semi-log-canonical (slc)\[12\].
{>> route: [[03_Compactifications/KSBA model for polarized Coble surfaces]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates that KSBA stability proofs (R_S̄ Q-Cartier and ample, pairs slc) are rigorous in final narrative; already routed from Turn 1 item 4; per-item split; locator: Turn 6 bullet 4 <<}

**Cusp Reduction to Sterk:** The model replaced the "made-up" counts with a rigorous **reduction mechanism**, where Coble cusps are defined as orbits of pairs (I,r) mapping to Sterk’s established five 0-cusps and nine 1-cusps\[4\].
{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: remark; status: duplicate; action: preserve-source-visible; reason: restates Coble cusps defined as orbits of pairs (I,r) mapping to Sterk; already routed from Turn 1 item 5; per-item split; locator: Turn 6 bullet 5 <<}

In summary, while the _framework_ for the proof is rigorously grounded in the sources, any **specific numerical results** (like cusp counts or the incidence table) should be viewed with skepticism, as the model itself identified them as "unproved" and "insufficient"\[1\]\[2\]. The final narrative provides the **recipe** for the proof, but the final numerical "deliverables" are still pending explicit computation\[21\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Discarded numerical attempts]]; unit: remark; status: source-backed; action: merge; reason: model concludes that only the framework is rigorous; specific numerical results (cusp counts, incidence tables) remain pending explicit lattice-orbit computation and should be viewed with skepticism; locator: Turn 6 summary <<}

> **来源：**
> [1] KSBA Compactification and Coble.md
> [2] KSBA Compactification and Coble.md
> [3] KSBA Compactification and Coble.md
> [4] KSBA Compactification and Coble.md
> [6] KSBA Compactification and Coble.md
> [7] KSBA Compactification and Coble.md
> [8] KSBA Compactification and Coble.md
> [9] KSBA Compactification and Coble.md
> [10] KSBA Compactification and Coble.md
> [11] KSBA Compactification and Coble.md
> [12] KSBA Compactification and Coble.md
> [21] KSBA Compactification and Coble.md

### 🧑 **用户**

So what are the remaining things to rigorously prove and verify?

### 🤖 **助手**

Based on the dialogue and proof sketch provided in the source, the following points are the critical mathematical gaps and tasks that remain to be rigorously proven or verified to complete the construction of the **KSBA compactification of the polarized Coble moduli space** FCo,2​:

### 1\. Irreducibility and Root-Orbit Uniqueness

While Namikawa’s result establishes a unique (−2)\-vector orbit for the unpolarized Enriques group ΓEn​, it does not automatically apply to the degree-two polarized subgroup ΓEn,2​\[1\]\[2\].

**Double-Coset Computation:** A formal computation of the double coset ΓEn,2​\\ΓEn​/StabΓEn​​(Zδ) is required to determine if the polarized Coble divisor is irreducible or consists of multiple branches\[2\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#How uniqueness could still be proved]]; unit: question; status: open; action: merge; reason: formal Γ_En,2\\Γ_En/Stab_Γ_En(Zδ) double-coset computation needed to determine whether polarized Coble divisor is irreducible or splits into multiple branches; one of two alternative routes recorded in vault note; locator: Turn 7 item 1 sub-item 1 <<}

**Geometric Transitivity:** Alternatively, a geometric argument must prove the D4​\-action transitively permutes the four torus fixed-point hyperplanes in the Horikawa model to ensure orbit uniqueness\[5\]\[6\].

{>> route: [[02_Moduli/Arithmetic-group issues in polarized Coble moduli#How uniqueness could still be proved]]; unit: question; status: open; action: merge; reason: D_4-action transitive permutation of four torus fixed-point hyperplanes in Horikawa model; second alternative route for root-orbit uniqueness under Γ_En,2; locator: Turn 7 item 1 sub-item 2 <<}
### 2\. Numerical Cusp and Incidence Verification

The earlier "numerical tables" were discarded as unproven\[7\]. Rigorous classification requires more than discriminant-form (AT​) analysis\[8\]\[9\].

**Explicit Lattice Enumeration:** One must use the period-domain package or Sterk’s existing lattice-orbit arguments to enumerate the actual orbits of pairs (I,r) and (J,r) under ΓEn,2​\[8\].

**Incidence Proof:** The incidence table mapping 0-cusps to 1-cusps must be verified by checking the containment Ik​⊂Jc​ while ensuring the marked Coble root r remains admissible\[11\].

{>> route: [[03_Compactifications/Cusp data for polarized Coble moduli#Reduction to Sterk]]; unit: question; status: open; action: merge; reason: explicit requirement for lattice-orbit enumeration or period-domain package computation rather than discriminant-form shortcuts; aligned with vault note's correction that full cusp incidence requires explicit orbit work; locator: Turn 7 item 2 <<}

### 3\. The "Trace Fan" Identity and Admissibility

It is a claim, rather than a proven fact, that the Coble semifan is simply the trace of the Enriques fan\[12\].

**Arrangement Analysis:** It must be proven that no "extra roots" appear in the hyperplane section Mk,r​ that do not originate from Enriques ramification walls, and that Enriques walls do not restrict or coincide in ways that alter the expected Coxeter structure\[12\]\[13\].

**Admissibility Definition:** The "admissibility" of roots in the cusp lattices must be explicitly defined and verified against the folded K3-to-Enriques Coxeter data\[7\].

{>> route: [[03_Compactifications/Restriction of the ramification semifan to polarized Coble moduli#Proof obligations]]; unit: question; status: open; action: merge; reason: restates requirements to prove no extra roots appear and no Enriques walls restrict/coincide incorrectly; admissibility sub-item points to [[03_Compactifications/Admissibility issues for polarized Coble cusps]]; locator: Turn 7 item 3 <<}

### 4\. KSBA Stability and Comparison "Hard Points"

The comparison between the KSBA closure and the semitoroidal compactification relies on several unexecuted "hard points"\[16\]:

**No-Moduli-Loss Argument:** A formal proof is needed to show the stable quotient "remembers" the marked Coble root (the 41​(1,1)\-point). This is essential to prevent a "strict coarsening" of the fan, which would invalidate the isomorphism\[17\].

**Stable Limit Extension:** The extension of the Enriques involution over the stable limits of the K3 pair family must be rigorously demonstrated\[20\].

**Singularity and Ampleness Checks:** While the sketch provides a narrative for semi-log-canonicity (slc) and the ampleness of RSˉ​, these must be formally verified for the specific singularities of the Coble quotient\[23\].

{>> route: [[05_Results/KSBA vs. semitoroidal comparison for polarized Coble moduli#Why this is a conjecture]]; unit: question; status: open; action: merge; reason: enumerates no-moduli-loss, stable-limit extension, and singularity/ampleness as unexecuted hard points for the KSBA comparison theorem; aligned with vault note's dependency list; locator: Turn 7 item 4 <<}

### 5\. Integral-Affine Structure (IAS) Grounding

**Upstairs Relationship:** The link between the abstract period-theoretic Coxeter diagrams and the actual integral-affine spheres remains delicate. The construction must be grounded in "upstairs" K3 data, assigning length parameters ℓi​ to K3 Coxeter roots and imposing the Coble condition as a zero-length constraint (λ⋅r\=0)\[27\].

**Triangulation Compatibility:** One must prove the existence of an equivariant triangulation of the IAS that is compatible with the marked Coble root\[29\]\[31\].

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Upstairs-before-downstairs principle]]; unit: question; status: open; action: merge; reason: restates the upstream-K3 IAS grounding requirement and zero-length constraint λ·r=0; aligned with vault note's construction principle; locator: Turn 7 item 5 <<}

> **来源：**
> [1] KSBA Compactification and Coble.md
> [2] KSBA Compactification and Coble.md
> [5] KSBA Compactification and Coble.md
> [6] KSBA Compactification and Coble.md
> [7] KSBA Compactification and Coble.md
> [8] KSBA Compactification and Coble.md
> [9] KSBA Compactification and Coble.md
> [11] KSBA Compactification and Coble.md
> [12] KSBA Compactification and Coble.md
> [13] KSBA Compactification and Coble.md
> [16] KSBA Compactification and Coble.md
> [17] KSBA Compactification and Coble.md
> [20] KSBA Compactification and Coble.md
> [23] KSBA Compactification and Coble.md
> [27] KSBA Compactification and Coble.md
> [29] KSBA Compactification and Coble.md
> [31] KSBA Compactification and Coble.md

### 🧑 **用户**

...what? "Triangulation compatibility" was never identified as a gap, nor is it even mentioned or discussed in any original surfaces.

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Compatibility question]]; unit: remark; status: disputed; action: needs-human; reason: the user challenges "triangulation compatibility" as a never-identified gap; model defends it from source text quoting IAS requirement; this Turn exposes a potential model confabulation where a source statement about requirements was inflated into a standalone proof obligation; preserves provenance about synthetic gap inference; locator: Turn 8 <<}

### 🤖 **助手**

While it is true that you did not explicitly label **"triangulation compatibility"** as a gap in your critiques, the concept is explicitly mentioned in the sources as a requirement for the integral-affine (IAS) construction. It was included in the previous list of items to verify because the source presents it as a necessary step in the "integral-affine construction"\[1\],\[2\].

The sources discuss this topic in the following ways:

**Requirement for Construction:** Source\[1\] states that in the affine model, once the vanishing cycle or root δ is marked in the K3 affine sphere, one **"requires the triangulation to be equivariant for both involutions and compatible with this marked root."**\[1\].

**Step in the Construction:** In the formal construction steps for the Coble IAS, Step 4 specifically instructs to **"Choose an equivariant triangulation containing the Coble mark"**\[2\].

In the previous turn, "triangulation compatibility" was identified as a remaining thing to verify for the following reasons grounded in the conversation history:

**Challenge to the IAS Story:** You previously noted that the "IAS story" was "unclear" and questioned how the abstract Coxeter diagrams related to the actual IAS construction\[3\].

**Inference of a Proof Obligation:** Since Source\[1\] and\[2\] present the existence of such a triangulation as a "requirement" for the construction, proving that such a triangulation exists (and is compatible with the marked Coble root) becomes a **mathematical "hard point"** that must be satisfied to complete the research program\[1\]\[2\].

Outside of these sources, in the context of integral affine geometry, the existence of a triangulation that is both equivariant under a group action and compatible with a specific sub-configuration (like a marked root or wall) is typically a non-trivial combinatorial check. Therefore, within the framework of refining a "papered over" research program into a rigorous proof, this requirement from the sources was categorized as an item needing formal verification.

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Compatibility question]]; unit: construction; status: source-backed; action: merge; reason: the model correctly quotes source text that IAS Construction Step 4 requires an "equivariant triangulation containing the Coble mark" and that the triangulation must be compatible with the marked root; these are source-backed construction requirements from KSBA Compactification and Coble.md, not model fabrications; locator: Turn 8 source quotes <<}

{>> route: [[04_Degenerations/Marked-root integral-affine structures for Coble surfaces#Compatibility question]]; unit: remark; status: disputed; action: needs-human; reason: the model infers that the triangulation construction requirement constitutes an open proof obligation (a hard point) requiring formal verification; the user explicitly rejects this inference, stating triangulation compatibility was never identified as a gap; the exchange is preserved as provenance of a potential model confabulation where a construction step was inflated into a standalone proof obligation; locator: Turn 8 model inference <<}
> **来源：**
> [1] KSBA Compactification and Coble.md
> [2] KSBA Compactification and Coble.md
> [3] KSBA Compactification and Coble.md
