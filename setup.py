import os
from setuptools import setup
from setuptools import find_packages
from pymed.version import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pymed",
    version=__version__,
    author="Kexin Quan",
    author_email="kequan@ucsd.com",
    description=("Python library for access to Updated PubMed"),
    license="MIT",
    keywords="PubMed PMC",
    url="https://github.com/kexinquan/pymed",
    # packages=find_packages(),
    packages=["pymed"],
    install_requires=["requests>=2.20.0"],
    tests_require=["pytest"],
    long_description_content_type="text/markdown",
    long_description=read("README.md"),
    classifiers=[
        "Topic :: Utilities",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
