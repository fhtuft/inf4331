#!/usr/bin/env python

from distutils.core import setup

setup(name='mandelbrot',
      version='1.0',
      description='compute the mandelbrot set',
      author='Me',
      packages=['mandelbrot', 'mandelbrot.serial','mandelbrot.vector','mandelbrot.cython','mandelbrot.swig','mandelbrot.test'],
     )
