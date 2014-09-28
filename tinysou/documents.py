class Document(object):

    """Document."""

    def __init__(self, rest):
        self.rest = rest

    def list(self, engine, collection, params=None):
        return self.rest.get('engines/{engine}/collections/{collection}/documents'.format(engine=engine,
                                                                                          collection=collection),
                             params)

    def create(self, engine, collection, data=None):
        return self.rest.post('engines/{engine}/collections/{collection}/documents'.format(engine=engine,
                                                                                           collection=collection),
                              data)

    def get(self, engine, collection, id):
        return self.rest.get('engines/{engine}/collections/{collection}/documents/{id}'.format(engine=engine,
                                                                                               collection=collection,
                                                                                               id=id))

    def update(self, engine, collection, id, data=None):
        return self.rest.put('engines/{engine}/collections/{collection}/documents/{id}'.format(engine=engine,
                                                                                               collection=collection,
                                                                                               id=id),
                             data)

    def delete(self, engine, collection, id):
        return self.rest.delete('engines/{engine}/collections/{collection}/documents/{id}'.format(engine=engine,
                                                                                                  collection=collection,
                                                                                                  id=id))
