# Rings Mapping

This file records the forward target mapping from Sage ring surfaces into the local
category-spec hierarchy. It is not a history of deleted files.

## Constructor Namespace

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| `Rings().NamedRings()` | `Rings().Constructors()` | Constructors are entry points into Sage objects, not mathematical subcategories. The target surface is an inner `Constructors` class on `Rings`. |
| Root shortcuts such as `Rings().ZZ()` | `Rings().Constructors().ZZ()` | Constructor shortcuts do not belong on the category root. The category root documents mathematics; `Constructors()` owns Sage entry points. |
| Parameterized families such as `RealField(prec)` and `Zp(p)` | Constructor methods returning objects refined into precision, valuation, or local-field subcategories | The parameterized family is not a one-object category; fixed objects such as `RR` and `CC` may have singleton refinements. |

Constructor signatures must follow Sage's documented input shapes. `PowerSeriesRing`,
`LaurentSeriesRing`, `PuiseuxSeriesRing`, and `MatrixRing` expose their structured
parameters directly. `PolynomialRing` exposes Sage's finite variable-specification
casework as overloads: `name`, `n` with `name`, `names`, `n` with `names`, single-count
`var_array`, and the names-external `n` form. Sage's higher-dimensional `var_array`
shape accepts an unbounded positional dimension list such as
`PolynomialRing(ZZ, 2, 3, 4, var_array='m')`; this pass does not admit that shape
because the public spec has no mathematical finite-indexing vocabulary for it yet. The
implementation may delegate to Sage's variadic factory, but the spec surface is closed
to the documented parameters: `base_ring`, `n`, `name`, `names`, `var_array`, `sparse`,
`order`, and `implementation`.

The remaining variadic ring factories are split as follows:

| Sage surface | Project surface | Decision |
| --- | --- | --- |
| `NumberField(polynomial, name, ...)` | `NumberField(polynomial, name, ...)` | Single defining polynomial route. Sequence-valued metadata is not accepted here. |
| `NumberField([f_1, ..., f_n], names, ...)` | `NumberFieldTower(polynomials, names, ...)` | Tower construction is a separate mathematical case with sequence metadata attached to the tower. |
| `Zp(p, prec=n, type=...)` / `Qp(p, prec=n, type=...)` | `Zp(p, prec=n, type=...)` / `Qp(p, prec=n, type=...)` | Scalar precision cap route. |
| `Zp(p, prec=(relative_cap, absolute_cap), type='lattice-*')` and `Qp` analogue | `ZpWithPrecisionCaps(...)` / `QpWithPrecisionCaps(...)` | Pair precision data is meaningful only for lattice precision, so it is named explicitly. |
| `Zp(p, prec=(default_prec, halting_prec, secure), type='relaxed')` and `Qp` analogue | `ZpRelaxed(...)` / `QpRelaxed(...)` | Relaxed arithmetic has default, halting, and security data; it is not a generic precision tuple. |
| `Zq(q, ...)` / `Qq(q, ...)` with integer prime power | `Zq(q, ...)` / `Qq(q, ...)` | Cardinality route. |
| `Zq((p, n), ...)` / `Qq((p, n), ...)` | `ZqFromPrimePower(p, degree=n, ...)` / `QqFromPrimePower(...)` | Prime-power pair route. |
| `Zq([(p, n)], ...)` / `Qq([(p, n)], ...)` | `ZqFromPrimePowerFactorization(factorization=...)` / `QqFromPrimePowerFactorization(...)` | Factorization route. |
| `Zq(..., prec=(relative_cap, absolute_cap), type='lattice-*')` and `Qq` analogue | Deferred admitted names `ZqWithPrecisionCaps(...)` / `QqWithPrecisionCaps(...)` | The split is mathematically meaningful, but installed Sage does not expose a working unramified extension parent for lattice precision caps. |
| `PowerSeriesRing(R, name, default_prec=...)` | `PowerSeriesRing(base_ring=R, name=..., default_prec=...)` | Univariate power-series route. Sage's deprecated positional precision route maps to the named `default_prec`. |
| `PowerSeriesRing(R, names=...)` or comma-separated/list names | `MultivariatePowerSeriesRing(base_ring=R, names=..., num_gens=...)` | Multivariate named-generator route. |
| `PowerSeriesRing(R, n, prefix, ...)` | `MultivariatePowerSeriesRingWithGeneratorPrefix(base_ring=R, prefix=..., num_gens=n, ...)` | Prefix-plus-count route. |
| `LaurentSeriesRing(PowerSeriesRing(...))` | `LaurentSeriesRingFromPowerSeriesRing(power_series_ring)` | Underlying power-series-ring route. |
| `PuiseuxSeriesRing(LaurentSeriesRing(...))` | `PuiseuxSeriesRingFromLaurentSeriesRing(laurent_series_ring)` | Underlying Laurent-series-ring route. |
| `MatrixSpace.matrix(x=None, **kwds)` | `zero_matrix`, `matrix_from_matrix`, `matrix_from_entries`, `matrix_from_rows`, `scalar_matrix` | The no-argument, matrix, flat-entry, row-entry, and scalar cases are separate element constructors. Sage's `coerce` keyword remains a named option on the data-bearing routes. |

