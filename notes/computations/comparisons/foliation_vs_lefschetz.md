# Comparison: `foliation.lib` vs `lefschetz-family`

## Overview

This document compares two computational approaches to the same mathematical objects: periods, monodromy, Picard-Fuchs operators, and Hodge-theoretic data for algebraic hypersurfaces.

|  | `foliation.lib` + `compute_monodromy.sing` | [`lefschetz-family`](https://pypi.org/project/lefschetz-family/0.1.11/) |
| --- | --- | --- |
| **Language** | Singular (computer algebra) | SageMath / Python |
| **Author** | — | Eric Pichon-Pharabod |
| **Approach** | Algebraic de Rham cohomology, Jacobian rings, Brieskorn modules | Picard-Lefschetz theory, numerical integration, vanishing cycles |
| **Arithmetic** | Exact (symbolic, over ℚ, cyclotomic fields) | Numerical (rigorous error bounds via interval arithmetic) |
| **Reference** | — | [arXiv:2306.05263](https://arxiv.org/abs/2306.05263) |

### Links

- **PyPI:** <https://pypi.org/project/lefschetz-family/>
- **GitHub (active development):** <https://github.com/ericpipha/lefschetz-family>
- **GitLab (INRIA mirror):** <https://gitlab.inria.fr/epichonp/lefschetz-family>
- **Predecessor:** [Pierre Lairez's `numperiods`](https://gitlab.inria.fr/lairez/numperiods) — early prototype for numerical period computation; `lefschetz-family` directly inherits and adapts code from it, eventually removing the dependency

* * *

## Feature Comparison

### Picard-Fuchs Operators

|  | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Entry point** | `PFequ(f, P_form, ve)`, `PFeq` | `X.picard_fuchs_equation(i)` |
| **Input** | Polynomial `f(x, t)`, differential form | Polynomial `P(X₀, …, Xₙ)` |
| **Output** | Differential operator in `D_t` annihilating periods | Differential operator for each cohomology basis element |
| **Method** | Gauss-Manin connection in Brieskorn-module basis | Computed implicitly from fibration data |

### Monodromy

|  | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Entry point** | `solve_hodge_monodromy(f, p_name)` | `X.monodromy_matrices` |
| **Method** | Indicial polynomial → residue matrix `R` → Jordan decomposition `R = R_s + R_n` → `N = 2πi·R_n`, `T = exp(N)` | Numerical continuation along loops around critical values → monodromy matrices on `H_{n-1}(X_b)` |
| **Output** | `N = log(T)`, `T = exp(N)`, Jordan blocks, unipotency check | Exact integral monodromy matrices (verified numerically) |
| **Certification** | Algebraic verification of `R_s = 0` (unipotency) | Checks that numerical monodromy matrices are integral |

### Periods

|  | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Entry point** | `PeriodMatrix`, `PeriodLinearCycle` | `X.period_matrix` |
| **Nature** | Symbolic (expressions in cyclotomic fields, Gamma values for Fermat) | Numerical complex with rigorous error bounds |
| **Scope** | Fermat hypersurfaces, linear cycles, special algebraic cycles | Arbitrary smooth projective hypersurfaces, elliptic surfaces |
| **Basis** | Jacobian-ring / Brieskorn-module basis | Explicit homology basis (thimbles + modifications) and cohomology basis (rational forms) |

### Gauss-Manin Connection

|  | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Entry point** | `gaussmanin(f, form, v)`, `gaussmaninmatrix(f, v)` | Implicit (not exposed directly) |
| **Output** | Connection matrix in de Rham basis | Not computed; periods obtained directly via integration |

### Vanishing Cycles & Thimbles

|  | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Vanishing cycles** | ❌ Not computed | ✅ `X.vanishing_cycles` |
| **Thimbles** | ❌ Not computed | ✅ `X.thimbles` — elements of `H_n(Y, Y_b)` |
| **Extensions** | ❌ | ✅ `X.extensions` — integer combinations of thimbles with vanishing boundary |

### Intersection Product

|  | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Entry point** | `IntersectionMatrix` (Fermat-specific) | `X.intersection_product` |
| **Scope** | Fermat hypersurfaces | General hypersurfaces, in computed homology basis |

### Homology

|  | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Approach** | Implicit via middle cohomology dimension and Jacobian ring | Explicit basis of `H_n(X)` via thimble decomposition and homology modification |
| **Entry points** | — | `X.homology`, `X.homology_modification`, `X.kernel_boundary`, `X.lift` |

### Hodge-Theoretic Data

|  | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Hodge numbers** | ✅ `HodgeNumber` | ❌ Not directly; inferable from period matrix |
| **Hodge filtration** | ✅ Via graded Jacobian-ring data | ❌ Not directly; inferable from `holomorphic_forms` indices |
| **Holomorphic forms** | Implicit | ✅ `X.holomorphic_forms` — indices of holomorphic basis elements |
| **Hodge cycles / classes** | ✅ `BasisHodgeCycles`, `DimHodgeCycles` (Fermat) | ❌ Not directly |
| **Hodge locus** | ✅ `HodgeLocusIdeal`, `SmoothReduced`, `DeformSpace` | ❌ Not implemented |

### Elliptic Surfaces

|  | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Support** | As hypersurfaces (no special treatment) | ✅ Dedicated `EllipticSurface` class |
| **Mordell-Weil** | ❌ | ✅ `X.mordell_weil`, `X.mordell_weil_lattice` |
| **Néron-Severi** | ❌ | ✅ `X.neron_severi` |
| **Trivial lattice** | ❌ | ✅ `X.trivial` |
| **Essential lattice** | ❌ | ✅ `X.essential_lattice` |
| **Singular fibres** | ❌ | ✅ `X.singular_components` |

### Extended Variety Classes

These are mathematical objects not covered by `foliation.lib`:

| Variety | Method | Mathematical interest |
| --- | --- | --- |
| **Double covers of ℙ²** ramified along a sextic | K3 surface as double cover → same Lefschetz pencil machinery | Alternative model for K3 periods, avoids high-degree hypersurface equations |
| **Fibre products of elliptic surfaces** | Iterated fibration structure → periods from component data | Calabi-Yau threefolds, modular forms |
| **Monodromy representations** of hypersurface families | Tracks differential operator monodromy across parameter space | Variation of Hodge structure over moduli |

* * *

## Mathematical Approach

### `foliation.lib`: Algebraic de Rham Cohomology

```
f(x, t) polynomial family
    │
    ▼
Jacobian ideal J = (∂f/∂x₀, …, ∂f/∂xₙ)
    │
    ▼
Brieskorn module basis (okbase, kbase)
    │
    ▼
Reduction of forms modulo dF and J
    │
    ▼
Gauss-Manin connection matrix (gaussmaninmatrix)
    │
    ▼
Picard-Fuchs operator (PFequ)
    │
    ▼
Indicial polynomial at t = 0
    │
    ▼
Residue matrix R → Jordan form → N = log(T), T = exp(N)
```

**Strengths:** exact arithmetic, Hodge interpretation, special-cycle machinery, Hodge-locus experiments.

**Limitations:** restricted to families where Jacobian-ring reduction terminates; no numerical period computation; Fermat-specialized for many features.

### `lefschetz-family`: Picard-Lefschetz Theory + Certified Numerical Integration

```
P(X₀, …, Xₙ) defining polynomial
    │
    ▼
Iterative Lefschetz pencil X ⇢ ℙ¹
    │
    ▼
Critical values (discriminant of the pencil)
    │
    ▼
Voronoi graph / Delaunay triangulation of critical points in ℂ
    │
    ▼
Numerical integration along paths in the Voronoi graph
    │
    ▼
Vanishing cycles δ_i ∈ H_{n-1}(X_b) at each critical value
    │
    ▼
Thimbles Δ_i ∈ H_n(Y, Y_b) with ∂Δ_i = δ_i
    │
    ▼
Period matrix ∫_{γ_j} ω_i via thimble decomposition
    │
    ▼
Homology modification: correct H_n(Y) → H_n(X)
```

The key idea is **Picard-Lefschetz theory**: the homology of the total space is reconstructed from the homology of a generic fiber together with the vanishing cycles at the critical points of the pencil.
The monodromy around each critical value is a Dehn twist along the corresponding vanishing cycle.
Numerical integration along explicit paths gives the period matrix, with rigorous error bounds propagated through every step via interval arithmetic — each output complex number comes with a guaranteed enclosure.

**Monodromy tracking**: the monodromy of the Picard-Fuchs differential operators is tracked as one moves around critical values, recovering the action on homology.
This is the numerical analogue of computing the residue matrix and its exponential.

**Exceptional divisors**: the modification Y → X requires correcting for the blow-up.
Computing this correction is costly; for some purposes (e.g. Picard rank of a quartic surface) the uncorrected periods suffice.

**Strengths:** works for arbitrary smooth hypersurfaces; handles varieties up to cubic fourfolds; explicit homology basis; elliptic surface arithmetic (MW/NS lattice).

**Limitations:** numerical, not exact; no symbolic Hodge-locus machinery; no special-cycle period computation; Delaunay method currently broken for some cases; singular varieties not yet supported.

* * *

## Variety Classes

`lefschetz-family` handles the following classes of varieties:

| Variety | Mathematical content |
| --- | --- |
| Smooth projective hypersurfaces | Full period matrix, monodromy, intersection form |
| Elliptic surfaces over ℙ¹ | Periods + Mordell-Weil group, Néron-Severi lattice, trivial/essential lattices, singular fibre components |
| Double covers of ℙ² ramified along a sextic | K3 periods via double-cover model rather than degree-6 hypersurface equation |
| Fibre products of elliptic surfaces | Calabi-Yau threefold periods from component data |
| Families of hypersurfaces | Monodromy representations over parameter space |

* * *

## Relationship to Extraction Specs

The two extraction specs in this directory are the bridge between these two worlds:

### `foliation_extraction_spec.md`

Extracts the **algebraic / Hodge-theoretic** side:
- Brieskorn-module engine
- Gauss-Manin / Picard-Fuchs toolkit
- Hodge numbers and filtrations
- Hodge-locus experimentation
- Fermat period computation

### `periods_extraction_spec.md`

Extracts the **holonomic / annihilator** side (from Lairez's Magma `periods` repo):
- Cohomological reduction of rational forms
- Annihilator computation for rational periods
- Diagonal / constant-term annihilators
- Modular reconstruction

### Combined Vision

A mature system would have two complementary layers sharing infrastructure:

```
sage.hodge.hypersurfaces.brieskorn     ← algebraic cohomology (foliation.lib)
sage.hodge.hypersurfaces.gaussmanin    ← Gauss-Manin / PF (foliation.lib)
sage.hodge.hypersurfaces.projective    ← smooth hypersurface Hodge theory
sage.hodge.degenerations.local         ← one-parameter degenerations
sage.hodge.fermat                      ← Fermat periods / cycles
sage.hodge.fermat.hodge_loci           ← Hodge-locus experiments

sage.holonomic.periods.reduction       ← rational form reduction (lairez/periods)
sage.holonomic.periods.annihilator     ← annihilator computation
sage.holonomic.diagonals               ← diagonals of rational functions
sage.experimental.reconstruction.modular ← modular reconstruction

                                          ← numerical periods (lefschetz-family)
                                          ← certified integration, thimbles
```

Shared infrastructure:
- Polynomial reduction backends
- Differential-operator infrastructure (Ore algebras)
- Modular reconstruction
- Local singularity and monodromy analysis

* * *

## Summary

| Dimension | `foliation.lib` | `lefschetz-family` |
| --- | --- | --- |
| **Arithmetic** | Exact / symbolic | Numerical (certified) |
| **Method** | Jacobian ring → Gauss-Manin → PF | Lefschetz pencil → integration → thimbles |
| **Scope** | Special families, Fermat, Hodge loci | General smooth hypersurfaces, elliptic surfaces |
| **Periods** | Symbolic (Gamma values, cyclotomic) | Numerical complex (rigorous error bounds) |
| **Monodromy** | From residue matrix Jordan form | From numerical continuation |
| **Hodge structure** | Explicit (numbers, filtration, cycles) | Implicit (recoverable from period matrix) |
| **Special cycles** | ✅ Period vectors, tangent spaces, Hodge loci | ❌ |
| **Elliptic surfaces** | As hypersurfaces | Dedicated class with MW / NS lattice |
| **Variety classes** | Polynomial families with Jacobian reduction | Arbitrary smooth hypersurfaces, double covers, fibre products |

They compute the **same mathematical objects** via **complementary methods**. The algebraic approach gives exact structure theorems and Hodge-locus experiments; the numerical approach gives period matrices for general varieties.
A complete computational Hodge theory package would combine both.
