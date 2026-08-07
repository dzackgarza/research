# Mathematical Coding Conventions

These rules govern mathematical code under `computations/`. Every example is a
normative code shape, not a statement about which classes or files currently exist.

## Reset Rule

Before implementing an operation, identify its mathematical input, parent/category,
owner (`ParentMethods`, `ElementMethods`, or `MorphismMethods`), output, and defining
maps.

If two consecutive corrections remove helpers, wrappers, caches, fallbacks, alternate
inputs, or stored fields from one operation, discard that implementation. Reconstruct
it from the corrected mathematical signature. Do not preserve the rejected design
under a new name.

## Exact Parents And Category Contracts

- **No attribute probing for category-guaranteed structure.**

  Forbidden:
  ```sage
  L = getattr(getattr(self, "_W", None), "some_lattice", lambda: None)()
  if L is not None and hasattr(L, "gram_matrix"):
      G = L.gram_matrix()
  ```

  Required:
  ```sage
  L = self.source_lattice()
  G = L.gram_matrix()
  ```

- **Use membership, not defensive parent recovery.**

  Forbidden: `assert getattr(x, "parent", lambda: None)() is self`

  Required: `assert x in self`

- **Do not check states excluded by membership.**

  After `x in L` for an integral lattice, do not check that `x` has integer
  coordinates. Rational-coordinate elements belong to a different parent.

- **Do not widen element APIs to coordinate data.**

  If the input is `e in L`, reject raw vectors, tuples, and lists. Convert coordinate
  data to an element at an explicit constructor boundary.

- **Required imports fail loudly.**

  Forbidden: `try`/`except ImportError` around Sage or a required mathematical package.

  Required: import it directly and let failure abort initialization.

- **No certificate layer.**

  Refine into a subcategory only by construction, an applicable cited theorem, or an
  actual computation. Otherwise retain the strongest justified supercategory. Never
  add certificate objects, proof wrappers, prose declarations, or `verify_*()` methods
  to claim membership.

## Method Ownership

- **Put operations on the object that owns them.**

  Parent operations go in `ParentMethods`, predicates on elements go in
  `ElementMethods`, and operations on arrows go in `MorphismMethods`.

- **No freestanding helper for a category operation.**

  Forbidden:
  ```sage
  def _source_lattice(A):
      return A._source

  class ParentMethods:
      def source_lattice(self):
          return _source_lattice(self)
  ```

  Required:
  ```sage
  class ParentMethods:
      def source_lattice(self):
          return self._source
  ```

- **No public wrapper around a private twin.**

  Forbidden: `source_lattice()` whose entire body is `return self._source_lattice()`.

  Required: the public method implements the operation directly.

- **No one-use helper indirection.**

  Forbidden: `as_finitely_presented_group()` delegating to a module-level
  `_as_finitely_presented_group(self)`.

  Required: put the implementation in `as_finitely_presented_group()`.

- **Predicates belong on the object they classify.**

  Forbidden: `L.is_primitive(x)`.

  Required: `x.is_primitive()` from the lattice category's `ElementMethods`.

- **Shared methods belong in a common supercategory.**

  Do not duplicate `abelian_group()`, `is_p_elementary()`, `_latex_()`,
  `as_finitely_presented_group()`, or common form-matrix handling in sibling
  categories.

## Categories, Concrete Parents, And Dispatch

- **A category is not its concrete realization.**

  Missing concrete objects do not justify replacing `BilinearModules(Category)` with a
  class named `BilinearForm`. Keep the category and add a concrete parent whose objects
  are refined into it.

- **Do not bypass category dispatch.**

  Forbidden:
  ```sage
  _native_gram_matrix = ...
  _native_normal_form = ...
  _native_associated_form = ...
  ```

  Also forbidden: per-object lambdas and native-class patches used to evade Sage's
  category dispatch.

- **Use Sage's native category construction and refinement.**

  An owned parent declares its category through `Parent.__init__(category=...)`.
  An existing object is refined with Sage's native category refinement only when its
  construction, an applicable theorem, or an actual computation justifies the new
  category.

  Forbidden:
  ```sage
  refine(obj, category)  # custom wrapper that rewrites classes
  obj.__class__ = dynamic_class(...)
  parent.element_class = dynamic_class(...)
  SageClass.__init__ = patched_init
  ```

  Do not reverse method-resolution order, rewrite element or morphism classes, patch
  every future instance of a Sage class, or maintain a private whitelist of categories
  whose methods are manually injected. If a Sage concrete parent cannot support the
  required mathematical surface through native categories, construct an owned parent
  that does.

  Required refinement shape:
  ```sage
  obj._refine_category_(category)
  ```

