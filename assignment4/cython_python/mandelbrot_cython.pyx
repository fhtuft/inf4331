import numpy as np
cimport numpy as np


    
def compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time):

	assert xmin<xmax
	assert ymin<ymax
	assert Nx > 0
	assert Ny > 0


	#image = np.zeros((Ny,Nx),dtype = int,order="C")
	#xes = np.linspace(xmin,xmax,Nx) # x'es
	#yes = np.linspace(ymin,ymax,Ny) # y 'es
	cdef np.ndarray[int,ndim=2] image = np.empty((Ny,Nx),'int32')
	
	cdef np.ndarray[double,ndim=1] xes = np.linspace(xmin,xmax,Nx)
	cdef np.ndarray[double,ndim=1] yes = np.linspace(xmin,xmax,Ny)


	cdef int i,j
	cdef double a,b,x,y

	for j in range(Ny):
		for i in range(Nx):
			a,b = (0.0,0.0)
			x,y = (xes[i],yes[j])
			while(a**2 + b**2 <= 4.0 and  image[j][i] < max_escape_time):
				a,b = a**2 - b**2 + x, 2*a*b + y
				image[j][i] += 1

	return image



