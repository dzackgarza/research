# Modules Triage

Source: `sage /home/dzack/research/plans/category_specs/modules/smoketest.sage`

This file records the module-side failures exposed by the current smoke test. Most module constructors currently fail during refinement because the refined object does not implement `Aut`. A smaller number fail for distinct structural reasons.

## Broad blocker: missing `Aut`

These constructors fail with `AssertionError: Not implemented method: Aut`.

- `Modules(Zmod(6)).NamedModules().FreeModule(2)`  
  Category target: `FreeModulesWithStandardBasis`
- `Modules(ZZ['x']).NamedModules().FreeModule(2)`  
  Category target: `FreeModulesOverIntegralDomains`
- `Modules(ZZ).NamedModules().FreeModule(2)`  
  Category target: `FreeModulesOverPIDs`
- `Modules(QQ).NamedModules().VectorSpace(2)`  
  Category target: `VectorSpaces`
- `refine_category(FreeModule(RDF, 2), Modules(RDF).NamedModules().RealDoubleVectorSpaces())`
- `refine_category(FreeModule(CDF, 2), Modules(CDF).NamedModules().ComplexDoubleVectorSpaces())`
- `refine_category(V.subspace(...), Modules(QQ).NamedModules().VectorSubspaces())`
- `refine_category(V.subspace_with_basis(...), Modules(QQ).NamedModules().VectorSubspacesWithOrderedGeneratingSet())`
- `refine_category(V.quotient_module(W), Modules(QQ).NamedModules().VectorSpaceQuotients())`
- `Modules(ZZ).NamedModules().FreeQuadraticModule(2, matrix(ZZ, [[2, 1], [1, 2]]))`
- `Modules(QQ).NamedModules().CombinatorialFreeModule(['a', 'b'])`
- `Modules(QQ).NamedModules().FiniteRankFreeModule(2)`
- `refine_category(M.submodule(...), Modules(ZZ).NamedModules().FreeModuleSubmodules())`
- `refine_category(M.submodule_with_basis(...), Modules(ZZ).NamedModules().FreeModuleSubmodulesWithOrderedGeneratingSet())`
- `refine_category(M.quotient_module(S), Modules(ZZ).NamedModules().FreeModuleQuotients())`
- `refine_category(C.submodule([a + b]), Modules(QQ).NamedModules().SubmodulesWithOrderedGeneratingSet())`
- `refine_category(C.quotient_module(CS), Modules(QQ).NamedModules().QuotientModulesWithOrderedGeneratingSet())`
- `refine_category(SymmetricGroup(3).regular_representation(QQ), Modules(QQ).NamedModules().RepresentationModules())`
- `refine_category(M / W, Modules(ZZ).NamedModules().FinitelyGeneratedPIDQuotientModules())`
- `Modules(GF(5^3)).NamedModules().OreQuotientModule(S, X^2 + z)`
- `Modules(ZZ).NamedModules().IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]])`
- `Modules(ZZ).NamedModules().TorsionQuadraticForm(matrix(QQ, [[1, 1/2], [1/2, 1]]))`

At the moment this single abstract-method gap blocks most of the module subtree from reaching any more specialized validation.

## Graded-module base-category mismatch

These constructors fail with:

`AssertionError: base category class for sage.categories.graded_modules.GradedModules mismatch; expected sage.categories.modules.Modules, got category_specs.modules.Modules`

- `Modules(ExteriorAlgebra(QQ)).NamedModules().FreeGradedModule(E, (-1, 3))`
- `Modules(ExteriorAlgebra(QQ)).NamedModules().FPModule(E, [0, 1], [[x, 1]])`

This is not a missing-method failure. It is a category-construction mismatch between Sage's graded-module functorial machinery and the replacement `category_specs.modules.Modules` root.

## Ring-object-as-module failure inherited from ring refinement

This constructor fails with `AssertionError: Not implemented method: is_algebraically_closed`.

- `Modules(ZZ).NamedModules().polynomial_ring_as_module('t')`

This failure comes from refining the underlying polynomial ring object, not from a module-specific method gap.

## Consequence

The module subtree currently has three distinct blockers:

- one dominant abstract-method gap, `Aut`
- one functorial-category incompatibility, `GradedModules`
- one inherited ring-side gap, `is_algebraically_closed` on ring objects viewed as modules

The `Aut` surface is the first blocker to remove if the goal is to expose the next layer of module-specific missing methods.
