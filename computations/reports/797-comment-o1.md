Intended comment on research#797, item 1 (O1), the coarse space of the stack of `def:coble-moduli-functor`.
The issue connector is read-only, so this is committed for the orchestrator to post.

---

**The page's "off $Z$" was wrong, and the correction does not save the step.** Clause 5 of
`rmk:coble-moduli-functor-five-clauses` had deduced that the Torelli step holds *off $Z$*, on the ground that
"there a member is Picard general (`def:picard-general-coble`), that is $\Pic(X)=S_\Co$". That ground is false.
$Z$ (`prop:the-coble-locus-in-the-period-domain`) is the union of the hyperplanes of the **$(-2)$-vectors of
$T_\Co$ only**; Picard-generality fails on the hyperplane of *every* nonzero vector of $T_\Co$. The two loci are
now named and separated on the page.

**What is proved, restated.** The period map $\mcM_\Co\to F_S$ is bijective on isomorphism classes over $\CC$ on
the **Picard-general locus**, the complement of $\bigcup_{d\ge1}\mch_{-2d}$ — a countable union of proper closed
analytic hyperplanes (`def:heegner-divisor`), dense complement — and not on $\bD\sm Z$. No isotropic or positive
vector contributes a hyperplane: no positive definite $2$-plane of $T_\Co\tensor\RR$ is orthogonal to a nonzero
vector of square $\ge0$, so the union over $d\ge1$ of the $(-2d)$-Heegner divisors is the whole
Noether--Lefschetz locus of $\bD(T_\Co)$. That union is **not** locally finite and no closedness is claimed for
it: a period orthogonal to the whole $E_8(2)$ summand (one whose positive $2$-plane is spanned by a class of
square $2$ in $\generators{2}$ and by $e+f$ for the isotropic $U(2)$ basis) lies in $\mch_{-2d}$ for infinitely
many $d$. Only $Z=\mch_{-2}$ is a locally finite arrangement, which is what makes it closed.
New block: `prop:coble-moved-minus-two-class` (moduli-construction.md:576, proof :584), clause 1.

