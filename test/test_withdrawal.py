import context
import unittest
from withdrawal import Withdrawal

class WithdrawalTestSuite(unittest.TestCase):

    def setUp(self):
        test_value = 100
        self.adjusted_value = test_value * -1
        self.withdrawal= Withdrawal(test_value)

    def test_withdrawal_is_always_negative(self):
        self.assertEqual(self.withdrawal.value, self.adjusted_value)

if __name__ == '__main__':
    unittest.main()
