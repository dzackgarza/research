# The unpolarized, unmarked moduli problem: K3, Enriques, lattice-polarized K3

Snapshot 2026-11-20. Labels: **read** = the quoted sentence was read in the text named;
**not read** = the source was named but its text was not opened in this session;
**not found** = searched and absent in the slice inspected.

Sources read: Huybrechts, *Lectures on K3 Surfaces* (CUP 2016), text version
`huybrechts-2016-lectures-on-k3.md` (research tmp/sources), Chapters 5, 6, 7 by grep and
the passages quoted; Kondo, *K3 Surfaces* (EMS 2020), `kondo-2020-k3-surfaces.md`, Ch. 6
and §9 by grep; Liedtke, *Arithmetic moduli and lifting of Enriques surfaces* (Crelle 2015,
arXiv:1007.0787), `liedtke-2013-arithmetic-moduli-enriques.md`, Intro and §§4-5;
Alexeev-Engel, *On lattice-polarized K3 surfaces*, arXiv:2505.22557 (HTML), §§3-5;
search highlights of Alexeev-Engel-Han arXiv:2110.13834 §2B, Gritsenko-Hulek-Sankaran
arXiv:1012.4155 §2, Harder-Thompson arXiv:1501.04049 §1.2, Di Lorenzo-Fringuelli-Vistoli
arXiv:2305.07574 §1. Zotero was not queried.

## K3 surfaces

### (a) Definition of the functor or stack

- Marked moduli space N (**read**). Huybrechts Ch. 6 §3.3: "As a set, N consists of all
  isomorphism classes of pairs (X, φ) with X a K3 surface and φ: H²(X,Z) → Λ a marking";
  the complex structure is glued from universal deformations, with a universal family
  f: X → N "together with a marking", reference [54, Exp. XIII] (Beauville et al.,
  Astérisque 126). Kondo Def. 6.8: "Let M be the set of isomorphism classes of marked K3
  surfaces." Alexeev-Engel Thm. 3.11: "There exists a fine moduli space M of marked
  analytic K3 surfaces, a non-separated, smooth complex analytic space of dimension 20
  endowed with an étale period map P: M → D, admitting a universal family."
- Unmarked unpolarized stack or functor of all K3 surfaces, with isomorphisms and pullback:
  **not found** as a defined object in any source read.
  - Searched: Huybrechts Ch. 5 (moduli functor M_d, polarized only; quasi-polarized M'_d
    in §1), Ch. 6 §§3-4, Ch. 7 §§2, 5 (grep "stack", "functor", "unmarked"); Kondo Ch. 6;
    Alexeev-Engel §§3-5; two web searches.
  - Found: every stack defined is polarized or lattice-(quasi)polarized (Huybrechts
    Thm. 5.1.3; Alexeev-Engel Def. 4.21, Thm. 4.22). The unmarked unpolarized object is
    treated only as the set O(Λ)\N.
  - Conclusion (inference): the sources read do not define the stack [N/O(Λ)] of all K3
    surfaces or prove properties of it.
  - Confidence: medium.
  - Gaps: Beauville Astérisque 126 Exp. XIII, Rizov's papers, Verbitsky (Duke 2013) and
    the Huybrechts Bourbaki talk, Giansiracusa (JLMS 2009) and Kreck-Su were not read;
    MathOverflow was not searched.

### (b) Structure

