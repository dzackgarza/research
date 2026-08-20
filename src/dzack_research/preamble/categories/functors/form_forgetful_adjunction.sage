r"""The free/forgetful adjunctions between modules and formed modules.

Forgetting a form is a functor \(U:\mathbf{FormMod}_R\to\mathbf{Mod}_R\), not
a method on a formed module.  A formed module **is** a module with a form, so
an object has nothing to forget to; the passage is between categories and is
written here with the other functors.

\(U\) has a left adjoint, and it is the tautological form.  A form on \(M\) is
a module map out of the module that **classifies** forms of its kind, so the
free one is the identity on that classifier:

- a bilinear form is a map out of \(T^2M\), so \(F(M)=(M,\;T^2M,\;\mathrm{id})\);
- a quadratic form is a map out of the divided square \(\Gamma^2M\), so
  \(F(M)=(M,\;\Gamma^2M,\;\mathrm{id})\).

The two kinds are different classifiers, so there are two adjunctions, one
over each flavour category.  What they share is written once below; each
flavour names only its classifying square.

A morphism of formed modules \((M,W,b)\to(N,W',c)\) is a pair \((f,g)\) with
\(g\circ b=c\circ(f\otimes f)\).  Out of the tautological form the condition
reads \(g\circ\mathrm{id}=c\circ(f\otimes f)\), so \(g\) is forced and the
pair is determined by \(f\) alone:

\[
    \mathrm{Hom}_{\mathbf{FormMod}}(F(M),(N,W',c))
    \;\cong\;
    \mathrm{Hom}_{\mathbf{Mod}}(M,N).
\]

That is the adjunction.  Every form of the given kind on \(M\) factors
uniquely through the tautological one, which is what makes it free.  The unit
at \(M\) is the identity, since \(U(F(M))=M\); the counit at \((N,W',c)\) is
\((\mathrm{id}_N,c)\), the form read as the map naming which quotient of the
tautological form the object is.
"""


from typing import TYPE_CHECKING

from dzack_research.preamble.categories.abstract_categories.functors import Functor
from dzack_research.preamble.categories.functors.free_forgetful_adjunction import (
    Adjunction,
)
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    BilinearFormModules,
    QuadraticFormModules,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules

if TYPE_CHECKING:
    from collections.abc import Callable

    from sage.categories.category import Category
    from sage.categories.modules import Module
    from sage.rings.ring import Ring

    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        ModuleMorphism,
    )


def _owned_base_ring(base_ring: "Ring") -> "Ring":
    # Local: importing the ring node at module level would close a cycle, and
    # the ring is built by the time any of these functors is constructed.
    from dzack_research.preamble.categories.rings.rings import owned_ring_view

    return owned_ring_view(base_ring)


class ForgetTheFormFunctor(Functor):
    r"""\(U\) from a flavour of formed modules to \(\mathbf{Mod}_R\).

    Faithful by declaration: a morphism of formed modules is a module
    morphism that additionally preserves the form, so two agreeing as module
    morphisms are equal.
    """

    _faithful = True

    def __init__(self, base_ring: "Ring", formed: "Category") -> None:
        base_ring = _owned_base_ring(base_ring)
        self._base_ring = base_ring
        super().__init__(formed, Modules(base_ring))

    def _apply_functor(self, formed_module: "Module") -> "Module":
        r"""Return the module, which is the formed module itself.

        A formed module is constructed through the module level, so it is
        already an object of \(\mathbf{Mod}_R\).  \(U\) moves it between
        categories and changes no object.
        """
        return formed_module

    def _apply_functor_to_morphism(
        self, formed_morphism: "ModuleMorphism"
    ) -> "ModuleMorphism":
        r"""Return the same arrow, read where nothing is asked of the form."""
        domain = self._apply_functor(formed_morphism.domain())
        codomain = self._apply_functor(formed_morphism.codomain())
        return domain.hom(codomain, formed_morphism)


