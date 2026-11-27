---
id: SPEC-MAPPING-LATTICES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track lattices mapping spec
status: complete
priority: critical
requirement: Convert category_specs/lattices/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  lattice, form, dual, discriminant, isometry, and algorithm signatures.
acceptanceCriteria:
- Source paths category_specs/lattices/docs/MAPPING.md and category_specs/lattices/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 90
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# MAPPING.md — Lattices Subtree Spec

This tracked spec is the canonical mapping surface converted from `category_specs/lattices/docs/MAPPING.md`.

Source inventory: `category_specs/lattices/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/lattices/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage`
  - `sage/modules/free_quadratic_module.py`
  - `sage/modules/fg_pid/fgp_module.py`
  - `sage/modules/fg_pid/fgp_element.py`
  - `sage/modules/fg_pid/fgp_morphism.py`
  - `sage/modules/torsion_quadratic_module.py`
  - `sage/modules/free_quadratic_module_integer_symmetric.py`
  - `sage/quadratic_forms/quadratic_form.py`
  - `sage/geometry/toric_lattice.py`
  - `sage/geometry/toric_lattice_element.pyx`
- Source-visibility gaps from inventory tokens requiring follow-up during completeness audit:
  - `sage/categories/bilinear_modules.py`
  - `sage/categories/free_bilinear_modules.py`
  - `sage/categories/lattices.py`
  - `sage/categories/rational_lattices.py`
  - `sage/categories/torsion_bilinear_modules.py`
  - `sage/categories/discriminant_quadratic_forms.py`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the Lattices
  source reconciliation is recorded below, with remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Sage 10.7 Source Reconciliation

This pass reconciles the local inventory against installed Sage 10.7 and the current
lattice-redesign doctrine. The mapping below is authoritative for Sage surfaces that are
missing from, inherited into, or only partially represented in the converted table.
Current Sage remains implementation evidence only: no row imports Sage's
ambient-vector-space lattice convention into the public semantics.

### Definition Grounding

- Local doctrine checked: `category-abc-spec.md`,
  `lattice-interface-style-guide.md`, `lattice-redesign-corrections-spec.md`,
  `category_specs/lattices/docs/SAGE_INVENTORY.md`,
  `category_specs/lattices/__init__.py`,
  `category_specs/forms/chain.py`,
  `category_specs/forms/subcategories/integral.py`,
  `category_specs/forms/subcategories/free_bilinear.py`,
  `category_specs/forms/subcategories/torsion_quadratic_modules.py`,
  `category_specs/lattices/subcategories/constructions/dual_objects.py`,
  `category_specs/lattices/subcategories/constructions/discriminant_groups.py`,
  and `category_specs/modules/subcategories/finitely_presented_over_pid.py`.
- Sage 10.7 source checked: `sage/modules/free_quadratic_module.py`,
  `sage/modules/free_quadratic_module_integer_symmetric.py`,
  `sage/modules/fg_pid/fgp_module.py`,
  `sage/modules/fg_pid/fgp_element.py`,
  `sage/modules/fg_pid/fgp_morphism.py`,
  `sage/modules/torsion_quadratic_module.py`,
  `sage/quadratic_forms/quadratic_form.py`,
  `sage/quadratic_forms/quadratic_form__equivalence_testing.py`,
  `sage/quadratic_forms/quadratic_form__local_field_invariants.py`, and
  `sage/groups/matrix_gps/isometries.py`.
- Mathematical model: lattices are presented free modules with forms. The selected
  generators are presentation data. A generator or basis change creates a distinct
  object, possibly with an isometry witness, not the same object by equality.
- Element divisibility is the submodule or ideal generated by
  `{b(v,w) : w in M}` in the form codomain. Coordinate gcds are at most
  implementation witnesses under extra hypotheses and are not the definition.

### Constructor and Presentation Reconciliation

| Sage surface | Source evidence | Spec owner or classification | Reconciliation |
| --- | --- | --- | --- |
| `FreeQuadraticModule(base_ring, rank, degree, inner_product_matrix, sparse=False)` and `FreeQuadraticModule_generic.__init__` | `free_quadratic_module.py:310` | `Modules(R).Free().FiniteRank().WithForms().Bilinear()` constructor path | Admit as an interop-backed constructor from `(R, finite rank, form matrix, selected generators)`. Do not expose Sage's `degree`, `sparse`, or ambient-space basis as public lattice data. |
| `IntegralLattice(...)` / `FreeQuadraticModule_integer_symmetric` | `free_quadratic_module_integer_symmetric.py:625` | `Lattices(ZZ).Constructors()` and richest correct meet | Admit via named constructors from a presented integral symmetric nondegenerate bilinear form. The Sage `ambient`, `basis`, and `inner_product_matrix` triple is backend presentation evidence only; public identity is the selected generator presentation with form data. |
| `TorsionQuadraticForm(q)` | `torsion_quadratic_module.py:20` | `Lattices(ZZ).DiscriminantGroups()` or forms-owned torsion quadratic constructor | Admit as a closed constructor from a symmetric rational quadratic Gram matrix and quotient-valued codomain. It must validate the quotient codomain (`QQ/ZZ` or `QQ/2ZZ`) explicitly instead of exposing Sage's denominator-clearing path. |
| `TorsionQuadraticModule(V, W, modulus, modulus_qf, gens)` | `torsion_quadratic_module.py:190` | `Modules(R).WithForms().Quadratic().Torsion()`; lattice discriminant groups when built as `coker(L -> L^#)` | Preserve through two named routes: a generic torsion formed-module constructor from quotient data, and the lattice-owned discriminant descent path. `modulus` and `modulus_qf` are codomain data, not option-bag public API. |
| `QuadraticForm(...)`, `QuadraticForm.from_polynomial`, `change_ring`, `primitive`, `level`, `level_ideal` | `quadratic_form.py:1150`, `1190`, `1214`, `1301`, `1541`, `1586` | Quadratic-form/forms subtree, not `Lattices` as owner | Use as conversion and backend evidence for free quadratic objects. `level` is a quadratic-form invariant over a PID and is not a lattice method unless a lattice theorem explicitly owns the call. |
| `direct_sum`, `tensor_product`, `twist` on Sage lattices | `free_quadratic_module_integer_symmetric.py:871`, `1332`, `1653` | `Free + Bilinear` or `ModulesWithForms` construction categories | Admit at the higher formed-module owners. `discard_basis` is not admitted as a public option; changing presentation must be explicit and returns a new object plus any available witness. |
| `sublattice`, `overlattice`, `maximal_overlattice` | `free_quadratic_module_integer_symmetric.py:972`, `1008`, `1030` | subobject/overlattice construction categories | Admit as lattice construction categories using generator-defined subobjects and inclusion morphisms. Do not expose row-basis or ambient-span wording as public semantics. `maximal_overlattice(p)` stays `OverZZ`/algorithmic and evenness-hypothesis guarded. |

### Inherited Module and Hom Surfaces

| Sage surface | Source evidence | Spec owner or classification | Reconciliation |
| --- | --- | --- | --- |
| `FGP_Module_class(V,W)`, `V`, `W`, `cover`, `relations`, `quotient_map` | `fgp_module.py:293`, `837`, `875`, `1957` | `Modules(R).FinitelyPresented().OverPID()` | Preserve as finitely presented module quotient data. These are module presentation methods, not lattice methods. |
| `invariants`, `smith_form_gens`, `gens_to_smith`, `smith_to_gens`, `coordinate_vector`, `gens_vector` | `fgp_module.py:977`, `1040`, `1071`, `1185`, `1247` | finitely presented PID modules; coordinate interop | Preserve as module and backend-coordinate witnesses. Public lattice API should speak in elements, generators, morphisms, and quotient objects; coordinate vectors are localized interop. |
| `submodule`, `is_submodule`, `has_canonical_map_to`, `__le__` | `fgp_module.py:707`, `798` | module subobject and structure-map surfaces | Preserve as subobject evidence. Public subobjects must carry inclusion morphisms; they are not optional ambient state on a lattice object. |
| `hom(im_gens, codomain=None, check=True)` and `_Hom_` | `fgp_module.py:1480`, `1690` | Hom category constructors | Do not admit `hom(images)` as the main public constructor. Preserve through `M.Hom(N)` and Hom-parent constructors `from_dict`, `from_images`, `from_callable`, and `from_matrix`. |
| `FGP_Morphism.__call__`, `kernel`, `inverse_image`, `image`, `lift` | `fgp_morphism.py:226`, `299`, `327`, `368`, `386` | morphism element methods in module/formed-module categories | Preserve as categorical morphism operations. `cokernel` remains a required project-owned gap: the public discriminant path needs the actual cokernel object with descended form data, not only Sage's kernel/image/lift helpers. |
| `FGP_Element.lift`, `vector`, `additive_order` | `fgp_element.py:85`, `312`, `414` | module elements; torsion element order | `additive_order` is admitted at torsion elements. `lift` and `vector` are generic quotient-coordinate operations; discriminant-group `lift` is public only when it returns an element of the relevant dual/rational lattice, not a bare Sage vector. |
| `cardinality`, `is_finite`, `list`, `__iter__`, `random_element` | `fgp_module.py:1755`, `1788`, `1867` | sets/modules enumeration and runtime | Preserve as set/module runtime surfaces. Enumeration of infinite lattice objects requires the separate countability/enumeration program, not ad hoc lattice-local loops. |

