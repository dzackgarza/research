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
            return self.module().relation_matrix()

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

def discriminant_gram(morphism: Any) -> Any:
    r"""Return the Gram matrix $A_L$ inherits: $L^\vee$'s, on its own generators."""
    return morphism.codomain().gram_matrix()


def regenerated_by(form: Any, lifts: Any) -> Any:
    r"""Return the morphism presenting ``form`` on the generators these lifts name.

    A different generating set is a different codomain, hence a different
    morphism: the lifts' pairings give the new codomain's Gram, the relations
    among their images give the new relations, and the domain's Gram
    $RBR^{\mathsf T}$ is forced by the morphism preserving forms.
    """
    lifts = [vector(QQ, lift) for lift in lifts]
    gram = discriminant_gram(form.correlation())
    new_gram = matrix(QQ, [[left * gram * right for right in lifts] for left in lifts])
    relations = relations_among(form, [form(lift) for lift in lifts])
    codomain = free_form_module(new_gram, QQ)
    domain = free_form_module(relations * new_gram * relations.transpose(), QQ)
    return FormMorphism(domain, codomain, relations)


def relations_among(form: Any, generators: Any) -> Matrix:
    r"""Return the relations among ``generators``: the kernel of $\mathbb Z^m\to A$."""
    generators = list(generators)
    known = form.module().relation_matrix()
    width = known.ncols()
    lifts = matrix(
        ZZ, len(generators), width, [list(g.coordinates()) for g in generators]
    )
    kernel = lifts.stack(known).left_kernel().basis_matrix()
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
    from sage.modules.free_quadratic_module import FreeQuadraticModule
    from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

    relations = matrix(ZZ, form.module().relation_matrix())
    realized = FreeQuadraticModule(ZZ, relations.nrows(), relations)
    reduced = TorsionQuadraticModule.normal_form(
        TorsionQuadraticModule(realized.span(relations.inverse().rows()), realized)
    )
    return [generator.lift() * relations for generator in reduced.gens()]


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
    so when the correlation's domain is decomposed its cuts are $A$'s -- and
    they have to be transported rather than recomputed, because a unimodular
    summand contributes a block of zeroes that reading the matrix alone would
    split into singletons.  A form on other generators has a synthesized domain
    carrying no decomposition, and there the matrix is all there is.
    """
    if raw.nrows() == 0:
        return []
    correlation = getattr(module, "_morphism", None)
    if correlation is not None:
        transported = list(correlation.domain().gram_matrix().subdivisions()[0])
        if transported and max(transported) < raw.nrows():
            return transported
    return _matrix_connected_component_cuts(raw)
