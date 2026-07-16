---
exported: 2026-05-11T03:53:20.420Z
source: NotebookLM
type: report
title: "A Rigorous Analysis of the KSBA Compactification of the Coble Moduli Space $F_{Co,2}$"
---

# A Rigorous Analysis of the KSBA Compactification of the Coble Moduli Space $F_{Co,2}$

导出时间: 5/11/2026, 11:53:20 AM

* * *

# A Rigorous Analysis of the KSBA Compactification of the Coble Moduli Space FCo,2​

## 1. Mathematical Introduction and Strategic Context

The moduli space of degree-two Enriques surfaces, FEn,2​, admits a natural decomposition into Noether-Lefschetz subvarieties, the most significant of which is the **Coble locus**. Geometrically, this locus corresponds to rational surfaces—Coble surfaces—realized as quotients of nodal K3 surfaces by an Enriques involution that fixes the node.
Strategically, the study of the Coble locus requires a transition from the broad symmetry of the Enriques lattice to the refined arithmetic of a specific vanishing root.
This shift necessitates a rigorous lattice-theoretic foundation to account for the transition from smooth Enriques theory to the singular geometry of rational surfaces.

A critical differentiator in this analysis is the distinction between the unpolarized Coble space FCofull​\=D(TCo​)/O(TCo​) and the polarized moduli space FCo,2​. While the former is governed by the unscaled lattice I2,9​, the degree-two polarization h imposes significant arithmetic constraints on the stabilizer group ΓCo,2​. This group is defined as a subgroup of ΓEn,2​\=ΓEn​∩ΓdP​, ensuring that the polarization datum is preserved.
Consequently, FCo,2​ is not merely an open subset of the Enriques space but must be viewed as the normalization of the unique Heegner divisor branch within FEn,2​. This structural precision is required to accurately map the period domain to the geometric features of the Horikawa model.

## 2. Lattice-Theoretic Foundation of the Coble Period Space

The transcendental lattice of a degree-two Enriques surface is TEn​\=U⊕U(2)⊕E8​(−2). The Coble locus is defined by the condition that a primitive (−2)\-vector δ∈TEn​, referred to as the Coble root, becomes algebraic.
This algebraic root corresponds to the vanishing cycle of the A1​\-node on the covering K3 surface.

**Lemma 2.1 (The Coble Noether-Lefschetz Sublattice)***Let* δ∈TEn​ *be a primitive* (−2)*\-vector.
The Coble transcendental lattice* TCo,2​:=δTEn​⊥​ *is isomorphic to* ⟨2⟩⊕U(2)⊕E8​(−2)≅I2,9​(2)*.*

**Proof:** Choose a hyperbolic basis {e,f} for the U\-summand of TEn​ (where e2\=f2\=0 and e⋅f\=1). Setting the Coble root as δ\=e−f and the polarization as h\=e+f yields δ2\=−2 and h2\=2 with δ⊥h. The orthogonal complement δ⊥ within TEn​ decomposes as Zh⊕U(2)⊕E8​(−2). Since Zh≅⟨2⟩, the result follows, identifying TCo,2​ as the scaled odd unimodular lattice I2,9​(2).

**Theorem 2.2 (Equivariance of the Coble Period Map)***The inclusion* ιδ​:D(δ⊥)↪D(TEn​) *is equivariant with respect to the stabilizer* ΓCo,2​:=im(StabΓEn,2​​(Zδ)→O(δ⊥))*.*

**Proof:** For any g∈StabΓEn,2​​(Zδ), the isometry g preserves the hyperplane δ⊥. Thus, for any \[ω\]∈D(δ⊥), we have ιδ​(g⋅ω)\=g⋅ιδ​(ω). This equivariance ensures that the induced morphism of arithmetic quotients D(δ⊥)/ΓCo,2​→D(TEn​)/ΓEn,2​ is well-defined, mapping the Coble period space to the normalization of the Coble Heegner divisor.

**Claim 2.3 (Orbit Uniqueness and the Normalization Model)**While Namikawa’s result established a unique orbit of (−2)\-vectors in TEn​ modulo the full Enriques group ΓEn​, the polarized case requires a more nuanced treatment.
In FEn,2​, the irreducibility of the Coble divisor follows from the transitivity of the D4​ symmetry on the four torus fixed points in the branch-curve model.
Thus, FCo,2​ is realized as the normalization of this unique Heegner branch.
This geometric route bypasses the potential splitting of orbits under the finite-index subgroup ΓEn,2​.

