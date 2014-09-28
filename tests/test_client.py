import unittest
from tinysou import Client


class TestClient(unittest.TestCase):

    """TestClient"""

    def test_init(self):
        client = Client('token')
        self.assertEqual(client.token, 'token')
        self.assertIsNotNone(client.rest)
        self.assertIsNotNone(client.engines)


if __name__ == '__main__':
    unittest.main()
