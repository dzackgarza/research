r"""Morphisms of modules with generating sets.

Their own layer, because a morphism is not an accessory of the object it
happens to be built for: cokernels are presented by one, forms are pulled back
along one, subobjects are one, and the numerical work of this universe belongs
here rather than in any of them.  Objects hold generators and relations and
answer questions about themselves; morphisms are where coordinates, matrices
and linear systems live, so that there is one place to read when asking whether
a computation is the mathematics it claims to be.

A morphism is an assignment on the domain's generators.  What its matrix means,
and which matrix operations are legitimate, depends on which of three cases it
is in:

**free to free.**  The matrix is the morphism, entry for entry; ordinary
integer linear algebra applies, and this is where most of it is quarantined.

**free to torsion.**  The assignment still determines the map, but the matrix
does not determine its entries: a row is the image's coordinates in generators
of orders $d_1,\dots,d_n$, so the $i$-th column is defined only modulo $d_i$.
Operations that mix columns -- inversion, a determinant, a transpose fed back
in -- are not operations on the morphism, and a value read off such a product
is not a value of anything.  What survives is what is invariant under changing
each column by its own $d_i$.

**torsion to torsion.**  As above, and the domain is presented too, so an
assignment is a morphism only if it kills the relations.  That is a condition
on the assignment, checked where the assignment is made.
"""

from typing import Any

from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement, vector


class ModuleHomset:
    """The owned homset of two framed modules."""

    def __init__(self, domain: Any, codomain: Any) -> None:
        self._domain = domain
        self._codomain = codomain

    def domain(self) -> Any:
        return self._domain

    def codomain(self) -> Any:
        return self._codomain

    def __call__(self, assignment: dict) -> "ModuleMorphism":
        return ModuleMorphism(assignment, parent=self)

    def __contains__(self, morphism: Any) -> bool:
        return isinstance(morphism, ModuleMorphism) and morphism.parent() is self

    def __repr__(self) -> str:
        return f"Hom({self._domain}, {self._codomain})"


def _module_morphism(assignment: dict) -> "ModuleMorphism":
    sources = tuple(assignment)
    assert sources, "a morphism needs its values on the generators"
    return ModuleHomset(sources[0].parent(), next(iter(assignment.values())).parent())(
        assignment
    )


def _coordinate_vector(element: Any) -> FreeModuleElement:
    r"""Return ``element``'s coordinates in its own module's generating set.

    Owned elements report their coordinates, while a class in a quotient
    reports its canonical lift.  Anything else has no generating set to be
    coordinates in, and guessing by which methods it happens to answer to is
    how a foreign object gets read as though it were one of ours.
    """
    if isinstance(element, (FormModuleElement, BasedFreeModuleElement)):
        return element._coordinates()
    if isinstance(element, (TorsionModuleElement, FinitelyPresentedModuleElement)):
        return vector(element._lift())
    assert False, (
        f"{element} is a {type(element).__name__}, which has no generating set "
        "for its entries to be coordinates in"
    )


def _is_torsion(module: Any) -> bool:
    r"""Return whether ``module`` lies over a quotient rather than a free module."""
    underlying = module.forget_form() if isinstance(module, FormModule) else module
    return isinstance(underlying, TorsionModule) or (
        isinstance(underlying, FinitelyPresentedModule)
        and underlying.is_torsion()
    )


def _independent_generators(ambient: Any, generators: Any) -> list:
    r"""Return an independent generating set for the submodule these span.

    A list of elements spans a submodule whether or not it is independent, and
    the submodule is free either way -- but a *presentation* of it on dependent
    generators would carry relations the object does not have.  So the span is
    taken first: the Hermite form of the coordinates is a basis of the same
    submodule, and its rows name the generators the subobject is built on.
    """
    generators = list(generators)
    if not generators:
        return []
    base_ring = ambient.base_ring()
    rows = matrix(base_ring, [_coordinate_vector(g) for g in generators])
    if base_ring is ZZ:
        independent = rows.hermite_form(include_zero_rows=False).rows()
    else:
        independent = tuple(
            row for row in rows.echelon_form().rows() if not row.is_zero()
        )
    return [
        _combination(ambient, row)
        for row in independent
    ]


