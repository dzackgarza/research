"""
Mathematical specification tests for the lattice foundation.

The assertions in this file are organized by root-lattice family and record
exact facts from the theory: Gram matrices, determinants, signatures, parity,
scale, divisibilities of the simple roots, norms of the simple roots, absence
of isotropic simple roots, and exact discriminant-form isometry classes.
"""

from __future__ import annotations

import pytest
from sage.all import QQ, ZZ, IntegralLattice, matrix
from src.lattices.lattices import DiscriminantGroup, Lattice


def q(num: int, den: int = 1):
    return QQ(num) / QQ(den)


def trivial_discriminant_form(*, even: bool) -> DiscriminantGroup:
    return DiscriminantGroup.from_invariants_and_gram((), [], quadratic_modulus=2 if even else 1)


def an_gram(n: int):
    return matrix(
        ZZ,
        [[-2 if i == j else 1 if abs(i - j) == 1 else 0 for j in range(n)] for i in range(n)],
    )


def bn_gram(n: int):
    rows = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        rows[i][i] = -2
    rows[-1][-1] = -1
    for i in range(n - 1):
        rows[i][i + 1] = 1
        rows[i + 1][i] = 1
    return matrix(ZZ, rows)


def cn_gram(n: int):
    rows = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        rows[i][i] = -2
    rows[-1][-1] = -4
    for i in range(n - 2):
        rows[i][i + 1] = 1
        rows[i + 1][i] = 1
    rows[-2][-1] = 2
    rows[-1][-2] = 2
    if n == 2:
        rows[0][1] = 2
        rows[1][0] = 2
    return matrix(ZZ, rows)


def dn_gram(n: int):
    if n == 4:
        return matrix(
            ZZ,
            [
                [-2, 1, 0, 0],
                [1, -2, 1, 1],
                [0, 1, -2, 0],
                [0, 1, 0, -2],
            ],
        )
    rows = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        rows[i][i] = -2
    for i in range(n - 3):
        rows[i][i + 1] = 1
        rows[i + 1][i] = 1
    branch = n - 3
    rows[branch][branch + 1] = 1
    rows[branch + 1][branch] = 1
    rows[branch][branch + 2] = 1
    rows[branch + 2][branch] = 1
    return matrix(ZZ, rows)


def e_gram(n: int):
    tables = {
        6: [
            [-2, 0, 1, 0, 0, 0],
            [0, -2, 0, 1, 0, 0],
            [1, 0, -2, 1, 0, 0],
            [0, 1, 1, -2, 1, 0],
            [0, 0, 0, 1, -2, 1],
            [0, 0, 0, 0, 1, -2],
        ],
        7: [
            [-2, 0, 1, 0, 0, 0, 0],
            [0, -2, 0, 1, 0, 0, 0],
            [1, 0, -2, 1, 0, 0, 0],
            [0, 1, 1, -2, 1, 0, 0],
            [0, 0, 0, 1, -2, 1, 0],
            [0, 0, 0, 0, 1, -2, 1],
            [0, 0, 0, 0, 0, 1, -2],
        ],
        8: [
            [-2, 0, 1, 0, 0, 0, 0, 0],
            [0, -2, 0, 1, 0, 0, 0, 0],
            [1, 0, -2, 1, 0, 0, 0, 0],
            [0, 1, 1, -2, 1, 0, 0, 0],
            [0, 0, 0, 1, -2, 1, 0, 0],
            [0, 0, 0, 0, 1, -2, 1, 0],
            [0, 0, 0, 0, 0, 1, -2, 1],
            [0, 0, 0, 0, 0, 0, 1, -2],
        ],
    }
    return matrix(ZZ, tables[n])


def cd_even_discriminant_form(n: int) -> DiscriminantGroup:
    diagonal = q(-n, 4)
    off_diagonal = q(1, 2) if n % 4 == 0 else 0
    return DiscriminantGroup.from_invariants_and_gram(
        (2, 2),
        [
            [diagonal, off_diagonal],
            [off_diagonal, diagonal],
        ],
    )


