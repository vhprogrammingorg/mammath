import tabulate
from .helper import remove_decimal

"""
SEQUENCES
"""

def sequence_checker(*terms):
    """
    Checks the degree / type of sequence.

    Args:
        *terms (int/float): The terms of the sequence.
        
    Returns:
        str: The type or degree of the sequence.
    """
    if len(terms) < 3:
        return "Insufficient data to determine sequence type"
    
    if all((terms[i+1] - terms[i] == terms[1] - terms[0]) for i in range(len(terms) - 1)):
        return "Arithmetic"
    
    if all((terms[i+1] / terms[i] == terms[1] / terms[0]) for i in range(len(terms) - 1)):
        return "Geometric"
    
    differences = [terms[i+1] - terms[i] for i in range(len(terms) - 1)]
    second_differences = [differences[i+1] - differences[i] for i in range(len(differences) - 1)]
    
    if all(d == second_differences[0] for d in second_differences):
        return "Quadratic"
    
    degree = 2
    while len(set(second_differences)) > 1:
        degree += 1
        differences = second_differences
        second_differences = [differences[i+1] - differences[i] for i in range(len(differences) - 1)]
    
    return f"Polynomial of degree {degree}"

def nth_term_value(formula, n):
    """
    Returns the value of the nth term in a sequence defined by the formula.
    
    Args:
        formula (str): The formula of the sequence with variable "n".
        n (int): The term number to be found.
        
    Returns:
        int: The value of the nth term in the sequence.
    """
    formula = formula.replace("n", str(n))
    return eval(formula)

def terms_in_range(formula, start, end):
    """
    Returns the terms from start to end in a sequence defined by the formula.
    
    Args:
        formula (str): The formula of the sequence with variable "n".
        start (int): The starting term number.
        end (int): The ending term number.
        
    Returns:
        list: A list of terms from start to end in the sequence.
    """
    return [nth_term_value(formula, i) for i in range(start, end + 1)]

def terms_table(formula, start, end):
    """
    Returns the terms from start to end in a sequence defined by the formula in a table format.
    
    Args:
        formula (str): The formula of the sequence with variable "n".
        start (int): The starting term number.
        end (int): The ending term number.
    """
    terms = [[i, nth_term_value(formula, i)] for i in range(start, end + 1)]
    headers = ["Term", "Value"]
    print(tabulate.tabulate(terms, headers=headers))

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
    return nth_term_value(eq, a)

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
    return terms_in_range(eq, a, b)

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
    return terms_table(eq, a, b)
    
def partial_harmonic_series(n):
    """
    Returns the sum of the first n terms of the harmonic series.
    
    Args:
        n (int): The number of terms to sum.
    """
    return sum(1 / i for i in range(1, n + 1))

def sum_arithmetic_sequence(n, *terms):
    """
    Returns the sum of the first n terms of an arithmetic sequence given the starting terms
    
    Args:
        n (int): The number of terms to sum.
        *terms: A list of the first terms of the arithmetic sequence
    """
    terms = list(terms)
    d = terms[1]-terms[0]
    return n*(2*terms[0]+(n-1)*d)/2

def sum_geometric_sequence(n, *terms):
    """
    Returns the sum of the first n terms of a geometric sequence given the starting terms
    
    Args:
        n (int): The number of terms to sum.
        *terms: A list of the first terms of the geometric sequence
    """
    terms = list(terms)
    r = terms[1]/terms[0]
    return (terms[0]*(1-r**n))/(1-r)

def infinite_geometric_sum(*terms):
    """
    Returns the sum of an infinite geometric series

    Args:
        *terms: A list of the first terms of the geometric series
    """
    terms = list(terms)
    return terms[0]/(1-terms[1]/terms[0])

"""
END OF SEQUENCES
"""

