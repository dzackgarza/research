# Architecture and issue-evidence audit, 2026-10-25

The observed problem crosses instructions, public category construction, source
inspection, tests and issue disposition. Repairing the wording of #597 cannot
resolve it. The records below identify distinct mechanisms and their affected
owners; they do not certify the mathematics of the remaining implementation.

## Population and limits

The activity window is 2026-10-24 09:35:16 through 2026-10-25 09:35:16 UTC.
Local reachable history contains 247 commits in that window, touching 50 paths:
124 commits touch `src/`, 110 touch tests without touching `src/`, and 13 touch
neither. These are disjoint activity counts, not completion counts. The endpoint
comparison is `311b8f6faf38c8e82d7e61dccac79780202c96ce` to
`326c95a31b4893ffef1c1433da533df1351a2c24`; its source delta spans 18 files.
Merge ancestry and other hosts' unpublished work are not established by this
inventory. Live GitHub issue bodies were read for #384, #606, #603, #562 and #498;
closure evidence for #597, #598, #492, #354 and #605 was inspected earlier in
the same investigation.

Detailed call/source inspection covered the category parser, `OwnedCategory`,
category base adapters, ring additive placement, native module construction,
lattice property membership, the Nikulin table validator and its test, bilinear
descent, radical quotient construction, and the set-layer handoff. The remaining
changed source families include ADE construction, Sterk indexing, algebra
construction, ring finiteness and centrality, and minimal-prime loci. Their
individual mathematical algorithms have not all been independently audited.
No preamble execution or mathematical acceptance was performed in this audit.

## Instructions still prescribe the runtime slated for removal

`CONTRIBUTING.md`, “Layers and permitted dependencies”, assigns public semantics
to the formal catalogue and `lean-cas-dsl`. Commit `1a7cf5096a` explicitly replaced
the earlier Python-runtime ownership table. Its TODO change says #384/#556
precede repairs to the transitional runtime they retire.

However, `AGENTS.md`, “The preamble category is the only extension point”, still
directs placement through `ObjectType`, `ElementType` and category-generated
arrow types. “The preamble is a universe over Sage” prescribes owned public
objects and a Sage session with shadowed names. `OWN-03` still prescribes
construction through immediate structure owners and inherited initialization.
These are concrete implementation instructions, whereas the migration direction
is expressed principally as a future replacement.

The inconsistency is operational: a worker following the detailed instructions
can extend the runtime that the priority rule says to replace. Calling this
runtime transitional does not determine which new edits are necessary for
migration. Each such edit needs a demonstrated consumer migration dependency.
#384 and #606 own that migration; no completed layer follows merely from the
policy-table correction or dependency pin.

Another unresolved instruction pair appears in “A missing foundation parks the
work that found it”. One paragraph says research has no notion until its formal
release; another says an algorithm is written as a preamble-category method
whether or not the notion is formalized. Independent algorithm development can
coexist with a missing public operation, but these instructions do not consistently
keep that private computation separate from public category extension.

## Implementation behavior still decides public category membership

Commit `78583f57ea` adds `Twisted` and `Untwisted` property categories in
`categories/lattices.py`; `24b785eb53` adds `Indecomposable` and enumeration methods.
Their `__contains__` implementations call local Python predicates and return
their Boolean answers as membership. The classes install names into Sage's
`all_axioms`. `OwnedJoinCategory.__contains__`, added in `78583f57ea`, discovers
`_certifying_predicate` through the Python MRO and combines branch membership.

This is a concrete local route from implementation methods to public category
membership. Its mathematical predicates may have correct algorithms; that does
not turn the route into a catalogue-derived classifier. The inspected route
does not consume a formal registration or the semantic kernel. It extends the
mechanism #384 requires retiring. The audit does not claim that no corresponding
formal mathematics exists elsewhere: that correspondence still needs to be
traced, including exact classifier identities and the public consuming path.

## Constructor repairs repeat membership declarations

`OwnedRngs.super_categories()` already names the additive commutative group
category. `2bbab736af` adds that declaration directly to `OwnedRings` too.
`4457492d9e` adds it to restricted-scalar module placement. `c6aec764d7` moves
an additional placement into the ring constructor before construction hooks.
The comments explain that category joins do not necessarily materialize the
inherited interface before native module construction needs it.