def generator_norms(lattice: Lattice):
    return tuple(generator.inner_product(generator) for generator in lattice.gens())


def generator_divisibilities(lattice: Lattice):
    return tuple(generator.divisibility() for generator in lattice.gens())


def generator_isotropy(lattice: Lattice):
    return tuple(generator.is_isotropic() for generator in lattice.gens())


class TestRoutingAndVocabulary:
    def test_named_routing_agrees_with_sage_named_lattices(self):
        assert Lattice.from_gram(IntegralLattice("A1").gram_matrix()).is_isometric_to(Lattice.Z().rescale(2))
        assert Lattice.from_gram(-IntegralLattice("A1").inner_product_matrix()).is_isometric_to(Lattice.A(1))
        assert Lattice.from_gram(-IntegralLattice("E8").inner_product_matrix()).is_isometric_to(Lattice.E(8))
        assert Lattice.from_gram(IntegralLattice("U").gram_matrix()).is_isometric_to(Lattice.U())

    def test_scale_is_the_pairing_ideal_and_rescale_changes_the_form(self):
        positive_line = Lattice.Z()
        negative_root = Lattice.A(1)
        assert positive_line.scale() == 1
        assert negative_root.scale() == 2
        assert positive_line.rescale(2).gram_matrix() == matrix(ZZ, [[2]])
        assert negative_root.rescale(q(1, 2)).gram_matrix() == matrix(QQ, [[-1]])


class TestAnFamily:
    @pytest.mark.parametrize("n", range(1, 11))
    def test_an_root_lattices_match_their_theory(self, n: int):
        lattice = Lattice.A(n)
        discriminant_form = DiscriminantGroup.from_invariants_and_gram(
            (n + 1,),
            [[q(-n, n + 1)]],
        )
        expected_divisibilities = (2,) if n == 1 else (1,) * n
        assert lattice.gram_matrix() == an_gram(n)
        assert lattice.det() == ((-1) ** n) * (n + 1)
        assert lattice.is_even()
        assert lattice.scale() == (2 if n == 1 else 1)
        assert lattice.signature() == (0, n)
        assert generator_norms(lattice) == (-2,) * n
        assert generator_divisibilities(lattice) == expected_divisibilities
        assert generator_isotropy(lattice) == (False,) * n
        assert lattice.discriminant_group().is_isometric_to(discriminant_form)


class TestBnFamily:
    @pytest.mark.parametrize("n", range(2, 11))
    def test_bn_root_lattices_match_their_theory(self, n: int):
        lattice = Lattice.B(n)
        assert lattice.gram_matrix() == bn_gram(n)
        assert lattice.det() == (-1) ** n
        assert not lattice.is_even()
        assert lattice.scale() == 1
        assert lattice.signature() == (0, n)
        assert generator_norms(lattice) == (-2,) * (n - 1) + (-1,)
        assert generator_divisibilities(lattice) == (1,) * n
        assert generator_isotropy(lattice) == (False,) * n
        assert lattice.discriminant_group().is_isometric_to(trivial_discriminant_form(even=False))


class TestCnFamily:
    @pytest.mark.parametrize("n", range(2, 11))
    def test_cn_root_lattices_match_their_theory(self, n: int):
        lattice = Lattice.C(n)
        if n % 2:
            discriminant_form = DiscriminantGroup.from_invariants_and_gram((4,), [[q(-n, 4)]])
        else:
            discriminant_form = cd_even_discriminant_form(n)
        expected_divisibilities = (2, 2) if n == 2 else (1,) * (n - 1) + (2,)
        assert lattice.gram_matrix() == cn_gram(n)
        assert lattice.det() == 4 * ((-1) ** n)
        assert lattice.is_even()
        assert lattice.scale() == (2 if n == 2 else 1)
        assert lattice.signature() == (0, n)
        assert generator_norms(lattice) == (-2,) * (n - 1) + (-4,)
        assert generator_divisibilities(lattice) == expected_divisibilities
        assert generator_isotropy(lattice) == (False,) * n
        assert lattice.discriminant_group().is_isometric_to(discriminant_form)


