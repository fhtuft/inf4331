#!/usr/bin/env python3

from numpy import *

max_iters = 100
size = 10
x_center = 0.0
y_center = 0.0

image = zeros((size,size));

for j in range(size):
    for i in range(size):
        a,b = (0.0,0.0)
        x,y = ( x_center + 4.0*float(i-size/2)/size,y_center + 4.0*float(j-size/2)/size) 
        
        while(a**2 + b**2 <= 4.0 and  image[i][j] < max_iters):
            a,b = a**2 - b**2 + x, 2*a*b + y
            image[i][j] += 1
        


