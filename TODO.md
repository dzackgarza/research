# Open work in this repository

Research and exposition obligations that nothing in the tree has closed. The preamble and library
programme that used to live here is posted upstream as
[`sage-extensions` #7--#13](https://github.com/dzackgarza/sage-extensions/issues); this repository's
preamble is a two-file re-export of `sage_extensions.all`, so none of that work belongs here.

## Unfinished text in the book

1. **`F_{\Nod,2}` is undefined.** `moduli-construction.md` lists it beside $F_{\Nod}$ in a display of
   moduli spaces and gives `???` as its definition. Either it is a quotient of $\mathbf D(T_\Nod)$ by a
   named group, in which case it should be written, or the row should go. The same display's
   $\Gamma_{\Co,2}=\operatorname{Stab}_{\Orth(\ten)}(T_\Co)$ is written but not characterised beyond
   that, and the question block under it says so.

2. **The map $F_{\Co,2}\to\fco$ in the tower diagram, marked `?`.** It is undetermined for the stated
   reason: no explicit description of $\Gamma_{\Co,2}$ is known, and the prose records that degree-$2$
   polarized Coble surfaces appear nowhere in the earlier literature. Closing it means either
   describing $\Gamma_{\Co,2}$ or removing the arrow and saying why the tower stops there. A `?` in a
   commutative diagram is the one place a reader cannot tell conjecture from typo.

## Open mathematics

3. **Identify the two names of one group.** `lattices.md` defines
   $\Gamma_\Co \definedas \Orth^+(T_\Co)^*$, `moduli-construction.md` spells the star out as the
   discriminant kernel, and `clifford-lifting-and-spinor-obstructions.md` defines
   $\widetilde O^+(L)=\ker(\rho_L,\chi_{\mathrm{sp}})$. They are the same group by substitution, and
   the book never says so. A reader cannot tell whether the equality is asserted or assumed.

4. **The number of $\Gamma_\Co$-orbits of primitive isotropic planes**, equivalently whether $\fco$
   has one $1$-cusp or several. The full-group statement is `thm:plane-transitivity-tco`. The
   candidate separator is the subspace a plane cuts out of $A_{T_\Co}$; whether it separates is
   undecided. Nothing in the tree gives a generating set for $\Gamma_\Co$, which is what an orbit
   computation would need.

5. **The fine Heegner decomposition $[1,2,120,135,270]$ under $G_\Co$** has no certificate. It needs
   the image of $G_\Co$ in $\Orth(q_{T_\Co})$, which needs $\Gamma_\Co$'s generators reduced through
   the gluing identification the book lists as open. The two lists and the index $136$ are
   cross-checked against each other, so a computation contradicting one is immediately visible.

6. **The $\Gamma_\Co$-lifting in the cusp correspondence** --- the strong form of
   `rmk:descent-of-an-equivariant-inclusion`, a homomorphism rather than pointwise orbit
   compatibility. The weak form is proved; the strong form is what equivariance and stabilizer
   comparison use.

7. **Vector-level transitivity under $\Orth^+(\latI_{1,8})$**, left open by
   `prop:rank-nine-line-transitivity`. For signature $(2,9)$ it does follow, because $-\id$ lies
   inside $\Orth^+$ there and supplies the sign; the $(1,8)$ case is the one where that fails.

## Verification debt

8. **The coarse decomposition $[1,255,272]$** is partition-checked and generator-unchecked. The run
   stopped after `stabilizer generators: 1984`, before the block asserting that each generator fixes
   the polarization class and preserves $q$. Do not rerun the exhaustive loop as written; the
   maintained alternative is in [GAPS](writing/dissertation/GAPS.md), awaiting review.

9. **Ste91's source group.** `thm:orbit-classification-sterk` and the proof of Lemma 4.2.1 in
   `475-our-cusps.md` quote the paper, which is not in this tree; the corpus has no match and both
   eudml and the Radboud repository refuse automated access. The book keeps the source's group as
   stated and marks the item number unconfirmed. Closing it needs the paper.
