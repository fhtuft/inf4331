#!usr/bin/enc python3

import numpy as np
import pylab

import mandelbrot.maker as mb

print("Give option: --color  autumn|pink|copper  ")

solver = mb.maker(function = 2) #vector 
image = solver('contest_image.png')

pylab.show()

    


