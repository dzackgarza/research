r"""The lattice construction and the Gram presentations of lattice forms.

A lattice over a commutative ring \(R\) is a free \(R\)-module \(M\) with a
symmetric \(R\)-valued bilinear form \(b\in\operatorname{Hom}_R(M\otimes_R M,R)\).
It is built through its immediate structure owner.  The form \(b\) on \(M\)
is computed from a Gram presentation of \(b\) in the framing of \(M\), and
``FormModules(R)(b)`` builds the lattice on the data of \(M\), joined with
``Lattices(R)`` and with the property axioms the presentation decides.  The
lattice therefore is a module all the way down to its underlying set and
answers ``unformed_module()`` with \(M\).  ``FormModules(R)`` retains \(b\) and
\(M\); ``Lattices(R)`` retains the Gram presentation, which is the datum its
level introduces.

A Gram presentation is a type-$(0,2)$ tensor.  At finite rank it has a
component array.  At infinite rank it is a pairing rule on finite supports
(:class:`_PairingGram`), an element of \((M\otimes M)^*\) and not of
\((M^*)^{\otimes 2}\).  Named descriptors (``U``, a finite crystallographic
Cartan type, a Euclidean rank) are Gram presentations.

The pairing rules are this module's private representation of a form; the
routines that read their fields are the rules' own methods and the
construction functions below, which share their owner.
"""

import re
from bisect import bisect_right
from itertools import accumulate, product
from math import prod as product_value

from sage.arith.misc import factor
from sage.combinat.root_system.cartan_type import CartanType, CartanType_abstract
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.misc.unknown import Unknown
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ
from sage.structure.category_object import normalize_names
from sage.structure.element import Matrix, ModuleElement
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FramedFreeModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
    cardinal,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import (
    NN,
    FiniteSets,
    EnumeratedSets,
    Sets,
)
from dzack_research.preamble.tensors.tensor import (
    Tensor,
    TensorModule,
    _component_shape,
    _engine_component_matrix,
    _owned_set_pair,
    _tensor_richcmp,
    tensor,
)
from dzack_research.static_types import ProductOfNaturalNumbers


def _formal_symbol(index):
    r"""The formal module generator \(e_i\in\mathrm{SR}\)."""
    index = int(index)
    return SR.var(f"e_{index}", latex_name=rf"e_{{{index}}}")


def _formal_symbol_index(elt):
    r"""The selected inverse on the formal-symbol image, with ``None`` off it."""
    if elt not in SR:
        return None
    symbol = SR(elt)
    if not symbol.is_symbol():
        return None
    match re.fullmatch(r"e_(0|[1-9][0-9]*)", str(symbol)):
        case None:
            return None
        case matched:
            return NN(int(matched.group(1)))


@cached_function
def _formal_symbols():
    r"""The countably infinite set \(\{e_i : i\in\mathbb N\}\subset\mathrm{SR}\).

    It is the image of \(\mathbb N\) under the injection \(i\mapsto e_i\),
    whose inverse reads the index off the symbol, so it is enumerated by
    \(\mathbb N\) and ranked by that inverse.
    """
    return NN.image_set(
        _formal_symbol,
        inverse=_formal_symbol_index,
    )


def _formal_generating_set(rank):
    r"""The formal symbols \(e_0,\ldots,e_{n-1}\), or all \(e_i\) at infinite rank."""
    size = cardinal(rank)
    match size.is_finite():
        case False:
            return _formal_symbols()
        case True:
            positions = Sets.Δ[int(size) - 1]
            return FiniteOrderedSets().from_indexed(
                positions,
                lambda position: _formal_symbol(int(position)),
                index_of=lambda symbol: positions[_formal_symbol_index(symbol)],
                name="Formal lattice generators",
            )


def _as_generating_set(keys, rank):
    r"""Return ``keys`` as an owned enumerated generating set of cardinality ``rank``.

    An owned enumerated set is taken as given; a finite literal enumeration
    becomes the finite ordered set it enumerates.
    """
    selected = keys if keys in EnumeratedSets() else finite_ordered_set(keys)
    size = cardinal(rank)
    key_cardinality = cardinal(selected.cardinality())
    assert key_cardinality == size, (
        f"the generating set has cardinality {key_cardinality}, not the free-module rank {size}"
    )
    return selected


def _generating_set_from_names(names):
    r"""Return the SR symbols named by the normalized generator ``names``."""
    name_source = finite_ordered_set(names)
    return FiniteOrderedSets().from_indexed(
        name_source,
        lambda name: SR.var(str(name)),
        index_of=lambda symbol: name_source(str(symbol)),
        name="Named lattice generators",
    )


def _generating_set_for(rank, module_generators, names):
    r"""The generating set: explicit, else the named SR symbols, else the formal symbols \(e_i\).

    Names name the generators of a finite framing only; at infinite rank the
    generators are the formal symbols.
    """
    match module_generators:
        case None:
            pass
        case _:
            return _as_generating_set(module_generators, rank)
    match names is not None and cardinal(rank).is_finite():
        case True:
            return _generating_set_from_names(names)
        case False:
            return _formal_generating_set(rank)


def _resolve_key(keys, index):
    r"""Return ``index`` as an element of ``keys``: a label, or a position in its enumeration."""
    match index in keys:
        case True:
            return index
        case False:
            return keys[int(index)]


def _vector_coefficients(vector):
    r"""The finite support of a module vector, as its coefficient on each framing label."""
    return dict(vector.monomial_coefficients())


def _lattice_vector_from_coefficients(lattice, coefficients):
    r"""The lattice vector with the given coefficients on labels or framing positions."""
    return sum(
        (
            lattice.scalar_multiple(coefficient, lattice.module_generator(key))
            for key, coefficient in coefficients.items()
        ),
        lattice.zero(),
    )


