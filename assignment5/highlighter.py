#!usr/bin/env python
import re
import sys

assert  sys.version_info >= (3,0)



def argParser():
    
    # Read and parse fileinput
    returnList =  []
    f = open(sys.argv[1],'r') #Syntex file
    syntax = []
    for line in f.readlines():
        regex,token = line.split(": ")
        regex = re.compile(regex)
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
        for regex,token in syntex:
            match = regex.match(string,pos)
            if match:
                yield token,string[pos:match.end(0)]
                pos = match.end(0)
                break
        #No match found 
        yield None,string[pos:pos+1]
        pos += 1
    
        
if __name__ == "__main__":
   
    
    if len(sys.argv) <= 3:
        print("Wrong number of args: regex, theme, source")
        sys.exit()

 
    syntax,theme,sourceFile = argParser()
    #print(syntax)
    #print(theme)
    new_string = ""
    for token,string in lexer(syntax,sourceFile):
        if token:
            colour = "\33["+theme[token] #Add escape seqence
            new_string+= colour
            new_string+= string
            new_string+= "\033[00m" #Restore prev colour output 
        else:
            new_string+=string
    
    print(new_string)    

        





