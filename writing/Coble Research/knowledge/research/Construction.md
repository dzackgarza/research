---
title: Construction of Coble Surfaces
tags:
  - mathematics/algebraic-geometry
  - surface/coble
  - surface/k3
created: 2026-05-10
---

# Construction of Coble Surfaces

Let $C \subset \mathbb{P}^2$ be an irreducible plane sextic with ten ordinary nodes $p_1, \dots, p_{10}$ and no other singularities.
Let
$$
S = \operatorname{Bl}_{p_1, \dots, p_{10}} \mathbb{P}^2,
$$
and denote by $H$ the pullback of a line and by $E_i$ the exceptional curves.
Then
$$
\operatorname{Pic}(S) = \mathbb{Z}H \oplus \bigoplus_{i=1}^{10} \mathbb{Z}E_i,
$$
with
$$
H^2=1, \qquad E_i^2=-1, \qquad H \cdot E_i = 0, \qquad E_i \cdot E_j = 0 \quad (i \neq j).
$$
Thus
$$
\operatorname{Pic}(S) \cong I_{1,10}.
$$

Let $B \subset S$ be the strict transform of $C$.
Since $C$ has degree 6 and multiplicity 2 at each node,
$$
B \sim 6H - 2\sum_{i=1}^{10} E_i.
$$
Also
$$
K_S = -3H + \sum_{i=1}^{10} E_i,
$$
so
$$
B \sim -2K_S.
$$

Let
$$
f: X \to S
$$
be the double cover branched along $B$.
Equivalently, it is determined by
$$
L = \mathcal{O}_S(-K_S), \qquad B \in |2L|.
$$
The curve $B$ is smooth, since the blow-up resolves the nodes of $C$.
Therefore $X$ is smooth.
The canonical bundle formula for a double cover gives
$$
K_X = f^*(K_S + L) = f^*(K_S - K_S) = 0.
$$
Moreover,
$$
f_* \mathcal{O}_X \simeq \mathcal{O}_S \oplus L^{-1} = \mathcal{O}_S \oplus \mathcal{O}_S(K_S).
$$
Since $f$ is finite,
$$
H^1(X, \mathcal{O}_X) \simeq H^1(S, \mathcal{O}_S) \oplus H^1(S, \mathcal{O}_S(K_S)).
$$
The surface $S$ is rational, so $H^1(S, \mathcal{O}_S) = 0$.
By Serre duality,
$$
H^1(S, \mathcal{O}_S(K_S)) \simeq H^1(S, \mathcal{O}_S)^\vee = 0.
$$
Hence
$$
K_X = 0, \qquad H^1(X, \mathcal{O}_X) = 0,
$$
so $X$ is a K3 surface.

## Induced Lattice

The pullback
$$
f^*: \operatorname{Pic}(S) \to \operatorname{Pic}(X)
$$
is injective: if $f^*D = 0$, then $2D = f_* f^* D = 0$, and $\operatorname{Pic}(S)$ is torsion-free.
For $D, D' \in \operatorname{Pic}(S)$, the projection formula gives
$$
(f^*D \cdot f^*D') = D \cdot f_* f^* D' = D \cdot 2D' = 2(D \cdot D').
$$
Therefore
$$
M_{\mathrm{Co}} := f^* \operatorname{Pic}(S) = \langle f^*H, f^*E_1, \dots, f^*E_{10} \rangle \subset \operatorname{Pic}(X)
$$
has Gram matrix $\operatorname{diag}(2, -2, \dots, -2)$.
Thus
$$
M_{\mathrm{Co}} \cong \langle 2 \rangle \oplus \langle -2 \rangle^{\oplus 10} = I_{1,10}(2).
$$

The embedding is primitive.
Let $\iota$ be the covering involution.
The lattice $M_{\mathrm{Co}}$ lies in $H^2(X, \mathbb{Z})^\iota$.
The fixed locus of $\iota$ is the ramification curve $R \cong B \cong \mathbb{P}^1$.
The topological Lefschetz formula gives
$$
2 + \operatorname{tr}(\iota^* | H^2(X, \mathbb{Z})) = \chi(R) = 2,
$$
so the trace on $H^2$ is 0. Since $H^2(X, \mathbb{Z})$ has rank 22, the invariant lattice has rank 11. Hence $M_{\mathrm{Co}}$ has finite index in $H^2(X, \mathbb{Z})^\iota$.

By Nikulin's fixed-locus formula for non-symplectic involutions on K3 surfaces, a fixed locus consisting of one rational curve has invariant-lattice invariants
$$
(r, a, \delta) = (11, 11, 1).
$$
Thus
$$
|\det H^2(X, \mathbb{Z})^\iota| = 2^{11}.
$$
But $|\det M_{\mathrm{Co}}| = 2^{11}$.
Since $M_{\mathrm{Co}} \subset H^2(X, \mathbb{Z})^\iota$ has the same rank and determinant, it equals the invariant lattice and is primitive.

## Transcendental Lattice

Now define
$$
T_{\mathrm{Co}} := M_{\mathrm{Co}}^\perp \subset \Lambda_{K3}, \qquad \Lambda_{K3} \cong U^{\oplus 3} \oplus E_8^{\oplus 2},
$$
where $E_8$ is negative definite.
Since $M_{\mathrm{Co}}$ has signature $(1, 10)$, the complement has signature
$$
(3, 19) - (1, 10) = (2, 9).
$$
Because $\Lambda_{K3}$ is unimodular and $M_{\mathrm{Co}}$ is primitive,
$$
A_{T_{\mathrm{Co}}} \cong A_{M_{\mathrm{Co}}}, \qquad q_{T_{\mathrm{Co}}} \cong -q_{M_{\mathrm{Co}}}.
$$
Now $M_{\mathrm{Co}} \cong \langle 2 \rangle \oplus \langle -2 \rangle^{10}$, so $A_{M_{\mathrm{Co}}} \cong (\mathbb{Z}/2)^{11}$, with discriminant form
$$
q_{M_{\mathrm{Co}}} \cong \left\langle \frac{1}{2} \right\rangle \oplus \left\langle -\frac{1}{2} \right\rangle^{\oplus 10}.
$$
Therefore $T_{\mathrm{Co}}$ is an even 2-elementary lattice with
$$
\operatorname{sign}(T_{\mathrm{Co}}) = (2, 9), \qquad a(T_{\mathrm{Co}}) = 11, \qquad \delta(T_{\mathrm{Co}}) = 1.
$$
By Nikulin's classification of indefinite even 2-elementary lattices, these invariants determine the isometry class.
The lattice
$$
\langle 2 \rangle \oplus U(2) \oplus E_8(2)
$$
has signature $(2, 9)$, discriminant group $(\mathbb{Z}/2)^{11}$, and $\delta = 1$.
Hence
$$
T_{\mathrm{Co}} \cong \langle 2 \rangle \oplus U(2) \oplus E_8(2).
$$
Equivalently, with $E_{10} := U \oplus E_8$, one gets
$$
T_{\mathrm{Co}} \cong \langle 2 \rangle \oplus E_{10}(2).
$$
