# Mathematical taste and method

Suppose an involution of a surface induces an isometry $F$ of a lattice $L$.
The identity $\operatorname{Fix}(F)=\ker(F-I)$ needs little explanation.
The real work is to identify the operator $F$ and prove that its fixed lattice answers the geometric question.
In discussing this example, the researcher explicitly preferred symbolic methods when a computation is to enter a proof. Derive $F$ from the geometric action and establish that the classes sought are exactly the classes it fixes. Code can then compute the kernel over $\mathbb Z$ or check a proposed basis. If the geometric identification is conjectural, the calculation supplies a candidate lattice. The familiar kernel identity needs no separate citation. The identification needs its own argument or a source that proves it for this action. [Invariant and coinvariant lattices](../writing/lattice-theory/invariant-and-coinvariant-lattices.md)

## Which problems are interesting?

One recurring question in this research is what becomes computable when the same object is described in a different way. In the Coble programme, a geometric degeneration suggests a boundary stratum. On the period side, primitive isotropic lines and planes give arithmetic orbit problems. The interesting steps are to determine which degenerations map to which cusps, what geometric data the map retains, and how to recognize when two inputs give the same orbit. For example, to count boundary strata by counting orbits, one needs to know the fibers of the map from the strata to the orbit set. [Research statement](../writing/research-statement/ResearchStatement.md) · [Cusp correspondence](../writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md)

The same distinction arises in stable homotopy. An identification of the stable homotopy groups of spheres with homotopy groups of the spaces in an $\Omega$-spectrum suggests a computation. To pursue it, one needs information about those spaces obtained independently of the stable groups one hopes to calculate. Substituting a known value across the identification answers a lookup question. The research question is what the geometry of the new presentation lets one calculate.

A small example is especially useful when it preserves the operation that is hard to understand. To study successive foldings of high-dimensional hyperbolic chambers, seek a low-rank instance in which the mirrors, chambers, and their images can all be drawn in the hyperbolic plane. The point of the drawing is to follow a chamber through both foldings. For a proposed local-to-global method of counting lattice orbits, choose a case with an independently known answer. Compute the local orbits, account for their global assembly, and then compare the count. Using the known count to decide which cases to enumerate defeats the experiment.

Geometric intuition can test a proposed definition. When the researcher asked what a categorical tangent construction recovers on a smooth manifold, the intended comparison was with the velocity of a curve through a point. A differential takes that velocity as input. Which role does the proposed object play? For an affine $k$-scheme $\operatorname{Spec} A$, a tangent vector at a $k$-point $x$ gives a map from $\operatorname{Spec}(k[\epsilon]/(\epsilon^2))$ to the scheme. On algebras the arrow is $A\to k[\epsilon]/(\epsilon^2)$ and reduces to $x\colon A\to k$. Writing both arrows shows exactly where the direction changes. [Calculus on schemes](../writing/calculus-on-schemes.md)

## Simplicity and naturality

The intended use determines the simplest satisfactory answer. A classification of integral lattices of rank two for use in algebraic geometry should let the reader recognize a lattice up to isometry. Named families, their distinguishing invariants, and explicit lists at small values are useful in that role. A comparison with Nikulin's classifications can specify this desired form of answer without invoking one of his theorems in rank two. For the different question of whether a given rational isometry preserves an integral lattice, writing its matrix in an integral basis can settle the question immediately.

Naturality matters because it explains where structure comes from. For an integral lattice $L$ with nondegenerate pairing, write $L^\#$ for its dual lattice in $L\otimes\mathbb Q$. The module quotient $L^\#/L$ gives the underlying discriminant group. A question about the discriminant *pairing* asks more. How does the original pairing induce the new one, why does its value group change to $\mathbb Q/\mathbb Z$, and in what category can the quotient carry this data as part of the construction?

An explicit choice can be equally useful. In a computation with an absolute Galois group, fixing a separable closure and the embeddings one needs can make particular elements accessible. What matters is being able to tell which part of the answer depends on the choice.

## Precision where it changes the mathematics

The object named in the question determines what an answer must construct. In asking for the Coble moduli functor, the researcher asked what constitutes a family over a test scheme $T$, what its isomorphisms are, and how it pulls back along $T'\to T$. A period description raises a further question about the map from that functor to a period space. Likewise, a characterization of quotient morphisms should use structure available in the stated category. Subtracting points to decide which of them to identify already fails for topological spaces. Invoking $X/A$ in the definition of the quotient assumes the construction the question asks for.

