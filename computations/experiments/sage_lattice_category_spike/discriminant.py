r"""Discriminant quotients for synthetic integral lattices."""

from __future__ import annotations

from itertools import product

from sage.matrix.constructor import identity_matrix, matrix
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.element import Element

from .domain_algebra import (
    DiscriminantAction as DiscriminantActionCarrier,
    DiscriminantOrthogonalGroup as DiscriminantOrthogonalGroupCarrier,
    Genus as GenusCarrier,
)


def _lattice_key(lattice):
    return (
        repr(lattice.base_ring()),
        lattice.rank(),
        tuple(lattice.gram_matrix().list()),
        tuple(lattice._inclusion_rows().list()),
        tuple(lattice._ambient_gram().list()),
    )


def _relation_inclusion_matrix(cover_lattice, relation_lattice):
    r"""Integer inclusion of ``relation_lattice`` into ``cover_lattice`` (rows in cover coordinates).

    A finite quotient ``cover / relation`` needs the relation expressed as a genuine
    sublattice of the cover.  Two based-model routes carry that inclusion:

    - the relation is a subobject sharing the cover's coordinate system (a common root);
    - the cover is the metric dual ``relation#``, so the inclusion is the natural map
      ``relation -> relation#`` with matrix ``G`` (the relation's Gram).
    """
    if cover_lattice.rank() == 0:
        return matrix(ZZ, 0, 0)
    if relation_lattice._ambient_gram() == cover_lattice._ambient_gram():
        if not (relation_lattice.is_submodule(cover_lattice)):
            raise ValueError("relations must be a sublattice of the cover")
        return matrix(
            ZZ,
            [
                cover_lattice._underlying_module().coordinate_vector(vector(QQ, row))
                for row in relation_lattice._inclusion_rows().rows()
            ],
        )
    if relation_lattice.base_ring() is ZZ and relation_lattice.determinant() != 0 \
            and relation_lattice.dual() == cover_lattice:
        return matrix(ZZ, relation_lattice.gram_matrix())
    raise ValueError(
        "relation lattice is not a recognized sublattice of the cover; provide the "
        "relation as a subobject of the cover or as its metric dual"
    )


def _finite_coordinates(group, element):
    return tuple(group.coordinates(group(element)))


def _all_group_automorphisms(group):
    if group.ngens() == 0:
        return (SyntheticDiscriminantAction(group, identity_matrix(ZZ, 0)),)
    automorphisms = []
    candidates = tuple(group.elements())
    for images in product(candidates, repeat=group.ngens()):
        action = SyntheticDiscriminantAction.from_images(group, images)
        if action.is_automorphism():
            automorphisms.append(action)
    return tuple(automorphisms)


def _finite_all_subgroups(parent):
    seen = {}
    zero = parent.subgroup_generated_by(())
    seen[zero._key()] = zero
    frontier = [zero]
    while frontier:
        subgroup = frontier.pop()
        for element in parent.elements():
            generated = parent.subgroup_generated_by(tuple(subgroup.gens()) + (element,))
            key = generated._key()
            if key not in seen:
                seen[key] = generated
                frontier.append(generated)
    return tuple(seen[key] for key in sorted(seen, key=lambda item: sorted(item)))


def _finite_relations_among(parent, gens):
    gens = tuple(parent(gen) for gen in gens)
    ranges = tuple(range(parent.order(generator)) for generator in gens)
    return tuple(
        tuple(ZZ(coefficient) for coefficient in coefficients)
        for coefficients in product(*ranges)
        if parent.discrete_exp(coefficients, gens=gens) == parent.zero()
    )


def _finite_basis_from_generators(parent, gens):
    subgroup = parent.subgroup_generated_by(gens)
    if not (subgroup.cardinality() == parent.cardinality()):
        raise ValueError("generators do not span the whole group")
    return tuple(parent(gen) for gen in gens)


def _finite_scalar_multiply(parent, scalar, element):
    return ZZ(scalar) * element


def _finite_p_torsion(parent, p, k=1):
    p = ZZ(p)
    k = ZZ(k)
    assert p.is_prime(), (f"p-torsion requires a prime; found={p}")
    assert k >= 1, (f"p-torsion exponent must be positive; found={k}")
    return parent.subgroup_generated_by(element for element in parent.elements() if _finite_scalar_multiply(parent, p ** k, element) == parent.zero())


def _form_matrix_on_images(group, images):
    images = tuple(group(image) for image in images)
    form = matrix(QQ, len(images), len(images))
    for i, left in enumerate(images):
        for j, right in enumerate(images):
            form[i, j] = group.q(left) if i == j else group.b(left, right)
    form.set_immutable()
    return form


