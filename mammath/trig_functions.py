from .constants import e
from .operations import ln
import math

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

def sin(theta, radians=False):
    """
    Computes the value of sin(theta)
    """
    return rad_to_deg(math.sin((theta))) if radians else math.sin((theta))

def cos(theta, radians=False):
    """
    Computes the value of cos(theta)
    """
    return rad_to_deg(math.cos((theta))) if radians else math.cos((theta))
    
def tan(theta, radians=False):
    """
    Computes the value of tan(theta)
    """
    return rad_to_deg(math.tan((theta))) if radians else math.tan((theta))
    
def csc(theta, radians=False):
    """
    Computes the value of cosecant(theta)
    """
    return rad_to_deg(1/math.sin(theta)) if radians else 1/math.sin((theta))

def sec(theta, radians=False):
    """
    Computes the value of secant(theta)
    """
    return rad_to_deg(1/math.cos((theta))) if radians else 1/math.cos((theta))
    
def cot(theta, radians=False):
    """
    Computes the value of cotangent(theta)
    """
    return rad_to_deg(1/math.atan((theta))) if radians else 1/math.atan((theta))
	
def acsc(n, radians=False):
    """
    Computes the value of arccosecant(n)
    """
    return rad_to_deg(math.asin(1/n)) if radians else math.asin(1/n)

def asec(n, radians=False):
    """
    Computes the value of arcsecant(n)
    """
    return rad_to_deg(math.acos(1/n)) if radians else math.acos(1/n)
	
def acot(n, radians=False):
    """
    Computes the value of arccotangent(n)
    """
    return rad_to_deg(math.atan(1/n)) if radians else math.atan(1/n)
	
def asin(n, radians=False):
    """
    Computes the value of arcsin(n)
    """
    return rad_to_deg(math.asin(n)) if radians else math.asin(n)

def acos(n, radians=False):
    """
    Computes the value of arccos(n)
    """
    return rad_to_deg(math.acos(n)) if radians else math.acos(n)
	
def atan(n, radians=False):
    """
    Computes the value of arctan(n)
    """
    return rad_to_deg(math.atan(n)) if radians else math.atan(n)

def sinh(theta):
    """
    The hyperbolic sine of theta.
    """
    return (e ** theta - e ** -theta)/2

def asinh(x):
    """
    Inverse hyperbolic sine of x.
    """
    return ln(x + (x ** 2 + 1) ** (1/2))

def cosh(theta):
    """
    The hyperbolic cosine of theta.
    """
    return (e ** theta + e ** -theta)/2

def acosh(x):
    """
    Inverse hyperbolic cosine of x.
    """
    return ln(x + (x ** 2 - 1) ** (1/2))

def tanh(theta):
    """
    The hyperbolic tangent of theta.
    """
    return sinh(theta)/cosh(theta)

def atanh(x):
    """
    Inverse hyperbolic tangent of x.
    """
    return 0.5 * ln((1 + x)/(1 - x))

def csch(theta):
    """
    The hyperbolic cosecant of theta.
    """
    return 1/sinh(theta)

def acsch(x):
    """
    Inverse hyperbolic cosecant of x.
    """
    return asinh(1/x)

def sech(theta):
    """
    The hyperbolic secant of theta.
    """
    return 1/cosh(theta)

def asech(x):
    """
    Inverse hyperbolic secant of x.
    """
    return acosh(1/x)

def coth(theta):
    """
    The hyperbolic cotangent of theta
    """
    return 1/tanh(theta)

def acoth(x):
    """
    Inverse hyperbolic cotangent of x.
    """
    return atanh(1/x)
