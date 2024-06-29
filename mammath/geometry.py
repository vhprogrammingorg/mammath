from .constants import pi, e
from .operations import sqrt, ln
from .trig_functions import sin, cos, tan
from .linalg import mat_solve
import typing

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

def is_valid_triangle(s1, s2, s3):
    """
    If a triangle with three given sides is valid
    """
    if s1 + s2 >= s3 and s2 + s3 >= s1 and s1 + s3 >= s2:
        return True
    return False

def triangle_area(b, h):
    """
    Area of a triangle from base and vertical height
    """
    return (b*h)/2

def trapezium_area(a, b, h):
    """
    Area of a trapezium from two parallel sides and vertical height
    """
    return (a+b)/h

def parallelogram_area(b, h):
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

def sphere_diameter(r):
    """
    Diameter of a sphere with radius
    """
    return 2*r

def cuboid_area(a, b, c):
    """
    Surface area of a cuboid with three side lengths
    """
    d = a*b
    e = a*c
    f = b*c
    return 2*(d+e+f)

def prism_area(farea, *args):
    """
    Surface area of a prism with frontal area and length
    """
    total = 2*farea
    i = 0
    while i < len(args):
        total += args[i]
        i += 1
    return total

def cuboid_volume(a, b, c):
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

def cylinder_diameter(v, h):
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

def cos_rule(a, b, C):
    """
    Finds the third side of a triangle given two sides and the angle between them
    """
    return a**2 + b**2 - 2*a*b*cos(C)

def polygon_area_nxn(n, s):
    """
    Computes the area of a regular n-sided polygon with lengths s
    """
    return round((n*s**2)/(4*tan(pi/n)), 6)

def pythagorean_triplets_printer(n):
    """
    Prints pythagorean triplets until n
    """
    for b in range(n):
        for a in range(1, b):
            c = sqrt(a * a + b * b)
            if c % 1 == 0:
                print(a, b, int(c))
            
def is_pythagorean_triplet(a, b, c):
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


"""Coordinate geometry"""

class Polygon:
    def __init__(self, *vertices):
        self.vertices = list(vertices)
    
def equation_of_circle(h, k, r) -> str:
    """
    Returns the equation of a circle in standard form - (x - h)^2 + (y - k)^2 = r^2
    """
    return f"(x - {h})^2 + (y - {k})^2 = {r**2}"

def equation_of_ellipse(h, k, a, b) -> str:
    """
    Returns the equation of an ellipse in the form ((x - h)^2 / a^2) + ((y - k)^2 / b^2) = 1
    """
    return f"((x - {h})^2 / {a**2}) + ((y - {k})^2 / {b**2}) = 1"

def point_distance(x1, y1, x2, y2) -> float:
    """
    Calculates the distance between two points (x1, y1) and (x2, y2)
    """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def line_from_points(*points: list[tuple]) -> tuple[float, float]:
    x2, y2 = points[1]
    x1, y1 = points[0]
    m = (y2-y1)/(x2-x1)
    c = y1-m*x1
    return m, c

def midpoint(x1, y1, x2, y2) -> tuple[float, float]:
    """
    Calculates the midpoint of a segment with endpoints (x1, y1) and (x2, y2)
    """
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def perpendicular_from_point(x, y, m, c) -> tuple[float, float]:
    """
    Returns the equation of a line perpendicular to a given line defined by y=mx+c, at a given point, (x, y)

    Args:
        x (float): x and y coordinates of point
        m (float): slope of line
        c (float): y-intercept of line 
    """
    m_perp = -1/m
    c = y+m_perp*x
    return m_perp, c

def perpendicular_bisector(x1, y1, x2, y2) -> tuple[float, float]:
    """
    Returns the slope and intercept of the perpendicular bisector of a segment with endpoints (x1, y1) and (x2, y2)
    """
    midpoint = midpoint(x1, y1, x2, y2)
    m, c = line_from_points(x1, y1, x2, y2)
    return perpendicular_from_point(m, c, *midpoint)

