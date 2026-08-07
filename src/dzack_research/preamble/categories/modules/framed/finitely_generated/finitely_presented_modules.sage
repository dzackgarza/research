r"""Finitely presented modules over a base ring.

Defines ``FinitelyPresentedModules`` as the category of finitely presented modules over a base ring $R$,
declaring ``FinitelyGeneratedModules(R)`` in its supercategories.
"""


from typing import Self

from sage.categories.category_types import Category_over_base_ring
from sage.categories.homset import Hom
from sage.misc.cachefunc import cached_method
from sage.categories.morphism import SetMorphism
from sage.matrix.constructor import matrix
from sage.matrix.matrix0 import Matrix
from sage.matrix.special import identity_matrix
from sage.misc.misc_c import prod
from sage.modules.free_module_element import vector
from sage.rings.integer_ring import ZZ
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp

from sage_lattice_category_spike.objects.cardinals import Cardinal
from sage_lattice_category_spike.lexicon import MorphismMatrix
from sage_lattice_category_spike.objects.sets import Sets
from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet


def _presented_on(module: "Module", relations: MorphismMatrix) -> "FinitelyPresentedModule":
    r"""Return the module presented by ``relations`` on ``module``'s generators.

    A presentation is a morphism, so the matrix is turned back into the one it
    is the matrix of; the generating set is ``module``'s own, because a normal
    form of $M$ is written on labels $M$ already names.
    """
    base_ring = module.base_ring()
    codomain = BasedFreeModule(base_ring, module.module_generating_set())
    domain = BasedFreeModule(base_ring, Sets.Δ[relations.nrows() - 1])
    return FinitelyPresentedModule(
        _module_morphism(
            domain,
            codomain,
            dict(
                zip(
                    domain.module_generating_set(),
                    (codomain._from_coordinates(row) for row in relations.rows()),
                )
            ),
        )
    )


def _change_of_module_generators(
    source: "Module",
    target: "Module",
    rows: list,
) -> "ModuleMorphism":
    r"""Return the morphism writing each generator of ``source`` in ``target``'s.

    Row $i$ is the coordinate vector of the image of the $i$-th generator.
    Whether the assignment is a morphism at all is decided by the constructor,
    which checks that every relation of ``source`` is killed -- so a wrong
    transformation matrix is rejected here and not carried onwards.
    """
    return module_homset(source, target)(
        dict(
            zip(
                source.module_generating_set(),
                (target._from_coordinates(row) for row in rows),
            )
        )
    )


