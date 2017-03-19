#!/usr/bin/python

import sys, string, csv, numpy


def printRows (listToPrint): 
	""" 
	print out all rows for test
	"""
	for row in listToPrint:
		print ', '.join(row)

def readFile (filename):
	fileList = []
	with open (filename, 'rb') as csvfile: 
		reader = csv.reader(csvfile)
		fileList.extend(reader)
	return fileList

def parseList (filename, listToParse):
	numOfValidRecords = 0
	numOfNegRecords = 0
	numOfMissing = 0
	totalRecords = 0
	aryOfValidRecords = []

	for row in listToParse:
		if float(row[8]) == -999.0: 
			row.append("3")
			numOfMissing = numOfMissing+1
			totalRecords = totalRecords+1
		elif float(row[8]) < 0: 
			row.append("2")
			numOfNegRecords = numOfNegRecords+1
			totalRecords = totalRecords+1
		else: 
			row.append("1")
			numOfValidRecords = numOfValidRecords+1
			totalRecords = totalRecords+1
			aryOfValidRecords.append(float(row[8]))

	printSummaryTable (filename, numOfValidRecords, numOfNegRecords, numOfMissing, totalRecords, aryOfValidRecords)

def printSummaryTable (filename, numOfValidRecords, numOfNegRecords, numOfMissing, totalRecords, aryOfValidRecords): 
	percentOfValidRecords = (numOfValidRecords/float(totalRecords))*100
	percentOfNegative = (numOfNegRecords/float(totalRecords))*100
	percentOfMissing = (numOfMissing/float(totalRecords))*100

	print "filename:" + filename
	print 'Total records: ' + str(totalRecords)
	print ('Number and percent of valid records %i, %.3f %%' % (numOfValidRecords, percentOfValidRecords))
	print ('Number and percent of records with negative values %i, %.3f %%' % (numOfNegRecords, percentOfNegative))
	print ('Number and percent of records with missing values %i, %.3f %%' % (numOfMissing, percentOfMissing))
	print 'Min of valid values: ' + str ( min (aryOfValidRecords))
	print 'Max of valid values: ' + str ( max (aryOfValidRecords))
	# 10% of the valid data lied below: 
	print ('10th percentile of valid values: %.4f' % float ( numpy.percentile(aryOfValidRecords, 10)))
	print ('50th percentile of valid values: %.4f' % float ( numpy.percentile(aryOfValidRecords, 50)))
	print ('90th percentile of valid values: %.4f' % float ( numpy.percentile(aryOfValidRecords, 90)))
	print 

def writeToFile (listToWrite, filename): 
	listToWrite.insert (0, ['Date start:', 'Time start:', 'Date end:', 'Time end:','Time zone:', 'Trip ID','Latitude:','Longitude:','VOC_ppbv:', 'Data flag:'])
	fileWriterHelper (listToWrite, filename, False)


def mergeFiles (listToWrite, filename, fileNumber): 
	if fileNumber == 1: 
		listToWrite.insert (0, ['Date start:', 'Time start:', 'Date end:', 'Time end:','Time zone:', 'Trip ID','Latitude:','Longitude:','VOC_ppbv:', 'Data flag:'])
	fileWriterHelper (listToWrite, filename, True)
	

def fileWriterHelper (listToWrite, filename, append):
	with open (filename, 'wb' if append==False else 'ab') as csvfile: 
		writer = csv.writer(csvfile)
		writer.writerows(listToWrite)

def main (): 
	listOfFiles = ['VOC12015.csv', 'VOC42015.csv', 'VOC82015.csv']
	fileList = []
	numOfValidRecords = 0
	numOfNegRecords = 0
	numOfMissing = 0
	totalRecords = 0
	fileNumber = 0
	aryOfValidRecords = []

	for eachFile in listOfFiles:
		fileNumber = fileNumber + 1
		fileList = readFile(eachFile)
		
		parseList (eachFile, fileList[1:])
		writeToFile (fileList[1:], eachFile)
		mergeFiles (fileList[1:], "mergedData.csv", fileNumber)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()