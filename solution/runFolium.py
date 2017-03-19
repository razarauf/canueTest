#!/usr/bin/python

import folium, datetime, parse

RADIUS_SCALE = 15.0;

def main (): 

	firstTime = True
	daysToColor = {"MONDAY": "#2ecc71", "TUESDAY":"#3498db", "WEDNESDAY":"#9b59b6", "THURSDAY":"#34495e", "FRIDAY":"#f1c40f", "SATURDAY":"#e67e22", "SUNDAY":"#e74c3c"}

	listToProcess = parse.readFile ('mergedData.csv')
	for row in listToProcess[1:]: 
		if firstTime:	
			map_5 = folium.Map(location=[row[6], row[7]], zoom_start=13)
			firstTime = False

		if float(row[8]) != -999.0 and float(row[8]) > 0:  
			tmpDayFromDate = datetime.datetime.strptime(row[0], '%d/%m/%Y').strftime('%A').upper()
			folium.RegularPolygonMarker(location=[row[6], row[7]], popup= tmpDayFromDate,
			                   fill_color=daysToColor[tmpDayFromDate], number_of_sides=4, radius=float(row[8]) * RADIUS_SCALE).add_to(map_5)
	
	map_5.save('part3.html')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()