#!/usr/bin/env python3

#from the lecture slides
from distutils.core import setup
name='my_unit_testing'

setup(name=name,
      version='0.1',
      py_modules=[name],       
      scripts=[name + '.py'],  
      )