**The question asked: is every $(-2)$-class of $\Pic(X')$ fixed by $\iota'$ off $Z$? No.** Clause 2 of the same
proposition gives a period and a class: $\bD\sm Z$ meets the $(-4)$-Heegner divisor, and at any period
$\pi\in\mch_{-4}$ outside $\mch_{-2d}$ for $d\neq2$ the Coble cover $X_\pi$ carries a class
$\delta\in\Pic(X_\pi)\intersect T_\Co$ of square $-4$; then $e_0+\delta$, with $e_0$ the class of square $2$ of
$S_\Co$, is a $(-2)$-class of $\Pic(X_\pi)$, and $\iota(e_0+\delta)=e_0-\delta$. So $s_{e_0+\delta}$ does not
commute with $\iota$, and the withdrawn sentence -- that every reflection in a $(-2)$-class of $\Pic(X')$
commutes with $\iota'$ -- is false on $\bD\sm Z$.

**What that does and does not decide.** It removes the page's justification off the Picard-general locus; it does
not decide the Torelli conclusion at the periods it produces. The statement that would close them is named on the
page (:570): a chamber-level form of `thm:automorphism-lifting-criterion` for the pair $(X',\iota')$ -- that an
$\iota'$-invariant Hodge isometry of $T_\Co$ extending to $\Lambda_{\mathrm{K3}}$ and carrying a Kähler class of
$X$ into the Kähler cone of $X'$ is realised by an isomorphism of pairs. No numbered statement on the page gives
it.

**One observation recorded here and deliberately not put on the page.** The reflection-trick element $w$ is
*unique*: the Kähler cone is a fundamental domain for $W(-2)(\Pic X')$ on the positive cone
([@PS24, Proposition 19.1.3(2)]), so the element carrying $\varphi\mathcal K_X$ to $\mathcal K_{X'}$ is unique.
Conjugation by $\iota'$ preserves $W(-2)(\Pic X')$ -- $s_{\iota'(\xi)}=\iota' s_\xi\iota'$ and
$\iota'(\xi)^2=\xi^2$ -- and $\iota'\varphi=\varphi\iota$ with $\iota(\mathcal K_X)=\mathcal K_X$,
$\iota'(\mathcal K_{X'})=\mathcal K_{X'}$ give $(\iota' w\iota')\varphi\mathcal K_X=\iota'\mathcal K_{X'}=\mathcal K_{X'}$;
by uniqueness $\iota' w\iota'=w$. If this is right, $w$ commutes with $\iota'$ unconditionally, the "Picard rank
eleven" case and the counterexample above are both unnecessary, and the Torelli step is unconditional up to the
choice of representative in the $\Gamma_\rho$-coset of $\varphi$ (the sign of the positive cone, absorbed by
$-\id\in\Gamma_\rho$ acting trivially on $\bD_S$). **This is not proved on the page and no statement there depends
on it**; it contradicts nothing recorded, but it would supersede the case split of :568--:571 and should be checked
independently before it does. The two inputs it needs are the fundamental-domain statement above and the
uniqueness of the element, which is what "fundamental domain" means.

**Acceptance, item by item.**

- "Read `rmk:coble-moduli-functor-five-clauses` first" -- MET.
- "Restate the conclusion on the locus proved, the complement of the Noether--Lefschetz locus" -- MET,
  moduli-construction.md:569 and :571.
- "Decide whether off $Z$ every $(-2)$-class of $\Pic(X')$ is fixed by $\iota'$; if not, give a period off $Z$ and
  a $(-2)$-class that $\iota'$ moves" -- MET, decided **negative**, with the period and the class in
  `prop:coble-moved-minus-two-class(2)` (:581, proof :590--:591).
- "If so, bijectivity extends off $Z$" -- not applicable: it does not, and the page no longer says it does.
- O1's **algebraicity**: NOT MET, unchanged. No smooth atlas is exhibited; `prop:coble-stack-as-quotient` charts
  the classical substack, and the two candidate atlases are not essentially surjective
  (:558, clause 3). Nothing this turn bears on it.
- O1's **coarse space**: NOT MET, but narrowed. Bijectivity on isomorphism classes over $\CC$ is decided on an
  open dense locus; it is open on $\bigcup_{d\ge2}\mch_{-2d}$ inside the Coble locus; and the universal property
  of a coarse space is not addressed anywhere, so $F_S$ is not a coarse space of $\mcM_\Co$ on what is proved
  (:571).

**Checks.** `scripts/docs_check.py --source`: 29 findings, before and after the edit, none naming
`moduli-construction.md`. `scripts/docs_dependency_graph.py` not run: `panflute` is absent from this checkout.
`tests/engineering/test_coble_797_items34.py` cannot be collected here (`tests/conftest.py` imports
`dzack_research`, absent from a plain checkout); its 28 test functions were run directly instead, 26 pass, and
the 2 that fail -- `test_injectivity_comes_from_the_chamber_not_from_an_ample_class` and
`test_the_subclass_with_a_plane_model_is_named` -- fail identically at the base commit `12bd1c4875`, so they are
pre-existing. Three tests added and passing: the locus of clause 1, the counterexample of clause 2, and a guard
that bites if the withdrawn sentence returns. CI is not visible from this session.

---

**Update, after the coordinator's ruling on the reported argument.** The argument reported last round is on
the page and is now the statement, not a note: `thm:coble-torelli-for-pairs`, with its proof, immediately after
the remark.

*What it says.* For two Coble covers $(X,\iota)$, $(X',\iota')$ and a Hodge isometry $\varphi\colon H^2(X)\iso
H^2(X')$ with $\varphi\iota=\iota'\varphi$ — the datum of equal periods in $F_S=(\bD_S-\Delta)/\Gamma_\rho$ —
there is $u$ in the group generated by the reflections in the $(-2)$-classes of $\Pic(X')$, commuting with
$\iota'$, and an isomorphism of pairs $f\colon(X',\iota')\iso(X,\iota)$ with $f^*=u\varphi$, after replacing
$\varphi$ by $-\varphi$. Hence $\mcM_\Co\to F_S$ is bijective on isomorphism classes over $\CC$ on the image of
$\bD(T_\Co)\sm Z$: on the **whole Coble locus**, with no hypothesis on $\Pic$. The previous round's restriction to
the Picard-general locus is superseded and is no longer asserted anywhere.

*The steps, each quoted by number from a source on this machine* (Peters--Sterk, read in
`references/literature/lattice-research/peters-sterk_symmetric-quadratic-forms.md`): Proposition 19.1.3(2), "If
$X$ is projective, the closure of the ample cone is a fundamental domain for the action of the Weyl group
$\mathsf W^-(X)$ on the intersection of the positive cone with $\mathsf{NS}(X)\otimes\mathbb R$"; Proposition
17.2.5(3), "$\mathsf W(L)$ acts simply transitively on root bases and on Weyl chambers"; the proof of Corollary
19.2.3, "For a unique element $w\in\mathsf W^-(X)$, $\pm w\circ\gamma(\kappa)\in\mathsf C_X^{\mathrm{Kah}}$";
Theorem 19.2.2 for the Torelli criterion; Theorem 19.2.1(1) for the existence of one isomorphism to conjugate by;
SS19.1 for "it preserves the positive cone", for "Reflections in $(-2)$-roots in $\mathsf{NS}(X)$ generate its
Weyl group" and for "If $X$ is projective, the ample classes belong to the Kähler cone"; SS19.2 for "two markings
$\varphi,\varphi'$ give the same period point in case the markings are opposite, i.e., $\varphi'=-\varphi$". The
component of the positive cone is handled by $-\id\in\Gamma_\rho$, which acts trivially on $\bD_S$.

*The case split.* Kept, as remarks, and marked as superseded: (a) Picard rank eleven, where $\iota'$ is the
identity on $\Pic(X')=S_\Co$ so every reflection commutes with it; and (b) the periods off $Z$ where
`prop:coble-moved-minus-two-class(2)` shows a $(-2)$-class is moved — so the earlier route's hypothesis really
fails there, and what makes $u$ commute with $\iota'$ is its uniqueness, not the commutation of its factors.

*The universal property.* Named as the failing step, with the reason: a morphism from $\mcM_\Co$ to a complex
space is automatically constant on isomorphism classes (a complex space is a sheaf of sets), so what is missing is
that the induced map of sets is holomorphic; what would supply it is a chart whose composite to $F_S$ is a
categorical quotient in complex spaces, and no chart exists on the page (clause 3, open). What is NOT claimed is
that the universal property fails.

*Acceptance.* O1 algebraicity: NOT MET, unchanged. O1 coarse space: first clause MET on the whole Coble locus
(`thm:coble-torelli-for-pairs`); universal property NOT MET, waiting on the atlas of clause 3. A parallel search on
the universal property is running and its findings will be reported separately.

*Correction to the universal-property paragraph, after a parallel search.* The paragraph first written said that what is
missing is the holomorphy of the induced set map $|F|\to|Z|$. That is wrong, and it is withdrawn on the page: a
morphism $g\colon\mcM_\Co\to Z$ is constant on isomorphism classes automatically, and the induced set map is
holomorphic, because about each point of the Coble locus the family over a ball of the proof of
`thm:coble-period-surjectivity` has period map an isomorphism onto an open subset of $\bD(T_\Co)$, the stabiliser
of a period is finite (`lem:period-stabiliser-finite`, on $T_\Co$ of signature $(2,9)$), and on a ball on which
only that finite group acts the period map is the quotient of a ball by a finite group. What is missing is the
descent for *families*: a chart $U\to\mcM_\Co$ whose composite $U\to F_S$ is a categorical quotient in complex
spaces, so that every object of $\mcM_\Co$ is locally after base change a pullback of the one family over $U$.
Clause 3 is still the statement that would close it, and it is still open. The equivalence of this with "the
period map is locally injective on isomorphism classes of families" is asserted by that search's report but not
proved there (its proof of the reverse implication assumes the finite cover it is meant to produce), so it is not
on the page.
