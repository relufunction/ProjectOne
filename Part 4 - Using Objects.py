import numpy as np

np.random.seed(0)

X = [
    [1, -2, 4, 3.5],
    [4.7, 7.1, -0.5, -1.1],
    [1.2, 5.1, 2.1, 3.6]
]

class Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer_1 = Dense(4, 3)
layer_2 = Dense(3, 2)

layer_1.forward(X)
print(layer_1.output)
layer_2.forward(layer_1.output)
print(layer_2.output)