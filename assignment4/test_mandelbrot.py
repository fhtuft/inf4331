import pytest

import numpy as np
import pylab
import timeit

import mandelbrot.serial.mandelbrot_1 as serielPy


# Assert failure if this region is outside. This one should fail now!
def test_outside():
    xmin,xmax,ymin,ymax,Nx,Ny = (3.0,4.0,3.0,4.0,300,300)
    image = serielPy.compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time = 1000) 
    pylab.imshow(image)
    pylab.show()	
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[y][x] > 1:
                return
    assert False

# Have not found the inside, has to try with other values
def test_inside():
    xmin,xmax,ymin,ymax,Nx,Ny = (-0.1,0.1,-0.1,0.1,300,300)
    image = serielPy.compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time = 100) 
    pylab.imshow(image)
    pylab.show()	
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[y][x] > 1:
                assert False
    
	
if __name__ == "__main__":
    test_inside()
    #test_outside()



