import unittest
import mock
from .helper import mock_response
from tinysou.rest import REST


class TestREST(unittest.TestCase):

    """TestREST"""
    def setUp(self):
        self.rest = REST('token')
        self.rest.session.request = mock.Mock()

    def test_init(self):
        rest = REST('token')
        self.assertEqual(rest.token, 'token')
        self.assertIsNotNone(rest.session)

    def test_get(self):
        self.rest.session.request.return_value = mock_response()
        self.rest.get('')
        assert self.rest.session.request.called

    def test_post(self):
        self.rest.session.request.return_value = mock_response()
        self.rest.post('')
        assert self.rest.session.request.called

    def test_put(self):
        self.rest.session.request.return_value = mock_response()
        self.rest.put('')
        assert self.rest.session.request.called

    def test_delete(self):
        self.rest.session.request.return_value = mock_response()
        self.rest.delete('')
        assert self.rest.session.request.called


if __name__ == '__main__':
    unittest.main()
