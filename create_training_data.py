import os
import cv2 
import matplotlib.pyplot as plt
import random
import numpy as np
import pickle

DATADIR = "C:\\users\\leslie\\desktop\\code\\python\\rex"
CATEGORIES = ["Jump","Stay"]
training_data = []

def create_training_data():
	for category in CATEGORIES:
		PATH = os.path.join(DATADIR,category)
		CLASSIFICATION_NUMBER = CATEGORIES.index(category)
		for image in os.listdir(PATH):
			image_array = cv2.imread(os.path.join(PATH,image),cv2.IMREAD_GRAYSCALE)
			new_image_array = cv2.resize(image_array,(57,19))
			training_data.append([new_image_array,CLASSIFICATION_NUMBER])

create_training_data()

random.shuffle(training_data)

X = []
y = []

for feature, label in training_data:
	X.append(feature)
	y.append(label)

X = np.array(X).reshape(-1,57,19,1)

with open("X.pickle","wb") as pickle_out:
	pickle.dump(X,pickle_out)
with open("y.pickle","wb") as pickle_out:
	pickle.dump(y,pickle_out)

print("Done creating the Dataset")	
input()