- **Put a generic method in the weakest category whose hypotheses imply it.**

  A method valid for every object belongs in the base category. A method requiring
  finiteness, commutativity, reducedness, integrality, smoothness, or another axiom
  belongs in the corresponding axiom subcategory. Do not put it in the base category
  and recover the missing hypothesis with a runtime branch.

- **Let refinement change the available mathematical surface.**

  A concrete parent begins in the strongest category justified by its construction.
  An applicable theorem or an actual computation may refine it further. Methods from
  the refined category then become available through Sage's category machinery; do
  not copy those methods onto the concrete class or install them on one instance.

- **Category membership is not a claim that every conceivable algorithm exists.**

  A category supplies the `ParentMethods`, `ElementMethods`, and `MorphismMethods`
  actually defined on it and its supercategories. From `G.category()` one may infer
  the recorded mathematical classification, not that methods such as `order()` or
  `center()` exist, nor which class or category supplied an observed method.

- **Categories complement concrete implementation classes; they do not abolish
  inheritance.**

  Concrete parents and elements still have implementation classes. The
  mathematician-facing API must be routed by categories, so using it does not require
  knowledge of that class hierarchy. Do not describe Sage's dynamic category mixins
  as an inheritance-free mechanism.

- **Split categories by mathematical ownership.**

  Distinct categories with distinct parent or method surfaces live in distinct files.
  Common behavior lives in a common category file. Delete the former combined loader;
  do not keep a compatibility loader.

- **Call native constructors without replacing them.**

  Forbidden:
  ```sage
  Original = globals()["IntegralLattice"]
  globals()["IntegralLattice"] = enriched_constructor
  ```

  Required shape:
  ```sage
  from sage.modules.free_quadratic_module_integer_symmetric import (
      IntegralLattice as SageIntegralLattice,
  )
  ```

  An owned constructor always calls `SageIntegralLattice`; it never discovers or
  replaces the native constructor through mutable global state.

## Public Mathematical API

- **Use the standard operation name; let the category distinguish meaning.**

  Forbidden:
  ```sage
  q.gram_matrix_quadratic()
  b.gram_matrix_bilinear()
  ```

  Required:
  ```sage
  q.gram_matrix()
  b.gram_matrix()
  q.associated_bilinear_form().gram_matrix()
  ```

- **Use `as_*` for conversions.**

  Forbidden: `A.finitely_presented_group()`

  Required: `A.as_finitely_presented_group()`

- **One operation gets one public spelling.**

  Delete public aliases such as `run_algorithm()` when they only call
  `algorithm()`.

- **A constructor-returning method exposes no post-init controls.**

  Forbidden:
  ```sage
  def normal_form(self, connected_components=True):
      result = ...
      subdivide_form_gram_matrix(result, connected_components)
      return result
  ```

  Required:
  ```sage
  def normal_form(self):
      result = ...  # construct the new form
      return result
  ```

- **Name accessors for their exact output.**

  Forbidden: `subobject.lattice()` and `subobject.codomain_generators()`.

  Required: `subobject.embedding_codomain()` and
  `subobject.embedded_gens()`. The subobject's own generators remain `gens()`.

## Coordinates, Elements, And Morphisms

- **A coordinate row is not an element.**

  Forbidden: `L.glue((1/2, 1/2, 0, 0))`

  Required shape:
  ```sage
  x_dual = L.dual_lattice_element((1/2, 1/2, 0, 0))
  a = L.discriminant_projection()(x_dual)
  L.glue(a)
  ```

- **Store defining maps as actual morphisms.**

  Required:
  ```sage
  L.dual_embedding()          # L -> L^*
  L.discriminant_projection() # L^* -> A_L
  ```

  Do not scatter equivalent coordinate formulas through callers.

- **A basis of a derived parent consists of elements of that parent.**

  Forbidden:
  ```sage
  def dual_basis(self):
      return self.gram_matrix().inverse().columns()
  ```

  Required shape:
  ```sage
  def dual_basis(self):
      return tuple(self.dual_lattice().basis())
  ```

  Columns of \(G^{-1}\) may be used inside the construction of the dual parent. They
  are not the public dual basis.

