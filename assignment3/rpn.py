#!/usr/bin/env python3
import sys 
from math import sqrt as v
from math import sin,cos
 
assert sys.version_info >= (3,0)  

#Make a empty stack
stack = []

#Get the string to parse, is list
parseTokens = sys.argv[1:]

#Loop forever 
while True:
    
    for token in parseTokens:
    
        if token.isdigit():
            stack.append(token) 
        # Test if it is one of the binary operators
        elif token == "+" or token == "*" or token == "/":
            try:
                rightOp  = stack.pop()
                leftOp = stack.pop()
                stack.append(str(eval(leftOp + token + rightOp)));
            except IndexError as e:
                sys.exit("parse error: Operator + lacking operand")
        # Test if token is a unary operator
        elif token == "v" or token == "sin" or token == "cos":
            try:
                op = stack.pop()
                stack.append(str(eval(token + "(" + op + ")")))
            except IndexError as e:
                sys.exit("parse error: Operator lacking operand")
        # Test if token is print command 
        elif token == "p":
            try:
                print(stack[-1])
            except IndexError as e:
                print("No value on the stack")
        else:
            sys.exit(token + " :is not a valid token")
            
    # Get input then call the lexer! Input string is split on separor  " "
    parseTokens = input(">").split()