def _normalized_lattice_names(names, rank):
    r"""Normalize the generator-name datum of a lattice of the given rank.

    Sage's ``L.<a1,...,a8> =`` preparser supplies the three names
    ``("a1", "Ellipsis", "a8")``.  The lattice constructor owns the rank, so
    it expands that syntax to the eight generator names; every other spelling
    is Sage's own name syntax, normalized by
    :func:`~sage.structure.category_object.normalize_names`.  At infinite rank
    no generator is named, and the names are normalized without a count.
    """
    match names:
        case None:
            return None
    size = cardinal(rank)
    match size.is_finite():
        case False:
            return normalize_names(-1, names)
    count = int(size)
    written = normalize_names(-1, names)
    match written.count("Ellipsis"):
        case 0:
            return normalize_names(count, names)
        case 1:
            assert len(written) == 3 and written[1] == "Ellipsis", (
                "lattice generator ellipsis syntax has the form a1, ..., an"
            )
            first = re.fullmatch(r"(.*?)(\d+)", written[0])
            last = re.fullmatch(r"(.*?)(\d+)", written[2])
            assert first is not None and last is not None, (
                "lattice generator ellipsis endpoints must end in integers"
            )
            assert first.group(1) == last.group(1), (
                "lattice generator ellipsis endpoints require one common prefix"
            )
            start = int(first.group(2))
            stop = int(last.group(2))
            assert start <= stop, "lattice generator ellipsis endpoints are increasing"
            return normalize_names(
                count,
                tuple(f"{first.group(1)}{index}" for index in range(start, stop + 1)),
            )
        case _:
            raise ValueError("lattice generator names contain more than one ellipsis")


def _block_offsets(ranks):
    r"""The positions at which consecutive blocks of the given ranks begin; all but the last are finite."""
    return tuple(accumulate((int(rank) for rank in ranks[:-1]), initial=0))


def _block_position(offsets, position):
    r"""The block a concatenated position lies in, and its place within that block."""
    which = bisect_right(offsets, position) - 1
    return which, position - offsets[which]


def _form_of_gram(module, gram):
    r"""The bilinear form \(b\) on ``module`` whose Gram presentation in its framing is ``gram``.

    At finite rank \(b(e_i,e_j)\) is the component of ``gram`` at \((i,j)\),
    the positions of the framing's enumeration.  At infinite rank \(b\) is the
    pairing rule of the presentation evaluated on finite supports.  Either way
    the result is an element of ``module.bilinear_forms(R)``, the Hom out of
    the tensor square.
    """
    ring = module.base_ring()
    forms = module.bilinear_forms(ring)
    rank = module.module_rank()
    match rank.is_finite():
        case True:
            size = int(rank)
            return forms(
                tuple(
                    tuple(ring(gram[row, column]) for column in range(size))
                    for row in range(size)
                )
            )
        case False:
            return forms(lambda left, right: gram(left, right))


def _gram_rank(gram):
    r"""The rank of the module a Gram presentation is stated on, as a cardinal."""
    return cardinal(gram.tensor_shape()[0])


def _gram_determinant(gram, ring):
    r"""\(\det G\) of a finite Gram presentation, in the framing's enumeration."""
    size = int(_gram_rank(gram))
    return ring.matrix_space(size).from_rows(
        tuple(
            tuple(gram[row, column] for column in range(size))
            for row in range(size)
        )
    ).determinant()


def _known_conjunction(values):
    r"""Conjoin mathematical decisions without treating Unknown as false."""
    unknown = False
    for value in values:
        match value:
            case False:
                return False
            case True:
                pass
            case _:
                unknown = True
    return Unknown if unknown else True


def _regular_scalar(scalar, ring):
    r"""Whether multiplication by this scalar is injective on R.

    Units are regular.  Over a domain regular means nonzero; over a finite
    ring, injective multiplication is surjective and hence the scalar is a
    unit.  Neither criterion asserts regularity for a general zero divisor
    ring whose nonunit regularity has not been decided by these data.
    """
    from dzack_research.preamble.categories.rings.ring_foundation import IntegralDomains

    if scalar.is_unit():
        return True
    if ring in IntegralDomains():
        return scalar != ring.zero()
    if ring in FiniteSets():
        return False
    if scalar == ring.zero():
        return False
    return Unknown


def _gram_is_nondegenerate(gram, ring):
    r"""Whether the correlation of the presented form is injective.

    A unit determinant makes the matrix invertible.  Over a domain, a
    nonzero determinant is equivalent to injectivity.  Over a finite ring,
    an injective endomorphism of R^n is surjective and its determinant is a
    unit.  Over other rings the nonunit determinant does not decide this
    predicate here.  Infinite forms use the actual pairing rule.
    """
    match _gram_rank(gram).is_finite():
        case True:
            return _regular_scalar(_gram_determinant(gram, ring), ring)
        case False:
            return gram.is_nondegenerate()


def _gram_is_unimodular(gram, ring):
    r"""Whether the correlation \(M\to M^\vee\) of the presented form is an isomorphism.

    At finite rank it is decided by \(\det G\in R^\times\); at infinite rank
    the pairing rule decides it or answers ``Unknown``.
    """
    match _gram_rank(gram).is_finite():
        case True:
            return bool(_gram_determinant(gram, ring).is_unit())
        case False:
            return gram.is_unimodular()


def _gram_is_even(gram, ring):
    r"""Whether \(b(x,x)\in 2R\) for every \(x\) of the presented symmetric form.

    For a symmetric form
    \(b(x,x)=\sum_i x_i^2 b(e_i,e_i)+2\sum_{i<j}x_ix_jb(e_i,e_j)\), so
    evenness is membership of every diagonal value in the ideal \(2R\).  The
    ideal is asked of a commutative base ring; over any other ring the answer
    is ``Unknown``.
    """
    match ring in OwnedRings().Commutative():
        case False:
            return Unknown
    twice = ring.ideal(ring(2))
    match _gram_rank(gram).is_finite():
        case True:
            size = int(_gram_rank(gram))
            return all(ring(gram[index, index]) in twice for index in range(size))
        case False:
            return gram.is_even_in(twice)


def _gram_axiom_categories(lattices, gram):
    r"""The property axioms of ``Lattices(R)`` the Gram presentation decides.

    Finite rank, nondegeneracy, unimodularity and evenness are properties of
    the form.  Each is joined at construction exactly when the presentation
    decides that it holds, so an undecided property places nothing.
    """
    ring = lattices.base_ring()
    axioms = []
    match _gram_rank(gram).is_finite():
        case True:
            axioms.append(lattices.FinitelyGenerated())
    match _gram_is_nondegenerate(gram, ring):
        case True:
            axioms.append(lattices.Nondegenerate())
            match _gram_is_unimodular(gram, ring):
                case True:
                    axioms.append(lattices.Unimodular())
    match _gram_is_even(gram, ring):
        case True:
            axioms.append(lattices.Even())
    return tuple(axioms)


