import unittest
import mock
from tinysou import Client


class TestClient(unittest.TestCase):

    """TestClient"""

    def setUp(self):
        self.client = Client('token')
        self.client.rest.request = mock.Mock()

    def test_init(self):
        client = Client('token')
        self.assertEqual(client.token, 'token')
        self.assertIsNotNone(client.rest)
        self.assertIsNotNone(client.engines)
        self.assertIsNotNone(client.collections)
        self.assertIsNotNone(client.documents)

    def test_search(self):
        self.client.search('blog')
        self.client.rest.request.assert_called_with('POST',
                                                    'engines/blog/search',
                                                    data=None)

    def test_autocomplete(self):
        self.client.autocomplete('blog')
        self.client.rest.request.assert_called_with('POST',
                                                    'engines/blog/autocomplete',
                                                    data=None)


if __name__ == '__main__':
    unittest.main()
