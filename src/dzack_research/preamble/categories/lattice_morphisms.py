r"""Form-preserving morphisms, embeddings, and isometries of lattices."""

from typing import TYPE_CHECKING

from sage.groups.matrix_gps.finitely_generated import MatrixGroup
from sage.categories.morphism import Morphism
from sage.matrix.constructor import matrix as engine_matrix
from sage.misc.cachefunc import cached_function, cached_method
from sage.quadratic_forms.binary_qf import BinaryQF
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.element import parent as element_parent

import dzack_research.preamble.categories.lattice_engines as lattice_engines
from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalIsomorphism,
    CategoricalMor,
    _distinct_supercategories,
)
from dzack_research.preamble.categories.group.cyclic_subgroups import CyclicGroups
from dzack_research.preamble.categories.group.groups import (
    OwnedFiniteGroups,
    OwnedGroups,
    _fix_selected_group_resolution_on,
)
from dzack_research.preamble.categories.group.predicate_subgroups import (
    IntersectionSubgroups,
    StabilizerSubgroups,
)
from dzack_research.preamble.categories.isotropic_orbits import (
    _primitive_isotropic_vector_orbit_decomposition,
    _isotropic_equivalence_witness,
    _isotropic_orbit_representatives,
    _isotropic_stabilizer_generators,
)
from dzack_research.preamble.categories.modules.framed.formed.torsion_form_modules import (
    _torsion_form_automorphism_from_engine_matrix,
    _torsion_form_isometry,
)
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    _represented_value_module,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleEmbeddingMethods,
    ModuleMorphism,
    ModuleMorphismMethods,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules, _engine_matrix
