# ModulesWithForms Category: ABC Contracts

Authoritative specification of the category-level contract for the lattice
redesign.

This file supersedes the earlier `BilinearModules`-first framing, but the
new `.sage` workflow specs show that the true foundation is broader than
forms alone. The current code-spec split is therefore:

- `rings.py` defines `ModuleBaseRings`, a Sage category that is a subcategory
  of `Rings().PrincipalIdealDomains().Commutative()`.  Existing ring parents
  are enrolled into this category at installation time via
  `ring._refine_category_(ModuleBaseRings())`.  No new ring classes are
  created; Sage's dynamic dispatch then serves the category's `ParentMethods`
  overrides for those ring instances.
- `Modules(R)` patches Sage's `Modules(R)` surface for finitely presented
  PID-module structure independent of forms,
- `Modules(R).WithForm()` is the form-bearing refinement, implemented by
  `ModulesWithForms(R)`.

`ModulesWithForms(R)` remains the category of pairs `(M, f)`, but it is no
longer the only foundational contract in the spec surface. It now sits on
top of the plain module layer rather than carrying all module semantics
itself.

This is an extend-and-specialize design, not a blank-slate replacement of
Sage. The ring/module foundation works directly with Sage's existing ring
parents, free modules, finitely presented quotient modules, homspaces,
tensor/exterior/symmetric algebra constructions, localizations, completions,
and quotient objects such as `QQ/ZZ`; the redesign adds the missing
category-level semantics and interoperable contracts on top of those
existing parents by refining their categories.

`ModuleBaseRings` targets commutative PIDs: base rings for which the
finitely presented module category has a structure theorem usable by the
redesign.  The current scope is expressed as a subcategory of
`Rings().PrincipalIdealDomains().Commutative()`.  A later scope can enlarge
this to Dedekind domains, including rings of integers of number fields with
class number greater than one, once the module layer represents the
necessary ideal-class and projective-module data.

The explicit target base-ring families are:

- `ZZ`,
- `Zp(p)` p-adic integer rings,
- `QQ`,
- `RR`,
- `CC`,
- `QQbar`,
- finite fields `GF(p^n)`.

The `ModuleBaseRings.ParentMethods` overrides drive the enriched surface:

- `r * R` / `R * r` → principal ideal as an *ideal-submodule* (Sage ideal
  with category refined to carry `R`-module structure),
- `R / I` → finitely presented `R`-module quotient object,
- `R^n` → enriched free module in the redesigned `Modules(R)` surface,
- `R.localize(...)`, `R.completion(...)`, `R.fraction_field()` → ring
  returned with `_refine_category_(ModuleBaseRings())` applied so
  downstream expressions keep propagating.

Typical installation sequence (called by `import src.sage_patches`):

```python
from src.sage_patches.ring_base_category import install
install()  # calls ZZ._refine_category_(ModuleBaseRings()), etc.
```

after which ordinary expressions like `2*ZZ`, `ZZ/(2*ZZ)`, and `ZZ^3`
already land in the enriched spec surface without any object-wrapping.

The membership hooks must agree with this class-extension strategy. In
particular:

```python
R = 2 * ZZ
Z2 = ZZ / R

assert ZZ in Modules(ZZ)
assert R in Modules(ZZ)
assert Z2 in Modules(ZZ)
assert Z2 in Modules(Z2)
assert ZZ^3 in Modules(ZZ)
```

These assertions are not optional sugar. They are the reason the ring layer
must override the native Sage methods `__mul__`, `__pow__`, `ideal`, and
`quotient` for the target rings.  The override contract — call `super()` for
the native construction, then call `_refine_category_` on the returned parent
— is the same in each case.  `ModuleBaseRings.ParentMethods` houses all of
those overrides; `ring._refine_category_(ModuleBaseRings())` at installation
time is what activates Sage's dispatch into those methods.

So the design is not "leave every existing method untouched and only bolt on
new names," nor "create new subclasses for every ring family."  Sage's
`_refine_category_` mechanism lets the category's `ParentMethods` selectively
override native Sage methods on existing ring instances precisely where Sage
would otherwise return a parent outside the enriched module category.

