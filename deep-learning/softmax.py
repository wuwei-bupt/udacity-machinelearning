"""Softmax."""

import numpy as np
import math


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # TODO: Compute and return softmax(x)
    return np.exp(x)/np.sum(np.exp(x), axis=0)

# test case 1
scores = np.array([3.0, 1.0, 0.2])
print(softmax(scores))
# Multiply the score by 10. What happens?
print(softmax(scores*10))
# Divide the score by 10. What happens?
print(softmax(scores/10))

# Plot softmax curves
import matplotlib.pyplot as plt

x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
