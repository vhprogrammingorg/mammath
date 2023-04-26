from sympy import *
from sympy.abc import x, y, z
import tkinter
from tkinter import *
from tabulate import tabulate
import string
from fractions import Fraction
from tkinter import messagebox
import numpy as np
import math
import cmath
import random
import time
import sys
import keyboard
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import inspect
import re
import mpmath

# Mathematics
π = pi = 3.14159265359
ℯ = e = 2.71828182846
ϕ = phi = golden_ratio = 1.61803398875
𝑖 = i = imaginary_unit = complex(0, 1)
γ = euler_mascheroni = 0.5772156649
ζ_3 = apery = 1.2020569032
G = catalan = 0.9159655942
sqrt2 = 1.41421356237
sqrt3 = 1.73205080757
ln2 = log2 = 0.69314718056
ln10 = log10 = 2.30258509299
khinchin = 2.68545200107
twin_prime = 0.6601618158468696
conways_constant = 1.303577269
feigenbaum_constant = 4.669201609
glaisher_constant = 1.282427129
lehmer_constant = 0.110264815
levy_constant = 3.275822918
mills_constant = 1.306377883
mrB_constant = 0.2614972128
odds_constant = 0.78515625
omega_constant = 0.5671432904
sierpinski_constant = 2.584981759
thue_morse_constant = 0.4124540336
universal_parabolic_constant = 2.29558714939
viswanath_constant = 1.13198824

# Physics and Astronomy
𝑐 = c = speed_of_light = 299792458
𝐺 = G = gravitational_constant = 6.67430e-11
ℎ = h = plancks_constant = 6.62607015e-34
ℏ = h_bar = reduced_plancks_constant = 1.054571817e-34
𝑘 = k = boltzmanns_constant = 1.380649e-23
𝑁_A = N_A = avogadros_number = 6.02214076e23
𝑒 = e = elementary_charge = 1.602176634e-19
𝑅 = R = gas_constant = 8.314462618
σ = stefan_boltzmann = 5.670374419e-8
ε_0 = vacuum_permittivity = 8.8541878128e-12
μ_0 = vacuum_permeability = 4 * pi * 1e-7
k_e = coulomb_constant = 1/(4*pi*vacuum_permittivity)
α = fine_structure = 1 / 137
m_p = proton_mass = 1.67262192369e-27
m_n = neutron_mass = 1.67492749804e-27
m_e = electron_mass = 9.1093837015e-31
a_0 = bohr_radius = 5.29177210903e-11
R_inf = rydberg_constant = 10973731.568160
m_u = atomic_mass_constant = 1.66053906660e-27
F = faraday_constant = 96485.33212
b = wien_displacement = 2.897771955e-3
H_0 = hubble_constant = 70  # Value between 67 and 73
Λ = cosmological_constant = 1.1056e-52
Gpc = giga_parsec = 3.08567758128e25
solar_mass = 1.98847e30
solar_radius = 6.9634e8
solar_luminosity = 3.828e26
AU = astronomical_unit = 149597870.7
ly = light_year = 9.46073047258e15
pc = parsec = 3.08567758128e16
c_air = sound_speed_air = 343.2
c_water = sound_speed_water = 1481
c_steel = sound_speed_steel = 5130
l_P = planck_length = 1.616255e-35
t_P = planck_time = 5.391247e-44
T_P = planck_temperature = 1.416784e32

# Mechanics
eV = electron_volt = 1.602176634e-19
joule_per_electronvolt = 6.242e+12
N = newton = 1
Pa = pascal = 1
atm = atmosphere = 101325
bar = 100000
torr = 133.322
dyne = 1e-5
erg = 1e-7
cal = calorie = 4.184
btu = 1055.06
hp = horsepower = 745.7
W = watt = 1

# Quantum Mechanics
alpha = fine_structure_constant = 7.2973525664e-3
h_over_4pi = quantum_of_circulation = 3.6369475516e-4
h_over_2pi = quantum_of_circulation_times_2 = 7.2738951033e-4
Phi_0 = flux_quantum = 2.067833848e-15
K_J = josephson_constant = 483597.8484e9
R_K = von_klitzing_constant = 25812.80745
mu_B = bohr_magneton = 9.2740100783e-24
mu_N = nuclear_magneton = 5.0507837461e-27
lambda_C = compton_wavelength = 2.42631023867e-12
lambda_C_over_2pi = compton_wavelength_over_2pi = 386.1592678e-15
r_e = classical_electron_radius = 2.8179403262e-15
E_h = hartree_energy = 4.3597447222071e-18
G_0 = conductance_quantum = 7.748091729e-5
R_0_inv = inverse_conductance_quantum = 12906.40372
mu_0 = magnetic_constant = 1.25663706212e-6
epsilon_0 = electric_constant = 8.8541878128e-12
Z_0 = characteristic_impedance_of_vacuum = 376.730313461
e = elementary_charge = 1.602176634e-19


# Chemistry
V_m = molar_volume_ideal_gas = 22.414
𝑅 = R = molar_gas_constant = 8.314462618
M_air = molar_mass_of_air = 28.97e-3
ρ_water = density_of_water = 1e3
R_d = gas_constant_dry_air = 287.05
eV = electronvolt = 1.602176634e-19
K_w = ion_product_of_water = 1.0e-14  # at 25°C
pK_w = 14  
K_b_chem = boltzmann_constant_chem = 1.380649e-23  
h_chem = planck_constant_chem = 6.62607015e-34  

# Geophysics and Geology
𝑔 = g = earth_gravity = 9.80665
M_E = earth_mass = 5.97237e24
R_E = earth_equatorial_radius = 6378.1
R_p = earth_polar_radius = 6356.8
R_m = earth_mean_radius = 6371.0
f = earth_oblateness = 0.0033528
P_sidereal = sidereal_year = 365.25636
P_tropical = tropical_year = 365.24219

# Electronics and Computer Science
bit = 1
byte = 8 * bit
kB = kilobyte = 1024 * bit
MB = megabyte = 1024 * kilobyte
GB = gigabyte = 1024 * megabyte
TB = terabyte = 1024 * gigabyte
PB = petabyte = 1024 * terabyte
EB = exabyte = 1024 * petabyte
ZB = zettabyte = 1024 * exabyte
YB = yottabyte = 1024 * zettabyte
fLOPS = floating_point_operations_per_second = 1  
MIPS = million_instructions_per_second = 1e6  
Baud = symbols_per_second = 1  
bps = bits_per_second = 1  
Hz = hertz = cycles_per_second = 1  


"""
SHUNTING YARD ALGORITHM
A safe replacement for eval
"""

operatorsDict = {"*": 2, "/": 2, "+": 1, "%": 2, '': 4, "-": 1, "^": 3, "**": 3}
operators = operatorsDict.keys()

def tokenize(inputExpression):
    return re.split("([()" + ''.join(operators) + "])", inputExpression.replace(" ", ""))

def shunting_yard(inputExpression):
    queue = []
    stack = []

    tokens = tokenize(inputExpression)
    tokens = [x for x in tokens if x]
    for token in tokens:
        if(token not in operators and token != "(" and token != ")"):
            queue.append(token)

        if(token == "("):
            stack.append(token)
       
        if(token == ")"):
            while(len(stack) != 0 and stack[-1] != "("):
                queue.append(stack.pop())
     
            stack.pop()
       
        if(token in operators):
            while(len(stack) != 0 and stack[-1] in operators and operatorsDict[stack[-1]] >= operatorsDict[token]):
                queue.append(stack.pop())

            stack.append(token)

    while(len(stack) != 0):
        queue.append(stack.pop())

    return queue

def evaluatePostfix(inputList):
    stack = []
    
    for token in inputList:
        if(token not in operators):
            stack.append(token)
        else:
            operand2 = float(stack.pop())
            operand1 = float(stack.pop())
            if(token == "+"):
                stack.append(operand1 + operand2)

            if(token == "-"):
                stack.append(operand1 - operand2)

            if(token == "*"):
                stack.append(operand1 * operand2)

            if(token == "/"):
                stack.append(operand1 / operand2)

            if(token == '^'):
                stack.append(operand1 ** operand2)
               
    return stack[0]

def evaluateExpression(inputExpression):
    return evaluatePostfix(shunting_yard(inputExpression))

"""
END OF SHUNTING YARD
"""



"""
MATH TEACHERS
"""

def teach_me_trig():
    print("Welcome to the trigonometry basics course!")
    time.sleep(0.5)
    print("One of the most fundamental formulas in trigonometry is the Pythagorean theorem - a^2 + b^2 = c^2, which allows you to find missing sides in a right angled triangle.")
    time.sleep(2)
    print("it works on all right angled triangles")
    time.sleep(1)
    print("Then, to calculate sides given an angle and one other side, SOHCAHTOA will help you remember the ratios:")
    time.sleep(0.5)
    print("sin = opposite/hypotenuse")
    time.sleep(1)
    print("cos = adjacent/hypotenuse")
    time.sleep(1)
    print("and tan = opposite/adjacent")
    time.sleep(1)
    ans = input("If one side of a triangle is 3 and another is 4, what is the hypotenuse? ")
    chances = 2
    while ans.lower().replace(" ", "") not in ["hypotenuse=5", "hyp=5", "5", "five"] and chances > 0:
        print("That is not correct. Please refer to the pythagorean theorem!")
        ans = input("If one side of a triangle is 3 and another is 4, what is the hypotenuse? ")
        chances = chances - 1
    if ans in ["hypotenuse=5", "hyp=5", "5", "five"]:
        print("Great job! This is also a special case for right angled triangles and is known as a Pythagorean triplet.")
    else:
        print("The answer was 5. We needed to use the Pythagorean theorem which states that a^2 + b^2 = c^2, therefore, 3^2 + 4^2 = c^2, and c = 5")
    print("Wikipedia, mathisfun, and other websites can help too")
    print("Thank you!")
    
def teach_me_algebra():
    print("Welcome to the algebra basics course!")
    time.sleep(0.5)
    print("In this basic algebra course, you will learn the basics of solving equations and working with variables.")
    time.sleep(2)
    print("In order to solve one step equations, we will try to isolate all of the varaibles. This means that we want all instances of a variable on one side, and all regular numbers on another.")
    time.sleep(3)
    print("You will often be given an equation where you will have a few operations taking place on either side of the equation. If an 'x' variable is on a side with other numbers, we will perform the opposite operation that eliminates it from that side that it is on.")
    time.sleep(3)
    print("For instance, if we have x+3 = 5, we notice that we have a 3 on the same side as the x. In order to solve for x, we notice that we are adding a three, therefore, we will subtract a three to eliminate it from the x side. However, we need to remember to do the same thing on the other side of the equation. Therefore, the right side becomes 5 -3 = 2. x = 2.")
    time.sleep(3)
    print("In general, a + on one side becomes a - to eliminate it, a * becomes a /, a ^ becomes a root. ")
    time.sleep(1)
    ans = input("3x+5=8, what is x? ")
    chances = 2
    while ans.lower().replace(" ", "") not in ["x=1", "1", "one"] and chances > 0:
        if chances == 2:
            print("That is not correct. Notice that the 3x means 3*x.")
        elif chances == 1:
            print("That is not correct. First, subtract the 5 on both sides. As we have 3*x. We will need to divide both sides by three to solve for x.")
        ans = input("3x+5=8, what is x? ")
        chances = chances - 1
    if ans in ["x=1", "1", "one"]:
        print("Great job!")
    else:
        print("The answer was 1")
        
    print("Wikipedia, mathisfun, and other websites can help too")
    print("Thank you!")
    
