# Homsets Sage Inventory

This inventory records Sage homset category surfaces.

## Sage Category Surfaces

| Sage surface | Source anchor | Method surface to represent |
| --- | --- | --- |
| `sage.categories.homsets.HomsetsCategory` | `sage/categories/homsets.py` | Functorial construction for `C.Homsets()`, default supercategory computation, `_test_homsets_category`, `base`, and named-class key routing through the base category. |
| `sage.categories.homsets.HomsetsOf` | `sage/categories/homsets.py` | Stub homset category for categories that have structure but no specialized homset category. |
| `sage.categories.homsets.Homsets` | `sage/categories/homsets.py` | Category of all homsets, supercategory `Sets()`, and generic homset parent method `is_endomorphism_set`. |
| `Homsets().Endset()` | `sage/categories/homsets.py`, nested `Homsets.Endset` | Endomorphism-set axiom; Sage adds `Monoids()` as an extra supercategory and provides parent method `is_endomorphism_set() -> True`. |
