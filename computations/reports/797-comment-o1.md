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