def teach_me_derivitives():
    print("welcome to the derivitives basics course!")
    time.sleep(0.5)
    print("a you solve basic derivitives by using a set of rules")
    time.sleep(0.5)
    print("use this link")
    time.sleep(1)
    print("https://www.mathsisfun.com/calculus/derivatives-rules.html")
    print("press enter when you are done")
    while True:
        if keyboard.is_pressed("enter"):
            break
        else:
            pass
    ans = input("what is the derivitive of 1/3x^3? ")
    chances = 2
    while ans not in ["X**2", "x^2", "X^2", "x**2"] and chances > 0:
        print("not correct")
        ans = input("what is the derivitive of 1/3x^3? ")
        chances = chances - 1
    if ans in ["X**2", "x^2", "X^2", "x**2"]:
        print("great job!")
    else:
        print("the answer was x^2")
    print("wikipedia, mathisfun, and other websites can help too")
    print("thank you!")
def teach_me_integrals():
    print("this is a course on basic integrals")
    print("make sure you know derivitives first")
    print("press control C to cancel this course and type teach_me_derivitives() to begin that course")
    time.sleep(2)
    print("integration involves you finding the function for which the derivitive is the function you are integrating (the antidreavative)")
    time.sleep(1)
    print("use the rules from https://www.mathsisfun.com/calculus/integration-rules.html to learn them")
    print("to find the definite integral of a function, you must take the function of the upper bound minus the function of the lower bound")
    print("press enter to continue")
    while True:
        if keyboard.is_pressed("enter"):
            break
        else:
            pass
    time.sleep(1)
    ans = input("what is the integral of x^2? ")
    chances = 2
    while ans not in [9] and chances > 0:
        print("not correct")
        ans = input("what is the integral of x^2? ")
        chances = chances - 1
    if ans in [9]:
        print("great job!")
    else:
        print("the answer was 9")
    print("wikipedia, mathisfun, and other websites can help too")
    print("thank you!")
def teach_me_adalgebra():
    print("welcome to advanced algebra!")
    print("make sure you know basic algebra first")
    print("press control C to cancel this course and type teach_me_algebra() to begin that course")
    time.sleep(1)
    print("let us start with simeltaneous equations")
    print("simultaneous equations involve 2 equations and 2 variables")
    time.sleep(1)
    print("you solve by substituting an equation of x into y in the other one")
    time.sleep(2)
    ans = input("If x + 2y = 14 and 2x + 2= y, find x and y").lower()
    chances = 2
    while ans not in ["x=2, y=6", "x = 2, y=6", "x=2, y = 6", "x = 2, y = 6", "y=6, x=2", "y = 6, x=2", "y=6, x = 2", "y = 6, x = 2", "2, 6", "6, 2"] and chances > 0:
        print("not correct")
        ans = input("If x + 2y = 14 and 2x + 2= y, find x and y").lower()
        chances = chances - 1
    if ans in ["x=2, y=6", "x = 2, y=6", "x=2, y = 6", "x = 2, y = 6", "y=6, x=2", "y = 6, x=2", "y=6, x = 2", "y = 6, x = 2", "2, 6", "6, 2"]:
        print("great job!")
    else:
        print("the answer was x = 2, y = 6")
    print("wikipedia, mathisfun, and other websites can help too")
    print("Now for quadratics")
    print("quadratics are always ax^2 + bx + c = 0")
    print("they have two answers and you use a formula to solve them")
    print("the formula is:")
    print("(-b+_ sqrt(4ac))/2a")
    ans = input("If x^2 - 3x + 2 = 0, find x").lower()
    chances = 2
    while ans not in ["x=1, x=2", "x=2, x=1", "x = 1, x = 2", "x = 2, x = 1", "1 and 2", "1, 2"] and chances > 0:
        print("not correct")
        ans = input("If x^2 - 3x + 2 = 0, find x").lower()
        chances = chances - 1
    if ans in ["x=1, x=2", "x=2, x=1", "x = 1, x = 2", "x = 2, x = 1"]:
        print("great job!")
    else:
        print("the answers were 1 and 2")
def teach_me_adtrig():
    print("welcome to advanced trig!")
    print("make sure you know basic trig first")
    print("press control C to cancel this course and type teach_me_trig() to begin that course")
    time.sleep(1)
    print("let us start with trig identities")
    print("trig identities are relationships between trigonometric functions")
    print("before we learn the identities, we must learn the other three trigonometric functions:")
    time.sleep(1)
    print("csc = hyp/opp")
    time.sleep(1)
    print("sec = hyp/adj")
    time.sleep(1)
    print("cot = adj/opp")
    time.sleep(2)
    print("https://www.mathsisfun.com/algebra/trigonometric-identities.html")
    print("press enter when you are done")
    while True:
        if keyboard.is_pressed("enter"):
            break
        else:
            pass
    print("complete the equation:")
    ans = int(input("sin^2 θ + cos^2 θ = "))
    chances = 2
    while ans not in [1] and chances > 0:
        print("not correct")
        print("complete the equation:")
        ans = int(input("sin^2 θ + cos^2 θ = "))
        chances = chances - 1
    if ans in [1]:
        print("great job!")
    else:
        print("the answer was 1")
def teach():
    print("welcome to random teach (basic)! we will choose a random concept to teach you!")
    rnum = random.randint(1, 4)
    if rnum == 1:
        print("We found derivitives!")
        teach_me_derivitives()
    elif rnum == 2:
        print("We found trig!")
        teach_me_trig()
    else:
        print("We found algebra!")
        teach_me_algebra()
def adteach():
    print("welcome to random teach (advanced)! we will choose a random concept to teach you!")
    rnum = random.randint(1, 3)
    if rnum == 1:
        print("We found integrals!")
        teach_me_integrals()
    elif rnum == 2:
        print("We found trig (advanced)!")
        teach_me_adtrig()
    else:
        print("We found algebra (advanced)!")
        teach_me_adalgebra()

val = ""
def ShowCalculator():
    global bt
    global do_it
    global tk
    global clear
    tk = Tk()
    global data
    data= StringVar()
    lbl=Label(
        tk,
        text="Label",
        anchor=SE,
        font=("Verdana",20),
        textvariable=data,
        background="#ffffff",
        fg="#000000",
    )
    lbl.grid(row = 0, column = 0)
    btn1 = Button(tk, text="1", command= lambda: bt("1"))
    btn1.grid(row = 1, column = 0, sticky = W)
    btn2 = Button(tk, text="2", command= lambda: bt("2"))
    btn2.grid(row = 1, column = 1, sticky = W)
    btn3 = Button(tk, text="3", command= lambda: bt("3"))
    btn3.grid(row = 1, column = 2, sticky = W)
    plus = Button(tk, text="+", command= lambda: bt("+"))
    plus.grid(row = 1, column = 3, sticky = W)
    btn4 = Button(tk, text="4", command= lambda: bt("4"))
    btn4.grid(row = 2, column = 0, sticky = W)
    btn5 = Button(tk, text="5", command= lambda: bt("5"))
    btn5.grid(row = 2, column = 1, sticky = W)
    btn6 = Button(tk, text="6", command= lambda: bt("6"))
    btn6.grid(row = 2, column = 2, sticky = W)
    minus = Button(tk, text="-", command= lambda: bt("-"))
    minus.grid(row = 2, column = 3, sticky = W)
    btn7 = Button(tk, text="7", command= lambda: bt("7"))
    btn7.grid(row = 3, column = 0, sticky = W)
    btn8 = Button(tk, text="8", command= lambda: bt("8"))
    btn8.grid(row = 3, column = 1, sticky = W)
    btn9 = Button(tk, text="9", command= lambda: bt("9"))
    btn9.grid(row = 3, column = 2, sticky = W)
    times = Button(tk, text="*", command= lambda: bt("*"))
    times.grid(row = 3, column = 3, sticky = W)
    btn0 = Button(tk, text="0", command= lambda: bt("0"))
    btn0.grid(row = 4, column = 0, sticky = W)
    dot = Button(tk, text=".", command= lambda: bt("."))
    dot.grid(row = 4, column = 1, sticky = W)
    divide = Button(tk, text="/", command= lambda: bt("/"))
    divide.grid(row = 4, column = 2, sticky = W)
    clr = Button(tk, text="C", command= lambda: clear())
    clr.grid(row = 4, column = 3, sticky = W)
    eq = Button(tk, text="=", command= lambda: do_it())
    eq.grid(row = 5, column = 0, sticky = W)
def HideCalculator():
    tk.destroy()
def bt(x):
    global val
    val = val + x
    data.set(val)
def do_it():
    global val
    y = eval(val)
    data.set(y)
    ans = val
    val=""
def clear():
    global val
    val =""
    data.set(val)
    

"""
END OF MATH TEACHERS
"""
    
"""
OPERATIONS
"""

def add(*args):
    """
    Adds any amount of numbers
    """
    return sum(args)

def subtract(a, *args):
    """
    Subtracts any amount of numbers
    """
    return a - sum(args)

def multiply(*args):
    """
    Multiplies any amount of numbers
    """
    x = 1
    y = 0
    while y < len(args):
        x = x*args[y]
        y+=1
    return x

def divide(a, *args):
    """
    Divides any amount of numbers
    """
    return a / listMultiply(args)


def listMultiply(lis):
    """
    Returns the product of a list
    """
    x = 1
    y = 0
    while y < len(List):
        x = x*List[y]
        y+=1
    return x

def power(base, exponent):
    """
    Returns base^exponent
    """
    
    if exponent == 0:
        return 1
    if exponent > 0:
        return (base * power(base, exponent - 1))
    return 1 /(base * power(base, -exponent - 1))

def sqrt(a):
    return a ** (1/2)

def root(a, b):
    """
    Returns the bth root of a
    """
    
    x = a**(1/b)
    try:
        y = round(x)
        if y-x <= 0.000000000000001:
            if x**(b) != a:
                if b % 2 == 0 and a < 0:
                    z = str(abs(y)) + 'i'
                    print(z)
                else:
                    return y
            else:
                 if b % 2 == 0 and a < 0:
                    z = str(abs(y)) + 'i'
                    print(z)
                 else:
                    return x
        elif y-x >= -0.000000000000001:
            if x**(b) != a and y-x<0:
                 if b % 2 == 0 and a < 0:
                    z = str(abs(y)) + 'i'
                    print(z)
                 else:
                    return y
            else:
                 if b % 2 == 0 and a < 0:
                    z = str(abs(y)) + 'i'
                    print(z)
                 else:
                    return x
        else:
             if b % 2 == 0 and a < 0:
                z = str(abs(y)) + 'i'
                print(z)
             else:
                return x
    except:
        c = b/2
        t = cmath.sqrt(a)
        while c > 2:
             t = cmath.sqrt(t)
             c -= 1
        return t

def factorial(a):
    """
    Returns the factorial (n*factorial(n-1)) of a
    """
    
    x = 1
    while a > 0:
        x *=a
        a -=1
    return x

def log(num, base):
    """
    Returns the logarithm of num with the given base
    """
    
    return math.log(num, base)

def ln(num):
    """
    Returns the natural log (log base e) of num
    """
    
    return log(num, math.e)

def sig_fig(num, figs):
    """
    Rounds num to figs significant figures
    """
    
    rounded = round(num, figs - int(math.floor(math.log10(abs(num)))) - 1)
    return rounded

def abs_val(num):
    """
    Returns the absoltue value of num
    """
    
    return math.fabs(a)

def remainder(a, b):
    """
    Returns the remainder when a is divided by b
    """
    
    return a % b

def gamma(a):
    pass

def lgamma(a):
    return math.lgamma(a)
    pass

def to_degrees(a):
    """
    Returns the angle in radians given converted into degrees
    """
    return math.degrees(a)
