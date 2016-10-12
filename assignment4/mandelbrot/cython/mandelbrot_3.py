import numpy as np
import pylab
import timeit
import cython.mandelbrot_cython


def compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000,plot_filename=None):
    image = mandelbrot_cython.compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time)
	
    if(plot_filename != None):
        np.savetxt(plot_filename,image,fmt='%d') 
    
    return image

if __name__ == "__main__":
	
    start = timeit.timeit()
    print(start)
    xmin,xmax,ymin,ymax,Nx,Ny = (-4.0,2.0,-3.0,3.0,300,300)
    image = compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time = 100,plot_filename='test.txt')
    end = timeit.timeit()
    print(end)
    print( (end -start))
    #pylab.imshow(image) 
    #pylab.show()
		

