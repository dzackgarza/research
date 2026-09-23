r"""Lattices.

Sage does not define a category of (quadratic-form) lattices.  Sage's
:func:`~sage.modules.free_quadratic_module_integer_symmetric.IntegralLattice`
constructs a free quadratic module; the order-theoretic category is
:class:`~sage.categories.lattice_posets.LatticePosets`.  This module
owns the missing category, following Sage's category primer
(``super_categories``, ``ParentMethods``, ``ElementMethods``) and the
``Category_over_base_ring`` parameterization.  A lattice is a free
`R`-module with a symmetric form, built through ``FormModules(R)``: it is
the module, all the way down to its underlying set, and holds no second
module.  The classcall is the category over a ring.  Objects are
constructed by calling that category.
"""

from __future__ import annotations

from collections.abc import Hashable, Sequence
from typing import overload

from sage.arith.misc import gcd
from sage.categories.morphism import SetMorphism
from sage.combinat.root_system.root_system import RootSystem
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.misc.repr import repr_lincomb
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent

import dzack_research.preamble.categories.lattice_engines as lattice_engines
from dzack_research.preamble.categories._lattice import (
    _IdentityGram,
    _block_offsets,
    _block_position,
    _colimit_lattice,
    _discriminant_of_gram,
    _generating_set_for,
    _gram_is_even,
    _lattice,
    _lattice_latex,
    _lattice_object,
    _nested_gram_tensor,
    _normalized_lattice_names,
    _orthogonal_sum,
    signature_pair,
    _signature_pair_of_gram,
    _tensor_product_lattice,
)
from dzack_research.preamble.categories._lattice import (
    signature_pairs as signature_pairs,
)
from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import DirectSumObjects
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    MorCategoryConstruction,
    IsoCategoryConstruction,
    MonoCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.definite_lattices import (
    _babai,
    _bkz_reduction,
    _center_density,
    _close_vectors,
    _closest_vector,
    _contact_polytope,
    _covering_radius,
    _gaussian_heuristic,
    _hadamard_ratio,
    _hermite_invariant,
    _hkz_reduction,
    _kissing_number,
    _lll_reduction,
    _minimum,
    _packing_density,
    _packing_radius,
    _root_sublattice,
    _roots,
    _roots_of_square,
    _shortest_vectors,
    _successive_minima,
    _theta_series,
    _vectors_of_square,
    _vectors_of_square_and_divisibility,
    _voronoi_cell,
    _voronoi_facets,
    _voronoi_relevant_vectors,
)
from dzack_research.preamble.categories.group.groups import Groups, OwnedGroups, _engine_group
from dzack_research.preamble.categories.isotropic_orbits import (
    IsotropicFlag,
    _isotropic_flag_locus,
    _isotropic_sublattice_locus,
    _primitive_isotropic_sublattice_locus,
)
from dzack_research.preamble.categories.lattice_morphisms import (
    LatticeEmbeddingMor,
    LatticeMor,
    LatticeIsometryMor,
    _lattice_embedding_mor,
    _lattice_mor,
    _lattice_isometry_mor,
)
from dzack_research.preamble.categories.modules.framed.formed.discriminant_modules import (
    DiscriminantBilinearModules,
    _discriminant_module,
    DiscriminantQuadraticModules,
)
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    BilinearFormModules,
    FormModules,
    FreeFormModules,
)
from dzack_research.preamble.categories.modules.framed.formed.torsion_form_modules import (
    _form_gram_on,
    _relations_among_generators,
    _torsion_form_modules,
    _torsion_form_isometry,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    _module_subobject_constructor_data,
    _span_basis_elements,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    _solve_left_integrally,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    ModuleSubobjectConstruction,
    ModuleSubobjects,
    TensorProductModules,
    _torsion_module_presented_by_matrix,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    NN,
    Sets,
)
from dzack_research.preamble.categories.vector_configurations import VectorConfigurations
from dzack_research.preamble.categories.vector_orbits import (
    VectorPrimitiveExtension,
    _definite_complement_extensions,
    _gluing_route_discriminant_classes,
    _stable_complement_root_reflections,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.tensors.tensor import Tensor, _engine_component_matrix, tensor


def nikulin_invariants(rank, discriminant_length, delta):
    r"""Return \((r,a,\delta)\) as a point of \(\mathbb N^3\)."""

    return (NN**3)((int(rank), int(discriminant_length), int(delta)))


_Rings = OwnedRings()


_INDECOMPOSABLE_NAMES = {}


class LatticeMorCategoryConstruction(MorCategoryConstruction):
    r"""The strict form-preserving Mor categories of lattices."""

    def fixed_category_class(self):

        return LatticeMor


class LatticeMonoCategoryConstruction(MonoCategoryConstruction):
    r"""The form-preserving monomorphisms of lattices."""

    def fixed_category_class(self):

        return LatticeEmbeddingMor


class LatticeIsoCategoryConstruction(IsoCategoryConstruction):
    r"""The isometries of lattices."""

    def fixed_category_class(self):

        return LatticeIsometryMor


def _gram_key(gram):
    rank = int(gram.tensor_shape()[0])
    return tuple(
        tuple(gram[row, column] for column in range(rank))
        for row in range(rank)
    )


def _register_indecomposable_gram(name, gram):
    r"""Register an exact Gram matrix under its indecomposable display name."""
    _INDECOMPOSABLE_NAMES.setdefault(_gram_key(gram), str(name))


def _register_indecomposable(name, lattice):
    r"""Register an indecomposable live lattice by exact Gram equality."""
    if lattice.is_decomposable():
        raise ValueError("only an indecomposable lattice can name one Gram block")
    _register_indecomposable_gram(name, lattice.gram_tensor())


def _indecomposable_name(lattice):
    r"""Return the registered exact or scalar-twist name, if one exists."""
    gram = lattice.gram_tensor().change_ring(_own_ring(SageZZ))
    exact = _INDECOMPOSABLE_NAMES.get(_gram_key(gram))
    if exact is not None:
        return exact
    rank = int(gram.tensor_shape()[0])
    content = gcd(
        gram[row, column]
        for row in range(rank)
        for column in range(rank)
    )
    for scale in (content, -content):
        if scale in (0, 1, -1):
            continue

        rank = gram.tensor_shape()[0]
        integers = gram.base_ring()
        divisor = int(scale)
        untwisted = tensor(
            integers,
            (),
            (rank, rank),
            [[integers(int(gram[i, j]) // divisor) for j in range(rank)] for i in range(rank)],
        )
        name = _INDECOMPOSABLE_NAMES.get(_gram_key(untwisted))
        if name is not None:
            return f"{name}({scale})"
    return None


@cached_function(
    key=lambda module, basis, root_cartan_type=None: (
        id(module),
        basis,
        root_cartan_type,
    )
)
def _lattice_subobject_spanning(module, basis, root_cartan_type=None):
    r"""Return the canonical lattice subobject on a finite span basis.

    The subobject is the lattice on the free module framed by the span basis,
    with the restricted Gram \(b(v_i,v_j)\), built in one construction that
    retains its inclusion into ``module``.  A ``root_cartan_type`` places it
    in ``RootLattices`` with that Cartan type as its datum.
    """
    ring = module.base_ring()
    rank = int(basis.cardinality())
    labels, embedded, lift = _module_subobject_constructor_data(module, basis)
    source_module = ring._fresh_free_module_on(labels)
    match rank:
        case 0:
            gram = _IdentityGram(source_module)
        case _:
            gram = tensor(
                ring,
                (),
                (rank, rank),
                (module.b(basis[i], basis[j]) for i in range(rank) for j in range(rank)),
            )

    def inclusion_factory(source):
        module_inclusion = source.Mono(module)(embedded)
        return source.Emb(module)(module_inclusion)

    extra_categories = ()
    construction_data = {}
    match root_cartan_type:
        case None:
            pass
        case _:
            extra_categories = (RootLattices(),)
            construction_data = {"cartan_type": root_cartan_type}
    return _lattice_object(
        Lattices(ring),
        source_module,
        gram,
        extra_categories=extra_categories,
        construction_data=construction_data,
        subobject_construction=ModuleSubobjectConstruction(
            ambient=module,
            generator_images=embedded,
            lift=lift,
            inclusion_factory=inclusion_factory,
        ),
    )


class LocalGenusSymbol:
    r"""The Conway--Sloane Jordan-block invariants at one finite prime.

    For odd ``p`` each block is ``(m,n,d)``.  At ``p=2`` each block is
    ``(m,n,s,d,o)``.  These integer tuples are the mathematical local-symbol
    data; Sage's ``Genus_Symbol_p_adic_ring`` is reconstructed privately when
    one of its exact algorithms is used.
    """

    def __init__(self, prime, jordan_blocks) -> None:

        integers = _own_ring(SageZZ)
        self._prime = integers(prime)
        if not self._prime.is_prime():
            raise ValueError("a local genus symbol is attached to a prime")
        self._jordan_blocks = tuple(tuple(integers(entry) for entry in block) for block in jordan_blocks)

    def prime(self):
        return self._prime

    def jordan_blocks(self):
        return self._jordan_blocks

    symbol = jordan_blocks

    @cached_method
    def _engine(self):
        from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring

        integers = self.prime().parent()
        return Genus_Symbol_p_adic_ring(
            _engine_element(integers, self.prime()),
            [[_engine_element(integers, entry) for entry in block] for block in self.jordan_blocks()],
        )

    def excess(self):
        integers = self.prime().parent()
        return _owned_engine_element(integers, SageZZ(self._engine().excess()))

    def level(self):
        integers = self.prime().parent()
        return _owned_engine_element(integers, SageZZ(self._engine().level()))

    def norm(self):
        integers = self.prime().parent()
        return _owned_engine_element(integers, SageZZ(self._engine().norm()))

    def number_of_blocks(self):
        return self.prime().parent()(len(self.jordan_blocks()))

    def __eq__(self, other):
        return isinstance(other, LocalGenusSymbol) and self.prime() == other.prime() and self.jordan_blocks() == other.jordan_blocks()

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return f"Local genus at {self.prime()} with Jordan blocks {self.jordan_blocks()}"


class Genus:
    r"""The genus determined by signature and discriminant quadratic form."""

    def __init__(self, signature, discriminant_quadratic_form) -> None:
        r"""``signature`` is the archimedean signature pair, an object of ``signature_pairs()``."""
        self._signature_pair = signature
        self._discriminant_quadratic_form = discriminant_quadratic_form

    def signature_pair(self):
        r"""Return the archimedean signature component ``(t_+,t_-)``."""
        return self._signature_pair

    def discriminant_form(self):
        r"""Return the finite discriminant quadratic form component."""
        return self._discriminant_quadratic_form

    @cached_method
    def _engine_form(self):
        r"""Privately rebuild Sage's finite quadratic form from owned data."""
        from sage.modules.torsion_quadratic_module import TorsionQuadraticForm
        from sage.rings.rational_field import QQ as SageQQ

        form = self.discriminant_form()
        generators = tuple(form.module_generators())
        rationals = _own_ring(SageQQ)
        written = tensor(
            rationals,
            (),
            (len(generators), len(generators)),
            [
                [form.q(left).parent().lift(form.q(left)) if i == j else form.b(left, right).parent().lift(form.b(left, right)) for j, right in enumerate(generators)]
                for i, left in enumerate(generators)
            ],
        )
        engine_form = TorsionQuadraticForm(_engine_component_matrix(written))
        if int(engine_form.cardinality()) != int(form.cardinality()):
            raise ArithmeticError("reconstructing the genus engine changed the discriminant-group cardinality")
        return engine_form

    def _engine_signature_pair(self):

        integers = _own_ring(SageZZ)
        pair = self.signature_pair()
        return (
            _engine_element(integers, integers(int(pair.first()))),
            _engine_element(integers, integers(int(pair.second()))),
        )

    @cached_method
    def _engine(self):
        r"""Return Sage's private global genus realization of these exact data."""
        return self._engine_form().genus(self._engine_signature_pair())

    def exists(self) -> bool:
        r"""Return whether the signature/discriminant-form datum is realizable."""
        return bool(self._engine_form().is_genus(self._engine_signature_pair(), even=True))

    def determinant(self):
        r"""Return the determinant of a representative of this genus."""
        integers = _own_ring(SageZZ)
        return _owned_engine_element(integers, SageZZ(self._engine().determinant()))

    def local_symbol(self, prime):
        r"""Return the owned exact ``ZZ_p`` genus symbol at ``prime``."""
        integers = _own_ring(SageZZ)
        prime = integers(prime)

        backend = self._engine().local_symbol(_engine_element(integers, prime))
        return LocalGenusSymbol(prime, backend.symbol_tuple_list())

    def excess(self, prime):
        return self.local_symbol(prime).excess()

    def level(self, prime):
        return self.local_symbol(prime).level()

    def representative(self):
        r"""Return one owned integral lattice representing this genus."""
        integers = _own_ring(SageZZ)
        representative = self._engine().representative()
        rows = [[_owned_engine_element(integers, entry) for entry in row] for row in representative.rows()]
        return Lattices(integers)(rows)

    def representatives(self):
        r"""Return the owned representatives enumerated by the exact genus computation."""
        integers = _own_ring(SageZZ)
        return finite_ordered_set(
            tuple(
                Lattices(integers)(
                    [
                        [_owned_engine_element(integers, entry) for entry in row]
                        for row in representative.rows()
                    ]
                )
                for representative in self._engine().representatives()
            )
        )

    def class_number(self):
        integers = _own_ring(SageZZ)
        return integers(len(self._engine().representatives()))

    def mass(self):
        r"""Return the Smith--Minkowski--Siegel mass for a definite genus."""
        from sage.rings.rational_field import QQ as SageQQ

        _signature = self.signature_pair()

        positive, negative = _signature.first(), _signature.second()
        if positive != 0 and negative != 0:
            raise ValueError("the finite orthogonal-group mass is defined here for definite genera")
        rationals = _own_ring(SageQQ)
        return _owned_engine_element(rationals, SageQQ(self._engine().mass()))

    def __eq__(self, other):
        if not isinstance(other, Genus):
            return NotImplemented
        if self.signature_pair() != other.signature_pair():
            return False
        return self.discriminant_form().is_isomorphic(other.discriminant_form())

    def __ne__(self, other):
        result = self.__eq__(other)
        return result if result is NotImplemented else not result

    def __repr__(self):
        return f"Genus of even integral lattices with signature {self.signature_pair()} and discriminant order {self.discriminant_form().cardinality()}"


_BLACKBOARD_RING_NAMES = {
    "Z": "ZZ",
    "Q": "QQ",
    "R": "RR",
    "C": "CC",
    "N": "NN",
}


def _ring_notation(ring):
    r"""Session name and latex for a base ring.

    Sage typesets `\ZZ`, `\QQ`, `\RR`, `\CC`, and the rest of that
    family as ``\Bold{Z}``, ``\Bold{Q}``, \ldots .  The session names
    are ``ZZ``, ``QQ``, ``RR``, ``CC``; the latex is ``\mathbb{Z}``
    and so on, not Sage's ``\Bold``.
    """
    raw = str(latex(ring))
    prefix = r"\Bold{"
    if raw.startswith(prefix) and raw.endswith("}") and raw.count("{") == 1:
        letter = raw[len(prefix) : -1]
        name = _BLACKBOARD_RING_NAMES.get(letter)
        if name is not None:
            return name, rf"\mathbb{{{letter}}}"
    return str(ring), raw


class Lattices(OwnedCategoryOverBaseRing):
    r"""
    The category of lattices over a base ring, and the constructor for
    its objects.

    Sage's ``IntegralLattice`` factory constructs finite nondegenerate
    integral forms but does not provide the mathematical category used here.
    ``Lattices(R)`` owns the broader category of free `R`-modules with an
    `R`-valued symmetric form; finite rank and nondegeneracy are refinements,
    not hidden constructor assumptions.      Named descriptors (``U``, a finite
    simply-laced Cartan type, a Euclidean rank) are owned Gram tensors.

    Sage's meet/join lattices are :class:`LatticePosets`, a different
    mathematical object.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.lattices import Lattices
        sage: Lattices(ZZ)
        Lattices(ZZ)
        sage: Lattices(ZZ).super_categories()
        [Category of framed free modules,
         Category of modules with a symmetric bilinear form,
         Category of formed modules]

        sage: C = Lattices(ZZ)
        sage: L = C("U")
        sage: L
        Integral lattice of rank 2 and signature (1, 1)
        sage: L in C
        True
        sage: C("A2")
        Integral lattice of rank 2 and signature (0, 2)
        sage: latex(L)
        \begin{gathered}
        L \in \mathrm{Lattices}(\mathbb{Z}), \quad \mathrm{rk}(L) = 2, \quad \mathrm{sig}(L) = (1, 1), \quad \mathrm{disc}(L) = 1 \\
        L = U \\
        G_L = \left(\begin{array}{rr}
        \cdot & 1 \\
        1 & \cdot
        \end{array}\right) \\
        \end{gathered}
        sage: latex(Lattices(ZZ))
        \mathrm{Lattices}(\mathbb{Z}) \in \mathrm{Cat}
    """

    @staticmethod
    def __classcall_private__(cls, *args):
        r"""Return the category of lattices over a ring.

        This is not a lattice constructor.  An object is
        ``Lattices(R)(data)``.
        """
        if len(args) != 1:
            raise TypeError("Lattices(R) takes a ring R; construct an object as Lattices(R)(data)")
        ring = _own_ring(args[0])
        assert ring in _Rings, "Lattices(R) takes a ring R; construct an object as Lattices(R)(data)"
        from dzack_research.preamble.categories.modules.pure.modules import _is_group_algebra

        if cls is Lattices and _is_group_algebra(ring):
            # Lattices(R[G]): lattices over R with a form-preserving G-action.
            from dzack_research.preamble.categories.modules.group_modules.group_lattices import (
                LatticesOverGroupAlgebra,
            )

            return LatticesOverGroupAlgebra(ring)
        return super().__classcall__(cls, ring)

    @cached_method
    def twist_functor(self, scale):
        r"""Return the integral-lattice endofunctor ``L |-> L(scale)``."""
        if _engine_ring(self.base_ring()) is not SageZZ:
            raise TypeError("the represented lattice twist functor is integral")
        from dzack_research.preamble.categories.functors.twist import TwistFunctor

        return TwistFunctor(scale)

    @overload  # type: ignore[override]  # the stub promises a SageObject; the object type of this category is its provider class
    def __call__(self, data: str | Sequence[Sequence[object]], *args: object, **options: object) -> Lattices.ParentMethods: ...

    @overload
    def __call__(self, data: object, *args: object, **options: object) -> Lattices.ParentMethods: ...

    def __call__(self, data: object, *args: object, **options: object) -> Lattices.ParentMethods:
        r"""Return the lattice that ``data`` presents; a lattice in this category is returned as is.

        A named form or a Gram given by rows has finite rank.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: L = Lattices(ZZ)("U")
            sage: Lattices(ZZ)(L) is L
            True
        """
        lattice = super().__call__(data, *args, **options)
        assert lattice in self, f"{lattice!r} is not a lattice in {self}"
        return lattice

    def _call_(  # type: ignore[override]  # the stub promises a SageObject; the object type of this category is its provider class
        self,
        data: object,
        basis: None = None,
        names: str | Sequence[str] | None = None,
        form: Tensor | None = None,
        module_generators: Sequence[Hashable] | Parent | None = None,
    ) -> Lattices.ParentMethods:
        r"""Construct a lattice in this category.

        This is Sage's category constructor: ``C(x)`` for ``C`` a
        category.  ``Lattices(ZZ)("U")`` is the hyperbolic plane over
        `\ZZ`.  ``Lattices(R)(R^n)`` is the standard Euclidean lattice
        of rank `n`; ``Lattices(R)(R^{\mathbb N})`` is its colimit.
        A pairing Gram is a lattice: ``C((R^NN).diagonal_gram({0: -1}))``.
        ``module_generators=`` is the generating set of the underlying
        free module; when omitted, the generators are the formal symbols
        \(e_i\in\mathrm{SR}\).  The result is an owned lattice.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: Lattices(ZZ)("U")
            Integral lattice of rank 2 and signature (1, 1)
            sage: I2 = Lattices(ZZ)(ZZ^2)
            sage: I2
            Integral lattice of rank 2 and signature (2, 0)
            sage: I2.gram_tensor().tensor_valence()
            (0, 2)
            sage: e = I2.basis_vector(0)
            sage: e
            e_0
            sage: I2.framing_coefficients(e)
            {e_0: 1}
            sage: e*e, e.b(I2.basis_vector(1))
            (1, 0)
            sage: I2((1, 0))
            e_0
            sage: Linf = Lattices(ZZ)(ZZ^NN)
            sage: Linf
            Integral lattice of rank +Infinity and signature (+Infinity, 0)
            sage: Linf((1, 0, 0, 1))
            e_0 + e_3
            sage: Lattices(ZZ)((ZZ^NN).diagonal_gram({0: -1}))
            Integral lattice of rank +Infinity and signature (+Infinity, 1)
        """

        return _lattice(
            data,
            basis,
            names=names,
            form=form,
            module_generators=module_generators,
            category=self,
        )

    def _specialize_existing_lattice(
        self,
        lattice,
        *,
        extra_categories=(),
        construction_data=(),
        unformed_module=None,
    ):
        r"""Build a lattice carrying added structure on the data of ``lattice``.

        Protected construction contract of ``Lattices(R)`` (``OWN-05``).  Its
        callers are the entries of categories whose structure is stated on an
        existing lattice and which have no Gram presentation of their own to
        supply, such as ``Lattices(R[G])(L, action)``.  It takes the lattice,
        the categories the structure adds, the data those categories declare
        (a mapping, or a family of name-value pairs), and the module the
        structure is stated on: ``lattice`` itself when the structure is
        stated on the lattice, as for a group action, and otherwise the
        module ``lattice`` is built on.

        It computes the datum of the one lattice construction and calls it:
        the Gram presentation of ``lattice`` stated on that module, together
        with the structure ``lattice`` already carries by its placement -- its
        subobject inclusion, its biproduct or tensor-product factors and its
        root framing.  The result is a new lattice on the same data, and it
        answers ``unformed_module()`` with the module the structure was
        stated on.
        """
        ring = self.base_ring()
        assert lattice in self, f"a specialization of {self} is built on a lattice of {self}"
        stated_on = lattice.unformed_module() if unformed_module is None else unformed_module
        carried_categories = []
        carried_data = {}
        match lattice in BiproductLattices(ring):
            case True:
                carried_categories.append(BiproductLattices(ring))
                carried_data["biproduct_factors"] = lattice.biproduct_factors()
        match lattice in TensorProductModules(ring):
            case True:
                carried_categories.append(TensorProductModules(ring))
                carried_data["tensor_factors"] = lattice.tensor_factors()
        match lattice in RootLattices():
            case True:
                carried_categories.append(RootLattices())
                carried_data["cartan_type"] = lattice.cartan_type()
        match lattice in NoncrystallographicRootLattices(ring):
            case True:
                carried_categories.append(NoncrystallographicRootLattices(ring))
                carried_data["coxeter_type"] = lattice.coxeter_type()
        match lattice in ModuleSubobjects(ring):
            case True:
                subobject_construction = lattice.module_subobject_construction()
            case False:
                subobject_construction = None
        carried_data.update(dict(construction_data))
        return _lattice_object(
            self,
            stated_on,
            lattice.gram_tensor(),
            extra_categories=(*carried_categories, *tuple(extra_categories)),
            construction_data=carried_data,
            subobject_construction=subobject_construction,
        )

    def colimit(self, stage, *, row_support=None):
        r"""Return \(\operatorname{colim}_n \mathrm{stage}(n)\) along \(x\mapsto(x,0)\).

        ``stage(n)`` is a rank-\(n\) lattice in this category.  The
        resulting form is evaluated in a finite stage containing the supports
        of the vectors being paired.  The stage callback alone does not prove
        an infinite signature, nondegeneracy or unimodularity; those predicates
        remain undecided unless the represented Gram rule supplies the missing
        global information.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: C = Lattices(ZZ)
            sage: L = C.colimit(lambda n: C(ZZ^n))
            sage: L.basis_vector(3) * L.basis_vector(3)
            1
        """

        return _colimit_lattice(stage, category=self, row_support=row_support)

    def orthogonal_direct_sum_bifunctor(self):
        r"""Return the orthogonal direct-sum bifunctor on lattices over this ring."""
        from dzack_research.preamble.categories.functors.linear_constructions import (
            _orthogonal_direct_sum_bifunctor,
        )

        return _orthogonal_direct_sum_bifunctor(self.base_ring())

    def an_object(self):
        r"""The hyperbolic plane U."""
        return self("U")

    @staticmethod
    def root_lattice(kind, rank, names=None):
        r"""Return the exact negative-definite root lattice of the selected finite type."""
        kind = str(kind)
        rank = int(rank)
        if kind == "H":
            if rank not in (3, 4):
                raise ValueError("the finite H root systems are H3 and H4")
            from dzack_research.preamble.categories.rings.number_fields import QuadraticField

            field = QuadraticField(5, "sqrt5")
            order = field.ring_of_integers()
            phi = order((field.one() + field.primitive_element()) / field(2))
            bonds = (phi, *([order.one()] * (rank - 2)))
            gram = _nested_gram_tensor(
                tuple(
                    tuple(
                        -order(2)
                        if row == column
                        else bonds[min(row, column)]
                        if abs(row - column) == 1
                        else order.zero()
                        for column in range(rank)
                    )
                    for row in range(rank)
                ),
                order,
            )
            selected_names = _normalized_lattice_names(names, cardinal(rank))
            module = order.free_module(
                _generating_set_for(cardinal(rank), None, selected_names)
            )
            return _lattice_object(
                Lattices(order),
                module,
                gram,
                names=selected_names,
                extra_categories=(NoncrystallographicRootLattices(order),),
                construction_data={"coxeter_type": (kind, rank)},
            )
        if kind not in {"A", "B", "C", "D", "E", "F", "G"}:
            raise ValueError(f"unknown finite root family {kind!r}")
        return Lattices(_own_ring(SageZZ))(f"{kind}{rank}", names=names)

    @staticmethod
    def IPQ(positive, negative):
        r"""Return the odd unimodular lattice ``I_(positive,negative)``."""
        positive = int(positive)
        negative = int(negative)
        if positive < 0 or negative < 0 or positive + negative == 0:
            raise ValueError("I_(p,q) requires p,q >= 0 and positive total rank")
        diagonal = [1] * positive + [-1] * negative
        gram = [
            [entry if row == column else 0 for column, entry in enumerate(diagonal)]
            for row in range(len(diagonal))
        ]
        return Lattices(_own_ring(SageZZ))(gram)

    @staticmethod
    def IIPQ(positive, negative):
        r"""Return the indefinite even unimodular lattice ``II_(positive,negative)``.

        Such a lattice exists exactly when both inertia indices are positive and
        ``positive-negative`` is divisible by eight.  With the repository's
        negative-definite ``E8`` convention it is the orthogonal sum of
        hyperbolic planes and the required signed ``E8`` blocks.
        """
        positive = int(positive)
        negative = int(negative)
        if positive < 1 or negative < 1:
            raise ValueError("II_(p,q) here denotes an indefinite even unimodular lattice")
        if (positive - negative) % 8:
            raise ValueError("an even unimodular lattice has signature divisible by eight")
        integers = _own_ring(SageZZ)
        category = Lattices(integers)
        summands = [category("U") for _ in range(min(positive, negative))]
        if negative > positive:
            summands.extend(category("E8") for _ in range((negative - positive) // 8))
        elif positive > negative:
            positive_e8 = category("E8").twist(-1)
            summands.extend(positive_e8 for _ in range((positive - negative) // 8))
        return _orthogonal_sum(tuple(summands))

    @staticmethod
    def rank_one_negative(scale):
        r"""Return the rank-one lattice ``<-2 scale>``."""
        integers = _own_ring(SageZZ)
        return Lattices(integers)(1).twist(integers(-2 * int(scale)))

    @staticmethod
    def LK3_2d(degree):
        r"""Return ``<-2d> + U^2 + E8^2``, the degree-``2d`` K3 complement lattice."""
        degree = int(degree)
        if degree < 1:
            raise ValueError("the polarized K3 degree parameter d is positive")
        integers = _own_ring(SageZZ)
        category = Lattices(integers)
        return _orthogonal_sum(
            (
                Lattices.rank_one_negative(degree),
                category("U"),
                category("U"),
                category("E8"),
                category("E8"),
            )
        )

    @staticmethod
    def hyperkaehler_lattice(deformation_type, n=2):
        r"""Return the Beauville--Bogomolov--Fujiki lattice of a standard deformation type.

        ``K3`` means ``K3^[n]`` and ``Kum`` the generalized Kummer series;
        ``OG6`` and ``OG10`` are the two O'Grady types.  The formulas are the
        standard integral BBF lattices and use the existing owned ``U``, ``E8``
        and ``A2`` constructors rather than a second lattice representation.
        """
        deformation_type = str(deformation_type)
        n = int(n)
        if deformation_type not in {"K3", "Kum", "OG6", "OG10"}:
            raise ValueError(f"unknown hyperkähler deformation type {deformation_type!r}")
        integers = _own_ring(SageZZ)
        category = Lattices(integers)
        hyperbolic = (category("U"), category("U"), category("U"))
        if deformation_type == "K3":
            if n < 2:
                raise ValueError("the K3^[n] series here requires n >= 2")
            return _orthogonal_sum(
                (*hyperbolic, category("E8"), category("E8"), category(1).twist(2 - 2 * n))
            )
        if deformation_type == "Kum":
            if n < 2:
                raise ValueError("the generalized Kummer series here requires n >= 2")
            return _orthogonal_sum((*hyperbolic, category(1).twist(-2 - 2 * n)))
        if deformation_type == "OG6":
            minus_two = category(1).twist(-2)
            return _orthogonal_sum((*hyperbolic, minus_two, minus_two))
        return _orthogonal_sum(
            (*hyperbolic, category("E8"), category("E8"), category("A2"))
        )

    @staticmethod
    @cached_function
    def leech_lattice():
        r"""Return the negative-definite Leech lattice through Hecke's maintained construction."""
        integers = _own_ring(SageZZ)
        positive = Lattices(integers)(lattice_engines._leech_gram_rows())
        return positive.twist(-integers.one())

    @cached_method
    def super_categories(self):
        r"""
        Return the immediate super categories of ``self``.

        A lattice is a free `R`-module with a symmetric `R`-valued form.
        Immediate supers only, as required by the Sage category primer.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: Lattices(ZZ).super_categories()
            [Category of free form modules,
             Category of modules with a symmetric bilinear form]
        """

        return [
            FreeFormModules(self.base_ring()),
            BilinearFormModules(self.base_ring()).Symmetric(),
        ]

    _MorCategory = LatticeMorCategoryConstruction
    _MonoCategory = LatticeMonoCategoryConstruction
    _IsoCategory = LatticeIsoCategoryConstruction

    class SubcategoryMethods:
        def tensor_product(self, factors):
            r"""Return the tensor product lattice with the product pairing."""
            return _tensor_product_lattice(factors)

        def _categorical_tensor_product(self, left, right):
            return self.tensor_product((left, right))

        def biproduct(self, summands):
            r"""Return $\bigoplus_{i \in I} L_i$, the orthogonal sum of a family.

            A lattice is a module with a form, so the biproduct of lattices is
            the biproduct of the underlying modules carrying the orthogonal
            sum of the forms.  It is taken over the index set: the summand at
            each index has its own block of coordinates, so three summands are
            three and not a two-summand sum whose first summand is a sum.

            ``L + M`` is the two-index case, and ``L ** n`` the constant
            family over an $n$-element index set.
            """
            return _orthogonal_sum(summands)

        def _categorical_biproduct(self, left, right):
            return self.biproduct((left, right))

        def product(self, summands):
            r"""Return $\prod_{i \in I} L_i$, which over a finite index set is the biproduct."""
            return self.biproduct(summands)

        def coproduct(self, summands):
            r"""Return $\coprod_{i \in I} L_i$, which over a finite index set is the biproduct."""
            return self.biproduct(summands)

    def _repr_(self):
        r"""Return ``Lattices(R)`` with the session name of the base ring.

        This is the cell's text/plain output.  The notebook typesets
        :meth:`_latex_` when it can; both must say ``Lattices(R)``, not
        Sage's "Category of lattices over Integer Ring".

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: Lattices(ZZ)
            Lattices(ZZ)
            sage: Lattices(QQ)
            Lattices(QQ)
        """
        name, _tex = _ring_notation(self.base_ring())
        return f"Lattices({name})"

    def _latex_(self):
        r"""Return ``Lattices(R) \in Cat``, with blackboard bold for `\ZZ`, `\QQ`, `\RR`, `\CC`.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: latex(Lattices(ZZ))
            \mathrm{Lattices}(\mathbb{Z}) \in \mathrm{Cat}
            sage: latex(Lattices(QQ))
            \mathrm{Lattices}(\mathbb{Q}) \in \mathrm{Cat}
        """
        _name, tex = _ring_notation(self.base_ring())
        return rf"\mathrm{{Lattices}}({tex}) \in \mathrm{{Cat}}"

    class ParentMethods:
        r"""Operations generic to every lattice.

        The datum this level introduces is the Gram presentation of the form
        in the framing of the module the form is stated on.  The form itself
        and that module are the datum of ``FormModules(R)``, which the
        construction computes from the presentation.
        """

        def __init__(self, gram_tensor, **rest) -> None:
            self._preamble_gram_tensor = gram_tensor
            super().__init__(**rest)

        def _first_ngens(self, n):
            r"""Return the first ``n`` module generators, for Sage's ``L.<e,f> =`` naming syntax."""
            labels = self.module_generating_set()
            return tuple(self.module_generator(labels[position]) for position in range(int(n)))

        def lattice_category(self):
            r"""Return the base-ring lattice category owning this object."""
            return Lattices(self.base_ring())

        def subobject_on(self, module_generating_set):
            r"""Return the span with the restricted lattice form."""

            basis = _span_basis_elements(self, module_generating_set)
            return _lattice_subobject_spanning(self, basis)

        def sublattice_from(self, vectors, *, saturate=False):
            r"""Return the lattice subobject spanned by ``vectors``.

            When ``saturate`` is true, first take the primitive closure of the
            underlying module inclusion and then rebuild the restricted form on
            that saturated embedded basis.  Thus the result is still a lattice
            subobject of ``self`` rather than a bare saturated module.
            """
            span = self.subobject_on(vectors)
            if not saturate:
                return span
            saturated_module = span.inclusion().saturation()
            embedded_basis = tuple(saturated_module.inclusion()(generator) for generator in saturated_module.module_generators())
            return self.subobject_on(embedded_basis)

        def primitive_sublattice_from(self, vectors):
            r"""Return the saturated lattice subobject generated by ``vectors``."""
            return self.sublattice_from(vectors, saturate=True)

        def ambient_lattice(self):
            r"""Return the ambient lattice of a represented lattice subobject."""
            if self not in ModuleSubobjects(self.base_ring()):
                raise TypeError("ambient_lattice() requires a represented lattice subobject")
            return self.inclusion().codomain()

        def lattice_basis(self):
            r"""Return the selected lattice basis as actual lattice elements."""
            return self.module_generators()

        def rank(self):
            r"""Return the lattice rank."""
            return self.module_rank()

        def saturation(self):
            r"""Return the primitive closure as a lattice subobject of the same ambient lattice."""
            if self not in ModuleSubobjects(self.base_ring()):
                raise TypeError("saturation() requires a represented lattice subobject")
            ambient = self.inclusion().codomain()
            saturated_module = self.inclusion().saturation()
            embedded_basis = tuple(saturated_module.inclusion()(generator) for generator in saturated_module.module_generators())
            return ambient.subobject_on(embedded_basis)

        def orthogonal_complement(self, sublattice=None):
            r"""Return an orthogonal lattice subobject.

            ``L.orthogonal_complement(I)`` computes ``I^perp`` in ``L``.  On a
            lattice that is itself represented as a subobject, omitting ``I``
            retains the existing ``I.orthogonal_complement()`` convention.
            """
            if sublattice is None:
                if self not in ModuleSubobjects(self.base_ring()):
                    raise TypeError("orthogonal_complement() without an argument requires a represented lattice subobject")
                return self.inclusion().orthogonal_complement()
            if sublattice not in ModuleSubobjects(self.base_ring()):
                raise TypeError("the orthogonal complement is taken from a represented lattice subobject")
            inclusion = sublattice.inclusion()
            if inclusion.codomain() is not self:
                raise ValueError("the selected sublattice has the wrong ambient lattice")
            return inclusion.orthogonal_complement()

        def perp(self, sublattice=None):
            r"""Synonym for :meth:`orthogonal_complement`."""
            return self.orthogonal_complement(sublattice)

        def _root_subobject_on(self, module_generating_set, cartan_type):
            r"""Return the selected root sublattice with Cartan data at construction."""
            basis = _span_basis_elements(self, module_generating_set)
            return _lattice_subobject_spanning(
                self,
                basis,
                root_cartan_type=cartan_type,
            )

        def Mor(self, codomain, category=None):
            lattices = Lattices(self.base_ring())
            if category is None or category.is_subcategory(lattices):
                return _lattice_mor(self, codomain)
            from sage.categories.homset import Hom as SageHom

            return SageHom(self, codomain, category)

        def _Hom_(self, codomain, category=None):

            lattices = Lattices(self.base_ring())
            if codomain in lattices and (category is None or category.is_subcategory(lattices)):
                return _lattice_mor(self, codomain)
            return super()._Hom_(codomain, category)

        def Emb(self, codomain):
            r"""Return the set of form-preserving embeddings into ``codomain``."""

            return _lattice_embedding_mor(self, codomain)

        def Isom(self, codomain):
            r"""Return the set of isometries to ``codomain``."""

            return _lattice_isometry_mor(self, codomain)

        def Aut(self):
            r"""Return ``Isom(L,L)``, the orthogonal automorphism Mor."""
            return self.Isom(self)

        def orthogonal_group(self):
            r"""Return ``O(L,b)=Aut(L,b)`` as the owned isometry group."""
            return self.Aut()

        O = orthogonal_group  # noqa: E741 - standard mathematical notation O(L)

        def bilinear_orthogonal_group(self):
            r"""Return ``O(L,b)``; explicit name for the lattice pairing."""
            return self.Aut()

        def quadratic_orthogonal_group(self):
            r"""Return ``O(L,q)`` for ``q(x)=b(x,x)``.

            On a free integral lattice, preserving the symmetric bilinear form
            and preserving its diagonal quadratic form are equivalent, so this
            is the same represented group as ``O(L,b)``.
            """
            return self.Aut()

        @cached_method
        def discriminant_representation(self):
            r"""Return ``rho_L:O(L)->O(A_L)`` by functoriality of discriminants."""
            source = self.Aut()
            target = self.discriminant_group().orthogonal_group()
            return SetMorphism(
                source.Mor(target),
                lambda isometry: isometry.discriminant_morphism(),
            )

        @cached_method
        def discriminant_image(self):
            r"""Return the computed image of ``rho_L`` when ``O(L)`` generators are known."""
            return self.Aut().discriminant_image()

        @cached_method
        def discriminant_representation_is_surjective(self) -> bool:
            r"""Return whether the computed discriminant image equals ``O(A_L)``."""
            image = self.discriminant_image()
            return image.cardinality() == self.discriminant_group().orthogonal_group().cardinality()

        @cached_method
        def stable_orthogonal_group(self):
            r"""Return ``ker(rho_L)`` as the stable orthogonal subgroup."""
            target = self.discriminant_group().orthogonal_group()
            trivial = target.subgroup_on(())
            return self.Aut().discriminant_preimage(trivial)

        def O_plus(self):
            r"""Return the stable orthogonal group ``ker(O(L) -> O(A_L))``.

            The project vocabulary uses ``O_plus`` for the stable subgroup;
            positive-cone preservation is exposed separately by
            :meth:`O_component`.
            """
            return self.stable_orthogonal_group()

        @cached_method
        def special_orthogonal_group(self):
            r"""Return ``SO(L)=ker(det:O(L)->{+-1})`` as a predicate subgroup."""

            return self.Aut().predicate_subgroup(lambda automorphism: automorphism.determinant() == 1, "det(g)=1", character_data={"determinant_kernel": True})

        SO = special_orthogonal_group

        def spinor_kernel_subgroup(self):
            r"""Return the kernel of the real spinor-norm sign on ``O(L)``."""

            return self.Aut().predicate_subgroup(lambda automorphism: automorphism.real_spinor_norm_sign() == 1, "real spinor norm(g)=+1", character_data={"spinor_kernel": True})

        @cached_method
        def component_character(self):
            r"""Return \(\chi_\Omega\colon O(L)\to C_2\), the character of the positive cone.

            In signature \((1,n)\) the cone \(\{v: b(v,v)>0\}\) has two
            components, and an isometry either preserves each of them or
            exchanges the two.  That assignment is a group morphism to the
            cyclic group of order two, and :meth:`positive_cone_subgroup` is
            its kernel.
            """
            _signature = self.signature_pair()
            positive, negative = _signature.first(), _signature.second()
            integers = positive.parent()
            if positive != integers.one() or negative < integers.one():
                raise ValueError(f"the component character is defined in signature (1,n); got {(positive, negative)}")

            target = OwnedGroups().C(2)
            exchange = target.group_generators()[0]
            return SetMorphism(
                self.Aut().Mor(target),
                lambda isometry: target.one() if isometry.preserves_positive_cone() else exchange,
            )

        def positive_cone_subgroup(self):
            r"""Return the positive-cone-preserving subgroup in signature ``(1,n)``."""
            _signature = self.signature_pair()
            positive, negative = _signature.first(), _signature.second()
            integers = positive.parent()
            if positive != integers.one() or negative < integers.one():
                raise ValueError(f"positive_cone_subgroup requires signature (1,n); got {(positive, negative)}")

            return self.Aut().predicate_subgroup(lambda automorphism: automorphism.preserves_positive_cone(), "g preserves the positive cone")

        def O_component(self):
            r"""Return the subgroup preserving the selected positive-cone component."""
            return self.positive_cone_subgroup()

        @cached_method
        def decomposition(self):
            r"""Return the represented direct-sum decomposition, or ``None`` when this lattice was not built as one.

            A lattice built as an orthogonal sum is an object of
            ``BiproductLattices(R)``, whose datum is its family of summands.
            """
            match self in BiproductLattices(self.base_ring()):
                case True:
                    return DirectSumObjects(self.lattice_category()).verify_decomposition(
                        self, self.biproduct_factors()
                    )
                case False:
                    return None

        def is_decomposable(self):
            return self.decomposition() is not None

        def indecomposable_name(self):
            return _indecomposable_name(self)

        def indecomposable_summands(self):
            r"""Return the family of indecomposable summands, in order.

            A summand may itself be an orthogonal sum -- as every summand of
            ``L + M + N`` is, ``+`` being binary -- so this descends through
            the represented decompositions until every summand is
            indecomposable.
            """

            if self.decomposition() is None:
                return finite_family((self,), name="Indecomposable summands")
            summands = []
            for factor in self.biproduct_factors():
                summands.extend(factor.indecomposable_summands())
            return finite_family(summands, name="Indecomposable summands")

        def decomposition_names(self):
            r"""Return the registered name of each indecomposable summand."""
            return self.indecomposable_summands().map(
                lambda summand: summand.indecomposable_name(),
                name="Decomposition names",
            )

        def is_isometric(self, other):
            r"""Return whether ``self`` and ``other`` are isometric when decidable.

            The live isometry Mor preserves ``Unknown`` outside implemented
            exact regimes instead of treating matching coarse invariants as a
            proof.
            """
            empty = self.Isom(other).is_empty()
            if empty is Unknown:
                return Unknown
            return not empty

        def isometry_to(self, other):
            r"""Return an explicit isometry ``self -> other`` when one is constructible.

            A proved empty isometry Mor returns ``None``.  An undecided
            Mor, or a theorem-backed nonempty Mor whose current exact
            machinery does not exhibit a witness, retains that distinction by
            raising from :meth:`Isom(...).an_element` rather than turning it
            into a false negative.
            """
            mor = self.Isom(other)
            empty = mor.is_empty()
            match empty:
                case True:
                    return None
            assert empty is not Unknown, (
                "the isometry Mor is not decided by the available exact classifiers"
            )
            return mor.an_element()

        def is_isometric_to(self, other):
            r"""Return the verified boolean isometry decision.

            Unlike :meth:`is_isometric`, this semantic spelling is strictly
            boolean: an unresolved exact-classification case raises instead of
            exposing ``Unknown`` as though it were a truth value.
            """
            decision = self.is_isometric(other)
            assert decision is not Unknown, (
                "the isometry question is not decided by the available exact classifiers"
            )
            return bool(decision)

        def with_isometry(self, isometry):
            r"""Return the infinite-cyclic action on this lattice generated by ``isometry``."""
            from dzack_research.preamble.categories.lattice_centralizers import (
                _equivariant_lattice,
            )

            return _equivariant_lattice(self, isometry)

        def similarity_mor(self, other, scale):
            r"""Return similarities of scale ``scale`` as ``Isom(L(scale),other)``."""
            return self.twist(scale).Isom(other)

        def is_similar(self, other, scale):
            r"""Return whether a similarity of the stated scale exists."""
            return self.twist(scale).is_isometric(other)

        def similarity(self, scale, images=None, codomain=None):
            r"""Return an explicit similarity as an isometry from ``L(scale)``.

            A scale-``a`` similarity ``sigma:L->M`` satisfies
            ``b_M(sigma x,sigma y)=a*b_L(x,y)``.  Hence its owned
            form-preserving arrow is exactly an isometry ``L(a)->M``.  When
            ``images`` is omitted, return the distinguished isometry supplied
            by the represented exact isometry Mor.
            """
            target = self if codomain is None else codomain
            mor = self.similarity_mor(target, scale)
            if images is None:
                return mor.an_element()
            return mor(images)

        def identity_morphism(self):
            r"""Return ``id_L`` in the lattice endomorphism Mor.

            The morphism is a callable on generators, not an enumerated
            image of every \(e_i\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Iinf = Lattices(ZZ)(ZZ^NN)
                sage: f = Iinf.identity_morphism()
                sage: f(Iinf.basis_vector(7))
                e_7
            """
            return self.Aut().identity()

        def gram_tensor(self):
            r"""Return the Gram tensor of the form: type $(0,2)$, not a matrix.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: I2.gram_tensor()
                I_2 ∈ ((ZZ^2)*)^{⊗2}
                sage: latex(I2.gram_tensor())
                I_{2}
                sage: latex(Lattices(ZZ)(ZZ^NN).gram_tensor())
                I_{\infty}
                sage: A2 = Lattices(ZZ)("A2")
                sage: latex(A2.gram_tensor())
                \left(\begin{array}{rr}
                -2 & 1 \\
                1 & -2
                \end{array}\right)
                sage: I2.gram_tensor().parent()
                ((ZZ^2)*)^{⊗2}
                sage: Lattices(ZZ)(ZZ^NN).gram_tensor()
                I_∞ ∈ (ZZ^NN ⊗ ZZ^NN)*
            """
            return self._preamble_gram_tensor

        def gram_matrix(self, basis=None):
            r"""Return the finite coordinate matrix of the selected form.

            With no ``basis`` this is the matrix of
            :meth:`algebraic_correlation_morphism` in the selected finite
            framing and its dual.  An infinite algebraic dual has no
            finite-support dual framing, so an infinite lattice has no
            default Gram *matrix*; its Gram tensor remains the form.  Passing
            finitely many vectors explicitly returns their finite pairing
            matrix.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U").gram_matrix().determinant()
                -1
                sage: Lattices(ZZ)("A2").gram_matrix().determinant()
                3
            """
            if basis is not None:
                selected = tuple(basis)
                for vector in selected:
                    if vector.parent() is not self:
                        raise ValueError("a Gram matrix basis consists of vectors of this lattice")
                size = len(selected)
                return self.base_ring().matrix_space(size, size).from_rows(tuple(tuple(self.b(left, right) for right in selected) for left in selected))
            assert self.module_rank().is_finite(), (
                "the default Gram matrix requires finite rank; use gram_tensor() for an infinite form or pass a finite list of vectors"
            )
            correlation = self.algebraic_correlation_morphism()
            linear = correlation.domain().module_category().Mor(
                correlation.domain(), correlation.codomain()
            )(correlation)
            return linear.matrix()

        def basis_vector(self, position):
            r"""Return the selected lattice basis vector at integer ``position``.

            Positional basis access is a lattice convenience distinct from the
            generic framing evaluation ``module_generator(label)``: it reads the
            label at ``position`` in the framing's enumeration.
            """
            labels = self.module_generating_set()
            return self.module_generator(labels[int(position)])

        def signature_pair(self):
            r"""Return $(p,q)$: the positive and negative indices of inertia.

            This is the real signature of the quadratic space over
            \(\mathbb{Q}\) obtained by extending scalars along
            \(\operatorname{Frac}(R)\) when that field is \(\mathbb{Q}\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U").signature_pair()
                (1, 1)
                sage: Lattices(ZZ)(ZZ^NN).signature_pair()
                (+Infinity, 0)
            """

            signature = _signature_pair_of_gram(self.gram_tensor())
            assert signature is not Unknown, (
                "the exact signature of this infinite lattice is not determined by its represented Gram rule"
            )
            return signature

        def signature(self):
            r"""Return the inertia pair ``(p,q)`` of the lattice form."""
            return self.signature_pair()

        def discriminant(self):
            r"""Return $d_\pm(b)=(-1)^{n(n-1)/2}\det G$, the signed determinant.

            An invariant of $L$, not the framing-dependent $\det G$.
            Transcribed from the archived integral-lattice discriminant
            (Lam, *Introduction to Quadratic Forms over Fields*, I.2).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U").discriminant()
                1
                sage: Lattices(ZZ)(ZZ^2).discriminant()
                -1
            """

            return _discriminant_of_gram(self.gram_tensor())

        def determinant(self):
            r"""Return the determinant of a finite-rank lattice form."""
            assert self.module_rank().is_finite(), "the determinant requires a finite-rank lattice"

            rank = int(self.module_rank())
            gram = self.gram_tensor()
            matrix = self.value_module().matrix_space(rank).from_rows((gram[row, column] for column in range(rank)) for row in range(rank))
            return matrix.determinant()

        def is_even(self) -> bool:
            r"""Return whether ``b(x,x)`` lies in ``2R`` for every lattice vector.

            The represented Gram rule may decide this globally.  If it does
            not, the exact predicate stops at the declared computational
            frontier rather than replacing the exact predicate by an epistemic value.
            """
            decision = _gram_is_even(self.gram_tensor(), self.base_ring())
            assert decision is not Unknown, (
                "exact evenness of this infinite lattice is not determined by its represented Gram rule"
            )
            return decision

        def level(self):
            r"""Return the level of a finite nondegenerate integral lattice.

            This is the least ``N > 0`` annihilating the discriminant form.
            For an even lattice the relevant form is
            ``q:A_L -> QQ/2ZZ``; for an odd lattice only the bilinear pairing
            ``b:A_L^2 -> QQ/ZZ`` is canonically defined.  In particular the
            even level need not equal the exponent of ``A_L``: ``<2>`` has
            discriminant group ``ZZ/2`` but level ``4``.
            """
            assert _engine_ring(self.base_ring()) is SageZZ, (
                "lattice level is currently implemented for integral ZZ-lattices"
            )
            if not self.module_rank().is_finite() or not self.is_nondegenerate():
                raise ValueError("lattice level requires a finite nondegenerate lattice")

            discriminant = self.discriminant_module()
            generators = tuple(discriminant.module_generators())
            denominators = [discriminant.b(left, right).lift().denominator() for left in generators for right in generators]
            if self.is_even():
                denominators.extend((discriminant.q(generator).lift() / SageZZ(2)).denominator() for generator in generators)
            level = SageZZ.one()
            for denominator in denominators:
                level = level.lcm(SageZZ(denominator))
            return level

        @cached_method
        def genus(self):
            r"""Return the genus from signature and discriminant quadratic form.

            The current owned realization is the even, finite-rank,
            nondegenerate ``ZZ`` case, where these data determine the genus.
            """
            assert _engine_ring(self.base_ring()) is SageZZ, (
                "the live genus object currently implements integral ZZ-lattices"
            )
            if not self.module_rank().is_finite() or not self.is_nondegenerate():
                raise ValueError("a genus here requires a finite nondegenerate lattice")
            assert self.is_even(), (
                "the current genus reconstruction from a discriminant quadratic form requires an even lattice"
            )
            return Genus(self.signature_pair(), self.discriminant_quadratic_form())

        def is_locally_isometric(self, other, prime) -> bool:
            r"""Return whether ``self`` and ``other`` are isometric over ``ZZ_p``."""
            if other not in Lattices(self.base_ring()):
                raise TypeError("local lattice isometry compares lattices over one base ring")
            return bool(self.genus().local_symbol(prime) == other.genus().local_symbol(prime))

        def divisibility_ideal(self, element):
            r"""Return the ideal \(b(v, L) = \{b(v,x) : x\in L\}\) of the base ring.

            The pairings against a generating set generate it.  Over
            \(\mathbb Z\) its positive generator is :meth:`div`.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: L = Lattices(ZZ)([[2, 0], [0, -6]])
                sage: L.divisibility_ideal(L.basis_vector(1)) == ZZ.ideal(6)
                True
            """
            assert element.parent() is self, "the divisibility ideal is defined for an element of this lattice"
            ring = self.base_ring()
            pairings = tuple(self.generator_pairings(element).values())
            if not pairings:
                return ring.ideal(ring.zero())
            return ring.ideal(*pairings)

        def generator_pairings(self, element):
            r"""Return the pairings of ``element`` against the selected generators.

            At finite rank every generator is paired; at infinite rank the
            pairing rule of the Gram presentation returns the finitely many
            nonzero pairings.
            """
            assert element.parent() is self, "generator pairings require an element of this lattice"
            match self.module_rank().is_finite():
                case True:
                    return {
                        label: element.b(self.module_generator(label))
                        for label in self.module_generating_set()
                    }
                case False:
                    return self.gram_tensor().pairings_against(element)

        def is_totally_isotropic(self) -> bool:
            r"""Return whether the form vanishes identically: \(\operatorname{rad}(L)=L\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: U.is_totally_isotropic()
                False
                sage: U.subobject_on((U.basis_vector(0),)).is_totally_isotropic()
                True
            """
            assert self.module_rank().is_finite(), "total isotropy is decided here on a finite generating set"
            zero = self.base_ring().zero()
            return all(
                value == zero
                for generator in self.module_generators()
                for value in self.generator_pairings(generator).values()
            )

        def div(self, element):
            r"""Return the divisibility ``gcd{b(element,x): x in L}`` over ``ZZ``."""
            if element.parent() is not self:
                raise TypeError("divisibility is defined for an element of this lattice")

            ring = self.base_ring()
            assert _engine_ring(ring) is SageZZ, "integer divisibility is the ZZ specialization"
            pairings = tuple(
                abs(ring(value)) for value in self.generator_pairings(element).values()
            )
            if not pairings:
                return ring.zero()
            divisor = pairings[0]
            for value in pairings[1:]:
                divisor = divisor.gcd(value)
            return abs(divisor)

        def linear_dual(self):
            r"""Return the exact algebraic dual ``Hom_R(L,R)``."""
            return self.dual_module()

        def metric_map(self):
            r"""Return ``L -> L.linear_dual()``, ``v |-> b(v,-)``."""
            return self.algebraic_correlation_morphism()

        @cached_method
        def dual_lattice(self):
            r"""Return the metric dual ``L^#`` in the rational span of L.

            The underlying module remains an ``R``-module.  For a
            non-unimodular integral lattice its form takes values in
            ``Frac(R)``; it is not turned into a vector space over ``Frac(R)``.
            At infinite rank this is a represented metric-dual lattice in the
            rational span when the Gram rule supplies an inverse rule.  It is
            not the full algebraic dual returned by :meth:`linear_dual`.
            """
            ring = self.base_ring()
            assert self in FormModules(ring).Nondegenerate(), (
                "the metric dual requires nondegeneracy established by the lattice construction"
            )
            match self.module_rank().is_finite():
                case False:
                    dual = ring.free_module(self.module_generating_set())
                    return Lattices(ring)(self.gram_tensor().dual_gram_on(dual))

            fraction_field = ring.fraction_field()
            dual_tensor = self.gram_tensor().change_ring(fraction_field).dual_tensor()
            rank = int(self.module_rank())
            match all(
                dual_tensor[row, column] in ring
                for row in range(rank)
                for column in range(rank)
            ):
                case True:
                    integral_dual_form = tensor(
                        ring,
                        (),
                        (rank, rank),
                        [
                            [ring(dual_tensor[row, column]) for column in range(rank)]
                            for row in range(rank)
                        ],
                    )
                    return Lattices(ring)(
                        integral_dual_form,
                        module_generators=self.module_generating_set(),
                    )
                case False:
                    rational = self.dual_module().equip_bilinear_form(fraction_field, inverse_components)
                    return refine(rational, FormModules(ring).Nondegenerate())

        def metric_dual(self):
            r"""Return the metric dual ``L^#``; explicit synonym for ``dual_lattice``."""
            return self.dual_lattice()

        def dual_basis(self):
            r"""Return the selected basis of ``L^#`` dual to the selected basis of ``L``."""
            return self.dual_lattice().module_generators()

        @cached_method
        def correlation_morphism(self):
            r"""Return ``L -> L^#``, ``v |-> b(v,-)``, whose selected-basis matrix is ``G``."""

            dual_lattice = self.dual_lattice()
            return self.module_category().Mor(self, dual_lattice)(
                lambda label: dual_lattice.linear_combination(
                    self.generator_pairings(self.module_generator(label))
                )
            )

        def correlation(self):
            return self.correlation_morphism()

        @cached_method
        def discriminant_module(self):
            r"""Return ``A_L = coker(L -> L^#)`` with the selected dual-basis presentation."""

            return _discriminant_module(self)

        def discriminant_projection(self):
            r"""Return the quotient morphism ``L^# -> A_L``."""
            return self.discriminant_module().projection()

        def discriminant_class(self, dual_lattice_element):
            r"""Project an element of ``L^#`` to its discriminant class."""
            if dual_lattice_element.parent() is self:
                dual_lattice_element = self.correlation_morphism()(dual_lattice_element)
            return self.discriminant_module().discriminant_class(dual_lattice_element)

        def primitive_dual(self, element):
            r"""Return ``correlation(element)/div(element)`` in ``L^#``.

            For the zero vector this is the zero correlation image, matching
            the archived convention without dividing by the zero
            divisibility.  For a nonzero integral vector, divisibility is the
            positive generator of its pairing ideal, so every selected dual
            coordinate of the correlation image is divisible by it.
            """
            if element.parent() is not self:
                raise TypeError("primitive_dual expects an element of this lattice")
            correlation_image = self.correlation_morphism()(element)
            if element.is_zero():
                return correlation_image
            divisibility = self.div(element)
            if divisibility <= self.base_ring().zero():
                raise ArithmeticError("a nonzero integral vector has positive divisibility")
            dual_lattice = self.dual_lattice()
            divided_coefficients = {}
            for label, coefficient in dual_lattice.framing_coefficients(correlation_image).items():
                if not coefficient:
                    continue
                quotient = coefficient // divisibility
                if divisibility * quotient != coefficient:
                    raise ArithmeticError("the correlation coordinates are not divisible by the vector divisibility")
                divided_coefficients[label] = quotient
            return dual_lattice.linear_combination(divided_coefficients)

        def divided_discriminant_class(self, element):
            r"""Return the class represented by ``correlation(element)/div(element)``."""
            if element.parent() is not self:
                raise TypeError("divided_discriminant_class expects an element of this lattice")
            divisibility = self.div(element)
            if divisibility == 0:
                raise ValueError("the zero vector has no divided discriminant class")
            return self.discriminant_class(self.primitive_dual(element))

        def get_isotropic_type(self, element) -> str:
            r"""Classify a primitive isotropic vector in an even 2-elementary lattice.

            Divisibility one is ``"Odd"``.  Divisibility two is separated by
            whether the class ``[v/2]`` in the discriminant quadratic module
            is characteristic, giving ``"Even characteristic"`` or
            ``"Even ordinary"``.  These names classify the cusp type; they do
            not assert that the ambient lattice itself is odd or even beyond
            the explicit quadratic-form hypothesis.
            """
            if element.parent() is not self:
                raise TypeError("isotropic type is defined for a vector of this lattice")
            if not element.is_isotropic():
                raise ValueError("isotropic type requires an isotropic vector")
            if not element.is_primitive():
                raise ValueError("isotropic type requires a primitive vector")
            if not self.is_even() or not self.is_p_elementary(self.base_ring()(2)):
                raise ValueError("the selected cusp-type classification requires an even 2-elementary lattice")
            divisibility = self.div(element)
            if divisibility == self.base_ring().one():
                return "Odd"
            if divisibility != self.base_ring()(2):
                raise ValueError("a primitive isotropic vector in the selected 2-elementary regime must have divisibility one or two")
            divided_class = self.divided_discriminant_class(element)
            if divided_class.is_characteristic():
                return "Even characteristic"
            return "Even ordinary"

        def radical(self):
            r"""Return ``rad(L)=id_L(L)^perp`` as a subobject of ``L``."""
            return self.identity_morphism().orthogonal_complement()

        def isotropic_reduction(self):
            r"""Return ``S^perp/S`` when this lattice is represented as a subobject."""

            if self not in ModuleSubobjects(self.base_ring()):
                raise TypeError("isotropic reduction requires a chosen lattice inclusion")
            return self.inclusion().isotropic_reduction()

        def I_perp_mod_I(self, vectors):
            r"""Return ``I^perp/I`` for the primitive isotropic span of ``vectors``.

            This is the archived parent-facing name for the same owned
            isotropic-reduction construction.  The input vectors are promoted
            immediately to a represented primitive totally isotropic
            subobject, so the quotient retains its inclusion, perpendicular,
            projection lifts and parabolic data.
            """
            isotropic = self.primitive_isotropic_subobject(*tuple(vectors))
            return isotropic.inclusion().isotropic_reduction()

        def radical_quotient(self):
            r"""Return the nondegenerate quotient ``L/rad(L)``."""
            return self.radical().isotropic_reduction()

        def overlattice(self, *discriminant_classes):
            r"""Return the inclusion ``L -> L'`` generated by discriminant classes.

            The supplied classes are lifted to ``L^#``.  Together with ``L``
            they span ``L'`` inside ``L tensor QQ``; the result is accepted
            exactly when the inherited form is integral on that span.
            """
            assert _engine_ring(self.base_ring()) is SageZZ
            assert self.module_rank().is_finite() and self.is_nondegenerate()

            from functools import reduce

            from sage.modules.free_module import FreeModule as SageFreeModule
            from sage.rings.rational_field import QQ as SageQQ

            discriminant_module = self.discriminant_module()
            ring = self.base_ring()
            rationals = ring.fraction_field()
            rank = int(self.module_rank())
            dual_gram = self.gram_tensor().change_ring(rationals).dual_tensor()
            rational_rows = [[rationals.one() if i == j else rationals.zero() for j in range(rank)] for i in range(rank)]
            dual_labels = tuple(self.dual_lattice().module_generating_set())
            for discriminant_class in discriminant_classes:
                element = discriminant_class if discriminant_class.parent() is discriminant_module else discriminant_module(discriminant_class)
                lift = discriminant_module.dual_lattice_lift(element)
                coefficients = discriminant_module.dual_lattice().framing_coefficients(lift)
                dual_coordinates = tensor(
                    rationals,
                    (),
                    (rank,),
                    [coefficients.get(label, rationals.zero()) for label in dual_labels],
                )
                rational_rows.append(tuple(dual_gram * dual_coordinates))

            denominator = reduce(
                lambda current, coordinate: current.lcm(coordinate.denominator()),
                (coordinate for row in rational_rows for coordinate in row),
                ring.one(),
            )

            # Private HNF/span workspace.  Only backend scalars enter this block.
            backend_denominator = _engine_element(ring, denominator)
            scaled_rows = [[SageZZ(backend_denominator * _engine_element(rationals, coordinate)) for coordinate in row] for row in rational_rows]
            scaled_span = SageFreeModule(SageZZ, rank).submodule(scaled_rows)
            integral_basis_backend = scaled_span.basis_matrix()
            integral_basis_rows = [[_owned_engine_element(ring, entry) for entry in row] for row in integral_basis_backend.rows()]
            basis_rows = tensor.matrix(
                rationals,
                tuple(
                    tuple(_owned_engine_element(rationals, SageQQ(_engine_element(ring, entry)) / SageQQ(backend_denominator)) for entry in row) for row in integral_basis_rows
                ),
            )

            basis_map = rationals.matrix_space(rank, rank).from_rows(tuple(tuple(basis_rows[column, row] for column in range(rank)) for row in range(rank)))
            gram = self.gram_tensor().change_ring(rationals).pullback(basis_map)
            if not all(gram[i, j] in ring for i in range(rank) for j in range(rank)):
                raise ValueError("the selected discriminant classes do not define an integral overlattice")
            integral_entries = [[ring(gram[i, j]) for j in range(rank)] for i in range(rank)]

            labels = finite_ordered_set(range(rank))
            integral_gram = tensor(
                ring,
                (),
                (rank, rank),
                integral_entries,
            )
            enlarged = Lattices(ring)(
                integral_gram,
                module_generators=labels,
            )
            # The system every generator is solved against: the basis of L'
            # in the coordinates of L, as the owned matrix the solver takes.
            integral_basis = ring.matrix_space(rank, rank).from_rows(tuple(tuple(row) for row in integral_basis_rows))
            images = {}
            for source_position, source_label in enumerate(self.module_generating_set()):
                target = [denominator if index == source_position else ring.zero() for index in range(rank)]
                coefficients = _solve_left_integrally(
                    integral_basis,
                    target,
                    ring,
                )
                images[source_label] = enlarged.linear_combination({label: coefficient for label, coefficient in zip(labels, coefficients, strict=True) if coefficient})
            return self.Emb(enlarged)(images)

        def maximal_overlattice(self):
            r"""Return one maximal integral/even overlattice inclusion of ``L``.

            Nikulin's overlattice correspondence identifies integral
            overlattices with bilinear-isotropic subgroups of ``A_L`` and,
            for even ``L``, even overlattices with quadratic-isotropic
            subgroups.  ``discriminant_group()`` selects the applicable form;
            choosing one maximal isotropic subgroup therefore gives one
            maximal overlattice.  No uniqueness is asserted.
            """
            if not self.is_nondegenerate():
                raise ValueError("maximal overlattices require a finite discriminant form")
            form = self.discriminant_group()
            maximal = form.maximal_isotropic_subgroups()
            if maximal.cardinality() == 0:
                raise ArithmeticError("a finite discriminant form has no maximal isotropic subgroup")
            subgroup = maximal[0]
            inclusion = form.overlattice_from_isotropic_subobject(subgroup)
            for larger in form.isotropic_subgroups():
                if int(larger.cardinality()) <= int(subgroup.cardinality()):
                    continue
                if all(element in larger for element in subgroup.embedded_elements()):
                    raise ArithmeticError("the selected glue subgroup is not maximal isotropic")
            return inclusion

        def local_modification(self, prime, *discriminant_classes):
            r"""Return the isotropic ``p``-primary overlattice modification.

            A local modification at ``p`` is the usual discriminant-form glue
            along an isotropic subgroup contained in the ``p``-primary part of
            ``A_L``.  The returned value is the actual inclusion ``L -> L'``.
            """
            prime = self.base_ring()(prime)
            if not prime.is_prime():
                raise ValueError("a local modification is indexed by a prime")
            form = self.discriminant_group()
            classes = tuple(element if element.parent() is form else form(element) for element in discriminant_classes)
            for element in classes:
                order = element.additive_order()
                if order != prime ** int(order.valuation(prime)):
                    raise ValueError(f"local modification at p={prime} requires p-primary glue; the class {element} has order {order}")
            subgroup = form.subgroup_on(classes)
            return form.overlattice_from_isotropic_subobject(subgroup)

        def even_overlattice_inclusions(self):
            r"""Return all even overlattice inclusions ``L -> L'``.

            For an even integral lattice, Nikulin's overlattice correspondence
            identifies even overlattices with isotropic subgroups of the
            discriminant quadratic form.  The zero subgroup is included and
            therefore contributes the identity extension.
            """
            assert _engine_ring(self.base_ring()) is SageZZ, (
                "even overlattice enumeration is currently implemented for integral ZZ-lattices"
            )
            if not self.is_even() or not self.module_rank().is_finite() or not self.is_nondegenerate():
                raise ValueError("even overlattice enumeration requires a finite nondegenerate even lattice")
            form = self.discriminant_quadratic_form()
            return finite_ordered_set(
                tuple(
                    form.overlattice_from_isotropic_subobject(subgroup)
                    for subgroup in form.isotropic_subgroups()
                )
            )

        def embeds_in_even_unimodular(self, positive, negative) -> bool:
            r"""Decide primitive embeddability into an even unimodular ``II_{p,q}``.

            Nikulin's primitive-embedding criterion reduces this to existence
            of the orthogonal complement: its signature is the signature
            difference and its discriminant quadratic form is ``-q_L``.
            """
            ring = self.base_ring()
            positive = ring(positive)
            negative = ring(negative)
            assert _engine_ring(ring) is SageZZ, (
                "the current Nikulin primitive-embedding criterion is for integral ZZ-lattices"
            )
            if not self.is_even() or not self.module_rank().is_finite() or not self.is_nondegenerate():
                raise ValueError("Nikulin's primitive-embedding criterion requires a finite nondegenerate even lattice")
            _signature = self.signature_pair()
            source_positive, source_negative = _signature.first(), _signature.second()
            if (positive - negative) % 8 != 0:
                return False
            if positive < source_positive or negative < source_negative:
                return False
            complement_signature = signature_pair(
                positive - source_positive,
                negative - source_negative,
            )
            return Genus(
                complement_signature,
                self.discriminant_quadratic_form().twist(-1),
            ).exists()

        def embed_in_even_unimodular(self, positive, negative):
            r"""Return one primitive embedding into an even unimodular lattice."""
            if not self.embeds_in_even_unimodular(positive, negative):
                raise ValueError(f"no primitive embedding into II_{{{positive},{negative}}} exists")

            target_gram, embedding_matrix = lattice_engines._even_unimodular_primitive_embedding(self.gram_tensor(), positive, negative)
            target = Lattices(self.base_ring())(target_gram)
            target_generators = tuple(target.module_generators())
            images = tuple(
                sum(
                    (
                        target.scalar_multiple(embedding_matrix[row, column], target_generators[row])
                        for row in range(int(target.module_rank()))
                        if embedding_matrix[row, column]
                    ),
                    target.zero(),
                )
                for column in range(int(self.module_rank()))
            )
            embedding = self.Emb(target)(images)
            if not embedding.is_primitive():
                raise ArithmeticError("OSCAR returned a nonprimitive embedding")
            if target.signature_pair() != signature_pair(positive, negative):
                raise ArithmeticError("OSCAR's primitive-embedding target has the wrong signature")
            return embedding

        def glue_map(self, first, second):
            r"""Return the glue anti-isometry presenting a primitive extension.

            ``first`` and ``second`` are primitive orthogonal subobjects
            ``S,R <= L`` with ranks summing to ``rk(L)``.  Then

            ``L/(S + R)``

            embeds in ``A_S ⊕ A_R`` as the graph of an anti-isometry
            ``H_S -> H_R`` between subgroups of the two discriminant forms.
            The returned arrow is that anti-isometry written as an ordinary
            isometry ``H_S -> H_R(-1)``.  Its domain and codomain are actual
            formed subobjects carrying their inclusions into ``A_S`` and
            ``A_R(-1)``.

            Which discriminant form states this is the parity of ``L``, and
            the returned arrow says which one it used.

            - ``L`` even.  Its sublattices are even, both discriminants carry
              their ``K/2R``-valued quadratic forms, and the glue satisfies
              ``q_R(gamma x) = -q_S(x)``.  Domain and codomain are torsion
              quadratic forms and ``is_quadratic()`` holds.
            - ``L`` odd.  Only the ``K/R``-valued bilinear forms are defined
              on both discriminants -- one of ``S``, ``R`` may itself be even,
              while the extension is not -- and the glue satisfies
              ``b_R(gamma x, gamma y) = -b_S(x,y)``.  Domain and codomain are
              torsion bilinear forms and ``is_quadratic()`` fails.

            The odd statement asks no hypothesis the even one does not; it
            concludes less.  A quadratic-isotropic subgroup is
            bilinear-isotropic and not conversely, so reading an even ``L``
            through its bilinear form would lose exactly the distinction
            between an integral overlattice and an even one.

            Peters and Sterk, *Symmetric and Quadratic Forms, with
            Applications to Coding Theory, Algebraic Geometry and Topology*
            (version of June 2024) state both parities at once, as "symmetric
            (respectively quadratic)": Prop. 15.1.1 for the glue criterion
            ``b_R(psi -, psi -) + b_S(-,-) = 0`` and its reading as an
            anti-isometry, Prop. 15.1.3 for the converse construction with
            ``[L:S+R] = |H_S|`` and ``S``, ``R`` primitive in the result,
            Prop. 1.7.4 for the overlattice correspondence in each parity,
            and Example 1.7.5.1 for a subgroup of ``A_{U(2)}`` that is
            bilinear-isotropic and not quadratic-isotropic.
            """
            ring = self.base_ring()
            assert _engine_ring(ring) is SageZZ, "primitive-extension glue is currently implemented over ZZ"
            for subobject in (first, second):
                assert subobject in ModuleSubobjects(ring) and subobject.inclusion().codomain() is self, "a glue map is taken between two subobjects of this lattice"
                assert subobject.is_primitive(), "a primitive extension is presented by primitive sublattices"
            assert first.module_rank() + second.module_rank() == self.module_rank(), "a primitive extension of L needs rk(S)+rk(R)=rk(L)"
            assert all(self.b(left, right) == ring.zero() for left in first.embedded_module_generators() for right in second.embedded_module_generators()), (
                "a primitive extension is presented by mutually orthogonal sublattices"
            )

            quadratic = self.is_even()
            if quadratic:
                first_discriminant = first.discriminant_quadratic_form()
                second_discriminant = second.discriminant_quadratic_form()
            else:
                first_discriminant = first.discriminant_bilinear_form()
                second_discriminant = second.discriminant_bilinear_form()
            glue_forms = _torsion_form_modules(ring, quadratic=quadratic)
            first_inclusion = tensor.from_morphism(first.inclusion())
            second_inclusion = tensor.from_morphism(second.inclusion())
            ambient_gram = self.gram_tensor()

            graph = {}
            for ambient_generator in self.module_generators():
                coefficients = self.framing_coefficients(ambient_generator)
                labels = tuple(self.module_generating_set())
                ambient_vector = tensor.vector(
                    ring,
                    [coefficients.get(label, ring.zero()) for label in labels],
                )
                ambient_covector = ambient_gram * ambient_vector
                first_covector = ambient_covector * first_inclusion
                second_covector = ambient_covector * second_inclusion
                first_class = first_discriminant.linear_combination(
                    {
                        label: ring(coefficient)
                        for label, coefficient in zip(
                            first_discriminant.module_generating_set(),
                            first_covector,
                            strict=True,
                        )
                        if coefficient
                    }
                )
                second_class = second_discriminant.linear_combination(
                    {
                        label: ring(coefficient)
                        for label, coefficient in zip(
                            second_discriminant.module_generating_set(),
                            second_covector,
                            strict=True,
                        )
                        if coefficient
                    }
                )
                if first_class == first_discriminant.zero():
                    if second_class != second_discriminant.zero():
                        raise ArithmeticError("primitive-extension data send the zero class of A_S to a nonzero class of A_R")
                    continue
                previous = graph.get(first_class)
                if previous is not None and previous != second_class:
                    raise ArithmeticError("primitive-extension data do not define a function H_S -> H_R")
                graph[first_class] = second_class

            source_classes = tuple(graph)
            target_classes = tuple(graph[value] for value in source_classes)
            labels = finite_ordered_set(range(len(source_classes)))
            relations = _relations_among_generators(first_discriminant, source_classes)
            abstract_glue = _torsion_module_presented_by_matrix(relations, labels)

            glue_values = first_discriminant.value_module()
            source_images = {label: source_class for label, source_class in zip(labels, source_classes, strict=True)}

            def source_inclusion(source):
                return source.Mono(first_discriminant)(source_images, quadratic=quadratic)

            source_form = glue_forms.from_module(
                abstract_glue,
                _form_gram_on(first_discriminant, source_classes, quadratic=quadratic),
                glue_values,
                _subobject_ambient=first_discriminant,
                _subobject_generator_images=source_images,
                _subobject_inclusion_factory=source_inclusion,
            )
            target_gram = tuple(tuple(-entry for entry in row) for row in _form_gram_on(second_discriminant, target_classes, quadratic=quadratic))
            # The twist is taken on the module underlying A_R, which is A_R
            # itself when it is the discriminant module and its bilinear
            # reading when the summand is even inside an odd L, so the classes
            # cross into the twist the same way in both parities.
            second_twist = second_discriminant.twist(-1)
            target_images = {label: second_twist(target_class) for label, target_class in zip(labels, target_classes, strict=True)}

            def target_inclusion(target):
                return target.Mono(second_twist)(target_images, quadratic=quadratic)

            target_form = glue_forms.from_module(
                abstract_glue,
                target_gram,
                glue_values,
                _subobject_ambient=second_twist,
                _subobject_generator_images=target_images,
                _subobject_inclusion_factory=target_inclusion,
            )

            second_unformed = second_discriminant.unformed_module()
            target_subgroup = second_unformed.subobject_on(
                tuple(second_unformed(target_class) for target_class in target_classes)
            )
            extension_index = first.sum(second).index()
            if source_form.cardinality() != extension_index:
                raise ArithmeticError("the recovered glue subgroup does not have order [L:S+R]")
            if target_subgroup.cardinality() != extension_index:
                raise ArithmeticError("the two primitive-extension glue subgroups have different orders")

            forward = source_form.module_category().Mor(source_form, target_form)({label: target_form.module_generator(label) for label in labels})
            inverse = target_form.module_category().Mor(target_form, source_form)({label: source_form.module_generator(label) for label in labels})
            return _torsion_form_isometry(forward, inverse, quadratic=quadratic)

        @cached_method
        def discriminant_bilinear_form(self):
            r"""Return ``A_L`` with its descended ``K/R``-valued bilinear form."""

            module = self.discriminant_module()
            assert module in DiscriminantBilinearModules(self.base_ring())
            if module in DiscriminantQuadraticModules(self.base_ring()):
                return module.associated_bilinear_form()
            return module

        def discriminant_quadratic_form(self):
            r"""Return ``A_L`` with its ``K/2R``-valued quadratic form when ``L`` is even."""

            if not self.is_even():
                raise ValueError("a discriminant quadratic form requires an even lattice")
            module = self.discriminant_module()
            assert module in DiscriminantQuadraticModules(self.base_ring())
            return module

        def discriminant_group(self):
            r"""Return the ``ZZ`` discriminant group with every form supported by ``L``."""
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("discriminant_group is the ZZ specialization; use discriminant_module")
            return self.discriminant_quadratic_form() if self.is_even() else self.discriminant_bilinear_form()

        def discriminant_length(self):
            r"""Return the minimal number of generators of ``A_L`` over ``ZZ``."""
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("discriminant length is currently the integral-lattice invariant")
            ring = self.base_ring()
            return ring(len(tuple(invariant for invariant in self.discriminant_module().invariant_factors() if abs(invariant) > ring.one())))

        def is_p_elementary(self, prime) -> bool:
            r"""Return whether ``A_L`` is an elementary abelian ``prime``-group."""
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("p-elementarity is currently the integral-lattice invariant")
            ring = self.base_ring()
            prime = ring(prime)
            if not prime.is_prime():
                raise ValueError("p-elementarity requires a prime p")
            invariants = tuple(abs(invariant) for invariant in self.discriminant_module().invariant_factors() if abs(invariant) > ring.one())
            return all(invariant == prime for invariant in invariants)

        def delta(self):
            r"""Return Nikulin's ``delta`` for an even 2-elementary lattice.

            This is zero exactly when the discriminant quadratic form is
            integer-valued, and one otherwise.  It suffices to test Smith
            generators: on a 2-elementary discriminant group every bilinear
            value lies in ``(1/2)ZZ/ZZ``, so the cross term ``2b(x,y)`` in
            ``q(x+y)`` is integral.
            """
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("Nikulin's delta is an integral-lattice invariant")
            if not self.is_even() or not self.is_p_elementary(self.base_ring()(2)):
                raise ValueError("Nikulin's delta requires an even 2-elementary lattice")
            discriminant_form = self.discriminant_quadratic_form()
            ring = self.base_ring()
            return ring(
                int(
                    any(
                        discriminant_form.q(element).lift() not in ring
                        for element in discriminant_form.smith_form_module_generators()
                    )
                )
            )

        def is_coeven(self) -> bool:
            r"""Return whether the discriminant quadratic form is integer-valued.

            This is the coeven property of an even nondegenerate integral
            lattice.  Unlike :meth:`delta`, it is not restricted to
            2-elementary discriminant groups: every element of ``A_L`` is
            checked in the finite discriminant quadratic module.
            """
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("coevenness is currently the integral-lattice invariant")
            if not self.is_even():
                raise ValueError("coevenness uses the discriminant quadratic form of an even lattice")
            if not self.is_nondegenerate():
                raise ValueError("coevenness requires a finite discriminant quadratic module")
            discriminant_form = self.discriminant_quadratic_form()
            ring = self.base_ring()
            return all(
                discriminant_form.q(element).lift() in ring
                for element in discriminant_form
            )

        def is_coodd(self) -> bool:
            r"""Return the negation of :meth:`is_coeven`."""
            return not self.is_coeven()

        def two_elementary_invariants(self):
            r"""Return Nikulin's \((r,a,\delta)\) for an even 2-elementary lattice.

            The rank, the length of the discriminant group and \(\delta\) are
            three natural numbers, so the triple is a point of
            \(\mathbb N^3\).
            """
            if not self.is_p_elementary(self.base_ring()(2)) or not self.is_even():
                raise ValueError("the lattice is not even and 2-elementary")
            return nikulin_invariants(self.module_rank(), self.discriminant_length(), self.delta())

        def two_u_eichler_model(self):
            r"""Return the represented ``U + U + self`` Eichler model."""
            from dzack_research.preamble.categories.eichler_criterion import (
                TwoUEichlerModel,
            )

            return TwoUEichlerModel(self)

        def rational_polyhedral_cone(
            self,
            halfspace_covectors,
            *,
            equation_covectors=(),
            wall_roots=None,
            complete=None,
        ):
            r"""Return the exact rational polyhedral cone cut out in this lattice."""
            from dzack_research.preamble.categories.polyhedral_cones import (
                _rational_polyhedral_cone,
            )

            return _rational_polyhedral_cone(
                self,
                halfspace_covectors,
                equation_covectors=equation_covectors,
                wall_roots=wall_roots,
                complete=complete,
            )

        def number_field_vinberg(self, real_embedding):
            r"""Retain the selected real place for number-field Vinberg enumeration."""
            from dzack_research.preamble.categories.hyperbolic_lattices import (
                NumberFieldVinbergLattice,
            )

            return NumberFieldVinbergLattice(self, real_embedding)

        def reflection(self, root):
            r"""Return the integral orthogonal reflection in ``root``.

            A lattice root is defined by this integrality: for every selected
            module generator ``e_i``, ``2*b(e_i,root)/b(root,root)`` must lie
            in the base ring.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: root = U.basis_vector(0) + U.basis_vector(1)
                sage: U.reflection(root)(U.basis_vector(0))
                -e_1
            """
            if root.parent() is not self:
                raise TypeError("the reflecting vector must belong to this lattice")
            if not root.is_root():
                raise ValueError(f"{root} does not define an integral lattice reflection")
            ring = self.base_ring()
            fraction_field = ring.fraction_field()
            norm = fraction_field(root.q())

            def image(label):
                generator = self.module_generator(label)
                coefficient = ring(fraction_field(ring(2) * generator.b(root)) / norm)
                return generator - self.scalar_multiple(coefficient, root)

            return self.Aut()(image)

        def eichler_transvection(self, isotropic, orthogonal):
            r"""Return the Eichler transvection \(t(e,a)\in O(L)\).

            For isotropic \(e\) and \(a\in e^\perp\),

            \[
            t(e,a)(x) = x - b(a,x)\,e + b(e,x)\,a - \tfrac12 q(a)\,b(e,x)\,e .
            \]

            It fixes \(e\) and acts trivially on \(e^\perp/e\), so it lies in
            the unipotent radical of the parabolic subgroup stabilizing
            \(\mathbb Z e\).  These transvections generate the stable
            orthogonal group and put vectors into normal form, which is how
            Eichler's criterion realizes its orbit equivalences.  The formula
            is transcribed at ``notes/topics/coble-enriques-lattice-theory/``
            ``reflective-two-elementary-lattices.md``, which attributes it to
            Dawes, section 2 equation (7).
            \(t(e,a)\) preserves \(L\) exactly when every coefficient
            \(\tfrac12 q(a)\,b(e,x)\) is integral, automatic on an even
            lattice and asserted otherwise.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: L = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
                sage: e, f, a, _b = L.module_generators()
                sage: t = L.eichler_transvection(e, a)
                sage: t(e) == e and t(f) == f + a + e
                True
            """
            assert isotropic.parent() is self and orthogonal.parent() is self, "an Eichler transvection is built from two vectors of this lattice"
            ring = self.base_ring()
            zero = ring.zero()
            assert isotropic.q() == zero, f"an Eichler transvection is taken in an isotropic vector; q(e)={isotropic.q()}"
            assert isotropic.b(orthogonal) == zero, f"an Eichler transvection needs a in e^perp; b(e,a)={isotropic.b(orthogonal)}"
            fraction_field = ring.fraction_field()
            half_norm = fraction_field(orthogonal.q()) / fraction_field(ring(2))

            def image(label):
                x = self.module_generator(label)
                half_coefficient = half_norm * fraction_field(x.b(isotropic))
                assert half_coefficient in ring, f"t(e,a) does not preserve the lattice: q(a) b(e,{x})/2 = {half_coefficient} is not integral"
                return (
                    x
                    - self.scalar_multiple(x.b(orthogonal), isotropic)
                    + self.scalar_multiple(x.b(isotropic), orthogonal)
                    - self.scalar_multiple(ring(half_coefficient), isotropic)
                )

            return self.Aut()(image)

        def is_positive_definite(self) -> bool:
            rank = self.module_rank()
            return self.signature_pair() == signature_pair(rank, 0)

        def is_negative_definite(self) -> bool:
            rank = self.module_rank()
            return self.signature_pair() == signature_pair(0, rank)

        def is_definite(self) -> bool:
            return self.is_positive_definite() or self.is_negative_definite()

        def is_elliptic(self) -> bool:
            r"""Return whether this finite-rank lattice is negative definite.

            In the reflection-lattice convention used by the project, an
            elliptic form has signature ``(0,n,0)``.  The public signature pair
            records only the positive and negative indices, while the rank
            determines the radical dimension.
            """

            return self.is_negative_definite()

        def is_parabolic(self) -> bool:
            r"""Return whether the form has signature ``(0,n-1,1)``.

            Thus a parabolic lattice is negative semidefinite with a
            one-dimensional radical; negative-definite (elliptic) lattices are
            deliberately excluded.
            """

            rank = self.module_rank()
            if not rank.is_finite():
                return False
            finite_rank = int(rank.finite_value())
            if finite_rank < 2:
                return False
            return self.signature_pair() == signature_pair(0, finite_rank - 1)

        def lll_reduction(self):

            return _lll_reduction(self)

        def LLL(self):
            r"""Return the same formed lattice in an LLL-reduced framing."""
            return self.lll_reduction().reduced

        def bkz_reduction(self, block_size=20):

            return _bkz_reduction(self, block_size=block_size)

        def BKZ(self, block_size=20):
            r"""Return the same formed lattice in a BKZ-reduced framing."""
            return self.bkz_reduction(block_size=block_size).reduced

        def hkz_reduction(self):

            return _hkz_reduction(self)

        def HKZ(self):
            r"""Return the full-block BKZ (HKZ) reframing."""
            return self.hkz_reduction().reduced

        def minimum(self):

            return _minimum(self)

        def vectors_of_square(self, square):

            return _vectors_of_square(self, square)

        def vectors_of_square_and_divisibility(self, square, divisibility):

            return _vectors_of_square_and_divisibility(self, square, divisibility)

        def roots(self):

            return _roots(self)

        def roots_of_square(self, square):

            return _roots_of_square(self, square)

        def root_sublattice(self):

            return _root_sublattice(self)

        def reduction_cell(self, inequalities, *, equations=()):
            r"""Return the homogeneous rational cell ``{x : a(x) >= 0, e(x) = 0}`` in this lattice.

            The cell is a rational polyhedral cone.  Each rational wall, given
            by its coordinates in the dual framing, is stated by the primitive
            integral covector on its ray, which cuts out the same half-space.
            """
            from dzack_research.preamble.categories.polyhedral_cones import (
                _integral_covector,
            )

            return self.rational_polyhedral_cone(
                tuple(_integral_covector(self, wall) for wall in inequalities),
                equation_covectors=tuple(_integral_covector(self, wall) for wall in equations),
            )

        def reduction_complex_exploration(
            self,
            cells,
            adjacencies,
            *,
            complete=False,
        ):
            r"""Return the selected finite exact reduction-complex exploration."""
            from dzack_research.preamble.categories.reduction_complexes import (
                RationalReductionComplexExploration,
            )

            return RationalReductionComplexExploration(
                self,
                cells,
                adjacencies,
                complete=complete,
            )

        def lorentzian_reduction_complex(self, marked_vectors=None):
            r"""Return the completed Lorentzian perfect-domain traversal of this lattice."""
            from dzack_research.preamble.categories.reduction_complexes import (
                _lorentzian_reduction_complex,
            )

            return _lorentzian_reduction_complex(self, marked_vectors=marked_vectors)

        def vector_configuration(self, module_generating_set):
            r"""Return the sublattice framed by the stated ordered vector family."""
            subobject = self.subobject_on(module_generating_set)
            return refine(subobject, VectorConfigurations(self.base_ring()))

        def vector_primitive_extension(self, element):
            r"""Return the primitive-extension/gluing datum cut out by ``element``."""

            return VectorPrimitiveExtension(self, element)

        def definite_complement_extensions(self, left, right):
            r"""Return all isometries ``g`` with ``g(left)=right`` in the definite-complement regime."""

            return _definite_complement_extensions(self, left, right)

        def gluing_route_discriminant_classes(self, left, right):
            r"""Return admissible ``O(A_L)`` classes from the primitive-extension gluing route."""

            return _gluing_route_discriminant_classes(self, left, right)

        def stable_complement_root_reflections(self, element):
            r"""Return stable reflections in root-orbit representatives of ``element^perp``."""

            return _stable_complement_root_reflections(self, element)

        def primitive_isotropic_subobject(self, *basis):
            r"""Return the primitive totally isotropic sublattice spanned by ``basis``.

            Admission checks saturation and vanishing of the restricted form
            before refining the represented subobject, so a refused span leaves
            no wrongly placed object behind.  The stated family must also be
            nonempty and independent.
            """
            from dzack_research.preamble.categories.isotropic_parabolics import (
                PrimitiveIsotropicSubobjects,
            )

            elements = tuple(
                element if element_parent(element) is self else self(element)
                for element in basis
            )
            assert elements, "an isotropic sublattice is spanned by a nonempty family"
            subobject = self.subobject_on(elements)
            assert subobject.is_primitive(), (
                "a primitive isotropic subobject has torsion-free cokernel; the stated "
                "span is not saturated in its lattice"
            )
            zero = self.base_ring().zero()
            embedded = subobject.embedded_module_generators()
            labels = subobject.module_generating_set()
            assert all(
                self.b(embedded[left], embedded[right]) == zero
                for left in labels
                for right in labels
            ), "the stated span is not totally isotropic for the lattice form"
            subobject = refine(
                subobject,
                PrimitiveIsotropicSubobjects(self.base_ring()),
            )
            assert subobject.module_rank() == finite_ordered_set(elements).cardinality(), (
                "the stated isotropic family is linearly dependent, so it does not "
                "frame the sublattice it spans"
            )
            return subobject

        def covering_discriminant_classes(self, square):
            r"""Return discriminant classes covering primitive vectors of ``square``.

            For a primitive ``v`` write ``d = div(v)``.  Then ``v/d`` lies in
            ``L^#`` and ``x = [v/d]`` lies in ``A_L`` with additive order
            exactly ``d``: a smaller order ``e`` would put ``(e/d)v`` in
            ``L`` and contradict primitivity.  The discriminant quadratic form
            satisfies ``q_{A_L}(x) = q(v)/d^2``.  Thus the classes satisfying

            ``q_{A_L}(x) = square / ord(x)^2``

            form a finite covering list for primitive vectors of that square,
            computed by one pass over the finite discriminant group.  Under
            Eichler's criterion each class carries at most one stable orbit;
            whether a covering class is attained is a separate question.
            """
            discriminant = self.discriminant_group()
            values = discriminant.quadratic_value_module()
            field = self.base_ring().fraction_field()
            target = field(square)
            return finite_ordered_set(
                tuple(
                    element
                    for element in discriminant.elements()
                    if discriminant.q(element)
                    == values(target / field(element.additive_order()) ** 2)
                )
            )

        def hyperbolic_plane_summand_count(self):
            r"""Return the number of represented indecomposable hyperbolic-plane summands."""
            plane = Lattices(self.base_ring())("U")
            return sum(
                1
                for summand in self.indecomposable_summands()
                if summand.is_isometric(plane)
            )

        def splits_two_hyperbolic_planes(self) -> bool:
            r"""Return whether the represented decomposition splits at least two copies of ``U``.

            This reads the selected decomposition.  A Gram-matrix presentation
            with no represented decomposition therefore answers ``False`` even
            when the abstract lattice is isometric to one splitting ``U + U``.
            """
            if not self.is_decomposable():
                return False
            return self.hyperbolic_plane_summand_count() >= 2

        def eichler_criterion_applies(self) -> bool:
            r"""Return whether Eichler's criterion classifies primitive-vector orbits here."""
            return bool(self.is_even()) and self.splits_two_hyperbolic_planes()

        def are_in_one_stable_orbit(self, left, right) -> bool:
            r"""Decide whether two primitive vectors share one ``ker(rho_L)`` orbit.

            Eichler's criterion says that, for an even lattice splitting two
            hyperbolic planes, square, divisibility, and divided discriminant
            class are a complete invariant of a primitive-vector orbit.  Both
            vectors are therefore required to be primitive and to belong to
            this represented lattice.
            """
            assert left.parent() is self and right.parent() is self, (
                "an orbit comparison is between two vectors of this lattice"
            )
            assert self.eichler_criterion_applies(), (
                "Eichler's criterion classifies primitive-vector orbits for an even "
                "lattice splitting two hyperbolic planes; this lattice does not "
                "present such a decomposition, and the orbit question is then a "
                "computation for the exact indefinite backend rather than a "
                "comparison of invariants"
            )
            for vector in (left, right):
                assert self.subobject_on((vector,)).is_primitive(), (
                    "Eichler's criterion compares primitive vectors"
                )
            return (
                left.q() == right.q()
                and left.div() == right.div()
                and left.divided_discriminant_class() == right.divided_discriminant_class()
            )

        @cached_method
        def primitive_isotropic_vectors(self):
            r"""Return the exact locus of nonzero primitive isotropic vectors.

            Membership is ``q(v) = 0`` together with saturation of ``Z v``:
            the vector is not a proper multiple of another lattice vector.
            For an indefinite isotropic lattice this locus is countably
            infinite, so it is represented by exact membership rather than by
            enumeration; its finite ``O(L)`` orbit decomposition gives the
            cusps.
            """
            zero = self.zero()
            value_zero = self.base_ring().zero()

            def is_primitive_isotropic(vector) -> bool:
                if vector == zero:
                    return False
                if self.q(vector) != value_zero:
                    return False
                return bool(self.subobject_on((vector,)).is_primitive())

            return self.condition_set(is_primitive_isotropic)

        def cusps(self, rank=1):
            r"""Return the ``O(L)``-orbits of primitive isotropic rank-``rank`` subobjects.

            The finite ordered result retains each representative, its
            parabolic subgroup and stabilizer generators, and transporter
            witnesses for membership.  Rank one gives zero-dimensional cusps;
            rank two gives one-dimensional cusps.
            """
            return self.Aut().cusps(rank)

        def tits_building_incidence(self):
            r"""Return finite line/plane incidence in the ``O(L)`` quotient building.

            Rank-two flag representatives come from the exact indefinite
            flag computation with its selected flag.  Their two terms determine unique
            line and plane cusp orbits.  Each record retains the actual nested
            embeddings, transporters to the selected cusp representatives, and
            exact flag stabilizer generators.
            """
            return self.Aut().tits_building_incidence()

        def primitive_isotropic_sublattices(self, rank=1):
            r"""Return primitive totally isotropic rank-``rank`` subobjects of this lattice."""
            return _primitive_isotropic_sublattice_locus(self, rank)

        def vector_locus(self, norm, primitive=False):
            r"""Return vectors of square ``norm``, optionally restricted to primitive vectors."""
            selected_norm = self.base_ring()(norm)
            return self.condition_set(
                lambda vector: (
                    vector.q() == selected_norm
                    and (not primitive or vector.is_primitive())
                )
            )

        def isotropic_sublattice_locus(self, rank):
            r"""Return represented totally isotropic rank-``rank`` sublattices."""
            return _isotropic_sublattice_locus(self, rank)

        def isotropic_flag_locus(self, ranks):
            r"""Return nested represented isotropic sublattices with the stated ranks."""
            return _isotropic_flag_locus(self, ranks)

        def isotropic_flag(self, *basis):

            return IsotropicFlag(self, basis)

        def isotropic_line_orbit_representatives(self):
            return self.O().isotropic_orbit_representatives(1)

        def isotropic_plane_orbit_representatives(self):
            return self.O().isotropic_orbit_representatives(2)

        def isotropic_flag_orbit_representatives(self, rank=2):
            return self.O().isotropic_orbit_representatives(rank, flag=True)

        def shortest_vectors(self):

            return _shortest_vectors(self)

        def theta_series(self, precision=20, variable="q"):

            return _theta_series(self, precision=precision, variable=variable)

        def hermite_invariant(self):

            return _hermite_invariant(self)

        def successive_minima(self):

            return _successive_minima(self)

        def gaussian_heuristic(self, *, exact_form=False):

            return _gaussian_heuristic(self, exact_form=exact_form)

        def hadamard_ratio(self):

            return _hadamard_ratio(self)

        def closest_vector(self, target):

            return _closest_vector(self, target)

        def close_vectors(self, target, square_bound):
            r"""Return the lattice vectors within the stated quadratic bound of ``target``."""
            return _close_vectors(self, target, square_bound)

        def babai(self, target):

            return _babai(self, target)

        approximate_closest_vector = babai

        def voronoi_cell(self, bound=None):
            r"""Return the Voronoi cell of this definite lattice, a convex polytope in ``L tensor QQ``."""
            return _voronoi_cell(self, bound=bound)

        def voronoi_facets(self):
            r"""Return the facets of the Voronoi cell, indexed by their relevant vectors."""
            return _voronoi_facets(self)

        def voronoi_relevant_vectors(self):
            r"""Return the Voronoi-relevant vectors, the normals of the facets of the cell."""
            return _voronoi_relevant_vectors(self)

        def contact_polytope(self):

            return _contact_polytope(self)

        def packing_radius(self):

            return _packing_radius(self)

        def covering_radius(self):

            return _covering_radius(self)

        def center_density(self):

            return _center_density(self)

        def packing_density(self):

            return _packing_density(self)

        def kissing_number(self):

            return _kissing_number(self)

        def twist(self, scalar):
            r"""Keep the module and rescale its form by ``scalar``.

            The result is the same free module with
            \(b'(x,y)=\mathrm{scalar}\cdot b(x,y)\).  The Gram is
            scaled as a type-$(0,2)$ tensor: a pairing rule is not
            materialized as a finite array.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Iinf = Lattices(ZZ)(ZZ^NN)
                sage: Iinf.basis_vector(0)^2
                1
                sage: Iinf.twist(2).basis_vector(0)^2
                2
                sage: latex(Iinf.twist(2).gram_tensor())
                2\,I_{\infty}
                sage: Iinf.twist(2).gram_tensor()
                2 I_∞ ∈ (ZZ^NN ⊗ ZZ^NN)*
            """

            ring = self.base_ring()
            gram = self.gram_tensor()
            scalar = ring(scalar)
            lattices = Lattices(ring)
            match self.module_rank().is_finite():
                case True:
                    size = int(self.module_rank())
                    scaled = tensor(
                        ring,
                        (),
                        (size, size),
                        [[scalar * gram[row, column] for column in range(size)] for row in range(size)],
                    )
                    return lattices(scaled, module_generators=self.module_generating_set())
                case False:
                    return lattices(gram.scaled_by(scalar))

        def __matmul__(self, other):
            r"""Return the tensor product lattice ``self \otimes other``."""
            category = Lattices(self.base_ring())
            match other in category:
                case True:
                    return category.tensor_product((self, other))
                case False:
                    return NotImplemented

        def __add__(self, other):
            r"""Return the orthogonal direct sum of the two summands.

            The two-index case of ``Lattices(R).biproduct``, in the
            concatenated basis.  Being binary, ``L + M + N`` is a
            two-summand sum whose first summand is a sum; the sum of three
            summands over a three-element index set is
            ``Lattices(R).biproduct([L, M, N])``.  Infinite \(\oplus\)
            infinite is not constructed.  ``sum([...])`` uses ``0 + L``.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U") + Lattices(ZZ)(ZZ^NN)
                Integral lattice of rank +Infinity and signature (+Infinity, 1)
            """
            if other == 0:
                return self

            category = Lattices(self.base_ring())
            assert other in category
            return category.biproduct((self, other))

        def __radd__(self, other):
            if other == 0:
                return self
            return NotImplemented

        def __pow__(self, exponent):
            r"""Return \(L^{\oplus n}\), the \(n\)-fold orthogonal direct sum.

            It is the biproduct of the constant family over \(\Delta[n-1]\),
            so \(L^{\oplus 3}\) has three summands, one per index.  ``L ** 0``
            is the empty sum: the zero lattice, the unit of ``+``.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: (Lattices(ZZ)("U") ** 3).signature_pair()
                (3, 3)
            """
            count = int(exponent)
            assert count >= 0, "an orthogonal power L^n takes a natural number n"
            category = Lattices(self.base_ring())
            if count == 0:
                return category(0)
            return category.biproduct(
                indexed_family(
                    Sets.Δ[count - 1],
                    lambda _position: self,
                    name=f"Orthogonal power summands of {self}",
                )
            )

        def _repr_(self):
            r"""Name the lattice by rank and, over \(\mathbb{Q}\), signature.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U")
                Integral lattice of rank 2 and signature (1, 1)
            """
            from sage.rings.integer_ring import ZZ
            from sage.rings.rational_field import QQ

            kind = "Integral lattice" if _engine_ring(self.base_ring()) is ZZ else "Lattice"
            rank = self.module_rank()
            _signature = _signature_pair_of_gram(self.gram_tensor())
            if _engine_ring(self.base_ring().fraction_field()) is QQ and _signature is not Unknown:
                pos, neg = _signature.first(), _signature.second()
                return f"{kind} of rank {rank} and signature ({pos}, {neg})"
            return f"{kind} of rank {rank} over {self.base_ring()}"

        def _latex_(self):
            r"""Display $L$ with its invariants; the Gram is $G_L$, not $L$.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: latex(Lattices(ZZ)("U"))
                \begin{gathered}
                L \in \mathrm{Lattices}(\mathbb{Z}), \quad \mathrm{rk}(L) = 2, \quad \mathrm{sig}(L) = (1, 1), \quad \mathrm{disc}(L) = 1 \\
                L = U \\
                G_L = \left(\begin{array}{rr}
                \cdot & 1 \\
                1 & \cdot
                \end{array}\right) \\
                \end{gathered}
            """

            _name, tex = _ring_notation(self.base_ring())
            return _lattice_latex(self, tex)

    class ElementMethods:
        r"""Operations generic to every lattice element.

        The pairing ``v.b(w)`` and the norm ``v.q()`` are the form module's;
        this level adds the lattice notation and the lattice invariants of a
        vector.
        """

        def _lattice_terms(self):
            r"""The nonzero coefficients of this vector, in the order of the framing's enumeration."""
            ranking = self.parent().module_generating_set().ranking_map()
            return sorted(
                self.monomial_coefficients().items(),
                key=lambda term: int(ranking(term[0])),
            )

        def _repr_(self):
            r"""Print the vector as a linear combination of the generator labels.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U").basis_vector(0)
                e_0
            """
            return repr_lincomb(self._lattice_terms(), strip_one=True)

        def _latex_(self):
            return repr_lincomb(self._lattice_terms(), is_latex=True, strip_one=True)

        def __mul__(self, other):
            r"""``v * w`` is \(b(v,w)\) for a vector of this lattice, and ``v * r`` the scalar multiple for ``r`` in the base ring.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: e, f = I2.basis_vector(0), I2.basis_vector(1)
                sage: e.b(f), e*e
                (0, 1)
            """
            parent = self.parent()
            match element_parent(other) is parent:
                case True:
                    return parent.b(self, other)
            match other in parent.base_ring():
                case True:
                    return parent.scalar_multiple(other, self)
            return NotImplemented

        def __pow__(self, exponent):
            r"""``v^2`` is \(q(v)\)."""
            assert exponent == 2, f"v^n on a lattice vector is q(v) at n=2, got {exponent}"
            return self.q()

        __xor__ = __pow__

        def norm(self):
            r"""Return the form norm ``b(v,v)``."""
            return self.q()

        def divisibility_ideal(self):
            return self.parent().divisibility_ideal(self)

        def div(self):
            r"""Return the positive integer generator of ``b(v,L)`` over ``ZZ``.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)(ZZ^NN).basis_vector(0).div()
                1
            """
            return self.parent().div(self)

        def divisor(self):
            r"""Return the positive generator of ``b(v,L)`` over ``ZZ``."""
            return self.div()

        def primitive_dual(self):
            r"""Return ``v/div(v)`` under the metric embedding ``L -> L^#``."""
            return self.parent().primitive_dual(self)

        def primitive_dual_in_discriminant_bilinear_form(self):
            r"""Return the class of ``v/div(v)`` in the discriminant bilinear form."""
            form = self.parent().discriminant_bilinear_form()
            return form.discriminant_class(self.primitive_dual())

        def primitive_dual_in_discriminant_quadratic_form(self):
            r"""Return the class of ``v/div(v)`` in the discriminant quadratic form.

            This operation requires an even lattice, exactly as the
            discriminant quadratic form itself does.
            """
            form = self.parent().discriminant_quadratic_form()
            return form.discriminant_class(self.primitive_dual())

        def divided_discriminant_class(self):
            return self.parent().divided_discriminant_class(self)

        def discriminant_class(self):
            r"""Return ``[v/div(v)]`` in the discriminant module for primitive ``v``."""
            if not self.is_primitive():
                raise ValueError("the associated primitive discriminant class requires a primitive lattice vector")
            return self.divided_discriminant_class()

        def to_covector(self):
            r"""Return \(b(v,-)\in\operatorname{Hom}_R(L,R)\), the image of \(v\) under the algebraic correlation.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: e, f = U.module_generators()
                sage: e.to_covector().parent() is U.dual_module()
                True
            """
            return self.parent().algebraic_correlation_morphism()(self)

        def sublattice(self):
            r"""Return \(Rv\hookrightarrow L\): the rank-one subobject spanned by this vector, with its inclusion."""
            return self.parent().subobject_on((self,))

        def is_primitive(self) -> bool:
            r"""Return whether \(Rv\hookrightarrow L\) has torsion-free cokernel.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: e, f = Lattices(ZZ)("U").module_generators()
                sage: e.is_primitive(), (2 * e).is_primitive(), (2 * e + 3 * f).is_primitive()
                (True, False, True)
            """
            return self.sublattice().is_primitive()

        def orthogonal_complement(self):
            r"""Return \(v^\perp\hookrightarrow L\) as a subobject of the lattice."""
            return self.sublattice().orthogonal_complement()

        def perp(self):
            r"""Synonym for :meth:`orthogonal_complement`."""
            return self.orthogonal_complement()

        def isotropic_reduction(self):
            r"""Return \(v^\perp/Rv\) for an isotropic vector, with its parabolic data."""
            return self.sublattice().inclusion().isotropic_reduction()

        def e_perp_mod_e(self):
            r"""Return ``v^perp/Rv``; archived synonym for :meth:`isotropic_reduction`."""
            return self.isotropic_reduction()

        def is_root(self) -> bool:
            r"""Return whether the orthogonal reflection in this vector is integral.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Iinf = Lattices(ZZ)(ZZ^NN)
                sage: Iinf.basis_vector(0).is_root()
                True
                sage: Iinf.linear_combination({0: ZZ(2), 1: ZZ(1)}).is_root()
                False
            """

            parent = self.parent()
            ring = parent.base_ring()
            assert ring.is_integral_domain(), "roots are defined here over an integral domain"
            norm = ring(self.q())
            if norm == ring.zero():
                return False
            fraction_field = ring if ring.is_field() else ring.fraction_field()
            norm_in_fraction_field = fraction_field(norm)
            return all(
                fraction_field(ring(2) * coefficient) / norm_in_fraction_field in ring
                for coefficient in parent.generator_pairings(self).values()
            )



class BiproductLattices(OwnedCategoryOverBaseRing):
    r"""Lattice biproducts in their concatenated lattice framing."""

    def an_object(self):
        lattice = Lattices(self.base_ring()).an_object()
        return Lattices(self.base_ring()).biproduct((lattice, lattice))

    @classmethod
    def _repr_object_names(cls):
        return "chosen lattice biproducts"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import (
            BiproductModules,
        )

        return [
            DirectSumObjects(Lattices(self.base_ring())),
            BiproductModules(self.base_ring()),
        ]

    class ParentMethods:
        def _biproduct_factor_position(self, index):
            factors = self.biproduct_factors()
            normalized = factors.index_set()(index)
            return int(factors.index_set().ranking_map()(normalized))

        def _biproduct_block_offsets(self):
            r"""The positions at which the summands' blocks begin in the concatenated framing."""
            return _block_offsets(
                tuple(cardinal(factor.module_rank()) for factor in self.biproduct_factors())
            )

        def injection(self, index):
            r"""Return the selected summand inclusion into this orthogonal sum."""
            factors = self.biproduct_factors()
            normalized = factors.index_set()(index)
            position = self._biproduct_factor_position(normalized)
            summand = factors[normalized]
            source_labels = summand.module_generating_set()
            target_labels = self.module_generating_set()
            offset = self._biproduct_block_offsets()[position]

            def image(label):
                source_position = int(source_labels.ranking_map()(label))
                target_label = target_labels.ranking_map().inverse()(
                    offset + source_position
                )
                return self.module_generator(target_label)

            return summand.module_category().Mor(summand, self)(image)

        def projection(self, index):
            r"""Return the selected projection from this orthogonal sum."""
            factors = self.biproduct_factors()
            normalized = factors.index_set()(index)
            position = self._biproduct_factor_position(normalized)
            summand = factors[normalized]
            offsets = self._biproduct_block_offsets()
            source_labels = self.module_generating_set()
            target_labels = summand.module_generating_set()

            def image(label):
                source_position = int(source_labels.ranking_map()(label))
                which, place = _block_position(offsets, source_position)
                match which == position:
                    case True:
                        target_label = target_labels.ranking_map().inverse()(place)
                        return summand.module_generator(target_label)
                    case False:
                        return summand.zero()

            return self.module_category().Mor(self, summand)(image)

        def from_coproduct_cocone(self, legs):
            r"""Return the unique map out of this biproduct with the stated legs."""
            from dzack_research.preamble.categories.abstract_categories.products import (
                _finite_factor_family,
            )

            factors = self.biproduct_factors()
            legs = _finite_factor_family(legs, name="Coproduct cocone legs")
            assert legs.index_set() == factors.index_set(), (
                "a cocone under a biproduct has one leg per factor"
            )
            first = factors.index_set().ranking_map().inverse()(0)
            target = legs[first].codomain()
            assert all(leg.codomain() is target for leg in legs), (
                "a cocone has one apex"
            )
            assert all(
                legs.value(index).domain() is factors.value(index)
                for index in factors.index_set()
            ), "each leg of the cocone starts at its own factor"
            offsets = self._biproduct_block_offsets()
            source_labels = self.module_generating_set()

            def image(label):
                source_position = int(source_labels.ranking_map()(label))
                which, place = _block_position(offsets, source_position)
                factor_index = factors.index_set().ranking_map().inverse()(which)
                factor = factors[factor_index]
                factor_label = factor.module_generating_set().ranking_map().inverse()(place)
                return legs[factor_index](factor.module_generator(factor_label))

            return self.module_category().Mor(self, target)(image)

        def from_product_cone(self, legs):
            r"""Return the unique map into this biproduct with the stated legs."""
            from dzack_research.preamble.categories.abstract_categories.products import (
                _finite_factor_family,
            )

            factors = self.biproduct_factors()
            legs = _finite_factor_family(legs, name="Product cone legs")
            assert legs.index_set() == factors.index_set(), (
                "a cone over a biproduct has one leg per factor"
            )
            first = factors.index_set().ranking_map().inverse()(0)
            source = legs[first].domain()
            assert all(leg.domain() is source for leg in legs), "a cone has one apex"
            assert all(
                legs.value(index).codomain() is factors.value(index)
                for index in factors.index_set()
            ), "each leg of the cone lands in its own factor"

            def image(label):
                generator = source.module_generator(label)
                return sum(
                    (
                        self.injection(index)(legs.value(index)(generator))
                        for index in factors.index_set()
                    ),
                    self.zero(),
                )

            return source.module_category().Mor(source, self)(image)


def FiniteRankLattices(base_ring):
    r"""``Lattices(R).FinitelyGenerated()``, under the name the session catalogue uses."""
    return Lattices(base_ring).FinitelyGenerated()


def NondegenerateLattices(base_ring):
    r"""``Lattices(R).Nondegenerate()``, under the name the session catalogue uses."""
    return Lattices(base_ring).Nondegenerate()


def EvenLattices(base_ring):
    r"""``Lattices(R).Even()``, under the name the session catalogue uses."""
    return Lattices(base_ring).Even()


class RankOneRationalWittDecomposition:
    r"""The rational Witt decomposition attached to a primitive isotropic line.

    The integral objects ``I <= I^perp <= L`` and ``K_I=I^perp/I`` remain the
    source arithmetic data.  After base change to ``Frac(R)``, a selected
    isotropic partner ``f`` with ``b(e,f)=1`` gives

    ``L_Q = <e,f> perp K_Q``.

    In a non-unimodular cusp ``f`` need not lie in ``L``; that failure is the
    integral gluing which can restrict the Levi image.
    """

    def __init__(
        self,
        reduction,
        bezout_partner,
        rational_lattice,
        rational_isotropic,
        rational_partner,
        hyperbolic_plane,
        orthogonal_summand,
    ) -> None:
        self._reduction = reduction
        self._bezout_partner = bezout_partner
        self._rational_lattice = rational_lattice
        self._rational_isotropic = rational_isotropic
        self._rational_partner = rational_partner
        self._hyperbolic_plane = hyperbolic_plane
        self._orthogonal_summand = orthogonal_summand

    def reduction(self):
        return self._reduction

    def integral_line(self):
        return self.reduction().isotropic_sublattice()

    def integral_perpendicular(self):
        return self.reduction().orthogonal_complement()

    def integral_reduction(self):
        return self.reduction()

    def divisibility(self):
        inclusion = self.reduction().isotropic_embedding()
        generator = self.integral_line().module_generators()[0]
        return inclusion(generator).div()

    def bezout_partner(self):
        r"""Return integral ``h`` with ``b(e,h)=div(e)``."""
        return self._bezout_partner

    def rational_lattice(self):
        return self._rational_lattice

    def isotropic_vector(self):
        return self._rational_isotropic

    def dual_isotropic_vector(self):
        return self._rational_partner

    def hyperbolic_plane(self):
        return self._hyperbolic_plane

    def orthogonal_summand(self):
        return self._orthogonal_summand

    def __repr__(self) -> str:
        return f"Rational Witt decomposition of {self.reduction().isotropic_embedding().codomain()} along {self.integral_line()}"


class RankOneParabolicLeviExactSequence:
    r"""The exact sequence ``1 -> U_I -> P_I^1 -> M_I^1 -> 1``.

    Here ``P_I^1`` is the pointwise stabilizer of a primitive isotropic line,
    ``M_I^1`` is its represented image in ``O(K_I)``, and ``U_I`` is the
    kernel.  The target is the actual gluing-preserving image, not the whole
    orthogonal group of the reduction.
    """

    def __init__(self, reduction) -> None:
        self._reduction = reduction

    def reduction(self):
        return self._reduction

    def source(self):
        return self.reduction().pointwise_parabolic_subgroup()

    def kernel(self):
        return self.reduction().unipotent_kernel()

    def target(self):
        return self.reduction().pointwise_levi_image()

    @cached_method
    def projection(self):
        target = self.target()
        levi = self.reduction().levi_action()
        return SetMorphism(
            self.source().Mor(target),
            lambda isometry: target(levi(isometry)),
        )

    def lift(self, isometry):
        r"""Return the retained pointwise-parabolic lift of one target element."""
        return self.reduction().pointwise_levi_lift(isometry)

    def __repr__(self) -> str:
        return f"1 -> {self.kernel()} -> {self.source()} -> {self.target()} -> 1"


class IsotropicReductions(OwnedCategoryOverBaseRing):
    r"""Lattices \(K_I=I^\perp/I\) built from a totally isotropic \(\iota:I\hookrightarrow L\).

    An object is the quotient lattice itself, together with the data that
    built it: the embedding \(\iota\), the complement \(I^\perp\), the
    inclusion \(I\hookrightarrow I^\perp\) and the chosen lifts of the
    framing of \(K_I\) into \(I^\perp\).  The parabolic subgroup
    \(P_I=\operatorname{Stab}_{O(L)}(I)\) acts on \(K_I\) through its Levi
    quotient; the kernel of that action together with the restriction to
    \(I\) is the unipotent radical.
    """

    def an_object(self):
        r"""The reduction of \(U\oplus U\) by an isotropic line, which is \(U\)."""
        plane = Lattices(self.base_ring())("U")
        return (plane + plane).basis_vector(0).isotropic_reduction()

    @classmethod
    def _repr_object_names(cls) -> str:
        return "isotropic reductions"

    def super_categories(self):
        return [Lattices(self.base_ring())]

    def _call_(self, isotropic_embedding):
        r"""Return \(K_I=I^\perp/I\) for the totally isotropic embedding \(\iota:I\hookrightarrow L\).

        \(I\) pairs to zero against \(I^\perp\), so the form of \(L\)
        descends to the quotient of \(I^\perp\) by the image of \(I\).  The
        quotient is framed by its invariant-factor generators, lifted into
        \(I^\perp\); its Gram presentation is the form of \(L\) on those
        lifts.  The reduction is built in one construction that retains the
        embedding, the complement \(I^\perp\), the inclusion
        \(I\hookrightarrow I^\perp\), the lifts and the invariant-factor
        normalization of the quotient.
        """
        source = isotropic_embedding.domain()
        target = isotropic_embedding.codomain()
        ring = target.base_ring()
        assert ring is self.base_ring(), (
            f"an isotropic reduction in {self} reduces a lattice over {self.base_ring()}"
        )
        assert source.is_totally_isotropic(), (
            "an isotropic reduction is taken along a totally isotropic sublattice"
        )

        perpendicular = isotropic_embedding.orthogonal_complement()
        perpendicular_inclusion = perpendicular.inclusion()
        into_perpendicular = source.Mono(perpendicular)(
            lambda label: perpendicular_inclusion.lift(
                isotropic_embedding(source.module_generator(label))
            )
        )
        assert into_perpendicular.is_primitive(), (
            "the isotropic quotient is not free over the base ring; the selected "
            "isotropic sublattice is not primitive in its orthogonal complement"
        )
        quotient = into_perpendicular.cokernel()
        normalization = quotient.invariant_factor_form()
        quotient_module_generators = quotient.smith_form_module_generators()
        rank = int(quotient_module_generators.cardinality())
        labels = Sets.Δ[rank - 1]

        def lift(position):
            quotient_generator = quotient_module_generators[int(position)]
            coefficients = quotient_generator.parent().framing_coefficients(
                quotient_generator
            )
            return perpendicular.linear_combination(coefficients)

        lifts = finite_indexed_family(
            labels,
            lift,
            name="Isotropic-reduction lifts",
        )
        module = ring._fresh_free_module_on(labels)
        match rank:
            case 0:
                gram = _IdentityGram(module)
            case _:
                gram = tensor(
                    ring,
                    (),
                    (rank, rank),
                    (
                        perpendicular.b(lifts[i], lifts[j])
                        for i in range(rank)
                        for j in range(rank)
                    ),
                )
        return _lattice_object(
            Lattices(ring),
            module,
            gram,
            extra_categories=(self,),
            construction_data={
                "isotropic_embedding": isotropic_embedding,
                "orthogonal_complement": perpendicular,
                "isotropic_inclusion": into_perpendicular,
                "reduction_lifts": lifts,
                "reduction_normalization": normalization,
            },
        )

    class ParentMethods:
        def __init__(
            self,
            isotropic_embedding,
            orthogonal_complement,
            isotropic_inclusion,
            reduction_lifts,
            reduction_normalization,
            **rest,
        ) -> None:
            self._preamble_isotropic_embedding = isotropic_embedding
            self._preamble_orthogonal_complement = orthogonal_complement
            self._preamble_isotropic_inclusion = isotropic_inclusion
            self._preamble_reduction_lifts = reduction_lifts
            self._preamble_reduction_normalization = reduction_normalization
            super().__init__(**rest)

        def isotropic_embedding(self):
            r"""Return \(\iota:I\hookrightarrow L\), the embedding this reduces."""
            return self._preamble_isotropic_embedding

        def isotropic_sublattice(self):
            r"""Return \(I\), the totally isotropic sublattice."""
            return self.isotropic_embedding().domain()

        def orthogonal_complement(self):
            r"""Return \(I^\perp\hookrightarrow L\) as a subobject of the lattice."""
            return self._preamble_orthogonal_complement

        def isotropic_inclusion(self):
            r"""Return \(I\hookrightarrow I^\perp\)."""
            return self._preamble_isotropic_inclusion

        def inclusion(self):
            r"""Return \(I\hookrightarrow I^\perp\), the inclusion defining the quotient."""
            return self.isotropic_inclusion()

        @cached_method
        def rational_witt_decomposition(self):
            r"""Return the exact rational Witt decomposition for a rank-one isotropic line.

            If ``e`` generates ``I`` and ``d=div(e)``, an exact Bezout
            combination of the selected lattice frame gives ``h in L`` with
            ``b(e,h)=d``.  Over the fraction field put

            ``f = h/d - q(h)e/(2d^2)``.

            Then ``e^2=f^2=0`` and ``b(e,f)=1``.  The orthogonal complement of
            ``<e,f>`` is the rational anisotropic/reduction summand.  The
            integral line, perpendicular and quotient remain separately
            retained; no integral splitting is asserted.
            """
            line = self.isotropic_sublattice()
            if int(line.module_rank()) != 1:
                raise ValueError("the selected rational Witt construction currently starts from an isotropic line")
            ambient = self.isotropic_embedding().codomain()
            ring = ambient.base_ring()
            if _engine_ring(ring) is not SageZZ:
                raise ValueError("the selected Bezout Witt construction currently uses an integral ZZ-lattice")
            line_generator = line.module_generators()[0]
            isotropic = self.isotropic_embedding()(line_generator)
            labels = tuple(ambient.module_generating_set())
            pairings = tuple(ambient.b(isotropic, ambient.module_generator(label)) for label in labels)
            gcd_value = ring.zero()
            coefficients = []
            for pairing in pairings:
                new_gcd, old_coefficient, new_coefficient = gcd_value.xgcd(pairing)
                coefficients = [old_coefficient * coefficient for coefficient in coefficients]
                coefficients.append(new_coefficient)
                gcd_value = new_gcd
            divisibility = isotropic.div()
            if gcd_value != divisibility:
                coefficients = [-coefficient for coefficient in coefficients]
                gcd_value = -gcd_value
            if gcd_value != divisibility:
                raise ArithmeticError("the Bezout pairing witness has the wrong divisibility")
            bezout_partner = ambient.linear_combination({label: coefficient for label, coefficient in zip(labels, coefficients, strict=True) if coefficient})
            if ambient.b(isotropic, bezout_partner) != divisibility:
                raise ArithmeticError("the selected integral Witt partner has the wrong pairing")

            fraction_map = ring.fraction_field_map()
            rational = ambient.base_change(fraction_map)
            field = rational.base_ring()

            def rationalize(vector):
                coefficients = ambient.framing_coefficients(vector)
                return rational.linear_combination({label: fraction_map(coefficient) for label, coefficient in coefficients.items() if coefficient})

            rational_isotropic = rationalize(isotropic)
            rational_bezout = rationalize(bezout_partner)
            d = fraction_map(divisibility)
            two = field(2)
            correction = rational.q(rational_bezout) / (two * d * d)
            rational_partner = rational.scalar_multiple(field.one() / d, rational_bezout) - rational.scalar_multiple(correction, rational_isotropic)
            if rational.q(rational_partner) != field.zero():
                raise ArithmeticError("the rational Witt partner is not isotropic")
            if rational.b(rational_isotropic, rational_partner) != field.one():
                raise ArithmeticError("the rational Witt hyperbolic pair does not pair to one")
            hyperbolic_plane = rational.subobject_on((rational_isotropic, rational_partner))
            orthogonal_summand = hyperbolic_plane.orthogonal_complement()
            if int(orthogonal_summand.module_rank()) + 2 != int(rational.module_rank()):
                raise ArithmeticError("the rational Witt orthogonal summand has the wrong rank")
            return RankOneRationalWittDecomposition(
                self,
                bezout_partner,
                rational,
                rational_isotropic,
                rational_partner,
                hyperbolic_plane,
                orthogonal_summand,
            )

        def reduction_lifts(self):
            r"""Return the chosen lifts of the framing of \(K_I\) into \(I^\perp\)."""
            return self._preamble_reduction_lifts

        def quotient_lattice(self):
            r"""Return \(K_I=I^\perp/I\), which is this lattice."""
            return self

        @cached_method
        def projection(self):
            r"""Return the quotient morphism \(\pi:I^\perp\twoheadrightarrow K_I\)."""
            perpendicular = self.orthogonal_complement()
            quotient = self.isotropic_inclusion().cokernel()
            normalization = self._preamble_reduction_normalization
            normalized = normalization.codomain()
            normalized_labels = normalized.module_generating_set()
            labels = self.module_generating_set()
            presentation_projection = quotient.presentation_projection()

            def image(label):
                normalized_element = normalization.forward()(presentation_projection(perpendicular.module_generator(label)))
                return self.linear_combination(
                    {
                        labels[int(normalized_labels.ranking_map()(normalized_label))]: coefficient
                        for normalized_label, coefficient in normalized.framing_coefficients(normalized_element).items()
                        if coefficient
                    }
                )

            return perpendicular.module_category().Mor(perpendicular, self)(image)

        @cached_method
        def parabolic_subgroup(self):
            r"""Return \(P_I=\operatorname{Stab}_{O(L)}(I)\), the setwise stabilizer of \(I\)."""
            embedding = self.isotropic_embedding()
            return embedding.codomain().O().setwise_stabilizer(embedding)

        @cached_method
        def pointwise_parabolic_subgroup(self):
            r"""Return ``P_I^1``, the subgroup fixing the isotropic sublattice pointwise."""
            embedding = self.isotropic_embedding()
            return embedding.codomain().O().pointwise_stabilizer(embedding)

        @cached_method
        def levi_action(self):
            r"""Return \(P_I\to O(K_I)\), \(g\mapsto\bar g\), the action on \(I^\perp/I\).

            An isometry stabilizing \(I\) stabilizes \(I^\perp\), so it
            descends to the quotient.  The descended map is read on the
            chosen lifts.
            """
            perpendicular = self.orthogonal_complement()
            perpendicular_inclusion = perpendicular.inclusion()
            lifts = self.reduction_lifts()
            projection = self.projection()
            automorphisms = self.Aut()

            def descend(isometry):
                return automorphisms(lambda label: projection(perpendicular_inclusion.lift(isometry(perpendicular_inclusion(lifts(label))))))

            return SetMorphism(self.parabolic_subgroup().Mor(automorphisms), descend)

        @cached_method
        def _parabolic_levi_generator_pairs(self):
            r"""Return paired generators ``(g, gbar)`` for ``P_I -> O(K_I)``."""
            if not self.is_definite():
                raise ValueError("the exact represented Levi image currently requires a definite isotropic reduction")
            embedding = self.isotropic_embedding()
            source = embedding.domain()
            ambient = embedding.codomain()
            levi = self.levi_action()
            return tuple((generator, levi(generator)) for generator in ambient.O().isotropic_stabilizer_generators(source))

        @cached_method
        def levi_image_generators(self):
            r"""Return exact generators of the image of ``P_I -> O(K_I)`` when ``K_I`` is definite.

            The exact indefinite stabilizer computation supplies generators of the full stabilizer
            ``P_I = Stab_{O(L)}(I)``.  Descending those generators through
            :meth:`levi_action` therefore generates the exact Levi image.  The
            target is required to be definite so that its owned orthogonal
            group is a finite represented group in which the image subgroup
            can be materialized exactly.
            """
            return finite_ordered_set(tuple(image for _generator, image in self._parabolic_levi_generator_pairs()))

        @cached_method
        def levi_image(self):
            r"""Return the exact subgroup ``im(P_I -> O(K_I))`` for definite ``K_I``."""
            return self.Aut().subgroup_on(tuple(self.levi_image_generators()))

        @cached_method
        def _rank_one_combined_levi_lift_table(self):
            r"""Return lifts indexed by ``(action on I, action on K_I)`` for rank one."""
            line = self.isotropic_sublattice()
            if int(line.module_rank()) != 1:
                raise ValueError("the selected combined Levi table currently treats an isotropic line")
            embedding = self.isotropic_embedding()
            line_label = line.module_generating_set()[0]
            embedded = embedding(line.module_generator(line_label))
            ring = embedding.codomain().base_ring()

            def line_scalar(isometry):
                preimage = embedding.lift(isometry(embedded))
                coefficients = line.framing_coefficients(preimage)
                scalar = coefficients.get(line_label, ring.zero())
                if scalar not in (ring.one(), -ring.one()):
                    raise ArithmeticError("a rank-one parabolic generator does not act on I by a unit")
                return scalar

            levi = self.levi_action()
            generators = tuple(
                ambient_generator
                for ambient_generator, _target_generator in self._parabolic_levi_generator_pairs()
            )

            def combined_image(isometry):
                return (line_scalar(isometry), levi(isometry))

            def multiply(left, right):
                return (left[0] * right[0], left[1] * right[1])

            return self.parabolic_subgroup().finite_image_lifts(
                combined_image,
                generators=generators,
                multiply=multiply,
                image_bound=2 * int(self.Aut().cardinality()),
            )

        @cached_method
        def pointwise_levi_image(self):
            r"""Return the image of ``P_I^1`` in ``O(K_I)`` for a rank-one definite reduction."""
            ring = self.isotropic_embedding().codomain().base_ring()
            targets = tuple(target for (scalar, target) in self._rank_one_combined_levi_lift_table() if scalar == ring.one())
            return self.Aut().subgroup_on(targets)

        def pointwise_levi_lift(self, isometry):
            r"""Return a lift in ``P_I^1`` exactly when ``isometry`` lies in its Levi image."""
            if isometry.parent() is not self.Aut():
                raise ValueError("a pointwise Levi lift starts with an element of O(K_I)")
            if isometry not in self.pointwise_levi_image():
                return None
            ring = self.isotropic_embedding().codomain().base_ring()
            lifted = self._rank_one_combined_levi_lift_table()[ring.one(), isometry]
            if lifted not in self.pointwise_parabolic_subgroup():
                raise ArithmeticError("the retained pointwise Levi lift does not fix I")
            if self.levi_action()(lifted) != isometry:
                raise ArithmeticError("the retained pointwise Levi lift descends incorrectly")
            return lifted

        @cached_method
        def parabolic_levi_exact_sequence(self):
            r"""Return ``1 -> U_I -> P_I^1 -> M_I^1 -> 1`` in the represented rank-one regime."""
            return RankOneParabolicLeviExactSequence(self)

        @cached_method
        def _levi_lift_table(self):
            r"""Return one actual parabolic lift of every element of the finite Levi image."""
            image = self.levi_image()
            generators = tuple(
                ambient_generator
                for ambient_generator, _target_generator in self._parabolic_levi_generator_pairs()
            )
            witnesses = self.parabolic_subgroup().finite_image_lifts(
                self.levi_action(),
                generators=generators,
                image_bound=int(image.cardinality()),
            )
            if len(witnesses) != int(image.cardinality()):
                raise ArithmeticError("the paired parabolic generators did not enumerate the represented Levi image")
            return witnesses

        def levi_lift(self, isometry):
            r"""Return a parabolic lift of ``isometry`` exactly when the gluing permits one.

            For definite ``K_I`` the represented Levi image is finite, so this
            returns an actual witness in ``P_I`` rather than only a membership
            decision.  An element of ``O(K_I)`` outside that image has no lift
            through the retained arithmetic parabolic and returns ``None``.
            """
            if isometry.parent() is not self.Aut():
                raise ValueError("a Levi lift starts with an element of O(K_I)")
            if isometry not in self.levi_image():
                return None
            lifted = self._levi_lift_table()[isometry]
            if lifted not in self.parabolic_subgroup():
                raise ArithmeticError("a retained Levi lift is not parabolic")
            if self.levi_action()(lifted) != isometry:
                raise ArithmeticError("a retained Levi lift descends incorrectly")
            return lifted

        @cached_method
        def unipotent_kernel(self):
            r"""Return \(U_I=\ker(P_I\to GL(I)\times O(K_I))\), the unipotent radical."""
            self.isotropic_embedding()
            levi = self.levi_action()
            identity = self.Aut().one()
            return self.pointwise_parabolic_subgroup().predicate_subgroup(lambda isometry: levi(isometry) == identity, "g fixes I pointwise and acts trivially on I^perp/I")

        def lift_isometry(self, isometry):
            r"""Return \(g\in P_I\) with \(\bar g=\) ``isometry``, when \(L\) splits along the lifts.

            The chosen lifts span \(K'\subseteq I^\perp\), a copy of
            \(K_I\).  When \(K'\) is primitive and \(M=K'^\perp\) is
            unimodular, \(L=M\perp K'\), so \(g=\mathrm{id}_M\perp\sigma\)
            lies in \(P_I\) and has the required Levi image; \(M\) then
            contains \(I\).  Without such a splitting the Levi quotient need
            not lift, which the assertion states.

            Unimodularity of \(M\) is what makes the splitting computable:
            the correlation \(M\to M^\vee\) is then an isomorphism, and the
            \(M\)-component of \(x\in L\) is the correlation's inverse
            applied to \(b(x,-)|_M\).
            """
            automorphisms = self.Aut()
            assert isometry.parent() is automorphisms, "the isometry to lift is an element of O(K_I)"
            lattice = self.isotropic_embedding().codomain()
            perpendicular_inclusion = self.orthogonal_complement().inclusion()
            lifts = self.reduction_lifts()
            labels = self.module_generating_set()
            embedded_lifts = finite_indexed_family(
                labels,
                lambda label: perpendicular_inclusion(lifts(label)),
                name="Embedded isotropic-reduction lifts",
            )
            complement = lattice.subobject_on(embedded_lifts)
            unimodular_summand = complement.orthogonal_complement()
            assert complement.is_primitive() and unimodular_summand.is_unimodular(), (
                "no represented splitting L = M perp K' along the chosen lifts; the Levi quotient need not lift"
            )
            complement_inclusion = complement.inclusion()
            summand_inclusion = unimodular_summand.inclusion()
            into_complement = self.module_category().Mor(self, complement)(lambda label: complement_inclusion.lift(embedded_lifts(label)))
            correlation = unimodular_summand.correlation_isomorphism()
            summand_dual = correlation.forward().codomain()

            def summand_component(vector):
                covector = summand_dual.linear_combination(
                    {
                        label: coefficient
                        for label in summand_dual.module_generating_set()
                        if (
                            coefficient := lattice.b(
                                vector,
                                summand_inclusion(unimodular_summand.module_generator(label)),
                            )
                        )
                    }
                )
                return correlation.inverse()(covector)

            def image(label):
                vector = lattice.module_generator(label)
                fixed_part = summand_component(vector)
                embedded_fixed = summand_inclusion(fixed_part)
                moved_part = into_complement.lift(complement_inclusion.lift(vector - embedded_fixed))
                return embedded_fixed + complement_inclusion(into_complement(isometry(moved_part)))

            lifted = lattice.O()(image)
            assert lifted in self.parabolic_subgroup(), "the assembled map does not stabilize I; the chosen lifts do not span a splitting"
            assert self.levi_action()(lifted) == isometry, "the assembled map descends to the wrong isometry of I^perp/I"
            return lifted


class NoncrystallographicRootLattices(OwnedCategoryOverBaseRing):
    r"""Finite noncrystallographic root lattices over their exact coefficient order."""

    def an_object(self):
        return Lattices.root_lattice("H", 3)

    @classmethod
    def _repr_object_names(cls):
        return "noncrystallographic root lattices"

    def super_categories(self):
        return [Lattices(self.base_ring()).FinitelyGenerated().Nondegenerate().Even()]

    class ParentMethods:
        def __init__(self, coxeter_type, **rest) -> None:
            self._preamble_coxeter_type = coxeter_type
            super().__init__(**rest)

        def coxeter_type(self):
            return self._preamble_coxeter_type

        def simple_roots(self):
            return self.module_generators()

        @cached_method
        def roots(self):
            r"""Return the finite H-root system from its Coxeter reflection group.

            Sage's maintained finite Coxeter-group implementation computes all roots
            in the basis of simple roots.  The H3/H4 coefficients lie in the
            golden integer order defining this lattice; crossing them through
            that order both preserves the selected framing and rejects an
            accidental nonintegral coordinate.
            """
            family, rank = self.coxeter_type()
            coxeter = Groups.Coxeter(
                [family, rank],
                base_ring=self.base_ring().fraction_field(),
            )
            backend_roots = _engine_group(coxeter).roots()
            ring = self.base_ring()
            engine_order = _engine_ring(ring)
            labels = tuple(self.module_generating_set())
            return finite_ordered_set(
                tuple(
                    self.linear_combination(
                        {
                            label: _owned_engine_element(ring,
                                engine_order(coefficient)
                            )
                            for label, coefficient in zip(
                                labels, tuple(root), strict=True
                            )
                            if coefficient
                        }
                    )
                    for root in backend_roots
                )
            )

        def coxeter_number(self):
            family, rank = self.coxeter_type()
            if family != "H" or rank not in (3, 4):
                raise ValueError("the represented noncrystallographic Coxeter number is for H3 and H4")
            return self.base_ring().base_ring()(10 if rank == 3 else 30)

        def simple_reflections(self):
            return finite_ordered_set(
                tuple(self.reflection(root) for root in self.simple_roots())
            )


class RootLattices(OwnedCategory):
    r"""Negative-definite ADE root lattices with a chosen simple-root framing."""

    def an_object(self):
        r"""Return the canonical ``A2`` root lattice as an inhabitant."""
        return Lattices(_own_ring(SageZZ))("A2")

    @classmethod
    def _repr_object_names(cls):
        return "root lattices"

    def super_categories(self):
        return [Lattices(_own_ring(SageZZ)).FinitelyGenerated().Nondegenerate().Even()]

    class ParentMethods:
        def __init__(self, cartan_type, **rest) -> None:
            self._preamble_cartan_type = cartan_type
            super().__init__(**rest)

        def cartan_type(self):
            return self._preamble_cartan_type

        def simple_roots(self):
            r"""Return the selected framing, which is the chosen simple system."""
            return self.module_generators()

        def coxeter_number(self):
            cartan_type = self.cartan_type()
            if not cartan_type.is_irreducible():
                raise ValueError("a reducible root system has one Coxeter number per irreducible component")
            return cartan_type.coxeter_number()

        def highest_root(self):
            r"""Return the highest root in the selected simple-root framing."""
            cartan_type = self.cartan_type()
            if not cartan_type.is_irreducible():
                raise ValueError("a reducible root system has one highest root per irreducible component")
            coefficients = tuple(RootSystem(cartan_type).root_lattice().highest_root().to_vector())
            return sum(
                (
                    self.scalar_multiple(self.base_ring()(int(coefficient)), root)
                    for coefficient, root in zip(
                        coefficients, self.simple_roots(), strict=True
                    )
                ),
                self.zero(),
            )

        def simple_reflections(self):
            return finite_ordered_set(
                tuple(self.reflection(root) for root in self.simple_roots())
            )

        def fundamental_weights(self):
            r"""Return the weights dual to the simple coroots."""

            norm = self.simple_roots()[0].norm()
            if norm not in (2, -2):
                raise ValueError(f"a simply-laced root framing has simple-root square +/-2, got {norm}")
            sign = norm // self.base_ring()(2)
            return FiniteOrderedSets().from_indexed(
                self.dual_basis(),
                lambda weight: weight.parent().scalar_multiple(sign, weight),
            )

    class ElementMethods:
        def is_positive_root(self) -> bool:
            return bool(self.is_root() and all(coefficient >= 0 for coefficient in self.monomial_coefficients().values()))

        def is_negative_root(self) -> bool:
            return bool((-self).is_positive_root())

        def height(self):
            return sum(
                self.monomial_coefficients().values(),
                self.parent().base_ring().zero(),
            )

        def coroot(self):
            r"""Return ``alpha^vee = 2*b(alpha,-)/b(alpha,alpha)`` in ``L^#``."""
            parent = self.parent()
            if not self.is_root():
                raise ValueError("the coroot in this lattice is defined for an integral root")
            norm = self.norm()
            two = parent.base_ring()(2)
            dual_lattice = parent.dual_lattice()
            return dual_lattice.linear_combination(
                {
                    label: two * parent.module_generator(label).b(self) / norm
                    for label in parent.module_generating_set()
                    if parent.module_generator(label).b(self) != 0
                }
            )
