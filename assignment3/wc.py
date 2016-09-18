#!/usr/bin/env python3
import sys
import fileinput

assert sys.version_info >= (3,0)
wordcount = 0
 
try:
    for line in fileinput.input():
        wordcount += len(line.split())
except IsADirectoryError as e:
    pass

print(wordcount) 
    
