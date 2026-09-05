r"""An owned lattice parent.

A lattice is a free module with a form.  The form is a type-$(0,2)$
tensor, not a matrix.  The Python class does not extend Sage's
module classes; it keeps an internal
:class:`~sage.combinat.free_module.CombinatorialFreeModule` on a
generating set.  When no generating set is given, that set is the
formal symbols \(e_i\in\mathrm{SR}\).  Named descriptors (``U``, a
finite simply-laced Cartan type, a Euclidean rank) are owned Gram
tensors of type $(0,2)$.
"""

import re

from sage.arith.misc import factor
from sage.categories.category import Category
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets
from sage.combinat.root_system.cartan_type import CartanType, CartanType_abstract
from sage.misc.latex import latex
from sage.misc.repr import repr_lincomb
from sage.modules.free_module_element import FreeModuleElement
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.misc.cachefunc import cached_function
from sage.rings.infinity import Infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ
from sage.structure.element import Matrix, ModuleElement
from sage.structure.element import parent as element_parent
from sage.structure.indexed_generators import IndexedGenerators
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _own_ring,
)
from dzack_research.static_types import ProductOfNaturalNumbers
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    NN,
    Sets,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.tensors.tensor import (
    Tensor,
    TensorModule,
    tensor,
)
from dzack_research.preamble.tensors.tensor import _engine_component_matrix
from dzack_research.preamble.categories.abstract_categories.category_constructions import ProductCategory
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FramedFreeModules,
    FreeModule,
    FreeModuleOn,
    FreshFreeModuleOn,
    MatrixSpace,
)
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
    aleph0,
    cardinal,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.tensors.tensor import (
    _component_shape,
    _tensor_richcmp,
)


def _formal_symbol(index):
    r"""The formal module generator \(e_i\in\mathrm{SR}\)."""
    index = int(index)
    return SR.var(f"e_{index}", latex_name=rf"e_{{{index}}}")


def _formal_symbol_index(elt):
    r"""Return \(i\) when ``elt`` is the formal symbol \(e_i\)."""
    if elt not in SR:
        raise ValueError(elt)
    symbol = SR(elt)
    if not symbol.is_symbol():
        raise ValueError(elt)
    text = str(symbol)
    if not text.startswith("e_"):
        raise ValueError(elt)
    rest = text[2:]
    if not rest.isdigit():
        raise ValueError(elt)
    index = int(rest)
    if symbol != _formal_symbol(index):
        raise ValueError(elt)
    return index


class _FormalSymbols(UniqueRepresentation, Parent):
    r"""The enumerated set \(\{e_i : i\in\mathbb N\}\subset\mathrm{SR}\)."""

    def __init__(self) -> None:
        Parent.__init__(self, facade=SR, category=InfiniteEnumeratedSets())

    def cardinality(self):
        return aleph0

    def unrank(self, index):
        return _formal_symbol(index)

    def rank(self, elt):
        return _formal_symbol_index(elt)

    def __contains__(self, elt):
        try:
            self.rank(elt)
        except TypeError, ValueError:
            return False
        return True

    def __iter__(self):
        index = 0
        while True:
            yield self.unrank(index)
            index += 1

    def _repr_(self) -> str:
        return "{e_i : i in NN} subset of SR"


def _as_generating_set(keys, rank):
    r"""Return ``keys`` as an owned ordered generating set of cardinality ``rank``."""

    if keys is None:
        if rank == Infinity:
            return _FormalSymbols()
        positions = Sets.Δ[int(rank) - 1]
        return finite_ordered_image(
            positions,
            lambda position: _formal_symbol(int(position)),
            rank=lambda symbol: positions.unrank(_formal_symbol_index(symbol)),
            name="Formal lattice generators",
        )
    if isinstance(keys, (list, tuple, range)):
        keys = finite_ordered_set(keys)
    assert keys in EnumeratedSets()
    key_cardinality = keys.cardinality()
    if rank == Infinity:
        if key_cardinality.is_finite():
            raise ValueError(
                f"the generating set has finite cardinality {key_cardinality}, not infinite rank"
            )
    elif (
        not key_cardinality.is_finite()
        or int(key_cardinality.finite_value()) != int(rank)
    ):
        raise ValueError(
            f"the generating set has cardinality {key_cardinality}, not the free-module rank {rank}"
        )
    return keys


def _generating_set_from_names(names, rank):
    r"""Return an owned ordered family of SR symbols named by ``names``."""

    if names is None or rank == Infinity:
        return None
    if isinstance(names, str):
        raw_names = names.split(",")
        name_source = finite_ordered_set(raw_names)
        symbols = finite_ordered_image(
            name_source,
            lambda name: SR.var(str(name).strip()),
            rank=lambda symbol: name_source(str(symbol)),
            name="Named lattice generators",
        )
    else:
        name_source = (
            finite_ordered_set(names)
            if isinstance(names, (list, tuple, range))
            else names
        )
        symbols = finite_ordered_image(
            name_source,
            lambda name: SR.var(str(name)),
            rank=lambda symbol: name_source(str(symbol)),
            name="Named lattice generators",
        )
    size = symbols.cardinality()
    if not size.is_finite() or int(size.finite_value()) != int(rank):
        return None
    return symbols


def _generating_set_for(rank, module_generators, names):
    r"""The generating set: explicit, else ``names`` as SR symbols, else \(e_i\)."""
    if module_generators is not None:
        return _as_generating_set(module_generators, rank)
    named = _generating_set_from_names(names, rank)
    if named is not None:
        return named
    return _as_generating_set(None, rank)


def _resolve_key(keys, index):
    r"""Return ``index`` as an element of the generating set ``keys``."""
    if index in keys:
        return index
    return keys.unrank(int(index))


