import urllib.request, sys, os.path

## inName: 	Name of the links file
## outname:	Name of the output files

def downloadFiles(inName, outName):
	outName = "files/spy_image_"

	# Retrieve list of links
	print()
	links = getLinks(inName)
	print()

	getFiles(links, outName)
	
	input("Press Enter to close...")

# Returns an array of links pulled from file
def getLinks(inName):
	if not os.path.isfile(inName):
		print ("File '{}' does not exist or is not accessable.".format(inName))
		return None
	with open(inName) as file:
		links = []
		for link in file:
			links.append(link)
	return links

# Takes in an array of URLs and returns a list of files
def getFiles(links, fileNameStub):
	files = []
	count = 405
	for link in links:
		try:
			count += 1n
			print("Retrieving '{}'".format(link))
			urllib.request.urlretrieve(link, fileNameStub + str(count) + ".jpg")
		except Exception as e:
			print("The file with URL: '{}' could not be retrieved.".format(link))
			print("Error: '{}'".format(e))