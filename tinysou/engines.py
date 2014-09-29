class Engine(object):

    """Engine"""

    def __init__(self, rest):
        self.rest = rest

    def list(self, params=None):
        return self.rest.get('engines', params)

    def create(self, data=None):
        return self.rest.post('engines', data)

    def get(self, name):
        return self.rest.get('engines/' + name)

    def update(self, name, data=None):
        return self.rest.put('engines/' + name, data=data)

    def delete(self, name):
        return self.rest.delete('engines/' + name)
