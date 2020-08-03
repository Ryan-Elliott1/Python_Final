import unittest
from appointment_gui import client as a


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = a.Client(1412, 'Johnson', 'Bill', '515-123-4567', '123 Happy St')

    def tearDown(self):
        del self.client

    def test_object_created_all_attributes(self):
        self.assertEqual(self.client._client_id, 1412)
        self.assertEqual(self.client._last_name, 'Johnson')
        self.assertEqual(self.client._first_name, 'Bill')
        self.assertEqual(self.client._phone_number, '515-123-4567')
        self.assertEqual(self.client._address, '123 Happy St')

    def test_client_str(self):
        self.assertEqual(str(self.client), 'client id 1412 last name Johnson first name Bill phone number 515-123-4567 address 123 Happy St')

    def test_client_repr(self):
        self.assertEqual(repr(self.client), 'client id 1412 last name Johnson first name Bill phone number 515-123-4567 address 123 Happy St')

    def test_object_not_created_error_client_id(self):
        with self.assertRaises(AttributeError):
            c = a.Client('1412', 'Johnson', 'Bill', '515-123-4567', '123 Happy St')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            c = a.Client(1412, 'J0hns0n', 'Bill', '515-123-4567', '123 Happy St')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            c = a.Client(1412, 'Johnson', 'B1ll', '515-123-4567', '123 Happy St')

    def test_object_not_created_error_phone_number(self):
        with self.assertRaises(ValueError):
            c = a.Client(1412, 'Johnson', 'Bill', '5one5-123-4567', '123 Happy St')

