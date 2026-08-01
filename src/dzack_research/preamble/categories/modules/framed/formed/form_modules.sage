r"""Modules carrying a form.

The node under lattices, rational lattices, and torsion bilinear and quadratic
forms.  All four are the same shape -- a module with a generating set carrying a
form -- and they differ only in the module and in where the form takes its
values:

===========================  ========================  ==============
object                       module                    value module
===========================  ========================  ==============
lattice                      $\mathbb Z^n$             $\mathbb Z$
rational lattice, $L^\vee$   $\mathbb Z^n$             $\mathbb Q$
torsion bilinear form        $\operatorname{coker} c$  $\mathbb Q/\mathbb Z$
torsion quadratic form       $\operatorname{coker} c$  $\mathbb Q/2\mathbb Z$
===========================  ========================  ==============

So integrality is not a property of the Gram entries but a fact about where the
form lands, and $L^\vee$ and $A_L$ -- same generators, same pairings -- are
distinguished only by their value modules.  Taking a cokernel changes the
module; reducing changes the value module; $A_L$ is both applied to $L^\vee$.

A form module is built from its form, which already knows its module and its
value module.  Nothing here consumes a Gram matrix: matrices enter at
:class:`BilinearForm` and are read back out of forms and morphisms when an
algorithm needs coordinates.

Which of the four an object is, is a matter of membership rather than of type:
:class:`FormModules` says what having a form means -- the pairing, the norm,
and the two abbreviations for them -- and the subcategories say what their
fibres add to it.  The classes below hold the data and the arithmetic Sage's
coercion model dispatches to a concrete type, and nothing else.
"""

from typing import Any

from sage.categories.category import Category
from sage.categories.modules import Modules
from sage.categories.sets_cat import Sets
from sage.matrix.matrix0 import Matrix
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet
from sage.structure.richcmp import richcmp


class FormHomset(Parent):
    """The owned homset of two form modules."""

    def __init__(self, domain: Any, codomain: Any) -> None:
        Parent.__init__(self, category=Sets())
        self._domain = domain
        self._codomain = codomain

    def domain(self) -> Any:
        return self._domain

    def codomain(self) -> Any:
        return self._codomain

    def __call__(self, assignment: Any) -> "FormMorphism":
        return FormMorphism(assignment, parent=self)

    def __contains__(self, morphism: Any) -> bool:
        return isinstance(morphism, FormMorphism) and morphism.parent() is self

    def _repr_(self) -> str:
        return f"Set of form-preserving maps from {self._domain} to {self._codomain}"


