# Spec: Extracting General-Purpose Hodge-Theoretic Tools from `foliation.lib`

## Goal

This document records a realistic extraction plan for turning the mathematically valuable parts of `foliation.lib` into reusable, higher-level code suitable for integration into a system such as SageMath for experimentation in explicit Hodge theory and degenerations of hypersurfaces.

The question is not merely what `foliation.lib` already implements directly. The question is what a state-of-the-art coding model, given this library plus standard mathematical infrastructure from Sage/Julia/Python/Ore-algebra ecosystems, could reasonably assemble into general-purpose computational tools.

The intended scale is a serious implementation effort, roughly on the order of 20-40M tokens of code generation, refactoring, glue, testing, and mathematical integration.

## High-Level Conclusion

The realistic target is not a universal engine for mixed Hodge structures of arbitrary degenerations. The realistic target is a strong experimental package for explicit Hodge theory of hypersurfaces and their degenerations, centered around:

- Jacobian-ring and Brieskorn-module models of cohomology.
- Gauss-Manin connection computation for explicit polynomial families.
- Picard-Fuchs operator extraction and local monodromy analysis.
- Hodge-number and Hodge-filtration computations for smooth hypersurfaces in structured settings.
- Explicit period calculations for distinguished algebraic cycles in special families.
- Tangent-space and infinitesimal Hodge-locus experiments.
- Partial limiting-Hodge-data experiments for one-parameter degenerations.

`foliation.lib` provides enough mathematical ingredients to make those goals plausible, but not enough to justify claims of a fully general MHS/VHS/LMHS package for arbitrary varieties.

## Mathematical Interpretation of the Existing Library

The library contains three main layers of mathematical content.

### 1. Algebraic models of cohomology

This layer includes:

- Jacobian-ring / Milnor-space basis construction.
- Reduction of forms modulo `df` and the Jacobian ideal.
- Explicit basis management for Brieskorn modules `H'` and `H''`.
- Ordering and basis heuristics related to mixed-Hodge-compatible structures, for example via `dbeta`.

This is the best foundation for reusable code.

### 2. Variation of Hodge structure and differential equations

This layer includes:

- Gauss-Manin connection of explicit de Rham representatives.
- Connection matrices in explicit bases.
- Picard-Fuchs operators for periods.
- Discriminant computations and parameter differentiation.
- Differential systems derived from connection matrices.

This is a strong basis for a reusable Gauss-Manin / Picard-Fuchs subsystem.

### 3. Explicit Hodge-theoretic experiments in special families

This layer includes:

- Mixed Hodge pieces for affine generalized Fermat hypersurfaces.
- Hodge numbers in special structured settings.
- Explicit period matrices and intersection matrices.
- Computation of Hodge cycles and their period vectors.
- Tangent-space and Hodge-locus computations for special cycles in Fermat-type deformations.

This is mathematically rich and distinctive, but more specialized.

## What Is Realistically Extractable

The realistic output is a stack of medium-level tools, not a single monolithic package.

## Package 1: A General Hypersurface de Rham / Brieskorn Module Engine

### Core functionality

Input:

- A polynomial family `f(x_0, ..., x_n, t_1, ..., t_r)`.
- Explicit assumptions such as smooth generic fiber, isolated singularities, tameness, or weighted-homogeneous leading part.

Output:

- Jacobian ring basis.
- Brieskorn-module basis.
- Reduction of forms to canonical representatives.
- Multiplication tables.
- Pole-order filtration data.
- Degree bookkeeping for candidate Hodge filtrations.

### Why this is general-purpose

This is not tied to Fermat families. It applies broadly to explicit hypersurface families and provides the algebraic model needed for many further computations.

### What `foliation.lib` contributes

- `okbase`
- `mulmat`
- `muldF`
- `divmat`
- `linear`
- `linearp`
- `infoof`
- `dbeta`

### What new code must add

- Modern basis caches.
- Better coercions between polynomial, quotient, and differential-form models.
- Graded structures.
- Exact/symbolic backends.
- Stable APIs and persistence.

### Recommended module name

`sage.hodge.hypersurfaces.brieskorn`

## Package 2: A Reusable Gauss-Manin / Picard-Fuchs Toolkit

### Core functionality

Given a family `f(x,t)` and a differential form, compute:

- Gauss-Manin derivatives.
- Connection matrices.
- Scalar Picard-Fuchs equations.
- Companion systems.
- Regular singularity tests.
- Local exponents from indicial polynomials.
- Residue matrices.
- Symbolic or semi-symbolic local monodromy data near singular points.

### Why this is general-purpose

This is broadly useful for explicit one-parameter and multi-parameter families of hypersurfaces.

### What `foliation.lib` contributes

- `gaussmanin`
- `gaussmaninvf`
- `gaussmaninmatrix`
- `PFequ`
- `PFeq`
- `sysdif`
- `discriminant`

### What new code must add

