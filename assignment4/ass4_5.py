#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--xmin', nargs=1,help=' x min')
parser.add_argument('--xmax', nargs=1,help=' x max')
parser.add_argument('--ymin', nargs=1,help=' y min')
parser.add_argument('--ymax', nargs=1,help=' y max')
parser.add_argument('--Nx', nargs=1,help=' Nx')
parser.add_argument('--Ny', nargs=1,help=' Ny')
parser.add_argument('--max_escapte_time', nargs=1,help=' max escape time')
parser.add_argument('--filename', nargs=1,help=' Name of the output file')


#xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time = 100,plot_filename=
args = parser.parse_args()

print(args)

#print(args.accumulate(args.integers))


