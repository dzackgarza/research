# Mathematical Background for GOAL.md Tasks

Consolidated from prior proof-sketch files.
All "computational verification" claims from those files were invalidated during the
March 2026 audit (scripts were print-theater with zero or self-validating assertions).
This file preserves only the genuine mathematical content: theorem statements, standard
results, and literature pointers.

Every claim below traces to REFERENCES.md.
No claim here is a repo-original result.

* * *

## Task 1.1: Rational Sextic with 10 Nodes

**Arithmetic genus formula.** For a plane curve of degree d, g_a = (d-1)(d-2)/2. For d =
6: g_a = 10.

**Genus-delta relation.** The geometric genus satisfies g = g_a - sum(delta_p), where
delta_p is the delta-invariant at each singular point.
For an ordinary node (A_1), delta = 1. Ten nodes give g = 10 - 10 = 0, so C is rational.

**Birational criterion.** A parametrization P^1 -> C is birational iff the generic fiber
has degree 1 (compute via gcd of fiber equations in QQ(a)[u]).

**Configuration constraint (Pieroni 2026, lines 752-759).** For generic 10 points in
P^2, no nodal sextic exists: 10 nodes impose 30 linear conditions on the 28-dimensional
space H^0(O_{P^2}(6)). Explicit examples require special configurations where these
conditions become dependent.

Literature: Coble (1917, 1929), Dolgachev-Kondo (2013), Pieroni (2026).

* * *

## Task 1.2: Gram Matrices and Nikulin Invariants

**Coble lattice.** S_Co = <2> + <-2>^10, Gram matrix diag(2, -2, ..., -2), signature
(1,10), rank 11.

**Transcendental lattice.** T_Co has signature (2,9), rank 11, det = -2^11. Discriminant
groups: A_S = A_T = (Z/2Z)^11.

**Nikulin invariants.** (r, a, delta) = (11, 11, 1) for both S_Co and T_Co.

**Nikulin's classification (Nikulin 1979, Theorem 1.14.2).** A 2-elementary lattice of
given signature is determined up to isometry by (r, a, delta).
For r > a, the genus contains a unique isometry class.

**Discriminant form duality.** For a primitive sublattice S in a unimodular lattice
Lambda, the discriminant forms satisfy q_T = -q_S, verified via Brown invariant:
Brown(q_T) + Brown(q_S) = 0 (mod 8).

**Pieroni connection (lines 146, 483-493).** The lattice E_10 = k^perp in Z^{1,10} is
identified as Num(X) for Coble surfaces, matching S_Co structure.

Literature: Nikulin (1979), Dolgachev-Kondo (2013), Pieroni (2026).

* * *

## Task 1.3: Primitive Embedding Chain

**Embedding chain.** T_Co -> T_En -> T_dP -> Lambda_K3, where:
- Lambda_K3 = U^3 + E_8(-1)^2 (signature (3,19), rank 22, even unimodular)
- T_dP: del Pezzo transcendental lattice (rank 9)
- T_En: Enriques transcendental lattice (rank 10)
- T_Co: Coble transcendental lattice (rank 11, signature (2,9))

**Primitive embedding theorem (Nikulin 1979, Section 1.5).** For a 2-elementary lattice
L with (r, a, delta) = (11, 11, 1) and signature (1, 10), a primitive embedding L ->
Lambda_K3 exists and is unique up to O(Lambda_K3).

**Orthogonal complement.** For primitive S in unimodular Lambda:
- rank(T) = rank(Lambda) - rank(S)
- det(T) = det(S) (up to sign)
- q_T = -q_S

**Huybrechts connection (K3 Lectures, lines 561, 1589-1619).** Foundational K3 lattice
theory including U^3 + E_8(-1)^2 structure.

Literature: Nikulin (1979), Dolgachev-Kondo (2013), Huybrechts.

* * *

## Task 2.1: Isotropic Vector Orbits in A_{T_Co}

**Discriminant group.** A_{T_Co} = (Z/2Z)^11, order 2048. Quadratic form q_T: A_{T_Co}
-> Q/2Z induced by the lattice bilinear form.

**Isotropic vectors.** v in A_{T_Co} with q_T(v) = 0 (mod 2Z). Count: 528 total (1 zero
\+ 527 nonzero). This count follows from the theory of quadratic forms over F_2.

**Nikulin surjectivity (Prop.
1.5.2).** For a 2-elementary lattice T with r > a, the map O(T) -> O(q_T) is surjective.
For T_Co with (r, a, delta) = (11, 11, 1): all nonzero isotropic vectors form a single
O(q_T)-orbit.

**Geometric significance.** The orbit structure determines the cusp classification in
the Baily-Borel compactification.
Each O(q_T)-orbit of nonzero isotropic vectors corresponds to a cusp type (Sterk 1991).

Literature: Nikulin (1979, Prop.
1.5.2), Sterk (1991), Dolgachev-Kondo (2013).

* * *

## Task 2.2: Orbit Lifting

**Divisibility constraint.** For T_Co with Gram matrix diag(2, 2, -2, ..., -2), all
diagonal entries are even.
For any v in T_Co, the pairing v.e_i = +/-2v_i is always even, so div(v) = gcd({v.w : w
in T_Co}) is always even.
Hence div(v) = 2 for all primitive isotropic vectors (no div = 1 vectors exist).

**Orbit lifting.** From Task 2.1, the 527 nonzero isotropic vectors in A_{T_Co} form one
O(q_T)-orbit. By Nikulin surjectivity (r = a = 11), O(T_Co) -> O(q_T) is surjective, so
all div = 2 lifts form one O(T_Co)-orbit.

