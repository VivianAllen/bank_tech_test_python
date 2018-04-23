from deposit import Deposit
from functools import reduce

class Account(object):

    def __init__(self, deposit_class=Deposit):
        self.deposit_class = deposit_class
        self.deposits = []

    def deposit(self, value):
        self.deposits.append(self.deposit_class(value))

    def balance(self):
        return reduce( lambda x, y: x.value + y.value, self.deposits)
