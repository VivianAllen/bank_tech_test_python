import context
import unittest
import time
from unittest.mock import patch
from transaction import Transaction

class ItemTestSuite(unittest.TestCase):
    """ unit tests for item class """

    def setUp(self):
        self.test_value = 100
        self.timenow = time.localtime()
        self.transaction = Transaction(self.test_value)

    def test_item_returns_value(self):
        self.assertEqual(self.transaction.value, self.test_value)

    @patch('time.localtime')
    def test_item_returns_date(self, mock_time):
        mock_time.return_value = self.timenow
        self.assertEqual(self.transaction.date, self.timenow)

if __name__ == '__main__':
    unittest.main()