def to_radians(a):
    """
    Returns the angle in degrees given converted into radians
    """
    return math.radians(a)

def HCF(a, b):
    """
    Returns the highest common factor of a and b
    """
    
    a, b = max(a, b), min(a, b)
    while b!=0:
        a, b = b, a % b
    return a

def LCM(a, b):
    """
    Returns the lowest common multiple of a and b
    """
    
    return (a*b)/HCF(a, b)
    
def summate(n, a, b):
    return sum(nth_range(n, a, b))

def product(n, a, b):
    return listMultiply(nth_range(n, a, b))

def nchoosek(n, k):
    """
    Returns nCk given by the formula n!/k!(n-k)!
    """
    
    return factorial(n)/(factorial(n-k)*factorial(k))

def permutations(n, r):
    """
    Returns nPr given by the formula n!/(n-k)!
    """
    
    return factorial(n)/factorial(n-r)


    
"""
END OF OPERATIONS
"""



"""
PRIME NUMBERS
"""

def prime_factors(n, Print=False):
    """
    Returns a list of prime factors
    """
    l = []
    while n % 2 == 0:
        l.append(2)
        if Print:
            print(2)
        n = n / 2  
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            l.append(i)
            if Print:
                print(i)
            n = n / i
    if n > 2 and prime_check(n):
        l.append(n)
        if Print:
            print(n)
    return l

def prime_number_printer(lower, upper):
    """
    Prints prime numbers from the lowerbound to the upperbound
    """
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)


def prime_check(n):
    """
    Returns True is it is prime and vice versa
    """
    if n == 1 or not n:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxNum = math.floor(math.sqrt(n))
    for i in range(3, maxNum + 1, 2):
        if not n % i:
            return False
    return True

"""
END OF PRIME NUMBERS
"""



"""
FIBONACCI
"""

def fibonacci_binet(n):
    """
    Fast Fibonacci calculator using Binets formula
    """
    x = (((((1+math.sqrt(5))/2)**n)-((((1-math.sqrt(5))/2)**n))))/math.sqrt(5)
    return round(x)
def fibonacci(n):
    """
    Manual Fibonacci computation
    """
    n0, n = n, abs(n)
    F = {}
    
    qinx = []  
    qinx.append(n)
    F[n] = -1
    while qinx:
        k = qinx.pop() >> 1
        if k not in F:
            F[k] = -1
            qinx.append(k)
        if (k + 1) not in F:
            F[k+1] = -1
            qinx.append(k + 1)
    
    F[0], F[1], F[2] = 0, 1, 1
    keys_sorted = sorted(F.keys())
    for k in keys_sorted[3:]:
        k2 = k >> 1
        f1, f2 = F[k2], F[k2 + 1]
        if k % 2 == 0:
            F[k] = 2 * f2 * f1 - f1 * f1
        else:
            F[k] = f2 * f2 + f1 * f1
    
    r = F[n]
    if n0 < 0:
        return negativeFib(n, r)
    return r

def fibonacci_check(n):
    """
    Checks if a number is in the classic Fibonacci sequence
    """
    return perfect_square_check(5*n*n + 4) or perfect_square_check(5*n*n - 4)

def fibonacci_printer(low, high):
    for i in range(low, high+1):
        if fibonacci_check(i) == True:
            print(i)

"""
END OF FIBONACCI
"""



"""
NUMBER/SEQUENCE CHECKS AND PRINTERS
"""

def perfect_square(num):
    """
    Checks if a number is perfect square
    """
    root = math.sqrt(num)

    if math.trunc(root)-root==0:
        return True
    return False

def perfect_square_check(num):
    """
    Checks if a number is perfect a square
    """
    if perfect_square(num) == True:
        return True
    return False

def perfect_square_printer(low, high):
    """
    Prints perfect squares
    """
    for i in range(low, high):
        if perfect_square(i) == True:
            print(i)
            
def perfect_root_check(a, b):
    """
    Checks if a number is perfect in a given root
    """
    x = root(a, b)
    if x % 1 == 0:
        return True
    return False
def triangular_check(n):
    """
    Checks if a number is a triangular number
    """
    for i in range(n):
        if i*(i+1)/2 == n:
            return True
    return False
def triangular_printer(low, high):
    """
    Prints triangular numbers
    """
    for i in range(low, high):
        if triangular_check(i) == True:
            print(i)
def pentagonal_check(n):
    """
    Checks if a number is a pentagonal number
    """
    i = 1
    while True:
        p = (3 * i * i - i) / 2
        i += 1
        if p >= n:
            break
    return p == n

def pentagonal_printer(low, high):
    """
    Prints pentagonal numbers
    """
    for i in range(low, high):
        if pentagonal_check(i) == True:
            print(i)

def perfect_number_check(n):
    """
    Checks is a number is a perfect number
    """
    pFactors = []
    for i in range(1, n):
        if not n % i:
            pFactors.append(i)
    return sum(pFactors) == n

def perfect_number_printer(lower, upper, list = False):
    """
    Prints perfect numbers
    """
    perfects = [i for i in range(lower, upper+1) if perfect_number_check(i)]
    if list:
        return perfects
    for i in perfects:
        print(i)


"""
END OF NUMBER/SEQUENCE CHECKS AND PRINTERS
"""




"""
DIVISIBILITY CHECKS
"""

def div2_check(num):
    """
    Checks divisibility by 2
    """
    if num % 2 == 0:
        return True
    else:
        return False
def div3_check(num):
    """
    Checks divisibility by 3
    """
    if num % 3 == 0:
        return True
    else:
        return False
def div4_check(num):
    """
    Checks divisibility by 4
    """
    if num % 4 == 0:
        return True
    else:
        return False
def div5_check(num):
    """
    Checks divisibility by 5
    """
    if num % 5 == 0:
        return True
    else:
        return False
def div6_check(num):
    """
    Checks divisibility by 6
    """
    if num % 6 == 0:
        return True
    else:
        return False
def div7_check(num):
    """
    Checks divisibility by 7
    """
    if num % 7 == 0:
        return True
    else:
        return False
def div8_check(num):
    """
    Checks divisibility by 8
    """
    if num % 8 == 0:
        return True
    else:
        return False
def div9_check(num):
    """
    Checks divisibility by 9
    """
    if num % 9 == 0:
        return True
    else:
        return False
def div_check(num, num2):
    """
    Checks divisibility by a given number
    """
    if num % num2 == 0:
        return True
    else:
        return False

"""
END OF DIVISIBILITY CHECKS
"""





"""
FRACTIONS
"""

def add_fraction(a, b):
    """
    Adds Fractions
    """
    ans = Fraction(a) + Fraction(b)
    return str(ans)
def subtract_fraction(a, b):
    """
    Subtracts Fractions
    """
    ans = Fraction(a) - Fraction(b)
    return str(ans)
def multiply_fraction(a, b):
    """
    Multiplies Fractions
    """
    ans = Fraction(a) * Fraction(b)
    return str(ans)
def divide_fraction(a, b):
    """
    Divides Fractions
    """
    ans = Fraction(a) / Fraction(b)
    return str(ans)
def simplify_fraction(a):
    """
    Simplifies Fractions
    """
    return str(Fraction(a).limit_denominator())

def percentage_decimal(percentage):
    """
    Converts percentages to decimals
    """
    return percentage / 100
def per_frac(p):
    """
    Converts percentages to fractions
    """
    dec = p / 100
    fraction = Fraction(dec)
    return str(fraction)
def percentage_fraction(percentage):
    """
    Converts percentages to fractions
    """
    fracOutput = per_frac(percentage)
    return "{0}".format(fracOutput)
def fraction_decimal(fraction):
    """
    Converts fractions to decimals
    """
    dec = f
    return str(round(dec, 5))
def fraction_percentage(fraction):
    """
    Converts fractions to percentages
    """
    return f * 100
def decimal_percentage(decimal):
    """
    Converts decimals to percentages
    """
    percentage = "{:.0%}".format(decimal)
    return str(percentage)
def decimal_fraction(decimal):
    """
    Converts decimals to fractions
    """
    return str(Fraction(decimal).limit_denominator())

"""
END OF FRACTIONS
"""



"""
GEOMETRY
"""

def valid_triangle(s1, s2, s3):
    """
    If a triangle with three given sides is valid
    """
    if s1 + s2 >= s3 and s2 + s3 >= s1 and s1 + s3 >= s2:
        return True
    return False

def triangle_area(l, w):
    """
    Area of a triangle from base and vertical height
    """
    return (l*w)/2
def trapezium_area(a, b, h):
    """
    Area of a trapezium from two parallel sides and vertical height
    """
    return (a+b)/h
def para_area(b, h):
    """
    Area of a parallelogram from base and vertical height
    """
    return b*h
def circle_circumference(r):
    """
    Circumference of a circle from radius
    """
    return 2*pi*r
def circle_area(r):
    """
    Area of a circle from radius
    """
    return pi*(r**2)
def sphere_volume(r):
    """
    Volume of a sphere from radius
    """
    return 4/3*pi*(r**3)
def sphere_area(r):
    """
    Surface area of a sphere from radius
    """
    return 4*pi*(r**2)
def sphere_diametre(r):
    """
    Diameter of a sphere with radius
    """
    return 2*r
def surface_area(a, b, c):
    """
    Surface area of a cuboid with three side lengths
    """
    d = a*b
    e = a*c
    f = b*c
    return 2*(d+e+f)
def surf_area_prism(farea, *args):
    """
    Surface area of a prism with frontal area and length
    """
    total = 2*farea
    i = 0
    while i < len(args):
        total += args[i]
        i += 1
    return total
def volume(a, b, c):
    """
    Volume of a cuboid with three side lengths
    """
    return a*b*c
def cylinder_volume(r, h):
    """
    Volume of a cylinder with height and radius
    """
    return (pi*(r**2))*h
def cylinder_area(r, h):
    """
    Surface area of a cylinder with height and radius
    """
    return (2*pi*r*h)+(2*pi*(r**2))
def cylinder_diametre(v, h):
    """
    Diameter of a cylinder with volume and height
    """
    return 2*(sqrt(v/pi*h))
def cylinder_height(v, r):
    """
    Height of a cylinder with volume and radius
    """
    return v/(pi*(r**2))
def cylinder_radius(h, A):
    """
    radius of a cylinder from height and surface area
    """
    return round(0.5*sqrt(h**2 + 2*(A/pi))-h/2, 5)
def cone_area(r, h):
    """
    Surface area of a cone
    """
    area = pi*r*(r + sqrt(h**2 + r**2))
    return round(area, 5)
def cone_volume(r, h):
    """
    Volume of a cone from radius and height
    """
    vol = pi*r**2*(h/3)
    return round(vol, 5)
def cone_radius(h, vol):
    """
    Radius of cone from height and volume
    """
    rad = sqrt(3*(vol/(pi*h)))
    return round(rad, 5)
def cone_height(r, vol):
    """
    Height of a cone from radius and volume
    """
    height = 3*(vol/(pi*r**2))
    return round(height, 5)

def mamsin(a):
    return math.sin(a)
def mamcos(a):
    return math.cos(a)
def mamtan(a):
    return math.tan(a)
def mamasin(a):
    return math.asin(a)
def mamacos(a):
    return math.acos(a)
def mamatan(a):
    return math.atan(a)
def mamsinh(a):
    return math.sinh(a)
def mamcosh(a):
    return math.cosh(a)
def mamtanh(a):
    return math.tanh(a)
def mamasinh(a):
    return math.asinh(a)
def mamacosh(a):
    return math.acosh(a)
def mamatanh(a):
    return math.atanh(a)
def mamsec(a):
    return round(1/cos(a), 5)
