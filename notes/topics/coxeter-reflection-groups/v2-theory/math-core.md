<!--
Origin: gitclones/Coxeter-v2/docs/authority/MATH_CORE.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is RESEARCH PROSE from the Coxeter working trees: a mathematical
account written for this project. Errors the audit found in it are listed in
the README.md of this directory.
-->

# Math Core Authority Document

This document serves as the central technical authority for the mathematical foundations of the Coxeter maximal parabolic project. It contains literal extractions from the project's research archives and foundational documents, consolidated to ensure 1:1 parity and mathematical rigor.

## 1. Fundamental Definitions

### Gram Matrix ($G$)
The Gram matrix $G$ of a set of simple roots $\{\alpha_1, \dots, \alpha_n\}$ is the $n \times n$ symmetric matrix with entries:
$$G_{ij} = \langle \alpha_i, \alpha_j \rangle$$
- **Convention**: We use a negative diagonal convention where $G_{ii} = -2$ for simple roots.
- **Consequence**: This convention is a negative multiple ($-2$) of standard geometric literature, inverting common definiteness criteria.

### Coxeter Matrix ($M$)
For a Coxeter system, the Coxeter matrix $M$ has entries:
- $M_{ii} = 1$
- $M_{ij} = \text{order of } s_i s_j \text{ in the Coxeter group for } i \neq j$
- **Relationship to Gram Matrix**: $G_{ij} = -2 \cos(\pi/M_{ij})$ for $i \neq j$.

### Subdiagram
For a root lattice $L$ with distinguished root system $\Phi = \{\alpha_1, \dots, \alpha_n\}$, a subdiagram corresponding to $I \subseteq \{1, \dots, n\}$ is the induced subgraph on nodes in $I$. Its Gram matrix is the principal submatrix $G[I,I]$.

### Orthogonality Bifurcation
- **Left Orthogonal Complement**: $M^\perp = \{v \in V : \langle v, m \rangle = 0 \text{ for all } m \in M \}$.
- **Right Orthogonal Complement**: ${}^\perp M = \{v \in V : \langle m, v \rangle = 0 \text{ for all } m \in M \}$.
- **Symmetry**: In the symmetric-bilinear case (mandated), $M^\perp = {}^\perp M$.

This identity serves as a primary verification gate for implementation correctness.

### Terminology Distinction: Bilinear Form vs. Inner Product
- **Bilinear Form**: The general symmetric pairing $\langle v, w \rangle$. Does NOT require positive definiteness.
- **Inner Product**: A bilinear form that is **positive definite**. In our convention ($G_{ii}=-2$), an "inner product" correspond to a **negative definite** Gram matrix.

## 2. Classification Theory

Classifications are based on the definiteness properties of the **negative** Gram matrix $-G$.

| Type | Definition | Signature of $G$ | Geometric Action |
| :--- | :--- | :--- | :--- |
| **Elliptic (Finite)** | $-G$ is positive definite | $(0, n, 0)$ | Sphere |
| **Parabolic (Affine)** | $-G$ is positive semidefinite, $\text{rank} = n-1$ | $(0, n-1, 1)$ | Euclidean Space |
| **Hyperbolic** | $-G$ is indefinite, exactly one positive eigenvalue | $(1, n-1, 0)$ | Hyperbolic Space |
| **General Indefinite**| $-G$ has multiple positive eigenvalues | $(p, q, r), p \geq 2$| Infinite Covolume |

### Eigenvalue Monotonicity
- **Theorem**: If a Coxeter subdiagram is not elliptic, no superdiagram can be elliptic.
- **Proof**: Based on Cauchy's interlacing theorem; adding vertices can only make eigenvalues less negative.