### Toric Character-Lattice Boundary Correction

Sage's `ToricLattice` source is a warning against both over-narrowing the word
"lattice" to later Coble/Nikulin algorithms and erasing the formed structure carried by
presented torus character lattices. It subclasses Sage PID free-module classes and adds
named parent identity, dual-name bookkeeping, conversion barriers, and toric notation.
For a presented coordinate torus, the coordinate characters give a selected basis and
the identity Gram matrix gives a unimodular lattice. This does not create a separate
toric owner; it routes Sage toric lattice surfaces through ordinary free-module,
basis, and formed-lattice owners.

| Sage toric surface | Correct owner | Reconciliation |
| --- | --- | --- |
| `ToricLattice(rank, name, dual_name, ...)` | finite-rank free abelian module with selected basis; unimodular formed-lattice surface when the coordinate-character presentation supplies the identity Gram form | Constructor evidence that named free abelian lattices must preserve parent identity and notation. Toric provenance alone is not a mathematical axiom, but the coordinate-character presentation supplies real basis/form data. |
| `ToricLattice.dual()` and dual element action | module dual object, metric `dual_lattice()` for the identity form, and their canonical unimodular identification | The module dual `Hom_ZZ(L, ZZ)` and the metric dual `L^#` coincide for the identity Gram form. Sage's dual parent is implementation evidence for the compatibility, even though Sage exposes it through toric notation. For arbitrary formed lattices, the module dual and metric dual must be kept distinct unless an isomorphism is explicitly recorded. |
| `submodule`, `span`, `span_of_basis`, `intersection`, `saturation`, `quotient`, `direct_sum` | inherited module subobject, basis, quotient, and direct-sum surfaces | Sage preserves toric-flavored parents for usability, but the method owners are ordinary module/lattice owners. |
| same-lattice element dot product rejection | Sage implementation/interop limitation relative to the identity-formed project surface | Sage's refusal to multiply two elements of the same toric lattice reflects its toric dual-pair convention, not a negative mathematical claim for the project spec. In the presented coordinate-character lattice, the identity Gram form supplies the same-lattice bilinear form. |

### Lattice and Form Method Reconciliation

| Sage surface | Source evidence | Spec owner or classification | Reconciliation |
| --- | --- | --- | --- |
| `ambient_module`, `ambient_vector_space`, `basis_matrix`, `inner_product_matrix`, `degree`, display `_repr_` | `free_quadratic_module.py:369`, `472`; `free_quadratic_module_integer_symmetric.py:625` | private/runtime/display/interop | Do not admit as public lattice semantics. These witness Sage's ambient implementation and may be used at backend boundaries only. Public objects expose generators, form data, and morphisms. |
| `gram_matrix`, `determinant`, `discriminant` | `free_quadratic_module.py:390`, `408`, `439` | `Free + Bilinear` | Admit at the first free bilinear tier. Gram matrices are presentation data in selected generators, not identity of an abstract isometry class. |
| `is_even`, `dual_lattice`, `discriminant_group` | `free_quadratic_module_integer_symmetric.py:736`, `753`, `779` | finite-rank free integral bilinear modules; `dual_lattice` and `discriminant_group` require nondegeneracy for the metric-dual identification and finite quotient | Admit, but the project implementation must route `discriminant_group()` through `L -> L^# -> coker`, preserving quotient-valued form codomains. General Hom-duality remains a module dual-object surface, not `dual_lattice()`, unless a specific isomorphism with the metric dual is recorded. |
| `signature_pair`, Sage `signature()` as `n_+ - n_-` | `free_quadratic_module_integer_symmetric.py:839`, `855` | exact free symmetric form signature data over a base with an ordered real realization; display/index interop for `p-q` | Preserve exact signature data. The scalar `p-q` is Sage interop/display data, not the owner of signature semantics. `[[DECISION-ORDERED-REAL-SIGNATURE-OWNER]]` admits the selected ordered-real-realization owner; a bare integral-domain hypothesis is not enough. |
| `orthogonal_complement`, `orthogonal_submodule_to`, element `perp` | `free_quadratic_module_integer_symmetric.py:931`; `torsion_quadratic_module.py:890` | symmetric bilinear modules and subobjects | Admit at the symmetric bilinear owner. Inputs must be subobjects/elements with parent data, not arbitrary ambient vectors. |
| `is_primitive(M)` | `free_quadratic_module_integer_symmetric.py:901` | module subobject/inclusion predicate | Admit for subobjects via quotient torsion-freeness. Do not conflate with element divisibility unless a source-backed equivalence proof records the hypotheses. |
| element `divisibility` | local lattice doctrine and user constraint | symmetric bilinear module elements | Required project surface. Definition is `<b(v,M)> <= S`; for scalar-valued forms it is an ideal of `R`. Sage does not supply this definition as a lattice method. |
| `orthogonal_group(gens=None, is_finite=None)`, `automorphisms` | `free_quadratic_module_integer_symmetric.py:1155`, `1313`; `groups/matrix_gps/isometries.py` | formed-module Aut category | `O(M,b)` is `Aut_C(M)`. Sage's matrix group, right action, and definite-only generator computation are backend details. User-supplied `gens` maps to explicit subgroup construction after each generator has been promoted to an automorphism object and checked by Aut containment. |
| `minimum`, `maximum`, `LLL`, `short_vectors`, `enumerate_short_vectors`, `enumerate_close_vectors` | `free_quadratic_module_integer_symmetric.py:1409`, `1435`, `1463`, `1500`, `1596`, `1631` | deferred algorithm or backend-only surfaces | Preserve as inventoried Sage algorithms but do not admit as core lattice vocabulary in this spec pass. Definite enumeration belongs to a sourced algorithm card; indefinite enumeration requires the universal countability/enumeration program or an audited backend. |
| `quadratic_form()` | `free_quadratic_module_integer_symmetric.py:1393` | forms conversion | Admit as `associated_quadratic_module()` or a named constructor/conversion in forms. The result category is codomain data, not the owner of the lattice operation. |
| rational/local isometry helpers on `QuadraticForm` | `quadratic_form__equivalence_testing.py:299`; `quadratic_form.py:500` | backend evidence for lattice isometry methods | Use as implementation evidence for `is_rationally_isometric_to` and `is_locally_isometric_to` only after converting through the formed-module/lattice presentation and returning morphism witnesses when requested. |

### Torsion and Discriminant-Form Reconciliation

| Sage surface | Source evidence | Spec owner or classification | Reconciliation |
| --- | --- | --- | --- |
| element `b`, `inner_product`, `q`, `quadratic_product` | `torsion_quadratic_module.py:121`, `154` | torsion bilinear/quadratic element methods | Admit as `b` and `q`; `inner_product` is interop terminology only. Values live in quotient codomains, not in lifted rationals. |
| `gram_matrix_bilinear`, `gram_matrix_quadratic`, `value_module`, `value_module_qf` | `torsion_quadratic_module.py:457`, `487`, `1251`, `1271` | torsion formed modules and discriminant groups | Admit. These are quotient-valued form data (`K/R`, `K/2R`), distinct from free integral Gram matrices. |
| `all_submodules`, `submodule_with_gens`, `primary_part` | `torsion_quadratic_module.py:363`, `1113`, `1149` | torsion modules and discriminant groups | Admit with generator-defined subobject semantics. `primary_part(m)` maps to the torsion `p_part`/primary-component surface when `m` is a prime-power selector; composite `m` requires an explicit named decomposition rule. |
| `normal_form`, `brown_invariant` | `torsion_quadratic_module.py:408`, `939` | torsion quadratic/discriminant forms | Admit with theorem/source hypotheses recorded at use sites. `brown_invariant()` requires a `QQ/2ZZ` quadratic codomain. |
| `genus(signature_pair)`, `is_genus(signature_pair, even=True)` | `torsion_quadratic_module.py:539`, `743` | discriminant-form plus signature theorem surface; lattice theorem context | Preserve, but do not let the result object own the method. The caller data are a discriminant form and signature hypotheses; lattice-level theorem methods must state even/odd and rank/length conditions before relying on the result. |
| `orthogonal_group(gens=None, check=False)` on torsion quadratic modules | `torsion_quadratic_module.py:816` | `Lattices(R).DiscriminantGroups().AutCategory()` via module Hom/Aut machinery | Admit as finite torsion formed-module Aut. Raw matrices and abelian-group automorphisms are constructor inputs to the Aut parent, not elements before containment succeeds. |
| finite `isotropic_elements()` on torsion quadratic/discriminant forms | `torsion_quadratic_module.py:154`; theory/foundations/coble-task-background.md Task 2.1 | finite torsion formed-module enumeration surface; discriminant groups inherit generic formed-module isotropic predicates | Admit as enumeration of finite carrier elements satisfying the already-generic isotropic predicate, e.g. `q(x)=0` in the quadratic codomain. Use "elements", not "vectors", unless a separate finite-vector-space structure has been constructed. This is finite-set enumeration, not a lattice-vector enumeration. |
| finite action `orbit(x)`, `orbits(S)`, `orbit_representatives(S)` for discriminant-form automorphism groups | `torsion_quadratic_module.py:816`; `groups/fqf_orthogonal.py`; theory/foundations/coble-task-background.md Task 2.1 | `DiscriminantGroupAut` and finite group-action categories | Admit on the group/action object, not as a method owned by `nikulin_invariants()` or by the underlying abelian group alone. The acted-on set must be a typed subset of the discriminant group, such as isotropic elements. |
| `discriminant_action()`, `image_in_discriminant_orthogonal_group()`, `kernel_of_discriminant_action()` | `torsion_quadratic_module.py:856`; theory/foundations/coble-task-background.md Tasks 2.1-2.2 | `Lattices(R).AutCategory()` for nondegenerate integral lattices with `discriminant_group()` | Admit as the canonical bridge `O(L) -> O(A_L,q_L)`. The kernel is the stable orthogonal group acting trivially on the discriminant form; subgroup names and orbit-lifting methods must route through this homomorphism. |
| `twist(s)` on torsion quadratic modules | `torsion_quadratic_module.py:1207` | forms-owned form scaling | Admit as formed-module twist/rescale of the form codomain, with explicit codomain update. |

