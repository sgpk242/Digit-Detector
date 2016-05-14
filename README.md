# Digit-Detector
## Python Machine Learning Application

A commmand-line application developed to create a Nearest-Neighbors machine learning classifier that learns how to recognize single digits in images. The classifier is trained using the MNIST database.

* trainClassifier.py downloads the database, trains the classifier, and saves it to the same directory. 

* test.py asks which images you'd like to analyze within the same directoy, displays the enhanced images that the classifier analyzes, and displays the classifier's digit predictions. The algorithm works best for clear images with a lot of contrast (e.g. black writing on white paper with no shadows).

Sample images are provided.

Currently, test.py performs fixed threshholding on the images. Future improvements include implimenting [adaptive threshholding](http://hanzratech.in/2015/01/21/adaptive-thresholding.html) and [recognizing multiple digits in one image](http://hanzratech.in/2015/02/24/handwritten-digit-recognition-using-opencv-sklearn-and-python.html).
