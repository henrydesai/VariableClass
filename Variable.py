class Variable:

    wengert = []

    def __init__(self, c=[], eval_=None):
        self.components = c
        self.index = len(Variable.wengert)

        if eval_ == None:
            self.eval_ = lambda *values: values[self.index]
        else:
            self.eval_ = eval_

        Variable.wengert.append(self)

    def __call__(self, *values):
        return self.eval_(*values)

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

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: self.eval_(*values) - other)
        elif isinstance(other, Variable):
            return Variable(c=[self, other],
                            eval_=lambda *values: self.eval_(*values) - other.eval_(*values))
        else:
            return NotImplemented

    def __rsub__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: other - self.eval_(*values))
        else:
            return NotImplemented

    def __mul__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: self.eval_(*values) * other)
        elif isinstance(other, Variable):
            return Variable(c=[self, other],
                            eval_=lambda *values: self.eval_(*values) * other.eval_(*values))
        else:
            return NotImplemented

    def __rmul__(self, other):

        return self.__mul__(other)

    def __div__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: self.eval_(*values) / other)
        elif isinstance(other, Variable):
            return Variable(c=[self, other],
                            eval_=lambda *values: self.eval_(*values) / other.eval_(*values))
        else:
            return NotImplemented

    def __rdiv__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: other / self.eval_(*values))
        else:
            return NotImplemented

    def __pow__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: self.eval_(*values) ** other)
        elif isinstance(other, Variable):
            return Variable(c=[self, other],
                            eval_=lambda *values: self.eval_(*values) ** other.eval_(*values))
        else:
            return NotImplemented

    def __rpow__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: other ** self.eval_(*values))
        else:
            return NotImplemented
