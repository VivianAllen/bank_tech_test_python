import context
import unittest
from withdrawal import Withdrawal

class WithdrawalTestSuite(unittest.TestCase):

    def setUp(self):
        self.test_value = 100
        self.adjusted_value = self.test_value * -1
        self.withdrawal= Withdrawal(self.test_value)

    def test_deposit_is_always_negative(self):
        self.assertEqual(self.withdrawal.value, self.adjusted_value)

if __name__ == '__main__':
    unittest.main()
