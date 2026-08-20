# n-category-tower — corpus INDEX

Landed 2026-08-20 from `gitclones/integral_lattice/cat/` (plus the repo-root
`newcat2.md`) by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, section R4-integral-lattice-cat-tower). Every
file keeps its original content under a prepended origin header. This INDEX
records what each cluster is, where its notions live now, and the
mathematical errors the corpora audit found — **a recorded divergence or
error is a finding, not a defect to repair in place**.

## What this corpus is

A specification tower for a toy model of (∞,n)-categories, written in three
stages (`README.md`: specification ABCs → partial implementation bases →
full implementations), organized around one idea: **iterated hom-enrichment**
— an $n$-morphism of `C` is a $0$-morphism of an iterated hom-category —
with suspension $\Sigma$ as its adjoint direction. (The corpus calls this
"the dimension shift"; the phrase is its own coinage and is used below only
in quotation.) `newcat2.md` (landed at this corpus
root) is the toy model's summary: equality of objects as the homotopy fibre
`Eq^0(A,B)`, the homotopy toolkit, and the requirements table for `Cat`,
`Fun`, `Hom_C`. `docs/background_theory.md` and
`docs/old_docs/original_specifications.md` are the fuller theory; `WARP.md`
holds the `Cat_n` level table and the chain
$\mathrm{Cat}_0 \to \mathrm{Cat}_1 \to \cdots$.

## Where the pieces went

| Piece | Disposition |
|---|---|
| KBMAG 2-polygraph encoding (`src/partial_implementation_bases/kbmag_implementation.py`) | migrated as research code to `computations/scripts/kbmag-two-polygraph/` with its design note; the copy here is part of the corpus record |
| `docs/sage_integration.md` roster (lines 1–55) | corrected and landed as `notes/category-design/lattice-categories-roster.md`; three false statements recorded there; the file's remainder is verbatim Sage source, third-party, not absorbed |
| Proof-carrying truth values (`src/_types.py`) | **ruling resolved**: the preamble keeps Sage's three-valued `Unknown` as its do-not-know channel; the genuinely extra content — witness, settling strategy, counterexample — is kept **as returned data**, not as a truth-value type. The model landing is `ModuleMorphism.equalizer` (`categories/modules/module_morphisms/module_morphisms.sage`): the equalizer subobject *is* the proof object for morphism equality, and a generator outside it is the counterexample. The four-valued type itself is not adopted (its probabilistic clause is a fuzzy t-norm, not probability — see errors) |
| Layered morphism equality (`src/partial_implementation_bases/hom/morphisms.py`) | collapses, for the preamble's framed module categories, to the equalizer (additive category: `Eq(f,g) = ker(f−g)`); the waterfall's other layers are either wrong (see errors) or engine regimes the preamble does not own; the presented-category regime is the KBMAG landing |
| Morphism coimage, sections, retractions (`hom` cluster of the sibling `FreeRModule` corpus, specified here) | landed on `ModuleMorphism` (`coimage`, `retraction`, `section`); the Moore–Penrose pseudoinverse was **not** landed — it is framing-dependent data, available as the presentation matrix's own `pseudoinverse()` |
| Cardinality (`src/utils/Cardinality.py`, `src/_sage_types.py`, `tests/test_cardinality.py`) | the three-class cardinal model is strictly weaker than the owned `categories/sets/cardinals.py` + `categories/functors/cardinality.sage`; nothing adopted. The **Sage-parent cardinality specimen table** (GF(7)=7, Subsets(3)=8, ZZ/QQ/QQbar countable, Zp/Qp uncountable, inheritance through polynomial/matrix constructions) remains here as a spec corpus, candidate rows against the owned cardinality functor; two of its rows are false (see errors) |
| Operation rosters (`docs/categories_to_implement.md`, `src/.../one_categories/*.py`) | parity-ledger inputs: per-category operation enumerations for Set, Groups, Rings, CommutativeRings, R-Mod against the owned categories; `ideals.py` is represented by `modules/fractional_ideals.sage` and `ring_as_module.sage` |
| `docs/variance_issues.md` | represented: in the preamble a functor is an element of `FunctorSpace(C,D)` (`categories/abstract_categories/functors.sage`), so domain and codomain are the parent's data and the variance-checking decorator scheme has no question left to answer |
| Test suites (`tests/`) | kept here as **spec corpora**: `test_cat_category.py` is a correct specimen table for Cat (see candidacy); `test_lattice.py` is represented by the owned lattice tree (two divergences: it takes A2 positive definite against this repo's negative-definite convention, and its constructor rejects indefinite Gram matrices that the corpus's own roster requires); `test_finite_set.py`, `test_terminal_category.py`, `test_empty_category.py`, `test_new_scaffolding_implementation.py` become specimen rows once their subjects are owned |