class FormModules(Category):
    r"""Category of modules lying over $\mathrm{Modules}$ and carrying a form.

    The fibre category of $U$, and the node every object with a form is under:
    lattices, $L^\vee$, and the torsion bilinear and quadratic forms differ in
    their module and in their value module, not in what having a form means.
    So the pairing, the norm, and the ergonomics that abbreviate them are
    stated once, here, rather than on each realization -- which is what lets
    $L^\vee$ and $A_L$ answer ``x.b(y)`` for the same reason.

    An object of this category supplies two things and derives the rest: its
    form, and its image under $U$.  Both are data, so they stay with whatever
    stores them; everything below is a consequence of having them.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "form modules"

    def super_categories(self) -> list:
        r"""Return $\mathbb Z\text{-Mod}$, which $U$ lands in.

        A form module is a module, and its addition and its $\mathbb Z$ action
        are that module's -- the form adds no arithmetic.  What it adds is a
        way to pair two elements, and that is what this category is.
        """
        return [Modules(ZZ).Framed()]

    class ParentMethods:
        r"""What can be asked of an object once it has a form and a module."""

        def value_module(self: Any) -> Any:
            r"""Return where the form takes its values."""
            return self.form().value_module()

        def gram_matrix(self: Any) -> Matrix:
            r"""Return the form's Gram matrix in this object's generating set.

            For a quadratic form this is the polarization's: $q$ is not
            bilinear and has no Gram matrix of its own, only values on the
            generators.
            """
            return self.form().gram_matrix()

        def is_torsion_free(self: Any) -> bool:
            r"""Return whether the underlying module is torsion-free."""
            return self.forget_form().is_torsion_free()

        def is_torsion(self: Any) -> bool:
            r"""Return whether the underlying module is a torsion module."""
            return self.forget_form().is_torsion()

        def linear_combination(self: Any, coefficients: Any) -> "FormModuleElement":
            r"""Return $\sum_i a_i g_i$ for ``coefficients`` $=(a_i)$.

            The declared reading of a coordinate vector, and the only one:
            calling it says which generating set the numbers are coordinates
            in, so a vector cannot drift from one module to another by being
            handed to a different parent.
            """
            coefficients = tuple(coefficients)
            generators = self.gens()
            assert len(coefficients) == len(generators), (
                f"this object has {len(generators)} generators, got "
                f"{len(coefficients)} coefficients"
            )
            return _combination(self, coefficients)

        def hom(self: Any, images: Any, parent: FormHomset) -> "FormMorphism":
            r"""Return the form morphism sending this object's generators to ``images``.

            Sugar for the assignment: the generators are this object's, in
            order, so only the images have to be named.  Where they land says
            what the codomain is.

            A generating set can name the same element twice, and then a map
            has to send it to the same place both times -- otherwise there is
            no map, which is what the check below says.
            """
            generators = self.gens()
            images = tuple(images)
            assert len(images) == len(generators), (
                f"this object has {len(generators)} generators, got {len(images)} images"
            )
            assignment = {}
            for generator, image in zip(generators, images):
                assert assignment.setdefault(generator, image) == image, (
                    f"{generator} appears twice among the generators and is sent to "
                    "two different places, so this assignment is not a map"
                )
            images = tuple(assignment.values())
            return FormMorphism(assignment, parent=parent)

    class ElementMethods:
        r"""What it is to be an element of a module carrying a form.

        A module element first: the addition and the $\mathbb Z$ action come
        from $\mathbb Z\text{-Mod}$, which this category is under, and are not
        restated.  What the form adds is that two elements of one object can be
        paired and that an element has a norm -- and the two abbreviations for
        those, $v*w$ and $x/n$, which are the same questions written shorter.
        """

        def _coordinates(self: Any) -> Any:
            r"""Return this element's coordinates in its parent's generating set.

            Private.  Reading coordinates is how an element stops being an
            element and becomes a list of numbers that any module will accept,
            so it is a backend step: a computation that has to leave the formed
            world takes them, and the result comes back through a named
            construction.  What is public is the element and what can be asked
            of it -- its pairings, its norm, its order, its image under a
            morphism.
            """
            underlying = self.forget_form()
            if isinstance(underlying, TorsionModuleElement):
                return vector(underlying._lift())
            return vector(underlying)

        def b(self: Any, other: Any) -> Any:
            r"""Return the pairing, asked of the form itself.

            Bilinear or quadratic, the form answers this: for a $q$ it is the
            polarization, which is a different form with a different value
            module, and knowing that is the form's business rather than the
            element's.
            """
            assert other.parent() is self.parent(), (
                f"b is a form on one module, and {other} lies in {other.parent()} "
                f"while this element lies in {self.parent()}. Pairing them would "
                "mean reading two coordinate vectors against one Gram matrix, "
                "which silently assumes a map identifying the two generating "
                "sets. If a morphism f relates them, write f(x).b(y) and pair in "
                "one place; if none does, the pairing is not defined."
            )
            form = self.parent().form()
            return form.b(self.forget_form(), other.forget_form())

        def span(self: Any) -> Any:
            r"""Return the rank-one subobject $Rx$ this element generates."""
            return self.parent().subobject_on([self])

        def isotropic_reduction(self: Any) -> Any:
            r"""Return $x^{\perp}/x$, which is its span's isotropic reduction.

            One element is not a special case of the construction: the span of
            an isotropic $x$ is an isotropic subobject, and this is that
            subobject's reduction under the name an element is asked by.
            """
            return self.span().isotropic_reduction()

        def norm(self: Any) -> Any:
            r"""Return this form's value on the diagonal at this element.

            $q(x)$ where the form is quadratic and $b(x,x)$ where it is
            bilinear, which is a difference of value modules the element does
            not have to know about -- it asks the form, and the form answers
            with its own.
            """
            return self.parent().form().norm(self.forget_form())

        def __mul__(self: Any, other: Any) -> Any:
            r"""``v * w`` -> $b(v,w)$, and ``v * a`` -> the scaled element."""
            if isinstance(other, FormModuleElement):
                return self.b(other)
            assert other in self.parent().base_ring(), (
                "this product is not scaling an element: the right factor is not "
                f"a scalar of {self.parent().base_ring()}.\n"
                "  - A matrix: x * M reads x's coordinates, multiplies, and reads "
                "the answer back in the same generating set, which is a map "
                "nobody has stated. Say it: build the morphism from where the "
                "generators go, N.hom([...]) or ModuleMorphism({g: image}), and "
                "apply that.\n"
                "  - A vector: the pairing of two elements is x.b(y), and a "
                "coordinate vector is not an element -- name the combination it "
                "stands for with linear_combination first.\n"
                "  - A fraction: see __truediv__, which explains when x/n exists.\n"
                f"got: {other}"
            )
            return self.parent()._over(other * self.forget_form())

        def __truediv__(self: Any, divisor: Any) -> "FormModuleElement":
            r"""Return the unique $y$ with $ny=x$, where there is one.

            Only in a torsion-free module.  In a quotient, $ny=x$ has either no
            solution or several -- any two differ by an $n$-torsion element,
            and a discriminant group is all torsion -- so there is nothing for
            $x/n$ to denote there, however suggestive the notation.
            """
            parent = self.parent()
            assert not isinstance(parent.forget_form(), TorsionModule), (
                f"x / {divisor} is not defined in {parent}: this is a quotient, so "
                f"{divisor}*y = x has either no solution or several -- any two "
                f"differ by an element killed by {divisor}, and here every element "
                "is torsion.\n"
                "  - To divide before passing to classes: divide the lift in the "
                "module being quotiented, then project it.\n"
                "  - To name one solution of n*y = x here: solve for it and say "
                "which one you mean; the notation x/n cannot."
            )
            quotient = self._coordinates() / divisor
            assert all(entry in ZZ for entry in quotient), (
                f"{divisor} does not divide {self._coordinates()} in {parent}: the "
                "quotient is not a Z-linear combination of the generators, so it "
                "is not an element of this module at all"
            )
            # Division happens where the coordinates live, which is $U(A)$, and
            # the answer comes back up the fibre.
            return parent._over(parent.forget_form()(list(quotient)))


class BilinearFormModules(Category):
    r"""Form modules whose stored form is bilinear."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a bilinear form"

    def super_categories(self) -> list:
        return [FormModules()]


