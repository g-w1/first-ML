
#some of this code was made by miachel neilsen
import random
import pickle
import os
import numpy as np
import keyboard
class Population:
	#class to manage networks
	def __init__(self,n,layers):
		self.number = n
		self.genepool = []
		self.pop = []
		for x in range(self.number):
			self.pop.append(Network(layers))

			#makes n networks with layers layers
	def addgenepool(self):
		self.genepool = []
		global layers
		topfit = Network(layers)
		topfit.fitness_numcor()
		for network in self.pop:
			fit = round(network.fitness_numcor())
			if fit>topfit.fitness:
				topfit = network

		for x in range(round(self.number/2)-1):
			self.genepool.append(topfit)
		for x in range(len(self.genepool)):
			self.genepool[x] = self.genepool[x].mutate(.1,.1)
		self.genepool.append(topfit)

	def createnewpop(self):
		self.pop = []
		for x in range(self.number):
			l = len(self.genepool)-1
			a = random.randint(0,l)
			self.pop.append(self.genepool[a])
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
	def fitness_numcor(self):
		global exit
		corr = 0
		global training_data
		for img in training_data:
			test = self.feedforward(img[0])
			if test[0][0]>test[1][0] and img[1][0]>img[1][1]:
				corr+=1
			if test[0][0]<test[1][0] and img[1][0]<img[1][1]:
				corr+=1
		fit = 100*(corr/len(training_data))
		if fit>70:
			print("working")
		if fit>90:
			f = open("data/data_2.data","w")
			pickle.save([self.weights,self.biases],f)
			f.close()
			exit = True
		print(fit)
		self.fitness = fit
		return 100 *(corr/len(training_data))
	def fitness_cost(self):
		#a fitness function for a network that is calculated inversely to the average cost
		global training_data
		costtotal = []#an array to hold the mean cost for each training example
		for img in training_data:
			test = self.feedforward(img[0])
			cost = np.mean(np.absolute(img[1]-test))
			costtotal.append(cost)

			if z>70:
				print("working")
			if z>90:
				f = open("data/data_2.data","w")
				pickle.save([self.weights,self.biases],f)
				f.close()
		z = 100*(1-(np.mean(costtotal)))
		print(z)
		self.fitness = z
		return z
	def mutate(self,mutation_rate,changerate):
		#changes mutation_rate elements changerate*1,-1
		def inputrandom(n,mutationrate,changerate):
			#returns a mutated number given an input
			r = random.uniform(0, 1)
			if r<mutationrate:
				a = random.randint(0,1)
			else:
				return n
			if a == 0:
				a = -1
			return n+a*changerate
		for i in range(len(self.weights)):
			for a in range(len(self.weights[i])):
				for b in range(len(self.weights[i][a])):
					self.weights[i][a][b] = inputrandom(self.weights[i][a][b],mutation_rate,changerate)
		for i in range(len(self.biases)):
			for a in range(len(self.biases[i])):
				for b in range(len(self.biases[i][a])):
					self.biases[i][a][b] = inputrandom(self.biases[i][a][b],mutation_rate,changerate)
		return self
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
	networks = Population(50,layers)
	exit = False
	counter = 0
	while not(exit):
		if keyboard.is_pressed('q'):
			exit = True
		counter+=1
		print(counter)
		#exit = True
		#main loop
		networks.addgenepool()
		networks.createnewpop()
