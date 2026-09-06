r"""Every constructor produces an object that can answer for itself.

A category states obligations with ``abstract_method``, and Sage raises only
when one is *called*.  So an object can enter a category carrying none of the
data that category is about, and the failure surfaces far away -- at a call
site that had no part in building it.  That is how this preamble came to have
modules with no ring action, form modules whose ``form()`` was missing, and
two free modules on one $(R,S)$.

The gate cannot be at construction: ``_refine_category_`` puts anything into
any category with no hook run at all, and refinement is how the preamble
places objects.  What is available is that the obligations are *visible*: a
method left abstract resolves to an ``AbstractMethod`` on the object's class,
an implemented one does not.

So the check is a sweep.  There are finitely many constructors; each is run,
and each result is asked whether anything its categories require was never
implemented.
"""

import functools
from unittest.mock import patch
from collections.abc import Callable

import pytest

from sage.all import Infinity
from sage.misc.abstract_method import AbstractMethod, abstract_methods_of_class
from sage.structure.parent import Parent

from dzack_research.preamble.categories.forms.forms import (
    BilinearFormMorphism,
    QuadraticFormMorphism,
)
from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.constructions import TensorSquare
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.modules.powers import DividedSquare
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism


def _identity_on(source: Parent):
    r"""Return $\mathrm{id}_S$ in the pre-existing owned Hom object."""
    return Sets().Mor(source, source).identity()


def _one_object_diagram(source: Parent):
    index = DiscreteCategory(Sets.Δ[0])
    return DiscreteDiagram(index, Sets(), lambda _index: source)


def _ensure_preamble() -> None:
    r"""Load the public preamble session used by every specimen."""
    if "Lattices" in globals():
        return
    exec("from dzack_research.preamble.all import *", globals())


def unmet_obligations(parent: Parent) -> list:
    r"""Return the names ``parent``'s categories require and nothing supplies.

    Read off the object rather than the category: what matters is whether the
    name resolves to something that answers, however it got there -- a class
    method, a ``ParentMethods`` further up, or an attribute set at
    construction.  An obligation is unmet only when the resolved attribute is
    still the abstract declaration.
    """
    required = abstract_methods_of_class(parent.category().parent_class)["required"]
    unmet = []
    for name in required:
        # Ask the object, and take its refusal at face value.  Reading the
        # attribute off the class instead misses both directions: a class-level
        # implementation is invisible there, and an unimplemented declaration
        # can read as plain absence, which is what made this sweep report
        # green while an object was raising on the very method.
        try:
            getattr(parent, name)
        except (NotImplementedError, AttributeError):
            unmet.append(name)
    return sorted(unmet)


@functools.cache
def _construction(name: str) -> Parent:
    r"""Return the specimen ``name`` names, building it at most once.

    Cached, for the reason the table used to be built eagerly: a construction
    named by several rows would otherwise be run once per row, multiplying
    every constructor's cost by the size of the table.  What the cache no
    longer does is build a row nobody asked for -- a specimen that raises is
    one red row naming its own construction, where before it was a collection
    error that silenced all hundred and six.
    """
    return _constructions()[name]()


