"""
Hyperbolic Diagram Creation Functions
=====================================

This module contains functions for creating and manipulating hyperbolic diagrams,
including tessellations, reflections, and geometric constructions in various 
hyperbolic models (Poincaré Disc, Upper Half Plane).

Extracted from the Isometry Searching.ipynb notebook.
"""

# Required imports for SageMath
from sage.all import *


# Initialize hyperbolic plane models (will be used globally)
UHP = HyperbolicPlane().UHP()
PD = HyperbolicPlane().PD()

# Global variables for tessellation functions
basealpha = 1.0
allpts = []
allgeos = []


# === IMAGE GENERATION FUNCTIONS ===

def generate_asymptotically_parallel_svg(filename="asymptotically_parallel.svg"):
    """
    Generate an image showing asymptotically parallel geodesics in the Poincaré Disc model.
    
    This creates two geodesics that are asymptotically parallel (they meet at a point 
    on the boundary circle) along with an auxiliary line.
    
    Parameters:
    -----------
    filename : str, default="asymptotically_parallel.svg"
        Output filename for the saved image
        
    Returns:
    --------
    Graphics object
        The plot containing the asymptotically parallel geodesics
    """
    # Load the hyperbolic plane in the Poincaré Disc model
    H = HyperbolicPlane().PD()

    # Define two hyperbolic geodesics with endpoints on the boundary (asymptotically parallel)
    tz1, tz2 = 2 * pi * I / 6, 2 * pi * I / 2
    z1, z2 = exp(tz1), exp(tz2)

    tw1, tw2 = 2 * pi * I / 6, -2 * pi * I / 24
    w1, w2 = exp(tw1), exp(tw2)

    g1 = H.get_geodesic(z1, z2)
    g2 = H.get_geodesic(w1, w2)

    # Create auxiliary line
    s = 0.6
    t = -1/2
    g3 = line([
        (1/2) * (1 + 3*t) + I * sqrt(3)/2 * (1 - t), 
        (1/2) * (1 + 3*s) + I * sqrt(3)/2 * (1 - s)
    ], linestyle="--", color="black", thickness=2)

    p = g1.plot(color="orange", thickness=2) + g2.plot(color="blue", thickness=2) + g3.plot()
    p.save_image(filename)
    return p


def generate_ultraparallel_plane_model_svg(filename="ultraparallel_plane_model.svg"):
    """
    Generate an image showing ultraparallel geodesics in the Upper Half Plane model.
    
    This demonstrates two geodesics that are ultraparallel (they have a unique 
    common perpendicular) in the UHP model.
    
    Parameters:
    -----------
    filename : str, default="ultraparallel_plane_model.svg"
        Output filename for the saved image
        
    Returns:
    --------
    Graphics object
        The plot containing the ultraparallel geodesics and their common perpendicular
    """
    # Load the hyperbolic plane in the Upper Half Plane model
    H = HyperbolicPlane().UHP()

    # Define two hyperbolic geodesics
    g1 = H.get_geodesic(-1, 3)
    g2 = H.get_geodesic(-3, -2)

    # Create auxiliary elements
    g3 = line([0, 3 * I], linestyle="--", alpha=0.2, color="black")
    g4 = g1.common_perpendicular(g2)

    p = (g1.plot(color="orange", thickness=2, ymin=-0.2, xmin=-4, xmax=4) + 
         g2.plot(color="blue", thickness=2) + 
         g3.plot() + 
         g4.plot(linestyle="--", color="black"))
    
    p.save_image(filename)
    return p


