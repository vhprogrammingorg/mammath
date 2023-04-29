import tabulate
from helper import remove_decimal
from fractions import Fraction

"""
SEQUENCES
"""

def sequence_checker(a, b, c):
    """
    Checks the degree / type of sequence.

    Args:
        a (int/float): The first term of the sequence.
        b (int/float): The second term of the sequence.
        c (int/float): The third term of the sequence.
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
    Returns the value of the bth term in a sequence whose formula is a.

    Args:
        a (str): The formula of the sequence with variable "n".
        b (int): The term number to be found.
        
    Returns:
        int: The value of the bth term in the sequence.
    """
    a = str(a)
    b = str(b)
    x = a.replace("n", b)
    y = eval(x)
    return y

def nth_range(a, b, c):
    """
    Returns the terms b-c of a sequence defined by the formula a.

    Args:
        a (str): The formula of the sequence with variable "n".
        b (int): The starting term number.
        c (int): The ending term number.
        
    Returns:
        list: A list of terms from bth to cth term in the sequence.
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
    Returns the terms b-c of a sequence defined by the formula a in a table format.

    Args:
        a (str): The formula of the sequence with variable "n".
        b (int): The starting term number.
        c (int): The ending term number.
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
    Returns the general formula and nth term for a given arithmetic sequence.

    Args:
        term1 (int/float): The first term of the sequence.
        term2 (int/float): The second term of the sequence.
        term (int, optional): The term number to be found. Defaults to 1.
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
    
def nth_term_quadratic(*series):
    """
    Returns the general formula for a quadratic sequence.

    Args:
        *series: A tuple containing at least 3 terms of a quadratic sequence.
        
    Returns:
        str: The general formula of the quadratic sequence.
    """
    r1d1 = series[1] - series[0]
    r1d2 = series[2] - series[1] 
    d2 = r1d2 - r1d1 
    a = d2/2
    b = r1d1 - 3 * a
    c = series[0] - (a + b)
    
    a = remove_decimal(a) 
    b = remove_decimal(b)
    c = remove_decimal(c)
    
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
    """
    Returns the value of the ath term for a sequence defined by ascending powers.

    Args:
        a (int): The term number to be found.
        *args: A tuple containing coefficients for the ascending powers of n.
        
    Returns:
        int: The value of the ath term for the given sequence.
    """
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
    """
    Returns the terms a-b of a sequence defined by ascending powers.

    Args:
        a (int): The starting term number.
        b (int): The ending term number.
        *args: A tuple containing coefficients for the ascending powers of n.
        
    Returns:
        list: A list of terms from ath to bth term in the sequence.
    """
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
    """
    Returns the terms a-b of a sequence defined by ascending powers in a table format.

    Args:
        a (int): The starting term number.
        b (int): The ending term number.
        *args: A tuple containing coefficients for the ascending powers of n.
    """
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

