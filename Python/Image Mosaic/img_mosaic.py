from PIL import Image
import urllib.request, sys, os, math

imageSize = 50

def constructComposite(target):
	resolution = 50
	images = getImages()
	imgSize = images[1].width

	compositeSize = imgSize * resolution
	
	target = target.resize((compositeSize, compositeSize), Image.NEAREST)

	outImage = Image.new("RGB", (compositeSize, compositeSize))
	selectedImage = None
	for y in range(0, compositeSize, imgSize):
		for x in range(0, compositeSize, imgSize):
			selectedImage = selectImage(images, target.getpixel((x, y)))
			outImage.paste(selectedImage, (x,y))
			#if selectedImage in images:
			#	images.remove(selectedImage)
		if x % imageSize == 0:
			print("{}% Complete...".format(math.floor((y / compositeSize) * 100)))
	return outImage

# determine which image is appropriate for the current pixel
def selectImage(images, pixelColour):
	threshold = 230
	# Loop over every image and compare to input Pixel Colour
	curAvg = ();
	for image in images:
		curAvg = getAvgColour(image)
		if getMatchScore(curAvg, pixelColour) > threshold:
			return image

	return Image.new("RGB", (imageSize,imageSize))

def getMatchScore(avgColour, pixelColour):
	score = 0

	# FOR all RGB values 
	for index in range(0,3):
		score += 256 - abs(avgColour[index] - pixelColour[index])
	# return average of the differences
	return int(score / 3)

# Pass in a Source Image and a tuple containing the avg RGB values will be returned
def getAvgColour(sourceImage):
	histogram = sourceImage.histogram()
	# r/g/b
	# total pixel count from image histogram
	colour = [0,0,0]
	size = sourceImage.width * sourceImage.height

	# total pixel colour count
	index = 0
	for pixel in histogram:
		if (index < 256):
			colour[0] += index * (pixel / size)
		elif (index < 512):
			colour[1] += (index - 256) * (pixel / size)
		else:
			colour[2] += (index - 512) * (pixel / size)
		index += 1
	return tuple(map(lambda c: math.floor(c), colour))

def showAvgColourComposite(sourceImage, avgColour, padding):
	avgColourImage = Image.new("RGB", (100,100), avgColour)
	compImage = Image.new("RGB", (sourceImage.width + padding * 2, sourceImage.height + avgColourImage.height + padding * 2))
	compImage.paste(sourceImage, (padding, padding))
	compImage.paste(avgColourImage, (padding + int((sourceImage.width / 2) - (avgColourImage.width / 2)), int(1.5 * padding + sourceImage.height)))
	compImage.show()

def getImages():
	images = []
	fileFolder = "files/"
	curImage = None
	for link in os.listdir(fileFolder):
		curImage = Image.open(fileFolder + link).resize((imageSize, imageSize), Image.BILINEAR)
		images.append(curImage)
	return images

def main():
	test()
	if (len(sys.argv) >= 2):
		fileName = sys.argv[1]
		targetImage = Image.open("files/{}".format(fileName))
		#outImage = constructComposite(targetImage)

		outImage = constructComposite(targetImage)
		outImage.save("{}_composite.jpg".format(fileName),"JPEG")
		outImage.show()
		print("*************** Composite complete ******************")
	else:
		print("Please provide an image number")
		input("\nPress any key to exit...")

def test():
	file = Image.open("files/spy_image_100.jpg")
	avg = getAvgColour(file)
	print("Red:{}".format(avg[0]))
	print("Green:{}".format(avg[1]))
	print("Blue:{}".format(avg[2]))
	exit()

main()