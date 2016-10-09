import numpy as np
import pylab
import timeit
import cmandel


def compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000,plot_filename=None):
	image = np.array(Nx*Ny,dtype=int)
	cmandel.compute_mandelbrot(image,xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time)
	
	image = image.shape(Nx,Ny)
	if(plot_filename != None):
       		np.savetxt(plot_filename,image,fmt='%d') 


	return image

if __name__ == "__main__":
	
	start = timeit.timeit()
	print(start)
	xmin,xmax,ymin,ymax,Nx,Ny = (-4.0,2.0,-3.0,3.0,300,300)
	image = compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time = 1000,plot_filename='test.txt')
	end = timeit.timeit()
	print(end)
	print( (end -start))
	#pylab.imshow(image)
	#pylab.show()
		

