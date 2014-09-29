import json
import requests
from . import __version__


class REST(object):

    """REST"""

    def __init__(self, token):
        self.token = token
        self.session = requests.Session()
        self.baseurl = 'http://api.tinysou.com/v1/'
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Tinysou-Python/' + __version__,
            'Authorization': 'token ' + self.token
        }

    def request(self, method, path, params=None, data=None):
        r = self.session.request(method,
                                 self._build_url(path),
                                 params=params,
                                 data=json.dumps(data),
                                 headers=self.headers)

        data = r.json() if r.content else None
        if r.status_code >= 400:
            raise requests.exceptions.HTTPError(r.content, response=r)
        return data

    def _build_url(self, path):
        return self.baseurl + path

    def get(self, path, params=None):
        return self.request('GET', path, params=params)

    def post(self, path, data=None):
        return self.request('POST', path, data=data)

    def put(self, path, data=None):
        return self.request('PUT', path, data=data)

    def delete(self, path, params=None):
        return self.request('DELETE', path, params=params) is None
