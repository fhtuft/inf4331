#!usr/bin/env python

import re
import sys

assert  sys.version_info >= (3,0)


def argParser():

    if len(sys.argv) <= 3:
        sys.exit()
    
    # Read and parse fileinput
    returnList =  []
    f = open(sys.argv[1],'r') #Syntex file
    syntax = []
    for line in f.readlines():
        regex,token = line.split(": ")
        syntax.append((regex,token.rstrip('\n'))) #Get rid of newline        
    f.close()
    f = open(sys.argv[2],'r') #Theme file
    theme = {}
    for line in f.readlines():    
        token,colour = line.split(": ")
        theme[colour.rstrip('\n')] = token 
    f.close()
    f = open(sys.argv[3],'r') #Source file
    sourceFile = f.read()
    f.close()
    
    return syntax,theme,sourceFile
   

def lexer(syntex,string):

    pos = 0

    while pos < len(string):
                
        for pattern,token in syntex:
            regex = re.compile("r"+pattern)
            match = re.match(string,regex,pos)
            if match:
                pos = match.end(0)
                yield token,string
        
        
 
    
syntax,theme,sourceFile = argParser()
print(syntax)
print(theme)
for i in lexer(None,None):
    print(i)
    

#print(sourceFile) 
        





