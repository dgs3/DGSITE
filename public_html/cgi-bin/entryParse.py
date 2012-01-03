import os

newNavlist = "<ul id='navlist'>\n<li id='active'><a href = '../commercial-insurance/commercial-insurance.html'>Commercial</a></li>\n<li><a href = '../personal-insurance/personal-insurance.html'>Personal</a></li>\n<li><a href = '../health-insurance/health-insurance.html'>Health</a></li>\n<li><a href = '../risk-management/risk-management.html'>Risk Management</a></li>\n<li><a href = '../insurance-school/insurance-school.html'>Education</a></li>\n<li><a href = '../insurance-verification/insurance-verification.html'>Insurance Verification</a></li>\n<li><a href = '../news/news.html'>Newsletters</a></li>\n<li><a href = '../insurance-dictionary/insurance-dictionary.html'>Dictionary</a></li>\n<li><a href = '../about/about.html'>About</a></li>\n</ul>\n"


def removeSpaces(string):
	while ' ' in string:
		i = string.index(" ")
		string = string[0:i] + '-' + string[i+1:len(string)]
	while '/' in string:
		i = string.index("/")
		string = string[0:i] + '-' + string[i+1:len(string)]
	return string

urlList = []

theFiles = os.listdir('./')

for file in theFiles:
	#Get file and read contents
	if file != "insurance-dictionary.html" and file!= "entryParse.py":
		inFile = open(file, 'r')
		inString = inFile.read()
		inFile.close()
		#Find start and end indexes of the title
		titleIndexStart = inString.index("keywords") + 21
		titleIndexEnd = inString[titleIndexStart:-1].index(",") + titleIndexStart
		title = inString[titleIndexStart:titleIndexEnd]
		urlList.append(title)
		title = removeSpaces(title)
		#Cut out the old navList and add the new navList
		firstHalf = inString[0:inString.index("<ul id='navlist'>")]
		secondHalf = inString[inString.index("<div id='content'>"):-1]
		outString = firstHalf + newNavlist + secondHalf
		#create outFile
		outFile = open(title+'.html', 'w')
		outFile.write(outString)
		outFile.close()
		os.remove(file)

urlFileList = open('fileList.txt', 'w')
urlString = ""
for url in urlList:
	urlString += '<li><a href = "'+removeSpaces(url)+'.html">'+url+'</a></li>\n'
urlFileList.write(urlString)
urlFileList.close()
