#!/usr/bin/env python

import tinysou
from datetime import datetime


TOKEN = 'YOUR_TOKEN'
ENGINE = 'YOUR_ENGINE_NAME'

engine = {
    'name': ENGINE,
    'display_name': 'My Blog'
}

collection = {
    'name': 'posts',
    'field_types': {
        'title': 'string',
        'tags': 'string',
        'author': 'enum',
        'date': 'date',
        'body': 'text'
    }
}

document = {
    'title': 'My First Post',
    'tags': ['news'],
    'author': 'Author',
    'date': datetime.utcnow().isoformat() + 'Z',
    'body': 'Tinysou start online today!'
}

client = tinysou.Client('YOUR_TOKEN')

client.engines.list()
client.engines.create(engine)
client.engines.get(engine['name'])
client.engines.update(engine['name'], engine)
client.engines.delete(engine['name'])

client.collections.list(engine['name'])
client.collections.create(engine['name'], collection)
client.collections.get(engine['name'], collection['name'])
client.collections.delete(engine['name'], collection['name'])

client.documents.list(engine['name'], collection['name'])
doc_id = 'abc'
client.documents.get(engine['name'], collection['name'], doc_id)
client.documents.update(engine['name'], collection['name'], doc_id, document)
client.documents.delete(engine['name'], collection['name'], doc_id)

client.search(engine['name'], {'q': 'first', 'c': collection['name']})
client.autocomplete(engine['name'], {'q': 'fi', 'c': collection['name']})
