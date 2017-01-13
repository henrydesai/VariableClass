class Variable():
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Variable(self.val + other.val)

    def __radd__(self, other):
        return Variable(self.val + other.val)

    def __sub__(self, other):

    def __rsub__(self, other):

    def __mul__(self, other):

    def __rmul__(self, other):

    def __div__(self, other):

    def __rdiv__(self, other):

    def __pow__(self, other):

    def __rpow__(self, other):
