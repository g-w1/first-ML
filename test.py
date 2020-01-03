import pygame
import pickle
from enterdata import Screen
from learn import Network
import numpy as np
scale = 25
f = open("data_2.data","rb")
params = pickle.load(f)
f.close()
inputweights = params[0]
inputbiases = params[1]
import enterdata
pygame.init()
win = pygame.display.set_mode((25*scale,25*scale))
network = Network([625,15,2],inputweights,inputbiases)
output = network.feedforward(Screen(scale).update_test(win))
if output[0][0] < output[1][0]:
  print("frowney face")
else:
  print("smiely face")
print(output)
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
