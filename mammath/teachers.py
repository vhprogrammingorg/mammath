from tkinter import *
import time
import random
import keyboard as keyboard

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
    
def teach_me_derivatives():
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
        teach_me_derivatives()
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


