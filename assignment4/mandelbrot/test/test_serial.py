import pytest

import serial.mandelbrot_1 as mb


def test_outside():
	xmin,xman,ymin,ymax = (3.0,4.0,3.0,4.0)
	Nx,Ny = (300,300)
	image = mb.compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny)
	
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			if image[y][x] != 1:
				return
	assert False

def test_inside():
	xmin,xman,ymin,ymax = (-1.0,1.0,-1.0,1.0) #Is this inside ?
	Nx,Ny = (300,300)
	image = mb.compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny)
	for x in range(image.shape[0]):
		for y in range(image.shape[1]):
			if image[y][x] == 1:
				return
	assert False
	
if __name__ == "__main__":

    test_outside()



