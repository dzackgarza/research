# Lean and Sage realizations

Lean and Sage realize different parts of the mathematics defined in the theory chapters.
The current repository contains a Sage parity implementation and a separate Lean proof of
concept.

## Mathematical boundary {#sec-layering}

A realization cites the defining occurrence of each category, functor, form, or invariant
that it implements. Lean declarations formalize that definition or a stated
specialization. Sage classes and methods implement the corresponding exact computation.
A comparison requires an explicit mathematical statement relating the named Lean
declaration and Sage operation.

## Sage parity implementation {#sec-sage-parity-realization}

The maintained base experiment is
`computations/experiments/sage_lattice_category_spike`. Its public facade is
`lattice_categories.py`; its packages implement algebraic objects, forms, morphisms, and
lattice constructions. The generated
[SageMath category framework reference](../sage/Sage-Category-Framework-Inventory.md)
and [Sage category class catalogue](../sage/Sage-Category-Classes.md) describe the pinned
Sage reference surface used for parity comparisons.

## Lean proof of concept {#sec-lean-realization}

The experiment in `computations/experiments/lean_category_dsl_spike/catdsl_poc` uses
Mathlib's category theory. It defines bundled categories for its finite-field example,
registers distinguished functors, and elaborates object and view commands into ordinary
Lean declarations. [Lean categorical DSL proof of concept](Categorical-DSL.md) records
the implemented commands and their current limits.

## Comparison claims {#sec-registry-semantics}

A comparison between the two realizations names the Lean declaration, the Sage operation,
the mathematical statement relating them, and evidence for that statement. The
mathematical statement may assert equality of exact outputs, compatibility with a
specified functor, or agreement after a named normalization. The category and functor
diagram records the categories and functors involved. Each comparison requires separate
evidence.

## Proof and computation {#sec-cop-out-visibility}

Commutativity, naturality, universal properties, and equivalences are theorem statements.
Finite examples test an implementation but do not prove those statements. A Sage result
with a compact certificate may be checked by Lean or by another specified certified
procedure. A result without such a check remains a computation.