### Signature Inheritance
- **Theorem**: Subdiagrams inherit definiteness properties with possible weakening: negative definite $\to$ negative semidefinite $\to$ indefinite.
- **Consequence**: Principal submatrices have signatures $(p', q', r')$ where $p' \leq p$ and $q' \leq q$.

## 3. Maximal Parabolic Subdiagrams

### Definition
A **maximal parabolic subdiagram** is a subdiagram that:
1. Is of parabolic type (signature $(0, |I|-1, 1)$).
2. Is not properly contained in any larger parabolic subdiagram.

### Poset-Theoretic Characterization
Maximal elements of the set:
$$\text{Max}(\{I \subseteq \{1, \dots, n\} : \text{subdiagram } I \text{ is parabolic}\})$$

### Geometric Significance (Vinberg's Theory)
- Each maximal parabolic subdiagram corresponds to a **cusp** at infinity.
- The number of cusps equals the number of maximal parabolic subdiagrams.

## 4. Hyperbolic Coxeter Groups

### Volume Finiteness (Vinberg)
A hyperbolic Coxeter group has finite covolume if and only if all maximal parabolic subdiagrams are affine (not hyperbolic).
- **Compact (Lannér)**: No parabolic subdiagrams exist.
- **Finite volume, non-compact**: All maximal parabolic subdiagrams are affine.
- **Infinite volume**: At least one maximal parabolic subdiagram is hyperbolic.

### Irreducible Affine Types
Canonical list of affine (parabolic) diagrams:
- $\tilde{A}_n (n \geq 1)$, $\tilde{B}_n (n \geq 3)$, $\tilde{C}_n (n \geq 2)$, $\tilde{D}_n (n \geq 4)$
- $\tilde{E}_6, \tilde{E}_7, \tilde{E}_8, \tilde{F}_4, \tilde{G}_2$

### Lattice Invariants
The core mathematical properties of integral lattices are:
- **Even/Odd**: A lattice is even if $\langle v, v \rangle \in 2\mathbb{Z}$ for all $v \in L$.
- **Unimodular**: A lattice is unimodular if $|\text{det}(G)| = 1$.
- **Level**: The smallest $N$ such that $N G^{-1}$ is integral and even.
- **Genus**: The set of lattices locally isomorphic to $L$ at every prime $p$ and over $\mathbb{R}$.
- **Minimum**: The smallest value of $\langle v, v \rangle$ for non-zero $v \in L$.

## 5. Field Theory & Exact Arithmetic

### Exact Arithmetic Mandate
- All computations must use **exact rings** ($\mathbb{Z}, \mathbb{Q}, \text{algebraic number fields}$).
- **Forbidden**: Floating-point approximations and epsilon-based comparisons.

### Field Preference (AA vs Qbar)
- **Algebraic Real Field (AA)**: Preferred for all geometric realizations to ensure exact comparison and eigenvalue computation.
- **Algebraic Field (QQbar)**: Secondary, used for cyclotomic computations where complex embeddings are required.
- **Decision**: Default to `AA` for root system construction to avoid precision degradation.

### Non-Crystallographic Types
Require field extensions to handle $\cos(\pi/5)$ and similar values:
- **$H_3$**: $\mathbb{Z}[\phi]$ where $\phi^2 - \phi - 1 = 0$ (golden ratio).
- **$H_4$**: $\mathbb{Z}[\tau]$ where $\tau^2 - \tau - 1 = 0$ ($\tau = 2\cos(\pi/5)$).
- **$I_2(p)$**: $\mathbb{Z}[2\cos(\pi/p)] \subseteq$ cyclotomic fields.

### Galois Invariance
- Eigenvalues come in conjugate sets; signature is preserved under Galois actions.

### LaTeX String Construction
Lattices may be constructed from LaTeX-style Dynkin labels or matrix strings to facilitate direct literature-to-code translation.

## 6. Matrix Distinction

### Gram ($G$) vs. Cartan ($A$)
- **Gram Matrix $G$**: Encodes inner products/metric structure. Always symmetric. $G_{ii} = -2$.
- **Cartan Matrix $A$**: Encodes reflection data. Can be non-symmetric. $A_{ii} = 2$.
- **Relationship**: $A = -G$ for simply-laced types (ADE). 

### Integral Scaling (BCFG)
To ensure integral Gram matrices for non-simply laced types, use the following scaling logic:
- **Type $B_n/C_n$**: Scale dual roots by 2.
- **Type $F_4$**: Scale short roots by 2.
- **Type $G_2$**: Scale short roots by 3.

### Fundamental Weights
Fundamental weights $\{\omega_i\}$ are the dual basis to simple roots $\{\alpha_i\}$ satisfying $\langle \alpha_i, \omega_j \rangle = \delta_{ij}$.
- **Computational Logic**: Fundamental weights are the rows of the inverse Gram matrix $G^{-1}$.
- **Node**: Fundamental Weights as rows of $G^{-1} \to$ src/coxeter/root_system.py

## 7. Implementation Requirements

### Rigor & Verification
1. **Definiteness-Based Methods**: Always use `-G.is_positive_definite()` or `-G.is_positive_semidefinite()` for classification.
2. **Poset-Based Maximality**: Test maximality by examining the entire poset of parabolic subdiagrams, not just single-vertex extensions.
3. **Symbolic Basis**: Use symbolic basis access ($L.e, L.f$) and natural notation ($v * w$ for evaluation).