class QuadraticFormModules(Category):
    r"""Form modules whose stored form is quadratic."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a quadratic form"

    def super_categories(self) -> list:
        return [FormModules()]


class FreeFormModules(Category):
    r"""Form modules whose image under $U$ is free.

    The other branch from :class:`TorsionModulesWithForm`, and what a lattice
    and $L^\vee$ have in common: the generating set is a basis, so it has a
    rank, no relation holds among its members, and a coordinate vector names
    exactly one element.  None of that is true in the torsion branch, and
    everything the two branches share is already stated by
    :class:`FormModules`.

    Freeness is about the module, not the form, so it says nothing about where
    the form lands -- $L$ is $\mathbb Z$-valued and $L^\vee$ is $\mathbb
    Q$-valued and both are here.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free form modules"

    def super_categories(self) -> list:
        return [FormModules()]

    class ParentMethods:
        r"""What freeness adds to having a form."""

        def rank(self: Any) -> Any:
            r"""Return the rank, which a free module has and a quotient does not."""
            return self.forget_form().rank()

        def basis(self):
            r"""Return the generating set, which here is a basis.

            The same tuple :meth:`gens` returns, under the name that says the
            extra fact: the generators of a free module are independent, so a
            coordinate vector names one element rather than a coset of them.
            In the torsion branch there is no such name, because there is no
            such fact.
            """
            return self.gens()

        def subobject_on(self: Any, generators: Any) -> "Subobject":
            r"""Return the sub-form-module these generate, as its inclusion into this one.

            A subobject is its inclusion, so what comes back is a morphism: the
            submodule is a new object with its own generators, and the only
            thing tying them to this object is where they go.  There is no
            containment being asserted and no ambient being shared.

            Its form is this one's, evaluated on those generators -- which is
            what makes the inclusion a morphism of form modules rather than of
            modules.  The restriction may be degenerate where this form is not:
            an isotropic vector lies in its own complement, and nothing about
            being a subobject prevents that.
            """
            generators = _independent_generators(self, generators)
            gram = matrix(
                [[left.b(right) for right in generators] for left in generators]
            )
            sub = self._sub_form_module(gram)
            return Subobject(
                ModuleMorphism.zero(sub, self)
                if not generators
                else _module_morphism(dict(zip(sub.gens(), generators)))
            )

        def _sub_form_module(self: Any, gram: Matrix) -> Any:
            r"""Return the object of this category carrying ``gram``.

            What kind of object that is follows from where the form lands,
            which is the one thing distinguishing the free objects here: a
            $\mathbb Z$-valued form makes a lattice, and the lattices override
            this to say so.
            """
            return BilinearForm(
                BasedFreeModule(ZZ, standard_framing_set(gram.nrows())),
                self.value_module(),
                gram,
            )


