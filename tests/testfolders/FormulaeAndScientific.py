from tabulate import tabulate
import math

def Force(m, a):
    return m*a
def Mass(f, a):
    return f/a
def Acceleration(f, m):
    return f/m

def constSearch(con):
    G = 6.67384*10**(-11)
    c = 2.99792458*10**(8)
    h = 6.626070040*10**(-34)
    k = 1.38064852*10**(-23)
    F = 9.648533289*10**(4)
    pi = math.pi
    e = math.e
    π = pi
    phi = 1.618033988749894848204586
    tau = math.tau
    τ = tau
    φ = phi
    conlist = [G, c, h, k, F, pi, π, φ, phi, tau, τ, e]
    x = 0
    while x < 10:
        variable_name = [k for k, v in locals().items() if v == conlist[x]][0]
        if variable_name == con:
            constant = conlist[x]
            return constant
        x += 1
    return None
def constTable():
    G = 6.67384*10**(-11)
    c = 2.99792458*10**(8)
    h = 6.626070040*10**(-34)
    k = 1.38064852*10**(-23)
    F = 9.648533289*10**(4)
    pi = math.pi
    e = math.e
    π = pi
    phi = 1.618033988749894848204586
    tau = math.tau
    τ = tau
    φ = phi
    conlist = [["The gravitational constant", "G", G], ["The speed of light in vacuum", "c", c], ["Planck's constant", "h", h], ["Boltzmann's constant", "k", k], ["Faraday's constant", "F", F], ["e", "e", e], ["pi", "φ", π], ["tau", "τ", tau], ["Phi", "φ", φ]]
    headers = ["Name", "Symbol", "Value"]
    thing = tabulate(conlist, headers = headers)
    print(thing)
def speedCalc(d, t):
    return d/t
def distCalc(s, t):
    return s*t
def timeCalc(s, d):
    return s*d
    