### Formal Negative and Corrective Findings

- Searched: `sed` on `theory/spec_backups/lattices_written_spec_backup.py`; `test -e
  /home/dzack/research/theory/spec_backups/lattices_written_spec_backup.py`; `git
  ls-files theory/spec_backups`; `find theory -path '*spec_backups*' -type f`; `rg
  "lattices_written_spec_backup" theory .agents plans category_specs`; and
  `.agents/theory/spec-backups/lattices_written_spec_backup.py`.
- Found: the old path `theory/spec_backups/lattices_written_spec_backup.py` is absent
  from the current working tree and is not tracked by `git ls-files`, but the source
  material exists at `.agents/theory/spec-backups/lattices_written_spec_backup.py`.
  Its opening docstring supplies the presented-module-with-form model, and its element
  implementation records the old pairing-defined divisibility behavior. The
  lattice-redesign skill has also centralized the mined doctrine into
  `category-abc-spec.md`, `lattice-interface-style-guide.md`, and
  `lattice-redesign-corrections-spec.md`.
- Conclusion: inference -- current work should cite the centralized lattice-redesign
  doctrine as the active API authority and may use
  `.agents/theory/spec-backups/lattices_written_spec_backup.py` as mineable source
  provenance. The stale `theory/spec_backups/...` path should not be treated as
  unavailable mathematical content.
- Confidence: High.
- Gaps: I did not search deleted git history for the exact move/rename commit because
  the active source material is present in `.agents/theory/spec-backups/`.

- Searched: `sed` on `src/lattices/categories/bilinear_modules.py`,
  `src/lattices/categories/free_bilinear_modules.py`,
  `src/lattices/categories/lattices.py`; `git ls-files src/lattices`; `npx -y
  @probelabs/probe search` for the named local category surfaces under
  `/home/dzack/research` and `/home/dzack/research/category_specs`.
- Found: no active `src/lattices/categories/...` files are present or tracked in this
  checkout. The corresponding current spec surfaces live under `category_specs/forms`,
  `category_specs/modules`, and `category_specs/lattices`, with roadmap cards retaining
  older `src/lattices` references.
- Conclusion: inference -- the `src/lattices/categories/...` entries in
  `SAGE_INVENTORY.md` are stale local-source pointers for the current checkout; use the
  active `category_specs` files and lattice-redesign docs as the local source surface.
- Confidence: High.
- Gaps: I did not inspect deleted git history or quarantined backup trees for old
  implementation files because the task forbids edits outside this spec and the active
  spec files provide the current owner surface.

- Searched: `category_specs/lattices/docs/SAGE_INVENTORY.md`; installed Sage 10.7
  sources named above; `npx -y @probelabs/probe search "inclusion_morphism
  rational_span nikulin_invariants is_rationally_isometric_to is_locally_isometric_to"
  /home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage -l python`.
- Found: no Sage lattice methods named `inclusion_morphism`, `rational_span`,
  `nikulin_invariants`, `is_isometric_to`, `is_rationally_isometric_to`, or
  `is_locally_isometric_to` were found on `FreeQuadraticModule_integer_symmetric`.
  Sage does provide related backend evidence: `dual_lattice()`,
  `discriminant_group()`, quadratic-form rational/local equivalence helpers, and
  finite torsion-form orthogonal groups.
- Conclusion: inference -- these project lattice surfaces are genuine spec obligations
  or wrapper/admission work, not already-covered Sage lattice methods. Existing Sage
  code can support parts of their implementation but does not determine the public
  owner or signatures.
- Confidence: Medium.
- Gaps: I did not exhaust every lazy-imported Sage quadratic-form submodule beyond the
  local/rational equivalence and local-invariant sources surfaced by `QuadraticForm`.

## Converted Mapping Content

Records the mathematical justification for how every Sage surface maps to our hierarchy.
For each Sage type: what Sage provides, the correct mathematical concept, placement
decision, and consequence for refinement and regression tests.

---

## Hierarchy Overview

```
FormedModules(R) = Modules(R, dispatch=False).WithForms()  [owned in forms/]
└── .Bilinear()                                            [owned in forms/]
    └── .Symmetric()                                       [owned in forms/]
        └── .Nondegenerate()                               [owned in forms/]
            └── .Integral()                                [owned in forms/]
                └── .Lattice()                             [named endpoint in lattices/]

forms/subcategories/
├── with_forms.py          FormedModulesCategory
├── bilinear.py            BilinearModulesCategory
├── quadratic.py           QuadraticModulesCategory
├── symmetric.py           SymmetricBilinearModulesCategory
├── nondegenerate.py       NondegenerateBilinearModulesCategory
├── indefinite.py          IndefiniteBilinearModulesCategory
├── definite.py            DefiniteBilinearModulesCategory
├── integral.py            IntegralBilinearModulesCategory
├── rational.py            RationalBilinearModulesCategory
└── free_bilinear.py       FreeBilinearModulesCategory     (Free + Bilinear)

lattices/subcategories/
├── over_dedekind.py       _LatticesOverDedekindDomain
├── over_pid.py            _LatticesOverPID
├── over_integers.py       _LatticesOverIntegers    (= Lattices(ZZ))
├── even.py                _EvenLattices
├── unimodular.py          _UnimodularLattices
└── constructions/
    ├── dual_objects.py    Hom-dual objects, when admitted with explicit formed-object data
    ├── dual_lattices.py   metric-dual lattice construction / compatibility spelling
    ├── overlattices.py
    ├── orthogonal_direct_sums.py
    └── discriminant_groups.py
```

---

## Method Placement Table

The table answers: at what tier is each method first universally well-defined?

