inputweights = []#put answers from training here
inputbiases = []
import enterdata
screen  = Screen()
network = Network([625,15,2],inputweights,inputbiases)
output = network.feedforward(screen.update_test())
if np.argmax(output) = output[1][0]:
  print(frowney face)
else:
  print(smiely face)
