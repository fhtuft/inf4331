#!usr/bin/env python

import sys
import numpy as np

class FileStr:
    def __init__(self,lineCount,fStr):
        self.lineCount = lineCount
        self.fStr = fStr


# Implementation of longest common subsequence algorithm
# from Intro to algorithms 3.Edition  p.394. Async runtime: O(mn) 
def computeLCS(X,Y):
    
    m,n = len(X),len(Y)
    
    c = np.zeros(m+1,n+1)
    b = np.array(m+1,n+1,dtype = 'c')
    # b uses 3 chars 'V': Vertical, 'C' : Corner, 'H': Horizontal
    # this are the arrows in the algo.


    for i in range(1,c.dim[0]):
        for j in range(1,c.dim[1]):
            i_c,j_c = i+1,j+1
            if X[i] == Y[j]:  
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'C'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'V'
            else:
                b[i][j] = 'H'


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

    file1,file2 = parsArgs()
    
       


