import pygame
import pickle
from enterdata import Screen
from learn import Network,layers
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
network = Network(layers,inputweights,inputbiases)
output = network.feedforward(Screen(scale).update_test(win))
if output[0][0] < output[1][0]:
  print("frowney face")
else:
  print("smiely face")
print(output)
