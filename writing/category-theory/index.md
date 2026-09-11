# Categorical and arithmetic foundations

Categorical and arithmetic foundations support the lattice research code, its Sage implementation, and its Lean formalization.

The three parts are a single chain, and each one is used by the next.

**Foundations** fixes the setting: higher categories and universes, the categorical constructions, truncation and the classifiers that both limits and monoidal structure are stated with, limits and colimits, loops and suspension, and what an identification and an equality are.

**Algebraic structure** builds algebra on that setting: categories presented by operations, monoidal structure and the internal algebraic objects it carries, modules and base change, generating families and presentations, joins meets and closure, the distinguished functors, elements and containment, and generic elements with their hypotheses and localization.

**Forms, lattices, and Witt theory** is one dependency chain in its own order.
A bilinear or quadratic form comes first, then forms on the underlying module of an algebra, then a lattice and its discriminant form, then isometries and arithmetic invariants, then Coxeter systems.
The hyperbolic form and the Witt class follow, then the stable category of modules with duality the Witt class lives in, and finally the morphisms and the chain complexes built over that category.

**Realizations** is the generated category and functor diagram.
**Authoring and reference** holds the mathematical language style guide and the sources the framework draws on.