## Candidacy for `categories/abstract_categories/`

Recorded, per the migration directive — these are the notions the corpus
specifies that the preamble does not own; the corpus is their design source:

- **Iterated hom-enrichment** — the corpus's "dimension shift"
  (`new_w_categories/_arrow_abcs.py`, `arrow_implementations.py`,
  `old_interfaces/__arrows.py`): the bijection
  `Mor_C(x,y) = Ob(Hom_C(x,y))` as `morphism_to_object` /
  `object_to_morphism`, iterated hom-categories unique per pair, the
  correspondence table (n-morphisms of `Hom^k_C` ↔ (n+k)-morphisms of `C`,
  in `tests/abc_specs/new_w_categories/test_initial_category.py`), and the
  suspension `ΣC` as the adjoint direction.
- **Hom/End/Aut as category families** (`hom_categories/`,
  `cells/categories/wCat/hom_categories/`): `Hom_C` with objects the
  `Hom_C(x,y)`; `End_C(x)`; `Aut_C(x)`; the functor-category family `Fun`
  with `Nat` as its next level; `Aut_Cat(C)` correctly a groupoid.
- **The general natural transformation**
  (`cells/categories/wCat/n_morphisms/natural_transformation.py`): the
  component function and the theorem that a natural transformation is
  invertible exactly when all components are.
- **Yoneda embedding, presheaf category, category of elements,
  covariant/contravariant hom, slice/coslice** (`w_categories/cat_w.py`) —
  the slice categories exist in the preamble; the Yoneda tier does not.
- **The product of categories** (`limits/cat_w_product.py`): the product in
  Cat with componentwise structure and
  `Hom_{C×D} = Hom_C × Hom_D` — distinct from the owned category of
  product objects inside one category.
- **The free category on a directed graph and presented categories**
  (`w_categories/free_category_on_digraph.py`): the free–forgetful
  adjunction between Cat and directed graphs; the KBMAG landing is its
  decision-procedure companion.
- **A catalogue of named categories** (empty, terminal;
  `terminal_category.py` ×3, `empty_category.py`): with
  `tests/test_cat_category.py`'s specimen table (empty × C = empty,
  empty + C = C, Fun(∅,1) = 1, Fun(1,∅) = ∅, Fun(1,1) = 1, Fun(∅,∅) = 1)
  as the maintained rows once the objects are owned.
- **The lifting problem along a forgetful functor**
  (`docs/abc_hierarchy_analysis.md` Part VII): where `kernel()` lives under
  `U: Mod_R → Ab → Set`; the document's stated reason ("defined
  algebraically") is corrected by the audit to *the forgetful functor
  creates limits* — a design note candidate beside
  `categories/functors/free_forgetful_adjunction.sage`.

## Errors the audit recorded (kept verbatim in the files)

1. **Initial/empty category conflation** —
   `new_w_categories/initial_category.py`,
   `old_interfaces/empty_category.py`, `docs/new_plan.md`, and
   `tests/abc_specs/new_w_categories/test_initial_category.py` give the
   empty category one object (the empty set) with one morphism; that is
   the *terminal* category. The empty category has no objects and is
   initial via the unique empty functor. The corpus's own
   `tests/test_cat_category.py` table (`Fun(1, ∅) = ∅`) contradicts the
   implementation.
2. **Negative-level table** — `w_categories/cat_w.py` makes `Cat_{-2}`
   empty and `Cat_{-1}` the truth values; `WARP.md` places the point at
   −1; `tests/test_empty_category.py` puts the empty category at −2.
   Standard negative thinking: a (−2)-category is trivial (the level is
   terminal, not empty) and the (−1)-level is the two truth values.
   `docs/background_theory.md` has it right (`mca_{-2} = pt`).
3. **0-cells given boundaries** — `new_w_categories/_arrow_abcs.py` sets
   `s(X) = t(X) =` "the unique empty element of X"; in a globular set
   0-cells have no boundary, and the clause asserts every object is
   inhabited (false for ∅ and misuses the (−1)-level reading).
4. **`Cat_ω` as a limit** — `docs/background_theory.md` writes
   `Cat_ω := lim(Cat_0 → Cat_1 → …)`; the described object is the
   *colimit* (union) of the chain. `old_docs/original_specifications.md`
   makes the dual mistake (pushouts written as `lim`).
5. **Operator errors in `partial_implementation_bases/cat_w.py`** — the
   "additive dual" `Hom(X, 0)` is constantly zero, so the derived `X − Y`
   and `X / Y` denote nothing (and the boolean `additive=` flag is the
   bare-"dual" naming failure); `!=` is inverted (returns true on
   equality); `==` accepts any conclusive answer including disproofs;
   `>=` tests the same hom-set as `<=`.