Number-field methods with optional `v` are also split. `discriminant()` is the field
discriminant, while `trace_pairing_discriminant(elements)` is the determinant of the
trace pairing on supplied elements. `integral_basis()`, `ring_of_integers()`, and
`maximal_order()` are the full-order routes; the `v=p` and `v=[p_i]` Sage paths are
named `*_at_prime` and `*_at_primes`.

## Signature Typing Decisions

Ring dimensions, generator indices, generator counts, precisions, p-adic print bounds,
orders, degrees, and multiplicities are Sage integer quantities. The spec uses
`Integer` from `types.py` instead of accepting both native Python `int` and
`Integer`. Constructor bodies may still pass these values to Sage's factories, but the
category-spec surface is mathematically typed.

Matrix-ring diagonal construction takes a sequence of ring elements. The previous
`Any` surface hid the mathematical input: diagonal entries form an ordered finite
family in the base ring.

Precision-family identities are exact Sage identity facts, not informal equality:
`RR is RealField(53)`, `CC is ComplexField(53)`,
`RIF is RealIntervalField(53)`, and `CIF is ComplexIntervalField(53)` are true.
`RDF is RealField(53)`, `CDF is ComplexField(53)`, `RR is RDF`, and `CC is CDF`
are false. Thus `RR`, `CC`, `RIF`, and `CIF` may have fixed-object refinements,
while `RealField(...)`, `ComplexField(...)`, and related precision families remain
multi-object parameterized subcategories.

Sage p-adic `change(...)` calls split into mathematical operations. Precision changes
map to `change_precision(precision, precision_type=None)` on `Rings().Approximate()`.
Changing `type='capped-abs'` supplies the optional `precision_type`. Changing
`p=17` maps to `change_prime(17)` on p-adic rings and fields. Switching
`field=True` maps to `fraction_field()`. Print-mode changes are display interop and
use the private convenience method `_change_print_mode(print_mode)`.

## Subcategory Layout

| Current source surface | Target file organization | Rationale |
| --- | --- | --- |
| Ring family category surface | `subcategories/<mathematical_name>.py` or nested directories | Files should correspond to mathematical subcategories: `field.py`, `finite.py`, `integral_domain.py`, `valuation/`, `number_fields/`, and so on. |
| Approximate ring surface | `subcategories/approximate.py` | Precision control is common to real/complex precision families and p-adic rings/fields. The shared mathematical method is `change_precision`, not Sage's raw `change(...)` option bag. |
| Construction-category surface | `subcategories/constructions/<notion>.py` | Constructions such as subobjects, quotients, rings under, rings over, characteristic, and Krull dimension are attachable categorical constructions and are split by notion. |
| Matrix ring/algebra surface | `algebras` plus ring refinement | Matrix rings are algebras over their base ring and modules over that base. Algebraic methods belong in `algebras`; ring methods belong in `rings`; module methods belong in `modules`. |

## Construction-Category Mapping

| Sage surface | Target surface | Rationale |
| --- | --- | --- |
| `Rings().Homsets()` | `Rings().HomCategory()` in `rings/homsets.py` and top-level `homsets/` | Ring morphisms are structure-preserving maps. The ring-specific file declares ring-homomorphism vocabulary; the top-level hom category hierarchy owns generic hom/end/aut behavior. |
| `Rings().Endsets()` | `Rings().EndCategory()` plus generic end-category wiring | Endomorphism objects are `End(R) = Hom(R, R)`. The ring subtree specifies ring endomorphism methods without duplicating generic end-category logic. |
| Sage/project automorphism surfaces | `Rings().AutCategory()` with ring specialization | A ring automorphism object is the bijective part of `End(R)`. The target exposes this explicitly because `Aut` appears in Sage ring objects even when category-level wiring is inherited. |
| `Rings().CartesianProducts()` | `subcategories/constructions/cartesian_products.py` | A product of rings is a ring with componentwise operations. Signatures should use sequence vocabulary for the factors unless Sage source proves a different mathematical input shape. |
| `Rings().Subquotients()` | `subcategories/constructions/subquotients.py` | Quotients and subobjects share the ambient/lift/retract construction. Ring documentation must keep this parent construction visible instead of jumping directly to quotient rings. |
| `Rings().Subobjects()` | `subcategories/constructions/subobjects.py` | Ring subobjects are subrings in ring categories, not arbitrary subsets. Ideals belong to their own ring-side vocabulary when they are not themselves ring objects. |
| `Rings().Quotients()` | `subcategories/constructions/quotients.py` | Quotient rings are rings modulo ideals or congruences and should refine the subquotient surface. |
| `Rings().IsomorphicObjects()` | `subcategories/constructions/isomorphic_objects.py` | Transport of ring structure along an isomorphism is both subobject-like and quotient-like in Sage's construction hierarchy. |
| `Rings().WithRealizations()` / `Rings().Realizations()` | `subcategories/constructions/with_realizations.py` and `realizations.py` using the generic realization method surface | Realization categories are categorical structure for parents with several concrete models, not constructor namespaces. The audited `Rings` category source contributes no additional ring-only realization methods. |

