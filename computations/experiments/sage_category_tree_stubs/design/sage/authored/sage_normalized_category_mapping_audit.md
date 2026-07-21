# Sage-to-normalized category mapping audit

Source scope: SageMath 10.9 at commit `686dc1a…`; runtime comparison 10.10.beta0.

## Coverage

- 179 of 179 public named categories and category-valued wrappers mapped.

- 43 non-public source classes explicitly dispositioned: 38 framework helpers, 4 test fixtures, and 1 example category.

- 51 Sage axiom names crosswalked.

- 17 Sage functorial constructions crosswalked.

- 66 distinct normalized base categories/families; 62 are standard named mathematical categories/constructions and 4 are explicit exceptions or parameter/compatibility cases.

- Confidence: 174 high, 3 medium, 2 review-required.

## Governing mapping rule

Each public Sage category maps to a named normalized base and an ordered list of classifier applications.
Implicit targets are finite-limit expressions and need not be named nodes.
The constructibility checker derives canonical support maps from the normalized graph, applies pullback-cone rules, and iterates to a fixed point.

## Required corrections highlighted by the ledger

- `UnitalAlgebras` means possibly nonassociative unital algebras; Sage `Algebras` maps to associative-unital algebras.

- Normalized `Modules(R)` means left modules; right modules are `Modules(Rᵒᵖ)`. Sage `Modules(R)` needs a commutative/symmetric-usage guard.

- `FiniteDimensional` maps to `FiniteRank`; `Finite` remains literal underlying-set finiteness.

- `DivisionRings := Rings.Division`, not a raw inverse axiom on all magmas.

- Lattice distributivity and two-operation distributivity are distinct host-qualified classifiers.

- `Facade` and most non-public framework classes are implementation metadata, not new mathematical categories.

- The common complex-reflection/generalized-Coxeter class is retained as the transparent exceptional host `GroupsWithSimpleReflections`.

- Sage `Groupoid(G)` remains a reviewed provisional fiber `GroupoidsOn(G)` because its own source marks the definition as unresolved.

## Review-required rows

- **FunctionFields** (medium): Sage declares an unparameterized subcategory of Fields.
  Keep FunctionFields as the standard named target; later refine the classifier by constant field/transcendence-degree conventions.

- **Groupoid** (review): Sage's source explicitly marks the definition and relation with the standard notion of groupoid as FIXME; its sole parent is Sets.
  Do not silently map it to the full category Groupoids.

- **KahlerAlgebras** (medium): KählerPackage is enabled only after WithBasis, Graded, and FiniteRank have been imposed; it abbreviates Poincaré duality, hard Lefschetz, and Hodge–Riemann relations.

- **MatrixAlgebras** (medium): Interpreted as algebras isomorphic to a full matrix algebra (possibly with chosen matrix presentation); Sage's category is intentionally broad and dimension-unspecified.

- **Modules** (review): For noncommutative R, Sage Modules(R) is not a reliable synonym for normalized left Modules(R); the adapter must inspect/limit the parameter or map to the appropriate symmetric-bimodule refinement.

## Base-name audit

All ordinary bases are either standard categories/families (`Sets`, `Rings`, `Modules(R)`, `Crystals`, `Schemes(S)`, etc.) or standard construction-defined categories (`Homsets(C)`, `ChainComplexes(C)`, ideals, group algebras).
The only deliberate descriptive hosts are `MagmasWithTwoOperations` and `GroupsWithSimpleReflections`; both are required as least classifier hosts and are defined by transparent mathematical data.
`AmbientObjects` is compatibility-only, and `GroupoidsOn(G)` is provisional.

See the workbook and JSON manifest for row-level sources, route selectors, classifier hosts, current-DOT status, and exception notes.
