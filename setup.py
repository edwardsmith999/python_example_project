#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='python_example_project',
    version='0.2',
    description='Demonstrates basic python project structure, documentation and continuous integration',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.13.1'
    ]
)
