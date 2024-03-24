import re

operatorsDict = {"**": 5, "*": 2, "/": 2, "+": 1, 'u': 6,  '^': 5, "%": 2, '': 4, "-": 1, }
otherDict = {'u': 1}
operators = operatorsDict.keys()
operatorsBracket = list(operators)[:]
operatorsBracket.append('(')

def tokenize(inputExpression):
    return re.split("([()" + ''.join(operators) + "])", inputExpression.replace(" ", ""))

def shunting_yard(inputExpression):
    queue = []
    stack = []

    tokens = tokenize(inputExpression)
    tokens = [x for x in tokens if x]

    x = 0
   
       
  #  print(tokens)

    for x in range(0, len(tokens)):
        if(tokens[x] == '-' and (x == 0 or tokens[x - 1] in operatorsBracket)):
            tokens[x] = 'u'
           
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
            if(token == 'u'):  
                while(len(stack) != 0 and stack[-1] in operators and operatorsDict[stack[-1]] > operatorsDict[token]):
                    queue.append(stack.pop())

                stack.append(token)

                continue
           
            while(len(stack) != 0 and stack[-1] in operators and operatorsDict[stack[-1]] >= operatorsDict[token]):
                queue.append(stack.pop())

            stack.append(token)

    while(len(stack) != 0):
        queue.append(stack.pop())

    return queue

def evaluatePostfix(inputList):
    stack = []

##    print(inputList)
    for token in inputList:
        if(token not in operators):
            stack.append(token)
        else:
            if(token == 'u'):
##                print(stack)
                operand = float(stack.pop())
                stack.append(-1 * operand)

                continue
            operand2 = float(stack.pop())
            operand1 = float(stack.pop())
##            print("current ")
##            print(operand1)
##            print(operand2)
##            print(token)
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

##            print(stack)
               
    return stack[0]

def calc(inputExpression):
    return evaluatePostfix(shunting_yard(inputExpression))