An object of `ModulesWithForms(R)` is a pair `(M, f)` where:

- `R` is a commutative PID,
- `M` is a finitely presented `R`-module, with free and torsion parts in
  general,
- `f` is semilinear tensor-degree data with domain some graded piece or
  quotient of the tensor algebra of `M`,
- the current named branches are:
  - bilinear: degree `2`, `sigma = id_R`, with source `M \otimes_R M` or a
    descended quotient such as `Sym_R^2(M)`,
  - quadratic: degree `1`, `sigma(r) = r^2`,
- the same general pair layer is broad enough to host future degree-two
  refinements such as alternating data factoring through `\Lambda_R^2(M)`,
- `S` is an arbitrary `R`-module.

The with-form layer is written for arbitrary finitely generated PID
modules, so objects may be mixed:

```text
M = F ⊕ T
```

with `F` free and `T` torsion. The generic interface must therefore be
defined at the mixed-module level rather than only on free lattices.

The first required codomain examples are:

- `S = R` for integral bilinear/quadratic modules,
- `S = Frac(R)` for rational bilinear/quadratic modules,
- `S = Frac(R) / R` and `S = Frac(R) / 2R` for discriminant-style torsion
  forms,
- `S = QQ / ZZ` and `S = QQ / 2ZZ` in the `R = ZZ` workflow from
  `misc.sage`.

The public contract is therefore module-valued from the start. Ring-valued
forms are important special cases, not the general definition.

The with-form layer owns the Sage-style subcategory machinery:

- `Bilinear()`
- `Quadratic()`
- `Free()`
- `Torsion()`
- `NonDegenerate()`
- `Integral()`
- `Rational()`
- `TensorProducts()`
- `CartesianProducts()`
- `DualObjects()`
- `Homsets()`

Downstream with-form categories are intersections of these axioms. For
example:

```text
BilinearModules(R)
    := ModulesWithForms(R).Bilinear()

QuadraticModules(R)
    := ModulesWithForms(R).Quadratic()

FreeBilinearModules(R)
    := ModulesWithForms(R).Bilinear().Free()

TorsionBilinearModules(R)
    := ModulesWithForms(R).Bilinear().Torsion()

Lattices(R)
    := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()

RationalLattices(R)
    := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()

DiscriminantQuadraticForms(R)
    := ModulesWithForms(R).Quadratic().Torsion().NonDegenerate()
       with quotient-valued codomain, typically K/R or K/2R
```

The older names `BilinearModules` and `QuadraticModules`, if retained at
all, are thin aliases for these subcategories. They are not separate
top-level foundations anymore; the plain-module layer now lives in
`Modules(R)`.

Likewise, `BilinearForms` and `QuadraticForms` should be treated as thin
facade names for the bilinear and quadratic form strata subordinate to
`ModulesWithForms(R)`, not as independent foundations.

The trigger for this split is the new module-level contract in
`tests/sage_spec/module_methods.sage`: duals as literal hom-objects,
submodules with stored embeddings, saturation/index/cokernel/lift
semantics, `Aut` and invariant/coinvariant constructions, tensor/exterior/
symmetric algebra surfaces, and base-change functors all exist before any
form data is attached. `research_workflows.sage` then consumes those
module-level nouns when building the lattice workflows.


## Form Codomains

The codomain of a form is an actual `R`-module parent. The spec should not
introduce a fake codomain descriptor type when Sage already has genuine
module parents for the interesting examples.

Important codomain strata remain:

- `Integral`: codomain `S = R`,
- `Rational`: codomain `S = Frac(R)`,
- discriminant-style quotient codomains such as `Frac(R) / R`,
  `Frac(R) / 2R`, `QQ / ZZ`, and `QQ / 2ZZ`.

These codomain predicates are orthogonal to the free/torsion and
bilinear/quadratic predicates.


## Form ABCs

