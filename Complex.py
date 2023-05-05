from operations import *
from geometry import *
from constants import e, pi, i
import cmath
import math

"""
COMPLEX
"""

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
    

def complex_ln(a, b, show_general = True):
    """
    Returns the natural log of a complex number
    """
    #ln(a+bi) =
    #ln(r) + i*theta
    r = sqrt(a**2+b**2)
    theta = math.atan2(b, a)
    i_theta = 1j * theta
    return ln(r) + i_theta
    

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
    return a**c * cmath.exp(1j * d * ln(a))

def complex_power(a, b, c, d):
    """
    Returns (a+bi)^(c+di)
    """
    r = sqrt(a**2+b**2)
    arg = math.atan2(b, a)
    theta = c*arg + d*ln(r)
    return r**c*e**(-d*arg)*(eulers_formula(theta))

def root_complex(n, a, b):
    r = sqrt(a**2+b**2)
    theta = math.atan2(b, a)
    return r**(1/n)*eulers_formula(theta/n)

def unit_complex_root_complex(a, b):
    r = sqrt(a**2+b**2)
    theta = math.atan2(b, a)
    ith_r = eulers_formula(-ln(r))
    return ith_r * e**theta

def complex_root_complex(a, b, c, d):
    pass

def complex_sin(a, b):
    return
    #sinx = (e^x + e^-x)/2
    #cosx = (e
    
"""
END OF COMPLEX
"""
