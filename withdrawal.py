from transaction import Transaction

class Withdrawal(Transaction):

    def __init__(self, value):
        adjusted_value = value if value < 0 else value * -1
        Transaction.__init__(self, adjusted_value)
