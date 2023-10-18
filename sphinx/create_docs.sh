#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: sphinx/create_docs.sh
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

# pip install sphinx
# mkdir sphinx
# cd sphinx
# sphinx-quickstart

## edit source/conf.py
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../..'))

# sphinx-apidoc -f -o source/ ../lucit_licensing_python/

# pip install python_docs_theme
## edit source/conf.py:
# html_theme = 'python_docs_theme'

# pip install recommonmark
# add 'recommonmark' to extentions in conf.py

rm source/changelog.md
rm source/copyright.rst
rm source/readme.md
cp ../CHANGELOG.md source/changelog.md
cp ../LICENSE source/copyright.rst
cp ../README.md source/readme.md

make html -d
#python3 -m sphinx source ../docs
