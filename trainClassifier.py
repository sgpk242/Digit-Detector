# Import the modules
from sklearn import datasets
from sklearn import neighbors
import numpy as np
import pickle

# Load the digits dataset
print "Fetching data..."
dataset = datasets.fetch_mldata("MNIST Original")

# Separate training and testing features and labels
print "Organizing data..."
train_idx = np.array([])
test_idx = np.array([])
start = 0
for x in range(len(dataset.target)):
	if (dataset.target[x] != dataset.target[start]) or (x == len(dataset.target)-1):
		train_idx = np.hstack((train_idx, np.array(range(start,x-11))))
		test_idx = np.hstack((test_idx, np.array(range(x-11,x-1))))
		start = x

print "Fitting data to classifier..."
classifier = neighbors.KNeighborsClassifier()
classifier.fit(dataset.data[train_idx.astype(int)], dataset.target[train_idx.astype(int)])
score = classifier.score(dataset.data[test_idx.astype(int)], dataset.target[test_idx.astype(int)])

print "Accuracy: ", score

print "Saving classifier..."
with open('neighbors_classifier.pkl', 'wb') as file:
	pickle.dump(classifier, file)