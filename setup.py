#!/usr/bin/env python

"""Setup script for the `humanfriendly` package."""

# Author: Peter Odding <peter@peterodding.com>
# Last Change: January 19, 2016
# URL: https://humanfriendly.readthedocs.org

# Standard library modules.
import codecs
import os
import re
import sys

# De-facto standard solution for Python packaging.
from setuptools import find_packages, setup


def get_contents(filename):
    """Get the contents of a file relative to the source distribution directory."""
    directory = os.path.dirname(os.path.abspath(__file__))
    pathname = os.path.join(directory, filename)
    with codecs.open(pathname, 'r', 'utf-8') as handle:
        return handle.read()


def get_version(filename):
    """Extract the version number from a Python module."""
    contents = get_contents(filename)
    metadata = dict(re.findall('__([a-z]+)__ = [\'"]([^\'"]+)', contents))
    return metadata['version']


# Conditional importlib dependency for Python 2.6 and 3.0.
install_requires = []
if sys.version_info[:2] <= (2, 6) or sys.version_info[:2] == (3, 0):
    install_requires.append('importlib')

setup(
    name='humanfriendly',
    version=get_version('humanfriendly/__init__.py'),
    description="Human friendly output for text interfaces using Python",
    long_description=get_contents('README.rst'),
    url='https://humanfriendly.readthedocs.org',
    author='Peter Odding',
    author_email='peter@peterodding.com',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points=dict(console_scripts=[
        'humanfriendly = humanfriendly.cli:main'
    ]),
    test_suite='humanfriendly.tests',
    tests_require=[
        'capturer >= 2.1',
        'coloredlogs >= 2.0',
    ],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
        'Topic :: System :: Systems Administration',
        'Topic :: Terminals',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ])