def _lattice_object(
    category,
    module,
    gram,
    *,
    names=None,
    extra_categories=(),
    construction_data=None,
    subobject_construction=None,
):
    r"""Build the lattice on ``module`` whose form has the Gram presentation ``gram``.

    This is the one construction every lattice route reaches (``CON-16``).
    ``category`` is ``Lattices(R)`` and ``module`` is the framed free module,
    or the lattice, the form is stated on.  The form \(b\) on ``module`` is
    computed from ``gram`` (:func:`_form_of_gram`) and ``FormModules(R)(b)``
    builds the lattice on the data of ``module``.  Its placement joins
    ``category``, the property axioms ``gram`` decides and
    ``extra_categories``; the lattice level receives ``gram`` as its datum,
    and ``construction_data`` supplies the data the extra categories declare.
    ``subobject_construction`` is the
    :class:`~dzack_research.preamble.categories.modules.pure.modules.ModuleSubobjectConstruction`
    of a lattice built as a subobject, whose inclusion the result retains.
    """
    from dzack_research.preamble.categories.lattices import Lattices
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        FormModules,
    )

    ring = module.base_ring()
    lattices = Lattices(ring)
    assert category is lattices, f"{category} is not the category of lattices over {ring}"
    data = dict(construction_data or {})
    data["gram_tensor"] = gram
    match names:
        case None:
            pass
        case _:
            data["names"] = names
    subobject = {}
    match subobject_construction:
        case None:
            pass
        case _:
            subobject = {
                "_subobject_ambient": subobject_construction.ambient_module(),
                "_subobject_generator_images": subobject_construction.generator_images(),
                "_subobject_lift": subobject_construction.selected_lift(),
                "_subobject_inclusion_factory": subobject_construction.inclusion_factory(),
                "_subobject_verify_linearity": subobject_construction.verify_linearity(),
            }
    return FormModules(ring)(
        _form_of_gram(module, gram),
        _extra_categories=(
            lattices,
            *_gram_axiom_categories(lattices, gram),
            *tuple(extra_categories),
        ),
        _extra_construction_data=data,
        **subobject,
    )


@cached_function
def _lattice_on_gram(category, module, gram, names, cartan_type):
    r"""The lattice on ``module`` with Gram presentation ``gram``.

    A lattice is its module together with its form, so two constructions
    naming one module and one Gram presentation name one lattice; equal Grams
    hash equally, so this is Sage's own construction cache.  A finite
    crystallographic ``cartan_type`` over \(\mathbb Z\) places the lattice in
    ``RootLattices`` with that Cartan type as its datum.
    """
    match cartan_type:
        case None:
            return _lattice_object(category, module, gram, names=names)
        case _:
            from dzack_research.preamble.categories.lattices import RootLattices

            return _lattice_object(
                category,
                module,
                gram,
                names=names,
                extra_categories=(RootLattices(),),
                construction_data={"cartan_type": cartan_type},
            )


