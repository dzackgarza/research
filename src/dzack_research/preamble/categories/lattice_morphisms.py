r"""Form-preserving morphisms, embeddings, and isometries of lattices."""

from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.categories.category import Category
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleEmbedding,
    ModuleMorphism,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    category_packet,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring
from dzack_research.preamble.categories.group.cyclic_subgroups import cyclic_subgroup
from dzack_research.preamble.categories.group.groups import (
    OwnedFiniteGroups,
    OwnedGroups,
)
from dzack_research.preamble.categories.group.predicate_subgroups import predicate_subgroup
from dzack_research.preamble.categories.isotropic_orbits import (
    isotropic_equivalence_witness,
    isotropic_orbit_representatives,
    isotropic_stabilizer_generators,
)
from dzack_research.preamble.categories import lattice_engines
from dzack_research.preamble.categories.modules.framed.formed.form_modules import form_embedding
from dzack_research.preamble.categories.modules.framed.formed.torsion_form_modules import torsion_form_isometry
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_embedding,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import _engine_matrix
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.engine_capabilities import engine_capabilities
from dzack_research.preamble.refine import realize_owned_category
from dzack_research.preamble.tensors.tensor import (
    _engine_component_matrix,
    tensor,
)


def _engine_gram_rows(lattice):
    r"""Return the Gram entries as plain integer rows, the shape the programs read."""
    rank = int(lattice.rank())
    gram = lattice.gram_tensor()
    return [[int(gram[i, j]) for j in range(rank)] for i in range(rank)]


def _tensor_view(morphism):

    return tensor.from_morphism(morphism)


def _normalize_lattice_generator_images(domain, images):
    r"""Interpret integer dictionary keys as framing positions when necessary.

    Lattice framings may use formal symbols even though ``module_generator(i)``
    deliberately accepts the integer position ``i``.  Keep the same positional
    spelling for explicit image dictionaries before the generic module-morphism
    layer sees the actual symbolic labels.
    """
    if not isinstance(images, dict):
        return images
    labels = domain.module_generating_set()
    normalized = {}
    for key, value in images.items():
        if key in labels:
            label = labels(key)
        else:
            try:
                label = labels.unrank(int(key))
            except (AttributeError, TypeError, ValueError, IndexError):
                label = key
        normalized[label] = value
    return normalized


