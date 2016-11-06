#!usr/bin/env python
import sys
import numpy as np

#Used as a enumarator  
class diffToken:
    SAME = "0"
    ADD  = "+"
    SUB  = "-" 

# Implementation of longest common subsequence algorithm
# returns a generator
def makeLCS(X,Y):
    
    m,n = len(X),len(Y)
   
    print("m%d n%d" %(m,n)) 
    c = np.zeros((m+1,n+1),dtype = int)
    b = np.zeros((m,n),dtype = int)
    class dirEnum:
        CORNER     = 1
        VERTICAL   = 2
        HORIZONTAL = 3

    for i in range(b.shape[0]):#Do somethin about this index, prob wrong
        for j in range(b.shape[1]):

            ic,jc = i+1,j+1
            if X[i] == Y[j]: 
                print("== " + str(i) + ","+str(j)) 
                c[ic][jc] = c[ic-1][jc-1] + 1
                b[i][j] = dirEnum.CORNER
            elif c[ic-1][jc] >= c[ic][jc-1]:
                print(">= " + str(i) + "," + str(j))
                c[ic][jc] = c[ic-1][jc]
                b[i][j] = dirEnum.VERTICAL
            else:
                print("else " + str(i) + "," + str(j))
                c[ic][jc] = c[ic][jc-1]
                b[i][j] = dirEnum.HORIZONTAL

    print(c)
    print(b)


    i,j = m-1,n-1
    lines,tokens = [],[]
    while(i >= 0 and j >= 0):
        
        if b[i][j] == dirEnum.CORNER:
            tokens.insert(0,diffToken.SAME)
            lines.insert(0,X[i])
            i,j = i-1,j-1
        elif b[i][j] == dirEnum.VERTICAL:
            tokens.insert(0,diffToken.SUB)
            lines.insert(0,X[i])
            i = i-1
        else:
            tokens.insert(0,diffToken.ADD)
            lines.insert(0,Y[j])
            j = j-1
     
    return tokens,lines  
    #def getList(i,j):
    #    if i < 0 or j < 0:
    #        pass
    #    if b[i][j] == dirEnum.CORNER:
    #        getList(i-1,j-1)
    #        yield diffToken.SAME,X[i]
    #    elif b[i][j] == dirEnum.VERTICAL:
    #        getList[i-1][j]
    #        yield diffToken.SUB,X[i]
    #    else:
    #        getList[i][j-1]
    #        yield diffToken.SUB,Y[j]
     
    #return getList(m-1,n-1)
''''
    i,j = 0,0 
    while( i < m and j < n ):
        if b[i][j] == dirEnum.CORNER:
            #print(X[i] + " corner")
            yield diffToken.SAME,X[i]
            i,j = i+1,j+1
        elif b[i][j] == dirEnum.VERTICAL:
            #print(X[i] + " vertical")
            yield diffToken.SUB,X[i]
            i,j  = i+1,j
        else:
            #print(Y[j] + " horizontal")
            yield diffToken.ADD,Y[j]
            i,j = i,j+1
        
 '''

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
    
    #gt = makeLCS(file1,file2)   
    
    #for token,line in gt:
    #    print(line) 

    # Make a lcs and print out the lcs/ses 
    tokens,lines = makeLCS(file1,file2)
    for token,line in zip(tokens,lines):
        if token == diffToken.SAME: 
            print("%s %s" %(diffToken.SAME,line.rstrip('\n')))
        elif token == diffToken.ADD:
            print("%s %s" %(diffToken.ADD,line.rstrip('\n')))
        else: 
            print("%s %s" %(diffToken.SUB,line.rstrip('\n')))
    
    
    
       


