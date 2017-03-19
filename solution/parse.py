#!/usr/bin/python
"""
Processes data from a CSV file, merges files, and outputs processed data results

Author: Raza Rauf <m.razarauf@gmail.com>
"""

import sys, string, csv, numpy

def printRows (listToPrint): 
	""" 
	prints out a 2D list

	Parameters
	----------
	listToPrint: List
		A 2D list
	"""
	for row in listToPrint:
		print ', '.join(row)

def readFile (filename):
	""" 
	reads data from a file into a list

	Parameters
	----------
	filename: String
		Name of the file to read

	Returns
	-------
	list
		a 2D list containing file data
	"""

	fileList = []
	# open the file
	with open (filename, 'rb') as csvfile: 
		reader = csv.reader(csvfile)
		# insert the csv file data into a list
		fileList.extend(reader)
	return fileList

def parseList (listToParse):
	""" 
	processes the inputted list

	Parameters
	----------
	listToParse: List
		The list to parse and process
	Returns
	-------
	tuple
		Tuple contains processed data
	"""

	# variables to various processed information
	numOfValidRecords = 0
	numOfNegRecords = 0
	numOfMissing = 0
	totalRecords = 0
	aryOfValidRecords = []

	# process each row individually
	for row in listToParse:
		# check if VOC is missing
		if float(row[8]) == -999.0: 
			row.append("3")
			numOfMissing = numOfMissing+1
			totalRecords = totalRecords+1
		# check if VOC is negative
		elif float(row[8]) < 0: 
			row.append("2")
			numOfNegRecords = numOfNegRecords+1
			totalRecords = totalRecords+1
		# otherwise VOC is valid
		else: 
			row.append("1")
			numOfValidRecords = numOfValidRecords+1
			totalRecords = totalRecords+1
			# store the valid array to process for later
			aryOfValidRecords.append(float(row[8]))

	return (numOfValidRecords, numOfNegRecords, numOfMissing, totalRecords, aryOfValidRecords)

def printSummaryTable (filename, numOfValidRecords, numOfNegRecords, numOfMissing, totalRecords, aryOfValidRecords): 
	""" 
	processes inputted data further and prints out processed results

	Parameters
	----------
	filename: String
		Name of the file to write to 
	numOfValidRecords: Int
		Number of valid records
	numOfNegRecords: Int
		Number of negative records
	numOfMissing: Int
		Number of missing records 
	totalRecords: Int
		Total records 
	aryOfValidRecords: List
		List containing valid records
	"""

	# calculate percentage
	percentOfValidRecords = (numOfValidRecords/float(totalRecords))*100
	percentOfNegative = (numOfNegRecords/float(totalRecords))*100
	percentOfMissing = (numOfMissing/float(totalRecords))*100

	# process and print out formatted data
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
	""" 
	writes data from a list to a file using a helper function

	Parameters
	----------
	listToWrite: List
		a 2D list containing data to write to the file
	filename: String
		Name of the file to write to 
	"""

	# insert the header
	listToWrite.insert (0, ['Date start:', 'Time start:', 'Date end:', 'Time end:','Time zone:', 'Trip ID','Latitude:','Longitude:','VOC_ppbv:', 'Data flag:'])
	# call the helper funtion to process data further
	fileWriterHelper (listToWrite, filename, False)


def mergeFiles (listToWrite, filename, fileNumber): 
	""" 
	merges files together using a helper function

	Parameters
	----------
	listToWrite: List
		a 2D list containing data to write to the file
	filename: String
		Name of the file to write to 
	fileNumber: int
		Number of the file being merged
	"""

	# insert the header if this is the first set of data (first file) being merged
	if fileNumber == 1: 
		listToWrite.insert (0, ['Date start:', 'Time start:', 'Date end:', 'Time end:','Time zone:', 'Trip ID','Latitude:','Longitude:','VOC_ppbv:', 'Data flag:'])
	fileWriterHelper (listToWrite, filename, True)
	

def fileWriterHelper (listToWrite, filename, append):
	""" 
	helper function for writing or appending to file

	Parameters
	----------
	listToWrite: List
		a 2D list containing data to write to the file
	filename: String
		Name of the file to write to 
	append: Boolean
		Flag for whether to append to the end of the file or not
	"""

	# check append flag to append to the file or just write out completely to the file
	with open (filename, 'wb' if append==False else 'ab') as csvfile: 
		writer = csv.writer(csvfile)
		writer.writerows(listToWrite)

def main (): 
	# list of files to process
	listOfFiles = ['VOC12015.csv', 'VOC42015.csv', 'VOC82015.csv']
	
	fileList = []
	fileNumber = 0

	# variables to various processed information
	numOfValidRecords = 0
	numOfNegRecords = 0
	numOfMissing = 0
	totalRecords = 0
	aryOfValidRecords = []

	# process each file individually 
	for eachFile in listOfFiles:
		# counter for how many files have been processed
		fileNumber = fileNumber + 1
		fileList = readFile(eachFile)

		(numOfValidRecords, numOfNegRecords, numOfMissing, totalRecords, aryOfValidRecords) = parseList (fileList[1:])
		printSummaryTable (eachFile, numOfValidRecords, numOfNegRecords, numOfMissing, totalRecords, aryOfValidRecords)
		writeToFile (fileList[1:], eachFile)
		mergeFiles (fileList[1:], "mergedData.csv", fileNumber)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()