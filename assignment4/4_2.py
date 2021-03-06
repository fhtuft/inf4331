#!usr/bin/env python3

import numpy as np
import pylab
import timeit

import mandelbrot.maker as mb

print("4.2 vector code")

solver = mb.maker(function = 2,max_escape_time=1000)  
start = timeit.timeit()
image = solver()
end = timeit.timeit()
print(end - start)
pylab.imshow(image)
pylab.show()


    


