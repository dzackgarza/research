r"""Finite torsion modules equipped with a bilinear or quadratic form."""

from typing import Any

from sage.arith.misc import factor
from sage.categories.category import Category
from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.matrix.matrix0 import Matrix
from sage.modules.fg_pid.fgp_morphism import FGP_Morphism
from sage.misc.latex import latex as _latex_fn
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_morphism import FreeModuleMorphism


class TorsionFormMorphism(FGP_Morphism):
    r"""A map of torsion modules with form that preserves the form.

    One type for both subcategories: a map of bilinear modules and a map of
    quadratic ones are the same kind of thing, and what differs -- which form
    has to be preserved -- is behaviour, so it lives in each category's
    ``MorphismMethods`` rather than in a second class.
    """


class TorsionModulesWithForm(Category):
    r"""Category of finite torsion modules equipped with a form."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "torsion modules with form"

    def super_categories(self) -> list:
        return [OwnedFiniteGroups()]

    class ParentMethods:
        r"""Methods shared by bilinear and quadratic discriminant modules."""

        def relation_matrix(self: Any) -> Matrix:
            r"""Return the relations among :meth:`gens`, one per row."""
            return relations_among(self, self.gens())

        def as_finitely_presented_group(self: Any) -> FinitelyPresentedGroup:
            r"""Return a Sage-native ``FinitelyPresentedGroup`` representing $A_L$.

            The relations come from the module's own cover and relation
            submodule, $A=V/W$, not from any lattice it happened to be built
            from -- a normal form has no such lattice, and asking one for its
            Gram matrix is what used to break the display.  For the cokernel
            $A_L$ the matrix below *is* $L$'s Gram, so nothing changes there.
            """
            G = self.relation_matrix()
            r = G.nrows()
            from sage.groups.free_group import FreeGroup
            from sage.misc.misc_c import prod

            if r == 0:
                F = FreeGroup(0, "e")
                return F.quotient([])

            names = [f"e{i+1}" for i in range(r)]
            F = FreeGroup(names)
            gens = F.gens()
            rels = []
            for i in range(r):
                for j in range(i + 1, r):
                    rels.append(gens[i] * gens[j] * (gens[i] ^ -1) * (gens[j] ^ -1))
            for k in range(r):
                word = prod((gens[j] ^ int(G[j, k])) for j in range(r))
                rels.append(word)
            return F.quotient(rels)

        def abelian_group(self: Any) -> AbelianGroup_class:
            r"""Return the underlying finite abelian group in invariant-factor form."""
            from sage.groups.abelian_gps.abelian_group import AbelianGroup

            return refine(
                own_group_types(AbelianGroup(list(self.invariants()))),
                OwnedFiniteGroups(),
            )

        def is_p_elementary(self: Any, p: Any) -> bool:
            r"""Return whether the underlying group is elementary abelian of exponent \(p\)."""
            from sage.rings.integer_ring import ZZ

            p = ZZ(p)
            assert p.is_prime(), f"p must be prime, got {p}"
            G = self.abelian_group().permutation_group()
            if not G.is_elementary_abelian():
                return False
            return G.order() == 1 or G.exponent() == p

        def _latex_(self: Any) -> str:
            r"""Return multi-line LaTeX for the torsion module and its form."""
            invs = self.invariants()
            n = self.gram_matrix().nrows()

            fp_latex = str(_latex_fn(self.as_finitely_presented_group()))
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


# ---- shared construction: a torsion form is a cokernel ----

def cokernel_of(morphism: LatticeMorphism) -> tuple[Any, Any]:
    r"""Return ``(codomain, relations)`` for $\operatorname{coker}$ of ``morphism``.

    A morphism of lattices with generating sets has a unique matrix, and its
    cokernel is settled by it: the generating set is the images of the
    codomain's, and the Gram matrix is the codomain's read in the value group.
    Nothing here is chosen.
    """
    domain, codomain = morphism.domain(), morphism.codomain()
    relations = morphism.matrix()
    assert relations.is_square(), (
        f"f: A -> B must have equal ranks; got {relations.dimensions()}"
    )
    # A morphism of lattices with generating sets preserves the forms.  Not
    # every free-module morphism does, and only the ones that do have a
    # cokernel this category can carry.
    transported = relations * codomain.gram_matrix() * relations.transpose()
    assert transported == domain.gram_matrix(), (
        "f must be a morphism of lattices with generating sets, but it does not "
        f"preserve the form: M G_B M^T is {transported}, not {domain.gram_matrix()}"
    )
    assert relations.det() != 0, (
        "f must be injective, or the cokernel is not torsion"
    )
    descent = relations * codomain.gram_matrix()
    assert all(entry in ZZ for entry in descent.list()), (
        "the form does not descend to the cokernel: the relations must pair "
        f"integrally with the generators, but f's matrix times B's Gram is {descent}"
    )
    return codomain, codomain.span(
        codomain.linear_combination_of_basis(row) for row in relations.rows()
    )


def cokernel_morphism(gram_matrix: Matrix, relations: Matrix) -> LatticeMorphism:
    r"""Return the morphism whose cokernel has this Gram matrix and these relations.

    The codomain is the lattice on the named generating set carrying
    ``gram_matrix``; the domain is the one the relations span, whose Gram
    $RBR^{\mathsf T}$ is forced by the morphism being form-preserving.  This is
    how a torsion form on new generators is *built* -- as a new morphism, since
    a different generating set is a different codomain and so a different
    morphism.
    """
    gram_matrix = matrix(QQ, gram_matrix)
    relations = matrix(ZZ, relations)
    codomain = RationalLattice(gram_matrix)
    domain = RationalLattice(relations * gram_matrix * relations.transpose())
    # Through the refined homset, so the result is checked and owned: a bare
    # ``domain.hom`` would hand back a FreeModuleMorphism with no form check,
    # since a RationalLattice does not refine its own Hom.
    homset = refine(domain.Hom(codomain), LatticeHomomorphisms())
    return homset(
        [codomain.linear_combination_of_basis(row) for row in relations.rows()]
    )


def regenerated_by(form: Any, lifts: Any) -> LatticeMorphism:
    r"""Return the morphism presenting ``form`` on the generators these lifts name.

    The lifts are elements of the current codomain; their pairings there give
    the new codomain's Gram matrix, and the relations among their images give
    its relations.  Both come out of the object, so the result is a morphism and
    not a second piece of data hung off this one.
    """
    lifts = list(lifts)
    gram = form.V().gram_matrix()
    new_gram = matrix(
        QQ, [[left * gram * right for right in lifts] for left in lifts]
    )
    generators = [form(lift) for lift in lifts]
    return cokernel_morphism(new_gram, relations_among(form, generators))


def form_morphism(domain: Any, images: Any, codomain: Any) -> TorsionFormMorphism:
    r"""Return the morphism of torsion forms with these images, typed by its category.

    Sage's FGP machinery hardcodes ``FGP_Morphism`` when it builds a map, so the
    class is reassigned afterwards -- the same ``__class__`` move override-refine
    makes.  The morphism is checked to preserve the form, which is what makes it
    a morphism of this category rather than of underlying groups.
    """
    from sage.cpython.type import can_assign_class

    images = list(images)
    morphism = domain.hom(images, codomain=codomain)
    for i, left in enumerate(domain.gens()):
        for j, right in enumerate(domain.gens()):
            assert left.b(right) == morphism(left).b(morphism(right)), (
                f"morphism does not preserve b at ({i}, {j})"
            )
    assert can_assign_class(morphism), (
        f"cannot own the type of {type(morphism).__name__}"
    )
    morphism.__class__ = TorsionFormMorphism
    return morphism


def relations_among(form: Any, generators: Any) -> Matrix:
    r"""Return the relations among ``generators``: the kernel of $\mathbb Z^m\to A$."""
    generators = list(generators)
    cover, relations = form.V(), form.W()
    coordinates = cover.basis_matrix().solve_left
    width = cover.rank()
    # Sized explicitly: a trivial group has no generators, and an empty matrix
    # with no columns cannot be stacked against the relations.
    lifts = matrix(
        ZZ, len(generators), width, [list(coordinates(g.lift())) for g in generators]
    )
    known = matrix(
        ZZ,
        relations.rank(),
        width,
        [list(coordinates(w)) for w in relations.basis_matrix().rows()],
    )
    kernel = lifts.stack(known).left_kernel().basis_matrix()
    return kernel[:, : lifts.nrows()]


def p_adic_jordan_generators(form: Any) -> list[Any]:
    r"""Return lifts of generators putting ``form`` in $p$-adic Jordan normal form.

    The reduction is Sage's, run on a scratch realization built from this
    object's own cover and relations and then discarded; only the generators it
    chooses come back.  Nothing is told a value group it does not have: for an
    even $L$ the scratch module carries $q$ and the reduction normalizes $q$;
    for an odd $L$ it carries $b$ alone and normalizes $b$.

    The even case serves the bilinear side too.  Peters--Sterk Prop. 11.2.3
    puts normal forms for symmetric and quadratic torsion forms on the same
    group in bijection, and $b_q$ is the polarization on the same generators --
    so generators that make $q$ block-diagonal make $b$ block-diagonal in the
    corresponding blocks.
    """
    from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

    scratch = TorsionQuadraticModule(form.V(), form.W())
    reduced = TorsionQuadraticModule.normal_form(scratch)
    return [generator.lift() for generator in reduced.gens()]


def _format_cyclic_group_latex(orders: tuple[int, ...]) -> str:
    r"""Format cyclic group orders as ``C_n^m``."""
    if not orders:
        return "0"
    from collections import Counter

    counts = Counter(orders)
    parts = []
    for n in sorted(counts):
        m = counts[n]
        if m == 1:
            parts.append(f"C_{{{n}}}")
        else:
            parts.append(f"C_{{{n}}}^{{{m}}}")
    return " \\oplus ".join(parts)


def _format_invariant_factor_latex(invariants: tuple[int, ...]) -> str:
    r"""Format invariant factors as ``C_n^m``."""
    return _format_cyclic_group_latex(invariants)


def _format_primary_decomp_latex(invariants: tuple[int, ...]) -> str:
    r"""Format the primary decomposition implied by invariant factors."""
    if not invariants:
        return "0"
    primary_orders: list[int] = []
    for n in invariants:
        primary_orders.extend(int(p) ** int(e) for p, e in factor(n))
    return _format_cyclic_group_latex(tuple(primary_orders))


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
    if cuts:
        G = raw.parent()(raw)
        G.subdivide(cuts, cuts)
    else:
        G = raw
    module.gram_matrix = lambda: G


def _form_gram_matrix_cuts(module: Any, raw: Any) -> list[int]:
    r"""Return the block cuts of ``module``'s form Gram matrix.

    The discriminant functor carries $L=\bigoplus L_i$ to $A=\bigoplus A_{L_i}$,
    so when the morphism's domain is decomposed its cuts are $A$'s -- and they
    have to be transported rather than recomputed, because a unimodular summand
    contributes a block of zeroes that reading the matrix alone would split into
    singletons.

    A regenerated object has a domain synthesized from its own relations, which
    carries no decomposition; there the blocks are whatever its Gram matrix
    shows.
    """
    n = raw.nrows()
    if n == 0:
        return []

    source = module.source_lattice()
    if source is not None and n == source.rank():
        transported = list(source.gram_matrix().subdivisions()[0])
        if transported:
            return transported
    return _matrix_connected_component_cuts(raw)
