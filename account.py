from deposit import Deposit
from withdrawal import Withdrawal
from functools import reduce

class Account(object):

    def __init__(self, deposit_class=Deposit, withdrawal_class=Withdrawal):
        self.deposit_class = deposit_class
        self.withdrawal_class = withdrawal_class
        self.deposits = []
        self.withdrawals = []

    def deposit(self, value):
        self.deposits.append(self.deposit_class(value))

    def withdraw(self, value):
        self.withdrawals.append(self.withdrawal_class(value))

    def balance(self):
        if len(self.deposits) < 1:
            return 0.0
        if len(self.deposits) == 1:
            return self.deposits[0].value
        else:
            return reduce( lambda x, y: x.value + y.value, self.deposits)
