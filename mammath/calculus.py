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

def partial_derivative(function, inputs, var_idx, h = 0.0001):
    """
    Partial derivative with respect to the variable whose index is specified.
    """
    fi = function(*inputs)
    inputs[var_idx] += h
    return round((function(*inputs) - fi) / h, 7)

def del_operator(function, inputs, h = 0.0001):
    """
    The vector at the location of the inputs.
    """
    vec = []
    for i in range(len(inputs)):
        vec.append(partial_derivative(function, inputs, i, h = h))
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

def tangent_plane(function, x, y, h = 0.001, partial = partial_derivative):
    """
    Tangent plane to a function at point x, y
    """
    return lambda X, Y: partial(function, [x, y], 0, h = h) * (X - x) + partial(function, [x, y], 1, h = h)) * (Y - y) + function(x, y)

def nth_derivative(n, function, x, h = 0.0001, derivative = point_derivative):
    """
    Finds the nth derivative at a point for a given function
    """
    if n < 1:
        raise ValueError
    if n == 1:
        return derivative(function, x, h = h)
    return nth_derivative(n - 1, lambda X: derivative(function, X, h = h))

def taylor_approx(function, x, terms, h = 0.001):
    """
    Numerical Taylor series approximation accurate at x.
    """
    return lambda X: sum([(1 / factorial(i)) * nth_derivative(i, function, x, h = h) * (X - x) ** i for i in range(1, terms + 1)]) + function(x)
   
def taylor_coefficients(function, x, terms, h = 0.001, with_factorial = True):
    """
    Numerical Taylor series coefficients. Choose to ignore factorial for speed.
    """
    if with_factorial:
        return [(1 / factorial(i)) * nth_derivative(i, function, x, h = h) for i in range(1, terms + 1)]
    return [nth_derivative(i, function, x, h = h) for i in range(1, terms + 1)]

def maclaurin_approx(function, terms, h = 0.001, taylor_alg = taylor_approx):
    """
    Numerical Maclaurin series approximation for accuracy analysis.
    """
    return taylor_alg(function, 0, terms, h = h)

def maclaurin_coefficients(function, terms, h = 0.001, with_factorial = True, taylor_alg = taylor_coefficients):
    """
    Numerical Taylor series coefficients. Choose to ignore factorial for speed.
    """
    return taylor_alg(function, x, terms, h = h, with_factorial = with_factorial)

def divergence(functions, inputs, h = 0.001, partial = partial_derivative):
    """
    The divergence of the vector field composed of many functions and a set of coordinates
    """
    s = 0
    for i in range(len(inputs)):
        s += parital(i, inputs, functions[i], h = h)
    return s

def curl(functions, inputs, h = 0.001, partial = partial_derivative):
    """
    The curl of the vector field composed of many functions and a set of coordinates
    """
    curl_matrix = [[0] * inputs for _ in range(inputs)]
    for i in range(inputs):
        for j in range(i + 1, inputs):
            partial_i = lambda *args: partial(i, args, functions[j])
            partial_j = lambda *args: partial(j, args, functions[i])
            curl_matrix[i][j] = partial_i(*[0]*inputs) - partial_j(*[0]*inputs)
            curl_matrix[j][i] = -curl_matrix[i][j]
    return curl_matrix

def curl(functions, inputs, h = 0.001):
    """
    Computes the curl of an n-dimensional vector field composed of many functions
    and a set of coordinates.
    """
    n = len(functions)
    curl_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            partial_i = partial_derivative(functions[j], inputs, i, h = h)
            partial_j = partial_derivative(functions[i], inputs, j, h = h)
            curl_matrix[i][j] = partial_i - partial_j
            curl_matrix[j][i] = -curl_matrix[i][j]
    
    return curl_matrix

def curl_3d(vector_field, point, h = 0.0001):
    """
    Computes the curl of a 3-dimensional vector field at a given point.
    """
    F1, F2, F3 = vector_field
    x, y, z = point

    dF3_dy = partial(F3, [x, y, z], 1, h)
    dF2_dz = partial(F2, [x, y, z], 2, h)
    
    dF1_dz = partial(F1, [x, y, z], 2, h)
    dF3_dx = partial(F3, [x, y, z], 0, h)
    
    dF2_dx = partial(F2, [x, y, z], 0, h)
    dF1_dy = (F1, [x, y, z], 1, h)

    curl_x = dF3_dy - dF2_dz
    curl_y = dF1_dz - dF3_dx
    curl_z = dF2_dx - dF1_dy

    return [curl_x, curl_y, curl_z]

def f_derivative(f_of, h = 0.00001):
    """
    The function for the derivative of f(x)
    """
    return lambda x: point_derivative(f_of, x, h = h)

def f_partial_derivative(function, var_idx, h = 0.0001):
    """
    The function for the partial derivative of any function
    """
    return lambda *args: partial_derivative(function, args, var_idx, h = h)

def f_del_operator(function, h = 0.0001):
    """
    The function for the del operator of any function
    """
    return lambda *args: (function, args, h = h)

def f_directional_derivative(vec, inputs, function, h = h):
    """
    The function for the directional derivative of any function
    """
    return lambda *args: directional_derivative(vec, args, function, h = 0.0001)

def f_nth_derivative(n, function, h = 0.0001, derivative = point_derivative):
    """
    The function for the nth derivative of f(x)
    """
    return lambda x: nth_derivative(n, function, x, h = h, derivative = derivative)

def f_divergence(functions, h = 0.001, partial = partial_derivative):
    """
    The function for the divergence of any function
    """
    return lambda *args: divergence(functions, args, h = h, partial = partial)

def f_curl(functions, h = h):
    """
    The function for the curl of any function
    """
    return lambda *args: curl(functions, args, h = h)

def f_curl_3d(vector_field, h = 0.0001):
    """
    The function for the curl of f(x, y)
    """
    return lambda *args: curl_3d(vector_field, point, h = h)

"""
END OF CALCULUS
"""
