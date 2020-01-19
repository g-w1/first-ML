import json
from learn import layers
import pickle
import numpy
f= open('data/data_2.data','rb')
a = pickle.load(f)
f.close()
weights = [z.tolist() for z in a[0]]
biases = [z.tolist() for z in a[1]]
json_data = json.dumps({"weights":weights,"biases":biases})
print(json_data)
with open('docs/weights_biases.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
a.append(layers)
f = open('data/good_data.data',"wb")
pickle.dump(a,f)
f.close()