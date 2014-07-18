#!/usr/bin/env python

try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

version = '0.0.2'

setup(
  name='pyunicode',
  version=version,
  url='http://github.com/Pixelapse/pyunicode',
  download_url='https://github.com/Pixelapse/pyunicode/tarball/v%s' % version,
  author='Shravan Reddy',
  author_email='shravan@pixelapse.com',
  maintainer='Pixelapse',
  maintainer_email='hello@pixelapse.com',
  packages=find_packages(),
  description='Library to deal with common python unicode handling issues',
  long_description=open('README.md').read(),
  license=open('LICENSE').read()
)
