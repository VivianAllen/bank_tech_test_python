import context
import unittest
import sys
from statement_printer import StatementPrinter
from statement_headers import statement_headers

class MockListParser(object):

    def timesort(self, transaction):
        return ['this is a formatted transaction']

    def balance_history(self, transaction):
        return [' and this is a balance']

class MockRowFormatter(object):

    def format(self, transaction, balance):
        return transaction + balance

class StatementPrinterTestSuite(unittest.TestCase):

    def setUp(self):
        self.printer = StatementPrinter(MockRowFormatter, MockListParser)
        self.transaction_list = "test"
        header = statement_headers[0]
        statement_row = ('this is a formatted transaction and this is a '
                        'balance')
        self.statement = header + "\n" + statement_row

    def test_statement_printer_prints_statement_to_shell(self):
        class MyOutput(object):
            def __init__(self):
                self.data = []

            def write(self, s):
                self.data.append(s)

            def __str__(self):
                return "".join(self.data)

        stdout_org = sys.stdout
        my_stdout = MyOutput()
        try:
            sys.stdout = my_stdout
            self.printer.print_statement(self.transaction_list)
        finally:
            sys.stdout = stdout_org

        self.assertEquals( str(my_stdout), self.statement)

if __name__ == '__main__':
    unittest.main()