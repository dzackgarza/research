
GOAL: record the entirety of the existing set of module methods as a proper set of ABC specs on specific sets of subcategories.
This should operate as a replacement for the categories SageX where X = FreeModule(...), CombinatorialFreeModule(...), etc, which operates non-destructively by intercepting and overwriting all constructors, using existing implementations wherever possible, and refining the results to lie in the new subcategory hierarchy.
Tasks:
    - Ensure all named constructors for all modules in sage appear as methods on Modules(R).NamedModules()
    - Ensure all known types of modules in the sage codebase map to a specific subcategory speccing their methods as ParentMethods, ElementMethods, MorphismMethods, etc.
    - Ensure there are constructions that regard rings R as rank 1 free R-modules, (fractional) ideals as submodules, invertible ideals as projective submodules, polynomial rings R[x_1,...,x_n] as R-modules, similarly for power series rings, matrix rings, and other constructions on rings
    - Ensure that all constructions in sage are collected onto this category, where one calls the existing sage constructor and refines the category of the result.
    - Ensure explicit interop with the new Rings subcategories, without bypassing and allow native sage categories.
    - Spot-check at runtime to find all methods on all constructible module objects in the codebase and docs, and ensure *all* module-specific methods are reflected in the spec as an abstractmethod in some subcategory's parentmethods (do not try to automate or script this, just manual checks)
    - Check all upstream concrete ring implementations for module-related methods and immediately downstream classes (e.g. lattices) and ensure they're all in the spec
    - Ensure that each of the 10+ named module constructors have a subcategory of rings that precisely corresponds to a subcategory in the new hierarchy speccing it.
    - Ensure basic syntax sugar is overridden so that if ZZ is the refined integer ring, then ZZ^n is in the refined free module category.
