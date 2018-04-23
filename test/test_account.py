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
        self.assertEqual(self.deposits[0].value(), 100)