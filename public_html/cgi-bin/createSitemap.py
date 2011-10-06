from xml.dom.minidom import Document, parse
import os
import datetime

"""
Creates a sitemap using the current date as the modification date.  Assuming all content is in the 'PAGES' folder, we root at that folder and recurse into all child folders, adding each .html file into the sitemap.  Manual addition of the index file must be made, since that file is a 'cousin' of the pages folder.
"""

class Node:
	def __init__(self, name):
		self.name = name
		self.children = []

	def addChild(self, child):
		self.children.append(child)

def addAllPathsToRoot(rootNode):
	try:
		os.chdir('./'+rootNode.name)
		for p in os.listdir('./'):
			if p[0] != '.':
				rootNode.addChild(Node(p))
				addAllPathsToRoot(rootNode.children[-1])
		os.chdir('../')
	except OSError:
		pass

#create the fileTree
root = Node('pages')
os.chdir('../')
addAllPathsToRoot(root)


date = datetime.date.today()
theDate = str(date.year)+'-'+str(date.month)+'-'+str(date.day)

thePath = []

def pushPath(path):
	thePath.append(path)

def popPath():
	thePath.pop()

def getUrl():
	wholeUrl = "http://www.dsayles.com/"
	for url in thePath:
		wholeUrl+=url+'/'
	return wholeUrl


doc = Document()
xmlRoot = doc.createElement('urlset')
xmlRoot.setAttribute('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
doc.appendChild(xmlRoot)

newXml = doc.createElement('url')
xmlRoot.appendChild(newXml)
theLoc = doc.createElement('loc')
newXml.appendChild(theLoc)
theLocText = doc.createTextNode("http://www.dsayles.com")
theLoc.appendChild(theLocText)
#lastMod = doc.createElement('lastmod')
#newXml.appendChild(lastMod)
#lastModText = doc.createTextNode(theDate)
#lastMod.appendChild(lastModText)
changeFreq = doc.createElement('changefreq')
newXml.appendChild(changeFreq)
changeFreqText = doc.createTextNode('monthly')
changeFreq.appendChild(changeFreqText)


def nodeToXml(currentNode):
	if '.html' in currentNode.name:
		#Create the the URL node
		newXml = doc.createElement('url')
		xmlRoot.appendChild(newXml)
		#Create a location for the URL
		theLoc = doc.createElement('loc')
		newXml.appendChild(theLoc)
		theLocText = doc.createTextNode(getUrl()+currentNode.name)
		theLoc.appendChild(theLocText)
		#Create a lastMod for the URL
		#lastMod = doc.createElement('lastmod')
		#newXml.appendChild(lastMod)
		#lastModText = doc.createTextNode(theDate)
		#lastMod.appendChild(lastModText)
		#Create a changeFrequency for the URL
		changeFreq = doc.createElement('changefreq')
		newXml.appendChild(changeFreq)
		changeFreqText = doc.createTextNode('monthly')
		changeFreq.appendChild(changeFreqText)		
	else:
		pushPath(currentNode.name)
		for child in currentNode.children:
			nodeToXml(child)
		popPath()

nodeToXml(root)

outFile = open('/Users/Dave/Documents/DGSITE/public_html/cgi-bin/Sitemap', 'w')
outFile.write(doc.toprettyxml(indent = '	'))
outFile.close()
