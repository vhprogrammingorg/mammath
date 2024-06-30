from .geometry import *
from .constants import e, pi, i
from .operations import *
from .calculus import trapezoidal_rule
import math

"""
COMPLEX
"""

def exp(x):
    return e**x

def eulers_formula(theta):
    return math.cos(theta) + 1j * math.sin(theta)

def stacked_power(x, a, b):
    """
    Gives the proper solutions for (x**a)**b using the improved formula
    """
    n = 0
    t = x ** (a*b)
    sols = []
    while True:
        sol = t * (round(cos(2*n*b*pi), 6) + i*round(sin(2*n*b*pi), 6))
        if sol in sols:
            return sols
        sols.append(sol)
        n += 1
        
def negative_ln(num, show_general = False):
    """
    Returns the natural log of a negative number
    """
    if num > 0:
        return ln(num)
    if show_general:
        principle = str(ln(-num)) + ' + iπ'
        general = str(ln(-num)) + '+ iπ(2n+1) n ∊ ℤ'
        print(f"Principal Value: {principle}")
        print(f"General: {general}")
        
    return complex(ln(-num), pi)

def negative_log(base, argument, show_general = False):
    
    argument_ln = complex(negative_ln(argument))
    base_ln = complex(negative_ln(base))
    principle_value = (argument_ln.real / base_ln.real)

    if show_general == True:
        print(f"(ln({-argument}) + iπ(2n+1))/(ln({-base}) + iπ(2m+1)) \n m ∊ ℤ")
        
    return principle_value
    

def complex_ln(a, b, n = 0, show_general = False):
    """
    Returns the natural log of a complex number given by the formula ln(r)+i*theta
    """
    #ln(a+bi) =
    #ln(r) + i*theta
    r = math.sqrt(a**2 + b**2)
    theta = math.atan2(b,a)
        
    if show_general == False:
        return math.log(r) + 1j*(theta+2*pi*n)
    else:
        if n:
            print(f"ln({r})+({theta}+2πn)i \nn ∊ ℤ")
            return math.log(r) + 1j*(theta+2*pi*n)
        else:
            print(f"ln({r})+({theta}+2πn)i \nn ∊ ℤ")
    
def root_i(n):
    root = n
    """
    Returns the nth root of i

    Uses Euler's formula to get cos(π/2n) + isin(2mπ/n) where n is the root and m are values to be substituted from 0...n-1 to get all distinct solutions
    """
    solutions= []
    for x in range(0, root):
        cos_theta = round(cos((pi/(2*root))+((2*x*pi)/root)), 6)
        i_sin_theta = 1j * round(sin((pi/(2*root))+((2*x*pi)/root)), 6)
        solutions.append(cos_theta + i_sin_theta)
    return solutions

def power_i(p):
    """
    Returns the principle value of i to the power of p
    """
    if isinstance(p, int) == False:
        pass
    cos_theta = round(cos((pi/2)*p), 6)
    i_sin_theta = 1j * round(sin((pi/2)*p), 6)
    principle_value = (cos_theta + i_sin_theta)
    return principle_value

def real_complex_power(a, c, d):
    """
    Returns a^(c+di) where a ∊ ℤ and c+di is the standard form of a complex number
    """
    return a ** c * e ** (1j * d * ln(a))

def complex_power(a, b, c, d):
    """
    Returns (a+bi)^(c+di)
    """
    r = sqrt(a**2+b**2)
    arg = math.atan2(b, a)
    theta = c*arg + d*ln(r)
    return r**c*e**(-d*arg)*(eulers_formula(theta))

def root_complex(n, a, b):
    """
    Returns the nth root of a complex number where n is an real number
    """
    r = sqrt(a**2+b**2)
    theta = math.atan2(b, a)
    return r**(1/n)*eulers_formula(theta/n)

def complex_sin(z):
    """
    Returns the sine of a complex number z using the complex definition of sine derived from Euler's formula
    """
    i = complex(0, 1)
    return (exp(1 * z) - exp(-i * z))/(2*i)

def complex_cos(z):
    """
    Returns the cosine of a complex number z using the complex definition of sine derived from Euler's formula
    """
    i = complex(0, 1)
    return (exp(1 * z) + exp(-i * z))/2

def complex_tan(z):
    """
    Returns the sine of a complex number z using the complex definition of sine derived from Euler's formula
    """
    return complex_sin(z)/complex_cos(z)

def complex_sinh(z):
    """
    Returns the hyperbolic sine of a complex number z.
    """
    return (math.e**z - math.e**(-z)) / 2

def complex_cosh(z):
    """
    Returns the hyperbolic cosine of a complex number z.
    """
    return (math.e**z + math.e**(-z)) / 2

def complex_tanh(z):
    """
    Returns the hyperbolic tangent of a complex number z.
    """
    return complex_sinh(z) / complex_cosh(z)

def complex_asinh(z):
    """
    Returns the inverse hyperbolic sine of a complex number z.
    """
    return math.log(z + math.sqrt(z**2 + 1))

def complex_acosh(z):
    """
    Returns the inverse hyperbolic cosine of a complex number z.
    """
    return math.log(z + math.sqrt(z**2 - 1))

def complex_atanh(z):
    """
    Returns the inverse hyperbolic tangent of a complex number z.
    """
    return 0.5 * math.log((1 + z) / (1 - z))

def roots_of_unity(n, r):
    """
    Returns all solutions for x ** n = r as the offset roots of unity.
    """
    return [r ** (1/n) * e ** (2 * i * pi * complex(0, 1)/n) for i in range(n)]
    
def W(x, n=100):
    """
    Calculates the the LambertW function of x. Larger n is more accurate.
    """
    ans = ln(x)
    for i in range(n):
        ans -= (ans * e ** ans - x)/((ans + 1) * e ** ans)
    return ans

lambertW = product_log = W

def gamma(x, n = 1000):
    """
    Computes gamma(x). Larger n yields greater accuracy
    """
    gamma_function = lambda t: t**(x-1) * math.e**(-t)
    return trapezoidal_rule(gamma_function, 0, n, n=n)

"""
END OF COMPLEX
"""