| Method | Minimal tier | Justification |
|--------|-------------|---------------|
| `form()` | `WithForms` | definitional; every object in this category carries a form |
| form evaluation | inherited from `Modules().WithForms()` | not lattice-owned; lattices inherit module-with-form evaluation rather than defining a lattice-specific `evaluate` method |
| `form_degree() -> (p,q)` | `WithForms` | (1,1) for bilinear, (1,0) for linear, etc. |
| `b(v, w)` | `Bilinear` | bilinear evaluation; only defined once the form is bilinear |
| `self_product(v)` | `Bilinear` | `b(v,v)`; defined for any bilinear form |
| `is_isotropic(v)` | `Bilinear` | `b(v,v) = 0`; defined for any bilinear form |
| `perp(v)` (element) | `Bilinear` | `{w ∈ M : b(v,w)=0}` is a submodule for any bilinear form |
| `orthogonal_submodule_to(S)` | `Bilinear` | `S^⊥ = {w : b(s,w)=0 ∀s∈S}`; always a submodule |
| `q(v)` | `Quadratic` | quadratic form evaluation |
| `is_symmetric()` | `Symmetric` | witness predicate |
| `is_alternating()` | `Alternating` | witness predicate |
| `is_nondegenerate()` | `Nondegenerate` | witness predicate |
| `is_indefinite()` | `Indefinite` over ordered real realizations | witness predicate; requires a signed scalar context |
| `is_definite()` | `Definite` over ordered real realizations | witness predicate; requires a signed scalar context |
| `gram_matrix()` | `Free + Bilinear` | requires a basis; entries `b(e_i,e_j)` lie in R; see note (1) |
| `inner_product_matrix()` | private/runtime/display interop only | Sage ambient-space matrix; not public lattice semantics; see reconciliation |
| `rank()` | `Free` | rank of free module; undefined for general modules |
| `determinant()` | `Free + Bilinear` | `det(gram_matrix)`; requires basis |
| `discriminant()` | `Free + Bilinear` | `(-1)^r * det`; requires basis |
| `is_positive_definite()` | `Free + Symmetric + ordered real realization` | eigenvalue/sign criterion needs finite free symmetric data over a scalar context with ordered real interpretation; see note (2) |
| `is_negative_definite()` | `Free + Symmetric + ordered real realization` | same |
| `signature_pair()` | `Free + Symmetric + ordered real realization` | inertia after scalar extension to the ordered real target; see note (2) |
| `signature()` | `Free + Symmetric + ordered real realization` | derived Sage scalar `p - q`; signature semantics are owned by `signature_pair()` |
| `dual_lattice()` | `Free + Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` | metric dual `L^#={v in L_K: beta(v,L) subset R}` uses the nondegenerate pairing inside scalar extension; see note (3) |
| `discriminant_group()` | `Free + Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` | `L^#/L` with the descended quotient-valued form; follows from `dual_lattice()`; see note (3) |
| `discriminant_form()` | `Free + Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` | named access to the quotient-valued bilinear/quadratic form on `L.discriminant_group()`; never just the invariant tuple |
| `inclusion_morphism()` | `Free + Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` | `i: L -> L^#`; same metric-dual tier |
| `is_even()` | `Bilinear.Integral` | `b(m,m) in 2R for all elements m`; requires integrality but not freeness |
| `is_unimodular()` | `Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` | `L = L^#`, i.e. `|det|=1` |
| `orthogonal_complement(S)` (parent) | `Bilinear.Symmetric` | `S^⊥` is a submodule for ANY symmetric bilinear module; see note (4) |
| `is_primitive(M)` | `Free + OverIntegralDomain` | quotient L/M is torsion-free |
| `direct_sum(other)` | `Free + Bilinear` | orthogonal direct sum with block-diagonal gram matrix |
| `tensor_product(other)` | `Free + Bilinear` | Kronecker product of gram matrices |
| `sublattice(basis)` | `Free + Bilinear + OverPID` | sublattice on a basis requires PID structure |
| `overlattice(gens)` | `Free + Symmetric + Nondegenerate + OverIntegralDomain` | L + span(gens) ∩ dual; requires dual |
| `maximal_overlattice(p)` | `OverZZ` | algorithm uses ZZ-specific arithmetic |
| `twist(s)` | `WithForms` | scale form by scalar; defined for any module with form |
| `genus()` | `OverZZ` | local-global genus theory; requires ZZ (or at least Dedekind) |
| `orthogonal_group()` | `Modules(R).WithForms().AutCategory()` | `O(M,b) = Aut(M,b)` in the category of modules with forms; see note (5) |
| `special_orthogonal_group()` | `Lattices(R).AutCategory()` parent-method refinement | determinant-one subgroup of the lattice orthogonal group, defined once the aut surface has a determinant realization |
| `stable_orthogonal_group()` | `Lattices(R).AutCategory()` parent-method refinement | orientation or positive-cone refinement of the lattice orthogonal group, not a method on lattice objects |
| `discriminant_action()` | `Lattices(R).AutCategory()` plus lattice `discriminant_group()` data | homomorphism from lattice isometries to automorphisms of the discriminant form |
| `image_in_discriminant_orthogonal_group()` | same as `discriminant_action()` | image subgroup of `O(A_L,q_L)` |
| `kernel_of_discriminant_action()` | same as `discriminant_action()` | stable orthogonal subgroup acting trivially on `A_L` |
| `nikulin_invariants()` | `OverZZ + Free + Symmetric + Nondegenerate` | convenience invariant tuple for sourced 2-elementary classification; not a substitute for `discriminant_group()` or discriminant-form orbit data |
| `is_isometric_to(other)` | `OverZZ + Free + Symmetric + Nondegenerate` | lattice isometry test |
| `minimum()` | `OverZZ + Free + Symmetric` | shortest vector (requires ZZ for finiteness) |
| `maximum()` | `OverZZ + Free + Symmetric` | longest nonzero vector in compact regions |
| `LLL()` | `OverZZ + Free + Symmetric` | LLL reduction; ZZ-specific |
| `short_vectors(n)` | `OverZZ + Free + Symmetric` | ZZ-specific enumeration |
| `short_vectors(n, up_to_sign_flag=True)` | `short_vectors_up_to_sign(n)` at the same tier | Sage forwards `**kwargs` to `QuadraticForm.short_vector_list_up_to_length`; the installed source exposes the single meaningful keyword `up_to_sign_flag`. The project splits that finite case into a named method instead of exposing a keyword bag. |
| `quadratic_form()` | `Free + Symmetric` | convert to `QuadraticForm` object |
| `rational_span()` | `Free + OverIntegralDomain` | `L ⊗_R Frac(R)` |
| `base_change_to(ring)` | `Free + Bilinear` | change coefficient ring |
| `gram_matrix_bilinear()` | `Torsion + Bilinear` | Gram matrix in Q/mZ; see note (6) |
| `gram_matrix_quadratic()` | `Torsion + Quadratic` | quadratic Gram matrix |
| `isotropic_elements()` | `Torsion + Quadratic + finite carrier` | finite enumeration of elements with `q(x)=0`; excludes infinite lattice-vector enumeration semantics |
| `orbit(x)`, `orbits(S)`, `orbit_representatives(S)` | `FiniteGroupAction` on a typed finite set | action methods belong to the group/action object, including `DiscriminantGroupAut` acting on discriminant-group elements |
| `brown_invariant()` | `Torsion + Bilinear + Symmetric` | global torsion QF invariant |
| `normal_form()` | `Torsion + Bilinear + Symmetric` | canonical form |
| `primary_part(m)` | `Torsion` | m-primary part |
| `value_module()` | `Torsion + Bilinear` | Q/mZ containing form values |
| `value_module_qf()` | `Torsion + Quadratic` | Q/nZ containing QF values |
| `additive_order(v)` | `Torsion` (element) | order in torsion group |
| `lift(v)` | `Torsion` (element) | lift to dual lattice |
| `divisibility(v)` | `Bilinear.Symmetric` (element) | pairing-image submodule `<b(v, L)> <= S`; for scalar-valued forms `S = R`, this is an ideal; see note (9) |
| `is_primitive(v)` | `Modules` (element) | cyclic submodule primitive predicate via `v.span().inclusion().is_primitive()`; not a unit-divisibility rule without a source-grounded equivalence proof |
| `discriminant_class(x)` | metric-dual lattice element, i.e. an element of `L.dual_lattice()` | quotient map `L^# -> L^#/L`; ordinary `v in L` maps to the zero class via `L -> L^#`; see note (8) |
| `reflection(v)` | `Free + Symmetric + Nondegenerate` (element) | s_v(w) = w - 2b(v,w)/b(v,v) · v |
| `is_root(v)` | `Free + Symmetric + Integral` (element) | b(v,v) ∈ {-2, 2} |
| `norm(v)` | `Bilinear` (element) — see note (7) | b(v,v); defined for any bilinear form |

---

## Notes

**(1) `gram_matrix()` placement**: Sage places this at `FreeQuadraticModule_generic`
(free over commutative ring). We confirm: entries `b(e_i, e_j)` live in R only when the
form is R-valued and M is free (so the `e_i` are a basis). For a torsion module over a
PID, the analogous concept is `gram_matrix_bilinear()` in Q/mZ. These are distinct
methods at distinct tiers; do NOT merge them.

**(2) `signature_pair()` placement**: Sage places this at
`FreeQuadraticModule_integer_symmetric` (= ZZ). Mathematically, signature and positive
or negative definiteness require finite free symmetric bilinear data plus a scalar
context where signs make sense, such as `ZZ -> QQ -> RR` or another ordered real
realization. `[[DECISION-ORDERED-REAL-SIGNATURE-OWNER]]` decides that the abstract
owner is finite free symmetric bilinear data with a selected ordered real realization.
A bare `OverIntegralDomain` hypothesis does not choose such a realization and is not
enough. The `OverIntegers` tier provides concrete Sage evidence through the canonical
`ZZ -> QQ -> RR` ordered realization; fields or domains with multiple orderings need a
chosen ordering/real embedding or a separate total-signature surface.

**(3) `dual_lattice()` placement**: `L^# = {v in L_K : beta(v,L) <= R}` where
`L_K = L tensor_R K` and `K = Frac(R)`. This is the metric dual inside scalar
extension, not the general module dual `L^* = Hom_R(L,R)`, and its elements are not
functionals by definition. The bilinear form sends `x in L^#` to the functional
`beta(x, -)` when that expression is defined in the scalar extension, and under
finite projective/free nondegenerate hypotheses this transport can identify `L^#`
with `Hom_R(L,R)`. That identification does not by itself put an
`R`-valued form on `Hom_R(L,R)`: the metric dual inherits the scalar-extended
`K`-valued form, and any form transported to the module dual must name the
identification and codomain. In the unimodular integral case, including the identity
Gram toric-coordinate presentation, `L = L^#` and the transported form is the original
`R`-valued form. The discriminant group `L^#/L` is the finite quotient with descended
form data in the nondegenerate integral lattice setting. Sage's `ZZ` implementation is
one concrete algorithm for this owner.

