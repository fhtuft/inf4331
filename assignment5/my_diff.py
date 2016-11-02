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
    
    c = np.zeros(m+1,n+1)
    b = np.array(m+1,n+1,dtype = 'c')
    # b uses 3 chars 'V': Vertical, 'C' : Corner, 'H': Horizontal

    class 

    for i in range(1,c.dim[0]):#Do somethin about this index, prob wrong
        for j in range(1,c.dim[1]):
            i_c,j_c = i+1,j+1
            if X[i] == Y[j]:  
                c[i_c][j_c] = c[i_c-1][j_c-1] + 1
                b[i][j] = 'C'
            elif c[i_c-1][j_c] >= c[i_c][j_c-1]:
                c[i_c][j_c] = c[i_c-1][j_c]
                b[i][j] = 'V'
            else:
                b[i][j] = 'H'
    
        def getLCS(i,j):
            if i == 0 or j == 0:
                return 
            if b[i][j] == 'C':
                getLCS(i-1,j-1)
                yield diffToken.SAME,X[i]
            elif b[i][j] == 'V':
                getLCS(i-1,j)
                yield diffToken.SUB,X[i]
            else:
                getLCS(i,j-1)
                yield diffToken.ADD,X[i]
        
    return getLCS(m,n)     
 

def parseArgs():
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
    for toke,line in makeLCS(file1,file2):
        if token == diffToken.SAME: 
            print("%s %s" %(diffToken.SAME,line))
        elif token == diffToken.ADD
            print("%s %s" %(diffToken.ADD,line))
        else: 
            print("%s %s" %(diffToken.SUB,line))
            
    
    
    
       


