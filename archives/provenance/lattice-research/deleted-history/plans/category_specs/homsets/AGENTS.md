# hom category subtree

This subtree owns the generic hom, end, and aut category specs.

Rules:

- Extend Sage's `sage.categories.homsets.HomsetsCategory`, `Homsets`, and
  `Homsets.Endset` through the registered re-exports in `category_specs.cat`; do not
  inherit raw Sage category bases directly or create a parallel model of hom categories.
- If a hom/end/aut failure suggests new local plumbing, first ask whether the object is
  using a raw Sage construction or the wrong base category. The intended solution is a
  Cat-native construction hierarchy that lets Sage mix in the declared method surfaces,
  not an additional dispatcher that imitates Sage's hom-category machinery.
- Domain, codomain, call, identity, composition, inverse, and invertibility are
  universal morphism/hom-category concerns. If they appear first or repeatedly in
  module, ring, set, or algebra hom-category subtrees, treat that as evidence that the
  generic `homsets.py`, `endsets.py`, or `autsets.py` file is missing the abstraction.
- Subtree hom-category specs own only the structure that first appears there. Set hom
  categories may declare that functions between sets are sets; module hom categories
  should focus on `R`-linearity, enrichment over `R-Mod`, algebra/ring structure on end
  categories, and representability of automorphism groups. They must not restate
  generic morphism mechanics.
- This is a mathematical separation, not a DRY rule. If a fact is true for every
  morphism, put it on the generic morphism/hom-category surface because that is where
  it is true. If a fact first becomes true for `R`-linear maps, ring maps, or
  continuous maps, put it in that subtree even if the implementation is inconvenient.
- Do not let set, module, ring, or algebra hom-category specs own the bare facts that
  `End(X)` is a monoid or `Aut(X)` is a group. Those are generic end/aut facts.
  Specialized subtrees may state the additional structure, such as `End_R(M)` as an
  `R`-algebra or `Aut_R(M)` as a representable matrix group when appropriate.
- Keep the three root spec categories in separate files:
  - `homsets.py` owns `HomCategory`, whose `ParentMethods` are hom specs and whose
    `ElementMethods` are morphism specs.
  - `endsets.py` owns `EndCategory`, defining only genuinely new end methods.
  - `autsets.py` owns `AutCategory`, defining only genuinely new aut methods.
- Use `C.HomCategory()` for the generic hierarchy internal to an arbitrary base
  category `C`. Evaluate it by `C.HomCategory().Of(A, B)`. Use
  `C.EndCategory().Of(A)` and `C.AutCategory().Of(A)` for end and aut objects.
- `HomCategoryOf`, `EndCategoryOf`, and `AutCategoryOf` are construction classes.
  These construction classes set supercategories so Sage mixes in the root specs.
- The generic method surfaces are public universal classes:
  `UniversalHomObjectMethods`, `UniversalHomElementMethods`,
  `UniversalEndObjectMethods`, `UniversalEndElementMethods`,
  `UniversalAutObjectMethods`, and `UniversalAutElementMethods`. Subtrees may
  extend these surfaces through category inheritance, but must not re-declare the same
  abstract method lower in an end/aut chain.
- Keep generic `Aut(X)` construction here. Subtrees must not recreate
  `ConditionSet`-based aut wiring.
- Subtree hom-category files inherit from `HomCategoryOf`, `GenericEndCategory`, and
  `GenericAutCategory`. They declare additional structure; they do not repeat generic
  identity, inverse, or invertibility plumbing.
- Sage still names the axiom hooks `Endset` and `Autset`; concrete hom category
  classes may attach `Endset = ...`, and concrete end category classes may attach
  `Autset = ...`, solely for `_with_axiom(...)` interop. Do not expose project-facing
  `Homsets()`, `Endsets()`, or `Autsets()` selectors.
- Subtree-specific files may add mathematical laws for their morphisms, such as set
  maps, ring homomorphisms, module homomorphisms, or algebra homomorphisms.
- A hom object has a domain and codomain. `End_C(A)` is `Hom_C(A, A)`. `Aut_C(A)` is
  the invertible part of `End_C(A)`.
- Element surfaces distinguish morphisms, endomorphisms, and automorphisms.