- Ore-algebra output and manipulation.
- Integration with Sage differential operators.
- Local analysis of singular points.
- Automatic normalization of operators and systems.
- More principled error handling and exactness control.

### Recommended module name

`sage.hodge.hypersurfaces.gaussmanin`

## Package 3: A Hodge-Theoretic Layer for Smooth Hypersurfaces

### Core functionality

For smooth projective hypersurfaces, compute:

- Primitive middle cohomology dimensions.
- Hodge numbers.
- Hodge filtration via graded Jacobian-ring data.
- Explicit de Rham representatives for Hodge pieces.

### Why this is realistic

This uses standard Griffiths theory and Jacobian-ring constructions. The theory is classical and algorithmic enough for implementation.

### What `foliation.lib` contributes

- `HodgeNumber` in special settings.
- Old routine `hodgenum` for weighted hypersurfaces in low dimensions.
- Various basis and grading utilities.

### What new code must add

- Full Griffiths residue formalism.
- General Jacobian-ring formulas for smooth projective hypersurfaces.
- Primitive-cohomology extraction.
- Hodge filtration APIs.

### Recommended module name

`sage.hodge.hypersurfaces.projective`

## Package 4: An Experimental One-Parameter Degeneration Lab

### Core functionality

For one-parameter degenerations of explicit hypersurfaces over a punctured disk, compute:

- Discriminant points.
- Picard-Fuchs operators.
- Local exponents.
- Regular-singular checks.
- Residue matrices.
- Quasi-unipotent / unipotent tests from local operators.
- Nilpotent logarithms after verifying or imposing unipotent reduction.
- Candidate limiting-Hodge data via basis tracking and asymptotic analysis.
- Numerical continuation and monodromy experiments for selected periods.

### What is realistic

- Local monodromy and nilpotent logarithm extraction.
- Comparison of filtration ranks across fibers.
- Period asymptotics for explicit forms.
- Regularity checks and basis changes.

### What is not realistic from these ingredients alone

- A full abstract limiting mixed Hodge structure engine.
- Arbitrary canonical Deligne-extension / nearby-cycle formalism.
- Clemens-Schmid-style general infrastructure.

### What `foliation.lib` contributes

- Discriminant computation.
- Gauss-Manin and Picard-Fuchs infrastructure.
- MHS-adapted basis heuristics via `dbeta`.

### What new code must add

- Local ODE analysis.
- Monodromy extraction from local differential equations.
- Basis transport and normalization.
- Numerical/symbolic comparison infrastructure.

### Recommended module name

`sage.hodge.degenerations.local`

## Package 5: A Special-Cycles / Hodge-Locus Experimentation Package

### Core functionality

For special families, especially Fermat and nearby deformations:

- Represent explicit algebraic cycles.
- Compute their period vectors.
- Build period-constraint matrices.
- Compute tangent-space codimensions of Hodge loci.
- Test smoothness and reducedness heuristically at finite truncation order.
- Explore Noether-Lefschetz-type phenomena experimentally.

### Why this is valuable

This is highly specialized, but mathematically distinctive and not something standard CAS packages already provide in an integrated way.

### What `foliation.lib` contributes

- `PeriodLinearCycle`
- `ListPeriodLinearCycle`
- `SumTwoLinearCycle`
- `SumThreeLinearCycle`
- `mTwoLinearCycle`
- `mLinearCycle`
- `HodgeLocusIdeal`
- `SmoothReduced`
- `EquHodge`
- `InterTang`
- `DeformSpace`
- `DistinctHodgeLocus`
- `TwoCI`

### What new code must add

- Cleaner cycle abstractions.
- Better matrix/rank bookkeeping.
- Truncation management.
- Exact and numerical comparison tools.
- Better APIs for cycle families and deformation spaces.

### Recommended module name

`sage.hodge.fermat.hodge_loci`

## Package 6: A Fermat Period / Intersection Package

### Core functionality

For generalized Fermat hypersurfaces, compute:

- Mixed Hodge pieces.
- Hodge numbers.
- Period matrices.
- Intersection matrices.
- Bases of Hodge cycles.
- Transcendental and algebraic pieces of cohomology.
- Explicit periods of linear cycles.

### Why this is attractive

This is mathematically clean, explicit, and probably the easiest specialized package to make robust.

### What `foliation.lib` contributes

- `MixedHodgeFermat`
- `HodgeNumber`
- `PeriodMatrix`
- `IntersectionMatrix`
- `DimHodgeCycles`
- `BasisHodgeCycles`
- `Matrixpij`
- `TranCoho`
- `LinearCoho`
- `PeriodLinearCycle`

### What new code must add

- Sage-native cyclotomic field integration.
- Better object models for cohomology and cycles.
- Explicit Hodge-diamond formatting and summaries.
- Improved documentation and examples.

### Recommended module name

`sage.hodge.fermat`

## What the Extracted System Would Mean by “Computing”

The extracted system should make the mathematical meaning of “compute” explicit.

### For a pure Hodge structure on a fixed smooth hypersurface

Computing the Hodge structure means, depending on context:

