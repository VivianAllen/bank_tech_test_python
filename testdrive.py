from account import Account
from transaction_historian import TransactionHistorian
from statement_printer import StatementPrinter

ac = Account()
th = TransactionHistorian()
sp = StatementPrinter()
ac.deposit(10)
ac.deposit(10)
trans = ac.transactions()