def _vector_coefficients(vector, module):
    r"""The support of an internal module vector, as an indexed family."""
    # The owned free-module element stores its finite support explicitly.
    return dict(vector.monomial_coefficients())


def _lattice_vector_from_coefficients(lattice, coefficients):
    r"""The lattice vector with the given basis coefficients."""
    return sum(
        (lattice.module_generator(key) * coefficient for key, coefficient in coefficients.items()),
        lattice.element_class(lattice, lattice._module.zero()),
    )


class Lattice(Parent, IndexedGenerators):
    r"""A lattice: a free module with a form, as a parent in :class:`Lattices`.

    The internal module is an owned free module on a generating
    set stored here.  With no generating set given, that set is the
    formal symbols \(e_i\in\mathrm{SR}\).  An element prints as a linear
    combination of those generators, never as a coordinate tuple.
    """

    _repr_term = IndexedGenerators._repr_generator
    _latex_term = IndexedGenerators._latex_generator

    def __init__(
        self,
        module,
        gram,
        category: Category,
        sage_lattice,
        names=None,
        *,
        subobject_ambient=None,
        subobject_generator_images=None,
        subobject_lift=None,
        subobject_inclusion_factory=None,
        subobject_verify_linearity=True,
    ) -> None:
        self._module = module
        self._preamble_free_module_constructor = module._fresh_free_module_on
        self._gram = gram
        self._sage_lattice = sage_lattice
        parent_category = category
        subobject_data = (
            subobject_inclusion_factory is not None
            or (subobject_ambient is not None and subobject_generator_images is not None)
        )
        if subobject_data:
            from dzack_research.preamble.categories.modules.pure.modules import (
                ModuleSubobjects,
            )

            self._preamble_subobject_ambient = subobject_ambient
            self._preamble_subobject_generator_images = subobject_generator_images
            self._preamble_subobject_lift = subobject_lift
            self._preamble_subobject_inclusion_factory = subobject_inclusion_factory
            self._preamble_subobject_verify_linearity = subobject_verify_linearity
            parent_category = Category.join(
                (category, ModuleSubobjects(category.base_ring()))
            )
        if isinstance(gram, _BiproductGram):
            from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import (
                DirectSumObjects,
            )
            from dzack_research.preamble.categories.sets.indexed_families import (
                indexed_family,
            )

            labels = Sets.Δ[1]
            summands = indexed_family(
                labels,
                lambda index: gram._left if int(index) == 0 else gram._right,
                name="Constructor-owned lattice summands",
            )
            self._preamble_direct_sum_summands = summands
            self._preamble_direct_sum_index_set = labels
            parent_category = Category.join((parent_category, DirectSumObjects()))
        IndexedGenerators.__init__(
            self,
            _basis_keys(module),
            prefix="",
            bracket=False,
            string_quotes=False,
        )
        parent_arguments = {
            "base": category.base_ring(),
            "category": parent_category,
        }
        if names is not None:
            parent_arguments["names"] = names
        Parent.__init__(self, **parent_arguments)

    def __call__(self, x):
        r"""Construct a lattice vector through the owned module representation."""
        return self._element_constructor_(x)

    def _element_constructor_(self, x):
        r"""Return a lattice vector from finite coordinates or keyed support."""
        if isinstance(x, self.element_class) and x.parent() is self:
            return x
        if isinstance(x, (tuple, list)):

            size = self.module_generating_set().cardinality()
            if not size.is_finite():
                raise TypeError(
                    "coordinate sequence syntax requires a finite lattice framing; "
                    "use finitely supported label-keyed coordinates"
                )
            if len(x) != int(size.finite_value()):
                raise ValueError("coordinate sequence has the wrong finite length")
            return self.element_class(self, self._module(x))
        if isinstance(x, FreeModuleElement):
            return self.element_class(self, self._module(x))
        return self.element_class(self, self._module(x))

    def zero(self):
        r"""Return the additive identity of the underlying free module."""
        return self.element_class(self, self._module.zero())

    def an_element(self):
        r"""Return a represented lattice element from the underlying module."""
        return self.element_class(self, self._module.an_element())

    def _first_ngens(self, n):
        r"""Return the first ``n`` module generators, for ``L.<e,f> =`` naming."""
        from itertools import islice

        return tuple(self.module_generator(key) for key in islice(self._indices, n))

    def _assign_names(self, names, *args, **kwds):
        Parent._assign_names(self, names, *args, **kwds)
        self.print_options(names=self.variable_names())

    def _monomial_coefficients(self, vector):
        r"""The support of an internal module vector, as an indexed family."""
        return _vector_coefficients(vector, self._module)

    class Element(ModuleElement):
        r"""A lattice vector: a module element whose parent is the lattice."""

        def __init__(self, parent, vector) -> None:
            ModuleElement.__init__(self, parent)
            self._vector = vector

        def _add_(self, other):
            return self.parent().element_class(self.parent(), self._vector + other._vector)

        def _neg_(self):
            return self.parent().element_class(self.parent(), -self._vector)

        def _lmul_(self, scalar):
            return self.parent().element_class(self.parent(), self._vector * scalar)

        def __mul__(self, other):
            if element_parent(other) is self.parent():
                return self.b(other)
            if other in self.parent().base_ring():
                return self._lmul_(self.parent().base_ring()(other))
            return NotImplemented

        def __pow__(self, exponent):
            if exponent != 2:
                raise ValueError(f"v^n on a lattice vector is q(v) at n=2, got {exponent}")
            return self.parent().q(self)

        __xor__ = __pow__

        def _richcmp_(self, other, op):
            return richcmp(self._vector, other._vector, op)

        def __hash__(self):
            return hash(self._vector)

        def _sorted_items_for_printing(self):
            print_options = self.parent().print_options()
            terms = list(self.parent()._monomial_coefficients(self._vector).items())
            try:
                terms.sort(
                    key=lambda term: print_options["sorting_key"](term[0]),
                    reverse=print_options["sorting_reverse"],
                )
            except TypeError, ValueError:
                pass
            return terms

        def _repr_(self):
            return repr_lincomb(
                self._sorted_items_for_printing(),
                scalar_mult=self.parent()._print_options["scalar_mult"],
                repr_monomial=self.parent()._repr_term,
                strip_one=True,
            )

        def _latex_(self):
            return repr_lincomb(
                self._sorted_items_for_printing(),
                scalar_mult=self.parent()._print_options["scalar_mult"],
                latex_scalar_mult=self.parent()._print_options["latex_scalar_mult"],
                repr_monomial=self.parent()._latex_term,
                is_latex=True,
                strip_one=True,
            )


