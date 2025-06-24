# setup.py
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy

extensions = [
    Extension(
        "stocproc.stocproc_c",
        ["stocproc/stocproc_c.pyx"],
        include_dirs=[numpy.get_include()],
    )
]

setup(
    name="stocproc",
    version="1.1.2",
    description="Stochastic Processes in Python",
    author="cimatosa",
    packages=["stocproc"],
    ext_modules=cythonize(extensions, language_level=3),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "fastcubicspline",
    ],
)
