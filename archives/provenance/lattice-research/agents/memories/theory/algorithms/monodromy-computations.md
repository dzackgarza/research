# Monodromy Computation for Algebraic Families

This document surveys available tools for computing the **homological monodromy** of a
one-parameter family f(x₁,...,xₙ, t) = 0 over a punctured disc Δ* = Δ \ {0}.

The object of interest is the monodromy operator

  M ∈ Aut(Hₖ(F_{t₀}, ℤ))  (for k = dim F_t, symplectic for k odd)

where F_{t₀} = V(f(·, t₀)) is the fiber over a basepoint. Since π₁(Δ*, t₀) ≅ ℤ,
the monodromy is a single matrix.

Two cases are treated separately:
- **Families of curves** (n=2): Sage's `RiemannSurface` machinery is directly applicable.
- **Families of surfaces** (n=3, e.g. K3 families): requires the Picard-Fuchs ODE
  approach via `ore_algebra`.

---

## Case 1: Families of curves — RiemannSurface parallel transport

**The per-fiber step is trivial**: `Curve(f_t).riemann_surface(prec=100)` already works
for any affine or projective plane curve over QQ (or a number field with complex
embedding). Both `AffinePlaneCurve` and `ProjectivePlaneCurve` expose `.riemann_surface()`.

**The family monodromy** requires chaining across a loop. Given f(z, w, t) ∈ ZZ[z,w,t],
specialize t to a sequence of QQ or QQ[i] values forming a closed loop around t=0,
with no critical value of Δ(t) = Res_z(f, ∂f/∂z) lying between consecutive points.

Canonical loop: the unit square in QQ[i] = QuadraticField(-1),
  t: 1  →  -i  →  -1  →  i  →  1
or scaled by ε if critical values are near the origin. Vertices are in ZZ[i], so each
specialization f(z, w, t_k) ∈ QQ[i][z,w] which `RiemannSurface` accepts.

At each consecutive pair (t_k, t_{k+1}):
1. S_k = Curve(f(z,w,t_k)).riemann_surface(prec=p)
2. S_{k+1} = Curve(f(z,w,t_{k+1})).riemann_surface(prec=p)
3. `isos = S_k.symplectic_isomorphisms(S_{k+1})`
   - Returns all M ∈ Sp(2g, ZZ) with Ω(S_k) ≈ Ω(S_{k+1})·M (via LLL on period matrices,
     filtered by M·Rosati(M) = I).
   - Since no critical value lies between t_k and t_{k+1}, the Jacobians are isomorphic
     and the list is non-empty.
   - The local parallel transport is the M ∈ isos minimising ||M − I|| (closest to identity).
4. Compose: M_total = M_{N-1} · ... · M_0.

**Base ring**: t_k ∈ QQ[i] means f(z,w,t_k) ∈ K[z,w] where K = QuadraticField(-1,
embedding=CC(I)). `RiemannSurface` accepts number fields with complex embeddings.

**Limitations of `symplectic_isomorphisms`**:
- Requires the two surfaces to have isomorphic Jacobians (automatic for small enough steps).
- LLL lattice reduction over the period matrix — cost scales as O(g^6) roughly, so fast
  for g=1,2, feasible for g≤4.
- Precision parameter `prec` must be large enough for LLL to resolve the answer: use
  `prec=100` or higher for genus ≥ 2.
- Returns the FULL GROUP of Sp(2g,ZZ) automorphisms when S_k = S_{k+1} (trivial step);
  for distinct nearby surfaces typically returns a singleton or very small set.

**Explicit code sketch**:

```python
from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
from sage.rings.number_field.number_field import NumberField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.matrix.constructor import identity_matrix
from sage.rings.integer_ring import ZZ

def monodromy_curve_family(f_zwt, t_vals, prec=100):
    """
    Compute the monodromy of f(z, w, t)=0 along the loop t_vals[0]->...->t_vals[-1].

    f_zwt: polynomial in QQ[z, w, t] (or ZZ[z, w, t])
    t_vals: list of (rational or QQ[i]) values forming a closed loop,
            e.g. [1, -I, -1, I, 1] (unit square in QQ[i]) or finer subdivision.
            No critical value of Disc_z(f) should lie strictly between consecutive points.
    """
    R = f_zwt.parent()
    z, w, t_var = R.gens()

    def surface_at(t_val):
        f_zw = f_zwt.subs({t_var: t_val})
        return RiemannSurface(f_zw, prec=prec)

    g = surface_at(t_vals[0]).genus
    M_total = identity_matrix(ZZ, 2*g)

    for k in range(len(t_vals) - 1):
        S0 = surface_at(t_vals[k])
        S1 = surface_at(t_vals[k+1])
        isos = S0.symplectic_isomorphisms(S1)
        if not isos:
            raise ValueError(f"No symplectic isomorphism at step {k}; "
                              "check for critical values between t_vals[{k}] and t_vals[{k+1}]")
        # Pick the one closest to identity (local parallel transport)
        M_k = min(isos, key=lambda M: (M - identity_matrix(ZZ, 2*g)).norm())
        M_total = M_k * M_total

    return M_total
```