@functools.cache
def _constructions() -> "dict[str, Callable[[], Parent]]":
    r"""Every way the preamble makes an object, with one specimen each.

    The values are thunks and not objects: collection needs the names, and
    asking for the names must not run a single constructor.
    """
    _ensure_preamble()
    e = list(Lattices(ZZ)("E8").module_generators())
    u = list(Lattices(ZZ)("U").module_generators())
    uu = Lattices(ZZ)("U") + Lattices(ZZ)("U")
    g = list(uu.module_generators())
    return {
        "Lattices(ring)": lambda: Lattices(ZZ),
        "Lattices(name)": lambda: NamedLattices.LK3,
        "Lattices(root system)": lambda: Lattices(ZZ)("A2"),
        "Lattices(gram)": lambda: Lattices(ZZ)([[2, 1], [1, 2]]),
        "direct sum": lambda: Lattices(ZZ)("A1") + Lattices(ZZ)("A2"),
        "tensor product": lambda: TensorProduct(
            BasedFreeModule(ZZ, Sets.Δ[1]), BasedFreeModule(ZZ, Sets.Δ[2])
        ),
        "twist": lambda: Lattices(ZZ)("E8").twist(2),
        "rooted Coxeter diagram from a Cartan type": lambda: CoxeterDiagrams().from_cartan_type(
            ["A", 2], rooted=True
        ),
        "dual lattice": lambda: Lattices(ZZ)("A2").dual_lattice(),
        "root sublattice": lambda: Lattices(ZZ)("A2").root_sublattice(),
        "symmetric group of a finite set": lambda: Groups.S(3),
        "subobject": lambda: Lattices(ZZ)("E8").subobject_on([2 * e[0]]),
        "discriminant group": lambda: Lattices(ZZ)("A2").discriminant_group(),
        "discriminant bilinear form": lambda: Lattices(ZZ)("A2").discriminant_bilinear_form(),
        "free module on a set": lambda: FreeModuleOn(ZZ, Sets.Δ[2]),
        "based free module": lambda: BasedFreeModule(ZZ, Sets.Δ[2]),
        "R^n": lambda: ZZ**3,
        # Not the row above: ``ZZ**3`` builds the framed free module on a
        # chosen generating set, while these two are built through the
        # category chain, where the underlying set is the product
        # $R\times\cdots\times R$ and the form is added on top of it.
        "free module of rank n": lambda: FreeModule(ZZ, 3),
        "isometry group": lambda: Lattices(ZZ)("A2").Aut(),
        # A finite abstract group's automorphism group, and the stated-gap
        # specimen: Aut of a free group constructs -- the object exists --
        # while enumeration and order state the algorithmic gap when asked.
        "abstract group automorphism group": lambda: Groups.Q().Aut(),
        "free group automorphism group": lambda: Groups.Free(2).Aut(),
        "isometry homset": lambda: Lattices(ZZ)("A2").Isom(Lattices(ZZ)("A2")),
        "embedding homset": lambda: Lattices(ZZ)("A1").Emb(Lattices(ZZ)("E8")),
        "discriminant image subgroup": lambda: Lattices(ZZ)("A2").discriminant_image(),
        # The stabilizer of one class in O(A): for A2 the discriminant form is
        # ZZ/3 with O(A) = {+-1}, so the stabilizer of a nonzero class is
        # trivial -- which also puts the empty generating set through the
        # subgroup constructor.
        "discriminant class stabilizer": lambda: Lattices(ZZ)("A2").discriminant_group()
        .automorphism_group()
        .stabilizer_of_element(
            list(Lattices(ZZ)("A2").discriminant_group().module_generators())[0]
        ),
        "special orthogonal subgroup": lambda: Lattices(ZZ)("A2").SO(),
        "spinor kernel subgroup": lambda: Lattices(ZZ)("A2").spinor_kernel_subgroup(),
        "stable orthogonal group": lambda: Lattices(ZZ)("A2").stable_orthogonal_group(),
        "vector stabilizer isometries": lambda: _vector_stabilizer(Lattices(ZZ)("A2")),
        "isotropic line stabilizer isometries": lambda: _isotropic_line_stabilizer(
            Lattices(ZZ)("U")
        ),
        "isotropic plane stabilizer isometries": lambda: _isotropic_plane_stabilizer(uu),
        "isotropic flag stabilizer isometries": lambda: _isotropic_flag_stabilizer(uu),
        "character-kernel subgroup intersection": lambda: Lattices(ZZ)("A2")
        .SO()
        .intersection(Lattices(ZZ)("A2").spinor_kernel_subgroup()),
        "free algebra": lambda: FreeAlgebraOn(QQ, Sets.Δ[1]),
        "tensor algebra": lambda: TensorAlgebraOn(QQ, Sets.Δ[1]),
        "alternating algebra": lambda: AlternatingAlgebraOn(QQ, Sets.Δ[1]),
        "tensor algebra degree two": lambda: TensorAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "symmetric algebra degree two": lambda: FreeAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "alternating algebra degree two": lambda: AlternatingAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "smooth function module": lambda: C(Infinity, RR),
        "square-integrable function module": lambda: Lp(2),
        # ---- indexed symbolic function families ----
        "Fourier characters": lambda: FourierCharacters(),
        "Hermite polynomials": lambda: HermitePolynomials(),
        "Laurent monomials": lambda: LaurentMonomials(),
        "sinc translates": lambda: SincTranslates(),
        # ---- restricted Hom categories with independent structure ----
        "derivation space": lambda: _derivation_space(),
        "graded derivation space": lambda: _graded_derivation_space(),
        "connection space": lambda: _connection_space(),
        "horizontal connection maps": lambda: _horizontal_connection_maps(),
        "absolute Galois group": lambda: AbsoluteGaloisGroup(GF(5)),
        "cartesian product of sets": lambda: CartesianProductOfSets(Sets.Δ[1], Sets.Δ[2]),
        "polynomial ring": lambda: QQ["x"],
        "prime field": lambda: PrimeField(3),
        "a ring as an algebra over itself": lambda: ZZ,
        "subobject sum": lambda: Lattices(ZZ)("E8").subobject_on([2 * e[0]]).sum(
            Lattices(ZZ)("E8").subobject_on([3 * e[1]])
        ),
        "subobject intersection": lambda: Lattices(ZZ)("E8").subobject_on([2 * e[0], 2 * e[1]])
        .intersection(Lattices(ZZ)("E8").subobject_on([3 * e[0], 3 * e[1]])),
        "discriminant quadratic form from data": lambda: _discriminant_quadratic_from_data(),
        "discriminant bilinear form from data": lambda: _discriminant_bilinear_from_data(),
        # ---- sets ----
        "power set": lambda: PowerSet(Sets.Δ[2]),
        "subsets of a fixed size": lambda: SubsetsOfSize(Sets.Δ[2], 2),
        "finite subsets": lambda: FiniteSubsets(Sets.Δ[2]),
        "ordinals": lambda: Ordinals(),
        # A cardinal is built by ``object_of`` through the owned chain like
        # any other object here -- ``type(cardinal(3))`` is
        # ``Cardinalities.parent_class`` and it is a ``Parent``, not an
        # element -- so the sweep's question is the same question for it.
        "cardinal": lambda: cardinal(3),
        # The image of the forgetful functor: what a lattice's cardinality,
        # finiteness and enumeration are actually asked of.
        "set from an iterable": lambda: Set([1, 2, 3]),
        "condition set": lambda: ConditionSet(ZZ, lambda n: n > 0),
        "image set": lambda: ImageSet(lambda n: n, Sets.Δ[2]),
        # ---- categorical constructions ----
        "coproduct of sets": lambda: CoproductOfSets(Sets.Δ[1], Sets.Δ[2]),
        "isomorphism homset": lambda: IsoCategoryOf(Sets()).Of(Sets.Δ[1], Sets.Δ[1]),
        # The five limit constructors, on one-object diagrams.  Not the direct
        # sum row above: ``Lattices(ZZ)("A1") + Lattices(ZZ)("A2")`` goes through the
        # lattice-specific block-diagonal sum and reaches none of these.
        "cone": lambda: _cone_on(Sets.Δ[11]),
        "cocone": lambda: _cocone_on(Sets.Δ[12]),
        "product": lambda: Product(Sets.Δ[13], Sets.Δ[14]),
        "coproduct": lambda: Coproduct(Sets.Δ[15], Sets.Δ[16]),
        "biproduct": lambda: Biproduct(
            BasedFreeModule(ZZ, Sets.Δ[1]), BasedFreeModule(ZZ, Sets.Δ[2])
        ),
        # ---- divisors ----
        # One free module each: every one of these refines the module it is
        # handed into its own divisor category.
        "divisor group": lambda: DivisorGroup(FreeModuleOn(ZZ, Sets.Δ[3])),
        "weil divisor group": lambda: WeilDivisorGroup(FreeModuleOn(ZZ, Sets.Δ[4])),
        "cartier divisor group": lambda: CartierDivisorGroup(FreeModuleOn(ZZ, Sets.Δ[5])),
        "picard group": lambda: PicardGroup(FreeModuleOn(ZZ, Sets.Δ[6])),
        "class group": lambda: ClassGroup(FreeModuleOn(ZZ, Sets.Δ[7])),
        # ---- schemes ----
        "affine space": lambda: AffineSpace(2, QQ),
        "projective space": lambda: ProjectiveSpace(2, QQ),
        "convex polytope": lambda: ConvexPolytope([[0, 0], [1, 0], [0, 1]]),
        "convex polygon": lambda: ConvexPolygon([[0, 0], [1, 0], [0, 1]]),
        "lattice polytope": lambda: LatticePolytope([[0, 0], [1, 0], [0, 1]]),
        "lattice polygon": lambda: LatticePolygon([[0, 0], [1, 0], [0, 1]]),
        "equation-defined closed subscheme": lambda: _affine_divisor(),
        # ---- algebras on an existing module ----
        # A different construction from the ``...On`` rows above: those build
        # the free algebra on a chosen generating set, these build it on a
        # module that already exists and keep that module's presentation.
        "tensor algebra of a module": lambda: TensorAlgebraOf(BasedFreeModule(QQ, Sets.Δ[1])),
        "symmetric algebra of a module": lambda: SymmetricAlgebraOf(
            BasedFreeModule(QQ, Sets.Δ[1])
        ),
        "alternating algebra of a module": lambda: AlternatingAlgebraOf(
            BasedFreeModule(QQ, Sets.Δ[1])
        ),
        # ---- modules ----
        "fractional ideal": lambda: FractionalIdeal(ZZ, [2]),
        # An S-module from its scalar action, and the coextension of scalars
        # that produces one: both along ZZ -> ZZ[C2].
        "module from a scalar action": lambda: _module_from_scalar_action(),
        "coextension of scalars": lambda: Modules(ZZ).coextension_of_scalars(
            _group_algebra_structure_map(Groups.C(2))
        )(FreeModuleOn(ZZ, Sets.Δ[0])),
        # The two square constructions on an arbitrary module rather than on a
        # free algebra's graded piece: they are where a form's domain comes
        # from, so a lattice is the specimen that matters.
        "tensor square": lambda: TensorSquare(Lattices(ZZ)("A2")),
        "divided square": lambda: DividedSquare(Lattices(ZZ)("A2")),
        # Not the ``torsion module`` path: this presents a module by a chosen
        # morphism of free modules.
        "finitely presented module": lambda: FinitelyPresentedModule(
            FreeModuleOn(ZZ, Sets.Δ[0]).hom(
                {0: FreeModuleOn(ZZ, Sets.Δ[0]).module_generator(0) * 2},
                FreeModuleOn(ZZ, Sets.Δ[0]),
            )
        ),
        # ---- forms ----
        # The two form homsets: built transiently everywhere a form is made,
        # and never asked for themselves.
        "bilinear form homset": lambda: BilinearForms(Lattices(ZZ)("A2"), ZZ),
        "quadratic form homset": lambda: QuadraticForms(Lattices(ZZ)("A2"), ZZ),
    }