- **Use projection and lifting in their correct directions.**

  Applying `L^* -> A_L` is projection. "Lift" means choosing a representative of an
  element of `A_L` back in `L^*`.

- **Compute divided classes through the maps.**

  Required:
  ```sage
  v_dual = L.dual_embedding()(v)
  v_bar = L.discriminant_projection()(v_dual / L.div(v))
  ```

- **Organize classifiers by their defining invariant.**

  Required:
  ```sage
  d = L.div(e)
  assert d in Set({1, 2})
  if d == 1:
      ...
  if d == 2:
      ...
  assert_never(d)
  ```

  Do not replace an intrinsic predicate with quotient construction, model recognition,
  or a check that an isometry routine happens to exist.

- **A matrix represents a morphism relative to chosen bases; it is not the morphism.**

  Do not normalize morphisms, matrices, lists of images, and arbitrary objects with a
  `.matrix()` method into one untyped input. The ordinary constructor accepts
  generator images in the stated domain and codomain. If matrix construction is
  needed, expose one explicit matrix constructor at the homset boundary.

  Forbidden:
  ```sage
  if hasattr(x, "to_matrix"):
      x = matrix(ZZ, x.to_matrix())
  elif hasattr(x, "matrix"):
      x = matrix(ZZ, x.matrix())
  ```

- **Compose and compare morphisms as morphisms.**

  Do not multiply representing matrices and feed the product back through a
  constructor. Use the homset's composition and identity operations. Extract a matrix
  only for a backend that explicitly requires one.

## Computational Representation Boundaries

Coordinates, matrices, floating-point fields, and backend-specific objects are valid
computational representations. They are not the common language between mathematical
operations.

- **Lower once and reconstruct once.**

  A backend adapter performs both directions:

  ```text
  structured input
      -> explicit representation in a chosen basis and scalar field
      -> backend computation
      -> elements, morphisms, subobjects, or quotients in the correct parent
  ```

  Raw backend rows, matrices, indices, or floating-point vectors do not cross that
  boundary.

- **The public operation keeps the mathematical signature.**

  A root enumeration on \(L\) accepts an element of \(L\) as its starting vector and
  returns elements of \(L\). A fixed-lattice operation accepts an action by
  endomorphisms of \(L\) and returns a subobject of \(L\). It does not accept "a
  morphism or matrix or iterable of either" and return coordinate bases.

- **Base change is an explicit mathematical construction.**

  If a backend requires a real or complex field, first construct the base-changed
  parent and the induced map:

  ```sage
  L_R, ι = L.base_extend_with_map(RealField(precision))
  ```

  The backend operates on a representation of `L_R`, and its reconstructed outputs
  belong to `L_R`. Return an element of `L` only after an exact recognition or a named
  map back to `L`; numerical closeness is not such a map.

- **Precision belongs at the numerical boundary.**

  Numerical fields are chosen once with explicit precision. Do not coerce individual
  coefficients opportunistically inside unrelated category methods.

- **Reuse the strongest existing operation before lowering.**

  Search the owning Sage parent and the local category tree for `kernel`, `image`,
  `intersection`, `orthogonal_complement`, `quotient`, `inverse_image`, `base_extend`,
  and the relevant Hom operation. If a needed operation is missing, add it once to the
  weakest category whose hypotheses define it. Do not reproduce it privately with
  matrix arithmetic at every caller.

- **Owned low-level computation becomes named mathematical vocabulary.**

  If no Sage or backend operation exists and this repository must own a calculation,
  place it once on the object that mathematically owns it. Repeated expressions such
  as \(v^{\mathsf T}Gw\), intersections of coordinate kernels, denominator clearing,
  or reconstruction from Hermite form are evidence that an operation or functor is
  missing.

## Functorial Derived Structure

- **A derived object retains the maps that define it.**

  A subobject retains its monomorphism, a quotient retains its projection, a base
  change retains its induced map, and a normal form retains the comparison isometry or
  change of basis when that map is part of the result's meaning.

