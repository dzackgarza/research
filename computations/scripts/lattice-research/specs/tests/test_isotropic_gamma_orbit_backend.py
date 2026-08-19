from __future__ import annotations

import math
from functools import cache
from itertools import combinations

import pytest
from src.lattices.lattices import Lattice


def _hyperbolic_plane():
    return Lattice.U()


def _two_hyperbolic_planes():
    return Lattice.U() + Lattice.U()


@cache
def _t_en():
    return Lattice.U() + Lattice.U().twist(2) + Lattice.E(8).twist(2)


@cache
def _degree_two_enriques_gamma():
    lattice = _t_en()
    h_over_2 = lattice.discriminant_group()(lattice([0, 0, 1, 1] + [0] * 8) / 2)
    disc_stabilizer = lattice.discriminant_group().orthogonal_group().stabilizer(h_over_2)
    return lattice.orthogonal_group().preimage_of_discriminant_subgroup(disc_stabilizer).plus_subgroup()


@cache
def _sterk_zero_cusp_representatives():
    lattice = _t_en()
    omega = [1, 0, 0, 0, 0, 0, 0, 0]
    alpha = [1, 1, 0, 0, 0, 0, 0, 0]
    return {
        "e": lattice([1, 0, 0, 0] + [0] * 8),
        "e_prime": lattice([0, 0, 1, 0] + [0] * 8),
        "e_prime_plus_f_prime_plus_omega": lattice([0, 0, 1, 1] + omega),
        "e_prime_plus_2f_prime_plus_alpha": lattice([0, 0, 1, 2] + alpha),
        "2e_plus_2f_plus_alpha": lattice([2, 2, 0, 0] + alpha),
    }


def _is_totally_isotropic(basis):
    return all(v.is_isotropic() for v in basis) and all(
        basis[i].inner_product(basis[j]).is_zero() for i in range(len(basis)) for j in range(i + 1, len(basis))
    )


class TestIsotropicLineSplitting:
    def test_ambient_orthogonal_group_of_u_has_one_isotropic_line_orbit(self):
        U = _hyperbolic_plane()
        assert len(U.orthogonal_group().isotropic_line_orbits()) == 1

    def test_special_orthogonal_group_of_u_splits_into_two_line_orbits(self):
        U = _hyperbolic_plane()
        SO = U.orthogonal_group().special_orthogonal_subgroup()
        orbits = SO.isotropic_line_orbits()
        assert len(orbits) == 2
        assert all(v.is_isotropic() for v in orbits)

    def test_ambient_group_identifies_the_two_standard_isotropic_lines(self):
        U = _hyperbolic_plane()
        e = U([1, 0])
        f = U([0, 1])
        assert U.orthogonal_group().isotropic_lines_are_equivalent(e, f)

    def test_special_orthogonal_group_separates_the_two_standard_isotropic_lines(self):
        U = _hyperbolic_plane()
        e = U([1, 0])
        f = U([0, 1])
        SO = U.orthogonal_group().special_orthogonal_subgroup()
        assert not SO.isotropic_lines_are_equivalent(e, f)


class TestIsotropicPlaneAndFlagSplitting:
    def test_ambient_orthogonal_group_of_u_plus_u_has_one_plane_orbit(self):
        lattice = _two_hyperbolic_planes()
        orbits = lattice.orthogonal_group().isotropic_plane_orbits()
        assert len(orbits) == 1
        assert _is_totally_isotropic(orbits[0])

    def test_special_orthogonal_group_of_u_plus_u_has_two_plane_orbits(self):
        lattice = _two_hyperbolic_planes()
        SO = lattice.orthogonal_group().special_orthogonal_subgroup()
        orbits = SO.isotropic_plane_orbits()
        assert len(orbits) == 2
        assert all(_is_totally_isotropic(orbit) for orbit in orbits)

    def test_ambient_orthogonal_group_of_u_plus_u_has_one_flag_orbit(self):
        lattice = _two_hyperbolic_planes()
        orbits = lattice.orthogonal_group().isotropic_flag_orbits(2)
        assert len(orbits) == 1
        assert _is_totally_isotropic(orbits[0])

    def test_special_orthogonal_group_of_u_plus_u_has_two_flag_orbits(self):
        lattice = _two_hyperbolic_planes()
        SO = lattice.orthogonal_group().special_orthogonal_subgroup()
        orbits = SO.isotropic_flag_orbits(2)
        assert len(orbits) == 2
        assert all(_is_totally_isotropic(orbit) for orbit in orbits)


