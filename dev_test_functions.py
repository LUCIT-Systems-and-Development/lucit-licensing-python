#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# File: dev_test.py
#

import asyncio
import logging
import time
import pprint
from lucit_licensing_python.manager import LucitLicensingManager


class LTC:
    def __init__(self, api_secret=None, license_token=None):
        self.api_secret = api_secret
        self.license_token = license_token
        self.llm = LucitLicensingManager(api_secret=api_secret, license_token=license_token,
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

            close = self.llm.close()
            print(f"\r\n/close:")
            pprint.pprint(close)

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

            info = self.llm.get_info(api_secret=self.api_secret, license_token=self.license_token)
            print(f"\r\n/info:")
            pprint.pprint(info)

            print(f"Runtime: {(time.time()-start_time)}")
            time.sleep(5)
        self.close()


if __name__ == "__main__":
    logging.getLogger("lucit_licensing_python")
    logging.basicConfig(level=logging.INFO,
                        format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                        style="{")
    ltc = LTC()
    try:
        asyncio.run(ltc.test_licensing())
    except KeyboardInterrupt:
        print("\r\nGracefully stopping ...")
        ltc.close()