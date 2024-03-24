import math

def triangleArea(l, w):
    return (l*w)/2
def trapeziumArea(a, b, h):
    return (a+b)/h
def paraHeight(a, b):
    return a/b
def paraArea(b, h):
    return b*h
def circleCircumference(r):
    return 2*math.pi*r
def circleArea(r):
    return math.pi*(r**2)
def sphereVolume(r):
    return 4/3*math.pi*(r**3)
def sphereArea(r):
    return 4*math.pi*(r**2)
def sphereDiametre(r):
    return 2*r
def surfaceArea(a, b, c):
    d = a*b
    e = a*c
    f = b*c
    return 2*(d+e+f)
def surfAreaPrism(farea, *args):
    total = 2*farea
    i = 0
    while i < len(args):
        total += args[i]
        i += 1
    return total
def volume(a, b, c):
    return a*b*c
def cylinderVolume(r, h):
    return (math.pi*(r**2))*h
def cylinderArea(r, h):
    return (2*math.pi*r*h)+(2*math.pi*(r**2))
def cylinderDiametre(v, h):
    return 2*(math.sqrt(v/math.pi*h))
def cylinderHeight(v, r):
    return v/(math.pi*(r**2))
def cylindeRadius(h, A):
    return round(0.5*math.sqrt(h**2 + 2*(A/math.pi))-h/2, 5)
def coneArea(r, h):
    pi = math.pi
    area = pi*r*(r + math.sqrt(h**2 + r**2))
    return round(area, 5)
def coneVolume(r, h):
    pi = math.pi
    vol = pi*r**2*(h/3)
    return round(vol, 5)
def coneRadius(h, vol):
    pi = math.pi
    rad = math.sqrt(3*(vol/(pi*h)))
    return round(rad, 5)
def coneHeight(r, vol):
    pi = math.pi
    height = 3*(vol/(pi*r**2))
    return round(height, 5)

def pythagoreanTriplets(n):
  for b in range(n):
    for a in range(1, b):
        c = math.sqrt( a * a + b * b)
        if c % 1 == 0:
            print(a, b, int(c))
def pythagoreanTripletsCheck(a, b, c):
    if (a ** 2) + (b ** 2) == (c ** 2):
        return True
    else:
        return False
