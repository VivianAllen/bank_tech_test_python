import context
import unittest
from item import Item

class ItemTestSuite(unittest.TestCase):
    """ unit tests for item class """

    def setUp(self):
        self.test_amount = 100
        self.item = Item(self.test_amount)

    def test_item_returns_amount(self):
        self.assertEqual(self.item.amount, self.test_amount)

if __name__ == '__main__':
    unittest.main()
