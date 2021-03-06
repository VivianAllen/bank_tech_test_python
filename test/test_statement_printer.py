import context
import unittest
import sys
from statement_printer import StatementPrinter

class MockListParser(object):

    def history(self, transaction_list):
        return [['this is a formatted transaction', ' and this is a balance']]

class MockRowFormatter(object):

    header = "header"

    def format(self, transaction, balance):
        return transaction + balance

class MyOutput(object):
    def __init__(self):
        self.data = []

    def write(self, s):
        self.data.append(s)

    def __str__(self):
        return "".join(self.data)

class StatementPrinterTestSuite(unittest.TestCase):

    def setUp(self):
        self.printer = StatementPrinter(MockListParser, MockRowFormatter)
        self.transaction_list = ["test"]
        statement_row = ('this is a formatted transaction and this is a '
                        'balance')
        self.statement = "header\n" + statement_row +"\n"

    def test_statement_printer_prints_statement_to_shell(self):
        stdout_org = sys.stdout
        my_stdout = MyOutput()
        try:
            sys.stdout = my_stdout
            self.printer.print_statement(self.transaction_list)
        finally:
            sys.stdout = stdout_org

        self.assertEqual( str(my_stdout), self.statement)

if __name__ == '__main__':
    unittest.main()
