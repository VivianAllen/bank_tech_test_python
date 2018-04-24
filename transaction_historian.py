import time

class TransactionHistorian(object):

    def timesort(self, transaction_list):
        return sorted(transaction_list, key=lambda x: x.date, reverse=True)
