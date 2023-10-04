#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: test.py
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

import asyncio
import logging
import time
import pprint
from lucit_licensing_python.manager import Manager


class LTC:
    def __init__(self, api_secret=None, license_token=None):
        self.api_secret = api_secret
        self.license_token = license_token
        self.llm = Manager(api_secret=api_secret, license_token=license_token,
                           program_used="unicorn-binance-websocket-api", start=False)
        self.sigterm = False

    def close(self):
        self.sigterm = True
        return self.llm.close()

    async def test_licensing(self):
        while self.sigterm is False:
            start_time = time.time()
            test = self.llm.test()
            if "Connection Error - Connection could not be established." not in str(test):
                print(f"/test:\r\n{test}")

            timestamp = self.llm.get_timestamp()
            if "Connection Error - Connection could not be established." not in str(timestamp):
                print(f"\r\n/timestamp:\r\n{timestamp}")

            version = self.llm.get_version()
            if "Connection Error - Connection could not be established." not in str(version):
                print(f"\r\n/version:\r\n{version}")

            quotas = self.llm.get_quotas(api_secret=self.api_secret, license_token=self.license_token)
            print(f"\r\n/quotas:")
            pprint.pprint(quotas)

            status = self.llm.verify()
            if "error" in str(status):
                if "404 Not Found" in str(status['error']) \
                        or "403 Forbidden" in str(status['error']):
                    if "Forbidden - Timestamp not valid" in status['error']:
                        print(f"Timestamp not valid - Syncing time ...")
                        self.llm.sync_time()
                    print(f"Negative License Verification: {status}")
                    break
                elif "429 Too Many Requests" in str(status['error']):
                    print(f"{status['error']}")
                    time.sleep(20)

            print(f"\r\n/verify:")
            pprint.pprint(status)

            quotas = self.llm.get_quotas(api_secret=self.api_secret, license_token=self.license_token)
            print(f"\r\n/quotas:")
            pprint.pprint(quotas)

            print(f"Runtime: {(time.time()-start_time)}")
            time.sleep(5)
        self.close()


if __name__ == "__main__":
    lucit_api_secret = ""
    lucit_license_token = ""

    logging.getLogger("lucit-licensing-logger")
    logging.basicConfig(level=logging.INFO,
                        format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                        style="{")

    ltc = LTC(api_secret=lucit_api_secret, license_token=lucit_license_token)

    try:
        asyncio.run(ltc.test_licensing())
    except KeyboardInterrupt:
        print("\r\nGracefully stopping ...")
        ltc.close()