def mamcsc(a):
    return round(1/sin(a), 5)
def mamcot(a):
    return round(1/tan(a), 5)


def py_theorem_ab(a, b):
    """
    Returns the hypotenuse of a triangle given a and b sides
    """
    return sqrt(a**2+b**2)

def py_theorem_c(c, a):
    """
    Returns the missing side length given one leg and the hypotenuse
    """
    return sqrt(c**2-a**2)

def cos_rule(a, b, A_rad):
    """
    Finds the third side of a triangle given two sides and the angle between them
    """
    return a**2 + b**2 - 2*a*b*mamcos(A_rad)

def area_tan(n, s):
    """
    Finds the third side of a triangle given two sides and the angle between them
    """
    s1 = s*s
    up = n*s1
    intan = 180/n
    tanpart = math.tan(intan)
    down = 4*tanpart
    ans = up/down
    return ans

def pythagorean_triplets(n):
    """
    Prints pythagorean triplets until n
    """
    for b in range(n):
        for a in range(1, b):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0:
                print(a, b, int(c))
            
def pythagorean_triplets_check(a, b, c):
    """
    Checks if three numbers can be pythagorean triplets
    """
    return True if a**2 + b**2 == c**2 else False

def hex_area(a):
    """
    Finds the area of a regular hexagon given the side length
    """
    return 1.5 * sqrt(3) * a ** 2

def pent_area(a):
    """
    Finds the area of a regular pentagon given the side length
    """
    return sqrt(5*(5+2*sqrt(5)))/4

def herons_formula(a, b, c):
    """
    Finds the area of any triangle when given three valid sides
    """
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))



"""
END OF OF GEOMETRY
"""



"""
SEQUENCES
"""

def sequence_checker(a, b, c):
    """
    Checks the degree / type of sequence
    """
    while True:
        if b - a == c - b:
            print("Arithmetic")
            break
        if b / a == c / b or a / b == b / c:
            print("Geometric")
            break
        else:
            print("Quadratic")
            break

def nth_finder(a, b):
    """
    Returns the value of the bth term in a sequence whose formula is a
    """
    a = str(a)
    b = str(b)
    x = a.replace("n", b)
    y = eval(x)
    return y

def nth_range(a, b, c):
    """
    Returns the terms b-c of a sequence defined by the formula a
    """
    ls = []
    a = str(a)
    b = str(b)
    c = str(c)
    if int(b) > int(c):
        while int(c) < int(b)+1:
            x = a.replace("n", c)
            y = int(eval(x))
            ls.append(y)
            c = int(c)
            c=int(c)+1
            c = str(c)
    elif int(c) > int(b):
        while int(b) < int(c)+1:
            x = a.replace("n", b)
            y = int(eval(x))
            ls.append(y)
            b = int(b)
            b=int(b)+1
            b = str(b)
    return list(ls)

def nth_table(a, b, c):
    """
    Returns the terms b-c of a sequence defined by the formula a in a table format
    """
    ls = []
    a = str(a)
    b = str(b)
    c = str(c)
    if int(b) > int(c):
        while int(c) < int(b)+1:
            x = a.replace("n", c)
            y = eval(x)
            q = [c, y]
            ls.append(q)
            ls.append(q)
            c = int(c)
            c=int(c)+1
            c = str(c)
    elif int(c) > int(b):
        while int(b) < int(c)+1:
            x = a.replace("n", b)
            y = eval(x)
            q = [b, y]
            ls.append(q)
            b = int(b)
            b=int(b)+1
            b = str(b)
    headers = ["Term", "Value"]
    terms = tabulate(ls, headers = headers)
    print(terms)

def arithemetic_sequence(term1, term2, term = 1):
    """
    Returns the general formula and nth term for a given arithmetic sequence
    """
    dif = term2 - term1
    before = term1 - dif
    newTerm = dif*term+before
    if before == 0:
        print("Nth Term:", str(dif) + "n")
        print(str(term) + "th term:", str(newTerm))
        
    else:
        if before < 0:
            print("Nth Term:", str(dif) + "n" + str(before))
            print(str(term) + "th term:", str(newTerm)) 
        else:
            print("Nth Term:", str(dif) + "n" + " + " + str(before))
            print(str(term) + "th term:", str(newTerm))

def remove_decimal(num):
        if(num == int(num)):
            return int(num)
        return num
    
def nth_term_quadratic(*series):
    """
    Returns the general formula for a quadratic sequence
    """
    r1d1 = series[1] - series[0]
    r1d2 = series[2] - series[1] 
    d2 = r1d2 - r1d1 
    a = d2/2
    b = r1d1 - 3 * a
    c = series[0] - (a + b)
    
    a = removeDecimal(a) 
    b = removeDecimal(b)
    c = removeDecimal(c)
    
    quadraticDict = {0: "", 1: "n^2", -1: "-n^2"}
    linearDict = {0: "", 1: "n", -1: "-n"}
    constantDict = {0: ""}

    quadraticTerm = "{}n^2".format(a) if (a != 0 and a != 1 and a != -1) else quadraticDict[a]
    linearTerm = "{}n".format(b) if (b != 0 and b != 1 and b != -1) else linearDict[b]
    constantTerm = "{}".format(c) if (c != 0) else constantDict[c]

    bSign = "+" if b > 0 else ""
    cSign = "+" if c > 0 else ""

    print(quadraticTerm + bSign + linearTerm + cSign + constantTerm)

def ascending_powers(a, *args):
    args = list(args)
    i = '0'
    eq = ''
    while int(i) < len(args):
        eq += str(args[int(i)]) + '*(n**' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'
    return nth_finder(eq, a)

def ascending_powers_range(a, b, *args):
    args = list(args)
    i = '0'
    eq = ''
    while int(i) < len(args):
        eq += str(args[int(i)]) + '*(n**' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'  
    return nth_range(eq, a, b)

def ascendingpowers_table(a, b, *args):
    args = list(args)
    i = '0'
    eq = ''
    while int(i) < len(args):
        eq += str(args[int(i)]) + '*(n**' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'  
    return nth_table(eq, a, b)
    
"""
END OF SEQUENCES
"""



"""
FORMULAS
"""
#Force, Mass, Acceleration - F=ma
def Force(m, a):
    return m*a
def Mass(f, a):
    return f/a
def Acceleration(f, m):
    return f/m

#Speed, Distance, Time - S=d/t
def Speed(d, t):
    return d/t
def Distance(s, t):
    return s*t
def Time(s, d):
    return s*d
"""
END OF FORMULAS
"""



"""
BASE CONVERSIONS
"""

def base_converter(x, base):
    """
    Converts number x to any given base
    """
    if not isinstance(x, int):
        if x.isdigit():
            x = int(x)
        else:
            x = int("".join(map(str, [ord(i) for i in x])))
            
    digs = string.digits + string.ascii_letters
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[x % base])
        x = x // base

    if sign < 0:
        digits.append("-")

    digits.reverse()
    return "".join(digits)

def int_to_binary(num):
    """
    Converts an integer in base 10 to binary number in base 2
    """
    return bin(num)[2:]
def binary_to_int(num):
    """
    Converts binary number in base 2 to integer in base 10
    """
    return int(str(num), 2)

def int_to_hex(num):
    """
    Converts an integer in base 10 to hexadecimal in base 16
    """
    return hex(num)[2:]
def hex_to_int(num):
    """
    Converts hexadecimal value in base 16 to integer in base 10
    """
    return int(str(num, 2))

def binary_to_hex(num):
    """
    Converts binary number in base 2 to hexadecimal in base 16
    """
    return hex(int(str(num), 2))[2:]
def hex_to_binary(num):
    """
    Converts hexadecimal value in base 16 to to binary number in base 2
    """
    return bin(int(str(num), 2))[2:]

def binary_add(a, b):
    """
    Adds two binary numbers in base two and prints the base 10 result as well
    """
    sum = binary_to_int(a) + binary_to_int(b)
    print("Binary:", int_to_binary(sum))
    print("Base 10:", sum)
    return int_to_binary(sum)
    
def binary_subtract(a, b):
    """
    Subtracts two binary numbers in base two and prints the base 10 result as well
    """
    sub = binary_to_int(a) - binary_to_int(b)
    print("Binary:", int_to_binary(sub))
    print("Base 10:", sub)
    return int_to_binary(sub)
    
def binary_multiply(a, b):
    """
    Multiplies two binary numbers in base two and prints the base 10 result as well
    """
    mult = binary_to_int(a) * binary_to_int(b)
    print("Binary:", int_to_binary(mult))
    print("Base 10:", mult)
    return int_to_binary(mult)
    
def binary_divide(a, b):
    """
    Divides two binary numbers in base two and prints the base 10 result as well
    """
    div = binary_to_int(a) / binary_to_int(b)
    print("Binary:", int_to_binary(div))
    print("Base 10:", div)
    return int_to_binary(div)
    
def hex_add(a, b):
    """
    Adds two hexadecimal numbers in base 16 and prints the base 10 result as well
    """
    sum = hex_to_int(a) + hex_to_int(b)
    print("Hexadecimal:", int_to_hex(sum))
    print("Base 10:", sum)
def hex_subtract(a, b):
    """
    Subtracts two hexadecimal numbers in base 16 and prints the base 10 result as well
    """
    sub = hex_to_int(a) - hex_to_int(b)
    print("Hexadecimal:", int_to_hex(sub))
    print("Base 10:", sub)
def hex_multiply(a, b):
    """
    Multiplies two hexadecimal numbers in base 16 and prints the base 10 result as well
    """
    mult = hex_to_int(a) * hex_to_int(b)
    print("Hexadecimal:", int_to_hex(mult))
    print("Base 10:", mult)
def hex_divide(a, b):
    """
    Divides two hexadecimal numbers in base 16 and prints the base 10 result as well
    """
    div = hex_to_int(a) / hex_to_int(b)
    print("Hexadecimal:", int_to_hex(div))
    print("Base 10:", div)

"""
END OF BASE CONVERSIONS
"""



"""
TABLES
"""

