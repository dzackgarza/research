<!--
Origin: gitclones/integral_lattice/cat/docs/old_docs/original_specifications.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of
this corpus.
-->

Goal: build a truncated toy model of infinity-categories, modeled as a variation of CW complexes in which we allow ZZ-indexed cells. We establish some axioms:

    - There is some universe Cat in which all categories live.
        - There exists an infinity category Cat_w of weak infinity categories.
        - There is a grading fibration p: Cat_w → Bℤ, with fibers Cat_n := p^{-1}(n).
        - By definition, Cat_n is enriched over Cat_{n-1}, so for every C in Cat_n and every pair of objects x, y in C, Hom_C(x, y) is an (n-1)-category.
        - Every set X is identified with an object X in Cat_0 by regarding X as a discrete category with objects x ∈ X and only identity morphisms.
        - For each C ∈ Cat_w, there is a grading fibration q: C → Bℤ, with Cᵏ := q⁻¹(k) the set of k-cells in C.
          Note that this differs from C⁽ᵏ⁾ := q⁻¹((-∞, k]) = ⋃_{i ≤ k} Cⁱ, the k-skeleton.

        - Suspension and loop functors:
        - Fix the distinguished terminal object * ∈ Cat_w, and let ∅ ∈ Cat_w be the initial object.
            - Why these exist: for any C, there is a chain ∅ ↪ C ↣ *.
            - In a simplicial model, * := Δ^0 has exactly one n-cell for every n, and ∅ has an empty set of n-cells for every n.
            - Say C is contractible iff C -> * is an equivalence.
            - A point x in C is a morphism * -> C.
        - Pushout constructions:
            - X ⨿_C Y := lim(X <- C -> Y)
            - X ⨿ Y := X ⨿_∅ Y = lim(X <- ∅ -> Y)
            - Cof(f) := Y ⨿_X * = lim(Y <-_f X -> *)
        - Pullback constructions:
            - X ⊓_C Y := lim(X -> C <- Y)
            - X ⊓ Y := X ⊓_* Y = lim(X -> * <- Y)
            - Fib(f) := X ⊓_Y * = lim(X -> Y <- )
        - Define fibers and cofibers: for a morphism f: X -> Y in Cat_w,
        - Define endofunctors on Cat_w:
            Σ C := * ⨿_C * := lim(* <- C -> *)
            Ω_b X := * ⊓_X * := lim(* ->_b C <-_b *) where b: * -> C is a point.
        - Define endofunctors on Cat_w:
            ΩX := * ⊓_X * := lim(* -> X <- *)
            ΣX := * ⨿_X * := lim(X <- * -> X)
        - These shift grading:
            Ω(Cat_n) ⊆ Cat_{n-1}
            Σ(Cat_n) ⊆ Cat_{n+1}
        - These recover:
            - Fib(C -> *) = C
            - Cof(C -> *) = ΣC
        - We define balls and spheres:
            - D^{-1} := ...
                S^{-1} := , the initial object in Cat_w (the empty category)
            - D⁰ := *, the terminal object in Cat_w,
                S⁰ := ΣS⁻¹ := *⨿* := * ⨿_{∅} *
            - D¹ := ΣD⁰ := Σ* := * ⨿_{*} *,
                S¹ := ΣS⁰ := * ⨿_{*⨿*} * = Σ² ∅
            - D² := ΣD¹ := Σ² *
                S² := ΣS¹ := Σ³ ∅
            - ...
            - Dⁿ := ΣDⁿ⁻¹ = Σⁿ *
                Sⁿ := ΣSⁿ⁻² = Σⁿ⁺¹ ∅,

        - Walking-arrow shapes and copower/power:
        - Fix a family of “walking k-morphism” shapes Iᵏ, with I⁰ = *, I = {0 → 1}, and Iᵏ := Iᵏ⁻¹ ⊗ I.
        - Define copower/tensor ⊗ and power (–)^I := [I, –] := Fun(I, –) so that
            C ⊗ I ⊣ Fun(I, –)
        - With this, suspension and loop are concretely:
            ΣC ≃ C ⊗ I
            ΩC ≃ [I, C]
        - Thus:
            - D¹ := I
            - D² := D¹ ⊗ I, S¹ := S⁰ ⊗ I
            - ...
            - Dⁿ := Dⁿ⁻¹ ⊗ I, Sⁿ⁻¹ := S⁰ ⊗ I

        - Cells via mapping out of Iᵏ:
        - For C ∈ Catₙ, define its k-cells by
            Cᵏ := Fun(Iᵏ, C)
        - C is an n-type iff Cᵏ is contractible for all k > n (never “empty” once C is inhabited).

        - Interval attachment vs skeleta:
        - The construction I(C) := C ⊗ I¹ is the walking-arrow attachment with hom(C).
        - It is not a skeleton; it is the level-raising copower/suspension object.

        - Objects, morphisms, elements:
        - Ob(C) := C⁰ = Fun(I⁰, C) = Fun(*, C) ∈ Cat₀
        - Mor(C) := C¹ = Fun(I¹, C) ∈ Catₙ₋₁
        - Mor(C) = ΩC by the power/loop identification.
        - The “elements” level is encoded by adjoining Cat₋₁ := * and then taking
            Elt(C) := C⁻¹ := Ob(Ob(C)) ∈ Cat₋₁
        - This is essentially the (-1)-truncation/“mere inhabitation” layer.


    - Explicit fibration shapes and recursive symmetry:
        - For every k ≥ 1, the k-fold composition of Mor gives Morᵏ(C) = Cᵏ = Fun(Iᵏ, C), inducing
            Fib(Morᵏ) → Catₙ →_{Morᵏ} Catₙ₋ₖ,  Mor⁻ᵏ(x) = {C ∈ Catₙ | Morᵏ(C) = x}
        - For negative k, negative cells and categories are constructed by iterated tensoring (copower) with positive walking shapes:
            C⁻ᵏ := C ⊗ Iᵏ for k < 0
        - These extend the NN-grading on Cat_w to a ZZ-grading, where:
            Cᵏ :=
                C⁻ᵏ for k < 0,
                Ob(C) for k = 0,
                Morᵏ(C) for k > 0.

        - The hierarchy and symmetry for cells of positive and negative degree:
            - Cⁿ ∈ 0-Cat,
            - Cⁿ⁻¹ ∈ 1-Cat,
            - ...
            - C² ∈ (n-2)-Cat,
            - C¹ ∈ (n-1)-Cat,
            - --------------------
            - C⁰ ∈ (n-1)-Cat,
            - C⁻¹ ∈ (n-2)-Cat,
            - ...
            - C⁻⁽ⁿ⁻²⁾ ∈ 1-Cat,
            - C⁻⁽ⁿ⁻¹⁾ ∈ 0-Cat.

        - For connective objects in Catₙ, the hierarchy simplifies:
            - Cⁿ ∈ 0-Cat,
            - Cⁿ⁻¹ ∈ 1-Cat,
            - ...
            - C² ∈ (n-2)-Cat,
            - C¹ ∈ (n-1)-Cat,
            - C⁰ ∈ (n-1)-Cat.

        - This allows regarding an element of Catₙ as an element of Cat_w, defined as a colimit above, with Cᵏ = {*} for all k < 0 and all k > n, and Cᵏ ∈ Catₙ₋ₖ for 0 ≤ k ≤ n.
        - Letting Iₙ := [0, n-1] ⊂ ℤ, we can construct an element of Catₙ as a functor F: Iₙ → Cat_w such that F(k) = Cᵏ ∈ Catₙ₋ₖ for all k ∈ Iₙ, and then defining C := colim(F). This can be concretely represented by an element of the product category:
            [Cⁿ, Cⁿ⁻¹, ..., C², C¹, C⁰] ∈ Cat₀ × Cat₁ × ... × Catₙ₋₂ × Catₙ₋₁ × Catₙ₋₁.

        - For every n, there is a contractible object pt ∈ Catₙ, with ptᵏ = {*} for all k ∈ ℤ.
        - It is terminal in Catₙ. It can be constructed inductively by starting with a raw singleton set {x} where x = {}, regarding this as a discrete 0-Cat, and defining
            - pt⁻¹ = Σ(pt⁰), the category with a single object p₋₁ and an identity morphism id_{p₋₁} indexed by x,
            - pt⁻ᵏ := Σ(pt⁻⁽ᵏ⁻¹⁾) for k ≥ 2,
            - pt⁰ := {x},
            - pt¹ := {id_{pt⁰}},
            - ptᵏ := {id_{pt⁽ᵏ⁻¹⁾}} for k ≥ 2.

        - For any C ∈ Catₙ, we interpret higher cells as morphisms of lower cells:
            - C⁻ᵏ = {*} for all k ≥ 1,
            - C⁰ as the (n-1)-category of objects in C, often just a 0-category (set).
            - C¹ as the (n-1)-category of morphisms between objects in C,
            - C² as the (n-2)-category of morphisms between morphisms in C,
            - ...
            - Cⁿ⁻¹ as the 1-category of morphisms between (n-2)-morphisms in C,
            - Cⁿ as the 0-category (set) of morphisms between (n-1)-morphisms in C.
            - Cⁿ⁺ᵏ = {*} for all k ≥ 1.

        - Dually, we can work top-down and interpret lower cells as objects within higher cells:
            - Cⁿ⁺ᵏ = {*} for all k ≥ 1,
            - Cⁿ as some 0-category (set) C,
            - Cⁿ⁻¹ as the 1-category of objects in C,
            - Cⁿ⁻² as the 2-category of objects of (objects of C), i.e. elements in objects of C,
            - Cⁿ⁻³ as objects of (elements of objects in C),
            - ...
            - C¹ as the (n-1)-category of objects in ( ... (objects in C) ... ),
            - C⁰ as the (n-1)-category of objects in C¹,
            - C⁻ᵏ = {*} for all k ≥ 1.

        - There exists a notion of an n-category: a connective object D such that Dᵏ = {*} for all k > n and Dⁿ is nontrivial.
        - We write n-Cat for the full subcategory of Cat_w spanned by n-categories.

        - For C any category, define:
            - Elt(C) := C⁻¹ := Ob(Ob(C)),
            - Ob(C) := C⁰,
            - Mor(C) := C¹,
            - Nat(C) := C², and more generally,
            - Morᵏ(C) := Cᵏ⁺¹ for k ≥ 0, so Mor⁰(C) = Mor(C), Mor¹(C) = Nat(C), etc.
        - These are related by:
            - Elt(C) = Ob(Ob(C)),
            - Nat(C) = Mor(Mor(C)),
            - Morᵏ(C) = Mor(Morᵏ⁻¹(C)) for k ≥ 1.
        - So a priori, these define functors:
            - Elt: n-Cat → (n-2)-Cat,
            - Ob: n-Cat → (n-1)-Cat,
            - Mor = Mor^0: n-Cat → (n-1)-Cat,
            - Nat = Mor^1: n-Cat → (n-2)-Cat,
            - Mor^k: n-Cat → (n-k-1)-Cat for k ≥ 0.

        - This hierarchy realizes the following:
            - Cat in 2-Cat:
                - Elt(Cat) in 0-Cat: Objects X in categories C.
                - Ob(Cat) in 1-Cat: Categories C.
                - Mor(Cat) in 1-Cat: Functors F: C_1 → C_2.
                - Nat(Cat) in 0-Cat: Natural transformations η: F → G.
            - C in 1-Cat:
                - Elt(C) in (-1)-Cat: Elements x in X
                - Ob(C) in 0-Cat: Objects X in C.
                - Mor(C) in 0-Cat: Morphisms f: X_1 → X_2 in C.
                - Nat(C) in (-1)-Cat: *
            - X in 0-Cat:
                - Elt(X) in (-2)-Cat: *
                - Ob(X) in (-1)-Cat: Elements x
                - Mor(X) in (-1)-Cat: *
                - Nat(X) in (-2)-Cat: *
            - Hom_C in 2-Cat:
                - Elt(Hom_C) in 0-Cat: Morphisms f: X → Y for X, Y in C in 1-Cat
                - Ob(Hom_C) in 1-Cat: Hom categories Hom_C(X, Y) for X, Y in C in 1-Cat
                - Mor(Hom_C) in 1-Cat: Functors F: Hom_C(X_1, Y_1) → Hom_C(X_2, Y_2)
                - Nat(Hom_C) in 0-Cat: Natural transformations η: F → G
            - Hom_C(X, Y) in 1-Cat:
                - Elt(Hom_C(X, Y)) in (-1)-Cat: *
                - Ob(Hom_C(X, Y)) in 0-Cat: Morphisms f: X → Y for X, Y in C in 1-Cat
                - Mor(Hom_C(X, Y)) in 0-Cat: *
                - Nat(Hom_C(X, Y)) in (-1)-Cat: *
            - Fun = Hom_Cat in 2-Cat:
                - Elt(Fun) in 0-Cat: Functors F: C → D for C, D in 1-Cat
                - Ob(Fun) in 1-Cat: Functor categories Fun(C, D) in 1-Cat for C, D in 1-Cat
                - Mor(Fun) in 1-Cat: Functors α: Fun(C, D) → Fun(E, F)
                - Nat(Fun) in 0-Cat: Natural transformations η: α → β
            - Fun(C, D) in 1-Cat:
                - Elt(Fun(C, D)) in (-1)-Cat: *
                - Ob(Fun(C, D)) in 0-Cat: Functors F: C → D for C, D in 1-Cat
                - Mor(Fun(C, D)) in 0-Cat: Natural transformations η: F → G
                - Nat(Fun(C, D)) in (-1)-Cat: *

        - Note: Ob, Elt, Mor, Nat, Mor^k all define endofunctors on Cat_w. For n < 0:
            - (-1)-Cat := Ob(0-Cat)
            - (-2)-Cat := Ob((-1)-Cat) := Elt(0-Cat)
            - ...
            - (-n)-Cat := Ob((-n+1)-Cat) for n ≥ 1
        - For n > 0:
            - 1-Cat := Mor(0-Cat)
            - 2-Cat := Mor(1-Cat)
            - ...
            - n-Cat := Mor((n-1)-Cat) for n ≥ 1
        - Also:
            - 1-Cat = Ob(2-Cat)
            - 2-Cat = Ob(3-Cat)
            - ...
            - n-Cat = Ob((n+1)-Cat) for n ≥ 1
        - Thus n-Cat can be defined either as Mor((n-1)-Cat) or as Ob((n+1)-Cat) for n ≥ 1.