- N is a smooth 20-dimensional complex manifold, not Hausdorff (**read**, Huybrechts Ch. 6
  §3.3 "Warning: The moduli space N of marked K3 surface exists as a (20-dimensional)
  complex manifold, but it is not Hausdorff."; Kondo Rem. 6.10 "this space is not
  Hausdorff", with Atiyah's quartic family, citing BHPV VIII §12).
- Hausdorff reduction (**read**, Huybrechts Ch. 7 Prop. 2.1): "The period map P: N → D
  factorizes uniquely over a Hausdorff space N̄", attributed to Verbitsky.
- Unmarked quotient: Huybrechts Ch. 6 Rem. 3.6(iii) (**read**), Burns-Rapoport:
  "the period map between the quotients is indeed a bijection O(Λ)\N ≅ O(Λ)\D" and "by
  passing to the quotient by the action of O(Λ) one gets rid of the non-Hausdorffness of N
  but creates it anew on the quotient of D." Kondo Rem. 6.7: "the quotient Ω/O(L) does
  not have the structure of a complex analytic space." Gritsenko-Hulek-Sankaran Thm. 2.7:
  O(L_K3)\Ω is in 1:1 correspondence with isomorphism classes of K3 surfaces; the action
  "is not properly discontinuous".
- Algebraic stack, DM, coarse space, base ring for the unpolarized problem: **not found**
  (same search as (a)). Polarized comparison (**read**): Huybrechts Thm. 5.1.3 "The
  groupoid M_d → (Sch/S) is a separated Deligne-Mumford stack of finite type", smooth over
  Z[1/(2d)] (Rem. 5.4.11); the quasi-polarized functor M'_d "is not separated"
  (Ch. 5 §1). Inference: the unpolarized unmarked groupoid has infinite discrete
  automorphism groups for some X (Aut(X) infinite), so it cannot be DM or quasi-separated
  of finite type; this is the analogue of Liedtke Rem. 5.3 and is not stated for K3 in the
  sources read.

### (c) Monodromy and O+(L)

- **read** Huybrechts Ch. 7 Prop. 5.5: "The monodromy group Mon(X) ⊂ O(H²(X,Z)) of a K3
  surface X coincides with the index two subgroup O+(H²(X,Z))"; Thm. 5.7 (Donaldson):
  "Mon(X) = ρ(Diff(X)) = O+(H²(X,Z))". Question 5.8 (connectedness of ker ρ) is open there;
  Prop. 5.11: Diff(X) → ρ(Diff(X)) has no section (citing Giansiracusa).
- **read** Alexeev-Engel-Han §2B: M has "two isomorphic connected components interchanged
  by negating φ"; the fibre π⁻¹(x) "is a torsor under the group Z₂ × W_x". So O(Λ)
  permutes the two components and O+(Λ) (up to the ±1 convention) stabilizes one; the
  orbifold fundamental group of [N₀/O+(Λ)] is then O+(Λ) only if N₀ is simply connected,
  which **not found** in the sources read.
- Farb-Looijenga (JDG 2024, search highlight, **read** at abstract/intro level): Teichmüller
  space of Ricci-flat metrics with Mod(M)-action and period map to Gr⁺₃(Λ_R), image
  simply connected. Giansiracusa's corrigendum (JLMS 2019) invalidates Thms. 1.1(i), 1.2.
  Kreck-Su: **not read**.

## Enriques surfaces

- (a) **read** Liedtke Intro: "the stack M_Enriques of smooth and unpolarized Enriques
  surfaces is not quasiseparated (that is, its diagonal is not quasi-compact)". The
  defining display of §5 is an image in the text version and was not read; the stack is
  introduced in §5 ("Clearly, both moduli spaces are stacks").
- (b) **read** Liedtke Rem. 5.3: "the automorphism group of a generic Enriques surface is
  infinite and discrete ... and so, although M_Enriques is a stack, its diagonal will not
  be quasi-compact." Rem. 5.7: "one could use Φ_forget and Prop. 5.4 to argue that
  M_Enriques ⊗ Z[1/2] is smooth, unirational, and 10-dimensional" (argued, not proved).
  Base: Spec Z. Polarized comparison: Cor. 5.2 M_CV,smooth is "a quasi-separated Artin
  stack of finite type over Spec Z", DM over Z[1/2]; Thm. 4.12 for M_CV,ample.
  Kondo Rem. 9.27(iii): "(Ω(L⁻) \ H)/Γ is called the moduli space of Enriques surfaces.
  Here we do not consider a polarization. No algebraic construction of this space is
  known"; quasi-affine by Borcherds (Rem. 9.27(iv)), Γ = O(L⁻).
- (c) Monodromy of the unmarked Enriques family as O(L⁻) or O+(L⁻): **not found** as a
  theorem in the sources read (Kondo states the period quotient by Γ = O(L⁻) only;
  Torelli by Horikawa/Namikawa, Rem. 9.27(i)). Gaps: BHPV VIII §§19-21, Namikawa 1985 not
  read.

## Lattice-polarized K3 and non-symplectic involutions

- (a) **read** Alexeev-Engel Def. 4.6 (functor of marked (Λ,h)-quasipolarized K3 surfaces,
  h very irrational) and Def. 4.21: "F^q_{Λ,σ} denote the moduli stack of
  (Λ,σ)-quasipolarized K3 surfaces ... the families parameterized by F^q do not have a
  marking." Dolgachev, *Mirror symmetry for lattice polarized K3 surfaces*
  (alg-geom/9502005), Thm. 3.1: cited by Alexeev-Engel, its text **not read**; Alexeev-Engel
  say their definition differs from Dol96 (Rem. 4.3) at non-separated points.
- (b) **read** Thm. 4.7: M_{Λ,h} "is represented by a non-separated, smooth complex
  analytic space of dimension 20 − rank Λ". Thm. 4.22: "F^q_{Λ,σ} = [M_{Λ,σ} : Γ] where
  Γ := {γ ∈ O(L_K3) : γ|_Λ = id_Λ}" and the quotiented period map to D_Λ/Γ is a bijection.
  Thm. 5.5: the ADE-polarized stack is the separated DM stack [D_Λ :_W Γ], coarse space
  D_Λ/Γ (Baily-Borel, Rem. 4.23). These need an h with h² > 0 in Λ: a lattice
  polarization in Dolgachev's sense fixes a big class, so it is not "unpolarized" in the
  sense of this question. Over C only.
- Non-symplectic involution, unpolarized: Alexeev-Engel-Han (Trans. AMS B 2024) build
  their moduli from the marked unpolarized M (§2B); a stack of (X, ι) with no polarization:
  **not found** in the highlights read. Gaps: that paper's §2C onward, Nikulin, Yoshikawa
  not read.
- (c) Γ is the group of changes of marking fixing Λ pointwise (Thm. 4.22, read); its
  relation to Õ⁺(T) is not stated in the passages read.

## The slogan "the unpolarized moduli of K3 surfaces is not separated"

| Occurrence | Sentence (quoted) | Object | Proof |
| --- | --- | --- | --- |
| Huybrechts Ch. 6 §3.3, Warning | "The moduli space N of marked K3 surface exists as a (20-dimensional) complex manifold, but it is not Hausdorff." | marked N | cited [54, Exp. XIII]; Atiyah's example elsewhere |
| Huybrechts Ch. 6 Rem. 3.6(iii) | "passing to the quotient by O(Λ) ... gets rid of the non-Hausdorffness of N but creates it anew on the quotient of D" | unmarked set O(Λ)\N ≅ O(Λ)\D, a topological quotient | Ch. 6 Ex. 1.9 (action not properly discontinuous) |
| Huybrechts Ch. 5 §1 | the quasi-polarized functor M'_d "is not separated" | polarized-type functor, unmarked | families (1.2) over a DVR given |
| Kondo Rem. 6.10 | "this space is not Hausdorff" | marked M (Def. 6.8) | cited BHPV VIII §12, Atiyah |
| Kondo Rem. 6.7 | "Ω/O(L) does not have the structure of a complex analytic space" | period quotient | none given |
| Alexeev-Engel Thm. 3.11 | "a non-separated, smooth complex analytic space" | marked M | sketch; non-separation cited [BR75, LP81, Bea85] |
| Alexeev-Engel §2 (1) | "the moduli stacks and coarse moduli spaces of smooth quasipolarized K3 surfaces are not separated" | quasipolarized stack, unmarked | the two-family example after it |
| Alexeev-Engel-Han §2B | "M is a non-Hausdorff 20-dimensional complex manifold" | marked M | cited [ast85] |
| Harder-Thompson §1.2 | quotient of Ω by isometries "won't be Hausdorff" | period quotient | cited BHPV VIII §12 |
| Gritsenko-Hulek-Sankaran after Thm. 2.7 | "the action of O(L_K3) is not well behaved ... not properly discontinuous" | period quotient | none in highlight |

No occurrence read attributes non-separatedness to an unmarked unpolarized stack of K3
surfaces with a proof for that stack. Ambiguous: none of the read sentences is ambiguous in
its own text; the slogan becomes ambiguous only when it is restated without the word
"marked" or "quasipolarized".
- Searched: the sources above; one web search for the slogan.
- Found: only the marked space, the period quotient and quasi-polarized stacks.
- Conclusion (inference): the slogan, where sourced, means the marked space N, the period
  quotient O(Λ)\D, or a quasi-polarized stack.
- Confidence: medium.
- Gaps: Beauville Astérisque 126, BHPV VIII, Rizov, Verbitsky, MathOverflow not read.