def const_table(category=None):
    """
    Prints a table of all constants, with the option to choose a category
    """
    headers = ["Name", "Symbol", "Value", "Unit"]

    math_constants = [
        ["pi", "π", pi, "dimensionless"],
        ["e", "ℯ", e, "dimensionless"],
        ["Golden Ratio", "ϕ", phi, "dimensionless"],
        ["Imaginary Unit", "𝑖", i, "dimensionless"],
        ["Euler-Mascheroni Constant", "γ", euler_mascheroni, "dimensionless"],
        ["Apery's Constant", "ζ_3", apery, "dimensionless"],
        ["Catalan's Constant", "G", catalan, "dimensionless"],
        ["Square Root of 2", "sqrt2", sqrt2, "dimensionless"],
        ["Square Root of 3", "sqrt3", sqrt3, "dimensionless"],
        ["Natural Logarithm of 2", "ln2", ln2, "dimensionless"],
        ["Natural Logarithm of 10", "ln10", ln10, "dimensionless"],
        ["Khinchin's Constant", "khinchin", khinchin, "dimensionless"],
        ["Twin Prime Constant", "twin_prime", twin_prime, "dimensionless"],
        ["Conway's Constant", "conways_constant", conways_constant, "dimensionless"],
        ["Feigenbaum Constant", "feigenbaum_constant", feigenbaum_constant, "dimensionless"],
        ["Glaisher's Constant", "glaisher_constant", glaisher_constant, "dimensionless"],
        ["Lehmer's Constant", "lehmer_constant", lehmer_constant, "dimensionless"],
        ["Levy's Constant", "levy_constant", levy_constant, "dimensionless"],
        ["Mills' Constant", "mills_constant", mills_constant, "dimensionless"],
        ["MrB Constant", "mrB_constant", mrB_constant, "dimensionless"],
        ["Odds Constant", "odds_constant", odds_constant, "dimensionless"],
        ["Omega Constant", "omega_constant", omega_constant, "dimensionless"],
        ["Sierpinski's Constant", "sierpinski_constant", sierpinski_constant, "dimensionless"],
        ["Thue-Morse Constant", "thue_morse_constant", thue_morse_constant, "dimensionless"],
        ["Universal Parabolic Constant", "universal_parabolic_constant", universal_parabolic_constant, "dimensionless"],
        ["Viswanath's Constant", "viswanath_constant", viswanath_constant, "dimensionless"],
    ]
    physics_constants = [
        ["Speed of Light", "𝑐", c, "m/s"],
        ["Gravitational Constant", "𝐺", G, "m³/kg/s²"],
        ["Planck Constant", "ℎ", h, "J⋅s"],
        ["Reduced Planck Constant", "ℏ", h_bar, "J⋅s"],
        ["Boltzmann Constant", "𝑘", k, "J/K"],
        ["Avogadro Constant", "𝑁_A", N_A, "1/mol"],
        ["Elementary Charge", "𝑒", e, "C"],
        ["Gas Constant", "𝑅", R, "J/(mol⋅K)"],
        ["Stefan-Boltzmann Constant", "σ", stefan_boltzmann, "W/(m²⋅K⁴)"],
        ["Vacuum Permittivity", "ε_0", vacuum_permittivity, "F/m"],
        ["Vacuum Permeability", "μ_0", vacuum_permeability, "H/m"],
        ["Fine Structure Constant", "α", fine_structure, "dimensionless"],
        ["Proton Mass", "m_p", proton_mass, "kg"],
        ["Neutron Mass", "m_n", neutron_mass, "kg"],
        ["Electron Mass", "m_e", electron_mass, "kg"],
        ["Bohr Radius", "a_0", bohr_radius, "m"],
        ["Rydberg Constant", "R_inf", rydberg_constant, "1/m"],
        ["Atomic Mass Constant", "m_u", atomic_mass_constant, "kg"],
        ["Faraday Constant", "F", faraday_constant, "C/mol"],
        ["Wien Displacement Constant", "b", wien_displacement, "m⋅K"],
        ["Hubble Constant", "H_0", hubble_constant, "km/(s⋅Mpc)"],
        ["Cosmological Constant", "Λ", cosmological_constant, "1/m²"],
        ["Giga Parsec", "Gpc", giga_parsec, "m"],
        ["Solar Mass", "solar_mass", solar_mass, "kg"],
        ["Solar Radius", "solar_radius", solar_radius, "m"],
        ["Solar Luminosity", "solar_luminosity", solar_luminosity, "W"],
        ["Astronomical Unit", "AU", astronomical_unit, "m"],
        ["Light Year", "ly", light_year, "m"],
        ["Parsec", "pc", parsec, "m"],
        ["Sound Speed in Air", "c_air", sound_speed_air, "m/s"],
        ["Sound Speed in Water", "c_water", sound_speed_water, "m/s"],
        ["Sound Speed in Steel", "c_steel", sound_speed_steel, "m/s"],
        ["Planck Length", "l_P", planck_length, "m"],
        ["Planck Time", "t_P", planck_time, "s"],
        ["Planck Temperature", "T_P", planck_temperature, "K"],
    ]
    mechanics_constants = [
        ["Electron Volt", "eV", electron_volt, "J"],
        ["Joule per Electronvolt", "joule_per_electronvolt", joule_per_electronvolt, "J/eV"],
        ["Newton", "N", newton, "kg⋅m/s²"],
        ["Pascal", "Pa", pascal, "N/m²"],
        ["Atmosphere", "atm", atmosphere, "Pa"],
        ["Bar", "bar", bar, "Pa"],
        ["Torr", "torr", torr, "Pa"],
        ["Dyne", "dyne", dyne, "N"],
        ["Erg", "erg", erg, "J"],
        ["Calorie", "cal", calorie, "J"],
        ["British Thermal Unit", "btu", btu, "J"],
        ["Horsepower", "hp", horsepower, "W"],
        ["Watt", "W", watt, "J/s"],
    ]
    quantum_constants = [
        ["Fine Structure Constant", "alpha", fine_structure_constant, ""],
        ["Quantum of Circulation", "h_over_4pi", quantum_of_circulation, "m^2/kg"],
        ["Quantum of Circulation Times 2", "h_over_2pi", quantum_of_circulation_times_2, "m^2/kg"],
        ["Flux Quantum", "Phi_0", flux_quantum, "Wb"],
        ["Josephson Constant", "K_J", josephson_constant, "Hz/V"],
        ["Von Klitzing Constant", "R_K", von_klitzing_constant, "ohm"],
        ["Bohr Magneton", "mu_B", bohr_magneton, "J/T"],
        ["Nuclear Magneton", "mu_N", nuclear_magneton, "J/T"],
        ["Compton Wavelength", "lambda_C", compton_wavelength, "m"],
        ["Compton Wavelength Over 2pi", "lambda_C_over_2pi", compton_wavelength_over_2pi, "m"],
        ["Classical Electron Radius", "r_e", classical_electron_radius, "m"],
        ["Hartree Energy", "E_h", hartree_energy, "J"],
        ["Conductance Quantum", "G_0", conductance_quantum, "S"],
        ["Inverse Conductance Quantum", "R_0_inv", inverse_conductance_quantum, "ohm"],
        ["Magnetic Constant", "mu_0", magnetic_constant, "N/A^2"],
        ["Electric Constant", "epsilon_0", electric_constant, "F/m"],
        ["Characteristic Impedance of Vacuum", "Z_0", characteristic_impedance_of_vacuum, "ohm"],
        ["Elementary Charge", "e", elementary_charge, "C"],
    ]
    chemistry_constants = [
        ["Electronvolt", "eV", electronvolt],
        ["Molar Volume of Ideal Gas", "V_m", V_m, "L/mol"],
        ["Molar Gas Constant", "𝑅", R, "J/mol·K"],
        ["Ion product of water", "K_w", K_w, "mol^2/L^2"],
        ["pKw of water", "pK_w", pK_w, "dimensionless"],
        ["Boltzmann constant (Chemistry)", "K_b_chem", k, "J/K"],
        ["Planck constant (Chemistry)", "h_chem", h_chem, "J·s"],
        ["Molar Mass of Air", "M_air", M_air, "kg/mol"],
        ["Density of Water", "ρ_water", ρ_water, "kg/m^3"],
        ["Gas Constant for Dry Air", "R_d", R_d, "J/kg·K"],
    ]
    geophysics_constants = [
        ["Earth Gravity", "𝑔", earth_gravity, "m/s^2"],
        ["Earth Mass", "M_E", earth_mass, "kg"],
        ["Earth Equatorial Radius", "R_E", earth_equatorial_radius, "km"],
        ["Earth Polar Radius", "R_p", earth_polar_radius, "km"],
        ["Earth Mean Radius", "R_m", earth_mean_radius, "km"],
        ["Earth Oblateness", "f", earth_oblateness, "dimensionless"],
        ["Sidereal Year", "P_sidereal", sidereal_year, "days"],
        ["Tropical Year", "P_tropical", tropical_year, "days"],
    ]
    computer_constants = [
        ["Bit", "bit", bit, "bit"],
        ["Byte", "byte", byte, "bit"],
        ["Kilobyte", "kB", kilobyte, "byte"],
        ["Megabyte", "MB", megabyte, "byte"],
        ["Gigabyte", "GB", gigabyte, "byte"],
        ["Terabyte", "TB", terabyte, "byte"],
        ["Petabyte", "PB", petabyte, "byte"],
        ["Exabyte", "EB", exabyte, "byte"],
        ["Zettabyte", "ZB", zettabyte, "byte"],
        ["Yottabyte", "YB", yottabyte, "byte"],
        ["Floating point operations per second", "fLOPS", floating_point_operations_per_second, "FLOPS"],
        ["Million instructions per second", "MIPS", million_instructions_per_second, "instructions/s"],
        ["Symbols per second", "Baud", symbols_per_second, "Baud"],
        ["Bits per second", "bps", bits_per_second, "bps"],
        ["Hertz", "Hz", hertz, "Hz"],
    ]
    constants_by_category = {
        "Mathematics": math_constants,
        "Physics": physics_constants,
        "Mechanics": mechanics_constants,
        "Quantum": quantum_constants,
        "Chemistry": chemistry_constants,
        "Geophysics": geophysics_constants,
        "Computer": computer_constants,
    }
    
    if category is None:
        for cat, constants in constants_by_category.items():
            print(f"{cat} Constants:")
            print(tabulate(constants, headers=headers))
            print("\n")
    else:
        if category in constants_by_category:
            print(f"{category} Constants:")
            print(tabulate(constants_by_category[category], headers=headers))
        else:
            print("Invalid category. Please choose a valid category ['Mathematics', 'Physics', 'Mechanics', 'Quantum', 'Chemistry', 'Geophysics', 'Computer'].")

  
    
def trig_table():
    """
    Prints a table of the most useful trigonometric identities
    """
    identities = {"Quotient Identities": ["tanθ = sinθ/cosθ", "cotθ = cosθ/sinθ"],
           "Reciprocal Identities": ["cotθ = 1/tanθ", "cscθ = 1/sinθ", "sec = 1/cosθ"],
           "Pythagorean Identities": ["sin^2θ + cos^2θ = 1", "tan^2θ + 1 = sec^2θ", "1 + cot^2θ = csc^2θ"],
           "Sum Identities": ["sin(a+b) = sin(a)cos(b)+cos(a)sin(b)", "cos(a+b) = cos(a)cos(b)-sin(a)sin(b)", "tan(a+b) = (tan(a) + tan(b))/1 - tan(a)tan(b)"],
           "Difference Identities": ["sin(a-b) = sin(a)cos(b)-cos(a)sin(b)", "cos(a-b) = cos(a)cos(b)+sin(a)sin(b)", "tan(a-b) = (tan(a)-tan(b))/1 + tan(a)tan(b)"],
           "Double-Angle Formulas": ["sin(2a) = 2sin(a)cos(a)", "cos(2a) = 2cos^2 a - 1 = 1 - 2sin^2 a", "tan(2a) = 2tan(a)/1-tan^2 a"]
           }
    print(tabulate(identities, headers = "keys"))

"""
END OF TABLES
"""



"""
HELPER FUNCTIONS
"""

def f(fx, x, y):
    if type(eval(fx)) == np.ndarray:
        return eval(fx)

def parse_equation(eq):
    pass

"""
END OF HELPER FUNCTIONS
"""






"""
GRAPHING
"""

#graph("2*x", "3*x")
def graph(*args, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, gridset=True, scaling=True, graph_title=None, xtitle=None, ytitle=None):
    """
    Graphs any number of 2D functions given a string function of x equating to y. The first 4 keyword arguments change the axis of the graph.
    """
    i = 0
    x = np.linspace(lrangex, urangex, graph_points)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines["left"].set_position("center")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    while i < len(args):
        if type(eval(args[i])) == np.ndarray:
            y = eval(args[i])
            plt.plot(x,y, "-b", label=args)
            i+=1
    plt.title(graph_title)
    plt.xlabel(xtitle,fontsize=20)
    plt.ylabel(ytitle,fontsize=20)
    plt.autoscale(enable=scaling)
    plt.grid(gridset)
    if lrangex or urangex != False:
        plt.xlim([lrangex,urangex])
        if lrangey or urangey != False:
            plt.ylim([lrangey,urangey])
            plt.show()

    
