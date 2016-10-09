#!/usr/bin/env python3
import argparse
import sys
import pylab
sys.path.insert(0, './cython_python')

import serial_python.mandelbrot_1 as serialPy
import vector_python.mandelbrot_2 as vecPy
#import cython_python.mandelbrot_3 as cyPy


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



#xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time = 100,plot_filename=
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

image = None
if(args.implementation != None):
	imlp = args.implementation[0]
	#Not very pythonic..
	if(impl == 1):
		image =serialPy.compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,plot_filename)
	elif(impl == 2):
		image =vecPy.compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,plot_filename) 	
	elif(impl == 3):
		image =cyPy.compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,plot_filename) 	
		
	else:
		print("Not a implementation")
else:
	image  = serialPy.compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,plot_filename)	

pylab.imshow(image)
pylab.show()
print(args)
print(type(args.ymin))

#print(args.accumulate(args.integers))


