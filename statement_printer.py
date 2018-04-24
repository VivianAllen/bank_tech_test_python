from transaction_formatter import TransactionFormatter
from transaction_historian import TransactionHistorian
from statement_headers import statement_headers

class StatementPrinter(object):

    def __init__(self,
            row_formatter=TransactionFormatter,
            list_parser=TransactionHistorian,
            header=statement_headers[0]
        ):
        self.row_formatter = row_formatter
        self.list_parser = list_parser
        self.header = header

    def print_statement(self, transaction_list):
        print(self.header)
        [print(x) for x in self.get_transactions(transaction_list)]

    def get_transactions(self, transaction_list):
        timesorted = self.list_parser.timesort(transaction_list)
        balances = self.list_parser.balance_history(transaction_list)



        
