from sympy import *
from sympy.abc import x, y
import tkinter
from tkinter import *
from tabulate import tabulate
import string
from fractions import Fraction
from mpmath import *
import numpy as np
import math
import cmath
import time
import sys
import keyboard
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import inspect
import re

operatorsDict = {"*": 2, "/": 2, "+": 1, "%": 2, '': 4, "-": 1}
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


def teach_me_trig():
    print("welcome to the trig basics course!")
    time.sleep(0.5)
    print("a basics trigonometric formula is a^2 + b^2 = c^2, the pythagorean theorom")
    time.sleep(2)
    print("it works on all right angled triangles")
    time.sleep(1)
    print(" soh cah toa will help you remember:")
    time.sleep(0.5)
    print("sin = opposite/hypotenuse")
    time.sleep(1)
    print("cos = adjacent over hypotenuse")
    time.sleep(1)
    print("and tan = opposite over adjacent")
    time.sleep(1)
    ans = input("If one side of a triangle is 3 and another is 4, what is the hypotenuse? ")
    chances = 2
    while ans not in ["hypotenuse = 5", "Hypotenuse = 5", "Hyp = 5, hyp = 5", "5", "hyp=5", "Hyp=5", "Hypotenuse=5", "hypotenuse=5"] and chances > 0:
        print("not correct")
        ans = input("If one side of a triangle is 3 and another is 4, what is the hypotenuse? ")
        chances = chances - 1
    if ans in ["hypotenuse = 5", "Hypotenuse = 5", "Hyp = 5, hyp = 5", "5", "hyp=5", "Hyp=5", "Hypotenuse=5", "hypotenuse=5"]:
        print("great job!")
    else:
        print("the answer was 5")
    print("wikipedia, mathisfun, and other websites can help too")
    print("thank you!")
def teach_me_algebra():
    print("welcome to the algebra basics course!")
    time.sleep(0.5)
    print("a you solve basic equations by moving variables to one side and numbers to the other")
    time.sleep(2)
    print("remember, change the operation when it crosses the equals sign")
    time.sleep(1)
    print(" - becomes +, + becomes -")
    time.sleep(1)
    print("x becomes /, / becomes x")
    time.sleep(1)
    print("and ^n becomes root(n), root(n) becomes ^n")
    time.sleep(1)
    ans = input("3x+5=8, what is x? ")
    chances = 2
    while ans not in ["X = 1", "x = 1", "x=1", "X=1", "3"] and chances > 0:
        print("not correct")
        ans = input("3x+5=8, what is x? ")
        chances = chances - 1
    if ans in ["X = 1", "x = 1", "x=1", "X=1", "3"]:
        print("great job!")
    else:
        print("the answer was 3")
    print("wikipedia, mathisfun, and other websites can help too")
    print("thank you!")
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
    y = evaluateExpression(val)
    data.set(y)
    ans = val
    val=""
def clear():
    global val
    val =""
    data.set(val)
    


    
def add(*args):
    return sum(args)
def subtract(a, *args):
    return a - sum(args)
def multiply(*args):
    x = 1
    y = 0
    while y < len(args):
        x = x*args[y]
        y+=1
    return x
def divide(a, *args):
    return a / listMultiply(args)
def listMultiply(List):
    x = 1
    y = 0
    while y < len(List):
        x = x*List[y]
        y+=1
    return x
def power(a, *args):    
    b = mult(args)
    x = a**(b)
    if b < 1:
        return root(a, 1/b)
    else:
        return x
    
def recLimit(a):
    messagebox.askyesno("RECURSION SETTINGS", "Setting your recursion limit may slow your laptop or cause a crash. Proceed with caution. Do You wish to continue?")
def sqrt(a):
    return math.sqrt(a)

def addFraction(a, b):
    ans = Fraction(a) + Fraction(b)
    return str(ans)
def subtractFraction(a, b):
    ans = Fraction(a) - Fraction(b)
    return str(ans)
def multiplyFraction(a, b):
    ans = Fraction(a) * Fraction(b)
    return str(ans)
def divideFraction(a, b):
    ans = Fraction(a) / Fraction(b)
    return str(ans)
def simplifyFraction(a):
    return str(Fraction(a).limit_denominator())

def root(a, b):    #
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
    
def log(a, b):
    return math.log(a, b)
def sf(a, b):
    rounded = round(a, b - int(math.floor(math.log10(abs(a)))) - 1)
    return rounded