from dzack_research.preamble.categories.rings.ring_foundation import (
    _owned_engine_element,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.logic import AtomicProposition
from dzack_research.preamble.validation import validator
from dzack_research.preamble.tensors.tensor import (
    _engine_binary_form_pullback,
    _engine_column_matrix_from_row_action,
    _engine_component_matrix,
    _engine_row_action_matrix,
    tensor,
)

if TYPE_CHECKING:
    from dzack_research.preamble.categories.lattices import Lattices


def _framing_tuple(element):
    r"""Return ordered framing coefficients only at a private engine boundary."""
    parent = element.parent()
    coordinates = element.to_vector()
    return tuple(coordinates(label) for label in parent.module_generating_set())


def _module_matrix(morphism):
    r"""Return the finite-free underlying module Mor element for computation."""
    linear = morphism.domain().module_category().Mor(morphism.domain(), morphism.codomain())(morphism)
    from dzack_research.preamble.categories.modules.pure.modules import MatrixSpaces

    assert linear.parent() in MatrixSpaces(linear.parent().base_ring()), (
        f"{morphism} has no matrix: its domain {morphism.domain()} and codomain "
        f"{morphism.codomain()} must be free modules of finite rank with a chosen basis, "
        f"but the module maps between them form {linear.parent()}"
    )
    return linear


def _binary_form_from_gram(gram):
    r"""Return the integral binary quadratic form ``x |-> gram(x, x)``."""
    return BinaryQF(
        SageZZ(gram[0, 0]),
        SageZZ(2 * gram[0, 1]),
        SageZZ(gram[1, 1]),
    )


def _proper_reduced_binary_equivalence_matrix(source, target):
    r"""Return ``M in SL_2(ZZ)`` with ``M^* source = target``, or ``None``.

    Both forms are reduced indefinite forms of the same non-square
    discriminant.  Sage supplies their proper reduced cycle.  Consecutive
    forms differ alternately by a ``_Rho`` step and its conjugate by
    ``diag(1,-1)``; the step pulling one back to the next is respectively
    ``[[0,-1],[1,s]]`` and ``[[0,1],[-1,s]]``.  Recovering ``s`` from the two
    consecutive exact forms avoids reproducing the reduction algorithm, and the
    steps compose as matrices because pullback is contravariant.
    """
    identity = engine_matrix(SageZZ, ((1, 0), (0, 1)))
    cycle = tuple(source.cycle(proper=True))
    match target in cycle:
        case False:
            return None
    target_position = cycle.index(target)
    transformation = identity
    for position in range(target_position):
        current = cycle[position]
        following = cycle[position + 1]
        denominator = SageZZ(2) * SageZZ(current[2])
        if denominator == 0:
            raise ArithmeticError(
                f"the reduced indefinite binary form {current} in the proper cycle of {source} "
                f"has c = 0, which is impossible for non-square discriminant {source.discriminant()}"
            )
        numerator = SageZZ(following[1]) + SageZZ(current[1])
        candidates = []
        for sign in (SageZZ.one(), -SageZZ.one()):
            signed_numerator = sign * numerator
            step_parameter = signed_numerator // denominator
            if denominator * step_parameter != signed_numerator:
                continue
            if sign == SageZZ.one():
                step = engine_matrix(
                    SageZZ,
                    ((0, -1), (1, step_parameter)),
                )
            else:
                step = engine_matrix(
                    SageZZ,
                    ((0, 1), (-1, step_parameter)),
                )
            if _engine_binary_form_pullback(current, step) == following:
                candidates.append(step)
        if not candidates:
            raise ArithmeticError(
                f"no matrix [[0,-1],[1,s]] or [[0,1],[-1,s]] in SL_2(ZZ) carries the reduced binary form {current} to the next form {following} of its proper cycle"
            )
        step = candidates[0]
        transformation = transformation * step
    return transformation


def _rho_step_matrix(current, following):
    r"""Return the exact ``SL_2(ZZ)`` matrix pulling ``current`` back to ``following=current._Rho()``."""
    denominator = SageZZ(2) * SageZZ(current[2])
    if denominator == 0:
        raise ArithmeticError(f"the reduction step Rho is undefined on the binary form {current}: its c-coefficient is 0")
    numerator = SageZZ(following[1]) + SageZZ(current[1])
    step_parameter = numerator // denominator
    if denominator * step_parameter != numerator:
        raise ArithmeticError(
            f"the reduction step from the binary form {current} to {following} has non-integral parameter {numerator}/{denominator}, so it is not in SL_2(ZZ)"
        )
    return engine_matrix(
        SageZZ,
        ((0, -1), (1, step_parameter)),
    )


def _split_binary_reduction_to_zero_c(form):
    r"""Reduce a split indefinite binary form to ``c=0`` and retain the change of variables."""
    reduced, transformation = form.reduced_form(
        transformation=True,
        algorithm="sage",
    )
    current = reduced
    while current[2] != 0:
        following = current._Rho()
        transformation = transformation * _rho_step_matrix(current, following)
        current = following
    return current, transformation


def _proper_split_binary_equivalence_matrix(source, target):
    r"""Return ``M in SL_2(ZZ)`` with ``M^* source = target`` for split indefinite forms."""
    source_reduced, source_reduction = _split_binary_reduction_to_zero_c(source)
    target_reduced, target_reduction = _split_binary_reduction_to_zero_c(target)
    if source_reduced[1] != target_reduced[1]:
        return None
    b = SageZZ(source_reduced[1])
    if b == 0:
        raise ArithmeticError(
            f"the reduced form {source_reduced} of the split indefinite binary form {source} has b = c = 0, so its discriminant is 0 and the form is not indefinite"
        )
    difference = SageZZ(target_reduced[0]) - SageZZ(source_reduced[0])
    shear_parameter = difference // b
    if b * shear_parameter != difference:
        return None
    shear = engine_matrix(
        SageZZ,
        ((1, 0), (shear_parameter, 1)),
    )
    return source_reduction * shear * target_reduction.inverse()


def _binary_indefinite_isometry_matrix(domain_gram, codomain_gram):
    r"""Return a binary indefinite isometry matrix, or ``False`` when there is none.

    A returned matrix ``P`` pulls the codomain form back to the domain form,
    ``P^* codomain_gram = domain_gram``.  It is an engine answer: the
    isometry built from it is checked by its own form-square validator
    (`OWN-22`).  The non-square-discriminant classification is complete by binary reduction
    cycles.  For square discriminant, Sage's split reduction terminates at a
    form ``a*x^2+b*x*y``; Conway--Sloane's criterion is then constructive via
    an integral shear, with one fixed determinant-minus-one twist handling the
    improper-equivalence case.
    """
    domain_form = _binary_form_from_gram(domain_gram)
    codomain_form = _binary_form_from_gram(codomain_gram)
    if domain_form.discriminant() != codomain_form.discriminant():
        return False
    if domain_form.discriminant().is_square():
        transformation = _proper_split_binary_equivalence_matrix(
            codomain_form,
            domain_form,
        )
        if transformation is None:
            improper_twist = engine_matrix(SageZZ, ((-1, 0), (0, 1)))
            twisted_codomain = _engine_binary_form_pullback(codomain_form, improper_twist)
            proper_after_twist = _proper_split_binary_equivalence_matrix(
                twisted_codomain,
                domain_form,
            )
            if proper_after_twist is None:
                return False
            transformation = improper_twist * proper_after_twist
        return transformation
    domain_reduced, domain_reduction = domain_form.reduced_form(
        transformation=True,
        algorithm="sage",
    )
    codomain_reduced, codomain_reduction = codomain_form.reduced_form(
        transformation=True,
        algorithm="sage",
    )
    reduced_transport = _proper_reduced_binary_equivalence_matrix(
        codomain_reduced,
        domain_reduced,
    )
    if reduced_transport is None:
        swap = engine_matrix(SageZZ, ((0, 1), (1, 0)))
        swapped = _engine_binary_form_pullback(codomain_reduced, swap)
        proper_after_swap = _proper_reduced_binary_equivalence_matrix(
            swapped,
            domain_reduced,
        )
        if proper_after_swap is None:
            return False
        reduced_transport = swap * proper_after_swap
    transformation = codomain_reduction * reduced_transport * domain_reduction.inverse()
    if transformation.base_ring() is not SageZZ:
        transformation = transformation.change_ring(SageZZ)
    return transformation


def _tensor_view(morphism):

    return tensor.from_morphism(morphism)


def _rational_spinor_norm_representative(isometry):
    r"""Return \(b(v_1,v_1)\cdots b(v_m,v_m)\) for an automorphism \(s_{v_1}\cdots s_{v_m}\) of a space over \(\mathbb Q\).

    The private computation behind ``Lattices.spinor_norm``: a representative
    of the spinor norm of the form \(b\) (O'Meara, *Introduction to Quadratic
    Forms*, §55), with the whole square class and not only its sign, computed
    as the discriminant of the Wall form of the isometry by GAP
    (``_gap_rational_spinor_norm_class``).  The owning morphism applies its
    multiplier.
    """
    space = isometry.domain()
    value = lattice_engines._gap_rational_spinor_norm_class(
        space.gram_tensor(),
        isometry,
    )
    return _owned_engine_element(space.base_ring(), value)


def _number_field_spinor_norm_representative(isometry):
    r"""Return the untwisted spinor-norm representative of an automorphism over an owned number field."""
    space = isometry.domain()
    field = space.base_ring()
    return lattice_engines._oscar_lattices.number_field_spinor_norm_class(
        field,
        space.gram_tensor(),
        isometry,
    )


def _labelled_generator_images(domain, images):
    r"""Read the keys of a generator-image mapping as labels of ``domain``'s framing.

    Lattice framings may use formal symbols even though ``module_generator(i)``
    deliberately accepts the integer position ``i``.  A key that is not a
    label is that position in the framing's enumeration, so an explicit image
    mapping keeps the positional spelling before the generic module-morphism
    layer sees the actual labels.
    """
    labels = domain.module_generating_set()
    return {(labels(key) if key in labels else labels[int(key)]): value for key, value in images.items()}


class LatticeMorphismMethods:
    r"""A module morphism preserving the lattice form."""

    if TYPE_CHECKING:
        def domain(self) -> Lattices.ParentMethods: ...
        def codomain(self) -> Lattices.ParentMethods: ...
        def __call__(self, element: Lattices.ElementMethods) -> Lattices.ElementMethods: ...
    _derived_construction_parameters = frozenset(
        {"module_morphism", "value_morphism"}
    )

    def __init__(self, parent, images, *, elementwise=False) -> None:
        domain = parent.domain()
        codomain = parent.codomain()
        module_mor = domain.module_category().Mor(domain, codomain)
        module_morphism = module_mor.elementwise(images) if elementwise else module_mor(images)
        values = _represented_value_module(domain)
        target_values = _represented_value_module(codomain)
        if target_values is not values:
            raise TypeError(f"a lattice morphism {domain} -> {codomain} needs both forms valued in one module, but they take values in {values} and {target_values}")
        super().__init__(
            parent,
            module_morphism,
            values.module_category().Mor(values, values).identity(),
        )

    def __mul__(self, other):
        if not isinstance(other, LatticeMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        return source.Mor(self.codomain())(lambda label: self(other(source.module_generator(label))))


class LatticeMorphism(LatticeMorphismMethods, ModuleMorphism):
    r"""Compatibility shell for private lattice-arrow realizations not yet graph-generated."""

    def __init__(self, parent, images, *, elementwise=False) -> None:
        ModuleMorphism.__init__(self, parent, images, elementwise=elementwise)


class LatticeEmbeddingMethods:
    r"""A form-preserving monomorphism of lattices."""

    @validator
    def validate_injectivity(self) -> None:
        r"""Raise ``ValueError`` unless ``ker(f) = 0`` is established for the underlying linear map."""
        domain = self.domain()
        decision = domain.module_category().Mor(domain, self.codomain())(self).is_injective()
        if decision is False:
            raise ValueError(f"{domain} -> {self.codomain()} is not a lattice embedding: its kernel is nonzero")
        if decision is not True:
            raise ValueError(f"cannot accept {domain} -> {self.codomain()} as a lattice embedding: its injectivity cannot be decided")

    def __mul__(self, other):
        if not isinstance(other, LatticeEmbeddingMethods):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        return source.Emb(self.codomain())(lambda label: self(other(source.module_generator(label))))

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
        from dzack_research.preamble.categories.lattices import IsotropicReductions

        return IsotropicReductions(self.codomain().base_ring())(self)

    def orthogonal_complement(self):
        r"""Return the orthogonal complement of this embedded lattice.

        For an embedding ``i: S -> L`` of finite-rank integral lattices the
        orthogonal complement is the right kernel of the pairing
        ``S \times L -> ZZ``, ``(s, x) \mapsto b_L(i s, x)``, which is the
        pullback of ``b_L`` along ``(i, 1_L)``.  Computing that kernel from the
        pulled-back tensor is the finite-free realization of the generic
        pairing-morphism kernel.
        """
        source = self.domain()
        target = self.codomain()
        if (
            _engine_ring(source.base_ring()) is not SageZZ
            or _engine_ring(target.base_ring()) is not SageZZ
            or not source.module_rank().is_finite()
            or not target.module_rank().is_finite()
        ):
            return super().orthogonal_complement()

        identity = target.module_category().Mor(target, target).identity()
        pairing = target.gram_tensor().pullback(self, identity)
        kernel_basis = _engine_component_matrix(pairing).right_kernel().basis_matrix()
        target_labels = tuple(target.module_generating_set())
        ring = target.base_ring()
        embedded_basis = tuple(
            target.linear_combination(
                {
                    label: _owned_engine_element(ring, coefficient)
                    for label, coefficient in zip(target_labels, row, strict=True)
                    if coefficient
                }
            )
            for row in kernel_basis.rows()
        )
        return target.subobject_on(embedded_basis)

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
        assert _engine_ring(source.base_ring()) is SageZZ and _engine_ring(target.base_ring()) is SageZZ, (
            f"the discriminant inclusion of {self} is computed only for ZZ-lattices, but {source} is over {source.base_ring()} and {target} is over {target.base_ring()}"
        )
        if not (source.module_rank().is_finite() and target.module_rank().is_finite() and source.is_nondegenerate() and target.is_nondegenerate()):
            raise ValueError(f"{self} has no discriminant inclusion: {source} and {target} must both be nondegenerate lattices of finite rank")

        target_discriminant = target.discriminant_module()
        target_dual = target_discriminant.projection().domain()
        target_dual_labels = tuple(target_dual.module_generating_set())

        if target.is_even():
            source_form = source.discriminant_quadratic_form()
            target_form = target.discriminant_quadratic_form()
        else:
            source_form = source.discriminant_bilinear_form()
            target_form = target.discriminant_bilinear_form()

        source_rank = int(source.module_rank())
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
                [rationals.one() if index == source_position else rationals.zero() for index in range(source_rank)],
            )
            source_vector = source_dual_form * basis_covector
            target_vector = inclusion_tensor * source_vector
            extended_covector = target_form_tensor * target_vector
            if any(coefficient not in target_ring for coefficient in extended_covector):
                raise ValueError(
                    f"{self} has no discriminant inclusion: {source} is not an orthogonal "
                    f"direct summand of {target}, since extending by zero the dual vector "
                    f"of {source} at discriminant generator {label} gives a covector with coefficients "
                    f"outside {target_ring}"
                )
            integral_coefficients = tuple(target_ring(coefficient) for coefficient in extended_covector)
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

        return source_form.Mono(target_form)(images, quadratic=target.is_even())


class LatticeEmbedding(LatticeEmbeddingMethods, LatticeMorphism):
    r"""Compatibility shell for private lattice-embedding realizations."""

    def is_injective(self) -> bool:
        r"""True: membership in the embedding Mor states it (``OWN-22``)."""
        return True


class _TransportedLatticeEmbedding(LatticeEmbedding):
    r"""A represented module embedding read in the corresponding lattice Mono."""

    def __init__(self, parent, embedding) -> None:
        self._underlying_module_embedding = embedding
        super().__init__(parent, embedding)


class LatticeIsometryMethods:
    r"""An invertible lattice morphism."""

    def __init__(self, parent, images) -> None:
        match images:
            case CategoricalIsomorphism():
                domain = parent.domain()
                codomain = parent.codomain()
                forward = domain.module_category().Mor(domain, codomain)(images.forward())
                values = _represented_value_module(domain)
                target_values = _represented_value_module(codomain)
                if target_values is not values:
                    raise TypeError(
                        f"a lattice isometry {domain} -> {codomain} needs both forms valued in one module, "
                        f"but they take values in {values} and {target_values}"
                    )
                self._value_morphism = values.module_category().Mor(values, values).identity()
                self._underlying_module_isomorphism = images
                ModuleMorphismMethods.__init__(self, parent, forward)
                return
        self._underlying_module_isomorphism = None
        super().__init__(parent, images)

    def is_surjective(self) -> bool:
        r"""True: membership in the isometry Mor states it (``OWN-22``)."""
        return True

    @validator
    def validate_surjectivity(self) -> None:
        r"""Raise ``ValueError`` unless ``coker(f) = 0`` is established for the underlying linear map."""
        domain = self.domain()
        decision = domain.module_category().Mor(domain, self.codomain())(self).is_surjective()
        if decision is False:
            raise ValueError(f"{domain} -> {self.codomain()} is not an isometry: it is not surjective")
        if decision is not True:
            raise ValueError(f"cannot accept {domain} -> {self.codomain()} as an isometry: its surjectivity cannot be decided")

    @cached_method
    def _coordinate_tensor(self):
        r"""The type-``(1,1)`` tensor of this isometry in the chosen framings, computed once."""
        return _tensor_view(self)

    def base_change(self, ring_map):
        r"""Extend this isometry along the selected ring map as an isometry.

        Scalar extension preserves inverse pairs and the defining form
        equation. Retain those facts explicitly instead of forgetting to a
        bare module morphism and re-proving surjectivity and form preservation
        in the target lattice hom-set.
        """
        ring = self.domain().base_ring()
        if self.codomain().base_ring() is not ring or ring_map.domain() is not ring:
            raise ValueError(
                "a lattice isometry can only be base changed along a map out "
                "of the common base ring of its endpoints"
            )
        scalar_extension = Modules(ring).scalar_extension(ring_map)
        source = scalar_extension(self.domain())
        target = scalar_extension(self.codomain())
        forward = scalar_extension(self)
        inverse = scalar_extension(self.inverse())
        module_isomorphism = source.module_category().Core().Mor(
            source,
            target,
        )._from_known_inverse_pair(
            forward,
            inverse,
        )
        homset = source.Isom(target)
        return homset.element_class(homset, module_isomorphism)

    def inverse(self):
        r"""Return the inverse isometry."""
        codomain = self.codomain()
        module_isomorphism = self._underlying_module_isomorphism
        if module_isomorphism is not None:
            target = codomain.Isom(self.domain())
            reverse = codomain.module_category().Core().Mor(
                codomain,
                self.domain(),
            )._from_known_inverse_pair(
                module_isomorphism.inverse(),
                module_isomorphism.forward(),
            )
            return target.element_class(target, reverse)
        if self.domain().module_rank().is_finite() and codomain.module_rank().is_finite():
            forward_matrix = _engine_matrix(_module_matrix(self))
            return codomain.Isom(self.domain())._isometry_from_column_matrix(
                forward_matrix.inverse()
            )
        return codomain.Isom(self.domain())(lambda label: self.lift(codomain.module_generator(label)))

    def __invert__(self):
        return self.inverse()

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        return (
            isinstance(other, LatticeIsometryMethods) and other.domain() is self.domain() and other.codomain() is self.codomain() and other._coordinate_tensor() == self._coordinate_tensor()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(
            (
                id(self.domain()),
                id(self.codomain()),
                self._coordinate_tensor(),
            )
        )

    def determinant(self):
        r"""Return the determinant of this automorphism/isometry tensor."""
        if self.domain().module_rank() != self.codomain().module_rank():
            raise ValueError(f"{self} has no determinant: its domain has rank {self.domain().module_rank()} and its codomain has rank {self.codomain().module_rank()}")
        return _module_matrix(self).determinant()

    def __mul__(self, other):
        if isinstance(other, LatticeIsometryMethods) and other.codomain() is self.domain():
            if self.domain() is self.codomain() and other.parent() is self.parent():
                return self.parent().compose(self, other)
            source = other.domain()
            return source.Isom(self.codomain())(lambda label: self(other(source.module_generator(label))))
        return super().__mul__(other)

    def transport_isotropic_object(self, obj):
        r"""Transport a primitive isotropic subobject or flag along this isometry.

        A subobject \(\iota:I\hookrightarrow L\) goes to the image of
        \(g\circ\iota\); a flag goes to the flag of the images of its basis.
        """
        from dzack_research.preamble.categories.isotropic_orbits import IsotropicFlag
        from dzack_research.preamble.categories.modules.pure.modules import (
            ModuleSubobjects,
        )

        match obj in ModuleSubobjects(self.codomain().base_ring()):
            case True:
                return (self * obj.inclusion()).image()
            case False:
                return IsotropicFlag(
                    self.codomain(),
                    tuple(self(element) for element in obj.isotropic_basis()),
                )

    @cached_method
    def invariant_lattice(self):
        r"""Return ``ker(self-id)`` as a formed subobject of the lattice."""
        if self.domain() is not self.codomain():
            raise ValueError(f"{self} has no invariant lattice: it is an isometry from {self.domain()} to {self.codomain()}, not an automorphism of one lattice")
        lattice = self.domain()

        difference = lattice.module_category().Mor(lattice, lattice)(tuple(self(generator) - generator for generator in lattice.module_generators()))
        return difference.kernel()

    @cached_method
    def formed_coinvariants(self):
        r"""Return ``(L^self)^perp`` as a formed subobject of ``L``.

        This is deliberately not called ``coinvariants``: module coinvariants
        are the quotient ``L/(self-1)L`` and are generally a different object.
        """
        return self.invariant_lattice().orthogonal_complement()

    @cached_method
    def primitive_extension(self):
        r"""Return the retained primitive extension cut out by this isometry.

        The two primitive sublattices are ``S = ker(self-id)`` and
        ``T = S^perp`` inside the ambient lattice.  The extension retains
        their inclusions, the finite-index map ``S direct-sum T -> L``, and
        its discriminant gluing.  Here ``T`` is the formed orthogonal
        complement; it is not the module quotient ``L/(self-id)L``.
        """
        if self.domain() is not self.codomain():
            raise ValueError(f"{self} cuts out no primitive extension: it is an isometry from {self.domain()} to {self.codomain()}, not an automorphism of one lattice")
        from dzack_research.preamble.categories.lattice_centralizers import (
            IsometryPrimitiveExtension,
        )

        return IsometryPrimitiveExtension(self)

    def centralizer_group(self):
        r"""Return ``Z_{O(L)}(self)`` through the owned primitive-extension data."""
        return self.primitive_extension().centralizer_group()

    def cyclotomic_summand(self, order):
        r"""Return ``ker Phi_d(self)`` as a primitive sublattice.

        Here ``d`` is ``order``.  The kernel of a module morphism into a
        torsion-free module is saturated, so no separate saturation step is
        needed.  If this isometry has finite order ``n``, the summands over
        divisors ``d`` of ``n`` span a finite-index sublattice and each is the
        intersection with the rational cyclotomic subspace ``V_{Phi_d}``.
        """
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no cyclotomic summand ker Phi_{order}: it is an isometry from {self.domain()} to {self.codomain()}, not an automorphism of one lattice"
            )
        from sage.rings.polynomial.cyclotomic import cyclotomic_coeffs

        lattice = self.domain()
        ring = lattice.base_ring()
        coefficients = cyclotomic_coeffs(int(order))

        def image(label):
            iterate = lattice.module_generator(label)
            total = lattice.zero()
            for coefficient in coefficients:
                total = total + lattice.scalar_multiple(ring(int(coefficient)), iterate)
                iterate = self(iterate)
            return total

        evaluated = lattice.module_category().Mor(lattice, lattice)({label: image(label) for label in lattice.module_generating_set()})
        return evaluated.kernel()

    @cached_method
    def cyclotomic_decomposition(self, order):
        r"""Return the integral cyclotomic decomposition for this finite-order automorphism."""
        from dzack_research.preamble.categories.lattice_centralizers import (
            CyclotomicDecomposition,
        )

        return CyclotomicDecomposition(self, order)

    @cached_method
    def polarized(self, polarization):
        r"""Retain an invariant nonzero polarization together with this automorphism."""
        from dzack_research.preamble.categories.lattice_centralizers import (
            PolarizedEquivariantLattice,
        )

        return PolarizedEquivariantLattice(self, polarization)

    def equivariant_sublattice(self, sublattice):
        r"""Return this automorphism restricted to a stable represented sublattice."""
        from dzack_research.preamble.categories.lattice_centralizers import (
            _restrict_isometry,
        )

        return _restrict_isometry(self, sublattice)

    def equivariant_isometry_to(self, other):
        r"""Return ``h`` with ``h*self = other*h`` when exactly decidable."""
        if self.domain() is not self.codomain() or other.domain() is not other.codomain():
            raise ValueError(
                f"an equivariant isometry from {self} to {other} requires both to be "
                f"automorphisms of one lattice each, but they are maps "
                f"{self.domain()} -> {self.codomain()} and {other.domain()} -> {other.codomain()}"
            )
        source = self.domain()
        target = other.domain()
        if source is target and self == other:
            return source.O().one()
        mor = source.Isom(target)
        empty = mor.is_empty()
        if empty is True:
            return None
        if target.module_rank().is_finite() and target.is_definite():
            for candidate in mor:
                if candidate * self == other * candidate:
                    return candidate
            return None
        assert empty is False, (
            f"cannot find an isometry h: {source} -> {target} with h*{self} = {other}*h: "
            f"{target} is indefinite or of infinite rank, and whether {source} and {target} "
            f"are isometric at all could not be decided"
        )
        witness = mor.an_element()
        assert witness * self == other * witness, (
            f"cannot decide whether {self} and {other} are conjugate by an isometry "
            f"{source} -> {target}: the one isometry found, {witness}, does not satisfy "
            f"h*{self} = {other}*h, and no conjugacy classification exists for indefinite lattices"
        )
        return witness

    def equivariant_vector_orbit_decomposition(self, square):
        r"""Return exact centralizer orbits on vectors of the selected square."""
        from dzack_research.preamble.categories.lattice_centralizers import (
            _equivariant_vector_orbit_decomposition,
        )

        return _equivariant_vector_orbit_decomposition(self, square)

    def equivariant_vector_orbit_representatives(self, square):
        r"""Return vector-orbit representatives under ``Z_{O(L)}(self)`` in the supported regime."""
        return self.equivariant_vector_orbit_decomposition(square).representatives()

    def equivariant_sublattice_orbit_decomposition(self, sublattices):
        r"""Return exact centralizer orbits on a finite stable family of sublattices."""
        from dzack_research.preamble.categories.isotropic_orbits import _same_subobject
        from dzack_research.preamble.categories.lattice_centralizers import (
            _equivariant_finite_orbit_decomposition,
            _transport_sublattice,
        )

        sublattices = tuple(sublattices)
        for sublattice in sublattices:
            self.equivariant_sublattice(sublattice)
        return _equivariant_finite_orbit_decomposition(
            self,
            sublattices,
            _transport_sublattice,
            _same_subobject,
        )

    def equivariant_flag(self, terms):
        r"""Return the represented nested flag of sublattices stable under this automorphism."""
        from dzack_research.preamble.categories.lattice_centralizers import (
            EquivariantSublatticeFlag,
        )

        return EquivariantSublatticeFlag(self, terms)

    def equivariant_flag_orbit_decomposition(self, flags):
        r"""Return exact centralizer orbits on a finite stable family of equivariant flags."""
        from dzack_research.preamble.categories.lattice_centralizers import (
            _equivariant_finite_orbit_decomposition,
            _same_equivariant_flag,
            _transport_equivariant_flag,
        )

        flags = tuple(flags)
        if any(flag.isometry() != self for flag in flags):
            raise ValueError(f"the flags {flags} are not all stable flags of {self}: some flag belongs to a different automorphism")
        return _equivariant_finite_orbit_decomposition(
            self,
            flags,
            _transport_equivariant_flag,
            _same_equivariant_flag,
        )

    @cached_method
    def _discriminant_forward_morphism(self):
        r"""Return the induced module map on discriminant groups.

        For an isometry ``f: L -> M`` the map ``f^#: L^# -> M^#`` sends the
        dual basis vector ``e^s`` to the vector whose ``r``-th dual-basis
        coordinate is ``b_M(f e^s, m_r) = b_L(e^s, f^{-1} m_r)``, the
        ``e_s``-coordinate of ``f^{-1}(m_r)``.
        """
        source = self.domain().discriminant_group()
        target = self.codomain().discriminant_group()
        target_dual = target.projection().domain()
        target_dual_generators = target_dual.module_generators()
        inverse = ~self
        codomain = self.codomain()
        preimage_coordinates = tuple(
            inverse(codomain.module_generator(label)).to_vector()
            for label in codomain.module_generating_set()
        )
        images = {}
        for domain_label, label in zip(
            self.domain().module_generating_set(), source.module_generating_set(), strict=True
        ):
            dual_image = sum(
                (
                    target_dual.scalar_multiple(
                        coordinates(domain_label),
                        target_dual_generators[target_position],
                    )
                    for target_position, coordinates in enumerate(preimage_coordinates)
                    if coordinates(domain_label)
                ),
                target_dual.zero(),
            )
            images[label] = target.projection()(dual_image)

        return source.module_category().Mor(source, target)(images)

    @cached_method
    def discriminant_isometry(self):
        r"""Return the induced isometry ``Disc(self): A_L -> A_M``.

        For ``f:L->M`` the map on duals is ``(f^{-1})^vee:L^vee->M^vee``.
        Passing to the cokernels of the correlation maps gives the finite-form
        isometry on discriminant modules.
        """

        forward = self._discriminant_forward_morphism()
        inverse = (~self)._discriminant_forward_morphism()
        return _torsion_form_isometry(
            forward,
            inverse,
            quadratic=self.domain().is_even(),
        )

    @cached_method
    def discriminant_morphism(self):
        r"""Return ``Disc(self)`` parented by ``O(A_L)`` for an automorphism."""
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} induces no automorphism of a discriminant form: it is an isometry from {self.domain()} to {self.codomain()}, not an automorphism of one lattice"
            )
        form = self.domain().discriminant_group()
        return form.orthogonal_group().from_morphism(self._discriminant_forward_morphism())

    def is_involution(self) -> bool:
        r"""Return whether this lattice automorphism satisfies ``self^2 = 1``."""
        match self.domain() is self.codomain():
            case False:
                return False
            case True:
                return self * self == self.parent().one()

    def cyclic_subgroup(self):
        r"""Return the literal subgroup ``<self> <= O(L)``."""
        if self.domain() is not self.codomain():
            raise ValueError(f"{self} generates no cyclic subgroup of an orthogonal group: it is an isometry from {self.domain()} to {self.codomain()}, not an automorphism")

        return CyclicGroups()(self)

    def preserves_positive_cone(self) -> bool:
        r"""Return whether an isometry preserves a component of the positive cone.

        This character is defined here only for signature ``(1,n)``, where
        ``{v : b(v,v)>0}`` has exactly two components.  For one exact rational
        positive vector ``v``, the isometry preserves its component exactly
        when ``b(v,g(v))>0``.
        """
        if self.domain() is not self.codomain():
            raise ValueError(
                f"cannot ask whether {self} preserves the positive cone: it is an isometry from {self.domain()} to {self.codomain()}, not an automorphism of one lattice"
            )
        lattice = self.domain()
        _signature = lattice.signature_pair()
        positive, negative = _signature.first(), _signature.second()
        integers = positive.parent()
        if positive != integers.one() or negative < integers.one():
            raise ValueError(
                f"cannot ask whether {self} preserves the positive cone of {lattice}: the "
                f"positive cone has two components only in signature (1,n) with n >= 1, "
                f"but {lattice} has signature {(positive, negative)}"
            )

        rationals = lattice.base_ring().fraction_field()
        gram = lattice.gram_tensor().change_ring(rationals)
        vector = lattice_engines._rational_positive_vector(gram)
        image = _tensor_view(self).change_ring(rationals) * vector
        pairing = gram.contract(vector, image)
        if pairing == rationals.zero():
            raise ArithmeticError(f"the positive vector {vector} of {lattice} is orthogonal to its image {image} under {self}, which is impossible in signature (1,n)")
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
            raise ValueError(
                f"{self} has no centralizer in an orthogonal group: it is an isometry from {self.domain()} to {self.codomain()}, not an automorphism of one lattice"
            )
        lattice = self.domain()
        assert _engine_ring(lattice.base_ring()) is SageZZ, (
            f"the image of the centralizer of {self} in O(A_L) is computed only for ZZ-lattices, but {lattice} is over {lattice.base_ring()}"
        )
        if not lattice.is_even():
            raise ValueError(f"the image of the centralizer of {self} in O(A_L) is computed by hermitian Miranda--Morrison theory only for even lattices, but {lattice} is odd")
        if not lattice.module_rank().is_finite() or not lattice.is_nondegenerate():
            raise ValueError(f"the image of the centralizer of {self} in O(A_L) requires {lattice} to be a nondegenerate lattice of finite rank")

        engine_generators, expected_order, invariant_rank, coinvariant_rank = lattice_engines._oscar_lattices.centralizer_discriminant_image(
            lattice.gram_tensor(),
            self,
        )
        if self.invariant_lattice().module_rank() != invariant_rank:
            raise ArithmeticError(
                f"OSCAR gives rank {invariant_rank} for the invariant lattice of {self}, but "
                f"its invariant lattice ker({self} - 1) has rank "
                f"{self.invariant_lattice().module_rank()}"
            )
        if self.formed_coinvariants().module_rank() != coinvariant_rank:
            raise ArithmeticError(
                f"OSCAR gives rank {coinvariant_rank} for the coinvariant lattice of {self}, "
                f"but its coinvariant lattice (L^g)^perp has rank "
                f"{self.formed_coinvariants().module_rank()}"
            )

        orthogonal_group = lattice.discriminant_group().orthogonal_group()
        generators = tuple(
            _torsion_form_automorphism_from_engine_matrix(
                orthogonal_group,
                # Both OSCAR's finite discriminant group and Sage's FQF
                # engine act on their Smith generators on the right.
                _engine_component_matrix(engine_generator),
            )
            for engine_generator in engine_generators
        )
        induced = self.discriminant_morphism()
        if any(generator * induced != induced * generator for generator in generators):
            raise ArithmeticError(
                f"a generator OSCAR returned for the image of the centralizer of {self} in O(A_L) does not commute with the induced discriminant automorphism {induced}"
            )
        image = orthogonal_group.subgroup_on(generators)
        if image.order() != expected_order:
            raise ArithmeticError(
                f"the subgroup of O(A_L) generated by OSCAR's centralizer-image generators for {self} has order {image.order()}, but OSCAR reports order {expected_order}"
            )
        return image


