[![Get a UNICORN Binance Suite License](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/logo/LUCIT-UBS-License-Offer.png)](https://shop.lucit.services)

[![Github](https://img.shields.io/badge/source-github-cbc2c8)](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python)
[![GitHub Release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/lucit-licensing-python.svg?label=github)](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/LUCIT-Systems-and-Development/lucit-licensing-python/total?color=blue)](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/releases)
[![Conda Release](https://img.shields.io/conda/vn/conda-forge/lucit-licensing-python.svg?color=blue)](https://anaconda.org/conda-forge/lucit-licensing-python)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/lucit-licensing-python.svg?color=blue)](https://anaconda.org/conda-forge/lucit-licensing-python)
[![PyPi Release](https://img.shields.io/pypi/v/lucit-licensing-python?color=blue)](https://pypi.org/project/lucit-licensing-python/)
[![PyPi Downloads](https://pepy.tech/badge/lucit-licensing-python)](https://pepy.tech/project/lucit-licensing-python)
[![License](https://img.shields.io/badge/license-LSOSL-blue)](https://lucit-licensing-python.docs.lucit.tech/license.html)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/lucit_licensing_python.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/lucit-licensing-python.svg)](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/issues)
[![codecov](https://codecov.io/gh/LUCIT-Systems-and-Development/lucit-licensing-python/graph/badge.svg?token=Y95LLP231L)](https://codecov.io/gh/LUCIT-Systems-and-Development/lucit-licensing-python)
[![CodeQL](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/actions/workflows/codeql-analysis.yml)
[![Unit Tests](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/actions/workflows/unit-tests.yml)
[![Build and Publish](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/actions/workflows/build_wheels.yml)
[![Azure Pipelines](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/lucit-licensing-python-feedstock?branchName=main)](https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=15698&branchName=main)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://lucit-licensing-python.docs.lucit.tech)
[![Telegram](https://img.shields.io/badge/chat-telegram-41ab8c)](https://t.me/unicorndevs)
[![Gitter](https://badges.gitter.im/lucit-licensing-python.svg)](https://app.gitter.im/#/room/#lucit-licensing-python:gitter.im)

# LUCIT Licensing Python (Module)

[Description](#description) | [Installation](#installation-and-upgrade) | [Change Log](#change-log) | [How To](#howto) | 
[Wiki](#wiki) | [Social](#social) | [Notifications](#receive-notifications) | 
[Bugs](#how-to-report-bugs-or-suggest-improvements) | 
[Contributing](#contributing) | [Commercial Support](#commercial-support)

Python client module of the LUCIT Licensing Service.

## Description

This module is used to verify [LUCIT software licenses](https://shop.lucit.services/software) and also provides the 
developer with a command line interface to interact with the LUCIT Licensing API. 

If you have already installed modules of LUCIT like the 
[UNICORN Binance Suite](https://www.lucit.tech/unicorn-binance-suite.html), which use the `lucit-licensing-python` 
library, you have already installed the commandline tool `lucitlicmgr` automatically.

### Query contingents of your license
```` 
$ lucitlicmgr --quotas --apisecret bf7df011327d09b70fb0c6bfbc8661x33fdb0c58d42629c94ab35188d8d011ba  --licensetoken 5e84cbd7-acfa-489f-a84d-z7d1b615af40d
````

Example output: 

````
{'quotas': {'instances': {'available': 10, 'free': 10, 'used': 0},
            'ips': {'available': 3, 'free': 2, 'used': 1},
            'resets': {'available': 3, 'free': 3, 'used': 0}},
 'signature': 'e762a949cb0987d6b6e11260a203752c1b2cbf1f8315f3eb6873100e528f8258',
 'timestamp': '1697880811.9013143'}
````

The `apisecret` and the `licensetoken` parameter can also be loaded from an INI file. Simply create the file 
[`lucit_license.ini`](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/lucit-licensing-python/main/example_lucit_license.ini) 
in the app root path or in your home directory in the folder `.lucit` e.g. `C:\Users\Name\.lucit` or 
`/home/Name/.lucit`. with the following content:

````
[LUCIT]
api_secret = bf7df011327d09b70fb0c6bfbc8661x33fdb0c58d42629c94ab35188d8d011ba
license_token = 5e84cbd7-acfa-489f-a84d-z7d1b615af40d
````

Then just use:

```` 
$ lucitlicmgr --quotas
````

Example output: 

````
{'quotas': {'instances': {'available': 10, 'free': 10, 'used': 0},
            'ips': {'available': 3, 'free': 2, 'used': 1},
            'resets': {'available': 3, 'free': 3, 'used': 0}},
 'signature': 'e762a949cb0987d6b6e11260a203752c1b2cbf1f8315f3eb6873100e528f8258',
 'timestamp': '1697880811.9013143'}
 ````

### Query information of your license
```` 
$ lucitlicmgr --info --apisecret bf7df011327d09b70fb0c6bfbc8661x33fdb0c58d42629c94ab35188d8d011ba  --licensetoken 5e84cbd7-acfa-489f-a84d-z7d1b615af40d
````

Example output: 

````
{'license': {'license_holder_email': 'johndoe82@gmail.com',
             'license_holder_name': 'John Doe',
             'licensed_product': 'UNICORN-BINANCE-SUITE',
             'paid_till': '2023-10-24 18:39:03.681745+00:00'},
 'signature': 'e0f7b631006c3480477f81e127729f2ee1489e2dd5dc0ffd7504fb590c4d515a',
 'timestamp': '1697881034.4675057'}
````

The `apisecret` and the `licensetoken` parameter can also be loaded from an INI file. Simply create the file 
[`lucit_license.ini`](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/lucit-licensing-python/main/example_lucit_license.ini) 
in the app root path or in your home directory in the folder `.lucit` e.g. `C:\Users\Name\.lucit` or 
`/home/Name/.lucit`. with the following content:

````
[LUCIT]
api_secret = bf7df011327d09b70fb0c6bfbc8661x33fdb0c58d42629c94ab35188d8d011ba
license_token = 5e84cbd7-acfa-489f-a84d-z7d1b615af40d
````

Then just use:

```` 
$ lucitlicmgr --info
````

Example output: 

````
{'license': {'license_holder_email': 'johndoe82@gmail.com',
             'license_holder_name': 'John Doe',
             'licensed_product': 'UNICORN-BINANCE-SUITE',
             'paid_till': '2023-10-24 18:39:03.681745+00:00'},
 'signature': 'e0f7b631006c3480477f81e127729f2ee1489e2dd5dc0ffd7504fb590c4d515a',
 'timestamp': '1697881034.4675057'}
````


### Release the occupied slots of your quota. 

**Please note:** 
*This will stop ALL active instances. This command can be executed only 3 times every 24 hours.*

```` 
$ lucitlicmgr --reset --apisecret bf7df011327d09b70fb0c6bfbc8661x33fdb0c58d42629c94ab35188d8d011ba  --licensetoken 5e84cbd7-acfa-489f-a84d-z7d1b615af40d
````

Example output: 

````
{'reset': {'status': 'SUCCESSFUL'},
 'signature': '25e8868f963f583f451c0ce1d7bf8daeaaeae4a17db0265adace034232e6f925',
 'timestamp': '1697881249.771824'}
````

The `apisecret` and the `licensetoken` parameter can also be loaded from an INI file. Simply create the file 
[`lucit_license.ini`](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/lucit-licensing-python/main/example_lucit_license.ini) 
in the app root path or in your home directory in the folder `.lucit` e.g. `C:\Users\Name\.lucit` or 
`/home/Name/.lucit`. with the following content:

````
[LUCIT]
api_secret = bf7df011327d09b70fb0c6bfbc8661x33fdb0c58d42629c94ab35188d8d011ba
license_token = 5e84cbd7-acfa-489f-a84d-z7d1b615af40d
````

Then just use:

```` 
$ lucitlicmgr --reset
````

Example output: 

````
{'reset': {'status': 'SUCCESSFUL'},
 'signature': '25e8868f963f583f451c0ce1d7bf8daeaaeae4a17db0265adace034232e6f925',
 'timestamp': '1697881249.771824'}
````

### Test the availability of the Licensing API

```` 
$ lucitlicmgr --test
````

Example output: 

````
{'message': 'Hello World!'}
````

### Use multiple licenses (multi tenant) with profiles
Simply create the file 
[`lucit_license.ini`](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/lucit-licensing-python/main/example_lucit_license.ini) 
in the app root path or in your home directory in the folder `.lucit` e.g. `C:\Users\Name\.lucit` or 
`/home/Name/.lucit`. with the following content:

````
[LUCIT]
api_secret = bf7df011327d09b70fb0c6bfbc8661x33fdb0c58d42629c94ab35188d8d011ba
license_token = 5e84cbd7-acfa-489f-a84d-z7d1b615af40d

[TENANT_A]
api_secret = 62a9efe20be3d038d3be15ea339495629c096ad22762fa7b72ee2df607f194d3
license_token = f829d452-651b-4c6a-89a0-t742a16d0010e
````

Then just use:

```` 
$ lucitlicmgr --info --licenseprofile TENANT_A
````

Example output: 

````
{'license': {'license_holder_email': 'tenant_a@gmail.com',
             'license_holder_name': 'Tenant A',
             'licensed_product': 'UNICORN-BINANCE-SUITE',
             'paid_till': '2023-11-02 13:43:22.723258+00:00'},
 'signature': 'e0f7b631006c3480477f81e127729f2ee1489e2dd5dc0ffd7504fb590c4d515a',
 'timestamp': '1697881034.4675057'}
````

***Note:***
All UNICORN Binance Suite modules also support the use of profiles. Please read the documentation of the respective 
module regarding the parameter `license_profile`. 

### Discover more options
```` 
$ lucitlicmgr --help
````

## Installation and Upgrade
The module requires Python 3.7 or above.

The current dependencies are listed 
[here](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/blob/master/requirements.txt).

If you run into errors during the installation take a look [here](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/wiki/Installation).

### A Cython binary, PyPy or source code based CPython wheel of the latest version with `pip` from [PyPI](https://pypi.org/project/lucit-licensing-python/)
`pip install lucit-licensing-python --upgrade`

### A conda package of the latest release with `conda` from [Anaconda](https://anaconda.org/conda-forge/lucit-licensing-python) via [CONDA-FORGE](https://conda-forge.org).
`conda install -c conda-forge lucit-licensing-python`

`conda update -c conda-forge lucit-licensing-python`

### From source of the latest release with PIP from [GitHub](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python)
#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/archive/$(curl -s https://api.github.com/repos/LUCIT-Systems-and-Development/lucit-licensing-python/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 1.4.0) you determined 
[here](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/releases/latest):

`pip install https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/archive/1.4.0.tar.gz --upgrade`
### From the latest source (dev-stage) with PIP from [GitHub](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://www.python.org)
Download the [latest release](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/releases/latest) 
or the [current master branch](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/archive/master.zip)
 and use:

- ./environment.yml
- ./pyproject.toml
- ./requirements.txt
- ./setup.py

## Change Log
[https://lucit-licensing-python.docs.lucit.tech/changelog.html](https://lucit-licensing-python.docs.lucit.tech/changelog.html)

## Howto
- [How to Obtain and Use a Unicorn Binance Suite License Key and Run the UBS Module According to Best Practice](https://medium.lucit.tech/how-to-obtain-and-use-a-unicorn-binance-suite-license-key-and-run-the-ubs-module-according-to-best-87b0088124a8)

## Project Homepage
[https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python)

## Wiki
[https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/wiki](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/wiki)

## Social
- [Discussions](https://github.com/LUCIT-Systems-and-Development/lucit-licensing/discussions)
- [Gitter](https://app.gitter.im/#/room/#lucit-licensing-python:gitter.im)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)

## Receive Notifications
Follow us on [LinkedIn](https://www.linkedin.com/company/lucit-systems-and-development), 
[X](https://twitter.com/LUCIT_SysDev) or [Facebook](https://www.facebook.com/lucit.systems.and.development)!

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://raw.githubusercontent.com/lucit-systems-and-development/lucit-licensing-python/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python#installation-and-upgrade). If the issue still exists, provide the error trace, OS 
and Python version and explain how to reproduce the error. A demo script is appreciated.

If you don't find an issue related to your topic, please open a new [issue](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/issues)!

[Report a security bug!](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/security/policy)

## Contributing
[LUCIT Licensing Python](https://www.lucit.tech/lucit-licensing-python.html) is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=LUCIT-Systems-and-Development/lucit-licensing-python)](https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/graphs/contributors)

We ![love](https://raw.githubusercontent.com/lucit-systems-and-development/lucit-licensing-python/master/images/misc/heart.png) open source!

## Commercial Support
[![Get professional and fast support](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/support/LUCIT-get-professional-and-fast-support.png)](https://www.lucit.tech/get-support.html)

***Do you need a developer, operator or consultant?*** [Contact us](https://www.lucit.tech/contact.html) for a non-binding initial consultation!
