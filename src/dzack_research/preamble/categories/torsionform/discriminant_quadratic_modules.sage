r"""Discriminant quadratic modules.

A sibling of :mod:`discriminant_bilinear_modules`, not a refinement of it.  A
quadratic torsion module's data is $q$; $b_q$ is derived from it by
polarization, which is a functor and not an inclusion -- distinct $q$ can share
a $b$ (Peters--Sterk Sec. 12.5 [PS24]), so an object cannot be both.

Objects are :class:`TorsionQuadraticForm`, this package's own.  Sage's
``TorsionQuadraticModule`` carries $b$ and $q$ together, distinguished by a pair
of moduli, and is not refined into this category.
"""

from typing import Any

from sage.categories.category import Category
from sage.groups.additive_abelian.qmodnz import QmodnZ, QmodnZ_Element
from sage.matrix.matrix0 import Matrix
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.fg_pid.fgp_morphism import FGP_Morphism
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module import FreeModule
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric,
)
from sage.rings.rational_field import QQ


class TorsionQuadraticFormElement(FormModuleElement):
    r"""A class $\bar x\in\operatorname{coker} c$ carrying $q$.

    Its own type, distinct from the bilinear one: the two answer different
    questions -- $q$ into $\mathbb Q/2\mathbb Z$ against $b$ into
    $\mathbb Q/\mathbb Z$ -- and are not interchangeable.
    """


class TorsionQuadraticForm(FormModule):
    r"""$(\operatorname{coker} c,\; q)$ for the correlation $c: L\to L^\vee$ of an even $L$.

    The mirror of :func:`TorsionBilinearForm`, built the same way from the same
    morphism; what differs is the form, and with it the value group and the
    category.

    Its own type rather than Sage's ``TorsionQuadraticModule``, which holds $b$
    and $q$ at once and tells them apart by a pair of moduli.  Here the type
    does that, so there is no ``modulus_qf`` to carry, no ``value_module_qf``,
    and no accessor that answers a question this object does not have.

    Carries no methods of its own -- they are :class:`DiscriminantQuadraticModules`'s.  The type exists
    so the object has a name, for annotations and for ``isinstance``.
    """

    Element = TorsionQuadraticFormElement


