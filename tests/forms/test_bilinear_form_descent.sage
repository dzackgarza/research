r"""Descent of a bilinear form to a quotient by vectors in its radical.

A bilinear form \(b\) on \(M\) descends along \(\rho\colon N\to M\) to
\(\operatorname{coker}\rho\) exactly when \(b(\rho(n), m) = 0\) for all \(n, m\); the
descended form is \(\bar b(\bar x,\bar y) = b(x,y)\).  The Gram
\(\begin{pmatrix}1&1\\1&1\end{pmatrix}\) on \(\mathbf Z^2\) has radical
\(\mathbf Z(e_0-e_1)\), so it descends along \(1\mapsto e_0-e_1\) to
\(\mathbf Z^2/\mathbf Z(e_0-e_1)\cong\mathbf Z\), where the classes of \(e_0\) and \(e_1\) coincide and have square
\(b(e_0,e_0)=1\).  It does not descend along \(1\mapsto e_0\), since \(b(e_0,e_0)=1\ne0\).
Its pullback along \(1\mapsto e_0+e_1\) has value \(b(e_0+e_1,e_0+e_1)=4\).
"""

from dzack_research.preamble.all import *


def test_a_rational_valued_form_descends_to_the_quotient_by_its_radical() -> None:
    module = ZZ.free_module(2)
    first, second = module.module_generators()
    line = ZZ.free_module(1)
    radical = line.Mor(module)((first - second,))
    form = module.bilinear_forms(QQ)([[1, 1], [1, 1]])
    identity = QQ.Mor(QQ).identity()
    descended = form.descend_along(radical, identity)
    first_class, second_class = descended.module().module_generators()

    assert form.descends_along(radical, identity)
    assert not form.descends_along(line.Mor(module)((first,)), identity)
    assert descended(first_class, first_class) == 1
    assert descended(first_class, second_class) == 1


def test_the_form_of_a_degenerate_lattice_descends_only_along_its_radical() -> None:
    lattice = Lattices(ZZ)([[1, 1], [1, 1]])
    form = lattice.form()
    module = form.module()
    first, second = module.module_generators()
    line = ZZ.free_module(1)
    identity = ZZ.Mor(ZZ).identity()

    assert form.descends_along(line.Mor(module)((first - second,)), identity)
    assert not form.descends_along(line.Mor(module)((first,)), identity)


def test_the_descended_form_of_a_degenerate_lattice() -> None:
    lattice = Lattices(ZZ)([[1, 1], [1, 1]])
    form = lattice.form()
    module = form.module()
    first, second = module.module_generators()
    line = ZZ.free_module(1)
    descended = form.descend_along(line.Mor(module)((first - second,)), ZZ.Mor(ZZ).identity())
    first_class, second_class = descended.module().module_generators()

    assert descended(first_class, first_class) == 1
    assert descended(first_class, second_class) == 1


def test_the_pullback_of_a_lattice_form_along_the_diagonal() -> None:
    lattice = Lattices(ZZ)([[1, 1], [1, 1]])
    form = lattice.form()
    module = form.module()
    first, second = module.module_generators()
    line = ZZ.free_module(1)
    (generator,) = line.module_generators()
    pulled_back = form.pullback(line.Mor(module)((first + second,)))

    assert pulled_back(generator, generator) == 4
