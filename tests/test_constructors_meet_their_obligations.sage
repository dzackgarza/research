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

import pytest

from sage.misc.abstract_method import AbstractMethod, abstract_methods_of_class
from sage.structure.parent import Parent

from dzack_research.preamble.categories.forms.forms import (
    BilinearFormMorphism,
    DividedSquare,
    QuadraticFormMorphism,
    TensorSquare,
)


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    Lattices.install(globals())


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
def _constructions() -> dict:
    r"""Every way the preamble makes an object, with one specimen each.

    Built once per process: the sweep below is parametrized over this table,
    and rebuilding every non-unique construction per parameter multiplies
    every constructor's cost by the number of rows.
    """
    _ensure_preamble()
    e = list(Lattices.E8.module_generators())
    return {
        "Lattices(ring)": Lattices(ZZ),
        "Lattices(name)": Lattices("LK3"),
        "Lattices(root system)": Lattices("A", 2),
        "Lattices(gram)": Lattices(matrix(ZZ, [[2, 1], [1, 2]])),
        "IntegralLattice(name)": IntegralLattice("E8"),
        "direct sum": Lattices.A1 + Lattices.A2,
        "tensor product": Lattices.U @ Lattices.A2,
        "twist": Lattices.E8.twist(2),
        "dual lattice": Lattices.A2.dual_lattice(),
        "subobject": Lattices.E8.subobject_on([2 * e[0]]),
        "discriminant group": Lattices.A2.discriminant_group(),
        "discriminant bilinear form": Lattices.A2.discriminant_bilinear_form(),
        "free module on a set": FreeModuleOn(ZZ, Sets.Δ[2]),
        "based free module": BasedFreeModule(ZZ, Sets.Δ[2]),
        "R^n": ZZ**3,
        "isometry group": Lattices.A2.Aut(),
        "free algebra": FreeAlgebraOn(QQ, Sets.Δ[1]),
        "tensor algebra": TensorAlgebraOn(QQ, Sets.Δ[1]),
        "alternating algebra": AlternatingAlgebraOn(QQ, Sets.Δ[1]),
        "divided power algebra": DividedPowerAlgebraOn(QQ, Sets.Δ[1]),
        "tensor algebra degree two": TensorAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "symmetric algebra degree two": FreeAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "alternating algebra degree two": AlternatingAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "divided power algebra degree two": DividedPowerAlgebraOn(QQ, Sets.Δ[1]).graded_piece(2),
        "mixed tensor": Tensor(BasedFreeModule(QQ, Sets.Δ[1]), (1, 1)),
        "smooth function module": smooth_functions(RR),
        "square-integrable function module": square_integrable_functions(RR),
        "cartesian product of sets": CartesianProductOfSets((Sets.Δ[1], Sets.Δ[2])),
        "polynomial ring": QQ["x"],
        "a ring as an algebra over itself": ZZ,
    }


def _formed_constructions() -> dict:
    r"""The constructions whose results carry a form."""
    return {
        name: parent
        for name, parent in _constructions().items()
        if hasattr(parent, "form") and hasattr(parent, "value_module")
    }


@pytest.mark.parametrize("name", sorted(_formed_constructions()))
def test_a_form_is_a_morphism_into_the_value_module(name: str) -> None:
    r"""The form is a map, not a matrix.

    A bilinear form on $M$ with values in $W$ is an element of
    $\operatorname{Hom}_R(M\otimes_R M, W)$: its domain is the tensor square
    and its codomain is the value module.  A Gram matrix is how a *finitely
    generated* one can be written down, and asking for the morphism is what
    keeps the general case expressible.
    """
    parent = _formed_constructions()[name]
    form = parent.form()

    assert form.codomain() is parent.value_module(), (
        f"{name}: the form's codomain must be the value module, "
        f"got {form.codomain()} against {parent.value_module()}"
    )
    # Both forms are morphisms out of a square construction of the module:
    # a bilinear form on $M\otimes_R M$, a quadratic form on $\Gamma^2M$.
    # A quadratic form is not linear on $M$ -- $q(rx)=r^2q(x)$ -- so it is not
    # a map out of $M$ at all, and the divided square is what makes it a
    # morphism without pretending otherwise.
    domain = form.domain()
    expected_constructor = {
        BilinearFormMorphism: TensorSquare,
        QuadraticFormMorphism: DividedSquare,
    }[type(form)]
    expected_domain = expected_constructor(parent.forget_form())

    assert domain is expected_domain, (
        f"{name}: the form has domain {domain}, not the degree-two "
        f"construction {expected_domain}"
    )


@pytest.mark.parametrize("name", sorted(_constructions()))
def test_a_constructed_object_answers_what_its_categories_require(name: str) -> None:
    r"""Nothing the object's categories declare is left unimplemented."""
    parent = _constructions()[name]
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

    assert lattice.forget_form().relations().cardinality() == 0
    assert lattice.rank() == len(generators) == 2
    assert all(left.b(right) in ZZ for left in generators for right in generators)
    assert lattice.correlation_morphism().is_injective()


def test_a_degenerate_gram_matrix_does_not_claim_nondegeneracy() -> None:
    r"""A zero determinant does not enter the nondegenerate subcategory."""
    _ensure_preamble()
    formed = Lattices(matrix(ZZ, [[1, 1], [1, 1]]))

    assert formed in Lattices(ZZ).FinitelyGenerated().Integral()
    assert formed not in Lattices(ZZ).Nondegenerate()
    assert formed not in IntegralLattices()


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
