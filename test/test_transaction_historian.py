import context
import unittest
import time
from unittest.mock import patch
from transaction_historian import TransactionHistorian

class MockTransaction(object):

    def __init__(self, value, time):
        self.value = value
        self.date = time

class TransactionHistorianTestSuite(unittest.TestCase):

    def setUp(self):
        self.trans_hist = TransactionHistorian()
        self.trans1 = MockTransaction(
            -100,
            time.localtime(time.mktime((2018, 1, 1, 0, 0, 0, 0, 1, 0)))
        )
        self.trans2 = MockTransaction(
            -100,
            time.localtime(time.mktime((2018, 1, 1, 0, 1, 0, 0, 1, 0)))
        )
        self.trans3 = MockTransaction(
            100,
            time.localtime(time.mktime((2018, 1, 1, 0, 2, 0, 0, 1, 0)))
        )
        self.trans4 = MockTransaction(
            100,
            time.localtime(time.mktime((2018, 1, 1, 0, 3, 0, 0, 1, 0)))
        )

    def test_transaction_historian_timesort_sorts_in_ascending_age(self):
        trans_list = [self.trans2, self.trans4, self.trans1, self.trans3]
        sorted_list =  [self.trans4, self.trans3, self.trans2, self.trans1]
        self.assertEqual(self.trans_hist.timesort(trans_list), sorted_list)

    def test_transaction_historian_timesort_descending_sorts_in_descending_age(self):
        trans_list = [self.trans2, self.trans4, self.trans1, self.trans3]
        sorted_list =  [self.trans1, self.trans2, self.trans3, self.trans4]
        self.assertEqual(self.trans_hist.timesort_descending(trans_list), sorted_list)

    def test_transaction_historian_balance_history_descending_calcs_rolling_balance_in_descending_age(self):
        trans_list = [self.trans1, self.trans2, self.trans3, self.trans4]
        balance_list = [-100, -200, -100, 0]
        self.assertEqual(self.trans_hist.balance_history_descending(trans_list), balance_list)

    def test_transaction_historian_balance_history_calcs_rolling_balance(self):
        trans_list = [self.trans1, self.trans2, self.trans3, self.trans4]
        balance_list = [0, -100, -200, -100]
        self.assertEqual(self.trans_hist.balance_history(trans_list), balance_list)

    def test_transaction_historian_history_returns_list_of_timesorted_transactions_balance_pairs(self):
        trans_list = [self.trans1, self.trans2, self.trans3, self.trans4]
        sorted_list =  [self.trans4, self.trans3, self.trans2, self.trans1]
        balance_list = [0, -100, -200, -100]
        self.assertEqual(self.trans_hist.history(trans_list), list(zip(sorted_list, balance_list)))
