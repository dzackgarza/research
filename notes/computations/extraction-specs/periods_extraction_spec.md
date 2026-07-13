# Spec: Extracting General-Purpose Tools from `lairez/periods`

## Goal

This document records what is worth extracting and generalizing from Pierre Lairez's `periods` repository:

- Repository: `https://github.com/lairez/periods`
- Scope: a preliminary Magma implementation of the algorithm in "Computing periods of rational integrals"

The aim is not to preserve the implementation as-is.
The aim is to identify the mathematically significant, algorithmically reusable pieces that a state-of-the-art coding model could turn into general-purpose code for SageMath or similar systems.

## High-Level Conclusion

Yes, there is definitely material here worth extracting and generalizing.

The strongest reusable contribution is not merely "a Magma implementation of Picard-Fuchs equations."
The most important extractable content is a computational pipeline for turning rational integrals into annihilating differential equations by combining:

- de Rham / Griffiths-Dwork / Rham-Koszul reduction of rational forms,
- polynomial linear algebra over function fields,
- modular computation and rational reconstruction,
- operator synthesis for periods, diagonals, and constant-term generating functions.

This is mathematically substantial and more broadly reusable than the current repository framing might suggest.

## What the Repository Already Exposes

The README states that the package computes periods of rational integrals and implements the algorithm from Lairez's paper "Computing periods of rational integrals."
It also points to `misc/apery.m` for documentation.

The key user-facing entry points in the code are:

- `Periods`
- `LaurentSequence`
- `Diagonal`

These are defined in `src/PicardFuchs.m`.

The intended outputs are annihilating differential operators for:

- rational periods,
- generating functions of constant terms of Laurent powers,
- diagonals of rational functions.

This is already a signal that the natural generalization target is not only AG-specific period computation, but a broader holonomic-function / rational-integral engine.

## Mathematical Core Worth Extracting

There are four especially valuable layers.

## 1. Cohomological Reduction of Rational Forms

This is the mathematical heart of the package.

The repository contains a reduction layer labeled in the source as:

- "Reduction via Rham-Koszul à la Dimca"

This indicates an algorithmic reduction of rational differential forms modulo exact forms / Jacobian-type relations, in a way suitable for period computation.

### Why this is valuable

This reduction machinery is not tied only to the final annihilator computation.
It is useful as a standalone computational engine for:

- reduction of rational forms in de Rham cohomology,
- period computations,
- integration-by-parts style reductions,
- explicit Gauss-Manin experiments,
- diagonals and constant-term computations after geometric encoding.

### Generalization target

A modern system should expose this as a reusable cohomological reduction layer, rather than leaving it hidden inside a single monolithic period routine.

### Recommended module name

`sage.holonomic.periods.reduction`

## 2. Annihilators of Rational Periods

The top-level intrinsic

- `Periods(f : r := 1, variant := {}, onlyprep := false)`

takes a rational function and outputs an annihilating differential operator for its periods.

### Why this is valuable

This is the core computational objective: an exact operator satisfied by a period integral.

The key point is that the repository already frames this in a relatively abstract way: the object is not tied to a single geometric family or basis, but to a rational integrand and a distinguished parameter.

### Generalization target

A robust extracted package should provide something like:

- `annihilator_of_period(f, parameter=t)`
- `period_operator(f, parameter=t)`

with options for:

- exact symbolic computation,
- modular reconstruction,
- local singularity analysis,
- normal-form / monic normalization of the resulting operator.

### Recommended module name

`sage.holonomic.periods.annihilator`

## 3. Diagonals and Constant-Term / Laurent-Sequence Annihilators

The repository exposes:

- `LaurentSequence`
- `Diagonal`

as wrappers that transform a combinatorial / generating-function problem into a period problem and then call the same backend.

### Why this is valuable

This broadens the package from a pure AG tool into a general holonomic-function engine for special functions defined by:

- diagonals of rational functions,
- generating functions of constant terms,
- Apéry-style and lattice-walk style recurrences.

This is highly reusable and should be treated as a first-class extraction target.

### Generalization target

A modernized package should expose:

- `annihilator_of_diagonal(F, t)`
- `annihilator_of_constant_term(F, t)`
- `annihilator_of_laurent_sequence(F, t)`

all backed by the same reduction and reconstruction machinery.

### Recommended module name

`sage.holonomic.diagonals`

## 4. Modular Computation and Rational Reconstruction

The repository contains a nontrivial reconstruction layer over finite fields / modular data, later lifted back to characteristic zero.

### Why this is valuable

In practice, exact symbolic period computation over `QQ(t)` often becomes unusable without modular evaluation and rational reconstruction.

So this layer is important not just for this repository, but as generic infrastructure for:

- rational function reconstruction,
- polynomial matrix reconstruction,
- exact operator reconstruction from modular computations.

### Generalization target

This should be extracted as backend infrastructure usable by multiple packages, not only a period package.

### Recommended module name

