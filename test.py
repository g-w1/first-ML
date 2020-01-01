def feedforward(weights,biases,a):
  for w,b in zip(weights,biases):
    a = sigmoid(np.dot(w, a)+b)
      return a
def sigmoid(z):
  def sigmoid(z):
    """The sigmoid function."""
  return 1.0/(1.0+np.exp(-z))
import enterdata
screen  = Screen()
output = feedforward(weight,bias,screen.update_test())
if output[1]>.5:
  print("smiely")
else:
  print("frowny")
