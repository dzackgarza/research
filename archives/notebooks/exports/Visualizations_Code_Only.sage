"""
Code extracted from: Visualizations.ipynb
This file contains only the code cells from the notebook.
"""

# === Code Cell 1 ===

var('x,y,z')
p=x^3+y^3+z^3+1-0.25*(x+y+z+1)^3
r=5
color='aquamarine'
s = implicit_plot3d(p==0, (x,-r,r), (y,-r,r), (z,-r,r), plot_points=100, region=lambda x,y,z: x**2+y**2+z**2<=r*r, color=color)
s.show(frame=False, viewer='threejs')


# === Code Cell 2 ===

x*x*x+y*y*y+z*z*z+1-0.25*(x+y+z+1)*(x+y+z+1)*(x+y+z+1)

