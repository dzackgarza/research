Intended comment for research#802 (the issue connector here is read-only; the orchestrator posts it).

## K4: **refuted**, both equivalences, by automorphism groups

Commit `6aaa39cc1735bd1d68a72dec5a062b67bd4f5fb0`. The statement is refuted, not proved, so the first acceptance clause ("proved on a page of `writing/` and read MET by one Kimi review") is **NOT MET** and the second ("refuted with a counterexample") is **MET**; the item-by-item record is `computations/reports/802-acceptance-item-by-item.txt`.

The invariant is the automorphism group of an object, which an equivalence of stacks preserves. That is now a lemma on the page, `lem:automorphism-group-under-an-equivalence` (`writing/coble/lattices-and-moduli/moduli-construction.md:1125`): for an equivalence of categories $F\colon\mca\to\mcb$ with quasi-inverse $G$ — the Stacks Project's **Definition 4.2.17**, tag 001J: "An *equivalence of categories* $F : \mathcal{A} \to \mathcal{B}$ is a functor such that there exists a functor $G : \mathcal{B} \to \mathcal{A}$ such that the compositions $F \circ G$ and $G \circ F$ are isomorphic to the identity functors" — the map is an isomorphism $\Aut_{\mca}(x)\to\Aut_{\mcb}(Fx)$. The proof uses only the unit and the counit; it needs no adjoint-equivalence upgrade, and it is on the page.

### (a) The marked Coble stack is not $D(T_{\mathrm{Co}}) - Z$

Quoting `rmk:coble-labelled-versus-unlabelled(1)` (`moduli-construction.md:1097`), whose objects are exactly those of the marked stack $\mathcal M^{\mathrm{lab}}_{\mathrm{Co}}$ as the page defines it (`:664`):

> "The covering involution $\iota$ is a nontrivial automorphism of every labelled object — it preserves each $e_i$, preserves the period, and acts as $-\id$ on $T_\Co$ (@prop:coble-transcendental) — so the isotropy of $\mcM^{\mathrm{lab}}_\Co$ contains $\theset{\id,\iota}\cong\ZZ/2$ at every object. It is finite, and $[\widetilde\Orth^+(T_\Co)\backslash\bD(T_\Co)^+]$ is a Deligne--Mumford stack locally of finite type, but its isotropy is not trivial."

$D(T_{\mathrm{Co}})^+ - Z$ is a complex manifold (`prop:the-coble-locus-in-the-period-domain(1)`, `(4)`: "$Z$ is a closed analytic subset of $\bD$, locally finite"; "the locus of periods realised by *some* Coble cover is exactly $\bD\sm Z$; it is open, and it is connected"), so read as a stack through its functor of points, every object over a point is a point and its only automorphism is the identity — `prop:no-identification-with-the-period-domain(1)` with $G=1$ (`moduli-construction.md:1150`). $\ZZ/2\neq\{\id\}$ at a single object refutes the equivalence.

### (b) The Coble stack is not $[(D(T_{\mathrm{Co}})^+ - Z)/G]$ for any $G\subseteq\Orth(T_{\mathrm{Co}})$, hence not for $G=\widetilde\Orth^+(T_{\mathrm{Co}})$

Every point of the quotient has a **finite** stabiliser. Quoting `lem:period-stabiliser-finite`:

> "Let $T$ be a lattice of signature $(2,n)$ and $P\subset T\tensor\RR$ a positive definite $2$-plane (a point of $\bD(T)$). Then $\Stab_{\Orth(T)}(P)=\theset{g\in\Orth(T)\mid g(P)=P}$ is finite."

$T_\Co$ is of signature $(2,9)$ (`prop:coble-period-domain(2)`), and the automorphism group of the object $(\tilde x)$ of $[U/G]$ over a point is the stabiliser $G_{\tilde x}\subseteq\Stab_{\Orth(T_\Co)}(\tilde x)$, computed from the action-groupoid presentation `lem:action-groupoid-fibre-product` (`prop:no-identification-with-the-period-domain(1)`, `moduli-construction.md:1150`-`1152`).

The Coble stack, on the other hand, has **infinite** isotropy at every object. Quoting `rmk:coble-labelled-versus-unlabelled(2)`:

> "The automorphism group of a Coble surface is $W_{10}(2)$, infinite and discrete (@rmk:coble-automorphisms-infinite(1)--(2)), so $\mcM_\Co$ has infinite isotropy, is not locally of finite type, and is not separated."

and `lem:coble-automorphism-group-is-infinite(3)`, the page's own proof:

> "Hence the image of $\operatorname{Aut}(S)$ in $\Orth(\Pic(S))$ is infinite, and $\operatorname{Aut}(S)$ is infinite."