class FormModuleElement(Element):
    r"""An element of a form module, held by its coordinates in the generating set.

    $U(A)$ decides what the coordinates mean -- for a cokernel it reduces them
    to a canonical representative -- and the fibre adds the pairing, which is
    why the element's parent is the form module and not its image under $U$.

    Carries the datum -- its image under $U$ -- and the arithmetic Sage's
    coercion model dispatches to the element class.  What can be *asked* of it
    is :class:`FormModules`'s: pairing, norm, and the abbreviations for them
    are the same questions in every fibre, so they are stated there once
    instead of on each realization.
    """

    def __init__(self, parent: Any, x: Any) -> None:
        Element.__init__(self, parent)
        self._underlying = parent.forget_form()(x)

    def forget_form(self) -> Any:
        r"""Return this element's image under $U$, the fibration's projection.

        $U$ is faithful on a fibre, so an element of $(M,b)$ and its image in
        $M$ correspond -- which is why this looks like unwrapping.  It is not:
        the form module is not $M$ with something attached, it lies over $M$,
        and $U$ is what says so.
        """
        return self._underlying

    # Z-Mod's structure, realized for this representation.  The operations are
    # the category's; what is here is only how adding and scaling are carried
    # out on the image under $U$, which is what Sage's coercion model
    # dispatches to.
    def _add_(self, other: Any) -> "FormModuleElement":
        return self.parent()._over(self._underlying + other._underlying)

    def _sub_(self, other: Any) -> "FormModuleElement":
        return self.parent()._over(self._underlying - other._underlying)

    def _neg_(self) -> "FormModuleElement":
        return self.parent()._over(-self._underlying)

    def _lmul_(self, factor: Any) -> "FormModuleElement":
        return self.parent()._over(factor * self._underlying)

    _rmul_ = _lmul_

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._underlying, other._underlying, op)

    def __hash__(self) -> int:
        # Not the image under $U$: a module element can be mutable, and
        # freezing one would be reaching into a representation this object
        # only lies over.  Equal elements have equal coordinates, which is
        # what a hash needs.
        return hash(tuple(self._coordinates()))

    def _repr_(self) -> str:
        return repr(self._underlying)


