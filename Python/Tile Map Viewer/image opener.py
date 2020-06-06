from PIL import Image
import os, io, sys

# File Name
inFileName = sys.argv[1];
outFileName = sys.argv[2];

byteCount = 0
imgX = 8 * int(sys.argv[3]);

def main():
	# Initialize the file
	with open(inFileName, "rb") as hex_file:
		# construct a byte array using the file
		byteArr = constructByteArray(hex_file)
		byteArr = extractColours(byteArr)

		# The height of the image is the total number of bytes over the width of the image
		constructImage(byteArr, imgX, len(byteArr) / imgX)

def extractColours(data):
	mul = 10

	count = 1
	colours = []
	curBinColour = ""
	
	red = 0
	green = 0
	blue = 0
	
	colour = ()

	for byte in data:
		curBinColour = curBinColour + '{0:08b}'.format(byte)
		if(count % 2 == 0):
			blue = int(curBinColour[1:6], 2)
			green = int(curBinColour[6:11], 2)
			red = int(curBinColour[11:16], 2)
			colours.append((red * mul, green * mul, blue * mul))
			curBinColour = ""
		count += 1
	return colours

def constructByteArray(file):
	arr = []
	for byte in file.read():
			#print('{0:08b}'.format(byte))
			arr.append(byte)
	return arr

def constructImage(data, x, y):
	img = Image.new("RGB", (x, int(y) + 10))
	img.putdata(data)
	img.save(outFileName)

main()