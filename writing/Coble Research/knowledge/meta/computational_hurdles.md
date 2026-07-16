# Computational Lattice Hurdles: Coble Moduli Project

This document outlines the lattice-theoretic and computational verification tasks required to establish the moduli space of terminal Coble surfaces of K3 type.

## 1. Foundation: Coble Curves and Picard Lattices

### Background

A **Coble surface** $S$ is obtained via the blowup $\pi: S \to \mathbb{P}^2$ at the 10 $A_1$ nodes of an irreducible rational plane sextic $C = \{ F(x,y,z) = 0 \}$.
The polynomial $F$ is a homogeneous sextic of the form: $$F(x,y,z) = \sum_{i+j+k=6} a_{ijk} x^i y^j z^k$$ satisfying the **nodal conditions** $F(p_m) = \frac{\partial F}{\partial x}(p_m) = \frac{\partial F}{\partial y}(p_m) = \frac{\partial F}{\partial z}(p_m) = 0$ for 10 "special" point positions $p_1, \dots, p_{10} \in \mathbb{P}^2$.
The moduli space of such sextics is 9-dimensional.
Explicit equations can be derived from the **Steiner sextic** or configurations related to index-2 Halphen pencils.
2 The **K3 cover** $X \xrightarrow{2:1} S$ is the double cover of $\mathbb{P}^2$ branched along $C$, with equation $w^2 = F(x,y,z)$ in the weighted projective space $\mathbb{P}(1,1,1,3)$.
The singularities of $X$ consist of ten $A_1$ nodes lying directly above the nodal positions $p_m$.

The **Picard Groups** and their isometry classes are defined on the basis $\{e_0, e_1, \dots, e_{10}\}$ (where $e_0 = \pi^* L$ and $e_i = E_i$):
- **Coble Lattice**: $S_{\mathrm{Co}} \cong \langle 2 \rangle \oplus \langle -2 \rangle^{10} \cong (11, 11, 1)_1$.
  Signature $(1, 10)$.
- **Gram Matrix**: $Q_{S_{\mathrm{Co}}} = \text{diag}(2, -2, \dots, -2)$.
- **Transcendental Lattice**: $T_{\mathrm{Co}} = S_{\mathrm{Co}}^{\perp \Lambda_{\mathrm{K3}}} \cong (11, 11, 1)_2$.
  Signature $(2, 9)$.
- **Invariants**: Both satisfy $q_S \cong q_{T} \cong (\mathbb{Z}/2\mathbb{Z})^{11}$ with $q_S = -q_T \pmod{2\mathbb{Z}}$.
- **Ambient Lattices**: $T_{\mathrm{En}} \cong (12, 10, 0)_2$, $T_{\mathrm{dP}} \cong (20, 2, 0)_2$, and $\Lambda_{\mathrm{K3}} \cong (22, 0, 0)_1$.

### Technical Gap

While the invariants $(r, a, \delta)$ are listed, the **isometry class verification** and **genus decomposition** (e.g., verifying if the genus contains a unique class) are not formally established for $T_{\mathrm{Co}}$.
The explicit **equations for $C$ and $X$** given a configuration of 10 points, and the **primitivity of the lattice embeddings**, lack rigorous derivation in terms of coordinate bases.

### Computational Verification

- **Task 1.1**: Derive an explicit equation $F(x,y,z)=0$ for a rational sextic with 10 nodes and the corresponding K3 surface $w^2 = F(x,y,z)$.
- **Task 1.2**: Compute the Gram matrices for $S_{Co}$ and $T_{Co}$, and verify their $(r, a, \delta)$ invariants and **genus cardinality** using Nikulin's classification ($r > a$ check).
- **Task 1.3**: Derive the explicit primitive embedding matrices for $T_{\mathrm{Co}} \hookrightarrow T_{\mathrm{En}} \hookrightarrow T_{\mathrm{dP}} \hookrightarrow \Lambda_{\mathrm{K3}}$.

* * *

## 2. Isotropic Orbit Enumeration (Sterk's Technique)

### Background

The 0-cusp classification relies on the orbits of primitive isotropic vectors $v \in T_{\mathrm{Co}}$ under $O(T)$, $O^*(T)$, and the arithmetic group $\Gamma_{\mathrm{Co}}$.
**Sterk's Technique** (Sterk 1991) determines these orbits by analyzing the orbits of their images (lifts) in the **discriminant group** $A_T = T^*/T$ under $O(q_T)$.
For 2-elementary lattices with $r > a$, the genus contains a **unique isometry class**, and $O(T) \to O(q_T)$ is surjective (Nikulin 1.5.2).

### Technical Gap

The number of isotropic orbits in $A_{T_{\mathrm{Co}}} \cong (\mathbb{Z}/2\mathbb{Z})^{11}$ is not yet computed.
**Nikulin's classification** (Nikulin 1.5.2) implies that for a 2-elementary lattice $(r, a, \delta)$, any primitive isotropic vector $v$ with $\operatorname{div}(v)=d$ is uniquely determined up to $O(T)$ by the image $v/d + T \in A_T$.
One must formally verify the **lifting of isotropic orbits** from $A_T$ to $T_{\mathrm{Co}}$ using Sterk's lifting theorems.
One must also verify that $O(T)$ orbits coincide with $\Gamma_{\mathrm{Co}}$ orbits to ensure the BB 0-cusp is unique.

### Computational Verification

- **Task 2.1**: Enumerate isotropic vectors in $A_{T_{\mathrm{Co}}}$ and compute their orbits under $O(q_T)$.
- **Task 2.2**: Lift these orbits to $T_{\mathrm{Co}}$ and verify that exactly one $O^*(T)$-orbit exists for divisibility 2.

