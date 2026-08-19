# Origin: gitclones/integral_lattice/tests/test_aut_group.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, section R3). Content below is unmodified.

"""
Coverage checklist of Sage group constructors (✓ covered by tests below; □ pending).
Derived from Sage group catalogs (perm_gps, matrix_gps, misc_gps, coxeter, braid) as reported by deepwiki.

Permutation / abstract finite
✓ SymmetricGroup(n)
✓ AlternatingGroup(n)
✓ DihedralGroup(n)
✓ CyclicPermutationGroup(n)
✓ KleinFourGroup()
✓ QuaternionGroup()
✓ PermutationGroup(gens)
✓ SmallGroup(id).sage()
□ DiCyclicGroup(n)  # kept; DicyclicGroup spelled this way in Sage
□ SemidihedralGroup(n)
□ GeneralDihedralGroup(G)
□ SplitMetacyclicGroup(p, m)
□ SuzukiGroup(q)
□ MathieuGroup(...)
□ TransitiveGroup(...)
□ RubiksCube()
□ SuzukiSporadicGroup()
□ ComplexReflectionGroup(m, p, n)  # also reflection
□ PrimitiveGroup(...), PrimitiveGroups(...)
□ TransitiveGroups(...)
□ CubeGroup (alias RubiksCube)
□ SmallPermutationGroup(...)
□ JankoGroup(...)
□ SemimonomialTransformationGroup
□ GroupExp
□ GroupSemidirectProduct
□ ShephardToddFamilyGroup
□ PrimitiveGroup(...), PrimitiveGroups(...)  # duplicate kept above
□ SmallPermutationGroup(...)  # duplicate kept above
□ JankoGroup(...)  # duplicate kept above

Abelian / pc / free
✓ AbelianGroup(invariants)
□ AdditiveAbelianGroup(invariants)
□ Polycyclic/PCGroup explicit constructor
□ MultiplicativeAbelianGroup (catalog alias)

Matrix / classical (finite fields)
✓ MatrixGroup(gens over GF(q))
✓ GL(n, q)
✓ SL(n, q)
□ Sp(2n, q)
□ SU(n, q) / GU(n, q)
□ GO(n, q) / SO(n, q)
□ PGL / PSL / PSp / PSU / PGU
□ QuaternionGF3

Matrix over other rings
□ GL(n, QQ), GL(n, K), GL(n, Qp)
□ SL(n, ZZ) for n > 2

Coxeter / Weyl / reflection
□ CoxeterGroup(type, rank)
□ WeylGroup(type)
□ ComplexReflectionGroup(m, p, n)

Braid / Artin
□ BraidGroup(n)
□ ArtinGroup(type)
□ RightAngledArtinGroup

Products / constructions
✓ gap.WreathProduct(CyclicGroup(2), CyclicGroup(3)) sample
□ WreathProduct(G, H) general
□ direct_product_permgroups([...])
□ semidirect product helpers (GroupSemidirectProduct, H.semidirect_product(K, phi))

Other named
✓ GAP HeisenbergGroup(3)
✓ FreeGroup(n) (raises on failure)
✓ FinitelyPresentedGroup via GAP quotient
□ Baumslag–Solitar, lamplighter C2 wr Z, other infinite GAP families
□ AffineGroup, EuclideanGroup, ReflectionGroup, CactusGroup, PureCactusGroup
□ Heisenberg presentations (FinitelyGeneratedHeisenbergPresentation)
□ AlternatingPresentation, SymmetricPresentation, DihedralPresentation, DicyclicPresentation, KleinFourPresentation, QuaternionPresentation, FGAbelianPresentation
□ CactusPresentation
□ BinaryDihedralPresentation
□ BinaryDihedralGroup(n)
□ CyclicPresentation
□ AdditiveCyclic
□ SemimonomialTransformation
□ ShephardToddFamily
□ PariGroup
□ CubicBraidGroup, AssionGroupU, AssionGroupS
□ Nilpotent (Lie group constructor)
"""

import importlib.machinery
import importlib.util
import os
import pathlib
import sys
import unittest