@cached_function
def _lattice_parent(module, gram, category, sage_lattice, names=None):
    r"""Construct a lattice and install the owned category surface.

    A lattice is its free module together with its form, so two
    constructions naming one module and one Gram name one lattice.  Equal
    Grams hash equally, so this is Sage's own construction cache.
    """

    lattice = Lattice(module, gram, category, sage_lattice, names)
    refiner = getattr(category, "_refine_lattice_object", None)
    return refiner(lattice) if refiner is not None else lattice


class _PairingGram(ModuleElement, Tensor):
    r"""A type-$(0,2)$ tensor named by a pairing rule on a free module.

    The module may have infinite rank.  Components are never stored as a
    rectangular array.  The parent is the type-$(0,2)$ tensor space on
    that module: \((M^*)^{\otimes 2}\) at finite rank, and
    \((M\otimes M)^*\) at infinite rank.
    """

    __hash__ = Tensor._tensor_hash

    def _become_tensor_on(self, module) -> None:
        self._module = module
        rank = module.rank()
        ModuleElement.__init__(self, TensorModule(module.base_ring(), (), (rank, rank)))

    def tensor_valence(self) -> ProductOfNaturalNumbers:
        r"""A Gram tensor is type $(0, 2)$, a point of $\mathbb N^2$ (`CON-15`)."""
        return (NN**2)((0, 2))

    def _index_ranks(self):
        rank = self._module.rank()
        return (rank, rank)

    def index_modules(self):
        return self.parent().index_modules()

    def tensor_indices(self):
        keys = _basis_keys(self._module)
        return ((), (keys, keys))

    def _pairing_name(self) -> str:
        return "pairing"

    def _repr_(self) -> str:
        return f"{self._pairing_name()} ∈ {self.parent()}"

    def base_ring(self):
        return self._module.base_ring()

    def _richcmp_(self, other, op):

        return _tensor_richcmp(self, other, op)

    def signature_pair(self):
        rank = self.tensor_shape()[0]
        if rank == Infinity:
            raise TypeError("this Gram does not supply a signature at infinite rank")
        return _sylvester(self)

    def scaled_by(self, scalar):
        r"""Return the pairing \(\mathrm{scalar}\cdot b\)."""
        scalar = self.base_ring()(scalar)
        if scalar == self.base_ring().one():
            return self
        return _ScaledGram(self, scalar)

    def __mul__(self, other):
        if other in self.base_ring():
            return self.scaled_by(other)
        if isinstance(other, Tensor) and other.tensor_valence() == (NN**2)((1, 0)):
            rank = self.tensor_shape()[0]
            if rank == Infinity:
                raise NotImplementedError(
                    "contraction of a lazy infinite-rank Gram tensor requires a represented dual covector"
                )
            rank = int(rank)
            if other._upper_index_ranks() != (rank,):
                raise ValueError(
                    f"cannot contract Gram rank {rank} with vector ranks {other._upper_index_ranks()}"
                )
            return tensor(
                self.base_ring(),
                (),
                (rank,),
                [
                    sum(
                        (self[i, j] * other[j] for j in range(rank)),
                        self.base_ring().zero(),
                    )
                    for i in range(rank)
                ],
            )
        raise TypeError("a Gram tensor contracts a vector or scales by a scalar")

    def __rmul__(self, scalar):
        return self.scaled_by(scalar)


class _ScaledGram(_PairingGram):
    r"""The pairing \(b'(x,y)=\mathrm{scalar}\cdot b(x,y)\)."""

    def __init__(self, gram, scalar) -> None:
        self._gram = gram
        self._scalar = gram.base_ring()(scalar)
        self._become_tensor_on(gram._module)

    def scaled_by(self, scalar):
        return self._gram.scaled_by(self._scalar * self.base_ring()(scalar))

    def __getitem__(self, index):
        return self._scalar * self._gram[index]

    def pairings_against(self, vector):
        return {key: self._scalar * value for key, value in self._gram.pairings_against(vector).items()}

    def __call__(self, left, right):
        return self._scalar * self._gram(left, right)

    def signature_pair(self):
        if self._scalar == 0:
            return signature_pair(0, 0)
        scaled = self._gram.signature_pair()
        if self._scalar > 0:
            return scaled
        return signature_pair(scaled.second(), scaled.first())

    def _latex_(self) -> str:
        return rf"{latex(self._scalar)}\,\left({latex(self._gram)}\right)"

    def _pairing_name(self) -> str:
        return f"{self._scalar} ({self._gram._pairing_name()})"


