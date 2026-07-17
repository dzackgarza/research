# Extending the proof of concept

This file gives the concrete recipe for adding a new mathematical layer.

## 0. Locate the Mathlib expression first

Before defining anything, find how Mathlib already expresses the concept, and anchor to it exactly or by a thin thread.
This is not a style preference; it is what makes placement automatic: **in Lean the home of a notion is read off its signature, not chosen.**  A synthetic definition ("cardinality as a field we attach wherever we like") is attachable to anything and therefore coheres with nothing; the real anchor (`Cardinal.mk : Type → Cardinal`) puts the notion in a coherent place with its whole lemma library for free.

Precedents in this tree:

- `SetObj.cardinality` **is** `Cardinal.mk`, one line; the enumeration presentation only *evaluates* it (`cardinality_eval`).

- `ModuleHom.index` **is** `AddSubgroup.index`'s invariant applied to `range f`, and its ℕ shadow equals Mathlib's convention by `rfl` (`index_toNat`).

- `CountableSetObj` / `FiniteSetObj` are field-for-field Mathlib's `Encodable` / `FinEnum`; the identity is stated at the definitions and consolidation onto the classes is queued (#217).

If the anchoring is exact, cite the Mathlib name in the docstring.
If it is a thin thread (a wrapper, a convention change, a generalization), prove the connection — ideally a `rfl` lemma — and add a ledger marker (below).
Only when Mathlib genuinely lacks the concept does new theory get written, and then it goes in `ForMathlib/` with its upstream target named (see the layer contract in `CatDSL/ForMathlib/`).

## The alignment surface: tethers (checked), not markers (self-reported)

What must be visible at a glance is what we DON'T know: (A) which notions are untethered to any Lean definition, and (B) which are tethered but diverge in convention.
Neither is answerable by docstring grep — prose is self-reporting.
The mechanism is `CatDSL/Manifest/Tether.lean`:

- `tether Local ~ Anchor via Witness` elaborates only if the witness's *type* mentions both constants — a connection theorem (`rfl` for definitional wrappers, `index_toNat`-style for convention bridges) or a construction (`CountableSetObj.encodable : Encodable X.set`).

- The kind is **computed**, never declared: `exact` (equation headed by the two constants — same convention), `divergent` (a wrapped side — the wrap IS the convention gap, machine-visible), `structural` (a bundling construction).

- **(A) is the computed complement**: `untetheredIn` walks the environment and subtracts the tethered; `Example/TetherTest.lean` pins the result, so a new unanchored notion reds until tethered or consciously acknowledged.
  Shrinking that pinned list is catalogue work; silent growth is the drift this exists to catch.

- **(B) is the divergent/structural tether list** — `just tether-report`.

Prose remains only for what cannot be computed:

- `Upstream target: <Mathlib module>` — on every `ForMathlib/` declaration (the directory is by construction the upstream-contribution queue; `just upstream-candidates`).

- `Convention divergence:` — the human *adjudication* for each divergent tether: which side should change, upstream (Mathlib too narrow or subtly wrong) or local (our definition was myopic, under-general, or missing hypotheses).
  `just conventions` lists them; a divergent tether without an adjudication marker is a defect.

## A. Add a category family

Suppose objects are `StructuredObj R`.

```lean
structure StructuredObj (R : FiniteRingObj) where
  module : FreeFinModuleObj R
  extra : ExtraData module
```

Name each field for the entity it holds (here: a module), never for a relationship to another category.
Relationships are realization functors, and those are separate declarations — see step B.

Define morphisms and install the `Category` instance:

```lean
structure StructuredHom {R} (X Y : StructuredObj R) where
  hom : X.module.module.set →ₗ[R.set]
        Y.module.module.set
  law : PreservesExtra X.extra Y.extra hom

instance (R : FiniteRingObj) : Category (StructuredObj R) where
  Hom := StructuredHom
  id := ...
  comp := ...
  -- id_comp / comp_id / assoc are autoParams; `aesop_cat` usually closes them

abbrev Structured (R : FiniteRingObj) : LargeCat := Cat.of (StructuredObj R)
```

The `Category` instance lives on the object *type*; `Cat.of` bundles it into a first-class object of `Cat`. Keep the bundle an `abbrev`: it is only a name for a category that already exists on the type.

## B. Add the preferred realization functor

```lean
def Structured.toFree (R : FiniteRingObj) :
    StructuredObj R ⥤ FreeFinModuleObj R where
  obj := StructuredObj.module
  map := StructuredHom.hom
```

Declare it between the object **types**, not the bundles: `Structured R ⥤ FreeFinModules R` would resolve `Cat.str` instead of the `Category` instance and leave `⇑f` without its coercion.

Register the entire dependent family once:

```text
prefer Structured.toFree.
```

No edge for `R = 𝔽₂` is declared separately.
The resolver infers it by unifying the source of the family with the current category.

## C. Add a concrete obligation

Do not attach a Boolean or proposition to objects when an implementation is required.
Make the implementation data into a structured category.

For example:

```lean
structure SearchableSetObj where
  set : Type
  search : (set → Bool) → Option set
  search_spec : ...
```

Define the projection:

```lean
def SearchableSet.forget : Functor SearchableSets Sets := ...
```

To state that objects of `Structured R` inherit this implementation, construct a lift:

```lean
def Structured.toSearchable (R : FiniteRingObj) :
    Functor (Structured R) SearchableSets := ...
```

and register it:

```text
prefer Structured.toSearchable.
```

The ordinary Set-realization path and the implementation path should be related by a natural isomorphism when they are not definitionally equal.

## D. Add an inherited operation

An operation whose implementation lives on a target category follows the pattern in `elabCardinality`:

1. recover the object's home category from its declaration type;

2. request a path to the operation's implementation category;

3. apply every functor in that path;

4. invoke the target operation;

5. ask Lean to unify the generated result with the expected type.

For example, an operation implemented on `SearchableSets` should resolve to `SearchableSets`, not merely to `Sets`.

## E. Add theorem-backed capabilities

View reachability must not be used for properties such as preservation or creation of limits.
Add a second persistent attribute:

```lean
initialize capabilityRuleAttr : TagAttribute ←
  registerTagAttribute `CatDSL.capabilityRule "..."
```

A rule is an ordinary Lean theorem.
For example:

```lean
theorem hasProducts_of_creates
    (F : Functor C D)
    (h₁ : CreatesProducts F)
    (h₂ : HasProducts D) :
    HasProducts C := ...
```

A capability resolver should instantiate theorem families by the same metavariable technique used for preferred functor families, recursively solve their proposition-valued premises, and return the resulting Lean proof term.
The Lean kernel then checks the proof.

Do not merge capability search with preferred-view path search.

## F. Add a surface term former

For notation whose interpretation depends on an expected category:

```lean
scoped[CatDSL] syntax (name := mySyntax) ... : term

@[term_elab mySyntax]
def elabMySyntax : TermElab := fun stx expected? => do
  ...
```

The `R²` and `(M,id)` elaborators in `CatDSL/Syntax.lean` are complete examples.
They inspect the expected object type, recover the parameter `R`, elaborate their subterms against precise dependent types, and emit ordinary Lean applications.

## G. Test the extension

Every category layer should have a vertical-slice test containing:

```text
let X := ... ∈ Structured(𝔽₂).
#home X.
#via X ∈ FiniteSets.
#via X ∈ CountableSets.
#via X ∈ Sets.

example : |X| = expected := by
  rfl
```

Also test one invalid route and one parameter mismatch.
These should be compile-fail fixtures checked by a shell test harness.