def _coset_reduce(ambient, relation_subgroup):
    r"""Return ``x |-> min representative of the coset x + H``."""
    relations = relation_subgroup.elements()
    return lambda x: min(
        (ambient(x) + h for h in relations),
        key=lambda element: tuple(element.coefficient_vector()),
    )


def _quotient_closure(reduce, zero, generators):
    r"""BFS closure of ``generators`` under coset addition, keyed by rep coords."""
    seen = {tuple(zero.coefficient_vector()): zero}
    frontier = [zero]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            nxt = reduce(current + generator)
            key = tuple(nxt.coefficient_vector())
            if key not in seen:
                seen[key] = nxt
                frontier.append(nxt)
    return seen


def _induced_subquotient_form(ambient, relation_subgroup, cover_subgroup):
    r"""The finite quadratic form on ``K / H`` (``H ⊆ K ⊆ H``-perp, ``H`` isotropic).

    The ambient bilinear/quadratic form descends to ``K / H``; present it on a
    canonical (min-representative, greedily generated) set as the consolidated
    Gram-presented quadratic form -- the same parent TYPE as every other finite
    quadratic discriminant form. The result is nondegenerate exactly when the
    descended form is; recovering the ``K / H`` group order from the Gram
    denominators is sound only then, so it is asserted.
    """
    reduce = _coset_reduce(ambient, relation_subgroup)
    zero = reduce(ambient.zero())
    representatives = sorted(
        {reduce(element) for element in cover_subgroup.elements()},
        key=lambda element: tuple(element.coefficient_vector()),
    )
    generators = []
    span = {tuple(zero.coefficient_vector())}
    for representative in representatives:
        if tuple(representative.coefficient_vector()) in span:
            continue
        generators.append(representative)
        span = set(_quotient_closure(reduce, zero, generators))
        if len(span) == len(representatives):
            break
    form = _form_matrix_on_images(ambient, generators)
    # lazy import: discriminant_forms imports this module at load time
    from .discriminant_forms import SyntheticQuadraticDiscriminantForm
    result = SyntheticQuadraticDiscriminantForm(form, quadratic_modulus=ambient._quadratic_modulus())
    expected_order = cover_subgroup.cardinality() // relation_subgroup.cardinality()
    assert result.cardinality() == expected_order, (
        "subquotient K/H is degenerate; its group order is not recoverable from the induced "
        f"Gram; |K|/|H|={expected_order}, induced form order={result.cardinality()}; "
        "supply K with K/H nondegenerate"
    )
    return result


class SyntheticDiscriminantGroupElement(Element):
    r"""Element of ``L# / L`` in Smith invariant coordinates."""

    def __init__(self, parent, coordinates):
        Element.__init__(self, parent)
        if isinstance(coordinates, SyntheticDiscriminantGroupElement):
            coordinates = coordinates.coefficient_vector()
        if coordinates == 0:
            coordinates = [ZZ.zero()] * parent.ngens()
        coords = vector(ZZ, coordinates)
        assert len(coords) == parent.ngens(), ("discriminant coordinates must match Smith invariant count; "
        f"invariants={parent.invariants()}, coordinates={coordinates}")
        coords = vector(ZZ, [coords[i] % parent.invariants()[i] for i in range(parent.ngens())])
        coords.set_immutable()
        self._coordinates = coords

    def _repr_(self):
        return repr(self._coordinates)

    def coefficient_vector(self):
        return self._coordinates

    def b(self, other):
        return self.parent().b(self, other)

    def q(self):
        return self.parent().q(self)

    def _add_(self, other):
        return self.parent()(self.coefficient_vector() + other.coefficient_vector())

    def _sub_(self, other):
        return self.parent()(self.coefficient_vector() - other.coefficient_vector())

    def _neg_(self):
        return self.parent()(-self.coefficient_vector())

    def _lmul_(self, scalar):
        return self.parent()(ZZ(scalar) * self.coefficient_vector())

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticDiscriminantGroupElement)
            and self.parent() == other.parent()
            and self.coefficient_vector() == other.coefficient_vector()
        )

    def __hash__(self):
        return hash((self.parent(), tuple(self.coefficient_vector())))


