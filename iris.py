# /------------------------------------------------------------------------------------------------------------------\ #
# |                                                 Import statements                                                | #
# \------------------------------------------------------------------------------------------------------------------/ #
import tensorflow as tf
import pandas as pd
import numpy as np


def get_data(predictor_columns, shuffle_data, test_size):
    """Read the dataset from the CSV file and prepare the data for using it in training and testing the neural network.
    :param predictor_columns: The names of the columns used for predicting the classes (the Iris species)
    :param shuffle_data: Whether or not the data is shuffled before using it for the neural network
    :param test_size: The number of rows in the dataset of 150 rows in total which will be used for testing
    :return: A list with Iris classes (the three species) and the test and training datasets containing the predictor
             values and containing the classes."""
    # Load the dataset from the file
    dataset = pd.read_csv('iris_data.csv')
    iris_classes = dataset['Species'].unique()  # Create a list with all Iris species
    dataset = pd.get_dummies(dataset, columns=['Species'])  # One Hot encoding

    # Select the correct classification and predictor columns and make numpy arrays of them with the correct types
    # Classification columns: 'Species_Iris-setosa', 'Species_Iris-versicolor', 'Species_Iris-virginica'
    y = dataset[list(dataset.columns.values)[-3:]]
    y = np.array(y, dtype='float32')

    # Predictor columns: (a subset of) 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'
    x = dataset[predictor_columns]
    x = np.array(x, dtype='float32')

    # Shuffle the data; initially the data is ordered based on their class
    if shuffle_data:
        indices = np.random.choice(len(x), len(x), replace=False)
        x_values, y_values = x[indices], y[indices]
    else:
        x_values, y_values = x, y

    # Create a train set and a test set. Total dataset size is 150.
    x_testset = x_values[-test_size:]
    x_trainset = x_values[:-test_size]
    y_testset = y_values[-test_size:]
    y_trainset = y_values[:-test_size]

    return iris_classes, x_testset, x_trainset, y_testset, y_trainset


def create_neural_network(predictor_columns, number_of_hidden_nodes, learning_rate):
    """Create the neural network, without training it.
    :param predictor_columns: The names of the predictor columns to be used
    :param number_of_hidden_nodes: The number of hidden nodes of the single hidden layer
    :param learning_rate: The learning rate of the neural network
    :return: The session, optimizer, loss function, input-placeholder, output-placeholder, the final_output variable"""
    # Start the Tensorflow Session
    sess = tf.Session()

    # Number of nodes in the three layers
    input_layer_nodes = len(predictor_columns)  # The number of predictor columns
    hidden_layer_nodes = number_of_hidden_nodes
    output_layer_nodes = 3  # The three Iris classes

    # Initialize placeholders for the nodes in the input and the output layers
    x_data = tf.placeholder(shape=[None, input_layer_nodes], dtype=tf.float32)
    y_target = tf.placeholder(shape=[None, output_layer_nodes], dtype=tf.float32)

    # Create variables for Neural Network layers
    w1 = tf.Variable(tf.random_normal(shape=[input_layer_nodes, hidden_layer_nodes]))  # Inputs -> Hidden Layer
    b1 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes]))   # First Bias
    w2 = tf.Variable(tf.random_normal(shape=[hidden_layer_nodes, output_layer_nodes]))  # Hidden layer -> Outputs
    b2 = tf.Variable(tf.random_normal(shape=[output_layer_nodes]))   # Second Bias

    # Operations (the activation functions of the hidden and output nodes)
    hidden_output = tf.nn.relu(tf.add(tf.matmul(x_data, w1), b1))
    final_output = tf.nn.softmax(tf.add(tf.matmul(hidden_output, w2), b2))

    # Cost Function
    loss = tf.reduce_mean(-tf.reduce_sum(y_target * tf.log(final_output), axis=0))

    # Optimizer
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

    # Initialize variables and start the session
    init = tf.global_variables_initializer()
    sess.run(init)

    return sess, optimizer, loss, x_data, y_target, final_output


