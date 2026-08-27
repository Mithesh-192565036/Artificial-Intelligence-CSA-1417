import numpy as np

# Sigmoid Activation Function
def sigmoid(x):
  return 1 / (1 + np.exp(-x))

# Feedforward computation
def feedforward(X, W1, b1, W2, b2):
  # Hidden layer calculation
  hidden_input = np.dot(X, W1) + b1
  hidden_output = sigmoid(hidden_input)

  # Output layer calculation
  final_input = np.dot(hidden_output, W2) + b2
  final_output = sigmoid(final_input)

  return final_output

# Inputs: 2 samples, 3 features each
X = np.array([
    [0.5, 0.2, 0.1],
    [0.9, 0.7, 0.3]
])

# Reproducible random weights initialization
np.random.seed(42)

# Layer 1 weights (3 input features -> 4 hidden units)
W1 = np.random.randn(3, 4)
b1 = np.zeros((1, 4))

# Layer 2 weights (4 hidden units -> 1 output unit)
W2 = np.random.randn(4, 1)
b2 = np.zeros((1, 1))

# Execute forward pass
output = feedforward(X, W1, b1, W2, b2)

print("Neural Network Output Predictions:\n", output)