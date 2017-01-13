class Variable():
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return Variable(self.val + other.val)
    def __radd__(self, other):
        return Variable(self.val + other.val)
