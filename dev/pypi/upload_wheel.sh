#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/upload_wheel.sh
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
#
# create this file:
# ~/.pypirc

python3 -m twine upload dist/*
