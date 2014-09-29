import unittest
import mock
from tinysou.rest import REST
from tinysou.engines import Engine


class TestEngine(unittest.TestCase):

    """Tests for Engine."""

    def setUp(self):
        self.rest = REST('token')
        self.engine = Engine(self.rest)
        self.rest.request = mock.Mock()

    def test_list(self):
        self.engine.list()
        self.rest.request.assert_called_with('GET', 'engines', params=None)

    def test_create(self):
        self.engine.create()
        self.rest.request.assert_called_with('POST', 'engines', data=None)

    def test_get(self):
        self.engine.get('blog')
        self.rest.request.assert_called_with('GET',
                                             'engines/blog',
                                             params=None)

    def test_update(self):
        self.engine.update('blog')
        self.rest.request.assert_called_with('PUT', 'engines/blog', data=None)

    def test_delete(self):
        self.engine.delete('blog')
        self.rest.request.assert_called_with('DELETE',
                                             'engines/blog',
                                             params=None)


if __name__ == '__main__':
    unittest.main()
