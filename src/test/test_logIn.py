import unittest
from atproto_client.client.session import Session, SessionEvent, SessionString
import pytest
#login/ create cesion test
class TestSession(unittest.TestCase):
    def setUp(self):
        self.handle = "test_handle"
        self.did = "test_did"
        self.access_jwt = "access_jwt_token"
        self.refresh_jwt = "refresh_jwt_token"
        self.session = Session(self.handle, self.did, self.access_jwt, self.refresh_jwt)

    def test_session_attributes(self):
        self.assertEqual(self.session.handle, self.handle)
        self.assertEqual(self.session.did, self.did)
        self.assertEqual(self.session.access_jwt, self.access_jwt)
        self.assertEqual(self.session.refresh_jwt, self.refresh_jwt)

    def test_encode_decode(self):
        encoded = self.session.encode()
        decoded_session = Session.decode(encoded)
        self.assertEqual(decoded_session.handle, self.session.handle)
        self.assertEqual(decoded_session.did, self.session.did)
        self.assertEqual(decoded_session.access_jwt, self.session.access_jwt)
        self.assertEqual(decoded_session.refresh_jwt, self.session.refresh_jwt)

    def test_copy(self):
        session_copy = self.session.copy()
        self.assertEqual(session_copy.handle, self.session.handle)
        self.assertEqual(session_copy.did, self.session.did)
        self.assertEqual(session_copy.access_jwt, self.session.access_jwt)
        self.assertEqual(session_copy.refresh_jwt, self.session.refresh_jwt)
        self.assertNotEqual(id(session_copy), id(self.session), "Copy should not be the same object in memory")


    def test_session_event(self):
        self.assertTrue(SessionEvent.CREATE.value, 'creat')
        self.assertTrue(SessionEvent.IMPORT.value, 'import')
        self.assertTrue(SessionEvent.REFRESH.value, 'refresh')

if __name__ == '__main__':
    unittest.main()