from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "mandelbrot_cython",
    ext_modules = cythonize("*.pyx"),
)
