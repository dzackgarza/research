r"""Finitely presented modules over a base ring.

Defines ``FinitelyPresentedModules`` as the category of finitely presented modules over a base ring $R$,
declaring ``FinitelyGeneratedModules(R)`` in its supercategories.
"""


from typing import Protocol, TYPE_CHECKING
from dzack_research.preamble.utilities import zipsum
if TYPE_CHECKING:
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.lexicon import ModuleElement
    from dzack_research.preamble.lexicon import OrderedSet
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.rings.integer import Integer
    from sage.structure.element import Vector
    from sage.structure.parent import ElementConstructorInput, MembershipInput

from dzack_research.preamble.categories.sets.sets import finite_ordered_set
from dzack_research.preamble.refine import refine
if TYPE_CHECKING:
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import Isomorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from sage.structure.element import RingElement
    from sage.rings.ring import Ring

from dzack_research.preamble.categories.rings.rings import OwnedBaseRing
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.owned_category import object_of
from typing import Self

from sage.categories.homset import Hom
from sage.misc.cachefunc import cached_method
from sage.categories.morphism import SetMorphism
from sage.matrix.constructor import matrix
from sage.matrix.matrix0 import Matrix
from sage.matrix.special import identity_matrix
from sage.misc.misc_c import prod
from sage.modules.free_module_element import FreeModuleElement, vector
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import Element as SageElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp

from dzack_research.preamble.categories.sets.cardinals import Cardinal, cardinal
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet


def _presented_on(module: "Module", relations: MorphismMatrix) -> Parent:
    r"""Return the module presented by ``relations`` on ``module``'s generators.

    A presentation is a morphism, so the matrix is turned back into the one it
    is the matrix of; the generating set is ``module``'s own, because a normal
    form of $M$ is written on labels $M$ already names.
    """
    # Local: at module level these close an import cycle; the free module and
    # morphism modules are built by the time a presentation is written.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _module_morphism

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
    # Local: at module level this closes an import cycle; the homset module is
    # built by the time a change of generators is written.
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    return module_homset(source, target)(
        dict(
            zip(
                source.module_generating_set(),
                (target._from_coordinates(row) for row in rows),
            )
        )
    )


if TYPE_CHECKING:
    class PresentedModuleParent(Protocol):
        r"""What a parent placed in ``FinitelyPresentedModules(R)`` supplies:
        the presentation itself, its Smith decomposition, the ring underneath,
        the generator count, and the coordinate route in."""

        def base_ring(self) -> "Ring": ...
        def relation_matrix(self) -> MorphismMatrix: ...
        def number_of_module_generators(self) -> int: ...
        def _smith(self) -> tuple: ...
        def _from_coordinates(self, coordinates: "Vector") -> "Element": ...