class _DiagonalGram(_PairingGram):
    r"""The diagonal pairing \(b(e_i,e_j)=\delta_{ij}\,d_i\).

    Unspecified diagonal entries take the default value.  The Lorentz
    form on \(R^{\mathbb N}\) is the identity with \(d_0=-1\).
    """

    def __init__(self, module, exceptions, default) -> None:
        self._exceptions = exceptions
        self._default = default
        self._become_tensor_on(module)

    def scaled_by(self, scalar):
        scalar = self.base_ring()(scalar)
        if scalar == self.base_ring().one():
            return self
        return _DiagonalGram(
            self._module,
            {key: scalar * value for key, value in self._exceptions.items()},
            scalar * self._default,
        )

    def pairings_against(self, vector):
        coefficients = _vector_coefficients(vector, self._module)
        return {key: self._diagonal_entry(key) * value for key, value in coefficients.items()}

    def _diagonal_entry(self, key):
        key = _resolve_key(_basis_keys(self._module), key)
        if key in self._exceptions:
            return self._exceptions[key]
        return self._default

    def __getitem__(self, index):
        keys = _basis_keys(self._module)
        i = _resolve_key(keys, index[0])
        j = _resolve_key(keys, index[1])
        if i != j:
            return self.base_ring().zero()
        return self._diagonal_entry(i)

    def __call__(self, left, right):
        coefficients_left = _vector_coefficients(left, self._module)
        coefficients_right = _vector_coefficients(right, self._module)
        keys = set(coefficients_left) | set(coefficients_right)
        ring = self.base_ring()
        return sum(
            (self._diagonal_entry(key) * coefficients_left.get(key, ring.zero()) * coefficients_right.get(key, ring.zero()) for key in keys),
            ring.zero(),
        )

    def signature_pair(self):
        rank = self._module.rank()
        default = self._default
        if rank != Infinity:
            return _sylvester(self)
        negative_exceptions = sum(1 for value in self._exceptions.values() if value < 0)
        positive_exceptions = sum(1 for value in self._exceptions.values() if value > 0)
        if default > 0:
            return signature_pair(Infinity, negative_exceptions)
        if default < 0:
            return signature_pair(positive_exceptions, Infinity)
        return signature_pair(positive_exceptions, negative_exceptions)

    def _latex_(self) -> str:
        rank = self._module.rank()
        ring = self.base_ring()
        if self._default == ring.one() and len(self._exceptions) == 1:
            key, value = next(iter(self._exceptions.items()))
            if _basis_keys(self._module).rank(key) == 0 and value == -ring.one():
                if rank == Infinity:
                    return r"[-1]\oplus I_{\infty}"
                if rank == 1:
                    return r"[-1]"
                return rf"[-1]\oplus I_{{{int(rank) - 1}}}"
        if not self._exceptions:
            if rank == Infinity:
                return rf"{latex(self._default)}\,I_{{\infty}}"
            return rf"{latex(self._default)}\,I_{{{rank}}}"
        if rank == Infinity:
            return r"D_{\infty}"
        return rf"D_{{{rank}}}"

    def _pairing_name(self) -> str:
        rank = self._module.rank()
        ring = self.base_ring()
        if self._default == ring.one() and len(self._exceptions) == 1:
            key, value = next(iter(self._exceptions.items()))
            if _basis_keys(self._module).rank(key) == 0 and value == -ring.one():
                if rank == Infinity:
                    return "[-1] ⊕ I_∞"
                if rank == 1:
                    return "[-1]"
                return f"[-1] ⊕ I_{int(rank) - 1}"
        if not self._exceptions:
            default = self._default
            if default == ring.one():
                symbol = "I_∞" if rank == Infinity else f"I_{rank}"
                return symbol
            prefix = str(default)
            symbol = "I_∞" if rank == Infinity else f"I_{rank}"
            return f"{prefix} {symbol}"
        if rank == Infinity:
            return "D_∞"
        return f"D_{rank}"


class _IdentityGram(_DiagonalGram):
    r"""The identity type-$(0,2)$ tensor of a free module in its standard basis.

    This is the Euclidean form of \(R^n\) and of the colimit \(R^{\mathbb N}\):
    \(\langle x,y\rangle=\sum_i x_i y_i\), a finite sum.
    """

    def __init__(self, module) -> None:
        super().__init__(module, {}, module.base_ring().one())

    def signature_pair(self):
        _rational_fraction_field(self.base_ring())
        return signature_pair(self._module.rank(), 0)

    def _latex_(self) -> str:
        rank = self._module.rank()
        if rank == Infinity:
            return r"I_{\infty}"
        return rf"I_{{{rank}}}"

    def _pairing_name(self) -> str:
        rank = self._module.rank()
        if rank == Infinity:
            return "I_∞"
        return f"I_{rank}"


class _BiproductGram(_PairingGram):
    r"""The Gram of an orthogonal sum, in the concatenated basis.

    The left summand has finite rank \(n\); the right summand may be
    infinite.  Indices \(0,\ldots,n-1\) are the left basis, and the
    right basis is shifted by \(n\).
    """

    def __init__(self, module, left, right, split) -> None:
        self._left = left
        self._right = right
        self._split = split
        self._become_tensor_on(module)

    def __getitem__(self, index):
        i, j = int(index[0]), int(index[1])
        n = self._split
        if i < n and j < n:
            return self._left.gram_tensor()[i, j]
        if i >= n and j >= n:
            return self._right.gram_tensor()[i - n, j - n]
        return self.base_ring().zero()

    def pairings_against(self, vector):
        n = self._split
        keys = _basis_keys(self._module)
        coefficients = _vector_coefficients(vector, self._module)
        left_part = {}
        right_part = {}
        for key, value in coefficients.items():
            position = _basis_position(keys, key)
            if position < n:
                left_part[position] = value
            else:
                right_part[position - n] = value
        result = {}
        for label, value in generator_pairings(
            self._left,
            _lattice_vector_from_coefficients(self._left, left_part),
        ).items():
            left_keys = _basis_keys(self._left._module)
            position = _basis_position(left_keys, label)
            result[keys.unrank(position)] = value
        for label, value in generator_pairings(
            self._right,
            _lattice_vector_from_coefficients(self._right, right_part),
        ).items():
            right_keys = _basis_keys(self._right._module)
            position = _basis_position(right_keys, label)
            result[keys.unrank(n + position)] = value
        return result

    def __call__(self, left, right):
        n = self._split
        keys = _basis_keys(self._module)
        coefficients_left = _vector_coefficients(left, self._module)
        coefficients_right = _vector_coefficients(right, self._module)

        def _split_coefficients(coefficients):
            left_part = {}
            right_part = {}
            for key, value in coefficients.items():
                position = _basis_position(keys, key)
                if position < n:
                    left_part[position] = value
                else:
                    right_part[position - n] = value
            return left_part, right_part

        left_on_left, left_on_right = _split_coefficients(coefficients_left)
        right_on_left, right_on_right = _split_coefficients(coefficients_right)
        return _lattice_vector_from_coefficients(self._left, left_on_left).b(_lattice_vector_from_coefficients(self._left, right_on_left)) + _lattice_vector_from_coefficients(
            self._right, left_on_right
        ).b(_lattice_vector_from_coefficients(self._right, right_on_right))

    def signature_pair(self):
        left = self._left.signature_pair()
        right = self._right.signature_pair()
        return signature_pair(
            left.first() + right.first(),
            left.second() + right.second(),
        )

    def _latex_(self) -> str:
        return (
            rf"{latex(self._left.gram_tensor())} \oplus "
            rf"{latex(self._right.gram_tensor())}"
        )

    def _pairing_name(self) -> str:
        return f"{self._left.gram_tensor()._pairing_name()} ⊕ {self._right.gram_tensor()._pairing_name()}"


