import string

def baseConverter(num, base):
    digs = string.digits + string.ascii_letters
    if num < 0:
        sign = -1
    elif num == 0:
        return digs[0]
    else:
        sign = 1

    num *= sign
    digits = []

    while num:
        digits.append(digs[num % base])
        num = num // base

    if sign < 0:
        digits.append("-")

    digits.reverse()
    return int("".join(digits))

def IntToBinary(num):
    return bin(num)[2:]
def BinaryToInt(num):
    return int(str(num), 2)
def IntToHex(num):
    return hex(num)[2:]
def HexToInt(num):
    return int(str(num, 2))
def binaryToHex(num):
    base10 = BinaryToInt(num)
    base16 = IntToHex(base10)
    return base16
def HexToBinary(num):
    base10 = HexToInt(num)
    base2 = IntToBinary(base10)
    return base2
    
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
