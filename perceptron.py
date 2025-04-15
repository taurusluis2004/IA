# Inputs and expected outputs
input1 = [1, 1, 0, 1, 0, 1, 1, 0, 1, 0]
input2 = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
output_expected = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]

# Initialize weights and parameters
weights = [0, 0]  # Weights for input1 and input2
learning_rate = 0.6  # Learning rate

# Perceptron output function
def output(input1, input2):
    result = weights[0] * input1 + weights[1] * input2
    return 1 if result >= 0 else 0  # Threshold function

# Correct weights function
def correct_(error, input1, input2):
    global weights
    # Update weights based on error
    weights[0] += learning_rate * error * input1
    weights[1] += learning_rate * error * input2

# Train function
def train(input1, input2, output_expected):
    global weights
    for epoch in range(10):  # Train for 10 epochs
        for i in range(len(input1)):
            predicted = output(input1[i], input2[i])  # Predicted output
            error = output_expected[i] - predicted  # Error calculation
            correct_(error, input1[i], input2[i])  # Adjust weights
        print(f"Epoch {epoch + 1}: Weights: {weights}")

# Use the perceptron
def use(inputuse, inputuse2):
    for i in range(len(inputuse)):
        print(f"Input: ({inputuse[i]}, {inputuse2[i]}) => Output: {output(inputuse[i], inputuse2[i])}")

# Run the training
train(input1, input2, output_expected)

# Test the perceptron with new inputs
print("Testing perceptron:")
inputuse = [0, 0, 1, 1, 1]
inputuse2 = [0, 0, 0, 1, 1]
use(inputuse, inputuse2)
print(input1)
print(input2)
print("hahaha")
