# Import modules
from numpy import array
import pickle
from PIL import Image, ImageEnhance

# Get user input for image file names
num = 's'
while not isinstance(num, int):
	num = raw_input("How mang images? ")
	try:
		num = int(num)
	except ValueError:
		continue
files = list()
for x in range(0, num):
	f = raw_input("Image " + str(x+1) + " name: ")
	files.append(f)

# Manipulate images for optimum analysis
print ""
print "Resizing, gray-scaling, and threshholding images..." if num>1 else "Resizing, gray-scaling, and threshholding image..."
images = list()
for x in range(0, num):
	# Gray-scale (and then we only need one channel)
	images.append(Image.open(files[x]).convert("L"))
	images[x] = images[x].split()[0]
	# Intial threshhold based on darkest corner RGB value to adjust for corner shadows
	z = images[x].convert("RGB")
	w = list()
	w.append([z.getpixel((1,1))[0]])
	w.append([z.getpixel((1,z.size[1]-1))[0]])
	w.append([z.getpixel((z.size[0]-1, z.size[1]-1))[0]])
	w.append([z.getpixel((z.size[0]-1, 1))[0]])
	base = min((val, index) for (index, val) in enumerate(w))[0]
	pixelMap = images[x].load()
	for i in range(0, images[x].size[0]):
		for j in range(0, images[x].size[1]):
			if pixelMap[i, j] > base[0] + 5:
				pixelMap[i, j] = 0
			else:
				pixelMap[i, j] = 255
	# Resize
	images[x] = images[x].resize((28, 28), Image.ANTIALIAS)
	# Enhance resized image
	sharpness = ImageEnhance.Sharpness(images[x])
	images[x] = sharpness.enhance(2.0)
	contrast = ImageEnhance.Contrast(images[x])
	images[x] = contrast.enhance(2.0)
	# Threshhold resized image
	pixelMap = images[x].load()
	for i in range(0, 28):
		for j in range(0, 28):
			if pixelMap[i, j] > 10:
				pixelMap[i, j] = 255
			else:
				pixelMap[i, j] = 0
	images[x].show()

# Organize image data
img_data = list()
for x in range(0, num):
	img_data.append(images[x].getdata())
feats = array(img_data)

# Import trained classifier
print "Loading trained classifier..."
with open("neighbors_classifier.pkl", "rb") as file:
	classifier = pickle.load(file)

# Analyze
print "Evaluating images..." if num>1 else "Evaluating image..."
print ""

for x in range(0, num):
	prediction = classifier.predict(feats[x])
	print "Image", str(x+1), "prediction:", int(prediction)

print ""