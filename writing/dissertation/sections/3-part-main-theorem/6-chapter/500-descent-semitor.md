### Descent of Semitoroidal Data {#section-7-5}

Let $B \subset \cpt{\fttz}$ be the closure of the image of $\fent$ under the period morphism. Following the proof of [@AEGS25, Thm. 5.9], we pass to the normalization $\normalize{B}$: it extends the normalization of the open period image, carries the pulled-back family of stable Enriques pairs, and is the space on which the ambient ramification semifan restricts to the semitoroidal data for $\fent$. No local classification of the possible causes of non-normality of $B$ is needed for this construction.

:::{.proposition
    title="Normalization and Pullback Family"
    #prop:normalization-pullback-family
}
Let $\nu: \normalize{B} \to B$ be the normalization of $B$. Then:

- $\normalize{B}$ is a normal projective variety,

- The morphism $\nu$ is finite, surjective, birational, and proper,

- The pullback family $\nu^*(\mcz, \epsilon \mcr_Z)$ is a family of KSBA-stable Enriques pairs of degree two over the normal base $\normalize{B}$.
:::

:::{.proof}
The variety $B$ is projective over $\CC$. Its normalization is therefore finite and projective, and is normal by construction [@stacks-0BXR]. Pulling back the stable family along the finite morphism $\nu$ preserves the fiberwise KSBA-stability conditions, giving the stated family on $\normalize{B}$.
:::


:::{.theorem
    title="Universal Family and Moduli Classification"
    #thm:universal-family-moduli
}
The pulled-back family

\begin{align*}
(\mcz^\nu, \epsilon \mcr_Z^\nu) := \nu^*(\mcz, \epsilon \mcr_Z) \to \normalize{B}
.\end{align*}

satisfies:

- Every fiber is a KSBA-stable Enriques pair of degree two,
- It extends the universal family on the open moduli space $\fent$,
- There exists a canonical classifying morphism $\phi: \normalize{B} \to \cpt{\fent}$ compatible with the moduli functor.
:::

:::{.proof}
This is the family construction in the proof of [@AEGS25, Thm. 5.9]. Pull back the universal family of KSBA-stable K3 pairs from the ambient compactified K3 moduli space to $B$. On the general fiber the K3 surface carries the Enriques involution, and uniqueness of KSBA-stable limits extends this involution across the family. Taking its quotient produces a family of stable Enriques pairs extending the universal family on the open locus $\fent$. By [@AEGS25, Lem. 2.8], $\normalize{B}$ compactifies that open moduli space; after pulling the quotient family back to $\normalize{B}$, the resulting universal family defines the classifying morphism $\phi\colon\normalize{B}\to\cpt{\fent}$.
:::

:::{.proposition
    title="Restriction of Semifans and Semitoroidal Compactification"
    #prop:restriction-semifans
}
The embedding $B \hookrightarrow \cpt{\fttz}$ induces on $\normalize{B}$ a semitoroidal structure as follows:

- The period domain $\halfpd{B}$ for $\normalize{B}$ embeds as a closed linear subdomain of the period domain for $\fttz$, determined by additional constraints imposed by symmetry under the involution,
- The rational polyhedral cones from the ramification semifan $\semifan{F}_{\ram}$ on $\cpt{\fttz}$ restrict to produce a semifan $\semifan{F}_B$ on $\normalize{B}$,
- The normalization $\normalize{B}$ is isomorphic, as a modular compactification, to the semitoroidal compactification associated to $\semifan{F}_B$.
:::

:::{.proof}
This is the semitoroidal restriction used in the proof of [@AEGS25, Thm. 5.9]. By [@AEGS25, Lem. 2.8], the open Enriques period space is the normalization of its image in $\fttz$, so normalizing its closure gives a compactification of that open space. On the period-domain side, the Enriques locus is cut out by the invariant lattice condition, and the ambient ramification semifan induces a semifan on this subdomain by restriction. The proof of [@AEGS25, Thm. 5.9] identifies $\normalize{B}$ with the resulting semitoroidal compactification; this induced semifan is the $\semifan{F}_B$ above.
:::

:::{.construction
    title="Folded Semifans and Complete Boundary Stratification"
    #const:folded-semifans
}
The classifying morphism $\phi: \normalize{B} \to \cpt{\fent}$ transports the combinatorial structure of $\semifan{F}_B$ to the boundary stratification on $\cpt{\fent}$.
By [@AEGS25, Thm. 5.9], the normalization $\normksbacpt{\fent}$ is the semitoroidal compactification associated to the collection $\semifans{F}=\{\semifan{F}_k\}_{k=1}^5$ of Section 5.2, one semifan for each $0$-cusp of $\fent$.
By [@AEGS25, Lem. 5.5], each $\semifan{F}_k$ is the generalized Coxeter semifan of the corresponding folded Coxeter diagram, with the irrelevant folded roots omitted. Equivalently, it is obtained from the folded Coxeter fan by removing the faces cut out entirely by irrelevant roots.
The resulting boundary structure is as follows:

- $\semifan{F}_2$ and $\semifan{F}_4$ are fans because their irrelevant reflection subgroups are finite [@AEGS25, Lem. 5.6].
- $\semifan{F}_1$, $\semifan{F}_3$, and $\semifan{F}_5$ are not fans: their irrelevant reflection subgroups are infinite and their fundamental cones have infinitely many generators [@AEGS25, Lem. 5.6].
- The compactification is toroidal over the $0$-cusps $2$ and $4$, over every $1$-cusp adjacent to them, and also over $1$-cusp $35$; it is strictly semitoroidal over the remaining cusps [@AEGS25, Lem. 5.7].
:::

:::{.proposition
    title="Properties of the Classifying Morphism"
    #prop:properties-classifying
}
The classifying morphism $\phi : \normalize{B} \to \cpt{\fent}$ has the following properties:

- $\phi$ restricts over the interior to the classifying identification of the open moduli space $\fent$, and hence is birational;
- $\phi$ is proper.
:::

:::{.proof}
The family on $\normalize{B}$ restricts over the open locus to the universal family of degree-two numerically polarized Enriques surfaces, so its classifying morphism agrees there with the open moduli identification; this gives birationality. The source $\normalize{B}$ is proper over $\CC$, while the KSBA moduli stack is separated, so the classifying morphism is proper. These are the properties available before the finiteness argument in the proof of [@AEGS25, Thm. 5.9]; equality of the boundary stratifications is a consequence of the subsequent no-coarsening argument, not an input here.
:::
