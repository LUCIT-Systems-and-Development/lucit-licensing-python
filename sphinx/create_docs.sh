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

rm source/changelog.md
rm source/code_of_conduct.md
rm source/contributing.md
rm source/license.rst
rm source/readme.md
rm source/security.md

cp ../CHANGELOG.md source/changelog.md
cp ../CODE_OF_CONDUCT.md source/code_of_conduct.md
cp ../CONTRIBUTING.md source/contributing.md
cp ../LICENSE source/license.rst
cp ../README.md source/readme.md
cp ../SECURITY.md source/security.md

make html -d