**Stable orbit uniqueness.** O*(T_Co) = ker(O(T_Co) -> O(q_T)) acts trivially on
A_{T_Co}. Since all div = 2 vectors map to the same O(q_T)-orbit, there is exactly one
O*(T_Co)-orbit for divisibility 2. This implies a unique cusp type (Sterk 1991).

Literature: Nikulin (1979, Prop.
1.5.2), Sterk (1991).

* * *

## Task 3.1: Arithmetic Group Gamma_Co

**Definition.** Gamma_Co = Stab_{O(T_En)}(h_Co) intersect Z_{O(T_En)}(theta), where T_En
has rank 10 and signature (2, 8), h_Co is the Coble polarization with h_Co^2 = 2, and
theta is the horizontal folding involution.

**Moduli interpretation.** The Coble moduli space is a quotient of the period domain by
Gamma_Co. The polarization h_Co corresponds to the ample divisor class on the Coble
surface, and theta encodes the Enriques involution structure.

**No explicit generators have been computed.** This remains an open computational task.

Literature: Sterk (1991), Dolgachev-Kondo (2013).

* * *

## Task 3.2: Isotropic Plane Uniqueness

**Isotropic planes.** A 2-dimensional subspace J in T_Co such that the bilinear form
restricts to zero on J. The Witt index of T_Co is min(2, 9) = 2, so maximal isotropic
subspaces have dimension 2.

**Quotient structure.** For a primitive isotropic plane J:
- J^perp has rank 11 - 2 = 9
- J^perp/J has rank 9 - 2 = 7
- J^perp/J inherits a nondegenerate negative-definite bilinear form

**Theoretical prediction.** From Nikulin surjectivity and 2-elementary lattice theory:
there should be exactly one O(T_Co)-orbit of primitive isotropic planes, and for any
such plane, J^perp/J = A_1^{+7}.

**Status.** The orbit uniqueness claim is UNVERIFIED computationally.
A bounded search found 15 primitive isotropic planes with J^perp/J = diag(-2, ..., -2)
(7 times), but the orbit computation via GAP was never performed.

Literature: Nikulin (1979), Sterk (1991), AEGS (2023), Dawes (2022).

* * *

## Task 4.1: Coxeter Diagram and Parabolic Subdiagrams

**Reflection group.** W(S_Co) acts on the period domain.
The root system Phi(S_Co) = {r in S_Co : r^2 = -2}. The Coxeter diagram G_{S_Co} encodes
angles between simple roots.

**Parabolic subdiagrams.** A maximal parabolic subdiagram is an affine Dynkin diagram
not properly contained in any larger affine Dynkin diagram.
These correspond to cusps in the Baily-Borel compactification.

**Claim.** G_{S_Co} contains a unique maximal parabolic subdiagram of type B_7-tilde(2),
corresponding to the 0-cusp with boundary lattice (9, 9, 1)_1.

**Status.** UNVERIFIED. The deleted script hand-coded the adjacency matrix rather than
deriving it from the lattice.
The Coxeter diagram itself needs to be constructed from scratch using Vinberg's
algorithm or equivalent.

Literature: AEGS (2023, Section 3), Nikulin (1979, 1980), Bourbaki (Lie Groups, Ch.
4-6).

* * *

## Task 5.1: Involution theta on Lambda_K3

**Goal.** Construct explicit 22x22 matrix theta in O(Lambda_K3) such that:
- Lambda_K3^{+theta} = T_Co (signature (2,9))
- Lambda_K3^{-theta} = S_Co (signature (1,10))
- theta^2 = I, theta^T G theta = G

**Nikulin's framework (Section 1.5).** For a primitive embedding S -> Lambda with Lambda
unimodular, the orthogonal complement T = S^perp satisfies Lambda = S + T and there
exists a sign involution acting by -I on S and +I on T.

**Status.** The deleted script claimed to construct a "glued lattice model" but the
construction was not independently verified.
Needs reimplementation.

Literature: Nikulin (1979), Dolgachev-Kondo (2013), Sterk (1991), Pieroni (2026, Theorem
72).

* * *

## Task 6.1: Surgery Vector and slc Stability

**Setup.** h_Co in T_Co is the Coble polarization (h_Co^2 = 2). The surgery vector is
l_i = h_Co . alpha_i for roots alpha_i. Since h_Co lies in the positive-definite part
<2>^2 and roots alpha_i lie in the negative-definite part <-2>^9, they are orthogonal: l
= 0.

**Dual complex.** For l = 0: B(0) = S^2 with standard integral-affine structure (Type
III degeneration, maximal unipotent monodromy).

**slc stability conditions.** The five KSBA conditions (S_2, nodal singularities,
Q-Cartier ampleness, avoidance, quotient structure) must be verified for (Z, epsilon C)
with Z = X / iota_Enr.

**Status.** The deleted script was the worst offender: 439 lines, 4 asserts, 47
f-strings, 14 checkmarks, 8 hardcoded booleans.
The "verification" consisted of setting is_S2 = True and then checking it later.
The genuine mathematical argument (surgery vector vanishes by orthogonality) is trivial
and correct, but the slc stability verification was pure prose theater.
The slc conditions require genuine geometric arguments, not print statements.

Literature: AEGS (2023, Sections 2.4, 6, 7), Nikulin (1979), Kollar (2013), Pieroni
(2026, lines 1225-1280).
