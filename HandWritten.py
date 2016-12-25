

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