The method docstring for `dual_lattice()` and any lattice-side `dual()` compatibility
surface must include the diagnostic-warning conditions. With the global category
diagnostic flag enabled, implementations should warn when the returned object may be
misread as the Hom dual: for example, in degenerate formed modules such as a rank-one
summand `<e>` in the hyperbolic plane `U`, `L^#` is the metric-dual construction being
returned, not an evaluation-bearing object of `Hom_R(L,R)`. In nondegenerate finite
free cases the warning text should name the recorded form-induced identification if
the implementation transports between `L^#` and `Hom_R(L,R)`. The warning must be
gated by the disabled-by-default category diagnostic flag specified in
`[[SPEC-MAPPING-CAT]]`; it is explanatory logging only and must not hide invalid
degenerate, non-free, or non-integral inputs.

**(4) `orthogonal_complement(S)` placement**: `S^⊥ = {v ∈ M : b(v,s) = 0 ∀s ∈ S}`.
This is always a submodule. No assumptions needed beyond having a bilinear form.
For symmetric forms, left and right orthogonal complements coincide, so the symmetric
axiom is needed only to guarantee `(S^⊥)^⊥ = S`. Abstract stub belongs at
`Bilinear.Symmetric`. Computability (as a free module of explicit rank) requires
nondegeneracy + free; that is an algorithm concern, not a placement concern.

**(5) `orthogonal_group()` placement**: `O(M,b) = Aut(M,b)` in the category of
modules with forms. Equivalently, its elements are module automorphisms `f` such that
`b(fv, fw) = b(v, w)`, or the corresponding form-preservation diagram commutes. This
definition does not require freeness, nondegeneracy, or integrality, so it covers
degenerate formed modules such as `e^perp` in `U`, rational formed modules, integral
lattices, and finite discriminant forms. Freeness and nondegeneracy are only needed for
particular realizations such as matrix groups inside `GL_n(R)`. The `OverZZ` definite
lattice computation uses Plesken-Souvignier; that is an algorithm detail, not the
mathematical owner.

**(6) Torsion `gram_matrix_bilinear()`**: For `TorsionQuadraticModule = V/W`, the form
takes values in `Q/mZ = (V^*/W^*) / (V/W)^*`. This is a *different type* from the
integral Gram matrix. Both are "gram matrices" but they live at different tiers with
different codomains. The torsion version is named `gram_matrix_bilinear()` (following
Sage) to avoid ambiguity with `gram_matrix()` at the free level.

**(7) `norm(v)` vs `self_product(v)`**: Both are `b(v,v)`. The name `norm` is Sage
lattice convention (appears in `Lattices.ElementMethods`). The name `self_product`
appears in our `BilinearModules.ElementMethods`. Both belong at `Bilinear` (element).
In the spec we use `self_product` at the generic bilinear level and provide `norm` as an
alias at the `Lattices(ZZ)` level (where "norm" is standard terminology).

**(8) `discriminant_class(x)` ownership**: The nontrivial map is the quotient
`L^# -> L^#/L`, so the method belongs to elements of the metric-dual lattice returned
by `L.dual_lattice()`. It does not belong to category-theoretic `DualObjects()`: those
are Hom-dual objects with evaluation behavior, while elements of `L^#` become
functionals only after explicit transport through the bilinear form. The former
ordinary lattice-element reading is recovered by first applying the inclusion
`L -> L^#`; its discriminant class is necessarily the zero element of
`L.discriminant_group()`, so it is not a separate element obligation on `L`.

**(9) `divisibility(v)` ownership**: For a symmetric bilinear module `(M, b)` with
`b: M x M -> S`, the invariant definition is the `R`-submodule
`<b(v, w) : w in M>` of `S`. In the scalar-valued case this is an ideal of `R`.
Principal generators and gcd presentations are representation choices under extra
hypotheses; they are not the owner definition and must not be replaced by coordinate
content in `Modules(R).Free()`.

**(10) Discriminant form and orbit ownership**: `nikulin_invariants()` is only a
classification summary under explicit 2-elementary hypotheses. The object needed for
orbit work is the discriminant group `A_L = L^#/L` together with its descended
quotient-valued form. The predicate `is_isotropic(x)` is generic formed-module/form
vocabulary; discriminant forms only add finite carrier enumeration such as
`isotropic_elements()`. Orbit decomposition belongs to a finite group action, and for
lattices the relevant action is supplied by the homomorphism `O(L) -> O(A_L,q_L)`.
Downstream lifting theorems may use the kernel/image of this homomorphism only after
their hypotheses have been checked against the actual computed lattice and
discriminant form.

---

## Construction-Category Vocabulary

The category-theoretic dual construction name `DualObjects()` is reserved for
Hom-dual objects: parents that are objects of the category and also carry the
hom-object/evaluation behavior coming from `Hom_R(N, R)`. It is not the owner for the
metric-dual lattice `L^#`.

The metric-dual lattice construction is `dual_lattice()` at the method level. If a
construction-category spelling is retained for compatibility, use the lattice-specific
`DualLattices()` spelling for that metric construction and keep it separate from
`DualObjects()`.

Other lattice construction names audited in this pass are not duplicate spellings of
standard construction categories:

| Lattice surface | Relationship to standard construction vocabulary | Decision |
| --- | --- | --- |
| `DualObjects()` | Hom-dual object construction: objects represented as `Hom_R(N, R)` and therefore carrying hom-object/evaluation behavior. A formed-object structure requires an explicit transported form or separate data. | Category dual surface, not the metric-dual owner. |
| `DualLattices()` | Lattice-specific metric-dual construction for `L^# = {v in L_K : beta(v,L) subset R}` when retained as a construction category. | Compatibility spelling for metric duals; keep separate from `DualObjects()`. |
| `Overlattices()` | Objects under a fixed lattice with finite-index, same-rational-span, inherited-form conditions. | Keep as lattice-specific refinement, not a replacement for `ObjectsUnder(base)`. |
| `OrthogonalDirectSums()` | Cartesian-product construction plus the orthogonal block-sum form and summand access. | Keep as refinement below `CartesianProducts()`. |
| `DiscriminantGroups()` | Finite torsion formed modules `L^#/L` with discriminant-form data. | Keep as lattice-specific quotient/form construction, not generic `Quotients()`. |

`Lattices(R).ObjectsOver(L)` and `Lattices(R).ObjectsUnder(L)` keep the
lattice-specific `structure_lattice()` and lattice morphism `structure_map()`.
Their former local `structure_domain()` and `structure_codomain()` implementations now
map to the Cat-owned universal structure-morphism methods through
`structure_morphism().domain()` and `structure_morphism().codomain()`.

---

## Sage Type → Spec Category Mapping

| Sage Type | Spec Category | Justification |
|-----------|--------------|---------------|
| `FreeQuadraticModule_generic` | `FormedModules(R).Bilinear()` plus free finite-rank module refinements | free quadratic module over commutative ring |
| `FreeQuadraticModule_generic_pid` | `FormedModules(R).Bilinear()` plus free finite-rank `OverPID()` refinements | adds span/span_of_basis with PID structure |
| `FreeQuadraticModule_generic_field` | `FormedModules(K).Bilinear()` plus free finite-rank `OverField()` refinements | over a field (= vector space with form) |
| `FreeQuadraticModule_submodule_*_pid` | forms-owned bilinear subobjects over PID | submodule of free quadratic over PID |
| `FGP_Module_class` | `Modules(R).FinitelyPresented().OverPID()` | V/W presentation; no form |
| `TorsionQuadraticModule` | `forms.subcategories.torsion_quadratic_modules.TorsionQuadraticModulesCategory` | V/W with Q/mZ-valued bilinear form |
| `FreeQuadraticModule_integer_symmetric` | forms-owned finite-rank free symmetric nondegenerate integral bilinear chain, then `Lattices(ZZ)` | the canonical integral lattice |
| `QuadraticForm` | forms-owned finite-rank free symmetric nondegenerate integral bilinear chain, then `Lattices(ZZ)` | same category; different presentation (upper-triangular coefficients) |

**Note on `QuadraticForm` vs `FreeQuadraticModule_integer_symmetric`**: Both represent
the same mathematical object (an integral lattice). Sage keeps them as separate classes
for historical reasons. Our spec treats them as objects in the same category; the
constructor `Lattices(ZZ).Constructors().from_quadratic_form(qf)` converts between them.

---

## What Lives in `forms/` vs What Lives in `lattices/`

### Lives in `forms/`

The forms subtree owns the formed-module hierarchy:

- `FormedModulesCategory`
- `BilinearModulesCategory`
- `QuadraticModulesCategory`
- `SymmetricBilinearModulesCategory`
- `AlternatingBilinearModulesCategory`
- `NondegenerateBilinearModulesCategory`
- `DefiniteBilinearModulesCategory`
- `IndefiniteBilinearModulesCategory`
- `IntegralBilinearModulesCategory`
- `RationalBilinearModulesCategory`
- `FreeBilinearModulesCategory`
- `TorsionQuadraticModulesCategory`

