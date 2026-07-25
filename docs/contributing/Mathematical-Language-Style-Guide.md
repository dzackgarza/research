# Mathematical authoring conventions

Contributions state mathematical types, chosen structures, model choices, universal constructions, diagrams, notation, and the relation between a primitive construction and its familiar specializations.

## Types and structure {#sec-types-and-structure}

[]{#convention-mathematical-type} **State the mathematical type.** A named entity has a domain, codomain, and kind.
Distinguish objects and morphisms in a specified category, categories and functors, natural transformations, object properties, chosen structures, invariants, sections, and obstructions.
An obstruction is a specified class or map together with a theorem stating whether its vanishing is necessary, sufficient, or equivalent to the stated lifting or extension problem under the given hypotheses.
A set-valued isomorphism invariant has the form $\pi_0(\mathcal C^{\simeq})\to S$; a functorial invariant with a richer codomain states that codomain and its functoriality.

[]{#convention-property-and-structure} **Use the forgetful functor to distinguish properties and structure.** For a specified forgetful functor $U\colon\mathcal S\to\mathcal C$, full faithfulness gives at most property, faithfulness gives at most structure, and an arbitrary functor gives at most stuff.
Repleteness is a separate condition when an essential image is replaced by a full subcategory.
Property language is used only when each homotopy fiber is empty or a contractible groupoid; otherwise name the chosen structured object over $X$.

[]{#convention-chosen-structure} **Name every chosen structure.** A structure on $X$ is a chosen object of the fiber of a specified forgetful functor over $X$.
When several choices exist, name the one used by a construction.
For example, tensor product and direct sum give different monoidal structures on modules.
For a commutative ring $R$, these are $(R\text{-}\mathbf{Mod},\otimes_R,R)$ and $(R\text{-}\mathbf{Mod},\oplus,0)$.
Over a noncommutative ring, state the applicable bimodule or left- or right-module setting.

[]{#convention-hypotheses-and-witnesses} **State hypotheses and name witnesses.** A theorem states every object property, characteristic restriction, limit assumption, flatness assumption, and equality of named morphisms used in its conclusion.
If a construction uses a basis, embedding, section, presentation, or other witness, name that witness in the construction.

[]{#convention-typed-notation} **Use notation with its typed meaning.** Literal equality, isomorphism, and equivalence are written with distinct symbols.
The symbol $\hookrightarrow$ denotes the stated inclusion, embedding, or monomorphism; fullness, faithfulness, and repleteness are asserted separately.
Strict pullbacks and pseudo-pullbacks are not identified by notation.

[]{#convention-mathematics-before-realization} **State the mathematics before its realization.** A mathematical chapter defines its categories, functors, morphisms, and universal properties without depending on implementation names.
A realization or implementation section may then identify the Lean, Sage, or Mathlib object that represents the already-defined mathematics.

## Higher-categorical primitives and specializations

When a notion is intended to be intrinsic to higher categories, first fix the universe, the chosen model of higher categories, and the standard name for the category that model defines.
Define the primitive construction there, with the type of every object, morphism, and comparison cell stated.

If the familiar formulation lives in $\mathbf{Spaces}$, name the model-dependent functor or construction that passes from the chosen category of higher categories to spaces.
Then state and cite the theorem identifying the image of the primitive construction with the published space-level definition.
The space-level formulation is a specialization or comparison theorem; it does not replace the higher-categorical definition.

A definition and a characterization have different roles.
Representable, Yoneda, mapping-space, or detection criteria follow the definition and are stated as theorems with their hypotheses.
Likewise, recovery of an ordinary or strict special case is a lemma or remark after the general construction, not the definition of that construction.

## Universal constructions and diagrams

- A classifying object, classifying category, or universal family is named only together with the represented functor or explicit universal property.

- A pullback or pseudo-pullback is displayed by its square, including the projection maps and the universal property.
  Fiber-product notation may then name the apex.

- An adjunction $F\dashv G$ is displayed with its source and target categories, both functors, and the adjunction.
  The shared `\adj` macro supplies the book's diagrammatic convention.

- A comparison between functors is a natural transformation or another specified 2-cell.
  A morphism between objects remains a morphism in the stated category.

- Every arrow in a diagram names a functor, natural transformation, or map with the displayed source and target.
  A construction defined only on cores is drawn from the cores, and an invariant on isomorphism classes is drawn as a map from $\pi_0$.
  Membership of an object in a category is not drawn as a functor between categories.

- A theorem that a functor lands in a replete full subcategory is a proved factorization through its inclusion.
  Other landing statements name their actual codomain.

## Formation conventions {#sec-formation-conventions}

- **Working 2-category.** State the universe.
  In $\mathbf{Cat}_{\mathcal U}$, objects are $\mathcal U$-small categories, 1-morphisms are functors, and 2-morphisms are natural transformations.

- **Pullbacks.** Use pseudo-pullbacks unless the relevant leg is an isofibration.
  A strict pullback along an isofibration presents the pseudo-pullback up to equivalence.
  A replete full inclusion is an isofibration.

- **Repleteness.** A full subcategory defined by an isomorphism-invariant object property is replete.
  A predicate that is not isomorphism-invariant may define a full subcategory that is not replete.

- **Categories of elements.** Fix one variance convention and state whether the resulting projection is a fibration or an opfibration.
  For a presheaf $F$, define its category of elements and projection once; a natural transformation of presheaves induces the corresponding functor between categories of elements.

- **Nerves.** The ordinary nerve of a category is the simplicial set of composable chains.
  For a simplicial category, specify the homotopy coherent nerve ([Kerodon `00KS`](https://kerodon.net/tag/00KS)); on an ordinary category with discrete mapping spaces it agrees with the ordinary nerve.

- **Truncation.** Set-level and groupoid-level constructions are not interchangeable.
  Applying $\pi_0$ to a homotopy pullback requires hypotheses under which it preserves the construction; otherwise retain the groupoid- or space-level object.

- **Generated functors.** A composite, induced functor, inclusion, projection, or whiskered natural transformation cites the constructions from which it is obtained.

- **Abelian characterizations.** In an abelian category, monicity, epicity, or isomorphism may be expressed by the applicable kernel and cokernel vanishing criteria.
  Outside an additive or abelian setting, use the relevant categorical definition.

- **Form presheaves.** A family of forms is a named presheaf with its codomain stated.
  If comparison identities use $R$-module operations, state the presheaf as $F\colon\mathcal C^{\mathrm{op}}\to R\text{-}\mathbf{Mod}$ and type every natural transformation in the identity.

## Standard names and local notation {#sec-standard-terms}

Use the established names in their standard meanings: category of elements, Grothendieck construction, core, arrow category, full subcategory, replete, natural isomorphism, automorphism group, torsor, monoidal category, abelian category, preadditive category, kernel, cokernel, discriminant form, genus, isometry, classifying object, classifying space, classifying category, and total category.

Project notation is introduced at the defining occurrence, after the underlying standard construction has been stated.
Every symbol records the same type and meaning throughout the book.
