#!usr/bin/env python3

import numpy as np
import pylab
import timeit

import mandelbrot.maker as mb

print("4.5 user inteface, --help if you need help")

solver = mb.maker()  
#start = timeit.timeit()
image = solver()
#end = timeit.timeit()

pylab.imshow(image)
pylab.show()


    


