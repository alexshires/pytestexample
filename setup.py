"""
Define Categorise Module
"""
# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="demopytest",
    version="0.1",
    packages=find_packages(),
    license="",
    long_description=open("README.md").read(),
    # package_dir={"": "src"},
)