**Example — Legendre family y² = x(x-1)(x-t)**:

```python
R.<z, w, t> = ZZ[]
f = w^2 - z*(z-1)*(z-t)
# Critical values of f: t=0, t=1. Loop around t=0 using QQ[i] square:
QQi.<I> = QuadraticField(-1)
t_loop = [QQi(v) for v in [1/2 + I/2, -1/2 + I/2, -1/2 - I/2, 1/2 - I/2, 1/2 + I/2]]
# (scale avoids t=0 and t=1 critical values; check Disc_z(f) = t^2(t-1)^2)
M = monodromy_curve_family(f, t_loop, prec=100)
# Expected: M = (1,0; -2,1) or (1,2; 0,1) depending on orientation/basis
```

**Example — cuspidal degeneration y² = x³ - t**:

```python
R.<z, w, t> = ZZ[]
f = w^2 - z^3 + t
# Single critical value at t=0. Loop:
QQi.<I> = QuadraticField(-1)
t_loop = [QQi(v) for v in [1, -I, -1, I, 1]]  # unit square, avoids t=0
M = monodromy_curve_family(f, t_loop, prec=100)
# Expected: unipotent M = (1,0; 1,1), N = M-I, N^2 = 0 (Kodaira type I_1)
```

---

## Case 2: Families of surfaces — ore_algebra (Picard-Fuchs ODE)

**Setup**: f(x₁,...,xₙ, t) for n ≥ 3 (fibers are surfaces). The period integrals
  ω(t) = ∫_{γ(t)} Ω    (Ω = holomorphic (n-1)-form on F_t)
satisfy a Picard-Fuchs ODE L_t(ω) = 0, a linear ODE in t with rational function
coefficients. The monodromy of this ODE (analytic continuation of solutions around
the singular points) IS the monodromy of the family.

**Key tool**: `ore_algebra.analytic.monodromy.monodromy_matrices(dop, base)`.
- Input: a differential operator `dop` in `ore_algebra`'s `DifferentialOperators` ring,
  and a base point `base ∈ QQbar`.
- Output: one matrix per singular point, each an element of CBF (complex ball field),
  with certified precision. The matrices generate the monodromy group.
- Algorithm: analytic continuation via numerical_transition_matrix along carefully
  chosen Voronoi-like paths, using ball arithmetic for certified error bounds.
 Two modes: `algorithm='connect'` (default), `algorithm='binsplit'` (more ).

**Note on availability**: `ore_algebra` is NOT a standard Sage package and is not
currently installed. It is available from https://github.com/mkauers/ore_algebra .
It requires a Cython build step.

**The hard step — computing the Picard-Fuchs ODE**:

Given f(x, y, z, t) = 0 (K3 surface family), the Picard-Fuchs ODE for ∫ Ω/(f^k) as a
function of t is obtained by Griffiths-Dwork reduction: repeatedly differentiate
∫ Ω/f^k with respect to t, and reduce the resulting rational differential forms modulo
the image of the Griffiths reduction map to express everything in terms of a basis of
H^n(F_t). This gives an ODE of order = dim H^n.

This computation is NOT available in Sage. It requires:
- Macaulay2's `PeriodIntegrals` package (Lian-Song-Yau, implemented by H. Lê Trung Nhân)
- or Singular's deformation module / `gaussman.lib`
- or an explicit tabulation (for standard families, the Picard-Fuchs ODE is in the
  literature — see Doran-Morgan [DM06] for K3 families, or AESZ database for CY3)

Once the ODE is known:
```python
# ore_algebra (once installed):
from ore_algebra import DifferentialOperators
from ore_algebra.analytic.monodromy import monodromy_matrices

Dops, t, Dt = DifferentialOperators()

# Example: Picard-Fuchs for the family y^2 = x(x-1)(x-t) (Legendre, genus 1)
# ODE: 4t(1-t)·y'' + 4(1-2t)·y' - y = 0
dop = 4*t*(1-t)*Dt^2 + 4*(1-2*t)*Dt - 1
mats = monodromy_matrices(dop, base=QQ(1,2))
# Returns one matrix per singularity (t=0, t=1, t=∞)
```

