class test_class(object):

    def __init__(self, value):
        self.value = value

class tester_class(object):

    def __init__(self):
        self.test_class = test_class
        self.storage = []

    def add_to_array(self, value):
        self.storage.append(self.test_class(value))
