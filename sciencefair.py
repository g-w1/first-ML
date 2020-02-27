import pickle
from learn import Network,layers
import numpy as np
import os
network = Network(layers)
f= open("data/data_expanded.data","rb")
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
if corr/len(test_data)<=.945:
    os.system("python3 learn.py")
