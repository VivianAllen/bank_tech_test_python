import context
import unittest
import sys
from account import Account

class MockTransaction(object):

    def __init__(self, value):
        self.value = value

class MockPrinter(object):

    def print_statement(self, transaction_list):
        print('This is a printed statement')

class MyOutput(object):
    def __init__(self):
        self.data = []

    def write(self, s):
        self.data.append(s)

    def __str__(self):
        return "".join(self.data)

class AccountTestSuite(unittest.TestCase):

    def setUp(self):
        self.account = Account(MockTransaction, MockTransaction, MockPrinter)

    def test_account_making_a_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.deposits[0].value, 100)

    def test_account_making_two_deposits(self):
        self.account.deposit(100)
        self.account.deposit(100)
        self.assertEqual(len(self.account.deposits), 2)

    def test_account_making_a_withdrawal(self):
        self.account.withdraw(-100)
        self.assertEqual(self.account.withdrawals[0].value, -100)

    def test_account_making_two_withdrawals(self):
        self.account.withdraw(-100)
        self.account.withdraw(-100)
        self.assertEqual(len(self.account.withdrawals), 2)

    def test_account_combining_withdrawals_and_deposits_as_transactions_list(self):
        self.account.deposit(100)
        self.account.withdraw(-100)
        self.assertEqual(len(self.account.transactions()), 2)

    def test_account_get_values_with_one_transaction(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_values(), [100])

    def test_account_get_values_with_two_transaction(self):
        self.account.deposit(100)
        self.account.withdraw(-100)
        self.assertEqual(self.account.get_values(), [100, -100])

    def test_account_seeing_balance_no_transactions(self):
        stdout_org = sys.stdout
        my_stdout = MyOutput()
        try:
            sys.stdout = my_stdout
            self.account.balance()
        finally:
            sys.stdout = stdout_org

        self.assertEqual( str(my_stdout), "0\n")

    def test_account_seeing_balance_one_deposits(self):
        self.account.deposit(100)
        stdout_org = sys.stdout
        my_stdout = MyOutput()
        try:
            sys.stdout = my_stdout
            self.account.balance()
        finally:
            sys.stdout = stdout_org

        self.assertEqual( str(my_stdout), "100\n")

    def test_account_seeing_balance_deposits_and_withdrawals(self):
        self.account.deposit(100)
        self.account.deposit(100)
        self.account.withdraw(-100)
        self.account.withdraw(-100)

        stdout_org = sys.stdout
        my_stdout = MyOutput()
        try:
            sys.stdout = my_stdout
            self.account.balance()
        finally:
            sys.stdout = stdout_org

        self.assertEqual( str(my_stdout), "0\n")

    def test_account_printing_statement_prints_account_to_shell(self):
        stdout_org = sys.stdout
        my_stdout = MyOutput()
        try:
            sys.stdout = my_stdout
            self.account.print_statement()
        finally:
            sys.stdout = stdout_org

        self.assertEqual( str(my_stdout), 'This is a printed statement' + '\n')

if __name__ == '__main__':
    unittest.main()
