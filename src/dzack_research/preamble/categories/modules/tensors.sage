r"""Type-$(p,q)$ tensors on a module, and a constructor for them.

A tensor of type $(p,q)$ on $M$ is an element of $M^{\otimes p}\otimes
(M^*)^{\otimes q}$ -- a graded piece of $T(M)\otimes_R T(M^*)$, which is an
$R$-algebra for any commutative $R$ and is bigraded by $(p,q)$ without further
hypothesis.  Identifying that piece with multilinear maps $ (M^*)^p\times M^q
\to R$ is the part that wants $M$ finitely generated projective, and the
components below are read in a framing, so that is where these live.

Evaluation is contraction and is partial: a type-$(p,q)$ tensor fed $k\le q$
elements is a type-$(p,q-k)$ tensor, and only one with no slots left is a
scalar.  A vector is type $(1,0)$ and a functional type $(0,1)$, so nothing
has to be handed in that is not already a tensor.

A Gram matrix is the components of a type-$(0,2)$ tensor in a framing: twice
covariant, because it eats two vectors.  A multiplication table $m:A\otimes_R
A\to A$ is type $(1,2)$ -- once up, twice down.

The constructor mirrors ``matrix``: ``tensor(R, [[...], [...]])`` reads its
shape off the nesting, so a Gram matrix is written exactly as a matrix is.
Mixed valence is stated rather than guessed, since nesting cannot say which
slots are up.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import Element

from itertools import product as _index_product
from typing import ClassVar, Self

from sage.structure.parent import Parent
from sage.structure.element import Element as _SageElement, ModuleElement
from sage.structure.unique_representation import UniqueRepresentation
from sage.misc.cachefunc import cached_function

if TYPE_CHECKING:
    # What ``tensor`` reads its shape off: a rectangular nesting of lists or
    # tuples bottoming out in scalars.  Drawn from Sage's element hierarchy
    # rather than the lexicon noun, because a union is a type only when every
    # member is one, and the lexicon has no stubs yet (issue #354).  Type-only;
    # nothing constructs it.
    Components = list | tuple | _SageElement | int

    # The two parents here are generic in the elements they construct, which is
    # what makes ``self(entries)`` a tensor rather than a bare element.  The
    # runtime classes are Cython extension types and cannot be subscripted, so
    # the binding happens through an alias, per the note in
    # ``typings/sage/structure/parent.pyi``.
    TensorParent = Parent["TensorElement"]
    MixedTensorParent = Parent["MixedTensorElement"]
else:
    TensorParent = Parent
    MixedTensorParent = Parent


def _nesting_shape(components: "Components") -> tuple:
    r"""Return the shape of a nested list, checking it is rectangular."""
    if not isinstance(components, (list, tuple)):
        return ()
    assert components, "a tensor's components cannot be an empty list"
    inner: set[tuple] = {_nesting_shape(entry) for entry in components}
    assert len(inner) == 1, (
        f"the components are ragged: {sorted(inner)} at one level"
    )
    return (len(components),) + inner.pop()


def _entries_by_index(components: "Components", shape: tuple) -> dict:
    r"""Return ``{multi-index: entry}`` for a rectangular nesting."""
    if not shape:
        return {(): components}
    assert isinstance(components, (list, tuple)), (
        f"shape {shape} says there is another level of nesting, but "
        f"{components} is a leaf"
    )
    entries: dict = {}
    for position, block in enumerate(components):
        for index, entry in _entries_by_index(block, shape[1:]).items():
            entries[(position,) + index] = entry
    return entries


@cached_function
def DualModule(module: "Module") -> "Module":
    r"""Return (M^*=\operatorname{Hom}_R(M,R)) from a presentation of (M)."""
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set
    from dzack_research.preamble.utilities import zipsum

    dual_frame = BasedFreeModule(
        module.base_ring(),
        module.module_generating_set(),
    )
    relations = module.relation_matrix()._sage_matrix()
    if relations.nrows() == 0:
        return dual_frame

    relation_labels = finite_ordered_set(tuple(range(relations.nrows())))
    relation_dual = BasedFreeModule(module.base_ring(), relation_labels)
    transpose = relations.transpose()
    restriction = module_homset(dual_frame, relation_dual)(
        {
            label: zipsum(
                row,
                relation_dual.module_generators(),
                relation_dual.zero(),
            )
            for label, row in zip(
                dual_frame.module_generating_set(),
                transpose.rows(),
            )
        }
    )
    return restriction.kernel()


@cached_function
def TensorProductModule(left: "Module", right: "Module") -> "Module":
    r"""Return (M\otimes_RN) from presentations of (M) and (N).

    Sage's mature free-module implementation is
    ``sage.combinat.free_module.CombinatorialFreeModule_Tensor``. This keeps
    its product basis and extends it through the standard right-exact
    presentation: relations are (K\otimes F_N+F_M\otimes L).
    """
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set
    from dzack_research.preamble.utilities import zipsum

    assert left.base_ring() == right.base_ring(), (
        "a tensor product is formed over one base ring"
    )
    left_labels = tuple(left.module_generating_set())
    right_labels = tuple(right.module_generating_set())
    product_labels = finite_ordered_set(
        tuple(_index_product(left_labels, right_labels))
    )
    free_product = BasedFreeModule(left.base_ring(), product_labels)
    left_relations = left.relation_matrix()._sage_matrix().rows()
    right_relations = right.relation_matrix()._sage_matrix().rows()
    relations = []
    for relation in left_relations:
        for right_label in right_labels:
            relations.append(
                zipsum(
                    relation,
                    (
                        free_product.module_generator((left_label, right_label))
                        for left_label in left_labels
                    ),
                    free_product.zero(),
                )
            )
    for left_label in left_labels:
        for relation in right_relations:
            relations.append(
                zipsum(
                    relation,
                    (
                        free_product.module_generator((left_label, right_label))
                        for right_label in right_labels
                    ),
                    free_product.zero(),
                )
            )
    if not relations:
        return free_product

    relation_module = BasedFreeModule(
        left.base_ring(),
        finite_ordered_set(tuple(range(len(relations)))),
    )
    presentation = module_homset(relation_module, free_product)(
        dict(zip(relation_module.module_generating_set(), relations))
    )
    return FinitelyPresentedModule(presentation)


class Tensor(UniqueRepresentation, TensorParent):
    r"""The module of type-$(p,q)$ tensors on $M$."""

    # Bound below, once ``TensorElement`` exists; the category framework reads
    # it off the class.  Declared here so the class states its own element.
    Element: ClassVar[type["TensorElement"]]

    def __init__(self, module: "Module", valence: tuple) -> None:
        contravariant, covariant = valence
        assert contravariant >= 0 and covariant >= 0, (
            f"a tensor type is a pair of counts, got {valence}"
        )
        self._module = module
        self._valence = (contravariant, covariant)
        self._dual_module = DualModule(module)
        self._intrinsic_module, self._index_to_generator = self._build_intrinsic_module()
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        Parent.__init__(self, base=module.base_ring(), category=Modules(module.base_ring()))

    def module(self) -> "Module":
        r"""Return $M$, the module the tensors are on."""
        return self._module

    def valence(self) -> tuple:
        r"""Return $(p,q)$: how many slots are up, and how many down."""
        return self._valence

    def degree(self) -> int:
        r"""Return $p+q$, the number of slots."""
        return sum(self._valence)

    def base_ring(self) -> "Ring":
        return self.base()

    def dual_module(self) -> "Module":
        return self._dual_module

    def intrinsic_module(self) -> "Module":
        r"""Return (M^{\otimes p}\otimes_R(M^*)^{\otimes q})."""
        return self._intrinsic_module

    def _build_intrinsic_module(self) -> tuple:
        from dzack_research.preamble.categories.algebras.framed_free_algebras import TensorAlgebraOn
        from dzack_research.preamble.categories.forms.forms import TensorPower

        contravariant, covariant = self._valence
        vector_power = TensorPower(self._module, contravariant)
        covector_power = TensorPower(self._dual_module, covariant)
        intrinsic = TensorProductModule(vector_power, covector_power)

        def word_label(factor_module: "Module", word: tuple) -> ModuleElement:
            algebra = TensorAlgebraOn(
                factor_module.base_ring(),
                factor_module.module_generating_set(),
            )
            element = algebra.one()
            for label in word:
                element *= algebra.algebra_generator(label)
            label_element: ModuleElement = next(iter(element.coefficients()))
            return label_element

        module_labels = tuple(self._module.module_generating_set())
        dual_labels = tuple(self._dual_module.module_generating_set())
        index_to_generator = {}
        for vector_word in _index_product(module_labels, repeat=contravariant):
            vector_label = word_label(self._module, vector_word)
            for covector_word in _index_product(dual_labels, repeat=covariant):
                covector_label = word_label(self._dual_module, covector_word)
                index = tuple(vector_word) + tuple(covector_word)
                index_to_generator[index] = intrinsic.module_generator(
                    (vector_label, covector_label)
                )
        return intrinsic, index_to_generator

    def _intrinsic_element(self, entries: dict) -> ModuleElement:
        combination: ModuleElement = sum(
            (
                coefficient * self._index_to_generator[index]
                for index, coefficient in entries.items()
            ),
            self._intrinsic_module.zero(),
        )
        return combination

    def _entries_of_intrinsic_element(self, element: ModuleElement) -> dict:
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        generator_to_index = {
            generator: index
            for index, generator in self._index_to_generator.items()
        }
        return {
            generator_to_index[generator]: coefficient
            for generator, coefficient in zip(
                self._intrinsic_module.module_generators(),
                _coordinate_vector(element),
            )
            if coefficient != 0
        }

    def _ring_morphism_defining_module_action(self: Self) -> "Morphism":
        r"""Return $\rho$, scaling every component."""
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
        from sage.categories.homset import Hom
        from sage.categories.morphism import SetMorphism
        from sage.categories.rings import Rings

        endomorphisms = module_homset(self, self)
        return SetMorphism(
            Hom(self.base_ring(), endomorphisms, Rings()),
            lambda scalar: SetMorphism(endomorphisms, lambda t: scalar * t),
        )

    def _repr_(self) -> str:
        contravariant, covariant = self._valence
        return f"Type-({contravariant},{covariant}) tensors on {self._module}"

    def _element_constructor_(self, entries: dict) -> "TensorElement":
        tensor_element: "TensorElement" = self.element_class(self, entries)
        return tensor_element

    def zero(self) -> "TensorElement":
        return self({})

    def mixed_tensor_algebra(self) -> "MixedTensorAlgebra":
        r"""Return \(T(M)\otimes_R T(M^*)\), containing this homogeneous piece."""
        return MixedTensorAlgebra(self._module)


class TensorElement(ModuleElement):
    r"""A tensor, held by its components in the module's framing."""

    if TYPE_CHECKING:
        # A tensor's parent is the type-$(p,q)$ module it was built in;
        # ``Element.parent`` states only that it is some parent.  Declared,
        # never defined: the inherited implementation is the one that runs.
        def parent(self) -> Tensor: ...

    def __init__(self, parent: Tensor, entries: dict) -> None:
        ModuleElement.__init__(self, parent)
        self._intrinsic_element = parent._intrinsic_element(entries)
        self._entries = parent._entries_of_intrinsic_element(self._intrinsic_element)

    def base_changed(self, module: "Module") -> "TensorElement":
        r"""Read this tensor after extending scalars to ``module.base_ring()``."""
        target = Tensor(module, self.valence())
        ring = module.base_ring()
        return target({index: ring(entry) for index, entry in self._entries.items()})

    def valence(self) -> tuple:
        return self.parent().valence()

    def __getitem__(self, index: tuple | int) -> "Element":
        r"""Return the component at a multi-index, zero where unrecorded."""
        index = index if isinstance(index, tuple) else (index,)
        assert len(index) == self.parent().degree(), (
            f"a type-{self.parent().valence()} tensor takes "
            f"{self.parent().degree()} indices, got {len(index)}"
        )
        return self._entries.get(index, self.parent().base_ring().zero())

    def components(self) -> dict:
        r"""Return the components, keyed by multi-index."""
        return dict(self._entries)

    def __eq__(self, other: "Element") -> bool:
        return (
            isinstance(other, TensorElement)
            and other.parent() is self.parent()
            and other._intrinsic_element == self._intrinsic_element
        )

    def _scaled(self, scalar: "Element") -> "TensorElement":
        return self.parent()(
            {index: scalar * entry for index, entry in self._entries.items()},
        )

    def _lmul_(self, scalar: "Element") -> "TensorElement":
        return self._scaled(scalar)

    def _rmul_(self, scalar: "Element") -> "TensorElement":
        return self._scaled(scalar)

    def _add_(self, other: "TensorElement") -> "TensorElement":
        assert other.parent() is self.parent(), (
            "tensors add within one type on one module"
        )
        entries = dict(self._entries)
        for index, entry in other._entries.items():
            entries[index] = entries.get(index, self.parent().base_ring().zero()) + entry
        return self.parent()(entries)

    def _scalar_or_tensor(self, valence: tuple, entries: dict) -> "Element":
        r"""Return the scalar when no slots are left, else the tensor."""
        if sum(valence) == 0:
            return entries.get((), self.parent().base_ring().zero())
        return Tensor(self.parent().module(), valence)(
            {index: entry for index, entry in entries.items() if entry != 0},
        )

    def __call__(self, *arguments: "Element") -> "Element":
        r"""Feed elements into the covariant slots, left to right.

        Partial: a type-$(p,q)$ tensor given $k\le q$ elements is a
        type-$(p,q-k)$ tensor, and only a tensor with no slots left is a
        scalar.  So a multiplication table eats two elements and returns the
        product -- a vector, which is a type-$(1,0)$ tensor -- rather than
        refusing because it has an upper slot.

        Covectors are not a separate kind of thing to be handed in: a
        functional is a type-$(0,1)$ tensor, so pairing against one is
        :meth:`contract`.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        contravariant, covariant = self.valence()
        assert len(arguments) <= covariant, (
            f"a type-{self.valence()} tensor has {covariant} covariant slots, "
            f"got {len(arguments)} arguments"
        )
        coordinates = [_coordinate_vector(argument) for argument in arguments]
        filled = len(coordinates)
        entries: dict = {}
        for index, entry in self._entries.items():
            eaten = index[contravariant : contravariant + filled]
            weight = self.parent().base_ring().one()
            for slot, position in enumerate(eaten):
                weight = weight * coordinates[slot][position]
            if weight == 0:
                continue
            remaining = index[:contravariant] + index[contravariant + filled :]
            entries[remaining] = entries.get(
                remaining, self.parent().base_ring().zero()
            ) + entry * weight
        return self._scalar_or_tensor((contravariant, covariant - filled), entries)

    def contract(self, other: "TensorElement", slot: int | Integer = 0, other_slot: int | Integer = 0) -> "Element":
        r"""Contract an upper slot of this tensor with a lower slot of ``other``.

        The basic operation of the calculus: sum over the shared index.  The
        result is type $(p-1+p',\,q+q'-1)$, and a full contraction leaves a
        scalar.  Evaluating on a vector is the case where ``other`` is that
        vector as a type-$(1,0)$ tensor; pairing with a functional is the case
        where it is a type-$(0,1)$ one.
        """
        contravariant, covariant = self.valence()
        other_contravariant, other_covariant = other.valence()
        assert contravariant > slot >= 0, (
            f"slot {slot} is not an upper index of a type-{self.valence()} tensor"
        )
        assert other_covariant > other_slot >= 0, (
            f"slot {other_slot} is not a lower index of a "
            f"type-{other.valence()} tensor"
        )
        assert other.parent().module() is self.parent().module(), (
            "contraction pairs tensors on one module"
        )
        entries: dict = {}
        for index, entry in self._entries.items():
            for other_index, other_entry in other.components().items():
                if index[slot] != other_index[other_contravariant + other_slot]:
                    continue
                left = index[:slot] + index[slot + 1 :]
                right = (
                    other_index[: other_contravariant + other_slot]
                    + other_index[other_contravariant + other_slot + 1 :]
                )
                # Upper indices first, then lower, so the pieces interleave by
                # valence rather than by which tensor they came from.
                merged = (
                    left[: contravariant - 1]
                    + right[:other_contravariant]
                    + left[contravariant - 1 :]
                    + right[other_contravariant:]
                )
                entries[merged] = entries.get(
                    merged, self.parent().base_ring().zero()
                ) + entry * other_entry
        return self._scalar_or_tensor(
            (contravariant - 1 + other_contravariant, covariant + other_covariant - 1),
            entries,
        )

    def trace(self, slot: int | Integer = 0, other_slot: int | Integer = 0) -> "Element":
        r"""Contract one of this tensor's own upper slots against a lower one."""
        contravariant, covariant = self.valence()
        assert contravariant > slot >= 0 and covariant > other_slot >= 0, (
            f"a type-{self.valence()} tensor has no such pair of slots"
        )
        entries: dict = {}
        for index, entry in self._entries.items():
            if index[slot] != index[contravariant + other_slot]:
                continue
            remaining = tuple(
                position
                for place, position in enumerate(index)
                if place not in (slot, contravariant + other_slot)
            )
            entries[remaining] = entries.get(
                remaining, self.parent().base_ring().zero()
            ) + entry
        return self._scalar_or_tensor((contravariant - 1, covariant - 1), entries)

    def tensor_product(self, other: "TensorElement") -> "TensorElement":
        r"""Return the outer product, concatenating upper and lower slots."""
        assert self.parent().module() is other.parent().module(), (
            "an outer product uses tensors on one module"
        )
        left_upper, left_lower = self.valence()
        right_upper, right_lower = other.valence()
        entries: dict = {}
        for left_index, left_entry in self._entries.items():
            for right_index, right_entry in other._entries.items():
                index = (
                    left_index[:left_upper]
                    + right_index[:right_upper]
                    + left_index[left_upper:]
                    + right_index[right_upper:]
                )
                entries[index] = entries.get(
                    index,
                    self.parent().base_ring().zero(),
                ) + left_entry * right_entry
        return Tensor(
            self.parent().module(),
            (left_upper + right_upper, left_lower + right_lower),
        )({index: entry for index, entry in entries.items() if entry != 0})

    def raise_index(self, formed_module: "Module", slot: int | Integer = 0) -> "TensorElement":
        r"""Raise one lower index with the inverse Gram matrix."""
        from sage.matrix.constructor import matrix

        contravariant, covariant = self.valence()
        assert covariant > slot >= 0, (
            f"slot {slot} is not a lower index of a type-{self.valence()} tensor"
        )
        assert formed_module.forget_form() is self.parent().module(), (
            "the form and tensor must use the same module"
        )
        inverse = matrix(formed_module.gram_matrix()).inverse()
        ring = self.parent().base_ring()
        assert all(entry in ring for entry in inverse.list()), (
            "raising an index over this ring requires a unimodular form"
        )
        rank = inverse.nrows()
        entries: dict = {}
        for index, entry in self._entries.items():
            contracted = index[contravariant + slot]
            remaining_lower = (
                index[contravariant:contravariant + slot]
                + index[contravariant + slot + 1:]
            )
            for raised in range(rank):
                output = index[:contravariant] + (raised,) + remaining_lower
                entries[output] = entries.get(output, ring.zero()) + (
                    ring(inverse[raised, contracted]) * entry
                )
        return Tensor(self.parent().module(), (contravariant + 1, covariant - 1))(
            {index: entry for index, entry in entries.items() if entry != 0}
        )

    def lower_index(self, formed_module: "Module", slot: int | Integer = 0) -> "TensorElement":
        r"""Lower one upper index with the Gram matrix."""
        from sage.matrix.constructor import matrix

        contravariant, covariant = self.valence()
        assert contravariant > slot >= 0, (
            f"slot {slot} is not an upper index of a type-{self.valence()} tensor"
        )
        assert formed_module.forget_form() is self.parent().module(), (
            "the form and tensor must use the same module"
        )
        gram = matrix(formed_module.gram_matrix())
        ring = self.parent().base_ring()
        rank = gram.nrows()
        entries: dict = {}
        for index, entry in self._entries.items():
            contracted = index[slot]
            remaining_upper = index[:slot] + index[slot + 1:contravariant]
            lower = index[contravariant:]
            for lowered in range(rank):
                output = remaining_upper + lower + (lowered,)
                entries[output] = entries.get(output, ring.zero()) + (
                    ring(gram[lowered, contracted]) * entry
                )
        return Tensor(self.parent().module(), (contravariant - 1, covariant + 1))(
            {index: entry for index, entry in entries.items() if entry != 0}
        )

    def __repr__(self) -> str:
        contravariant, covariant = self.valence()
        return (
            f"type-({contravariant},{covariant}) tensor on "
            f"{self.parent().module()}"
        )


