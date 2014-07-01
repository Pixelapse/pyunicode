#!/usr/bin/env python

try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

import pyunicode

setup(
  name='pyunicode',
  version=pyunicode.__version__,
  url='http://github.com/Pixelapse/pyunicode',
  author='Shravan Reddy',
  author_email='shravan@pixelapse.com',
  maintainer='Pixelapse',
  maintainer_email='hello@pixelapse.com',
  packages=find_packages(),
  long_description=open('README.md').read(),
  license=open('LICENSE').read()
)