class _ColimitGram(_PairingGram):
    r"""The Gram of \(\operatorname{colim}_n L_n\) along \(x\mapsto(x,0)\).

    A pairing on finite support is the pairing in a finite stage large
    enough to contain that support.
    """

    def __init__(self, module, stage) -> None:
        self._stage = stage
        self._stages = {}
        self._become_tensor_on(module)

    def _stage_at(self, n):
        n = int(n)
        if n not in self._stages:
            stage = self._stage(n)
            if stage.rank() != n:
                raise ValueError(f"stage(n) must have rank n, got stage({n}) of rank {stage.rank()}")
            self._stages[n] = stage
        return self._stages[n]

    def __getitem__(self, index):
        i, j = int(index[0]), int(index[1])
        return self._stage_at(max(i, j) + 1).gram_tensor()[i, j]

    def pairings_against(self, vector):
        generating_set = _basis_keys(self._module)
        coefficients = _vector_coefficients(vector, self._module)
        if not coefficients:
            return {}
        stage = self._stage_at(max(int(generating_set.rank(key)) for key in coefficients) + 1)
        stage_vector = _lattice_vector_from_coefficients(
            stage,
            {int(generating_set.rank(key)): value for key, value in coefficients.items()},
        )
        return {generating_set.unrank(int(_basis_keys(stage._module).rank(label))): value for label, value in generator_pairings(stage, stage_vector).items()}

    def __call__(self, left, right):
        generating_set = _basis_keys(self._module)
        coefficients_left = _vector_coefficients(left, self._module)
        coefficients_right = _vector_coefficients(right, self._module)
        keys = set(coefficients_left) | set(coefficients_right)
        if not keys:
            return self.base_ring().zero()
        stage = self._stage_at(max(int(generating_set.rank(key)) for key in keys) + 1)
        positions_left = {int(generating_set.rank(key)): value for key, value in coefficients_left.items()}
        positions_right = {int(generating_set.rank(key)): value for key, value in coefficients_right.items()}
        return _lattice_vector_from_coefficients(stage, positions_left).b(_lattice_vector_from_coefficients(stage, positions_right))

    def signature_pair(self):
        small = self._stage_at(4).signature_pair()
        large = self._stage_at(8).signature_pair()
        small_positive, small_negative = small.first(), small.second()
        large_positive, large_negative = large.first(), large.second()
        if large_negative == small_negative and large_positive > small_positive:
            return signature_pair(Infinity, large_negative)
        if large_positive == small_positive and large_negative > small_negative:
            return signature_pair(large_positive, Infinity)
        if large_positive > small_positive and large_negative > small_negative:
            return signature_pair(Infinity, Infinity)
        return large

    def _latex_(self) -> str:
        return r"\operatorname{colim}_n G_n"

    def _pairing_name(self) -> str:
        return "colim_n G_n"


def diagonal_gram(module, exceptions, default=1):
    r"""The diagonal type-$(0,2)$ tensor on ``module``.

    ``exceptions`` is the indexed family of diagonal values that differ
    from ``default``.  The Lorentz form on \(R^{\mathbb N}\) is
    ``diagonal_gram(R^NN, {0: -1}, default=1)``.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.lattices import Lattices, diagonal_gram
        sage: G = diagonal_gram(ZZ^NN, {0: -1})
        sage: G
        [-1] ⊕ I_∞ ∈ (ZZ^NN ⊗ ZZ^NN)*
        sage: latex(G)
        [-1]\oplus I_{\infty}
        sage: G.parent()
        (ZZ^NN ⊗ ZZ^NN)*
        sage: Lattices(ZZ)(G)
        Integral lattice of rank +Infinity and signature (+Infinity, 1)
    """
    resolved = _owned_free_module(module, module.base_ring())
    keys = _basis_keys(resolved)
    stored = {_resolve_key(keys, index): resolved.base_ring()(value) for index, value in exceptions.items()}
    return _DiagonalGram(resolved, stored, resolved.base_ring()(default))