Tensor.Element = TensorElement


class MixedTensorAlgebra(UniqueRepresentation, MixedTensorParent):
    r"""The bigraded algebra \(T(M)\otimes_R T(M^*)\)."""

    # Bound below, once ``MixedTensorElement`` exists; the category framework
    # reads it off the class.
    Element: ClassVar[type["MixedTensorElement"]]

    def __init__(self, module: "Module") -> None:
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.algebras.framed_free_algebras import TensorAlgebraOf

        self._module = module
        self._dual_module = DualModule(module)
        self._vector_tensor_algebra = TensorAlgebraOf(module)
        self._covector_tensor_algebra = TensorAlgebraOf(self._dual_module)
        Parent.__init__(
            self,
            base=module.base_ring(),
            category=Algebras(module.base_ring()),
        )

    def module(self) -> "Module":
        return self._module

    def base_ring(self) -> "Ring":
        return self.base()

    def dual_module(self) -> "Module":
        return self._dual_module

    def vector_tensor_algebra(self) -> "Parent":
        r"""Return the factor (T(M))."""
        algebra: "Parent" = self._vector_tensor_algebra
        return algebra

    def covector_tensor_algebra(self) -> "Parent":
        r"""Return the factor (T(M^*))."""
        algebra: "Parent" = self._covector_tensor_algebra
        return algebra

    def homogeneous_piece(self, valence: tuple) -> Tensor:
        r"""Return the component of bidegree ``valence``."""
        return Tensor(self._module, valence)

    def include(self, tensor_element: TensorElement) -> "MixedTensorElement":
        r"""Include a homogeneous tensor in the bigraded algebra."""
        assert tensor_element.parent().module() is self._module, (
            "the tensor must be on this algebra's module"
        )
        return self({tensor_element.valence(): tensor_element})

    def _element_constructor_(self, components: dict) -> "MixedTensorElement":
        mixed_element: "MixedTensorElement" = self.element_class(self, components)
        return mixed_element

    def zero(self) -> "MixedTensorElement":
        return self({})

    def one(self) -> "MixedTensorElement":
        scalar = Tensor(self._module, (0, 0))({(): self.base_ring().one()})
        return self.include(scalar)

    def _ring_morphism_defining_algebra_structure(self) -> "Morphism":
        from sage.categories.homset import Hom
        from sage.categories.morphism import SetMorphism
        from sage.categories.rings import Rings

        return SetMorphism(
            Hom(self.base_ring(), self, Rings()),
            lambda scalar: scalar * self.one(),
        )

    def _repr_(self) -> str:
        return f"Mixed tensor algebra on {self._module}"