class ModuleMorphism:
    r"""$f: A\to B$, given as $\{a_i\mapsto f(a_i)\}$ on $A$'s generators.

    A map out of a module generated by $\{a_i\}$ is exactly that assignment, so
    the assignment is the datum and nothing else has to be supplied: $A$ is
    where the generators live and $B$ is where the images live, both read off
    the elements themselves.  The matrix -- the images' coordinates, one per
    row -- is a reading of the morphism, which is what algorithms that want
    coordinates call for.
    """

    def __init__(self, assignment: dict, parent: ModuleHomset) -> None:
        sources = tuple(assignment)
        assert sources, "a morphism needs its values on the generators"
        domain = sources[0].parent()
        codomain = next(iter(assignment.values())).parent()
        assert all(source.parent() is domain for source in sources), (
            "the generators assigned come from more than one module"
        )
        assert all(image.parent() is codomain for image in assignment.values()), (
            "the images land in more than one module"
        )
        generators = tuple(domain.gens())
        assert set(sources) == set(generators), (
            f"a map out of this module is an assignment on all {len(generators)} "
            f"of its generators, got {len(sources)}"
        )
        self._domain = domain
        self._codomain = codomain
        self._assignment = dict(assignment)
        self._parent = parent
        assert parent.domain() is domain and parent.codomain() is codomain

    @classmethod
    def zero(cls, domain: Any, codomain: Any) -> "ModuleMorphism":
        r"""Return the unique map from a named zero module."""
        assert not tuple(domain.gens()), "the zero morphism needs a zero domain"
        return ZeroModuleMorphism(domain, codomain, parent=ModuleHomset(domain, codomain))

    def domain(self) -> Any:
        return self._domain

    def parent(self) -> Any:
        return self._parent

    def codomain(self) -> Any:
        return self._codomain

    def images(self) -> tuple:
        r"""Return $f$ on the generators, one per generator of the domain.

        Looked up rather than listed, because a generating set can repeat an
        element -- the five generators of $A_5$'s $2$-primary part span $\mathbb
        Z/2$ -- and then the assignment has fewer entries than the module has
        generators while still saying where each one goes.
        """
        return tuple(
            self._assignment[generator] for generator in self._domain.gens()
        )

    def matrix(self) -> Matrix:
        r"""Return the images' coordinates, one row per generator of the domain."""
        images = self.images()
        if not images:
            return matrix(
                self._codomain.base_ring(), 0, len(tuple(self._codomain.gens()))
            )
        return matrix([_coordinate_vector(image) for image in images])

    def __call__(self, x: Any) -> Any:
        r"""Return $f(x)=\sum_i a_i f(g_i)$ for $x=\sum_i a_i g_i$.

        The definition rather than a matrix product read into the codomain:
        the coefficients are $x$'s, asked of $x$, and what they multiply are
        the images, which are already elements of the codomain.  So nothing
        here has to be interpreted as belonging anywhere -- the arithmetic is
        the codomain's own.
        """
        assert x.parent() is self._domain, (
            f"{x} belongs to {x.parent()}, and this morphism is defined on "
            f"{self._domain}"
        )
        total = self._codomain.zero()
        for coefficient, image in zip(_coordinate_vector(x), self.images()):
            total += coefficient * image
        return total

    def lift(self, y: Any) -> Any:
        r"""Return an $x$ in the domain with $f(x)=y$, or fail because there is none.

        The one place a preimage is computed.  Writing $x=\sum_ia_ig_i$, the
        equation $f(x)=y$ says $aM=t$ *in the codomain*, and what that means is
        the case distinction of this module:

        - a free codomain makes it the integer system $aM=t$;
        - a torsion codomain makes it $aM\equiv t$ modulo the relations, which
          is the integer system $aM+zR=t$ in the unknowns $(a,z)$.

        Both are solved by the same routine below, the second by stacking $R$,
        and neither by a rule about which representative is canonical.  A
        canonical representative is a fact about printing and equality; that it
        also happens to be a preimage is a theorem, and one this code should
        not be quietly asserting -- so the answer here is whatever solves the
        system, and the assertion at the end is what makes it checkable.

        A choice, not a map.  $f$ being surjective does not split it, so
        nothing here is natural in $y$: two calls may legitimately differ, and
        anything computed from a lift that is not invariant under changing it
        depends on this computation and not on $y$ alone.
        """
        assert y.parent() is self._codomain, (
            f"{y} lies in {y.parent()}, and this morphism lands in "
            f"{self._codomain}"
        )
        system = self.matrix()
        relations = self._codomain_relations()
        coefficients = _solve_left_integrally(
            system.stack(relations) if relations.nrows() else system,
            _coordinate_vector(y),
        )
        x = _combination(self._domain, coefficients[: system.nrows()])
        assert self(x) == y, (
            f"{y} is not in the image of this morphism: the system is solved "
            f"by {x}, whose image is {self(x)}"
        )
        return x

    def kernel(self) -> "Subobject":
        r"""Return $\ker f\hookrightarrow A$, as the inclusion it is.

        A subobject is its inclusion (#25), so what is returned is the map and
        not a set of vectors: $\ker f$ is an object in its own right, with its
        own generators, and the only thing relating it to $A$ is where those
        generators go.

        Free domain and free codomain, which is where this is defined.  Then
        $x=\sum_ia_ig_i$ is killed exactly when $aM=0$, so the kernel's
        generators are a basis of the left kernel of $M$ -- an integral, hence
        saturated, basis, which is why $A/\ker f$ comes out torsion free.  Over
        a torsion domain the same equation reads modulo the relations and the
        solution set is not free, so this refuses rather than returning
        something of the wrong kind.

        The domain's form, if it has one, restricts to the kernel: the
        generators are elements of $A$ and the form is evaluated on them.  That
        restriction can be degenerate even when $A$'s form is not.
        """
        domain = self._domain
        assert not _is_torsion(domain), (
            f"kernel is defined here for a free domain, and {domain} is a "
            "quotient: the equation aM = 0 reads modulo its relations, and its "
            "solutions do not form a free module. The kernel of a map of "
            "finitely presented torsion modules is a further presentation, "
            "which is a different construction."
        )
        basis = self.matrix().left_kernel_matrix().rows()
        return domain.subobject_on([_combination(domain, row) for row in basis])

    def cokernel(self) -> Any:
        r"""Return $B/\operatorname{im} f$, presented by $f$ itself.

        Which is what a cokernel is: the codomain modulo the images of the
        domain's generators, and $f$ is exactly the list of those images.  So
        nothing is computed here -- the presentation morphism is this morphism,
        and the quotient reads its relations off it.

        A form on $B$ descends only when it is constant on cosets, which is a
        condition on $f$ and is asserted where the quotient's form is built.
        This returns the module; the form-bearing quotients are
        :meth:`DiscriminantBilinearModules.cokernel` and its quadratic sibling,
        which are this together with that check.
        """
        return TorsionModule(self)

    def image(self) -> "Subobject":
        r"""Return $\operatorname{im} f\hookrightarrow B$, as the inclusion it is.

        The submodule generated by the images, which may be dependent -- $f$
        need not be injective -- so the span is taken and the subobject is
        built on an independent generating set of it.  It is the image as a
        subobject, not a claim that the domain maps onto it isomorphically.
        """
        return self._codomain.subobject_on(list(self.images()))

    def index(self) -> Any:
        r"""Return the finite index of the image of this morphism.

        For a morphism $f:A\to B$, this is $[B:\operatorname{im} f]$, when
        that quotient is finite.  Over $\mathbb Z$ it is the determinant of a
        full-rank basis of the image lattice; for a finitely presented torsion
        codomain it is the cardinality of the presented quotient.  Over a
        field, every full-rank image is all of the codomain and has index one.
        A rank-deficient image has no finite index and is rejected.
        """
        codomain = self._codomain
        module = codomain.forget_form() if isinstance(codomain, FormModule) else codomain
        image = self.matrix()
        width = len(tuple(module.gens()))
        if isinstance(module, (TorsionModule, FinitelyPresentedModule)):
            relations = module.relation_matrix()
            rows = relations.stack(image) if image.nrows() else relations
            basis = rows.hermite_form(include_zero_rows=False)
            assert basis.nrows() == width, (
                "the image does not have finite index in the torsion codomain"
            )
            return abs(basis.det())

        assert image.ncols() == width, "the morphism matrix has the wrong codomain rank"
        if module.base_ring() is ZZ:
            basis = image.hermite_form(include_zero_rows=False)
            assert basis.nrows() == width, (
                "the image does not have finite index in the free codomain"
            )
            return abs(basis.det())

        assert image.rank() == width, (
            "the image does not have finite index in the free codomain"
        )
        return ZZ.one()

    def orthogonal_complement(self) -> "Subobject":
        r"""Return $(\operatorname{im} f)^{\perp}\hookrightarrow B$.

        $\{y\in B: b(y,f(x))=0 \text{ for all } x\}$, which by bilinearity is
        the condition on the images of the domain's generators alone.  In
        coordinates $y$ has $cG M^{\mathsf T}=0$ for $M$ the morphism's matrix
        and $G$ the codomain's Gram matrix, so the complement's generators are
        a basis of that left kernel.

        Of the *image*, not of the domain: what a subspace is perpendicular to
        is a subobject of $B$, and $f$ names one.  This is how $e^{\perp}$ is
        asked for -- the inclusion of $\mathbb Ze$ has $e$ as its image, and
        its complement in $U\oplus E_8$ is the rank-9 sublattice, degenerate
        because $e$ is isotropic and so lies in its own complement.  A
        complement being degenerate is ordinary and is not an error.
        """
        codomain = self._codomain
        assert not _is_torsion(codomain), (
            f"orthogonal complement is defined here in a free codomain, and "
            f"{codomain} is a quotient"
        )
        pairing = matrix(codomain.gram_matrix()) * self.matrix().transpose()
        basis = pairing.left_kernel().basis()
        return codomain.subobject_on(
            [_combination(codomain, row) for row in basis]
        )

    def _codomain_relations(self) -> Matrix:
        r"""Return the codomain's relations, or no rows when it is free.

        Which of the three cases this morphism is in, asked of the codomain.
        """
        codomain = self._codomain
        module = codomain.forget_form() if isinstance(codomain, FormModule) else codomain
        if isinstance(module, (TorsionModule, FinitelyPresentedModule)):
            return module.relation_matrix()
        return matrix(ZZ, 0, len(tuple(codomain.gens())))

    def __repr__(self) -> str:
        return (
            f"Module morphism on {len(self._assignment)} generators into "
            f"{self._codomain}"
        )

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, ModuleMorphism)
            and self._domain is other._domain
            and self._codomain is other._codomain
            and self.images() == other.images()
        )

    def __hash__(self) -> int:
        return hash((
            id(self._domain),
            id(self._codomain),
            tuple(tuple(_coordinate_vector(image)) for image in self.images()),
        ))


