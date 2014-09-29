#!/usr/bin/env python

import sys
import tinysou
from datetime import datetime


TOKEN = 'YOUR_TOKEN'
ENGINE = 'YOUR_ENGINE'


def main():
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

    client = tinysou.Client(TOKEN)

    get_doc_id = lambda: client.documents.list(
        engine['name'], collection['name'])[0]['id']

    tasks = {
        'engines.list': lambda: client.engines.list(),
        'engines.create': lambda: client.engines.create(engine),
        'engines.get': lambda: client.engines.get(engine['name']),
        'engines.update': lambda: client.engines.update(engine['name'], engine),
        'engines.delete': lambda: client.engines.delete(engine['name']),
        'collections.list': lambda: client.collections.list(engine['name']),
        'collections.create': lambda: client.collections.create(engine['name'], collection),
        'collections.get': lambda: client.collections.get(engine['name'], collection['name']),
        'collections.delete': lambda: client.collections.delete(engine['name'], collection['name']),
        'documents.list': lambda: client.documents.list(engine['name'], collection['name']),
        'documents.create': lambda: client.documents.create(engine['name'], collection['name'], document),
        'documents.get': lambda: client.documents.create(engine['name'], collection['name'], get_doc_id()),
        'documents.update': lambda: client.documents.update(engine['name'], collection['name'], get_doc_id(), document),
        'documents.delete': lambda: client.documents.delete(engine['name'], collection['name'], get_doc_id()),
        'search': lambda: client.search(engine['name'], {'q': 'first', 'c': collection['name']}),
        'autocomplete': lambda: client.search(engine['name'], {'q': 'fi', 'c': collection['name']})
    }

    if len(sys.argv) != 2 or sys.argv[1] not in tasks:
        print 'Available argument:'
        print '\n'.join(sorted(tasks.keys()))
    else:
        print tasks[sys.argv[1]]()


if __name__ == '__main__':
    main()