def generate_asymptotically_parallel_plane_model(filename="asymptotically_parallel_plane_model.svg"):
    """
    Generate an image showing asymptotically parallel geodesics in the Upper Half Plane model.
    
    Parameters:
    -----------
    filename : str, default="asymptotically_parallel_plane_model.svg"
        Output filename for the saved image
        
    Returns:
    --------
    Graphics object
        The plot containing asymptotically parallel geodesics in UHP
    """
    # Load the hyperbolic plane in the Upper Half Plane model
    H = HyperbolicPlane().UHP()

    # Define two geodesics that are asymptotically parallel
    g1 = H.get_geodesic(-3, 3)
    g2 = H.get_geodesic(-3, 1)

    # Create auxiliary elements
    g3 = line([0, 4 * I], linestyle="--", alpha=0.2, color="black")
    g4 = line([-3 - 0.4 * I, -3 + 4 * I], linestyle="--", color="black")

    p = (g1.plot(color="orange", thickness=2, ymin=-0.2, xmin=-4, xmax=4) + 
         g2.plot(color="blue", thickness=2) + 
         g3.plot() + 
         g4.plot())
    
    p.save_image(filename)
    return p


def generate_hyperbolic_triangle_examples():
    """
    Generate basic hyperbolic triangle examples and save them.
    
    This creates several example triangles using the hyperbolic_triangle function.
    
    Returns:
    --------
    list
        List of graphics objects for the generated triangles
    """
    triangles = []
    
    # Example 1: Triangle in PD model with complex coordinates
    try:
        tri1 = hyperbolic_triangle(
            exp(2 * pi * I / 2), exp(2 * pi * I / 3), 1, 
            model='PD', color='cyan', fill=True, resolution=200
        )
        tri1.save_image("hyperbolic_triangle_pd_example1.png")
        triangles.append(tri1)
    except:
        pass
    
    # Example 2: Triangle in UHP model
    try:
        tri2 = hyperbolic_triangle(
            -1, Infinity, 1, 
            fill=True, rgbcolor="#80DAEB", resolution=200, 
            xmin=-2, xmax=2, ymax=3, axes=False
        )
        tri2.save_image("hyperbolic_triangle_uhp_example.png")
        triangles.append(tri2)
    except:
        pass
    
    return triangles


def generate_complete_tessellation_sequence(max_iterations=6):
    """
    Generate a complete sequence of tessellation images showing the progression.
    
    This function creates the full tessellation sequence as shown in the notebook,
    saving images at each major step.
    
    Parameters:
    -----------
    max_iterations : int, default=6
        Maximum number of tessellation iterations
        
    Returns:
    --------
    Graphics object
        The final tessellation graphics
    """
    global allpts, basealpha
    
    # Reset globals
    reset_tessellation_globals()
    
    # Initialize hyperbolic plane models
    UHP = HyperbolicPlane().UHP()
    PD = HyperbolicPlane().PD()
    
    # Create fundamental triangle vertices
    p1 = UHP.get_point(-1).to_model(PD)
    p2 = UHP.get_point(1).to_model(PD)
    p3 = UHP.get_point(Infinity).to_model(PD)

    allpts = [(p1.coordinates(), p2.coordinates(), p3.coordinates())]
    a, b, c = allpts.pop(0)

    # Create initial geodesics
    g1 = PD.get_geodesic(a, b, color="blue", axes=False)
    g2 = PD.get_geodesic(b, c, color="blue", axes=False)
    g3 = PD.get_geodesic(c, a, color="blue", axes=False)

    # Create initial triangle
    basealpha = 1.0
    tri1 = hyperbolic_triangle(
        a, b, c, model="PD", fill=True, rgbcolor="#80DAEB", 
        axes=False, resolution=400, alpha=basealpha
    )
    tri1 += g1.plot() + g2.plot() + g3.plot()
    tri1.save_image("tessellation_start.png")

    # First reflection
    basealpha = 0.5
    tri1 += do_reflect(a, b, c)
    tri1.save_image("tessellation_0.png")

    # Iterative tessellation with image saving
    basealpha = 0.25
    j = 1
    i = 1
    
    while true:
        print(f"Iteration {i}")
        if i in [3^n + 1 for n in [1..10]]:
            basealpha = basealpha / 5
            tri1.save_image(f'tessellation_{j}.png')
            j += 1
            if j >= max_iterations:
                break
        
        if allpts:  # Check if there are points to process
            a, b, c = allpts.pop(0)
            tri1 += do_reflect(a, b, c)
        else:
            break
        
        i += 1
        if i % 100 == 0:
            print(".", end='')

    tri1.save_image('tessellation_end.png')
    print(f"\nGenerated tessellation sequence with {j} images")
    return tri1


