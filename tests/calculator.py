from tkinter import *
from ShuntingYardAlgorithm import evaluateExpression

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
