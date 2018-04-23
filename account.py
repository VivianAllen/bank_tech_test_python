from deposit import Deposit

class Account(object):

    def __init__(self, deposit_class=Deposit):
        self.deposit_class = deposit_class