class ZeroModuleMorphism(ModuleMorphism):
    r"""The unique morphism out of a named zero module.

    This is a separate semantic object, not an empty assignment passed to the
    generator-image constructor.
    """

    def __init__(self, domain: Any, codomain: Any, parent: ModuleHomset) -> None:
        assert not tuple(domain.gens()), "the zero morphism needs a zero domain"
        self._domain = domain
        self._codomain = codomain
        self._assignment = {}
        self._parent = parent


class ModuleAutomorphism(ModuleMorphism):
    r"""An invertible module map, declared by images of generators.

    ``matrix()`` is deliberately only a view.  There is no constructor taking
    a matrix: the assignment on the chosen generators is the declaration of
    the map.
    """

    def __init__(
        self, assignment: dict, parent: ModuleHomset
    ) -> None:
        ModuleMorphism.__init__(self, assignment, parent=parent)
        assert self.domain() is self.codomain(), (
            "an automorphism must have the same module as domain and codomain"
        )
        determinant = self.matrix().det()
        if self.domain().base_ring() is ZZ:
            assert determinant in (ZZ.one(), -ZZ.one()), (
                "an automorphism of a free ZZ-module must have determinant "
                f"1 or -1, got {determinant}"
            )
        else:
            assert determinant != 0, (
                "the images of the generators do not define an invertible map"
            )

    @classmethod
    def identity(cls, module: Any, parent: ModuleHomset) -> "ModuleAutomorphism":
        r"""Return the identity of the explicitly named module."""
        generators = tuple(module.gens())
        if not generators:
            return ZeroModuleAutomorphism(module, parent=parent)
        return cls(dict(zip(generators, generators)), parent=parent)

    def __mul__(self, other: Any) -> "ModuleAutomorphism":
        assert isinstance(other, ModuleAutomorphism), (
            "composition is defined for module automorphisms"
        )
        assert self.domain() is other.codomain(), (
            "the codomain of the right map must be the domain of the left map"
        )
        generators = tuple(other.domain().gens())
        images = [self(other(generator)) for generator in generators]
        if not generators:
            return ModuleAutomorphism.identity(other.domain(), parent=self.parent())
        return ModuleAutomorphism(dict(zip(generators, images)), parent=self.parent())

    def inverse(self) -> "ModuleAutomorphism":
        r"""Return the inverse, reconstructed from its generator images."""
        inverse_matrix = self.matrix().inverse()
        images = [
            self.domain().linear_combination(row)
            for row in inverse_matrix.rows()
        ]
        assert all(
            coordinate in self.domain().base_ring()
            for image in images
            for coordinate in _coordinate_vector(image)
        ), "the inverse does not have coefficients in the module's base ring"
        if not self.domain().gens():
            return ModuleAutomorphism.identity(self.domain(), parent=self.parent())
        return ModuleAutomorphism(
            dict(zip(self.domain().gens(), images)), parent=self.parent()
        )

    def cyclic_subgroup(self) -> "ModuleAutomorphismGroup":
        r"""Return the literal subgroup generated by this automorphism."""
        return self.domain().Aut().subgroup([self])