def orthogonal_sum(left, right, *, category):
    r"""The orthogonal direct sum, in the concatenated basis.

    The left summand must have finite rank, so its basis occupies the
    first \(n\) coordinates and the right basis is shifted by \(n\).
    That covers finite \(\oplus\) finite and finite \(\oplus\) infinite.
    Infinite \(\oplus\) infinite is not this concatenation, and is not
    constructed.
    """
    ring = category.base_ring()
    left_rank = left.rank()
    assert left_rank != Infinity, "the orthogonal sum concatenates the left basis first; put the finite-rank summand on the left"
    split = int(left_rank)
    right_rank = right.rank()
    if right_rank == Infinity:
        generating_set = _as_generating_set(None, Infinity)
    else:
        generating_set = _as_generating_set(None, split + int(right_rank))

    module = FreeModuleOn(ring, generating_set)
    gram = _BiproductGram(module, left, right, split)
    return _lattice_parent(module, gram, category, None, names=None)


def colimit_lattice(stage, *, category):
    r"""\(\operatorname{colim}_n \mathrm{stage}(n)\) along \(x\mapsto(x,0)\).

    ``stage(n)`` is a rank-\(n\) lattice in ``category``.  The colimit
    module is the free module on \(\mathbb N\).
    """
    ring = category.base_ring()
    probe = stage(2)
    if probe not in category:
        raise TypeError("stage(n) must be a lattice in this category")
    if probe.rank() != 2:
        raise ValueError(f"stage(n) must have rank n, got stage(2) of rank {probe.rank()}")

    module = FreshFreeModuleOn(ring, _as_generating_set(None, Infinity))
    return _lattice_parent(
        module,
        _ColimitGram(module, stage),
        category,
        None,
        names=None,
    )


def scale_gram_tensor(gram, scalar):
    r"""Return the type-$(0,2)$ tensor \(\mathrm{scalar}\cdot G\)."""
    scalar = gram.base_ring()(scalar)
    match gram:
        case _PairingGram():
            return gram.scaled_by(scalar)
        case Tensor() if gram.tensor_valence() == (NN**2)((0, 2)):
            return scalar * gram
        case _:
            raise TypeError("scale_gram_tensor takes a type-(0,2) Gram tensor")


def generator_pairings(lattice, element):
    r"""The finite family \(i\mapsto b(e_i,v)\) of nonzero pairings against generators."""
    gram = lattice.gram_tensor()
    match gram:
        case _PairingGram():
            return gram.pairings_against(element._vector)
        case _:
            assert lattice.is_finite_rank()
            return {label: element.b(lattice.module_generator(label)) for label in lattice.module_generating_set()}


def _rational_fraction_field(ring):
    r"""Return \(\operatorname{Frac}(R)\) when that field is \(\mathbb{Q}\).

    The signature pair \((p,q)\) is the real signature of a quadratic
    space over \(\mathbb{Q}\).  When \(\operatorname{Frac}(R)\) is a
    number field, that invariant is not this pair; see the GW theory
    of that field.
    """
    field = ring.fraction_field()
    if _engine_ring(field) is QQ:
        return QQ
    raise TypeError(f"the signature pair (p, q) is the real signature of a quadratic space over QQ; Frac({ring}) is {field}")


def signature_pairs():
    r"""Return \(\mathbf{Card}\times\mathbf{Card}\), where a signature pair lives.

    An index of inertia can be infinite -- \(\mathbb Z^{(\mathbb N)}\) with
    its standard form has \((p,q)=(\aleph_0,0)\) -- so each entry is a
    cardinal and the pair is an object of the product category.
    """

    return ProductCategory(Cardinalities(), Cardinalities())


def signature_pair(positive, negative):
    r"""Return \((p,q)\) as an object of :func:`signature_pairs`."""

    return signature_pairs().pair(cardinal(positive), cardinal(negative))


def _sylvester(gram: Tensor):
    r"""Return $(p,q)$ by Sylvester's law on \(\operatorname{Frac}(R)=\mathbb{Q}\)."""
    field = _rational_fraction_field(gram.base_ring())
    engine_gram = _engine_component_matrix(gram).change_ring(field)
    positive, negative, _radical = QuadraticForm(
        field, engine_gram
    ).signature_vector()
    return signature_pair(int(positive), int(negative))


def signature_pair_of_gram(gram: Tensor):
    r"""Return $(p,q)$ for a Gram tensor, by Sylvester over $\mathbb Q$."""
    if isinstance(gram, _PairingGram):
        return gram.signature_pair()
    return _sylvester(gram)