class LatticeIsometry(LatticeIsometryMethods, LatticeEmbedding):
    r"""Compatibility shell for private lattice-isometry realizations."""


class LatticeMor(CategoricalMor):
    ElementMethods = LatticeMorphismMethods

    def __init__(self, mor_family, domain, codomain) -> None:
        domain.base_ring()
        lattices = domain.lattice_category()
        if domain not in lattices or codomain not in lattices:
            raise TypeError(
                f"no lattice morphisms from {domain} to {codomain}: both must be objects of {lattices}, but they lie in {domain.category()} and {codomain.category()}"
            )
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images, *, check=False):
        r"""Construct the lattice morphism; ``check=True`` runs its validators (``OWN-22``)."""
        morphism = self._morphism_from_images(images)
        morphism.validate_linearity(check=check)
        morphism.validate_form_preservation(check=check)
        return morphism

    def _morphism_from_images(self, images):
        if isinstance(images, ModuleMorphismMethods):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError(
                    f"the module morphism {images} goes from {images.domain()} to "
                    f"{images.codomain()}, so it is not a lattice morphism from "
                    f"{self.domain()} to {self.codomain()}"
                )
            if images.parent() is self:
                return images
            return self.element_class(self, images)
        if isinstance(images, Morphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError(
                    f"the morphism {images} goes from {images.domain()} to {images.codomain()}, so it is not a lattice morphism from {self.domain()} to {self.codomain()}"
                )
            return self.elementwise(lambda element: images(element))
        if isinstance(images, dict):
            images = _labelled_generator_images(self.domain(), images)
        return self.element_class(self, images)

    def elementwise(self, function):
        if not callable(function):
            raise TypeError(f"{function} cannot define a lattice morphism from {self.domain()} to {self.codomain()}: it is not a function of the elements of {self.domain()}")
        source = self.domain()
        return self.element_class(
            self,
            lambda label: function(source.module_generator(label)),
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(f"there is no identity morphism from {self.domain()} to {self.codomain()}: they are different lattices")
        return self.elementwise(lambda element: element)

    def _repr_(self):
        return f"LatticeMor({self.domain()}, {self.codomain()})"


class LatticeEmbeddingMor(CategoricalMor):
    ElementMethods = LatticeEmbeddingMethods

    def __init__(self, mor_family, domain, codomain, *, category=None) -> None:
        lattices = domain.lattice_category()
        if domain not in lattices or codomain not in lattices:
            raise TypeError(
                f"no lattice embeddings from {domain} to {codomain}: both must be objects of {lattices}, but they lie in {domain.category()} and {codomain.category()}"
            )
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
            category=category,
        )

    def _element_constructor_(self, images, *, check=False):
        r"""Construct the lattice embedding; ``check=True`` runs its validators (``OWN-22``)."""
        embedding = self._morphism_from_images(images)
        embedding.validate_linearity(check=check)
        embedding.validate_form_preservation(check=check)
        embedding.validate_injectivity(check=check)
        return embedding

    def _morphism_from_images(self, images):
        if isinstance(images, ModuleEmbeddingMethods):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError(
                    f"the module embedding {images} goes from {images.domain()} to "
                    f"{images.codomain()}, so it is not a lattice embedding of "
                    f"{self.domain()} into {self.codomain()}"
                )
            return _TransportedLatticeEmbedding(self, images)
        if isinstance(images, ModuleMorphismMethods):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError(
                    f"the module morphism {images} goes from {images.domain()} to "
                    f"{images.codomain()}, so it is not a lattice embedding of "
                    f"{self.domain()} into {self.codomain()}"
                )
            if images.parent() is self:
                return images
            return self.element_class(self, images)
        if isinstance(images, Morphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError(
                    f"the morphism {images} goes from {images.domain()} to {images.codomain()}, so it is not a lattice embedding of {self.domain()} into {self.codomain()}"
                )
            return self.elementwise(lambda element: images(element))
        if isinstance(images, dict):
            images = _labelled_generator_images(self.domain(), images)
        return self.element_class(self, images)

    def elementwise(self, function):
        if not callable(function):
            raise TypeError(f"{function} cannot define a lattice embedding of {self.domain()} into {self.codomain()}: it is not a function of the elements of {self.domain()}")
        source = self.domain()
        return self.element_class(
            self,
            lambda label: function(source.module_generator(label)),
        )

    def super_categories(self):
        packet = self.base_category().category_packet()
        source = self.domain()
        target = self.codomain()
        inherited = [superpacket.Monos().Of(source, target) for superpacket in packet.super_packets() if source in superpacket.C() and target in superpacket.C()]
        return [packet.Mors().Of(source, target), *inherited]

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"

    def _codomain_is_even_unimodular_indefinite(self) -> bool:
        target = self.codomain()
        if not target.module_rank().is_finite() or not target.is_nondegenerate():
            return False
        _signature = target.signature_pair()
        positive, negative = _signature.first(), _signature.second()
        return positive > 0 and negative > 0 and target.is_even() and target.is_unimodular()

    def even_overlattice_inclusions(self):
        r"""Return the finite even-overlattice sweep used by Nikulin existence."""
        return self.domain().even_overlattice_inclusions()

    @cached_method
    def _target_primitive_embedding_data(self):
        source = self.domain()
        target = self.codomain()
        if (
            _engine_ring(source.base_ring()) is not SageZZ
            or _engine_ring(target.base_ring()) is not SageZZ
            or not source.module_rank().is_finite()
            or not target.module_rank().is_finite()
            or not source.is_nondegenerate()
            or not target.is_nondegenerate()
            or source.module_rank() >= target.module_rank()
            or target.is_definite()
        ):
            return None
        return lattice_engines._oscar_lattices.target_primitive_embedding(
            source.gram_tensor(),
            target.gram_tensor(),
        )

    def _target_primitive_embedding(self):
        data = self._target_primitive_embedding_data()
        assert data is not None, (
            f"no primitive embedding of {self.domain()} into {self.codomain()} can be "
            f"constructed: this requires nondegenerate ZZ-lattices of finite rank with "
            f"the source of smaller rank and an indefinite target"
        )
        if data is False:
            raise ValueError(f"there is no primitive embedding of {self.domain()} into {self.codomain()}")
        return self._reconstruct_target_primitive_embedding(data)

    def _reconstruct_target_primitive_embedding(self, data):
        target_prime_gram, source_prime_gram, embedding_matrix = data
        from dzack_research.preamble.categories.lattices import Lattices

        source = self.domain()
        target = self.codomain()
        lattices = Lattices(source.base_ring())
        source_prime = lattices(source_prime_gram)
        target_prime = lattices(target_prime_gram)
        source_to_prime = source.Isom(source_prime).an_element()
        target_prime_to_target = target_prime.Isom(target).an_element()
        target_prime_generators = tuple(target_prime.module_generators())
        inclusion = source_prime.Emb(target_prime)(
            tuple(
                sum(
                    (
                        target_prime.scalar_multiple(
                            embedding_matrix[row, column],
                            target_prime_generators[row],
                        )
                        for row in range(int(target_prime.module_rank()))
                        if embedding_matrix[row, column]
                    ),
                    target_prime.zero(),
                )
                for column in range(int(source_prime.module_rank()))
            )
        )
        composed = target_prime_to_target * inclusion * source_to_prime
        embedding = self(tuple(composed(source.module_generator(label)) for label in source.module_generating_set()))
        if not embedding.is_primitive():
            raise ArithmeticError(f"the embedding {embedding} of {source} into {target} built from OSCAR's primitive embedding is not primitive")
        return embedding

    def primitive_embedding_class_representatives(self, classification="emb"):
        r"""Return OSCAR/Nikulin representatives of primitive-embedding classes.

        ``classification='sub'`` classifies primitive sublattices up to the
        actions of ``O(source)`` and the target discriminant group, whereas
        ``classification='emb'`` retains the source marking and quotients only
        by the target discriminant action.  These are finite class
        representatives, not an enumeration of every embedding.
        """
        if classification not in ("sub", "emb"):
            raise ValueError(
                f"classification={classification!r} is not a classification of primitive embeddings: use 'sub' (sublattices up to O(source)) or 'emb' (embeddings)"
            )
        source = self.domain()
        target = self.codomain()
        assert (
            _engine_ring(source.base_ring()) is SageZZ
            and _engine_ring(target.base_ring()) is SageZZ
            and source.module_rank().is_finite()
            and target.module_rank().is_finite()
            and source.is_nondegenerate()
            and target.is_nondegenerate()
            and source.module_rank() <= target.module_rank()
        ), (
            f"primitive embeddings of {source} into {target} are classified only for "
            f"nondegenerate ZZ-lattices of finite rank with rank(source) <= rank(target); "
            f"here the base rings are {source.base_ring()} and {target.base_ring()}"
        )
        data = lattice_engines._oscar_lattices.target_primitive_embedding_classes(
            source.gram_tensor(),
            target.gram_tensor(),
            classification,
        )
        assert data is not None, f"OSCAR returned no classification of primitive embeddings of {source} into {target}"
        return finite_ordered_set(tuple(self._reconstruct_target_primitive_embedding(record) for record in data))

    def __iter__(self):
        r"""Enumerate all embeddings when the target lattice is definite.

        Each source generator must land in the finite shell of target vectors
        having the same square.  A depth-first placement is pruned by the
        pairings with generators already placed, so a complete placement
        preserves the form.  A form-preserving map into a definite lattice
        sends each vector \(x\) of the radical of the source to a vector with
        \(q=0\), which is zero; so every complete placement is injective when
        the source form is nondegenerate, and none is when it is degenerate.
        """
        source = self.domain()
        target = self.codomain()
        assert target.module_rank().is_finite() and target.is_definite(), (
            f"the embeddings of {source} into {target} are enumerated only when {target} is definite of finite rank"
        )
        assert source.module_rank().is_finite(), f"the embeddings of {source} into {target} are enumerated only when {source} has finite rank"
        match source.is_nondegenerate():
            case False:
                return
        source_generators = tuple(source.module_generators())
        source_gram = source.gram_tensor()
        pools = tuple(tuple(target.vectors_of_square(source_gram[index, index])) for index in range(len(source_generators)))

        def assign(placed):
            position = len(placed)
            if position == len(source_generators):
                yield self(tuple(placed))
                return
            for candidate in pools[position]:
                if all(target.b(placed[index], candidate) == source_gram[index, position] for index in range(position)):
                    yield from assign((*placed, candidate))

        yield from assign(())

    def is_empty(self):
        if self.codomain().module_rank().is_finite() and self.codomain().is_definite():
            for _embedding in self:
                return False
            return True
        source = self.domain()
        target = self.codomain()
        if source.module_rank().is_finite() and target.module_rank().is_finite() and source.module_rank() == target.module_rank():
            return source.Isom(target).is_empty()
        target_embedding_data = self._target_primitive_embedding_data()
        if target_embedding_data is False:
            return True
        if target_embedding_data is not None:
            return False
        if self._codomain_is_even_unimodular_indefinite():
            match source.is_even():
                case False:
                    return True
                case True:
                    _signature = self.codomain().signature_pair()
                    positive, negative = _signature.first(), _signature.second()
                    return not any(inclusion.codomain().embeds_in_even_unimodular(positive, negative) for inclusion in self.even_overlattice_inclusions())
        return AtomicProposition("is_empty", self)

    def an_element(self):
        if self.codomain().module_rank().is_finite() and self.codomain().is_definite():
            for embedding in self:
                return embedding
            raise ValueError(f"there is no lattice embedding of {self.domain()} into {self.codomain()}")
        source = self.domain()
        target = self.codomain()
        if source.module_rank().is_finite() and target.module_rank().is_finite() and source.module_rank() == target.module_rank():
            isometry = source.Isom(target).an_element()
            return self(tuple(isometry(source.module_generator(label)) for label in source.module_generating_set()))
        target_embedding_data = self._target_primitive_embedding_data()
        if target_embedding_data is not None:
            return self._target_primitive_embedding()
        if self._codomain_is_even_unimodular_indefinite():
            if self.is_empty():
                raise ValueError(f"there is no lattice embedding of {self.domain()} into {self.codomain()}")
            _signature = self.codomain().signature_pair()
            positive, negative = _signature.first(), _signature.second()
            for inclusion in self.even_overlattice_inclusions():
                overlattice = inclusion.codomain()
                if not overlattice.embeds_in_even_unimodular(positive, negative):
                    continue
                primitive = overlattice.embed_in_even_unimodular(positive, negative)
                constructed = primitive.codomain()
                transport = constructed.Isom(self.codomain()).an_element()
                composed = transport * primitive * inclusion
                return self(tuple(composed(self.domain().module_generator(label)) for label in self.domain().module_generating_set()))
            raise ArithmeticError(
                f"Nikulin's criterion says {self.domain()} embeds into the even unimodular "
                f"lattice {self.codomain()}, but no even overlattice of {self.domain()} "
                f"yielded a primitive embedding"
            )
        assert False, (
            f"cannot construct an embedding of {self.domain()} into {self.codomain()}: "
            f"embeddings are constructed only into definite targets, targets of equal "
            f"rank, indefinite targets OSCAR classifies, and even unimodular indefinite "
            f"targets, and {self.codomain()} is none of these"
        )


class LatticeIsometryMor(LatticeEmbeddingMor):
    ElementMethods = LatticeIsometryMethods

    def __init__(self, mor_family, domain, codomain) -> None:
        categories = []
        if domain is codomain:
            categories.append(OwnedGroups())
            if (
                _engine_ring(domain.base_ring()) in (SageZZ, SageQQ)
                and domain.module_rank().is_finite()
                and domain.is_definite()
            ):
                categories.append(OwnedFiniteGroups())
        LatticeEmbeddingMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
            category=Cat().meet(tuple(categories)) if categories else None,
        )
        if (
            domain is codomain
            and _engine_ring(domain.base_ring()) in (SageZZ, SageQQ)
            and domain.module_rank().is_finite()
            and domain.is_definite()
        ):
            self._select_computed_group_resolution()

    def _element_constructor_(self, images, *, check=False):
        r"""Construct the isometry; ``check=True`` runs its validators (``OWN-22``)."""
        isometry = self._morphism_from_images(images)
        isometry.validate_linearity(check=check)
        isometry.validate_form_preservation(check=check)
        isometry.validate_injectivity(check=check)
        isometry.validate_surjectivity(check=check)
        return isometry

    def _morphism_from_images(self, images):
        if isinstance(images, LatticeIsometryMethods):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError(
                    f"the isometry {images} goes from {images.domain()} to {images.codomain()}, so it is not an isometry from {self.domain()} to {self.codomain()}"
                )
            if images.parent() is self:
                return images
            return self.element_class(self, images)
        if isinstance(images, dict):
            images = _labelled_generator_images(self.domain(), images)
        return self.element_class(self, images)

    def super_categories(self):
        packet = self.base_category().category_packet()
        source = self.domain()
        target = self.codomain()
        inherited = [superpacket.Isos().Of(source, target) for superpacket in packet.super_packets() if source in superpacket.C() and target in superpacket.C()]
        supers = [
            packet.Mors().Of(source, target),
            packet.Monos().Of(source, target),
            packet.Epis().Of(source, target),
            *inherited,
        ]
        if self.aut_family() is not None:
            supers.append(packet.Ends().Of(source))
            supers.extend(superpacket.Auts().Of(source) for superpacket in packet.super_packets() if source in superpacket.C())
        return _distinct_supercategories(supers)

    def identity(self) -> LatticeIsometryMethods:
        if self.domain() is not self.codomain():
            raise ValueError(f"there is no identity isometry from {self.domain()} to {self.codomain()}: they are different lattices")
        return self(lambda label: self.domain().module_generator(label))

    def one(self):
        return self.identity()

    def ambient_lattice(self):
        r"""Return the lattice acted on by this orthogonal group."""
        return self.lattice()

    def contains(self, element) -> bool:
        r"""Return whether ``element`` is an isometry in this fixed orthogonal group."""
        return element in self

    identity_automorphism = identity

    def acting_group(self):
        r"""Return ``O(codomain)`` acting by postcomposition on this Mor."""
        return self.codomain().Aut()

    def cardinality(self):
        r"""Return the cardinality of ``Isom(L,M)`` from its torsor structure.

        An empty isometry Mor has cardinality zero.  A nonempty one is a
        torsor under ``O(M)`` by postcomposition and therefore has the same
        cardinality as ``O(M)``.  When emptiness is undecided, the cardinality
        is not computed (`CAT-01`).
        """
        empty = self.is_empty()
        assert empty is True or empty is False, (
            f"cannot compute the cardinality of {self}: it is undecided whether "
            f"{self.domain()} and {self.codomain()} are isometric"
        )
        if empty:
            return cardinal(0)
        return self.acting_group().cardinality()

    def act(self, automorphism, isometry):
        r"""Postcompose an isometry by a codomain automorphism."""
        if automorphism.parent() is not self.acting_group():
            raise ValueError(
                f"{automorphism} cannot act on the isometries {self.domain()} -> "
                f"{self.codomain()} by postcomposition: it lies in {automorphism.parent()}, "
                f"not in the orthogonal group {self.acting_group()} of {self.codomain()}"
            )
        if element_parent(isometry) is not self:
            raise ValueError(
                f"{automorphism} acts by postcomposition only on isometries {self.domain()} -> {self.codomain()}, but {isometry} lies in {element_parent(isometry)}"
            )
        return self(lambda label: automorphism(isometry(self.domain().module_generator(label))))

    def transporter(self, source, target):
        r"""Return an orthogonal transporter.

        For lattice vectors this is an exact orbit witness ``g(source)=target``.
        For two isometries in ``Isom(L,M)`` it retains the torsor operation
        ``g ∘ source = target``.
        """
        lattice = self.codomain()
        if self.domain() is lattice and element_parent(source) is lattice and element_parent(target) is lattice:
            return self.vector_equivalence_witness(source, target)
        for candidate in (source, target):
            if element_parent(candidate) is not self:
                raise ValueError(
                    f"no transporter from {source} to {target} in {self.acting_group()}: "
                    f"{candidate} is neither a vector of {lattice} nor an isometry "
                    f"{self.domain()} -> {self.codomain()}"
                )
        codomain = self.codomain()
        return self.acting_group()(lambda label: target(source.lift(codomain.module_generator(label))))

    def discriminant_image(self):
        r"""Return the subgroup of ``O(A_L)`` generated by the known ``O(L)`` generators."""
        if self.domain() is not self.codomain():
            raise ValueError(f"the isometries {self.domain()} -> {self.codomain()} form no group, so they have no image in the orthogonal group of a discriminant form")
        target = self.domain().discriminant_group().orthogonal_group()
        return target.subgroup_on(tuple(generator.discriminant_morphism() for generator in self.select_group_resolution().group_generators()))

    def discriminant_lift(self, automorphism):
        r"""Return ``g in O(L)`` inducing ``automorphism`` on ``A_L``, or ``None``.

        The image of ``O(L) -> O(A_L)`` is finite.  Starting from the known
        arithmetic generators of ``O(L)``, enumerate that finite image while
        retaining one live lattice isometry above every image element.  The
        search is exhaustive in the generated image and therefore returns
        ``None`` exactly when the selected discriminant automorphism is not in
        that image; no denominator bound or lattice-vector search is used.
        """
        if self.domain() is not self.codomain():
            raise ValueError(
                f"cannot lift {automorphism} to an isometry {self.domain()} -> "
                f"{self.codomain()}: lifts along O(L) -> O(A_L) require an orthogonal group "
                f"O(L), and these are different lattices"
            )
        target = self.domain().discriminant_group().orthogonal_group()
        automorphism = target(automorphism)
        representation = self.discriminant_representation()
        witnesses = self.select_group_resolution().finite_image_lifts(representation)
        return witnesses.get(automorphism)

    def discriminant_preimage(self, subgroup):
        r"""Return ``rho_L^{-1}(subgroup)`` as a predicate subgroup of ``O(L)``.

        ``subgroup`` is a subgroup ``H`` of ``O(A_L)``, given with its
        inclusion ``H -> O(A_L)``.  The preimage is cut out of ``O(L)`` by the
        one predicate ``rho_L(g) in H``.
        """
        if self.domain() is not self.codomain():
            raise ValueError(f"the isometries {self.domain()} -> {self.codomain()} form no orthogonal group O(L), so {subgroup} has no preimage under O(L) -> O(A_L)")
        target = self.domain().discriminant_group().orthogonal_group()
        assert subgroup.inclusion().codomain() is target, (
            f"{subgroup} has no preimage under O(L) -> O(A_L) for L = {self.domain()}: "
            f"it is a subgroup of {subgroup.inclusion().codomain()}, not of {target}"
        )
        return self.discriminant_representation().preimage_subgroup(
            subgroup,
            description=f"rho_L(g) lies in {subgroup}",
            character_data={"discriminant_preimages": (subgroup,)},
        )

    def discriminant_representation(self):
        r"""Return ``rho_A: O(L) -> O(A_L)``."""
        return self.lattice().discriminant_representation()

    def component_character(self):
        r"""Return the positive-cone component character when defined."""
        return self.lattice().component_character()

    def preimage(self, morphism, subgroup):
        r"""Return the subgroup ``morphism^{-1}(subgroup)`` of this group."""
        if morphism.domain() is not self:
            raise ValueError(f"cannot take the preimage of {subgroup} in {self} under {morphism}: its domain is {morphism.domain()}, not {self}")
        return morphism.preimage_subgroup(subgroup)

    def kernel(self, morphism):
        r"""Return the kernel subgroup of a represented group morphism."""
        if morphism.domain() is not self:
            raise ValueError(f"the kernel of {morphism} is not a subgroup of {self}: its domain is {morphism.domain()}, not {self}")
        return morphism.kernel()

    def stable_subgroup(self):
        r"""Return ``ker(O(L) -> O(A_L))``."""
        return self.lattice().stable_orthogonal_group()

    def component_subgroup(self):
        r"""Return the positive-cone-preserving subgroup when defined."""
        return self.lattice().positive_cone_subgroup()

    def centralizer(self, isometry):
        r"""Return ``Z_{O(L)}(isometry)`` as an exact predicate subgroup."""
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            CentralizerSubgroups,
        )

        return CentralizerSubgroups(self)(isometry)

    def intersection(self, *subgroups):
        r"""Return the intersection of represented subgroups of this orthogonal group."""
        return IntersectionSubgroups(self)(subgroups)

    def lattice(self):
        r"""Return \(L\), the lattice this orthogonal group acts on."""
        assert self.domain() is self.codomain(), (
            f"the isometries {self.domain()} -> {self.codomain()} are not an orthogonal group O(L): domain and codomain are different lattices"
        )
        return self.domain()

    def stabilizer(self, target, action="setwise"):
        r"""Return a vector or sublattice stabilizer in ``O(L)``.

        A lattice vector is fixed pointwise.  A represented lattice subobject
        accepts ``action='setwise'`` or ``action='pointwise'`` and delegates to
        the existing inclusion-based subgroup constructions.
        """
        lattice = self.lattice()
        from dzack_research.preamble.categories.modules.pure.modules import (
            ModuleSubobjects,
        )

        if target in ModuleSubobjects(lattice.base_ring()):
            embedding = target.inclusion()
            if embedding.codomain() is not lattice:
                raise ValueError(f"{target} has no stabilizer in O({lattice}): it is a sublattice of {embedding.codomain()}, not of {lattice}")
            if action == "setwise":
                return self.setwise_stabilizer(embedding)
            if action == "pointwise":
                return self.pointwise_stabilizer(embedding)
            raise ValueError(f"action={action!r} is not a stabilizer of the sublattice {target}: use 'setwise' (g(I) = I) or 'pointwise' (g fixes I elementwise)")
        if action != "setwise":
            raise ValueError(f"action={action!r} applies only to sublattices; {target} is not a sublattice of {lattice}, and a vector is always fixed pointwise")
        assert target.parent() is lattice, (
            f"{target} has no stabilizer in O({lattice}): it is neither a vector nor a sublattice of {lattice}, but an element of {target.parent()}"
        )
        return StabilizerSubgroups(self)(
            target,
            "pointwise",
            lambda automorphism: automorphism(target) == target,
            description=f"g fixes {target}",
        )

    def pointwise_stabilizer(self, embedding):
        r"""Return \(\{g\in O(L): g|_I=\mathrm{id}\}\) for \(\iota:I\hookrightarrow L\).

        A linear map that fixes a generating set of \(I\) fixes \(I\)
        pointwise, so the condition is decided on the framing of \(I\).
        """
        lattice = self.lattice()
        assert embedding.codomain() is lattice, (
            f"{embedding} does not embed into {lattice}, so its image has no stabilizer in O({lattice}); its codomain is {embedding.codomain()}"
        )
        source = embedding.domain()
        embedded = tuple(embedding(generator) for generator in source.module_generators())
        return StabilizerSubgroups(self)(
            source,
            "pointwise",
            lambda automorphism: all(automorphism(vector) == vector for vector in embedded),
            description=f"g fixes {source} pointwise",
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
            f"{embedding} does not embed into {lattice}, so its image has no stabilizer in O({lattice}); its codomain is {embedding.codomain()}"
        )
        source = embedding.domain()
        embedded = tuple(embedding(generator) for generator in source.module_generators())

        def preserves_image(automorphism):
            inverse = automorphism.inverse()
            return all(embedding.is_in_image(automorphism(vector)) and embedding.is_in_image(inverse(vector)) for vector in embedded)

        return StabilizerSubgroups(self)(
            source,
            "setwise",
            preserves_image,
            description=f"g(I)=I for I={source}",
        )

    @cached_method
    def _engine_group(self):
        r"""Return Sage's private orthogonal-group engine when it is exact.

        The public group remains this Mor of live lattice isometries.  Sage's
        ``GroupOfIsometries`` is used only to compute the finite definite
        integral case; its matrices act on row vectors, hence are transposed
        when converted to this Mor's column-image convention.
        """
        lattice = self.domain()
        if lattice is not self.codomain():
            raise ValueError(f"the isometries {lattice} -> {self.codomain()} are not an orthogonal group O(L): domain and codomain are different lattices")
        assert lattice.module_rank().is_finite() and lattice.is_definite(), (
            f"O({lattice}) is computed as a finite group only for definite lattices of finite rank, and {lattice} is not one"
        )
        from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

        engine_ring = _engine_ring(lattice.base_ring())
        match engine_ring is SageZZ, engine_ring is SageQQ:
            case True, _:
                gram = _engine_component_matrix(lattice.gram_tensor()).change_ring(SageZZ)
            case False, True:
                rational_gram = _engine_component_matrix(lattice.gram_tensor()).change_ring(SageQQ)
                denominator = SageZZ.one()
                for entry in rational_gram.list():
                    denominator = denominator.lcm(SageZZ(entry.denominator()))
                gram = (denominator * rational_gram).change_ring(SageZZ)
            case _:
                raise ValueError(
                    f"O({lattice}) is computed by the finite definite engine only over ZZ or QQ, "
                    f"but {lattice} is over {lattice.base_ring()}"
                )
        signature = lattice.signature_pair()
        if signature.first() == lattice.base_ring().zero() and signature.second() != lattice.base_ring().zero():
            gram = -gram
        engine = IntegralLattice(gram).orthogonal_group()
        # PARI's ``qfauto`` (Plesken--Souvignier) returns |O(L)| with the
        # generators; GAP would otherwise recompute the order of the matrix
        # group by an orbit algorithm.  TRAPS.md records both wall times.
        engine.gap().SetSize(SageZZ(QuadraticForm(SageZZ, 2 * gram).number_of_automorphisms()))
        return engine

    def _from_engine(self, _engine_element):
        r"""Transport one backend row-action isometry to a live automorphism."""
        engine = self._engine_group()
        return self._from_backend_row_action(engine(_engine_element).matrix())

    def _from_backend_row_action(self, row_action_matrix):
        r"""Cross a private row-action matrix into this live isometry Mor."""
        codomain = self.codomain()
        ring = codomain.base_ring()
        generators = tuple(codomain.module_generators())
        return self(
            tuple(
                sum(
                    (
                        codomain.scalar_multiple(
                            _owned_engine_element(ring, SageZZ(coefficient)),
                            generator,
                        )
                        for coefficient, generator in zip(column, generators, strict=True)
                        if coefficient
                    ),
                    codomain.zero(),
                )
                for column in _engine_column_matrix_from_row_action(row_action_matrix).columns()
            )
        )

    def _row_action_matrix(self, automorphism):
        r"""Return the private row-action matrix of one live lattice isometry."""
        if element_parent(automorphism) is not self:
            raise ValueError(f"{automorphism} has no matrix in {self}: it lies in {element_parent(automorphism)}")
        return _engine_row_action_matrix(automorphism)

    def _to_engine(self, automorphism):
        r"""Transport one live automorphism to the full private engine."""
        return self._engine_group()(self._row_action_matrix(automorphism))

    def _engine_subgroup_from_generators(self, generators):
        r"""Build only the matrix group generated by the selected isometries.

        This does not require a presentation of the full orthogonal group.
        In particular, explicit isometries returned by an indefinite-lattice
        computation can generate their represented subgroup even when Sage has
        no engine for all of ``O(L)``.
        """
        matrices = tuple(self._row_action_matrix(generator) for generator in generators)
        if not matrices:
            rank = int(self.domain().module_rank())
            identity = engine_matrix.identity(SageZZ, rank)
            ambient = MatrixGroup((identity,))
            return ambient.subgroup(())
        return MatrixGroup(matrices)

    def _to_subgroup_engine(self, automorphism, engine_subgroup):
        r"""Cross a live isometry directly into a generated matrix subgroup."""
        return engine_subgroup(self._row_action_matrix(automorphism))

    def _from_subgroup_engine(self, engine_element):
        r"""Raise an element of a generated matrix subgroup to a live isometry."""
        return self._from_backend_row_action(engine_element.matrix())

    @cached_method
    def _computed_group_generators(self):
        r"""Return generators of ``O(L)``, computed by a backend, as a finite ordered set of ``O(L)``.

        For definite ``L``, Sage's ``GroupOfIsometries`` computes the
        generators of the finite group ``O(L)``. For indefinite ``L``,
        ``sage_indefinite_port`` computes them. Both answers are untrusted
        engine output: each computed isometry is constructed through ``O(L)``
        into an element of ``O(L)``, and the family becomes one finite ordered
        set of ``O(L)``.
        """
        lattice = self.domain()
        if lattice.is_definite():
            generators = tuple(self._from_engine(generator) for generator in self._engine_group().gens())
        else:
            from sage_indefinite_port.indefinite.recursive import (
                orthogonal_group_generators,
            )

            generators = tuple(self(generator) for generator in orthogonal_group_generators(self))
        positions = Sets.Δ[len(generators) - 1]
        return FiniteOrderedSets().from_indexed(
            positions,
            lambda position: generators[int(position)],
            name=f"Orthogonal-group generators of {lattice}",
        )

    def _select_computed_group_resolution(self) -> None:
        r"""Select the generating epimorphism from the free group on the computed generators of ``O(L)``.

        Selecting computes nothing; the generators are computed when
        ``group_generators()`` first reads the selected resolution.
        """
        _fix_selected_group_resolution_on(self, self._computed_group_generators)

    def select_group_resolution(self):
        r"""Select the generating epimorphism ``F(S) -> O(L)`` on the computed generating set ``S``, and return ``O(L)``.

        It is the degree-zero truncation of a free-group resolution of
        ``O(L)`` (``CAT-29``); after it, ``group_generators()`` answers.
        """
        if self.has_selected_group_resolution():
            return self
        self._select_computed_group_resolution()
        return self

    def structure_description(self):
        r"""Return GAP's descriptive structure label for a finite ``O(L)``.

        The maintained Sage ``GroupOfIsometries`` computation uses GAP internally and
        supplies ``StructureDescription``.  This method is intentionally
        descriptive only: GAP does not promise that the returned string is an
        isomorphism invariant, so no equality or subgroup decision in the
        owned layer depends on it.
        """
        lattice = self.domain()
        assert lattice.is_definite(), f"O({lattice}) has a structure description only when it is finite, i.e. when {lattice} is definite, and {lattice} is indefinite"
        return str(self._engine_group().structure_description())

    def __iter__(self):
        return (self._from_engine(element) for element in self._engine_group())

    def vector_equivalence_witness(self, left, right):
        r"""Return ``g in O(L)`` with ``g(left)=right``, or ``None``.

        In the finite definite regime this is an exact search through the full
        owned orthogonal group.  Indefinite vector equivalence belongs to its
        separate exact computation and is not approximated here.
        """
        lattice = self.domain()
        if lattice is not self.codomain():
            raise ValueError(f"{left} and {right} cannot be compared under the isometries {lattice} -> {self.codomain()}: these form no orthogonal group O(L)")
        left = left if element_parent(left) is lattice else lattice(left)
        right = right if element_parent(right) is lattice else lattice(right)
        if left == right:
            return self.one()
        if lattice.q(left) != lattice.q(right):
            return None
        if not lattice.is_definite():
            from sage_indefinite_port.indefinite.recursive import (
                vector_equivalence_witness,
            )

            return vector_equivalence_witness(self, left, right)
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
        element = element if element_parent(element) is lattice else lattice(element)
        if not lattice.is_definite():
            from sage_indefinite_port.indefinite.recursive import (
                vector_stabilizer_generators,
            )

            return vector_stabilizer_generators(self, element)
        stabilizer_elements = tuple(automorphism for automorphism in self if automorphism(element) == element)
        engine_subgroup = self._engine_group().subgroup(tuple(self._to_engine(automorphism) for automorphism in stabilizer_elements))
        return finite_ordered_set(tuple(self._from_engine(engine_isometry) for engine_isometry in engine_subgroup.gens()))

    def vector_orbit_representatives(self, square):
        r"""Return one representative of each ``O(L)``-orbit of square ``square``.

        For a definite lattice the represented shell is finite, and ``O(L)``
        is finite, so this is an exact finite quotient with no search bound.
        """
        lattice = self.domain()
        square = lattice.base_ring()(int(square))
        if not lattice.is_definite():
            from sage_indefinite_port.indefinite.recursive import (
                vector_orbit_representatives,
            )

            return vector_orbit_representatives(self, square)
        remaining = {_framing_tuple(vector): vector for vector in lattice.vectors_of_square(square)}
        representatives = []
        while remaining:
            _coordinates, representative = next(iter(remaining.items()))
            representatives.append(representative)
            for automorphism in self:
                image = automorphism(representative)
                remaining.pop(_framing_tuple(image), None)
        return finite_ordered_set(representatives)

    def isotropic_orbit_representatives(self, rank, *, flag=False):

        return _isotropic_orbit_representatives(self, rank, flag=flag)

    def cusps(self, rank=1):
        r"""Return the ``O(L)``-orbits of primitive isotropic rank-``rank`` subobjects."""
        from dzack_research.preamble.categories.isotropic_orbits import _cusp

        return finite_ordered_set(tuple(_cusp(representative) for representative in self.isotropic_orbit_representatives(rank)))

    def tits_building_incidence(self):
        r"""Return the line/plane incidence in the full orthogonal-group quotient building."""
        from dzack_research.preamble.categories.isotropic_orbits import CuspIncidence

        lattice = self.lattice()
        line_cusps = self.cusps(1)
        plane_cusps = self.cusps(2)
        incidences = []
        for flag in self.isotropic_orbit_representatives(2, flag=True):
            line, plane = flag.terms()
            line_vertices = tuple(cusp for cusp in line_cusps if line in cusp)
            plane_vertices = tuple(cusp for cusp in plane_cusps if plane in cusp)
            if len(line_vertices) != 1 or len(plane_vertices) != 1:
                raise ArithmeticError(
                    f"the isotropic flag {flag} of {lattice} has line {line} in "
                    f"{len(line_vertices)} O(L)-orbits of isotropic lines and plane {plane} in "
                    f"{len(plane_vertices)} O(L)-orbits of isotropic planes; each must lie in exactly one"
                )
            line_cusp = line_vertices[0]
            plane_cusp = plane_vertices[0]
            line_transporter = line_cusp.transporter_witness(line)
            plane_transporter = plane_cusp.transporter_witness(plane)
            if line_transporter is None or plane_transporter is None:
                raise ArithmeticError(
                    f"the isotropic flag {flag} of {lattice} lies in the cusps {line_cusp} and "
                    f"{plane_cusp}, but no element of O(L) carries their representatives "
                    f"to its line {line} and plane {plane}"
                )
            incidences.append(
                CuspIncidence(
                    flag,
                    line_cusp,
                    plane_cusp,
                    line_transporter,
                    plane_transporter,
                    self.isotropic_stabilizer_generators(flag, flag=True),
                )
            )
        assert all(incidence.lattice() is lattice for incidence in incidences), f"an incidence of cusps of O({lattice}) belongs to a different lattice than {lattice}"
        return finite_ordered_set(tuple(incidences))

    def orbit_decomposition(self, locus):
        r"""Return exact orbit data on a represented locus supported by this group.

        The first supported infinite locus is the primitive isotropic vector
        locus.  It uses the exact rank-one isotropic orbit computation and returns a
        structured finite list of orbits, each retaining its representative,
        stabilizer and transporter operation.  The locus states which orbit
        decomposition it has.
        """
        if locus is self.lattice().primitive_isotropic_vectors():
            return _primitive_isotropic_vector_orbit_decomposition(self, locus)
        return locus.orbit_decomposition(self)

    def isotropic_equivalence_witness(self, left, right, *, flag=False):

        return _isotropic_equivalence_witness(self, left, right, flag=flag)

    def isotropic_stabilizer_generators(self, obj, *, flag=False):

        return _isotropic_stabilizer_generators(self, obj, flag=flag)

    def compose(self, second, first):
        r"""Return ``second ∘ first`` as an isometry."""
        if first.codomain() is not second.domain():
            raise ValueError(f"cannot compose {second} after {first}: the codomain {first.codomain()} of {first} is not the domain {second.domain()} of {second}")
        return first.domain().Isom(second.codomain())(lambda label: second(first(first.domain().module_generator(label))))

    def is_empty(self):
        r"""Decide emptiness through exact obstructions and proved classifiers.

        Passing an obstruction never proves isometry by itself.  Definite
        survivors are decided by Sage's exact equivalence engine, binary
        indefinite survivors by reduction of binary forms where it decides,
        and the remaining indefinite survivors by ``sage-indefinite-port``.
        """
        return self._isometry_decision()[0]

    def _isometry_from_column_matrix(self, transformation):
        r"""The isometry whose \(j\)-th generator image has the \(j\)-th column of ``transformation`` as coordinates."""
        domain = self.domain()
        codomain = self.codomain()
        codomain_generators = tuple(codomain.module_generators())
        ring = codomain.base_ring()
        domain_rank = int(domain.module_rank())
        codomain_rank = int(codomain.module_rank())
        if transformation.nrows() != codomain_rank or transformation.ncols() != domain_rank:
            raise ValueError(
                f"the matrix of an isometry {domain} -> {codomain} must have shape "
                f"({codomain_rank}, {domain_rank}), but {transformation} has shape "
                f"({transformation.nrows()}, {transformation.ncols()})"
            )
        if domain_rank != codomain_rank:
            raise ValueError(
                f"there is no matrix isometry {domain} -> {codomain}: the ranks "
                f"{domain_rank} and {codomain_rank} differ"
            )

        inverse_transformation = transformation.inverse()
        domain_generators = tuple(domain.module_generators())

        forward = domain.module_category().Mor(domain, codomain)(
            tuple(
                sum(
                    (
                        codomain.scalar_multiple(_owned_engine_element(ring, coefficient), generator)
                        for coefficient, generator in zip(column, codomain_generators, strict=True)
                        if coefficient
                    ),
                    codomain.zero(),
                )
                for column in transformation.columns()
            )
        )
        inverse_ring = domain.base_ring()
        inverse = codomain.module_category().Mor(codomain, domain)(
            tuple(
                sum(
                    (
                        domain.scalar_multiple(
                            _owned_engine_element(inverse_ring, coefficient), generator
                        )
                        for coefficient, generator in zip(
                            column, domain_generators, strict=True
                        )
                        if coefficient
                    ),
                    domain.zero(),
                )
                for column in inverse_transformation.columns()
            )
        )
        module_isomorphism = domain.module_category().Core().Mor(domain, codomain)(
            forward,
            inverse,
        )
        return self.element_class(self, module_isomorphism)

    @cached_method
    def _isometry_decision(self):
        r"""The decision of this isometry Mor object, with the witness that decided it.

        Private computation record of :meth:`is_empty` and :meth:`an_element`:
        the triple of the emptiness answer (``True``, ``False`` or the
        proposition that the Mor is empty), an explicit isometry when the deciding computation
        exhibits one (else ``None``), and the theorem that proves
        nonemptiness without a witness (else ``None``).
        """
        domain = self.domain()
        codomain = self.codomain()
        if domain is codomain:
            return (False, self.identity(), None)
        undecided = AtomicProposition("is_empty", self)
        if not domain.module_rank().is_finite() or not codomain.module_rank().is_finite():
            return (undecided, None, None)
        if domain.module_rank() != codomain.module_rank():
            return (True, None, None)
        if domain.signature_pair() != codomain.signature_pair():
            return (True, None, None)
        if _engine_ring(domain.base_ring()) is not SageZZ or _engine_ring(codomain.base_ring()) is not SageZZ:
            return (undecided, None, None)

        domain_gram = _engine_component_matrix(domain.gram_tensor()).change_ring(SageZZ)
        codomain_gram = _engine_component_matrix(codomain.gram_tensor()).change_ring(SageZZ)
        if domain_gram == codomain_gram:
            return (
                False,
                self._isometry_from_column_matrix(domain_gram.parent().one()),
                None,
            )
        rank = domain.module_rank()
        if int(rank.finite_value()) <= 1:
            return (True, None, None)
        if domain.is_nondegenerate() != codomain.is_nondegenerate():
            return (True, None, None)
        if not domain.is_nondegenerate():
            return (undecided, None, None)
        if domain.is_even() != codomain.is_even():
            return (True, None, None)
        if domain.discriminant() != codomain.discriminant():
            return (True, None, None)
        if domain.discriminant_module().invariant_factors() != codomain.discriminant_module().invariant_factors():
            return (True, None, None)

        from sage.quadratic_forms.genera.genus import LocalGenusSymbol
        from sage.rings.rational_field import QQ as SageQQ

        domain_engine = domain_gram
        codomain_engine = codomain_gram
        rational_domain = QuadraticForm(SageQQ, 2 * domain_engine.change_ring(SageQQ))
        rational_codomain = QuadraticForm(SageQQ, 2 * codomain_engine.change_ring(SageQQ))
        if not rational_domain.is_rationally_isometric(rational_codomain):
            return (True, None, None)

        determinant = abs(SageZZ(domain_gram.det()))
        for prime in (2 * determinant).prime_divisors():
            if LocalGenusSymbol(domain_engine, prime) != LocalGenusSymbol(codomain_engine, prime):
                return (True, None, None)

        domain_discriminant = domain.discriminant_group()
        codomain_discriminant = codomain.discriminant_group()
        if not domain_discriminant.is_isomorphic(codomain_discriminant):
            return (True, None, None)

        _signature = domain.signature_pair()

        positive, negative = _signature.first(), _signature.second()
        if positive == 0 or negative == 0:
            sign = SageZZ.one() if negative == 0 else -SageZZ.one()
            transformation = QuadraticForm(SageZZ, 2 * sign * codomain_engine).is_globally_equivalent_to(
                QuadraticForm(SageZZ, 2 * sign * domain_engine),
                return_matrix=True,
            )
            if transformation is False:
                return (True, None, None)
            # The engine's matrix is an untrusted answer; the isometry's own
            # form-square validator checks it under strict checking (OWN-22).
            return (False, self._isometry_from_column_matrix(transformation), None)

        if int(domain.module_rank()) == 2:
            binary_witness = _binary_indefinite_isometry_matrix(
                domain_gram,
                codomain_gram,
            )
            if binary_witness is False:
                return (True, None, None)
            return (False, self._isometry_from_column_matrix(binary_witness), None)

        from sage_indefinite_port.indefinite.recursive import isometry

        witness = isometry(domain, codomain)
        if witness is None:
            return (True, None, None)
        return (False, witness, None)

    def an_element(self):
        r"""Return an explicit isometry when the exact decision exhibits one."""
        empty, witness, reason = self._isometry_decision()
        assert empty is True or empty is False, f"cannot decide whether {self.domain()} and {self.codomain()} are isometric, so no isometry between them can be returned"
        if empty:
            raise ValueError(f"there is no isometry from {self.domain()} to {self.codomain()}: the lattices are not isometric")
        assert witness is not None, f"{self.domain()} and {self.codomain()} are isometric by {reason}, but no explicit isometry between them can be constructed"
        return witness

    def _repr_(self):
        if self.domain() is self.codomain():
            return f"Orthogonal group O({self.domain()})"
        return f"Isom({self.domain()}, {self.codomain()})"