```python
from abc import ABC, abstractmethod


class ModuleForm(ABC):

    @abstractmethod
    def ambient_module(self) -> FinitelyGeneratedRModule: ...
    """The underlying module M in the pair (M, f)."""

    @abstractmethod
    def domain(self) -> Parent: ...
    """The actual tensor-degree source used to represent the datum."""

    @abstractmethod
    def codomain(self) -> FinitelyGeneratedRModule: ...
    """The target R-module S."""

    @abstractmethod
    def tensor_degree(self) -> Integer: ...

    @abstractmethod
    def scalar_action_endomorphism(self) -> RingEndomorphism: ...
    """The semilinearity twist sigma on the base ring."""

    @abstractmethod
    def evaluate(self, value) -> ModuleElement: ...

    @abstractmethod
    def gram_matrix(self) -> Matrix: ...


class BilinearForm(ModuleForm):
    @abstractmethod
    def evaluate(
        self,
        left,
        right=None,
    ) -> ModuleElement: ...
    """Evaluate on a degree-two tensor source, with optional pair syntax."""

    @abstractmethod
    def associated_quadratic_form(self) -> QuadraticForm: ...


class QuadraticForm(ModuleForm):
    @abstractmethod
    def associated_bilinear_form(self) -> BilinearForm: ...
```

Quadratic structure is a refinement, not the default organizing principle.
The common base is meant to support `L`, `L^*`, and `A_L` uniformly with a
bilinear-first public vocabulary. In particular, code may use `v.q()`
uniformly for diagonal evaluation:

- on bilinear objects: `v.q() := b(v, v)`,
- on quadratic objects: `v.q()` is the genuine quadratic value.


## `ModulesWithForms(R)`

```python
class ModulesWithForms(Category_module):
    """Category of finitely generated R-modules equipped with a form."""

    def super_categories(self):
        return [Modules(self.base_ring()).WithBasis().FinitelyPresented()]

    def additional_structure(self):
        return self
```

`additional_structure()` returns `self`, not `None`: a module map between
two objects with forms is not automatically form-preserving.


## `ModulesWithForms.SubcategoryMethods`

This category should reproduce and specialize the Sage machinery exposed by
`sage.categories.modules.Modules`, especially the pattern around
`SubcategoryMethods`, `TensorProducts`, `CartesianProducts`, and
`DualObjects`.

```python
class ModulesWithForms(Category_module):

    class SubcategoryMethods:

        @cached_method
        def base_ring(self):
            ...

        @cached_method
        def Bilinear(self):
            return self._with_axiom("Bilinear")

        @cached_method
        def Quadratic(self):
            return self._with_axiom("Quadratic")

        @cached_method
        def Free(self):
            return self._with_axiom("Free")

        @cached_method
        def Torsion(self):
            return self._with_axiom("Torsion")

        @cached_method
        def NonDegenerate(self):
            return self._with_axiom("NonDegenerate")

        @cached_method
        def Integral(self):
            return self._with_axiom("Integral")

        @cached_method
        def Rational(self):
            return self._with_axiom("Rational")

        @cached_method
        def TensorProducts(self):
            return TensorProductsCategory.category_of(self)

        @cached_method
        def CartesianProducts(self):
            return CartesianProductsCategory.category_of(self)

        @cached_method
        def DualObjects(self):
            return DualObjectsCategory.category_of(self)

        dual = DualObjects
```

Semantics of the main axioms:

- `Bilinear`: the primary form has arity 2.
- `Quadratic`: the primary form has arity 1.
- `Free`: the underlying module is torsion-free and free of finite rank.
- `Torsion`: the underlying module is finite torsion.
- `NonDegenerate`: the associated bilinear pairing has zero radical.
- `Integral`: codomain is exactly `R`.
- `Rational`: codomain is exactly `K = Frac(R)`.

Objects may carry more structure than one axiom records. For example, an
even discriminant form may be implemented as a torsion bilinear object with
an additional quadratic refinement. The category contract should not force a
second top-level hierarchy for that case.


## `ModulesWithForms.ParentMethods`