class FormModule(Parent):
    r"""A module with a generating set, carrying a form.

    Composition, not inheritance: this has an underlying module rather than
    being a submodule of, or an ambient for, anything.  Sage's lattice classes
    are realizations -- ``FreeQuadraticModule_submodule_with_basis_pid`` is a
    submodule of a rational ambient with a chosen basis -- and subclassing one
    inherits an embedding this object does not have.  The module interface below
    is delegated, so the realization stays a detail of the module rather than
    part of what a form module is.

    The form is the datum, and the module and value module are read off it: a
    form already knows what it is defined on and where it lands, so passing all
    three would let them disagree.

    Holds the two data of an object of :class:`FormModules` -- the form and the
    image under $U$ -- and the construction that is particular to how those are
    represented.  Everything derived from them is the category's.
    """

    def __init__(self, form: Any) -> None:
        module = form.module()
        Parent.__init__(self, base=module.base_ring())
        self._form = form
        self._module = module
        self._generating_set = module.generating_set()
        refine(self, FormModules())

    def _initialize_framing(self) -> None:
        r"""Lift the module framing after all categorical refinements are installed."""
        self._framing_map = {
            e: self._over(g)
            for e, g in zip(self._generating_set, self._module.gens())
        }
        self._gens = TotallyOrderedSet(tuple(self._framing_map.values()))

    # ---- the form ----

    def form(self) -> Any:
        r"""Return the form this module carries."""
        return self._form

    def forget_form(self) -> Any:
        r"""Return $U(A)$, this object's image under the fibration's projection.

        $U:\mathrm{FormModules}\to\mathrm{Modules}$ forgets the form; the
        objects over a fixed $M$ are the forms on $M$, and this is a fibration
        rather than an inclusion of a subcategory -- so this is not "the module
        underneath", which would make a form module a module with extra data
        that could be reached past.  It is where an algorithm goes when it has
        to leave the formed world to compute, and the result comes back through
        this object, never as a bare module element.
        """
        return self._module

    # ---- delegated to the module ----

    def gens(self):
        r"""Return the generating set the form is written in."""
        return self._gens

    def ngens(self) -> int:
        return len(tuple(self._module.gens()))

    Element = FormModuleElement

    def _element_constructor_(self, x: Any) -> FormModuleElement:
        r"""Return ``x``, which has to be an element of this object already.

        Nothing is converted here.  A coordinate vector is not an element of
        this module -- it is a list of numbers, and reading it as $\sum_i a_ig_i$
        is a claim about which generating set is meant, which the caller has to
        make in as many words with :meth:`linear_combination`.  An element of
        another form module is refused outright: whatever relates the two is a
        morphism, and applying it is that morphism's job, not this one's.
        """
        assert isinstance(x, FormModuleElement) and x.parent() is self, (
            f"{x} is not an element of {self}; build one from this object's "
            "own generators -- linear_combination for a coordinate vector, and "
            "a morphism to come from somewhere else"
        )
        return x

    def __contains__(self, x: Any) -> bool:
        r"""Return whether ``x`` is an element of this object.

        Which is parenthood and nothing else.  There is no ambient module here
        for two objects to sit inside and be compared in, so membership is not
        a test on coordinates: an element of another module is not in this one
        even when its coordinate vector would be accepted, and a bare vector
        is not in it either.  A question about a subobject is a question about
        its inclusion, not about containment.
        """
        return isinstance(x, FormModuleElement) and x.parent() is self

    def _over(self, x: Any) -> FormModuleElement:
        r"""Return the element of this object lying over ``x`` $\in U(A)$.

        Private, and the section of $U$ that exists because $U$ is faithful on
        this fibre: the object's own generators and their arithmetic are the
        only things entitled to it, since everything else would be choosing a
        fibre for an element that has none.
        """
        return self.element_class(self, x)

    def zero(self) -> FormModuleElement:
        return self._over(self._module.zero())

    def _repr_(self) -> str:
        return (
            f"Form module on {self.ngens()} generators over {self.base_ring()} "
            f"with values in {self.value_module()}"
        )