class FinitelyPresentedModules(Category_over_base_ring):
    r"""Category of finitely presented modules over a base ring $R$."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented modules"

    def super_categories(self) -> list:
        return [FinitelyGeneratedModules(self.base_ring())]

    class ParentMethods:
        def is_finitely_presented(self: Self) -> bool:
            r"""Return whether this module is finitely presented."""
            return True

        def hermite_form(self: Self) -> "Isomorphism":
            r"""Return the isomorphism $M\to M'$ onto the reduced presentation.

            A normal form of a module is another module of this category
            together with the arrow relating them, and never a matrix: the
            matrix is what presents $M'$, and on its own it names no object
            and no map back.  So this returns the arrow, and $M'$ is read off
            it as ``target()``.

            Which reduction applies is a fact about the base ring -- Hermite
            over a PID, echelon over a field -- and that branch is
            ``MorphismMatrix.normal_form``'s, called here as the
            implementation of the module-level notion.

            The reduced relations span the relations they were reduced from,
            so $M'$ carries $M$'s generators and the arrow is the identity on
            them.  That is the content, not a degeneracy: reducing rows
            changes the presentation and nothing else, and this says so.
            """
            target = _presented_on(self, self.relation_matrix().normal_form())
            unchanged = identity_matrix(self.base_ring(), self.number_of_module_generators()).rows()
            return Isomorphism(
                _change_of_module_generators(self, target, unchanged),
                _change_of_module_generators(target, self, unchanged),
            )

        def invariant_factor_form(self: Self) -> "Isomorphism":
            r"""Return the isomorphism $M\to M'$ onto the invariant factor presentation.

            The Smith form $D=URV$ of the relations $R$ is a normal form of a
            *matrix*; the module it names is $M'=F/\operatorname{rowspace}(D)$,
            and the arrow is $V$.  Row operations ($U$) leave the row space
            alone, so $\operatorname{rowspace}(D)=\operatorname{rowspace}(RV)$
            and right multiplication by $V$ carries $M$'s relations exactly
            onto $M'$'s -- which is what makes $x\mapsto xV$ an isomorphism and
            not merely a map.

            This is where the two cokernels part company.  For $f:A\to B$,
            ``f.cokernel()`` is $\operatorname{coker}(f)$ *on the nose*:
            presented by $f$'s own matrix, framed by $B$'s generators.
            ``f.cokernel().invariant_factor_form()`` is the arrow onto the
            different object presented by the Smith form of that matrix.  They
            are isomorphic and not equal, and everything written on the
            generating set -- a form, a decomposition, a chosen basis -- lives
            on one of them and not the other.  A caller asking for one never
            silently receives the other, because the second is reached only by
            naming this arrow.
            """
            smith, _, right = self._smith()
            target = _presented_on(self, MorphismMatrix(smith))
            return Isomorphism(
                _change_of_module_generators(self, target, right.rows()),
                _change_of_module_generators(
                    target,
                    self,
                    right.inverse().change_ring(self.base_ring()).rows(),
                ),
            )


class FinitelyPresentedModuleElement(Element):
    r"""An element of a presented module, reduced modulo its relations."""

    def __init__(self, parent: "Parent", coordinates: "Vector") -> None:
        Element.__init__(self, parent)
        self._coordinates_ = parent._reduce(coordinates)

    def _coordinates(self) -> "Vector":
        return self._coordinates_

    def _lift(self) -> "ModuleElement":
        return self._coordinates_

    def coefficients(self) -> dict:
        r"""Return $\{g_i:c_i\}$ for this element's reduced coordinates.

        The same question a free module answers, and it has an answer here
        too: reduction modulo the relations leaves coordinates in the chosen
        generating set.  Without it a form on a presented module cannot say
        what its own elements' coefficients are -- it delegates the question
        to the module underneath.
        """
        return {
            generator: coefficient
            for generator, coefficient in zip(
                self.parent().module_generating_set(), self._coordinates_
            )
            if coefficient != 0
        }

    def _add_(self, other: object) -> "FinitelyPresentedModuleElement":
        return self.parent()._from_coordinates(self._coordinates_ + other._coordinates_)

    def _sub_(self, other: object) -> "FinitelyPresentedModuleElement":
        return self.parent()._from_coordinates(self._coordinates_ - other._coordinates_)

    def _neg_(self) -> "FinitelyPresentedModuleElement":
        return self.parent()._from_coordinates(-self._coordinates_)

    def _lmul_(self, factor: "RingElement") -> "FinitelyPresentedModuleElement":
        return self.parent()._from_coordinates(
            self.parent().base_ring()(factor) * self._coordinates_
        )

    _rmul_ = _lmul_

    def _richcmp_(self, other: object, op: int) -> bool:
        return richcmp(self._coordinates_, other._coordinates_, op)

    def __hash__(self) -> int:
        return hash(tuple(self._coordinates_))


class FinitelyPresentedModule(Parent):
    r"""The cokernel of a morphism of finite free modules.

    The relation morphism may have arbitrary rank, so this includes free,
    torsion, and mixed finitely presented modules.  The rows of its matrix are
    relations on the named generators of the codomain.
    """

    Element = FinitelyPresentedModuleElement

    def __init__(self, presentation: "ModuleMorphism") -> None:
        assert isinstance(presentation, (ModuleMorphism, FormMorphism)), (
            "a presentation is a morphism of framed modules"
        )
        codomain = presentation.codomain()
        base_ring = codomain.base_ring()
        relations = presentation.matrix()._sage_matrix().change_ring(base_ring)
        assert relations.ncols() == codomain.module_generating_set().cardinality(), (
            "the presentation matrix does not have the codomain's number of "
            "distinguished generators as its number of columns"
        )
        Parent.__init__(
            self,
            base=base_ring,
            category=FinitelyPresentedModules(base_ring),
        )
        self._presentation = presentation
        self._relations = relations
        assert base_ring is ZZ or base_ring.is_field(), (
            "finitely presented modules currently require ZZ or a field"
        )
        self._normal_form = MorphismMatrix(relations).normal_form()._sage_matrix()
        refine(self, FinitelyPresentedModules(base_ring))
        if base_ring is ZZ and self.is_torsion():
            refine(self, FinitelyPresentedTorsionModules(base_ring))
        source = _underlying_module(codomain)
        source_module_generator_morphism = source.module_generator_morphism()
        quotient_generator_morphism = SetMorphism(
            Hom(
                source_module_generator_morphism.domain(),
                UnderlyingSet(self),
                Sets(),
            ),
            lambda element_of_S: self._from_coordinates(
                _coordinate_vector(
                    source_module_generator_morphism(element_of_S)
                )
            ),
        )
        self._framing_morphism = framing_morphism(
            source,
            self,
            quotient_generator_morphism,
        )

    def framing_morphism(self) -> "FramingMorphism":
        return self._framing_morphism

    def presentation(self) -> "ModuleMorphism":
        return self._presentation

    def relation_matrix(self) -> MorphismMatrix:
        return MorphismMatrix(self._relations)

    def number_of_module_generators(self) -> int:
        return self._relations.ncols()

    def rank(self) -> "Cardinal":
        return self.number_of_module_generators() - self._relations.rank()

    def is_torsion(self) -> bool:
        return self.base_ring() is ZZ and self.rank() == 0

    @cached_method
    def _smith(self) -> tuple:
        r"""Return the Smith normal form $D=URV$ of the relations.

        Every invariant of a presented module -- its invariant factors, its
        torsion freeness, its torsion-free quotient -- is read off this one
        decomposition, so it is computed once and named rather than
        recomputed at each question.
        """
        return self._relations.smith_form()

    def torsion_free_quotient(self) -> "ModuleMorphism":
        r"""Return the projection $M\twoheadrightarrow M/\operatorname{tors}(M)$.

        The Smith form $D=URV$ of the relations puts $M$ in the coordinates
        $y=xV$, where the relations are diagonal: a coordinate with a nonzero
        entry is torsion, one with a zero entry is free.  The projection is
        therefore $V$ restricted to the free columns, and this is the one
        place that computation is done -- every saturation and primitivity
        question routes through it rather than restating it as a matrix
        normal form at the call site.
        """
        smith, _, right = self._smith()
        diagonal = list(smith.diagonal())
        free_columns = [
            column
            for column in range(self._relations.ncols())
            if column >= len(diagonal) or diagonal[column] == 0
        ]
        coordinates = right.matrix_from_columns(free_columns)
        target = BasedFreeModule(
            self.base_ring(), Sets.Δ[len(free_columns) - 1]
        )
        return self.Hom(target)(
            {
                label: zipsum(row, target.module_generators(), target.zero())
                for label, row in zip(self.module_generating_set(), coordinates.rows())
            }
        )

    def is_torsion_free(self) -> bool:
        if self.base_ring() is not ZZ:
            return True
        smith = self._smith()[0]
        return all(abs(entry) == 1 for entry in smith.diagonal() if entry != 0)

    def is_zero(self) -> bool:
        return all(generator == self.zero() for generator in self.module_generators())

    def invariants(self) -> tuple:
        assert self.base_ring() is ZZ, "invariants are defined here over ZZ"
        smith = self._smith()[0]
        return tuple(
            abs(entry) for entry in smith.diagonal() if abs(entry) > 1
        )

    def cardinality(self) -> "Cardinal":
        r"""Return \(|M|\).

        Total, so positive rank is answered rather than refused: a module
        with a free part is countably infinite, not an error.
        """
        if not self.is_torsion():
            return Sets.ℵ[0]
        return Cardinal(prod(self.invariants(), 1))

    def exponent(self) -> "Integer":
        invariants = self.invariants()
        return invariants[-1] if invariants else 1

    def zero(self) -> FinitelyPresentedModuleElement:
        return self._from_coordinates(
            [self.base_ring().zero()] * self.number_of_module_generators()
        )

    def _reduce(self, coordinates: "Vector") -> "Vector":
        result = vector(self.base_ring(), list(coordinates))
        assert len(result) == self.number_of_module_generators(), (
            f"this module has {self.number_of_module_generators()} coordinates, got {len(result)}"
        )
        for row in self._normal_form.rows():
            pivot = next((i for i, entry in enumerate(row) if entry != 0), None)
            if pivot is None:
                continue
            match self.base_ring():
                case ring if ring is ZZ:
                    coefficient = result[pivot] // row[pivot]
                case ring if ring.is_field():
                    coefficient = result[pivot] / row[pivot]
                case _:
                    assert False, (
                        "normal-form reduction currently requires ZZ or a field"
                    )
            result -= coefficient * row
        return result

    def reduce(self, coordinates: "Vector") -> "Vector":
        r"""Return the canonical representative modulo the presentation."""
        return self._reduce(coordinates)

    def _from_coordinates(self, coordinates: "Vector") -> FinitelyPresentedModuleElement:
        return self.element_class(self, coordinates)

    def _element_constructor_(self, x: "Element") -> FinitelyPresentedModuleElement:
        assert isinstance(x, FinitelyPresentedModuleElement) and x.parent() is self, (
            f"{x} is not an element of {self}; construct classes using this "
            "module's generators and explicit sums"
        )
        return x

    def __contains__(self, x: "Element") -> bool:
        return isinstance(x, FinitelyPresentedModuleElement) and x.parent() is self

    def _repr_(self) -> str:
        return (
            f"Finitely presented module on {self.number_of_module_generators()} generators over "
            f"{self.base_ring()}"
        )