def graph3d_contour(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='binary'):
    """
    Graphs any number of 3D functions given a string function of x equating to y as a contour. The first 6 keyword arguments change the axis of the graph.
    """
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    i = 0
    while i < len(args):
        X, Y = np.meshgrid(x, y)
        Z = f(args[i], X, Y)
        ax.contour3D(X, Y, Z, 50, cmap=cmap)
        i += 1
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    ax.set_title(graph_title)
    if lrangez != False or urangez == False:
        ax.set_zlim(lrangez, urangez)
    if lrangex != False or urangex == False:
        ax.set_zlim(lrangex, urangex)
    if lrangey != False or urangey == False:
        ax.set_zlim(lrangey, urangey)
    return plt.show()

def graph3d_line(*args, lrangex=-10, lrangey=-10, lrangez = -10, urangex=10, urangey=10, urangez = 10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, color='gray'):
    """
    Graphs any number of 3D functions given a list of 2 elements - a function of x and a function of y, both equating to z. The first 6 keyword arguments change the axis of the graph.
    """
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    i = 0
    while i < len(args):
        lis = args[i]
        fz = lis[0]
        fy = lis[1]
        if type(eval(fz)) == np.ndarray:
            zline = eval(fz)
        else:
            pass
        if type(eval(fy)) == np.ndarray:
            yline = eval(fy)
        else:
            pass
        ax.plot3D(x, yline, zline, color)
        i+=1
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)
    ax.set_title(graph_title)
    if lrangez != False or urangez == False:
        ax.set_zlim(lrangez, urangez)
    if lrangex != False or urangex == False:
        ax.set_zlim(lrangex, urangex)
    if lrangey != False or urangey == False:
        ax.set_zlim(lrangey, urangey)
    return plt.show()

def graph3d_wire(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, edgecolor=False, color='black', fill='viridis'):
    """
    Graphs any number of 3D functions given a string function of x equating to y as a wire. The first 6 keyword arguments change the axis of the graph.
    """
    x = np.linspace(lrangex, urangex, graph_points)
    y = np.linspace(lrangey, urangey, graph_points)
    ax = plt.axes(projection='3d')
    X, Y = np.meshgrid(x, y)
    i = 0
    while i < len(args):
        Z = f(args[i], X, Y)
        if fill==False:
            ax.plot_wireframe(X, Y, Z, color=color)
        elif edgecolor == True:
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap=fill, edgecolor=color)
        elif edgecolor == False:
            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap=fill, edgecolor='none')
        else:
            raise TypeError('Parameter "edgecolor" must be a boolean operator')
        i += 1
    ax.set_xlabel(lablex)
    ax.set_ylabel(labley)
    ax.set_zlabel(lablez)   
    ax.set_title(graph_title)
    if lrangez != False or urangez == False:
        ax.set_zlim(lrangez, urangez)
    if lrangex != False or urangex == False:
        ax.set_zlim(lrangex, urangex)
    if lrangey != False or urangey == False:
        ax.set_zlim(lrangey, urangey)
    return plt.show()

"""
END OF GRAPHING
"""



"""
ALGEBRA
"""

def quadratic_solver(a,b,c):
    """
    Prints the roots of a quadratic function in the form of ax^2 + bx + c = 0
    """
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))
    elif dis == 0:
        print(-b / (2 * a))
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

        
def solve_gauss_elimination(*equations):
    """
    Solves any system of equations using Gaussian Elimination
    """
    equations = list(equations)
    for i in range(0, len(equations)):
        equations[i] = equations[i].replace(" ", "")
        
    eqs = []
    varis = set()
    for k in range(len(equations)):
        equations[k] = equations[k].replace('-','+-')
        eqDict = dict()
        sides = equations[k].split('=')
        termsLeft = sides[0].split('+')
        termsRight = sides[1].split('+')
        for term in termsLeft:
            if term != '':
                if term.isnumeric():
                    if 'constant' in eqDict:
                        eqDict['constant'] += -int(term)
                    else:
                        eqDict['constant'] = -int(term)
                    continue
                elif not '-' in term:
                    if term.isalpha():
                        coeff = 1
                        vari = term
                    else:
                        l = 0
                        while term[l].isdigit():
                            l += 1
                        coeff = int(term[:l])
                        vari = term[l:]
                else:
                    if term[1:].isnumeric():
                        if 'constant' in eqDict:
                            eqDict['constant'] += -int(term)
                        else:
                            eqDict['constant'] = -int(term)
                        continue
                    elif term[1:].isalpha():
                        coeff = -1
                        vari = term[1:]
                    else:
                        l = 1
                        while term[l].isdigit():
                            l += 1
                        coeff = -int(term[1:l])
                        vari = term[l:]
                varis.add(vari)
                if vari in eqDict:
                    eqDict[vari] += coeff
                else:
                    eqDict[vari] = coeff
        for term in termsRight:
            if term != '':
                if term.isnumeric():
                    if 'constant' in eqDict:
                        eqDict['constant'] += int(term)
                    else:
                        eqDict['constant'] = int(term)
                    continue
                elif not '-' in term:
                    if term.isalpha():
                        coeff = -1
                        vari = term
                    else:
                        l = 0
                        while term[l].isdigit():
                            l += 1
                        coeff = -int(term[:l])
                        vari = term[l:]
                else:
                    if term[1:].isnumeric():
                        if 'constant' in eqDict:
                            eqDict['constant'] += int(term)
                        else:
                            eqDict['constant'] = int(term)
                        continue
                    if term[1:].isalpha():
                        coeff = 1
                        vari = term[1:]
                    else:
                        l = 1
                        while term[l].isdigit():
                            l += 1
                        coeff = int(term[1:l])
                        vari = term[l:]
                varis.add(vari)
                if vari in eqDict:
                    eqDict[vari] += coeff
                else:
                    eqDict[vari] = coeff
        if not 'constant' in eqDict:
            eqDict['constant'] = 0
        eqs.append(eqDict)
    if len(eqs) < len(varis):
        return None
    varis = sorted(list(varis))
    matrix = []
    for eq in eqs:
        row = []
        for vari in varis:
            if vari in eq:
                row.append(eq[vari])
            else:
                row.append(0)
        matrix.append(row)
    b = [eq['constant'] for eq in eqs]
    
    nothingHappened = False
    while not nothingHappened:
        nothingHappened = True
        for i1 in range(len(matrix)-1):
            for i2 in range(1+i1,len(matrix)):
                j1 = 0
                while matrix[i1][j1] == 0:
                    j1 += 1
                j2 = 0
                while matrix[i2][j2] == 0:
                    j2 += 1
                if [matrix[i1][j]/matrix[i1][j1] for j in range(len(matrix[i1]))] == [matrix[i2][j]/matrix[i2][j2] for j in range(len(matrix[i2]))]:
                    if b[i1]/matrix[i1][j1] != b[i2]/matrix[i2][j2]:
                        return None
                    else:
                        matrix = matrix[:i1]+matrix[i1+1:]
                        b = b[:i1]+b[i1+1:]
                        nothingHappened = False
                        break
            if not nothingHappened:
                break
    if len(matrix) != len(matrix[0]):
        return None
    n = 0
    while n < len(matrix):
        while matrix[n][n] == 0:
            if n == len(matrix)-1:
                return None
            r = matrix[n]
            matrix.pop(n)
            matrix.append(r)
            v = b[n]
            b.pop(n)
            b.append(v)
        c = 1/matrix[n][n]
        matrix[n] = [c*matrix[n][j] for j in range(len(matrix[n]))]
        b[n] = c*b[n]
        k = 1
        while n+k < len(matrix):
            c = matrix[n+k][n]
            matrix[n+k] = [matrix[n+k][j] - c*matrix[n][j] for j in range(len(matrix[n]))]
            if matrix[n+k] == [0]*len(matrix[n+k]):
                return None
            b[n+k] = b[n+k] - c*b[n]
            k += 1
        n += 1
    n = len(matrix)-1
    while n >= 0:
        k = 1
        while n-k >= 0:
            c = matrix[n-k][n]
            matrix[n-k] = [matrix[n-k][j] - c*matrix[n][j] for j in range(len(matrix[n]))]
            b[n-k] = b[n-k] - c*b[n]
            k += 1
        n -= 1
    answer = {}
    for k in range(len(varis)):
        answer[varis[k]] = b[k]
    return answer

def linear_system_2x2(equation1, equation2):
    """
    Solves any 2x2 system of equations
    """
    def preprocess_equation(eq):
        eq = eq.replace(" ", "")
        eq = eq.replace("+x", "+1x").replace("+y", "+1y")
        eq = eq.replace("-x", "-1x").replace("-y", "-1y")
        if eq[0] == "x" or eq[0] == "y":
            eq = "1" + eq
        return eq

    equation1, equation2 = preprocess_equation(equation1), preprocess_equation(equation2)

    def parse_equation(eq):
        eq = eq.replace("x", " ").replace("y", " ").replace("=", " ").replace("+", "").split()
        coefficients = list(map(float, eq[:2]))
        product = float(eq[2])
        return coefficients, product

    coefficients1, product1 = parse_equation(equation1)
    coefficients2, product2 = parse_equation(equation2)

    coMatrix = np.array([coefficients1, coefficients2])
    productMatrix = np.array([[product1], [product2]])

    solMatrix = np.linalg.solve(coMatrix, productMatrix)
    sols = [round(float(x), 1) if round(float(x)) == float(x) else "%0.4f" % x for x in solMatrix.flatten()]
    check = np.allclose(np.dot(coMatrix, solMatrix), productMatrix)

    return print(f"x: {sols[0]}\ny: {sols[1]}") if check else None    

def discriminant_quadratic(a, b, c):
    """
    Discriminant of a quadratic equation in the form of ax^2 + bx + c = 0
    """
    return b**2 - 4 * a * c

def rootp_quadratic(a, b, c, disc):
    """
    Returns the plus root of a quadratic equation in the form of ax^2 + bx + c = 0
    """
    return (-b + disc ** (1/2)) / (2 * a)

def rootm_quadratic(a, b, c, disc):
    """
    Returns the minus root of a quadratic equation in the form of ax^2 + bx + c = 0
    """
    return (-b - disc ** (1/2)) / (2 * a)

def roots_quadratic(a, b, c):
    """
    Returns the roots of a quadratic equation in the form of ax^2 + bx + c = 0 as a tuple
    """
    return (rootp_quadratic(a, b, c, discriminant_quadratic(a, b, c), rootm_quadratic(a, b, c, discriminant_quadratic(a, b, c))))
            
def solve_first_degree(b, c):
    """
    Returns the solution of a first degree equation in the form of bx+c=0
    """
    return -c / b

def second_degree_solver(a, b, c):
    """
    Prints the solutions up to a second degree equation
    """
    if a == 0:
        if b == 0:
            return "The equation is indeterminate" if c == 0 else "Impossible situation. Wrong entries"
        return f"It is a first degree equation. Solution: {'0.0' if c == 0 else solve_first_degree(b, c)}"
    else:
        disc = discriminant_quadratic(a, b, c)
        if disc < 0:
            return "There are no real solutions"
        elif disc == 0:
            root = rootm_quadratic(a, b, c, disc)
            return f"It has one double solution: {abs(root)}"
        else:
            root1, root2 = rootm_quadratic(a, b, c, disc), roots_quadratic(a, b, c, disc)
            sorted_sol = sorted([abs(root1) if root1 == -0.0 else root1, abs(root2) if root2 == -0.0 else root2])
            return f"Two solutions: {sorted_sol[0]}, {sorted_sol[1]}"

def inequality(eq):
    pass

"""
END OF ALGEBRA
"""









