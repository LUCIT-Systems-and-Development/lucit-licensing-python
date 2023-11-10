#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Project website: https://www.lucit.tech/lucit-licensing-python.html
# Github: https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python
# Documentation: https://lucit-licensing-python.docs.lucit.tech
# PyPI: https://pypi.org/project/lucit-licensing-python/
#
# License: LSOSL - LUCIT Synergetic Open Source License
# https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/blob/main/LICENSE
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2023-2023, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.

from setuptools import setup
from Cython.Build import cythonize

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    ext_modules=cythonize(
        ['lucit_licensing_python/__init__.py',
         'lucit_licensing_python/cli.py',
         'lucit_licensing_python/exceptions.py',
         'lucit_licensing_python/manager.py'],
        annotate=False),
    name='lucit-licensing-python',
    version="1.5.0",
    author="LUCIT Systems and Development",
    author_email='info@lucit.tech',
    url="https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python",
    description="LUCIT Licensing Client Module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='LSOSL - LUCIT Synergetic Open Source License',
    install_requires=['Cython', 'requests', 'simplejson'],
    keywords='',
    project_urls={
        'Documentation': 'https://lucit-licensing-python.docs.lucit.tech',
        'Wiki': 'https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/wiki',
        'Author': 'https://www.lucit.tech',
        'Changes': 'https://lucit-licensing-python.docs.lucit.tech/changelog.html',
        'License': 'https://lucit-licensing-python.docs.lucit.tech/license.html',
        'Issue Tracker': 'https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/issues',
        'Chat': 'https://app.gitter.im/#/room/#lucit-licensing-python:gitter.im',
        'Get Support': 'https://www.lucit.tech/get-support.html',
    },
    python_requires='>=3.7.0',
    package_data={'': ['lucit_licensing_python/*.so',
                       'lucit_licensing_python/*.dll']},
    entry_points={
        "console_scripts": [
            "lucitlicmgr  = lucit_licensing_python.cli:main",
        ]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: Other/Proprietary License",
        'Intended Audience :: Developers',
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
