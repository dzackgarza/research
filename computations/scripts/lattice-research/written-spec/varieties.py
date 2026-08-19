"""Exact algebraic geometry nouns for the Coble project.

This module provides general nouns for algebraic varieties, divisors, morphisms,
and their specializations to curves and surfaces relevant to the Coble moduli.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Self, final, override

if TYPE_CHECKING:
    from ore_algebra.differential_operator_1_1 import (
        UnivariateDifferentialOperatorOverUnivariateRing,
    )
    from sage.rings.polynomial.multi_polynomial import MPolynomial

from src.backends.foliation_backend import HodgeTheoreticMonodromy
from src.lattices.lattices import Lattice

_LOGGER = logging.getLogger(__name__)


# ============================================================================
# FOUNDATIONAL NOUNS: ABSTRACT INTERFACES
# ============================================================================


class Variety(ABC):
    """Base class for any algebraic variety.

    Implementation notes:
    - Each Variety should maintain an underlying Sage scheme object
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/scheme.html)
      for computations. Use self._sage_scheme to access e.g. dimension(),
      Hom spaces, point enumeration, Jacobian, etc.
    - For embedded varieties (e.g. curves in P^2, surfaces in P^3),
      maintain the embedding context: self._embedding maps to the
      ambient projective space, so we can compute adjunction, normal
      bundles, etc.
    - Concrete implementations should provide classmethods:
      - from_equations(equations: list, ambient: Variety) -> Self
      - from_ideal(ideal: Any, ambient: Variety) -> Self
    - Sage's algebraic schemes compute Jacobian, codimension(),
      defining ideals, irreducible components automatically.
    """

    # _sage_scheme: sage.schemes.generic.scheme.Scheme
    #   The underlying Sage scheme object (e.g., Scheme, AlgebraicScheme)
    # _embedding: dict  # { 'into': Variety, 'by': morphism }

    @abstractmethod
    def dimension(self) -> int:
        """Return the dimension of this variety.

        Delegates to self._sage_scheme.dimension().
        """
        ...

    @abstractmethod
    def degree(self) -> int:
        """Return the degree of this variety in its ambient projective space."""
        ...

    @abstractmethod
    def is_irreducible(self) -> bool:
        """Check if the variety is irreducible.

        Delegates to self._sage_scheme.is_irreducible().
        """
        ...

    @abstractmethod
    def is_smooth(self) -> bool:
        """Check if the variety is smooth (non-singular)."""
        ...

    @abstractmethod
    def is_reduced(self) -> bool:
        """Check if the variety is reduced."""
        ...

    @abstractmethod
    def is_normal(self) -> bool:
        """Check if the variety is normal."""
        ...

    @abstractmethod
    def is_complete(self) -> bool:
        """Check if the variety is complete (proper)."""
        ...

    @abstractmethod
    def is_projective(self) -> bool:
        """Check if the variety is projective."""
        ...

    @abstractmethod
    def is_affine(self) -> bool:
        """Check if the variety is affine."""
        ...

    @abstractmethod
    def is_quasi_projective(self) -> bool:
        """Check if the variety is quasi-projective."""
        ...

    @abstractmethod
    def singular_locus(self) -> Subvariety:
        """Return the singular locus as a subvariety."""
        ...

    @abstractmethod
    def smooth_locus(self) -> Subvariety:
        """Return the smooth locus (complement of singular locus)."""
        ...

    @abstractmethod
    def is_snc(self) -> bool:
        """Check if the variety is simple normal crossing (snc)."""
        ...

    @abstractmethod
    def is_hypersurface(self) -> bool:
        """Check if the variety is a hypersurface in its ambient space.

        See https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/hypersurface.html
        """
        ...

    @abstractmethod
    def is_complete_intersection(self) -> bool:
        """Check if the variety is a complete intersection."""
        ...

    @abstractmethod
    def is_calabi_yau(self) -> bool:
        """Check if the variety is a Calabi-Yau (trivial canonical bundle)."""
        ...

    @abstractmethod
    def is_general_type(self) -> bool:
        """Check if the variety is of general type (big canonical bundle)."""
        ...

    @abstractmethod
    def is_rational(self) -> bool:
        """Check if the variety is rational (birational to P^n)."""
        ...

    @abstractmethod
    def is_unirational(self) -> bool:
        """Check if the variety is unirational."""
        ...

    @abstractmethod
    def is_abelian_variety(self) -> bool:
        """Check if the variety is an abelian variety."""
        ...

    @abstractmethod
    def is_pencil(self) -> bool:
        """Check if this variety is a pencil (family of dimension 1 over a curve)."""
        ...

    # -------------------------------------------------------------------------
    # Numerical invariants
    # -------------------------------------------------------------------------

    @abstractmethod
    def kodaira_dimension(self) -> int:
        r"""Return the Kodaira dimension $\kappa(X)$."""
        ...

    @abstractmethod
    def hilbert_polynomial(self) -> MPolynomial:
        """Return the Hilbert polynomial."""
        ...

    @abstractmethod
    def holomorphic_euler_characteristic(self) -> int:
        r"""
        $\chi(\mathcal{O}_X)$.
        """
        ...

    @abstractmethod
    def hodge_number(self, p: int, q: int) -> int:
        """Return the Hodge number $h^{p,q}$."""
        ...

    @abstractmethod
    def base_ring(self) -> Any:
        """Return the base ring (typically ZZ, QQ, or CC)."""
        ...

    # -------------------------------------------------------------------------
    # Hodge-theoretic invariants (well-defined for proper varieties)
    # -------------------------------------------------------------------------

    @abstractmethod
    def arithmetic_genus(self) -> int:
        r"""
        Return the arithmetic genus $p_a(X) = (-1)^{\dim X}(\chi(\mathcal{O}_X) - 1)$.

        For curves: $p_a = g - \delta$ where $g$ is geometric genus and $\delta$ is
        the number of nodes.
        """
        ...

    @abstractmethod
    def geometric_genus(self) -> int:
        r"""
        Return the geometric genus $p_g = h^0(X, K_X)$.

        For surfaces: $p_g = h^{2,0}$.
        """
        ...

    @abstractmethod
    def q(self) -> int:
        """Return the irregularity $q = h^1(\\mathcal{O}_X)$."""
        ...

    def canonical_divisor(self) -> Divisor:
        """The canonical divisor K_X"""
        ...

    @abstractmethod
    def defining_ideal(self) -> Any:
        """Return the defining ideal in the ambient coordinate ring."""
        ...

    @abstractmethod
    def equations(self) -> list[Any]:
        """Return the homogeneous equations defining this variety."""
        ...

    @abstractmethod
    def is_proper(self) -> bool: ...

    @abstractmethod
    def picard_group(self) -> PicardGroup:
        r"""Return the Picard group Pic(X) as divisor classes modulo lin. equiv."""

    @abstractmethod
    def normalization(self) -> Variety:
        """Return the normalization (integral closure of the coordinate ring)."""
        ...

    @abstractmethod
    def blowup(self, center: Subvariety) -> Variety:
        """Return the blowup of this variety along the center."""
        ...

    @abstractmethod
    def resolution(self) -> VarietyMorphism:
        """Return a resolution of singularities."""
        ...


class Subvariety(Variety):
    """A closed subscheme of a variety.

    A Subvariety IS a Variety; dimension(), defining_ideal(), equations(), etc.
    are inherited. This class adds the ambient context and codimension.

    Implementation notes:
    - Each Subvariety should maintain an underlying Sage subscheme object
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/algebraic_scheme.html)
      accessible via self._sage_subscheme.
    - Sage's algebraic schemes provide: Jacobian matrix, codimension(),
      defining_ideal(), irreducible_components(), is_irreducible(), etc.
    """

    # _sage_subscheme: sage.schemes.generic.algebraic_scheme.AlgebraicScheme_subscheme

    @abstractmethod
    def ambient(self) -> Variety:
        """Return the ambient variety containing this subvariety."""
        ...

    @abstractmethod
    def codimension(self) -> int:
        """Return the codimension in the ambient variety."""
        ...


class Point(ABC):
    """A closed point on a variety.

    Implementation notes:
    - Each Point should maintain an underlying Sage scheme point
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/point.html)
      accessible via self._sage_point.
    - For projective varieties (which all our varieties are), use
      https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/projective/projective_point.html
      for multiplicities and projective coordinate methods.
    - The Sage point provides coordinate access, reduction modulo
      prime ideals, etc.
    """

    # _sage_point: sage.schemes.generic.point.SchemePoint

    @abstractmethod
    def variety(self) -> Variety:
        """Return the variety on which this point lies."""
        ...

    @abstractmethod
    def coordinates(self) -> tuple:
        r"""
        Return coordinates of this point as (vector, chart).
        """
        ...

    @abstractmethod
    def coordinate_ring(self) -> Any:
        """Return the coordinate ring of the point (local ring)."""
        ...


class Divisor(ABC):
    """A Weil/Cartier divisor = integer linear combination of prime divisors.

    Implementation notes:
    - Concrete implementations should maintain an underlying Sage divisor
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/divisor.html)
      accessible via self._sage_divisor.
    - Sage divisors provide: is_effective(), intersection(),
      linear_equivalence(), coefficients(), etc.
    """

    # _sage_divisor: sage.schemes.generic.divisor.Divisor

    @abstractmethod
    def is_cartier_divisor(self) -> bool: ...

    @abstractmethod
    def is_Q_cartier_divisor(self) -> bool: ...

    @abstractmethod
    def is_weyl_divisor(self) -> bool: ...

    @abstractmethod
    def is_prime(self) -> bool:
        """Check if this divisor is prime (irreducible codimension 1 subvariety)."""
        ...

    @abstractmethod
    def coefficients(self) -> dict[Divisor, int]:
        """Return the dictionary of prime divisors and their coefficients."""
        ...

    @abstractmethod
    def is_principal(self) -> bool:
        """Check if linearly equivalent to 0."""
        ...

    @abstractmethod
    def is_effective(self) -> bool:
        r"""Check if $D \geq 0$ (effective divisor)."""
        ...

    @abstractmethod
    def is_ample(self) -> bool:
        """Check if the divisor is ample."""
        ...

    @abstractmethod
    def is_big(self) -> bool: ...

    @abstractmethod
    def is_very_ample(self) -> bool: ...

    @abstractmethod
    def is_polarization(self) -> bool: ...

    @abstractmethod
    def is_nef(self) -> bool:
        """Check if numerically effective (nef)."""
        ...

    @abstractmethod
    def degree(self) -> int: ...

    @abstractmethod
    def intersection(self, other: Divisor) -> int:
        r"""Return the intersection number $D \cdot E$."""
        ...

    @abstractmethod
    def h(self, n: int) -> int:
        r"""
        h^n(O_X(D)) := dim_k H^n(X, O_X(D))
        """

    @final
    def riemann_roch_space_dimension(self) -> int:
        return self.h(0)

    @final
    def index_of_speciality(self) -> int:
        r"""Return the index of speciality $\ell(K_X - D)$."""
        return (self.variety().canonical_divisor() - self).h(0)

    @abstractmethod
    def is_numerically_effective(self) -> bool:
        """Alias for is_nef: numerically effective."""
        ...

    # -------------------------------------------------------------------------
    # Divisor operations
    # -------------------------------------------------------------------------

    @classmethod
    @abstractmethod
    def from_meromorphic_function(cls, f: MPolynomial, domain: Variety) -> Self:
        """Construct the divisor of a meromorphic function $f$."""
        ...

    @abstractmethod
    def is_linearly_equivalent_to(self, other: Divisor) -> bool:
        """Check if this divisor is linearly equivalent to another."""
        ...

    @abstractmethod
    def is_canonical_divisor(self) -> bool:
        """Check if this divisor is a canonical divisor $K_X$."""
        ...

    @abstractmethod
    def ord_D(self, f: MPolynomial) -> int:
        r"""Return the order of vanishing of $f$ along $D$, i.e. $\mathrm{ord}_D(f)$.

        This is the length of $\mathcal{O}_{X,D}/(f)$.
        """
        ...

    @abstractmethod
    def to_coherent_sheaf(self) -> CoherentSheaf:
        r"""Return the associated rank-1 coherent sheaf $\mathcal{O}_X(D)$."""
        ...

    @abstractmethod
    def pullback(self, f: VarietyMorphism) -> Divisor:
        """Return the pullback $f^*(D)$."""
        ...

    @abstractmethod
    def pushforward(self, f: VarietyMorphism) -> Divisor:
        """Return the pushforward $f_*(D)$."""
        ...


class PicardGroup(ABC):
    r"""Divisor classes: Pic(X) ≅ Z^r ⊕ Tors.

    This extends Sage's AbelianGroup (see sage.groups.abelian_gp) and adds
    the intersection form specific to algebraic geometry.

    Implementation notes:
    - Inherits rank(), torsion(), generators() from SageAbelianGroup.
    - Concrete implementations should set self._sage_abelian_group to the
    underlying Sage AbelianGroup and delegate methods as needed.
    """

    @abstractmethod
    def variety(self) -> Variety:
        """Return the variety whose Picard group this is."""
        ...

    @abstractmethod
    def as_lattice(self) -> Lattice:
        """Return the abstract lattice defined by the intersection form."""
        ...


class LinearSystem(ABC):
    r"""Complete linear system $|D| = \mathbb{P}H^0(X, \mathcal{O}(D))$."""

    @abstractmethod
    def defining_divisor(self) -> Divisor:
        """Return the divisor $D$ such that this is $|D|$."""
        ...

    @abstractmethod
    def dimension(self) -> int:
        r"""Return $\dim |D| = h^0(\mathcal{O}(D)) - 1$."""
        ...

    @abstractmethod
    def base_locus(self) -> Subvariety:
        """Return the base locus (fixed component)."""
        ...


class VarietyMorphism(ABC):
    """A morphism of varieties $f: X \to Y$.

    Implementation notes:
    - Concrete implementations should maintain an underlying Sage morphism
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/morphism.html)
      accessible via self._sage_morphism.
    - Sage morphisms provide: degree(), is_finite(), fiber(),
      exceptional_locus(), etc.
    """

    # _sage_morphism: sage.schemes.generic.morphism.SchemeMorphism

    @abstractmethod
    def domain(self) -> Variety:
        """Return the source variety $X$."""
        ...

    @abstractmethod
    def codomain(self) -> Variety:
        """Return the target variety $Y$."""
        ...

    @abstractmethod
    def degree(self) -> int:
        """Return the degree of the morphism."""
        ...

    @abstractmethod
    def is_finite(self) -> bool:
        """Check if the morphism is finite."""
        ...

    @abstractmethod
    def is_étale(self) -> bool:
        """Check if the morphism is étale."""
        ...


class BirationalMap(ABC):
    r"""A birational map $X \dashrightarrow Y$."""

    @abstractmethod
    def is_regular(self) -> bool:
        """Check if the map is actually a regular morphism."""
        ...

    @abstractmethod
    def inverse(self) -> BirationalMap:
        """Return the inverse birational map."""
        ...


# ============================================================================
# SPECIALIZATIONS: DIMENSION 1 (CURVES)
# ============================================================================


class Curve(Variety):
    """Algebraic curve (dimension 1)."""

    @override
    def dimension(self) -> int:
        return 1

    @abstractmethod
    def is_nodal(self) -> bool:
        """Check if the curve has only nodes as singularities."""
        ...

    @abstractmethod
    def nodes(self) -> list[Point]:
        """Return the list of node singularities."""
        ...


# ============================================================================
# SPECIALIZATIONS: DIMENSION 2 (SURFACES)
# ============================================================================


class Surface(Variety):
    """Algebraic surface (dimension 2)."""

    @override
    def dimension(self) -> int:
        return 2


class Blowup(VarietyMorphism):
    """A blowup of a surface at a center (points or curves)."""

    @abstractmethod
    def center(self) -> Subvariety:
        """Return the center being blown up."""
        ...

    @abstractmethod
    def exceptional_divisor(self) -> Divisor:
        """Return the exceptional divisor (or their union)."""
        ...


class CobleSurface(Surface):
    r"""Coble surface $= \mathrm{Bl}_{p_1,\dots,p_{10}}\mathbb{P}^2$.

    The surface obtained by blowing up $\mathbb{P}^2$ at the 10 nodes of a rational
    sextic curve.

    - $\mathrm{Pic}(S) \cong I_{1,10}$: generated by $H, E_1,\dots,E_{10}$ with
      $H^2 = 1$, $E_i^2 = -1$, all cross-terms zero; signature $(1, 10)$.
    - Let $f: X \to S$ be the K3 double cover.  The rank-11 lattice $f^*\mathrm{Pic}(S)
      \subset H^2(X, \mathbb{Z})$ is obtained by pulling back divisor classes along
      the cover, so its form is twice the intersection form on $\mathrm{Pic}(S)$.
      Computing this pullback lattice and its discriminant data is part of the Coble
      pipeline; the orthogonal complement in the K3 lattice is a separate
      transcendental computation.

    Defining property: $h^0(-K_S) = 0$ and $h^0(-2K_S) = 1$ (the unique member of
    $|-2K_S|$ is the proper transform of the rational sextic).
    """

    @classmethod
    @abstractmethod
    def from_sextic(cls, C: Curve) -> Self:
        r"""
        Construct as blowup at the nodes of a singular sextic curve.
        """
        ...

    @classmethod
    @abstractmethod
    def from_nodes(cls, points: list[Point]) -> Self:
        r"""Construct from 10 points in $\mathbb{P}^2$.

        The 10 points should be the nodes of some rational sextic.
        """
        ...

    @abstractmethod
    def underlying_curve(self) -> Curve:
        """Return the rational sextic whose nodes were blown up."""
        ...

    @abstractmethod
    def exceptional_divisors(self) -> list[Divisor]:
        r"""Return the 10 exceptional divisors $E_1, \dots, E_{10}$."""
        ...

    @abstractmethod
    def coble_lattice(self) -> Lattice:
        r"""Return the pullback lattice on the K3 cover induced by $\mathrm{Pic}(S)$."""
        ...


class BranchedCover(VarietyMorphism):
    r"""A branched cover $f: Y \to X$, a finite morphism ramified over a divisor.

    Inherits domain() (= total space $Y$), codomain() (= base $X$), degree(),
    is_finite(), is_étale() from VarietyMorphism.
    """

    @abstractmethod
    def branch_divisor(self) -> Divisor:
        r"""Return the branch divisor $D \subset X$ (ramification locus)."""
        ...

    @abstractmethod
    def ramification_divisor(self) -> Divisor:
        r"""Return the ramification divisor $R \subset Y$, where $K_Y = f^* K_X + R$."""
        ...

    @abstractmethod
    def ramification_index(self, point: Point) -> int:
        r"""Return the ramification index $e_p$ at a point $p \in Y$."""
        ...

    @abstractmethod
    def satisfies_riemann_hurwitz(self) -> bool:
        r"""Verify $2g_Y - 2 = \deg(f)(2g_X - 2) + \deg R$ (Riemann-Hurwitz)."""
        ...


# ============================================================================
# SPECIALIZATIONS: K3 AND ENRIQUES SURFACES
# ============================================================================


class K3Surface(Surface):
    r"""A K3 surface: smooth projective surface with $p_g = 1$, $q = 0$, $K_X \sim 0$.

    In the Coble construction, arises as the double cover of $\mathbb{P}^2$
    branched over a rational sextic $C$: the surface $w^2 = F(x,y,z)$ in
    $\mathbb{P}(1,1,1,3)$.
    """

    @classmethod
    @abstractmethod
    def from_branch_sextic(cls, sextic: Curve) -> Self:
        r"""Construct as the double cover of $\mathbb{P}^2$ branched over a sextic."""
        ...

    @override
    def geometric_genus(self) -> int:
        """K3 surfaces satisfy $p_g = 1$ by definition."""
        return 1

    @override
    def q(self) -> int:
        """K3 surfaces satisfy $q = 0$ by definition."""
        return 0

    @override
    def is_calabi_yau(self) -> bool:
        """K3 surfaces have trivial canonical bundle ($K_X \\sim 0$)."""
        return True

    @override
    def kodaira_dimension(self) -> int:
        """K3 surfaces have Kodaira dimension 0."""
        return 0


class EnriquesSurface(Surface):
    r"""An Enriques surface: $p_g = 0$, $q = 0$, $2K_Z \sim 0$, $K_Z \not\sim 0$.

    Every Enriques surface is the quotient $Z = X / \iota$ of a K3 surface $X$
    by a fixed-point-free involution $\iota$ (the Enriques involution).
    """

    @abstractmethod
    def k3_cover(self) -> K3Surface:
        r"""Return the canonical K3 double cover $X \to Z$."""
        ...

    @abstractmethod
    def enriques_involution(self) -> VarietyMorphism:
        r"""Return the deck transformation $\iota: X \to X$ (fixed-point-free)."""
        ...

    @override
    def geometric_genus(self) -> int:
        """Enriques surfaces satisfy $p_g = 0$."""
        return 0

    @override
    def q(self) -> int:
        """Enriques surfaces satisfy $q = 0$."""
        return 0

    @override
    def kodaira_dimension(self) -> int:
        """Enriques surfaces have Kodaira dimension 0."""
        return 0


# ============================================================================
# COHERENT SHEAVES
# ============================================================================


class CoherentSheaf(ABC):
    """A coherent sheaf on a variety.

    Implementation notes:
    - Concrete implementations wrap Sage sheaves
      (see sage.categories.sheaves Sheaf) and provide
      h^0, h^1, Euler characteristic, Chern class, etc.
    """

    @classmethod
    @abstractmethod
    def from_divisor(cls, D: Divisor) -> Self:
        """
        Construct O_X(D) from D.
        """
        ...

    @abstractmethod
    def base_variety(self) -> Variety:
        """Return the variety on which this sheaf is defined."""
        ...

    @abstractmethod
    def rank(self) -> int:
        """Return the rank of the sheaf."""
        ...

    @abstractmethod
    def h(self, n: int) -> int:
        r"""Return $h^n(\mathcal{F}) = \dim H^n(X, \mathcal{F})$."""
        ...

    @abstractmethod
    def euler_characteristic(self) -> int:
        r"""Return $\chi(\mathcal{F}) = \sum (-1)^i h^i(\mathcal{F})$."""
        ...

    @abstractmethod
    def twist(self, n: int) -> Self:
        r"""
        Return F(n) := F \otimes O_X(n)
        """
        ...

    @abstractmethod
    def dual(self) -> Self:
        """Return F^*"""
        ...


# ============================================================================
# FAMILIES OF VARIETIES
# ============================================================================


class FamilyOfVarieties(VarietyMorphism):
    r"""A flat family of varieties $f: \mathcal{X} \to S$.

    A flat VarietyMorphism where domain() = total space $\mathcal{X}$ and
    codomain() = base scheme $S$. Inherits domain(), codomain(), degree(),
    is_finite(), is_étale() from VarietyMorphism.
    """

    @abstractmethod
    def fiber(self, s: Point) -> Variety:
        r"""Return the fiber $X_s = f^{-1}(s)$ over $s \in S$."""
        ...

    @abstractmethod
    def specialization(self, s: Point) -> Variety:
        r"""Return the specialized variety at $s$ (e.g. stable model at boundary).

        See https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/algebraic_scheme.html
        for degeneration handling.
        """
        ...

    def hypersurface_family_equation(self) -> Any:
        r"""Return the unique defining equation for a one-parameter hypersurface family."""
        total_space = self.domain()
        base = self.codomain()
        assert base.dimension() == 1
        assert total_space.is_hypersurface()
        equations = total_space.equations()
        assert len(equations) == 1
        return equations[0]

    def hodge_theoretic_monodromy(self) -> HodgeTheoreticMonodromy:
        r"""Return Picard-Fuchs and monodromy data via the vendored Singular backend."""
        cached = getattr(self, "_hodge_theoretic_monodromy_cache", None)
        if cached is None:
            from src.backends.foliation_backend import hodge_theoretic_monodromy_of_family

            cached = hodge_theoretic_monodromy_of_family(self)
            setattr(self, "_hodge_theoretic_monodromy_cache", cached)
        return cached

    def milnor_number(self) -> int:
        r"""Return the Milnor number used by the Picard-Fuchs/monodromy solver."""
        return self.hodge_theoretic_monodromy().milnor_number

    def picard_fuchs_operator(self) -> UnivariateDifferentialOperatorOverUnivariateRing:
        r"""Return the Picard-Fuchs operator attached to this family."""
        return self.hodge_theoretic_monodromy().picard_fuchs_operator

    def indicial_polynomial(self):
        r"""Return the indicial polynomial extracted from the Picard-Fuchs operator."""
        return self.hodge_theoretic_monodromy().indicial_polynomial

    def monodromy_matrix(self):
        r"""Return the Hodge-theoretic monodromy matrix in the logarithmic Jordan basis."""
        return self.hodge_theoretic_monodromy().monodromy_matrix

    def nilpotent_monodromy_matrix(self):
        r"""Return the nilpotent matrix $N = \\log(T_u)$ in the logarithmic Jordan basis."""
        return self.hodge_theoretic_monodromy().nilpotent_monodromy_matrix

    def monodromy_jordan_form(self):
        r"""Return the standard Jordan normal form of the monodromy matrix."""
        return self.hodge_theoretic_monodromy().monodromy_jordan_form
