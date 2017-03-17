#!/usr/bin/python

import sys, string, csv, numpy

def main (): 

	file_list = []
	numOfValidRecords = 0
	numOfNegRecords = 0
	numOfMissing = 0
	totalRecords = 0
	aryOfValidRecords = []
	
	with open ('VOC12015.csv', 'rb') as csvfile: 
		reader = csv.reader(csvfile)
		file_list.extend(reader)
		# for row in reader: 
		# 	print ', '.join(row)

	file_list[0] = ['Date start:', 'Time start:', 'Date end:', 'Time end:','Time zone:','Latitude:','Longitude:','VOC_ppbv:', 'Data flag:']

	for row in file_list:
		if row[8] == 'Data flag:': continue 

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

	# print out all rows for test
	# for row in file_list:
	# 	print ', '.join(row)

	percentOfValidRecords = numOfValidRecords/float(totalRecords)
	percentOfNegative = numOfNegRecords/float(totalRecords)
	percentOfMissing = numOfMissing/float(totalRecords)

	print "filename: test.csv"
	print 'Total records: ' + str(totalRecords)
	print ('Number and percent of valid records %i, %.3f%%' % (numOfValidRecords, percentOfValidRecords))
	print ('Number and percent of valid records %i, %.3f%%' % (numOfNegRecords, percentOfNegative))
	print ('Number and percent of valid records %i, %.3f%%' % (numOfMissing, percentOfMissing))
	print 'Min of valid values: ' + str ( min (aryOfValidRecords))
	print 'Max of valid values: ' + str ( max (aryOfValidRecords))
	print '10th percentile of valid values: ' + str ( numpy.percentile(aryOfValidRecords, 10))
	print '50th percentile of valid values: ' + str ( numpy.percentile(aryOfValidRecords, 50))
	print '90th percentile of valid values: ' + str ( numpy.percentile(aryOfValidRecords, 90))


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()