`Rings().RingsOver(R)` and `Rings().RingsUnder(R)` own the ring-specific
`structure_ring()` and ring morphism `structure_map()` methods. Their old local
`structure_domain()` and `structure_codomain()` methods now map to the Cat-owned
universal structure-morphism surface through `structure_morphism().domain()` and
`structure_morphism().codomain()`.

## Deferred Q-Adic Lattice Precision

`ZpWithPrecisionCaps` and `QpWithPrecisionCaps` are concrete because Sage's `Zp` and
`Qp` base constructors canonicalize lattice precision pairs. The corresponding
unramified extension names `ZqWithPrecisionCaps` and `QqWithPrecisionCaps` are retained
as admitted split names, but their bodies assert the installed Sage gap instead of
passing through to a broken constructor path.

- Searched: `rings/docs/MAPPING.md`, `rings/docs/SAGE_INVENTORY.md`,
  `rings/smoketest.sage`, `rings/__init__.py`, Sage
  `sage/rings/padics/factory.py` around `get_key_base`, `Zq`, `Qq`, and
  `pAdicExtension_class`, Sage `sage/rings/padics/padic_extension_leaves.py`,
  Sage `sage/rings/padics/generic_nodes.py`, and Sage
  `sage/rings/padics/local_generic.py`. Runtime probes covered direct Sage
  `Zq(25, prec=4, type="lattice-cap", names="a")`,
  `Zq(25, prec=(4, 8), type="lattice-cap", names="a")`,
  `Qq(25, prec=4, type="lattice-cap", names="a")`,
  `Qq(25, prec=(4, 8), type="lattice-cap", names="a")`, the analogous
  `lattice-float` pair routes, `check=False` factorization routes, and explicit
  `Zp(..., type="lattice-cap").extension(...)` /
  `Qp(..., type="lattice-cap").extension(...)` routes.
- Found: Sage `Zp`/`Qp` base constructors canonicalize lattice precision pairs through
  `get_key_base`, and `pAdicLatticeGeneric` stores separate relative and absolute
  caps. Installed Sage `Zq`/`Qq` extension constructors document q-adic `prec` as an
  integer cap and coerce non-`Integer` precision with `prec = Integer(prec)` before
  calling `ExtensionFactory`. Direct q-adic pair precision fails with `TypeError:
  unable to coerce <class 'tuple'> to an integer`. Scalar lattice-cap q-adic routes
  and explicit lattice-base extension routes fail before returning a usable extension
  parent. The installed `ext_table` has unramified extension leaves for
  capped-relative, capped-absolute, fixed-modulus, and floating-point bases, but no
  lattice extension leaf keyed by `pAdicRingLattice` or `pAdicFieldLattice`.
- Conclusion: inference -- no real installed Sage construction path currently realizes
  unramified q-adic extensions with split lattice relative/absolute precision caps.
  These names remain deferred frontiers until Sage exposes an extension-specific
  lattice-precision route or an upstream fix.
- Confidence: High.
- Gaps: upstream Sage issue trackers, unreleased Sage branches, and Sage developer
  discussion were not searched in this pass; the conclusion is limited to the installed
  Sage source, installed written docs, and direct local runtime probes.

## Axiom vs. Implementation Decision

Use direct implementation categories only for genuinely computable implementation
targets, such as a concrete finite-field family or a future finitely generated free
module implementation over a PID. Use `with_axiom` restrictions for mathematical
adjectives that must attach to arbitrary ring subcategories, such as `Commutative`,
`Finite`, `Reduced`, or `Topological`.

## Topological Rings

Topological ring structure must inherit from the `topological_spaces` subtree for the
topological-space surface and from `rings` for ring operations. It should not duplicate
topological-space methods inside a ring-only file.