def angle_bisector(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Returns the slope and intercept of the angle bisector of the angle formed at (x2, y2) by the lines (x1, y1)-(x2, y2) and (x2, y2)-(x3, y3).

    Args:
        x1, y1 (float): x and y coordinates of the first point.
        x2, y2 (float): x and y coordinates of the vertex where the angle is formed.
        x3, y3 (float): x and y coordinates of the third point.
    """
    side1 = point_distance(x1, y1, x2, y2)
    side2 = point_distance(x3, y3, x2, y2)
    side3 = point_distance(x1, y1, x3, y3)
    ratio = side3/(side1+side2)
    m_opp, c_opp = line_from_points(x1, y1, x3, y3)
    x_ab, y_ab = ratio * side1, m_opp*ratio*side1+c_opp
    return line_from_points(x2, y2, x_ab, y_ab)

def median(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Returns the slope and intercept of the median from the vertex (x2, y2) in the triangle with all three vertices
    """
    return line_from_points((x2, y2), midpoint(x1, y1, x3, y3))

def intersection_of_lines(m1, c1, m2, c2):
    """
    Calculates the intersection point of two lines given by y = m1*x + c1 and y = m2*x + c2
    """
    if m1 == m2:
        return None 
    if m1 == float('inf'):
        x = c1
        y = m2*x + c2
    elif m2 == float('inf'):
        x = c2
        y = m1*x + c1
    else:
        x = (c2 - c1)/(m1 - m2)
        y = m1*x + c1
    return x, y

def reflect_point_in_line(x, y, m, c) -> tuple[float, float]:
    """
    Args:
        x, y (float): x and y coordinates of point
        m (float): slope of line
        c (float): y-intercept of line 
    """
    x_i, y_i = perpendicular_from_point(x, y, m, c)
    return 2*x_i-x, 2*y_i-y

def reflect_segment_in_line(x1, y1, x2, y2, m, c) -> list[tuple[float, float], tuple[float, float]]:
    """
    Args:
        x (float): x and y coordinates of point
        m (float): slope of line
        c (float): y-intercept of line 
    """
    return [reflect_point_in_line(x1, y1, m, c), reflect_point_in_line(x2, y2, m, c)]

def equation_of_parabola(vertex_x, vertex_y, focus_x, focus_y) -> str:
    """
    Returns the equation of a parabola given its vertex and focus
    """
    if vertex_x == focus_x:
        p = focus_y - vertex_y
        return f"(x - {vertex_x})^2 = 4 * {p} * (y - {vertex_y})"
    else:
        p = focus_x - vertex_x
        return f"(y - {vertex_y})^2 = 4 * {p} * (x - {vertex_x})"
    
def parabola_given_points(x1, y1, x2, y2, x3, y3) -> tuple[float, float, float, float]:
    """
    Computes the focus and vertex of a parabola given three points on the parabola
    """
    A = [
        [x1**2, x1, 1],
        [x2**2, x2, 1],
        [x3**2, x3, 1]
    ]
    B = [y1, y2, y3]
    a, b, c = mat_solve(A, B)

    h = -b/(2*a)
    k = a*h**2 + b*h + c
    focus_x = h
    focus_y = k + 1/(4*a)

    return h, k, focus_x, focus_y

def equation_of_parabola_given_points(x1, y1, x2, y2, x3, y3) -> str:
    """
    Returns the equation of a parabola given three points on the parabola
    """
    return equation_of_parabola(parabola_given_points(x1, y1, x2, y2, x3, y3))

def polygon_area(vertices: list[tuple]):
    """
    Calculates the area of a polygon given its vertices using the Shoelace Theorem
    """
    area = 0
    n = len(vertices)
    for i in range(0, n):
        xi, yi = vertices[i]
        if i == n-1:
            xi2, yi2 = vertices[0]
        else:
            xi2, yi2 = vertices[i+1]
        area += (xi2+xi)*(yi2-yi)
    return abs(area)/2
    
def circumcenter(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Calculates the coordinates of the circumcenter of a triangle given its vertices
    """
    m1_perp_bis, c1_perp_bis = perpendicular_bisector(x1, y1, x2, y2)
    m2_perp_bis, c2_perp_bis = perpendicular_bisector(x2, y2, x3, y3)
    return intersection_of_lines(m1_perp_bis, c1_perp_bis, m2_perp_bis, c2_perp_bis)
    
def incenter(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Calculates the coordinates of the incenter of a triangle given its vertices
    """
    m1_angle_bis, c1_angle_bis = angle_bisector(x1, y1, x2, y2, x3, y3)
    m2_angle_bis, c2_angle_bis = angle_bisector(x2, y2, x3, y3, x1, y2)
    return intersection_of_lines(m1_angle_bis, c1_angle_bis, m2_angle_bis, c2_angle_bis)

def orthocenter(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Calculates the coordinates of the orthocenter of a triangle given its vertices
    """
    m1_altitude, c1_altitude = perpendicular_from_point(line_from_points(x2, y2, x3, y3), x1, y1)
    m2_altitude, c2_altitude = perpendicular_from_point(line_from_points(x1, y1, x2, y2), x3, y3)
    return intersection_of_lines(m1_altitude, c1_altitude, m2_altitude, c2_altitude)

def centroid(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Calculates the coordinates of the centroid of a triangle given its vertices
    """
    m1_median, c1_median = median(x1, y1, x2, y2, x3, y3)
    m2_median, c2_median = median(x2, y2, x3, y3, x1, y1)
    return intersection_of_lines(m1_median, c1_median, m2_median, c2_median)

def symmedian_point(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Calculates the coordinates of the symmedian point of a triangle given its vertices
    This is the intersection of the three symmedians (medians reflected in the angle bisectors) of the triangle
    """
    m1_symmedian, c1_symmedian = reflect_segment_in_line(x1, y1, midpoint(x2, y2, x3, y3), angle_bisector(x2, y2, x1, y1, x3, y3))
    m2_symmedian, c2_symmedian = reflect_segment_in_line(x2, y2, midpoint(x1, y1, x3, y3), angle_bisector(x1, y1, x2, y2, x3, y3))
    return intersection_of_lines(m1_symmedian, c1_symmedian, m2_symmedian, c2_symmedian)

def nine_point_center(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Calculates the coordinates of the nine point center of a triangle given its vertices
    """
    pass

def nagel_point(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Calculates the coordinates of the Nagel point of a triangle given its vertices
    """
    pass

def spieker_center(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Calculates the coordinates of the Spieker center of a triangle given its vertices
    """
    pass

def harmonic_conjugate():
    pass

def balancing_point_triangle(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Computes the coordinates of the balancing point of a triangle (centroid) given its vertices
    """
    return centroid(x1, y1, x2, y2, x3, y3)

"""
END OF OF GEOMETRY
"""
