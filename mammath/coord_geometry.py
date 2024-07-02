from .constants import pi, e
from .operations import sqrt, ln
from .trig_functions import sin, cos, tan
from .linalg import mat_solve
from typing import overload, Union, Tuple

"""
COORDINATE GEOMETRY
"""

class Polygon:
    def __init__(self, *vertices):
        self.vertices = list(vertices)

def rotate_about_origin(x, y, theta) -> tuple[float, float]:
    """
    Returns the coordinates of the rotation of a given point (x, y) clockwise about the origin by an angle of theta
    """
    return x*cos(theta)+y*sin(theta), -x*sin(theta) + y*cos(theta)

def rotate_about_point(x, y, p, q, theta) -> tuple[float, float]:
    """
    Returns the coordinates of the rotation of a given point (x, y) clockwise about a point (p, q) by an angle of theta
    """
    return (x-p)*cos(theta)-(y-q)*sin(theta)+p, -(x-p)*sin(theta)+(y-q)*cos(theta)+q
    
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

def are_points_collinear(*points: tuple[tuple[float, float]]) -> bool:
    """
    Determines whether all of the given points are collinear
    """
    points = list(points)
    if len(points) <= 2:
        return True
    (x0, y0), (x1, y1) = points[0], points[1]
    dx, dy = x1 - x0, y1 - y0

    for (x, y) in points[2:]:
        if (y - y0)*dx != (x - x0)*dy:
            return False
    return True

def line_from_points(*points: tuple[tuple[float, float], tuple[float, float]]) -> tuple[float, float]:
    """
    Returns the slope and intercept of the line formed by the two given points
    """
    (x1, y1), (x2, y2) = points
    if x1 == x2:
        return float('inf'), x1 
    m = (y2-y1)/(x2-x1)
    c = y1 - m*x1
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
    return midpoint(orthocenter(x1, y1, x2, y2, x3, y3), circumcenter(x1, y1, x2, y2, x3, y3))

def spieker_center(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Calculates the coordinates of the Spieker center (incenter of the medial triangle) of a triangle given its vertices
    """
    return incenter(midpoint(x1, y1, x2, y2), midpoint(x2, y2, x3, y3), midpoint(x3, y3, x1, y1))

def balancing_point_triangle(x1, y1, x2, y2, x3, y3) -> tuple[float, float]:
    """
    Computes the coordinates of the balancing point of a triangle (centroid) given its vertices
    """
    return centroid(x1, y1, x2, y2, x3, y3)

def shoelace(coords):
    '''
    Returns the area of simple polygons based on coordinates
    '''
    coords += [coords[0]]
    a = [coords[i][0] * coords[i + 1][1] for i in range(len(coords) - 1)]
    b = [coords[i][1] * coords[i + 1][0] for i in range(len(coords) - 1)]
    return 0.5 * abs(sum(a) - sum(b))
    
"""
END OF COORDINATE GEOMETRY
"""
