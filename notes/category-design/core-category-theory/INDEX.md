# Core category theory — design corpus

The abstract categorical layer the bilinear-module tower was designed to sit
on: abelian and concrete categories, diagram and cone machinery, limits
and colimits, internal algebraic objects, and symmetric monoidal structure.
Landed 2026-08-20 from `~/gitclones/Coxeter/implementation/planning/` and
`~/gitclones/Coxeter/tmp_restore/docs/api-planning/`.

Read against `src/dzack_research/preamble/categories/abstract_categories/`
(`cat.sage`, `products.sage`, `arrow_categories.sage`,
`slice_categories.sage`, `functors.sage`, `direct_sum_objects.sage`) and
`categories/functors/`.

---

## 1. Documents

| Document | Mathematical content |
|---|---|
| `core/abelian_categories.md` | The abelian axioms: a zero object (initial and terminal at once), the biproduct as $+$, kernel and cokernel with the image factorization, the snake and five lemmas, exactness stated on complexes. |
| `core/CATEGORY_INHERITANCE_GUIDE.md` | Which methods of an abelian category are *abstract* (kernel, cokernel), which are *derived* from them (mono, epi, iso, image, coimage, the canonical factorization), and which are concrete. The distinction is the corpus's organising principle: a subcategory declares what it must be given and inherits what follows. |
| `core/concrete_categories.md` | A concrete category as a faithful functor $U$ to $\mathbf{Set}$; the Mac Lane characterisations of mono, epi and iso; fibre and cofibre as pullback and pushout; limits and colimits unified; the endomorphism and automorphism structure; the diagram and cone classes. |
| `core/objects_homsets_interface.md` | Hom-sets as Sage parents whose elements are morphisms; an `objects()` collection on a category; a composition cache; tests for a full subcategory. |
| `core/objects_in_categories.md` | Internal algebraic objects in a monoidal category: monoid, group, ring, Lie and Hopf objects. A ring is a monoid object in $\mathbf{Ab}$; an $R$-algebra is a monoid object in $R\text{-Mod}$. |
| `core/symmetric_monoidal_categories.md` | The monoidal, braided, symmetric, rigid and closed axioms: the associator, the unitors, the braiding, duals with evaluation and coevaluation, the internal hom, the coherence conditions. |
| `core/symmetric_monoidal_category.md`, `categories/symmetric_monoidal_category.md` | Interface stubs for the symmetric monoidal structure on modules: tensor unit, associator, unitors, braiding, the pentagon/triangle/hexagon checks, the monoidal dual object $[A, I]$. The second copy names its intended instances: $\mathrm{Bil}_R\text{-Mod}$, its stable category, chain complexes. |
| `diagrams/diagram_infrastructure.md` | A diagram as a functor $J \to C$; cone and cocone objects with coherence validation; dispatch of the limit or colimit by the shape of $J$; the specialised Product, Equalizer and Pullback diagrams. |
| `diagrams/diagram_categories_summary.md` | The shape toolkit: which index category (thin, from a poset; or free, from a digraph) produces which universal construction. |
| `diagrams/poset_categories.md` | The poset-to-thin-category construction, and the chain, discrete, span and cospan shapes; poset diagrams for products, filtrations and pullbacks. |
| `diagrams/digraph_categories.md` | The free category on a directed graph: paths as morphisms; the parallel-pair, walking-arrow and commutative-square shapes; quotient categories by relations on paths. |
| `limits/unified_limits_colimits.md` | Universal properties with an explicit witness object; the hom-equivalence $\mathrm{Hom}(X, \lim D) \cong \mathrm{Cones}(X, D)$; limits and colimits as Kan extensions along $J \to \mathbf{1}$. |
| `limits/universal_constructions_via_limits.md` | Every universal construction as a limit or colimit — a kernel is an equalizer against $0$, a fibre is a pullback along a point — with a layered architecture that gives a default from the general construction and specialises where a better algorithm exists. |
| `examples/morphism_inverse_operator.md` | The operator $f^{(-1)}$: the inverse morphism when $f$ is invertible, and otherwise a partial section — a preimage operator whose fibre over $y$ is $x_0 + \ker f$. Includes the deprecation path for `lift()`. |
| `examples/working_f_inverse_example.py` | The working prototype of that operator, implemented by overriding `__pow__` on a vector-space morphism. Prototype code, not maintained preamble code. |
| `examples/category_decorators.md` | Decorator machinery marking a category method as abstract, derived, or concrete, with dependency tracking and generated documentation. An engineering sketch rather than mathematics. |
| `PHASE1_COMPLETION_SUMMARY.md` | The design decisions this corpus reached: the axiom hierarchy with $\mathrm{WithBasis} \subseteq \mathrm{Free}$, the split of the Grothendieck-ring operations across `+`, `*`, `@`, `/`, and one file per mathematical level. |

