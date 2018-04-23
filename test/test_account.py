import context
import unittest
from account import Account

class MockDeposit(object):

    def __init__(self, value):
        self.value = value

class MockWithdrawal(object):

    def __init__(self, value):
        self.value = value

class AccountTestSuite(unittest.TestCase):
    """ unit tests for account class """

    def setUp(self):
        self.account = Account(MockDeposit, MockWithdrawal)

    def test_making_a_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.deposits[0].value, 100)

    def test_making_two_deposits(self):
        self.account.deposit(100)
        self.account.deposit(100)
        self.assertEqual(len(self.account.deposits), 2)

    def test_seeing_balance_no_transactions(self):
        self.assertEqual( self.account.balance(), 0)

    def test_seeing_balance_one_deposits(self):
        self.account.deposit(100)
        self.assertEqual( self.account.balance(), 100)

    def test_seeing_balance_two_deposits(self):
        self.account.deposit(100)
        self.account.deposit(50)
        self.assertEqual( self.account.balance(), 150)

    def test_making_a_withdrawal(self):
        self.account.withdraw(-100)
        self.assertEqual(self.account.withdrawals[0].value, -100)

    def test_making_two_withdrawals(self):
        self.account.withdraw(-100)
        self.account.withdraw(-100)
        self.assertEqual(len(self.account.withdrawals), 2)

    def test_combining_withdrawals_and_deposits_as_transactions_list(self):
        self.account.deposit(100)
        self.account.withdraw(-100)
        self.assertEqual(len(self.account.transactions), 2)
