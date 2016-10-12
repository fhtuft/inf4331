#!/usr/bin/env python3
import argparse
import sys
import pylab

import serial.mandelbrot_1 as serielPy
import vector.mandelbrot_2 as vecPy
import cython.mandelbrot_3 as cyPy

def maker(xim = -1.0,xmax = 1.0 , ymin = -1.0,ymax = 1.0,Nx = 300, Ny = 300, max_escapte_time = 100, filename = None, function = 1): 
	
	parser = argparse.ArgumentParser(description='Process some integers.')

	parser.add_argument('--xmin', nargs=1,help=' x min')
	parser.add_argument('--xmax', nargs=1,help=' x max')
	parser.add_argument('--ymin', nargs=1,help=' y min')
	parser.add_argument('--ymax', nargs=1,help=' y max')
	parser.add_argument('--Nx', nargs=1,help=' Nx')
	parser.add_argument('--Ny', nargs=1,help=' Ny')
	parser.add_argument('--max_escapte_time', nargs=1,help=' max escape time')
	parser.add_argument('--filename', nargs=1,help=' Name of the output file')
	parser.add_argument('--implementation', nargs=1,help=' witch of 3 implementations to use')


	args = parser.parse_args()

	xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,plot_filename = (-4.0,2.0,-3.0,3.0,300,300,100,'test.txt')
	
	if(args.xmin != None):
		xmin = float(args.xmin[0])
	if(args.xmax != None):
		xmax = float(args.xmax[0])
	if(args.ymin != None):
		ymin = float(args.ymin[0])
	if(args.xmax != None):
		xmax = float(args.ymax[0])

	if(args.Nx != None):
		Nx = int(args.Nx[0])
	if(args.Ny != None):
		Ny = int(args.Ny[0])

	if(args.max_escapte_time != None):
		max_escape_time = int(arg.max_escape_time[0])

	if(args.filename != None):
		plot_filename = args.filename[0]

	if(args.implementation != None):
		function = int(args.implementation[0])



	mandel_compute = serielPy.compute_mandelbrot
	if(function == 2):
		mandel_compute = vecPy.compute_mandelbrot
	elif(function == 3):
		mandel_compute = cyPy.compute_mandelbrot
		

	def inner_compute():
		return mandel_compute(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,plot_filename)
	
	return inner_compute


if __name__ == "__main__":

    mandel = maker()
    image = mandel()
    print(image)
    pylab.imshow(image,cmap = 'autumn')
    pylab.show()


