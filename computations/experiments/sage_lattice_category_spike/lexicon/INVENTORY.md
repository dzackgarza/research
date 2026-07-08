# Lexicon Inventory

The single catalogue of the spike's typed mathematical language: every noun the code is allowed to use in a signature, where it is defined, how it is represented, and what Sage object realizes it.
This document is normative for *names and placement*; the type definitions themselves live in the sibling modules and in `typings/sage/` (see `README.md` for the layout and rules).

Status legend used throughout:

- **canonical** — defined in this subtree; downstream code should draw from here.
- **owned elsewhere** — defined in `algebra/domain_algebra.py` (the lattice DSL proper), re-exported here so the lexicon is the one import surface.
- **defect** — an existing construct this catalogue supersedes; listed with the evidence so remediation is a lookup, not an investigation.

* * *

## Part I — Audit of the current type surface (2026-07-08 sweep)

Ground truth: `mypy --strict --ignore-missing-imports --follow-imports=silent` over the package finds 1055 errors in 24 files; 148 of them are in package (non-test) code.
They decompose into five defect classes, all structural:

### I.1 Sage is untyped, so every boundary is `Any`

29 `[misc]` errors of the form `Class cannot subclass "Parent" (has type "Any")` (`objects/parents.py:110`, `objects/elements.py:19`, `objects/categories.py:124` and 15 sibling category classes, `forms/discriminant.py:188`), and 36 `[no-any-return]` errors wherever a Sage value flows back out of a typed signature.
No amount of annotation inside the package can fix this: the meaning of `Parent`, `Element`, `Matrix`, `Integer` is owned by Sage, and mypy sees `Any`. The only correct fix is a stub tree for the `sage.*` modules the package imports — that is `../typings/sage/` (a sibling of this package; see README).

### I.2 Hand-written partial protocols drift into golfing

`domain_algebra.py` declares structural protocols for Sage objects and grows them one method at a time as call sites demand:

- `SageRing` (`domain_algebra.py:178`) — 7 methods, described in its own docstring as "the finite union of Sage ring classes" but implemented as a protocol, so it captures neither the union nor the interface.
- `SageFreeModule` (`domain_algebra.py:202`) — 3 methods, while `objects/parents.py` calls `basis_matrix`, `base_ring`, `gen`, `is_submodule`, `intersection`, `saturation`, `index_in`, `quotient`, `submodule`, `dimension` on values of this type → 15 `[attr-defined]` errors.
- `MatrixGroupLike`, `PermutationGroupLike`, `FundamentalChamberLike` (`domain_algebra.py:159-175`) — near-empty placeholder facades.

Each new method call forces a protocol patch.
That is remediation drifting into type-system golf: the protocol chases the interface instead of the type being the interface.
Superseded by real Sage classes from `typings/sage/` (`interop.py` names them); `FundamentalChamberLike` was a placeholder for a type that simply did not exist yet and is superseded by `geometry.Polyhedron`.

### I.3 Invented engineering mangles of mathematical terms (neuralese)

The underlying classes have correct mathematical names; the mangles are manufactured at import and mixin sites:

- `Lattice as LatticeCarrier`, `NondegenerateLattice as NondegenerateCarrier`, … — ten aliased imports in `objects/parents.py:50-79` and eleven in `objects/categories.py:35-81`. A "LatticeCarrier" resolves to the class installed as `ParentMethods` on the category of lattices — i.e. it is literally a `Lattice`. The suffix encodes an implementation role (this class is copied into a dynamic parent class), which is invisible to a reader and false as mathematics.
- `_PositiveDefiniteKernelHost`, `_DefiniteKernelHost`, `_RootGeneratedHost` (`objects/parents.py:809-821`) — TYPE_CHECKING-conditional base aliases.
- `_carrier_delta` (`objects/categories.py:113`) — projects a class's own attributes for Sage's category injection.

Rule (Part IV): types in signatures are mathematical nouns.
Implementation-role vocabulary (`Carrier`, `Host`, `Kernel`, `Delta`) never appears in a type name.
The import-alias layer is unnecessary once the lexicon is the import surface: `from ..lexicon import Lattice` and use the name `Lattice`.

### I.4 Broken typing constructs in the central module itself

`domain_algebra.py` does not pass `mypy --strict` on its own:

- `GramMatrix = NewType("GramMatrix", MatrixLike)` and `MorphismMatrix` (`domain_algebra.py:145,149`) — `NewType` over a Protocol is invalid (`[misc]` × 2).
- `ExactScalar = NewType("ExactScalar", ExactScalarBase)` (`domain_algebra.py:152`) with `ExactScalarBase = int | Integer | Rational` under TYPE_CHECKING — `NewType` over a union is invalid (`[valid-newtype]`), and the runtime/`TYPE_CHECKING` fork means the checked type and the runtime type disagree.