- **Associated structure is not a detached reconstruction.**

  Forbidden shape:
  ```sage
  B = BilinearForm(q.invariants(), q.source(), q.bilinear_gram_matrix())
  ```

  Required shape:
  ```sage
  B = q.associated_bilinear_form()
  B.underlying_module() is q.underlying_module()
  ```

  The associated form reuses the underlying module and its elements. It is not a
  plain wrapper around copied invariants and a matrix.

- **Do not encode an associated-object functor as a false subcategory.**

  If `q.gram_matrix()` and `b.gram_matrix()` have different meanings or codomains, do
  not make quadratic-form objects inherit a bilinear-form API merely to obtain common
  methods. Put common behavior in a genuine common supercategory and expose
  `associated_bilinear_form()` as the structure-changing operation.

- **Conversions retain comparison data.**

  Constructing an abstract group from a torsion module, a finite presentation from an
  abelian group, or a normal form from a form must reuse a native realization when
  possible. When the result is genuinely a distinct object, make the canonical
  comparison map accessible rather than returning an unrelated object reconstructed
  from invariant factors or relations.

- **Zero cases remain objects of the same category.**

  A zero lattice, zero subobject, or zero quotient is not `None` and not a \(0\times0\)
  matrix returned in place of the usual parent.

- **Presentation metadata is ephemeral.**

  Forbidden:
  ```sage
  module.gram_matrix = lambda: subdivided_matrix
  module._gram_matrix = subdivided_matrix
  ```

  Matrix cuts, preferred display blocks, colors, and layout positions do not alter the
  mathematical operation. If cuts arise from a direct-sum decomposition, retain the
  summand subobjects and derive a subdivided copy only while rendering.

- **Do not branch on cases the mathematical object already handles.**

  A `gram_matrix()` implementation does not need a zero-object branch unless its
  mathematical definition genuinely differs there.

## Subobjects And Direct Sums

- **A subobject requires a monomorphism.**

  An unconstrained field named `embedding: Any` does not define a subobject.

- **Return a subobject, not an induced Gram matrix.**

  Forbidden shape:
  ```sage
  basis = intersection_of_coordinate_kernels(action_matrices)
  return IntegralLattice(induced_gram_matrix(basis))
  ```

  Required mathematical shape:
  ```sage
  fixed = action.fixed_subobject()                 # (L^G, i: L^G -> L)
  coinvariant = fixed.orthogonal_complement()      # (L_G, j: L_G -> L)
  ```

  The inclusion maps are part of both results. Do not reconstruct them later from
  basis rows.

- **Construct fixed objects from morphism kernels.**

  For an action \(G\to\operatorname{Aut}(L)\),
  \[
  L^G=\bigcap_{g\in S}\ker(g-\operatorname{id}_L)
  \]
  for a generating set \(S\). Compute this with endomorphisms, their identity, kernel
  subobjects, and subobject intersection. Coordinate kernels belong only inside a
  generic kernel implementation.

- **A quotient retains its source, subobject, and projection.**

  The result of \(I^\perp/I\) is not merely a lattice with the induced Gram matrix.
  Construct \(I\hookrightarrow I^\perp\), the quotient parent, and
  \(I^\perp\twoheadrightarrow I^\perp/I\). Keep the induced form on the quotient and
  make the defining maps accessible.

- **Gluing is inverse image under the discriminant projection.**

  For \(H\subseteq A_L\) and \(\pi:L^\vee\to A_L\), the glued overlattice is
  \(\pi^{-1}(H)\). Required shape:

  ```sage
  A = L.discriminant_group()
  H = A.submodule(generators)
  L_H = L.discriminant_projection().inverse_image(H)
  ```

  Do not lift the generators to rational rows, clear denominators, run Hermite form,
  and build an unrelated lattice inside `glue()`. If inverse image requires that
  calculation, implement it once on the relevant morphism or subobject category and
  return the resulting subobject with its inclusion.

- **A direct summand requires a splitting.**

  Required data:
  ```text
  f: A -> B
  r: B -> A
  r * f = id_A
  ```

  Without a retraction, complement, or equivalent splitting data, call it a subobject
  or embedded sublattice.

- **Direct-sum structure is installed by construction.**

  A direct-sum object records an ordered collection of subobjects and receives
  direct-sum-specific element and homomorphism methods only when constructed as a
  direct sum.

- **Do not confuse submodule sum with morphism addition.**

  Componentwise addition of embedded generator images describes addition of maps with
  a common domain. It is not the sum of two submodules.

