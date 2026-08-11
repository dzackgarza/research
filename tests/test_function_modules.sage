r"""Modules whose elements are functions, and a form given by an integral.

$C^\infty(\RR)$ and $L^2(\RR)$ have no finite generating set, no coordinates
and no Gram matrix.  What they do have is the module structure and, for
$L^2$, a bilinear form $\langle f,g\rangle=\int fg$.  So they exercise the
parts of the preamble that are about being a module rather than about being a
finitely generated one, and a construction that quietly assumed coordinates
fails here rather than years later.

Shells: smoothness and square-integrability are not checked, and neither is
the bilinearity of the pairing.  None of that is decidable here.  The
mathematics asserted below is what *is* decidable -- the module axioms on
specimens, and the values of an integral computed two ways.
"""


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    Lattices.install(globals())


def _smooth():
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.function_modules import smooth_functions

    return smooth_functions(RR)


def _square_integrable():
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.function_modules import (
        square_integrable_functions,
    )

    return square_integrable_functions(RR)


def _integral_pairing():
    r"""Return $\langle f,g\rangle=\int_{-1}^{1}fg$, on the symbolic variable."""
    t = var("t")
    return lambda f, g: (f(t) * g(t)).integrate(t, -1, 1)


def test_functions_form_a_module_over_the_reals() -> None:
    r"""Addition is pointwise and scaling is pointwise, on functions."""
    C = _smooth()
    f = C(lambda x: x**2)
    g = C(lambda x: x)

    assert (f + g)(3) == 12, "(x^2 + x)(3) = 12"
    assert (2 * f)(3) == 18, "(2x^2)(3) = 18"
    assert (f - f)(3) == 0
    assert (f + C.zero())(3) == f(3)


def test_the_module_action_needs_no_generating_set() -> None:
    r"""$\rho(r)$ is scaling, read off nothing.

    The obligation is about being a module, and this module has no generators
    to read an action off -- so it supplies one directly, which is what a
    module that is not finitely generated has to be able to do.
    """
    C = _smooth()
    f = C(lambda x: x**2)

    action = C._ring_morphism_defining_module_action()

    assert action(RR(2))(f)(3) == 18
    assert action(RR(1))(f)(3) == f(3), "the identity scalar acts as the identity"
    assert action(RR(0))(f)(3) == 0


def test_a_form_can_be_given_by_its_pairing_rather_than_a_matrix() -> None:
    r"""$\langle f,g\rangle=\int_{-1}^1 fg$ is a form on a module with no basis.

    A Gram matrix is how a finitely generated form is written down.  $L^2$ has
    no finite generating family to run over, so the form is stated as the
    pairing it is.
    """
    from dzack_research.preamble.categories.forms.forms import BilinearForms

    L2 = _square_integrable()
    form = BilinearForms(L2, RR)(_integral_pairing())
    x = L2(lambda t: t)
    x_squared = L2(lambda t: t**2)

    assert abs(form(x, x) - RR(2) / 3) < 1e-9, "int_{-1}^{1} t^2 = 2/3"
    assert abs(form(x, x_squared)) < 1e-9, "int_{-1}^{1} t^3 = 0, by parity"
    assert abs(form(x_squared, x_squared) - RR(2) / 5) < 1e-9, "int_{-1}^{1} t^4 = 2/5"


def test_that_form_is_symmetric_and_bilinear_on_specimens() -> None:
    r"""Bilinearity cannot be checked in general, so it is checked on cases.

    The pairing is trusted -- nothing here can decide bilinearity of an
    arbitrary callable -- but a form that failed it on these specimens would
    not be one, and the integral is the reason it holds.
    """
    from dzack_research.preamble.categories.forms.forms import BilinearForms

    L2 = _square_integrable()
    form = BilinearForms(L2, RR)(_integral_pairing())
    x = L2(lambda t: t)
    x_squared = L2(lambda t: t**2)

    assert abs(form(x, x_squared) - form(x_squared, x)) < 1e-9, "symmetric"
    assert abs(form(2 * x, x_squared) - 2 * form(x, x_squared)) < 1e-9, "linear in the first slot"
    assert abs(
        form(x + x_squared, x) - form(x, x) - form(x_squared, x)
    ) < 1e-9, "additive in the first slot"


def test_such_a_form_has_no_gram_matrix_and_says_so() -> None:
    r"""Asking for coordinates of a module that has none is refused.

    Not an oversight to paper over: the entries of a Gram matrix are the
    pairings of a finite generating family, and there is no such family here.
    """
    import pytest

    from dzack_research.preamble.categories.forms.forms import BilinearForms

    L2 = _square_integrable()
    form = BilinearForms(L2, RR)(_integral_pairing())

    with pytest.raises(AssertionError, match="no finite generating set"):
        form.gram_matrix()


def test_a_finitely_generated_form_still_has_one() -> None:
    r"""The general case does not cost the finite one its Gram matrix."""
    assert Lattices.A2.form().gram_matrix() is not None
    assert Lattices.A2.gram_matrix().list() == [-2, 1, 1, -2]
