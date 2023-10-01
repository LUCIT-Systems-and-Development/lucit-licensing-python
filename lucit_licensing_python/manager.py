#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# File: lucit_licensing_python/manager.py
#

import cython
import hashlib
import hmac
import logging
import platform
import requests
import sys
import threading
import time
from typing import Callable
import uuid
from copy import deepcopy
from operator import itemgetter
from requests.exceptions import ConnectionError, RequestException, HTTPError
from simplejson.errors import JSONDecodeError

logger = logging.getLogger("lucit-licensing-logger")


class Manager(threading.Thread):
    def __init__(self, api_secret: str = None, license_token: str = None,
                 program_used: str = None, start: bool = True,
                 parent_shutdown_function: Callable[[bool], bool] = None,
                 needed_license_type: str = None):
        super().__init__()
        self.api_secret = api_secret
        self.id = str(uuid.uuid4())
        self.license_token = license_token
        self.mac = str(hex(uuid.getnode()))
        self.module_version: str = "1.0.0"
        self.needed_license_type = needed_license_type
        self.os = platform.system()
        self.parent_shutdown_function = parent_shutdown_function
        self.program_used = program_used
        self.python_version = platform.python_version()
        self.request_interval = 20
        self.sigterm = False
        self.time_delta = 0.0
        self.url: str = "https://private.api.lucit.services/licensing/v1/"
        self.version: str = "1.0.0"
        logger.info(f"Starting instance of `lucit-licensing-python_{self.version}"
                    f"{'_compiled' if cython.compiled else '_source'}' ...")
        if start is True:
            self.start()

    def __generate_signature(self, api_secret: str = None, data: dict = None) -> str:
        ordered_data = self.__order_params(data)
        query_string = '&'.join(["{}={}".format(d[0], d[1]) for d in ordered_data])
        m = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256)
        return str(m.hexdigest())

    @staticmethod
    def __order_params(data: dict = None) -> list:
        has_signature: bool = False
        params = []
        for key, value in data.items():
            if key == 'signature':
                has_signature = True
            else:
                params.append((key, value))
        params.sort(key=itemgetter(0))
        if has_signature:
            params.append(('signature', data['signature']))
        return params

    def __private_request(self, api_secret: str = None, license_token: str = None,
                          key_value: str = None, endpoint: str = None) -> dict:
        api_secret = api_secret if api_secret is not None else self.api_secret
        license_token = license_token if license_token is not None else self.license_token
        params = {
            "license_token": license_token,
            "id": self.id,
            "mac": self.mac,
            "os": self.os,
            "program_used": self.program_used,
            "python_version": self.python_version,
            "timestamp": time.time()+self.time_delta,
        }
        if key_value is not None:
            params['key_value'] = key_value
        params["signature"] = self.__generate_signature(api_secret=api_secret, data=params)
        response = None
        try:
            response = requests.get(self.url+endpoint, params=params)
            response.raise_for_status()
        except (ConnectionError, RequestException, HTTPError):
            try:
                if response is None:
                    return {"error": f"Connection Error - Connection could not be established."}
                else:
                    if response.status_code == 404 or response.status_code == 500 or response.status_code == 503:
                        return {"error": f"Connection Error - Connection could not be established."}
                    else:
                        try:
                            return {"error": f"{response.status_code} {response.json()['detail']}"}
                        except KeyError:
                            return {"error": f"Connection Error - Connection could not be established."}
            except (UnboundLocalError, JSONDecodeError) as error_msg:
                if "HTTPConnectionPool" in str(error_msg):
                    return {"error": f"Connection Error - Connection could not be established."}
                return {"error": f"{error_msg}"}
        result: dict = response.json()
        time_gap = time.time() + self.time_delta - float(result['timestamp'])
        if time_gap > 30 or time_gap < -30:
            return {"error": "Server timestamp in signed response is out of valid range."}
        try:
            if self.__verify_signature(api_secret=api_secret, params=result,
                                       signature=result["signature"]):
                return result
            else:
                return {"error": "Invalid Signature - The response is not signed correctly."}
        except KeyError:
            return {"error": "Missing Signature - The response is not signed."}

    def __public_request(self, endpoint: str = None) -> dict:
        response = None
        try:
            response = requests.get(self.url+endpoint)
            response.raise_for_status()
        except (ConnectionError, RequestException, HTTPError):
            try:
                if response is None:
                    return {"error": f"Connection Error - Connection could not be established."}
                else:
                    if response.status_code == 404 or response.status_code == 500 or response.status_code == 503:
                        return {"error": f"Connection Error - Connection could not be established."}
                    else:
                        try:
                            return {"error": f"{response.status_code} {response.json()['detail']}"}
                        except KeyError:
                            return {"error": f"Connection Error - Connection could not be established."}
            except (UnboundLocalError, JSONDecodeError) as error_msg:
                if "HTTPConnectionPool" in str(error_msg):
                    return {"error": f"Connection Error - Connection could not be established."}
                return {"error": f"{error_msg}"}
        result: dict = response.json()
        return result

    def __verify_signature(self, api_secret: str = None, params: dict = None, signature: str = None) -> bool:
        params_without_signature: dict = deepcopy(params)
        try:
            del params_without_signature['signature']
        except KeyError:
            logger.debug(f"params_without_signature['signature'] not deletable, it does not exist.")
        params_signature: str = self.__generate_signature(api_secret=api_secret, data=params_without_signature)
        if params_signature == signature:
            return True
        else:
            return False

    def close(self, key_value: str = None) -> dict:
        self.sigterm = True
        if self.parent_shutdown_function is not None:
            self.parent_shutdown_function(close_api_session=False)
        return self.__private_request(api_secret=None, license_token=None,
                                      key_value=key_value, endpoint="close")

    def get_module_version(self):
        return self.module_version

    def get_quotas(self, api_secret: str = None, license_token: str = None) -> dict:
        return self.__private_request(api_secret=api_secret, license_token=license_token, endpoint="quotas")

    def get_timestamp(self) -> dict:
        return self.__public_request(endpoint="timestamp")

    def get_version(self) -> dict:
        return self.__public_request(endpoint="version")

    def run(self):
        connection_errors = 0
        while self.sigterm is False:
            license_result = self.verify()
            try:
                if license_result['license']['licensed_product'] != self.needed_license_type:
                    logger.critical(f"License not useable, its issued for product: "
                                    f"{license_result['license']['licensed_product']}")
                    self.close()
                    break
                else:
                    if license_result['license']['status'] == "VALID":
                        try:
                            request_interval = int(license_result['license']['request_interval'])
                            if request_interval != self.request_interval:
                                logger.debug(f"Setting `request_interval` to {request_interval}")
                                self.request_interval = request_interval-1
                        except KeyError:
                            pass
                        logger.debug(f"License validated for product: {license_result['license']['licensed_product']}")
                    else:
                        logger.critical(f"License is invalid! License Status: {license_result['license']['status']}")
                        self.close()
                        break
            except KeyError:
                if "403 Forbidden" in license_result['error']:
                    if "Forbidden - Timestamp not valid" in license_result['error']:
                        logger.error(f"Timestamp not valid - Syncing time ...")
                        self.sync_time()
                    elif "403 Forbidden - Access forbidden due to misuse of test licenses." in license_result['error']:
                        logger.critical(f"License is invalid!")
                        self.close()
                        break
                    elif "403 Forbidden - Insufficient access rights." in license_result['error']:
                        logger.critical(f"{license_result['error']}")
                        self.close()
                        break
                    else:
                        logger.critical(f"{license_result['error']}")
                        self.close()
                        break
                elif "429 Too Many Requests" in license_result['error']:
                    logger.critical(f"{license_result['error']}")
                    time.sleep(30)
                elif "Connection Error - Connection could not be established" in license_result['error']:
                    logger.critical(f"{license_result['error']}")
                    if connection_errors > 10:
                        logger.critical(f"Connection to LUCIT Licensing Backend could not be established. Please "
                                        f"try again later!")
                        self.close()
                        break
                    connection_errors += 1
                    time.sleep(1)
                    continue
                else:
                    logger.critical(f"Unknown error: {license_result['error']}")
                    break

            connection_errors = 0
            for _ in range(self.request_interval * 60):
                if self.sigterm is False:
                    threading.Event().wait(1)
                else:
                    break

    def stop(self, key_value: str = None) -> dict:
        return self.close(key_value=key_value)

    def sync_time(self) -> bool:
        try:
            self.time_delta = float(self.get_timestamp()['timestamp']) - time.time()
            return True
        except KeyError:
            return False

    def test(self) -> dict:
        return self.__public_request(endpoint="test")

    def verify(self, api_secret: str = None, license_token: str = None, key_value: str = None) -> dict:
        return self.__private_request(api_secret=api_secret, license_token=license_token,
                                      key_value=key_value, endpoint="verify")
