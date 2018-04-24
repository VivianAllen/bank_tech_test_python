import context
import unittest
import time
from unittest.mock import patch
from transaction_formatter import TransactionFormatter

class MockTransaction(object):

    def __init__(self, value, balance, time):
        self.value = value
        self.balance = balance
        self.date = time

class TransactionFormatterTestSuite(unittest.TestCase):

    def setUp(self):
        timenow = time.localtime()
        timestring = time.strftime("%x", timenow)
        self.deposit = MockTransaction(100, 200, timenow)
        self.withdrawal = MockTransaction(-100, 0, timenow)
        self.formatter = TransactionFormatter()
        self.formatted_deposit = " || ".join([
            timestring,
            str(self.deposit.value),
            "",
            str(self.deposit.balance)
        ])

    def test_transaction_formatter_format_formats_a_deposit(self):
        self.assertEqual(
        self.formatter.format(self.deposit), self.formatted_deposit
        )

if __name__ == '__main__':
    unittest.main()