def train_neural_network(session, optimizer, loss, epochs, x_placeholder, y_placeholder, x_train, y_train):
    """Train the neural network.
    :param session: The session in which the network resides
    :param optimizer: The optimizer used to optimize the quality of the neural network
    :param loss: The loss function used by the optimizer. This is the difference between actual and predicted classes
    :param epochs: The number of times the entire train set will be used for training the neural network
    :param x_placeholder: The TensorFlow placeholder for the input
    :param y_placeholder: The TensorFlow placeholder for the output (the classes)
    :param x_train: The predictor data to train the network on
    :param y_train: The class data on which the netowrk is trained
    :return: Nothing: the network in the session is updated"""
    print('Training the model...')
    for i in range(1, (epochs + 1)):
        session.run(optimizer, feed_dict={x_placeholder: x_train, y_placeholder: y_train})
        if i % 50 == 0:
            print('Epoch', i, '|', 'Loss:',
                  session.run(loss, feed_dict={x_placeholder: x_train, y_placeholder: y_train}))


def calculate_confusion_matrix(y_test, y_pred, iris_classes, session):
    """Calculate the confusion matrix from the test classes and the predicted classes by the neural network.
    :param y_test: The actual classes of the test data
    :param y_pred: The predicted classes of the test data
    :param iris_classes: The names of the Iris species (the names of the classes)
    :param session: The session in which the neural network resides
    :return: Nothing; this def will output the confusion matrix"""
    conf_matrix = tf.confusion_matrix(tf.argmax(y_test, 1), tf.argmax(y_pred, 1), num_classes=len(iris_classes))
    eval_conf_matrix = tf.Tensor.eval(conf_matrix, feed_dict=None, session=session)

    labels = [x + (' ' * (len(max(iris_classes, key=len)) - len(x))) for x in iris_classes]
    print(24 * " " + " ".join(labels))
    for count, (row_label, row) in enumerate(zip(labels, eval_conf_matrix)):
        print('%s %s' % (row_label, ' '.join('%15s' % i for i in row)))


def create_train_and_predict():
    """Create the neural network, train the neural network, predict the neural network and obtain the confusion matrix
    with the quality of the neural network."""

    # /--------------------------------------------------------------------------------------------------------------\ #
    # |                                           Neural network parameters                                          | #
    # \--------------------------------------------------------------------------------------------------------------/ #
    # Columns used to predict the Iris-classes. This is equal to the number of input variables of the neural network
    predictor_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

    # Whether or not the input data is be shuffled. Initially, the first 50 rows are Iris Setosa, the next 50 rows are
    # Iris Versicolor and the last 50 rows are Iris Virginica.
    shuffle_data = True

    # Number of rows to be used for testing. In total there are 150 rows in the dataset.
    test_size = 20

    # The number of epochs. A single epoch will use all rows of the dataset (minus the rows reserved for testing)
    # exactly once in order to update the parameters of all hidden and output nodes.
    epochs = 500

    # In this network there is one single hidden layer. This variable defines the number of nodes in this layer.
    number_of_hidden_nodes = 8

    # The learning rate of the training of the network
    learning_rate = 0.001

    # /--------------------------------------------------------------------------------------------------------------\ #
    # |                                         End neural network parameters                                        | #
    # \--------------------------------------------------------------------------------------------------------------/ #

    # Make the results reproducible
    seed = 42
    np.random.seed(seed)
    tf.set_random_seed(seed)

    # Get all required data from the dataset and make it neural network-ready
    iris_classes, x_test, x_train, y_test, y_train = get_data(predictor_columns, shuffle_data, test_size)

    # Create the neural network and get all variables required for training and predicting
    session, optimizer, loss, x_placeholder, y_placeholder, final_output = \
        create_neural_network(predictor_columns, number_of_hidden_nodes, learning_rate)

    # Train the neural network; there will be no output as the trained network is in the session variable
    train_neural_network(session, optimizer, loss, epochs, x_placeholder, y_placeholder, x_train, y_train)

    # Predict the values for the test data
    y_pred = np.rint(session.run(final_output, feed_dict={x_placeholder: x_test}))

    # Calcualte the confusion matrix and show it
    calculate_confusion_matrix(y_test, y_pred, iris_classes, session)


create_train_and_predict()
