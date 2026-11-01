# Open work in this repository

Writing and mathematics only. An item belongs here if it is a hole in the prose or a question of
mathematics the book needs settled. Code, tooling, the library, the build, and the state of any
computation do not belong here; library work is upstream
([`sage-extensions` #7--#13](https://github.com/dzackgarza/sage-extensions/issues)) and computation
status lives in [GAPS](writing/dissertation/GAPS.md).

Each item states what is missing from the mathematics or the text, and what writing it would take.

## Holes in the prose

1. **`F_{\Nod,2}` is undefined.** The display of moduli spaces in `moduli-construction.md` gives it as
   `???` beside $F_\Nod$. Either it is $\mathbf D(T_\Nod)$ modulo a group that should be named, or the
   row does not belong.

2. **The tower diagram carries a `?`.** The map $F_{\Co,2}\to\fco$ is undetermined because
   $\Gamma_{\Co,2}$ has no explicit description, and degree-$2$ polarized Coble surfaces appear nowhere
   in the earlier literature. Either $\Gamma_{\Co,2}$ is described, or the arrow goes and the text says
   why the tower stops. A `?` inside a commutative diagram is the one place a reader cannot tell
   conjecture from typo.

3. **One group, two names.** The book writes $\Gamma_\Co=\Orth^+(T_\Co)^*$, spells the star out as the
   discriminant kernel in `moduli-construction.md`, and defines
   $\widetilde O^+(L)=\ker(\rho_L,\chi_{\mathrm{sp}})$ in `clifford-lifting-and-spinor-obstructions.md`.
   These are the same group by substitution and the book never says so, leaving a reader unable to tell
   whether the equality is asserted or assumed.

## Open mathematics

4. **Primitive isotropic planes of $T_\Co$ under $\Gamma_\Co$.** How many orbits, equivalently whether
   $\fco$ has one $1$-cusp or several. $\Orth^+(T_\Co)$ is transitive, by `thm:plane-transitivity-tco`.
   For $\Gamma_\Co$ the candidate separator is the subspace a plane cuts out of $A_{T_\Co}$, and
   whether it separates is undecided. A generating set for $\Gamma_\Co$ is not known, which is what
   either route to the count needs.

5. **The decomposition $[1,2,120,135,270]$ is asserted and not proved.** It is claimed to be the orbit
   decomposition of the $528$ isotropic classes under $G_\Co$, and nothing in the book establishes that
   $G_\Co$ has order $696\,729\,600$ or that its orbits have those lengths. The claim is consistent with
   the proved coarser list and the index $136$, which is a check and not a proof.

6. **The decomposition $[1,255,272]$ is half proved.** Its three parts are known to partition the $528$
   isotropic classes; that they are the orbits of the stabilizer of the polarization class is not
   established. Until then the three numbers are computed rather than proved, and the chapter says so.

7. **$\Gamma_\Co$ acts on the cusp correspondence only weakly.** `rmk:descent-of-an-equivariant-inclusion`
   proves pointwise orbit compatibility and needs a homomorphism for equivariance and for comparing
   stabilizers. The strong form is missing.

8. **Vector-level transitivity for $\latI_{1,8}$.** `prop:rank-nine-line-transitivity` leaves open
   whether $\Orth^+(\latI_{1,8})$ is transitive on primitive isotropic vectors, not only on lines. For
   signature $(2,9)$ it follows, since $-\id$ lies in $\Orth^+$ there and supplies the sign; the $(1,8)$
   case is where that fails.

9. **Ste91's group.** `thm:orbit-classification-sterk` and the proof of Lemma 4.2.1 in `475-our-cusps.md`
   rest on a theorem whose group the book cannot confirm, the paper being unavailable. The chapter keeps
   the source's group as stated and flags the item number as unconfirmed. Settling it needs the source.