class _PairingGram(ModuleElement, Tensor):
    r"""A type-$(0,2)$ tensor named by a pairing rule on a free module.

    The module may have infinite rank.  Components are never stored as a
    rectangular array.  The parent is the type-$(0,2)$ tensor space on
    that module: \((M^*)^{\otimes 2}\) at finite rank, and
    \((M\otimes M)^*\) at infinite rank.

    At infinite rank the rule is the only presentation of the form, so it
    also answers the property questions the construction asks of it:
    :meth:`is_nondegenerate`, :meth:`is_unimodular` and :meth:`is_even_in`
    answer ``Unknown`` for a rule with no decision procedure, and each
    subclass with one overrides them.
    """

    __hash__ = Tensor._tensor_hash

    def _become_tensor_on(self, module) -> None:
        self._module = module
        rank = module.module_rank()
        ModuleElement.__init__(self, TensorModule(module.base_ring(), (), (rank, rank)))

    def tensor_valence(self) -> ProductOfNaturalNumbers:
        r"""A Gram tensor is type $(0, 2)$, a point of $\mathbb N^2$ (`CON-15`)."""
        return (NN**2)((0, 2))

    def _index_ranks(self):
        rank = self._module.module_rank()
        return (rank, rank)

    def index_modules(self):
        return self.parent().index_modules()

    def contravariant_index_generating_sets(self):
        r"""Return the empty contravariant index family of this covariant Gram tensor."""
        return finite_ordered_set(())

    def covariant_index_generating_sets(self):
        r"""Return the two copies of the lattice's actual selected basis set."""
        keys = _basis_keys(self._module)
        return FiniteOrderedSets().from_indexed(
            finite_ordered_set((0, 1)),
            lambda _slot: keys,
            name="Gram-tensor index generating sets",
        )

    def tensor_indices(self):
        return _owned_set_pair(
            self.contravariant_index_generating_sets(),
            self.covariant_index_generating_sets(),
        )

    def _pairing_name(self) -> str:
        return "pairing"

    def _repr_(self) -> str:
        return f"{self._pairing_name()} ∈ {self.parent()}"

    def base_ring(self):
        return self._module.base_ring()

    def _richcmp_(self, other, op):

        return _tensor_richcmp(self, other, op)

    def signature_pair(self):
        r"""Return $(p,q)$ of the rule, by Sylvester's law at finite rank."""
        return _sylvester(self) if _gram_rank(self).is_finite() else Unknown

    def is_nondegenerate(self):
        r"""``Unknown``: no finite restriction of this rule decides injectivity of its correlation."""
        return Unknown

    def is_unimodular(self):
        r"""``Unknown``: no finite restriction of this rule decides that its correlation is an isomorphism."""
        return Unknown

    def is_even_in(self, twice):
        r"""``Unknown``: this rule states no decision of \(b(x,x)\in 2R\) on all of its module."""
        return Unknown

    def dual_gram_on(self, dual_module):
        r"""Materialize the inverse finite Gram; sparse infinite rules override it."""
        rank = _gram_rank(self)
        assert rank.is_finite(), (
            "materializing the inverse of a general pairing requires finite rank; an infinite metric dual needs a defining rule"
        )
        ring = self.base_ring()
        size = int(rank)
        inverse = ring.matrix_space(size).from_rows(
            tuple(self[row, column] for column in range(size)) for row in range(size)
        ).inverse()
        return tensor(ring, (), (rank, rank), tuple(tuple(inverse[row, column] for column in range(size)) for row in range(size)))

    def scaled_by(self, scalar):
        r"""Return the pairing \(\mathrm{scalar}\cdot b\)."""
        scalar = self.base_ring()(scalar)
        if scalar == self.base_ring().one():
            return self
        return _ScaledGram(self, scalar)

    def __mul__(self, other):
        r"""Scale by an element of the base ring, or contract a type-$(1,0)$ vector of the same rank."""
        ring = self.base_ring()
        match other in ring:
            case True:
                return self.scaled_by(other)
        rank = _gram_rank(self)
        assert rank.is_finite(), (
            "contraction of a lazy infinite-rank Gram tensor requires a represented dual covector"
        )
        size = int(rank)
        assert other in TensorModule(ring, (size,), ()), (
            f"a Gram tensor of rank {size} contracts a type-(1,0) vector of rank {size} or scales by a scalar"
        )
        return tensor(
            ring,
            (),
            (size,),
            [
                sum(
                    (self[i, j] * other[j] for j in range(size)),
                    ring.zero(),
                )
                for i in range(size)
            ],
        )

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
        if scaled is Unknown:
            return Unknown
        if self._scalar > 0:
            return scaled
        return signature_pair(scaled.second(), scaled.first())

    def is_nondegenerate(self):
        r"""Scaling a free-module form preserves injectivity exactly for a regular scalar."""
        return _known_conjunction((_regular_scalar(self._scalar, self.base_ring()), self._gram.is_nondegenerate()))

    def is_unimodular(self):
        r"""\(sb\) is unimodular when \(s\) is a unit and \(b\) is unimodular."""
        return self._scalar.is_unit() and self._gram.is_unimodular()

    def is_even_in(self, twice):
        r"""\(sb\) is even when \(s\in 2R\) or \(b\) is even."""
        return self._scalar in twice or self._gram.is_even_in(twice)

    def dual_gram_on(self, dual_module):
        r"""The dual of \(sb\) is \(s^{-1}b^\vee\), for a unit \(s\)."""
        assert self._scalar.is_unit(), (
            f"the metric dual of a scaled form needs a unit scalar; {self._scalar} is not one"
        )
        return _ScaledGram(self._gram.dual_gram_on(dual_module), self._scalar.inverse_of_unit())

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
        coefficients = _vector_coefficients(vector)
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
        coefficients_left = _vector_coefficients(left)
        coefficients_right = _vector_coefficients(right)
        keys = set(coefficients_left) | set(coefficients_right)
        ring = self.base_ring()
        return sum(
            (self._diagonal_entry(key) * coefficients_left.get(key, ring.zero()) * coefficients_right.get(key, ring.zero()) for key in keys),
            ring.zero(),
        )

    def signature_pair(self):
        match _gram_rank(self).is_finite():
            case True:
                return _sylvester(self)
        default = self._default
        negative_exceptions = sum(1 for value in self._exceptions.values() if value < 0)
        positive_exceptions = sum(1 for value in self._exceptions.values() if value > 0)
        if default > 0:
            return signature_pair(cardinal(self._module.module_rank()), negative_exceptions)
        if default < 0:
            return signature_pair(positive_exceptions, cardinal(self._module.module_rank()))
        return signature_pair(positive_exceptions, negative_exceptions)

    def is_nondegenerate(self):
        r"""A diagonal correlation is injective exactly when each entry is regular."""
        return _known_conjunction(
            _regular_scalar(value, self.base_ring())
            for value in (self._default, *self._exceptions.values())
        )

    def is_unimodular(self):
        r"""Unimodularity refers to the full algebraic dual, not its finite-support part.

        At infinite rank over a nonzero ring, all correlation values have
        finite support.  The functional taking every basis vector to 1 is
        in Hom(R^(I), R) but outside that image.  At finite rank the entries
        must all be units, and the common finite-Gram entry checks that case.
        """
        ring = self.base_ring()
        if not _gram_rank(self).is_finite():
            return ring.one() == ring.zero()
        return all(self._diagonal_entry(label).is_unit() for label in _basis_keys(self._module))

    def is_even_in(self, twice):
        r"""A diagonal form is even when every diagonal value lies in \(2R\)."""
        return self._default in twice and all(value in twice for value in self._exceptions.values())

    def dual_gram_on(self, dual_module):
        r"""The dual of a diagonal form with unit entries is the diagonal form of the inverse entries.

        ``dual_module`` is framed by the labels of this form's module, so each
        exceptional value keeps its label.
        """
        assert self._default.is_unit() and all(value.is_unit() for value in self._exceptions.values()), (
            "the represented finite-support metric dual has unit diagonal values"
        )
        return _DiagonalGram(
            dual_module,
            {key: value.inverse_of_unit() for key, value in self._exceptions.items()},
            self._default.inverse_of_unit(),
        )

    def _latex_(self) -> str:
        rank = cardinal(self._module.module_rank())
        ring = self.base_ring()
        if self._default == ring.one() and len(self._exceptions) == 1:
            key, value = next(iter(self._exceptions.items()))
            if int(_basis_keys(self._module).ranking_map()(key)) == 0 and value == -ring.one():
                match rank.is_finite():
                    case False:
                        return r"[-1]\oplus I_{\infty}"
                if int(rank) == 1:
                    return r"[-1]"
                return rf"[-1]\oplus I_{{{int(rank) - 1}}}"
        if not self._exceptions:
            match rank.is_finite():
                case False:
                    return rf"{latex(self._default)}\,I_{{\infty}}"
            return rf"{latex(self._default)}\,I_{{{rank}}}"
        match rank.is_finite():
            case False:
                return r"D_{\infty}"
        return rf"D_{{{rank}}}"

    def _pairing_name(self) -> str:
        rank = cardinal(self._module.module_rank())
        ring = self.base_ring()
        if self._default == ring.one() and len(self._exceptions) == 1:
            key, value = next(iter(self._exceptions.items()))
            if int(_basis_keys(self._module).ranking_map()(key)) == 0 and value == -ring.one():
                match rank.is_finite():
                    case False:
                        return "[-1] ⊕ I_∞"
                if int(rank) == 1:
                    return "[-1]"
                return f"[-1] ⊕ I_{int(rank) - 1}"
        symbol = f"I_{rank}" if rank.is_finite() else "I_∞"
        if not self._exceptions:
            if self._default == ring.one():
                return symbol
            return f"{self._default} {symbol}"
        return f"D_{rank}" if rank.is_finite() else "D_∞"


class _IdentityGram(_DiagonalGram):
    r"""The identity type-$(0,2)$ tensor of a free module in its standard basis.

    This is the Euclidean form of \(R^n\) and of the colimit \(R^{\mathbb N}\):
    \(\langle x,y\rangle=\sum_i x_i y_i\), a finite sum.
    """

    def __init__(self, module) -> None:
        super().__init__(module, {}, module.base_ring().one())

    def signature_pair(self):
        _rational_fraction_field(self.base_ring())
        return signature_pair(cardinal(self._module.module_rank()), 0)

    def dual_gram_on(self, dual_module):
        r"""The identity form is its own metric dual."""
        return _IdentityGram(dual_module)

    def _latex_(self) -> str:
        rank = cardinal(self._module.module_rank())
        match rank.is_finite():
            case False:
                return r"I_{\infty}"
        return rf"I_{{{rank}}}"

    def _pairing_name(self) -> str:
        rank = cardinal(self._module.module_rank())
        match rank.is_finite():
            case False:
                return "I_∞"
        return f"I_{rank}"


