r"""Free groups, cyclic subgroups and the orders of catalogued groups.

The free group on $\{a, b\}$ is nonabelian, finitely presented with no
relations, and $a b b^{-1} = a$; the word $a b a^{-1}$ is reduced.  A group
morphism out of it is determined by the images of $a$ and $b$ (the
universal property of the free group).  In $C_4 = \langle g \rangle$ the
cyclic subgroups $\langle g \rangle$ and $\langle g^2 \rangle$ have orders
$4$ and $2$.  The hyperoctahedral group $W(B_2)$ of signed permutations of
two letters has order $2^2 \cdot 2! = 8$.  $|\mathrm{SL}_2(\mathbb{F}_q)| =
q(q^2 - 1)$ and $\mathrm{PSL}_2(\mathbb{F}_7) = \mathrm{SL}_2(\mathbb{F}_7) /
\{\pm 1\}$ has order $7 \cdot 48 / 2 = 168$.  The Heisenberg group of upper
unitriangular $3 \times 3$ matrices over $\mathbb{Z}/3$ has $3^3 = 27$
elements.  $\mathrm{SL}_2(\mathbb{Z})$ is infinite and arithmetic, and the
braid group on three strands is infinite (it surjects onto $\mathbb{Z}$ by
the exponent sum).  All are computations from the definitions.
"""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_the_free_group_on_two_letters_is_nonabelian_and_freely_reduces_words() -> None:
    free = Groups.Free(2)
    a, b = free.group_generators()

    assert free.number_of_group_generators() == cardinal(2)
    assert a * b * ~b == a
    assert a * b != b * a
    assert not free.is_abelian()
    assert free.is_finitely_generated()
    assert free.is_finitely_presented()
    assert free.free_generator(0) == a
    assert free.reduced_word(a * b * a**-1).cardinality() == cardinal(3)


def test_a_morphism_out_of_the_free_group_is_given_by_the_images_of_its_letters() -> None:
    r"""$a \mapsto (1\,2)$, $b \mapsto (1\,2\,3)$ is onto $S_3$ and sends $a b$ to $(1\,2)(1\,2\,3)$."""
    free = Groups.Free(2)
    a, b = free.group_generators()
    symmetric = Groups.S(3)
    morphism = free.Mor(symmetric)({a: symmetric((1, 2)), b: symmetric((1, 2, 3))})

    assert morphism.image().order() == 6
    assert morphism(a * b) == symmetric((1, 2)) * symmetric((1, 2, 3))


def test_the_cyclic_subgroups_of_c4_have_orders_four_and_two() -> None:
    group = Groups.C(4)
    generator = group.group_generators()[0]

    assert generator.cyclic_subgroup().order() == 4
    assert (generator**2).cyclic_subgroup().order() == 2


def test_orders_of_catalogued_finite_groups_from_their_definitions() -> None:
    assert Groups.Weyl(["B", 2]).order() == 8
    assert Groups.PSL(2, 7).order() == 168


def test_the_heisenberg_group_over_z_mod_three_has_twenty_seven_elements() -> None:
    assert Groups.Heisenberg(1, 3).order() == 27


def test_sl2z_and_the_three_strand_braid_group_are_infinite() -> None:
    modular = Groups.SL(2, ZZ)

    assert not modular.is_finite()
    assert modular.is_arithmetic_group()
    assert not Groups.Braid(3).is_finite()
