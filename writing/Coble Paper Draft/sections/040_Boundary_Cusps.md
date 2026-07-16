# Cusp Correspondence

## Coble Cusps

::: {.remark}
We recall the mirror move algorithm from \cite{AE22nonsympinv}.
We have Nikulin's 2-elementary diagram:

\begin{figure}[H]
\centering
\input{tikz/nikulin_table.tikz}
\caption{White nodes are $\delta=0$, black are $\delta=1$, double circled are $\delta = 1,2$.}
\label{fig:nikulin_table}
\end{figure}
:::

::: {.remark}
Having identified the 2-elementary lattice $S_\Co = (11, 11, 0)_1$, one can apply the mirror move algorithm of \cite[Thm. 5.10]{AE22nonsympinv} to determine the 0-cusps and 1-cusps of $F_\Co$.
The outcome of the algorithm is summarized by the following tree:

\begin{figure}[H]
\centering
\input{tikz/mirror-moves-coble.tikz}
\caption{Blue (resp. red) indicate lattices which are valid (resp. invalid) targets of mirror moves.}
\label{fig:unlabeledtwo}
\end{figure}

Thus $F_{\Co}$ has one 0-cusp corresponding to an isotropic vector $v$ with 
\[
v_0^{\perp T_{\Co}}/\gens{v_0} \cong (9,9,1)_1 \cong \gens{2} \oplus E_{8}(2)
.\] 
Moreover, this 0-cusp $v_0$ is incident to one 1-cusp $C_0$ corresponding to an isotropic plane $J = \gens{v_0, v_1}$ with 
\[
J^{\perp T_{\Co}}/\gens{J} \cong (7,7,1)_0 \cong A_1^{\oplus 7}
.\]
where $v_1 \in v_0^{\perp T_{\Co}}/\gens{v_0}$.
In the diagrammatic language of \cite[Fig.\, 1, Thm.\,5.10]{AE22nonsympinv}, this corresponds to a $U^2$ move and can be summarized in the following mirror move diagram as a composition of two even ordinary $U(2)$-type moves:

\begin{figure}[H]
\centering
\input{tikz/mirror-moves-coble-simplified.tikz}
\caption{}
\label{fig:unlabeledthree}
\end{figure}


Note that $v_0$ corresponds to a Type $\rm{III}$ boundary, while $C_0$ corresponds to a type $\rm{II}$ boundary. It is easily verified that the Coxeter diagram $G_{(9,9,1)_1}$ at $v_0$ has precisely one maximal parabolic subdiagram, corresponding to a finite-index root lattice of type $A_7$.
We note that by \cite[\S 5]{AE22nonsympinv}, such isotropic vectors are unique up to $\Orth(T_\Co)$, and so we can choose representatives:

- $v_0 = e'$,
- $v_1 = 2h + \alpha_1 + \alpha_2$.

Calculations verify that $v_0^2 = v_1^2 = 0$, that $v_1 \in v_0^{T_{\Co}}/\gens{v_0}$, and that $v_0v_1 = 0$, and thus $J \da \gens{v_0, v_1}$ is an admissible choice of an isotropic plane.
We further note that $\div_{T_{\Co}}(v_0) = \div_{T_{\Co}}(v_1) = 2$, which will be an important invariant for establishing a correspondence to cusps of other moduli spaces.
For an isotropic plane $J$, we denote the divisibilities of the constituent generating vectors as a tuple $(d_1, d_2)$, and in this convention we have $\div_{T_{\Co}}(v_0, v_1) = (2, 2)$. We summarize this in the following boundary cusp diagram:

% Cusp diagram F_Co
\begin{figure}[H]
\centering
\input{tikz/coble-cusp-diagram-detailed.tikz}
\caption{Cusp diagram for $F_\Co = F_{(11, 11, 1)}$ where $T_\Co = \gens{2} \oplus E_{10}(2)$.}
\label{fig:coble-cusp-diagram}
\end{figure}
:::

::: {.remark}
As further proof that this cusp diagram is correct, we can use the theory of Coxeter diagrams.
Given an isotropic vector $e\in L$ a lattice of signature $(2, n)$, the lattice $e^{\perp L}/\gens{e}$ is a hyperbolic lattice equipped with a root system $R_e$ with a Coxeter diagram $G_e$. Generally, when $e$ corresponds to a 0-cusp in a Baily-Borel compactification, the adjacent 1-cusps correspond precisely to maximal parabolic subdiagrams of $G_e$. The cusp diagram above suggests that the 0-cusp $v_0$ should have a Coxeter diagram $G_{v_0}$ with precisely one maximal parabolic subdiagram. One can run Vinberg's algorithm to determine the Coxeter diagram for $v_0$, and it is a straightforward check to determine that there is indeed a unique maximal parabolic subdiagram of the form $\tilde B_7(2)$:

