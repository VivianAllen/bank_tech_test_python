import time
from decimal import Decimal

class TransactionFormatter(object):

    header = "date || credit || debit || balance"

    def format(self, transaction, balance):
        if transaction.value > 0: return self.format_deposit(transaction, balance)
        if transaction.value < 0: return self.format_withdrawal(transaction, balance)

    def format_deposit(self, transaction, balance):
        return " || ".join([
            time.strftime("%d/%m/%Y", transaction.date),
            str(abs(transaction.value)),
            "",
            str(round(Decimal(balance),2))
        ])

    def format_withdrawal(self, transaction, balance):
        return " || ".join([
            time.strftime("%d/%m/%Y", transaction.date),
            "",
            str(abs(transaction.value)),
            str(round(Decimal(balance),2))
        ])