class LatticeMorphism(ModuleMorphism):
    r"""A module morphism preserving the lattice form."""

    def __init__(self, parent, images, *, elementwise=False) -> None:
        ModuleMorphism.__init__(self, parent, images, elementwise=elementwise)
        domain = self.domain()
        codomain = self.codomain()
        if domain.is_finite_rank() and codomain.is_finite_rank():
            pulled_back = codomain.gram_tensor().pullback(self)
            if not pulled_back.is_equal_tensor(domain.gram_tensor()):
                raise ValueError("the stated module morphism does not preserve the lattice form")

    def __mul__(self, other):
        if not isinstance(other, LatticeMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        return lattice_homset(source, self.codomain())(
            lambda label: self(other(source.module_generator(label)))
        )



class LatticeEmbedding(LatticeMorphism):
    r"""A form-preserving monomorphism of lattices."""

    def __init__(self, parent, images, *, verify_injective=True) -> None:
        LatticeMorphism.__init__(self, parent, images)
        if (
            verify_injective
            and self.domain().is_finite_rank()
            and self.codomain().is_finite_rank()
            and not ModuleMorphism.is_injective(self)
        ):
            raise ValueError("a lattice embedding must be injective")

    def is_injective(self) -> bool:
        return True

    def factor_through(self, target_embedding):
        r"""Factor this lattice embedding through a module embedding when possible."""
        if target_embedding.codomain() is not self.codomain():
            raise ValueError("subobject factorization requires one common codomain")
        images = {}
        for label in self.domain().module_generating_set():
            image = self(self.domain().module_generator(label))
            try:
                images[label] = target_embedding.lift(image)
            except (TypeError, ValueError) as error:
                raise ValueError("the first subobject is not contained in the second") from error
        return module_homset(self.domain(), target_embedding.domain())(images)

    def __mul__(self, other):
        if not isinstance(other, LatticeEmbedding):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        return lattice_embedding_homset(source, self.codomain())(
            lambda label: self(other(source.module_generator(label)))
        )

    def isotropic_reduction(self):
        r"""Return \(K_I=I^\perp/I\) for this totally isotropic embedding \(\iota:I\hookrightarrow L\).

        \(I\) pairs to zero against \(I^\perp\), so the form of \(L\) descends
        to the quotient.  When \(L\) is nondegenerate of signature \((p,q)\)
        and \(\operatorname{rk}I=k\), the quotient is nondegenerate of
        signature \((p-k,q-k)\).

        The result is a lattice in ``IsotropicReductions``, which keeps the
        embedding, the complement \(I^\perp\), the inclusion
        \(I\hookrightarrow I^\perp\) and the chosen lifts of the quotient
        framing.  The parabolic subgroup of \(O(L)\) stabilizing \(I\), its
        Levi action on \(K_I\) and its unipotent radical are all read off that
        retained data.
        """
        from dzack_research.preamble.categories._lattice import Lattice
        from dzack_research.preamble.categories.lattices import IsotropicReductions

        source = self.domain()
        target = self.codomain()
        ring = target.base_ring()
        assert source.is_totally_isotropic(), (
            "an isotropic reduction is taken along a totally isotropic sublattice"
        )

        perpendicular = self.orthogonal_complement()
        perpendicular_inclusion = perpendicular.inclusion()
        into_perpendicular = module_embedding(
            source,
            perpendicular,
            lambda label: perpendicular_inclusion.lift(
                self(source.module_generator(label))
            ),
        )
        assert into_perpendicular.is_primitive(), (
            "the isotropic quotient is not free over the base ring; the selected "
            "isotropic sublattice is not primitive in its orthogonal complement"
        )
        quotient = into_perpendicular.cokernel()
        normalization = quotient.invariant_factor_form()
        quotient_module_generators = quotient.smith_form_module_generators()
        rank = int(quotient_module_generators.cardinality())
        labels = Sets.Δ[rank - 1]
        lifts = finite_indexed_family(
            labels,
            lambda position: perpendicular.linear_combination(
                module_coefficients(
                    quotient_module_generators.unrank(int(position))
                )
            ),
            name="Isotropic-reduction lifts",
        )

        lattice_category = target.lattice_category()
        if rank == 0:
            prototype = lattice_category(0)
        else:
            gram = tensor(
                ring,
                (),
                (rank, rank),
                (
                    perpendicular.b(lifts.unrank(i), lifts.unrank(j))
                    for i in range(rank)
                    for j in range(rank)
                ),
            )
            prototype = lattice_category(gram, module_generators=labels)

        reduction = Lattice(
            prototype._module,
            prototype.gram_tensor(),
            lattice_category,
            prototype._sage_lattice,
            extra_categories=(IsotropicReductions(ring),),
            construction_data=(
                ("isotropic_embedding", self),
                ("orthogonal_complement", perpendicular),
                ("isotropic_inclusion", into_perpendicular),
                ("reduction_lifts", lifts),
                ("reduction_normalization", normalization),
            ),
        )
        return lattice_category._refine_lattice_object(reduction)

    def discriminant_inclusion(self):
        r"""Return ``A_S -> A_L`` for an orthogonal direct-summand embedding.

        For ``i:S -> L`` the extension-by-zero map on duals is the intrinsic
        contraction

        ``S^vee --g_S^vee--> S --i--> L --g_L--> L^vee``.

        It descends to an injective map of discriminant forms exactly when the
        displayed rational covectors are integral on ``L``; for an isometric
        embedding this is precisely the represented orthogonal direct-summand
        situation.  No matrix transpose convention enters the construction.

        If ``L`` is even the map preserves the quadratic discriminant forms.
        If ``L`` is odd, only the bilinear discriminant forms are functorial,
        so an even source has its quadratic refinement forgotten first.
        """
        source = self.domain()
        target = self.codomain()
        if (
            _engine_ring(source.base_ring()) is not SageZZ
            or _engine_ring(target.base_ring()) is not SageZZ
        ):
            raise NotImplementedError(
                "discriminant inclusions are currently implemented for integral ZZ-lattices"
            )
        if not (
            source.is_finite_rank()
            and target.is_finite_rank()
            and source.is_nondegenerate()
            and target.is_nondegenerate()
        ):
            raise ValueError(
                "a discriminant inclusion requires finite nondegenerate lattices"
            )


        target_discriminant = target.discriminant_module()
        target_dual = target_discriminant.projection().domain()
        target_dual_labels = tuple(target_dual.module_generating_set())

        if target.is_even():
            source_form = source.discriminant_quadratic_form()
            target_form = target.discriminant_quadratic_form()
        else:
            source_form = source.discriminant_bilinear_form()
            target_form = target.discriminant_bilinear_form()

        source_rank = int(source.rank())
        rationals = source.base_ring().fraction_field()
        source_dual_form = source.gram_tensor().change_ring(rationals).dual_tensor()
        inclusion_tensor = _tensor_view(self).change_ring(rationals)
        target_form_tensor = target.gram_tensor().change_ring(rationals)
        target_ring = target.base_ring()

        images = {}
        for source_position, label in enumerate(source_form.module_generating_set()):
            basis_covector = tensor(
                rationals,
                (),
                (source_rank,),
                [
                    rationals.one()
                    if index == source_position
                    else rationals.zero()
                    for index in range(source_rank)
                ],
            )
            source_vector = source_dual_form * basis_covector
            target_vector = inclusion_tensor * source_vector
            extended_covector = target_form_tensor * target_vector
            if any(
                coefficient not in target_ring for coefficient in extended_covector
            ):
                raise ValueError(
                    "the lattice embedding is not an orthogonal direct summand: "
                    "extension by zero does not send the selected dual lattice into "
                    "the dual lattice of the codomain"
                )
            integral_coefficients = tuple(
                target_ring(coefficient) for coefficient in extended_covector
            )
            dual_element = target_dual.linear_combination(
                {
                    target_label: coefficient
                    for target_label, coefficient in zip(
                        target_dual_labels,
                        integral_coefficients,
                        strict=True,
                    )
                    if coefficient
                }
            )
            images[label] = target_discriminant.projection()(dual_element)

        return form_embedding(
            source_form,
            target_form,
            images,
            quadratic=target.is_even(),
        )


class LatticeIsometry(LatticeEmbedding):
    r"""An invertible lattice morphism."""

    def __init__(self, parent, images) -> None:
        LatticeEmbedding.__init__(self, parent, images)
        if self.domain().is_finite_rank() and self.codomain().is_finite_rank() and not ModuleMorphism.is_surjective(self):
            raise ValueError("a lattice isometry must be surjective")

    def is_surjective(self) -> bool:
        return True

    def inverse(self):
        r"""Return the inverse isometry."""
        codomain = self.codomain()
        return codomain.Isom(self.domain())(lambda label: self.lift(codomain.module_generator(label)))

    def __invert__(self):
        return self.inverse()

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        return (
            isinstance(other, LatticeIsometry)
            and other.domain() is self.domain()
            and other.codomain() is self.codomain()
            and _tensor_view(other) == _tensor_view(self)
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        tensor_ = _tensor_view(self)
        return hash(
            (
                id(self.domain()),
                id(self.codomain()),
                tuple(tensor_.list()),
            )
        )

    def determinant(self):
        r"""Return the determinant of this automorphism/isometry tensor."""
        if self.domain().rank() != self.codomain().rank():
            raise ValueError("determinant is defined here for equal-rank isometries")
        return self.matrix().determinant()

    def __mul__(self, other):
        if isinstance(other, LatticeIsometry) and other.codomain() is self.domain():
            if self.domain() is self.codomain() and other.parent() is self.parent():
                return self.parent().compose(self, other)
            source = other.domain()
            return lattice_isometry_homset(source, self.codomain())(
                lambda label: self(other(source.module_generator(label)))
            )
        return super().__mul__(other)

    @cached_method
    def invariant_lattice(self):
        r"""Return ``ker(self-id)`` as a formed subobject of the lattice."""
        if self.domain() is not self.codomain():
            raise ValueError("invariants are defined here for a lattice automorphism")
        lattice = self.domain()

        difference = module_homset(lattice, lattice)(tuple(self(generator) - generator for generator in lattice.module_generators()))
        return difference.kernel()

    @cached_method
    def formed_coinvariants(self):
        r"""Return ``(L^self)^perp`` as a formed subobject of ``L``.

        This is deliberately not called ``coinvariants``: module coinvariants
        are the quotient ``L/(self-1)L`` and are generally a different object.
        """
        return self.invariant_lattice().orthogonal_complement()

    @cached_method
    def _discriminant_forward_morphism(self):
        r"""Return the induced module map on discriminant groups."""
        source = self.domain().discriminant_group()
        target = self.codomain().discriminant_group()
        target_dual = target.projection().domain()
        target_dual_generators = target_dual.module_generators()
        dual_map = self.matrix().inverse().transpose()
        images = {}
        for source_position, label in enumerate(source.module_generating_set()):
            dual_image = sum(
                (
                    target_dual.scalar_multiple(
                        dual_map[target_position, source_position],
                        target_dual_generators.unrank(target_position),
                    )
                    for target_position in range(dual_map.parent().nrows())
                    if dual_map[target_position, source_position]
                ),
                target_dual.zero(),
            )
            images[label] = target.projection()(dual_image)

        return module_homset(source, target)(images)

    @cached_method
    def discriminant_isometry(self):
        r"""Return the induced isometry ``Disc(self): A_L -> A_M``.

        For ``f:L->M`` the map on duals is ``(f^{-1})^vee:L^vee->M^vee``.
        Passing to the cokernels of the correlation maps gives the finite-form
        isometry on discriminant modules.
        """

        forward = self._discriminant_forward_morphism()
        inverse = (~self)._discriminant_forward_morphism()
        return torsion_form_isometry(
            forward,
            inverse,
            quadratic=self.domain().is_even(),
        )

    @cached_method
    def discriminant_morphism(self):
        r"""Return ``Disc(self)`` parented by ``O(A_L)`` for an automorphism."""
        if self.domain() is not self.codomain():
            raise ValueError("a discriminant automorphism requires a lattice automorphism")
        form = self.domain().discriminant_group()
        return form.orthogonal_group().from_morphism(
            self._discriminant_forward_morphism()
        )

    def cyclic_subgroup(self):
        r"""Return the literal subgroup ``<self> <= O(L)``."""
        if self.domain() is not self.codomain():
            raise ValueError("a cyclic isometry subgroup requires a lattice automorphism")

        return cyclic_subgroup(self)

    @cached_method
    def real_spinor_norm_sign(self):
        r"""Return the sign of the real spinor norm in Dawes' convention.

        OSCAR computes the rational spinor norm with a reflection ``s_w``
        represented by the square class of ``(w,w)``.  The convention used by
        the arithmetic ``O^+(L)`` character is the square class of
        ``-(w,w)/2``.  Their signs differ by the determinant character, so the
        exact OSCAR sign is multiplied by ``det(self)`` here.
        """
        if self.domain() is not self.codomain():
            raise ValueError("the spinor norm is a character of a lattice automorphism group")
        lattice = self.domain()
        if _engine_ring(lattice.base_ring()) is not SageZZ:
            raise NotImplementedError("the current exact spinor-norm seam is for integral ZZ-lattices")
        if not lattice.is_finite_rank() or not lattice.is_nondegenerate():
            raise ValueError("the real spinor norm requires a finite nondegenerate lattice")

        ring = lattice.base_ring()
        if lattice.is_positive_definite():
            return self.determinant()
        if lattice.is_negative_definite():
            return ring.one()
        backend_sign = SageZZ(
            lattice_engines.rational_spinor_norm_sign(
                lattice.gram_tensor(), _tensor_view(self)
            )
        )
        return ring._from_engine_element(backend_sign) * self.determinant()

    def preserves_positive_cone(self) -> bool:
        r"""Return whether an isometry preserves a component of the positive cone.

        This character is defined here only for signature ``(1,n)``, where
        ``{v : b(v,v)>0}`` has exactly two components.  For one exact rational
        positive vector ``v``, the isometry preserves its component exactly
        when ``b(v,g(v))>0``.
        """
        if self.domain() is not self.codomain():
            raise ValueError("positive-cone preservation is a property of a lattice automorphism")
        lattice = self.domain()
        _signature = lattice.signature_pair()
        positive, negative = _signature.first(), _signature.second()
        integers = positive.parent()
        if positive != integers.one() or negative < integers.one():
            raise ValueError(
                f"the positive cone has two components only in signature (1,n); got {(positive, negative)}"
            )

        rationals = lattice.base_ring().fraction_field()
        gram = lattice.gram_tensor().change_ring(rationals)
        vector = lattice_engines.rational_positive_vector(gram)
        image = _tensor_view(self).change_ring(rationals) * vector
        pairing = gram.contract(vector, image)
        if pairing == rationals.zero():
            raise ArithmeticError(
                "a positive vector cannot be orthogonal to its image under a hyperbolic isometry"
            )
        return bool(pairing > rationals.zero())

    @cached_method
    def centralizer_discriminant_image(self):
        r"""Return ``rho_L(Z_{O(L)}(self)) <= O(A_L)`` when OSCAR computes it.

        Hermitian Miranda--Morrison theory supplies this finite image directly
        for even integral lattices; it does not require generators of the
        (generally infinite) arithmetic centralizer itself.  OSCAR's output is
        interpreted only in the private Smith-coordinate engine of ``O(A_L)``
        and transported back to live discriminant-form automorphisms.
        """
        if self.domain() is not self.codomain():
            raise ValueError("a centralizer is defined here for a lattice automorphism")
        lattice = self.domain()
        if _engine_ring(lattice.base_ring()) is not SageZZ:
            raise NotImplementedError(
                "the centralizer discriminant image is currently implemented for integral ZZ-lattices"
            )
        if not lattice.is_even():
            raise ValueError(
                "the hermitian Miranda--Morrison centralizer-image backend requires an even lattice"
            )
        if not lattice.is_finite_rank() or not lattice.is_nondegenerate():
            raise ValueError(
                "the centralizer discriminant image requires a finite nondegenerate lattice"
            )


        engine_generators, expected_order, invariant_rank, coinvariant_rank = (
            lattice_engines.centralizer_discriminant_image(
                lattice.gram_tensor(),
                _tensor_view(self),
            )
        )
        if self.invariant_lattice().rank() != invariant_rank:
            raise ArithmeticError(
                "OSCAR's invariant-lattice rank disagrees with the owned invariant lattice"
            )
        if self.formed_coinvariants().rank() != coinvariant_rank:
            raise ArithmeticError(
                "OSCAR's coinvariant-lattice rank disagrees with the owned formed coinvariants"
            )

        orthogonal_group = lattice.discriminant_group().orthogonal_group()
        generators = tuple(
            orthogonal_group._from_engine_matrix(
                # Both OSCAR's finite discriminant group and Sage's FQF
                # engine act on their Smith generators on the right.
                _engine_component_matrix(engine_generator)
            )
            for engine_generator in engine_generators
        )
        induced = self.discriminant_morphism()
        if any(
            generator * induced != induced * generator
            for generator in generators
        ):
            raise ArithmeticError(
                "a centralizer-image generator does not commute with the induced discriminant automorphism"
            )
        image = orthogonal_group.subgroup_on(generators)
        if image.order() != expected_order:
            raise ArithmeticError(
                "the crossed-back centralizer image has the wrong order"
            )
        return image


class LatticeHomset(CategoricalHomset):
    Element = LatticeMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        ring = domain.base_ring()
        lattices = domain.lattice_category()
        if domain not in lattices or codomain not in lattices:
            raise TypeError("a lattice homset has lattices as its domain and codomain")
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        if isinstance(images, ModuleMorphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the module morphism has the wrong lattice endpoints")
            if images.parent() is self:
                return images
            return self.elementwise(lambda element: images(element))
        return self.element_class(
            self,
            _normalize_lattice_generator_images(self.domain(), images),
        )

    def elementwise(self, function, *, verify_linearity=True):
        if not callable(function):
            raise TypeError("an elementwise lattice map must be callable")
        source = self.domain()
        return self.element_class(
            self,
            lambda label: function(source.module_generator(label)),
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a lattice endomorphism homset")
        return self.elementwise(lambda element: element)

    def _repr_(self):
        return f"LatticeHom({self.domain()}, {self.codomain()})"


class LatticeEmbeddingHomset(CategoricalHomset):
    Element = LatticeEmbedding

    def __init__(self, hom_family, domain, codomain, *, category=None) -> None:
        lattices = domain.lattice_category()
        if domain not in lattices or codomain not in lattices:
            raise TypeError("a lattice embedding homset has lattice endpoints")
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
            category=category,
        )
        if category is not None:
            realize_owned_category(self)

    def _element_constructor_(self, images):
        if isinstance(images, ModuleEmbedding):
            if (
                images.domain() is not self.domain()
                or images.codomain() is not self.codomain()
            ):
                raise ValueError("the module embedding has the wrong lattice endpoints")
            source = self.domain()
            return self.element_class(
                self,
                lambda label: images(source.module_generator(label)),
                verify_injective=False,
            )
        if isinstance(images, ModuleMorphism):
            if (
                images.domain() is not self.domain()
                or images.codomain() is not self.codomain()
            ):
                raise ValueError("the module morphism has the wrong lattice endpoints")
            if images.parent() is self:
                return images
            source = self.domain()
            return self.element_class(
                self,
                lambda label: images(source.module_generator(label)),
            )
        return self.element_class(
            self,
            _normalize_lattice_generator_images(self.domain(), images),
        )

    def elementwise(self, function, *, verify_linearity=True):
        if not callable(function):
            raise TypeError("an elementwise lattice embedding must be callable")
        source = self.domain()
        return self.element_class(
            self,
            lambda label: function(source.module_generator(label)),
        )

    def super_categories(self):
        packet = category_packet(self.base_category())
        source = self.domain()
        target = self.codomain()
        inherited = [
            superpacket.Monos().Of(source, target)
            for superpacket in packet.super_packets()
            if source in superpacket.C() and target in superpacket.C()
        ]
        return [packet.Homs().Of(source, target), *inherited]

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"

    def _codomain_is_even_unimodular_indefinite(self) -> bool:
        target = self.codomain()
        if not target.is_finite_rank() or not target.is_nondegenerate():
            return False
        _signature = target.signature_pair()
        positive, negative = _signature.first(), _signature.second()
        return (
            positive > 0
            and negative > 0
            and target.is_even()
            and target.is_unimodular()
        )

    def even_overlattice_inclusions(self):
        r"""Return the finite even-overlattice sweep used by Nikulin existence."""
        return self.domain().even_overlattice_inclusions()

    def __iter__(self):
        r"""Enumerate all embeddings when the target lattice is definite.

        Each source generator must land in the finite shell of target vectors
        having the same square.  A depth-first placement is pruned by the
        pairings with generators already placed; at a complete placement the
        live embedding constructor verifies injectivity and form preservation.
        """
        source = self.domain()
        target = self.codomain()
        if not target.is_finite_rank() or not target.is_definite():
            raise NotImplementedError(
                "embedding enumeration is currently implemented for finite definite targets"
            )
        if not source.is_finite_rank():
            raise NotImplementedError(
                "embedding enumeration requires a finite-rank source"
            )
        source_generators = tuple(source.module_generators())
        source_gram = source.gram_tensor()
        pools = tuple(
            tuple(target.vectors_of_square(source_gram[index, index]))
            for index in range(len(source_generators))
        )

        def assign(placed):
            position = len(placed)
            if position == len(source_generators):
                try:
                    yield self(tuple(placed))
                except ValueError:
                    return
                return
            for candidate in pools[position]:
                if all(
                    target.b(placed[index], candidate)
                    == source_gram[index, position]
                    for index in range(position)
                ):
                    yield from assign((*placed, candidate))

        yield from assign(())

    def is_empty(self):
        if self.codomain().is_finite_rank() and self.codomain().is_definite():
            for _embedding in self:
                return False
            return True
        if self._codomain_is_even_unimodular_indefinite():
            source = self.domain()
            if not source.is_even():
                return True
            _signature = self.codomain().signature_pair()
            positive, negative = _signature.first(), _signature.second()
            return not any(
                inclusion.codomain().embeds_in_even_unimodular(
                    positive, negative
                )
                for inclusion in self.even_overlattice_inclusions()
            )
        return Unknown

    def an_element(self):
        if self.codomain().is_finite_rank() and self.codomain().is_definite():
            for embedding in self:
                return embedding
            raise ValueError("the embedding homset is empty")
        if self._codomain_is_even_unimodular_indefinite():
            if self.is_empty():
                raise ValueError("the embedding homset is empty")
            _signature = self.codomain().signature_pair()
            positive, negative = _signature.first(), _signature.second()
            for inclusion in self.even_overlattice_inclusions():
                overlattice = inclusion.codomain()
                if not overlattice.embeds_in_even_unimodular(positive, negative):
                    continue
                primitive = overlattice.embed_in_even_unimodular(
                    positive, negative
                )
                constructed = primitive.codomain()
                transport = constructed.Isom(self.codomain()).an_element()
                composed = transport * primitive * inclusion
                return self(
                    tuple(
                        composed(self.domain().module_generator(label))
                        for label in self.domain().module_generating_set()
                    )
                )
            raise ArithmeticError(
                "Nikulin existence was true but no even-overlattice witness was constructed"
            )
        raise NotImplementedError(
            "no distinguished embedding is implemented for this indefinite target"
        )


class LatticeIsometryHomset(LatticeEmbeddingHomset):
    Element = LatticeIsometry

    def __init__(self, hom_family, domain, codomain) -> None:
        categories = []
        if domain is codomain:
            categories.append(OwnedGroups())
            if (
                _engine_ring(domain.base_ring()) is SageZZ
                and domain.is_finite_rank()
                and domain.is_definite()
            ):
                categories.append(OwnedFiniteGroups())
        LatticeEmbeddingHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
            category=Category.join(tuple(categories)) if categories else None,
        )

    def _element_constructor_(self, images):
        if isinstance(images, LatticeIsometry):
            if (
                images.domain() is not self.domain()
                or images.codomain() is not self.codomain()
            ):
                raise ValueError("the isometry has the wrong lattice endpoints")
            if images.parent() is self:
                return images
            source = self.domain()
            return self.element_class(
                self,
                lambda label: images(source.module_generator(label)),
            )
        return self.element_class(
            self,
            _normalize_lattice_generator_images(self.domain(), images),
        )

    def super_categories(self):
        packet = category_packet(self.base_category())
        source = self.domain()
        target = self.codomain()
        inherited = [
            superpacket.Isos().Of(source, target)
            for superpacket in packet.super_packets()
            if source in superpacket.C() and target in superpacket.C()
        ]
        supers = [
            packet.Homs().Of(source, target),
            packet.Monos().Of(source, target),
            packet.Epis().Of(source, target),
            *inherited,
        ]
        if self.aut_family() is not None:
            supers.append(packet.Ends().Of(source))
            supers.extend(
                superpacket.Auts().Of(source)
                for superpacket in packet.super_packets()
                if source in superpacket.C()
            )
        return supers

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an automorphism homset")
        return self(lambda label: self.domain().module_generator(label))

    def one(self):
        return self.identity()

    identity_automorphism = identity

    def acting_group(self):
        r"""Return ``O(codomain)`` acting by postcomposition on this homset."""
        return self.codomain().Aut()

    def act(self, automorphism, isometry):
        r"""Postcompose an isometry by a codomain automorphism."""
        if automorphism.parent() is not self.acting_group():
            raise ValueError("the torsor action is by the orthogonal group of the codomain")
        if (
            not isinstance(isometry, LatticeIsometry)
            or isometry.domain() is not self.domain()
            or isometry.codomain() is not self.codomain()
        ):
            raise ValueError("the torsor action is on this isometry homset")
        return self(
            lambda label: automorphism(
                isometry(self.domain().module_generator(label))
            )
        )

    def transporter(self, source, target):
        r"""Return the unique ``g in O(M)`` with ``g ∘ source = target``."""
        for candidate in (source, target):
            if (
                not isinstance(candidate, LatticeIsometry)
                or candidate.domain() is not self.domain()
                or candidate.codomain() is not self.codomain()
            ):
                raise ValueError("a transporter compares two isometries in this homset")
        codomain = self.codomain()
        return self.acting_group()(
            lambda label: target(
                source.lift(codomain.module_generator(label))
            )
        )

    def discriminant_image(self):
        r"""Return the subgroup of ``O(A_L)`` generated by the known ``O(L)`` generators."""
        if self.domain() is not self.codomain():
            raise ValueError("the discriminant image is defined for an automorphism group")
        target = self.domain().discriminant_group().orthogonal_group()
        return target.subgroup_on(
            tuple(generator.discriminant_morphism() for generator in self.group_generators())
        )

    def discriminant_preimage(self, subgroup):
        r"""Return ``rho_L^{-1}(subgroup)`` as a predicate subgroup of ``O(L)``."""
        if self.domain() is not self.codomain():
            raise ValueError("a discriminant preimage is defined for an automorphism group")
        target = self.domain().discriminant_group().orthogonal_group()
        containing_group = (
            subgroup
            if subgroup is target
            else getattr(subgroup, "supergroup", lambda: None)()
        )
        if (
            containing_group is None
            or getattr(containing_group, "domain", lambda: None)() is not target.domain()
            or getattr(containing_group, "is_quadratic", lambda: None)()
            != target.is_quadratic()
        ):
            raise ValueError("the subgroup must lie in O(A_L)")

        if int(subgroup.cardinality()) == 1:

            form = target.domain()
            identity = module_homset(form, form).identity()
            predicate = (
                lambda automorphism: automorphism._discriminant_forward_morphism()
                == identity
            )
        else:
            predicate = lambda automorphism: automorphism.discriminant_morphism() in subgroup
        return predicate_subgroup(
            self,
            predicate,
            f"rho_L(g) lies in {subgroup}",
            character_data={"discriminant_preimages": (subgroup,)},
        )

    def lattice(self):
        r"""Return \(L\), the lattice this orthogonal group acts on."""
        assert self.domain() is self.codomain(), (
            "the acted lattice is the common domain and codomain of an automorphism group"
        )
        return self.domain()

    def stabilizer(self, vector):
        r"""Return \(\operatorname{Stab}_{O(L)}(v)=\{g\in O(L): g(v)=v\}\).

        The subgroup is cut out by its defining condition, so it is
        constructed for indefinite \(L\) as well, where \(O(L)\) is infinite
        and cannot be enumerated.  When the engine computes a generating set
        of this subgroup, :meth:`vector_stabilizer_generators` supplies it.
        """
        lattice = self.lattice()
        assert vector.parent() is lattice, (
            "a point stabilizer in O(L) fixes a vector of L"
        )
        return predicate_subgroup(
            self,
            lambda automorphism: automorphism(vector) == vector,
            f"g fixes {vector}",
        )

    def pointwise_stabilizer(self, embedding):
        r"""Return \(\{g\in O(L): g|_I=\mathrm{id}\}\) for \(\iota:I\hookrightarrow L\).

        A linear map that fixes a generating set of \(I\) fixes \(I\)
        pointwise, so the condition is decided on the framing of \(I\).
        """
        lattice = self.lattice()
        assert embedding.codomain() is lattice, (
            "a stabilizer in O(L) is taken of a sublattice of L"
        )
        source = embedding.domain()
        embedded = tuple(
            embedding(generator) for generator in source.module_generators()
        )
        return predicate_subgroup(
            self,
            lambda automorphism: all(
                automorphism(vector) == vector for vector in embedded
            ),
            f"g fixes {source} pointwise",
        )

    def setwise_stabilizer(self, embedding):
        r"""Return \(\{g\in O(L): g(I)=I\}\) for \(\iota:I\hookrightarrow L\).

        The image of \(I\) is carried into itself by \(g\) exactly when every
        \(g(\iota(e))\) has a preimage under \(\iota\); asking the same of
        \(g^{-1}\) turns that containment into equality.  Both conditions are
        decided by the coordinate lift along \(\iota\), so the subgroup is
        constructed for indefinite \(L\) too.

        For a totally isotropic \(I\) this is the parabolic subgroup
        \(P_I\), whose Levi action on \(I^\perp/I\) and unipotent radical are
        read off the isotropic reduction of \(\iota\).
        """
        lattice = self.lattice()
        assert embedding.codomain() is lattice, (
            "a stabilizer in O(L) is taken of a sublattice of L"
        )
        source = embedding.domain()
        embedded = tuple(
            embedding(generator) for generator in source.module_generators()
        )

        def preserves_image(automorphism):
            inverse = automorphism.inverse()
            return all(
                embedding.is_in_image(automorphism(vector))
                and embedding.is_in_image(inverse(vector))
                for vector in embedded
            )

        return predicate_subgroup(
            self,
            preserves_image,
            f"g(I)=I for I={source}",
        )

    @cached_method
    def _engine_group(self):
        r"""Return Sage's private orthogonal-group engine when it is exact.

        The public group remains this homset of live lattice isometries.  Sage's
        ``GroupOfIsometries`` is used only to compute the finite definite
        integral case; its matrices act on row vectors, hence are transposed
        when converted to this homset's column-image convention.
        """
        lattice = self.domain()
        if lattice is not self.codomain():
            raise ValueError("an orthogonal group is an automorphism homset")
        if _engine_ring(lattice.base_ring()) is not SageZZ:
            raise NotImplementedError(
                "the active orthogonal-group engine currently computes integral ZZ-lattices"
            )
        if not lattice.is_finite_rank() or not lattice.is_definite():
            raise NotImplementedError(
                "the available Sage engine computes full generators only for finite definite lattices"
            )
        from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

        return IntegralLattice(
            _engine_component_matrix(lattice.gram_tensor()).change_ring(SageZZ)
        ).orthogonal_group()

    def _from_engine(self, _engine_element):
        r"""Transport one backend row-action isometry to a live automorphism."""
        engine = self._engine_group()
        return self._from_backend_row_action(engine(_engine_element).matrix())

    def _from_backend_row_action(self, row_action_matrix):
        r"""Cross a private row-action matrix into this live isometry homset."""
        codomain = self.codomain()
        ring = codomain.base_ring()
        generators = tuple(codomain.module_generators())
        rank = len(generators)
        images = []
        for source_position in range(int(self.domain().rank())):
            row = row_action_matrix[source_position]
            images.append(
                sum(
                    (
                        codomain.scalar_multiple(
                            ring._from_engine_element(SageZZ(coefficient)),
                            generator,
                        )
                        for coefficient, generator in zip(
                            row, generators, strict=True
                        )
                        if coefficient
                    ),
                    codomain.zero(),
                )
            )
        return self(tuple(images))

    def _to_engine(self, automorphism):
        r"""Transport one live automorphism to the private row-action engine."""
        if (
            not isinstance(automorphism, LatticeIsometry)
            or automorphism.domain() is not self.domain()
            or automorphism.codomain() is not self.codomain()
        ):
            raise ValueError("the engine crossing takes an automorphism in this orthogonal group")

        # Publicly the linear map acts on columns. Sage's GroupOfIsometries
        # acts on coordinate rows on the right, hence one transpose here.
        engine_matrix = _engine_matrix(automorphism.matrix()).transpose()
        return self._engine_group()(engine_matrix)

    @cached_method
    def group_generators(self):
        r"""Return exact generators of ``O(L)`` when the backend computes them."""

        lattice = self.domain()
        if not lattice.is_definite():
            backend_generators = engine_capabilities.compute(
                "lattice.indefinite_automorphism_group", _engine_gram_rows(lattice)
            )
            positions = Sets.Δ[len(backend_generators) - 1]
            return finite_ordered_image(
                positions,
                lambda position: self._from_backend_row_action(
                    backend_generators[int(position)]
                ),
                name=f"Orthogonal-group generators of {lattice}",
            )
        backend_generators = self._engine_group().gens()
        positions = Sets.Δ[len(backend_generators) - 1]
        return finite_ordered_image(
            positions,
            lambda position: self._from_engine(backend_generators[int(position)]),
            name=f"Orthogonal-group generators of {lattice}",
        )

    def number_of_group_generators(self):
        r"""Return the cardinality of the chosen generating set of ``O(L)``."""
        return self.group_generators().cardinality()

    def __iter__(self):
        return (self._from_engine(element) for element in self._engine_group())

    def vector_equivalence_witness(self, left, right):
        r"""Return ``g in O(L)`` with ``g(left)=right``, or ``None``.

        In the finite definite regime this is an exact search through the full
        owned orthogonal group.  Indefinite vector equivalence belongs to its
        separate exact backend and is not approximated here.
        """
        lattice = self.domain()
        if lattice is not self.codomain():
            raise ValueError("vector equivalence is an orthogonal-group operation")
        left = left if getattr(left, "parent", lambda: None)() is lattice else lattice(left)
        right = right if getattr(right, "parent", lambda: None)() is lattice else lattice(right)
        if lattice.q(left) != lattice.q(right):
            return None
        if not lattice.is_definite():
            witness = engine_capabilities.compute(
                "lattice.indefinite_vector_isometry_witness",
                _engine_gram_rows(lattice),
                [int(entry) for entry in left.to_list()],
                [int(entry) for entry in right.to_list()],
            )
            if witness is None:
                return None
            result = self._from_backend_row_action(witness)
            if result(left) != right:
                raise ArithmeticError(
                    "the indefinite vector-equivalence backend returned a witness with the wrong action"
                )
            return result
        for automorphism in self:
            if automorphism(left) == right:
                return automorphism
        return None

    def vectors_are_equivalent(self, left, right) -> bool:
        r"""Return whether two vectors lie in the same ``O(L)``-orbit."""
        return self.vector_equivalence_witness(left, right) is not None

    def vector_stabilizer_generators(self, element):
        r"""Return exact generators of ``Stab_{O(L)}(element)`` when finite.

        The subgroup reduction happens in Sage's private finite isometry group;
        only live lattice isometries cross back into the public result.
        """
        lattice = self.domain()
        element = (
            element
            if getattr(element, "parent", lambda: None)() is lattice
            else lattice(element)
        )
        if not lattice.is_definite():
            isometries = finite_ordered_set(
                tuple(
                    self._from_backend_row_action(engine_isometry)
                    for engine_isometry in engine_capabilities.compute(
                        "lattice.indefinite_vector_stabilizer",
                        _engine_gram_rows(lattice),
                        [int(entry) for entry in element.to_list()],
                    )
                )
            )
            if any(isometry(element) != element for isometry in isometries):
                raise ArithmeticError(
                    "an indefinite vector-stabilizer isometry does not fix the vector"
                )
            return isometries
        stabilizer_elements = tuple(
            automorphism
            for automorphism in self
            if automorphism(element) == element
        )
        engine_subgroup = self._engine_group().subgroup(
            tuple(self._to_engine(automorphism) for automorphism in stabilizer_elements)
        )
        return finite_ordered_set(
            tuple(self._from_engine(engine_isometry) for engine_isometry in engine_subgroup.gens())
        )

    def vector_orbit_representatives(self, square):
        r"""Return one representative of each ``O(L)``-orbit of square ``square``.

        For a definite lattice the represented shell is finite, and ``O(L)``
        is finite, so this is an exact finite quotient with no search bound.
        """
        lattice = self.domain()
        if not lattice.is_definite():
            gram = _engine_gram_rows(lattice)
            lattice_generators = tuple(lattice.module_generators())
            representatives = tuple(
                sum(
                    (
                        lattice.scalar_multiple(
                            lattice.base_ring()(int(coefficient)), generator
                        )
                        for coefficient, generator in zip(
                            row,
                            lattice_generators,
                            strict=True,
                        )
                        if coefficient
                    ),
                    lattice.zero(),
                )
                for row in engine_capabilities.compute(
                    "lattice.indefinite_orbit_representative", gram, int(square)
                )
            )
            if any(lattice.q(representative) != square for representative in representatives):
                raise ArithmeticError(
                    "an indefinite vector-orbit representative has the wrong square"
                )
            return representatives
        remaining = {
            tuple(vector.to_tuple()): vector
            for vector in lattice.vectors_of_square(square)
        }
        representatives = []
        while remaining:
            _coordinates, representative = next(iter(remaining.items()))
            representatives.append(representative)
            for automorphism in self:
                image = automorphism(representative)
                remaining.pop(tuple(image.to_tuple()), None)
        return tuple(representatives)

    def isotropic_orbit_representatives(self, rank, *, flag=False):

        return isotropic_orbit_representatives(self, rank, flag=flag)

    def isotropic_equivalence_witness(self, left, right, *, flag=False):

        return isotropic_equivalence_witness(self, left, right, flag=flag)

    def isotropic_stabilizer_generators(self, obj, *, flag=False):

        return isotropic_stabilizer_generators(self, obj, flag=flag)

    def compose(self, second, first):
        r"""Return ``second ∘ first`` as an isometry."""
        if first.codomain() is not second.domain():
            raise ValueError("isometry composition requires matching middle objects")
        return lattice_isometry_homset(first.domain(), second.codomain())(lambda label: second(first(first.domain().module_generator(label))))

    def is_empty(self):
        r"""Decide emptiness through exact obstructions and proved classifiers.

        Passing an obstruction never proves isometry by itself.  Definite
        survivors are decided by Sage's exact equivalence engine.  Indefinite
        survivors are declared nonempty only in theorem-backed uniqueness
        regimes (Nikulin's indefinite even 2-elementary classification, or
        Eichler when the common genus has one improper spinor genus).  All
        remaining indefinite cases retain Sage's three-valued ``Unknown``.
        """
        domain = self.domain()
        codomain = self.codomain()
        if domain is codomain:
            return False
        if not domain.is_finite_rank() or not codomain.is_finite_rank():
            return Unknown
        if domain.rank() != codomain.rank():
            return True
        if domain.signature_pair() != codomain.signature_pair():
            return True
        if _engine_ring(domain.base_ring()) is not SageZZ or _engine_ring(codomain.base_ring()) is not SageZZ:
            return Unknown

        domain_gram = _engine_component_matrix(domain.gram_tensor()).change_ring(SageZZ)
        codomain_gram = _engine_component_matrix(codomain.gram_tensor()).change_ring(SageZZ)
        if domain_gram == codomain_gram:
            self._definite_witness_matrix = domain_gram.parent().one()
            return False
        rank = domain.rank()
        if rank <= rank.parent().one():
            return True
        if domain.is_nondegenerate() != codomain.is_nondegenerate():
            return True
        if not domain.is_nondegenerate():
            return Unknown
        if domain.is_even() != codomain.is_even():
            return True
        if domain.discriminant() != codomain.discriminant():
            return True
        if (
            domain.discriminant_module().invariant_factors()
            != codomain.discriminant_module().invariant_factors()
        ):
            return True

        from sage.quadratic_forms.genera.genus import Genus as SageGenus
        from sage.quadratic_forms.genera.genus import LocalGenusSymbol
        from sage.rings.rational_field import QQ as SageQQ

        domain_engine = domain_gram
        codomain_engine = codomain_gram
        rational_domain = QuadraticForm(SageQQ, 2 * domain_engine.change_ring(SageQQ))
        rational_codomain = QuadraticForm(SageQQ, 2 * codomain_engine.change_ring(SageQQ))
        if not rational_domain.is_rationally_isometric(rational_codomain):
            return True

        determinant = abs(SageZZ(domain_gram.det()))
        for prime in (2 * determinant).prime_divisors():
            if LocalGenusSymbol(domain_engine, prime) != LocalGenusSymbol(
                codomain_engine, prime
            ):
                return True

        domain_discriminant = domain.discriminant_group()
        codomain_discriminant = codomain.discriminant_group()
        if not domain_discriminant.is_isomorphic(codomain_discriminant):
            return True

        _signature = domain.signature_pair()

        positive, negative = _signature.first(), _signature.second()
        if not (positive and negative):
            sign = SageZZ.one() if negative == 0 else -SageZZ.one()
            transformation = QuadraticForm(
                SageZZ, 2 * sign * codomain_engine
            ).is_globally_equivalent_to(
                QuadraticForm(SageZZ, 2 * sign * domain_engine),
                return_matrix=True,
            )
            if transformation is False:
                return True
            if transformation.transpose() * codomain_gram * transformation != domain_gram:
                raise RuntimeError("the definite-isometry backend returned an invalid witness")
            self._definite_witness_matrix = transformation
            return False

        # The absence of this program is not fatal here: the classification
        # theorems below still decide some pairs, so the capability is asked
        # for first rather than demanded.
        if engine_capabilities.is_available("lattice.indefinite_isometry_witness"):
            witness_rows = engine_capabilities.compute(
                "lattice.indefinite_isometry_witness",
                [list(row) for row in codomain_gram.components()],
                [list(row) for row in domain_gram.components()],
            )
            if witness_rows is None:
                return True
            witness = self._from_backend_row_action(witness_rows)
            self._indefinite_witness = witness
            return False

        if (
            domain.is_even()
            and domain.is_p_elementary(2)
            and codomain.is_p_elementary(2)
            and domain.two_elementary_invariants()
            == codomain.two_elementary_invariants()
        ):
            self._nonconstructive_nonempty_reason = (
                "Nikulin's classification of indefinite even 2-elementary lattices"
            )
            return False

        rank = domain.rank()
        if rank >= rank.parent()(3):
            spinor_generators = SageGenus(domain_engine).spinor_generators(proper=False)
            if not spinor_generators:
                self._nonconstructive_nonempty_reason = (
                    "Eichler's theorem and uniqueness of the improper spinor genus"
                )
                return False
        return Unknown

    def an_element(self):
        r"""Return an explicit isometry when the exact decision exhibits one."""
        if self.domain() is self.codomain():
            return self.identity()
        empty = self.is_empty()
        if empty is Unknown:
            raise NotImplementedError("no exact isometry witness backend is available for this pair")
        if empty:
            raise ValueError("the isometry homset is empty")
        if hasattr(self, "_indefinite_witness"):
            return self._indefinite_witness
        if not hasattr(self, "_definite_witness_matrix"):
            reason = getattr(
                self,
                "_nonconstructive_nonempty_reason",
                "an exact classification theorem",
            )
            raise NotImplementedError(
                f"{reason} proves this isometry homset is nonempty, but no explicit witness backend is available"
            )
        transformation = self._definite_witness_matrix
        codomain = self.codomain()
        codomain_generators = tuple(codomain.module_generators())
        ring = codomain.base_ring()
        images = tuple(
            sum(
                (
                    codomain.scalar_multiple(
                        ring._from_engine_element(coefficient), generator
                    )
                    for coefficient, generator in zip(
                        column, codomain_generators, strict=True
                    )
                    if coefficient
                ),
                codomain.zero(),
            )
            for column in transformation.columns()
        )
        return self(images)

    def _repr_(self):
        if self.domain() is self.codomain():
            return f"Orthogonal group O({self.domain()})"
        return f"Isom({self.domain()}, {self.codomain()})"


@cached_function
def lattice_homset(domain, codomain) -> LatticeHomset:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError("lattice morphisms require one common base ring")
    return domain.lattice_category().Mor(domain, codomain)


@cached_function
def lattice_embedding_homset(domain, codomain) -> LatticeEmbeddingHomset:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError("lattice embeddings require one common base ring")
    return domain.lattice_category().Mono(domain, codomain)


@cached_function
def lattice_isometry_homset(domain, codomain) -> LatticeIsometryHomset:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError("lattice isometries require one common base ring")
    category = domain.lattice_category()
    return category.Aut(domain) if domain is codomain else category.Iso(domain, codomain)


__all__ = [
    "LatticeEmbedding",
    "LatticeEmbeddingHomset",
    "LatticeHomset",
    "LatticeIsometry",
    "LatticeIsometryHomset",
    "LatticeMorphism",
    "lattice_embedding_homset",
    "lattice_homset",
    "lattice_isometry_homset",
]
