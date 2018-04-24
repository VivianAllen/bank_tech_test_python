from transaction_formatter import TransactionFormatter
from transaction_historian import TransactionHistorian
from statement_headers import statement_headers

class StatementPrinter(object):

    def __init__(self,
            row_formatter=TransactionFormatter,
            list_parser=TransactionHistorian
        ):
        self.row_formatter = row_formatter
        self.list_parser = list_parser

    def print_statement(self, transaction_list):
        pass
