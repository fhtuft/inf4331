#! /usr/bin/env python
#From http://scipy-cookbook.readthedocs.io/items/SWIG_NumPy_examples.html
# System imports
from distutils.core import *
from distutils      import sysconfig

import numpy

try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

_cmandel = Extension("_cmandel",
                   ["cmandel.i","cmandel.c"],
                   include_dirs = [numpy_include],
                   )

setup(  name        = "mandelbrot",
        description = "calculata mandebrot",

        author      = "Finn-Haakon",
        version     = "1.0",
        ext_modules = [_cmandel]
        )
