# -----------------------------------

#
#   In this exercise we write a perceptron class
#   which can update its weights
#
#   Your job is to finish the train method so that it implements the perceptron update rule

import numpy as np
import random


class Perceptron:
    def activate(self, value):
        '''Takes in @param values, @param weights lists of numbers
        and @param threshold a single number.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        '''

        # First calculate the strength with which the perceptron fires
        strength = 0
        for i in range(len(value)):
            strength += value[i] * self.weights[i]

        # if strength>self.threshold:
        #     result = 1
        # else:
        #     result = 0

        return strength

    def update(self, values, train, eta=.1):
        '''Takes in a 2D array @param values consisting of a LIST of inputs
        and a 1D array @param train, consisting of a corresponding list of
        expected outputs.
        Updates internal weights according to the perceptron training rule
        using these values and an optional learning rate, @param eta.
        '''
        # YOUR CODE HERE
        # update self.weights based on the training data
        print values, train
        self.weights = [1 for item in values[0]]
        print self.weights, self.threshold
        self.threshold = 0
        iteration = 0
        while iteration < 100:
            print iteration, self.weights
            iteration += 1
            for i in range(len(values[0])):
                # updata the weigths
                diff = [train[j] - self.activate(values[j]) for j in range(len(values))]
                x_i = [values[j][i] for j in range(len(values))]
                print diff, x_i
                self.weights[i] += eta * np.dot(diff, x_i)
        return self.weights

    def __init__(self, weights=None, threshold=None):
        if weights is not None:
            self.weights = weights
        if threshold is not None:
            self.threshold = threshold