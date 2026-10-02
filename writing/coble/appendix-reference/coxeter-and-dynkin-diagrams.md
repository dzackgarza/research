# Diagrams

Conventions:

1. White vertices: $v^2 = -2$.

2. Black vertices: $v^2 = -4$.

## Classical and affine Dynkin diagrams

The table below lists the labelled classical and affine Dynkin diagrams.

{{< include ../tables/dynkin-diagrams.md >}}

### Mirror move algorithm

* * *

::: {#fig-appendix-1 .figure}
\input{tikz/fig_Coxeter_Diagram_L_Co_1.tex}

Coxeter diagrams for $T_\Co$ and $\ten$ parabolics.
:::

* * *

::: {#fig-appendix-mirror-moves-enriques .figure}
\begin{tikzpicture}
\pic {object=mirror-moves/enriques};
\end{tikzpicture}

Mirror moves for the Enriques lattices.
:::

* * *

::: {#fig-appendix-2 .figure}
\begin{tikzpicture}
\pic[mirror targets=all] {object=mirror-moves/coble};
\end{tikzpicture}

Geometric cusp correspondence (Coble).
:::

* * *

::: {#fig-coxeter-diagrams .figure}
\input{tikz/fig_Coxeter_Diagram_L_Co_1.tex}

The Coxeter diagram of $L_{\Co, 1} \definedas \generators{2} \oplus E_8(2)$.
:::
