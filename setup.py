#!/usr/bin/env python

from distutils.core import setup
from tinysou import __version__


setup(
    name='tinysou',
    version=__version__,
    description='Tinysou Python Client',
    author='Hemslo Wang',
    author_email='hemslo.wang@gmail.com',
    url='https://github.com/tinysou/tinysou-python',
    license='MIT',
    packages=['tinysou'],
    install_requires=['requests'],
    tests_require=['nose', 'mock'],
)