class SyntheticDiscriminantSubgroup:
    r"""Finite subgroup of a synthetic discriminant group."""

    def __init__(self, ambient, gens):
        from .discriminant_forms import SyntheticDiscriminantForm

        assert isinstance(ambient, SyntheticDiscriminantForm), (
            f"discriminant subgroups live in a consolidated finite quotient parent; found={type(ambient)}"
        )
        self._ambient = ambient
        self._gens = tuple(self._coerce(gen) for gen in gens)
        self._elements = tuple(sorted(self._closure(), key=self._element_key))

    def ambient(self):
        return self._ambient

    def gens(self):
        return self._gens

    def elements(self):
        return self._elements

    def cardinality(self):
        return ZZ(len(self.elements()))

    def invariants(self):
        r"""Smith invariants of this subgroup as an abstract group, from an
        ephemeral Sage FGP quotient (generator span over the ambient relations)."""
        from sage.modules.free_module import FreeModule

        ambient_module = FreeModule(ZZ, self.ambient().ngens())
        relations = ambient_module.span(matrix.diagonal(ZZ, self.ambient().invariants()).rows())
        span = ambient_module.span(
            [vector(ZZ, generator.coefficient_vector()) for generator in self.gens()] + list(relations.gens())
        )
        return tuple(span.quotient(relations).invariants())

    def __contains__(self, element):
        return self._element_key(element) in self._key()

    def is_bilinear_isotropic(self):
        return all(
            self.ambient().b(left, right) == 0
            for left in self.elements()
            for right in self.elements()
        )

    def is_quadratic_isotropic(self):
        return all(self.ambient().q(element) == 0 for element in self.elements())

    def orthogonal_submodule(self):
        return self.ambient().orthogonal_submodule_to(self)

    def _key(self):
        return frozenset(self._element_key(element) for element in self.elements())

    def __eq__(self, other):
        return isinstance(other, SyntheticDiscriminantSubgroup) and self.ambient() is other.ambient() and self._key() == other._key()

    def __hash__(self):
        return hash((id(self.ambient()), self._key()))

    def _closure(self):
        if not self._gens:
            return {self.ambient().zero()}
        ranges = [range(self.ambient().order(generator)) for generator in self._gens]
        elements = set()
        for coefficients in product(*ranges):
            element = self.ambient().zero()
            for coefficient, generator in zip(coefficients, self._gens):
                element = element + ZZ(coefficient) * generator
            elements.add(element)
        return elements

    def _coerce(self, element):
        return self.ambient()(element)

    def _element_key(self, element):
        return tuple(self.ambient().coordinates(self._coerce(element)))


class SyntheticDiscriminantAction(DiscriminantActionCarrier):
    r"""Endomorphism of a synthetic discriminant group in invariant coordinates."""

    def __init__(self, discriminant_group, matrix_data):
        from .discriminant_forms import SyntheticDiscriminantForm

        assert isinstance(discriminant_group, SyntheticDiscriminantForm), (
            f"discriminant actions act on a consolidated finite quotient parent; found={type(discriminant_group)}"
        )
        matrix_data = matrix(ZZ, matrix_data)
        assert matrix_data.nrows() == discriminant_group.ngens(), ("action matrix rows must match invariant count; "
        f"rows={matrix_data.nrows()}, invariants={discriminant_group.invariants()}")
        assert matrix_data.ncols() == discriminant_group.ngens(), ("action matrix columns must match invariant count; "
        f"columns={matrix_data.ncols()}, invariants={discriminant_group.invariants()}")
        reduced = matrix(ZZ, matrix_data.nrows(), matrix_data.ncols())
        for i, invariant in enumerate(discriminant_group.invariants()):
            for j in range(matrix_data.ncols()):
                reduced[i, j] = matrix_data[i, j] % invariant
        reduced.set_immutable()
        self._discriminant_group = discriminant_group
        self._matrix = reduced

    @classmethod
    def from_images(cls, discriminant_group, images):
        columns = []
        for image in images:
            columns.extend(_finite_coordinates(discriminant_group, image))
        return cls(discriminant_group, matrix(ZZ, discriminant_group.ngens(), discriminant_group.ngens(), columns).transpose())

    def discriminant_form(self):
        return self._discriminant_group

    def matrix(self):
        return self._matrix

    def __call__(self, element):
        group = self.discriminant_form()
        column = self.matrix() * matrix(ZZ, group.ngens(), 1, _finite_coordinates(group, element))
        return group([column[i, 0] for i in range(group.ngens())])

    def is_identity(self):
        return all(self(element) == element for element in self.discriminant_form().elements())

    def is_automorphism(self):
        group = self.discriminant_form()
        images = {_finite_coordinates(group, self(element)) for element in group.elements()}
        return len(images) == group.cardinality()

    def kernel(self):
        group = self.discriminant_form()
        return SyntheticDiscriminantSubgroup(group, (element for element in group.elements() if self(element) == group.zero()))

    def inverse_image(self, subgroup_or_gens):
        group = self.discriminant_form()
        subgroup = group._subgroup(subgroup_or_gens)
        return SyntheticDiscriminantSubgroup(group, (element for element in group.elements() if self(element) in subgroup))

    def image(self):
        group = self.discriminant_form()
        return SyntheticDiscriminantSubgroup(group, (self(generator) for generator in group.gens()))

    def im_gens(self):
        return self.image().gens()

    def lift(self, element):
        group = self.discriminant_form()
        element = group(element)
        preimages = tuple(candidate for candidate in group.elements() if self(candidate) == element)
        if not preimages:
            raise ValueError(f"element is not in the image of this finite homomorphism: {element}")
        return min(preimages, key=lambda candidate: _finite_coordinates(group, candidate))

    def inverse(self):
        if not (self.is_automorphism()):
            raise ValueError(f"only automorphisms have inverses; matrix={self.matrix()}")
        inverse_images = []
        for generator in self.discriminant_form().gens():
            preimages = tuple(
                element
                for element in self.discriminant_form().elements()
                if self(element) == generator
            )
            assert len(preimages) == 1, ("automorphism inverse must have a unique preimage for each generator; "
            f"generator={generator}, preimages={preimages}")
            inverse_images.append(preimages[0])
        return SyntheticDiscriminantAction.from_images(self.discriminant_form(), inverse_images)

    def preserves_bilinear_form(self):
        group = self.discriminant_form()
        return all(
            group.b(self(left), self(right)) == group.b(left, right)
            for left in group.elements()
            for right in group.elements()
        )

    def preserves_quadratic_form(self):
        group = self.discriminant_form()
        return all(group.q(self(element)) == group.q(element) for element in group.elements())

    def preserves_form(self, kind="quadratic"):
        assert kind in ("quadratic", "bilinear"), (f"form kind must be quadratic or bilinear; found={kind}")
        if kind == "bilinear":
            return self.preserves_bilinear_form()
        return self.preserves_bilinear_form() and self.preserves_quadratic_form()

    def __eq__(self, other):
        return (
            isinstance(other, SyntheticDiscriminantAction)
            and self.discriminant_form() is other.discriminant_form()
            and self.matrix() == other.matrix()
        )

    def __hash__(self):
        return hash((id(self.discriminant_form()), self.matrix()))


