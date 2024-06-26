from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

exts = []
mod1 = Extension('module',
              sources=['module.pyx'],
              include_dirs=[np.get_include()],  # include header from numpy.      
              extra_compile_args=['-std=c99'],  # enables flag for c99 standard.
              libraries=['m'], # Link to math library.
    )


setup(
    ext_modules=cythonize( mod1, annotate=True ),
)