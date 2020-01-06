
#some of this code was made by miachel neilsen
import random
import pickle
import os

# Third-party libraries
import numpy as np
class Network:
    def __init__(self, sizes, weights = None, biases = None):
        """The list ``sizes`` contains the number of neurons in the
        respective layers of the network.  For example, if the list
        was [2, 3, 1] then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron.  The biases and weights for the
        network are initialized randomly, using a Gaussian
        distribution with mean 0, and variance 1.  Note that the first
        layer is assumed to be an input layer, and by convention we
        won't set any biases for those neurons, since biases are only
        ever used in computing the outputs from later layers."""
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)/np.sqrt(x/5)
                        for x, y in zip(sizes[:-1], sizes[1:])]
        if biases:
            self.biases = biases
        if weights:
            self.weights = weights

    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

    def fitness_numcor(self,training_data):
        for img in test_data:
            test = self.feedforward(img[0])

            if test[0][0]>test[1][0] and img[1][0][0]>img[1][1][0]:
                corr+=1
            if test[0][0]<test[1][0] and img[1][0][0]<img[1][1][0]:
                corr+=1
        return corr/len(training_data)
    def fitness_cost(self,training_data):
        costtotal = []
        for img in test_data:
            test = self.feedforward(img[0])
            cost = np.mean(np.absolute(img[1]-test))
            costtotal.append(cost)
        return np.mean(costtotal)
    def mutate(self):
		pass
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))
    #return np.maximum(0,z)
layers = [625,10,2]
if __name__ == "__main__":
    f = open("data/data_expanded.data","rb")
    training_data = pickle.load(f)
    f.close()
    learningrate = 4
    mini_batch_size = 4
    epochs = 5
    net = Network(layers)
    net.SGD(training_data, epochs, mini_batch_size, learningrate)
    f = open("data/data_2.data","wb")
    pickle.dump([net.weights,net.biases],f)
    f.close
    os.system("python numbercorrect.py")