@cached_function(key=lambda domain, codomain: (id(domain), id(codomain)))
def _lattice_mor(domain, codomain) -> LatticeMor:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError(f"no lattice morphisms from {domain} to {codomain}: {domain} is over {ring} and {codomain} is over {codomain.base_ring()}, not the same base ring")
    return domain.lattice_category().Mor(domain, codomain)


@cached_function(key=lambda domain, codomain: (id(domain), id(codomain)))
def _lattice_embedding_mor(domain, codomain) -> LatticeEmbeddingMor:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError(f"no lattice embeddings of {domain} into {codomain}: {domain} is over {ring} and {codomain} is over {codomain.base_ring()}, not the same base ring")
    return domain.lattice_category().Mono(domain, codomain)


@cached_function(key=lambda domain, codomain: (id(domain), id(codomain)))
def _lattice_isometry_mor(domain, codomain) -> LatticeIsometryMor:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError(f"no lattice isometries from {domain} to {codomain}: {domain} is over {ring} and {codomain} is over {codomain.base_ring()}, not the same base ring")
    category = domain.lattice_category()
    return category.Aut(domain) if domain is codomain else category.Iso(domain, codomain)


__all__ = [
    "LatticeEmbedding",
    "LatticeEmbeddingMor",
    "LatticeMor",
    "LatticeIsometry",
    "LatticeIsometryMor",
    "LatticeMorphism",
]