class _BiproductGram(_PairingGram):
    r"""The Gram of an orthogonal sum, in the concatenated basis.

    The form on \(\bigoplus_{i\in I} L_i\) is the orthogonal sum of the
    summands' forms: each summand's own form on its own block of
    coordinates, and zero across two distinct blocks.  The bases are
    concatenated in index order, so the summand at the \(k\)-th index
    occupies the coordinates from its offset up to the next one.

    Every summand but the last has finite rank, which is what lets the
    bases be concatenated at all; the last may be infinite.
    """

    def __init__(self, module, summands, offsets) -> None:
        self._summands = summands
        self._blocks = tuple(summands)
        self._offsets = offsets
        self._become_tensor_on(module)

    def _block_of(self, position):
        r"""The summand a concatenated position lies in, and its place there."""
        return _block_position(self._offsets, position)

    def _by_block(self, coefficients):
        r"""Split coefficients on the sum's basis into one part per summand."""
        keys = _basis_keys(self._module)
        parts = {}
        for key, value in coefficients.items():
            which, place = self._block_of(_basis_position(keys, key))
            parts.setdefault(which, {})[place] = value
        return parts

    def __getitem__(self, index):
        row_block, row_place = self._block_of(int(index[0]))
        column_block, column_place = self._block_of(int(index[1]))
        if row_block != column_block:
            return self.base_ring().zero()
        return self._blocks[row_block].gram_tensor()[row_place, column_place]

    def pairings_against(self, vector):
        keys = _basis_keys(self._module)
        result = {}
        for which, part in self._by_block(_vector_coefficients(vector)).items():
            block = self._blocks[which]
            block_keys = block.module_generating_set()
            for label, value in block.generator_pairings(
                _lattice_vector_from_coefficients(block, part)
            ).items():
                position = self._offsets[which] + _basis_position(block_keys, label)
                result[keys[position]] = value
        return result

    def __call__(self, left, right):
        left_parts = self._by_block(_vector_coefficients(left))
        right_parts = self._by_block(_vector_coefficients(right))
        # Distinct summands pair to zero, so only the blocks both vectors
        # meet contribute.
        return sum(
            (
                _lattice_vector_from_coefficients(
                    self._blocks[which], left_parts[which]
                ).b(
                    _lattice_vector_from_coefficients(
                        self._blocks[which], right_parts[which]
                    )
                )
                for which in left_parts.keys() & right_parts.keys()
            ),
            self.base_ring().zero(),
        )

    def signature_pair(self):
        pairs = tuple(block.signature_pair() for block in self._blocks)
        if any(pair is Unknown for pair in pairs):
            return Unknown
        return signature_pair(
            sum(pair.first() for pair in pairs),
            sum(pair.second() for pair in pairs),
        )

    def is_nondegenerate(self):
        r"""An orthogonal sum is nondegenerate when every summand is."""
        return _known_conjunction(block.is_nondegenerate() for block in self._blocks)

    def is_unimodular(self):
        r"""An orthogonal sum is unimodular when every summand is."""
        return _known_conjunction(block.is_unimodular() for block in self._blocks)

    def is_even_in(self, twice):
        r"""An orthogonal sum is even when every summand is."""
        return _known_conjunction(block.is_even() for block in self._blocks)

    def _latex_(self) -> str:
        return r" \oplus ".join(
            str(latex(block.gram_tensor())) for block in self._blocks
        )

    def _pairing_name(self) -> str:
        return " ⊕ ".join(_gram_name(block.gram_tensor()) for block in self._blocks)


class _TensorProductGram(_PairingGram):
    r"""The product pairing on a represented tensor product of lattices."""

    def __init__(self, module, factors) -> None:
        self._factors = factors
        self._become_tensor_on(module)

    def _basis_pairing(self, left_label, right_label):
        ring = self.base_ring()
        return product_value(
            (
                lattice_factor.b(
                    lattice_factor.module_generator(left_label.component(index)),
                    lattice_factor.module_generator(right_label.component(index)),
                )
                for index in self._factors.index_set()
                for lattice_factor in (self._factors[index],)
            ),
            start=ring.one(),
        )

    def __getitem__(self, index):
        labels = _basis_keys(self._module)
        left = _resolve_key(labels, index[0])
        right = _resolve_key(labels, index[1])
        return self._basis_pairing(left, right)

    def pairings_against(self, vector):
        labels = _basis_keys(self._module)
        factors = self._factors
        factor_indices = tuple(factors.index_set())
        result = {}
        for source_label, source_coefficient in _vector_coefficients(vector).items():
            pairing_data = tuple(
                tuple(
                    factors[index].generator_pairings(
                        factors[index].module_generator(source_label.component(index)),
                    ).items()
                )
                for index in factor_indices
            )
            for selected in product(*pairing_data):
                selected_labels = {
                    index: entry[0]
                    for index, entry in zip(factor_indices, selected, strict=True)
                }
                target_label = labels(
                    lambda index, selected_labels=selected_labels: selected_labels[index]
                )
                value = source_coefficient * product_value(
                    (entry[1] for entry in selected), start=self.base_ring().one()
                )
                result[target_label] = result.get(
                    target_label, self.base_ring().zero()
                ) + value
        zero = self.base_ring().zero()
        return {label: value for label, value in result.items() if value != zero}

    def __call__(self, left, right):
        left_coefficients = _vector_coefficients(left)
        right_coefficients = _vector_coefficients(right)
        return sum(
            (
                left_coefficient
                * right_coefficient
                * self._basis_pairing(left_label, right_label)
                for left_label, left_coefficient in left_coefficients.items()
                for right_label, right_coefficient in right_coefficients.items()
            ),
            self.base_ring().zero(),
        )

    def signature_pair(self):
        positive = SageZZ.one()
        negative = SageZZ.zero()
        for lattice_factor in self._factors:
            pair = lattice_factor.signature_pair()
            if pair is Unknown:
                return Unknown
            new_positive = positive * pair.first() + negative * pair.second()
            new_negative = positive * pair.second() + negative * pair.first()
            positive, negative = new_positive, new_negative
        return signature_pair(positive, negative)

    def _latex_(self) -> str:
        return r" \otimes ".join(
            str(latex(lattice_factor.gram_tensor()))
            for lattice_factor in self._factors
        )

    def _pairing_name(self) -> str:
        return " ⊗ ".join(
            _gram_name(lattice_factor.gram_tensor())
            for lattice_factor in self._factors
        )