### Lives in `lattices/subcategories/`

Only lattice-specific axiom classes live here:

- `over_dedekind.py` — `_LatticesOverDedekindDomain`
- `over_pid.py` — `_LatticesOverPID`
- `over_integers.py` — `_LatticesOverIntegers` (canonical `Lattices(ZZ)`)
- `even.py` — `_EvenLattices`
- `unimodular.py` — `_UnimodularLattices`

The former lattice files for generic formed-module axioms are compatibility shims that
import the forms-owned classes.

### Discriminant groups live in `lattices/subcategories/constructions/discriminant_groups.py`

`DiscriminantGroups(ZZ)` = finite torsion formed modules with discriminant form data.
The full discriminant group method surface lives here, while generic torsion quadratic
module ownership lives in `forms`.

The standard type package is owned by
`lattices/subcategories/constructions/discriminant_groups.py` and re-exported through
`types.py` as `DiscriminantGroup`, `DiscriminantGroupElement`,
`DiscriminantGroupMorphism`, `DiscriminantGroupHom`, `DiscriminantGroupEnd`,
`DiscriminantGroupAut`, and the corresponding Hom/End/Aut category and element names.
These names use the module Hom/End/Aut machinery as the categorical carrier; when the
base category is `Lattices(R).DiscriminantGroups()`, containment is interpreted in the
finite torsion formed-module category, not as raw matrices or Sage torsion backends.

The required finite discriminant-form surface includes named access to the bilinear and
quadratic quotient-valued forms, inherited generic isotropic predicates, finite
`isotropic_elements()` enumeration, and `orthogonal_group()`. Orbit decomposition is
exposed by the resulting `DiscriminantGroupAut` or a typed finite group-action object
through `orbit(x)`, `orbits(S)`, and `orbit_representatives(S)`. Lattice orthogonal
groups expose `discriminant_action()`, `image_in_discriminant_orthogonal_group()`, and
`kernel_of_discriminant_action()` to connect lattice isometries to discriminant-form
automorphisms. These methods are not owned by `nikulin_invariants()`.

---

## Dual Convention: `dual()` vs `lattice_dual()`

The metric dual `L^# = {v ∈ L_K : β(v, L) ⊆ R}` and the Hom dual
`L^* = Hom_R(L, R)` are distinct mathematical objects kept as separate types with
compatible surfaces.

### Justification for the distinction

The degenerate case `<e> ⊂ U` (a generator of the hyperbolic plane) proves the
distinction is necessary:

- The Hom dual `<e>^* = Hom_Z(<e>, Z) ≅ Z`, carrying the evaluation pairing
  `(f, e) ↦ f(e)`. Its elements are functionals.
- The metric dual `<e>^# = {v ∈ <e>_Q : β(v, <e>) ⊆ Z}`. Since
  `β(e, e) = 0`, the condition `β(v, e) ∈ Z` imposes no restriction on the
  rational multiple of `e`. So `<e>^# ≅ Q·e`, not `Z`. These are fundamentally
  different objects — one is rank-1 free, the other is rank-1 rational.

In the nondegenerate integral case, both duals are canonically isomorphic via
`v ↦ β(v, –)`, but the isomorphism is structure-dependent (it uses the form)
and must be recorded explicitly.

### End-user convention: `lattice_dual()`

The **lattice** subcategory overrides the dual surface so that users working with
concrete lattices (integral formed modules) get the expected behavior:

- `L.lattice_dual()` → the metric dual `L^#`, returned as a **lattice** (formed
  module). This is the standard meaning of "dual lattice" in the lattice theory
  literature and the object needed for discriminant group computations.
- `L.dual()` → in the `Lattices(R)` category, `dual()` is overridden to call
  `lattice_dual()`, returning the metric dual. A diagnostic-level log message
  (gated by the global category diagnostic flag) informs the user that the metric
  dual is being returned, not the module-theoretic Hom dual.
- `L.hom_dual()` → the Hom dual `Hom_R(L, R)`, returned as a module. Available
  when the module dual is needed as a bare `R`-module without the transported
  form data.

### Subcategory override rules

- `Modules(R).ParentMethods.dual()` returns `Hom_R(M, R)` (the generic module
  dual). No log warning.
- `Lattices(R).ParentMethods.dual()` overrides to call `lattice_dual()`, with
  the optional log warning described above.
- `BilinearModules(R).ParentMethods.dual()` keeps the generic module dual
  (no form transported). The metric dual `L^#` is accessed via
  `L.dual_lattice()` at `Free + Bilinear.Symmetric.Nondegenerate.Integral`.
- Subcategories of lattices (even, unimodular, over_integers) inherit the
  override from `Lattices(R)`.

### Diagnostic logging convention

All dual-like methods that may confuse metric duals with Hom duals participate
in the global category diagnostic system specified in `[[SPEC-MAPPING-CAT]]`:

- Warnings are gated by the disabled-by-default diagnostic flag.
- When enabled, `L.dual()` on a lattice logs: "Returning metric dual L^#;
  use L.hom_dual() for the Hom-dual module."
- The log level is `INFO` and the message is explanatory, not a correctness
  check.
- The same convention applies to `discriminant_class()` and `inclusion_morphism()`
  — any method that returns or uses metric-dual data.

### Resolved design decisions

- `dual()` is NOT removed from the lattice subcategory. It is overridden to
  return `lattice_dual()`, aligning normative lattice-theory usage.
- `lattice_dual()` is the unambiguous name for the metric dual. No other
  category owns this name.
- `hom_dual()` is the unambiguous name for the module-theoretic Hom dual on
  formed-module categories.

## 6-Gate Protocol Review Log

**Review date:** 2026-05-07
**Reviewer:** Hermes Agent (fresh-context subagent)
**Scope:** Core mathematical correctness — tier table, forms/lattice boundary, discriminant group. Less exhaustive than full Sage file scan; prioritizes mathematical reasoning.

---

### G1 — Source Grounding: PASS

Every mathematical claim in the spec traces to a canonical source. Verified source references:

| Claim | Source checked | Result |
|-------|---------------|--------|
| Source Coverage Ledger (lines 44-63) | 13 installed Sage files probed via `search_files` on `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/` | All 11 named files confirmed present. Two visibility-gap entries (categories/bilinear_modules.py etc.) correctly flagged as requiring follow-up via TASK-MAPPING-DOC-COMPLETENESS-RESEARCH. |
| Constructor reconciliation table Sage line references (lines 109-117) | `free_quadratic_module.py:310`, `free_quadratic_module_integer_symmetric.py:625`, `torsion_quadratic_module.py:20/190`, `quadratic_form.py:1150+` | Line ranges verified against Sage 10.7 source. The `__init__` signatures match the spec's descriptions. |
| LatticesCategory chain (lines 247-281) | `/home/dzack/research/category_specs/lattices/__init__.py:68-71` — `_base_category_class_and_axiom = (IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory, "Lattice")` | Confirmed. The lattice endpoint sits at the end of the forms chain. |
| Forms chain (lines 247-281) | `/home/dzack/research/category_specs/forms/chain.py:30-296` — `FiniteRankFreeFormedModulesCategory` → `Bilinear` → `Symmetric` → `Nondegenerate` → `Integral` | Confirmed. Each link's `_base_category_class_and_axiom` matches. |
| TorsionQuadraticModulesCategory | `/home/dzack/research/category_specs/forms/subcategories/torsion_quadratic_modules.py:17-60` — `super_categories()` joins Torsion, Quadratic(WithForms), FinitelyPresented | Confirmed. Abstract methods `gram_matrix_quadratic`, `gram_matrix_bilinear`, `brown_invariant` present. |
| DECISION-ORDERED-REAL-SIGNATURE-OWNER | `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-ORDERED-REAL-SIGNATURE-OWNER.md` — status: `decided`, chosen: "Add ordered-real-realization refinement" | Confirmed. The spec's `signature_pair()` tier assignment reflects this decision. |
| SPEC-MAPPING-CAT cross-reference | `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-CAT.md` — exists at 528+ lines | Confirmed. Diagnostic flag gating documented there. |
| Formal Negative findings (lines 180-238) | `.agents/theory/spec-backups/lattices_written_spec_backup.py` — confirmed present; no active `src/lattices/categories/` — confirmed absent | Both findings verified. The docstring model and stale-path conclusions are correct. |

**G1 finding (advisory):** The hierarchy overview diagram (lines 249-255) omits `.Free().FiniteRank()` from the canonical chain. The actual chain in `chain.py` starts at `Modules(R).Free().FiniteRank().WithForms()`. The method placement table correctly prefixes tiers with `Free +` where needed (e.g., `Free + Bilinear` for `gram_matrix()`), so the tier assignments are internally consistent. The diagram is simplified for readability; this is acceptable for a mapping spec but may confuse readers comparing against the Python source.

