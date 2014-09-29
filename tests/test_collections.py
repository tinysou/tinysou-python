import unittest
import mock
from tinysou.rest import REST
from tinysou.collections import Collection


class TestCollection(unittest.TestCase):

    """Tests for Collection."""

    def setUp(self):
        self.rest = REST('token')
        self.collection = Collection(self.rest)
        self.rest.request = mock.Mock()

    def test_list(self):
        self.collection.list('blog')
        self.rest.request.assert_called_with('GET',
                                             'engines/blog/collections',
                                             params=None)

    def test_create(self):
        self.collection.create('blog')
        self.rest.request.assert_called_with('POST',
                                             'engines/blog/collections',
                                             data=None)

    def test_get(self):
        self.collection.get('blog', 'posts')
        self.rest.request.assert_called_with('GET',
                                             'engines/blog/collections/posts',
                                             params=None)

    def test_delete(self):
        self.collection.delete('blog', 'posts')
        self.rest.request.assert_called_with('DELETE',
                                             'engines/blog/collections/posts',
                                             params=None)


if __name__ == '__main__':
    unittest.main()
