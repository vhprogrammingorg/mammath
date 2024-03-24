import time
import keyboard
import random

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
