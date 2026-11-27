# Shared foundation contracts for the trusted lattice base.

from importlib.machinery import SourceFileLoader
from pathlib import Path

from sage.all import IntegralLattice

foundation = SourceFileLoader(
    "coble_geometry_foundation",
    str(Path("src") / "coble_geometry_foundation.py"),
).load_module()

positive_native = IntegralLattice("A1")
positive_scale = next(iter(positive_native.basis())).inner_product(
    next(iter(positive_native.basis()))
)
positive_line = foundation.Lattice.Z().twist(positive_scale)
negative_line = foundation.Lattice.A(1)
negative_eight = foundation.Lattice.E(8)
hyperbolic_plane = foundation.Lattice.U()
coble_picard = foundation.Lattice.coble_picard()
coble_transcendental = foundation.Lattice.coble_transcendental()
k3_lattice = foundation.Lattice.k3()

ambient_module = foundation.FreeBilinearModule.from_sage(
    hyperbolic_plane.ambient_module()
)
ambient_generator = next(iter(ambient_module.gens()))
assert ambient_generator.is_isotropic()

positive_generator = next(iter(positive_line.gens()))
assert positive_generator.divisibility().is_one()
assert positive_generator.is_primitive()
assert positive_line.is_isometric_to(positive_native)

discriminant_group = positive_line.discriminant_group()
positive_line_copy = foundation.Lattice.from_sage(positive_native)
assert positive_line_copy.is_even()
assert next(iter(positive_line_copy.gens())).divisibility().is_one()
assert positive_line_copy.is_isometric_to(positive_native)

discriminant_group_copy = foundation.DiscriminantGroup.from_lattice(positive_line)
assert not discriminant_group_copy.cardinality().is_one()
assert discriminant_group_copy.cardinality().is_prime_power()

discriminant_group_from_sage = foundation.DiscriminantGroup.from_sage(
    positive_native.discriminant_group()
)
assert not discriminant_group_from_sage.cardinality().is_one()
assert discriminant_group_from_sage.cardinality().is_prime_power()

discriminant_generator = next(iter(discriminant_group.gens()))
assert not discriminant_generator.is_isotropic()
discriminant_class = positive_generator.discriminant_class()
assert discriminant_class.parent() is discriminant_group
assert discriminant_class.is_isotropic()
assert discriminant_class.is_zero()

lattice_identity = hyperbolic_plane.hom(hyperbolic_plane, hyperbolic_plane.gens())
identity_image_lattice = lattice_identity.image_lattice()
assert identity_image_lattice.is_even()
assert identity_image_lattice.discriminant_group().cardinality().is_one()
assert identity_image_lattice.is_isometric_to(hyperbolic_plane)
assert lattice_identity.orthogonal_complement_of_image().rank().is_zero()

discriminant_identity = discriminant_group.hom(
    discriminant_group,
    discriminant_group.gens(),
)
identity_images = discriminant_identity.image_generators()
assert identity_images
assert next(iter(identity_images)).parent() is discriminant_group
assert discriminant_identity.is_identity()
assert not next(iter(identity_images)).is_isotropic()

assert negative_line.is_even()
assert negative_eight.is_even()
assert coble_picard.is_even()
assert coble_transcendental.is_even()
assert k3_lattice.is_even()