Superseded: with real stubs, `ExactScalar` is the plain union `Integer | Rational` (`foundations.py`) and `GramMatrix` is a `NewType` over the real (subclassable) `Matrix` class.
`MorphismMatrix` is retired entirely (ratified 2026-07-08): a morphism and a matrix are different things — the matrix expressing a morphism in bases is an ordinary `Matrix`, and the validated-morphism witness is the `LatticeMorphism` object itself, so a "MorphismMatrix" type is a category error, not vocabulary.

### I.5 Missing vocabulary forces `Any`

`algebra/arithmetic.py` (`named_gram`, `as_square_qq_matrix`, `rational_mod`) and `algebra/value_objects.py` (`value_module` and friends) return `Any` because no `Matrix`, `Rational`, or `QmodnZ` noun existed to name the returns.
Every future module touching a graph, polytope, symbolic constant, real number, or permutation group would hit the same wall.
Part II fills the catalogue so `Any` is never the reachable spelling.

* * *

## Part II — The catalogue

Representation vocabulary used below:

- *alias* — `Name = SageClass` (or `type Name = ...` union).
  The semantic noun **is** the Sage implementation type; tightest possible contract, follows the ratified preference for tying types to real implementations.
- *union* — enumerated union over the Sage implementation classes in play.
  Sage's class inventory is stable on the timescale of this research; extend the union when a new implementation class actually enters the repo.
- *owned class* — a class this repo defines (the lattice DSL). The lattice-side classes double as category `ParentMethods` (the single-source design of `domain_algebra.py`).
- *NewType* — a parse-witness: same runtime object, but the type records that a codec has validated it.

### II.1 Foundations (`foundations.py`)

| Name | Meaning | Representation | Sage realization |
| --- | --- | --- | --- |
| `Integer` | element of ℤ, exact | alias | `sage.rings.integer.Integer` |
| `Rational` | element of ℚ, exact | alias | `sage.rings.rational.Rational` |
| `RealNumber` | element of ℝ (mpfr, *inexact*: display/plot boundaries only — never in exact arithmetic; repo policy bans floats in domain signatures) | alias | `sage.rings.real_mpfr.RealNumber` |
| `ExactScalar` | exact scalar of a ℤ/ℚ computation | union `Integer \| Rational` | — |
| `SymbolicExpression` | exact symbolic value (π, e, Γ-expressions; e.g. `gaussian_heuristic`) | alias | `sage.symbolic.expression.Expression` |
| `SignaturePair` | Sylvester pair (p, n) | `tuple[int, int]` | — |
| `CartanType` | simply-laced Cartan datum | `tuple[Literal["A","D","E"], int]` | — |
| `Set` | unordered mathematical set | alias `collections.abc.Set` | — |
| `OrderedSet` | set with a distinguished linear order (bases, generator tuples) | alias `Sequence` (uniqueness is the constructor's contract, not the type's) | — |

Superseded defects: `ExactScalar` NewType (I.4); the `int`-vs-`Integer` runtime fork.

### II.2 General algebra (`algebra.py`)

Semantic nouns.
The preferred representation is **category-first** (ratified 2026-07-08): a *kind of parent* is typed as the Sage category's `ParentMethods` (`Ring = Rings.ParentMethods`). Sage realizes category methods by *copying* them into dynamic parent classes, so the stub tree declares the mathematically true MRO edge on each implementation class it stubs — every implementation Sage codes correctly then satisfies the type for free (ℤ_p, ℝ, ℂ arrive by stubbing their classes with the same edge, not by type migration).
Where a Sage implementation *fails to opt into its category* (a known Sage defect class), that edge case gets the documented enumeration union (or an inspection-based protocol) instead — catalogued per noun.
Element kinds use the real cdef hierarchy (`RingElement`, `ModuleElement`), which every implementation genuinely inherits, in preference to `ElementMethods`.