## Semantic Objects And Catalogues

- **Expose constructed objects, not public construction tables.**

  Forbidden:
  ```sage
  PUBLIC_DATA = {...}

  def get_object(name):
      return build_object(PUBLIC_DATA[name])
  ```

  Required shape:
  ```sage
  _construction_data = {...}
  Example_1 = build_object(_construction_data["Example_1"])
  Example_2 = build_object(_construction_data["Example_2"])
  ```

- **Consume raw data once.**

  Coordinates, layouts, labels, and lookup rows are private inputs used to construct
  the public mathematical objects. Do not expose both surfaces.

- **Do not populate catalogues by late mutation.**

  Construct a named catalogue object where it is declared.

- **Private catalogue constructors belong to the catalogue owner.**

  Forbidden:
  ```sage
  def _rank_one_negative(n):
      ...

  class Lattices:
      A = _rank_one_negative(2)
  ```

  Required:
  ```sage
  class Lattices:
      @staticmethod
      def _rank_one_negative(n):
          ...

      A = _rank_one_negative(2)
  ```

- **Do not store a redundant parent field.**

  If every retained element must share a parent, obtain that parent from the elements.

- **Retain the generated object and its embedding.**

  When elements generate a subobject, the mathematical data are the abstract object
  determined by their induced relations and the embedding sending its distinguished
  generators to those elements. A matrix plus loose coordinate rows is not an
  equivalent public API.

- **Display conventions belong to the displayed object.**

  Labels, colors, preferred positions, and edge conventions belong in that object's
  methods and documentation, not in unrelated fixtures.

- **Fixtures are not prose storage.**

  Minimal mathematical examples belong on the category they exemplify. Do not mix
  examples, expected values, unfinished-object inventories, and prose in a fixture
  file.

## Idiomatic Sage: Mathematical Syntax

Sage code should expose the parent, object, map, and mathematical operation being
studied. This is not a ban on algorithms: an explicit enumeration, recurrence, or
reduction is appropriate when that procedure is itself the mathematics.

### Declare The Parent Before Its Elements

In a Sage notebook or `.sage` file, introduce the mathematical universe and its
distinguished generators together:

```sage
R.<x,y> = QQ[]
I = R.ideal(x^2 - y, y^2 - x)

F.<a> = GF(3^3)
```

Read these as declarations of a polynomial ring and a finite field, not as variable
initialization. Use the angle-bracket preparser syntax where it makes the declaration
shorter and clearer. Do not use it in ordinary `.py` files, where it is not Python
syntax.

Prefer canonical Sage mathematical objects to manual matrices, raw vectors, and
ad-hoc records when the canonical object exists. In `.sage`, use `^` for powers, `+`
for established direct-sum notation, and `@` for monoidal products.

### Use Mathematical Unicode In Notebooks

The notebook preamble defines:

```sage
Σ = sum
Π = prod

ℤ = ZZ
ℚ = QQ
ℝ = RR
ℂ = CC
```

Prefer these aliases when they make the Sage expression read like the mathematics:

```sage
R.<x,y> = ℚ[]
M = Π(moduli)
s = Σ(a_i * b_i for a_i, b_i in zip(a, b))
```

Use conventional Greek identifiers such as `φ`, `π`, `τ`, or `Δ` when they are the
names used for the same objects and maps in the surrounding Markdown. The code and
prose should use one notation, not force the reader to translate between `tau`,
`tau_map`, and `τ`.

Unicode is encouraged in notebooks, not indiscriminately in package internals. Use
standard mathematical glyphs with an unambiguous visual meaning; avoid decorative
symbols, confusable lookalikes, and identifiers that cannot be read aloud naturally.

Remember that `ℝ` and `ℂ` are aliases for Sage's machine real and complex fields
`RR` and `CC`. When numerical precision is mathematically relevant, construct and
name the required `RealField` or `ComplexField` explicitly.

### Choose The Kind Of Unknown Intentionally

- Use a symbolic variable for symbolic calculus, limits, differential equations, and
  expressions whose domain is controlled by symbolic assumptions.
- Use a polynomial or power-series generator when coefficients, degree,
  factorization, ideals, quotient rings, or ring homomorphisms matter.
