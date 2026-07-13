---
title: "Technical Roadmap: Mathematical Gaps in Coble Moduli"
tags:
  - project/roadmap
  - mathematics/gaps
created: 2026-05-10
---

# Technical Roadmap: Mathematical Gaps in Coble Moduli

This document identifies the non-trivial architectural and technical gaps in the current draft of "Complete Moduli Spaces of Coble Surfaces," providing a roadmap for parity with the rigor of `AEGS23` (Garza et al., 2023).

## 1. Lattice-Theoretic Induction of Coxeter Folding

While diagrammatic folding is used to identify cusp correspondences, the paper lacks the formal bridge from lattice theory to the $(9,9,1)_1$ Coxeter diagram:
- **Nikulin Foundations**: One must apply **Nikulin (1979) Prop 1.14.4 and 1.15.2** to rigorously verify the uniqueness of the primitive embedding $T_{Co} \hookrightarrow T_{En}$ and the surjectivity of the map $O(L) \to O(T_{Co})$.
- **Folding Involution**: Construct the explicit orthogonal involution $\theta$ on the K3 lattice $\Lambda$ (or the del Pezzo lattice $T_{dP}$) such that its fixed sublattice is isomorphic to $T_{Co}$.
  Show that the action of $\theta$ on the roots induces the **horizontal folding** of the $(18,0,0)_1$ diagram as a functorial consequence of the lattice isometry.

## 2. DLT Models for Coble Stable Pairs

`AEGS23` (Remark 8.16) modernizes Morrison’s (1981) "flowerpots" for Enriques surfaces, but the **Coble-specific dlt models** are not detailed in the current draft (Section 4.5 is empty):
- **Coble Pot Geometry**: Define the explicit **stable pair** $(\mathcal{V}, \mathcal{D})$ where the "Pot" component is a rational Coble surface.
  According to `AEGS23` (Line 543), these surfaces contain a **$1/4(1,1)$-singularity** corresponding to the nodes of the rational sextic $C$.
- **Stalk Assembly**: Describe the transition of the stalk assembly and the IAS configuration as the Enriques surface log-collapses onto the discriminant divisor $\Delta$, where the K3 cover becomes nodal.

## 3. Formal Derivation of Cusp Correspondence (Thm 5)

The correspondence between Coble cusps $(9,9,1)$ and $(7,7,1)$ and their Enriques predecessors must be proved using the **Hyperbolic Quotient method**:
- **Proof Strategy**: Supply the missing proof for Theorem 5 by explicitly computing the **isometry type of the hyperbolic quotient** $e^\perp / e$ for isotropic vectors $e \in T_{Co}$.
- **Lattice Invariants**: Use the **divisibility** $\text{div}*{T*{Co}}(e)$ to determine the unique $O(T_{Co})$-orbit and verify that the quotient lattice matches the Enriques $(10,8,0)_1$ (for 0-cusps) and $(8,6,0)_0$ (for 1-cusps) signatures.
  This establishes the correspondence beyond the "alignment of invariants" in the current text.
