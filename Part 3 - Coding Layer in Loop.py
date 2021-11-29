inputs = [1.2, 5.1, 2.1, 3.4]

weights = [[0.1, 0.2, 0.3, 0.4],
            [0.3, 0.9, 0.6, 0.5],
            [0.4, 0.5, 0.6, 0.7]]

biases = [2, 3, 0.5]

layer_outputs = []
for neron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for neuron_input, weight in zip(inputs, neron_weights):
        neuron_output += neuron_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)