class FinitelyPresentedModules(OwnedCategoryOverBaseRing):
    r"""Category of finitely presented modules over a base ring $R$."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented modules"

    def super_categories(self) -> list:
        # Local: at module level this closes an import cycle; the category is
        # built by the time supercategories are asked for.
        from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import FinitelyGeneratedModules

        return [FinitelyGeneratedModules(self.base_ring())]

    class ParentMethods(OwnedBaseRing):
        r"""One presented module: the presenting morphism, and its relations."""

        def __init__(
            self: Self,
            presentation: "ModuleMorphism",
            **rest: "ConstructionData",
        ) -> None:
            r"""Present $N/f(M)$ on the generators of the codomain of $f$."""
            # Local: at module level these close an import cycle; the morphism,
            # form and torsion modules are built by the time one is presented.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import FinitelyPresentedTorsionModules
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import is_form_morphism
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism
            from dzack_research.preamble.categories.rings.rings import engine_ring

            assert isinstance(presentation, ModuleMorphism) or is_form_morphism(presentation), (
                "a presentation is a morphism of framed modules"
            )
            codomain = presentation.codomain()
            # The quotient is over the ring the presented module is over, read
            # as the engine names it: the category is built from this, and a
            # category over one name for a ring holds no object over the other.
            base_ring = engine_ring(codomain.base_ring())
            images = presentation.matrix().change_ring(base_ring)
            assert images.ncols() == codomain.module_generating_set().cardinality(), (
                "the presentation matrix does not have the codomain's number of "
                "distinguished generators as its number of columns"
            )
            # $N/f(M)$ is written on $N$'s generators, so it imposes $N$'s own
            # relations as well as $f$'s images: both are relations among those
            # generators.  A free $N$ answers no relations of its own, which is
            # why the free case needs no separate construction -- it is this one
            # with an empty matrix to stack.
            underlying = codomain
            assert engine_ring(base_ring) is SageZZ or base_ring.is_field(), (
                "finitely presented modules currently require ZZ or a field"
            )
            self._presentation = presentation
            self._relations = (
                underlying.relation_matrix()
                .change_ring(base_ring)
                .stack(images)
                ._sage_matrix()
            )
            super().__init__(base=base_ring, **rest)
            if engine_ring(base_ring) is SageZZ and self.is_torsion():
                refine(self, FinitelyPresentedTorsionModules(base_ring))
            # The classes are named by $N$'s generators, and those generators are
            # named by $N$'s own presenting free module -- itself when $N$ is
            # free, its cover when $N$ is already a quotient.
            source = underlying.framing_morphism().domain()
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

        def relation_matrix(self: "PresentedModuleParent") -> MorphismMatrix:
            r"""Return the relations of the chosen presentation.

            A finitely presented module is a module together with a chosen
            finite presentation, and the rows of this matrix are the relations
            that presentation imposes on the chosen generators.  Every
            invariant below -- rank, torsion, the invariant factors, the
            reduction of a coordinate vector -- is read off it, so it is the
            one route by which the mathematics reaches the presentation.  A
            construction that reaches this category another way states its own
            relations here.
            """
            return MorphismMatrix(self._relations)

        def framing_morphism(self: Self) -> "FramingMorphism":
            return self._framing_morphism

        def presentation(self: Self) -> "ModuleMorphism":
            return self._presentation

        def zero(self: Self) -> "Element":
            return self._from_coordinates(
                [self.base_ring().zero()] * self.number_of_module_generators()
            )

        def _from_coordinates(self: Self, coordinates: "Vector") -> "Element":
            member: "Element" = self.element_class(self, coordinates)
            return member

        def _element_constructor_(self: Self, x: "ElementConstructorInput") -> "Element":
            assert isinstance(x, SageElement) and x.parent() is self, (
                f"{x} is not an element of {self}; construct classes using this "
                "module's generators and explicit sums"
            )
            return x

        def __contains__(self: Self, x: "MembershipInput") -> bool:
            return isinstance(x, SageElement) and x.parent() is self

        def _repr_(self: Self) -> str:
            return (
                f"Finitely presented module on "
                f"{self.number_of_module_generators()} generators over "
                f"{self.base_ring()}"
            )

        def is_finitely_presented(self: "PresentedModuleParent") -> bool:
            r"""Return whether this module is finitely presented."""
            return True

        def number_of_module_generators(self: "PresentedModuleParent") -> int:
            r"""Return the number of generators the presentation is written on."""
            count: int = self.relation_matrix().ncols()
            return count

        def rank(self: "PresentedModuleParent") -> "Cardinal":
            r"""Return the rank of the free part: generators minus independent relations."""
            return (
                self.number_of_module_generators()
                - self.relation_matrix()._sage_matrix().rank()
            )

        def is_torsion(self: "PresentedModuleParent") -> bool:
            # Local: at module level this closes an import cycle; the ring module
            # is built by the time a module answers about its torsion.
            from dzack_research.preamble.categories.rings.rings import engine_ring

            return engine_ring(self.base_ring()) is SageZZ and self.rank() == 0

        @cached_method
        def _smith(self: "PresentedModuleParent") -> tuple:
            r"""Return the Smith normal form $D=URV$ of the relations.

            Every invariant of a presented module -- its invariant factors, its
            torsion freeness, its torsion-free quotient -- is read off this one
            decomposition, so it is computed once and named rather than
            recomputed at each question.
            """
            decomposition: tuple = self.relation_matrix()._sage_matrix().smith_form()
            return decomposition

        @cached_method
        def _relations_normal_form(self: "PresentedModuleParent") -> Matrix:
            r"""Return the relations row-reduced, as the reduction below uses them."""
            reduced: Matrix = self.relation_matrix().normal_form()._sage_matrix()
            return reduced

        def torsion_free_quotient(self: "PresentedModuleParent") -> "ModuleMorphism":
            r"""Return the projection $M\twoheadrightarrow M/\operatorname{tors}(M)$.

            The Smith form $D=URV$ of the relations puts $M$ in the coordinates
            $y=xV$, where the relations are diagonal: a coordinate with a nonzero
            entry is torsion, one with a zero entry is free.  The projection is
            therefore $V$ restricted to the free columns, and this is the one
            place that computation is done -- every saturation and primitivity
            question routes through it rather than restating it as a matrix
            normal form at the call site.
            """
            # Local: at module level this closes an import cycle; the free module
            # is built by the time a quotient is projected onto.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule

            smith, _, right = self._smith()
            diagonal = list(smith.diagonal())
            free_columns = [
                column
                for column in range(self.number_of_module_generators())
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

        def is_torsion_free(self: "PresentedModuleParent") -> bool:
            # Local: at module level this closes an import cycle; the ring module
            # is built by the time a module answers about its torsion.
            from dzack_research.preamble.categories.rings.rings import engine_ring

            if engine_ring(self.base_ring()) is not SageZZ:
                return True
            smith = self._smith()[0]
            return all(abs(entry) == 1 for entry in smith.diagonal() if entry != 0)

        def is_zero(self: "PresentedModuleParent") -> bool:
            return all(generator == self.zero() for generator in self.module_generators())

        def invariants(self: "PresentedModuleParent") -> tuple:
            # Local: at module level this closes an import cycle; the ring module
            # is built by the time invariants are asked for.
            from dzack_research.preamble.categories.rings.rings import engine_ring

            assert engine_ring(self.base_ring()) is SageZZ, "invariants are defined here over ZZ"
            smith = self._smith()[0]
            return tuple(
                abs(entry) for entry in smith.diagonal() if abs(entry) > 1
            )

        def cardinality(self: "PresentedModuleParent") -> "Cardinal":
            r"""Return \(|M|\).

            Total, so positive rank is answered rather than refused: a module
            with a free part is countably infinite, not an error.
            """
            if not self.is_torsion():
                return Sets.ℵ[0]
            return cardinal(prod(self.invariants(), 1))

        def exponent(self: "PresentedModuleParent") -> "Integer":
            invariants = self.invariants()
            return invariants[-1] if invariants else 1

        def _reduce(self: "PresentedModuleParent", coordinates: "Vector") -> "Vector":
            # Local: at module level this closes an import cycle; the ring module
            # is built by the time an element is reduced.
            from dzack_research.preamble.categories.rings.rings import engine_ring

            result = vector(engine_ring(self.base_ring()), list(coordinates))
            assert len(result) == self.number_of_module_generators(), (
                f"this module has {self.number_of_module_generators()} coordinates, got {len(result)}"
            )
            for row in self._relations_normal_form().rows():
                pivot = next((i for i, entry in enumerate(row) if entry != 0), None)
                if pivot is None:
                    continue
                match self.base_ring():
                    case ring if engine_ring(ring) is SageZZ:
                        coefficient = result[pivot] // row[pivot]
                    case ring if ring.is_field():
                        coefficient = result[pivot] / row[pivot]
                    case _:
                        assert False, (
                            "normal-form reduction currently requires ZZ or a field"
                        )
                result -= coefficient * row
            return result

        def reduce(self: "PresentedModuleParent", coordinates: "Vector") -> "Vector":
            r"""Return the canonical representative modulo the presentation."""
            return self._reduce(coordinates)

        def hermite_form(self: "PresentedModuleParent") -> "Isomorphism":
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
            # Local: at module level these close an import cycle; the arrow and
            # ring modules are built by the time a normal form is asked for.
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import Isomorphism
            from dzack_research.preamble.categories.rings.rings import engine_ring

            target = _presented_on(self, self.relation_matrix().normal_form())
            unchanged = identity_matrix(
                engine_ring(self.base_ring()), self.number_of_module_generators()
            ).rows()
            return Isomorphism(
                _change_of_module_generators(self, target, unchanged),
                _change_of_module_generators(target, self, unchanged),
            )

        def smith_form_module_generators(self: "PresentedModuleParent") -> "OrderedSet":
            r"""Return generators realizing the invariant factor decomposition.

            The Smith form $D=URV$ diagonalizes the relations, so the rows of
            $V^{-1}$ are a generating set in which the module is
            $\bigoplus_i R/d_iR$.  The diagonal runs out when there are fewer
            relations than generators, and the generators past it are free:
            $d_i=0$ there, and $R/0R=R$ is the summand each contributes.  A
            generator with $d_i$ a unit spans the zero module and is dropped,
            which is the whole reason this is a different generating set from
            the presented one and not a change of basis of it.
            """
            # Local: at module level this closes an import cycle; the ring
            # module is built by the time generators are asked for.
            from dzack_research.preamble.categories.rings.rings import engine_ring

            smith, _, right = self._smith()
            coordinates = right.inverse().change_ring(engine_ring(self.base_ring())).rows()
            invariants = list(smith.diagonal())
            invariants += [self.base_ring().zero()] * (
                self.number_of_module_generators() - len(invariants)
            )
            return finite_ordered_set(
                tuple(
                    self._from_coordinates(coordinates[index])
                    for index, invariant in enumerate(invariants)
                    if invariant != 1
                )
            )

        def invariant_factor_form(self: "PresentedModuleParent") -> "Isomorphism":
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
            # Local: at module level these close an import cycle; the arrow and
            # ring modules are built by the time a normal form is asked for.
            from dzack_research.preamble.categories.abstract_categories.arrow_categories import Isomorphism
            from dzack_research.preamble.categories.rings.rings import engine_ring

            smith, _, right = self._smith()
            target = _presented_on(self, MorphismMatrix(smith))
            return Isomorphism(
                _change_of_module_generators(self, target, right.rows()),
                _change_of_module_generators(
                    target,
                    self,
                    right.inverse().change_ring(engine_ring(self.base_ring())).rows(),
                ),
            )

    class ElementMethods:
        r"""A class of a presented module, reduced modulo its relations."""

        def __init__(
            self: Self,
            parent: Parent,
            coordinates: "Vector",
            **rest: "ConstructionData",
        ) -> None:
            self._coordinates_: FreeModuleElement = parent._reduce(coordinates)
            super().__init__(parent, **rest)

        def additive_order(self: Self) -> "Integer":
            r"""Return the additive order of this class.

            Read off the invariant factors, which a torsion module has.  A
            module with a free part has classes of infinite order, and a
            presentation does not name that order.
            """
            # Local: the torsion category imports this module to build its
            # parent, so the category owner is available when this runs.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_torsion_modules import FinitelyPresentedTorsionModules

            assert self.parent().is_torsion(), (
                "an additive order is read off the invariant factors of a "
                "torsion module"
            )
            order: "Integer" = FinitelyPresentedTorsionModules.ElementMethods.additive_order(self)
            return order

        def _coordinates(self: Self) -> "Vector":
            return self._coordinates_

        def _lift(self: Self) -> "ModuleElement":
            return self._coordinates_

        def coefficients(self: Self) -> dict:
            r"""Return $\{g_i:c_i\}$ for this class's reduced coordinates.

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

        def _add_(self: Self, other: Self) -> "Element":
            return self.parent()._from_coordinates(
                self._coordinates_ + other._coordinates_
            )

        def _sub_(self: Self, other: Self) -> "Element":
            return self.parent()._from_coordinates(
                self._coordinates_ - other._coordinates_
            )

        def _neg_(self: Self) -> "Element":
            return self.parent()._from_coordinates(-self._coordinates_)

        def _lmul_(self: Self, factor: "RingElement") -> "Element":
            return self.parent()._from_coordinates(
                self.parent().base_ring()(factor) * self._coordinates_
            )

        _rmul_ = _lmul_

        def _richcmp_(self: Self, other: Self, op: int) -> bool:
            return richcmp(self._coordinates_, other._coordinates_, op)

        def __hash__(self: Self) -> int:
            return hash(tuple(self._coordinates_))


def FinitelyPresentedModule(presentation: "ModuleMorphism") -> Parent:
    r"""Return the cokernel $N/f(M)$ of a morphism $f$ of framed modules.

    The relation morphism may have arbitrary rank, so this includes free,
    torsion, and mixed finitely presented modules.  The rows of its matrix are
    relations on the named generators of the codomain, and the codomain's own
    relations are relations on those generators too -- so $N$ itself may be a
    quotient, and $K/H$ for $H\subseteq K$ two finite torsion modules is this
    construction as much as $L^{\vee}/L$ is.
    """
    # Local: at module level this closes an import cycle; the ring module is
    # built by the time a presentation is written.
    from dzack_research.preamble.categories.rings.rings import engine_ring

    base_ring = engine_ring(presentation.codomain().base_ring())
    return object_of(
        FinitelyPresentedModules(base_ring), presentation=presentation
    )