def _group_algebra_structure_map(group):
    group_algebra = ZZ[group]
    return ring_morphism(ZZ, group_algebra, lambda integer: integer * group_algebra.one())


def _module_from_scalar_action():
    r"""``ZZ^2`` as a ``ZZ[C2]``-module, the generator swapping the coordinates."""
    group_algebra = ZZ[Groups.C(2)]
    plane = FreeModuleOn(ZZ, Sets.Δ[1])
    endomorphisms = Modules(ZZ).End(plane)
    swap = endomorphisms({0: plane.module_generator(1), 1: plane.module_generator(0)})

    def action(scalar):
        coefficients = module_coefficients(scalar, group_algebra)
        return endomorphisms.elementwise(
            lambda vector: sum(
                (
                    coefficient * (vector if label == group_algebra.group().one() else swap(vector))
                    for label, coefficient in coefficients.items()
                ),
                plane.zero(),
            ),
            verify_linearity=False,
        )

    return Modules(group_algebra)(plane, ring_morphism(group_algebra, endomorphisms, action))


def _derivation_algebra():
    return SymmetricAlgebraOn(QQ, ("x",))


def _derivation_space():
    algebra = _derivation_algebra()
    return VectorFields(algebra)


def _graded_derivation_space():
    de_rham = DeRhamAlgebra(_derivation_algebra())
    return GradedDerivations(de_rham, shift=-1)


