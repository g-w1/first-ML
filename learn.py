
#some of this code was made by miachel neilsen
import random
import pickle
import os
import numpy as np
class Population:
	#class to manage networks
	def __init__(self,n,layers):
		self.number = n
		self.genepool = []
		self.pop = []
		for x in range(n):
			self.pop.append(Network(layers))
		#makes n networks with layers layers
	def addgenepool(self):
		global training_data
		for network in self.pop:
			for x in round(network.fitness_numcor(training_data)):
				self.genepool.append(network.mutate(.04,.1))
		#adds each network to the genepool its finess times
	def createnewpop(self):
		self.pop = []
		for x in range(self.number):
			self.pop.append(self.genepool.pop(random.randint(0,len(self.genepool)-1)))
		#takes the genepool and selects a random element to add to the pop n times
class Network:
    def __init__(self, sizes, weights = None, biases = None):
		#creates a network of size layers with random weights and biases unless weighs and biases are specified
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)/np.sqrt(x/5) for x, y in zip(sizes[:-1], sizes[1:])]
        if biases:
            self.biases = biases
        if weights:
            self.weights = weights

    def feedforward(self, a):
        #Return the output of the network if a is input
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a
    def fitness_numcor(self,training_data):
		#a fitness function for a network that is calculated by how many it gets correct
        for img in test_data:
            test = self.feedforward(img[0])
            if test[0][0]>test[1][0] and img[1][0][0]>img[1][1][0]:
                corr+=1
            if test[0][0]<test[1][0] and img[1][0][0]<img[1][1][0]:
                corr+=1
        if 100(corr/len(training_data))>70:
            print("working")
        return 100 *(corr/len(training_data))
    def fitness_cost(self,training_data):
		#a fitness function for a network that is calculated inversely to the average cost
		costtotal = []
        for img in test_data:
            test = self.feedforward(img[0])
            cost = np.mean(np.absolute(img[1]-test))
            costtotal.append(cost)
		z = 100*(1/np.mean(costtotal))
		if z>70:
			print("working")
		if z>90:
			f = open("data/data_2.data","w")
			pickle.save([self.weights,self.biases],f)
			f.close()
        return z
    def mutate(self,mutation_rate,changerate):
		#changes mutation_rate elements changerate*1,-1
		def inputrandom(n,mutationrate,changerate):
			#returns a mutated number given an input
			r = random.uniform(0, 1)
			if r<mutationrate:
				a = random.randint(0,1)
				if a == 0:
					a = 1
				return n+=a*changerate
		for i in self.weights:
			for a in i:
				for b in a:
					inputrandom(b,.mutationrate,changerate)
		for i in self.biases:
			for a in i:
				for b in a:
					inputrandom(b,.mutationrate,changerate)
def sigmoid(z):
    #The sigmoid function
    return 1.0/(1.0+np.exp(-z))
#the topology of each neuron
layers = [625,10,2]
if __name__ == "__main__":
    f = open("data/data_expanded.data","rb")
    training_data = pickle.load(f)
    f.close()
	#create 1000 networks
	networks = Population(1000,layers)
	exit = False
	counter = 1
	while not(exit):
		c+=1
		if c>100000:
			exit = True
		#main loop
		networks.addgenepool()
		networks.createnewpop()
	
