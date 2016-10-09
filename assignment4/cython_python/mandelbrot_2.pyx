#!/usr/bin/env python3

import numpy as np
import pylab
import timeit

def compute_mandelbrot_vec(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000,plot_filename=None):
    
    assert xmin<xmax
    assert ymin<ymax
    assert Nx > 0
    assert Ny > 0


    x,y = np.meshgrid(np.linspace(xmin,xmax,Nx) ,np.linspace(ymin,ymax,Ny)) 
    a = x + np.zeros((Ny,Nx))
    b = y + np.zeros((Ny,Nx))
    
    image = 1 + np.zeros((Ny,Nx))

    for i in range(max_escape_time):
        mask = ((a*a + b*b) <= 2.0)
        image[mask] = i  
        a,b = a*a - b*b + x, 2*a*b + y

    if(plot_filename != None):
       np.savetxt(plot_filename,image,fmt='%d') 

    return image
     

    
def compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000,plot_filename=None):

    assert xmin<xmax
    assert ymin<ymax
    assert Nx > 0
    assert Ny > 0


    image = np.zeros((Ny,Nx),dtype = int,order="C")
    xes = np.linspace(xmin,xmax,Nx) # x'es
    yes = np.linspace(ymin,ymax,Ny) # y 'es
    

    for j in range(image.shape[0]):
        for i in range(image.shape[1]):
            a,b = (0.0,0.0)
            x,y = (xes[i],yes[j])
            #x,y = ( -1 + 4.0*float(i-Nx/2)/Nx,0 + 4.0*float(j-Ny/2)/Ny)
            #print(x,y)
            while(a**2 + b**2 <= 4.0 and  image[j][i] < max_escape_time):
                a,b = a**2 - b**2 + x, 2*a*b + y
                image[j][i] += 1
    
    if(plot_filename != None):
       np.savetxt(plot_filename,image,fmt='%d') 

    return image


if __name__ == "__main__":

    xmin,xmax,ymin,ymax,Nx,Ny = (-4.0,2.0,-3.0,3.0,300,300)
    image = compute_mandelbrot_vec(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time = 100,plot_filename='test.txt')
    

    pylab.imshow(image)
    pylab.show()
