

# import MNIST
# The input_data class is a standard python class that downloads the dataset
# splits it into training and testing data, and formats it for use later on
import input_data

mnist = input_data.read_data_sets("/tmp/data", one_hot=True)
