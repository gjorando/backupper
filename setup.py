#!/usr/bin/env python3

from setuptools import setup, find_packages

import os
import re
import sys

# Inspired by docker-compose setup.py
def read(*tree):
    with open(os.path.join(os.path.dirname(__file__), *tree), encoding='utf-8') as f:
        return f.read()

def version(*tree):
    init_file = read(*tree)
    version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", init_file, re.M)
    if version:
        return version.group(1)
    raise RuntimeError("No version string found in {}.".format(os.path.join(*tree)))

def requirements(*tree):
    requirements_file = read(*tree)
    return [r for r in requirements_file.split("\n") if r != ""]

setup(
    name = "backupper",
    version = version("backupper", "__init__.py"),
    author = "Guillaume Jorandon",
    author_email = "jorandon@gmail.com",
    description = "Easy and configurable backup tool",
    long_description = "TODO",
    license = "MIT",
    url = "https://github.com/dolfinsbizou/backupper",
    packages = find_packages(exclude=["tests"]), # Yeah I don't have a test package (yet) but I should totally have one
    install_requires=requirements("requirements.txt"),
    entry_points = {
        'console_scripts': ['backupper=backupper.cli:main']
    },
    classifiers =[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Archiving :: Backup'
    ]
)
