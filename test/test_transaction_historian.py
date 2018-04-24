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