**G1 verdict: PASS.** All sources resolve on disk. One advisory on diagram simplification.

---

### G2 — Sage Surface Completeness: PASS

The spec accounts for every inventoried Sage lattice surface through four reconciliation tables plus the method placement table:

| Inventory section | Coverage | Check |
|------------------|----------|-------|
| `FreeQuadraticModule` / `IntegralLattice` constructors (lines 109-117) | 8 Sage surfaces mapped | All 8 have owner classification + reconciliation rows |
| Inherited Module and Hom Surfaces (lines 119-130) | 11 surface groups (FGP_Module, FGP_Morphism, FGP_Element, enumeration) | All admitted or routed to correct owners |
| Toric Character-Lattice Boundary (lines 131-147) | 4 surface groups | Correctly routed to free-module/formed-lattice owners; toric-dual convention flagged as interop limitation, not negative claim |
| Lattice and Form Method Reconciliation (lines 149-163) | 18 surface groups | All have correct owner classification |
| Torsion and Discriminant-Form Reconciliation (lines 165-178) | 11 surface groups | All admitted with codomain/hypothesis precision |
| Method Placement Table (lines 285-362) | 60 method rows | Covers free, bilinear, quadratic, torsion, discriminant-group, and aut-group methods |

**Cross-reference check:** The method placement table rows are consistent with the reconciliation tables. Specifically verified:
- `gram_matrix()` at `Free + Bilinear` ↔ reconciliation says "Admit at the first free bilinear tier" (line 154) ✓
- `dual_lattice()` at `Free + Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` ↔ reconciliation lines 155-156 ✓
- `discriminant_group()` at same tier ↔ reconciliation lines 155-156 ✓
- `is_even()` at `Bilinear.Integral` ↔ reconciliation lines 155 ✓
- `orthogonal_group()` at `Modules(R).WithForms().AutCategory()` ↔ reconciliation lines 160 ✓

**G2 finding 1 (advisory):** Inherited module surfaces from the FGP reconciliation table (cardinality, is_finite, list, __iter__, random_element — line 129) are not represented in the method placement table. The spec's note says "Preserve as set/module runtime surfaces," which is correct inheritance from `Modules(R).Finite()` or `Sets().Finite()`, but a row in the method placement table confirming they're inherited (not lattice-owned) would close the audit loop.

**G2 finding 2 (advisory):** The `cokernel` gap flagged in line 127 ("cokernel remains a required project-owned gap") is correctly identified as a spec obligation not covered by Sage. The method placement table has no `cokernel()` row — this is a genuine spec gap that should become a tracked task, not a spec defect. The obligation is preserved (Gate 6).

**G2 verdict: PASS.** All inventoried Sage surfaces accounted. Two advisory findings on documentation completeness.

---

### G3 — Mathematical Correctness: PASS with ADVISORY NOTES

This gate focuses on the tier table, forms/lattice boundary, and discriminant group.

#### 3a. Tier Table Correctness

Verified the mathematical justification for 12 key tier assignments:

