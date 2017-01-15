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

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: other + self.eval_(*values))
        elif isinstance(other, Variable):
            return Variable(c=[self, other],
                            eval_=lambda *values: self.eval_(*values) + other.eval_(*values))
        else:
            return NotImplemented

    def __radd__(self, other):

        return self.__add__(other)

    def __sub__(self, other):

    def __rsub__(self, other):

    def __mul__(self, other):

    def __rmul__(self, other):

    def __div__(self, other):

    def __rdiv__(self, other):

    def __pow__(self, other):

    def __rpow__(self, other):
