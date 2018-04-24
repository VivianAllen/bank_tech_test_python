import time
from itertools import accumulate

class TransactionHistorian(object):

    def timesort(self, transaction_list):
        return sorted(transaction_list, key=lambda x: x.date, reverse=True)

    def timesort_descending(self, transaction_list):
        return sorted(transaction_list, key=lambda x: x.date)

    def balance_history_descending(self, transaction_list):
        return list(
            accumulate(
                [x.value for x in self.timesort_descending(transaction_list)]
            )
        )

    def balance_history(self, transaction_list):
        return list(reversed(self.balance_history_descending(transaction_list)))

    def history(self, transaction_list):
        return dict(
            zip(
                self.timesort(transaction_list),self.balance_history(transaction_list)
            )
        )
