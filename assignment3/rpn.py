#!/usr/bin/env python3
import sys 
 
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
                leftOp  = stack.pop()
                rightOp = stack.pop()
                stack.append(str(int(eval(leftOp + token + rightOp))));
            except IndexError as e:
                sys.exit("parse error: Operator + lacking operand")
        elif token == "p":
            try:
                print(stack[-1])
            except IndexError as e:
                print("No value on the stack")
        else:
            sys.exit(token + " :is not a valid token")
            
    # Get input then call the lexer! Input string is split on separor  " "
    parseTokens = input(">").split()

