from learn import layers
import pickle
f= open('data/data_2.data','rb')
a = pickle.load(f)
f.close()
a.append(layers)
f = open('data/good_data.data',"wb")
pickle.dump(a,f)
f.close()
