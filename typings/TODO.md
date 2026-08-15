# Outstanding Sage stub work

The Sage stubs are complete when they express the mathematical types supplied
by Sage category membership and preserve those types through the concrete Sage
implementations used by the preamble.

## Category-owned types

- [ ] Complete the static types `Set`, `Group`, `Ring`, `Field`, `Module`,
  `EnumeratedSet`, and `FiniteEnumeratedSet`.
- [ ] Give each type the complete method surface supplied by its category's
  inherited `ParentMethods` hierarchy.
- [ ] Encode the category inheritance between these method surfaces. Do not
  derive a category type from a Python implementation class.
- [ ] Add the category edge to every concrete implementation stub used by the
  preamble.
- [ ] Preserve distinct implementation types for free modules, free
  submodules, presented modules, and other module constructions.

`Module` must contain every object in `Modules(R)`. The type must not select a
single implementation class or enumerate the implementation classes known to
this repository.

## Foundational Sage contracts

- [ ] Replace unresolved `Any` inputs and returns in `Category`,
  `CategoryWithAxiom`, and `Functor`.
- [ ] Preserve parent element types through construction, membership, maps,
  morphisms, hom-sets, composition, domains, and codomains.
- [ ] Preserve the scalar ring and element type through module construction,
  module morphisms, quotients, and scalar change.
- [ ] Give genuinely unrestricted Sage boundaries one named input type. Keep
  each such boundary local to its owning stub.

## Sage surfaces used by the preamble

- [ ] Finish the overloads and return types for matrix constructors and matrix
  operations.
- [ ] Finish the integer, rational, arithmetic, and symbolic operation types.
- [ ] Finish ideal construction, ideal membership, and ideal element types.
- [ ] Finish graph vertex, edge, layout, and plot types.
- [ ] Finish Cartan-matrix and Coxeter-matrix construction and entry types.
- [ ] Finish quadratic-module, quadratic-form, genus, and normal-form types.
- [ ] Resolve the current partial edits under these paths before adding another
  stub family:
  - `typings/sage/arith/`
  - `typings/sage/functions/`
  - `typings/sage/matrix/`
  - `typings/sage/graphs/`
  - `typings/sage/combinat/root_system/`
  - `typings/sage/modules/`
  - `typings/sage/quadratic_forms/`
  - `typings/sage/rings/ideal.pyi`

## Static specimens

- [ ] Assert the common `Module` contract on parents from distinct module
  implementation hierarchies.
- [ ] Assert that category-created parents receive the same category-owned
  type as concrete Sage parents.
- [ ] Assert preservation of element and scalar types through each foundational
  construction listed above.
- [ ] Assert the refined guarantees supplied by refined categories without
  adding those guarantees to their base category types.

Runtime inspection supplies signatures and confirms Sage's category method
installation. It does not define the mathematical type. The stubs derive that
type from category membership.

Preamble source annotations and implementation errors are separate work after
the stub contracts above are complete.
