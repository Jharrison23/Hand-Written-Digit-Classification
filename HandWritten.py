

# import MNIST
# The input_data class is a standard python class that downloads the dataset
# splits it into training and testing data, and formats it for use later on
import input_data

mnist = input_data.read_data_sets("/tmp/data", one_hot=True)

import tensorflow as tf

# Set Hyperparameters represent tuning knobs for the model

# Learning rate: Defines how fast we want to update our weights
# if this is too small our model might need too many iterations to converge on
# the best results, if its it too big the model might skip the optimal solution
# 0.01 is a known good learning rate for this particular problem
learning_rate = 0.01

# the number of iterations used for training
training_iteration = 30

batch_size = 100

display_step = 2


# Create our model
# in tensorflow this model is represented as a dataflow graph, the graph contains
# a set of nodes called operations, these are units of computations ranging in
# difficulty from addition to multivariable equations, each operations takes as input
# a tensor and ourputs a tensor

# A tensor is a multi dimensional array and flow between operations, this is how
# data is represented in tensor flow

# Start building our model by creating two operations

# placeholder operations are just variables which we assign data to at a later date
# they are never initialize and doesnt contain data,

# we will define the the type and shape of our data as the parameters
# variable x: Input images represented by a 2d tensor of numbers, 784 is the dimensionalality
# of a single flattened mnist image, flattening an image is when you convert a 2d array
# to a 1d array by unstacking the rows and lining them up 28 * 28 = 784
x = tf.placeholder("float", [none, 784])

#output classes y: consist of a 2d tensor, where each row is a one_hot ten dimensional
# vector showing which digit class the corresponding mnist digit corresponds to
y = tf.placeholder("float", [none, 10])


# Setting model weights
# weights: Probabilities that affect how data flows in the graph
# They are updated continuously during training so closer to the correct solution
w = tf.variable(tf.zeros([784, 10]))

# Define biases
# Bias: Lets us shift our regression line to fit the data better
b = tf.variable(tf.zeros([10]))

# Create a name scope, scopes help us organize nodes in the graph visualizer called tensorboard
with tf.name_scope("Wx_b") as scope:
    # construct linear model
    # Implement the model logistic regression, by using matrix multiplication on the
    # input images x by the weight matrix W and then adding the bias b
    model = tf.nn.softmax(tf.matmul(x, W) + b)