class ZeroModuleAutomorphism(ModuleAutomorphism):
    r"""The identity automorphism of a named zero module."""

    def __init__(self, module: Any, parent: ModuleHomset) -> None:
        assert not tuple(module.gens()), "the zero automorphism needs a zero module"
        self._domain = module
        self._codomain = module
        self._assignment = {}
        self._parent = parent


class ModuleAutomorphismGroup:
    r"""The automorphism homset, or a finite subgroup of it.

    Elements of a generated subgroup are ``ModuleAutomorphism`` objects
    themselves.  No abstract group is substituted for the subgroup of
    ``Aut(M)``.
    """

    def __init__(self, module: Any, generators: Any = None) -> None:
        self._module = module
        self._generators = None if generators is None else tuple(generators)
        if self._generators is not None:
            assert self._generators, "a generated subgroup needs a generator"
            assert all(
                isinstance(generator, ModuleAutomorphism)
                and generator.domain() is module
                and generator.codomain() is module
                for generator in self._generators
            ), "subgroup generators must be automorphisms of this module"
            self._elements = self._close()
        else:
            self._elements = None

    def module(self) -> Any:
        return self._module

    def domain(self) -> Any:
        return self._module

    def codomain(self) -> Any:
        return self._module

    def __call__(self, images: Any) -> ModuleAutomorphism:
        if isinstance(images, dict):
            assignment = images
        else:
            images = tuple(images)
            assert len(images) == self._module.rank(), (
                f"this module has {self._module.rank()} generators, got "
                f"{len(images)} images"
            )
            assignment = dict(zip(self._module.gens(), images))
        if not assignment:
            assert self._module.rank() == 0, (
                "an automorphism must be declared by images of generators"
            )
            return ModuleAutomorphism.identity(self._module, parent=self)
        return ModuleAutomorphism(assignment, parent=self)

    def subgroup(self, generators: Any) -> "ModuleAutomorphismGroup":
        return ModuleAutomorphismGroup(self._module, generators)

    def one(self) -> ModuleAutomorphism:
        return ModuleAutomorphism.identity(self._module, parent=self)

    def gens(self) -> tuple:
        if self._generators is None:
            return ()
        return self._generators

    def is_finite(self) -> bool:
        return self._elements is not None

    def order(self) -> int:
        assert self.is_finite(), "the full automorphism homset is not finite"
        return len(self._elements)

    def __iter__(self):
        assert self.is_finite(), "the full automorphism homset is not enumerable"
        return iter(self._elements)

    def __contains__(self, element: Any) -> bool:
        if self.is_finite():
            return element in self._elements
        return isinstance(element, ModuleAutomorphism) and element.parent() is self

    def irreducible_characters(self) -> tuple:
        r"""Return characters for a cyclic literal automorphism subgroup.

        The character values are functions on this subgroup's actual
        automorphisms.  No isomorphic replacement group is exposed.
        """
        assert self.is_finite(), "characters require a finite subgroup"
        assert len(self._generators) == 1, (
            "character tables for generated automorphism subgroups currently "
            "require a cyclic subgroup"
        )
        return tuple(
            _AutomorphismCharacter(self, index)
            for index in range(self.order())
        )

    def trivial_character(self) -> Any:
        return self.irreducible_characters()[0]

    def _close(self) -> tuple:
        identity = self.one()
        elements = {identity}
        frontier = [identity]
        steps = 0
        while frontier:
            current = frontier.pop()
            for generator in self._generators:
                for factor in (generator, generator.inverse()):
                    candidate = current * factor
                    if candidate in elements:
                        continue
                    elements.add(candidate)
                    frontier.append(candidate)
                    steps += 1
                    assert steps <= 100000, (
                        "the proposed subgroup has not closed after 100000 "
                        "elements; it is not a finite subgroup"
                    )
        return tuple(elements)

    def __repr__(self) -> str:
        if self.is_finite():
            return f"Subgroup of Aut({self._module}) of order {self.order()}"
        return f"Aut({self._module})"


