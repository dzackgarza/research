# Open items

Things noticed while moving the dissertation from LaTeX back to Markdown that need the author's judgment.
None of them blocks the build, which compiles with no LaTeX errors.
What has since been settled is listed at the end, so that a reader can tell "resolved" from "never noticed".

## Unfinished text

- None. The last one, `\todo{Separate the Hodge-theoretic work}` in [[450-scattone|Scattone boundary analysis]], is resolved: the lattice-theoretic cusp enumeration and the limiting mixed Hodge structures at the boundary are now separate subsections, and the second opens by saying what it adds that the first does not supply.

## Possibly missing content

- [[450-scattone|Scattone boundary analysis]] carries
  the Scattone boundary analysis only for $F_2$, where it lists the four
  lattices of the genus $G(1)$ containing $A_{17}$. Working notes in the old
  dissertation tree also carried the parallel analysis for $F_4$, where
  $N \cong D_7$: the seven Niemeier lattices containing $D_7$

  $$\tilde E_8^{3},\ \tilde E_8 \oplus \tilde D_{16},\ \tilde E_7^{2} \oplus \tilde D_{10},\ \tilde D_{12}^{2},\ \tilde D_8^{3},\ \tilde D_9 \oplus \tilde A_{15},\ \tilde E_6 \oplus \tilde D_7 \oplus \tilde A_{11}$$

  and their orthogonal complements, giving nine possibilities, among them
  $\tilde D_{17}$, $\tilde D_{12} \oplus \tilde D_5$,
  $\langle -4 \rangle \oplus \tilde D_8^{2}$,
  $\tilde A_1^{2} \oplus \tilde A_{15}$, and $\tilde E_6 \oplus \tilde A_{11}$.
  The list displayed is the one the working notes carried. It is unsettled, and a revision of
  this note that replaced one of its items was wrong to do so; the list as it stands is neither
  verified nor known to be complete.
  Counting subdiagrams of one fixed simple-root diagram does not enumerate root embeddings: in
  the model of $E_8$ whose roots are the $\pm e_i\pm e_j$ and the half-spinors, the simple roots
  $e_1-e_2,\dots,e_6-e_7,e_6+e_7$ generate a $D_7$ inside the coordinates $1,\dots,7$, so $E_8$
  does contain $D_7$, although $D_7$ is no subdiagram of the standard $E_8$ diagram.
  Nor is $D_7$ an orthogonal direct summand of $D_n$ in the coordinate block: $D_7\oplus
  D_{n-7}$ has index $2$ in $D_n$, since $D_n$ imposes one parity condition on the whole
  coordinate vector and that block imposes two, so the gluing has to be kept and primitivity
  checked rather than assumed.
  Both points were got wrong in the previous revision of this note, which therefore does not
  correct the list either: which lattice-theoretic condition on a Niemeier lattice these seven
  items are meant to satisfy is still to be read off Scattone's construction, and until it is,
  the degree-$4$ case is open and no replacement list should be quoted.
  What the certified degree-2 data now says about the shape of the condition.  The four
  boundary lattices computed from the source presentation are one genus: rank 17, signature
  (0,17), even, determinant -2, discriminant module Z/2.  The sentence above, that the four are
  "the four lattices of the genus G(1) containing A_17", is therefore the kind of statement the
  degree-4 case needs -- a genus plus a root lattice contained with finite index -- and not a
  list of complements.  It is not yet reproduced for degree 4: the genus of the corresponding
  T_8 quotient and the root lattice whose containments enumerate the cusps would have to come
  from Scattone's ch. 5-6, which have not been read, and the seven-item list above should not be
  quoted until they are.
  The degree-4 condition has an accessible primary source, and the attribution is to
  Laza--O'Grady directly: *GIT stability of K3 surfaces of degree 4*, arXiv:1801.04845, Appendix A.
  Their Sec. 2.1 sets Lambda_N = U^2 + D_{N-2}, with D_N the negative definite Dynkin lattice and
  D_1 the rank one lattice with generator of square -4 (the family's low-rank convention, not one
  of the root types below), and F(N) = Gamma(N)\D^+(N) with Gamma(N) = O^+(Lambda_N) unless
  N = 6 mod 8, where Gamma(N) is a subgroup of index 3 in O^+(Lambda_N).  So n = 17 in Corollary
  A.5 and Theorem A.6 is N = 19 and Lambda_19 = U^2 + D_17, of rank 21; a rank two isotropic J
  leaves J^perp/J of rank 21 - 4 = 17.  Corollary A.5 identifies the image of alpha_N with the
  lattices in the genus of D_{N-2}; Theorem A.6 says a lattice in the genus of D_n (1 <= n <= 18)
  is determined by its root sublattice and lists them -- for n = 17 nine of them: D_17,
  D_9 + E_8, D_12 + D_5, D_3 + (E_7)^2, A_15 + D_2, A_11 + E_6, (D_8)^2, D_16, (E_8)^2 -- and,
  when the root sublattice has rank one less than the lattice, the lattice is an overlattice of
  R(M) + D_1.  Remark A.7 credits the cases n = 17, 18 to Scattone [Sca87, Sec. 6.3] and Camere,
  the method being the embeddings of D_k into the Niemeier lattices, tabulated in Table 9;
  Theorem A.12 and its table count the Type II components.

  It applies to the manuscript, and that is a computation rather than an inference.  The
  manuscript's convention is T_{2d} = <-2d> + U^2 + E8^2 of rank 21, so degree 4 means 2d = 4 and
  T_4 = <-4> + U^2 + E8^2.  `t4_is_lambda19.py` checks on the maintained baseline that
  T_4 is isometric to Lambda_19 = U^2 + D_17: is_isometric returns True, both being even of rank
  21, signature (2,19), determinant -4 and discriminant module Z/4.  Hence Corollary A.5 and
  Theorem A.6 do classify the rank-17 quotients in the degree-4 case, and the seven-item
  Niemeier list with its nine complements in the working notes is Theorem A.6(9) -- the nine
  lattices above, each named by its root sublattice, with D_1 = <-4> entering only the
  overlattice clause and not the list itself.

  An earlier version of this note got the indexing wrong (writing Lambda_18 = U^2 + D_16 for
  n = 17), called the case hyperelliptic degree 4 on the strength of the source's own summary
  sentence rather than its moduli definition, identified degree 4 with T_8, and called the
  difference a change of polarization.  All four were wrong; the determinant comparison alone
  settles that the n = 18 lattice is not T_4, and the isometry above settles that the n = 17 one
  is.  The count, and the two things it is a count of.  Laza--O'Grady's Sec. A.3 defines, for J in
  I_2(Lambda_N) -- rank two *saturated* isotropic -- the map alpha_N from their group's orbits,
  tilde Gamma^xi_N \ I_2(Lambda_N), to isomorphism classes of negative definite lattices of rank
  N - 2, by [J] -> [J^perp/J]; this is well defined because tilde Gamma^xi_N < O(Lambda_N) and
  O(Lambda_N)-equivalent J give isomorphic quotients.  Proposition A.4 gives the dichotomy for
  saturated J: either Lambda_N -> Hom(J, Z) is surjective, in which case J sits in U + U and
  J^perp/J lies in the genus of D_{N-2}, or its image has index two, in which case J sits in
  U + U(2) and J^perp/J is even, negative definite and unimodular -- and the second case cannot
  occur when N is not 2 mod 8.  Proposition A.11 says alpha_N is injective for N not 6 mod 8
  (with N = 14 the one exception), and Theorem A.12 draws the consequence: for N not 2 mod 8 the
  Type II components are uniquely labelled by the lattices in the genus of D_{N-2} listed in
  Theorem A.6.  For N = 19, which is 3 mod 8, all of that applies, so there are exactly nine Type
  II components, in bijection with the nine lattices.

  Two distinctions have to survive that sentence, and both are now settled rather than noted.
  First, nine quotient-lattice classes is not the same statement as nine orbits of primitive
  isotropic planes under an arbitrary group: it is nine orbits for the group the source's period
  space is divided by, and the bijection with lattices is Proposition A.11's injectivity.  Second,
  the two groups are read from their definitions and compared, not matched by name.

  The definitions, from the sources.  AET (arXiv:1903.09742, Sec. 3A, p. 15) take Gamma_{2d} to be
  the spinor-norm-one subgroup of the stabilizer of h in O(Lambda_K3).  The chapter's sentence had
  dropped the spinor condition and read "the intersection of the original orthogonal group with the
  subgroup stabilizing h", which is a different, larger group; it is corrected in
  sections/1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md to the source's definition,
  and the group itself is not redefined anywhere.  Laza--O'Grady's degree-four period space is the
  quotient by the *stable* orthogonal group: eq. (2.1.2) of arXiv:1607.01324, p. 27, reads
  O~^+(Lambda_19)\D^+ = F(19), which was read in the source and not taken from a summary; for
  N = 19,
  which is odd and 3 mod 8, their Gamma^xi_19 equals O^+(Lambda_19) with no index-3 case (ibid.
  Def. 1.1.2, Def. 1.2.1, Prop. 1.2.3, pp. 9-10), and the same proposition places the stable
  orthogonal group in O^+ with index two, the quotient generated by -id, which acts trivially on
  the projective domain.

  The bridge, proved.  Let Lambda = Lambda_K3, h primitive of square 2d > 0, T = h^perp.  These do
  not split integrally -- Lambda versus Zh + T has index 2d and determinant (2d)^2 against the
  unimodular determinant 1, and the certificate reproduces the mismatch for d = 2 -- only over Q;
  the integral statement is a gluing, treated in full in the paragraph on the splitting below, and
  the extension criterion used here is the one proved there: an isometry of T extends to Lambda
  fixing h exactly when it acts trivially on A_T.  With that, restriction rho: Stab_{O(Lambda)}(h)
  -> O(T) is injective, an isometry fixing h and acting trivially on T being the identity, and its
  image is the discriminant kernel O~(T) = ker(O(T) -> O(A_T)).  (ii) The spinor norms agree:
  g = id_{Qh} + g|_T on Lambda_Q, a factorization of g|_T into m reflections is one of g, and the
  multiplier c enters both the same way, so sn_Lambda(g) = sn_T(g|_T) under either normalization;
  and g preserves each component of the period domain exactly when g|_T does, since h is positive
  and the positive 3-space of Lambda_Q is Qh plus the positive 2-space of T_Q.  Hence

      Gamma_{2d} = {g in O~^+(T_{2d}) : sn_T(g) = 1},

  and the spinor norm has to be the one AET's period-group definition uses.  Gritsenko--Hulek--
  Sankaran, Abelianisation of orthogonal groups, Sec. 1 p. 3 [@GHS08], distinguish two objects:
  O^+ = ker(sn_R), the kernel of the *real* spinor norm, and O' = SO cap ker(sn_Q), the intersection
  of the special orthogonal group with the kernel of the *rational* one, with sn_K of a reflection
  given by [-r^2/2] in K^times / (K^times)^2.  These are different groups and the rational kernel
  need not have index at most two -- an earlier version of this note assumed it did, and that is
  withdrawn.  AET ask for the spinor-norm-one subgroup of the stabilizer, in the same breath as
  saying that the period domain is a component associated to O^+(2,19); under the real normalisation
  O^+ *is* that kernel, so the condition is the component condition, and
  ker(sn_R) cap O~^+ = O~^+ by definition.  Hence

      Gamma_{2d} = O~^+(T_{2d}),

  not merely a subgroup of index at most two: the isometry of the stabilizer of h is in Gamma_{2d}
  exactly when its restriction to T_{2d} lies in the stable orthogonal group.  The same reading is
  what Laza--O'Grady's Prop. 1.2.3 records, where -1 lies in Gamma^xi for every N and -1 lies in
  O~ only when N is even, so that for N = 19 odd the centre generates O^+/O~^+ and sits inside
  O^+, not outside it.

  The transport is canonical, which is what makes "under the retained isometry" unambiguous.  O~ is
  the kernel of the map to the discriminant module; an isometry T_4 -> Lambda_19 carries that
  module and its quadratic form to the other side (both are Z/4 here, printed by
  computations/reports/t4_group_comparison.py), so it carries one discriminant kernel onto the
  other, and different isometries give the same subgroup of O(Lambda_19).  The certificate retains
  the isometry decision and does not print a matrix: the witness search is unavailable on this
  image, because Lattices.isometry_to() imports sage-indefinite-port, whose import of
  dzack_research.preamble.categories fails against the preamble checkout the image carries.

  The splitting, correctly stated.  Lambda_K3 is unimodular and h is primitive of square 2d > 0,
  so Lambda_K3 and Zh + T_{2d}, with T_{2d} = h^perp, are *not* equal: det(Zh + T_{2d}) = -(2d)^2
  in signature (3,19), of absolute value (2d)^2, and the index is 2d, against the unimodular
  determinant +-1; the certificate reproduces the mismatch (T_4 has determinant -4 and Zh the
  determinant +4, while Lambda_K3 is unimodular).  What holds is an orthogonal decomposition over Q, Lambda_QQ = Qh + T_{2d,QQ}, and
  integrally a finite-index gluing: A_{T_{2d}} = Z/2d = A_{Zh}, and Lambda_K3 is obtained from
  Zh + T_{2d} by adjoining the graph of an anti-isometry gamma: A_{Zh} -> A_{T_{2d}} of discriminant
  forms.  An isometry g of Lambda_K3 fixing h restricts to T_{2d}, and an isometry g_T of T_{2d}
  extends to Lambda_K3 fixing h exactly when g_T x id on A_{T} + A_{Zh} preserves that graph.  The
  graph is the image of gamma, so it is preserved exactly when g_T o gamma = gamma, and gamma is an
  isomorphism onto A_T: hence g_T is the identity on A_T.  (No appeal to the automorphism group of
  Z/2d is made or needed -- that group is {+1, -1} only for 2d = 4, 6 and a few others, and is
  larger for 2d = 12, so a claim phrased through it would have been false as stated.)  So the image
  of restriction is exactly O~(T_{2d}) = ker(O(T_{2d}) -> O(A_{T_{2d}})), the discriminant kernel
  and not the whole of O(T_{2d}); no splitting was needed for this, only the gluing.

  The spinor norm and the component.  For g with g(h) = h, g = id_{Qh} + g|_T on Lambda_QQ, a
  factorization of g|_T into m reflections is one of g, and the multiplier enters both sides the
  same way, so sn_Lambda(g) = sn_T(g|_T); and g preserves D^+ exactly when g|_T does, since the
  positive 3-space of Lambda_QQ is Rh plus the positive 2-space of T_QQ.  AET (Sec. 3A) define
  Gamma_{2d} as the spinor-norm-one subgroup of the stabilizer of h, in the same breath as calling
  the period domain a component of a domain associated to O^+(2,19); in the normalisation
  Gritsenko--Hulek--Sankaran fix [@GHS08, Sec. 1], O^+ *is* the kernel of the real spinor norm, and
  their sn_K of a reflection is [-r^2/2].  With that, ker(sn_R) cap O~^+ = O~^+ by definition, and

      Gamma_{2d} = {g in O~^+(T_{2d}) : sn_R(g) = 1} = O~^+(T_{2d});

  the rational object O' = SO cap ker(sn_Q) is a different subgroup and is not compared with the
  real component character anywhere here.  In particular a (-2)-root reflection has
  [-r^2/2] = [+1], so it lies in every kernel under discussion, which is the point of GHS's
  normalisation.

  Which reflections are in the discriminant kernel, measured.  For a *primitive* r, rho_r fixes A_L
  exactly when |q(r)| = 2, as the arithmetic above shows; measured through the owner's morphism
  isometry.discriminant_morphism() with Lattices.stable_orthogonal_group() as the kernel, the
  (-2)-root a_1 of Lambda_19 is in the kernel, a_16 + a_17 of square -4 is not, -1 on one hyperbolic
  summand is, the uniform -1 on H = U + U is, and the generator of T_4's <-4> summand is not.  The
  earlier claims that a (-4)-vector of even divisibility is a witness, and that the (-2)-root lies
  outside the kernel, are both withdrawn: the first is false, the second came from a transposed
  contragredient in my own test file.  The primitivity hypothesis is not decorative -- r = 2a with
  a^2 = -2 gives the same reflection as a while |q(2a)|/2 = 4 -- and the library's reflection()
  refuses r = 2a because it tests the scalar coefficient.  A minimal reproduction and the exact
  contract are in computations/reports/se_reflection_nonprimitive_repro.py: the published contract
  says the reflection exists exactly when the scalar is integral, which is false for non-primitive
  root, so the defect is a false negative and belongs to sage-extensions; the fix is either to
  state the contract for primitive root or to test the image rather than the scalar.  Nothing here
  works around it.

  The orbits, in both quotients, and then the count.  Let I_2 be the set of rank-2 saturated
  isotropic sublattices.
  (i) O~^+ inside O^+.  The centre -id lies in O^+(Lambda_19) -- the positive plane is two
  dimensional and det on it is (-1)^2 = +1 -- and not in O~(Lambda_19), since A_{Lambda_19} = Z/4
  and -1 acts on it non-trivially.  It maps every sublattice onto itself as a set, so it fixes each
  J in I_2 setwise; hence Stab_{O^+}(J) meets O^+ \ O~^+ and, by Laza--O'Grady's Remark A.9
  [@LO21], the fibre of O~^+\I_2 -> O^+\I_2 is a singleton: the two groups have the same orbits.
  (ii) The O/O^+ component quotient.  This is the step the centre does not supply.  Lemma A.10(1)
  [@LO21] states that for every J in I_2(U + U) there is an element of O(U + U) \ O^+(U + U) fixing
  J; with Prop. A.4 writing Lambda_19 = H + L, H = U + U, such an element extended by the identity
  on L is an isometry of Lambda_19 outside O^+ fixing J, and it lies in O~(Lambda_19) because H is
  unimodular and it acts identically on L, where the discriminant lives.  The concrete instance is
  -1 on ONE hyperbolic summand with +1 on the other and on L: measured, it fixes J = <e_1, e_2> as
  a sublattice, lies in the stable group, has -1-eigenspace of signature (1,1) so det on the
  positive plane is -1, and its spinor character is c^2 * 2 * (-2).  So O-, O^+, O~- and O~^+-orbits
  on I_2 are one and the same set of orbits.
  (iii) The count.  For N = 19, Prop. A.11's injectivity and Cor. A.5 give the image of alpha_19 as
  the genus of D_17, and Theorem A.12 with Table 8 gives nine Type II components; A.6(9) lists the
  nine by root sublattice -- six of rank 17 (D_17, D_9 + E_8, D_12 + D_5, D_3 + (E_7)^2,
  A_15 + D_2, A_11 + E_6) and three of rank 16 (D_16, (E_8)^2, (D_8)^2), which complete to rank 17
  as overlattices of the root lattice plus D_1 = <-4>.  Hence there are nine orbits, and by the two
  steps above they are the orbits of Gamma_{2d} as well.

  The next open gap, named and not yet done.  The nine labels of Theorem A.6(9) are quoted from the
  source and have not been constructed here.  Remark A.8 prints the construction: the lattices of
  the genus of D_n other than D_n itself are index two overlattices of D_a + D_b (a + b = n) given
  by adjoining the norm -4 vector named by an order two isotropic subgroup of A_{D_a} + A_{D_b} --
  H = <(xi_a, xi_b)> always gives D_n, and for special pairs the source writes out
  H = <(alpha_a, alpha_b)> and H = <(alpha_12, xi_b)> with their glued vectors.  Carrying that out
  for the nine, and checking rank 17, evenness, negative definiteness and the discriminant form
  against D_17, is the next piece of work; nothing above depends on it beyond the citation of A.6,
  and the chapter says as much.

  What is claimed, and what is not.  The degree-four space has nine Type II boundary components,
  labelled by the nine lattices in the genus of D_17, and the same nine are the Gamma_{2d}-orbits of
  primitive isotropic planes: the count is not conditional and no index-two refinement survives.
  Withdrawn in the course of this: that the comparison was the open step; that Gamma sat in the
  discriminant kernel with index at most two; that a rational squareclass should be compared with a
  real component character; that the central -id lies outside O^+; that a (-4)-vector can be a
  witness; and the plan of settling anything by a search over gluings.  The isometry T_4 = Lambda_19
  is a change of coordinates, never a change of polarization.

  The general cusp mechanism corrected, and two chapter statements retired.  The section claimed
  that cusp enumeration reduces to isotropic subgroups of the discriminant group A_{T_{2d}}.  At
  d = 1 it does not: A_{T_2} = Z/2, and its non-zero element is not isotropic -- the retained form
  D.q, evaluated in D.quadratic_value_module() = Q/2Z, does not vanish on it -- so {0} is the only
  isotropic subgroup, one class, while the Baily-Borel boundary of F_2 has four 1-cusps
  (AET Sec. 3B).  What classifies the orbits is the quotient lattice J = I^perp/I together with the
  gluing of J back into T_{2d}; at d = 1 the four quotients are pairwise non-isometric, and at
  d = 2 nine classes in a single genus give nine orbits (Prop. A.11 injectivity), so neither the
  discriminant group nor the genus is the classifier.  The splitting that makes J = L and
  A_{T_{2d}} = A_L is Prop. A.4's and is quoted only inside its hypotheses (Lambda_N = U^2 +
  D_{N-2}, 3 <= N, I a rank two saturated isotropic sublattice, case (1) surjectivity, second case
  excluded for N not 2 mod 8); in this book it is used only for T_4 = Lambda_19 with
  19 = 3 mod 8.  The chapter now says that.  The second retirement is the Type III
  sentence: the Baily-Borel stratum at a 0-cusp is a point (AET Sec. 3B), and eta^perp/eta for a
  primitive isotropic line has rank 19 and signature (1,18), which is not a Type IV signature, so
  no period domain is attached to it; the boundary point, the weight-two Hodge structure on the
  graded piece, and the toroidal data (which at a Type III cusp is nothing) are now kept apart in
  the chapter, with a correction made in turn: the Type III point has no Baily-Borel stratum of
  positive dimension, but it does carry fan data, and AET construct it -- for a 0-cusp I the lattice
  I^perp/I has signature (1,18) and the fan is supported on the rational closure of its positive
  cone (Sec. 3C), realised for the unique 0-cusp of F_2 as the Coxeter fan (Sec. 4A, 4C).  The
  earlier sentence in this note that the toroidal data at a Type III cusp is "nothing" was wrong and
  is withdrawn, and so is the sentence that replaced it, that the 0-cusp contributes no divisor:
  rays of the fan inside the open positive cone give toric divisors over the Type III point, and
  the null rays are the ones whose strata the open set V_I does not fully contain (AET Sec. 3C),
  the strata themselves being AET's torus quotients of elliptic subdiagrams and j-line fibre
  products of maximal parabolic ones (Prop. 4.13).  Both facts are computed in
  computations/reports/cusp_mechanism_audit.py, and that certificate was itself rewritten twice.  The object is the formed finite module
  D = T.discriminant_quadratic_form(), which is A_L *with* its quadratic form; D(x) coerces an
  element and is not the form, so the value is D.q(x), with values in D.quadratic_value_module()
  (QQ/2Z here, Nikulin's convention mod 2Z, nothing hand-divided), and isotropy is asked of the
  same object through D.isotropic_elements().  Earlier versions counted the 21 module generators of
  the embedding as elements, hand-divided a Gram entry, and called the module as if it were the
  form -- mistakes of mine as consumer, not library defects -- and those versions are retired.  Laza--O'Grady's Prop. A.4 is quoted in the chapter
  only inside its own hypotheses (Lambda_N = U^2 + D_{N-2}, 3 <= N, I a rank two saturated
  isotropic, case (1) surjectivity, excluded second case for N not 2 mod 8), and only for the
  degree-four case, where T_4 = Lambda_19 and 19 = 3 mod 8; it is not asserted for a general T_{2d}.

  The Sterk construction has been run against the five subsections, on the shared image with its
  OCI environment (JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot:) and the canonical
  sage-extensions, and its transcript is kept at computations/reports/sterk-cusp-diagrams-run.txt.
  It works through five named isotropic representatives and, for each, the roots of
  v^perp/Zv and the maximal parabolic subdiagrams:

    v = e                    12 roots    9 maximal parabolic subdiagrams
    v = e'                   10 roots    2
    v = e' + f' + abar_8     12 roots    4
    v = 2e' + f' + abar_1    11 roots    5
    v = 2e + 2f + abar_1     14 roots   13

  What that does and does not settle for the chapter's claims.  The subdiagram arithmetic is
  reproduced with its named representatives, so the *structures* behind the ray counts are now
  machine output rather than assertion.  But the chapter's counts are 4/4, 2/8, 3/15, 4/12, 5/17
  (Type II/III in the Coxeter compactification), and matching those to the five rows above is not
  a lookup: the counts are orbit counts under the diagram's symmetries rather than counts of
  subdiagrams, and that reduction had to be done at all five cusps.  The Type III side of it was
  got wrong here, and the sentence that stood in this place is corrected: those rays are not among
  the maximal *parabolic* subdiagrams at all -- they are the elliptic subdiagrams of rank 9, as the
  rank-9 paragraph below records.  The nine maximal parabolic subdiagrams of v = e and their four
  orbits (E8, E7 + A1, D8, A7 + A1) are cusp 1's four Type *II* rays; its Type III rays are a
  separate four, elliptic.

  Nor is the correspondence
  between the manuscript's five cusps and Sterk's five representatives yet written down: the
  manuscript distinguishes cusp 1 by the label (10,10,0) and the others by (10,8,0), which does
  not by itself order them.

  The reduction is done on the maintained API's labelled action on the original vertices
  (G.add_vertices(range(n)) first, so no source root is only a partition member; vertices carry
  their norm through the partition, edges their labels; algorithm="sage" named explicitly, since
  this image's default Bliss backend segfaults on the smallest input).  It verifies the Type II
  counts and says nothing yet about the Type III ones:

    representative                roots  |Aut|  parabolic orbits  manuscript Type II
    3.3.7   v = e                 12     4      4                 4     verified
    3.3.9   v = e'                10     1      2                 2     verified
    3.3.10  v = e' + f' + abar_8  12     2      3                 3     verified
    3.3.11  v = 2e' + f' + abar_1 11     2      4                 4     verified
    3.3.12  v = 2e + 2f + abar_1  14     8      5                 5     verified

  A claim of "Type III does not reproduce" was made here and is withdrawn.  It came from a
  selection error, not from the manuscript: v^perp/Zv has signature (1,9) and rank 10, and by
  AET's Theorem 4.3 the cone dimension is the ambient rank minus the elliptic rank, so a Type III
  *ray* (dimension one) needs elliptic rank 10 - 1 = 9, while rank 8 counts two-dimensional cones;
  parabolic rank 8 stays right for the Type II rays.  The numbers I compared (35, 45, 84, 65, 88
  against 4, 8, 15, 12, 17) were therefore orbits of the wrong-rank subdiagrams, and the agreement
  between my two readings was tautological besides: the local maximal_elliptic(M, rank=8)
  discarded subsets larger than 8 before testing maximality, so "rank exactly 8" and
  "inclusion-maximal within rank 8" were the same set by construction and tested nothing.

  The local checker is retired.  The Type III count is taken from the owner's enumeration instead,
  maximal_elliptic_subdiagrams(connected=False), which is maximality by inclusion with no rank cap,
  and its vertex sets are acted on by the labelled automorphisms of the diagram rather than by the
  coarser Coxeter-order group of the owner's own orbit methods.  Removing the local rank cap did
  not by itself fix the count, because maximality by inclusion is still not the right *selection*
  at these cusps: the maximal elliptic subdiagrams occur in two ranks, and the chapter's Type III
  rays are only those of rank 9.  For the five cusps in Sterk's order the owner returns
  44, 9, 34, 29 and 132 maximal elliptic subdiagrams, of which 30, 1, 5, 8 and 30 have elliptic
  rank 8 and 14, 8, 29, 21 and 102 have rank 9.  A Type III *ray* needs rank 9 because
  v^perp/Zv has rank 10 and signature (1,9) and the cone dimension is the ambient rank minus the
  elliptic rank (AET, Thm 4.3); a rank-8 elliptic subdiagram spans a two-dimensional cone and is
  not a ray.  So the mixed-rank orbit counts 15, 9, 18, 17 were that selection error, not a
  contradiction of the chapter, and the run that produced them
  (computations/reports/sterk_owner_subdiagrams.py, background job jmvx3lwga) is superseded; it
  stopped at the fifth cusp and its output is kept as it stood.

  With rank 9 selected the counts are 14, 8, 29, 21, 102 subdiagrams and 4, 8, 15, 12, 17 orbits
  under the labelled action, which is the chapter's list exactly, at all five cusps and in all
  five entries.  That is computations/reports/sterk_type_iii_rays.py with transcript
  sterk_type_iii_rays-run.txt, and it runs on the maintained rooted diagrams
  (Sterk.diagrams(), vertices r_0..r_{n-1}) as well as on the reconstruction's own root family,
  the two being carried into one another set for set.  The enumeration is also cheap now:
  sage-extensions 6ce8cdeb2b6d579c766f30f41811f482d333ae3c decides inertia and maximality on
  vertex sets and constructs only the survivors, so the five diagrams take tens of seconds where
  building every induced diagram took about half an hour.

  The semifan and irrelevant-subgroup statements, audited against the *retained figure
  numbering* -- which is not the Sterk script's a-indexing and had to be found first.  The diagram
  objects live in the pandoc configuration, not in this repository:
  figures/objects/coxeter/sterk-cusp-{1,3,4,5}.tikz and vinberg-10-8-0.tikz in the .pandoc
  checkout, drawn through styles/macros/tikz/constructors/dzg-coxeter.tex.  Each states its
  provenance and its numbering: "Roots: dzack_research.preamble.sterk, Sterk.sterk_roots()[Sterk_k],
  the folds of the (18,2,0) roots under J_k ... Root i is the (i+1)-th root there and is labelled
  r_i, as in 900-five-cusps.md".  So the manuscript's r_i is the object's root i, and the objects
  also fix the correspondence: cusp 1 is "Sterk 1991, diagram I", cusp 3 diagram III, cusp 4
  diagram IV, cusp 5 diagram V, and vinberg-10-8-0 is "the Coxeter diagram of the 0-cusp eta_2
  (Sterk's diagram II)".

  The exact label correspondence, from the canonical ordered root family.  The objects are the
  pinned pandoc configuration, pandoc-config@a84f0becc5b777cf193b1ca6466cd4922556f5fa, and they
  read their roots from the maintained library rather than from the archived preamble:
  sage-extensions/src/sage_extensions/sterk.py:240-281.  That block orders the five configurations
  explicitly and, zero-based, gives

    Sterk_1  r_9  = v_21                    r_10 = v_22
    Sterk_3  r_10 = orbit_sum(v_20)         r_11 = orbit_sum(v_18)
    Sterk_5  r_12 = v_21                    r_13 = v_22

  with orbit_sum the folded orbit sum used for the two Sterk_3 roots; an earlier version of this
  note called it reflect, after the archived preamble, and that name is wrong for the maintained
  source.  So the pairs the manuscript names are particular roots of these ordered configurations:
  (v_21, v_22) for cusp 1, (orbit_sum(v_20), orbit_sum(v_18)) for cusp 3, (v_21, v_22) again for
  cusp 5.  The assets mark exactly those index pairs with the infinity weight -- cusp 1 "8-9-10-11
  bold (inner products 4)", cusp 3 \coxeteredges{infinity}{10/11}, cusp 5
  \coxeteredges{infinity}{12/13} -- so b(r_i, r_j) = 4 with both norms -4 at each named pair, an
  affine A~1.  The manuscript's named pairs are present in its own diagram source and are not to be
  reinterpreted through the Sterk script's a-numbering.

  Two orderings must not be confused, and the assets say so themselves: vinberg-10-8-0.tikz 5-11
  maps the folded Sterk_2 indices 0..9 to diagram vertices 1, 3, 4, 5, 6, 7, 8, 9, 10, 2, and the
  library exposes sterks_in_TEn() and sterk5_in_U_E8_2() in orderings of their own.  The transport
  from the separate Sterk script's a-indices to the manuscript's r_i is nevertheless established,
  and not by position or by count: it is the isomorphism of the two angle-labelled graphs -- root
  norm on the vertex, Coxeter weight on the edge, the sign of a pairing dropped as the diagram
  drops it -- and it is determined up to the diagram's own labelled automorphism group, of order
  4, 1, 2, 2, 8 at cusps 1 to 5, and no further.  Two independent readings of the r-side agree on
  the same map at every cusp: the parsed tikz objects, whose r_i is root i of the ordered family,
  and Sterk.diagrams(), which names its vertices r_0..r_{n-1} and is generated from that same
  family.  The maps are in computations/reports/sterk_figure_labels-run.txt and
  sterk_type_iii_rays-run.txt; anything that needs both numbering systems can now be read in
  either, with that residual ambiguity stated rather than resolved.

  The transport is checked on the signed Gram and not only on the diagram.  Norm and Coxeter
  weight do not pin a pairing down: b and -b give one weight, and between roots of unequal length
  the magnitudes 2 and 4 do too, so an angle-preserving map need not preserve a single signed
  pairing.  Each retained transport is therefore required to carry every entry of the
  reconstruction's Gram to the maintained diagram's -- signs and magnitudes, the full matrix and
  not its norms and angles -- and sterk_type_iii_rays.py reports how many of the angle-preserving
  coset elements do so: 4 of 4 at cusp 1, 1 of 1 at cusp 2, 2 of 2 at cusp 3, 2 of 2 at cusp 4
  and 8 of 8 at cusp 5.  So the transport is an isometry of the two Gram matrices and not only of
  their Coxeter diagrams, and the statement survives passing from the reconstruction's roots to
  the library's.  This was a missing check, not a found mismatch: adding it changes no count.

  With that numbering the three named-root statements check out, and my earlier "these pairs are
  not edges" conclusion is withdrawn -- it compared the manuscript's r-indices with the Sterk
  script's unrelated a-labels.  From the object files themselves: cusp 1 has "8-9-10-11 bold
  (inner products 4)", so r_9 . r_10 = 4 with both norms -4 and the pair spans an affine A~1, as
  the text says; cusp 3 has "10-11 bold"; cusp 5 has "12-13 bold".  All three statements are
  therefore consistent with the retained figure data.  What is still not computed is the finiteness
  or infinitude of any irrelevant subgroup, i.e. the semifan statements proper: the Sterk script
  does not implement the semifan construction, and nothing here substitutes for it.

  The representative-to-subsection matching is settled by source, not by counts: each object names
  its Sterk diagram number and its root family, and the root counts agree with the script's five
  representatives in the order 3.3.7, 3.3.9, 3.3.10, 3.3.11, 3.3.12 as 12, 10, 12, 11, 14.  Cusp 1
  is diagram I (12 roots), cusp 2 diagram II (10), cusp 3 diagram III (12), cusp 4 diagram IV (11),
  cusp 5 diagram V (14).

  The Type II counts, now computed at the owner.  sage-extensions
  2a1babbbc530430f1836707d6f2a4e8ad7a458ee publishes the complete caller query:
  is_componentwise_affine() accepts every nonempty subdiagram all of whose connected components are
  affine -- a single affine component included -- and maximal_componentwise_affine_subdiagrams()
  decides maximality over that whole family *before* any cap, with form_rank() the geometric rank
  (vertices less nullity) and max_rank still the vertex-count cap.  Computations/reports/
  sterk_type_ii_rays.py runs that query on the five cusp families and filters to form_rank() == 8
  explicitly, because a cap is not an equality: it returns 9, 2, 4, 5 and 13 maximal componentwise-
  affine subdiagrams, all of geometric rank 8 at these five cusps, and their orbit counts under the
  labelled action are 4, 2, 3, 4 and 5, the chapter's list in all five entries.  Each cusp's
  transport was re-decided on the signed Gram (4 of 4, 1 of 1, 2 of 2, 2 of 2 and 8 of 8 coset
  elements pass), and the two families -- the reconstruction's a_i Gram and Sterk.diagrams()'s r_i --
  are asserted to give the same rank-eight maximal unions element for element under it.  So the
  Type II numbers are no longer local-checker output: they are the owner's, and they agree with the
  provisional enumeration they replace.  The provisional numbers stay in the record as
  sterk-cusp-diagrams-run.txt, and sterk_figure_labels.py no longer calls the reconstruction's
  enumeration at all.

  Two properties of the query, recorded so that a reader does not repeat the hazard: the family
  includes a single affine component, so a connected affine subdiagram is in it -- is_parabolic_union(),
  which needs at least two components, would have missed exactly those; and max_rank caps the vertex
  count, not the geometric rank, so max_rank=8 is not the rank-eight condition and is not passed
  anywhere in these two scripts.

  So, separated: the Type II counts are *computed and accepted*, from the reconstruction script's
  per-component enumeration of rank-8 semidefinite subdiagrams together with the labelled action;
  the lattice data are *computed and accepted*; the Type III counts are *computed and accepted* as
  the orbits of the rank-9 elliptic subdiagrams; and the semifan/irrelevant-subgroup statements
  remain *source claims only*, one of them corroborated at the level of named roots, because
  nothing here implements the semifan construction -- the labelling obstacle is gone, the
  construction is not.  The owner's predicate is not a substitute for the Type II convention:
  is_parabolic() asks for nullity exactly one, while the chapter's Type II subdiagrams include
  disconnected ones (E~7 + A~1, A~7 + A~1, B~4 + B~4) whose nullity is one per component, so
  maximal_parabolic_subdiagrams() does not reproduce those counts and the reconstruction script's
  enumeration stays the one that does, for now.  That enumeration is a *local* checker and the
  Type II counts carry that provenance: they were not computed by the maintained API, so wherever
  they are quoted they are marked as checked against the reconstruction's per-component test and
  not as owner output, and they are to be re-derived and compared once the library query lands.

  Two facts about the published partial affine API, recorded so that nobody closes the gap with
  the wrong parameter.  is_parabolic_union() covers at least two affine components, so a single
  connected affine subdiagram -- which is most of what these counts are made of -- is outside it.
  And max_rank bounds the *vertex count*, not the Gram rank: the geometric condition here is
  nodes minus components equal to eight, i.e. nine vertices for a single affine component, so
  max_rank=8 is not that condition and must not be passed for it.  The reconstruction script's own
  maximal_parabolic_subdiagrams(M, rank) takes the geometric rank (nodes minus components), which
  is a different parameter from the library's max_rank; computations/reports/sterk_figure_labels.py
  calls it with 8 in that sense, and the two ought not to be read as the same thing.

  That query has since landed -- see the paragraph below on the owner computation -- and the
  provisional enumeration it replaces is kept only as the record of what was checked before it.

  The displayed subdiagrams, read from the chapter itself and transported through that map.  Cusp
  1 draws {0,1,2,4,5,6,7,8,11}, {0,1,3,4,5,6,7,8,10,11}, {0,1,2,3,5,6,7,8,11} and
  {0,1,2,3,4,5,6,7,9,10} in the figure's indexing, and each of the four is a maximal parabolic
  subdiagram, one from each of the four Type II orbits.  So the sentence that called them "the four
  elliptic subdiagrams displayed above" was wrong about the pictures: they are parabolic, and the
  four Type III orbits are the rank-9 elliptic subdiagrams, which the pictures do not show.  The
  sentence now attributes the display to the Type II orbits and states the Type III counting rule
  instead of pointing at the pictures.

  As the chapter stood, 14 of the 18 displayed sets over the five cusps were maximal parabolic
  subdiagrams and covered the orbits one for one -- cusp 1 four of four, cusp 2 two of two, cusp 3
  one of three, cusp 4 four of four, cusp 5 three of five -- and the four that were not have been
  replaced by computed orbit representatives of the orbits their cusp had left uncovered.  The four
  were cusp 3's second (ten nodes, indefinite) and third (eight nodes, of rank 7), and cusp 5's
  second (ten nodes, indefinite) and third (eleven nodes, indefinite).  The change is forced by type
  and node count and not by the choice of transport: a maximal parabolic subdiagram is negative
  semidefinite with one null direction per component, and no relabelling carries an indefinite set
  to one.  With the four replaced, all 18 are maximal parabolic subdiagrams and each cusp's
  displayed sets cover its Type II orbits exactly once.  The displayed sets are read from the
  chapter by the certificate rather than copied into it, so the two cannot drift apart unnoticed.

  What the chapter unit still does not claim.  The five cusps' identification with Sterk's five
  representatives is source-settled (each object names its diagram number and its root family, the
  root counts 12, 10, 12, 11, 14 agreeing in the order 3.3.7, 3.3.9, 3.3.10, 3.3.11, 3.3.12), but
  the Type II and Type III counts are orbit counts under the *diagram's* labelled symmetries, which
  is what the chapter says they are counted by, and whether those orbits are the Gamma-orbits of
  the chapter's fans is the group comparison recorded above and stays open.  The semifan statements
  are untouched and remain source claims.

  The five Enriques cusps' lattice data are checked as one unit in
  enriques_cusp_lattice_data.py.  Cusps 1, 3, 4 and 5 all quote T-bar = (18,2,0)_1 = U(2) + E8^2
  with invariant sublattice U(2) + E8(2); cusp 2 quotes (18,0,0)_1 = U + E8^2 with U + E8(2).  The
  maintained two-elementary API gives (18,2,0) and (10,10,0) for the first pair and (18,0,0) and
  (10,8,0) for the second, matching the text in all five subsections.

  The degree-two glue sentences in the chapter, reconciled with its own table.  Two sentences there
  still said the boundary lattices were "not settled" and that the overlattice was undetermined,
  which contradicted the marked-inclusion paragraph above them that records S, its index and its
  gluing subgroup for all four rows.  They now say what the table certifies (the marked inclusion,
  not a reading of the discriminant form) and what is not claimed (that an isometry class of
  J^perp/J follows from discriminant data alone), which is the formulation GAPS withdrew to earlier.

  The rank rule behind the Type III counts, from the source.  AET's Theorem 4.3 is an order
  reversing bijection between the faces of the fundamental chamber and the elliptic and maximal
  parabolic subdiagrams, under which a Type III cone of dimension d corresponds to an elliptic
  subdiagram of rank 19 - d and a Type II ray to a maximal parabolic subdiagram with 17 vertices;
  in the rank-10 quotient of an Enriques cusp that reads 10 - 1 = 9 for a Type III ray, which is
  exactly the rank AEGS25's Lemma 5.2 enumerates and exactly the rank the computation above used.
  The chapter now cites both where it states the rank.

  The irrelevant sets, now computed for four of the five cusps.  AEGS25's Figure 5 is read off the
  e-print artwork: the square panel (the (18,2,0) diagram) has vertices 0-15 on its boundary and
  16-21 in its interior, and Definition 5.4's irrelevant roots are the non-boundary ones.  With the
  retained fold data from Sterk.sterk_roots() -- every folded root written as a sum of the K3 roots
  -- and the identification v_i = figure vertex i-1 (which three independent agreements support: the
  manuscript's named pairs at cusps 1, 3 and 5 all land in the interior), the folded roots whose
  constituents are all non-boundary are, at cusp 1, the four entries r_8, r_9, r_10, r_11 (folding
  figure vertices {16,18}, {20}, {21}, {17,19}); at cusp 3, r_9, r_10, r_11 ({16,18}, {19}, {17});
  at cusp 4, r_9, r_10 ({16,19}, {17,18}); at cusp 5, r_8 to r_13 ({16}, ..., {21}).  The
  computation is computations/reports/sterk_irrelevant_roots.py.
  What that settles, against the retained labelled diagrams: at cusp 1 the four irrelevant roots are
  joined by the bold edges 8-9-10-11, so their Gram is indefinite and W_irr is infinite, which is
  Lemma 5.6's claim there; at cusp 3 the two roots r_10, r_11 are joined by the bold edge 10-11 while
  r_9 is orthogonal to both, so W_irr contains an affine A_1 factor and is infinite; at cusp 5 the
  bold edge 12-13 again gives an affine A_1 factor and infinitude; at cusp 4 the two irrelevant roots
  r_9 and r_10 are joined by no edge of the labelled diagram, so they are orthogonal and
  W_irr = S_2 x S_2, which is Lemma 5.6's S_2^2 there.  So three of the five finiteness verdicts and
  one of the two finiteness verdicts are now checked against the labelled data, and the manuscript's
  named pairs are inside the computed sets in each case.
  What is still open: cusp 2, whose diagram is the triangle panel and whose folded roots are the
  library's w1..w19 rather than v1..v22 -- Figure 5's triangle has interior vertices {17,19}, but the
  match from that numbering to the w-numbering is not recorded, so the single irrelevant root that
  Lemma 5.6's S_2 needs there is not yet identified.  And Lemma 5.8's deletion counts have not been
  re-derived: they need the irrelevant sets at all five cusps together with the subgraph lists.

  The semifan provenance, carried as far as the sources allow.  The e-print of AEGS25 is retained
  at .scratch/refs/aegs_src, and its figure numbering can now be read off en.tex instead of guessed:
  Figure 5 of the paper is fig-k3-cusps-circled.pdf, captioned "Coxeter diagrams for (18,2,0)_1 and
  (18,0,0)_1" -- the diagrams whose non-boundary roots Definition 5.4 calls irrelevant -- and its
  Figures 7 and 8 are fig-cusp2.pdf ("Folded diagram for cusp 2") and fig-cusps1345.pdf ("Folded
  diagrams for cusps 1, 3, 4, 5"), which are the diagrams the pandoc objects sterk-cusp-{1,3,4,5}
  and vinberg-10-8-0 transcribe in the manuscript's r-numbering.  The folded side is therefore
  retained in full: the library's Sterk.sterk_roots() records every folded root as an explicit sum
  of the K3 roots, e.g. Sterk_1's r_9 = v21, r_10 = v22, r_8 = v17 + v19, r_11 = v18 + v20, and
  Sterk_3's r_10, r_11 as orbit sums of v20, v18.
  What cannot yet be done, stated exactly: the correspondence between Figure 5's printed root
  numbers and the library's v1,...,v22 (or w1,...,w19) is not recorded anywhere in the repository,
  so the irrelevant subset of each *folded* diagram -- which is what Definition 5.4 transports --
  cannot be recomputed here, and with it neither can Lemma 5.6's S_2 and S_2^2 cases be checked
  independently nor Lemma 5.8's deletion counts be re-derived.  The labels are text in the artwork
  (pdftotext returns 6, 7, 8, ..., 21 from fig-k3-cusps-circled.pdf), but the circling and the
  square/triangle boundary membership are vector strokes; the same technique used for AET's Figure 1
  in writing/coble/scripts/certificates/read_fig1.py would read them, and that reading is the
  concrete next step rather than a library matter.
  What is verified without that correspondence: the three labelled pairs the manuscript names are
  affine A_1's (b = 4 with both squares -4, from the retained assets), which is what makes the
  irrelevant subgroup infinite at cusps 1, 3 and 5 once those roots are known to be irrelevant; the
  rank rule of AET Thm. 4.3 gives the rank-9 elliptic class that both AEGS25 Lemma 5.2 and the
  certificate enumerate; and the orbit counts agree with Lemma 5.2's numbers.
  The Gamma_k bridge, as far as it goes: by [Ste91] the groups induced on e^perp/e are
  Gamma_k = Aut(G_r^k) x| W(G_r^k) [AEGS25, Sec. 5.1].  The action computed here is Aut(G) on the
  Gram-labelled diagram, and it reproduces Lemma 5.2's counts exactly; what a reader of the source
  is entitled to ask, and what is not yet shown here, is that Aut(G) on subdiagram classes is the
  same quotient as Gamma_k on the fan -- equivalently, that the reflection factor W(G_r^k) moves no
  subdiagram class.  That is a statement about two actions, and it is the one piece of the bridge
  left open.

  The semifan claims, resolved as source statements with their hypotheses.  They are
  Alexeev--Engel--Garza--Schaffler's, not something this repository proves, and the chapter now
  carries the citations: Definition 5.4 (a folded root is irrelevant if it is the fold of an
  irrelevant root of Figure 5, i.e. of a root not on the boundary of the square or the triangle),
  Lemma 5.5 (the semifans are the generalized Coxeter fans with those roots), Lemma 5.6 (the
  irrelevant subgroup is S_2 at cusp 2 and S_2^2 at cusp 4, finite, and infinite at cusps 1, 3 and 5
  -- the cones there have infinitely many generators), Lemma 5.7 (toroidal over 0-cusps 2 and 4 and
  their adjacent 1-cusps and over 1-cusp 35, strictly semitoroidal elsewhere), and Lemma 5.8 (the
  deletion rule -- discard subgraphs with a connected component entirely of irrelevant vertices --
  giving 2+0, 2+7, 2+7, 4+7, 3+0, which are the chapter's semitoroidal rows exactly).  Also
  Lemma 5.2: the Coxeter-compactification counts 4+4, 2+8, 3+15, 4+12, 5+17 are that lemma's, its
  proof being a direct enumeration of maximal parabolic and rank-nine elliptic subdiagrams.  The
  affinity with the computations recorded above is exact -- the independent labelled-orbit
  enumeration gives 4/2/3/4/5 parabolic and 4/8/15/12/17 rank-nine elliptic orbits -- so the
  chapter's numbers are corroborated as well as cited.
  The diagram-to-arithmetic bridge is in the source too, §5.1: by [Ste91] the groups induced on
  e^perp/e are Gamma_k = Aut(G_r^k) x| W(G_r^k).  The action used in this book's computations is
  Aut(G) on the Gram-labelled diagram, and it gives the lemma's numbers; what is *not* established
  here is that Aut(G) acting on subdiagrams is the same quotient as Gamma_k acting on the fan --
  the reflection factor must be seen to move no subdiagram class.  That is the precise remaining
  step, and it is a statement about the two actions rather than a computation to be invented.
  No semifan implementation was written, and none is needed for the claims as they stand.

  The "Sigma versus N" note is not in the repository.  Searched: the whole tree for the phrase and
  for "zero-cusp invariant", for the glyph and the macro in markdown and text, the vault plans under
  .scratch/vault, the inbox, INTENT.md and the ultramath reports.  What turns up is unrelated
  (a ruled surface Sigma_4 in the Morrison--Flowerpot material, a Sigma in INTENT.md's algebra).  So
  the item stays unlocated: there is no original note to interpret, and nothing is asserted about
  what it meant.

  The five Enriques boundary types, computed.  What this note recorded as unsettled -- the
  boundary labels (10,10,0)_1 and (10,8,0)_1, which "need the five isotropic orbits and their
  quotients" -- is now computed: for each of Sterk's five representatives v of the Gamma_{En}-orbits
  of primitive isotropic vectors in L_- = H + H(2) + E8(-2), K = v^perp/Zv has rank 10 and
  signature (1,9), and its two-elementary invariants are (10,10,0) for v = e and (10,8,0) for the
  other four, matching the chapter's labels in all five rows (determinants -1024 and -256
  respectively).  The route is the retained one -- v.isotropic_reduction() for the quotient and
  EvenTwoElementaryLattices(K.base_ring())(K).two_elementary_invariants() for the type -- and the
  certificate is computations/reports/enriques_cusp_boundary_labels.py.

  The earlier six-minute stall was my call, not the library's.  A step-by-step timing certificate
  (computations/reports/enriques_quotient_timing.py, sixty-second alarm per step) shows the lattice
  building in 0.04 s, v.is_primitive() in 0.22 s, v.sublattice() in 0.03 s,
  v.orthogonal_complement() in 0.63 s and v.isotropic_reduction() -- the whole kernel, cokernel,
  Smith, lift and Gram evaluation -- in 0.89 s, returning rank 10, determinant -1024, signature
  (1,9).  So no orbit enumeration, no Julia call and no dual-hash bottleneck is involved on this
  route, and no library defect or owner gap is claimed: the stalled call was the subobject wrapper
  around the same reduction, and it is simply not used.

  The Niemeier-complement description of the four degree-two lattices is withdrawn rather than
  repaired.  The chapter now says which support it uses (AET's four labels, and the boundary
  lattices computed with their marked inclusions) and which it does not (reading each class as an
  E_7-complement in a Niemeier lattice), and why not: a complement is not a root sublattice of a
  fixed diagram, the witness being D_7 inside E_8 in the half-spinor model, so deleting nodes
  enumerates neither the embeddings nor their complements.  Three of the four still read visibly as
  complements; D_16 + A_1 does not, and closing that would mean exhibiting primitive embeddings,
  which is not done here and which nothing in the chapter depends on.

  Two things the audit did not settle and does not claim.  The boundary labels (10,10,0)_1 and
  (10,8,0)_1 are the manuscript's Enriques-cusp invariants and were not recomputed here from
  L_- = H + H(2) + E8(-2); they need the five isotropic orbits and their quotients, which is the
  Sterk transcription's job.  The arithmetic-group comparison, recorded here as open when this
  paragraph was written, is settled above: the manuscript's Gamma_{2d} is Laza--O'Grady's stable
  orthogonal group, and the nine Type II components of the degree-four space are its orbits on
  primitive isotropic planes, so that count does transfer.  Nothing in the Enriques chapter depends
  on it either way.

  The "Sigma versus N zero-cusp invariant" still does not resolve.  Inspected as asked: the
  introduction and historical context carry no such phrase, and the nearest textual home is the
  Enriques chapter's "The five cusps" section, where the five 0-cusps of F_{En,2} carry semifans
  Sigma_k and where N-type lattices appear in the AET sense; a Sigma-versus-N comparison could
  plausibly be about the Enriques transcendental lattice against that N.  That is a reading, not
  an identification, so nothing is asserted and the item needs its original note.
  Acceptance of the glue, when it is done, must keep the source-root images and the maintained
  inclusion and index maps -- the actual inclusion whose codomain is the computed quotient, with
  its index -- rather than resting on an isometry-class match or a determinant ratio.  For
  degree 2 that is in hand for all four rows (one inclusion for A_17 and for E_8^2 + A_1, two
  each for the two D rows, the quotient being determined in the first two cases and one of a
  pair in the others).
  The nine complements listed here and in the working notes have not been recomputed and
  should not be quoted until they are. What a complement names is a root system and not a
  lattice: at $d=1$ the four labels are root lattices of rank $17$ and determinants $2,8,8,18$,
  each sitting with finite index in the boundary lattice $J^\perp/J$ it labels, so a boundary
  lattice may be a proper overlattice of its label, and the glue subgroup is data the root
  system does not carry; for one of the four the boundary lattice is the label itself, and for
  the other three which overlattice occurs is not settled here (see
  [[450-scattone|Scattone boundary analysis]]).
  What is settled is the index. A unimodular sublattice of an integral lattice splits it
  orthogonally with no index, and `formalization/coble-enriques/Splitting.lean` proves that
  (`splits_of_unimodular`, `det_eq_mul_of_unimodular_block_diagonal`); since $J\oplus J'
  \cong U^{\oplus 2}$ for AET's complementary isotropic plane, $\det(J^\perp/J) = \pm 2$ for
  all four, and the index of the label is $1$, $2$, $2$, $3$. The lattice follows for
  $A_1\oplus E_8^{\oplus 2}$ and did not follow for the other three without a certified quotient
  and overlattice computation.  That computation has since been run, and its result is recorded
  below under the marked inclusion; the paragraph that follows describes the state before it, and
  is kept only for the API inventory it lists, `sage-extensions` at revision
  `441519c574cec12ada06ad586f6c3862fbca96d0` (clean checkout) has every operation it needs --
  `primitive_isotropic_subobject` (`lattices.py:7312`), `isotropic_reduction`
  (`lattices.py:5688`, `:8414`), `even_overlattice_inclusions` (`lattices.py:5937`),
  `discriminant_module` (`lattices.py:5583`), `discriminant_projection` (`lattices.py:5588`),
  `saturation` (`lattices.py:2990`), `is_primitive` (`lattices.py:8379`,
  `module_morphisms.py:1665`) with `is_saturated := is_primitive` (`module_morphisms.py:1671`)
  -- and the calls that express the cusps are written out, unexecuted, in
  `writing/coble/scripts/certificates/cusps_degree_two.sage`.
  The numbered-root Gram data is settled, and the four cusp boundary lattices are computed on
  the maintained baseline from it: each has rank 17, signature (0,17), is even, has determinant
  -2 and discriminant module Z/2, with label index k = 3, 2, 1, 2.  The glue, settled through the marked inclusion rather than through isometry.  The label's
  roots are pushed through P -> Q and the reduction of the plane, and the sublattice S of
  J^perp/J that their images span is recorded with its inclusion, index and gluing subgroup:
  A_17 gives S of determinant -18 and index 3 with glue Z/3; D_10 + E_7 gives index 2 and glue
  Z/2; E_8^2 + A_1 gives index 1 and trivial glue, i.e. the label is the boundary; D_16 + A_1
  gives index 2 and glue Z/2.  So nothing here waits on an invariant that could distinguish
  isometric candidates -- that formulation was withdrawn -- and the marked data is complete for
  all four rows.
  The library targets the research image's Sage development baseline on Python 3.14. It was not
  run on this container's Sage 10.8 / Python 3.12, which is not a supported host: nothing about
  the library is thereby in question, and provisioning an environment, or changing the library,
  belongs to the `sage` and `sage-extensions` projects rather than to this one. Until those
  calls are run on the supported baseline, no result of them is verified -- and in particular
  nothing in `writing/coble/scripts/certificates/two_elementary_checks.py` counts as verified,
  since it reimplements quotient, saturation and discriminant-group arithmetic in plain
  integers instead of going through the library. The same caution applies term by term to the
  nine items below. What the seven-item list is for is the analogue of the
  $d=1$ construction, where the four boundary lattices arise from $E_7$-complements in Niemeier
  lattices — and even there the bookkeeping is not uniform: at the level of root systems only
  three of the four come from an $E_7$ subdiagram (see [[450-scattone|Scattone boundary
  analysis]]), the fourth needing an embedding that is not a root subsystem. So the
  degree-$4$ case is incomplete, and the bound on what is missing is not a list but the
  construction itself.

  The note observes that the complements can be recovered by running Vinberg's algorithm
  on $\langle -4 \rangle \oplus U \oplus E_8^{2}$, and that the resulting
  Coxeter diagram matches Scattone 1987, Figure 6.3.1, while differing from the
  one for $(18,2,0)$ in AET. Whether the thesis wants the degree 4 case is a
  completeness decision, not a loss: the content is in Scattone.

## Structure

- The submitted LaTeX had four subsection headings in Part II that the Markdown never had, so this is a long-standing divergence, not a regression.
  Part II now opens with framing prose like the other two, but those four headings are still absent.

## Notes on the move

- Citation keys were remapped to the live Zotero library, so a key in the text now matches the Better BibTeX key of the item.
  Two of them changed meaning: Zotero has `Sha81` for Shah's degree 4 K3 paper and `Sha81a` for his Enriques paper, which is the opposite of the old local bibliography, and the text was swapped to match Zotero.
  Worth spot-checking the two citation sites.

- `[@Alexeev]` appears twice inside HTML comments in [[000-ksba|the KSBA chapter]]. It resolves to nothing, but the comments are invisible to the build, so nothing is broken.

## Settled since this list was written

Each of these was open when this list was written and is settled now; the two that appeared above have been removed from it.
The check is the one each item names, run over `sections/`.

- **Five targets with no label.** The text no longer uses `\Cref` at all; every cross-reference is written `@label`, and each of those names a label `sections/` declares.
  The five were:

  | target | was referenced from |
  | --- | --- |
  | <code>def:<wbr>hyperbolic-plane</code> | intro, the K3 and Enriques lattices |
  | <code>ex:<wbr>root-lattices</code> | intro, the K3 and Enriques lattices |
  | <code>thm:<wbr>complete-classification-0-cusps-fen2</code> | part III, main theorem statement |
  | <code>lem:<wbr>fent-semitoroidal-semifans-at-cusps</code> | part III, main theorem statement |
  | <code>thm:<wbr>five-semifans</code> | chapter 7, five cusps |

  The first two were referenced by the LaTeX too, so they predate the move.

- **The appendix's $D_n$ entry.** It now reads "We take $D_n$ to mean $D_n(-1)$, and identify the Coxeter diagram as:" and carries the $\dynkin$ diagram, so nothing stops mid-word.

- **Three `\todo` markers.** The lattice-classification and five-cusps markers are gone; the Scattone one remains, and is the only item under "Unfinished text".

- **The two 2-adic displays.** $V_k$ and $U_k$ are both written over $\ZZtwoadic$, so the neighbouring displays agree.

- **The toroidal boundary paragraph.** It now attributes $\signature$ and $\rank$ to the boundary lattice $\bar T_I$ rather than to the isotropic sublattice $I$.

- **Every statement block has a proof block.** The twenty-nine theorem, lemma, proposition and corollary blocks that had none now carry one, in the form the book's chapters use: a short derivation where the statement follows from the definitions on the page, and a one- or two-sentence citing block where it is quoted from the literature. Nothing was padded and no statement was weakened to make a proof easier.

  Three of them were not proofs waiting to be written but claims of a different status, and are now labelled as such. The Noether--Lefschetz non-normality discussion is a remark whose three mechanisms are recorded as observed rather than proved, and its second item no longer asserts that a non-snc intersection of divisors makes a variety non-normal, which is false. The determination of the KSBA limit by its dual complex is a conjecture, and it now says which direction is established (from the divisor model to the data) and that neither properness of the KSBA functor nor the invariance of dual complexes supplies the other. Zariski's Main Theorem is stated in the finite form — a finite birational morphism onto a normal variety is an isomorphism — and proved by integral closure, because that is the case the classifying map uses and the previous list of four hypotheses included normality of the source and properness of the target, neither of which appears in any form of the theorem. The quasi-finite form, which concludes only an open immersion, is recorded with it as the classical statement and is cited at [@Har10a, §V.5]; `Har77` and `Mum70` were the citations before, and neither carries the theorem in this bibliography, the `Mum70` entry being *Varieties defined by quadratic equations*.

- **Six Nikulin citations.** The tree cited `@Nik79` for Witt's analogue, the surjectivity of $\Orth(T)\to\Orth(q_T)$, and the discriminant theory. In the shared bibliography `Nik79` is *Finite groups of automorphisms of Kählerian K3 surfaces*; those results are in *Integral symmetric bilinear forms and some of their applications*, which is `Nik80`. The six sites now cite `@Nik80`, and `@Nik79` is left to the automorphism paper, which the research statement uses it for.

- **The one numeric citation.** The recognition statement in the divisor-models chapter cited `[6, Sec. 5C]`; it cites `[@AEGS25, §5C]`, which is the key the rest of the chapter uses for the same work.

- **Two references in the notation paragraph of the K3 chapter.** It cited `@def:root-lattice` and `@def:weyl-group`; the tree declares neither, and the paragraph states each symbol it introduces, so the parenthetical is gone rather than pointing at nothing.
  The root lattices themselves are presented in [[200-examples|Lattice examples]], which declares no label for them.