def _connection_space():
    algebra = _derivation_algebra()
    module = BasedFreeModule(algebra, Sets.Δ[0])
    return Connections(module)


def _horizontal_connection_maps():
    connection_space = _connection_space()
    connection = connection_space(lambda _label: connection_space.target_module().zero())
    structured_module = ModuleWithConnection(connection)
    return connection_homset(structured_module, structured_module)


def _is_owned_object(parent: Parent) -> bool:
    r"""Whether ``parent`` is represented in at least one owned object category."""
    try:
        categories = parent.category().all_super_categories(proper=False)
    except AttributeError:
        return False
    return any(isinstance(category, OwnedCategory) for category in categories)


def _cone_on(source: Parent):
    diagram = _one_object_diagram(source)
    return Cone(diagram, source, lambda _index: _identity_on(source))


def _cocone_on(source: Parent):
    diagram = _one_object_diagram(source)
    return Cocone(diagram, source, lambda _index: _identity_on(source))


def _vector_stabilizer(lattice):
    group = lattice.O()
    vector = lattice.module_generators()[0]
    return group.vector_stabilizer_generators(vector)


def _identity_backend_stabilizer(gram, _basis, choice="plane"):
    size = len(gram)
    return [
        [[1 if row == column else 0 for column in range(size)] for row in range(size)]
    ]