class _AutomorphismCharacter:
    """A character of a cyclic subgroup, evaluated on its automorphisms."""

    def __init__(self, group: ModuleAutomorphismGroup, index: int) -> None:
        self._group = group
        self._index = index
        generator = group._generators[0]
        current = group.one()
        self._powers = {}
        for power in range(group.order()):
            self._powers[current] = power
            current = current * generator

    def __call__(self, element: Any) -> Any:
        assert element in self._powers, "the element is outside this character's group"
        power = self._powers[element]
        order = self._group.order()
        if order <= 2:
            return QQ.one() if self._index == 0 or power == 0 else QQ(-1)
        root = CyclotomicField(order).gen()
        return root ** (self._index * power)

    def degree(self) -> int:
        return 1

    def __repr__(self) -> str:
        return f"character {self._index} of {self._group}"

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, _AutomorphismCharacter)
            and self._group is other._group
            and self._index == other._index
        )

    def __hash__(self) -> int:
        return hash((id(self._group), self._index))


class GroupAction:
    r"""A semantic homomorphism from a finite group to ``Aut(M)``."""

    def __init__(self, group: Any, module: Any, values: dict) -> None:
        assert group.is_finite(), "a group action here must have a finite group"
        assert set(values) == set(group), (
            "a semantic group action must name the image of every group element"
        )
        assert all(
            isinstance(value, ModuleAutomorphism)
            and value.domain() is module
            and value.codomain() is module
            for value in values.values()
        ), "the action values must be automorphisms of the supplied module"
        identity = group.one()
        assert values[identity] == module.Aut().one(), (
            "the identity of the group must map to the identity automorphism"
        )
        for left in group:
            for right in group:
                assert values[left * right] == values[left] * values[right], (
                    "the supplied map is not a group homomorphism into Aut(M)"
                )
        self._group = group
        self._module = module
        self._values = dict(values)

    @classmethod
    def from_generators(
        cls, group: Any, module: Any, generator_images: Any
    ) -> "GroupAction":
        assert group.is_finite(), "a group action here must have a finite group"
        generators = tuple(group.gens())
        images = tuple(generator_images)
        assert len(images) == len(generators), (
            f"{group} has {len(generators)} generators, got {len(images)} images"
        )
        assert all(
            isinstance(image, ModuleAutomorphism)
            and image.domain() is module
            and image.codomain() is module
            for image in images
        ), "the generator images must be automorphisms of the supplied module"
        values = {group.one(): module.Aut().one()}
        frontier = [group.one()]
        while frontier:
            current = frontier.pop()
            for generator, image in zip(generators, images):
                product = current * generator
                candidate = values[current] * image
                if product in values:
                    assert values[product] == candidate, (
                        "the declared generator images do not respect the "
                        "relations of the supplied group"
                    )
                    continue
                values[product] = candidate
                frontier.append(product)
        return cls(group, module, values)

    def domain(self) -> Any:
        return self._group

    def codomain(self) -> ModuleAutomorphismGroup:
        return self._module.Aut()

    def module(self) -> Any:
        return self._module

    def __call__(self, element: Any) -> ModuleAutomorphism:
        return self._values[element]

    def values(self) -> dict:
        return dict(self._values)