\begin{figure}[H]
\centering
\input{tikz/coble-coxeter-diagram-maximal-parabolic.tikz}
\caption{The unique maximal parabolic subdiagram $\tilde B_7(2)$ of $(9,9,1)_1$, corresponding to single one-cusp $(7,7,1)_0$ in $F_\Co$.}
\label{fig:coble-cusp-9-9-1-parabolics}
\end{figure}
:::

::: {.remark}
\begin{align*}
\div_{T_{\dP}}(v_0) = 2 &&
\div_{T_{\dP}}(v_1) = 1 
.\end{align*}

The former is clear, since the image of $v_0$ in $T_{\dP}$ is $e'\in U(2)$ and $e'f' = 2$.
The latter follows from the fact that $v_1\alpha_3 = 1$.
:::

::: {.remark}
We note the divisibilities of $v_i$ under various lattice embeddings:

\begin{table}[H]
\centering
\begin{tabular}{|l|l|l|l|l|}
\hline
Coble Vector & Representative & $\mathrm{div}_{T_{\Co}}$ & $\mathrm{div}_{T_{\En}}$ & $\mathrm{div}_{T_{\dP}}$ \\ \hline
$v_0$        & $e'$   & 2                        & 2                        & 2                        \\ \hline
$v_1$        & $2h + \alpha_1 + \alpha_2$   & 2                        & 2                        & 1                        \\ \hline
\end{tabular}
\caption{Isotropic vectors in $F_{\En, 2}$ and their divisibilities.}
\label{tab:sterk-cusps-two}
\end{table}

More concisely:

\begin{table}[H]
\centering
\begin{tabular}{|l|l|l|l|}
\hline
Lattice   & Image of $v_0$ & Image of $v_1$                  & Divisibility \\ \hline
$T_{\Co}$ & $e'$           & $2h + \alpha_1 + \alpha_2$      & $(2, 2)$     \\ \hline
$T_{\En}$ & $e'$           & $2e + 2f + \alpha_1 + \alpha_2$ & $(2, 2)$     \\ \hline
$T_{\dP}$ & $e'$ & $2e + 2f + \alpha_1 + \tilde\alpha_1 + \alpha_2 + \tilde \alpha_2$ & $(2, 1)$ \\ \hline
\end{tabular}
\caption{Isotropic vectors in $F_{\En, 2}$ and their divisibilities.}
\label{tab:coble-cusp-divisibilities}
\end{table}
:::

## Enriques Cusps

::: {.remark}
We recall the cusp diagram of $F_{\En}$:

% Cusp diagram F_En
\begin{figure}[H]
\centering
\input{tikz/enriques-cusp-diagram-detailed.tikz}
\caption{Cusp diagram for $F_{\En} = F_{(10, 10, 0)}$ corresponding to $T_{\En} = U \oplus E_{10}(2)$.}
\label{fig:enriques-cusp-diagram}
\end{figure}

This can be recovered using the mirror move algorithm:

\begin{figure}[H]
\centering
\input{tikz/mirror-moves-enriques-simplified.tikz}
\caption{}
\label{fig:mirror-moves-enriques-simplified}
\end{figure}
:::

::: {.remark}
We recall the Coxeter diagrams and their maximal parabolic subdiagrams at the 0-cusps of $F_{\En}$:

\begin{figure}[H]
\centering
\caption{}
\input{tikz/enriques-cusp-coxeter-diagrams-maximal-parabolics.tikz}
\label{fig:enriques-maximal-parabolics-10-10-0}
\end{figure}
:::

## Sterk Cusps

::: {.remark}
We recall Sterk's cusp diagram for $F_{\En, 2}$:

\begin{figure}[H]
\centering
\input{tikz/sterk-cusp-diagram.tikz}
\caption{Sterk's cusp diagram}
\label{fig:sterk-cusp-diagram}
\end{figure}

We have the following divisibilities in various lattices:

\begin{table}[]
\centering
\begin{tabular}{llll}
\hline
Sterk Cusp & Vector                           & $\mathrm{div}_{T_{\En}}$ & $\mathrm{div}_{T_{\mathrm{K3} } }$ \\ \hline
1          & $e$                              & 1                      & 1                                  \\
2          & $e'$                             & 2                      & 2                                  \\
3          & $e' + f' + \overline{\alpha}_8$  & 2                      & 1                                  \\
4          & $2e' + f' + \overline{\alpha}_1$ & 2                      & 1                                  \\
5          & $2e + 2f + \overline{\alpha}_1$  & 2                      & 1                                  \\ \hline
\end{tabular}
\caption{Isotropic vectors in $F_{\En, 2}$ and their divisibilities.}
\label{tab:sterk-cusp-divisibilities}
\end{table}
:::

## K3 Cusps

::: {.remark}
We recall the cusp diagram for $F_{(2,2,0)}$:

\begin{figure}[H]
\centering
\input{tikz/220-cusp-diagram.tikz}
\caption{}
\label{fig:220-cusp-diagram}
\end{figure}
:::