- For a symbolic function, `f(x) = ...` is appropriate. For a polynomial element,
  write `f = ...` after declaring its polynomial ring.
- Do not reuse one printed variable name for unrelated symbolic and algebraic
  elements in the same discussion.
- At a change of parent, write the coercion or named morphism explicitly when that
  change is mathematically significant. A symbolic substitution is not a replacement
  for a ring homomorphism, pullback, base change, or induced map.

### Keep Exact Arithmetic Exact

In preparsed Sage code, write `2/3`, not `0.666...`, when the object is rational.
Write `sqrt(2)` when the exact radical is intended. Better still, construct the number
field when its field structure is part of the question:

```sage
K.<a> = QuadraticField(2)
a^2 == 2
```

A decimal point is a choice of numerical approximation. When approximation is the
question, choose and name the real or complex field and its precision.

Request the mathematical transformation that is wanted: `factor`, `expand`,
`normal_form`, or an appropriate symbolic simplification. Do not apply a generic
simplifier merely to make output look shorter.

### Use Standard Mathematical Operations And Predicates

Prefer the standard Sage surface that names the mathematics:

```sage
A.det()
A.column_space()
f.roots()
p.is_prime()
A.is_singular()
R in CommutativeRings()
```

- Preserve root multiplicities unless the mathematical question asks only for the
  underlying set of roots; only then request `multiplicities=False`.
- Use a predicate on the mathematical object or membership in a Sage category.
  `isinstance(...)` answers an implementation question and is not a substitute for
  either.
- Use the standard Sage spelling actually owned by the object or operation. Do not
  mechanically rewrite every free operation as a method: `gcd(a, b)` and
  `a.gcd(b)` may both be legitimate surfaces.

### Make Collections Match Their Mathematics

- Use a comprehension for the explicit image of a finite collection.
- Construct `Set(...)` only when order and multiplicity are mathematically
  irrelevant. Retain a list, tuple, family, or sequence when either matters.
- A list comprehension is not set-builder notation merely because its syntax resembles
  it. Its codomain is a list, with order and repetitions.
- Prefer a comprehension or application of a named morphism to
  `map(lambda ...)` when the latter hides the mathematical map.
- Use `sum(...)` and `prod(...)` when the expression is mathematically an aggregate.
- Preserve the specified order in a product in a noncommutative parent.
- Prefer `sum(...)` or `prod(...)` to a generic `reduce(...)` when the operation has
  that standard mathematical name.
- Iterate over paired mathematical data directly with `zip(...)`; do not introduce
  indices solely to coordinate parallel lists.
- Keep an explicit loop when it displays a recurrence, orbit, reduction, exhaustive
  search, or boundary calculation that the reader needs to inspect.

Do not praise an abstraction because it saves lines or time. Name the morphism,
action, quotient, universal property, or theorem that explains the repeated
calculation.

When Sage already provides the standard construction, use it in research code.
Reproduce a formula by comprehensions, `sum`, and `prod` only when deriving or auditing
that formula is the notebook's mathematical purpose; compare the result with the
native construction afterward.

### Preserve Mathematical Transformations

When a substitution is genuinely an operation on a symbolic expression, retain the
original and name the result:

```sage
g = f.subs(x=u^2)
```

Do not silently rebind `f` if the notebook is meant to compare the two expressions.
When the change is functorial or algebraic, construct the relevant map and apply it
instead of imitating it with `.subs(...)`.

Prefer an explicit parent or domain to global symbolic assumptions. If symbolic
assumptions are unavoidable, state them beside the expression, keep them local to the
calculation, and remove exactly those assumptions afterward. Never call bare
`forget()`: it erases unrelated mathematical context from the session.

### Let Mathematical Objects Render Themselves

The tracked Sage preamble typesets a typesettable object when it is the final
expression in a cell. Use that form for ordinary inspection:

```sage
X.singular_subscheme()
```

Use `show(...)` when presentation is itself the intent, especially for several named
objects or a deliberately arranged display. Use `print(...)` only when plain text is
the intended mathematical output. Do not duplicate every result with both.

Do not enable `%display latex`. It indiscriminately typesets strings, arrays, and
opaque objects; the repository preamble already provides the narrower behavior
needed for mathematical notebooks.

## Notebook Style: A Digital Chalkboard

