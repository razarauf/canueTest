#!/usr/bin/python
"""
Takes the longitude and latitude information from a CSV file and exports mapped data to an HTML file

Author: Raza Rauf <m.razarauf@gmail.com>
"""

import folium, datetime, parse

# scale for various size of markers showing VOC level
RADIUS_SCALE = 15.0;

def main (): 
	firstTime = True
	# store a dictionary with key as day of the week and value as color
	daysToColor = {"MONDAY": "#2ecc71", "TUESDAY":"#3498db", "WEDNESDAY":"#9b59b6", "THURSDAY":"#34495e", "FRIDAY":"#f1c40f", "SATURDAY":"#e67e22", "SUNDAY":"#e74c3c"}

	# call the readFile funtion in the parse script
	listToProcess = parse.readFile ('mergedData.csv')
	for row in listToProcess[1:]: 
		# if it is the first row -> set up the map 
		# starting location is the longitude and latitude of the first row in the data
		if firstTime:	
			map_5 = folium.Map(location=[row[6], row[7]], zoom_start=13)
			firstTime = False

		# check whether the data is valid, column 9 was the flag for valid data
		if int(row[9]) == 1:  
			# temporarily store the date conversion to a day of the week 
			tmpDayFromDate = datetime.datetime.strptime(row[0], '%d/%m/%Y').strftime('%A').upper()

			# create the marker using the day of the week as a popup, color according to the day of the week
			# stored in the dictionary, and radius (VOC level scaled by 15)
			folium.RegularPolygonMarker(location=[row[6], row[7]], popup= tmpDayFromDate,
			                   fill_color=daysToColor[tmpDayFromDate], number_of_sides=4, radius=float(row[8]) * RADIUS_SCALE).add_to(map_5)
	# exports mapped data to an HTML file
	map_5.save('part3.html')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()