def _isotropic_line_stabilizer(lattice):
    line = lattice.primitive_isotropic_subobject(lattice.module_generators()[0])
    group = lattice.O()
    with patch(
        "py_polyhedral.binaries.indefinite_form_stabilizer_isotropic_subspace",
        _identity_backend_stabilizer,
    ):
        return group.isotropic_stabilizer_generators(line)


def _isotropic_plane_stabilizer(lattice):
    basis = lattice.module_generators()
    plane = lattice.primitive_isotropic_subobject(basis[0], basis[2])
    group = lattice.O()
    with patch(
        "py_polyhedral.binaries.indefinite_form_stabilizer_isotropic_subspace",
        _identity_backend_stabilizer,
    ):
        return group.isotropic_stabilizer_generators(plane)


def _isotropic_flag_stabilizer(lattice):
    basis = lattice.module_generators()
    flag = lattice.isotropic_flag(basis[0], basis[2])
    group = lattice.O()
    with patch(
        "py_polyhedral.binaries.indefinite_form_stabilizer_isotropic_subspace",
        _identity_backend_stabilizer,
    ):
        return group.isotropic_stabilizer_generators(flag, flag=True)


def _affine_divisor():
    affine = AffineSpace(2, QQ)
    x = affine.coordinate_ring().algebra_generators()[0]
    return affine.closed_subscheme(x)


def _discriminant_quadratic_from_data() -> Parent:
    values = FractionFieldQuotient(ZZ, 2)
    return TorsionQuadraticFormModules(ZZ).from_relations_and_gram(
        [[2]], [[-QQ(1) / 2]], values
    )


def _discriminant_bilinear_from_data() -> Parent:
    values = FractionFieldQuotient(ZZ, 1)
    return TorsionBilinearFormModules(ZZ).from_relations_and_gram(
        [[2]], [[QQ(1) / 2]], values
    )


def test_a_form_is_a_morphism_into_the_value_module() -> None:
    r"""The form is a map, not a matrix.

    One test over the whole table rather than one per formed row: which rows
    carry a form is not knowable without building them, and building the
    table to find out is what a single bad specimen used to be able to break.

    A bilinear form on $M$ with values in $W$ is an element of
    $\operatorname{Hom}_R(M\otimes_R M, W)$: its domain is the tensor square
    and its codomain is the value module.  A Gram matrix is how a *finitely
    generated* one can be written down, and asking for the morphism is what
    keeps the general case expressible.
    """
    checked = 0
    for name in sorted(_constructions()):
        parent = _construction(name)
        if not (hasattr(parent, "form") and hasattr(parent, "value_module")):
            continue
        checked += 1
        form = parent.form()

        assert form.codomain() is parent.value_module(), (
            f"{name}: the form's codomain must be the value module, "
            f"got {form.codomain()} against {parent.value_module()}"
        )
        # When the universal square object is represented, the form is a
        # morphism out of that square.  The explicit callable fallback is used
        # only when no such represented classifier exists.
        if not hasattr(form, "domain"):
            assert callable(form), f"{name}: an extensional form must remain callable"
            continue
        domain = form.domain()
        if isinstance(form, BilinearFormMorphism):
            expected_constructor = TensorSquare
        elif isinstance(form, QuadraticFormMorphism):
            expected_constructor = DividedSquare
        else:
            raise AssertionError(f"{name}: unrecognized represented form morphism {type(form)}")
        expected_domain = expected_constructor(parent)

        assert domain is expected_domain, (
            f"{name}: the form has domain {domain}, not the degree-two "
            f"construction {expected_domain}"
        )

    assert checked > 0, "the table names no formed construction at all"


