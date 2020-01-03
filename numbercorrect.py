import pickle
from learn import Network
import numpy as np
f = open("data_2.data","rb")
params = pickle.load(f)
f.close()
inputweights = params[0]
inputbiases = params[1]
network = Network([625,15,2],inputweights,inputbiases)
f= open("test_data.data","rb")
test_data = pickle.load(f)
f.close()
corr = 0
for img in test_data:
    test = network.feedforward(img[0])

    if test[0][0]>test[1][0] and img[1][0][0]>img[1][1][0]:
        corr+=1
    if test[0][0]<test[1][0] and img[1][0][0]<img[1][1][0]:
        corr+=1
print(str(corr)+"/"+str(len(test_data)))
print(corr/len(test_data))