* * *

## 3. Uniqueness of 1-Cusps and $\Gamma_{\mathrm{Co}}$ Stabilizer

### Background

The arithmetic group $\Gamma_{\mathrm{Co}}$ is the **stabilizer of the polarization** $h_{Co}$ within $O(T_{En})$, further constrained by the horizontal folding involution $\theta$: $$\Gamma_{\mathrm{Co}} = \text{Stab}_{O(T_{En})}(h_{Co}) \cap Z_{O(T_{En})}(\theta)$$ In the Enriques sector, $h_{En} = e+f$ is the degree 2 polarization ($h^2=2$). The Coble polarization $h_{Co}$ is induced by the hyperplane class $E_0$.

### Technical Gap

An explicit representation of $\Gamma_{\mathrm{Co}}$ in terms of **matrix generators** is currently a stub.
Construction requires the centralizer/stabilizer intersection in the Enriques sector: $$\Gamma_{\mathrm{Co}} = \text{Stab}_{O(\Lambda)}(h_{Co}) \cap Z_{O(\Lambda)}(\theta)$$ where $h_{Co}^2=2$.
One must also verify the **uniqueness of the 1-cusp** by checking the negative-definite quotient $J^\perp/J$ for all orbits of isotropic primitive planes $J \subset T_{Co}$ and confirming isometry with $A_1^{\oplus 7}$.

### Computational Verification

- **Task 3.1**: Compute the stabilizer/centralizer intersection in the Enriques lattice to find a minimal set of generators for $\Gamma_{\mathrm{Co}}$.
- **Task 3.2**: Enumerate all $O(T_{\mathrm{Co}})$-orbits of isotropic planes $J$ and compute $J^\perp/J$.

* * *

## 4. Combinatorial Search for Coxeter Parabolics

### Background

The reflection group $W(S_{\mathrm{Co}})$ acts on the period domain.
The 0-cusp $(9,9,1)_1$ is described by a maximal parabolic subdiagram in the Coxeter diagram $G_{S_{\mathrm{Co}}}$.

### Technical Gap

The 10-node Coxeter diagram $G_{S_{\mathrm{Co}}}$ is highly connected.
Confirming that $\widetilde{B}_7(2)$ is the **only** maximal parabolic subdiagram is essential to the "one 0-cusp" claim.

### Computational Verification

- **Task 4.1**: Implement a subdiagram search on the $10 \times 10$ Gram matrix of roots to identify all possible maximal parabolic configurations.

* * *

## 5. Explicit Involution Matrix and Sublattice Invariants

### Background

The "horizontal folding" $\theta$ must act on $\Lambda_{\mathrm{K3}}$ such that its **invariant and coinvariant sublattices** are correctly identified: $\Lambda_{\mathrm{K3}}^\theta \cong T_{\mathrm{Co}}$ and $\Lambda_{\mathrm{K3}}^{-\theta} \cong S_{\mathrm{Co}}$.
This involution swaps the polarization generators between sectors ($h_{En} \leftrightarrow h_{Co}$).

### Technical Gap

The explicit matrix for $\theta$ on the standard basis of $U^3 \oplus E_8^2$ is missing.
One must verify the **isometry classes** of the $\pm 1$ eigenspaces via $(r, a, \delta)$ comparison to ensure $\Lambda_{K3}^+ \cong T_{Co}$ and $\Lambda_{K3}^- \cong S_{Co}$, and that the embedding $T_{Co} \hookrightarrow T_{En}$ is primitive.

### Computational Verification

- **Task 5.1**: Construct the $22 \times 22$ matrix $\theta$ and compute the signature and invariants of its fixed sublattice to confirm isometry (2-elementary check).

* * *

## 6. Monodromy Invariants and Stable Models $B(\lambda)$

### Background

Stable limits of Coble surfaces correspond to $S_2$-quotients of nodal K3 surfaces.
These models are parameterized by the monodromy invariant $\ell \in \check{\mathcal{H}}$ (surgery sizes) via the construction $B(\lambda)$ (AEGS23).

### Technical Gap

The stability of the slc pair $(Z, \epsilon C)$ for specific surgery vectors $\ell$ must be verified.
One must determine the mapping from the transcendental vector $h_{Co}$ to the discretization $\ell$ on the dual complex.

### Computational Verification

- **Task 6.1**: Map the Coble polarization $h_{Co}$ to the the surgery vector $\ell$ and verify the slc stability of the resulting stable limit.

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
- **Polarization Basis**: The degree-2 polarization $h$ in $T_{\mathrm{En}}$ corresponds to $h = e+f$ in a standard $U$-basis, which must be identified in a basis compatible with $\theta$.
- **Discriminant Forms**:
  - $q_{S_{\mathrm{Co}}}: (\mathbb{F}_2)^{11} \to \mathbb{Q}/2\mathbb{Z}$
  - $q_{T_{\mathrm{Co}}}: (\mathbb{F}_2)^{11} \to \mathbb{Q}/2\mathbb{Z}$
  - Isometry of complements implies $q_S = -q_T \pmod{2\mathbb{Z}}$.

### 8.3. Orbits and Stabilizers

- **Sterk Orbit Lift**: For the 2-elementary lattice $T$, the orbits are uniquely determined by the tuple $(\operatorname{div}(v), \bar{v} \in A_T, v^2=0)$.
  The search reduces to checking $\mathbb{F}_2$-vector space orbits under the orthogonal group of the quadratic form $q_T$.
- **$\Gamma_{\mathrm{Co}}$ Generators**: Computation involves finding the intersection of the group of reflections $W(T)$ with the centralizer $Z(\theta)$ and the stabilizer of the primitive vector $h$.