For K3 families (Picard number ρ, second cohomology H²), the monodromy group is a
subgroup of O(Λ) where Λ = H²(F, ZZ) with the intersection form. The Picard-Fuchs
ODE has order = 2 + (rank of primitive cohomology) for a one-parameter family.

**`ore_algebra.analytic.monodromy` code structure** (from source):
- `monodromy_matrices(dop, base, eps, sing)`: iterates `_monodromy_matrices`
- For regular singular points: computes `formal_monodromy` (purely from local exponents,
  no numerical work) if the point is regular and the formal monodromy is scalar.
  Otherwise uses `numerical_transition_matrix` along a polygon around the singularity.
- For irregular singular points: `_local_monodromy_loop` integrates numerically around
  a polygon.
- The base point can be QQbar (including QQ and QQ[i]). Singularities are roots of
  the leading coefficient of dop.

---

## Summary: what is directly feasible

| Family type | Method | Tools | Base ring | Status |
|---|---|---|---|---|
| Curves (f(z,w,t)=0) | RiemannSurface chain | Sage built-in | ZZ/QQ/QQ[i] | **Directly implementable** |
| Curves (known ODE) | ore_algebra | external package | QQ | Needs ore_algebra install |
| Surfaces (known Picard-Fuchs ODE) | ore_algebra | external package | QQ | Needs ore_algebra install |
| Surfaces (ODE not known) | Griffiths-Dwork reduction | Macaulay2 / Singular | QQ | Requires external CAS step |

For the primary use case (ZZ-coefficient families of curves): the `RiemannSurface` chain
approach is completely self-contained in Sage. Loop coordinates are always taken in
QQ[i] (vertices {1, -i, -1, i} scaled to avoid critical values).

---

## Explicit examples with expected monodromy

### Legendre family y² = x(x-1)(x-t)

Critical values: t=0, t=1. Fundamental group π₁(ℙ¹ \ {0,1,∞}) = ⟨γ₀, γ₁ | γ₀γ₁γ∞ = 1⟩.

Monodromy in standard symplectic basis {[α],[β]} of H₁(F_{1/2}, ZZ):
  M₀ = (1, 0; -2, 1)   (around t=0; transvection by the vanishing cycle δ₀)
  M₁ = (1, 2; 0, 1)    (around t=1; transvection by the vanishing cycle δ₁)
  M∞ = (M₀·M₁)⁻¹ = (-1, -2; 2, 3)

These generate Γ(2) ⊂ SL(2,ZZ) (principal congruence subgroup of level 2).

### Weierstrass/cuspidal family y² = x³ - t

Critical value: t=0 (Δ = -27t² = 0). Fiber F_0: cuspidal cubic (genus 0 with cusp).
Kodaira fiber type: I₁ (nodal after change of variables; the cusp is a rational
singularity). Monodromy:
  M = (1, 0; 1, 1)   (unipotent; N = M-I, N² = 0)
This is the standard Type II unipotent in Kulikov/Persson-Pinkham classification.

### Hesse pencil x³+y³+1 = 3t·xyz (elliptic surface)

Critical values: t = 1, ω, ω² (ω = e^{2πi/3}), t = ∞ (Hessian inflection). Each
gives an I₁ Kodaira fiber. The global monodromy group is commensurable with SL(2,ZZ).

---

## References

- Sage RiemannSurface: `sage.schemes.riemann_surfaces.riemann_surface` (4115 lines).
  Key methods: `period_matrix`, `riemann_matrix`, `homomorphism_basis`,
  `symplectic_isomorphisms`, `monodromy_group` (sheet permutations only).
  `integer_matrix_relations`: LLL-based Z-basis of Hom(Jac₁, Jac₂).
  Source: Bruin-Sijsling-Zotine [BSZ2019].
- ore_algebra: https://github.com/mkauers/ore_algebra — Kauers-Mezzarobba et al.
  `analytic/monodromy.py`: `monodromy_matrices`, `formal_monodromy`, `_monodromy_matrices`.
- Griffiths-Dwork: Dwork (1962); Griffiths (1969); Dimca "Singularities and Topology"§5.
- Picard-Lefschetz: SGA 7 Exp. XV (Katz); Lamotke (1981).
- Kulikov/Persson-Pinkham: classification of degenerate fibers, Kodaira types I_n/II/III/IV.
- Doran-Morgan [DM06]: classification of K3 families by Picard-Fuchs ODE.
