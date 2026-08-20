# Owned mathematical category hierarchy

- The preamble owns every mathematical category and every mathematical inclusion.
- Sage supplies `Category`, `Parent`, `Element`, `Homset`, `Morphism`, coercion, dynamic method installation, refinement, joins, and construction-class generation.
- Native Sage categories are implementation providers and compatibility tags only.
- Do not use native Sage categories as mathematical supercategories.
- Delegate computational algorithms directly to Sage implementations.
- Do not copy Sage algorithms into the preamble.
- Retain `SageSets()` only where `Parent._init_category_` requires it.
- Treat this `SageSets()` link as runtime compatibility, not mathematical ownership.
- Do not replace dynamic refinement with wrapper objects.
- Do not remove Sage runtime machinery unless the replacement preserves object identity, native hom-sets, coercion, and dynamic refinement.
