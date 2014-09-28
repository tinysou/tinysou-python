class Collection(object):

    """Collection."""

    def __init__(self, rest):
        self.rest = rest

    def list(self, engine, params=None):
        return self.rest.get('engines/{engine}/collections'.format(engine=engine),
                             params)

    def create(self, engine, data=None):
        return self.rest.post('engines/{engine}/collections'.format(engine=engine),
                              data)

    def get(self, engine, name):
        return self.rest.get('engines/{engine}/collections/{name}'.format(engine=engine,
                                                                          name=name))

    def delete(self, engine, name):
        return self.rest.delete('engines/{engine}/collections/{name}'.format(engine=engine,
                                                                             name=name))
