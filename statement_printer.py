from transaction_formatter import TransactionFormatter
from transaction_historian import TransactionHistorian
from statement_headers import statement_headers

class StatementPrinter(object):

    def __init__(self,
            list_parser_class=TransactionHistorian,
            row_formatter_class=TransactionFormatter,
            header=statement_headers[0]
        ):
        self.row_formatter = row_formatter_class()
        self.list_parser = list_parser_class()
        self.header = header

    def print_statement(self, transaction_list):
        print(self.header)
        [print(x) for x in self.get_formatted_transactions(transaction_list)]

    def get_formatted_transactions(self, transaction_list):
        history = self.list_parser.history(transaction_list)
        return list([self.row_formatter.format(x[0], x[1]) for x in history ])
