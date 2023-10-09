from typing import Dict

import requests


class RestAdapter:
    def __init__(self, hostname: str, ssl_verify: bool = True):
        self._url = f"https://{hostname}/api/"
        self._ssl_verify = ssl_verify

        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def get(self, endpoint: str, ep_params: Dict = None):
        request_path = self._url + endpoint

        response = requests.get(url=request_path, verify=self._ssl_verify, params=ep_params)
        response.raise_for_status()

        response_data = response.json()

        return response_data

