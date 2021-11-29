import numpy as np

inputs = [[1.2, 5.1, 2.1, 3.6],
            [1.2, -5.1, 2.1, 3.4],
            [-1.2, 6.1, 4.3, -8.5]]

weights = [[0.1, 0.2, 0.3, 0.4],
            [0.3, 0.9, 0.6, 0.5],
            [0.4, 0.5, 0.6, 0.7]]

biases = [2, 3, 0.5]

weights2 = [[0.4, 0.7, 0.2],
            [1.3, 0.5, 0.9],
            [-0.4, 0.8, 0.1]]

biases2 = [1.2, 0.1, 0.9]

layer_1 = np.dot(inputs, np.array(weights).T) + biases

layer_2 = np.dot(layer_1, np.array(weights2).T) + biases2


print(layer_2)