```python
class ModulesWithForms(Category_module):

    class ParentMethods(ABC):

        @abstractmethod
        def form(self) -> Form: ...
        """The primary form carried by this object."""

        @abstractmethod
        def gens(self) -> tuple[ModuleWithFormElement, ...]: ...
        """Canonical generators."""

        @abstractmethod
        def zero(self) -> ModuleWithFormElement: ...
        """The additive identity."""

        @abstractmethod
        def base_ring(self) -> Ring: ...
        """The PID R."""

        @abstractmethod
        def free_part(self) -> ModuleWithForm: ...
        """The free summand with the restricted/induced form data."""

        @abstractmethod
        def torsion_part(self) -> ModuleWithForm: ...
        """The torsion summand with the restricted/induced form data."""

        @abstractmethod
        def Hom(self, other: ModuleWithForm) -> ModuleWithFormHomSpace: ...
        """The hom space in ModulesWithForms(R)."""

        @abstractmethod
        def dual(self) -> ModuleWithForm: ...
        """The dual object in the appropriate DualObjects subcategory."""

        @abstractmethod
        def span(
            self,
            elements: Iterable[ModuleWithFormElement],
        ) -> ModuleWithForm: ...
        """The subobject generated by the given elements."""

        @abstractmethod
        def cardinality(self) -> CardinalNumber: ...
        """Cardinality of the underlying set."""

        def End(self) -> ModuleWithFormHomSpace:
            return self.Hom(self)
```

The generic contract intentionally stays thin. Arity-specific operations
belong to the `Bilinear()` and `Quadratic()` refinements.

For a mixed object `M = F ⊕ T`, `free_part()` and `torsion_part()` must be
real objects in the relevant meets of `ModulesWithForms(R)`, not raw
underlying modules or invariant summaries. They are the category-level
handles that allow kernel, image, and cokernel constructions to stay
honest on arbitrary finitely generated PID modules.


## `ModulesWithForms.ElementMethods`

```python
class ModulesWithForms(Category_module):

    class ElementMethods(ABC):

        @abstractmethod
        def parent(self) -> ModuleWithForm: ...

        @abstractmethod
        def __add__(self, other: ModuleWithFormElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def __neg__(self) -> ModuleWithFormElement: ...

        @abstractmethod
        def _lmul_(self, scalar: RingElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def _rmul_(self, scalar: RingElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def __rmul__(self, scalar: RingElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def __eq__(self, other: object) -> bool: ...

        @abstractmethod
        def __hash__(self) -> int: ...

        @abstractmethod
        def to_vector(self) -> Vector: ...
        """Coordinates with respect to parent().gens()."""

        def span(self) -> ModuleWithForm:
            return self.parent().span([self])
```

Uniform diagonal syntax:

- `v.q()` is allowed everywhere.
- In `Bilinear()`, it means `b(v, v)`.
- In `Quadratic()`, it means evaluation of the quadratic form.


## `ModulesWithForms.MorphismMethods`

```python
class ModulesWithForms(Category_module):

    class MorphismMethods(ABC):

        @abstractmethod
        def domain(self) -> ModuleWithForm: ...

        @abstractmethod
        def codomain(self) -> ModuleWithForm: ...

        @abstractmethod
        def __call__(self, v: ModuleWithFormElement) -> ModuleWithFormElement: ...

        @abstractmethod
        def to_matrix(self) -> Matrix: ...
        """Matrix with respect to canonical generators."""

        @abstractmethod
        def kernel(self) -> ModuleWithForm: ...

        @abstractmethod
        def image(self) -> ModuleWithForm: ...

        @abstractmethod
        def cokernel(self) -> ModuleWithForm: ...
        """The actual cokernel object with descended form data."""

        @abstractmethod
        def is_form_preserving(self) -> bool: ...

        def is_injective(self) -> bool:
            ...

        def is_surjective(self) -> bool:
            ...

        def is_bijective(self) -> bool:
            return self.is_injective() and self.is_surjective()
```

Important negative constraints from the corrections:

- morphisms are not containers,
- morphisms do not have `perp`,
- cokernels must construct the correct target object rather than a helper
  invariant package.


## Mixed-Module Kernels, Images, and Cokernels

The motivating case is not only the free lattice path `L -> L^* -> A_L`.
The generic machinery must work for arbitrary finitely generated
`R`-modules with forms:

```text
M = F_M ⊕ T_M
N = F_N ⊕ T_N.
```

Required semantics:

