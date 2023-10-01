#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: lucit-licensing-python.py
#
# Part of ‘UNICORN Binance WebSocket API’
# Project website: https://www.lucit.tech/unicorn-binance-websocket-api.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api
# Documentation: https://unicorn-binance-websocket-api.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-websocket-api/
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2023, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from setuptools import setup
from Cython.Build import cythonize


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    ext_modules=cythonize(
        ['lucit_licensing_python/__init__.py',
         'lucit_licensing_python/manager.py'],
        annotate=False),
    name='lucit-licensing-python',
    version="1.0.0",
    author="LUCIT Systems and Development",
    author_email='info@lucit.tech',
    url="https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python",
    description="LUCIT Licensing Client Module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='LUCIT Synergetic Open Source License',
    install_requires=['cython', 'requests', 'simplejson'],
    keywords='',
    project_urls={
        'Howto': 'https://www.lucit.tech/lucit-licensing-python.html#howto',
        'Documentation': 'https://lucit-licensing-python.docs.lucit.tech',
        'Wiki': 'https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/wiki',
        'Author': 'https://www.lucit.tech',
        'Changes': 'https://lucit-licensing-python.docs.lucit.tech//CHANGELOG.html',
        'Issue Tracker': 'https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/issues',
        'Chat': 'https://gitter.im/unicorn-binance-suite/lucit-licensing-python',
        'Get Support': 'https://www.lucit.tech/get-support.html',
    },
    python_requires='>=3.7.0',
    package_data={'': ['lucit_licensing_python/*.so',
                       'lucit_licensing_python/*.dll']},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        'Intended Audience :: Developers',
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
