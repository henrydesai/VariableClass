import numpy as np
from VariableClass.Variable import Variable

class LogisticRegression:

    def __init__(self):
        return

    def fit(self, X, y, c=1):
        Variable.clear_wengert()
        self.X = X
        self.y = y
        cost = self.make_cost_function()

        # Starting points
        pos = np.random.rand(len(X[0])+1)
        print("pos", pos)

        for i in range(100):
            grad = cost.grad_(pos)
            print("grad", grad)
            pos = pos - grad * c

        print("pos2", pos)

        self.slopes = pos[:-1]
        self.b = pos[-1]

    def predict(self, X):
        preds = []
        for point in X:
            exponent = self.b
            print("b", self.b)
            for i in range(len(point)):
                exponent += point[i] * self.slopes[i]
            pred = 1/(1 + np.e**(-exponent))
            print("exp:", exponent)
            print("pred", pred)
            if pred >= 0.5:
                preds.append(1)
            else:
                preds.append(0)
        return preds

    def make_cost_function(self):

        vars_ = []
        for _ in range(len(self.X[0]) + 1):
            vars_.append(Variable())

        hats = []
        for i in range(len(self.X)):
            temp = vars_[len(vars_) - 1]
            for j in range(len(self.X[i])):
                prod = self.X[i][j] * vars_[j]
                temp = temp + prod
            temp = -1 * temp
            temp = np.e**temp
            temp = temp + 1
            temp = 1 / temp
            hats.append(temp)

        terms = []
        for i in range(len(hats)):
            temp = hats[i].ln()
            temp = temp * self.y[i]
            temp2 = 1 - hats[i]
            temp2 = temp2.ln()
            temp2 = temp2 * (1-self.y[i])
            terms.append(temp + temp2)

        temp = 0
        for i in range(len(terms)):
            temp = temp + terms[i]

        return temp/len(self.y)
