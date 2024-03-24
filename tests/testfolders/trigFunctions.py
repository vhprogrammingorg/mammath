import math

def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def asin(a):
    return math.asin(a)
def acos(a):
    return math.acos(a)
def atan(a):
    return math.atan(a)
def sinh(a):
    return math.sinh(a)
def cosh(a):
    return math.cosh(a)
def tanh(a):
    return math.tanh(a)
def asinh(a):
    return math.asinh(a)
def acosh(a):
    return math.acosh(a)
def atanh(a):
    return math.atanh(a)
def sec(a):
    return round(1/cos(a), 5)
def csc(a):
    return round(1/sin(a), 5)
def cot(a):
    return round(1/tan(a), 5)

def pytheoromside(a, b):
    if a > c:
        a1 = a*ad
        b1 = b*b
        c1 = a1 - b1
        c = math.sqrt(c1)
    else:
        a1 = a*a
        b1 = b*b
        c1 = b1 - a1
        c = math.sqrt(c1)
    return c
def pyTheoremAB(a, b):
    a1 = a*a
    b1 = b*b
    c1 = a1 + b1
    c = math.sqrt(c1)
    return c
def pyTheoremCA(c, a):
    c1 = c*c
    a1 = a*a
    b1 = c1 - a1
    b = math.sqrt(b1)
    return b
def pyTheoremCB(c, b):
    c1 = c*c
    b1 = a*a
    a1 = c1 - b1
    a = math.sqrt(a1)
    return a
def cos_rule(c, b, A):
    c1 *= c
    b1 *= b
    A1 = math.cos(A)
    thing = A1*c*b
    ans = b1 + a1 - thing
    answer = math.sqrt(answer)
    return answer
def areabytan(n, s):
    s1 = s*s
    up = n*s1
    intan = 180/n
    tanpart = math.tan(intan)
    down = 4*tanpart
    ans = up/down
    return ans