"""
CALCULUS
"""

def derivative_at(f_of, x):
    """
    Returns the derivative of any function at a point x
    """
    h = 0.00001
    return round(1 / (12 * h) * (f_of(x - 2 * h) - 8 * f_of(x - h) + 8 * f_of(x + h) - f_of(x + 2 * h)), 7)
    #1/12h * f(x-2 *h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)

def derivative(f_of, solvefor):
    """
    Returns the symbolic derivative of any function
    """
    return diff(f_of, solvefor)
    
def def_integral(f, lowerbound, upperbound, n = 10000):
    """
    Returns the definite integral of any function with the lower and upper bounds specified
    """
    stepLen = (upperbound - lowerbound) / n
    lb = lowerbound
    xRange = np.arange(lb, upperbound, stepLen)
    total = f(lowerbound) + f(upperbound)
    for i in range(1, n):
        total += 2*f(xRange[i])
    integralVal = total * stepLen / 2
    return round(integralVal, 5)

def indef_integral(f_of, solvefor):
    """
    Returns the symbolic integral of any function
    """
    integral = str(integrate(f_of, solvefor)) + " + C"
    return integral 

"""
END OF CALCULUS
"""


"""
LINEAR ALGEBRA
"""
def diagonal_sum(mat):
    """
    Returns the sum of the diagonal elements in a matrix
    """
    left = 0
    right = 0
    for i in range(0, len(mat)):
        left += mat[i][i]
        right += mat[i][len(mat) - i - 1]
    total = left + right
    if len(mat) % 2 != 0:
        return total - (mat[len(mat) // 2][len(mat) // 2])
    return total

def adjoint2x2(matrix):
    return np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]).tolist()

def adjoint3x3(matrix):
    a = np.array([[(matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1]),
                   -((matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0])),
                   ((matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0]))],
                                    
                  [-((matrix[0][1]*matrix[2][2]) - (matrix[0][2]*matrix[2][1])),
                    ((matrix[0][0]*matrix[2][2]) - (matrix[0][2]*matrix[2][0])),
                    -((matrix[0][0]*matrix[2][1]) - (matrix[0][1]*matrix[2][0]))],
                                    
                  [((matrix[0][1]*matrix[1][2]) - (matrix[0][2]*matrix[1][1])),
                   -((matrix[0][0]*matrix[1][2]) - (matrix[0][2]*matrix[1][0])),
                    ((matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0]))]])

    return np.transpose(a)

def cofactor_matrix(matrix, tempMatrix, row, col, order):
    """
    Helper function for finding the cofactor matrix, which can be transposed to get the adjoint matrix, useful for finding the inverse of a matrix
    """
    i = 0
    j = 0
    for r in range(order):
        for c in range(order):
            if r != row and c != col:
                tempMatrix[i][j] = matrix[r][c]
                j += 1
                if j == order - 1:
                    j = 0
                    i += 1

def determinant(matrix, order=1):
    """
    Returns the determinant of an nxn matrix
    """
    det = 0
    order = len(matrix[0])-1
    print(order)
    if order == 1:
        return matrix[0][0]
    tempMatrix = [[None for i in range(order)] for i in range(order)]
    sign = 1

    for f in range(order):
        cofactor_matrix(matrix, tempMatrix, 0, f, order)
        det += sign * matrix[0][f] * determinant(tempMatrix, order = order - 1)
        sign = -sign

    return det    

"""
END OF LINEAR ALGEBRA
"""





"""
COMPLEX
"""

def complex_ln(num):
    """
    Returns the natural log of a complex number
    """
    principle = str(ln(-num)) + ' + iπ'
    general = str(ln(-num)) + 'iπ(2n+1) n ∊ ℤ'
    print(f"Principal Value: {principle}")
    print(f"General: {general}")
    return str(ln(-num)) + " + " + str(math.pi) + 'i'


"""
END OF COMPLEX
"""




    
"""
PHYSICS
"""

class Planet:
    def __init__(self, name, mass, radius, semi_major_axis, orbital_period, eccentricity):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.semi_major_axis = semi_major_axis
        self.orbital_period = orbital_period
        self.eccentricity = eccentricity

    def as_dict(self):
        return {
            'Name': self.name,
            'Mass (kg)': self.mass,
            'Radius (km)': self.radius,
            'Semi-major Axis (km)': self.semi_major_axis,
            'Orbital Period (Earth days)': self.orbital_period,
            'Eccentricity': self.eccentricity
        }

class SolarSystem:
    def __init__(self):
        self.planets = [
            Planet('Mercury', 3.3011e23, 2439.7, 57_909_227, 87.9691, 0.2056),
            Planet('Venus', 4.8675e24, 6051.8, 108_209_475, 224.70069, 0.0067),
            Planet('Earth', 5.97237e24, 6371, 149_598_262, 365.25641, 0.0167),
            Planet('Mars', 6.4171e23, 3389.5, 227_943_824, 687.0, 0.0934),
            Planet('Jupiter', 1.8982e27, 69_911, 778_340_821, 4_332.59, 0.0489),
            Planet('Saturn', 5.6834e26, 58_232, 1_426_666_422, 10_759.22, 0.0565),
            Planet('Uranus', 8.6810e25, 25_362, 2_870_658_186, 30_688.5, 0.0463),
            Planet('Neptune', 1.02413e26, 24_622, 4_498_396_441, 60_182, 0.0095),
        ]

    def display_planet(self, name):
        """
        Displays all the information of a given planet in a table
        """
        planet = self.get_planet(name)
        if planet:
            table = tabulate([planet.as_dict()], headers='keys', tablefmt='pretty')
            print(table)
        else:
            print("Planet not found.")

    def get_planet(self, name):
        """
        Displays all of the information of a given planet
        """
        for planet in self.planets:
            if planet.name.lower() == name.lower():
                return planet
        return None
            
solar_system = SolarSystem()


def event_horizon(mass):
    """
    Computes the schwarzschild radius of a schwarzschild black hole given the mass of the black hole
    """
    return (2*G*mass)/speed_of_light**2

def grav_field(mass, distance):
    """
    Computes the gravitational field given the mass and distance. E.g. Earth: G*earth_mass / (earth_mean_radius*1000)^2 ≈ 9.82
    """
    return mass * G / distance ** 2

def separate_vectors(vector, theta, deg=True):
    if not deg:
        theta = 180 * theta / pi
    return (vector * cos(theta), vector * sin(theta))

def electric_field(q, r):
    """
    Calculates the acceleration from a point on an electromagnetic field
    """
    return q * coulomb_constant / r ** 2

def centripetal_acceleration(v, r):
    """
    Returns the centripetal acceleration for the given velocity and radius.
    """
    return v**2 / r

def centripetal_force(m, v, r):
    """
    Calculates the centripetal force of an object in a circular motion
    """
    return m * v ** 2 / r

def get_hookes(F, dx):
    """
    Returns the Hookes constant for the spring
    """
    return F / dx

def newtonian_gravity(m1, m2, d):
    """
    Returns the gravtitational force on two given objects of defined mass and centers d meters apart
    """
    return (m1*m2)/(d**2) * G

def suvat_solve(solve_for, s=None, u=None, v=None, a=None, t=None):
    """
    Uses the SUVAT equations to solve for s, u, v, a, t
    """
    equations = {
        's': lambda u, v, a, t: (u + v) * t / 2 if u and v and t else u * t + 0.5 * a * t**2,
        'u': lambda s, v, a, t: (s - 0.5 * a * t ** 2) / t if s else v - a * t,
        'v': lambda s, u, a, t: u + a * t,
        'a': lambda s, u, v, t: 2 * (s - (u + v) * t / 2) / t ** 2,
        't': lambda s, u, v, a: (v - u) / a,
    }

    if solve_for not in equations:
        raise ValueError("Invalid 'solve_for' value. Must be one of 's', 'u', 'v', 'a', or 't'.")

    variables = {'s': s, 'u': u, 'v': v, 'a': a, 't': t}
    known_vars = [var for var, value in variables.items() if value is not None]

    if len(known_vars) < 3:
        raise ValueError("There must be at least 3 known variables to solve the equation.")

    try:
        result = equations[solve_for](*[variables[var] for var in 'suvat' if var != solve_for])
    except ZeroDivisionError:
        raise ValueError("Cannot solve for the given variables, division by zero encountered.")

    return result

def vis_viva_equation(r_au, a_au, m1, m2):
    """
    Returns the orbital velocity of a body in an orbital motion
    """
    r = r_au * 1.496*10**11
    a = a_au * 1.496*10**11
    standard_grav_param = G*(m1 + m2)
    return sqrt(standard_grav_param*(2/r - 1/a))

def einsteinian_force(mass, acceleration, v):
    """
    Returns the force taking into account Einstein's laws of motion
    """
    return mass * acceleration / (1 - v**2/c**2)**(3/2)

def terminal_velocity(m, cross_area, drag_coefficient=0.294, air_density=1.225, gravity=g):
    """
    Calculates the terminal velocity based on mass and cross sectional area, drag_coefficient pre defined to headfirst human.
    """
    return sqrt(2*m*gravity/(cross_area*air_density*drag_coefficient))

def acceleration_constant(v, u, t):
    """
    Returns the acceleration when given v (final velocity), u (initial velocity, and t (time).
    """
    return (v-u)/t

def kinetic_energy(m, v):
    """
    Returns the kinetic energy for the given mass and velocity.
    """
    return 0.5 * m * v**2

def potential_energy(m, g, h):
    """
    Returns the potential energy for the given mass, gravity, and height.
    """
    return m * g * h

def power(w, t):
    """
    Returns the power as the ratio of work done to time.
    """
    return w / t

def momentum(m, v):
    """
    Returns the momentum for the given mass and velocity.
    """
    return m * v

def impulse_momentum_theorem(f, delta_t):
    """
    Returns the impulse, equal to the product of force and time interval.
    """
    return f * delta_t

def ideal_gas_law(p, v, n, T):
    """
    Returns the result of the ideal gas law equation for given pressure, volume, moles, gas constant, and temperature.
    """
    return p * v - n * R * T

def heat_capacity(m, c, delta_t):
    """
    Returns the heat capacity for the given mass, specific heat capacity, and temperature change.
    """
    return m * c * delta_t

def ohms_law(v, I, R):
    """
    Returns the result of Ohm's Law for the given voltage, current, and resistance.
    """
    return v - I * R

def coulombs_law(k, q1, q2, r):
    """
    Returns the electrostatic force between two charges according to Coulomb's Law.
    """
    return coulomb_constant * q1 * q2 / r**2

def faradays_law_em_induction(d_phi_b, dt):
    """
    Returns the induced electromotive force according to Faraday's Law of Electromagnetic Induction.
    """
    return -d_phi_b / dt

def lensmakers_equation(n, R1, R2):
    """
    Returns the focal length of a lens using the lensmaker's equation.
    """
    return (n - 1) * (1 / R1 - 1 / R2)

def time_dilation(delta_t0, v, c):
    """
    Returns the time dilation for a given proper time, relative velocity, and speed of light.
    """
    return delta_t0 / sqrt(1 - v**2 / c**2)

def length_contraction(length, v):
    """
    Returns the length contraction for a given proper length, relative velocity, and speed of light.
    """
    return length * sqrt((1 - v**2 / c**2))

def wave_speed(frequency, wavelength):
    """
    Returns the wave speed given the frequency and wavelength.
    """
    return frequency * wavelength

def boltzmann_entropy(W):
    """
    Returns the entropy according to Boltzmann's entropy formula.
    """
    return boltzmanns_constant * ln(W)

