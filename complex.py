from operations import *
from geometry import *

"""
COMPLEX
"""

def negative_ln(num, show_general = False):
    """
    Returns the natural log of a negative number
    """
    if num > 0:
        return "Please enter a number < 0"
    
    if show_general:
        principle = str(ln(-num)) + ' + iπ'
        general = str(ln(-num)) + 'iπ(2n+1) n ∊ ℤ'
        print(f"Principal Value: {principle}")
        print(f"General: {general}")
        
    return complex(ln(-num), pi)

def negative_log(base, argument, show_general = False):
    argument_ln = negative_ln(argument)
    base_ln = negative_ln(base)
    principle_value = (argument_ln.real / base_ln.real)

    if show_general == True:
        print(f"(ln({-argument}) + iπ(2n+1))/(ln({-base}) + iπ(2m+1))")
        
    return principle_value
    

def complex_ln(a, b, show_general = True):
    """
    Returns the natural log of a complex number
    """        
    return ln(a) * complex(ln(b), pi)

def root_i(n):
    root = n
    """
    Returns the nth root of i
    """
    solutions= []
    for x in range(0, root):
        cos_theta = round(cos((pi/(2*root))+((2*x*pi)/root)), 6)
        i_sin_theta = 1j * round(sin((pi/(2*root))+((2*x*pi)/root)), 6)
        solutions.append(cos_theta + i_sin_theta)
    return solutions

def power_i(p):
    solutions = []
    """
    Returns i to the power of p
    """
    for x in range(0, round(p)):
        cos_theta = round(cos((pi/2)*p+((2*x*pi)*p)), 6)
        i_sin_theta = 1j * round(sin((pi/2)*p+((2*x*pi)*p)), 6)
        solutions.append(cos_theta + i_sin_theta)
    return solutions
    


"""
END OF COMPLEX
"""
