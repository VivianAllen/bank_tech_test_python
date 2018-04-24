import context
import unittest
import time
from unittest.mock import patch
from transaction_formatter import TransactionFormatter

class MockTransaction(object):

    def __init__(self, value):
        self.value = value

class TransactionFormatterTestSuite(unittest.TestCase):

    def setUp(self):
        self.timenow = time.localtime()
        deposit_val = 100
        withdrawal_val = -100
        self.deposit = MockTransaction(100, timenow)
        self.withdrawal = MockTransaction(-100, timenow)
        self.formatter = TransactionFormatter()
        timestring = time.strftime("%x", timenow)
        self.formatted_deposit = " || ".join([timestring, deposit_val, )

    def test_format(self):
        self.assertEqual(
        self.formatter.format(self.deposit), self.formatted_deposit
        )

if __name__ == '__main__':
    unittest.main()
