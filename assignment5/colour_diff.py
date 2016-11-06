#!usr/bin/env python
import sys
import numpy as np

from my_diff import makeLCS

#Used as a enumarator  
class diffToken:
    SAME = "0"
    ADD  = "+"
    SUB  = "-" 



def parsArgs():
    assert len(sys.argv) > 3     
   
    file1 = []
    f = open(sys.argv[1],'r')
    for line in f.readlines():
        file1.append(line)
    f.close()
    file2 =[]
    f = open(sys.argv[2],'r')
    for line in f.readlines():
        file2.append(line)
    f.close()
    f = open(sys.argv[3],'r') #Theme file
    theme = {}
    for line in f.readlines():    
        token,colour = line.split(": ")
        theme[colour.rstrip('\n')] = token 
    f.close()
    
    return file1,file2,theme

if __name__ == "__main__" :
    
    if len(sys.argv)  <= 3:
        print("Wrong number of args!")
        sys.exit()

    # Parse the args
    file1,file2,theme = parsArgs()
    

    # Make a lcs and print out the lcs/ses 
    tokens,lines = makeLCS(file1,file2)
    new_string = ""
    for token,line in zip(tokens,lines):
        colour = "\33["+theme[token] #Add escape seqence
        new_string+= colour
        new_string+= line
        new_string+= "\033[00m" #Restore prev colour output 
    print(new_string) 
    
    
       


