'''
Group Names: Lior Hirschfeld, Henry Desai, Pham Nhat, and Jihoun Im
Class: Compsci 630 Machine Learning
Teacher: Dr. Z
'''

import numpy as np

class Variable:

    wengert = [] #created two different wengert lists. One stores all variables and the other stores "root" variables.
    all_wengert = []

    def __init__(self, c=[], eval_=None, grad_=None, op="No Operation"):
        self.components = c
        self.op = op #stores the operand as a string to be printed out in repr
        self.index = len(Variable.all_wengert)

        if eval_ == None: #if eval_ is None, then so is grad_
            self.trueIndex = len(Variable.wengert)
            Variable.wengert.append(self)
            self.eval_ = lambda *values: values[self.trueIndex]
            self.grad_ = lambda *values: np.array([1 if i==self.index else 0 for i in range(len(Variable.wengert))])
        else:
            self.eval_ = eval_
            self.grad_ = grad_

        Variable.all_wengert.append(self)



    def __call__(self, *values):
        return self.eval_(*values)

    def __repr__(self, depth=0):
        s=""
        for i in range(depth):
            s += "| "
        s += "W" + str(self.index) + ": " + self.op + "\n"
        for c in self.components:
            s += c.__repr__(depth=depth+1) #Used recursion to print out all children variables and their operands

        return s

    def clear_wengert():
        Variable.wengert = []
        Variable.all_wengert = []

    def __add__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: other + self.eval_(*values),
                            grad_=lambda *values: self.grad_(*values), op="+")
        elif isinstance(other, Variable):
            return Variable(c=[self, other],
                            eval_=lambda *values: self.eval_(*values) + other.eval_(*values),
                            grad_=lambda *values: self.grad_(*values) + other.grad_(*values), op="+")
        else:
            return NotImplemented

    def __radd__(self, other):

        return self.__add__(other)

    def __sub__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: self.eval_(*values) - other,
                            grad_=lambda *values: self.grad_(*values), op="-")
        elif isinstance(other, Variable):
            return Variable(c=[self, other],
                            eval_=lambda *values: self.eval_(*values) - other.eval_(*values),
                            grad_=lambda *values: self.grad_(*values) - other.grad_(*values), op="-")
        else:
            return NotImplemented

    def __rsub__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: other - self.eval_(*values),
                            grad_=lambda *values: 0-self.grad_(*values), op="-")
        else:
            return NotImplemented

    def __mul__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: self.eval_(*values) * other,
                            grad_=lambda *values: other * self.grad_(*values),op="*")
        elif isinstance(other, Variable):
            return Variable(c=[self, other],
                            eval_=lambda *values: self.eval_(*values) * other.eval_(*values),
                            grad_=lambda *values: self.grad_(*values) * other.eval_(*values) +
                            self.eval_(*values) * other.grad_(*values),op="*")
        else:
            return NotImplemented

    def __rmul__(self, other):

        return self.__mul__(other)

    def __truediv__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: self.eval_(*values) / other,
                            grad_=lambda *values: self.grad_(*values) / other, op="/")
        elif isinstance(other, Variable):
            return Variable(c=[self, other],
                            eval_=lambda *values: self.eval_(*values) / other.eval_(*values),
                            grad_=lambda *values: (self.grad_(*values) * other.eval_(*values) -
                            other.grad_(*values) * self.eval_(*values)) / other.eval(*values) ** 2, op="/")
        else:
            return NotImplemented

    def __rtruediv__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: other / self.eval_(*values),
                            grad_=lambda *values: (0-other / (self.eval_(*values)**2))*self.grad_(*values), op="/")
        else:
            return NotImplemented

    def __pow__(self, other):

        if isinstance(other, (int, float)):
            return Variable(c=[self],
                            eval_=lambda *values: self.eval_(*values) ** other,
                            grad_=lambda *values: (other*self.eval_(*values)**(other-1) * self.grad_(*values)), op="**")
        else:
            return NotImplemented

    def __rpow__(self, other):
        if other == np.e:
            return Variable(c=[self],
                            eval_=lambda *values: np.e ** self.eval_(*values),
                            grad_=lambda *values: np.e ** self.eval_(*values) * self.grad_(*values), op="**")
        else:
            return NotImplemented

    def ln(self):
        return Variable(c=[self],
                        eval_=lambda *values: np.log(self.eval_(*values)),
                        grad_=lambda *values: 1/(self.eval_(*values)) * self.grad_(*values), op="ln")
