'''

New Data Model Definition

To store the results of the analysis, we can create a new table with the following columns:

year: year for which the statistics are calculated (integer)
weather_station: the code for the weather station (string)
avg_max_temp: average maximum temperature for that year and station in degrees Celsius (float)
avg_min_temp: average minimum temperature for that year and station in degrees Celsius (float)
total_precipitation: total accumulated precipitation for that year and station in centimeters (float)

'''

#Defining table using SQL Syntax

CREATE TABLE weather_statistics (
  year INTEGER,
  weather_station TEXT,
  avg_max_temp REAL,
  avg_min_temp REAL,
  total_precipitation REAL
);

#Data Analysis and Code Storage

import sqlite3

# Connect to the database
conn = sqlite3.connect('weather_data.db')
c = conn.cursor()

# Loop over all years and weather stations
for year in range(1985, 2015):
    for station in ['NE', 'IA', 'IL', 'IN', 'OH']:
        # Initialize variables for calculating statistics
        total_max_temp = 0.0
        total_min_temp = 0.0
        total_precipitation = 0.0
        num_days = 0

        # Open the file for this year and station
        filename = f"wx_data/{station}{year}.txt"
        with open(filename, 'r') as f:
            # Loop over all lines in the file
            for line in f:
                # Parse the line into its components
                date_str, max_temp_str, min_temp_str, precip_str = line.strip().split('\t')
                max_temp = float(max_temp_str) / 10.0
                min_temp = float(min_temp_str) / 10.0
                precip = float(precip_str) / 10.0

                # Ignore missing data
                if max_temp == -999.9 or min_temp == -999.9 or precip == -999.9:
                    continue

                # Accumulate statistics
                total_max_temp += max_temp
                total_min_temp += min_temp
                total_precipitation += precip
                num_days += 1

        # Calculate averages
        if num_days > 0:
            avg_max_temp = total_max_temp / num_days
            avg_min_temp = total_min_temp / num_days
            total_precipitation_cm = total_precipitation / 10.0  # convert to cm
        else:
            avg_max_temp = None
            avg_min_temp = None
            total_precipitation_cm = None

        # Store the results in the database
        c.execute("INSERT INTO weather_statistics VALUES (?, ?, ?, ?, ?)",
                  (year, station, avg_max_temp, avg_min_temp, total_precipitation_cm))

# Commit changes and close connection
conn.commit()
conn.close()
