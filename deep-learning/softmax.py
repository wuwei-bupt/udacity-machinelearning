"""Softmax."""

import numpy as np
import math


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # TODO: Compute and return softmax(x)
    if len(x.shape) == 1:
        row, column = x.shape[0], 1
        x = x.reshape((row, column))
    else:
        row, column = x.shape
    result = np.array([[0.0] * column for i in range(row)])

    for j in range(column):
        denominator = 0
        for i in range(row):
            denominator += math.exp(x[i][j])
        for i in range(row):
            result[i][j] = math.exp(x[i][j]) / denominator
    if column == 1:
        result = result.reshape((row,))
    return result


scores = np.array([3.0, 1.0, 0.2])
print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt

x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
print scores

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
