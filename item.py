import time

class Item(object):

    def __init__(self, value):
        self.value = value
        self.date = time.localtime()
