import context
import unittest
from statement_printer import StatmentPrinter

class MockTransaction(object):

    def __init__(self, value, date):
        self.value = value
        self.date = date

class StatementPrinterTestSuite(unittest.TestCase):

    def setUp(self):
        self.statement_printer = StatementPrinter()

    def test_timesort_transactions(self):

if __name__ == '__main__':
    unittest.main()
