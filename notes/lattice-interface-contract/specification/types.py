from __future__ import annotations

from abc import ABC
from fractions import Fraction

from pydantic import BaseModel, ConfigDict


def assert_equal(actual, expected, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: actual={actual}, expected={expected}")


class LatticeElement(BaseModel, ABC):
    """Base lattice-element contract."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def coords(self) -> tuple[int, ...]:
        assert False, "stub: LatticeElement.coords"

    def norm(self) -> int:
        assert False, "stub: LatticeElement.norm"

    def __mul__(self, other: LatticeElement) -> int:
        assert False, "stub: LatticeElement.__mul__"

    def __iter__(self):
        assert False, "stub: LatticeElement.__iter__"

    def perp(self) -> SubLattice:
        assert False, "stub: LatticeElement.perp"


class LatticeHyperplane(BaseModel, ABC):
    """Hyperplane contract in a lattice ambient space."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class SageMatrix(BaseModel, ABC):
    """Sage matrix contract type."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class LatticeMorphism(BaseModel, ABC):
    """Morphism contract between lattices.

    A lattice morphism is a homomorphism of underlying abelian groups
    represented by an integral/rational matrix in chosen bases.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def source(self) -> Lattice:
        assert False, "stub: LatticeMorphism.source"

    def target(self) -> Lattice:
        assert False, "stub: LatticeMorphism.target"

    def matrix(self) -> SageMatrix:
        assert False, "stub: LatticeMorphism.matrix"

    def __call__(self, x: LatticeElement) -> LatticeElement:
        assert False, "stub: LatticeMorphism.__call__"


class LatticeAutomorphism(LatticeMorphism, ABC):
    """Automorphism contract for a lattice (invertible lattice morphism `L -> L`)."""

    def lattice(self) -> Lattice:
        assert False, "stub: LatticeAutomorphism.lattice"

    def inverse(self) -> LatticeAutomorphism:
        assert False, "stub: LatticeAutomorphism.inverse"

    def determinant(self) -> int | Fraction:
        assert False, "stub: LatticeAutomorphism.determinant"


class RootLatticeElement(LatticeElement, ABC):
    """Root-lattice element contract."""

    def reflection(self) -> LatticeAutomorphism:
        assert False, "stub: RootLatticeElement.reflection"

    def orthogonal_hyperplane(self) -> LatticeHyperplane:
        assert False, "stub: RootLatticeElement.orthogonal_hyperplane"


class Lattice(BaseModel, ABC):
    """Base contract for integral lattices used in arithmetic/classification workflows.

    Mathematical scope:
    - Even/non-even integral lattices with symmetric bilinear form.
    - Discriminant-form and genus data used in Nikulin-style classification.
    - Primitive embeddings, complements, and overlattice gluing.

    Source hints:
    - Nikulin, "Integral symmetric bilinear forms..." (Izv. Akad. Nauk SSSR, 1979/1980).
    - Typical AG usage: K3 / IHS lattice embedding and glue arguments.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def from_gram(cls, gram: SageMatrix) -> Lattice:
        assert False, "stub: Lattice.from_gram"

    @classmethod
    def hyperbolic(cls, *, rank: int) -> HyperbolicLattice:
        assert False, "stub: Lattice.hyperbolic"

    @classmethod
    def U(cls) -> HyperbolicLattice:
        assert False, "stub: Lattice.U"

    @classmethod
    def H(cls) -> HyperbolicLattice:
        assert False, "stub: Lattice.H"

    @classmethod
    def I(cls, *, p: int, q: int) -> IndefiniteLattice:
        assert False, "stub: Lattice.I"

    @classmethod
    def II(cls, *, p: int, q: int) -> IndefiniteLattice:
        assert False, "stub: Lattice.II"

    @classmethod
    def A(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.A"

    @classmethod
    def B(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.B"

    @classmethod
    def C(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.C"

    @classmethod
    def D(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.D"

    @classmethod
    def E(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.E"

    @classmethod
    def F(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.F"

    @classmethod
    def G(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.G"

    @classmethod
    def A_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.A_affine"

    @classmethod
    def B_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.B_affine"

    @classmethod
    def C_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.C_affine"

    @classmethod
    def D_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.D_affine"

    @classmethod
    def E_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.E_affine"

    @classmethod
    def F_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.F_affine"

    @classmethod
    def G_affine(cls, rank: int) -> RootLattice:
        assert False, "stub: Lattice.G_affine"

    def rank(self) -> int:
        assert False, "stub: Lattice.rank"

    def gram(self) -> SageMatrix:
        assert False, "stub: Lattice.gram"

    def element(self, coords: tuple[int, ...] | list[int]) -> LatticeElement:
        assert False, "stub: Lattice.element"

    def norm(self, x: LatticeElement) -> int:
        assert False, "stub: Lattice.norm"

    def pairing(self, x: LatticeElement, y: LatticeElement) -> int:
        assert False, "stub: Lattice.pairing"

    def signature(self) -> tuple[int, int]:
        assert False, "stub: Lattice.signature"

    def determinant(self) -> int | Fraction:
        assert False, "stub: Lattice.determinant"

    def dual(self) -> RationalLattice | Lattice:
        assert False, "stub: Lattice.dual"

    def sublattice(self, generators: tuple[LatticeElement, ...] | list[LatticeElement]) -> SubLattice:
        assert False, "stub: Lattice.sublattice"

    def quotient(self, *, by: SubLattice) -> LatticeQuotient:
        assert False, "stub: Lattice.quotient"

    def discriminant(self) -> LatticeDiscriminantGroup:
        assert False, "stub: Lattice.discriminant"

    def orthogonal_group(self) -> OrthogonalGroup:
        assert False, "stub: Lattice.orthogonal_group"

    def stable_orthogonal_group(self) -> StableOrthogonalGroup:
        assert False, "stub: Lattice.stable_orthogonal_group"

    def discriminant_orthogonal_group(self) -> DiscriminantOrthogonalGroup:
        assert False, "stub: Lattice.discriminant_orthogonal_group"

    def orthogonal_set_stabilizer(
        self,
        vectors: tuple[LatticeElement, ...] | list[LatticeElement],
        *,
        subgroup: LatticeOrthogonalSubgroup | None = None,
    ) -> LatticeOrthogonalSubgroup:
        assert False, "stub: Lattice.orthogonal_set_stabilizer"

    def genus(self) -> LatticeGenus:
        assert False, "stub: Lattice.genus"

    def in_genus_of(self, other: Lattice) -> bool:
        assert False, "stub: Lattice.in_genus_of"

    def class_number(self) -> int:
        assert False, "stub: Lattice.class_number"

    def is_unique_in_genus(self) -> bool:
        assert False, "stub: Lattice.is_unique_in_genus"

    def is_isometric(
        self, other: Lattice, *, subgroup: LatticeOrthogonalSubgroup | None = None
    ) -> bool:
        """Return whether `self` and `other` are isometric (globally or inside `subgroup`)."""
        assert False, "stub: Lattice.is_isometric"

    def primitive_embedding_exists(self, target: Lattice) -> bool:
        """Decide existence of a primitive embedding `self -> target`."""
        assert False, "stub: Lattice.primitive_embedding_exists"

    def primitive_embeddings(self, target: Lattice) -> tuple[LatticePrimitiveEmbedding, ...]:
        """Enumerate primitive embeddings `self -> target` up to interface equivalence."""
        assert False, "stub: Lattice.primitive_embeddings"

    def orthogonal_complement_in(
        self, target: Lattice, *, embedding: LatticePrimitiveEmbedding | None = None
    ) -> Lattice:
        """Return the orthogonal complement of `self` in `target` for the chosen primitive embedding."""
        assert False, "stub: Lattice.orthogonal_complement_in"

    def primitive_complement_in(
        self, target: Lattice, *, embedding: LatticePrimitiveEmbedding | None = None
    ) -> Lattice:
        """Return the primitive orthogonal complement associated to a primitive embedding."""
        assert False, "stub: Lattice.primitive_complement_in"

    def overlattices(self) -> tuple[Lattice, ...]:
        """Enumerate overlattices of `self` in the current arithmetic scope."""
        assert False, "stub: Lattice.overlattices"

    def overlattice_from_glue(self, glue: LatticeGlueData) -> Lattice:
        """Construct an overlattice from isotropic gluing data on the discriminant form."""
        assert False, "stub: Lattice.overlattice_from_glue"

    def glue_data(self, overlattice: Lattice) -> LatticeGlueData:
        """Recover gluing data for `self ⊂ overlattice`."""
        assert False, "stub: Lattice.glue_data"

    def direct_sum(self, other: Lattice) -> Lattice:
        """Return the orthogonal direct sum lattice `self ⊕ other`."""
        assert False, "stub: Lattice.direct_sum"

    def is_glued_from(self, left: Lattice, right: Lattice, glue: LatticeGlueData) -> bool:
        """Check whether `self` is the overlattice obtained by gluing `left ⊕ right` via `glue`."""
        assert False, "stub: Lattice.is_glued_from"

    def automorphism_group_on_discriminant(
        self, *, subgroup: LatticeOrthogonalSubgroup | None = None
    ) -> DiscriminantOrthogonalGroup:
        """Return image of `subgroup` (default `O(L)`) in the discriminant-form orthogonal group `O(A_L)`."""
        assert False, "stub: Lattice.automorphism_group_on_discriminant"

    def automorphism_lifts_to_overlattice(
        self,
        automorphism: LatticeAutomorphism,
        complement: Lattice,
        glue: LatticeGlueData,
    ) -> bool:
        """Decide whether an automorphism of `self` lifts through a gluing to an isometry of the glued lattice."""
        assert False, "stub: Lattice.automorphism_lifts_to_overlattice"

    def extend_automorphism_to_overlattice(
        self,
        automorphism: LatticeAutomorphism,
        complement: Lattice,
        glue: LatticeGlueData,
    ) -> LatticeAutomorphism:
        """Construct a lifted automorphism on the glued lattice when liftability holds."""
        assert False, "stub: Lattice.extend_automorphism_to_overlattice"

    def liftable_automorphisms(
        self,
        complement: Lattice,
        glue: LatticeGlueData,
        *,
        subgroup: LatticeOrthogonalSubgroup | None = None,
    ) -> LatticeOrthogonalSubgroup:
        """Return subgroup of automorphisms of `self` liftable through the specified gluing."""
        assert False, "stub: Lattice.liftable_automorphisms"

    def glue_compatibility(
        self,
        automorphism_self: LatticeAutomorphism,
        automorphism_complement: LatticeAutomorphism,
        glue: LatticeGlueData,
    ) -> bool:
        """Check discriminant-form compatibility condition for a pair of summand automorphisms."""
        assert False, "stub: Lattice.glue_compatibility"

    def automorphism_lifting_result(
        self,
        automorphism: LatticeAutomorphism,
        complement: Lattice,
        glue: LatticeGlueData,
    ) -> tuple[bool, LatticeAutomorphism | None, str | None]:
        """Return `(lifts, witness, obstruction)` for the lifting problem."""
        assert False, "stub: Lattice.automorphism_lifting_result"


class DefiniteLattice(Lattice, ABC):
    """Definite-lattice contract."""

    def minimum(self) -> int | Fraction:
        assert False, "stub: DefiniteLattice.minimum"

    def shortest_vector(self) -> LatticeElement:
        assert False, "stub: DefiniteLattice.shortest_vector"


class IndefiniteLattice(Lattice, ABC):
    """Indefinite-lattice contract."""

    def is_indefinite(self) -> bool:
        assert False, "stub: IndefiniteLattice.is_indefinite"

    def witt_index(self) -> int:
        assert False, "stub: IndefiniteLattice.witt_index"

    def has_isotropic_vector(self) -> bool:
        assert False, "stub: IndefiniteLattice.has_isotropic_vector"

    def isotropic_vector(self) -> LatticeElement:
        assert False, "stub: IndefiniteLattice.isotropic_vector"

    def primitive_isotropic_vectors(self, *, bound: int) -> tuple[LatticeElement, ...]:
        assert False, "stub: IndefiniteLattice.primitive_isotropic_vectors"

    def isotropic_orbit_representatives(
        self, *, bound: int, primitive: bool = True
    ) -> tuple[LatticeElement, ...]:
        assert False, "stub: IndefiniteLattice.isotropic_orbit_representatives"

    def vinberg(self) -> CoxeterData:
        assert False, "stub: IndefiniteLattice.vinberg"

    def reflection(self, root: RootLatticeElement) -> LatticeAutomorphism:
        assert False, "stub: IndefiniteLattice.reflection"

    def orthogonal_hyperplane(self, root: RootLatticeElement) -> LatticeHyperplane:
        assert False, "stub: IndefiniteLattice.orthogonal_hyperplane"

    def eichler_criterion_equivalent(self, x: LatticeElement, y: LatticeElement) -> bool:
        assert False, "stub: IndefiniteLattice.eichler_criterion_equivalent"


class DegenerateLattice(Lattice, ABC):
    """Degenerate-lattice contract."""


class RationalLattice(Lattice, ABC):
    """Rational-lattice contract."""


class SubLattice(Lattice, ABC):
    """Sub-lattice contract."""

    def ambient(self) -> Lattice:
        assert False, "stub: SubLattice.ambient"

    def contains(self, x: LatticeElement) -> bool:
        assert False, "stub: SubLattice.contains"


class RootLattice(DefiniteLattice, ABC):
    """Root-lattice contract."""

    def root_system(self) -> LatticeRootSystem:
        assert False, "stub: RootLattice.root_system"


class HyperbolicLattice(IndefiniteLattice, ABC):
    """Hyperbolic-lattice contract."""


class LatticePolytope(BaseModel, ABC):
    """Polytope contract for fundamental chambers/domains."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class LatticeOrthogonalSubgroup(BaseModel, ABC):
    """Subgroup contract for O(L), O^+(L), and stabilizers."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __contains__(self, element: LatticeAutomorphism) -> bool:
        return self.contains(element)

    def contains(self, element: LatticeAutomorphism) -> bool:
        assert False, "stub: LatticeOrthogonalSubgroup.contains"


class LatticeCoxeterGroup(LatticeOrthogonalSubgroup, ABC):
    """Coxeter/orthogonal-group contract attached to lattice reflection data."""


class OrthogonalGroup(LatticeOrthogonalSubgroup, ABC):
    """Orthogonal-group contract O(L)."""

    def identity(self) -> LatticeAutomorphism:
        assert False, "stub: OrthogonalGroup.identity"

    def orbit(self, x: LatticeElement, *, bound: int) -> tuple[LatticeElement, ...]:
        assert False, "stub: OrthogonalGroup.orbit"

    def same_orbit(self, x: LatticeElement, y: LatticeElement) -> bool:
        assert False, "stub: OrthogonalGroup.same_orbit"

    def stabilizer(self, x: LatticeElement) -> LatticeOrthogonalSubgroup:
        assert False, "stub: OrthogonalGroup.stabilizer"

    def stabilizer_of_set(
        self, vectors: tuple[LatticeElement, ...] | list[LatticeElement]
    ) -> LatticeOrthogonalSubgroup:
        assert False, "stub: OrthogonalGroup.stabilizer_of_set"


class StableOrthogonalGroup(OrthogonalGroup, ABC):
    """Stable orthogonal-group contract O^+(L)."""


class LatticeRootSystem(BaseModel, ABC):
    """Root-system contract for Coxeter/Vinberg outputs."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def A(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.A"

    @classmethod
    def B(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.B"

    @classmethod
    def C(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.C"

    @classmethod
    def D(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.D"

    @classmethod
    def E(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.E"

    @classmethod
    def F(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.F"

    @classmethod
    def G(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.G"

    @classmethod
    def A_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.A_affine"

    @classmethod
    def B_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.B_affine"

    @classmethod
    def C_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.C_affine"

    @classmethod
    def D_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.D_affine"

    @classmethod
    def E_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.E_affine"

    @classmethod
    def F_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.F_affine"

    @classmethod
    def G_affine(cls, rank: int) -> LatticeRootSystem:
        assert False, "stub: LatticeRootSystem.G_affine"

    def is_isomorphic(self, other: LatticeRootSystem) -> bool:
        assert False, "stub: LatticeRootSystem.is_isomorphic"


class CoxeterData(BaseModel, ABC):
    """Vinberg-style aggregated data contract."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def root_lattice(self) -> RootLattice:
        assert False, "stub: CoxeterData.root_lattice"

    def fundamental_domain(self) -> LatticePolytope:
        assert False, "stub: CoxeterData.fundamental_domain"

    def coxeter_group(self) -> LatticeCoxeterGroup:
        assert False, "stub: CoxeterData.coxeter_group"

    def root_system(self) -> LatticeRootSystem:
        assert False, "stub: CoxeterData.root_system"

    def simple_roots(self) -> tuple[RootLatticeElement, ...]:
        assert False, "stub: CoxeterData.simple_roots"


class LatticeQuotient(BaseModel, ABC):
    """Quotient contract for L/M with M a sublattice."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def order(self) -> int:
        assert False, "stub: LatticeQuotient.order"

    def zero(self) -> LatticeQuotientElement:
        assert False, "stub: LatticeQuotient.zero"


class LatticeQuotientElement(BaseModel, ABC):
    """Element contract for quotient lattices/groups."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __add__(self, other: LatticeQuotientElement) -> LatticeQuotientElement:
        assert False, "stub: LatticeQuotientElement.__add__"

    def __neg__(self) -> LatticeQuotientElement:
        assert False, "stub: LatticeQuotientElement.__neg__"


class DiscriminantGroupElement(LatticeQuotientElement, ABC):
    """Element contract for lattice discriminant groups."""

    def order(self) -> int:
        assert False, "stub: DiscriminantGroupElement.order"


class LatticeDiscriminantGroup(LatticeQuotient, ABC):
    """Finite quadratic discriminant-form contract `(A_L, q_L)`.

    Mathematical role:
    - Stores arithmetic invariants used in genus/embedding classification.
    - Supports isotropic subgroup extraction for overlattice gluing.

    Source hints:
    - Nikulin 1979/1980, §1 (discriminant forms and gluing).
    - Standard overlattice correspondence via isotropic subgroups.
    """

    def generator(self, i: int) -> DiscriminantGroupElement:
        assert False, "stub: LatticeDiscriminantGroup.generator"

    def zero(self) -> DiscriminantGroupElement:
        assert False, "stub: LatticeDiscriminantGroup.zero"

    def bilinear(self, x: DiscriminantGroupElement, y: DiscriminantGroupElement) -> Fraction:
        assert False, "stub: LatticeDiscriminantGroup.bilinear"

    def quadratic(self, x: DiscriminantGroupElement) -> Fraction:
        assert False, "stub: LatticeDiscriminantGroup.quadratic"

    def orthogonal_group(self) -> DiscriminantOrthogonalGroup:
        assert False, "stub: LatticeDiscriminantGroup.orthogonal_group"

    def is_isomorphic(self, other: LatticeDiscriminantGroup) -> bool:
        assert False, "stub: LatticeDiscriminantGroup.is_isomorphic"

    def minimal_number_of_generators(self, *, prime: int | None = None) -> int:
        assert False, "stub: LatticeDiscriminantGroup.minimal_number_of_generators"

    def signature_mod_8(self) -> int:
        assert False, "stub: LatticeDiscriminantGroup.signature_mod_8"

    def exists_even_lattice(self, *, t_plus: int, t_minus: int) -> bool:
        assert False, "stub: LatticeDiscriminantGroup.exists_even_lattice"

    def isotropic_subgroups(self) -> tuple[LatticeGlueData, ...]:
        assert False, "stub: LatticeDiscriminantGroup.isotropic_subgroups"


class DiscriminantOrthogonalGroup(BaseModel, ABC):
    """Orthogonal group `O(A_L)` of a finite quadratic discriminant form."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def identity(self):
        """Return identity automorphism of the finite quadratic form."""
        assert False, "stub: DiscriminantOrthogonalGroup.identity"

    def contains(self, automorphism) -> bool:
        assert False, "stub: DiscriminantOrthogonalGroup.contains"


class LatticeGenus(BaseModel, ABC):
    """Genus-level classification contract (signature + discriminant-form data)."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def signature(self) -> tuple[int, int]:
        assert False, "stub: LatticeGenus.signature"

    def discriminant_form(self) -> LatticeDiscriminantGroup:
        assert False, "stub: LatticeGenus.discriminant_form"

    def contains(self, lattice: Lattice) -> bool:
        assert False, "stub: LatticeGenus.contains"

    def class_number(self) -> int:
        assert False, "stub: LatticeGenus.class_number"

    def is_single_class(self) -> bool:
        assert False, "stub: LatticeGenus.is_single_class"


class LatticeGlueData(BaseModel, ABC):
    """Gluing datum for constructing overlattices from isotropic subgroups.

    Mathematical meaning:
    - Encodes isotropic subgroup data in discriminant forms.
    - Determines overlattice and complement-glue compatibility constraints.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def base_discriminant_form(self) -> LatticeDiscriminantGroup:
        assert False, "stub: LatticeGlueData.base_discriminant_form"

    def subgroup_generators(self) -> tuple[DiscriminantGroupElement, ...]:
        assert False, "stub: LatticeGlueData.subgroup_generators"

    def is_isotropic(self) -> bool:
        assert False, "stub: LatticeGlueData.is_isotropic"


class LatticePrimitiveEmbedding(BaseModel, ABC):
    """Primitive embedding data contract for Nikulin-style lattice embeddings."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def source(self) -> Lattice:
        assert False, "stub: LatticePrimitiveEmbedding.source"

    def target(self) -> Lattice:
        assert False, "stub: LatticePrimitiveEmbedding.target"

    def image_generators(self) -> tuple[LatticeElement, ...]:
        assert False, "stub: LatticePrimitiveEmbedding.image_generators"

    def glue_isometry(self) -> DiscriminantFormIsometry:
        """Return discriminant-form isometry/anti-isometry induced by the embedding gluing."""
        assert False, "stub: LatticePrimitiveEmbedding.glue_isometry"


class DiscriminantFormIsometry(BaseModel, ABC):
    """Isometry data between finite quadratic discriminant forms.

    In embedding/gluing contexts this often appears as an anti-isometry
    between discriminant forms of primitive summands.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def source(self) -> LatticeDiscriminantGroup:
        assert False, "stub: DiscriminantFormIsometry.source"

    def target(self) -> LatticeDiscriminantGroup:
        assert False, "stub: DiscriminantFormIsometry.target"

    def is_anti_isometry(self) -> bool:
        assert False, "stub: DiscriminantFormIsometry.is_anti_isometry"

    def is_compatible_with_glue(self, glue: LatticeGlueData) -> bool:
        assert False, "stub: DiscriminantFormIsometry.is_compatible_with_glue"