class TautologicalFormFunctor(Functor):
    r"""\(F:\mathbf{Mod}_R\to\) a flavour of formed modules.

    \(M\mapsto(M,\;C(M),\;\mathrm{id})\) for the module \(C(M)\) that
    classifies forms of this kind.  Every such form on \(M\) is a map out of
    \(C(M)\), so the identity is the one they all factor through.

    Subclasses supply the classifier and nothing else.
    """

    def __init__(self, base_ring: "Ring", formed: "Category") -> None:
        base_ring = _owned_base_ring(base_ring)
        self._base_ring = base_ring
        super().__init__(Modules(base_ring), formed)

    def _classifying_square(self, module: "Module") -> "Module":
        r"""Return \(C(M)\): the module whose maps out are the forms."""
        raise NotImplementedError(
            "a tautological form functor names its classifying square"
        )

    def _apply_functor(self, module: "Module") -> "Module":
        # Local: at module level this closes an import cycle; the form module
        # is built by the time a form is put on a module.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
            FormModule,
        )

        classifier = self._classifying_square(module)
        return FormModule(classifier.hom(classifier, lambda t: t))

    def _apply_functor_to_morphism(
        self, module_morphism: "ModuleMorphism"
    ) -> "ModuleMorphism":
        r"""Return \(F(f)\): \(f\) on modules, \(C(f)\) on the values."""
        domain = self._apply_functor(module_morphism.domain())
        codomain = self._apply_functor(module_morphism.codomain())
        return domain.hom(codomain, module_morphism)


class TautologicalBilinearFormFunctor(TautologicalFormFunctor):
    r"""\(M\mapsto(M,\;T^2M,\;\mathrm{id})\): the free bilinear form."""

    def __init__(self, base_ring: "Ring") -> None:
        super().__init__(base_ring, BilinearFormModules(base_ring))

    def _classifying_square(self, module: "Module") -> "Module":
        # Local: at module level this closes an import cycle.
        from dzack_research.preamble.categories.modules.tensors import TensorSquare

        return TensorSquare(module)


class TautologicalQuadraticFormFunctor(TautologicalFormFunctor):
    r"""\(M\mapsto(M,\;\Gamma^2M,\;\mathrm{id})\): the free quadratic form."""

    def __init__(self, base_ring: "Ring") -> None:
        super().__init__(base_ring, QuadraticFormModules(base_ring))

    def _classifying_square(self, module: "Module") -> "Module":
        # Local: at module level this closes an import cycle.
        from dzack_research.preamble.categories.modules.tensors import DividedSquare

        return DividedSquare(module)


class FormForgetfulAdjunction(Adjunction):
    r"""\(F\dashv U\) between \(\mathbf{Mod}_R\) and one flavour of forms."""

    def unit(self, module: "Module") -> "ModuleMorphism":
        r"""Return \(\eta_M:M\to U(F(M))\), the identity.

        \(F\) puts a form on \(M\) and changes no module, so \(U(F(M))=M\).
        """
        return module.hom(module, lambda element: element)

    def counit(self, formed_module: "Module") -> "ModuleMorphism":
        r"""Return \(\varepsilon:F(U(N))\to N\), which is the form of \(N\).

        \(F(U(N))\) carries the tautological form on the same module; the
        arrow to \(N\) is the identity on modules paired with \(N\)'s own form
        on the values.
        """
        return formed_module.hom(formed_module, lambda element: element)

    def hom_set_isomorphism_forward(
        self, formed_morphism: "ModuleMorphism"
    ) -> "ModuleMorphism":
        r"""Return \(\Phi(\phi)=U(\phi)\circ\eta_M\), which is \(U(\phi)\)."""
        return self.right_adjoint()(formed_morphism)

    def hom_set_isomorphism_inverse(
        self, module_morphism: "ModuleMorphism", formed_codomain: "Module"
    ) -> "ModuleMorphism":
        r"""Return \(\Phi^{-1}(f)=\varepsilon\circ F(f)\).

        The value half is forced: out of the tautological form the condition
        \(g\circ\mathrm{id}=c\circ(f\otimes f)\) determines \(g\), which is
        why the bijection holds.
        """
        return self.left_adjoint()(module_morphism)


class BilinearFormForgetfulAdjunction(FormForgetfulAdjunction):
    r"""\(F\dashv U\) with \(T^2\) classifying the forms."""

    def __init__(self, base_ring: "Ring") -> None:
        super().__init__(
            TautologicalBilinearFormFunctor(base_ring),
            ForgetTheFormFunctor(base_ring, BilinearFormModules(base_ring)),
        )


class QuadraticFormForgetfulAdjunction(FormForgetfulAdjunction):
    r"""\(F\dashv U\) with \(\Gamma^2\) classifying the forms."""

    def __init__(self, base_ring: "Ring") -> None:
        super().__init__(
            TautologicalQuadraticFormFunctor(base_ring),
            ForgetTheFormFunctor(base_ring, QuadraticFormModules(base_ring)),
        )
