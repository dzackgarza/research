r"""Lattices.

Sage does not define a category of (quadratic-form) lattices.  Sage's
:func:`~sage.modules.free_quadratic_module_integer_symmetric.IntegralLattice`
constructs a free quadratic module; the order-theoretic category is
:class:`~sage.categories.lattice_posets.LatticePosets`.  This module
owns the missing category, following Sage's category primer
(``super_categories``, ``ParentMethods``, ``ElementMethods``) and the
``Category_over_base_ring`` parameterization.  A lattice is a free
`R`-module with a form.  The Python class does not extend Sage's
module classes; it keeps an internal module reference.
The classcall is the category over a ring.  Objects are constructed by
calling that category.
"""

from sage.arith.misc import gcd
from sage.categories.category import Category
from sage.categories.morphism import SetMorphism
from sage.combinat.root_system.root_system import RootSystem
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.misc.unknown import Unknown
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.parent import Parent

from collections.abc import Hashable, Sequence
from typing import overload

from dzack_research.preamble.categories._lattice import diagonal_gram as diagonal_gram
from dzack_research.preamble.categories._lattice import signature_pair, signature_pairs
from dzack_research.preamble.categories._lattice import (
    _BiproductGram,
    _ColimitGram,
    _DiagonalGram,
    _IdentityGram,
    _PairingGram,
    _ScaledGram,
    Lattice,
    colimit_lattice,
    discriminant_of_gram,
    generator_pairings,
    lattice,
    lattice_latex,
    orthogonal_sum,
    scale_gram_tensor,
    signature_pair_of_gram,
)
from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import DirectSumDecomposition
from dzack_research.preamble.categories.definite_lattices import (
    babai,
    bkz_reduction,
    center_density,
    closest_vector,
    contact_polytope,
    covering_radius,
    gaussian_heuristic,
    hadamard_ratio,
    hermite_invariant,
    hkz_reduction,
    kissing_number,
    lll_reduction,
    minimum,
    packing_density,
    packing_radius,
    root_sublattice,
    roots,
    roots_of_square,
    shortest_vectors,
    successive_minima,
    theta_series,
    vectors_of_square,
    vectors_of_square_and_divisibility,
    voronoi_cell,
    voronoi_relevant_vectors,
)
from dzack_research.preamble.categories.forms.forms import BilinearForms
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.group.predicate_subgroups import predicate_subgroup
from dzack_research.preamble.categories.isotropic_orbits import (
    IsotropicFlag,
    primitive_isotropic_subobject,
)
from dzack_research.preamble.categories import lattice_engines
from dzack_research.preamble.categories.lattice_morphisms import (
    LatticeEmbeddingHomset,
    LatticeHomset,
    LatticeIsometryHomset,
    lattice_embedding_homset,
    lattice_homset,
    lattice_isometry_homset,
)
from dzack_research.preamble.categories.modules.framed.formed.discriminant_modules import (
    DiscriminantBilinearModules,
    DiscriminantModule,
    DiscriminantQuadraticModules,
)
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    BilinearForm,
    SymmetricBilinearFormModules,
    form_embedding,
)
from dzack_research.preamble.categories.modules.framed.formed.torsion_form_modules import (
    _form_gram_on,
    _relations_among_generators,
    _torsion_form_modules,
    torsion_form_isometry,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    BasedFreeModule,
    MatrixSpace,
    _module_subobject_constructor_data,
    _span_basis_elements,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    _solve_left_integrally,
    module_coefficients,
    module_embedding,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    ModuleSubobjects,
)
from dzack_research.preamble.categories.modules.pure.torsion_modules import _torsion_module_presented_by_matrix
from dzack_research.preamble.categories.rational_lattices import refine_rational_lattice
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
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
from dzack_research.preamble.categories.vector_orbits import (
    VectorPrimitiveExtension,
    definite_complement_extensions,
    gluing_route_discriminant_classes,
    stable_complement_root_reflections,
)
from dzack_research.preamble.tensors.tensor import _engine_component_matrix


def nikulin_invariants(rank, discriminant_length, delta):
    r"""Return \((r,a,\delta)\) as a point of \(\mathbb N^3\)."""

    return (NN**3)((int(rank), int(discriminant_length), int(delta)))
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
    IsoCategoryConstruction,
    MonoCategoryConstruction,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.tensors.tensor import Tensor, tensor

_Rings = OwnedRings()


_INDECOMPOSABLE_NAMES = {}


class LatticeHomCategoryConstruction(HomCategoryConstruction):
    r"""The strict form-preserving Hom categories of lattices."""

    def fixed_category_class(self):

        return LatticeHomset


class LatticeMonoCategoryConstruction(MonoCategoryConstruction):
    r"""The form-preserving monomorphisms of lattices."""

    def fixed_category_class(self):

        return LatticeEmbeddingHomset


class LatticeIsoCategoryConstruction(IsoCategoryConstruction):
    r"""The isometries of lattices."""

    def fixed_category_class(self):

        return LatticeIsometryHomset


def _gram_key(gram):
    return tuple(tuple(row) for row in gram.components())


def register_indecomposable_gram(name, gram):
    r"""Register an exact Gram matrix under its indecomposable display name."""
    _INDECOMPOSABLE_NAMES.setdefault(_gram_key(gram), str(name))


def register_indecomposable(name, lattice):
    r"""Register an indecomposable live lattice by exact Gram equality."""
    if lattice.is_decomposable():
        raise ValueError("only an indecomposable lattice can name one Gram block")
    register_indecomposable_gram(name, lattice.gram_tensor())


