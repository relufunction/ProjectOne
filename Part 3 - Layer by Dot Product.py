import numpy as np

inputs = [1.2, 5.1, 2.1, 3.4]

weights = [[0.1, 0.2, 0.3, 0.4],
            [0.3, 0.9, 0.6, 0.5],
            [0.4, 0.5, 0.6, 0.7]]

biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases


print(output)