| Name | Meaning | Representation | Sage realization |
| --- | --- | --- | --- |
| `Ring` | ring parent | **category** | `Rings.ParentMethods` (stub MRO opt-in per implementation class) |
| `Field` | field parent | **category** | `Fields.ParentMethods` |
| `BaseRing` | ring a lattice is based over — any ring; the v1 ℤ/ℚ restriction is the codec's runtime contract, not the type's | alias of `Ring` | — |
| `RingElement` | element of a ring | alias | `sage.structure.element.RingElement` |
| `Module` | R-module | alias | `sage.modules.free_module.FreeModule_generic` ∪ `TorsionModule` |
| `ModuleElement` | element of a module | alias | `sage.structure.element.ModuleElement` |
| `FreeModule` | free R-module with distinguished basis | alias | `FreeModule_generic` |
| `VectorSpace` | free module over a field | alias | `sage.modules.free_module.FreeModule_generic_field` |
| `TorsionModule` | finitely generated torsion module over a PID | alias | `sage.modules.fg_pid.fgp_module.FGP_Module_class` |
| `Vector` | element of a free module | alias | `sage.modules.free_module_element.FreeModuleElement` |
| `Matrix` | matrix over an exact ring | alias | `sage.structure.element.Matrix` |
| `AbelianGroup` | additive abelian group in play | union | `FGP_Module_class \| QmodnZ` (owned finite quotients are `FiniteAbelianGroup`) |
| `FiniteAbelianGroup` | finite abelian group with the full structure vocabulary (invariants, primary parts, subgroup lattice) | alias of owned class | `domain_algebra.DiscriminantForm` (base class: the pure group layer, no form) |
| `Group` | group object in play | union | `IsometryGroup \| IsometrySubgroup \| DiscriminantOrthogonalGroup \| MatrixGroup \| PermutationGroup` |
| `GroupElement` | element of a group in play | union | `LatticeMorphism \| DiscriminantAction \| sage.structure.element.MultiplicativeGroupElement` |
| `MatrixGroup` | finitely generated matrix group (GAP seam) | alias | `sage.groups.matrix_gps.finitely_generated_gap.FinitelyGeneratedMatrixGroup_gap` |
| `PermutationGroup` | finite permutation group (GAP seam) | alias | `sage.groups.perm_gps.permgroup.PermutationGroup_generic` |
| `QuotientRing` | ℤ/nℤ | alias | `sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic` |

Ontology note (ruling 2026-07-08): `FiniteAbelianGroup` and `DiscriminantForm` are *different objects* — the first lives in the category of torsion ℤ-modules (a group G; the runtime base class of the tower, renamed in M4), the second in a category of pairs (G, b) or (G, q). The bare noun `DiscriminantForm` is therefore DEPRECATED: it survives only as a compatibility alias in `domain_algebra`, and each annotation site must migrate to the object it means.
Moreover the two form theories are distinct: over ℤ, discriminant *bilinear* forms and discriminant *quadratic* forms are qualitatively different and not always interchangeable (Sterk, symmetric forms book — Zotero bibkey to be attached), so form-carrying sites choose `BilinearDiscriminantForm` or `QuadraticDiscriminantForm` deliberately; the subclass edge Quadratic → Bilinear encodes only that q induces its polar b, never that the theories coincide.

Superseded defects: `SageRing` protocol (I.2 — replaced by the `Ring`/ `BaseRing` unions over real classes); `MatrixGroupLike`/`PermutationGroupLike` facades.

### II.3 Lattice theory — the owned tower (re-exported; owned elsewhere)

Defined in `algebra/domain_algebra.py`, re-exported by `lexicon/__init__.py`. The names are already mathematical; the lexicon adds nothing but the single import surface.
(This is the vocabulary that must *never* be aliased into `*Carrier` spellings again.)

Objects: `Lattice`, `NondegenerateLattice`, `IntegralNondegenerateLattice`, `DefiniteLattice`, `PositiveDefiniteLattice`, `IndefiniteLattice`, `HyperbolicLattice`, `RootGeneratedLattice`, `LatticeElement`.

