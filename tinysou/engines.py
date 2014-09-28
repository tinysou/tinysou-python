class Engine(object):

    """Engine"""

    def __init__(self, rest):
        self.rest = rest

    def list(self, params=None):
        self.rest.get('engines', params)

    def create(self, data=None):
        self.rest.post('engines', data)

    def get(self, name):
        self.rest.get('engines/' + name)

    def update(self, name, data=None):
        self.rest.put('engines/' + name, data=data)

    def delete(self, name):
        self.rest.delete('engines/' + name)