class _ColimitGram(_PairingGram):
    r"""The Gram of \(\operatorname{colim}_n L_n\) along \(x\mapsto(x,0)\).

    A pairing on finite support is the pairing in a finite stage large
    enough to contain that support.
    """

    def __init__(self, module, stage, row_support=None) -> None:
        self._stage = stage
        self._row_support = row_support
        self._become_tensor_on(module)

    @cached_method
    def _stage_at(self, n):
        stage = self._stage(int(n))
        assert stage.module_rank() == cardinal(n), (
            f"stage(n) must have rank n, got stage({n}) of rank {stage.module_rank()}"
        )
        return stage

    def __getitem__(self, index):
        i, j = int(index[0]), int(index[1])
        return self._stage_at(max(i, j) + 1).gram_tensor()[i, j]

    def pairings_against(self, vector):
        r"""Read all generator pairings using stated finite row supports.

        ``row_support(i)`` contains every j with G[i,j] nonzero.  Such data
        are not part of an arbitrary colimit: a first-stage vector may pair
        nontrivially with arbitrarily late basis vectors.  Evaluation on two
        finite vectors does not need this additional row-finiteness datum.
        """
        coefficients = _vector_coefficients(vector)
        if not coefficients:
            return {}
        assert self._row_support is not None, (
            "enumerating every nonzero generator pairing of this colimit needs stated finite row supports"
        )
        labels = _basis_keys(self._module)
        ranking = labels.ranking_map()
        positions = {int(ranking(label)): value for label, value in coefficients.items()}
        support = {int(column) for row in positions for column in self._row_support(row)}
        return {
            labels[column]: sum((value * self[row, column] for row, value in positions.items()), self.base_ring().zero())
            for column in support
        }

    def __call__(self, left, right):
        generating_set = _basis_keys(self._module)
        coefficients_left = _vector_coefficients(left)
        coefficients_right = _vector_coefficients(right)
        keys = set(coefficients_left) | set(coefficients_right)
        if not keys:
            return self.base_ring().zero()
        ranking = generating_set.ranking_map()
        stage = self._stage_at(max(int(ranking(key)) for key in keys) + 1)
        positions_left = {int(ranking(key)): value for key, value in coefficients_left.items()}
        positions_right = {int(ranking(key)): value for key, value in coefficients_right.items()}
        return _lattice_vector_from_coefficients(stage, positions_left).b(_lattice_vector_from_coefficients(stage, positions_right))

    def signature_pair(self):
        r"""Finite sampling does not determine the inertia of an arbitrary colimit.

        Diagonal forms agreeing through any chosen N can acquire their first
        negative entry at N+1, or infinitely many negative entries thereafter.
        The stage function alone supplies no decision of that infinite datum.
        """
        return Unknown

    def _latex_(self) -> str:
        return r"\operatorname{colim}_n G_n"

    def _pairing_name(self) -> str:
        return "colim_n G_n"


def _gram_name(gram) -> str:
    r"""Name a Gram block in text.

    An infinite-rank block is a pairing rule and is named by its rule.  A
    finite block is named from its components: ``U`` for the hyperbolic
    plane, ``I_n`` for the identity, and ``G_n`` otherwise.
    """
    rank = _gram_rank(gram)
    match rank.is_finite():
        case False:
            return gram._pairing_name()
    size = int(rank)
    match _hyperbolic_plane_name(gram):
        case None:
            pass
        case name:
            return name
    ring = gram.base_ring()
    identity = all(
        gram[row, column] == (ring.one() if row == column else ring.zero())
        for row in range(size)
        for column in range(size)
    )
    return f"I_{size}" if identity else f"G_{size}"


