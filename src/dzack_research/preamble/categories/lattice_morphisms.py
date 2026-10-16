r"""Form-preserving morphisms, embeddings, and isometries of lattices."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.groups.matrix_gps.finitely_generated import MatrixGroup
from sage.categories.morphism import Morphism
from sage.matrix.constructor import matrix as engine_matrix
from sage.misc.cachefunc import cached_function, cached_method
from sage.quadratic_forms.binary_qf import BinaryQF
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import parent as element_parent

import dzack_research.preamble.categories.lattice_engines as lattice_engines
from dzack_research.preamble.categories.abstract_categories.cat import Cat
from sage.misc.lazy_attribute import lazy_attribute

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    CoreMor,
    CosliceCategory,
    _CoreCategory,
)
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalIsomorphism,
    CategoricalMor,
    _distinct_supercategories,
    _category_accepts_morphism,
)
from dzack_research.preamble.categories.group.cyclic_subgroups import CyclicGroups
from dzack_research.preamble.categories.group.groups import (
    OwnedFiniteGroups,
    OwnedGroups,
)
from dzack_research.preamble.categories.group.predicate_subgroups import (
    IntersectionSubgroups,
    PredicateSubgroups,
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
from dzack_research.preamble.categories.abstract_categories.mor_foundation import (
    _refuse_foreign_arrow,
)
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FormedModuleMorphism,
    _represented_value_module,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleAutomorphismMethods,
    ModuleMorphism,
    ModuleMorphismMethods,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules, ModulesOverIntegralDomains, _engine_matrix
from dzack_research.preamble.categories.rings.ring_foundation import (
    _own_ring,
    _owned_engine_element,
    _owned_integers,
    _owned_rationals,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring
from dzack_research.preamble.categories.sets.cardinals import aleph, cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    OrderedEnumeratedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import NN, Sets
from dzack_research.preamble.logic import AtomicProposition
from dzack_research.preamble.validation import validator
from dzack_research.preamble.tensors.tensor import (
    _engine_binary_form_pullback,
    _engine_column_matrix_from_row_action,
    _engine_component_matrix,
    _engine_row_action_matrix,
    tensor,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level

if TYPE_CHECKING:
    from dzack_research.preamble.categories.lattices import Lattices


def _pointed_marking(lattice, vector):
    r"""Return the coslice category and marked lattice ``<q(v)> -> L``."""
    from dzack_research.preamble.categories.lattices import Lattices

    lattices = Lattices(lattice.base_ring())
    source = lattices([[lattice.q(vector)]])
    category = lattices.CosliceUnder(source)
    arrow = source.Mor(lattice)(lambda _label: vector)
    return category, category.object(arrow)


def _primitive_pointed_classes(lattice, square):
    r"""Return primitive vector classes of square ``square`` through the frozen marked API."""
    from dzack_research.preamble.categories.lattices import Lattices
    from sage_indefinite_port.indefinite.marked_lattices import (
        primitive_marking_classes,
    )

    lattices = Lattices(lattice.base_ring())
    source = lattices([[square]])
    category = lattices.CosliceUnder(source)
    classes = primitive_marking_classes(category, source, lattice)
    label = next(iter(source.module_generating_set()))
    return tuple(marked.arrow()(source.module_generator(label)) for marked in classes)


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

    def _factor_from_generator_preimages(self, target_embedding, preimages):
        r"""Factor a form-preserving map through a lattice embedding.

        Injectivity of the subobject map and preservation of the same form
        give the factor's form equation; a monic source map gives a monic
        factor.  Its selected generator images are computed by the module
        factorization owner, without reconstructing an existing arrow.
        """
        base = self.parent().base_category()
        assert _category_accepts_morphism(base, target_embedding.domain(), self.codomain(), target_embedding), (
            f"factorization in {base} needs a lattice subobject map of {base}"
        )
        return self.domain().Mor(target_embedding.domain())(preimages)

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

    def _factor_from_generator_preimages(self, target_embedding, preimages):
        base = self.domain().lattice_category()
        assert _category_accepts_morphism(base, target_embedding.domain(), self.codomain(), target_embedding), (
            f"factorization of a lattice embedding needs a lattice subobject map of {base}"
        )
        return self.domain().Emb(target_embedding.domain())(preimages)

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


class LatticeIsometryMethods:
    r"""An invertible lattice morphism."""

    def __init__(self, parent, images, *, inverse_computation=None) -> None:
        self._isometry_inverse_computation = inverse_computation
        match images:
            # A module isomorphism of the underlying modules: an inverse pair,
            # or an element of Aut_R(M) = Core(Mod_R)(M, M) when L = M.
            case CategoricalIsomorphism() | ModuleAutomorphismMethods():
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

    def extension_across(self, source_vector, target_vector, *, source_inclusion=None, target_inclusion=None):
        r"""Extend this perpendicular isometry over the common fraction field.

        The endpoints must admit specified codimension-one embeddings into
        the vectors' ambient lattices. The vectors must have the same nonzero
        square. Their lines and perpendicular spaces then give orthogonal
        direct sums, so the extension is unique. No signature hypothesis is
        needed. The result retains the scalar-extended ambient endpoints.

        The defining splitting is
        ``LeanCategories.Lattices.Valued.isCompl_span_anisotropicComplement``
        in ``Lattices/Valued/OrthogonalSplitting.lean``.

        EXAMPLES::

            sage: L = Lattices(ZZ)([[2, 0, 0], [0, 2, 0], [0, 0, -2]])
            sage: v = L.basis_vector(0)
            sage: P = L.subobject_on((v,)).orthogonal_complement()
            sage: a = P.Isom(P)(lambda s: -P.module_generator(s))
            sage: g = a.extension_across(v, v)
            sage: g.is_integral_on(L) and L.integral_isometry(g)(v) == v
            True
            sage: L.integral_isometry(g)(L.basis_vector(1)) == -L.basis_vector(1)
            True
            sage: a.extension_across(v, v, source_inclusion=P.inclusion(), target_inclusion=P.inclusion()).is_integral_on(L)
            True
            sage: w = L.basis_vector(1)
            sage: Q = L.subobject_on((w,)).orthogonal_complement()
            sage: P is not Q
            True
            sage: between = P.Isom(Q)(lambda s: Q.module_generator(s))
            sage: between.extension_across(v, w, source_inclusion=P.inclusion(), target_inclusion=Q.inclusion()).is_integral_on(L)
            True
            sage: between.extension_across(v, w, source_inclusion=Q.inclusion(), target_inclusion=P.inclusion())
            Traceback (most recent call last):
            ...
            ValueError: the perpendicular embedding must start at the corresponding isometry endpoint
            sage: neg = P.Isom(P)(lambda s: -P.module_generator(s))
            sage: j = P.inclusion()
            sage: twisted = j * neg
            sage: twisted != j
            True
            sage: g = P.Isom(P).identity().extension_across(v, v, source_inclusion=twisted, target_inclusion=j)
            sage: h = L.integral_isometry(g)
            sage: all(h(twisted(x)) == j(x) for x in P.module_generators())
            True
            sage: a.extension_across(L.zero(), L.zero())
            Traceback (most recent call last):
            ...
            ValueError: orthogonal extension requires equal nonzero vector squares
        """
        source = source_vector.parent()
        target = target_vector.parent()
        ring = source.base_ring()
        if target.base_ring() is not ring:
            raise ValueError("orthogonal extension requires a common base ring")
        if not source_vector.q() or source_vector.q() != target_vector.q():
            raise ValueError("orthogonal extension requires equal nonzero vector squares")
        if source_inclusion is None:
            source_inclusion = self.domain().inclusion()
        if target_inclusion is None:
            target_inclusion = self.codomain().inclusion()
        for inclusion, endpoint, ambient, vector in (
            (source_inclusion, self.domain(), source, source_vector),
            (target_inclusion, self.codomain(), target, target_vector),
        ):
            if inclusion.codomain() is not ambient:
                raise ValueError("the perpendicular inclusion has the wrong ambient lattice")
            if inclusion.domain() is not endpoint:
                raise ValueError("the perpendicular embedding must start at the corresponding isometry endpoint")
            if inclusion.domain().module_rank() + 1 != ambient.module_rank():
                raise ValueError("the perpendicular subobject must have codimension one")
            if any(ambient.b(vector, inclusion(x)) for x in inclusion.domain().module_generators()):
                raise ValueError("the subobject is not perpendicular to the selected vector")
        fraction_map = ring.fraction_field_map()
        rational_source = source.base_change(fraction_map)
        rational_target = target.base_change(fraction_map)
        source_embedding = source_inclusion.base_change(fraction_map)
        target_embedding = target_inclusion.base_change(fraction_map)
        restriction = self.base_change(fraction_map)
        source_coordinates = source_vector.to_vector()
        target_coordinates = target_vector.to_vector()
        v = rational_source.linear_combination(
            {label: fraction_map(source_coordinates(label)) for label in source_coordinates.support().domain()}
        )
        w = rational_target.linear_combination(
            {label: fraction_map(target_coordinates(label)) for label in target_coordinates.support().domain()}
        )
        source_line = rational_source.subobject_on((v,))
        target_line = rational_target.subobject_on((w,))
        source_splitting = rational_source.orthogonal_decomposition(
            (source_line.inclusion(), source_embedding)
        )
        target_splitting = rational_target.orthogonal_decomposition(
            (target_line.inclusion(), target_embedding)
        )

        def line_image(label):
            x = source_line.inclusion()(source_line.module_generator(label))
            coefficient = rational_source.b(x, v) / v.q()
            return target_line.inclusion().lift(rational_target.scalar_multiple(coefficient, w))

        line_isometry = source_line.Isom(target_line)(line_image)
        source_sum = source_splitting.codomain()
        target_sum = target_splitting.codomain()
        assembled = source_sum.from_coproduct_cocone((
            target_sum.injection(0) * line_isometry,
            target_sum.injection(1) * restriction,
        ))
        sum_isometry = source_sum.Isom(target_sum)(
            lambda label: assembled(source_sum.module_generator(label))
        )
        return target_splitting.inverse() * sum_isometry * source_splitting

    def is_integral_on(self, source, target=None):
        r"""Decide whether this rational map sends ``source`` into ``target``.

        For an endomorphism, ``target`` defaults to ``source``. Otherwise
        the target integral structure must be supplied: a rational vector
        space alone does not specify an integral lattice.

        EXAMPLES::

            sage: L = Lattices(ZZ)("U")
            sage: V = L.vector_space()
            sage: labels = tuple(V.module_generating_set())
            sage: e, f = V.module_generator(labels[0]), V.module_generator(labels[1])
            sage: phi = V.Isom(V)(lambda j: V.scalar_multiple(QQ(2), e) if j == labels[0] else V.scalar_multiple(QQ(1)/QQ(2), f))
            sage: phi.is_integral_on(L)
            False
            sage: phi.integral_restriction(L, L) is None
            True
        """
        if target is None:
            target = source
        ring = source.base_ring()
        fraction_map = ring.fraction_field_map()
        if target.base_ring() is not ring:
            raise ValueError("integrality requires a common integral scalar ring")
        if self.domain() is not source.base_change(fraction_map) or self.codomain() is not target.base_change(fraction_map):
            raise ValueError("integrality requires the source and target integral structures of this rational map")
        restrict = Modules(fraction_map.codomain()).restriction_of_scalars(fraction_map)
        return (restrict(self) * ModulesOverIntegralDomains(ring)(source).generic_fibre_map()).factor_through_or_none(
            ModulesOverIntegralDomains(ring)(target).generic_fibre_map()
        ) is not None

    @cached_method
    def witt_extension_locus(self, source_inclusion, target_inclusion):
        r"""The full locus of ambient isometries extending this partial isometry."""
        from dzack_research.preamble.categories.sets.set_categories import Sets

        if source_inclusion.domain() is not self.domain() or target_inclusion.domain() is not self.codomain():
            raise ValueError("the inclusions must start at the endpoints of the partial isometry")
        source, target = source_inclusion.codomain(), target_inclusion.codomain()
        maps = Modules(source.base_ring()).Mor(self.domain(), target)
        isometries = source.Isom(target)
        restriction = Sets().Mor(isometries, maps)(
            lambda extension: Modules(source.base_ring()).Mor(source, target)(extension) * source_inclusion
        )
        prescribed = Modules(source.base_ring()).Mor(self.codomain(), target)(target_inclusion) * self
        constant = Sets().Mor(isometries, maps)(lambda extension: prescribed)
        return Sets().equalizer_construction(restriction, constant)

    def witt_extension(self, source_inclusion, target_inclusion):
        r"""Extend a codimension-one partial rational isometry when compatible with radicals.

        The affine pairing fibre supplies the image of a complementary vector.
        Its norm equation is linear for an isotropic normal, and quadratic
        otherwise. A complementary ambient radical vector is handled as a
        radical vector. This is the codimension-one Witt construction; the
        isotropic norm correction is the one in sage-indefinite-port at
        709f81a, ``CodimensionOneIsotropicExtension.rational_extension``.
        The extension locus retains the square with the two given inclusions.

        EXAMPLES::

            sage: L = Lattices(ZZ)("U") + Lattices(ZZ)([[2]])
            sage: V = L.base_change(ZZ.fraction_field_map())
            sage: e, f, a = tuple(V.module_generators())
            sage: H = V.subobject_on((e, a))
            sage: i = H.inclusion()
            sage: u, v = tuple(H.module_generators())
            sage: partial = H.Isom(H)((u, -v))
            sage: extension = partial.witt_extension(i, i)
            sage: all(extension(i(x)) == i(partial(x)) for x in H.module_generators())
            True
            sage: extension.inverse() * extension == V.Isom(V).identity()
            True

            sage: W = Lattices(QQ)([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
            sage: e, f, r = tuple(W.module_generators())
            sage: H = W.subobject_on((e + f, r))
            sage: u, v = tuple(H.module_generators())
            sage: swap = H.Isom(H)((v, u))
            sage: swap.witt_extension(H.inclusion(), H.inclusion())
            Traceback (most recent call last):
            ...
            ValueError: the partial isometry does not identify the ambient radical intersections
        """
        locus = self.witt_extension_locus(source_inclusion, target_inclusion)
        source, target = source_inclusion.codomain(), target_inclusion.codomain()
        field = source.base_ring()
        if field is not _owned_rationals() or target.base_ring() is not field:
            raise TypeError("this codimension-one extension requires rational quadratic spaces")
        for inclusion in (source_inclusion, target_inclusion):
            if inclusion.domain().module_rank() + 1 != inclusion.codomain().module_rank():
                raise ValueError("the specified subspaces must have codimension one")
        source_radical = source.metric_map().kernel()
        target_radical = target.metric_map().kernel()
        if source_radical.module_rank() != target_radical.module_rank():
            raise ValueError("isometric ambient spaces must have radicals of equal dimension")
        for partial, first, second, ambient in (
            (self, source_inclusion, target_inclusion, target),
            (self.inverse(), target_inclusion, source_inclusion, source),
        ):
            intersection = (first.codomain().metric_map() * first).kernel()
            for vector in intersection.module_generators():
                image = second(partial(intersection.inclusion()(vector)))
                if ambient.metric_map()(image) != ambient.metric_map().codomain().zero():
                    raise ValueError("the partial isometry does not identify the ambient radical intersections")

        radical_complements = tuple(
            source_radical.inclusion()(vector)
            for vector in source_radical.module_generators()
            if not source_inclusion.is_in_image(source_radical.inclusion()(vector))
        )
        target_radical_complements = tuple(
            target_radical.inclusion()(vector)
            for vector in target_radical.module_generators()
            if not target_inclusion.is_in_image(target_radical.inclusion()(vector))
        )
        if bool(radical_complements) != bool(target_radical_complements):
            raise ValueError("the specified hyperplanes have incompatible ambient-radical intersections")
        if radical_complements:
            source_vector = radical_complements[0]
            target_vector = target_radical_complements[0]
        else:
            source_vector = next(
                vector for vector in source.module_generators()
                if not source_inclusion.is_in_image(vector)
            )
            scalars = field.regular_module()
            functionals = Modules(field).Mor(self.domain(), scalars)
            pairing = Modules(field).Mor(target, functionals)(
                lambda label: functionals(
                    lambda index: scalars(target.b(
                        target.module_generator(label),
                        target_inclusion(self(self.domain().module_generator(index))),
                    ))
                )
            )
            prescribed = functionals(
                lambda label: scalars(source.b(
                    source_vector, source_inclusion(self.domain().module_generator(label))
                ))
            )
            target_vector = pairing.solution_fibre(prescribed).base_point()
            perpendicular = pairing.kernel()
            normal = next(
                perpendicular.inclusion()(vector)
                for vector in perpendicular.module_generators()
                if not target_radical.inclusion().is_in_image(perpendicular.inclusion()(vector))
            )
            a = target.q(normal)
            b = field(2) * target.b(target_vector, normal)
            c = target.q(target_vector) - source.q(source_vector)
            if a == field.zero():
                if b == field.zero():
                    if c != field.zero():
                        raise ValueError("the complementary norm equation has no solution")
                    parameters = (field.zero(), field.one())
                else:
                    parameters = (-c / b,)
            else:
                discriminant = b * b - field(4) * a * c
                if not discriminant.is_square():
                    raise ValueError("the complementary norm equation has no rational solution")
                root = discriminant.sqrt()
                parameters = ((-b + root) / (field(2) * a), (-b - root) / (field(2) * a))
            candidates = tuple(target_vector + target.scalar_multiple(t, normal) for t in parameters)
            target_vector = next(
                (vector for vector in candidates if not target_inclusion.is_in_image(vector)), None
            )
            if target_vector is None:
                raise ValueError("no norm-compatible complementary vector extends the partial isometry")

        scalars = field.regular_module()
        frame = Modules(field).biproduct((self.domain(), scalars))
        source_map = frame.from_summands(
            source_inclusion, Modules(field).Mor(scalars, source)(lambda label: source_vector)
        )
        target_map = frame.from_summands(
            target_inclusion * self, Modules(field).Mor(scalars, target)(lambda label: target_vector)
        )
        extended_map = target_map * source_map.section()
        extension = source.Isom(target)(lambda label: extended_map(source.module_generator(label)))
        points = locus.object()
        return points.inclusion()(points(extension))

    def integral_restriction(self, source, target):
        r"""Return the induced lattice isometry, or ``None`` if it is not integral.

        ``self`` must have the fraction-field extensions of ``source`` and
        ``target`` as endpoints. Both the map and its inverse must preserve
        the respective lattices; an integral embedding alone is insufficient.
        """
        ring = source.base_ring()
        if target.base_ring() is not ring:
            raise ValueError("integral restriction requires a common base ring")
        fraction_map = ring.fraction_field_map()
        if self.domain() is not source.base_change(fraction_map) or self.codomain() is not target.base_change(fraction_map):
            raise ValueError("the isometry must join the selected lattices' fraction-field extensions")
        restrict = Modules(fraction_map.codomain()).restriction_of_scalars(fraction_map)
        source_inclusion = ModulesOverIntegralDomains(ring)(source).generic_fibre_map()
        target_inclusion = ModulesOverIntegralDomains(ring)(target).generic_fibre_map()
        rational_source = self.domain()
        rational_target = self.codomain()
        linear = rational_source.module_category().Mor(rational_source, rational_target)(self)
        forward = (restrict(linear) * source_inclusion).factor_through_or_none(target_inclusion)
        if forward is None:
            return None
        inverse = self.inverse()
        inverse_linear = rational_target.module_category().Mor(rational_target, rational_source)(inverse)
        backward = (restrict(inverse_linear) * target_inclusion).factor_through_or_none(source_inclusion)
        if backward is None:
            return None
        module_isomorphism = Modules(ring).Core().Mor(source, target)(forward, backward)
        homset = source.Isom(target)
        return homset.element_class(homset, module_isomorphism)

    def integral_similarity(self, source, target):
        r"""Clear the least integral denominator, retaining ``sigma=N*self``.

        The result is a formed module embedding from source to target with
        form multiplier ``N^2``. Its ``scale()`` is ``N`` and its image
        is the integral image submodule, which may have nontrivial index.
        For ``diag(2,1/2)`` on U, these are 2, 4, and index 4 respectively.
        """
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules

        ideal = self.denominator_ideal(source, target)
        (scale,) = tuple(ideal.ideal_generators())
        ring = source.base_ring()
        field_map = ring.fraction_field_map()
        restrict = Modules(field_map.codomain()).restriction_of_scalars(field_map)
        rational = restrict(self) * ModulesOverIntegralDomains(ring)(source).generic_fibre_map()
        scaled = Modules(ring).Mor(source, rational.codomain())(
            lambda label: rational.codomain().scalar_multiple(
                scale, rational(source.module_generator(label))
            )
        )
        integral = scaled.factor_through_or_none(ModulesOverIntegralDomains(ring)(target).generic_fibre_map())
        if integral is None:
            raise ArithmeticError("the denominator ideal failed to clear the rational map")
        values = ring.regular_module()
        value_map = Modules(ring).Mor(values, values)(
            lambda label: values.scalar_multiple(scale * scale, values.module_generator(label))
        )
        return FormModules(ring).Mono(source, target)(
            integral, value_morphism=value_map,
            denominator_clearing=(self, ideal, scale),
        )

    def inverse(self):
        r"""Return the inverse isometry."""
        codomain = self.codomain()
        if self._isometry_inverse_computation is not None:
            inverse = self._isometry_inverse_computation()
            target = codomain.Isom(self.domain())
            return target._from_inverse_computation(inverse, lambda: self)
        module_isomorphism = self._underlying_module_isomorphism
        if module_isomorphism is not None:
            target = codomain.Isom(self.domain())
            reverse = codomain.module_category().Core().Mor(
                codomain,
                self.domain(),
            )._from_known_inverse_pair(
                module_isomorphism.inverse().forward(),
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
            # The search runs over the finite group O(L) of a definite lattice over ZZ
            # (orthogonalGroup_finite); over QQ they form O(V), not finite in rank at least 2.
            assert target.base_ring() is _owned_integers(), (
                f"cannot find an isometry h: {source} -> {target} with h*{self} = {other}*h: "
                f"the search runs over the finite orthogonal group of a definite lattice over ZZ, "
                f"and {target} is over {target.base_ring()}"
            )
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
        if isinstance(images, Morphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError(
                    f"the morphism {images} goes from {images.domain()} to {images.codomain()}, so it is not a lattice morphism from {self.domain()} to {self.codomain()}"
                )
            if images.parent() is self:
                return images
            _refuse_foreign_arrow(self, images, "use the functor between the source and target categories")
        if isinstance(images, dict):
            images = _labelled_generator_images(self.domain(), images)
        return self.element_class(self, images)

    def elementwise(self, function):
        if isinstance(function, Morphism):
            return self(function)
        if not callable(function):
            raise TypeError(f"{function} cannot define a lattice morphism from {self.domain()} to {self.codomain()}: it is not a function of the elements of {self.domain()}")
        source = self.domain()
        return self.element_class(
            self,
            lambda label: function(source.module_generator(label)),
        )

    @object_level
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
        if isinstance(images, Morphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError(
                    f"the morphism {images} goes from {images.domain()} to {images.codomain()}, so it is not a lattice embedding of {self.domain()} into {self.codomain()}"
                )
            if images.parent() is self:
                return images
            _refuse_foreign_arrow(self, images, "use the functor between the source and target categories")
        if isinstance(images, dict):
            images = _labelled_generator_images(self.domain(), images)
        return self.element_class(self, images)

    def elementwise(self, function):
        if isinstance(function, Morphism):
            return self(function)
        if not callable(function):
            raise TypeError(f"{function} cannot define a lattice embedding of {self.domain()} into {self.codomain()}: it is not a function of the elements of {self.domain()}")
        source = self.domain()
        return self.element_class(
            self,
            lambda label: function(source.module_generator(label)),
        )

    def super_categories(self):
        r"""Retain lattice morphisms and endpoint-admissible inherited monomorphisms.

        Only packets containing both endpoints contribute inherited Mor
        categories; a lattice embedding is not automatically a morphism in
        a packet whose objects exclude either endpoint.

        EXAMPLES::

            sage: L = Lattices(ZZ)("U")
            sage: E = L.Mono(L)
            sage: E.domain() is L and E.codomain() is L and len(E.super_categories()) >= 1
            True
            sage: all(C.domain_object() is L and C.codomain_object() is L for C in E.super_categories())
            True
            sage: identity = E.identity()
            sage: identity * identity == identity
            True
        """
        packet = self.base_category().category_packet()
        source = self.domain()
        target = self.codomain()
        inherited = [superpacket.Monos().Of(source, target) for superpacket in packet.super_packets() if source in superpacket.C() and target in superpacket.C()]
        return [packet.Mors().Of(source, target), *inherited]

    def _repr_(self):
        return f"Emb({self.domain()}, {self.codomain()})"

    def _codomain_is_definite_over_integers(self) -> bool:
        r"""Whether the codomain is a definite ZZ-lattice of finite rank, whose square shells are finite.

        Over ``QQ`` a definite space has infinite square fibres (``x^2 + y^2 = 1``
        has the rational points ``(3/5, 4/5)``), so embeddings into it are not
        enumerated shell by shell.
        """
        target = self.codomain()
        return target.base_ring() is _owned_integers() and target.module_rank().is_finite() and target.is_definite()

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
        assert target.base_ring() is _owned_integers() and target.module_rank().is_finite() and target.is_definite(), (
            f"the embeddings of {source} into {target} are enumerated only when {target} is a definite lattice of "
            f"finite rank over ZZ, whose square shells are finite; {target} is over {target.base_ring()}"
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

    def _emptiness_decision(self) -> bool | None:
        r"""``Emb(L, M) = ∅``, supplied to the ``Sets`` emptiness hook; ``None`` where no route decides it."""
        if self._codomain_is_definite_over_integers():
            for _embedding in self:
                return False
            return True
        source = self.domain()
        target = self.codomain()
        if source.module_rank().is_finite() and target.module_rank().is_finite() and source.module_rank() == target.module_rank():
            match source.Isom(target).is_empty():
                case True:
                    return True
                case False:
                    return False
                case _:
                    return None
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
        return None

    def an_element(self):
        if self._codomain_is_definite_over_integers():
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
            f"embeddings are constructed only into definite targets over ZZ, targets of equal "
            f"rank, indefinite targets OSCAR classifies, and even unimodular indefinite "
            f"targets, and {self.codomain()} is none of these"
        )


def _orthogonal_group_is_finite_by_theorem(lattice) -> bool:
    r"""Whether a cited theorem places ``O(L) = Aut(L)`` among the finite groups (``CON-07``).

    The decision reads the base ring, the rank, the signature and the square
    class of the determinant; it never computes the group.  The routed cases:

    - ``L`` a definite lattice of finite rank over ``ZZ``.  For positive
      definite ``L`` this is ``lean-categories``
      ``LeanCategories/Lattices/Valued/Mass.lean:41``, ``orthogonalGroup_finite``.
      A negative definite ``L`` has the positive definite sign twist ``L(-1)``,
      the same module with form ``-b``; an automorphism preserves ``b`` exactly
      when it preserves ``-b``, so ``O(L) = O(L(-1))`` is the same group.
    - ``L`` of rank 2 over ``ZZ`` with ``-det G`` a nonzero square in ``QQ``.
      C. O'Sullivan, *Topographs for binary quadratic forms and class numbers*,
      arXiv:2408.14405v3, Section 8.1, Corollary 8.2 (p. 29), with
      ``Aut(q) := {M in SL(2, Z) : q|M = q}`` for ``q = [a, b, c]`` of
      discriminant ``D = b^2 - 4ac``: "Let q be a primitive form of
      discriminant D. Then Aut(q) = {±I} for D a nonzero square or D < -4."
      The same section notes ``Aut(lambda q) = Aut(q)``, so primitivity is no
      restriction.  The form of ``L`` is ``q = [g_11, 2 g_12, g_22]``, so
      ``D = -4 det G``, and ``D`` is a nonzero square exactly when ``-det G``
      is one.  Hence ``SO(L) = Aut(q) = {1, -1}``.  The determinant
      ``O(L) -> {1, -1}`` is a group morphism with kernel ``SO(L)``, so
      ``[O(L) : SO(L)] <= 2`` and ``O(L)`` has order at most 4; for the
      hyperbolic plane ``U``, ``O(U) = {1, -1, swap, -swap}``.  The
      ``lean-categories`` statement is requested (COMPLAINTS.md, *Finiteness
      of O(L) for split binary lattices is not formalized*).

    Definite lattices over ``QQ`` are not routed: ``O(x^2 + y^2)`` over ``QQ``
    contains the rotation with cosine ``3/5`` and sine ``4/5``, of infinite
    order.  A rank-2 indefinite ``ZZ``-lattice with ``-det G`` not a square is
    not routed either; its group is infinite by Pell's equation, whose
    solvability has no opened source here.
    """
    if _engine_ring(lattice.base_ring()) is not SageZZ or not lattice.module_rank().is_finite():
        return False
    if lattice.is_definite():
        return True
    if lattice.module_rank() != 2:
        return False
    minus_determinant = lattice_engines._binary_form_discriminant(lattice)
    return bool(minus_determinant != 0 and minus_determinant.is_square())


class LatticeIsometryMor(LatticeEmbeddingMor, CoreMor):
    r"""``Isom(L, M)``: the core Mor of ``Lattices(R)``, its isomorphisms being the isometries.

    It is ``Lattices(R).Core().Mor(L, M)`` (``_LatticeCore``), so
    ``O(L) = Aut(L)`` takes its group placement from the core owner
    (``CoreMor._vertex_group_placement``).  Its elements remain the lattice
    isometries (``LatticeIsometryMethods``), and its group computations are
    realized by Sage matrix groups.
    """

    ElementMethods = LatticeIsometryMethods

    @lazy_attribute
    def element_class(self) -> type:
        r"""The lattice isometry arrow type generated from ``LatticeIsometryMethods``, not ``CoreMor``'s isomorphism pair."""
        return self._generated_arrow_type()

    @property
    def ElementType(self) -> type:
        return self._generated_arrow_type()

    def core_category(self):
        return self.domain().lattice_category().Core()

    def _from_known_inverse_pair(self, forward, inverse):
        r"""The isometry whose forward arrow is ``forward``; its inverse is that of the isometry."""
        return self._from_inverse_computation(forward, lambda: inverse)

    def _from_inverse_computation(self, forward, inverse_computation):
        r"""Retain the core's forward lattice arrow and lazy inverse (``CoreMor``'s protected contract)."""
        base = self.core_category().base_category()
        assert _category_accepts_morphism(base, self.domain(), self.codomain(), forward), (
            f"{forward} is not a lattice morphism {self.domain()} -> {self.codomain()}"
        )
        return self.element_class(self, forward, inverse_computation=inverse_computation)

    def __init__(self, mor_family, domain, codomain) -> None:
        group = CoreMor._vertex_group_placement(domain, codomain)
        categories = [] if group is None else [group]
        if domain is codomain and _orthogonal_group_is_finite_by_theorem(domain):
            categories.append(OwnedFiniteGroups())
        LatticeEmbeddingMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
            category=Cat().meet(tuple(categories)) if categories else None,
        )
        if domain is codomain:
            self._initialize_vertex_group()

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
            _refuse_foreign_arrow(self, images, "use the functor between the source and target categories")
        if isinstance(images, Morphism):
            # A module isomorphism or automorphism, a lattice endomorphism or a
            # set map: almost none is an isometry (``CON-17``).
            _refuse_foreign_arrow(
                self, images, "an isometry is given by its generator images, a function on elements or a "
                "matrix; the scalar extension of an isometry is its base_change"
            )
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

    @object_level
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

    def _cardinality_decision(self):
        r"""``|Isom(L, M)|``, supplied to the ``Sets`` cardinality hook by this realization.

        ``O(L)`` is counted from its own data: the finite definite engine
        for definite ``L`` over ``ZZ``; for definite ``L`` over another base
        ring no exact count is computed here (``CAT-01``); otherwise the
        integral matrix group generated by
        the selected generators of ``O(L)``, whose finiteness and order GAP
        decides.  A nonempty ``Isom(L, M)`` is a torsor under ``O(M)`` by
        postcomposition and has its cardinality; an empty one has none.
        When emptiness is undecided, the cardinality is not computed
        (``CAT-01``).
        """
        if self.domain() is self.codomain():
            if self.domain().module_rank() == 0:
                return cardinal(1)
            if self.domain().is_definite():
                self._assert_definite_over_integers("count")
                return cardinal(int(self._engine_group().order()))
            generated = self._engine_subgroup_from_generators(tuple(self._computed_group_generators()))
            if generated.is_finite():
                return cardinal(int(generated.order()))
            return aleph(0)
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
        ``g ∘ source = target``.  For two finite families of vectors of ``L``
        (elements of ``Sets().Mor(I, L)``, or of ``Sets().Mor(I, L x C)`` for
        coloured families) it is one ``g`` in ``O(L)`` with ``g o v = w o sigma`` for
        some colour-preserving bijection ``sigma`` of the index sets, or
        ``None`` when there is none; see ``coloured_vector_families`` for the
        computation and its spanning hypothesis.
        """
        lattice = self.codomain()
        if self.domain() is lattice and element_parent(source) is lattice and element_parent(target) is lattice:
            return self.vector_equivalence_witness(source, target)
        if self.domain() is lattice and element_parent(source) is not self and element_parent(target) is not self:
            from dzack_research.preamble.categories.coloured_vector_families import _transporter

            return _transporter(self, source, target)
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
        generating_subgroup = self.subgroup(tuple(self.group_generators()))
        return generating_subgroup.image_under(self.discriminant_representation())

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
        witnesses = self.finite_image_lifts(representation)
        return witnesses.get(automorphism)

    def discriminant_orthogonal_group_generator_lifts(self):
        r"""Return lifts along ``rho_L: O(L) -> O(A_L)`` of the group generators of ``O(A_L)``.

        The family has the index set of the generating family
        ``O(A_L).group_generators()``; its value at a label is an isometry
        ``g`` of ``L`` with ``rho_L(g) = h`` for the generator ``h`` at that
        label, the lift :meth:`discriminant_lift` selects.  This is the operation of any
        lattice ``L`` whose discriminant representation is surjective; the
        hypothesis is asserted, generator by generator, before the family is
        returned.  When ``rho_L`` is not surjective, the group generators of
        ``O(A_L)`` do not all lie in ``rho_L(O(L))``, and lifts of elements of
        that image are :meth:`discriminant_lift` and
        :meth:`discriminant_factorization`.

        Owner ruling 2026-10-15: this lift is a research primitive on
        ``O(L)``, not part of the ``2U + K`` approximate-model assembly.
        """
        from dzack_research.preamble.categories.sets.indexed_families import (
            finite_indexed_family,
        )

        assert self.domain() is self.codomain(), (
            f"lifts along O(L) -> O(A_L) need an orthogonal group O(L), but {self} is the set of "
            f"isometries {self.domain()} -> {self.codomain()} between different lattices"
        )
        lattice = self.domain()
        generators = lattice.discriminant_group().orthogonal_group().group_generators()
        labels = generators.index_set()
        lifts = {label: self.discriminant_lift(generators.value(label)) for label in labels}
        for label, lift in lifts.items():
            assert lift is not None, (
                f"cannot lift {generators.value(label)} along O(L) -> O(A_L) for L = {lattice}: it "
                f"is a group generator of O(A_L) that is not induced by any isometry generated by "
                f"the known group generators of O(L), so O(L) -> O(A_L) is not known to be surjective"
            )
        return finite_indexed_family(
            labels,
            lambda label: lifts[label],
            name=f"lifts along O(L) -> O(A_L) of the group generators of O(A_L), L = {lattice}",
        )

    def discriminant_factorization(self, isometry):
        r"""Return the point ``(s, l)`` with ``g = s l``, ``s`` stable and ``rho_L(l) = rho_L(g)``.

        Let ``rho_L: O(L) -> O(A_L)`` be the discriminant representation and
        ``1 -> ker(rho_L) -> O(L) -> rho_L(O(L)) -> 1`` its exact sequence.
        For ``g`` in ``O(L)``, ``l`` is the lift of ``rho_L(g)`` that
        :meth:`discriminant_lift` selects, and ``s = g l^{-1}``.  Since
        ``rho_L`` is a homomorphism, ``rho_L(s) = 1``, so ``s`` lies in the
        stable orthogonal group ``ker(rho_L)``; ``g = s l`` holds by the
        definition of ``s``.  The selected lift is a set section of
        ``O(L) ->> rho_L(O(L))``, not a group splitting, so ``g |-> (s, l)``
        is a bijection of underlying sets and not a homomorphism.

        The result is a point of the product of the underlying sets of
        ``ker(rho_L)`` and ``O(L)`` (``CON-15``), in that order; it is
        defined for every lattice ``L`` whose known group generators of
        ``O(L)`` generate a group with image ``rho_L(O(L))``.

        Owner ruling 2026-10-15: this factorization is a research primitive
        on ``O(L)``.
        """
        assert self.domain() is self.codomain(), (
            f"the factorization through O(L) -> O(A_L) needs an orthogonal group O(L), but {self} "
            f"is the set of isometries {self.domain()} -> {self.codomain()} between different lattices"
        )
        lattice = self.domain()
        isometry = self(isometry)
        lift = self.discriminant_lift(isometry.discriminant_morphism())
        assert lift is not None, (
            f"cannot factor {isometry} through O(L) -> O(A_L) for L = {lattice}: its image "
            f"{isometry.discriminant_morphism()} is not induced by any isometry generated by the "
            f"known group generators of O(L), so those generators do not generate O(L)"
        )
        stable = lattice.stable_orthogonal_group()
        return Sets().product((stable, self))((stable(isometry * ~lift), lift))

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

    def _centralizer_construction(self, isometry):
        r"""Realization of the groups' centralizer hook: ``Z_{O(L)}(isometry)`` with its generators selected.

        Implementer side of ``OwnedGroups.ParentMethods._centralizer_construction``
        (``OWN-05``), called only by ``centralizer``.  The subgroup is the
        predicate subgroup ``{g : g f = f g}``; its group generators are
        computed on first request, by gluing the centralizers on the
        cyclotomic summands of ``isometry``
        (``lattice_centralizers.arithmetic_centralizer``).
        """
        from dzack_research.preamble.categories.lattice_centralizers import (
            arithmetic_centralizer,
        )

        return arithmetic_centralizer(self, isometry)

    def intersection(self, *subgroups):
        r"""Return the intersection of represented subgroups of this orthogonal group."""
        return IntersectionSubgroups(self)(subgroups)

    def lattice(self):
        r"""Return \(L\), the lattice this orthogonal group acts on."""
        assert self.domain() is self.codomain(), (
            f"the isometries {self.domain()} -> {self.codomain()} are not an orthogonal group O(L): domain and codomain are different lattices"
        )
        return self.domain()

    @cached_method
    def natural_module_action_functor(self):
        r"""The action functor `BO(L) -> Mod_R` on the module of L."""
        from dzack_research.preamble.categories.functors.group_actions import GroupActionFunctor
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        lattice = self.lattice()
        modules = Modules(lattice.base_ring())
        return GroupActionFunctor(
            self,
            modules,
            lattice,
            lambda automorphism: modules.Mor(lattice, lattice)(automorphism),
        )

    def stabilizer(self, target, action="setwise"):
        r"""Return a vector, sublattice or family stabilizer in ``O(L)``.

        A lattice vector is fixed pointwise.  A represented lattice subobject
        accepts ``action='setwise'`` or ``action='pointwise'`` and delegates to
        the existing inclusion-based subgroup constructions.  A finite family
        ``v: I -> L`` (an element of ``Sets().Mor(I, L)``), or a coloured family
        ``i |-> (v_i, c_i)`` in ``Sets().Mor(I, L x C)``, has the stabilizer
        ``O(L)_[v] = {g : g o v = v o sigma for some colour-preserving bijection sigma of I}``,
        the image in ``O(L)`` of its stabilizer under ``O(L) x Sym_C(I)``; the
        kernel of that projection, ``K_v``, is trivial exactly when the coloured
        family is injective (``coloured_vector_families``).
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
            raise ValueError(f"action={action!r} applies only to sublattices; {target} is not a sublattice of {lattice}, and a vector or a family is stabilized up to reindexing")
        if element_parent(target) is not lattice:
            return self._family_stabilizer(target)
        return StabilizerSubgroups(self)(
            target,
            self.natural_module_action_functor(),
            lambda automorphism: automorphism(target) == target,
            description=f"g fixes {target}",
        )

    @cached_method(key=lambda self, family: id(family))
    def _family_stabilizer(self, family):
        r"""``O(L)_[v]`` for a finite (coloured) family of vectors, with its computed group generators.

        The subgroup is cut out of ``O(L)`` by its definition: ``g`` carries
        the coloured family to itself up to a colour-preserving bijection of
        its indices.  Its generators are the stabilizer of the integral
        structure ``L`` under the rational configuration group of the family
        (``coloured_vector_families``), selected as its generating set; they
        are the computation's answer, untrusted like every answer.
        """
        from dzack_research.preamble.categories.coloured_vector_families import (
            _matching,
            _realization,
            _stabilizer_generators,
        )

        realization = _realization(self.lattice(), family)
        return self.predicate_subgroup(
            lambda automorphism: _matching(realization, realization, automorphism) is not None,
            f"g o v = v o sigma for a colour-preserving bijection sigma, for the family {family}",
            generating_morphism=self.free_cover(_stabilizer_generators(self, family)),
        )

    def index_action(self, family):
        r"""The action of ``O(L)_[v]`` on the index set ``I`` of an injective coloured family.

        For an injective coloured family ``(v_i, c_i)_{i in I}`` an element
        ``g`` of its stabilizer determines the colour-preserving bijection
        ``sigma = (v, c)^-1 o (g x id) o (v, c)`` of ``I``, and
        ``g . i = sigma(i)`` is an action.  The result is that finite
        ``O(L)_[v]``-set on ``I``; its ``permutation_representation()`` is the
        group morphism ``O(L)_[v] -> Sym(I)``.  For a family carrying one
        coloured vector at two indices ``sigma`` is determined only up to
        ``K_v`` and no action on ``I`` is defined.
        """
        from dzack_research.preamble.categories.coloured_vector_families import (
            _assert_injective,
            _index_permutation,
        )
        from dzack_research.preamble.categories.group.g_sets import FiniteGSets

        realization = _assert_injective(self, family)
        return FiniteGSets(self.stabilizer(family))(
            realization.indices(),
            lambda automorphism, index: _index_permutation(self, family, automorphism)[index],
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
            embedding,
            self.natural_module_action_functor(),
            lambda automorphism: all(automorphism(vector) == vector for vector in embedded),
            description=f"g fixes {embedding} pointwise",
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
            embedding,
            self.natural_module_action_functor(),
            preserves_image,
            description=f"g(im({embedding}))=im({embedding})",
        )

    def _assert_definite_over_integers(self, operation: str) -> None:
        r"""State the hypothesis of the finite routes of ``O(L)``: ``L`` definite of finite rank over ``ZZ``.

        ``O(L)`` is finite for such ``L`` (``lean-categories``
        ``orthogonalGroup_finite``, ``LeanCategories/Lattices/Valued/Mass.lean:41``,
        with ``L(-1)`` for negative definite ``L``).  A definite lattice over
        ``QQ`` is a quadratic space ``V`` whose ``O(V)`` is not finite in rank
        at least 2 (``O(x^2+y^2)`` contains the rotation ``(3/5, 4/5)``); no
        exact computation of it is supplied here (``CAT-01``).
        """
        lattice = self.domain()
        assert lattice.base_ring() is _owned_integers() and lattice.module_rank().is_finite() and lattice.is_definite(), (
            f"cannot {operation} O({lattice}) as a finite group: that computation is supplied for a definite "
            f"lattice of finite rank over ZZ, and {lattice} is a lattice over {lattice.base_ring()} of rank "
            f"{lattice.module_rank()}"
        )

    @cached_method
    def _engine_group(self):
        r"""Return Sage's private orthogonal-group engine when it is exact.

        The public group remains this Mor of live lattice isometries.  Sage's
        ``GroupOfIsometries`` is used only to compute the finite group ``O(L)``
        of a definite lattice of finite rank over ``ZZ``
        (``orthogonalGroup_finite``); its matrices act on row vectors, hence
        are transposed when converted to this Mor's column-image convention.
        Over ``QQ`` the Gram matrix cleared of denominators presents only the
        integral span of the chosen basis, whose finite group is not ``O(V)``.
        """
        lattice = self.domain()
        if lattice is not self.codomain():
            raise ValueError(f"the isometries {lattice} -> {self.codomain()} are not an orthogonal group O(L): domain and codomain are different lattices")
        self._assert_definite_over_integers("compute")
        from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

        gram = _engine_component_matrix(lattice.gram_tensor()).change_ring(SageZZ)
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
                            _owned_engine_element(ring, _engine_ring(ring)(coefficient)),
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

    def _engine_subgroup_contains(self, automorphism, engine_subgroup):
        matrix = self._row_action_matrix(automorphism)
        # The selected generator and its inverse are members by the
        # definition of generated subgroup, independently of whether Sage's
        # matrix-group membership algorithm decides an infinite subgroup.
        # Orbit-span closure needs precisely these two directions.
        if any(matrix == generator.matrix() or matrix == generator.matrix().inverse()
               for generator in engine_subgroup.gens()):
            return True
        return matrix in engine_subgroup

    def _from_subgroup_engine(self, engine_element):
        r"""Raise an element of a generated matrix subgroup to a live isometry."""
        return self._from_backend_row_action(engine_element.matrix())

    @cached_method
    def _computed_group_generators(self):
        r"""Return generators of ``O(L)``, computed by a backend, as a finite ordered set of ``O(L)``.

        Protected realization hook (``OWN-05``): owner ``LatticeIsometryMor``;
        caller ``Lattices._core_automorphism_generators`` (read by ``CoreMor._initialize_vertex_group``)
        (the lattice implementer of ``CoreMor``'s core contract).

        For definite ``L`` over ``ZZ``, Sage's ``GroupOfIsometries`` computes the
        generators of the finite group ``O(L)``; a definite ``L`` over another
        base ring reaches the stated frontier. For indefinite ``L``,
        ``sage_indefinite_port`` computes them. Both answers are untrusted
        engine output: each computed isometry is constructed through ``O(L)``
        into an element of ``O(L)``, and the family becomes one finite ordered
        set of ``O(L)``.
        """
        lattice = self.domain()
        if lattice.module_rank() == 0:
            # O(0) is trivial, generated by the empty family (TRAPS.md: Sage's
            # GroupOfIsometries cannot be formed on an empty generating family).
            generators = ()
        elif lattice.is_definite():
            self._assert_definite_over_integers("compute generators of")
            generators = tuple(self._from_engine(generator) for generator in self._engine_group().gens())
        else:
            from dzack_research.preamble.categories.lattices import Lattices
            from sage_indefinite_port.indefinite.marked_lattices import (
                automorphism_group_generators,
            )

            category = Lattices(lattice.base_ring())
            generators = tuple(
                self(generator)
                for generator in automorphism_group_generators(category, lattice)
            )
        positions = Sets.Δ[len(generators) - 1]
        return FiniteOrderedSets().from_indexed(
            positions,
            lambda position: generators[int(position)],
            name=f"Orthogonal-group generators of {lattice}",
        )

    def structure_description(self):
        r"""Return GAP's descriptive structure label for a finite ``O(L)``.

        The maintained Sage ``GroupOfIsometries`` computation uses GAP internally and
        supplies ``StructureDescription``.  This method is intentionally
        descriptive only: GAP does not promise that the returned string is an
        isomorphism invariant, so no equality or subgroup decision in the
        owned layer depends on it.
        """
        self._assert_definite_over_integers("describe the structure of")
        return str(self._engine_group().structure_description())

    def __iter__(self):
        r"""Enumerate the finite group ``O(L)`` of a definite lattice over ``ZZ``."""
        self._assert_definite_over_integers("enumerate")
        return (self._from_engine(element) for element in self._engine_group())

    def vector_equivalence_witness(self, left, right):
        r"""Return ``g in O(L)`` with ``g(left)=right``, or ``None``.

        For a definite lattice over ``ZZ`` this is an exact search through the
        finite group ``O(L)``; a definite lattice over another base ring reaches
        the stated frontier.  Indefinite vector equivalence belongs to its
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
            from sage_indefinite_port.indefinite.marked_lattices import (
                isometry,
            )

            category, marked_left = _pointed_marking(lattice, left)
            source = category.base_object()
            marked_right = category.object(
                source.Mor(lattice)(lambda _label: right)
            )
            return isometry(category, marked_left, marked_right)
        self._assert_definite_over_integers("search")
        for automorphism in self:
            if automorphism(left) == right:
                return automorphism
        return None

    def vectors_are_equivalent(self, left, right) -> bool:
        r"""Return whether two vectors lie in the same ``O(L)``-orbit."""
        return self.vector_equivalence_witness(left, right) is not None

    def vector_stabilizer_generators(self, element):
        r"""Return generators of ``Stab_{O(L)}(element)``.

        ``Stab_{O(L)}(v)`` is the apex image of ``Aut`` of the pointed
        lattice ``(L, <q(v)> -> L)``, so this is the pointed case of the
        stabilizer of a marking (:meth:`_marking_stabilizer_generators`).
        """
        lattice = self.domain()
        element = element if element_parent(element) is lattice else lattice(element)
        category, marked = _pointed_marking(lattice, element)
        return self._marking_stabilizer_generators(category, marked, category.apex_stabilizer(marked))

    def _finite_subgroup_generators(self, subgroup):
        r"""Generators of a subgroup of the finite ``O(L)`` of a definite lattice over ``ZZ``.

        The subgroup is listed in one pass over ``O(L)`` and reduced to a
        generating set in Sage's private finite isometry group; only live
        lattice isometries cross back into the public result.
        """
        self._assert_definite_over_integers("reduce a subgroup of")
        elements = tuple(automorphism for automorphism in self if automorphism in subgroup)
        engine_subgroup = self._engine_group().subgroup(tuple(self._to_engine(automorphism) for automorphism in elements))
        return finite_ordered_set(tuple(self._from_engine(engine_isometry) for engine_isometry in engine_subgroup.gens()))

    def _marking_stabilizer_generators(self, category, marked, stabilizer):
        r"""Generators of ``stabilizer``, the apex image in ``O(L)`` of ``Aut`` of a marked lattice with apex ``L``.

        ``stabilizer`` is ``category.apex_stabilizer(marked)``.  For definite
        ``L`` over ``ZZ`` it is a subgroup of the finite ``O(L)``, reduced to
        generators here.  For indefinite ``L`` the generators are the apex
        isometries that the lattice category's marked-diagram decision
        supplies (``sage-indefinite-port``, #403); they are untrusted engine
        output.
        """
        lattice = self.lattice()
        if lattice.is_definite():
            return self._finite_subgroup_generators(stabilizer)
        return lattice.lattice_category()._marked_automorphism_generators(category, marked)

    def _marking_category(self, marked):
        r"""The category of marked lattices with apex ``L`` of which ``marked`` is an object.

        The marking categories over ``Lattices(R)`` are ``Ar(Lattices)``,
        ``Fun([2], Lattices)`` and the coslices ``X/Lattices``; a coslice
        object names its ``X`` as the source of its arrow.
        """
        from dzack_research.preamble.categories.abstract_categories.products import (
            FiniteOrdinalCategory,
        )

        lattice = self.lattice()
        lattices = lattice.lattice_category()
        sublattices = Cat().Mor(FiniteOrdinalCategory(2), lattices)
        flags = Cat().Mor(FiniteOrdinalCategory(3), lattices)
        match marked:
            case _ if marked in sublattices:
                category = sublattices
            case _ if marked in flags:
                category = flags
            case _:
                category = CosliceCategory(lattices, marked.arrow().domain())
        assert marked in category, (
            f"{marked} is not a marked lattice: it is an object of none of Ar({lattices}), "
            f"Fun([2], {lattices}) or a coslice X/{lattices}"
        )
        return category

    def split_orbit(self, marked, subgroup):
        r"""One marked lattice in each ``H``-orbit of the ``O(L)``-orbit of ``marked``.

        ``G = O(L)`` acts on the marked lattices with apex ``L`` (objects of
        ``X/Lattices``, ``Ar(Lattices)`` or ``Fun([2], Lattices)``) by
        postcomposing the marking, ``g . m``, with stabilizer
        ``G_m = category.apex_stabilizer(m)``.  The ``G``-orbit of ``m`` is
        ``G/G_m``, and for ``H = subgroup`` its ``H``-orbits are the double
        cosets ``H \ G / G_m``: ``g . m`` and ``g' . m`` are carried onto one
        another by an element of ``H`` exactly when ``g'`` lies in ``H g G_m``.

        ``H`` contains the kernel of a finite-image character map
        ``rho: G -> Q`` (``H.contains_character_kernel()``), so these double
        cosets are those of ``rho(H) \ rho(G) / rho(G_m)``, computed by the
        character quotient of ``H`` from generators of ``G_m``
        (``OrthogonalCharacterQuotient.splitting_isometries``).  For ``H = G``
        there is one double coset and ``m`` is its representative.

        The result is the finite set of the representatives ``g . m``.  The
        stabilizer in ``H`` of ``g . m`` is ``H cap g G_m g^{-1}``, which is
        ``subgroup.intersection(category.apex_stabilizer(g . m))``.
        """
        category = self._marking_category(marked)
        stabilizer = category.apex_stabilizer(marked)
        assert stabilizer.supergroup() is self, (
            f"the orbit of {marked} under {self} is not defined: its marking ends at a lattice other "
            f"than {self.lattice()}"
        )
        match subgroup:
            case _ if subgroup is self:
                return finite_ordered_set((marked,))
            case _ if (
                subgroup in PredicateSubgroups(self)
                and subgroup.supergroup() is self
                and subgroup.contains_character_kernel()
            ):
                stabilizer_generators = self._marking_stabilizer_generators(category, marked, stabilizer)
                return finite_ordered_set(
                    tuple(
                        category.apex_action(splitting, marked)
                        for splitting in subgroup.finite_character_quotient().splitting_isometries(
                            stabilizer_generators
                        )
                    )
                )
        assert False, (
            f"cannot split the orbit of {marked} under {self} along {subgroup}: the splitting is "
            f"computed through a finite quotient of {self} by characters (discriminant, determinant, "
            f"spinor norm), so {subgroup} must contain the kernel of such a character map; it is "
            f"neither {self} itself nor a subgroup of {self} known to contain one"
        )

    def vector_orbit_representatives(self, square):
        r"""Return one representative of each ``O(L)``-orbit of square ``square``.

        For a definite lattice over ``ZZ`` the represented shell is finite, and
        ``O(L)`` is finite, so this is an exact finite quotient with no search
        bound; a definite lattice over another base ring reaches the stated
        frontier.
        """
        lattice = self.domain()
        square = lattice.base_ring()(int(square))
        if not lattice.is_definite():
            if square == lattice.base_ring().zero():
                primitive = tuple(_primitive_pointed_classes(lattice, square))
                zero = lattice.zero()
                if not primitive:
                    return finite_ordered_set((zero,))
                orbit_count = len(primitive)

                def element_at(index):
                    position = int(index)
                    if position == 0:
                        return zero
                    content_position, orbit_position = divmod(position - 1, orbit_count)
                    return lattice.scalar_multiple(
                        lattice.base_ring()(content_position + 1),
                        primitive[orbit_position],
                    )

                def index_of(vector):
                    if element_parent(vector) is not lattice:
                        return None
                    if vector == zero:
                        return NN(0)
                    if vector.q() != square:
                        return None
                    content = int(vector.content())
                    primitive_part = vector.primitive_part()
                    orbit_position = next(
                        (
                            position
                            for position, representative in enumerate(primitive)
                            if primitive_part == representative
                        ),
                        None,
                    )
                    if orbit_position is None:
                        return None
                    return NN(1 + (content - 1) * orbit_count + orbit_position)

                return OrderedEnumeratedSets()(
                    NN,
                    element_at,
                    index_of=index_of,
                    name=f"Square-zero orbit representatives of {lattice}",
                )
            representatives = []
            for content in abs(square).divisors():
                if square % (content * content) != lattice.base_ring().zero():
                    continue
                primitive_square = square // (content * content)
                representatives.extend(
                    lattice.scalar_multiple(content, representative)
                    for representative in _primitive_pointed_classes(lattice, primitive_square)
                )
            return finite_ordered_set(tuple(representatives))
        self._assert_definite_over_integers("split a square shell into the orbits of")
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

    def _emptiness_decision(self) -> bool | None:
        r"""``Isom(L, M) = ∅``, supplied to the ``Sets`` emptiness hook, decided without constructing an isometry where a theorem allows.

        :meth:`_isometry_decision` owns the decision; an isometry is built
        only by :meth:`an_element`.  An undecided case supplies no decision,
        and ``Sets.is_empty`` returns the proposition.
        """
        match self._isometry_decision()[0]:
            case True:
                return True
            case False:
                return False
            case _:
                return None

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
        r"""The decision whether this isometry Mor object is empty, and the theorem that decides it.

        Private computation record of :meth:`is_empty` and :meth:`an_element`:
        the pair of the emptiness answer (``True``, ``False`` or the
        proposition that the Mor is empty) and, for a nonempty Mor, the
        citation of what established nonemptiness.  No isometry is
        constructed here; :meth:`an_element` constructs one on request.

        After the invariant obstructions the decision compares the owned
        genera, ``L.genus() == M.genus()`` (equal signature and canonical
        ``ZZ_p``-symbols at every ``p | 2d``)
        [CS99, Ch. 15, §7, Thms 9-10; extraction
        ``references/literature/lattice-research/conway1999sphere.md``
        l.12139, l.12197, l.12251].  Inside one genus:

        - indefinite, rank at least 3: a spinor genus is one class
          [CS99, Ch. 15, Thm 14 (Eichler), l.12511].  With one improper
          spinor genus the Mor is nonempty with no further computation;
          with several, membership in one spinor genus is the criterion of
          [CS99, Ch. 15, Thm 15, l.12521-12529], decided by the one private
          adapter ``integer_lattices_are_isometric``;
        - indefinite, rank 2: comparison of the cycles of reduced binary
          forms [CS99, Ch. 15, §3.3, l.11569; Thm 1, l.11482], whose walk
          yields the equivalence matrix, cached by :meth:`_witness_matrix`;
        - definite: a genus whose mass ``sum_i 1/|O(L_i)|``
          [Conway--Sloane, *Low-dimensional lattices IV*, eq. (1);
          ``references/literature/lattice-research/conway1988mass.md``
          l.13-16] equals ``1/|O(L)|`` is the one class of ``L``; otherwise
          the exact equivalence search of :meth:`_witness_matrix` decides
          [CS99, Ch. 15, §10-§11, l.12775, l.12905].
        """
        domain = self.domain()
        codomain = self.codomain()
        if domain is codomain:
            return (False, "the identity of the lattice")
        undecided = AtomicProposition("is_empty", self)
        if not domain.module_rank().is_finite() or not codomain.module_rank().is_finite():
            return (undecided, None)
        if domain.module_rank() != codomain.module_rank():
            return (True, None)
        if domain.signature_pair() != codomain.signature_pair():
            return (True, None)
        if _engine_ring(domain.base_ring()) is not SageZZ or _engine_ring(codomain.base_ring()) is not SageZZ:
            return (undecided, None)

        domain_gram, codomain_gram = self._engine_grams()
        if domain_gram == codomain_gram:
            return (False, "equal Gram tensors: the identity on the generators")
        rank = domain.module_rank()
        if int(rank.finite_value()) <= 1:
            return (True, None)
        if domain.is_nondegenerate() != codomain.is_nondegenerate():
            return (True, None)
        if not domain.is_nondegenerate():
            return (undecided, None)
        if domain.is_even() != codomain.is_even():
            return (True, None)
        if domain.discriminant() != codomain.discriminant():
            return (True, None)
        if domain.discriminant_module().invariant_factors() != codomain.discriminant_module().invariant_factors():
            return (True, None)

        if domain.genus() != codomain.genus():
            return (True, None)

        signature = domain.signature_pair()
        definite = signature.first() == 0 or signature.second() == 0
        match definite, int(rank.finite_value()) >= 3:
            case False, True:
                if domain.genus().spinor_genus_count() == domain.base_ring().one():
                    return (False, "one genus with one spinor genus is one class [CS99, Ch. 15, Thm 14]")
                if lattice_engines.isometric_within_genus(domain, codomain):
                    return (False, "one spinor genus [CS99, Ch. 15, Thms 14-15]")
                return (True, None)
            case False, False:
                if self._witness_matrix() is False:
                    return (True, None)
                return (False, "equivalent in the cycle classification of binary forms [CS99, Ch. 15, §3.3]")
            case True, _:
                order = domain.orthogonal_group().cardinality()
                if domain.genus().mass() * domain.base_ring().fraction_field()(order) == 1:
                    return (False, "a genus of mass 1/|O(L)| is one class [Conway--Sloane, Low-dimensional lattices IV, eq. (1)]")
                if self._witness_matrix() is False:
                    return (True, None)
                return (False, "the exact equivalence search found an isometry [CS99, Ch. 15, §10-§11]")

    @cached_method
    def _engine_grams(self):
        r"""The Gram matrices over Sage's ``ZZ`` of the two endpoints; private engine data of the decision."""
        return (
            _engine_component_matrix(self.domain().gram_tensor()).change_ring(SageZZ),
            _engine_component_matrix(self.codomain().gram_tensor()).change_ring(SageZZ),
        )

    @cached_method
    def _witness_matrix(self):
        r"""The equivalence matrix the deciding search produces, or ``False`` when it finds none.

        Private engine data, for a definite pair (Sage's exact equivalence
        search, PARI ``qfisom``) or an indefinite binary pair (the cycle
        walk of :func:`_binary_indefinite_isometry_matrix`).  Its columns
        are the coordinates of the images of the domain generators.
        """
        domain_gram, codomain_gram = self._engine_grams()
        signature = self.domain().signature_pair()
        positive, negative = signature.first(), signature.second()
        if positive == 0 or negative == 0:
            sign = SageZZ.one() if negative == 0 else -SageZZ.one()
            return QuadraticForm(SageZZ, 2 * sign * codomain_gram).is_globally_equivalent_to(
                QuadraticForm(SageZZ, 2 * sign * domain_gram),
                return_matrix=True,
            )
        assert int(self.domain().module_rank()) == 2, (
            f"an equivalence search between {self.domain()} and {self.codomain()} is run here only for a definite or a binary pair"
        )
        return _binary_indefinite_isometry_matrix(domain_gram, codomain_gram)

    def an_element(self):
        r"""Return an isometry, constructed on request after the decision.

        The engine's matrix is an untrusted answer; the isometry's own
        form-square validator checks it under strict checking (OWN-22).
        """
        empty, reason = self._isometry_decision()
        assert empty is True or empty is False, f"cannot decide whether {self.domain()} and {self.codomain()} are isometric, so no isometry between them can be returned"
        if empty:
            raise ValueError(f"there is no isometry from {self.domain()} to {self.codomain()}: the lattices are not isometric")
        domain = self.domain()
        codomain = self.codomain()
        if domain is codomain:
            return self.identity()
        domain_gram, codomain_gram = self._engine_grams()
        if domain_gram == codomain_gram:
            return self._isometry_from_column_matrix(domain_gram.parent().one())
        signature = domain.signature_pair()
        if signature.first() == 0 or signature.second() == 0 or int(domain.module_rank()) == 2:
            transformation = self._witness_matrix()
            assert transformation is not False, (
                f"{domain} and {codomain} are isometric by {reason}, but the equivalence search found no isometry"
            )
            return self._isometry_from_column_matrix(transformation)

        from dzack_research.preamble.categories.lattices import Lattices
        from sage_indefinite_port.indefinite.marked_lattices import isometry

        witness = isometry(Lattices(domain.base_ring()), domain, codomain)
        assert witness is not None, (
            f"{domain} and {codomain} are isometric by {reason}, but sage-indefinite-port constructed no isometry between them"
        )
        return witness

    def _repr_(self):
        if self.domain() is self.codomain():
            return f"Orthogonal group O({self.domain()})"
        return f"Isom({self.domain()}, {self.codomain()})"


class _LatticeCore(_CoreCategory):
    r"""The core of ``Lattices(R)``: its Mor objects are the isometry Mors ``Isom(L, M)``."""

    def Mor(self, domain, codomain) -> LatticeIsometryMor:
        return _lattice_isometry_mor(domain, codomain)


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