def generate_all_hyperbolic_images():
    """
    Generate all hyperbolic images that were created in the original notebook.
    
    This is a convenience function that creates all the images at once.
    
    Returns:
    --------
    dict
        Dictionary mapping image names to their graphics objects
    """
    images = {}
    
    print("Generating asymptotically parallel geodesics...")
    images['asymptotically_parallel'] = generate_asymptotically_parallel_svg()
    
    print("Generating ultraparallel plane model...")
    images['ultraparallel_plane'] = generate_ultraparallel_plane_model_svg()
    
    print("Generating asymptotically parallel plane model...")
    images['asymptotically_parallel_plane'] = generate_asymptotically_parallel_plane_model()
    
    print("Generating hyperbolic triangle examples...")
    images['triangle_examples'] = generate_hyperbolic_triangle_examples()
    
    print("Generating complete tessellation sequence...")
    images['tessellation'] = generate_complete_tessellation_sequence()
    
    print("All images generated successfully!")
    return images


# === ORIGINAL TESSELLATION FUNCTIONS ===

def do_reflect(p1, p2, p3):
    """
    Create hyperbolic reflections and tessellations from a triangle.
    
    This function takes three points forming a hyperbolic triangle and generates
    reflections across each edge, creating new triangles for tessellation.
    
    Parameters:
    -----------
    p1, p2, p3 : coordinates
        Three points defining a hyperbolic triangle
    
    Returns:
    --------
    Graphics object
        Combined graphics object containing the reflected triangles and geodesics
    """
    global allpts
    global basealpha

    # Create geodesics from the triangle edges
    g1 = PD.get_geodesic(p1, p2, color="blue", axes=False)
    g2 = PD.get_geodesic(p2, p3, color="blue", axes=False)
    g3 = PD.get_geodesic(p3, p1, color="blue", axes=False)
    
    # Get reflection involutions for each edge
    inv1 = g1.reflection_involution()
    inv2 = g2.reflection_involution()
    inv3 = g3.reflection_involution()

    # First reflection (across edge g1)
    g1p = inv1 * g1
    g2p = inv1 * g2
    g3p = inv1 * g3
    
    newpoints = tuple(Set([
        g1p.start().coordinates(), g1p.end().coordinates(),
        g2p.start().coordinates(), g2p.end().coordinates(), 
        g3p.start().coordinates(), g3p.end().coordinates()
    ]))
    allpts.append(newpoints)

    t1 = hyperbolic_triangle(
        newpoints[0], newpoints[1], newpoints[2], 
        model="PD", fill=True, rgbcolor="#80DAEB", 
        axes=False, alpha=basealpha, resolution=400
    )
    t1 += g1p.plot(color="blue", axes=False) + g2p.plot(color="blue", axes=False) + g3p.plot(color="blue", axes=False)

    # Second reflection (across edge g2)
    g1p = inv2 * g1
    g2p = inv2 * g2
    g3p = inv2 * g3

    newpoints = tuple(Set([
        g1p.start().coordinates(), g1p.end().coordinates(),
        g2p.start().coordinates(), g2p.end().coordinates(), 
        g3p.start().coordinates(), g3p.end().coordinates()
    ]))
    allpts.append(newpoints)

    t2 = hyperbolic_triangle(
        newpoints[0], newpoints[1], newpoints[2], 
        model="PD", fill=True, rgbcolor="#80DAEB", 
        axes=False, alpha=basealpha, resolution=400
    )
    t2 += g1p.plot(color="blue", axes=False) + g2p.plot(color="blue", axes=False) + g3p.plot(color="blue", axes=False)

    # Third reflection (across edge g3)
    g1p = inv3 * g1
    g2p = inv3 * g2
    g3p = inv3 * g3

    newpoints = tuple(Set([
        g1p.start().coordinates(), g1p.end().coordinates(),
        g2p.start().coordinates(), g2p.end().coordinates(), 
        g3p.start().coordinates(), g3p.end().coordinates()
    ]))
    allpts.append(newpoints)

    t3 = hyperbolic_triangle(
        newpoints[0], newpoints[1], newpoints[2], 
        model="PD", fill=True, rgbcolor="#80DAEB", 
        axes=False, alpha=basealpha, resolution=400
    )
    t3 += g1p.plot(color="blue", axes=False) + g2p.plot(color="blue", axes=False) + g3p.plot(color="blue", axes=False)

    return t1 + t2 + t3


