# Autset Integration Plan

## Overview

This document outlines a systematic approach to integrate **autset** categories into
SageMath's categorical framework, aligning with the existing homset/endset hierarchy.

## Structural Hierarchy

```
Homsets  →  Endsets (axiom: Endset, extra_super: Monoids)
                  →  Autsets (axiom: Autset, extra_super: Groups)
```
- **Endsets** represent endomorphism monoids.
- **Autsets** represent groups of invertible endomorphisms (automorphism groups).

## Implementation Steps

### 1. Register the `Autset` Axiom

- **Location**: `src/sage/categories/category_with_axiom.py`
- **Action**: Add `"Autset"` to `all_axioms` after `"Endset"` in the ordering.
- **Impact**: Enables the axiom system to recognize autsets as a distinct categorical
  concept.

### 2. Define Autset Category Within Endsets

- **Location**: `src/sage/categories/homsets.py`
- **Structure**:
  ```python
  class SubcategoryMethods:
      def Autset(self):
          return self._with_axiom("Autset")

  class Autset(CategoryWithAxiom):
      def extra_super_categories(self):
          from .groups import Groups
          return [Groups()]  # Every autset is a group under composition
  ```
- **Rationale**: Mirrors the relationship where `Endset.extra_super_categories` returns
  `[Monoids()]`.

### 3. Per-Category Specialization

- **Location**: Category-specific modules (e.g., `Modules`, `AbelianVarieties`)
- **Action**: Override `extra_super_categories` in nested `Autset` classes to encode
  domain-specific algebraic structure.
  - Example: `Modules(R).Homsets().Endset().Autset()` could return `[UnitsOfRing]` or
    similar specialized constraints.
  - Example: `AbelianVarieties(k).Homsets().Endset().Autset()` could return
    `[FiniteGroups]` for finite fields.

### 4. Representation Handling

- **Location**: `_repr_object_names_static` handling
- **Action**: Add a rule replacing `"endsets"` with `"autsets"` analogous to the
  existing `"homsets"` → `"endsets"` replacement.

### 5. Top-Level `Aut()` Function

- **Location**: `src/sage/categories/homset.py`
- **Implementation**:
  ```python
  def Aut(X, category=None):
      return Hom(X, X, category).autset()
  ```
- **Function**: Returns the autset subcategory (invertible elements) of an endset.

### 6. Refactor Existing Automorphism Implementations

- **Target Classes**:
  - `FreeModuleLinearGroup` (`src/sage/tensor/modules/free_module_linear_group.py`)
  - `AbelianGroupAutomorphismGroup` (`src/sage/groups/abelian_gps/abelian_aut.py`)
  - `FiniteFieldHomset` (`src/sage/rings/finite_rings/homset.py`)
- **Refactoring Goals**:
  - Change category assignment from `Groups()` to `SomeCategory().Endsets().Autsets()`
 - `extra_super_categories` for automatic group structure
  - Ensure proper `domain()` and `codomain()` pointing to the acting object
  - Enable categorical coercion maps `Aut(M) → End(M)`
  - Make `Aut(M)` return the same object as `M.automorphism_group()` via
    `UniqueRepresentation`

### 7. Categorical Coercions

- **Implementation**: Use categorical `_coerce_map_from_` mechanisms instead of ad-hoc
  overrides.
- **Benefit**: Cleaner integration with the category framework and automatic adherence
  to algebraic laws.

## Key Files to Modify

1. `src/sage/categories/category_with_axiom.py` - Add `"Autset"` axiom
2. `src/sage/categories/homsets.py` - Define `Autset` category and `Aut()` function
3. Category modules with `Homsets.Endset` specializations (e.g.,
   `src/sage/categories/modules.py`, `src/sage/categories/schemes.py`)
4. Representation utilities (`_repr_object_names_static`)
5. Automorphism group implementations in:
   - `src/sage/tensor/modules/free_module_linear_group.py`
   - `src/sage/groups/abelian_gps/abelian_aut.py`
   - `src/sage/rings/finite_rings/homset.py`

## Verification Strategy

- Ensure existing automorphism group functionality remains intact
- Verify that new autset categories properly inherit algebraic structures
- Test categorical coercions and dispatch mechanisms
- Validate that representation strings correctly reflect autset contexts

## Dependencies

- Requires proper implementation of `CategoryWithAxiom` pattern
- Relies on existing `Endset` infrastructure
- Needs coordination with `SubcategoryMethods` and axiom registration system
