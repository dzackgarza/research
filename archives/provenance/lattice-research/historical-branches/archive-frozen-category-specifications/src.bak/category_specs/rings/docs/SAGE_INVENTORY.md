# Rings Sage Inventory

This inventory records Sage ring-category and constructor surfaces.
It is source-facing: mathematical mappings belong in `MAPPING.md`; implementation status, blockers, and deferred work belong in Nimbalyst tracker items.

## Category Surfaces

| Sage surface | Sage vocabulary |
| --- | --- |
| `sage.categories.rings.Rings` | Root ring parent, element, morphism, homset, endset, and autset surfaces. |
| `sage.categories.commutative_rings.CommutativeRings` | Commutative rings, fields, integral domains, quotient fields, local rings, complete rings, and valuation refinements. |
| `sage.categories.fields.Fields` | Fields, finite fields, number fields, local fields, global fields, algebraically closed fields, and real/complex precision families. |
| `sage.categories.principal_ideal_domains.PrincipalIdealDomains` | PID-specific ideal, gcd, factorization, quotient, and module-construction surfaces. |
| `sage.categories.euclidean_domains.EuclideanDomains` | Euclidean-domain methods, quotient/remainder behavior, and gcd/lcm refinements. |

## Functorial and Construction Surfaces

These surfaces are category-level structure, not named ring constructors.

| Sage surface | Source anchor | Ring meaning to inventory |
| --- | --- | --- |
| `Rings().Homsets()` | inherited through `Objects.SubcategoryMethods`; ring morphisms constructed by `Rings.ParentMethods._Hom_` and Sage `RingHomset` classes | Sets of ring homomorphisms preserving addition, multiplication, zero, and one. Sage currently often categorizes ring homsets through lower algebraic supercategories rather than a ring-specific `Rings.Homsets` class. |
| `Rings().Endsets()` | inherited through `Objects.SubcategoryMethods` and generic `Homsets().Endset()` | Endomorphism sets of a ring object; Sage also exposes the public constructor `End(R)`. |
| Sage ring automorphism surfaces | generic homset/endset machinery plus concrete ring-family automorphism methods | Sage exposes ring homomorphism and endomorphism parents through generic homset machinery; concrete automorphism methods appear on ring families rather than as a separate inventoried `Rings().Autsets()` category. |
| `Rings().CartesianProducts()` | inherited from `Sets.SubcategoryMethods.CartesianProducts()` and Sage cartesian-product functorial machinery | Direct products of rings, with componentwise ring operations. |
| `Rings().Subquotients()` | inherited from `Sets.SubcategoryMethods.Subquotients()` | Constructive ring subquotients with ambient ring, lift, and retract. Quotient rings and subrings are special cases. |
| `Rings().Subobjects()` | inherited from `Sets.SubcategoryMethods.Subobjects()` | Subrings, ideals where the category context asks for ring objects, and other embedded ring objects. |
| `Rings().Quotients()` | inherited from `Sets.SubcategoryMethods.Quotients()` plus `Rings.ParentMethods.quotient`/`quotient_ring` | Quotient rings by ideals or congruence data, with the quotient map/retract semantics documented through subquotients. |
| `Rings().IsomorphicObjects()` | inherited from Sage `IsomorphicObjectsCategory` | Ring objects transported along ring isomorphisms; simultaneously subobjects and quotients in Sage's construction hierarchy. |
| `Rings().WithRealizations()` / `Rings().Realizations()` | generic realization category machinery | Ring parents with several concrete realizations or bases. The audited `Rings` category source adds no ring-specific realization parent methods beyond the generic construction surface. |

## Constructor Families

| Sage constructor family | Sage behavior or meaning |
| --- | --- |
| `ZZ`, `QQ`, `AA`, `QQbar`, `RR`, `CC`, `RDF`, `CDF`, `RIF`, `CIF` | Fixed singleton objects and precision-family ring objects. |
| `IntegerModRing`, `Zmod`, `Integers` | Integer-modulo ring categories, including finite and quotient-ring structure. |
| `GF`, `FiniteField` | Finite-field categories, including cardinality, characteristic, generator, and Conway/polynomial data where Sage exposes it. |
| `NumberField`, `QuadraticField`, `CyclotomicField` | Number-field categories with quadratic and cyclotomic refinements. |
| `PolynomialRing`, `PowerSeriesRing`, `LaurentSeriesRing`, `PuiseuxSeriesRing` | Ring constructors that also interact with algebra and module categories. |
| `MatrixRing`, `MatrixSpace` when square | Square matrix spaces with ring, algebra, and module category structure in Sage. |
| `Zp`, `Qp`, `Zq`, `Qq` | Valued, complete, discrete-valuation, and local field/ring categories. |

## Additional Sage Source Areas

- `sage/categories/rings.py` parent, element, morphism, homset, and quotient methods.
- `sage/rings/ideal.py` and concrete ideal families for ideal and quotient-ring surfaces.
- Sage ring-family sources for fields, number fields, finite fields, p-adic rings, polynomial rings, series rings, and matrix rings.
- Sage construction-category sources inherited by ring categories: subobjects, quotients, subquotients, isomorphic objects, Cartesian products, and realizations.