| Method | Claimed tier | Mathematical check | Result |
|--------|-------------|-------------------|--------|
| `b(v,w)` | `Bilinear` | Bilinear evaluation defined once form is bilinear | CORRECT |
| `gram_matrix()` | `Free + Bilinear` | Requires basis; entries `b(e_i,e_j)` in R | CORRECT |
| `determinant()` | `Free + Bilinear` | `det(gram_matrix)`; basis-dependent | CORRECT |
| `dual_lattice()` | `Free + Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` | Metric dual `L^# = {v in L_K : beta(v,L) subset R}` requires free (for scalar extension), symmetric, nondegenerate (for finite index), integral (for L subset L^#), over integral domain (for Frac(R)) | CORRECT. Each hypothesis is necessary. |
| `discriminant_group()` | same as `dual_lattice()` | `L^#/L` follows from `dual_lattice()` | CORRECT |
| `signature_pair()` | `Free + Symmetric + ordered real realization` | Inertia after extension to ordered real target; bare integral domain insufficient | CORRECT. Reflects DECISION-ORDERED-REAL-SIGNATURE-OWNER. |
| `is_even()` | `Bilinear.Integral` | `b(m,m) in 2R` requires integrality, not freeness | CORRECT |
| `is_unimodular()` | `Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` | `L = L^#` depends on `dual_lattice()` | CORRECT |
| `orthogonal_group()` | `Modules(R).WithForms().AutCategory()` | `O(M,b) = Aut(M,b)`; no freeness/nondegeneracy needed for definition | CORRECT. Verified against `chain.py:54-60` where `orthogonal_group()` is defined at `FiniteRankFreeFormedModulesCategory.ParentMethods`. Note: the Python implementation is at the finite-rank-free tier, but the spec correctly places the mathematical definition higher (at generic WithForms). The implementation's lower placement is a runtime convenience; the spec's tier is the correct mathematical owner. |
| `divisibility(v)` | `Bilinear.Symmetric` (element) | `<b(v,w) : w in M>` as submodule; symmetry needed so `b(v,w)` and `b(w,v)` generate same ideal | CORRECT. Note 9 (lines 449-454) provides rigorous justification. |
| `reflection(v)` | `Free + Symmetric + Nondegenerate` (element) | `s_v(w) = w - 2b(v,w)/b(v,v) · v` | CORRECT as a mathematical formula, but see advisory G3-a below. |
| `brown_invariant()` | `Torsion + Bilinear + Symmetric` | Global torsion QF invariant | CORRECT. The spec correctly notes the QQ/2ZZ codomain requirement. |

**Advisory G3-a (reflection tier):** The reflection formula requires `b(v,v)` to be a unit in the coefficient ring. Nondegeneracy guarantees the radical is zero but does NOT guarantee `b(v,v)` is invertible (e.g., `b(v,v) = 2` is not a unit in Z). For ZZ-lattices, reflections are only well-defined as automorphisms when `b(v,v) ∈ {±1, ±2}`. The spec's placement at `Free + Symmetric + Nondegenerate` is correct for the mathematical formula in the scalar extension, but the result may not be an automorphism of the original lattice. This tension is inherent in the mathematics (reflections of an integral lattice typically live in the rational span), and the spec's tier assignment is acceptable for a mapping surface — implementation cards will need to handle the unit-check precondition.

**Advisory G3-b (form_degree convention):** The spec defines `form_degree() -> (p,q)` at `WithForms` with values `(1,1)` for bilinear and `(1,0)` for linear (line 293). In standard multilinear algebra, a bilinear form `M × M → R` has tensor type `(0,2)`, and a linear form has type `(0,1)`. The spec's convention `(1,1)` appears to count "inputs per slot" rather than covariant/contravariant degree. This is nonstandard and should either be explicitly defined as a project-specific convention or corrected to the standard (0,2)/(0,1) notation. **Not blocking** — the concept is clear regardless of convention — but implementers coming from multilinear algebra will be confused.

**Advisory G3-c (discriminant sign convention):** The spec defines `discriminant()` as `(-1)^r * det` (line 309). The standard discriminant of a quadratic form in r variables uses factor `(-1)^{r(r-1)/2}`. Sage's `FreeQuadraticModule_generic.discriminant()` uses `(-1)^{rank} * det` (confirmed at `free_quadratic_module.py:439`). The spec faithfully maps Sage's convention, but the sign convention should be explicitly noted as "following Sage's convention" to avoid confusion for readers who expect the quadratic-form discriminant. **Not blocking** — the spec's role is to map Sage surfaces, and it maps this one correctly.

#### 3b. Forms/Lattice Boundary Correctness

The boundary is clean and mathematically justified:

- **forms/** owns: FormedModules, Bilinear, Quadratic, Symmetric, Alternating, Nondegenerate, Definite, Indefinite, Integral, Rational, FreeBilinear, TorsionQuadraticModules (lines 522-537)
- **lattices/subcategories/** owns: OverDedekindDomain, OverPID, OverIntegers, Even, Unimodular (lines 539-547)
- **lattices/subcategories/constructions/** owns: DualObjects, DualLattices, Overlattices, OrthogonalDirectSums, DiscriminantGroups (lines 249-280)

**Verification:**
- The lattice category at `lattices/__init__.py:68` extends `IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory` with axiom `"Lattice"`. This means the lattice endpoint adds only the `Lattice` axiom name — all formed-module axioms (Bilinear, Symmetric, Nondegenerate, Integral) are owned by forms. Mathematically correct: a lattice is an integral nondegenerate symmetric bilinear module that happens to be free of finite rank, and the "Lattice" axiom is the named endpoint.
- The `Even` and `Unimodular` subcategories are lattice-specific (nonstandard outside lattice theory). Correct ownership.
- The `DualLattices()` construction is correctly distinguished from `DualObjects()` (Hom-dual) — the degenerate case `<e> ⊂ U` (lines 586-594) provides a rigorous counterexample proving the two duals differ. This is strong mathematical evidence.

**Advisory G3-d (dual_lattice tier gap):** The spec places `dual_lattice()` at `Free + Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` (line 314), but the Python chain in `chain.py` does not include `OverIntegralDomain` as a separate axiom — the `Integral` axiom in the chain sits on top of `Free().FiniteRank()`, which already provides the fraction field via the base ring's `fraction_field()` method. The spec's tier description is mathematically precise (it names the hypotheses) but the project's actual category graph may not have a separate `OverIntegralDomain` refinement. This is a spec/implementation alignment detail for the implementation phase, not a mathematical error.

#### 3c. Discriminant Group Correctness

The discriminant group surface is mathematically well-defined:

- `A_L = L^#/L` is a finite abelian group with descended bilinear form `b_L: A_L × A_L → Q/Z` and (when L is even) quadratic form `q_L: A_L → Q/2Z`
- The spec correctly identifies the codomains as quotient-valued (`K/R`, `K/2R`), distinct from integral Gram matrices (lines 170-171)
- `discriminant_action()` is correctly identified as the canonical bridge `O(L) → O(A_L, q_L)` (line 177)
- `nikulin_invariants()` is correctly identified as a convenience invariant under 2-elementary hypotheses, not a substitute for the discriminant group (lines 335, 456-465)
- Orbit methods (`orbit`, `orbits`, `orbit_representatives`) are correctly owned by finite group actions, not by `nikulin_invariants()` (lines 176, 348)
- The type package (`DiscriminantGroup`, `DiscriminantGroupElement`, etc.) correctly uses the module Hom/End/Aut machinery (lines 558-565)

**Advisory G3-e (cokernel gap):** The spec acknowledges (line 127) that the `cokernel` object with descended form data is a required project-owned gap — Sage provides `kernel`, `image`, and `lift` on FGP_Morphism but not a formed `cokernel` with the descended bilinear/quadratic form. This is a genuine spec obligation that should become a tracked implementation task. The gap is correctly documented and does not affect spec correctness.

#### 3d. Picard Lattice vs Picard Group

The task requested checking this distinction. The spec `SPEC-MAPPING-LATTICES.md` does not address Picard lattices or Picard groups. This is correct scope discipline: Picard groups (divisor class groups) and Picard lattices (Néron-Severi lattices with intersection form) are geometry concepts owned by geometry categories, not by the algebraic lattice mapping surface. The distinction is properly treated in the geometry spec `SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE.md` (line 72: "Picard group is not the Picard lattice"). No mathematical conflation exists in this mapping spec.

**G3 verdict: PASS.** Five advisory notes recorded (G3-a through G3-e). All are documentation/clarification items, not mathematical errors. No tier assignment is wrong. No boundary is misplaced. The discriminant group surface is mathematically correct.

---

### G4 — Nonmathematical Rejection: PASS

The spec correctly rejects or marks as interop-only:

| Surface | Classification | Check |
|---------|---------------|-------|
| `ambient_module`, `ambient_vector_space`, `basis_matrix`, `inner_product_matrix`, `degree`, `_repr_` (line 153) | private/runtime/display/interop | Correctly rejected as public lattice semantics. These are Sage ambient-space implementation details. |
| `hom(images)` as main constructor (line 126) | rejected; Hom-parent constructors admitted instead | Correct. `hom(images)` is an ad hoc Sage convenience; the spec routes through `M.Hom(N)` and structured constructors. |
| `discard_basis` option (line 116) | rejected as public option | Correct. Basis changes must be explicit. |
| Sage's variadic `short_vectors(n, **kwargs)` (line 341) | rejected; `short_vectors_up_to_sign(n)` admitted | Correct. The single keyword `up_to_sign_flag` is split into a named method. |
| Raw Sage `Parent`/`Element` surface leaks | absent from public spec | Verified: the spec consistently uses project type names (Lattice, DiscriminantGroup, etc.). |
| `nikulin_invariants()` as discriminant-form owner (line 335) | rejected; convenience tuple only | Correct. The discriminant group + form is the canonical object. |
| `genus()` result owning the method (line 173) | rejected; "do not let the result object own the method" | Correct. The genus is evidence; lattice theorem methods own the verdict. |

**G4 verdict: PASS.** All nonmathematical Sage surfaces correctly rejected or marked interop-only. No "option bag" constructors or raw Sage types leak into the public API.

---

### G5 — Ambiguity Routing: PASS

The spec routes mathematical ambiguities through tracked decision cards:

| Ambiguity | Routed to | Status |
|-----------|----------|--------|
| Signature/definiteness owner (lines 156, 302-304, 377-382) | `[[DECISION-ORDERED-REAL-SIGNATURE-OWNER]]` | `decided` — "Add ordered-real-realization refinement" |
| Diagnostic flag for dual-vs-metric-dual (lines 399-409, 628-639) | `[[SPEC-MAPPING-CAT]]` | exists at `plans/features/.../SPEC-MAPPING-CAT.md` |
| Source-visibility gaps from inventory (line 63) | `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]` | tracked |
| Missing `cokernel` with descended form (line 127) | documented gap; not yet a tracked task | Should become a tracked card; see G6 recommendation |

**G5 finding:** The cokernel gap (line 127) is documented but not routed to a specific tracked card. This is a minor routing completeness issue — the gap is acknowledged and its mathematical shape is specified, but no tracker ID is given. Recommend creating a task card for "formed cokernel with descended bilinear/quadratic form" or explicitly deferring it.

**G5 verdict: PASS.** One routing recommendation.

---

### G6 — Obligation Preservation: PASS

The spec preserves all Sage obligations and adds project-owned ones:

| Obligation | Status |
|-----------|--------|
| Every Sage lattice/formed-module surface inventoried in SAGE_INVENTORY.md | Preserved — each has a reconciliation row, owner classification, and mapping consequence |
| `element divisibility` (line 159) — Sage does not supply this | Added as required project surface with definition at Note 9 |
| `cokernel` with descended form (line 127) | Documented as required gap |
| `inclusion_morphism()` (line 317) — Sage does not supply this | Added at correct tier |
| `discriminant_form()` (line 316) | Added as named accessor |
| `rational_span()` (line 343) | Added at `Free + OverIntegralDomain` |
| `is_isometric_to()` (line 336) | Added as lattice isometry test |
| `discriminant_class(x)` (line 358) | Correctly owned by metric-dual element |
| `special_orthogonal_group()` / `stable_orthogonal_group()` (lines 330-331) | Correctly routed through Aut-category parent methods |
| Dual convention preservation (lines 578-648) | `dual()` is overridden (not removed); `lattice_dual()` and `hom_dual()` added as unambiguous names |

**G6 finding:** The `cokernel` gap (line 127) is a genuine spec obligation that exceeds current Sage coverage. It should become a tracked implementation task. The obligation itself is correctly specified and preserved.

**G6 verdict: PASS.** No obligations deleted, weakened, or relocated without grounded replacement.

---

### Summary

| Gate | Result | Blocking? |
|------|--------|-----------|
| G1 Source Grounding | **PASS** | No |
| G2 Sage Surface Completeness | **PASS** | No |
| G3 Mathematical Correctness | **PASS** with 5 advisories | No |
| G4 Nonmathematical Rejection | **PASS** | No |
| G5 Ambiguity Routing | **PASS** | No |
| G6 Obligation Preservation | **PASS** | No |

**Overall verdict: PASS.** The spec is mathematically sound, the tier table is correct, the forms/lattice boundary is clean and rigorously justified, and the discriminant group surface is complete. Five advisory notes (G3-a through G3-e) identify documentation improvements and one implementation-planning gap. None are blocking for spec advancement.

**Advisory notes requiring no action before advancement:**
1. G3-a: Reflection tier — note that `b(v,v)` unit-check is a runtime precondition
2. G3-b: `form_degree` convention — clarify or correct to standard (0,2)/(0,1)
3. G3-c: Discriminant sign — note Sage-convention provenance
4. G3-d: `dual_lattice` tier — `OverIntegralDomain` vs actual category graph alignment
5. G3-e: Cokernel gap — should become a tracked implementation task

**Recommended follow-up:** Create a task card for the formed cokernel with descended bilinear/quadratic form (G5/G6 finding) if not already tracked.

---

## Compatibility Paths

`modules/subcategories/with_forms.py`, `modules/subcategories/bilinear.py`,
`modules/subcategories/quadratic.py`, `modules/subcategories/torsion_quadratic_modules.py`,
and the old generic formed-module files in `lattices/subcategories/` re-export the
forms-owned classes. They exist only to preserve old import paths.

Former ordinary lattice-element calls to `v.discriminant_class()` are represented as
`L.inclusion_morphism()(v).discriminant_class()` or, equivalently, the zero element of
`L.discriminant_group()`.

Former lattice-object calls to `L.special_orthogonal_group()` and
`L.stable_orthogonal_group()` are represented by first taking the lattice aut object:
`L.orthogonal_group().special_orthogonal_group()` and
`L.orthogonal_group().stable_orthogonal_group()`. The subgroup constructors live on
`Lattices(R).AutCategory().ParentMethods`; `special_subgroup()` and
`stable_subgroup()` are the primitive subgroup selectors there.
