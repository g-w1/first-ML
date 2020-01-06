
#some of this code was made by miachel neilsen
import random
import pickle
import os

# Third-party libraries
import numpy as np
class Population:
	def __init__(self,n,layers):
		self.number = n
		self.genepool = []
		self.pop = []
		for x in range(n):
			self.pop.append(Network(layers))
	def addgenepool(self):
		global training_data
		for network in self.pop:
			for x in round(network.fitness_numcor(training_data)):
				self.genepool.append(network.mutate(.04))
	def createnewpop(self):
		self.pop = []
		for x in range(self.number):
			self.pop.append(self.genepool.pop(random.randint(0,len(self.genepool)-1)
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
        self.weights = [np.random.randn(y, x)/np.sqrt(x/5) for x, y in zip(sizes[:-1], sizes[1:])]
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
        if corr/len(training_data)>70:
            print("working")
        return corr/len(training_data)
    def fitness_cost(self,training_data):
		costtotal = []
        for img in test_data:
            test = self.feedforward(img[0])
            cost = np.mean(np.absolute(img[1]-test))
            costtotal.append(cost)
        return np.mean(costtotal)
    def mutate(self,mutation_rate):

		def inputrandom(n,mutationrate,changerate):
			r = random.uniform(0, 1)
			if r<mutationrate:
				a = random.randint(0,1)
				if a == 0:
					a = 1
				return n+=a*changerate
		for i in self.weights:
			for a in i:
				for b in a:
					inputrandom(b,.mutationrate,.1)
		for i in self.biases:
			for a in i:
				for b in a:
					inputrandom(b,.mutationrate,.1)
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))
    #return np.maximum(0,z)
layers = [625,10,2]
if __name__ == "__main__":
    f = open("data/data_expanded.data","rb")
    training_data = pickle.load(f)
    f.close()