`sage.experimental.reconstruction.modular`

## What Is Worth Extracting Only as Internal Infrastructure

The repository also contains polynomial linear algebra utilities that are clearly important, but mostly as supporting infrastructure:

- linearization of polynomial lists,
- polynomial echelon forms,
- relation matrices,
- row-space extraction.

These are useful because period algorithms often need custom linear algebra over polynomial/function-field objects rather than naive coefficient-vector expansions everywhere.

However, these should likely remain internal building blocks unless a broader use case emerges.

### Recommended module name

`sage.holonomic.periods.linear_algebra`

## What the Extracted System Should Mean by "Computing"

The extracted system should be explicit about what it computes.

### For a rational integral

Given a rational function in variables `(t, x_1, ..., x_n)`, computing means:

- constructing a differential operator in `t` annihilating the period integral,
- optionally certifying the operator through internal reduction and reconstruction checks,
- exposing singular points, indicial data, and local monodromy information where feasible.

### For a diagonal

Computing means:

- encoding the diagonal as a rational period,
- deriving a differential operator for its generating function,
- optionally extracting recurrences or asymptotic data from the operator.

### For a Laurent / constant-term sequence

Computing means:

- converting the constant-term generating function into the period formalism,
- computing its annihilating operator,
- optionally converting the differential equation into a recurrence.

## Best Generalization Target

The strongest extraction target is a package of the following shape:

- `sage.holonomic.periods`
  - annihilators of rational periods,
  - diagonals of rational functions,
  - constant-term / Laurent-sequence annihilators,
  - exact and modular backends,
  - local singularity analysis of resulting operators.

This would be a broader and more generally reusable package than an AG-only framing.

## Relation to `foliation.lib`

The natural overlap with `foliation.lib` is in the general area of periods and differential equations, but the two repositories are mathematically complementary.

### What `foliation.lib` is stronger at

- explicit Gauss-Manin connection matrices,
- Brieskorn-module computations,
- Hodge-theoretic interpretation,
- specialized computations for Fermat hypersurfaces and Hodge loci.

### What `periods` is stronger at

- direct annihilator computation for rational integrals,
- diagonals and Laurent sequences,
- modular / reconstruction-oriented algorithm design,
- a more holonomic-function style abstraction.

### Combined extraction opportunity

A mature system could combine both into a larger package with two complementary layers:

- a Gauss-Manin / Brieskorn / Hodge-theoretic layer,
- an annihilator / diagonal / holonomic layer.

These should share:

- polynomial reduction backends,
- modular reconstruction infrastructure,
- differential-operator infrastructure,
- local singularity and monodromy analysis tools.

## What Is Probably Not Worth Preserving Literally

The following should not be copied wholesale as end-user-facing design:

- Magma-specific packaging,
- current ad hoc `variant` switches in their present form,
- current preliminary implementation details,
- repository-local heuristics without reinterpretation and testing.

The README itself warns that the implementation is preliminary and likely buggy.

So the extraction should preserve the mathematics and the algorithmic structure, not the literal software form.

## Recommended Package Architecture

The following architecture is realistic:

- `sage.holonomic.periods.reduction`
- `sage.holonomic.periods.annihilator`
- `sage.holonomic.periods.linear_algebra`
- `sage.holonomic.diagonals`
- `sage.experimental.reconstruction.modular`

Optionally, in a larger merged effort with hypersurface-Hodge tooling:

- `sage.hodge.hypersurfaces.gaussmanin`
- `sage.hodge.hypersurfaces.brieskorn`
- `sage.holonomic.periods`

## Most Valuable Extraction Targets, Ranked

### Highest value

1. Cohomological reduction of rational forms.
2. Annihilator computation for rational periods.
3. Diagonal / constant-term annihilator wrappers.
4. Modular reconstruction backend.

### Medium value

5. Polynomial linear algebra layer as reusable internal infrastructure.

### Lower value

6. Current heuristics and Magma-specific packaging details.

## Most Likely To Become Robust General-Purpose Features

- Annihilators of rational periods.
- Annihilators of diagonals of rational functions.
- Constant-term / Laurent-sequence annihilator computation.
- Modular reconstruction infrastructure.

## Most Likely To Remain Specialized

- Geometry-specific interpretations of the resulting operators.
- Direct integration with deeper Hodge-theoretic structures, unless combined with `foliation.lib`-style machinery.

## Final Summary

There is absolutely something here worth extracting and generalizing.

The main thing worth preserving is:

- a general-purpose rational-period / diagonal annihilator engine built from
  - cohomological reduction of rational forms,
  - modular reconstruction,
  - and exact operator synthesis.

This is mathematically meaningful, algorithmically distinctive, and broadly reusable in explicit AG, special-function computation, combinatorics, and holonomic systems.

The correct target is not "port this Magma package as-is."
The correct target is a modern period/diagonal/holonomic subsystem for Sage that uses the ideas and structure of `periods` as one of its main mathematical inputs.
