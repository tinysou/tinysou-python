tinysou-python
==============

[![Build Status](https://travis-ci.org/tinysou/tinysou-python.svg?branch=master)](https://travis-ci.org/tinysou/tinysou-python)

Tinysou Python Client

## Installation

    $ pip install tinysou

## Usage

```python
import tinysou
client = tinysou.Client('YOUR_TOKEN')
```

### Engine

List:

```python
client.engines.list()
```

Create:

```python
client.engines.create({'name': 'blog', 'display_name': 'Blog'})
```

Retrieve:

```python
client.engines.get('blog')
```

Update:

```python
client.engines.update('blog', {'display_name': 'My Blog'})
```

Delete:

```python
client.engines.delete('blog')
```

### Collection

List:

```python
client.collections.list('blog')
```

Create:

```python
client.collections.create('blog',
                          {'name': 'posts',
                           'field_types': {
                                'title': 'string',
                                'tags': 'string',
                                'author': 'enum',
                                'date': 'date',
                                'body': 'text'
                           }})
```

Retrieve:

```python
client.collections.get('blog', 'posts')
```

Delete:

```python
client.collections.delete('blog', 'posts')
```

### Document

List:

```python
client.documents.list('blog', 'posts', {'page': 0, 'per_page': 20})
```

Create:

```python
client.documents.create('blog', 'posts', {
    'title': 'My First Post',
    'tags': ['news'],
    'author': 'Author',
    'date': '2014-08-16T00:00:00Z',
    'body': 'Tinysou start online today!'
})
```

Retrieve:

```python
client.documents.get('blog', 'posts', '293ddf9205df9b36ba5761d61ca59a29')
```

Update:

```python
client.documents.update('blog', 'posts', '293ddf9205df9b36ba5761d61ca59a29', {
    'title': 'First Post',
    'tags': ['news'],
    'author': 'Author',
    'date': '2014-08-16T00:00:00Z',
    'body': 'Tinysou start online today!'
})
```

Delete:

```python
client.documents.delete('blog', 'posts', '293ddf9205df9b36ba5761d61ca59a29')
```

### Search

```python
client.search('blog', {
    'q': 'tinysou', 'c': 'posts',
    'page': 0, 'per_parge': 10,
    'filter': {
        'range': {
            'field': "date",
            'from': "2014-07-01T00:00:00Z",
            'to': "2014-08-01T00:00:00Z"
        }
    },
    'sort': {
        'field': "date",
        'order': "asc",
        'mode': "avg"
    }
})
```

### Autocomplete

```python
client.autocomplete('blog', {'q': 't', 'c': 'posts'})
```

## Examples

See [examples](https://github.com/tinysou/tinysou-python/tree/master/examples)

## Contributing

1. Fork it ( https://github.com/tinysou/tinysou-python/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
