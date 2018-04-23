from deposit import Deposit

class Account(object):

    def __init__(self, deposit_class=Deposit):
        self.deposit_class = deposit_class
        self.deposits = []

    def deposit(self, value):
        self.deposits.append(self.deposit_class(value))