class DiscriminantQuadraticModules(Category):
    r"""Category of discriminant quadratic modules.

    Its objects carry $q:A\to\mathbb Q/2\mathbb Z$; the polarization
    $b_q:A\times A\to\mathbb Q/\mathbb Z$ is reachable through
    :meth:`~DiscriminantQuadraticModules.ParentMethods.associated_bilinear_form`,
    which lands in the sibling category.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "discriminant quadratic modules"

    def super_categories(self) -> list:
        return [TorsionModulesWithForm()]

    def cokernel(self, morphism: LatticeMorphism) -> TorsionQuadraticForm:
        r"""Return $\operatorname{coker}$ of ``morphism`` as an object of this category.

        Which category is asked settles which form the answer carries, and here
        that is the value module: the same cokernel of the same $c$ with the
        same Gram matrix is a bilinear form in $\mathbb Q/\mathbb Z$ and a
        quadratic one in $\mathbb Q/2\mathbb Z$.
        """
        source_gram = morphism.domain().gram_matrix()
        assert all(entry in 2 * ZZ for entry in source_gram.diagonal()), (
            "q is well defined only when the relations have even norm; these do "
            "not, so the cokernel carries b alone -- use discriminant_bilinear_form"
        )
        form = TorsionQuadraticForm(
            Cokernel(morphism), QmodnZ(2), discriminant_gram(morphism)
        )
        form._morphism = morphism
        refine(form, self)
        subdivide_form_gram_matrix(form)
        return form

    class ParentMethods:
        r"""Methods available on discriminant quadratic modules."""

        def _unused_value_module(self: Any) -> QmodnZ:
            r"""Return $\mathbb Q/2\mathbb Z$, where $q$ takes its values."""
            return QmodnZ(2)

        def gram_matrix(self: Any) -> Matrix:
            r"""Return the form in this object's generating set, in its value module."""
            gram = FormModule.gram_matrix(self)
            r"""Diagonal $q(g_i)$ in $\mathbb Q/2\mathbb Z$, off-diagonal
            $b_q(g_i,g_j)$ in $\mathbb Q/\mathbb Z$: the two halves report
            different things and live in different value groups."""
            generators = self.gens()
            size = len(generators)
            gram = matrix(QQ, size, size)
            for i, left in enumerate(generators):
                gram[i, i] = left.q().lift()
                for j in range(i + 1, size):
                    gram[i, j] = gram[j, i] = left.b(generators[j]).lift()
            return gram

        def associated_quadratic_form(self: Any) -> Any:
            r"""Return this form: it is already the quadratic one."""
            return self

        def associated_bilinear_form(self: Any) -> Any:
            r"""Return $b_q$, the polarization -- an object of the sibling category.

            Always defined, and it forgets: distinct $q$ on the same group can
            polarize to isometric $b$ (Peters--Sterk Sec. 12.5).
            """
            return DiscriminantBilinearModules().cokernel(self.correlation())

        def _form_matrix_latex_label(self: Any) -> str:
            r"""Return the LaTeX label for the quadratic Gram matrix."""
            return "G_{q_{A_L}}"

        def _form_matrix_latex_codomain(self: Any) -> str:
            r"""Return the LaTeX codomain for the quadratic Gram matrix entries."""
            return "\\mathbb{Q}/2\\mathbb{Z}"

        def correlation(self: Any) -> LatticeMorphism:
            r"""Return the $f$ this module is the cokernel of.

            It settles the object: a morphism of lattices with generating sets has a
            unique matrix, and $\operatorname{coker} f$ takes its generating set
            from $f$'s codomain and its form from that codomain's Gram matrix.
            """
            return self._morphism

        def gens(self: Any) -> tuple:
            r"""Return the generating set: the images of $L^\vee$'s generators."""
            return FormModule.gens(self)

        def primary_part(self: Any, p: Any) -> Subobject:
            r"""Return $A_p\hookrightarrow A$ as a subobject: the inclusion is the data.

            $A_p$ is an object of this category in its own right -- the cokernel of
            the correlation with codomain cut down to the preimage of $A_p$ -- and
            the subobject is that object together with its inclusion, not a
            predicate about which elements are $p$-primary.
            """
            multiplier = self.annihilator().gen().prime_to_m_part(p)
            images = [multiplier * generator for generator in self.gens()]
            part = DiscriminantQuadraticModules().cokernel(
                regenerated_by(self, [multiplier * g.lift() for g in self.gens()])
            )
            return Subobject(FormMorphism(part, self, matrix(ZZ, [g.coordinates() for g in images])))

        def invariant_factor_form(self: Any) -> "TorsionQuadraticForm":
            r"""Return $q$ on generators from the invariant factor decomposition.

            The change merges factors across summands -- $A_{A_2\oplus A_3}$ lands
            on one generator as $\mathbb Z/12$ rather than on two as
            $\mathbb Z/3\oplus\mathbb Z/4$ -- so no decomposition of $L$ survives
            it, which is why it cannot be :meth:`discriminant_group`.
            """
            return DiscriminantQuadraticModules().cokernel(
                regenerated_by(self, [g.lift() for g in self.smith_form_gens()])
            )

        def normal_form(self: Any) -> "TorsionQuadraticForm":
            r"""Return $q$ on $p$-adic Jordan generators -- a different object.

            For $p$ odd the blocks are those of Peters--Sterk Prop. 9.4.1; at $p=2$
            the reduced normal form of Cor. C.3.2 applies, which is where the
            quadratic side has a uniqueness statement the bilinear side lacks.
            """
            return DiscriminantQuadraticModules().cokernel(
                regenerated_by(self, p_adic_jordan_generators(self))
            )

        def source_lattice(self: Any) -> FreeQuadraticModule_integer_symmetric:
            r"""Return the lattice $L$ whose dual basis generates this form.

            ``None`` unless the generating set is the one $c$ induces, which is what
            the identity generating morphism says.  $L$ supplies a decomposition of
            *its* dual basis and of nothing else.
            """
            return self._morphism.domain()

    class ElementMethods:
        r"""Methods available on elements of discriminant quadratic modules."""

        def q(self: Any) -> Any:
            r"""Return $q(\bar x)=\tilde b(x,x)\in\mathbb Q/2\mathbb Z$.

            The same pairing the bilinear form reads modulo $\mathbb Z$, read
            here modulo $2\mathbb Z$ instead -- Nikulin's convention, and the
            reason $q$ and $b$ differ only in their value module.
            """
            return FormModuleElement.b(self, self)

        def b(self: Any, other: Any) -> Any:
            r"""Return the polarization $b_q(\bar x,\bar y)\in\mathbb Q/\mathbb Z$."""
            return QmodnZ(1)(
                self.coordinates()
                * FormModule.gram_matrix(self.parent())
                * other.coordinates()
            )

        def __pow__(self: Any, exponent: Any, modulus: Any = None) -> Any:
            r"""``x ^ 2`` -> $q(x)$."""
            assert exponent == 2, f"exponent {exponent} not supported"
            return self.q()

        def is_characteristic(self: Any) -> bool:
            r"""Return whether $q(x)=b(x,v^*)$ modulo $\mathbb Z$ for every $x$."""
            for x in self.parent():
                if QQ(x.q().lift() - x.b(self).lift()) not in ZZ:
                    return False
            return True
