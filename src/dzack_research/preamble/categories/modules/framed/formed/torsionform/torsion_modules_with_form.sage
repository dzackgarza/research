r"""Finite torsion modules equipped with a bilinear or quadratic form."""

from typing import Any

from sage.arith.misc import factor
from sage.categories.category_types import Category_over_base_ring
from sage.matrix.matrix0 import Matrix
from sage.misc.latex import latex as _latex_fn


class TorsionModulesWithForm(Category_over_base_ring):
    r"""Category of finite torsion modules equipped with a form."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        match base_ring:
            case None:
                return super().__classcall__(cls, ZZ)
            case _ if base_ring is ZZ:
                return super().__classcall__(cls, ZZ)
            case _:
                raise TypeError(
                    "finite torsion-form algorithms here are over ZZ"
                )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "torsion modules with form"

    def super_categories(self) -> list:
        r"""Return the finite framed form modules lying over torsion modules.

        Not a category of groups: an element of $(G,b)$ is a module element
        that a form can be evaluated on, and its addition and its $\mathbb Z$
        action are the module's.  What $G$ is belongs to :meth:`forget_form`,
        which is where the group questions are asked and answered.

        Nor a category with its own pairing: $b(a,a')$ and the norm are what it
        is to have a form at all, so they come from :class:`FormModules` here
        exactly as they do for a lattice or for $L^\vee$.  What is added below
        is what being *torsion* adds, which is finiteness and everything that
        follows from it.
        """
        return [
            FinitelyGeneratedFormModules(self.base_ring()),
            TorsionModules(self.base_ring()),
        ]

    class ParentMethods:
        r"""Methods shared by bilinear and quadratic discriminant modules."""

        def gram_matrix(self: Any) -> Matrix:
            r"""Return the form's matrix with its entries read in the value module.

            The form stores representatives -- rationals -- because $\mathbb
            Q/n\mathbb Z$ has no matrix space to hold the entries themselves.
            This reduces each into the value module and takes the canonical
            representative back, so the same object is displayed the same way
            however it was built.  Which matrix it is, is the form's business:
            $b$'s matrix for a bilinear module, $q$'s upper-triangular one for
            a quadratic module.
            """
            form = self.form()
            target = form.value_module()
            reduced = matrix(
                QQ,
                [
                    [target(entry).lift() for entry in row]
                    for row in form.gram_matrix().rows()
                ],
            )
            reduced.subdivide(*form.gram_matrix().subdivisions())
            return reduced

        def relation_matrix(self: Any) -> Matrix:
            r"""Return :meth:`presentation`'s matrix, one row per relation."""
            return self.forget_form().relation_matrix()

        def presentation(self: Any) -> Any:
            r"""Return $p$, the morphism this object is the cokernel of.

            Every object here has one, because every finitely presented module
            does.  What $p$ *is* varies -- a lattice's correlation, a
            finite-index map of lattices, or a morphism synthesized from a
            group and a matrix -- and that is what the refinements below are
            about; that there is one is not.
            """
            return self.forget_form().presentation()

        def invariants(self: Any) -> tuple:
            r"""Return the invariant factors of the underlying module."""
            return tuple(self.forget_form().invariants())

        def cardinality(self: Any) -> Any:
            r"""Return how many elements there are, which is finitely many."""
            return self.forget_form().cardinality()

        def annihilator(self: Any) -> Any:
            r"""Return $\operatorname{Ann}(A)\subseteq\mathbb Z$, which is nonzero here."""
            return self.forget_form().annihilator()

        def smith_form_gens(self: Any) -> Any:
            r"""Return generators realizing the invariant factor decomposition.

            The form is not written in them -- they are a different generating
            set, and a form written in one is a different object from the same
            form written in another, which is what ``regenerate`` builds.
            """
            return finite_ordered_set(
                tuple(
                    self._over(generator)
                    for generator in self.forget_form().smith_form_gens()
                )
            )

        def __iter__(self: Any):
            r"""Iterate over the elements, of which there are finitely many."""
            return map(self._over, self.forget_form())


        def primary_part(self: Any, p: Any) -> Subobject:
            r"""Return $A_p\hookrightarrow A$ as a subobject: the inclusion is the data.

            A presentation does not say which combinations of its generators
            have $p$-power order, and no bounded family of extra relations
            makes it say so, so $A_p$ is not cut out of one.  It is read off
            the primary decomposition: the invariant factor decomposition
            $A\cong\bigoplus\mathbb Z/d_i$ has generators $g_i$ of order $d_i$,
            and $(d_i/p^{v_p(d_i)})g_i$ generates the $p$-primary summand of
            that factor.  There is one per $d_i$ divisible by $p$ and they are
            independent, so they generate $A_p$ minimally -- which matters
            downstream, because a form written on a dependent generating set
            has a rank of its own that is not the group's.

            The inclusion comes with them.  Passing to the invariant factor
            decomposition is a change of basis, and $g_i$ is its $i$-th row
            already expressed in $A$'s own generating set, so composing with it
            is what makes the images above elements of $A$ rather than of a
            decomposition standing apart from it.
            """

            def primary_generator(generator: Any) -> tuple:
                order = generator.order()
                primary = p ** order.valuation(p)
                assert primary >= 1
                match primary:
                    case 1:
                        return ()
                    case value if value > 1:
                        return ((order // value) * generator,)

            generators = tuple(
                primary_element
                for generator in self.smith_form_gens()
                for primary_element in primary_generator(generator)
            )
            regenerated = self.regenerate(generators)
            return Subobject(
                regenerated.Hom(self)(
                    {
                        label: label
                        for label in regenerated.generating_set()
                    }
                )
            )

        def abelian_group(self: Any) -> Any:
            r"""Return the underlying group, asked of the underlying group.

            $(G,b)$ is not determined by $G$, and this method is about $G$
            alone, so the answer comes from :meth:`forget_form` -- which is an
            object of :class:`FinitelyPresentedTorsionModules` and the place
            such questions are settled and cached.
            """
            return self.forget_form().abelian_group()

        def is_p_elementary(self: Any, p: Any) -> bool:
            r"""Return whether the underlying group is elementary abelian of exponent $p$."""
            return self.forget_form().is_p_elementary(p)

        def primary_decomposition(self: Any) -> dict:
            r"""Return the underlying group's primary decomposition."""
            return self.forget_form().primary_decomposition()

        def _latex_(self: Any) -> str:
            r"""Return multi-line LaTeX for the torsion module and its form."""
            invs = self.invariants()
            n = self.gram_matrix().nrows()

            fp_latex = str(_latex_fn(self.forget_form().as_finitely_presented_group()))
            inv_str = _format_invariant_factor_latex(invs)
            prim_str = _format_primary_decomp_latex(invs)
            gram_latex = _form_gram_matrix_latex(self)
            label = self._form_matrix_latex_label()

            line1 = (
                f"A_L = {fp_latex} \\in \\mathrm{{Groups}} \\quad "
                "\\text{(Finite presentation)} \\\\"
            )
            line2 = (
                f"A_L \\cong {inv_str} \\in \\mathrm{{Groups}} \\quad "
                "\\text{(Invariant factor decomposition)} \\\\"
            )
            line3 = (
                f"A_L \\cong {prim_str} \\in \\mathrm{{Groups}} \\quad "
                "\\text{(Primary decomposition)} \\\\"
            )
            line4 = (
                f"{label} = {gram_latex} \\in "
                f"\\mathrm{{Mat}}_{{{n}}}({self._form_matrix_latex_codomain()})"
            )

            return (
                "\\begin{gathered}\n"
                + "\n".join([line1, line2, line3, line4])
                + "\n\\end{gathered}"
            )

        def _form_matrix_latex_label(self: Any) -> str:
            r"""Return the LaTeX label for this form's Gram matrix."""
            return "G_{A_L}"

        def _form_matrix_latex_codomain(self: Any) -> str:
            r"""Return the LaTeX codomain for this form's Gram matrix entries."""
            return "\\mathbb{Q}/\\mathbb{Z}"

    class ElementMethods:
        r"""What torsion adds to being an element of a module with a form.

        Which is one thing.  Addition and the $\mathbb Z$ action are
        $\mathbb Z\text{-Mod}$'s and are not a group's operation under another
        name; pairing and norm are :class:`FormModules`'s, since they are what
        having a form means and not what having a *torsion* one means.  Both
        arrive with membership.

        What is left is that the annihilator of an element is a nonzero ideal,
        so it has a generator -- a question that has no answer in a free form
        module, which is why it is stated here and not above.
        """

        def order(self: Any) -> Any:
            r"""Return the generator of $\operatorname{Ann}(a)$, asked of $U(a)$.

            A module question, and one the form has no part in, so it is put to
            the element's image under the fibration's projection.
            """
            return self.forget_form().order()


class CokernelForms(Category):
    r"""Torsion forms constructed as $\operatorname{coker}(f)$ for $f:L\to M$ of finite index.

    A construction, not a kind of object.  A torsion form is $(G,b)$ -- a
    finite torsion module and a form on it -- and is as primitive as a lattice
    $(L,b)$ is; nothing about it requires a morphism.  Taking the cokernel of a
    finite-index morphism of lattices is *one way* to obtain one, and the
    objects that arise that way carry more than the general ones do: the
    morphism itself, the lattice it maps into, and the projection from that
    lattice onto the classes.

    Finite index is the whole hypothesis.  It is what makes the cokernel
    torsion, and it is $\det f\ne 0$, which is where the construction is
    gated.  The morphism need not be a correlation: any $f:L\to M$ of finite
    index between lattices whose form descends gives a torsion form here, and
    the discriminant forms are the further special case $f=c$.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "cokernel torsion forms"

    def super_categories(self) -> list:
        return [TorsionModulesWithForm()]

    class ParentMethods:
        r"""What a lattice presentation adds, which is a cover and little else.

        Not the presentation itself -- every torsion form has one of those.
        What is special here is that $p$ maps between lattices, so its codomain
        is a lattice whose classes these are and which there is a projection
        from.  Every form method belongs to the torsion form this object
        already is; nothing below computes with a form.
        """

        def cover(self: Any) -> Any:
            r"""Return $M=\operatorname{codom} f$, whose classes these are."""
            return self.presentation().codomain()

        def projection(self: Any) -> Any:
            r"""Return $\pi:M\to G$, sending $M$'s $i$-th generator to this object's.

            Available because there is a cover to project from.  A torsion form
            built from a group and a matrix has no such morphism, which is the
            point of the refinement.
            """
            cover = self.cover()
            return _module_morphism(
                cover,
                self,
                {
                    label: self.generator(label)
                    for label in cover.generating_set()
                },
            )


class DiscriminantForms(Category):
    r"""The cokernels whose morphism is a correlation: $A_L=\operatorname{coker}(c:L\to L^\vee)$.

    A refinement, not a kind of object.  A torsion bilinear form is a finite
    torsion module with a form and nothing else -- $(G,b)$ for whatever $G$ and
    $b$, exactly as a lattice is $(L,b)$ -- and the ones that happen to be
    discriminant forms of a lattice are a special class of those.  What is
    special is a fact about the *presentation*: its domain is a lattice, so
    there is an $L$ to ask about, and $\pi$ has $L^\vee$ for its domain.

    So the two methods below live here and nowhere else.  A form written on
    invariant factor generators or on $p$-adic Jordan generators is presented
    by a morphism synthesized from that generating set, whose domain is a free
    module carrying a $\mathbb Q$-valued form; it is a perfectly good torsion
    form, it has a presentation, and it has no source lattice.  Before this
    split it answered ``source_lattice`` with that synthesized module.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "discriminant forms"

    def super_categories(self) -> list:
        return [CokernelForms()]

    class ParentMethods:
        r"""Methods available on the discriminant form of a lattice."""

        def correlation(self: Any) -> Any:
            r"""Return $c: L\to L^\vee$: the presentation, under its own name."""
            return self.presentation()

        def source_lattice(self: Any) -> Any:
            r"""Return the lattice $L$ this is the discriminant form of."""
            return self.presentation().domain()

        def dual(self: Any) -> Any:
            r"""Return $L^\vee$, which is what a correlation lands in."""
            return self.cover()


def cokernel_categories(morphism: Any) -> list:
    r"""Return the refinements ``morphism`` earns for its cokernel.

    Two independent questions, asked in order.  Is this the cokernel of a
    morphism of lattices at all -- which is what :class:`CokernelForms` is
    about, and which a synthesized presentation on some other generating set is
    not?  And if so, is that morphism the domain's own correlation, which is
    what makes the cokernel a discriminant form rather than one of the many
    other torsion forms a finite-index $f:L\to M$ produces?
    """
    domain = morphism.domain()
    if domain not in IntegralLattices():
        return []
    if morphism is domain.correlation():
        return [CokernelForms(), DiscriminantForms()]
    return [CokernelForms()]



def _coordinates_in_generators(
    element: Any,
    generating_set: Any,
) -> tuple[Any, ...]:
    r"""Return this element's coordinates in the requested generating set."""
    if hasattr(element, "coefficients"):
        coefficients = element.coefficients()
        return tuple(
            coefficients.get(generator, 0) for generator in generating_set
        )
    if hasattr(element, "_lift"):
        return tuple(element._lift())
    raise TypeError(
        f"{element} has no coordinate extraction compatible with the generating set"
    )


# ---- shared construction: a torsion form is a cokernel ----

def regenerating_data(form: Any, generators: Any) -> tuple:
    r"""Return the relations and Gram matrix of ``form`` on ``generators``.

    The data of a torsion form, which is all a torsion form is: a presentation
    of the group on the new generating set, and the matrix of the form with
    respect to it.  No morphism is invented to hold them -- the object built
    from this pair is a torsion form in its own right, and whether it is also
    anyone's cokernel is a separate question with, here, the answer no.

    Both are read off this object's own data.  Its Gram matrix is part of what
    it is -- the form *with respect to its chosen generators* -- so the new one
    is $RGR^{\mathsf T}$ for $R$ the new generators' coordinates, which is a
    change of generating set and not a pairing computed behind the form's back.
    """
    generators = list(generators)
    assert all(generator.parent() is form for generator in generators), (
        "a generating set for this object is made of its own elements; "
        "elements of another module reach it through a morphism"
    )
    underlying_set = tuple(form.forget_form().generating_set())
    rows = matrix(
        QQ,
        [
            list(_coordinates_in_generators(generator, underlying_set))
            for generator in generators
        ],
    )
    # The symmetric matrix the object is built on, whichever form it carries:
    # for a bilinear one its own, for a quadratic one its polarization's lift.
    gram = form.form().polar_form().gram_matrix()
    return relations_among(form, generators), rows * gram * rows.transpose()


def relations_among(form: Any, generators: Any) -> Matrix:
    r"""Return the relations among ``generators``: the kernel of $\mathbb Z^m\to A$."""
    generators = list(generators)
    known = form.forget_form().relation_matrix()
    width = known.ncols()
    underlying_set = tuple(form.forget_form().generating_set())
    lifts = matrix(
        ZZ,
        len(generators),
        width,
        [
            list(_coordinates_in_generators(generator, underlying_set))
            for generator in generators
        ],
    )
    kernel = lifts.stack(known).left_kernel().generator_matrix()
    return kernel[:, : lifts.nrows()]


def p_adic_jordan_generators(form: Any) -> list[Any]:
    r"""Return lifts of generators putting ``form`` in $p$-adic Jordan normal form.

    Sage's reduction is the engine and works on a realization, so one is built
    from this object's own relations and Gram, run, and discarded; only the
    generators it chooses come back, as coordinates in $L^\vee$.  Nothing is
    told a value group it does not have -- an even $L$ gives the scratch module
    a $q$ and the reduction normalizes $q$; an odd one gives it $b$ alone.

    The even case serves the bilinear side too: Peters--Sterk Prop. 11.2.3 puts
    normal forms for symmetric and quadratic torsion forms on the same group in
    bijection, and $b_q$ is the polarization on the same generators.
    """
    from sage.quadratic_forms.genera.normal_form import _normalize, p_adic_normal_form
    from sage.rings.padics.factory import Zp

    generators = []
    exponent = form.annihilator().gen()
    for p in exponent.prime_divisors():
        # The primary decomposition is where the reduction can run: it is one
        # generator per $p$-primary cyclic factor, so the form written on it
        # has the rank the group has.
        embedding = form.primary_part(p).structure_morphism()
        component = embedding.domain()
        engine = _p_adic_engine_matrix(component)

        # Degenerate directions are split off, normalized around, and put back.
        rank = engine.rank()
        match rank == engine.ncols():
            case True:
                split = engine.parent().identity_matrix()
            case False:
                integral = (engine * engine.denominator()).change_ring(ZZ)
                split = integral.hermite_form(transformation=True)[1]
        degenerate, nondegenerate = split[rank:, :], split[:rank, :]
        engine = nondegenerate * engine * nondegenerate.transpose()

        precision = exponent.valuation(p) + 5
        padics = Zp(p, type="fixed-mod", prec=precision)
        # The reduction is written for p-adic lattices, so it runs on the
        # inverse form and the transformation is carried back.
        transform = p_adic_normal_form(
            engine.inverse(), p, precision=precision + 5
        )[1]
        transform = transform.change_ring(ZZ).inverse().transpose()
        transform = transform.change_ring(padics).change_ring(ZZ)
        scaled = (
            transform
            * engine
            * transform.transpose()
            * p ** engine.denominator().valuation(p)
        )
        transform = (
            _normalize(scaled.change_ring(padics), normal_odd=False)[1].change_ring(ZZ)
            * transform
        )
        transform = (transform * nondegenerate).stack(degenerate)

        # A row of the transformation is a combination of the component's
        # generators, so it is that element's coordinate vector; the embedding
        # carries it back into the whole group.
        generators.extend(
            embedding(
                zipsum(
            row,
            component.module_generators(),
            component.zero(),
        )
            )
            for row in transform.rows()
        )
    return generators


def _p_adic_engine_matrix(form: Any) -> Matrix:
    r"""Return the matrix of representatives the $p$-adic reduction reads.

    Not a Gram matrix of anything: the reduction wants rational numbers, and
    these are chosen representatives of the form's values, scaled by the
    modulus so that the whole matrix lands in $[0,1)$.  The diagonal is the
    form's norm -- $q$ where there is one, $b(x,x)$ where there is not -- and
    that is where the two categories differ, because $q$ is read modulo
    $2\mathbb Z$ before scaling and $b(x,x)$ modulo $\mathbb Z$.
    """
    generators = tuple(
        form.generator(label)
        for label in form.generating_set()
    )
    size = len(generators)
    modulus = form.value_module().n

    def entry(i: int, left: Any, j: int, right: Any) -> Any:
        match i == j:
            case True:
                return left.norm().lift() / modulus
            case False:
                return left.b(right).lift() / modulus

    return matrix(
        QQ,
        [
            [
                entry(i, left, j, right)
                for j, right in enumerate(generators)
            ]
            for i, left in enumerate(generators)
        ],
    )


def _format_cyclic_group_latex(orders: tuple[int, ...]) -> str:
    r"""Format cyclic group orders as ``C_n^m``."""
    if not orders:
        return "0"
    from collections import Counter

    counts = Counter(orders)

    def cyclic_factor(n: int, multiplicity: int) -> str:
        assert multiplicity >= 1
        match multiplicity:
            case 1:
                return f"C_{{{n}}}"
            case _ if multiplicity > 1:
                return f"C_{{{n}}}^{{{multiplicity}}}"

    return " \\oplus ".join(
        cyclic_factor(n, counts[n])
        for n in sorted(counts)
    )


def _format_invariant_factor_latex(invariants: tuple[int, ...]) -> str:
    r"""Format invariant factors as ``C_n^m``."""
    return _format_cyclic_group_latex(invariants)


def _format_primary_decomp_latex(invariants: tuple[int, ...]) -> str:
    r"""Format the primary decomposition implied by invariant factors."""
    if not invariants:
        return "0"
    return _format_cyclic_group_latex(
        tuple(
            int(p) ** int(e)
            for n in invariants
            for p, e in factor(n)
        )
    )


def _form_gram_matrix_latex(module: Any) -> str:
    r"""Return LaTeX for a form Gram matrix."""
    import re

    if not module.invariants():
        return "()"
    gram_str = str(_latex_fn(module.gram_matrix()))
    zero_dots = globals().get("_zero_dots", lambda: False)
    if zero_dots():
        gram_str = re.sub(r"\b0\b", lambda m: r"\cdot", gram_str)
    return gram_str


def subdivide_form_gram_matrix(module: Any) -> None:
    r"""Partition ``module``'s Gram matrix once and replace ``gram_matrix``."""
    raw = module.gram_matrix()
    cuts = _form_gram_matrix_cuts(module, raw)
    match cuts:
        case []:
            G = raw
        case [_, *_]:
            G = raw.parent()(raw)
            G.subdivide(cuts, cuts)
    module.gram_matrix = lambda: G


def _form_gram_matrix_cuts(module: Any, raw: Any) -> list[int]:
    r"""Return the block cuts of ``module``'s form Gram matrix.

    The discriminant functor carries $L=\bigoplus L_i$ to $A=\bigoplus A_{L_i}$,
    so when the correlation's domain is decomposed its cuts are $A$'s -- and
    they have to be transported rather than recomputed, because a unimodular
    summand contributes a block of zeroes that reading the matrix alone would
    split into singletons.  A form on other generators has a synthesized domain
    carrying no decomposition, and there the matrix is all there is.
    """
    if raw.nrows() == 0:
        return []
    # Only a cokernel of a lattice morphism has a decomposition to transport:
    # the discriminant functor carries L = (+) L_i to A = (+) A_{L_i}, and a
    # unimodular summand contributes a block of zeroes that reading the matrix
    # alone would split into singletons.  A form on some other generating set
    # has no such morphism, and there the matrix is all there is.
    if module.category().is_subcategory(CokernelForms()):
        transported = list(
            module.presentation().domain().gram_matrix().subdivisions()[0]
        )
        if transported and max(transported) < raw.nrows():
            return transported
    return _matrix_connected_component_cuts(raw)
