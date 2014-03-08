import sys, os, json

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")

(options, args) = parser.parse_args()

def convertCSV(fileName):

	print "Parsing " + fileName

	f = open(fileName, 'rb')

	data = []

	fileKeys = f.readline().lstrip().rstrip().split(',')

	for idx, key in enumerate(fileKeys):
		fileKeys[idx] = fileKeys[idx].replace("\"", "")

	for line in f:
		
		thisLine = line.lstrip().rstrip().split(',')

		if thisLine[0] != '\x00' and thisLine[0] != '':

			thisObject = {}

			for idx, key in enumerate(fileKeys):
				
				thisObject[key] = thisLine[idx].replace("\"", "")

			#print thisObject

			data.append(thisObject);

	nf = open(fileName.replace('.csv', '.json'), 'w')
	nf.write(json.dumps(data))

	print "Parsing complete"


#convertCSV('/Users/seantracey/Downloads/ndpb-high-earners.csv')

convertCSV(args[0])
