# Modular forms, Hecke operators and L-functions

Theory and leads behind the TODO node `modular-forms-and-hecke-algebras`. The
statements come from conversation and are unchecked. Open the source before
anything becomes a docstring.

## Objects

- **Congruence subgroups** of `SL_n(ZZ)`: the kernels `Γ(N)` of reduction mod `N`, and any subgroup containing some `Γ(N)`. For `n = 2`, `Γ_0(N)` and `Γ_1(N)`, with indices given by the usual product formulas. They are finite-index subgroups, so generators come from the Schreier route (`finite-index-subgroup-generators`).
- **Modular curves.** `Y_0(N) = Γ_0(N)\ℍ` and its compactification `X_0(N)`, obtained by adding cusps. Likewise `Y_1(N)`, `X_1(N)` and `X(N)`. They have genus formulas, cusps and elliptic points, and are moduli of elliptic curves with level structure.
- **Modular forms** `M_k(Γ)` and **cusp forms** `S_k(Γ)`. At the cusp `∞`, `f` has the Fourier (q-)expansion `f(τ) = Σ a_n q^n`, with `q = e^{2πiτ}`. The spaces are finite dimensional, with dimension formulas.
- **Automorphic forms.** The general setting, of which classical modular forms are the case `GL_2` over `QQ`, with the adelic reformulation.
- **Hecke operators** `T_n` on `M_k(Γ_0(N))`, with `T_p` given on q-expansions. They commute. The Hecke algebra `T` they generate over `ZZ` has normalized eigenforms, whose coefficients `a_n` are the eigenvalues.
- **L-functions.** For an eigenform, `L(f, s) = Σ a_n n^{-s} = ∏_p (1 − a_p p^{-s} + χ(p) p^{k−1−2s})^{-1}` (Euler product), with analytic continuation and a functional equation.
- **Varieties over `ZZ`.** `a_p`-type data come from counting points mod `p`. For an elliptic curve `E/QQ`, `a_p(E) = p + 1 − #E(F_p)` at good primes, not `#E(F_p)` itself. `L(E, s)` is the Euler product over good and bad primes, and `#X(F_p)` enters through the zeta function of `X`.
- **Modularity theorem** (Wiles, Taylor–Wiles, Breuil–Conrad–Diamond–Taylor). For an elliptic curve `E/QQ` of conductor `N`:
  - there is a newform `f ∈ S_2(Γ_0(N))` with `L(E, s) = L(f, s)`;
  - equivalently, there is a nonconstant map `X_0(N) → E`;
  - `E` is an isogeny factor of `J_0(N)`, and the Eichler–Shimura construction produces an abelian variety `A_f` from `f`.
- **Isogenies.** Surjective morphisms with finite kernel, `E → E/K` (Vélu's formulas), with dual isogenies and isogeny classes. `a_p` is an isogeny invariant.
- **Torsion points on complex tori.** For `E(ℂ) = ℂ/Λ` with `Λ = ZZ + ZZτ`, `E[n] = (1/n)Λ/Λ ≅ (ZZ/n)^2`. Its points are the `n^2` points `(a + bτ)/n` with `0 ≤ a, b < n`, which are the lattice points of `(1/n)Λ` lying in the half-open fundamental parallelogram. The same holds for `ℂ^g/Λ`, with `n^{2g}` points.

## Leads

- Diamond–Shurman, *A First Course in Modular Forms*: congruence subgroups, modular curves, Hecke operators, Eichler–Shimura, modularity.
- Serre, *A Course in Arithmetic*, ch. VII.
- Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*.
- Bump, *Automorphic Forms and Representations*.
- Silverman, *The Arithmetic of Elliptic Curves*: isogenies, torsion, `a_p`, `L(E, s)`.
- Stein, *Modular Forms, a Computational Approach*: modular symbols, and algorithms for `M_k(Γ)` and Hecke operators.
- Sage: `ModularForms`, `CuspForms`, `ModularSymbols`, `Gamma0`, `Gamma1`, `EllipticCurve.ap`, `EllipticCurve.lseries`, `isogeny`, `torsion_subgroup`. PARI: `mf*`, `ellap`, `lfun`. LMFDB for specimens.
