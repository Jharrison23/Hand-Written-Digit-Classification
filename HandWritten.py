# Machine learning program written in python which buids a handwritten digit image classifier
# and trains this classifier to recognize images in the MNIST digit dataset.
# uses logistic regression as its model and will test and train on the mnist dataset
# tensorboard can then be used to view the constructed data

# This was written by James Harrison following along with an open source tutorial

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
x = tf.placeholder("float", [None, 784])

#output classes y: consist of a 2d tensor, where each row is a one_hot ten dimensional
# vector showing which digit class the corresponding mnist digit corresponds to
y = tf.placeholder("float", [None, 10])


# Setting model weights
# weights: Probabilities that affect how data flows in the graph
# They are updated continuously during training so closer to the correct solution
w = tf.Variable(tf.zeros([784, 10]))

# Define biases
# Bias: Lets us shift our regression line to fit the data better
b = tf.Variable(tf.zeros([10]))

# Create a name scope, scopes help us organize nodes in the graph visualizer called tensorboard
with tf.name_scope("Wx_b") as scope:
    # construct linear model
    # Implement the model logistic regression, by using matrix multiplication on the
    # input images x by the weight matrix W and then adding the bias b
    model = tf.nn.softmax(tf.matmul(x, w) + b)


# summary operations for collecting data
# These help visualize the distribution of our weights and biases
w_h = tf.histogram_summary("weights", w)
b_h = tf.histogram_summary("bias", b)


# Another Scope, create a cost function to help minimize our error during training
with tf.name_scope("cost_function") as scope:
    # Uses cross entropy to minimize error
    cost_function = -tf.reduce_sum(y*tf.log(model))

    # crete a summary to monitor the cost function
    tf.scalar_summary("cost_function", cost_function)


# Last scope used, create an optimization function that makes our model improve during training
with tf.name_scope("train") as scope:

    # Gradiant descent algorithm which takes our learning rate as a parameter for pacing
    # and our cost funtion as a parameter to help minimize the error
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)


# initialize all the variables
init = tf.initialize_all_variables()


# Merge all of our summaries into a single operator
merged_summary_op = tf.merge_all_summaries()


# initialize a session which is going to let us execute our dataflow graph
with tf.Session() as sess:
    sess.run(init)

    # set our summary writer folder location which will load data to visualize in tensor board
    summary_writer = tf.train.SummaryWriter('/Users/jamesharrison/Downloads/Hand-Written-Digit-Classification/', graph_def=sess.graph_def)

    # Training cycle
    for iteration in range(training_iteration):

        #initialize average cost
        avg_cost = 0

        # compute batch size
        total_batch = int(mnist.train.num_examples/batch_size)

        # Loop over all batches
        for i in range(total_batch):

            batch_xs, batch_ys = mnist.train.next_batch(batch_size)

            # Fit our model using the batch data and the gradiant descent algorithm for backpropagation
            sess.run(optimizer, feed_dict={x: batch_xs, y:batch_ys})

            # compute the average loss
            avg_cost  += sess.run(cost_function, feed_dict={x: batch_xs, y: batch_ys})/total_batch

            # write logs for each iteration
            summary_str = sess.run(merged_summary_op, feed_dict={x: batch_xs, y: batch_ys})
            summary_writer.add_summary(summary_str, iteration*total_batch + i)

        # Display the logs for each iteration step
        if iteration % display_step == 0:
            print ("Iteration:", '%04d' % (iteration + 1), "cost=", "{:.9f}".format(avg_cost))


    print ("Tuning Completed!")

    # Test model
    predictions = tf.equal(tf.argmax(model, 1), tf.argmax(y, 1))

    #calculate the accuracy
    accuracy = tf.reduce_mean(tf.cast(predictions, "float"))

    print("Accuracy", (accuracy.eval({x: mnist.test.images, y: mnist.test.labels})) * 100 )
