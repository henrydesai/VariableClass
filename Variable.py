class Variable():

    Variable.wengert = []

    def __init__(self, c=[], eval_=None):
        self.components = c
        self.index = len(Variable.wengert)

        if eval_ == None:
            self.eval_ = lambda *values: values[self.index]
        else:
            self.eval_ = eval_

        Variable.wengert.append(self)

    def __add__(self, other):


    def __radd__(self, other):

    def __sub__(self, other):

    def __rsub__(self, other):

    def __mul__(self, other):

    def __rmul__(self, other):

    def __div__(self, other):

    def __rdiv__(self, other):

    def __pow__(self, other):

    def __rpow__(self, other):
