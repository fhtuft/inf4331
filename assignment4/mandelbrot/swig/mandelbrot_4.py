import numpy as np
import pylab
import timeit
import cmandel


def compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000,plot_filename=None):
    
    array = np.zeros(Ny*Nx, dtype='int32', order='C')

    image = cmandel.solver(array,xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time)
       
    return image

if __name__ == "__main__":
	
    start = timeit.timeit()
    print(start)
    xmin,xmax,ymin,ymax,Nx,Ny = (-4.0,2.0,-3.0,3.0,300,300)
    image = compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time = 100)
    end = timeit.timeit()
    print(end)
    print( (end -start))
   		

