import context
import unittest
from item import Item

class ItemTestSuite(unittest.TestCase):
    """ unit tests for item class """

    def setUp(self):
        self.test_value = 100
        self.item = Item(self.test_value)

    def test_item_returns_value(self):
        self.assertEqual(self.item.value, self.test_value)

if __name__ == '__main__':
    unittest.main()