class SyntheticOrthogonalGroup(DiscriminantOrthogonalGroupCarrier):
    r"""Finite group wrapper for owned discriminant-form automorphisms."""

    def __init__(self, discriminant_group, actions, close=False):
        self._discriminant_group = discriminant_group
        self._generators = tuple(actions)
        self._actions = self._closure(self._generators) if close else self._generators

    def discriminant_form(self):
        return self._discriminant_group

    def gens(self):
        return self._generators

    def order(self):
        return ZZ(len(self._actions))

    def __iter__(self):
        return iter(self._actions)

    def __len__(self):
        return len(self._actions)

    def __getitem__(self, index):
        return self._generators[index]

    def __call__(self, action):
        action = action if isinstance(action, SyntheticDiscriminantAction) else SyntheticDiscriminantAction(self.discriminant_form(), action)
        assert any(action == group_action for group_action in self._actions), (f"action is not in this orthogonal group: {action.matrix()}")
        return action.matrix()

    def _closure(self, generators):
        identity = SyntheticDiscriminantAction(self.discriminant_form(), identity_matrix(ZZ, self.discriminant_form().ngens()))
        seen = {identity}
        frontier = [identity]
        generators = tuple(generators)
        while frontier:
            current = frontier.pop()
            for generator in generators:
                product_action = SyntheticDiscriminantAction(self.discriminant_form(), generator.matrix() * current.matrix())
                if product_action not in seen:
                    seen.add(product_action)
                    frontier.append(product_action)
        return tuple(sorted(seen, key=lambda action: tuple(action.matrix().list())))


def TorsionQuadraticForm(gram_matrix):
    r"""Public Sage-compatible constructor for an owned finite quadratic form."""
    # lazy import: discriminant_forms imports this module at load time
    from .discriminant_forms import SyntheticQuadraticDiscriminantForm
    return SyntheticQuadraticDiscriminantForm(gram_matrix)


class SyntheticGenus(GenusCarrier):
    r"""Minimal owned genus datum determined by a signature and discriminant form."""

    def __init__(self, discriminant_group, signature_pair, even=True):
        self._discriminant_group = discriminant_group
        self._signature_pair = (ZZ(signature_pair[0]), ZZ(signature_pair[1]))
        self._even = bool(even)

    def discriminant_form(self):
        return self._discriminant_group

    def signature_pair(self):
        return self._signature_pair

    def signature(self):
        return self._signature_pair[0] - self._signature_pair[1]

    def is_even(self):
        return self._even

    def brown_invariant(self):
        return self.discriminant_form().brown_invariant()

    def __eq__(self, other):
        if not isinstance(other, SyntheticGenus):
            return False
        if self.signature_pair() != other.signature_pair() or self.is_even() != other.is_even():
            return False
        left = self.discriminant_form()
        right = other.discriminant_form()
        if left.source_lattice().gram_matrix() == right.source_lattice().gram_matrix():
            return True
        return left.normal_form() == right.normal_form()

    def __repr__(self):
        return (
            "Synthetic genus with signature "
            f"{self.signature_pair()} and discriminant invariants {self.discriminant_form().invariants()}"
        )