These arithmetic structures directly inform the stability conditions required for the geometric branch-curve model.

## 3. The Geometric Model and KSBA Stability

The bridge between the period domain and the KSBA compactification is the stability of Coble pairs (Sˉ,ϵRSˉ​). Using the Horikawa model on Y\=P1×P1 with involution τ(x,y)\=(−x,−y), we consider invariant (4,4)\-curves B that pass through the τ\-fixed points.

**Lemma 3.1 (Local Singularity of the Coble Branch)***An invariant* (4,4)*\-curve* B *passing through a* τ_\-fixed point_ p *with a non-degenerate quadratic part* q2​ *induces an* A1​_\-singularity on the K3 double cover_ X_._

**Proof:** Let (u,v) be local coordinates at p where τ(u,v)\=(−u,−v). Since B is τ\-invariant, the local equation f contains no odd terms: f\=q2​(u,v)+q4​(u,v)+…. The condition f(p)\=0 with det(q2​)\=0 defines an ordinary node.
The double cover X\={z2\=f(u,v)} inherits this node as an A1​\-singularity, which is fixed by the Enriques lift ιEn​(u,v,z)\=(−u,−v,−z).

**Theorem 3.2 (Stability of Coble Pairs)***For* 0<ϵ≪1_, the pair_ (Sˉ,ϵRSˉ​) *is semi-log-canonical (slc) and* KSˉ​+ϵRSˉ​ *is ample.*

**Proof:** The K3 cover X has du Val singularities, which are canonical.
The quotient Sˉ\=X/ιEn​ possesses a cyclic quotient singularity of type 41​(1,1) at the fixed node.
The index-one cover of this singularity is the A1​\-node.
Consequently, the canonical divisor KSˉ​ is Q\-Cartier of index 2 at the node.
The ramification divisor RX​ is the pullback of an ample OY​(2,2) and is itself ample.
Since KX​∼0, KSˉ​+ϵRSˉ​ pulls back to ϵRX​. Ampleness is preserved under the finite surjective quotient.
The pair is slc by standard quotient criteria for canonical singularities.

### Comparison of Geometric and Stable Features

| Feature | Smooth Coble Resolution S | Stable KSBA Model Sˉ |
| --- | --- | --- |
| Singularity Type | Smooth | 41​(1,1) quotient singularity |
| Index-One Cover | N/A | A1​ (node) |
| Exceptional Locus | (−4)-curve C∈∣−2KS​∣ | Contracted to the 41​(1,1) point |
| Log Canonical Divisor | KS​+21+ϵ​C+ϵRS​ | KSˉ​+ϵRSˉ​ |
| Curvature | KS​ is not ample | KSˉ​+ϵRSˉ​ is ample (Q-Cartier index 2) |

## 4. Baily-Borel Boundary and Cusp Classification

The Baily-Borel compactification FCo,2BB​ is constructed from orbits of isotropic subspaces in TCo,2​ under the action of ΓCo,2​. Sterk’s classification of Enriques cusps provides the coordinate system for this boundary.

**Proposition 4.1 (Coble Cusp Correspondence)***0-cusps are* ΓCo,2​_\-orbits of pairs_ (I,r) *and 1-cusps are orbits of pairs* (J,r)*, where* I,J *are isotropic subspaces of* TEn​ *and* r∈RCo,2​_._

Coble 0-cusps map to Sterk Enriques cusps **2, 3, 4,** and **5**. Sterk Cusp **1** is excluded from the Coble boundary; it corresponds to divisibility-one isotropic vectors, whereas any primitive isotropic vector in the Coble lattice TCo,2​≅I2,9​(2) necessarily has divisibility two in the ambient TEn​. The 1-cusps are mapped based on the 0-cusps contained in their closure (e.g., Cusp 245 is the unique 1-cusp incident to 0-cusps 2, 4, and 5).

### Incidence Matrix of the Coble Baily-Borel Boundary

| Coble 0-Cusp (Sterk Label) | Incident Coble 1-Cusps |
| --- | --- |
| 2 | 245 |
| 3 | 34, 35 |
| 4 | 245, 34, 45 |
| 5 | 245, 35, 45, 55 |