Consider evaluation of maps from $A$ to $B$. Fixing a source point $a$ gives evaluation at $a$. Fixing a target point $b$ as well lets one take its fiber over $b$. With $b$ fixed and $a$ variable, the data include the source point itself. Writing down which points are parameters and which are fixed resolves an ambiguity about the object being constructed. Reusing the same symbol for the different maps would hide it.

In the discussion of plane models of Coble surfaces, calling a forgetful map “ambiguous” left the mathematical question undecided. Asking where a rational map is defined calls for its domain of definition. Asking which plane models give the same abstract surface calls for the fiber over that surface. Specifying the fiber already makes the second question precise. Qualifications about finiteness or étaleness introduce new questions and can obscure the one the reader is trying to answer. [A forgetful map for nodal plane sextics](../writing/coble/coble-surfaces/rational-sextic-calculations.md)

Once a distinction is settled, let the notation carry it. In a K3 period calculation, specify the cycles, the holomorphic form being integrated, and the marking used to express the period line in the complexification of a fixed lattice. One can then work with periods in those coordinates. Reintroducing the duality identifications at every step makes the dependence on the marking harder to see. [Periods and monodromy](../writing/coble/lattices-and-moduli/k3-periods-and-monodromy.md)

## What an argument establishes

For a rational plane sextic, the genus formula constrains the sum of the local singularity invariants. A proposed configuration that satisfies the sum passes a numerical test. Existence calls for a curve realizing that configuration or a theorem that applies to it. The same care applies when reading a paper. A mention of a possible geometric invariant theory (GIT) construction, an explicit quotient construction, and a proof identifying the quotient with a moduli space support different claims. Cite the passage that supplies the step being used. [Rational sextic calculations](../writing/coble/coble-surfaces/rational-sextic-calculations.md)

A negative conclusion needs evidence with the same scope as the conclusion. A failed computation can exhibit the step at which a proposed method breaks down. A literature search can establish what was found in the works searched. An impossibility claim requires an obstruction that applies to every case it excludes.

When the researcher asked whether a proposed interval object has the required universal property, the appropriate response was to test that property. Describing the question as advocacy attributed a position the question left open. A prediction that a route is unlikely to help can also close an inquiry prematurely. In the sphere-spectrum example, passing to a more complicated space might make a particular homotopy group easier to compute. Assessing that possibility calls for identifying a calculation the new presentation permits and seeing how far it goes.

Partial progress on a proof can be judged by the step it settles. Consider the claim that $v^\perp/\mathbb Z v$ is a nondegenerate lattice for a nonzero isotropic vector $v$ in a nondegenerate integral lattice. If $v=2e$ with $e$ primitive, then the class of $e$ has order two in the quotient. This identifies the missing primitivity hypothesis. For primitive $v$, proving freeness settles one part of the repaired claim. Nondegeneracy of the induced pairing is a separate proof obligation.

## How far does a correction extend?

A correction applies wherever the argument used the disputed inference. For compactifications attached to semifans, refinement gives a map from the finer compactification to the coarser one. If a refinement was read backwards, this determines which arrow to reverse. The direction of the next arrow in the diagram requires its own refinement relation. [Morphisms from refinements](../writing/coble/compactifications/toroidal-and-semitoroidal.md)

An inconsistency between formulas can require a wider correction. Let $L$ be a lattice with pairing $b$ and let $c$ be a nonzero rational scalar. On $cL\subset L\otimes\mathbb Q$, the extended pairing satisfies $b(cx,cy)=c^2 b(x,y)$. On $L$ with its pairing rescaled by $c$, the value is $c b(x,y)$. Thus multiplying the vectors by $1/2$ pulls the pairing back to $b/4$ on $L$. A purported identification of a dual lattice that uses $b/2$ at this step must be recomputed, along with every isometry deduced from it.

## How much detail belongs in the answer?

A reader using a classification needs to find the relevant family and distinguish it from its neighbors. A student using a model solution needs to see the equational steps. A researcher consulting a formula sheet needs hypotheses and formulas close enough to use together. In a correction to a proof, the reader already has the settled steps. Give the detail that lets them carry out the next mathematical operation.

These examples draw on the researcher's questions and corrections in the local GPT web archive through November 2026. The preference for symbolic computations in proofs, the treatment of choices in an absolute Galois group, and the objections to attributing a position or discouraging an untested idea were explicit. The account of what makes a problem interesting is an inference from the questions pursued about Coble degenerations, lattice orbits, and stable homotopy.