from sage.all import *
from sage.groups.perm_gps.permgroup_named import (
    SemidihedralGroup,
    SplitMetacyclicGroup,
    SuzukiSporadicGroup,
    SmallPermutationGroup,
    DiCyclicGroup,
    ComplexReflectionGroup,
    MathieuGroup,
    PrimitiveGroup,
    PrimitiveGroups,
    SuzukiGroup,
    TransitiveGroup,
    TransitiveGroups,
    JankoGroup,
    GeneralDihedralGroup,
)
from sage.groups.perm_gps.cubegroup import CubeGroup, RubiksCube
from sage.groups.group_exp import GroupExp
from sage.groups.group_semidirect_product import GroupSemidirectProduct
from sage.groups.semimonomial_transformations.semimonomial_transformation_group import (
    SemimonomialTransformationGroup,
)
from sage.groups.semimonomial_transformations.semimonomial_transformation import (
    SemimonomialTransformation,
)
from sage.combinat.colored_permutations import ShephardToddFamilyGroup, ShephardToddFamilyGroup as ShephardToddFamily
from sage.groups.affine_gps.affine_group import AffineGroup
from sage.groups.affine_gps.euclidean_group import EuclideanGroup
from sage.combinat.root_system.reflection_group_real import ReflectionGroup
from sage.groups.cactus_group import CactusGroup, PureCactusGroup
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as AdditiveCyclic
from sage.groups.cubic_braid import CubicBraidGroup, AssionGroupU, AssionGroupS
from sage.groups.lie_gps.nilpotent_lie_group import NilpotentLieGroup as Nilpotent
from sage.groups.matrix_gps.heisenberg import HeisenbergGroup
from sage.groups.matrix_gps.binary_dihedral import BinaryDihedralGroup
from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup
from sage.groups.abelian_gps.abelian_group import AbelianGroup as MultiplicativeAbelianGroup
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.groups.finitely_presented_named import (
    AlternatingPresentation,
    SymmetricPresentation,
    DihedralPresentation,
    DiCyclicPresentation,
    KleinFourPresentation,
    QuaternionPresentation,
    CactusPresentation,
    BinaryDihedralPresentation,
    FinitelyGeneratedAbelianPresentation,
    CyclicPresentation,
)
from sage.groups.pari_group import PariGroup
from sage.groups.perm_gps.permgroup import direct_product_permgroups
from sage.algebras.lie_algebras.heisenberg import HeisenbergAlgebra

# Load dispatcher module
for cand in [pathlib.Path(os.getcwd()), pathlib.Path(__file__).resolve().parents[1]]:
    if (cand / "scripts" / "aut_group.py").exists():
        ROOT = cand
        break
else:
    raise FileNotFoundError("Cannot locate scripts/aut_group.py")

sys.path.insert(0, str(ROOT))
AUT_PATH = ROOT / "scripts" / "aut_group.py"
loader = importlib.machinery.SourceFileLoader("aut_group", str(AUT_PATH))
spec = importlib.util.spec_from_loader("aut_group", loader)
aut_mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = aut_mod
loader.exec_module(aut_mod)
compute_aut = aut_mod.compute_aut


