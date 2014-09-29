import requests


def mock_response(status_code=200, content=None):
    r = requests.Response()
    r.status_code = status_code
    r._content = str.encode(content) if content else None
    return r