def discriminant_of_gram(gram: Tensor):
    r"""Return $d_\pm(b)=(-1)^{n(n-1)/2}\det G$."""
    rank = gram.tensor_shape()[0]
    assert rank != Infinity
    if isinstance(gram, _IdentityGram):
        n = int(rank)
        return (-1) ** (n * (n - 1) // 2)
    n = int(rank)

    matrix = MatrixSpace(gram.base_ring(), n).from_rows(gram.components())
    return (-1) ** (n * (n - 1) // 2) * matrix.determinant()


def _format_disc_latex(disc) -> str:
    r"""Format the discriminant with its prime factorization."""
    if disc in (-1, 0, 1):
        return str(disc)
    factorization = factor(disc)
    factorization_latex = str(latex(factorization))
    if factorization_latex == str(disc):
        return str(disc)
    return f"{disc} = {factorization_latex}"


def _hyperbolic_plane_name(gram: Tensor) -> str | None:
    r"""Return ``U`` when ``gram`` is the hyperbolic plane in the standard basis."""
    shape = gram.tensor_shape()
    if shape[0] != 2 or shape[1] != 2:
        return None
    if gram[0, 0] == 0 and gram[1, 1] == 0 and gram[0, 1] == 1 and gram[1, 0] == 1:
        return "U"
    return None


def lattice_latex(lattice: Lattice, ring_tex: str) -> str:
    r"""The archived lattice display: $L$ with its invariants, then $G_L$.

    The Gram tensor is the form of $L$, not $L$; $G_L$ typesets its components.
    """
    rank = lattice.rank()
    gram_latex = str(latex(lattice.gram_tensor()))
    gram_latex = re.sub(r"\b0\b", lambda _match: r"\cdot", gram_latex)
    signature_field = _engine_ring(lattice.base_ring().fraction_field())

    if rank == Infinity:
        if signature_field is QQ:
            pos, neg = lattice.signature_pair()
            invariants = f"L \\in \\mathrm{{Lattices}}({ring_tex}), \\quad \\mathrm{{rk}}(L) = {latex(rank)}, \\quad \\mathrm{{sig}}(L) = ({latex(pos)}, {neg}) \\\\"
        else:
            invariants = f"L \\in \\mathrm{{Lattices}}({ring_tex}), \\quad \\mathrm{{rk}}(L) = {latex(rank)} \\\\"
    elif signature_field is QQ:
        pos, neg = lattice.signature_pair()
        disc_latex = _format_disc_latex(lattice.discriminant())
        invariants = (
            f"L \\in \\mathrm{{Lattices}}({ring_tex}), "
            f"\\quad \\mathrm{{rk}}(L) = {rank}, "
            f"\\quad \\mathrm{{sig}}(L) = ({pos}, {neg}), "
            f"\\quad \\mathrm{{disc}}(L) = {disc_latex} \\\\"
        )
    else:
        disc_latex = _format_disc_latex(lattice.discriminant())
        invariants = f"L \\in \\mathrm{{Lattices}}({ring_tex}), \\quad \\mathrm{{rk}}(L) = {rank}, \\quad \\mathrm{{disc}}(L) = {disc_latex} \\\\"

    lines = [
        r"\begin{gathered}",
        invariants,
    ]
    name = _hyperbolic_plane_name(lattice.gram_tensor())
    if name is not None:
        lines.append(f"L = {name} \\\\")
    lines.append(f"G_L = {gram_latex} \\\\")
    lines.append(r"\end{gathered}")
    return "\n".join(lines)


def _finite_simply_laced_cartan_type(data):
    r"""Return the finite simply-laced Cartan type named by ``data``."""
    match data:
        case CartanType_abstract():
            cartan_type = data
        case str():
            cartan_type = CartanType(data)
        case list() | tuple() if data and isinstance(data[0], str):
            cartan_type = CartanType(list(data))
        case _:
            raise TypeError(f"{data} is not a Cartan type")
    if not cartan_type.is_finite() or not cartan_type.is_simply_laced():
        raise TypeError(f"{cartan_type} is not a finite simply-laced Cartan type")
    return cartan_type


def _hyperbolic_plane_gram_tensor(ring) -> Tensor:
    r"""Return the Gram tensor of the hyperbolic plane \(U\).

    In the standard basis this is the type-$(0,2)$ pairing with
    \(b(e,f)=1\) and \(b(e,e)=b(f,f)=0\).
    """
    zero = ring.zero()
    one = ring.one()
    gram_tensor = tensor(ring, (), (2, 2), ((zero, one), (one, zero)))
    assert gram_tensor.tensor_valence() == (NN**2)((0, 2))
    return gram_tensor


def _root_cartan_gram_tensor(ring, cartan_type) -> Tensor:
    r"""Return the Gram tensor of the simply-laced root lattice.

    In the simple-root basis the pairing is the negative of the Cartan
    form.  That form is type $(0,2)$; Sage's Cartan matrix is only the
    array of those pairing components.
    """
    pairings = cartan_type.cartan_matrix()
    rank = int(cartan_type.rank())
    components = [
        tuple(-ring._from_engine_element(pairings[i, j]) for j in range(rank))
        for i in range(rank)
    ]
    gram_tensor = tensor(ring, (), (rank, rank), components)
    assert gram_tensor.tensor_valence() == (NN**2)((0, 2))
    return gram_tensor


def _nested_gram_tensor(data, ring) -> Tensor:

    match _component_shape(data):
        case (rows, columns):
            gram_tensor = tensor(ring, (), (rows, columns), data)
            assert gram_tensor.tensor_valence() == (NN**2)((0, 2))
            return gram_tensor
        case shape:
            raise TypeError(f"a Gram tensor is type (0,2), got nested shape {shape}")


def _lattice_from_gram_tensor(
    gram_tensor,
    ring,
    names,
    module_generators,
    category,
    root_cartan_type=None,
) -> Lattice:
    match gram_tensor:
        case Tensor() if gram_tensor.tensor_valence() == (NN**2)((0, 2)):
            pass
        case _:
            raise TypeError("a named lattice is built from a type-(0,2) Gram tensor")
    rows, columns = gram_tensor.tensor_shape()
    if rows != columns:
        raise ValueError(f"a Gram tensor is square, got shape {gram_tensor.tensor_shape()}")
    generating_set = _generating_set_for(rows, module_generators, names)

    module = (
        FreeModuleOn(ring, generating_set)
        if module_generators is None
        else FreshFreeModuleOn(ring, generating_set)
    )
    result = _lattice_parent(module, gram_tensor, category, None, names)
    if root_cartan_type is not None and _engine_ring(ring) is SageZZ:
        return category._refine_root_lattice(result, root_cartan_type)
    return result


def _require_form_tensor(form, ring):
    match form:
        case Tensor() if form.tensor_valence() == (NN**2)((0, 2)):
            pass
        case _:
            raise TypeError("form= takes a type-(0,2) tensor")
    if _engine_ring(form.base_ring()) != _engine_ring(ring):
        raise TypeError(f"Lattices({ring}) takes an {ring}-valued form, got a form over {form.base_ring()}")
    return form


def _basis_keys(module):
    r"""The index set of the distinguished basis of ``module``."""
    return module.module_generating_set()


def _basis_position(keys, label):
    r"""Return the owned framing rank of ``label``."""
    return int(keys.rank(label))


def _owned_free_module(data, ring, module_generators=None, names=None):
    r"""The engine free module of a lattice on the generating set of ``data``.

    ``data`` is an owned free module.  Its labels are kept when they were
    chosen; positional labels (``R^n``, ``R^NN``) name nothing, so the
    lattice's generators are then ``module_generators``, ``names``, or the
    formal symbols \(e_i\).
    """

    if data not in FramedFreeModules(ring):
        raise TypeError(f"Lattices({ring}) takes a free module over {ring}, got {data}")
    if _engine_ring(data.base_ring()) != _engine_ring(ring):
        raise TypeError(f"Lattices({ring}) takes a free module over {ring}, got base ring {data.base_ring()}")
    labels = data.module_generating_set()
    rank = data.rank()
    if rank == Infinity:
        positional = labels is NN
    else:
        positional = int(labels.cardinality()) == int(rank) and all(
            (label := labels.unrank(position)) == position
            or (label in NN and int(label) == position)
            for position in range(int(rank))
        )

    if module_generators is None and not positional:
        return FreshFreeModuleOn(ring, labels)
    return FreshFreeModuleOn(
        ring,
        _generating_set_for(rank, module_generators, names),
    )


def _identity_lattice(data, ring, names, module_generators, category) -> Lattice:
    module = _owned_free_module(data, ring, module_generators=module_generators, names=names)
    return _lattice_parent(module, _IdentityGram(module), category, None, names)


def lattice(
    data,
    basis=None,
    names=None,
    form=None,
    module_generators=None,
    *,
    category: Category,
) -> Lattice:
    r"""Return an owned lattice in ``category``.

    ``Lattices(R)(R^n)`` is the standard Euclidean lattice: the identity
    Gram tensor on \(R^n\).  ``Lattices(R)(R^{\mathbb N})`` is the colimit
    of those, with \(\langle x,y\rangle=\sum_i x_i y_i\) on finite
    supports.  A pairing Gram on a free module is itself a lattice:
    ``Lattices(R)(diagonal_gram(R^NN, {0: -1}))``.  ``form=`` equips a
    given free module with such a Gram.  ``module_generators=`` is the
    generating set of that free module; when omitted, the generators
    are the formal symbols \(e_i\in\mathrm{SR}\).  A matrix (type
    $(1,1)$) is refused.  Named descriptors (``'U'``, a finite
    simply-laced Cartan type, a Euclidean rank) are owned Gram tensors.
    """
    if basis is not None:
        raise TypeError("Lattices(R) does not take a spanning basis; construct the free module and the Gram in this category")
    ring = category.base_ring()

    framed = FramedFreeModules(ring)

    if form is not None:
        match data:
            case _PairingGram():
                raise TypeError("a pairing Gram already determines the lattice")
            case _ if data in framed:
                module = _owned_free_module(data, ring, module_generators=module_generators, names=names)
            case _:
                raise TypeError("form= takes a free module as the first argument")
        form = _require_form_tensor(form, ring)
        match form:
            case _PairingGram() if form._module != module:
                raise TypeError("the form is on a different free module")
            case _:
                return _lattice_parent(module, form, category, None, names)

    match data:
        case _PairingGram():
            if module_generators is not None:
                raise TypeError("a pairing Gram already determines the generating set")
            if _engine_ring(data.base_ring()) != _engine_ring(ring):
                raise TypeError(f"Lattices({ring}) takes a Gram over {ring}, got base ring {data.base_ring()}")
            return _lattice_parent(data._module, data, category, None, names)
        case _ if data in framed:
            return _identity_lattice(data, ring, names, module_generators, category)
        case Tensor() if data.tensor_valence() == (NN**2)((0, 2)):
            if _engine_ring(data.base_ring()) != _engine_ring(ring):
                raise TypeError(f"Lattices({ring}) takes a Gram over {ring}, got base ring {data.base_ring()}")
            return _lattice_from_gram_tensor(data, ring, names, module_generators, category)
        case Tensor() | Matrix():
            raise TypeError("a matrix is a type-(1,1) tensor (a linear map); a Gram is a type-(0,2) tensor")
        case "U" | "H":
            return _lattice_from_gram_tensor(
                _hyperbolic_plane_gram_tensor(ring),
                ring,
                names,
                module_generators,
                category,
            )
        case Integer() | int() if int(data) >= 0:

            return _identity_lattice(
                FreeModule(ring, int(data)),
                ring,
                names,
                module_generators,
                category,
            )
        case str():
            cartan_type = _finite_simply_laced_cartan_type(data)
            return _lattice_from_gram_tensor(
                _root_cartan_gram_tensor(ring, cartan_type),
                ring,
                names,
                module_generators,
                category,
                root_cartan_type=cartan_type,
            )
        case CartanType_abstract():
            cartan_type = _finite_simply_laced_cartan_type(data)
            return _lattice_from_gram_tensor(
                _root_cartan_gram_tensor(ring, cartan_type),
                ring,
                names,
                module_generators,
                category,
                root_cartan_type=cartan_type,
            )
        case list() | tuple() if data and isinstance(data[0], (list, tuple)):
            return _lattice_from_gram_tensor(
                _nested_gram_tensor(data, ring),
                ring,
                names,
                module_generators,
                category,
            )
        case list() | tuple() if data and isinstance(data[0], str):
            cartan_type = _finite_simply_laced_cartan_type(data)
            return _lattice_from_gram_tensor(
                _root_cartan_gram_tensor(ring, cartan_type),
                ring,
                names,
                module_generators,
                category,
                root_cartan_type=cartan_type,
            )
        case _:
            raise TypeError(f"Lattices({ring}) takes a free {ring}-module, a type-(0,2) Gram, 'U', a finite simply-laced Cartan type, or a nonnegative rank, got {data!r}")
