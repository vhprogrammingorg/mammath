from .constants import pi, e
from .operations import sqrt, ln
from .trig_functions import sin, cos, tan
import math


"""
GEOMETRY
"""

def rad_to_deg(rad):
    """
    Converts radians to degrees
    """
    return rad * 180/pi

def deg_to_rad(deg):
    """
    Converts degrees to radians
    """
    return deg * pi/180

def valid_triangle(s1, s2, s3):
    """
    If a triangle with three given sides is valid
    """
    if s1 + s2 >= s3 and s2 + s3 >= s1 and s1 + s3 >= s2:
        return True
    return False

def triangle_area(l, h):
    """
    Area of a triangle from base and vertical height
    """
    return (l*h)/2

def trapezium_area(a, b, h):
    """
    Area of a trapezium from two parallel sides and vertical height
    """
    return (a+b)/h

def para_area(b, h):
    """
    Area of a parallelogram from base and vertical height
    """
    return b*h

def circle_circumference(r):
    """
    Circumference of a circle from radius
    """
    return 2*pi*r

def circle_area(r):
    """
    Area of a circle from radius
    """
    return pi*(r**2)

def sphere_volume(r):
    """
    Volume of a sphere from radius
    """
    return 4/3*pi*(r**3)

def sphere_area(r):
    """
    Surface area of a sphere from radius
    """
    return 4*pi*(r**2)

def sphere_diametre(r):
    """
    Diameter of a sphere with radius
    """
    return 2*r

def surface_area(a, b, c):
    """
    Surface area of a cuboid with three side lengths
    """
    d = a*b
    e = a*c
    f = b*c
    return 2*(d+e+f)

def surf_area_prism(farea, *args):
    """
    Surface area of a prism with frontal area and length
    """
    total = 2*farea
    i = 0
    while i < len(args):
        total += args[i]
        i += 1
    return total

def volume(a, b, c):
    """
    Volume of a cuboid with three side lengths
    """
    return a*b*c

def cylinder_volume(r, h):
    """
    Volume of a cylinder with height and radius
    """
    return (pi*(r**2))*h

def cylinder_area(r, h):
    """
    Surface area of a cylinder with height and radius
    """
    return (2*pi*r*h)+(2*pi*(r**2))

def cylinder_diametre(v, h):
    """
    Diameter of a cylinder with volume and height
    """
    return 2*(sqrt(v/pi*h))

def cylinder_height(v, r):
    """
    Height of a cylinder with volume and radius
    """
    return v/(pi*(r**2))

def cylinder_radius(h, A):
    """
    radius of a cylinder from height and surface area
    """
    return round(0.5*sqrt(h**2 + 2*(A/pi))-h/2, 5)

def cone_area(r, h):
    """
    Surface area of a cone
    """
    area = pi*r*(r + sqrt(h**2 + r**2))
    return round(area, 5)

def cone_volume(r, h):
    """
    Volume of a cone from radius and height
    """
    vol = pi*r**2*(h/3)
    return round(vol, 5)

def cone_radius(h, vol):
    """
    Radius of cone from height and volume
    """
    rad = sqrt(3*(vol/(pi*h)))
    return round(rad, 5)

def cone_height(r, vol):
    """
    Height of a cone from radius and volume
    """
    height = 3*(vol/(pi*r**2))
    return round(height, 5)

def pythagoras(a, b):
    """
    Returns the hypotenuse of a triangle given a and b sides
    """
    return sqrt(a**2+b**2)

def pythagoras_hyp(c, a):
    """
    Returns the missing side length given one leg and the hypotenuse
    """
    return sqrt(c**2-a**2)

def cos_rule(a, b, A_rad):
    """
    Finds the third side of a triangle given two sides and the angle between them
    """
    return a**2 + b**2 - 2*a*b*cos(A_rad)

def area_tan(n, s):
    """
    Finds the third side of a triangle given two sides and the angle between them
    """
    s1 = s**2
    up = n * s1
    intan = (180 / n)
    tanpart = math.tan(math.radians(intan))
    down = 4 * tanpart
    ans = up / down
    return ans

def polygon_area_nxn(n, s):
    """
    Computes the area of a regular n-sided polygon with lengths s
    """
    return round((n*s**2)/(4*tan(pi/n)), 6)