def _diagonal_gram(module, exceptions, default=1):
    r"""The diagonal type-$(0,2)$ tensor on ``module``.

    ``exceptions`` is the indexed family of diagonal values that differ
    from ``default``.  The Lorentz form on \(R^{\mathbb N}\) is
    ``R^NN.diagonal_gram({0: -1}, default=1)``.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.lattices import Lattices
        sage: G = (ZZ^NN).diagonal_gram({0: -1})
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


def _orthogonal_sum(summands):
    r"""\(\bigoplus_{i\in I} L_i\), in the concatenated basis.

    The sum is taken over the family's index set, so three summands are
    three: the summand at each index has its own block of coordinates and
    its own projection, rather than being reached through a nest of
    two-summand sums.

    The bases are concatenated in index order, so every summand but the last
    must have finite rank.  That covers finite \(\oplus\cdots\oplus\) finite
    and a trailing infinite summand.  Two infinite summands are not this
    concatenation, and are not constructed.

    The sum of \(R\)-lattices is an \(R\)-lattice, so the base ring is read
    off the summands rather than supplied.  The result is placed in
    ``BiproductLattices(R)`` with the summand family as its datum.
    """
    from dzack_research.preamble.categories.abstract_categories.products import (
        _finite_factor_family,
    )
    from dzack_research.preamble.categories.lattices import (
        BiproductLattices,
        Lattices,
    )

    summands = _finite_factor_family(summands, name="Orthogonal summands")
    blocks = tuple(summands)
    assert blocks, "an orthogonal sum is taken over a nonempty family of summands"
    ring = blocks[0].base_ring()
    category = Lattices(ring)
    assert all(block in category for block in blocks), (
        "an orthogonal sum requires lattices over one common base ring"
    )
    ranks = tuple(cardinal(block.module_rank()) for block in blocks)
    assert all(rank.is_finite() for rank in ranks[:-1]), (
        "the orthogonal sum concatenates the bases in index order, so only "
        "the summand at the last index may have infinite rank"
    )
    offsets = _block_offsets(ranks)
    total = ranks[-1] if not ranks[-1].is_finite() else cardinal(offsets[-1] + int(ranks[-1]))

    module = ring.free_module(_formal_generating_set(total))
    return _lattice_object(
        category,
        module,
        _BiproductGram(module, summands, offsets),
        extra_categories=(BiproductLattices(ring),),
        construction_data={"biproduct_factors": summands},
    )


def _tensor_product_lattice(factors):
    r"""Return the tensor product lattice with the product bilinear form.

    The lattice is built on the tensor product module of the factors and
    placed in ``TensorProductModules(R)`` with the factor family as its datum.
    """
    from dzack_research.preamble.categories.abstract_categories.products import (
        _finite_factor_family,
    )
    from dzack_research.preamble.categories.lattices import Lattices
    from dzack_research.preamble.categories.modules.pure.modules import (
        Modules,
        TensorProductModules,
    )

    factors = _finite_factor_family(factors, name="Lattice tensor factors")
    values = tuple(factors)
    assert values, "a lattice tensor product is taken over a nonempty family of factors"
    ring = values[0].base_ring()
    category = Lattices(ring)
    assert all(lattice_factor in category for lattice_factor in values), (
        "a lattice tensor product requires lattices over one ring"
    )
    module = Modules(ring).tensor_product(factors)
    return _lattice_object(
        category,
        module,
        _TensorProductGram(module, factors),
        extra_categories=(TensorProductModules(ring),),
        construction_data={"tensor_factors": factors},
    )


def _colimit_lattice(stage, *, category, row_support=None):
    r"""\(\operatorname{colim}_n \mathrm{stage}(n)\) along \(x\mapsto(x,0)\).

    ``stage(n)`` is a rank-\(n\) lattice in ``category``.  The colimit
    module is the free module on the formal symbols \(e_i\), \(i\in\mathbb N\).
    """
    ring = category.base_ring()
    probe = stage(2)
    assert probe in category, "stage(n) must be a lattice in this category"
    assert probe.module_rank() == cardinal(2), (
        f"stage(n) must have rank n, got stage(2) of rank {probe.module_rank()}"
    )
    module = ring._fresh_free_module_on(_formal_symbols())
    return _lattice_object(category, module, _ColimitGram(module, stage, row_support=row_support))


def _rational_fraction_field(ring):
    r"""Return \(\operatorname{Frac}(R)\) when that field is \(\mathbb{Q}\).

    The signature pair \((p,q)\) is the real signature of a quadratic
    space over \(\mathbb{Q}\).  When \(\operatorname{Frac}(R)\) is a
    number field, that invariant is not this pair; see the GW theory
    of that field.
    """
    field = ring.fraction_field()
    assert _engine_ring(field) is QQ, (
        f"the signature pair (p, q) is the real signature of a quadratic space over QQ; Frac({ring}) is {field}"
    )
    return QQ


def signature_pairs():
    r"""Return \(\mathbf{Card}\times\mathbf{Card}\), where a signature pair lives.

    An index of inertia can be infinite -- \(\mathbb Z^{(\mathbb N)}\) with
    its standard form has \((p,q)=(\aleph_0,0)\) -- so each entry is a
    cardinal and the pair is an object of the product category.
    """

    return Cat().product((Cardinalities(), Cardinalities()))


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


def _signature_pair_of_gram(gram: Tensor):
    r"""Return $(p,q)$ for a Gram presentation.

    At finite rank it is Sylvester's law on the components; at infinite rank
    the pairing rule states it.
    """
    match _gram_rank(gram).is_finite():
        case True:
            return _sylvester(gram)
        case False:
            return gram.signature_pair()


def _discriminant_of_gram(gram: Tensor):
    r"""Return $d_\pm(b)=(-1)^{n(n-1)/2}\det G$."""
    rank = _gram_rank(gram)
    assert rank.is_finite(), "the discriminant is the signed determinant of a finite Gram"
    n = int(rank)
    negative_sign = (n * (n - 1) // 2) % 2 == 1
    determinant = _gram_determinant(gram, gram.base_ring())
    return -determinant if negative_sign else determinant


def _format_disc_latex(disc) -> str:
    r"""Format the discriminant with its prime factorization."""
    if disc in (-1, 0, 1):
        return str(disc)
    # Factorization is the engine's; the owned integer crosses once, here.
    factorization = factor(_engine_element(disc.parent(), disc))
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


def _lattice_latex(lattice, ring_tex: str) -> str:
    r"""The archived lattice display: $L$ with its invariants, then $G_L$.

    The Gram tensor is the form of $L$, not $L$; $G_L$ typesets its components.
    """
    rank = lattice.module_rank()
    gram_latex = str(latex(lattice.gram_tensor()))
    gram_latex = re.sub(r"\b0\b", lambda _match: r"\cdot", gram_latex)
    signature_field = _engine_ring(lattice.base_ring().fraction_field())

    match cardinal(rank).is_finite():
        case False:
            if signature_field is QQ and lattice.signature_pair() is not Unknown:
                _signature = lattice.signature_pair()
                pos, neg = _signature.first(), _signature.second()
                invariants = f"L \\in \\mathrm{{Lattices}}({ring_tex}), \\quad \\mathrm{{rk}}(L) = {latex(rank)}, \\quad \\mathrm{{sig}}(L) = ({latex(pos)}, {neg}) \\\\"
            else:
                invariants = f"L \\in \\mathrm{{Lattices}}({ring_tex}), \\quad \\mathrm{{rk}}(L) = {latex(rank)} \\\\"
        case True:
            if signature_field is QQ:
                _signature = lattice.signature_pair()
                pos, neg = _signature.first(), _signature.second()
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


def _finite_crystallographic_cartan_type(data):
    r"""Return the finite crystallographic Cartan type named by ``data``.

    ``data`` is a Cartan type, its name, or its list form; Sage's
    ``CartanType`` reads all three.
    """
    cartan_type = CartanType(data)
    assert cartan_type.is_finite() and cartan_type.is_crystallographic(), (
        f"{cartan_type} is not a finite crystallographic Cartan type"
    )
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
    r"""Return the negative Gram tensor of a finite crystallographic root lattice.

    If ``A`` is the Cartan matrix and ``D`` its minimal positive integral
    symmetrizer, then ``D A`` is the simple-root Gram matrix: its ``i``-th
    diagonal entry is the square of the ``i``-th root.  The repository uses
    negative-definite root lattices, hence ``-D A``.  In the simply-laced
    case ``D=1`` and this is the existing ``-A`` construction.
    """
    cartan = cartan_type.cartan_matrix()
    symmetrizer = cartan_type.symmetrizer()
    assert symmetrizer is not None, f"{cartan_type} has no integral Cartan symmetrizer"
    indices = tuple(cartan_type.index_set())
    rank = int(cartan_type.rank())
    components = [
        tuple(
            -ring._from_engine_element(symmetrizer[indices[i]] * cartan[i, j])
            for j in range(rank)
        )
        for i in range(rank)
    ]
    gram_tensor = tensor(ring, (), (rank, rank), components)
    assert gram_tensor.tensor_valence() == (NN**2)((0, 2))
    return gram_tensor


def _nested_gram_tensor(data, ring) -> Tensor:
    r"""The type-$(0,2)$ Gram tensor with the given rows of components."""
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
    cartan_type=None,
):
    r"""The lattice with Gram presentation ``gram_tensor``.

    An infinite-rank presentation is a pairing rule, which already names the
    free module it is stated on.  A finite presentation is stated on the free
    module framed by ``module_generators``, by ``names``, or by the formal
    symbols \(e_i\).
    """
    rows, columns = gram_tensor.tensor_shape()
    assert rows == columns, f"a Gram tensor is square, got shape {gram_tensor.tensor_shape()}"
    rank = cardinal(rows)
    match rank.is_finite():
        case False:
            assert module_generators is None, (
                "a pairing rule already determines the generating set"
            )
            return _lattice_on_gram(
                category,
                gram_tensor._module,
                gram_tensor,
                _normalized_lattice_names(names, rank),
                None,
            )
    selected_names = _normalized_lattice_names(names, rank)
    generating_set = _generating_set_for(rank, module_generators, selected_names)
    module = (
        ring.free_module(generating_set)
        if module_generators is None
        else ring._fresh_free_module_on(generating_set)
    )
    root_cartan_type = cartan_type if ring is _own_ring(SageZZ) else None
    return _lattice_on_gram(category, module, gram_tensor, selected_names, root_cartan_type)


def _basis_keys(module):
    r"""The index set of the distinguished basis of ``module``."""
    return module.module_generating_set()


def _basis_position(keys, label):
    r"""Return the owned framing rank of ``label``."""
    return int(keys.ranking_map()(label))


def _owned_free_module(data, ring, module_generators=None, names=None):
    r"""The free module a lattice is stated on, on the generating set of ``data``.

    ``data`` is an owned free module.  Its labels are kept when they were
    chosen; positional labels (``R^n``, ``R^NN``) name nothing, so the
    lattice's generators are then ``module_generators``, ``names``, or the
    formal symbols \(e_i\).
    """
    assert data in FramedFreeModules(ring), (
        f"Lattices({ring}) takes a free module over {ring}, got {data}"
    )
    assert module_generators is None, (
        "equipping a selected free module retains its framing; construct a reframed module first"
    )
    return data


def _identity_lattice(data, ring, names, module_generators, category):
    r"""The Euclidean lattice on the free module ``data``: the identity Gram in its framing."""
    selected_names = _normalized_lattice_names(names, data.module_rank())
    module = _owned_free_module(
        data, ring, module_generators=module_generators, names=selected_names
    )
    return _lattice_object(category, module, _IdentityGram(module), names=selected_names)


def _root_lattice(cartan_type, ring, names, module_generators, category):
    r"""The root lattice of a finite crystallographic Cartan type, in its simple-root framing."""
    return _lattice_from_gram_tensor(
        _root_cartan_gram_tensor(ring, cartan_type),
        ring,
        names,
        module_generators,
        category,
        cartan_type=cartan_type,
    )


def _lattice_with_form(data, form, ring, names, module_generators, category):
    r"""The free module ``data`` equipped with the finite Gram presentation ``form``."""
    assert data in FramedFreeModules(ring), (
        "form= equips a free module given as the first argument"
    )
    assert form.tensor_valence() == (NN**2)((0, 2)), "form= takes a type-(0,2) tensor"
    assert form.base_ring() is ring, (
        f"Lattices({ring}) takes an {ring}-valued form, got a form over {form.base_ring()}"
    )
    assert _gram_rank(form).is_finite(), (
        "form= states a finite Gram on a free module; a pairing rule determines "
        "its own lattice, Lattices(R)(G)"
    )
    selected_names = _normalized_lattice_names(names, data.module_rank())
    module = _owned_free_module(
        data, ring, module_generators=module_generators, names=selected_names
    )
    return _lattice_on_gram(category, module, form, selected_names, None)


def _lattice(
    data,
    basis=None,
    names=None,
    form=None,
    module_generators=None,
    *,
    category,
):
    r"""Return the lattice in ``category`` that ``data`` presents.

    This is the literal ingress of ``Lattices(R)(data)``: it reads which
    presentation ``data`` is and computes the free module and Gram
    presentation :func:`_lattice_object` builds on.

    ``Lattices(R)(R^n)`` is the standard Euclidean lattice: the identity
    Gram tensor on \(R^n\).  ``Lattices(R)(R^{\mathbb N})`` is the colimit
    of those, with \(\langle x,y\rangle=\sum_i x_i y_i\) on finite
    supports.  A pairing Gram on a free module is itself a lattice:
    ``Lattices(R)((R^NN).diagonal_gram({0: -1}))``.  ``form=`` equips a
    given free module with a finite Gram.  ``module_generators=`` is the
    generating set of that free module; when omitted, the generators
    are the formal symbols \(e_i\in\mathrm{SR}\).  A matrix (type
    $(1,1)$) is refused.  Named descriptors (``'U'``, a finite
    crystallographic Cartan type, a Euclidean rank) are Gram tensors.
    """
    assert basis is None, (
        "Lattices(R) does not take a spanning basis; construct the free module and the Gram in this category"
    )
    ring = category.base_ring()
    match form:
        case None:
            pass
        case _:
            return _lattice_with_form(data, form, ring, names, module_generators, category)

    match data:
        case Tensor() if data.tensor_valence() == (NN**2)((0, 2)):
            assert data.base_ring() is ring, (
                f"Lattices({ring}) takes a Gram over {ring}, got base ring {data.base_ring()}"
            )
            return _lattice_from_gram_tensor(data, ring, names, module_generators, category)
        case Tensor() | Matrix():
            raise TypeError("a matrix is a type-(1,1) tensor (a linear map); a Gram is a type-(0,2) tensor")
        case _ if data in FramedFreeModules(ring):
            return _identity_lattice(data, ring, names, module_generators, category)
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
                ring.free_module(int(data)),
                ring,
                names,
                module_generators,
                category,
            )
        case str() | CartanType_abstract():
            return _root_lattice(
                _finite_crystallographic_cartan_type(data),
                ring,
                names,
                module_generators,
                category,
            )
        case list() | tuple() if data:
            match _component_shape(data):
                case (_rows, _columns):
                    return _lattice_from_gram_tensor(
                        _nested_gram_tensor(data, ring),
                        ring,
                        names,
                        module_generators,
                        category,
                    )
                case _:
                    return _root_lattice(
                        _finite_crystallographic_cartan_type(list(data)),
                        ring,
                        names,
                        module_generators,
                        category,
                    )
        case _:
            raise TypeError(f"Lattices({ring}) takes a free {ring}-module, a type-(0,2) Gram, 'U', a finite crystallographic Cartan type, or a nonnegative rank, got {data!r}")
