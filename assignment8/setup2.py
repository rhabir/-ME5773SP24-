from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension("matmul_cython", ["matmul_cython.pyx"],
              include_dirs=[np.get_include()],
              extra_compile_args=['-std=c99']),
]

setup(
    name="matmul_cython",
    ext_modules=cythonize(extensions),
)
