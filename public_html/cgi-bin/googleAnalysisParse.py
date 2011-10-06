import os

"""
Goes through each folder and replaces the google code with my code
"""

thePath = []

def pushPath(path):
	thePath.append(path)

def popPath():
	thePath.pop()

def replaceAllHtml(root):
	try:
		os.chdir('./'+ root)
		for file in os.listdir('./'):
			if '.html' in file:
				replaceTheCode(file)
			else:
				replaceAllHtml(file)
		os.chdir('../')
	except OSError:
		pass

def replaceTheCode(file):
	inFile = open(file, 'r')
	theFile = inFile.read()
	inFile.close()
	firstHalf = theFile[0:theFile.index("'UA")]
	secondHalf = theFile[theFile.index("'UA")+15:len(theFile)]
	wholeFile = firstHalf + "'UA-25914862-1'" + secondHalf
	outFile = open(file, 'w')
	outFile.write(wholeFile)
	outFile.close()

replaceAllHtml('pages')
