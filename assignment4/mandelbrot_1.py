#!/usr/bin/env python

import numpy as np
import pylab



def compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000,plot_filename=None):

    assert xmin<xmax
    assert ymin<ymax
    assert Nx > 0
    assert Ny > 0


    image = np.zeros((Ny,Nx),dtype = int,order="C")
    xes = np.linspace(xmin,xmax,Nx) # x'es
    yes = np.linspace(ymin,ymax,Ny) # y 'es
    
    print(xes)

    for j in range(image.shape[0]):
        for i in range(image.shape[1]):
            a,b = (0.0,0.0)
            x,y = (xes[i],yes[j])
            while(a**2 + b**2 <= 4.0 and  image[j][i] < max_escape_time):
                a,b = a**2 - b**2 + x, 2*a*b + y
                image[j][i] += 1
    
    if(plot_filename != None):
       np.savetxt(plot_filename,image,fmt='%d') 

    return image

xmin,xmax,ymin,ymax,Nx,Ny = (0.0,200.0,0.0,200.0,50,50)


image = compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,plot_filename='test.txt')

pylab.imshow(image)
pylab.show()
