import numpy as np

np.random.seed(0)

X, y = np.array([1.3, 4.5, 3.6, 8.6, 4.5, 3.5]), np.array([0, 0, 0, 1, 0, 0])


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


layer1 = Layer_Dense(X.shape[0], 6)
activation1 = Activation_ReLU()

layer1.forward(X)

# print(layer1.output)
activation1.forward(layer1.output)
print(activation1.output)