def create_hyperbolic_tessellation(iterations=6, initial_alpha=1.0):
    """
    Create a hyperbolic tessellation starting from a fundamental triangle.
    
    This function generates a tessellation of the Poincaré disc using reflections
    of a fundamental triangle across its edges.
    
    Parameters:
    -----------
    iterations : int, default=6
        Number of tessellation iterations to perform
    initial_alpha : float, default=1.0
        Initial transparency level for the triangles
        
    Returns:
    --------
    Graphics object
        The complete tessellation graphics
    """
    global allpts, basealpha
    
    # Initialize hyperbolic plane models
    UHP = HyperbolicPlane().UHP()
    PD = HyperbolicPlane().PD()
    
    # Create fundamental triangle vertices
    p1 = UHP.get_point(-1).to_model(PD)
    p2 = UHP.get_point(1).to_model(PD)
    p3 = UHP.get_point(Infinity).to_model(PD)

    allpts = [(p1.coordinates(), p2.coordinates(), p3.coordinates())]

    a, b, c = allpts.pop(0)

    # Create initial geodesics
    g1 = PD.get_geodesic(a, b, color="blue", axes=False)
    g2 = PD.get_geodesic(b, c, color="blue", axes=False)
    g3 = PD.get_geodesic(c, a, color="blue", axes=False)

    # Create initial triangle
    basealpha = initial_alpha
    tri1 = hyperbolic_triangle(
        a, b, c, model="PD", fill=True, rgbcolor="#80DAEB", 
        axes=False, resolution=400, alpha=basealpha
    )
    tri1 += g1.plot() + g2.plot() + g3.plot()
    
    # Save initial state
    tri1.save_image("tesselation_start.png")

    # First reflection
    basealpha = 0.5
    tri1 += do_reflect(a, b, c)
    tri1.save_image("tesselation_0.png")

    # Iterative tessellation
    basealpha = 0.25
    j = 1
    i = 1
    
    while true:
        print(i)
        if i in [3^n + 1 for n in [1..10]]:
            basealpha = basealpha / 5
            tri1.save_image(f'tesselation_{j}.png')
            j += 1
            if j >= iterations:
                break
        
        if allpts:  # Check if there are points to process
            a, b, c = allpts.pop(0)
            tri1 += do_reflect(a, b, c)
        
        i += 1
        if i % 100 == 0:
            print("i,", end='')

    tri1.save_image('tesselation_end.png')
    return tri1


def create_hyperbolic_triangle_basic(p1_coords, p2_coords, p3_coords, model="PD", **kwargs):
    """
    Create a basic hyperbolic triangle with specified coordinates.
    
    Parameters:
    -----------
    p1_coords, p2_coords, p3_coords : tuple or complex
        Coordinates of the three triangle vertices
    model : str, default="PD"
        Hyperbolic model to use ("PD" for Poincaré Disc, "UHP" for Upper Half Plane)
    **kwargs : additional arguments
        Additional arguments passed to hyperbolic_triangle function
        
    Returns:
    --------
    Graphics object
        The hyperbolic triangle graphics
    """
    default_kwargs = {
        'fill': True,
        'rgbcolor': '#80DAEB',
        'axes': False,
        'resolution': 400
    }
    default_kwargs.update(kwargs)
    
    return hyperbolic_triangle(p1_coords, p2_coords, p3_coords, model=model, **default_kwargs)


