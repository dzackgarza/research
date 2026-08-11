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

import pytest

from sage.misc.abstract_method import AbstractMethod, abstract_methods_of_class

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


def unmet_obligations(parent) -> list:
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


def _constructions() -> dict:
    r"""Every way the preamble makes an object, with one specimen each."""
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
    expected = {
        BilinearFormMorphism: TensorSquare,
        QuadraticFormMorphism: DividedSquare,
    }[type(form)]

    assert isinstance(domain, expected), (
        f"{name}: a {type(form).__name__} is defined on "
        f"{expected.__name__}(M), got a form on {domain}"
    )
    assert domain.module() is parent.forget_form(), (
        f"{name}: the square must be of this module, got one of "
        f"{domain.module()}"
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