6. **`_types.py` local errors** — a "point" required to be an
   endomorphism (restricting it to `1 → 1`); `Subobject` glossed as "some
   morphism X → Y exists" (a subobject is an isomorphism class of
   monomorphisms), with the same comment pasted onto `Superobject`
   unreversed; the probabilistic clause combines "probabilities" by
   min/max — a fuzzy t-norm, not probability.
7. **Equality waterfall errors**
   (`partial_implementation_bases/hom/morphisms.py`) — factorwise
   equality of decompositions is sufficient, not necessary; equality on
   generators decides only for structure-preserving maps; "probability
   1 − 1/n after n samples" is not a bound on anything (no measure, no
   independence, meaningless on infinite domains).
8. **`hom_cat_w_xy.py`** — endofunctors typed as 1-cells of `Fun(C,D)`
   (those are natural transformations; an endofunctor is a 0-cell of
   `Fun(C,C)`); "contravariant := domain is an opposite category" is not
   well defined (every category is an opposite); the same non-predicate
   appears as `is_op_category` in `two_category_mixins.py`.
9. **Empty-category completeness**
   (`tests/abc_specs/new_w_categories/test_initial_category.py`) —
   asserts the empty category complete; completeness includes the empty
   diagram, whose limit is a terminal object, which ∅ lacks. The older
   `tests/test_empty_category.py` says "not complete", correctly.
10. **Cardinality table rows** (`tests/test_cardinality.py`,
    `src/utils/Cardinality.py`) — the row for `AA` and the identity for
    the continuum raised to itself are false; the three-class cardinal
    model is superseded by the owned cardinals.
11. **KBMAG file defects** — recorded beside the migrated copy in
    `computations/scripts/kbmag-two-polygraph/README.md` (isomorphism
    search restricted to generating morphisms; composition-order
    convention conflict; an uncalled-method comparison bug; completion
    non-termination unstated).
12. **Kernel and cokernel by fibre over a terminal object**
    (`w_categories/hom_categories/abstract_arrows.py`, repeated at
    `partial_implementation_bases/cat_w.py` `kernel_C`) — writes
    $\ker(f) = \{x \in X : f(x) = *\}$ for "the terminal object of $Y$",
    and $\operatorname{coker}(f) = Y/\operatorname{im}(f) = * +_X Y$. A
    kernel is defined only in a pointed category, as the pullback of $f$
    along $0 \to Y$; the fibre over a terminal object is a preimage, and
    in $\mathbf{Set}$ the fibre over a point is nonempty for every point
    of the image. "The terminal object of $Y$" is also a category error —
    $Y$ is an object, not a category. The cokernel formula holds in an
    abelian category, not generally.
13. **Forgetting structure realised as inheritance**
    (`w_categories/one_categories/rings.py`, same pattern in `mod_R.py`
    and `groups.py`) — a ring object is declared a subtype of a group
    object and of a set object, with `as_set` and `as_additive_group`
    returning `self`. A forgetful functor is a functor, not a subtype
    relation. The consequence is concrete: the ring inherits `centre`,
    `commutator_subgroup`, `is_abelian`, `order` and `quotient_by` from
    the group layer, so `R.center()` denotes the centre of $(R,+)$, which
    is all of $R$, rather than the centre of the ring. The corpus's own
    `docs/abc_hierarchy_analysis.md` Part VII states the correct model
    ("WRONG (inheritance-based) … CORRECT (functor-based)") and its
    summary then reinstates inheritance.
14. **Mediating-morphism condition on the wrong legs**
    (`abc_specs/structures.py`) — the pullback clause requires
    $f \cdot \pi_1 = g \cdot \pi_2$ for $f: B \to X_1$, $g: B \to X_2$,
    using the pullback projections; the condition is on the cospan legs
    $p_1: X_1 \to Z$, $p_2: X_2 \to Z$, namely $p_1 \cdot f = p_2 \cdot
    g$, and as written the composites are not even composable. The
    pushout clause carries the dual mistake, writing $\iota_1 \cdot f =
    \iota_2 \cdot g$ with the pushout injections instead of
    $f \cdot i_1 = g \cdot i_2$ with the span legs.

## Vocabulary rule

The corpus's coinages — "ruly"/"unruly" categories, the "amb()" ambient
accessor, bare "dual" with a boolean flag — are session-local inventions
and do not survive relocation into owned code: the preamble's names state
their structure (`dual_module`, `dual_lattice`, ...), per the banned-language
index in `AGENTS.md`.
