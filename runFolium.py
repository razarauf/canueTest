#!/usr/bin/python

import folium, parse

COLORS =  ["#EE82EE", "#FFFF00", "#FF6347","#4169E1", "#000000"] 

DATES = ["18/09/2015", "23/09/2015", "02/09/2015", "09/09/2015", "17/09/2015"]

def main (): 

	firstTime = True

	listToProcess = parse.readFile ('mergedData.csv')
	for row in listToProcess[1:]: 
		if firstTime:	
			map_5 = folium.Map(location=[row[6], row[7]], zoom_start=13)
			firstTime = False

		if float(row[8]) != -999.0 and float(row[8]) > 0:  
			tmpRadius = float(row[8])/float(0.759368) * 20
			dateAndColorIndex = DATES.index(row[0])

			folium.RegularPolygonMarker(location=[row[6], row[7]], popup=DATES[dateAndColorIndex],
			                   fill_color=COLORS[dateAndColorIndex], number_of_sides=4, radius=tmpRadius).add_to(map_5)

	
	map_5.save('./html/canuex2.html')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()