def feedforward(weights,biases,a):
  for w,b in zip(weights,biases):
    a = sigmoid(np.dot(w, a)+b)
      return a
def sigmoid(z):
  def sigmoid(z):
    """The sigmoid function."""
  return 1.0/(1.0+np.exp(-z))