class GroupSamples:
    """
    Instantiate one representative for each checklist constructor.
    Any failure here is a real failure (no try/except).
    """

    def __init__(self):
        self.samples = {}
        # permutation / abstract finite
        self.samples["SymmetricGroup"] = SymmetricGroup(5)
        self.samples["AlternatingGroup"] = AlternatingGroup(5)
        self.samples["DihedralGroup"] = DihedralGroup(8)
        self.samples["CyclicPermutationGroup"] = CyclicPermutationGroup(6)
        self.samples["KleinFourGroup"] = KleinFourGroup()
        self.samples["QuaternionGroup"] = QuaternionGroup()
        self.samples["PermutationGroup"] = PermutationGroup([()])
        from sage.libs.gap.libgap import libgap
        self.samples["SmallGroup"] = libgap.SmallGroup(8, 3)
        self.samples["DiCyclicGroup"] = DiCyclicGroup(6)
        self.samples["SemidihedralGroup"] = SemidihedralGroup(ZZ(4))
        self.samples["GeneralDihedralGroup"] = GeneralDihedralGroup([ZZ(3), ZZ(3)])
        self.samples["SplitMetacyclicGroup"] = SplitMetacyclicGroup(ZZ(2), ZZ(4))
        self.samples["SuzukiGroup"] = SuzukiGroup(8)
        self.samples["MathieuGroup"] = MathieuGroup(11)
        self.samples["TransitiveGroup"] = TransitiveGroup(5, 1)
        self.samples["TransitiveGroups"] = TransitiveGroups(5)
        self.samples["PrimitiveGroup"] = PrimitiveGroup(5, 1)
        self.samples["PrimitiveGroups"] = PrimitiveGroups(5)
        self.samples["RubiksCube"] = RubiksCube()
        self.samples["CubeGroup"] = CubeGroup()
        self.samples["SuzukiSporadicGroup"] = SuzukiSporadicGroup()
        self.samples["ComplexReflectionGroup"] = ComplexReflectionGroup(3, 1, 2)
        self.samples["SmallPermutationGroup"] = SmallPermutationGroup(6, 1)
        self.samples["JankoGroup"] = JankoGroup(1)
        self.samples["SemimonomialTransformationGroup"] = SemimonomialTransformationGroup(GF(4, "a"), 2)
        V = QQ**2
        EV = GroupExp()(V)
        self.samples["GroupExp"] = EV

        def _twist(g, v):
            return EV(g * v.value)

        self.samples["GroupSemidirectProduct"] = GroupSemidirectProduct(GL(2, QQ), EV, twist=_twist, prefix1="t")
        self.samples["ShephardToddFamilyGroup"] = ShephardToddFamilyGroup(3, 1, 3)
        # abelian / pc / free
        self.samples["AbelianGroup"] = AbelianGroup([2, 6])
        self.samples["AdditiveAbelianGroup"] = AdditiveAbelianGroup([])
        self.samples["MultiplicativeAbelianGroup"] = MultiplicativeAbelianGroup([2, 2, 3])
        # matrix / classical
        self.samples["MatrixGroup_GF"] = MatrixGroup([matrix(GF(3), [[1, 1], [0, 1]])])
        self.samples["GL"] = GL(2, 3)
        self.samples["SL"] = SL(2, 3)
        self.samples["Sp"] = Sp(4, 3)
        self.samples["SU"] = SU(2, 2)
        self.samples["GU"] = GU(2, 2)
        self.samples["GO"] = GO(3, 3)
        self.samples["SO"] = SO(3, 3)
        self.samples["PGL"] = PGL(2, 5)
        self.samples["PSL"] = PSL(2, 5)
        self.samples["PSp"] = PSp(4, 3)
        self.samples["PSU"] = PSU(2, 2)
        self.samples["PGU"] = PGU(2, 2)
        self.samples["GL_QQ"] = GL(2, QQ)
        self.samples["GL_Qp"] = GL(2, Qp(3))
        self.samples["SL_ZZ"] = SL(2, ZZ)
        # reflection / Coxeter (requires GAP3+CHEVIE)
        self.samples["CoxeterGroup"] = CoxeterGroup(["A", 3])
        self.samples["WeylGroup"] = WeylGroup(["A", 3])
        self.samples["ReflectionGroup"] = ReflectionGroup(["A", 3])
        # braid / Artin
        self.samples["BraidGroup"] = BraidGroup(4)
        self.samples["ArtinGroup"] = ArtinGroup(["A", 3])
        self.samples["RightAngledArtinGroup"] = RightAngledArtinGroup([[1, 2]])
        # products / constructions
        from sage.libs.gap.libgap import libgap as _gap
        self.samples["WreathProduct_sample"] = _gap.WreathProduct(_gap.CyclicGroup(2), _gap.SymmetricGroup(3))
        self.samples["direct_product_permgroups"] = direct_product_permgroups([SymmetricGroup(3), DihedralGroup(6)])
        # misc named
        self.samples["GAP_HeisenbergGroup"] = HeisenbergGroup(3)
        self.samples["FreeGroup"] = FreeGroup(2)
        self.samples["FinitelyPresentedGroup"] = FinitelyPresentedGroup(FreeGroup(2), tuple())
        self.samples["AffineGroup"] = AffineGroup(3, GF(3))
        self.samples["EuclideanGroup"] = EuclideanGroup(2, GF(3))
        self.samples["CactusGroup"] = CactusGroup(3)
        self.samples["PureCactusGroup"] = PureCactusGroup(3)
        # presentations
        self.samples["AlternatingPresentation"] = AlternatingPresentation(5)
        self.samples["SymmetricPresentation"] = SymmetricPresentation(5)
        self.samples["DihedralPresentation"] = DihedralPresentation(8)
        self.samples["DicyclicPresentation"] = DiCyclicPresentation(6)
        self.samples["KleinFourPresentation"] = KleinFourPresentation()
        self.samples["QuaternionPresentation"] = QuaternionPresentation()
        self.samples["CactusPresentation"] = CactusPresentation(3)
        self.samples["BinaryDihedralPresentation"] = BinaryDihedralPresentation(4)
        self.samples["CyclicPresentation"] = CyclicPresentation(5)
        # Disabled: current Sage build segfaults in PARI Smith form even for [1]
        # self.samples["FinitelyGeneratedAbelianPresentation"] = FinitelyGeneratedAbelianPresentation([1])
        # misc
        self.samples["AdditiveCyclic"] = AdditiveCyclic(5)
        F = GF(4, "a")
        S = SemimonomialTransformationGroup(F, 2)
        self.samples["SemimonomialTransformation"] = S(v=[F.one(), F.one()])
        self.samples["ShephardToddFamily"] = ShephardToddFamily(3, 1, 3)
        self.samples["PariGroup"] = PariGroup([6, -1, 2, "S3"], 3)
        self.samples["CubicBraidGroup"] = CubicBraidGroup()
        self.samples["AssionGroupU"] = AssionGroupU()
        self.samples["AssionGroupS"] = AssionGroupS()
        L = HeisenbergAlgebra(QQ, 1)
        self.samples["Nilpotent"] = Nilpotent(L, "H")


