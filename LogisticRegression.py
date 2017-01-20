'''
Group Names: Lior Hirschfeld, Henry Desai, Pham Nhat, and Jihoun Im
Class: Compsci 630 Machine Learning
Teacher: Dr. Z
'''

import numpy as np
import matplotlib.pyplot as plt
from VariableClass.Variable import Variable

class LogisticRegression:

    def __init__(self):
        return

    # Set verbose to true if you wish to plot the cost over time.
    def fit(self, X, y, ss=1, verbose=False):
        Variable.clear_wengert()
        self.X = X
        self.y = y
        cost = self.make_cost_function()

        if verbose:
            costs = []
        # Starting points
        pos = np.random.rand(len(X[0])+1)*10

        for i in range(100):
            grad = cost.grad_(*pos)
            pos = pos - grad * ss #ss is the hyper-parameter stepsize
            if verbose:
                costs.append(cost(*pos))

        self.slopes = pos[:-1]
        self.b = pos[-1]

        if verbose:
            plt.plot(np.linspace(0, 99, num=100), costs, 'ro')
            plt.axis([0, 90, min(costs), max(costs)])
            plt.show()

    def predict(self, X):
        preds = []
        for point in X:
            exponent = self.b
            for i in range(len(point)):
                exponent += point[i] * self.slopes[i]
            pred = 1/(1 + np.e**(-exponent))
            if pred >= 0.5:
                preds.append(1)
            else:
                preds.append(0)
        return preds

    def make_cost_function(self):

        vars_ = [] #list of all the m values from 1/(1+e^(-(mx + b)))
        for _ in range(len(self.X[0]) + 1):
            vars_.append(Variable())

        hats = [] #computes all y-hat values and appends them to list hats
        for i in range(len(self.X)):
            temp = vars_[len(vars_) - 1]
            for j in range(len(self.X[i])):
                prod = self.X[i][j] * vars_[j]
                temp = temp + prod
            temp = -1 * temp
            temp = np.e**temp
            temp = temp + 1.01 # Prevents divide by zero errors.
            temp = 1 / temp
            hats.append(temp)

        terms = [] #creates the cost function and apppends them to terms
        for i in range(len(hats)):
            temp = hats[i].ln()
            temp = temp * self.y[i]
            temp2 = 1 - hats[i]
            temp2 = temp2.ln()
            temp2 = temp2 * (1-self.y[i])
            terms.append(temp + temp2)

        #takes the average of all the cost functions
        temp = 0
        for i in range(len(terms)):
            temp = temp + terms[i]

        return temp/(-len(self.y))