def indecomposable_name(lattice):
    r"""Return the registered exact or scalar-twist name, if one exists."""
    gram = lattice.gram_tensor().change_ring(_own_ring(SageZZ))
    exact = _INDECOMPOSABLE_NAMES.get(_gram_key(gram))
    if exact is not None:
        return exact
    content = gcd(gram.list())
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
            [
                [integers(int(gram[i, j]) // divisor) for j in range(rank)]
                for i in range(rank)
            ],
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
    r"""Return the canonical lattice subobject on a finite span basis."""

    ring = module.base_ring()
    rank = int(basis.cardinality())
    labels, embedded, lift = _module_subobject_constructor_data(module, basis)
    category = module.lattice_category()
    if rank == 0:
        prototype = category(0)
    else:
        gram = tensor(
            ring,
            (),
            (rank, rank),
            (
                module.b(basis.unrank(i), basis.unrank(j))
                for i in range(rank)
                for j in range(rank)
            ),
        )
        prototype = category(gram, module_generators=labels)

    def inclusion_factory(source):
        module_inclusion = module_embedding(source, module, embedded)
        return source.Emb(module)(module_inclusion)

    extra_categories = ()
    construction_data = ()
    if root_cartan_type is not None:
        extra_categories = (RootLattices(),)
        construction_data = (("cartan_type", root_cartan_type),)
    source = Lattice(
        prototype._module,
        prototype.gram_tensor(),
        category,
        prototype._sage_lattice,
        extra_categories=extra_categories,
        construction_data=construction_data,
        subobject_ambient=module,
        subobject_generator_images=embedded,
        subobject_lift=lift,
        subobject_inclusion_factory=inclusion_factory,
    )
    return category._refine_lattice_object(source)


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
        self._jordan_blocks = tuple(
            tuple(integers(entry) for entry in block)
            for block in jordan_blocks
        )

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
            [
                [_engine_element(integers, entry) for entry in block]
                for block in self.jordan_blocks()
            ],
        )

    def excess(self):
        integers = self.prime().parent()
        return integers._from_engine_element(SageZZ(self._engine().excess()))

    def level(self):
        integers = self.prime().parent()
        return integers._from_engine_element(SageZZ(self._engine().level()))

    def norm(self):
        integers = self.prime().parent()
        return integers._from_engine_element(SageZZ(self._engine().norm()))

    def number_of_blocks(self):
        return self.prime().parent()(len(self.jordan_blocks()))

    def __eq__(self, other):
        return (
            isinstance(other, LocalGenusSymbol)
            and self.prime() == other.prime()
            and self.jordan_blocks() == other.jordan_blocks()
        )

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return repr(self._engine())


class Genus:
    r"""The genus determined by signature and discriminant quadratic form."""

    def __init__(self, signature_pair, discriminant_quadratic_form) -> None:
        self._signature_pair = signature_pair
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
                [
                    form.q(left).parent().lift(form.q(left))
                    if i == j
                    else form.b(left, right).parent().lift(form.b(left, right))
                    for j, right in enumerate(generators)
                ]
                for i, left in enumerate(generators)
            ],
        )
        engine_form = TorsionQuadraticForm(_engine_component_matrix(written))
        if int(engine_form.cardinality()) != int(form.cardinality()):
            raise ArithmeticError(
                "reconstructing the genus engine changed the discriminant-group cardinality"
            )
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
        return bool(
            self._engine_form().is_genus(
                self._engine_signature_pair(), even=True
            )
        )

    def determinant(self):
        r"""Return the determinant of a representative of this genus."""
        integers = _own_ring(SageZZ)
        return integers._from_engine_element(SageZZ(self._engine().determinant()))

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
        rows = [
            [integers._from_engine_element(entry) for entry in row]
            for row in representative.rows()
        ]
        return Lattices(integers)(rows)

    def representatives(self):
        r"""Return the owned representatives enumerated by the exact backend."""
        integers = _own_ring(SageZZ)
        return tuple(
            Lattices(integers)(
                [
                    [integers._from_engine_element(entry) for entry in row]
                    for row in representative.rows()
                ]
            )
            for representative in self._engine().representatives()
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
            raise ValueError(
                "the finite orthogonal-group mass is defined here for definite genera"
            )
        rationals = _own_ring(SageQQ)
        return rationals._from_engine_element(SageQQ(self._engine().mass()))

    def __eq__(self, other):
        if not isinstance(other, Genus):
            return NotImplemented
        return (
            self.signature_pair() == other.signature_pair()
            and self.discriminant_form() == other.discriminant_form()
        )

    def __ne__(self, other):
        result = self.__eq__(other)
        return result if result is NotImplemented else not result

    def __repr__(self):
        return (
            f"Genus of even integral lattices with signature {self.signature_pair()} "
            f"and discriminant order {self.discriminant_form().cardinality()}"
        )


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
        [Category of framed free modules]

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
        try:
            ring = _own_ring(args[0])
        except TypeError as error:
            raise TypeError(
                "Lattices(R) takes a ring R; construct an object as Lattices(R)(data)"
            ) from error
        if ring not in _Rings:
            raise TypeError("Lattices(R) takes a ring R; construct an object as Lattices(R)(data)")
        from dzack_research.preamble.categories.modules.pure.modules import _is_group_algebra

        if cls is Lattices and _is_group_algebra(ring):
            # Lattices(R[G]): lattices over R with a form-preserving G-action.
            from dzack_research.preamble.categories.modules.group_modules.group_lattices import (
                LatticesOverGroupAlgebra,
            )

            return LatticesOverGroupAlgebra(ring)
        return super().__classcall__(cls, ring)

    @overload  # type: ignore[override]  # the stub promises a SageObject; the object type of this category is its provider class
    def __call__(self, data: str | Sequence[Sequence[object]], *args: object, **options: object) -> "FiniteRankLattices.ParentMethods": ...

    @overload
    def __call__(self, data: object, *args: object, **options: object) -> "Lattices.ParentMethods": ...

    def __call__(self, data: object, *args: object, **options: object) -> "Lattices.ParentMethods":
        r"""Return the lattice that ``data`` presents; a lattice in this category is returned as is.

        A named form or a Gram given by rows has finite rank.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: L = Lattices(ZZ)("U")
            sage: Lattices(ZZ)(L) is L
            True
        """
        lattice = super().__call__(data, *args, **options)
        if not isinstance(lattice, Lattices.ParentMethods):
            raise TypeError(f"{lattice!r} is not a lattice in {self}")
        return lattice

    def _call_(  # type: ignore[override]  # the stub promises a SageObject; the object type of this category is its provider class
        self,
        data: object,
        basis: None = None,
        names: str | Sequence[str] | None = None,
        form: Tensor | None = None,
        module_generators: Sequence[Hashable] | Parent | None = None,
    ) -> "Lattices.ParentMethods":
        r"""Construct a lattice in this category.

        This is Sage's category constructor: ``C(x)`` for ``C`` a
        category.  ``Lattices(ZZ)("U")`` is the hyperbolic plane over
        `\ZZ`.  ``Lattices(R)(R^n)`` is the standard Euclidean lattice
        of rank `n`; ``Lattices(R)(R^{\mathbb N})`` is its colimit.
        A pairing Gram is a lattice: ``C(diagonal_gram(R^NN, {0: -1}))``.
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
            sage: e = I2.module_generator(0)
            sage: e
            e_0
            sage: e.to_tuple()
            (1, 0)
            sage: e*e, e.b(I2.module_generator(1))
            (1, 0)
            sage: I2((1, 0))
            e_0
            sage: Linf = Lattices(ZZ)(ZZ^NN)
            sage: Linf
            Integral lattice of rank +Infinity and signature (+Infinity, 0)
            sage: Linf((1, 0, 0, 1))
            e_0 + e_3
            sage: from dzack_research.preamble.categories.lattices import diagonal_gram
            sage: Lattices(ZZ)(diagonal_gram(ZZ^NN, {0: -1}))
            Integral lattice of rank +Infinity and signature (+Infinity, 1)
        """

        return lattice(
            data,
            basis,
            names=names,
            form=form,
            module_generators=module_generators,
            category=self,
        )

    def _refine_lattice_object(self, lattice):
        r"""Attach the lattice-property subcategories decidable from its form."""
        categories = []
        if lattice.module_rank() != Infinity:
            categories.append(FiniteRankLattices(lattice.base_ring()))
        if lattice.is_nondegenerate():
            categories.append(NondegenerateLattices(lattice.base_ring()))
        try:
            is_even = lattice.is_even()
        except NotImplementedError:
            is_even = False
        if is_even:
            categories.append(EvenLattices(lattice.base_ring()))
        return refine(lattice, categories) if categories else lattice

    def _refine_root_lattice(self, lattice, cartan_type):
        r"""Return a root-structured copy with constructor-owned Cartan data."""
        if lattice in RootLattices() and lattice.cartan_type() == cartan_type:
            return lattice
        result = Lattice(
            lattice._module,
            lattice.gram_tensor(),
            self,
            lattice._sage_lattice,
            extra_categories=(RootLattices(),),
            construction_data=(("cartan_type", cartan_type),),
            subobject_ambient=lattice.__dict__.get("_preamble_subobject_ambient"),
            subobject_generator_images=lattice.__dict__.get(
                "_preamble_subobject_generator_images"
            ),
            subobject_lift=lattice.__dict__.get("_preamble_subobject_lift"),
            subobject_inclusion_factory=lattice.__dict__.get(
                "_preamble_subobject_inclusion_factory"
            ),
            subobject_verify_linearity=lattice.__dict__.get(
                "_preamble_subobject_verify_linearity", True
            ),
        )
        return self._refine_lattice_object(result)

    def colimit(self, stage):
        r"""Return \(\operatorname{colim}_n \mathrm{stage}(n)\) along \(x\mapsto(x,0)\).

        ``stage(n)`` is a rank-\(n\) lattice in this category.  The
        odd unimodular lattice \(I_{\infty,1}\) is the colimit of
        \(I_{n,1}\).

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: C = Lattices(ZZ)
            sage: C.colimit(lambda n: C(ZZ^n))
            Integral lattice of rank +Infinity and signature (+Infinity, 0)
        """

        return colimit_lattice(stage, category=self)

    def an_object(self):
        r"""The hyperbolic plane U."""
        return self("U")

    @cached_method
    def super_categories(self):
        r"""
        Return the immediate super categories of ``self``.

        A lattice is a free `R`-module with a form.  Immediate supers
        only, as required by the Sage category primer.

        EXAMPLES::

            sage: from dzack_research.preamble.categories.lattices import Lattices
            sage: Lattices(ZZ).super_categories()
            [Category of framed free modules]
        """

        return [
            FramedFreeModules(self.base_ring()),
            SymmetricBilinearFormModules(self.base_ring()),
        ]

    _HomCategory = LatticeHomCategoryConstruction
    _MonoCategory = LatticeMonoCategoryConstruction
    _IsoCategory = LatticeIsoCategoryConstruction

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
        """Operations generic to every lattice."""

        def lattice_category(self):
            r"""Return the base-ring lattice category owning this object."""
            return Lattices(self.base_ring())

        def subobject_on(self, module_generating_set):
            r"""Return the span with the restricted lattice form."""

            basis = _span_basis_elements(self, module_generating_set)
            return _lattice_subobject_spanning(self, basis)

        def _root_subobject_on(self, module_generating_set, cartan_type):
            r"""Return the selected root sublattice with Cartan data at construction."""
            basis = _span_basis_elements(self, module_generating_set)
            return _lattice_subobject_spanning(
                self,
                basis,
                root_cartan_type=cartan_type,
            )

        @cached_method
        def form(self):
            r"""Return the existing lattice pairing as a bilinear-form morphism."""

            return BilinearForms(self, self.base_ring())(
                lambda left, right: self.b(left, right)
            )

        def value_module(self):
            return self.base_ring()

        def unformed_module(self):
            r"""Read this same parent at its weaker module level."""
            return self

        @cached_method
        def forget_form_morphism(self):

            return module_homset(self, self).identity()

        @cached_method
        def equip_form_morphism(self):
            return self.forget_form_morphism()

        def Mor(self, codomain, category=None):
            lattices = Lattices(self.base_ring())
            if category is None or category.is_subcategory(lattices):
                return lattice_homset(self, codomain)
            from sage.categories.homset import Hom as SageHom
            return SageHom(self, codomain, category)

        def _Hom_(self, codomain, category=None):

            lattices = Lattices(self.base_ring())
            if codomain in lattices and (
                category is None or category.is_subcategory(lattices)
            ):
                return lattice_homset(self, codomain)
            return super()._Hom_(codomain, category)

        def Emb(self, codomain):
            r"""Return the set of form-preserving embeddings into ``codomain``."""

            return lattice_embedding_homset(self, codomain)

        def Isom(self, codomain):
            r"""Return the set of isometries to ``codomain``."""

            return lattice_isometry_homset(self, codomain)

        def Aut(self):
            r"""Return ``Isom(L,L)``, the orthogonal automorphism homset."""
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

        @cached_method
        def special_orthogonal_group(self):
            r"""Return ``SO(L)=ker(det:O(L)->{+-1})`` as a predicate subgroup."""

            return predicate_subgroup(
                self.Aut(),
                lambda automorphism: automorphism.determinant() == 1,
                "det(g)=1",
                character_data={"determinant_kernel": True},
            )

        SO = special_orthogonal_group

        def spinor_kernel_subgroup(self):
            r"""Return the kernel of the real spinor-norm sign on ``O(L)``."""

            return predicate_subgroup(
                self.Aut(),
                lambda automorphism: automorphism.real_spinor_norm_sign() == 1,
                "real spinor norm(g)=+1",
                character_data={"spinor_kernel": True},
            )

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
                raise ValueError(
                    f"the component character is defined in signature (1,n); got {(positive, negative)}"
                )

            target = OwnedGroups().C(2)
            exchange = target.group_generators().unrank(0)
            return SetMorphism(
                self.Aut().Mor(target),
                lambda isometry: target.one()
                if isometry.preserves_positive_cone()
                else exchange,
            )

        def positive_cone_subgroup(self):
            r"""Return the positive-cone-preserving subgroup in signature ``(1,n)``."""
            _signature = self.signature_pair()
            positive, negative = _signature.first(), _signature.second()
            integers = positive.parent()
            if positive != integers.one() or negative < integers.one():
                raise ValueError(
                    f"positive_cone_subgroup requires signature (1,n); got {(positive, negative)}"
                )

            return predicate_subgroup(
                self.Aut(),
                lambda automorphism: automorphism.preserves_positive_cone(),
                "g preserves the positive cone",
            )

        @cached_method
        def biproduct_factors(self):
            r"""Return the indexed family of factors when this lattice was built by ``+``."""

            gram = self.gram_tensor()
            if not isinstance(gram, _BiproductGram):
                raise ValueError("this lattice has no represented biproduct factors")

            return indexed_family(
                Sets.Δ[1],
                lambda index: gram._left if int(index) == 0 else gram._right,
                name=f"Biproduct factors of {self}",
            )

        @cached_method
        def decomposition(self):
            r"""Return the represented direct-sum decomposition, if present."""
            try:
                factors = self.biproduct_factors()
            except ValueError:
                return None

            return DirectSumDecomposition(self, factors)

        def is_decomposable(self):
            return self.decomposition() is not None

        def summands(self):
            decomposition = self.decomposition()
            if decomposition is None:
                raise ValueError("this lattice has no represented direct-sum decomposition")
            return self._preamble_direct_sum_summands

        def indecomposable_name(self):
            return indecomposable_name(self)

        def indecomposable_summands(self):
            r"""Return the family of indecomposable summands, in order.

            The biproduct of three lattices associates, so its immediate
            factors are two, not three.  This descends through the represented
            decompositions until every summand is indecomposable.
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

            The live isometry homset preserves ``Unknown`` outside implemented
            exact regimes instead of treating matching coarse invariants as a
            proof.
            """
            empty = self.Isom(other).is_empty()
            if empty is Unknown:
                return Unknown
            return not empty

        def similarity_homset(self, other, scale):
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
            by the exact isometry homset backend.
            """
            target = self if codomain is None else codomain
            homset = self.similarity_homset(target, scale)
            if images is None:
                return homset.an_element()
            return homset(images)

        def identity_morphism(self):
            r"""Return ``id_L`` in the lattice endomorphism homset.

            The morphism is a callable on generators, not an enumerated
            image of every \(e_i\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Iinf = Lattices(ZZ)(ZZ^NN)
                sage: f = Iinf.identity_morphism()
                sage: f(Iinf.module_generator(7))
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
            return self._gram

        def gram_matrix(self):
            r"""Return the matrix of \(L\to\operatorname{Hom}_R(L,R)\) in the framing and its dual.

            The Gram tensor is the form; this is its coordinate presentation,
            the matrix of :meth:`algebraic_correlation_morphism` as an element
            of \(\operatorname{Hom}_R(F(S),F(S^\vee))\), so its entry at
            \((i,j)\) is \(b(e_i,e_j)\) and its determinant is the
            discriminant.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U").gram_matrix().determinant()
                -1
                sage: Lattices(ZZ)("A2").gram_matrix().determinant()
                3
            """
            return self.algebraic_correlation_morphism().matrix()

        def module_generating_set(self):
            r"""Return the labels of the distinguished free-module framing.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)(ZZ^2).module_generating_set()
                {e_0, e_1}
                sage: Lattices(ZZ)(ZZ^NN).module_generating_set()
                {e_i : i in NN} subset of SR
            """
            return self._indices

        @cached_method
        def module_generators(self):

            return indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name="Lattice-generator family",
            )

        def module_generator(self, index):
            r"""Return the module generator indexed by ``index``.

            ``index`` is an element of the generating set, or an integer
            position in that enumerated set.  The default generating set
            is the formal symbols \(e_i\in\mathrm{SR}\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: I2.module_generator(0)
                e_0
                sage: I2.module_generator(0).to_tuple()
                (1, 0)
            """
            keys = self.module_generating_set()
            if index not in keys:
                index = keys.unrank(int(index))
            return self.element_class(self, self._module.module_generator(index))

        def b(self, left, right):
            r"""Return the bilinear pairing \(b(v,w)\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: e, f = U.module_generator(0), U.module_generator(1)
                sage: U.b(e, f)
                1
            """
            assert left.parent() is self
            assert right.parent() is self
            gram = self.gram_tensor()
            if self.module_rank().is_finite():
                return gram.contract(left.to_vector(), right.to_vector())
            return gram(left._vector, right._vector)

        def q(self, vector):
            r"""Return the quadratic form \(q(v)=b(v,v)\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: I2.q(I2.module_generator(0))
                1
                sage: A2 = Lattices(ZZ)("A2")
                sage: A2.q(A2.module_generator(0))
                -2
            """
            return self.b(vector, vector)

        def module_rank(self):
            r"""Return the rank of this lattice as a free module.

            The answer is a cardinal, so a lattice on a countably infinite
            generating set answers with an aleph rather than refusing.

            EXAMPLES::

                sage: from dzack_research.preamble.all import *
                sage: Lattices(ZZ)(FreeModule(ZZ, 2)).module_rank()
                2
                sage: Lattices(ZZ)(FreeModuleFunctor(ZZ)(NN)).module_rank()
                ℵ_0
            """
            return self._module.module_rank()

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

            return signature_pair_of_gram(self.gram_tensor())

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

            return discriminant_of_gram(self.gram_tensor())

        def determinant(self):
            r"""Return the determinant of a finite-rank lattice form."""
            if not self.module_rank().is_finite():
                raise TypeError("the determinant requires a finite-rank lattice")

            rank = int(self.module_rank())
            gram = self.gram_tensor()
            matrix = MatrixSpace(self.value_module(), rank).from_rows(
                (gram[row, column] for column in range(rank))
                for row in range(rank)
            )
            return matrix.determinant()

        def is_nondegenerate(self) -> bool:
            r"""Return whether the correlation map has zero radical."""

            gram = self.gram_tensor()
            match gram:
                case _IdentityGram():
                    return True
                case _DiagonalGram():
                    if gram._default == 0:
                        return False
                    return all(value != 0 for value in gram._exceptions.values())
                case _ScaledGram():
                    return gram._scalar != 0 and Lattices(self.base_ring())(gram._gram).is_nondegenerate()
                case _BiproductGram():
                    return gram._left.is_nondegenerate() and gram._right.is_nondegenerate()
                case _ColimitGram():
                    # The represented colimit forms used here are orthogonal
                    # unions of nondegenerate finite stages.
                    return all(stage.is_nondegenerate() for stage in gram._objects)
                case _:
                    if not self.module_rank().is_finite():
                        raise NotImplementedError("nondegeneracy of this infinite Gram presentation is not decided")
                    return self.determinant() != 0

        def is_even(self) -> bool:
            r"""Return whether ``b(x,x)`` lies in ``2R`` for every lattice vector."""
            ring = self.base_ring()
            try:
                twice_ring = ring.ideal(ring(2))
                def is_twice(value) -> bool:
                    return ring(value) in twice_ring
            except (AttributeError, NotImplementedError, TypeError):
                try:
                    engine = _engine_ring(ring)
                    twice_ring = engine.ideal(_engine_element(ring, ring(2)))
                except (AttributeError, NotImplementedError, TypeError) as error:
                    raise NotImplementedError(
                        "membership in the principal ideal 2R is not decidable over this base ring"
                    ) from error

                def is_twice(value) -> bool:
                    return _engine_element(ring, ring(value)) in twice_ring

            if self.module_rank().is_finite():
                gram = self.gram_tensor()
                return all(is_twice(gram[i, i]) for i in range(int(self.module_rank())))

            gram = self.gram_tensor()
            match gram:
                case _IdentityGram():
                    return is_twice(ring.one())
                case _DiagonalGram():
                    return is_twice(gram._default) and all(is_twice(value) for value in gram._exceptions.values())
                case _ScaledGram():
                    return is_twice(gram._scalar) or Lattices(self.base_ring())(gram._gram).is_even()
                case _:
                    raise NotImplementedError("evenness of this infinite Gram presentation is not decided")

        def level(self):
            r"""Return the level of a finite nondegenerate integral lattice.

            This is the least ``N > 0`` annihilating the discriminant form.
            For an even lattice the relevant form is
            ``q:A_L -> QQ/2ZZ``; for an odd lattice only the bilinear pairing
            ``b:A_L^2 -> QQ/ZZ`` is canonically defined.  In particular the
            even level need not equal the exponent of ``A_L``: ``<2>`` has
            discriminant group ``ZZ/2`` but level ``4``.
            """
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError("lattice level is currently implemented for integral ZZ-lattices")
            if not self.module_rank().is_finite() or not self.is_nondegenerate():
                raise ValueError("lattice level requires a finite nondegenerate lattice")

            discriminant = self.discriminant_module()
            generators = tuple(discriminant.module_generators())
            denominators = [
                discriminant.b(left, right).lift().denominator()
                for left in generators
                for right in generators
            ]
            if self.is_even():
                denominators.extend(
                    (discriminant.q(generator).lift() / SageZZ(2)).denominator()
                    for generator in generators
                )
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
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError("the live genus object currently implements integral ZZ-lattices")
            if not self.module_rank().is_finite() or not self.is_nondegenerate():
                raise ValueError("a genus here requires a finite nondegenerate lattice")
            if not self.is_even():
                raise NotImplementedError(
                    "the current genus reconstruction from a discriminant quadratic form requires an even lattice"
                )
            return Genus(self.signature_pair(), self.discriminant_quadratic_form())

        def is_locally_isometric(self, other, prime) -> bool:
            r"""Return whether ``self`` and ``other`` are isometric over ``ZZ_p``."""
            if other not in Lattices(self.base_ring()):
                raise TypeError("local lattice isometry compares lattices over one base ring")
            return bool(self.genus().local_symbol(prime) == other.genus().local_symbol(prime))

        def is_unimodular(self) -> bool:
            r"""Return whether the correlation ``L -> L^#`` is an isomorphism."""
            if not self.is_nondegenerate():
                return False
            if self.module_rank().is_finite():
                return bool(self.determinant().is_unit())

            gram = self.gram_tensor()
            match gram:
                case _IdentityGram():
                    return True
                case _DiagonalGram():
                    ring = self.base_ring()
                    return ring(gram._default).is_unit() and all(
                        ring(value).is_unit() for value in gram._exceptions.values()
                    )
                case _ScaledGram():
                    ring = self.base_ring()
                    return ring(gram._scalar).is_unit() and Lattices(ring)(gram._gram).is_unimodular()
                case _:
                    raise NotImplementedError("unimodularity of this infinite Gram presentation is not decided")

        def divisibility_ideal(self, element):
            r"""Return the ideal \(b(v, L) = \{b(v,x) : x\in L\}\) of the base ring.

            The pairings against a generating set generate it.  Over
            \(\mathbb Z\) its positive generator is :meth:`div`.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: L = Lattices(ZZ)([[2, 0], [0, -6]])
                sage: L.divisibility_ideal(L.module_generator(1)) == ZZ.ideal(6)
                True
            """
            assert element.parent() is self, "the divisibility ideal is defined for an element of this lattice"
            ring = self.base_ring()
            pairings = tuple(generator_pairings(self, element).values())
            if not pairings:
                return ring.ideal(ring.zero())
            return ring.ideal(*pairings)

        def is_totally_isotropic(self) -> bool:
            r"""Return whether the form vanishes identically: \(\operatorname{rad}(L)=L\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: U.is_totally_isotropic()
                False
                sage: U.subobject_on((U.module_generator(0),)).is_totally_isotropic()
                True
            """
            assert self.module_rank().is_finite(), "total isotropy is decided here on a finite generating set"
            zero = self.base_ring().zero()
            return all(
                value == zero
                for generator in self.module_generators()
                for value in generator_pairings(self, generator).values()
            )

        def div(self, element):
            r"""Return the divisibility ``gcd{b(element,x): x in L}`` over ``ZZ``."""
            if element.parent() is not self:
                raise TypeError("divisibility is defined for an element of this lattice")

            ring = self.base_ring()
            if _engine_ring(ring) is not SageZZ:
                raise NotImplementedError("integer divisibility is the ZZ specialization")
            pairings = tuple(
                abs(ring(value))
                for value in generator_pairings(self, element).values()
            )
            if not pairings:
                return ring.zero()
            divisor = pairings[0]
            for value in pairings[1:]:
                divisor = divisor.gcd(value)
            return abs(divisor)

        @cached_method
        def dual_module(self):
            r"""Return the algebraic dual module ``Hom_R(L,R)`` in the dual framing."""

            return BasedFreeModule(self.base_ring(), self.module_generating_set())

        @cached_method
        def dual_lattice(self):
            r"""Return the metric dual ``L^#`` on the algebraic dual module.

            The underlying module remains an ``R``-module.  For a
            non-unimodular integral lattice its form takes values in
            ``Frac(R)``; it is not turned into a vector space over ``Frac(R)``.
            """
            assert self.is_nondegenerate()

            if isinstance(self.gram_tensor(), _IdentityGram):
                return Lattices(self.base_ring())(self.dual_module())
            if not self.module_rank().is_finite():
                raise NotImplementedError("the metric dual of this infinite non-identity Gram presentation is not materialized")


            fraction_field = self.base_ring().fraction_field()
            dual_tensor = self.gram_tensor().change_ring(fraction_field).dual_tensor()
            inverse_components = dual_tensor.components()
            try:
                integral_components = [
                    [self.base_ring()(entry) for entry in row]
                    for row in inverse_components
                ]
            except (TypeError, ValueError):
                integral_components = None
            if integral_components is not None:

                integral_dual_form = tensor(
                    self.base_ring(),
                    (),
                    (int(self.module_rank()), int(self.module_rank())),
                    integral_components,
                )
                return Lattices(self.base_ring())(
                    integral_dual_form,
                    module_generators=self.module_generating_set(),
                )
            return refine_rational_lattice(
                BilinearForm(
                    self.dual_module(),
                    fraction_field,
                    inverse_components,
                )
            )

        def metric_dual(self):
            r"""Return the metric dual ``L^#``; explicit synonym for ``dual_lattice``."""
            return self.dual_lattice()

        def dual_basis(self):
            r"""Return the selected basis of ``L^#`` dual to the selected basis of ``L``."""
            return self.dual_lattice().module_generators()

        @cached_method
        def correlation_morphism(self):
            r"""Return ``L -> L^#``, ``v |-> b(v,-)``, whose selected-basis matrix is ``G``."""

            assert self.is_nondegenerate()
            dual_lattice = self.dual_lattice()
            return module_homset(self, dual_lattice)(lambda label: dual_lattice.linear_combination(generator_pairings(self, self.module_generator(label))))

        def correlation(self):
            return self.correlation_morphism()

        @cached_method
        def discriminant_module(self):
            r"""Return ``A_L = coker(L -> L^#)`` with the selected dual-basis presentation."""

            return DiscriminantModule(self)

        def discriminant_projection(self):
            r"""Return the quotient morphism ``L^# -> A_L``."""
            return self.discriminant_module().projection()

        def discriminant_class(self, dual_lattice_element):
            r"""Project an element of ``L^#`` to its discriminant class."""
            if dual_lattice_element.parent() is self:
                dual_lattice_element = self.correlation_morphism()(dual_lattice_element)
            return self.discriminant_module().discriminant_class(dual_lattice_element)

        def divided_discriminant_class(self, element):
            r"""Return the class represented by ``correlation(element)/div(element)``."""
            if element.parent() is not self:
                raise TypeError("divided_discriminant_class expects an element of this lattice")
            divisibility = self.div(element)
            if divisibility == 0:
                raise ValueError("the zero vector has no divided discriminant class")
            dual_lattice = self.dual_lattice()
            correlation_image = self.correlation_morphism()(element)

            divided = dual_lattice.linear_combination(
                {label: coefficient // divisibility for label, coefficient in module_coefficients(correlation_image, dual_lattice).items() if coefficient}
            )
            return self.discriminant_class(divided)

        def radical(self):
            r"""Return ``rad(L)=id_L(L)^perp`` as a subobject of ``L``."""
            return self.identity_morphism().orthogonal_complement()

        def isotropic_reduction(self):
            r"""Return ``S^perp/S`` when this lattice is represented as a subobject."""

            if self not in ModuleSubobjects(self.base_ring()):
                raise TypeError("isotropic reduction requires a chosen lattice inclusion")
            return self.inclusion().isotropic_reduction()

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
            rational_rows = [
                [rationals.one() if i == j else rationals.zero() for j in range(rank)]
                for i in range(rank)
            ]
            dual_labels = tuple(self.dual_lattice().module_generating_set())
            for discriminant_class in discriminant_classes:
                element = (
                    discriminant_class
                    if discriminant_class.parent() is discriminant_module
                    else discriminant_module(discriminant_class)
                )
                lift = discriminant_module.dual_lattice_lift(element)
                coefficients = module_coefficients(
                    lift, discriminant_module.dual_lattice()
                )
                dual_coordinates = tensor(
                    rationals,
                    (),
                    (rank,),
                    [
                        coefficients.get(label, rationals.zero())
                        for label in dual_labels
                    ],
                )
                rational_rows.append(tuple(dual_gram * dual_coordinates))

            denominator = reduce(
                lambda current, coordinate: current.lcm(coordinate.denominator()),
                (coordinate for row in rational_rows for coordinate in row),
                ring.one(),
            )

            # Private HNF/span workspace.  Only backend scalars enter this block.
            backend_denominator = _engine_element(ring, denominator)
            scaled_rows = [
                [
                    SageZZ(
                        backend_denominator
                        * _engine_element(rationals, coordinate)
                    )
                    for coordinate in row
                ]
                for row in rational_rows
            ]
            scaled_span = SageFreeModule(SageZZ, rank).submodule(scaled_rows)
            integral_basis_backend = scaled_span.basis_matrix()
            integral_basis_rows = [
                [ring._from_engine_element(entry) for entry in row]
                for row in integral_basis_backend.rows()
            ]
            basis_rows = tensor.matrix(
                rationals,
                tuple(
                    tuple(
                        rationals._from_engine_element(
                            SageQQ(_engine_element(ring, entry))
                            / SageQQ(backend_denominator)
                        )
                        for entry in row
                    )
                    for row in integral_basis_rows
                ),
            )

            basis_map = MatrixSpace(rationals, rank, rank).from_rows(
                tuple(
                    tuple(basis_rows[column, row] for column in range(rank))
                    for row in range(rank)
                )
            )
            gram = self.gram_tensor().change_ring(rationals).pullback(basis_map)
            try:
                integral_entries = [
                    [ring(gram[i, j]) for j in range(rank)]
                    for i in range(rank)
                ]
            except (TypeError, ValueError) as error:
                raise ValueError(
                    "the selected discriminant classes do not define an integral overlattice"
                ) from error

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
            images = {}
            for source_position, source_label in enumerate(
                self.module_generating_set()
            ):
                target = [
                    denominator if index == source_position else ring.zero()
                    for index in range(rank)
                ]
                coefficients = _solve_left_integrally(
                    integral_basis_rows,
                    target,
                    ring,
                )
                images[source_label] = enlarged.linear_combination(
                    {
                        label: coefficient
                        for label, coefficient in zip(
                            labels, coefficients, strict=True
                        )
                        if coefficient
                    }
                )
            return self.Emb(enlarged)(images)

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
            classes = tuple(
                element if element.parent() is form else form(element)
                for element in discriminant_classes
            )
            for element in classes:
                order = element.additive_order()
                if order != prime ** int(order.valuation(prime)):
                    raise ValueError(
                        f"local modification at p={prime} requires p-primary glue; "
                        f"the class {element} has order {order}"
                    )
            subgroup = form.subgroup_on(classes)
            return form.overlattice_from_isotropic_subobject(subgroup)

        def even_overlattice_inclusions(self):
            r"""Return all even overlattice inclusions ``L -> L'``.

            For an even integral lattice, Nikulin's overlattice correspondence
            identifies even overlattices with isotropic subgroups of the
            discriminant quadratic form.  The zero subgroup is included and
            therefore contributes the identity extension.
            """
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise NotImplementedError(
                    "even overlattice enumeration is currently implemented for integral ZZ-lattices"
                )
            if not self.is_even() or not self.module_rank().is_finite() or not self.is_nondegenerate():
                raise ValueError(
                    "even overlattice enumeration requires a finite nondegenerate even lattice"
                )
            form = self.discriminant_quadratic_form()
            return tuple(
                form.overlattice_from_isotropic_subobject(subgroup)
                for subgroup in form.isotropic_subgroups()
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
            if _engine_ring(ring) is not SageZZ:
                raise NotImplementedError(
                    "the current Nikulin primitive-embedding criterion is for integral ZZ-lattices"
                )
            if not self.is_even() or not self.module_rank().is_finite() or not self.is_nondegenerate():
                raise ValueError(
                    "Nikulin's primitive-embedding criterion requires a finite nondegenerate even lattice"
                )
            _signature = self.signature_pair()
            source_positive, source_negative = _signature.first(), _signature.second()
            if (positive - negative) % 8 != 0:
                return False
            if positive < source_positive or negative < source_negative:
                return False
            complement_signature = (
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
                raise ValueError(
                    f"no primitive embedding into II_{{{positive},{negative}}} exists"
                )

            target_gram, embedding_matrix = lattice_engines.even_unimodular_primitive_embedding(
                self.gram_tensor(), positive, negative
            )
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
            if _engine_ring(ring) is not SageZZ:
                raise NotImplementedError("primitive-extension glue is currently implemented over ZZ")
            for subobject in (first, second):
                assert (
                    subobject in ModuleSubobjects(ring)
                    and subobject.inclusion().codomain() is self
                ), "a glue map is taken between two subobjects of this lattice"
                assert subobject.is_primitive(), (
                    "a primitive extension is presented by primitive sublattices"
                )
            assert first.module_rank() + second.module_rank() == self.module_rank(), (
                "a primitive extension of L needs rk(S)+rk(R)=rk(L)"
            )
            assert all(
                self.b(left, right) == ring.zero()
                for left in first.embedded_module_generators()
                for right in second.embedded_module_generators()
            ), "a primitive extension is presented by mutually orthogonal sublattices"

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
                ambient_covector = ambient_gram * ambient_generator.to_vector()
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
                        raise ArithmeticError(
                            "primitive-extension data send the zero class of A_S to a nonzero class of A_R"
                        )
                    continue
                previous = graph.get(first_class)
                if previous is not None and previous != second_class:
                    raise ArithmeticError(
                        "primitive-extension data do not define a function H_S -> H_R"
                    )
                graph[first_class] = second_class

            source_classes = tuple(graph)
            target_classes = tuple(graph[value] for value in source_classes)
            labels = finite_ordered_set(range(len(source_classes)))
            relations = _relations_among_generators(first_discriminant, source_classes)
            abstract_glue = _torsion_module_presented_by_matrix(relations, labels)

            glue_values = first_discriminant.value_module()
            source_images = {
                label: source_class
                for label, source_class in zip(labels, source_classes, strict=True)
            }

            def source_inclusion(source):
                return form_embedding(
                    source,
                    first_discriminant,
                    source_images,
                    quadratic=quadratic,
                )

            source_form = glue_forms.from_module(
                abstract_glue,
                _form_gram_on(first_discriminant, source_classes, quadratic=quadratic),
                glue_values,
                _subobject_ambient=first_discriminant,
                _subobject_generator_images=source_images,
                _subobject_inclusion_factory=source_inclusion,
            )
            target_gram = tuple(
                tuple(-entry for entry in row)
                for row in _form_gram_on(second_discriminant, target_classes, quadratic=quadratic)
            )
            # The twist is taken on the module underlying A_R, which is A_R
            # itself when it is the discriminant module and its bilinear
            # reading when the summand is even inside an odd L, so the classes
            # cross into the twist the same way in both parities.
            second_forget = second_discriminant.forget_form_morphism()
            second_twist = second_discriminant.twist(-1)
            target_images = {
                label: second_twist.equip_form_morphism()(second_forget(target_class))
                for label, target_class in zip(labels, target_classes, strict=True)
            }

            def target_inclusion(target):
                return form_embedding(
                    target,
                    second_twist,
                    target_images,
                    quadratic=quadratic,
                )

            target_form = glue_forms.from_module(
                abstract_glue,
                target_gram,
                glue_values,
                _subobject_ambient=second_twist,
                _subobject_generator_images=target_images,
                _subobject_inclusion_factory=target_inclusion,
            )

            target_subgroup = second_discriminant.unformed_module().subgroup_on(
                tuple(second_forget(target_class) for target_class in target_classes)
            )
            extension_index = first.sum(second).index()
            if source_form.cardinality() != extension_index:
                raise ArithmeticError(
                    "the recovered glue subgroup does not have order [L:S+R]"
                )
            if target_subgroup.cardinality() != extension_index:
                raise ArithmeticError(
                    "the two primitive-extension glue subgroups have different orders"
                )

            forward = module_homset(source_form, target_form)(
                {
                    label: target_form.module_generator(label)
                    for label in labels
                }
            )
            inverse = module_homset(target_form, source_form)(
                {
                    label: source_form.module_generator(label)
                    for label in labels
                }
            )
            return torsion_form_isometry(forward, inverse, quadratic=quadratic)

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
            return ring(
                len(
                    tuple(
                        invariant
                        for invariant in self.discriminant_module().invariant_factors()
                        if abs(invariant) > ring.one()
                    )
                )
            )

        def is_p_elementary(self, prime) -> bool:
            r"""Return whether ``A_L`` is an elementary abelian ``prime``-group."""
            if _engine_ring(self.base_ring()) is not SageZZ:
                raise TypeError("p-elementarity is currently the integral-lattice invariant")
            ring = self.base_ring()
            prime = ring(prime)
            if not prime.is_prime():
                raise ValueError("p-elementarity requires a prime p")
            invariants = tuple(
                abs(invariant)
                for invariant in self.discriminant_module().invariant_factors()
                if abs(invariant) > ring.one()
            )
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

            def nonintegral(element):
                lifted = discriminant_form.q(element).lift()
                try:
                    ring(lifted)
                except (TypeError, ValueError):
                    return True
                return False

            return ring(
                int(
                    any(
                        nonintegral(element)
                        for element in discriminant_form.smith_form_module_generators()
                    )
                )
            )

        def two_elementary_invariants(self):
            r"""Return Nikulin's \((r,a,\delta)\) for an even 2-elementary lattice.

            The rank, the length of the discriminant group and \(\delta\) are
            three natural numbers, so the triple is a point of
            \(\mathbb N^3\).
            """
            if not self.is_p_elementary(self.base_ring()(2)) or not self.is_even():
                raise ValueError("the lattice is not even and 2-elementary")
            return nikulin_invariants(
                self.module_rank(), self.discriminant_length(), self.delta()
            )

        def reflection(self, root):
            r"""Return the integral orthogonal reflection in ``root``.

            A lattice root is defined by this integrality: for every selected
            module generator ``e_i``, ``2*b(e_i,root)/b(root,root)`` must lie
            in the base ring.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: root = U.module_generator(0) + U.module_generator(1)
                sage: U.reflection(root)(U.module_generator(0))
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
                coefficient = ring(
                    fraction_field(ring(2) * generator.b(root)) / norm
                )
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
            assert isotropic.parent() is self and orthogonal.parent() is self, (
                "an Eichler transvection is built from two vectors of this lattice"
            )
            ring = self.base_ring()
            zero = ring.zero()
            assert isotropic.q() == zero, f"an Eichler transvection is taken in an isotropic vector; q(e)={isotropic.q()}"
            assert isotropic.b(orthogonal) == zero, (
                f"an Eichler transvection needs a in e^perp; b(e,a)={isotropic.b(orthogonal)}"
            )
            fraction_field = ring.fraction_field()
            half_norm = fraction_field(orthogonal.q()) / fraction_field(ring(2))

            def image(label):
                x = self.module_generator(label)
                half_coefficient = half_norm * fraction_field(x.b(isotropic))
                assert half_coefficient in ring, (
                    f"t(e,a) does not preserve the lattice: q(a) b(e,{x})/2 = {half_coefficient} is not integral"
                )
                return (
                    x
                    - self.scalar_multiple(x.b(orthogonal), isotropic)
                    + self.scalar_multiple(x.b(isotropic), orthogonal)
                    - self.scalar_multiple(ring(half_coefficient), isotropic)
                )

            return self.Aut()(image)

        def is_positive_definite(self) -> bool:
            return bool(
                self.module_rank().is_finite()
                and self.signature_pair() == signature_pair(self.module_rank(), 0)
            )

        def is_negative_definite(self) -> bool:
            return bool(
                self.module_rank().is_finite()
                and self.signature_pair() == signature_pair(0, self.module_rank())
            )

        def is_definite(self) -> bool:
            return self.is_positive_definite() or self.is_negative_definite()

        def lll_reduction(self):

            return lll_reduction(self)

        def LLL(self):
            r"""Return the same formed lattice in an LLL-reduced framing."""
            return self.lll_reduction().reduced

        def bkz_reduction(self, block_size=20):

            return bkz_reduction(self, block_size=block_size)

        def BKZ(self, block_size=20):
            r"""Return the same formed lattice in a BKZ-reduced framing."""
            return self.bkz_reduction(block_size=block_size).reduced

        def hkz_reduction(self):

            return hkz_reduction(self)

        def HKZ(self):
            r"""Return the full-block BKZ (HKZ) reframing."""
            return self.hkz_reduction().reduced

        def minimum(self):

            return minimum(self)

        def vectors_of_square(self, square):

            return vectors_of_square(self, square)

        def vectors_of_square_and_divisibility(self, square, divisibility):

            return vectors_of_square_and_divisibility(self, square, divisibility)

        def roots(self):

            return roots(self)

        def roots_of_square(self, square):

            return roots_of_square(self, square)

        def root_sublattice(self):

            return root_sublattice(self)

        def vector_primitive_extension(self, element):
            r"""Return the primitive-extension/gluing datum cut out by ``element``."""

            return VectorPrimitiveExtension(self, element)

        def definite_complement_extensions(self, left, right):
            r"""Return all isometries ``g`` with ``g(left)=right`` in the definite-complement regime."""

            return definite_complement_extensions(self, left, right)

        def gluing_route_discriminant_classes(self, left, right):
            r"""Return admissible ``O(A_L)`` classes from the primitive-extension gluing route."""

            return gluing_route_discriminant_classes(self, left, right)

        def stable_complement_root_reflections(self, element):
            r"""Return stable reflections in root-orbit representatives of ``element^perp``."""

            return stable_complement_root_reflections(self, element)

        def primitive_isotropic_subobject(self, *basis):

            return primitive_isotropic_subobject(self, basis)

        def isotropic_flag(self, *basis):

            return IsotropicFlag(self, basis)

        def isotropic_line_orbit_representatives(self):
            return self.O().isotropic_orbit_representatives(1)

        def isotropic_plane_orbit_representatives(self):
            return self.O().isotropic_orbit_representatives(2)

        def isotropic_flag_orbit_representatives(self, rank=2):
            return self.O().isotropic_orbit_representatives(rank, flag=True)

        def shortest_vectors(self):

            return shortest_vectors(self)

        def theta_series(self, precision=20, variable="q"):

            return theta_series(self, precision=precision, variable=variable)

        def hermite_invariant(self):

            return hermite_invariant(self)

        def successive_minima(self):

            return successive_minima(self)

        def gaussian_heuristic(self, *, exact_form=False):

            return gaussian_heuristic(self, exact_form=exact_form)

        def hadamard_ratio(self):

            return hadamard_ratio(self)

        def closest_vector(self, target):

            return closest_vector(self, target)

        def babai(self, target):

            return babai(self, target)

        approximate_closest_vector = babai

        def voronoi_cell(self, bound=None):

            return voronoi_cell(self, bound=bound)

        def voronoi_relevant_vectors(self):

            return voronoi_relevant_vectors(self)

        def contact_polytope(self):

            return contact_polytope(self)

        def packing_radius(self):

            return packing_radius(self)

        def covering_radius(self):

            return covering_radius(self)

        def center_density(self):

            return center_density(self)

        def packing_density(self):

            return packing_density(self)

        def kissing_number(self):

            return kissing_number(self)

        def twist(self, scalar):
            r"""Keep the module and rescale its form by ``scalar``.

            The result is the same free module with
            \(b'(x,y)=\mathrm{scalar}\cdot b(x,y)\).  The Gram is
            scaled as a type-$(0,2)$ tensor: a pairing rule is not
            materialized as a finite array.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Iinf = Lattices(ZZ)(ZZ^NN)
                sage: Iinf.module_generator(0)^2
                1
                sage: Iinf.twist(2).module_generator(0)^2
                2
                sage: latex(Iinf.twist(2).gram_tensor())
                2\,I_{\infty}
                sage: Iinf.twist(2).gram_tensor()
                2 I_∞ ∈ (ZZ^NN ⊗ ZZ^NN)*
            """

            scaled = scale_gram_tensor(self.gram_tensor(), self.base_ring()(scalar))
            match scaled:
                case _PairingGram():
                    return Lattices(self.base_ring())(scaled)
                case _:
                    return Lattices(self.base_ring())(
                        scaled,
                        module_generators=self.module_generating_set(),
                    )

        def __add__(self, other):
            r"""Return the orthogonal direct sum.

            Finite \(\oplus\) finite and finite \(\oplus\) infinite, in
            the concatenated basis.  Infinite \(\oplus\) infinite is
            not constructed.  ``sum([...])`` uses ``0 + L``.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)("U") + Lattices(ZZ)(ZZ^NN)
                Integral lattice of rank +Infinity and signature (+Infinity, 1)
            """
            if other == 0:
                return self

            ring = self.base_ring()
            category = Lattices(ring)
            assert other in category
            return orthogonal_sum(self, other, category=category)

        def __radd__(self, other):
            if other == 0:
                return self
            return NotImplemented

        def __pow__(self, exponent):
            r"""Return \(L^{\oplus n}\), the \(n\)-fold orthogonal direct sum.

            It is the sum of the constant family over \(\Delta[n-1]\), so
            ``L ** 0`` is the empty sum: the zero lattice, the unit of ``+``.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: (Lattices(ZZ)("U") ** 3).signature_pair()
                (3, 3)
            """
            count = int(exponent)
            assert count >= 0, "an orthogonal power L^n takes a natural number n"
            if count == 0:
                return Lattices(self.base_ring())(0)
            return sum(
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
            if _engine_ring(self.base_ring().fraction_field()) is QQ:
                _signature = self.signature_pair()
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
            return lattice_latex(self, tex)

    class ElementMethods:
        r"""Operations generic to every lattice element."""

        def b(self, other):
            r"""Return \(b(v,w)\) by contracting the Gram tensor on \(v\) and \(w\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: I2 = Lattices(ZZ)(ZZ^2)
                sage: e, f = I2.module_generator(0), I2.module_generator(1)
                sage: e.b(f), e*e
                (0, 1)
            """
            assert other.parent() is self.parent()
            return self.parent().b(self, other)

        def q(self):
            r"""Return \(q(v)=b(v,v)\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: U = Lattices(ZZ)("U")
                sage: root = U.module_generator(0) + U.module_generator(1)
                sage: root.q()
                2
            """
            return self.b(self)

        def norm(self):
            r"""Return the form norm ``b(v,v)``."""
            return self.q()

        def divisibility_ideal(self):
            return self.parent().divisibility_ideal(self)

        def div(self):
            r"""Return the positive integer generator of ``b(v,L)`` over ``ZZ``.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)(ZZ^NN).module_generator(0).div()
                1
            """
            return self.parent().div(self)

        def divided_discriminant_class(self):
            return self.parent().divided_discriminant_class(self)

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

        def is_isotropic(self) -> bool:
            r"""Return whether \(q(v)=0\).

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: e, f = Lattices(ZZ)("U").module_generators()
                sage: e.is_isotropic(), (e + f).is_isotropic()
                (True, False)
            """
            return self.q() == self.parent().base_ring().zero()

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

        def isotropic_reduction(self):
            r"""Return \(v^\perp/Rv\) for an isotropic vector, with its parabolic data."""
            return self.sublattice().inclusion().isotropic_reduction()

        def is_root(self) -> bool:
            r"""Return whether the orthogonal reflection in this vector is integral.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Iinf = Lattices(ZZ)(ZZ^NN)
                sage: Iinf.module_generator(0).is_root()
                True
                sage: Iinf((2, 1)).is_root()
                False
            """

            parent = self.parent()
            ring = parent.base_ring()
            if not ring.is_integral_domain():
                raise TypeError("roots are defined here over an integral domain")
            norm = ring(self.q())
            if norm == ring.zero():
                return False
            fraction_field = ring if ring.is_field() else ring.fraction_field()
            norm_in_fraction_field = fraction_field(norm)
            for coefficient in generator_pairings(parent, self).values():
                quotient = (
                    fraction_field(ring(2) * coefficient)
                    / norm_in_fraction_field
                )
                try:
                    ring(quotient)
                except (TypeError, ValueError):
                    return False
            return True

        def monomial_coefficients(self):
            return self.parent()._monomial_coefficients(self._vector)

        def to_list(self):
            r"""Return the coordinates of this element as a Python list."""
            from sage.rings.infinity import Infinity

            parent = self.parent()
            coefficients = parent._monomial_coefficients(self._vector)
            keys = parent.module_generating_set()
            zero = parent.base_ring().zero()
            rank = parent.module_rank()
            if rank == Infinity:
                if not coefficients:
                    return []
                last = max(int(keys.rank(key)) for key in coefficients)
                return [coefficients.get(keys.unrank(index), zero) for index in range(last + 1)]
            return [coefficients.get(key, zero) for key in keys]

        def to_tuple(self):
            r"""Return the coordinates of this element as a Python tuple."""
            return tuple(self.to_list())

        def to_vector(self):
            r"""Return the coordinates of this element as a vector tensor of type $(1,0)$.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.lattices import Lattices
                sage: Lattices(ZZ)(ZZ^2).module_generator(0).to_vector()
                (1, 0)
            """

            return tensor.vector(self.parent().base_ring(), self.to_list())


class FiniteRankLattices(OwnedCategoryOverBaseRing):
    r"""Lattices whose underlying free module has finite rank."""

    _certifying_predicate = "module_rank.is_finite"

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finite-rank lattices"

    def an_object(self):
        r"""The hyperbolic plane U, of rank two."""
        return Lattices(self.base_ring())("U")

    def super_categories(self):

        return [
            Lattices(self.base_ring()),
            FinitelyGeneratedFreeModules(self.base_ring()),
        ]


class NondegenerateLattices(OwnedCategoryOverBaseRing):
    r"""Lattices whose correlation map has zero kernel."""

    _certifying_predicate = "is_nondegenerate"

    @classmethod
    def _repr_object_names(cls) -> str:
        return "nondegenerate lattices"

    def an_object(self):
        r"""The hyperbolic plane U, whose form is unimodular."""
        return Lattices(self.base_ring())("U")

    def super_categories(self):
        return [Lattices(self.base_ring())]


class EvenLattices(OwnedCategoryOverBaseRing):
    r"""Lattices satisfying ``b(x,x) in 2R`` for every lattice vector ``x``."""

    _certifying_predicate = "is_even"

    @classmethod
    def _repr_object_names(cls) -> str:
        return "even lattices"

    def an_object(self):
        r"""The hyperbolic plane U, on which every square is even."""
        return Lattices(self.base_ring())("U")

    def super_categories(self):
        return [Lattices(self.base_ring())]


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
        return (plane + plane).module_generator(0).isotropic_reduction()

    @classmethod
    def _repr_object_names(cls) -> str:
        return "isotropic reductions"

    def super_categories(self):
        return [Lattices(self.base_ring())]

    class ParentMethods:
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
                normalized_element = normalization.forward()(
                    presentation_projection(perpendicular.module_generator(label))
                )
                return self.linear_combination(
                    {
                        labels.unrank(int(normalized_labels.rank(normalized_label))): coefficient
                        for normalized_label, coefficient in module_coefficients(
                            normalized_element, normalized
                        ).items()
                        if coefficient
                    }
                )

            return module_homset(perpendicular, self)(image)

        @cached_method
        def parabolic_subgroup(self):
            r"""Return \(P_I=\operatorname{Stab}_{O(L)}(I)\), the setwise stabilizer of \(I\)."""
            embedding = self.isotropic_embedding()
            return embedding.codomain().O().setwise_stabilizer(embedding)

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
                return automorphisms(
                    lambda label: projection(
                        perpendicular_inclusion.lift(
                            isometry(perpendicular_inclusion(lifts(label)))
                        )
                    )
                )

            return SetMorphism(
                self.parabolic_subgroup().Mor(automorphisms), descend
            )

        @cached_method
        def unipotent_kernel(self):
            r"""Return \(U_I=\ker(P_I\to GL(I)\times O(K_I))\), the unipotent radical."""
            embedding = self.isotropic_embedding()
            source = embedding.domain()
            embedded = tuple(
                embedding(generator) for generator in source.module_generators()
            )
            levi = self.levi_action()
            identity = self.Aut().one()
            return predicate_subgroup(
                self.parabolic_subgroup(),
                lambda isometry: all(
                    isometry(vector) == vector for vector in embedded
                )
                and levi(isometry) == identity,
                "g fixes I pointwise and acts trivially on I^perp/I",
            )

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
            assert isometry.parent() is automorphisms, (
                "the isometry to lift is an element of O(K_I)"
            )
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
                "no represented splitting L = M perp K' along the chosen lifts; "
                "the Levi quotient need not lift"
            )
            complement_inclusion = complement.inclusion()
            summand_inclusion = unimodular_summand.inclusion()
            into_complement = module_homset(self, complement)(
                lambda label: complement_inclusion.lift(embedded_lifts(label))
            )
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
                                summand_inclusion(
                                    unimodular_summand.module_generator(label)
                                ),
                            )
                        )
                    }
                )
                return correlation.inverse()(covector)

            def image(label):
                vector = lattice.module_generator(label)
                fixed_part = summand_component(vector)
                embedded_fixed = summand_inclusion(fixed_part)
                moved_part = into_complement.lift(
                    complement_inclusion.lift(vector - embedded_fixed)
                )
                return embedded_fixed + complement_inclusion(
                    into_complement(isometry(moved_part))
                )

            lifted = lattice.O()(image)
            assert lifted in self.parabolic_subgroup(), (
                "the assembled map does not stabilize I; the chosen lifts do not span a splitting"
            )
            assert self.levi_action()(lifted) == isometry, (
                "the assembled map descends to the wrong isometry of I^perp/I"
            )
            return lifted


class RootLattices(Category):
    r"""Negative-definite ADE root lattices with a chosen simple-root framing."""

    @classmethod
    def _repr_object_names(cls):
        return "root lattices"

    def super_categories(self):
        integers = _own_ring(SageZZ)
        return [
            FiniteRankLattices(integers),
            NondegenerateLattices(integers),
            EvenLattices(integers),
        ]

    class ParentMethods:
        def cartan_type(self):
            return self._preamble_cartan_type

        def simple_roots(self):
            r"""Return the selected framing, which is the chosen simple system."""
            return self.module_generators()

        def coxeter_number(self):
            cartan_type = self.cartan_type()
            if not cartan_type.is_irreducible():
                raise ValueError(
                    "a reducible root system has one Coxeter number per irreducible component"
                )
            return cartan_type.coxeter_number()

        def highest_root(self):
            r"""Return the highest root in the selected simple-root framing."""
            cartan_type = self.cartan_type()
            if not cartan_type.is_irreducible():
                raise ValueError(
                    "a reducible root system has one highest root per irreducible component"
                )
            coefficients = tuple(
                RootSystem(cartan_type).root_lattice().highest_root().to_vector()
            )
            return sum(
                (
                    coefficient * root
                    for coefficient, root in zip(
                        coefficients, self.simple_roots(), strict=True
                    )
                ),
                self.zero(),
            )

        def simple_reflections(self):
            return tuple(self.reflection(root) for root in self.simple_roots())

        def fundamental_weights(self):
            r"""Return the weights dual to the simple coroots."""

            norm = self.simple_roots()[0].norm()
            if norm not in (2, -2):
                raise ValueError(
                    f"a simply-laced root framing has simple-root square +/-2, got {norm}"
                )
            sign = SageZZ(norm) // 2
            return finite_ordered_image(
                self.dual_basis(),
                lambda weight: sign * weight,
            )

    class ElementMethods:
        def is_positive_root(self) -> bool:
            return bool(
                self.is_root()
                and all(
                    coefficient >= 0
                    for coefficient in self.monomial_coefficients().values()
                )
            )

        def is_negative_root(self) -> bool:
            return bool((-self).is_positive_root())

        def height(self):
            return sum(self.monomial_coefficients().values(), SageZZ.zero())

        def coroot(self):
            r"""Return ``alpha^vee = 2*b(alpha,-)/b(alpha,alpha)`` in ``L^#``."""
            parent = self.parent()
            if not self.is_root():
                raise ValueError("the coroot in this lattice is defined for an integral root")
            norm = SageZZ(self.norm())
            dual_lattice = parent.dual_lattice()
            return dual_lattice.linear_combination(
                {
                    label: SageZZ(2 * parent.module_generator(label).b(self) / norm)
                    for label in parent.module_generating_set()
                    if parent.module_generator(label).b(self) != 0
                }
            )


def refine_root_lattice(lattice, cartan_type):
    r"""Record the Cartan type whose negative Cartan form built ``lattice``."""
    return lattice.lattice_category()._refine_root_lattice(lattice, cartan_type)


def refine_lattice_properties(lattice):
    r"""Attach the finite lattice properties directly decidable from the form."""
    return lattice.lattice_category()._refine_lattice_object(lattice)
