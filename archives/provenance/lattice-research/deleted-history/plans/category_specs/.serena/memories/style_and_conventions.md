# Coding Style and Conventions

## Subcategory Hierarchy
- All named objects (e.g., `Primes`, `ZZ`, `Modules(R)`) should have a specific subcategory in the new hierarchy.
- Use the `_base_category_class_and_axiom` pattern for defining subcategories with axioms.

## Method Specification
- All methods specific to a mathematical structure (e.g., set-specific methods like `cardinality()`, ring-specific methods like `is_integral_domain()`) must be reflected as `abstractmethod` in the appropriate category's `ParentMethods`.
- Review existing SageMath implementations and documentation to ensure the spec is exhaustive.
- Differentiate between methods that depend only on the underlying structure (e.g., set methods vs. ring methods).

## Interoperability
- Operations should be non-destructive.
- Maintain interop with native SageMath categories without bypassing them.
- Syntax sugar (e.g., `ZZ^n`) should be overridden to return objects in the refined hierarchy.