class MixedTensorElement(ModuleElement):
    r"""A finite sum of homogeneous mixed tensors."""

    if TYPE_CHECKING:
        # A mixed tensor's parent is the bigraded algebra it was built in;
        # ``Element.parent`` states only that it is some parent.  Declared,
        # never defined: the inherited implementation is the one that runs.
        def parent(self) -> MixedTensorAlgebra: ...

    def __init__(self, parent: MixedTensorAlgebra, components: dict) -> None:
        ModuleElement.__init__(self, parent)
        self._components = {
            tuple(valence): component
            for valence, component in components.items()
            if component != component.parent().zero()
        }
        assert all(
            component.parent() is parent.homogeneous_piece(valence)
            for valence, component in self._components.items()
        ), "each component must belong to its stated bidegree"

    def valences(self) -> tuple:
        return tuple(self._components)

    def homogeneous_component(self, valence: tuple[int, int]) -> TensorElement:
        component: TensorElement = self._components.get(
            tuple(valence),
            self.parent().homogeneous_piece(tuple(valence)).zero(),
        )
        return component

    def _add_(self, other: "MixedTensorElement") -> "MixedTensorElement":
        components = dict(self._components)
        for valence, component in other._components.items():
            components[valence] = components.get(
                valence,
                component.parent().zero(),
            ) + component
        return self.parent()(components)

    def _scaled(self, scalar: "Element") -> "MixedTensorElement":
        return self.parent()(
            {
                valence: scalar * component
                for valence, component in self._components.items()
            }
        )

    def _lmul_(self, scalar: "Element") -> "MixedTensorElement":
        return self._scaled(scalar)

    def _rmul_(self, scalar: "Element") -> "MixedTensorElement":
        return self._scaled(scalar)

    def _mul_(self, other: "MixedTensorElement") -> "MixedTensorElement":
        components: dict = {}
        for left in self._components.values():
            for right in other._components.values():
                product = left.tensor_product(right)
                valence = product.valence()
                components[valence] = components.get(
                    valence,
                    product.parent().zero(),
                ) + product
        return self.parent()(components)

    def __eq__(self, other: "Element") -> bool:
        return (
            isinstance(other, MixedTensorElement)
            and other.parent() is self.parent()
            and other._components == self._components
        )

    def __repr__(self) -> str:
        return repr(self._components)