def _combination(module: Any, coefficients: Any) -> Any:
    r"""Return $\sum_i a_ig_i$ over ``module``'s generators.

    Written out rather than delegated to the object, because not every module a
    morphism can start from is one of ours: Sage's own ``linear_combination``
    takes pairs, so calling it here with a coefficient vector would mean
    something else entirely on a lattice.  Adding and scaling generators is a
    thing every module does the same way.
    """
    generators = tuple(module.gens())
    coefficients = tuple(coefficients)
    assert len(coefficients) == len(generators), (
        f"{module} has {len(generators)} generators, got {len(coefficients)} "
        "coefficients"
    )
    total = module.zero()
    for coefficient, generator in zip(coefficients, generators):
        total += module.base_ring()(coefficient) * generator
    return total


def _solve_left_integrally(system: Matrix, target: Any) -> Any:
    r"""Return an integral $a$ with $aS=t$, or fail because there is none.

    Smith form: with $D=US^{\mathsf T}V$ diagonal, $S^{\mathsf T}a=t$ becomes
    $Dw=Ut$ for $w=V^{-1}a$, which is one exact division per row.  Exactness is
    the point -- a rational solve answers a different question, and over
    $\mathbb Z$ the difference between "solvable" and "solvable after clearing
    a denominator" is the whole content.
    """
    smith, left, right = system.transpose().smith_form()
    shifted = left * vector(ZZ, target)
    width = smith.ncols()
    solution = [ZZ.zero()] * width
    for i, value in enumerate(shifted):
        divisor = smith[i, i] if i < width else ZZ.zero()
        assert divisor != 0 or value == 0, (
            f"no solution: row {i} of the system is zero but asks for {value}"
        )
        if divisor != 0:
            assert value % divisor == 0, (
                f"no integral solution: row {i} asks for {value}/{divisor}, "
                "which solves over Q and not over Z"
            )
            solution[i] = value // divisor
    return right * vector(ZZ, solution)
