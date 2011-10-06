def getInfoBetween(string, currChar, nextChar):
	return string[string.index('%'+currChar)+2:string.index('%'+nextChar)]

inHtml = open('dummypage.html', 'rw+')
metaDescription = '<meta name = "description" content = "'
metaContent = '<meta name = "keywords" content = "'
theTemplate = inHtml.read()

definitions = open('head.js', 'r')

while True:
	curLink = definitions.readline()
	curLink = curLink[0:curLink.index(" ")]
	curWrd = definitions.readline()
	curWrd = curWrd[curWrd.index('"')+1:len(curWrd)-3]
	curDef = definitions.readline()
	curDef = curDef[curDef.index('"')+1:len(curDef)-3]
	title = "<title>Dictionary of Insurance Terms. Define " + curWrd + "</title>\n"
	outFile = open(curLink+'.html', 'w+')
	outData = theTemplate[0:theTemplate.index('%T')] + title + metaDescription
	userContent = "Entry in David Sayles Insurance Services' Dictionary of Insurance Terms that defines " + curWrd + ".  Please look through our dictionary of insurance terms for definitions of Marine Insurance, Marine Cargo Insurance, Property Insurance, Auto Insurance, Casualty Insurance, Personal Liability Insurance, Homeowners Insurance, Life Insurance and any other pertinent insurance questions you have."
	outData += userContent + '">\n' + metaContent + curWrd + ", Insurance, Dictionary, Marine Insurance, Marine Cargo Insurance, Property Insurance, Casualty Insurance, Auto Insurance, Casualty Insurance, Perosnal Liability Insurance, Homeowners Insurance, Life Insurance" + '">\n'
	outData += theTemplate[theTemplate.index('%T')+3:theTemplate.index('%N')] + curWrd
	outData += theTemplate[theTemplate.index('%N')+2:theTemplate.index('%D')] + curDef
	outData += theTemplate[theTemplate.index('%D')+2:len(theTemplate)]
	
	outFile.write(outData)
	outFile.close()
	waste = definitions.readline()
