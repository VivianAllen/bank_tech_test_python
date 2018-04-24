import time

class TransactionFormatter(object):

    def format(self, transaction):
        if transaction.value > 0: return self.format_deposit(transaction)
        if transaction.value < 0: return self.format_withdrawal(transaction)

    def format_deposit(self, transaction):
        return " || ".join([
            time.strftime("%x", transaction.date),
            str(abs(transaction.value)),
            "",
            str(transaction.balance)
        ])

    def format_withdrawal(self, transaction):
        return " || ".join([
            time.strftime("%x", transaction.date),
            "",
            str(abs(transaction.value)),
            str(transaction.balance)
        ])
