Intended comment for research#802 (the issue connector here is read-only; the orchestrator posts it).

## Both clauses refuted, each on its own; the exact $\varphi$-marked statement decided

Commit `d33b0e5ab8ad253fc30fca4f1862b29a94218b90`. Acceptance: item 1 (proved on a page and read MET by a Kimi review) is **NOT MET**; item 2 (refuted with a counterexample) is **MET**, by one counterexample per clause, neither inferred from the other. The item-by-item record is `computations/reports/802-acceptance-item-by-item.txt`.

### The $\varphi$-marked clause: decided, and false

The statement decided is `rmk:phi-marked-what-is-decided(1)`, `writing/coble/lattices-and-moduli/marked-coble-covers-and-the-period-map.md:117`:

> the period map $\mathcal P_\Co\colon\mcM^{\varphi}_\Co\to\bD(T_\Co)^+\sm Z$ from the marked Coble covers of `def:marked-coble-cover(1)`, with the isomorphisms of `(4)`, is an equivalence — that is, every period off $Z$ occurs and **a marked Coble cover is determined up to isomorphism by its period**.

It is false. `prop:phi-marked-is-not-the-period-domain` (same page, `:96`) computes the period map:

1. **Essentially surjective.** For $\pi\in U$ there are $X$, an isometry $\varphi\colon H^2(X,\bZ)\isoto\lkt$ with $\varphi_\bC(H^{2,0}(X))=\pi$, and an involution $\iota$ with $\iota^*=\varphi^{-1}\rho\varphi$ whose fixed locus is one smooth rational curve and whose quotient is a Coble surface of `def:coble-moduli-functor` — `thm:coble-period-surjectivity`, whose $\sigma$ is $\rho=\id_{S_\Co}\perp(-\id_{T_\Co})$, clauses (1)--(3) being the rest of `def:marked-coble-cover(1)`.
2. **Faithful.** Every morphism set of $\mcM^{\varphi}_\Co$ is empty or a singleton, and $U$ is a set.
3. **Not full.** `prop:marked-coble-period-not-injective` (`:25`) gives two marked covers with equal periods and no isomorphism in the sense of `def:marked-coble-cover(4)`, while the target has only the identity at that period; fullness there would produce the isomorphism.

Objects and isotropy, `lem:phi-marked-objects-and-automorphisms` (`:73`):

- $\iota^*=\varphi^{-1}\circ\rho\circ\varphi$, and it is the only involution of $X$ with that action, since $(\iota_2^{-1}\iota_1)^*=\id$ forces $\iota_2^{-1}\iota_1=\id$; the citation is [@PS24, Lemma 19.2.4] in the form the page uses elsewhere: "there is an injection $\operatorname{Aut}(X)\hookrightarrow\operatorname O(H^2(X,\mathbb Z)), g\mapsto g^*$".
- **The covering involution is not an automorphism of the marked object**: $\varphi\circ\iota^*=\rho\circ\varphi\neq\varphi$ because $\rho=-\id$ on $T_\Co\neq0$. So $\Aut(X,\iota,\varphi)=\{\id\}$, and a $\varphi$-marked object has isotropy $\{\id\}$ where a labelled object's contains $\{\id,\iota\}$ (`rmk:coble-labelled-versus-unlabelled(1)`); the marked groupoid is discrete.
- **How the marking, the involution and the period interact.** For a fixed $(X,\iota)$ the markings are a torsor under the centraliser $\Gamma_\rho=\{\gamma\in\Orth(\lkt):\gamma\rho\gamma^{-1}=\rho\}$, which is the set of pairs $\gamma_S\perp\gamma_T$ with $\gamma_T\circ\gamma_\Co=\gamma_\Co\circ\gamma_S$ for the gluing isometry $\gamma_\Co$ of the page. Since $\iota$ is nonsymplectic, $\pi=\varphi_\bC(H^{2,0}(X))$ lies in $T_\Co\tensor\bC$, and the period of $\gamma\circ\varphi$ is $\gamma_{T,\bC}(\pi)$: the period sees the marking only through the $T_\Co$-component. Two markings of one surface therefore have the same period exactly when their quotient has $T_\Co$-component in $\Stab_{\Orth(T_\Co)}(\pi)$, a finite group (`lem:period-stabiliser-finite`, at signature $(2,9)$).
- **The counterexample in these terms**: the two markings of `prop:marked-coble-period-not-injective` differ by $s_{\varphi([E_0])}\perp\id_{T_\Co}\in\Gamma_\rho$, whose $T_\Co$-component is the identity; they are in one $\Gamma_\rho$-orbit, have the same period, and no isomorphism exists.

Not decided here, and named as such: a version in families, which would need marked Coble covers over a base that `def:marked-coble-cover` does not define; and whether equal period **and equal chamber** forces an isomorphism, the counterexample's two objects carrying different chambers (`rmk:marked-coble-period-scope(2)`). A bare equivalence of groupoids is not the statement at stake: a groupoid with trivial automorphism groups is equivalent to its set of isomorphism classes, so that reading asserts only that two sets have the same cardinality. The eleven-class-labelled stack is a different object and decides nothing here.

### The unmarked clause: refuted, as recorded before, and used by nothing above

`prop:no-identification-with-the-period-domain` (`moduli-construction.md:1201`), clause (3) at `:1211`: for no subgroup $G\subseteq\Orth(T_\Co)$ is $\mcM_\Co$ equivalent to $[U/G]$. One object suffices — an unnodal classical Coble surface, whose automorphism group is infinite (`lem:coble-automorphism-group-is-infinite(3)`; Cantat–Dolgachev, **Theorem 3.5**: "Let X be an unnodal Coble surface. Then Aut(X)∗ contains the subgroup of WX which is isomorphic to W10(2) …"), against finite stabilisers in the quotient (clause (1) at `:1205`). Objects of $\mcM_\Co$ with finite automorphism groups exist and are not the witness (`rmk:coble-automorphisms-infinite(2)`, `:1143`). The group clause of #802 is not reached: there is no equivalence at which $G=\widetilde\Orth^+(T_\Co)$ could be read off.

### K1

K1 is research#799, **closed as refuted**: "Closed: refuted. prop:coble-family-over-c-star-with-infinite-monodromy-on-m … is a family of Coble covers over C^*, an object of the stack of def:coble-moduli-functor, whose invariant-lattice monodromy has infinite order … For #798: no route may fix a global marking of M on the stack".

### Verification

Prose only; no test in `tests/engineering` pins the new blocks and none was added. `scripts/docs_check.py --source` runs all eight source checks and reports 29 citation-key findings, none on the page touched. The rendered book gate (CI renders `writing/`) and `tests/engineering` (needs `dzack_research`) were **not run**, so nothing is claimed about them.
