#!/usr/bin/env sage

from sage.all import euler_phi, graphs
from sage.groups.group import Group
from sage.groups.perm_gps.permgroup_named import (
    CyclicPermutationGroup as CyclicGroup,
)
from sage.groups.perm_gps.permgroup_named import (
    DihedralGroup,
    QuaternionGroup,
    SymmetricGroup,
)


def analyze_automorphism_group(G: Group, group_name: str = "") -> Group:
    """
    Analyze the automorphism group of G with detailed information.
    
    Parameters:
    G: A SageMath group object
    group_name: Optional name for the group
    
    Returns:
    The automorphism group
    """
    print(f"=== Automorphism Analysis: {group_name or 'Group'} ===")

    group_order = G.order()
    print(f"Original group order: {group_order}")

    aut_group = G.automorphism_group()
    print("✓ Automorphism group computation: SUCCESS")

    aut_order = aut_group.order()
    print(f"Automorphism group order: {aut_order}")

    structure = aut_group.structure_description()
    print(f"Structure: {structure}")

    generators = aut_group.gens()
    print(f"Number of generators: {len(generators)}")
    
    # Show action on original group elements
    print("\nAutomorphism action on group elements:")
    elements = list(G)[:min(8, len(G))]  # Show first 8 elements
    for i, gen in enumerate(generators[:3]):  # Show first 3 generators
        print(f"  Generator {i}:")
        for elem in elements:
            image = gen(elem)
            if image != elem:
                print(f"    {elem} → {image}")
    
    return aut_group

def compare_automorphism_orders(groups_dict: dict[str, Group]) -> None:
    """
    Compare automorphism group orders for multiple groups.
    
    Parameters:
    groups_dict: Dictionary {name: group} of groups to compare
    """
    print("=== Automorphism Group Order Comparison ===")
    print(f"{'Group':<20} {'Order':<8} {'Aut Order':<12} {'Ratio':<8}")
    print("-" * 50)
    
    for name, G in groups_dict.items():
        order = G.order()
        aut_order = G.automorphism_group().order()
        ratio = aut_order / order
        print(f"{name:<20} {order:<8} {aut_order:<12} {ratio:<8.2f}")

def find_inner_automorphisms(G: Group) -> Group:
    """
    Find the inner automorphism group and compare to full automorphism group.
    
    Parameters:
    G: A SageMath group object
    """
    print("=== Inner vs Full Automorphisms ===")
    print(f"Group order: {G.order()}")
    
    # Full automorphism group
    aut_group = G.automorphism_group()
    print(f"Full automorphism group order: {aut_group.order()}")
    
    # Inner automorphisms (conjugation by group elements)
    # Inn(G) ≅ G/Z(G) where Z(G) is the center
    center = G.center()
    center_order = center.order()
    inner_aut_order = G.order() // center_order

    print(f"Center order: {center_order}")
    print(f"Inner automorphism group order: {inner_aut_order}")
    print(f"Outer automorphism group order: {aut_group.order() // inner_aut_order}")
    print("Center elements:", list(center))
    
    return aut_group

def automorphism_series_analysis(n_max: int = 12) -> None:
    """
    Analyze automorphism groups for series of groups.
    
    Parameters:
    n_max: Maximum parameter for group series
    """
    print("=== Automorphism Series Analysis ===")
    
    # Cyclic groups
    print("\nCyclic groups Z/nZ:")
    print(f"{'n':<4} {'|Aut(Z/nZ)|':<12} {'φ(n)':<8}")
    print("-" * 25)
    
    for n in range(2, n_max + 1):
        G = CyclicGroup(n)
        aut_order = G.automorphism_group().order()
        phi_n = euler_phi(n)
        print(f"{n:<4} {aut_order:<12} {phi_n:<8}")
    
    # Dihedral groups
    print("\nDihedral groups D_n:")
    print(f"{'n':<4} {'|D_n|':<8} {'|Aut(D_n)|':<12}")
    print("-" * 25)
    
    for n in range(3, min(n_max + 1, 8)):  # Limit to avoid large computations
        G = DihedralGroup(n)
        aut_order = G.automorphism_group().order()
        print(f"{n:<4} {G.order():<8} {aut_order:<12}")

def graph_automorphism_demo() -> None:
    """
    Demonstrate automorphism computation for graphs.
    """
    print("=== Graph Automorphism Examples ===")
    
    graphs_to_test = [
        ("Complete graph K4", graphs.CompleteGraph(4)),
        ("Cycle graph C6", graphs.CycleGraph(6)),
        ("Petersen graph", graphs.PetersenGraph()),
        ("Cube graph", graphs.CubeGraph(3)),
    ]
    
    for name, graph in graphs_to_test:
        aut_group = graph.automorphism_group()
        print(f"{name}:")
        print(f"  Vertices: {graph.num_verts()}")
        print(f"  Automorphism group order: {aut_group.order()}")
        print(f"  Generators: {len(aut_group.gens())}")
        print()

# Example usage
if __name__ == "__main__":
    print("=== SageMath Automorphism Group Analysis ===\n")
    
    # Individual group analysis
    print("1. Detailed analysis of specific groups:")
    analyze_automorphism_group(CyclicGroup(8), "Z/8Z")
    print()
    
    analyze_automorphism_group(DihedralGroup(4), "D4")
    print()
    
    analyze_automorphism_group(SymmetricGroup(4), "S4")
    print()
    
    # Group comparison
    print("2. Comparison of multiple groups:")
    test_groups = {
        "Z/6Z": CyclicGroup(6),
        "Z/8Z": CyclicGroup(8),
        "D4": DihedralGroup(4),
        "S3": SymmetricGroup(3),
        "Q8": QuaternionGroup(),
    }
    compare_automorphism_orders(test_groups)
    print()
    
    # Inner automorphisms
    print("3. Inner automorphism analysis:")
    find_inner_automorphisms(DihedralGroup(4))
    print()
    
    # Series analysis
    print("4. Series analysis:")
    automorphism_series_analysis(8)
    print()
    
    # Graph automorphisms
    print("5. Graph automorphisms:")
    graph_automorphism_demo()
    
    print("\n=== Usage Notes ===")
    print("This program leverages SageMath's built-in automorphism computation")
    print("and focuses on analysis and comparison rather than reimplementation.")
    print("\nFor custom analysis:")
    print("G = YourGroup()")
    print("analyze_automorphism_group(G, 'Your Group Name')")
    print("\n=== Guarantees ===")
    print("✓ GUARANTEED: CyclicGroup, SymmetricGroup, DihedralGroup, AbelianGroup")
    print("✓ GUARANTEED: GL/SL/PSL over finite fields, QuaternionGroup, graph groups")
    print("⚠ LIKELY: PermutationGroup, CoxeterGroup, BraidGroup (finite cases)")
    print("⚡ LIMITED: FreeGroup, finitely presented groups (infinite cases)")
    print("✗ NO GUARANTEE: Custom groups, very large groups, arbitrary rings")
    print("\nRun full test suite: sage test_automorphism_groups.py")
    print("Check guarantees: sage automorphism_guarantees.py")
