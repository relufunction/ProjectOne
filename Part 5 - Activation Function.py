import numpy as np

np.random.seed(0)

X = np.random.randint(-10, 10, (5, 10))

class Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
    
class ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)



layer_1 = Dense(10, 5)
layer_2 = Dense(5, 4)
activation1 = ReLU()
activation2 = ReLU()


layer_1.forward(X)
#print(layer_1.output)
activation1.forward(layer_1.output)
layer_2.forward(activation1.output)
#print(layer_2.output)
activation2.forward(layer_2.output)

print(activation2.output)
