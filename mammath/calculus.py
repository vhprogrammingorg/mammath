from .constants import pi, e
from .operations import factorial

"""
CALCULUS
"""
def rsum(f, a, b, n = 1000):
    """
    Riemann sum of f(x) (a to b). Larger n is more accurate to the integral.
    """
    dx = (b - a)/n
    s = 0
    for i in range(n):
        s += dx * f(dx * i)
    return s

riemann_sum = rsum

def trapezoidal_rule(f, a, b, n = 100):
    """
    Trapezoidal approximation of f(x) (a to b). Larger n is more accurate to the integral.
    """
    x = f(a) + f(b)
    d = (b - a)/n
    for i in range(1, n):
        x += 2 * f(i * d + a)
    return x/2 * d

def disk_volume(f, a, b, n = 100, int_approx = trapezoidal_rule):
    """
    The volume of the figure formed by rotating f(x) around the x-axis (or f(y) around the y-axis). Larger n is more accurate.
    """
    return pi * int_approx(lambda x: f(x) ** 2, a, b, n = n)

def washer_volume(f, g, a, b, n = 100):
    """
    Calculates the volume between two functions. You may wish to verify points of intersection. Larger n is more accurate.
    """
    return disk_volume(f, a, b, n = n) - disk_volume(g, a, b, n = n)

def shell_volume(f, a, b, n = 100, g = lambda x: 0, R = lambda x: x, int_approx = trapezoidal_rule):
    """
    Calculates the volume between f(x) and g(x) from a to b given R(x). Larger n is more accurate.
    """
    return 2 * pi * int_approx(lambda x: (f(x) - g(x)) * R(x), a, b, n = n)

def point_derivative(f_of, x, h = 0.00001):
    """
    Returns the derivative of any function at a point x. Smaller h is more accurate.
    """
    return round(1 / (12 * h) * (f_of(x - 2 * h) - 8 * f_of(x - h) + 8 * f_of(x + h) - f_of(x + 2 * h)), 7)

def limit_derivative(f, x, h = 0.00001):
    """
    Returns the derivative of any function at a point x. Smaller h is more accurate.
    """
    return (f(x + h) - f(x))/h

def newton_approx(f, initial, n = 100, h = 0.00001, dydx = point_derivative):
    """
    Approximates the 0 of f(x) closest to the inital approximation. Smaller h, accurate.
    """
    for i in range(n):
        initial = initial - f(initial)/limit_derivative(f, initial, h = h)
    return initial

def limit(f, x, h=0.00001):
    """
    [BETA]
    Calculates the limit of a function f(x) as x approaches a given value. Smaller h is cen be more accurate.
    Not always accurate. Only for simple limits.
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def convergence_test(f, h = 0.00001):
    """
    [BETA]
    Tests the convergence of the sum of all terms of f(n). 
    Smaller h is can be more accurate.
    Not always accurate.
    """
    return limit(lambda x: f(x)/f(x + 1), x = float('inf'), h = h) < 1

def gamma(x, a = 0.001, b = 100, int_approx = trapezoidal_rule):
    """
    Computes the gamma function (factorial but offset) of x. a closer to 0 and larger b are more accurate.
    """
    gammaF = lambda t: t**(x - 1) * e ** -t
    return int_approx(gammaF, a, b)

def pi_function(x, a = 0.001, b = 100, int_approx = trapezoidal_rule):
    """
    Computes the pi (factorial, offset gamma) function of x. a closer to 0 and larger b are more accurate.
    """
    return gamma(x + 1, a = a, b = b, int_approx = int_approx)

def local_minima(f, a, b, h = 0.00001):
    """
    Finds the local minimum of a function f(x) from a to b. Smaller h is more accurate.
    """
    l = []
    x = a
    while x <= b:
        if f(x - h) > f(x) and f(x + h) > f(x):
            l.append(x)
        x += h
    return l

def local_maxima(f, a, b, h = 0.00001):
    """
    Finds the local maximum of a function f(x) from a to b. Smaller h is more accurate.
    """
    l = []
    x = a
    while x <= b:
        if f(x - h) < f(x) and f(x + h) < f(x):
            l.append(x)
        x += h
    return l

def partial_derivative(var_idx, inputs, function, h = 0.0001):
    """
    Partial derivative with respect to the variable whose index is specified.
    """
    fi = function(*inputs)
    inputs[var_idx] += h
    return (function(*inputs) - fi) / h

def del_operator(function, inputs, h = 0.0001):
    """
    The vector at the location of the inputs.
    """
    vec = []
    for i in range(len(inputs)):
        vec.append(partial_derivative(i, inputs, function, h = h))
    return vec

def directional_derivative(vec, inputs, function, h = 0.0001):
    """
    Dot product of the del operator with the corresponding unit vector.
    """
    mag = (vec[0] ** 2 + vec[1] ** 2) ** (1/2)
    vec = [i / mag for i in vec]
    delop = del_operator(function, inputs, h = h)
    new = list(zip(vec, delop))
    for i in range(len(new)):
        new[i] = new[i][0] * new[i][1]
    return new

def tangent_line(function, x, h = 0.001, derivative = point_derivative):
    """
    Tangent line to a function at point x
    """
    return lambda X: derivative(function, x, h = h) * (X - x) + function(x)

def tangent_plane(function, x, y, h = 0.001):
    """
    Tangent plane to a function at point x, y
    """
    return lambda X, Y: partial_derivative(0, [x, y], function, h = 0.0001) * (X - x) + partial_derivative(1, [x, y], function, h = 0.0001) * (Y - y) + function(x, y)

def nth_derivative(n, function, x, h = 0.0001, derivative = point_derivative):
    """
    Finds the nth derivative at a point for a given function
    """
    if n < 1:
        raise ValueError
    if n == 1:
        return derivative(function, x, h = h)
    return nth_derivative(n - 1, lambda X: derivative(function, X, h = h))

def taylor_approx(function, x, terms = 10, h = 0.001):
    """
    Numerical Taylor series approximation
    """
    return lambda X: sum([(1 / factorial(i)) * nth_derivative(i, function, x, h = h) * (X - x) for i in range(1, terms + 1)]) + function(x)

"""
END OF CALCULUS
"""
