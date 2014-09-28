import unittest
import mock
from tinysou.rest import REST
from tinysou.documents import Document


class TestDocument(unittest.TestCase):

    """Tests for Collection."""

    def setUp(self):
        self.rest = REST('token')
        self.document = Document(self.rest)
        self.rest.request = mock.Mock()

    def test_list(self):
        self.document.list('blog', 'posts')
        self.rest.request.assert_called_with('GET',
                                             'engines/blog/collections/posts/documents',
                                             params=None)

    def test_create(self):
        self.document.create('blog', 'posts')
        self.rest.request.assert_called_with('POST',
                                             'engines/blog/collections/posts/documents',
                                             data=None)

    def test_get(self):
        self.document.get('blog', 'posts', '1')
        self.rest.request.assert_called_with('GET',
                                             'engines/blog/collections/posts/documents/1',
                                             params=None)

    def test_update(self):
        self.document.update('blog', 'posts', '1')
        self.rest.request.assert_called_with('PUT',
                                             'engines/blog/collections/posts/documents/1',
                                             data=None)

    def test_delete(self):
        self.document.delete('blog', 'posts', '1')
        self.rest.request.assert_called_with('DELETE',
                                             'engines/blog/collections/posts/documents/1',
                                             params=None)


if __name__ == '__main__':
    unittest.main()