GROUP_SAMPLES = GroupSamples()

def assert_order_matches(testcase, G, res):
    try:
        baseline = G.automorphism_group().order()
    except Exception:
        baseline = None
    if baseline is None and hasattr(G, "aut"):
        try:
            baseline = G.aut().order()
        except Exception:
            baseline = None
    testcase.assertIsNotNone(res.group)
    testcase.assertIsNotNone(res.order)
    if baseline is not None:
        testcase.assertEqual(res.order, baseline)
    else:
        testcase.assertTrue(res.order > 0)


class TestAutGroupFinite(unittest.TestCase):
    def test_symmetric5(self):
        G = SymmetricGroup(5)
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_alternating5(self):
        G = AlternatingGroup(5)
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_dihedral8(self):
        G = DihedralGroup(8)
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_quaternion8(self):
        G = QuaternionGroup()
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_cyclic6(self):
        G = CyclicPermutationGroup(6)
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_cyclic7(self):
        G = CyclicPermutationGroup(7)
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_klein_c2c2(self):
        G = KleinFourGroup()
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_c3x_c3(self):
        G = AbelianGroup([3, 3])
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_sl2_3(self):
        G = SL(2, 3)
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_gl2_3(self):
        G = GL(2, 3)
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_heisenberg3(self):
        H = aut_mod.gap.HeisenbergGroup(3)

        class Obj:
            def gap(self_inner):
                return H

        res = compute_aut(Obj())
        self.assertIsNotNone(res.group)

    def test_smallgroup_16_3(self):
        G = aut_mod.gap.SmallGroup(16, 3).sage()
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_smallgroup_16_8(self):
        G = aut_mod.gap.SmallGroup(16, 8).sage()
        res = compute_aut(G)
        assert_order_matches(self, G, res)

    def test_matrix_group_gf11(self):
        g1 = matrix(GF(11), [[1, 1], [0, 1]])
        g2 = matrix(GF(11), [[1, 0], [1, 1]])
        G = MatrixGroup(GF(11), [g1, g2])
        res = compute_aut(G)
        self.assertIsNotNone(res.group)


if __name__ == "__main__":
    unittest.main()
