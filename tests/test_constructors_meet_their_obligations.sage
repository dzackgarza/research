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
from collections.abc import Callable

import pytest

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.misc.abstract_method import AbstractMethod, abstract_methods_of_class
from sage.structure.parent import Parent

from dzack_research.preamble.categories.forms.forms import (
    BilinearFormMorphism,
    QuadraticFormMorphism,
)
# Imported rather than named: ``install_preamble`` does not list
# ``categories.modules.framed.formed.free_lattices``, so a session cannot
# reach this constructor the way it reaches ``FreeModuleOfRank``.
from dzack_research.preamble.categories.modules.framed.formed.free_lattices import (
    FreeLatticeOfRank,
)
from dzack_research.preamble.categories.modules.tensors import (
    DividedSquare,
    TensorSquare,
)


def _identity_on(source: Parent) -> SetMorphism:
    r"""Return $\mathrm{id}_S$, the arrow the diagram constructors are given.

    A one-object diagram is the smallest cone, cocone, product, coproduct and
    biproduct there is: $S$ is the limit of the diagram $(S)$ with
    $\pi=\mathrm{id}$, and dually the colimit with $\iota=\mathrm{id}$.  The
    identity is also a monomorphism and an epimorphism, which is what
    ``Superobject``, ``Covering`` and ``Covered`` require.

    Each row below is given its own $\Delta[n]$: every one of these
    constructors *refines the object it is handed*, so two rows sharing a set
    would each see the other's placement.
    """
    return SetMorphism(Hom(source, source, Sets()), lambda member: member)