That lemma's source, as the page states it, is Cantat–Dolgachev: "For the rest, [@CD12, Thm. 3.5 and its proof] display the involution $\tau$ of a Coble surface as $\tau^*=\id_U\oplus\qty(-\id_{E_8})$ on $K_S^{\perp}$". I read Cantat–Dolgachev, *Rational surfaces with a large group of automorphisms* (arXiv:1106.0930), **Theorem 3.5**, verbatim:

> "Theorem 3.5. Let X be an unnodal Coble surface. Then Aut(X)∗ contains the subgroup of WX which is isomorphic to W10(2) := {w ∈ W10 : w(v) − v ∈ 2E10 for all v ∈ Pic(X)} under the natural identification of WX with W10."

It gives the containment only for unnodal surfaces, and only in the image $\operatorname{Aut}(X)^*$; the page's lemma does not need either restriction, because it exhibits two of the $45$ Bertini involutions whose product has infinite order in $\Orth(\Pic(S))$ at every ten-nodal member — so the image is infinite and $\operatorname{Aut}(S)$ with it. The surfaces exist as objects of the stack: `prop:coble-family-over-c-star-with-infinite-monodromy-on-m(1)`: "every fibre of $f$ is $S$ ... and $f$ with the relative double cover ... is an object of $\mcM_\Co$ (@def:coble-moduli-functor) over $\CC^\times$".

Infinite $\neq$ finite at one object, so no equivalence. Since the argument excludes **every** subgroup of $\Orth(T_\Co)$, it excludes $\widetilde\Orth^+(T_\Co)$ (`def:gamma-co-groups(3)`) and with it the "gluing argument of step (c)": there is no equivalence whose group could be identified.

### What the page does prove about the marked stack's isotropy

One sentence: that it is finite, nontrivial and contains $\theset{\id,\iota}\cong\ZZ/2$ at **every** object, and on the generic substack, under hypothesis (v), it is **exactly** $\theset{\id,\iota}=\Stab_{\widetilde\Orth^+(T_\Co)}(\pi)$ — which makes the period map an equivalence onto $\qty[\widetilde\Orth^+(T_\Co)\backslash U^{\mathrm{gen}}]$ "with the isotropy $\theset{\id,\iota}$ on both sides" (`thm:gamma-co-labelled-equality(1)`, `(v)`).

### Recorded beside the refutation (`rmk:what-the-marked-isotropy-is`, `moduli-construction.md:1170`)

- The coarse space is not the stack. `rmk:d2-routes-for-the-equality` says "the identification of $H$ with $(\bD(T_\Co)-Z)/G$ for an explicit $G$ is *equivalent* to the equality", $H$ being the labelled base $B$; that is a statement about two spaces, and it neither implies nor is implied by (a) or (b). A rigidified or coarse quotient is **not** offered in place of either equivalence.
- Two markings occur in the volume, and they are different data. On the eleven classes of `rmk:coble-labelled-versus-unlabelled` (the objects of $\mathcal M^{\mathrm{lab}}_{\mathrm{Co}}$) the argument (a) runs, since $\iota$ preserves each $e_i$. On the isometry marking $\varphi\colon H^2(X,\bZ)\isoto\lkt$ of `def:marked-coble-cover`, $\iota$ is not an automorphism: "$\varphi\circ\iota^*\circ\varphi^{-1} = \rho$" (`def:marked-coble-cover(1)`), and $\rho\neq\id$. That reading is not decided here, and (b) does not depend on it.

### K1, and the pointer that #802 was

K1 is research#799, and it is **closed as refuted**: "Closed: refuted. prop:coble-family-over-c-star-with-infinite-monodromy-on-m ... is a family of Coble covers over C^*, an object of the stack of def:coble-moduli-functor, whose invariant-lattice monodromy has infinite order, so no global isomorphism with the constant M respecting the eleven classes exists ... For #798: no route may fix a global marking of M on the stack". So #802's hypotheses are not available: K1 is false, and K4's two equivalences are false as stated.

`writing/coble/lattices-and-moduli/local-systems-of-lattices-and-monodromy.md:186` named research#802 as the place where the quotient presentation of the Coble family would come from; it is repaired in the same commit to state that no such presentation exists for any subgroup of $\Orth(T_\Co)$.

### Verification

The change is prose: no test in `tests/engineering` pins either edited passage and none was added; `scripts/docs_check.py --source` reports 29 citation-key findings, the same count as at the parent commit, none of them on either page touched. The rendered book gate (CI renders `writing/`) and `tests/engineering` (needs `dzack_research`) were **not run** here, so nothing is claimed about them.
