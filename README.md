Programming Task: The attached csv files contain data collected on three different days, each one contains GPS data from a mobile air quality monitor and associated values for a VOC (volatile organic compound). Please do the following: 

1. Use python to process each file: 
- Simplify the headers  
- Add a data flag column  
- Fill the data flag column with 1 (valid data) 2 (negative value) or 3 (missing value, noted as -999 in the raw data) 

2. Use python to create a summary table with statistic for each of the above input files:  
- Total records 
 - Number and percent of valid records  
- Number and percent of records with negative values 
 - Number and percent of records with missing values  
- Minimum, 10th 50th and 90th percentile, and maximum of valid values 

 3. Append all the files into a single file and visualize using leaflet.js (or another approach of your choice). Use different colours for each day, and different sized symbols to show changes in VOC levels. 