- `kernel(f)` is the actual kernel object with the form restricted from the
  domain; it may itself be free, torsion, or mixed.
- `image(f)` is the actual image object with the form restricted from the
  codomain; it may itself be free, torsion, or mixed.
- `cokernel(f)` is the actual quotient object `N / im(f)` together with the
  descended form data; it is not an SNF-invariant package, even when SNF is
  the internal algorithm used to construct it.
- promotion into `Free()`, `Torsion()`, `Integral()`, `Rational()`,
  `NonDegenerate()`, or quotient-valued discriminant meets happens after
  the categorical object has been constructed, not instead of it.

This is what allows:

- mixed-to-mixed morphisms to stay inside one framework,
- free-to-rational morphisms to produce torsion cokernels when appropriate,
- discriminant descent to be one special case of the generic cokernel
  machine rather than a separate architecture.


## `ModulesWithForms.Homsets.ParentMethods`

```python
class ModulesWithForms(Category_module):

    class Homsets(HomsetsCategory):

        def extra_super_categories(self):
            return [Modules(self.base_category().base_ring())]

        class ParentMethods(ABC):

            @abstractmethod
            def domain(self) -> ModuleWithForm: ...

            @abstractmethod
            def codomain(self) -> ModuleWithForm: ...

            @abstractmethod
            def from_dict(
                self,
                mapping: dict[ModuleWithFormElement, ModuleWithFormElement],
            ) -> ModuleWithFormMorphism: ...

            @abstractmethod
            def from_matrix(self, matrix_data: Matrix) -> ModuleWithFormMorphism: ...

            @abstractmethod
            def from_images(
                self,
                images: Sequence[ModuleWithFormElement],
            ) -> ModuleWithFormMorphism: ...

            @abstractmethod
            def __contains__(self, f: object) -> bool: ...

            def identity(self) -> ModuleWithFormMorphism:
                ...

            def zero(self) -> ModuleWithFormMorphism:
                ...
```

Hom-space containment owns the structural checks. If a specialized homset
represents isometries, its `__contains__` method owns the form-preservation
test.


## Bilinear Refinement

`ModulesWithForms(R).Bilinear()` is the symmetric degree-two,
`sigma = id_R` working stratum for Phases 0 and 1.

```python
class ModulesWithForms(Category_module):

    class Bilinear(CategoryWithAxiom_over_base_ring):

        class ParentMethods(ABC):

            @abstractmethod
            def form(self) -> BilinearForm: ...

            def b(
                self,
                left: ModuleWithFormElement,
                right: ModuleWithFormElement,
            ) -> object:
                return self.form().evaluate(left, right)

            def gram_matrix(self) -> Matrix:
                return self.form().gram_matrix()

            @abstractmethod
            def associated_quadratic_module(self) -> ModuleWithForm: ...

        class ElementMethods(ABC):

            def b(self, other: ModuleWithFormElement) -> object:
                return self.parent().b(self, other)

            def q(self) -> object:
                return self.parent().associated_quadratic_module().form().evaluate(self)

            def is_isotropic(self) -> bool:
                return self.q() == 0

        class MorphismMethods(ABC):

            def is_isometry(self) -> bool:
                return self.is_form_preserving()
```

This is the layer used for lattices, rational lattices, duals, and the
bilinear side of discriminant descent. Its actual source may be
`M \otimes_R M` or a descended symmetric quotient such as `Sym^2_R(M)`,
but the public convenience API still evaluates on pairs `(v, w)`.


## Quadratic Refinement

`ModulesWithForms(R).Quadratic()` is the degree-one semilinear refinement,
with `sigma(r) = r^2` in the current lattice workflow.

```python
class ModulesWithForms(Category_module):

    class Quadratic(CategoryWithAxiom_over_base_ring):

        class ParentMethods(ABC):

            @abstractmethod
            def form(self) -> QuadraticForm: ...

            @abstractmethod
            def associated_bilinear_module(self) -> ModuleWithForm: ...

        class ElementMethods(ABC):

            def q(self) -> object:
                return self.parent().form().evaluate(self)

            def b(self, other: ModuleWithFormElement) -> object:
                return self.parent().associated_bilinear_module().form().evaluate(
                    self,
                    other,
                )
```

