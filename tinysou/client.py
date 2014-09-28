from .rest import REST

class Client(object):

    """Tinysou Client"""

    def __init__(self, token):
        self.token = token
        self.rest = REST(token)
