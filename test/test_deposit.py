import context
import unittest
from deposit import Deposit

class DepositTestSuite(unittest.TestCase):
    """ unit tests for transaction class """

    def setUp(self):
        self.test_value = -100
        self.adjusted_value = self.test_value * -1
        self.deposit = Deposit(self.test_value)

    def test_deposit_is_always_positive(self):
        self.assertEqual(self.deposit.value, self.adjusted_value)

if __name__ == '__main__':
    unittest.main()