@pytest.mark.parametrize("name", sorted(_constructions()))
def test_a_constructed_object_answers_what_its_categories_require(name: str) -> None:
    r"""Nothing the object's categories declare is left unimplemented."""
    parent = _construction(name)
    unmet = unmet_obligations(parent)

    assert not unmet, (
        f"{name} built an object in {parent.category()} that never implements "
        f"{unmet}: the constructor placed it in a category without supplying "
        "what that category is about"
    )


@pytest.mark.parametrize("name", sorted(_constructions()))
def test_every_owned_constructed_object_has_one_interned_mor(name: str) -> None:
    r"""Every owned object uses one canonical endomorphism category."""
    parent = _construction(name)
    if not _is_owned_object(parent):
        pytest.skip("this construction is not represented in an owned object category")

    endomorphisms = parent.Mor(parent)
    assert endomorphisms in Cat(), f"{name}: Mor must itself be a category"
    assert endomorphisms is parent.Mor(parent), (
        f"{name}: repeated A.Mor(A) calls must return the same category"
    )

    identity = endomorphisms.identity()
    assert identity.parent() is endomorphisms, (
        f"{name}: the identity must belong to the canonical Mor category"
    )
    composite = identity * identity
    assert composite.parent() is endomorphisms, (
        f"{name}: composition must remain in the canonical Mor category"
    )
    assert composite == identity, f"{name}: the represented identity is not a two-sided unit"


def test_a_lattice_subobject_has_the_restricted_form() -> None:
    r"""The inclusion \(i:N\hookrightarrow L\) satisfies \(b_N=i^*b_L\)."""
    _ensure_preamble()
    generator = next(iter(Lattices(ZZ)("E8").module_generators()))
    subobject = Lattices(ZZ)("E8").subobject_on([2 * generator])
    source_generator = next(iter(subobject.module_generators()))
    image = subobject.inclusion()(source_generator)

    assert source_generator.b(source_generator) == image.b(image)


def test_a_constructed_lattice_satisfies_its_defining_properties() -> None:
    r"""A lattice is finite free, integral-valued, and nondegenerate."""
    _ensure_preamble()
    lattice = Lattices(ZZ)("A2")
    module_basis = tuple(lattice.module_generators())

    assert lattice.module_rank() == len(module_basis) == 2
    assert all(left.b(right) in ZZ for left in module_basis for right in module_basis)
    assert lattice.is_nondegenerate() is True
    assert lattice.correlation_morphism().is_injective()


def test_a_degenerate_gram_matrix_does_not_claim_nondegeneracy() -> None:
    r"""A zero determinant does not enter the nondegenerate subcategory."""
    _ensure_preamble()
    formed = Lattices(ZZ)([[1, 1], [1, 1]])

    assert formed in FiniteRankLattices(ZZ)
    assert formed not in NondegenerateLattices(ZZ)


def test_a_degenerate_lattice_answers_its_own_nondegeneracy() -> None:
    r"""$\operatorname{rad}(L)=\ker(v\mapsto b(v,-))$ is askable outside the axiom.

    The Gram matrix $[[1,1],[1,1]]$ has radical $\mathbb Z(e_1-e_2)$, so the
    honest answers are rank one and ``False``.  They must be available on the
    object *before* it enters any nondegenerate category: the axiom's gate
    asks the candidate, so a candidate that cannot answer cannot participate.
    """
    _ensure_preamble()
    formed = Lattices(ZZ)([[1, 1], [1, 1]])

    assert formed.is_nondegenerate() is False
    assert formed.radical().module_rank() == 1
    assert Lattices(ZZ)("A2").is_nondegenerate() is True


def test_refining_a_degenerate_gram_into_nondegenerate_is_refused() -> None:
    r"""Entering ``Nondegenerate`` asserts the radical is the zero module."""
    _ensure_preamble()
    from dzack_research.preamble.refine import refine

    formed = Lattices(ZZ)([[1, 1], [1, 1]])

    with pytest.raises(AssertionError):
        refine(formed, NondegenerateLattices(ZZ))