def _ensure_preamble() -> None:
    r"""Make this module a session, the way a session is made.

    The one import, and not ``install_preamble`` plus ``Lattices.install``:
    the table names ``QuaternionGroup``, ``RR``, ``matrix`` and their
    fellows, which the preamble does not export and a lowered module is not
    given.  ``preamble.all`` is a superset of ``sage.all``, so the names the
    specimens are written in resolve here for the same reason they resolve at
    a prompt.
    """
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
    e = list(Lattices.E8.module_generators())
    u = list(Lattices.U.module_generators())
    uu = Lattices.U + Lattices.U
    g = list(uu.module_generators())
    return {
        "Lattices(ring)": lambda: Lattices(ZZ),
        "Lattices(name)": lambda: Lattices("LK3"),
        "Lattices(root system)": lambda: Lattices("A", 2),
        "Lattices(gram)": lambda: Lattices(matrix(ZZ, [[2, 1], [1, 2]])),
        "IntegralLattice(name)": lambda: IntegralLattice("E8"),
        "direct sum": lambda: Lattices.A1 + Lattices.A2,
        "tensor product": lambda: Lattices.U @ Lattices.A2,
        "twist": lambda: Lattices.E8.twist(2),
        "rooted Coxeter diagram from a scaled Cartan type": lambda: CoxeterDiagrams().from_cartan_type(
            ["A", 2], scale=2
        ),
        "dual lattice": lambda: Lattices.A2.dual_lattice(),
        "hyperkaehler lattice": lambda: Lattices.hyperkaehler_lattice("Kum", 2),
        "leech lattice": lambda: Lattices.leech_lattice(),
        "root sublattice": lambda: Lattices.A2.root_sublattice(),
        "symmetric group of a finite set": lambda: Sets.Δ[2].symmetric_group(),
        "subobject": lambda: Lattices.E8.subobject_on([2 * e[0]]),
        "discriminant group": lambda: Lattices.A2.discriminant_group(),
        "discriminant bilinear form": lambda: Lattices.A2.discriminant_bilinear_form(),
        "free module on a set": lambda: FreeModuleOn(ZZ, Sets.Δ[2]),
        "based free module": lambda: BasedFreeModule(ZZ, Sets.Δ[2]),
        "R^n": lambda: ZZ**3,
        # Not the row above: ``ZZ**3`` builds the framed free module on a
        # chosen generating set, while these two are built through the
        # category chain, where the underlying set is the product
        # $R\times\cdots\times R$ and the form is added on top of it.
        "free module of rank n": lambda: FreeModuleOfRank(ZZ, 3),
        "free lattice of rank n": lambda: FreeLatticeOfRank(ZZ, identity_matrix(ZZ, 2)),
        "isometry group": lambda: Lattices.A2.Aut(),
        # A finite abstract group's automorphism group, and the stated-gap
        # specimen: Aut of a free group constructs -- the object exists --
        # while enumeration and order state the algorithmic gap when asked.
        "abstract group automorphism group": lambda: QuaternionGroup().Aut(),
        "free group automorphism group": lambda: FreeGroup(2).Aut(),
        "isometry homset": lambda: Lattices.A2.Isom(Lattices.A2),
        "embedding homset": lambda: Lattices.A1.Emb(Lattices.E8),
        "discriminant image subgroup": lambda: Lattices.A2.Aut().discriminant_image(),
        # The stabilizer of one class in O(A): for A2 the discriminant form is
        # ZZ/3 with O(A) = {+-1}, so the stabilizer of a nonzero class is
        # trivial -- which also puts the empty generating set through the
        # subgroup constructor.
        "discriminant class stabilizer": lambda: Lattices.A2.discriminant_group()
        .automorphism_group()
        .stabilizer_of_element(
            list(Lattices.A2.discriminant_group().module_generators())[0]
        ),
        "special orthogonal subgroup": lambda: Lattices.A2.Aut().special_orthogonal_subgroup(),
        "spinor kernel subgroup": lambda: Lattices.U.Aut().spinor_kernel_subgroup(),
        "stable orthogonal group": lambda: Lattices.A2.stable_orthogonal_group(),
        "vector stabilizer subgroup": lambda: Lattices.A2.Aut().stabilizer_of_vector(
            list(Lattices.A2.module_generators())[0]
        ),
        "isotropic line stabilizer subgroup": lambda: Lattices.U.Aut().stabilizer_of_isotropic_line(
            u[0]
        ),
        "isotropic plane stabilizer subgroup": lambda: uu.Aut().stabilizer_of_isotropic_plane(
            (g[0], g[2])
        ),
        "isotropic flag stabilizer subgroup": lambda: uu.Aut().stabilizer_of_isotropic_flag(
            (g[0], g[2])
        ),
        "character-kernel subgroup intersection": lambda: Lattices.U.Aut()
        .special_orthogonal_subgroup()
        .intersection(Lattices.U.Aut().spinor_kernel_subgroup()),
        "free algebra": lambda: FreeAlgebraOn(QQ, Sets.Δ[1]),
        "tensor algebra": lambda: TensorAlgebraOn(QQ, Sets.Δ[1]),
        "alternating algebra": lambda: AlternatingAlgebraOn(QQ, Sets.Δ[1]),
        "divided power algebra": lambda: DividedPowerAlgebraOn(QQ, Sets.Δ[1]),
        "tensor algebra degree two": lambda: TensorAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "symmetric algebra degree two": lambda: FreeAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "alternating algebra degree two": lambda: AlternatingAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "divided power algebra degree two": lambda: DividedPowerAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "mixed tensor": lambda: Tensor(BasedFreeModule(QQ, Sets.Δ[1]), (1, 1)),
        "smooth function module": lambda: smooth_functions(RR),
        "square-integrable function module": lambda: square_integrable_functions(RR),
        "cartesian product of sets": lambda: CartesianProductOfSets((Sets.Δ[1], Sets.Δ[2])),
        "polynomial ring": lambda: QQ["x"],
        "prime field": lambda: PrimeField(3),
        "a ring as an algebra over itself": lambda: ZZ,
        "subobject sum": lambda: Lattices.E8.subobject_on([2 * e[0]]).sum(
            Lattices.E8.subobject_on([3 * e[1]])
        ),
        "subobject intersection": lambda: Lattices.E8.subobject_on([2 * e[0], 2 * e[1]])
        .intersection(Lattices.E8.subobject_on([3 * e[0], 3 * e[1]])),
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
        "underlying set of a lattice": lambda: UnderlyingSet(Lattices.A2),
        "set from an iterable": lambda: Set([1, 2, 3]),
        "condition set": lambda: ConditionSet(ZZ, lambda n: n > 0),
        "image set": lambda: ImageSet(lambda n: n, Sets.Δ[2]),
        # ---- categorical constructions ----
        "functor space": lambda: FunctorSpace(Cat(), Cat()),
        "coproduct of sets": lambda: CoproductOfSets((Sets.Δ[1], Sets.Δ[2])),
        "isomorphism homset": lambda: IsoAr(Lattices.A2, Lattices.A2),
        # The five limit constructors, on one-object diagrams.  Not the direct
        # sum row above: ``Lattices.A1 + Lattices.A2`` goes through the
        # lattice-specific block-diagonal sum and reaches none of these.
        "cone": lambda: Cone((_identity_on(Sets.Δ[11]),)),
        "cocone": lambda: Cocone((_identity_on(Sets.Δ[12]),)),
        "product": lambda: Product((_identity_on(Sets.Δ[13]),)),
        "coproduct": lambda: Coproduct((_identity_on(Sets.Δ[14]),)),
        "biproduct": lambda: Biproduct(
            (_identity_on(Sets.Δ[15]),), (_identity_on(Sets.Δ[15]),)
        ),
        "superobject": lambda: Superobject(_identity_on(Sets.Δ[18])),
        "covering object": lambda: Covering(_identity_on(Sets.Δ[16])),
        "covered object": lambda: Covered(_identity_on(Sets.Δ[17])),
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
        "toric scheme": lambda: ToricScheme(LatticePolytope([[0, 0], [1, 0], [0, 1]])),
        "toric subscheme": lambda: ToricSubscheme(
            ToricScheme(LatticePolytope([[0, 0], [1, 0], [0, 1]])), (0,)
        ),
        "toric variety": lambda: ToricVariety(
            LatticePolytope([[1, 0], [0, 1], [-1, -1]]).normal_fan()
        ),
        "curve": lambda: Curve(AffineSpace(2, QQ).coordinate_ring().gens()[0]),
        "toric log pair": lambda: ToricLogPair(
            ToricVariety(LatticePolytope([[1, 0], [0, 1], [-1, -1]]).normal_fan())
        ),
        "ade surface": lambda: ADESurface("A", 1),
        "ade base surface": lambda: ADEBaseSurface(ADESurface("A", 1)),
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
        "divided power algebra of a module": lambda: DividedPowerAlgebraOf(
            BasedFreeModule(QQ, Sets.Δ[1])
        ),
        # ---- modules ----
        # Not the ``mixed tensor`` row above: that is one bidegree $T^{p,q}M$,
        # this is the whole graded algebra $\bigoplus_{p,q}T^{p,q}M$.
        "mixed tensor algebra": lambda: MixedTensorAlgebra(BasedFreeModule(QQ, Sets.Δ[1])),
        "fractional ideal": lambda: FractionalIdeal(ZZ, [2]),
        # The two square constructions on an arbitrary module rather than on a
        # free algebra's graded piece: they are where a form's domain comes
        # from, so a lattice is the specimen that matters.
        "tensor square": lambda: TensorSquare(Lattices.A2),
        "divided square": lambda: DividedSquare(Lattices.A2),
        # Not the ``torsion module`` path: this presents a module by a chosen
        # morphism of free modules.
        "finitely presented module": lambda: FinitelyPresentedModule(
            FreeModuleOn(ZZ, Sets.Δ[0]).hom(
                {0: FreeModuleOn(ZZ, Sets.Δ[0]).module_generator(0) * 2},
                FreeModuleOn(ZZ, Sets.Δ[0]),
            )
        ),
        # ---- forms ----
        # A quadratic map supplied by its value function, before any
        # classifying morphism is formed.
        "quadratic map": lambda: QuadraticMap(Lattices.A2, ZZ, lambda x: x.b(x)),
        # The two form homsets: built transiently everywhere a form is made,
        # and never asked for themselves.
        "bilinear form homset": lambda: BilinearForms(Lattices.A2, ZZ),
        "quadratic form homset": lambda: QuadraticForms(Lattices.A2, ZZ),
    }


