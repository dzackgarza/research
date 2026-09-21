r"""Form-preserving morphisms, embeddings, and isometries of lattices."""

from sage.groups.matrix_gps.finitely_generated import MatrixGroup
from sage.categories.morphism import Morphism
from sage.matrix.constructor import matrix as engine_matrix
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.quadratic_forms.binary_qf import BinaryQF
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import parent as element_parent

import dzack_research.preamble.categories.lattice_engines as lattice_engines
from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    _fix_selected_framing,
)
from dzack_research.preamble.categories.group.cyclic_subgroups import CyclicGroups
from dzack_research.preamble.categories.group.groups import (
    Groups,
    OwnedFiniteGroups,
    OwnedGroups,
    _group_framing_morphism,
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
    _torsion_form_isometry,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleEmbedding,
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import _engine_matrix
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.engine_capabilities import engine_capabilities
from dzack_research.preamble.refine import realize_owned_category, refine
from dzack_research.preamble.tensors.tensor import (
    _engine_component_matrix,
    tensor,
)


def _engine_gram_rows(lattice):
    r"""Return the Gram entries as plain integer rows, the shape the programs read."""
    rank = int(lattice.module_rank())
    gram = lattice.gram_tensor()
    return [[int(gram[i, j]) for j in range(rank)] for i in range(rank)]


def _framing_tuple(element):
    r"""Return ordered framing coefficients only at a private engine boundary."""
    parent = element.parent()
    coefficients = parent.framing_coefficients(element)
    zero = parent.base_ring().zero()
    return tuple(
        coefficients.get(label, zero)
        for label in parent.module_generating_set()
    )


def _module_matrix(morphism):
    r"""Return the finite-free underlying module Mor element for computation."""
    linear = morphism.domain().module_category().Mor(
        morphism.domain(), morphism.codomain()
    )(morphism)
    from dzack_research.preamble.categories.modules.pure.modules import MatrixSpaces

    assert linear.parent() in MatrixSpaces(linear.parent().base_ring()), (
        "matrix computation requires finite framed-free module endpoints"
    )
    return linear


def _binary_form_from_gram(gram):
    r"""Return the integral binary quadratic form ``x^T gram x``."""
    return BinaryQF(
        SageZZ(gram[0, 0]),
        SageZZ(2 * gram[0, 1]),
        SageZZ(gram[1, 1]),
    )


def _proper_reduced_binary_equivalence_matrix(source, target):
    r"""Return ``M in SL_2(ZZ)`` with ``source * M = target``, or ``None``.

    Both forms are reduced indefinite forms of the same non-square
    discriminant.  Sage supplies their proper reduced cycle.  Consecutive
    forms differ alternately by a ``_Rho`` step and its conjugate by
    ``diag(1,-1)``.  Their right-action matrices are respectively
    ``[[0,-1],[1,s]]`` and ``[[0,1],[-1,s]]``.  Recovering ``s`` from the two
    consecutive exact forms avoids reproducing the reduction algorithm.
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
                "a non-square reduced indefinite binary form has zero c-coefficient"
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
            if current.matrix_action_right(step) == following:
                candidates.append(step)
        if not candidates:
            raise ArithmeticError(
                "the proper binary cycle step did not determine a unimodular transformation"
            )
        step = candidates[0]
        transformation = transformation * step
    if source.matrix_action_right(transformation) != target:
        raise ArithmeticError("the reconstructed proper binary equivalence is incorrect")
    return transformation


def _rho_step_matrix(current, following):
    r"""Return the exact ``SL_2(ZZ)`` matrix carrying ``current`` to ``following=current._Rho()``."""
    denominator = SageZZ(2) * SageZZ(current[2])
    if denominator == 0:
        raise ArithmeticError("a Rho step from c=0 is undefined")
    numerator = SageZZ(following[1]) + SageZZ(current[1])
    step_parameter = numerator // denominator
    if denominator * step_parameter != numerator:
        raise ArithmeticError("the Rho step parameter is not integral")
    step = engine_matrix(
        SageZZ,
        ((0, -1), (1, step_parameter)),
    )
    if current.matrix_action_right(step) != following:
        raise ArithmeticError("the reconstructed Rho matrix gives the wrong reduced form")
    return step


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
    if form.matrix_action_right(transformation) != current:
        raise ArithmeticError("the split binary reduction matrix gives the wrong form")
    return current, transformation


def _proper_split_binary_equivalence_matrix(source, target):
    r"""Return ``M in SL_2(ZZ)`` with ``source * M = target`` for split indefinite forms."""
    source_reduced, source_reduction = _split_binary_reduction_to_zero_c(source)
    target_reduced, target_reduction = _split_binary_reduction_to_zero_c(target)
    if source_reduced[1] != target_reduced[1]:
        return None
    b = SageZZ(source_reduced[1])
    if b == 0:
        raise ArithmeticError("a split indefinite reduced form with c=0 has nonzero b")
    difference = SageZZ(target_reduced[0]) - SageZZ(source_reduced[0])
    shear_parameter = difference // b
    if b * shear_parameter != difference:
        return None
    shear = engine_matrix(
        SageZZ,
        ((1, 0), (shear_parameter, 1)),
    )
    if source_reduced.matrix_action_right(shear) != target_reduced:
        raise ArithmeticError("the split binary shear gives the wrong reduced form")
    transformation = source_reduction * shear * target_reduction.inverse()
    if source.matrix_action_right(transformation) != target:
        raise ArithmeticError("the split binary proper equivalence matrix is incorrect")
    return transformation


def _binary_indefinite_isometry_matrix(domain_gram, codomain_gram):
    r"""Return a binary indefinite isometry matrix, ``False``, or ``Unknown``.

    A returned matrix ``P`` satisfies ``P^T codomain_gram P = domain_gram``.
    The non-square-discriminant classification is complete by binary reduction
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
            twisted_codomain = codomain_form.matrix_action_right(improper_twist)
            proper_after_twist = _proper_split_binary_equivalence_matrix(
                twisted_codomain,
                domain_form,
            )
            if proper_after_twist is None:
                return False
            transformation = improper_twist * proper_after_twist
        if codomain_form.matrix_action_right(transformation) != domain_form:
            raise ArithmeticError("the split binary equivalence matrix does not preserve the lattice form")
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
        swapped = codomain_reduced.matrix_action_right(swap)
        proper_after_swap = _proper_reduced_binary_equivalence_matrix(
            swapped,
            domain_reduced,
        )
        if proper_after_swap is None:
            return False
        reduced_transport = swap * proper_after_swap
    transformation = (
        codomain_reduction
        * reduced_transport
        * domain_reduction.inverse()
    )
    if transformation.base_ring() is not SageZZ:
        transformation = transformation.change_ring(SageZZ)
    if codomain_form.matrix_action_right(transformation) != domain_form:
        raise ArithmeticError("the binary equivalence matrix does not preserve the lattice form")
    return transformation


def _tensor_view(morphism):

    return tensor.from_morphism(morphism)


def _labelled_generator_images(domain, images):
    r"""Read the keys of a generator-image mapping as labels of ``domain``'s framing.

    Lattice framings may use formal symbols even though ``module_generator(i)``
    deliberately accepts the integer position ``i``.  A key that is not a
    label is that position in the framing's enumeration, so an explicit image
    mapping keeps the positional spelling before the generic module-morphism
    layer sees the actual labels.
    """
    labels = domain.module_generating_set()
    return {
        (labels(key) if key in labels else labels[int(key)]): value
        for key, value in images.items()
    }


class LatticeMorphism(ModuleMorphism):
    r"""A module morphism preserving the lattice form."""

    def __init__(self, parent, images, *, elementwise=False) -> None:
        ModuleMorphism.__init__(self, parent, images, elementwise=elementwise)
        if self.linearity_decision() is not True:
            raise ValueError("a lattice morphism requires an established underlying linear map")
        domain = self.domain()
        codomain = self.codomain()
        if domain.module_rank().is_finite() and codomain.module_rank().is_finite():
            pulled_back = codomain.gram_tensor().pullback(self)
            if not pulled_back.is_equal_tensor(domain.gram_tensor()):
                raise ValueError("the stated module morphism does not preserve the lattice form")

    def __mul__(self, other):
        if not isinstance(other, LatticeMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        return source.Mor(self.codomain())(
            lambda label: self(other(source.module_generator(label)))
        )



class LatticeEmbedding(LatticeMorphism):
    r"""A form-preserving monomorphism of lattices."""

    def _injectivity_derivation(self):
        return None

    def __init__(self, parent, images, *, elementwise=False) -> None:
        LatticeMorphism.__init__(self, parent, images, elementwise=elementwise)
        decision = self._injectivity_derivation()
        if decision is None:
            try:
                decision = ModuleMorphism.is_injective(self)
            except (AssertionError, AttributeError, TypeError, ValueError):
                decision = Unknown
        if decision is False:
            raise ValueError("a lattice embedding must be injective")
        if decision is not True:
            raise ValueError("injectivity is not established for this lattice embedding")

    def is_injective(self) -> bool:
        return True


class _TransportedLatticeEmbedding(LatticeEmbedding):
    r"""A represented module embedding read in the corresponding lattice Mono."""

    def __init__(self, parent, embedding) -> None:
        self._underlying_module_embedding = embedding
        source = parent.domain()
        super().__init__(
            parent,
            lambda label: embedding(source.module_generator(label)),
        )

    def _injectivity_derivation(self):
        return True

    def factor_through(self, target_embedding):
        r"""Factor this lattice embedding through a module embedding when possible."""
        factor = self.factor_through_or_none(target_embedding)
        if factor is None:
            raise ValueError("the first subobject is not contained in the second")
        return factor

    def factor_through_or_none(self, target_embedding):
        r"""Return the module factor through target_embedding, or None."""
        if target_embedding.codomain() is not self.codomain():
            raise ValueError("subobject factorization requires one common codomain")
        source = self.domain()
        target = target_embedding.domain()
        images = {}
        for label in source.module_generating_set():
            image = self(source.module_generator(label))
            if not target_embedding.is_in_image(image):
                return None
            images[label] = target_embedding.lift(image)
        return source.module_category().Mor(source, target)(images)

    def __mul__(self, other):
        if not isinstance(other, LatticeEmbedding):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        return source.Emb(self.codomain())(
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
        from dzack_research.preamble.categories.lattices import IsotropicReductions

        return IsotropicReductions(self.codomain().base_ring())(self)

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
        assert (
            _engine_ring(source.base_ring()) is SageZZ
            and _engine_ring(target.base_ring()) is SageZZ
        ), "discriminant inclusions are currently implemented for integral ZZ-lattices"
        if not (
            source.module_rank().is_finite()
            and target.module_rank().is_finite()
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

        return source_form.Mono(target_form)(images, quadratic=target.is_even())


class LatticeIsometry(LatticeEmbedding):
    r"""An invertible lattice morphism."""

    def __init__(self, parent, images) -> None:
        LatticeEmbedding.__init__(self, parent, images)
        if self.domain().module_rank().is_finite() and self.codomain().module_rank().is_finite() and not ModuleMorphism.is_surjective(self):
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
        return hash(
            (
                id(self.domain()),
                id(self.codomain()),
                _tensor_view(self),
            )
        )

    def determinant(self):
        r"""Return the determinant of this automorphism/isometry tensor."""
        if self.domain().module_rank() != self.codomain().module_rank():
            raise ValueError("determinant is defined here for equal-rank isometries")
        return _module_matrix(self).determinant()

    def __mul__(self, other):
        if isinstance(other, LatticeIsometry) and other.codomain() is self.domain():
            if self.domain() is self.codomain() and other.parent() is self.parent():
                return self.parent().compose(self, other)
            source = other.domain()
            return source.Isom(self.codomain())(
                lambda label: self(other(source.module_generator(label)))
            )
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
            raise ValueError("invariants are defined here for a lattice automorphism")
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
            raise ValueError("a primitive extension is cut out by a lattice automorphism")
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
            raise ValueError("a cyclotomic summand is cut out by a lattice automorphism")
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

        evaluated = lattice.module_category().Mor(lattice, lattice)(
            {label: image(label) for label in lattice.module_generating_set()}
        )
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
            raise ValueError("equivariant isometry compares two lattice automorphisms")
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
        assert empty is not Unknown, (
            "equivariant-isometry search in the indefinite regime requires the underlying isometry Mor to be decided exactly"
        )
        witness = mor.an_element()
        assert witness * self == other * witness, (
            "the represented indefinite equivariant-isometry path requires the selected underlying isometry witness to intertwine the equipped actions; no exhaustive indefinite conjugacy classifier is selected"
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
            raise ValueError("an equivariant flag family belongs to one lattice automorphism")
        return _equivariant_finite_orbit_decomposition(
            self,
            flags,
            _transport_equivariant_flag,
            _same_equivariant_flag,
        )

    @cached_method
    def _discriminant_forward_morphism(self):
        r"""Return the induced module map on discriminant groups."""
        source = self.domain().discriminant_group()
        target = self.codomain().discriminant_group()
        target_dual = target.projection().domain()
        target_dual_generators = target_dual.module_generators()
        dual_map = _module_matrix(self).inverse().transpose()
        images = {}
        for source_position, label in enumerate(source.module_generating_set()):
            dual_image = sum(
                (
                    target_dual.scalar_multiple(
                        dual_map[target_position, source_position],
                        target_dual_generators[target_position],
                    )
                    for target_position in range(dual_map.parent().nrows())
                    if dual_map[target_position, source_position]
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
            raise ValueError("a discriminant automorphism requires a lattice automorphism")
        form = self.domain().discriminant_group()
        return form.orthogonal_group().from_morphism(
            self._discriminant_forward_morphism()
        )

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
            raise ValueError("a cyclic isometry subgroup requires a lattice automorphism")

        return CyclicGroups()(self)

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
        assert _engine_ring(lattice.base_ring()) is SageZZ, (
            "the current exact spinor-norm seam is for integral ZZ-lattices"
        )
        if not lattice.module_rank().is_finite() or not lattice.is_nondegenerate():
            raise ValueError("the real spinor norm requires a finite nondegenerate lattice")

        ring = lattice.base_ring()
        if lattice.is_positive_definite():
            return self.determinant()
        if lattice.is_negative_definite():
            return ring.one()
        backend_sign = SageZZ(
            lattice_engines._rational_spinor_norm_sign(
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
        vector = lattice_engines._rational_positive_vector(gram)
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
        assert _engine_ring(lattice.base_ring()) is SageZZ, (
            "the centralizer discriminant image is currently implemented for integral ZZ-lattices"
        )
        if not lattice.is_even():
            raise ValueError(
                "the hermitian Miranda--Morrison centralizer-image computation requires an even lattice"
            )
        if not lattice.module_rank().is_finite() or not lattice.is_nondegenerate():
            raise ValueError(
                "the centralizer discriminant image requires a finite nondegenerate lattice"
            )


        engine_generators, expected_order, invariant_rank, coinvariant_rank = (
            lattice_engines._centralizer_discriminant_image(
                lattice.gram_tensor(),
                _tensor_view(self),
            )
        )
        if self.invariant_lattice().module_rank() != invariant_rank:
            raise ArithmeticError(
                "OSCAR's invariant-lattice rank disagrees with the owned invariant lattice"
            )
        if self.formed_coinvariants().module_rank() != coinvariant_rank:
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


class LatticeMor(CategoricalMor):
    Element = LatticeMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        domain.base_ring()
        lattices = domain.lattice_category()
        if domain not in lattices or codomain not in lattices:
            raise TypeError("a lattice Mor has lattices as its domain and codomain")
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        if isinstance(images, ModuleMorphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the module morphism has the wrong lattice endpoints")
            if images.parent() is self:
                return images
            if images.linearity_decision() is not True:
                raise ValueError("a lattice morphism requires an established underlying linear map")
            return self.elementwise(lambda element: images(element))
        if isinstance(images, Morphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong lattice endpoints")
            return self.elementwise(lambda element: images(element))
        if isinstance(images, dict):
            images = _labelled_generator_images(self.domain(), images)
        return self.element_class(self, images)

    def elementwise(self, function):
        if not callable(function):
            raise TypeError("an elementwise lattice map must be callable")
        source = self.domain()
        return self.element_class(
            self,
            lambda label: function(source.module_generator(label)),
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a lattice endomorphism Mor")
        return self.elementwise(lambda element: element)

    def _repr_(self):
        return f"LatticeMor({self.domain()}, {self.codomain()})"


class LatticeEmbeddingMor(CategoricalMor):
    Element = LatticeEmbedding

    def __init__(self, mor_family, domain, codomain, *, category=None) -> None:
        lattices = domain.lattice_category()
        if domain not in lattices or codomain not in lattices:
            raise TypeError("a lattice embedding Mor has lattice endpoints")
        CategoricalMor.__init__(
            self,
            mor_family,
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
            return _TransportedLatticeEmbedding(self, images)
        if isinstance(images, ModuleMorphism):
            if (
                images.domain() is not self.domain()
                or images.codomain() is not self.codomain()
            ):
                raise ValueError("the module morphism has the wrong lattice endpoints")
            if images.parent() is self:
                return images
            if images.linearity_decision() is not True:
                raise ValueError("a lattice embedding requires an established underlying linear map")
            source = self.domain()
            return self.element_class(
                self,
                lambda label: images(source.module_generator(label)),
            )
        if isinstance(images, Morphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong lattice-embedding endpoints")
            return self.elementwise(lambda element: images(element))
        if isinstance(images, dict):
            images = _labelled_generator_images(self.domain(), images)
        return self.element_class(self, images)

    def elementwise(self, function):
        if not callable(function):
            raise TypeError("an elementwise lattice embedding must be callable")
        source = self.domain()
        return self.element_class(
            self,
            lambda label: function(source.module_generator(label)),
        )

    def super_categories(self):
        packet = self.base_category().category_packet()
        source = self.domain()
        target = self.codomain()
        inherited = [
            superpacket.Monos().Of(source, target)
            for superpacket in packet.super_packets()
            if source in superpacket.C() and target in superpacket.C()
        ]
        return [packet.Mors().Of(source, target), *inherited]

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"

    def _codomain_is_even_unimodular_indefinite(self) -> bool:
        target = self.codomain()
        if not target.module_rank().is_finite() or not target.is_nondegenerate():
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
        if not engine_capabilities.is_available("lattice.target_primitive_embedding"):
            return None
        return lattice_engines._target_primitive_embedding(
            source.gram_tensor(),
            target.gram_tensor(),
        )

    def _target_primitive_embedding(self):
        data = self._target_primitive_embedding_data()
        assert data is not None, (
            "target-specific primitive embeddings require an integral nondegenerate target and the OSCAR embedding provider"
        )
        if data is False:
            raise ValueError("the primitive embedding Mor is empty")
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
        embedding = self(
            tuple(
                composed(source.module_generator(label))
                for label in source.module_generating_set()
            )
        )
        if not embedding.is_primitive():
            raise ArithmeticError("a reconstructed OSCAR primitive embedding is not primitive")
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
            raise ValueError("primitive embedding classes are 'sub' or 'emb'")
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
        ), "OSCAR primitive-embedding classes currently require finite nondegenerate integral lattices"
        assert engine_capabilities.is_available("lattice.target_primitive_embedding_classes"), (
            "primitive-embedding class representatives require the OSCAR lattice provider"
        )
        data = lattice_engines._target_primitive_embedding_classes(
            source.gram_tensor(),
            target.gram_tensor(),
            classification,
        )
        assert data is not None, (
            "OSCAR's target-specific primitive-embedding classification is unavailable"
        )
        return finite_ordered_set(
            tuple(self._reconstruct_target_primitive_embedding(record) for record in data)
        )

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
            "embedding enumeration is currently implemented for finite definite targets"
        )
        assert source.module_rank().is_finite(), (
            "embedding enumeration requires a finite-rank source"
        )
        match source.is_nondegenerate():
            case False:
                return
        source_generators = tuple(source.module_generators())
        source_gram = source.gram_tensor()
        pools = tuple(
            tuple(target.vectors_of_square(source_gram[index, index]))
            for index in range(len(source_generators))
        )

        def assign(placed):
            position = len(placed)
            if position == len(source_generators):
                yield self(tuple(placed))
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
        if self.codomain().module_rank().is_finite() and self.codomain().is_definite():
            for _embedding in self:
                return False
            return True
        source = self.domain()
        target = self.codomain()
        if (
            source.module_rank().is_finite()
            and target.module_rank().is_finite()
            and source.module_rank() == target.module_rank()
        ):
            return source.Isom(target).is_empty()
        target_embedding_data = self._target_primitive_embedding_data()
        if target_embedding_data is False:
            return True
        if target_embedding_data is not None:
            return False
        if self._codomain_is_even_unimodular_indefinite():
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
        if self.codomain().module_rank().is_finite() and self.codomain().is_definite():
            for embedding in self:
                return embedding
            raise ValueError("the embedding Mor is empty")
        source = self.domain()
        target = self.codomain()
        if (
            source.module_rank().is_finite()
            and target.module_rank().is_finite()
            and source.module_rank() == target.module_rank()
        ):
            isometry = source.Isom(target).an_element()
            return self(
                tuple(
                    isometry(source.module_generator(label))
                    for label in source.module_generating_set()
                )
            )
        target_embedding_data = self._target_primitive_embedding_data()
        if target_embedding_data is not None:
            return self._target_primitive_embedding()
        if self._codomain_is_even_unimodular_indefinite():
            if self.is_empty():
                raise ValueError("the embedding Mor is empty")
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
        assert False, (
            "a distinguished embedding is constructed into definite targets, equal-rank "
            "targets, targets the OSCAR embedding provider covers, and even unimodular "
            "indefinite targets; this target is none of them"
        )


class LatticeIsometryMor(LatticeEmbeddingMor):
    Element = LatticeIsometry

    def __init__(self, mor_family, domain, codomain) -> None:
        categories = []
        if domain is codomain:
            categories.append(OwnedGroups())
            if (
                _engine_ring(domain.base_ring()) is SageZZ
                and domain.module_rank().is_finite()
                and domain.is_definite()
            ):
                categories.append(OwnedFiniteGroups())
                categories.append(OwnedGroups().Framed())
        LatticeEmbeddingMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
            category=Cat().meet(tuple(categories)) if categories else None,
        )
        if domain is codomain and self in OwnedGroups().Framed():
            self._retain_group_framing(self._computed_group_generators())

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
        if isinstance(images, dict):
            images = _labelled_generator_images(self.domain(), images)
        return self.element_class(self, images)

    def super_categories(self):
        packet = self.base_category().category_packet()
        source = self.domain()
        target = self.codomain()
        inherited = [
            superpacket.Isos().Of(source, target)
            for superpacket in packet.super_packets()
            if source in superpacket.C() and target in superpacket.C()
        ]
        supers = [
            packet.Mors().Of(source, target),
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
            raise ValueError("identity is defined on an automorphism Mor")
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
        cardinality as ``O(M)``.  When emptiness is genuinely undecided, keep
        that three-valued boundary instead of turning it into a cardinal.
        """
        empty = self.is_empty()
        if empty is True:
            return cardinal(0)
        if empty is False:
            return self.acting_group().cardinality()
        return Unknown

    def act(self, automorphism, isometry):
        r"""Postcompose an isometry by a codomain automorphism."""
        if automorphism.parent() is not self.acting_group():
            raise ValueError("the torsor action is by the orthogonal group of the codomain")
        if element_parent(isometry) is not self:
            raise ValueError("the torsor action is on this isometry Mor")
        return self(
            lambda label: automorphism(
                isometry(self.domain().module_generator(label))
            )
        )

    def transporter(self, source, target):
        r"""Return an orthogonal transporter.

        For lattice vectors this is an exact orbit witness ``g(source)=target``.
        For two isometries in ``Isom(L,M)`` it retains the torsor operation
        ``g ∘ source = target``.
        """
        lattice = self.codomain()
        if (
            self.domain() is lattice
            and element_parent(source) is lattice
            and element_parent(target) is lattice
        ):
            return self.vector_equivalence_witness(source, target)
        for candidate in (source, target):
            if element_parent(candidate) is not self:
                raise ValueError("a transporter compares two isometries in this Mor")
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
            tuple(
                generator.discriminant_morphism()
                for generator in self.framing().group_generators()
            )
        )

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
            raise ValueError("a discriminant lift is defined for an automorphism group")
        target = self.domain().discriminant_group().orthogonal_group()
        automorphism = target(automorphism)
        representation = self.discriminant_representation()
        witnesses = self.framing().finite_image_lifts(representation)
        return witnesses.get(automorphism)

    def discriminant_preimage(self, subgroup):
        r"""Return ``rho_L^{-1}(subgroup)`` as a predicate subgroup of ``O(L)``."""
        if self.domain() is not self.codomain():
            raise ValueError("a discriminant preimage is defined for an automorphism group")
        target = self.domain().discriminant_group().orthogonal_group()
        # A subgroup of the finite orthogonal group is a subcategory of it: its
        # declared supercategory is the group it was cut out of.
        if not (subgroup is target or subgroup.is_subcategory(target)):
            raise ValueError("the subgroup must lie in O(A_L)")

        if int(subgroup.cardinality()) == 1:
            form = target.domain()
            identity = form.module_category().Mor(form, form).identity()

            def predicate(automorphism):
                return automorphism._discriminant_forward_morphism() == identity
        else:
            def predicate(automorphism):
                return automorphism.discriminant_morphism() in subgroup
        return self.discriminant_representation().preimage_subgroup(
            subgroup,
            predicate=predicate,
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
            raise ValueError("a group preimage requires a morphism whose domain is this group")
        return morphism.preimage_subgroup(subgroup)

    def kernel(self, morphism):
        r"""Return the kernel subgroup of a represented group morphism."""
        if morphism.domain() is not self:
            raise ValueError("a group kernel requires a morphism whose domain is this group")
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
            "the acted lattice is the common domain and codomain of an automorphism group"
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
                raise ValueError("a sublattice stabilizer requires a subobject of the acted lattice")
            if action == "setwise":
                return self.setwise_stabilizer(embedding)
            if action == "pointwise":
                return self.pointwise_stabilizer(embedding)
            raise ValueError("a sublattice stabilizer action is 'setwise' or 'pointwise'")
        if action != "setwise":
            raise ValueError("the action option applies only to represented sublattices")
        assert target.parent() is lattice, (
            "a point stabilizer in O(L) fixes a vector of L"
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
            "a stabilizer in O(L) is taken of a sublattice of L"
        )
        source = embedding.domain()
        embedded = tuple(
            embedding(generator) for generator in source.module_generators()
        )
        return StabilizerSubgroups(self)(
            source,
            "pointwise",
            lambda automorphism: all(
                automorphism(vector) == vector for vector in embedded
            ),
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
            raise ValueError("an orthogonal group is an automorphism Mor")
        assert _engine_ring(lattice.base_ring()) is SageZZ, (
            "the active orthogonal-group engine currently computes integral ZZ-lattices"
        )
        assert lattice.module_rank().is_finite() and lattice.is_definite(), (
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
        r"""Cross a private row-action matrix into this live isometry Mor."""
        codomain = self.codomain()
        ring = codomain.base_ring()
        generators = tuple(codomain.module_generators())
        len(generators)
        images = []
        for source_position in range(int(self.domain().module_rank())):
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

    def _row_action_matrix(self, automorphism):
        r"""Return the private row-action matrix of one live lattice isometry."""
        if element_parent(automorphism) is not self:
            raise ValueError(
                "the engine crossing takes an automorphism in this orthogonal group"
            )
        # Publicly the linear map acts on columns. Sage matrix groups act on
        # coordinate rows on the right, hence one transpose at this boundary.
        return _engine_matrix(_module_matrix(automorphism)).transpose()

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
        r"""Return exact generators of ``O(L)`` when the backend computes them."""

        lattice = self.domain()
        if not lattice.is_definite():
            backend_generators = engine_capabilities.compute(
                "lattice.indefinite_automorphism_group", _engine_gram_rows(lattice)
            )
            positions = Sets.Δ[len(backend_generators) - 1]
            return FiniteOrderedSets().from_indexed(
                positions,
                lambda position: self._from_backend_row_action(
                    backend_generators[int(position)]
                ),
                name=f"Orthogonal-group generators of {lattice}",
            )
        backend_generators = self._engine_group().gens()
        positions = Sets.Δ[len(backend_generators) - 1]
        return FiniteOrderedSets().from_indexed(
            positions,
            lambda position: self._from_engine(backend_generators[int(position)]),
            name=f"Orthogonal-group generators of {lattice}",
        )

    def _retain_group_framing(self, generators) -> None:
        r"""Retain one computed exact generating family as this group's framing."""
        source = Groups.Free(index_set=generators)
        generator_morphism = Sets().Mor(generators, self)(lambda generator: generator)
        _fix_selected_framing(
            self,
            OwnedGroups(),
            source,
            generators,
            generator_morphism,
            lambda: _group_framing_morphism(
                self, source, generators, generator_morphism
            ),
        )

    def framing(self):
        r"""Explicitly select and retain the represented generator framing of ``O(L)``."""
        if self in OwnedGroups().Framed():
            return self
        self._retain_group_framing(self._computed_group_generators())
        return refine(self, OwnedGroups().Framed())

    def structure_description(self):
        r"""Return GAP's descriptive structure label for a finite ``O(L)``.

        The maintained Sage ``GroupOfIsometries`` computation uses GAP internally and
        supplies ``StructureDescription``.  This method is intentionally
        descriptive only: GAP does not promise that the returned string is an
        isomorphism invariant, so no equality or subgroup decision in the
        owned layer depends on it.
        """
        lattice = self.domain()
        assert lattice.is_definite(), (
            "GAP StructureDescription is exposed here for finite definite orthogonal groups"
        )
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
            raise ValueError("vector equivalence is an orthogonal-group operation")
        left = left if element_parent(left) is lattice else lattice(left)
        right = right if element_parent(right) is lattice else lattice(right)
        if left == right:
            return self.one()
        if lattice.q(left) != lattice.q(right):
            return None
        if not lattice.is_definite():
            witness = engine_capabilities.compute(
                "lattice.indefinite_vector_isometry_witness",
                _engine_gram_rows(lattice),
                [int(entry) for entry in _framing_tuple(left)],
                [int(entry) for entry in _framing_tuple(right)],
            )
            if witness is None:
                return None
            result = self._from_backend_row_action(witness)
            if result(left) != right:
                raise ArithmeticError(
                    "the exact indefinite vector-equivalence computation returned a witness with the wrong action"
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
        element = element if element_parent(element) is lattice else lattice(element)
        if not lattice.is_definite():
            isometries = finite_ordered_set(
                tuple(
                    self._from_backend_row_action(engine_isometry)
                    for engine_isometry in engine_capabilities.compute(
                        "lattice.indefinite_vector_stabilizer",
                        _engine_gram_rows(lattice),
                        [int(entry) for entry in _framing_tuple(element)],
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
            return finite_ordered_set(representatives)
        remaining = {
            _framing_tuple(vector): vector
            for vector in lattice.vectors_of_square(square)
        }
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

        return finite_ordered_set(
            tuple(
                _cusp(representative)
                for representative in self.isotropic_orbit_representatives(rank)
            )
        )

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
                    "an isotropic flag term does not determine a unique full-group cusp orbit"
                )
            line_cusp = line_vertices[0]
            plane_cusp = plane_vertices[0]
            line_transporter = line_cusp.transporter_witness(line)
            plane_transporter = plane_cusp.transporter_witness(plane)
            if line_transporter is None or plane_transporter is None:
                raise ArithmeticError(
                    "a flag term lies in a cusp with no transporter witness"
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
        assert all(incidence.lattice() is lattice for incidence in incidences), (
            "a full-group quotient-building incidence changed its ambient lattice"
        )
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
            raise ValueError("isometry composition requires matching middle objects")
        return first.domain().Isom(second.codomain())(lambda label: second(first(first.domain().module_generator(label))))

    def is_empty(self):
        r"""Decide emptiness through exact obstructions and proved classifiers.

        Passing an obstruction never proves isometry by itself.  Definite
        survivors are decided by Sage's exact equivalence engine.  Indefinite
        survivors are declared nonempty only in theorem-backed uniqueness
        regimes (Nikulin's indefinite even 2-elementary classification, or
        Eichler when the common genus has one improper spinor genus).  All
        remaining indefinite cases retain Sage's three-valued ``Unknown``.
        """
        return self._isometry_decision()[0]

    def _isometry_from_column_matrix(self, transformation):
        r"""The isometry whose \(j\)-th generator image has the \(j\)-th column of ``transformation`` as coordinates."""
        codomain = self.codomain()
        codomain_generators = tuple(codomain.module_generators())
        ring = codomain.base_ring()
        return self(
            tuple(
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
        )

    @cached_method
    def _isometry_decision(self):
        r"""The decision of this isometry Mor object, with the witness that decided it.

        Private computation record of :meth:`is_empty` and :meth:`an_element`:
        the triple of the emptiness answer (``True``, ``False`` or
        ``Unknown``), an explicit isometry when the deciding computation
        exhibits one (else ``None``), and the theorem that proves
        nonemptiness without a witness (else ``None``).
        """
        domain = self.domain()
        codomain = self.codomain()
        if domain is codomain:
            return (False, self.identity(), None)
        if not domain.module_rank().is_finite() or not codomain.module_rank().is_finite():
            return (Unknown, None, None)
        if domain.module_rank() != codomain.module_rank():
            return (True, None, None)
        if domain.signature_pair() != codomain.signature_pair():
            return (True, None, None)
        if _engine_ring(domain.base_ring()) is not SageZZ or _engine_ring(codomain.base_ring()) is not SageZZ:
            return (Unknown, None, None)

        domain_gram = _engine_component_matrix(domain.gram_tensor()).change_ring(SageZZ)
        codomain_gram = _engine_component_matrix(codomain.gram_tensor()).change_ring(SageZZ)
        if domain_gram == codomain_gram:
            return (False, self._isometry_from_column_matrix(domain_gram.parent().one()), None)
        rank = domain.module_rank()
        if int(rank.finite_value()) <= 1:
            return (True, None, None)
        if domain.is_nondegenerate() != codomain.is_nondegenerate():
            return (True, None, None)
        if not domain.is_nondegenerate():
            return (Unknown, None, None)
        if domain.is_even() != codomain.is_even():
            return (True, None, None)
        if domain.discriminant() != codomain.discriminant():
            return (True, None, None)
        if (
            domain.discriminant_module().invariant_factors()
            != codomain.discriminant_module().invariant_factors()
        ):
            return (True, None, None)

        from sage.quadratic_forms.genera.genus import Genus as SageGenus
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
            if LocalGenusSymbol(domain_engine, prime) != LocalGenusSymbol(
                codomain_engine, prime
            ):
                return (True, None, None)

        domain_discriminant = domain.discriminant_group()
        codomain_discriminant = codomain.discriminant_group()
        if not domain_discriminant.is_isomorphic(codomain_discriminant):
            return (True, None, None)

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
                return (True, None, None)
            if transformation.transpose() * codomain_gram * transformation != domain_gram:
                raise ArithmeticError("the exact definite-isometry computation returned an invalid witness")
            return (False, self._isometry_from_column_matrix(transformation), None)

        if int(domain.module_rank()) == 2:
            binary_witness = _binary_indefinite_isometry_matrix(
                domain_gram,
                codomain_gram,
            )
            if binary_witness is False:
                return (True, None, None)
            if binary_witness is not Unknown:
                return (False, self._isometry_from_column_matrix(binary_witness), None)

        # The absence of this program is not fatal here: the classification
        # theorems below still decide some pairs, so the capability is asked
        # for first rather than demanded.
        if engine_capabilities.is_available("lattice.indefinite_isometry_witness"):
            witness_rows = engine_capabilities.compute(
                "lattice.indefinite_isometry_witness",
                _engine_gram_rows(codomain),
                _engine_gram_rows(domain),
            )
            if witness_rows is None:
                return (True, None, None)
            return (False, self._from_backend_row_action(witness_rows), None)

        if engine_capabilities.is_available("lattice.oscar_isometry_witness"):
            witness_rows = lattice_engines._integral_isometry_witness(
                domain.gram_tensor(),
                codomain.gram_tensor(),
            )
            if witness_rows is None:
                return (True, None, None)
            witness = self._from_backend_row_action(witness_rows)
            if any(
                witness(domain.module_generator(label)).parent() is not codomain
                for label in domain.module_generating_set()
            ):
                raise ArithmeticError("the OSCAR isometry witness has the wrong codomain")
            return (False, witness, None)

        if (
            domain.is_even()
            and domain.is_p_elementary(2)
            and codomain.is_p_elementary(2)
            and domain.two_elementary_invariants()
            == codomain.two_elementary_invariants()
        ):
            return (
                False,
                None,
                "Nikulin's classification of indefinite even 2-elementary lattices",
            )

        rank = domain.module_rank()
        if rank >= rank.parent()(3):
            spinor_generators = SageGenus(domain_engine).spinor_generators(proper=False)
            if not spinor_generators:
                return (
                    False,
                    None,
                    "Eichler's theorem and uniqueness of the improper spinor genus",
                )
        return (Unknown, None, None)

    def an_element(self):
        r"""Return an explicit isometry when the exact decision exhibits one."""
        empty, witness, reason = self._isometry_decision()
        assert empty is not Unknown, "no exact isometry witness construction is available for this pair"
        if empty:
            raise ValueError("the isometry Mor is empty")
        assert witness is not None, (
            f"{reason} proves this isometry Mor is nonempty, but no explicit witness construction is available"
        )
        return witness

    def _repr_(self):
        if self.domain() is self.codomain():
            return f"Orthogonal group O({self.domain()})"
        return f"Isom({self.domain()}, {self.codomain()})"


@cached_function(key=lambda domain, codomain: (id(domain), id(codomain)))
def _lattice_mor(domain, codomain) -> LatticeMor:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError("lattice morphisms require one common base ring")
    return domain.lattice_category().Mor(domain, codomain)


@cached_function(key=lambda domain, codomain: (id(domain), id(codomain)))
def _lattice_embedding_mor(domain, codomain) -> LatticeEmbeddingMor:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError("lattice embeddings require one common base ring")
    return domain.lattice_category().Mono(domain, codomain)


@cached_function(key=lambda domain, codomain: (id(domain), id(codomain)))
def _lattice_isometry_mor(domain, codomain) -> LatticeIsometryMor:
    ring = domain.base_ring()
    if codomain.base_ring() != ring:
        raise ValueError("lattice isometries require one common base ring")
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
