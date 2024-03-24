import re

operatorsDict = {"*": 2, "/": 2, "+": 1, '^': 5, "%": 2, '': 4, "-": 1}
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
            while(len(stack)-1 != 0 and stack[-1] != "("):
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
    operand1 = ""
    operand2 = ""
    for token in inputList:
        if(token not in operators):
            stack.append(token)
        else:
            try:
                operand2 = float(stack.pop())
                operand1 = float(stack.pop())
            except:
                pass
            
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
                
            if(token == "**"):
                stack.append(operand1 ** operand2)
                
    return stack[0]

def evaluateExpression(inputExpression):
    return evaluatePostfix(shunting_yard(inputExpression))
