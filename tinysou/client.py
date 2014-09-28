from .rest import REST
from .engines import Engine

class Client(object):

    """Tinysou Client"""

    def __init__(self, token):
        self.token = token
        self.rest = REST(token)
        self.engines = Engine(self.rest)
