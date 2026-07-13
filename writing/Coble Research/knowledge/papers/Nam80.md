---
title: Lecture Notes in Mathematics
authors: []
year: ''
bibkey: Nam80
tags:
- paper
- extraction
abstract: |
  theory of bounded symmetric domains 113
  (with explicit description in the case of Siegel upperhalf plane).
  I.
  The structure of bounded symmetric domains.
  113
  A) Definition and realizations.
  113
  B) The structure of roots of G.
  119
  
  VIII
  
  C) The description of $\mathcal{D}$ in $\pi_{+}$ via the Harish-Chandra embedding.
  
  II.
  Boundary components.
  128
  
  A) Boundary components.
  128
  B) The normalizer of a boundary component.
  134
  C) The structure of $\mathbf{N}(\mathbf{F})$ 136
  D) The natural projection $\pi_{\mathbb{P}}: \mathcal{D} \to \mathbb{F}$ .
  140
  E) Rational boundary components.
  143
  
  III.
  Realization of $\mathcal{D}$ as a Siegel domain of the third kind.
  144
  
  A) The self-adjoint cone $C(F)$ in $U(F)$ .
  144
  B) Realization of $\mathcal{D}$ as a Siegel domain.
  145
  C) Relation of the normalizers of adjacent boundary components.
  152
  
  Bibliography.
  153
  
  List of notations.
  156
  
  Index. 161
  
  §1.
  The Siegel upperhalf plane and the symplectic group.
  
  We first define two notions which are the main objects studied in this section.
  They are meaningful generalizations of the usual upper half plane $H = \{\tau \in \mathfrak{C} ; \text{Im } \tau &gt; 0\}$ and the linear fractional transformation group $\text{SL}(2, \mathbb{Z})$ acting on $H$.
  
  **Definition (1.1).** The complex domain
  
  $$
  \mathcal{G}_g = \{\tau \in M(g, \mathfrak{C}) ; \tau = \tau, \text{Im } \tau &gt; 0\}
  $$
  
  is called the _Siegel upper half plane of degree $g$._
  
  **Definition (1.2).** The subgroup of $\text{GL}(2g, \mathbb{R})$ defined as
  
  $$
  \begin{aligned}
  G &amp;= \{M \in M(2g, \mathbb{R}) ; \quad \tau_M \begin{pmatrix} 0 &amp; 1_g \\ -1_g &amp; 0 \end{pmatrix} M = \begin{pmatrix} 0 &amp; 1_g \\ -1_g &amp; 0 \end{pmatrix} \} \\
  &amp;= \{M = \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} ; \quad \tau_{AC} = \tau_{CA}, \quad \tau_{BD} = \tau_{DB}, \quad \tau_{AD} - \tau_{CB} = 1_g \} \\
  &amp;= \{M = \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} ; \quad M^{-1} = \begin{pmatrix} \tau_D - \tau_B \\ -\tau_C &amp; \tau_A \end{pmatrix} \}
  \end{aligned}
  $$
  
  is called the (real) _symplectic group_ (of degree $g$) and denoted by $\text{Sp}(g, \mathbb{R})$.
  (Some denote it by $\text{Sp}(2g, \mathbb{R})$.)
  
  **Remark (1.3).** In general, for a non-degenerate skew-symmetric bilinear form $A$ of degree $2g$, we can define
  
  $$
  \text{Sp}(A, \mathbb{R}) = \{M \in M(2g, \mathbb{R}) ; \quad \tau_{MAM} = A\}.
  $$
  
  However, these groups, called _paramodular groups_, are conjugate to each other in $\text{GL}(2g, \mathbb{R})$ hence isomorphic, for there is an element
  
  $$
  T \quad \text{in} \quad \text{GL}(2g, \mathbb{R}) \quad \text{with} \quad \tau_{TAT} = \begin{pmatrix} 0 &amp; 1_g \\ -1_g &amp; 0 \end{pmatrix}, \quad \text{then}
  $$
  
  $$
  \begin{array}{c c c}
  \text{Sp}(A, \mathbb{R}) &amp; \xrightarrow{\sim} &amp; \text{Sp}(g, \mathbb{R}) \\
  \downarrow &amp; &amp; \downarrow \\
  M &amp; \longrightarrow &amp; T^{-1}MT.
  \end{array}
  $$
  
  We shall now exhibit fundamental properties of the Siegel upper-
  
  2
  
  half plane and the symplectic groups.
  We restrict ourselves only in stating results we need later.
  Much more beautiful and stimulating exposition on these subjects is [31].
  
  **Proposition (1.4).**
  i) G acts on $\mathcal{G}_g$ biholomorphically as
  
  $$
  M = \left( \begin{array}{cc} A &amp; B \\ C &amp; D \end{array} \right) : \tau \to M \cdot \tau = (A\tau + B)(C\tau + D)^{-1}.
  $$
  
  ii) G acts on $\mathcal{G}_g$ transitively.
  
  **Remark (1.5).**
  Actually all biholomorphic automorphisms of $\mathcal{G}_g$ are expressed in this form.
  Namely
  
  $$
  \operatorname{Aut}(\mathcal{G}_g) = \operatorname{Sp}(g, \mathbb{R}) / \pm 1
  $$
  
  (cf.
  (1.6)).
  Note that $\{\pm 1\}$ is the center of $\operatorname{Sp}(g, \mathbb{R})$ and the quotient is a simple group.
  
  **Proof of (1.4).**
  i) First we note the following two equalities:
  a) $t(A\tau + B)(C\tau + D) - t(C\tau + D)(A\tau + B) = 0$
  b) $t(A\tau + B)(\overline{C\tau + D}) - t(C\tau + D)(\overline{A\tau + B}) = 2\sqrt{-1} \operatorname{Im} \tau.$
  
  We shall prove the second equality.
  
  $$
  \begin{aligned}
  \text{left side} &amp;= (\tau^t A + t B)(C\tau + D) - (\tau^t C + t D)(A\tau + B) \\
  &amp;= \tau^t AC\tau + t B C\tau + \tau^t AD + t BD - \tau^t CA\tau - t DA\tau - \tau^t CB - t DB \\
  &amp;= -\tau + \tau \quad \text{(cf. (1.2))}.
  \end{aligned}
  $$
  
  Next we show that $C\tau + D$ is invertible.
  If not, there is a non-zero vector $z \in \mathbb{C}^g$ such that $(C\tau + D)z = 0$.
  Then
  
  $$
  \begin{aligned}
  0 &amp;= t z^t (A\tau + B)(\overline{C\tau + D}) \overline{z} - t z^t (C\tau + D)(\overline{A\tau + B}) \overline{z} \\
  &amp;= 2\sqrt{-1} t z (\operatorname{Im} \tau) \overline{z} \quad \text{(by b)}),
  \end{aligned}
  $$
  
  which is impossible because $\operatorname{Im} \tau &gt; 0$.
  
  As the last step, it is shown that $\tau' = (A\tau + B)(C\tau + D)^{-1}$ is contained in $\mathcal{G}_g$.
  The proof, being elementary, is left to the reader.
  In order to show that $\tau'$ is symmetric and $\operatorname{Im} \tau' &gt; 0$ we use the equalities a) and b) respectively.
  
  ii) Write $\tau = x + \sqrt{-1} y$ with real $x, y$.
  There is a matrix $u \in GL(g, \mathbb{R})$ with $y = u^t u$.
  Then we have
  
  3
  
  $$
  \tau = \left( \begin{array}{cc} 1 &amp; x \\ 0 &amp; 1 \end{array} \right) \left( \begin{array}{cc} u &amp; 0 \\ 0 &amp; t_{u-1} \end{array} \right) (\sqrt{-1} \mathbf{l}_{g}).
  $$
  
  **Facts (1.6) (differential-geometric background).**
---

# Lecture Notes in Mathematics

Edited by A. Dold and B. Eckmann

812

Yukihiko Namikawa

Toroidal Compactification of Siegel Spaces

![img-0.jpeg](img-0.jpeg)

Springer-Verlag

Berlin Heidelberg New York 1980

# Author

Yukihiko Namikawa Department of Mathematics, Nagoya University Furocho, Chikusa-Ku Nagoya, 464/Japan

AMS Subject Classifications (1980): 14 L17, 20 G20, 32 J05, 32 M15, 32 N15

ISBN 3-540-10021-0 Springer-Verlag Berlin Heidelberg New York ISBN 0-387-10021-0 Springer-Verlag New York Heidelberg Berlin

This work is subject to copyright.
All rights are reserved, whether the whole or part of the material is concerned, specifically those of translation, reprinting, re-use of illustrations, broadcasting, reproduction by photocopying machine or similar means, and storage in data banks.
Under § 54 of the German Copyright Law where copies are made for other than private use, a fee is payable to the publisher, the amount of the fee to be determined by agreement with the publisher.

© by Springer-Verlag Berlin Heidelberg 1980 Printed in Germany Printing and binding: Beltz Offsetdruck, Hemsbach/Bergstr.
2141/3140-543210

To My Parents

Τίς ἄξιος ἀνοῖξαι το βιβλίον και λῦσαι τας σφραγῖδας αὐτοῦ.

Introduction

One of the simplest but the richest object to study in mathematics is a unit disc

$$
D = \{z \in \mathbb{C} ; |z| &lt; 1\}
$$

in the complex plane.
Among several generalizations of it the notion of hermitian bounded symmetric domain would be the most meaningful one, which is a generalization in the field of differential geometry (for full exposition see [13] for example).

As a generalization of $\operatorname{SL}(2, \mathbb{Z})$ acting on $D$ we have a notion of an arithmetic subgroup $\Gamma$ which is a discrete subgroup of the Lie group $G = \operatorname{Aut}(\mathcal{D})$ of biholomorphic automorphisms of a hermitian bounded symmetric domain $\mathcal{D}$.
The quotient space $\Gamma \backslash \mathcal{D}$ is naturally endowed with a structure of a normal complex analytic space.

Two facts stand in the way of studying the geometric structure of $\Gamma \backslash \mathcal{D}$.

The first is that $\Gamma$ may have fixed points in $\mathcal{D}$ which give rise to singularities on $\Gamma \backslash \mathcal{D}$.
This difficulty can be, however, overcome by taking a suitable subgroup $\Gamma'$ of $\Gamma$ of finite index which acts on $\mathcal{D}$ without fixed points.

The second is that $\Gamma \backslash \mathcal{D}$ may not be compact.
Here arises the problem to compactify $\Gamma \backslash \mathcal{D}$ suitably.
The first answer to this problem was given first by Satake [27] in the case of the Siegel upperhalf plane and finally by Baily-Borel [4] in the most general form.
The second answer was quite recently given by Mumford and others [2], suggested by the early work by Siegel [30] and Igusa [15].

The aim of this lecture note is to exhibit these theories of compactification of $\Gamma \backslash \mathcal{D}$ in the case of the Siegel upperhalf plane.
Thanks to this restriction one can see the whole theory elementarily and explicitly in this typical example, which would help the reader to understand the general theory developed in [2] written in complete but abstract form.
In this respect this book might be considered as an introduction to or supplement of [2]. On account of such expositive character of this book all proofs where one needs general theory (the latter half of Chap.V, Chap.VI-VII) are omitted but giving a suitable reference, mostly to [2] or [17].

The content is as follows.
In Chapter I we introduce the notion of the Siegel upperhalf plane, the symplectic group and its arithmetic

VI

subgroup and exhibit their fundamental properties.
Chapter II is devoted to the summary of main results concerning the problem of compactification.
In Chapter III we explained the idea of the toroidal compactification in the simplest case of $\Gamma \backslash D$ with the unit disc $D$ and $\Gamma = \operatorname{SL}(2, \mathbb{Z})$ . Two main tools are used for the construction of the compactification, the theory of bounded symmetric domain due to Korányi-Wolf [20] from differential geometry and the theory of torus embeddings due to Mumford [17] from algebraic geometry.
The former is exhibited in Chapter IV and V, and the latter in Chapter VI. More precisely, the notion of boundary component of $D$ and the structure of the associated parabolic subgroup in $G$ are given in Chapter IV and the realization of the domain as a Siegel domain of the third kind with a boundary component in the first half of Chapter V. Here we give complete proof for the case of Siegel upperhalf plane.
For the general case we refer the reader to [2] or [28] (the latter would be more readable).
The theory of torus embedding is given without proof in Chapter VI. The complete proof can be found in [17] or [24] except for an elementary construction of torus embedding given in (6.13). The latter half of Chapter V is devoted to the exposition of the Satake compactification.
After these preliminaries, in Chapter VII we construct Mumford's toroidal compactification and show fundamental properties of it, some of which are not explicitly stated in [2] though the proof is already contained there essentially.
In Chapter VIII we give some concrete examples of admissible decompositions which relate to the reduction theory of quadratic forms in our case.
In the last Chapter IX a particular decomposition, called the 2nd Voronoi decomposition, is treated and we show that the toroidal compactification associated with this decomposition admits an algebro-geometric interpretation of this compactification extending the fact that $\operatorname{Sp}(g, \mathbb{Z}) \backslash \mathfrak{S}_g$ can be considered as the coarse moduli space of principally polarised abelian varieties of dimension $g$ . As an appendix we sum up the abstract theory by giving explicit description in the case of the Siegel upperhalf plane with notations and the course of exposition being in accordance with those in [2] in order that the reader would see where the abstract procedure is going through.
There we indicate also a number of missprints in [2].

This note is based on the author's lecture at the Catholic University at Nijmegen in 1978. He would like to express his sincere gratitude to Prof. Looijenga and his colleagues at Nijmegen for their kind hospitality and encouragement, and to Mrs. Kozaki for her neat typing.

Table of Contents

§1. The Siegel upperhalf plane and the symplectic group.
1 §2. Main problem and main results.
7 §3. The case of g = 1. 11 §4. Boundary components and the structure of parabolic subgroups.
15 §5. Realization as a Siegel domain of the third kind, and 29 Satake compactification.
§6. Theory of torus embeddings.
39 §7. Toroidal compactification due to Mumford.
58 A) Construction of toroidal compactification.
58 B) Geometric properties of toroidal compactifications 70 (smoothness, projectivity, extension of holomorphic maps).
§8. Examples: reduction theory of positive quadratic forms.
85 §9. An application of the Voronoi compactification to 95 the theory of moduli of polarized abelian varieties.
A) 2nd Voronoi reduction theory.
95 B) Mixed decomposition of Ω² × V. 100 C) Compactification of the moduli space of polarized abelian varieties.
102 D) The extension of Torelli map.
110 Appendix: Abstract theory of bounded symmetric domains 113 (with explicit description in the case of Siegel upperhalf plane).
I. The structure of bounded symmetric domains.
113 A) Definition and realizations.
113 B) The structure of roots of G. 119

VIII

C) The description of $\mathcal{D}$ in $\pi_{+}$ via the Harish-Chandra embedding.

II. Boundary components.
128

A) Boundary components.
128 B) The normalizer of a boundary component.
134 C) The structure of $\mathbf{N}(\mathbf{F})$ 136 D) The natural projection $\pi_{\mathbb{P}}: \mathcal{D} \to \mathbb{F}$ . 140 E) Rational boundary components.
143

III. Realization of $\mathcal{D}$ as a Siegel domain of the third kind.
144

A) The self-adjoint cone $C(F)$ in $U(F)$ . 144 B) Realization of $\mathcal{D}$ as a Siegel domain.
145 C) Relation of the normalizers of adjacent boundary components.
152

Bibliography.
153

List of notations.
156

Index.
161

§1. The Siegel upperhalf plane and the symplectic group.

We first define two notions which are the main objects studied in this section.
They are meaningful generalizations of the usual upper half plane $H = \{\tau \in \mathfrak{C} ; \text{Im } \tau &gt; 0\}$ and the linear fractional transformation group $\text{SL}(2, \mathbb{Z})$ acting on $H$.

**Definition (1.1).** The complex domain

$$
\mathcal{G}_g = \{\tau \in M(g, \mathfrak{C}) ; \tau = \tau, \text{Im } \tau &gt; 0\}
$$

is called the *Siegel upper half plane of degree $g$.*

**Definition (1.2).** The subgroup of $\text{GL}(2g, \mathbb{R})$ defined as

$$
\begin{aligned}
G &amp;= \{M \in M(2g, \mathbb{R}) ; \quad \tau_M \begin{pmatrix} 0 &amp; 1_g \\ -1_g &amp; 0 \end{pmatrix} M = \begin{pmatrix} 0 &amp; 1_g \\ -1_g &amp; 0 \end{pmatrix} \} \\
&amp;= \{M = \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} ; \quad \tau_{AC} = \tau_{CA}, \quad \tau_{BD} = \tau_{DB}, \quad \tau_{AD} - \tau_{CB} = 1_g \} \\
&amp;= \{M = \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} ; \quad M^{-1} = \begin{pmatrix} \tau_D - \tau_B \\ -\tau_C &amp; \tau_A \end{pmatrix} \}
\end{aligned}
$$

is called the (real) *symplectic group* (of degree $g$) and denoted by $\text{Sp}(g, \mathbb{R})$.
(Some denote it by $\text{Sp}(2g, \mathbb{R})$.)

**Remark (1.3).** In general, for a non-degenerate skew-symmetric bilinear form $A$ of degree $2g$, we can define

$$
\text{Sp}(A, \mathbb{R}) = \{M \in M(2g, \mathbb{R}) ; \quad \tau_{MAM} = A\}.
$$

However, these groups, called *paramodular groups*, are conjugate to each other in $\text{GL}(2g, \mathbb{R})$ hence isomorphic, for there is an element

$$
T \quad \text{in} \quad \text{GL}(2g, \mathbb{R}) \quad \text{with} \quad \tau_{TAT} = \begin{pmatrix} 0 &amp; 1_g \\ -1_g &amp; 0 \end{pmatrix}, \quad \text{then}
$$

$$
\begin{array}{c c c}
\text{Sp}(A, \mathbb{R}) &amp; \xrightarrow{\sim} &amp; \text{Sp}(g, \mathbb{R}) \\
\downarrow &amp; &amp; \downarrow \\
M &amp; \longrightarrow &amp; T^{-1}MT.
\end{array}
$$

We shall now exhibit fundamental properties of the Siegel upper-

2

half plane and the symplectic groups.
We restrict ourselves only in stating results we need later.
Much more beautiful and stimulating exposition on these subjects is [31].

**Proposition (1.4).** i) G acts on $\mathcal{G}_g$ biholomorphically as

$$
M = \left( \begin{array}{cc} A &amp; B \\ C &amp; D \end{array} \right) : \tau \to M \cdot \tau = (A\tau + B)(C\tau + D)^{-1}.
$$

ii) G acts on $\mathcal{G}_g$ transitively.

**Remark (1.5).** Actually all biholomorphic automorphisms of $\mathcal{G}_g$ are expressed in this form.
Namely

$$
\operatorname{Aut}(\mathcal{G}_g) = \operatorname{Sp}(g, \mathbb{R}) / \pm 1
$$

(cf.
(1.6)). Note that $\{\pm 1\}$ is the center of $\operatorname{Sp}(g, \mathbb{R})$ and the quotient is a simple group.

**Proof of (1.4).** i) First we note the following two equalities: a) $t(A\tau + B)(C\tau + D) - t(C\tau + D)(A\tau + B) = 0$ b) $t(A\tau + B)(\overline{C\tau + D}) - t(C\tau + D)(\overline{A\tau + B}) = 2\sqrt{-1} \operatorname{Im} \tau.$

We shall prove the second equality.

$$
\begin{aligned}
\text{left side} &amp;= (\tau^t A + t B)(C\tau + D) - (\tau^t C + t D)(A\tau + B) \\
&amp;= \tau^t AC\tau + t B C\tau + \tau^t AD + t BD - \tau^t CA\tau - t DA\tau - \tau^t CB - t DB \\
&amp;= -\tau + \tau \quad \text{(cf. (1.2))}.
\end{aligned}
$$

Next we show that $C\tau + D$ is invertible.
If not, there is a non-zero vector $z \in \mathbb{C}^g$ such that $(C\tau + D)z = 0$.
Then

$$
\begin{aligned}
0 &amp;= t z^t (A\tau + B)(\overline{C\tau + D}) \overline{z} - t z^t (C\tau + D)(\overline{A\tau + B}) \overline{z} \\
&amp;= 2\sqrt{-1} t z (\operatorname{Im} \tau) \overline{z} \quad \text{(by b)}),
\end{aligned}
$$

which is impossible because $\operatorname{Im} \tau &gt; 0$.

As the last step, it is shown that $\tau' = (A\tau + B)(C\tau + D)^{-1}$ is contained in $\mathcal{G}_g$.
The proof, being elementary, is left to the reader.
In order to show that $\tau'$ is symmetric and $\operatorname{Im} \tau' &gt; 0$ we use the equalities a) and b) respectively.

ii) Write $\tau = x + \sqrt{-1} y$ with real $x, y$.
There is a matrix $u \in GL(g, \mathbb{R})$ with $y = u^t u$.
Then we have

3

$$
\tau = \left( \begin{array}{cc} 1 &amp; x \\ 0 &amp; 1 \end{array} \right) \left( \begin{array}{cc} u &amp; 0 \\ 0 &amp; t_{u-1} \end{array} \right) (\sqrt{-1} \mathbf{l}_{g}).
$$

**Facts (1.6) (differential-geometric background).**

1. $\operatorname{Iso}(\sqrt{-1} \mathbf{l}*{g}) := \{ M \in G; M \cdot (\sqrt{-1} \mathbf{l}*{g}) = \sqrt{-1} \mathbf{l}_{g} \}$

$$
= \{ \left( \begin{array}{cc} A &amp; B \\ -B &amp; A \end{array} \right) \in G \} \xrightarrow{\sim} U(g) = \{ A + \sqrt{-1} B \}
$$

(the unitary group).

Hence, as a real analytic manifold, $\mathcal{G}_{g}$ is a homogeneous space

$$
\mathcal{G}_{g} \cong \operatorname{Sp}(g, \mathbb{R}) / U(g).
$$

Here $\operatorname{Sp}(g, \mathbb{R}) / \pm 1$ is a simple Lie group and $U(g)$ is a maximal compact subgroup unique up to conjugate.

2. $\mathcal{G}_{g}$ is realized as a bounded domain by the Cayley transformation

$$
c: \mathcal{G}_{g} \xrightarrow{\sim} \mathcal{D}_{g} = \{ Z \in M(g, \mathbb{C}); \; t_{Z} = Z, \; t_{Z\overline{Z}} &lt; l_{g} \}
$$

$$
\tau \longrightarrow Z = (\tau - \sqrt{-1} \mathbf{l}_{g})(\tau + \sqrt{-1} \mathbf{l}_{g})^{-1}.
$$

$$
c^{-1}(Z) = \sqrt{-1}(Z + 1)(-Z + 1)^{-1}.
$$

The expression of $\mathcal{G}_{g}$ as (1.1) is then called an unbounded realization as a tube domain (cf.
4) below.

3. $\mathcal{G}_{g}$ is a symmetric space.
   Namely

$$
s = \left( \begin{array}{cc} 0 &amp; l_{g} \\ -l_{g} &amp; 0 \end{array} \right): \mathcal{G}_{g} \longrightarrow \mathcal{G}_{g} \quad \text{or} \quad \mathcal{D}_{g} \longrightarrow \mathcal{D}_{g}
$$

$$
\tau \longrightarrow -T^{-1} \quad Z \longrightarrow -Z
$$

is an involution ($s^2 = 1$) having $\sqrt{-1} \mathbf{l}*{g}$ (or 0) as an isolated fixed point.
Such $s$ is called a symmetry at $\sqrt{-1} \mathbf{l}*{g}$.
As $G$ acts transitively, every point of $\mathcal{G}_{g}$ has a symmetry.

4. $\mathcal{G}_{g}$ is a tube domain, i.e.

$$
\mathcal{G}_{g} = \mathcal{V}_{g} + \sqrt{-1} \mathcal{V}_{g}^{+}
$$

where

4

$$
\begin{array}{l}
\mathbf{y}_g = \{y \in M(g, \mathbb{R}) \mid y = y\}, \quad \text{the vector space of} \\
\quad \text{symmetric matrices}, \\
\mathbf{y}_g^+ = \{y \in \mathbf{y}_g \mid y &gt; 0\}, \quad \text{the cone of positive} \\
\quad \text{definite matrices}.
\end{array}
$$

The third main notion studied here is the following.

**Definition (1.7).** A subgroup $\Gamma$ of $G$ is called an *arithmetic subgroup* if

1. $\Gamma \subset G_{\mathbb{Q}} = \operatorname{Sp}(g, \mathbb{Q})$ and 1i) for a faithful rational representation $\rho : G_{\mathbb{Q}} \to GL(n, \mathbb{Q})$, $\rho(\Gamma)$ is commensurable with $\rho(G) \cap GL(n, \mathbb{Z})$.

**Example (1.8).**

1. $\Gamma = \operatorname{Sp}(g, \mathbb{Z}) \subset G$.
   We mainly consider this group.

1i) $\Gamma(\Delta) = \operatorname{Sp}(A, \mathbb{Z})$ for a 2g-matrix

$$
A = \left( \begin{array}{cc}
0 &amp; \Delta \\
-\Delta &amp; 0
\end{array} \right), \quad
\Delta = \left( \begin{array}{c}
d_1 \\
\cdots \\
d_g
\end{array} \right),
$$

where $d_i \in N$ with $d_i \mid d_{i+1}$ (cf.
(1.3)). $\Gamma(\Delta)$ is seen to be an arithmetic subgroup of $G$ by a monomorphism

$$
\begin{array}{l}
\Gamma(\Delta) = \operatorname{Sp}(A, \mathbb{Z}) \longrightarrow \operatorname{Sp}(g, \mathbb{Q}) \\
M^{\omega} \longrightarrow \left( \begin{array}{c}
1 \\
\Delta
\end{array} \right) M \left( \begin{array}{c}
1 \\
\Delta
\end{array} \right)^{-1}.
\end{array}
$$

Note that for an arbitrary nondegenerate skew-symmetric matrix $A$ there is an invertible integral $2g$ matrix $T \in GL(2g, \mathbb{Z})$ such that $T_{TAT}$ is as above.

1ii) $\Gamma(n) = \{M \in \operatorname{Sp}(g, \mathbb{Z}) \mid M \equiv l_{2g} \pmod{n}\}$.

This group is called the *principal congruence subgroup of Stufe $n$*.

1v) $\Gamma(\Delta)(n)$ is defined similarly.

**Proposition (1.9).** Any arithmetic subgroup $\Gamma$ of $G$ acts on $D = \mathbb{G}_g$ properly discontinuously, i.e. for $\forall \tau \in D$, $\exists U$ a neighbourhood of $\tau$ such that $\{M \in \Gamma \mid M \cdot U \cap U \neq \phi\}$ is a finite set (actually $\operatorname{Iso}(\tau) \cap \Gamma$ for a sufficiently small $U$).

This follows directly from (1.6) 1) and the following general fact.

5

## Lemma (1.9.1)

Let $X$ be a homogeneous space $G/K$ for a real Lie group $G$ and a compact subgroup $K$.
Then any discrete subgroup $\Gamma$ of $G$ acts on $X$ properly discontinuously.

The proof is elementary if we note the fact that the natural projection $G \to G/K$ is a proper map.

## Remark (1.10)

We know much stronger property on the action of arithmetic subgroups on a bounded symmetric domain, namely, the existence of a so-called fundamental domains, thanks to Borel *[11]* (in our particular case of $\mathcal{G}*g$ by Siegel *[31]*). In particular for any arithmetic subgroup the number of conjugacy classes of $\mathcal{U}*{\tau}$ (Iso$(\tau)$ $\cap$ $\Gamma$) is finite and a suitable subgroup $\Gamma'$ of $\Gamma$ of finite index acts on $\mathcal{D}$ even without fixed points.
For example $\Gamma(n)$, $n \geq 3$, acts on $\mathcal{G}_g$ without fixed points.

However, concrete description of fundamental domain is very difficult.
Only classical case of $g = 1$ is known.
Gauss obtained fundamental domains of $\Gamma(2)$ and $\Gamma(4)$ for $g = 1$ already in 1805 (*[10]* Vol.8). Siegel expressed a fundamental domain of $\Gamma = \operatorname{Sp}(g, \mathbb{Z})$ with a countable number of inequalities as follows (*[16]* Chap.V §4).

$$
F = \{\tau \in \mathcal{G}_g \mid i) \quad | \det(0 \tau + D) | \geq 1 \quad \text{for} \quad \forall \underset{0}{\overset{A}{C}} B \in \Gamma,
$$

$$
\begin{aligned}
&amp;\text{in } \tau = y = (y_{ij}) \text{ is Minkowski reduced,} \\
&amp;\text{i.e. } \tens{aya} \geq y_{kk}, \; 1 \leq k \leq g, \text{ for } \forall a \\
&amp;= \begin{pmatrix} a_1 \\ \vdots \\ a_g \end{pmatrix} \in \mathbb{Z}^g \quad \text{where } a_k, \dots, a_g \text{ are} \\
&amp;\text{relatively prime,}
\end{aligned}
$$

$$
\iff \quad -\frac{1}{2} \leq \operatorname{Re} \tau_{ij} \leq \frac{1}{2}.
$$

## Corollary (1.11)

Let $\Gamma$ be an arithmetic subgroup of $G$ acting on $\mathcal{D} = \mathcal{G}*g$.
Then the quotient space $\Gamma \backslash \mathcal{D}$ admits a canonical structure of a normal analytic space enjoying the universal property that a map $f: \Gamma \backslash \mathcal{D} \to X$ to an analytic space $X$ is holomorphic if and only if the composite $\mathrm{Top}: \mathcal{D} \to \Gamma \backslash \mathcal{D} \to X$ is holomorphic.
This follows from the theorem of Cartan (*[6]_) on the existence of the quotient analytic space for action of a finite group.

## Remark (1.12)

i) If $\Gamma$ acts on $\mathcal{D}$ without fixed points, then $\Gamma \backslash \mathcal{D}$ is a manifold.
Since a subgroup $\Gamma'$ of $\Gamma$ of a finite

6

index acts on $\mathcal{D}$ without fixed points, $\Gamma \backslash \mathcal{D}$ has only quotient singularities.

ii) It turns out that $\Gamma \backslash \mathcal{D}$ admits even the structure of a quasi-projective algebraic variety ([3] in our case of $\mathcal{D} = \mathbb{G}_{\mathbf{g}}$, and [4] in general).

A holomorphic function $f$ on $\mathcal{D}$ is called a *modular form of weight* $k$ if

$$
f(gz) = \left(\frac{dg}{dz}(z)\right)^k f(z)
$$

for all $g \in \Gamma$.
In the case of $\mathcal{D} = \mathbb{G}_g$ and $\Gamma \subset \operatorname{Sp}(g, \mathbb{R})$,

$$
\frac{dM}{d\tau} = \frac{1}{\det(C\tau + D)^2}
$$

for $\tau \in \mathbb{G}_g$ and $M = \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} \subset \operatorname{Sp}(g, \mathbb{R})$.
Let $A_k$ be the vector space of modular forms of weight $k$.
Then naturally

$$
A = \begin{cases} \Phi &amp; A_k \\ k &amp; \geq 0 \end{cases}
$$

has a structure of a graded ring.

The theory of modular forms says the following:

I) A is finitely generated.

II) For sufficiently large $k$, the meromorphic map

$$
\begin{array}{c}
\mathcal{D} \longrightarrow \mathbb{P}^N \\
\swarrow \quad \swarrow
\end{array}
$$

$$
z \bmod \Gamma \to (f_0(z) : f_1(z) : \dots : f_N(z))
$$

is holomorphic and an immersion, where $\{f_0, \dots, f_N\}$ is a basis of $A_k$.
In other words divisors defined by modular forms are ample.

III) If $\Gamma$ operates freely, then the divisor defined by $f = 0$ for $f \in A_k$ represents a $k$-times canonical divisor on $\Gamma \backslash \mathcal{D}$.
(This last statement is straightforward from the definition.)

iii) The space $\Gamma(\Delta) \backslash \mathbb{G}_g$ is of much importance in algebraic geometry since it is interpreted as the coarse moduli space of polarised abelian varieties of dimension $g$ with type of polarization $\Delta$ ([16]).

§2. Main problem and main results.

As we have seen in the previous section, the quotient space $\Gamma \backslash \mathcal{D}$ endowed with the canonical normal analytic structure is an important geometric object to study.
In studying, the main difficulty lies in the fact that this quotient space is not necessarily compact as is the case when $\Gamma = \operatorname{Sp}(g, \mathbb{Z})$.
Here arises our main problem.

**Problem (2.1).** Find a "good" compactification of $\Gamma \backslash \mathcal{D}$.

Of course it is obscure what "good" means.
It will be made precise in the course of the statement of main results in the following.

**1st Answer (2.2).** (Satake compactification or Baily-Borel compactification.)
([27], [4]. → §5)

This compactification $(\Gamma \backslash \mathcal{D})^{\gamma}$ is defined to be the quotient space $\Gamma \backslash (\mathcal{D}^{\mathfrak{I}})$ of the "rational" closure $\mathcal{D}^{\mathfrak{I}}$ of $\mathcal{D}$ in $\overline{\mathcal{D}}$ endowed with the Satake topology or the cylindrical topology.
(The latter topology, defined by Pjatečki-Šapiro, is different from the former.
But the quotient topology in $\Gamma \backslash (\mathcal{D}^{\mathfrak{I}})$ turns out to be homeomorphic [18].) (The symbol $\gamma$ and $\mathfrak{J}$, pronounced as "sa" and "yu" respectively, are the initials of "Satake" and "rational" in Japanese.
I prefer this notation because both letters contain bar "-" which usually stands for the "closure".)

A) "Good" properties.
i) It is projective and normal, and contains $\Gamma \backslash \mathcal{D}$ as a Zariski open subset.
ii) It has the following minimal property: let $D = \{z \in \mathbb{C} ; |z| &lt; 1\}$ and $D^* = \{z \in \mathbb{C} ; 0 &lt; |z| &lt; 1\}$ be the unit disc and the punctured disc respectively.
Then any holomorphic map

$$
f: D \times \cdots \times D \times D^* \times \cdots \times D^* \to \Gamma \backslash \mathcal{D}
$$

locally liftable to $\mathcal{D}$ extends to a holomorphic map

$$
\overline{f}: (D)^{m+n} \to (\Gamma \backslash \mathcal{D})^{\gamma}.
$$

Hence, in particular, for every nonsingular compactification $X$ of $\Gamma \backslash \mathcal{D}$ with normally crossing boundary there is a dominating holomorphic map $p: X \to (\Gamma \backslash \mathcal{D})^{\gamma}$ extending $\operatorname{id}: \Gamma \backslash \mathcal{D} \to \Gamma \backslash \mathcal{D}$ (Borel [5], Kobayashi and Ochiai [19]).

8

iii) The space of automorphic forms gives the projective embedding of $(\Gamma \backslash \mathcal{D})^{\gamma}$.
In other words we have

$$
(\Gamma \backslash \mathcal{D})^{\gamma} = \operatorname{Proj}\left( \begin{array}{c c} * &amp; * \\ k &amp; \geq 0 \end{array} A_{k} \right)
$$

(cf.
(1.12) ii)).

iv) For two arithmetic subgroups $\Gamma'$, $\Gamma$ with $\Gamma' \subset \Gamma$ and $[\Gamma : \Gamma'] &lt; \infty$, we have a canonical finite holomorphic map

$$
c: (\Gamma' \backslash \mathcal{D})^{\gamma} \longrightarrow (\Gamma \backslash \mathcal{D})^{\gamma}
$$

extending the natural finite map $\Gamma' \backslash \mathcal{D} \to \Gamma \backslash \mathcal{D}$.

B) Example.
For $\Gamma = \operatorname{Sp}(g, \mathbb{Z})$, $\mathbb{G}_g^* = \Gamma \backslash \mathbb{G}_g$,

$$
(\mathbb{G}_g^*)^{\gamma} = \mathbb{G}_g^* \coprod \mathbb{G}_{g-1}^* \coprod \cdots \coprod \mathbb{G}_1^* \coprod \mathbb{G}_0^*
$$

where $\mathbb{G}_0^*$ is understood to be the set of one point.

C) Bad property: in the case of $\mathcal{D} = \mathbb{G}_{\mathbf{g}}$ and $\Gamma = \operatorname{Sp}(\mathbf{g}, \mathbb{Z})$ etc. the boundary $(\Gamma \backslash \mathcal{D})^{\gamma} - (\Gamma \backslash \mathcal{D})$ has codimension $\mathbf{g}$ and there it has very complicated singularity.

Igusa studied the blowing up along the boundary.
For $\mathbf{g} \leq 3$ this procedure gives a resolution for $\Gamma(n)$, $n \geq 3$, but not for $\mathbf{g} \geq 4$ ([15]).

2nd Answer (2.3) (Mumford's toroidal compactification) ([2], $\rightarrow$ §7).

As is shown in the following this compactification $(\Gamma \backslash \mathcal{D})^{\gamma}$ complements the bad property of Satake compactification, and gives sometimes even nicer compactification to study.
(The symbol "$\gamma$", pronounced as "ma", is the initial of Mumford in Japanese.)
The main purpose of this lecture is to exhibit how to construct this toroidal compactification.

A) Good and bad properties: i) The boundary is of codimension 1.

ii) It is normal and has only finite quotients of toroidal singularities ($\rightarrow$ §6), hence Cohen-Macaulay (Hochster, [17] p.52).

iii) There is a bimeromorphic holomorphic map $p: (\Gamma \backslash \mathcal{D})^{\gamma} \to (\Gamma \backslash \mathcal{D})^{\gamma}$ extending the identity on $\Gamma \backslash \mathcal{D}$.

iv) An apparent disadvantage of this compactification consists in the property that it is not unique.
It is constructed by using additional data, "admissible cone decomposition".
We have however

9

nice criterion for smoothness, or projectivity of $(\Gamma \backslash \mathcal{D})^{\gamma}$ and the extendability of holomorphic maps as in (2.2) A) ii) ([2] Chap.4) in terms of geometric properties of decompositions.
By means of it we know that there exist nonsingular projective compactifications (up to finite quotient if $\Gamma$ operates with fixed points).
(In [2] one cannot find explicit proof of this important existence theorem.
See §7.)

v) For a subgroup $\Gamma'$ of $\Gamma$ we have a finite holomorphic map $(\Gamma' \backslash \mathcal{D})^{\gamma} \to (\Gamma \backslash \mathcal{D})^{\gamma}$ extending the canonical map $\Gamma' \backslash \mathcal{D} \to \Gamma \backslash \mathcal{D}$ (when an admissible decomposition is fixed).

B) Example: $\Gamma = \operatorname{Sp}(g, \mathbb{Z})$ (or $\Gamma(n)$). $(\rightarrow \S 8)$

Given $\Sigma = \{\sigma_{1}\}*{1\in \mathcal{I}}$, cone decomposition of $\overline{\Psi}*{g}^{+}$

s.t. i) $\sigma_{1} \subset \overline{\Psi}_{g}^{+}$, generated by a finite number of integral matrices;

ii) $\sigma_{1} &gt; \sigma'$ ($\sigma'$ is a face of $\sigma_{1}$) $\Rightarrow \sigma' \in \Sigma$;

iii) $\sigma_{1}, \sigma_{1}, \in \Sigma \Rightarrow \sigma_{1} \cap \sigma_{1}, \prec \sigma_{1}, \sigma_{1}$;

iv) $u \in GL(g, \mathbb{Z})$, $\sigma_{1} \in \Sigma \Rightarrow {}^t u \sigma_{1} u \in \Sigma$;

v) for $g' &lt; g$, with the inclusion

$$
\begin{array}{c}
\Psi_{g'} \longrightarrow \Psi_{g} \\
\downarrow \\
y' \longrightarrow \left( \begin{array}{cc}
0 &amp; 0 \\
0 &amp; y'
\end{array} \right),
\end{array}
$$

we have

$$
\begin{array}{l}
\underset{1 \in \mathcal{I}}{\cup} \sigma_{1} = \underset{u \in GL(g, \mathbb{Z})}{\cup} \mathrm{t}_{u}(\underset{g' \leq g}{\cup} \Psi_{g'}^{+}) u; \\
\text{vi) there are only a finite number of classes of } \sigma_{1} \\
\text{modulo } GL(g, \mathbb{Z}),
\end{array}
$$

then we can construct $(\Gamma \backslash \mathfrak{S}*g)^{\gamma}$ (defined by $\Sigma$) with a stratification $\{X*{\overline{1}} - \}_{\overline{1} \in \mathcal{I}}$ mod $GL(g, \mathbb{Z})$

s.t. i) $X_{\overline{1}} \subset \overline{X}*{\overline{1}}, \iff \exists*{1'}, 1' \mod GL(g, \mathbb{Z}) = \overline{1}'$ with $\sigma_{1} &gt; \sigma_{1}$;

ii) $\dim X_{\overline{1}} + \dim \sigma_{1} = \frac{1}{2} g(g + 1)$ ($= \dim \mathfrak{S}_g$);

iii) $\sigma_{1} = \{0\} \iff X_{\overline{1}} = \Gamma \backslash \mathfrak{S}_{g}$;

iv) $\exists_{1}, 1 \mod GL(g, \mathbb{Z}) = \overline{1}$ with $\sigma_{1} \subset \overline{\Psi}*{g}^{+}, \iff p(\overline{X}*{\overline{1}}) \supset \mathfrak{S}*{g}^{*}$, with $p: (\Gamma \backslash \mathfrak{S}*{g})^{\gamma} \to (\Gamma \backslash \mathfrak{S}_{g})^{\gamma}$ $(\rightarrow (2.2) \text{ B})$.

10

An explicit example of cone decomposition in the case of $\mathbf{g} = 2$ :

$$
\begin{array}{l}
\sigma_ {0} = \{0 \}, \\
\sigma_ {1} = \left\{\left( \begin{array}{cc} 0 &amp; 0 \\ 0 &amp; \lambda \end{array} \right); \lambda \geq 0 \right\}, \\
\sigma_ {2} = \left\{\left( \begin{array}{cc} \lambda_ {1} &amp; 0 \\ 0 &amp; \lambda_ {2} \end{array} \right); \lambda_ {1} \geq 0, \lambda_ {2} \geq 0 \right\}, \\
\sigma_ {3} = \left\{\left( \begin{array}{cc} \lambda_ {1} + \lambda_ {3} &amp; - \lambda_ {3} \\ - \lambda_ {3} &amp; \lambda_ {2} + \lambda_ {3} \end{array} \right); \lambda_ {1}, \lambda_ {2}, \lambda_ {3} \geq 0 \right\}. \\
\Sigma = \operatorname {G L} (2, \mathbb {Z}) \cdot \{\sigma_ {0}, \sigma_ {1}, \sigma_ {2}, \sigma_ {3} \}, \\
\Sigma \mod \operatorname {G L} (2, \mathbb {Z}) = \{\sigma_ {\overline {{0}}}, \sigma_ {\overline {{1}}}, \sigma_ {\overline {{\overline {{2}}}}}, \sigma_ {\overline {{3}}} \}.
\end{array}
$$

![img-1.jpeg](img-1.jpeg)

(2.4) We use two main tools in construction of $(\Gamma \backslash D)^{\overline{2}}$ :

1. realization of a domain as a Siegel domain of the third kind concerning (rational) boundary components (due to Korányi-Wolf [20]);
2. theory of torus embeddings (due to Mumford et al.).

Here we show the first theory in the case of $\mathcal{D} = \mathbf{G}_{\mathbf{g}}$ , where it can be obtained elementarily and explicitly ( $\rightarrow$ §5), and give an outline of the second theory without proof ( $\rightarrow$ §6).

§3. The case of g = 1.

(3.1) We shall explain in this section how to construct toroidal compactification in the simplest case:

$$
\mathcal {D} = \mathbb {G} _ {1} = H = \{\tau \in \mathbb {C}; \text {Im} \tau &gt; 0 \},
$$

$$
\Gamma = \operatorname {Sp} (1, \mathbb {Z}) = \operatorname {SL} (2, \mathbb {Z}) = \left\{\left( \begin{array}{l l} a &amp; b \\ c &amp; d \end{array} \right); a d - b c = 1 \right\}.
$$

The well-known j-function $j: H \to \mathbb{C}$ with $j(\sqrt{-1}) = 1$ , $j(\exp(\frac{2\pi\sqrt{-1}}{3})) = 0$ induces an isomorphism

$$
\tilde {\mathcal {J}}: \operatorname {SL} (2, \mathbb {Z}) \backslash H \xrightarrow {\sim} \mathbb {C}.
$$

(3.2) The only possible normal compactification of $\Gamma \backslash H$ is

$$
\left(\Gamma \backslash H\right) ^ {-} = \mathbb {P} _ {\mathbb {C}} ^ {1} = \mathbb {C} \perp \{\infty \}
$$

obtained by adding the point of infinity $\infty$ .

We try to construct this compactification from our point of view, in other words, to show how we can regard it as toroidal compactification.

(3.3) Step 1 (1st partial quotient).

Let

$$
B = \{\pm \left( \begin{array}{c c} 1 &amp; b \\ 0 &amp; 1 \end{array} \right); b \in \mathbb {Z} \}
$$

which is the parabolic subgroup fixing the boundary component $\{\infty\}$ .

The map

$$
\begin{array}{l}
\underline {{e}}: H \longrightarrow U ^ {*} = \{z \in \mathbb {C}; 0 &lt;   | z | &lt;   1 \} \\
\begin{array}{c c} \text {w} &amp; \text {w} \end{array} \\
\tau \longrightarrow \underline {{e}} (\tau) = \exp (2 \pi \sqrt {- 1} \tau) \\
\end{array}
$$

induces an isomorphism $\mathsf{B} \backslash H \xrightarrow{\sim} \mathsf{U}^*$ through which we identify both of them.

Note that the above $\underline{e}$ is a restriction of the map $\underline{e} : \mathbb{C} \to \mathbb{C}^* = \mathbb{C} - \{0\}$ defined similarly

$$
\begin{array}{c c c}
\underline {{e}}: \mathbb {C} &amp; \longrightarrow &amp; \mathbb {C} ^ {*} \\
\upsilon &amp; &amp; \upsilon \\
H &amp; \longrightarrow &amp; \mathrm {U} ^ {*}
\end{array}
$$

and the latter can be considered as the universal covering map of $\mathbb{C}^*$ with $B / \pm 1$ as the covering transformation group.
This interpretation is essential for generalization.

(3.4) Step 2 (partial compactification).

The map defined by taking the imaginary part

![img-2.jpeg](img-2.jpeg)

is factored with $\underline{\mathbf{e}}$ as

![img-3.jpeg](img-3.jpeg)

and we have $H = \operatorname{Im}^{-1}(\mathbb{R}_{+})$ .

We obtain $\mathbb{C}$ by adding $\{0\}$ to $\mathbb{C}^*$ , which can be regarded as the torus embedding associated with $\overline{\mathbb{R}}_+ = \{r \in \mathbb{R} : r \geq 0\}$ . Then we have

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

(3.5) Step 3 (2nd partial quotient).

This step is unnecessary in our case $(\rightarrow (7.10))$

# (3.6) Step 4 (Gluing).

First we note

Lemma (3.6.1). There is a positive constant $K$ (= 1 in fact) such that in $V_{K} = \{\tau ; \text{Im } \tau &gt; K\}$ , $\Gamma$ -equivalence and B-equivalence are the same, or equivalently, if for $\tau_{1}, \tau_{2} \in V_{K}$ , $\mathbb{H}M \in \Gamma$ with $M \cdot \tau_{1} = \tau_{2}$ , then $M \in B$ .

This can be seen at once from the well-known shape of a fundamental domain in $H$ with respect to $\operatorname{SL}(2, \mathbb{Z})$ .

![img-6.jpeg](img-6.jpeg)

If we put

$$
U _ {K} ^ {*} = \{z \in \mathbb {C} ^ {*}; 0 &lt;   | z | &lt;   e ^ {- 2 \pi K} \} = \underline {{e}} (V _ {K}),
$$

$$
U _ {K} = \left(\left(U _ {1} ^ {*}\right) ^ {-}\right) ^ {\circ} \quad \text {i n} \quad \mathbb {C} = U _ {K} ^ {*} \coprod \{0 \},
$$

$$
\overline {{V}} _ {K} = \mathrm {j} (V _ {K}),
$$

then the above lemma says that the map $\mathsf{U}*{\mathsf{K}}^{*} \to \overline{\mathsf{V}}*{\mathsf{K}}$ induced from the canonical map $\mathsf{U}^{*} \simeq \mathsf{B} \backslash \mathsf{H} \to \mathbb{C} \simeq \Gamma \backslash \mathsf{H}$ is an isomorphism.

![img-7.jpeg](img-7.jpeg)

Noting that $\mathsf{U}*{\mathsf{K}}$ is a neighbourhood of $\{0\}$ in $\mathsf{U}$ , we glue $\mathbb{C}$ and $\mathsf{U}*{\mathsf{K}}$ together by the above isomorphism $\mathsf{U}*{\mathsf{K}}^{\bullet} \supset \overline{\mathsf{V}}*{\mathsf{K}}$ to get the desired compactification

$$
\left(\Gamma \backslash H\right) ^ {\sim} = \mathbb {C} \cup U _ {K} = \mathbb {C} \coprod \{0 \} _ {U}.
$$

By definition, for a sequence $\{\tau_n\}$ in $H$

$$
\underline {{\mathbf {e}}} \left(\tau_ {n}\right)\rightarrow 0 &lt;   = &gt; \operatorname {I m} \tau_ {n} \rightarrow \infty ,
$$

and as is wellknown

$$
\operatorname {I m} \tau_ {n} \rightarrow \infty = &gt; j (\tau_ {n}) \rightarrow \infty ,
$$

hence $\{0\}_{U}$ can be interpreted as the point of infinity for $\mathbb{C}$ .

§ 4. Boundary components and the structure of parabolic subgroups.

(4.1) The Siegel upper half plane

$$
\Theta_g = \{ \tau \in M(g, \mathbb{C}) \ ; \ t_{\tau} = \tau, \ \text{Im} \ \tau &gt; 0 \}
$$

can be realized as a bounded domain

$$
\varrho_g = \{ Z \in M(g, \mathbb{C}) \ ; \ l_g - Z \overline{Z} &gt; 0 \}
$$

in $\Psi_{g,\mathbb{C}} = \{ \text{symmetric} \ \mathbb{C}\text{-matrices of degree} \ g \}$ by the Cayley transformation $Z = (\tau - \sqrt{-1} \l_g)(\tau + \sqrt{-1} \l_g)^{-1}$ ((1.6) 2)). This realization is a special case of Harish-Chandra realization ([2] p.170).

In the topological closure $\overline{\varrho}*g$ of $\varrho_g$ in $\Psi*{g,\mathbb{C}}$, we introduce an equivalence relation:

for $p, q \in \overline{\varrho}_g$, $p \sim q \iff \exists \xi_1: D = \{ z \in \mathbb{C} \ ; \ |z| &lt; 1 \} \to \overline{\varrho}*g$, $i = 1, \cdots, m$, holomorphic maps, such that $\xi_1(0) = p$, $\xi_m(0) = q$, and $\xi_1(D) \cap \xi*{i+1}(D) \neq \emptyset$.
Roughly speaking, $p \sim q$ if they can be connected by a finite number of holomorphic curves.

**Definition (4.2).** A maximal subset in $\overline{\varrho}_g$ of mutually equivalent points is called a *boundary component* of $\varrho_g$.

Hence $\overline{\varrho}_g$ is devided into a disjoint union of boundary components.

We know that the symplectic group $G$ acts on $\varrho_g$.
Hence it is natural to ask whether this action extends to the boundary.
We can answer this question affirmatively.

**Proposition (4.3).** The action of $G$ on $\varrho_g$ induced from the Cayley transformation

$$
\begin{aligned}
(*) \ M = \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} : Z \to \left( (A - \sqrt{-1}C)(Z + 1) + (B - \sqrt{-1}D)\sqrt{-1}(Z - 1) \right) \\
\times \left( (A + \sqrt{-1}C)(Z + 1) + (B + \sqrt{-1}D)\sqrt{-1}(Z - 1) \right)^{-1}
\end{aligned}
$$

extends to the closure of $\varrho_g$.

**Proof.** It suffices to prove that the matrix

$$
( A + \sqrt{-1}C)(Z + 1 ) + (B + \sqrt{-1}D)\sqrt{-1}(Z - 1)
$$

16

is invertible for $Z \in \mathcal{D}^{-}$.

Put

$$
U_{\pm} = (A \pm \sqrt{-1} C)(Z + 1) + (B \pm \sqrt{-1} D)\sqrt{-1}(Z - 1).
$$

Then

$$
\begin{pmatrix} U_{-} \\ U_{+} \end{pmatrix} = \begin{pmatrix} 1 &amp; -\sqrt{-1} \\ 1 &amp; \sqrt{-1} \end{pmatrix} \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} \begin{pmatrix} 1 &amp; 1 \\ \sqrt{-1} &amp; -\sqrt{-1} \end{pmatrix} \begin{pmatrix} Z \\ 1 \end{pmatrix}
$$

and

$$
\begin{aligned}
(t \overline{U}_{\pm})(U_{\pm}) &amp;= (\overline{Z} + 1)(t_{AA} + t_{CC})(Z + 1) \\
&amp;\quad + (\overline{Z} - 1)(t_{BB} + t_{DD})(Z - 1) \\
&amp;\quad - \sqrt{-1} (\overline{Z} - 1)(t_{BA} + t_{DC})(Z + 1) \\
&amp;\quad + \sqrt{-1} (\overline{Z} + 1)(t_{AB} + t_{CD})(Z - 1) \\
&amp;\quad \pm 2 (1 - \overline{Z} Z).
\end{aligned}
$$

Hence we have

$$
t \overline{U}_{+} \cdot U_{+} = \frac{1}{2} (t \overline{U}_{+} \cdot U_{+} + t \overline{U}_{-} \cdot U_{-}) + 2 (1 - \overline{Z} Z).
$$

Since $\text{rank } (U_{+}) = \text{rank } (Z) = g$,

$$
t \overline{U}_{+} \cdot U_{+} + t \overline{U}_{-} \cdot U_{-} &gt; 0
$$

and by the condition $Z \in \overline{\mathcal{D}}_{g}$,

$$
1 - \overline{Z} Z \geq 0.
$$

Therefore $t \overline{U}*{+} \cdot U*{+} &gt; 0$, in particular $\text{rank } U_{+} = g$.
Q.E.D.

By the action of $G$ a boundary component is transformed to another, namely the division of $\overline{\mathcal{D}}_{g}$ into boundary components is invariant under the action of $G$.

17

**Proposition (4.4).**

1. $\overline{\mathbf{p}}_g = \{Z \in M(g, \mathfrak{C}); {}^tZ = Z, 1_g - Z\overline{Z} \geq 0\}$.

2. We have a bijective correspondence between the set of boundary components $\{F\}$ and the set of real subspaces in $\mathbb{R}^{2g}$ of dimension $g'' \leq g$ $\{U\}$ defined as

$$F = F(U) = \{Z \in \overline{\mathbf{p}}*g \text{; for } W := \text{the vector subspace in } \mathfrak{C}^{2g} \text{ spanned by the columns of } \left( \begin{array}{c} Z + 1_g \\ \sqrt{-1}(Z - 1_g) \end{array} \right), U*{\mathfrak{C}} = W \cap \overline{W}\}$.

111. For a boundary component $F = F(U)$ and $M \in G$ we have

$$M \cdot F = F(M \cdot U)$$

where $M$ acts on $\mathbb{R}^{2g}$ (considered as a set of column vectors) as a $2g$-matrix.

iv) $F_{g'} = \left\{ \begin{pmatrix} Z' &amp; 0 \\ 0 &amp; 1_{g-g'} \end{pmatrix} \text{; } Z' \in \mathbf{p}*{g'} \right\} \oplus \mathbf{p}*{g'}$ is a boundary component.

In particular $\mathbf{p}_g$ itself is a boundary component.

For $F_{g'}$ the corresponding real subspace is of dimension $g'' = g - g'$.

v) $\overline{\mathbf{p}}*g = \bigcup*{0 \leq g' \leq g} G \cdot F_{g'}$.

If $F = M \cdot F_{g'}$ for $M \in G$, we say $F$ is *of degree* $g'$.
For $F = F(U)$ we have: degree $F + \dim U = g$.
(Actually $G$ can be replaced by a maximal compact subgroup $K = \operatorname{Iso}(\sqrt{-1}1_g) \to (1.6) \text{ i})$ as is seen in the proof.)

**Proof.**

1. Easy.

iv) It is clear that all points in $F_{g'}$ are mutually equivalent.

We want to show $F_{g'}$ is a maximal set with respect to this equivalence relation.
By definition it suffices to prove the following

**Claim (4.4.1).** Let $\xi : D = \{t \in \mathfrak{C} ; |t| &lt; 1\} \to \overline{\mathbf{p}}*g$ be a holomorphic map with $\xi(0) \in F*{g'}$.
Then $\xi(D) \subset F_{g'}$.

**Proof.** The coefficients of a matrix

$$n(t) = 1 - \xi(t)\overline{\xi}(t)$$

18

are harmonic functions and $\eta(t) \geq 0$.
Hence for $\alpha = (0 \cdots 0 \alpha_{g' + 1} \cdots \alpha_{g}) \in \mathbb{R}^{g}$, $\alpha \eta(t)^{t} \alpha \geq 0$ and $\alpha \eta(0)^{t} \alpha = 0$, therefore $\alpha \eta(t)^{t} \alpha \equiv 0$ by the maximum principle.
Also for $\alpha = (\alpha_{1} \cdots \alpha_{g'} \quad 0 \cdots 0) \in \mathbb{R}^{g}$ we have $\alpha \eta(t)^{t} \alpha &gt; 0$ since $\alpha \eta(0)^{t} \alpha &gt; 0$.
Again by noting $\eta(t) \geq 0$ we have

$$
\eta(t) = \begin{pmatrix} \eta'(t) &amp; 0 \\ 0 &amp; 0 \end{pmatrix}, \quad \eta'(t) \in \mathcal{V}_{g'}^{+}.
$$

Write

$$
\xi(t) = \begin{pmatrix} \xi'(t) &amp; \xi'''(t) \\ t \xi'''(t) &amp; \xi''(t) \\ g' &amp; g - g' \end{pmatrix} \quad \text{)} g^{-}.
$$

Then the above says

$$
\begin{aligned}
1 - (\xi'(t) \overline{\xi}'(t) + \xi'''(t)^{t} \overline{\xi}'''(t)) &amp;&gt; 0, \\
t \xi'''(t) \overline{\xi}'(t) + \xi''(t)^{t} \overline{\xi}'''(t) &amp;= 0 \\
t \xi'''(t) \overline{\xi}'''(t) + \xi''(t) \overline{\xi}''(t) &amp;= 1.
\end{aligned}
$$

Hence

$$
\begin{aligned}
0 &amp;= \overline{\xi}''(t) \left( t \xi'''(t) \overline{\xi}'(t) + \xi''(t)^{t} \overline{\xi}'''(t) \right) \\
&amp;= - t \overline{\xi}'''(t) \xi'(t) \overline{\xi}'(t) - t \overline{\xi}'''(t) \xi'''(t) t \overline{\xi}'''(t) + t \overline{\xi}'''(t) \\
&amp;= t \overline{\xi}'''(t) \left( 1 - \xi'(t) \overline{\xi}'(t) - \xi'''(t)^{t} \overline{\xi}'''(t) \right).
\end{aligned}
$$

Therefore

$$
\xi'''(t) \equiv 0,
$$

and

$$
\xi''(t) \overline{\xi}''(t) = 1,
$$

namely $\xi''(t)$ is a unitary matrix.

By the next lemma we have

19

The proof of (4.4.1) is then complete.

**Lemma (4.4.2).** If a matrix-valued holomorphic function on a disc $\xi : D \to M(n, \mathbb{C})$ has its image in the set of unitary matrices, then $\xi$ is a constant function.

**Proof.** By differentiating the identity

$$
\xi(t)^t \overline{\xi}(t) = 1,
$$

we have

$$
\begin{aligned}
0 &amp;= \frac{d}{dt} (\xi(t)^t \overline{\xi}(t)) \\
&amp;= \frac{d\xi}{dt}(t)^t \overline{\xi}(t).
\end{aligned}
$$

Hence

$$
\frac{d\xi}{dt}(t) \equiv 0.
$$

iii) For $Z \in \overline{\mathbf{D}}_g$ and $M \in G$ we see from (\*) in (4.3) that the space generated by column vectors of

$$
(\sqrt{-1} (M \cdot Z - 1))
$$

is the same as the space generated by those of

$$
M(\sqrt{-1} (Z - 1)),
$$

which implies iii) by the definition of $F(U)$.

ii), v). It is easily seen that

$$
F_g' = F(U_{g'}')
$$

where $U_{g'}$ is the space generated by the columns of

$$
\begin{pmatrix} 0 \\ 1_{g'} \end{pmatrix}_{0g'}, \quad g'' = g - g'.
$$

20

The claims iii) and iv) being established, the conclusion follows from these and the next lemma.

**Lemma (4.4.3).** The unitary group $U(g)$ operates transitively on the set of real subspaces of dimension $g'' \leq g$ in $\mathfrak{C}^g$.

Proof is left to the reader.

**Remark (4.5) (Intrinsic description).**

A: non-degenerate skew-symmetric form on $\mathbb{R}^{2g}$ and extend it to $\mathfrak{C}^{2g} = \mathbb{R}^{2g}$ $\mathfrak{g}$ naturally.

$F(x, y) := \sqrt{-1} A(x, \overline{y})$, hermitian form.

We then have the following inclusion.

$$
\begin{aligned}
\mathcal{D}_g &amp;= \{W, \text{g-space in } \mathfrak{C}^{2g} \text{; } A_{|W} = 0, F_{|W} &gt; 0\}, \\
&amp;\text{open} \\
\mathcal{D}_g^c &amp;= \{W, \text{g-space in } \mathfrak{C}^{2g} \text{; } A_{|W} = 0\}, \\
&amp;\text{compact} \\
\text{Grass}(2g, g) &amp;= \{W, \text{g-space in } \mathfrak{C}^{2g}\}.
\end{aligned}
$$

The first embedding

$$
\begin{aligned}
\mathcal{D}_g &amp;&lt; \quad \mathcal{D}_g^c \\
\partial \pi &amp;&amp; \partial \pi \\
G/K &amp;&lt; \quad G_{\mathfrak{C}}/B
\end{aligned}
$$

is the so-called Borel embedding in our case.

Then a boundary component in the topological closure $(\mathcal{D}_g)^-$ in $\mathcal{D}_g^c$ is defined as

$$
F = F(U) \text{; } U, \text{ real } g''\text{-dimensional subspace in } \mathbb{R}^{2g},
$$

$$
:= \{W, \text{g-space in } \mathfrak{C}^{2g} \text{; } A_{|W} \equiv 0, F_{|W} \geq 0, \text{ and } W \cap \overline{W} = U_{\mathfrak{C}}\}.
$$

In this case we have

$$
\operatorname{rank} F_{|W} + \dim U = g.
$$

Now we go into study of the second topic, the structure of the parabolic subgroup associated with a boundary component.

21

Definition (4.6). Let $F$ be a boundary component of $D = D_g$.
Then we define:

1. $P(F) = \{g \in G; gF = F\}$, the parabolic subgroup associated with $F$;

2. $W(F) =$ the unipotent radical of $P(F)$;

3. $U(F) =$ the centre of $W(F)$.

Lemma (4.7). Let $F_1$ and $F_2$ be two boundary components.
If $gF_1 = F_2$ for an element $g \in G$, then $P(F_2) = gP(F_1)g^{-1}$, etc.

Proof.
Clear from the Definition (4.6).

Proposition (4.8). For a boundary component $F_g$, the subgroups of $G$ defined in (4.6) can be expressed explicitly as follows.

1. $P_{g'} = P(F_{g'}) = \left\{ \begin{array}{lll} A' &amp; 0 &amp; B' * \\ * &amp; u &amp; * * \\ C' &amp; 0 &amp; D' * \\ 0 &amp; 0 &amp; 0 &amp; t_{u^{-1}} \end{array} \right\} \in G; u \in GL(g'', IR), g'' = g - g' \}.$

2. $W_{g'} = W(F_{g'}) = \left\{ \begin{array}{llll} \frac{1}{g'} &amp; 0 &amp; 0 &amp; n \\ t_m &amp; \frac{1}{g''} &amp; t_n &amp; b \\ 0 &amp; 0 &amp; \frac{1}{g'} &amp; -m \\ 0 &amp; 0 &amp; 0 &amp; \frac{1}{g''} \end{array} \right\}; t_{nm} + b = t_{mn} + t_b.$

3. $U_{g'} = U(F_{g'}) = \{[b] = \begin{pmatrix} 1_{g'} &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; \frac{1}{g''} &amp; 0 &amp; b \\ 0 &amp; 0 &amp; \frac{1}{g'} &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; \frac{1}{g''} \end{pmatrix}; t_b = b\}$

We have inclusions of normal subgroups

$$
P_{g'} \supset W_{g'} \supset U_{g'}.
$$

Proof.
If the claim 1) is established, the others 11) 111) are easy.

22

We prove i). Write $ g = \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} \in \mathbb{P}(F_g') $ and further

$$
A = \begin{pmatrix} A_1 &amp; A_2 \\ A_3 &amp; A_4 \end{pmatrix}, \quad B = \begin{pmatrix} B_1 &amp; B_2 \\ B_3 &amp; B_4 \end{pmatrix}, \quad C = \begin{pmatrix} C_1 &amp; C_2 \\ C_3 &amp; C_4 \end{pmatrix}, \quad D = \begin{pmatrix} D_1 &amp; D_2 \\ D_3 &amp; D_4 \end{pmatrix},
$$

so that the matrices with index 1 are $ g' $ by $ g' $ matrices, with index 2 $ g' $ by $ g' $, with index 3 $ g'' $ by $ g' $, with index 4 $ g'' $ by $ g'' $, respectively.
By (4.4) iii)

$$
\mathbb{P}(F(U)) = \{ F \in G \ ; \ FU = U \}.
$$

Applying this to $ U = U_g $, (cf.
proof of (4.4) ii), v)), we see that

$$
A_2 = C_2 = 0, \quad C_4 = 0.
$$

Referring to the condition (1.2) that $ g \in G $, we have

$$
C_3 = D_3 = 0, \quad {}^t A_4 D_4 = 1
$$

and

$$
\begin{pmatrix} A_1 &amp; B_1 \\ C_1 &amp; D_1 \end{pmatrix} \in \mathrm{Sp}(g', \mathbb{R}).
$$

Let us show, for example, $ C_3 = 0 $ and $ {}^t A_4 D_4 = 1 $.

Rewriting the condition $ {}^t AD - {}^t CB = 1 $, we have

$$
\begin{aligned}
1 &amp;= \begin{pmatrix} a_1 &amp; 0 \\ A_3 &amp; A_4 \end{pmatrix} \begin{pmatrix} D_1 &amp; D_2 \\ D_3 &amp; D_4 \end{pmatrix} - {}^t \begin{pmatrix} C_1 &amp; 0 \\ C_3 &amp; 0 \end{pmatrix} \begin{pmatrix} B_1 &amp; B_2 \\ B_3 &amp; B_4 \end{pmatrix} \\
1 &amp;= \begin{pmatrix} {}^t A_1 D_1 + {}^t A_3 D_3 &amp; {}^t A_1 D_2 + {}^t A_2 D_4 \\ -{}^t C_1 B_1 - {}^t C_3 B_3 &amp; -{}^t C_1 B_2 - {}^t C_3 B_4 \\ {}^t A_4 D_3 &amp; {}^t A_4 D_4 \end{pmatrix}
\end{aligned}
$$

The lower half of the last matrix shows :

23

$$ {}^tA_4D_4 = l_g'' \quad \text{and} \quad {}^tA_4D_3 = 0, $$

hence

$$ D_3 = 0. $$

To show the rest is left to the reader.

Definition (4.9). For $ F = F_g' $,

$$ G_h(F_g') := \left\{ \begin{pmatrix} A' &amp; 0 &amp; B' &amp; 0 \\ 0 &amp; l_g'' &amp; 0 &amp; 0 \\ C' &amp; 0 &amp; D' &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; l_g'' \end{pmatrix} \right\} ; \quad \begin{pmatrix} A' &amp; B' \\ C' &amp; D' \end{pmatrix} \in \mathrm{Sp}(g'', \mathbb{R}) \right\} $$

$$
\begin{array}{l} \updownarrow \mathrm{Sp}(g', \mathbb{R}).
\end{array}
$$

$$ G_k(F_g') := \left\{ \begin{pmatrix} l_g' &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; u &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; l_g' &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; t_u - 1 \end{pmatrix} \right\} ; \quad u \in \mathrm{GL}(g'', \mathbb{R}) \right\}, \quad g'' = g - g' $$

$$
\begin{array}{l} \updownarrow \mathrm{GL}(g'', \mathbb{R}).
\end{array}
$$

In order to define these groups in general, we need quite deep part of the theory of Lie algebras.
Note that these subgroups are not normal in $ P_g' $.

Proposition (4.10). For $ F = F_g' $, $ P_g' = P(F_g') $ enjoys the following properties.

1. $ P_g' = (G_h \times G_k)W_g' $, semidirect product.

ii) $ W_g' $ is a metaabelian group with a decomposition

$$
0 \rightarrow U_g' \rightarrow W_g' \rightarrow W_g'/U_g' \rightarrow 0 \text{ (exact)}.
$$

Here $ U_g' $ and $ W_g'/U_g' $ are vector groups.

24

iii) The normalizer of $U_{g'}$ in $G$ is $P_{g'}$.

iv) The centralizer of $U_{g'}$ in $G$ is $G_{h}(F_{g'}) \omega_{g'}$.

v) Put

$$
\omega = [1_{g''}] \in U_{g'}
$$

and $\Omega_{g'} =$ the $P_{g'}$-orbit ($= G_{h}(F_{g'})$-orbit) of $\omega$ in $U_{g'}$ where the action of $P_{g'}$ on $U_{g'}$ is defined by conjugation.
Then we have isomorphisms

$$
\begin{array}{l}
\Omega_{g'} \xrightarrow{\sim} \mathcal{U}_{g''} \\
n \qquad \qquad n \\
U_{g'} \xrightarrow{\sim} \mathcal{U}_{g''} \quad (\text{cf. (4.8) iii}).
\end{array}
$$

vi) We have two epimorphisms

$$
\begin{array}{l}
P_{g'} \rightarrow G_{h}(F_{g'}) \stackrel{\sim}{\to} \operatorname{Aut}(\mathcal{D}_{g'}) = \operatorname{Sp}(g', \mathbb{R}), \\
P_{g'} \rightarrow G_{h}(F_{g'}) \stackrel{\sim}{\to} \operatorname{Aut}(U_{g'}, \Omega_{g'}) \\
= \operatorname{Aut}(\mathcal{U}_{g''}, \mathcal{U}_{g''}') = \operatorname{GL}(g'', \mathbb{R}).
\end{array}
$$

Here $\operatorname{GL}(g'', \mathbb{R}) \ni u$ acts on $\mathcal{U}_{g''}$ as $y'' \rightarrow uy''^t u$.

The proof, being straightforward or elementary, is left to the reader.

**Remark (4.11).** i) The above holds for all $F$ when one defines $G_{h}$ and $G_{h'}$ suitably.
(The easiest way would be to put $G_{h}(gF_{g'}) = gG_{h}(F_{g'})g^{-1}$, etc. Note that these subgroups are defined up to conjugacy.)

ii) $P(F)$ acts transitively on $\mathcal{D}_{g}$.

**Proof.** For $p, q \in \mathcal{D}_{g}$ there is a $g \in G$ with $q = g(p)$ ((1.4) ii)). By (4.4) v) there is an element $h \in \operatorname{Iso}(q) \approx K$ such that $h(g(F)) = F$.
Then $(h \cdot q)(p) = q$ and $h \cdot g \in P(F)$.

iii) Under the notation in (4.10) v) $\mathcal{U}_{g''}$ has a quadratic form

$$
(y_1, y_2) \rightarrow \operatorname{tr}(y_1 y_2),
$$

25

by which $\mathfrak{g}_g$ is selfdual.
The quadratic form on $U_g$, induced by the isomorphism $U_g \xrightarrow{\cong} \mathfrak{g}_g$ is nothing but the one induced from the Killing form on $\operatorname{Lie}(U_g)$, by the exponential map which is an isomorphism.

Next we investigate adherence relation among boundary components.

**Proposition (4.12).** Let $F = F(U)$, $U \subset \mathbb{R}^{2g}$ as in (4.4) ii).
Then the topological closure of $F$ in $\overline{\mathcal{D}}_g$ is

$$
\overline{F} = \{Z \in \overline{\mathcal{D}}_g \mid W := \text{the vector space in } \mathbb{C}^{2g} \text{ spanned by the columns of } \left( \sqrt{-1}(Z - 1) \right), \text{ then } W \cap \overline{W} \supset U_{\mathfrak{C}}\}.
$$

**Proof.** It follows from the following three facts each of which can be proved easily.

i) The subset $\{W : U_{\mathfrak{C}} \subset W \cap \overline{W}\}$ is closed and real analytic in Grass(2g, g).

ii) The function $Z \to \dim W \cap \overline{W}$ is upper semicontinuous in real Zariski topology.
In particular in any connected closed real analytic subset $A$ of $\mathcal{D}_g^c$, the subset $A' = \{Z \in A \mid \dim W \cap \overline{W} \text{ is not maximal}\}$ is a thin set.

iii) $\overline{F}$ is convex, hence connected.

**Notation (4.13).** For two boundary components $F, F'$ of $\mathcal{D}$ we write

$$
F \langle F' \quad \text{if} \quad F \subset (F')^*.
$$

Proposition (4.12) says that for $F = F(U)$ and $F' = F(U')$,

$$
F \langle F' \quad \langle \Rightarrow \quad U \supset U'.
$$

**Theorem (4.14).** i) For two boundary components $F$ and $F'$ of $\mathcal{D}$ with $F \langle F' \quad$ we have a) $U(F) \supset U(F')$ (The converse holds by (4.10) iii).) b) $G_{\mathfrak{L}}(F) \supset G_{\mathfrak{L}}(F')$,

26

c) $G_{h}(F) \subset G_{h}(F')$.

(b), c) by taking conjugate if necessary.)

ii) a) For two boundary components $F$ and $F'$ of $\mathcal{D}$ with $F &lt; F'$, we have

$$
\Omega(F')^{-} = \Omega(F)^{-} \circ U(F')
$$

with the above inclusion $U(F') \subset U(F)$.

b) We fix a boundary component $F$ of $\mathcal{D}$.
Defining boundary components of $\Omega(F)$ in $U(F)$ as sets of the form: $\Omega(F)^{-} \circ$ a linear subspace of $U(F)$, we have a bijective correspondence between the set of boundary components $F'$ with $F &lt; F'$ and the set of boundary components of $\Omega(F)$ as

$$
\begin{array}{c}
\{F'; F &lt; F'\} \to \{\text{boundary components of } \Omega(F)\} \\
\downarrow \\
F' \xrightarrow{\text{boundary components of } \Omega(F')} \\
\end{array}
$$

by which the adherence relation is reversed, i.e.

$$
F' &lt; F'' \quad \Leftrightarrow \quad \Omega(F') &gt; \Omega(F'')
$$

iii) For two boundary components $F^{(1)}, F^{(2)}$ with $F^{(1)} &lt; F^{(2)}$ there is an element $M \in G = \operatorname{Sp}(g, \mathbb{R})$ such that $M \cdot F^{(1)} = F_{g_1}$ and $M \cdot F^{(2)} = F_{g_2}$ with $g_1 \leq g_2$.

(As the proof shows, a stronger statement holds that for any chain of boundary components

$$
F^{(g-1)} &gt; F^{(g-2)} &gt; \dots &gt; F^{(0)}
$$

where $F^{(k)}$ is of degree $k$, there is an $M \in G$ with

$$
M \cdot F^{(k)} = F_k, \quad k = 0, 1, \dots, g-1.)
$$

Proof.
We prove iii), from which the other statements follow easily.

27

We may assume $F_0 \leqslant F^{(1)}$, i.e. writing $F^{(1)} = F(U^{(1)})$, $F^{(2)} = F(U^{(2)})$, we have

$$
U_0 = \left\{ \begin{array}{l} u_1 \\ u_2 \\ 0 \\ \vdots \\ 0 \end{array} \right\}_{g} \leqslant \mathbb{R}_{2g} \supset U^{(1)} \supset U^{(2)}.
$$

Considering $U^{(1)}$ and $U^{(2)}$ as subspaces of $\mathbb{R}^g = U_0$, one can show that there is an element $u_1 \in GL(g, \mathbb{R})$ with $u_1 U^{(1)} = U_{g_1}$.
(This operation is nothing but to choose a basis of $U^{(1)}$ and extend it to a basis of $U_0$.)
Again choose an element $u_2 \in GL(g_1, \mathbb{R})$ so that $u_2(u_1 U^{(2)}) = U_{g_2}$.
Then $u = \begin{pmatrix} 1 &amp; &amp; \\ &amp; u_2 \end{pmatrix} \cdot u_1$ satisfies the condition

$$
u U^{(1)} = U_{g_1}, \quad u U^{(2)} = U_{g_2}.
$$

Hence by means of (4.4) iii) we see that

$$
M = \begin{pmatrix} u &amp; 0 \\ 0 &amp; t_{u^{-1}} \end{pmatrix}
$$

has the desired property.
Q.E.D.

The last topic in this section is "rationality" of boundary components.

**Definition (4.15).** A boundary component $F$ of $D_g$ is called *rational* if it satisfies one of the following mutually equivalent conditions.

i) $P(F)$ is defined over $\mathbb{Q}$ (general definition).

ii) $F = F(U)$ and $U$ is defined over $\mathbb{Q}$ (i.e. a basis is chosen in $\mathbb{Q}^{2g}$).

iii) $\mathbb{M} \in G_{\mathbb{Q}} = \operatorname{Sp}(g, \mathbb{Q})$ with $M \cdot F = F_{g'}$.

(To show: ii) $\langle \Rightarrow \text{iii} \Rightarrow \text{i} \rangle$ is easy.
The claim: i) $\Rightarrow \text{iii} \text{ is not trivial.}$)

We put

$$
D^2 = \prod_{F: \text{rational}} F \in \overline{D}
$$

28

and call it the *rational closure* of $\mathcal{D}$.

**Remark (4.16).** Actually, if $F$ is a rational boundary component of $\mathcal{D}*g$, then there is $M \in G*{\mathbb{Z}} = \mathrm{Sp}(g, \mathbb{Z})$ such that $M \cdot F = F_g$.
This is a very special property of $\Gamma$.

**Proof.** First we prove it for $F = F(U)$ of degree $g' = 0$.
By definition there is a $\mathbb{Q}$-subspace $U_{\mathbb{Q}}$ of $\mathbb{Q}^{2g}$ with $U_{\mathbb{Q}} \otimes \mathbb{R} = U$.
Then we have a direct decomposition

$$
\mathbb{Q}^{2g} = U_{\mathbb{Q}} \oplus U_{\mathbb{Q}}^{*}
$$

where $U^{*}$ is embedded in $\mathbb{Q}^{2g}$ by an alternating bilinear form

$$
A = \left( \begin{array}{cc} 0 &amp; 1_g \\ -1_g &amp; 0 \end{array} \right).
$$

Since $A$ is an integrally invertible matrix, this decomposition can be reduced to

$$
\mathbb{Z}^{2g} = U_{\mathbb{Z}} \oplus U_{\mathbb{Z}}^{*}
$$

Take a basis $e_1, \dots, e_g$ of $U_{\mathbb{Z}}$ and its dual basis $e_1^*, \dots, e_g^*$ in $U_{\mathbb{Z}}^*$.
Then

$$
M = (e_1 \cdots e_g \ e_1^* \ \cdots \ e_g^*) \in \mathrm{Sp}(g, \mathbb{Z})
$$

and $M \cdot U_0 = U$.

Now we treat general case.
From the above we may assume $F &gt; F_0$.
Then the same proof as (4.14) iii) goes through under a stronger condition that $u$ is chosen to be integral.
(In our case this operation is essentially to choose a basis of $U_{\mathbb{Z}}$ and extend it to a basis of $(U_0)_{\mathbb{Z}}$.)

§5. Realization as a Siegel domain of the third kind, and Satake compactification.

(5.1) We keep our notation in the previous section.

We consider the Borel embedding

$$
D_g = G/K \subset D_g^C = G_\pi/B,
$$

and a boundary component $F$ of $D_g$ in $\overline{D}_g$ (4.2), and associated groups $P(F), \mathcal{W}(F), U(F)$ etc. (4.6).

We put moreover

$$
D(F) = U(F)_\pi D_g \subset D_g^C,
$$

and

$$
D'(F) = U(F)_\pi \setminus D(F).
$$

**Theorem (5.2)** (Realization of $D$ as a Siegel domain of the third kind with respect to a boundary component).

We use the notation above.

i) We have the following commutative diagram of holomorphic maps, among which the horizontal arrows are isomorphisms and the right vertical ones are projections.

$$
\begin{array}{c c c}
D(F) &amp; \tilde{\gamma} &amp; F \times V(F) \times U(F)_\pi \\
\downarrow &amp; &amp; \downarrow \\
\pi_F \left| \begin{array}{c c c}
D'(F) &amp; \tilde{\gamma} &amp; F \times V(F) \\
\downarrow &amp; &amp; \downarrow \\
F &amp; = &amp; F
\end{array} \right. \\
\end{array}
$$

Here $V(F) = \mathcal{W}(F)/U(F)$ carries a complex structure defined suitably.
The map $D(F) \to D'(F)$ is the canonical one.

The map $\pi_F$ is $P(F)$-equivariant when the action of $P(F)$ on $F$ is defined by the epimorphism $P(F) \to G_h$ in (4.10) vi).

$$
\begin{array}{c c c}
\pi_F : D(F) &amp; \to &amp; F \\
\uparrow &amp; &amp; \uparrow \\
\vdots &amp; &amp; \vdots \\
\vdots &amp; &amp; \vdots \\
P(F) &amp; \to &amp; G_h
\end{array}
$$

30

ii) There is a real analytic map

$$
\begin{array}{l}
\phi : \mathcal{D}(F) \to \mathcal{U}(F) \stackrel{\circ}{\to} \mathcal{W}_{g''} \\
\upsilon \qquad \upsilon \qquad \upsilon \\
\mathcal{D}_{g} \quad \to \quad \Omega(F) \quad \stackrel{\circ}{\to} \mathcal{W}_{g''}^+, \quad (4.10) \ v)
\end{array}
$$

which maps $\mathcal{D}_{g}$ onto $\Omega(F)$ and has the properties:

a) $\phi$ is $P(F)$-equivariant when the action of $P(F)$ on $\mathcal{U}(F)$ is defined by conjugation (cf.
(4.10) iv)), or equivalently by the epimorphism $P(F) \to G_{\ell}$ in (4.10) vi);

$$
\begin{array}{l}
\phi : \mathcal{D}_{g} \quad \to \quad \Omega(F) \quad \stackrel{\circ}{\to} \mathcal{W}_{g''}^+ \\
\begin{array}{c c c c}
\uparrow &amp; &amp; \uparrow &amp; \\
\vdots &amp; &amp; \vdots &amp; \\
\end{array} \\
P(F) \to G_{\ell} \quad \stackrel{\circ}{\to} \mathrm{GL}(g'', \mathbb{R});
$$

b) $\phi^{-1}(\Omega(F)) = \mathcal{D}_{g}$.

Roughly speaking, the theorem claims that $\mathcal{D}$ is a family of tube domain parametrized by $\mathcal{D}'(F)$ which is a vector bundle over the boundary component $F$ considered.

**Remark (5.3).** $\phi$ is *not* defined by the projection with the isomorphism in 1).

(5.4) *Example-Proof of (5.2).* By (4.4) it suffices to treat the case when $F = F_{g'}$ which we exhibit the theorem more explicitly (cf.
(4.8)).

i) In the unbounded realization $\mathcal{G}_{g}$, we write

$$
\mathcal{G}_{g} \ni \tau = \begin{pmatrix}
\tau' &amp; \tau''' \\
t_{\tau'''} &amp; \tau''' \\
\hline
g' &amp; g''
\end{pmatrix}_{g''}.
$$

Put

$$
V(F_{g'}) = M(g', g''; \mathfrak{C}),
$$

which is isomorphic to $\mathcal{W}*{g'}/\mathcal{U}*{g'}$ via

31

$$
\left( \begin{array}{cccc}
1 &amp; 0 &amp; 0 &amp; n \\
t_m &amp; 1 &amp; t_n &amp; b \\
0 &amp; 0 &amp; 1 &amp; -m \\
0 &amp; 0 &amp; 0 &amp; 1
\end{array} \right) \quad \longleftrightarrow \quad \sqrt{-1} \, m + n,
$$

and recall an isomorphism

$$
\begin{array}{ccc}
u(F)_{\mathfrak{C}} &amp; \to &amp; \mathcal{F}_{g^*}, \mathfrak{C} \\
\vee &amp; &amp; \vee \\
[b] &amp; \to &amp; b.
\end{array}
$$

Then clearly

$$
D(F_{g'}) = \{ \tau = \begin{pmatrix} \tau' &amp; \tau''' \\ t_{\tau'''} &amp; \tau'' \end{pmatrix} \in M(g, \mathfrak{C}) \quad ; \quad t_{\tau} = \tau, \tau' \in \mathcal{G}_{g'} \},
$$

and the first horizontal isomorphism in the diagram is

$$
\begin{array}{ccc}
D(F_{g'}) &amp; \to &amp; \mathcal{G}_{g'} \times V(F_{g'}) \times U_{g'}, \mathfrak{C} \\
\vee &amp; &amp; \vee \\
[ \tau' \quad \tau''' ] &amp; \to &amp; (\tau', \quad \tau''', \quad [\tau']) \\
t_{\tau'''} \quad \tau'' &amp; &amp; .
\end{array}
$$

from which the other maps are naturally induced.

11. With the above notation $\Phi$ is defined as

$$
\begin{array}{ccc}
\Phi : D(F_{g'}) &amp; \to &amp; U_{g'} \xrightarrow{\gamma} \mathcal{F}_{g''} \\
\vee &amp; &amp; \vee \\
[ \tau' \quad \tau''' ] &amp; \to &amp; \text{Im } \tau'' - {}^t(\text{Im } \tau''')(\text{Im } \tau')^{-1}(\text{Im } \tau''). \\
t_{\tau'''} \quad \tau'' &amp; &amp; .
\end{array}
$$

All claims can be checked directly.
Let us just prove the claim b). Put

$$
a = \text{Im } \tau', \quad b = \text{Im } \tau'', \quad c = \text{Im } \tau'''.
$$

We should show that under the assumption

$$
t_{\tau} = \tau, \quad \text{and} \quad a &gt; 0,
$$

32

two conditions

a) $\left( \begin{array}{ll} a &amp; c \\ t_c &amp; b \end{array} \right) &gt; 0$

b) $b - {}^{t} \mathrm{ca}^{-1} \mathrm{c} &gt; 0$

are equivalent.
This follows, however, directly from an equality:

$$
\left( \begin{array}{cc} 1 &amp; 0 \\ t_{ca}^{-1} &amp; 1 \end{array} \right) \left( \begin{array}{cc} a &amp; c \\ t_c &amp; b \end{array} \right) \left( \begin{array}{cc} 1 &amp; -a^{-1}c \\ 0 &amp; 1 \end{array} \right) = \left( \begin{array}{cc} a &amp; 0 \\ 0 &amp; b - {}^{t} \mathrm{ca}^{-1}c \end{array} \right).
$$

Remark (5.5) (Intrinsic proof of (5.2)-outlined)

1. One can show first that for a boundary component $F$ of $D$ there is a one-parameter subgroup $w_{F}: \mathfrak{S}_{m} \to G$ such that

$$
\lim_{t \to 0} w_{F}(t)^{-1} \circ = \circ_{F} \in F
$$

where $\circ$ is a base point in $D$ . For example in the case of $D = \mathfrak{S}_g$ , $F = F_g$ ,

$$
w_{F}(t) = \left( \begin{array}{cccc} 1_g &amp; &amp; &amp; \\ &amp; t_{1_g} &amp; &amp; \\ &amp; &amp; 1_g &amp; \\ &amp; &amp; &amp; t^{-1}_{1_g} \end{array} \right),
$$

and

$$
\begin{array}{l}
o = \sqrt{-1} \lg \text{ in } \mathfrak{S}_g, \quad = 0 \text{ in } D_g, \\
o_{F} = \left( \begin{array}{cc} 0 &amp; 0 \\ 0 &amp; 1_g \end{array} \right) \text{ in } \overline{D}_g.
\end{array}
$$

This $o_{F}$ depends only on the choice of $o$ and not on $w_{F}$ .

By means of $w_{F}$ , parabolic subgroups defined in §4 are characterised as

$$
P(F) = \{M \in G; \exists \lim_{t \to 0} w_{F}(t) M w_{F}(t)^{-1} \},
$$

33

$$
W(F) = \{M \in G; \lim_{t \to 0} w_F(t) M w_F(t)^{-1} = 1\},
$$

$$
G_n(F) \times G_k(F) = \text{the centralizer of } w_F.
$$

Let

$$
s_o = \text{the symmetry at } o \text{ in } p,
$$

$$
s_{o_F} = \text{the symmetry at } o_F \text{ in } F,
$$

and

$$
F^s = s_o(F).
$$

Using the map

$$
p_w : p_g(F) \longrightarrow F^s
$$

$$
\begin{array}{c}
w \\
z
\end{array}
\longrightarrow
\begin{array}{c}
lim_{t \to 0} w_F(t) z,
\end{array}
$$

the desired projection $\pi_F : p_g(F) \to F$ is defined as

$$
\pi_F = s_{o_F} \cdot s_o \cdot p_w.
$$

One should take note on the fact that a map

$$
p_{w^{-1}} : p_g(F) \longrightarrow F
$$

$$
\begin{array}{c}
w \\
z
\end{array}
\longrightarrow
\begin{array}{c}
lim_{t \to 0} w_F(t^{-1}) z
\end{array}
$$

defined more simply is not $P(F)$-equivariant.

11. As a real analytic manifold

$$
p(F) = U(F)_{\underline{\mathbf{e}}} P(F) / P(F) \cap K,
$$

since

$$
p = G/K \quad \approx \quad P(F) / P(F) \cap K.
$$

(4.11) 11)

34

Hence we can define $\Phi$ as

$$
\begin{array}{r l}
\Phi : \mathcal{D}(F) &amp; \longrightarrow U(F)_{\mathfrak{C}} P(F) / P(F) = U(F) \\
&amp; \text{canonical} \\
&amp; \quad \text{up mod } P(F) \to \text{Im } u.
\end{array}
$$

**Proposition (5.6).** i) Let $F$ and $F'$ be two boundary components with $F &lt; F'$.
Then there is a holomorphic epimorphism

$$
\pi_{F, F'}: F' \longrightarrow F
$$

which satisfies a commutative diagram

![img-8.jpeg](img-8.jpeg)

where $\pi_F$ and $\pi_{F'}$ are projections defined in (5.2) i).

ii) For a boundary component $F$ of $\mathcal{D}_g$ put

$$
\overline{\mathcal{D}}_{g}^{(F)} = \underset{F' &gt; F}{\cup} F'.
$$

Then $\overline{\mathcal{D}}_{g}^{(F)} \subset \mathcal{D}(F)$, and by the map $\Phi$ in (5.2) ii) $F'$ is mapped onto a boundary component $\Omega(F')^*$ which is the dual of $\Omega(F')$ in (4.14) ii) b) with respect to a natural quadratic form on $U(F)$ ((4.11) iii)).

The proof is similar to (5.4) by reducing to the case $F = F_{g'}$.

(5.7) *Definition of cylindrical topology on $\mathcal{D}^2$* (Pjatečki-Šapiro).

Consider a boundary component $F_{g'}, 0 \leq g' \leq g$.
We have a chain of boundary components

$$
\mathcal{D}_g = F_g &gt; F_{g-1} &gt; \dots &gt; F_{g'+1} &gt; F_{g'}
$$

and projections

$$
\pi_{g', g_1} = \pi_{F_{g'}, F_{g_1}}: F_{g_1} \to F_{g', g' \leq g_1 \leq g}
$$

35

defined in (5.6). Also by (5.6) 11) the map $\Phi : \mathcal{D}(\mathsf{F}*{\mathsf{g}^{\prime}}) \to \mathcal{U}*{\mathsf{g}^{\prime}}$ maps $\mathsf{F}_{\mathsf{g}_1}, \mathsf{g}*1 \geq \mathsf{g}^{\prime}$, onto a boundary component $\Omega*{\mathsf{g}*1}^*$ dual to $\Omega*{\mathsf{g}^{\prime} - \mathsf{g}*1}$ in $\mathcal{U}*{\mathsf{g}^{\prime}}$ (cf.(5.4)).

For an open set $U$ of $\mathsf{F}*{\mathsf{g}'}$ and an element $K*{\mathsf{g}*1}$ in $\Omega*{\mathsf{g}_1}^*$, $\mathsf{g}' \leq \mathsf{g}_1 \leq \mathsf{g}$, we put

$$
U _ {g _ {1}} (U; K _ {g _ {1}}) = \{p \in F _ {g _ {1}}; \pi_ {g ^ {\prime}, g _ {1}} (p) \in U, \Phi (p) - K _ {g _ {1}} \in \Omega_ {g _ {1}} ^ {*} \}.
$$

Rewriting this definition by (5.4), we have for

$$
p = \left( \begin{array}{c c} \tau^ {\prime} &amp; \tau^ {\prime \prime} \\ t _ {\tau^ {\prime \prime \prime}} &amp; \tau^ {\prime \prime} \end{array} \right) \in F _ {g _ {1}} \text{ with } \tau^ {\prime} \in \mathfrak {S} _ {g ^ {\prime}},
$$

$$
\begin{array}{l} p \in U _ {g _ {1}} (U; K _ {g _ {1}}) \iff \tau^ {\prime} \in U, \text{ and } \text{Im } \tau^ {\prime \prime} - ^ {t} (\text{Im } \tau^ {\prime \prime \prime}) (\text{Im } \tau^ {\prime \prime}) ^ {- 1} (\text{Im } \tau^ {\prime \prime \prime}) \\ - K _ {g _ {1}} &gt; 0 \text{ in } \mathcal {U} _ {g _ {1} - g ^ {\prime}}. \\ \end{array}
$$

We put

$$
\begin{array}{l} U (U; K _ {g}, K _ {g - 1}, \dots , K _ {g ^ {\prime} + 1}) \\ = \left(G _ {\mathbb {Z}} \cap G _ {\xi} \cdot W _ {g ^ {\prime}}\right) \cdot \left(U \amalg_ {g ^ {\prime} &lt; g _ {1} \leq g} U _ {g _ {1}} (U; K _ {g _ {1}})\right) \\ \end{array}
$$

for $U \in F_{g'}$ and $K_{g_1} \in \Omega_{g_1}^* \subset U_{g'}$.
Then we define cylindrical topology on $\mathcal{D}^2$ as the weakest topology which has $U(U; K_g, \dots, K_{g' + 1})$ as open sets and is $G_{\mathfrak{Q}}$-invariant.

Note that $\mathcal{D}_g$ is open in $\mathcal{D}^2$ and on $\mathcal{D}_g$ the cylindrical topology is a natural one.

Example (5.8). In the case of $\mathbf{g} = 1$ fundamental system of neighbourhood of $1 \in \mathcal{D}^2$ is given as unions of $\{1\}$ and open discs in $\overline{\mathcal{D}}$ whose boundary circles pass through 1.

![img-9.jpeg](img-9.jpeg)

36

Note that such discs are Cayley transforms of $V_K$'s in (3.6.1).

The following fact would help us to understand the meaning of this topology.

**Scholie (5.9).** Let

$$
\tau_n = \begin{pmatrix} \tau_n' &amp; \tau_n'' \\ t_{\tau_n''} &amp; \tau_n'' \end{pmatrix}, \quad n = 1, 2, \cdots
$$

be a sequence in $\mathcal{G}_g$ with $\tau_n' \in \mathcal{G}_g$, and $\tau' \in \mathcal{G}_g' = F_g'$.
Then

$$
\tau_n \to \tau' \quad (n \to \infty) \quad \text{in} \quad \mathcal{D}
$$

iff

$$
\tau_n' \to \tau', \quad \text{Im} \quad \tau_n'' - {}^t(\text{Im} \quad \tau_n''')(\text{Im} \quad \tau_n'')(\text{Im} \quad \tau_n''') \to \infty.
$$

or under the assumption that $\{\tau_n'''\}$ is bounded, iff

$$
\tau_n' \to \tau', \quad \text{and} \quad \text{Im} \quad \tau_n'' \to \infty.
$$

Here we say that a sequence of real symmetric matrices $\{y_n\}$ diverges to infinity if for any symmetric matrix $A$, we have $y_n - A &gt; 0$ for $n \gg 0$.

Then we have the main theorem in this section, which however we don't prove.
For the precise proof see [26], [2].

**Theorem (5.10).** Let $\Gamma \in G_\mathfrak{Q}$ be an arithmetic subgroup acting on $\mathcal{D}$.
We consider the rational closure $\mathcal{D}^2$ of $\mathcal{D}$ with the cyclic topology.
Then

i) $\Gamma$ acts on $\mathcal{D}^2$ properly discontinuously.

ii) $(\Gamma \backslash \mathcal{D})^\gamma := \Gamma \backslash \mathcal{D}^2$ with its quotient topology is compact and contains $\Gamma \backslash \mathcal{D}$ as an open dense subset.

iii) $(\Gamma \backslash \mathcal{D})^\gamma$ admits a canonical structure of a normal analytic space such that $\Gamma \backslash \mathcal{D}$ is an analytic open subset, and is even a projective algebraic variety.

We call $(\Gamma \backslash \mathcal{D})^\gamma$ *Satake(-Baily-Borel)* *compactification* of $\Gamma \backslash \mathcal{D}$.

**Remark (5.11).** The topology on $\mathcal{D}^2$ defined by Satake-Baily-Borel (called Satake topology) is somewhat different from the

37

cylindrical topology, but they define the same quotient topology on $(\Gamma \backslash \mathcal{D})^{\gamma}$ (Kiernan-Kobayashi [18]).

Example (5.12). $\Gamma = \operatorname{Sp}(g, \mathbb{Z})$.

By (4.16) we see that as a set

$$
\left(\mathbb{G}_{g}^{*}\right)^{\gamma} = \mathbb{G}_{g}^{*} \amalg \mathbb{G}_{g-1}^{*} \amalg \cdots \amalg \mathbb{G}_{1}^{*} \amalg \mathbb{G}_{0}^{*}
$$

where $\mathbb{G}*{g}^{*} = (P*{g}, \cap \Gamma) \backslash F_{g}, = \operatorname{Sp}(g', \mathbb{Z}) \backslash \widetilde{\mathbb{G}}_{g}$.

We shall prove in our case that $(\mathbb{G}_{g}^{*})^{\gamma}$ is compact.

By the above description it suffices to show that any set $\{\tau_{n} \bmod \Gamma ; \tau_{n} \in \mathbb{G}*{g}\}$ has an accumulating point.
By (1.10) we may assume $\tau*{n} \in F$.
In particular for $x_{n} = \operatorname{Re} \tau_{n}$, $y_{n} = \operatorname{Im} \tau_{n}$, we have

$$
\left(y_{n}\right)_{kk} \leq \left(y_{n}\right)_{kk}, \quad k \leq k,
$$

$$
\left| \left(y_{n}\right)_{kk} \right| \leq \left(y_{n}\right)_{kk} \quad \text{by ii) in the definition of } F
$$

and

$$
-\frac{1}{2} \leq \left(x_{n}\right)_{k} \leq \frac{1}{2} \quad \text{by iii) in the definition of } F.
$$

Hence for unique $g'$ with $0 \leq g' \leq g$, $(y_{n})*{g'g'}$ is bounded but $(y*{n})_{g'+1, g'+1}$ diverges to infinity.
Then writing

$$
\tau_{n} = \left( \begin{array}{cc}
\tau_{n}' &amp; \tau_{n}'' \\
t &amp; \tau_{n}'' \\
\frac{\tau_{n}'}{\sum_{g'=g'}^{n} g - g'}
\end{array} \right) \begin{array}{c}
g' \\
g - g',
\end{array},
$$

we see that $\tau_{n}'$ and $\tau_{n}''$ are bounded.
Hence we can find a subsequence $\{\tau_{n_{i}}\}_{i}$ such that

$$
\tau_{n_{i}}' \to \tau', \tau_{n_{i}}''' \text{ bounded},
$$

and

$$
\operatorname{Im} \tau_{n}'' \to \infty \quad \text{again by ii) of the definition of } F.
$$

38

Applying the condition 1) in the definition of $F$ for

$$
M = \left( \begin{array}{ccccc}
0 &amp; 0 &amp; -l_g, &amp; 0 \\
0 &amp; l_g - g' &amp; 0 &amp; 0 \\
l_g, &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; l_{g-g'}
\end{array} \right)
$$

we have

$$
| \det \tau_n' | \geq 1.
$$

Together with the condition $\operatorname{Im} \tau_n &gt; 0$, we see

$$
\operatorname{Im} \tau' &gt; 0,
$$

hence

$$
\tau' \in \mathcal{G}_{g'}.
$$

By Scholie (5.9)

$$
\tau_{n_1} \rightarrow \tau' \in F_{g'},,
$$

hence

$$
\tau_{n_1} \mod \Gamma \rightarrow \tau' \mod \operatorname{Sp}(g', \mathbb{Z}) \in \mathcal{G}_{g''}^.
$$

# 6. Theory of torus embeddings.

We work only over the complex number field $\mathbb{C}$, though all the results except (6.2) and (6.16) ff.
hold for arbitrary algebraically closed fields.
All results are stated without proof, which can be found in [17] and [24] ((6.2), (6.16) in [2] Chap.
I).

(6.1) T = n-dimensional algebraic torus over $\mathbb{C}$

$$
\begin{array}{rl}
&amp; = \operatorname{Spec}(\mathbb{C}[T_1, T_1^{-1}, \dots, T_n, T_n^{-1}]) \text{ as a scheme} \\
&amp; = (\mathbb{C}^*)^n, \mathbb{C}^* = \mathbb{C} - \{0\}, \text{ as an analytic space}
\end{array}
$$

with the structure of multiplicative group.

$$
\begin{array}{l}
M = \operatorname{Hom}_{\text{alg. group}}(T, \mathbb{C}^*): \text{ the group of characters on } T \\
\downarrow \{\text{the monomials } \chi^r = \prod_{i=1}^{n} T_i^r\}^1 \} \simeq \mathbb{Z}^n = \{(r_1, \dots, r_n)\}. \\
N = \operatorname{Hom}_{\text{alg. group}}(\mathbb{C}^*, T) \colon \text{ the group of one-parameter} \\
\text{ subgroups in } T.
\end{array}
$$

$$
\begin{array}{c c c c}
\mathbb{Z}^n &amp; \searrow &amp; &amp; N \\
\searrow &amp; &amp; &amp; \searrow \\
a = (a_1, \dots, a_n) &amp; \to &amp; \lambda_a : \mathbb{C}^* &amp; \to (\mathbb{C}^*)^n \\
&amp; &amp; \searrow &amp; \searrow \\
&amp; &amp; t &amp; \to (t^a_1, \dots, t^a_n).
\end{array}
$$

M and N are dual to each other by the pairing

$$
\begin{array}{l}
&lt; , &gt; : M \times N \longrightarrow \mathbb{Z} \\
\searrow \quad \searrow \\
(r, a) \quad \to \quad \mathbb{1}r_ia_1 \quad \text{or} \quad \chi^r(\lambda_a(t)) = t^{&lt;r, a&gt;}.
\end{array}
$$

(6.2) There are natural isomorphisms

1. $N \downarrow \pi_1(T) \simeq H_1(T, \mathbb{Z})$,

2. $N \otimes \mathbb{C} \downarrow$ the universal covering space of $T$.

3. $N \otimes \mathbb{C}/N \downarrow T$,

4. $N \otimes \mathbb{C} \longrightarrow N \otimes \mathbb{C}/N$ : the covering map

$$
\begin{array}{c c c}
\parallel &amp; &amp; \parallel \\
\mathbb{C}^n &amp; \xrightarrow{\varrho} &amp; (\mathbb{C}^*)^n \\
\searrow &amp; &amp; \searrow \\
z = (z_1, \dots, z_n) \to \varrho(z) = (\varrho(z_1), \dots, \varrho(z_n))
\end{array}
$$

where $\varrho( ) = \exp(2\pi\sqrt{-1( )})$.

We write $N_{\mathbb{C}} = N \otimes \mathbb{C}$, $N_{\mathbb{R}} = N \otimes \mathbb{R}$, $M_{\mathbb{R}} = M \otimes \mathbb{R}$.

As a real analytic group

40

$$
\begin{array}{l}
N_{\mathbb{C}} / N \quad \stackrel{\circ}{\rightarrow} \quad (N_{\mathbb{R}} / N) \times N_{\mathbb{R}} \\
\downarrow \quad \downarrow \\
x + \sqrt{-1} y \bmod N \rightarrow (x \bmod N, y).
\end{array}
$$

In particular the projection onto the imaginary part

$$
\operatorname{Im}: T = N_{\mathbb{C}} / N \rightarrow N_{\mathbb{R}}
$$

is an epimorphism of real analytic groups whose kernel is a real compact torus.

**Definition (6.3).**

1. An *affine torus embedding* (resp.
   a *torus embedding*) of $T$, $X$, is an affine $\mathbb{C}$-scheme (resp.
   a $\mathbb{C}$-scheme) such that
2. $X$ contains $T$ as a Zariski open dense subset;
3. $T$ acts on $X$ extending the natural action on itself defined by translation.
4. Let $X$ (resp.
   $X'$) be a torus embedding of $T$ (resp.
   $T'$). A *morphism* $f: X \to X'$ of *torus embeddings* is a morphism of $\mathbb{C}$-schemes such that
5. $f(T) = T'$,
6. $g = f|_{T}: T \to T'$ is a homomorphism of groups, hence the diagram

$$
\begin{array}{c}
T \times X \to X \\
(g, f) \Big{\downarrow} \qquad \qquad \Big{\downarrow} f \\
T' \times X' \to X'
\end{array}
$$

commutes where the horizontal arrows denote the action of $T$ and $T'$ on $X$ and $X'$ respectively.

**Definition (6.4).**

1. A cone $\sigma$ in $N_{\mathbb{R}}$ (or $M_{\mathbb{R}}$) is called a *convex rational polyhedral cone* (abbreviated to a *c.r.p. cone*) if
   $$
   \begin{array}{r l}
   \sigma &amp; = (a \in N_{\mathbb{R}} \text{ (or } M_{\mathbb{R}}) \text{; } \langle r_i, a \rangle \geq 0, i = 1, \dots, m, \\
   &amp; \text{with } r_i \in M \text{ (or } N).
   \end{array}
   $$
2. A (*finite*) rational partial polyhedral decomposition (abbr.

41

to an $(f.)$ r.p.p. decomposition) of $\mathbf{N}*{\mathbb{R}}$ is a (finite) collection $\Sigma = \{\sigma*{\alpha}\}$ of c.r.p. cones in $\mathbf{N}_{\mathbb{R}}$ such that

0. $\sigma_{\alpha}$ contains no linear subspaces;

1. if $\sigma$ is a face of $\sigma_{\alpha} \in \Sigma$ (we write $\sigma \prec \sigma_{\alpha}$), then $\sigma \in \Sigma$;

2. for $\sigma_{\alpha}, \sigma_{\beta} \in \Sigma, \sigma_{\alpha} \cap \sigma_{\beta} \prec \sigma_{\alpha}, \prec \sigma_{\beta}$.

iii) Let $\Sigma$ (resp.
$\Sigma'$) be an r.p.p. decomposition of $\mathbb{N}$ (resp.
$\mathbb{N}'$). A morphism $\psi : \Sigma \to \Sigma'$ of r.p.p. decompositions is a linear map $\psi : \mathbb{N} \to \mathbb{N}'$ with finite cokernel such that for $\sigma \in \Sigma$ there is a $\sigma' \in \Sigma'$ with $\psi_{\mathbb{R}}(\sigma) \subset \sigma'$ where $\psi_{\mathbb{R}} = \psi \otimes \mathbb{R} : \mathbb{N}*{\mathbb{R}} \to \mathbb{N}*{\mathbb{R}}'$.

Thus r.p.p. decompositions form a category.

iv) By the correspondence $\sigma \to \Sigma(\sigma) = \{\sigma \text{ and its faces}\}$ the set of c.r.p. cones can be considered as a full subcategory of the category of r.p.p. decompositions.

```
Category of r.p.p. decompositions
```

Category of f.r.p.p. decompositions

Category of c.r.p. cones.

**Notation (6.5).** Let $\sigma$ be a c.r.p. cone in $\mathbf{N}_{\mathbb{R}}$.
Then the dual cone of $\sigma$ is defined to be

$$
\hat{\sigma} = \{r \in \mathbf{M}_{\mathbb{R}} : \langle r, a \rangle \geq 0 \text{ for } \forall a \in \sigma\}.
$$

(6.6) Let $S$ be a subsemigroup of $M$ containing 0. Then the $\mathbb{C}$-vector space

$$
\mathbb{C}[S] = \mathbb{C}[x^r]_{r \in S} \subset \mathbb{C}[T_1, T_1^{-1}, \dots, T_n, T_n^{-1}] = \mathbb{C}[M]
$$

generated by $x^r, r \in S$, is a subring of $\mathbb{C}[M]$.

The following claims hold.

i) For a subset $I$ of $S$,

$$
\{r_i\}_{i \in I} \text{ generates } S \text{ as a semigroup}
$$

$$
\ll \left\{x^{r_1}\right\}_{1 \in I} \text{ generates } \mathbb{C}[S] \text{ as a ring.}
$$

ii) $\dim \operatorname{Spec}(\mathbb{C}[S]) = \dim$ dimension of the $\mathbb{R}$-vector space generated by $S$ in $\mathbf{M}_{\mathbb{R}}$.

42

iii) Denote the quotient field of an integral domain $R$ by $Q(R)$, Then

$$Q(\mathbb{C}[S]) = Q(\mathbb{C}[M]) \iff S \text{ generates } M \text{ as a group.}$$

In this case $\operatorname{Spec}(\mathbb{C}[S])$ is an affine torus embedding by $\mathbb{C}[S] \subset \mathbb{C}[M]$.
Conversely all affine torus embeddings can be constructed in this way.

iv) Suppose that $S$ generates $M$ as a group.
Then

$$\mathbb{C}[S] \text{ is normal } \iff S \text{ is saturated, i.e. for } r \in M, \ n \in \mathbb{N}$$

$$\text{nr} \in S \implies r \in S.$$

**Theorem (6.7).** There are equivalences of categories:

```
{r.p.p. decompositions of N} &lt;—&gt; {normal torus embeddings of T locally of finite type}
u
}
{f.r.p.p. decompositions of N} &lt;—&gt; { " of finite type}
u
}
{c.r.p. cones in N} &lt;—&gt; {affine normal torus embeddings of T of finite type}
```

where the last correspondence is given by

$$\sigma \to X_{\sigma} = \operatorname{Spec}(\mathbb{C}[\hat{\sigma} \cap M])$$

and the property,

$$\sigma \cap M = \{a \in N; \ E_{\lim_{t \to 0} \lambda_a(t)} \in X_{\sigma}\}.$$

The proof is based on the following two facts (6.8), (6.10).

**Proposition (6.8).** For c.r.p. cones $\sigma, \tau$

1. $$\tau \subset \sigma \iff X_{\tau} \to X_{\sigma} \text{ homomorphism};$$ u u T = T

43

2. $\tau &lt; \sigma &lt; \Rightarrow X_{\tau} \subset X_{\sigma}$ open immersion

$$
\begin{array}{cc}
\upsilon &amp; \upsilon \\
T &amp; = T.
\end{array}
$$

Proof.

1. $\tau \subset \sigma &lt; \Rightarrow \hat{\tau} &gt; \hat{\sigma}$

$$
\begin{array}{l}
&lt; \Rightarrow \mathbb{C}[M] &gt; \mathbb{C}[\hat{\tau} \cap M] &gt; \mathbb{C}[\hat{\sigma} \cap M] \\
&lt; \Rightarrow X_{\tau} \to X_{\sigma} \\
\begin{array}{cc}
\upsilon &amp; \upsilon \\
T &amp; = T.
\end{array}
\end{array}
$$

2. Similar.

**Corollary (6.9).** Given an r.p.p. decomposition $\Sigma = \{\sigma_{\alpha}\}$, the affine torus embeddings $X_{\sigma_{\alpha}}$ patches together to form a torus embedding $X_{\Sigma} = \upsilon_{\alpha} X_{\sigma_{\alpha}}$ by $X_{\sigma_{\alpha}} \subset X_{\sigma_{\beta}}$ for $\sigma_{\alpha} &lt; \sigma_{\beta}$.

Hence we have a morphism of categories $\Sigma \to X_{\Sigma}$.

**Theorem (6.10) (Sumihiro [32]).** If $T$ acts on a normal variety $X$ locally of finite type, then $X$ is covered with affine $T$-invariant open subsets.

This theorem implies that the correspondence $\Sigma \to X_{\Sigma}$ is an equivalence of categories.

**Remark (6.11).** i) Sumihiro proved only for the case of finite type.
But Ishida pointed out that the claim can be strengthened as above with a fact that, if an algebraic group acts on $X$ locally of finite type, then $X$ is covered with $G$-stable open sets which are of finite type.

ii) The claim (6.10) does not hold unless $X$ is normal and the action is algebraic.
For example $T = \mathbb{C}^*$ acts naturally on a rational curve with one node $\mathbb{P}^1 / \{0\} = \{\infty\}$, and the node has no $T$-stable affine open neighbourhood (remarked by Prof. Matsumura).
On the other hand $T = \mathbb{C}^*$ acts on elliptic curves $\mathbb{C}^* / \mathbb{Z}$ analytically, which however has no $T$-stable open affine subsets.

The action of $T$ on $X_{\Sigma}$ determines an orbit decomposition whose structure can be described in terms of $\Sigma$ as follows.

44

## Proposition (6.12)

Let $\Sigma$ be an r.p.p. decomposition and $X_{\Sigma}$ the corresponding torus embedding of $T$.
Then there is a bijective correspondence

$$
\begin{aligned}
\Sigma &amp;&lt;\longrightarrow \quad \text{(T-orbits in } X_{\Sigma}) \\
\oplus &amp;&amp;\oplus \\
\sigma &amp;\to &amp; \circ_{\sigma}
\end{aligned}
$$

such that

1. for $a \in N$

$$
a \in \sigma^{\circ} \iff \lim_{t \to 0} \lambda_{a}(t) \in \circ_{\sigma}
$$

where $\sigma^{\circ}$ denotes the relative interior of $\sigma$, i.e. $\sigma - \upsilon$ proper faces of $\sigma$.
Here the limit in the right hand side does not depend on a (cf.
(6.13));

2. $\sigma \prec \tau \iff (\circ_{\sigma})^{-} &gt; \circ_{\tau}$;

3. dim $\sigma + \dim \circ_{\sigma} = n = \dim T$;

4. $\circ_{\{0\}} = T$.

5. Elementary description of $X_{\sigma}$.

a) Construction of $X_{\sigma}$.

Let $\sigma$ be a c.r.p. cone and suppose that

$$
\hat{\sigma} \cap M = \mathbb{Z}r_{1} + \cdots + \mathbb{Z}r_{m},
$$

hence

$$
X_{\sigma} = \operatorname{Spec}(\mathbb{E}[X^{r_{1}}, \dots, X^{r_{m}}]).
$$

This is equivalent to say that with an immersion

$$
\begin{aligned}
T &amp;\xrightarrow{1} \mathbb{E}^{m} \\
\oplus &amp; \\
\underline{t} &amp;\to (X^{r_{1}}(\underline{t}), \dots, X^{r_{m}}(\underline{t}))
\end{aligned}
$$

$X_{\sigma}$ is the scheme-theoretic closure of $i(T)$ in $\mathbb{E}^{m}$.
$T$ acts on $X_{\sigma}$ as

45

$$
\underline{t} \cdot \underline{x} = (x^{r_1}(\underline{t})x_1, \dots, x^{r_m}(\underline{t})x_m)
$$

for $\underline{t} \in \mathbb{T}$ and $\underline{x} = (x_1, \dots, x_m) \in \mathbb{X}_\sigma \subset \mathbb{C}^m$.

b) Orbit decomposition.

First note that

to choose $\tau &lt; \sigma \iff$ to give a subset $N(\tau)$ of $\{r_1, \dots, r_n\}$ s.t. $N(\tau) \ni r_1 \iff r_1, \dots, r_n$, and

$$
\tau &lt; \tau' \iff N(\tau) \ni N(\tau'),
$$

$$
a \in \tau \iff r_1, a \ni 0 \text{ for } r_1 \in N(\tau),
$$

$$
a \in \tau' \iff r_1, a \ni 0 \text{ for } r_1 \in N(\tau),
$$

$$
\vee r_1 \in N(\tau),
$$

and

$$
r_1, a \ni 0 \text{ for } r_1 \notin N(\tau).
$$

If $a \in \tau'$,

$$
i \circ \lambda_a(t) = (t^{<r_1, a="">}, \dots, t^{<r_m, a="">}) \quad (6.1),
$$

hence

$$
\lim_{t \to 0} \lambda_a(t) = (\lambda_1), \quad \lambda_1 = 1 \quad \text{if } r_1 \in N(\tau),
$$

$$
= 0 \quad \text{if } r_1 \notin N(\tau).
$$

Therefore we have

$$
0_\tau = \{(x_1) \in \mathbb{X}_\sigma \mid x_1 \neq 0 \text{ if } r_1 \in N(\tau),
$$

$$
= 0 \quad \text{if } r_1 \notin N(\tau)\},
$$

and</r_m,></r_1,>

46

$$
(O_{\tau})^{-} = \left\{ (x_i) \in X_{\sigma} ; x_i = 0 \text{ if } r_i \notin N(\tau) \right\}.
$$

c) Defining equation of $X_{\sigma}$.

Let $\{s_1, \dots, s_k\}$ be a generator of relations of $\{r_i\}$, i.e. a generator of the kernel of a homomorphism

$$
\begin{array}{c c c}
\mathbb{Z}^m &amp; \longrightarrow &amp; M \\
\downarrow &amp; &amp; \downarrow \\
(a_1, \dots, a_m) &amp; \rightarrow &amp; \sum_{i=1}^{m} a_i r_i.
\end{array}
$$

For each $s_j = (a_1^{(j)}, \dots, a_m^{(j)})$ put

$$
b_1^{(j)} = \max\{a_1^{(j)}, 0\}, \quad c_1^{(j)} = \max\{-a_1^{(j)}, 0\}.
$$

Then the ideal $I$ in $\mathbb{C}[X_1, \dots, X_m]$ defining $X_{\sigma}$ is generated by

$$
f_j(X) = \prod_{i=1}^{m} X_i^{b_1^{(j)}} - \prod_{i=1}^{m} X_i^{c_1^{(j)}},
$$

i.e.

$$
\mathbb{C}[X_1, \dots, X_m]/(f_1, \dots, f_s) \cong \mathbb{C}[X^r_1, \dots, X^r_m].
$$

Some geometric properties of $X_{\Sigma}$ can be expressed also in terms of those of $\Sigma$.

**Proposition (6.14).**

1. For a c.r.p. cone $\sigma$, $X_{\sigma}$ is nonsingular iff $\sigma$ is given by a part of a basis of $N$.
   (We call such $\sigma$ *regular*.) In particular in this case $\sigma$ is a cone over a simplex.

2. $X_{\Sigma}$ is proper iff $\Sigma$ is finite and $N_{\mathbb{R}} = \upsilon \sigma_{\alpha}$.

3. $X_{\Sigma}$ is quasi-projective iff $\Sigma$ is finite and there is a real convex function on the convex hull of $\upsilon \sigma_{\alpha}$ such that

i) $f$ is continuous;

ii) $f$ is $\mathbb{R}$-linear on $\sigma_{\alpha}$;

iii) $f(N \cap \upsilon \sigma_{\alpha}) \subset \mathbb{Z}$;

iv) for each $\sigma_{\alpha}$ there are $r_i \in M$ and $n_i &gt; 0$ such that $n_i f \geq r_i$ on $\upsilon \sigma_{\alpha}$ and $\sigma_{\alpha} = \{a \in N_{\mathbb{R}}; \langle r_i, a \rangle = n_i f(a)\}$.
(We call such $f$ *a polar function*.)

47

In this case $f$ defines a T-invariant ample invertible sheaf on $X_{\mathbb{I}}$.

**Example (6.15).** 1) Affine space $\mathbb{T}^n$.

$$
\begin{aligned}
\sigma &amp;= \{(a_1, \dots, a_n) \mid a_1 \geq 0\}, \\
\hat{\sigma} \cap M &amp;= \{(r_1, \dots, r_n) \in \mathbb{Z}^n \mid r_1 \geq 0\} \\
&amp;= \sum_{i=1}^{n} Ze_i, \ e_i = (0, \dots, 0, \overset{i}{\underset{1}{=}}, 0, \dots, 0), \ x^{\ e_1} = T_1.
\end{aligned}
$$

$$
\begin{aligned}
X_{\sigma} &amp;= \operatorname{Spec}(\mathbb{T}[T_1, \dots, T_n]) \\
&amp;= \mathbb{T}^n = \{(z_1, \dots, z_n) \mid z_1 \in \mathbb{T}\} \\
&amp;= \left(\mathbb{T}^*\right)^n = \{(z_1, \dots, z_n) \mid z_1 \neq 0\}.
\end{aligned}
$$

The action of $T$ on $X_{\sigma}$ is given by the coordinatewise multiplication (cf.
(6.13) a)).

For a subset $I$ of $\{1, \dots, n\}$,

$$
\sigma_I = \{(a_1) \mid a_1 = 0 \text{ for } i \in I\}
$$

is a face of $\sigma$.
We have

$$
N(\sigma_I) = \{e_1 \mid i \in I\} \quad \text{((6.13) b)}
$$

since $<e_1, a=""> = a_1$, and

$$
\begin{aligned}
O_{\sigma_I} &amp;= \{(z_1, \dots, z_n) \mid z_1 \neq 0 \text{ if } i \in I \\
&amp;= 0 \text{ if } i \notin I\}.
\end{aligned}
$$

2. Projective space, $\mathbb{P}^n$.

$$
\begin{aligned}
\mathbb{P}^n &amp;= \{(u_0 : u_1 : \dots : u_n)\} \text{ homogeneous coordinates} \\
\mathbb{T}^n &amp;= \{u = (u_1) \mid u_1 \neq 0\} \approx (\mathbb{T}^*)^n = \{(u_1 / u_0, \dots, u_n / u_0)\}.
\end{aligned}
$$</e_1,>

48

The action of  $\mathbf{T}$  on  $\mathbb{P}^n$  is defined by the coordinatewise multiplication.
$$

\Sigma = \left\{\sigma* {0}, \sigma* {1}, \dots , \sigma\_ {n} \text{ and their faces} \right\}

$$

where
$$

\sigma* {0} = \left\{\left(a * {1}, \dots , a _ {n}\right) \in \mathbb {R} ^ {n}; a _ {1} \geq 0 \right\},

$$
$$

\sigma* {k} = \left\{\left(a * {1}, \dots , a _ {n}\right) \in \mathbb {R} ^ {n}; - a _ {k} \geq 0, a _ {1} - a _ {k} \geq 0 \text{ for } \forall\_ {i} \right\},

$$
$$

k = 1, \dots , n.

$$

For example  $n = 2$

![img-10.jpeg](img-10.jpeg)
$$

\hat {\sigma} _ {0} \cap M = \sum_ {i = 1} ^ {n} \mathbb {N} e \_ {i}, \quad (\text{cf.1})

$$
$$

\hat {\sigma} _ {k} \cap M = \mathbb {N} (- e _ {k}) \oplus \sum* {i = 1} ^ {n} \mathbb {N} (e * {i} - e \_ {k}), \quad k = 1, \dots , n.

$$
$$

x _ {\sigma_ {0}} = \operatorname {Spec} \left(\mathbb {C} \left[ T _ {1}, \dots , T _ {n} \right]\right),

$$
$$

x _ {\sigma_ {k}} = \operatorname {Spec} \left(\mathbb {C} \left[ T _ {k} ^ {- 1}, T _ {1} T _ {k} ^ {- 1}, \dots , T _ {n} T _ {k} ^ {- 1} \right]\right), \quad k = 1, \dots , n.

$$
$$

\mathbb {P} ^ {n} = \operatorname {Proj} \left(\mathbb {C} \left[ U _ {0}, \dots , U _ {n} \right]\right),

$$
$$

\begin{array}{l} \left(\mathbb {P} ^ {n}\right) _ {u _ {0}} = \{u = (u _ {1}); u _ {0} \neq 0 \} \\
= \operatorname {Spec} \left(\mathbb {C} \left[ U _ {1} / U _ {0}, \dots , U _ {n} / U _ {0} \right]\right) \\
\end{array}

$$
$$

x _ {\sigma_ {0}} = \operatorname {Spec} \left(\mathbb {C} \left[ T _ {1} \right]\right) \quad \text{with} \quad T _ {1} = U _ {1} / U \_ {0}.

$$

49

Then
$$

\begin{array}{l} \left(\mathbb{P}^{n}\right)*{u*{k}} = \{u = \left(u*{1}\right); u*{k} \neq 0\} \\
= \operatorname{Spec}\left(\mathbb{C}\left[\mathrm{U}*{0} / \mathrm{U}*{k}, \dots, \mathrm{U}*{n} / \mathrm{U}*{k}\right]\right) \\
\end{array}

$$
$$

x*{\sigma*{k}} \quad \text{as above}.

$$

Hence
$$

\mathbb{P}^{n} \nsubseteq x\_{\Sigma}.

$$

3) Cyclic quotient singularity and its resolution.

a) Let $\zeta = \exp(2\pi \sqrt{-1/p})$ be a primitive $p$-th root. Then the map
$$

\begin{array}{l} g: \mathbb{C}^{n} \longrightarrow \mathbb{C}^{n} \\
\downarrow \\
\left(z*{1}, \dots, z*{n}\right) \longrightarrow \left(\zeta^{a*{1}} z*{1}, \dots, \zeta^{a*{n}} z*{n}\right) \end{array}

$$

generates a finite cyclic group $G = \langle g \rangle$ of automorphisms of $\mathbb{C}^{n}$ of order $p$. The quotient space
$$

X = \mathbb{C}^{n}/G

$$

has a normal singularity at $o = 0$ mod $G$ called cyclic quotient singularity. It is isolated for example if $(a_{1}, \dots, a_{n}) = 1$, and $a_{i} \neq 0$ (p).

Put
$$

\begin{array}{l} \pi: M = ZZ^{n} \longrightarrow ZZ/pZZ \\
\downarrow \\
\alpha = (\alpha*{1}, \dots, \alpha*{n}) \rightarrow \langle \alpha, a \rangle = \Sigma \alpha*{1} a*{1} \bmod p. \end{array}

$$

Then $M = \operatorname{Ker}(\pi)$ is again a free abelian group of rank $n$. Consider the transpose of the inclusion map $i: M \subset \mathring{M}$,
$$

j = {}^{t}i: \mathring{N} \approx \operatorname{Hom}(\mathring{M}, ZZ) \rightarrow N = \operatorname{Hom}(M, ZZ).

$$

50

and put
$$

\hat{\sigma} = \{t = (t*1, \dots, t_n) \in \mathbb{N}*{\mathbb{R}}; t*1 \geq 0, i = 1, \dots, n\} \in \mathbb{N}*{\mathbb{R}}

$$

and
$$

\sigma = j*{\mathbb{R}}(\hat{\sigma}) \in \mathbb{N}*{\mathbb{R}}.

$$

Then we have
$$

X \ni X\_\sigma

$$

and $j: \mathbb{N} \to \mathbb{N}$ corresponds to the canonical surjection
$$

p: \mathbb{C}^n \left(= X\_{\hat{\sigma}}\right) \to X.

$$

b) (Hirzebruch's method of resolution of quotient singularity of dimension 2 [14])

We consider the case $n = 2$, and
$$

\begin{array}{l} g: \mathbb{C}^2 \longrightarrow \mathbb{C}^2 \\
\downarrow \\
(z_1, z_2) \rightarrow (\zeta z_1, \zeta^q z_2), (p, q) = 1. \end{array}

$$

(It is easily seen that for $n = 2$ we have not lost generality by this assumption.) We want to obtain a resolution of the quotient singularity
$$

X = \mathbb{C}^2 / \langle g \rangle \gg 0.

$$

By the above a)
$$

X \ni X\_\sigma

$$

with $\sigma = \mathbb{R}_+(0,1) + \mathbb{R}_+(p, -q)$ (by choosing a basis of $\mathbb{N}$ suitably).

Define non-negative integers $\lambda_1$ and $\mu_1$ inductively by the following relations.

51
$$

\begin{array}{l} \lambda*0 = p, \lambda_1 = q, \\
\lambda_0 = b_1 \lambda_1 - \lambda_2, \; 0 \leq \lambda_2 &lt; \lambda_1, \; 1 &lt; b_1, \\
\lambda_1 = b_2 \lambda_2 - \lambda_3, \; 0 \leq \lambda_3 &lt; \lambda_2, \; 1 &lt; b_2, \\
\vdots \\
\lambda*{s-2} = b*{s-1} \lambda*{s-1} - \lambda*s, \; \lambda_s = 1, \\
\lambda*{s-1} = b*s \lambda_s - \lambda*{s+1}, \; \lambda\_{s+1} = 0, \end{array}

$$

and
$$

\begin{array}{l} \mu*0 = 0, \; \mu_1 = 1, \\
\mu_k = b*{k-1} \mu*{k-1} - \mu*{k-2}. \end{array}

$$

Set moreover
$$

a_i = \mu_i, \; b_i = \frac{1}{p} (\lambda_i - q \mu_i).

$$

Then we see that

a) $(a_1, b_1) \in \mathbb{Z}^2$,

b) $a_1 b_{i+1} - a_{i+1} b_i = 1$,

c) $(a_0, b_0) = (0, 1), \; (a_1, b_1) = (1, 0), \; (a_{s+1}, b_{s+1}) = (p, -q)$.

We define a *subdivision* $\{\sigma_i\}$ of $\sigma$ as
$$

\sigma*i = \mathbb{R}*+ (a*i, b_i) + \mathbb{R}*+ (a*{i+1}, b*{i+1}), \; i = 0, \dots, s.

$$

Then $\Sigma = \{\sigma_i, \tau_j = \mathbb{R}_+ (a_j, b_j), \{0\}\}$ form a f.r.p.p. decomposition which is regular by $b$). The corresponding torus embedding $X_\Sigma$ together with the canonical map $p: X_\Sigma \to X_\sigma$ gives the minimal resolution of the quotient singularity $(X, \sigma)$. $p^{-1}(\sigma)$ is a chain of non-singular rational curves $C_j = O(\tau_j)^{-}$ with $(C_j)^2 = -b_j$.

![img-11.jpeg](img-11.jpeg)

The number-theoretic meaning of this example is as follows. The above  $(\mathbf{b}_1)$  gives the development of  $\frac{\mathbf{q}}{\mathbf{p}}$  into continued fraction

![img-12.jpeg](img-12.jpeg)

and
$$

- \frac {b _ {1}}{a _ {1}} = \frac {1}{p} \left(\frac {\lambda* {1}}{\mu* {1}} - q\right)
  $$
  $$
gives the 1-th convergent of $q / p$ .

53

A similar torus embedding appears in constructing a resolution of cusp singularity in the Hilbert modular variety for a real quadratic number field in connection with the development of a real quadratic number into an infinite but recurring continued fraction ([24]).

(6.16) In order to study properties of $X_{\Sigma}$ in the classical topology it is convenient to introduce a topological quotient space $N_{\Sigma}$ of $X_{\Sigma}$ by the compact torus $c-T = N_{\mathbb{R}}/N$.
We denote by $\operatorname{Im}$ the canonical quotient map: $X_{\Sigma} \to N_{\Sigma}$ (cf.(6.2)).

$$
\operatorname{Im}: \begin{array}{c c c} X_{\Sigma} &amp; \to &amp; N_{\Sigma} \\ \upsilon &amp; &amp; \upsilon \end{array}
$$

$$
\operatorname{Im}: \mathrm{T} \quad \rightarrow \quad N_{\mathbb{R}}
$$

We can construct $N_{\Sigma}$ similarly as $X_{\Sigma}$ in two ways as follows.

A) First elementary construction.
This construction is analogous to (6.13). We use the notation there.

For a c.r.p. cone $\sigma$ in $\Sigma$ define an immersion of $N_{\mathbb{R}}$ as

$$
\begin{array}{c c c c c}
1: N_{\mathbb{R}} &amp; \longrightarrow &amp; (\mathbb{R}_{&gt;0})^m \\
\downarrow &amp; &amp; \downarrow \\
y &amp; \rightarrow &amp; (e^{-2\pi<r_{1}}, y="">, \dots, e^{-2\pi<r_{m}, y="">})
\end{array}
$$

and let

$$
N_{\Sigma} = \text{the closure of } 1(N_{\mathbb{R}}) \text{ in } (\mathbb{R}_{\geq 0})^m.
$$

$N_{\mathbb{R}}$ acts on $N_{\Sigma}$ as

$$
y \cdot \underline{y} = (e^{-2\pi<r_{1}}, y="">y_{1}, \dots, e^{-2\pi<r_{m}, y="">} y_{m}).
$$

for $y \in N_{\mathbb{R}}$ and $\underline{y} = (y_{1}, \dots, y_{m}) \in (\mathbb{R}_{\geq 0})^{m}$.

We have an $N_{\mathbb{R}}$-orbit decomposition $\underset{\tau \prec \sigma}{\sqcup} \overline{\sigma}*{\tau}$ of $N*{\sigma}$ as

$$
\begin{array}{l}
\overline{\sigma}_{\tau} = \{(y_{i}) \in N_{\sigma} \mid y_{i} \neq 0 \text{ if } r_{i} \in N(\tau) \\
= 0 \text{ if } r_{i} \notin N(\tau)\},
\end{array}
$$

and</r*{m},></r*{1}},></r*{m},></r*{1}},>

54

$$
(\overline{O}_\tau)^{-} = \{(y_1) \in N_\sigma; \, y_1 = 0 \text{ if } r_1 \neq N(\tau)\}.
$$

For $\epsilon_\tau = (\epsilon_1) \in \overline{O}*\tau$ with $\epsilon_1 = 1$ if $r_1 \in N(\tau)$, $r_1 \neq N(\tau)$ the stabilizer of $\epsilon*\tau$ is

$$
\begin{aligned}
L(\tau) &amp;= \text{the smallest linear space containing } \tau \\
&amp;= \underset{r_1}{\cap} \in N(\tau) \left\{ r_1 = 0 \right\},
\end{aligned}
$$

so we get

$$
\begin{array}{ccc}
N_{\mathbb{R}} / L(\tau) &amp; \stackrel{\circ}{\to} &amp; \overline{O}_\tau \\
\downarrow &amp; &amp; \downarrow \\
y \mod L(\tau) &amp; \to &amp; y \cdot \epsilon_\tau.
\end{array}
$$

Taking note of a commutative diagram

$$
\begin{array}{ccc}
T &amp; \xrightarrow{\text{Im}} &amp; N_{\mathbb{R}} \\
1 &amp; \cap &amp; \cap 1 \\
\underline{\mathfrak{C}}^m &amp; \xrightarrow{||} &amp; (\mathbb{R}_{\geq 0})^m \\
\downarrow &amp; &amp; \downarrow \\
(x_1, \dots, x_m) &amp; \to &amp; (|x_1|, \dots, |x_m|)
\end{array}
$$

(This diagram is commutative because

$$
|X^r(\underline{e}(\underline{z}))| = e^{-2\pi &lt; r, \text{ Im } \underline{z} &gt;}
$$

where $\underline{e} : N_{\underline{\mathfrak{C}}} \to T$ is the covering map (6.2).), we have an equivariant extension of the map "Im"

$$
\begin{array}{ccc}
\text{Im} : T &amp; \to &amp; N_{\mathbb{R}} \\
\cap &amp; &amp; \cap \\
\text{Im} : X_\sigma &amp; \to &amp; N_\sigma
\end{array}
$$

by which we can see

55

$$
N_{\sigma} \stackrel{\circ}{\to} X_{\sigma}/c-T
$$

and

$$
O_{\tau} = \text{Im}^{-1}(\overline{O}_{\tau}) \quad \text{for} \quad \tau &lt; \sigma.
$$

We can see easily that $N_{\sigma}$'s patch together naturally to form $N_{\Sigma}$ with an equivariant extension

$$
\begin{array}{c c c}
\text{Im}: T &amp; \to &amp; N_{\mathbb{R}} \\
\tilde{n} &amp; &amp; \tilde{n}
\end{array}
$$

$$
\text{Im}: X_{\Sigma} \to N_{\Sigma}
$$

by which $X_{\Sigma}/c-T \stackrel{\circ}{\to} N_{\Sigma}$.

B) Second coordinate-free construction.
We keep the notation in A). For $\tau \in \Sigma$ we define

$$
\overline{O}_{\tau} = N_{\mathbb{R}} / L(\tau)
$$

on which $N_{\mathbb{R}}$ acts naturally, and we put

$$
N_{\Sigma} = \prod_{\tau \in \Sigma} \overline{O}_{\tau}
$$

as a set.
$N_{\Sigma}$ contains $N_{\mathbb{R}}$ as $\overline{O}*{\{0\}}$ and $N*{\mathbb{R}}$ acts on $N_{\Sigma}$ naturally so that the above is the orbit decomposition.

The point is to define a suitable topology on $N_{\Sigma}$.
It is similar to the definition of the cylindrical topology in (5.7).

For $\tau \in \Sigma$ and $y \in N_{\mathbb{R}}$ we denote $y \bmod L(\tau)$ in $\overline{O}_{\tau}$ by $y + \infty \cdot \tau$.
This notation would be justified soon later.

Taking a fixed metric on $N_{\mathbb{R}}$, we denote by $B_{\varepsilon}$ the $\varepsilon$-ball around $0 \in N_{\mathbb{R}}$ for $\varepsilon &gt; 0$.
For $\varepsilon &gt; 0$ and $w \in L(\tau)$ we set

$$
U^{\circ}(y + \infty \cdot \tau; \varepsilon, w) = y + w + B_{\varepsilon} + \tau \subset N_{\mathbb{R}}
$$

and for $\tau' &lt; \tau$

$$
U^{\tau'}(y + \infty \cdot \tau; \varepsilon, w) = y + w + B_{\varepsilon} + \tau + \infty \cdot \tau' \subset \overline{O}_{\tau'}.
$$

Then a fundamental system of neighbourhoods of $y + \infty \cdot \tau \in \overline{O}$ is

56

given by

$$
\left\{U(y + \infty \cdot \tau ; \varepsilon, w) = \prod_{\tau' \leqslant \tau} U^{\tau'} (y + \infty \cdot \tau ; \varepsilon, w) \right\}_{(\varepsilon, w)}
$$

$(U^{\circ} = U^{\{0\}})$ where $\varepsilon$ and $w$ run through $\mathbb{R}_{+}$ and $L(\tau)$ respectively.
Such neighbourhood is called *typical*.

![img-13.jpeg](img-13.jpeg)

Then this topology is shown to coincide with the one induced from the map $\text{Im}: \mathbf{x}*{\Sigma} \to \mathbf{N}*{\Sigma}$.

Take a direct summand $\mathbf{N}*{\mathbb{R}}'$ of $L(\tau)$ in $\mathbf{N}*{\mathbb{R}}$ and write $y = y' + y''$, $y' \in \mathbf{N}*{\mathbb{R}}'$, $y'' \in L(\tau)$, for $y \in \mathbf{N}*{\mathbb{R}}$.
Given a sequence $\{y_n\}$ in $\mathbf{N}*{\mathbb{R}}$ and $y' \in \mathbf{N}*{\mathbb{R}}'$, we have with this topology

$$
\lim_{n \to \infty} y_n' = y' + \infty \cdot \tau \quad \text{in} \quad \mathbf{N}_{\Sigma}
$$

$$
\Leftrightarrow \lim_{n \to \infty} y_n' = y' \quad \text{in} \quad \mathbf{N}_{\mathbb{R}}' \quad \text{and for} \quad \forall w \in L(\tau) \, y_n'' \in w + \tau
$$

57

for $n \gg 0$ (cf.(5.9)).

Roughly speaking, $y + \infty \cdot \tau$ is the ideal point obtained by starting at $y$ and moving to infinity in the direction of $\tau$.

§7. Toroidal compactification due to Mumford.

## A) Construction of toroidal compactification.

### (7.1) We recall fundamental facts we use in this section (cf.

(4.6), (4.8), (5.2)).

$\mathcal{D} := \mathcal{D}_{\mathbf{g}}$, in general a hermitian bounded symmetric domain.

$G = \operatorname{Aut}(\mathcal{D}) := \operatorname{Sp}(g, \mathbb{R}) / \pm 1$, a semisimple real algebraic group defined over $\mathbb{Q}$.

$\Gamma \subset G$, an arithmetic subgroup (1.7).

$\mathcal{D}^{-} = \mathcal{D} \amalg \Pi_{\alpha} F_{\alpha}, F_{\alpha}: \text{boundary component} (= \mathcal{D}_{\mathbf{g}'}, 0 \leq \mathbf{g}' &lt; \mathbf{g})$ (4.2).

$\mathcal{D}^{\perp} \left( \subset \mathcal{D}^{-} \right) = \mathcal{D} \amalg \Pi_{\alpha, \text{rational}} F_{\alpha}, \text{rational closure} \quad (4.15)$.

### I.

$P_{\alpha} = \{g \in G; gF_{\alpha} = F_{\alpha}\}$, the parabolic subgroup associated with $F_{\alpha}$.

$W_{\alpha} = \text{the unipotent radical of } P_{\alpha}$.

$U_{\alpha} = \text{the centre of } W_{\alpha}$.

$\Omega_{\alpha}: \text{a self-dual open cone}$.

$G_{h}(F_{\alpha}), G_{\ell}(F_{\alpha}) \subset P_{\alpha}$ (4.9).

1. $P_{\alpha} \simeq (G_{h}(F_{\alpha}) \times G_{\ell}(F_{\alpha})) \cdot W_{\alpha}$ (modulo finite group).

2. $p_{h}: P_{\alpha} \to G_{h}(F_{\alpha}) \simeq \operatorname{Aut}(F_{\alpha})$,

$$
p_{\ell}: P_{\alpha} \rightarrow G_{\ell}(F_{\alpha}) \simeq \operatorname{Aut}(U_{\alpha}, \Omega_{\alpha}) \quad (\subset \operatorname{GL}(U_{\alpha}))
$$

(G$*{\ell}(F*{\alpha})$ acts on $U_{\alpha}$ by conjugation.)

3. $0 \to U_{\alpha} \to W_{\alpha} \to V_{\alpha} \to 0$

where $V_{\alpha}$ is a vector group.

### II.

1. $\mathcal{D}(F_{\alpha}) = U_{\alpha, \mathbb{C}} \cdot \mathcal{D} \simeq F_{\alpha} \times V_{\alpha} \times U_{\alpha, \mathbb{C}}$

$$
\pi_{\alpha} \left\{
\begin{array}{l}
+ \pi'_{\alpha} \\
\mathcal{D}(F_{\alpha})' = \mathcal{D}(F_{\alpha}) / U_{\alpha, \mathbb{C}} \\
+ \\
F_{\alpha}
\end{array}
\right.
\quad \text{and} \quad
\begin{array}{l}
+ \\
+ \\
F_{\alpha}
\end{array}
\quad \text{and}
\quad
\begin{array}{l}
+ \\
+ \\
F_{\alpha}
\end{array}
\quad .
$$

59

$$
\pi_{\alpha} : \mathcal{D}(F_{\alpha}) \to F_{\alpha}
$$

$$
\uparrow \quad \uparrow \quad \text{action}
$$

$$
p_{h} : P_{\alpha} \quad \rightarrow \quad G_{h} \approx \operatorname{Aut}(F_{\alpha}).
$$

(equivariant action)

2. $\Phi_{\alpha} : \mathcal{D}(F_{\alpha}) = P_{\alpha} \cdot U_{\alpha, \mathbb{C}} / (P_{\alpha} \cap K) \to P_{\alpha} \cdot U_{\alpha, \mathbb{C}} / P_{\alpha} \approx U_{\alpha}$

$$
\begin{array}{c}
\text{U} \\
\mathcal{D} \\
\uparrow
\end{array}
\quad \xrightarrow{\text{Im}} \quad
\begin{array}{c}
\text{U} \\
\mathcal{D}_{\alpha} \\
\uparrow \\
\end{array}
$$

$$
p_{\ell} : P_{\alpha} \quad \xrightarrow{\text{Aut}(U_{\alpha}, \Omega_{\alpha})} \quad G_{\ell}(F_{\alpha}) \approx \operatorname{Aut}(U_{\alpha}, \Omega_{\alpha})
$$

(equivariant action).

$$
\Phi_{\alpha}^{-1}(\Omega_{\alpha}) = \mathcal{D}.
$$

3. $(\pi_{\alpha}', \Phi_{\alpha}) : \mathcal{D}(F_{\alpha}) / U_{\alpha} \approx \mathcal{D}(F_{\alpha})' \times U_{\alpha}$ (real analytically).

For explicit description of these maps see (4.8) and (5.4).

**Notation (7.2).**

$$
\Gamma_{\alpha} := \Gamma \cap P_{\alpha}.
$$

$$
\Gamma_{\alpha}' := \Gamma_{\alpha} \cap \operatorname{Ker} p_{\ell}, \quad p_{\ell} : P_{\alpha} \to G_{\ell}(F_{\alpha}).
$$

$$
\overline{F}_{\alpha} := p_{\ell}(\Gamma_{\alpha}) \underset{\text{mod finite}}{\overset{\text{c}}{\text{}}} \operatorname{Aut}(U_{\alpha}, \Omega_{\alpha}), \text{ arithmetic subgroup}.
$$

Hence we have

$$
\begin{array}{l}
l \to \Gamma_{\alpha}' \to \Gamma_{\alpha} \to \overline{F}_{\alpha} \to l. \\
U_{\alpha} := \Gamma \cap U_{\alpha}, \text{ lattice in } U_{\alpha}. \\
W_{\alpha} := \Gamma \cap W_{\alpha}. \\
W_{\alpha} / U_{\alpha} \subset V_{\alpha}, \text{ lattice.}
\end{array}
$$

**Definition (7.3).** i) $\overline{F}*{\alpha}$-admissible polyhedral decomposition of $\Omega*{\alpha}$, $\Sigma_{\alpha} = \{\sigma_{\mu}\}$

&lt;=&gt; with introducing a rational structure on $U_{\alpha}$ by $U_{\alpha}$,

0. $\sigma_{\mu}, \text{ c.r.p. cone in } \overline{\Omega}_{\alpha}$;

1. $\sigma_{\mu} \in \Sigma_{\alpha}, \sigma_{\mu} \succ \sigma \Rightarrow \sigma \in \Sigma_{\alpha}$;

2. $\sigma_{\mu}, \sigma_{\nu} \in \Sigma_{\alpha} \Rightarrow \sigma_{\mu} \cap \sigma_{\nu} \prec \sigma_{\mu}, \sigma_{\nu}$;

(0), 1), 2) &lt;=&gt; $\Sigma_{\alpha}$ is an r.p.p. decomposition of $U_{\alpha}$)

3. $\gamma \in \overline{F}*{\alpha}, \sigma*{\mu} \in \Sigma_{\alpha} \Rightarrow \gamma \sigma_{\mu} \in \Sigma_{\alpha}$;

4. the number of classes of cones modulo $\overline{F}_{\alpha}$ is finite;

5. $\Omega_{\alpha} \subset \underset{\mu}{\cup} \sigma_{\mu}$ (= $\Omega_{\alpha}^2$ : rational closure).

60

ii) $\Gamma$-admissible family of polyhedral decompositions

$$
\Sigma = \{\Sigma_{\alpha}\}_{\mathrm{F}_{\alpha}:\text{rational}} \iff 0) \quad \Sigma_{\alpha} : \overline{\Gamma}_{\alpha}\text{-admissible polyhedral decomposition of } \Omega_{\alpha};
$$

1. for $\gamma \in \Gamma$, $\gamma \Sigma_{\alpha} = \Sigma_{\beta}$, if $\gamma F_{\alpha} = F_{\beta}$, by the map

$$
\gamma : U_{\alpha} \longrightarrow U_{\beta}
$$

$$
\downarrow \quad \downarrow
$$

$$
g \longrightarrow \gamma g \gamma^{-1};
$$

2. for $F_{\alpha} &lt; F_{\beta}$ (i.e. $F_{\alpha} \subset \overline{F}*{\beta}$, then $U*{\alpha} &gt; U_{\beta}$) $\Sigma_{\beta}$ is the restriction of $\Sigma_{\alpha}$ on $U_{\beta}$.

**Main Theorem (7.4) (Weak form).**

Given a $\Gamma$-admissible family of decompositions, we can construct a compactification $(\Gamma \backslash D)^{\nabla}$ of $\Gamma \backslash D$ and a holomorphic map

$$
p : (\Gamma \backslash D)^{\nabla} \rightarrow (\Gamma \backslash D)^{\eta}
$$

whose restriction on $\Gamma \backslash D$ is the identity map.

**(7.5) Steps of construction.**

1. 1st partial quotient (by $U_{\alpha}$);
2. partial compactification (with $\Sigma_{\alpha}$);
3. 2nd partial quotient (by $\Gamma_{\alpha}$);
4. gluing.

**(7.6) Step 1. Take the quotient of $D$ by $U_{\alpha}$.**

We have then the following commutative diagram.

$$
\Omega_{\alpha} \subset U_{\alpha}
$$

$$
\uparrow \quad \uparrow \uparrow
$$

$$
U_{\alpha} \backslash D \subset U_{\alpha} \backslash D(F_{\alpha}) \quad \text{or} \quad F_{\alpha} \times V_{\alpha} \times (U_{\alpha}, \mathfrak{m}/U_{\alpha})
$$

$$
\downarrow \quad \downarrow \quad \overline{\pi}_{\alpha}^{\prime} \quad \downarrow
$$

$$
D(F_{\alpha})^{\prime} = D(F_{\alpha})^{\prime} \quad \text{or} \quad F_{\alpha} \times V_{\alpha}
$$

where $\overline{\pi}*{\alpha}^{\prime}$ is a principal fibre bundle with an algebraic torus $T*{\alpha} = U_{\alpha}, \mathfrak{m}/U_{\alpha}$ as fibre.

61

Observe that in each fibre

$$
1 \rightarrow U_{\alpha} / U_{\alpha} \rightarrow T_{\alpha} \stackrel{\phi}{\rightarrow} U_{\alpha} \rightarrow 1
$$

and recall the canonical identifications (6.2)

$$
U_{\alpha} \stackrel{\sim}{\rightarrow} \operatorname{Hom}(\mathfrak{S}_{m}, T_{\alpha}) \stackrel{\sim}{\rightarrow} \pi_{1}(T_{\alpha})
$$

$$
U_{\alpha, \mathfrak{C}} \stackrel{\sim}{\rightarrow} \text{the universal covering of } T_{\alpha}.
$$

As real analytic manifolds we have

$$
(\overline{\pi}_{\alpha}', \phi): U_{\alpha} \backslash \mathcal{D}(F_{\alpha}) / c - T_{\alpha} \stackrel{\sim}{\rightarrow} \mathcal{D}(F_{\alpha})' \times U_{\alpha}
$$

$$
U_{\alpha} \backslash \mathcal{D} / c - T_{\alpha} \quad \stackrel{\sim}{\rightarrow} \mathcal{D}(F_{\alpha})' \times \Omega_{\alpha}.
$$

(7.7) Step 2. Construct a partial torus compactification of $U_{\alpha} \backslash \mathcal{D}$ with $\Sigma_{\alpha}$.

Let $X_{\Sigma_{\alpha}}$ be the torus embedding of $T_{\alpha}$ associated with a $\overline{F}*{\alpha}$-admissible decomposition $\Sigma*{\alpha} = \{\sigma_{\mu}\}$.
Then with the bundle structure $\overline{\pi}*{\alpha}': U*{\alpha} \backslash \mathcal{D}(F_{\alpha}) \to \mathcal{D}(F_{\alpha})'$ we can construct a fibre bundle

$$
(U_{\alpha} \backslash \mathcal{D}(F_{\alpha}))_{\Sigma_{\alpha}} = (U_{\alpha} \backslash \mathcal{D}(F_{\alpha})) \times {}^{\mathrm{T}_{\alpha}} X_{\Sigma_{\alpha}} \quad \text{over} \quad \mathcal{D}(F_{\alpha})' \quad \text{with fibre} \quad X_{\Sigma_{\alpha}} \quad \text{canonically}.
$$

It has a fibrewise $T_{\alpha}$-orbit decomposition (cf.
(4.9))

$$
\coprod_{\mu} O(\mu)
$$

such that

0. each $O(\mu)$ is an algebraic torus bundle over $\mathcal{D}(F_{\alpha})'$;

i) $\sigma_{\mu} \prec \sigma_{\nu} \iff O(\mu)^{-} \supset O(\nu)$;

ii) $\dim \sigma_{\mu} + \dim O(\mu) = \dim \mathcal{D}$;

iii) for $\sigma_{\mu} = \{0\}$, $O(\mu) = U_{\alpha} \backslash \mathcal{D}(F_{\alpha})$.

Define

$$
(U_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} := \text{the interior of the closure of } U_{\alpha} \backslash \mathcal{D}
$$

$$
\text{in} \quad (U_{\alpha} \backslash \mathcal{D}(F_{\alpha}))_{\Sigma_{\alpha}}
$$

(cf.
3.4)). We have the following commutative diagram.

62

$$
\begin{array}{c c c}
U _ {\alpha} \backslash \mathcal {D} &amp; c &amp; U _ {\alpha} \backslash \mathcal {D} (F _ {\alpha}) \\
\hline
\widetilde {\pi} _ {\alpha} ^ {\prime} + &amp; (U _ {\alpha} \backslash \mathcal {D}) _ {\Sigma_ {\alpha}} &amp; c \\
&amp; \nearrow &amp; (U _ {\alpha} \backslash \mathcal {D} (F _ {\alpha})) _ {\Sigma_ {\alpha}} \\
\hline
\mathcal {D} (F _ {\alpha}) ^ {\prime} / &amp; = &amp; \mathcal {D} (F _ {\alpha}) ^ {\prime} \\
+ &amp; \widetilde {\pi} _ {\alpha} &amp; \\
F _ {\alpha} &amp; &amp;
\end{array}
$$

(7.8) The map $\operatorname{Im}: U_{\alpha} \backslash \mathcal{D}(F_{\alpha}) \to U_{\alpha}$ defined as

$$
\begin{array}{l}
\operatorname{Im}: U _ {\alpha} \backslash \mathcal {D} (F _ {\alpha}) \stackrel {{\circ}} {{\to}} F _ {\alpha} \times V _ {\alpha} \times (U _ {\alpha}, \underline {{m}} / U _ {\alpha}) \quad (7.1) \text{II.1} \\
\xrightarrow [ \text{long} ]{\text{projection}} (U _ {\alpha}, \underline {{m}} / U _ {\alpha}) \xrightarrow [ ]{\text{Im}} U _ {\alpha}, \tag{6.2}
\end{array}
$$

whose fibres are $\mathcal{D}(F_{\alpha})' \times c - T_{\alpha}$ , (7.6), extends to a map

$$
\operatorname{Im}: (U _ {\alpha} \backslash \mathcal {D} (F _ {\alpha})) _ {\Sigma_ {\alpha}} \rightarrow (U _ {\alpha}) _ {\Sigma_ {\alpha}}
$$

compatible with the actions of $\mathbf{T}*{\alpha}$ and $U*{\alpha}$ via the epimorphism

$$
\operatorname{Im}: T _ {\alpha} \rightarrow U _ {\alpha},
$$

hence preserving the orbit decompositions $\{0(\mu)\}$ in $(U_{\alpha} \backslash \mathcal{D}(F_{\alpha}))*{\Sigma*{\alpha}}$ and $\{\widetilde{O}*{\mu}\}$ in $(U*{\alpha})*{\Sigma*{\alpha}}$ by (6.16).

We have another map $\Phi$ of $U_{\alpha} \backslash \mathcal{D}(F_{\alpha})$ to $U_{\alpha}$ . We see that, if one fixes the $(F_{\alpha} \times V_{\alpha})$ -component, then $\Phi$ and $\operatorname{Im}$ differ only by a translation of $U_{\alpha}$ as shown directly in the case of $F_{\alpha} = F_{g'}$ ;

$$
\text{for } \tau \text{ mod } U _ {g ^ {\prime}} = (\tau^ {\prime}, \tau^ {\prime \prime}, \tau^ {\prime \prime} \text{ mod } U _ {g ^ {\prime}}),
$$

$$
\operatorname{Im} (\tau \text{ mod } U _ {g ^ {\prime}}) = \operatorname{Im} \tau^ {\prime \prime},
$$

$$
\Phi (\tau \text{ mod } U _ {g ^ {\prime}}) = \operatorname{Im} \tau^ {\prime \prime} - ^ {t} (\operatorname{Im} \tau^ {\prime \prime}) (\operatorname{Im} \tau^ {\prime}) ^ {- 1} (\operatorname{Im} \tau^ {\prime \prime}).
$$

Therefore $\Phi$ also extends to a map

$$
\Phi : (U _ {\alpha} \backslash \mathcal {D} (F _ {\alpha})) _ {\Sigma_ {\alpha}} \rightarrow (U _ {\alpha}) _ {\Sigma_ {\alpha}}
$$

63

which enjoys the same properties as Im above.

In fact it can be shown that as a real analytic manifolds

$$
(\overline{\pi}_{\alpha}^{\prime}, \phi): (U_{\alpha} \setminus D(F_{\alpha}))_{\Sigma_{\alpha}} / c - T_{\alpha} \stackrel{\sim}{\to} D(F_{\alpha})^{\prime} \times (U_{\alpha})_{\Sigma_{\alpha}}
$$

(cf.
(7.6)). In $(U_{\alpha})*{\Sigma*{\alpha}}$ we define $(\Omega_{\alpha})*{\Sigma*{\alpha}}$ in the similar manner as in (7.7), namely

$$
(\Omega_{\alpha})_{\Sigma_{\alpha}} := \text{the interior of the closure of } \Omega_{\alpha} \text{ in } (U_{\alpha})_{\Sigma_{\alpha}}.
$$

Then we have $\phi^{-1}((\Omega_{\alpha})*{\Sigma*{\alpha}}) = (U_{\alpha} \setminus D)*{\Sigma*{\alpha}}$, hence

$$
(\overline{\pi}^{\prime}, \phi): (U_{\alpha} \setminus D)_{\Sigma_{\alpha}} / c - T_{\alpha} \stackrel{\sim}{\to} D(F_{\alpha})^{\prime} \times (\Omega_{\alpha})_{\Sigma_{\sigma}}
$$

![img-14.jpeg](img-14.jpeg)

Facts (7.9).

1. If $\sigma_{\mu} \cap \Omega_{\alpha} \neq \phi$, then $O(\mu) &lt; (U_{\alpha} \setminus D)*{\Sigma*{\alpha}}$ (for $\overline{O}*{\mu} &lt; (\Omega*{\alpha})*{\Sigma*{\alpha}}$ as the above picture shows).
   We let

$$
O(F_{\alpha}) := \prod_{\sigma_{\mu} \cap \Omega_{\alpha}} \sigma_{\mu} O(\mu)
$$

64

which is closed in $(\mathrm{U}*{\alpha} \backslash \mathcal{D})*{\Sigma_{\alpha}}$ by the property i) in (7.7). This is so-to-say the set of points essentially added with respect to $\mathbf{F}_{\alpha}$.

2. For $\mathbf{F}*{\alpha} &lt; \mathbf{F}*{\beta}$ (i.e. $\mathbf{F}*{\alpha} \subset (\mathbf{F}*{\beta})^{-}$) (hence $U_{\beta} \subset U_{\alpha}$, $\Sigma_{\beta} = \Sigma_{\alpha} \cap U_{\beta}$) we have a commutative diagram

$$
\begin{array}{c c c}
\mathrm{U}_{\beta} \backslash \mathcal{D} &amp; \rightarrow &amp; \mathrm{U}_{\alpha} \backslash \mathcal{D} \\
\cap &amp; &amp; \cap
\end{array}
$$

$$
\begin{array}{c c c}
(\mathrm{U}_{\beta} \backslash \mathcal{D})_{\Sigma_{\beta}} &amp; \rightarrow &amp; (\mathrm{U}_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \\
\cap &amp; &amp; \cap
\end{array}
$$

$$
\begin{array}{c c c}
\Pi_{\alpha, \beta}: (\mathrm{U}_{\beta} \backslash \mathcal{D}(\mathrm{F}_{\beta}))_{\Sigma_{\beta}} &amp; \rightarrow &amp; (\mathrm{U}_{\alpha} \backslash \mathcal{D}(\mathrm{F}_{\alpha}))_{\Sigma_{\alpha}} \\
\cup &amp; &amp; \cup \\
\mathrm{O}_{\beta}(\mu) &amp; \rightarrow &amp; \mathrm{O}_{\alpha}(\mu) \quad \text{for} \quad \sigma_{\mu} \in \Sigma_{\beta}
\end{array}
$$

where $\Pi_{\alpha, \beta}$ is an Galois covering over the open image with covering group $\mathrm{U}*{\alpha} / \mathrm{U}*{\beta}$.
(Easy to see from the definition.)
Note also that $\mathrm{O}(\mathbf{F}*{\alpha})$ is the complement of the union of $\operatorname{Im} \Pi*{\alpha, \beta}$ for $\forall \mathbf{F}*{\beta} \geqslant \mathbf{F}*{\alpha}$, which is the reason why we call $\mathrm{O}(\mathbf{F}_{\alpha})$ the set of points essentially added.

3. The canonical holomorphic map: $\mathrm{U}_{\alpha} \backslash \mathcal{D} \to \Gamma \backslash \mathcal{D}$ extends to a holomorphic map

$$
p_{\alpha}: (\mathrm{U}_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \rightarrow (\Gamma \backslash \mathcal{D})^{\vee}
$$

whose restriction on $\mathrm{O}(\mathbf{F}_{\alpha})$ coincides with the map

$$
\mathrm{O}(\mathbf{F}_{\alpha}) \rightarrow \Gamma_{\alpha} \backslash \mathbf{F}_{\alpha}
$$

induced from $\overline{\pi}*{\alpha}: (\mathrm{U}*{\alpha} \backslash \mathcal{D})*{\Sigma*{\alpha}} \to \mathbf{F}*{\alpha}$.
(The last statement is easy to see for $\mathbf{F}*{\alpha} = \mathbf{F}_{\beta}$, from Scholie (5.9), (6.16) B) and (7.8).)

Also we have

$$
p_{\alpha}^{-1}(\Gamma_{\alpha} \backslash \mathbf{F}_{\alpha}) = \mathrm{O}(\mathbf{F}_{\alpha}).
$$

**Main Theorem (7.10) (strong form).**

Given a $\Gamma$-admissible family of decompositions, there is a unique compactification $(\Gamma \backslash \mathcal{D})^{\vee}$ of $\Gamma \backslash \mathcal{D}$ such that

1. for each $\mathbf{F}_{\alpha}$ the canonical map

65

$$
U_{\alpha} \backslash D \quad \rightarrow \quad \Gamma \backslash D
$$

extends to an open holomorphic map

$$
\pi_{F_{\alpha}} : (U_{\alpha} \backslash D)_{\Sigma_{\alpha}} \rightarrow (\Gamma \backslash D)^{\vee},
$$

$$
\text{ii)} \quad (\Gamma \backslash D)^{\vee} = \underset{\alpha}{\cup} \operatorname{Im} \pi_{F_{\alpha}}.
$$

(7.11) Step 3. Take the quotient by $\Gamma_{\alpha} / U_{\alpha}$.

The basic fact is the following

Proposition (7.11.1). $\Gamma_{\alpha} / U_{\alpha}$ acts properly discontinuously on $(U_{\alpha} \backslash D)*{\Sigma*{\alpha}}$.

Idea of the proof.
By the $\overline{\Gamma}*{\alpha}$-admissibility of $\Sigma*{\alpha}$ (especially (7.3) i) 3)) $\Gamma_{\alpha} / U_{\alpha}$ acts on $(U_{\alpha} \backslash D(F_{\alpha}))*{\Sigma*{\alpha}}$ and preserves $(U_{\alpha} \backslash D)*{\Sigma*{\alpha}}$.

Recall the next commutative diagram:

$$
\begin{aligned}
\Omega_{\alpha} &amp;= (\Omega_{\alpha})_{\Sigma_{\alpha}} \\
\uparrow \Phi &amp; \uparrow \Phi \\
U_{\alpha} \backslash D &amp;= (U_{\alpha} \backslash D)_{\Sigma_{\alpha}} \\
\downarrow \pi'_{\alpha} &amp; \downarrow \\
D(F_{\alpha})' &amp;= D(F_{\alpha})' \xrightarrow{\sim} F_{\alpha} \times V_{\alpha} \\
\downarrow \pi_2 &amp; \downarrow \\
F_{\alpha} &amp;= F_{\alpha}
\end{aligned}
$$

and exact sequences

$$
\begin{aligned}
1 \rightarrow \Gamma'_{\alpha} / U_{\alpha} \rightarrow \Gamma_{\alpha} / U_{\alpha} &amp;\stackrel{p_{\ell}}{\rightarrow} \overline{\Gamma'_{\alpha} \rightarrow 1} \\
&amp; \text{Aut}(U_{\alpha}, \Omega_{\alpha}), \\
1 \rightarrow W_{\alpha} / U_{\alpha} &amp;\rightarrow \Gamma'_{\alpha} / U_{\alpha} &amp; \stackrel{p_{\mathrm{h}}}{\rightarrow} \overline{\Gamma'_{\alpha} \rightarrow 1} \\
V_{\alpha} &amp; &amp; \text{Aut}(F_{\alpha}).
\end{aligned}
$$

We use one more elementary lemma.

Lemma (7.11.2). Let $f: X \to Y$ be a continuous map of Hausdorff

66

topological spaces on which groups $G$ and $H$ acts equivariantly with respect to a homomorphism $\phi : G \to H$.

$$
\begin{array}{l}
f: X \to Y \\
+ \quad + \text{(action)} \\
\phi: G \to H \\
\end{array}
$$

If $H$ acts properly discontinuously on $Y$ and $\text{Ker } \phi$ acts properly discontinuously on $X$, then $G$ acts properly discontinuously on $X$.

We proceed as follows.

1. $\overline{F}*{\alpha}$ acts properly discontinuously on $F*{\alpha}$ (standard).

2. Since $W_{\alpha} / U_{\alpha} \subset V_{\alpha}$ is a discrete subgroup and $\pi_2: \mathcal{D}(F_{\alpha})' \to F_{\alpha}$ is a principal $V_{\alpha}$-bundle, $W_{\alpha} / U_{\alpha}$ acts properly discontinuously on $\mathcal{D}(F_{\alpha})'$.

3. By 1), 2) and the second exact sequence, we can apply (7.11.2) to conclude that $\Gamma_{\alpha}' / U_{\alpha}$ acts properly discontinuously on $\mathcal{D}(F_{\alpha})'$, hence so on $(U_{\alpha} \setminus \mathcal{D})*{\Sigma*{\alpha}}$.

4. The most crucial step is to show that

$\overline{F}*{\alpha}$ acts properly discontinuously on $(\Omega*{\alpha})*{\Sigma*{\alpha}}$.

We shall give a sketchy but almost complete proof.

Recall the construction of $(U_{\alpha})*{\Sigma*{\alpha}}$ in (6.16) B). All points of $(U_{\alpha})*{\Sigma*{\alpha}}$ can be described with symbols $y + \infty \cdot \sigma_{\mu}$, $y \in U_{\alpha}$, and a fundamental system of neighbourhoods of $y + \infty \cdot \sigma_{\mu}$ meets $\Omega_{\alpha}$ in the sets $y + z + B_{\varepsilon} + \sigma_{\mu}$, $B_{\varepsilon} : \varepsilon$-ball around $0 \in U_{\alpha}$ and $z \in \sigma_{\mu}$.
Hence by the definition of $(\Omega_{\alpha})*{\Sigma*{\alpha}}$ in (7.8) if $y + \infty \cdot \sigma_{\mu} \in (\Omega_{\alpha})*{\Sigma*{\alpha}}$, then $y + z + B_{\varepsilon} + \sigma_{\mu} \subset \Omega_{\alpha}$ for suitable $z \in \sigma_{\mu}$ and $\varepsilon$.
Since $x + y + \infty \cdot \sigma_{\mu} = x + \infty \cdot \sigma_{\mu}$, it follows that all points in $(\Omega_{\alpha})*{\Sigma*{\alpha}}$ can be described as $y + \infty \cdot \sigma_{\mu}$ with $y \in \Omega_{\alpha}$.
Conversely if $y \in \Omega_{\alpha}$, $y + B_{\varepsilon} + \sigma_{\mu} \subset \Omega_{\alpha}$ for small enough $\varepsilon$, hence $y + z + B_{\varepsilon} + \infty \cdot \sigma_{\mu}$ is contained in the closure of $\Omega_{\alpha}$ in $(U_{\alpha})*{\Sigma*{\alpha}}$ for all $z \in \sigma_{\mu}$ and for all faces $\sigma_{\nu}$ of $\sigma_{\mu}$.
This implies that $y + \infty \cdot \sigma_{\mu} \in (\Omega_{\alpha})*{\Sigma*{\alpha}}$.
Therefore we have obtained

**Claim (7.11.3).**

$$
(\Omega_{\alpha})_{\Sigma_{\alpha}} = \bigcup_{\mu} \bigcup_{\nu} y \in \Omega_{\alpha} \left\{y + \infty \cdot \sigma_{\mu} \right\}.
$$

(Actually (7.8) 1) is a corollary of this claim.)

67

The existence of a fundamental domain with respect to the action of $\overline{\Gamma}*{\alpha}$ on $\Omega*{\alpha}$ (non trivial, cf.
§8) and the $\overline{\Gamma}*{\alpha}$-admissibility (7.3) 4) imply that for $y \in \Omega*{\alpha}$ and $\sigma_{\mu} \in \Sigma_{\alpha}$ the set

$$
I = \{v; \sigma_{v} \cap \tau \cap \Omega_{\alpha} \neq \phi\}
$$

is finite where $\tau$ is the cone generated by $y$ and $\sigma_{\mu}$, and

$$
\sigma = \begin{array}{c} v \\ v \in I \end{array} \sigma_{v}
$$

contains $y$ in its interior.
(Here some precise argument is skipped.)
Then it follows in a similar way as above that $\overline{\sigma}$ in $(U_{\alpha})*{\Sigma*{\alpha}}$ is a neighbourhood of $y + \infty \cdot \sigma_{\mu}$, hence so is $(\sigma)*{\Sigma*{\alpha}} = (\overline{\sigma})^{\circ}$ in $(U_{\alpha})*{\Sigma*{\alpha}}$.

By the $\overline{\Gamma}*{\alpha}$-admissibility (7.3) 3) only a finite number of $\overline{\gamma} \in \overline{\Gamma}*{\alpha}$ satisfy $\overline{\gamma} \cdot \sigma^{\circ} \cap \sigma^{\circ} \neq \phi$, which is shown to be equivalent to say that $\overline{\gamma}(\sigma)*{\Sigma*{\alpha}} \cap (\sigma)*{\Sigma*{\alpha}} \neq \phi$.
This last claim is what we want to prove.

Q.E.D. of 4).

Applying Lemma (7.11.2) once again for $\phi : (U_{\alpha} \backslash D)*{\Sigma*{\alpha}} \to (\Omega_{\alpha})*{\Sigma*{\alpha}}$ and $p_{\xi} : \Gamma_{\alpha} / U_{\alpha} \to \overline{\Gamma}_{\alpha}$ and using 3) and 4) we obtain the desired result (7.11.1).

Q.E.D. of (7.11.1).

By H. Cartan's theorem we obtain:

**Theorem (7.12).** The quotient space $(\Gamma_{\alpha} / U_{\alpha}) \backslash (U_{\alpha} \backslash D)*{\Sigma*{\alpha}}$ has a canonical quotient structure of a normal analytic space, and $\overline{O}(F_{\alpha}) = (\Gamma_{\alpha} / U_{\alpha}) \backslash O(F_{\alpha})$ is a closed analytic set in it.

**Conclusion (7.13).** We get the following commutative diagram of holomorphic maps of normal analytic spaces:

$$
\begin{array}{c c c}
\Gamma_{\alpha} \backslash D &amp; \longrightarrow &amp; \Gamma \backslash D \\
\tilde{\cap} &amp; \overline{p}_{\alpha} &amp; \tilde{\cap} \\
(\Gamma_{\alpha} / U_{\alpha}) \backslash (U_{\alpha} \backslash D)_{\Sigma_{\alpha}} &amp; \xrightarrow{\overline{p}_{\alpha}} &amp; (\Gamma \backslash D)^{\eta} \\
\tilde{\cup} &amp; \overline{\pi}_{\alpha} &amp; \tilde{\cup} \\
\overline{O}(F_{\alpha}) &amp; \xrightarrow{\overline{\pi}_{\alpha}} &amp; \Gamma_{\alpha} \backslash F_{\alpha} \quad (\text{cf.}(7.9) 3)).
\end{array}
$$

(7.14) **Step 4.** *Gluing.*

68

By $\Gamma$-admissibility (7.3) ii) 1) and the construction the action of $\gamma \in \Gamma$ on $\mathcal{D}$ extends to an isomorphism

$$
\gamma : (U_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \xrightarrow{\sim} (U_{\beta} \backslash \mathcal{D})_{\Sigma_{\beta}}
$$

$$
U_{\alpha} \backslash \mathcal{D} \xrightarrow{\sim} U_{\beta} \backslash \mathcal{D}
$$

for $\gamma F_{\alpha} = F_{\beta}$.
On the other hand if $F_{\alpha} &lt; F_{\beta}$ we have an etale map

$$
\Pi_{\alpha, \beta} : (U_{\beta} \backslash \mathcal{D})_{\Sigma_{\beta}} \rightarrow (U_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}}
$$

defined in (7.9) 2).

We glue $(U_{\alpha} \backslash \mathcal{D})*{\Sigma*{\alpha}}$'s via these $\gamma, \Pi_{\alpha, \beta}$, more precisely: let

$$
(\Gamma \backslash \mathcal{D})^{\sim} = \frac{11}{F_{\alpha}} (U_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}}
$$

and define an equivalence relation on it as follows:

$$
\begin{aligned}
\text{for } x_{\alpha} \in (U_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \text{ and } x_{\beta} \in (U_{\beta} \backslash \mathcal{D})_{\Sigma_{\beta}} \\
x_{\alpha} \sim x_{\beta} \text{ if } 1) \quad \mathcal{H}_{F_{\omega}}, \quad \mathcal{H}_{\gamma} \in \Gamma \text{ s.t. } F_{\alpha} &lt; F_{\omega}, \\
\quad \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad
&amp; s.t. a) \quad \Pi_{\alpha, \omega} : (U_{\omega} \backslash \mathcal{D})_{\Sigma_{\omega}} \rightarrow (U_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \\
&amp; \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad
&amp; x_{\omega} \quad \rightarrow \quad x_{\alpha}, \\
\text{b) } \quad \Pi_{\beta', \omega} : (U_{\omega} \backslash \mathcal{D})_{\Sigma_{\omega}} \rightarrow (U_{\beta'} \backslash \mathcal{D})_{\Sigma_{\beta'}} \\
&amp; \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad
&amp; x_{\omega} \quad \rightarrow \quad \gamma x_{\beta}.
\end{aligned}
$$

Then we define

$$
(\Gamma \backslash \mathcal{D})^{\gamma} := (\Gamma \backslash \mathcal{D})^{\sim} / \sim \text{ with the quotient topology}.
$$

We have a canonical map

69

$$
\pi_{\mathrm{F}_{\alpha}}: (\mathrm{U}_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \subset (\Gamma \backslash \mathcal{D})^{\sim} \rightarrow (\Gamma \backslash \mathcal{D})^{\vee}
$$

which is both closed and open and factors through

$$
\pi_{\mathrm{F}_{\alpha}}: (\mathrm{U}_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \rightarrow (\Gamma_{\alpha} / \mathrm{U}_{\alpha}) \backslash (\mathrm{U}_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \xrightarrow{\overline{\pi}_{\mathrm{F}_{\alpha}}} (\Gamma \backslash \mathcal{D})^{\vee}.
$$

Then by definition $\overline{\pi}*{\mathrm{F}*{\alpha}}$ is injective on $\overline{\mathcal{O}}(\mathrm{F}_{\alpha})$, but the reduction theory asserts a stronger property than

$$
\overline{\pi}_{\mathrm{F}_{\alpha}} \text{ is injective near } \overline{\mathcal{O}}(\mathrm{F}_{\alpha})
$$

(far from trivial, cf.(3.6.1)), by which we can endow $(\Gamma \backslash \mathcal{D})^{\vee}$ a structure of a normal complex analytic space.

**Observations (7.15).** i) We have a commutative diagram of holomorphic maps

$$
\begin{array}{l}
(\mathrm{U}_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \xrightarrow{\pi_{\mathrm{F}_{\alpha}}} (\Gamma \backslash \mathcal{D})^{\vee} \\
\begin{array}{c}
\downarrow \\
(\Gamma_{\alpha} / \mathrm{U}_{\alpha}) \backslash (\mathrm{U}_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \xrightarrow{\overline{\pi}_{\mathrm{F}_{\alpha}}} (\Gamma \backslash \mathcal{D})^{\vee} \\
\downarrow \\
\overline{\mathcal{O}}(\mathrm{F}_{\alpha}) \xrightarrow{\sim} \overline{\mathcal{O}}(\mathrm{F}_{\alpha})
\end{array} \\
\end{array}
$$

$(\overline{\pi}*{\mathrm{F}*{\alpha}}$ is isomorphic near $\overline{\mathcal{O}}(\mathrm{F}_{\alpha})$.)

ii) We have another commutative diagram of holomorphic maps

$$
\begin{array}{l}
p: (\Gamma \backslash \mathcal{D})^{\vee} \rightarrow (\Gamma \backslash \mathcal{D})^{\vee} \\
\begin{array}{c}
\uparrow \\
\end{array} \\
\begin{array}{c}
p_{\alpha}: (\mathrm{U}_{\alpha} \backslash \mathcal{D})_{\Sigma_{\alpha}} \rightarrow (\Gamma \backslash \mathcal{D})^{\vee} \\
\downarrow \quad \downarrow \\
\end{array} \\
\begin{array}{c}
\overline{\pi}_{\alpha}: \mathcal{O}(\mathrm{F}_{\alpha}) \rightarrow \Gamma_{\alpha} \backslash \mathrm{F}_{\alpha}
\end{array} \\
\end{array}
$$

where $p$ is the identity map on $\Gamma \backslash \mathcal{D}$.

iii) As a set we have

70

$$
(\Gamma \backslash D) ^ {\vee} = \underset {F _ {\alpha} \mod \Gamma} {\Pi} \overline {{O}} (F _ {\alpha}).
$$

Thus we have shown the main theorem (7.10). The other properties of $(\Gamma \backslash D)^{\vee}$ in (2.3) are now easy to check.

(2.3) i). By (7.7) ii) the boundary $O(\mu)$ is of codimension one in $(U_{\alpha} \setminus (F_{\alpha}))*{\Sigma*{\alpha}}$ if $\dim \mu = 1$.
Since any cone $\sigma_{\mu}$ has a face of dimension 1 and any $O(\mu)$ meets $(U_{\alpha} \setminus D)*{\Sigma*{\alpha}}$, the boundary $(U_{\alpha} \setminus D)*{\Sigma*{\alpha}} - U_{\alpha} \setminus D$ is purely of codimension 1. Therefore the boundary $(\Gamma \setminus D)^{\vee} - (\Gamma \setminus D)$, being locally a finite quotient of $(U_{\alpha} \setminus D)*{\Sigma*{\alpha}}$, has also pure codimension 1.

(2.3) ii) is clear from the construction, and (2.3) iii) has already been shown.
(2.3) v) is quite easy to show if one recalls the way of construction.

We state one more property of $(\Gamma \backslash D)^{\vee}$ which can be easily verified from the construction and (6.8).

**Proposition (7.16).** Let $\Sigma_{\alpha}^{(i)}$, $i = 1, 2$, be two $\Gamma$-admissible decompositions and $(\Gamma \backslash D)*{1}^{\vee}$ the associated toroidal compactification.
If for each $\alpha$, $\Sigma*{\alpha}^{(1)}$ is a refinement of $\Sigma_{\alpha}^{(2)}$, then there is a holomorphic map

$$
p_{2,1}: (\Gamma \backslash D)_{1}^{\vee} \rightarrow (\Gamma \backslash D)_{2}^{\vee}
$$

which is the identity map on $\Gamma \backslash D$.

**B) Geometric properties of toroidal compactifications (smoothness, projectivity, extension of holomorphic maps).**

Some geometric properties of $(\Gamma \backslash D)^{\vee}$ can be expressed in terms of those of decompositions.

Before stating a criterion for smoothness we need one notion as preliminary.

**Definition (7.17).** A subgroup $\Gamma$ of $\mathrm{GL}(n, \mathbb{C})$ is called *neat* if the subgroup of $\mathbb{C}^*$ generated by the eigenvalues of all $\gamma \in \Gamma$ is torsion free.

We recall two fundamental properties concerning neat subgroups

71

proved by Baily-Borel [4].

**Theorem (7.18).** Let $\Gamma$ be an arithmetic subgroup of the automorphism group $G$ of a bounded symmetric domain $\mathcal{D}$.

i) $\Gamma$ contains a neat subgroup $\Gamma'$ of finite index.

ii) If $\Gamma$ itself is neat, then $\Gamma$ operates on $\mathcal{D}$ without fixed points.
(This claim is an easy consequence from the fact that $\Gamma$ operates on $\mathcal{D}$ properly discontinuously.)

Now we can state a smoothness criterion.

**Proposition (7.19).** Suppose that all cones $\sigma_{\mu}$ in $\Sigma_{\alpha}$ are regular $(\rightarrow (6.14)\ 1))$.
Then

i) $(\Gamma \backslash \mathcal{D})^{\mathcal{V}}$ has at most finite quotient singularities;

ii) $(\Gamma \backslash \mathcal{D})^{\mathcal{V}}$ is smooth if moreover $\Gamma$ is neat.
(More strongly, as the proof below shows, under the assumption for $\Gamma$ to be neat, $(\Gamma \backslash \mathcal{D})^{\mathcal{V}}$ is smooth near $\pi_{\mathbb{F}*{\alpha}}(0(\mu))$ iff $\sigma*{\mu}$ in $\Sigma_{\alpha}$ is regular.)

**Proof.** The first claim follows from the second by using (7.18) i) and (2.3) v). By the assumption $(U_{\alpha} \backslash \mathcal{D})*{\Sigma*{\alpha}}$ is nonsingular for any $\alpha$ ((6.14) 1)) and $\Gamma_{\alpha}$ is neat.
Then one can show that $\Gamma_{\alpha} / U_{\alpha}$ operates on $(U_{\alpha} \backslash \mathcal{D})*{\Sigma*{\alpha}}$ without fixed points in a similar way as (7.11.1) and by using (7.11.1). (The essential idea is the same as to show (7.18) ii).) Hence the claim ii) follows since $(\Gamma \backslash \mathcal{D})^{\mathcal{V}}$ is locally isomorphic to $(\Gamma_{\alpha} / U_{\alpha}) \backslash (U_{\alpha} \backslash \mathcal{D})*{\Sigma*{\alpha}}$ which is nonsingular.
Q. E. D.

Concerning the existence of smooth compactifications we have

**Theorem (7.20).** For any $\Gamma$-admissible decomposition $\Sigma = \{\Sigma_{\alpha}\}$ there exists a refinement $\Gamma' = \{\Sigma_{\alpha}'\}$ such that all cones are regular.

Hence if $\Gamma$ is neat, any toroidal compactification is dominated by a smooth toroidal compactification.
(N.B. Moreover, as the proof shows, the dominating map is a blowing-up, hence projective.)

**Proof.** In [17] Theorem 11 (p.32) this statement is proved in the case of torus embeddings of finite type, which is not the case for $\Sigma_{\alpha}$.
By virtue of the finiteness condition (7.3) 4), however, the same argument works since, as one notes, the construction of the refinement is done essentially by the ascending induction on the dimension of cones.

72

Next we treat the projectivity of the compactification.
For that purpose we introduce another notation.

**Definition (7.21).**

$$
\begin{array}{l}
u := \underset{\mathbf{v}}{\mathrm{U}} \quad \mathbf{v}, \quad \mathbf{u}_\alpha &lt; \mathbf{G} \\
\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \Omega := \\
\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \Gamma \quad \text{acts continuously on } \mathbf{u} \text{ and preserves } \Omega.
\end{array}
$$

**Definition (7.22).** A $\Gamma$-admissible decomposition $\Sigma = \{\Sigma_\alpha\}$ is called *projective* if there exists a continuous convex piecewise linear function

$$
f: \Omega \longrightarrow \mathbb{R}
$$

such that

1. $f(u) &gt; 0$ for $u \neq 1$ ($= 0$ in $\mathbf{u}_\alpha$);
2. for each $\sigma_\mu \in \Sigma_\alpha$ there is a linear function $\ell_\mu$ on $\mathbf{u}*\alpha$ such that a) $\ell*\mu \geq f$ on $\Omega_\alpha$ and b) $\sigma_\mu = \{u \in \mathbf{u}*\alpha; \ell*\mu(u) = f(u)\}$;
3. $f(\Gamma \cap \Omega) &lt; \mathbb{Z}$;

(1) -3) $\leq f|*{\mathbf{u}*\alpha}$ is a polar function (6.14); 4) $f$ is $\Gamma$-invariant.

**Theorem (7.23)** (Tai, [2] Chap.
IV, §2). If $\Gamma$-admissible decomposition is projective, then

$$
p: (\Gamma \backslash p)^\gamma \longrightarrow (\Gamma \backslash p)^\eta
$$

is the normalization of the blowing-up along a sheaf of ideals $I$ with $I_{|(\Gamma \backslash p)} = \varnothing_{\Gamma \backslash p}$.

In particular $(\Gamma \backslash p)^\gamma$ is projective.

**Proof.** Outlined in the case of $p = p_g$.

With an easy argument we can reduce the general case to the case when $\Gamma$ is neat and see that we have only to consider near $\Gamma_g, \backslash F_g$, ($\Gamma_g = \Gamma \cap P_g$, similar notations in the sequel) in $(\Gamma \backslash \mathbf{E}_g)^\eta$.

73

Recall the canonical maps

$$
\begin{array}{c}
(U_{g}, \backslash D)_{\Sigma_{g}}, \\
\Big{\downarrow} \\
(\Gamma_{g}, / U_{g},) \backslash (U_{g}, \backslash D)_{\Sigma_{g}}, \xrightarrow{\overline{\pi}_{F_{g}},} (\Gamma \backslash D)^{\vee} \xrightarrow{p} (\Gamma \backslash D)^{\vee} \\
\upsilon \\
\overline{O}(F_{g},) \xrightarrow{\sim} \overline{O}(F_{g},) \xrightarrow{\overline{\pi}_{g}}, \Gamma_{g}, \backslash F_{g}, \\
(\overline{\pi}_{F_{g}}, : \text{isomorphic near } \overline{O}(F_{g},)).
\end{array}
$$

For $\sigma \in \Sigma_{g}$, we can define an open subset $(U_{g}, \backslash D)*{\sigma}$ of $(U*{g}, \backslash D)*{\Sigma*{g}}$, similarly as $(U_{g}, \backslash D)*{\Sigma*{g}}$ in (7.7). By virtue of (6.8) $(U_{g}, \backslash D)*{\Sigma*{g}}$ is covered with $(U_{g}, \backslash D)*{\sigma}$, $\sigma \in \Sigma*{g}$, where $\Sigma_{g}^{\max} = \{\sigma \in \Sigma_{g}; \text{dim } \sigma \text{ is maximal in } \Sigma_{g}\}$.

For $\sigma \in \Sigma_{g}^{\max}$, there is a unique linear form $\ell_{\sigma}$ on $U_{g}$, such that a) $f \leq \ell_{\sigma}$ on $\Omega_{g}$, and b) $\sigma = \{u \in U_{g}; f(u) = \ell_{\sigma}(u)\}$.

If we identify $U_{g}$, with $\Psi_{g}$ ($g = g - g’$), a linear form $\ell$ corresponds to an element $a \in \Psi_{g}$ via

$$
\ell(y) = tr(ay),
$$

hence the above $\ell_{\sigma}$ corresponds to $a_{\sigma} \in \Psi_{g}$, and moreover $a_{\sigma} \geq 0$ by the condition a) and the positivity of $f$.

By the above correspondence $\ell \leftrightarrow a$ the dual $U_{g}^{\prime \prime}$ of $U_{g}$, can be embedded in $\Psi_{g}^{\prime \prime}$ as a lattice, and the group $\overline{\Gamma}*{g^{\prime}} = p*{\ell}(\Gamma_{g^{\prime}})$ can be embedded in $\mathrm{GL}(g^{\prime \prime}, \mathbb{R})$ acting on $\Psi_{g}^{\prime \prime}$.

We use the notation in (5.4), in particular for $\tau \in \Theta_{g}$ we write

$$
\tau = \left( \begin{array}{cc} \tau' &amp; \tau'' \\ t_{\tau''} &amp; \tau'' \end{array} \right), \tau' \in \Theta_{g'}, \tau'' \in \Theta_{g''}^{-}(g'' = g - g').
$$

We further denote $\exp(2\pi\sqrt{-1}())$ by $e()$.

Take a point $\tau' \in F_{g'}$.
Since $\Gamma$ is neat, a sufficiently small neighbourhood $V$ of $\tau'$ in $F_{g'}$ is mapped biholomorphically into $\Gamma_{g'}, \backslash F_{g'}$.
We note that for the canonical map $m: D \to \Gamma \backslash D \subset (\Gamma \backslash D)^{\vee}$ the inverse image of a neighbourhood of $\overline{\tau'} = \tau' \mod \Gamma_{g'}$ by $m$ is expressed in the form

74

$$
U(V, K) = \left\{ \begin{array}{l} \tau' \quad \tau'' \\ t_{\tau''} \quad \tau'' \end{array} \right\}; \tau' \in V, \text{ Im } \tau'' - {}^t(\text{Im } \tau''')(\text{Im } \tau')^{-1}(\text{Im } \tau'') &gt; K
$$

and near $\overline{\tau}' \in \Gamma \setminus \mathcal{D}$ is isomorphic to $\Gamma_g', \setminus \mathcal{D}$ where

$$
\Gamma_g' = \left\{ \begin{array}{l} \begin{array}{cccc} 1 &amp; 0 &amp; * &amp; * \\ * &amp; u &amp; * &amp; * \\ 0 &amp; 0 &amp; 1 &amp; * \\ 0 &amp; 0 &amp; 0 &amp; t_u^{-1} \end{array} \right\} \in \Gamma \} \\
= (G_{\mathfrak{L}} \cdot W_{g'}) \cap \Gamma \quad (\text{cf.}(4.8), (4.9)).
$$

For $\sigma \in \Sigma_{g'}^{\max}$ we set

$$
\begin{aligned}
H_{\sigma}^{\theta}(\tau', \tau'', \tau'') \\
= \sum_{u \in \overline{\Gamma}_{g'}} \theta_{\sigma}(\tau', \tau''', t_u) \underline{\underline{e}} \left( \text{tr}(a_{\sigma} u \tau''^t u) \right)
\end{aligned}
$$

where $\theta_{\sigma}(\tau', \tau'')$ is a holomorphic function on $V \times V_{g'}, \mathfrak{C}$ with equalities

$$
\begin{aligned}
\theta_{\sigma}(\tau', \tau''' + \tau'm + n) \\
= \theta_{\sigma}(\tau', \tau'') \underline{\underline{e}} \left( \text{tr}(a_{\sigma} (2^t m \tau''' + {}^t m \tau'm)) \right)
\end{aligned}
$$

for any

$$
\left( \begin{array}{cccc} 1 &amp; 0 &amp; 0 &amp; n \\ t_m &amp; 1 &amp; t_n &amp; b \\ 0 &amp; 0 &amp; 1 &amp; -m \\ 0 &amp; 0 &amp; 0 &amp; 1 \end{array} \right) \in W_{g'} = W_{g'} \cap \Gamma,
$$

namely $\theta_{\sigma}$ is a theta function with a Riemann form

$$
2 \text{tr}(a_{\sigma}^t \tau'''(\text{Im } \tau')^{-1} \overline{\tau}'').
$$

Since $a_{\sigma} \geq 0$, such $\theta_{\sigma}$ exists.
By replacing $f$ by $nf$ (hence $a_{\sigma}$ by $na_{\sigma}$) if necessary, we may assume that for any $\sigma \in \Sigma_{g'}^{\max}$ and $\forall \tau' \in \mathfrak{G}*{g'}, \forall \tau''' \in M(g' \times g'', \mathfrak{C})$ there is a $\theta*{\sigma}$ as above with

75

$\theta_{\sigma}(\tau', \tau'') \neq 0$.
(Here we need the finiteness condition (7.3) 4).)

This series $\overline{H}*{\sigma}^{\theta}$, called a Fourier-Jacobi series, is uniformly convergent on any compact set in $U(V, K)$ ([15] Lemma 8). Moreover it is $\Gamma*{g'}'$-invariant and defines a holomorphic function on $m(U(V, K)) \subset \Gamma \backslash D$ which turns out to extend to a holomorphic function $\overline{H}*{\sigma}^{\theta}$ near $\overline{\tau}' \in \Gamma*{g'}, \backslash F_{g'}, \subset (\Gamma \backslash D)^{\gamma}$.

Now we define a sheaf of ideals $I$ of $\mathcal{O}_{(\Gamma \backslash D)^{\gamma}}$ as

$$
I_{\overline{\tau}'} = \text{the } \mathcal{O}_{\overline{\tau}'} \text{-ideal generated by such } \overline{H}_{\sigma}^{\theta}, \quad \sigma \in \Sigma_{g'}^{\max}
$$

for $\overline{\tau}' \in \Gamma_{g'}, \backslash F_{g'}, \subset (\Gamma \backslash D)^{\gamma}$ (for the other boundary components by the action of $\overline{G}$). We claim that

$$
\begin{array}{r}
(\Gamma \backslash D)^{\gamma} \text{ is the normalization of the blowing-up } \mathcal{B}_I \\
= \operatorname{Proj}_{(\Gamma \backslash D)^{\gamma}} (\Phi_{m \geq 0} I^m) \text{ of } (\Gamma \backslash D)^{\gamma} \text{ along } I.
\end{array}
$$

The claim can be derived from the following two facts.

i) With the canonical map $p: (\Gamma \backslash D)^{\gamma} \to (\Gamma \backslash D)^{\gamma} p^*(I)$ is invertible.
Hence $p$ factors through $(\Gamma \backslash D)^{\gamma} \xrightarrow{\widehat{p}} \mathcal{B}_I \xrightarrow{\text{canonical}} (\Gamma \backslash D)^{\gamma}$.

ii) The map $\widehat{p}$ is finite.

In order to prove i), since $\Gamma$ is neat, it is enough to show that $(p_{g'})^*(I)$ is invertible for $p_{g'}: (U_{g'}, \backslash D)*{\Sigma*{g'}} \xrightarrow{\pi_{F_{g'}}} (\Gamma \backslash D)^{\gamma} \xrightarrow{p} (\Gamma \backslash D)^{\gamma}$ near $O(F_{g'})$.
Let $z \in O(F_{g'}) \cap (U_{g'}, \backslash D)*{\sigma}$ for $\sigma \in \Sigma*{g'}^{\max}$ and

$$
\begin{array}{l}
\pi_{g'}' : (U_{g'}, \backslash D)_{\Sigma_{g'}} \to D(F_{g'})' \stackrel{\sim}{\approx} \mathcal{C}_{g'} \times V_{g'}, \alpha \\
w \quad w \\
z \quad \rightarrow \quad (\tau_{0}', \tau_{0}'''), \quad (5.4) \ i).
\end{array}
$$

As we have remarked above there is a $\theta_{\sigma}$ with $\theta_{\sigma}(\tau_{0}', \tau_{0}''') \neq 0$.
Then we show that

$$
(p_{g'})^*(I)_z \text{ is generated by } \widehat{H}_{\sigma}^{\theta} = (p_{g'})^*(\overline{H}_{\sigma}^{\theta}).
$$

The claim is again reduced to the following two facts:

1. $\widehat{H}*{\sigma}^{\theta} / e(\operatorname{tr}(a*{\sigma} \tau'')) \in \mathcal{O}_{z}^*$;

2. $H_{\sigma'}^{\theta'} / e(\operatorname{tr}(a_{\sigma} \tau'')) \in \mathcal{O}*{z}$ for $\forall \sigma' \in \Sigma*{g'}^{\max}, \forall \theta'$.

76

In both claims the essential point lies in the equality

$$
\begin{aligned}
|\underline{e}(\operatorname{tr}(a_{\sigma} \cdot u\tau"^{\mathrm{t}}u)| &amp;= \exp(-2\pi \operatorname{tr}(a_{\sigma} \cdot u(\operatorname{Im} \tau")^{\mathrm{t}}u)) \\
&amp;= \exp(-2\pi &lt;^{\mathrm{t}}u a_{\sigma} \cdot u, \operatorname{Im} \tau" &gt;).
\end{aligned}
$$

Hence if $\operatorname{Im} \tau'' \leq \sigma$, then

$$
|\underline{e}(\operatorname{tr}(a_{\sigma} \tau")| = \exp(-2\pi f(\operatorname{Im} \tau"))
$$

and

$$
\begin{aligned}
|\underline{e}(\operatorname{tr}(a_{\sigma} \cdot u\tau"^{\mathrm{t}}u)| &amp;\leq |\underline{e}(\operatorname{tr}(a_{\sigma} \tau")| \quad \text{for} \quad \forall \sigma' \in \Sigma_{\underline{g}'}^{\max}, \\
&amp;\forall u \in GL(\underline{g}'', \mathbb{Z}).
\end{aligned}
$$

The claim 2), being a problem of convergence, is essentially proved in [15] Lemma 9. This proof shows that

$$
\tilde{H}_{\sigma}^{\theta} \sim \theta_{\sigma}(\tau', \tau''') \underline{e}(\operatorname{tr}(a_{\sigma} \tau"))
$$

near $z$, hence the claim 1) follows because $\theta_{\sigma}(\tau'', \tau''') \neq 0$.

The proof of the claim 11 proceeds in a similar way.
We omit it but a remark that there one reduces it to an elementary fact that for a fixed $\sigma \in \Sigma_{\underline{g}'}^{\max}$, $a_{\sigma'} - a_{\sigma}$, $\sigma' \in \Sigma_{\underline{g}'}^{\max}$, generate a rational cone $\sigma \cap U_{\underline{g}', \mathfrak{Q}}^{*}$ over $\mathfrak{Q}$.

Q.E.D. of (7.23).

As a typical example the normalized blowing-up of $(\Gamma \backslash D)^{\eta}$ along the boundary turns out to be a toroidal compactification.

**Definition (7.24).** Let $F_{\alpha}$ be a rational boundary component and consider $U_{\alpha}$ which is isomorphic to its Lie algebra by the exponential map.
Hence $U_{\alpha}$ admits a $P_{\alpha}$-invariant quadratic form $B(\, , )$ induced from the Killing form $(\rightarrow (4.11) \mathrm{iii}))$.
Let $U_{\alpha}^{*}$ denote the lattice dual to $U_{\alpha} = U_{\alpha} \cap \Gamma$.
Define a polar function on $\Omega_{\alpha}^{I}$ as

$$
\varphi|_{U_{\alpha}}(u) = \min_{u^{*}} \epsilon U_{\alpha}^{*} \cap \Omega_{\alpha} B(u, u^{*}).
$$

77

## Proposition (7.25)

$\varphi$ is a well-defined function on $\Omega$ and a family of cone decompositions $\Sigma$ determined by $\varphi$ (whose members are the maximal cones on which $\varphi$ is linear) is $\Gamma$-admissible and projective.
The associated toroidal compactification is the normalized blowing up of $(\Gamma \backslash \mathcal{D})^{\gamma}$ along the boundary.

We omit the proof here, which is essentially contained in Tai’s work (loc.
cit.)
though not explicitly mentioned.
In the case of $\Gamma = \operatorname{Sp}(g, \mathbb{Z})$ or $\Gamma(n)$ this result is essentially due to Igusa [15] ($\rightarrow$ Proof of (7.23)). The associated cone decomposition is what we call the central decomposition ($\rightarrow$ (8.9)).

Together with (7.20) we have the following existence theorem.

## Theorem (7.26)

For any neat arithmetic subgroup there is a *nonsingular and projective* toroidal compactification $(\Gamma \backslash \mathcal{D})^{\gamma}$ of $(\Gamma \backslash \mathcal{D})$.

### (7.27)

As the last topic we treat the problem of the extendability of holomorphic maps to $\Gamma \backslash \mathcal{D}$.

Let $D = \{t \in \mathbb{C} ; |t| &lt; 1\}$ be a disc and $D^* = D - \{0\}$ a punctured disc.
For a holomorphic map

$$
h: X = \underbrace{D^* \times \cdots \times D}_{m}^m \times \underbrace{D \times \cdots \times D}_{n} \rightarrow \Gamma \backslash \mathcal{D}
$$

which lifts locally to $\mathcal{D}$, we consider a *problem*:

- Does $h$ extend to a holomorphic map

$$
\overline{h}: \overline{X} = D^{m+n} \longrightarrow (\Gamma \backslash \mathcal{D})^{\gamma}
$$

for a toroidal compactification $(\Gamma \backslash \mathcal{D})^{\gamma}$ constructed with a $\Gamma$-admissible family of decompositions $\Sigma = \{\Sigma_{\alpha}\}$.

### (7.28)

By Borel’s extension theorem (2.2) A) 11) we know that $h$ extends to a holomorphic map

$$
\overline{\overline{h}}: \overline{X} \longrightarrow (\Gamma \backslash \mathcal{D})^{\gamma}.
$$

The value $\overline{\overline{h}}(0)$ determines a rational boundary component $F_{\alpha}$ of $\mathcal{D}$ up to $\Gamma$.

Let $\underline{e}: H = \{z \in \mathbb{C} ; \operatorname{Im} z &gt; 0\} \rightarrow D^*$; $\underline{e}(z) = \exp(2\pi\sqrt{-1}z)$ be the universal covering of $D^*$ with the covering transformation group $\{z \rightarrow z + \xi ; \xi \in \mathbb{Z}\}$ isomorphic to $\mathbb{Z}$.
Then the universal covering

78

of X is

$$
\begin{array}{l}
\underline{e}: \tilde{X} = H^m \times D^n \longrightarrow X = (D^*)^m \times D^n \\
(z_1, \dots, z_m, t_{m+1}, \dots, t_{m+n}) \rightarrow (\underline{e}(z_1), \dots, \underline{e}(z_m), t_{m+1}, \dots, t_{m+n})
\end{array}
$$

with the covering group $U = \{(\xi_1, \dots, \xi_m) \in \mathbb{Z}^m; (z_1, \dots, z_m, t_{m+1}, \dots, t_{m+n}) \rightarrow (z_1 + \xi_1, \dots, z_m + \xi_m, t_{m+1}, \dots, t_{m+n})\}$ canonically isomorphic to $\mathbb{Z}^m$.
We write $t = (t_1, \dots, t_m)$, $t' = (t_{m+1}, \dots, t_{m+n})$, $z = (z_1, \dots, z_m)$, $\xi = (\xi_1, \dots, \xi_m)$.

The map $h$ lifts to

$$
\begin{array}{ccc}
\tilde{h}: \tilde{X} &amp; \longrightarrow &amp; p \\
\underline{e} \downarrow &amp; &amp; \downarrow p \\
h: X &amp; \longrightarrow &amp; \Gamma \backslash p
\end{array}
$$

and there is a homomorphism

$$
\psi: U \longrightarrow \Gamma
$$

by which $\tilde{h}$ is an equivariant map, i.e.

$$
\tilde{h}(z + \xi, t') = \psi(\xi) \tilde{h}(z, t')
$$

for $\xi \in U$.
Moreover the fact that $\tilde{h}(0) \in F_{\alpha}$ modulo $\Gamma$ implies that after a suitable change of $\tilde{h}$ and $\psi$ by an element of $\Gamma$ we may assume that $\operatorname{Im} \psi \in P(F_{\alpha})$.
Then we have the following theorem concerning the extendability of the map $h$.

**Theorem (7.29).** In the above situation (7.27), (7.28) 1) for a subgroup $U'$ of $U$ of finite index we have

$$
\begin{array}{ccc}
\psi(U') &amp; \subset &amp; U(F_{\alpha}) \\
u &amp; &amp; u \\
\end{array}
$$

$$
\psi(U'^{+}) \subset U(F_{\alpha}) \cap \overline{\Omega(F_{\alpha})}
$$

where $U'^{+} = \{(\xi_1, \dots, \xi_m) \in U'; \xi_i \geq 0\}$.
Hence in particular $\psi$ defines an $\mathbb{R}$-linear map

79

$$
\psi_{\mathbb{R}}: \mathrm{U}_{\mathbb{R}}' = \mathrm{U}_{\mathbb{R}} \left( \succcurlyeq \mathbb{R}^m \right) \quad \rightarrow \quad \mathcal{U}(F_\alpha).
$$

Suppose moreover that we are given a $\Gamma$-admissible family of decompositions $\Sigma = \{\Sigma_\alpha\}$ for the construction of $(\Gamma \backslash \mathcal{D})^\gamma$.
Then

2. $h$ extends to a holomorphic map

$$
\overline{h}: \overline{x} = (D)^{m+n} \quad \rightarrow \quad (\Gamma \backslash \mathcal{D})^\gamma
$$

if and only if for $\mathbf{U}*{\mathbb{R}}^+ = \{ (\xi_1, \dots, \xi_m) \mid \xi_i \geq 0 \} \succcurlyeq (\mathbb{R}*{\geq 0})^m$, $\psi_{\mathbb{R}}(\mathbf{U}*{\mathbb{R}}^+)$ is contained in one of the c.r.p. cones in $\Sigma*\alpha$.
(The meaning of this condition will become clear in the proof.
cf.
Remark (7.30).)

*Proof.* We shall prove this theorem in the case of $\mathcal{D} = \mathfrak{S}_g$.
However almost all arguments work in general.

Recall the construction of $(\Gamma \backslash \mathcal{D})^\gamma$ (7.14) which says that we have a commutative diagram

$$
\begin{array}{l}
p_\alpha: (\mathrm{U}_\alpha \backslash \mathcal{D})_{\Sigma_\alpha} \xrightarrow{\pi_{F_\alpha}} (\Gamma \backslash \mathcal{D})^\gamma \xrightarrow{p} (\Gamma \backslash \mathcal{D})^\gamma \\
\overline{\pi}_\alpha: \mathrm{O}(F_\alpha) \longrightarrow \overline{\mathrm{O}}(F_\alpha) \longrightarrow \overline{\Gamma}_\alpha^\prime \backslash F_\alpha
\end{array}
$$

and $p_\alpha$ is a generically etale, proper holomorphic map near $\mathrm{O}(F_\alpha)$.
Hence for $i = 1, \dots, m$, if all but $i$-th coordinates are fixed, the map $h^{(i)}(t) = h(t_1, \dots, t_{i-1}, t, t_{i+1}, \dots, t_{m+n})$ has a lifting $h_i(s): D \to (\mathrm{U}*\alpha \backslash \mathcal{D})*{\Sigma_\alpha}$ subjects to

$$
p_\alpha \circ h_i(s) = h(t_1, \dots, t_{i-1}, s^{d_i}, t_{i+1}, \dots, t_{m+n})
$$

for $s \in D^*$.
This implies that

$$
\psi\left( (0, \dots, 0, \frac{i}{d_i}, 0, \dots, 0) \right) \in \mathrm{U}_\alpha.
$$

Hence the subgroup $\mathrm{U}'$ generated by $(0, \dots, 0, \frac{i}{d_i}, 0, \dots, 0)$, $i = 1, \dots, m$, satisfies the condition: $\psi(\mathrm{U}') \in \mathrm{U}(F_\alpha)$.

We consider a modified map $h_1: (\mathrm{D}^*)^m \times (\mathrm{D})^n \to \Gamma \backslash \mathcal{D}$ defined as

$$
\begin{array}{l}
h_1(s_1, \dots, s_m, t_{m+1}, \dots, t_{m+n}) \\
= h(s_1^{d_1}, \dots, s_m^{d_m}, t_{m+1}, \dots, t_{m+n}).
\end{array}
$$

Then $\mathrm{U}'$ is the covering group of $(\mathrm{D}^*)^m \times (\mathrm{D})^n$ and $\psi_1 = \psi|_{\mathrm{U}'}$.

80

satisfies the condition: $\psi_{1}(U') \subset U(F_{\alpha})$.
For simplicity we write $h$ for $h_1, \psi$ for $\psi_{1}$ and $U$ for $U'$ until the distinction between $h$ and $h_1$ is again needed.

Now we restrict ourselves to the case of $\mathcal{D} = \mathcal{G}*{\mathbf{g}}$ and $\mathbf{F} = \mathbf{F}*{\mathbf{g}'}$.
We write a (multiple-valued) map $h: X \to \mathcal{G}_{\mathbf{g}}$ as

$$
\begin{array}{l}
h(t, t') = (h_{ij}(t, t')) \in \mathcal{G}_{\mathbf{g}} \subset \mathbb{M}(\mathbf{g}, \mathfrak{C}) \\
= \left\{
\begin{array}{ll}
h'(t, t') &amp; h'''(t, t') \\
t h'''(t, t') &amp; h''(t, t')
\end{array}
\right\}, \\
h'(t, t') \in \mathcal{G}_{\mathbf{g}'}, \quad h''(t, t') \in \mathcal{G}_{\mathbf{g}''}, \\
\mathbf{g}'' = \mathbf{g} - \mathbf{g}'.
\end{array}
$$

Note that $h'(t, t')$ and $h'''(t, t')$ are hence single-valued (cf.
(4.8)).

Then we are ready to prove the next claim which contains the first part of (7.29).

**Claim (7.29.1).** i) $h'(t, t')$ and $h'''(t, t')$ are bounded, hence extends to matrix-valued holomorphic functions $\overline{h}'(t, t')$ and $\overline{h}'''(t, t')$ on $\overline{X}$.
ii) $h''(t, t')$ has a lifting $\tilde{h}(z, t')$ on $\tilde{X}$ written in the form

$$
\tilde{h}(z, g') = (i \circ \psi_{\mathfrak{C}})(z) + h_{0}(\underline{e}(z), t')
$$

so that $h_{0}(t, t')$ is single-valued and bounded (hence extends to $\overline{h}*{0}: \overline{X} \to \Psi*{\mathbf{g}''}, \mathfrak{C}$) where $i$ is the canonical isomorphism

$$
\begin{array}{c}
i: \mathcal{U}_{\mathbf{g}', \mathfrak{C}} \xrightarrow{\sim} \Psi_{\mathbf{g}''}, \mathfrak{C} \\
\swarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \omega
\end{array}
$$

$$
\left
\begin{array}{cccc}
1 &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; 1 &amp; 0 &amp; b \\
0 &amp; 0 &amp; 1 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 1
\end{array}
\right\} \longrightarrow b, \tag{4.8}.
$$

iii) For $\xi = (\xi_1, \dots, \xi_m)$, $\xi_1 \geq 0$, $\psi(\xi) \in \mathfrak{T}*{\mathbf{g}''}^+$, and for $\xi = (\xi_1)$, $\xi_1 &gt; 0$, $\psi(\xi) \in \mathfrak{T}*{\mathbf{g}''}^+$.

81

Proof.
1), 11). With the same argument as before the statement of (7.29.1) we can again replace $h$ by $h_1$ so that $\psi_1(U') \subset U_{g'}$ since $U_{g'}$ and $U(F_{g'})$ is commensurable in $U_{g'}$.
Hence we may assume that $\psi(U) \subset U_{g'}$, namely $e(h_{ij}(t, t'))$ is single-valued.

Since $\text{Im}(h(t, t')) &gt; 0$, for $\eta = (\eta_1, \dots, \eta_g) \in \mathbb{Z}^g$ we have

$$
\left| e(\eta h(t, t')^t \eta) \right| = \exp(-2\pi\eta(\text{Im } h(t, t'))^t \eta) &lt; 1,
$$

hence bounded.
With $\eta = e_1 = (0, \dots, 0, \overset{1}{\to}, 0, \dots, 0)$ we have

$$
0 &lt; |e(h_{ij}(t, t'))| &lt; 1
$$

and with $\eta = e_1 - e_j$ we have

$$
0 &lt; |e(h_{ij}(t, t'))|^2 &lt; |e(h_{ij}(t, t'))| \cdot |e(h_{jj}(t, t'))| &lt; 1.
$$

Therefore they extend to holomorphic functions on $\overline{X}$ and can be written as

$$
e(h_{ij}(t_1, \dots, t_m, t')) = \left( \prod_{k=1}^{m} t_k^{a_{ijk}} \right) f_{ij}(t, t')
$$

where $f_{ij}(t, t')$ does not vanish on $\overline{X}$.
By taking a branch $(h_0)*{ij}$ of $\frac{1}{2\pi\sqrt{-1}}$ log $f*{ij}(t, t')$ and defining a linear map $\varphi: U \to Y_g$ by $\varphi(e_k) = (a_{ijk})_{ij}$ we have

$$
h_{ij}(z, t') = \varphi_g(z) + (h_0)_{ij}(e(z), t').
$$

Then clearly $\varphi = \psi$ and the claims 1), 11) follow.

111. With the above description, we must show that $A_k = (a_{ijk})$ is positive semidefinite.
     For $\eta = (\eta_1, \dots, \eta_g) \in \mathbb{Z}^g$ we have

$$
e(\eta h(t, t')^t \eta) = \prod_{k=1}^{m} t_k^{\eta A_k t \eta} e(\eta h_0(t, t')^t \eta).
$$

Since $e(\eta h(t, t')^t \eta)$ does not vanish on $\overline{X}$ and $e(\eta h(t, t')^t \eta)$ is bounded on $\overline{X}$, we have $\eta A_k^t \eta \geq 0$.
A closer argument shows the second claim which we leave to the reader.
Q.E.D. of (7.29.1).

Next we prove 2) of Theorem (7.29). We keep the assumption that $U' = U$.
Hence $h$ has a lifting $\tilde{h}$ satisfying the commutative diagram

82

$$
\begin{array}{c c c c c}
\tilde{\overline{X}} &amp; \xrightarrow{\tilde{h}} &amp; D &amp; \subset F_{\alpha} \times V_{\alpha} \times U_{\alpha, \mathbb{C}} = D(F_{\alpha}) \\
\underline{e} &amp; \downarrow &amp; \downarrow &amp; \downarrow \\
X &amp; \xrightarrow{h} &amp; U_{\alpha} \setminus D \subset F_{\alpha} \times V_{\alpha} \times (U_{\alpha} \setminus U_{\alpha, \mathbb{C}}) \\
\| &amp; &amp; \downarrow &amp; p_{\alpha} &amp; (= T_{\alpha}) \\
X &amp; \xrightarrow{h} &amp; \Gamma \setminus D.
\end{array}
$$

Now we claim

(7.29.2) Under the assumption that $\psi_{\mathbb{R}}(U_{\mathbb{R}}^{+}) \subset \sigma$ for $\sigma \in \Sigma_{\alpha}$ the map $\tilde{h}$ extends to a map

$$
\tilde{\overline{h}}: \overline{X} \rightarrow (U_{\alpha} \setminus D)_{\Sigma_{\alpha}}.
$$

Proof.
We may assume that $F_{\alpha} = F_{g}$ , by transforming $F_{\alpha}$ to $F_{g}$ , by an element $g$ of $\operatorname{Sp}(g, \mathbb{C})$ and replacing $\Gamma$ by $g \Gamma g^{-1}$ . Hence we can use the claim (7.29.1).

Recall the example (6.15) 1) where the affine space $\mathbb{C}^m$ can be considered as the torus embedding of $(\mathbb{C}^*)^m$ associated with the cone $U_{\mathbb{R}}^{+}$ . $X$ and $\overline{X}$ can be then considered as subsets of them such as

$$
\begin{array}{l}
X \subset (\mathbb{C}^*)^m \times D^n \\
n \qquad n \\
\overline{X} \subset \mathbb{C}^m \times D^n.
\end{array}
$$

Now $h'(t, t')$, $h'''(t, t')$ and $\psi: U \to U_{\alpha}$ define holomorphic maps

$$
\begin{array}{l}
\psi_{\mathbb{C}}: \tilde{\overline{X}} \subset \mathbb{C}^m \times D^n \rightarrow D(F_{\alpha}) = F_{\alpha} \times V_{\alpha} \times U_{\alpha, \mathbb{C}} \\
\underline{e} \downarrow \quad \downarrow \\
\tilde{\psi}: X \subset (\mathbb{C}^*)^m \times D^n \rightarrow U_{\alpha} \setminus D(F_{\alpha}) = F_{\alpha} \times V_{\alpha} \times T_{\alpha},
\end{array}
$$

the latter of which extends by the assumption of (7.29.2) to

$$
\overline{\psi}: \overline{X} \subset \mathbb{C}^m \times D^n \rightarrow (U_{\alpha} \setminus D(F_{\alpha}))_{\Sigma_{\alpha}} = (F_{\alpha} \times V_{\alpha}) \times {}^{\mathrm{T}\alpha} X_{\Sigma_{\alpha}}
$$

((6.4)iii), (6.7) + some trivial generalization).

83

Next the extension $\overline{h}_0$ of $h_0$ defines a holomorphic map

$$
\underline{e}_\alpha \cdot \overline{h}_0: \overline{X} \to T_\alpha \quad \text{(where } \underline{e}_\alpha: U_{\alpha,\mathfrak{C}} \to T_\alpha = U_\alpha \setminus U_{\alpha,\mathfrak{C}})
$$

and $\overline{h}'$ and $\overline{h}''$ define a holomorphic map

$$
h_1 = (\overline{h}', \overline{h}''): \overline{X} \to F_\alpha \times V_\alpha,
$$

hence we have a holomorphic family of bundle maps

$$
\hat{h}_0: \overline{X} \to \operatorname{Aut}_{F_\alpha \times V_\alpha}(U_\alpha \setminus \mathcal{D}(F_\alpha))_{\Sigma_\alpha}.
$$

Then clearly the composite

$$
\hat{h}_0 \cdot \overline{\psi}_|\overline{X}: \overline{X} \xrightarrow{\overline{\psi}_|\overline{X}} (U_\alpha \setminus \mathcal{D}(F_\alpha))_{\Sigma_\alpha} \xrightarrow{\hat{h}_0} (U_\alpha \setminus \mathcal{D}(F_\alpha))_{\Sigma_\alpha}
$$

is the extension of $\hat{h}$.

The second clause of (7.29.1) iii) says that $\sigma \cap \Psi_{\mathfrak{C}}'' \neq \phi$, hence by (7.9) i) $\overline{h}(0) \in O(\sigma) \subset (U_\alpha \setminus \mathcal{D})*{\Sigma*\alpha}$.

For general $(t, t') \in \overline{X}$ we can easily reduce to the above case by taking a disc $D$ meeting $\overline{X} - X$ only at $(t, t')$ and considering the restriction of $h$ to $D^*$.
(Here we use (7.29) 2) for $F_\beta$ with $(h|_{D^*})^0(0) \in F_\beta$.)

Now (7.29.2) being established, $p_\alpha \cdot \overline{h}: \overline{X} \to (U_\alpha \setminus \mathcal{D})*{\Sigma*\alpha} \xrightarrow{p_\alpha} (\Gamma \setminus \mathcal{D})^\gamma$ gives the extension of $h$.

In order to prove the general case we recall the modified map $h_1: X' = \hat{X}/U' \to (\Gamma \setminus \mathcal{D})$ satisfying the commutative diagram

$$
\begin{array}{c}
X' = \hat{X}/U' \xrightarrow{h_1} (\Gamma \setminus \mathcal{D}) \\
\Big\downarrow \quad \text{c} \\
X = \hat{X}/U \xrightarrow{h} (\Gamma \setminus \mathcal{D})
\end{array}
$$

where $c$ is a finite map, which extends to a finite ramified covering

$$
\overline{c}: \overline{X}' \to \overline{X}
$$

where both $\overline{X}'$ and $\overline{X}$ are isomorphic to $D^m$.

We have seen that $h_1$ extends to $\overline{h}_1: \overline{X}' \to (\Gamma \setminus \mathcal{D})^\gamma$ since

84

$\psi_{1}(U') \subset U(F_{\alpha})$.
Then by Riemann's extension theorem $h$ extends to

$$
\overline{h}: \overline{X} \rightarrow (\Gamma \backslash \mathcal{D})^{\mathcal{P}}.
$$

A closer observation shows that we can reverse the argument to prove the converse of 2), but we omit it.
Q.E.D. of (7.29).

**Remark (7.30).**

1. The above theorem (7.29) shows a very special property of the domain $\mathcal{D}$ which more generally any "period domain" enjoys as the nilpotent orbit theorem asserts ([12], [29]).
2. As the above proof of (7.29.2) shows, the point is to consider $(D^*)^m$ as a subset of torus $(\mathbb{C}^*)^m$ and $D^m$ as a subset of the torus embedding $\mathbb{C}^m$ of $(\mathbb{C}^*)^m$ associated with the cone $U_{\mathbb{R}}^{+}$ with $U'$ as its lattice of one-parameter subgroups of $(\mathbb{C}^*)^m$.
   Then the condition 2) in (7.29) is nothing but the linear map

$$
\psi_{1}: U' \rightarrow U_{\alpha}
$$

is a morphism of r.p.p. decompositions

$$
\{U_{\overline{\mathbb{R}}}^{+}\} \rightarrow \Sigma_{\alpha}
$$

((6.4) iii)).

8. Examples : reduction theory of positive quadratic forms.

In this section we give some examples of admissible decompositions in the case of $\mathcal{D} = \mathfrak{S}_{\mathfrak{g}}$, which relates to the theory of reduction of positive quadratic forms in number theory.

$$
\begin{array}{l}
\mathfrak{V}_{\mathrm{g}} = \{y = (y_{ij}) \in \mathbb{M}(\mathrm{g}, \mathbb{R}) \mid {}^t y = y\}, \\
\quad \mathrm{u} \\
\quad \Omega = \mathfrak{V}_{\mathrm{g}}^{+} = \{y \in \mathfrak{V}_{\mathrm{g}} \mid y &gt; 0 \text{ (positive definite)}\}, \\
\quad \overline{\Omega} = \overline{\mathfrak{V}}_{\mathrm{g}}^{+} = \{y \in \mathfrak{V}_{\mathrm{g}} \mid y \geq 0 \text{ (positive semidefinite)}\}.
\end{array}
$$

1. $G = \mathrm{GL}(\mathrm{g}, \mathbb{R})$ operates on $\mathfrak{V}_{\mathrm{g}}$ as

$$
u: y \longrightarrow u y^t u
$$

and $\mathfrak{V}*{\mathrm{g}}^{+}$ is the $G$-orbit of $\mathfrak{L}*{\mathrm{g}}$.
And moreover

$$
\begin{array}{l}
G / \pm 1 = \operatorname{Aut}(\mathfrak{V}_{\mathrm{g}}, \mathfrak{V}_{\mathrm{g}}^{+}) \\
:= \{g \in \mathrm{GL}(\mathfrak{V}_{\mathrm{g}}) \mid g \mathfrak{V}_{\mathrm{g}}^{+} = \mathfrak{V}_{\mathrm{g}}^{+}\}
\end{array}
$$

(cf.
(4.11) iii)).

2. We can define a bilinear form on $\mathfrak{V}_{\mathrm{g}}$ as

$$
\begin{array}{l}
&lt; , &gt;: \mathfrak{V}_{\mathrm{g}} \times \mathfrak{V}_{\mathrm{g}} \rightarrow \mathbb{R} \\
\quad \mathrm{w} \quad \mathrm{w} \\
\quad (y_1, y_2) \rightarrow \operatorname{tr}(y_1 y_2) \quad (= \operatorname{tr}(\frac{1}{2}(y_1 y_2 + y_2 y_1))),
\end{array}
$$

and with respect to which $\overline{\Omega}$ is self-dual, i.e.

$$
\overline{\Omega} = \{y \in \mathfrak{V}_{\mathrm{g}} \mid \langle y, y' \rangle \geq 0 \text{ for } {}^t y' \in \overline{\Omega}\}.
$$

3. (cf.
   (4.4)). We can decompose $\overline{\Omega}$ into boundary components as

$$
\overline{\Omega} = \Omega \perp \perp_{\mathrm{W}} \Omega(\mathrm{W})
$$

86

where $\Omega(W) = \{y \in \overline{\Omega} \mid \text{Ker } y = W\}$ for a subspace $W$ of $\mathbb{R}^g$.

Defining

$$
\begin{aligned}
\Omega_{g''} := \left( \left( \begin{array}{cc} 0 &amp; 0 \\ 0 &amp; g'' \end{array} \right) \right); \quad y'' \in \mathbb{V}_{g''}^+ \\
= \Omega(W_{g''}), \quad W_{g''} = \left\{ \left( \begin{array}{cc} * &amp; \cdots * &amp; 0 \\ \cdots &amp; 0 &amp; \cdots &amp; 0 \end{array} \right) \right\}, \quad g' = g - g'',
\end{aligned}
$$

we have for $\Omega(W)$

$$
\dim W = g' \iff \exists u \in G \text{ s.t. } u\Omega(W)^t u = \Omega_{g''}.
$$

(8.2) We define two lattices in $\mathbb{V}_g$.

$$
\begin{aligned}
Y_g := \mathbb{V}_g \cap M(g, \mathbb{Z}), \\
Y'_g := \{ y \in \mathbb{V}_g \mid 2y \in Y_g, y_{ii} \in \mathbb{Z} \}. \\
\text{half-integer matrices}
\end{aligned}
$$

They are lattices in $\mathbb{V}_g$ dual to each other (i.e. $Y'_g = \{y' \in \mathbb{V}*g \mid xy', y \in \mathbb{Z} \text{ for } y \in Y_g\}$ and vice versa) and preserved by $G*{\mathbb{Z}} = GL(g, \mathbb{Z})$, and define the same rational structure on $\mathbb{V}_g$.

For $W \subset \mathbb{R}^g$ we say $\Omega(W)$ is rational if $W$ is defined over $\mathbb{Q}$, which is equivalent to say that for a $u \in G_{\mathbb{Q}} = GL(g, \mathbb{Q})$ (actually one can take one in $G_{\mathbb{Z}}$) $u\Omega(W)^t u = \Omega_{g''}$ (cf.
(4.15), (4.16)). We define

$$
\Omega^1 := \Omega \amalg \amalg W: \text{rational} \quad \Omega(W), \text{ the rational closure of } \Omega.
$$

**Lemma (8.3).** To give a $\mathrm{Sp}(g, \mathbb{Z})$-admissible family of decompositions

$\iff$ To give a $G_{\mathbb{Z}} = GL(g, \mathbb{Z})$-admissible decomposition of $\Omega = \mathbb{V}_g^+$, i.e.

$$
\begin{aligned}
\Sigma = \{ \sigma_\mu \} : 0) \sigma_\mu, \text{ cone generated by a finite number of } y's \text{ in } Y_g \cap \overline{\Omega}, \\
1) \sigma_\mu \succ \sigma \Rightarrow \sigma_\mu \in \Sigma, \\
2) \sigma_\mu, \sigma_\nu \in \Sigma \Rightarrow \sigma_\mu \cap \sigma_\nu \prec \sigma_\mu, \sigma_\nu,
\end{aligned}
$$

87

3. $\sigma_{\mu} \in \Sigma \Rightarrow u \sigma_{\mu}^{t} u \in \Sigma$ for $u \in G_{\mathbb{Z}^{\prime}}$,

4. $\# \{\sigma_{\mu} \mod G_{\mathbb{Z}^{\prime}}\} &lt; \infty$

5. $u \sigma_{\mu} = \Omega^{1}$.

*Proof.* By (5.4), for $F = F_{g}$, we have natural isomorphisms: $\Omega(F_{g}) = \Omega$, $\overline{F}(F_{g}) = GL(g, \mathbb{Z})$, with which $G_{\mathbb{Z}^{\prime}}$-admissible decomposition $\Sigma$ of $\Omega$ can be identified with $\overline{F}(F_{g})$-admissible decomposition on $U(F_{g})$.

First suppose that a family of decompositions $\{ \Sigma_{\alpha} \}$ is given.
For any rational boundary component $F_{\alpha}$ there is an $M \in \operatorname{Sp}(g, \mathbb{Z})$ such that $M \cdot F_{\alpha} = F_{g'}$.
Since

$$
\begin{array}{l}
U(F_{g'}) = \eta_{g''} \\
n \quad n \\
U(F_{g}) = \eta_{g} \\
\end{array}
$$

by the lower isomorphism, and by the properties (7.3) 11) 1), 2) $\overline{F}_{\alpha}$-admissible decomposition is determined by $\Sigma$.

Conversely, given a $G_{\mathbb{Z}^{\prime}}$-admissible decomposition $\Sigma$ on $\Omega$, one defines $\overline{F}*{\alpha}$-admissible decomposition on $U(F*{\alpha})$ by the above procedure.
The property 3) of $\Sigma$ and Proposition (4.8) for $F = F_{g}$ (note also that $P(F_{g}) = U(F_{g})$) ensure that such a $\overline{F}_{\alpha}$-admissible decomposition is well-defined (i.e. does not depend on the choice of $M$) and they form a family of decomposition.

Now we state the main problem in this section.

(8.4) Problem of reduction theory.
Find an explicit $GL(g, \mathbb{Z})$-admissible decomposition of $\eta_{g}^{+}$.

(8.5) Known results.

1. Perfect cone decomposition, or $1^{st}$ Voronoi decomposition.
   (Voronoi: Crelle J. 133 (1908), Coxeter: Canad.
   J. 3 (1951) etc.)

2. Central cone decomposition.
   (Koecher: Math.
   Ann.
   144 (1961), Igusa: Math.
   Ann.
   168 (1967))

3. $2^{nd}$ Voronoi decomposition ($\rightarrow$ §9). (Voronoi: Crelle J. 134 (1908), 136 (1909))

4. Minkowski reduction (C.R. 96 (1883)).

88

When one wants to prove the admissibility of such decompositions, the condition 4) in (8.3) is the most difficult to check.

Among the above decompositions 1) and 2) can be generalized to the case of other selfdual homogeneous cones (cf.
[2] Chap.II). The decomposition 3) appears naturally when one studies degeneration of theta functions (cf.
§9, [?3]).

(8.6) The case of $g = 2$ (Legendre).

$$
F = \left\{ \begin{pmatrix} a &amp; c \\ c &amp; b \end{pmatrix} ; 0 \leq 2c \leq a \leq b \right\} = \{(b-a)\begin{pmatrix} 0 &amp; 0 \\ 0 &amp; 1 \end{pmatrix} + (a-2c)\begin{pmatrix} 1 &amp; 0 \\ 0 &amp; 1 \end{pmatrix} + c\begin{pmatrix} 2 &amp; 1 \\ 1 &amp; 2 \end{pmatrix} \}
$$

is a fundamental domain in $\Omega$ with respect to the action of $GL(2, \mathbb{Z})$.

This is a corollary of the following theorem.

**Theorem (8.7).** Let

$$
\sigma_o = \left\{ \begin{pmatrix} \lambda_1 + \lambda_3 &amp; -\lambda_3 \\ -\lambda_3 &amp; \lambda_2 + \lambda_3 \end{pmatrix} ; \lambda_1, \lambda_2, \lambda_3 \geq 0 \right\}.
$$

Then $GL(g, \mathbb{Z})\sigma_o = \Omega^2$.

$$
\begin{aligned}
\operatorname{Iso}(\sigma_o) &amp;:= \{u \in GL(2, \mathbb{Z}) ; u \sigma_o^t u = \sigma_o\} \\
&amp;= \{\pm 1_2, \pm \begin{pmatrix} 0 &amp; 1 \\ 1 &amp; 0 \end{pmatrix}, \pm \begin{pmatrix} 0 &amp; 1 \\ 1 &amp; -1 \end{pmatrix}, \pm \begin{pmatrix} 1 &amp; -1 \\ 1 &amp; 0 \end{pmatrix}, \pm \begin{pmatrix} 1 &amp; -1 \\ 0 &amp; 1 \end{pmatrix}, \pm \begin{pmatrix} 1 &amp; 0 \\ 1 &amp; -1 \end{pmatrix} \}.
\end{aligned}
$$

$\operatorname{Iso}(\sigma_o)/\pm 1 \stackrel{\circ}{\to} S_3$ (the permutation group of degree 3).

**Proof.** First we note that $(\lambda_1, \lambda_2, \lambda_3)$ can be considered as a system of coordinates of $\mathfrak{Q}_2$ with respect to the basis

$$
\begin{pmatrix} 1 &amp; 0 \\ 0 &amp; 0 \end{pmatrix}, \begin{pmatrix} 0 &amp; 0 \\ 0 &amp; 1 \end{pmatrix}, \begin{pmatrix} 1 &amp; -1 \\ -1 &amp; 1 \end{pmatrix}.
$$

The permutation group $S_3$ acts naturally on $(\lambda_1, \lambda_2, \lambda_3)$ and preserves $\sigma_o$.
This is nothing but the isomorphism $\operatorname{Iso}(\sigma_o)/\pm 1 \stackrel{\circ}{\to} S_3$.
(The above says only $S_3 \subset \operatorname{Iso}(\sigma_o)/\pm 1$, but the equality is clear since any $u \in \operatorname{Iso}(\sigma_o)$ interchanges the above three generators of $\sigma_o$.

![img-15.jpeg](img-15.jpeg) Ω mod scalar

Then the theorem can be deduced from the following two claims.

Claim (8.7.1).

$\sigma_{0} = \{y \in \Omega^{2}; \operatorname{tr}(\mathrm{u a}*{0}^{\mathrm{t}} \mathrm{u y}) \geq \operatorname{tr}(a*{0} y) \text{ for } \forall u \in \mathrm{GL}(2, \mathbb{Z})\}$ ,

$(\sigma_{0})^{\circ}$ ( $=$ the interior of $\sigma_0$ ）

$$
= \{y \in \Omega^ {2}; \operatorname {t r} \left(u a _ {0} ^ {t} u y\right) &gt; \operatorname {t r} \left(a _ {0} y\right) \text {f o r} \forall u \in G L (2, Z), \tag {but} \neq I s o (\sigma_ {0}) \}
$$

where $a_0 = \begin{pmatrix} 1 &amp; 1/2 \\ 1/2 &amp; 1 \end{pmatrix}$ .

(Note that $\operatorname{Iso}(\sigma_0) = \operatorname{Iso}(a_0)$ as is directly checked.)

90

**Claim (8.7.2).** We consider general $g$.
For a halfinteger positive matrix $a \in Y_g$ or $Y_g^+$ we let

$$F = \{y \in \Omega^1; \operatorname{tr}(\mathrm{u}a^{\mathrm{t}}\mathrm{u}y) \geq \operatorname{tr}(\mathrm{a}y) \text{ for } \forall u \in G_{\mathbb{Z}} := \mathrm{GL}(g, \mathbb{Z})\}.$$

Then we have

$$G_{\mathbb{Z}} \cdot F = \Omega^1.$$

**Proof of (8.7.2).** We recall a well-known fact as follows.

**Lemma (8.7.3).** For $y \in \Omega^1$ the value

$$\min_{u \in \mathrm{GL}(g, \mathbb{Z})} \operatorname{tr}(\mathrm{u}a^{\mathrm{t}}\mathrm{u}y) \quad (\geq 0)$$

is strictly positive and attained with an element $u \in \mathrm{GL}(g, \mathbb{Z})$.

We just indicate the idea of the proof whose method is standard.
The point is to show that for a positive number $C$ the set

$$\{\alpha \in \Omega; \operatorname{tr}(\alpha y) &lt; C\}$$

is bounded in $\mathcal{Y}_g$.
Then, since $Y \cap \Omega$ is discrete in $\Omega$, the set

$$\{\alpha \in Y \cap \Omega; \operatorname{tr}(\alpha y) &lt; C\}$$

is finite.
This implies the claim of (8.7.3).

We note that the condition "$y \in \Omega^1$" is essential in order to reduce to the case of $y \in \Omega$.
For general points in the boundary of $\Omega$ the claim does not hold.

Now we continue the proof of (8.7.2). For any $y$ by the last lemma there is $v \in G_{\mathbb{Z}} = \mathrm{GL}(g, \mathbb{Z})$ such that $\operatorname{tr}(\mathrm{v}a^{\mathrm{t}}\mathrm{v}y) \leq \operatorname{tr}(\mathrm{u}a^{\mathrm{t}}\mathrm{u}y)$ for $\forall u \in G_{\mathbb{Z}}$.
The last condition is rewritten as

$$\operatorname{tr}(a^{\mathrm{t}}\mathrm{v}yv) \leq \operatorname{tr}((v^{-1}u)a^{\mathrm{t}}(v^{-1}u)(\mathrm{t}vyv)) \text{ for } \forall u \in G_{\mathbb{Z}},$$

which implies

$$\mathrm{t}vyv \in F.$$

Q.E.D.

91

Proof of (8.7.1). For

$$
y = \begin{pmatrix} \lambda_1 + \lambda_3 &amp; -\lambda_3 \\ -\lambda_3 &amp; \lambda_2 + \lambda_3 \end{pmatrix} \in \mathfrak{V}_2
$$

$$
y \in \sigma_0 \iff \lambda_1 \geq 0, \lambda_2 \geq 0, \lambda_3 \geq 0,
$$

$$
y \in (\sigma_0)^0 \iff \lambda_1 &gt; 0, \lambda_2 &gt; 0, \lambda_3 &gt; 0.
$$

For another $ a = \begin{pmatrix} \alpha &amp; \gamma \\ \gamma &amp; \beta \end{pmatrix} \in \mathfrak{V}\_2 $ we have

$$
\operatorname{tr}(ay) = \alpha \lambda_1 + \beta \lambda_2 + (\alpha + \beta - 2\gamma)\lambda_3,
$$

$$
\operatorname{tr}(a_0y) = \lambda_1 + \lambda_2 + \lambda_3.
$$

If $ a \in Y_2' \cap \Omega $, then

$$
\begin{aligned}
\alpha &amp;\geq 1, \quad \beta \geq 1, \\
\alpha + \beta - 2\gamma &amp;= (1 - 1)a \begin{pmatrix} 1 \\ -1 \end{pmatrix} \geq 1,
\end{aligned}
$$

and all equalities hold iff $ a = a_0 $.

Therefore if $ y \in \sigma_0 $, then $ \operatorname{tr}(ay) \geq \operatorname{tr}(a_0y) $ for $ \forall a \in Y_2' \cap \Omega $ and if $ y \in (\sigma_0)^0 $, then $ \operatorname{tr}(ay) &gt; \operatorname{tr}(a_0y) $ for $ a \neq a_0 \in Y_2' \cap \Omega $.

Conversely suppose that $ y \in \Omega^1 $ satisfies the condition:

$$
\operatorname{tr}(ua_0^t uy) \geq \operatorname{tr}(a_0y) \quad \text{for} \quad \forall u \in GL(2, \mathbb{Z}).
$$

In particular for $ u = \begin{pmatrix} 1 &amp; 0 \\ 0 &amp; -1 \end{pmatrix} $ we have

$$
a_1 = ua_0^t u = \begin{pmatrix} 1 &amp; -1/2 \\ -1/2 &amp; 1 \end{pmatrix}
$$

and

$$
\operatorname{tr}(a_1y) = \lambda_1 + \lambda_2 + 3\lambda_3 \geq \operatorname{tr}(a_0y) = \lambda_1 + \lambda_2 + \lambda_3.
$$

Hence $ \lambda_3 \geq 0 $.
Similarly with $ u = \begin{pmatrix} 1 &amp; 1 \\ 0 &amp; 1 \end{pmatrix} $ and $ \begin{pmatrix} 1 &amp; 0 \\ 1 &amp; 1 \end{pmatrix} $ we see that $ \lambda_1 \geq 0 $ and $ \lambda_2 \geq 0 $ respectively.
If $ y $ satisfies a stronger condition

92

$$
\operatorname{tr}(\mathrm{u a}_{\mathrm{o}}^{\mathrm{t}} \mathrm{u y}) &gt; \operatorname{tr}(\mathrm{a}_{\mathrm{o}} \mathrm{y}) \quad \text{for} \quad \forall \mathrm{u} \notin \operatorname{Iso}(\sigma_{\mathrm{o}}).
$$

Then the above shows that $\lambda_1 &gt; 0$, $\lambda_2 &gt; 0$, and $\lambda_3 &gt; 0$.
Q.E.D.

### (8.8) Perfect cone decomposition.

For $y \in \Omega$ we set

$$
\begin{array}{l}
\mu(y) = \min_{\xi \in \mathbb{Z}^g} \xi y^t \xi = \operatorname{tr}((^t \xi \xi) y), \\
\quad \xi \in \mathbb{M}(y) = \{\xi \in \mathbb{Z}^g; \xi y^t \xi = \mu(y)\}.
\end{array}
$$

We see that $\mathbb{M}(y) \neq \phi$ similarly as (8.7.3). Then the cone decomposition

$$
\Sigma_{\text{perf}} = \{\sigma = \sigma(y) = \sum_{\xi \in \mathbb{M}(y)} \mathbb{R}^{+t} \xi \xi\}_y \in \Omega
$$

is admissible.

A matrix $y \in \Omega$ is called a perfect form if $\sigma(y)$ has the biggest dimension, or equivalently, if $\sigma = \sigma(y)$ has the property that

$$
\sigma(y) = \sigma(y') \iff y' = \lambda y \quad \text{for} \quad \lambda \in \mathbb{R}^{+}.
$$

Perfect forms have been studied by Coxeter [7] who found an interesting method to obtain many perfect forms.
This gives all perfect forms up to $g = 6$ but not for $g &gt; 8$.

The geometric meaning of the toroidal compactification with this decomposition is not clear.

### (8.9) Central cone decomposition.

For $y \in \Omega^2$ we set

$$
\mu'(y) = \min_{a \in \Omega \cap Y_g'} \operatorname{tr}(ay) \quad (&gt; 0, \text{cf. (8.7.3)}),
$$

and for $a \in \Omega \cap Y_g'$

$$
c(a) = \{y \in \Omega^2; \mu'(y) = \operatorname{tr}(ay)\}.
$$

Then the cone decomposition

$$
\Sigma_{\text{cent}} = \{\sigma = c(a)\}_{a \in \Omega \cap Y_g'}
$$

93

is admissible.
Moreover this decomposition is of projective type with the polar function $\mu'(y)$.

A halfinteger positive matrix $a \in \Omega \cap Y_g'$ is called central if the cone $c(a)$ has the biggest dimension.

For $g \leq 3$ the principal cone (see below (8.10)) is the unique maximal cone up to $G(g, \mathbb{Z})$.
For $g = 4, 5$ besides the principal cone there appears a cone $\sigma_{12} = c(a_{12})$ defined by a central form

$$
a_{12} = \begin{cases}
1 &amp; 0 \quad 1/2 \cdots \quad 1/2 \\
0 &amp; 1 \quad 1/2 \cdots \quad 1/2 \\
1/2 &amp; 1/2 \quad 1 \quad \vdots \quad \vdots \\
\vdots &amp; \vdots \quad \ddots \quad \vdots \\
\vdots &amp; \vdots \quad \ddots \quad 1/2 \\
1/2 &amp; 1/2 \quad \cdots \quad 1/2 \quad 1
\end{cases}
$$

and these two cones exhaust $\Omega^2$ by the action of $GL(g, \mathbb{Z})$.
The cone $\sigma_{12}$ turns out not to be regular.
For $g \geq 6$ also the above two types of cones appear but the precise structure of $\Sigma_{\text{cent}}$ is not known.

This decomposition has been studied by Igusa [15] who obtained all central forms up to $g = 4$.
For $g = 5$ see [23] p.111.

The toroidal compactification associated with this decomposition is nothing but the normalization of the blowing-up of the Satake compactification along the boundary.
Together with (7.19) the above explicit structure of the central cone decomposition implies the following main result of Igusa in [15].

**Theorem (8.9.1).** Let $n \geq 3$.
(Then $\Gamma(n)$, (1.8) iii), is neat.)
The (normalization of the) blowing-up of the Satake compactification $(\Gamma(n) \backslash \mathfrak{S}_g)^\top$ along the boundary is nonsingular for $g \leq 3$ but singular for $g \geq 4$.

## (8.10) Principal cone.

In all the first three decompositions in (8.5) there appears a special cone in common which we call principal cone and plays an essential role as we have already seen in (8.6) partly.

It is defined as

$$
\sigma_o = \{y = (y_{ij}) \mid y_{ij} \leq 0 \ (i \neq j), \ \sum_{j=1}^{g} y_{ij} \geq 0\}
$$

94

$$
= \left\{ \sum_{i=1}^{g} \lambda_{i,g+1}x_i^2 + \sum_{1 \leq i &lt; j \leq g} \lambda_{ij}(x_i - x_j)^2; \lambda_{ij} \geq 0, \lambda_{i,g+1} \geq 0 \right\}
$$

(Here we identify a matrix $y = (y_{ij})$ and a quadratic form $\sum_{i,j} y_{ij}x_i x_j$.)
which is clearly a maximal and regular cone contained in $\Omega^1$.

Now for

$$
a_o = \begin{pmatrix} 1 &amp; \cdots &amp; 1/2 \\ \cdots &amp; 1/2 &amp; \cdots \\ 1/2 &amp; \cdots &amp; 1 \end{pmatrix} = \frac{1}{2}(x_1^2 + \cdots + x_g^2 + (x_1 + \cdots + x_g)^2)
$$

we see that

$$
\sigma_o = \sigma(a_o) = c(a_o),
$$

i.e. $a_o$ is both perfect and central.
The former equality is easy to see and the latter is shown similarly as in (8.7.1). (Use $a_{ij} = \frac{1}{2}(\sum_{k \neq i,j}^{g+1} x_k^2 + (x_i - x_j)^2$ with $x_{g+1} = -(x_1 + \cdots + x_g)$, $1 \leq i &lt; j \leq g+1$.)

For $g \leq 3$, $\sigma_o$ is the unique maximal cone in those three decompositions up to $\mathrm{GL}(g, \mathbb{Z})$ but not for $g \geq 4$.

The form

$$
a_{12} = \frac{1}{2}((x_1 - x_2)^2 + \sum_{i=3}^{g} x_i^2 + (x_1 + \cdots + x_g)^2)
$$

in (8.9) is also both perfect and central, and $\sigma_o$ is not conjugate to $\sigma(a_{12})$ nor $c(a_{12})$ for $g \geq 4$.
For $g = 4$, $\sigma(a_{12}) = c(a_{12})$ but for $g \geq 5$, $\sigma(a_{12}) \leq c(a_{12})$.

The relation between the first and the second Voronoi decompositions ((8.4) 1), 3)) seems interesting.
The central problem is:

whether the second Voronoi decomposition is a refinement of the first.

Dickson [9] has shown that a cone $\sigma$ appears in the both decompositions iff $\sigma$ is conjugate to a principal cone by $\mathrm{GL}(g, \mathbb{Z})$.

§9. An application of the Voronoi compactification to the theory of moduli of polarized abelian varieties.

(9.1) The toroidal compactification of $\mathbf{G}*{\mathbf{g}}^{\mathbf{s}} = \mathrm{Sp}(\mathbf{g},\mathbb{Z})\backslash \mathbf{G}*{\mathbf{g}}$ associated with the $2^{\mathrm{nd}}$ Voronoi reduction theory (8.5) 3) has a remarkable geometric meaning.
As is wellknown the space $\mathbf{G}*{\mathbf{g}}^{\mathbf{s}}$ can be interpreted as the (coarse) moduli space of principally polarized abelian varieties of dimension $\mathbf{g}$ ($\rightarrow$ (9.19)). Namely every point of $\mathbf{G}*{\mathbf{g}}^{\mathbf{s}}$ corresponds bijectively to an isomorphism class of a principally polarized abelian variety of dimension $\mathbf{g}$.
If one considers $(\mathbf{G}_{\mathbf{g}}^{\mathbf{s}})^{\gamma}$ associated with the $2^{\mathrm{nd}}$ Voronoi decomposition, then every boundary point also corresponds to a polarized singular variety to which abelian varieties degenerate.
From function theoretic point of view it can be regarded as a degeneration of theta functions.
We here sketch an outline of this theory, whose more precise and complete description can be found in [23].

A) $2^{\mathrm{nd}}$ Voronoi reduction theory.

**Definition (9.2).** Let $\mathbf{y} \in \mathbf{W}*{\mathbf{g}}^{+} = \Omega$.
Then $\mathbf{y}$ endows a metric on a g-dimensional vector space $V^{\mathbf{s}}$ (= $\mathbb{R}^{\mathbf{g}}$) by $\| \mathbf{x} \|*{y}^{2} = xy^{t} x$ for $x \in V^{\mathbf{s}}$.

i) For $a_1, \dots, a_k \in V_{\mathbb{Z}}^{\mathbf{s}}$ (= $\mathbb{Z}^{\mathbf{g}}$) we denote by $D(a_1, \dots, a_k)$ the convex hull generated by $a_i$'s, i.e. $\{\sum_{i=1}^{k} \lambda_i a_i; \sum \lambda_i = 1, \lambda_i \geq 0\}$.
We say that $D(a_1, \dots, a_k)$ is a Delaunay cell (abbreviated to a D-cell) if there exists a vector $\alpha \in V^{\mathbf{s}}$ such that for $a \in V_{\mathbb{Z}}^{\mathbf{s}}$, $\|a - \alpha\|*y = \min*{\xi \in V_{\mathbb{Z}}^{\mathbf{s}}} \| \xi - \alpha \|_y$

iff $a = a_i$ for $\exists i = 1, \dots, k$.

ii) For a Delaunay cell $\sigma = D(a_1, \dots, a_k)$ we define $\Delta = \Delta(\sigma) \subset V = \operatorname{Hom}(V^{\mathbf{s}}, \mathbb{R})$ ($\geq \mathbb{R}^{\mathbf{g}}$ with the dual base) to be $\Delta = \{-2\alpha y \in \mathbb{R}^{\mathbf{g}}; \|a_1 - \alpha\|*y = \min*{\xi \in \mathbb{Z}^{\mathbf{g}}} \| \xi - \alpha \|_y\}$, and call it the Voronoi cell (abbreviated to V-cell) corresponding to $\sigma$.

**Proposition (9.3).** i) The D-cells and V-cells are bounded, piecewise linear and have only a finite number of faces.
ii) All faces of D-cells (resp.
V-cells) are again D-cells (resp.
V-cells).

96

iii) For two D-cells (resp.
V-cells) $\sigma_1, \sigma_2$ the intersection $\sigma_1 \cap \sigma_2$ is a common face of $\sigma_1$ and $\sigma_2$.

iv) We have a bijection

$$
\begin{array}{c c c}
\{0\text{-dimensional D-cells}\} &amp; \stackrel{\circ}{\sim} &amp; \mathbb{Z}^g \\
\smile &amp; &amp; \smile \\
\{a\} &amp; \longleftarrow &amp; a.
\end{array}
$$

v) For two D-cells $\sigma_1, \sigma_2, \sigma_1$ is a face of $\sigma_2$ iff $\Delta(\sigma_2)$ is a face of $\Delta(\sigma_1)$.

vi) For a D-cell $\sigma$

$$
\dim \sigma + \dim \Delta(\sigma) = g.
$$

vii) For a D-cell $\sigma$ and $\xi \in \mathbb{Z}^g$ the translation $\sigma + \xi$ is again a D-cell and

$$
\Delta(\sigma + \xi) = \Delta(\sigma) - 2\xi y.
$$

viii) The number of classes of D-cells modulo $\mathbb{Z}^g$ is finite.

ix) If $\sigma$ is a D-cell with respect to $y$, then for $u \in GL(g, \mathbb{Z})$, $\sigma u^{-1}$ is a D-cell with respect to $u y^t u$ and

$$
\Delta_{u y^t u} (\sigma u^{-1}) = \Delta_y (\sigma)^t u.
$$

The proof is elementary.

**Definition (9.4).**

i) The decomposition $\{\sigma\}$ of $V^*$ with D-cells is called the *Delaunay decomposition* of $V^*$ with respect to $y$.

ii) The decomposition $\{\Delta\}$ of $V$ with V-cells is called the *Voronoi decomposition* of $V$ with respect to $y$.

The above proposition (9.3) says that these two decompositions are dual to each other.

**Remark (9.5).**

For $y \in \Omega^1$ (the rational closure) one can define such decompositions similarly.
In particular if $y = \begin{pmatrix} 0 &amp; 0 \\ 0 &amp; y^* \end{pmatrix}$, $y^* \in \Omega_{g^*^*}$, then

$$
\sigma = \mathbb{R}^{g - g^*} \times \sigma^*, \quad \sigma^* : D\text{-cell w.r.t. } y^*,
$$

97

$$
\Delta_y(\sigma) = \{0\} \times \Delta_{y''}(\sigma''), \quad \Delta_{y''}(\sigma'') : \text{V-cell w.r.t. } y''.
$$

Examples (9.6).

1. $g = 1$, $y = (1)$.

![img-16.jpeg](img-16.jpeg)

11. $g = 2$.
    a) $y = \begin{pmatrix} 1 &amp; 0 \\ 0 &amp; 1 \end{pmatrix}$.

$\sigma_0 = \{(0, 0)\}$

$\sigma_{11} = D((0, 0), (1, 0))$

$\sigma_{12} = D((0, 0), (0, 1))$

$\sigma_2 = D((0, 0), (0, 1), (1, 0), (1, 1))$

$\Delta(\sigma_0) = D((1, 1), (1, -1), (-1, 1), (-1, -1))$

$\Delta(\sigma_{11}) = D((-1, 1), (-1, -1))$

$\Delta(\sigma_{12}) = D((1, -1), (-1, -1))$

$\Delta(\sigma_2) = \{(-1, -1)\}$

![img-17.jpeg](img-17.jpeg) V\*

![img-18.jpeg](img-18.jpeg) V

98

$$
b) \ y = \left( \begin{array}{cc} 2 &amp; -1 \\ -1 &amp; 2 \end{array} \right).
$$

$$
\sigma_0 = \{(0, 0)\},
$$

$$
\sigma_{11} = D((0, 0), (1, 0)),
$$

$$
\sigma_{12} = D((0, 0), (1, 1)),
$$

$$
\sigma_{13} = D((0, 0), (0, 1)),
$$

$$
\sigma_{21} = D((0, 0), (1, 0), (1, 1)),
$$

$$
\sigma_{22} = D((0, 0), (0, 1), (1, 1)).
$$

$$
\Delta(\sigma_0) = D((2, 0), (0, 2), (-2, 2), (-2, 0), (0, -2), (2, -2)),
$$

$$
\Delta(\sigma_{11}) = D((-2, 0), (-2, 2)),
$$

$$
\Delta(\sigma_{12}) = D((-2, 0), (0, -2)),
$$

$$
\Delta(\sigma_{13}) = D((0, -2), (2, -2)),
$$

$$
\Delta(\sigma_{21}) = \{(-2, 0)\},
$$

$$
\Delta(\sigma_{22}) = \{(0, -2)\}.
$$

![img-19.jpeg](img-19.jpeg) V\*

![img-20.jpeg](img-20.jpeg) V

$$
y = \left( \begin{array}{ccc} g &amp; &amp; \\ &amp; \ddots &amp; -1 \\ -1 &amp; &amp; g \end{array} \right) \in \Omega_g.
$$

99

Set $I = \{1, \cdots, g\}$.
For a subset $I'$ of $I$ let $e_{I'}$ be a $g$-vector whose $i$-th coefficient is 1 or 0 according as $1 \leq I'$ or $1 \leq I'$.
Then for $0 \leq g' \leq g$ any $g'$-dimensional $D$-cell can be translated by an integral vector in $V_{\mathbb{Z}}^{\#}$ to $D(e_{I_0}, \cdots, e_{I_g'})$ where $\phi = I_0 \leq I_1 \leq \cdots \leq I_{g'}$.
For a permutation $\pi$ of $I$ we define $I_k = \{\pi(1) ; 1 \leq i \leq k\}$ which determines a $g$-dimensional $D$-cell $D(\pi) = D(e_{I_0}, \cdots, e_{I_g'})$ and conversely any $g$-dimensional $D$-cell is translated by $V_{\mathbb{Z}}^{\#}$ to a unique $D(\pi)$.
The corresponding $V$-cell is

$$
\Delta(\pi) = \{(a_1, \cdots, a_g) ; a_1 = 2\pi(1) - g - 2\}.
$$

(9.7) One sees that

$$
y = \begin{pmatrix} \lambda_1 &amp; 0 \\ 0 &amp; \lambda_2 \end{pmatrix}, \quad \lambda_1, \lambda_2 &gt; 0,
$$

defines the same Delaunay decomposition as $y = \begin{pmatrix} 1 &amp; 0 \\ 0 &amp; 1 \end{pmatrix}$ and

$$
y = \begin{pmatrix} \lambda_1 + \lambda_3 &amp; -\lambda_3 \\ -\lambda_3 &amp; \lambda_2 + \lambda_3 \end{pmatrix}, \quad \lambda_1, \lambda_2, \lambda_3 &gt; 0,
$$

does as $y = \begin{pmatrix} 2 &amp; -1 \\ -1 &amp; 2 \end{pmatrix}$.
This observation leads us the following definition.

**Definition (9.8).** For $y \in \Omega^2$ we set

$$
\begin{aligned}
\Sigma(y)^\circ &amp;= \{y' \in \Omega^2 \mid D\text{-decomposition w.r.t. } y' \\
&amp;= D\text{-decomposition w.r.t. } y\},
\end{aligned}
$$

and

$$
\Sigma(y) = (\Sigma(y)^\circ)^{-}
$$

which we call a *Delaunay-Voronoi cone* (abbreviated to a *D-V cone*).

We see that the relative interior of $\Sigma(y)$ ($= \Sigma(y)$ - proper faces) is then $\Sigma(y)^\circ$, which justifies the notation.
By definition we can say a Delaunay cell or Voronoi cell with respect to $\Sigma$.

**Theorem (9.9) (Voronoi).** The D-V cones $\{\Sigma\}$ form a $\mathrm{GL}(g, \mathbb{Z})$-admissible cone decomposition of $\Omega^2$ (8.3) which we call the (2nd) Voronoi decomposition ((8.5) 3)).

100

## Example (9.10)

In the case of $g = 2$ the 2nd Voronoi decomposition is given as in (2.3).

### B) Mixed decomposition of $\Omega^1 \times V$.

**Lemma (9.11)**. Let $y \in \Omega^1$ and $\sigma = D(a_1)_{1 \in I}$ a D-cell w.r.t. $y$.
Then the corresponding V-cell can be expressed in the form

$$
\begin{aligned}
\Delta_y(\sigma) &amp;= \{x \in V; \xi y^t(\xi + 2a_1) + \xi^tx \geq 0 \\
\text{for } \forall \xi \in \mathbb{Z}^g, \forall 1 \in I\}.
\end{aligned}
$$

### Proof

Clear from the equality

$$
\begin{aligned}
\|(\xi + a_1) - \alpha \|_{y}^2 - \|a_1 - \alpha \|_{y}^2 \\
= \xi y^t(\xi + 2a_1) - 2\alpha y^t\xi.
\end{aligned}
$$

### Definition (9.12)

Let $\Sigma$ be a D-V cone and $\sigma = D(a_1)*{1 \in I}$ a D-cell w.r.t. $\Sigma$.
Then the cone $K*{\Sigma,\sigma}$ in $\mathcal{Y}_g \times V$ defined by

$$
\begin{aligned}
K_{\Sigma,\sigma} &amp;= \{(y, z) \in \Sigma \times V; \xi y^t(\xi + 2a_1) + \xi^tx \geq 0 \\
\text{for } \forall \xi \in \mathbb{Z}^g, \forall 1 \in I\}
\end{aligned}
$$

is called a *mixed cone*.

If we consider the projection $p: \mathcal{Y}_g \times V \to \mathcal{Y}*g$, then $K*{\Sigma,\sigma}$ is mapped onto $\Sigma$ and the fibre over $y \in \Sigma^\circ$ is nothing but $\Delta_y(\sigma)$ (9.11). Hence by (9.3) and (9.9) mixed cones form a p.p.r. decomposition in $\mathcal{Y}_g \times V$ which we call the *mixed decomposition* of $\Omega^1 \times V$.

$$
\begin{aligned}
p: \Omega^1 \times V &amp;\to \Omega^1 \\
u &amp; u \\
K_{\Sigma,\sigma} &amp;\to \Sigma \\
u &amp; u \\
\Delta_y(\sigma) &amp;\to y.
\end{aligned}
$$

(9.13) Let $\mathcal{G}*{\mathbb{Z}}$ be a semidirect product group $\mathrm{GL}(g, \mathbb{Z}) \cdot V*{\mathbb{Z}}^{\bullet}$ with commutating relation $\xi \cdot u = u \cdot (\xi u)$ for $u \in \mathrm{GL}(g, \mathbb{Z})$ and $\xi \in V_{\mathbb{Z}}^{\bullet}$.
This group $\mathcal{G}_{\mathbb{Z}}$ acts linearly on $\mathcal{Y}_g \times V$ as

101

$$
u: (y, x) \longrightarrow \left(u y ^ {t} u, x ^ {t} u\right)
$$

$$
\xi: (y, x) \longrightarrow (y, x + \xi y).
$$

Then the action of $G_{\mathbb{Z}}$ preserves the mixed decomposition ((9.3), vii), ix)).

Example (9.14).

1. $g = 1$ .

![img-21.jpeg](img-21.jpeg)

$$
\begin{array}{r l} {1 1)} &amp; {\mathrm {g} = 2, \quad \Sigma = \Sigma_ {2} = \{y = \left( \begin{array}{c c} \lambda_ {1} + \lambda_ {3} &amp; - \lambda_ {3} \\ - \lambda_ {3} &amp; \lambda_ {2} + \lambda_ {3} \end{array} \right);} \\ &amp; {\lambda_ {1} \geq 0, \lambda_ {2} \geq 0, \lambda_ {3} \geq 0 \}.} \end{array}
$$

$$
\sigma = \sigma_ {0}, \quad (9.6) \quad 11).
$$

$$
K _ {\Sigma , \sigma} = \left\{\left( \begin{array}{c c} \lambda_ {1} + \lambda_ {3} &amp; - \lambda_ {3} \\ - \lambda_ {3} &amp; \lambda_ {2} + \lambda_ {3} \end{array} \right), x _ {1}, x _ {2}) \right\};
$$

$$
\lambda_ {1} + \lambda_ {3} \geq x _ {1} \geq - (\lambda_ {1} + \lambda_ {3}),
$$

$$
\lambda_ {2} + \lambda_ {3} \geq x _ {2} \geq - (\lambda_ {2} + \lambda_ {3}),
$$

$$
\lambda_ {1} + \lambda_ {2} \geq x _ {1} + x _ {2} \geq - (\lambda_ {1} + \lambda_ {2}) \}.
$$

102

The V-cell $p^{-1}(y) \cap K_{\Sigma, \sigma}$ varies as follows.

![img-22.jpeg](img-22.jpeg)

![img-23.jpeg](img-23.jpeg)

![img-24.jpeg](img-24.jpeg)

$(\lambda_1, \lambda_2, \lambda_3) = (1, 1, 1) \longrightarrow (1, 1, \frac{1}{2}) \longrightarrow (1, 1, 0) \in \Sigma_1$

C) Compactification of the moduli space of polarized abelian varieties.

Notation (9.15).

1. For

$$
G = \operatorname{Sp}(g, \mathbb{R}), \quad R = \mathbb{R}^{2g} \quad \text{(row vectors)}
$$

set

$\hat{\mathcal{Q}} = G \cdot \mathbb{R}$ semidirect product with commutating relation:

$$
\chi \cdot M = M \cdot (\chi M) \quad \text{for} \quad M \in G, \quad \chi \in \mathbb{R}.
$$

Then $\mathbb{R}$ is the radical of $\hat{\mathcal{Q}}$ and $\hat{\mathcal{Q}}$ acts on $\mathcal{C}_g \times \mathbb{T}^g$ as

$$
M = \left( \begin{array}{cc} A &amp; B \\ C &amp; D \end{array} \right) \in G: (\tau, \zeta) \to (M \cdot \tau, \zeta (C \tau + D)^{-1}),
$$

$$
\chi \in \mathbb{R}: (\tau, \zeta) \to (\tau, \zeta + \chi \left( \begin{array}{c} \tau \\ 1 \end{array} \right)).
$$

ii) For $\Gamma = \operatorname{Sp}(g, \mathbb{Z}) \subset G$, $X = \mathbb{Z}^{2g} \subset \mathbb{R}$, set

$$
\hat{\Gamma} = \Gamma \cdot X \subset \hat{\mathcal{Q}}.
$$

103

Let $X$ act on the trivial line bundle $(\mathcal{G}_g \times \mathfrak{C}^g) \times \mathfrak{C}$ as

$$
\begin{array}{l}
\chi = (\chi', \chi'): (\tau, \zeta, \theta) \rightarrow (\tau, \zeta + \chi' \tau + \chi'', \\
\underline{e}(-\frac{1}{2} \chi' \tau^t \chi' - \chi'^t \zeta) \theta)
\end{array}
$$

where $\underline{e}(.) = \exp(2\pi \sqrt{-1}(.))$.

**Proposition (9.16).** i) $\chi$ acts on $\mathcal{G}_g \times \mathfrak{C}^g$ properly discontinuously.

ii) $X$ acts on $\mathcal{G}_g \times \mathfrak{C}^g$ freely and

$$
\mathfrak{L}: A_g := (\mathcal{G}_g \times \mathfrak{C}^g)/X \rightarrow \mathcal{G}_g
$$

is a family of abelian varieties on which $\Gamma$ acts.

iii) $L_g = \mathcal{G}*g \times \mathfrak{C}^g \times \mathfrak{C}/X$ is a line bundle on $A_g$ relatively ample with respect to $\mathfrak{L}$ with $\mathfrak{L}** L_g = \mathcal{O}_{\mathcal{G}_g}$ (principal polarization).

iv) For $\tau \in \mathcal{G}*g$ we write $A*\tau = \mathfrak{L}^{-1}(\tau)$, $L_\tau = L_{g|A_\tau}$.
Then for $\tau_1, \tau_2 \in \mathcal{G}*g$, $(A*{\tau_1}, L_{\tau_1}) \supseteq (A_{\tau_2}, L_{\tau_2})$ (as polarized varieties iff $\mathfrak{A}_M \in \Gamma$ with $\tau_2 = M \cdot \tau_1$).

**Proof (except iii), iv).** i) It is easy to show that $X$ acts on $\mathcal{G}_g \times \mathfrak{C}^g$ properly discontinuously and we know already that $\Gamma$ acts $\mathcal{G}_g$ properly discontinuously.
Then we can apply Lemma (7.11.2) to the projection: $\mathcal{G}_g \times \mathfrak{C}^g \to \mathcal{G}_g$ and the natural homomorphism: $\mathfrak{F} \to \mathfrak{F}/X \stackrel{\sim}{\to} \Gamma$.

ii) It is straightforward to show that $X$ acts on $\mathcal{G}_g \times \mathfrak{C}^g$ freely and moreover that the quotient $\mathfrak{L}: \mathcal{G}_g \times \mathfrak{C}^g/X \to \mathcal{G}_g$ is a smooth family of complex tori on which $\Gamma$ ($\supseteq \Gamma/X$) acts.
The next claim iii) asserts that all fibres are abelian varieties.

iii) and iv) are well-known main theorems in the theory of abelian varieties (see [16] for example).
Here we only note that the trivialization $\mathfrak{L}** L_g \supseteq \mathcal{O}*{\mathcal{G}_g}$ is given by a theta function

$$
\theta(\tau, \zeta) = \sum_{\xi \in \mathcal{Z}^g} \underline{e}\left(\frac{1}{2} \xi \tau^t \xi + \xi^t \zeta\right)
$$

with the identification

$$
\Gamma(\mathcal{G}_g, \mathfrak{L}_* L_g) \supseteq \Gamma(A_g, L_g) \supseteq \Gamma(\mathcal{G}_g \times \mathfrak{C}^g, \mathcal{O}_{\mathcal{G}_g \times \mathfrak{C}^g})^X.
$$

Q. E. D.

104

Remark (9.17).

1. We can define the action of $\Gamma$ on $L_g$ (which proves the half of (9.16) iv)), which is different from that on $A_g$ above up to translation by a suitable point of order 2 in each fibre (cf.
   [16] Chap.II).

ii) The above family of polarized abelian varieties descends to the one over $U_g' \backslash \mathcal{G}_g = \mathbb{Z}_g^\circ$ where $U_g' = \{ [b] \in U_g; b \in 0 \pmod{2} \}$.

Definition (9.18). A pair $(A, L)$ of an abelian variety $A$ and an ample line bundle $L$ on $A$ with $\dim \Gamma(A, L) = 1$ is called a principally polarized abelian variety.

The above (9.16) shows that $(\mathfrak{L} : A_g \to \mathcal{G}_g, L_g)$ is a family of principally polarized abelian varieties.

Theorem (9.19).

1. The space $\mathcal{G}_g^* = \mathrm{Sp}(g, \mathbb{Z}) \backslash \mathcal{G}_g$ is the coarse moduli space of principally polarized abelian varieties of dimension $g$.

ii) The identification of $\mathcal{G}_g^*$ with the set $p.p.AV(g)$ of isomorphism classes of principally polarized abelian varieties of dimension $g$ is given by

$$
\begin{array}{c}
\mathcal{G}_g^* \longleftrightarrow p.p.AV(g) \\
\swarrow \\
\tau \bmod \Gamma \longrightarrow (A_\tau, L_\tau)
\end{array}
$$

(cf.
(9.16) iv)).

iii) For each point $\tau \bmod \Gamma$ there are an open neighbourhood $U$ of $\tau \bmod \Gamma$, a Galois covering $p: V \to U$ with $p^{-1}(\tau \bmod \Gamma) = 0$ whose covering group is $\operatorname{Iso}(\tau)/\pm 1$ ($&lt; \Gamma/\pm 1$) and a family of principally polarized abelian varieties $(\pi: A_V \to V, L_V)$ such that for each $v \in V$ the isomorphism class of $(A_V = \pi^{-1}(v), L_V = L_{V|A_V})$ corresponds to $p(v)$ in $\mathcal{G}*g^*$.
Moreover $\operatorname{Iso}(\tau)$ acts on $\pi: A_V \to V$ and this action induces an isomorphism: $\operatorname{Iso}(\tau) \stackrel{\sim}{\to} \operatorname{Aut}(A*\circ, L_\circ)$.
(Clear from the fact that $\mathcal{G}_g^*$ is locally isomorphic to $\mathcal{G}_g / \operatorname{Iso}(\tau)$ near $\tau$.)

Now we can state the main result in this section, which gives an algebro-geometric meaning of the Voronoi compactification by extending the above theorem.

Main Theorem (9.20). Consider the toroidal compactification $(\mathcal{G}_g^*)^\gamma$ of $\mathcal{G}_g^* = \mathrm{Sp}(g, \mathbb{Z}) \backslash \mathcal{G}_g$ associated with the second Voronoi decomposition (cf.
(8.3)), which we call the Voronoi compactification.

105

Each point of the Voronoi compactification corresponds to a polarized variety which is in $\mathbb{G}_{\mathbf{g}}^{\bullet}$ the corresponding principally polarized abelian variety in (9.19). This correspondence has the following properties.

1. (cf.
   (9.19) iii)) For each point $x \in (\mathbb{G}*{\mathbf{g}}^{\bullet})^{\overline{\mathbf{r}}}$ there are an open neighbourhood $U$ of $x$, a finite Galois covering $p: V \to U$ with $p^{-1}(x) = 0$ with its covering group $G$ and a polarized family $(\hat{\pi}: \hat{A}*V \to V, \hat{L}*V)$ such that for each $v \in V$ the point $p(v)$ corresponds to the fibre $(A_V = \hat{\pi}^{-1}(v), L_V = L*{V|A_V})$ and the extension $\hat{G}$ of $G$ by $\{\pm 1\}$ acts on $\hat{\pi}$.
   Moreover this $\hat{G}$ is isomorphic to $\operatorname{Iso}(\hat{\mathbf{x}}) \subset \Gamma$ where $\hat{\mathbf{x}}$ is a point in $(U*{\mathbf{g}}, \backslash \mathcal{D})*{\Sigma_{\mathbf{g}}}$, with $\pi_{\mathbf{F}*{\mathbf{g}}}, (\hat{\mathbf{x}}) = x$ and $p*{\mathbf{g}}, (\hat{\mathbf{x}}) \in P_{\mathbf{g}}, \backslash F_{\mathbf{g}}, \subset (\Gamma \backslash \mathcal{D})^{\overline{\mathbf{r}}}$ where $\pi_{\mathbf{F}*{\mathbf{g}}}: (U*{\mathbf{g}}, \backslash \mathcal{D})*{\Sigma*{\mathbf{g}}}, \to (\Gamma \backslash \mathcal{D})^{\overline{\mathbf{r}}}$ and $p_{\mathbf{g}}: (U_{\mathbf{g}}, \backslash \mathcal{D})*{\Sigma*{\mathbf{g}}}, \to (\Gamma \backslash \mathcal{D})^{\overline{\mathbf{r}}}$ (7.15).

ii) We consider $\hat{\mathbf{x}} \in (U_{\mathbf{g}}, \backslash \mathcal{D})*{\Sigma*{\mathbf{g}}}$, as above in 1). Moreover we suppose that $\overline{\pi}'(\hat{\mathbf{x}}) = (\tau', \tau'') \in \mathbb{G}*{\mathbf{g}}, \times V*{\mathbf{g}}$, for $\overline{\pi}': (U_{\mathbf{g}}, \backslash \mathcal{D})*{\Sigma*{\mathbf{g}}}, \to \mathcal{D}(F_{\mathbf{g}},)' \supsetneq \mathbb{G}*{\mathbf{g}}, \times V*{\mathbf{g}}$, and $\hat{\mathbf{x}} \in O(\Sigma)$ for a D-V cone $\Sigma \in \Sigma_{\mathbf{g}}$, with $\Sigma \cap \Omega_{\mathbf{g}}' \neq \varphi$ ($g'' = g - g'$) (7.7). In other words $\hat{\mathbf{x}}$ is a limit of $\left[ \begin{array}{cc} \tau' &amp; \tau''' \\ \tau''' &amp; \tau''' \end{array} \right]$ mod $\Gamma$ with $\tau' \in \mathbb{G}_{\mathbf{g}}, \tau''' \in M(\mathbf{g}', \mathbf{g}'', \mathbb{C})$, and $\operatorname{Im} \tau'' \to \infty$ in the direction of $\Sigma$.

Then the structure of the variety $A_{x}$ corresponding to $x$ is as follows.

a) $A_{x}$ has a stratification

$$
A _ {x} = \underline {{U}} _ {\sigma} O (\bar {\sigma})
$$

where the index set is $\{D$-cells w.r.t. $\Sigma\}$ mod $V_{\Sigma}^{\bullet}$.

b) For a D-cell $\sigma$ w.r.t. $\Sigma$ the corresponding stratum $O(\overline{\sigma})$ is a commutative group variety with an exact sequence

$$
1 \rightarrow T _ {\overline {{\sigma}}} \rightarrow O (\overline {{\sigma}}) \rightarrow A _ {\tau}, \rightarrow 0
$$

where $A_{\tau'} = \mathbb{C}^{g'} / (\tau', 1_{g'}) \mathbb{Z}^{2g'}$ (g'-dimensional abelian variety corresponding to $\tau' \in \mathbb{G}*{g'}$) and $\underline{T}*{\overline{\sigma}} \supseteq (\mathbb{C}^{\bullet})^{\dim \sigma}$.
The extension class of this exact sequence is determined by $\tau'''$.
(Note that $A_{\tau'}$ corresponds to $p(x) \in (\Gamma \backslash \mathcal{D})^{\overline{\sigma}}$ and appears in common in all strata but in general $A_{x}$ has no global fibre structure over $A_{\tau'}$, see (9.22) ii) a).)

106

c) The adherence relation of the stratification $\{O(\overline{\sigma})\}$ is given by that of the Delaunay decomposition w.r.t. $\Sigma$.

*Remark (9.21).* i) The letter "$\overline{\sigma}$", pronounced as "te", is the initial of theta function in Japanese.
The reason why we employed this notation is given in the next remark.

ii) The varieties appearing in corresponding to the boundary points are constructed essentially by using "degenerating" theta functions as follows.
Consider the descended family of polarized abelian varieties over $\mathcal{Z}_{\mathbf{g}}^{\circ}$ in (9.17) ii),

$$
\mathfrak{L}^{\circ}: A_{\mathbf{g}}^{\circ} = U_{\mathbf{g}}^{\prime} \backslash A_{\mathbf{g}} \quad \rightarrow \quad \mathcal{Z}_{\mathbf{g}}^{\circ} = U_{\mathbf{g}}^{\prime} \backslash \mathcal{G}_{\mathbf{g}}, \quad L_{\mathbf{g}}^{\circ} = U_{\mathbf{g}}^{\prime} \backslash L_{\mathbf{g}}.
$$

For $m &gt;&gt; 0$ (actually $m \geq 3$) $\mathfrak{L}*{\mathbf{g}}^{\circ}((L*{\mathbf{g}}^{\circ})^{\mathfrak{m}})$ gives a projective embedding

$$
i: A_{\mathbf{g}}^{\circ} \subset \mathcal{Z}_{\mathbf{g}}^{\circ} \times \mathbb{P}^{N}, \quad N = m^{\mathbf{g}} - 1
$$

which can be expressed explicitly by using theta functions.
With the D-V decomposition $\{\Sigma\}$ we have a partial compactification $(\mathcal{Z}*{\mathbf{g}}^{\circ})*{\{\Sigma\}}$ (7.7). Now take the closure of $\operatorname{Im} i$ in $(\mathcal{Z}*{\mathbf{g}}^{\circ})*{\{\Sigma\}} \times \mathbb{P}^{N}$ to obtain a family

$$
\overline{\mathfrak{L}}^{\prime}: \overline{A}_{\mathbf{g}}^{\prime} \subset (\mathcal{Z}_{\mathbf{g}}^{\circ})_{\{\Sigma\}} \times \mathbb{P}^{N} \quad \rightarrow \quad (\mathcal{Z}_{\mathbf{g}}^{\circ})_{\{\Sigma\}}
$$

extending $\mathfrak{L}^{\circ}$.
Then for each $\overline{\mathbf{x}} \in (\mathcal{Z}*{\mathbf{g}}^{\circ})*{\{\Sigma\}}$, $\pi_{\mathcal{F}*{\mathbf{g}}}(\mathbf{x}) \in (\mathcal{G}*{\mathbf{g}}^{\circ})^{\overline{\mathbf{x}}}$ corresponds to a suitable finite quotient (isogeny) of the fibre of $\overline{\mathfrak{L}}$ over $\overline{\mathbf{x}}$.
Here we make essential use of the explicit form of theta functions.

iii) The result can be generalized for any type of polarizations in which case we change the arithmetic subgroup $(\Gamma(\Delta)$ in (1.8) ii)) and the decomposition suitably ([23] Part III).

*Idea of the proof of (9.20).* (For the complete proof see [23]) The method is almost word-for-word modification of the construction of $(\Gamma \backslash \mathcal{D})^{\overline{\mathbf{v}}}$.

Since $\pi_{\mathcal{F}*{\mathbf{g}}}: (U*{\mathbf{g}}^{\prime} \backslash \mathcal{D})_{\{\Sigma\}} \rightarrow (\Gamma \backslash \mathcal{D})^{\overline{\mathbf{v}}}$ is surjective, it is enough to extend the family

$$
\mathfrak{L}^{\circ}: A_{\mathbf{g}}^{\circ} = U_{\mathbf{g}}^{\prime} \backslash A_{\mathbf{g}} \quad \rightarrow \quad \mathcal{Z}_{\mathbf{g}}^{\circ} = U_{\mathbf{g}}^{\prime} \backslash \mathcal{G}_{\mathbf{g}}
$$

to a family

107

$$
\overline{\mathbb{U}} : \overline{A}_g \rightarrow (Z_g^\circ)_{\{\Sigma\}}.
$$

We set

$$
\begin{aligned}
\overline{P}_g &amp;:= P_g \cdot X \subset \overline{P}, \\
\widehat{U}_g &amp;:= U_g^\cdot \cdot X" \subset \overline{P}_g
\end{aligned}
$$

where $X" = \{(0\ \chi") \in X\ ;\ \chi" \in \mathbb{Z}^g\}$.

1. 1st step.
   Take the quotient by $\widehat{U}_g$.

Noting that $\mathcal{D}(F_g) \simeq \Psi_{g,\mathfrak{C}}$, we have

$$
\begin{aligned}
\mathcal{D}(F_g) \times \mathfrak{C}^g &amp;\rightarrow \mathcal{D}(F_g) \simeq \mathfrak{C}_g \\
\int \frac{\partial}{\partial F_g} &amp;\quad \int \frac{\partial}{\partial U_g^\cdot} &amp;\quad \int \frac{\partial}{\partial Z_g^\circ} \\
\mathcal{C}_g &amp;\rightarrow \mathcal{Z}_g &amp;\simeq \mathcal{Z}_g^\circ
\end{aligned}
$$

where $\mathcal{C}_g \simeq \mathcal{Z}_g \times (\mathfrak{C}^*)^g$.

2. 2nd step.
   Take the partial compactification with $\{K_{\Sigma,\sigma}\}$.

Identifying $\pi_1(\mathcal{C}_g)$ with $\widehat{U}_g$ and $(\widehat{U}*g)*{\mathbb{R}}$ with $\Psi_g \times V$, we construct the torus embedding $\mathbf{S}*g = (\mathcal{C}*g)*{\{K*{\Sigma,\sigma}\}}$ with the mixed decomposition.
The projection $p: \Psi_g \times V \to \Psi_g$ induces a morphism of torus embeddings

$$
\rho: \mathbf{S}_g \rightarrow (\mathcal{Z}_g)_{\{\Sigma\}}.
$$

The space $\mathbf{S}_g$ has the $\mathcal{C}_g$-orbit decomposition

$$
\underset{\Sigma,\sigma}{\mathrm{II}}\ O(\Sigma;\sigma)
$$

enjoying similar properties as in (7.7) and moreover that

$$
\rho^{-1}(O(\Sigma)) = \underset{\sigma: D\text{-cell w.r.t.}\Sigma}{\mathrm{II}}\ O(\Sigma;\sigma)
$$

and $\rho: O(\Sigma;\sigma) \to O(\Sigma)$ is a torus bundle of relative dim.
= $\dim \sigma$.

3. 3rd step.
   Take the quotient by $X/X"$.

We set

$$
\mathbf{S}_g^\circ = \rho^{-1} \left( (\mathcal{Z}_g^\circ)_{\{\Sigma\}} \right),
$$

108

for which we have the following claim:

**Claim (9.20.1).**

1. The action of $X/X''$ on $\mathfrak{C}_g$ extends to that on $\mathfrak{B}_g$.
   ($\because$) $(y, x) \rightarrow (y, x - 2x'y)$ for $x' \in \mathbb{Z}^g$ induces an automorphism of $\mathfrak{B}_g$ by (9.3) vii).
2. On $\mathfrak{B}_g^\circ$ the action of $X/X''$ is properly discontinuous and free.

Finally the quotient, which exists by the above claim,

$$
\bar{\mathfrak{F}}: \bar{A}_g := (X/X'') \setminus \mathfrak{B}_g^\circ \rightarrow (\mathbb{Z}_g^\circ)_{\{\Sigma\}}
$$

is the desired family.
The structure of the fibre is now easy to check by writing the action of $X/X''$ explicitly.
Q. E. D.

*Example (9.22).*

1. $g = 1$.

![img-25.jpeg](img-25.jpeg)

![img-26.jpeg](img-26.jpeg)

109

ii) $g = 2$.

a) $p = \lim_{t \to 0} \frac{\log t}{\sqrt{-1}} \begin{bmatrix} 0 &amp; 0 \\ 0 &amp; 1 \end{bmatrix} + \begin{bmatrix} \tau_1 &amp; \tau_3 \\ \tau_3 &amp; * \end{bmatrix} \mod \mathrm{Sp}(g, \mathbb{Z})$.

![img-27.jpeg](img-27.jpeg)

b) $p = \lim_{t \to 0} \frac{\log t}{\sqrt{-1}} \begin{bmatrix} 1 &amp; 0 \\ 0 &amp; 1 \end{bmatrix} + \begin{bmatrix} * &amp; \tau_3 \\ \tau_3 &amp; * \end{bmatrix} \mod \mathrm{Sp}(g, \mathbb{Z})$.

![img-28.jpeg](img-28.jpeg)

c) $p = \lim_{t \to 0} \frac{\log t}{\sqrt{-1}} \begin{bmatrix} 2 &amp; -1 \\ -1 &amp; 2 \end{bmatrix} \mod \mathrm{Sp}(g, \mathbb{Z})$.

![img-29.jpeg](img-29.jpeg)

glue each pair of lines

110

We see that the configuration of the fibre is exactly the Delaunay decomposition modulo $\mathbb{Z}^{\mathrm{g}}$ (cf.
(9.6)).

**Problem (9.23).**

1. Is the Vornoi compactification projective?
   (The answer is affirmative for $g \leq 4$.)
   ii) Is the 2nd Voronoi decomposition regular?
   (Yes for $g \leq 4$.)

**D)** The extension of Torelli map.

**(9.24)** For a smooth projective curve $C$ of genus $g$ we can construct the Jacobian variety $J(C)$ of $C$ which has a canonical structure of a principally polarized abelian varieties.
This correspondence $C \to J(C)$ gives a holomorphic map

$$
i: M_g \to G_g^*
$$

where $M_g$ denotes the coarse moduli space of smooth projective curves of genus $g$.

**Theorem (9.25).**

1. (Torelli [1], [23]) $i$ is injective.
   ii) (Oort-Steenbrink [25]) $i$ is an immersion.

The second statement is far from trivial and rather unexpected, for character of $i$ might be quite different at the points corresponding to hyperelliptic curves.

Now the space $M_g$ has a nice compactification $S_g$ of moduli of stable curves due to Deligne-Mumford.

**Definition (9.26)** (Deligne-Mumford-Mayer).
A complete curve $C$ is called a stable curve of genus $g$ (≥ 1) if

1. $C$ is reduced; ii) $C$ has only ordinary double points as possible singularities; iii) each nonsingular rational irreducible component of $C$ meets the other components at more than two points; iv) $\dim_{\mathbb{R}} H^1(C, O_C) = g$.

**Theorem (9.27)** (Mumford et al. [8], [21]).

1. The coarse moduli space $S_g$ of stable curves of genus $g$ exists and contains $M_g$ as a Zariski open subset.
   ii) $S_g$ is projective and irreducible.

Now we can state the main theorem in this paragraph.

Theorem (9.28) (Mumford, [23] §18). The map $i: M_g \to \mathbb{G}_g^*$ extends to a holomorphic map

![img-30.jpeg](img-30.jpeg)

Concerning the property of $j$ we can say the following.
Before stating the result we prepare a notion.

Definition (9.29). To a stable curve $C$ we associate a graph $\Gamma(C)$ as follows:

```txt
{vertices of  $\Gamma (C)\}$  = {irreducible components of C}, {edges of  $\Gamma (C)\}$  = {double points on C}, {terminal points of an edge} the corresponding double point lies}.
```

e.g.

![img-31.jpeg](img-31.jpeg) C

![img-32.jpeg](img-32.jpeg) $\Gamma (C)$

Theorem (9.30) ([22]).

1. The composite map $\mathrm{poj}: S_g \to (\mathbb{G}_g^*)^\overline{\tau} \to (\mathbb{G}_g^*)^\overline{\tau}$ maps the isomorphism class [C] of a stable curve C with irreducible components $C_1, i = 1, \dots, r$ , to the isomorphism class of $J(\mathcal{C}_1) \times \dots \times J(\mathcal{C}_r)$ where $\mathcal{C}*1$ denotes the normalization of $C_1$ . ii) We keep the notation in i), and let $g' = \sum*{i} \text{ genus of } \mathcal{C}_i$ . We have rank $H_1(\Gamma(C), \mathbb{Z}) = g'' := g - g'$ (elementary).
   Giving an orientation on $\Gamma(C)$ and regarding edges $\{e_k\}$ as 1-simplices,

112

we choose a basis $\{\gamma_1,\dots ,\gamma_{g''}\}$ of $H_{1}(\Gamma (C),2\mathbb{Z})$ and express them as

$$
\gamma_ {j} = \sum_ {k} a _ {j k} e _ {k}, \quad a _ {j k} \in 2 \mathbb {Z},
$$

to obtain a matrix $A = (a_{jk})$.
Then $j([C])$ is contained in the orbit $\overline{O}(\Sigma)$ where $\Sigma$ is the D-V cone in $\mathcal{G}_{g''}$ containing $A^t A$ in its relative interior.

iii) Consider an open set $(\mathrm{U_g}\backslash \underline{\mathbb{G}}*{\mathrm{g}})*{\sigma_0} = (\mathrm{U_g}\backslash \mathcal{D}(\mathrm{F_g}))*{\sigma_0}\cap (\mathrm{U_g}\backslash \underline{\mathbb{G}}*{\mathrm{g}})\{\Sigma \}$ in $(\mathrm{U_g}\backslash \underline{\mathbb{G}}*{\mathrm{g}})\{\Sigma \}$ where $\sigma_0$ is the principal cone (8.10), and set $\underline{\mathbb{G}}*{\mathrm{g}}^{\bullet})*{\circ}^{\overline{\gamma}} = p*{\mathrm{F}*{\mathrm{g}}}((\mathrm{U_g}\backslash \underline{\mathbb{G}}*{\mathrm{g}})*{\sigma_0}) &lt;   \underline{\mathbb{G}}*{\mathrm{g}}^{\bullet})^{\overline{\gamma}}$.
For a stable curve C if the associated graph $\Gamma (C)$ is planar (i.e. embeddable in $\mathbb{R}^2$), then $j([C])\in \underline{\mathbb{G}}*{\mathrm{g}}^{\bullet})*{\circ}^{\overline{\gamma}}$ where [C] is the isomorphism class of C in $S_{\mathrm{g}}$.

iv) Let $\underline{u}*{\mathbf{g}}$ be the open subset of $S*{\mathbf{g}}$ consisting of points corresponding to irreducible stable curves.
Then $j$ is injective on $\underline{u}_{\mathbf{g}}$.

v) In case $g = 2$, $j$ is an isomorphism.

vi) For $g \geq 3$ $j$ is not injective already when $j([C]) \in \underline{\mathbb{G}}*{\mathbf{g}}^{\bullet}$.
(Hence it has nothing to do with the compactification.)
Namely let $S*{\mathbf{g}', \mathbf{g}''}, \mathbf{g}' + \mathbf{g}'' = \mathbf{g}, \mathbf{g}' &gt; 0, \mathbf{g}'' &gt; 0$, be the closed subset of $S_{\mathbf{g}}$ whose general points correspond to a join of two smooth curves of genus $\mathbf{g}'$ and $\mathbf{g}''$ meeting at one point.

![img-33.jpeg](img-33.jpeg)

Then $j$ is not injective on $S_{\mathbf{g}', \mathbf{g}''}$ (since $j([C_1 \cup C_2]) = [J(C_1) \times J(C_2)] \in \underline{\mathbb{G}}_{\mathbf{g}}^{\bullet}$ but the isomorphism class of $C_1 \cup C_2$ depends not only on those of $C_1$ and $C_2$ but also on the point where $C_1$ and $C_2$ meet together).

Problem (9.31). i) Does the converse of iii) hold?

ii) Is $j$ injective on $S_{\mathbf{g}} - \cup S_{\mathbf{g}', \mathbf{g}''}$?

Appendix: Abstract theory of bounded symmetric domains (with explicit description in the case of Siegel upper-half plane)

Here we sum up the abstract (i.e. with Lie group theory) theory of the structure of bounded symmetric domains.
We employ the same notation and framework as in [2] Chapter III and then we give an explicit description in the case of Siegel upper half plane, which would help the reader to understand the contents of [2] written in the most general form.

We correct also a number of missprints in [2] pointed out with $(\star)$.

We indicate the corresponding place in [2] as follows:

[§2.1, p.166]... [2] Chapter III, §2.1, p.166.

I. The structure of bounded symmetric domains [§2].

A) Definition and realizations [§2.1, p.166 ff]

Definition 1. A complex hermitian manifold $\mathcal{D}$ is called a hermitian symmetric space if for each point $x \in \mathcal{D}$ there exists a biholomorphic and isometric involution $s_x$ with $x$ as an isolated fixed point (called symmetry at $x$).

Proposition 1. Any hermitian symmetric space $\mathcal{D}$ decomposes as

$$
\mathcal{D} = \mathcal{D}_0 \times \mathcal{D}_1 \times \dots \times \mathcal{D}_n
$$

where $\mathcal{D}_0$ is the quotient of a complex vector space by a discrete group of translations (called of euclidean type) and $\mathcal{D}_1$, $i &gt; 0$, is an irreducible non-euclidean hermitian symmetric space.

Definition 2. A non-euclidean irreducible hermitian symmetric space $\mathcal{D}$ is called of compact type (resp.
of non-compact type) if $\mathcal{D}$ is compact (resp.
not compact).

If $\mathcal{D}$ is of compact type, $\mathcal{D}$ is a rational projective variety (e.g. projective space, Grassmann variety), and if $\mathcal{D}$ is of non-compact type, $\mathcal{D}$ can be realized as a bounded domain in $\mathfrak{E}^n$, $n = \dim \mathcal{D}$, (see below).

Definition 3. A hermitian symmetric space $\mathcal{D}$ is called a bounded symmetric domain if $\mathcal{D}$ has no component of euclidean type nor of compact type.

Definition 4. If a non-euclidean symmetric space $\mathcal{D}$ consists of only one irreducible component, then $\mathcal{D}$ is called simple.

Theorem 1 (E. Cartan).
The simple bounded symmetric domains

114

can be classified as follows:

$$
\begin{array}{l}
I_{m,n}^{*}, m \geq n \geq 1, \quad \{Z \in M(m, n; \mathbb{C}); \, l_n - {}^{t}\overline{Z}Z &gt; 0\}; \\
II_{m}^{*}, m \geq 2, \quad \{Z \in M(m, \mathbb{C}); \, {}^{t}Z = -Z, \, l_m - {}^{t}\overline{Z}Z &gt; 0\}; \\
III_{m}^{*}, m \geq 1, \quad \{Z \in M(m, \mathbb{C}); \, {}^{t}Z = Z, \, l_m - {}^{t}\overline{Z}Z &gt; 0\}; \\
IV_{m}^{*}, m \geq 1, m \neq 2, \\
\{z \in \mathbb{C}^{m} ; \, |z_1|^2 + \cdots + |z_m|^2 &lt; (1 + |z_1|^2 + \cdots + z_m|^2) / 2 &lt; 1\};
\end{array}
$$

and two other exceptional types.

Among these there are following isomorphisms:

$$
\begin{array}{l}
I_{1,1}^{*} \supseteq II_{2}^{*} \supseteq III_{1}^{*} \supseteq IV_{1}^{*} \supseteq D, \\
II_{3}^{*} \supseteq I_{3,1}^{*}, \\
IV_{3}^{*} \supseteq III_{2}^{*}, \\
IV_{4}^{*} \supseteq I_{2,2}^{*}, \\
IV_{6}^{*} \supseteq II_{4}^{*}.
\end{array}
$$

In what follows we consider only bounded symmetric domains for simplicity.

**Fact 1.**

1. For a symmetric domain $\mathcal{D}$ the group $\operatorname{Aut}(\mathcal{D})$ of biholomorphic automorphisms of $\mathcal{D}$ admits a canonical structure of (real) Lie group,

2. the identity component $G$ of $\operatorname{Aut}(\mathcal{D})$ acts on $\mathcal{D}$ transitively,

3. the isotropy group $K$ at $0 \in \mathcal{D}$ is compact (actually a maximal compact subgroup).

**Example.** For $\mathcal{D} = \mathbb{G}_g = \{ \tau \in M(g, \mathbb{C}); \, {}^{t}\tau = \tau, \, \text{Im} \, \tau &gt; 0 \}$, (the Siegel upper half plane of degree $g$ (1.1) which is of type $III_g^*$ (Theorem 2, (1.6) 2)),

1. (cf.
   (1.2)) $G = \operatorname{Sp}(g, \mathbb{R}) / \pm 1$

where

$$
\operatorname{Sp}(g, \mathbb{R}) = \{ M \in M(2g, \mathbb{R}); \, M I^{t}M = I \quad \text{for} \quad I = \begin{pmatrix} 0 &amp; 1 \\ -1g &amp; 0 \end{pmatrix} \};
$$

11. (cf.
    (1.4)) $\operatorname{Sp}(g, \mathbb{R})$ acts on $\mathbb{G}_g$ as

$$
M \cdot \tau = (A\tau + B)(C\tau + D)^{-1} \quad \text{for} \quad M = \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} \in \operatorname{Sp}(g, \mathbb{R});
$$

115

iii) (cf.
(1.6)) $K = \mathrm{Iso}(\sqrt{-1} l_g) = \{\begin{pmatrix} A &amp; B \\ -B &amp; A \end{pmatrix} ; A^t A + B^t B = 1, A^t B = B^t A\} \sim \{U = A + \sqrt{-1} B; U^t \overline{U} = l_g\}$ (the unitary group);

iv) (cf.
(1.6)) the symmetry $s_o$ at $o = \sqrt{-1} l_g$ is

$$
s_o = \begin{pmatrix} 0 &amp; l_g \\ -l_g &amp; 0 \end{pmatrix} : \tau \rightarrow -\tau^{-1}.
$$

**Definition 5.** Let

$$
\varphi = \operatorname{Lie}(G),
$$

$$
\kappa = \operatorname{Lie}(K) = \text{the subspace of } \varphi \text{ where } s_o = \operatorname{Id},
$$

$$
\varpi = \text{the subspace of } \varpi \text{ where } s_o = -\operatorname{Id}.
$$

We have a decomposition (called *Cartan decomposition*)

$$
\varphi = \kappa \oplus \varpi
$$

and canonically

$$
\varpi \sim T_o, \text{ the tangent space to } \varnothing \text{ at } o.
$$

This isomorphism is compatible with the adjoint action of $K$.

**Example.** For $\varnothing = \mathbb{S}_g$,

$$
\varphi = \{M \in M(2g, \mathbb{R}); M I + I^t M = 0\}
$$

$$
= \{M = \begin{pmatrix} A &amp; B \\ C &amp; D \end{pmatrix} ; A + {}^t D = 0, B = {}^t B, C = {}^t C\},
$$

$$
\kappa = \{M = \begin{pmatrix} A &amp; B \\ -B &amp; A \end{pmatrix} ; {}^t A + A = 0, B = {}^t B\} \sim u(g),
$$

$$
\varpi = \{M = \begin{pmatrix} A' &amp; B' \\ B' &amp; -A' \end{pmatrix} ; {}^t A' = A', {}^t B' = B'\}.
$$

$$
\begin{array}{ccc}
\varpi &amp; \xrightarrow{\sim} &amp; T_o = \varphi_{g,\mathbb{C}} \\
\Bigl(\begin{array}{cc}A' &amp; B' \\ B' &amp; -A' \end{array}\Bigr) &amp; \longrightarrow &amp; B' + \sqrt{-1}A'.
\end{array}
$$

**Definition 6.** Set

$$
\tilde{\kappa}_c = \tilde{\kappa},
$$

116

$$
\begin{array}{l}
\boldsymbol{r}_c = \sqrt{-1} \boldsymbol{r} \quad (\in \boldsymbol{q}_{\mathbb{C}}), \\
\boldsymbol{q}_c = \boldsymbol{E}_c \circ \boldsymbol{r}_c.
\end{array}
$$

Then $\boldsymbol{q}*c$ is a compact real form of $\boldsymbol{q}*{\mathbb{C}}$.
For the corresponding Lie group $G_c$

$$
\vec{v} = G_c / K_c
$$

is a compact hermitian symmetric space, called the compact dual of $\vec{v}$.
Example.
For $\vec{v} = \vec{G}_g$

$$
\boldsymbol{q}_c = \boldsymbol{H}(g, \mathbb{C}) \circ \boldsymbol{u}(2g).
$$

**Fact 2.** For $\vec{v}$ there is a homomorphism

$$
u_0: U^1 \to G
$$

from the circle group $U^1$ into $G$ such that

a) $\operatorname{Im} u_0 \subset K$, b) $u_0(z)$ induces the multiplication by $z$ on the tangent space $T_0$ of $\vec{v}$ at $0$, c) $K$ is the centralizer of $\operatorname{Im} u_0$ in $G$, d) if moreover $G$ is simple, $\operatorname{Im} u_0$ is the center of $K$.
Example.
For $\vec{v} = \vec{G}_g$

$$
\begin{array}{l}
u_0: U^1 \to \underset{w}{\overset{u}{\rightleftharpoons}} \\
e^{\sqrt{-1} \theta} \to \left( \begin{array}{cc}
c' \frac{1}{g} &amp; s' \frac{1}{g} \\
-s' \frac{1}{g} &amp; c' \frac{1}{g}
\end{array} \right) \mod \pm 1,
\end{array}
$$

where $e^{\sqrt{-1} \theta / 2} = c' + \sqrt{-1} s'$.

**Fact 3.** We use the notation in Fact 2. For $h_0 = u_0^2: U^1 \to K \subset G$,

$$
J = \operatorname{Ad}(h_0(e^{2\pi \sqrt{-1}/8})) \mid_{\boldsymbol{r}}
$$

defines the complex structure on $T_0$ via $\boldsymbol{R} \cong T_0$ (Def.5), and

$$
s_0 = \operatorname{Ad}(h_0(\sqrt{-1}))^{(#)}.
$$

117

($\mathbb{P}$) denotes the place where change of the corresponding text in [2] is necessary.)

Example.
For $\mathcal{D} = \mathbb{G}_{\mathrm{g}}$

$$
\begin{array}{l}
h_{\mathrm{o}}: \mathcal{U}^{\mathrm{l}} \longrightarrow \mathcal{G}_{\mathrm{w}} \\
e^{\sqrt{-1}\theta} \longrightarrow \left( \begin{array}{cc}
c_{\mathrm{l}} &amp; \mathrm{s} \mathrm{l} \mathrm{g} \\
-\mathrm{s} \mathrm{l}_{g} &amp; \mathrm{c} \mathrm{l}_{g}
\end{array} \right) \quad \text{where} \quad c + s\sqrt{-1} = e^{\sqrt{-1}\theta}, \\
J = \frac{1}{\sqrt{2}} \left( \begin{array}{cc} 1 &amp; 1 \\ -1 &amp; 1 \end{array} \right): \left( \begin{array}{cc} a' &amp; b' \\ b' &amp; -a' \end{array} \right) \rightarrow \left( \begin{array}{cc} b' &amp; -a' \\ -a' &amp; -b' \end{array} \right), \\
s_{\mathrm{o}} = J^{2} = \left( \begin{array}{cc} 0 &amp; 1 \\ -1 &amp; 0 \end{array} \right).
\end{array}
$$

Definition 7. Let

$\mathcal{R}_{+} =$ the $\sqrt{-1}$-eigenspace for J (Fact 3),

$\mathcal{R}_{-} =$ the $-\sqrt{-1}$-eigenspace for J,

which are abelian subalgebras of $\mathcal{Q}*{\mathfrak{m}}$ with $\mathcal{R}*{\mathfrak{m}} = \mathcal{R}*{+} \oplus \mathcal{R}*{-}$, and $\mathbb{P}*{\pm}$ the corresponding subgroups of $\mathbb{G}*{\mathfrak{m}}$.

Theorem 2 (Borel and Harish-Chandra embeddings).

0. $\mathbb{K}*{\mathfrak{m}}$ normalizes $\mathbb{P}*{\pm}$ and $\mathbb{K}*{\mathfrak{m}}\mathbb{P}*{-}$ is a parabolic subgroup of $\mathbb{G}*{\mathfrak{m}}$ with unipotent radical $\mathbb{P}*{-}$.
   Hence $\mathbb{G}*{\mathfrak{m}} / \mathbb{K}*{\mathfrak{m}}\mathbb{P}_{-}$ is a projective algebraic variety X.

i) The natural map

$$
\mathbb{P}_{+} \times \mathbb{K}_{\mathfrak{m}} \times \mathbb{P}_{-} \rightarrow \mathbb{G}_{\mathfrak{m}}
$$

given by multiplication is injective, $\mathbb{G}$ is contained in the image and $\mathbb{K}*{\mathfrak{m}}\mathbb{P}*{-} \cap \mathbb{G} = \mathbb{K}$.

ii) The maps

$$
\begin{array}{c c c c c}
\mathcal{D} &amp; \longrightarrow &amp; \mathcal{R}_{+} &amp; \longrightarrow &amp; X \\
\stackrel{\circ}{&amp;} + &amp; \exp \stackrel{\circ}{&amp;} + &amp; &amp; \\
&amp; &amp; \stackrel{\circ}{P}_{+} &amp; &amp; \\
&amp; &amp; \stackrel{\circ}{=} \pi &amp; &amp; \\
\mathbb{G}/\mathbb{K} &amp; \rightarrow &amp; \mathbb{P}_{+} \times \mathbb{K}_{\mathfrak{m}} \times \mathbb{P}_{-}/\mathbb{K}_{\mathfrak{m}}\mathbb{P}_{-} &amp; \rightarrow &amp; \mathbb{G}_{\mathfrak{m}}/\mathbb{K}_{\mathfrak{m}}\mathbb{P}_{-}
\end{array}
$$

are holomorphic open immersions.
The image of $\mathcal{D}$ in $\mathcal{R}*{+}$ is bounded (called Harish-Chandra embedding cf.
Theorem 4), and the image of $\mathcal{R}*{+}$ in $X$ is Zariski open.

iii) The compact form $\mathbb{G}*{\mathrm{c}}$ acts on $X$ transitively and $\mathbb{G}*{\mathrm{c}} \cap \mathbb{K}*{\mathfrak{m}}\mathbb{P}*{-} = \mathbb{K}$, hence

$$
X \stackrel{\circ}{\cong} \check{\mathcal{D}} = \mathbb{G}_{\mathrm{c}} / \mathbb{K}.
$$

118

The induced open immersion $ \mathcal{D} \to \overline{\mathcal{D}} $ is called the Borel embedding.

Example.
For $ \mathcal{D} = \underline{\mathcal{G}}\_{\mathrm{g}} $

$$
\begin{aligned}
\underline{\mathcal{R}}_{\pm} &amp;= \pm \left( \begin{array}{cc} X &amp; \pm \sqrt{-1}X \\ \pm \sqrt{-1}X &amp; -X \end{array} \right) ; \quad t_X = X \right) \stackrel{\sim}{\to} \underline{\mathcal{R}}_{\mathrm{g}}, \underline{\mathfrak{T}} = \{2X\}, \\
&amp;\stackrel{\sim}{\exp} \quad P_{\pm} = \left\{ \left( \begin{array}{cc} 1 + X &amp; \pm \sqrt{-1}X \\ \pm \sqrt{-1}X &amp; 1 - X \end{array} \right) ; \quad t_X = X \right\}, \\
&amp;\stackrel{\sim}{\mathrm{G}} \longrightarrow \quad P_{+} \quad \times \quad \underset{\omega}{\mathrm{K}}_{\underline{\mathfrak{T}}} \quad \times \quad P_{-} \\
&amp;\left( \begin{array}{cc} A &amp; B \\ C &amp; D \end{array} \right) &amp;= \left( \begin{array}{cc} 1 + X &amp; \sqrt{-1}X \\ \sqrt{-1}X &amp; 1 - X \end{array} \right) \left( \begin{array}{cc} a &amp; b \\ -b &amp; a \end{array} \right) \left( \begin{array}{cc} 1 + Y &amp; -\sqrt{-1}Y \\ -\sqrt{-1}Y &amp; 1 - Y \end{array} \right)
\end{aligned}
$$

where

$$
\begin{aligned}
a + \sqrt{-1}b &amp;= \frac{B - C}{2} + \sqrt{-1} \frac{A + D}{2}, \\
2X &amp;= \{(B + C) + \sqrt{-1}(A - D)\} \{(B - C) + \sqrt{-1}(A + D)\}^{-1} \\
2Y &amp;= \left\{ -(B + C) + \sqrt{-1}(A - D) \right\} \{(B - C) + \sqrt{-1}(A + D)\}^{-1}
\end{aligned}
$$

If we let

$$
\begin{aligned}
1: &amp;\mathrm{G/K} \longrightarrow \underline{\mathcal{R}}_{+} \stackrel{\sim}{\to} \underline{\mathcal{R}}_{\mathrm{g}}, \underline{\mathfrak{T}} \\
&amp;\stackrel{\sim}{\left( \begin{array}{cc} A &amp; B \\ C &amp; D \end{array} \right) \mod K} \longrightarrow 2X, \\
j: &amp;\mathrm{G/K} \longrightarrow \underline{\mathcal{G}}_{\mathrm{g}} \\
M &amp;= \left( \begin{array}{cc} A &amp; B \\ C &amp; D \end{array} \right) \mod K \to M \cdot o = (\sqrt{-1}A + B)(\sqrt{-1}C + D)^{-1},
\end{aligned}
$$

$$
\begin{aligned}
c: &amp;\underline{\mathcal{G}}_{\mathrm{g}} \longrightarrow \mathcal{D}_{\mathrm{g}} \subset \underline{\mathcal{R}}_{\mathrm{g}}, \underline{\mathfrak{T}} \quad \text{(cf. (1.6) 2)} \\
&amp;\stackrel{\sim}{\tau} \longrightarrow (\tau - \sqrt{-1}l_{\mathrm{g}})(\tau + \sqrt{-1}l_{\mathrm{g}})^{-1},
\end{aligned}
$$

then we have

$$
i = c \circ j.
$$

119

B) The structure of roots of $G$ [§2.3, p.175ff]

**Definition 8.** Let $\mathfrak{J}$ be a Cartan subalgebra of $\mathfrak{k}$ which turns out to be that of $\mathfrak{g}$.
Let

$$
\Psi = \mathfrak{J}_{\mathfrak{C}}\text{-root system of } \mathfrak{g}_{\mathfrak{C}}
$$

so that

$$
\mathfrak{g}_{\mathfrak{C}} = \mathfrak{J}_{\mathfrak{C}} + \sum_{\varphi \in \Psi} \mathfrak{g}^{\varphi}.
$$

A root $\varphi$ is called *compact* (resp.
*non-compact*) if $\mathfrak{g}^{\varphi} \subset \mathfrak{k}*{\mathfrak{C}}$ (resp.
$\mathfrak{g}^{\varphi} \subset \mathfrak{p}*{\mathfrak{C}}$). We denote

$$
\begin{aligned}
\Psi_{K} &amp;= \text{compact roots}, \\
\Psi_{P}^{+} &amp;= \text{non-compact roots with } \mathfrak{g}^{\varphi} \subset \mathfrak{p}_{+}, \\
\Psi_{P}^{-} &amp;= \text{non-compact roots with } \mathfrak{g}^{\varphi} \subset \mathfrak{p}_{-}, \\
\Psi_{P} &amp;= \Psi_{P}^{+} \cup \Psi_{P}^{-}.
\end{aligned}
$$

We can choose a linear order on $\Psi$ such that all roots in $\Psi_{P}^{+}$ are positive and all roots in $\Psi_{P}^{-}$ negative, and we fix it.

**Example.** For $D = \mathbb{G}_{g}$

$$
\mathfrak{J} = \{h = \begin{pmatrix}
0 &amp; \lambda_{1} &amp; &amp; &amp; \\
-\lambda_{1} &amp; &amp; &amp; \lambda_{g} &amp; \\
&amp; -\lambda_{g} &amp; 0 &amp; \end{pmatrix} \},
$$

$$
\begin{aligned}
\Lambda_{i} : \mathfrak{J} &amp;\to \mathbb{R} \in \mathfrak{J}^{*} \\
\oplus &amp; \to \lambda_{i}, \\
\Psi &amp;= \{\pm \sqrt{-1}(\Lambda_{i} + \Lambda_{j}), \, 1 \leq i \leq j \leq g, \\
&amp;\pm \sqrt{-1}(\Lambda_{i} - \Lambda_{j}), \, 1 \leq i &lt; j \leq g\}, \\
\Psi_{K} &amp;= \{\pm \sqrt{-1}(\Lambda_{i} - \Lambda_{j}), \, 1 \leq i \leq j \leq g\}, \\
\Psi_{P}^{+} &amp;= \{\sqrt{-1}(\Lambda_{i} + \Lambda_{j}), \, 1 \leq i \leq j \leq g\}, \\
\Psi_{P}^{-} &amp;= \{-\sqrt{-1}(\Lambda_{i} + \Lambda_{j}), \, 1 \leq i \leq j \leq g\},
\end{aligned}
$$

120

fundamental root system ( $&lt;=&gt;$ choosing a linear order)

$$
= \{\sqrt{-1}(\Lambda_i - \Lambda_{i+1}), i = 1, \dots, g-1, 2\sqrt{-1}\Lambda_g\}.
$$

**Definition 9.** i) Two roots $\varphi, \psi$ are called *strongly orthogonal* if neither of $\varphi \pm \psi$ is a root.
In this case $\varphi$ and $\psi$ are orthogonal.

ii) Choose a maximal set of strongly orthogonal roots

$$
\gamma_1', \dots, \gamma_r'
$$

as follows (Harish-Chandra): $\gamma_1'$ is the smallest element of $\Psi_P^+$

strongly orthogonal to $\gamma_1', \dots, \gamma_{i-1}'$.

**Example.** For $D = \mathcal{G}_g$

$$
\gamma_1' = 2\sqrt{-1}\Lambda_i, \ i = 1, \dots, g.
$$

**Definition 10.** For $\varphi \in \Psi$ (Def.
8), we define

$$
h_\varphi \in \sqrt{-1} \Psi
$$

by

$$
2 \frac{&lt;\varphi, \psi&gt;}{&lt;\varphi, \varphi&gt;} = \psi(h_\varphi), \ \text{for} \quad \forall \psi \in \Psi^*
$$

where $&lt;, &gt;$ is the Killing form.

Choose

$$
e_\varphi \in \varphi^\varphi
$$

by

$$
[e_\varphi, e_{-\varphi}] = h_\varphi,
$$

$$
\overline{e}_\varphi = e_{-\varphi} \ \text{if} \ \varphi \in \Psi_P.
$$

For $\varphi \in \Psi_P^+$ let

$$
x_\varphi = e_\varphi + e_{-\varphi},
$$

$$
y_\varphi = \sqrt{-1}(e_\varphi - e_{-\varphi}).
$$

121

They form a real basis of $\pmb{\mu}$ such that $\mathrm{Jx}*{\varphi} = \mathrm{y}*{\varphi}, \mathrm{Jy}*{\varphi} = -\mathrm{x}*{\varphi}$.

We write $h_1, x_1, e_1, e_{-1}, y_1$ etc. for $h_{\gamma_1'}, x_{\gamma_1'}, e_{\gamma_1'}, e_{-\gamma_1'}, y_{\gamma_1'}$ etc.

Example.
For $\mathcal{D} = \mathcal{G}_g$,

$$
h_1 = \begin{pmatrix}
1 &amp; g+1 \\
0 &amp; -\sqrt{-1} \\
0 &amp; 0 \\
\sqrt{-1} &amp; 0
\end{pmatrix}
\begin{pmatrix}
(1) \\
(g+1)
\end{pmatrix}
$$

$$
e_1 = \begin{pmatrix}
1 &amp; g+1 \\
\frac{1}{2} &amp; \frac{\sqrt{-1}}{2} \\
\frac{\sqrt{-1}}{2} &amp; -\frac{1}{2}
\end{pmatrix}
\begin{pmatrix}
(1) \\
(g+1)
\end{pmatrix}
$$

$$
x_1 = \begin{pmatrix}
1 &amp; g+1 \\
1 &amp; \\
-1 &amp;
\end{pmatrix}
\begin{pmatrix}
(1) \\
(g+1)
\end{pmatrix}
$$

$$
y_1 = \begin{pmatrix}
1 &amp; g+1 \\
-1 &amp; (1) \\
-1 &amp; (g+1)
\end{pmatrix}
$$

**Theorem 3 (Harish-Chandra).** We use the above notation.

1. $\alpha = \sum_{i=1}^{r} \mathbb{R}x_i \subset \pmb{\mu}$ is a maximal commutative subalgebra of $\pmb{\mu}$.

$A = \operatorname{Exp}(\alpha)$ is the maximal split torus $T$ in $G$.
Moreover $KA_0 = \mathcal{D}$.

11. There is a morphism

$$
\varphi : U^1 \times \operatorname{SL}(2, \mathbb{R})^r \to G
$$

such that

122

a) $\varphi(u, h^{\mathrm{SL}}(u), \dots, h^{\mathrm{SL}}(u)) = h_0(u),$

b) $d\varphi$ on the 1-th factor $\mathcal{A}(2, \mathbb{R})$ is given by

$$
d\varphi \left( \begin{array}{cc} a &amp; b \\ c &amp; -a \end{array} \right) = a x_1 - \frac{b + c}{2} y_1 + \frac{b - c}{2} (\sqrt{-1} h_1)^{(*)}.
$$

(In [2] the false sign + is given before $\frac{b + c}{2}$.
This has caused not a few mistakes after.
Among a number of possible ways to correct we employ the above one.)

c) $\varphi$ induces a symmetric holomorphic map

$$
\tilde{\varphi}: H^r \to \mathcal{D}
$$

equivariant with respect to $\varphi$ and taking $(\sqrt{-1}, \dots, \sqrt{-1}) \in H^r$ to $0 \in \mathcal{D}$.

Example.
For $\mathcal{D} = \mathfrak{S}_g$

i)

$$
\boldsymbol{\sigma} = \left\{ \left( \begin{array}{cccc} a_1 &amp; &amp; &amp; \\ &amp; \ddots &amp; &amp; \\ &amp; &amp; a_g &amp; \\ &amp; &amp; &amp; -a_1 &amp; \\ &amp; &amp; &amp; &amp; -a_g \end{array} \right) \right\} \subset \boldsymbol{\sigma},
$$

ii) $\varphi = \varphi_1 \times \varphi_2: U^1 \times \mathrm{SL}(2, \mathbb{R})^g \to G$

$$
\begin{array}{c}
\varphi_1: U^1 \longrightarrow G, \text{ trivial} \\
\downarrow \quad \downarrow \\
u \longrightarrow 1,
\end{array}
$$

$$
\begin{array}{c}
\varphi_2: \mathrm{SL}(2, \mathbb{R})^g \longrightarrow \quad G \\
\downarrow \quad \downarrow \\
\end{array}
$$

$$
\left( \begin{array}{cc} a_1 &amp; b_1 \\ c_1 &amp; d_1 \end{array} \right)_{1=1, \dots, g} \to \left( \begin{array}{cccc} a_1 &amp; &amp; &amp; b_1 &amp; \\ &amp; &amp; a_g &amp; &amp; \\ c_1 &amp; &amp; &amp; d_1 &amp; \\ &amp; &amp; &amp; c_g &amp; \end{array} \right)
$$

123

we define for $\varphi, \psi \in \Psi$

$$
\varphi \sim \psi \iff \varphi - \psi | \sigma | \equiv 0.
$$

**Proposition 3.** i) For each $\varphi \in \Psi$ one of the following cases occurs:

I) $\varphi \sim \pm \gamma_{1}^{\prime}$, for $\exists_{1}$, in which case

$$
\sigma / \varphi \in \text{factor of type } (a_{1}), \text{ hence } \varphi = \pm \gamma_{1}^{\prime} \text{ in fact};
$$

II) $\varphi \sim \pm \frac{1}{2} (\gamma_{1}^{\prime} \pm \gamma_{j}^{\prime})$, for $\exists_{1}, \exists_{j} (1 \neq j)$, in which case

$$
\sigma / \varphi \in \text{factor of type } (b_{1j});
$$

III) $\varphi \sim \pm \frac{1}{2}\gamma_{1}^{\prime}$, for $\exists_{1}$, in which case

$$
\sigma / \varphi \in \text{factor of type } (c_{1});
$$

IV) $\varphi \sim 0$, in which case

$$
\sigma / \varphi \in \text{factor of type } (e).
$$

ii) In each irreducible factor roots are distributed as follows:

I) each $(a_{1})$ -factor is

$$
\mathbb{R}(\sqrt{-1} h_{1}) + \mathbb{R} x_{1} + \mathbb{R} y_{1}^{(*)},
$$

giving one positive non-compact root $\gamma_{1}^{\prime}$, one negative non-compact root $-\gamma_{1}^{\prime}$;

II) each $(b_{1j})$ -factor is 4-dimensional and gives one positive non-compact root $\gamma_{1}^{\prime} + \gamma_{j}^{\prime}$ , one positive and one negative compact roots $\gamma_{1}^{\prime} - \gamma_{j}^{\prime}$ , one negative non-compact root $\gamma_{1}^{\prime} + \gamma_{j}^{\prime}$ ;

III) each $(c_{1})$ -factor is 4-dimensional and gives one positive non-compact root $\gamma_{1}^{\prime}$ , one positive and one negative compact root $\gamma_{1}^{\prime}$ , one negative non-compact root $\gamma_{1}^{\prime} - \gamma_{j}^{\prime}$ .

IV) each (e)-factor is 1-dimensional and gives a compact root.

**Example.** For $\mathcal{D} = \mathcal{G}_{\mathrm{g}}$

factor of type $a_{1}$ : $\varphi = \pm 2\sqrt{-1}\Lambda_{1}$ for $1 = 1,\dots ,g$ ;

factor of type $b_{1j}$ : $\varphi = \pm \sqrt{-1} (\Lambda_1 - \Lambda_j)$ for $1\leq i &lt; j\leq g$

124

iii) $\tilde{\varphi}: H^g \longrightarrow \mathbf{G}_g$

$$
(\tau_1, \dots, \tau_g) \longrightarrow \begin{pmatrix} \tau_1^w &amp; &amp; \\ &amp; \cdot &amp; \\ &amp; &amp; \tau_g \end{pmatrix}.
$$

*Definition 11.* The number $r$ appearing in Theorem 3 is called the *rank* of $D$ or the *R-rank* of $G$.

Next we analyze the irreducible decomposition of the representation $\operatorname{Ad}(\varphi)$ of $U^1 \times \operatorname{SL}(2, \mathbb{R})^r$ in $\varphi$ and relation with the structure of roots.

*Notation.* 1) We denote the irreducible representations of $U^1$ by

$$
U_0 = \mathbb{R}, \text{ trivial},
$$

$$
U_k = \mathbb{R}^2 \quad \text{with} \quad e^{\sqrt{-1}\theta} \rightarrow \begin{pmatrix} \cos k\theta &amp; \sin k\theta \\ -\sin k\theta &amp; \cos k\theta \end{pmatrix}, \quad k = 1, 2, \dots.
$$

ii) We denote the irreducible representations of $\operatorname{SL}(2, \mathbb{R})$ by

$$
W_k = k\text{-th symmetric power of the standard representation}, \quad k = 0, 1, 2, \dots.
$$

*Proposition 2.* The irreducible representations of $U^1 \times \operatorname{SL}(2, \mathbb{R})^r$ which appear in $\varphi$ (associated with $\varphi$ in Theorem 3) are the following:

a_1) $U_0 \otimes (W_0 \otimes \cdots \otimes W_2 \otimes \cdots \otimes W_0)$ (one $W_2$),

b\_{ij}) $U_0 \otimes (W_0 \otimes \cdots \otimes W_1 \otimes \cdots \otimes W_1 \otimes \cdots \otimes W_0)$ (two $W_1$),

c_1) $U_1 \otimes (W_0 \otimes \cdots \otimes W_1 \otimes \cdots \otimes W_0)$ (one $W_1$),

e) $U_0 \otimes (W_0 \otimes \cdots \otimes W_0)$ (trivial).

Moreover the representation of type $a_1$) appears only as i-th factor of $d\varphi$ in Theorem 3 ii) b).

*Definition 12.* Letting

$$
\sigma' = \sum_{i=1}^{r} \mathbb{R}h_i \subset \sqrt{-1}\gamma,
$$

125

## Definition 13. ($\sigma'$-root decomposition)

Let

$$
\mathbb{R}^{\Psi'} = \text{the set of non-zero linear maps } \sigma' \to \mathbb{R} \quad \text{given by} \quad \varphi|_{\sigma'} \quad \text{for} \quad \varphi \in \Psi.
$$

Then we have

$$
\varphi_{\mathbb{C}} = Z(\sigma')_{\mathbb{C}} \oplus \sum_{\psi \in \mathbb{R}^{\Psi'}} \varphi^{\psi}
$$

where

$$
\begin{aligned}
Z(\sigma')_{\mathbb{C}} &amp;= \varphi_{\mathbb{C}} \oplus \sum_{\varphi \sim 0} \varphi^{\varphi} \\
\varphi^{\psi} &amp;= \sum_{\substack{\varphi \in \Psi \\ \varphi|_{\sigma'} = \psi}} \varphi^{\varphi} \text{ (eigenspace for } \psi\text{).}
\end{aligned}
$$

### Fact 4. For

$$
c = \varphi\left( \cdots \frac{1}{\sqrt{2}} \begin{pmatrix} 1 &amp; \sqrt{-1} \\ \sqrt{-1} &amp; 1 \end{pmatrix} \cdots \right)
$$

we have

$$
\operatorname{Ad}(c)(\sigma) = \sigma'.
$$

Hence for $\mathbb{R}^{\Psi} = (\operatorname{Ad}(c))^*(\mathbb{R}^{\Psi'})$ (the induced set of linear maps $\sigma \to \mathbb{R}$) we have an isomorphic *real* decomposition of $\varphi$ via $\operatorname{ad} \sigma$:

$$
\varphi = Z(\sigma) \oplus \sum_{\psi \in \mathbb{R}^{\Psi}} \varphi^{\psi}.
$$

## Proposition 4. (The structure of $\mathbb{R}^{\Psi}$)

1. Corresponding to each $(a_1)$-factor $\pm \gamma_1 = (\operatorname{Ad}(c))^*(\pm \gamma_1')$ appear.
   They are roots occurring in $d\varphi$ (Th.3).

2. If moreover $\varphi$ is simple, then either:

- Case $C_r$) $\mathbb{R}^{\Psi} = \{ \pm \frac{\gamma_1 + \gamma_j}{2}, 1 \geq j, \pm \frac{\gamma_1 - \gamma_j}{2}, 1 &gt; j \}$ all $(b_{1j})$-factor occur, but no $(c_1)$-factors; or
- Case $BC_r$) $\mathbb{R}^{\Psi} = \{ \pm \frac{\gamma_1 + \gamma_j}{2}, 1 \geq j, \pm \frac{\gamma_1 - \gamma_j}{2}, 1 &gt; j, \pm \frac{\gamma_1}{2} \}$ all $(b_{1j})$- and all $(c_1)$-factors occur.

126

iii) If $\mathcal{D}$ is simple, then the Weyl group is the group of all signed permutations $\gamma_1 \to \pm \gamma_{\sigma(1)}$, $\sigma$ a permutation of $\{1, \dots, r\}$.
If we order the real roots so that $\gamma_1 &gt; \cdots &gt; \gamma_r$, then the simple roots $\mathbb{R}^{\Delta}$ are

$$
\begin{aligned}
\alpha_1 &amp;= (\gamma_1 - \gamma_{1+1})/2, \quad 1 \leq 1 &lt; r, \\
\alpha_r &amp;= \gamma_r \quad \text{(Case C}_r\text{)} \\
&amp;= \gamma_r/2 \quad \text{(Case BC}_r\text{)}.
\end{aligned}
$$

Example.
For $\mathcal{D} = \mathbb{G}_g$ the case $\mathbb{C}_g$) occurs.
We have

$$
\alpha = \{A = \begin{pmatrix}
a_1 &amp; \cdots &amp; 0 \\
&amp; a_g &amp; \\
0 &amp; -a_1 &amp; \cdots &amp; -a_g
\end{pmatrix}
$$

and

$$
\begin{aligned}
\gamma_1 : \alpha &amp;\to \mathbb{R}, \quad 1 = 1, \dots, g. \\
\vee &amp;\vee \\
A &amp;\to 2a_1
\end{aligned}
$$

C) The description of $\mathcal{D}$ in $\mathcal{R}_+$ via the Harish-Chandra embedding [§2.4, p.187ff].

Definition 14. We use the notation in A).

i) For $X \in \mathcal{R}_+$, define the linear map

$$
\begin{aligned}
T(X) : \mathcal{R}_- &amp;\longrightarrow \mathbb{R}_\Xi \\
\vee &amp;\vee \\
Y &amp;\longrightarrow [Y, X].
\end{aligned}
$$

ii) If

$$
\tau : \mathcal{Q}_\Xi \longrightarrow \mathcal{Q}_\Xi
$$

denote the complex conjugation with respect to $\mathcal{Q}_c$, the Killing form

127

B(x, y) on $\mathfrak{A}*{\mathbb{C}}$ induces a hermitian form on $\mathfrak{A}*{\mathbb{C}}$:

$$
B_{\tau}(u, v) = -B(u, \tau(v)), \ u, v \in \mathfrak{A}_{\mathbb{C}}
$$

which is positive definite.

iii) Let

$$
T^{*}(X): \mathbb{R}_{\mathbb{C}} \longrightarrow \mathbb{R}_{-}
$$

be the adjoint of $T(X)$ with respect to $B_{\tau}$.

**Theorem 4 (Harish-Chandra, Hermann).**

Let

$$
D_{0} = D \cap \sum_{i=1}^{r} \mathbb{C}e_{i}.
$$

Then

i) $D_{0} = \{\sum_{i=1}^{r} a_{i}e_{i}; |a_{i}| &lt; 1\}$

$$
= \operatorname{Im} \tilde{\phi} \text{ (Theorem 3)};
$$

ii) $D = \{X \in \mathbb{R}*{+}; T^{*}(X)T(X) &lt; 2Id*{\mathbb{R}_{-}}\}$

$$
= Ad(K)(D_{0}).
$$

In particular for $a, b \in \mathbb{C}$ with $|a| + |b| &lt; 1$,

$$
x, y \in D \Rightarrow ax + by \in D
$$

(Hermann convexity).

**Example.** For $D = \mathbb{G}_{g}$

recall

$$
\begin{array}{c}
\mathbb{R}_{\pm} \xrightarrow{\sim} \mathfrak{A}_{g,\mathbb{C}} \\
w \qquad \qquad \qquad \qquad w \\
\frac{1}{2} \begin{pmatrix} X &amp; \pm \sqrt{-1}X \\ \pm \sqrt{-1}X &amp; -X \end{pmatrix} \longrightarrow X
\end{array}
$$

(Theorem 2).

128

i) T(X) : $\pi_{-}$ $\longrightarrow$ $\mathcal{K}_{\mathfrak{C}}$

$\frac{1}{2}\left( \begin{array}{cc} y &amp; -\sqrt{-1}y \\ -\sqrt{-1}y &amp; y \end{array} \right) \longrightarrow \frac{1}{2}\left( \begin{array}{cc} YX - XY &amp; -\sqrt{-1}(XY+YX) \\ \sqrt{-1}(XY+YK) &amp; YX-XY \end{array} \right)$

ii) $B_{\tau}$ on $\mathcal{K}_{\mathfrak{C}}$

$B_{\tau}\left(\left( \begin{array}{cc} A &amp; -\sqrt{-1}B \\ \sqrt{-1}B &amp; A \end{array} \right), \left( \begin{array}{cc} A' &amp; -\sqrt{-1}B' \\ \sqrt{-1}B' &amp; A' \end{array} \right)\right)$

= $4\mathrm{Tr}(-\mathrm{A}\overline{\mathrm{A}}' + \mathrm{B}\overline{\mathrm{B}}')$,

$B_{\tau}$ on $\pi_{-}$ ($\sim \psi_{g,\mathfrak{C}}$)

$B_{\tau}(Y, Y') = 2\mathrm{Tr}(Y\overline{Y}')$.

iii) $\mathrm{T}^{*}(X): \mathcal{K}*{\mathfrak{C}} \longrightarrow \pi*{-} \simeq \psi_{g,\mathfrak{C}}$

$\left( \begin{array}{cc} A &amp; -\sqrt{-1}B \\ \sqrt{-1}B &amp; A \end{array} \right) \longrightarrow Y = (A\overline{X} - \overline{X}A) + (B\overline{X} + \overline{X}B)$.

Hence $\mathrm{T}^{*}(X)\mathrm{T}(X)(Y) = YX\overline{X} + \overline{X}XY$.

iv) $\mathcal{D}*{g} = \{X \in \psi*{g,\mathfrak{C}} (\sim \pi_{-}) ; X\overline{X} &lt; l_{g}\}$ (cf.
(1.6) 2)).

II. Boundary components [§3](cf. §4).

A) Boundary components [§3.1, p.194ff].

Definition 1. Recall

$$
\sigma = \sum x_{i} \mathbb{R} \in \pi
$$

and

$$
\mathcal{L}(2, \mathbb{R})^r = \sum x_{i} \mathbb{R} + \sum y_{i} \mathbb{R} + \sum \sqrt{-1} h_{i} \mathbb{R} \in \mathcal{G}
$$

in I B) Theorem 3. For a subset $S \in \{1, \dots, r\}$ we define the subalgebra $\ell_{S}$ of $\mathcal{G}$:

129

$$
\begin{array}{l}
\ell_{S} = \sum_{\psi = \sum_{j \notin S} a_{j} \gamma_{j} \in \mathbb{R}^{\psi}} (\eta^{\psi} + [\eta^{\psi}, \eta^{\psi}]) \\
= \sum_{i \notin S} (a_{i}\text{-factor}) + \sum_{\substack{1 &lt; j \\ i,j \notin S}} (b_{ij}\text{-factor}) \\
+ \sum_{i \notin S} (c_{i}\text{-factor}) \\
+ \{\text{the part of e-factor spanned by } [x, y] \text{ with } x, y \in \mathfrak{E} b_{ij}\text{-factor or } \mathfrak{E} c_{i}\text{-factor}\}.
\end{array}
$$

Hence

$$
(\ell_{S})_{\mathfrak{C}} = \sum_{\substack{\varphi \in \Psi \\ \varphi \notin 0, \varphi \vee \sum_{j \notin S} a_{j} \gamma_{j}^{\prime}}} (\eta^{\varphi} + [\eta^{\varphi}, \eta^{\varphi}]).
$$

**Fact 1.** 1) We have

a) $\ell_{S} = \mathcal{K} \cap \ell_{S} \oplus \mathcal{R} \cap \ell_{S};$ b) $\mathcal{R}*{\mathfrak{C}} \cap (\ell*{S})*{\mathfrak{C}} = \mathcal{R}*{+} \cap (\ell_{S})*{\mathfrak{C}} \oplus \mathcal{R}*{-} \cap (\ell_{S})_{\mathfrak{C}}.$

We write $\mathcal{R}*{S}, \mathcal{R}*{i,S}$ for $\mathcal{R} \cap \ell_{S}, \mathcal{R}*{i} \cap (\ell*{S})_{\mathfrak{C}}$ respectively.

11. The subgroup $L_{S}$ of $G$ corresponding to $\ell_{S}$ is closed and

$$
\varrho_{S} = L_{S} / L_{S} \cap K
$$

is a bounded symmetric domain symmetrically embedded in $\varrho$.

iii) The subgroup

$$
\prod_{i \in S} SL(2, \mathbb{R})_{i}
$$

arising from the subalgebra

$$
\sum_{i \in S} (x_{i}\mathbb{R} + y_{i}\mathbb{R} + \sqrt{-1} h_{i}\mathbb{R})
$$

commutes with $L_{S}$, hence induces equivariant symmetric holomorphic maps

130

$$
\begin{array}{l}
D^{s} \times D_{S} \xrightarrow{\text{f}_{1}} D \\
\quad n \quad \quad \quad \quad \quad \quad \quad n \\
\mathbb{C}^{s} \times \mathcal{P}_{+,S} \xrightarrow{\text{f}_{2}} \mathcal{P}_{+} \\
\quad \quad \quad \quad \quad \quad \quad n \\
(\mathbb{P}^{1})^{s} \times \vec{D}_{S} \xrightarrow{\text{f}_{3}} \vec{D}
\end{array}
$$

where $s = |S|$ and $D = \{z \in \mathbb{C}; |z| &lt; 1\}$ considered as a bounded symmetric domain $\operatorname{SL}(2, \mathbb{R}) / \operatorname{SO}(2, \mathbb{R})$ (instead of $H$). Note that $f_{2}$ is linear and $f_{3}$ is algebraic.

Example.
For $\mathcal{D} = \mathbb{G}_g$ recall

$$
\sigma = \{A = \begin{pmatrix}
a_{1} &amp; \cdots &amp; a_{g} \\
&amp; &amp; &amp; \\
&amp; &amp; &amp; \cdots &amp; a_{g-1} \\
&amp; &amp; &amp; &amp; \cdots &amp; a_{g}
\end{pmatrix} \},
$$

$$
\gamma_{i} : \sigma \longrightarrow \mathbb{R}, \quad i = 1, \cdots, g,
$$

$$
\begin{array}{c}
\text{w} \\
\text{A} \\
\end{array} \longrightarrow 2a_{i},
$$

$$
\mathbb{R}^{\psi} = \pm \frac{\gamma_{i} + \gamma_{j}}{2}, \pm \frac{\gamma_{i} - \gamma_{j}}{2} \quad (\text{I. Prop. 4}),
$$

$$
\begin{array}{ccc}
\mathcal{R}_{+} &amp; \xrightarrow{\sim} &amp; \mathcal{Q}_{g}, \mathbb{C} \\
u &amp; &amp; u \\
\vec{D} &amp; \xrightarrow{\sim} &amp; \vec{D}_{g} = \{Z; Z\vec{Z} \leq l_{g}\} \\
u &amp; &amp; u \\
D &amp; \xrightarrow{\sim} &amp; D_{g} = \{Z; Z\vec{Z} &lt; l_{g}\}.
\end{array}
$$

Let $S = \{g' + 1, \cdots, g\}$, $g'' = g - g' = \#S$.

1. $$
   \ell_{S} = \left\{ \begin{pmatrix}
   a' &amp; 0 &amp; b' &amp; 0 \\
   0 &amp; 0 &amp; 0 &amp; 0 \\
   c' &amp; 0 &amp; d' &amp; 0 \\
   0 &amp; 0 &amp; 0 &amp; 0
   \end{pmatrix} \in \mathcal{Q}; \begin{pmatrix}
   a' &amp; b' \\
   c' &amp; d' \end{pmatrix} \in \mathcal{M}(g', \mathbb{R}) \right\} \supseteq \mathcal{M}(g', \mathbb{R}),
   $$

131

$$
\boldsymbol{\mathcal{P}}_{+,\mathrm{S}} = \left\{ \begin{pmatrix}
\mathrm{X'} &amp; 0 &amp; \sqrt{-1}\mathrm{X'} &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 0 \\
\sqrt{-1}\mathrm{X'} &amp; 0 &amp; -\mathrm{X'} &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 0
\end{pmatrix} ; \quad t\mathrm{X'} = \mathrm{X'} \right\} \supsetneq \boldsymbol{\mathcal{Y}}_{\mathrm{g}',\mathrm{C}} = \{2\mathrm{X'} \},
$$

$$
\boldsymbol{\mathcal{P}}_{-,\mathrm{S}} = \left\{ \begin{pmatrix}
\mathrm{Y'} &amp; 0 &amp; -\sqrt{-1}\mathrm{Y'} &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 0 \\
-\sqrt{-1}\mathrm{Y'} &amp; 0 &amp; -\mathrm{Y'} &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 0
\end{pmatrix} ; \quad t\mathrm{Y'} = \mathrm{Y'} \right\} \supsetneq \boldsymbol{\mathcal{Y}}_{\mathrm{g}',\mathrm{C}} = \{2\mathrm{Y'} \}.
$$

ii)

$$
\mathrm{L}_{\mathrm{S}} = \left\{ \begin{pmatrix}
\mathrm{A'} &amp; 0 &amp; \mathrm{B'} &amp; 0 \\
0 &amp; 1\,\mathrm{g''} &amp; 0 &amp; 0 \\
\mathrm{C'} &amp; 0 &amp; \mathrm{D'} &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 1\,\mathrm{g''}
\end{pmatrix} ; \quad
\begin{pmatrix}
\mathrm{A'} &amp; \mathrm{B'} \\
\mathrm{C'} &amp; \mathrm{D'}
\end{pmatrix} \in \mathrm{Sp}(\mathrm{g}',\mathbb{R}) \right\} \supsetneq \mathrm{Sp}(\mathrm{g}',\mathbb{R}),
$$

$$
\begin{aligned}
\boldsymbol{\mathcal{D}}_{\mathrm{S}} &amp;\supsetneq \boldsymbol{\mathcal{G}}_{\mathrm{g}'} = \{\tau' \in \mathrm{M}(\mathrm{g}',\mathbb{C}); \quad t\tau' = \tau', \text{Im } \tau' &gt; 0\} \\
&amp;\supsetneq \boldsymbol{\mathcal{D}}_{\mathrm{g}'} = \{\mathrm{W'} \in \boldsymbol{\mathcal{Y}}_{\mathrm{g}',\mathrm{C}}; \quad \mathrm{W'}\overline{\mathrm{W}}' &lt; 1\,\mathrm{g}'\} \\
&amp;\quad \left(\mathrm{W'} = (\tau' - \sqrt{-1}\mathrm{1}_{\mathrm{g}'})(\tau' + \sqrt{-1}\mathrm{1}_{\mathrm{g}'})^{-1}\right).
\end{aligned}
$$

iii) $f_2: \mathbb{C}^{\mathrm{g}''} \times \boldsymbol{\mathcal{P}}*{+,\mathrm{S}} \longrightarrow \boldsymbol{\mathcal{P}}*{+,\mathrm{S}}$

$$
\begin{aligned}
&amp;\mathbb{C}^{\mathrm{g}''} \times \boldsymbol{\mathcal{Y}}_{\mathrm{g}',\mathrm{C}} \longrightarrow \boldsymbol{\mathcal{Y}}_{\mathrm{g},\mathrm{C}} \\
&amp;\quad \left(\lambda_{\mathrm{g}'+1}, \dots, \lambda_{\mathrm{g}}\right) \times \mathrm{X'} \rightarrow \begin{pmatrix}
\mathrm{X'} &amp; 0 \\
\lambda_{\mathrm{g}'+1} &amp; \ddots \\
0 &amp; \lambda_{\mathrm{g}}
\end{pmatrix}.
\end{aligned}
$$

**Definition 2.**

$$
\begin{aligned}
F_{\mathrm{S}} &amp;= f_2((1, \dots, 1) \times \boldsymbol{\mathcal{D}}_{\mathrm{S}}) \subset \boldsymbol{\mathcal{P}}_{+}, \\
\check{\gamma}_{\mathrm{S}} &amp;= f_3((1, \dots, 1) \times \check{\boldsymbol{\mathcal{D}}}_{\mathrm{S}}) \subset \check{\boldsymbol{\mathcal{D}}}^{(\ast)}.
\end{aligned}
$$

Note that $F_{\mathrm{S}}$ lies in $\partial \boldsymbol{\mathcal{D}}$ in $\boldsymbol{\mathcal{P}}*{+}$ and is a translation of naturally embedded $\boldsymbol{\mathcal{D}}*{\mathrm{S}}$ by $f_2((1, \dots, 1) \times 0) = \sum_{1 \in \mathrm{S}} e_1$.

**Example.** For $\boldsymbol{\mathcal{D}} = \boldsymbol{\mathcal{G}}_{\mathrm{g}}$, $S = \{g'+1, \dots, g\}$,

132

$$
\begin{array}{l}
\underset{\mathrm{U}}{\mathcal{R}} \xrightarrow{\sim} \underset{\mathrm{U}}{\mathcal{V}} \\
\mathrm{F}_{\mathrm{S}} \xrightarrow{\sim} \mathrm{F}_{\mathrm{g}}' = \left\{ \left( \begin{array}{cc} \mathrm{Z}' &amp; 0 \\ 0 &amp; 1_{\mathrm{g}}'' \end{array} \right); \mathrm{Z}'\overline{\mathrm{Z}}' &lt; 1_{\mathrm{g}}' \right\} \\
\end{array}
$$

(cf.
(4.4) iv)).

**Fact 2.** i) $\overline{F}*{\mathrm{S}} = \overline{F}*{\mathrm{S}} \circ \overline{D}$.

ii) (cf.
(4.4.1)) Any holomorphic map

$$
\lambda : \mathrm{D} \longrightarrow \mathcal{R}_{+}
$$

such that

$$
\operatorname{Im} \lambda \subset \overline{D}, \quad \operatorname{Im} \lambda \circ \mathrm{F}_{\mathrm{S}} \neq \varnothing
$$

maps $\cdot\mathrm{D}$ into $\mathrm{F}_{\mathrm{S}}$.

*Definition 3 (cf.
(4.2)). A boundary component of a bounded symmetric domain* $\mathcal{D}$ is an equivalence class in $\overline{\mathcal{D}}$ under the equivalence relation generated by $x \sim y$ if there is a holomorphic map

$$
\lambda : \mathrm{D} \longrightarrow \mathcal{R}_{+}
$$

such that $\operatorname{Im} \lambda \subset \overline{D}, x, y \in \operatorname{Im} \lambda$.

The above Fact 2 ii) together with the Hermann convexity (I. Theorem 4) says that $\mathrm{F}_{\mathrm{S}}$ is a boundary component.

We consider $\mathcal{D}$ itself as a boundary component $\mathrm{F}_{\Phi}$.

*Theorem 1 (cf.
(4.4)).* i) $\overline{\mathcal{D}}$ is the disjoint union of boundary components (trivial).

ii) The boundary components of $\mathcal{D}$ are just the set of the form

$$
k \cdot \mathrm{F}_{\mathrm{S}}, \; k \in \mathrm{K}, \; \mathrm{S} \subset \{1, \dots, r\}
$$

which are hermitian symmetric domains of rank $r - |\mathrm{S}|$.

iii) If $\mathcal{D}$ is decomposed into simple factors as

$$
\mathcal{D} = \mathcal{D}_{1} \times \dots \times \mathcal{D}_{n},
$$

then the boundary components of $\mathcal{D}$ are the products of boundary

133

components of the simple factors $\mathcal{D}_1$.

iv) A boundary component of a boundary component of $\mathcal{D}$ is a boundary component of $\mathcal{D}$.

v) For every boundary component $F$ there is a holomorphic symmetric map

$$
\begin{array}{c c c}
\mathbb{F}^1 &amp; \xrightarrow{\mathrm{F}_F} &amp; \nabla \\
\upsilon &amp; &amp; \upsilon \\
H &amp; \longrightarrow &amp; \mathcal{D}
\end{array}
$$

such that $f_{\mathbb{F}}(\sqrt{-1}) = 0$, $f_{\mathbb{F}}(\infty) \in \mathbb{F}$, equivariant with respect to a homomorphism

$$
\varphi_{\mathbb{F}}: \mathbb{U}^1 \times \mathrm{SL}(2, \mathbb{R}) \longrightarrow \mathbb{G}
$$

such that $\varphi_{\mathbb{F}}(\mathrm{e}^{\sqrt{-1}\theta}, \mathrm{h}^{\mathrm{SL}}(\mathrm{e}^{\sqrt{-1}\theta})) = \mathrm{h}_{\mathrm{o}}(\mathrm{e}^{\sqrt{-1}\theta})$.

For $\mathbb{F} = \mathbb{F}*S$, $\varphi_S = \varphi*{\mathbb{F}_S}$ is given by

$$
\varphi_S(\mathrm{e}^{\sqrt{-1}\theta}, x) = \varphi(\mathrm{e}^{\sqrt{-1}\theta}, \dots, \mathrm{e}_{1 \times S}^{\sqrt{-1}\theta} \dots x, \dots)
$$

with the Harish-Chandra map $\varphi$ in I. Theorem 3.

Example.
For $\mathcal{D} = \mathbb{G}_g$, $S = \{g' + 1, \dots, g\}$ ($g'' = g - g'$),

$$
f_S = f_{\mathbb{F}_S} : \mathbb{H} \longrightarrow \mathbb{G}_g \quad \xrightarrow{\sim} \quad \mathcal{D}_g
$$

$$
\tau \rightarrow \begin{pmatrix}
\sqrt{-1}l_g' &amp; 0 \\
0 &amp; \tau l_g'
\end{pmatrix} \rightarrow \begin{pmatrix}
0 &amp; 0 \\
0 &amp; c(\tau) l_g'
\end{pmatrix}
$$

where $c(\tau) = (\tau - \sqrt{-1})(\tau + \sqrt{-1})^{-1}$,

$$
\varphi_S = \varphi_{\mathbb{F}_S} : \mathbb{U}^1 \times \mathrm{SL}(2, \mathbb{R}) \longrightarrow \underset{\omega}{\mathrm{G}}
$$

$$
(\mathrm{e}^{\sqrt{-1}\theta}, \begin{cases} a &amp; b \\ c &amp; d \end{cases}) \rightarrow \begin{pmatrix}
c(\theta) l_g' &amp; 0 &amp; s(\theta) l_g' &amp; 0 \\
0 &amp; a l_g' &amp; 0 &amp; b l_g' \\
-s(\theta) l_g' &amp; 0 &amp; c(\theta) l_g' &amp; 0 \\
0 &amp; c l_g' &amp; 0 &amp; d l_g'
\end{pmatrix}
$$

where $s(\theta) = \sin \theta$, $c(\theta) = \cos \theta$.

134

## Proposition 1.

1. If $S_1 \subset S_2$, then $\overline{F}*{S_1} \supset F*{S_2}$.

2. (cf.
   (4.14) 111)). For any flag of boundary components

$$
\overline{D} \supset \overline{F}_1 \supset \overline{F}_2 \supset \cdots \supset \overline{F}_t
$$

there are subsets

$$
S_1 \subset S_2 \subset \cdots \subset S_t \subset \{1, \cdots, r\}
$$

and an element $k \in K$ such that

$$
k \cdot F_1 = F_{S_1}, \quad 1 \leq i \leq t.
$$

B) The normalizer of a boundary component [§3.2, p.202ff].

### Definition 4.

1. For a boundary component $F$

$$
N(F) := \{g \in G; gF = F\}
$$

(the normalizer of $F$).

11. With the homomorphism $\varphi_F$ in Theorem 1 we define a one-parameter subgroup $w_F: \mathbb{G}_m \to G$ by

$$
w_F(t) = \varphi_F(t, \begin{pmatrix} t &amp; 0 \\ 0 &amp; t^{-1} \end{pmatrix}).
$$

Note that $w_F(\infty) \in F$.

111. For $w_F$ above the associated parabolic subgroup is defined to be

$$
P(w_F) := \{g \in G; \text{Lim}_{t \to 0} w_F(t) g w_F(t)^{-1}\}.
$$

### Fact 3.

Consider $F = F_S$, $S \subset \{1, \cdots, r\}$.
Then

1. Lie $P(w_S) = Z(\alpha) + \sum_{\substack{\psi \in \mathbb{R}^* \\ \langle dw_S, \psi \rangle \geq 0}} \varphi^{(*)}$

where $w_S = w_{F_S}$ (cf.
I. Fact 4).

11. $\{\psi \in \mathbb{R}^* ; \langle dw_S, \psi \rangle \geq 0\}$

135

$$
= \left\{ \begin{array}{l l} \text{all roots} &amp; \frac{\pm \gamma_1 \pm \gamma_j}{2}, \pm \frac{\gamma_1}{2}, 1, j \notin S \\ \text{and} &amp; \\ \text{all roots} &amp; \frac{\gamma_1 \pm \gamma_j}{2}, \frac{\gamma_1}{2}, 1 \in S, \text{ any } j \end{array} \right.
$$

(The change of signs here is the result of the correction in I. Theorem 3 ii) b).)

**Theorem 2.** i) For each boundary component $F \subset \overline{\mathcal{D}}$, the equivariant pair $(f, \varphi)$ (cf.
Theorem 1):

$$
f_F: H \longrightarrow \mathcal{D}
$$

$$
\varphi_F: U^1 \times \mathrm{SL}(2, \mathbb{R}) \longrightarrow G
$$

such that $f$ is symmetric, $f(\sqrt{-1}) = 0$, $f(\infty) \in F$, is unique, and if $w_F(t) = \varphi_F(1, \begin{pmatrix} t &amp; 0 \\ 0 &amp; t^{-1} \end{pmatrix})$, then

$$
N(F) = P(w_F).
$$

ii) For two boundary components $F_1, F_2$ if $N(F_1) = N(F_2)$, then $F_1 = F_2$.

iii) $N(F)$ acts on $\mathcal{D}$ transitively (by Theorem 1 ii), cf.
(4.11) iii)).

**Example.** For $\mathcal{D} = \mathbb{G}_g$, $S = \{g' + 1, \dots, g\}$,

$$
\begin{array}{r l}
w_S: \mathbb{S}_m &amp; \longrightarrow G \\
\downarrow &amp; \\
t &amp; \rightarrow \left( \begin{array}{ccc}
1 &amp; g' &amp; 0 \\
&amp; t &amp; 0 \\
0 &amp; 0 &amp; t^{-1} \\
\end{array} \right), \quad
g'' = g - g';
\end{array}
$$

$$
\begin{array}{l}
N(F_S) = P(w_S) = \left\{ \left( \begin{array}{cccc}
A' &amp; 0 &amp; B' \\
* &amp; u &amp; * \\
C' &amp; 0 &amp; D' \\
0 &amp; 0 &amp; 0 \\
\end{array} \right) \in G; \left( \begin{array}{c}
A' \quad B' \\
C' \quad D' \\
u \in \mathrm{GL}(g'', \mathbb{R})
\end{array} \right) \right\}, \\
(= P_g, \quad \text{in} \ (4.8)).
\end{array}
$$

**Corollary.** For two boundary components $F_1, F_2$ with $\overline{F}_1 \supset F_2$

136

there is a unique symmetric holomorphic map

$$
f: H^2 \longrightarrow D
$$

such that

$$
\begin{array}{l}
f(\sqrt{-1}, \sqrt{-1}) = 0, \\
f(\sqrt{-1}, \infty) \in F_1, \\
f(\infty, \infty) \in F_2, \\
\end{array}
$$

and $w_{F_1}$ and $w_{F_2}$ commute with each other.

Example.
For $D = \mathbb{G}*g$, $F_1 = F*{S_1}$ with $S_1 = \{g_1' + 1, \dots, g\}$, $i = 1, 2, g_1' &gt; g_2'$,

$$
\begin{array}{l}
f: H \times H \longrightarrow \begin{array}{c}
G_g \\
w \\
\end{array} \\
( \tau_1, \tau_2 ) \rightarrow \left( \begin{array}{cccc}
\sqrt{-1} \, g_2' &amp; &amp; &amp; \\
&amp; \tau_1 \, g_1' - g_2' &amp; &amp; 0 \\
0 &amp; &amp; \tau_2 \, g - g_1'
\end{array} \right). \\
\end{array}
$$

**Proposition 2.** If $D = D_1 \times \cdots \times D_n$ is the irreducible decomposition of $D$ and $G = G_1 \times \cdots \times G_n$, $G_i = \mathrm{Aut}(D_i)^0$, the corresponding decomposition of $G$ into simple factors, then the correspondence $F \to N(F)$ defines a bijection between the set of boundary components and the set of real parabolic subgroups $P = P_1 \times \cdots \times P_n$ of $G$ with $P_i$ either maximal real parabolic subgroup or $P_1 = G_1$.

C) The structure of $N(F)$ [§3.3 p.209ff, §4.1 p.223ff].

**Fact 4.** Recall (Fact 3) that for $F = F_S$

$$
\operatorname{Lie} N(F_S) = Z(\mathfrak{sl}) + \sum_{\substack{\psi \in \mathbb{R}^N \\ &lt;\mathrm{dw}_S, \psi &gt; \geq 0}} \mathfrak{g}^{\psi}.
$$

It decomposes into a direct sum of 3 eigenspaces with respect to

137

$w_S : \mathfrak{G}_m \to N(F_S)$ where $\text{Ad}(w_s(t))$ is a multiplication by $l, t, t^2$ respectively in the following manner:

$$
\begin{array}{l}
\text{(Lie } N(F_S))_0 = Z(\mathfrak{oc}) + \sum_{\psi = \frac{\sum \gamma_1 \pm \gamma_j}{2}} \mathfrak{g}^{\psi} + \sum_{\psi = \frac{\sum \gamma_1 - \gamma_j}{2}} \mathfrak{g}^{\psi}, \\
\text{or} = \pm \gamma_1/2, \quad i,j \notin S \\
\text{(Lie } N(F_S))_1 = \sum_{\psi = \frac{\gamma_1 \pm \gamma_j}{2}} \mathfrak{g}^{\psi(*)}: \text{denote by } \underline{v}(F_S) \\
\text{or } \gamma_1/2 \\
\text{i} \in S, \quad j \notin S \\
\text{(Lie } N(F_S))_2 = \sum_{\psi = \frac{\gamma_1 + \gamma_j}{2}} \mathfrak{g}^{\psi}: \text{denote by } \underline{u}(F_S). \\
\text{i}, j \in S
\end{array}
$$

**Definition 5.** For a boundary component $F$

$$
\begin{array}{l}
W(F) = \text{the unipotent radical of } N(F) \\
\quad = \{g \in G; \lim_{t \to 0} w_F(t) g w_F(t)^{-1} = 1\}, \\
U(F) = \text{the commutative subgroup on } N(F) \\
\quad \text{corresponding to } t^2\text{-eigenspace of} \\
\quad \text{Lie } N(F) \text{ with respect to } \text{Ad}(w_F(t)), \\
Z(w_F) = \text{the centralizer of } w_F.
\end{array}
$$

**Fact 5.** 1) Lie $Z(w_S) = (\text{Lie } N(F_S))_0$.

ii) Lie $W(F_S) = \underline{u}(F_S) + \underline{v}(F_S)$.

iii) Lie $U(F_S) = \underline{u}(F_S)$.

iv) $U(F_S)$ is contained in (actually equal to, cf.
III. Corollary to Theorem 2,) the centre of $W(F_S)$.

v) With $V(F_S) = \exp \underline{v}(F_S)$,

$$
W(F_S) = U(F_S) \times V(F_S)
$$

as a manifold.

vi) $W(F_S)/U(F_S)$ is an abelian Lie group whose Lie algebra is naturally isomorphic to $\underline{v}(F_S)$.

138

Definition 6. 1) Recall (I. Def.
13)

$$
Z(\sigma) = \sigma \circ m(\sigma)
$$

where

$$
\begin{aligned}
m(\sigma) &amp;= \{\text{type (e)-factors in the decomposition of } \varphi\} \\
&amp;= Z(\sigma) \cap \mathbb{R}.
\end{aligned}
$$

We have for $\psi \in \mathbb{R}^{\psi}$

$$
[\varphi^{\psi}, \varphi^{-\psi}] = [\varphi^{\psi}, \varphi^{-\psi}] \cap \sigma \circ [\varphi^{\psi}, \varphi^{-\psi}] \cap m(\sigma).
$$

Denote $[\varphi^{\psi}, \varphi^{-\psi}] \cap m(\sigma)$ by $[\varphi^{\psi}, \varphi^{-\psi}]_{(e)}$.

11. Define:

$$
\begin{aligned}
\varphi_h(F_S) &amp;= \ell_S \quad \text{(Def. 1)} \\
&amp;= \sum_{\psi=\frac{\pm \gamma_1 \pm \gamma_j}{2} \text{ or } \pm \gamma_1/2} (\varphi^{\psi} + [\varphi^{\psi}, \varphi^{-\psi}]_{(e)}) + \sum_{1 \notin S} x_1 \mathbb{R}, \\
&amp;\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad 1, j \notin S \\
\varphi_\ell(F_S) &amp;= \sum_{\psi=\frac{\gamma_1 - \gamma_j}{2},} (\varphi^{\psi} + [\varphi^{\psi}, \varphi^{-\psi}]_{(e)}) + \sum_{1 \in S} x_1 \mathbb{R}, \\
&amp;\quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad 1, j \in S \\
m(F_S) &amp;= [\text{type (e)-factors which do not appear in } \varphi_h \text{ or } \varphi_\ell].
\end{aligned}
$$

Then we have a decomposition

$$
\left(\operatorname{Lie} N(F_S)\right)_0 = \varphi_h(F_S) \circ \varphi_\ell(F_S) \circ m(F_S)
$$

whose summands commute with each other.

111. Let $G_h(F_S)$ (= $L_S$ in Fact 111)), $G_\ell(F_S), M(F_S)$ be the subgroup corresponding to $\varphi_h(F_S), \varphi_\ell(F_S), m(F_S)$ respectively.

Theorem 3. Let $F \in \overline{\mathcal{D}}$ be a boundary component and $w_F: \mathbb{G}_m \to G$ be as in Theorem 2. Then

139

i) N(F) is a semidirect product

$$
\mathrm{N}(F) = \mathrm{Z}(\mathrm{w}_F) \cdot \mathrm{W}(F)
$$

where $\mathrm{W}(F) = \text{the unipotent radical of } \mathrm{N}(F),$ $\mathrm{Z}(\mathrm{w}_F) = \text{the centralizer of } \mathrm{w}_F;$

ii) $\mathrm{Z}(\mathrm{w}_F)^0$ is a direct product up to finite group

$$
\mathrm{Z}(\mathrm{w}_F)^0 = \mathrm{G}_h(F) \times \mathrm{G}_k(F) \times \mathrm{M}(F)
$$

where $\mathrm{G}_h(F)$ is semisimple without compact factor and

$$
\mathrm{G}_h(F)/\text{centre} = \mathrm{Aut}(F)^0,
$$

$\mathrm{G}_k(F)$ is reductive without compact factor,

$\mathrm{M}(F)$ is compact.

Example (cf.
(4.8), (4.9)). For $\mathcal{D} = \mathbb{G}_g$, $F = F_S$ with $S = \{g' + 1, \dots, g\}$,

$$
\mathrm{W}(F) = \left\{ \begin{array}{l}
l_g, \ 0 \quad 0 \quad n \\
t_m \quad l_g' \quad t_n \quad b \\
0 \quad 0 \quad l_g, -m \\
0 \quad 0 \quad 0 \quad l_g'
\end{array} \right\}; \ t_{nm} + b = t_{mn} + t_{b},
$$

$$
\mathrm{U}(F) = \left\{ \begin{array}{l}
l \quad 0 \quad 0 \quad 0 \\
0 \quad 1 \quad 0 \quad b \\
0 \quad 0 \quad 1 \quad 0 \\
0 \quad 0 \quad 0 \quad 1
\end{array} \right\}; \ t_b = b \} \sim \mathcal{W}_g" = \{b\},
$$

$$
\mathrm{V}(F) = \left\{ \begin{array}{l}
l \quad 0 \quad 0 \quad n \\
t_m \quad 1 \quad t_n \quad (t_{mn} - t_{nm})/2 \\
0 \quad 0 \quad 1 \quad -m \\
0 \quad 0 \quad 0 \quad 1
\end{array} \right\},
$$

140

$$
Z(w_F) = \begin{cases}
\left[ \begin{array}{cccc}
A' &amp; 0 &amp; B' &amp; 0 \\
0 &amp; u &amp; 0 &amp; 0 \\
C' &amp; 0 &amp; D' &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; t_{u^{-1}} \end{array} \right] \\
; &amp; \left[ \begin{array}{cc}
A' &amp; B' \\
C' &amp; D' \\
u \in GL(g", \mathbb{R}) \end{array} \right], \\
G_h(F) = \begin{cases}
A' &amp; 0 &amp; B' &amp; 0 \\
0 &amp; 1 &amp; 0 &amp; 0 \\
C' &amp; 0 &amp; D' &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 1
\end{cases}
; \\
; &amp; \left[ \begin{array}{cccc}
A' &amp; B' \\
C' &amp; D' \\
u \in GL(g", \mathbb{R}) \end{array} \right] \\
\end{cases}
\quad \in Sp(g', \mathbb{R}),
$$

$$
G_k(F) = \begin{bmatrix}
1 &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; u &amp; 0 &amp; 0 \\
0 &amp; 0 &amp; 1 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; t_{u^{-1}}
\end{bmatrix}
\quad \text{det} \quad u &gt; 0 \quad \text{in } GL(g", \mathbb{R})^0,
$$

$$
M(F) = \{1\}.
$$

**D) The natural projection** $\pi_F: D \to F$ [§3.4, p.214ff] (cf.
(5.5)).

**Definition 7.** Recall the map

$$
\begin{aligned}
f_F: H &amp;\longrightarrow &amp; D \\
n &amp;&amp; n \\
\mathbb{P}^1 &amp; \longrightarrow &amp; D
\end{aligned}
$$

in Theorem 2. We have

$$
o = f_F(\sqrt{-1}),
$$

$$
o_F = f_F(\infty) \in F.
$$

We define moreover

$$
o_{F^0} = f_F(0) = s_o(o_F),
$$

$$
F^0 = \text{the boundary component} \ni o_{F^0}
$$

$$
= s_o(F)
$$

where $s_o$ is the symmetry at $o$.

141

## Example.

For $\mathcal{D} = \mathbb{G}_g$, $F = F_S$ with $S = \{g' + 1, \dots, g\}$, recall $f_F: H \to \mathbb{G}_g \stackrel{\sim}{\to} \mathcal{D}_g$ in Theorem 1. Then

$$
F = \left( \begin{pmatrix} Z' &amp; 0 \\ 0 &amp; 1_g'' \end{pmatrix} \in \mathcal{P}_g, \mathfrak{C}; Z' \overline{Z'} &lt; 1_g, \right) \stackrel{\sim}{\to} \mathcal{D}_g,
$$

$$
F^\circ = \left( \begin{pmatrix} Z' &amp; 0 \\ 0 &amp; -1_g'' \end{pmatrix} \in \mathcal{P}_g, \mathfrak{C}; Z' \overline{Z'} &lt; 1_g, \right) \stackrel{\sim}{\to} \mathcal{D}_g,
$$

$$
o = 0
$$

$$
o_F = \begin{pmatrix} 0 &amp; 0 \\ 0 &amp; 1_g'' \end{pmatrix} \in F,
$$

$$
o_{F^\circ} = \begin{pmatrix} 0 &amp; 0 \\ 0 &amp; -1_g'' \end{pmatrix} \in F^\circ,
$$

$$
s_o = \begin{pmatrix} 0 &amp; 1_g \\ -1_g &amp; 0 \end{pmatrix} : \overline{\mathcal{D}}_g \longrightarrow \begin{pmatrix} \overline{\mathcal{D}}_g \\ \omega \end{pmatrix} \quad \text{w} \quad z \longrightarrow -Z.
$$

## Definition 8.

1. Let

$$
\mathcal{D}(\overline{F}) = N(F)_{\mathfrak{C}} \mathcal{D} \subset \overline{\mathcal{D}} = N(F)_{\mathfrak{C}} \cdot o \quad (\text{since } N(F) \cdot o = \mathcal{D}).
$$

11. We use $w_F$ in Theorem 2. Define

$$
p_F: \mathcal{D}(\overline{F}) \longrightarrow \overline{F}^\circ \quad \text{w} \quad x \longrightarrow \lim_{t \to 0} w_F(t)(x).
$$

We have

$$
p_F(\mathcal{D}) \subset F^\circ.
$$

111. Let $s_{o_F}$ be the symmetry at $o_F$ in $F$.
     Define

$$
\pi_F = s_{o_F} \circ s_{o} \circ p_F : \mathcal{D}(\overline{F}) \longrightarrow \overline{F},
$$

which is often called the *geodesic projection* of $\mathcal{D}$ onto $F$ because of its differential-geometric property.

142

Theorem 4. We use the notation in Definition 8. Then

1. $\pi_{\mathrm{F}}(\mathcal{D}) \subset \mathrm{F}$, ii) $\pi_{\mathrm{F}}$ is equivariant for $\mathsf{N}(\mathsf{F})*{\mathfrak{C}}$ acting $\mathcal{D}(\vec{\mathsf{F}})$ and $\vec{\mathsf{F}}$ naturally, iii) $\pi*{\mathrm{F}}$ is independent of a choice of base point $\circ$.

Example.
For $\mathcal{D} = \mathbb{G}*{\mathrm{g}}$, $\mathrm{F} = \mathrm{F}*{\mathrm{S}}$ with $\mathrm{S} = \{\mathrm{g}' + 1, \dots, \mathrm{g}\}$,

$$
\begin{array}{l}
p_{\mathrm{F}}: \mathbb{G}_{\mathrm{g}} \longrightarrow \mathbb{G}_{\mathrm{g}} \\
\tau = \left( \begin{array}{cc}
\tau' &amp; \tau'' \\
t_{\tau'''} &amp; \tau''
\end{array} \right) \to \left( \begin{array}{cc}
\tau' &amp; 0 \\
0 &amp; 0
\end{array} \right)
\end{array}
$$

since

$$
w_{\mathrm{F}}(t)(\tau) = \left( \begin{array}{cc}
\tau' &amp; t\tau'' \\
t^2\tau'' &amp; t^2\tau''
\end{array} \right)
$$

$$
s_{\mathrm{O}_{\mathrm{F}}} = \left( \begin{array}{cccc}
0 &amp; 0 &amp; 1_{\mathrm{g}} &amp; 0 \\
0 &amp; 1_{\mathrm{g}} &amp; 0 &amp; 0 \\
-1_{\mathrm{g}} &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 1_{\mathrm{g}}
\end{array} \right) : \mathbb{G}_{\mathrm{g}} \longrightarrow \mathbb{G}_{\mathrm{g}}
$$

$$
\left( \begin{array}{cc}
\tau' &amp; \tau'' \\
t_{\tau'''} &amp; \tau''
\end{array} \right) \longrightarrow \left( \begin{array}{cc}
-\tau'^{-1} &amp; -\tau'^{-1}\tau'' \\
-t_{\tau'''} \tau'^{-1} &amp; \tau''
\end{array} \right),
$$

$$
\begin{array}{c}
\mathrm{F} \longrightarrow \mathrm{F} \subset \mathcal{D}_{\mathrm{g}} \\
\omega \qquad \omega
\end{array}
$$

$$
\left( \begin{array}{cc}
Z' &amp; 0 \\
0 &amp; 1_{\mathrm{g}}
\end{array} \right) \longrightarrow \left( \begin{array}{cc}
-Z' &amp; 0 \\
0 &amp; 1_{\mathrm{g}}
\end{array} \right).
$$

$$
\pi_{\mathrm{F}} : \mathcal{D}_{\mathrm{g}} \longrightarrow \mathrm{F}
$$

$$
Z = (\tau - \sqrt{-1} \mathrm{l}_{\mathrm{g}})(\tau + \sqrt{-1} \mathrm{l}_{\mathrm{g}})^{-1} \to \left( \begin{array}{cc}
(\tau' - \sqrt{-1} \mathrm{l}_{\mathrm{g}})(\tau' + \sqrt{-1} \mathrm{l}_{\mathrm{g}})^{-1} &amp; 0 \\
0 &amp; 1_{\mathrm{g}}
\end{array} \right)
$$

where

$$
\tau = \left( \begin{array}{cc}
\tau' &amp; \tau'' \\
t_{\tau'''} &amp; \tau''
\end{array} \right) \subset \mathbb{G}_{\mathrm{g}}.
$$

143

E) Rational boundary components [§2.5, p.192f, §3.5, p.219ff].

**Definition 9.** Suppose that a semisimple algebraic group $G$ is defined over $\mathbb{Q}$.
(We allow $G$ such that $G^{\circ}$/compact normal subgroup $= \operatorname{Aut}(\mathcal{D})^{\circ}$.)
Choose a maximal $\mathbb{Q}$-split torus $A_{\mathbb{Q}}$ and a maximal $\mathbb{R}$-split torus $A$ containing $A_{\mathbb{Q}}$.
Let $q = \dim A_{\mathbb{Q}} = \mathbb{Q}$-rank of $G$ and $r = \dim A = \mathbb{R}$-rank of $G$ (defined before).

**Proposition 3.** There is a maximal strongly-orthogonal system of roots $\gamma_1, \dots, \gamma_r \in \operatorname{Hom}(A, \mathbb{G}*m) \otimes \mathbb{Q}$ enjoying similar properties as in I. Prop.
3, and moreover $A*{\mathbb{Q}}$ is defined by the equations:

$$A_{\mathbb{Q}} = \text{the connected component of the subgroup defined by } \gamma_1 = 1 \text{ for } 1 \in I_0, \gamma_1 = \gamma_j \text{ for } 1, j \in I_k$$

with a suitable partition

$$\{1, \dots, r\} = I_0 \cup I_1 \cup \cdots \cup I_q.$$

**Definition 10 (cf.
(4.15)).** A boundary component $F$ of $\mathcal{D}$ is called *rational* if $N(F)$ is defined over $\mathbb{Q}$ as a subgroup of $G$.

**Proposition 4.** A boundary component $F_S$ is rational if and only if

$$S = I_{i_1} \cup I_{i_2} \cup \cdots \cup I_{i_p} \text{ for } 1 \leq i_1, \dots, i_p \leq q.$$

**Proposition 5.** 1) If $G$ is $\mathbb{Q}$-simple, the correspondence $F^{(*)} \to N(F)$ defines a bijection between the set of rational boundary components and the set of maximal $\mathbb{Q}$-parabolic subgroups in $G$.

11. If $G$ decomposes into $\mathbb{Q}$-simple factors as $G = G_1 \times \cdots \times G_n$ and let $\mathcal{D} = \mathcal{D}_1 \times \cdots \times \mathcal{D}_n$ the corresponding decomposition, then a boundary component $F = F_1 \times \cdots \times F_n$ is rational if and only if all $F_1$ are rational.

**Theorem 5.** If $F$ is a rational boundary component the five factor decomposition in Theorem 3

$$N(F) = \left[G_h(F) \times G_g(F) \times M(F)\right] \cdot V(F) \cdot U(F)$$

is defined over $\mathbb{Q}$.

144

III. Realization of $\mathcal{D}$ as a Siegel domain of the third kind (cf.
§5)[§4].

A) The self-adjoint cone $\mathrm{C}(\mathrm{F})$ in $\mathrm{U}(\mathrm{F})$ (cf.
(4.10))[§4.2, p.227ff].

Definition 1. With $\varphi_{\mathrm{F}}: \mathrm{U}^{1} \times \mathrm{SL}(2, \mathbb{R}) \to \mathrm{G}$ in II. Theorem 1 we define

$$
\Omega_{\mathrm{F}} = \varphi_{\mathrm{F}}(1, \begin{pmatrix} 1 &amp; 1 \\ 0 &amp; 1 \end{pmatrix}) \in \mathrm{U}(\mathrm{F}).
$$

Theorem 1. With the above definition and notation in II. Theorem 3,

i) $[\mathrm{G}_{\mathrm{h}}(\mathrm{F}) \times \mathrm{M}(\mathrm{F})] \cdot \mathrm{W}(\mathrm{F})$ centralizes $\mathrm{U}(\mathrm{F})$;

ii) the orbit of $\Omega_{\mathrm{F}}$ by $\mathrm{G}_{\ell}(\mathrm{F})$

$$
\mathrm{C}(\mathrm{F}) = \left\{ \mathrm{g} \Omega_{\mathrm{F}} \mathrm{g}^{-1}; \mathrm{g} \in \mathrm{G}_{\ell}(\mathrm{F}) \right\}
$$

is an open homogeneous cone in $\mathrm{U}(\mathrm{F})$ which is self-adjoint with respect to the positive quadratic form $\mathbf{B}_{\mathrm{I}}$ on $\underline{\mathbf{u}}(\mathrm{F})$ (I. Def.
14 ii)), hence on $\mathrm{U}(\mathrm{F})$ (by exp).

The centralizer of $\Omega_{\mathrm{F}}$ in $\mathbf{G}*{\ell}(\mathbf{F})$ is a maximal compact subgroup $\mathbf{G}*{\ell}(\mathbf{F}) \cap \mathbf{K}$, hence

$$
\mathrm{C}(\mathrm{F}) = \mathrm{G}_{\ell}(\mathrm{F}) / \mathrm{G}_{\ell}(\mathrm{F}) \cap \mathrm{K}.
$$

Example.
For $\mathcal{D} = \mathbb{G}*{\mathrm{g}}$, $\mathrm{F} = \mathrm{F}*{\mathrm{S}}$ with $\mathrm{S} = \{ \mathrm{g}' + 1, \dots, \mathrm{g} \}$,

$$
\Omega_{\mathrm{F}} = \begin{pmatrix} 1 \mathrm{g}' &amp; &amp; &amp; \\ &amp; 1 \mathrm{g}'' &amp; &amp; 1 \mathrm{g}'' \\ &amp; &amp; 1 \mathrm{g}'' &amp; &amp; 1 \mathrm{g}'' \end{pmatrix} \in \mathrm{U}(\mathrm{F}) \leftrightarrow 1 \mathrm{g}'' \in \mathcal{Y}_{\mathrm{g}}'',
$$

$$
\begin{aligned}
\mathrm{G}_{\ell}(\mathrm{F}) &amp;\times \quad \mathrm{U}(\mathrm{F}) \xrightarrow{\text{adjoint}} \mathrm{U}(\mathrm{F}) \\
\stackrel{\circ}{\varepsilon} &amp;\stackrel{\circ}{\varepsilon} \quad \mathrm{U}(\mathrm{F}) \quad (\text{II. Th.3})
\end{aligned}
$$

$$
\mathrm{GL}(\mathrm{g}'',\mathbb{R}) \times \mathcal{Y}_{\mathrm{g}''} \longrightarrow \mathcal{Y}_{\mathrm{g}''}
$$

$$
(\mathrm{u}, \quad \mathrm{b}) \longrightarrow \mathrm{u b}^{\mathrm{t}} \mathrm{u},
$$

145

$$
\begin{array}{l}
U(F) \xrightarrow{\sim} \Psi_{g''} \\
U \quad U \\
C(F) \xrightarrow{\sim} \Psi_{g''}^+ = \{u^t u; u \in GL(g'', \mathbb{R})\}, \\
G_{\ell}(F) \cap K \sim O(g'') = \{u; u^t u = l_{g''}\} \subset GL(g'', \mathbb{R}).
\end{array}
$$

**Theorem 2.** For $v \neq 0 \in v(F)$ (II. Fact 4)

$$
[v, J_F v] \in \overline{C(F)} - \{0\}^{(*)}
$$

where $J_F = \mathrm{Ad}(\varphi_F(\sqrt{-1}, 1_2))^{(*)}$ defines a complex structure on $v(F)$.

**Corollary.** $U(F)$ is the centre of $W(F)$.

**Example.** For $\mathcal{D} = \mathcal{G}_g$, $F = F_S$ with $S = \{g' + 1, \dots, g\}$,

$$
J_F = \begin{pmatrix}
0 &amp; 0 &amp; l_{g'} &amp; 0 \\
0 &amp; l_{g''} &amp; 0 &amp; 0 \\
-l_{g'} &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; l_{g''}
\end{pmatrix},
$$

for

$$
[m : n] = \begin{pmatrix}
0 &amp; 0 &amp; 0 &amp; n \\
t_m &amp; 0 &amp; t_n &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; -m \\
0 &amp; 0 &amp; 0 &amp; 0
\end{pmatrix},
$$

we have

$$
\mathrm{Ad}(J_F)([m : n]) = [n : -m],
$$

$$
[\mathrm{Ad}(J_F)([m : n]), [m : n]] = \begin{pmatrix}
0 &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 2^t_{mm+2}^t_{nn} \\
0 &amp; 0 &amp; 0 &amp; 0 \\
0 &amp; 0 &amp; 0 &amp; 0
\end{pmatrix}
$$

**B) Realization of $\mathcal{D}$ as a Siegel domain** [§4.3, p.233ff].

**Definition 2.** Recall (II. Theorem 2 iii), Theorem 3)

$$
\mathcal{D} = [G_h(F) \cdot G_\ell(F) \cdot M(F)] \cdot W(F) / K_h(F) \cdot K_\ell(F) \cdot M(F)
$$

where

146

$$
K_h(F) = G_h(F) \cap K
$$

$$
K_{\ell}(F) = G_{\ell}(F) \cap K
$$

are maximal compact subgroups of $G_h$ and $G_{\ell}$ respectively.
We denote the natural projections by

$$
\begin{array}{c}
\phi_F: [G_h \cdot G_{\ell} \cdot M] \cdot W/K_h \cdot K_{\ell} \cdot M \longrightarrow G_{\ell}/K_{\ell}, \\
\partial \parallel \\
D \longrightarrow C(F) \\
w \quad \quad \quad \quad \quad w \\
o \longrightarrow \Omega_F
\end{array}
$$

$$
\begin{array}{c}
\pi_F: [G_h \cdot G_{\ell} \cdot M] \cdot W/K_h \cdot K_{\ell} \cdot M \longrightarrow G_h/K_h \\
\partial \parallel \\
D \longrightarrow F \\
w \quad \quad \quad \quad \quad w \\
o \longrightarrow \circ_F
\end{array}
$$

the latter of which is the same as the map defined in II. Def.
8 by virtue of II. Th.
4 ii).

**Fact 1.** The above description of $D$ induces a decomposition of $D$ as a real analytic manifold:

$$
\begin{array}{l}
D \xrightarrow{\sim} F \times C(F) \times W(F) \\
w \quad \quad \quad \quad \quad w \\
x \longrightarrow (\pi_F(x), \phi_F(x), w(x))
\end{array}
$$

where $w(x)$ is defined as an element in $W(F)$ such that

$$
x = w(x)g_h g_{\ell} \cdot o \quad \text{(not} \quad g_h g_{\ell} w(x) \cdot o\text{)}
$$

with $\pi_F(x) = g_h \cdot \circ_F$, $g_h \in G_h$, and $\phi_F(x) = g_{\ell} \cdot \Omega_F$, $g_{\ell} \in G_{\ell}$.

**Example.** For $D = \bigotimes_g$, $F = F_S$ with $S = \{g' + 1, \dots, g\}$ write $\tau \in \bigotimes_g$ as

$$
\tau = \begin{pmatrix} \tau' &amp; \tau'' \\ t_{\tau''} &amp; \tau'' \end{pmatrix}, \quad \tau' \in \bigotimes_{g'}, \quad \tau'' \in \bigotimes_{g''}, \quad g'' = g - g'.
$$

147

Since the map

$$
\begin{array}{c}
[ G _ {h} \cdot G _ {\ell} ] \cdot W \longrightarrow \bigotimes_ {g} \\
\swarrow \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\
(g _ {h}, g _ {\ell}, w) \longrightarrow w g _ {h} g _ {\ell} \cdot o
\end{array}
$$

is expressed explicitly as

$$
\begin{array}{c}
[ G _ {h} \times G _ {\ell} ] \times W \longrightarrow \bigotimes_ {g} \\
\searrow \\
[ \mathrm {S p} (\mathrm {g} ^ {\prime}, \mathrm {I R}) \cdot \mathrm {G L} (\mathrm {g} ^ {\prime \prime}, \mathrm {I R}) ] \cdot W \longrightarrow \bigotimes_ {g} \\
\swarrow
\end{array}
$$

$$
\left(\left(\begin{array}{c c c} A ^ {\prime} &amp; B ^ {\prime} \\ C ^ {\prime} &amp; D ^ {\prime} \end{array}\right), u\right), \left( \begin{array}{c c c c} 1 &amp; 0 &amp; 0 &amp; n \\ t _ {m} &amp; 1 &amp; t _ {n} &amp; b \\ 0 &amp; 0 &amp; 1 &amp; - m \\ 0 &amp; 0 &amp; 0 &amp; 1 \end{array} \right) \rightarrow \left( \begin{array}{c c c} \tau^ {\prime} = (\sqrt {- 1} A ^ {\prime} + B ^ {\prime}) (\sqrt {- 1} C ^ {\prime} + D ^ {\prime}) ^ {- 1}, &amp; \tau^ {\prime} m + n \\ t _ {m \tau^ {\prime}} + t _ {n}, &amp; t _ {m \tau^ {\prime}} m + t _ {n m} + b + \sqrt {- 1} u t _ {u} \end{array} \right),
$$

we have

$$
\begin{array}{c c c}
\bigotimes_ {g} &amp; \sim_ {\rightarrow} &amp; F \times C (F) \times W (F) \\
\bigotimes_ {g} &amp; \sim_ {\rightarrow} &amp; \bigotimes_ {g ^ {\prime}} ^ {+} \times \bigotimes_ {g ^ {\prime \prime}} ^ {+} \times W (F) \\
\swarrow &amp; &amp; \swarrow
\end{array}
$$

$$
\tau = \left( \begin{array}{c c} \tau^ {\prime} &amp; \tau^ {\prime \prime} \\ t _ {\tau^ {\prime \prime \prime}} &amp; \tau^ {\prime \prime} \end{array} \right) \rightarrow (\pi_ {F} (\tau), \phi_ {F} (\tau), w (\tau))
$$

where

$$
\pi_ {F} (\tau) = \tau^ {\prime}
$$

$$
\phi_ {F} (\tau) = \operatorname {I m} \tau^ {\prime \prime} - t (\operatorname {I m} \tau^ {\prime \prime \prime}) (\operatorname {I m} \tau^ {\prime}) ^ {- 1} (\operatorname {I m} \tau^ {\prime \prime}),
$$

$$
w (\tau) = \left( \begin{array}{c c c c} 1 &amp; 0 &amp; 0 &amp; n \\ t _ {m} &amp; 1 &amp; t _ {n} &amp; b \\ 0 &amp; 0 &amp; 1 &amp; - m \\ 0 &amp; 0 &amp; 0 &amp; 1 \end{array} \right)
$$

$$
\begin{array}{r l}
\text{with} &amp; m = (\operatorname {I m} \tau^ {\prime}) ^ {- 1} (\operatorname {I m} \tau^ {\prime \prime}), \\
&amp; n = \operatorname {R e} \tau^ {\prime \prime} - (\operatorname {R e} \tau^ {\prime}) (\operatorname {I m} \tau^ {\prime}) ^ {- 1} (\operatorname {I m} \tau^ {\prime \prime}), \\
&amp; b = \operatorname {R e} \tau^ {\prime \prime} - t _ {m} (\operatorname {R e} \tau^ {\prime}) m - t _ {n m}.
\end{array}
$$

148

Definition 3. $\mathcal{D}(\mathrm{F}) = \mathrm{U}(\mathrm{F})*{\mathfrak{T}} \cdot \mathcal{D} = \bigcup*{\mathrm{g} \in \mathrm{U}(\mathrm{F})_{\mathfrak{T}}} \mathrm{g}\mathcal{D} \subset \overset{\vee}{\mathcal{D}}$.

Note that $\mathrm{N}(\mathrm{F})\mathrm{U}(\mathrm{F})_{\mathfrak{T}}$ acts on $\mathcal{D}(\mathrm{F})$ transitively.

**Lemma.** For $\circ_{\mathrm{F}^{\circ}}^{(*)} = \varphi_{\mathrm{F}}(1, \left( \frac{1}{0} - \sqrt{\frac{-1}{1}} \right) \circ = f_{\mathrm{F}}(0)$ (II. Def.
7)

$$
\{g \in \mathrm{N}(\mathrm{F})\mathrm{U}(\mathrm{F})_{\mathfrak{T}}; \mathrm{g} \circ_{\mathrm{F}^{\circ}} = \circ_{\mathrm{F}^{\circ}}\} = K_{\mathrm{h}}(\mathrm{F}) \times G_{\mathrm{k}}(\mathrm{F}) \times M(\mathrm{F}).
$$

**Fact 2.** The above lemma implies

$$
\begin{array}{c}
(G_{\mathrm{h}}(\mathrm{F}) / K_{\mathrm{h}}(\mathrm{F})) \times W(\mathrm{F}) \cdot U(\mathrm{F})_{\mathfrak{T}} \stackrel{\vee}{\to} D(\mathrm{F}) \\
\underset{\circ}{\omega} \quad w) \longrightarrow \quad w g o_{\mathrm{F}^{\circ}}^{(*)},
\end{array}
$$

hence

$$
\mathcal{D}(\mathrm{F}) \xrightarrow{\sim} \mathrm{F} \times V(\mathrm{F}) \times U(\mathrm{F})_{\mathfrak{T}}
$$

where the projection $\pi_{\mathrm{F}}$ to $\mathrm{F}$ is given by

$$
\begin{array}{c}
\mathrm{N}(\mathrm{F}) \cdot \mathrm{U}(\mathrm{F})_{\mathfrak{T}} / K_{\mathrm{h}} \cdot G_{\mathrm{k}} \cdot M \longrightarrow \mathrm{N}(\mathrm{F}) \cdot \mathrm{U}(\mathrm{F})_{\mathfrak{T}} / K_{\mathrm{h}} \cdot G_{\mathrm{k}} \cdot M \cdot W \cdot U_{\mathfrak{T}} \\
\stackrel{\circ}{\circ} \quad G_{\mathrm{h}} / K_{\mathrm{h}} \\
D(\mathrm{F}) \longrightarrow \stackrel{\circ}{\circ} \quad F
\end{array}
$$

which is $\mathrm{N}(\mathrm{F})$-equivariant, hence is the same as in II. Definition 8.

**Example.** For $\mathcal{D} = \mathbb{G}*{\mathrm{g}}$, $\mathrm{F} = \mathrm{F}*{\mathrm{S}}$ with $\mathrm{S} = \{g' + 1, \dots, g\}$

$$
\begin{array}{l}
\mathcal{D}(\mathrm{F}) = \mathrm{U}(\mathrm{F})_{\mathfrak{T}} \cdot \mathbb{G}_{\mathrm{g}} \subset \mathcal{Y}_{\mathrm{g}, \mathfrak{T}} \\
= \left\{ \tau = \left( \begin{array}{cc} \tau' &amp; \tau'' \\ t_{\tau''} &amp; \tau'' \end{array} \right) \in \mathcal{Y}_{\mathrm{g}, \mathfrak{T}}; \tau' \in \mathbb{G}_{\mathrm{g}}, \right\}, \\
\circ_{\mathrm{F}^{\circ}} = \left( \begin{array}{cc} \sqrt{-1} \mathrm{l}_{\mathrm{g}}, &amp; 0 \\ 0 &amp; 0 \end{array} \right) \in \mathcal{D}(\mathrm{F}),
\end{array}
$$

149

$$
\begin{array}{l}
\mathcal{D}(F) \quad \xrightarrow{\sim} \quad F \times V(F) \times U(F)_{\mathfrak{C}} \\
\parallel \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad (cf. II. Th.3) \\
\mathcal{D}(F) \quad \xrightarrow{\sim} \quad \mathbb{S}_{g'} \times V(F) \times \mathbb{V}_{g''}, \mathfrak{C} \\
\downarrow \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \\
\tau = \left( \begin{array}{cc} \tau' &amp; \tau''' \\ t_{\tau'''} &amp; \tau''' \end{array} \right) \quad \rightarrow \quad (\tau', \left( \begin{array}{cccc} 1 &amp; 0 &amp; 0 &amp; n \\ t_m &amp; 1 &amp; t_n &amp; (t_{mn} - t_{nm})/2 \\ 0 &amp; 0 &amp; 1 &amp; -m \\ 0 &amp; 0 &amp; 0 &amp; 1 \end{array} \right), b) \\
\text{with } \tau''' = \tau'm + n \\
b = \tau'' - t_{m\tau'm} - (t_{nm} - t_{mn})/2.
\end{array}
$$

**Definition 4.** Define an $N(F) \cdot U(F)_{\mathfrak{C}}$-equivariant map

$$
\begin{array}{l}
\Phi_F : \mathcal{D}(F) \xrightarrow{\quad} \quad U(F) \\
\uparrow \quad \text{taking imaginary part} \\
\partial \parallel \quad U(F)_{\mathfrak{C}} / U(F) \\
\downarrow \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad 0 \\
N(F)U(F)_{\mathfrak{C}} / K_h G_k M \quad \longrightarrow \quad N(F)U(F)_{\mathfrak{C}} / N(F)
\end{array}
$$

where $N(F)U(F)_{\mathfrak{C}}$ acts on $U(F)$ so that $N(F)$ acts by conjugation and $\sqrt{-1}U(F)$ acts by (real) translation.

**Fact 3** (cf.
(5.2) ii)). i) Two $\Phi_F$ in Def.2 and Def.4 coincide on $\mathcal{D}$

$$
\begin{array}{l}
\Phi_F : \mathcal{D}(F) \longrightarrow U(F) \\
\downarrow \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad 0 \\
\Phi_F : \mathcal{D} \longrightarrow C(F).
\end{array}
$$

ii) $\Phi_F^{-1}(C(F)) = \mathcal{D}$.

**Example** ((cf.
(5.4) ii)). For $\mathcal{D} = \mathbb{S}_g$, $F = F_S$ with $S = \{g' + 1, \dots, g\}$

$$
\begin{array}{l}
\Phi_F : \mathcal{D}(F) \longrightarrow U(F) \supseteq \mathbb{V}_{g''} \\
\downarrow \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad 0 \\
\tau = \left( \begin{array}{cc} \tau' &amp; \tau''' \\ t_{\tau'''} &amp; \tau''' \end{array} \right) \longrightarrow \text{Im } \tau'' - t(\text{Im } \tau''') (\text{Im } \tau')^{-1} (\text{Im } \tau'')
\end{array}
$$

150

Definition 5. Let

$$
\begin{array}{l}
\varrho(F)' = U(F)_{\underline{\alpha}} \backslash \varrho(F) \\
\simeq N(F)/K_h \cdot G_{\underline{k}} \cdot M \cdot U \\
\end{array}
$$

and denote the natural projection by

$$
\pi_F' : \varrho(F) \longrightarrow \varrho(F)'
$$

which induces a decomposition of $\pi_F$ as

$$
\pi_F : \varrho(F) \xrightarrow{\pi_F'} \varrho(F)' \xrightarrow{p_F} F.
$$

Note that these maps are $N(F)U(F)*{\underline{\alpha}}$-equivariant.
By virtue of Fact 2 $\pi_F'$ is a holomorphic principal fibre bundle with fibre $U(F)*{\underline{\alpha}}$ and $p_F$ is a real analytic fibre bundle with fibre $V(F)$.

Theorem 3 ((5.2) i)). i) The fibre bundle $\pi_F'$ is trivial:

$$
\varrho(F) \simeq \varrho(F)' \times U(F)_{\underline{\alpha}}.
$$

ii) The map $p_F : \varrho(F)' \to F$ is a complex vector bundle which in fact is trivial:

$$
\varrho(F)' \cong F \times \mathfrak{C}^k.
$$

Each fibre of $p_F$ hence determines a complex structure $J_z$, $z \in F$, on $V(F) \cong \underline{v}(F)$ with $J_{o_F} = J_F$ in Theorem 2. $V(F)$ acts on $\varrho(F)'$ as

$$
(z, y) \rightarrow (z, y + \lambda_v(z))
$$

for $v \in V(F)$ with the above trivialization.

iii) (i) + ii)) We have a holomorphic decomposition

$$
\begin{array}{r l}
\varrho(F) &amp; \stackrel{\circ}{=} F \times \mathfrak{C}^k \times U(F)_{\underline{\alpha}} \\
\pi_F' \downarrow &amp; \downarrow \text{projection} \\
\varrho(F)' &amp; = F \times \mathfrak{C}^k \\
p_F \downarrow &amp; \downarrow \text{projection} \\
F &amp; = F.
\end{array}
$$

151

Note that this is not the same as $\mathcal{D}(\mathrm{F}) \succcurlyeq \mathrm{F} \times \mathrm{V}(\mathrm{F}) \times \mathrm{U}(\mathrm{F})_{\mathfrak{C}}$ defined in Fact 2.

iv) With the above decomposition $\Phi_{\mathrm{F}}$ is expressed as

$$
\Phi_{\mathrm{F}}(x, y, z) = \operatorname{Im} z - h_{x}(y, y)
$$

where $h_x$ is a real bilinear quadratic form

$$
h_{x}: \mathbb{C}^{k} \times \mathbb{C}^{k} \longrightarrow \mathrm{U}(\mathrm{F})
$$

depending real-analytically on $x \in \mathrm{F}$.
Hence

$$
\begin{array}{l}
\mathcal{D} = \{(x, y, z); x \in \mathrm{F}, y \in \mathbb{C}^{k}, z \in \mathrm{U}(\mathrm{F})_{\mathfrak{C}}, \\
\operatorname{Im} z \in \mathrm{C}(\mathrm{F}) + h_{x}(y, y)\},
\end{array}
$$

roughly saying, $\mathcal{D}$ is a family of tube domains (in $\mathrm{U}(\mathrm{F})_{\mathfrak{C}}$) parametrized by $\mathcal{D}(\mathrm{F})' \succcurlyeq \mathrm{F} \times \mathbb{C}^{k}$.
Such a domain is called a *Siegel domain of the third kind* due to Pjatecki-Sapiro.

*Example (cf.
(5.4)).* For $\mathcal{D} = \mathbb{G}*{\mathrm{g}}$, $\mathrm{F} = \mathrm{F}*{\mathrm{S}}$ with $\mathrm{S} = \{ \mathrm{g}' + 1, \dots, \mathrm{g} \}$

i) + iii) $\mathcal{D}(\mathrm{F}) \succcurlyeq \mathrm{F} \times \mathbb{C}^{\mathrm{g}'\mathrm{g}''} \times \mathrm{U}(\mathrm{F})_{\mathfrak{C}}$

$\mathcal{D}(\mathrm{F}) \succcurlyeq \mathbb{G}*{\mathrm{g}}' \times \mathbb{C}^{\mathrm{g}'\mathrm{g}''} \times \mathfrak{W}*{\mathrm{g}''}, \mathfrak{C}$

$\tau = \begin{pmatrix} \tau' &amp; \tau'' \\ t_{\tau'''} &amp; \tau'' \end{pmatrix} \longrightarrow (\tau', \tau'', \tau''),$

ii) Denoting $\begin{pmatrix} 1 &amp; 0 &amp; 0 &amp; n \\ t_{m} &amp; 1 &amp; t_{n} &amp; (t_{mn} - t_{nm}) / 2 \\ 0 &amp; 0 &amp; 1 &amp; -m \\ 0 &amp; 0 &amp; 0 &amp; 1 \end{pmatrix} \in \mathrm{V}(\mathrm{F})$ by $(m, n)$

$= \exp([m, n])$ in Th.2), we see that $\mathrm{V}(\mathrm{F})$ operates on $\mathcal{D}(\mathrm{F})' = \mathbb{G}_{\mathrm{g}}, \times \mathbb{C}^{\mathrm{g}'\mathrm{g}''}$ as

$$
(m, n): (\tau', \tau'') \longrightarrow (\tau', \tau'' + \tau'm + n).
$$

The complex structure $\mathbf{J}*{\tau'}$ on $\mathrm{V}(\mathrm{F})$ in the fibre $p*{\mathrm{F}}^{-1}(\tau')$,

152

$\tau' \in \mathcal{G}_g$, is

$$
\begin{array}{l}
(V(F), J_{\tau'}) \xrightarrow{\sim} \mathfrak{C}^{g' g"} \\
\begin{array}{c}
w \\
(m, n)
\end{array}
\quad \xrightarrow{\sim} \tau'm + n,
\end{array}
$$

or

$$
J_{\tau'}: (m, n) \rightarrow \left( (Im \tau')^{-1} \left( (Re \tau') m + n \right), \right.
$$

$$
\begin{array}{l}
(-Im \tau' - (Re \tau')(Im \tau')^{-1}(Re \tau')) m \\
\quad - ((Re \tau')(Im \tau')^{-1}n).
\end{array}
$$

Note $J_{\sqrt{-1}l_g'} = J_F: (m, n) \rightarrow (n, -m)$ (Theorem 2).

iv) $\Phi_F(\tau', \tau'', \tau") = Im \tau" - {}^t (Im \tau"') (Im \tau')^{-1} (Im \tau"')$

$$
\begin{array}{l}
h_{\tau'}: \mathfrak{C}^{g' g"} \times \mathfrak{C}^{g' g"} \longrightarrow \mathfrak{F}_{g"} \\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ( \\
(\tau_1"', \tau_2"') \longrightarrow {}^t (Im \tau_1"') (Im \tau')^{-1} (Im \tau_2"').
\end{array}
$$

C) Relation of the normalizers of adjacent boundary components [§4.4, p.240ff].

Theorem 4 (cf.
(4.14)). Let $F$ and $F'$ be two boundary components with $F \subset (F')^-$.
Then

1. $U(F) \supset U(F')$

$$
\begin{array}{l}
G_{\ell}(F) \supset G_{\ell}(F'), \\
G_h(F) \subset G_h(F');
\end{array}
$$

ii) $C(F')$ is a boundary component of $C(F)$ such that $C(F')^- = C(F)^- \cap U(F')$.
Moreover if we fix $F$, the correspondence $F' \rightarrow C(F')$ is a face-order-reversing bijection between the set of boundary components $F'$ with $(F')^- \supset F$ and the set of boundary components of $C(F)$;

iii) if moreover $\mathcal{D} = G(\mathbb{R})^\circ / K$ where $G$ is defined over $\mathbb{Q}$, and $F$ is a rational boundary component, then in the above bijective correspondence $F'$ is rational if and only if $C(F')$ is a rational boundary component of $C(F)$ (i.e. $C(F')^- = C(F)^- \cap$ a subspace of $U(F)$ defined over $\mathbb{Q}$).

# Bibliography

[1] Andreotti, A.: On a theorem of Torelli, Amer.
J. Math.
80 (1958), 801-828.

[2] Ash, A., Mumford, D., Rapoport, M. and Tai, Y.: Smooth Compactification of Locally Symmetric Varieties, Math.
Sci.
Press, Brookline, 1975.

[3] Baily, W. L.: Satake's compactification of $V_n$, Amer.
J. Math., 80 (1958), 348-364.

[4] Baily, W.L. and Borel, A.: Compactification of arithmetic quotients of bounded symmetric domains, Ann.
of Math., 84 (1966), 442-528.

[5] Borel, A.: Some metric properties of arithmetic quotients of symmetric spaces and an extension theorem, J. Diff.
Geom., 6 (1972), 543-560.

[6] Cartan, H.: Quotient d'un espace analytique par un groupe d'automorphismes, Algebraic Geometry and Topology, A Symposium in Honor of S. Lefschetz, Princeton Univ. Press, 1957, 90-102.

[7] Coxeter, H. S. M.: Extreme forms, Can.
J. Math., 3 (1951), 391-441.

[8] Deligne, P. and Mumford, D.: The irreducibility of the space of curves of given genus, Publ.
math.
I.H.E.S., 36 (1969), 75-110.

[9] Dickson, T. J.: On Voronoi reduction of positive definite quadratic forms, J. Number Theory, 4 (1972), 330-341.

[10] Gauss, C. F.: Werke, Göttingen, 1870-1927.

[11] Godement, R.: Domaines fondamentaux des groupes arithmétiques, Sém.
Bourbaki, 15, 1962-63, Exp.257.

[12] Griffiths, P.H. and Schmid, W.: Recent developments in Hodge theory: a discussion of techniques and results, Discrete Subgroups of Lie Groups and Applications to Moduli, Bombay, 1973, Oxford Univ. Press, 1975, 31-127.

[13] Helgason, S.: Differential Geometry and Symmetric Spaces, Academic Press, New York, 1963.

[14] Hirzebruch, F.: Über vierdimensionale Riemannsche Flächen mehrdeutiger analytischer Funktionen von zwei komplexen Veränderlichen, Math.
Ann., 126 (1953), 1-22.

[15] Igusa, J.: A desingularization problem in the theory of Siegel modular functions, Math.
Ann., 168 (1967), 228-260.

154

[16] Igusa, J.: Theta Functions, Grundlehren, 194, Springer, Berlin-Heidelberg-New York, 1972.

[17] Kempf, G., Knudsen, F., Mumford, D. and Saint-Donat, B.: Toroidal Embeddings, I., Lect.
Notes in Math., 339, Springer, Berlin-Heidelberg-New York, 1972.

[18] Kiernan, P. and Kobayashi, S.: Comments on Satake compactification and the great Picard theorem, J. Math.
Soc.
Japan, 28 (1976), 577-580.

[19] Kobayashi, S and Ochiai, T.: Satake compactification and the great Picard theorem, J. Math.
Soc.
Japan, 23 (1971), 340-350.

[20] Korányi, A. and Wolf, J.A.: Realization of hermitian symmetric spaces as generalized half planes, Ann.
of Math., 81 (1965), 265-288.

[21] Mumford, D: Stability of projective varieties, L'Enseignement Math., 23 (1977), 39-110.

[22] Namikawa, Y.: On the canonical holomorphic map from the moduli space of stable curves to the Igusa monoidal transform, Nagoya Math.
J., 52 (1973), 197-259.

[23] Namikawa, Y.: A new compactification of the Siegel space and degeneration of abelian varieties, I, Math.
Ann., 221 (1976), 97-141; II. ibid.
201-241; III. in preparation.

[24] Oda, T.: On Torus Embeddings and Applications, Tata Lect.
Notes, 57, Springer, Berlin-Heidelberg-New York, 1978.

[25] Oort, F. and Steenbrink, J.: The local Torelli theorem for algebraic curves, to appear.

[26] Pjatečki-Shapiro, I. I.: Arithmetic groups on complex domains, Uspehi Mat.
Nauk.
SSSR, 19(6) (1964), 93-121; English translation, Russ.
Math.
Surveys, 19(6), 83-109.

[27] Satake, I.: On the compactification of the Siegel space, J. Indian Math.
Soc., 20 (1956), 259-281.

[28] Satake, I.: Realization of symmetric domains as Siegel domains of 3rd kind, Lecture Notes at Berkeley, 1972.

[29] Schmid, W.: Variation of Hodge structure: the singularities of the period mapping, Inventiones math., 22 (1973), 211-319.

[30] Siegel, C. F.: Zur Theorie der Modulfunktionen n-ten Grades, Comm.
Pure Appl.
Math., 8 (1955), 677-681; Gesammelte Abhandlungen, 3, Springer, Berlin-Heidelberg-New York, 1966, 223-227.

[31] Siegel, C. F.: Symplectic Geometry, Academic Press, New York, 1964; Gesammelte Abhandlungen, 2, Springer, Berlin-Heidelberg-New York, 1966, 274-360.

155

[32] Sumihiro, H.: Equivariant completion, I-II, J. Math.
Kyoto Univ., 14 (1974), 1-28; 15 (1975), 573-605. [33] Weil, A.: Zum Beweis des Torellischen Satzes, Nachr.
Akad.
Wiss.
Göttingen, 1957, 33-53.

# List of Notations

A = exp(σ), App.
I B) Th.3. $\sigma = \sum \mathbb{R}x_{1}$, App.
I B) Th.3. $\sigma' = \sum \mathbb{R}h_{1}$, App.
I B) Def.12. Aut(D): the group of biholomorphic automorphisms of D.

$$
\operatorname{Aut}(U_{g'}, \Omega_{g'}) = \{g \in GL(U_{g'}); g\Omega_{g'} = \Omega_{g'} \}, \operatorname{Aut}(U(F), \Omega(F)), (4.10), (8.1).
$$

B, App.
I C) Def.14.

$$
\mathbb{C}^* = \mathbb{C} - \{0\}.
$$

$$
C(F) := \Omega(F) \quad \text{in} \ (4.10), \text{App. III A} \ \text{Th.1}.
$$

$$
c-T = N_{\mathbb{R}}/N: \text{real compact torus} \ (\text{in} \ T), \ (6.2), \ (6.16).
$$

$$
D = \{z \in \mathbb{C}; |z| &lt; 1\}: \text{unit disc}.
$$

$$
D^* = D - \{0\}: \text{punctured disc}.
$$

$$
D \supseteq G/K: \text{a bounded symmetric domain (here } = G_g \text{ usually)}, \quad \text{App. I A} \ \text{Def.3}.
$$

$$
D^C = G_{\mathbb{C}}/B = G_c/K_c: \text{the compact dual of } D, \text{App. I A} \ \text{Def.6}.
$$

$$
D_g: \text{bounded realization of } G_g, \ (1.6) \ 2).
$$

$$
D(a_1, \dots, a_k): \text{the convex hull generated by } a_1, \dots, a_k, \ (9.2).
$$

$$
D(F) = U(F)_{\mathbb{C}} \cdot D \subset D^C, \ (5.1), \text{App. III B} \ \text{Def.3}.
$$

$$
D(F)' = U(F)_{\mathbb{C}} \setminus D(F), \ (5.1), \text{App. III B} \ \text{Def.5}.
$$

$$
D(F'), \text{App. II D} \ \text{Def.8}.
$$

$$
e(\cdot) = \exp(2\pi\sqrt{-1}(\cdot)).
$$

$$
e_\varphi, e_{\bar{\varphi}}, e_1, e_{-1}, \text{App. I B} \ \text{Def.10}.
$$

F: boundary component of D, (4.2).

$$
F_g': \text{typical boundary component of } G_g \text{ of degree } g', \ (4.4) \ 1v).
$$

$$
F_S, F_{\bar{S}}, \text{App. II A} \ \text{Def.2}.
$$

$$
F^\circ = s_\circ(F) \ (= F^S \ \text{in} \ (5.5)), \text{App. II D} \ \text{Def.7}.
$$

G = Aut(D)^\circ (here = Sp(g, \mathbb{R}) usually), App.
I A) Fact 1 11).

$$
\vec{Q} = G \cdot R, \ (9.15).
$$

$\vec{q} = \text{Lie}(G)$, App.
I A) Def.5. $\vec{q}_c$: the compact real form of $\vec{q}$, App.
I A) Def.6.

$$
G_h(F), \ (4.9), \ (5.5).
$$

$$
G_\xi(F), \ (4.9), \ (5.5).
$$

157

$H = \{\tau \in \mathbb{C}; \text{Im } \tau &gt; 0\}$: upper half plane.

$h_{\varphi}, h_{1}, \text{App.
I B) Def.10.}$

$\text{Im} : T \to N_{\mathbb{R}}, x_{\Sigma} \to N_{\Sigma}, (6.2), (6.16).$

$\text{Iso}(p)$: the isotropy group at $p$, (1.6) 1).

$K$ (= Iso(p)): a maximal compact subgroup of $G$.

$\bar{K} = \text{Lie}(K), \text{App.
I A) Def.5.}$

$K_{\Sigma, \sigma}$: a mixed cone, (9.12).

$\ell_{S}, \text{App.
II A) Def.1.}$

$M = \text{Hom}(T, \mathbb{C}^*)$: the group of characters of $T$, (6.1).

$M_g$: the moduli space of smooth curves of genus $g$, (9.24).

$M(n, R)$: the set of matrices of degree $n$ with coefficients in $R$.

$N = \text{Hom}(\mathbb{C}^*, T)$: the group of one-parameter subgroups of $T$, (6.1).

$N_{\Sigma} = x_{\Sigma} / c - T$, (6.16).

$N(F)$ (= $P(F)$ in (4.6)), App.
II B) Def.4 i).

$O_{\sigma}$: T-orbit in $x_{\Sigma}$ corresponding to $\sigma \in \Sigma$, (6.12).

$O(F_{\alpha})$, (7.9) 1).

$\overline{O}(F_{\alpha}) = \left(\frac{\Gamma_{\alpha}}{U_{\alpha}}\right) \backslash O(F_{\alpha})$.

$P_{\alpha} = P(F_{\alpha}), w_{\alpha} = w(F_{\alpha}), u_{\alpha} = u(F_{\alpha}), (7.1).$

$P_{g'} = P(F_{g'})$, $w_{g'} = w(F_{g'})$, $u_{g'} = u(F_{g'})$, (4.8).

$P(F)$: the parabolic subgroup associated with $F$, (4.6) i), (5.5).

$\mathcal{P}$, App.
I A) Def.5.

$\mathcal{P}_{+}$, App.
I A) Def.7.

$p: (\Gamma \backslash p)^{\gamma} \to (\Gamma \backslash p)^{\gamma}$, (2.3) iii).

$p_h: P_{\alpha} \to G_h(F_{\alpha})$, (7.1).

$p_{\ell}: P_{\alpha} \to G_{\ell}(F_{\alpha})$, (7.1).

$p_{\alpha}: (U_{\alpha} \backslash p)*{\Sigma*{\alpha}} \to (\Gamma \backslash p)^{\gamma}$, (7.9) 3).

$S_g$: the moduli space of stable curves of genus $g$, (9.27).

$\mathcal{G}_g$: the Siegel upper half plane of degree $g$, (1.1).

$\mathcal{G}_g^* = \text{Sp}(g, \mathbb{Z}) \backslash \mathcal{G}_g$.

$\text{Sp}(g, \mathbb{R})$: real symplectic group, (1.2).

$\text{Sp}(g, \mathbb{Z})$: integral symplectic group, (1.8).

158

T: algebraic torus, (6.1).

T : $\pi_+$ → $\pi_-$, App.
I C) Def.14.

T\* : $\pi_+$ → $\pi_-$, App.
I C) Def.14.

$\tau$: Cartan subalgebra of $\pi$, App.
I B) Def.8.

$U_\alpha = \Gamma \cap U_\alpha$, (7.2).

$(U_\alpha \setminus D)*{\Sigma*\alpha}$, (7.7).

$(U_\alpha \setminus D(F_\alpha))*{\Sigma*\alpha}$, (7.7).

$u(F)$: the centre of $w(F)$, (4.6) iii).

$U(g)$: the unitary group of degree $g$.

$v(F) = w(F)/u(F)$, (5.2) i).

$W_\alpha = \Gamma \cap W_\alpha$, (7.2).

$w(F)$: the unipotent radical of $P(F)$, (4.6) ii), (5.5).

$w_F(t)$, App.
II B) Def.4 ii).

$x^r = \Pi T_1^{r_1} \in M$: a character of $T$ = a monomial in $k[T]$, (6.1).

$x_\Sigma$: torus embedding associated with an r.p.p. decomposition $\Sigma$, (6.9).

$x_\sigma$: affine torus embedding associated with a c.r.p. cone $\sigma$, (6.7).

$x_\phi$, $x_1$, App.
I B) Def.10.

$Y_g = \gamma_g \cap M(g, \mathbb{Z})$: the set of integral symmetric matrices, (8.2).

$Y'*g = \{y \in \gamma_g; 2y \in Y_g, y*{11} \in \mathbb{Z}\}$: the set of halfintegral symmetric matrices, (8.2).

$\gamma_g$: the space of real symmetric matrices of degree $g$, (1.6) 4), (8.1).

$\gamma_{g,\mathbb{Z}}$: the space of complex symmetric matrices of degree $g$.

$\gamma_g^+$: the cone of positive definite matrices of degree $g$, (1.6) 4), (8.1).

$\gamma_g^+$: the cone of positive semidefinite matrices of degree $g$, (8.1).

$y_\phi, y_1$, App.
I B) Def.10.

$$
Z_g^0 = U'_g \setminus S_g, \quad (9.17).
$$

$\Gamma$: arithmetic subgroup of $G$, (1.7).

$\gamma = \Gamma \cdot X$, (9.15)

$\Gamma_\alpha = \Gamma \cap P_\alpha$, (7.2).

159

$$\overline{\Gamma}*{\alpha} = p*{\ell}(\Gamma_{\alpha}), \quad (7.2).$$

$$\Gamma_{\alpha}' = \Gamma \cap \text{Ker } p_{\ell}, \quad (7.2).$$

$$\Gamma(n): \text{ principal congruence subgroup of Stufe } n, \quad (1.8).$$

$$\Delta = \Delta(\sigma): \text{ the V-cell corresponding to D-cell } \sigma, \quad (9.2).$$

$$\lambda_{a} \in \mathbb{N}: \text{ one-parameter subgroup in } T, \quad (6.1).$$

$$\Pi_{\alpha,\beta}: (U_{\beta} \setminus p(F_{\beta}))*{\Sigma*{\beta}} \to (U_{\alpha} \setminus p(F_{\alpha}))*{\Sigma*{\alpha}}, \quad (7.9) \quad 2).$$

$$\pi_{F}: p(F) \to F, \quad (5.2) \quad i), \quad (5.3) \quad i), \quad (5.5) \quad i), \quad \text{App.
II D) Def.8, App.
III B) Def.2.}$$

$$\pi_{F,F'}: F' \to F, \quad (5.6).$$

$$\pi_{F_{\alpha}}: (U_{\alpha} \setminus p)*{\Sigma*{\alpha}} \to (\Gamma \setminus p)^\vee, \quad (7.10).$$

$$\overline{\pi}*{F*{\alpha}}: (\Gamma_{\alpha}/U_{\alpha}) \setminus (U_{\alpha} \setminus p)*{\Sigma*{\alpha}} \to (\Gamma \setminus p)^\vee.$$

$$\pi_{\alpha}': p(F_{\alpha}) \to p(F_{\alpha})', \quad (7.1).$$

$$\overline{\pi}*{\alpha}': U*{\alpha} \setminus p(F_{\alpha}) \to p(F_{\alpha})', \quad (7.5).$$

$$\Sigma = \{ \sigma_{\alpha} \}: \text{ r.p.p. decomposition, } (6.4) \quad ii).$$

$$\hat{\sigma}: \text{ dual cone of } \sigma, \quad (6.5).$$

$$\sigma^{\circ} = \sigma - \text{ proper faces: relative interior of } \sigma.$$

$$\sigma_{0}: \text{ principal cone, } (8.7), \quad (8.10).$$

$$\phi: p(F) \to u(\overline{F}), \quad (5.2) \quad ii), \quad (5.3) \quad ii), \quad (5.5) \quad ii), \quad \text{App.
III B) Def.2, Def.4.}$$

$$\phi: (U_{\alpha} \setminus p(F_{\alpha}))*{\Sigma*{\alpha}} \to (U_{\alpha})*{\Sigma*{\alpha}}, \quad (7.8).$$

$$\Psi: \text{ root system of } \Psi_{\text{II}}, \quad \text{App.
I B) Def.8.}$$

$$\Psi': \text{ root system, App.
I B) Fact 4.}$$

$$\Psi': \text{ root system, App.
I B) Def.13.}$$

$$\Omega_{F}, \quad \text{App.
III A) Def.1.}$$

$$\Omega(F): \text{ selfdual cone in } u(F), \quad (4.10).$$

$$(\Omega_{\alpha})*{\Sigma*{\alpha}}, \quad (7.8).$$

$$(\Gamma \setminus p)^{\gamma}: \text{ Satake-Baily-Borel compactification, } (2.2), \quad (5.10).$$

$$(\Theta_{\beta}^{*})^{\gamma}: \text{ Voronoi compactification, } (9.20).$$

$$(\Gamma \setminus p)^{\nu}: \text{ Mumford's toroidal compactification, } (2.3), \quad (7.4), \quad (7.10), \quad (7.14).$$

$$p^2: \text{ rational closure of } p, \quad (2.2).$$

160

$$
\Omega^{\mathrm{I}} : \text{rational closure of } \Omega = \Psi_{\mathrm{g}}^{+}, \quad (8.2).
$$

$$
\begin{array}{l}
l_{\mathrm{g}}: \text{the identity matrix of degree } \mathrm{g}. \\
F &lt; F' &lt;=&gt; F &lt; (F')^{-}, \quad (4.13).
\end{array}
$$

$$
\sigma &lt; \tau : \sigma \text{ is a face of } \tau.
$$

# Index

affine torus embedding (6.3) algebraic torus (6.1) arithmetic subgroup (1.7)

Baily-Borel compactification (2.2), (5.10) Borel embedding App.I A) Th.2 boundary component of a bounded symmetric domain (4.2), App.
II A) Def.3 of a cone $\Omega(\mathbf{F})$ 4.14), (8.1) bounded symmetric domain App.
I A) Def.3

Cartan decomposition App.
I A) Def.5 Cayley transformation (1.6) 2) Central (cone decomposition, form) (8.9) compact dual App.
I A) Def.6 convex rational polyhedral cone, c.r.p. cone (6.4) 1) cylindrical topology (5.7)

Delaunay (Delone) cell, D-cell (9.2) Delaunay decomposition (9.4) Delaunay-Voronoi cone, D-V cone (9.8)

geodesic projection App.
II D) Def.8

Harish-Chandra embedding App.
I A) Th.2 hermitian symmetric space App.
I A) Def.1

mixed cone (9.12) mixed decomposition (9.12) modular form (1.12) 11)

neat (arithmetic subgroup) (7.17) normalizer of $\mathbf{F}$ (= parabolic subgroup associated with $\mathbf{F}$ ) App.
II B) Def.4

parabolic subgroup (associated with $\mathbf{F}$ ) (4.6) 1) perfect (cone decomposition, form) (8.8) polar function (6.14)

162

principal cone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . (8.10) principal congruence subgroup . . . . . . . . . . . . . . . . . . (1.8) iii) principally polarized abelian variety . . . . . . . . . . . . . . . (9.18) projective (Γ-admissible decomposition) . . . . . . . . . . . . . (7.22) properly discontinuous . . . . . . . . . . . . . . . . . . . . . . . . . (1.9)

Q-rank of G . . . . . . . . . . . . . . . . . . . . . . . . App.
II E) Def.9

rank of D . . . . . . . . . . . . . . . . . . . . . . . . App.
I B) Def.11 rational boundary component . . . . . . . . . (4.15), App.
II E) Def.10 rational closure of a bounded symmetric domain . . . . . . . . . . . . . (2.2), (4.15) of a cone Ω = ηg⁺ . . . . . . . . . . . . . . . . . . . . . . . . . (8.2) rational partial polyhedral decomposition, r.p.p. decomposition . . . . . . . . . . . . . . . . . . . . . . (6.4) ii) regular (c.r.p. cone) . . . . . . . . . . . . . . . . . . . . . . . . (6.14) R-rank of G . . . . . . . . . . . . . . . . . . . . . . . . App.
I B) Def.11

Satake compactification . . . . . . . . . . . . . . . . . . . (2.2), (5.10) Siegel domain of the third kind . . . . . . . . (5.2), App.
III B) Th.3 Siegel upperhalf plane . . . . . . . . . . . . . . . . . . . . . . . (1.1) simple (symmetric domain) . . . . . . . . . . . . . . . . App.
I A) Def.4 stable curve . . . . . . . . . . . . . . . . . . . . . . . . . . . . (9.26) strongly orthogonal (roots) . . . . . . . . . . . . . . . . App.
I B) Def.9 symmetric space . . . . . . . . . . . . . . . . . . . . . . . . . . (1.6) 3) symmetry . . . . . . . . . . . . . . . . . . . . . (1.6) 3), App.
I A) Def.1 symplectic group . . . . . . . . . . . . . . . . . . . . . . . . . . (1.2)

toroidal compactification . . . . . . . . . . . . . (2.3), (7.4), (7.10) torus embedding . . . . . . . . . . . . . . . . . . . . . . . . . . (6.3) tube domain . . . . . . . . . . . . . . . . . . . . . . . . . . . (1.6) 4) typical neighbourhood in NΣ . . . . . . . . . . . . . . . . . . . (6.16)

Voronoi cell, V-cell . . . . . . . . . . . . . . . . . . . . . . . . . (9.2) Voronoi compactification . . . . . . . . . . . . . . . . . . . . . . (9.20) Voronoi decomposition of V . . . . . . . . . . . . . . . . . . . . . (9.4) (second) Voronoi decomposition of ηg⁺ . . . . . . . . . . . . . . (9.9)

Γ-admissible family of polyhedral decompositions . . . . . . . (7.3) Γa-admissible polyhedral decomposition . . . . . . . . . . . . (7.3)