def _discriminant_quadratic_from_data() -> Parent:
    r"""The independent torsion-quadratic-form constructor: $q$ on $\ZZ/2$
    with $q(e)=-1/2$, the $A_1$ discriminant form built from data alone."""
    from sage.matrix.constructor import matrix as _matrix
    from sage.rings.integer_ring import ZZ as _ZZ
    from sage.rings.rational_field import QQ as _QQ

    from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_quadratic_modules import (
        DiscriminantQuadraticModules,
    )

    return DiscriminantQuadraticModules(_ZZ).from_relations_and_gram(
        _matrix(_ZZ, [[2]]), _matrix(_QQ, [[-_QQ(1) / 2]])
    )


def _discriminant_bilinear_from_data() -> Parent:
    r"""The independent torsion-bilinear-form constructor: $b$ on $\ZZ/2$
    with $b(e,e)=1/2$, built from data alone."""
    from sage.matrix.constructor import matrix as _matrix
    from sage.rings.integer_ring import ZZ as _ZZ
    from sage.rings.rational_field import QQ as _QQ

    from dzack_research.preamble.categories.modules.framed.formed.torsionform.discriminant_bilinear_modules import (
        DiscriminantBilinearModules,
    )

    return DiscriminantBilinearModules(_ZZ).from_relations_and_gram(
        _matrix(_ZZ, [[2]]), _matrix(_QQ, [[_QQ(1) / 2]])
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
        # Both forms are morphisms out of a square construction of the module:
        # a bilinear form on $M\otimes_R M$, a quadratic form on $\Gamma^2M$.
        # A quadratic form is not linear on $M$ -- $q(rx)=r^2q(x)$ -- so it is
        # not a map out of $M$ at all, and the divided square is what makes it
        # a morphism without pretending otherwise.
        domain = form.domain()
        expected_constructor = {
            BilinearFormMorphism: TensorSquare,
            QuadraticFormMorphism: DividedSquare,
        }[type(form)]
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


def test_a_lattice_subobject_has_the_restricted_form() -> None:
    r"""The inclusion \(i:N\hookrightarrow L\) satisfies \(b_N=i^*b_L\)."""
    _ensure_preamble()
    generator = next(iter(Lattices.E8.module_generators()))
    subobject = Lattices.E8.subobject_on([2 * generator])
    source_generator = next(iter(subobject.module_generators()))
    image = subobject.inclusion()(source_generator)

    assert source_generator.b(source_generator) == image.b(image)


def test_a_constructed_lattice_satisfies_its_defining_properties() -> None:
    r"""A lattice is finite free, integral-valued, and nondegenerate."""
    _ensure_preamble()
    lattice = Lattices.A2
    generators = tuple(lattice.module_generators())

    assert lattice.relations().cardinality() == 0
    assert lattice.rank() == len(generators) == 2
    assert all(left.b(right) in ZZ for left in generators for right in generators)
    assert lattice.correlation_morphism().is_injective()


def test_a_degenerate_gram_matrix_does_not_claim_nondegeneracy() -> None:
    r"""A zero determinant does not enter the nondegenerate subcategory."""
    _ensure_preamble()
    formed = Lattices(matrix(ZZ, [[1, 1], [1, 1]]))

    assert formed in Lattices(ZZ).FinitelyGenerated().Integral()
    assert formed not in Lattices(ZZ).Nondegenerate()
    assert formed not in IntegralLattices(ZZ)


def test_a_degenerate_lattice_answers_its_own_nondegeneracy() -> None:
    r"""$\operatorname{rad}(L)=\ker(v\mapsto b(v,-))$ is askable outside the axiom.

    The Gram matrix $[[1,1],[1,1]]$ has radical $\mathbb Z(e_1-e_2)$, so the
    honest answers are rank one and ``False``.  They must be available on the
    object *before* it enters any nondegenerate category: the axiom's gate
    asks the candidate, so a candidate that cannot answer cannot participate.
    """
    _ensure_preamble()
    formed = Lattices(matrix(ZZ, [[1, 1], [1, 1]]))

    assert formed.is_nondegenerate() is False
    assert formed.radical().rank() == 1
    assert Lattices("A2").is_nondegenerate() is True


def test_refining_a_degenerate_gram_into_nondegenerate_is_refused() -> None:
    r"""Entering ``Nondegenerate`` asserts the radical is the zero module."""
    _ensure_preamble()
    from dzack_research.preamble.refine import refine

    formed = Lattices(matrix(ZZ, [[1, 1], [1, 1]]))

    with pytest.raises(AssertionError):
        refine(formed, Lattices(ZZ).Nondegenerate())


def test_a_half_integral_form_is_refused_the_integral_axiom() -> None:
    r"""$b(e_1,e_2)=1/2$ puts the scale outside $\mathbb Z$, and the gate says so.

    Integrality is a statement about the form's values: every $b(x,y)$ is
    integral over $\mathbb Z$ inside the value ring.  $A_2$ has scale
    $\mathbb Z$ and passes; the half-integral form fails, and refinement
    into the ``Integral`` axiom refuses it.
    """
    _ensure_preamble()
    from dzack_research.preamble.refine import refine

    half = BilinearForm(
        BasedFreeModule(ZZ, 2),
        QQ,
        matrix(QQ, [[1, 1 / 2], [1 / 2, 1]]),
    )

    assert half.is_integral() is False
    assert Lattices("A2").is_integral() is True
    with pytest.raises(AssertionError):
        refine(half, Lattices(ZZ).Integral())


def test_a_torsion_valued_form_has_no_integrality_and_routes_past_the_axiom() -> None:
    r"""$b_L:A_L\times A_L\to\mathbb Q/\mathbb Z$: nothing there is integral.

    Integrality has one a priori meaning -- integrality over the image of a
    ring morphism -- and $\mathbb Q/\mathbb Z$ is not a ring, so there is no
    morphism from $\mathbb Z$ to be integral over.  The answer is ``False``
    and the discriminant form routes past the ``Integral`` axiom: a
    different category, not an error.
    """
    _ensure_preamble()
    disc = Lattices.A2.discriminant_bilinear_form()

    assert disc.is_integral() is False
    assert disc not in Lattices(ZZ).Integral()


def test_the_scale_submodule_is_generated_by_the_forms_values() -> None:
    r"""$\mathfrak s(L)\subseteq W$ is the $R$-submodule generated by the $b(x,y)$.

    Definitionally the image of $b$.  When $W=R$ an $R$-submodule of $R$ is
    an ideal, and that is how it is presented (O'Meara §82:8 calls it the
    scale): $A_2$ has Gram entries $\{\pm 2,\mp 1\}$, so
    $\mathfrak s=\mathbb Z$; $A_2$ twisted by $3$ has
    $\mathfrak s=3\mathbb Z$, a proper ideal -- which is what separates the
    scale from a yes/no integrality bit.
    """
    _ensure_preamble()
    lattice = Lattices("A2")

    assert lattice.scale_submodule() == ZZ.ideal(1)
    assert lattice.twist(3).scale_submodule() == ZZ.ideal(3)