Morphisms and homs: `LatticeMorphism`, `LatticeHomset`, `LatticeSimilarity`. `LatticeSimilarity` (name ratified 2026-07-08) is a *similitude*: a map with `b(f x, f y) = λ·b(x, y)` for a fixed multiplier λ (O'Meara, Introduction to Quadratic Forms, §42; λ = 1 recovers isometry; distinct from a homothety `x ↦ λx`, which multiplies the form by λ²). Its role here is mostly a convenient generalization for discussing symmetric and skew-symmetric forms at once.

Isometry: `IsometryGroup`, `IsometrySubgroup`, `DiscriminantOrthogonalGroup`, `DiscriminantAction`.

Finite forms: `DiscriminantForm`, `BilinearDiscriminantForm`, `QuadraticDiscriminantForm`, `SourcedDiscriminantForm`, `DiscriminantFormElement`, `DiscriminantSubgroup`.

Genus: `Genus`.

Boundary codecs: `RawGramMatrix`, `RawMorphismMatrix` (raw matrix payloads: `Matrix | Sequence[Sequence[ExactScalar]]`), `RawVectors` (raw family of vectors in given coordinates — the subobject-algebra input: matrix rows, nested sequences, or actual `Vector`s), `GramMatrix` (in `foundations`), `FormKind`, `ValueModule`, narrowing functions `in_*`. (`MorphismMatrix` is retired — see I.4; `.matrix()` of a morphism is an ordinary `Matrix`. The `MatrixLike` protocol is retired 2026-07-09: it shadowed the real `Matrix` class — defect class I.2.)

Missing-but-named (declared contracts whose types the audit shows are wrong or placeholder): `HyperbolicLattice.fundamental_chamber` returns `FundamentalChamberLike` (a placeholder) — the lexicon type is `geometry.Polyhedron`; `Genus.local_symbol` likewise returns the placeholder — the honest type is the Conway–Sloane local symbol object (`interop.SageLocalGenusSymbol`).

### II.4 Geometry and combinatorics (`geometry.py`)

| Name | Meaning | Representation | Sage realization |
| --- | --- | --- | --- |
| `Polyhedron` | convex polyhedron (Voronoi cells, fundamental chambers) | alias | `sage.geometry.polyhedron.base.Polyhedron_base` |
| `Polygon` | 2-dimensional polytope | alias of `Polyhedron` (dimension is the constructor's contract) | same |
| `Graph` | finite (undirected) graph — Coxeter/Dynkin diagrams, root graphs | alias | `sage.graphs.graph.Graph` |

Note the annotation defect this fixes: `objects/parents.py` annotates `voronoi_cell` with the *constructor function* `sage.geometry.polyhedron.constructor.Polyhedron` used as a type.
The lexicon noun is the class of its values.

### II.5 Technical Sage-interop vocabulary (`interop.py`)

The `Sage*` spellings exist for exactly one purpose: naming Sage's object when it is *distinct from* (or must be distinguished from) the repo's semantic object of the same mathematical kind.
Dev-facing; never in researcher-facing signatures unless the sentence is genuinely about Sage's object.

| Name | Distinct from | Sage realization |
| --- | --- | --- |
| `SageLattice` | the owned `Lattice` tower | `FreeQuadraticModule_integer_symmetric` (Sage's `IntegralLattice`) |
| `SageGenus` | owned `Genus` | `sage.quadratic_forms.genera.genus.GenusSymbol_global_ring` |
| `SageLocalGenusSymbol` | (no owned counterpart yet) | `sage.quadratic_forms.genera.genus.Genus_Symbol_p_adic_ring` |
| `SageDiscriminantForm` | owned `DiscriminantForm` tower | `sage.modules.torsion_quadratic_module.TorsionQuadraticModule_ambient_with_category` — constructed via `TorsionQuadraticForm`/`TorsionQuadraticModule` |
| `SageQuadraticForm` | owned lattices carry the form intrinsically | `sage.quadratic_forms.quadratic_form.QuadraticForm` |
| `SageFreeModule` | semantic `FreeModule`; dev union over whatever module implementation a Sage seam hands back | `FreeModule_generic \| FGP_Module_class` (extend on first use) |
| `SageParent` / `SageElement` | owned parents/elements subclass these | `sage.structure.parent.Parent`, `sage.structure.element.Element` |
| `SageCategory` | owned category classes subclass these | `sage.categories.category_types.Category_over_base_ring` |
| `SageCartanMatrix` | `foundations.CartanType` (the datum) vs Sage's matrix object | `sage.combinat.root_system.cartan_matrix.CartanMatrix_crystallographic` |
| `SageQmodnZ` | `ValueModule` protocol in `domain_algebra` (kept: it types this external object structurally by ratified design) | `sage.groups.additive_abelian.qmodnz.QmodnZ` |
| `SageInfinity` | — (return type of `minimum`/`maximum` on rank-0/indefinite regimes) | `sage.rings.infinity.PlusInfinity` / `MinusInfinity` |

Semantic nouns that *coincide* with Sage's implementation (Matrix, Vector, Integer, …) do **not** get a `Sage*` doppelgänger; the semantic spelling in II.1/II.2 is the only spelling.
A `Sage*` name is introduced only at the moment the repo gives the bare name a different meaning.

### II.6 Named-but-deferred vocabulary

Nouns the research program will need, catalogued now so their future homes are fixed; each is one alias/union away using the same policy — they are *not* declared until first use (a lexicon entry with no consumer is untestable):

`Cone`, `Fan` (toric/chamber geometry, Vinberg workstream — `geometry.py`); `WeylGroup`, `CoxeterGroup` (→ `algebra.py`, GAP/Sage-backed); `NumberField`, `PadicRing`, `PadicNumber` (local theory — `foundations.py`); `QuadraticSpace` (ℚ-form without integral structure — owned tower, next to `Lattice`); `ModularForm` (theta series); `EllipticCurve`/`K3Surface` (AG side, likely owned protocols over external data); `AbelianGroupMorphism` (the quotient projection `L → L/M` is an abelian-group hom, not a `LatticeMorphism`; until declared, such maps are typed as callables).

* * *

## Part III — Representation policy

Priority order when a noun enters the lexicon:

1. **Owned class, wired as category `ParentMethods`** — when the repo owns the mathematics (the lattice/discriminant towers).
   This is the ratified single-source design: the typed class and the runtime-injected API are one artifact.
2. **Sage category `ParentMethods`** — when the noun is a *kind of Sage parent* (`Ring`, `Field`). The stub tree declares the category MRO edge on each implementation class it stubs, so everything Sage codes correctly is captured for free; check that the category actually carries the surface, since many Sage implementations forget to opt in (see II.2 preamble).
3. **Alias to the Sage implementation class** (through `typings/sage/`) — when the semantic meaning coincides with one Sage class (`Matrix`, `Vector`, `Polyhedron`). Tightest contract; no drift possible.
4. **Union over enumerated Sage implementation classes** — the documented fallback for kinds whose implementations don't opt into their category, and for dev seams (`SageFreeModule`). Extension is a catalogued one-liner.
5. **Protocol** — only for external objects we neither own nor can enumerate, where structural typing is the honest statement (`ValueModule` is the one ratified example; a protocol built by *inspecting* a known set of non-opted-in implementations is the other sanctioned shape).
   A protocol that shadows a single concrete class is a defect (I.2).
6. **NewType over a real class** — parse-witnesses (`GramMatrix`): the codec proved a property the class does not encode.
   A witness must still be a mathematical noun: "Gram matrix" is one; "MorphismMatrix" was not (the morphism object is its own witness), which is why it does not exist here.

`Any` is not a representation.
If a value cannot be named with 1–5, the noun is missing from the catalogue — add it (Part II or II.6), don't write `Any`.

**Scalar parametrization.** The linear-algebra chain (`Matrix`, `Vector`, `FreeModuleElement`, `FreeModule_generic`) is generic in its scalar, bounded by `RingElement`, with the exact regime `Integer | Rational` as the PEP 696 *default*. Bare `Matrix` therefore means an exact matrix (today's code checks unchanged), and future regimes are spelled at the type level — `Matrix[SymbolicExpression]`, `Matrix[RealNumber]`, a future `Matrix[PadicNumber]` — instead of being golfed into the exact stubs.
The same pattern is the template for any future noun whose meaning varies over a coefficient ring: parametrize, bound mathematically, default to the regime the research program actually computes in.

## Part IV — Naming rules

1. Type names are mathematical nouns a researcher would say aloud: `Lattice`, `FiniteAbelianGroup`, `IsometryGroup`.
2. Banned in type names: implementation-role vocabulary — `Carrier`, `Host`, `Kernel` (in the software sense), `Delta`, `Like`, `Impl`, `Base` (as a suffix), `Mixin`. If a class plays an implementation role, the *docstring* says so; the name states the mathematics.
3. `Sage*` prefix is reserved for Part II.5: Sage's object where it differs from ours.
   Never prefix a noun whose only realization is Sage's class.
4. No import-site renames of lexicon nouns (`import X as YCarrier` is how I.3 happened).
   If two meanings collide in one module, the collision is real: one of them is a `Sage*` noun or a missing catalogue entry.
5. Raw/parsed pairs follow the codec convention: `RawX` (untrusted input) → codec → `X` (witness).
   Codecs are the only producers of witnesses.

## Part V — Consistency obligations

The subtree must satisfy, at all times (enforced by `just -f justfile lexicon-check`, see README):

1. `mypy --strict` passes over `lexicon/` with `../typings/` on the stub path — the catalogue type-checks as a collection of stubs.
2. Every Sage identifier the stubs or aliases name exists on the running Sage (`lexicon/verify_against_sage.py` imports every aliased class and asserts every stubbed attribute) — stubs are claims about an external system and are verified against it, never trusted from memory.
3. One authority per noun: a name is defined in exactly one lexicon module; `__init__.py` is re-export only; `domain_algebra.py` remains the authority for the owned tower until migration step M2.