class TestSterkDegreeTwoEnriquesLines:
    r"""Paper-backed line-orbit checks for Sterk Prop. 4.2.3 and AEGS Def. 2.6."""

    @pytest.fixture(scope="class")
    def lattice(self):
        return _t_en()

    @pytest.fixture(scope="class")
    def ambient_group(self, lattice):
        return lattice.orthogonal_group()

    @pytest.fixture(scope="class")
    def gamma(self):
        return _degree_two_enriques_gamma()

    @pytest.fixture(scope="class")
    def representatives(self):
        return _sterk_zero_cusp_representatives()

    @pytest.fixture(scope="class")
    def gamma_line_orbits(self, gamma):
        return gamma.isotropic_line_orbits()

    @pytest.fixture(scope="class")
    def gamma_plane_orbits(self, gamma):
        return gamma.isotropic_plane_orbits()

    @pytest.fixture(scope="class")
    def gamma_line_orbit_labels(self, gamma, representatives, gamma_line_orbits):
        labels = {}
        for name, representative in representatives.items():
            matching_indices = [
                index
                for index, orbit_representative in enumerate(gamma_line_orbits)
                if gamma.isotropic_lines_are_equivalent(
                    representative,
                    orbit_representative,
                )
            ]
            assert len(matching_indices) == 1, name
            labels[name] = matching_indices[0]
        return labels

    def test_paper_representatives_are_primitive_isotropic(self, representatives):
        for name, representative in representatives.items():
            assert representative.is_isotropic(), name
            assert math.gcd(*(int(entry) for entry in representative)) == 1, name

    def test_ambient_group_has_two_equivalence_classes_on_paper_representatives(
        self,
        ambient_group,
        representatives,
    ):
        assert not ambient_group.isotropic_lines_are_equivalent(
            representatives["e"],
            representatives["e_prime"],
        )
        for name in (
            "e_prime_plus_f_prime_plus_omega",
            "e_prime_plus_2f_prime_plus_alpha",
            "2e_plus_2f_plus_alpha",
        ):
            assert ambient_group.isotropic_lines_are_equivalent(
                representatives["e_prime"],
                representatives[name],
            ), name

    @pytest.mark.slow
    def test_degree_two_enriques_group_has_five_line_orbits(self, gamma_line_orbits):
        assert len(gamma_line_orbits) == 5

    @pytest.mark.slow
    def test_paper_representatives_are_pairwise_nonequivalent_mod_gamma(
        self,
        gamma_line_orbit_labels,
    ):
        for left_name, right_name in combinations(gamma_line_orbit_labels, 2):
            assert gamma_line_orbit_labels[left_name] != gamma_line_orbit_labels[right_name], f"{left_name} ~ {right_name}"

    @pytest.mark.slow
    def test_paper_representatives_match_the_five_gamma_orbits(
        self,
        representatives,
        gamma_line_orbits,
        gamma_line_orbit_labels,
    ):
        assert len(gamma_line_orbits) == len(representatives)
        assert set(gamma_line_orbit_labels.values()) == set(range(len(gamma_line_orbits)))

    @pytest.mark.slow
    def test_degree_two_enriques_group_has_nine_plane_orbits(self, gamma_plane_orbits):
        assert len(gamma_plane_orbits) == 9
