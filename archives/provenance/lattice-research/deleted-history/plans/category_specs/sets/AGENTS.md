
GOAL: map the existing collection of set methods into mathematical category specs on
specific subcategories.
This should operate as a replacement for the categories SageX where X = Sets, FiniteEnumeratedSets, etc, which operates non-destructively by intercepting and overwriting all constructors, using existing implementations wherever possible, and refining the results to lie in the new subcategory hierarchy.
Tasks:
    - Ensure all named sets have a specific one-object subcategory speccing their methods, e.g. Sets().Primes() = {P} is the one-object category whose one object is sage's current implementation of the set of primes, refined into the new set subcategory hierarchy.
    - Find and list all named Sage set constructors X and expose
      Sets().Constructors().X() to return the corresponding refined set object.
    - Spot-check at runtime to find all methods on these set objects, and ensure every
      mathematically meaningful set-specific method is represented in the spec or
      explicitly mapped to inventory-only in `docs/MAPPING.md` (do not try to automate
      or script this, just manual checks)
    - Do not add Sage fallback/cache helpers or enumeration convenience names as
      project abstract methods when standard iteration, indexing, rank, cardinality, or
      Python conversion protocols recover the behavior.
    - This requires reviewing code: ring-theoretic methods do not go here, only methods that only depend on the underlying set, e.g. cardinality()
    - Check all upstream concrete ring implementations for set-related methods and ensure they're all in the spec
    - Check all upstream set-specific subcategories and ensure their methods/properties/etc are represented in this subcategory hierarchy
    - Ensure that each of the 10+ named set constructors have a subcategory of sets that precisely corresponds to a subcategory in the new hierarchy speccing it.
    - Ensure all axioms are composable and mathematically meaningful, and chained appropriately to define subcategories, using the same _base_category_class_and_axiom pattern used in modules.