`_RingModulePresentation.construct` in `categories/modules/native_modules.py`
requires membership in `AdditiveGroups().AdditiveCommutative()` and then retains
a presentation on, and potentially refines, the supplied object. This connects
the repeated declarations to an actual consuming prerequisite.

The inspected formal counterpart is
`LeanCategories/Catalogue/Semantics/Algebra/Ports.lean::ringsAdditive`, an explicit
forgetful functor, and
`Semantics/Modules/CatalogueRegistration.lean::regularModule`, which constructs
`ModuleCat.of R R` and proves its additive structure and scalar action.
The Python placement edits do not show a consumer moving through those formal
operations. They repair the existing class construction route. Whether each
repair is needed for a particular migration remains unestablished; ordinary
ring mathematics alone does not establish that implementation choice.

## A test delegates its assertion to the implementation

`b30bf3f019` adds `_TwoElementaryTable.validate()` in `preamble/catalogue.py`.
That method computes and checks rank, category membership, invariants and
signature using the same package, then returns `True`.
`9904d7f423` adds `assert TwoElementary.validate() is True` to
`tests/lattices/test_nikulin_classification.sage`.

The implementation now owns the assertions behind that test line. Changing the
method to return `True` removes those checks without changing the test. The
independent cardinality assertions already in the test are separate and are not
invalidated by this observation. A local diagnostic is not itself evidence of
leaf correctness; the new assertion cannot count toward the independent
acceptance required by the evidence model. Its actual contribution to any
reported acceptance or closure must be checked, rather than inferred from the
method's name.

## Source descriptions become repeated apparent authority

`ringed_spaces.py::DistinguishedAffineCovers` calls its no-argument branch a
catalogue and names it in the parameterized branch's `super_categories()`.
The generated megadoc repeats the docstring. `65de001e62` adds
`_catalogue_and_fibre` to the graph parser to recognize that optional-parameter
source shape. Its commit and #597's closure describe the resulting distinct
vertices and successful source slice.

These establish a source-inspection repair. They are dependent records of the
same Python declaration, not independent definitions of catalogue, fibre or
inclusion. Neither agreeing with that declaration nor rejecting it because of a
conversational correction settles the mathematics. The total-category/family
construction, objects, arrows and relevant functor have not been independently
identified for this example. Do not promote the parser's labels to definitions.

The review environment can reinforce this mistake. The loaded anti-slop skill
in `~/ai/opencode/skills/anti-slop/SKILL.md` tells reviewers that unusual design
choices are almost certainly user-driven and should be treated as premises.
That instruction is not evidence of authorship or mathematical validity. It
cannot govern an investigation explicitly questioning those premises. The
skill is outside this repository and was not changed here.

## Closure records have already required correction

[#603](https://github.com/dzackgarza/research/issues/603) is reopened: its recorded
rank-two pairing and correct quotient-map acceptance was not established by
source changes and unexecuted assertions. Moving execution to terminal T did
not discharge the original issue. Its comments preserve that correction.

[#562](https://github.com/dzackgarza/research/issues/562) is also reopened. One
comment reports targeted probes passing; the following correction says those
probes occurred during the pre-T suspension and did not discharge the full
final-revision, finite/infinite-family acceptance. This is a second instance of
completion evidence being reconsidered, not a deduction from #603.

The two issues do not show that every closure is invalid. They show why issue
state and source activity alone cannot answer how much required work was done.
For each closure, recover its complete obligation and compare the actual
delivered construction and evidence. Keep source implementation, formal proof,
consumer migration and final computational acceptance distinct.

## Required extent of reconciliation

The affected surface is broader than the eighteen source files changed that
day: their shared category machinery and the instructions for extending it
are dependencies of later work. The examples above establish that reach; they
do not establish that every dependent construction is wrong.

Use #384/#606 to reconcile the active implementation prescriptions and the
actual public consumer route with the final architecture. For each mathematical
layer, identify the formal definitions and structural maps, the kernel's actual
use of them, and the independent acceptance assertions. Existing Python classes
are implementation evidence to compare, not definitions to transplant.

The unresolved audit work is the complete layer-by-layer dependency census;
the disposition of the other changed algorithms and tests; the exact formal
construction for the cover example; and a full acceptance review of the day's
closures and reopened issues. These remain required before a programme-wide
extent or progress percentage can be stated. This record makes no such claim.
