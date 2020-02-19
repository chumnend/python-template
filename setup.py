import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="template",
    version="1.0.0",
    author="Nicholas Chumney",
    author_email="nchumney@hotmail.com",
    description=("A python template"),
    long_description=read('README.md'),
    packages=find_packages(),
)