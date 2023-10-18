#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: lucit_licensing_python/cli.py
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


#from lucit_licensing_python.manager import LucitLicensingManager
from manager import LucitLicensingManager

import asyncio
from configparser import ConfigParser, ExtendedInterpolation
from pathlib import Path
import argparse
import logging
import os
import sys
import textwrap


async def cli(lucit_license_manager=None):
    """
        LUCIT License Manager Command Line Interface
    """
    llm = lucit_license_manager if lucit_license_manager is not None else LucitLicensingManager(start=False)
    module_version = llm.get_module_version()
    home_path = f"{Path.home()}{os.sep}"
    config_path = f"{home_path}.lucit{os.sep}"
    log_format = "{asctime} [{levelname:8}] {process} {thread} {module}: {message}"

    parser = argparse.ArgumentParser(
        description=f"LUCIT License Manager {module_version} by LUCIT Systems and Development. All Rights Reserved. ",
        prog=f"lucitlicmgr",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''\
             examples:
                 Query contingents of your license:
                 $ lucitlicmgr --quotas

                 Test the availability of the Licensing API:
                 $ lucitlicmgr --test 
                 
                 Query server timestamp of the Licensing API:
                 $ lucitlicmgr --timestamp 
                 
                 Query the version of the Licensing API:
                 $ lucitlicmgr --version

             additional information:
                 Get a valid license in our store: https://shop.lucit.services/software
                 Author: https://www.lucit.tech
                 Changes: https://lucit-licensing-python.docs.lucit.tech//CHANGELOG.html
                 Documentation: https://lucit-systems-and-development.github.io/lucit-licensing-python
                 Issue Tracker: https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/issues
                 Source: https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python
                 Wiki: https://github.com/LUCIT-Systems-and-Development/lucit-licensing-python/wiki
             '''))

    parser.add_argument('-s', '--apisecret',
                        type=str,
                        help="The LUCIT `api_secret`.",
                        required=False)
    parser.add_argument('-l', '--licensetoken',
                        type=str,
                        help="The LUCIT `license_token`.",
                        required=False)
    parser.add_argument('-cf', '--configfile',
                        type=str,
                        help=f"Specify path including filename to the config file (ex: `~/license_a.ini`). If not "
                             f"provided lucitlicmgr tries to load a `lucit_license.ini` from `{config_path}`.",
                        required=False)
    parser.add_argument('-lf', '--logfile',
                        type=str,
                        help=f'Specify path including filename to the logfile. Default is logfile path is '
                             f'`{config_path}lucit_licensing.log`',
                        required=False)
    parser.add_argument('-ll', '--loglevel',
                        type=str,
                        help='Choose a loglevel. Default: INFO; Options: DEBUG, INFO, WARNING, ERROR and CRITICAL',
                        required=False)
    parser.add_argument('-q', '--quotas',
                        help=f'Query contingents of your license.',
                        required=False,
                        action='store_true')
    parser.add_argument('-t', '--test',
                        help=f'Test the availability of the Licensing API.',
                        required=False,
                        action='store_true')
    parser.add_argument('-ts', '--timestamp',
                        help=f'Query server timestamp of the Licensing API.',
                        required=False,
                        action='store_true')
    parser.add_argument('-v', '--version',
                        help=f'Query the version of the Licensing API.',
                        required=False,
                        action='store_true')
    options = parser.parse_args()

    input_license_token = None
    input_api_secret = None
    input_quotas = False
    input_test = False
    input_timestamp = False
    input_version = False

    if options.logfile is True:
        input_logfile = options.logfile
    else:
        input_logfile = config_path + 'lucit_licensing.log'

    if str(options.loglevel).upper() == "DEBUG":
        input_loglevel = logging.DEBUG
    elif str(options.loglevel).upper() == "INFO":
        input_loglevel = logging.INFO
    elif str(options.loglevel).upper() == "WARN" or str(options.loglevel).upper() == "WARNING":
        input_loglevel = logging.WARNING
    elif str(options.loglevel).upper() == "ERROR":
        input_loglevel = logging.ERROR
    elif str(options.loglevel).upper() == "CRITICAL":
        input_loglevel = logging.CRITICAL
    else:
        input_loglevel = logging.ERROR

    parent_dir = Path(input_logfile).parent
    if not os.path.isdir(parent_dir):
        os.makedirs(parent_dir)
    try:
        logging.basicConfig(level=input_loglevel,
                            filename=input_logfile,
                            format=log_format,
                            style="{")
    except FileNotFoundError as error_msg:
        print(f"File not found: {error_msg}")
    logger = logging.getLogger("lucit_licensing_python")

    if len(sys.argv) <= 1:
        # Exit if no args provided
        parser.print_help()
        sys.exit(1)

    if options.configfile is not None:
        input_config_file = str(options.configfile)
    else:
        input_config_file = f"{config_path}lucit_license.ini"

    if os.path.isfile(input_config_file):
        if input_config_file:
            logger.info(f"Loading configuration file `{input_config_file}`")
            config = ConfigParser(interpolation=ExtendedInterpolation())
            config.read(input_config_file)
            input_api_secret = config['LUCIT']['api_secret']
            input_license_token = config['LUCIT']['license_token']

    # cli args overwrite profile settings
    if options.apisecret is not None:
        input_api_secret = options.apisecret
    if options.licensetoken is not None:
        input_license_token = options.licensetoken
    if options.quotas is not None:
        input_quotas = options.quotas
    if options.test is not None:
        input_test = options.test
    if options.timestamp is not None:
        input_timestamp = options.timestamp
    if options.version is not None:
        input_version = options.version

    if input_quotas is True:
        print(f"{llm.get_quotas(api_secret=input_api_secret, license_token=input_license_token)}")

    if input_test is True:
        print(f"{llm.test()}")

    if input_timestamp is True:
        print(f"{llm.get_timestamp()}")

    if input_version is True:
        print(f"{llm.get_version()}")

if __name__ == "__main__":
    try:
        asyncio.run(cli())
    except KeyboardInterrupt:
        print("\r\nGracefully stopping ...")
