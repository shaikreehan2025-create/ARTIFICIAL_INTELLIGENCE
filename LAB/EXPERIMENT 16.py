import math

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

# XOR Truth Table Dataset: Inputs (X) and Target (Y)
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0, 1, 1, 0]

# Network Architecture: 2 Input neurons, 2 Hidden neurons, 1 Output neuron
w_input_hidden = [[0.5, -0.2], [-0.3, 0.8]]
b_hidden = [0.1, -0.1]
w_hidden_output = [0.7, -0.4]
b_output = 0.2
learning_rate = 0.5
epochs = 5000

print("Feed Forward Neural Network with Backpropagation (Learning XOR):\n")
print("Input Layer: 2 neurons | Hidden Layer: 2 neurons | Output Layer: 1 neuron")
print(f"Learning Rate: {learning_rate} | Training Epochs: {epochs}\n")

for epoch in range(epochs):
    total_error = 0.0
    for i in range(len(X)):
        # 1. Forward Propagation
        h1 = sigmoid(X[i][0] * w_input_hidden[0][0] + X[i][1] * w_input_hidden[1][0] + b_hidden[0])
        h2 = sigmoid(X[i][0] * w_input_hidden[0][1] + X[i][1] * w_input_hidden[1][1] + b_hidden[1])
        out = sigmoid(h1 * w_hidden_output[0] + h2 * w_hidden_output[1] + b_output)

        error = Y[i] - out
        total_error += error ** 2

        # 2. Backpropagation
        out_delta = error * sigmoid_derivative(out)
        h1_delta = out_delta * w_hidden_output[0] * sigmoid_derivative(h1)
        h2_delta = out_delta * w_hidden_output[1] * sigmoid_derivative(h2)

        # 3. Update Weights & Biases
        w_hidden_output[0] += learning_rate * out_delta * h1
        w_hidden_output[1] += learning_rate * out_delta * h2
        b_output += learning_rate * out_delta

        w_input_hidden[0][0] += learning_rate * h1_delta * X[i][0]
        w_input_hidden[1][0] += learning_rate * h1_delta * X[i][1]
        w_input_hidden[0][1] += learning_rate * h2_delta * X[i][0]
        w_input_hidden[1][1] += learning_rate * h2_delta * X[i][1]
        b_hidden[0] += learning_rate * h1_delta
        b_hidden[1] += learning_rate * h2_delta

print(f"Training Completed. Final Mean Squared Error: {total_error / 4:.5f}\n")
print("Testing Predictions on XOR Input Data:")
for i in range(len(X)):
    h1 = sigmoid(X[i][0] * w_input_hidden[0][0] + X[i][1] * w_input_hidden[1][0] + b_hidden[0])
    h2 = sigmoid(X[i][0] * w_input_hidden[0][1] + X[i][1] * w_input_hidden[1][1] + b_hidden[1])
    pred = sigmoid(h1 * w_hidden_output[0] + h2 * w_hidden_output[1] + b_output)
    print(f"  Input: {X[i]} -> Predicted: {pred:.4f} (Rounded: {round(pred)}), Expected: {Y[i]}")