Quadratic objects should not fork the architecture. They sit inside the
same `ModulesWithForms` framework and reuse the same module, morphism,
homset, tensor, Cartesian-product, and dual machinery whenever the
mathematics allows it.


## Tensor Products, Cartesian Products, and Duals

The category must expose Sage-style construction subcategories analogous to
`sage.categories.modules.Modules`.

```python
class ModulesWithForms(Category_module):

    class CartesianProducts(CartesianProductsCategory):

        def extra_super_categories(self):
            return [self.base_category()]

    class TensorProducts(TensorProductsCategory):

        def extra_super_categories(self):
            return [self.base_category()]

        class ParentMethods(ABC):

            @abstractmethod
            def tensor_factors(self) -> tuple[ModuleWithForm, ...]: ...
```

Required semantics:

- `CartesianProducts` model direct products with componentwise module
  structure and product form data.
- `TensorProducts` model tensor products of objects with forms whenever the
  codomain arithmetic supports the induced form; the first required target
  is the bilinear integral/rational stratum.
- `DualObjects()` mirrors the Sage construction but is not required to stay
  inside the same codomain stratum. For example, the dual of an integral
  nondegenerate free bilinear object typically lands in the rational
  bilinear stratum.


## Cokernels and Discriminant Descent

This is the main reason the contract is organized at the
`ModulesWithForms` level rather than around separate lattice and
discriminant hierarchies.

The generic construction order is:

1. build the actual module kernel/image/cokernel in the finitely generated
   PID module sense,
2. determine whether the bilinear or quadratic data descends,
3. construct the descended form object on that quotient,
4. promote the resulting object into the richest correct meet.

Suppose:

- `(L_2, beta_2)` is a free bilinear object over `R` with codomain `K`,
- `i: L_1 -> L_2` is a morphism in `ModulesWithForms(R).Bilinear()`,
- `beta_2(v, i(L_1)) \subseteq R` for every `v in L_2`.

Then the cokernel `coker(i)` carries a well-defined descended bilinear form
with codomain `K/R`:

```text
beta_bar([v], [w]) := beta_2(v, w) mod R  in K/R.
```

This is the abstract mechanism behind:

```text
L  ->  L^*  ->  A_L = coker(L -> L^*).
```

If additional quadratic data descends, it should be expressed as a
quadratic refinement on the same cokernel object, typically with codomain
`K/2R`.

Implementation note:

- the public object is the actual cokernel of a specific morphism,
- computing it via Smith normal form invariants is acceptable internally,
- presenting only the invariant package is not acceptable as the public
  semantics.


## Named Downstream Categories

These names are ordinary intersections of `ModulesWithForms` axioms:

```text
BilinearModules(R)
    := ModulesWithForms(R).Bilinear()

QuadraticModules(R)
    := ModulesWithForms(R).Quadratic()

FreeBilinearModules(R)
    := ModulesWithForms(R).Bilinear().Free()

TorsionBilinearModules(R)
    := ModulesWithForms(R).Bilinear().Torsion()

Lattices(R)
    := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Integral()

RationalLattices(R)
    := ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()

DiscriminantBilinearForms(R)
    := ModulesWithForms(R).Bilinear().Torsion()
       with quotient-valued codomain, typically K/R

DiscriminantQuadraticForms(R)
    := ModulesWithForms(R).Quadratic().Torsion().NonDegenerate()
       with quotient-valued codomain, typically K/R or K/2R
```

The point is that `L`, `L^*`, and `A_L` live in one framework and differ by
intersecting axioms, not by switching between unrelated object systems.


## Notes on Sage Wiring

- The design should follow the category pattern of
  `sage.categories.modules.Modules`, especially the source around
  `SubcategoryMethods`, `CartesianProducts`, and `TensorProducts`.
- `_Hom_` is an internal Sage hook. The public contract is `M.Hom(N)`.
- Elements must be genuine Sage `Element` or `ElementWrapper` instances.
- Concrete implementations may store Sage, Julia, or other backend objects,
  but those are calculation engines, not the public API.
