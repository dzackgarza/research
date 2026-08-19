# Category Specs Mypy Error Ledger

- source_artifact: `reports/workstreams/category-specs-mypy-structural-full/latest.json`
- structural_status: pass
- source_mode: all
- full_structural_mismatches: 0
- full_structural_missing_typeinfos: 0
- full_structural_projected_ancestor_missing_typeinfos: 0
- ordinary_error_count: 1740
- ignored_negative_control_count: 1

## Toolchain

- research_sha: `c3e276ba41168191a146c5a3fa8dc922f74a4307`
- plugin_sha: `322c1eb9174ca779c8d833ea855e6305d19cff04`
- sidecar_sha: `97ae58f07a403b650be8f62d0c4a1208925285d4`

## Counts By Owner

- research typing/design: 1275
- mathematical/category-interface question: 369
- mypy-plugin dynamic method-container inheritance: 96

## Counts By Code

- misc: 529
- override: 423
- list-item: 256
- arg-type: 235
- attr-defined: 98
- assignment: 57
- return-value: 45
- abstract: 41
- operator: 22
- call-arg: 13
- no-redef: 11
- return: 4
- call-overload: 3
- type-var: 2
- valid-type: 1

## Counts By Root Area

- rings: 439
- sets: 347
- modules: 277
- algebras: 223
- cat: 134
- posets: 97
- lattices: 62
- forms: 54
- topological_spaces: 50
- homsets: 35
- tensor_algebra_components: 20
- constructor_redefinitions.py: 2

## Representative Examples

- research typing/design / arg-type / cat: `category_specs/cat/base_category_types.py:474: error: Argument 1 to "__init__" of "Parent" has incompatible type "_CatObjectMixin"; expected "Parent"  [arg-type]`
- research typing/design / assignment / cat: `category_specs/cat/base_category_types.py:548: error: Incompatible types in assignment (expression has type "type | None", variable has type "type[Category_singleton]")  [assignment]`
- research typing/design / misc / cat: `category_specs/cat/base_category_types.py:593: error: Definition of "Hom" in base class "_CatObjectMixin" is incompatible with definition in base class "Category"  [misc]`
- research typing/design / override / cat: `category_specs/cat/base_category_types.py:602: error: Signature of "join" incompatible with supertype "sage.categories.category.Category"  [override]`
- research typing/design / list-item / cat: `category_specs/cat/join_categories.py:34: error: List item 0 has incompatible type "Cat"; expected "Category"  [list-item]`
- research typing/design / return-value / homsets: `category_specs/homsets/homsets.py:160: error: Incompatible return value type (got "HomCategory", expected "Category")  [return-value]`
- research typing/design / type-var / homsets: `category_specs/homsets/autsets.py:58: error: Value of type variable "_ParentT" of "refine_category" cannot be "UniversalAutObjectMethods"  [type-var]`
- mathematical/category-interface question / return / cat: `category_specs/cat/homsets.py:27: error: Missing return statement  [return]`
- mathematical/category-interface question / no-redef / cat: `category_specs/cat/__init__.py:162: error: Name "Hom" already defined (possibly by an import)  [no-redef]`
- mathematical/category-interface question / valid-type / cat: `category_specs/cat/__init__.py:163: error: Function "sage.structure.parent.Parent.Hom" is not valid as a type  [valid-type]`
- mathematical/category-interface question / misc / sets: `category_specs/sets/homsets.py:70: error: Cannot override final attribute "is_isomorphism" (previously declared in base class "_SetMorphisms")  [misc]`
- mathematical/category-interface question / attr-defined / modules: `category_specs/modules/subcategories/finitely_presented_over_pid.py:66: error: "Category" has no attribute "FinitelyPresented"  [attr-defined]`
- mypy-plugin dynamic method-container inheritance / misc / modules: `category_specs/modules/subcategories/constructions/quotients.py:80: error: Method "quotient_module" is marked as an override, but no base method was found with this name  [misc]`
- mathematical/category-interface question / abstract / sets: `category_specs/sets/__init__.py:317: error: Cannot instantiate abstract class "Modules" with abstract attributes "R", "torsion_module" and "zero_module"  [abstract]`
- mathematical/category-interface question / call-arg / sets: `category_specs/sets/__init__.py:654: error: Too few arguments  [call-arg]`
- research typing/design / operator / sets: `category_specs/sets/subcategories/infinite.py:36: error: Unsupported right operand type for in ("Infinite")  [operator]`
- mathematical/category-interface question / call-overload / algebras: `category_specs/algebras/__init__.py:532: error: No overload variant of "AssociativeAlgebras" matches argument type "_RingObjectMethods"  [call-overload]`