MixedTensorAlgebra.Element = MixedTensorElement


def tensor(
    base_ring: "Ring",
    components: "Components",
    valence: tuple | None = None,
    module: "Module | None" = None,
) -> TensorElement:
    r"""Return the tensor with these components, as ``matrix`` returns a matrix.

    ``tensor(R, [[-2, 1], [1, -2]])`` is a type-$(0,2)$ tensor: the nesting
    says how many slots there are, and they are covariant unless told
    otherwise, because that is what a form is.  Mixed valence is stated --
    ``valence=(1, 2)`` for a multiplication table -- since a nested list
    cannot say which slots are up.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOn
    from dzack_research.preamble.categories.sets.owned_sets import Sets as _OwnedSets

    shape = _nesting_shape(components)
    assert shape, "a tensor is built from a nested list of components"
    assert len(set(shape)) == 1, (
        f"the slots of a tensor on one module have one size, got shape {shape}"
    )
    if valence is None:
        valence = (0, len(shape))
    assert sum(valence) == len(shape), (
        f"a type-{valence} tensor has {sum(valence)} slots but the components "
        f"are nested {len(shape)} deep"
    )
    if module is None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.sets.sets import Sets

        module = FreeModuleOn(base_ring, Sets.Δ[shape[0] - 1])
    entries = {
        index: base_ring(entry)
        for index, entry in _entries_by_index(components, shape).items()
        if entry != 0
    }
    return Tensor(module, tuple(valence))(entries)
