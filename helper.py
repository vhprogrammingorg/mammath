import numpy as np

"""
HELPER FUNCTIONS
"""

def f(fx, x, y):
    if type(eval(fx)) == np.ndarray:
        return eval(fx)

def preprocess_equation(eq):
    """
    Helper function for adding the appropriate coefficients to equations 
    """
    eq = eq.replace(" ", "")
    eq = eq.replace("+x", "+1x").replace("+y", "+1y")
    eq = eq.replace("-x", "-1x").replace("-y", "-1y")
    if eq[0] == "x" or eq[0] == "y":
        eq = "1" + eq
    return eq

def parse_equation(eq):
    """
    Parses a linear equation in the form of ax+by=c into its coefficients and product 
    """
    equation = preprocess_equation(eq)
    equation = equation.replace("x", " ").replace("y", " ").replace("=", " ").replace("+", "").split()
    coefficients = list(map(float, equation[:2]))
    product = float(equation[2])

    return coefficients, product

def standard_form_float(n):
    """
    Converts a standard for tuple of type (a, b) = a * 10 ** b to a float
    """
    return n[0] * 10 ** n[1]

def parse_standard(sf):
    """
    Converts a standard form equation in the form of n*10^m into a tuple of (n, m)
    """
    sf = sf.replace(" ", "").split("*")
    sf[-1] = sf[-1][3:]
    return tuple(map(float, sf))

def parse_to_standard(tup):
    """
    Converts a tuple in the form of (n, m) into standard form in the form of n * 10^m
    """
    return f"{tup[0]} * 10^{tup[1]}"

def remove_decimal(num):
    """
    Removes the .0 from a floating point number
    """
    if(num == int(num)):
        return int(num)
    return num

"""
END OF HELPER FUNCTIONS
"""

