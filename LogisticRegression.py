import numpy as np

class LogisticRegression:

    def __init__(self):


    def get_grad(self, X, y):

    def fit(self, X, y):

        self.X = X
        self.y = y


    def  make_cost_function(self):

        vars_ = []
        for _ in range(len(slopes) + 1):
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
            hats.append(1 / temp)

        terms = []
        for i in range(len(hats)):
            temp = hats[i].ln()
            temp = temp * self.y[i]
            temp2 = 1 - hats[i]
            temp2 = temp2.ln()
            temp2 = temp2 * (1-y[i])
            terms.append(temp + temp2)
