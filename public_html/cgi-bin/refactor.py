import os
#Visit each .html file
#Change the name of comins to commercial_insurance, etc

def doStuff(inFile):
	print 'EDITING: ' + inFile
	file = open(inFile, "r")
	text = file.read()
	file.close()
	textReplace = {'/healins':'/health_insurance', '/comins':'/commercial_insurance', '/persins':'/personal_insurance', '/rm':'/risk_management', '/verif':'/insurance_verification', '/dic':'/insurance_dictionary', '/school':'/insurance_school'}
	for key in textReplace.keys():
		while key in text:
			firstHalf = text[0:text.index(key)]
			secondHalf = text[text.index(key) + len(key):-1]
			text = firstHalf + textReplace[key] + secondHalf
			print textReplace[key]
	file = open(inFile, "w")
	file.write(text)
	file.close()

def htmlSearch(file):
	try:
		os.chdir(file)
		for file in os.listdir('./'):
			htmlSearch(file)
		os.chdir('../')
	except OSError:
		if '.html' in file:
			doStuff(file)

htmlSearch('./index.html')