def pythagorean_triplets(n):
    """
    Prints pythagorean triplets until n
    """
    for b in range(n):
        for a in range(1, b):
            c = sqrt(a * a + b * b)
            if c % 1 == 0:
                print(a, b, int(c))
            
def pythagorean_triplets_check(a, b, c):
    """
    Checks if three numbers can be pythagorean triplets
    """
    return True if a**2 + b**2 == c**2 else False

def hexagon_area(a):
    """
    Finds the area of a regular hexagon given the side length
    """
    return 1.5 * sqrt(3) * a ** 2

def pentagon_area(a):
    """
    Finds the area of a regular pentagon given the side length
    """
    return a**2* sqrt(5*(5+2*sqrt(5)))/4

def herons_formula(a, b, c):
    """
    Finds the area of any triangle when given three valid sides
    """
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))

def ptolemys_theorem(a, b, c, d, p, q):
    """
    Checks if the quadrilateral is cyclic using Ptolemy's Theorem
    """
    return (a * c + b * d) == (p * q)

##Coordinate geometry

def point_distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points (x1, y1) and (x2, y2)
    """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def midpoint(x1, y1, x2, y2):
    """
    Calculates the midpoint of a segment with endpoints (x1, y1) and (x2, y2)
    """
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def equation_of_circle(h, k, r):
    """
    Returns the equation of a circle in standard form - (x - h)^2 + (y - k)^2 = r^2
    """
    return f"(x - {h})^2 + (y - {k})^2 = {r**2}"

def intersection_of_lines(m1, c1, m2, c2):
    """
    Calculates the intersection point of two lines given by y = m1*x + c1 and y = m2*x + c2
    """
    if m1 == m2:
        return None  
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1
    return (x, y)

def equation_of_ellipse(h, k, a, b):
    """
    Returns the equation of an ellipse in the form ((x - h)^2 / a^2) + ((y - k)^2 / b^2) = 1
    """
    return f"((x - {h})^2 / {a**2}) + ((y - {k})^2 / {b**2}) = 1"

def equation_of_parabola(vertex_x, vertex_y, focus_x, focus_y):
    """
    Returns the equation of a parabola given its vertex and focus
    """
    if vertex_x == focus_x:
        p = focus_y - vertex_y
        return f"(x - {vertex_x})^2 = 4 * {p} * (y - {vertex_y})"
    else:
        p = focus_x - vertex_x
        return f"(y - {vertex_y})^2 = 4 * {p} * (x - {vertex_x})"
    
def equation_of_parabola_given_points(x1, y1, x2, y2, x3, y3):
    """
    Returns the equation of a parabola given three points on the parabola
    """
    vertex_x, vertex_y, focus_x, focus_y = 0
    return equation_of_parabola(vertex_x, vertex_y, focus_x, focus_y)



def polygon_area(vertices):
    """
    Calculates the area of a polygon given its vertices
    """
    pass

def circumcenter(x1, y1, x2, y2, x3, y3):
    """
    Calculates the coordinates of the circumcenter of a triangle given its vertices
    """
    pass

def incenter(x1, y1, x2, y2, x3, y3):
    """
    Calculates the coordinates of the incenter of a triangle given its vertices
    """
    pass

def orthocenter(x1, y1, x2, y2, x3, y3):
    """
    Calculates the coordinates of the orthocenter of a triangle given its vertices
    """
    pass

def centroid(x1, y1, x2, y2, x3, y3):
    """
    Calculates the coordinates of the centroid of a triangle given its vertices
    """
    pass

def nine_point_center(x1, y1, x2, y2, x3, y3):
    """
    Calculates the coordinates of the nine point center of a triangle given its vertices
    """
    pass

def nagel_point():
    """
    Calculates the coordinates of the Nagel point of a triangle given its vertices
    """
    pass

def spieker_center():
    """
    Calculates the coordinates of the Spieker center of a triangle given its vertices
    """
    pass

def symmedian_point():
    """
    Calculates the coordinates of the symmedian point of a triangle given its vertices
    """
    pass

def harmonic_conjugate():
    pass


def balancing_point_triangle():
    pass

"""
END OF OF GEOMETRY
"""
