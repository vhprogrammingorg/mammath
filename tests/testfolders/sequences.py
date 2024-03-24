from ShuntingYardAlgorithm import evaluateExpression
from tabulate import tabulate

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

def arithmeticSequence(*args, term = 1):
    terms = list(args)
    dif = terms[1] - terms[0]
    before = terms[0] - dif
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
def geometricSequence(term1, term2, term3, term = 1):
    dif = term2 / term1
    

def quadraticSequence(*args, term = 1):
    terms = list(args)
    r1d1 = terms[1] - terms[0]
    print(r1d1)
    r1d2 = terms[2] - terms[1]
    print(r1d2)
    r2d1 = r1d2-r1d1
    print(r2d1)
    
    a = r2d1 / 2
    b = r1d1 - 3*a
    c = -a - b + terms[0]
    print(a)
    print(b)
    print(c)
    
    finalTerm = a*term**2 + b*term + c
    
    if b < 0:
        print("Nth term:", str(int(a)) + "x^2 " + str(int(b)) + "x + " + str(int(c)) + ". Term " + str(int(term)) + ": " + str(int(finalTerm)))
    elif c < 0:
        print("Nth term:", str(int(a)) + "x^2 + " + str(int(b)) + "x " + str(int(c)) + ". Term " + str(int(term)) + ": " + str(int(finalTerm)))
    else:
        print("Nth term:", str(int(a)) + "x^2 + " + str(int(b)) + "x + " + str(int(c)) + ". Term " + str(int(term)) + ": " + str(int(finalTerm)))
def cubicSequence(*args, term = 1):
    terms = list(args)
    r1d1 = terms[1] - terms[0]
    r1d2 = terms[2] - terms[1]
    r1d3 = terms[3] - terms[2]
    r2d1 = r1d2 - r1d1
    r2d2 = r1d3 - r1d2
    r3d1 = r2d2 - r2d1
    a = r3d1 / 6
    b = (r2d1/2)-6*a
    c = -7*a-3*b+r1d1
    d = -a - b - c + terms[0]
    finalTerm = a*term**3 + b*term**2 + c*term + d
    if b < 0:
        print("Nth term:", str(int(a)) + "x^3 " + str(int(b)) + "x^2 + " + str(int(c)) + "x + " + str(int(d)) + ". Term " + str(int(term)) + ": " + str(int(finalTerm)))
    if c < 0:
        print("Nth term:", str(int(a)) + "x^3 + " + str(int(b)) + "x^2 " + str(int(c)) + "x + " + str(int(d)) + ". Term " + str(int(term)) + ": " + str(int(finalTerm)))
    if d < 0:
        print("Nth term:", str(int(a)) + "x^3 + " + str(int(b)) + "x^2 + " + str(int(c)) + "x " + str(int(d)) + ". Term " + str(int(term)) + ": " + str(int(finalTerm)))
def SequenceChecker(*args):
    seq_nums = list(args)
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    if len(set(seq_nums)) == 1:
        return "Linear Sequence"
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    if len(set(seq_nums)) == 1:
        return "Quadratic Sequence"
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    if len(set(seq_nums)) == 1:
        return "Cubic Sequence"


