import context
import unittest
import time
from unittest.mock import patch
from transaction_formatter import TransactionFormatter

class MockTransaction(object):

    def __init__(self, value, time):
        self.value = value
        self.date = time

class TransactionFormatterTestSuite(unittest.TestCase):

    def setUp(self):
        timenow = time.localtime()
        timestring = time.strftime("%d/%m/%Y", timenow)
        self.deposit = MockTransaction(100, timenow)
        self.withdrawal = MockTransaction(-100, timenow)
        self.formatter = TransactionFormatter()
        self.formatted_deposit = " || ".join([
            timestring,
            str(self.deposit.value),
            "",
            "100.00"
        ])
        self.formatted_withdrawal = " || ".join([
            timestring,
            "",
            str(abs(self.withdrawal.value)),
            "0.00"
        ])

    def test_transaction_formatter_format_formats_a_deposit(self):
        self.assertEqual(
        self.formatter.format(
            self.deposit, 100),
            self.formatted_deposit
        )

    def test_transaction_formatter_format_formats_a_withdrawal(self):
        self.assertEqual(
        self.formatter.format(
            self.withdrawal, 0),
            self.formatted_withdrawal
        )

if __name__ == '__main__':
    unittest.main()
