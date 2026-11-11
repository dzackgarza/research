### Finiteness by Kulikov Models and a Coarsening Argument {#section-7-6}



We now prove a crucial structural property of the classifying morphism

\begin{align*}
\phi : \normalize{B} \to \cpt{\fentwo}
.\end{align*}

constructed in previous sections: namely, that $\phi$ is finite.
This assertion is the final step needed for modular identification of the compactified moduli of degree-2 polarized stable Enriques pairs via the period map and semitoroidal construction.

#### Semifan Comparison and Finiteness: Addressing the Critical Gap

::: {.lemma title="{Semifan Comparison}" #lem:semifan-comparison}
Let $\semitorcpt{\fentwo}$ be the semitoroidal compactification defined using the five semifans $\semifan{F} = \{\semifan{F}_k\}_{k=1}^5$ as in @AEGS25. There exist semifans $\semifan{G} = \{\semifan{G}_k\}_{k=1}^5$ associated with the normalization of the KSBA compactification $\ksbacpt{\fentwo}$ such that:

1. $\normksbacpt{\fentwo} = \semitorcpt{\fentwo}$ if and only if $\semifan{G}_k = \semifan{F}_k$ for all $k$.

2. Each $\semifan{G}_k$ is a coarsening of $\semifan{F}_k$.

3. The morphism $\phi$ is finite if and only if all $\semifan{G}_k = \semifan{F}_k$.
:::

::: {.proof}
The argument is the published one, the proof of [@AEGS25, Thm. 5.9, printed pp. 611--612]; each step below names the numbered statement that carries it.

*The source of $\phi$ and its folded structure.*
The morphism $\phi$ is the classifying morphism of @thm:universal-family-moduli, defined on the normalization $\normalize{B}$ of the closure $B$ of the image of $\fentwo$ in $\ksbacpt{\fttz}$.
That $\fentwo$ is the normalization of a closed subvariety of $\fttz$ is [@AEGS25, Lem. 2.8, printed p. 587], and that $\normalize{B}$ is then a compactification of $\fentwo$ carrying a universal family of pairs is [@AEGS25, proof of Thm. 5.9, printed p. 612].
The normalization of the KSBA compactification of the K3 pairs is semitoroidal because the ramification divisor is recognizable, and for $\fttz$ its semifan is the ramification semifan $\semifan{F}_{\ram}$ [@AEGS25, proof of Thm. 5.9, printed pp. 611--612], which invokes the main theorem of [@AE23] and the recognizability statement of [@AEH24], and identifies the semifan via [@AE22].
The same proof states that $\normalize{B}$ is the semitoroidal compactification of the Noether--Lefschetz locus $B$ induced by $\semifan{F}_{\ram}$, and that the induced compactification of $\fentwo$ has as its normalization the semitoroidal compactification for the folded semifans $\semifan{F}_k$; these are obtained by intersecting $\semifan{F}_{\ram}(\tdp)$ with the Enriques lattice subspace $\ten$ [@AEGS25, Def. 5.3, printed p. 610] and are the generalized Coxeter semifans of the folded Coxeter diagrams [@AEGS25, Lem. 5.5, printed p. 611].
This is the folded-semifan construction of the preceding section, under which $\normalize{B}$ carries the semitoroidal structure of $\semitorcpt{\fentwo}$.
Since $\normalize{B}$ is normal (@prop:normalization-pullback-family) and $\phi$ is an isomorphism over the interior $\fentwo$ (@prop:properties-classifying), $\phi$ is dominant and lifts uniquely through the normalization $\nu\colon\normksbacpt{\fentwo}\to\cpt{\fentwo}$ as $\phi=\nu\circ\psi$, as in the diagram of the main theorem.

*Domination of the Baily--Borel compactification.*
The $j$-invariant of a Type $\mathrm{II}$ boundary point of $\bbcpt{\fentwo}$ is recovered from the stable pair $(Z, \eps R_Z)$: the surface $Z$ has either an elliptic double curve, or a $\PP^1$ double curve with four distinguished points that are $A_1$-singularities on a component containing it, and the $j$-invariant is that of the double cover of $\PP^1$ branched at these four points [@AEGS25, proof of Thm. 5.9, printed p. 612].
The argument is the one of [@AET23, Thm. 3.17 with Lem. 3.18, arXiv:1903.09742v3, printed pp. 20--21]: the central fiber of a one-parameter family of stable pairs determines whether the Baily--Borel limit is of Type $\mathrm{II}$ or of Type $\mathrm{III}$ and, in the Type $\mathrm{II}$ case, the $j$-invariant, whence the rational map from the normalization to the Baily--Borel compactification is regular.
Therefore $\normksbacpt{\fentwo}$ dominates $\bbcpt{\fentwo}$.

*Domination by a toroidal compactification, and the coarsening.*
The morphism $\phi$ is proper (@prop:properties-classifying) and dominant, hence surjective; so $\normksbacpt{\fentwo}$ is dominated by $\normalize{B}=\semitorcpt{\fentwo}$, which is dominated by the toroidal compactification $\coxcpt{\fentwo}$ for the folded Coxeter fans: the normalization of the closure of the image of $\fentwo$ in the Coxeter toroidal compactification is that toroidal compactification, and each generalized Coxeter semifan $\semifan{F}_k$ is the coarsening of the Coxeter fan obtained by deleting the faces spanned by the irrelevant roots [@AEGS25, §5.2, printed p. 610]; this is the chain of morphisms of @thm:main-theorem.
Thus $\normksbacpt{\fentwo}$ is a normal compactification of $\fentwo$ which dominates $\bbcpt{\fentwo}$ and is dominated by a toroidal compactification.
By [@AE23, Thm. 7.18], in the form stated in [@AEGS25, §5.2, printed p. 610], the semitoroidal compactifications are exactly the normal compactifications with these two properties, and they are defined by collections of compatible semifans, one for each Baily--Borel $0$-cusp, with the data for the $1$-cusps uniquely determined.
Hence $\normksbacpt{\fentwo}$ is the semitoroidal compactification of $\fentwo$ for semifans $\semifan{G}_k$, and the $\semifan{G}_k$ coarsen the $\semifan{F}_k$ [@AEGS25, proof of Thm. 5.9, printed p. 612].
This proves (2).

*The equivalences (1) and (3).*
Suppose $\semifan{G}_k=\semifan{F}_k$ for all $k$.
Then $\normksbacpt{\fentwo}$ and $\semitorcpt{\fentwo}=\normalize{B}$ are both the semitoroidal compactification of $\fentwo$ for the semifans $\semifan{F}_k$, and the lift $\psi$ is a morphism between them which is an isomorphism over $\fentwo$.
A semitoroidal compactification is determined by its collection of compatible semifans [@AEGS25, §5.2, printed p. 610], so $\psi$ is an isomorphism, and $\phi=\nu\circ\psi$ is finite: $\cpt{\fentwo}$ is a closed subvariety of the projective KSBA coarse moduli space [@AEGS25, Def. 2.10, printed p. 588], so its normalization $\nu$ is finite, as in the proof of @prop:normalization-pullback-family.
This proves the if directions of (1) and (3).
Conversely, suppose $\phi$ is finite.
Since $\phi=\nu\circ\psi$ with $\nu$ finite, $\psi$ is finite: it is proper, both of its spaces being proper -- $\normalize{B}$ by @prop:normalization-pullback-family, and $\normksbacpt{\fentwo}$ as the normalization of the KSBA compactification, which is proper by [@Kol23] -- and its fibers are finite, since for $y\in\normksbacpt{\fentwo}$ one has $\psi^{-1}(y)\subseteq\phi^{-1}(\nu(y))$, a closed subset of a fiber of the finite morphism $\phi$.
The lift $\psi$ is birational, an isomorphism over the interior $\fentwo$ (@prop:properties-classifying), and its target is normal; a finite birational morphism onto a normal variety is an isomorphism, by Zariski's main theorem in the form of [@AET23, Lem. 3.18, arXiv:1903.09742v3, printed p. 21], whose proof concludes: "The morphism $Z\to X$ is birational, and the condition is that it is finite. By Zariski's Main Theorem $Z\to X$ is an isomorphism."
Hence $\normalize{B}\cong\normksbacpt{\fentwo}$ over $\fentwo$; the two are then the semitoroidal compactification of $\fentwo$ for the same collection of compatible semifans -- $\semitorcpt{\fentwo}$ for the $\semifan{F}_k$ by construction, $\normksbacpt{\fentwo}$ for the $\semifan{G}_k$ by (2) -- and a semitoroidal compactification is determined by that collection [@AEGS25, §5.2, printed p. 610].
Therefore $\semifan{G}_k=\semifan{F}_k$ for all $k$, which proves the only-if directions of (3) and of (1).
:::

#### Maximality, Moduli, and Injectivity: Scheme-Theoretic Proof

::: {.definition title="{Maximality of Degenerations}" #def:maximality-degenerations}
A degeneration $(X_0, \epsilon R_0)$ of K3 pairs is **maximal** if $X_0$ realizes the largest possible number of double curves among all degenerations with the same monodromy data.
The analogous definition applies for Enriques degenerations $(Z_0, \epsilon R_{Z,0})$.
This is the "maximal number of double curves" of [@AEGS25, proof of Thm. 5.9, printed p. 612], the notion in which the comparison below is made.
:::

::: {.proposition title="{The Double Curve Constraint}" #prop:double-curve-constraint}
Let $(X_0, \epsilon R_0)$ be a degeneration of K3 pairs with a fixed-point-free Enriques involution $\ien$, with quotient $(Z_0, \epsilon R_{Z,0})$.
Then:

- The number of irreducible components of $Z_0$ is the number of $\ien$-orbits of components of $X_0$;

- The number of double curves in $Z_0$ is the number of $\ien$-orbits of double curves in $X_0$;

- $(Z_0, \epsilon R_{Z,0})$ is maximal if and only if $(X_0, \epsilon R_0)$ is maximal.
:::

::: {.proof}
Let $(\mcx, \epsilon R) \to (C, 0)$ be a divisor model for a degeneration of Enriques K3 surfaces, so that the folding symmetry induces the involution $\iota_{\En,\IA}$ of the polarized $\IAS^2$ [@AEGS25, Prop. 4.5, printed p. 601], and the general such model admits a second involution $\ien$ preserving $R$ [@AEGS25, Thm. 4.6, printed p. 603].
The half-divisor model is the quotient $(\mcz, \epsilon R_Z) := (\mcx, R)/\ien$ [@AEGS25, Def. 4.7, printed p. 603], and [@AEGS25, Prop. 4.8, printed p. 603] describes it in every type: in Type $\mathrm{III}$ at cusp $1$ the dual complex $\Gamma(\mcz_0)=\RP^2$ and each component of $\mcz_0$ is, up to normalization, one of the two connected components of its inverse image in $\mcx_0$; at cusps $2$--$5$ one has $\Gamma(\mcz_0)=\DD^2$, and a component is either covered by two components of $\mcx_0$, to each of which it is isomorphic up to normalization, or is the quotient of a single component on which $\ienzero$ has exactly four fixed points, two pairs on double curves of that component; in Type $\mathrm{II}$ the dual complex $\Gamma(\mcz_0)$ is a segment, and $\ienzero$ either flips $\Gamma(\mcx_0)$, fixing no points and acting on a preserved double curve by a nontrivial $2$-torsion translation, or preserves every component, acting on each double curve by an elliptic involution with exactly four fixed points.
In all cases the components of $\mcz_0$ are the $\ien$-orbits of the components of $\mcx_0$ and the double curves of $\mcz_0$ are the $\ien$-orbits of the double curves of $\mcx_0$, the quotient dual complex being $\Gamma(\mcz_0)=\Gamma(\mcx_0)/\iota_{\En,\IA}$ with its inherited integral-affine structure [@AEGS25, Remark 4.10, printed p. 605].
This proves the first two bullets.
For the third, the KSBA-stable limit of a degeneration of $(Z, \epsilon R_Z)$ is computed from the half-divisor model as $\Proj$ of its plurigenera [@AEGS25, Cor. 4.9, printed p. 605], and the explicit description of the Kulikov and stable models in [@AEGS25, Prop. 4.8, printed p. 603, and Cor. 4.9, printed p. 605] gives the criterion: a degeneration of $(Z, \epsilon R_Z)$ has the maximal number of double curves if and only if $(X, \epsilon R)$ does [@AEGS25, proof of Thm. 5.9, printed p. 612].
:::

#### The Core Finiteness-Injectivity Argument

::: {.theorem title="{No Coarsening Occurs}" #thm:no-coarsening}
For each $k \in \{1,2,3,4,5\}$, the boundary semifans satisfy $\semifan{G}_k = \semifan{F}_k$.
:::

::: {.proof}
Suppose, for contradiction, that for some $k$ the semifan $\semifan{G}_k$ is a proper coarsening of $\semifan{F}_k$.
Then some cone of $\semifan{F}_k$ is not a cone of $\semifan{G}_k$, and there is a codimension-one cone $\sigma$ of $\semifan{F}_k$, a common face of two maximal cones, which is deleted in the coarsening.
By [@AEGS25, proof of Thm. 5.9, printed p. 612], the deleted cone would parameterize a $1$-dimensional family of pairs $(X, \epsilon R)$ that are not maximal, whose Enriques quotients $(Z, \epsilon R_Z)$ have the maximal number of double curves.
This is impossible: by @prop:double-curve-constraint, which is the maximality criterion of [@AEGS25, proof of Thm. 5.9, printed p. 612] resting on the explicit models of [@AEGS25, Prop. 4.8, printed p. 603, and Cor. 4.9, printed p. 605], a quotient is maximal exactly when its cover is.
Hence no proper coarsening occurs, and $\semifan{G}_k = \semifan{F}_k$ for all $k$.
This is the first statement of [@AEGS25, Thm. 5.9, printed pp. 611--612], and of [@AEGS25, Thm. 1.1, printed p. 582].
:::

#### Properness, Quasi-finiteness, and Conclusion

::: {.corollary title="{Finiteness of the Classifying Map}" #cor:finiteness-classifying-map}
By @thm:no-coarsening, the boundary stratifications, as encoded by semifans, agree identically.
Therefore, by @lem:semifan-comparison(3), the morphism $\phi: \normalize{B} \to \cpt{\fentwo}$ is finite.
:::

::: {.proof}
By @thm:no-coarsening, $\semifan{G}_k = \semifan{F}_k$ for all $k$, so @lem:semifan-comparison(3) gives that $\phi$ is finite.
Concretely, the lift $\psi\colon\normalize{B}\to\normksbacpt{\fentwo}$ is an isomorphism, both sides being the semitoroidal compactification for the semifans $\semifan{F}_k$, and $\phi = \nu\circ\psi$ is the composite of an isomorphism with the finite normalization $\nu$.
No separate argument on the interior is needed: $\phi$ is already an isomorphism over $\fentwo$ (@prop:properties-classifying).
This finiteness is the one the published proof reduces the comparison to: it remains, for the semifan agreement, to show that $\normalize{B}\to\ksbacpt{\fentwo}$ is a finite map, equivalently, that no moduli are lost in the quotient by $\ien$ [@AEGS25, proof of Thm. 5.9, printed p. 612].
:::