## 5. The Coble Trace Fan and Semitoroidal Construction

The semitoroidal compactification is obtained by refining the Baily-Borel boundary using the "trace" of the Enriques ramification fans.

**Definition 5.1 (The Trace Semifan)***For a Coble 0-cusp* (ek​,r)*, the Coble semifan* Fk,rCo​ *is the trace of the Enriques ramification semifan* FkEn​ *onto the Coble positive cone* C(Mk,r​)*, defined by the condition that* relint(σ)∩C(Mk,r​)\=∅*.*

**Lemma 5.2 (Inheritance of Relevance)***A wall in* Fk,rCo​ *is irrelevant if and only if every Enriques wall that restricts to it is irrelevant in* FkEn​_._

In this construction, the **Vinberg algorithm** applied to Mk,r​ serves as a diagnostic tool.
The Coble Coxeter diagrams are the *outputs* of the trace computation rather than independent inputs.
This ensures the fans accurately reflect the symmetries inherited from the ambient K3 and Enriques structures.

## 6. The Main Theorem: KSBA-Semitoroidal Comparison

The central result of this program establishes that the geometric limits of stable pairs coincide with the arithmetic limits in the period domain.

**Theorem 6.1 (The Coble Comparison Theorem)***The normalization* (FCo,2KSBA​)ν *is isomorphic to the semitoroidal compactification* FCo,2FCo​​ *defined by the collection of trace semifans.*

**Proof Strategy:**

**Pullback of the universal K3 family:** We restrict the universal family of K3 stable pairs over the F(2,2,0) space to the Noether-Lefschetz locus D(r⊥).

**Extension of the Enriques involution:** By the uniqueness of KSBA limits, the Enriques involution extends over the boundary of the family, fixing the Coble root δ.

**Descent of the ramification divisor:** The invariant ramification divisor RX​ descends to RSˉ​, maintaining the slc and ampleness conditions.

**The "No-Moduli-Loss" argument:** Because the stable pair (Sˉ,ϵRSˉ​) remembers the 41​(1,1)\-singularity (or the anti-bicanonical (−4)\-curve), any further coarsening of the fan would identify geometrically distinct degenerations.
This "maximal-double-curve" argument ensures that the trace fan is the correct level of coarsening.

## 7. Integral-Affine Structures and Dual Complexes

Integral-Affine Structures (IAS) provide the dual complex visualization for the boundary degenerations.

**Construction 7.1 (The Marked IAS)**The Coble IAS is obtained by taking the Enriques affine sphere B(ℓ) and imposing the linear condition λ⋅r\=0 for the Coble root r. This corresponds to a zero-length condition on the vanishing cycle giving the A1​\-node.

The relationship between these structures is one of nested restrictions:

**K3 Coxeter Diagram:** Defines the ramification fan of the cover.

**Folded Enriques Diagram:** Represents the trace of the K3 fan under the Enriques involution.

**Coble Hyperplane Diagram:** Represents the final trace onto the r⊥ hyperplane.

## 8. Classification of Boundary Strata and ADE Dictionary

The boundary strata are identified using a dictionary that maps K3 ADE components to folded ABCDE quotient types.
Type II divisors correspond to **maximal parabolic** subdiagrams, while Type III divisors correspond to **rank 8 elliptic** subdiagrams.

### Classification of Coble Boundary Components

| Cusp Label | Subdiagram Type | K3 Cover ADE Type | Coble Quotient Type | Coble Mark Location |
| --- | --- | --- | --- | --- |
| Type II | Max. Parabolic (RDownload Image) | Affine An​,Dn​,En​ | Folded Bn​,Cn​,F4​,G2​ | Node on double curve |
| Type III | Rank 8 Elliptic (R) | Finite An​,Dn​,En​ | Folded Bn​,Cn​,F4​,G2​ | The 41​(1,1) point |
| Type III | Finite (R) | Rank < 8 | Sub-maximal quotients | Vanishing cycle of node |

This research program establishes the coherence of the KSBA compactification of FCo,2​. By anchoring geometric stability in the lattice-theoretic trace of Enriques ramification fans, we provide a complete framework for boundary classification.
The consistency between the branch-curve model and the semitoroidal compactification underscores the robustness of the KSBA program.
Final numerical completion of the subdiagram tables remains the objective of current finite lattice computations.