A pure-mathematics notebook is a digital chalkboard. Its narrative constructs a
mathematical world; its Sage cells make the objects, maps, calculations, examples, and
failure boundaries inspectable.

### Open With Mathematics
- Open with a precise question, counterexample, unexpected phenomenon, or concrete
  object, not imports, `var(...)`, setup narration, or a feature list.
- Show the first decisive symbolic, geometric, or finite output immediately after the
  question, then state which hypothesis, definition, or distinction it exposes.
- Do not use a sensational claim whose mathematical interpretation is deferred or
  ambiguous. State the summation method, topology, base field, category, or other
  governing context at the point where it matters.

### One Mathematical Move Per Cell
Organize cells by mathematical role, not by software execution phase.

- **Definition or construction:** introduce one parent, object, morphism, or family.
- **Calculation:** compute one invariant, image, kernel, singular locus, normal form,
  or other mathematically named result.
- **Example or boundary case:** instantiate the construction or violate one
  hypothesis deliberately.
- **Consequence:** interpret what follows from the preceding output.

Do not combine a new structure, several unrelated computations, and their
interpretation in one large cell. A reader should be able to name the mathematical
purpose of every cell.

### Narrate The Mathematical World
- Use first-person plural to locate the reader inside a parent, category, base field,
  scheme, or hypothesis: "We now work over `GF(7)`."
- Do not narrate API mechanics: avoid "we call this function", "the next cell runs",
  and "Sage gives us".
- State each computation's mathematical input and purpose, then interpret the
  displayed object instead of repeating its printed representation.
- Keep code readable to a mathematician. Prefer Sage declarations such as
  `R.<x,y> = PolynomialRing(QQ, 2)` and named morphisms over setup scaffolding.

### Use Failure To Expose Hypotheses
- Deliberately include examples where a tempting identity is false, an operation is
  undefined, a parent is wrong, or a theorem's hypotheses fail.
- A failing cell must be intentional and locally explained. Do not leave an
  unexplained traceback as pedagogy.
- State the exact missing hypothesis, then construct the corrected object or
  assumption. Prefer noninvertibility, noncommutativity, nonreducedness, parent
  mismatch, or predicate failure over artificial software errors.

### Use Visuals For A Named Geometric Question
- A plot follows the construction of the object it depicts.
- Its caption names the feature to inspect: components, intersections, fixed points,
  singular points, real loci, chambers, or variation in a family.
- State explicitly what the picture suggests and what it does not establish.
- Never infer genus, smoothness, irreducibility, multiplicity, or a universal claim
  from appearance alone. Compute or prove the relevant invariant separately.

### Move From Explicit Examples To Structure
- Begin with finite enumeration or a small hand-check when it reveals the definition.
- Then replace the repeated calculation by the homomorphism, action, quotient,
  functor, universal property, or category method that explains it.
- Name what the abstraction removes and what new statement it makes possible; fewer
  lines or faster execution are not mathematical explanations.

### Survive Static Export
- The mathematical argument must remain readable in HTML, PDF, and a nonexecuted
  notebook.
- Every interactive display has representative static states chosen for a stated
  mathematical reason.
- Explain what the control varies and which features remain invariant.
- Do not make an animation or slider the only place where a mathematical distinction
  appears; surrounding Markdown must make sense without interaction.

### State The Epistemic Status Of The Output
End each substantial exploration with a clearly labeled mathematical conclusion. State
whether a definition was instantiated, an identity was established by an exact
algorithm, a finite statement was established by exhaustive enumeration, examples
suggest a conjecture, a general theorem was invoked with identified hypotheses, or a
general statement remains to be proved.

Do not say that computation never proves anything. Complete finite enumeration can
establish a finite claim, and an exact algorithm can establish a result within its
mathematical contract. Conversely, finitely many examples do not establish an
unbounded universal statement.

### Markdown-Only Litmus Test
If the computation cells are hidden, the Markdown should still present a coherent
mathematical chapter: question, definitions, hypotheses, logical transitions, and
interpretation of each result. It need not reproduce the calculations or pretend that
the missing outputs were proved in prose.

For a mathematical writer, a test is a notebook whose code and output let a
mathematician inspect falsifiable mathematical work. Software test plans, QC commands,
build instructions, readiness reports, and internal consistency summaries do not meet
that standard.

Do not run software verification or terminology audits for notebook or preamble work
unless the user explicitly requests them.