def particle_in_box_energy(n, L, m):
    """
    Returns the energy of a particle in a one-dimensional box for the given quantum number.
    """
    return (n**2 * pi**2 * h_bar**2) / (2 * m * L**2)

def planck_law(wavelength, T):
    """
    Returns the spectral radiance for a blackbody at a given temperature and wavelength.
    """
    return (2 * pi * h * c**2) / (wavelength**5 * (np.exp((h * c) / (wavelength * k * T)) - 1))

def lorentz_force(q, E, B, v):
    """
    Returns the Lorentz force experienced by a charged particle in an electric and magnetic field.
    """
    return q * (E + np.cross(v, B))

def lorentz_factor(v):
    """
    Returns the Lorentz factor for a given velocity.
    """
    return 1 / sqrt(1 - v**2 / c**2)

def decay_law(N0, lambda_, t):
    """
    Returns the number of radioactive nuclei remaining after a given time.
    """
    return N0 * np.exp(-lambda_ * t)

def relativistic_doppler_shift(wavelength, v):
    """
    Returns the shifted wavelength due to the relativistic Doppler effect.
    """
    return wavelength * sqrt((1 + v/c) / (1 - v/c))

def escape_velocity(m, r):
    """
    Returns the escape velocity for a celestial body of mass m and radius r.
    """
    return sqrt(2 * G * m / r)

def heat_engine_efficiency(W, Qh):
    """
    Returns the efficiency of a heat engine given the work done and heat input.
    """
    return W / Qh

def first_law_of_thermodynamics(Q, W, U1, U2):
    """
    Returns the relationship between heat, work, and internal energy changes in a thermodynamic process.
    """
    return Q - W == U2 - U1

def de_broglie_wavelength(m, v):
    """
    Returns the de Broglie wavelength of a particle with a given mass and velocity.
    """
    return h_bar / (m * v)

def photon_energy(frequency):
    """
    Returns the energy of a photon given its frequency.
    """
    return h * frequency



"""
END OF PHYSICS
"""

"""
UNIT CONVERSIONS
"""

def distance_converter(value, from_unit, to_unit):
    """
    Converts between any two distance units
    """
    units = {
        "m": 1,                       # meter
        "km": 1000,                   # kilometer
        "cm": 0.01,                   # centimeter
        "mm": 0.001,                  # millimeter
        "um": 1e-6,                   # micrometer
        "nm": 1e-9,                   # nanometer
        "angstrom": 1e-10,            # angstrom
        "mi": 1609.34,                # mile
        "yd": 0.9144,                 # yard
        "ft": 0.3048,                 # foot
        "in": 0.0254,                 # inch
        "nmi": 1852,                  # nautical mile
        "au": 149597870700,           # astronomical unit
        "ly": 9.4607e15,              # light year
        "pc": 3.08567758149137e16,    # parsec
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit. Supported units: m, km, cm, mm, um, nm, angstrom, mi, yd, ft, in, nmi, au, ly, pc")

    meters = value * units[from_unit]
    converted_value = meters / units[to_unit]

    return converted_value

def area_converter(value, from_unit, to_unit):
    """
    Converts between any two area units
    """
    units = {
        "sq_m": 1,                           # square meter
        "sq_km": 1e6,                        # square kilometer
        "sq_cm": 1e-4,                       # square centimeter
        "sq_mm": 1e-6,                       # square millimeter
        "sq_um": 1e-12,                      # square micrometer
        "sq_nm": 1e-18,                      # square nanometer
        "sq_angstrom": 1e-20,                # square angstrom
        "sq_mi": 2.589988110336e6,           # square mile
        "sq_yd": 0.83612736,                 # square yard
        "sq_ft": 0.09290304,                 # square foot
        "sq_in": 6.4516e-4,                  # square inch
        "acre": 4046.8564224,                # acre
        "hectare": 10000,                    # hectare
        "sq_nmi": 3.4299039988274e6,         # square nautical mile
        "sq_au": 2.2379529036721e22,         # square astronomical unit
        "sq_ly": 8.9505421074819e31,         # square light year
        "sq_pc": 9.5214088218406e32,         # square parsec
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit. Supported units: sq_m, sq_km, sq_cm, sq_mm, sq_um, sq_nm, sq_angstrom, sq_mi, sq_yd, sq_ft, sq_in, acre, hectare, sq_nmi, sq_au, sq_ly, sq_pc")

    sq_meters = value * units[from_unit]
    converted_value = sq_meters / units[to_unit]

    return converted_value

def volume_converter(value, from_unit, to_unit):
    """
    Converts between any two volume units
    """
    units = {
        "cu_m": 1,                          # cubic meter
        "cu_km": 1e9,                       # cubic kilometer
        "cu_cm": 1e-6,                      # cubic centimeter
        "cu_mm": 1e-9,                      # cubic millimeter
        "cu_um": 1e-18,                     # cubic micrometer
        "cu_nm": 1e-27,                     # cubic nanometer
        "cu_angstrom": 1e-30,               # cubic angstrom
        "cu_mi": 4.16818183e9,              # cubic mile
        "cu_yd": 0.764554857984,            # cubic yard
        "cu_ft": 0.028316846592,            # cubic foot
        "cu_in": 1.6387064e-5,              # cubic inch
        "l": 0.001,                         # liter
        "ml": 1e-6,                         # milliliter
        "gal": 0.00378541,                  # US gallon
        "qt": 0.000946353,                  # US quart
        "pt": 0.000473176,                  # US pint
        "cup": 0.000236588,                 # US cup
        "floz": 2.957353e-5,                # US fluid ounce
        "tbsp": 1.47867648e-5,              # US tablespoon
        "tsp": 4.92892159e-6,               # US teaspoon
        "imp_gal": 0.00454609,              # imperial gallon
        "imp_qt": 0.001136523,              # imperial quart
        "imp_pt": 0.000568261,              # imperial pint
        "imp_floz": 2.841306e-5,            # imperial fluid ounce
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit. Supported units: cu_m, cu_km, cu_cm, cu_mm, cu_um, cu_nm, cu_angstrom, cu_mi, cu_yd, cu_ft, cu_in, l, ml, gal, qt, pt, cup, floz, tbsp, tsp, imp_gal, imp_qt, imp_pt, imp_floz")

    cu_meters = value * units[from_unit]
    converted_value = cu_meters / units[to_unit]

    return converted_value

def mass_converter(value, from_unit, to_unit):
    units = {
        "kg": 1,                     # kilogram
        "g": 0.001,                  # gram
        "mg": 1e-6,                  # milligram
        "ug": 1e-9,                  # microgram
        "ng": 1e-12,                 # nanogram
        "pg": 1e-15,                 # picogram
        "lb": 0.45359237,            # pound
        "oz": 0.028349523125,        # ounce
        "st": 6.35029318,            # stone
        "ton": 907.18474,            # short ton (US ton)
        "long_ton": 1016.0469088,    # long ton (UK ton)
        "t": 1000,                   # metric ton
        "ct": 0.0002,                # carat
        "gr": 0.00006479891,         # grain
        "amu": 1.66053904e-27,       # atomic mass unit
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid unit. Supported units: kg, g, mg, ug, ng, pg, lb, oz, st, ton, long_ton, t, ct, gr, amu")

    kilograms = value * units[from_unit]
    converted_value = kilograms / units[to_unit]

    return converted_value

"""
END OF UNIT CONVERSIONS
"""


"""
MISC
"""

def is_infinite(x):
    return mpmath.isinf(x)
def is_finite(x):
    return mpmath.isfinite(x)
def is_int(x, gaussian = False): 
    return mpmath.isint(x, gaussian)

def Zeta(s):
    pass

def percentage_change(a, b):
    """
    Returns the percentage change from a to b
    """
    if a == b:
        return 100.0
    try:
        return round(((b - a)/a)*100, 3)
    except ZeroDivisionError:
        return float("inf")
    
def percentage(a, b, integer = False):
    """
    Returns what percent a is of b
    """
    percent = a / b * 100
    if integer:
        return int(percent)
    return percent

def average(*numbers):
    """
    Returns the average of any amount of given numbers
    """
    total = np.sum(list(numbers))
    length = len(numbers)
    return total / length

def consecutive_int_calc(x):
    """
    Returns three consecutive numbers that sum to the given number x
    """
    a = (x/3)-1
    b = x/3
    c = (x/3)+1
    return [a, b, c]

def ascending_sort(*args):
    """
    Sorts given values in ascending order
    """
    argList = list(args)
    argList.sort()
    return argList

def descending_sort(*args):
    """
    Sorts given values in descending order
    """
    argList = list(args)
    argList.sort(reverse=True)
    return argList

def times_tables(n):
    """
    Prints times tables until n
    """
    for i in range(1, n+1):
        for j in range(i, (n*i)+i, i):
            print(str(j) + " ", end="")
        print("")

def coefficients_quadratic(string):
    """
    Returns the coefficients of a quadratic equation in a list given in the form of ax^2 + bx + c
    """
    string = "".join(" " if i == "x" or i == "+" else i for i in string)
    string = string.replace("^2", " ")
    return list(map(int, string.split()))

def sum_to_palindrome(num, stepsList = False):
    """
    Returns the amount of iterations it takes for the reverse of a number, added to the number to be a palindrome, and the resulting palindrome
    """
    isPalindrome = lambda num: num == num[::-1]
    steps = 0
    stepList = [] if stepsList else None
    while not isPalindrome(str(num)):
        num = str(num)
        num = str(int(num) + int(str(num)[::-1]))
        steps += 1
        stepList.append(num) if stepsList else None
  
    return "Final palindrome: " + num + ", Steps: " + str(steps) if not stepsList else "Final Palindrome: " + num + ", Steps: " + str(steps) + ", Step List: " + str([(i+1, int(j)) for i, j in enumerate(stepList)]).strip("[]")
        
def proth_primes(k):
    """
    Returns the next Proth prime (k*2^n + 1) with k given 
    """
    n = 1
    while not prime_check((k * 2**n) + 1):
        n += 1
    return "Number: " + str((k * 2**n) + 1) + ", n: " + str(n)
    
def proth_primes_check(k, n):
    """
    Checks if a number is in the form of a Proth prime
    """
    return prime_check((k * 2**n) + 1)

def is_polydivisible(number):
    """
    Returns whether a number is polydivisible or not - a number where the first to the nth digit in the number is divisible by n
    """
    polydiv = False
    if number > 0:
        n = number
        length = 0
        while n > 0:
            n = int(n / 10)
            length += 1
        if n == 1:
            polydiv = True
        else:
            data = [0] * length
            i = length - 1
            num = 0
            n = number
            while n > 0:
                data[i] = n % 10
                n = int(n / 10)
                i -= 1
            num = data[0]
            i = 1
            if num:
                polydiv = True
            while i < length and polydiv:
                num = (num * 10) + data[i]
                if ((num % (i + 1)) != 0):
                    polydiv = False
                i += 1          
    return polydiv

def weighted_avg(*args):
    """
    Input any nmber of numbers with values and weights in tuple of that orders
    """
    t = 0
    x = 0
    for i in args:
        t += i[1]
        x += i[0] * i[1]
    return x / t

def to_standard_form(n):
    """
    Converts the integer n to standard form as a tuple, (a, b) where n = a * 10 ** b
    """
    t = 0
    while n > 10:
        n /= 10
        t += 1
    return n, t

def pascals_printer(n):
    """
    Gives the rows up to the nth row of Pascal's triangle
    """
    for i in range(n):
        print('')
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
            
def pascals(n):
    """
    Gives the nth row of the pascals triangle
    """
    l = []
    for i in range(n+1):
        l.append(factorial(n)//(factorial(i)*factorial(n-i)))     
    return l

"""
END OF MISC
"""
