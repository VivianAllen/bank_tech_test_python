from deposit import Deposit
from withdrawal import Withdrawal
from statement_printer import StatementPrinter
from functools import reduce
from decimal import Decimal

class Account(object):

    def __init__(self,
        deposit_class=Deposit,
        withdrawal_class=Withdrawal,
        printer_class=StatementPrinter,
        ):
        self.deposit_class = deposit_class
        self.withdrawal_class = withdrawal_class
        self.printer = printer_class()
        self.deposits = []
        self.withdrawals = []

    def deposit(self, value):
        self.deposits.append(self.deposit_class(value))

    def withdraw(self, value):
        self.withdrawals.append(self.withdrawal_class(value))

    def transactions(self):
        return self.deposits + self.withdrawals

    def get_values(self):
        return [x.value for x in self.transactions()]

    def balance(self):
        print (
            round(Decimal(reduce(lambda x, y: x + y, self.get_values(), 0)),2)
        )

    def print_statement(self):
        self.printer.print_statement(self.transactions())
