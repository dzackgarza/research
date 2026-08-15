# Sage category types

## Contents

- [The mathematical type](#the-mathematical-type)
- [The module schism](#the-module-schism)
- [How the stubs encode category membership](#how-the-stubs-encode-category-membership)
- [Method ownership](#method-ownership)
- [Stub authoring rule](#stub-authoring-rule)

## The mathematical type

For a ring `R`, `Module` is the type of every Sage parent in `Modules(R)`.
Python class ancestry does not define this type.

```text
M in Modules(R)  =>  M: Module
```

Sage supplies category methods to each parent in `Modules(R)`. The complete
inherited `Modules(R).ParentMethods` surface is therefore the common method
guarantee for `Module`.

`ParentMethods` is not the mathematical type. It is Sage's method provider for
parents in a category. The static type is `Module`, and its method surface comes
from that provider.

## The module schism

Sage has two separate hierarchies for modules.

The category hierarchy classifies mathematical objects. Every parent in
`Modules(R)` is a module, independent of its Python implementation class.

The implementation hierarchies represent particular constructions. Examples
include `FreeModule_generic` and `FGP_Module_class`. These classes have different
semantics, methods, and ancestry. Other module implementations can use other
class hierarchies.

No implementation class joins these hierarchies into the mathematical type
`Module`. In particular, `sage.modules.module.Module` names one implementation
class. It does not contain every parent in `Modules(R)`.

This distinction becomes essential for free modules. Sage has several
class-level implementations of free modules, submodules, and presented
quotients. Their common mathematical structure comes from category membership,
not from a selected class, a shared class ancestor, or a union of known classes.

## How the stubs encode category membership

At runtime, Sage combines an implementation class with the dynamic parent class
of its category. This process installs the applicable `ParentMethods` hierarchy
on the parent.

Static type checkers do not reproduce this runtime class construction. These
stubs encode its mathematical result in two places:

```python
Module = Modules.ParentMethods
```

This type-only alias gives the name `Module` to the method surface guaranteed by
membership in `Modules(R)`. It does not claim that Sage exports a runtime class
named `Module`. It also does not identify a mathematical module with Sage's
method-provider class.

Each stubbed implementation class also declares its category edge. For example:

```python
class FreeModule_generic(Modules.ParentMethods[FreeModuleElement, Scalar]): ...
class FGP_Module_class(Modules.ParentMethods[FGP_Element, Scalar]): ...
```

These declarations tell the type checker that each implementation produces
objects of the category type. They do not make either implementation the owner
of `Module`.

## Method ownership

`Module` contains every method guaranteed by the full inherited
`Modules(R).ParentMethods` hierarchy. It contains no method supplied only by one
implementation class.

A concrete implementation type can add stronger guarantees. A refined category
type can add the methods guaranteed by that category. Neither change enlarges
the base type `Module`.

Runtime inspection can confirm that Sage installs category methods. Inspection
of representative implementation classes cannot define the common type or its
method surface.

Generic parameters record facts such as the scalar type and element type. They
parameterize `Module`; they do not establish category membership or method
ownership.

## Stub authoring rule

When a stub needs the type of an arbitrary object in a Sage category:

1. Use the mathematical noun for that category, such as `Module`.
2. Take its guaranteed methods from the complete inherited `ParentMethods`
   hierarchy.
3. Read Sage source for exact signatures and return types.
4. Declare the category edge on each concrete implementation stub.
5. Keep implementation-specific methods on their implementation types.
6. Add generic parameters only to preserve scalar and element relationships.

Do not derive a category type from a nominal implementation class, a union of
known implementations, or the intersection of methods found on sample classes.
Those constructions follow the implementation hierarchy and therefore miss
Sage's category model.
