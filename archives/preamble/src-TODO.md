# Outstanding architectural work

- [x] Audit remaining `refine()` calls against the architectural boundary: owned constructors build objects through cooperative `super()` calls; each leaf constructs only its immediate declared supercategory object; refinement is limited to constructor-computed membership in subcategories that add properties or axioms, and never supplies construction data after instantiation.
