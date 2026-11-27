# Test Suite Audit — conformance to the math-fact + Zotero-citation standard

Audited all 83 test files (`tests/**` + `category_specs/**/*.sage`) against the standard
in vault memory `What A Test Cites`. A test conforms iff it (1) asserts a real
mathematical fact, (2) does not assert software/engineering properties or source/graph
structure as the point, (3) cites any literature value as Zotero item key + text/markdown
extraction attachment key + specific verified line.

**Result: 1 file conforms** (`tests/category_specs/test_root_lattice_facts.py`, the WS-1
exemplar). Every other file fails on at least one axis. The failures cluster into three
classes.

## Class 1 — META: assertions on source / category-graph structure (must be replaced)

These assert `X is Y.ParentMethods`, `abstract_method_has_name(...)`, `obj in Cat()` as
the point, `_base_category_class_and_axiom == (...)`, class/parent-class identity,
`issubclass(...parent_class...)`. They verify the category *wiring*, not mathematics.
This is the meta-assertion engine defect (ROADMAP "the gating tests are not
mathematical").

- Every `*/category_obligations.sage`: cat, forms, homsets, lattices, lattices/chain,
  modules, posets, algebras, tensor_algebra_components, topological_spaces, sets, rings.
- `type_alias_obligations.sage` (almost entirely alias-identity meta).
- `sets/tests/regression/set_partitions.sage` (100% category-graph, zero math).
- `rings/tests/regression/object_method_resolution.sage` (ABC/`__abstractmethods__`
  plumbing).
- `rings/tests/new_spec/{end_refinement,number_field_option_bag_split}.sage`
  (the latter also `ast.parse` + markdown-string asserts).
- `modules/tests/new_spec/category_refinement.sage`; `cat/tests/new_spec/subobject_predicates.sage`.
- pytest: `test_spec_core_categories.py`, `test_spec_core_constructor_specs.py`,
  `test_spec_core_reports.py`, `test_constructor_provenance.py`, and
  `test_spec_obligations.py` (Sage-membership-as-the-point across ~19 tests).
- `tests/sage_spec/category_construction_structure_spec.sage` §I.

Correction: replace each with a test that computes a mathematical value and asserts it
(cited where literature-sourced), OR — for tests of pure framework machinery (registry
cycle-rejection, ABC enforcement) — recognize they are not math tests; move the genuine
invariant into the spec/validator layer rather than masquerading as a test. **No
wholesale deletion without transferring the real obligation** (anti-laundering).

## Class 2 — SE: software-engineering assertions as the point (banned)

`pytest.raises`/assert-raises, `is` identity, `repr ==`, `hasattr`, bare-call-doesn't-raise,
`order() > 1`, `is_finite()`.

- pytest: `test_spec_core_categories.py`, `test_spec_core_constructor_specs.py`,
  `test_spec_core_reports.py`, `test_spec_core_inspection.py`,
  `test_free_module_witnesses.py` (negative-rank raises).
- `modules/tests/new_spec/surface_gaps.sage` (bare calls asserting non-raising).
- `tests/sage_spec/category_construction_spec.sage` (whole file = Sage-tower wiring).
- `variety_spec/automorphisms.sage` (`Aut.order()>1`, `is_finite()`);
  `variety_spec/variety_pairs.sage` (`StabilityWitness` scaffolding).
- minor blemishes: `disjoint_union_enumerated_sets.sage` (`is`),
  `enumerated_set_from_iterator.sage` (`repr ==`).

Correction: assert the actual mathematical value (the group order, the computed object),
not non-emptiness/type/identity/non-raising.

## Class 3 — UNCITED / LOCAL-CITE / VAGUE-CITE: real math, wrong/absent citation (migrate to Zotero)

These assert genuine mathematical facts but cite nothing, a local file, or a vague
textual reference. All literature-sourced values must migrate to Zotero
item-key + extraction-attachment + verified line.

- **LOCAL-CITE — `tests/fixtures/coble_literature_fixtures.json`**: all 14 entries cite
  `theory/references/literature/*.md` + `bibliographic_key` (aegs2023compact,
  pieroni2026coble, dolgachev2013rationality, thas1994, sterk1991). Largest single
  migration cluster.
- **LOCAL-CITE — modules regression**: `free_modules.sage`, `modules_with_basis.sage`,
  `lattices_and_torsion_quadratic.sage` (cite Sage docstrings / doc.sagemath.org).
- **VAGUE-CITE**: `sage_spec/research_workflows.sage` ("Nikulin 79 Thm 1.14.4", "Nam85
  2.13/2.15"); `variety_spec/{del_pezzo,automorphisms,stability,variety_pairs}.sage`
  headers ("SGA 7", "Manin", "DM69", "Kollár–Mori §2.3", "Mukai 1988", "Sterk 1985");
  all rings/sets regression headers ("sourced from sage doctests").
- **UNCITED** (genuine, mostly textbook facts, zero citation): the bulk of
  `tests/sage_spec/*` (class numbers, Krull dims, Tor/Ext, Coxeter A_4) and
  `tests/variety_spec/*` (genus-degree, K^2, Hodge, ADE, Riemann-Hurwitz, blowup Picard,
  K3 classification, toric RR, etc.), plus the math blocks of `posets`, `algebras`,
  `modules`, `lattices` obligation files and all rings/sets regression computations
  (elementary computed facts — these may be exempt from citation as elementary, but their
  Sage-doctest provenance comments are not Zotero citations).

Correction: for each literature value, resolve the source on the workstation Zotero
instance (`qmode=titleCreatorYear`), find its markdown extraction attachment, verify the
line, and cite item-key + attachment-key + line. Elementary computed facts (a finite set
has cardinality 5) need no literature citation but must not carry a fake/vague one.

## Correction strategy

This is the execution of ROADMAP WS-1 (fix the engine) + WS-3 (Coble surfaces), not a
mechanical pass. Per the chosen "one vertical slice" altitude:

1. The conforming exemplar exists: `test_root_lattice_facts.py`.
2. Correct **incrementally, area by area**, each slice producing math-fact tests with
   verified Zotero citations — not a single giant rewrite.
3. For Class-1 framework tests, decide per test: replace with a math-fact test, or move
   the invariant into the spec/validator layer (with the obligation transferred, not
   dropped).
4. Migrate `coble_literature_fixtures.json` to Zotero citations as one focused unit (it
   is the densest real-math cluster and directly feeds Coble research).

Counts (dominant tag per file/cluster): META ≈ 22 files, SE ≈ 8, LOCAL-CITE ≈ 18
(14 fixture entries + 3 modules regression + 1), VAGUE-CITE ≈ 12, UNCITED ≈ 30+
(variety_spec/sage_spec bulk), OK = 1.

## Slice outcome: META obligation tests -> math facts (2026-06-18)

Applied the lattices-exemplar conversion across all per-area `category_obligations.sage`
(+ `type_alias_obligations.sage`). Two outcomes:

**Converted to math-fact obligations (mixed files; all run green, exit 0):**
lattices, modules, posets, algebras, rings, sets, tensor_algebra_components. Kept only
real computed-value obligations (ranks, dimensions, determinants, cardinalities, orders,
characteristics, precisions, degrees, ideal/subalgebra dims, gram/scalar matrices, element
membership, group-action orbits, tensor structure constants, A_2 roots) — all elementary
computed facts (no fabricated citations; A_2 root count cited to SPLAG TCJKXU3D:4676).
Deleted the category-graph meta-assertions. Net ~-2000 lines.

**Pure-META (no DSL constructors that compute values -> nothing to keep; left intact,
NOT emptied):** forms, cat, homsets, lattices/chain, topological_spaces,
type_alias_obligations. These assert only category-graph structure (method ownership,
subcategory placement, type-package aliases, defining predicates, axiom ownership). Their
structural invariants are enumerated in the conversion subagents' reports and must migrate
to `category_specs/validators/` before these obligation files can be retired — this is the
**framework-tests -> validators** workstream. Until then they remain as-is (green,
testing structure); nothing is dropped.
