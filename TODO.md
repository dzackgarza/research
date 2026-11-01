# Work in this repository

This file was the preamble programme: 134 leaf issues under seven cluster parents, all of them
about the `sage-extensions` library, tracked here because the preamble used to live in this tree.
It does not any more. `src/dzack_research/preamble/` is two files and about 12 KB, and `all.py` is
`from sage_extensions.all import *`; the categories, modules, algebras, schemes, lattices and
engines that every issue body cites are in the library, which `pyproject.toml` takes from
`git+https://github.com/dzackgarza/sage-extensions`. Issue #482 makes the drift concrete: it cites
`src/dzack_research/preamble/categories/lattices.py:1444`, a path that does not exist here, and at
the retained pin line 1444 of the real file is not the site it names.

That programme is factored out and posted upstream: the seven clusters are now
[issues #7--#13 of `dzackgarza/sage-extensions`](https://github.com/dzackgarza/sage-extensions/issues),
one per former milestone, each carrying that milestone's source identifiers.
[docs/issue-migration/sage-extensions.md](docs/issue-migration/sage-extensions.md) records the
evidence, the per-cluster issue number, and the full leaf mapping from source identifier to the
`research` issue that still carries it. The `research` issues stay open here as pointers until
their clusters close upstream; #482 is the example of why they should not be worked here -- it
cites a path this repository does not contain.

## What this repository owns

- `writing/` --- the book. Not externalized to GitHub issues or PRs by policy
  ([AGENTS.md](AGENTS.md), "Documentation work"); developed directly, pushed after an
  interactive pass.
- `computations/` --- the reports that certify sentences in the book.
- `docs/theory/` --- the proof notes those reports and chapters cite.
- `subrepos/`, `formalization/*` --- submodules; their work belongs to their own repositories.

## The standard a claim has to meet

A mathematical claim in `writing/` is one of three things: proved in the text, cited to a source
someone opened, or marked open with the question stated sharply enough to attack. A computation
exists to certify a sentence; it is not a result on its own. Anything withdrawn goes in
[writing/dissertation/GAPS.md](writing/dissertation/GAPS.md) and stays there.

## Open book obligations

Ordered by what unblocks the most prose.

1. **Identify the two names of one group.** `lattices.md` defines
   $\Gamma_\Co \definedas \Orth^+(T_\Co)^*$, `moduli-construction.md` spells the star out as the
   discriminant kernel, and `clifford-lifting-and-spinor-obstructions.md` defines
   $\widetilde O^+(L)=\ker(\rho_L,\chi_{\mathrm{sp}})$. The two are the same group by substitution.
   The book never says so, and a reader cannot tell whether an equality is asserted or assumed.
   Closing it: one sentence and one cross-reference where the notation is introduced.

2. **The number of $\Gamma_\Co$-orbits of primitive isotropic planes**, equivalently whether
   $\fco$ has one $1$-cusp or several. Open in the text. The full-group statement is
   `thm:plane-transitivity-tco`; the candidate separator is the subspace a plane cuts out of
   $A_{T_\Co}$, and whether it separates is undecided. Closing it: a comparison of the two
   exhibited planes' subspaces in one presentation of $T_\Co$ --- which the book does not yet
   construct --- or an orbit computation under a generating set for $\Gamma_\Co$, which the book
   also lacks.

3. **The fine Heegner decomposition $[1,2,120,135,270]$ under $G_\Co$** has no certificate.
   Closing it: the image of $G_\Co$ in $\Orth(q_{T_\Co})$, which needs the generators of
   $\Gamma_\Co$ reduced through the gluing identification the book lists as open. The two lists and
   the index $136$ are cross-checked against each other (`thm:coble-heegner-finite-orbits`), so a
   computation contradicting one is immediately visible.

4. **The coarse decomposition $[1,255,272]$** is partition-checked and generator-unchecked: the
   capped run stopped after `stabilizer generators: 1984`, before the block asserting that each
   generator fixes the polarization class and preserves $q$. Do not rerun the exhaustive loop as
   written; the maintained alternative is recorded in
   [GAPS](writing/dissertation/GAPS.md) and awaits review.

5. **The $\Gamma_\Co$-lifting in the cusp correspondence** --- the strong form of
   `rmk:descent-of-an-equivariant-inclusion`, a homomorphism rather than pointwise orbit
   compatibility. The weak form is proved; the strong form is what equivariance and stabilizer
   comparison use.

6. **Ste91's source group.** `thm:orbit-classification-sterk` and the proof of Lemma 4.2.1 in
   `475-our-cusps.md` quote the paper. It is not retained in this tree, the corpus has no match,
   and both eudml and the Radboud repository refuse automated access. The book keeps the source's
   group as stated and marks the item number unconfirmed. Closing it needs the paper.

7. **Vector-level transitivity under $\Orth^+(\latI_{1,8})$**, left open by
   `prop:rank-nine-line-transitivity`. Note the contrast the book now draws: for signature $(2,9)$
   it does follow, because $-\id$ lies inside $\Orth^+$ there and supplies the sign.

## Where work is tracked

The research issue tree (#46) remains for implementation and research work that is this
repository's; the book is deliberately not in it. Library work goes upstream.
