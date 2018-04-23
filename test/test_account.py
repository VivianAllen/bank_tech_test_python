import context
import unittest
from account import Account

class MockDeposit(object):

    def __init__(self, value):
        self.value = value

class AccountTestSuite(unittest.TestCase):
    """ unit tests for account class """

    def setUp(self):
        self.account = Account(MockDeposit)

    def test_making_a_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.deposits[0].value, 100)

    def test_making_two_deposits(self):
        self.account.deposit(100)
        self.account.deposit(100)
        self.assertEqual(len(self.account.deposits), 2)

    def test_seeing_balance_deposits_only(self):
        self.account.deposit(100)
        self.account.deposit(50)
        self.assertEqual( self.account.balance(), 150)
