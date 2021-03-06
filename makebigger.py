#originally made by miachel nielson
# i am also using .npy files instead of .gz files
import os.path
import random
override = True
import pickle
# Third-party libraries
import numpy as np

print("Expanding the training set")
def expand(image):
    expanded = []
    img = np.reshape(image, (-1, 25))
    for d, axis, index_position, index in [
            (1,  0, "first", 0),
            (-1, 0, "first", 24),
            (1,  1, "last",  0),
            (-1, 1, "last",  24)]:
        new_img = np.roll(img, d, axis)
        if index_position == "first":
            new_img[index, :] = np.zeros(25)
        else:
            new_img[:, index] = np.zeros(25)
        expanded.append((np.reshape(new_img, (625,-1)), y))
    return (expanded[x] for x in range(4))


if os.path.exists("data/data_expanded.data") and override == False:
    print("The expanded training set already exists.  Exiting.")
else:
    f = open("data/data.data","rb")
    training_data = pickle.load(f)
    expanded_training_pairs = []
    f.close()
    j = 0 # counter
    for example in training_data:
        x = example[0]
        y = example[1]
        expanded_training_pairs.append((x, y))
        image = np.reshape(x, (-1, 25))
        j += 1
        if j % 1000 == 0: print("Expanding image number", j)
        # iterate over data telling us the details of how to
        # do the displacement
        for d, axis, index_position, index in [
                (1,  0, "first", 0),
                (-1, 0, "first", 24),
                (1,  1, "last",  0),
                (-1, 1, "last",  24)]:
            new_img = np.roll(image, d, axis)
            if index_position == "first":
                new_img[index, :] = np.zeros(25)
            else:
                new_img[:, index] = np.zeros(25)
            expanded_training_pairs.append((np.reshape(new_img, (625,-1)), y))
    random.shuffle(expanded_training_pairs)
    expanded_training_data = [list(d) for d in zip(*expanded_training_pairs)]
    print("Saving")
    f = open("data/data_expanded.data","wb")
    pickle.dump(expanded_training_pairs,f)
    f.close()
    print(len(expanded_training_pairs),"images")