class TestDnFamily:
    @pytest.mark.parametrize("n", range(4, 11))
    def test_dn_root_lattices_match_their_theory(self, n: int):
        lattice = Lattice.D(n)
        if n % 2:
            discriminant_form = DiscriminantGroup.from_invariants_and_gram((4,), [[q(-n, 4)]])
        else:
            discriminant_form = cd_even_discriminant_form(n)
        assert lattice.gram_matrix() == dn_gram(n)
        assert lattice.det() == 4 * ((-1) ** n)
        assert lattice.is_even()
        assert lattice.scale() == 1
        assert lattice.signature() == (0, n)
        assert generator_norms(lattice) == (-2,) * n
        assert generator_divisibilities(lattice) == (1,) * n
        assert generator_isotropy(lattice) == (False,) * n
        assert lattice.discriminant_group().is_isometric_to(discriminant_form)


class TestExceptionalFamilies:
    @pytest.mark.parametrize(
        ("rank", "determinant", "discriminant_form"),
        [
            (6, 3, DiscriminantGroup.from_invariants_and_gram((3,), [[q(2, 3)]])),
            (7, -2, DiscriminantGroup.from_invariants_and_gram((2,), [[q(1, 2)]])),
            (8, 1, trivial_discriminant_form(even=True)),
        ],
    )
    def test_en_root_lattices_match_their_theory(
        self,
        rank: int,
        determinant: int,
        discriminant_form: DiscriminantGroup,
    ):
        lattice = Lattice.E(rank)
        assert lattice.gram_matrix() == e_gram(rank)
        assert lattice.det() == determinant
        assert lattice.is_even()
        assert lattice.scale() == 1
        assert lattice.signature() == (0, rank)
        assert generator_norms(lattice) == (-2,) * rank
        assert generator_divisibilities(lattice) == (1,) * rank
        assert generator_isotropy(lattice) == (False,) * rank
        assert lattice.discriminant_group().is_isometric_to(discriminant_form)

    def test_f4_root_lattice_matches_its_theory(self):
        lattice = Lattice.F(4)
        discriminant_form = DiscriminantGroup.from_invariants_and_gram(
            (2, 2),
            [
                [1, q(1, 2)],
                [q(1, 2), 1],
            ],
        )
        assert lattice.gram_matrix() == matrix(
            ZZ,
            [
                [-4, 2, 0, 0],
                [2, -4, 2, 0],
                [0, 2, -2, 1],
                [0, 0, 1, -2],
            ],
        )
        assert lattice.det() == 4
        assert lattice.is_even()
        assert lattice.scale() == 1
        assert lattice.signature() == (0, 4)
        assert generator_norms(lattice) == (-4, -4, -2, -2)
        assert generator_divisibilities(lattice) == (2, 2, 1, 1)
        assert generator_isotropy(lattice) == (False, False, False, False)
        assert lattice.discriminant_group().is_isometric_to(discriminant_form)

    def test_g2_root_lattice_matches_its_theory(self):
        lattice = Lattice.G(2)
        discriminant_form = DiscriminantGroup.from_invariants_and_gram((3,), [[q(4, 3)]])
        assert lattice.gram_matrix() == matrix(ZZ, [[-2, 3], [3, -6]])
        assert lattice.det() == 3
        assert lattice.is_even()
        assert lattice.scale() == 1
        assert lattice.signature() == (0, 2)
        assert generator_norms(lattice) == (-2, -6)
        assert generator_divisibilities(lattice) == (1, 3)
        assert generator_isotropy(lattice) == (False, False)
        assert lattice.discriminant_group().is_isometric_to(discriminant_form)