- Producing a basis of de Rham cohomology.
- Organizing that basis by Hodge level or graded Jacobian-ring data.
- Computing Hodge numbers.
- Computing periods against chosen cycles.
- Computing the intersection form.
- Identifying Hodge classes inside middle cohomology.

### For a variation of Hodge structure

Computing the variation means:

- Computing Gauss-Manin connection matrices.
- Computing Picard-Fuchs operators for period integrals.
- Computing period vectors or their Taylor expansions.
- Computing local monodromy-related data near singular fibers.

### For a degeneration

The extracted system should be careful not to overstate what it computes. A realistic claim is:

- It computes de Rham/Gauss-Manin/Picard-Fuchs data for explicit families.
- It can derive local monodromy information and nilpotent data in many one-parameter cases.
- It can support experiments toward limiting Hodge-theoretic structures.

It should not claim, by default, that it computes the full limiting mixed Hodge structure of arbitrary degenerations.

## What Is Not Realistically Achievable from `foliation.lib` Alone

Even with substantial LLM-generated code and external glue, the resulting system should not be advertised as a package for:

- Arbitrary LMHS computation.
- Arbitrary mixed Hodge structures of singular varieties.
- General nearby/vanishing cycle formalisms.
- Arbitrary homology computation.
- Fully general Hodge-diamond computation for arbitrary degenerations.
- General cycle-class computation for arbitrary subvarieties.

Those require broader theory infrastructure than what is present in this library.

## Required External Mathematical Infrastructure

To make the extraction successful, the generated system would need to combine `foliation.lib` ideas with standard external ingredients:

- Griffiths residue formalism for smooth projective hypersurfaces.
- Better Jacobian-ring and graded-module abstractions.
- Ore algebra / Weyl algebra support for differential operators.
- Regular-singular and indicial analysis.
- Exact cyclotomic and number-field linear algebra.
- Symbolic and numeric ODE continuation for periods.
- Filtration bookkeeping and basis normalization.
- Interfaces to Sage quotient rings, ideals, modules, differential operators, and number fields.
- A substantial test suite against known elliptic, K3, Calabi-Yau, and Fermat examples.

## Proposed Priority Order

### Highest priority

1. Brieskorn-module / Jacobian-ring cohomology engine.
2. Gauss-Manin / Picard-Fuchs engine.
3. Local monodromy and nilpotent-log extraction for one-parameter families.

These are the most reusable and most likely to become stable, general tools.

### Second priority

4. Hodge-number and Hodge-filtration package for smooth projective hypersurfaces.
5. Fermat period / intersection / Hodge-cycle package.

These are mathematically important and highly usable, but somewhat more specialized.

### Third priority

6. Hodge-locus and special-cycle experimentation layer.

This is valuable, but more likely to remain research-grade experimental code than a core general-purpose subsystem.

## Most Reusable Outputs

The most reusable extractions are:

- Brieskorn-module reduction and Jacobian-ring cohomology.
- Gauss-Manin connection and Picard-Fuchs computation.
- Local monodromy and nilpotent-log extraction from Picard-Fuchs operators.
- Hodge numbers and Hodge filtration for explicit smooth hypersurfaces.

## Most Distinctive Outputs

The most mathematically distinctive extractions are:

- Fermat period and Hodge-cycle computations.
- Tangent-space and Hodge-locus machinery.
- Explicit period-vector computations for special algebraic cycles.

## Most Likely To Become Robust Sage Features

- Hodge numbers and filtrations for smooth hypersurfaces.
- Gauss-Manin / Picard-Fuchs for explicit one-parameter families.
- Local monodromy experiments for degenerations.

## Most Likely To Remain Experimental

- `SmoothReduced` / `HodgeLocusIdeal` / `DeformSpace` style Hodge-locus machinery.
- Special-cycle deformation experiments beyond linear cycles.

## Recommended Initial Module Architecture

The most coherent initial architecture is:

- `sage.hodge.hypersurfaces.brieskorn`
- `sage.hodge.hypersurfaces.gaussmanin`
- `sage.hodge.hypersurfaces.projective`
- `sage.hodge.degenerations.local`
- `sage.hodge.fermat`
- `sage.hodge.fermat.hodge_loci`

## Final Summary

`foliation.lib` contains enough mathematical content that a GPT-5.4-scale implementation effort could plausibly produce a genuinely valuable Sage extension for explicit computational Hodge theory of hypersurfaces and their one-parameter degenerations.

The strongest general-purpose outputs would be:

- Brieskorn-module cohomology.
- Gauss-Manin / Picard-Fuchs computation.
- Local monodromy analysis.
- Hodge-number and filtration tools for smooth hypersurfaces.

The strongest specialized outputs would be:

- Fermat period computations.
- Hodge-cycle calculations.
- Hodge-locus and tangent-space experimentation.

The correct scope is an explicit computational Hodge-theory package for hypersurfaces, not a universal package for arbitrary MHS or arbitrary degenerations.
