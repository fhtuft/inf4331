#!usr/bin/env python
import sys
import numpy as np

#Used as a enumarator  
class diffToken:
    SAME = "0"
    ADD  = "+"
    SUB  = "-" 

# Implementation of longest common subsequence algorithm
# returns a clousre generator that gives the lcs/ses
def makeLCS(X,Y):
    
    m,n = len(X),len(Y)
    
    c = np.zeros((m+1,n+1),dtype = int)
    b = np.zeros((m,n),dtype = int)
    class dirEnum:
        VERTICAL   = 1
        CORNER     = 2
        HORIZONTAL = 3

    for i in range(b.shape[0]):#Do somethin about this index, prob wrong
        for j in range(b.shape[1]):
            i_c,j_c = i+1,j+1
            if X[i] == Y[j]: 
                #print("==") 
                c[i_c][j_c] = c[i_c-1][j_c-1] + 1
                b[i][j] = dirEnum.VERTICAL
            elif c[i_c-1][j_c] >= c[i_c][j_c-1]:
                #print(">=")
                c[i_c][j_c] = c[i_c-1][j_c]
                b[i][j] = dirEnum.CORNER
            else:
                #print("else")
                b[i][j] = dirEnum.HORIZONTAL

    print(c)
    print(b)

    i,j = m-1,n-1 
    while( i != 0 and j != 0 ):
        if b[i][j] == dirEnum.CORNER:
            #print(X[i] + " corner")
            yield diffToken.SAME,X[i]
            i,j = i-1,j-1
        elif b[i][j] == dirEnum.VERTICAL:
            #print(X[i] + " vertical")
            yield diffToken.SUB,X[i]
            i,j  = i-1,j
        else:
            #print(Y[j] + " horizontal")
            yield diffToken.ADD,Y[j]
            i,j = i,j-1
        
 

def parsArgs():
    assert len(sys.argv) > 2     
   
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
    
    return file1,file2

if __name__ == "__main__" :
    
    if len(sys.argv)  <= 2:
        print("Wrong number of args!")
        sys.exit()

    # Parse the args
    file1,file2 = parsArgs()
    
    # Make a lcs and print out the lcs/ses 
    for token,line in makeLCS(file1,file2):
        if token == diffToken.SAME: 
            print("%s %s" %(diffToken.SAME,line.rstrip('\n')))
        elif token == diffToken.ADD:
            print("%s %s" %(diffToken.ADD,line.rstrip('\n')))
        else: 
            print("%s %s" %(diffToken.SUB,line.rstrip('\n')))
            
    
    
    
       