def absVal(a):
    return math.fabs(a)
def remainder(a, b):
    return math.remainder(a, b)
def toDegrees(a):
    return math.degrees(a)
def toRadians(a):
    return math.radians(a)

def HCF(a, b):
    a, b = max(a, b), min(a, b)
    while b!=0:
        a, b = b, a % b
    return a
def LCM(a, b):
    return (a*b)/HCF(a, b)
def primeFactors(n):
    while n % 2 == 0:
            print(2)
            n = n / 2  
    for i in range(3,int(math.sqrt(n))+1,2):
            while n % i== 0:
                    print(i)
                    n = n / i
    if n > 2:
            print(n)

def factorial(a):
    x = 1
    while a > 0:
        x *=a
        a -=1
    return x
def checkPrime(num):
    x = False
    for i in range(2, num):
        if num % i == 0:
            x = True
    if x:
        return False
    return True
def primeNumberPrinter(low, high):
    for num in range(low, high+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
def perfectSquare(num):
    root = math.sqrt(num)

    if math.trunc(root)-root==0:
        return True
    return False
def perfectSquarePrinter(low, high):
    for i in range(low, high):
        if perfectSquare(i) == True:
            print(i)
def perfectRootCheck(a, b):
    x = root(a, b)
    if x % 1 == 0:
        return True
    return False
def triangularCheck(n):
    for i in range(n):
        if i*(i+1)/2 == n:
            return True
    return False
def triangularPrinter(low, high):
    for i in range(low, high):
        if triangularCheck(i) == True:
            print(i)
def pentagonalCheck(n):
    i = 1
    while True:
        p = (3 * i * i - i) / 2
        i += 1
        if p >= n:
            break
    return p == n

def pentagonalPrinter(low, high):
    for i in range(low, high):
        if pentagonalCheck(i) == True:
            print(i)
def fibonacci(n):
    x = (((((1+math.sqrt(5))/2)**n)-((((1-math.sqrt(5))/2)**n))))/math.sqrt(5)
    return round(x)
def fibonacciCheck(n):
    return perfectSquareCheck(5*n*n + 4) or perfectSquareCheck(5*n*n - 4)
def fibonacciPrinter(low, high):
    for i in range(low, high+1):
        if fibonacciCheck(i) == True:
            print(i)
            
def divis2Check(num):
    if num % 2 == 0:
        return True
    else:
        return False
def divis3Check(num):
    if num % 3 == 0:
        return True
    else:
        return False
def divis4Check(num):
    if num % 4 == 0:
        return True
    else:
        return False
def divis5Check(num):
    if num % 5 == 0:
        return True
    else:
        return False
def divis6Check(num):
    if num % 6 == 0:
        return True
    else:
        return False
def divis7Check(num):
    if num % 7 == 0:
        return True
    else:
        return False
def divis8Check(num):
    if num % 8 == 0:
        return True
    else:
        return False
def divis9Check(num):
    if num % 9 == 0:
        return True
    else:
        return False
def divisCheck(num, num2):
    if num % num2 == 0:
        return True
    else:
        return False
def summate(n, a, b):
    return sum(nthRange(n, a, b))
def product(n, a, b):
    return listMultiply(nthRange(n, a, b))

def PercentagetoDecimal(percentage):
    return p / 100
def PerToFrac(p):
    dec = p / 100
    fraction = Fraction(dec)
    return str(fraction)
def PercentagetoFraction(percentage):
    fracOutput = PertoFrac(p)
    return "{0}".format(fracOutput)
def FractiontoDecimal(fraction):
    dec = f
    return str(round(dec, 5))
def FractiontoPercentage(fraction):
    return f * 100
def DecimaltoPercentage(decimal):
    percentage = "{:.0%}".format(d)
    return str(percentage)
def DecimaltoFraction(decimal):
    return str(Fraction(d).limit_denominator())

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
def gamma(a):
    return math.gamma(a)
def lgamma(a):
    return math.lgamma(a)

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
    
def speedCalc(d, t):
    return d/t
def distCalc(s, t):
    return s*t
def timeCalc(s, d):
    return s*d
    
def quadraticSolver(a,b,c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
            print(" real and different roots ")
            print((-b + sqrt_val)/(2 * a))
            print((-b - sqrt_val)/(2 * a))
    elif dis == 0:
            print(" real and same roots")
            print(-b / (2 * a))
    else:
            print("Complex Roots")
            print(- b / (2 * a), " + i", sqrt_val)
            print(- b / (2 * a), " - i", sqrt_val)

def sequenceChecker(a, b, c, d, e):
    while 1 < 2:
        if b - a == c - b:
            print("Arithmetic")
            break
        if b / a == c / b or a / b == b / c:
            print("Geometric")
            break
        else:
            print("Quadratic")
            break

def nthFinder(a, b):
    a = str(a)
    b = str(b)
    x = a.replace("n", b)
    y = evaluateExpression(x)
    return y
def nthRange(a, b, c):
    ls = []
    a = str(a)
    b = str(b)
    c = str(c)
    if int(b) > int(c):
        while int(c) < int(b)+1:
            x = a.replace("n", c)
            y = int(evaluateExpression(x))
            ls.append(y)
            c = int(c)
            c=int(c)+1
            c = str(c)
    elif int(c) > int(b):
        while int(b) < int(c)+1:
            x = a.replace("n", b)
            y = int(evaluateExpression(x))
            ls.append(y)
            b = int(b)
            b=int(b)+1
            b = str(b)
    return list(ls)
def nthTable(a, b, c):
    ls = []
    a = str(a)
    b = str(b)
    c = str(c)
    if int(b) > int(c):
        while int(c) < int(b)+1:
            x = a.replace("n", c)
            y = evaluateExpression(x)
            q = [c, y]
            ls.append(q)
            ls.append(q)
            c = int(c)
            c=int(c)+1
            c = str(c)
    elif int(c) > int(b):
        while int(b) < int(c)+1:
            x = a.replace("n", b)
            y = evaluateExpression(x)
            q = [b, y]
            ls.append(q)
            b = int(b)
            b=int(b)+1
            b = str(b)
    headers = ["term", "value"]
    thing = tabulate(ls, headers = headers)
    print(thing)

def arithemeticSequence(term1, term2, term = 1):
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

def percentageChange(a, b):
    if a == b:
        return 100.0
    try:
        return round(((b - a)/a)*100, 3)
    except ZeroDivisionError:
        return float("inf")
def percentage(a, b, integer = False):
    percent = a / b * 100
    if integer:
        return int(percent)
    return percent

def average(*argv):
    total = np.sum(list(argv))
    length = len(argv)
    return total / length
def consecutiveIntCalc(x):
    a = (x/3)-1
    b = x/3
    c = (x/3)+1
    return [a, b, c]

def ascendingSort(*args):
    argList = list(args)
    argList.sort()
    return argList
def descendingSort(*args):
    argList = list(args)
    argList.sort(reverse=True)
    return argList

def ascendingPowers(a, *args):
    args = list(args)
    i = '0'
    eq = ''
    while int(i) < len(args):
        eq += str(args[int(i)]) + '*(n**' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'
    return nthFinder(eq, a)
def ascendingPowersRange(a, b, *args):
    args = list(args)
    i = '0'
    eq = ''
    while int(i) < len(args):
        eq += str(args[int(i)]) + '*(n**' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'  
    return nthRange(eq, a, b)
def ascendingpowersTable(a, b, *args):
    args = list(args)
    i = '0'
    eq = ''
    while int(i) < len(args):
        eq += str(args[int(i)]) + '*(n**' + str(i) + ') +'
        i = int(i)
        i += 1
        i = str(i)
    eq += '0'  
    return nthTable(eq, a, b)

def F(m, a):
    return m*a
def M(f, a):
    return f/a
def A(f, m):
    return f/m

def baseConverter(x, base):
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

def IntToBinary(num):
    return bin(num)[2:]
def BinaryToInt(num):
    return int(str(num), 2)
def IntToHexa(num):
    return hex(num)[2:]
def HexaToInt(num):
    return int(str(num, 2))
def binaryAdd(a, b):
    sum = BinaryToInt(a) + BinaryToInt(b)
    print("Binary:", IntToBinary(sum))
    print("Base 10:", sum)
def binarySubtract(a, b):
    sub = BinaryToInt(a) - BinaryToInt(b)
    print("Binary:", IntToBinary(sub))
    print("Base 10:", sub)
def binaryMultiply(a, b):
    mult = BinaryToInt(a) * BinaryToInt(b)
    print("Binary:", IntToBinary(mult))
    print("Base 10:", mult)
def binaryDivide(a, b):
    div = BinaryToInt(a) / BinaryToInt(b)
    print("Binary:", IntToBinary(div))
    print("Base 10:", div)
    
def hexaAdd(a, b):
    sum = HexaToInt(a) + HexaToInt(b)
    print("Hexadecimal:", IntToHexa(sum))
    print("Base 10:", sum)
def hexaSubtract(a, b):
    sub = HexaToInt(a) - HexaToInt(b)
    print("Hexadecimal:", IntToHexa(sub))
    print("Base 10:", sub)
def hexaMultiply(a, b):
    mult = HexaToInt(a) * HexaToInt(b)
    print("Hexadecimal:", IntToHexa(mult))
    print("Base 10:", mult)
def hexaDivide(a, b):
    div = HexaToInt(a) / HexaToInt(b)
    print("Hexadecimal:", IntToHexa(div))
    print("Base 10:", div)

def constSearch(con):
    G = 6.67384*10**(-11)
    c = 2.99792458*10**(8)
    h = 6.626070040*10**(-34)
    k = 1.38064852*10**(-23)
    F = 9.648533289*10**(4)
    pi = 3.141592653589793238462643
    e = 2.718281828459045235360287
    π = pi
    phi = 1.618033988749894848204586
    φ = phi
    conlist = [G, c, h, k, F, pi, π, φ, phi, e]
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
    pi = 3.141592653589793238462643
    e = 2.718281828459045235360287
    π = pi
    phi = 1.618033988749894848204586
    φ = phi
    conlist = [["The gravitational constant", "G", G], ["The speed of light in vacuum", "c", c], ["Planck's constant", "h", h], ["Boltzmann's constant", "k", k], ["Faraday's constant", "F", F], ["e", "e", e], ["pi", "φ", π], ["Phi", "φ", φ]]
    headers = ["Name", "Symbol", "Value"]
    thing = tabulate(conlist, headers = headers)
    print(thing)

def graph(*args, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, gridset=True, scaling=True, graph_title=None, xtitle=None, ytitle=None):
    i = 0
    x = np.linspace(lrangex, urangex, graph_points)
    while i < len(args):
        if type(eval(args[i])) == np.ndarray:
            y = eval(args[i])
        else:
            pass
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines["left"].set_position("center")
        ax.spines["bottom"].set_position("zero")
        ax.spines["right"].set_color("none")
        ax.spines["top"].set_color("none")
        ax.xaxis.set_ticks_position("bottom")
        ax.yaxis.set_ticks_position("left")
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

def isInfinite(x):
    return mpmath.isinf(x)
def isFinite(x):
    return mpmath.isfinite(x)
def isInt(x, gaussian = False): 
    return mpmath.isint(x, gaussian)

def Zeta(s):
    return zeta(s)

def graph(*args, lrangex=-10, urangex=10, lrangey=-10, urangey=10, graph_points=100, gridset=True, scaling=True, graph_title=None, xtitle=None, ytitle=None):
    i = 0
    x = np.linspace(lrangex, urangex, graph_points)
    while i < len(args):
        if type(eval(args[i])) == np.ndarray:
            y = eval(args[i])
        else:
            pass
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines["left"].set_position("center")
        ax.spines["bottom"].set_position("zero")
        ax.spines["right"].set_color("none")
        ax.spines["top"].set_color("none")
        ax.xaxis.set_ticks_position("bottom")
        ax.yaxis.set_ticks_position("left")
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
def f(fx, x, y):
    if type(eval(fx)) == np.ndarray:
        return eval(fx)
    else:
        pass
    
def graph3dcontour(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, cmap='binary'):
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
def linein3d(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, color='gray'):
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
def graph3dwire(*args, lrangex=-10, lrangey=-10, urangex=10, urangey=10, lrangez=-10, urangez=10, graph_points=1000, lablex='x', labley='y', lablez='z', graph_title=None, edgecolor=False, color='black', fill='viridis'):
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

def derivative(f_of, solvefor):
    return diff(f_of, solvefor)
def secondDerivative(f_of, *args):
    return diff(f_of, args)
def integral(f_of, solvefor):
    integral = integrate(f_of, solvefor)
    return integral
def IndefIntegral(f_of, solvefor):
    integral = str(integrate(f_of, solvefor)) + " + C"
    return integral
def defIntegral(f_of, solvefor, lowerbound, upperbound):
    return integrate((f_of), (solvefor, lowerbound, upperbound))
def Limit(f_of, solvefor, to):
    return limit(f_of, solvefor, to)
    