def create_hyperbolic_geodesics_parallel_demo():
    """
    Create a demonstration of asymptotically parallel geodesics in hyperbolic plane.
    
    Returns:
    --------
    Graphics object
        Visualization of asymptotically parallel geodesics
    """
    # Load the hyperbolic plane in the Poincaré Disc model
    H = HyperbolicPlane().PD()

    # Define two hyperbolic geodesics with endpoints on the boundary (non-intersecting)
    tw1, tw2 = 2 * pi * I / 6, -2 * pi * I / 24
    w1, w2 = exp(tw1), exp(tw2)

    z1 = exp(2 * pi * I / 3)
    z2 = exp(-2 * pi * I / 12)

    g1 = H.get_geodesic(z1, z2)
    g2 = H.get_geodesic(w1, w2)

    # Create auxiliary line
    s = 0.6
    t = -1/2
    g3 = line([
        (1/2) * (1 + 3*t) + I * sqrt(3)/2 * (1 - t), 
        (1/2) * (1 + 3*s) + I * sqrt(3)/2 * (1 - s)
    ], linestyle="--", color="black", thickness=2)

    p = g1.plot(color="orange", thickness=2) + g2.plot(color="blue", thickness=2) + g3.plot()
    return p


def create_hyperbolic_geodesics_uhp_demo():
    """
    Create a demonstration of geodesics in the Upper Half Plane model.
    
    Returns:
    --------
    Graphics object
        Visualization of geodesics and their relationships in UHP
    """
    # Load the hyperbolic plane in the Upper Half Plane model
    H = HyperbolicPlane().UHP()

    # Define geodesics
    g1 = H.get_geodesic(-1, 3)
    g2 = H.get_geodesic(-3, -2)

    # Create auxiliary elements
    g3 = line([0, 3 * I], linestyle="--", alpha=0.2, color="black")
    g4 = g1.common_perpendicular(g2)

    p = (g1.plot(color="orange", thickness=2, ymin=-0.2, xmin=-4, xmax=4) + 
         g2.plot(color="blue", thickness=2) + 
         g3.plot() + 
         g4.plot(linestyle="--", color="black"))
    
    return p


def create_fundamental_triangle_pd():
    """
    Create a fundamental hyperbolic triangle in the Poincaré Disc model.
    
    Returns:
    --------
    tuple
        (triangle_graphics, geodesics_list, points_list)
    """
    UHP = HyperbolicPlane().UHP()
    PD = HyperbolicPlane().PD()
    
    # Convert standard points from UHP to PD
    p1 = UHP.get_point(-1).to_model(PD)
    p2 = UHP.get_point(1).to_model(PD)
    p3 = UHP.get_point(Infinity).to_model(PD)

    # Create triangle
    tri = hyperbolic_triangle(
        p1.coordinates(),
        p2.coordinates(),
        p3.coordinates(),
        model="PD",
        fill=True,
        rgbcolor="#80DAEB",
        axes=False,
    )

    # Create geodesics
    g1 = PD.get_geodesic(p1.coordinates(), p2.coordinates(), color="blue", axes=False)
    g2 = PD.get_geodesic(p2.coordinates(), p3.coordinates(), color="blue", axes=False)
    g3 = PD.get_geodesic(p3.coordinates(), p1.coordinates(), color="blue", axes=False)

    return tri, [g1, g2, g3], [p1, p2, p3]


def reset_tessellation_globals():
    """
    Reset global variables used in tessellation functions.
    
    Useful when starting a new tessellation computation.
    """
    global allpts, allgeos, basealpha
    allpts = []
    allgeos = []
    basealpha = 1.0 