---

## 2. Divergences between the design and the built preamble

Recorded findings, not repairs to make.

### 2.1 A diagram is a category in the preamble, not a validated object

The design (`diagrams/diagram_infrastructure.md`) makes the diagram a
first-class object — a functor $J \to C$ — and gives cones a `validate()`
step that re-checks coherence at runtime.

The preamble makes the *shape* a category. `products.sage` defines
`DiagramCategory` (`:66`) with `DirectedSystem` (`:114`) and `InverseSystem`
(`:159`) beneath it, then `ConeCategory` (`:204`) and `CoconeCategory`
(`:235`), then `ProductCategory` (`:265`), `CoproductCategory` (`:303`) and
`BiproductCategory` (`:341`). A cone is an *object of a cone category*, and
its structure morphisms are read off its placement (`structure_morphisms`,
`factors`) rather than re-verified. This follows the repository's standing
rule that a computer algebra system is not a proof assistant: coherence is a
theorem about the construction, not a runtime check.

The design's runtime pentagon, triangle and hexagon verification
(`core/symmetric_monoidal_category.md`) is the same pattern and is likewise
not taken.

### 2.2 The abelian structure is absent

No abelian node exists in the preamble. There is no `kernel`/`cokernel`
contract at the abstract level, no image factorization, and no exactness
predicate on complexes; the kernel and cokernel constructions that exist are
module-specific. The design's derivation scheme in
`core/CATEGORY_INHERITANCE_GUIDE.md` — declare kernel and cokernel abstract,
derive everything else — remains the statement of what an abelian node would
have to provide.

### 2.3 Limits are not general; three shapes are built

The preamble owns products, coproducts and biproducts as categories, the
arrow category (`arrow_categories.sage:54`) and slice categories
(`slice_categories.sage`), and the free/forgetful adjunction
(`functors/free_forgetful_adjunction.sage`). It does **not** own a general
limit over an arbitrary index category, Kan extensions, comma categories, or
the witness objects the design attaches to a universal property. Slice
categories are a special case of the comma category the design asks for.

### 2.4 Internal algebraic objects are absent

`core/objects_in_categories.md` designs monoid, group, ring, Lie and Hopf
objects internal to a monoidal category, with rings recovered as monoid
objects in $\mathbf{Ab}$. The preamble has rings, groups and algebras as
their own categories, not as internal objects of a monoidal category, and no
mechanism producing one from the other.

### 2.5 The Grothendieck-ring operator scheme

`PHASE1_COMPLETION_SUMMARY.md` and the `RMod` documents in the sibling corpus
split $K_0$ operations across `+`, `*`, `@` and `/`. The preamble sites the
two it uses on integral lattices themselves rather than on a $K_0$ surface:
`+` is the orthogonal direct sum, `**` the $n$-fold sum, and `@` the tensor
product (`integral_lattices.sage:1386`). There is no quotient operator and no
$K_0$ object.

### 2.6 `WithBasis` versus a framing

`PHASE1_COMPLETION_SUMMARY.md` records $\mathrm{WithBasis} \subseteq
\mathrm{Free}$ as the settled axiom hierarchy. The preamble replaced this
with the framing doctrine — see §2.2 of `../bilinear-module-tower/INDEX.md`.

---

## 3. Errors recorded in these documents

The audit recorded no mathematical error in this corpus. Its foundational
claims are standard; what it lacks is a decision about which of them the
preamble should own.