class FormMorphism:
    r"""A form-preserving map of form modules, held by the module map underneath it.

    Owned rather than a Sage morphism, because the objects are no longer Sage
    modules.  The datum is the map of modules; being a morphism *of form
    modules* is the single condition $f^*b_B=b_A$, which is checked here by
    pulling the codomain's form back along $f$ and comparing it to the domain's.

    That comparison is between two forms, so it happens in one value module --
    the domain's.  There is no entry-by-entry comparison in which different
    positions of a matrix are read in different places; a quadratic form
    compares its values on the generators and its polarization, each in its own
    value module, because those are two forms and not two halves of one matrix.
    """

    def __init__(self, assignment: Any, parent: FormHomset) -> None:
        morphism = (
            _module_morphism(assignment) if isinstance(assignment, dict) else assignment
        )
        domain, codomain = morphism.domain(), morphism.codomain()
        pulled_back = codomain.form().pullback(morphism)
        assert domain.form() == pulled_back, (
            f"not a morphism of form modules: the pullback of {codomain.form()} "
            f"is not {domain.form()}"
        )
        self._domain = domain
        self._codomain = codomain
        self._morphism = morphism
        self._parent = parent
        assert parent.domain() is domain and parent.codomain() is codomain

    def module_morphism(self) -> Any:
        r"""Return the map of modules this is a form morphism of."""
        return self._morphism

    def domain(self) -> Any:
        return self._domain

    def parent(self) -> Any:
        return self._parent

    def codomain(self) -> Any:
        return self._codomain

    def matrix(self) -> Matrix:
        r"""Return the images of the domain's generators, one per row."""
        return self._morphism.matrix()

    def __call__(self, x: Any) -> Any:
        return self._morphism(x)

    def lift(self, y: Any) -> Any:
        r"""Return an $x$ with $f(x)=y$, asked of the map of modules underneath.

        Preserving the form has nothing to say about preimages, so there is
        nothing to add here: the case distinction and the linear system are
        :meth:`ModuleMorphism.lift`'s, and this is the same map.
        """
        return self._morphism.lift(y)

    def kernel(self) -> Any:
        r"""Return $\ker f\hookrightarrow A$.

        Preserving the form says nothing about which elements are killed, so
        this is the underlying map's kernel; what the form contributes is that
        the subobject it comes back as carries the restriction, which
        :meth:`FormModules.ParentMethods.subobject_on` supplies.
        """
        return self._morphism.kernel()

    def cokernel(self) -> Any:
        r"""Return $B/\operatorname{im} f$ as a module, presented by $f$."""
        return self._morphism.cokernel()

    def image(self) -> Any:
        r"""Return $\operatorname{im} f\hookrightarrow B$."""
        return self._morphism.image()

    def index(self) -> Any:
        r"""Return the index of the image of the underlying module morphism."""
        return self._morphism.index()

    def orthogonal_complement(self) -> Any:
        r"""Return $(\operatorname{im} f)^{\perp}\hookrightarrow B$."""
        return self._morphism.orthogonal_complement()

    def then(self, other: "FormMorphism") -> "FormMorphism":
        r"""Return $g\circ f$ for ``other`` $=g$: this map followed by that one."""
        assert other.domain() is self._codomain, (
            "these do not compose: this map lands in "
            f"{self._codomain}, the next starts from {other.domain()}"
        )
        return FormHomset(self._domain, other.codomain())(
            dict(
                zip(
                    self._domain.gens(),
                    [other(self(generator)) for generator in self._domain.gens()],
                )
            )
        )

    def __repr__(self) -> str:
        return (
            f"Form morphism from {self._domain.ngens()} to "
            f"{self._codomain.ngens()} generators"
        )


def correlation_of(lattice: Any) -> FormMorphism:
    r"""Return $c: L\to L^\vee$, $v\mapsto\langle v,-\rangle$.

    $L$ is free with Gram $G$ and $\mathbb Z$-valued form; $L^\vee$ is free on
    the dual generators with Gram $G^{-1}$ and $\mathbb Q$-valued form; and $c$
    sends $e_i$ to $\sum_j G_{ij}e_j^\vee$.  Form preservation is then
    $G\,G^{-1}G^{\mathsf T}=G$, which is what makes $c$ a morphism here.
    """
    # The domain is the lattice, not a free module built to the same Gram
    # matrix: a duplicate would make $L$'s elements foreign to $c$, and the
    # only way to apply $c$ to one would be to hand its coordinates to the
    # duplicate -- which is a map, and so something a morphism has to state.
    gram = lattice.gram_matrix()
    dual = lattice.dual()
    return FormHomset(lattice, dual)(
        dict(
            zip(
                lattice.gens(),
                (dual.linear_combination(row) for row in gram.rows()),
            )
        )
    )
